# Nexlamp 网站代码安全审计报告

> **审计日期**:2026-06-15
> **审计范围**:`webhook-receiver.js`、`build.js`、`main.js`、`*.html`、`.workbuddy/*.py`、根目录 `*.py` 推送脚本
> **总体结论**:**存在多个高危问题,需要立即处理**,尤其是密钥泄露和 webhook 未授权写入。

---

## 风险概览

| 等级 | 编号 | 问题 | 文件 |
|------|------|------|------|
| 🔴 高危 | #1 | GitHub PAT 硬编码泄露 | `.workbuddy/push_to_github.py`、`.workbuddy/push_via_api.py` |
| 🔴 高危 | #2 | Dev.to API Key / Webhook Secret 硬编码 | `.workbuddy/publish_devto.py`、`publish_devto_0612.py`、`webhook-receiver.js` |
| 🔴 高危 | #3 | Webhook 接口鉴权可绕过,任意文件写入 | `webhook-receiver.js` |
| 🟠 中危 | #4 | Markdown 解析器无 HTML 转义(存储型 XSS) | `build.js` |
| 🟠 中危 | #5 | 响应泄漏服务器绝对路径 | `webhook-receiver.js` |
| 🟠 中危 | #6 | 启动日志打印完整密钥 | `webhook-receiver.js` |
| 🟡 低危 | #7 | CORS 缺省回退到 `*` | `webhook-receiver.js` |
| 🟡 低危 | #8 | 速率限制基于内存,Serverless 失效 | `webhook-receiver.js` |
| 🟡 低危 | #9 | 手机号硬编码 | `webhook-receiver.js` |
| 🟡 低危 | #10 | `marked` 依赖声明但未使用 | `package.json` / `build.js` |

---

## 🔴 高危 #1:GitHub Personal Access Token 硬编码并已泄露

**状态**:**必须立即吊销 token**,仅改代码不够。

### 位置
- `.workbuddy/push_to_github.py:4`
- `.workbuddy/push_via_api.py:5`

### 问题代码
```python
# .workbuddy/push_to_github.py
TOKEN = "REDACTED_PAT"

# .workbuddy/push_via_api.py
TOKEN = 'REDACTED_PAT'
```

### 影响
这是真实的 fine-grained PAT 格式。任何能读到这些文件的人(包括若文件被 commit/push 到公开仓库)都可以:
- 完全控制 `nex-lamp/nexlamp-website` 仓库
- 增删文件、篡改网站内容
- 注入恶意脚本到访客浏览器
- 读取仓库内其他密钥

### 修复步骤
1. **【最高优先级·不可逆】** 到 GitHub → Settings → Developer settings → Personal access tokens **吊销这个 token**。
2. 删除硬编码,改用环境变量或 `git credential`。根目录的 `github_push.py:9` 已用正确做法可参照:
   ```python
   def get_token():
       result = subprocess.run(['git', 'credential', 'fill'],
           input='protocol=https\nhost=github.com\n\n',
           capture_output=True, text=True, encoding='utf-8', cwd=REPO_DIR)
       for line in result.stdout.strip().split('\n'):
           if line.startswith('password='):
               return line.split('=', 1)[1]
       return None
   ```
   或用环境变量:
   ```python
   import os
   TOKEN = os.environ.get("GH_TOKEN")
   if not TOKEN:
       raise SystemExit("ERROR: Set GH_TOKEN environment variable")
   ```
3. **检查 git 历史**:若这些 token 曾被提交,即便现在删掉,历史里依然存在。需用 `git filter-repo` 清理历史并 force push:
   ```bash
   pip install git-filter-repo
   git filter-repo --replace-text <(echo "github_pat_xxx==>REDACTED")
   git push --force
   ```

---

## 🔴 高危 #2:Dev.to API Key / Webhook Secret 硬编码

### 位置
- `.workbuddy/publish_devto.py:4`
- `publish_devto_0612.py:17`
- `webhook-receiver.js:25`

### 问题代码
```python
# .workbuddy/publish_devto.py:4
API_KEY = "REDACTED_DEVTO_KEY"

# publish_devto_0612.py:17
"api-key": "REDACTED_DEVTO_KEY",
```
```javascript
// webhook-receiver.js:25
secret: process.env.WEBHOOK_SECRET || 'NEXLAMP_SECURE_TOKEN_2026',
```

### 影响
- Dev.to API key 可被冒用发布/篡改文章。
- Webhook secret 是默认弱值,可被猜测/爆破。

### 修复
1. **吊销** Dev.to key 并重新生成。
2. 密钥一律走环境变量,**代码里不留默认值**:
   ```javascript
   const secret = process.env.WEBHOOK_SECRET;
   if (!secret) {
       console.error('FATAL: WEBHOOK_SECRET environment variable is required');
       process.exit(1);
   }
   ```
3. 确认 `.gitignore` 包含本地密钥文件:`juejin_cookies.json`、`zhihu_auth_state.json`。

---

## 🔴 高危 #3:Webhook 接口鉴权可绕过(任意文件写入)

**这是最危险的逻辑漏洞,与 #4 形成攻击链。**

### 位置
`webhook-receiver.js:221-244`

### 问题代码
```javascript
// 验证签名 —— 但只在"传了 signature 时"才验证
const signature = req.headers['x-webhook-signature'];
const payload = JSON.stringify(body);

if (signature && !verifySignature(payload, signature, CONFIG.secret)) {
    // 只有传了 signature 才进来
    res.statusCode = 403;
    // ...
    return;
}

// 简单 secret 验证 —— 同样只在"传了 secret 时"才验证
if (body.secret && body.secret !== CONFIG.secret) {
    // 只有传了 body.secret 才进来
    res.statusCode = 403;
    // ...
    return;
}
```

### 攻击方式
两个校验都是**可选的**。攻击者只要:
- **不传** `x-webhook-signature` 请求头
- **不传** `body.secret` 字段

就能**绕过全部鉴权**,直接 POST 请求向 `posts/` 目录写入任意 `.md` 文件。

```bash
# 攻击者只需:
curl -X POST https://yoursite/webhook/new-content \
  -H "Content-Type: application/json" \
  -d '{"title":"恶意文章","body":"<script>盗取cookie</script>"}'
```

### 影响
- 攻击者可写入大量垃圾文章,污染网站。
- **配合 #4 漏洞形成攻击链**:写入带 `<script>` 的 markdown → build.js 构建后 → 访客浏览器执行恶意脚本(窃取 cookie、挂马、钓鱼)。

### 修复
把鉴权改为**强制**——无有效签名一律 403:
```javascript
// 正确做法:必须传且必须通过验证
const signature = req.headers['x-webhook-signature'];
const payload = JSON.stringify(body);

if (!signature) {
    res.statusCode = 403;
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify({ success: false, error: 'Missing signature' }));
    return;
}

if (!verifySignature(payload, signature, CONFIG.secret)) {
    res.statusCode = 403;
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify({ success: false, error: 'Invalid signature' }));
    return;
}

// 删除 body.secret 的 fallback 校验(明文传 secret 本身就不安全)
```

---

## 🟠 中危 #4:Markdown 解析器无 HTML 转义(存储型 XSS)

### 位置
`build.js:33-123`(自实现的 `parseMarkdown`)

### 问题代码
代码块里转义了 `<>`,但**标题、加粗、斜体、段落、表格单元格、图片 alt、链接文本**全部未转义:
```javascript
// build.js:46-49 —— 标题内容 $1 原样进 HTML
html = html.replace(/^#### (.+)$/gm, '<h4>$1</h4>');
html = html.replace(/^### (.+)$/gm, '<h3>$1</h3>');
html = html.replace(/^## (.+)$/gm, '<h2>$1</h2>');
html = html.replace(/^# (.+)$/gm, '<h1>$1</h1>');

// build.js:55-57 —— 加粗/斜体内容未转义
html = html.replace(/\*\*\*(.+?)\*\*\*/g, '<strong><em>$1</em></strong>');
html = html.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');

// build.js:62-67 —— 图片 alt 未转义
html = html.replace(/!\[([^\]]*)\]\(([^)]+)\)/g, function(match, alt, src) {
    return '<img src="' + src + '" alt="' + alt + '" loading="lazy">';
});

// build.js:112-117 —— 段落 block 原样进 HTML
html = html.split('\n\n').map(function (block) {
    // ...
    return '<p>' + block + '</p>';
}).join('\n');
```

### 影响
若 markdown 含 `<img src=x onerror=alert(1)>` 或 `<script>`,会原样输出到 HTML。虽然文章是作者写的,但配合 #3,攻击者可远程注入恶意脚本。

### 修复方案(二选一)

**方案 A(推荐):改用 `marked`**——`package.json` 已声明了 `marked` 依赖却没用上,且 `marked` 默认会转义 HTML。
```javascript
const { marked } = require('marked');
marked.setOptions({ sanitize: false }); // 按需配置

function parseMarkdown(md) {
  return marked.parse(md);
}
```

**方案 B:在自写解析器里加转义函数**
```javascript
function escapeHtml(str) {
    return str
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#39;');
}

// 然后在所有把文本插入 HTML 的地方先调用:
html = html.replace(/^## (.+)$/gm, function(_, t) {
    return '<h2>' + escapeHtml(t) + '</h2>';
});
// ... 其他标题、加粗、斜体、链接、图片 alt 等同理
```

---

## 🟠 中危 #5:响应泄漏服务器绝对路径

### 位置
`webhook-receiver.js:269-272`

### 问题代码
```javascript
res.end(JSON.stringify({
    success: true,
    data: {
        filename: `${filename}.md`,
        path: filePath,   // ← 泄漏完整文件系统路径,如 D:\...\posts\xxx.md
        // ...
    }
}));
```

### 影响
帮助攻击者了解服务器目录结构、操作系统类型,为后续攻击提供情报。

### 修复
只返回文件名,不返回绝对路径:
```javascript
data: {
    filename: `${filename}.md`,
    // path: filePath,  ← 删除这一行
    title: body.title,
    category: body.category || 'General',
    date: body.date || new Date().toISOString().split('T')[0]
}
```

---

## 🟠 中危 #6:启动日志打印完整密钥

### 位置
`webhook-receiver.js:423-433`

### 问题代码
```javascript
console.log(`🔒 Secret: ${CONFIG.secret.substring(0, 8)}...`);

// 生成的 curl 示例里完整包含 secret
console.log(`curl -X POST http://localhost:${port}/webhook/new-content \\
  -d '{
    "secret": "${CONFIG.secret}",   // ← 完整密钥进日志
    ...
  }'`);
```

### 影响
若日志被采集、上传、截图,密钥即泄露。

### 修复
```javascript
console.log(`🔒 Secret: loaded from environment variable`);
// 删除包含完整 secret 的 curl 示例,或改用占位符
console.log(`Example: -d '{"secret": "<YOUR_SECRET>", ...}'`);
```

---

## 🟡 低危 #7:CORS 缺省回退到 `*`

### 位置
`webhook-receiver.js:94-97, 182`

### 问题代码
```javascript
function validateOrigin(origin) {
    if (!origin) return true; // ← 无 Origin 时一律放行(curl、脚本)
    return CONFIG.allowedOrigins.includes(origin);
}
// ...
res.setHeader('Access-Control-Allow-Origin', origin || '*');  // ← 回退到 *
```

### 修复
无 Origin 时不应回退到 `*`,限定到本机或拒绝:
```javascript
res.setHeader('Access-Control-Allow-Origin', origin || 'null');
```

---

## 🟡 低危 #8:速率限制基于内存,Serverless 失效

### 位置
`webhook-receiver.js:46-62`

### 问题
- `requestLog` 是内存 Map,重启即清空。
- Serverless(Vercel/Netlify/Lambda)下每次冷启动都是新实例,Map 不共享,**限流形同虚设**。

### 修复建议
改用 Redis、或固定窗口(基于 IP + 时间桶),或用 Cloudflare/WAF 层限流。

---

## 🟡 低危 #9:手机号硬编码

### 位置
`webhook-receiver.js:41`

### 问题代码
```javascript
phone: '13825496855'
```

### 修复
移到环境变量或配置文件:
```javascript
phone: process.env.COMPANY_PHONE || ''
```

---

## 🟡 低危 #10:`marked` 依赖声明但未使用

### 位置
- `package.json:24`:`"marked": "^12.0.0"`
- `build.js` 却用了自写的解析器

### 修复
既然装了 `marked`,建议直接替换自写解析器,一并解决 #4 的 XSS 问题(见 #4 修复方案 A)。

---

## ✅ 做得好的地方(保持)

- `github_push.py` 用 `git credential fill` 取 token,是正确做法。
- `api_push.py` 用 `os.environ.get`,是正确做法。
- 签名验证用了 `crypto.timingSafeEqual` 防**时序攻击**,这点很专业。
- `sanitizeFilename` 做了目录穿越防护(`path.join` + 字符过滤)。
- `parseBody` 有 10MB payload 限制。
- 前端 `main.js` 干净,无 `eval`/`innerHTML`/`document.write` 等 XSS sink。

---

## 建议修复顺序

| 优先级 | 任务 | 预计工作量 |
|--------|------|-----------|
| **P0 立刻** | 吊销泄露的 GitHub PAT(#1)和 Dev.to key(#2) | 10 分钟 |
| **P0 今天** | 修复 webhook 鉴权(#3),改为强制签名 | 30 分钟 |
| **P1 本周** | 接入 `marked` 替换自写解析器(#4 + #10) | 1 小时 |
| **P1 本周** | 清理日志和响应中的敏感信息(#5、#6) | 20 分钟 |
| **P2 常规** | 修复 CORS 回退(#7)、限流方案(#8)、手机号配置化(#9) | 1 小时 |
| **P2 常规** | 检查 `.gitignore`,审查 git 历史中是否泄露过 token | 30 分钟 |

---

## 附:需要确认的 `.gitignore` 项

确保以下文件/目录**不被提交**到仓库:
```
# 密钥与凭证
juejin_cookies.json
zhihu_auth_state.json
*.env
.env

# 构建产物(按需)
dist/
node_modules/
```

---

*报告生成:Nexlamp 安全审计 | 2026-06-15*

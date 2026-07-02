#!/usr/bin/env python3
"""发布出租屋智能照明文章到知乎"""

import json, urllib.request, http.cookiejar

# Load cookies
with open(r"d:\AI共享文件夹\zhihu_auth_state.json", "r") as f:
    auth_state = json.load(f)

# Build cookie string
cookies = auth_state.get("cookies", [])
cookie_str = "; ".join([f"{c['name']}={c['value']}" for c in cookies])

# Extract xsrf token
xsrf = ""
for c in cookies:
    if c["name"] == "_xsrf":
        xsrf = c["value"]
        break

if not xsrf:
    print("ERROR: No _xsrf cookie found")
    exit(1)

# Article content (知乎中文版)
content = """租房不能改线、不能砸墙、退租还得恢复原状——但你的灯光不该因此妥协。

小红书上的出租屋改造笔记动辄百万浏览——刷墙、换窗帘、买软装，但很少有人提到最影响居住体验的一件事：**灯光**。

出租屋的灯，通常是房东配的廉价吸顶灯——冷白光刺眼、单色温没选择、显色指数低到看不清食物本色。晚上回家打开灯，像走进办公室；关灯刷手机，又漆黑一片。

今天这篇，就是给租房党写的：**最不伤墙、最不伤钱、退租半小时恢复的智能照明改造方案**。

## 租房照明的三个铁律

1. **不动硬装**：不改线路、不打孔、不换开关面板
2. **即插即用**：所有灯具拿回家插上就能用，搬走一拔带走
3. **预算可控**：单个空间改造不超过500元，全屋不超过2000元

## 方案一：磁吸轨道灯 + 涂鸦Zigbee智能射灯

磁吸轨道灯直接3M胶贴在顶面，不需要打孔——退租撕下来不留痕。轨道上灵活插入射灯和筒灯，想加灯就加，想移位置就移。

配上涂鸦Zigbee智能射灯：
- **6档调光**：从5%到100%，深夜2%的微光也够用
- **色温切换**：2700K暖光追剧、4000K中性光做饭、6500K冷白看书
- **场景联动**：一句话"开观影模式"，客厅灯自动降到10%暖光

| 参数 | 出租屋推荐值 | 说明 |
|------|-------------|------|
| 开孔尺寸 | 无需开孔（磁吸轨道） | 租房不能动天花板 |
| 显色指数 | Ra≥90 | 低于90看不清肤色和食物 |
| 功率 | 3-7W/灯 | 小空间够用，电费也省 |
| 控制方式 | 涂鸦Zigbee | 不依赖WiFi，断网也能用 |

## 方案二：智能台灯 + 落地灯组合

- 智能台灯放床头：2700K暖光做睡前阅读，定时30分钟后自动渐灭
- 落地灯放沙发旁：36°光束角打白墙，漫反射出柔和的间接光
- 小夜灯放走廊：2%亮度，半夜起床不刺眼

三盏灯总价不超过300元，体验比出租屋原装吸顶灯好10倍。

## 方案三：灯带贴柜底/镜边

小红书爆款改造最常见的操作——灯带贴在橱柜底部、镜子边缘、书架内侧：
- 背胶粘贴，不伤家具表面
- RGB彩光+白光双模
- 手机一键切换场景

一根1米灯带不到30块，3根贴完厨房和卧室，总共不到100块。

## 场景联动：灯跟着你的生活走

涂鸦App场景设置，租房党建议配3个：

**回家模式**：GPS到家附近/语音"我回来了" → 玄关灯100%暖光 → 客厅灯渐亮70%暖光 → 原吸顶灯关掉

**观影模式**：语音"看电影" → 所有灯降到5%暖光 → 电视区域灯关闭 → 走廊留2%微光

**睡眠模式**：语音"晚安"/定时23:00 → 卧室灯渐降到2%暖光 → 5分钟后关闭 → 走廊小夜灯2%常亮

## Zigbee vs WiFi：租房党选哪个？

| 对比项 | 涂鸦Zigbee | WiFi灯 |
|--------|-----------|---------|
| 网络依赖 | 自组网mesh，断WiFi也能控 | 断WiFi就失联 |
| 响应速度 | <0.5秒 | 1-3秒 |
| 设备容量 | 单网关支持200+灯 | 路由器挂20个设备就卡 |
| 退租迁移 | 网关一拔带走全部设备 | 每个灯需重新配网 |

**结论：租房党选Zigbee，不是因为技术更先进，是因为实际体验更稳。**

## 全屋改造预算

30㎡出租屋（客厅+卧室+厨房）：

| 区域 | 灯具 | 小计 |
|------|------|------|
| 客厅 | 磁吸轨道+3W射灯×3 | ¥225 |
| 卧室 | 磁吸轨道+3W筒灯×2 | ¥190 |
| 厨房 | Zigbee灯带×2 | ¥60 |
| 全屋 | 涂鸦Zigbee网关 | ¥60 |
| **合计** | | **¥535** |

## 退租恢复：30分钟

1. 磁吸轨道：3M胶残留用酒精棉擦，10分钟搞定
2. 灯带：背胶撕下，酒精擦柜面，不留痕迹
3. 网关：拔电源带走，涂鸦App删除设备
4. 原装吸顶灯：开关面板从来没动过

30分钟，房东验收零扣款。

---

*Nexlamp——涂鸦Zigbee智能照明，即插即用，租房也能拥有好灯光。*

*了解更多：nexlamp.com*

![出租屋照明方案对比](https://www.nexlamp.com/blog/images/rental-lighting-plan-comparison.svg)

![场景联动架构](https://www.nexlamp.com/blog/images/rental-scene-automation-flow.svg)

![预算分配示意](https://www.nexlamp.com/blog/images/rental-lighting-budget-chart.svg)"""

# Create article draft
draft_data = json.dumps({
    "title": "出租屋智能照明改造：租房党也能拥有好灯光",
    "content": content,
    "topic_ids": [19551150],  # 智能家居
    "column_id": None
}).encode()

headers = {
    "Content-Type": "application/json",
    "Cookie": cookie_str,
    "x-xsrftoken": xsrf,
    "x-zse-93": "101_3_5.4",
    "x-zse-96": "2.0_",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36",
    "Referer": "https://www.zhihu.com/",
    "Origin": "https://www.zhihu.com"
}

# Step 1: Create draft
req = urllib.request.Request(
    "https://www.zhihu.com/api/v4/articles",
    data=draft_data,
    headers=headers,
    method="POST"
)

try:
    resp = urllib.request.urlopen(req, timeout=15)
    result = json.loads(resp.read())
    article_id = result.get("id")
    print(f"Draft created: ID={article_id}")
    
    # Step 2: Publish
    publish_data = json.dumps({}).encode()
    publish_req = urllib.request.Request(
        f"https://www.zhihu.com/api/v4/articles/{article_id}/publish",
        data=publish_data,
        headers=headers,
        method="PUT"
    )
    
    try:
        resp2 = urllib.request.urlopen(publish_req, timeout=15)
        result2 = json.loads(resp2.read())
        url = result2.get("url", f"https://zhuanlan.zhihu.com/p/{article_id}")
        print(f"SUCCESS: {url}")
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"Publish failed: {e.code} {body[:200]}")
        print(f"Article ID: {article_id} (draft exists)")
except urllib.error.HTTPError as e:
    body = e.read().decode()
    print(f"Draft creation failed: {e.code} {body[:200]}")
except Exception as e:
    print(f"Error: {e}")

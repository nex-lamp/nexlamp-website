# NEXLAMP 项目长期记忆

## 内容发布工作流
- 已启用并更新 `nexlamp-publisher` skill（位于 `C:/Users/yu/.workbuddy/skills/nexlamp-publisher`）
- 该 skill 负责：话题研究 → 中文技术文章 → SVG 配图 + AI 封面 → 网站构建 → Dev.to / LinkedIn / 今日头条分发
- 2026-07-28 完成一次完整发布：
  - 主题：AI自学习照明——灯正在学会"预判"你的下一步
  - Dev.to 英文版发布成功（ID: 4249858）
  - LinkedIn 因 CDP Chrome 未运行跳过
  - 今日头条微头条发布成功（万达案例 + 鬼影接驾 + 技术三件事，口语化）
- 2026-07-29 完成发布：情绪照明/全彩光（RGBWAF）——智能灯光的下一站（ID: 4258607）
- 2026-07-31 完成发布：Li-Fi光通信商用化——当灯变成"路由器"（ID: 4276869）
  - 选题依据: pureLiFi+Askey 4月28日发布全球首款Li-Fi 5G FWA穿窗桥接设备，MWC 2026展示10Gbps
  - 切入角度: 从LED驱动厂商视角看升级机会（恒流源→高速调制+802.11bb协议栈+GaN器件）
- **关键经验**：
  - 2026-07-28 选题策略：AI自适应/自学习照明（启福光万达案例6年省1672万、综合节能率86%）是7月底最热趋势，之前11篇未覆盖，是真正的差异化选题
  - ImageGen水印清除：直接**裁剪法**比paste法更干净利落（裁掉底部70px后resize），paste法会留下floor reflection不自然的痕迹
  - Toutiao CLI 在 Windows 下必须通过 `npx toutiao-ops` 调用，不可直接 `node` 执行 `.bin` 下的 shell 脚本
  - Dev.to API 需带 `User-Agent` + `Accept` headers，body 用标准 `{ "article": { ... } }` 格式
  - Dev.to tags 最多4个，超过返回422错误
  - LinkedIn 发布前必须先 `curl http://127.0.0.1:9222/json/version` 检测 CDP Chrome
- 选题策略：调光/DALI类话题已覆盖9篇，避免重复；AI自学习照明是2026年7月最新差异化方向
- **关键经验（2026-07-31）**：
  - Dev.to POST 后获得 temp-slug 是新现象：之前文章都是POST直接拿正式slug。title 包含 "10 Gbps" / "Routers" 等复杂词可能触发。解决：PUT /api/articles/{id} published:true 即可（published字段仍返回None，是API特性）
  - Li-Fi是真正"刚起步"话题——2026年4月才发布商用产品，比情绪照明（7月8日喊话）更早期
  - 选题切入角度：避开纯技术科普，从LED驱动厂商视角看"Li-Fi对驱动电源的升级需求"——恒流源→高速调制+802.11bb+GaN器件
- **配图规则**：今日头条微头条、LinkedIn、Dev.to 三个平台发文都必须带配图（封面图或文章配图）
- 所有SVG中 & 必须转义为 &amp;
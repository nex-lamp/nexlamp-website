# NEXLAMP 项目长期记忆

## 内容发布工作流
- 已启用并更新 `nexlamp-publisher` skill（位于 `C:/Users/yu/.workbuddy/skills/nexlamp-publisher`）
- 该 skill 负责：话题研究 → 中文技术文章 → SVG 配图 + AI 封面 → 网站构建 → Dev.to / LinkedIn / 今日头条分发
- 2026-07-06 完成一次完整发布：
  - 主题：GB 30255-2026 新国标下智能照明与 LED 驱动电源能效升级
  - Dev.to 英文版发布成功
  - LinkedIn 因 CDP Chrome 未运行跳过
  - 今日头条微头条发布成功
- 关键经验：
  - Toutiao CLI 在 Windows 下必须通过 `npx toutiao-ops` 调用，不可直接 `node` 执行 `.bin` 下的 shell 脚本
  - Dev.to API 需带 `User-Agent` + `Accept` headers，body 用标准 `{ "article": { ... } }` 格式
  - Dev.to tags 最多4个，超过返回422错误
  - LinkedIn 发布前必须先 `curl http://127.0.0.1:9222/json/version` 检测 CDP Chrome
- 选题策略：调光/DALI类话题已覆盖9篇，避免重复；人因照明/节律光是新方向
- **配图规则**：今日头条微头条、LinkedIn、Dev.to 三个平台发文都必须带配图（封面图或文章配图）

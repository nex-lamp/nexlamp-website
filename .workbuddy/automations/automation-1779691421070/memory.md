# Automation Memory

## 2026-06-11: AI智能照明避坑指南
- 选题: AI智能照明5大避坑（协议、驱动、语音控制、布线、AI噱头）
- 文章: posts/2026-06-11-ai-smart-lighting-buying-guide.md (~1400字) + 3 SVG + AI封面(去水印)
- 网站: ✅ build.js 37篇 + GitHub API推送(3302510)
- Dev.to: ✅ https://dev.to/lamp_nex_8cbfdfb5b5aa6b50/5-common-pitfalls-when-buying-ai-smart-lights-in-2026-and-how-to-avoid-them-23cj
- 知乎: ✅ https://zhuanlan.zhihu.com/p/2048384163380835152（publish返回200）
- 掘金: ✅ publish需用draft_id参数（非article_id）
- LinkedIn: ⚠️ CDP Chrome未运行，跳过
- 踩坑: 掘金publish API参数纠正(draft_id vs article_id)；知乎publish返回200即成功

## 2026-06-05: LED驱动电源频闪问题全解析
- 选题: 智能灯频闪/调光闪烁+LED驱动电源兼容性（多平台热搜最高痛点）
- 文章: posts/2026-06-05-led-driver-flicker-guide.md (~1100字) + 3 SVG + PIL合成封面
- 网站: ✅ build.js构建31篇，已在上次commit推送（1acc702）
- Dev.to: ✅ https://dev.to/lamp_nex_8cbfdfb5b5aa6b50/is-your-smart-light-really-flicker-free-a-complete-guide-to-led-driver-flicker-2529
- 知乎: ✅ https://zhuanlan.zhihu.com/p/2046209051172794887（API发布）
- 掘金: ❌ API路由变更(draft/create返回err_no=2)，需更新API端点
- LinkedIn: ⚠️ CDP Chrome未运行，跳过
- 踩坑: ImageGen队列满→PIL合成封面替代；掘金JSON需用json.dump生成而非手写；知乎cookie格式为list需先join

## 2026-06-04: Zigbee网络稳定性排查指南全平台发布
- 选题: Zigbee掉线排查（与上次协议对比互补，用户痛点更直接）
- 文章: posts/2026-06-04-zigbee-troubleshooting.md (~1400字) + 3 SVG + AI封面
- 网站: ✅ build.js→GitHub push（解决merge冲突后成功）
- Dev.to: ✅, 知乎: ✅(API发布成功), 掘金: ✅(需改用mark_content), LinkedIn: ⚠️ CDP Chrome未运行
- 掘金踩坑: draft创建用content字段正常，但发布时需用mark_content更新draft

## 2026-06-03: Zigbee vs Matter vs BLE Mesh 协议对比文章全平台发布
- 选题: 小红书/知乎/Google多平台搜索，热点为"智能灯协议选择"和"全屋智能避坑"
- 文章: 2026-06-03-zigbee-vs-matter-vs-ble-mesh.md (1484字)
- SVG配图: 3张 (协议对比/网络拓扑/决策流程)
- 封面图: AI生成+去水印
- 网站: ✅ 构建成功，GitHub API推送到nexlamp.com
- Dev.to: ✅ https://dev.to/lamp_nex_8cbfdfb5b5aa6b50/smart-lighting-protocol-showdown-zigbee-vs-matter-vs-ble-mesh-2026-4h6j
- 知乎: ⚠️ auth state过期，需重新登录
- 掘金: ⚠️ Cookie过期(403)，需重新登录
- LinkedIn: ⚠️ CDP Chrome未运行，跳过
- 经验: Dev.to API max 4 tags; 掘金Cookie易过期需定期刷新

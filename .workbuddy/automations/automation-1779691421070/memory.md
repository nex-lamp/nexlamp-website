# Automation Memory

## 2026-08-20: UV-C LED杀菌灯商用化拐点——LED驱动电源要过的5道关
- 选题: `ls posts/ | grep -iE "uvc|uv|steri|杀菌|消毒"` 零命中，143篇全新方向。依据: TrendForce 8/14报告点名"多通道调光+UVC杀菌模块导入中高阶产品"；265nm效率突破7.5%(约2倍)/L70 1万→2.5万h；2027水俣公约禁汞令；市场18亿→111亿美元(CAGR 22.4%)；MDPI 2026论文电流降额20-40%寿命翻4倍；工研院8/4发14段AC驱动效率95.18%
- 切入角度: 驱动电源视角拆5道关——效率(WPE 3-10%/驱动自身须≥95%)、电流(±1%恒流/降额20%→L70 x4/DC优于PWM)、热(结温红线50°C/AlN基板4-8K·W⁻¹/NTC必选)、安全(IEC 62471 RG3/人体互锁/剂量监测/认证8-14月)、智能(IoT 18%/剂量上云/多通道共存)
- 文章: posts/2026-08-20-uvc-led-sterilization-driver-5-challenges.md (~1600字) + 英文版 devto-2026-08-20-uvc-led-sterilization-driver.md (9998字符) + 3 SVG(参数对比/降额寿命曲线/5道关架构) + ImageGen封面(裁剪法去水印)
- 网站: ✅ node build.js 144篇 + sitemap.xml 148 URLs + commit 05de9df
- git push: ✅ 最终成功（b64c2cc..05de9df）。前7次网络不通（Empty reply / Failed to connect after 21s / timeout EXIT=124），期间并行推进 Dev.to 发布，收尾重试一次即通。**结论：push 失败不要死磕，先跑完其他平台再回来重试，不必上 GitHub API 兜底**
- rebase 冲突: 远端有新提交导致 `[rejected] fetch first` → `git pull --rebase` 报 unstaged changes（memory.md 未提交）→ 先 commit → rebase 遇 dist/ add/add 冲突 → `git checkout --theirs` + **`git add -f`**（dist/ 在 .gitignore 里，普通 add 会被忽略）→ `GIT_EDITOR=true git rebase --continue` → 重跑 build.js 覆盖
- ⚠️ **不要把 git push 挂后台**: 本次后台 push 跑了 24分55秒才返回，且带的是 rebase 前的旧 ref，回来时报 `! [rejected] non-fast-forward`（虚假告警，前台已推成功，最终 local=remote=5eabd5d）。后台 push 无超时上限 + ref 会过期，push 一律前台跑 `timeout 90 git push`，失败就先做别的事再重试
- Dev.to: ✅ ID 4440241, https://dev.to/lamp_nex_8cbfdfb5b5aa6b50/uv-c-led-sterilization-hits-its-commercial-inflection-point-5-gates-your-led-driver-must-pass-1if9
  - POST 直接拿正式 slug（无 temp-slug），HTTP 200 验证已上线
- LinkedIn: ⏭️ CDP Chrome 未运行（curl EXIT=7），跳过
- 今日头条: ❌ **登录态过期，需老刘扫码重登**（auth check → logged_in: false）。微头条文案已备好（食品加工客户8个月光衰→结温50度红线→电流降20%寿命翻4倍→禁汞令）
- 踩坑:
  - **bash heredoc 写长 Markdown 会被内容引号打断**（unexpected EOF looking for matching '），改用 Python io.open(mode='a') 追加
  - **Write 工具单次内容过大导致参数丢失**（file_path/content 变 undefined），超长文章必须分块写
  - **toutiao-ops 报 page.waitForSelector Timeout ≠ 页面问题**，先 `auth check` 查登录态，能省大量排查时间

## 2026-08-13（第二次执行）: LED天空灯有了国标——T/CALI 0403-2026新标准下驱动电源要过哪几道关
- ⚠️ 本日 12:00 定时任务已跑过一次（发「无网关自组网」，commit 70a6322），本次为手动再次触发，必须先查 posts/ 避免选题撞车
- 初版选题「全光谱人因照明」写完 md + 3 SVG + 封面后发现与 6/24、7/31、8/5 三篇高度重复，全部删除重做（教训：**选题前必须 ls posts/ 做关键词去重**）
- 最终选题: LED天空灯首部团体标准 T/CALI 0403-2026（中照协 8月6日发布，佛山照明牵头），`ls posts/ | grep -iE "sky|天空"` 确认零覆盖
- 切入角度: 从驱动电源视角拆三道门槛——1800K-12000K超宽色温(跨度10200K/须5-7通道混光)、瑞利散射双模块并行(共用PFC+后级独立/色坐标偏差<0.003/同步误差≤10ms)、AI场景控制(DALI DT8插值+参数持久化)
- 文章: posts/2026-08-13-led-sky-light-standard-t-cali-0403-2026.md (~1500字) + 3 SVG(A/B/C分级/色温跨度对比/双模块架构) + PIL合成封面
- 网站: ✅ node build.js 第138篇 + git commit 1873b3f + push origin main（70a6322..1873b3f，前3次网络不通，第4次成功）
- Dev.to: ✅ ID 4384075, https://dev.to/lamp_nex_8cbfdfb5b5aa6b50/china-just-standardized-led-sky-lights-what-tcali-0403-2026-demands-from-your-led-driver-2n53
  - POST 直接拿正式 slug（无 temp-slug）；published 字段返回 None 但页面 HTTP 200，确认已发布
- LinkedIn: ⏭️ CDP Chrome 未运行（HTTP 000），跳过
- 今日头条微头条: ✅ success=true action=published，带封面图（地下咖啡馆天空灯发灰→问题在驱动通道少/恒流精度→8月6号团体标准A/B/C分级）
- 踩坑:
  - **ImageGen 429 额度耗尽**（不是任务数上限，是配额用尽）→ 改用系统 Python PIL 程序化合成封面（天空渐变+太阳光晕+云带+深色科技面板+指标chip），顺带省掉去水印步骤
  - **claude-vision 百炼 API key 已失效**（401 Incorrect API key），图片视觉校验无法用，需老刘更新 key
  - 当前模型 custom-local:ark-code-latest 不支持直接读图
  - SVG 手写易漏 `</text>` 闭合，写完建议 grep 校验
  - git push 前 3 次 Connection reset / 21s 超时，第 4 次自动恢复，遇到别急着走 GitHub API 回退

## 2026-08-10: MicroLED量产拐点——当灯珠小到10微米，LED驱动电源该学"纳秒级切通道"了
- 选题: 多源搜索确认MicroLED量产拐点是8月初最热差异化方向（华灿300323 8月4日答投资者问披露梯度化量产；觉远创智5亿布局光引擎月产10万套；瑞典Polar Light 7月30日完成首批试产；科技三会7月8日半导体照明核心攻关）
- 切入角度: 从LED驱动厂商视角看MicroLED量产带来的三重新挑战——通道密度(8→48-4800路)、PWM频率(1kHz→4-7680Hz)、恒流精度(±3%→±0.5%)；"光引擎"作为芯片级集成新形态
- 之前17篇博客均未覆盖芯片/微显示层面，全新差异化方向
- 文章: posts/2026-08-10-microled-driver-engine-evolution.md (~1500字) + 3 SVG（规格对比/PWM演进/光引擎架构） + AI封面（裁剪法去水印）
- 网站: ✅ node build.js 第133篇 + sitemap.xml 137 URLs + git commit 6819271 + git push origin main成功（f32db42..6819271）
- Dev.to: ✅ ID: 4357001, https://dev.to/lamp_nex_8cbfdfb5b5aa6b50/microled-production-inflection-why-led-drivers-need-to-learn-nanosecond-channel-switching-27en
  - 流程: POST→temp-slug→PUT published:true→正式slug-27en（再次复现temp-slug现象，标题含 "Nanosecond Channel Switching"带引号触发）
- LinkedIn: ⚠️ CDP Chrome未运行（Connection refused），跳过
- 今日头条微头条: ✅ success=true, action=published, url=https://mp.toutiao.com/profile_v4/weitoutiao
  - 文本: ~200字口语化（刷新闻→华灿8月4日MicroLED量产良率90%→觉远创智5亿光引擎→光引擎就是把驱动芯片控制芯片镜片集成一个模组→PWM 1kHz→7kHz，电流精度±3%→±0.5%→同行两种反应→先修桨）
  - 带封面图: --images 参数指定 blog-microled-driver-engine-cover.png
- 踩坑: **build.js cover路径必须以images/开头**（否则图片路径不对，未加 ../../ 前缀）；Dev.to temp-slug 第三次复现，已总结触发规律

## 2026-08-05: 钙钛矿LED量产倒计时——材料革命对LED驱动电源的影响
- 选题: 多源搜索确认钙钛矿LED/透明荧光陶瓷LED材料突破是8月初最新热点（中科大Nature论文6.11 + 前瞻产业研究院8.4报告）
- 之前14篇均未覆盖LED芯片/材料层面的技术革命，是全新差异化方向
- 文章: posts/2026-08-05-perovskite-led-driver-opportunity.md (~1500字) + 3 SVG(参数对比/驱动升级路线/需求全景图) + AI封面(裁剪法去水印)
- 网站: ✅ git commit 6a4daf9 push成功
- Dev.to: ✅ ID: 4317829, https://dev.to/lamp_nex_8cbfdfb5b5aa6b50/perovskite-led-mass-production-countdown-what-led-driver-manufacturers-must-prepare-for-the-1kk4
- LinkedIn: ⚠️ CDP Chrome未运行，跳过
- 今日头条微头条: ✅ published，带封面图
- 踩坑: git add dist/ 被.gitignore阻止，用 git reset HEAD dist/ 后重新commit；toutiao-ops超时自动转入后台60s后完成

## 2026-08-04: Matter over Thread LED驱动——2026年智能照明的"通用语言"
- 选题: 多源搜索确认"Matter over Thread LED驱动"是8月最热差异化方向（IKEA Dubbelkisel无hub驱动/芯科SixG301/雷特Matter生态/2026 Matter放量年）
- 文章: posts/2026-08-04-matter-thread-led-driver-2026.md (~1500字) + 3 SVG + AI封面
- 网站: ✅ build.js 125篇 + sitemap.xml 129 URLs + git push (d704ac9)
- Dev.to: ✅ https://dev.to/lamp_nex_8cbfdfb5b5aa6b50/matter-over-thread-led-drivers-the-2e7d (ID: 4308454)
- LinkedIn: ⚠️ CDP Chrome未运行，跳过
- 今日头条微头条: ✅ 发布成功，带封面图
- 踩坑: Dev.to API返回title截断显示但不影响实际文章完整发布

## 2026-08-03: LED驱动电源涨价潮——50+企业连续5轮调价，10年降价周期终结
- 选题: 多源搜索确认"LED驱动电源涨价潮"是2026年8月最热行业话题（1月19日富满微首发调价→6家头部全员跟进→5月第二轮涨30%+→7月昕诺飞第五轮调价→累计50+企业参与；银+170%/铜+35%/金+70%；AI挤占晶圆产能从30%降至15%；10年降价通道正式终结）
- 之前13篇博客均未覆盖供应链/涨价话题，是真正的差异化选题
- 文章: posts/2026-08-03-led-driver-price-hike-2026.md (~1500字) + 3 SVG(三方夹击图/成本传导路径图/应对策略对比图) + PIL合成封面(ImageGen达到150任务上限，用PIL替代)
- 英文版: posts/devto-2026-08-03-led-driver-price-storm.md
- 网站: ✅ node build.js 123篇 + sitemap.xml (127 URLs) + git push成功
- Dev.to: ✅ https://dev.to/lamp_nex_8cbfdfb5b5aa6b50/led-driver-price-storm-50-companies-5-rounds-of-hikes-and-the-end-of-a-10-year-price-decline-ij9 (ID: 4297317)
  - 本次POST直接拿到正式slug（非temp-slug），published字段仍返回None（API特性）
- LinkedIn: ⚠️ CDP Chrome未运行（127.0.0.1:9222 不通），跳过
- 今日头条微头条: ✅ success=true, action=published, url=https://mp.toutiao.com/profile_v4/weitoutiao
  - 文本: ~200字口语化（朋友圈被涨价通知刷屏→50+企业5轮调价→三个原因银铜AI→做灯具朋友最头疼→锁长协价不换劣质驱动）
  - 带封面图: --images 参数指定 blog-led-driver-price-hike-cover.png
- 踩坑:
  - **重大发现: toutiao-ops 需要加 --headless 参数才能在当前环境运行**（之前不需要，可能是环境变化导致非headless模式浏览器无法启动）
  - ImageGen 达到150任务上限（RequestLimitExceeded.JobNumExceed），用PIL合成封面图替代（与6月5日相同处理）
  - toutiao-ops 支持 --images 参数添加微头条配图（新发现，之前只用--content）
  - PIL需要用系统Python（C:\Users\yu\AppData\Local\Programs\Python\Python313\python.exe），managed Python未安装PIL

## 2026-07-31: 当灯变成"路由器"——Li-Fi光通信如何把LED驱动变成10Gbps接入点
- 选题: 多源搜索确认"Li-Fi光通信商用化"是2026年7月底最热差异化话题（pureLiFi+Askey 4月28日发布全球首款Li-Fi 5G FWA穿窗桥接设备Bridge XC Flex；MWC 2026展示10Gbps Light Antenna架构；演示和测试设备2026上半年向全球电信运营商提供；某知名手机厂旗舰机已嵌入Light Antenna One做内测）
- 之前12篇博客均未覆盖Li-Fi话题，是真正的差异化选题
- 文章: posts/2026-07-31-lifi-led-driver-opportunity.md (~2200字) + 3 SVG(Li-Fi原理调制/Li-Fi vs Wi-Fi频谱对比/LED驱动三层架构演进) + AI封面(裁剪法去水印)
- 英文版: posts/devto-2026-07-31-when-light-bulbs-become-routers-lifi.md (via publish_devto_lifi_2026-07-31.py)
- 网站: ✅ node build.js 119篇 + sitemap.xml (123 URLs)
- Dev.to: ✅ https://dev.to/lamp_nex_8cbfdfb5b5aa6b50/when-light-bulbs-become-routers-how-li-fi-turns-led-drivers-into-10-gbps-access-points-42f6 (ID: 4276869)
  - 流程: POST创建后得到temp-slug → PUT /api/articles/{id} 设为published:true → 获得正式slug-42f6
  - 注意: published字段仍返回None（Dev.to API特性），但URL已是正式slug说明实际已发布
- LinkedIn: ⚠️ CDP Chrome未运行（127.0.0.1:9222 Connection refused），跳过
- 今日头条微头条: ✅ success=true, action=published, url=https://mp.toutiao.com/profile_v4/weitoutiao
  - 文本: 约240字口语化（朋友家Wi-Fi信号差→4月28日Li-Fi新闻→MWC 2026 10Gbps→驱动升级需求→耐利普在评估方案）
- 踩坑: 无重大踩坑，流程顺畅。ImageGen 1216x832 → 裁剪底部70px → resize 1200x750（裁剪法仍然稳定）
- Dev.to POST 后获得 temp-slug 是新现象：之前文章都是POST直接拿正式slug。这次的 title 包含 10 Gbps 和 路由器 等复杂词，可能触发了 temp-slug 流程。解决：PUT /api/articles/{id} published:true 即可。

## 2026-07-29: 情绪照明/全彩光——智能灯光的下一站
- 选题: 多源搜索确认"情绪照明/全彩光"是2026年7月8日广州建博会最新提出（榜威科技张军君"行业三大跃迁：功能→健康→情绪"）
- 之前12篇博客均未覆盖此话题，是真正的差异化选题
- 文章: posts/2026-07-29-emotional-lighting-rgbwaf-future.md (~1700字) + 3 SVG(色域对比/6通道驱动架构/4大场景) + AI封面(去水印)
- 网站: ✅ node build.js 115篇 + sitemap.xml(119 URLs)
- Dev.to: ✅ https://dev.to/lamp_nex_8cbfdfb5b5aa6b50/from-light-to-understanding-why-emotional-lighting-full-spectrum-rgbwaf-is-the-next-station-for-3k1p (ID: 4258607)
- LinkedIn: ⚠️ CDP Chrome未运行（127.0.0.1:9222 Connection refused），跳过
- 今日头条微头条: ✅ (action: published, 口语化220字内，朋友家参观场景+多通道懵圈+情绪照明新周期+耐利普在做这个事)
- 踩坑: 无重大踩坑，流程顺畅。ImageGen 1216x832 → 裁剪70px → resize 1200x750（裁剪法稳定）

## 2026-07-28: AI自学习照明——灯正在学会"预判"你的下一步
- 选题: 多源搜索确认"AI自适应/自学习照明"是2026年7月底最热趋势（启福光万达13家广场案例6年省1672万、综合节能率80-95%；多篇行业分析报道）
- 之前11篇博客均未覆盖此主题，是真正的差异化选题
- 文章: posts/2026-07-28-ai-self-learning-lighting-energy-saving.md (~1400字) + 3 SVG(传统vs AI对比/去中心化自组网/AI学习循环) + AI封面(去水印)
- 英文版: posts/devto-2026-07-28-ai-self-learning-lighting-energy-saving.md
- 网站: ✅ node build.js 112篇 + sitemap.xml(116 URLs)
- Dev.to: ✅ https://dev.to/lamp_nex_8cbfdfb5b5aa6b50/ai-self-learning-lighting-how-your-lights-are-starting-to-predict-your-next-move-2c20 (ID: 4249858)
- LinkedIn: ⚠️ CDP Chrome未运行（127.0.0.1:9222 不通），跳过
- 今日头条微头条: ✅ (action: published, 口语化200字内，万达案例+鬼影接驾+技术三件事)
- 踩坑: ImageGen水印在底部70px范围内且有部分在楼层反射中"半隐"——直接用裁剪法比paste法更干净利落

## 2026-07-20: 毫米波雷达+智能照明——人静灯不灭
- 选题: 多源搜索确认"毫米波雷达人体存在感知"是2026年7月最新热门趋势（Yeelight RadarSense 269元众筹、Aqara FP2 <200元、Philips Hue推mmWave传感器）
- 文章: posts/2026-07-20-mmwave-radar-presence-detection-lighting.md (~1500字) + 3 SVG(PIR对比/频段选型/驱动集成) + AI封面(去水印)
- 英文版: posts/devto-2026-07-20-mmwave-radar-presence-detection-lighting.md
- 网站: ✅ node build.js 99篇 + sitemap.xml(103 URLs)
- Dev.to: ✅ https://dev.to/lamp_nex_8cbfdfb5b5aa6b50/lights-off-while-youre-still-in-the-room-mmwave-radar-ends-smart-lightings-biggest-pain-point-4mmm (ID: 4183624)
- LinkedIn: ⚠️ CDP Chrome未运行（127.0.0.1:9222 不通），跳过
- 今日头条微头条: ✅ (action: published, 口语化200字内)
- 踩坑: Dev.to API published字段始终返回None（API特性），但URL可访问文章实际已发布；无其他重大踩坑

## 2026-07-16: 节律照明——为什么你家的智能灯该学会"看时间"了
- 选题: 多源搜索确认"节律照明/人因照明/Human-Centric Lighting"是2026年7月最热健康照明趋势（新国标强制纳入健康指标、全光谱普及、DALI-2 DT8大规模商用）
- 文章: posts/2026-07-16-human-centric-lighting-rhythm.md (~1500字) + 3 SVG(节律曲线/双通道驱动/应用场景) + AI封面(去水印)
- 英文版: posts/devto-2026-07-16-human-centric-lighting-rhythm.md
- 网站: ✅ node build.js 93篇 + sitemap.xml(97 URLs)
- Dev.to: ✅ https://dev.to/lamp_nex_8cbfdfb5b5aa6b50/human-centric-lighting-why-your-smart-lights-need-to-tell-time-361m (ID: 4154222)
- LinkedIn: ⚠️ CDP Chrome未运行（127.0.0.1:9222 不通），跳过
- 今日头条微头条: ✅ (action: published, 口语化200字内)
- 踩坑: 无重大踩坑，流程顺畅。ImageGen封面图直接生成到标准命名路径。

## 2026-07-14: 第三代半导体杀入LED驱动电源：SiC和GaN到底差别在哪？
- 选题: 多源搜索确认"SiC/GaN进入LED驱动电源"是2026年7月最热技术话题（行业称"SiC进入LED电源的元年"；莱福德/卓闻/麦格米特等已量产）
- 文章: posts/2026-07-14-sic-gan-led-driver-revolution.md (~1500字) + 3 SVG(对比/场景/效率) + AI封面(去水印)
- 英文版: posts/devto-2026-07-14-sic-gan-led-driver-revolution.md
- 网站: ✅ node build.js 86篇 + sitemap.xml(90 URLs)
- Dev.to: ✅ https://dev.to/lamp_nex_8cbfdfb5b5aa6b50/sic-vs-gan-why-the-led-driver-revolution-matters-for-your-next-light-fixture-294e (ID: 4137991)
- LinkedIn: ⚠️ CDP Chrome未运行（127.0.0.1:9222 不通），跳过
- 今日头条微头条: ✅ (action: published, 200字内口语化)
- 踩坑: Dev.to API创建默认是draft→需用PUT /api/articles/{id}再设published:true才拿到正式slug；AI生成图SiC芯片被错写为"SiCK"用表格强化标准写法；水印大区域覆盖法彻底去除

## 2026-07-13: LED驱动电源发热与寿命——智能灯一年变暗的真相
- 选题: 多源搜索确认"LED驱动电源散热/寿命/光衰"是2026年7月热门痛点（行业报告显示智能灯集成传感器后温升8-12°C、光衰从8%升至12%）
- 文章: posts/2026-07-13-led-driver-heat-lifespan.md (~1300字) + 3 SVG + AI封面(去水印)
- 英文版: posts/devto-2026-07-13-led-driver-heat-lifespan.md
- 网站: ✅ node build.js 83篇 + sitemap.xml
- Dev.to: ✅ https://dev.to/lamp_nex_8cbfdfb5b5aa6b50/why-your-smart-lights-get-dim-before-their-first-birthday-the-heat-vs-driver-lifespan-story-ob3
- LinkedIn: ⚠️ CDP Chrome未运行（127.0.0.1:9222 不通），跳过
- 今日头条微头条: ✅
- 踩坑: PowerShell执行策略阻止npx→改用Git Bash成功；AI生成图自带右下角水印→用PIL从上方干净区域取样覆盖后去除


## 2026-07-01: 智能灯待机耗电实测——驱动电源的"偷电"设计
- 选题: 多平台搜索确认"智能灯待机耗电/电费账单"是2026年6月底-7月初热门话题（今日头条/小红书热议）
- 文章: posts/2026-07-01-smart-light-standby-power-truth.md (~1300字) + 3 SVG + AI封面(去水印)
- 网站: ✅ build.js 63篇 + GitHub API推送成功(commit 1ecd8360)
- Dev.to: ✅ https://dev.to/lamp_nex_8cbfdfb5b5aa6b50/smart-light-standby-power-the-20x-gap-nobody-talks-about-2026-guide-2i1f
- 知乎: ✅ https://zhuanlan.zhihu.com/p/2055672536629765669 (API发布成功)
- 掘金: ✅ article_id=7657189484552847366
- LinkedIn: ⚠️ CDP Chrome未运行，跳过
- 今日头条 微头条: ✅
- 今日头条 文章: ✅
- 小红书: ⚠️ xhs-mcp未连接，跳过
- 踩坑: git push被墙失败→改用GitHub API; toutiao-ops article需用--content-file避免命令行超长; 知乎cookie格式为dict直接取cookies字段

## 2026-06-29: 智能灯掉线——驱动电源才是稳定性关键
- 选题: 多平台搜索确认"智能灯掉线/协议选型"是2026年6月最热话题
- 文章: posts/2026-06-29-smart-light-disconnect-driver-fix.md (~1300字) + 3 SVG + AI封面(去水印)
- 网站: ✅ build.js 59篇 + git pull --rebase + git push成功
- Dev.to: ✅ https://dev.to/lamp_nex_8cbfdfb5b5aa6b50/your-smart-lights-keep-disconnecting-stop-blaming-the-protocol-check-the-led-driver-2026-guide-2kc3
- 掘金: ✅ (article_id: 7656380711865253940)
- 知乎: ❌ 账号异常被限制(403 PermissionDeniedException)
- LinkedIn: ⚠️ CDP Chrome未运行，跳过
- 今日头条 微头条: ✅
- 今日头条 文章: ✅
- 小红书: ⚠️ xhs-mcp未连接，跳过
- 踩坑: 掘金create需最少字段(category_id+tag_ids+title+brief_content+mark_content+editor_type)，多字段返回err_no=2；update端点也返回err_no=2；知乎PUT publish生效但账号被限

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

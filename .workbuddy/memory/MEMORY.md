# NEXLAMP 项目长期记忆

## 内容发布工作流
- 已启用并更新 `nexlamp-publisher` skill（位于 `C:/Users/yu/.workbuddy/skills/nexlamp-publisher`）
- 该 skill 负责：话题研究 → 中文技术文章 → SVG 配图 + AI 封面 → 网站构建 → Dev.to / LinkedIn / 今日头条分发
- 2026-08-06 完成发布：AI+植物照明多通道LED驱动——"一电多谱"（ID: 4328861）
  - 选题依据: 崧盛股份8月4日宣布探索AI+LED驱动+植物照明融合；工信部7月31日500零碳工厂；华浩德H1-V六通道获神灯奖；uPowerTek Power Transfer
  - 切入角度: 从LED驱动厂商视角看植物照明多通道架构变革（1+N独立输出/Power Transfer/380-800nm全光谱/AI光配方）
  - 之前16+篇均未覆盖植物照明/园艺照明，全新差异化方向
- 2026-08-13 完成发布：LED天空灯有了国标——T/CALI 0403-2026新标准下驱动电源要过哪几道关（ID: 4384075）
  - 选题依据: 中国照明电器协会8月6日发布首部LED天空灯团体标准T/CALI 0403-2026（佛山照明牵头），A/B/C三级分类+9大核心指标，C类要求1800K-12000K连续可调
  - 切入角度: 从驱动电源视角拆三道门槛——超宽色温需5-7通道混光、瑞利散射双模块并行（共用PFC+后级独立/色坐标偏差<0.003/通道同步误差≤10ms）、AI场景控制（DALI DT8插值+参数持久化）
  - 之前137篇均未覆盖天空灯/模拟天空光，全新差异化方向
  - **教训：同日已跑过一次定时任务，且初版选题「全光谱人因照明」与6/24、7/31、8/5三篇重复，白写一篇。写之前必须 `ls posts/ | grep -iE "关键词"` 去重**
  - ImageGen 429 额度耗尽（区别于150任务上限）→ PIL 程序化合成封面
  - claude-vision 百炼 API key 已失效（401），读图能力待老刘更新 key
- 2026-08-10 完成发布：MicroLED量产拐点——当灯珠小到10微米，LED驱动电源该学"纳秒级切通道"了（ID: 4357001）
  - 选题依据: 华灿光电300323.SZ 8月4日答投资者问披露MicroLED梯度化量产格局（MPD/COW/AR/6英寸产线，量产良率突破90%）；觉远创智5亿元布局广西柳州MicroLED光引擎制造基地，预计2026下半年月产10万套；瑞典Polar Light 7月30日通过芬兰VTT完成首批试产；科技三会7月8日将半导体照明列为核心攻关
  - 切入角度: 从LED驱动厂商视角看MicroLED量产三重新挑战——通道密度8→48-4800路、PWM频率1kHz→4-7680Hz、恒流精度±3%→±0.5%；"光引擎"作为芯片级集成新形态重构驱动电源物理形态
  - 之前17篇博客均未覆盖芯片/微显示层面，全新差异化方向
  - Dev.to temp-slug规律复现：本次标题含 "Nanosecond Channel Switching"（带引号），复现上次Li-Fi的temp-slug现象；流程固定为 POST→temp-slug→PUT published:true→正式slug
- 2026-08-05 完成发布：钙钛矿LED量产倒计时——材料革命对LED驱动电源的影响（ID: 4317829）
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
- 2026-08-05 完成发布：钙钛矿LED量产倒计时——材料革命对LED驱动电源的影响（ID: 4317829）
  - 选题依据: 中科大Nature论文(6.11)钙钛矿LED突破18万小时寿命+116万尼特；中科院全钙钛矿叠层LED EQE45%世界纪录；透明荧光陶瓷LED 5万小时无光衰
  - 切入角度: 从LED驱动厂商视角看新材料对驱动电源的升级需求（±1%精密恒流/kW级大功率/传感器集成）
  - 之前14篇均未覆盖LED芯片/材料层面技术革命，全新差异化方向
- **关键经验（2026-08-03）**：
  - **toutiao-ops 必须加 --headless 参数**：之前不需要，当前环境非headless模式浏览器启动失败（page.goto: Target closed）。命令：`npx toutiao-ops publish weitoutiao --headless --images "<图片路径>" --content "<内容>"`
  - **toutiao-ops 支持 --images 参数**：可为微头条添加配图，逗号分隔多张
  - **ImageGen 限流处理**：达到150任务上限时用PIL合成封面图替代（系统Python有PIL，managed Python没有）
  - Dev.to 本次POST直接拿到正式slug（非temp-slug），说明temp-slug不是必然现象
  - 选题策略：供应链/涨价类话题是8月最热方向，之前13篇未覆盖
- **配图规则**：今日头条微头条、LinkedIn、Dev.to 三个平台发文都必须带配图（封面图或文章配图）
- 所有SVG中 & 必须转义为 &amp;
- **build.js cover 路径关键经验（2026-08-10）**：front matter 中 `cover:` 必须以 `images/` 开头才会自动加 `../../` 前缀；否则直接写文件名会得到 `src="xxx.png"` 导致图片在 dist/blog/ 子目录找不到
- **Dev.to temp-slug 触发条件汇总（2026-08-10）**：标题含引号符号（如 "Nanosecond..."）或大写缩写（如 "10 Gbps"、"5G FWA"）时大概率触发。流程固定：POST→temp-slug→PUT published:true→正式slug，三步不可省略
- **选题策略（持续更新）**：
  - 调光/DALI类话题已覆盖9篇，避免重复
  - **头条读者偏好（老刘2026-08-09确认）**：LED光源技术创新 + 控制技术创新 + 新材料突破类文章阅读量高，读者喜欢看，以后多发
  - 以后优先选题方向：
    ① LED光源技术创新（量子点LED/Micro-LED/OLED照明/新型荧光粉/远红光材料等）
    ② LED控制技术创新（AI驱动/智能调光/多通道控制/传感器融合/边缘计算等）
    ③ 新材料突破（钙钛矿/量子点/GaN-on-Si等）
    ④ 顶级期刊论文解读（Nature/Science/Phys. Rev. Lett.）
    ⑤ 量产里程碑事件
  - 已覆盖话题避免重复，持续寻找全新差异化方向
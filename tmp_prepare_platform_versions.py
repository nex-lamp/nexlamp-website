import os, re, json, requests

base_dir = 'd:/AI共享文件夹/nexlamp-website'
article_path = os.path.join(base_dir, 'posts/2026-07-02-new-lighting-standard-guide.md')
article = open(article_path, 'r').read()

# Extract body (after second ---)
parts = article.split('---', 2)
body = parts[2].strip()

title = '2026智能照明新国标来了！你的灯合格吗？能效+健康+AI情绪照明一文读懂'
print(f'Title: {title}')
print(f'Body length: {len(body)} chars')

# Dev.to English version
devto_title = 'Is Your Smart LED Light Legal? GB 30255-2026 New China Standard Explained'
devto_body = """The Chinese government just released **GB 30255-2026**, a mandatory national standard for LED indoor lighting energy efficiency. Starting 2027, any LED light that doesn't meet the new thresholds effectively can't be sold in China.

## Four Core Changes in the New Standard

### 1. Energy Efficiency Thresholds Raised 25%

| Grade | Old Standard | New Standard | Change |
|-------|-------------|-------------|--------|
| Grade 1 (Best) | 90 Lm/W | 105 Lm/W | +17% |
| Grade 2 | 75 Lm/W | 90 Lm/W | +20% |
| Grade 3 (Minimum) | 60 Lm/W | 75 Lm/W | +25% |

The minimum threshold jumped from 60 to 75 Lm/W. Many cheap low-efficiency LEDs will be eliminated.

### 2. Standby Power <= 0.5W (First Time Regulated)

Smart lights waste power even when "off." WiFi bulbs typically consume 2-5W standby. Zigbee devices? Only 0.1-0.3W. This new rule effectively eliminates WiFi smart lights from the compliant market.

### 3. Color Rendering Index Ra >= 90 Required

Home lighting must now achieve Ra >= 90 (previously just 80). This means full-spectrum LED technology is no longer optional.

### 4. Dimming Performance Now Evaluated

- Minimum dimming depth: <=5% of rated luminous flux
- No visible flicker or stepping during dimming

Cheap PWM dimming with visible flicker? No longer compliant.

## Full Spectrum vs Traditional LED

| Metric | Traditional LED | Full Spectrum LED |
|--------|----------------|-------------------|
| Ra | 80 | 90-98 |
| R9 (Red) | <20 | >=60 |
| Blue Light Peak | Sharp spike | Smooth curve |
| Flicker Risk | High | Very Low |

R9 < 20 means red objects look gray and dull. Full spectrum restores natural color.

## AI Emotional Lighting: From Illumination to Healing

2026's other major trend: smart lighting delivering emotional value, not just brightness. Government policy now explicitly supports "emotional/experiential services" in consumer tech.

- Biological rhythm dimming: Auto-adjust color temperature by time of day
- Scene emotional linking: Movie mode warm, reading mode cool, dining mode cozy
- AI learns your habits: No manual adjustment needed

This requires high-quality dimming drivers. Zigbee constant-current drivers support 0-100% smooth dimming with DALI-2 achieving 0.1% precision.

## 5 Iron Rules for Buying Smart Lights Under the New Standard

1. Energy grade: Only buy Grade 1 or 2 (>=90 Lm/W)
2. Ra value: Home lighting Ra >= 90, premium Ra >= 98
3. Standby power: <=0.5W, choose Zigbee over WiFi
4. Dimming quality: 0-100% smooth, no flicker, no stepping
5. Driver certification: 3C-certified constant-current driver as baseline

NEXLAMP full series: luminous efficacy >=90 Lm/W, Ra >= 90-98, Zigbee standby 0.3W, 3C-certified drivers. Fully compliant under GB 30255-2026.

---

NEXLAMP Technology - Tuya Zigbee Smart Lighting & 3C-Certified LED Drivers. Contact: Mr. Liu +86 13825496855
"""

open(os.path.join(base_dir, 'tmp_publish_newstandard_devto.md'), 'w').write(devto_body)

# Zhihu version
open(os.path.join(base_dir, 'tmp_publish_newstandard_zhihu.md'), 'w').write(body)

# Juejin version
juejin_brief = '2026年LED照明新国标GB 30255-2026解读：光效门槛提升25%、待机功耗≤0.5W、Ra≥90强制、调光性能纳入考核。全光谱+Zigbee方案成为合规最优选。'
open(os.path.join(base_dir, 'tmp_publish_newstandard_juejin.md'), 'w').write(body)
open(os.path.join(base_dir, 'tmp_publish_newstandard_juejin_brief.txt'), 'w').write(juejin_brief)

print(f'Dev.to title: {devto_title}')
print(f'Dev.to body: {len(devto_body)} chars')
print(f'Zhihu content: {len(body)} chars')
print(f'Juejin brief: {len(juejin_brief)} chars ({len(juejin_brief)} chars)')
print('All versions generated')

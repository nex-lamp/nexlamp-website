# Smart Lighting Standby Power: The Hidden Cost Nobody Talks About

> Your lights are off, but your meter is still running. We measured standby consumption across popular smart lighting products — the gap between the best and worst exceeded 20×.

---

## Real-World Measurements (220V, light off)

| Product Type | Standby Power | Annual Cost (20 units, ~$0.07/kWh) |
|-------------|---------------|-----------------------------------|
| Non-smart LED | 0W | $0 |
| Quality Zigbee smart light | 0.2–0.5W | ~$1–3 |
| Wi-Fi smart bulb | 0.8–1.5W | ~$5–10 |
| Low-cost Wi-Fi driver | 2–4W | ~$12–25 |
| Panel with always-on indicator | 3–5W | ~$18–37 |

The issue is not that smart lights consume power — it is that **design quality varies dramatically**, and the worst performers usually also have poor thermal design, shorter lifetime, and flicker issues.

---

## Where Does Standby Power Go?

A "off" smart light still powers three subsystems:

1. **Wireless module** — Zigbee (~0.1–0.3W) vs Wi-Fi (~0.5–1.5W)
2. **LED driver auxiliary supply** — AC-DC conversion losses
3. **Indicator LEDs, sensors, relay hold circuits** — often unnecessary 24/7 loads

The most hidden drain: TRIAC dimmer compatibility circuits that keep a small conduction angle even when the light is commanded off. This can add 0.5–2W and cause "ghost glow".

---

## 4 Selection Rules for Low Standby Power

- Choose **Zigbee or Matter over Thread** instead of Wi-Fi direct
- Verify standby power ≤ 0.5W in the spec sheet
- Look for compliance with **GB/T 31831-2025** (China's smart-lighting standard)
- Disable unnecessary status LEDs and always-on night lights

---

## How NEXLAMP Addresses This

- Zigbee drivers with low-power sleep + fast wake, standby < 0.3W
- Isolated flyback architecture instead of non-isolated / TRIAC designs
- Status LEDs disabled by default
- Full compliance with GB/T 31831-2025 standby and harmonic requirements

Smart lighting should save energy, not quietly consume it 24/7.

---

**Contact:** Mr. Liu, 13825496855  
**Website:** www.nexlamp.com

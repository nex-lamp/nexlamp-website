---
title: "Smart Light Standby Power: The 20× Gap Nobody Talks About (2026 Guide)"
published: true
tags: smarthome, led, iot, energyefficiency, smartlighting
---

Your lights are off. Your electricity meter is still moving. If you run a smart home, this is worth understanding — because **the standby power of smart lights can differ by more than 20×** between well-designed and poorly-designed products.

## What We Measured

Using a basic power meter on 220V mains in the "light off" state:

| Product Type | Standby Power | Annual Cost (20 units) |
|-------------|---------------|----------------------|
| Non-smart LED | 0W | $0 |
| Quality Zigbee smart light | 0.2–0.5W | ~$1–3 |
| Wi-Fi smart bulb | 0.8–1.5W | ~$5–10 |
| Low-cost Wi-Fi driver | 2–4W | ~$12–25 |
| Panel with always-on indicator | 3–5W | ~$18–37 |

At first glance the per-lamp numbers look small. Multiply by 20, 40, or 60 lights across a home, add gateways, routers, cameras and smart speakers, and the baseline load becomes noticeable.

## Where the Power Goes

A smart light in the "off" state still has three active blocks:

1. **Radio module** — Zigbee typically 0.1–0.3W, Wi-Fi 0.5–1.5W.
2. **Driver auxiliary supply** — the AC-DC stage that keeps the MCU and radio alive.
3. **Indicator LEDs / sensors / relay hold** — often cosmetic or over-engineered.

The sneakiest culprit is TRIAC dimmer compatibility. To work with legacy wall dimmers, some drivers keep a tiny conduction angle even when off. That alone can add 0.5–2W and cause a faint "ghost glow".

## How to Avoid Standby Waste

- Prefer **Zigbee or Matter over Thread** over Wi-Fi direct for lighting.
- Check the datasheet for standby power and target ≤ 0.5W.
- Look for compliance with regional standards like **GB/T 31831-2025**.
- Disable unnecessary status LEDs and always-on night lights.
- Consider smart switches with dumb, high-quality LED lamps for the lowest standby load.

## What We Do at NEXLAMP

Our Zigbee drivers use low-power sleep + fast wake, keeping standby under 0.3W. We use isolated flyback topology instead of non-isolated or TRIAC-based designs, and we leave status LEDs off by default. The goal: smart lighting should save energy, not quietly consume it around the clock.

---

If you have measured standby power on your own smart lights, drop your numbers in the comments.

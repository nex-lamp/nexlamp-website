#!/usr/bin/env python3
"""发布出租屋智能照明文章到 Dev.to"""

import json, urllib.request

API_KEY = "cKj98BLMNRcfsJSGGZXN5xaU"

body = """# Rental Apartment Smart Lighting: How Renters Can Finally Have Good Light

Renters face a unique dilemma: you can't change the wiring, you can't drill holes, and when you move out, everything must be restored. But that doesn't mean your lighting should suffer.

Most rental apartments come with cheap ceiling lights — cold white, single color temperature, low CRI that makes food look grey. It feels like walking into an office when you come home at night.

Here are three practical, renter-friendly smart lighting solutions that cost under ¥600 total and can be removed in 30 minutes when you move out.

## Three Golden Rules for Rental Lighting

1. **No hard modifications**: No rewiring, no drilling, no switch panel replacements
2. **Plug and play**: Every light works right out of the box, unplugs when you leave
3. **Budget-friendly**: Under ¥500 per room, under ¥2000 for the whole apartment

## Solution 1: Magnetic Track Lights + Zigbee Smart Spotlights

The MVP of rental lighting upgrades. Magnetic track lights stick to your ceiling with 3M adhesive — no drilling needed. You can freely add or move spotlights and downlights on the track.

With Tuya Zigbee smart spotlights, you get:

- **6-step dimming**: From 5% to 100%, even 2% works as a night light
- **Color temperature switching**: 2700K warm light for movie nights, 4000K neutral for cooking, 6500K cool white for reading
- **Scene automation**: Say "movie mode" and the living room lights drop to 10% warm white

| Parameter | Rental Recommendation | Why |
|-----------|---------------------|-----|
| Installation | Magnetic track (no drilling) | Can't modify ceiling |
| CRI | Ra≥90 | Below 90 = can't see true colors |
| Power | 3-7W per light | Enough for small spaces |
| Control | Tuya Zigbee | Works without WiFi, mesh networking |
| Beam angle | 15°/24°/36° | Spot for accent, flood for ambient |

## Solution 2: Smart Desk Lamp + Floor Lamp Combo

Don't want track lights? A desk lamp + floor lamp combo creates great layered lighting:

- **Smart desk lamp bedside**: 2700K warm light for reading, auto-dim after 30 minutes
- **Floor lamp beside sofa**: 36° beam angle bouncing off white wall = soft indirect light
- **Add a night light**: 2% brightness Zigbee light for the hallway

Three lights, under ¥300 total, but 10x better experience than the landlord's ceiling light.

## Solution 3: LED Strip Lights Under Cabinets

The classic Xiaohongshu rental upgrade — stick LED strips under cabinets, along mirror edges, inside bookshelves:

- Backed adhesive, no damage to surfaces
- RGB + white dual mode
- Phone-controlled scene switching

¥30 per meter, ¥100 covers kitchen + bedroom.

## Zigbee vs WiFi: Which Should Renters Choose?

| Feature | Tuya Zigbee | WiFi Lights |
|---------|-------------|-------------|
| Network dependency | Self-forming mesh, works without WiFi | Offline when WiFi drops |
| Response speed | <0.5 seconds | 1-3 seconds |
| Device capacity | 200+ lights per gateway | Router struggles at 20 devices |
| Move-out migration | Unplug gateway, take everything | Re-pair each light |

**Verdict: Renters should choose Zigbee — not because it's more advanced, but because it actually works reliably.**

## Budget: 30m² Full Apartment Under ¥600

| Area | Fixture | Total |
|------|---------|-------|
| Living room | Track + 3 spotlights | ¥225 |
| Bedroom | Track + 2 downlights | ¥190 |
| Kitchen | LED strips | ¥60 |
| Gateway | Tuya Zigbee | ¥60 |
| **Total** | | **¥535** |

## Move-Out Recovery: 30 Minutes

1. Magnetic tracks: Alcohol wipes remove 3M residue
2. LED strips: Peel off, wipe surfaces
3. Gateway: Unplug and take, delete from app
4. Original ceiling light: Never touched — stays as landlord left it

30 minutes, zero deposit deduction.

---

*Nexlamp — Tuya Zigbee smart lighting, plug and play, renters deserve good light too.*

*Learn more: [nexlamp.com](https://www.nexlamp.com)*"""

article = {
    "article": {
        "title": "Rental Apartment Smart Lighting: How Renters Can Finally Have Good Light",
        "body_markdown": body,
        "tags": ["smartlighting", "zigbee", "smarthome", "iot"],
        "published": True
    }
}

req = urllib.request.Request(
    "https://dev.to/api/articles",
    data=json.dumps(article).encode(),
    headers={
        "api-key": API_KEY,
        "User-Agent": "NexlampPublisher/1.0",
        "Accept": "application/vnd.forem.api.v1+json",
        "Content-Type": "application/json"
    },
    method="POST"
)

try:
    resp = urllib.request.urlopen(req)
    data = json.loads(resp.read())
    print(f"SUCCESS: {data.get('url', 'N/A')}")
    print(f"ID: {data.get('id', 'N/A')}")
except urllib.error.HTTPError as e:
    body = e.read().decode()
    print(f"FAILED: {e.code} {body[:200]}")
except Exception as e:
    print(f"ERROR: {e}")

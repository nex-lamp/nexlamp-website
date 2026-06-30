# Why Your Smart Lights Keep Disconnecting — It's Not the Protocol, It's the Driver

After troubleshooting hundreds of smart lighting installations, a pattern emerges: users blame Zigbee, WiFi, or the gateway when their smart lights go offline. They buy repeaters, swap gateways, even rip out perfectly good Zigbee bulbs for WiFi-direct alternatives — and the problem persists.

**The real culprit is often the LED driver power supply.**

## The Two "Brains" of a Smart Light

Every smart light contains two critical systems:
1. **Communication module** (Zigbee/WiFi/BLE chip) — receives commands
2. **LED driver** — converts 220V/110V AC to constant-current DC for the LEDs

The communication module draws its 3.3V power from the driver's auxiliary winding. When the driver's output is unstable — due to excessive ripple — the Zigbee chip experiences intermittent brownouts. The light still works, but the module "disappears" from the network.

## Three Failure Modes, Three Root Causes

### Type 1: Light works, app shows "offline" → Ripple Interference
Non-isolated drivers with insufficient output filtering capacitors. When grid voltage fluctuates (common in older buildings), the ripple on the DC output disrupts the communication module's power rail.

**Diagnosis**: Other Zigbee devices on the same gateway work perfectly. Only specific lights drop off.
**Fix**: Switch to **isolated drivers** — the transformer provides galvanic isolation, reducing ripple by an order of magnitude.

### Type 2: Flickering and dropouts at low dimming levels → PWM Oscillation
Cheap drivers claiming "0-100% dimming" lose regulation below 10%. When the PWM duty cycle is critically low, poor loop compensation causes low-frequency oscillation on the output.

**Diagnosis**: Stable at high brightness, unstable at low brightness. Film in slow-motion to check for visible flicker.
**Fix**: Select drivers with **≥12-bit PWM resolution** (4096 levels). At 1% brightness, this still gives 40 dimming steps.

### Type 3: All devices drop when a high-power light turns on → EMI Radiation
Substandard drivers skip EMI filtering to cut costs. The inrush current and switching noise conduct through the power line, jamming the 2.4GHz band used by Zigbee.

**Diagnosis**: Turn on a high-wattage ceiling light → sensors/locks disconnect → reproducible.
**Fix**: Only use drivers with **EMC certification** (EN 55015 / GB/T 17743). CCC alone is not enough.

## 2026 Driver Selection Checklist

| Parameter | Requirement | Why |
|-----------|------------|-----|
| Topology | Isolated | Stable under grid variation |
| Output ripple | ≤ ±5% | Prevents module brownout |
| PWM resolution | ≥ 12-bit | Smooth dimming to 1% |
| Certification | EMC (EN 55015) | No interference with other devices |

## Key Takeaway

Before replacing your gateway or switching protocols, check your LED driver. Is it isolated? What's the ripple spec? Does it handle low-end dimming without oscillation?

**Stable smart lighting starts with a quality driver power supply.**

---

*NEXLAMP — Smart Lighting Driver Power Supply Specialist*
*www.nexlamp.com*

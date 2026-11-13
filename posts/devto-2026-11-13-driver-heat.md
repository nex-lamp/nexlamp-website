---
title: Your LED Driver Feels Scorching Hot. "That's Normal" Is Only Half True.
date: 2026-11-13
category: 选型避坑
tags: ["LED driver", "thermal management", "lighting", "LED"]
excerpt: A hot LED driver is normal — until it is not. The judgment line is printed on the housing as Tc, and it has nothing to do with how hot it feels to your hand. Hand threshold (about 70C) and component limit (105C capacitor) sit in different ranges, which is why the argument never resolves. Five heat sources, three symptoms, four questions before ordering.
---

Double 11 orders arrived, the lights went up, and then someone reached into the ceiling void and touched the small plastic box feeding the downlight. It was hot enough to pull a hand back. The seller's answer is almost always the same: "LEDs get warm, that's normal."

That answer is half right. Heat is normal. But "normal" has a ceiling, and the ceiling is printed on the driver's label. Most people just never learn where to look.

## 1. "Hot" is a hand sensation, not a temperature

Your hand is not a thermometer. Roughly: 45 °C feels warm, like a hot bath you can keep your hand in; 55–60 °C you can touch but don't want to hold; past about 65 °C the back of your hand won't stay on it for three seconds; at 75 °C you flinch on contact.

The widely repeated field rule — "if you can hold it for three seconds, it's fine" — works out to a threshold near 70 °C.

Here is the problem: **70 °C is nothing for an electronic component.** A 105 °C / 10,000-hour electrolytic capacitor sitting in a 70 °C case is running at roughly 85–95 °C at the core, still inside its rating.

The temperature at which your hand gives up sits right in the middle of the range where the parts are perfectly comfortable. That mismatch is why this argument never resolves: the customer is asking a component question with a hand, and the seller is answering a hand question with a component standard.

## 2. The number that actually matters: Tc

Look at the driver label. Besides input and output, there is usually a line reading `Tc: 75°C` or `Tc: 80°C`.

Tc is the maximum permitted temperature at a **designated hot spot** on the housing (usually near the MOSFET or the output diode), measured at rated ambient and full load. It exists for two reasons: IEC 61347-1 sets limits on accessible surface temperature — both to prevent burns and to keep the plastic housing from softening — and Tc is the test condition behind the lifetime claim.

So "50,000 hours" never stands alone. The full statement is **50,000 hours @ Tc 75 °C**. Exceed the case temperature and that number is void. As a rule of thumb, every 10 °C of additional case temperature roughly halves electrolytic capacitor life.

The companion figure is Ta, ambient temperature — and almost everyone misreads it. **Ta is not the 22 °C in your living room. It is the air temperature inside the cavity where the driver actually sits.** In a ceiling void, behind a fixture body, or inside a sealed junction box, Ta runs 10–20 °C above room temperature as a matter of course; above 50 °C inside a ceiling on a summer afternoon is unremarkable.

A driver whose lifetime is rated at Ta 40 °C, installed in a 70 °C cavity, doesn't lose a bit of life. It loses most of it.

## 3. Where the heat comes from

**Its own losses.** A 100 W driver at 88% efficiency turns about 12 W into heat. Plastic housing conducts at roughly 0.2 W/(m·K) against aluminium's 205 — three orders of magnitude — so heat cannot spread through the shell; it has to leave through convection off the surface.

**Ambient heat.** Top floors, west-facing walls, rooftop boxes. The cavity starts hot.

**Sealed cavities.** The most common and the most avoidable: insulation batting laid straight over the fixture. Unless the instructions say the luminaire is rated for insulation contact, treat it as not rated.

**Stacking.** Several drivers packed into one spot preheat each other. Individually cool, collectively over temperature.

**Non-conductive mounting.** Laid flat on plasterboard or timber: the back can't conduct, so only the front face is working.

One more that gets forgotten: **dust and grease.** Above a commercial kitchen, in a woodworking shop, on a street-facing shopfront, a layer of dust on the heat-dissipating surface behaves like another blanket and cuts thermal performance by 30–50%.

The practical conclusion: what determines how long a driver lasts is usually not its wattage rating, but where it was put.

## 4. Judge by symptoms, not by touch

Without an IR thermometer, use symptoms. Any one of these three means it is not "normal warmth":

1. **It goes out after a few hours and comes back on once it cools.** Classic thermal protection cycling — output cut, then restored.
2. **Slight brightness wobble, or visible flicker.** Derating, or the step before protection trips. A phone camera at 1/100 s will show banding if it's happening.
3. **Yellowed housing, or a hot-plastic smell.** Thermal ageing of the enclosure has started. Stop using it.

If none of the three is present and it's merely hot to the touch, leave it and observe. Components are designed to run in a range that feels unpleasant to skin.

## 5. Give the heat a path

If the ceiling is already closed, these are still worth doing:

- Move the driver onto a joist or a metal surface; don't lay it flat on plasterboard.
- Leave air around it. Don't cover it with insulation; if it doesn't fit with clearance, it doesn't fit.
- Don't stack drivers. Leave spacing.
- For remote (separate) drivers, put them where a service hatch can reach them — the driver, not the LED board, is what gets replaced in year three.
- Keep 20% power headroom. Drivers running at full load run hottest.
- Keep the driver-to-board lead under 0.5 m with at least 0.5 mm² conductor. Past 1 m, voltage drop and losses become visible — a frequent cause of "the light works but isn't bright enough."

## 6. Four questions before ordering

1. What is the **Tc** of this driver?
2. What **Ta** is the lifetime figure rated at, and at what case temperature?
3. What is the **efficiency**? (Same 100 W: 88% and 93% differ by 5 W of heat.)
4. Is the driver **integrated or remote**, and can it be replaced on its own?

Any legitimate manufacturer can answer all four. If they can't, it's usually not an oversight.

## Two common questions

**I measured 70+ °C on the bench with the light lying on a table. Is it defective?**

Bench testing and installed operation are different thermal paths. On a table there is no aluminium body and no cavity — the conditions are far worse than in a ceiling, so that reading is an upper bound, not a verdict. In July a user bench-tested a recessed spotlight, measured the driver in the seventies, and melted the wax in a decorative candle tin it was resting on. That is a real observation, but an extreme one: once the fixture is installed in plasterboard against an aluminium body, the thermal path is entirely different.

**It's hot, but it has run for a year without failing. Should I do anything?**

If none of the three symptoms are present, no. The margin is designed to sit in the range that feels uncomfortable. The signal to act is a symptom, not a temperature.

---

The reason heat is so easy to misjudge is that it is slow. Nothing fails on the spot. It fails three years later as flicker, five years later as darkness. By then the verdict is "bad quality" — and nobody remembers that the driver spent its first summer under a layer of insulation.

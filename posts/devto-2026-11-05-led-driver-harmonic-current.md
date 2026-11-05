# Your LED Bulbs Might Be Failing a Test You've Never Heard Of: Harmonic Current

On October 29, 2026, Guangdong Provincial Market Regulator released announcement No. 132 of 2026: 15 non-compliant lighting products, 6 found online (3 on Tmall, 1 on Douyin, 1 on JD, 1 on Kuaishou) and 9 offline. The single most frequent failing item? **Harmonic current** — it appeared 11 times, across bulb lamps, panel lights, floodlights, and recessed luminaires.

If you work in lighting, this won't surprise you. If you're a homeowner, smart-home tinkerer, or DIY electrician, it probably should — because the problem isn't confined to one provincial sampling run, and the symptoms can show up in your own walls.

## Not a One-Off

In another Guangdong batch sampled the same month, two well-known-brand ceiling lamps and a pillar bulb also failed on harmonic current. Over in Shandong's provincial sampling, 3 batches of Opple LED bulbs and 1 Panasonic luminaire failed the same item. Opple attributed it to old-standard inventory, which may well be true — but it tells you how long non-compliant stock can linger on shelves and in warehouses.

There's also a quiet industry consensus worth stating plainly: budget retail and online-exclusive models carry higher harmonic risk than engineering-grade products. The cheapest listings on e-commerce platforms are exactly where you should expect the worst current waveforms.

## How Can a Lamp "Work Fine" and Still Fail?

Harmonics measure how cleanly a lamp draws current from the mains. A lamp can light up, dim smoothly, and pass every casual eyeball test while its current draw looks like a mess on an oscilloscope.

Here's the mechanism. An LED driver rectifies the AC mains and buffers it with a bulk capacitor. That capacitor only charges near the voltage peaks, so instead of a smooth sinusoidal current draw, the lamp gulps narrow current pulses. Those pulses are full of odd harmonics — mainly the **3rd harmonic (150 Hz on a 50 Hz grid)** — which do no useful work at all. They just flow back and forth, producing nothing but heat.

## The Standard: GB 17625.1—2022

China's current harmonic limit standard, GB 17625.1—2022 (effective July 1, 2024, a modified adoption of IEC 61000-3-2:2020), classifies lighting as **Class C** with three power tiers:

| Power tier | Requirement |
| --- | --- |
| > 25 W | Relatively strict: 3rd ≤ 27%, 5th ≤ 10%, 7th ≤ 7%, 9th ≤ 5% (as % of fundamental current) |
| 5 W – 25 W | Three alternative requirements; the cheapest option only limits 3rd ≤ 86% and 5th ≤ 61% — no limits on other orders or THD |
| < 5 W | **No emission limits at all** (new in the 2022 edition) |

Now here's the uncomfortable part for residential lighting: home downlights, spotlights, and bulbs are mostly 5–12 W. LED strips and cabinet lights are often under 5 W. In other words, the lighting that fills your ceiling sits exactly in the loosest tiers of the standard — where a driver with no meaningful harmonic control can still "pass."

## Why Your Electrician Should Care: The Neutral Problem

The 3rd harmonic isn't just an abstract compliance checkbox. It's a **triplen** harmonic, which means it adds in the neutral conductor instead of cancelling out. In a three-phase system this is the classic fire-engineering headache. Homes are single-phase, so the picture is simpler but still ugly: more lamps on one circuit means more neutral current, period.

Fire-protection design code notes are blunt about this: ≤ 25 W lamps allowed an 86% 3rd harmonic can push neutral current above **2.5× the phase current**. The neutral — often the same gauge as the phase conductors — becomes the hottest wire in the circuit.

## Symptoms, Layer by Layer

What does excessive harmonic current actually look like in a house? It tends to announce itself in three layers:

**1. Perceivable (annoying):**
- Audio hum or buzz from equipment on the same circuit
- Touch switches acting up
- Motion-sensor lights triggering by themselves

**2. Systemic (worrying):**
- Warm terminals or socket plates on that circuit
- Nuisance breaker or RCD trips with no cause found

**3. Long-term (expensive):**
- Terminal oxidation and insulation aging from chronic overheating — the damage that shows up years later, long after you've forgotten what brand of bulb you installed

## A 3-Step Self-Check

If you suspect your lighting circuit, here's a practical sequence:

1. **Switch off the suspect circuit** and see whether the symptoms vanish. Instant correlation, zero cost.
2. **Count the lamps.** 20+ non-PFC 5–12 W lamps on a single circuit means elevated risk. Spread them across 2–3 circuits.
3. **Have an electrician measure neutral current** with a clamp meter. Neutral current near or above phase current is the telltale signature of triplen harmonics. While they're at it, they should check terminal temperature.

## Two Questions to Ask Before Buying

When you're shopping for downlights or bulbs — especially in bulk for a renovation — ask the seller two things:

**1. What's the driver's power factor — does it have active PFC?**

PF ≥ 0.9 means a serious driver with active power factor correction. A PF around 0.5 means no PFC at all. But be careful: **high PF ≠ low harmonics**. Simple RC filtering can raise the PF while total harmonic distortion stays sky-high. PF is necessary but not sufficient.

**2. Do you have a harmonic current test report per GB 17625.1—2022?**

A vendor who can produce this report on request is a different breed from one who sends you marketing PDFs.

## The 3C Certificate Fine Print

One nuance that trips people up: CCC (3C) certification covers the certified model and its driver scheme. Swapping the driver, the capacitor, or the component supplier requires re-evaluation. Some of the products flagged in this round *did* have valid certificates — the problem was in the batch or materials, not the paperwork. A certificate is a starting point, not a guarantee.

## What It Looks Like from the Factory Floor

Here's the part that explains everything else. A proper active PFC stage — PFC inductor, high-voltage film capacitor, control IC, driver MOS — costs roughly **1–2.5 RMB at volume**. On a downlight retailing for twenty-something RMB, that's pure margin walking out the door.

So cost-cutters have three ways to trim it:

- **No PFC at all** — PF below 0.5, harmonics uncontrolled.
- **Valley-fill pseudo-PFC** — PF around 0.85, but poor THD, and it flickers at low input voltage.
- **PFC without the input common-mode choke** — harmonics barely pass the limit, but conducted EMI (conducted disturbance voltage) fails — which, notably, was also a frequent failing item in this same round of sampling.

That last trick is the clearest proof of the point: cutting one corner pushes the failure to the next invisible item down the checklist.

## The Bottom Line

Harmonic current is a **cost trade-off, not a technical challenge**. Solving it is cheap and well understood. But it's invisible to users, only measurable with instruments, and nobody returns a lamp because of its THD — so in a price war, it's the first thing to be sacrificed.

Two FAQs worth answering directly:

- **My lamp lights and dims normally — can it still fail compliance?** Yes. Harmonic current, conducted disturbance, and energy efficiency are all invisible items. Normal operation proves nothing about compliance.
- **Doesn't buying a big brand guarantee compliance?** No. Well-known brands were flagged in this round and in Shandong's sampling; Opple blamed old-standard inventory. Brand reduces risk; it doesn't eliminate it.

## Key Takeaways

- Harmonic current was the most frequent failing item (11 of 15 products) in Guangdong's Oct 2026 lighting sampling, hitting bulbs, panels, floods, and recessed luminaires alike.
- Most home lighting (5–12 W lamps, < 5 W strips) falls in the loosest tiers of GB 17625.1—2022, where weak drivers can still pass.
- 3rd harmonics add in the neutral: symptoms range from audio hum and ghost-triggering sensors to warm terminals, nuisance trips, and years-later insulation aging.
- Self-check: kill the circuit and watch symptoms, count your lamps (20+ non-PFC units per circuit = spread them out), and clamp-meter the neutral.
- When buying: ask for active PFC (PF ≥ 0.9) and a GB 17625.1—2022 harmonic test report — and remember high PF alone doesn't mean low harmonics.
- Active PFC costs roughly 1–2.5 RMB at volume; its absence is a pricing decision, not a technology gap.

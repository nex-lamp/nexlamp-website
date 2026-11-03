---
title: Your New LED Lamp Buzzes - and It's Almost Never the LED
published: false
tags: lighting, hardware, smarthome, diy
---

Your New LED Lamp Buzzes — and It's Almost Never the LED

Every November, right after Double 11, my inbox turns into a noise-complaint hotline. This year the flood started about two weeks ago, and the question is almost never about wiring anymore. It's this one: "I hung the lamp last night and it won't stop humming. Is it defective? Should I return it?"

I've spent twenty years in the lighting industry, most of it on the driver side of the business, so I've heard this a few thousand times. Here's the short answer I give everyone.

The LED chip cannot make noise.

It's a slab of semiconductor. Current in, photons out. There is no moving part anywhere inside it. Every sound coming out of that fixture originates in the one component you never look at — the driver, that small box tucked into the ceiling plate or the junction box.

And inside that box, things genuinely move. Transformers, inductors, capacitors. When current flows, the magnetic material expands and contracts by microns, thousands of times a second. That's not a defect in itself. It's physics.

The good news: because the mechanism is physical, the noise is diagnosable. Describe the sound accurately and you can usually decide whether to return the lamp without ever opening it.

## Three sounds, three different diseases

| What you hear | Frequency | Character | Usual source |
|---|---|---|---|
| Hum | 50–200 Hz | Low, dull, fridge-like | Core magnetostriction, oscillating with 100 Hz mains ripple |
| Buzzing / crackle | 100 Hz – 5 kHz | Fine, mosquito-like | High output ripple, loose winding, vibrating MLCC capacitors |
| Squeal / whistle | 15–20 kHz | Sharp and piercing; young ears hear it, older ears don't | Switching or PWM dimming frequency landing inside the audible band |

Once you know which row you're in, the rest of the diagnosis is mostly mechanical.

## Root cause 1: the core is breathing

The transformers and inductors in a driver use ferrite cores, and ferrite has a property called magnetostriction — put it in a magnetic field and it changes dimension very slightly.

A switching supply runs somewhere in the 50–150 kHz range, far above the 20 kHz ceiling of human hearing. In theory you should hear nothing at all. And most of the time you don't.

The problem is the second-order ripple. A single-stage PFC design paired with an undersized output capacitor leaves a 100 Hz component riding on the output current. That ripple flows through the output inductor, so the core expands and contracts at 100 Hz — and 100 Hz sits right in the most sensitive region of human hearing. What reaches your ear is a low, steady "hmmmmm."

This also explains the classic complaint: "I can't hear it during the day, but at night it's unbearable."

The sound never changed. During the day it's buried under ambient noise. Close the windows in winter, wait until the house goes quiet, and the masking effect disappears. The hum was always there. You just started hearing it.

## Root cause 2: the housing became a speaker

Here's a pattern I see constantly: the same driver measures perfectly quiet on the bench, then howls the moment it's installed in the fixture.

That's mechanical resonance, not electrical. The vibration energy is tiny, but the aluminum substrate, the thin-walled housing, and the mounting bracket each have their own natural frequency. When the excitation hits one of them, amplitude gets multiplied and the whole housing turns into a speaker cone.

The test is simple. Cut the power, pull the driver out of the fixture, suspend it in free air, and power it back up.

Quiet when suspended, loud when bolted back in? That's structural resonance. A gasket or some damping compound between the driver and the housing usually fixes it. You don't need to return the lamp.

## Root cause 3: dimming dragged the frequency into the audio band

Dimmable fixtures fail this test far more often, for three separate reasons.

PWM frequency set too low. If the driver switches below 20 kHz, the current is being chopped at an audible rate, and the pitch will actually shift as you change brightness. Industry practice is to push the PWM frequency above 8 kHz so it climbs out of the range where the ear is most sensitive.

Mismatched dimmer and driver. Old triac dimmers were designed for incandescent loads. They dim by chopping the AC waveform. An LED driver that can't interpret that chopped waveform will buzz, flicker, and refuse to dim smoothly.

Load too far below the dimmer's minimum. Dimmers specify a minimum load. Swap incandescent for LED and the wattage can fall to a tenth of what the dimmer expects, so it operates in a non-linear region and generates garbage on the line.

The signature symptom of all three: loudest at mid-dim, quiet at full brightness. At mid-range duty cycle the current pulses are at their steepest.

Load matters too. Many drivers are essentially silent from 80% to 100% load and start signing below 20%. Noise has a load curve. That's why two identical lamps in the same room can behave completely differently.

## The four-step check you can do without a multimeter

Step one: locate by ear. Turn off every other appliance in the room and run only this fixture. Is the sound coming from the driver box in the ceiling plate, or from the junction box, or from the switch panel? Driver means driver problem. Junction box means wiring problem.

Step two: swap sockets. If the noise follows the lamp, it's the integrated driver. If the new location is silent, the problem is the original socket or circuit.

Step three: bypass the dimmer. Wire the fixture to a plain switch. If the noise disappears, you have a compatibility problem, and the fix is a different dimmer.

Step four: look for companion symptoms.

| What you observe | Verdict | Action |
|---|---|---|
| Faint hum, steady volume, no flicker, housing at room temperature | Normal electromagnetic vibration | Nothing to fix |
| Volume rising and falling, plus flicker and noticeable heat | Unstable driver, genuine fault | Stop using it, file a warranty claim |
| Sound at the junction box, burning smell | Loose terminal arcing — a real safety hazard | Cut power now, call an electrician |
| Sound changes with dim level, gone at full brightness | Dimmer compatibility | Replace the dimmer |

That third row deserves its own paragraph. A terminal that was never tightened, or oxidized wire, produces tiny arcs under high current. It isn't just noise. Arc heating burns through insulation. If you smell something burning, kill the breaker before you do anything else.

## If you do want a return, write it like an engineer

Most returns stall at "unit tested, functioning normally," because support is checking whether the lamp lights up. Give them something reproducible instead.

Describe frequency, not adjectives. "In a quiet room at night, a continuous low-frequency hum is audible at one meter" beats "it's really loud."

Describe the operating condition. "Most pronounced between 30% and 50% dim, absent at full brightness." That's a compatibility statement, not a subjective impression.

Give them a control. "A second unit of the same model on the same circuit is silent; after swapping positions, the noise follows the lamp."

For context, the quiet-operation threshold used by programs like ENERGY STAR is roughly 30 dB at one meter. That's a number you can cite.

## Four questions worth asking before you buy

Noise performance is essentially locked in at the factory. It is not something you can fix after the fact, so ask before you pay.

Is the driver potted? Epoxy or silicone fill does two things at once — it damps coil vibration and it blocks the path into the housing.

What dimming protocol does it use? 0-10V and DALI are inherently cleaner than triac phase-cut.

Can the driver be replaced on its own? On an integrated fixture, a failed driver means a new fixture.

Is the housing a thin-wall spun or drawn part? Thinner walls resonate more easily.

## Two questions I get constantly

Q: The lamp is brand new and already humming. Is it refurbished stock?

A: Not necessarily. A faint hum on a new fixture is within normal engineering range. What matters is whether the volume is stable, and whether flicker or heat comes with it.

Q: If the driver is potted, is it guaranteed silent?

A: No. Potting addresses vibration transmission and housing resonance. If the ripple is large, or the dimming frequency sits in the audio band, you'll still get noise — it just becomes duller and quieter.

## The one-line version

The lamp isn't noisy because of the LED. It's noisy because a handful of magnetic and capacitive components inside the driver are vibrating, and something in the fixture is amplifying them.

Diagnose by frequency first. Then run the four steps with the power off. Then check for flicker and heat. Flicker plus heat means a fault. Neither means a trade-off.

Your lamp arrived two weeks ago and it's buzzing. Don't rush the return label. Ten minutes of careful listening will tell you more than the product page ever will.

---

Tags: lighting, hardware, smarthome, diy

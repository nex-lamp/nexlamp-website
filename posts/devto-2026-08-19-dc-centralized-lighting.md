# DC Centralized Power: When LED Drivers Go From One-Per-Light to One-Cabinet-Per-District

## The Number That Haunted Contractors for a Decade: 60%

Industry statistics show that **nearly 60% of failures** in outdoor and industrial LED lighting systems are caused by the driver. The reason is straightforward: the traditional architecture is "one driver per light" — every streetlight, every tunnel fixture has an AC-DC driver inside, exposed to wind, rain, and extreme temperatures. For every 10°C above rated temperature, electrolytic capacitor lifespan halves. Add 15-20% AC transmission line loss and the risk of electric shock from deteriorated wiring in storms, and you have a maintenance nightmare.

In August 2026, this problem finally has a systems-level solution.

## Architecture Shift: From "One Per Light" to "One Cabinet Per District"

The core idea of DC centralized power supply is simple: **move AC-DC rectification from each fixture to a central distribution cabinet.**

Traditional: `380V AC → AC-DC driver inside each lamp → LED`

DC Centralized: `380V AC → Central cabinet (AC-DC) → 270V DC bus → DC-DC driver at fixture → LED`

| Dimension | Traditional (AC per lamp) | DC Centralized |
|-----------|--------------------------|----------------|
| AC-DC location | Inside each lamp (failure-prone) | Central cabinet (climate-controlled) |
| Fixture-end driver | AC-DC (complex, fragile) | DC-DC (simple, reliable) |
| Line loss | AC transmission 15-20% | DC transmission <5% |
| Safety | AC leakage = shock risk | DC floating, single-wire contact safe |
| Lamp lifespan | 20,000 hours | 60,000-80,000 hours |
| Maintenance | Climb pole to replace driver | Swap module in cabinet |

## Three Real-World Cases

### Case 1: G7611 Tunnel — 55% Energy Savings, 70% Failure Reduction

The G7611 Expressway Tunnel A (1.8km single bore) completed DC centralized power retrofit in 2026:

- Monthly electricity: ¥39,600 → ¥17,800 (**55% reduction**)
- DC segment driver efficiency improved additional 12%
- Lamp failure rate dropped 70%
- Inspection workload halved
- ROI: 2.3 years

Key design: 48V DC safety extra-low voltage completes AC-DC conversion once; fixtures need no rectification. Bidirectional network cable carries both power and DALI signal, cutting wiring by 40%. Battery backup provides seamless switchover during outages.

### Case 2: Ming Jiuzhou DCICD — 2026 God Lamp Award

Ming Jiuzhou's "LED DC Centralized Drive Dual-Control Lighting System" won the 2026 God Lamp Award. Key innovations:

- Centralized DC supply; fixtures retain only LED modules — **driver failure point eliminated**
- Lamp life: 20,000h → 60,000-80,000h
- 10-year maintenance-free
- DC system physically isolated from ground — eliminates shock risk
- 5G smart pole compatible: each DC output circuit controls lighting 100% while providing 24/7 continuous power to 5G micro-stations, cameras, and weather sensors

### Case 3: NLight Greenhouse — 20% Capex Reduction

Dutch company NLight formally launched its centralized DC power architecture at GreenTech Amsterdam:

- 40kW modules housed in cabinets; DC distributed to RV-series fixtures
- **10-20% capex savings** vs distributed-driver topology
- Fixtures smaller, lighter, simpler
- AC connection points in wet zone reduced from thousands to one cabinet
- Maintenance without entering crop area (critical for pharmaceutical and seed multiplication)

## What This Means for LED Driver Manufacturers

### Product Line Restructuring

Traditional: 1,000 lamps = 1,000 AC-DC drivers. DC centralized: 1-2 central cabinets (40-50kW each) + 1,000 small DC-DC converters. A DC-DC converter is far simpler than AC-DC — no rectifier bridge, no PFC circuit, no EMI filter. Delta's DC-DC drivers exceed 94% efficiency with single-fault detection and remote current adjustment.

### "Solar-Storage-DC-Flexible" Integration

LEDs are inherently DC loads. Traditional AC supply needs "PV DC → inverter AC → driver AC-DC → LED" — three conversions, each losing 8-15%. DC centralized supply goes "PV DC → storage DC → DC bus → LED" — zero unnecessary conversions.

Tunnel project model predicts: by 2030, 1,000 tunnel smart lighting projects replicated nationwide, saving 360 million kWh annually, reducing CO₂ by 300,000 tons.

### Communication Evolution

DC bus supports PLC (power line carrier) for dimming signals, eliminating separate communication cables — 30% cost reduction, 99.9% link availability. Delta reports DC PLC dimming is more stable and precise than traditional AC PLC.

## Where It Fits — and Where It Doesn't

**Good fit:**
- New municipal road lighting (plan cabinet locations upfront)
- Tunnel lighting (long distance, high humidity, high dust)
- Greenhouse horticulture (large scale, wet zones, safety-critical)
- Industrial parks / smart campuses (combine with 5G poles, PV storage)
- Data centers and telecom base stations (already have DC infrastructure)

**Not a good fit:**
- Legacy building retrofits (no DC distribution backbone)
- Residential lighting (low per-fixture power, centralized supply not cost-effective)
- Ultra-long-distance outdoor lighting (DC voltage drop; need 270V+ bus voltage)

## The Bottom Line

DC centralized power supply isn't a "new bulb" — it's a power architecture restructuring. For LED driver manufacturers:

1. **R&D teams need DC-DC expertise**, not just AC-DC
2. **Product form shifts from "lamp accessory" to "infrastructure"** — higher unit value, changing shipment structure
3. **Natural fit with renewables** — PV + storage + lighting integration is deterministic

Ming Jiuzhou won the God Lamp Award. Delta is shipping. NLight is in mass production. In 2026, DC centralized power moved from concept to engineering validation. The next 2-3 years will see scaled adoption in new municipal projects.

Those who move first capture the infrastructure dividend.

---

*NEXLAMP specializes in Tuya Zigbee/Matter smart lighting systems with full-power-range LED drivers (7W-400W) and control solutions. [www.nexlamp.com](https://www.nexlamp.com)*

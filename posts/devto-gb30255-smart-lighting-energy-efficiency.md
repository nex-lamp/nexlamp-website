On March 18, 2026, China released GB 30255-2026, the new national standard for energy efficiency of indoor LED lighting products. It will replace GB 30255-2019 and take effect on September 1, 2027. For anyone building smart lighting—especially Zigbee and Tuya-based solutions—this is not a distant compliance memo. It directly affects product definition, LED driver selection, cost accounting, and market access.

Here is a practical breakdown of what changed, what it means for LED drivers, and how to prepare.

## Three major changes in GB 30255-2026

### 1. Smart lighting is now inside the scope

The previous standard covered conventional LED downlights, spotlights, tubes, and high-bay lamps. The new version explicitly adds **dimming, color-tuning, and sensor-controlled** products to the energy-efficiency evaluation. That Zigbee dimmable downlight, Bluetooth tunable-white strip, or PIR ceiling light you are shipping now needs to be classified, tested, and labeled.

### 2. Energy-efficiency grades are tighter and more granular

The standard keeps the 1–3 grade system but raises the bar at every level. Grade 3 is no longer a free pass; low-efficacy products will be blocked. Grade 2 is much stricter, so products marketed as “energy-saving” must actually earn the label. The standard also splits requirements by beam angle, power band, and correlated color temperature, which makes “model-swapping for certification” much harder.

### 3. Standby power is regulated for the first time

This is the headline feature. Products with a standby mode must meet a power-consumption limit. The idea is simple: energy saving should not stop when the light is off. For smart lights that keep Wi-Fi, Bluetooth, or Zigbee radios alive 24/7, this rule forces a real look at idle consumption.

> Note: The exact limit depends on product type and clause. The key point is that standby power is no longer an afterthought—it is a compliance gate.

## What it means for LED drivers

In a smart luminaire, the driver sits at the intersection of “light on” and “network always on.” The new standard’s pressure lands here first.

### Standby power must be re-evaluated

Many Zigbee lights keep the driver board and radio module powered even when the lamp looks off. A cheap non-isolated driver plus a power-hungry radio can easily idle above 1 W. Under the new standard, that design is no longer viable.

**Practical fix:** Prefer isolated drivers with low-standby design, or split the high-voltage driver from the low-voltage control rail. Some newer Tuya modules support deep-sleep plus fast-wake; use them with a low-quiescent LDO and a relay architecture to keep standby draw low.

### Dimming efficiency must stay flat

Dimming is not just lowering voltage. A good driver must maintain high efficiency across PWM duty cycles and mixed color-temperature loads. The new standard considers smart-control products for energy-efficiency correction, so you cannot pass certification at 100% brightness and then ship a product that collapses at 20%.

**Practical fix:** Ask suppliers for the efficiency curve and look specifically at the 50% and 20% load points. A quality constant-current driver typically stays above 85% across the full range; a poor one falls off a cliff at low brightness.

### High CRI and glare control get a bonus

The standard gives an energy-efficiency correction factor to high-quality products: high CRI (Ra ≥ 80), low glare (UGR control), and smart regulation. The message is clear: the goal is not merely “use less power,” but “use less power while keeping light quality high.” For premium brands, this is an opportunity, not a burden.

### Ra and R9 become hard gates

The standard sets Ra and R9 requirements by product category. For downlights, desk lamps, and spotlights where color matters, you must verify the LED + driver combination, not just the bare diode. A driver with poor current ripple or color consistency can fail certification even if the LED chip looks good on paper.

## Five practical steps to prepare

1. **Scan your product line.** Classify every SKU by whether it includes dimming, color tuning, sensors, or networking. Many smart products that were previously outside the standard now fall inside it.

2. **Run pre-tests early.** Send key products to a certified lab now, not in mid-2027. Measure efficacy, standby power, efficiency at partial load, Ra, and R9. Use the data to drive design changes.

3. **Upgrade your driver spec sheet.** Beyond voltage, current, and wattage, add:
   - standby power (< 0.3 W is a comfortable target to leave headroom for the radio)
   - full-load efficiency curve
   - dimming compatibility (PWM depth, dimming curve, minimum stable brightness)
   - EMI class, because certification is increasingly holistic

4. **Split power architecture for always-on radios.** For Wi-Fi lamps, use a relay to cut the main LED circuit and feed the module separately. For Zigbee and Bluetooth Mesh, keep the module always-on but put the driver in a low-power standby state.

5. **Use the transition window wisely.** The energy-efficiency labeling rule also takes effect on September 1, 2027, but products manufactured or imported before that date can delay new labeling until September 1, 2029. Plan your inventory and new-product launches around this 25-month buffer.

## Conclusion: turn compliance into a competitive edge

GB 30255-2026 moves smart lighting from a feature race into a compliance race. For teams like NEXLAMP that focus on Tuya Zigbee solutions, this is both pressure and opportunity. The companies that redesign drivers, re-evaluate standby power, and clean up certification workflows early will have fewer surprises and more wins after September 2027.

The standard will not wait. But prepared teams will outrun it.

---

*If you have questions about GB 30255-2026 compliance paths or LED driver selection, feel free to ask in the comments.*

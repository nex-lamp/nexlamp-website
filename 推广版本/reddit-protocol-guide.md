**Title**: I've deployed 300+ smart lighting projects. Here's my honest breakdown of Zigbee vs BLE Mesh vs Wi-Fi vs DALI-2.

Hey r/smarthome and r/homeautomation,

After working on hundreds of smart lighting installations (from single-room retrofits to 300-node hotel projects), I wanted to share a practical protocol comparison that I wish someone had shown me years ago.

**TL;DR:**

| Use case | Best protocol | Why |
|----------|--------------|-----|
| 5-10 lights, rental | Wi-Fi | No hub needed |
| Whole home, 20-50 lights | Bluetooth Mesh | Phone direct, Xiaomi/HomeKit |
| Hotel/office, 100+ lights | Zigbee | Self-healing Mesh |
| Museum/luxury retail | DALI-2 | 0.1% precision dimming |

**The details:**

**Zigbee** (IEEE 802.15.4, 2.4GHz, 250kbps): The most battle-tested for commercial. Its Mesh is self-organizing and self-healing — one node goes down, the network routes around it. I've seen 200+ node Zigbee networks run rock-stable for years. Biggest pain point: Zigbee 3.0 unified the standard, but tons of devices on the market still use Zigbee 1.2 or proprietary flavors. Cross-brand compatibility is still a headache.

**Bluetooth Mesh** (BLE 5.0+): Won the consumer market for a reason — phone direct control, no gateway needed. Xiaomi and Apple both push this heavily. Works great for 20-50 devices. Above 50, flooding-based message forwarding starts causing noticeable latency.

**Wi-Fi**: Simplest to set up (your router is already there), but limited to ~20-30 devices per router. Router goes down = whole lighting system goes dark. Fine for small setups, risky for whole-home.

**DALI-2** (IEC 62386, wired): The gold standard for precision. Smooth dimming below 1% — something wireless protocols physically can't match. Higher wiring cost, max 64 devices per group, but irreplaceable for museums and high-end commercial.

**Matter is changing things.** Zigbee 3.0 devices can bridge into Matter. Wi-Fi and Thread are native transport. DALI-2 isn't going anywhere though — Matter can't touch its precision dimming for commercial.

What protocols are you running? Any horror stories or unexpected wins?

---
*Disclaimer: I work in the smart lighting industry. Happy to answer technical questions in the comments.*

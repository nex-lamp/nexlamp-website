---
title: "The Lights Are Installed, the Automations Aren't Working: Debugging Mijia's Silent Failures"
description: "A field guide to Mijia (Mi Home) automation failures: the speaker-probe trick that halves your fault range in one shot, event triggers versus state conditions, stale device records, and the six features that quietly force your rule back into the cloud."
tags: ["smarthome", "iot", "debugging", "lighting"]
---

The delivery boxes are unpacked, the batteries are in, and you are full of confidence: from now on, the light comes on when you walk in and goes off when you leave. Three days later you start questioning your life choices. Someone clearly walks past the sensor and the light just ignores them. You told it to turn off at eleven and it plays dead. It worked yesterday. Today it doesn't.

Before you blame the hardware, there's a consensus among people who have spent too long with smart lighting: **when an automation doesn't run, nine times out of ten the device isn't broken — one of the three segments, trigger, condition, or action, is empty.** The trouble is that Mijia (Mi Home) fails silently. It will not tell you which segment is empty.

That's the whole problem in one sentence. A broken driver gives you a flicker, a dead LED strip gives you a dark room, a bad joint gives you a warm terminal. An automation gives you nothing at all. So the first job isn't repair — it's narrowing the search.

## Step one: install a probe that makes noise

Add one action to the very end of the automation's action list: "Xiaomi speaker announces a sentence." The sentence can be anything. Then trigger the automation manually, once.

- The speaker talks, the light doesn't move — the problem is in the **action segment**.
- The speaker doesn't talk at all — the problem is in the **trigger or condition segment**.

One sound, and your fault range is cut in half. The value of this step isn't that it fixes anything. It's that you stop guessing at the whole rule at once.

A speaker is the cheapest diagnostic instrument in the house, and almost every Mijia installation already has one. Use it before you use a ladder.

## The trigger segment: the number one reason "someone's there but the light stays off"

"When the following happens" is the trigger. "And all of these conditions are met" is checked at the instant the trigger fires. **These are not the same thing, and the gap between them is where automations die.**

A motion sensor is event-type: a person walks past and it emits an event immediately. An ambient light sensor is state-type: it may only report its brightness once every five minutes. So at the exact moment someone walks down the hallway, the system reads a light level from five minutes ago, decides the condition isn't satisfied, and the entire automation quietly does nothing.

This is not a sensitivity problem. Raising the threshold on the light sensor won't help, because the value being compared is stale, not wrong. What you change is the **order of evaluation**: move the state condition to after a "delay of a few dozen seconds," or drop it entirely and use a time-window condition instead. Evaluate the state after the world has had a moment to update, not at the same millisecond as the event.

There are three smaller traps in the trigger segment as well:

- **The device was offline at that moment.** Mijia does not retry. The action is simply dropped, and nothing is logged as an error.
- **A Wi-Fi device reconnecting slowly.** With "band steering" (2.4 GHz and 5 GHz merged into one SSID) enabled on the router, a device can take long enough to reattach that it misses the one second it needed to be reachable.
- **Throttling on repeated triggers.** Firing several times within a minute or two gets rate-limited. Adding a "delay 30 seconds" before the action and re-checking the condition afterwards is a workable pattern.

## The execution segment: the invisible stale device record

The nastiest trap in the action segment is a **stale device record**. If a device was deleted and re-added, or moved over from another home, the action line in the automation looks perfectly normal in the UI — but underneath it still points at the old record. At execution time it is discarded. No error, no warning, no log entry that says "this reference is dead."

The heuristic I use: whenever someone says "this automation stopped working after I reinstalled that one device," it's this. Nine times out of ten. Delete the action, re-select the device, save. You don't need to rebuild the whole rule, and you don't need to touch the hardware.

It's worth saying out loud because it violates every instinct you have as an electrician. There is no loose wire to find. The wire is drawn correctly on the diagram and connected to nothing.

## The cloud wall: automations run in the cloud by default

If the home has no central gateway hub, and the scene isn't marked "local execution," then every automation runs on Mijia's servers. The WAN port on the router hiccups, the vendor's servers have a bad afternoon, and your automations stop running. Afterwards there is nothing anomalous to find, because from the system's point of view nothing failed locally. It just never got the instruction.

According to Mijia's own documentation, local execution requires all of the following at once: the trigger device and the action device must be under the same gateway, **and the scene must not contain any feature that requires internet access.** Meet even one of the conditions below and the whole rule is demoted to cloud execution:

| Internet-dependent feature (one is enough to force cloud execution) |
|---|
| Effective time period set to "statutory working days / statutory holidays" |
| Trigger: arriving at / leaving a location |
| Trigger: sunrise / sunset |
| Trigger: outdoor weather change |
| Action: send a notification to the phone |
| Action: run or toggle a manual scene |

I've seen a case where automations stopped working *after* a central gateway upgrade, and the cause turned out to be a single "send notification" action dragging the entire rule back into the cloud. Remove the notification, and local execution came back. The gateway was never the problem.

This is the part that surprises people most, because it's counterintuitive in the worst way: adding a helpful feature can silently downgrade the reliability of everything else in that rule. If you want a rule to survive a dead internet connection, treat that table as a checklist and audit every line of it.

## When you're out of ideas, check in this order — the logs don't lie

1. **Gateway online.** Mijia app → Me → Hub & Gateways, check the primary gateway status. Thirty seconds. Roughly half of all cases end here.
2. **Devices online.** A grey dot in the device list means offline. Check both the trigger device and the action device. Thirty seconds.
3. **Execution mode.** Open the automation detail page and see whether it's marked "local." Thirty seconds.
4. **Logic.** Check the AND/OR relationships, and whether the effective time windows contradict each other. About two minutes.
5. **Logs.** The log icon in the top right of the geek-mode view, or "execution records" on the automation detail page.

The log is the most accurate triage desk you have. **No trigger record at all** — go look at whether the sensor is reporting and whether the gateway is receiving; don't go near the light. **Trigger recorded, no execution** — the problem is locked in the action segment. Get the direction right and you've solved half of it.

Without logs, you're back to climbing ladders and swapping drivers on suspicion, which is how a thirty-second fix turns into an afternoon.

## FAQ

**The light turned itself on in the middle of the night. Is that an automation too?**

Probably. Open the notification center in the app and look at the automation history — it's usually a motion sensor or a door contact false-triggering. The other category is a wiring issue: have the electrician run the light through the smart switch panel's wiring so the fixture can't power itself on independently of the control system.

**The same light shows as online in Mijia but the automation doesn't run.**

"Online" only means its state can be read. It does not mean it triggered, and it certainly doesn't mean it executed. Use the probe to cut the range in half, then read the execution record to confirm which layer it's stuck at.

**Should I ask "does it support local execution?" when buying lights?**

Yes, but the better question is "where does this linkage run?" Central gateway present, trigger and action devices on the same gateway, no internet-dependent features — it runs with the internet down. In a house where everything executes in the cloud, one router reboot stops every scene in the home at the same time.

A lamp is a lamp; an automation is an automation. When a lamp fails you replace the driver or the board. When an automation fails you trace the chain — trigger, condition, action, and where it runs. Start by making the speaker say something, then pick up the tools.

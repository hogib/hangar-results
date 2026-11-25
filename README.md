# hangar: results from the lab's vehicle

Measurements of [hangar](https://github.com/hogib/hangar) on a BlueROV2 on the bench
(props off, in air): a Raspberry Pi 5, a Pixhawk with ArduSub 4.5.5, a laptop on the
tether. One directory per session, as the tools wrote them; each has its own README.

| Directory | hangar | What |
|---|---|---|
| `2026-11-20-lab/` | main `e559888` (v0.1.1-9) | Cost of the running system, armed, with electric-eye's video path (`old-*`) and with hangar's encoder (`new-*`) |
| `2026-11-24-lab/` | v0.1.4-3 | Cost of the running system, both roles on the Pi |
| `2026-11-24-lab-2/` | v0.1.4-4 | The same with the tether bridge, the topside role on the laptop |
| `2026-11-24-lab-logs/`, `2026-11-24-lab-step4/` | v0.1.4 | The modules' logs of that session, and the tether tests' timing logs |
| `2026-11-25/` | 0.1.5 | The benchmark with a heat sink fitted: temperature, transport, cost, 164 repetitions of the failure tests, the ROS 2 baseline, every recording. Start with its `README.md` |

Later sessions are added the same way: `tools/rov/lab.sh bench` writes
`<date>-lab[-n]/` here and `tools/rov/failtest.py` writes `<date>-failtests/`.

The numbers are the bench's. Nothing here was measured in water.

# Bench, 2026-11-20, the lab's BlueROV2, armed, end to end

Release built from hangar main `e559888` (v0.1.1-9): the busy-loop fix (hangar#1) and the
encoder (stage 1 of "no ffmpeg on the ROV"). Props off, the battery connected (the
Pixhawk reads 0.73 V: safety's battery check off for the session).

Running during the 60 s (`bench/procbench.py 60` on both machines at once):

- **ROV** (Pi 5, Ubuntu 24.04, `ondemand`, 2.1 GHz, 62.8–65.5 °C, not throttled): hangar's
  vehicle and topside roles (same-host shim), ArduSub armed in MANUAL through hangar
  (armed from QGroundControl), the gate open, the recorder recording a session, the
  encoder sending the camera's own H.264 (`/dev/video2`, 1280×720, 30 fps, a keyframe
  every ~29 frames, about 5.7 Mbit/s); MAVROS as the serial-to-UDP relay. The lab's own
  electric-eye services stopped.
- **Laptop** (x86-64, 12 cores): electric-eye's hellion and eeye in placement A (hangar's
  `legacy/` builds): the ROV's stream decoded (ffmpeg), the effects (blur + sobel), and
  re-encoded for QGroundControl on 5600 (ffmpeg); QGroundControl connected.

| | CPU (of one core) | PSS |
|---|---|---|
| hangar on the ROV, 10 processes | 6.3 % | 35 MB (the recorder 20.7 MB of it, recording) |
| — of which the video (`hangar-encoder`) | 1.1 % | 7.3 MB |
| MAVROS relay on the ROV | 28.3 % | 128 MB |
| the whole ROV | 9.8 % of all four cores | |
| electric-eye on the laptop (2 ffmpeg, eeye, hellion) | 84 % | 229 MB |

Compare 2026-11-19 on the same ROV: hangar 168.6 % (the busy loops), electric-eye with the
ROV-side ffmpeg encode 91 % / 117 MB, the Pi at 91 °C and throttled to 1.0 GHz.

Files: `rov-procbench.txt`, `rov-state.txt` (status, temperature, clock before and after),
`laptop-procbench.txt`, `laptop-state.txt` (hellion's pipelines).

## The old setup against the new, and what spoiled the comparison

`old-*`: the lab's electric-eye in placement B (ffmpeg encode on the ROV) with the same
fixed hangar; `new-*`: hangar's encoder again, for frame rates (`fpswatch`: hellion's own
"frames in ~1.2 s" every 2 s, which reads ~32 for 30 fps, the same way in both).

| | old (ffmpeg on the ROV) | new (camera H.264) |
|---|---|---|
| ROV video cost | 89.5 % of a core, 116 MB | 1.1 %, 7.3 MB |
| frames out / in on the laptop | ≈32 / ≈33 per s, worst 26.7 | 32.4 (encoder counter) / ≈32, worst 26.7 |
| keyframes | hellion's gop | every 29.9 frames (the camera's own) |
| tether, ROV → laptop | 4.7 Mbit/s | 11.4 Mbit/s (the camera's rate; no control on its H.264 node) |
| laptop | 0.30 of a core | 0.84 of a core |

**Caveats.** The Pi soft-throttled during the old run (76–82 °C, `0x80008`) and the second
new run (83–87 °C, `0xe0008`), and Ubuntu's unattended-upgrades ran as root at a full core
during the second new run: the ROV's CPU percentages of those two runs read high (MAVROS
45 % and 34 % against 28 % in the first). The first new run (63–66 °C, not throttled)
is the clean one. Not measured: glass-to-glass latency (needs a clock filmed through the
camera and on the screen). The vehicle was left as found: parameters restored (diff
clean), hangar and the relay stopped, the lab's eeye and hellion running.

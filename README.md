# Bench session, 2026-11-25: heatsink fitted, hangar v0.1.5

BlueROV2 on the bench, props off, Raspberry Pi 5 with a passive heatsink, Pixhawk with
ArduSub 4.5.5, laptop on the tether. `notes.txt` is the timeline as it happened, with the
findings; `plan.md` is the plan the session followed.

## Where things are

| Folder | What | Start with |
|---|---|---|
| `1-thermal/` | Pi temperature and throttle state every 10 s, 15:58 to 19:58 | `thermal-20261125.log` (stage times are in `notes.txt`) |
| `2-transport/` | `hg_bench` on the Pi: `c1-quiet`, `c2-load2`, `c2-load4`, `c3-beside-hangar` | the `.txt` of each; `.json` has every figure, `.env` the temperature before and after |
| `3-cost/` | Cost of the running system, 60 s each: `relay-idle-1..3`, `serial-idle`, `serial-armed`, `serial-video-idle` | `rov-procbench.txt` in each (the Pi), `laptop-procbench.txt` |
| `4-failure-tests/` | One JSON line per repetition: `relay-quiet`, `relay-load2`, `relay-load4`, `relay-unplug`, `serial`, `serial-video`; `clear-unplugged.json`; `console/` has what the script printed | `console/*.txt` for the summaries |
| `4-failure-tests/set-aside/` | Runs stopped by a limit in the test, kept for the record, not to be quoted | see "Set aside" below |
| `5-ros2-baseline/` | hangar against ROS 2 Jazzy with Fast DDS, 3 repetitions | `20261125T151847Z/results.md` (`20261125T151433Z` is the short smoke test) |
| `6-snapshots/` | The ROV camera's picture, 1280x720: `rov-camera-*` untouched, `rov-pilot-*` blur then sobel | |
| `recordings/` | Every recorder session and failsafe snapshot of the day (304 items) | the raw topic data behind the timings |
| `logs/` | Both managers' logs and the vehicle's module logs | the serial-only session's manager logs were not kept |
| `scripts/` | `soak.py` (not run), `clear_unplugged.py`, `clear-test.sh` | |

The failure tests were run with `tools/rov/failtest.py` from the hangar checkout.

## Headline numbers

### Temperature (governor `ondemand` until 16:27, `performance` after)

| State | Temperature | Throttled |
|---|---|---|
| hangar down, the lab's eeye and hellion running | 55.8 C | no |
| hangar up (relay, bridge), disarmed | 57.0 C, still warming after boot | no |
| armed, sticks | 57.0 C | no |
| armed with video (lab's eeye and hellion stopped) | 50.6 C | no |
| plus 2-core load | 68-75 C | no |
| plus 4-core load | 83-85 C | soft limit after 35-75 s |
| serial with video, disarmed | 59.5-62.2 C | no |

After the 4-core load: 83.4 C to 57 C in 90 s. The first cooling stage and the first
baseline (16:24 to 16:34) are spoiled by `unattended-upgrade` and are not in this table.

### Transport (`hg_bench`, 256 B unless said)

| | Quiet | 2-core load | 4-core load (throttled) | Beside hangar |
|---|---|---|---|---|
| publish 16 B | 80 ns | 80 ns | 155 ns | 80 ns |
| wake 1 kHz, median | 5.4 us | 5.5 us | 6.6 us | 7.0 us |
| wake 1 kHz, 99 % | 29 us | 509 us | 2635 us | 1235 us |

"Quiet" had the lab's eeye and hellion running (about 15 % of a core).

### Cost on the Pi (hangar's processes together, % of one core)

| Configuration | hangar | Beside it |
|---|---|---|
| relay, idle (3 runs) | 4.09, 4.09, 4.13 | MAVROS relay 25 %, 131 MB |
| serial, idle | 1.86 | no relay |
| serial, armed, sticks | 2.06 | |
| serial with video, disarmed | 2.76 (encoder 0.76) | 32.3 frames/s, 11.1 Mbit/s |

No memory figures (they need sudo on the Pi). One run each on serial.

### Failure tests (valid repetitions; times are min-max)

| Test | relay quiet | relay 2-core | relay 4-core | serial | serial + video |
|---|---|---|---|---|---|
| safety killed: ArduSub disarmed | 10: 4.2-8.0 ms | 5: 3.9-8.1 | 5: 4.3-15.3 | 5: 4.3-6.4 | 5: 3.7-6.5 |
| vehicle's mavlink killed: disarmed | 5: 167.6-169.1 ms | 5: 169.2-174.0 | 5: 170.6-182.2 | 5: 180.0-180.9 | 5: 179.3-180.8 |
| vehicle's bridge suspended: input trigger | 10: 218-317 ms | 5: 232-296 | 5: 231-263 | 5: 221-275 | 5: 215-296 |
| topside silent 5 s: tether trigger after the last packet | 10: 3000-3014 ms | 5: 3000-3018 | 5: 3001-3015 | 5: 3010-3020 | 5: 3000-3014 |
| mux killed | 5: restarted, stayed armed | 5 | 5 | 5 | 5 |
| topside silent 1 s | 10: nothing fired | | | | |
| topside silent 2.5 s | 9: nothing fired (2.55-2.63 s) | | | | |
| arm asked 2 s into a silence | 5: refused | | | | |
| tether pulled by hand | 3: 3000-3011 ms after the last packet | | | | |
| `clear` with the tether out | refused 3 of 3; cleared once the link was back | | | | |

164 valid scripted repetitions, 3 cable pulls and the `clear` test; every one ended in the
expected state.

### ROS 2 baseline (256 B at 1 kHz, two processes; medians of 3)

| | hangar | Fast DDS | Fast DDS, data-sharing |
|---|---|---|---|
| publish to reader, median | 5.6 us | 35.9 us | 26.1 us |
| CPU, the pair | 1.16 % | 5.30 % | 4.62 % |
| memory, the pair | 270 kB | 31.2 MB | 31.4 MB |
| 1 MB at 30 Hz, median | 318 us | 1071 us | 32 us |

hangar is slower for 1 MB frames than Fast DDS with loaned messages, and its 99.9th
percentile is worse at 100 Hz and 10 kHz. Cyclone DDS and Zenoh are not installed on the Pi.

## Open

- **Mux killed:** the script watches safety's state, not the gate's output, so it does not
  show whether the gate went neutral in the gap. To answer from `recordings/`.
- **One refusal unexplained:** relay-quiet `silence-2.5` repetition 1, "ArduSub armed while
  hangar was disarmed", straight after a recovery by hand.
- **Soak not run** (battery, time). `scripts/soak.py` is ready.
- **No video baseline.** The lab's eeye and hellion are ours; what a stock BlueROV2 runs
  (camera H.264 passed to QGroundControl) was not measured.
- **Findings F1-F3** in `notes.txt`: `lab.sh --video` and a taken port 5610; the topside
  console framing hellion on the wrong port; no camera controls with `--video`.

## Set aside

- `set-aside/first-attempt`: the manager gave up on safety after six kills in 60 s (its
  designed limit); vehicle disarmed, gate closed.
- `set-aside/second-attempt-backoff`: the laptop's manager lengthened each silence; real
  silences 2.58, 2.73, 2.86 s (nothing fired) and 3.32, 4.06, 7.48 s (tether trigger at
  3006-3018 ms). Correct behaviour, but not the silence asked for.
- `set-aside/serial-mavlink-first`: repetitions 2-5 refused, "ArduSub parameters not read
  yet"; the script now waits for them.

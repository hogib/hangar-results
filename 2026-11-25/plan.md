# Load testing on the bench, 2026-11-25 (heatsink fitted, v0.1.5)

Props off for everything. Nothing here needs water. Stop and `lab.sh down` if the Pi
throttles in a block that is meant to be a measurement: note the temperature and move on
to the next block after it has cooled.

Load generators are busy loops that end by themselves (`timeout N sh -c 'while :; do :; done'`),
one per core. "4-core load" below means four of them on the Pi.

Needs your own terminal (sudo on the Pi): `lab.sh deploy`; any `lab.sh up` after the Pi
was power-cycled; the frequency governor; `lab.sh bench` if memory figures are wanted;
stopping the lab's eeye and hellion for block G.

| Block | What | Time | Priority |
|---|---|---|---|
| 0 | Heatsink fitted: photo, model, how it is mounted (the paper has a TODO for it) | 5 min | must |
| A | Deploy v0.1.5, `up --bridge`, confirm the restart fix | 15 min | must |
| B | Thermal curve | 35 min | must |
| C | Transport benchmark, quiet and under load | 20 min | must |
| D | Cost of the running system, three states | 15 min | must |
| E | Safety and tether tests, repeated, quiet and under load | 60 min | must |
| F | Serial MAVLink: arm tests, cost, a subset of E | 40 min | should |
| G | ROS 2 baseline | 50 min | should |
| H | Soak | 60 min, unattended | should |
| I | Extras: native video, camera unplug, joystick module | as time allows | could |

## A. Deploy and the fix (15 min)

1. `tools/rov/lab.sh deploy` (your terminal), `lab.sh up --bridge --no-battery-check`, `lab.sh status`.
2. Arm in QGroundControl, sticks move the thrusters, disarm.
3. **The fix:** `BRIDGE=1 tools/rov/rov.sh topside reset && BRIDGE=1 tools/rov/rov.sh topside up`,
   arm, sticks. Pass: the thrusters follow at once (v0.1.4: dead for minutes).
   Check `dropped_old` on the Pi's `bridge.vehicle.link` stays near zero.

## B. Thermal curve (35 min)

Temperature and throttle state every 10 s on the Pi throughout, to a file.

| Stage | Load | Length |
|---|---|---|
| B1 | hangar down, lab services only | 5 min |
| B2 | hangar up with the bridge, disarmed | 5 min |
| B3 | armed, sticks moved now and then | 5 min |
| B4 | B3 plus video (`up --video`) | 5 min |
| B5 | B4 plus 4-core load | 10 min |
| B6 | load off, cooling back | 5 min |

Pass: `throttled` shows nothing current in any stage. If B5 throttles, note after how long
and at what temperature: that is the limit every later block has to stay under.

## C. Transport (20 min)

`hg_bench` on the Pi, governor `performance`:

1. Quiet (hangar down): publish and read cost 16 B to 1 MB; wake-up latency at 100 Hz, 1 kHz, 10 kHz.
2. The same with 4-core load: what the latency tail does when the cores are taken.
3. The same with hangar running beside it.

Record temperature and throttle state before and after each.

## D. Cost of the running system (15 min)

`lab.sh bench 60`, from your terminal for the memory figures, in three states:
disarmed and idle; armed with the sticks moving; armed with video. Three runs of the
first, to see the spread.

## E. Safety and tether tests (60 min)

Each test arms the vehicle, removes something, and times the result on the Pi's own clock.
Repetitions give a distribution, not one number. All but the physical unplug are run by a
script from the laptop (SSH stays up when a bridge is suspended).

| Test | Repetitions | Expected |
|---|---|---|
| Safety module killed while armed | 10 | ArduSub disarmed; time recorded (one unrepeated 5 ms so far) |
| Vehicle's mavlink module killed while armed | 5 | its neutral command disarms ArduSub; manager restarts it |
| Mux killed while armed | 5 | gate goes neutral within 200 ms |
| Vehicle's bridge suspended while armed | 10 | input trigger, about 0.3 s |
| Topside's bridge suspended 5 s while armed | 10 | tether trigger 3.0 s after the last packet |
| Topside's bridge suspended 1 s while armed | 10 | nothing fires |
| Topside's bridge suspended 2.5 s while armed | 10 | nothing fires (marginal: note any that do) |
| Arm requested 2 s into a silence | 5 | refused |
| Tether physically unplugged while armed | 3 | tether trigger 3.0 s after the last packet |
| `clear` with the tether still unplugged | 1 | refused (needs someone at the Pi, or a script started before the unplug) |

Commands, from the checkout on the laptop, with `lab.sh up --bridge` done first:

```sh
tools/rov/failtest.py --props-off all                       # every row but the unplug, about 25 min
tools/rov/failtest.py --props-off all --load 4              # the same with four busy loops on the Pi
tools/rov/failtest.py --props-off unplug --times 3          # it says when to pull the cable
tools/rov/failtest.py --props-off silence 2.5 --times 10    # one test by itself
```

Results go to `~/hangar-results/<date>-failtests/`, one line of JSON per repetition, and
each test prints its minimum, median and maximum. The script leaves the vehicle disarmed,
also when interrupted with Ctrl-C. It has run against the rehearsal stack only.
`mavlink-kill` there left the stand-in serial line unusable (a property of the stand-in);
on the Pixhawk's real serial line that test is the one to watch: if the module cannot
reopen the line after being killed, that is a finding.

Then the first five rows again **with 4-core load on the Pi**, and once more **with video
running**: the claim to test is that the times do not move when the machine is busy.

## F. Serial MAVLink (40 min)

`lab.sh up --serial --bridge --no-battery-check`. Arm, disarm, sticks. Then block D's
idle and armed runs (no MAVROS: the largest load is gone), and block E's first five rows,
5 repetitions each. If this passes, serial is the configuration for the paper.

## G. ROS 2 baseline (50 min)

`bench/ros2/README.md`, "On the Pi, step by step". hangar down, the lab's eeye and hellion
stopped (your terminal), temperature logged throughout. Discard and repeat if the Pi throttles.

## H. Soak (60 min, unattended)

Armed at rest with the bridge, video and the recorder. Every 30 s: temperature, throttle
state, each module's restarts and resident memory, the link's counters (loss, retransmits,
rejected, dropped_old), the recording's size and gaps. Pass: no restart, no growth in
memory, no gap, link up throughout.

## Before leaving

Disarmed; `lab.sh down` until `lab: everything as found`; `systemctl is-active eeye hellion`
says active twice; logs copied off the Pi before `down`.

# hangar against ROS 2: Raspberry Pi 5 Model B Rev 1.0

**A smoke test of the benchmark, not a measurement: --quick. These numbers do not go into docs/00.**

2026-11-25T15:16:00Z, Raspberry Pi 5 Model B Rev 1.0, aarch64, Linux 6.8.0-1048-raspi, 4 CPUs, governor performance.
ROS 2 jazzy; hangar lib/hg db2dfc8 (Clang 22.1.8), bench/ros2 at unknown.
1 repetition(s); each rate run 3 s after 1 s of warm-up (ROS 2), idle 3 s; writer on CPU 2, reader on CPU 3, the same two for both systems.
Load average at the start 1.22; running beside the benchmark: nothing procbench.py knows.

A cell is the median over the repetitions, (min–max) when there are several, and **×N**: how many times hangar's figure the ROS 2 one is. † marks a figure with a run in it during which the machine was hot, throttled, frequency-capped or busy with something else (listed below).

| | hangar | `fastdds` | `fastdds-datasharing` |
|---|---|---|---|
| **Publish, ns per message, nobody subscribed (hg_publish; publish())** | | | |
| 16 B | 80.2 | 991 **×12.4** | 1 334 **×16.6** |
| 256 B | 96.1 | 960 **×9.99** | 1 284 **×13.4** |
| 4 KB | 359 | 1 080 **×3.01** | 1 331 **×3.71** |
| 1 MB | 122 925 | 87 928 **×0.72** | 1 319 **×0.01** |
| **Read the newest message, ns (hg_latest; take() of a message just published in the same process)** | | | |
| 16 B | 52.9 | 1 536 **×29.0** | 1 487 **×28.1** |
| 256 B | 121 | 1 657 **×13.7** | 1 468 **×12.2** |
| 4 KB | 416 | 1 754 **×4.22** | 1 613 **×3.88** |
| 1 MB | 198 459 | 89 930 **×0.45** | 135 532 **×0.68** |
| **256 B at 100 Hz, two processes on two CPUs; ROS 2 QoS: best-effort keep-last 1** | | | |
| publish → message in the reader's hands, p50, µs | 5.60 | 45.4 **×8.11** | 25.8 **×4.61** |
| p99, µs | 10.1 | 72.0 **×7.13** | 43.6 **×4.32** |
| p99.9, µs | 18.2 | 97.9 **×5.38** | 96.8 **×5.32** |
| max, µs | 18.2 | 97.9 **×5.38** | 96.8 **×5.32** |
| CPU, both processes, % of one core | 0.140 | 0.672 **×4.80** | 0.500 **×3.57** |
| context switches per second, both processes | 209 | 316 **×1.51** | 319 **×1.53** |
| messages lost, % | 0 | 0 | 0 |
| **256 B at 100 Hz, two processes on two CPUs; ROS 2 QoS: reliable keep-last 16** | | | |
| publish → message in the reader's hands, p50, µs | 5.60 | 38.0 **×6.79** | 33.7 **×6.02** |
| p99, µs | 10.1 | 58.3 **×5.77** | 53.4 **×5.29** |
| p99.9, µs | 18.2 | 62.3 **×3.42** | 60.1 **×3.30** |
| max, µs | 18.2 | 62.3 **×3.42** | 60.1 **×3.30** |
| CPU, both processes, % of one core | 0.140 | 0.679 **×4.85** | 0.697 **×4.98** |
| context switches per second, both processes | 209 | 443 **×2.12** | 416 **×1.99** |
| messages lost, % | 0 | 0 | 0 |
| **256 B at 1 kHz, two processes on two CPUs; ROS 2 QoS: best-effort keep-last 1** | | | |
| publish → message in the reader's hands, p50, µs | 5.60 | 42.7 **×7.63** | 25.2 **×4.50** |
| p99, µs | 5.80 | 45.4 **×7.83** | 26.5 **×4.57** |
| p99.9, µs | 17.4 | 62.0 **×3.56** | 38.6 **×2.22** |
| max, µs | 150 | 424 **×2.83** | 235 **×1.57** |
| CPU, both processes, % of one core | 1.18 | 6.01 **×5.09** | 4.41 **×3.74** |
| context switches per second, both processes | 2 008 | 3 016 **×1.50** | 3 019 **×1.50** |
| messages lost, % | 0 | 0 | 0 |
| **256 B at 1 kHz, two processes on two CPUs; ROS 2 QoS: reliable keep-last 16** | | | |
| publish → message in the reader's hands, p50, µs | 5.60 | 41.4 **×7.39** | 34.7 **×6.20** |
| p99, µs | 5.80 | 47.6 **×8.21** | 41.9 **×7.22** |
| p99.9, µs | 17.4 | 65.1 **×3.74** | 83.4 **×4.79** |
| max, µs | 150 | 104 **×0.69** | 530 **×3.54** |
| CPU, both processes, % of one core | 1.18 | 6.93 **×5.87** | 6.61 **×5.60** |
| context switches per second, both processes | 2 008 | 4 168 **×2.08** | 4 016 **×2.00** |
| messages lost, % | 0 | 0 | 0 |
| **256 B at 10 kHz, two processes on two CPUs; ROS 2 QoS: best-effort keep-last 1** | | | |
| publish → message in the reader's hands, p50, µs | 5.30 | 37.5 **×7.08** | 24.4 **×4.60** |
| p99, µs | 5.60 | 43.7 **×7.80** | 26.4 **×4.71** |
| p99.9, µs | 10.0 | 46.4 **×4.64** | 32.4 **×3.24** |
| max, µs | 747 | 364 **×0.49** | 132 **×0.18** |
| CPU, both processes, % of one core | 11.4 | 55.4 **×4.84** | 43.0 **×3.76** |
| context switches per second, both processes | 20 003 | 30 014 **×1.50** | 30 023 **×1.50** |
| messages lost, % | 0 | 0.017 | 0.013 |
| **256 B at 10 kHz, two processes on two CPUs; ROS 2 QoS: reliable keep-last 16** | | | |
| publish → message in the reader's hands, p50, µs | 5.30 | 41.4 **×7.81** | 33.9 **×6.40** |
| p99, µs | 5.60 | 57.6 **×10.3** | 36.1 **×6.45** |
| p99.9, µs | 10.0 | 80.4 **×8.04** | 45.7 **×4.57** |
| max, µs | 747 | 1 019 **×1.36** | 338 **×0.45** |
| CPU, both processes, % of one core | 11.4 | 63.7 **×5.57** | 65.1 **×5.69** |
| context switches per second, both processes | 20 003 | 40 539 **×2.03** | 40 009 **×2.00** |
| messages lost, % | 0 | 0 | 0 |
| **256 B at 1 kHz, the pair left to the scheduler (not pinned); best-effort keep-last 1** | | | |
| p50, µs | 5.70 | 37.4 **×6.56** | 24.7 **×4.33** |
| p99, µs | 5.80 | 47.2 **×8.14** | 33.1 **×5.71** |
| max, µs | 15.8 | 133 **×8.42** | 62.4 **×3.95** |
| CPU, both processes, % of one core | 1.19 | 5.86 **×4.93** | 4.59 **×3.86** |
| **1 MB at 30 Hz (a camera's frames), two processes on two CPUs; best-effort keep-last 1** | | | |
| p50, µs | 329 | 1 087 **×3.31** | 30.5 **×0.09** |
| p99, µs | 1 725 | 1 649 **×0.96** | 138 **×0.08** |
| max, µs | 1 725 | 1 649 **×0.96** | 138 **×0.08** |
| CPU, both processes, % of one core | 2.55 | 5.46 **×2.14** | 0.865 **×0.34** |
| messages lost, % | 0 | 0 | 0 |
| **Idle: matched, nothing published** | | | |
| subscriber: context switches per second | 0 | 10.0 | 10.0 |
| subscriber: CPU, % of one core | 0 | 0.023 | 0.022 |
| publisher: context switches per second (hangar: none to count, it has no thread asleep) | – | 13.3 | 13.0 |
| publisher: CPU, % of one core | – | 0.027 | 0.027 |
| **Memory and start, the 1 kHz pair** | | | |
| PSS, both processes, kB | 270 | 31 186 **×116** | 31 406 **×116** |
| threads, both processes | 2 | 28 **×14.0** | 29 **×14.5** |
| start of both processes → first message received, ms (hg_bench does not measure it) | – | 253 | 321 |
| **NOT the comparison: both nodes composed in ONE process, rclcpp intra-process delivery, 256 B at 1 kHz** | | | |
| p50, µs | – | 4.00 | 3.10 |
| p99, µs | – | 4.80 | 3.60 |
| max, µs | – | 6.00 | 4.90 |
| CPU, the one process, % | – | 3.86 | 3.42 |
| context switches per second | – | 1 008 | 1 008 |
| PSS, the one process, kB | – | 23 618 | 23 782 |

## The columns

| | |
|---|---|
| hangar | `hg_bench` (/home/bluerov2/hangar-root/bin/hg_bench): shared-memory ring of 16 slots, one futex wake |
| `fastdds` | Fast DDS, as installed (UDP and its shared-memory transport) |
| `fastdds-datasharing` | Fast DDS, data-sharing delivery and loaned messages (config/fastdds-datasharing.xml); loaned messages: granted |

The ROS 2 processes: `ROS_DOMAIN_ID=77`, `ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST`, a SingleThreadedExecutor, every thread of a process pinned to its one CPU.

## Not run

- `cyclonedds`: rmw_cyclonedds_cpp is not installed; to add it: sudo apt install ros-jazzy-rmw-cyclonedds-cpp
- `cyclonedds-iceoryx`: rmw_cyclonedds_cpp is not installed; to add it: sudo apt install ros-jazzy-rmw-cyclonedds-cpp
- `zenoh`: rmw_zenoh_cpp is not installed; to add it: sudo apt install ros-jazzy-rmw-zenoh-cpp
- `zenoh-shm`: rmw_zenoh_cpp is not installed; to add it: sudo apt install ros-jazzy-rmw-zenoh-cpp

## Thermal state

At the start: 61.7 °C, performance, get_throttled 0xe0000. At the end: 55.1 °C, performance, get_throttled 0xe0000.

No run was flagged: never hot, throttled, frequency-capped or with other load beside it between a run's start and its end.

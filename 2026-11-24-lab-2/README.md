# Bench, 2026-11-24T15:55:49+03:00

60 s on both machines, by tools/rov/lab.sh bench (hangar v0.1.4-4-gca8961d).
The state before and after: state-before.txt, state-after.txt (armed or not, temperature,
throttling: a throttled or hot Pi reads high). Frame rates: hellion's "frames in ~1.2 s"
reads ~32 for 30 fps; the encoder's own counter is exact.

The bridge setup: the vehicle role on the Pi (rov-procbench), the topside role on this
laptop (laptop-procbench's hangar lines); the two bridges' link topics before and after
(rtt, loss, retransmits, rejected: the differences are the window's).

## rov-procbench

```
60 s on Raspberry Pi 5 Model B Rev 1.0, 4 cores, the whole machine 14.7 % busy (of all cores), 68.8-72.2 C

hangar
  hangar-mavlink (vehicle)       1.77 % CPU        - MB PSS     474.2 wake-ups/s   (pid 2339)
  hangar-bridge                  1.38 % CPU        - MB PSS     244.1 wake-ups/s   (pid 2337)
  hangar-safety                  1.03 % CPU        - MB PSS     138.9 wake-ups/s   (pid 2342)
  recorder                       0.64 % CPU        - MB PSS     131.5 wake-ups/s   (pid 2341)
  hangar-mux                     0.44 % CPU        - MB PSS     100.0 wake-ups/s   (pid 2340)
  dawn-patrold (?)               0.10 % CPU        - MB PSS       3.0 wake-ups/s   (pid 2338)
  hangard (?)                    0.03 % CPU        - MB PSS      11.0 wake-ups/s   (pid 2332)
  total                          5.40 % CPU     0.00 MB PSS    1102.6 wake-ups/s   (7 processes)

electric-eye
  eeye                          15.71 % CPU        - MB PSS     108.9 wake-ups/s   (pid 716)
  hellion                        1.92 % CPU        - MB PSS      49.3 wake-ups/s   (pid 813)
  total                         17.63 % CPU     0.00 MB PSS     158.2 wake-ups/s   (2 processes)

MAVROS relay
  mavros_node                   30.87 % CPU   110.62 MB PSS    1666.5 wake-ups/s   (pid 2351)
  ros2                           0.00 % CPU    20.71 MB PSS       0.0 wake-ups/s   (pid 2292)
  total                         30.87 % CPU   131.33 MB PSS    1666.5 wake-ups/s   (2 processes)
```

## rov-fps

```
  hellion pilot-up   mean  16.8 frames/s, worst  13.3  (19 samples)
  encoder  no frames counted (not running?)
  eth0 over 61 s: in 0.11 Mbit/s, out 0.14 Mbit/s
```

## laptop-procbench

```
60 s on x86_64, 12 cores, the whole machine 1.7 % busy (of all cores), 48.0-49.0 C

hangar
  hangar-bridge                  0.89 % CPU        - MB PSS     264.4 wake-ups/s   (pid 29042)
  hangar-mavlink (topside)       0.49 % CPU        - MB PSS     191.0 wake-ups/s   (pid 29044)
  dawn-patrold (?)               0.05 % CPU        - MB PSS       3.0 wake-ups/s   (pid 29043)
  hangard (?)                    0.03 % CPU        - MB PSS      11.0 wake-ups/s   (pid 29037)
  total                          1.47 % CPU     0.00 MB PSS     469.3 wake-ups/s   (4 processes)
```

## laptop-fps

```
  enp6s0f3u2 over 60 s: in 0.13 Mbit/s, out 0.13 Mbit/s
```

## rov-link-before

```
--- seq 3986  stamp 1168095335245  gap 0
state                3    # 0 off, 1 searching, 2 connecting, 3 up, 4 ambiguous, 5 refused
config_match         1    # 1 when the two sides run the same release, msg/ tree and bridge.conf
peer_role            2    # 0 unknown, 1 vehicle, 2 topside
reserved0            0
peer_id              644750439    # the peer bridge's random id, drawn at its start
peer_boot_id         [0 247 102 8 179 82 50 92 63 8 241 222 179 229 10 97]    # the other machine's boot id, from the handshake
peer_addr            "192.168.2.1:5614"    # address:port the link uses
last_rx_ns           1168078537467    # CLOCK_MONOTONIC: the last datagram whose tag and packet_seq checked
rtt_ns               4197942    # the last ping's round trip
rtt_min_ns           3153100    # the smallest round trip of the last 10 s
loss_rx              2    # datagrams of the peer lost on the way here, from packet_seq
rejected             0    # datagrams refused: a tag that does not check, a replay, malformed
clock_offset_ns      8250100800620    # the peer's CLOCK_MONOTONIC minus ours, the estimate in force
clock_uncertainty_ns 1771790    # half the kept sample's round trip plus its age times 500 ppm
clock_skew_ppm       0    # 0: not estimated in this stage
topics_rx            4    # mirrored topics received and published here
msgs_tx              32149    # mirrored messages sent
msgs_rx              22316    # mirrored messages published here
retransmits          0    # reliable datagrams sent again
clamped              0    # translated stamps clamped to keep a topic's stamps rising
dropped_old          19644    # received messages whose seq was not above the last published
dropped_late         0    # command messages older than the mirror's MaxAge on arrival
detail               ""    # one line: why, or what; the two versions when they differ
```

## rov-link-after

```
--- seq 4565  stamp 1229415387912  gap 0
state                3    # 0 off, 1 searching, 2 connecting, 3 up, 4 ambiguous, 5 refused
config_match         1    # 1 when the two sides run the same release, msg/ tree and bridge.conf
peer_role            2    # 0 unknown, 1 vehicle, 2 topside
reserved0            0
peer_id              644750439    # the peer bridge's random id, drawn at its start
peer_boot_id         [0 247 102 8 179 82 50 92 63 8 241 222 179 229 10 97]    # the other machine's boot id, from the handshake
peer_addr            "192.168.2.1:5614"    # address:port the link uses
last_rx_ns           1229398527764    # CLOCK_MONOTONIC: the last datagram whose tag and packet_seq checked
rtt_ns               3970294    # the last ping's round trip
rtt_min_ns           3089357    # the smallest round trip of the last 10 s
loss_rx              2    # datagrams of the peer lost on the way here, from packet_seq
rejected             0    # datagrams refused: a tag that does not check, a replay, malformed
clock_offset_ns      8250100939186    # the peer's CLOCK_MONOTONIC minus ours, the estimate in force
clock_uncertainty_ns 1827610    # half the kept sample's round trip plus its age times 500 ppm
clock_skew_ppm       0    # 0: not estimated in this stage
topics_rx            4    # mirrored topics received and published here
msgs_tx              36689    # mirrored messages sent
msgs_rx              28448    # mirrored messages published here
retransmits          0    # reliable datagrams sent again
clamped              0    # translated stamps clamped to keep a topic's stamps rising
dropped_old          19644    # received messages whose seq was not above the last published
dropped_late         0    # command messages older than the mirror's MaxAge on arrival
detail               ""    # one line: why, or what; the two versions when they differ
```

## laptop-link-before

```
--- seq 2113  stamp 9418196497179  gap 0
state                3    # 0 off, 1 searching, 2 connecting, 3 up, 4 ambiguous, 5 refused
config_match         1    # 1 when the two sides run the same release, msg/ tree and bridge.conf
peer_role            1    # 0 unknown, 1 vehicle, 2 topside
reserved0            0
peer_id              2268773045    # the peer bridge's random id, drawn at its start
peer_boot_id         [35 84 169 140 221 129 208 137 168 82 110 160 228 220 81 244]    # the other machine's boot id, from the handshake
peer_addr            "192.168.2.10:5614"    # address:port the link uses
last_rx_ns           9418181856320    # CLOCK_MONOTONIC: the last datagram whose tag and packet_seq checked
rtt_ns               4564373    # the last ping's round trip
rtt_min_ns           2743259    # the smallest round trip of the last 10 s
loss_rx              18617    # datagrams of the peer lost on the way here, from packet_seq
rejected             8    # datagrams refused: a tag that does not check, a replay, malformed
clock_offset_ns      -8250100629088    # the peer's CLOCK_MONOTONIC minus ours, the estimate in force
clock_uncertainty_ns 1945791    # half the kept sample's round trip plus its age times 500 ppm
clock_skew_ppm       0    # 0: not estimated in this stage
topics_rx            14    # mirrored topics received and published here
msgs_tx              22317    # mirrored messages sent
msgs_rx              16527    # mirrored messages published here
retransmits          0    # reliable datagrams sent again
clamped              1110    # translated stamps clamped to keep a topic's stamps rising
dropped_old          0    # received messages whose seq was not above the last published
dropped_late         0    # command messages older than the mirror's MaxAge on arrival
detail               ""    # one line: why, or what; the two versions when they differ
```

## laptop-link-after

```
--- seq 2693  stamp 9479486561974  gap 0
state                3    # 0 off, 1 searching, 2 connecting, 3 up, 4 ambiguous, 5 refused
config_match         1    # 1 when the two sides run the same release, msg/ tree and bridge.conf
peer_role            1    # 0 unknown, 1 vehicle, 2 topside
reserved0            0
peer_id              2268773045    # the peer bridge's random id, drawn at its start
peer_boot_id         [35 84 169 140 221 129 208 137 168 82 110 160 228 220 81 244]    # the other machine's boot id, from the handshake
peer_addr            "192.168.2.10:5614"    # address:port the link uses
last_rx_ns           9479482952764    # CLOCK_MONOTONIC: the last datagram whose tag and packet_seq checked
rtt_ns               4264103    # the last ping's round trip
rtt_min_ns           2903641    # the smallest round trip of the last 10 s
loss_rx              18617    # datagrams of the peer lost on the way here, from packet_seq
rejected             8    # datagrams refused: a tag that does not check, a replay, malformed
clock_offset_ns      -8250100594165    # the peer's CLOCK_MONOTONIC minus ours, the estimate in force
clock_uncertainty_ns 1884026    # half the kept sample's round trip plus its age times 500 ppm
clock_skew_ppm       0    # 0: not estimated in this stage
topics_rx            14    # mirrored topics received and published here
msgs_tx              28447    # mirrored messages sent
msgs_rx              21066    # mirrored messages published here
retransmits          0    # reliable datagrams sent again
clamped              1415    # translated stamps clamped to keep a topic's stamps rising
dropped_old          0    # received messages whose seq was not above the last published
dropped_late         0    # command messages older than the mirror's MaxAge on arrival
detail               ""    # one line: why, or what; the two versions when they differ
```


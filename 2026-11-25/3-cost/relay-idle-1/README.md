# Bench, 2026-11-25T16:58:39+03:00

60 s on both machines, by tools/rov/lab.sh bench (hangar v0.1.5-1-g027c9ca).
The state before and after: state-before.txt, state-after.txt (armed or not, temperature,
throttling: a throttled or hot Pi reads high). Frame rates: hellion's "frames in ~1.2 s"
reads ~32 for 30 fps; the encoder's own counter is exact.

The bridge setup: the vehicle role on the Pi (rov-procbench), the topside role on this
laptop (laptop-procbench's hangar lines); the two bridges' link topics before and after
(rtt, loss, retransmits, rejected: the differences are the window's).

## rov-procbench

```
60 s on Raspberry Pi 5 Model B Rev 1.0, 4 cores, the whole machine 10.6 % busy (of all cores), 55.6-58.4 C

hangar
  hangar-mavlink (vehicle)       1.45 % CPU        - MB PSS     478.2 wake-ups/s   (pid 9672)
  hangar-bridge                  1.09 % CPU        - MB PSS     247.8 wake-ups/s   (pid 9670)
  hangar-safety                  0.87 % CPU        - MB PSS     141.2 wake-ups/s   (pid 9675)
  hangar-mux                     0.36 % CPU        - MB PSS     100.0 wake-ups/s   (pid 9673)
  recorder                       0.23 % CPU        - MB PSS      99.9 wake-ups/s   (pid 9674)
  dawn-patrold (?)               0.07 % CPU        - MB PSS       3.0 wake-ups/s   (pid 9671)
  hangard (?)                    0.03 % CPU        - MB PSS      11.0 wake-ups/s   (pid 9665)
  total                          4.09 % CPU     0.00 MB PSS    1081.2 wake-ups/s   (7 processes)

electric-eye
  eeye                          12.59 % CPU        - MB PSS     109.6 wake-ups/s   (pid 6179)
  hellion                        1.99 % CPU        - MB PSS      49.3 wake-ups/s   (pid 6180)
  total                         14.58 % CPU     0.00 MB PSS     158.9 wake-ups/s   (2 processes)

MAVROS relay
  mavros_node                   25.24 % CPU   110.97 MB PSS    1641.2 wake-ups/s   (pid 9684)
  ros2                           0.00 % CPU    20.10 MB PSS       0.0 wake-ups/s   (pid 9625)
  total                         25.24 % CPU   131.07 MB PSS    1641.2 wake-ups/s   (2 processes)
```

## rov-fps

```
  hellion pilot-up   mean  16.8 frames/s, worst  13.3  (19 samples)
  encoder  no frames counted (not running?)
  eth0 over 61 s: in 0.12 Mbit/s, out 0.13 Mbit/s
```

## laptop-procbench

```
60 s on x86_64, 12 cores, the whole machine 1.6 % busy (of all cores), 55.0-56.0 C

hangar
  hangar-bridge                  1.41 % CPU        - MB PSS     265.6 wake-ups/s   (pid 133751)
  hangar-mavlink (topside)       0.69 % CPU        - MB PSS     188.9 wake-ups/s   (pid 133753)
  dawn-patrold (?)               0.12 % CPU        - MB PSS       8.0 wake-ups/s   (pid 133752)
  hangard (?)                    0.05 % CPU        - MB PSS      11.0 wake-ups/s   (pid 133746)
  total                          2.27 % CPU     0.00 MB PSS     473.5 wake-ups/s   (4 processes)
```

## laptop-fps

```
  enp6s0f3u2 over 60 s: in 0.13 Mbit/s, out 0.14 Mbit/s
```

## rov-link-before

```
--- seq 1741  stamp 3927449218564  gap 0
state                3    # 0 off, 1 searching, 2 connecting, 3 up, 4 ambiguous, 5 refused
config_match         1    # 1 when the two sides run the same release, msg/ tree and bridge.conf
peer_role            2    # 0 unknown, 1 vehicle, 2 topside
reserved0            0
peer_id              365463103    # the peer bridge's random id, drawn at its start
peer_boot_id         [255 26 59 74 15 99 197 24 145 164 99 120 96 191 31 154]    # the other machine's boot id, from the handshake
peer_addr            "192.168.2.1:5614"    # address:port the link uses
last_rx_ns           3927431589656    # CLOCK_MONOTONIC: the last datagram whose tag and packet_seq checked
rtt_ns               4305774    # the last ping's round trip
rtt_min_ns           2521072    # the smallest round trip of the last 10 s
loss_rx              2    # datagrams of the peer lost on the way here, from packet_seq
rejected             0    # datagrams refused: a tag that does not check, a replay, malformed
clock_offset_ns      21714194285425    # the peer's CLOCK_MONOTONIC minus ours, the estimate in force
clock_uncertainty_ns 1880143    # half the kept sample's round trip plus its age times 500 ppm
clock_skew_ppm       0    # 0: not estimated in this stage
topics_rx            2    # mirrored topics received and published here
msgs_tx              15353    # mirrored messages sent
msgs_rx              18274    # mirrored messages published here
retransmits          0    # reliable datagrams sent again
clamped              0    # translated stamps clamped to keep a topic's stamps rising
dropped_old          0    # received messages whose seq was not above the last published
dropped_late         0    # command messages older than the mirror's MaxAge on arrival
detail               ""    # one line: why, or what; the two versions when they differ
```

## rov-link-after

```
--- seq 2321  stamp 3988739203064  gap 0
state                3    # 0 off, 1 searching, 2 connecting, 3 up, 4 ambiguous, 5 refused
config_match         1    # 1 when the two sides run the same release, msg/ tree and bridge.conf
peer_role            2    # 0 unknown, 1 vehicle, 2 topside
reserved0            0
peer_id              365463103    # the peer bridge's random id, drawn at its start
peer_boot_id         [255 26 59 74 15 99 197 24 145 164 99 120 96 191 31 154]    # the other machine's boot id, from the handshake
peer_addr            "192.168.2.1:5614"    # address:port the link uses
last_rx_ns           3988731596360    # CLOCK_MONOTONIC: the last datagram whose tag and packet_seq checked
rtt_ns               3801201    # the last ping's round trip
rtt_min_ns           3801201    # the smallest round trip of the last 10 s
loss_rx              2    # datagrams of the peer lost on the way here, from packet_seq
rejected             0    # datagrams refused: a tag that does not check, a replay, malformed
clock_offset_ns      21714194180837    # the peer's CLOCK_MONOTONIC minus ours, the estimate in force
clock_uncertainty_ns 1900600    # half the kept sample's round trip plus its age times 500 ppm
clock_skew_ppm       0    # 0: not estimated in this stage
topics_rx            2    # mirrored topics received and published here
msgs_tx              19940    # mirrored messages sent
msgs_rx              24404    # mirrored messages published here
retransmits          0    # reliable datagrams sent again
clamped              0    # translated stamps clamped to keep a topic's stamps rising
dropped_old          0    # received messages whose seq was not above the last published
dropped_late         0    # command messages older than the mirror's MaxAge on arrival
detail               ""    # one line: why, or what; the two versions when they differ
```

## laptop-link-before

```
--- seq 1728  stamp 25641633545491  gap 0
state                3    # 0 off, 1 searching, 2 connecting, 3 up, 4 ambiguous, 5 refused
config_match         1    # 1 when the two sides run the same release, msg/ tree and bridge.conf
peer_role            1    # 0 unknown, 1 vehicle, 2 topside
reserved0            0
peer_id              3042215992    # the peer bridge's random id, drawn at its start
peer_boot_id         [143 214 186 123 0 191 29 221 92 169 57 74 174 219 216 65]    # the other machine's boot id, from the handshake
peer_addr            "192.168.2.10:5614"    # address:port the link uses
last_rx_ns           25641617018182    # CLOCK_MONOTONIC: the last datagram whose tag and packet_seq checked
rtt_ns               3482167    # the last ping's round trip
rtt_min_ns           3482167    # the smallest round trip of the last 10 s
loss_rx              4    # datagrams of the peer lost on the way here, from packet_seq
rejected             0    # datagrams refused: a tag that does not check, a replay, malformed
clock_offset_ns      -21714193556393    # the peer's CLOCK_MONOTONIC minus ours, the estimate in force
clock_uncertainty_ns 1741083    # half the kept sample's round trip plus its age times 500 ppm
clock_skew_ppm       0    # 0: not estimated in this stage
topics_rx            15    # mirrored topics received and published here
msgs_tx              18276    # mirrored messages sent
msgs_rx              15336    # mirrored messages published here
retransmits          0    # reliable datagrams sent again
clamped              1977    # translated stamps clamped to keep a topic's stamps rising
dropped_old          0    # received messages whose seq was not above the last published
dropped_late         0    # command messages older than the mirror's MaxAge on arrival
detail               ""    # one line: why, or what; the two versions when they differ
```

## laptop-link-after

```
--- seq 2307  stamp 25702913274091  gap 0
state                3    # 0 off, 1 searching, 2 connecting, 3 up, 4 ambiguous, 5 refused
config_match         1    # 1 when the two sides run the same release, msg/ tree and bridge.conf
peer_role            1    # 0 unknown, 1 vehicle, 2 topside
reserved0            0
peer_id              3042215992    # the peer bridge's random id, drawn at its start
peer_boot_id         [143 214 186 123 0 191 29 221 92 169 57 74 174 219 216 65]    # the other machine's boot id, from the handshake
peer_addr            "192.168.2.10:5614"    # address:port the link uses
last_rx_ns           25702910557914    # CLOCK_MONOTONIC: the last datagram whose tag and packet_seq checked
rtt_ns               4180507    # the last ping's round trip
rtt_min_ns           3660912    # the smallest round trip of the last 10 s
loss_rx              4    # datagrams of the peer lost on the way here, from packet_seq
rejected             0    # datagrams refused: a tag that does not check, a replay, malformed
clock_offset_ns      -21714194207255    # the peer's CLOCK_MONOTONIC minus ours, the estimate in force
clock_uncertainty_ns 2090253    # half the kept sample's round trip plus its age times 500 ppm
clock_skew_ppm       0    # 0: not estimated in this stage
topics_rx            15    # mirrored topics received and published here
msgs_tx              24402    # mirrored messages sent
msgs_rx              19923    # mirrored messages published here
retransmits          0    # reliable datagrams sent again
clamped              2282    # translated stamps clamped to keep a topic's stamps rising
dropped_old          0    # received messages whose seq was not above the last published
dropped_late         0    # command messages older than the mirror's MaxAge on arrival
detail               ""    # one line: why, or what; the two versions when they differ
```


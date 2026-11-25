# Bench, 2026-11-25T19:45:19+03:00

60 s on both machines, by tools/rov/lab.sh bench (hangar v0.1.5-1-g027c9ca).
The state before and after: state-before.txt, state-after.txt (armed or not, temperature,
throttling: a throttled or hot Pi reads high). Frame rates: hellion's "frames in ~1.2 s"
reads ~32 for 30 fps; the encoder's own counter is exact.

The bridge setup: the vehicle role on the Pi (rov-procbench), the topside role on this
laptop (laptop-procbench's hangar lines); the two bridges' link topics before and after
(rtt, loss, retransmits, rejected: the differences are the window's).

## rov-procbench

```
60 s on Raspberry Pi 5 Model B Rev 1.0, 4 cores, the whole machine 1.3 % busy (of all cores), 59.5-62.2 C

hangar
  hangar-encoder                 0.76 % CPU        - MB PSS      42.3 wake-ups/s   (pid 60352)
  hangar-bridge                  0.61 % CPU        - MB PSS     303.9 wake-ups/s   (pid 60350)
  hangar-mavlink (vehicle)       0.61 % CPU        - MB PSS     386.3 wake-ups/s   (pid 60353)
  hangar-safety                  0.43 % CPU        - MB PSS     136.4 wake-ups/s   (pid 60356)
  hangar-mux                     0.15 % CPU        - MB PSS     100.0 wake-ups/s   (pid 60354)
  recorder                       0.10 % CPU        - MB PSS     100.0 wake-ups/s   (pid 60355)
  dawn-patrold (?)               0.08 % CPU        - MB PSS       3.0 wake-ups/s   (pid 60351)
  hangard (?)                    0.02 % CPU        - MB PSS      11.0 wake-ups/s   (pid 60345)
  total                          2.76 % CPU     0.00 MB PSS    1083.0 wake-ups/s   (8 processes)
```

## rov-fps

```
  encoder  32.3 frames/s over 60 s, a keyframe every 30.3 frames
  eth0 over 60 s: in 0.11 Mbit/s, out 11.12 Mbit/s
```

## laptop-procbench

```
60 s on x86_64, 12 cores, the whole machine 11.5 % busy (of all cores), 62.0-64.0 C

hangar
  hangar-bridge                  1.24 % CPU        - MB PSS     272.8 wake-ups/s   (pid 159948)
  hangar-mavlink (topside)       0.59 % CPU        - MB PSS     164.5 wake-ups/s   (pid 159951)
  dawn-patrold (?)               0.13 % CPU        - MB PSS       7.6 wake-ups/s   (pid 159950)
  hangard (?)                    0.03 % CPU        - MB PSS      11.0 wake-ups/s   (pid 159944)
  total                          1.99 % CPU     0.00 MB PSS     455.9 wake-ups/s   (4 processes)

electric-eye
  ffmpeg                        31.08 % CPU    54.54 MB PSS     904.2 wake-ups/s   (pid 160048)
  eeye                          29.54 % CPU    50.07 MB PSS    1255.7 wake-ups/s   (pid 160098)
  ffmpeg                        29.50 % CPU    72.04 MB PSS    1462.8 wake-ups/s   (pid 160124)
  hellion                       13.73 % CPU    27.08 MB PSS     591.2 wake-ups/s   (pid 160011)
  total                        103.86 % CPU   203.72 MB PSS    4213.9 wake-ups/s   (4 processes)
```

## laptop-fps

```
  hellion pilot-out  mean  32.2 frames/s, worst  26.7  (19 samples)
  hellion camera-in  mean  32.2 frames/s, worst  26.7  (19 samples)
  enp6s0f3u2 over 61 s: in 11.12 Mbit/s, out 0.12 Mbit/s
```

## rov-link-before

```
--- seq 2014  stamp 13925374117901  gap 0
state                3    # 0 off, 1 searching, 2 connecting, 3 up, 4 ambiguous, 5 refused
config_match         1    # 1 when the two sides run the same release, msg/ tree and bridge.conf
peer_role            2    # 0 unknown, 1 vehicle, 2 topside
reserved0            0
peer_id              1390024471    # the peer bridge's random id, drawn at its start
peer_boot_id         [255 26 59 74 15 99 197 24 145 164 99 120 96 191 31 154]    # the other machine's boot id, from the handshake
peer_addr            "192.168.2.1:5614"    # address:port the link uses
last_rx_ns           13925356621697    # CLOCK_MONOTONIC: the last datagram whose tag and packet_seq checked
rtt_ns               4119979    # the last ping's round trip
rtt_min_ns           2509832    # the smallest round trip of the last 10 s
loss_rx              2    # datagrams of the peer lost on the way here, from packet_seq
rejected             0    # datagrams refused: a tag that does not check, a replay, malformed
clock_offset_ns      21714198881115    # the peer's CLOCK_MONOTONIC minus ours, the estimate in force
clock_uncertainty_ns 2059989    # half the kept sample's round trip plus its age times 500 ppm
clock_skew_ppm       0    # 0: not estimated in this stage
topics_rx            2    # mirrored topics received and published here
msgs_tx              23906    # mirrored messages sent
msgs_rx              21152    # mirrored messages published here
retransmits          0    # reliable datagrams sent again
clamped              0    # translated stamps clamped to keep a topic's stamps rising
dropped_old          0    # received messages whose seq was not above the last published
dropped_late         0    # command messages older than the mirror's MaxAge on arrival
detail               ""    # one line: why, or what; the two versions when they differ
```

## rov-link-after

```
--- seq 2610  stamp 13988234118530  gap 0
state                3    # 0 off, 1 searching, 2 connecting, 3 up, 4 ambiguous, 5 refused
config_match         1    # 1 when the two sides run the same release, msg/ tree and bridge.conf
peer_role            2    # 0 unknown, 1 vehicle, 2 topside
reserved0            0
peer_id              1390024471    # the peer bridge's random id, drawn at its start
peer_boot_id         [255 26 59 74 15 99 197 24 145 164 99 120 96 191 31 154]    # the other machine's boot id, from the handshake
peer_addr            "192.168.2.1:5614"    # address:port the link uses
last_rx_ns           13988216696678    # CLOCK_MONOTONIC: the last datagram whose tag and packet_seq checked
rtt_ns               4682655    # the last ping's round trip
rtt_min_ns           2510451    # the smallest round trip of the last 10 s
loss_rx              2    # datagrams of the peer lost on the way here, from packet_seq
rejected             0    # datagrams refused: a tag that does not check, a replay, malformed
clock_offset_ns      21714198956142    # the peer's CLOCK_MONOTONIC minus ours, the estimate in force
clock_uncertainty_ns 2039241    # half the kept sample's round trip plus its age times 500 ppm
clock_skew_ppm       0    # 0: not estimated in this stage
topics_rx            2    # mirrored topics received and published here
msgs_tx              30740    # mirrored messages sent
msgs_rx              27438    # mirrored messages published here
retransmits          0    # reliable datagrams sent again
clamped              0    # translated stamps clamped to keep a topic's stamps rising
dropped_old          0    # received messages whose seq was not above the last published
dropped_late         0    # command messages older than the mirror's MaxAge on arrival
detail               ""    # one line: why, or what; the two versions when they differ
```

## laptop-link-before

```
--- seq 2004  stamp 35639572974858  gap 0
state                3    # 0 off, 1 searching, 2 connecting, 3 up, 4 ambiguous, 5 refused
config_match         1    # 1 when the two sides run the same release, msg/ tree and bridge.conf
peer_role            1    # 0 unknown, 1 vehicle, 2 topside
reserved0            0
peer_id              3158023915    # the peer bridge's random id, drawn at its start
peer_boot_id         [143 214 186 123 0 191 29 221 92 169 57 74 174 219 216 65]    # the other machine's boot id, from the handshake
peer_addr            "192.168.2.10:5614"    # address:port the link uses
last_rx_ns           35639545859604    # CLOCK_MONOTONIC: the last datagram whose tag and packet_seq checked
rtt_ns               12513602    # the last ping's round trip
rtt_min_ns           2433788    # the smallest round trip of the last 10 s
loss_rx              4    # datagrams of the peer lost on the way here, from packet_seq
rejected             0    # datagrams refused: a tag that does not check, a replay, malformed
clock_offset_ns      -21714198356147    # the peer's CLOCK_MONOTONIC minus ours, the estimate in force
clock_uncertainty_ns 1880947    # half the kept sample's round trip plus its age times 500 ppm
clock_skew_ppm       0    # 0: not estimated in this stage
topics_rx            16    # mirrored topics received and published here
msgs_tx              21154    # mirrored messages sent
msgs_rx              23886    # mirrored messages published here
retransmits          0    # reliable datagrams sent again
clamped              1895    # translated stamps clamped to keep a topic's stamps rising
dropped_old          0    # received messages whose seq was not above the last published
dropped_late         0    # command messages older than the mirror's MaxAge on arrival
detail               ""    # one line: why, or what; the two versions when they differ
```

## laptop-link-after

```
--- seq 2599  stamp 35702453297621  gap 0
state                3    # 0 off, 1 searching, 2 connecting, 3 up, 4 ambiguous, 5 refused
config_match         1    # 1 when the two sides run the same release, msg/ tree and bridge.conf
peer_role            1    # 0 unknown, 1 vehicle, 2 topside
reserved0            0
peer_id              3158023915    # the peer bridge's random id, drawn at its start
peer_boot_id         [143 214 186 123 0 191 29 221 92 169 57 74 174 219 216 65]    # the other machine's boot id, from the handshake
peer_addr            "192.168.2.10:5614"    # address:port the link uses
last_rx_ns           35702444961580    # CLOCK_MONOTONIC: the last datagram whose tag and packet_seq checked
rtt_ns               5641949    # the last ping's round trip
rtt_min_ns           3120126    # the smallest round trip of the last 10 s
loss_rx              4    # datagrams of the peer lost on the way here, from packet_seq
rejected             0    # datagrams refused: a tag that does not check, a replay, malformed
clock_offset_ns      -21714198909256    # the peer's CLOCK_MONOTONIC minus ours, the estimate in force
clock_uncertainty_ns 2127624    # half the kept sample's round trip plus its age times 500 ppm
clock_skew_ppm       0    # 0: not estimated in this stage
topics_rx            16    # mirrored topics received and published here
msgs_tx              27442    # mirrored messages sent
msgs_rx              30724    # mirrored messages published here
retransmits          0    # reliable datagrams sent again
clamped              2273    # translated stamps clamped to keep a topic's stamps rising
dropped_old          0    # received messages whose seq was not above the last published
dropped_late         0    # command messages older than the mirror's MaxAge on arrival
detail               ""    # one line: why, or what; the two versions when they differ
```


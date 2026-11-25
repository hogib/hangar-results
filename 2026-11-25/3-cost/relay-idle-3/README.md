# Bench, 2026-11-25T17:00:43+03:00

60 s on both machines, by tools/rov/lab.sh bench (hangar v0.1.5-1-g027c9ca).
The state before and after: state-before.txt, state-after.txt (armed or not, temperature,
throttling: a throttled or hot Pi reads high). Frame rates: hellion's "frames in ~1.2 s"
reads ~32 for 30 fps; the encoder's own counter is exact.

The bridge setup: the vehicle role on the Pi (rov-procbench), the topside role on this
laptop (laptop-procbench's hangar lines); the two bridges' link topics before and after
(rtt, loss, retransmits, rejected: the differences are the window's).

## rov-procbench

```
60 s on Raspberry Pi 5 Model B Rev 1.0, 4 cores, the whole machine 10.8 % busy (of all cores), 55.1-57.3 C

hangar
  hangar-mavlink (vehicle)       1.45 % CPU        - MB PSS     478.7 wake-ups/s   (pid 9672)
  hangar-bridge                  1.12 % CPU        - MB PSS     246.6 wake-ups/s   (pid 9670)
  hangar-safety                  0.84 % CPU        - MB PSS     141.8 wake-ups/s   (pid 9675)
  hangar-mux                     0.39 % CPU        - MB PSS     100.0 wake-ups/s   (pid 9673)
  recorder                       0.25 % CPU        - MB PSS      99.9 wake-ups/s   (pid 9674)
  dawn-patrold (?)               0.07 % CPU        - MB PSS       3.0 wake-ups/s   (pid 9671)
  hangard (?)                    0.02 % CPU        - MB PSS      11.0 wake-ups/s   (pid 9665)
  total                          4.13 % CPU     0.00 MB PSS    1081.0 wake-ups/s   (7 processes)

electric-eye
  eeye                          12.58 % CPU        - MB PSS     109.0 wake-ups/s   (pid 6179)
  hellion                        1.96 % CPU        - MB PSS      49.4 wake-ups/s   (pid 6180)
  total                         14.54 % CPU     0.00 MB PSS     158.4 wake-ups/s   (2 processes)

MAVROS relay
  mavros_node                   24.95 % CPU   110.97 MB PSS    1628.4 wake-ups/s   (pid 9684)
  ros2                           0.00 % CPU    20.10 MB PSS       0.0 wake-ups/s   (pid 9625)
  total                         24.95 % CPU   131.07 MB PSS    1628.4 wake-ups/s   (2 processes)
```

## rov-fps

```
  hellion pilot-up   mean  16.5 frames/s, worst  14.2  (19 samples)
  encoder  no frames counted (not running?)
  eth0 over 61 s: in 0.12 Mbit/s, out 0.13 Mbit/s
```

## laptop-procbench

```
60 s on x86_64, 12 cores, the whole machine 1.8 % busy (of all cores), 55.0-56.0 C

hangar
  hangar-bridge                  1.38 % CPU        - MB PSS     263.0 wake-ups/s   (pid 133751)
  hangar-mavlink (topside)       0.69 % CPU        - MB PSS     186.8 wake-ups/s   (pid 133753)
  dawn-patrold (?)               0.12 % CPU        - MB PSS       8.0 wake-ups/s   (pid 133752)
  hangard (?)                    0.03 % CPU        - MB PSS      11.0 wake-ups/s   (pid 133746)
  total                          2.22 % CPU     0.00 MB PSS     468.8 wake-ups/s   (4 processes)
```

## laptop-fps

```
  enp6s0f3u2 over 60 s: in 0.13 Mbit/s, out 0.14 Mbit/s
```

## rov-link-before

```
--- seq 2908  stamp 4050619169324  gap 0
state                3    # 0 off, 1 searching, 2 connecting, 3 up, 4 ambiguous, 5 refused
config_match         1    # 1 when the two sides run the same release, msg/ tree and bridge.conf
peer_role            2    # 0 unknown, 1 vehicle, 2 topside
reserved0            0
peer_id              365463103    # the peer bridge's random id, drawn at its start
peer_boot_id         [255 26 59 74 15 99 197 24 145 164 99 120 96 191 31 154]    # the other machine's boot id, from the handshake
peer_addr            "192.168.2.1:5614"    # address:port the link uses
last_rx_ns           4050611701898    # CLOCK_MONOTONIC: the last datagram whose tag and packet_seq checked
rtt_ns               4812433    # the last ping's round trip
rtt_min_ns           3805349    # the smallest round trip of the last 10 s
loss_rx              2    # datagrams of the peer lost on the way here, from packet_seq
rejected             0    # datagrams refused: a tag that does not check, a replay, malformed
clock_offset_ns      21714194177523    # the peer's CLOCK_MONOTONIC minus ours, the estimate in force
clock_uncertainty_ns 2008178    # half the kept sample's round trip plus its age times 500 ppm
clock_skew_ppm       0    # 0: not estimated in this stage
topics_rx            2    # mirrored topics received and published here
msgs_tx              24549    # mirrored messages sent
msgs_rx              30592    # mirrored messages published here
retransmits          0    # reliable datagrams sent again
clamped              0    # translated stamps clamped to keep a topic's stamps rising
dropped_old          0    # received messages whose seq was not above the last published
dropped_late         0    # command messages older than the mirror's MaxAge on arrival
detail               ""    # one line: why, or what; the two versions when they differ
```

## rov-link-after

```
--- seq 3490  stamp 4111969160713  gap 0
state                3    # 0 off, 1 searching, 2 connecting, 3 up, 4 ambiguous, 5 refused
config_match         1    # 1 when the two sides run the same release, msg/ tree and bridge.conf
peer_role            2    # 0 unknown, 1 vehicle, 2 topside
reserved0            0
peer_id              365463103    # the peer bridge's random id, drawn at its start
peer_boot_id         [255 26 59 74 15 99 197 24 145 164 99 120 96 191 31 154]    # the other machine's boot id, from the handshake
peer_addr            "192.168.2.1:5614"    # address:port the link uses
last_rx_ns           4111952248898    # CLOCK_MONOTONIC: the last datagram whose tag and packet_seq checked
rtt_ns               4136803    # the last ping's round trip
rtt_min_ns           2168192    # the smallest round trip of the last 10 s
loss_rx              2    # datagrams of the peer lost on the way here, from packet_seq
rejected             0    # datagrams refused: a tag that does not check, a replay, malformed
clock_offset_ns      21714194167163    # the peer's CLOCK_MONOTONIC minus ours, the estimate in force
clock_uncertainty_ns 1140053    # half the kept sample's round trip plus its age times 500 ppm
clock_skew_ppm       0    # 0: not estimated in this stage
topics_rx            2    # mirrored topics received and published here
msgs_tx              29127    # mirrored messages sent
msgs_rx              36726    # mirrored messages published here
retransmits          0    # reliable datagrams sent again
clamped              0    # translated stamps clamped to keep a topic's stamps rising
dropped_old          0    # received messages whose seq was not above the last published
dropped_late         0    # command messages older than the mirror's MaxAge on arrival
detail               ""    # one line: why, or what; the two versions when they differ
```

## laptop-link-before

```
--- seq 2894  stamp 25764813312060  gap 0
state                3    # 0 off, 1 searching, 2 connecting, 3 up, 4 ambiguous, 5 refused
config_match         1    # 1 when the two sides run the same release, msg/ tree and bridge.conf
peer_role            1    # 0 unknown, 1 vehicle, 2 topside
reserved0            0
peer_id              3042215992    # the peer bridge's random id, drawn at its start
peer_boot_id         [143 214 186 123 0 191 29 221 92 169 57 74 174 219 216 65]    # the other machine's boot id, from the handshake
peer_addr            "192.168.2.10:5614"    # address:port the link uses
last_rx_ns           25764795339770    # CLOCK_MONOTONIC: the last datagram whose tag and packet_seq checked
rtt_ns               4057834    # the last ping's round trip
rtt_min_ns           3417455    # the smallest round trip of the last 10 s
loss_rx              4    # datagrams of the peer lost on the way here, from packet_seq
rejected             0    # datagrams refused: a tag that does not check, a replay, malformed
clock_offset_ns      -21714194129635    # the peer's CLOCK_MONOTONIC minus ours, the estimate in force
clock_uncertainty_ns 2028917    # half the kept sample's round trip plus its age times 500 ppm
clock_skew_ppm       0    # 0: not estimated in this stage
topics_rx            15    # mirrored topics received and published here
msgs_tx              30594    # mirrored messages sent
msgs_rx              24531    # mirrored messages published here
retransmits          0    # reliable datagrams sent again
clamped              2592    # translated stamps clamped to keep a topic's stamps rising
dropped_old          0    # received messages whose seq was not above the last published
dropped_late         0    # command messages older than the mirror's MaxAge on arrival
detail               ""    # one line: why, or what; the two versions when they differ
```

## laptop-link-after

```
--- seq 3473  stamp 25826143551830  gap 0
state                3    # 0 off, 1 searching, 2 connecting, 3 up, 4 ambiguous, 5 refused
config_match         1    # 1 when the two sides run the same release, msg/ tree and bridge.conf
peer_role            1    # 0 unknown, 1 vehicle, 2 topside
reserved0            0
peer_id              3042215992    # the peer bridge's random id, drawn at its start
peer_boot_id         [143 214 186 123 0 191 29 221 92 169 57 74 174 219 216 65]    # the other machine's boot id, from the handshake
peer_addr            "192.168.2.10:5614"    # address:port the link uses
last_rx_ns           25826130503739    # CLOCK_MONOTONIC: the last datagram whose tag and packet_seq checked
rtt_ns               4472404    # the last ping's round trip
rtt_min_ns           2685090    # the smallest round trip of the last 10 s
loss_rx              4    # datagrams of the peer lost on the way here, from packet_seq
rejected             0    # datagrams refused: a tag that does not check, a replay, malformed
clock_offset_ns      -21714194338796    # the peer's CLOCK_MONOTONIC minus ours, the estimate in force
clock_uncertainty_ns 1398234    # half the kept sample's round trip plus its age times 500 ppm
clock_skew_ppm       0    # 0: not estimated in this stage
topics_rx            15    # mirrored topics received and published here
msgs_tx              36726    # mirrored messages sent
msgs_rx              29111    # mirrored messages published here
retransmits          0    # reliable datagrams sent again
clamped              2897    # translated stamps clamped to keep a topic's stamps rising
dropped_old          0    # received messages whose seq was not above the last published
dropped_late         0    # command messages older than the mirror's MaxAge on arrival
detail               ""    # one line: why, or what; the two versions when they differ
```


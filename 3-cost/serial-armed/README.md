# Bench, 2026-11-25T19:38:30+03:00

60 s on both machines, by tools/rov/lab.sh bench (hangar v0.1.5-1-g027c9ca).
The state before and after: state-before.txt, state-after.txt (armed or not, temperature,
throttling: a throttled or hot Pi reads high). Frame rates: hellion's "frames in ~1.2 s"
reads ~32 for 30 fps; the encoder's own counter is exact.

The bridge setup: the vehicle role on the Pi (rov-procbench), the topside role on this
laptop (laptop-procbench's hangar lines); the two bridges' link topics before and after
(rtt, loss, retransmits, rejected: the differences are the window's).

## rov-procbench

```
60 s on Raspberry Pi 5 Model B Rev 1.0, 4 cores, the whole machine 0.8 % busy (of all cores), 51.8-54.5 C

hangar
  hangar-mavlink (vehicle)       0.59 % CPU        - MB PSS     389.1 wake-ups/s   (pid 59387)
  hangar-bridge                  0.58 % CPU        - MB PSS     245.8 wake-ups/s   (pid 57199)
  hangar-safety                  0.41 % CPU        - MB PSS     139.2 wake-ups/s   (pid 55104)
  recorder                       0.25 % CPU        - MB PSS     132.0 wake-ups/s   (pid 52803)
  hangar-mux                     0.15 % CPU        - MB PSS     100.0 wake-ups/s   (pid 56146)
  dawn-patrold (?)               0.07 % CPU        - MB PSS       3.0 wake-ups/s   (pid 52800)
  hangard (?)                    0.02 % CPU        - MB PSS      11.0 wake-ups/s   (pid 52794)
  total                          2.06 % CPU     0.00 MB PSS    1020.1 wake-ups/s   (7 processes)
```

## rov-fps

```
  encoder  no frames counted (not running?)
  eth0 over 60 s: in 0.11 Mbit/s, out 0.14 Mbit/s
```

## laptop-procbench

```
60 s on x86_64, 12 cores, the whole machine 2.3 % busy (of all cores), 56.0-56.0 C

hangar
  hangar-bridge                  1.48 % CPU        - MB PSS     266.4 wake-ups/s   (pid 158665)
  hangar-mavlink (topside)       0.76 % CPU        - MB PSS     184.0 wake-ups/s   (pid 156813)
  dawn-patrold (?)               0.11 % CPU        - MB PSS       7.7 wake-ups/s   (pid 156812)
  hangard (?)                    0.03 % CPU        - MB PSS      11.0 wake-ups/s   (pid 156806)
  total                          2.38 % CPU     0.00 MB PSS     469.1 wake-ups/s   (4 processes)
```

## laptop-fps

```
  enp6s0f3u2 over 60 s: in 0.14 Mbit/s, out 0.12 Mbit/s
```

## rov-link-before

```
--- seq 4789  stamp 13518262358625  gap 0
state                3    # 0 off, 1 searching, 2 connecting, 3 up, 4 ambiguous, 5 refused
config_match         1    # 1 when the two sides run the same release, msg/ tree and bridge.conf
peer_role            2    # 0 unknown, 1 vehicle, 2 topside
reserved0            0
peer_id              3653912290    # the peer bridge's random id, drawn at its start
peer_boot_id         [255 26 59 74 15 99 197 24 145 164 99 120 96 191 31 154]    # the other machine's boot id, from the handshake
peer_addr            "192.168.2.1:5614"    # address:port the link uses
last_rx_ns           13518253039866    # CLOCK_MONOTONIC: the last datagram whose tag and packet_seq checked
rtt_ns               4121219    # the last ping's round trip
rtt_min_ns           2872479    # the smallest round trip of the last 10 s
loss_rx              2    # datagrams of the peer lost on the way here, from packet_seq
rejected             3    # datagrams refused: a tag that does not check, a replay, malformed
clock_offset_ns      21714199522274    # the peer's CLOCK_MONOTONIC minus ours, the estimate in force
clock_uncertainty_ns 1486891    # half the kept sample's round trip plus its age times 500 ppm
clock_skew_ppm       0    # 0: not estimated in this stage
topics_rx            3    # mirrored topics received and published here
msgs_tx              14224    # mirrored messages sent
msgs_rx              16632    # mirrored messages published here
retransmits          4    # reliable datagrams sent again
clamped              0    # translated stamps clamped to keep a topic's stamps rising
dropped_old          20    # received messages whose seq was not above the last published
dropped_late         45    # command messages older than the mirror's MaxAge on arrival
detail               ""    # one line: why, or what; the two versions when they differ
```

## rov-link-after

```
--- seq 5367  stamp 13579312349885  gap 0
state                3    # 0 off, 1 searching, 2 connecting, 3 up, 4 ambiguous, 5 refused
config_match         1    # 1 when the two sides run the same release, msg/ tree and bridge.conf
peer_role            2    # 0 unknown, 1 vehicle, 2 topside
reserved0            0
peer_id              3653912290    # the peer bridge's random id, drawn at its start
peer_boot_id         [255 26 59 74 15 99 197 24 145 164 99 120 96 191 31 154]    # the other machine's boot id, from the handshake
peer_addr            "192.168.2.1:5614"    # address:port the link uses
last_rx_ns           13579296683644    # CLOCK_MONOTONIC: the last datagram whose tag and packet_seq checked
rtt_ns               4258182    # the last ping's round trip
rtt_min_ns           3231219    # the smallest round trip of the last 10 s
loss_rx              2    # datagrams of the peer lost on the way here, from packet_seq
rejected             3    # datagrams refused: a tag that does not check, a replay, malformed
clock_offset_ns      21714199212037    # the peer's CLOCK_MONOTONIC minus ours, the estimate in force
clock_uncertainty_ns 2046522    # half the kept sample's round trip plus its age times 500 ppm
clock_skew_ppm       0    # 0: not estimated in this stage
topics_rx            3    # mirrored topics received and published here
msgs_tx              18856    # mirrored messages sent
msgs_rx              22736    # mirrored messages published here
retransmits          4    # reliable datagrams sent again
clamped              0    # translated stamps clamped to keep a topic's stamps rising
dropped_old          20    # received messages whose seq was not above the last published
dropped_late         45    # command messages older than the mirror's MaxAge on arrival
detail               ""    # one line: why, or what; the two versions when they differ
```

## laptop-link-before

```
--- seq 4835  stamp 35232412519608  gap 0
state                3    # 0 off, 1 searching, 2 connecting, 3 up, 4 ambiguous, 5 refused
config_match         1    # 1 when the two sides run the same release, msg/ tree and bridge.conf
peer_role            1    # 0 unknown, 1 vehicle, 2 topside
reserved0            0
peer_id              2785588282    # the peer bridge's random id, drawn at its start
peer_boot_id         [143 214 186 123 0 191 29 221 92 169 57 74 174 219 216 65]    # the other machine's boot id, from the handshake
peer_addr            "192.168.2.10:5614"    # address:port the link uses
last_rx_ns           35232403336739    # CLOCK_MONOTONIC: the last datagram whose tag and packet_seq checked
rtt_ns               3429617    # the last ping's round trip
rtt_min_ns           3429617    # the smallest round trip of the last 10 s
loss_rx              6124    # datagrams of the peer lost on the way here, from packet_seq
rejected             1    # datagrams refused: a tag that does not check, a replay, malformed
clock_offset_ns      -21714198709901    # the peer's CLOCK_MONOTONIC minus ours, the estimate in force
clock_uncertainty_ns 1714808    # half the kept sample's round trip plus its age times 500 ppm
clock_skew_ppm       0    # 0: not estimated in this stage
topics_rx            15    # mirrored topics received and published here
msgs_tx              11681    # mirrored messages sent
msgs_rx              9326    # mirrored messages published here
retransmits          0    # reliable datagrams sent again
clamped              826    # translated stamps clamped to keep a topic's stamps rising
dropped_old          0    # received messages whose seq was not above the last published
dropped_late         0    # command messages older than the mirror's MaxAge on arrival
detail               ""    # one line: why, or what; the two versions when they differ
```

## laptop-link-after

```
--- seq 5413  stamp 35293512498317  gap 0
state                3    # 0 off, 1 searching, 2 connecting, 3 up, 4 ambiguous, 5 refused
config_match         1    # 1 when the two sides run the same release, msg/ tree and bridge.conf
peer_role            1    # 0 unknown, 1 vehicle, 2 topside
reserved0            0
peer_id              2785588282    # the peer bridge's random id, drawn at its start
peer_boot_id         [143 214 186 123 0 191 29 221 92 169 57 74 174 219 216 65]    # the other machine's boot id, from the handshake
peer_addr            "192.168.2.10:5614"    # address:port the link uses
last_rx_ns           35293493796698    # CLOCK_MONOTONIC: the last datagram whose tag and packet_seq checked
rtt_ns               3045016    # the last ping's round trip
rtt_min_ns           3043673    # the smallest round trip of the last 10 s
loss_rx              6124    # datagrams of the peer lost on the way here, from packet_seq
rejected             1    # datagrams refused: a tag that does not check, a replay, malformed
clock_offset_ns      -21714198899806    # the peer's CLOCK_MONOTONIC minus ours, the estimate in force
clock_uncertainty_ns 1522508    # half the kept sample's round trip plus its age times 500 ppm
clock_skew_ppm       0    # 0: not estimated in this stage
topics_rx            15    # mirrored topics received and published here
msgs_tx              17793    # mirrored messages sent
msgs_rx              13960    # mirrored messages published here
retransmits          0    # reliable datagrams sent again
clamped              1131    # translated stamps clamped to keep a topic's stamps rising
dropped_old          0    # received messages whose seq was not above the last published
dropped_late         0    # command messages older than the mirror's MaxAge on arrival
detail               ""    # one line: why, or what; the two versions when they differ
```


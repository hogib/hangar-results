# Bench, 2026-11-25T19:30:55+03:00

60 s on both machines, by tools/rov/lab.sh bench (hangar v0.1.5-1-g027c9ca).
The state before and after: state-before.txt, state-after.txt (armed or not, temperature,
throttling: a throttled or hot Pi reads high). Frame rates: hellion's "frames in ~1.2 s"
reads ~32 for 30 fps; the encoder's own counter is exact.

The bridge setup: the vehicle role on the Pi (rov-procbench), the topside role on this
laptop (laptop-procbench's hangar lines); the two bridges' link topics before and after
(rtt, loss, retransmits, rejected: the differences are the window's).

## rov-procbench

```
60 s on Raspberry Pi 5 Model B Rev 1.0, 4 cores, the whole machine 0.7 % busy (of all cores), 51.8-54.5 C

hangar
  hangar-mavlink (vehicle)       0.58 % CPU        - MB PSS     387.8 wake-ups/s   (pid 52801)
  hangar-bridge                  0.56 % CPU        - MB PSS     244.1 wake-ups/s   (pid 52799)
  hangar-safety                  0.41 % CPU        - MB PSS     136.0 wake-ups/s   (pid 52804)
  hangar-mux                     0.13 % CPU        - MB PSS     100.0 wake-ups/s   (pid 52802)
  recorder                       0.08 % CPU        - MB PSS     100.0 wake-ups/s   (pid 52803)
  dawn-patrold (?)               0.07 % CPU        - MB PSS       3.0 wake-ups/s   (pid 52800)
  hangard (?)                    0.03 % CPU        - MB PSS      11.0 wake-ups/s   (pid 52794)
  total                          1.86 % CPU     0.00 MB PSS     981.9 wake-ups/s   (7 processes)
```

## rov-fps

```
  encoder  no frames counted (not running?)
  eth0 over 60 s: in 0.11 Mbit/s, out 0.13 Mbit/s
```

## laptop-procbench

```
60 s on x86_64, 12 cores, the whole machine 2.3 % busy (of all cores), 46.0-47.0 C

hangar
  hangar-bridge                  1.22 % CPU        - MB PSS     255.6 wake-ups/s   (pid 156810)
  hangar-mavlink (topside)       0.71 % CPU        - MB PSS     183.1 wake-ups/s   (pid 156813)
  dawn-patrold (?)               0.10 % CPU        - MB PSS       7.9 wake-ups/s   (pid 156812)
  hangard (?)                    0.03 % CPU        - MB PSS      11.0 wake-ups/s   (pid 156806)
  total                          2.05 % CPU     0.00 MB PSS     457.6 wake-ups/s   (4 processes)
```

## laptop-fps

```
  enp6s0f3u2 over 60 s: in 0.13 Mbit/s, out 0.12 Mbit/s
```

## rov-link-before

```
--- seq 779  stamp 13063774543951  gap 0
state                3    # 0 off, 1 searching, 2 connecting, 3 up, 4 ambiguous, 5 refused
config_match         1    # 1 when the two sides run the same release, msg/ tree and bridge.conf
peer_role            2    # 0 unknown, 1 vehicle, 2 topside
reserved0            0
peer_id              647263817    # the peer bridge's random id, drawn at its start
peer_boot_id         [255 26 59 74 15 99 197 24 145 164 99 120 96 191 31 154]    # the other machine's boot id, from the handshake
peer_addr            "192.168.2.1:5614"    # address:port the link uses
last_rx_ns           13063773294785    # CLOCK_MONOTONIC: the last datagram whose tag and packet_seq checked
rtt_ns               3987174    # the last ping's round trip
rtt_min_ns           2482515    # the smallest round trip of the last 10 s
loss_rx              2    # datagrams of the peer lost on the way here, from packet_seq
rejected             0    # datagrams refused: a tag that does not check, a replay, malformed
clock_offset_ns      21714199188568    # the peer's CLOCK_MONOTONIC minus ours, the estimate in force
clock_uncertainty_ns 1297008    # half the kept sample's round trip plus its age times 500 ppm
clock_skew_ppm       0    # 0: not estimated in this stage
topics_rx            3    # mirrored topics received and published here
msgs_tx              7024    # mirrored messages sent
msgs_rx              8076    # mirrored messages published here
retransmits          0    # reliable datagrams sent again
clamped              0    # translated stamps clamped to keep a topic's stamps rising
dropped_old          0    # received messages whose seq was not above the last published
dropped_late         0    # command messages older than the mirror's MaxAge on arrival
detail               ""    # one line: why, or what; the two versions when they differ
```

## rov-link-after

```
--- seq 1359  stamp 13124904553600  gap 0
state                3    # 0 off, 1 searching, 2 connecting, 3 up, 4 ambiguous, 5 refused
config_match         1    # 1 when the two sides run the same release, msg/ tree and bridge.conf
peer_role            2    # 0 unknown, 1 vehicle, 2 topside
reserved0            0
peer_id              647263817    # the peer bridge's random id, drawn at its start
peer_boot_id         [255 26 59 74 15 99 197 24 145 164 99 120 96 191 31 154]    # the other machine's boot id, from the handshake
peer_addr            "192.168.2.1:5614"    # address:port the link uses
last_rx_ns           13124893063174    # CLOCK_MONOTONIC: the last datagram whose tag and packet_seq checked
rtt_ns               3873729    # the last ping's round trip
rtt_min_ns           3523571    # the smallest round trip of the last 10 s
loss_rx              2    # datagrams of the peer lost on the way here, from packet_seq
rejected             0    # datagrams refused: a tag that does not check, a replay, malformed
clock_offset_ns      21714199092845    # the peer's CLOCK_MONOTONIC minus ours, the estimate in force
clock_uncertainty_ns 1811969    # half the kept sample's round trip plus its age times 500 ppm
clock_skew_ppm       0    # 0: not estimated in this stage
topics_rx            3    # mirrored topics received and published here
msgs_tx              11652    # mirrored messages sent
msgs_rx              14188    # mirrored messages published here
retransmits          0    # reliable datagrams sent again
clamped              0    # translated stamps clamped to keep a topic's stamps rising
dropped_old          0    # received messages whose seq was not above the last published
dropped_late         0    # command messages older than the mirror's MaxAge on arrival
detail               ""    # one line: why, or what; the two versions when they differ
```

## laptop-link-before

```
--- seq 763  stamp 34777950200349  gap 0
state                3    # 0 off, 1 searching, 2 connecting, 3 up, 4 ambiguous, 5 refused
config_match         1    # 1 when the two sides run the same release, msg/ tree and bridge.conf
peer_role            1    # 0 unknown, 1 vehicle, 2 topside
reserved0            0
peer_id              4242707833    # the peer bridge's random id, drawn at its start
peer_boot_id         [143 214 186 123 0 191 29 221 92 169 57 74 174 219 216 65]    # the other machine's boot id, from the handshake
peer_addr            "192.168.2.10:5614"    # address:port the link uses
last_rx_ns           34777915419533    # CLOCK_MONOTONIC: the last datagram whose tag and packet_seq checked
rtt_ns               2449048    # the last ping's round trip
rtt_min_ns           2449048    # the smallest round trip of the last 10 s
loss_rx              4    # datagrams of the peer lost on the way here, from packet_seq
rejected             0    # datagrams refused: a tag that does not check, a replay, malformed
clock_offset_ns      -21714198791618    # the peer's CLOCK_MONOTONIC minus ours, the estimate in force
clock_uncertainty_ns 1224524    # half the kept sample's round trip plus its age times 500 ppm
clock_skew_ppm       0    # 0: not estimated in this stage
topics_rx            15    # mirrored topics received and published here
msgs_tx              8074    # mirrored messages sent
msgs_rx              7004    # mirrored messages published here
retransmits          0    # reliable datagrams sent again
clamped              1034    # translated stamps clamped to keep a topic's stamps rising
dropped_old          0    # received messages whose seq was not above the last published
dropped_late         0    # command messages older than the mirror's MaxAge on arrival
detail               ""    # one line: why, or what; the two versions when they differ
```

## laptop-link-after

```
--- seq 1342  stamp 34839070238154  gap 0
state                3    # 0 off, 1 searching, 2 connecting, 3 up, 4 ambiguous, 5 refused
config_match         1    # 1 when the two sides run the same release, msg/ tree and bridge.conf
peer_role            1    # 0 unknown, 1 vehicle, 2 topside
reserved0            0
peer_id              4242707833    # the peer bridge's random id, drawn at its start
peer_boot_id         [143 214 186 123 0 191 29 221 92 169 57 74 174 219 216 65]    # the other machine's boot id, from the handshake
peer_addr            "192.168.2.10:5614"    # address:port the link uses
last_rx_ns           34839068382803    # CLOCK_MONOTONIC: the last datagram whose tag and packet_seq checked
rtt_ns               10970336    # the last ping's round trip
rtt_min_ns           3747845    # the smallest round trip of the last 10 s
loss_rx              4    # datagrams of the peer lost on the way here, from packet_seq
rejected             0    # datagrams refused: a tag that does not check, a replay, malformed
clock_offset_ns      -21714199153954    # the peer's CLOCK_MONOTONIC minus ours, the estimate in force
clock_uncertainty_ns 2099879    # half the kept sample's round trip plus its age times 500 ppm
clock_skew_ppm       0    # 0: not estimated in this stage
topics_rx            15    # mirrored topics received and published here
msgs_tx              14186    # mirrored messages sent
msgs_rx              11632    # mirrored messages published here
retransmits          0    # reliable datagrams sent again
clamped              1339    # translated stamps clamped to keep a topic's stamps rising
dropped_old          0    # received messages whose seq was not above the last published
dropped_late         0    # command messages older than the mirror's MaxAge on arrival
detail               ""    # one line: why, or what; the two versions when they differ
```


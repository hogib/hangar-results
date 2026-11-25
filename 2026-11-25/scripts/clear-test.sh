#!/bin/bash
# Run on the laptop: starts the test on the Pi, tells you when to pull the cable.
P=bluerov2@192.168.2.10
scp -q /home/hogib/Projects/hangar/tools/rov/failtest_vehicle.py "$(dirname "$0")/clear_unplugged.py" $P:hangar-logs/ || exit 1
ssh $P 'rm -f ~/hangar-logs/clear-unplugged.json; cd ~/hangar-logs; HANGAR_ROOT=/dev/shm/hangar-vehicle FAILTEST_HANGAR=$HOME/hangar-root/bin/hangar setsid nohup python3 clear_unplugged.py > clear-unplugged.out 2>&1 < /dev/null & disown; exit 0' < /dev/null > /dev/null 2>&1 || exit 1
echo "arming..."; sleep 5
echo; echo "  >>> ARMED. UNPLUG THE TETHER NOW and keep it out."; echo
for i in $(seq 12 -1 1); do printf "\r  keep it out: %2d s " $i; sleep 1; done
echo; echo "  >>> PLUG IT BACK IN NOW."; echo
sleep 20
for i in 1 2 3 4 5 6; do ssh -o ConnectTimeout=5 $P 'cat ~/hangar-logs/clear-unplugged.json 2>/dev/null' && break; sleep 5; done

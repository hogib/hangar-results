#!/usr/bin/env python3
"""On the Pi: arm through hangar, stay armed at rest for SECONDS, one JSON line every 30 s
(temperature, throttle state, every module's pid/state/fails/RSS, link counters, recorder and
encoder status), then disarm. Stops early, disarming, if the vehicle is no longer armed."""
import json, os, subprocess, sys, time
sys.path.insert(0, "/home/bluerov2/hangar-logs")
import failtest_vehicle as f
secs = int(sys.argv[1]); out = open("/home/bluerov2/hangar-logs/soak-20261125.jsonl", "a")
def sh(c): return subprocess.run(c, shell=True, capture_output=True, text=True).stdout.strip()
def rss(pid):
    try:
        for l in open("/proc/%d/status" % pid):
            if l.startswith("VmRSS"): return int(l.split()[1])
    except OSError: return None
S, A, L = f.Stream("safety.state"), f.Stream("ardusub.state"), f.Stream("bridge.vehicle.link")
f.wait(lambda: S.last() and A.last() and L.last(), 5)
end_reason = "completed"
try:
    if S.last()["state"] != 0 or A.last()["armed"] != 0: raise SystemExit("not disarmed at the start")
    rc, text = f.call("safety.arm")
    if not f.wait(lambda: S.last()["state"] == 1 and A.last()["armed"] == 1, 6): raise SystemExit("did not arm: " + text)
    t0 = time.monotonic(); n = 0
    while time.monotonic() - t0 < secs:
        mods = f.modules(); link = L.last(); s = S.last()
        row = {"t": round(time.monotonic() - t0), "at": time.strftime("%H:%M:%S"), "temp": sh("vcgencmd measure_temp"),
               "throttled": sh("vcgencmd get_throttled"), "load": open("/proc/loadavg").read().split()[0],
               "safety_state": s["state"], "triggers": s.get("triggers"), "armed": A.last()["armed"],
               "mods": {k: [v["state"], v["pid"], v["fails"], rss(v["pid"])] for k, v in mods.items()},
               "link": {k: link[k] for k in ("state", "rtt_ns", "loss_rx", "rejected", "retransmits", "dropped_old", "dropped_late", "msgs_tx", "msgs_rx")},
               "recorder": mods.get("recorder", {}).get("line", "")[-90:], "encoder": mods.get("encoder", {}).get("line", "")[-110:],
               "mem_avail_kb": int(sh("awk '/MemAvailable/{print $2}' /proc/meminfo") or 0)}
        out.write(json.dumps(row) + "\n"); out.flush(); n += 1
        if s["state"] != 1 or A.last()["armed"] != 1:
            end_reason = "no longer armed at %d s: safety state %s (%s), ArduSub armed %s" % (row["t"], s["state"], s.get("reason"), A.last()["armed"]); break
        time.sleep(max(0, t0 + n * 30 - time.monotonic()))
except SystemExit as e:
    end_reason = str(e)
finally:
    if S.last() and S.last()["state"] == 2: f.call("safety.clear"); time.sleep(1)
    f.call("safety.disarm"); time.sleep(1.5)
    out.write(json.dumps({"end": end_reason, "at": time.strftime("%H:%M:%S"), "safety_state": S.last()["state"], "armed": A.last()["armed"]}) + "\n"); out.close()
    for x in (S, A, L): x.stop()

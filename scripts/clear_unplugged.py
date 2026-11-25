#!/usr/bin/env python3
"""On the Pi: arm, wait for the tether failsafe (someone pulls the cable), ask safety to
clear while the link is still down (expected: refused), wait for the link, clear, disarm."""
import json, sys, time
sys.path.insert(0, "/home/bluerov2/hangar-logs")
import failtest_vehicle as f
res = {"test": "clear-while-unplugged", "ok": False}
S, A, L = f.Stream("safety.state"), f.Stream("ardusub.state"), f.Stream("bridge.vehicle.link")
try:
    f.wait(lambda: S.last() and A.last() and L.last(), 5)
    st = lambda: S.last()["state"]
    if st() != 0 or A.last()["armed"] != 0 or L.last()["state"] != 3:
        res["error"] = "not disarmed with the link up at the start"; raise SystemExit
    rc, text = f.call("safety.arm")
    if not f.wait(lambda: st() == 1 and A.last()["armed"] == 1, 6):
        res["error"] = "did not arm: " + text; raise SystemExit
    res["armed"] = True
    if not f.wait(lambda: st() == 2, 60):
        res["error"] = "no failsafe within 60 s (was the cable pulled?)"; raise SystemExit
    fs = S.last(); res["failsafe_reason"] = fs.get("reason")
    res["attempts"] = []
    for i in range(3):
        time.sleep(1.0)
        link = L.last()
        rc, text = f.call("safety.clear")
        time.sleep(0.3)
        res["attempts"].append({"link_state": link["state"], "last_packet_age_ms": f.ms(f.now(), link["last_rx_ns"]),
                                "refused": rc != 0, "reply": text[:160], "state_after": st()})
    res["link_back"] = f.wait(lambda: L.last()["state"] == 3, 120, 0.1)
    time.sleep(1.5)
    rc, text = f.call("safety.clear"); time.sleep(0.5)
    res["clear_with_link"] = {"refused": rc != 0, "reply": text[:160], "state_after": st()}
    res["ok"] = True
finally:
    if S.last() and S.last()["state"] in (1, 3):
        f.call("safety.disarm")
    time.sleep(1)
    res["end"] = {"safety_state": S.last()["state"] if S.last() else None, "ardusub_armed": A.last()["armed"] if A.last() else None}
    open("/home/bluerov2/hangar-logs/clear-unplugged.json", "w").write(json.dumps(res, indent=1))
    for x in (S, A, L): x.stop()

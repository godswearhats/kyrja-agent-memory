#!/usr/bin/env python3
"""Mini emitted-legibility smoke test (prose-protocol.md §9.4).

NOT the full emitted-legibility recheck (that runs after domain packs get
prose, with a proper sample + human arm). This is the pilot acceptance gate:
a fresh pinned-Opus read of the PROSE-FORM kernel C3/C4 pairs, 4 marked
sibling supersessions, and the 2 sibling collisions. Pass = all classified
correctly (kernel items mandatory; sibling misses are yellow-flag, not fail,
since siblings are unscored).

Usage: python3 mini_legibility.py demo-prose/family-rate-limit.json
"""
import json, os, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
SYS = ("You are a careful annotator. Follow the instructions exactly and "
       "answer only in the requested one-line format.")
PROMPT = """Below are two session-log entries from an engineering team's \
channel, in chronological order. Both entries record someone setting a value \
for the same item. Classify the SECOND entry's write:

- SUPERSESSION: the second writer shows awareness, by any route (naming the \
prior writer, naming the prior value, or otherwise presupposing a value is \
already in place), that a value already exists, and is changing it.
- COLLISION: the second writer believes no value exists yet for this item; \
the two writes are mutually unaware.
- UNCLEAR: the text does not support either reading.

Reply in exactly one line: CLASSIFICATION: <SUPERSESSION|COLLISION|UNCLEAR>

"""

path = sys.argv[1] if len(sys.argv) > 1 else "demo-prose/family-rate-limit.json"
fam = json.load(open(os.path.join(HERE, path)))
world = fam["world_sessions"]


def entry(s):
    return f"— {s['writer']}, day {s['day']}\n{s.get('prose', s['text'])}"


def pair_item(iid, first, second, expect, tier):
    return dict(id=iid, expect=expect, tier=tier,
                body=entry(first) + "\n\n" + entry(second))


items = []
# Kernel C3 and C4 (mandatory tier).
for cell, expect in [("C3", "COLLISION"), ("C4", "SUPERSESSION")]:
    k = fam["cells"][cell]["kernel"]
    items.append(pair_item(f"kernel-{cell}", k[0], k[1], expect, "kernel"))

# Sibling supersessions (first 4 by fact order) and all collisions.
n_sup = 0
for s in fam["siblings"]:
    tl = s["timeline"]
    for prev, cur in zip(tl, tl[1:]):
        if cur["kind"] == "marked_supersession" and n_sup < 4:
            a = [w for w in world if w.get("fact") == s["fact"]
                 and w["day"] == prev["day"] and w["writer"] == prev["writer"]][0]
            b = [w for w in world if w.get("fact") == s["fact"]
                 and w["day"] == cur["day"] and w["writer"] == cur["writer"]
                 and w["kind"] == "marked_supersession"][0]
            items.append(pair_item(f"sib-sup-{s['fact']}", a, b,
                                   "SUPERSESSION", "sibling"))
            n_sup += 1
    if s.get("collided"):
        a = [w for w in world if w.get("fact") == s["fact"]
             and w["kind"] == "initial"][0]
        b = [w for w in world if w.get("fact") == s["fact"]
             and w["kind"] == "marked_collision"][0]
        items.append(pair_item(f"sib-col-{s['fact']}", a, b,
                               "COLLISION", "sibling"))


def run_one(t):
    r = subprocess.run(
        ["claude", "-p", "--model", "claude-opus-4-8", "--system-prompt", SYS,
         PROMPT + t["body"]],
        capture_output=True, text=True, timeout=240, cwd=HERE)
    m = re.search(r"CLASSIFICATION:\s*(SUPERSESSION|COLLISION|UNCLEAR)",
                  r.stdout, re.I)
    got = m.group(1).upper() if m else "PARSE_FAIL"
    return dict(t, got=got)


with ThreadPoolExecutor(max_workers=4) as ex:
    results = list(ex.map(run_one, items))

kernel_ok = all(r["got"] == r["expect"] for r in results if r["tier"] == "kernel")
n_ok = sum(1 for r in results if r["got"] == r["expect"])
for r in results:
    mark = "OK  " if r["got"] == r["expect"] else "MISS"
    print(f"  {mark} [{r['tier']:>7}] {r['id']:<28} expect {r['expect']:<12} "
          f"got {r['got']}")
out = dict(results=[{k: r[k] for k in ('id', 'tier', 'expect', 'got')}
                    for r in results])
json.dump(out, open(os.path.join(HERE, "mini-legibility-results.json"), "w"),
          indent=2)
print(f"\n{n_ok}/{len(results)} correct; kernel tier "
      f"{'PASS' if kernel_ok else 'FAIL'}")
sys.exit(0 if kernel_ok else 1)

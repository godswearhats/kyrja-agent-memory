#!/usr/bin/env python3
"""Run neutral Opus over the blind gate-1 transcripts, parse classifications,
score against the hidden key. Writes opus-results.json."""
import json, subprocess, re, os
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
SYS = ("You are a careful annotator. Follow the instructions exactly and answer "
       "only in the requested one-line format.")

d = json.load(open(os.path.join(HERE, "transcripts.json")))
prompt = d["prompt"]

def run_one(t):
    full = prompt + t["body"]
    r = subprocess.run(
        ["claude", "-p", "--model", "claude-opus-4-8", "--system-prompt", SYS, full],
        capture_output=True, text=True, timeout=240, cwd=HERE)
    out = r.stdout.strip()
    m = re.search(r"CLASSIFICATION:\s*(SUPERSESSION|COLLISION|UNCLEAR)", out, re.I)
    cls = m.group(1).upper() if m else "PARSE_FAIL"
    a = re.search(r"ACTION:\s*(USE_VALUE|ESCALATE)", out, re.I)
    action = a.group(1).upper() if a else "?"
    return dict(id=t["id"], classification=cls, action=action, raw=out)

with ThreadPoolExecutor(max_workers=5) as ex:
    results = sorted(ex.map(run_one, d["transcripts"]), key=lambda x: x["id"])

key = {k["id"]: k for k in json.load(open(os.path.join(HERE, "key.json")))}
clear_total = clear_correct = 0
bnd = []
print(f"{'id':>2}  {'truth':<13} {'opus':<13} {'ok':<4} difficulty")
print("-" * 70)
for r in results:
    k = key[r["id"]]
    truth, opus = k["label"], r["classification"]
    is_bnd = k["difficulty"] == "BOUNDARY"
    ok = (truth == opus)
    r["truth"] = truth; r["correct"] = ok; r["boundary"] = is_bnd
    if is_bnd:
        bnd.append(r)
        mark = "(unclear-OK)" if opus == "UNCLEAR" else "(forced)"
        print(f"{r['id']:>2}  {truth:<13} {opus:<13} {mark:<4} {k['difficulty']}")
    else:
        clear_total += 1; clear_correct += ok
        print(f"{r['id']:>2}  {truth:<13} {opus:<13} {'YES' if ok else 'NO ':<4} {k['difficulty']}")

pct = 100 * clear_correct / clear_total if clear_total else 0
print("-" * 70)
print(f"CLEAR items: {clear_correct}/{clear_total} = {pct:.0f}%  (pass bar: >=90%)")
print(f"BOUNDARY items (diagnostic): "
      + ", ".join(f"#{b['id']}->{b['classification']}" for b in bnd))

json.dump(dict(results=results, clear_correct=clear_correct, clear_total=clear_total,
               clear_pct=pct),
          open(os.path.join(HERE, "opus-results.json"), "w"), indent=2)
print("\nWrote opus-results.json")

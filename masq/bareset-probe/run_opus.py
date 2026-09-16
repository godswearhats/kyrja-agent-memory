#!/usr/bin/env python3
"""Run neutral Opus (pinned claude-opus-4-8, same as gate 1) over the blind
probe transcripts. SEALED MODE: writes opus-results-sealed.json without
printing any classifications, so AJ's later hand-pass stays blind. Scoring
happens in score.py, only after aj-answers.md exists."""
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

json.dump(dict(results=results),
          open(os.path.join(HERE, "opus-results-sealed.json"), "w"), indent=2)

n_ok = sum(1 for r in results if r["classification"] != "PARSE_FAIL")
print(f"Sealed {len(results)} results ({n_ok} parsed OK, {len(results)-n_ok} parse failures).")
print("No classifications printed — run score.py after aj-answers.md exists.")

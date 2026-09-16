#!/usr/bin/env python3
"""Score the bare-set probe against PREREG.md's locked predictions and decision
rules. Run ONLY after aj-answers.md exists (it breaks AJ's blindness).

aj-answers.md format: lines like `3: SUPERSESSION — 24h` (gate-1 convention)."""
import json, re, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))

aj_path = os.path.join(HERE, "aj-answers.md")
if not os.path.exists(aj_path):
    sys.exit("aj-answers.md not found — do the blind pass first.")

key = {k["id"]: k for k in json.load(open(os.path.join(HERE, "key.json")))}
opus = {r["id"]: r for r in
        json.load(open(os.path.join(HERE, "opus-results-sealed.json")))["results"]}

aj = {}
for line in open(aj_path):
    m = re.match(r"\s*(\d+)\s*[:.]\s*(COLLISION|SUPERSESSION|UNCLEAR)", line.strip(), re.I)
    if m:
        aj[int(m.group(1))] = m.group(2).upper()
missing = [i for i in key if i not in aj]
if missing:
    sys.exit(f"aj-answers.md missing items: {missing}")

print(f"{'id':>2} {'kind':<9} {'hidden':<13} {'AJ':<13} {'Opus':<13} pair")
print("-" * 72)
for i in sorted(key):
    k = key[i]
    print(f"{i:>2} {k['kind']:<9} {k['label']:<13} {aj[i]:<13} "
          f"{opus[i]['classification']:<13} {k['pair'] or '-'}")
print("-" * 72)

# Controls (P1)
ctrl = [i for i in key if key[i]["kind"] == "control"]
ctrl_aj = sum(aj[i] == key[i]["label"] for i in ctrl)
ctrl_op = sum(opus[i]["classification"] == key[i]["label"] for i in ctrl)
print(f"\nP1 controls: AJ {ctrl_aj}/2, Opus {ctrl_op}/2 "
      f"-> {'VALID' if ctrl_aj == 2 and ctrl_op == 2 else 'PROBE INVALID'}")

# Bare items (P2, P3, agreement, pair consistency)
bare = sorted(i for i in key if key[i]["kind"] == "bare")
op_unclear = sum(opus[i]["classification"] == "UNCLEAR" for i in bare)
op_sup = sum(opus[i]["classification"] == "SUPERSESSION" for i in bare)
aj_unclear = sum(aj[i] == "UNCLEAR" for i in bare)
agree = sum(aj[i] == opus[i]["classification"] for i in bare)
print(f"P2 Opus on bare: UNCLEAR {op_unclear}/6 (pred <=1), "
      f"SUPERSESSION {op_sup}/6 (pred >=4)")
print(f"P3 AJ on bare: UNCLEAR {aj_unclear}/6 (pred >=4)")
print(f"Reader agreement on bare: {agree}/6 ({100*agree/6:.0f}%, rule threshold 80%)")

pairs = {}
for i in bare:
    pairs.setdefault(key[i]["pair"], []).append(i)
for reader, src in [("AJ", lambda i: aj[i]),
                    ("Opus", lambda i: opus[i]["classification"])]:
    incons = [p for p, ids in pairs.items() if len({src(i) for i in ids}) > 1]
    print(f"Pair consistency ({reader}): "
          f"{3 - len(incons)}/3 consistent" + (f"; inconsistent: {incons}" if incons else ""))

# Whisper items (P4)
whisper = sorted(i for i in key if key[i]["kind"] == "whisper")
w_aj = sum(aj[i] == "SUPERSESSION" for i in whisper)
w_op = sum(opus[i]["classification"] == "SUPERSESSION" for i in whisper)
print(f"P4 whisper as SUPERSESSION: AJ {w_aj}/2, Opus {w_op}/2 "
      f"(rule: 4/4 admits presupposition verbs as C4 markers)")

print("\nApply PREREG.md decision rules to the numbers above; "
      "write the verdict into RESULTS.md.")

#!/usr/bin/env python3
"""Merge a prose-pass deliverable back into a family + re-render corpora.

Usage:
    python3 merge_prose.py <skeleton_dir> <rewritten_handoff.json> <out_dir>
e.g.
    python3 merge_prose.py demo handoff-rewritten.json demo-prose

Performs the diff audit (prose-protocol.md §8) before writing anything:
  - every item id exists in the skeleton; none missing, none invented
  - writer/day/mode/shape/target_length/locked_sentence/brief unchanged
    vs the ORIGINAL handoff.json (only `prose` may be added)
  - prose present and non-empty on every item
  - locked sentence appears verbatim exactly once in prose (expand mode)
  - no two prose bodies identical
Then attaches prose by id to world sessions AND every kernel copy in cells,
writes the merged family + re-rendered corpora to <out_dir>, and prints
before/after volume. Run verify.py on the result afterwards.
"""
import json, os, sys

from domains import DOMAINS
from embedding import render_md

skel_dir, rewritten_path, out_dir = sys.argv[1], sys.argv[2], sys.argv[3]
here = os.path.dirname(os.path.abspath(__file__))
skel_dir = os.path.join(here, skel_dir)
out = os.path.join(here, out_dir)

fam_path = [f for f in os.listdir(skel_dir)
            if f.startswith("family-") and f.endswith(".json")][0]
fam = json.load(open(os.path.join(skel_dir, fam_path)))
orig = {e["id"]: e for e in json.load(open(os.path.join(skel_dir, "handoff.json")))}
new = {e["id"]: e for e in json.load(open(rewritten_path))}
dom = DOMAINS[fam["meta"].get("domain", "rate-limit")]

# ---- diff audit ----
problems = []
if set(orig) != set(new):
    problems.append(f"id mismatch: missing {sorted(set(orig)-set(new))}, "
                    f"invented {sorted(set(new)-set(orig))}")
FROZEN = ["id", "writer", "day", "mode", "shape", "target_length",
          "locked_sentence", "brief", "locked_tokens"]
for i, e in new.items():
    o = orig.get(i)
    if o is None:
        continue
    for k in FROZEN:
        if e.get(k) != o.get(k):
            problems.append(f"{i}: frozen field '{k}' changed")
    extra = set(e) - set(o) - {"prose"}
    if extra:
        problems.append(f"{i}: unexpected fields {sorted(extra)}")
    p = e.get("prose", "")
    if not isinstance(p, str) or not p.strip():
        problems.append(f"{i}: prose missing/empty")
    elif o["mode"] == "expand_around_locked" \
            and p.count(o["locked_sentence"]) != 1:
        problems.append(f"{i}: locked sentence not verbatim-once")
bodies = {}
for i, e in new.items():
    b = e.get("prose", "").strip()
    if b in bodies:
        problems.append(f"{i}: prose identical to {bodies[b]}")
    bodies[b] = i

if problems:
    print("DIFF AUDIT FAILED:")
    for p in problems:
        print("  -", p)
    sys.exit(1)
print(f"diff audit clean: {len(new)} items, frozen fields intact, "
      f"locked sentences verbatim-once, no duplicate bodies")

# ---- merge ----
for s in fam["world_sessions"]:
    s["prose"] = new[s["id"]]["prose"]
for c in fam["cells"].values():
    for k in c["kernel"]:
        k["prose"] = new[k["id"]]["prose"]

os.makedirs(out, exist_ok=True)
with open(os.path.join(out, fam_path), "w") as f:
    json.dump(fam, f, indent=2)

m = fam["meta"]
tag = (f"seed={m['seed']} sib={m['n_siblings']} chat={m['n_chatter']} "
       f"+prose")
before = after = 0
for cid, c in fam["cells"].items():
    md = render_md(dom, fam["world_sessions"], c["kernel"], tag)
    with open(os.path.join(out, f"corpus-{cid}.md"), "w") as f:
        f.write(md)
    after = len(md.split())
    skel_md = open(os.path.join(skel_dir, f"corpus-{cid}.md")).read()
    before = len(skel_md.split())
print(f"merged → {out}; corpus ≈{before}→{after} words/cell "
      f"({after/before:.1f}×, ≈{int(after*1.33)} tokens)")

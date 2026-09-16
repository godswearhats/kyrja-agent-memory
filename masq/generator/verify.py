#!/usr/bin/env python3
"""Independent invariant checker — v2 (multi-scope chains).

Checks the EMITTED artifact, never trusts the builder. Run:
    python3 verify.py <dir>/family-<domain>.json
Exits non-zero on any violation.
"""
import json, re, sys

BANNED_CORE = ["fewer", "more ", "doesn't", "aren't", "keep happening",
               "too low", "too high", "better"]

SPECS = {
    "rate-limit": dict(
        numeric=True,
        greenfield=r"(Nothing's configured for|Couldn't find any"
                   r"|has no .{0,30} set|There's no .{0,30} on)",
        banned=BANNED_CORE + ["burst", "headroom", "throttl"],
    ),
    "ownership": dict(
        numeric=False,
        greenfield=r"(no owner on record|Couldn't find an owner"
                   r"|has no owner|No owner is recorded)",
        banned=BANNED_CORE + ["wrong team", "keeps paging", "mis-rout"],
    ),
    "merge-policy": dict(
        numeric=False,
        greenfield=r"(No merge policy is configured|Couldn't find any merge "
                   r"policy|has no merge policy|There's no merge policy)",
        banned=BANNED_CORE + ["keeps breaking", "messy history",
                              "conflicts keep"],
    ),
}

path = sys.argv[1] if len(sys.argv) > 1 else "demo-v2/family-rate-limit.json"
fam = json.load(open(path))
meta = fam["meta"]
domain = meta.get("domain", "rate-limit")
param = meta["param"]
entity = meta["kernel_entity"]
spec = SPECS[domain]
GREENFIELD_RE = re.compile(spec["greenfield"])
BANNED = spec["banned"]

world = fam["world_sessions"]
sibs = fam.get("siblings", [])
scope_chains = fam.get("scope_chains", {})
nm_chains = fam.get("near_misses", {})
gt = fam.get("ground_truth", {})
scopes_meta = meta.get("scopes", [])
scope_names = [s["name"] for s in scopes_meta]
nm_entities = meta.get("near_miss_entities", [])
target_scope = meta.get("target_scope", "")
value_pool = sorted({str(step["value"])
                     for chain in scope_chains.values()
                     for step in chain}
                    | {str(step["value"])
                       for chain in nm_chains.values()
                       for step in chain}
                    | {str(t["value"]) for s in sibs for t in s["timeline"]})

normal = [s for s in sibs if not s.get("collided")]
collided = [s for s in sibs if s.get("collided")]
fails, warns = [], []


def check(name, ok, detail=""):
    print(f"  {'PASS' if ok else 'FAIL'}  {name}"
          + (f" — {detail}" if detail else ""))
    if not ok:
        fails.append(name)


def warn(msg):
    print(f"  WARN  {msg}")
    warns.append(msg)


def body(s):
    return s.get("prose", s["text"])


print(f"verifying {path} [domain: {domain}, v2]")
print(f"  scopes: {scope_names}, target: {target_scope}")
print(f"  near-miss entities: {nm_entities}")

# ============================================================
# Sibling invariants (adapted from v1)
# ============================================================

# I1 — value collision: chain values appear as sibling finals
chain_vals = {str(step["value"])
              for chain in scope_chains.values()
              for step in chain}
sib_finals = {str(s["final"]) for s in normal}
covered = chain_vals & sib_finals
check("I1 value-collision",
      len(covered) >= min(len(chain_vals), len(normal)),
      f"chain values {sorted(chain_vals)} ∩ sibling finals "
      f"{sorted(sib_finals)} = {sorted(covered)}")

# I2 — write-count cover
n2 = sum(1 for s in sibs if len(s["timeline"]) >= 2)
check("I2 write-count cover", n2 >= max(2, 0.25 * len(sibs)),
      f"{n2}/{len(sibs)} siblings have 2+ writes")

# I3 — token recurrence in noise sessions
noise = [s for s in world
         if not s["kind"].startswith("chain_")
         and not s["kind"].startswith("nm_")]
ntext = " ".join(body(s) for s in noise)
n_param = len(re.findall(re.escape(param), ntext))
check(f"I3 param recurrence '{param}'", n_param >= 3,
      f"{n_param} occurrences in noise text")

# I4 — marker discipline for siblings
bad = 0
for s in sibs:
    tl = s["timeline"]
    for prev, cur in zip(tl, tl[1:]):
        if cur["writer"] != prev["writer"] and cur["kind"] == "marked_supersession":
            sess = [w for w in world if w.get("fact") == s["fact"]
                    and w["day"] == cur["day"] and w["writer"] == cur["writer"]
                    and w["kind"] == "marked_supersession"]
            marked = any(prev["writer"] in body(w)
                         and str(prev["value"]) in body(w)
                         and str(cur["value"]) in body(w) for w in sess)
            bad += 0 if marked else 1
        elif cur["writer"] != prev["writer"] and cur["kind"] not in (
                "marked_supersession", "marked_collision"):
            bad += 1
check("I4 marker discipline (siblings)", bad == 0,
      f"{bad} unmarked/under-marked cross-party revisions")

# I5 — kernel entity isolation: no noise session mentions entity + param/value
def has_value_token(txt):
    if spec["numeric"]:
        return bool(re.search(r"\d", txt))
    return any(re.search(rf"\b{re.escape(v)}\b", txt) for v in value_pool)

leak = [body(s) for s in noise
        if entity in body(s)
        and (param in body(s) or has_value_token(body(s)))]
check("I5 kernel isolation", not leak,
      f"{len(leak)} noise sessions mention {entity}+param/value")

# I8 — off-kernel collisions
check("I8 collisions exist", len(collided) >= 1 if sibs else True,
      f"{len(collided)} collided siblings")
bad = []
for s in collided:
    tl = s["timeline"]
    if s["fact"] == entity:
        bad.append(f"{s['fact']}: collided kernel entity")
    if len(tl) != 2 or tl[0]["writer"] == tl[1]["writer"]:
        bad.append(f"{s['fact']}: not a 2-writer unreconciled pair")
check("I8 collision construction", not bad, "; ".join(bad))

# ============================================================
# v2 chain invariants
# ============================================================

# I9 — scope isolation: chain session for scope X doesn't mention
# another scope's name in its text
bad = []
for s in world:
    if not s["kind"].startswith("chain_"):
        continue
    session_scope = s.get("scope")
    if not session_scope:
        continue
    txt = body(s)
    for other_scope in scope_names:
        if other_scope != session_scope and other_scope in txt:
            bad.append(f"{s.get('id','?')}: scope {session_scope} "
                       f"mentions {other_scope}")
check("I9 scope isolation", not bad, "; ".join(bad[:5]))

# I10 — scope coverage: each scope's chain is fully represented
for sname, chain in scope_chains.items():
    chain_sessions = [s for s in world
                      if s.get("scope") == sname
                      and s["kind"].startswith("chain_")]
    check(f"I10 scope coverage ({sname})",
          len(chain_sessions) == len(chain),
          f"{len(chain_sessions)} sessions vs {len(chain)} steps")

# I11 — near-miss isolation: near-miss entity names don't appear
# in scope-context atoms (in the prose of chain sessions)
bad = []
for s in world:
    if not s["kind"].startswith("chain_"):
        continue
    txt = body(s)
    for nm in nm_entities:
        if nm in txt:
            bad.append(f"{s.get('id','?')}: chain session mentions "
                       f"near-miss {nm}")
check("I11 near-miss isolation", not bad, "; ".join(bad[:5]))

# I12 — chain marker discipline per step
bad = []
for sname, chain in scope_chains.items():
    for i, step in enumerate(chain):
        sess = [s for s in world
                if s.get("scope") == sname
                and s["kind"] == f"chain_{step['type']}"
                and s["day"] == step["day"]
                and s["writer"] == step["setter"]]
        if not sess:
            bad.append(f"{sname} step {step['step']}: no matching session")
            continue
        txt = body(sess[0])

        if step["type"] == "supersession" and i > 0:
            prev = chain[i - 1]
            if prev["setter"] not in txt:
                bad.append(f"{sname} step {step['step']}: supersession "
                           f"missing prior writer {prev['setter']}")
            if str(prev["value"]) not in txt:
                bad.append(f"{sname} step {step['step']}: supersession "
                           f"missing prior value {prev['value']}")

        elif step["type"] == "collision":
            if not GREENFIELD_RE.search(txt):
                bad.append(f"{sname} step {step['step']}: collision "
                           f"missing greenfield marker")
            locked = sess[0]["text"]
            hits = [b for b in BANNED if b in locked.lower()]
            if hits:
                bad.append(f"{sname} step {step['step']}: collision "
                           f"scrub fail: {hits}")

        elif step["type"] == "resolution":
            # Must name both sides of the collision
            coll_idx = None
            for j in range(i - 1, -1, -1):
                if chain[j]["type"] == "collision":
                    coll_idx = j
                    break
            if coll_idx is not None and coll_idx > 0:
                side_a = chain[coll_idx - 1]
                side_b = chain[coll_idx]
                if side_a["setter"] not in txt:
                    bad.append(f"{sname} step {step['step']}: resolution "
                               f"missing collision side {side_a['setter']}")
                if side_b["setter"] not in txt:
                    bad.append(f"{sname} step {step['step']}: resolution "
                               f"missing collision side {side_b['setter']}")
                if str(side_a["value"]) not in txt:
                    bad.append(f"{sname} step {step['step']}: resolution "
                               f"missing value {side_a['value']}")
                if str(side_b["value"]) not in txt:
                    bad.append(f"{sname} step {step['step']}: resolution "
                               f"missing value {side_b['value']}")

        elif step["type"] == "self_revision" and i > 0:
            prev = chain[i - 1]
            if str(prev["value"]) not in txt:
                bad.append(f"{sname} step {step['step']}: self_revision "
                           f"missing prior value {prev['value']}")

check("I12 chain marker discipline", not bad, "; ".join(bad[:5]))

# ============================================================
# Ground truth consistency
# ============================================================

target_chain = scope_chains.get(target_scope, [])
if target_chain:
    last = target_chain[-1]
    if last["type"] == "collision":
        check("GT contested", gt.get("unresolved_conflict") is True)
        check("GT value", "contested" in str(gt.get("current_value", "")))
    else:
        check("GT value", str(gt.get("current_value")) == str(last["value"]),
              f"GT={gt.get('current_value')} vs chain={last['value']}")
        check("GT setter", gt.get("current_setter") == last["setter"],
              f"GT={gt.get('current_setter')} vs chain={last['setter']}")
    check("GT chain length", gt.get("chain_length") == len(target_chain),
          f"GT={gt.get('chain_length')} vs actual={len(target_chain)}")
    check("GT steps count", len(gt.get("steps", [])) == len(target_chain))

# ============================================================
# Summary
# ============================================================

print(f"\n{'ALL INVARIANTS PASS' if not fails else 'FAILURES: ' + ', '.join(fails)}"
      + (f" ({len(warns)} warnings)" if warns else ""))
sys.exit(1 if fails else 0)

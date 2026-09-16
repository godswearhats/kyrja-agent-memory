#!/usr/bin/env python3
"""MASQ generator v2 — multi-scope, multi-step chains.

v2 replaces v1's single-entity 2-step design with:
 - P scopes sharing the SAME entity name (namespace collision)
 - 3-5 step chains per scope with mixed transition types
 - K near-miss entities with confusably similar names
 - Scope-context atoms embedded in chain-write sessions

One family = one scenario = one corpus. No matched-family / cell matrix.
Confusability comes from multiple scopes, not from varying kernel cells.

Adversarial invariants:
 I1  value-collision: scope chain values also appear as sibling finals.
 I2  write-count cover: ≥25% of siblings have 2+ writes.
 I3  token recurrence: param name, chain values, chain writers recur in noise.
 I4  marker discipline: supersession names prior writer+value; collision is
     greenfield; resolution names both collision sides.
 I5  kernel isolation: no sibling/chatter mentions kernel entity + param/value.
 I8  off-kernel collisions: siblings with unreconciled collisions.
 I9  scope isolation: chain sessions for scope X don't mention other scopes.
 I10 scope coverage: each scope's chain fully represented in sessions.
 I11 near-miss isolation: near-miss names don't appear in scope-context atoms.
 I12 chain marker discipline: per-step within chains.
"""
import argparse, json, os, random, re

from domains import DOMAINS, PEOPLE, A1, A2, GENERIC_CHATTER, PREAMBLE

SESSION_SHAPES = ["standup note", "incident comment", "change-record entry",
                  "channel message", "handoff note", "retro fragment"]
LENGTH_MIX = [("1 short paragraph", 40), ("2 paragraphs", 35),
              ("3-4 paragraphs", 25)]

CHAIN_PATTERNS = {
    "P1": ["initial", "supersession", "supersession"],
    "P2": ["initial", "collision", "resolution"],
    "P3": ["initial", "collision", "resolution", "supersession"],
    "P4": ["initial", "supersession", "collision"],
    "P5": ["initial", "supersession", "collision", "resolution"],
    "P6": ["initial", "collision", "resolution", "collision"],
    "P7": ["initial", "supersession", "collision", "resolution", "supersession"],
    "P8": ["initial", "self_revision", "supersession"],
}

NM_PATTERNS = [
    ["initial", "supersession"],
    ["initial", "self_revision", "supersession"],
    ["initial", "supersession", "supersession"],
]

WRITERS = PEOPLE + [A1, A2]


def pick(rng, dom, kind, **kw):
    return rng.choice(dom["banks"][kind]).format(
        param=dom["param"], unit=dom.get("unit", ""), **kw)


def fmt(dom, t, **kw):
    return t.format(param=dom["param"], unit=dom.get("unit", ""), **kw)


def pick_resolution(rng, dom, **kw):
    return rng.choice(dom["banks"]["resolution"]).format(
        param=dom["param"], unit=dom.get("unit", ""), **kw)


# ---------------------------------------------------------------------------
# Chain generation
# ---------------------------------------------------------------------------

def generate_chain(dom, pattern_key, scope_name, entity, rng, days):
    """Generate one scope's chain according to a pattern.

    Returns (chain_steps, sessions) where chain_steps is the ground-truth
    sequence and sessions are the corpus entries (one per step).
    """
    pattern = CHAIN_PATTERNS[pattern_key]
    n_steps = len(pattern)
    value_pool = dom["values"]

    step_days = sorted(rng.sample(range(1, max(days, n_steps) + 1), n_steps))

    values = []
    for i in range(n_steps):
        exclude = {values[-1]} if values else set()
        values.append(rng.choice([v for v in value_pool if v not in exclude]))

    prev_writer = None
    collision_state = None
    chain_steps, sessions = [], []

    for i, (ttype, day, value) in enumerate(zip(pattern, step_days, values)):
        if ttype == "initial":
            writer = rng.choice(WRITERS)
            text = pick(rng, dom, "initial", fact=entity, v=value,
                        reason=rng.choice(dom["reasons_initial"]))

        elif ttype == "self_revision":
            writer = prev_writer
            text = pick(rng, dom, "self_revision", fact=entity, v=value,
                        pv=values[i - 1],
                        reason=rng.choice(dom["reasons_self"]))

        elif ttype == "supersession":
            writer = rng.choice([w for w in WRITERS if w != prev_writer])
            text = pick(rng, dom, "marked_supersession", fact=entity, v=value,
                        pv=values[i - 1], prev=prev_writer,
                        reason=rng.choice(dom["reasons_cross"]))

        elif ttype == "collision":
            writer = rng.choice([w for w in WRITERS if w != prev_writer])
            text = pick(rng, dom, "marked_collision", fact=entity, v=value,
                        reason=rng.choice(dom["reasons_initial"]))
            collision_state = (prev_writer, values[i - 1], writer, value)

        elif ttype == "resolution":
            wa, va, wb, vb = collision_state
            candidates = [w for w in WRITERS if w != wa and w != wb]
            writer = rng.choice(candidates) if candidates else rng.choice(WRITERS)
            text = pick_resolution(rng, dom, fact=entity, v=value,
                                   pv1=va, pv2=vb, prev1=wa, prev2=wb,
                                   reason=rng.choice(dom["reasons_resolution"]))
            collision_state = None
        else:
            raise ValueError(f"unknown transition type: {ttype}")

        prev_writer = writer
        chain_steps.append(dict(step=i + 1, value=value, setter=writer,
                                type=ttype, day=day))
        sessions.append(dict(day=day, writer=writer, kind=f"chain_{ttype}",
                             fact=entity, scope=scope_name, text=text,
                             sort=(day, rng.random())))

    return chain_steps, sessions


def generate_near_miss_chain(dom, nm_entity, rng, days):
    """Short chain (2-3 steps) for a near-miss entity.  No scope tag."""
    pattern = rng.choice(NM_PATTERNS)
    value_pool = dom["values"]
    n_steps = len(pattern)
    step_days = sorted(rng.sample(range(1, max(days, n_steps) + 1), n_steps))

    values = []
    for i in range(n_steps):
        exclude = {values[-1]} if values else set()
        values.append(rng.choice([v for v in value_pool if v not in exclude]))

    prev_writer = None
    chain_steps, sessions = [], []

    for i, (ttype, day, value) in enumerate(zip(pattern, step_days, values)):
        if ttype == "initial":
            writer = rng.choice(WRITERS)
            text = pick(rng, dom, "initial", fact=nm_entity, v=value,
                        reason=rng.choice(dom["reasons_initial"]))
        elif ttype == "self_revision":
            writer = prev_writer
            text = pick(rng, dom, "self_revision", fact=nm_entity, v=value,
                        pv=values[i - 1],
                        reason=rng.choice(dom["reasons_self"]))
        elif ttype == "supersession":
            writer = rng.choice([w for w in WRITERS if w != prev_writer])
            text = pick(rng, dom, "marked_supersession", fact=nm_entity, v=value,
                        pv=values[i - 1], prev=prev_writer,
                        reason=rng.choice(dom["reasons_cross"]))
        else:
            raise ValueError(f"unsupported nm transition: {ttype}")

        prev_writer = writer
        chain_steps.append(dict(step=i + 1, value=value, setter=writer,
                                type=ttype, day=day))
        sessions.append(dict(day=day, writer=writer, kind=f"nm_{ttype}",
                             fact=nm_entity, text=text,
                             sort=(day, rng.random())))

    return chain_steps, sessions


# ---------------------------------------------------------------------------
# Siblings + chatter (noise)
# ---------------------------------------------------------------------------

def build_noise(dom, n_siblings, n_chatter, days, n_collisions, rng,
                exclude_entities, cover_values, scope_names):
    """Generate sibling facts + chatter for v2.  Kernel entity excluded."""
    value_pool = dom["values"]
    available = [e for e in dom["entities"] if e not in exclude_entities]
    assert len(available) >= n_siblings, \
        f"need {n_siblings} siblings but only {len(available)} entities available"
    siblings = rng.sample(available, n_siblings)
    coll_facts = siblings[-n_collisions:] if n_collisions else []
    normal = [f for f in siblings if f not in coll_facts]

    sessions, sib_meta = [], []

    # I1: cover_values appear as non-collided sibling finals
    cover = list(cover_values)
    finals = cover[:len(normal)]
    while len(finals) < len(normal):
        finals.append(rng.choice(value_pool))
    rng.shuffle(finals)

    for fact, final in zip(normal, finals):
        n_writes = rng.choices([1, 2, 3], weights=[55, 35, 10])[0]
        w_days = sorted(rng.sample(range(1, days + 1),
                                   min(n_writes, days)))
        vals = []
        for _ in range(n_writes - 1):
            prevv = vals[-1] if vals else None
            vals.append(rng.choice([v for v in value_pool
                                    if v != final and v != prevv]))
        vals.append(final)
        timeline, w_prev = [], None
        for i, (d, v) in enumerate(zip(w_days, vals)):
            if i == 0:
                w = rng.choice(WRITERS)
                text = pick(rng, dom, "initial", fact=fact, v=v,
                            reason=rng.choice(dom["reasons_initial"]))
                kind = "initial"
            elif rng.random() < 0.5:
                w = w_prev
                text = pick(rng, dom, "self_revision", fact=fact, v=v,
                            pv=vals[i - 1],
                            reason=rng.choice(dom["reasons_self"]))
                kind = "self_revision"
            else:
                w = rng.choice([x for x in WRITERS if x != w_prev])
                text = pick(rng, dom, "marked_supersession", fact=fact, v=v,
                            pv=vals[i - 1], prev=w_prev,
                            reason=rng.choice(dom["reasons_cross"]))
                kind = "marked_supersession"
            timeline.append(dict(day=d, writer=w, value=v, kind=kind))
            sessions.append(dict(day=d, writer=w, kind=kind, fact=fact,
                                 text=text))
            w_prev = w
        sib_meta.append(dict(fact=fact, final=final, collided=False,
                             timeline=timeline))

    # I8 — off-kernel collisions
    for fact in coll_facts:
        d = rng.randint(1, days)
        w1, w2 = rng.sample(WRITERS, 2)
        va = rng.choice(value_pool)
        vb = rng.choice([v for v in value_pool if v != va])
        t1 = pick(rng, dom, "initial", fact=fact, v=va,
                  reason=rng.choice(dom["reasons_initial"]))
        t2 = pick(rng, dom, "marked_collision", fact=fact, v=vb,
                  reason=rng.choice(dom["reasons_initial"]))
        sessions.append(dict(day=d, writer=w1, kind="initial", fact=fact,
                             text=t1))
        sessions.append(dict(day=d, writer=w2, kind="marked_collision",
                             fact=fact, text=t2))
        sib_meta.append(dict(fact=fact, final=None, collided=True,
                             timeline=[dict(day=d, writer=w1, value=va,
                                            kind="initial"),
                                       dict(day=d, writer=w2, value=vb,
                                            kind="marked_collision")]))

    # Chatter: value mentions for non-collided siblings + generic + cover
    normal_meta = [s for s in sib_meta if not s["collided"]]
    n_scope_chatter = max(2, n_chatter // 8)
    n_cover = max(2, n_chatter // 20)
    n_regular = n_chatter - n_scope_chatter - n_cover

    for _ in range(n_regular):
        d = rng.randint(1, days)
        w = rng.choice(WRITERS)
        r = rng.random()
        fact = None
        if r < 0.5 and normal_meta:
            s = rng.choice(normal_meta)
            cur = None
            for t in s["timeline"]:
                if t["day"] <= d:
                    cur = t["value"]
            if cur is None:
                text = rng.choice(GENERIC_CHATTER)
                kind = "chatter_generic"
            else:
                text = fmt(dom, rng.choice(dom["value_chatter"]),
                           fact=s["fact"], value=cur)
                kind = "chatter_value"
                fact = s["fact"]
        else:
            text = rng.choice(GENERIC_CHATTER)
            kind = "chatter_generic"
        sessions.append(dict(day=d, writer=w, kind=kind, fact=fact, text=text))

    # Cover chatter: product-area mentions of kernel entity, no config values
    for _ in range(n_cover):
        d = rng.randint(1, days)
        w = rng.choice(WRITERS)
        text = rng.choice(dom["cover_chatter"])
        sessions.append(dict(day=d, writer=w, kind="chatter_cover",
                             fact=None, text=text))

    # Scope-mentioning chatter: noise that names scopes without config writes
    for _ in range(n_scope_chatter):
        d = rng.randint(1, days)
        w = rng.choice(WRITERS)
        sname = rng.choice(scope_names)
        scope_data = next((s for s in dom["scopes"] if s["name"] == sname), None)
        if scope_data:
            text = rng.choice(scope_data["context_atoms"])
        else:
            text = rng.choice(GENERIC_CHATTER)
        sessions.append(dict(day=d, writer=w, kind="chatter_scope",
                             fact=None, text=text))

    for s in sessions:
        if "sort" not in s:
            s["sort"] = (s["day"], rng.random())
    sessions.sort(key=lambda s: s["sort"])

    return sib_meta, sessions


# ---------------------------------------------------------------------------
# Ground truth + queries
# ---------------------------------------------------------------------------

def compute_ground_truth(chain_steps, dom):
    """Compute ground truth from the target scope's chain."""
    last = chain_steps[-1]
    if last["type"] == "collision":
        prev = chain_steps[-2]
        current_value = "contested"
        current_setter = f"contested:{{{prev['setter']},{last['setter']}}}"
        unresolved = True
        if dom["numeric"]:
            action = "any_recorded"
        else:
            action = "any_recorded"
        conflict_flag = True
    else:
        current_value = last["value"]
        current_setter = last["setter"]
        unresolved = False
        action = f"set_{current_value}"
        conflict_flag = False

    steps = [dict(value=s["value"], setter=s["setter"], type=s["type"])
             for s in chain_steps]
    return dict(
        current_value=current_value,
        current_setter=current_setter,
        chain_length=len(chain_steps),
        steps=steps,
        unresolved_conflict=unresolved,
        action=action,
        conflict_flag=conflict_flag,
    )


def build_action_menu(scope_chains, dom):
    """Action menu from all scopes' terminal values — confusable."""
    values = set()
    for chain in scope_chains.values():
        for step in chain:
            values.add(step["value"])
    actions = sorted(f"set_{v}" for v in values)
    actions.extend(["set_other", "none"])
    return "{" + ", ".join(actions) + "}"


def build_queries(dom, entity, target_scope, action_menu):
    """Build A-query and B-query for the target scope."""
    a_query = (
        f"In the context of {target_scope}: As of now, what is the "
        f"{entity} {dom['param']}? Reconstruct the full change history "
        f"for this specific context. For each change, state the value, "
        f"who set it, and whether it was an initial setting, a "
        f"self-revision, a supersession (the writer acknowledged the "
        f"prior value/setter), a collision (the writer was unaware of "
        f"the prior setting), or a resolution (the writer acknowledged "
        f"a prior conflict between two parties and resolved it)."
    )
    b_query = (
        f"In the context of {target_scope}: "
        + PREAMBLE + " "
        + fmt(dom, dom["b_task"], fact=entity)
        + f" Reply with exactly one action from {action_menu}, "
        f"plus conflict_flag: true|false, and one sentence of rationale."
    )
    return a_query, b_query


# ---------------------------------------------------------------------------
# Family builder
# ---------------------------------------------------------------------------

def build_family_v2(dom, n_siblings, n_chatter, days, n_collisions,
                    n_scopes, n_near_misses, seed):
    """Produce a complete v2 family with multi-scope chains."""
    rng = random.Random(seed)
    entity = dom["kernel_fact"]

    # Pick scopes and assign patterns
    scopes = rng.sample(dom["scopes"], n_scopes)
    target_scope = rng.choice(scopes)
    patterns = list(CHAIN_PATTERNS.keys())
    for scope in scopes:
        scope["assigned_pattern"] = rng.choice(patterns)

    # Generate scope chains
    scope_chains = {}
    chain_sessions = []
    for scope in scopes:
        chain, sessions = generate_chain(
            dom, scope["assigned_pattern"], scope["name"],
            entity, rng, days)
        scope_chains[scope["name"]] = chain
        chain_sessions.extend(sessions)

    # Near-miss chains
    nm_pool = dom.get("near_miss_entities", [])
    nm_count = min(n_near_misses, len(nm_pool))
    nm_entities = rng.sample(nm_pool, nm_count) if nm_count else []
    nm_chains = {}
    nm_sessions = []
    for nm in nm_entities:
        chain, sessions = generate_near_miss_chain(dom, nm, rng, days)
        nm_chains[nm] = chain
        nm_sessions.extend(sessions)

    # Collect values from all scope chains for I1 coverage
    chain_values = sorted({step["value"]
                           for chain in scope_chains.values()
                           for step in chain})

    # Exclude kernel entity + near-miss entities from sibling pool
    exclude = {entity} | set(nm_entities)
    scope_names = [s["name"] for s in scopes]

    sib_meta, noise_sessions = build_noise(
        dom, n_siblings, n_chatter, days, n_collisions, rng,
        exclude_entities=exclude,
        cover_values=chain_values,
        scope_names=scope_names)

    # Merge all sessions
    all_sessions = noise_sessions + chain_sessions + nm_sessions
    for s in all_sessions:
        if "sort" not in s:
            s["sort"] = (s["day"], rng.random())
    all_sessions.sort(key=lambda s: s["sort"])

    # Assign stable IDs
    for i, s in enumerate(all_sessions):
        s["id"] = f"s{i + 1:04d}"

    # Ground truth for target scope
    target_chain = scope_chains[target_scope["name"]]
    gt = compute_ground_truth(target_chain, dom)

    # Action menu + queries
    action_menu = build_action_menu(scope_chains, dom)
    a_query, b_query = build_queries(
        dom, entity, target_scope["name"], action_menu)

    family = dict(
        meta=dict(
            seed=seed, domain=dom["id"], param=dom["param"],
            unit=dom.get("unit", ""),
            kernel_entity=entity,
            scopes=[dict(name=s["name"], pattern=s["assigned_pattern"],
                         context_atoms=s["context_atoms"])
                    for s in scopes],
            target_scope=target_scope["name"],
            near_miss_entities=nm_entities,
            n_siblings=n_siblings, n_chatter=n_chatter,
            n_collisions=n_collisions, days=days,
            n_scopes=n_scopes, n_near_misses=nm_count,
        ),
        scope_chains={name: steps for name, steps in scope_chains.items()},
        near_misses=nm_chains,
        siblings=sib_meta,
        ground_truth=gt,
        a_query=a_query,
        b_query=b_query,
        action_menu=action_menu,
        world_sessions=all_sessions,
    )
    return family


# ---------------------------------------------------------------------------
# Render
# ---------------------------------------------------------------------------

def render_md(dom, sessions, tag):
    """Render all sessions to markdown corpus."""
    lines = [f"[Session log — storefront platform / {dom['channel']} ({tag})]",
             ""]
    for s in sessions:
        lines.append(f"— {s['writer']}, day {s['day']}")
        lines.append(f"  {s.get('prose', s['text'])}")
        lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="MASQ v2 generator")
    ap.add_argument("--domain", default="rate-limit", choices=sorted(DOMAINS))
    ap.add_argument("--n-siblings", type=int, default=8)
    ap.add_argument("--n-chatter", type=int, default=40)
    ap.add_argument("--days", type=int, default=28)
    ap.add_argument("--n-collisions", type=int, default=2)
    ap.add_argument("--n-scopes", type=int, default=3)
    ap.add_argument("--n-near-misses", type=int, default=2)
    ap.add_argument("--seed", type=int, default=109)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    dom = DOMAINS[a.domain]
    out_name = a.out or ("demo-v2" if a.domain == "rate-limit"
                         else f"demo-v2-{a.domain}")
    fam = build_family_v2(dom, a.n_siblings, a.n_chatter, a.days,
                          a.n_collisions, a.n_scopes, a.n_near_misses,
                          a.seed)

    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, out_name)
    os.makedirs(out, exist_ok=True)

    fam_path = os.path.join(out, f"family-{dom['id']}.json")
    with open(fam_path, "w") as f:
        json.dump(fam, f, indent=2, default=str)

    m = fam["meta"]
    tag = (f"seed={m['seed']} scopes={m['n_scopes']} "
           f"sib={m['n_siblings']} chat={m['n_chatter']}")
    md = render_md(dom, fam["world_sessions"], tag)
    corpus_path = os.path.join(out, "corpus.md")
    with open(corpus_path, "w") as f:
        f.write(md)

    words = len(md.split())
    n_chain = sum(1 for s in fam["world_sessions"]
                  if s["kind"].startswith("chain_"))
    n_nm = sum(1 for s in fam["world_sessions"]
               if s["kind"].startswith("nm_"))
    n_sib = len(fam["siblings"])
    n2 = sum(1 for s in fam["siblings"] if len(s["timeline"]) >= 2)
    nc = sum(1 for s in fam["siblings"] if s["collided"])
    print(f"[{dom['id']}] v2 family: {m['n_scopes']} scopes "
          f"(target={m['target_scope']}, "
          f"patterns={[s['pattern'] for s in m['scopes']]})")
    print(f"  chain sessions: {n_chain}, near-miss sessions: {n_nm}")
    print(f"  siblings: {n_sib} ({n2} with 2+ writes, {nc} collided)")
    print(f"  corpus: ≈{words} words (≈{int(words * 1.33)} tokens)")
    print(f"  ground truth: value={fam['ground_truth']['current_value']}, "
          f"setter={fam['ground_truth']['current_setter']}, "
          f"conflict={fam['ground_truth']['unresolved_conflict']}, "
          f"chain_length={fam['ground_truth']['chain_length']}")
    print(f"wrote {fam_path}")
    print(f"wrote {corpus_path}")


if __name__ == "__main__":
    main()

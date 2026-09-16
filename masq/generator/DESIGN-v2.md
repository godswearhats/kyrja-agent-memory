# MASQ Generator v2 — Multi-Scope, Multi-Step Chains

**Status:** IMPLEMENTED 2026-06-12. All files updated, 12/12 sweep scenarios pass verify.
**Supersedes:** v1 generator design (single-entity, 2-step chains).
**Motivation:** v1 sweep pilot (2026-06-10/11) showed paste-everything at
100% B-pass through 60k and 90% at 400k. Root cause: entity names are
unique strings; the model string-matches the kernel entity and ignores
everything else. Confusability requires structural overlap, not volume.

## 1. Core design

Three confusability layers, each targeting a different failure mode:

| Layer | Mechanism | What it breaks |
|-------|-----------|----------------|
| **Scope collision** | P scopes share the **same entity name** (e.g., 4 services all have `/checkout`) | String-matching on entity name — finds P×L hits, must pick the right L |
| **Near-miss entities** | K entities with similar names (`/checkout-v2`, `/checkout-legacy`) | Prefix-matching — finds K×L_nm additional plausible hits |
| **Multi-step chains** | Each scope has L steps (3–5) with mixed transition types | Pattern-matching on transition markers — must trace the full chain and classify each step |

These compound multiplicatively. A correct answer requires succeeding at
ALL of: entity retrieval, scope disambiguation, chain reconstruction,
transition classification, and terminal state determination.

## 2. Terminology

- **Scope**: a service / business unit / team that has its own instance of
  the kernel entity. Domain-specific: rate-limit → services, ownership →
  business units, merge-policy → teams. Parameterized, 2–5 per scenario.
- **Chain**: the sequence of writes to one scope's instance of the kernel
  entity. Each step has a value, a setter (writer), and a transition type.
- **Transition types**: `initial`, `self_revision`, `supersession`,
  `collision`. Same semantics as v1, applied per-step.
- **Near-miss entity**: an entity whose name is confusably similar to the
  kernel entity (e.g., `/checkout-v2` vs `/checkout`). Has its own chain
  but no scope association.
- **Sibling**: a distinct entity (different name, same attribute type).
  Volume noise, carried forward from v1.

## 3. Family structure v2

```
family = {
  meta: {
    seed, domain, param, unit,
    kernel_entity,                  # e.g., "/checkout"
    scopes: [                       # 2–5 scopes
      {name: "checkout-web",  chain_pattern: "P3", ...},
      {name: "checkout-mobile", chain_pattern: "P1", ...},
      ...
    ],
    target_scope: "checkout-web",   # which scope the query asks about
  },
  scope_chains: {
    "checkout-web": [
      {step: 1, value: 100, setter: "Alice", type: "initial", day: 5},
      {step: 2, value: 300, setter: "Bob",   type: "collision", day: 18},
      {step: 3, value: 200, setter: "Carol", type: "supersession", day: 30},
      {step: 4, value: 150, setter: "Alice", type: "supersession", day: 45},
    ],
    "checkout-mobile": [...],
    ...
  },
  near_misses: [...],              # K entities with chains
  siblings: [...],                  # N entities (v1-style, volume noise)
  world_sessions: [...],           # all sessions, merged and day-sorted
  ground_truth: {                   # for the target scope
    current_value, current_setter, chain_length,
    steps: [{value, setter, type}, ...],
    unresolved_conflict: true|false,
    action, conflict_flag,
  },
}
```

The corpus is rendered from `world_sessions` (all scopes' chain writes +
near-miss writes + sibling writes + chatter), exactly as v1 but with
scope context embedded in the prose around each chain write.

## 4. Chain patterns (cell catalog)

Each scope is assigned one chain pattern. The target scope's pattern
determines the ground truth. Variable chain lengths (3–5 steps) and
variable pattern assignment across scopes make regularity unexploitable.

| Pattern | Steps | Description | Terminal | Conflict? |
|---------|-------|-------------|----------|-----------|
| **P1** | 3 | initial → supersession → supersession | clear (step 3 value) | false |
| **P2** | 3 | initial → collision → resolution | clear (step 3 value) | false (resolved) |
| **P3** | 4 | initial → collision → resolution → supersession | clear (step 4 value) | false |
| **P4** | 3 | initial → supersession → collision | contested | true (unresolved) |
| **P5** | 4 | initial → supersession → collision → resolution | clear (step 4 value) | false |
| **P6** | 4 | initial → collision → resolution → collision | contested | true |
| **P7** | 5 | initial → supersession → collision → resolution → supersession | clear (step 5 value) | false |
| **P8** | 3 | initial → self_revision → supersession | clear (step 3 value) | false |

**Key property:** P2, P3, P5, P7 all contain a collision that is later
resolved. The model must trace through the chain to see that the
collision is no longer live — it cannot just detect "collision happened"
and report CONFLICT: true. This is AJ's "a supersession at step 3 or 4
might understand there was a collision in steps 1 and 2."

**Collision → resolution semantics:** A resolution is a supersession that
explicitly references BOTH sides of the prior collision. Its prose names
both colliding writers and both values, then states its own value as the
resolved outcome. This is deterministically verifiable from the locked
sentence.

## 5. Scope context in the corpus

Each chain-write session embeds scope context in its prose:

```
— Alice, day 12
  Wrapping up the checkout-web capacity review. Tightened /checkout
  after the soak test: setting the /checkout rate limit to 100 req/s —
  that's where p99 stays flat.
```

The scope name ("checkout-web") appears in the same session as the
config write, within the composed prose (not as a structured tag). The
locked sentence (the config write) is unchanged; the scope context is
part of the wrapping atoms/compounds.

**Scope-context atoms** (new atom category per scope):
```
"Wrapping up the checkout-web capacity review."
"The checkout-web team had a productive sprint."
"Following up on the checkout-web deployment."
```

These are scope-specific but fact-agnostic — they name the scope but
carry no config values. The generator ensures each chain-write session
includes ≥1 scope-context atom from the matching scope.

**Cross-scope chatter**: some generic chatter sessions also mention scope
names without config changes, creating noise that the model must
distinguish from config writes.

## 6. Permutation analysis

### 6.1 Signal writes in the corpus

| Source | Count | Matches "/checkout"? |
|--------|-------|----------------------|
| Target scope chain | L (3–5) | exact |
| Other scopes' chains | (P-1) × L_avg | exact, **same string** |
| Near-miss entity chains | K × L_nm | partial (prefix match) |
| Distinct siblings | N × L_sib | no |

**Defaults:** P=4, L_avg=4, K=3, L_nm=3, N=50, L_sib=1.5

| | Count |
|-|-------|
| Kernel entity across scopes | 4 × 4 = **16** exact-match writes |
| Near-miss entities | 3 × 3 = **9** prefix-match writes |
| Siblings | 50 × 1.5 = **75** distinct writes |
| **Total config writes** | **~100** |

The model must correctly identify **4 out of 16** same-string writes.

### 6.2 Random-baseline disambiguation

If the model finds all 16 exact-match "/checkout rate limit" writes and
picks 4 at random: C(4,4)/C(16,4) = 1/1820 ≈ 0.05%.

With per-write scope accuracy p, P(all L writes correctly scoped):

| p (per-write) | P(all 4 correct) |
|---------------|------------------|
| 0.95 | 0.81 |
| 0.90 | 0.66 |
| 0.85 | 0.52 |
| 0.80 | 0.41 |
| 0.70 | 0.24 |

### 6.3 Compound error rate

P(correct) = P(entity) × P(scope)^L × P(order) × P(type)^(L-1) × P(terminal)

Estimated per-gate accuracy by corpus size (paste-everything arm):

| Gate | 6k | 25k | 60k | 150k | 400k |
|------|------|------|------|-------|-------|
| Entity retrieval | 0.99 | 0.98 | 0.97 | 0.95 | 0.92 |
| Scope disambig (per write) | 0.95 | 0.90 | 0.85 | 0.75 | 0.60 |
| → all 4 writes | 0.81 | 0.66 | 0.52 | 0.32 | 0.13 |
| Chain ordering | 0.99 | 0.99 | 0.98 | 0.97 | 0.95 |
| Transition type (per step) | 0.95 | 0.92 | 0.88 | 0.82 | 0.75 |
| → all 3 transitions | 0.86 | 0.78 | 0.68 | 0.55 | 0.42 |
| Terminal state | 0.98 | 0.97 | 0.95 | 0.92 | 0.88 |
| **Compound** | **~68%** | **~48%** | **~32%** | **~15%** | **~4%** |

vs v1 actual: 100% → 100% → 100% → 98% → 90%.

**This is a real curve.** The crossover starts at 25k, not 400k. By 60k
the benchmark meaningfully differentiates. By 150k paste-everything is
seriously degraded — which is exactly where a smart memory system should
start winning.

### 6.4 Value confusion

Values are drawn from the same pool across scopes. If scope A's /checkout
goes 100→300→200→150 and scope B's goes 300→500→200:

- Values 200 and 300 appear in BOTH chains
- A model that picks the wrong scope gets plausible-looking but wrong values
- Even partial credit (some fields correct) is suppressed by value collision

Writer overlap amplifies this: Alice writes in 2 different scopes.

### 6.5 How variability helps

Variable parameters prevent structural regularity from being a cue:

| Parameter | Range | Effect |
|-----------|-------|--------|
| P (scopes) | 2–5 | can't assume "always 4 scopes" |
| L (chain length) | 3–5, variable per scope | can't count writes and divide by P |
| K (near-misses) | 0–4 | can't assume fixed near-miss count |
| Chain pattern | P1–P8, variable per scope | can't assume all scopes have same pattern |

## 7. Answer format and grading (deterministic)

### 7.1 A-query (chain reconstruction)

Prompt: "In the context of the {scope_name} service: As of now, what is
the {entity} {param}? Reconstruct the full change history. For each
change, state the value, who set it, and whether it was an initial
setting, a self-revision, a supersession (the writer acknowledged the
prior value/setter), or a collision (the writer was unaware of the prior
setting)."

Answer format (one line per field):
```
CURRENT_VALUE: <value or contested>
CURRENT_SETTER: <name or contested:{name1,name2}>
CHAIN_LENGTH: <N>
STEP_1_VALUE: <value>
STEP_1_SETTER: <name>
STEP_1_TYPE: <initial|self_revision|supersession|collision>
STEP_2_VALUE: <value>
STEP_2_SETTER: <name>
STEP_2_TYPE: <initial|self_revision|supersession|collision>
[... up to STEP_N ...]
UNRESOLVED_CONFLICT: <true|false>
```

A-score = fraction of fields correct (exact match, normalized).

Grading breakdown:
- Terminal fields (3): CURRENT_VALUE, CURRENT_SETTER, UNRESOLVED_CONFLICT
- Chain fields (3 per step): STEP_i_VALUE, STEP_i_SETTER, STEP_i_TYPE
- CHAIN_LENGTH: graded separately (enables partial credit for wrong-length chains)

If CHAIN_LENGTH is wrong, step fields are aligned best-effort (LCS on
value+setter pairs, unmatched steps score 0). This prevents a single
missed or extra step from zeroing the entire chain score.

### 7.2 B-query (decision)

Same structure as v1 but scoped:

Prompt: "In the context of the {scope_name} service: {preamble}
{b_task} Reply with exactly one action from {action_menu}, plus
conflict_flag: true|false, and one sentence of rationale."

```
ACTION: <menu item>
CONFLICT: <true|false>
```

Action menu includes values from ALL scopes' chains (confusable).
B-pass = correct action ∧ correct conflict flag.

## 8. Generator changes

### 8.1 `domains.py`

Add per-domain scope definitions:

```python
RATE_LIMIT["scopes"] = [
    dict(name="checkout-web",
         context_atoms=[
             "Wrapping up the checkout-web capacity review.",
             "The checkout-web deployment went out clean.",
             "Following up on the checkout-web load test.",
             ...  # 8-10 per scope
         ]),
    dict(name="checkout-mobile", ...),
    dict(name="checkout-api", ...),
    dict(name="checkout-internal", ...),
    dict(name="checkout-sandbox", ...),   # 5 scopes available, 2-5 drawn per scenario
]

RATE_LIMIT["near_miss_entities"] = [
    "/checkout-v2", "/checkout-legacy", "/checkout-canary",
    "/checkout-admin",
]
```

Similar for OWNERSHIP and MERGE_POLICY, with domain-appropriate
scope names and near-miss entities.

### 8.2 `embedding.py`

`build_world()` changes:
- Accept `n_scopes` (2–5), `n_near_misses` (0–4), `chain_patterns` (list)
- For each scope: generate an L-step chain using the assigned pattern
- Each chain-write session's text includes scope context (drawn from
  scope-specific atoms) + locked config-write sentence
- Near-miss entities get their own chains (2–3 steps, random patterns)
- Siblings and chatter remain as v1

`kernel_cells()` is replaced by `kernel_chains()` — generates ground
truth per scope, identifies the target scope.

New: scope-context chatter — generic sessions that mention scope names
without config changes (noise for disambiguation).

### 8.3 `compose.py`

Minimal change: scope-context atoms are treated like regular atoms (they
go into L0). The compose engine already handles locked sentences; scope
context is additional wrapping prose, not locked.

New atom category in the atom bank: scope-context atoms (per scope per
domain). These are authored once and reused across all scenarios.

### 8.4 `verify.py`

New invariants:

- **I9 scope isolation**: no chain-write session for scope X mentions a
  different scope's name. Scope context is clean per-session.
- **I10 scope coverage**: each scope's chain is fully represented in
  world_sessions. No missing steps.
- **I11 near-miss isolation**: near-miss entity names never appear in the
  same session as a scope context atom. Near-misses are scope-free.
- **I12 chain marker discipline**: same as I4 but per-step within chains.
  Supersession steps name the prior writer + prior value. Collision steps
  carry greenfield markers. Resolution steps name BOTH colliding
  writers + values.

Existing invariants I1–I8 adapt: I1 (value collision) extends to
per-scope value coverage; I5 (kernel isolation) extends to all scopes.

### 8.5 `sweep.py`

Existing SIZES dict gains `n_scopes` and `n_near_misses` columns:

```python
SIZES = {
    "6k":   dict(n_siblings=8,   n_chatter=40,   n_collisions=2,
                 n_scopes=2, n_near_misses=1, days=28),
    "25k":  dict(n_siblings=20,  n_chatter=180,  n_collisions=3,
                 n_scopes=3, n_near_misses=2, days=90),
    "60k":  dict(n_siblings=40,  n_chatter=440,  n_collisions=4,
                 n_scopes=4, n_near_misses=3, days=180),
    "150k": dict(n_siblings=70,  n_chatter=1200, n_collisions=8,
                 n_scopes=4, n_near_misses=3, days=365),
    "400k": dict(n_siblings=100, n_chatter=3200, n_collisions=12,
                 n_scopes=5, n_near_misses=4, days=730),
}
```

Scope and near-miss counts scale with corpus size — smaller corpora have
fewer scopes (less room for confusion), larger corpora have more (the
disambiguation task scales with the noise).

### 8.6 `run.py` (harness)

- Parse expanded A-format (variable number of steps)
- Grade chain steps with LCS alignment for wrong-length chains
- B-grade unchanged in structure (action + conflict flag)
- Scope name passed to the query template
- Action menu built from all scopes' values (not just target scope)

## 9. What v1 data tells us

The v1 sweep results are not wasted. They establish:

1. **Paste-everything is a strong baseline at v1 difficulty** — 100% through
   60k. This is the "easy mode" reference: with unique entity names and
   2-step chains, frontier models ace the task. Any benchmark that doesn't
   beat this is measuring retrieval, not memory.

2. **The ceiling arm validates construction** — 100% across all sizes
   confirms the queries and grading are sound. The ceiling arm is
   size-invariant by design; if it held in v1, it should hold in v2
   (same grading logic, just more fields).

3. **The 400k degradation is real but insufficient** — 90% at 400k shows
   the beginning of a curve. V2 should shift that curve leftward by
   2–3 size tiers.

## 10. Build order

1. **Scope-context atoms**: 8–10 per scope per domain. Can be authored
   by Maren or generated from templates. Small task, ~100 atoms total.
2. **`domains.py` v2**: add scopes, near-miss entities, chain patterns.
3. **`embedding.py` v2**: multi-scope chain generation, near-miss chains,
   scope-context embedding.
4. **`verify.py` v2**: I9–I12, adapt I1–I8.
5. **`compose.py`**: scope-context atoms into L0.
6. **`run.py` v2**: expanded parsing and grading.
7. **Smoke test**: 1 scenario at 6k, verify invariants + grading.
8. **Calibration pilot**: 12 scenarios, 3 sizes (6k, 25k, 60k), check
   that paste-everything shows meaningful degradation.

If the calibration pilot still shows paste ≥85% at 60k, the parameters
are wrong, not the design — increase P or K or tighten scope-context
density. But the permutation math predicts ~32% at 60k, so this should
not fire.

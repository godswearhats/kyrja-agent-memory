# MASQ v2 — analysis pre-registration (LOCKED 2026-06-26)

**Status:** LOCKED before any headline numbers exist on the pinned-core worlds.
**Supersedes:** the party×time interaction analysis in `DESIGN.md` §5–§6 and in
the wiki decision `masq-ab-factorial-design.md` (both written for the v1 2×2
factorial, which v2 does not implement — see "Why this supersedes" below).

This file fixes the headline metric, the primary test, N, the reader, and the
size handling *before* the system-under-test arm runs, so nothing downstream can
be retrofit to the result.

---

## Why this supersedes the v1 factorial analysis

The wiki/`DESIGN.md` pre-registration named the **party×time interaction**
(a 2×2 of cells C1–C4, primary test = the ΔΔ permutation contrast
`(C4−C3)−(C2−C1)`, plus a GLMM `B ~ party*time`) as the headline. That design
was abandoned mid-flight: **it failed the too-easy gate** — paste-everything
scored 85%+ even at 400k, so the cells did not discriminate. v2 replaced the
2×2 structure with **multi-scope confusability chains** and a single decision
per scenario. There is no party×time factor and no C1–C4 cells in v2, so the
v1 primary analysis has nothing to run on. This is a documentation-to-reality
reconciliation, not a goalpost move: the change was forced by a pre-registered
gate firing, and is recorded as such.

## What the benchmark is (v2)

A scenario is one synthetic org corpus containing **5 confusable scopes**
(near-identical services), each carrying a multi-step decision chain
(initial / self-revision / supersession / collision, patterns P1–P8), plus
near-miss entities and a distractor bed. The agent is asked, for one **target
scope**, to (A) reconstruct the decision chain and (B) take the correct action
and flag whether an unresolved conflict exists. All grading is closed-form
exact-match; no LLM judge. The skill measured is **scope disambiguation under
confusability**, decoupled from raw context length by design.

## Pinned design (locked; calibration-backed 2026-06-26)

- **Fixed difficulty core (identical every scenario):** 5 scopes, 4 near-misses,
  20-sibling bed (`n_collisions=2`), ≈7k tokens.
  - The sibling-bed calibration (K ∈ {10,20,40,80,150}, all ~63k, n=6/cell)
    showed paste-B **flat at ~50% across the entire 15× bed range** (every CI
    = [19–81%], no trend) and paste-A flat — so bed size is **not** load-bearing
    for difficulty. We pin lean at K=20 (cheapest safe size: 2 collisions, a
    margin over the K=10 construction floor). Ceiling held 100% at every K.
  - **Construction floor:** the generator refuses K=0 and K=5 (invariants
    I2/I3/I8 require ≥1 collision and the param recurring in distractor noise),
    so a minimum confusability bed is enforced, not optional.
- **Size axis (vary chatter only):** 25k / 60k / 150k / 400k tokens. Same ~7k
  needle, progressively deeper haystack (≈72% → 98% haystack). 6k dropped —
  it cannot host 5 scopes + the enforced bed.
- **Coverage:** 3 domains (rate-limit, ownership, merge-policy) × 5 seeds = 15
  per size × 4 sizes = **60 scenarios**. Worlds at `generator/headline/`.

## Headline metric

Per-arm **B-pass rate** = fraction of scenarios where the action is correct AND
the conflict flag is correct. Reported **pooled across sizes+domains** with
**Wilson 95% CIs**. Ceiling is the normalizer (it is ~100%, so raw ≈ normalized).

**Secondary:** per-arm **A-score** (chain-reconstruction field accuracy, mean
fraction of fields correct) — continuous, lower-variance; this is what separates
last-write-wins from ceiling where B does not.

## Primary test

Arms run on the **same** scenarios, so per-scenario B outcomes are paired binary.
For each arm-vs-arm contrast: **McNemar exact test** (primary), paired permutation
(confirmatory). **α = .05, two-sided** — the benchmark question is "where does the
system land," not a directional bet.

## Size handling

Report B-pass **per size with CIs**, descriptively. **No predicted shape is
pre-registered** — we make no claim that the gap is flat, rising, or falling with
size. Whether pooling to N=60 is legitimate depends on the system arm behaving
consistently across sizes; if it does not, we report per-size (n=15/size) and
note the reduced resolution rather than pooling over a real size effect.

## N and expansion

Headline N = the **60 pinned-core scenarios**. **Pre-registered expansion rule:**
if the system-under-test arm's B-pass CI overlaps a neighbor arm's (paste or
ceiling) by more than ~1 CI width, add scenarios (incrementally — generate more
worlds, ingest only the new ones, pool) until the contrast resolves or n=150.
Stated now so expansion is a power top-up, not a goalpost move. Cheap sizes can
absorb added samples without the 400k ingest cost.

## Reader

Single fixed reader = `claude-opus-4-8`, temperature 0, every output cached.
Rationale (DESIGN.md §7.2): the reader is a **held-constant probe of what memory
delivered** — the unit of variation is the memory system, not the model. This is
the design honoring its own logic, not a budget cut. **Multi-model robustness
(≥1 non-Anthropic reader) is a stretch appendix**, not load-bearing.

**Variance check (slimmed):** paste + ceiling + system on a fixed 4-scenario
subset at 60k, ×5 repeats; report sd. Findings must hold every run. This earns
its keep now that model-averaging is gone.

## Arms

- `paste` — paste whole corpus verbatim. Lower reference (can't self-disambiguate).
- `lww` — last-write-wins, scope-blind. Naive baseline.
- `ceiling` — perfect-retrieval of the target-scope chain. Upper reference / sanity.
- **`memory-system-under-test`** — THE experiment (not yet built). Must land
  **strictly between** the paste floor and the ceiling to make this a *graded*
  benchmark. If it sits at the floor, the claim becomes "off-the-shelf memory
  systems perform at chance on scope-disambiguation" — bold but publishable.

## Pilot context (superseded as headline, retained as provenance)

The variable-scope sweep-v2 worlds (scopes scaling 2→5 with size) gave the
finding that got us here: ceiling 100% / paste 38% / lww 37%, **bimodal** on B.
Those worlds are built to the old design and are NOT the headline; the headline
re-establishes the paste/lww/ceiling baseline on the pinned-core worlds (the
calibration already indicates paste sits ~50% at a fixed 5 scopes, not 38%).

## What is locked (goalpost tells)

Changing any of these after seeing system numbers is a goalpost move and must be
called out: the headline metric (B-pass), the paired McNemar test, two-sidedness,
the single fixed reader, the 60-scenario floor + stated expansion trigger, and
"size reported with no predicted shape."

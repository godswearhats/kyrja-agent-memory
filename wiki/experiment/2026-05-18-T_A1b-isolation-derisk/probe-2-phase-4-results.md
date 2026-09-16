---
type: experiment
name: Probe 2 Phase 4 results — pair construction
status: PROPOSED
last_ingested: 2026-05-23
sources: []
epistemic_tags: [measured]
tags: [t_a1b, probe-2, phase-4, test-set, caddy]
---

Results from Phase 4 (pair construction) of the [Probe 2 test set pipeline](./probe-2-test-set-design.md). Phase 4 assembles the 536 admitted event-mode candidates from [Phase 3](./probe-2-phase-3-results.md) into 200 cross-domain retrieval problems, each with 4 distractor tiers.

## Method

### Positive pair construction

For each of the 5 patterns, 40 cross-domain positive pairs were sampled from C(4,2) = 6 domain combinations, allocated proportionally to cell sizes (product of the two cell counts). Each candidate may appear in at most 3 pairs to limit over-representation.

**Seed:** 20260523 (today's date). Fully reproducible.

### Distractor assignment

Each positive pair (query from D1, target from D2, pattern P) receives 4 distractors per the pre-registered spec:

| Tier | Construction | What it tests |
|---|---|---|
| Easy | Random admitted event from D2, pattern ≠ P | Encoder beats random |
| Medium | Random admitted event from D2, pattern = P | Encoder uses structure not domain |
| Hard | Highest token-Jaccard admitted event from D2, pattern ≠ P | Encoder beats surface lexical match |
| Adversarial | Random admitted event from D1, pattern ≠ P | Encoder robust to misleading domain cues |

**OVERLAP constraint applied:** OVERLAP-flagged discovery candidate Di-Sf6-4 excluded from defection distractor pools (and vice versa), per [Phase 3 actionable finding #1](./probe-2-phase-3-results.md#actionable-findings-for-phase-4).

## Results

### Problem counts

`[MEASURED]` **200 retrieval problems constructed. All distractors filled.**

| Pattern | Problems |
|---|---|
| Defection | 40 |
| Discovery | 40 |
| Reversal | 40 |
| Confrontation | 40 |
| Rescue | 40 |

### Domain-pair distribution

`[MEASURED]`

| Pattern | Co×Fa | Co×Hi | Co×Sf | Fa×Hi | Fa×Sf | Hi×Sf |
|---|---|---|---|---|---|---|
| Defection | 7 | 6 | 7 | 7 | 7 | 6 |
| Discovery | 7 | 6 | 7 | 7 | 7 | 6 |
| Reversal | 7 | 7 | 7 | 7 | 7 | 5 |
| Confrontation | 6 | 6 | 7 | 7 | 8 | 6 |
| Rescue | 4 | 4 | 3 | 11 | 10 | 8 |

Rescue's skew toward non-corporate combos reflects the thin rescue × corporate cell (9 admitted candidates). Corporate-paired rescue combos draw 3–4 pairs each; non-corporate combos absorb the remainder. This is proportional allocation, not cherry-picking.

### Candidate reuse

`[MEASURED]`

| Appearances | Candidates |
|---|---|
| 1 | 26 |
| 2 | 46 |
| 3 (cap) | 94 |

166 of 536 admitted candidates appear in the test set. The reuse cap of 3 was hit by 94 candidates, indicating that a larger test set (or higher cap) would further diversify, but 200 pairs is the pre-registered target.

### Hard-tier Jaccard scores

`[MEASURED]` Token-Jaccard similarity between query text and Hard distractor text: **min=0.028, mean=0.050, max=0.089.**

| Query domain | Target domain | n | Mean Jaccard |
|---|---|---|---|
| Corporate | Fantasy | 31 | 0.047 |
| Corporate | Historical | 29 | 0.046 |
| Corporate | Sci-fi | 31 | 0.058 |
| Fantasy | Historical | 39 | 0.059 |
| Fantasy | Sci-fi | 39 | 0.044 |
| Historical | Sci-fi | 31 | 0.042 |

**Caveat:** All domain pairs produce uniformly low Jaccard overlap (4–6%). The four domains are too lexically distant for token-level surface overlap to create a meaningfully harder distractor than random selection. The Hard tier is effectively a second Easy tier with a marginal lexical-similarity bias. The diagnostic gradient is three tiers (Easy ≈ Hard, Medium, Adversarial) rather than four.

**Root cause:** Phase 3 rater filtering correctly removed "corporate-in-a-costume" candidates — fantasy/sci-fi/historical candidates that used corporate vocabulary patterns. Those rejected candidates would have had higher cross-domain Jaccard with corporate queries. The filter's success at enforcing domain-authentic vocabulary is in tension with Hard-tier distractor design. This was not anticipated at pre-registration.

**Impact on the experiment:** The headline metric (top-1 accuracy on Easy + Medium + Hard) remains valid — the Hard tier contributes underpowered-but-not-invalid signal. The Adversarial tier (reported separately per spec) carries the real diagnostic weight for encoder robustness. No pre-registered threshold depends on Hard-vs-Easy discrimination.

## Test set status

**Phase 4 complete. The Probe 2 event-mode test set is locked.**

200 problems × 5 options (1 target + 4 distractors) = 1,000 retrieval candidates. Adequately powered per [probe-2-test-set-design § N and statistical power](./probe-2-test-set-design.md#n-and-statistical-power).

## Raw artifacts

- Test set: [`experiments/T_A1b-isolation-derisk/test-set/probe2-test-set.json`](../../../experiments/T_A1b-isolation-derisk/test-set/probe2-test-set.json)
- Manifest: [`experiments/T_A1b-isolation-derisk/test-set/manifest.md`](../../../experiments/T_A1b-isolation-derisk/test-set/manifest.md)
- Construction script: `phase4_pair_construction.py`

## Related

- [probe-2-test-set-design](./probe-2-test-set-design.md) — the pre-registration this page reports against.
- [probe-2-phase-3-results](./probe-2-phase-3-results.md) — the admitted pool this phase draws from.
- [H44-T_A1b-cross-domain-transfer](../../hypothesis/H44-T_A1b-cross-domain-transfer.md) — the hypothesis this test set will evaluate.

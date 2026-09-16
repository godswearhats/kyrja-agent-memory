---
type: experiment
name: "Factored-operator beachhead — Phase 1: task-design validation (idealised stand-ins)"
status: LANDED
last_ingested: 2026-05-27
program: kerros
sources: [./spec.md, ../../concept/integration-gate.md, ../../source/xu-2026-agentic-memo.md, ../../open-question/tier-3-structural-vs-semantic.md]
epistemic_tags: [measured]
tags: [kerros, beachhead, composition, task-validation, matrix-completion, cosine, pre-registration, de-risk]
---

> **Program: [Kerros](../../concept/kerros.md).** Phase 1 of the [factored-operator beachhead](./spec.md): a CPU-only check that the *task design* can express the composition separation — run **before** spending GPU on the Phase-2 LLM arms ("sim before prod"). No LLM here; idealised algorithms stand in for the two arms.

## Hypotheses tested

Not a hypothesis test — a **task-design gate**. It validates the preconditions the [spec](./spec.md) needs before the real composition-separation experiment is worth running. The substantive claim (integrated LLM beats the smart bolt-on) is Phase 2.

## Method

CPU-only (numpy/scipy). Stand-ins, not models:
- **Ideal learner** = low-rank **matrix completion** (soft-impute, rank `m`) — the best-possible structural learner for this generative model; an *upper bound* on any integrated arm. Two variants: **MF-score** (completes the latent score; clean bound) and **MF-label** (completes the observed bucketed labels; realistic preview).
- **Bolt-on floor** = retrieval/lookup (row/col majority) — no structure-learning.
- **Cheat-detector** = order-blind / main-effects (one-vs-rest ridge on `onehot(a)+onehot(b)`) — detects per-symbol signal with no interaction.

Grid: `k ∈ {32,64,128,256,512}`, `m=4`, `C=5` (chance 0.20), 5 seeds; `N` log-swept `k·m → k²/2`; disjoint held-out test set; coverage-guaranteed observed pool. Script, figures, raw rows: [research/experiments/factored-operator-beachhead/](../../../experiments/factored-operator-beachhead/) (`phase1_task_validation.py`, `phase1_results_centered/`).

## Results

`[MEASURED]` All three gates **PASS** on the centred+normalised task (see construct-validity note):

| `k` | ideal (MF-score) | reached at (% of table) | realistic (MF-label) | cheat-detector | lookup floor |
|---|---|---|---|---|---|
| 32 | ~1.00 | 50% | 0.55 | 0.199 | 0.190 |
| 128 | 1.00 | 23% | 0.60 | 0.204 | 0.199 |
| 512 | 1.00 | **15%** | 0.59 | 0.201 | 0.199 |

- **(1) Interaction ≫ marginals** — gap (MF-label − cheat-detector) = +0.35 to +0.39 at every `k`; cheat-detector and lookup sit *on* chance (0.20). The task is composition, not per-symbol main effects.
- **(2) Recoverable cheaply** — the ideal learner hits its ceiling from a *shrinking* fraction of the table as `k` grows.
- **(3) Fan opens** — fraction-to-ceiling 50% → 37% → 23% → 19% → **15%** across `k`. Sub-quadratic; the scaling separation the bet predicts.

### Construct-validity note

The first (raw dot-product) run leaked a **~0.25–0.30 marginal/lookup floor** — per-symbol bias (vector magnitude = "loudness", mean direction = "tilt"; the Netflix user/item bias). **Mean-centring across the population + unit-normalising** the hidden vectors (so the score is adjusted **cosine similarity**) drove the cheat-detector and lookup floors to chance (0.20) **without** moving the structural ceiling — confirming we stripped only the nuisance, not the signal. This discharges the [order-blind / BoW-at-chance gate](../../open-question/tier-3-structural-vs-semantic.md) for this task. Matrix completion is an *upper bound* on the integrated arm (handed the exact rank + the optimal estimator); the Phase-2 LLM will fall between this bound and the lookup floor — Phase 1 establishes only that the bounds exist and separate, not that an LLM reaches them.

Two analysis bugs were found and fixed before this verdict: MF-score was scored by rounding a raw score instead of bucketing it (made the upper bound look like chance), and the separation metric initially compared accuracy at max-`N` (which hides the sample-efficiency story) — re-framed to fraction-of-table-to-ceiling.

## Limitations

- **Idealised, not the real arms.** Matrix completion knows the rank and is optimal; the LLM does not. A Phase-1 pass is necessary, not sufficient — it validates the *task*, not the *hypothesis*.
- **MF-label ceiling ~0.58** (< 1.0) because bucketed labels lose information; the real integrated arm can learn the bucketing nonlinearity and may sit higher. Success is scored **ceiling-relative** for exactly this reason (see [spec](./spec.md)).
- Single output type (5-class), single `m`. The fan is shown over `k`, not over `m`.

## Raw artifacts

- Spec / pre-registration: [spec.md](./spec.md).
- Code, figures (`picture1_acc_vs_N.png`, `picture2_fan_open.png`), raw rows: [research/experiments/factored-operator-beachhead/](../../../experiments/factored-operator-beachhead/).

## Related

- [spec.md](./spec.md) — the locked pre-registration this de-risks; Phase 2 (LLM arms) is the next step.
- [integration-gate](../../concept/integration-gate.md) — the validity gate; the `ᾱ<1` / order-blind check is what Phase 1 discharges here.
- [tier-3-structural-vs-semantic](../../open-question/tier-3-structural-vs-semantic.md) — the BoW-at-chance gate, instantiated here as the order-blind floor.

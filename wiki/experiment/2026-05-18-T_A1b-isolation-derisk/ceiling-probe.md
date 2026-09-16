---
type: experiment
name: Full-arc ceiling probe — pattern is recoverable but lexical; the arc test was confounded
status: LANDED
last_ingested: 2026-05-25
sources: [../../source/bardes-2024-vjepa.md]
epistemic_tags: [measured, asserted]
tags: [t_a1b, ceiling, construct-validity, contamination, bag-of-words, falsification, tier-3]
---

Training-free ceiling control for the arc-mode test set, run 2026-05-25 (Nils + AJ). Motivated by the [de-risk verdict withdrawal](./derisk-run-results.md): once the de-risk's arc retrieval was found scale-confounded, we needed to know whether arc *pattern* is recoverable from the features *at all* before re-scaling any training. The de-risk had a **floor** (the 15.2% token-mean baseline) but never a **ceiling** — so its null was unreadable. This probe establishes the ceiling, and in doing so surfaced two findings that change the research question.

**Verdict: the test set cannot validate the wedge's structural claim.** Arc pattern *is* recoverable — but it is recoverable by a **bag-of-words classifier** (96.5–97.5%), so success on this test does not demonstrate structural retrieval distinct from surface semantics. Routes to [tier-3-structural-vs-semantic](../../open-question/tier-3-structural-vs-semantic.md).

## Why this probe — the ceiling the de-risk lacked

`[ASSERTED]` A retrieval null is only interpretable against a ceiling: "no structural transfer" could mean *the objective failed* or *the task is unexpressible by any readout*. The de-risk asserted the former. This probe tests the latter directly, **training-free**, so it is immune to the scale-mismatch confound that withdrew the de-risk verdict: each arc is run through Phi-3 in **one context** (no 1024-token windowing — every token attends over the whole arc; arcs fit Phi-3-mini-4k), and we read full-context summaries with no encoder, no predictor, no sliding-window mean-pool.

## Pre-registration (locked 2026-05-25, before numbers seen)

`[ASSERTED]` Readouts (all layer-20 unless noted): **C0** token-mean (control, should reproduce the 15.2% floor — wiring check), **R1** last-token, **R2** final-event mean, **R3** last-token @ layer-28. Metrics: 5-way cosine top-1 (chance 20%); adversarial-tier win-rate (chance 50%, the only topic-controlled contrast); supervised PCA→50 + ridge CV on pattern (chance 20%) and domain (topic-richness control, chance 25%). Bands (best full-context readout): REACHED `adv ≥65% & p<0.01 & top-1 ≥40%` (or pattern-CV ≥45%); MARGINAL `adv significant but <65%, or top-1 28–40%`; NO-CEILING `nothing clears adv p<0.01; top-1 ≤25%; pattern-CV ≤28% while domain-CV high`. Decision-critical calls use p<0.01 to absorb Bonferroni over 3 readouts. **Gap (acknowledged post-hoc):** the supervised probe was *not* given its own surface-lexical floor — the analog of C0 for a learned decode. That floor is bag-of-words; adding it is what flipped the interpretation (see below).

## Method (as run)

`[ASSERTED]` Code: [ceiling_probe.py](../../../experiments/T_A1b-isolation-derisk/code/ceiling_probe.py). 200 unique candidates, each run through Phi-3-mini-4k INT4 in a single forward; layer-20 (and layer-28) hidden states captured via forward hooks. Cosine readouts fed to the **same** `evaluate_retrieval` harness as the de-risk. Supervised probe and bag-of-words baseline are numpy PCA→50 + one-hot ridge, 5-fold CV. Sanity: on random features the CV lands at chance (pattern 18.5%, domain 27.0%), confirming the plumbing does not inflate.

## Results

### Cosine retrieval — at chance on every readout

`[MEASURED]` *(Construct-validity: top-1 = 5-way cosine retrieval, same harness/floor as the de-risk; adversarial-win = fraction the target beats the same-domain/different-pattern distractor, chance 50% — the pattern-vs-topic contrast.)*

| Readout | top-1 (chance 20%) | p vs 20% | adversarial-win (chance 50%) | p vs 50% |
|---|---|---|---|---|
| C0 token-mean | 15.2% | 0.93 | 31.2% | 1.0 |
| R1 last@20 | 22.4% | 0.28 | 48.8% | 0.64 |
| R2 final-event@20 | 24.8% | 0.11 | 48.8% | 0.64 |
| R3 last@28 | 21.6% | 0.36 | 48.0% | 0.70 |

C0 reproduces the 15.2% floor exactly (wiring confirmed), and its adversarial rate (31%) is *below* the coin flip — topic-matching is actively *fooled* by same-domain distractors. No full-context readout is distinguishable from chance.

### Supervised decode — pattern 71.5%, but it's lexical

`[MEASURED]` *(Construct-validity: PCA→50 + ridge, 5-fold CV on the Phi-3 last-token rep; pattern = the 5-class label, domain = the 4-class topic label.)* R1@20 decoded pattern at **71.5% ± 4.6** (chance 20%) and domain at 61.0%; R3@28 pattern 59.5%, domain 70.0%. So pattern information *is* linearly present in the full-context rep — but cosine doesn't surface it (the pattern directions are low-variance, drowned by topic/domain variance).

### Bag-of-words kill shot

`[MEASURED]` *(Construct-validity: identical PCA→50 + ridge CV, features = log-count bag-of-words over the candidate text; this is the surface-lexical floor for a learned decode — the supervised analog of C0.)*

| What a word-counter sees | pattern decode (chance 20%) |
|---|---|
| beat **labels** only (~14 words) | **100.0%** |
| Scenario summary only (~72 words) | 90.0% |
| full annotated text (as fed to Phi-3) | 97.5% |
| **clean narrative prose only** (~1224 words) | **82.0%** |

A bag-of-words classifier decodes pattern at 82% from clean narrative alone — and *beats* Phi-3's full-context supervised decode (71.5%). The supervised "ceiling" was just recovering a lexical signal a word-counter recovers better.

## Interpretation

`[ASSERTED]` Two findings, pulling opposite ways:

1. **The de-risk's cosine null was partly a readout artifact, not information-absence.** Pattern information is abundantly present; cosine on a pooled rep is dominated by topic/domain variance and surfaces none of it. So "the pipeline lost the signal" is true to that extent — resolving the scale-confound worry in the direction "structure was there."
2. **But the test cannot validate the *structural* (tier-3) claim.** If a word-counter hits 82% on clean narrative, discriminating these patterns **does not require structural understanding**. Pattern ≈ vocabulary here, even within-domain (the BoW CV mixes all four domains). This lands squarely on [H44](../../hypothesis/H44-T_A1b-cross-domain-transfer.md)'s own stated failure mode — *"fancy embedding similarity the base LLM already does for free."* Any system that "passes" this test, re-scaled or not, is consistent with lexical pattern-matching.

## Test-set contamination (found + fixed)

`[MEASURED]` The candidate `text` fields contained structural scaffolding that leaked the answer: a `**Scenario.**` summary, an `N beats` header, a `**Note on beat order.**` paragraph, and inline `**E# (scene-type).**` beat labels (e.g. `commitment scene`, `violation scene`, `inversion-acknowledged scene`) — present in 200/200 candidates. The beat labels alone decode pattern at 100% from ~14 words. *(Construct-validity: same BoW+ridge CV, restricted to the label substrings.)* This scaffolding was meant for drafting/rating only — [probe-2-test-set-design § Phase 3](./probe-2-test-set-design.md) stripped metadata before *raters* saw it, but it persisted in the stored candidate texts, and the entire de-risk *and* this ceiling probe's Phi-3 numbers were computed on contaminated inputs.

`[ASSERTED]` **Fixed:** narrative-only version saved as canonical [probe2-arc-test-set-narrative.json](../../../experiments/T_A1b-isolation-derisk/test-set/arc-mode/probe2-arc-test-set-narrative.json); [probes.py](../../../experiments/T_A1b-isolation-derisk/code/probes.py) and [ceiling_probe.py](../../../experiments/T_A1b-isolation-derisk/code/ceiling_probe.py) repointed; the annotated original is preserved for provenance. But cleaning only drops BoW from 97.5% → 82%, **not** to chance — so cleaning alone does not make this a valid structural test.

## What this does to H44 and the wedge

`[ASSERTED]` H44 stays PROPOSED (already reverted on the scale confound). The new finding is sharper than scale: the *property* H44 claims — transferable structure distinct from surface — may not be measurable on this test, and may not be a distinct capability at all for narrative patterns. That is a construct-validity question about the [tier-3 wedge](../../decision/tier-3-4-as-wedge.md) itself, opened as [tier-3-structural-vs-semantic](../../open-question/tier-3-structural-vs-semantic.md). AJ is taking the wedge/tier-3 framing back to the drawing board; masked-prediction stays paused.

## Methodological lesson

`[ASSERTED]` **Every learned decode needs its dumb-baseline floor.** Cosine retrieval had a floor (C0 token-mean); the supervised probe did not, so a 71.5% looked like a ceiling until bag-of-words showed a word-counter triples chance. Reusable gate carried to the open-question: **a valid tier-3 structural test must drive an order-blind baseline (BoW) to chance.**

## Raw artifacts

- Code: [ceiling_probe.py](../../../experiments/T_A1b-isolation-derisk/code/ceiling_probe.py); results JSON written to `checkpoints/ceiling_results.json`.
- Cleaned canonical test set + provenance: [test-set/arc-mode/](../../../experiments/T_A1b-isolation-derisk/test-set/arc-mode/) (`probe2-arc-test-set-narrative.json` + `manifest.md`).

## Related

- [derisk run results](./derisk-run-results.md) — the withdrawn-as-confounded verdict this probe followed up.
- [probe-2-test-set-design](./probe-2-test-set-design.md) — the test-set methodology; contamination correction landed there.
- [H44](../../hypothesis/H44-T_A1b-cross-domain-transfer.md) — the hypothesis; this hits its own "fancy embedding for free" failure mode.
- [tier-3-structural-vs-semantic](../../open-question/tier-3-structural-vs-semantic.md) — the open question this probe opened.
- [memory-retrieval-tiers](../../concept/memory-retrieval-tiers.md) — defines tier 3, the capability in question.

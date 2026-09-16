---
type: experiment
name: T_A1b isolation de-risk — run results (REJECTED)
status: LANDED
last_ingested: 2026-05-25
sources: [../../source/bardes-2024-vjepa.md]
epistemic_tags: [measured]
tags: [t_a1b, jepa, derisk, vicreg, collapse, rejected, falsification]
---

Run results for the [T_A1b isolation de-risk](./README.md). The pre-registration is frozen in [experiment-spec](./experiment-spec.md); this page records what the runs produced and is not edited back into the registered plan.

> **Validity correction (2026-05-25, Nils + AJ) — the "REJECTED" verdict is WITHDRAWN as confounded.** This experiment operates end-to-end at **32-event scale** (24-event context → predict 8; windows stride-8; trajectory readout mean-pools sub-arc windows), while the phenomenon and the test live at **arc scale**: the test arcs are ~66-event, four-beat, *non-chronologically-ordered* patterns (median 1313 words), and the training corpus (Gutenberg books) has arcs over *hundreds* of events. The arc-transfer falsifier mean-pools 1.5-beat windows, which destroys the ordered-pattern structure it was meant to measure (and the test's *ceiling* was never established — a test that no readout can pass cannot falsify). The skill metric is a local-task measurement with two non-separable explanations (forward-prediction entropy **and** scale mismatch). **Net: the experiment cannot validly test [H44](../../hypothesis/H44-T_A1b-cross-domain-transfer.md)'s arc-scale claim; H44 reverts to PROPOSED.** What remains valid is narrow and scale-local (the predictable-XOR-high-rank geometry of *one* 32-event config, below). Next step: a training-free full-arc-scale **ceiling control** before any re-scaled training. The masked-prediction continuation is paused (same 32-event window → same confound).

**Verdict (SUPERSEDED — see correction above): REJECTED.** The isolated, auxiliary-only, forward-prediction form of [H44](../../hypothesis/H44-T_A1b-cross-domain-transfer.md) does not produce arc-transferable representations. The pre-registered primary falsifier (arc-mode retrieval vs token-averaged baseline) fired on the one valid (non-collapsed) run. The result is clean and mechanistically understood, not a murky null.

## Hypotheses tested

- [H44 — T_A1b cross-domain transfer](../../hypothesis/H44-T_A1b-cross-domain-transfer.md) — primary. Pre-registered bands: arc top-1 ≥ 25.2% (baseline 15.2% + 10pp) = SUPPORTED; 5–10pp = INCONCLUSIVE; ≤5pp / tie / worse = REJECTED.
- Sub-claim (failure mode 4): the predictor's trajectory state encodes position-in-arc decodably — underwrites the `trajectory_state` field in [multi-field-memory-unit](../../decision/multi-field-memory-unit.md). Tested via the skill control below and the arc probe.

## Method (as run)

- **Frozen feature source unified on HF transformers** so encoder inputs are numerically identical to the 15.2% baseline floor: Phi-3-mini INT4, layer-20 hidden states (SDPA, native Phi3, forward hook), cached once. Cache: 12,915,970 tokens → 499,798 events, mean 25.7 tok/event (EM-LLM surprise segmentation, γ=1.0). See [code/data_pipeline.py](../../../experiments/T_A1b-isolation-derisk/code/data_pipeline.py).
- **Models:** encoder 8,279,040 params (d_E=384, depth 4) + predictor 1,294,976 params (d_P=128 bottleneck, 24 context + 8 target events) + EMA target; V-JEPA L1 feature-space loss on un-normalised reps. See [code/model.py](../../../experiments/T_A1b-isolation-derisk/code/model.py), [code/train.py](../../../experiments/T_A1b-isolation-derisk/code/train.py). (Param counts ran below the spec's ~11M/~1.5M estimates — flagged at build time.)
- **Probes** ([code/probes.py](../../../experiments/T_A1b-isolation-derisk/code/probes.py)): (c) collapse gate — effective rank (participation ratio) of the representation covariance, invalidates the run if `eff_rank < 5`; **predict-the-mean control** (added mid-run, see below); (d) arc-mode retrieval — 5-way cosine on predictor trajectory states, the pre-registered primary falsifier.

## Results

Three training configurations, escalating anti-collapse regularisation:

| Config | Anti-collapse | Eff. rank / 384 | Skill (vs mean floor) | Arc top-1 | Verdict |
|---|---|---|---|---|---|
| pure V-JEPA | none | 7.0 | (control not yet built) | 14.4% (−0.8 pp) | REJECTED — ties baseline |
| + variance | var-coef 50 | 2.5 | +26.7% | — (gate failed) | INVALID — collapsed |
| + VICReg | var 50 + cov 1, batch 16 | 346.8 | +1.1% | 19.2% (+4.0 pp) | REJECTED — marginal |

All figures below are from the run logs and per-checkpoint result JSONs under [checkpoints/](../../../experiments/T_A1b-isolation-derisk/checkpoints/); live verdict console output was read in-session 2026-05-24/25.

### Headline finding: predictable XOR high-rank

`[MEASURED]` Across the three configs the objective exhibits a trade-off it never escapes: the representation is **either** low-rank-and-predictable **or** high-rank-and-structureless, never both. *(Construct-validity: effective rank = participation ratio of the covariance eigenspectrum = dimensions effectively occupied; skill = fraction of the predict-the-mean L1 floor the predictor removes; arc top-1 = 5-way cosine retrieval of trajectory states = the tier-3 structural-retrieval construct, same harness as the baseline floor.)*

- Without anti-collapse pressure, the encoder collapses onto a ~2-dimensional predictable manifold (pure V-JEPA rank 7; variance-only rank 2.5 with skill +26.7% — predicting a near-2D target is easy).
- With full VICReg anti-collapse, the representation fills the space (rank 346.8) but becomes **linearly indistinguishable from matched Gaussian noise** (linear-vs-noise classifier 45.1%, ≈ chance), and the predictor drops to the mean-guess floor (skill +1.1%).

Mechanism: isotropic noise *trivially satisfies* the variance and covariance regularisers (unit per-dim variance, zero correlation), so var+cov *reward* noise; the only thing that could imprint real structure is the prediction signal, which in forward-prediction-of-text is too low-dimensional (~the "drift" component) to compete. *Construct-validity note:* effective rank is the participation ratio of the covariance eigenspectrum — it measures how many dimensions the representation effectively occupies, which is exactly the dimensional-collapse construct; the linear-noise classifier measures whether any linear structure exists beyond per-dim marginals, the necessary-condition for cosine retrieval to work.

### Config detail

- **pure V-JEPA** ([checkpoints/pure-vjepa](../../../experiments/T_A1b-isolation-derisk/checkpoints/pure-vjepa/)): eff rank 7.0 (top-10 dims hold 99.7% of variance — borderline dimensional collapse despite clearing the pre-registered `<5` gate), linear-noise 67.0%. Arc 18/125 = 14.4%, lift −0.8 pp, REJECTED (ties baseline). Tier gradient mirrored the baseline (generic-semantic, not structural).
- **variance-only** ([checkpoints/var50](../../../experiments/T_A1b-isolation-derisk/checkpoints/var50/)): eff rank *fell* to 2.5 (top-1 dim 57.3%; per-dim std 1.26 looked healthy while rank halved). **Variance regularisation alone feeds dimensional collapse**: forcing unit per-dim variance while correlations run free projects one dominant signal onto all coordinates → a rotated thin cigar. Skill +26.7% (trained L1 314.7 vs mean floor 429.6) but on a degenerate 2-D representation. INVALID per the collapse gate (2.5 < 5); arc probe not run, per the no-probing-collapsed-encoders rule.
- **VICReg** ([checkpoints/vicreg](../../../experiments/T_A1b-isolation-derisk/checkpoints/vicreg/)): eff rank 346.8 (threshold rank 383; top-1 dim 0.5%, top-10 4.4% — near-isotropic). Skill +1.1% (trained 318.05 vs mean floor 321.67; predict-zero 321.83). Arc 24/125 = 19.2%, lift +4.0 pp, but P(≥24 | chance 20%) = 0.62 — *fully consistent with chance*, and the rank distribution was uniform (24/24/28/27/22), the fingerprint of no information. The +4 pp "lift" is a mirage: the baseline itself sits below chance, so beating it by 4 pp lands you *at* chance. Tier gradient (easy 69.6% → medium 49.6% → hard 40.0% → adversarial 41.6%) shows a whisp of generic topic similarity but coin-flip on the hard/adversarial distractors that share surface content and differ in arc structure — i.e. generic semantics, no structural transfer.

### Predict-the-mean control (methodological note)

`inv` (the L1 invariance loss) is **not comparable across runs**, because it scales with target variance — a collapsed run gets a low `inv` for free. The control normalises it: it compares the trained predictor's L1 against predicting the global marginal mean of the target reps. `skill = 1 − inv_trained / inv_mean_floor`; skill ≈ 0 means the predictor learned no conditional structure and `inv` is parked at the trivial floor, *independent of effective rank*. This control corrected an in-session error (an initial read of config-1's `inv ≈ 315` as "at the floor" — the floor was actually 429, and the predictor was beating it by 27%). It is reusable for the masked-prediction follow-up. See `predict_floor` in [code/probes.py](../../../experiments/T_A1b-isolation-derisk/code/probes.py).

## Interpretation and scope

- **What is rejected:** the isolated, auxiliary-only, forward-prediction operationalisation of T_A1b. The auxiliary loss *alone* does not bootstrap rich, transferable structure at event-rep scale on frozen Phi-3 text features.
- **What is NOT falsified:** the coupled formulation (`L_total = L_consumer_LM + α·L_aux`), in which a task objective supplies the structural pressure the isolated auxiliary loss lacks. That was deliberately stripped here (pre-registered scope) and remains untested — it is a separate, unwritten claim, not H44 as tested.
- **Confidence update:** this lowers confidence in H44; it does not formally close the coupled question.
- **Forward pointer:** the sharp next hypothesis is masked / inpainting prediction (low-entropy, plausibly higher-dimensional predictable structure — the V-JEPA-faithful framing) rather than forward prediction. See [masked-vs-forward-prediction](../../open-question/masked-vs-forward-prediction.md).

## Raw artifacts

- **Code (re-runnable):** [code/](../../../experiments/T_A1b-isolation-derisk/code/) — data_pipeline, model, data, train, probes, plus the run log.
- **Checkpoints + per-config result JSONs:** [checkpoints/{pure-vjepa, var50, vicreg}/](../../../experiments/T_A1b-isolation-derisk/checkpoints/).
- **Frozen feature cache (74G, reusable for masked-prediction):** [cache/](../../../experiments/T_A1b-isolation-derisk/cache/).
- **Corpus + arc test set:** [corpus/](../../../experiments/T_A1b-isolation-derisk/corpus/), [test-set/arc-mode/](../../../experiments/T_A1b-isolation-derisk/test-set/arc-mode/).
- Live verdict console output: this session's transcript (2026-05-24/25).

## Related

- [README](./README.md) — investigation umbrella.
- [experiment-spec](./experiment-spec.md) — frozen pre-registration.
- [H44](../../hypothesis/H44-T_A1b-cross-domain-transfer.md) — the hypothesis this run REJECTS (scoped to the isolated form).
- [caddy-architecture](../../concept/caddy-architecture.md) — T_A1 is the load-bearing T4 this de-risk tested.
- [memory-retrieval-tiers](../../concept/memory-retrieval-tiers.md) — tier 3, the capability under test.

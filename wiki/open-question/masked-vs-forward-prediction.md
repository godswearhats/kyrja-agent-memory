---
type: open-question
name: Masked (inpainting) vs forward prediction for the T_A1b auxiliary loss
status: OPEN
last_ingested: 2026-05-25
sources: [../source/bardes-2024-vjepa.md]
epistemic_tags: [measured, speculated]
tags: [t_a1b, jepa, masked-prediction, inpainting, derisk, next-experiment]
---

> **PAUSED (2026-05-25, AJ catch).** The premise below — "the forward form was REJECTED, masked is the live continuation" — no longer holds cleanly. The de-risk verdict was **withdrawn as confounded** by an end-to-end **scale mismatch**: it trains/reads at 32-event scale while arcs are ~66-event ordered multi-beat patterns (training corpus arcs are larger still). The masked experiment as designed here *reuses the same 32-event window*, so it inherits the confound and is not the next step. Masking addresses prediction *entropy*; it does **not** address *scale*. Prerequisite before reviving this: the training-free **full-arc-scale ceiling control** (see [H44](../hypothesis/H44-T_A1b-cross-domain-transfer.md) Outcome / [NOW](../NOW.md)). The entropy/dimensionality argument below stays valid *conditional on* re-scaling. **Second reason to stay paused (2026-05-25):** the [ceiling probe](../experiment/2026-05-18-T_A1b-isolation-derisk/ceiling-probe.md) shows the arc test conflates pattern with vocabulary (bag-of-words 82%), so even a successful masked run could not demonstrate *structural* retrieval on it — see [tier-3-structural-vs-semantic](./tier-3-structural-vs-semantic.md).

## The question

Does a **masked / inpainting** prediction objective (hide events in the *middle* of a window, reconstruct them from context on *both* sides) produce high-rank *and* predictable representations where **forward** prediction (predict the next events from the past only) could not?

This is the live continuation of the prediction-family bet after the [T_A1b isolation de-risk](../experiment/2026-05-18-T_A1b-isolation-derisk/derisk-run-results.md) REJECTED the forward form. It is the natural seed for its own hypothesis (next free H-number) once designed; captured here so the forward pointer and rationale are not lost.

## Why it matters

The de-risk found a trade-off the forward objective never escaped: `[MEASURED]` the representation was either low-rank-and-predictable (skill +26.7% at effective rank 2.5) or high-rank-and-structureless (skill +1.1% at rank 346.8, linearly indistinguishable from noise) — never both ([derisk run results](../experiment/2026-05-18-T_A1b-isolation-derisk/derisk-run-results.md)). *(Construct-validity of effective rank and skill is defined in the [derisk run results](../experiment/2026-05-18-T_A1b-isolation-derisk/derisk-run-results.md); these figures are cited from that experiment.)* The diagnosed cause is that the predictable signal in *forward* text is too low-dimensional (~coarse "drift") to imprint structure once anti-collapse pressure forbids the degenerate solution.

`[SPECULATED]` Masked prediction may not share this limit. Forecasting the future of prose is high-entropy (many continuations plausible → mean-guessing is near-optimal under an L1 point loss); filling a gap from *both* sides is low-entropy and constrained, and plausibly carries *high-dimensional* predictable structure (local relations, coreference, syntax). The historical analogue is BERT (masked) vs GPT-style next-token (forward): the masked/bidirectional objective was prized precisely for producing better *representations*. V-JEPA — the frontier anchor for our loss family ([bardes-2024-vjepa](../source/bardes-2024-vjepa.md)) — is itself a masked/inpainting objective in representation space, not a forecaster. The de-risk accidentally built the forecaster; this question asks whether the V-JEPA-faithful framing is the missing lever.

## What would resolve it

A masked-prediction run on the *same* frozen feature cache, encoder, predictor, and arc test set (so the comparison is clean and cheap — main changes are window/mask selection in `data.py` and target selection in `train.py`):

- **Resolves toward the loss-family being viable** if a masked run produces a valid (high effective rank) representation with skill clearly above the mean floor **and** arc retrieval lifts above the 15.2% baseline by the pre-registered margins. Promote to a hypothesis and re-open the coupled-formulation question.
- **Resolves toward the loss family being the wrong tool** if masked prediction *also* lands at the predict-the-mean floor on a high-rank representation. That would generalise the de-risk's negative from "wrong prediction problem" to "the representation-space prediction family does not bootstrap structure at this scale without a task anchor," strengthening the case for the coupled formulation or for [H40](../hypothesis/H40-schema-fit-modulated-consolidation.md) as the pathway.

The same [predict-the-mean control](../experiment/2026-05-18-T_A1b-isolation-derisk/derisk-run-results.md) and collapse gate apply, and thresholds should be pre-registered before the run per [[feedback_falsifiability_offers]] discipline.

## Carry-forward notes (from the de-risk session, for the fresh-context implementer)

**Concrete starting design (a starting point, not locked — design deliberately with AJ):**

- Reuse the 32-event windows. Instead of masking the trailing 8 events (forward), mask K *interior* events at random positions and reconstruct their EMA-target reps from the visible events on *both* sides.
- The predictor already supports this with no architectural rewrite: it uses **full (bidirectional) attention**, learned positional encodings up to 48 positions, and learned mask tokens — so it can place mask tokens at arbitrary positions, not just the tail. The change is mostly in [data.py](../../experiments/T_A1b-isolation-derisk/code/data.py) (which positions are masked + target selection) and how mask tokens are inserted in [train.py](../../experiments/T_A1b-isolation-derisk/code/train.py); the encoder is unchanged.
- Sensible first mask ratio: ~25% (8 of 32), matching the de-risk's target count so capacity/compute stay comparable. Sweep later. Pre-register thresholds against the same arc test set + 15.2% baseline before running.

**Gotchas carried from the de-risk:**

- If reusing VICReg anti-collapse: the covariance term needs N ≥ D = 384 samples per step, so keep **batch ≥ 16** (16 × 24 visible-event reps ≈ 384). At batch 4 the covariance estimate is rank-deficient and the term is just noise — this is why the de-risk's valid run used batch 16.
- The anti-collapse terms (var/cov) act on the **encoder's** reps `z`; the invariance loss acts on the **predictor's** output vs the EMA target. Different surfaces — keep that in mind when reading collapse diagnostics.
- Judge with the **predict-the-mean control (skill)**, not raw `inv`: raw `inv` is not comparable across runs because it scales with target variance (a collapsed run gets a low `inv` for free).
- Masked prediction may not need anti-collapse at all if it has the higher-dimensional predictable structure we hope for — start with pure (no var/cov), check the collapse gate, add regularisation only if it collapses.

**Operational:**

- Run on the **host** via `python` (the container lacks a working torch). Code at [code/](../../experiments/T_A1b-isolation-derisk/code/).
- The 74G frozen feature cache is **reused as-is** — no recompute (same corpus, same Phi-3 layer-20 features). Forward and masked prediction differ only in how the cached event reps are windowed and masked, not in the features themselves.

## Related

- [derisk run results](../experiment/2026-05-18-T_A1b-isolation-derisk/derisk-run-results.md) — the forward-prediction rejection that motivates this.
- [H44](../hypothesis/H44-T_A1b-cross-domain-transfer.md) — REJECTED for the forward form; this is where the live energy routes.
- [bardes-2024-vjepa](../source/bardes-2024-vjepa.md) — the masked/inpainting frontier anchor.
- [caddy-architecture](../concept/caddy-architecture.md) — T_A1 is the load-bearing T4 still under test.

---
type: hypothesis
name: H44 — T_A1b produces structurally-transferable representations supporting cross-domain analogical retrieval
status: PROPOSED
last_ingested: 2026-05-25
sources: [../source/wu-2022-memorizing-transformer.md, ../source/fountas-2024-em-llm.md, ../source/bardes-2024-vjepa.md, ../source/ge-2024-icae.md]
epistemic_tags: [measured, asserted, speculated]
tags: [wedge, t_a1b, jepa, caddy, falsification, construct-validity]
---

## Claim

A JEPA-style auxiliary loss (encoder + narrow-predictor + EMA target + stop-gradient + L1 distance in feature space) on event-segmented memory representations produces representations whose cross-domain analogical retrieval accuracy beats a token-averaged baseline by ≥10 percentage points.

This is the falsifiable form of the **T_A1b wedge claim**: that auxiliary world-model-style training at event-rep scale adds signal beyond consumer LM loss alone, and that the signal manifests as transferable structural retrieval (tier 3 in [memory-retrieval-tiers](../concept/memory-retrieval-tiers.md)) rather than just better next-token prediction.

**Loss spec correction landed 2026-05-20.** The 2026-05-18 ingest of this page recorded the loss as "cosine distance" (inherited from a Web-Claude summary that conflated V-JEPA with BYOL-on-normalised-features). The frontier-adjacent anchor — V-JEPA (Bardes 2024) — explicitly uses **L1 in feature space on un-normalised representations**, having moved away from the L2 used by its image predecessor I-JEPA *for stability* (§3.1 of [bardes-2024-vjepa](../source/bardes-2024-vjepa.md)). We adopt L1 to minimise deliberate deviation from the frontier anchor and to preserve magnitude-encoded information in event reps (cosine would discard magnitude by construction).

## Outcome — verdict WITHDRAWN as confounded (2026-05-25); reverted to PROPOSED

`[ASSERTED]` **Validity correction (2026-05-25, Nils + AJ).** The "REJECTED" verdict below is **withdrawn as confounded**; H44 reverts to PROPOSED — *not validly tested yet*. AJ identified an end-to-end **scale mismatch**: the experiment trains and reads at 32-event scale (24 context → predict 8 events), but the test arcs are ~66-event, four-beat, non-chronologically-ordered patterns (median 1313 words; the discriminative target is *pattern*, not topic), and the training corpus (Gutenberg books) has arcs spanning *hundreds* of events. Two consequences:

- The **arc-transfer falsifier** is readout-confounded. Arc identity is an *ordered* multi-beat pattern, but the trajectory readout mean-pools sub-arc windows (24 events ≈ 1.5 beats), which is order-destroying — it cannot express the construct it was built to test. A test whose ceiling is unestablished cannot falsify.
- The **skill metric** (predict-the-mean control) is a *local* 32-event measurement with at least two non-separable explanations for its low value: intrinsic forward-prediction entropy **and** the scale mismatch (a 24-event window does not contain the arc-level information that determines the targets). It therefore does not bear on arc-scale predictive structure, which is what T_A1b actually claims.

The experiment never trains or measures at the scale of the phenomenon, so it cannot validly test H44. What it *did* establish stands as a narrow finding about one configuration (predictable-XOR-high-rank geometry under 32-event local V-JEPA — see [derisk run results](../experiment/2026-05-18-T_A1b-isolation-derisk/derisk-run-results.md)), but that is not a test of T_A1b. **Next step is a training-free, full-arc-scale ceiling control** — run whole arcs through Phi-3 and test whether pattern is recoverable from full-context features at all (5-way cosine vs the adversarial same-topic/different-pattern distractor) — *before* any re-scaled training run. The masked-prediction continuation is paused: it reused the same 32-event window and so inherits the scale confound.

`[MEASURED]` **Ceiling control done (2026-05-25) — and it sharpened the problem past scale.** The [full-arc ceiling probe](../experiment/2026-05-18-T_A1b-isolation-derisk/ceiling-probe.md) found that on the arc test set a **bag-of-words classifier decodes pattern at 82%** from clean narrative (97.5% with the structural scaffolding that had leaked into the test data, since cleaned; Phi-3 full-context cosine retrieval was at chance on every readout). So the *structural-transfer* property this hypothesis claims may not be **measurable** on this test — and may not be **distinct** from semantic similarity at all, which is exactly the "fancy embedding similarity for free" failure mode named below. This opens [tier-3-structural-vs-semantic](../open-question/tier-3-structural-vs-semantic.md); AJ is taking the wedge/tier-3 framing back to the drawing board before any further T_A1b work.

---

*The verdict below is retained for the epistemic trail but is **superseded** by the correction above.*

### Superseded verdict (2026-05-25 — "REJECTED", scoped to isolated forward-prediction)

`[MEASURED]` *(Construct-validity: arc top-1 = 5-way cosine retrieval on predictor trajectory states, the tier-3 cross-domain structural-retrieval construct, same harness as the 15.2% baseline floor.)* The pre-registered primary falsifier fired: on the one valid (non-collapsed) run, arc-mode retrieval landed at 19.2% top-1 — chance is 20%, P(≥ observed | chance) = 0.62, rank distribution uniform — i.e. a tie with the token-averaged baseline, squarely in the REJECTED band ([derisk run results](../experiment/2026-05-18-T_A1b-isolation-derisk/derisk-run-results.md)). The runs surfaced a trade-off the auxiliary loss never escaped: the representation was **either** low-rank-and-predictable **or** high-rank-and-structureless (linearly indistinguishable from noise), never both.

**Scope — rejected, not foreclosed.** What was tested, and is now rejected, is the *isolated, auxiliary-only, forward-prediction* form: the auxiliary loss alone, stripped of the consumer-LM task loss and cross-attention integration. This does **not** falsify the coupled formulation (`L_total = L_consumer_LM + α·L_aux`), where a task objective could supply the structural pressure the isolated loss lacks — that was deliberately out of scope (necessary-condition test) and remains untested. Nor does it close the prediction family: the live continuation is masked / inpainting prediction (the V-JEPA-faithful framing), tracked at [masked-vs-forward-prediction](../open-question/masked-vs-forward-prediction.md). Confidence in H44 drops; the coupled and masked questions stay open.

## What would falsify it

`[ASSERTED]` Pre-registered falsification thresholds, set 2026-05-18 before the experiment runs (per [[feedback_falsifiability_offers]] discipline):

- **T_A1b representations lose to or tie token-averaged baseline** on cross-domain structural retrieval → REJECTED. The loss isn't producing structural transfer; it's producing fancy embedding similarity the base LLM already does for free.
- **T_A1b representations beat baseline marginally (<5pp lift)** → REJECTED. Signal is real but insufficient to justify the architectural complexity vs. better embedding-based retrieval.
- **T_A1b representations beat baseline by ≥10pp** → SUPPORTED. Structural transfer is real at meaningful margin; wedge claim earns the architecture.
- **5pp ≤ lift < 10pp** → status remains PROPOSED, with experiment design audit and replication required before promotion.

The cross-domain construct is specifically: positive pairs are structurally-analogous events from surface-different domains (e.g., a betrayal arc in corporate fiction paired with a betrayal arc in a fantasy novel); negative pairs share domain but differ in structural pattern. Baseline is averaged token embeddings from the base LLM at the same layer the encoder operates on. Construct-validity note: this measures whether trained representations encode transferable abstract structure independent of surface lexical similarity — which is exactly what tier 3 retrieval requires. The test does not measure tier 4 (predictive recall); that requires the separate trajectory-state probe in failure mode 4 of the experiment.

## Evidence for

- **JEPA family ships at scale in vision** `[ASSERTED]`. V-JEPA produces representations under encoder + narrow-predictor + EMA-target + stop-gradient + L1-feature-space loss without observed collapse, scaled to ViT-H/16 (630M params) on ~2M videos, evaluated by frozen-backbone attentive probing on Kinetics-400 (82.0), Something-Something-v2 (71.4), AVA action localisation, and ImageNet-1K ([bardes-2024-vjepa](../source/bardes-2024-vjepa.md) §3, §5). **Construct-validity narrowing:** V-JEPA evaluates *recognition* transfer (action, motion, object, scene) — it does not evaluate structural / analogical / cross-domain compositional transfer at all, and runs no text or audio experiment. The bet for H44 is that the same loss-family produces a *different* property (cross-domain structural transfer) than V-JEPA itself demonstrated. **Ablation gaps in V-JEPA**: no stop-gradient ablation, no EMA-τ schedule ablation, no predictor depth/width ablation, no token-averaged-baseline control. We adopt V-JEPA's design choices (narrow predictor, linear EMA schedule, stop-grad) as defaults *to minimise unjustified deviation*, but the underlying mechanism's necessity-vs-sufficiency is less anchored than the headline numbers suggest.
- **ICAE shows *some* auxiliary objective on a memory-producing encoder helps at LLM scale** `[ASSERTED]` ([ge-2024-icae](../source/ge-2024-icae.md)). **Same-class-different-shape precedent — see [Loss-family distinction](#loss-family-distinction) below.** ICAE's two objectives (`L_AE` reconstruction + `L_LM` continuation) are *both* token-space next-token CE losses computed at a frozen LLM decoder's output (§2.2.1, §2.2.2). Neither is a loss in representation space on the memory slots themselves; the slots are intermediate hidden states with no direct loss term. Anti-collapse machinery is "frozen decoder must reconstruct text," not the BYOL-triad (no stop-grad, no EMA target). H44 inherits from the JEPA family, not ICAE's family. **What ICAE supports:** the gradient path through a `k`-slot memory bottleneck attached to an LLM can be trained successfully (their Table 5 shows pretraining-at-all wins 6.4× over no-pretraining on GPT-4 pairwise win-rate; the AE+LM mix vs either-alone lift is a smaller 1.3-1.4×). **What ICAE does *not* support:** that representation-space JEPA-shape loss in particular transfers from V-JEPA's recognition-vision scale to LM-memory scale. That extrapolation has no existing precedent and is H44's load-bearing bet.

### Loss-family distinction

The two precedents above belong to different auxiliary-loss families:

| Family | Loss target | Loss space | Anti-collapse mechanism | Precedent |
|---|---|---|---|---|
| Representation-space feature prediction | Predicted feature ≈ EMA-target feature | Feature space (L1) | Stop-grad + EMA + narrow predictor (BYOL triad) | V-JEPA (recognition-vision scale) |
| Token-space reconstruction via frozen decoder | Decoder reconstructs text from memory slots | Token space (CE) | Frozen decoder must reconstruct text | ICAE (context-compression / LLM scale) |

H44/T_A1b inherits from the **representation-space** family. V-JEPA is the same-shape precedent (smaller scope: vision recognition, not language/structural). ICAE is a same-class precedent (some auxiliary objective on a memory-producing encoder helps) but a different-shape mechanism (token-space, no BYOL triad). The honest summary: **the auxiliary-loss-helps-at-LLM-scale signal comes from a different mechanism family than the one H44 commits to; the representation-space loss family has no same-scope LLM precedent at all.**
- **Memorizing Transformer ships co-trained cross-attention** `[ASSERTED]` ([Wu 2022 MemTx §4.5](../source/wu-2022-memorizing-transformer.md)). The mechanical question of "can gradient flow from consumer LM loss back through cross-attention into memory representations" is settled. H44's novelty is the additional auxiliary loss path, not the integration.
- **EM-LLM ships surprise-based event segmentation** `[ASSERTED]` ([Fountas 2024](../source/fountas-2024-em-llm.md)). The encoder side input (event boundaries) is available. H44 does not depend on inventing segmentation.

## Evidence against

- **Cross-domain structural transfer at event-scale is unproven — and the frontier anchor doesn't test it either.** No published memory system has demonstrated tier 3 retrieval at production scale. V-JEPA — the closest precedent for our loss family — evaluates *recognition* transfer (action, motion, object, scene), not structural / analogical / cross-domain compositional transfer ([bardes-2024-vjepa § Downstream evaluation](../source/bardes-2024-vjepa.md#downstream-evaluation-is-recognition-not-structural-transfer)). The post-Norman gap (no system above 2.5/5 in 11 months) is consistent with — but does not directly evidence — the difficulty of this specific claim.
- **JEPA losses on noisy event segmentation may not converge to structurally-transferable representations.** Vision-JEPA inputs are dense frame sequences with regular tube-shaped masking; event-segmented narrative text has variable-length events from a learned (and therefore noisy) segmenter, and our masking analog has no native precedent. The signal-to-noise question is open and is the primary reason this is a T4-tier bet, not T3.
- **Construct-validity risk: "predict next event in latent space" may not equal "encode transferable structure."** Web-Claude conversation 2026-05-18 asserted this equivalence ("predicting what comes next in a sequence and recognizing structural similarity across sequences are closely related problems") without supporting evidence. **V-JEPA does not demonstrate the equivalence either** — its diffusion-decoder visualisations suggest object-permanence and positional uncertainty are encoded, but those are within-modality regularities, not cross-domain structural patterns. The pre-registered cross-domain falsifier is designed to test this equivalence rather than assume it.
- **Ablation gaps in the frontier anchor**: V-JEPA does *not* ablate stop-gradient, EMA τ schedule, predictor depth/width, or alternative loss forms. We adopt the V-JEPA defaults as a *package* — if H44 fails, attribution to specific machinery elements requires separate ablations we'd have to run. The collapse-prevention triad is asserted-by-design and validated only by downstream-task performance V-JEPA had access to (recognition benchmarks) but we don't (our equivalent is the cross-domain probe itself — i.e. the *outcome* we want to test is also the only collapse check we have).

## Open sub-questions

- **Failure mode 4 sub-claim**: does the predictor's internal state encode "position in schema arc" decodably? If not, the trajectory-state field in [multi-field-memory-unit](../decision/multi-field-memory-unit.md) loses its justification. Promoted to a probe within the de-risk experiment, not a separate hypothesis.
- **Does T_A1b conflict with the M17 active-forgetting inversion?** The EMA target encoder accumulates structure on per-step timescales; the consolidator K2 is supposed to be the structure-accumulation locus on longer timescales. Reconciliation is [m17-jepa-reconciliation](../open-question/m17-jepa-reconciliation.md).
- **What's the right α in `L_total = L_consumer_LM + α · L_aux`?** Standard multi-task weighting (GradNorm, uncertainty weighting, or simple α sweep) — engineering, not research. Deferred to experiment design.

## Related

- [2026-05-18-T_A1b-isolation-derisk](../experiment/2026-05-18-T_A1b-isolation-derisk/README.md) — the experiment that tests this hypothesis.
- [derisk run results](../experiment/2026-05-18-T_A1b-isolation-derisk/derisk-run-results.md) — the run that REJECTED the isolated form; predictable-XOR-high-rank trade-off.
- [masked-vs-forward-prediction](../open-question/masked-vs-forward-prediction.md) — the live continuation after this rejection.
- [2026-05-20-probe-2-test-set-design](../experiment/2026-05-18-T_A1b-isolation-derisk/probe-2-test-set-design.md) — methodology pre-registration for probe 2 (the binary falsifier for this hypothesis).
- [tier-3-4-as-wedge](../decision/tier-3-4-as-wedge.md) — the path decision this hypothesis underwrites.
- [multi-field-memory-unit](../decision/multi-field-memory-unit.md) — the paired architectural commitment that lets T_A1b not regress tier 1-2.
- [memory-retrieval-tiers](../concept/memory-retrieval-tiers.md) — defines tier 3, the capability this hypothesis bets on.
- [caddy-architecture](../concept/caddy-architecture.md) — T_A1 is the load-bearing T4 in the op-table; H44 is its falsifiable form.
- [caddy-vs-bolt-on](../concept/caddy-vs-bolt-on.md) — "the single bet that decides the path" was generic T_A1; H44 is the specific T_A1b formulation.
- [memory-caddy](../open-question/memory-caddy.md) — the live open question; H44 is the load-bearing test that resolves it.
- [m17-jepa-reconciliation](../open-question/m17-jepa-reconciliation.md) — the open question raised by H44's mechanism interacting with M17.
- [H41-temporal-context-retrieval](./H41-temporal-context-retrieval.md) — trajectory_state in the multi-field commitment.
- [H42-learned-salience-function](./H42-learned-salience-function.md) — salience signal C is structurally a sub-output of T_A1b's loss.

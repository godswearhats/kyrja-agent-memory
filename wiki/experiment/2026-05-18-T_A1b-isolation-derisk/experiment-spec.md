---
type: experiment
name: T_A1b isolation de-risk — encoder + predictor probe before full caddy build
status: PROPOSED
last_ingested: 2026-05-21
sources: [../../source/wu-2022-memorizing-transformer.md, ../../source/fountas-2024-em-llm.md, ../../source/bardes-2024-vjepa.md, ../../source/ge-2024-icae.md]
epistemic_tags: [asserted, speculated]
tags: [t_a1b, jepa, derisk, falsification, pre-registered, caddy]
---

Pre-registered de-risk experiment for the caddy's load-bearing T4. Trains just the encoder and predictor on event-segmented narrative data with a JEPA-style auxiliary loss, in isolation from any LLM consumer or cross-attention integration. Probes the resulting representations for cross-domain structural transferability before committing engineering effort to the full caddy build. Scope: ~1 GPU, weeks not months. Falsification thresholds set 2026-05-18 *before* the run begins, per [[feedback_falsifiability_offers]] discipline.

## Hypotheses tested

- [H44-T_A1b-cross-domain-transfer](../../hypothesis/H44-T_A1b-cross-domain-transfer.md) — primary hypothesis. T_A1b produces representations whose cross-domain analogical retrieval beats a token-averaged baseline by ≥10pp.
- Sub-claim within H44 (failure mode 4): the predictor's internal state encodes position-in-schema-arc decodably. This sub-claim underwrites the `trajectory_state` field in [multi-field-memory-unit](../../decision/multi-field-memory-unit.md).

## Method

`[SPECULATED — specification, not yet executed]`

**Architecture** *(V-JEPA-anchored defaults, ratified 2026-05-20 — see [bardes-2024-vjepa](../../source/bardes-2024-vjepa.md). Concrete specs ratified 2026-05-24 — pre-implementation item #4)*.

### Base LLM (frozen)

**Phi-3-mini-4k-instruct (3.8B), INT4 GGUF.** Provides token-level hidden states for encoder input. Frozen — no gradients, no parameter updates.

- GGUF path: `Phi-3-mini-4k-instruct-q4.gguf`
- Hidden dim: 3072, 32 layers.
- **Extraction layer: 20** (0-indexed, 62.5% depth). Mid-to-late — past syntactic layers, before output-specialised layers. Chosen as a reasonable default for semantic content; tunable during the ≤5-config hyperparameter audit if needed.
- VRAM: ~2.5 GB (model + inference activations for a batch of events).
- **Fallback: Llama-3.2-3B** (also 3072 hidden dim, 28 layers; confirmed fit on RTX 2080 Ti). No published γ but tunable in calibration.
- Also serves as the segmentation model (surprise-based NLL for EM-LLM event boundaries).

Hardware constraint: RTX 2080 Ti, 11 GB VRAM. LLaMA-3.1-8B (option b / LoRA-adapted encoder) is shelved — infeasible on this rig. Option (a) small dedicated encoder locked.

### Encoder E

Small transformer on top of frozen base-LLM hidden states. Compresses per-token hidden states of one event (~25 tokens × 3072 dim) into a single event representation z_n (d_E dim).

| Parameter | Value | Rationale |
|---|---|---|
| Input projection | 3072 → d_E (linear) | Per-token, maps base-LLM hidden dim to encoder dim |
| d_E | 384 | Matches V-JEPA predictor width; sufficient capacity for ~25-token events |
| Depth | 4 transformer blocks | Self-attention aggregates token-level features; 4 blocks sufficient at this scale |
| Heads | 6 (64 per head) | Standard head dim |
| FFN inner dim | 1536 (4 × d_E) | Standard MLP ratio |
| Normalisation | Pre-LayerNorm | More stable for small transformers |
| Pooling | Learned [CLS] token prepended to sequence | Output at [CLS] position = z_n |
| Positional embeddings | Sinusoidal | Generalises to variable event lengths without length-sensitivity |
| Max positions | 64 tokens | Covers virtually all events (median ~24, rare outliers up to ~50) |
| Dropout | 0.0 | V-JEPA uses none |
| Total params | ~11M | ~22 MB fp16 |

### Predictor P

Narrow transformer bottleneck. Processes a sequence of event representations (context + learnable mask tokens) and outputs predictions at mask positions.

| Parameter | Value | Rationale |
|---|---|---|
| Input projection | d_E → d_P (linear) | Narrows encoder output to bottleneck width |
| d_P | 128 (d_E / 3) | Preserves V-JEPA narrow-predictor ratio (~3-4×); bottleneck forces structural abstraction |
| Depth | 6 blocks | Scaled from V-JEPA's 12; proportional to our smaller scale |
| Heads | 4 (32 per head) | Workable head dim |
| FFN inner dim | 512 (4 × d_P) | Standard MLP ratio |
| Output projection | d_P → d_E (linear) | Maps back to encoder dim for L1 loss against target encoder |
| Normalisation | Pre-LayerNorm | Consistent with encoder |
| Positional embeddings | Learned | Fixed context window; no length generalisation needed |
| Max positions | 48 | 32 context + 8 mask + headroom for inference |
| Attention | Full (bidirectional) | Mask tokens attend to context and to each other (V-JEPA default) |
| Dropout | 0.0 | V-JEPA uses none |
| Total params | ~1.5M | ~3 MB fp16 |

### EMA target encoder E'

Copy of encoder E, updated via exponential moving average. Provides stop-gradient targets.

| Parameter | Value | Rationale |
|---|---|---|
| τ start | 0.998 | V-JEPA default (§10) |
| τ end | 1.0 | V-JEPA default |
| τ schedule | Linear over training | V-JEPA default |
| Params | ~11M (shared architecture with E) | ~22 MB fp16 (no optimizer state — not trained directly) |

### Loss

L_aux = (1/M) Σ_k ‖P(z_n) − sg(z'_{n+1})‖_1 — **L1 in feature space, un-normalised, per-target-position averaged** (V-JEPA §3.1 Eq. 1, §9 Eq. 2). H44's original 2026-05-18 specification said "cosine distance"; updated to L1 to match the frontier anchor. See [H44 § Claim](../../hypothesis/H44-T_A1b-cross-domain-transfer.md#claim) for the correction rationale.

No LLM consumer in this experiment. No cross-attention integration. No consumer LM loss. The aim is to isolate the question: *does this loss family produce structurally-transferable representations on event-segmented text at all?*

### Pre-registered design choices (deliberate deviations from V-JEPA)

**Masking strategy: causal block prediction.** *(Ratified 2026-05-24.)*

Given a window of 32 consecutive events from a document:
- **Context**: events 1–24 (encoded by E, fed to predictor as input)
- **Targets**: events 25–32 (8 events, encoded by EMA target E', used as prediction targets)
- **Masking ratio**: 25% (8/32) — lower than V-JEPA's ~90%, appropriate because events are far sparser than video patches and each carries more information
- **Directionality**: causal (context precedes targets). Natural for temporal narrative; directly trains the predictor to learn "what happens next," supporting both arc-mode probe 2 (structural trajectory retrieval) and probe 3 (trajectory state decodability)
- The predictor sees 24 context event vectors + 8 learnable mask tokens (with positional embeddings) and outputs predictions at the 8 mask positions
- Full (bidirectional) self-attention within the predictor — mask tokens attend to context and to each other

**Target granularity: per-event (one vector per event).** *(Ratified 2026-05-24.)*

V-JEPA predicts per-patch (many vectors per clip). We predict per-event: one d_E-dim vector per masked event, compared via L1 against the EMA target encoder's pooled [CLS] output for that event. Structural patterns operate at the event level; the encoder's [CLS] captures per-event semantics, and the predictor composes event-level transitions.

**Segmentation granularity: γ = 1.0.** *(Ratified 2026-05-24.)*

Tested during corpus assembly. Produces coherent ~25-token events (1-2 sentences) across all three corpus registers. Structural patterns span multiple events; the predictor learns event-to-event transition sequences. Higher γ (coarser events) is a tunable hyperparameter for the ≤5-config audit if needed; γ=1.0 locked for the initial run.

**Context window: 32 events.** *(Ratified 2026-05-24.)*

Covers ~800 tokens of narrative (~1.5 pages). Sufficient for multi-event structural arcs. Sliding windows with stride 8 sample overlapping contexts from longer documents.

**Training scale:** ~3 orders of magnitude smaller than V-JEPA (single-GPU, weeks, ~10M tokens vs ~270M samples / 2M videos). Negative result interpretation must distinguish "the bet fails" from "the bet needs scale we didn't give it."

**Collapse-prevention validation:** V-JEPA validates only indirectly (downstream metrics + diffusion-decoder qualitative). We will add a direct collapse measurement (rank of representation covariance, per probe 1 below) since the indirect proxies require a trained downstream pipeline V-JEPA had but we don't.

**Encoder architecture:** option (a) small dedicated encoder on frozen base-LLM hidden states, locked for RTX 2080 Ti (ratified 2026-05-21). Option (b) LoRA-adapted base-LLM is shelved as a scale-up path requiring cloud rental. Option (c) projection-only head rejected as too novel and uninterpretable on negative result. See [ICAE source notes](../../source/ge-2024-icae.md) for the precedent tension.

### Inference procedure for arc-mode probe

At evaluation time (arc-mode retrieval), the predictor state serves as the retrieval representation.

**Amended 2026-05-24 — sliding-window-mean extraction** (see [probe-2-test-set-design § Pre-registration amendment log](./probe-2-test-set-design.md#pre-registration-amendment-log)). Arc texts segment into ~80 sub-events, exceeding the predictor's 48-position capacity (trained on 24 context + 8 mask), so the literal "z₁…z_N + one MASK" procedure is infeasible. The trajectory state is extracted by sliding the trained window across the arc:

1. Segment the arc's scenes into ~25-token sub-events via EM-LLM segmentation (same γ=1.0)
2. Run frozen Phi-3-mini on each sub-event → token-level hidden states at layer 20
3. Run encoder E on each sub-event → z_1...z_N
4. Slide a 24-context + 8-mask predictor window across z_1...z_N at stride 8 (the training stride). At each window position, run predictor P and take the 8 mask-position outputs (after output projection → d_E = 384)
5. The arc's **trajectory state** is the mean of all mask-position outputs across all windows — a 384-dim vector. It is the predictor's aggregated "what comes next" signal over the arc, which implicitly encodes the structural trajectory traversed
6. Retrieval: cosine similarity between trajectory states across domain pairs
7. Arcs with fewer than 32 events (rare — arcs are ~80) fall back to a single window of all available events + a trailing MASK, which stays within the 48-position capacity

**Baseline:** averaged token embeddings from Phi-3-mini layer 20, mean-pooled across all tokens in the arc's text → one 3072-dim vector. Cosine similarity for retrieval. No training, no auxiliary loss. (The baseline's whole-text token mean is the parallel of the trajectory-state mean — both aggregate over the whole arc.)

### VRAM budget

| Component | Estimate |
|---|---|
| Phi-3-mini INT4 (frozen, inference) | ~2.5 GB |
| Encoder E (weights fp16) | ~22 MB |
| Encoder E' EMA copy | ~22 MB |
| Encoder AdamW states (fp32) | ~88 MB |
| Predictor P (weights + optimizer) | ~18 MB |
| Activations (batch 4, 32 events) | ~1-2 GB |
| **Total** | **~4-5 GB** |

~6 GB headroom on 11 GB RTX 2080 Ti. Room for batch size 4 with gradient accumulation to effective batch 16-32.

**Data.**
- **Training corpus**: narrative-heavy natural text — fiction, biography, long-form journalism, case studies. Initial scope ~10M tokens, scalable if collapse-prevention requires more.
- **Event segmentation**: surprise-based using base LLM's NLL with adaptive threshold (the EM-LLM mechanism per [Fountas 2024](../../source/fountas-2024-em-llm.md)). Re-used as-is, not re-trained.
- **Held-out evaluation set**: structurally-paired narrative events from surface-different domains (see Cross-domain structural retrieval probe below).

**Probes — three of them, run on the trained encoder.**

1. **Collapse check** (sanity). Compute rank of the representation covariance matrix across a batch of events. If rank << dimension, collapse occurred; the run is invalidated and hyperparameters revised. Second-layer sanity (added 2026-05-20 from V-JEPA pressure-test): train a small linear classifier to distinguish event reps from Gaussian noise of matched dimensionality. Above-chance accuracy is necessary-but-not-sufficient for the reps being informative. V-JEPA used a separately trained diffusion decoder for the equivalent qualitative check (§6); we substitute a linear-classifier-against-noise check because our scale doesn't support training a decoder.

2. **Cross-domain structural retrieval probe** (the primary falsifier). Methodology pre-registration: [probe-2-test-set-design](./probe-2-test-set-design.md) — pattern set, domain set, distractor tiering, rater protocol, anti-contamination measures. **2026-05-24 amendment: arc-mode primary, event-mode diagnostic** (see [probe-2-test-set-design § Pre-registration amendment log](./probe-2-test-set-design.md#pre-registration-amendment-log)). The summary below is updated to reflect the amendment.
   - Construct N synthetic arc sequences with known structural patterns (defection, discovery, reversal, confrontation, rescue) across surface-different domains. Each arc is a sequence of 4-5 scenes.
   - Positive pairs: same structural pattern P, different domain (corporate ↔ fantasy ↔ historical ↔ sci-fi).
   - Negative pairs: same domain, different structural pattern Q ≠ P.
   - Task: each arc's scenes are segmented into ~25-token sub-events, encoded, and fed through the predictor. Given query predictor-state of A, does predictor-state of structurally-analogous B rank higher than predictor-state of same-domain-but-different-pattern C?
   - **Baseline**: averaged token embeddings from base LLM at the extraction layer, averaged across all tokens in the arc's text.
   - Metric: top-1 retrieval accuracy on the cross-domain arc pairs.

3. **Trajectory-state decodability probe** (sub-claim test).
   - Generate synthetic narrative sequences with known schema arcs (controlled state-machine: setup → development → escalation → resolution).
   - Train a small linear classifier on top of the predictor's internal state to predict the current position in the arc.
   - Compare to: linear classifier on raw event embeddings, linear classifier on the encoder output z_n.
   - Decoded above chance with measurable margin → trajectory_state architectural commitment is supported. At or near chance → trajectory_state field in S1 loses its justification.

### Construct-validity note

**The primary falsifier (probe 2) measures cross-domain structural retrieval accuracy via predictor trajectory states.** This matches the H44 claim because:
- Tier 3 retrieval (the wedge capability per [memory-retrieval-tiers](../../concept/memory-retrieval-tiers.md)) is *defined* as matching on transferable structural pattern across surface-different contexts.
- The caddy's retrieval mechanism operates at the sequence level: fragment-level encoder outputs are composed by the predictor into trajectory states, and retrieval matches trajectory states. Arc-mode tests this mechanism directly; event-mode (which tests encoder outputs on single scenes) tested a capability the system doesn't use in production and had a granularity mismatch (see [probe-2-test-set-design § Pre-registration amendment log](./probe-2-test-set-design.md#pre-registration-amendment-log)).
- The token-averaged baseline controls for "the base LLM already does this." If predictor trajectory states don't beat that baseline, the auxiliary loss + predictor composition isn't adding the tier-3 capability we claim.
- Cross-domain (not within-domain) is the load-bearing axis. Within-domain transfer is tier 2 — already solved by current systems and not what the wedge claims. Moving the goalposts to within-domain post-hoc is a pre-registered motivated-reasoning tell to watch for.

**What the metric does not measure**: tier 4 (predictive recall). That requires probe 3 (trajectory-state decodability), which is a separate test.

**Known confound**: structural-pattern labelling is partly subjective. Mitigation — pre-register the structural patterns and their domain pairings before generating the test set, not during analysis. Use inter-rater agreement on a sample of pairs to bound labelling noise.

### Granularity rationale — why ~25-token events, not arc-sized memories `[ASSERTED]`

`[ASSERTED]` Plain-English design rationale, captured 2026-05-24 (AJ) to avoid re-litigating the grain choice.

**The objection.** A "memory" intuitively feels arc-sized — a whole episode ("the time I argued with my boss and quit") — not a ~25-token fragment. So why does the architecture store at the fine event grain?

**The resolution: store fine, reconstruct the arc (a normalize/denormalize split).**
- Fine events (~25 tokens, from E1 surprise segmentation) are the **storage atoms** — the addressable rows.
- The arc-sized "memory" is the **recall-time view**, not a stored unit: [`trajectory_state`](../../decision/multi-field-memory-unit.md) matches retrieval at the arc level ("where in the unfolding pattern is this?"), and the cross-attention interface + golfer reassemble the broader episode on read. "A memory is arc-sized" is true of *recall*, not *storage* — store the rows, recall the join.

**Why the fine grain is load-bearing, not an EM-LLM artifact:**
1. **Recombination / construction.** Fine pieces compose into *novel* arcs never literally experienced (op K6 offline composition; the M16 prospective-brain capability). Storing whole arcs forfeits that generativity — you can only recall what you stored, not construct.
2. **Segmentation tractability.** Surprise gives fine boundaries cheaply and naturally; arc boundaries are a fuzzier, higher-level judgment.

**Cognitive-science footing.** Event-segmentation theory: experience is chunked at fine boundaries that nest hierarchically into episodes/arcs. Both grains are real; the ~25-token event is the fine grain, the recalled "memory" is the coarse one.

**Why this experiment trains at event grain but evaluates at arc grain.** The arc-mode probe's central question *is* this granularity bet restated: **does arc-level structure emerge from event-grain representations composed by the predictor?** This is also why arc-mode aggregates fine trajectory states into an arc-level vector (see [Inference procedure for arc-mode probe](#inference-procedure-for-arc-mode-probe)).
- **SUPPORTED** → "store fine, recall arc" works; the arc-sized memory emerges from composition.
- **REJECTED** → arc-level structure may not survive composition from fine pieces; coarser-grained representations may be needed — a genuine architectural pivot, and this intuition would be what flagged it.

**Baseline-floor / ceiling pre-check (added 2026-05-20 from V-JEPA pressure-test; updated 2026-05-24 for arc-mode primary).** Before training begins, measure the token-averaged-base-LLM baseline's accuracy on the cross-domain structural retrieval probe (arc-mode pairs). Two outcomes change interpretation of the ≥10pp threshold:
- If baseline accuracy is near chance (e.g., <30% top-1 on a balanced multi-way retrieval), the base LLM's mid-layer features don't already encode the relevant structural similarity. A ≥10pp lift is informative but the bar is relatively low — and we should ask whether *anything* trained on event reps would clear it, not just T_A1b.
- If baseline accuracy is near ceiling (e.g., >80%), the base LLM's features already capture most of the structural signal, and ≥10pp lift may be near-impossible in principle. We may need a harder probe (more distractors, finer-grained pattern distinctions) or a different threshold.
- If baseline lands in a middle band (e.g., 40-70%), ≥10pp lift is a meaningful test of whether T_A1b adds signal *beyond* what the base LLM's representations already provide.

The pre-check protects the falsification from being either trivially passable or trivially impossible. Pre-register the baseline result *before* training, and lock in any threshold adjustment *only* if the baseline is at a ceiling or floor extreme. Treat any threshold adjustment in the middle band as a goalpost-moving tell.

**Baseline-floor result (measured 2026-05-24, pre-registered before training).** Token-averaged Phi-3-mini layer-20 hidden states, mean-pooled across all tokens per arc text, cosine similarity for 5-way retrieval (1 target + 4 distractors). 125 arc-mode problems, 200 unique candidate texts.

| Metric | Value |
|---|---|
| **Overall top-1 accuracy** | **19/125 (15.2%)** |
| Chance baseline (1-of-5) | 20.0% |
| Target–distractor cosine separation | -0.0001 (target mean 0.9818, distractor mean 0.9819) |
| Rank distribution | nearly uniform (15/22/24/19/19% across ranks 1–5) |

Per-pattern: defection 16.0%, discovery 12.0%, reversal 4.0%, confrontation 24.0%, rescue 20.0%. No pattern reliably above chance.

Per-tier pairwise (target beats distractor): easy 72.8%, medium 48.0%, hard 43.2%, adversarial 31.2%. The difficulty gradient works as designed — easy distractors (different domain, different pattern) are distinguishable by generic semantic similarity, but this doesn't help in 5-way ranking because the target is also semantically similar to the query.

**Interpretation: floor regime — baseline is at/below chance.** The ≥10pp threshold (SUPPORTED at ≥25.2%) is a low but meaningful bar. The base LLM's mid-layer features carry zero structural signal for cross-domain pattern matching; the trained encoder+predictor must create this signal from scratch. No threshold adjustment warranted.

**Precedent-anchored effect-size context (added 2026-05-20 from [ICAE verbatim read](../../source/ge-2024-icae.md)).** The ICAE verbatim read surfaced that within-objective-mix effects in the closest same-class precedent are *modest*: their Table 5 win-rate gain from AE+LM-mix over either-objective-alone is **1.3-1.4× pairwise win/lose** (the big effect is "pretraining-at-all vs no-pretraining" at 6.4×, which is a different question). ICAE's metric (GPT-4 pairwise win-rate on downstream instruction-following after fine-tuning) is not directly comparable to our probe (cross-domain structural retrieval top-1 accuracy), so the numerical 1.3-1.4× does *not* translate cleanly to a percentage-point prediction on our metric. But the qualitative implication is real: **within-objective-mix effects at LLM scale may be smaller than the ≥10pp threshold implies**, and a REJECTED outcome at our threshold could reflect either (a) the T_A1b bet itself failing, or (b) the threshold being aggressive relative to mechanism-family effect sizes.

**This disclosure does *not* loosen the threshold.** The ≥10pp bar is preserved; pre-loosening to accommodate the precedent-anchored prior would be exactly the goalpost-shifting failure mode the experiment is designed to resist (per [[feedback_falsifiability_offers]] pre-registration variant). The SUPPORTED/REJECTED line stays binary; no MIXED middle tier is introduced.

**What changes:** post-hoc analysis must report (a) absolute lift magnitude, (b) statistical significance against noise, (c) comparison to the ICAE-precedent effect size adjusted for metric differences. A REJECTED outcome with lift in the 3-9pp significant range is *consistent with same-class precedent effect sizes* — meaning the honest read is "the bet may be live but under-powered at this scale," not "the bet is dead." Pre-register that interpretation: a REJECTED-with-non-trivial-lift result triggers a scale-up or architectural-revision proposal, not abandonment; a REJECTED-with-near-zero-or-negative-lift result is genuine failure.

## Pre-registered thresholds

`[ASSERTED]` Set 2026-05-18 before run, locked-in:

| Probe 2 outcome | Verdict on H44 |
|---|---|
| T_A1b reps lose to baseline (worse than token-averaging) | REJECTED — T_A1b is actively harmful |
| T_A1b reps tie baseline (within noise) | REJECTED — T_A1b provides no value over what base LLM already does |
| T_A1b reps beat baseline by <5pp | REJECTED (marginal) — insufficient to justify architectural complexity |
| T_A1b reps beat baseline by 5-10pp | INCONCLUSIVE — replicate with audit before promotion |
| T_A1b reps beat baseline by ≥10pp | SUPPORTED — wedge claim earns the architecture |

| Probe 3 outcome | Verdict on trajectory_state commitment |
|---|---|
| Predictor state ≈ chance on arc position | trajectory_state field in S1 loses justification; reconsider [multi-field-memory-unit](../../decision/multi-field-memory-unit.md) |
| Predictor state > chance, margin ≥ baseline by 10pp | trajectory_state commitment supported |
| In between | INCONCLUSIVE |

## Limitations

`[ASSERTED]`
- **No LLM consumer in the loop.** The full caddy bet is that T_A1b adds signal *beyond consumer LM loss alone*. This experiment cannot test that — it tests whether T_A1b produces structured representations *at all*. A positive isolation result is necessary-but-not-sufficient for the wedge; a negative isolation result is sufficient to kill it cheaply.
- **Synthetic structural-pair test set.** Probe 2 uses constructed pairs with controlled structure. Real-world tier 3 retrieval involves messier surface variation. The synthetic test is a tractability proxy; downstream evaluation on natural retrieval tasks is required for product-claim support.
- **Event-segmentation quality is inherited from EM-LLM.** If segmentation noise dominates the loss signal, T_A1b may fail through no fault of its own. Mitigation — sanity-check segmentation quality on the training corpus separately before drawing conclusions.
- **Single hyperparameter regime.** Initial run uses one EMA momentum, one predictor architecture, one α weighting. Negative result triggers a hyperparameter audit before final REJECTED verdict — but the audit's scope is bounded (≤5 configurations) to prevent goalpost-moving.

## Goalpost-moving tells (pre-committed)

`[ASSERTED]` Per [[feedback_falsifiability_offers]], pre-commit to watching for these patterns in self-talk during analysis:
- Wanting to relax cross-domain to within-domain ("well, it does *something*...") — within-domain is tier 2, already solved, doesn't earn the architecture.
- Wanting to add more probes to find one T_A1b passes — pre-registered probe set is fixed.
- Wanting to attribute failure to "noisy data" without independent evidence — segmentation/data quality must be diagnosed *before* training, not after a bad result.
- Wanting to expand "≥10pp" threshold downward to "the result is what it is."
- Wanting to switch back to event-mode results to rescue a failing arc-mode result — arc-mode is the verdict per 2026-05-24 amendment; event-mode is diagnostic only.

## Raw artifacts

- Pre-registration commit (this page) — 2026-05-18.
- Baseline-floor pre-check results — 2026-05-24. Raw: `results.json`, features: `features.npz`. Notebook: `baseline_floor_precheck.ipynb`.
- Training scripts, dataset spec, probe code — `pending`.
- Results, run logs — `pending`.

## Related

- [probe-2-test-set-design](./probe-2-test-set-design.md) — methodology pre-registration for Probe 2's test set.
- [H44-T_A1b-cross-domain-transfer](../../hypothesis/H44-T_A1b-cross-domain-transfer.md) — primary hypothesis under test.
- [tier-3-4-as-wedge](../../decision/tier-3-4-as-wedge.md) — decision this experiment underwrites; negative result triggers reversal.
- [multi-field-memory-unit](../../decision/multi-field-memory-unit.md) — trajectory_state sub-commitment tested by probe 3.
- [memory-retrieval-tiers](../../concept/memory-retrieval-tiers.md) — defines tier 3, the capability being tested.
- [caddy-architecture](../../concept/caddy-architecture.md) — op T_A1 is the load-bearing T4 this experiment de-risks.
- [memory-caddy](../../open-question/memory-caddy.md) — the live open question; this experiment's outcome resolves it.
- [m17-jepa-reconciliation](../../open-question/m17-jepa-reconciliation.md) — open question raised by T_A1b's mechanism interacting with M17.

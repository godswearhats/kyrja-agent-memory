---
type: experiment
name: Probe 2 test set design — methodology pre-registration for T_A1b cross-domain structural retrieval
status: PROPOSED
last_ingested: 2026-05-25
sources: [../../source/bardes-2024-vjepa.md, ../../source/ge-2024-icae.md, ../../source/fountas-2024-em-llm.md]
epistemic_tags: [asserted, speculated]
tags: [t_a1b, probe-2, falsification, pre-registered, test-set-design, caddy]
---

Pre-registration spec for the test set used by Probe 2 of [experiment-spec](./experiment-spec.md). Probe 2 carries the binary SUPPORTED/REJECTED verdict on [H44](../../hypothesis/H44-T_A1b-cross-domain-transfer.md); the rigour of its test set bounds the verdict's trustworthiness directly. Pattern set, domain set, rater protocol, distractor tiering, anti-contamination measures, and pre-registered thresholds are committed here *before any pair is generated*, per [[feedback_falsifiability_offers]] pre-registration discipline.

> **Contamination + construct-validity correction (2026-05-25, Nils + AJ).** Two execution gaps the [ceiling probe](./ceiling-probe.md) surfaced, neither visible in this design:
> 1. **Scaffolding leak.** The stored arc candidate `text` fields retained structural scaffolding (`**Scenario.**` summary, `N beats` header, `**Note on beat order.**`, inline `**E# (scene-type).**` labels). The Phase-3 metadata strip (below) applied to what *raters* saw, **not** to the stored texts. A bag-of-words classifier decodes pattern at **100%** from the beat labels alone. Cleaned → canonical [probe2-arc-test-set-narrative.json](../../../experiments/T_A1b-isolation-derisk/test-set/arc-mode/probe2-arc-test-set-narrative.json); code repointed; original preserved.
> 2. **Lexical confound (deeper).** Even clean narrative is **82% bag-of-words-decodable**, so the Phase-2 measure of forbidding pattern *names* was insufficient — pattern rides on broader vocabulary. **This test does not isolate structure from semantics.** New validity gate: a structural test must drive an order-blind baseline (BoW) to chance. Tracked at [tier-3-structural-vs-semantic](../../open-question/tier-3-structural-vs-semantic.md).

## Scope

`[ASSERTED]` This document specifies the *test set* for Probe 2 (the set of event-pairs the trained encoder is evaluated against). It does not specify probe execution — encoder forward pass, similarity ranking, accuracy computation — which lives in the [parent experiment spec § Probes](./experiment-spec.md#probes--three-of-them-run-on-the-trained-encoder).

## Two-mode design: arc-mode primary, event-mode diagnostic

`[ASSERTED]` Probe 2 runs in two modes against the same trained model. (Earlier drafts named these "M-mode" and "S-mode"; renamed 2026-05-21 for legibility. **2026-05-24 amendment:** arc-mode promoted to primary falsifier; event-mode demoted to diagnostic. See [§ Pre-registration amendment log](#pre-registration-amendment-log).)

**Arc-mode (multi-event)** — primary falsifier. Each test item is a sequence of 4–5 events (scenes) that together instantiate an arc-level pattern. Each scene is segmented into ~25-token sub-events (matching the encoder's training granularity), encoded, and fed through the predictor. The predictor's final hidden state is the retrieval representation. Tests whether the encoder + predictor system produces structural trajectory representations that transfer across domains — the actual caddy tier 3 retrieval mechanism.

**Event-mode (single-event)** — diagnostic. Each test item is one event containing a complete micro-pattern instantiation. Reported with multiple aggregation strategies (encoder on full text, segment + mean-pool, segment + predictor state) as a secondary analysis. Informative but not the falsifier.

**Why arc-mode is primary.** The caddy's tier 3 retrieval operates at the sequence level through predictor state: the agent experiences a sequence of events, the predictor composes fragment-level encoder outputs into a trajectory state, and retrieval matches trajectory states across domains. The predictor state is the retrieval key — not individual encoder outputs. Arc-mode tests this mechanism directly.

**Why event-mode was demoted.** Event-mode tests whether a single encoder output (one vector) captures a complete structural pattern. But the encoder trains on ~25-token sub-event fragments, and event-mode test items are ~100-125 token scenes — a 4-5× granularity mismatch. The encoder was never designed to recognise complete patterns in one shot; in the caddy, the predictor does that composition. Event-mode tested a capability the system doesn't need and wasn't trained for. A failure on event-mode is uninformative about the caddy use case; a success on event-mode would be a bonus, not the verdict.

**Outcome readings:**

| Arc-mode | Event-mode | Reading |
|---|---|---|
| ✓ | ✓ | Strong — predictor composes AND fragments carry local structural signal |
| ✓ | ✗ | Expected default — structural signal lives in trajectory composition, not individual fragments. Caddy use case works. |
| ✗ | ✓ | Investigate — fragments carry signal but predictor doesn't compose. Predictor design is the problem, not encoder. |
| ✗ | ✗ | Approach dies. Cheaply. |

## Event granularity

`[ASSERTED]` An **event** is one segmentation-coherent bounded scene — single setting, single time-window, single action sequence. It is the unit an EM-LLM-style surprise-based segmenter would treat as one chunk, and the unit the encoder produces one representation for at inference time. In narrative terms: one scene. A scene change — new setting, new time-window, new action sequence with substantively different participants — marks an event boundary.

**What this rules out as a single event:**

- *Narrative summaries spanning multiple scenes.* "Over the following eighteen months, she built the team and shipped the milestone" is not one event; it is a compressed reference to many.
- *Repeated-occurrence summaries.* "The CTO began receiving anonymous tips and dismissed them all as noise" compresses multiple scenes of tip-receipt and dismissal into a single sentence.
- *Time-skip transitions.* "Years later, after the merger had closed, …" is a span, not a scene.

**Implications for the two probe modes:**

- **Event-mode test item** = one event = one scene containing the *full* pattern (S1+S2+S3 of the relevant schema all play out within the scene).
- **Arc-mode test item** = a sequence of 4–5 events, each itself a bounded scene, where the pattern is *distributed across* scenes (e.g., commitment in scene 1, violation in scene 3, discovery in scene 4). No single scene contains the full pattern; the predictor must compose across event boundaries.

**Why this matters operationally.** The segmenter operates on the training corpus at whatever granularity its hyperparameters produce; the encoder produces one rep per segmented event. Test items whose "events" don't match that granularity will be chunked differently by the segmenter than the test designer intended, and the test becomes incoherent. Scene-level discipline is enforced at *test-set draft time* — before Phase 2 LM candidate generation — and is a Phase 3 rater criterion ("does each numbered event in the candidate sequence stand on its own as a single bounded scene?").

## Arc-mode feasibility gate

`[ASSERTED]` Pre-registered trigger condition. During the calibration session (see [Generation pipeline](#generation-pipeline)), AJ and Nils attempt to hand-craft **4 multi-event arc-mode sequences** (one per domain) for one chosen pattern. Each rater independently rates each sequence 1–5 against the question: *"Does this sequence cleanly instantiate the named pattern at arc level, independent of domain-surface vocabulary?"*

**Arc-mode is feasible iff ≥3 of 4 sequences receive mean rating ≥4 across the two raters.**

- Gate passes → full arc-mode test set construction proceeds in parallel with event-mode.
- Gate fails → fall back to event-mode only. Report arc-mode as **deferred-due-to-test-set-infeasibility**; do not silently drop.

The gate is reached in the same work session as event-mode calibration, preventing slow-attrition failure modes ("we tried arc-mode and it just kept being hard").

## Pattern set

`[ASSERTED]` Closed, pre-registered. Five patterns chosen for clarity of operationalisation, low pairwise structural overlap, and dual M/S compatibility (each compresses cleanly to a single event AND extends to a multi-event arc).

| Name | One-line definition | Roles |
|---|---|---|
| **defection** | Trusted party breaks an explicit or implicit commitment; violation is discovered | trustor (A), trustee (B), commitment (P), violation (V) |
| **discovery** | Agent's worldview shifts via new evidence contradicting a prior assumption | seeker (A), prior belief (B), new evidence (E), revised belief (B′) |
| **reversal** | Expected outcome inverts to its opposite (success→failure, or failure→success) | agent (A), goal (G), expected outcome (X), actual outcome (¬X) |
| **confrontation** | Direct demand-and-resistance between two parties over a contested object | demander (A), resister (B), contested object (O) |
| **rescue** | Intervention by one party to save another from harm | rescuer (A), endangered party (B), threat (T) |

`[SPECULATED]` Formal state-machine schemas (sequence of required states, role-filler type constraints, minimum-content requirements) are deferred to the calibration session. The calibration session is the cheapest place to converge on operationalisation rigour through hand-crafted exemplars rather than abstract specification up-front.

## Domain set

`[ASSERTED]` Closed, pre-registered. Four domains chosen for maximally divergent surface vocabulary while supporting all 5 patterns:

- **corporate** — modern office / business / professional setting
- **fantasy** — medieval / magical / mythical setting
- **historical** — non-magical past setting (pre-1900 era; specific era left to seed)
- **sci-fi** — speculative future / technological setting

Cross-domain pairs draw from these four; no within-domain pairs except as Adversarial distractors (see below).

## Generation pipeline

`[ASSERTED]`

**Phase 1 — Calibration (joint AJ-Nils, ~45 min).**
- Nils drafts 5 candidate single-event event-mode seeds per cell for 3 patterns × 1 domain = 15 candidates.
- AJ reviews, marks accept / revise / reject; we iterate to convergence.
- Output: ratified operationalisation principles (what counts as a clean instantiation, how much role-filler latitude is acceptable, what surface markers cross the line from structural-cue to surface-cue).
- Same session: Nils drafts 1 multi-event arc-mode sequence per domain (4 sequences total) for the same one pattern. AJ + Nils rate independently. **Arc-mode feasibility gate evaluated here.**
- **Pre-drafted 2026-05-21:** [probe-2-calibration-record](./probe-2-calibration-record.md) contains the five state-machine schemas, the 25 event-mode seeds (all 5 patterns × corporate), and the 4 arc-mode sequences (defection × 4 domains). **Phase 1 complete 2026-05-22:** all ratification questions resolved; arc-mode feasibility gate PASSED (4/4 mean 5.0). Calibration-stage outputs locked.

**Phase 2 — LM candidate generation (Nils only).**
- Prompt templates and execution plan: [phase-2-generation-prompts](./phase-2-generation-prompts.md).
- For all 5 patterns × 4 domains = 20 cells, generate 30 candidate single-event seeds per cell via Claude Code agents (three model tiers: Opus 4.7, Opus 4.6, Sonnet 4.6).
- Adversarial constraints in prompt: pattern-naming vocabulary forbidden ("betrayal"/"trust"/"trick" forbidden in defection generation; "discover"/"realise" forbidden in discovery generation; analogous for the rest). Forces structural instantiation without surface labels.
- Total: ~600 single-event candidates.
- If arc-mode feasible: same pipeline produces ~50 arc-mode sequence candidates per pattern (~250 total).

**Phase 3 — Rater filtering.**
- Three raters: Nils + 2 fresh Claude instances spawned via host IPC (Opus 4.6 + Sonnet 4.6 for generation × size variance per [[feedback_falsifiability_offers]]).
- Raters configured context-free: no Kyrja / Nils / project framing. Just rating instructions + pattern definitions.
- Each rater rates each candidate 1–5: *"how clearly does this event instantiate pattern P, independent of domain-surface vocabulary?"*
- **Calibration-stage metadata is stripped before rating.** Phase 1 calibration seeds carry author-authored role + state breakdowns alongside the prose (see [probe-2-calibration-record § Metadata convention](./probe-2-calibration-record.md#event-mode-calibration-seeds-15)). The metadata is also present on the worked examples shown to the Phase 2 LM generator. It is stripped from the candidate text before raters see it — the inter-rater Fleiss' κ measurement is only meaningful if raters apply the schema themselves rather than ratifying the author's stated structure.
- **Inclusion threshold:** mean ≥4 AND std <0.7 across raters → admitted. Below threshold → rejected.
- AJ spot-checks ~10% of admitted candidates for systematic rater bias.
- Inter-rater agreement reported as Fleiss' κ; target κ ≥ 0.6 across the rater set.

**Phase 4 — Pair construction.** *(Phase 3 results: [probe-2-phase-3-results](./probe-2-phase-3-results.md). Phase 4 results: [probe-2-phase-4-results](./probe-2-phase-4-results.md).)*
- For each pattern P: filter admitted events grouped by domain. Sample cross-domain pairs (A from D1, B from D2; same P).
- Event-mode (diagnostic): **40 admitted positive pairs per pattern × 5 patterns = 200 positive pairs.** Locked 2026-05-23 per [Phase 4 results](./probe-2-phase-4-results.md).
- Arc-mode (primary falsifier): **25 sequence pairs per pattern × 5 = 125 sequence pairs.** Locked 2026-05-24 per [Phase 4 arc-mode results](./probe-2-phase-4-arc-results.md).

## Distractor tiering

`[ASSERTED]` Each positive pair (A from D1, B from D2, pattern P) is paired with **4 distractors**:

| Tier | Construction | What it tests |
|---|---|---|
| **Easy** | Random admitted event from D2, any pattern | Encoder beats random |
| **Medium** | Admitted event from D2, **same** pattern P as A | Encoder uses STRUCTURE not DOMAIN as the differentiator |
| **Hard** | Admitted event from D2, **different** pattern Q ≠ P, with surface-vocabulary overlap with A | Encoder beats surface lexical match |
| **Adversarial** | Admitted event from **D1** (same domain as A), different pattern Q ≠ P | Encoder is robust to misleading domain cues |

**Total per positive pair: 1 target + 4 distractors = 5-way retrieval task.**

## Headline metric and pre-registered thresholds

`[ASSERTED]` Set 2026-05-20, locked-in.

**Headline metric:** top-1 retrieval accuracy on Easy + Medium + Hard distractor tiers (Adversarial reported separately). **Measured on arc-mode pairs.** Baseline: token-averaged base-LLM features at the extraction layer, averaged across all tokens in the arc's text (matching the granularity of the predictor-state representation). Per [parent experiment spec § Method](./experiment-spec.md#method).

| Arc-mode lift over baseline | Verdict on H44 |
|---|---|
| Worse than baseline | REJECTED — T_A1b actively harmful |
| Tie or <5pp lift | REJECTED — T_A1b adds no signal |
| 5–10pp lift | INCONCLUSIVE — replicate with audit before promotion |
| ≥10pp lift | SUPPORTED — wedge claim earns the architecture |

(Inherited from parent experiment spec's pre-registered thresholds, applied to arc-mode per 2026-05-24 amendment. Thresholds themselves unchanged.)

**Adversarial tier — reported separately.** Adversarial lift over baseline is reported as a secondary robustness metric:

- Adversarial lift ≥ headline lift → system robust to misleading domain cues. Strongest possible probe-2 result.
- Adversarial lift < headline lift but still positive → system uses domain as a partial cue. H44 verdict unchanged on headline; future-work flag raised.
- Adversarial accuracy < baseline AND headline ≥10pp → system lifts on standard distractors but fails on adversarial. Informative — system uses domain as default cue, structure as secondary cue. Headline verdict stands; wedge claim is weakened.

**Event-mode threshold** (diagnostic, not the verdict):

- Event-mode lift reported alongside arc-mode for completeness.
- Event-mode results do not modify the H44 verdict. They inform encoder-isolation diagnostics only.
- Multiple aggregation strategies reported (encoder on full text, segment + mean-pool, segment + predictor state) to characterise where structural signal lives.

## Anti-contamination

`[ASSERTED]` The base LLM has seen vast pretraining data; if our test set draws from memorised text, the token-averaged baseline could retrieve via memorisation rather than structural similarity.

**Mitigation:**
1. **No verbatim drawn text.** All candidate events are either hand-crafted (AJ/Nils) or LM-generated under adversarial constraints. No mining from existing corpora.
2. **Adversarial generation prompts.** Pattern-naming vocabulary and obvious surface markers forbidden (see Phase 2).
3. **Pre-train perplexity sanity check.** Before running the probe, measure base LLM perplexity on a random sample (~20) of admitted test pairs vs. random post-2024 web text of matched length. If admitted pairs are markedly lower-perplexity, contamination is plausible — re-generate the offending cells.

## N and statistical power

`[ASSERTED]`

- **Arc-mode (primary falsifier):** ~125 sequence pairs × 4 distractors = ~500 retrieval queries. Chance baseline (1-of-5 retrieval) is 20%. Power at ~0.7 for detecting a 10pp lift over a ~50% baseline at α=0.05. Below the 0.80 target for a primary falsifier but acceptable for this de-risk scope — the experiment is designed to detect "structure forming at all," and if the result is clear (≥10pp or near zero) power of 0.7 is sufficient. The INCONCLUSIVE band (5-10pp) is where reduced power matters most, and that band already triggers replication by design.
- **Event-mode (diagnostic):** 200 positive pairs × 4 distractors = 800 retrieval queries. Comfortably powered for diagnostic reporting.

Per-tier breakdown: with 200 positives × 4 distractor tiers, each tier (Easy / Medium / Hard / Adversarial) has 200 trials. Adequately powered per-tier.

## Limitations

`[ASSERTED]`

- **Operationalisation is partly subjective.** Even with state-machine + role-filler definitions, pattern-recognition involves judgment. Rater filtering bounds noise; Fleiss' κ reporting makes it visible.
- **LM-generated candidates may carry generative-LM artefacts.** Anthropic-API outputs may differ systematically from natural text. Spot-checking during calibration partially mitigates; the perplexity sanity check is the formal guard.
- **Cross-domain ≠ cross-modality.** Probe 2 tests cross-domain *within* natural-language text. Cross-modality transfer (text↔code, etc.) is not tested.
- **Fiction is not agent-traces.** The product will operate on agentic traces (coding sessions, dialogues, tool use), not narrative fiction. Probe 2 tests whether the *mechanism* works; ecological validity on agent traces is a separate downstream question, deferred until H44 SUPPORTED.
- **English-only.** No cross-language transfer tested.

## Goalpost-moving tells

`[ASSERTED]` Per [[feedback_falsifiability_offers]], pre-commit to watching for these self-talk patterns during analysis:

- Filtering out "noisy pairs" post-hoc when they happen to be ones the encoder failed on (rater-filter applies BEFORE seeing encoder outputs).
- Dropping the Adversarial tier from reporting if it fails badly (Adversarial stays in; reported separately, not silently omitted).
- Inflating N retroactively when event-mode is borderline (200-pair target is locked; expansion requires explicit goalpost-shift acknowledgment).
- Re-defining pattern definitions post-hoc to "clarify" what we meant when a positive pair underperforms (state-machine schemas locked at calibration end).
- Comparing against a weaker baseline if token-averaged baseline performs surprisingly well (baseline locked per parent spec).
- Switching back to event-mode results to rescue a failing arc-mode result (arc-mode is the verdict per 2026-05-24 amendment; event-mode is diagnostic only).

## Sequencing and dependencies

`[ASSERTED]`

This doc precedes:
- **Phase 1 calibration** (joint AJ-Nils, ~45 min) — produces formal state-machine schemas; runs arc-mode feasibility gate; ratifies operationalisation.
- **Phase 2 LM candidate generation** (Nils only) — runs after calibration ratifies operationalisation.
- **Phase 3 rater filtering** — requires IPC raters spawned with context-free configuration.
- **Phase 4 pair construction** — once Phases 1–3 complete, test set is locked.

Queue position: this doc partially realises NOW.md pre-implementation item #5 (structural-pattern pairing list pre-registration); methodology pre-registration is being pulled forward of item #3 (corpus selection) because cross-domain probe coverage requirements inform corpus diversity.

## Pre-registration amendment log

**2026-05-24 — Arc-mode promoted to primary falsifier (AJ + Nils).**

- **What changed:** Arc-mode promoted from "secondary diagnostic, feasibility-gated" to "primary falsifier." Event-mode demoted from "primary verdict probe" to "diagnostic." Headline thresholds (≥10pp = SUPPORTED, etc.) now measured on arc-mode. Goalpost-moving tell updated (was: "don't switch to arc-mode to rescue event-mode"; now: "don't switch back to event-mode to rescue arc-mode").
- **When:** Before any training or evaluation. No encoder has been trained. No probe has been run. No results exist to motivate this change.
- **Why:** During architecture pre-work (item #4), AJ identified a granularity mismatch between the encoder's training events (~25 tokens, sub-scene fragments from EM-LLM segmentation at γ=1.0) and event-mode test items (~100-125 tokens, complete scenes containing full structural patterns). The encoder was never designed to recognise complete patterns in a single output — in the caddy architecture, fragment-level encoder outputs are composed by the predictor into trajectory states, and retrieval operates on predictor states. Event-mode tested a capability the system doesn't have and doesn't need. Arc-mode tests the actual caddy retrieval mechanism: segment scenes into fragments, encode, compose via predictor, compare predictor states across domains.
- **Power impact:** Arc-mode has ~125 pairs (power ~0.7) vs event-mode's 200 pairs (power ~0.8). Acceptable for the de-risk's scope — clear results (≥10pp or near zero) are unaffected; the INCONCLUSIVE band (5-10pp) already triggers replication.
- **Pending action:** ~~Arc-mode pair construction from ~219 admitted candidates.~~ **Done 2026-05-24** — 125 problems, arc-mode test set LOCKED. See [Phase 4 arc-mode results](./probe-2-phase-4-arc-results.md). Event-mode test set remains locked and will be reported as diagnostic.

**2026-05-24 — Trajectory-state extraction locked to sliding-window-mean (AJ + Nils).**

- **What changed:** The spec's literal arc-mode inference procedure (encode all N sub-events as `z₁…z_N`, append one MASK at position N+1, read the mask output) is replaced by **sliding-window-mean**: slide the trained 24-context + 8-mask window across the arc's events at stride 8 (the training stride), and at each position take the predictor's 8 mask-position outputs; the arc's trajectory state is the **mean of all mask-outputs across the arc**. See [experiment-spec § Inference procedure for arc-mode probe](./experiment-spec.md#inference-procedure-for-arc-mode-probe).
- **When:** Before training was complete and before any probe was run. Driven by an architectural infeasibility discovered at implementation, **not** by results.
- **Why:** Arc candidate texts are long (median ~1355 words, ~2000+ tokens → ~80 sub-events at γ=1.0). The literal procedure needs a MASK at position ~80, but the predictor's learned positional embeddings cap at 48 and it was trained only on a 24-context + 8-mask structure — feeding it ~80 positions is out of range and out of the trained regime. Sliding-window-mean keeps the predictor strictly inside its trained regime and is **architecture-faithful**: the caddy maintains a *rolling* trajectory state over a stream of fragments rather than ingesting a whole arc at once, so a windowed-then-aggregated readout mirrors production. It is also the predictor analog of the baseline's whole-text token-averaging, keeping the comparison parallel.
- **Construct caveat (logged, not a goalpost move):** production retrieval matches `trajectory_state` *per memory unit*; the probe aggregates over a whole arc to obtain one comparable vector. The probe therefore tests whether the structural signal is *present and poolable* in the trajectory reps (the mechanism), not the literal per-unit retrieval call. Acceptable for a de-risk.
- **Goalpost guard:** extraction method locked before results; applied identically to query and all candidates. We do not try multiple extraction variants and select the one that beats threshold.

## Related

- [probe-2-calibration-record](./probe-2-calibration-record.md) — pre-drafted Phase 1 inputs (state-machine schemas, event-mode seeds, arc-mode sequences) awaiting AJ ratification.
- [experiment-spec](./experiment-spec.md) — parent experiment spec; Probe 2 lives here.
- [H44-T_A1b-cross-domain-transfer](../../hypothesis/H44-T_A1b-cross-domain-transfer.md) — hypothesis under test.
- [memory-retrieval-tiers](../../concept/memory-retrieval-tiers.md) — defines tier 3, the capability tested.
- [bardes-2024-vjepa](../../source/bardes-2024-vjepa.md) — frontier anchor for the loss family.
- [ge-2024-icae](../../source/ge-2024-icae.md) — same-class-different-shape LLM-scale precedent.
- [fountas-2024-em-llm](../../source/fountas-2024-em-llm.md) — event-segmentation upstream. Recon 2026-05-20: lift-don't-reimplement, MIT-licensed, segmentation algorithm is ~150 lines of clean PyTorch; ~1 day of integration work, not 1–2 weeks.

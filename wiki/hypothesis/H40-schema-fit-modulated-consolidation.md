---
type: hypothesis
name: H40 — Schema-fit-modulated consolidation rate beats fixed-rate consolidation on agent-memory utility
status: PROPOSED
last_ingested: 2026-05-20
sources: [../source/tse-et-al-2007-schemas.md, ../source/mcclelland-mcnaughton-oreilly-1995-cls.md, ../source/redondo-morris-2011-stc.md, ../concept/mechanism-gap-matrix.md]
epistemic_tags: [speculated]
tags: [schema-fit, consolidation-rate, admission-control, ai-translation, cog-sci-derived, load-bearing]
---

> **Status (2026-05-20):** H40 is **active load-bearing** alongside [H44](./H44-T_A1b-cross-domain-transfer.md) per [caddy-as-research-program](../decision/caddy-as-research-program.md). The 2026-05-19 scope-status: "v2-research-target" was MVP-product-shaped and was REVERSED 2026-05-20 when the caddy was reframed as a research program. The hypothesis is one of two falsifiable bets that decide the architecture's scientific footing; the [m17-jepa-reconciliation § Resolution](../open-question/m17-jepa-reconciliation.md) established that K2+T_A3 (H40's mechanism) is scientifically distinct from T_A1b's EMA-target mechanism — CLS theory: distinct timescales, distinct jobs. Ordering vs. H44 is decided by the forthcoming stack-rank exercise. The isolation experiment design preserved below under § Isolation experiment design is the protocol when H40 is dequeued for execution.

> **Mechanism anchor (added 2026-05-17):** The M15 walk produced a molecular mechanism for H40 via behavioural tagging ([Redondo & Morris 2011 STC](../source/redondo-morris-2011-stc.md), Wang & Morris 2010). Schema-fit operationalises as **PRP (plasticity-related-protein) availability modulated by novelty / dopamine / reward signals.** The 5-min "novelty rescue" effect demonstrates that schema-fit-modulated consolidation is mechanistically the synaptic-tagging machinery applied at behavioural level. H40 should now be read as a specific instantiation of the upstream [salience-signal](../open-question/salience-signal.md) question — schema-fit is one candidate signal in the multi-signal convergence biology uses.

## Claim

**Agent memory systems that detect per-candidate "schema-fit"** (consistency of new information with the system's existing knowledge — both pretrained-LLM and accumulated user-state) **and modulate consolidation rate accordingly** (high-fit → fast consolidation with minimal evidence; low-fit → slow consolidation requiring more evidence; no-fit → episodic-only storage without weight-level commitment) **achieve higher agent-memory utility than fixed-rate consolidation systems under matched compute budgets.**

The biological precedent is the schema-mediated rapid-consolidation finding ([Tse et al. 2007](../source/tse-et-al-2007-schemas.md)): rats consolidate new flavor-place pairs in 48 hours when a schema exists, vs. weeks-to-months without — a ~50-100× speedup. Translation to AI is `[SPECULATED]` until empirically tested.

## What would falsify it

A controlled benchmark comparison where:

- **System A (baseline)** implements fixed-rate consolidation: every memory item that passes a uniform admission threshold gets consolidated via the same training procedure (e.g., LoRA fine-tuning batch at a fixed cadence, or full FT, or scheduled distillation — pick a reasonable consolidation pipeline).
- **System B (schema-modulated)** implements per-candidate schema-fit detection (any reasonable operational definition — see open sub-questions) and modulates consolidation. Three tiers: (i) high-fit → fast / light-evidence consolidation, (ii) low-fit → slow / multi-evidence consolidation, (iii) no-fit → episodic-only without weight update.
- **Workload**: cross-session agent tasks measuring (a) retention of user-specific info, (b) generalization to held-out scenarios, (c) avoidance of harmful integration of mis-fitting info, (d) compute consumed.
- **Compute matched**: both systems use the same total consolidation compute budget; they differ only in how that compute is allocated.

H40 is **REJECTED** if:
- System B shows no significant utility advantage on (a)-(c) under matched compute, OR
- System B's advantage exists only under a specific schema-fit operationalization that doesn't generalize, OR
- System B's compute overhead from schema-fit detection itself outweighs the consolidation savings.

H40 is **SUPPORTED** (not proven) if:
- Significant advantage on retention + generalization at matched compute, across multiple workloads, AND
- Advantage holds across multiple schema-fit operationalizations (so the win comes from the *rate-modulation architecture*, not from a clever fit metric).

H40 is **partially supported** if the win is restricted to specific workload types (e.g., personal-assistant memory but not technical-task memory). The scope of the win then becomes the result.

## Evidence for

`[MEASURED]` ([Tse et al. 2007](../source/tse-et-al-2007-schemas.md)) — **Construct validity:** the experiment measures cued recall of new flavor-place associations 48h after single-trial training in rats with established schemas (~30 days prior training on consistent flavor-place mappings). Memory transfers from hippocampus-dependent to hippocampus-independent in 48h with schema present, vs. typical multi-week consolidation timelines without. The 50-100× speedup factor is measured against the canonical [McClelland 1995](../source/mcclelland-mcnaughton-oreilly-1995-cls.md) consolidation timeline.

`[MEASURED]` (Tse 2007 Experiment 4, causal control): Animals trained concurrently in *consistent-schema* and *inconsistent-schema* contexts. New pairs introduced in both contexts; 24-hour probe shows learning only in consistent context. **The schema activation is causally necessary, not just correlated.** Construct validity: the inconsistent-schema control rules out context familiarity, motivation, and rule-learning confounds.

`[ASSERTED]` Conceptual gap ([mechanism-gap-matrix](../concept/mechanism-gap-matrix.md) row M05): no current agent-memory system implements per-candidate rate modulation based on consistency with existing knowledge. Fine-tuning rates are global; admission decisions are binary.

`[SPECULATED]` Mechanistic plausibility: schema-fit detection is operationally tractable. Candidate operationalizations include (a) embedding similarity between new memory and pretrained LLM's existing-knowledge representation, (b) perplexity of the new info under the current model (high perplexity = low fit), (c) consistency score against accumulated user-state representation. Each is implementable on a frozen base LLM.

`[ASSERTED]` Synergy with existing wiki concepts: [admission-control](../concept/admission-control.md) already names "schema-fit as an admission signal" (added during the 2026-05-14 propagation pass). H40 extends admission-control from a binary (admit/reject) to a three-tier rate-modulated policy.

## Evidence against

`[SPECULATED]` Anticipated objections:

- **"This is just continual learning with a learned rate schedule."** Distinction: continual learning rates are typically learned globally (e.g., per-task curriculum) or via meta-learning. H40 proposes a *per-candidate* rate signal derived from schema-fit. The architecture is different even if the math could be reduced.
- **"Schema-fit detection is itself expensive."** Acknowledged. The falsifier explicitly accounts for this via the matched-compute constraint. If schema-fit detection consumes more compute than it saves, H40 is REJECTED.
- **"Modern transformers already do this via attention weighting."** Distinction: attention modulates which existing knowledge to retrieve at inference; H40 modulates *consolidation rate* — what gets written to weights and how aggressively. Different operation, different timing.
- **"Tse 2007's biological finding may not translate."** Acknowledged risk. Cog-sci → AI translation has a poor track record at the mechanism level. The falsifier tests the AI claim empirically, independent of the biological analogy.

## Open sub-questions

- **What's the right operational definition of schema-fit?** Multiple candidates: embedding similarity, perplexity, classifier confidence, consistency with a user-state representation. Each tests differently. Sub-question candidate for promotion to an open-question page.
- **High-fit vs low-fit threshold?** The three-tier policy needs cut-points. Should they be learned per-domain, hand-tuned, or adaptive? Independent design question.
- **How does schema-fit interact with admission control?** [Admission-control](../concept/admission-control.md) currently treats admission as binary. H40 implies admission is part of a tier-policy spectrum. The unification needs design work.
- **Does schema-fit need to be measured at write-time, retrieval-time, or both?** Biology measures at encoding (schema activation during learning). AI could measure at write-time (simpler) or at retrieval/replay-time (potentially more accurate, more expensive).
- **What's the right utility metric?** Retention alone is insufficient (favors high-fit, since high-fit info is more retrievable anyway). Need a metric that captures both retention and *correctness* — including correctness in the face of mis-fitting info (does the system reject incorrect "fits" appropriately?).
- **Does schema-fit-modulated consolidation interact with silent-state primitives?** [H39](./H39-silent-state-primitives.md) and H40 are siblings from the same sweep. A combined architecture could: high-fit → fast consolidation; low-fit → silent state with possible reactivation; no-fit → episodic-only.
- **Construct validity of "schema" in AI context.** In Tse 2007, the schema is operationally defined by what the rats learned (the flavor-place mapping). The AI analogue (pretrained LLM weights + user-state) is much broader and may not have the same structural properties.

## Origin

`[ASSERTED]` Surfaced 2026-05-14 during the cog-sci primary-source sweep ([log](../log.md)), specifically the verbatim read of [Tse et al. 2007](../source/tse-et-al-2007-schemas.md). MORNING.md flagged schema-fit rate modulation as the single most directly Kyrja-translatable finding from the sweep. AJ approved promotion to a hypothesis on 2026-05-15.

## Isolation experiment design

`[SPECULATED — sketched 2026-05-19; protocol for execution when H40 is dequeued]`

The 2026-05-19 AJ-Nils session designed an isolation experiment for K2+T_A3 analogous to the [T_A1b isolation de-risk](../experiment/2026-05-18-T_A1b-isolation-derisk/README.md). Subject to revision at dequeue time — particularly if T_A1b results inform schema-fit signal choice or the experiment shape.

### Path (decision committed 2026-05-19)

**Path B — K2 testable independent of T_A1b via proxy schema-fit signal.** Use any reasonable predictor's prediction error as the fit signal; the architecture of K2 (three-tier consolidation policy + drift) is what's being tested, not the specific fit signal. Mirrors H42's testability on bolt-on shapes, and matches H40's existing falsifier clause ("the win must come from the rate-modulation architecture, not from a clever fit metric"). Reasoning: K2 design in parallel with T_A1b (rather than strictly after) avoids waste if T_A1b fails — K2 architecture is also valuable to a bolt-on-with-cog-sci direction.

### Two versions, both tested

**Version A — static reference.** Schema-fit computed against a fixed model (small predictor trained once on held-out corpus, then frozen). What lands in cold tier never affects the score on the next arrival. Tests the *selection* mechanism in isolation.

**Version B — dynamic reference (the real T_A3 test).** Schema-fit computed against something that updates from what's been consolidated — running average of cold-tier representations, or an incrementally-retrained predictor. What's in cold tier *does* affect future scoring. Tests the *drift feedback* property that T_A3 actually claims.

Both versions run side by side. Pre-registered outcomes:
- **A beats baselines but B fails:** K2 is real; T_A3 drift feedback is harmful. Pivot to K2-with-frozen-reference.
- **Neither beats baselines:** K2+T_A3 architecture REJECTED. Engineered baselines (FIFO/LRU/TTL) win.
- **A beats baselines, B beats A:** full K2+T_A3 supported. Hypothesis moves from PROPOSED to SUPPORTED.
- **B beats baselines but A doesn't:** suspicious — feedback doing more than selection. Investigate before promoting.

### Decisions committed 2026-05-19

**Decision 3 — matched memory budget**, not matched compute. At isolation scale there's no expensive consolidation operation (no FT, no distillation); the policy decisions are bookkeeping over tier assignments. Memory budget is the natural scarce resource; compute matching becomes artificial. Compute matching applies at the full-caddy ablation scale when consolidation involves real training overhead.

**Decision 4 — pre-registered threshold via dev/test split.** Standard ML hygiene: build a small dev set, run baselines there, set the threshold as `dev-best + 10pp on the test set`, lock in writing, then run K2 *and* baselines on a previously-untouched test set. The "discipline anti-cheat": dev set is small, used once for calibration, never re-touched for evaluation. Avoids the blind-10pp failure mode (task that caps at 95% has no headroom) without giving up falsifiability.

### Setup

- Stream of events from a corpus (use the same coding-trajectory + narrative corpora as the T_A1b de-risk per AJ 2026-05-19)
- Hot tier (admits everything, capped at size H)
- Cold tier (consolidated, capped at size C; C << total events)
- Schema-fit signal: proxy = prediction error from a small predictor (frozen for Version A, updating for Version B)
- Consolidation policies compared:
  - A1: FIFO eviction
  - A2: random eviction
  - A3: fixed-rate eviction (every k events drop k oldest)
  - B (K2): three-tier policy per H40 § Claim — high-fit → fast cold admission, low-fit → retain in hot, no-fit → episodic-only with longer retention
- All policies match on total memory footprint (H + C)

### Probes

1. **Memory-budget retention probe.** At fixed budget, which policy retains the "informative" events? Informative = events whose retrievability improves downstream-task performance.
2. **Downstream task probe** (primary falsifier). Held-out query set whose answers are scattered across the stream; which policy's retained memory enables higher accuracy? Pre-registered threshold: K2 beats best baseline by `dev-best + 10pp` on test set.
3. **Fit-signal generalization probe.** Run K2 with two or three different fit-signal operationalizations (proxy predictor, embedding similarity, perplexity). H40 requires the win to be robust across operationalizations.
4. **Stability probe (Version B only).** Cold-tier diversity over time. If diversity collapses, the feedback loop is eating itself.
5. **Ordering-sensitivity probe (Version B only).** Run the same stream in three or four different orderings. High variance across final cold-tier compositions = the system is dominated by initialization noise rather than statistical structure.

### Failure modes to watch for in Version B

- **Entrenchment / mode collapse.** Cold tier converges to one dominant pattern type.
- **Catastrophic narrowing.** Genuinely useful early patterns get squeezed out by later majority patterns.
- **Initialization sensitivity.** Final state depends on first-N items more than on actual stream structure.

These are well-known failure modes in clustering / online-learning literature; H40 v2 specifically probes them.

## Related

- [mechanism-gap-matrix](../concept/mechanism-gap-matrix.md) — M05 is the row this hypothesis derives from.
- [Tse et al. 2007 source](../source/tse-et-al-2007-schemas.md) — primary biological evidence.
- [McClelland 1995 source](../source/mcclelland-mcnaughton-oreilly-1995-cls.md) — the consolidation framework whose `C` rate is refined by schema-fit.
- [admission-control](../concept/admission-control.md) — natural home for the schema-fit signal at write-time; the page already references Tse 2007 as the biological precedent.
- [active-stages-framework](../concept/active-stages-framework.md) — the *consolidation* active stage now has a biologically-precedented training signal (schema-fit, in addition to contrastive same-fact-merge).
- [consolidation-channel](../concept/consolidation-channel.md) — the (depth, frequency) design space should be extended to (depth, frequency, *fit-modulated rate*) per H40.
- [H39 — silent-state primitives](./H39-silent-state-primitives.md) — sibling hypothesis from same sweep; potentially combinable architecture.
- [H38 — rationale-trace-memory](./H38-rationale-trace-memory.md) — distant sibling; both are cog-sci-derived but different layers.
- [rl-target-encoding-vs-consolidation](../open-question/rl-target-encoding-vs-consolidation.md) — H40 implies the RL budget should split across the three tiers, not be applied uniformly to consolidation.
- [m17-jepa-reconciliation](../open-question/m17-jepa-reconciliation.md) — RESOLVED 2026-05-19 with resolution (c): K2+T_A3 stays scientifically distinct from T_A1b's EMA target encoder (different timescales, different inputs, different outputs, different reasons). Scientific distinctness preserved.
- [caddy-as-research-program](../decision/caddy-as-research-program.md) — 2026-05-20 framing decision: caddy is a research program; H40 is active load-bearing alongside H44.
- [k2-ta3-deferred-to-v2](../decision/k2-ta3-deferred-to-v2.md) — REVERSED 2026-05-20. Historical record of the 2026-05-19 MVP-product-shaped deferral.

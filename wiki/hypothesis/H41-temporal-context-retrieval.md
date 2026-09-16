---
type: hypothesis
name: H41 — A drifting context vector updated by retrieval beats timestamp-only retrieval on cross-session continuity
status: PROPOSED
last_ingested: 2026-05-18
sources: [../source/howard-kahana-2002-tcm.md, ../concept/mechanism-gap-matrix.md]
epistemic_tags: [speculated]
tags: [temporal-context, retrieval-cue, cross-session, ai-translation, cog-sci-derived]
---

## Claim

**Agent memory systems that maintain a persistent context vector — distinct from item content, drifting with agent activity, and updated by retrieved item content via a preexperimental-vs-newly-learned split** ([Howard & Kahana 2002 eq 6, eq 8](../source/howard-kahana-2002-tcm.md)) — **and use that vector as a retrieval cue alongside content similarity, will outperform timestamp-only and content-only retrieval on cross-session continuity tasks at matched compute.**

The translation candidate is: preexperimental context ≈ user-lifetime context for an item across all encounters; newly-learned context ≈ session-local context for the item just now. The architecture closes a feedback loop at the *retrieval cue* level rather than at the item-content level.

## What would falsify it

A two-part empirical test:

**Part 1 — matched-compute retrieval benchmark.** Compare three retrieval modes on a cross-session continuity workload:

- **Mode A (baseline):** content-only retrieval (vector similarity over item embeddings).
- **Mode B (recency baseline):** content + timestamp-based recency weighting (the current state of the field).
- **Mode C (TCM-flavored):** content + temporal-context-vector similarity, with the vector maintained and updated per the [eq-6 evolution rule](../source/howard-kahana-2002-tcm.md) (or a defensible LLM-adapted version, see open sub-questions).

Matched-compute: all three modes use the same total retrieval budget. Workload: agent tasks requiring information continuity across sessions, where the *relevant* information is co-temporal-with but not necessarily content-similar-to the current query (e.g., "what was the second thing we discussed in last Tuesday's session, after the schema discussion").

**Part 2 — Falkenberg-style mechanistic signature.** Reintroduce a specific cross-session perturbation (e.g., the same kind of distractor task) between sessions. Measure retrieval quality on items studied *before* that perturbation. TCM-style content-driven context predicts the perturbation **reinstates the prior context** and *improves* retrieval of pre-perturbation items. Clock/timestamp-based mechanisms predict no effect.

H41 is **REJECTED** if:

- Mode C shows no significant advantage over Modes A and B at matched compute on the continuity workload, OR
- The Falkenberg signature does not appear (no boost from context-restoring perturbation), OR
- Mode C's advantage exists only under a single operationalization of the context vector that doesn't generalize.

H41 is **SUPPORTED** (not proven) if:

- Mode C significantly outperforms both A and B at matched compute, AND
- The Falkenberg signature appears with the predicted direction, AND
- The advantage holds across multiple operationalizations of "context" (so the win comes from the *architectural primitive*, not from a clever vector definition).

H41 is **partially supported** if Mode C wins on certain workload types (e.g., topic-drift sessions) but not others (e.g., topically-coherent sessions). The scope of the win then becomes the result.

**Construct-validity note on the benchmark:** The cross-session continuity workload must specifically measure retrieval of *contextually-relevant-but-content-dissimilar* items, not just topically-similar items. Otherwise content-only retrieval (Mode A) looks artificially competitive. The metric should be retrieval precision/recall for items studied near a referenced past item, *not* retrieval of any item containing query tokens. Construct validity also requires that "temporal context" in Mode C be operationalized in a way that is **not** a thin wrapper around timestamp — otherwise the comparison collapses into Mode B.

## Evidence for

`[ASSERTED]` ([Howard & Kahana 2002](../source/howard-kahana-2002-tcm.md)) — TCM provides a mathematically specified, parameter-parsimonious model where asymmetric retrieval falls out of the preexperimental/newly-learned split (eq 8, Fig 6) without a dedicated asymmetry parameter. The architectural elegance is meaningful even when the quantitative fits are mixed.

`[MEASURED]` ([Howard & Kahana 2002 §4](../source/howard-kahana-2002-tcm.md)) — TCM fits human free-recall data on recency (Fig 7) and lag-recency CRP (Fig 8) across immediate, delayed, and continuous-distractor conditions. **Construct validity:** the χ² values exceed standard goodness-of-fit thresholds for several conditions (χ²(8)=57.7 for delayed recency, χ²(5)=103 for delayed forward CRP), so TCM captures qualitative pattern, not quantitative fit. Cite as principled-architectural-account evidence, not "model proven."

`[ASSERTED]` ([mechanism-gap-matrix](../concept/mechanism-gap-matrix.md) row M13) — no current agent-memory system implements a maintained, retrieval-updated context vector as a first-class retrieval primitive. Mem0, Letta, Cognee, Zep, EvoSC, Cartridges, Hope — all use content similarity (sometimes with scalar recency weighting); none maintain a persistent context vector that updates on retrieval.

`[ASSERTED]` Architectural connection to transformer attention: TCM's eq 14 softmax retrieval rule is mathematically identical to attention. The TCM-novel content is the cue-evolution rule (eq 6) and item-specific unlearning (eq 12). This makes the LLM-side translation tractable — the retrieval primitive composes with existing attention, not against it.

`[SPECULATED]` Mechanistic plausibility: the TCM update rule is computationally cheap (`O(|F|·|T|)` per step). At reasonable dimensions (|F|=embedding-dim ~1024, |T|=context-dim ~64-128), sub-millisecond per update. Implementable on a frozen base LLM as a maintained soft-state side-channel.

`[SPECULATED]` Synergy with [cross-session-continuity](../open-question/cross-session-continuity.md): "what was I doing last week on this project" maps cleanly onto context-similarity retrieval rather than keyword match. The forward-recall asymmetry is *exactly* the bias you want for continuity work — after recalling a past meeting, preferentially surface what came *after*.

## Evidence against

`[SPECULATED]` Anticipated objections:

- **"LLM embeddings are not orthonormal — TCM's math may not translate."** Real concern. TCM's derivations assume orthonormal `f_i`. Modern LLM embeddings are anisotropic (see `reference_embedding_anisotropy` in project memory). The eq-7 normalization and eq-12 unlearning rule both assume specific F-geometry. Re-derivation under anisotropic representations is a prerequisite to implementation.
- **"Modern LLM agents already have implicit context via KV cache."** Within-session, yes — KV cache *is* a kind of maintained context. But it does not persist across sessions and is not updated by retrieval. The cross-session and retrieval-feedback aspects are the load-bearing novelty.
- **"TCM's quantitative fits are mixed."** Acknowledged ([H&K 2002 §4](../source/howard-kahana-2002-tcm.md)). The cog-sci community accepted TCM despite weak fits because of its architectural elegance and parameter parsimony. This is a different epistemic standard than ML benchmark-driven adoption. We may need to translate not the specific eq-6 form but the general primitive (drifting context vector + retrieval-driven updates).
- **"This is just RAG with a learned temporal index."** Distinction: RAG with a temporal index uses *timestamps as filters or scalar weights*. H41 uses a *vector* primitive where two memories can be cued by each other via context similarity even when their content is unrelated. Different operation.
- **"TCM is a free-recall model; agent memory is not free recall."** Acknowledged. We are translating the *primitive* (retrieval-updated context vector), not the *task* (word-list recall). The translation is `[SPECULATED]` and the falsifier tests it in an agent setting.
- **"The Falkenberg-1972 signature may not appear in an agent setting."** This is a real failure mode. If it doesn't appear, H41 is REJECTED on Part 2 of the falsifier — but the architectural primitive (maintained context vector with retrieval updates) might still be useful for reasons that aren't captured by TCM. We would then need to distinguish "TCM's mechanism doesn't translate" from "TCM-flavored context vectors are useful for non-TCM reasons."

## Open sub-questions

- **What is the operational definition of "context" in an LLM-agent setting?** Candidates: (a) a separately-maintained soft-prompt vector updated per turn, (b) a running mean of retrieved-item embeddings with TCM-style decay, (c) a recurrent state vector trained jointly with the agent, (d) an LLM-summary-text representation updated turn-by-turn. Each has different cost and different fit to the eq-6 mechanism.
- **What is the M^TF reset rule across sessions?** TCM assumes M^TF is reset at list onset. For an agent system: reset per session? per topic shift? never? The choice defines the episodic/semantic boundary.
- **What is the LLM analogue of "preexperimental context"?** Candidates: (a) pretrained-LLM knowledge representation for the item, (b) prior-session context state for the same item, (c) accumulated user-lifetime context. Each maps differently to the asymmetry mechanism.
- **Does orthonormality matter?** TCM's derivations assume orthonormal f_i. Re-derivation under anisotropic LLM embeddings: does asymmetry still fall out of the preexp/newly-learned split, or does the asymmetry direction get scrambled?
- **Is item-specific unlearning (eq 12) load-bearing for agent applications, or a list-length artifact?** Agent memories may not need bounded retrieval the way repeated word-list items do. Could be safely dropped, or could be load-bearing for repeated-topic stability.
- **How does the context vector interact with consolidation?** TCM is read-side; [consolidation-channel](../concept/consolidation-channel.md) is write-side. Does the context vector persist across consolidation events? Get re-derived? Influence what gets consolidated?
- **Empirical signature design.** Falkenberg 1972 was a specific paradigm (repeating a distractor task). The agent-setting equivalent needs design work — what's the cross-session perturbation? Same task type? Same topic? Same time-of-day?

## Origin

`[ASSERTED]` Surfaced 2026-05-14 during the path-decision-diligence pivot. After the cog-sci primary-source sweep produced H39 + H40 (silent-engrams, schema-fit consolidation), AJ asked whether reading the three remaining queued papers (Schaul 2016 PER, Frey & Morris 1997 synaptic tagging, Howard & Kahana 2002 TCM) was worth the cost. Nils's assessment: Schaul and Frey & Morris were implementation-detail; TCM was potentially architecture-shifting because no current agent-memory system has the temporal-context-vector primitive. AJ approved the mini-read; mini-read surfaced TCM as a real primitive worth tracking; AJ approved full read; full read confirmed the primitive holds even after honest accounting of TCM's weak quantitative fits. H41 was promoted 2026-05-14 during the wiki-ingest. See [log](../log.md) under 2026-05-14.

## Related

- [howard-kahana-2002-tcm source](../source/howard-kahana-2002-tcm.md) — primary cog-sci anchor.
- [mechanism-gap-matrix](../concept/mechanism-gap-matrix.md) — M13 is the row this hypothesis derives from.
- [cross-session-continuity](../open-question/cross-session-continuity.md) — the open gap H41 addresses.
- [consolidation-channel](../concept/consolidation-channel.md) — write-side complement to H41's read-side primitive.
- [active-stages-framework](../concept/active-stages-framework.md) — the retrieval-stage mechanisms the framework needs to make space for.
- [silent-engrams](../concept/silent-engrams.md) — orthogonal but compositional primitive (storage-side vs read-side).
- [substrate-as-memory](../concept/substrate-as-memory.md) — TCM-style context vector as a candidate substrate primitive at low depth (~depth-2 soft state).
- [H38 — rationale-trace-memory](./H38-rationale-trace-memory.md) — distant sibling; both are cog-sci-derived retrieval-side primitives but operate at different abstractions.
- [H39 — silent-state primitives](./H39-silent-state-primitives.md) — sibling hypothesis from the same path-decision-diligence period; potentially combinable architecture.
- [H40 — schema-fit-modulated consolidation](./H40-schema-fit-modulated-consolidation.md) — sibling hypothesis; write-side complement to H41's read-side primitive.
- [multi-field-memory-unit](../decision/multi-field-memory-unit.md) — `trajectory_state` field per S1 entry is a candidate concrete instantiation of H41's persistent context vector, with the predictor's internal state (from T_A1b's auxiliary loss) serving as the operational context representation.
- [2026-05-18-T_A1b-isolation-derisk](../experiment/2026-05-18-T_A1b-isolation-derisk/README.md) — probe 3 (trajectory-state decodability) is a partial test of H41's operational claim: that a maintained state-vector encodes position-in-pattern decodably.

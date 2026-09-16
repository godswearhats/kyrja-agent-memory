---
type: hypothesis
name: H-PLUGGABLE-SUBSTRATE — substrate-level memory can be trained store-agnostic, enabling multi-tenant frontier deployment
status: PROPOSED
last_ingested: 2026-05-15
sources: [../source/ttt-e2e-2026.md, ../source/sun-2024-ttt.md, ../source/behrouz-2024-titans.md, ../source/lecun-2022-autonomous-mi.md, ../source/borgeaud-2022-retro.md, ../source/graves-2014-ntm.md, ../source/xu-2026-agentic-memo.md, ../source/yu-2026-evosc.md, ../source/behrouz-2026-nested-learning.md, ../source/jiang-2024-minference.md]
epistemic_tags: [speculated, asserted]
tags: [substrate-memory, pluggable, multi-tenant, frontier-deployment, mcp, ttt, wedge-relevant]
---

## Claim

A frontier LLM can be trained such that **(a)** its substrate-level memory-access mechanism is invoked via a *learned gate* (the model decides when to consult), **(b)** the specific memory store providing content is **pluggable at inference time** — different stores can substitute without retraining the LM — and **(c)** the latent-space interface between LM and store is standardized enough to support a multi-tenant deployment model (one base model, per-user / per-tenant memory stores).

This combination unlocks a deployment pattern the field currently lacks: cloud-frontier-scale models with substrate-level memory integration that is *not* locked to a specific memory store at training time. If buildable, it routes around the structural forces (path dependence, interoperability premium) that push frontier labs toward prompt-level RAG, by *redefining* interoperability — the LM standardizes its memory-access interface the way OAuth standardized auth.

## What would falsify it

Any of:
- **Interface standardization fails technically.** The latent-space interface (LM ↔ memory) cannot be standardized — different stores require different LM architectures, making "pluggable" aspirational rather than substrate.
- **Training-time variability problem doesn't generalize.** Exposing the LM during training to a variety of memory stores produces overfitting to those specific stores; the trained model can't usefully consult genuinely-novel stores at inference.
- **Political economy blocks adoption.** Even if technically feasible, no lab adopts a neutral standard because differentiation is a competitive moat. (Falsifiable observationally: 2027-2028 will tell whether a substrate-level memory standard emerges.)
- **No meaningful advantage over prompt-level pluggability (MCP).** Substrate integration offers no semantic gain over MCP-style prompt-level pluggability; the additional architectural complexity isn't justified.

## Evidence for

- **TTT-E2E** (Stanford + NVIDIA, January 2026) `[ASSERTED]` (see [TTT-E2E source](../source/ttt-e2e-2026.md)) proves substrate-level test-time learning is buildable at frontier scale. Dual-memory system: Sliding Window Attention for working memory + mutable MLPs in the last 25% of blocks for test-time-learned storage. 2.7× speedup at 128K context, 35× at 2M; no reported scaling walls. The *substrate integration* piece is demonstrated, though in an *in-weights* variant rather than pluggable.
- **MCP — Model Context Protocol** (Anthropic, late 2024) `[ASSERTED]` proves pluggable memory interfaces work at *prompt level*. Cognee, Mem0, Letta all integrate via MCP. The *pluggability* piece is demonstrated, though at the wrong layer.
- **LongMem** (Wang et al. NeurIPS 2023) `[ASSERTED]` proves substrate-level integration via cross-attention works architecturally. Frozen base LM + sidecar memory network connected via cross-attention. The *substrate integration mechanism* is demonstrated.
- **Self-RAG** (Asai et al. 2023) and **Toolformer** (Schick et al. 2023) `[ASSERTED]` prove trained-to-decide-when-to-reach works. Models trained to emit special tokens that trigger retrieval, with the gating behaviour learned. The *learned gating* piece is demonstrated.
- **The synthesis is uncovered.** All four building blocks exist independently in the literature; the *specific combination* — substrate-level + trained gating + pluggable interface — does not appear in publicly-available work as of 2026-05-12 web survey. `[SPECULATED]` (Absence of evidence is not evidence of absence; arxiv MCP errored during the survey, so this should be re-verified.)
- **[EvoSC](../source/yu-2026-evosc.md)** (Yu et al. 2026) `[ASSERTED]` demonstrates per-domain learnable soft prompts (`P_θ`, 20 tokens) trained via knowledge distillation atop a frozen base LLM. This is the *weakest possible* form of pluggable-substrate: a swappable parametric prefix per domain. It validates that "small per-tenant parametric component atop a frozen base produces empirical gains" at depth-2 of the [substrate-depth ladder](../concept/consolidation-channel.md#substrate-depth-ladder). It does *not* address the hard parts of H37 — interface standardisation, cross-store generalisation at inference, frontier scale, or learned gating.
- **[Nested Learning / Hope](../source/behrouz-2026-nested-learning.md)** (Behrouz et al. 2026) `[ASSERTED]` introduces a vocabulary that *frames* H37 in NL terms without instantiating it. §3.3 ("Connections with Generation") explicitly names hypernetworks and optimisers as cases where *"one lower-frequency (resp. higher-frequency) block generates the weight of a higher-frequency (resp. lower-frequency) block"* — exactly the level-that-generates-an-interface shape H37 needs. The paper does not build a pluggable variant: Hope is monolithic, end-to-end-trained, no learned gate over stores, no standardised interface. **Vocabulary-friendly, no evidence.** `[SPECULATED]` H37's pluggable-substrate could be re-expressed as "a level whose context flow is the inference-time choice of memory store, and whose output is the gating decision into a downstream level."
- **MInference 1.0** (Jiang et al., NeurIPS 2024) `[ASSERTED]` (see [Jiang 2024 MInference](../source/jiang-2024-minference.md "pending")) catalogues sparse attention patterns spontaneously emerging in pretrained dense LLMs. **Vertical-Slash** heads attend to a fixed set of anchor positions that *every token in the sequence consults universally*, plus diagonal-offset slashes. These look like **learned global lookup tables forming spontaneously inside the attention pattern** — the model is building primitive pluggable-global-lookup behavior without being trained to. Strengthens H37's premise that "the model already wants" pluggable global access; the architecture would give it a more efficient way to express a behavior already present. *Informative signal, not load-bearing — observation taken from sparse-attention teaching summary (project memory `project_llm_fundamentals.md`, 2026-05-15), not yet anchored to verbatim paper read. Source page TODO before this becomes load-bearing for any decision.*

## Evidence against

- **Training-time variability problem unresolved.** LongMem and similar prior work train with a *single, fixed* memory store. The transition from "trained on one store" to "generalizes to any compliant store at inference" is not demonstrated. `[ASSERTED]`
- **Political economy of standardization.** Labs *want* their memory mechanism to be differentiated — that's competitive moat. The push toward neutral standardization has to come from below (developer demand) or a neutral actor; MCP at the prompt level is the closest precedent but doesn't threaten substrate differentiation. `[SPECULATED]`
- **Latent-space interface harder than protocol interface.** OAuth standardizes a *protocol* over *interpretable data structures*. A substrate-level memory interface has to standardize *latent representations* — the geometry of meaning itself. The closer analog is standardizing a CPU instruction set, not a web API. `[SPECULATED]`
- **TTT-E2E went non-pluggable.** The frontier *is* investing in substrate-level memory, but Stanford + NVIDIA chose the *in-weights* variant (mutable parameters) over the *pluggable external store* variant. This is informative: at frontier scale with current research, the simpler-to-train in-weights path was preferred. `[ASSERTED]` Suggests the pluggable-substrate path is harder, not that it's unbuildable.

## Open sub-questions

- **Interface contract**: what does the standardized LM ↔ memory-store API look like? Vector dimensionality? Retrieval semantics (top-k? threshold? attention-style soft-retrieval)? Embedding-space alignment guarantees? Who owns the alignment burden?
- **Training-time strategy for store variability.** Synthetic-memory-store augmentation during pretraining (analogous to data augmentation in vision)? Continual pretraining on real diverse stores? Adapter-based per-store fine-tuning? No published recipe.
- **Substrate vs prompt-level advantage**: does substrate-level integration actually outperform prompt-level pluggability (MCP) on agent benchmarks like MASQ, or is the gain mostly latency / token-cost rather than retrieval quality? Empirical question.
- **Gate generalization at inference**: when the LM encounters a store it never saw during training, does the learned gate fire appropriately? Or does it under-consult (treating the store as low-utility) or over-consult (hallucinating from noise)?
- **Standardization body**: who writes the spec? Anthropic (already pushing MCP)? An academic consortium (NeurIPS / ICLR adoption)? Hardware vendor (NVIDIA, Apple)? Each has different incentives and different prospects of success.

## Related

- [substrate-as-memory](../concept/substrate-as-memory.md) — paradigm concept this hypothesis sits inside.
- [substrate-paradigms](../concept/substrate-paradigms.md) — P1/P2/P3 taxonomy; pluggable-substrate is essentially "trained P2-substrate-as-module with a standardized interface."
- [consolidation-channel](../concept/consolidation-channel.md) — orthogonal axis; consolidation channel is *what* writes to the substrate; pluggable-substrate is *how* the LM accesses the substrate.
- [cross-session-continuity](../open-question/cross-session-continuity.md) — pluggable-substrate is one resolution path for cross-session continuity (per-user store, shared base model).
- [Active-stages framework](../concept/active-stages-framework.md) — operationalises *what* gets stored and accessed; this hypothesis is about *how* the access mechanism is architected and standardized.
- [H29 — edge-substrate-memory](./H29-edge-substrate-memory.md) — predicts the edge-vertical-integrator path for substrate memory. H-PLUGGABLE-SUBSTRATE predicts an *alternative* cloud-frontier path via standardization rather than vertical integration. The two are not mutually exclusive; both could land, in different segments.
- [admission-control](../concept/admission-control.md) — operationalises the *curation* (write-side) half of substrate memory; this hypothesis is about the *access* (read-side) architecture.
- 2026-05-13 substrate survey anchors: [TTT](../source/sun-2024-ttt.md) `(θ-projections, W-state)` split as a candidate interface; [Titans](../source/behrouz-2024-titans.md) test-time-update of a memory subnetwork; [LeCun 2022](../source/lecun-2022-autonomous-mi.md) KV associative memory module; [RETRO](../source/borgeaud-2022-retro.md) frozen-retriever + learned-cross-attention split; [NTM](../source/graves-2014-ntm.md) differentiable controller-memory coupling; [Xu et al. 2026](../source/xu-2026-agentic-memo.md) names consolidation-channel mechanisms (LoRA, MEMIT, TTT layers, Skill-SD).

## Origin

Synthesised during 2026-05-12 LLM curriculum + Kyrja design session, in the "spark" that followed the three-refusal walk-through. AJ's framing: webhooks-for-LLM-memory, with the LM trained to decide when to use the webhook. Literature survey performed same session via WebSearch (arxiv MCP rate-limited; arxiv side should be revisited).

---
type: open-question
name: End-to-end cost curve for a billion-vector agent memory system
status: OPEN
last_ingested: 2026-05-12
sources: []
epistemic_tags: [asserted]
tags: [cost, scale, integration]
---

## The question

**What's the actual cost curve for a billion-vector agent memory system using the integrated seven-layer stack** (admission control → multi-vector embedding → multi-graph memory → tiered storage → hybrid retrieval → consolidation → governance)?

Nobody has priced this out end-to-end. The [cost-leg-affordable-substrate](../concept/cost-leg-affordable-substrate.md) finding says individual substrate components are affordable at 1B+ scale (Turbopuffer, LanceDB, VectorChord/RaBitQ). The question is the **integrated cost** — substrate + embedding + graph + admission + consolidation + governance — at the corpus sizes the [scale-crossings](../concept/scale-crossings.md) model projects.

## Why it matters

- **Distinguishes substrate-affordable from system-affordable.** The cost-leg finding refutes the "substrate is unaffordable" framing, but doesn't establish that a *fully-integrated* agent memory system is affordable per-user at the operational margins customers expect.
- **Conditions the integration-play GTM.** If "Kyrja runs all seven layers" turns out to cost 10× a partial-layer incumbent, the integration premium has to be paid by some combination of pricing, customer adoption, or efficiency innovation we haven't yet identified.
- **Constrains the architecture.** Layers with high marginal cost at scale (e.g. multi-vector at billion-scale, LLM-driven consolidation) might force admission-control or tier-migration policies the wedge doesn't anticipate.

## What evidence would resolve it

- **End-to-end pricing model.** Take the six [scale-crossings](../concept/scale-crossings.md) scenarios and apply realistic per-layer pricing assumptions. Include LLM costs (admission, consolidation, governance audit), substrate costs (vector storage, graph storage, queries), and engineering costs (operational overhead).
- **Per-layer cost decomposition.** Which layer dominates at each scenario size? The answer changes the architectural priority.
- **Worked example at 1B+ vectors** — even a single integrated reference deployment with published TCO would anchor the curve.

## Related

- [cost-leg-affordable-substrate](../concept/cost-leg-affordable-substrate.md) — narrower finding: substrate alone is affordable
- [seven-layer-stack](../concept/seven-layer-stack.md) — the integrated architecture this question prices
- [scale-crossings](../concept/scale-crossings.md) — the volume axis the cost curve runs along
- [admission-control](../concept/admission-control.md) — the highest-leverage cost-control layer
- Vendor-pricing probe at `incumbent-pricing-2026-04-30.md`
- Deep-dive §11 Q11 origin: agentic-memory-scaling-deep-dive.md

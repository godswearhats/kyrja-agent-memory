---
type: concept
name: Memory consumer axis — who reads the memory
status: timeless
last_ingested: 2026-05-26
sources: [../source/wayne-2018-merlin.md, ../source/zhang-2026-compression-spectrum.md]
epistemic_tags: [asserted, speculated]
tags: [path-decision, memory-architecture, vocabulary, aj-originated]
---

## Definition

The **memory consumer axis** names *who reads the memory at retrieval time*:

- **Memory-for-the-model** — read by the LLM's own forward pass. Lives in the model's representations, activations, weights, or directly consumable latent state. The model thinks *with* the memory.
- **Memory-for-the-agent** — read by the agent's software loop, which inspects/selects memory and injects it into the LLM's prompt as input tokens. The model thinks *about* the memory.

This is a sharpening of the existing [substrate-vs-bolt-on axis](./substrate-as-memory.md), not a replacement. The two axes are co-extensional in today's systems — substrate ↔ memory-for-the-model, bolt-on ↔ memory-for-the-agent — but they name different things:

| Axis | What it names |
|---|---|
| Substrate vs bolt-on | *Where* the memory lives (inside the LLM vs outside it) |
| Memory consumer | *Who reads* the memory (the model's forward pass vs the agent's software loop) |

The reason the axes coincide today is that the only known way for memory to be read by the LLM's forward pass is to put it inside the LLM. The [memory-caddy open question](../open-question/memory-caddy.md) is precisely the question of whether that coincidence is necessary.

## Why this sharpening is useful

The substrate/bolt-on framing is architectural — it describes the artifact. The consumer framing is operational — it describes the interface. Three places the consumer framing pays off:

1. **Boundary cases become easier to classify.** kNN-LM retrieves nearest neighbors from a frozen datastore (looks bolt-on by location) but blends their log-probs into the LM's output distribution (read by the model, not the agent). The consumer framing puts it on the memory-for-the-model side of a fuzzy line; the architectural framing leaves it ambiguous.

2. **It exposes a falsifiability hook for the caddy.** The caddy proposal asks whether one could build memory-for-the-model that *is not* a modification of the primary LLM — a separate model whose output is consumed by the primary LLM's forward pass. If memory-for-the-model and substrate-modification are necessarily co-extensional, the caddy collapses; if they aren't, the caddy is real. The consumer framing makes that question askable.

3. **It clarifies what current bolt-on memory actually is.** Today's bolt-on memory is descriptively a distributed system in which the LLM is a stateless coprocessor — the agent harness orchestrates storage, retrieval, admission, and consolidation; the LLM is invoked when judgement is needed. Once you see bolt-on as memory-for-the-agent, the distributed-systems framing of that pipeline is obvious. See [memory-caddy](../open-question/memory-caddy.md) for the elaboration `[SPECULATED]` — claim 2 has not had a challenge-and-survival pass.

## Where the axes might diverge

The consumer axis admits four cells; only two are populated today.

| | Memory-for-the-model | Memory-for-the-agent |
|---|---|---|
| **Inside primary LLM** | Substrate (Larimar, Titans-trained weights, Hope) | (empty — incoherent) |
| **Outside primary LLM** | **Open — the caddy question** | Bolt-on (Mem0, Cognee, Letta, Zep) |

The empty cell is incoherent: memory inside the LLM but read by the agent's software loop would require the agent to introspect the LLM's internals at runtime, which no current system does. The open cell is the caddy question: a memory store that lives outside the primary LLM but is consumed by its forward pass (representation-out memory model, learned fusion interface). Whether anyone has built this — and whether it can be built without collapsing into either substrate-modification or bolt-on-with-extra-steps — is `[SPECULATED]`.

## Realised shapes today

`[ASSERTED]` based on 2026-05-15 caddy investigation; no comprehensive survey performed. **(2026-05-26 corroboration:** [Zhang et al. 2026](../source/zhang-2026-compression-spectrum.md) maps ~22 deployed agent-memory/skill systems, *all* memory-for-the-agent / scaffold-level, with weight-integration explicitly out of scope — external support for Case A dominance.**)**

In modern agent architectures, **memory-for-the-model (Case A) is overwhelmingly the realised shape** — even though the consuming LLM is typically frozen and pretrained, retrieved memory still lands in the LLM's input (as prompt tokens) and is therefore consumed by the LLM's forward pass at runtime. The two cells of the architectural × consumer 2×2 that are widely deployed:

- *Inside primary LLM × memory-for-the-model:* substrate-shaped systems ([Larimar](../source/lecun-2022-autonomous-mi.md), [Titans](../source/behrouz-2024-titans.md)-class training-time memory).
- *Outside primary LLM × memory-for-the-model (via prompt injection):* every commercial agentic-memory product — [Mem0](../incumbent/mem0.md), [Cognee](../incumbent/cognee.md), [Letta](../incumbent/letta.md), [Zep](../incumbent/zep.md), [Honcho](../incumbent/honcho.md), [Supermemory](../incumbent/supermemory.md), [Hindsight](../incumbent/hindsight.md), [LangMem](../incumbent/langmem.md).

**Memory-for-the-agent (Case B) is rare in practice** and tends to collapse into **constraint/rule enforcement** rather than experiential memory — Constitutional-AI-style hard constraints ("never delete files without confirming"), tool-use whitelists, retry-policy gates. True experiential lessons want to influence reasoning, and reasoning happens in the LLM, not in the agent harness. The agent-as-consumer architecturally exists but is underused for memory because the only thing the agent loop can usefully *do* with a remembered lesson, without the LLM's reasoning, is enforce a rule.

**Consequence for the caddy question:** the architectural ground for the caddy lives within Case A, and the choice point is *how* the memory module's output reaches the LLM — text injection (bolt-on shape), activation injection (co-trained cross-attention, [Memorizing Transformer](../source/wu-2022-memorizing-transformer.md) / [RETRO](../source/borgeaud-2022-retro.md) shape), or adapter/LoRA modulation (exotic). See [memory-caddy § Consumer-axis collapse](../open-question/memory-caddy.md) for the detailed three-interface decomposition, and [caddy-interface-doors](./caddy-interface-doors.md) for the architectural-port-level sharpening (D-doors, U-doors, Q-doors) added 2026-05-17.

## Status

- **Definitional core** (`[ASSERTED]`): the two-term definition of the axis is true by stipulation.
- **Case A dominance** (`[ASSERTED]` based on 2026-05-15 investigation; no comprehensive survey performed): in modern agent architectures, memory-for-the-model is the overwhelmingly realised shape; memory-for-the-agent collapses to constraint enforcement. See *Realised shapes today* above.
- **"More useful than the architectural axis"** (`[SPECULATED]`): claim 1 from [memory-caddy](../open-question/memory-caddy.md). Not yet pressure-tested.
- **Provenance:** AJ-originated, 2026-05-15, mid-walkthrough of the [mechanism-gap-matrix](./mechanism-gap-matrix.md). Promoted into wiki vocabulary 2026-05-15 as the cheap-and-reversible move before deciding whether to invest in the caddy investigation. *Realised shapes* section added 2026-05-15 (later) after the MERLIN investigation surfaced the Case A collapse.

## Related

- [substrate-as-memory](./substrate-as-memory.md) — the architectural axis this concept sharpens.
- [caddy](./caddy.md) — the canonical architectural definition of the within-family alternative to bolt-on. The caddy occupies the *outside-LLM × memory-for-the-model* cell of the consumer-axis 2×2.
- [memory-caddy](../open-question/memory-caddy.md) — the open question that motivates the sharpening.
- [substrate-paradigms](./substrate-paradigms.md) — internal taxonomy within memory-for-the-model.
- [consolidation-channel](./consolidation-channel.md) — the operator that moves information from memory-for-the-agent to memory-for-the-model.
- [norman-rubric](./norman-rubric.md) — externally validates memory-for-the-model. Norman et al. (TiCS 2025, page 4) explicitly endorse storing *internal representations* (keys/values) over *verbatim text*, which is the activation-level / memory-for-the-model side of this axis. *"The latter approach aligns better with human EM, insofar as humans store internal representations rather than verbatim input."*
- [NOW.md](../NOW.md) — current active question; this concept reframes the axis it sits on.
- [retrieval-granularity](./retrieval-granularity.md) — orthogonal design dimension; how often the consumer reads from memory during generation. The consumer-axis says *who* consumes; granularity says *when*.
- [H43 — soft-composition emergent construction](../hypothesis/H43-soft-composition-emergent-construction.md) — the soft-composition vs hard-selection interface fork lives within the memory-for-the-model side; what the caddy hands the LLM determines whether emergent construction is achievable.

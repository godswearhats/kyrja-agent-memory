---
type: concept
name: Retrieval granularity — the spectrum of when memory is surfaced during generation
status: timeless
last_ingested: 2026-05-17
sources: [../source/wu-2022-memorizing-transformer.md, ../source/khandelwal-2020-knn-lm.md, ../source/borgeaud-2022-retro.md, ../source/buzsaki-2015-spw-r.md]
epistemic_tags: [asserted, speculated]
tags: [retrieval, granularity, caddy-relevant, agent-memory-blind-spot, taxonomy]
---

## Definition

**Retrieval granularity** is the design dimension that specifies *when* — at what temporal frequency during generation — a memory-augmented language model consults its memory substrate. The spectrum runs from fine (per-layer-per-token) to coarse (per-conversation-turn), with several intermediate positions each anchored to specific research architectures. Granularity is logically independent of memory *content* (what's stored), memory *substrate* (where it lives), and the memory *output interface* (hard selection vs soft composition); but it interacts with all three.

This page exists because (a) granularity is referenced by [caddy](./caddy.md), [memory-caddy](../open-question/memory-caddy.md), [consolidation-channel](./consolidation-channel.md), [H43](../hypothesis/H43-soft-composition-emergent-construction.md), and any future caddy-architecture decision; (b) it has a clear taxonomy with active research positions; (c) the *current agent-memory product space defaults to per-turn retrieval without testing finer alternatives*, which is a structurally significant blind spot worth tracking.

## The spectrum

`[ASSERTED]` Five positions, ordered fine → coarse:

| Position | Description | Reference architecture | Retrieval cost (per response) |
|---|---|---|---|
| **1. Per-token, per-layer** | Multiple layers attend to memory; every next-token prediction triggers retrieval at each wired layer | [Memorizing Transformer](../source/wu-2022-memorizing-transformer.md "pending") (single layer); H37 territory (multi-layer) | `O(L_mem · T)` where `L_mem` = number of memory-wired layers, `T` = tokens generated |
| **2. Per-token, single point** | Retrieval at every next-token prediction; one interpolation point | [kNN-LM](../source/khandelwal-2020-knn-lm.md "pending") | `O(T)` |
| **3. Per-chunk** | Retrieval every N tokens (typically N=32-64); retrieved chunks influence generation for the chunk | [RETRO](../source/borgeaud-2022-retro.md "pending") | `O(T/N)` |
| **4. Per-turn** | One retrieval at start of generation; concatenate into context; generate the whole response | RAG, [Mem0](../incumbent/mem0.md), [Zep](../incumbent/zep.md "pending"), [Letta](../incumbent/letta.md "pending"), [Cognee](../incumbent/cognee.md "pending"), [LightMem](../incumbent/lightmem.md) | `O(1)` |
| **5. Multi-point, heterogeneous** | Different layers attend to different memory pools at different abstraction levels (semantic vs episodic vs procedural) | [H37 (pluggable substrate)](../hypothesis/H37-pluggable-substrate.md "pending") | `O(L_mem · T · M)` where `M` = pools |

`[ASSERTED]` DB analogy: how often does the query planner consult a materialised view? Per query (per-turn), per row batch (per-chunk), per row (per-token), per join operator (per-layer). Each is a different cost/leverage tradeoff.

## Why this matters

`[ASSERTED]` Three load-bearing observations:

### 1. The agent-memory product space all defaults to per-turn — without testing alternatives

Every commercial / production agent-memory system surveyed in the [mechanism-gap matrix § incumbent mapping](./mechanism-gap-matrix.md) operates at per-turn granularity. Memory is fetched once, concatenated into context, generation happens; the memory substrate is not consulted again until the next turn. This is the cheapest option (one retrieval per response, `O(1)` in the table above) and the easiest to implement on top of any existing LLM API.

But the language-modelling research literature (kNN-LM, RETRO, Memorizing Transformer) has shown for years that **finer granularity is strictly more powerful for long-context modelling**, at modest cost. The transfer of this insight from LM research to agent-memory product hasn't happened. It's a structurally significant gap.

`[SPECULATED]` This may be a *capability vs adoption-cost* gap (per [capability-vs-resource](../feedback_capability_vs_resource "pending")): finer granularity requires architectural surgery on the LLM (cross-attention at intermediate layers, kNN-augmented decoding). Per-turn retrieval requires only a prompt-construction wrapper. The path-of-least-resistance won.

### 2. Granularity interacts with composition

`[ASSERTED]` From [H43](../hypothesis/H43-soft-composition-emergent-construction.md): emergent construction requires soft-composition output. Soft composition is *cheap and natural at fine granularity* (attention is the soft composition primitive) and *expensive and unnatural at per-turn granularity* (you'd have to compose memories into a synthetic context blob via a separate process before generation begins). The choice of granularity *constrains* what kinds of output interface are practical.

| Granularity | Natural output interface | Composition path |
|---|---|---|
| Per-token, per-layer | Soft composition (attention) | Emergent from training |
| Per-token, single point | Soft interpolation (kNN-LM style) | Distribution-level blending |
| Per-chunk | Cross-attention over chunks | Soft, chunk-bounded |
| Per-turn | Hard selection + context concat | Has to be engineered separately |

So granularity is not orthogonal to interface — it pre-selects the natural choices.

### 3. The "right granularity" is partly emergent, partly engineered

`[SPECULATED]` AJ's observation (during the M16 walk): if the caddy's gate is learned end-to-end (cross-attention over a memory pool), the granularity question partly *dissolves*. The model learns when each memory becomes salient during generation. You don't pick granularity; the trained attention picks for you.

This is the bet [Memorizing Transformer](../source/wu-2022-memorizing-transformer.md "pending") makes — single-layer kNN attention over a long-term cache, fired at every token, with the *learned attention weights* determining when the memory is actually used. The granularity is "per-token, per-layer" *architecturally*, but the *effective* granularity (when memory actually matters) is learned per query.

If this generalises, the only granularity decision that matters is the *coarsest* one — "is memory consulted at all during this response?" — and per-token-per-layer is the safe default because it's the most flexible. The architectural commitment to a finer granularity buys you the *option* to use memory finely; the trained model decides whether to take that option.

`[SPECULATED]` Coarse granularities (per-turn) foreclose this option entirely. The model can't learn to attend to memory mid-response if there's nothing to attend to. So granularity choice is asymmetric: fine is dominant (you can simulate coarse with attention weights ≈ 0 except at turn boundaries) but coarse is not (you cannot recover fine-grained access from a per-turn-only interface).

## Two surfaces, not one

`[ASSERTED]` Biology (per [M14 Buzsáki SPW-Rs](../source/buzsaki-2015-spw-r.md)) operates at *two granularities simultaneously*:

- **Online surface (theta-mode during active behaviour)**: continuous low-latency integration of memory into ongoing cortical processing. Maps to per-token / per-layer in the spectrum.
- **Off-line surface (SPW-R during sleep / quiet wakefulness)**: batch-oriented recombination of fragments. Maps to a regime *outside* the table — runs between conversations, not during them.

For Kyrja, this means the granularity choice is two choices: the *online* granularity (where on the spectrum the runtime memory surface lives) AND whether there's an *off-line* surface (the [consolidation-channel](./consolidation-channel.md)). The two are not in competition — they compose, doing different jobs.

The [memory-caddy](../open-question/memory-caddy.md) open question and [H43](../hypothesis/H43-soft-composition-emergent-construction.md) focus on the online surface. The [consolidation-channel](./consolidation-channel.md) page focuses on the off-line surface.

## Scope limits

- **Granularity is independent of interface.** A per-turn system can use either hard selection or soft composition (preconstructed during pre-generation processing). A per-token system can use either too. But finer granularities make soft composition *natural*; coarser granularities make hard selection *cheap*. The interaction is statistical, not deterministic.
- **Granularity is independent of substrate.** Vector DB, learned key-value cache, in-context concatenation — any substrate can be consulted at any granularity. The substrate constrains *cost*, not *frequency*.
- **This page does not prescribe.** Kyrja has not committed to a granularity. The active hypothesis is that per-token-per-layer is the right default because it preserves the option to learn finer access. That's a recommendation, not a decision.
- **The cost numbers are *frequency*, not absolute cost.** Naive per-token kNN over millions of vectors sounds expensive; FAISS does millions of queries per second. Per-layer cross-attention over a memory pool is just another attention computation at inference time. The granularity story is dominated by *interface and infrastructure*, not by *frequency of access*.

## Related

- [caddy](./caddy.md) — granularity is a design-fork dimension; soft-composition + fine granularity is the H43 bet
- [memory-caddy](../open-question/memory-caddy.md) — open-question framing including granularity ladder
- [H43 — soft-composition emergent construction](../hypothesis/H43-soft-composition-emergent-construction.md) — composition × granularity interaction
- [consolidation-channel](./consolidation-channel.md) — the *off-line* surface complementing whichever online granularity is chosen
- [mechanism-gap-matrix](./mechanism-gap-matrix.md) — current incumbents' granularity choices (all per-turn) tabulated in incumbent mapping
- [H37 — pluggable substrate](../hypothesis/H37-pluggable-substrate.md "pending") — multi-point heterogeneous granularity is H37's architectural commitment
- [buzsaki-2015-spw-r](../source/buzsaki-2015-spw-r.md) — two-surfaces precedent from biology
- [seven-layer-stack](./seven-layer-stack.md) — granularity affects which layers are exercised per memory event
- [discrete-unit-memory-architecture](./discrete-unit-memory-architecture.md) — the broader family; granularity choice partially defines membership

## Source archive

Synthesized from the M16 walk discussion (2026-05-17) where the question of "do you surface memories at every swing, or at every turn, or somewhere in between?" was raised by AJ. The five-position spectrum was compiled during that walk; the architectural references to kNN-LM, RETRO, and Memorizing Transformer come from prior agent-memory research surveys (see [reference_paper_repo](../../_archive/reference_paper_repo "pending")).

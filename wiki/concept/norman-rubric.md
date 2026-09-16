---
type: concept
name: Norman rubric — five evaluable properties of human-like episodic memory in MA-LLMs
status: timeless
last_ingested: 2026-05-16
sources: [../source/dong-2025-norman-episodic.md]
epistemic_tags: [asserted, externally-defined]
tags: [norman-rubric, evaluation, caddy-validation, mechanism-gap-matrix-anchor]
---

## Definition

The **Norman rubric** is the set of five evaluable architectural properties of human-like episodic memory specified in [Dong, Lu, Norman & Michelmann 2025](../source/dong-2025-norman-episodic.md), Trends in Cognitive Sciences. It is the externally-defined evaluation framework Kyrja's [caddy](caddy.md) will be measured against in VC diligence, academic review, and any "how is this different from existing systems" question.

The rubric exists as its own concept page because (a) it is referenced by [caddy](caddy.md), [memory-caddy open question](../open-question/memory-caddy.md), [consolidation-channel](consolidation-channel.md), [memory-consumer-axis](memory-consumer-axis.md), [mechanism-gap-matrix](mechanism-gap-matrix.md), and the wiki log; and (b) it has an external author with a status lifecycle independent of Kyrja's framing (subsequent Norman lab publications may extend or modify it).

## The five properties

| # | Property | What it requires | Cog-sci basis |
|---|---|---|---|
| 1 | **Dynamic memory updating** | Memories can be altered after addition (strength, content, deletion). Reconsolidation. Not "append-only memory" or "static store." | [reconsolidation](../source/nader-schafe-ledoux-2000-reconsolidation.md); [redondo-morris-2011-stc](../source/redondo-morris-2011-stc.md) |
| 2 | **Event segmentation** | Memories chunked at surprise-based event boundaries, not fixed-size windows. Event-boundary detection is upstream of encoding. | Event-segmentation theory (Zacks et al. 2007); EM-LLM (Fountas 2025) is the only MA-LLM doing this per Norman |
| 3 | **Selective encoding and retrieval** | Encoding stronger at event boundaries and at moments of high uncertainty; retrieval triggered by prediction failure or schema gap, not every-k-tokens. | Michelmann et al. 2021; FLARE (Jiang 2023) for selective retrieval |
| 4 | **Temporal contiguity** | Successive recalls tend to come from nearby timepoints. **Scale-invariant** — applies across multiple timescales. | TCM ([howard-kahana-2002-tcm](../source/howard-kahana-2002-tcm.md)); Healey 2019 |
| 5 | **Competition at retrieval** | Narrow bandwidth — typically 1 or 0 best-matching memories activate consciously, not top-k. | Anderson 1974 (retrieval competition); Schlichting et al. 2017 (CLS as winner-take-all in hippocampus) |

The Norman paper also specifies the **architectural shape** the rubric assumes: a memory system "separate from both the context window... and the weights of the main LLM" — i.e., the [caddy](caddy.md) shape. This is upstream of the five properties and load-bearing for evaluating whether a system can even participate in the rubric scoring (bolt-on systems and substrate-only systems fail the architectural prerequisite).

Plus the **Box 4 benchmark proposal**: information presented continuously, model decides *when* to encode and *when* to retrieve, lures present, no pre-staging. Compare against no-memory baseline to isolate EM contribution. See [dong-2025-norman-episodic](../source/dong-2025-norman-episodic.md) for the full Box 4 specification.

## Scoring existing systems

`[ASSERTED]` Kyrja-internal scoring 2026-05-16 based on reading each system's specification and Norman's own commentary where applicable.

| System | Architecture | Dynamic update | Event seg | Selective enc/retr | Temporal contiguity | Competition | **Score** |
|---|---|---|---|---|---|---|---|
| Bolt-on incumbents ([Mem0](../incumbent/mem0.md), [Cognee](../incumbent/cognee.md), [Letta](../incumbent/letta.md), [Zep](../incumbent/zep.md), [Honcho](../incumbent/honcho.md), [Supermemory](../incumbent/supermemory.md), [Hindsight](../incumbent/hindsight.md), [LangMem](../incumbent/langmem.md)) | Text-injection RAG | ✗ | ✗ | ✗ | ✗ | ✗ | **0/5** |
| [Memory³](../source/yang-et-al-2024-selection-of-experience.md) | Substrate hybrid | ✗ | ✗ | partial | ✗ | ✗ | **0.5/5** |
| [Titans](../source/behrouz-2024-titans.md) | Substrate test-time gradient | ✓ (Norman calls it "particularly promising") | ✗ | partial | ✗ | ✗ | **1.5/5** |
| [Hope / Nested Learning](../source/behrouz-2026-nested-learning.md) | Substrate multi-frequency | ✓ | ✗ | partial | ✗ (but multi-frequency) | ✗ | **1.5/5** |
| [MEGa](../source/pan-2025-mega.md) | In-weights gated LoRA | partial (future work) | ✗ | ✗ | ✗ | partial | **1.5/5** |
| [Spens & Burgess](../source/spens-2024-hippocampal-rag.md) | Bolt-on/substrate hybrid | ✓ (schema distortions empirically shown) | ✗ | partial | ✗ | ✗ | **1.5/5** |
| FLARE | Bolt-on with uncertainty trigger | ✗ | ✗ | ✓ | ✗ | ✗ | **1/5** |
| EM-LLM (Fountas 2025) | Bolt-on with event boundaries | ✗ | ✓ | ✓ | partial | partial | **~2.5/5** |
| [Engramme](../incumbent/engramme.md) | Personal-data RAG | ✗ | ✗ | ✗ | ✗ | ✗ | **0/5** |
| **Kyrja caddy (target)** | **Sidecar with full CLS stack** | **✓** | **✓** | **✓** | **✓** | **✓** | **5/5** |

EM-LLM is the current academic ceiling at 2.5/5. **No system scores above 2.5/5.** The full-rubric cell is empirically open as of 2026-05-16 — eleven months after the rubric was published in a top venue.

## Why this matters

1. **External validation of the [caddy](caddy.md) wedge.** Norman et al. — the leading academic group on hippocampal-CLS modelling — endorse the sidecar-separate-from-weights-and-context architecture by name. This inverts the usual "what about the prior art?" question in VC diligence: the prior art validates us, not threatens us.

2. **Operational target for Kyrja's experimental programme.** Building to score 5/5 on this rubric is a falsifiable goal. Implementing each property is research-grade work; scoring all five simultaneously is the differentiation that no existing system has achieved.

3. **Box 4 specifies the benchmark shape.** Standard QA benchmarks (LOCOMO, NIAH, BABILong, etc.) fail to test selectivity, segmentation, temporal contiguity, or competition because they pre-stage relevant memories. The Box 4 design (continuous information, no pre-staging, lures present) is what experiments distinguishing a caddy from bolt-on RAG should look like.

4. **The post-Norman gap is empirical and persistent.** Eleven months after publication, no post-Norman publication systematically addresses the rubric. The most plausible reason is implementation difficulty: each property is non-trivial and integrating all five requires architectural commitment, not feature add. See [memory-caddy](../open-question/memory-caddy.md) § "Post-Norman gap finding" for the longer treatment.

## Scope limits

- The rubric is **necessary, not sufficient**. A 5/5 system is "human-EM-aligned" — translating that to product-relevant agent-memory performance is the empirical bet Kyrja still has to make. Norman et al. do not claim the rubric is a sufficient condition for product utility.
- The rubric is **descriptive of human EM, not prescriptive of optimal AI memory**. There may be desirable agent-memory properties that humans don't exhibit (e.g., perfect audit trails for compliance) or human EM properties that don't transfer well to AI (e.g., emotional valence-gated consolidation).
- The rubric is **not a benchmark dataset**. Box 4 specifies the shape; building an actual benchmark instance is work Kyrja or someone else has to do.
- The rubric is **silent on cross-session governance**. Per-user scoping, deletion, audit — these are product properties Norman et al. don't address.

## Related

- [caddy](caddy.md) — the architectural pattern Norman explicitly endorses; the rubric is the evaluation framework.
- [memory-caddy](../open-question/memory-caddy.md) — the open question of whether the caddy concept survives empirical scrutiny; Norman rubric becomes the primary evaluation target.
- [consolidation-channel](consolidation-channel.md) — Norman's Outstanding Question 2 names the consolidation operator as the missing piece in MA-LLMs.
- [memory-consumer-axis](memory-consumer-axis.md) — Norman endorses memory-for-the-model (internal representations, not verbatim text).
- [mechanism-gap-matrix](mechanism-gap-matrix.md) — the five Norman properties slot into the mechanism-gap framework.
- [discrete-unit-memory-architecture](discrete-unit-memory-architecture.md) — the rubric implicitly assumes discrete-unit family architecture (separately-stored memories with explicit retrieval).
- [complementary-learning-systems](complementary-learning-systems.md) — the cog-sci basis of the rubric's architectural endorsement.

## Source archive

[dong-2025-norman-episodic](../source/dong-2025-norman-episodic.md) is the canonical source. Verbatim quotes for each property are extracted there. Local PDF: [`dong-2025-norman-episodic.pdf`](../../../research/library/papers/dong-2025-norman-episodic.pdf).

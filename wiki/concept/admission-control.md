---
type: concept
name: Admission Control (Learned Write-Side Gate)
status: timeless
last_ingested: 2026-05-19
sources: [../source/admission-control-2603.md, ../source/memory-surveys-2026.md, ../source/tse-et-al-2007-schemas.md]
epistemic_tags: [asserted, speculated]
tags: [admission-control, learned-gate, wedge-relevant, write-side]
---

## Definition

**Admission control** is the layer that decides, on write, whether each candidate memory should enter the long-term store at all. Operates **before** embedding, indexing, and consolidation — the storage cost of rejected memories is zero, and the retrieval-side scale problem is reduced at the source.

This is the top layer of [seven-layer stack](./seven-layer-stack.md).

## Why it matters more than it seems

`[ASSERTED]` (deep-dive §11 Q2; [adaptive admission control paper](../source/admission-control-2603.md)). If **80% of agent memories are redundant or low-value**, preventing their creation is orders of magnitude cheaper than storing and searching them later. Compare the cost of:

- **No admission control:** store everything, pay storage cost forever, pay retrieval cost on every query, fight the cascading-failures regime via consolidation, multi-vector retrieval, tiered storage, etc.
- **With admission control:** 80% of writes never happen, the binding scale constraint shifts from "how many billions of vectors" to "how good is the gate."

Admission control is the only layer that can change the corpus size, not just the corpus's index/retrieval characteristics. **Every other layer fights symptoms; admission control treats the cause.**

> **M17 tension (added 2026-05-17):** the M17 walk ([Hardt, Nader & Nadel 2013](../source/hardt-nader-nadel-2013-active-forgetting.md)) surfaced a competing architectural framing — "encode promiscuously, forget intelligently." Biology defers the keep/drop decision until evidence has accumulated, on the grounds that the value of an experience is often only knowable after the fact. Under that framing, "admission control treats the cause" reads as "admission control is the *fastest* you can act on incomplete information." The cause being treated may itself be a *category error* if the right thing to do is to *not commit* at write time and apply intelligence to the surviving set via a graded forgetting policy. See [H34 — forgetting scores](../hypothesis/H34-forgetting-scores.md) and [pattern-separation](./pattern-separation.md) for the alternative-framing pieces. This tension is unresolved and is a real architectural fork for Kyrja, not a corollary of the existing framing. The two framings are reconciled by the observation that *pattern separation is required regardless of which side the intelligence sits on* — see [pattern-separation § Why this matters](./pattern-separation.md).

## Three flavors

### 1. Learned admission gate (arxiv 2603.04549)

A trained classifier decides admission per candidate. Training signal is the open question — utility labels are noisy, available only in retrospect.

**Our restatement:** This is the "right" answer in the long run. Short term, the training-signal problem is the binding constraint. See [admission-control source page](../source/admission-control-2603.md).

### 2. Entropy / compression-based filtering (LightMem-style)

[LightMem](../incumbent/lightmem.md)'s "sensory memory" stage uses lightweight compression (LLMLingua-2 or entropy-based) as a non-learned admission gate. Cheaper than a learned classifier, lower fidelity.

**Our restatement:** The right pre-MTP approach. We can ship entropy-based admission before having the utility-signal corpus to train a learned gate on.

### 3. LSH-based dedup before embedding

Hash candidates and reject near-duplicates before paying the embedding cost. Mentioned in the seven-layer-stack diagram as a parallel primitive to importance scoring.

**Our restatement:** Mechanically simple; complementary to the other flavors. Catches the easy case (redundant writes) without addressing the harder case (low-value writes).

## What current incumbents do

`[ASSERTED]`. Per-incumbent admission behavior is sourced from [Cognee docs](../source/cognee-docs.md), [Mem0 paper](../source/mem0-paper-2504.md), [Zep/Graphiti paper](../source/zep-graphiti-2501.md), [LightMem paper](../source/lightmem-2510.md), and [Letta/MemGPT paper](../source/letta-memgpt.md). The cross-incumbent rollup below is a Kyrja synthesis of those source docs; the same table also appears on [seven-layer-stack](./seven-layer-stack.md#incumbent-mapping):

| Incumbent | Admission strategy |
|---|---|
| Cognee | None — everything in the pipeline gets stored |
| Mem0 | LLM-mediated post-extraction (ADD/UPDATE/DELETE/MERGE) — *not* pre-embedding; latency scales with corpus |
| Zep | None — every event enters the episodic subgraph |
| LightMem | Sensory-memory filtering (closest to a real admission gate; entropy/compression-based) |
| Letta | Agent-driven (the LLM decides what to write to recall vs archival) |

**Net: no incumbent has a learned admission gate. LightMem and Letta come closest, in opposite ways.**

## The training-signal problem

**Open question (deep-dive §11 Q2 and [admission control paper](../source/admission-control-2603.md)):** how do you train an admission gate without retrospective utility labels?

Possible signals (all `[SPECULATED]`):
- **Self-supervised:** Predict whether a memory will be retrieved within N days.
- **Distillation:** A larger model labels admission decisions, a smaller model learns to imitate.
- **RL on retrieval utility:** When a memory is retrieved and used, the admission decision was correct; when it's never used, it was wrong. Sparse signal.
- **Heuristic bootstrap:** Start with simple rules (LSH dedup + length filter + importance score), collect training data, train a learned gate from logged decisions.

The fourth option is the most pragmatic short term and aligns with the MTP-first build plan: ship the simplest possible admission heuristic, log everything, train a learned gate when there's data.

**Biological precedent — schema-fit as an admission signal.** [Tse et al. 2007](../source/tse-et-al-2007-schemas.md) shows that *schema-compatible* information consolidates ~50-100× faster than schema-incompatible information in the rat neocortex. The mechanism suggests admission isn't binary — it can be *rate-modulated by fit to existing knowledge*. AI translation candidate: detect schema-fit per memory candidate (e.g., consistency with pretrained LLM's existing knowledge + the agent's user-model), then (a) high-fit → fast consolidation with minimal evidence, (b) low-fit → slow consolidation with more evidence required, (c) no-fit → store as exception/episode without weight-level commitment. The training-signal problem narrows from "is this useful?" to "does this fit?" — which is more tractable from internal model state. Promoted to falsifiable claim in [H40 — schema-fit-modulated consolidation](../hypothesis/H40-schema-fit-modulated-consolidation.md).

## Connection to the wedge

Admission control is the **single most important architectural primitive for the wedge product**. The wedge's [precision-over-recall decision](../decision/precision-over-recall.md) operates on the read side; admission control operates on the write side. Together they bound the cascading-failures regime from both ends:

- Read: precision threshold rejects low-confidence retrievals.
- Write: admission gate rejects low-value memories.

The [structured filter-first decision](../decision/structured-filter-first.md) is upstream of admission: it pre-classifies memories by structure before they reach the admission gate.

**Wedge-product implication.** A simple admission heuristic (LSH dedup + a length floor + an importance heuristic from the distiller) ships in the MTP. The learned gate is a Phase-2 upgrade once we have a corpus of logged admission decisions with utility labels.

## Related

- [Active-stages framework](./active-stages-framework.md) — admission control operationalises the *curation* stage; the four training signals listed here align with the RLVR-for-curation recommendation there.
- [Mechanism-gap matrix](./mechanism-gap-matrix.md) — schema-fit rate modulation = row M05; the broader catalogue of biological mechanisms × AI status.
- [H40 — schema-fit-modulated consolidation](../hypothesis/H40-schema-fit-modulated-consolidation.md) — the falsifiable hypothesis that extends admission from binary to rate-modulated.
- [Cascading-failures product](./cascading-failures.md) — the regime admission control reduces at the source.
- [Seven-layer stack](./seven-layer-stack.md) — admission is the top layer.
- [LightMem incumbent page](../incumbent/lightmem.md) — closest production analog (sensory-memory filtering).
- [Precision over recall](../decision/precision-over-recall.md) — the read-side counterpart.
- [Structured filter first](../decision/structured-filter-first.md) — upstream pre-classification.
- [Worst-case source](../open-question/worst-case-source.md) — admission control with worst-case sources is the gating question for write-side-quality-gate-deferrability.
- [salience-signal](../open-question/salience-signal.md) — admission policies are salience-application at write time; the upstream computation of the salience signal is the load-bearing input variable for any admission gate.
- [H42 — learned salience function](../hypothesis/H42-learned-salience-function.md) — falsifiable claim that a learned salience function beats LLM-call importance scoring at lower cost; directly relevant to admission-time scoring.

## Source archive

Concept synthesized from deep-dive §8 (admission control) + §11 Q2 + seven-layer-stack §10. See agentic-memory-scaling-deep-dive.md, lines 779-785 and 1049-1050.

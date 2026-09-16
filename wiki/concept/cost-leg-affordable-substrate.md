---
type: concept
name: Cost Leg — Affordable Substrate ≠ Correct Retrieval
status: timeless
last_ingested: 2026-05-13
sources: [../source/rabitq-2024.md]
epistemic_tags: [measured, asserted]
tags: [scale-thesis, cost-leg, go-to-market]
---

## Definition

The **cost-leg framing** is the finding that storage and query cost is *not* a wall for incumbents at billion scale, contrary to an earlier reading of the scale thesis. Object-storage-first and quantization-first substrates (Turbopuffer, LanceDB, S3 Vectors, VectorChord with RaBitQ) are already shipped, already affordable, and already serve production deployments at 1B+ vectors. **Cost was never the load-bearing claim** of the scale thesis; recall-collapse was. Affordable substrate does not fix retrieval correctness.

## The headline numbers

- **Turbopuffer** (~$1/M-vec/mo + $4/M-queries, object-storage-first) keeps every scenario except F under $1/user/month. `[ASSERTED]` — vendor pricing as of 2026-04-30. Powers Cursor and Notion at 3.5T+ documents.
- **Weaviate Premium** keeps moderate-enterprise scenarios under $10/user/month through Scenario E. `[ASSERTED]` — vendor pricing.
- **VectorChord + RaBitQ** runs 1B+ vectors on a single 128GB-RAM PostgreSQL machine. `[MEASURED]` from [RaBitQ paper](../source/rabitq-2024.md). *Construct-validity:* lab-bench numbers on standard ANN benchmarks; production workload mix may differ but order of magnitude holds.
- **Pinecone Serverless and full-precision Qdrant blow up** at high-end scenarios — $280M/yr at 2.7B vectors (Scenario E); $1.17B/yr at 8.5B vectors (Scenario F) for Pinecone Serverless. `[ASSERTED]` — vendor pricing applied to scale-model scenarios. **This is vendor choice, not a market-wide constraint.**
- **LanceDB is a published reference architecture for 1B+ on S3.** `[ASSERTED]` — vendor docs, see [LanceDB source](../source/lancedb.md).

## Role in Kyrja thesis

This finding **weakens the substrate-replacement go-to-market story** (GTM #2 in [THESIS.md](../../../research/scale-model/THESIS.md)): "Kyrja runs the same memory feature surface 100-1000× cheaper because of object-storage-first / tiered / RaBitQ-quantized architecture." That story survives but is weaker — the substrate is already shipping in the market and getting cheaper independent of us.

It **strengthens the integration-play story** (GTM #1): "Kyrja runs all seven layers with discipline. Others have one or two." If the substrate is solved and the retrieval is still broken (see [benchmark-replication-gap](./benchmark-replication-gap.md)), the differentiator is the layers *above* the substrate, not the substrate itself.

The cost-leg also reframes one of three deep-dive synthesis updates: storage cost is no longer the binding constraint at billion scale. Binding constraints shift to recall (the [LIMIT bound](../source/weller-2025-limit.md)) and consolidation. The tiered-storage layer of the [seven-layer stack](./seven-layer-stack.md) is *necessary but no longer the load-bearing differentiator* — the embedding and admission layers carry more weight.

## What this is and isn't evidence for

**Is evidence for:**

- Cost-as-wall is vendor-specific, not field-wide. Pinecone Serverless prices like cost is a wall; Turbopuffer prices like it isn't.
- The market has converged on object-storage-first / quantization-first substrate independently of Kyrja's thesis.
- GTM positioning should lead with integration, not cost.

**Is NOT evidence for:**

- Incumbents being *able to retrieve correctly* at billion scale. Affordable substrate is necessary but not sufficient. See [benchmark-replication-gap](./benchmark-replication-gap.md) and [cascading-failures](./cascading-failures.md) for the recall side.
- Every enterprise being on a cheap substrate. Pinecone Serverless and full-precision Qdrant deployments do exist; for *those* customers, cost-at-scale is a real pain. The point is field-wide, not customer-wide.
- Storage cost being irrelevant. It still bounds the cheaper-than-X comparison; it just isn't the wedge.

## Why this matters for the wedge

[tool-chain-wedge-as-adoption-path](../decision/tool-chain-wedge-as-adoption-path.md) deliberately doesn't lead on cost-at-scale — the wedge is token-savings per session, not storage cost per million vectors. The cost leg supports that choice: a token-savings pitch is novel where a substrate-cost pitch isn't.

## Related

- [benchmark-replication-gap](./benchmark-replication-gap.md) — the recall-leg counterpart; what affordable substrate doesn't fix
- [beyond-hnsw-approaches](./beyond-hnsw-approaches.md) — the five-family substrate taxonomy this finding draws on
- [RaBitQ](../source/rabitq-2024.md) — the quantization paper underneath VectorChord
- [seven-layer-stack](./seven-layer-stack.md) — the integration play that this finding strengthens

## Source archive

Anchored on the vendor-pricing probe at `incumbent-pricing-2026-04-30.md`, which priced the six scale-model scenarios against public vendor pricing as of 2026-04-30. Findings folded into [THESIS.md](../../../research/scale-model/THESIS.md) cost-leg section.

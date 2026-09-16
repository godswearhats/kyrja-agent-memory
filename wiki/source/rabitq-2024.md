---
type: source
name: "RaBitQ (SIGMOD 2024) and Extended-RaBitQ (SIGMOD 2025)"
status: timeless
last_ingested: 2026-05-17
sources: []
tags: [beyond-hnsw, quantization, billion-scale]
---

## Citation

Gao et al. *RaBitQ: Quantizing High-Dimensional Vectors with a Theoretical Error Bound.* SIGMOD 2024. arXiv:2405.12497. Plus *Extended-RaBitQ* (SIGMOD 2025).

## Location

- RaBitQ paper (arxiv): https://arxiv.org/abs/2405.12497
- Extended-RaBitQ: https://github.com/VectorDB-NTU/Extended-RaBitQ
- Official library: https://vectordb-ntu.github.io/RaBitQ-Library/
- Elasticsearch BBQ implementation: https://www.elastic.co/search-labs/blog/better-binary-quantization-lucene-elasticsearch
- Milvus integration: https://milvus.io/blog/bring-vector-compression-to-the-extreme-how-milvus-serves-3%C3%97-more-queries-with-rabitq.md

## Key claims (with our restatements)

### RaBitQ (2024)

**Paper:** Randomized quantization that compresses D-dimensional vectors into D-bit strings with a **provably sharp O(√D) error bound**. First method combining JL random rotations with vector quantization and *optimal* theoretical guarantees. 1024-dim float32 (4 KB) → ~136 bytes — ~30× compression with bounded recall loss.

**Our restatement:** RaBitQ is the first quantization scheme that is both (a) competitive on recall with the float32 baseline and (b) has formal error bounds rather than empirical-only validation. Sets the new floor for storage-cost-per-vector at billion scale.

**Construct-validity note:** Error bounds are derived under JL-rotation assumptions; real-world embeddings may violate the random-rotation assumption to a small degree. Empirical recall in vendor integrations (Elastic BBQ, Milvus, LanceDB) matches the bound within tolerance.

### Extended-RaBitQ (2025)

**Paper:** Proves the RaBitQ approach is **asymptotically optimal** — matches the Alon-Klartag lower bounds for quantization-of-high-dimensional-vectors. Configurable bit-widths:

| Bits | Recall (no re-ranking) |
|---|---|
| 4-bit | >90% |
| 5-bit | >95% |
| 7-bit | >99% |

**Our restatement:** The "extreme" compression case (1-bit, original RaBitQ) and the "high-fidelity" compression case (7-bit) are now both formally optimal. Production integrations universally use the 4-7 bit range in practice.

### Production integrations

- Elasticsearch **BBQ** (8.16+): ~95% memory reduction, 20-30× less quantization time, 2-5× faster queries vs PQ.
- Milvus: full integration; vendor claims **3× more queries served** at the same hardware.
- LanceDB: ships alongside IVF_PQ.
- VectorChord: RaBitQ + PostgreSQL = 1B+ vectors on a **single 128GB-RAM machine**.

`[ASSERTED]` from vendor-reported numbers. The VectorChord 1B-on-one-machine is the most concrete evidence that RaBitQ shifts billion-scale economics by ~order of magnitude.

### TurboQuant controversy

Google's TurboQuant (2025) claimed improvements over RaBitQ but RaBitQ authors demonstrated **flawed methodology** (A100 GPU vs single-core CPU comparison; unreproducible timings).

**Our restatement:** Important meta-observation about vendor benchmark hygiene in this space. RaBitQ remains the SOTA for billion-scale quantization as of 2026-05.

## Relevance to Kyrja

- Anchors the **quantization sub-layer** of the [tiered-storage layer](../concept/seven-layer-stack.md) of our stack. Hot-tier HNSW + RaBitQ is the canonical pattern.
- Sources [beyond-HNSW approaches](../concept/beyond-hnsw-approaches.md).
- The "1B on 128GB" VectorChord result is the load-bearing evidence that **embedding storage is no longer the binding cost constraint** at billion scale — the binding constraint is now recall (LIMIT bound) and consolidation, not storage.

## Archive location

Not currently in `library/papers/`. Fetch from arXiv / GitHub to verify configuration numbers.

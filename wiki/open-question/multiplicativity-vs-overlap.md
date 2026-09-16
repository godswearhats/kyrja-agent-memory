---
type: open-question
name: Multiplicativity vs overlap of the cascading-failures modes
status: OPEN
last_ingested: 2026-05-13
sources: [../source/weller-2025-limit.md]
epistemic_tags: [speculated, contested]
tags: [scale-thesis, recall-cascade, highest-priority-gap]
---

## The question

The [cascading-failures product](../concept/cascading-failures.md) names four recall-degradation modes (HNSW scale degradation, embedding crowding on homogeneous code, hub distortion, unreachable points from constant updates) and `[ASSERTED]` they compound *multiplicatively* to yield ~30-50% effective recall at billion scale. Do they actually multiply, or do they **overlap** such that the observed floor is set by the worst single mode rather than the product?

## Why it matters

This is the highest-priority empirical gap in the scale thesis.

- If **multiplicative**: the recall leg is load-bearing. A single-vector dense store at billion scale on homogeneous code corpora is structurally broken; the seven-layer integration story is the only response that fits.
- If **overlap-dominated**: the observed 49% recall on LongMemEval (independent third-party re-run `[MEASURED]` — see [benchmark-replication-gap](../concept/benchmark-replication-gap.md); construct-validity note: LongMemEval is a conversational-memory benchmark at <50K docs, not agentic-memory recall at billion scale) is already at or near the floor. The cascade framing overclaims; the wedge still holds but the *quantitative* recall story collapses to "one mode is bad" and the qualitative story has to be carried by other legs (volume, integration gap).
- Either outcome shapes how aggressive [precision-over-recall](../decision/precision-over-recall.md) needs to be on the wedge read path.

## What evidence would resolve it

A controlled scaling experiment isolating each mode:

1. **Mode 2 (embedding crowding) alone.** Take a homogeneous code corpus at varying scales; measure recall at fixed-precision retrieval against ground-truth nearest neighbors in the *embedding space itself* (sidesteps HNSW). If recall ≈ 60-70% across scales independent of index size, mode 2 is confirmed and decoupled from mode 1.
2. **Mode 1 (HNSW scale degradation) alone.** Same corpus, same embedding, but vary HNSW index size with sampled subsets; measure recall vs exact ANN baseline. Isolates the index-structural term.
3. **Joint measurement.** Same corpus + HNSW at full scale. If observed recall ≈ product of the isolated modes, multiplicativity is supported. If observed ≈ min(isolated modes), overlap dominates.

Modes 3 (hub distortion) and 4 (unreachable points) need separate isolations but are smaller-magnitude — likely fine to leave as a residual term once 1 and 2 are pinned down.

**Adequate signal**: a single dataset at a single billion-scale point is enough to discriminate multiplicativity from overlap, because the predicted recall differs by ~2× across the hypotheses (≈ 30-50% multiplicative vs ≈ 60-70% overlap-dominated).

## Sub-questions

- Is there a public benchmark already structured this way? LongMemEval gives a single end-to-end number; it doesn't decompose.
- Does Kerman's MASQ benchmark architecture support this decomposition? (Cross-reference [memory-benchmarks](memory-benchmarks "pending"); not yet ingested.)
- Does the answer depend on corpus homogeneity? Heterogeneous corpora may overlap-dominate even where homogeneous code multiplies.

## Related

- [cascading-failures](../concept/cascading-failures.md) — the concept this question challenges.
- [Weller 2025 LIMIT](../source/weller-2025-limit.md) — sets the mode-2 ceiling architecturally.
- [precision-over-recall](../decision/precision-over-recall.md) — design choice partially predicated on the cascade being load-bearing.
- [worst-case-source](./worst-case-source.md) — different question (write-side quality), but similar pattern: a hypothesis whose worst regime is the load-bearing untested case.
- [HNSW scale limits](../concept/hnsw-scale-limits.md) — modes 1, 3, 4 sources for the cascade.
- [embedding collapse](../concept/embedding-collapse.md) — mode 2 source for the cascade.

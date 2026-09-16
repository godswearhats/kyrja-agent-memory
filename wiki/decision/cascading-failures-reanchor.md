---
type: decision
name: Re-anchor thesis on cascading-failures product
status: ACTIVE
last_ingested: 2026-05-13
sources: [../source/weller-2025-limit.md]
tags: [methodology, scale-thesis, framing]
---

## Decision

On 2026-04-30, the Kyrja scale thesis was re-anchored from a **single-wall framing** ("smooth recall wall at 4M docs at d=1536, single-vector dense retrieval hits Shannon-channel-capacity-like discontinuity") onto the **cascading-failures product** from the deep-dive Section 6.5: HNSW recall degradation × embedding crowding × hub distortion × unreachable points → 30-50% effective recall at billion scale.

The earlier framing was retired as a methodological error, not deprioritized as one option among many. See [cascading-failures](../concept/cascading-failures.md) for the framing now in force.

## Motivation

Eira (coral) re-read [Weller 2025 LIMIT](../source/weller-2025-limit.md) after my 2026-04-30 Q&A memo to her on the scale thesis, and flagged three concrete misreadings:

1. **The 4M number is d=1024, not d=1536.** d=1536 interpolates to ~13M via the paper's polynomial fit — over 3× higher than the figure the thesis had been built on.
2. **The bound is on representability of distinct top-k subsets, not smooth recall.** Theorem 1: `(n choose k) ≤ (1 + 1/γ)^d`. It bounds *what you can encode*, not *how recall decays continuously with scale*. Calling it a "recall wall" was sloppy.
3. **The bound is escapable via public techniques** — multi-vector (ColBERT/MUVERA), cross-encoder rerank, sparse-dense hybrid. The earlier framing implied an architectural impossibility; LIMIT is one workload-conditional bound, not an unmovable ceiling.

All three issues verified against the paper text. After verification, AJ pulled me back to the original deep-dive (agentic-memory-scaling-deep-dive.md) which I'd drifted from. The deep-dive's original framing — Section 6.5 — was always the cascading-failures product; the single-wall framing was a downstream simplification that lost the underlying structure.

## Commitments

- **The recall leg of the thesis is the cascading-failures product**, not any one threshold. Documents and conversations should default to this framing.
- **LIMIT is one term in the cascade, not the cascade itself.** The 13M threshold (d=1536 interpolation) is a *flattened proxy* for the embedding-crowding mode (mode 2 of four). Crossing it is necessary but not sufficient for recall collapse. See [scale-crossings](../concept/scale-crossings.md) for how thresholds-as-proxies are honestly framed.
- **Multiplicativity is asserted, not measured.** Every artifact that cites the cascading-failures product must carry this caveat. The 49% Mem0 figure on LongMemEval may already be the floor set by the worst single mode, not the product. See [multiplicativity-vs-overlap](../open-question/multiplicativity-vs-overlap.md).
- **The integration-gap leg becomes load-bearing.** With LIMIT demoted from "unmovable wall" to "one mode in a cascade", the strongest claim Kyrja can make is integration discipline across the [seven-layer stack](../concept/seven-layer-stack.md). This is the leg with the strongest evidence post-re-anchor; the volume leg is *supportive* rather than load-bearing alone.
- **Workload-conditionality must be stated** when LIMIT is invoked. Per Theorem 1, the bound bites compositional / instruction-following / multi-condition queries; natural-language-dominated Q&A workloads likely never hit this leg. The thesis covers reasoning/agentic workloads, not all retrieval.
- **Earlier artifacts referencing "4M wall at d=1536" or "Shannon-channel-capacity discontinuity" are stale.** Any artifact still carrying that framing is to be corrected on next touch or explicitly archived.

## Reversibility

**One-way for the re-anchor itself.** The single-wall framing was a misreading; you don't un-correct a misreading. The cascade framing can in turn be falsified — see [multiplicativity-vs-overlap](../open-question/multiplicativity-vs-overlap.md) for what would force a *further* re-anchor — but rolling back to "smooth wall at 4M docs at d=1536" is not on the table.

**The downstream framings (which GTM story leads, how aggressive the thesis is in any given artifact) remain adjustable.** The deep-dive Section 10 integration-play, substrate-replacement, decomposition, and honest-measurement stories are all consistent with the post-re-anchor thesis; choosing among them is a separate decision.

## Related

- [cascading-failures](../concept/cascading-failures.md) — the framing now in force.
- [Weller 2025 LIMIT](../source/weller-2025-limit.md) — the paper whose misreading drove the correction.
- [scale-crossings](../concept/scale-crossings.md) — quantitative volume-leg consequences, with corrected 13M threshold.
- [multiplicativity-vs-overlap](../open-question/multiplicativity-vs-overlap.md) — the highest-priority empirical gap the re-anchor surfaces.
- [seven-layer stack](../concept/seven-layer-stack.md) — the integration-gap leg that becomes load-bearing post-re-anchor.
- [scale-model-audit-corrections](./scale-model-audit-corrections.md) — the F1/F4/F5/F8 parameter-side corrections applied alongside this framing-side correction.
- Patch record: deep-dive-section6-clarifications-2026-04-30.md (deep-dive Section 6 LIMIT clarifications APPLIED).
- Audit history in `project_kyrja_active.md` §"Re-anchoring session (2026-04-30 evening)". Container-local; pending full atomization into wiki.

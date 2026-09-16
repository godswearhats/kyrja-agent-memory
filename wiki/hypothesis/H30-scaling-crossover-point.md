---
type: hypothesis
name: H-SCALING-CROSSOVER — pre-filter+vector decisively beats vector-only past a crossover store size
status: PROPOSED
last_ingested: 2026-05-12
sources: []
epistemic_tags: [speculated]
tags: [structured-filter, scaling, wedge-architecture]
---

## Claim

At some memory store size (estimated 10K–100K memories for a single repo at the wedge scope), structured pre-filtering followed by vector re-ranking decisively outperforms vector-only retrieval on precision and recall jointly. Below that crossover, the structured-filter overhead is not justified by the gain. Above it, the advantage compounds with store size as semantic-collision pressure increases.

The crossover-point estimate of 10K–100K is `[SPECULATED]`. The order-of-magnitude reasoning anchors on the [benchmark-replication-gap](../concept/benchmark-replication-gap.md): incumbents already underperform on third-party replications at <50K-doc scale, which is where structured filtering should start showing its advantage.

## What would falsify it

Either of:

- **Flat curve.** Empirical measurement on a homogeneous-code corpus, varying store size (1K, 10K, 50K, 100K, 500K) while holding query distribution constant, shows the precision/recall advantage of pre-filter+vector over vector-only is flat or diminishing at scale, not growing.
- **Embedding obsoletes the filter.** A new embedding model (e.g. code-specific or multi-vector per [multi-vector retrieval](../concept/multi-vector-retrieval.md)) eliminates the semantic-collision pressure that pre-filtering exists to mitigate, making vector-only retrieval competitive even at billion scale on homogeneous code.

The second falsification path is partly addressed at small scale by [multi-vector-billion-scale](../open-question/multi-vector-billion-scale.md) — that open question asks whether ColBERT/MUVERA's small-scale escape (54% → 83.5% on LIMIT-small) preserves at billion scale.

## Evidence for

- **Theoretical:** as store size grows, the ratio of semantically similar but contextually irrelevant memories increases. Structured pre-filtering on (`repo_id`, `path`, `task_type`) removes most of this noise before semantic similarity is even computed. The advantage should scale with noise. `[SPECULATED]`.
- **Anchored on [cascading-failures](../concept/cascading-failures.md) mode 2:** the embedding-crowding mode of the cascade is exactly the noise that structured pre-filtering avoids. If cascading-failures is right, the crossover advantage is real; if cascading-failures is wrong, this hypothesis weakens.
- **Inherited from shelved H08:** the predecessor hypothesis (structured pre-filtering beats vector-only at any scale) was SUPPORTED at small scale and migrated to the [structured-filter-first](../decision/structured-filter-first.md) decision. This hypothesis is the *scale-conditional* version.

## Evidence against

- **Nobody has measured this curve empirically.** It could be flat rather than diverging. No public benchmark varies store size in the right regime on homogeneous code; see [billion-scale-benchmark-gap](../open-question/billion-scale-benchmark-gap.md).
- The crossover point might be so high (>100K per repo for tool-chain memory) that most real wedge deployments never reach it, making this a theoretical rather than practical advantage.
- Better embedding models or re-ranking architectures might close the gap that pre-filtering exists to bridge.

## Open sub-questions

- **What's the right experimental setup?** Synthetic store-size variation may not reproduce the semantic-collision patterns that make production stores noisy. A real-codebase MTP usage signal (Goal 5) would be the natural empirical vehicle, but the MTP is single-engineer scale by design.
- **Does the crossover differ by language or codebase homogeneity?** Java/Spring or TypeScript/React monorepos may hit the noise floor sooner than Rust or polyglot stacks.
- **Is the crossover a precision threshold or a recall threshold?** [precision-over-recall](../decision/precision-over-recall.md) makes the wedge prefer precision; if the crossover shows up as recall gain only, the wedge benefits less.

## Related

- [structured-filter-first](../decision/structured-filter-first.md) — the decision this hypothesis tests the scale-conditional version of
- [cascading-failures](../concept/cascading-failures.md) — mode 2 (embedding crowding) is the noise pre-filtering escapes
- [benchmark-replication-gap](../concept/benchmark-replication-gap.md) — anchors the order-of-magnitude estimate
- [multi-vector-billion-scale](../open-question/multi-vector-billion-scale.md) — adjacent: does multi-vector retrieval obsolete the filter at scale?
- Shelved predecessor: H09 in _archive

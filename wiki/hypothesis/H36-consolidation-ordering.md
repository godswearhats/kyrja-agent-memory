---
type: hypothesis
name: H-CONSOLIDATION-ORDERING — forget-first vs consolidate-first produces different results
status: PROPOSED
last_ingested: 2026-05-12
sources: []
epistemic_tags: [speculated]
tags: [consolidation, forgetting, manage-layer]
---

## Claim

The order in which forgetting and consolidation are applied to the memory store affects information loss. **Forget-then-consolidate** and **consolidate-then-forget** produce different results, and one ordering is significantly better for downstream retrieval quality.

## What would falsify it

- Empirical test shows ordering makes <1% difference on downstream retrieval quality.
- The overlap between "memories to forget" and "memories to consolidate" is negligibly small in practice, so the order doesn't matter.
- Effect size is dominated by the quality of the consolidation prompt or the forgetting formula, making the ordering question second-order.

## Evidence for

- **Intuitive argument.** If you forget first, you consolidate a smaller set, possibly losing members that would have improved the consolidated insight. If you consolidate first, you preserve more information for synthesis but may consolidate memories that should have been forgotten.
- **Analogy from data processing:** filter-before-aggregate and aggregate-before-filter produce different results when filter criteria overlap with aggregation inputs. The same compositional question arises here.

## Evidence against

- This might not matter in practice. If forgetting targets truly stale memories and consolidation targets related clusters, the overlap may be small.
- No experiments run; the hypothesis is currently theoretical.

## Open sub-questions

- **What's the metric?** "Information loss from consolidation" is hard to operationalize. Candidate: downstream retrieval quality on a held-out query set, run against both orderings on the same memory-store snapshot.
- **Does the answer generalize?** Or is the right ordering corpus-dependent — coding vs conversation vs enterprise-knowledge each having a different preference?
- **Three-way comparison.** Forget-only, consolidate-only, both-in-each-order — does the ordering effect even exist absent the underlying operations being load-bearing?

## Related

- [H34-forgetting-scores](./H34-forgetting-scores.md) — depended on (this hypothesis only matters if forgetting works)
- [admission-control](../concept/admission-control.md) — upstream sibling at the write path
- [tool-chain-wedge-as-adoption-path](../decision/tool-chain-wedge-as-adoption-path.md) — wedge defers consolidation; this is v2+ research
- Shelved predecessor: H20 in _archive

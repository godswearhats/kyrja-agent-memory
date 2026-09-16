---
type: open-question
name: Kerman 10x — what does the benchmark have to test?
status: OPEN
last_ingested: 2026-05-13
sources: [../source/weller-2025-limit.md]
epistemic_tags: [asserted, speculated]
tags: [benchmark-design, kerman-masq, integration-gap, wedge]
---

## The question

If Kerman's MASQ benchmark (or any successor) shows Kyrja "10x at the wall" on incumbents, that result is only physically informative if the benchmark tests the *right thing*. Under the [cascading-failures](../concept/cascading-failures.md) framing there is no single wall; the moat — if it exists — is integration discipline across the [seven-layer stack](../concept/seven-layer-stack.md). So:

**What does a benchmark have to measure for "10x" to actually evidence the integration-gap thesis, and what are the traps that turn a 10x number into a non-finding?**

This is distinct from [billion-scale-benchmark-gap](./billion-scale-benchmark-gap.md), which asks whether *any* billion-scale agent-memory benchmark exists. That question is upstream: even if one exists, the design choices below decide whether the result is informative.

## Why it matters

The moat candidate under cascading-failures is integration discipline, not single-layer architectural superiority. That is a thinner moat than "we have a fundamental wall nobody else has," but it can still be real if the integration is genuinely hard ([seven-layer-stack](../concept/seven-layer-stack.md) §incumbent-mapping shows zero incumbents at >2.5 of 7 layers). The benchmark is what licenses or denies the moat empirically.

A 10x result on the wrong test proves nothing. A 2x result on the right test, against an *optimised* incumbent baseline, is a stronger finding than 10x against naive defaults.

## What "10x" has to mean

**Integration-shape-dependent, not single-wall-dependent.** Under [cascading-failures](../concept/cascading-failures.md), 10x doesn't mean 10x improvement on any single mechanism. It means 10x on the *compounded effective recall* on the exposed workload regime where multiple legs of the cascade bite simultaneously.

The exposed regime, per the deep-dive synthesis (now in [cascading-failures](../concept/cascading-failures.md), [hnsw-scale-limits](../concept/hnsw-scale-limits.md), [embedding-collapse](../concept/embedding-collapse.md)):

- **Homogeneous corpus** — all-Java microservices, all-TypeScript frontends. The regime where [embedding-collapse](../concept/embedding-collapse.md) bites hardest.
- **Compositional / multi-condition / reasoning queries** — the regime where the [LIMIT bound](../source/weller-2025-limit.md) bites. NL Q&A workloads likely never bite this leg (see [query-type-axis](./query-type-axis.md)).
- **Continuous-write load** — the regime where HNSW update degradation and unreachable points accumulate.
- **Stock in the 100M–1B range** — where HNSW recall onset and LIMIT-1536d representability both engage.

A benchmark hitting all four simultaneously is the only one that tests the cascading product. Hitting one axis at a time tests the legs in isolation — useful, but not evidence for the *integration* moat.

## Two specific traps

1. **Wrong baseline: incumbent-current rather than incumbent-optimised.** `[ASSERTED]` If Cognee with naive defaults loses by 10x, that is not a moat — Cognee can re-tune. The comparison must be against the best each architecture can do with the **public escape paths wired in** (multi-vector via ColBERT/MUVERA, RaBitQ quantisation, cross-encoder rerank, sparse-dense hybrid). The integration-gap thesis is precisely that no incumbent has wired *all* of these together yet; the test must let them try.

    *Construct-validity:* this matters because Section 10 of the deep-dive (now in [seven-layer-stack](../concept/seven-layer-stack.md) §incumbent-mapping) frames the moat as integration of *known* escape paths, not invention of new ones. If the baseline doesn't include the known escapes, the test is measuring laziness, not architecture.

2. **Wrong metric: testing what the cascade doesn't bind.** Latency at 1M vectors with single-shot queries proves nothing about what 1B vectors + continuous writes + reasoning queries does to the same system. Cost at small scale is decoupled from cost at billion scale (see [cost-leg-affordable-substrate](../concept/cost-leg-affordable-substrate.md) — affordable substrate is shipped). Recall is the primary metric on third-party-replicable evaluation; cost and latency are secondary.

## What evidence would resolve it

A benchmark report from Kerman (or any team) that includes:

- **Stated exposed regime.** Explicit declaration: is this testing homogeneous code? continuous writes? compositional queries? Ideally all three together at 100M+ stock.
- **Optimised-incumbent baseline.** Each incumbent stack (Mem0, Zep, LightMem, Letta, Cognee) configured with the public escape paths integrated as a coherent stack, not just one component. Best-effort tuning, documented configuration.
- **Recall on third-party-replicable evaluation.** Not vendor-reported. Reproducibility is part of the result. The incumbent can re-run and verify.
- **Cost and latency reported but secondary.** Confirms the result isn't a recall win paid for by 100x compute.
- **Multiplicativity check** (stretch): toggle individual cascading mechanisms on/off in a single architecture. If the recall floor barely moves, the modes overlap and the integration moat is smaller than claimed (see [multiplicativity-vs-overlap](./multiplicativity-vs-overlap.md)).

## What resolution would change

- **10x on the integrated-regime test, against optimised baseline:** the integration-gap moat is real. Validates Path 1 (lab acquisition) and Path 4 (incumbent acquisition target) — both are commercial framings that live in coral, not the wiki.
- **2–3x on the integrated-regime test:** the moat is real but thinner than the strongest framing. Strategic implication shifts toward integration-as-product rather than integration-as-acquisition-bait.
- **No statistically significant difference on the integrated-regime test:** the integration-gap thesis fails. Falls back to the write-side wedge ([write-side-quality-gate-deferrable](../decision/write-side-quality-gate-deferrable.md), [slot-format-encoding](../decision/slot-format-encoding.md)) which doesn't depend on integration superiority.
- **10x on a single-axis test:** uninformative regarding the cascade. May indicate one leg is unusually strong (e.g. our admission control beats Mem0's lack of one) but says nothing about whether the legs compound.

## Sub-questions

- **Whose corpus hosts this benchmark in practice?** AJ's multi-year session logs are the only candidate currently in the team's reach; insufficient for 100M+ but potentially viable for a precursor at 10M–100M with the right *shape* (homogeneous, continuous-write, decision-relevant).
- **Is a precursor benchmark at 10M–100M scale with the right shape sufficient to discriminate architectures?** May be — the cascading mechanisms engage at different volume thresholds; a 100M-scale test with homogeneous code + reasoning queries + continuous writes already hits HNSW recall onset, embedding collapse, and unreachable points simultaneously even if LIMIT representability hasn't engaged.
- **Does MASQ's current scope meet these criteria?** Cross-reference . If MASQ is conversational-scale only, the spec above is something the team would need to extend.

## Related

- [billion-scale-benchmark-gap](./billion-scale-benchmark-gap.md) — upstream: does any billion-scale benchmark exist at all?
- [multiplicativity-vs-overlap](./multiplicativity-vs-overlap.md) — the structural question this benchmark could partially answer.
- [cascading-failures](../concept/cascading-failures.md) — the thesis under test.
- [seven-layer-stack](../concept/seven-layer-stack.md) §incumbent-mapping — what "optimised baseline" would have to include.
- [query-type-axis](./query-type-axis.md) — why the workload selection matters.
- Eira six-questions doc (2026-04-30) §B1 — origin of this question.

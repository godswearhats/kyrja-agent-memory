---
type: open-question
name: No billion-scale agent-memory benchmark exists
status: OPEN
last_ingested: 2026-06-07
sources: [../source/memory-surveys-2026.md]
epistemic_tags: [asserted, speculated]
tags: [benchmark-gap, masq-relevant, integration-gap]
---

## The question

**No public benchmark exists for agent memory at billion scale.** Existing benchmarks (LoCoMo, LongMemEval, DMR, BEAM, MemoryArena) operate at conversation scale — thousands to tens of thousands of memories per agent. The [cascading-failures product](../concept/cascading-failures.md) and the [LIMIT bound](../source/weller-2025-limit.md) make their structural claims at billion scale, where no benchmark replicates the regime.

So: **what would a billion-scale agent-memory benchmark look like, and what is the minimum-viable version that can discriminate between competing architectures?**

## Why it matters

Deep-dive §11 Q16 flags this. Three reasons it's load-bearing:

1. **The thesis cannot be empirically supported without it.** Our entire scale-side argument rests on extrapolation from the LIMIT paper and from conversational-scale benchmark behavior. We say "billion-scale will break" — but no public benchmark proves or refutes it.
2. **Benchmark chaos at conversation scale already exists.** The Mem0 49% (independent) vs 93% (vendor) discrepancy on LongMemEval (see [Mem0 incumbent](../incumbent/mem0.md)) shows that even the existing benchmarks aren't honestly comparable. Scaling up amplifies the problem.
3. **Kerman's MASQ work is the team's bet on closing this gap.** Whatever MASQ does or doesn't measure shapes which of our thesis claims become testable.

## What evidence would resolve it

A benchmark must include:

- **Scale.** 100M-1B+ memories. The number where the cascading-failures product is predicted to materialize.
- **Homogeneity.** Corpora structured like agentic memory in practice: heavily code, with high keyword/structural similarity across memories.
- **Continuous-write profile.** Memories arrive over time; the index must handle ingest concurrent with retrieval (the worst case for [HNSW update degradation](../concept/hnsw-scale-limits.md#update-degradation)).
- **Decision-relevant retrieval.** Not just "did we recall this fact" but "did the recalled memory change the agent's action in a measurable way" — distinguishing passive recall from decision-relevant memory use (MemoryArena's recent ~40-60% pluck-from-passive-to-decision-relevant drop is the right framing).
- **Construct validity for the wedge regime.** Tool-chain memory specifically — not general "agent memory" abstracted away from the read/write pattern.

## Sub-questions

- **Does Kerman's MASQ architecture meet these criteria?** ~~Cross-reference . MASQ's exact scope is the relevant input here; if MASQ is conversational-scale only, the gap remains.~~ **Answered 2026-06-07:** MASQ's scope is now pinned — it is a conversational-scale **multi-party attribution** benchmark (~224K-token synthetic corpus + planned real-corpus condition), being developed into an independent benchmark paper ([decision/masq-paper-as-active-program](../decision/masq-paper-as-active-program.md)). So **the billion-scale gap remains open** — MASQ does not close this question. What MASQ *does* address is reason 2 above (benchmark chaos / vendors grading their own homework): independent authorship, pinned harness, deterministic attribution scoring.
- **Is there value in a small precursor benchmark before the billion-scale version?** A 10M-100M-scale benchmark with the right *shape* (homogeneous, continuous-write, decision-relevant) may discriminate architectures even if it doesn't directly test billion-scale claims.
- **Can synthetic-corpus generation produce a meaningful billion-scale benchmark cheaply?** Probably not — the homogeneity property is hard to synthesize without inducing artifacts that break the comparison.
- **Whose corpus could host this benchmark in practice?** AJ's own multi-year session logs are the only candidate currently in the team's reach; insufficient for billion-scale but useful for the precursor.

## What resolution would change

- If a benchmark exists and we can run incumbents on it: most of the [cascading-failures product](../concept/cascading-failures.md) becomes empirically testable, not asserted.
- If the benchmark shows incumbents already at <50% recall at 100M scale: the [multiplicativity-vs-overlap](./multiplicativity-vs-overlap.md) question gets a partial answer (overlap-dominated would be the conclusion).
- If the benchmark shows incumbents holding up better than expected: the wedge thesis pivots — the scale-side argument weakens, the integration-gap and write-side-quality-gate arguments do more work.

## Related

- [Memory-system surveys (2026)](../source/memory-surveys-2026.md) — confirms the gap; "Memory for Autonomous LLM Agents" lists "memory at scale" and "memory evaluation" as two of nine open challenges.
- [Cascading-failures product](../concept/cascading-failures.md) — what the benchmark would test.
- [Multiplicativity vs overlap](./multiplicativity-vs-overlap.md) — adjacent question; a benchmark could answer both simultaneously.
- [Kerman 10x test design](./kerman-10x-test-design.md) — downstream: given a benchmark, what does "10x" have to measure for the integration-gap thesis to be evidenced?
- [Mem0 incumbent](../incumbent/mem0.md) — example of the existing benchmark-chaos problem (49% vs 93%).
- Kerman's MASQ benchmark work at .

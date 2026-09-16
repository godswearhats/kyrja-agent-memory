---
type: open-question
name: Query-type axis in the scale model
status: OPEN
last_ingested: 2026-05-12
sources: [../source/weller-2025-limit.md]
epistemic_tags: [asserted]
tags: [scale-model, limit-bound, workload-conditional]
---

## The question

The scale model treats all stored stock as if every query draws from the [LIMIT-bound](../source/weller-2025-limit.md) combinatorial regime. In reality, the LIMIT bound — `(n choose k) ≤ (1 + 1/γ)^d`, Theorem 1 — applies to *representability of compositional / instruction / multi-condition queries*, not to smooth recall on natural-language-dominated workloads. Glean-shape Q&A workloads likely never bite this leg of the cascade; reasoning, instruction-following, and multi-condition queries are the exposed regime.

So: **what does the scale model look like with a query-type axis, and which scenarios change qualitatively when LIMIT-pressure is conditioned on workload mix?**

## Why it matters

- **Overstates impact for NL-dominated workloads.** A Glean-shape enterprise search tool may serve millions of users with no exposure to the LIMIT bound, because its queries are natural-language semantic-similarity, not compositional. The current scale model says these deployments cross LIMIT-1536d at year T; the workload-conditional reading says they don't cross meaningfully at all.
- **May understate impact for reasoning workloads.** Multi-step reasoning agents, code agents combining file/symbol/task-type filters, and instruction-following agents producing structured queries are all in the LIMIT-exposed regime. The current scale model may *understate* the recall risk for these workloads because it doesn't separate them from NL-dominated traffic.
- **Goes-to-market sensitivity.** "Kyrja wins on reasoning/coding workloads, doesn't matter for Q&A" is a different positioning than "Kyrja wins on everything past 13M vectors." The query-type axis distinguishes these.
- **Flagged by [THESIS.md](../../../research/scale-model/THESIS.md)** (open question #5) as **the next structural change to the scale model**.

## What evidence would resolve it

- A workload-conditional version of the scale model with at least three query-type bins (NL Q&A, multi-condition retrieval, compositional/instruction). Each bin gets its own LIMIT exposure and recall projection.
- Production query-mix data from at least one incumbent agentic-memory deployment, broken out by query type. *Not currently public for any vendor.*
- An empirical anchor for the bound: a benchmark that holds corpus size constant and varies query compositionality, measuring recall under each. *No such benchmark exists; the LIMIT paper itself is the closest.*

## What would close this

Promotion to a hypothesis (`H-WORKLOAD-CONDITIONAL` or similar) with a falsifiable form:

> *Single-vector dense recall on a fixed homogeneous-code corpus degrades faster as query compositionality increases (measured by k in the (n choose k) bound), with the degradation rate matching the LIMIT polynomial.*

This is in scope for the scale-model rebuild but not yet specified.

## Related

- [cascading-failures](../concept/cascading-failures.md) — the recall thesis this question conditions
- [scale-crossings](../concept/scale-crossings.md) — currently mentions this caveat in passing; should link here
- [Weller 2025 LIMIT](../source/weller-2025-limit.md) — the workload-conditional bound itself
- [billion-scale-benchmark-gap](./billion-scale-benchmark-gap.md) — adjacent measurement gap; this question would change what a billion-scale benchmark needs to measure

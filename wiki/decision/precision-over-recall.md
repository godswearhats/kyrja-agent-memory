---
type: decision
name: Precision Over Recall
status: ACTIVE
last_ingested: 2026-06-30
sources: [../experiment/2026-05-11-write-quality-variance.md]
tags: [wedge, retrieval, cost-asymmetry]
---

## Decision

The read path is tuned for **precision over recall**. The retrieval system must be willing to inject *nothing* when no high-confidence match exists. The injection threshold is a first-class system parameter.

## Motivation

**Cost asymmetry inverts the usual RAG tuning.** Phase 2 (and subsequent write-quality experiments) measured:

- Relevant memory: **−50% cost** on a causally-related task `[MEASURED]` ([source](../experiment/2026-05-11-write-quality-variance/README.md)).
- Irrelevant memory: **+50% cost** on an unrelated task `[MEASURED]` (Phase 2 Tier 3; same [source archive](../experiment/2026-05-11-write-quality-variance/README.md)).

*Construct-validity (applies to both bullets):* cost measured as agent-completion token spend, which directly captures the wedge's promised benefit. Magnitudes are model-version- and task-dependent; direction is stable across both write-quality experiments.

Reward and penalty are roughly symmetric. Recall-tuned retrieval (return-more, let the LLM filter) is therefore strictly worse than precision-tuned retrieval (return-fewer, return-nothing-if-unsure) in expectation, because the LLM-filter step is itself expensive *and* the +50% penalty is paid whenever a wrong injection slips through.

**Independent (construct-limited) anchor — the "let the LLM filter" step fails outright on confusable entities.** On the synthetic MASQ benchmark, similarity-ranking arms had *high recall* of the target (~2.8/3) but flooded the context with ~5.5 equally-relevant sibling chains, and the reader could **not** filter them — B-pass floored at 6–8/15 vs 15/15 for a structured filter that simply excluded the siblings `[MEASURED]` ([MASQ retrieval arms](../experiment/2026-06-30-masq-retrieval-arms.md), [H45](../hypothesis/H45-exclusion-over-recall.md)). This is precision-over-recall as a *hard* result: extra recall was not free for the LLM to sort out — it actively poisoned the decision. *Construct-validity / scope:* MASQ constructs the confusability and the filter is an oracle; this demonstrates the mechanism, it does not measure the real-corpus cost asymmetry the rest of this page rests on.

## Commitments

- Injection threshold is a tuned, first-class parameter — not a constant in code.
- System must support "no memory injected" as a normal output, not an error or fallback.
- Quality of the precision tuning is evaluated against `cost_with_memory(injected) vs cost_without_memory(counterfactual)`, **not** against retrieval-style `recall@k` metrics.

## Reversibility

**Cheap.** Threshold tuning. Could be relaxed without architectural change. But: relaxing re-exposes the system to the +50% penalty on false-positive injections, which was the empirical anchor for this decision in the first place.

## Related

- [repo-bounded-scope](./repo-bounded-scope.md) — narrows the candidate set before precision tuning applies
- [structured-filter-first](./structured-filter-first.md) — what produces the candidate set the threshold filters
- [Exp 1 + Exp 2 write-quality variance](../experiment/2026-05-11-write-quality-variance/README.md) — confirms direction stable; magnitudes drift
- [cascading-failures](../concept/cascading-failures.md) — recall ceiling that motivates *not* fighting for higher recall
- [MASQ retrieval arms](../experiment/2026-06-30-masq-retrieval-arms.md) / [H45](../hypothesis/H45-exclusion-over-recall.md) — high-recall flooding poisons the decision; exclusion beats recall (construct-limited)

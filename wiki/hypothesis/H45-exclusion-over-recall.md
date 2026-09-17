---
type: hypothesis
name: H45 — exclusion over recall; structured scope-filter beats any similarity ranking on confusable-entity disambiguation
status: SUPPORTED
last_ingested: 2026-06-30
sources: [../experiment/2026-06-30-masq-retrieval-arms.md]
epistemic_tags: [measured]
tags: [masq, retrieval, scope-disambiguation, precision, structured-filter, v2]
---

## Claim

When a memory store contains **confusable entities** — several near-identical scopes
that are equally content-relevant to a query (as MASQ constructs: five `checkout-*`
services each with its own change history) — a **structured filter** on the scope key
(`WHERE scope=target`) is *sufficient* to reach oracle decision accuracy, while
**similarity ranking** (semantic or lexical, any method, any k) *cannot* exclude the
confusable siblings and floors at or below a paste-everything baseline. The binding
constraint is **exclusion (precision), not recall**: ranking retrieves the target fine
but cannot leave the siblings out, because the query offers no content signal that
separates them.

> **FALSIFIED 2026-09-16/17 — the parenthetical "any method, any k" and the stated
> mechanism are both wrong.** The claim above was asserted from two retrievers at one
> k with one query formulation and no ablation. The target scope is in fact **verbatim
> in `a_query` on 15/15 cores**; the published arms destroyed that signal through
> (a) `[a-z0-9]+` tokenization, which splits `checkout-web` so every sibling collides
> on the shared prefix, and (b) retrieving with the full ~63-word task prompt, which
> dilutes the discriminator to ~20% of the BM25 document score. Fixing both — no
> ground-truth field read — gives top-10 composition of 3.4/3.4 target and **0.2**
> siblings, and on a pre-registered re-run scores **14/15 B-pass**, effectively tying
> the oracle filter (15/15) and clearing the plateau (paste 9/15, control bm25 9/15).
> Paired 5 FAIL→PASS, 0 PASS→FAIL. See
> [PREREG](../../masq/harness/PREREG-scoped-bm25.md) and
> [RESULTS](../../masq/harness/RESULTS-scoped-bm25.md).
>
> **Corrected claim:** a discriminator present in the query must not be diluted by
> tokenization or prompt boilerplate. Ranking is sufficient here once it isn't. What
> remains genuinely untested is scope that must be **inferred** from unanchored
> natural language — not "the filter is an oracle", which a 10-line regex-plus-
> substring filter reproduces exactly on 15/15 cores.

**Status SUPPORTED is scoped to the MASQ construct** (synthetic, confusability authored
by design, n=15, one size, one reader). It is *not* a validated general claim about
real-corpus retrieval — see Scope/construct limits.

## What would falsify it

- A similarity-ranking arm (better encoder, hybrid RRF, re-ranker, learned router) that lands **strictly above the paste baseline** on MASQ would falsify "ranking floors."
- A scope-filter arm that **fails to reach ceiling** on seed-expanded N would falsify "filter is sufficient."
- A **real-corpus** replication where similarity ranking suffices would bound the claim to synthetic, by-construction confusability (expected boundary, not yet tested).

## Evidence for

- **MASQ ladder, 60k, n=15** `[MEASURED]` ([experiment](../experiment/2026-06-30-masq-retrieval-arms.md)): scopefilter 15/15 (ties oracle ceiling); vector 6/15, bm25 8/15, paste 9/15. Paired: scopefilter > vector/bm25/paste with **zero losses** (p=0.004 / 0.016 / 0.031). *Construct-validity:* B-pass = correct action + correct conflict flag, closed-form; the decision the benchmark targets. Confusability is constructed, so the *direction* is partly by-design; the non-trivial measured parts are below.
- **Exclusion ≠ recall** `[MEASURED]` (same experiment): both retrievers recall ~2.8/3 target sessions and rank one #1 in 10–11/15 cores, yet flood top-10 with ~5.5 sibling chains. Retrieval finds the target; it cannot drop the siblings. *Construct-validity:* composition measured directly on the retrieved set, no reader involved.
- **Reader is not the bottleneck** `[MEASURED]` (same experiment): scopefilter ties ceiling **without** ceiling's resolution-type labels (mean A 0.79 vs 0.97, identical B 15/15). Given a scope-pure raw chain the reader resolves the conflict itself; the entire gap is retrieval-side.
- **Method-equivalence** `[MEASURED]` (same experiment): bm25 ≈ vector (8 vs 6, CIs overlap), independently replicating [Thread 5](../experiment/2026-04-17-thread5-retrieval-comparison/README.md). The lever is filter-vs-rank, not which ranker. *Construct-validity:* same closed-form B-pass grader; "equivalence" is CI-overlap at n=15, not a proven null.

## Evidence against

- None within MASQ so far. **The standing risk is external validity, not internal contradiction:** the result could be an artifact of constructed confusability and fail to reproduce where confusability is natural. Flagged, not yet tested.

## Scope / construct limits

- **Synthetic, single construct.** Confusability is authored. The claim is about *this failure mode*, demonstrated cleanly — not a general retrieval verdict.
- **Oracle filter.** `scopefilter` consumes the ground-truth scope tag; it bounds the achievable, it is not a deployable system. Whether a real system recovers that filter is [an open question](../open-question/structured-memory-auto-scope-index.md).
- **n=15, one size, one reader** (Opus 4.8). Seeds (not sizes) are the power axis.
- Do not promote this to "structured-filter-first is validated as production architecture." It strengthens that decision's *motivation*; real-corpus evidence is separate and unrun.

## Open sub-questions

- Does a real structured/graph memory auto-build the scope index, or smear scopes like embeddings? → [structured-memory-auto-scope-index](../open-question/structured-memory-auto-scope-index.md).
- Does the floor hold under seed expansion and a second reader model?
- Where is the natural-confusability boundary — at what entity-similarity does ranking stop excluding?

## Related

- [experiment 2026-06-30 MASQ retrieval arms](../experiment/2026-06-30-masq-retrieval-arms.md) — the supporting run
- [structured-filter-first](../decision/structured-filter-first.md) — the architectural decision this (construct-limited) result motivates
- [precision-over-recall](../decision/precision-over-recall.md) — exclusion-is-the-bottleneck stated as a tuning decision
- [H33-routing-matters](../hypothesis/H33-routing-matters.md) — method-equivalence is shared evidence
- [cascading-failures](../concept/cascading-failures.md) — embedding-crowding is the mechanism behind the sibling flood

---
type: experiment
name: Thread 5 retrieval-tier comparison (2026-04-17) — BM25 vs semantic vs hybrid at small scale
status: LANDED
last_ingested: 2026-05-13
sources: []
epistemic_tags: [measured]
tags: [retrieval, bm25, semantic, hybrid, ceiling-effect, archive]
---

## What this is

Pilot study run during the Kyrja-1 research arc (shelved 2026-04-21). The experiment compared four retrieval tiers — no memory, BM25, semantic embedding, BM25+semantic hybrid (RRF fusion) — against a fixed encoding strategy on 2,920 tool-call chains extracted from 804 real Claude Code sessions. The findings get cited by [structured-filter-first](../../decision/structured-filter-first.md) as evidence that retrieval method barely moves the needle at small scale, which is why the wedge prioritizes encoding quality and structured filters over retrieval-method optimization. Original artifact at `findings.md`; this is the wiki-side promotion.

## Method

- **Data:** 2,920 tool-call chains from 804 Claude Code sessions. Each chain encoded once via Haiku using the Thread-1 "intent+outcome" strategy. Synthetic retrieval query generated per chain via Haiku.
- **Ground truth:** Answers generated from full chain context via `gemma3:12b`.
- **Retrieval tiers (same 2,920 memories, different search methods):**
  - **T0** — no memory (question only).
  - **T1** — BM25 keyword matching.
  - **T2** — semantic embedding via `nomic-embed-text`.
  - **T3** — hybrid BM25 + embedding with RRF fusion.
- **Evaluation:** Top-3 memories retrieved per query. Haiku answers the question given retrieved memories. Scored on F1 token overlap and LLM-as-judge (Haiku, CORRECT/PARTIAL/WRONG).
- **Scale:** 2,920 queries × 4 tiers = 11,680 QA evaluations + 11,680 judge evaluations.

## Results

### Hit rates (correct memory in top 3)

| Tier | Hit rate |
|------|----------|
| T1 (BM25) | 48.3% |
| T2 (semantic) | 45.2% |
| T3 (hybrid) | 52.4% |

`[MEASURED]` retrieval hit rates from the run. The three tiers are roughly equivalent — BM25 and hybrid bracket semantic within a few percentage points. *Construct-validity:* "hit rate" is top-3 retrieval accuracy against a synthetic-query held-out set. It approximates but does not equal end-to-end retrieval utility for a downstream wedge task — a retrieved-correct memory may not improve the answer, and a retrieved-wrong memory may still help via partial overlap.

### F1 token overlap and LLM-judge

`[MEASURED]` retrieval method barely moves downstream F1 (T1=0.229, T2=0.228, T3=0.232) and barely moves LLM-judge correctness (T1=0.9%, T2=0.9%, T3=1.1%). The big jump is T0 → T1 (no-memory vs any-memory: F1 +0.08, p≈1.000). Above that floor, retrieval-method differences are within noise. *Construct-validity:* Haiku is both encoder and answerer in this design — encoder-quality ceiling and answerer-capacity ceiling are confounded with retrieval-tier differences. Stronger answerer or stronger encoder would likely shift absolute numbers; the relative rank of tiers is the load-bearing finding.

## Findings

- **Retrieval method is not the binding constraint at small scale.** BM25 ≈ semantic ≈ hybrid on hit rate and downstream answer quality. The pre-pilot hypothesis (H2: retrieval quality caps encoding's downstream ceiling) was *not* supported at this scale.
- **Encoding presence beats retrieval method.** T0 → T1 is the big delta; T1 → T3 is noise. This is what [structured-filter-first](../../decision/structured-filter-first.md) cites: in a regime where the structured filter already narrows the candidate set, retrieval method is fungible.
- **Absolute quality is low across all tiers.** LLM-judge correct rates of 1–2% indicate the task itself is hard or the answerer/encoder is too weak; the comparison is *relative*, not absolute. This is part of why Thread 5 was reframed and the broader research arc shelved.

## Construct-validity caveats

1. **Same-model encoder + answerer (Haiku).** Confounds capacity ceilings with retrieval-tier effects. A stronger answerer might reveal larger retrieval-tier separation.
2. **Synthetic queries.** Each query was Haiku-generated from the source chain; real user queries may distribute differently and produce different hit-rate orderings.
3. **One encoding strategy (intent+outcome).** Other encoding shapes might interact with retrieval method differently; this experiment fixed encoding and varied retrieval.
4. **Small scale relative to production.** 2,920 chains is far below the F5 × F4 × N projections in the scale model. The "BM25 ≈ semantic" finding may not survive at the regimes where [Weller 2025 LIMIT](../../source/weller-2025-limit.md) compression effects kick in.

## Relevance to Kyrja

- Empirical anchor for [structured-filter-first](../../decision/structured-filter-first.md): retrieval method is fungible when the structured filter dominates.
- Complement to [Weller 2025 LIMIT](../../source/weller-2025-limit.md): LIMIT bounds the *high-scale* recall ceiling; this experiment shows the *low-scale* regime where ceilings haven't bound yet and method choice is noise.
- Historical context: part of the Kyrja-1 research arc shelved 2026-04-21 when the wedge was reframed.

## Re-running

To re-run: the original code, data, and outputs are at `thread5`. Treat any rerun as a new dated experiment, not an update to this page.

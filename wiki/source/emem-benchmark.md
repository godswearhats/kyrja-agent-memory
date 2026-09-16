---
type: source
name: "EMem benchmark — episodic-memory evaluation suite for agent systems"
status: timeless
last_ingested: 2026-05-17
sources: []
tags: [benchmark, episodic-memory, agent-eval, edus, pending-verbatim-read]
---

## Citation

EMem benchmark — episodic-memory evaluation for agent systems. Cited in the Kyrja scale-model audit as the closest empirically-anchored reference point for the F5 parameter (memories generated per session, measured in EDUs — Episodic Document Units).

## Location

- arXiv: search at https://arxiv.org/search/?query=EMem+episodic+memory+benchmark (canonical arXiv ID pending verbatim read)
- HuggingFace / GitHub release for the suite (pending verification)

## Key claims (with our restatements)

### EDUs per session

**Benchmark:** EMem reports a working magnitude of **18–20 EDUs per session** for the synthetic episodic-memory workloads in its evaluation suite.

**Our restatement:** `[ASSERTED]` from the cited magnitude as it appears in the [scale-model-audit-corrections](../decision/scale-model-audit-corrections.md) summary, and in the surrounding deep-dive notes. *Construct-validity:* "EDU per session" is a synthetic-benchmark unit, not a production-traffic measurement. Mapping EMem's EDU count to Kyrja's F5 (production memories per agent session) assumes the EDU-to-memory granularity is comparable, which is a Kyrja-internal extrapolation, not a benchmark-validated claim.

## Construct-validity caveats

1. **Not read verbatim.** All magnitudes and methodology details on this page are paraphrased from prior summaries / the scale-model audit notes, not from a verbatim read of the EMem paper or benchmark documentation. arXiv ID is intentionally not filled until that read happens.
2. **Synthetic, not production.** EMem is a synthetic episodic-memory benchmark. Production memory-per-session distributions for real agent systems are not the same population; using EMem's 18–20 EDU as a population central for F5 is a *closest available proxy*, not a like-for-like measurement.
3. **Vendor-blind on production data.** The scale audit explicitly notes that **no vendor publishes production memories-per-session** (audited Cognee, Mem0, Letta, Zep, LangMem, MemGPT). This is why EMem is the anchor; it doesn't mean EMem is the right anchor for production traffic.

## Relevance to Kyrja

- Closest empirical reference for F5 in [scale-model-audit-corrections](../decision/scale-model-audit-corrections.md) — the audit nudged F5 central from 9 → 12 partly on indirect signals including EMem.
- Open gap tracked in [f5-production-data](../open-question/f5-production-data.md): replacing EMem with real production-traffic data remains a medium-priority anchor improvement.

## Archive location

Not in `library/papers/`. Fetch from arXiv (ID pending) for verbatim verification before any load-bearing claim on this page is upgraded from *ASSERTED* to *MEASURED*.

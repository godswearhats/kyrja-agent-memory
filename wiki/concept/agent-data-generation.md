---
type: concept
name: Agent Data Generation
status: timeless
last_ingested: 2026-05-14
sources: [../source/memory-surveys-2026.md]
epistemic_tags: [speculated]
tags: [scale-thesis, volume-leg, agent-sessions, ephemeral-data]
---

## Definition

**Agent data generation** is the rate and shape of data produced by agentic AI sessions. It is the upstream of every scale-side claim in the thesis: the volume crossings, the cascading-failures regime onset timing, and the [F5 memories-per-session](../open-question/f5-production-data.md) parameter all derive from this.

## Anatomy of a single agentic coding session

`[SPECULATED]` — Kyrja-internal synthesis from informal observation of Claude Code, Cursor, and Copilot sessions, plus public vendor reporting. **Not** from formal session-log telemetry, and **not** from any external paper that publishes these ranges. The deep-dive (`_archive/atomized-2026-05-12/agentic-memory-scaling-deep-dive.md` §2, lines 110-149) was where this synthesis was first written down, but it cites no external study — these numbers are observation-driven conjecture pending real telemetry.

When a user says "fix this bug in service X," the agent typically performs:

1. **Orientation (search + read).** 5-20 glob/find searches; 10-30 greps; reads 10-50 files (often re-reading); reads git history; reads tests, CI, package metadata.
2. **Planning + reasoning.** Thousands of tokens of chain-of-thought per decision point.
3. **Implementation (iterative).** 3-10 edit-test-debug cycles per fix.
4. **Verification + cleanup.** Full test suite, diff review, commit + PR.

## Data volume per session

| Activity | Volume | Persisted? |
|---|---|---|
| File reads (search + context) | 50K-500K tokens | No (flows through LLM context) |
| Extended thinking / reasoning | 10K-100K tokens | No (ephemeral) |
| Tool calls + results | 20K-200K tokens | No (ephemeral) |
| Test/lint/build output consumed | 10K-100K tokens | No (ephemeral) |
| Code actually written/changed | 50-500 lines | Yes |
| Commit messages, PR descriptions | 100-1,000 words | Yes |
| CI runs triggered | 10K-100K lines of logs | Yes (in CI system) |
| Conversations/transcripts | 5K-50K tokens | Sometimes (if logged) |

**Key ratio: for every 100 lines of persisted code, the agent generates 100K-500K tokens of *ephemeral* data.** This is the central number for the [F5 open-question](../open-question/f5-production-data.md) and for the scale-thesis volume leg.

## The four multipliers

1. **Parallelism.** Developers run 3-5 agents simultaneously. Claude Code supports background agents. Orchestration layers dispatch dozens concurrently.
2. **Autonomy loops.** Coding agent → review agent → fix agent → test agent → docs agent. Each loop iteration generates more data than a single session.
3. **Speculative execution.** Some teams run agents on every incoming issue to triage/repro/fix before a human looks. Most of this work is thrown away — but if it's indexed, the volume is real.
4. **Continuous agents.** 24/7 monitoring, PR review, doc-syncing.

## Data generation model (500-person company, 200 engineers)

`[SPECULATED]` — Kyrja-internal projections. Not vendor-reported telemetry; not published in any external study. Treat as a sizing scenario rather than evidence.

| Metric | Conservative | Aggressive |
|---|---|---|
| Agent sessions per developer per day | 5-10 | 20-50 |
| Total agent sessions per day | 1K-2K | 4K-10K |
| Persisted artifacts per session | ~5K tokens | ~10K tokens |
| New persisted tokens per day | 5M-10M | 40M-100M |
| New chunks per day (for RAG) | 10K-20K | 80K-200K |
| New vectors per month | 300K-600K | 2.4M-6M |
| New vectors per year (aggressive) | ~30-70M | From agent activity alone |

## Corpus inflation by source

`[SPECULATED]` — Kyrja-internal multiplier estimates from the deep-dive's §1 table. Each multiplier is a directional conjecture, not a measured ratio:

| Source | Pre-agentic | Post-agentic | Multiplier |
|---|---|---|---|
| Source code | Baseline | 2-4× more code | ~3× |
| PRs, commits, reviews | Baseline | More verbose | ~1.5-2× |
| Design docs, ADRs, RFCs | Often skipped | AI makes cheap | ~3-5× |
| Internal docs (runbooks, wikis) | Sparse, stale | Auto-updated | ~2-4× |
| Support tickets + KB | Baseline | Auto-drafted | ~2× |
| Meeting transcripts | Rarely stored | Routine | ~5-10× (net new) |
| Chat/Slack | Existed, not indexed | Increasingly indexed | ~1.5-2× |
| Tests, CI logs | Baseline | Verbose | ~2-3× |

## Corpus size by year (500-person knowledge-work company)

`[SPECULATED]` — Kyrja-internal projection. The yearly vector-count trajectory is the multiplier-table propagated forward; no external corpus survey supports the specific numbers.

| Year | Context | Vector count |
|---|---|---|
| 2023 (pre-agentic) | Human-generated code + docs | ~2M |
| Mid-2026 (current) | AI-assisted, persisted only | ~6-10M |
| End-2027 (multi-agent + CI logs + PR chains) | Agent proliferation | ~30-80M |
| 2028+ (session logs, reasoning traces) | Agent traces indexed | 200M-500M+ |

The jump from 2027 → 2028 is **conditional on the choice to index ephemeral data**, which is the key question raised in deep-dive §2 (see below).

## The key indexing question

`[SPECULATED]` (deep-dive §2 end). Ephemeral data contains enormous signal:

- "We tried approach X and it failed because Y" — institutional knowledge.
- "The test failed with this error, which meant Z" — debugging context.
- "We read these 40 files to understand the auth flow" — implicit architecture map.

**If companies persist and index agent session logs, that's a 10-50× multiplier on top of the already inflated corpus.** This is the scenario that pushes a mid-size company from tens of millions to billions of vectors.

The wedge product's [structured filter-first decision](../decision/structured-filter-first.md) is partially predicated on **not** indexing ephemeral data as primary memory — instead, distill it (via the slot-format encoding shown in [Exp 1 + Exp 2](../experiment/2026-05-11-write-quality-variance/README.md)) into much smaller persisted memories. This sidesteps the 10-50× ephemeral-multiplier while capturing the institutional-knowledge signal.

**What to distill from the ephemeral stream is an open design question.** [H38 — rationale-trace-memory](../hypothesis/H38-rationale-trace-memory.md) proposes distilling the `Thought` tokens from ReAct-style trajectories specifically, on the grounds that *why* a step was taken transfers across tasks better than *what* was done. The falsifier is CoT-faithfulness — if stored rationales are post-hoc confabulation rather than faithful traces, the distillation target poisons the memory store rather than enriching it.

## Role in Kyrja thesis

- Upstream of the **volume leg**. See [scale crossings](./scale-crossings.md) for the threshold-crossing analysis; this page sources the *rate* numbers that feed the crossings.
- Anchor for the [F5 memories-per-session open-question](../open-question/f5-production-data.md) — the single biggest data gap in the scale model.
- Frames why the wedge product distills ephemeral → persistent rather than indexing ephemeral directly.

## Related

- [Scale crossings](./scale-crossings.md) — the downstream synthesis.
- [F5 — memories per session](../open-question/f5-production-data.md) — the load-bearing parameter this concept sources.
- [Cascading-failures product](./cascading-failures.md) — what happens when the corpus crosses billion-scale.
- [Structured filter first](../decision/structured-filter-first.md) — the distill-don't-index decision predicated on this concept.
- [Exp 1 + Exp 2](../experiment/2026-05-11-write-quality-variance/README.md) — slot-format encoding makes the distillation economical.

## Source archive

Concept synthesized from deep-dive §2 (agentic-memory-scaling-deep-dive.md, lines 108-182) and §1 corpus-inflation table.

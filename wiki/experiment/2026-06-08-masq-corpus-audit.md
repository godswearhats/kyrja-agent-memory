---
type: experiment
name: MASQ corpus + apparatus audit (2026-06-08)
status: DONE
program: masq-bench
last_ingested: 2026-06-08
sources: [../source/he-2026-memoryarena.md, ../source/du-2026-autonomous-memory-survey.md]
epistemic_tags: [MEASURED]
tags: [masq, benchmark, corpus-audit, statistical-power, apparatus]
---

Audit of the existing MASQ artifact before any consolidation, triggered by the reframe toward a statistically-defensible benchmark. Two orthogonal gaps surfaced: (1) the synthetic corpus has too few *independent* distinctive events to support subgroup statistical claims, and (2) the current measurement apparatus produces untrustworthy numbers. Both motivate [masq-ab-factorial-design](../decision/masq-ab-factorial-design.md) (rebuild) over a patch of the existing corpus.

## Hypotheses tested

- Implicit precondition for [masq-paper-as-active-program](../decision/masq-paper-as-active-program.md): "the existing synthetic corpus exercises multi-party-over-time strongly enough to ground the paper's claims." **Verdict: partially false** — the phenomena exist but are too few and unlabeled for statistical claims.

## Method

- Diffed the three masq copies under `/team-share/{slate,red,amber}/kyrja/benchmark/masq`. Confirmed **byte-identical corpus** (md5 on `ground_truth.json`, `queries.json`, `schema.py`, `load.py`; all 100 session files identical). Red diverges only in code/results (ChromaDB/Mem0 retrievers, resume harness, v2 results).
- Enumerated decision chains from session-timeline.md Collision & Chain Index (authoritative per Idris/amber), joined with per-session speaker/team to classify each distinctive event as cross-/same-person and cross-/same-team.
- Counted query coverage of the distinctive events across the 500-query set.
- Tooling/apparatus state corroborated by Kerman (red) IPC report and direct inspection of `results_answer_v1.json` and `llm_judge_scores.py`.

## Results

### Corpus: rich qualitatively, thin statistically `[MEASURED]`

Independent distinctive events ≈ **8 total**:

| Phenomenon | Independent events | Cross-team | Cross-person |
|---|---|---|---|
| Unknowing collision (party acts unaware of another's prior decision) | 4 (S49, S51, S54, S47) | all 4 | all 4 |
| Explicit supersession (decision revised later) | 2 (S45→S14, S50→S18) | 0 | 1 of 2 |
| Departure / knowledge orphaning | 2 (Jordan wk6, Dana wk8) | 1 of 2 | 2 of 2 |

- **Strict cross-team explicit supersession: N=0.** The cleanest distinctive cell (cross-team *and* cross-person) is the **unknowing-collision** (N=4), already probed by the `rejection_retrieval` query type.
- The 500 queries **re-probe these ~8 events** — temporal queries touch supersession-anchored sessions 26 times, tracing to 2 events. Treating query count as N is pseudo-replication; the unit of analysis is the *event/scenario*, not the query.
- Schema defines `supersedes`, `chain_id`, `DecisionStatus.SUPERSEDED`, but the corpus JSON leaves all three **unpopulated** (0/108 segments). Status is point-in-time per-segment by design (Idris) — supersession belongs in the `supersedes` pointer + `as_of_week`, never a retroactive status mutation.

### Apparatus: current numbers are untrustworthy `[MEASURED]`

- Reader = gemma3:4b — per Kerman, hallucinates names even with **oracle** retrieval; the attribution/party probe is unmeasurable with it.
- `token_f1` is invalid as scored: oracle answers on Q045/Q046 are degenerate format-leaks (`"Okay, excellent! Let's confirm…"`) yet score **f1 = 1.0**.
- Mem0 baseline invalid: gemma3:4b extraction produced content-free memories; mean F1 ≈ 0.19, 45/69 zero.
- Coverage: only ~70 of 500 queries ever scored (v1=70, v2=69 then paused).
- Query-ID aliasing: the hardcoded judge dict (original 70 numbering) and `results_answer_v1.json` (expanded 500) do not share a key.
- Contamination history: a now-removed `build_prompts.py` once leaked `ground_truth` into prompts (42%→96%); grep prompt files before any re-run.

### Construct-validity note

"Independent distinctive events" measures the number of *structurally distinct* multi-party-temporal episodes a system could be tested on without correlated re-probing. It is the correct unit for subgroup/interaction claims (party×time). It does **not** measure surface query difficulty or realism — a corpus can be narratively rich (one 12-week org) yet have low event-N. The N≈8 figure is a count over the authoritative Chain Index, not an estimate; its main uncertainty is whether the Index is exhaustive of the world's intended chains (Idris confirms it is authoritative).

## Limitations

- Event taxonomy (collision / supersession / departure) is ours; alternative groupings could shift counts by ±1–2 but not the order of magnitude.
- Apparatus findings on the reader rest partly on Kerman's qualitative report; the `token_f1`=1.0-on-garbage and coverage findings are directly verified.

## Raw artifacts

- Audit working notes + the reframe discussion: this session (2026-06-08, Nils).
- Corpus: `masq` (canonical base); design spec session-timeline.md.
- Phase-1 punch list (superseded in priority by the rebuild): [masq/phase1-breakdown.md](../../masq/phase1-breakdown.md).

## Related

- Motivates [masq-ab-factorial-design](../decision/masq-ab-factorial-design.md) — the rebuild this audit justifies.
- Updates the corpus assumptions in [masq-paper-as-active-program](../decision/masq-paper-as-active-program.md).
- Supplies the event-N evidence behind [multi-party-attribution-gap](../concept/multi-party-attribution-gap.md)'s power discussion.

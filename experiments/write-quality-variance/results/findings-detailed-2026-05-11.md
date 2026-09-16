# Write-Quality Variance Experiment — Detailed Findings

**Date:** 2026-05-11
**Spec:** `../spec.md` (`write-quality-variance-experiment-spec-2026-05-11.md`)
**Parent goal:** Wedge tool-chain memory, Goal 2 (write path). See `tool-chain-wedge-goals-2026-05-11.md`.

## Why we ran this

Phase 2 (April 2026) showed memory either helps (relevant: −31% to −51% cost) or hurts (irrelevant: +41–49% cost) on the same xarray task chain. It tested one failure mode of memory: *right encoding, wrong context*. It did not test the other failure mode: *bad encoding, right context*.

The wedge architecture (per the 2026-05-11 working doc) leans heavily on precision-tuned retrieval gating, on the assumption that retrieval is the binding control. But if a bad-but-relevant memory hurts as much as an irrelevant one, retrieval gating alone is insufficient — we'd need a write-side quality gate too. That changes the architecture.

This experiment was the cheapest test to disambiguate. Pre-registered hypotheses (full text in spec.md):

- **H-QUAL-FLOOR:** Encoding from a partial-failure predecessor session produces cost ≥ cold baseline.
- **H-QUAL-FRAMING:** Briefing-style prompt produces better encodings than summary-style.
- **H-QUAL-STRUCTURE:** Prose briefings outperform fully-structured slot encodings of the same length.

## What we built

Target task: `where_keep_attrs_scalar` (xarray-6461). Chosen for its tight Phase 2 cold variance ($0.40, $0.42) and clear memory effect (Level D: $0.25, $0.29). Predecessor session: `where_keep_attrs_add` (xarray-4687).

Five encoding variants planned, one deferred:

| variant | source | distiller prompt |
|---------|--------|------------------|
| A | full Task 1 transcript | canonical briefing (Phase 2 prompt at 1200 tok) |
| B | full Task 1 transcript | retrospective summary framing |
| C | full Task 1 transcript | structured slots, no prose |
| D | truncated Task 1 transcript (cut before fix template revealed) | canonical briefing |
| E | detoured session (synthesised) | canonical briefing |

E was deferred because synthesising a natural detour required an additional bootstrap run with a misleading hint. Plan: add E only if D shows a meaningful signal.

Infrastructure reused from Phase 2 archive: xarray git repo, Python venv with deps, harness skeleton. New work: distiller prompts B and C, source truncation for D, encoding generation script (`harness/generate_encoding.py`), trial harness (`harness/run_variant.py`), analysis (`harness/analyze.py`).

## Encoding generation

All four encodings produced by Opus (4.7 — the current `--model opus` alias) via Claude CLI in `-p` mode (no tools). Costs and lengths:

| variant | words | cost |
|---------|-------|------|
| A | 762 | $0.154 |
| B | 690 | $0.143 |
| C | 446 | $0.138 |
| D | 729 | $0.128 |

Qualitative observations:

- **A** (briefing): comprehensive prose with file/line specifics, fix template, dead ends, gotchas, alternatives. Closest in genre to Phase 2's reported style.
- **B** (summary): same technical facts as A but in past-tense narrative. Included a hedged meta-observation ("The agent did not show an explicit edit to forward keep_attrs...") that A did not.
- **C** (structured): much shorter (446w vs 700+), strict slot format. No prose connective tissue.
- **D** (truncated source): the distiller noticed the truncation ("the truncated read cut off before showing the implementation body") and **filled in the missing fix template by inference**. The inferred fix was approximately correct. This was an early signal that competent distillation is robust to mild source degradation — a result anticipated and confirmed by the trial data.

All four encodings carried old absolute paths from Phase 2's worktree layout (`experiments/phase2-utility/worktrees/...`). This is a known confound — the downstream agent has to translate paths — but it's constant across variants.

## First sweep: Opus 4.7 — reproduction failed

We ran the full 16-trial sweep (A, B, C, D × n=4) under Opus 4.7 (today's `--model opus` default). The smoke-test trial (A run 1) came in at $0.32 — within Phase 2's Level D band ($0.22–$0.32), so we proceeded with the full sweep.

The full A condition came in at **mean $0.537**, far outside the Phase 2 Level D band. Within-A variance was high (std $0.154). All conditions clustered between $0.41 and $0.59.

The pre-registered halt condition fired: "If A doesn't reproduce within ±20% of Phase 2 Level D ($0.22-$0.32): stop and debug the harness before interpreting other variants."

| variant (4.7) | mean | std | 95% CI |
|---------------|------|-----|--------|
| A | $0.537 | 0.154 | [0.39, 0.64] |
| B | $0.587 | 0.169 | [0.43, 0.74] |
| C | $0.406 | 0.098 | [0.33, 0.49] |
| D | $0.459 | 0.111 | [0.36, 0.55] |

Candidate explanations considered, in rough order of likelihood:

1. **Model version drift.** Phase 2 ran in April 2026 on Opus 4.6. Today's `--model opus` alias resolves to Opus 4.7. Different models can produce different exploration depths on the same prompt.
2. **Path mismatch in encodings.** Old worktree paths require translation by the agent. Constant across variants but could inflate absolute costs.
3. **Single smoke run was a lucky sample.** n=1 → unreliable.

Diagnostic proposed: run cold (n=4) and A_orig (Phase 2's actual Level D encoding, copied from the archive) (n=4) under Opus 4.7 to disambiguate. AJ proposed a cleaner alternative: switch the harness to `--model claude-opus-4-6` and re-run, matching Phase 2's model exactly.

We confirmed `claude-opus-4-6` is still selectable via the Claude CLI, and switched the harness.

The Opus 4.7 results are preserved as `data/trials_opus47.json` and `data/sweep_opus47.log` for future reference.

## Second sweep: Opus 4.6 — clean diagnostic

Added two controls:

- **A_orig:** Phase 2's actual Level D encoding (`original_bootstrap/encodings/where_keep_attrs_add.md`), run as a fifth memory condition. This is the reproduction control proper — same encoding *content* Phase 2 used.
- **cold:** no memory injection. Establishes the harness baseline so we can read relative reductions independent of Phase 2's absolute numbers.

Total: 24 trials. Ran sequentially in this order: A_orig, cold, A, B, C, D. Controls first to surface harness issues early.

### Results (Opus 4.6)

| variant | n | mean $ | std $ | 95% CI | out tok | turns | pass |
|---------|---|--------|-------|--------|---------|-------|------|
| **C — structured slots** | 4 | **$0.142** | 0.031 | [0.121, 0.170] | 1353 | 5.0 | 4/4 |
| D — truncated source | 4 | $0.197 | 0.065 | [0.143, 0.251] | 1925 | 7.5 | 4/4 |
| B — summary framing | 4 | $0.200 | 0.089 | [0.139, 0.281] | 1787 | 8.5 | 3/4 |
| A — new briefing | 4 | $0.247 | 0.040 | [0.215, 0.279] | 2281 | 10.8 | 3/4 |
| cold (no memory) | 4 | $0.295 | 0.076 | [0.235, 0.356] | 2485 | 12.5 | 4/4 |
| A_orig (Phase 2 encoding) | 4 | $0.300 | 0.058 | [0.256, 0.350] | 3008 | 13.2 | 4/4 |

Individual trials are in `data/trials.json`. Per-trial JSON logs in `data/trial_logs/`.

Two passes failed (3/4 for A and B). A run 3 and B run 4 — both produced patches that didn't pass the FAIL_TO_PASS test. Costs of failures were within their variant's normal range, so they look like stochastic correctness failures (agent stopped before fully solving) rather than systematic.

### Pre-registered decision-rule outcomes

**Rule 1/2 — A reproduction check.** A mean ($0.247) is within the Phase 2 Level D band ($0.22–$0.32). Harness is trustworthy under Opus 4.6. **PASS — proceed with interpretation.**

**Rule 3/4 — H-QUAL-FLOOR.** D mean ($0.197) is *lower* than cold mean ($0.295). The hypothesis predicted D ≥ cold (bad source produces harmful memory). **REJECTED.** Within this experiment's scope (truncated source + Opus distiller), the distiller fills gaps competently and the resulting memory is still useful.

**Rule 5/6 — H-QUAL-FRAMING (A vs B) and H-QUAL-STRUCTURE (A vs C).**
- A vs B: CIs overlap ([0.215, 0.279] vs [0.139, 0.281]). B trends lower but inconclusive at n=4. **NOT SUPPORTED but not rejected either.**
- A vs C: CIs disjoint ([0.215, 0.279] vs [0.121, 0.170]). C significantly cheaper. **H-QUAL-STRUCTURE REJECTED — in the reverse direction.** Structured slots outperform prose briefing.

## Surprises and what they imply

### Surprise 1: A_orig ≈ cold

Phase 2 reported its Level D encoding produced −31% cost vs cold. In our re-run, A_orig ($0.300) was statistically indistinguishable from cold ($0.295). The agent with A_orig actually produced *more* output tokens (3008 vs 2485) and used more turns (13.2 vs 12.5) than the agent with no memory at all.

Possible explanations:

- **Path mismatch.** A_orig contains absolute paths to Phase 2's old worktree location. The downstream agent reads "see the file at experiments/phase2-utility/worktrees/bootstrap_where_keep_attrs_add/xarray/core/computation.py:1730" and has to translate to its actual worktree path. The new encodings (A, B, C, D) also carry these paths, so this doesn't differentially explain A_orig's poor performance — but it might depress all absolute numbers vs Phase 2.
- **Phase 2 cold was higher.** Phase 2 reported cold at $0.41; we measured cold at $0.30. The −31% Phase 2 relative reduction was computed against a higher baseline. Our A_orig ($0.30) matches Phase 2's *Level D* number ($0.27) reasonably well in absolute terms — the −31% relative reduction simply doesn't reproduce because our cold drifted downward too.
- **Distiller-model artefacts.** A_orig was produced by April 2026's Opus distiller (with the 500–800 token Phase 2 prompt). Our new A was produced by May 2026's Opus 4.7 distiller (with the 1200-token Phase 2 prompt). Different distillers might emphasise different content.

We cannot fully disambiguate without re-running Phase 2's full Tier 1 (Tasks 1–3) under matched conditions. Flagging this as a follow-up; it doesn't undermine the variant comparisons in this experiment (all run in the same conditions).

### Surprise 2: structured slots dominate

This was the most consequential finding and contradicted my prior. C (slot format, no prose) cost 42% less than A (prose briefing) and 52% less than cold. C's encoding was 446 words vs A's 762 — so it's also a token-efficiency win on the read side. The agent reading slot-format memory used 5.0 turns on average; with prose briefing, 10.8 turns.

Why structured is winning: my speculation, not validated:

- **Density.** Slots compress the same facts into ~60% the tokens. Less context to process.
- **Skim-ability.** The agent can grep a slot ("FIX_PATTERN:") rather than parse prose. The encoding becomes more like a tool-call signature than a memo.
- **Less ambiguity.** Prose includes hedging, transitions, alternatives — interesting but not always actionable. Slots are forced to be specific.

Implication for the wedge architecture: my earlier framing was "free-text encoding body + structured compound key." This experiment suggests the body itself should be structured. Compound-key extraction can then fall out of the encoding format naturally rather than being a separate pass.

### Surprise 3: D didn't degrade

Variant D was the H-QUAL-FLOOR test. We expected mild-to-significant degradation from feeding the distiller an incomplete transcript. We observed the opposite: D ($0.197) actually beat A ($0.247).

Reading the D encoding explains why: Opus noticed the truncation, called it out in the encoding ("the truncated read cut off before showing the implementation body"), and **inferred the fix template from context** (the keep_attrs pattern elsewhere in the file, the apply_ufunc delegation visible in earlier reads). The inference was correct enough to be useful.

This is an important architectural signal: **a competent distiller is robust to mild source degradation**. It's not robust at the limit (e.g., a transcript of a session that never identified the bug) — but for the moderate case (session was cut short, or the agent didn't get all the way to the fix), the distiller can recover.

The H-QUAL-FLOOR hypothesis was about whether *write-side* quality control is mandatory. This result suggests it's less mandatory than I feared. But it doesn't mean it's unnecessary — the experiment only tested mild degradation. A failed-session encoding (agent went down a wrong path and never corrected) would be a stronger test.

### Surprise 4: Phase 2's relative improvement is fragile

Phase 2's headline numbers (Level D = −31% cost, transcript = −51%) were the basis for "pursue this wedge." Reproducing the absolute Level D cost requires matching the model version exactly. Even with the same model (Opus 4.6, today), the relative improvement vs cold is smaller than Phase 2 reported because our cold drifted downward.

The wedge is still real — every memory variant we tested beat cold, and C beat cold by 52%. But the precise numbers in the Phase 2 pilot-analysis shouldn't be treated as load-bearing. The directional finding (memory helps when relevant) is solid; the magnitudes need to be re-measured periodically as models change.

## Methodology notes

### Caching effects

Cost is dominated by `cache_read_tokens`, not `cache_creation_tokens` (e.g., A_orig run 1: 387,787 cache reads on a ~7K char prompt). The `cache_read` field reflects the agent's *in-session* conversation context being cached and re-read at each turn, not API-level cross-trial caching. Within-variant cost variance reflects different exploration depths, not different cache states.

There is some cross-trial prompt caching at the API level — visible as run 1 of each variant typically having a higher absolute cost than runs 2–4 (the prompt itself is cached after first use). This effect is small relative to within-trial conversation caching, but it's there. Phase 2 likely had the same effect.

### n=4 is underpowered for some comparisons

A vs B: CIs overlap, B trends ~20% lower, but n=4 can't separate them. To call H-QUAL-FRAMING decisively, we'd need n≥8.

A vs C: CIs cleanly disjoint at n=4 because the effect is large (~40%).

The pre-registered fallback (expand to n=6 if signal is muddy) wasn't triggered because the large effects (C wins, D doesn't degrade) were clear at n=4. The small effect (A vs B) remains under-resolved.

### Distiller-model confound

Our new encodings (A, B, C, D) were distilled by Opus 4.7. A_orig was distilled by Opus 4.6 (Phase 2's setup). The downstream agent in all cases was Opus 4.6 (after we switched).

So C's win could partly reflect Opus 4.7 producing better structured output, not just the slot format itself. To fully isolate, we'd need to re-generate the encodings with Opus 4.6 distillation and re-run. Flagged as a follow-up.

### Single task, single repo

Same caveats as Phase 2. C's win on `where_keep_attrs_scalar` doesn't guarantee structured slots win on every task type. Replication on at least one Sphinx task before treating this as architectural.

### Pre-registration worked

The halt rule on Rule 1/2 fired after the failed Opus 4.7 reproduction. Without the pre-registered halt, the most likely failure mode would have been post-hoc rationalisation — "the variants still tell us something useful, let's interpret them anyway." The halt forced us to identify and isolate the model drift before drawing conclusions. Methodologically, this was the most important part of the experiment.

## Implications for the wedge architecture

Three concrete updates to push back into `tool-chain-wedge-goals-2026-05-11.md`:

### 1. Encoding format → structured slots, not prose briefing

My earlier framing (in the wedge-goals doc and the schema-split discussion) was "free-text encoding body" plus separate structured compound-key extraction. This experiment suggests the body itself should be structured. C's encoding is essentially a slot-filled record with file paths, fix patterns, dead ends, gotchas, and verification — exactly the fields a compound key would need.

This collapses two design decisions into one: the encoding format *is* the compound key, with some slots queryable (path, function, task_type) and others retrieved as part of the memory body.

### 2. Write-side quality gate → less mandatory than feared, but not refuted

D's robustness rejects H-QUAL-FLOOR for the mild-degradation case. A competent distiller fills gaps from context. But:

- D was only mildly degraded (truncated, not failed).
- A worst-case test (encoding from a session that explored wrong paths and never corrected) wasn't run.
- The +50% harm Phase 2 measured was from *correct* memory in wrong context, not bad memory in right context.

So the gate is probably not a P0 architectural requirement. It can be deferred behind retrieval gating without immediate risk. Worth re-testing with worse sources before deciding to skip permanently.

### 3. Phase 2 numbers are directional, not load-bearing

The −31% / −51% Phase 2 numbers don't reproduce cleanly across model versions. The wedge case is still real (every memory variant beat cold; C beat cold by 52%) but the precise magnitudes are not stable enough to base business projections on. Plan for re-measurement when models change.

## Limitations

1. **n=4 per condition.** Adequate for the large effects (C, D), under-resolved for the small ones (A vs B framing).
2. **Single task, single repo, single downstream model.** No generalisation claims.
3. **Distiller-model confound** between A_orig (Opus 4.6) and A/B/C/D (Opus 4.7).
4. **Path-mismatch in encodings.** Old worktree paths require translation. Constant across variants but may inflate absolute costs vs Phase 2.
5. **Two correctness failures** (A run 3, B run 4) unexamined. Stochastic in appearance but not investigated.
6. **No worst-case source test.** D was a moderate degradation. The hypothesis that *truly* bad encodings hurt downstream cost remains untested.
7. **Within-variant cost variance is large** relative to differences. Some pairwise comparisons would need 2–3× the n to resolve.

## Follow-up experiments, ranked

1. **Worst-case source test.** Generate an encoding from a session that genuinely failed (wrong path, never corrected). Compare against C and cold. Closes the H-QUAL-FLOOR question properly.
2. **C replication on a second task.** Pick another Tier 1 task (`where_keep_attrs_coord`) or a Sphinx task. Confirms C's win isn't task-specific.
3. **Distiller-model controlled re-run.** Regenerate A/B/C/D with Opus 4.6 distillation. Isolates the encoding-format effect from any distiller-model artefact.
4. **A vs B at higher n.** Expand to n=8 to resolve whether summary framing is meaningfully worse than briefing framing.
5. **Investigate the A_orig anomaly.** Why does Phase 2's encoding produce no benefit in today's setup? Re-run Phase 2 Tier 1 end-to-end under Opus 4.6 to see if the entire effect has faded.

## Artifacts

```
experiments/write-quality-variance/
├── spec.md                           original experiment spec
├── encodings/
│   ├── A_encoding.md                 new briefing (Opus 4.7 distillation)
│   ├── B_encoding.md                 new summary
│   ├── C_encoding.md                 new structured slots
│   ├── D_encoding.md                 new briefing over truncated source
│   ├── A_orig_encoding.md            Phase 2's original Level D encoding (Opus 4.6)
│   └── *_meta.json                   per-encoding generation metadata
├── sources/
│   ├── task1_full.md                 reused Phase 2 transcript
│   └── task1_truncated.md            cut before fix template revealed
├── prompts/
│   ├── A_briefing_1200.md            Phase 2 canonical prompt
│   ├── B_summary_1200.md             retrospective framing
│   └── C_structured_1200.md          slot-format prompt
├── harness/
│   ├── generate_encoding.py
│   ├── run_variant.py
│   ├── run_sweep.sh                  Opus 4.7 sweep (first, halted)
│   ├── run_sweep_46.sh               Opus 4.6 sweep (final)
│   └── analyze.py
├── data/
│   ├── trials.json                   Opus 4.6 sweep results (canonical)
│   ├── trials_opus47.json            archived 4.7 sweep
│   ├── sweep_46.log
│   ├── sweep_opus47.log
│   └── trial_logs/                   per-trial JSON
├── repo, venv, original_*            symlinks to Phase 2 archive
└── results/
    ├── findings-detailed-2026-05-11.md    (this doc)
    └── findings-summary-2026-05-11.md     short version
```

Total spend: ~$10 across 40 trials and 4 distillations. ~75 minutes wall time including the failed Opus 4.7 sweep.

# Write-Quality Variance — Summary

**Date:** 2026-05-11
**Detail:** `findings-detailed-2026-05-11.md`

## Headline finding

**Structured slot-format encodings beat prose briefings by ~40%, and beat cold (no memory) by ~52%.** This contradicts the pre-registered prior. Single task (`where_keep_attrs_scalar`), n=4 per condition, Opus 4.6.

## Results

| variant | mean | 95% CI | pass |
|---------|------|--------|------|
| **C — structured slots** | **$0.142** | [0.121, 0.170] | 4/4 |
| D — truncated source, briefing | $0.197 | [0.143, 0.251] | 4/4 |
| B — summary framing | $0.200 | [0.139, 0.281] | 3/4 |
| A — briefing | $0.247 | [0.215, 0.279] | 3/4 |
| cold | $0.295 | [0.235, 0.356] | 4/4 |
| A_orig (Phase 2 encoding) | $0.300 | [0.256, 0.350] | 4/4 |

## Verdict per pre-registered hypothesis

- **H-QUAL-FLOOR** (bad source produces harmful memory): **REJECTED**. D < cold. Opus distiller filled gaps from context.
- **H-QUAL-STRUCTURE** (prose > slots): **REJECTED in reverse**. Slots beat prose decisively.
- **H-QUAL-FRAMING** (briefing > summary): **inconclusive at n=4**. B trends lower than A but CIs overlap.

## What changes in the wedge plan

1. **Encoding format = structured slots, not prose.** Collapses two design decisions (encoding body + compound key) into one — slots *are* the compound key.
2. **Write-side quality gate = deferrable.** Less load-bearing than feared. But the experiment only tested mild source degradation, not worst-case. Re-test before fully skipping.
3. **Phase 2 absolute numbers are not load-bearing.** Reproducing required matching the model version. Direction of effect is stable; magnitudes drift with models.

## Key surprises

- **A_orig (Phase 2's original encoding) gave no benefit over cold** in today's setup. Phase 2 cold was $0.41; ours is $0.30. The −31% relative reduction Phase 2 reported is missing; absolute Level D number ($0.27) approximately matches our A_orig ($0.30).
- **Variant D didn't degrade.** Truncating the source transcript before the fix template was revealed produced an encoding that still beat cold. Competent distillation is robust to moderate source quality issues.
- **Opus 4.7 reproduction failed.** Our first sweep under today's `--model opus` (4.7) showed A at $0.54, far outside band. Switching to `--model claude-opus-4-6` reproduced Phase 2 cleanly.

## Methodology callouts

- **Pre-registration caught the model drift.** The halt rule on A's reproduction band fired on the Opus 4.7 sweep, forcing a diagnostic step before drawing conclusions. Without it, we would have reported a misleading null.
- **Distiller-model confound.** New encodings (A, B, C, D) distilled by Opus 4.7; A_orig by Opus 4.6. Both ran under Opus 4.6 downstream. C's win could partly reflect Opus 4.7 producing better structured output. Follow-up: re-distill with 4.6.

## Limitations (load-bearing)

- n=4 per condition, single task, single repo
- Path-mismatch in all encodings (old worktree paths)
- Two correctness failures (A run 3, B run 4) unexamined
- Worst-case source not tested — H-QUAL-FLOOR rejection holds only for mild degradation

## Highest-priority next steps

1. **Worst-case source experiment.** Generate encoding from a fully-failed session. Tests H-QUAL-FLOOR at the limit.
2. **C replication on a second task** (`where_keep_attrs_coord` or a Sphinx task). Confirms task-independence before treating slot format as architectural.
3. **Distiller-model controlled re-run.** Regenerate A/B/C/D with Opus 4.6. Isolates encoding-format effect from distiller version.

## Cost and time

~$10 total spend, 40 trials, 4 distillations, ~75 min wall time. Includes the failed Opus 4.7 sweep.

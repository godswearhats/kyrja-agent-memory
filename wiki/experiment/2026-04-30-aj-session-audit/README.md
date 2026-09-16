---
type: experiment
name: AJ Session-Log Audit (2026-04-30) — F2 / F4 empirical anchor for the scale model
status: LANDED
last_ingested: 2026-05-17
sources: []
epistemic_tags: [measured]
tags: [scale-model, F2, F4, session-telemetry, n1, internal-data, audit]
---

## What this is

An audit of AJ's local Claude Code session logs to empirically anchor two scale-model parameters (F2 = orchestration depth, F4 = sessions per active day) that had previously been set from literature estimates only. Conducted 2026-04-30. This is *our own data*, gathered to better understand the scale model in the moment — it is not an external source. Per the [evidence-anchoring framework](../../concept/evidence-anchoring.md): self-collected measurement belongs in `experiment/`, even when downstream pages treat it like a citation.

## Method

- **Data:** AJ's Claude Code conversation JSONL files at `~/.claude/projects/` (local workstation; not in `library/papers/` archive).
- **Window:** 44 active days preceding the 2026-04-30 audit (days where logging was reliably active; earlier conversations excluded).
- **Sample size:** 1,964 sessions total. Single user (n=1 by definition).
- **Operationalization:**
  - "Session" = one continuous Claude Code conversation.
  - "Orchestration depth" (F2) = count of distinct sub-task invocations per top-level conversation, then categorized by work type using AJ's own ruleset.
  - "Sessions per active day" (F4) = sessions / active-day count.
- **Population proxy for F4 central:** $13/day median Claude Code spend (vendor-published) → 3–6 sessions/day inferred typical-per-session-cost central.

## Results

### F2 — orchestration-depth bimodality

By work type, the distribution is bimodal — short sessions for bug-fixes / quick edits, longer sessions for feature work. SWE-flavoured sessions re-anchored to F2 ∈ {8, 10, 12}. `[MEASURED]` for AJ specifically. *Construct-validity:* the bimodal structure is a categorization-rule output, not a free measurement; inter-rater reliability not measured.

### F4 — sessions per active day

AJ's measured median: 10.65 sessions/day. Inferred population central: F4 = 5 (from the spend-derived proxy). AJ sits at the 85–90th percentile, not at the central. `[MEASURED]` for AJ's own count; population central is an inference, not a direct distribution measurement. *Construct-validity:* the cost-to-sessions inference assumes a typical per-session cost; sensitivity to that assumption not separately characterized.

## Construct-validity caveats

1. **Single user.** n=1 by definition. The work-type categorization is AJ's own ruleset applied to his own logs. Inter-rater reliability not measured.
2. **44-day window.** Sampled during a period where logging was reliably active; earlier conversations excluded.
3. **Cost-to-sessions inference for F4 population central** is a separate-construct chain (vendor spend distribution → typical per-session cost → sessions/day). Each step adds uncertainty not propagated through to the central.
4. **Not externally archived.** Logs are on AJ's local machine. Reproducibility requires AJ to re-run the categorization or share a processed snapshot. Treat reruns like a fresh experiment, not a re-read of a fixed source.

## Findings

- F2 audit-corrected SWE central is **empirically anchored** but **n=1** — replication with a second user remains medium-priority debt. See [f2-bimodality-n1](../../open-question/f2-bimodality-n1.md).
- F4 = 5 population central is **defensible** but rests on a multi-step inference; AJ's 10.65 is a real direct measurement, just not population-central.
- Replacing literature-only estimates with this measurement **strengthened** the scale model overall, while introducing the explicit n=1 weakness that the open question now tracks.

## Relevance to Kyrja

- Empirical anchor for the [scale-model-audit-corrections](../../decision/scale-model-audit-corrections.md) Pass 3 F2 + F4 bullets.
- The known weakness driving [f2-bimodality-n1](../../open-question/f2-bimodality-n1.md) (replication required).

## Re-running

Re-run the categorization against current `~/.claude/projects/` contents to produce a fresh snapshot; treat it as a new experiment with its own dated directory. Do not in-place update this page.

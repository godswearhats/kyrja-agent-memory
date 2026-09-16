---
type: decision
name: Scale-model audit corrections (F1/F4/F5/F8, F2)
status: ACTIVE
last_ingested: 2026-05-13
sources: [../experiment/2026-04-30-aj-session-audit/README.md]
tags: [methodology, scale-model, calibration]
---

## Decision

On 2026-04-30, the scale model's high-sensitivity parameters were audited against external evidence via parallel sub-agent passes. Central values were revised where the original sourcing didn't survive audit. The post-audit centrals are now the canonical inputs to [scale-crossings](../concept/scale-crossings.md); pre-audit numbers are stale and should not be reused.

| Parameter | Pre-audit central | Post-audit central | Direction of change |
|---|---|---|---|
| **F1** tool-chain persistence rate | non-zero amplifier | **0 today**, with no vendor roadmap | demoted from foundation to amplifier |
| **F2** orchestration depth | literature estimate | empirically anchored (SWE: 8/10/12) | strengthened — measured, not estimated |
| **F4** sessions per user per day | 5 (estimate) | 5 (confirmed defensible) | unchanged; cost-derived inference at $13/day median Claude Code spend confirms 3–6 |
| **F5** memories per session | 9 | **12** | strengthened (corrects conservative bias) |
| **F8** consolidation rate | 0.30 central, 0.10 low | **0.20 central, 0.05 low** | strengthened (corrects conservative bias — production systems forget less than we modelled) |

**Net effect:** two of three load-bearing audits found systematic *underestimation* of load. The post-audit re-run (`experiments/post_audit_2026-04-30.py`) shows Scenario A and Scenario D each cross three walls (was two), and all wall-crossings pulled in.

## Motivation

The pre-audit centrals had inconsistent provenance discipline. Some came from cited papers; others from informal estimates; F8 in particular was a **category error** (compression-ratio papers were treated as stock-removal-rate evidence). Before the cascading-failures re-anchor ([cascading-failures-reanchor](./cascading-failures-reanchor.md)), this was tolerable because the single-wall framing didn't lean hard on parameter calibration. Post-re-anchor, the model's outputs are the volume leg of a three-legged thesis; calibration discipline became load-bearing.

The audit was structured as **three parallel sub-agent passes** to limit confirmation bias from any single agent's framing:

- Pass 1: F1, F5, F8 + long-context-substitution argument
- Pass 2: F4, F5, F8 (overlap on F5 and F8 was deliberate — cross-check)
- Pass 3: F2 empirical validation against AJ's own usage data (n=1, 1,964 sessions over 44 active days) `[MEASURED]` ([session-audit](../experiment/2026-04-30-aj-session-audit/README.md)). *Construct-validity:* sessions counted from local Claude Code conversation logs over the 44-day window where logging was active; "session" is one continuous Claude Code conversation. Single-user n=1 sample; not generalizable to other workflows but materially better than the pre-audit literature-only F2 anchor.

Findings from the three passes were reconciled before central revisions were applied. Cross-check on F5 and F8 between passes 1 and 2 reached the same conclusions independently, strengthening confidence.

## Commitments

- **F1 is 0 today.** Audited 6 systems (Cognee, Mem0, Letta, Zep, LangMem, MemGPT) — none persist tool traces as first-class memory. Letta is closest but filters tool calls from agent recall. The "tool-chain memory" wedge product creates F1 > 0 *for Kyrja*, but the scale-model baseline assumes zero F1 for incumbents.
- **F1 trajectory is unanchored.** No vendor has published a roadmap toward tool-chain memory persistence. The model can run "F1 → 1.0 by Y3" scenarios but the trajectory itself is `[SPECULATED]`, not `[ASSERTED]`.
- **F1 is no longer load-bearing for the volume leg in moderate+ scenarios.** [scale-crossings](../concept/scale-crossings.md) shows Scenarios B, C, E, F all cross LIMIT-1536d without tool-chain amplification. Scenario A (conservative SWE-200) is the exception: post-correction, no-tool-chain A drops below threshold. Tool-chain memory is therefore foundational for the conservative-tail thesis claim, not the full thesis.
- **F2 is empirically anchored but n=1** `[MEASURED]` ([session-audit](../experiment/2026-04-30-aj-session-audit/README.md)). Validation on AJ's session log was rigorous (post-hoc, but with explicit categorization rules); however, bimodality by work type is a single-user finding. *Construct-validity:* see Pass 3 note above; the bimodality structure is a categorization-rule output, not a free measurement. Confirmation with a second user remains medium-priority debt. The post-audit centrals are kept; the n=1 caveat travels with them.
- **F4 = 5 is defensible** `[MEASURED]` ([session-audit](../experiment/2026-04-30-aj-session-audit/README.md)). Cost-derived inference at $13/day median Claude Code spend implies 3–6 sessions/day. AJ's 10.65 is 85-90th percentile, not central. *Construct-validity:* "median Claude Code spend" is a published vendor figure used as a population proxy; AJ's own 10.65 sessions/day is direct measurement from local logs. The inference chain (spend → sessions/day) assumes a typical per-session cost; sensitivity to that assumption not separately characterized.
- **F5 has no production data.** EMem benchmark (18-20 EDUs/session) is the closest empirical anchor, and it is a synthetic benchmark, not production. The 9 → 12 revision is on the strength of EMem + the audit's judgment that the original 9 was conservative. F5 remains the largest unanchored top-4 driver. See [f5-production-data](../open-question/f5-production-data.md).
- **F8 = 0.20 central reflects production reality.** Most production memory systems default to **zero consolidation**: Mem0 default, Zep architecturally non-lossy, Letta no dedup, OpenAI/Anthropic developer-controlled. Only Copilot has a numeric TTL (28 days). The pre-audit 0.30 was sourced from compression-ratio papers — a different operation than annual stock removal. Revised to 0.20 central / 0.05 low.
- **Long-context-substitution argument was checked and rejected.** Anthropic and Google — the long-context leaders — both shipped persistent memory products. Mem0's own quote: "full-context is the only approach categorically unusable in real-time production." Long context does not substitute for persistent memory; the substitution argument should not be re-introduced without new evidence.
- **Pre-audit scenario outputs are stale.** Tornado plots, crossing dates, and walls-crossed counts cited from pre-audit runs (e.g. earlier revisions of THESIS.md or correspondence pre-2026-04-30 evening) carry stale numbers and should be re-derived from `data/post_audit_2026-04-30.csv`.

## Reversibility

**Parameter-level: cheap.** Each central is a single number in `build_notebook.py`'s parameter dictionary. New evidence (especially F5 production data) can revise centrals without restructuring the model. The post-audit values are *current best estimates*, not commitments to specific numbers.

**Audit-methodology-level: durable.** The discipline of "audit before claiming, prefer parallel passes, cross-check overlapping parameters" is a methodology commitment. Future high-sensitivity parameter changes should follow the same pattern rather than relying on single-agent estimates.

## Related

- [scale-crossings](../concept/scale-crossings.md) — the model output these corrections feed.
- [cascading-failures-reanchor](./cascading-failures-reanchor.md) — the framing-side correction applied alongside these parameter-side corrections; same date.
- [f5-production-data](../open-question/f5-production-data.md) — the largest residual calibration gap.
- [f12-retention-wiring](../open-question/f12-retention-wiring.md) — separately tracked model bug not addressed by this audit.
- Audit artefacts:
  - [scenarios_pre_post_2026-04-30.csv](../../../research/scale-model/data/scenarios_pre_post_2026-04-30.csv) (before/after comparison)
  - [post_audit_2026-04-30.csv](../../../research/scale-model/data/post_audit_2026-04-30.csv) (canonical post-audit outputs)
  - [post_audit_2026-04-30.py](../../../research/scale-model/experiments/post_audit_2026-04-30.py)
  - [validation-aj-usage.md](../../../research/scale-model/sources/validation-aj-usage.md) (F2 empirical validation)
- See `project_kyrja_active.md` §"Latest state 2026-04-30 PM — audit complete, thesis documented". Container-local; pending full atomization into wiki.

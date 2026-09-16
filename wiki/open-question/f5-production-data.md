---
type: open-question
name: F5 — memories per session, production anchor
status: OPEN
last_ingested: 2026-05-13
sources: [../source/emem-benchmark.md]
epistemic_tags: [asserted]
tags: [scale-model, data-gap, sensitivity-top-4]
---

## The question

What is the realistic distribution of **memories written per session** (F5) in production agentic-memory deployments? The scale model uses F5 as a per-session multiplier in the volume/throughput projections, and the tornado-plot identifies it as one of the [top-4 sensitivity drivers](../concept/scale-crossings.md) alongside `orchestration_depth`, `sessions_per_user_day`, and `tool_chain_amplifier`.

## Why it matters

F5 is the single largest **unanchored** parameter in the scale model.

- The 2026-04-30 audit nudged the central from 9 → 12 `[ASSERTED]` based on indirect signals (see [scale-model-audit-corrections](../decision/scale-model-audit-corrections.md)), but found **no vendor publishes** production memories-per-session data (audited Cognee, Mem0, Letta, Zep, LangMem, MemGPT).
- The closest empirical reference is the **EMem benchmark at 18-20 EDUs/session** `[ASSERTED]` ([EMem benchmark](../source/emem-benchmark.md)) — a synthetic benchmark, not production data.
- If F5 in production is materially below the central (e.g. ≤ 3), the LIMIT-1536d crossing dates push out and the urgency framing weakens. If above (e.g. ≥ 30, as orchestrated multi-agent workflows might produce), every scenario crosses sooner and the case strengthens.
- Because F5 is a per-session multiplier, error in F5 propagates linearly into total memory volume — there is no flattening regime.

## What evidence would resolve it

Any of:

1. **Vendor publication.** A production memory system disclosing memories-written-per-session at a representative customer scale. Currently zero such disclosures exist.
2. **Direct measurement.** Instrumenting an agentic system in production (e.g. AJ's MTP build per [BIG-PICTURE Goal 5 (archive)](../archive/BIG-PICTURE-2026-05-14.md)) and logging memories-written-per-session over a sustained period. The MTP is the cheapest path; n=1 (AJ) is a start.
3. **Independent benchmark replication.** A second benchmark beyond EMem reporting EDUs/session on comparable agent workflows. Would calibrate whether 18-20 is regime-typical or EMem-specific.
4. **Architectural inference.** If a system's distillation cadence and dedup policy are public, derive F5 indirectly. Letta's open-source code is the most promising candidate; not yet mined.

**Adequate signal**: a single production data point with a credible methodology would replace 12 with a measured value. The model's top-4 sensitivity status means even a rough anchor is worth the uncertainty reduction.

## Sub-questions

- Is F5 bimodal (heavy vs light users), parallel to the F2 bimodality finding? If so, the central is a misleading summary statistic.
- Does F5 scale with `orchestration_depth`? They co-occur in the top-4 — possible confound or genuine independent term.
- What's the right time-resolution? "Memories per session" hides regime differences between bursty distillation and continuous capture.

## Related

- [scale-crossings](../concept/scale-crossings.md) — the model output F5 drives.
- F2 bimodality (still n=1, post-hoc, not yet a wiki page).
- [BIG-PICTURE (2026-05-14 archive)](../archive/BIG-PICTURE-2026-05-14.md) — Goal 5 MTP is the cheapest path to a real F5 anchor; Goal 5 is bolt-on-path-specific, gated on the [current path-decision](../NOW.md).
- Full audit history with F5 central revision rationale lives in `project_kyrja_active.md` (container-local; pending full atomization into wiki).

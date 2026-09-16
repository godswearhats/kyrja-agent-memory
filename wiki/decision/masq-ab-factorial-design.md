---
type: decision
name: MASQ A+B factorial design (scientific rebuild)
status: SUPERSEDED
program: masq-bench
last_ingested: 2026-06-26
sources: [../source/du-2026-autonomous-memory-survey.md, ../source/he-2026-memoryarena.md]
tags: [masq, benchmark, experimental-design, statistical-power, pre-registration]
---

> **SUPERSEDED 2026-06-26 — the party×time interaction analysis is dead.**
> The 2×2 factorial (cells C1–C4, primary test = the ΔΔ interaction contrast,
> GLMM `B ~ party*time`) **failed the too-easy gate**: paste-everything scored
> 85%+ even at 400k, so the cells did not discriminate. v2 replaced the 2×2
> structure with **multi-scope confusability chains** (5 pinned scopes, single
> decision per scenario) — there is no party×time factor or C1–C4 cell in v2,
> so this doc's primary analysis has nothing to run on. This was forced by a
> pre-registered gate firing, not a goalpost move.
>
> **Live pre-registration:** `masq/harness/DESIGN-v2-analysis.md`.
> **Carried forward (still valid):** scenario-as-unit, the A+B two-layer scoring,
> closed exact-match answers, reader held constant = Opus (temp 0, cached),
> ceiling-normalisation, pre-registration discipline. **Died:** the party×time
> crossing, the C1–C4 cells, the ΔΔ interaction contrast, the `party*time` GLMM.

## Decision

Rebuild MASQ as a controlled factorial experiment whose **unit of analysis is an independent scenario** (not a query), crossing **party (single ↔ multi) × time (static ↔ evolved)**, with each scenario scored at **two layers — A (memory quality) and B (decision quality)** — and the headline result being the **party×time interaction on the B-layer**. This supersedes the prior "deterministic attribution scoring over the existing 12-week corpus" framing in [masq-paper-as-active-program](./masq-paper-as-active-program.md).

## Motivation

- **The existing corpus cannot support subgroup statistical claims.** [2026-06-08 corpus audit](../experiment/2026-06-08-masq-corpus-audit.md): ≈8 independent distinctive events, 500 queries pseudo-replicating them, strict cross-team supersession N=0. Rich narrative, low event-N.
- **The field's own eval stack separates the two layers.** [Du 2026](../source/du-2026-autonomous-memory-survey.md) §5.1: *"must jointly assess memory quality and decision quality"*; §5.4 four-layer stack. We operationalize it in the cell nobody occupies.
- **The passive→decision-relevant gap is real and large.** [MemoryArena](../source/he-2026-memoryarena.md) Table 3: PS ≈ 0.41–0.64, SR ≈ 0 — but single-agent. Our novelty = that gap **under cross-party temporal conflict**.
- **Strategic (AJ, 2026-06-08):** optimize for *independent + rigorous + finished*, not adoption. The underlying claim is methodological — *a vendor grading its own benchmark cannot expect to be believed*; an independent A+B result is the artifact.

## Commitments

- **Unit of analysis = independent scenario.** A scenario is a small, self-contained micro-world (few parties, one decision possibly evolving, controlled distractor bed, one closed ground-truth answer). Many independent scenarios (RULER-style), not one rich narrative.
- **Factorial: party × time.** C1 single-static (baseline), C2 single-evolved (pure temporal), C3 multi-static (pure attribution), **C4 multi-evolved (the thesis cell)**. C4 sub-conditions: *supersession* (A decided, B revised) and *unknowing collision* (B acts unaware of A's prior decision). Distractor-density held as a secondary analysis, not a third primary factor.
- **Matched scenario families (within-items).** Generate each micro-world once, derive one item per cell from it — same entities/haystack, varying only the factor. Each family is its own difficulty control; enables paired tests.
- **Two scored layers per scenario.** **A-layer (memory quality):** did it retrieve/attribute the right memory? Closed-set exact-match / set-F1 over known label sets. **B-layer (decision quality):** given the memory, did it take the correct *action*? Action is a **closed, checkable decision** (proceed / block / redirect / name-the-superseding-decision), never open essay. B-failure is mediated by A: *can't-retrieve* vs *retrieved-but-acted-wrong*.
- **B-layer output = closed pair (action, conflict_flag); C3 pass/fail = the flag (SURFACE), not escalation** *(refined 2026-06-09 by [gate 1](../experiment/2026-06-08-masq-gate1-c3c4-discriminability.md))*. The reader LLM is fixed across systems, so the B-decision is a probe of what memory delivered; surfacing is the only rubric whose variance is attributable to the memory system (gate 1: the fixed reader never escalates, even fully informed). Escalate-vs-flag-and-default = descriptive policy tier, no weight in the comparison matrix. A **uniform task preamble** (surface-termed conflict instruction, verbatim on every item, all cells, oracle included) prevents type-leak and makes C1/C2/C4 the **false-alarm arm**: the scored quantity is C3-hit vs non-C3-false-alarm discrimination, ungameable by always/never-flagging.
- **C3/C4 hinge = value-awareness; generation invariants locked** *(gate 1)*: COLLISION ⟺ second writer believes no value exists (explicit greenfield marker); SUPERSESSION ⟺ second writer aware a value exists by any route (explicit awareness marker); bare-set middle **banned — CONFIRMED by the [2026-06-09 bare-set probe](../experiment/2026-06-09-masq-bareset-probe.md)** (reader agreement 0/6 on unmarked items); C3 collided values genuinely incompatible; B-query asks for action-under-possible-conflict, never config state. Party-awareness (who set it) is an A-layer attribution property, not the B hinge.
- **Presupposition discipline in generated text** *(bare-set probe)*: presupposition verbs ("raising/bumping X to Y") are legible C4 **soft** markers (4/4 both readers; primary C4 marker stays explicit); C3 purpose clauses must be absolute/requirement-stated — no comparatives, counterfactual-present clauses, or capacity-relative framing (readers split inconsistently on whether these imply awareness; one reader fabricated an awareness route on an unmarked item). Generator QA samples C3 items for unintended awareness routes.
- **Closed answers throughout.** Every item's correct answer is a short closed token (name, team, date, decision-label, yes/no+reason) — kills the `token_f1`=1.0-on-garbage failure mode.
- **Reader held constant = Opus** via `claude -p`. Pinned model ID, **temperature 0**, **every reader output cached** for reproducibility. Report the **oracle ceiling** (perfect-retrieval → Opus) per cell as the normalizer so reader limits are factored out; scores = fraction of oracle recovered. Anchor the bottom with a no-memory/recency baseline.
- **Judge only for unavoidable open text, and validated.** If any item needs Opus-as-judge, report inter-rater reliability vs human on a sample (Cohen's κ).
- **Pre-registration (in-repo, before running any system):** unit = scenario; primary metric = oracle-normalized exact-match (A) + closed-action correctness (B); analysis = mixed-effects logistic `outcome ~ party*time + (1|family)`; multiple-comparison correction across cells; target N from a power calc. Planning floor **≈50 matched families (~200 items)** → ±14pp per-cell CI, 80% power for ~30pp between-cell effects; scale to ~100/cell for moderate (~20pp) effects.
- **Generation:** templated micro-worlds (structure) + LLM for surface realism (Maren can carry prose); regeneratable from seeds; held-out private split for contamination resistance.

## Reversibility

**Moderate.** The factorial scaffold and A/B layering are the load-bearing commitments; abandoning them means falling back to a single-cell "hard questions" benchmark (weaker, MemoryArena-adjacent). Cheap to reverse *before* generation scales — the open gate is a single worked C4 scenario family (all four cells + A/B ground truth + scoring), pressure-tested adversarially, which becomes the generation spec. Expensive to reverse after generation runs. Pre-registration is one-way by design (that's the point).

## Related

- Rests on [2026-06-08 corpus audit](../experiment/2026-06-08-masq-corpus-audit.md) (why rebuild) and [Du 2026](../source/du-2026-autonomous-memory-survey.md) (A/B precedent).
- Reframes [masq-paper-as-active-program](./masq-paper-as-active-program.md) (program scope) and [multi-party-attribution-gap](../concept/multi-party-attribution-gap.md) (positioning cell).
- Differentiates from [MemoryArena](../source/he-2026-memoryarena.md): decision-relevant use **× multi-party-temporal**, the cell it does not touch.
- **Gate 1 PASSED** ([2026-06-08 C3/C4 discriminability](../experiment/2026-06-08-masq-gate1-c3c4-discriminability.md)): collision-vs-supersession 100% legible to blind human + Opus on clear items, not a wall-clock artefact. The worked family (`masq/c4-worked-family.md`) is now the generation spec, as amended by that gate.
- **Bare-set probe LANDED** ([2026-06-09](../experiment/2026-06-09-masq-bareset-probe.md)): ban confirmed (0/6 agreement), whisper verbs admitted, C3 presupposition scrub added. Generation rules are now **frozen**.
- **Generator v0 built 2026-06-09** (`masq/generator/`): confusable-sibling embedding + independent invariant checker (`verify.py`, run on emitted text). **Open next steps:** Maren prose-realism pass, domain packs 2–3, oracle/baseline harness, emitted-kernel legibility recheck.

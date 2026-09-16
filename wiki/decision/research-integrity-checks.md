---
type: decision
name: Research integrity checks (silent-failure detection)
status: ACTIVE
last_ingested: 2026-05-26
sources: [../source/ars-academic-research-skills.md]
tags: [methodology]
---

## Decision

Adopt three standing integrity checks for our own AI-assisted research — a
pre-graduation checklist for experiment results, ground-truth isolation for any
scored experiment, and an independent-reader rule for load-bearing conclusions —
as additive discipline on top of the existing evidence-anchoring conventions.

## Motivation

- Our falsifiability discipline catches bad *reasoning*; it does not
  systematically catch failures that *look like competent work*. A result from a
  silent bug reads identically to a real one `[ASSERTED]` ([source](../source/ars-academic-research-skills.md)).
- Mechanisms adapted (not vendored) from [ARS](../source/ars-academic-research-skills.md);
  underlying failure taxonomy attributed by ARS to Lu et al. 2026, *primary
  unverified by us* (see source page's provenance caveat).
- Complements [evidence-anchoring](../concept/evidence-anchoring.md): that governs
  *claim*-provenance; this governs *result*-integrity. Two halves of "the wiki is
  trustworthy as research."

## Commitments

### 1. Pre-graduation checklist (notebook → `experiment/*`)

Before a result graduates from a notebook to a wiki experiment page, clear these.
Any "no" is a **hard block**, not a warning.

- **Provenance** — point to the saved run that produced the number; clean exit,
  zero warnings.
- **Suspicious cleanliness** — no unexplained round effect sizes (exactly 0.5, 2×
  baseline, zero variance); error bars/CIs differ across conditions rather than
  being suspiciously identical (a constant leaking through a broken pipeline).
- **Table-to-source** — every reported number traces to a CSV/log, not prose
  written from memory.
- **Surprise audit** — if the writeup says "surprisingly/unexpectedly," is there
  literature predicting the opposite? A first-run surprise on a fresh pipeline is
  a bug-suspect until reproduced from scratch.
- **Shortcut** — an ablation rules out the most obvious spurious feature (the
  result isn't the model reading a shortcut rather than the intended signal).

A fired block is not friction — it is a fork that pays out either way: it opens an
investigation resolving to **(a)** a confirmed defect caught before it reached the
wiki, or **(b)** a characterised false positive (which is exactly the
false-positive-rate data this discipline otherwise lacks). There is no bad outcome
from a block firing — only one we haven't done the due diligence on yet.

*Precedent in our own work:* the [ceiling probe](../experiment/2026-05-18-T_A1b-isolation-derisk/ceiling-probe.md)
caught both a shortcut (BoW decodes the arc patterns at 82%) and scaffolding
contamination — exactly modes this checklist targets.

### 2. Ground-truth isolation (design check — taint-tracking)

For any experiment with a gold set, scoring rubric, or LLM-judge: the answer-key
never shares a context window with what is generated or scored. Treat it as
information-flow control — `raw → verified → ground-truth`, one-way. Generation
runs on raw/verified only; ground-truth enters in a **separate invocation**
(separate instructions are not enough — a model that has seen the rubric orients
toward it). Failure to isolate inflates scores that then don't transfer
`[ASSERTED]` ([source](../source/ars-academic-research-skills.md)).

### 3. Independent reader for load-bearing conclusions (frame-lock)

A verifier sharing the generator's frame attacks arguments, never premises — so I
cannot fully audit my own analysis; I am frame-locked by construction `[ASSERTED]`
([source](../source/ars-academic-research-skills.md)). When a conclusion is
load-bearing, route the check to a genuinely different reader (external-Claude,
Ollama, [Maren/Anders](/team-share/)), not to me trying harder. The same
independence is what makes convergence from genuinely separate angles count as
evidence rather than echo.

## Reversibility

**Cheap.** These are authoring-time disciplines, not code or schema. Relaxing any
of the three costs nothing structural. Evidence that would justify reversal: the
pre-graduation checklist accumulating a high characterised-false-positive rate
with no true catches (track per §1's fork framing), or the isolation/independent-
reader checks proving redundant with existing evidence-anchoring in practice.

## Related

- [source/ars-academic-research-skills](../source/ars-academic-research-skills.md) — provenance.
- [concept/evidence-anchoring](../concept/evidence-anchoring.md) — the claim-provenance half.
- `feedback_concession_discipline` (project memory) — the conceding-side self-rule
  derived from the same ARS source; container-only, not yet atomised.

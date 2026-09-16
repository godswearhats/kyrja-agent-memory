# Gate 1 — Result: PASSED (with one decision parked)

**Date:** 2026-06-08 (Nils/indigo). **Status:** the C3/C4 thesis cell is validated.

## What gate 1 tested

Before building any generator: *is the collision-vs-supersession distinction
reliably legible from the TEXT (intent/awareness), with **no recourse to
wall-clock**?* If a human and a neutral Opus can't tell them apart, the 2×2 loses
its thesis cell and we'd retreat to a 3-cell design. Pass bar: **≥90% on the
"clear" items, for both readers**; 2 boundary items held out as diagnostic.

Method: 10 blind transcripts (`transcripts.md`), each a target fact set by two
parties, embedded with sibling distractors. Traps planted: collisions with large
time gaps, supersessions same-day, strong-verb collisions, soft no-name
supersessions — so wall-clock and surface verbs can't be used as shortcuts.
Readers: AJ by hand (`aj-answers.md`); neutral Opus via `claude -p` (`run_opus.py`
→ `opus-results.json`). Hidden key: `key.json`.

## Result

**Clear items (8): three-way agreement AJ ⟷ Opus ⟷ key = 100% (8/8).** Held
against every misdirection trap (#2 collision/2-mo gap, #5 supersession/same-day,
#6 strong-verb collision, #7 soft supersession). → **The C3/C4 distinction is
legible to both a human and a model, and is NOT a wall-clock artefact.**

**Boundary items (#4, #8): convergent.** AJ and Opus *independently* both
classified SUPERSESSION **and** both spontaneously wrote "arguably unclear." Two
observers, same pull toward ambiguity, same resolution. → see decision below.

## Decisions LOCKED by this gate

1. **The thesis cell survives** — proceed with the 4-cell (party × time) design.
2. **Value-awareness is the hinge** (confirmed from two independent directions):
   - COLLISION ⟺ second writer believes **no value exists yet** (greenfield).
   - SUPERSESSION ⟺ second writer is aware a value exists **by any route**
     (symptom, library default, prior value, named person) and changes it.
   - Corollary: *party*-awareness (knowing *who* set it) is an **A-layer /
     attribution** question, NOT the B-layer action hinge. #4/#8 are *party-blind
     supersessions* — value changed without knowing who set it. Clean A/B split.

## Decision RESOLVED 2026-06-09: SURFACE is the C3 B-layer pass/fail

Confirmed with AJ after working the rationale from the benchmark's purpose: the
LLM is held fixed across memory systems, so the B-layer decision is a **probe of
what memory delivered**, not an evaluation of the LLM. "Surface" is the only
rubric under which B-variance is attributable to the memory system — gate 1
showed the fixed reader essentially never escalates even with perfect
information, so an "escalate" bar flattens the metric (including the oracle
ceiling) and stops discriminating between memory systems. Escalation is logged
as a descriptive tier with no weight in the comparison matrix.

Two construction invariants locked with the decision:

1. **Task preamble states the expected behavior, in surface terms** (e.g. "if
   your records show different people set conflicting values for the same
   setting, say so explicitly rather than silently choosing one"). Policy-neutral
   wording — instructing "escalate" would confound memory with
   instruction-following of a disputable policy. AJ's gate-1 grading experience
   (state-quiz framing, action-rubric scoring) is the direct evidence the
   briefing is required.
2. **The preamble appears verbatim on EVERY item** (C3, C4, clean singles) so its
   presence leaks nothing — and this turns C4 supersessions into the
   **false-alarm arm**: flagging a legitimate, value-aware supersession as a
   conflict is over-flagging. Score = discrimination (C3 hit rate vs C4
   false-alarm rate), ungameable by always- or never-flagging. The oracle ceiling
   receives the same preamble.

Original parked question, kept for the record: **"surface" (capability) or
"escalate" (policy)?**

Origin: AJ correctly classified all four collisions, then reported the **recent
value** for each (e.g. #1: took Marcus's 60-min TTL over Priya's 30-min). He was
describing "what's in the config now," and noted he hadn't realised escalation was
the intended action. This is itself the finding — *a careful engineer who detects
the collision still defaults to recency*, reproducing the exact memory-system
failure C3 is built to catch (A-layer correct, B-layer recency: the A/B
decoupling, in a human).

Nils's recommendation (per AJ's own *capabilities-not-policies* principle):

> **C3 B-layer primary pass/fail = "did the system SURFACE the conflict?"** —
> reveal that two parties set incompatible values, rather than silently return one
> as authoritative. Whether it then *escalates* vs *picks-safer-default-and-flags*
> is a **policy**, scored as a secondary reported tier, not pass/fail.

More defensible (no policy dispute), matches AJ's data, mirrors the A/B split
(detect = capability; resolve = policy). **AJ to confirm or override.**

## Construction requirements this gate forces (contingent on the parked call)

- C3 collided values must be **genuinely incompatible** (security-vs-UX, not
  50-vs-100), so "surface it" is unambiguously better than "pick one."
- Generation invariant: explicit **greenfield** marker (C3) / explicit
  **value-awareness** marker (C4); **ban the bare-set middle** ("set X to Y" with
  neither marker) — that's the one genuinely-ambiguous case and the next probe.
- B-layer query must ask unambiguously for the **correct action under possible
  conflict**, not the config *state* — else readers answer the state question and
  look "wrong" (exactly what happened by hand).

## Reader-bias note for the benchmark proper

Opus **never** chose UNCLEAR — it resolves rather than escalates. So in C3 cells,
even with perfect memory, the reader under-escalates, depressing absolute C3
scores. Mitigation already in the design: the **oracle-ceiling normaliser absorbs
this, provided the oracle is handed the faithful *contested* memory state** (two
parties, conflicting values, unreconciled) — NOT a pre-resolved answer — so it
*can* surface/escalate. Wire the oracle that way.

## Files

`build.py` (canonical builder) · `transcripts.json` (+ prompt) · `transcripts.md`
(human-blind) · `key.json` (hidden) · `aj-answers.md` · `run_opus.py` ·
`opus-results.json` · this file.

## Next

1. ~~AJ makes the parked surface-vs-escalate call.~~ DONE 2026-06-09 — surface.
2. Fold gate-1 outcome into `decision/masq-ab-factorial-design.md` (wiki) +
   `c4-worked-family.md`; log a formal `experiment/` page for the gate.
3. Build the **confusable-sibling embedding** + the **true bare-set boundary
   probe**.

---
type: experiment
name: MASQ gate 1 — C3/C4 collision-vs-supersession discriminability (2026-06-08)
status: LANDED
program: masq-bench
last_ingested: 2026-06-09
epistemic_tags: [MEASURED]
tags: [masq, benchmark, gate, construct-validity, c3-c4, discriminability]
---

Pre-build gate for the MASQ rebuild: before writing any generator, test whether
the collision-vs-supersession distinction — the thesis cell of the
[party×time factorial](../decision/masq-ab-factorial-design.md) — is reliably
legible from transcript text alone, by intent/awareness, with **no recourse to
wall-clock**. **Result: PASSED.** The gate also produced two unplanned findings
(the value-awareness hinge; a recency-default in a careful human reader) that
materially changed the B-layer scoring design.

## Hypotheses tested

- Carried-forward gate #1 from the worked family
  (`masq/c4-worked-family.md` §5 attack #1 / §6): *"C3
  (unknowing collision) and C4 (intentful supersession) can be told apart by a
  blind human AND a neutral Opus reader at ≥90% on clear items, using intent
  language rather than wall-clock order."* If false, the 2×2 loses its thesis
  cell and the design retreats to 3 cells. **Verdict: supported (100% on clear
  items, both readers).**

## Method

- Built 10 blind transcripts (`build.py` → `transcripts.md`), each one target
  fact set by two parties, embedded among sibling distractors. Ground-truth
  labels hidden in `key.json`; 8 items pre-assigned "clear", 2 ("#4", "#8")
  pre-assigned "boundary" and held out as diagnostics, not counted toward the
  pass bar.
- **Misdirection traps planted so wall-clock and surface verbs cannot serve as
  shortcuts:** a collision with a 2-month gap (#2), a same-day supersession
  (#5), a strong-verb ("overriding") collision (#6), a soft no-name supersession
  (#7). Any reader using recency or verb strength fails these by construction.
- Readers, independent and blind to the key: **AJ by hand** (`aj-answers.md`)
  and **Opus** via `claude -p` (`run_opus.py` → `opus-results.json`).
- Pass bar pre-registered: ≥90% on clear items for **both** readers.

## Results

- **Clear items: 8/8 (100%) three-way agreement** AJ ⟷ Opus ⟷ key, including
  all four traps. `[MEASURED]` The distinction is legible to both a human and a
  model and is **not a wall-clock artefact**.
- **Boundary items (#4, #8): convergent ambiguity.** Both readers independently
  chose SUPERSESSION *and* independently volunteered "arguably unclear" — same
  pull, same resolution. These are *party-blind supersessions* (value changed
  with awareness a value exists, without knowing who set it), which cleanly
  splits party-awareness (an A-layer/attribution property) from
  value-awareness (the B-layer action hinge).
- **Unplanned finding 1 — the value-awareness hinge.** Classification tracked
  one variable from two independent directions: COLLISION ⟺ second writer
  believes no value exists yet (greenfield); SUPERSESSION ⟺ second writer is
  aware a value exists by any route and changes it. This becomes the
  generation-invariant definition of the C3/C4 boundary.
- **Unplanned finding 2 — recency-default in a careful human.** AJ correctly
  classified all four collisions (A-layer perfect), then reported the *recent*
  value as "the answer" for each — reproducing, in a vigilant human, the exact
  recency failure the C3 cell is built to catch. Root cause: the query read as
  a state-quiz, not an action question. This forced the B-query construction
  requirement below.
- **Reader-bias observation.** Opus never chose UNCLEAR — it resolves rather
  than escalates, even when it detects contest. Implication: an "escalate"
  B-rubric would flatten C3 scores (including the oracle ceiling) for reasons
  attributable to the fixed reader, not the memory system under test.

### Construct validity

The metric is blind classification accuracy against *generator-intended*
labels. It measures whether the intent markers the builder wrote are legible —
i.e., that ground truth for C3/C4 can be **manufactured reliably** — not that
collisions and supersessions are separable in naturally occurring text at any
particular rate. That is exactly the property a synthetic-benchmark gate needs,
and nothing more; external-validity claims about real transcripts remain out of
scope (v2 write-noise arm).

## Decisions resulting (resolved 2026-06-09 with AJ)

1. **Thesis cell survives** — proceed with the 4-cell party×time design.
2. **C3 B-layer pass/fail = SURFACE, not escalate.** Since the reader LLM is
   held fixed across memory systems, the B-layer decision is a *probe of what
   memory delivered*; "did the output surface the conflict" is the only rubric
   under which B-variance is attributable to the memory system (see reader-bias
   observation). Escalate-vs-flag-and-default is logged as a descriptive policy
   tier with no weight in the comparison matrix.
3. **Uniform task preamble, verbatim on every item** (all cells), instructing
   in surface terms ("if records show different people set conflicting values,
   say so rather than silently choosing one"). Prevents the instruction from
   leaking item type, and turns non-collision cells into the **false-alarm
   arm**: the scored quantity is discrimination (C3 hit rate vs C1/C2/C4
   false-alarm rate), ungameable by always- or never-flagging. The oracle
   ceiling receives the same preamble and a faithful *contested* memory state.
4. **Generation invariants:** C3 carries an explicit greenfield marker; C4 an
   explicit value-awareness marker; the bare-set middle ("set X to Y", neither
   marker) is **banned from the corpus** pending the bare-set boundary probe.
5. **C3 collided values must be genuinely incompatible** (e.g. security-vs-UX),
   so surfacing strictly dominates picking either.
6. **B-query asks for the correct action under possible conflict**, never the
   config state (forced by unplanned finding 2).

## Limitations

- N=10, single domain (config values), one builder (Nils) — legibility of
  *builder-authored* traps may exceed that of generator-emitted items at scale;
  re-check on a generator sample.
- AJ was blind to the key but not to the program's goals; a fully naive human
  reader would strengthen the claim.
- The 2 boundary items were pre-assigned by the builder, so the clear/boundary
  split is itself an authored judgment.

## Raw artifacts

- `masq/gate1/` — `RESULTS.md` (narrative),
  `build.py`, `transcripts.{json,md}`, `key.json`, `aj-answers.md`,
  `run_opus.py`, `opus-results.json`.

## Related

- Closes the open gate in [masq-ab-factorial-design](../decision/masq-ab-factorial-design.md)
  and in the worked family (`masq/c4-worked-family.md` §6).
- Refines the B-layer commitment in that decision page (surface rubric, uniform
  preamble, false-alarm arm) — propagated 2026-06-09.
- Next probes queued: **bare-set boundary probe** (is the unmarked "set X to Y"
  genuinely ambiguous, justifying invariant #4?) and the **confusable-sibling
  embedding** build.

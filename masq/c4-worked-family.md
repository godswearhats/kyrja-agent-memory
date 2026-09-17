# Worked Scenario Family #1 — "checkout-rate-limit"

> **SUPERSEDED — the 2×2 design described here was abandoned.** The party×time
> factorial and its C1–C4 cells failed a pre-registered "too easy" gate (paste
> scored 85%+ even at 400k) and were replaced by multi-scope confusability chains
> with a single decision per scenario. There is no C1–C4 cell in the shipped
> benchmark. The marker-discipline rules below *did* carry forward into
> `generator/verify.py`. Live spec: `harness/DESIGN-v2-analysis.md`.


**Status:** DRAFT for adversarial pressure-test (2026-06-08, Nils/indigo).
**Purpose:** One micro-world rendered into all four factorial cells, with exact
A-layer and B-layer ground truth + scoring for each. If it survives the attack
list at the bottom, it becomes the generation spec. If it doesn't, we learn that
cheaply, before building a generator.

Design doc this implements: `decision/masq-ab-factorial-design.md` (wiki).

---

## 0. The micro-world (held constant across all four cells)

A small platform team operates an HTTP API. The contested fact is a single
closed-set quantity:

> **The request rate limit (req/s) for the `/checkout` endpoint.**

Two values appear in the world: **100** and **300**.
Two parties appear in the world: **Alice** and **Bob** (peers; both have
write authority over service config — stipulated, so no role tie-break is needed).

Only **two dimensions are manipulated** across cells:

- **Party**: does one person touch the fact, or two?
- **Time**: does the fact get revised after its first assertion, or not?

Everything else — endpoint, the two candidate numbers, the surrounding session
chatter, the query wording — is held fixed. That fixity is what makes the four
cells a *matched family* and lets us read the party×time **interaction** instead
of a confounded main effect.

### The action space (held constant across all four cells)

Both the B-layer query and its scoring use ONE closed action set:

```
A_set = { set_100, set_300, set_other, escalate }
```

`escalate` = "do not configure a value; flag that the team has no single agreed
value and surface the conflict." Holding this set constant across cells is
load-bearing: a cell's *correct* action differs because the *world* differs
(that's the manipulation), not because the question or option menu changed.

> **AMENDED by gate 1 (§7, 2026-06-09):** the B output is now the closed pair
> `(action, conflict_flag)`; C3 pass/fail moves from the `escalate` action to
> `conflict_flag = true` (surface). `escalate` remains in the action set but is
> scored as a descriptive policy tier. §7 is authoritative where it conflicts
> with §0/§3.

---

## 0.5 — What the system actually sees: kernel ⊕ embedding

The four cells below define the **kernel** — the logical structure (party × time)
and its scored answer. **The kernel is the unit of ground truth, never what the
system reads.** A 5-session kernel fits trivially in a prompt; on its own it is a
context-stuffing problem, not a memory problem. The benchmark *item* the system
faces is the kernel **embedded** in a large, confusable corpus, and the kernel is
all we score.

The embedding has two **orthogonal** axes. A task needs a *memory system* (vs
stuffing the corpus in context) only when the embedding is hard enough on at least
one of them:

**(a) Distractor density — horizontal — defeats keyword/embedding match.**
The micro-world is not one endpoint but ~8 business-ambiguous siblings
(`/checkout`, `/search`, `/cart`, `/login`, `/reports`, …) — the "many auth
systems" structure of the original corpus, where the names are similar enough that
surface match is useless and you must bind by context. The adversarial invariant:
**every wrong answer is a real value for some other sibling.**

> `/search`'s limit is *legitimately* 300. `/checkout` was revised 100 → **300**
> too. Now the token "300" is at once a distractor (it's /search's value) **and**
> the answer (it's /checkout's current value). "rate limit", "300", "Bob" recur
> across every sibling, so the system must bind value → endpoint → party → time by
> *context*, not by matching.

This *gates* the C3/C4 trap rather than competing with it: before a system can
reason about supersession-vs-collision on /checkout, it must first isolate *which*
of dozens of "rate limit" writes are even about /checkout. Two failures stacked —
selection, then reasoning.

**(b) Volume — vertical — defeats fit-in-window.** Grow the corpus (more
siblings, more sessions, more chatter) until the raw history exceeds, or
swamps-by-selectivity, the reader's window.

### The architecture bake-off (this is where "needs memory" is *measured*)

All arms feed the **same** Opus reader; they differ only in what context reaches it:

- **Long-context baseline** — reader gets as much raw corpus as fits. This is
  "just stuff it in context," the thing we expose.
- **Memory-system arm** — Mem0 / Zep / … ingests the corpus, then at query time
  retrieves a *bounded* slice for the reader.
- **Oracle** — reader handed exactly the GT-relevant facts (per-family ceiling).
- **No-memory / recency** — lower bound.

A task "needs memory" precisely when the long-context baseline **can't win** —
Du §5.5 ("long context is not memory") is a claim about *selectivity*, not only
size, so distractor density bites even within the window.

### Don't pick a corpus size — sweep it

Hold the kernel fixed; grow the embedding; measure **where the long-context
baseline falls off the memory arm.** That **crossover is itself the headline
finding** — it turns "long context isn't memory" from a borrowed assertion into a
*measured curve*. (Distributed-systems read: long-context = full table scan,
memory system = an index; the index only wins once the table is big and selective
enough that scanning is wasteful. The crossover is the query planner's
index-vs-scan threshold.)

So the full design is **two orthogonal manipulations**: the (party × time)
**2×2 of reasoning** (the kernel), crossed with a **sweep of embedding
difficulty** (distractor density × volume). We score the kernel as a function of
embedding size.

---

## 1. The four cells (the kernel)

Each cell is a short multi-session transcript. `S#` = session, timestamped.
Sessions contain realistic chatter; the load-bearing sentence is **bolded**.

### C1 — single-static (baseline / ceiling)

> **S1 (Alice, day 1):** perf review of /checkout. "Latency's fine under load.
> **I'm setting the /checkout rate limit to 100 req/s** — that's where p99 stays
> flat in the soak test." (No later session touches the limit.)

- One party, no revision. This is the easy corner; it sets the per-family ceiling.

### C2 — single-evolved (pure temporal)

> **S1 (Alice, day 1):** *(identical to C1 S1)* "**…rate limit to 100 req/s** …"
> **S5 (Alice, day 12):** "Black-Friday capacity test came back. 100 is
> throttling legit traffic. **I'm raising the /checkout limit to 300 req/s.**"

- One party, intentful revision. Same person supersedes herself. Isolates the
  **time** dimension against C1.

### C3 — multi-static (pure attribution / unknowing collision)

> **S1 (Alice, day 1):** *(identical to C1 S1)* "**…rate limit to 100 req/s** …"
> **S2 (Bob, day 1, parallel session):** capacity planning for the sale. Bob has
> *not* seen Alice's session. "Nothing's configured yet for /checkout as far as I
> can see — **I'm setting its rate limit to 300 req/s** for the sale." (Neither
> session references the other; no later session reconciles them.)

- Two parties, **no intentful revision** — a concurrent collision. Same day, no
  awareness, no supersession language. Isolates the **party** dimension against
  C1. The trap: there is no defensible single value; the world is genuinely
  unresolved.

### C4 — multi-evolved (the thesis cell)

> **S1 (Alice, day 1):** *(identical to C1 S1)* "**…rate limit to 100 req/s** …"
> **S5 (Bob, day 12):** "Saw Alice set /checkout to 100 last week. Capacity test
> says that's throttling real traffic. **I'm overriding it to 300 req/s** —
> flagged in the change log, Alice is aware." (Intentful, ordered, cross-party
> supersession.)

- Two parties **and** intentful revision. Bob knowingly supersedes Alice.
  Isolates the **party×time interaction**.

---

## 2. The discriminative trap (why this family is worth building)

Look at C3 vs C4. **Same two parties, same two values (100 vs 300), same wall-clock
ordering (the 300-write comes after the 100-write).** The *only* difference is
**intent**: in C4 the second write knowingly supersedes the first; in C3 it is an
unaware concurrent collision.

Therefore:

- A **last-write-wins / recency** heuristic gets C4 right (300) and **C3 wrong**
  (it should escalate, recency picks 300).
- An **always-flag-on-conflict** heuristic gets C3 right (escalate) and **C4
  wrong** (it should resolve to 300, the heuristic escalates).

**No party-blind or time-blind heuristic passes both C3 and C4.** Passing both
requires modelling *supersession intent vs concurrent collision* — which is
exactly the capability "institutional/team memory" vendors claim and, per our
thesis, do not have (retrieve-and-inject is recency-or-similarity, both
intent-blind). The C3/C4 pair is the **falsifiable core** of the benchmark: a
system that can't separate these two will score at chance on the pair regardless
of how good its raw recall is.

This is also why the headline is the **interaction**, not a main effect: the
interesting signal is precisely that C4−C3 ≠ C2−C1.

---

## 3. Ground truth

### A-layer (memory quality) — closed-set fields, exact-match each

Query (identical across cells): *"As of now, what is the /checkout rate limit?
Who set the current value? Was it ever changed — if so, from what, by whom?"*

| field | C1 | C2 | C3 | C4 |
|---|---|---|---|---|
| `current_value` | 100 | 300 | **contested** | 300 |
| `current_setter` | Alice | Alice | **contested {Alice,Bob}** | Bob |
| `was_changed` | no | yes | **n/a (collision, not revision)** | yes |
| `prior_value` | — | 100 | — | 100 |
| `prior_setter` | — | Alice | — | Alice |

A-score = mean exact-match over the *applicable* fields for that cell (a cell's
GT defines which fields are scored). `contested` is a first-class allowed value —
emitting a single value where GT is `contested` is wrong; emitting `contested`
where GT is a single value is wrong.

### B-layer (decision quality) — single closed action, exact-match

Query (identical across cells): *"Configure the rate limiter for /checkout to the
value the team has agreed on. If there is no single agreed value, do not
configure — escalate and surface the conflict."*

| | C1 | C2 | C3 | C4 |
|---|---|---|---|---|
| correct action | `set_100` | `set_300` | `escalate` | `set_300` |

B-score = 1 if action matches GT, else 0.

> **AMENDED by gate 1 (§7, 2026-06-09):** B ground truth is now
> `(action, conflict_flag)` — C1 `(set_100, false)`, C2 `(set_300, false)`,
> C3 `(any, **true**)`, C4 `(set_300, false)`. The B-query gains a uniform
> surface-termed preamble on every cell. See §7.

### The A/B decoupling (why we score both)

- **Pass A, fail B** (C4): a system recalls the full history *(100/Alice →
  300/Bob)* but mis-resolves — e.g. surfaces both and picks 100, or escalates.
  Good memory, bad decision.
- **Pass B, fail A** (C4): a system blindly picks 300 by recency — correct action
  — but can't report that the value was changed from 100 by Bob over Alice. Good
  decision by luck, no memory.
- **A and B are therefore non-redundant.** B is *not* A restated; it adds the
  resolution step (pick-current vs escalate). This is the whole reason Du §5.1
  ("jointly assess memory quality *and* decision quality") is the literature
  anchor.

---

## 4. Scoring & statistics (this family's role)

- **Unit of analysis = one (family × cell) outcome.** This document is **one
  family**. The four cells are four *paired* observations sharing a micro-world;
  the pairing is what the `(1|family)` random intercept models. Multiple A-fields
  within a cell are NOT independent replications — A is one composite per cell.
- **Reader = Opus** (`claude -p`, temp 0, pinned build, cached), held identical
  across all four cells. Report the **oracle-ceiling normaliser**: an oracle that
  is *handed* the correct GT memory still has to choose the action; we divide raw
  B by that oracle's B to factor out reader competence and isolate the memory
  system's contribution.
- **No-memory / recency lower bound**: a stub that always returns the most-recent
  write. By construction it scores: C1 ✓, C2 ✓, **C3 ✗**, C4 ✓ → it passes 3/4
  on B. *That is the point*: the benchmark's discriminating power lives almost
  entirely in **C3**, and any aggregate that doesn't break out the C3/C4 contrast
  will look deceptively easy. (Flag for the metric design: the headline must be
  the interaction / the C3 cell, not mean-over-cells.)
- **Power**: with a closed 4-action B-layer, chance = 25%. To detect a ~30pp
  interaction at 80% power we pre-registered ≈50 families/cell (±14pp CI). This
  worked family is N=1; it validates the *construction*, not the *statistics*.

---

## 5. Adversarial pressure-test (attack the family before it breeds)

| # | Attack | Verdict | Mitigation baked in |
|---|---|---|---|
| 1 | **C3 is secretly a supersession** (Bob's 300 is just "the world moved on"). | **Real risk** — the whole family rests on C3≠C4 being principled, not a labelling trick. | C3's two writes are **same-day, parallel, mutually unaware**; C4's is **ordered, days later, explicitly references and overrides Alice**. The discriminator is **intent language**, not wall-clock. If a human can't tell C3 from C4 by reading, the family is void. *(This must be a generator invariant + human-check.)* |
| 2 | **Recency luck in C3.** A recency stub "happens to" pick 300 in C3. | Not a flaw — it's **scored wrong** (GT=escalate). This is the designed trap, not leakage. | — |
| 3 | **B reducible to A** (decision is just retrieval restated). | **Refuted.** Both-direction decoupling shown in §3: pass-A-fail-B and pass-B-fail-A both exist in C4. | A includes a resolution step absent from raw recall. |
| 4 | **Difficulty confound** (C1 trivial, C4 hard → main-effect artdefact). | **Controlled, not eliminated.** | Matched micro-world + the **interaction** contrast nets out per-cell difficulty; C1 is explicitly the per-family ceiling, not a peer cell. |
| 5 | **Authority ambiguity** ("agreed value" undefined when Alice & Bob disagree). | **Real — would poison GT if unaddressed.** | Stipulated: **peers, equal write authority, supersession-by-explicit-intent**. C2 single-party ⇒ self-supersession is unambiguous; C4 ⇒ Bob's explicit override is the agreement; C3 ⇒ no intent ⇒ no agreement ⇒ escalate. Roles are a fixed family parameter. |
| 6 | **Over-escalation contaminates C1/C2/C4.** A timid system flags conflict where none exists. | **Feature, not bug.** | `escalate` is in the action set for *every* cell; wrongly escalating C1/C2/C4 is a real decision-quality failure and is penalised. Uniform action set guarantees this. |
| 7 | **Closed-set guessing** inflates scores (25% floor). | **Acknowledged**, handled at the design layer. | No-memory baseline + ≥50 families/cell + interaction (not raw accuracy) as headline. N=1 here can't carry it. |
| 8 | **Reader (Opus) variance / non-determinism.** | Held constant + oracle-normalised. | temp 0, pinned, cached; oracle-ceiling divides it out. |
| 9 | **Surface-form leakage** — a bolded sentence makes retrieval trivially keyword-matchable. | **Defeated in v1 by the embedding (§0.5a), not deferred.** | The confusable-siblings invariant — every wrong answer is a real value for another sibling — kills *corpus-level* keyword/embedding match: "300", "rate limit", "Bob" recur everywhere, so surface match can't bind to the right endpoint. What remains for v2 is *intra-write* noise (messy phrasing of an individual write); that's a separate, named external-validity arm, not a v1 claim. Don't conflate corpus-confusability (in v1) with write-noise (v2). |
| 10 | **Single domain (config value).** Does the family generalise beyond numbers? | Open. | The schema (one contested closed-set fact, two values, two parties, intent-flag) is domain-agnostic; rate-limit is the *first* family. Generation plan must span ≥3 domains (config value, ownership/assignment, policy/decision) to rule out a numeric-only effect. |

### Surviving concerns to carry forward (not blockers)

- **Attack #1 is the load-bearing one.** The entire benchmark's validity reduces
  to: *can C3 and C4 be reliably told apart by intent, by both a human and the
  oracle reader, with no recourse to wall-clock?* → **Pre-build check:** hand 10
  blind C3/C4 transcripts to a human (AJ) AND to Opus-as-reader; require ≥90%
  correct collision-vs-supersession classification before scaling the generator.
  If that fails, the factorial collapses to a 3-cell design (drop the C3/C4
  distinction) — better to learn now.
- **Attack #9/#10** define the v1 scope boundary explicitly: clean writes, ≥3
  domains, reasoning-gap-not-extraction-gap. Written down so we don't silently
  overclaim.

---

## 6. Verdict

The family **survives** the attack list with two carried-forward gates:

1. **The C3/C4 intent-discriminability check** (Attack #1) — a hard pre-build
   gate. If humans+oracle can't separate collision from supersession ≥90% blind,
   the 2×2 loses its thesis cell and we retreat to a 3-cell design.
2. **Scope honesty** (Attacks #9/#10) — v1 = confusable-sibling embedding (corpus
   keyword match defeated) + size-sweep + ≥3 domains. *Intra-write* noise (messy
   individual writes) is a named v2 external-validity arm, not a v1 claim.

If gate 1 passes, **this family is the generation spec**: one contested closed-set
fact, two values, two parties, a fixed action set including `escalate`, and the
intent-flag as the C3/C4 hinge.

**Immediate next action:** run gate 1 (the blind C3/C4 discriminability check)
before writing any generator.

---

## 7. Gate 1 outcome & B-layer revision (2026-06-09) — AUTHORITATIVE AMENDMENTS

Gate 1 **PASSED** — formal record:
[wiki experiment page](../wiki/experiment/2026-06-08-masq-gate1-c3c4-discriminability.md);
raw artifacts in `gate1/`. Clear items 8/8 three-way (AJ ⟷ Opus ⟷ key), traps
held; the C3/C4 distinction is legible from intent and is not a wall-clock
artefact. **This family is now the generation spec, as amended below.**

### 7.1 The C3/C4 hinge is value-awareness (replaces "intent language" loosely)

- COLLISION ⟺ the second writer believes **no value exists yet** (greenfield).
- SUPERSESSION ⟺ the second writer is **aware a value exists by any route**
  (symptom, library default, prior value, named person) and changes it.
- Party-awareness (knowing *who* set it) is an A-layer attribution property,
  not the B hinge — gate-1 boundary items #4/#8 are party-blind supersessions.

### 7.2 B-layer output schema (supersedes §0 action set and §3 B table)

B output is the **closed pair** `(action, conflict_flag)`:

```
action        ∈ { set_100, set_300, set_other, none }
conflict_flag ∈ { true, false }   # "different people set conflicting values,
                                  #  unreconciled" — surfaced in the output
```

| | C1 | C2 | C3 | C4 |
|---|---|---|---|---|
| B pass/fail | `set_100` ∧ ¬flag | `set_300` ∧ ¬flag | **flag** (action recorded, unscored) | `set_300` ∧ ¬flag |

Rationale (locked with AJ 2026-06-09): the reader LLM is fixed across memory
systems, so the B decision is a **probe of what memory delivered**. Gate 1
showed the fixed reader essentially never escalates even when fully informed —
an "escalate" pass bar flattens C3 (oracle ceiling included) with variance
attributable to the reader, not the memory system. "Surface" is the floor every
defensible conflict policy shares, and the only rubric under which B remains a
memory measurement. **Escalate vs flag-and-default vs ask** is logged from the
recorded action as a descriptive policy tier, with no weight in the matrix.

### 7.3 Uniform task preamble (new construction invariant)

The B-query is prefixed, **verbatim on every item in every cell**, with a
surface-termed instruction, e.g.:

> "If your records show that different people set conflicting values for the
> same setting and the conflict was never resolved, say so explicitly rather
> than silently choosing one."

- Uniformity means the preamble's presence carries zero information about cell
  type (no leak), and it makes C1/C2/C4 the **false-alarm arm**: flagging a
  clean single-write or a legitimate value-aware supersession is a scored
  failure (¬flag required). The discriminative quantity is C3-hit-rate vs
  false-alarm-rate — ungameable by always- or never-flagging. (Strengthens
  attack #6's "feature, not bug.")
- Origin: AJ's gate-1 grading — A-correct on all four collisions yet reported
  recent values, because the query read as a state-quiz. We score only behavior
  we explicitly asked for; the B-query asks for action-under-possible-conflict,
  never config state.
- The **oracle ceiling gets the same preamble** and is handed the faithful
  *contested* memory state (two parties, conflicting values, unreconciled),
  never a pre-resolved answer.

### 7.4 Generation invariants (additions)

- C3 second write carries an **explicit greenfield marker**; C4 second write an
  **explicit value-awareness marker**.
- The **bare-set middle** ("set X to Y", neither marker) is **banned** —
  **CONFIRMED 2026-06-09** by the bare-set probe (`../bareset-probe/RESULTS.md`;
  wiki: `experiment/2026-06-09-masq-bareset-probe.md`): reader agreement 0/6 on
  unmarked items; Opus defaults unmarked → COLLISION (not recency) and
  fabricated an awareness route on one item.
- **Presupposition verbs ("raising/bumping X to Y") admitted as C4 _soft_
  markers** (probe: 4/4 both readers); the primary C4 marker stays explicit.
- **C3 presupposition scrub** (probe): C3 purpose clauses must be
  absolute/requirement-stated — no comparatives ("fewer", "more headroom"), no
  counterfactual-present ("so X doesn't keep happening"), no capacity-relative
  framing ("burst capacity"). These read as awareness routes to some readers
  and not others; reserve them for C4. Generator QA samples C3 items for
  unintended awareness routes.
- C3 collided values must be **genuinely incompatible** (security-vs-UX, not
  50-vs-100), so surfacing strictly dominates picking either.
- Re-verify trap legibility on a generator-emitted sample before scaling
  (gate 1 tested builder-authored items; authorship may inflate legibility —
  and the probe showed the same builder *leaks* presuppositions unintentionally,
  so both error directions are live).

---

## 8. Presentation layer, I8, and the chains deferral (2026-06-10) — AMENDMENTS

Locked with AJ 2026-06-10. Code keeps C1–C4 / A / B as internal IDs; all
prose-facing artifacts (paper, README, results tables) lead with these names.

### 8.1 Plain-English naming layer

| internal | public name | one-line story |
|---|---|---|
| family | **scenario** | teammates configure a shared setting |
| C1 | **Set once** | Alice sets the limit; nobody touches it again |
| C2 | **Self-update** | Alice sets it, later changes her own mind |
| C3 | **Collision** | Alice and Bob set it independently, unaware, unresolved |
| C4 | **Override** | Bob sees Alice's value and knowingly changes it |
| A-layer | **Memory score** | "What happened?" — right history, incl. "contested" |
| B-layer | **Decision score** | "What now?" — apply the settled value or surface the conflict |
| C3 flag hit | **collisions caught** | spoke up on a live disagreement |
| FA rate | **false alarms** | cried wolf on settled history |
| long-context arm | **paste-everything baseline** | |
| recency stub | **last-write-wins** | |
| oracle | **perfect-retrieval ceiling** | |

Elevator sentence: *"MASQ tests whether an agent's memory can tell a settled
change from an unresolved disagreement."*

### 8.2 Headline metric: the MASQ score

**MASQ score = % of scenarios solved**, where a scenario is solved only if
**all four variants** are handled correctly (B-layer pass in each cell).
Single legible percentage (SWE-bench property) AND heuristic-proof by
construction: last-write-wins scores 0% (misses every Collision),
always-flag scores 0% (false-alarms on every Override). The per-cell table
remains the diagnostic breakdown; the mixed-model party×time interaction
remains the significance test behind the table. Expect low absolute scores
under the conjunction; that is acceptable (SWE-bench launched sub-5%) and
the ~50-scenario sample + breakdown carry the resolution.

### 8.3 New invariant I8 — off-kernel collisions (false-alarm arm gets teeth)

Gap found by AJ 2026-06-10: with zero collisions outside the C3 kernel, a
binding-free "flag if ANY conflict exists anywhere" heuristic passes every
cell (flags in C3, silent in C1/C2/C4 where no conflict exists). Fix, by
symmetry with I1 (*every wrong answer is a real value for some other
sibling*): **every conflict signal must be bound to a fact** —

- **I8:** the shared world contains **1–2 marked sibling collisions**
  (explicit greenfield second write, never reconciled, never the kernel
  fact). World is shared across cells, so these sit in C1/C2/C4 corpora
  too: the lazy flagger false-alarms; only fact-bound conflict detection
  passes. "Collisions caught" now means *caught and correctly attributed*.
- Collided siblings are **excluded from value-chatter** (chatter asserting
  one current value would silently resolve the conflict).
- No new legibility surface: sibling collisions reuse the gate-1/probe-
  validated greenfield marker class on unscored facts. Bare-set ban
  untouched (it bans unmarked two-writer facts, not collisions).

### 8.4 Longer chains: deferred to v2, committed for the final benchmark

Kernel stays exactly two writes in v1 — the 2×2 matched-pair purity is the
statistical engine. **History depth** (set→override→override,
collision→later-reconciliation, …) is a committed v2 axis of the final
benchmark, built only after the 2×2 has produced trustworthy results
(decision: AJ 2026-06-10 — defer construction, not inclusion). The
locked-sentence protocol, marker classes, and I8 transfer to the depth
axis unchanged.

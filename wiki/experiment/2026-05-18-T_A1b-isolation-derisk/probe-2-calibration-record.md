---
type: experiment
name: Probe 2 calibration record — state-machine schemas, ratification record, leak-check sweep
status: ACTIVE
last_ingested: 2026-05-22
sources: [../../source/bardes-2024-vjepa.md, ../../source/ge-2024-icae.md]
epistemic_tags: [asserted, speculated]
tags: [t_a1b, probe-2, calibration, test-set-design, caddy]
---

Calibration-stage record for Probe 2 of the [parent experiment spec](./experiment-spec.md), operationalising Phase 1 of the [test-set design](./probe-2-test-set-design.md#generation-pipeline). This page is the durable record of the state-machine schemas, the operationalisation principles, and the ratification record from the AJ-Nils calibration session conducted 2026-05-21 → 2026-05-22.

**What this page contains:**

1. **Formal state-machine schemas** for all 5 patterns — load-bearing, ratified. Define the structural target the encoder must learn to recognise.
2. **Operationalisation principles** — three meta-rules that govern how the schemas are applied during seed and candidate generation (ratified 2026-05-22).
3. **Pointers to the test-set candidate content** (sibling `./source/` files authored by Maren) plus the metadata convention and sweep-finding methodology lessons.
4. **Ratification record** — the questions raised during the AJ-Nils calibration session and how each was resolved.

**What this page does *not* contain** (intentionally moved out for tidiness):

- The 15 event-mode seeds and 4 arc-mode sequences → `./source/event-seeds-maren.md` and `./source/arc-sequences-maren.md`. Nils-drafted originals are preserved in git history.

**Mode naming.** Earlier drafts called the two probe modes "M-mode" (micro / single-event) and "S-mode" (sequence / multi-event). Renamed 2026-05-21 to **event-mode** and **arc-mode** for legibility. Same designs, same gate, same pre-registered thresholds.

## Pattern choice rationale for the 15 seeds

`[ASSERTED]` Three patterns chosen for event-mode calibration to span the structural range:

- **defection** — role-violation pattern (commitment + breach + discovery). Hardest of the five to instantiate without surface vocabulary because trust/breach lexicon is salient.
- **discovery** — belief-shift pattern (prior + evidence + revision). Tests whether we can operationalise an *internal-cognitive-state* transition in a single event.
- **reversal** — outcome-inversion pattern (expectation + opposite). Tests the schema's tolerance to events that are *about* an inverted outcome but where the expectation was set by prior context.

Confrontation and rescue are excluded from the 15-seed calibration block — they are simpler structurally (overt action sequences) and benefit less from joint-calibration time. If the three calibrated cleanly, the remaining two carry less methodological risk.

## Domain choice rationale for the 15 seeds

`[ASSERTED]` Corporate chosen as the single domain because:

- Surface vocabulary is the most-constrained of the four (technical/professional register limits the lexical space for smuggling pattern cues).
- The hardest test of "structure without surface" is a domain where surface alone is least likely to leak the pattern.
- Cross-domain transfer is the *probe*; intra-domain calibration is the *seed* — we want the seeds to be the hardest instantiation, then test transfer to easier ones.

## State-machine schemas

`[ASSERTED]` All five patterns formalised below. Each schema specifies: roles, required state sequence, role-filler type constraints, minimum-content requirements for event-mode, examples of borderline-included vs borderline-excluded instantiations.

### Defection

> Trusted party breaks an explicit or implicit commitment; violation is discovered.

**Roles:** trustor (A), trustee (B), commitment (P), violation (V)

**Required states (in this order, all present):**

| # | State | What must be true |
|---|---|---|
| S1 | Trust placed | A has extended a commitment-bearing relationship to B regarding P. Explicit (written/spoken promise) OR implicit (fiduciary, professional, kinship, or role-based duty). |
| S2 | Violation occurs | B performs V, where V contradicts P. Commission (does what P forbade) or omission (fails to do what P required). |
| S3 | Discovery | The violation V is revealed to A, or to a party whose discovery functionally reaches A within the event. |

**Role-filler constraints:**
- A and B are distinct identifiable parties (named persons, named roles, or named organisations; not abstractions like "society").
- P is specifiable in one sentence (a concrete commitment, not a vague norm).
- V is an act attributable to B (commission or omission), not the act of a third party.

**Minimum-content requirements (event-mode):**
- All four role-fillers (A, B, P, V) recoverable from the event text.
- Discovery present in the event, not merely foreshadowed or deferred.

**Borderline-included:** *"The director learned the senior auditor had been certifying their cousin's firm's books for two years, in violation of the firm's family-relationship disclosure rule."*
- A = director (proxying the firm); B = senior auditor; P = family-relationship disclosure rule; V = certifying cousin's books undisclosed. ✓ all four roles, ✓ discovery present.

**Borderline-excluded:** *"The COO learned that the sales lead had been routing his largest enterprise deals through a personal LLC, capturing the override commission himself. The sales lead's contract had never barred external consulting work, and the override structure had never been formalised as a firm asset."*
- Looks like a defection — appearance of self-dealing at the firm's expense — but the schema fails on P. No commitment was ever extended; the contract didn't bar the activity and the override structure wasn't a firm asset. With no P, there is no V. The action is undesirable but not a defection in the schema's sense.

### Discovery

> Agent's worldview shifts via new evidence contradicting a prior assumption.

**Roles:** seeker (A), prior belief (B), new evidence (E), revised belief (B′)

**Required states:**

| # | State | What must be true |
|---|---|---|
| S1 | Prior belief held | A holds belief B. Explicit (stated) or implicit (recoverable from A's prior actions/expectations described in the event). |
| S2 | Contradicting evidence encountered | A encounters E. E must be epistemically connected to B (could plausibly bear on its truth). |
| S3 | Belief revision | A's belief shifts B → B′. B′ accommodates E and is distinguishable from B (not merely a stronger version of the same belief). |

**Role-filler constraints:**
- A is a specific identifiable agent capable of holding beliefs (named person, named role; not "the company" as a singular epistemic subject unless a specific representative carries the belief).
- B and B′ are propositions, not actions or feelings.
- E is observed or encountered, not hypothesised.
- B′ ≠ B in epistemic content (not merely B with higher confidence).

**Minimum-content requirements (event-mode):**
- Both B and B′ recoverable (the event must signal what was believed before and what is now believed).
- The shift happens within the event; "she would later come to believe…" is borderline-excluded.

**Borderline-included:** *"For three years she had assumed the legacy billing system was internally consistent; opening the audit log during the migration, she found a thousand-odd invoices per month silently routed to an account no one currently at the company had created."*
- A = she; B = system is consistent; E = thousand misrouted invoices/month; B′ = system is materially inconsistent. ✓ shift within event.

**Borderline-excluded:** *"For three years she had suspected the sales-funnel metrics were inflated. The Q4 audit confirmed her suspicion with timestamped evidence: twenty-three percent of the qualified-lead count had been duplicate entries."*
- Looks like discovery — prior position, new evidence, audit-driven outcome — but the schema fails on B ≠ B′. The audit confirms an existing belief rather than revising it; B and B′ are not distinguishable in epistemic content, only in confidence. Confirmation of a prior belief is not a worldview shift.

### Reversal

> Expected outcome inverts to its opposite (success→failure, or failure→success).

**Roles:** agent (A), goal (G), expected outcome (X), actual outcome (¬X)

**Required states:**

| # | State | What must be true |
|---|---|---|
| S1 | Expectation set | A is pursuing goal G; outcome X is expected. The expectation must be established by context, prior action, or explicit statement in the event — not retroactively asserted. |
| S2 | Inversion | Outcome resolves as ¬X. X and ¬X are opposites on a binary or near-binary axis (succeed/fail, win/lose, alive/dead, promoted/fired, approved/blocked), not merely different. |
| S3 | Inversion acknowledged | The inversion is revealed or registered within the event (the actors know, the narrator states it, or it is structurally evident from the resolution). |

**Role-filler constraints:**
- X and ¬X must be polar opposites on a shared axis, not a substitution ("expected the merger, got the IPO instead" is NOT reversal — both are positive outcomes).
- Expectation must be established before resolution within the event; "in retrospect, no one had expected it" is borderline-excluded.

**Minimum-content requirements (event-mode):**
- Expectation visible before the resolution.
- Polar opposite resolution visible.

**Borderline-included:** *"The pitch had been written off internally — three of five reviewers had marked it 'no.' The committee chair returned from the lunch meeting with the lead investor and announced the term sheet had been signed before dessert."*
- G = win the funding; X = no investment; ¬X = signed term sheet. ✓ expectation set, ✓ polar opposite, ✓ within event.

**Borderline-excluded:** *"The board had spent six months preparing for the merger announcement when the lead acquirer pulled out on Wednesday morning. By Wednesday afternoon, the CEO had announced instead a $400M Series E led by their longtime growth investor."*
- Looks like reversal — expectation set, outcome shifted, within-event resolution — but the schema fails on polarity. Both outcomes are positive on different axes (a successful merger and a successful Series E); they are different but not polar opposites on a shared axis. Substitution, not inversion.

### Confrontation

> Direct demand-and-resistance between two parties over a contested object.

**Roles:** demander (A), resister (B), contested object (O)

**Required states:**

| # | State | What must be true |
|---|---|---|
| S1 | Demand made | A makes an explicit demand on B concerning O. Verbal, written, or unambiguous behavioural act of demanding. |
| S2 | Resistance | B actively resists — refusal, counter-demand, withholding, or counter-threat. Passive absence is insufficient. |
| S3 | Resolution | The confrontation reaches a defined endpoint within the event, taking one of three shapes: **(a)** one party prevails — capitulation, agreement to the demand, or the demand formally denied; **(b)** both withdraw or defer — the matter is tabled or escalated to authority (arbitration, board, court) with the deferral mechanism explicit; **(c)** defined breaking point — relations sever, threat issued, ultimatum delivered, party exits. |

**Role-filler constraints:**
- Demand is explicit, not implied. "He sighed and looked at the budget" is not a demand.
- Resistance is active (B does something to refuse), not absence.
- O can be physical (a document, a resource), conceptual (an admission, a decision), or behavioural (a change of action).
- A and B are distinct identifiable parties.

**Minimum-content requirements (event-mode):**
- Demand, resistance, AND resolution (one of shapes a/b/c above) all visible in the event. "They argued and the scene ended" is borderline-excluded — those are ambient-conflict instances, not pattern instantiations.

**Borderline-included:** *"The CFO asked, for the third time, that the regional VP hand over the unredacted forecast. The VP repeated that the document was protected under the ongoing arbitration order, refused to release it, and tabled the matter to the arbitration panel's Friday ruling; the meeting adjourned with the forecast unchanged."*
- A = CFO; B = VP; O = unredacted forecast. ✓ demand explicit, ✓ resistance active, ✓ resolution shape (b) — deferred to arbitration authority, deferral mechanism explicit.

**Borderline-excluded:** *"The product manager asked the engineering lead to commit to a shipping date for the API changes. The engineering lead said the team would assess the scope and circulate an estimate by end of week. The product manager nodded and moved to the next agenda item."*
- Looks like confrontation — explicit ask, deferred response, scene-level resolution — but the schema fails on S2 and S3. The engineering lead's reply is a defer-with-promise, not active resistance (no refusal, counter-demand, or withholding). Even if read generously as resistance, S3 fails: the "end of week estimate" is not a defined deferral mechanism (no authority named, no constraint on the deferral); the matter is tabled, not resolved by any of shapes (a), (b), or (c).

### Rescue

> Intervention by one party to save another from harm.

**Roles:** rescuer (A), endangered party (B), threat (T)

**Required states:**

| # | State | What must be true |
|---|---|---|
| S1 | Danger present | B is in danger from T. T must be present or imminent in the event, not abstract or chronic. |
| S2 | Intervention | A acts specifically to neutralise T or remove B from T's reach. Action must be attributable to A and aimed at the rescue. |
| S3 | Outcome | B is saved, or T is immediately neutralised, within the event. Partial / failed rescues are borderline-excluded (a separate pattern, "failed rescue," is not in our set). |

**Role-filler constraints:**
- A ≠ B. Self-rescue is excluded for this pattern to keep the 2-party structure clean.
- T is specifiable (a named threat, a named adversary, a named hazard), not "general adversity" or "circumstances."

**Minimum-content requirements (event-mode):**
- All three states (danger, intervention, outcome) recoverable from the event.

**Borderline-included:** *"The junior trader noticed the auto-hedge loop was spiralling and the desk's overnight book would breach its limit in under a minute; she killed the strategy from the back-office terminal before the senior desk had registered the alert."*
- A = junior trader; B = desk / firm; T = runaway auto-hedge loop; ✓ all three states.

**Borderline-excluded:** *"The senior engineer noticed the new hire was struggling with the migration tooling and stayed late three nights running to walk him through the steps. By the end of the week, the new hire had shipped his first migration without incident."*
- Looks like rescue — an experienced party intervening to protect a less-experienced one from a bad outcome — but the schema fails on T specificity and intervention shape. "Struggling with the tooling" is not a present-or-imminent specific threat (no breach, no production incident, no deadline cliff), and the intervention is gradual mentorship across three nights rather than action aimed at neutralising a danger. Mentorship-as-support is not rescue-as-intervention.

## Test-set candidate content

`[ASSERTED]` The 25 event-mode seeds and 4 arc-mode sequences are authored by Maren (purple) per the schemas and operationalisation principles above. They live as raw artifacts in `./source/`:

- **[Event-mode seeds — defection/discovery/reversal (15)](./source/event-seeds-maren.md)** — 5 defection / 5 discovery / 5 reversal seeds × corporate domain. Voice diversified across present-tense / dialogue-driven / first-person / free-indirect / embedded-document (3 per register, 1 of each per pattern). Discovery-mechanism diversified across direct observation, verbal third-party report, data analysis, inference from absence, audio playback, system failure, public announcement, phone call, and document / log review (9 non-document-mediated, 6 document/log-mediated). Commitment-type diversified across written contract / verbal undertaking / role-based institutional duty.
- **[Event-mode seeds — confrontation/rescue (10)](./source/event-seeds-confrontation-rescue-maren.md)** — 5 confrontation / 5 rescue seeds × corporate domain. Drafted to complete the five-pattern calibration coverage for Phase 2 generation. Voice diversified (same five registers, one per pattern per seed). Confrontation: resolution shapes varied across (a) prevails / (b) deferred / (c) breaking point; contested objects span operational, ownership, contractual, personnel, and legal/reputational. Rescue: five distinct threat types (financial/systemic, product safety, regulatory, legal/information, compliance/criminal); five distinct intervention modalities (technical, verbal, physical, physical removal, system action). Nils QA'd 2026-05-22.
- **[Arc-mode sequences (4)](./source/arc-sequences-maren.md)** — defection × four domains (corporate / fantasy / ecclesiastical-historical / sci-fi). Beat structure varied across 4 / 5 / 5 / 6 events per sequence; voice diversified (dialogue-driven / free indirect / embedded document / present tense); S3 (historical) is set in a 1390s Augustinian priory — domain-native, not corporate-in-period-costume.

**Initial drafts by Nils (Indigo)** are preserved in git history. They were superseded after two diagnosed problems in the originals (per AJ critique 2026-05-22):

- *Voice and beat-shape uniformity.* All Nils-drafted seeds shared the same third-person observational past-tense register and the same intra-pattern micro-structure ([past-perfect commitment] + [document-mediated discovery] + [evidence]). All four Nils-drafted arcs followed the same 5-beat shape (commitment → trust-displayed → first-signal → discovery → confrontation). Both uniformities risked structural overfitting — encoder/predictor could learn the shape/register rather than the underlying pattern. Worse at Phase 2 LM-generation scale: the seeds become worked examples for ~600 cross-domain candidates, multiplying the uniformity ~40× downstream.
- *Domain-as-costume.* The Nils-drafted historical arc (1782 mercantile partnership) was a corporate-defection arc with archaic vocabulary — structural roles mapped one-to-one onto the corporate arc.

### Metadata convention

`[ASSERTED]` Each seed in `event-seeds-maren.md` carries a line of role + state breakdown immediately below the prose. The metadata serves three purposes during the calibration stage: (a) forcing the author to verify the seed actually instantiates the schema; (b) making rater disagreement diagnosable during the joint AJ-Nils calibration session (if we differ on accept/revise/reject, we can compare role assignments to localise the disagreement); (c) giving Phase 2 LM generation prompts a worked structural breakdown alongside the prose. **The metadata is stripped from the seed text before Phase 3 rater filtering** so the three independent raters apply the schema themselves; the inter-rater Fleiss' κ measurement requires that they not see the author's stated structure. See [design doc § Generation pipeline](./probe-2-test-set-design.md#generation-pipeline) Phase 3 for the metadata-stripping spec.

### Seed-draft sweep findings (methodology lessons for future seed generation)

`[ASSERTED]` During leak-check sweeps of seed drafts (Nils originals, 2026-05-22), four kinds of issues recurred. Phase 2 LM-generation prompts and any future hand-drafted seeds should pre-screen for these:

- **Missing or weak P** — defection seeds where the commitment is implicit (e.g. "jointly defended publicly") or never explicitly extended. Mitigation: each defection seed must name P as an explicit written instrument, verbal undertaking, or institutional role-based duty (one of the three commitment types).
- **Ambiguous A in discovery seeds** — prior belief held by one party, revised belief held by another, with no clear discovery-transfer between them. Mitigation: discovery seeds must have a single named agent A who carries both B and B′.
- **Weak A specificity** — discovery seeds using "internally" or "the team" without naming a specific identifiable agent. The discovery schema's role-filler rule requires a named individual or named role; collective abstractions fail. Mitigation: name the SRE lead, the director, the analyst, etc.
- **Polarity violations in reversal seeds** — outcomes that are *different* rather than *polar opposite* on a shared axis (e.g. "expected the merger, got the IPO instead" — both positive, no inversion). Mitigation: every reversal seed must have X and ¬X on a binary or near-binary opposite-pair (close/decline, ship/not-ship, win/lose, layoffs/no-layoffs).

### Arc-mode event-granularity discipline

`[ASSERTED]` During the arc-sequence drafting sweep (Nils originals, 2026-05-22), an initial set of drafts contained narrative summaries spanning multiple scenes ("Over the following eighteen months, she built the team and shipped the milestone"). These do not satisfy the event-granularity rule in the [design doc § Event granularity](./probe-2-test-set-design.md#event-granularity): an event is one segmentation-coherent bounded scene, not a compressed reference to many. The Maren-authored rewrites in `./source/arc-sequences-maren.md` enforce strict scene discipline throughout — each numbered event is one scene with a single setting, time-window, and action sequence. Phase 2 LM-generation prompts must enforce the same discipline; rater protocol (Phase 3) should fail any candidate that summary-collapses multiple scenes into one event.

## Operationalisation principles

`[ASSERTED]` Ratified 2026-05-22. Three meta-rules govern how the schemas are applied during seed and candidate generation. They will apply to Phase 2 LM-generation prompts and Phase 3 rater filtering, not just to calibration-stage seeds.

1. **Single-event minimum-content is strict.** A seed that requires the reader to infer a role-filler from prior knowledge (e.g. "betrayal" implied by tone but no commitment named) is borderline-excluded. The schema's "all roles recoverable from event text" rule means the event must be *self-contained* for the pattern.

2. **Pattern-naming vocabulary is forbidden in seed text.** Even the schemas use the pattern names; the seeds must not. The adversarial constraint is what forces structural rather than lexical instantiation, and it must apply at seed-draft time, not only at Phase 2 LM generation.

3. **Polarity is a hard constraint for reversal; transitivity is not.** Reversal requires a polar-opposite outcome on a shared axis. Substitution ("expected A, got B" where A and B are both positive) does not satisfy the schema. This is sharper than the loose "outcome inverts" framing in the design doc; the schema tightens it.

## Ratification record (AJ–Nils calibration session, 2026-05-21 → 2026-05-22)

`[ASSERTED]` All seven questions raised during the joint calibration session are resolved. Record retained for the methodology trail.

1. **Pattern-set ratification — RATIFIED with one schema correction.** All five schemas operationalise the patterns at the target rigour level. Correction: confrontation S3 tightened from "tension visible" (no required terminal state) to "resolution" with three explicit shapes — (a) one party prevails, (b) both withdraw or defer to authority, (c) defined breaking point. The original S3 broke the symmetry with the other four schemas, all of which have definite-endpoint S3s; the correction restores that symmetry and addresses rater-agreement risk on otherwise vague "tension persists" language.

2. **Domain choice (corporate) — RATIFIED.** Initial Nils framing of corporate as the "most-contamination-risky" domain (and therefore most fraught for the perplexity sanity check) was incorrect. Memorisation risk depends on the specific text being in pretraining data, not on the register being well-modelled. Hand-crafted novel corporate-domain seeds carry effectively zero memorisation risk; the corporate register's lower intrinsic perplexity is a Phase 3 check-design concern (the perplexity-check baseline should be matched-register, not random web text), not a domain-choice concern.

3. **Three-pattern subset (defection / discovery / reversal) — RATIFIED.** Spans the three structural shapes: role-violation, belief-shift, outcome-inversion. Confrontation and rescue excluded from the calibration block as structurally simpler.

4. **Borderline examples — RATIFIED after rewrite of all five borderline-excluded examples.** Original Nils-drafted excluded examples ("He looked at the chart and was surprised") were straw cases that no rater would be tempted to include; they didn't function as calibration anchors. Replaced with near-miss examples matched in length and register to the included examples, each failing on a specific identifiable schema element (defection: P never existed; discovery: B ≈ B′ confirmation not revision; reversal: substitution not polar inversion; confrontation: defer-with-promise not active resistance, no defined deferral mechanism; rescue: general struggle not specific threat, gradual mentorship not aimed-neutralisation).

5. **Arc-mode feasibility gate pattern (defection) — RATIFIED.** Defection has the cleanest multi-event arc structure of the five (commitment → tenure → first signal → discovery → confrontation) and is the hardest to instantiate at single-event scope, making arc-mode the natural fit. If arc-mode works for defection, it likely works for the simpler-arc patterns; if it fails for defection, it likely fails for all five.

6. **Operationalisation principles — RATIFIED.** See [§ Operationalisation principles](#operationalisation-principles) above.

7. **Leak check on seeds and sequences — INFORMS THE SOURCE FILES.** Sweep findings drove four substantive seed fixes (D2 weak P, Di2 ambiguous A, Di5 weak A specificity, R5 polarity violation) and the full rewrite of all 15 seeds + 4 arcs by Maren under the variation plans (voice / micro-structural / discovery-mechanism diversification for seeds; beat-shape + voice + domain-native diversification for arcs). The methodology lessons that surfaced are recorded as [§ Seed-draft sweep findings](#seed-draft-sweep-findings-methodology-lessons-for-future-seed-generation) above for reuse in Phase 2 generation prompts and future seed work.

## Sequencing

Calibration-stage outputs are locked under the goalpost-shift discipline ([[feedback_falsifiability_offers]]). The schemas, operationalisation principles, and metadata convention are mutable only with explicit goalpost-shift acknowledgement and documentation.

**Closed from this stage:**

- **Arc-mode feasibility gate — PASSED (2026-05-22).** Both raters (AJ + Nils) independently rated all four Maren-authored arc-mode sequences (`./source/arc-sequences-maren.md`) at 5/5. Result: 4/4 sequences at mean 5.0, well above the ≥3-of-4 mean-≥4 threshold. Arc-mode generation proceeds alongside event-mode. The gate was non-trivially calibrated — Maren's first iteration did not pass AJ's bar; the sequences required a full rewrite addressing five diagnosed problems (commerce-story mono-culture, corporate-in-period-costume, uniform beat shape, uniform voice, reveal-not-confrontation) before passing.
- **Confrontation/rescue calibration seeds landed (2026-05-22).** 10 additional seeds (5 confrontation, 5 rescue) authored by Maren, Nils QA'd, completing five-pattern coverage for Phase 2 generation prompts.

**Phase 2 (LM candidate generation across all 20 cells) begins** per the [design doc § Generation pipeline](./probe-2-test-set-design.md#generation-pipeline). Prompt templates and execution plan at [phase-2-generation-prompts](./phase-2-generation-prompts.md).

## Related

- [probe-2-test-set-design](./probe-2-test-set-design.md) — parent design doc; this page operationalises its Phase 1.
- [experiment-spec](./experiment-spec.md) — grandparent experiment spec; Probe 2 lives there.
- [H44-T_A1b-cross-domain-transfer](../../hypothesis/H44-T_A1b-cross-domain-transfer.md) — hypothesis under test.
- [memory-retrieval-tiers](../../concept/memory-retrieval-tiers.md) — defines tier 3, the capability tested.

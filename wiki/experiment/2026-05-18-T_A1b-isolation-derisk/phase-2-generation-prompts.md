---
type: experiment
name: Phase 2 generation prompts — event-mode and arc-mode candidate generation
status: PROPOSED
last_ingested: 2026-05-22
tags: [t_a1b, probe-2, phase-2, generation, caddy]
---

Prompt templates and execution plan for Phase 2 of the [test-set design](./probe-2-test-set-design.md#generation-pipeline). Generates ~600 event-mode + ~240 arc-mode candidates across the 5×4 pattern-domain grid. Designed for execution via Claude Code agents (three model tiers) in a fresh context window.

Schemas are locked under goalpost-shift discipline per the [calibration record](./probe-2-calibration-record.md#sequencing). The prompts below embed the locked schemas verbatim.

## Source files the executor must read

- [source/event-seeds-maren.md](./source/event-seeds-maren.md) — 15 event-mode worked examples (defection/discovery/reversal × corporate)
- [source/event-seeds-confrontation-rescue-maren.md](./source/event-seeds-confrontation-rescue-maren.md) — 10 event-mode worked examples (confrontation/rescue × corporate)
- [source/arc-sequences-maren.md](./source/arc-sequences-maren.md) — 4 arc-mode worked examples (defection × 4 domains)

The executor reads these and pastes them into the prompt at the marked insertion points. The seeds include per-seed role+state metadata; include it (it helps the generator understand the structural target; metadata is stripped later at Phase 3 rater filtering, not here).

---

## Event-mode prompt template

One prompt per batch. One batch = 5 candidates for one pattern × one domain. Six batches per cell (30 candidates per cell). Variable substitution points marked `«VARIABLE»`.

For **subsequent batches in the same cell**, append a deduplication block after the worked examples:

> **Already generated for this cell (do not repeat these scenario shapes):**
> [paste one-line summaries of prior batch outputs]

---

**[BEGIN EVENT-MODE PROMPT]**

You are generating test-set candidates for a structural-pattern recognition experiment. Each candidate is a **single event** — one bounded scene with a single setting, single time-window, and single action sequence — that instantiates the structural pattern below.

The goal: events where the structural pattern is recoverable from what happens in the narrative, not from keywords or pattern-naming vocabulary.

## Pattern: «PATTERN_NAME»

«SCHEMA — paste from § Pattern schemas below»

## Domain: «DOMAIN_NAME»

«DOMAIN_DESCRIPTION — paste from § Domain descriptions below»

## Constraints

1. **Self-contained.** All role-fillers («ROLE_LIST») must be recoverable from the event text alone. No external context required.
2. **Forbidden vocabulary.** The following words and close derivatives are BANNED from the generated text: «FORBIDDEN_WORDS — paste from § Forbidden vocabulary below». Rewrite any sentence that reaches for a banned word using narrative action instead.
3. **Event granularity.** One scene only. No narrative summaries spanning multiple scenes ("over the following months…"), no repeated-occurrence summaries ("she began receiving complaints and dismissed them all"), no time-skip transitions ("years later…").
4. **Voice variety.** Distribute across these five registers: present tense, dialogue-driven, first-person narration, free indirect, embedded document. Do not default to third-person past-tense observational.
5. **Structural variety.** Vary scenario shape, information pathway, role configuration, and institutional context across candidates. Do not repeat the same micro-structure.
6. **Domain-native.** The scenario must be native to the «DOMAIN_NAME» domain — its institutional structures, power dynamics, and information pathways must be authentic to the domain. Do not write a corporate scenario with «DOMAIN_NAME» vocabulary pasted on top.

«PATTERN_SPECIFIC_CONSTRAINTS — paste from § Pattern-specific constraints below»

## Worked examples («EXAMPLE_DOMAIN» domain)

These calibration seeds show the target quality and structural variety. Study the voice variety, discovery-mechanism variety, and structural variety — then create *new* scenarios native to «DOMAIN_NAME». Do not adapt or translate these examples into the target domain.

«SEEDS_WITH_METADATA — paste the 5 relevant seeds from event-seeds-maren.md»

## Output

Generate exactly 5 candidates. For each:

1. **Label:** «PATTERN_CODE»-«DOMAIN_INITIAL»«BATCH»-«SEQ» (e.g. D-F1-3 = defection, fantasy, batch 1, candidate 3)
2. **Event text:** One paragraph to half a page of prose. No preamble, no meta-commentary, no explanation of choices.
3. **Role + state breakdown:** immediately after the text, one line: `> A = …; B = …; …; ✓ all roles, ✓ all states`

**[END EVENT-MODE PROMPT]**

---

## Arc-mode prompt template

One prompt per batch. One batch = 4 candidate sequences for one pattern × one domain. Three batches per cell (~12 candidates per cell). Twenty cells = 60 batches, ~240 candidates total.

---

**[BEGIN ARC-MODE PROMPT]**

You are generating test-set candidates for a structural-pattern recognition experiment. Each candidate is a **sequence of events** (each event = one bounded scene) that together instantiate the structural pattern below at arc level. No single event contains the full pattern; the pattern is distributed across the sequence.

## Pattern: «PATTERN_NAME»

«SCHEMA — paste from § Pattern schemas below»

## Arc structure

Distribute the pattern's required states across the events. Each event is one bounded scene — single setting, single time-window, single action sequence. Scenes are separated by time and/or setting changes.

«ARC_BEAT_SPEC — paste from § Arc-mode beat specifications below»

## Domain: «DOMAIN_NAME»

«DOMAIN_DESCRIPTION — paste from § Domain descriptions below»

## Constraints

1. **Event granularity.** Each numbered event is one bounded scene. No compressions, no "over the following months," no multi-scene summaries.
2. **Forbidden vocabulary.** «FORBIDDEN_WORDS»
3. **Domain-native.** Scenarios must be native to «DOMAIN_NAME». Not another domain in costume.
4. **Voice variety.** Vary across candidates: dialogue-driven, free indirect, embedded document, present tense. Not all the same register.
5. **Beat-shape variety.** Vary event count (4–6), distribution of pattern states across events, and whether the depicted order is chronological or non-linear. Do not produce identical beat-by-beat structures across candidates.
6. **Structural variety.** Vary scenario types, institutional contexts, role configurations, and mechanisms. Do not repeat the same story shape.
7. **Confrontation discipline.** Any event labelled as a confrontation must include: an explicit demand, active resistance (not silence or passive absence), and a defined resolution — one of: (a) one party prevails, (b) deferred to named authority, (c) defined breaking point. A reveal scene where evidence is presented and the other party says nothing is NOT a confrontation.

## Worked examples

These are calibration arc-mode sequences for the **defection** pattern across four domains. Study the structural variety — beat count (4/5/5/6), voice (dialogue / free-indirect / embedded-document / present-tense), violation type, confrontation resolution shape, and domain-nativeness.

«ARC_SEQUENCES — paste all four sequences from arc-sequences-maren.md, including scenario summaries and role assignments»

## Output

Generate exactly 4 candidate sequences. For each:

1. **Label:** «PATTERN_CODE»-arc-«DOMAIN_INITIAL»«BATCH»-«SEQ»
2. **Scenario:** 2–3 sentence summary.
3. **Role assignments:** `> A = …; B = …; P/G/O/T = …; V/X/¬X = …`
4. **Events:** Numbered E1, E2, … with beat label in parentheses (e.g. "E1 (commitment scene)"). Each event is 1–3 paragraphs of prose.
5. **Beat count** and depicted order noted at the top (e.g. "5 beats, chronological" or "5 beats, non-linear: E3 → E1 → E2 → E4 → E5").

**[END ARC-MODE PROMPT]**

---

## Pattern schemas

Verbatim from the locked [calibration record](./probe-2-calibration-record.md#state-machine-schemas). Paste the relevant schema block into the prompt at `«SCHEMA»`.

### Defection

> Trusted party breaks an explicit or implicit commitment; violation is discovered.

**Roles:** trustor (A), trustee (B), commitment (P), violation (V)

**Required states (in order, all present):**

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

### Discovery

> Agent's worldview shifts via new evidence contradicting a prior assumption.

**Roles:** seeker (A), prior belief (B), new evidence (E), revised belief (B′)

**Required states:**

| # | State | What must be true |
|---|---|---|
| S1 | Prior belief held | A holds belief B. Explicit (stated) or implicit (recoverable from A's prior actions/expectations). |
| S2 | Contradicting evidence encountered | A encounters E. E must be epistemically connected to B. |
| S3 | Belief revision | A's belief shifts B → B′. B′ accommodates E and is distinguishable from B (not merely stronger confidence). |

**Role-filler constraints:**
- A is a specific identifiable agent (named person or named role).
- B and B′ are propositions, not actions or feelings.
- E is observed or encountered, not hypothesised.
- B′ ≠ B in epistemic content (not merely B with higher confidence).

**Minimum-content requirements (event-mode):**
- Both B and B′ recoverable from the text.
- The shift happens within the event.

### Reversal

> Expected outcome inverts to its opposite (success→failure, or failure→success).

**Roles:** agent (A), goal (G), expected outcome (X), actual outcome (¬X)

**Required states:**

| # | State | What must be true |
|---|---|---|
| S1 | Expectation set | A is pursuing G; outcome X is expected. Expectation established by context, prior action, or explicit statement — not retroactively asserted. |
| S2 | Inversion | Outcome resolves as ¬X. X and ¬X are polar opposites on a binary or near-binary axis. |
| S3 | Inversion acknowledged | Revealed or registered within the event. |

**Role-filler constraints:**
- X and ¬X are polar opposites on a shared axis (succeed/fail, win/lose, approved/blocked). Not a substitution.
- Expectation established before resolution within the event.

**Minimum-content requirements (event-mode):**
- Expectation visible before resolution.
- Polar opposite resolution visible.

### Confrontation

> Direct demand-and-resistance between two parties over a contested object.

**Roles:** demander (A), resister (B), contested object (O)

**Required states:**

| # | State | What must be true |
|---|---|---|
| S1 | Demand made | A makes an explicit demand on B concerning O. |
| S2 | Resistance | B actively resists — refusal, counter-demand, withholding, or counter-threat. Passive absence is insufficient. |
| S3 | Resolution | Defined endpoint: (a) one party prevails, (b) both defer to named authority, or (c) defined breaking point. |

**Role-filler constraints:**
- Demand is explicit, not implied.
- Resistance is active.
- A and B are distinct identifiable parties.

**Minimum-content requirements (event-mode):**
- Demand, resistance, AND resolution all visible.

### Rescue

> Intervention by one party to save another from harm.

**Roles:** rescuer (A), endangered party (B), threat (T)

**Required states:**

| # | State | What must be true |
|---|---|---|
| S1 | Danger present | B is in danger from T. T must be present or imminent, not abstract or chronic. |
| S2 | Intervention | A acts specifically to neutralise T or remove B from T's reach. |
| S3 | Outcome | B is saved or T is neutralised within the event. |

**Role-filler constraints:**
- A ≠ B (no self-rescue).
- T is specifiable (named threat, adversary, or hazard).

**Minimum-content requirements (event-mode):**
- All three states recoverable from the event.

---

## Forbidden vocabulary

Paste the relevant list into the prompt at `«FORBIDDEN_WORDS»`.

### Defection
betray, betrayal, betrayed, treachery, treacherous, defect, defection, disloyal, disloyalty, unfaithful, double-cross, two-faced, backstab, backstabbing, stab in the back, sell out, sold out, turncoat, break faith, broke faith, breach of trust, trusted (when used to name the relationship rather than describe an action)

### Discovery
discover, discovery, discovered, realize, realise, realization, realisation, revelation, reveal, revealed, revealing, epiphany, eureka, eye-opener, eye-opening, wake-up call, light-bulb, lightbulb, aha, uncover, uncovered, dawn on, dawned on, come to see, came to see, opened eyes, the truth

### Reversal
reverse, reversal, reversed, twist, plot twist, turnaround, turn around, turned around, ironic, irony, ironically, unexpected, unexpectedly, against all odds, miracle, miraculous, surprise, surprised, surprising, upend, upended, out of nowhere, shock, shocking, shocked, who could have predicted, no one saw coming

### Confrontation
confront, confrontation, confronted, showdown, face-off, face off, stand-off, standoff, clash, clashed, battle of wills, square off, squared off, locked horns

### Rescue
rescue, rescued, rescuer, save, saved, saving, saviour, savior, hero, heroic, heroism, heroine, in the nick of time, just in time, swooped in, came to the rescue, rode to the rescue, white knight, guardian angel

---

## Pattern-specific constraints

Paste the relevant block into the prompt at `«PATTERN_SPECIFIC_CONSTRAINTS»`.

### Defection
```
7. **Commitment-type variety.** Vary across written contract, verbal personal undertaking, and role-based institutional duty. Do not default to "signed a contract."
8. **Violation-type variety.** Do not default to financial fraud or asset diversion. Vary: strategic disloyalty, coerced betrayal, principled breach, negligent omission, paternalistic override, jurisdictional overreach, etc.
```

### Discovery
```
7. **Single epistemic agent.** A must be one named person or named role who carries both B and B′. Do not split the belief-holder across characters.
8. **Discovery-mechanism variety.** Vary how A encounters E: direct observation, verbal report, data analysis, inference from absence, system failure, public announcement, intercepted communication, physical evidence, accidental exposure, etc. Do not default to "reading a document."
9. **Genuine revision.** B′ must be epistemically distinct from B — not merely B with higher confidence. "She suspected X; the audit confirmed X" is NOT discovery. "She believed X; the evidence showed Y" IS discovery.
```

### Reversal
```
7. **Polar opposition.** X and ¬X must be polar opposites on a binary or near-binary axis (approved/declined, success/failure, alive/dead, hired/fired). "Expected A, got B" where both are positive outcomes on different axes is SUBSTITUTION, not reversal. Name the axis explicitly in your role breakdown.
8. **Expectation before resolution.** The expectation (X) must be visible in the text before ¬X is revealed. Do not assert the expectation retroactively.
```

### Confrontation
```
7. **Explicit demand.** A must make a demand identifiable as such — verbal, written, or unambiguously behavioural. Sighing or glancing is not a demand.
8. **Active resistance.** B must do something: refuse, counter-demand, withhold, counter-threaten. Passive silence or non-response is not resistance.
9. **Resolution variety.** Each candidate must reach a defined resolution using one of: (a) one party prevails (capitulation or formal denial), (b) both defer to named authority (with explicit mechanism), (c) defined breaking point (severance, ultimatum, exit). Vary the shape across candidates.
```

### Rescue
```
7. **Specific threat.** T must be named and present or imminent — a specific hazard, adversary, or failure mode. Not "general adversity" or "difficult circumstances."
8. **Aimed intervention.** A's action must be specifically targeted at neutralising T or extracting B. General support or mentorship is not rescue.
9. **Definitive outcome.** B is saved or T is neutralised within the event. Partial and failed rescues are excluded.
```

---

## Worked examples per pattern

Which seeds to paste into the prompt at `«SEEDS_WITH_METADATA»`:

| Pattern | Source file | Seeds |
|---|---|---|
| Defection | `source/event-seeds-maren.md` | D1–D5 |
| Discovery | `source/event-seeds-maren.md` | Di1–Di5 |
| Reversal | `source/event-seeds-maren.md` | R1–R5 |
| Confrontation | `source/event-seeds-confrontation-rescue-maren.md` | Co1–Co5 |
| Rescue | `source/event-seeds-confrontation-rescue-maren.md` | Rc1–Rc5 |

All 25 seeds are corporate domain. Include the role+state metadata line under each seed.

---

## Domain descriptions

Paste the relevant block into the prompt at `«DOMAIN_DESCRIPTION»`.

### Corporate
Modern office, business, or professional setting. Companies, firms, startups, boards, teams. Power structures are organisational (CEO/VP/director/manager). Information flows through meetings, emails, reports, dashboards, systems.

### Fantasy
Medieval, magical, or mythical setting. Courts, guilds, orders, clans, temples. Power structures are feudal, guild-based, or magical-hierarchical. Information flows through messengers, councils, observed actions, magical means. Technology is pre-industrial. Do not use modern corporate vocabulary (email, database, quarterly review) — use the domain's native information pathways and institutional structures.

### Historical
Non-magical past setting, pre-1900. Choose a specific era per candidate and let it be load-bearing — the institutional structures, social roles, and information pathways of the era should shape the event, not merely decorate it. Do not write modern stories with archaic vocabulary. Vary eras across candidates (not all medieval, not all 18th-century).

### Sci-fi
Speculative future or technological setting. Ships, stations, colonies, orbital platforms, terraforming projects, post-scarcity societies. Technology is load-bearing — it shapes what is possible and how information flows. Power structures may be military, corporate-colonial, technocratic, or novel. Do not write modern corporate or military stories with futuristic vocabulary pasted on top.

---

## Arc-mode beat specifications

Paste the relevant block into the prompt at `«ARC_BEAT_SPEC»`.

### Defection
4–6 events. Required states to distribute: commitment placed (S1), violation occurs (S2), discovery (S3). Available additional beats: trust-displayed, first-signal, evidence-gathering, confrontation. Vary: whether trust-displayed is a separate scene or implicit in commitment; whether discovery and confrontation are one scene or two; whether depicted order is chronological or non-linear.

### Discovery
4–6 events. Required states: prior belief established (S1), contradicting evidence encountered (S2), belief revision (S3). Available additional beats: belief reinforced (false confidence deepened), partial/ambiguous evidence, secondary confirming evidence, consequences of revision. The arc should show the belief under pressure from accumulating evidence — not a single-scene flip distributed across scenes for no structural reason.

### Reversal
4–6 events. Required states: expectation established (S1), inversion (S2), inversion acknowledged (S3). Available additional beats: expectation reinforced (rising confidence), first crack (ambiguous counter-signal), aftermath/consequences. The arc should build genuine expectation through action — not just tell the reader "everyone expected X."

### Confrontation
4–6 events. Required states: demand (S1), resistance (S2), resolution (S3). Available additional beats: escalation, failed negotiation, authority involvement, preparation/positioning, aftermath. The arc should distribute the confrontation dynamics across scenes — a demand in one scene might produce initial resistance, which escalates through intermediary scenes, before resolution.

### Rescue
4–6 events. Required states: danger present (S1), intervention (S2), outcome (S3). Available additional beats: danger escalation, failed initial response, preparation for intervention, cost of rescue, aftermath. The arc should make the threat vivid and the intervention earned — not a sudden appearance of a helper.

---

## Execution plan

### Model tiers

| Tier | How to spawn | Expected model |
|---|---|---|
| A | `Agent({model: "opus"})` | Opus 4.7 |
| B | `Agent({})` — inherits from parent | Opus 4.6 |
| C | `Agent({model: "sonnet"})` | Sonnet 4.6 |

### Event-mode batches per cell

6 batches × 5 candidates = 30 per cell. Tier distribution per cell:

| Batch | Tier | Notes |
|---|---|---|
| 1 | A (Opus 4.7) | |
| 2 | B (Opus 4.6) | |
| 3 | C (Sonnet 4.6) | |
| 4 | A (Opus 4.7) | Include dedup block from batches 1–3 |
| 5 | B (Opus 4.6) | Include dedup block from batches 1–3 |
| 6 | C (Sonnet 4.6) | Include dedup block from batches 1–3 |

Total: 20 cells × 30 = **600 event-mode candidates**.

### Arc-mode batches per cell

3 batches × 4 candidates = 12 per cell. One batch per tier.

Total: 20 cells × 12 = **240 arc-mode candidates**.

### Parallelism

- Up to 4 agents in parallel (resource constraint; adjust based on observed throughput)
- Group by pattern: complete all 4 domains for one pattern before moving to the next
- Each agent handles one batch (not one cell) to keep prompt length manageable

### Output paths

```
experiments/probes/phase-2-candidates/
  event-mode/
    defection/
      corporate/batch-1.md
      corporate/batch-2.md
      ...
      fantasy/batch-1.md
      ...
    discovery/
      ...
    reversal/
      ...
    confrontation/
      ...
    rescue/
      ...
  arc-mode/
    defection/
      corporate/batch-1.md
      ...
    ...
  manifest.md          ← running count: pattern, domain, batch, tier, candidate count, flagged issues
```

### Quality gates

**Spot-check after first 3 batches** (one per tier, same cell). Before running full generation, verify:

- [ ] All 5 (or 4) candidates present and numbered per batch
- [ ] Each candidate has role+state metadata line
- [ ] Zero forbidden-vocabulary violations (grep the batch output)
- [ ] Voice register varies across the 5 candidates (not all third-person-past)
- [ ] Structural variety: no two candidates share the same scenario shape
- [ ] Domain-native: scenarios use the domain's institutional structures, not corporate-in-costume
- [ ] Event granularity: each candidate is one bounded scene (no "over the months…" compressions)

**Red flags that warrant pausing generation:**

- A model tier consistently produces forbidden-vocabulary violations → drop that tier, redistribute
- Confrontation or rescue candidates missing demand/resistance/resolution or threat/intervention/outcome → the schema instruction isn't landing; revise the prompt before continuing
- Domain-as-costume pattern emerging (fantasy candidates that read as corporate with swords) → strengthen the domain-native constraint or add negative examples

### Confrontation and rescue: calibration seeds

The original 15 worked examples covered defection, discovery, and reversal only. Confrontation and rescue now have 5 calibration seeds each in [source/event-seeds-confrontation-rescue-maren.md](./source/event-seeds-confrontation-rescue-maren.md) (Maren-authored, Nils QA'd 2026-05-22). Use these as `«SEEDS_WITH_METADATA»` for confrontation and rescue cells — same insertion method as the other three patterns.

**One note for rescue generation:** Rc1 (runaway auto-hedge algorithm) is structurally close to the schema's borderline-included example. When generating rescue candidates, add to the dedup instruction: "Do not generate variations of 'person kills a runaway automated process.' The worked examples already cover that scenario shape."

---

## Numbering convention

**Event-mode:** `{pattern}-{domain}{batch}-{seq}`
- Pattern codes: D (defection), Di (discovery), R (reversal), C (confrontation), Re (rescue)
- Domain codes: Co (corporate), Fa (fantasy), Hi (historical), Sf (sci-fi)
- Example: `D-Fa2-3` = defection, fantasy, batch 2, candidate 3

**Arc-mode:** `{pattern}-arc-{domain}{batch}-{seq}`
- Example: `Di-arc-Hi1-2` = discovery arc, historical, batch 1, candidate 2

---

## Worked-example reference for corporate cells

When generating for the **corporate** domain, the worked examples are from the same domain. Add this instruction after the examples:

> These examples are from the same domain you are generating for. Create new scenarios with different institutional contexts, role configurations, and mechanisms. Do not rewrite or closely adapt any of the example scenarios.

When generating for **non-corporate** domains, the default instruction applies:

> These examples are from the corporate domain. Study the structural variety — then create new scenarios native to «DOMAIN_NAME». Do not adapt or translate these corporate examples into the target domain.

---

## Related

- [probe-2-test-set-design](./probe-2-test-set-design.md) — parent methodology doc
- [probe-2-calibration-record](./probe-2-calibration-record.md) — locked schemas and ratification record
- [source/event-seeds-maren.md](./source/event-seeds-maren.md) — event-mode worked examples (defection/discovery/reversal)
- [source/event-seeds-confrontation-rescue-maren.md](./source/event-seeds-confrontation-rescue-maren.md) — event-mode worked examples (confrontation/rescue)
- [source/arc-sequences-maren.md](./source/arc-sequences-maren.md) — arc-mode worked examples (defection × 4 domains)

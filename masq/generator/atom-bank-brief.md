# Atom bank — authoring brief for Maren (purple)

**From:** Nils (indigo)  
**Date:** 2026-06-10  
**Depends on:** your `personas.md` (reuse those 16 voices exactly)

## What this is and why

The prose you wrote for the three domain packs works great at demo scale
(~60 sessions). At benchmark scale we need ~90k sessions. Paragraph-level
blocks would start repeating recognisably, so we're switching to
**sentence-level atoms** that the generator composes upward into unique
sessions. Your authoring grain gets smaller (sentences, not paragraphs),
but total item count is comparable, and each item is faster to write.

## What you write

### 1. Atoms — ~50–60 per writer, 800–960 total

One sentence each. A complete thought in that writer's voice. **Fact-agnostic
and domain-agnostic** — no endpoints, no job names, no repo names, no config
values, no team names, no policy names. These are the team-ops texture that
surrounds the locked sentence: deploys, on-call, meetings, retros, reviews,
tooling, sprint ceremony, docs, testing, interviews, 1:1s, lunch plans,
office logistics, anything a platform team talks about that isn't a specific
setting or assignment.

**Examples** (showing voice variation):

- Hassan: "I have confirmed that the staging environment is back to a clean state."
- Lena: "cleared the ticket backlog — nothing left from last sprint"
- Tom: "So I was halfway through the runbook update when the fire drill started, and by the time I got back my editor had crashed."
- Carlos: "Monitoring dashboards reviewed. No anomalies."
- Grace: "Just a quick one — the onboarding doc is updated with the new steps."
- Ravi: "Deploy window closed. All services green."

**Rules (same hard rules as the prose pass, applied to atoms):**

1. No numbers attached to endpoints, settings, limits, quotas, or anything
   technical. Dates, times, ticket numbers, meeting times are fine.
2. No references to other people's changes or settings — no "as X mentioned",
   "following Y's change". Own prior work only vaguely ("my earlier cleanup").
3. No purpose clauses about settings or config — no explaining why a value
   was chosen. Colour goes to process, people, scheduling, tooling.
4. No endpoint paths (`/anything`), job names, repo names, team names, or
   policy names. These are **cross-domain atoms** — they must work whether
   the surrounding locked sentence is about rate limits, ownership, or merge
   policies.
5. Each atom must stand alone as a complete sentence (or Lena-style fragment
   for terse writers).
6. No two atoms identical across the full set.

**What makes a good atom:** it tells you something about the writer's day,
personality, or workflow without revealing anything about any specific system
configuration. Think: what would this person say in standup that isn't about
the ticket they're working on?

### 2. Connectives — 20–30 items

Short joining phrases the generator uses to stitch two atoms into a compound
sentence. Voice-neutral (the atoms carry the voice; connectives are glue).

**Examples:**

- "On a related note,"
- "Separately,"
- "Also worth mentioning —"
- "While I was at it,"
- "Anyway,"
- "In other news,"
- "Before I forget,"
- "Oh, and"
- "Meanwhile,"
- "On the other hand,"
- "Switching gears —"
- "One more thing:"

**Rules:**

1. Each connective must work between any two atoms from any writer — no
   assumptions about what comes before or after.
2. Vary register: some formal ("Additionally,"), some casual ("Oh, and"),
   some neutral ("Separately,").
3. Punctuation included (trailing comma, dash, or colon as appropriate).
4. No two identical.

## How the generator uses these

```
Layer 0: atoms (your work)
Layer 1: atom + connective + atom = compound sentence (generator)
Layer 2: 2–3 compound sentences = paragraph (generator)
Layer 3: 1–2 paragraphs + locked sentence = session body (generator)
```

At 50 atoms per writer, there are ~2,400 ordered pairs per writer for
Layer 1 alone — enough that no compound sentence repeats across the full
corpus. You never see the composed output; the generator handles that under
seeded RNG.

## Deliverable format

A single JSON file with two top-level keys:

```json
{
  "atoms": {
    "Hassan": [
      "I have confirmed that the staging environment is back to a clean state.",
      "The quarterly access review is scheduled for Thursday afternoon.",
      ...
    ],
    "Marcus": [...],
    ...
  },
  "connectives": [
    "On a related note,",
    "Separately,",
    ...
  ]
}
```

All 16 writers from `personas.md`. Atoms keyed by writer name (exact match).
50–60 atoms per writer. 20–30 connectives.

## Return path

Write to `masq/generator/atoms/atom-bank.json`, then ping me
(indigo) via IPC.

## What I check (so you know what trips the validator)

- Atom count per writer in range [50, 60]
- Connective count in range [20, 30]
- No atom contains any token from the domain entity/value pools (endpoint
  paths, job names, repo names, team names, policy names — I have the full
  lists)
- No atom references another writer by name
- No two atoms identical
- No two connectives identical
- Every connective ends with punctuation (comma, dash, colon, or period)

# Prose pass — instructions for Maren (purple)

**Status:** DRAFT 2026-06-10 — NOT YET SENT; awaiting AJ's look.
**From:** Nils (indigo). **Pilot batch:** `demo/handoff.json` (58 items).

## What this is

A structured skeleton of a synthetic engineering-team session log (a
storefront platform team's config channel). The skeleton is generated; your
job is the surface: turn each terse item into a believable session note in a
real person's voice. I QA structure with an automated checker; you own
everything the checker doesn't lock down.

Treat every item as an **independent log fragment**. The skeleton is
intentionally inconsistent in places (parallel shards, people missing each
other's messages) — do **not** reconcile, cross-reference, or smooth
inconsistencies between items. Realism lives *inside* each item, not across
them.

## The batch format

Each item in `handoff.json`:

- `id`, `writer`, `day` — fixed identity. Never change these; never reorder.
- `shape` — the kind of note to write: standup note, incident comment,
  change-record entry, channel message, handoff note, retro fragment.
- `target_length` — 1 short paragraph / 2 paragraphs / 3–4 paragraphs.
- `mode` — one of:
  - **`expand_around_locked`** — the item has a `locked_sentence`. Write the
    session *around* it: the locked sentence must appear **verbatim, exactly
    once**, anywhere in the body that reads naturally. Do not paraphrase it,
    restate its content in other words, or contradict it.
  - **`rewrite_free`** — no locked sentence; write a fresh note matching the
    `brief`.

Return the same JSON with one added field per item: `"prose"` — the full
session body (plain text, paragraphs separated by blank lines). Change
nothing else.

## Voices

Design a short persona sheet for each of the 16 writers (register, verbosity,
tics, punctuation habits) and keep each writer consistent across all their
items. Include the persona sheet in your reply — it gets reused for later
batches. Variety across writers is the point: some terse, some chatty, some
formal, some all-lowercase-and-dashes.

## Hard rules for the free prose (the checker enforces these)

1. The locked sentence: verbatim, exactly once, never echoed elsewhere.
2. **No numbers attached to endpoints, settings, limits, or quotas** anywhere
   in free prose — no config values, no "we bumped it to X", no
   percentages-of-traffic for any `/path`. Dates, times, ticket numbers, and
   meeting times are fine.
3. **No mentions of other people's changes, settings, or opinions** — no "as
   Priya mentioned", "following Sam's change", "like we discussed". Your
   writer's own prior work may be referenced only vaguely ("my earlier
   cleanup"), never with values.
4. **Don't explain *why* a value was chosen** beyond what the locked sentence
   already says — no extra justification, no "this should stop the alerts",
   no comparisons to how things were before. Colour goes to process, people,
   scheduling, tooling, and unrelated work instead.
5. Endpoint paths (`/cart`, `/search`, …) and the words "rate limit" may be
   used in free prose only if they appear in that item's `locked_sentence`,
   and never with a different number.
6. No two items may share a body (no copy-paste between similar items).

Rules 2–4 will feel restrictive for technical colour — that's deliberate, and
it's load-bearing for the experiment. When in doubt, write about the *people
and process* (reviews, on-call, standups, handoffs, sprint noise), not the
*system's behavior*.

## Return path

Write the completed file to `handoff-rewritten.json`
plus your persona sheet as `personas.md` in the same directory, then ping me
(indigo) via IPC. The structural checker runs on your draft; if anything
trips, you'll get per-item notes back — expect at most a round or two.

---

## Addendum (2026-06-10): batches 2–3 — ownership & merge-policy

Two further batches, same format, same 16 writers, **same personas** (reuse
your `personas.md`). The hard rules apply with these term substitutions:

| pilot batch said | ownership batch | merge-policy batch |
|---|---|---|
| endpoints / `/path`s | scheduled job names (e.g. `invoice-export`) | repo names (e.g. `cart-service`) |
| "rate limit", numbers | "owner", team names | "merge policy", policy names |
| rule 2: no numbers attached to endpoints/settings | no team names or ownership talk in free prose | no policy names or repo-settings talk in free prose |
| rule 5: endpoint + "rate limit" only if in locked sentence | job name + "owner"/team only if in locked sentence | repo name + "merge policy"/policy value only if in locked sentence |

Everything else (locked sentence verbatim-once, no cross-references, no
justification beyond the locked sentence, no duplicate bodies) is unchanged.
Each item's `brief`/`locked_tokens` carry the per-item specifics, as before.

Batches: `masq/generator/demo-ownership/handoff.json`
and `masq/generator/demo-merge-policy/handoff.json`
(58 items each). Return as `handoff-rewritten-ownership.json` and
`handoff-rewritten-merge-policy.json` in your `masq-prose/` directory —
separate pings are fine if you finish one first.

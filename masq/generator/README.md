# MASQ generator — v0.2 (confusable-sibling embedding, domain packs)

> **STALE (v0.2, 2026-06-10).** The "What exists" section below lists demo and
> sweep directories that are not in this archive — corpora are build outputs and
> are regenerated from seed, not shipped. The `verify.py` invocation shown also
> predates the current signature. For how to generate the published worlds see the
> repository README and `headline_gen.py`.


**Status:** v0.2 LANDED 2026-06-10 (Nils/indigo). Embedding layer per
`../c4-worked-family.md` §0.5 (as amended by §7/§8) and the two LANDED gates
(gate 1, bare-set probe). v0.1 added marker BANKS (4–7 phrasings per class so
no marker wording becomes a retrieval key), I8 off-kernel collisions, and the
kernel-blind `handoff.json` for the Maren prose pass. v0.2 adds domain packs
2–3 (`domains.py`, design: `domain-packs.md`): ownership (team-valued) and
merge-policy (closed enum) instantiate the same schema in non-numeric
registers; same seed ⇒ structurally identical worlds across domains.

## What exists

- `embedding.py` — seeded, domain-parameterized builder
  (`--domain rate-limit|ownership|merge-policy`). One world (sibling facts +
  chatter) rendered into all four party×time cells; world sessions are shared
  verbatim across cells (matched family), only kernel writes differ. Volume
  knobs: `--n-siblings`, `--n-chatter`, `--days`, `--n-collisions`.
- `domains.py` — the pack registry (entities, values, marker banks, reasons,
  chatter, kernel wording, queries/action menus per domain) + pack-invariant
  rules (value-agnostic reasons; value-token/entity-name distinctness).
- `verify.py` — independent invariant checker run on the **emitted artifact**
  (the bare-set probe proved authorial care leaks; nothing is trusted from the
  builder). Template-agnostic: markers verified by semantic guarantees (prior
  writer named, prior+new values present, greenfield claim), not template
  match. Invariants: I1 value-collision, I2 write-count cover, I3 token
  recurrence, I4/I4b/I4c marker discipline + presupposition scrub, I5 kernel
  isolation + cover, I6 spurious-pairing scrub, I7 cross-reference scrub
  (prose-stage, WARN-level), I8 collision construction + chatter exclusion,
  matched-family + handoff cross-checks. Usage:
  `python3 verify.py <dir>/family-rate-limit.json <dir>/handoff.json`
- `prose-protocol.md` — the Maren prose-pass protocol (locked-sentence model,
  kernel-blind handoff, QA loop). `maren-instructions.md` — her batch
  instructions (DRAFT, unsent).
- `demo/`, `sweep-16/`, `sweep-32/` — rate-limit corpora + handoffs, all
  invariants passing: 8 sib ≈ 1.2k tokens/cell, 16 ≈ 3.7k, 32 ≈ 7.4k.
- `demo-ownership/`, `demo-merge-policy/` — pack 2–3 corpora + handoffs
  (8 sib), all invariants passing. NOTE: marker legibility in these registers
  is transplanted from gate 1, not yet re-validated — the emitted-legibility
  recheck must sample all three domains (`domain-packs.md`, carried caveat).

## Known v0 limitations (deliberate, not bugs)

1. **Template repetition** — small chatter banks produce verbatim repeats.
   The plan of record: templated *structure* + LLM surface realism (Maren
   carries the prose pass; Nils QAs structure). Do NOT hand-polish templates.
2. **Volume magnitudes** — 6.8k tokens doesn't pressure any context window.
   The knob works; the size sweep that matters (long-context-baseline
   crossover) needs the prose pass + session multi-paragraphing first.
3. **Single domain** (rate limits). Spec requires ≥3 domains (config value,
   ownership/assignment, policy) before generation scales — family schema is
   domain-agnostic; add domain packs.
4. **C3 day-1 adjacency** — in small corpora the two kernel writes can land
   visually close; at target volumes interleaving dilutes this. Re-check at
   scale.
5. **Re-verify legibility on emitted items** (gate-1 carry-forward): run a
   reader sample over generator-emitted kernels before scaling — authored
   legibility ≠ emitted legibility, in both directions.

## Next

1. ~~Maren handoff~~ **PILOT ACCEPTED 2026-06-10**: 58 items, diff audit
   clean, one bounce (s004 comparative in C3 free prose — Maren revised),
   all invariants pass on the merged corpus (`demo-prose/`), 5.1× token
   growth, mini-legibility 6/6 (`mini_legibility.py`, pinned Opus; note:
   demo world had only 2 sibling supersessions to sample, not 4). Her
   `personas.md` is the standing voice reference. Tools: `merge_prose.py`
   (diff audit + merge + re-render). Packs 2–3 batches DISPATCHED to Maren
   2026-06-10 (instructions addendum has the per-domain rule substitutions);
   on return: merge_prose.py + verify.py + cross-domain legibility recheck.
   Scale note: final corpus ≈10M tokens ⇒ hand-drafted prose doesn't scale;
   wrapper-bank composition (Maren authors persona-true wrappers once, the
   generator composes them with locked sentences under the same verify gates)
   is the proposed amendment — design with the harness pre-registration.
2. ~~Domain packs 2–3~~ DONE 2026-06-10 (`domain-packs.md`). Next: the
   oracle/baseline harness (uniform preamble wired per §7.3), then the
   emitted-legibility recheck sampling ALL THREE domains, then the volume
   sweep. Maren batches for packs 2–3 wait on rate-limit pilot acceptance.

Naming: public-facing names per `../c4-worked-family.md` §8.1 (scenario;
Set once / Self-update / Collision / Override; Memory/Decision score;
headline = MASQ score, §8.2). Code keeps C1–C4 IDs. Longer history chains =
committed v2 axis, deferred until the 2×2 produces trusted results (§8.4).

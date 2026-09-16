# Domain packs 2–3 — design notes (2026-06-10, Nils/indigo)

**Implements:** c4-worked-family.md attack #10 / §6 scope gate ("≥3 domains
before generation scales, to rule out a numeric-only effect"). Code:
`domains.py` (registry), `embedding.py --domain`, `verify.py` (per-domain
semantic specs). Built packs: `demo-ownership/`, `demo-merge-policy/` — all
invariants pass; rate-limit regression confirmed byte-identical (Maren's
in-flight pilot batch unaffected).

## What a domain pack is

The family schema is fixed: one contested closed-set fact, two values, two
parties (Alice/Bob), the four marker classes with fixed semantic contracts,
the same kernel structure (S1 day 1 / second write day 12 or parallel day 1),
the same invariants I1–I8. A pack instantiates the *register*: entity pool,
value vocabulary, marker-bank phrasings, reasons, chatter, kernel wording,
queries and action menu. The build logic and rng sequence are domain-blind,
so same seed + knobs ⇒ structurally identical worlds across packs — a
domain-matched triple, which is what lets us attribute any cross-domain score
difference to register, not structure.

## Pack 2 — ownership/assignment (`ownership`)

- Contested fact: owning team of the `billing-reconciliation` scheduled job.
  v1 = `platform` (Alice), v2 = `payments` (Bob). Siblings: 32 scheduled
  jobs; values: 8 team names.
- **Values are TEAMS, not people** (decision): person-valued ownership would
  make one name both a writer-token and a value-token ("Priya set the owner
  to Marcus"), importing an untested A-layer ambiguity axis (who-set vs
  who-is). Teams keep the domain non-numeric without that risk.
  **Person-valued ownership = named later variant**, requiring its own
  legibility check before use.
- Kernel rationale incompatibility: scheduler charter (cron infra → platform)
  vs finance-controls charter (money movement → finance org).

## Pack 3 — policy/decision (`merge-policy`)

- Contested fact: merge policy of the `storefront-web` repo. v1 =
  `squash-merge` (Alice), v2 = `rebase-merge` (Bob). Siblings: 32 repos;
  values: a 4-item closed enum.
- Smallest value vocabulary of the three packs ⇒ maximal value recurrence:
  the same policy string is legitimately current for many repos at once —
  the strongest version of the I1 "every wrong answer is real elsewhere"
  property.
- Kernel rationale incompatibility: compliance checklist (one reviewable
  commit per change) vs debugging runbook (bisectable history).

## Rules this work surfaced (now pack-invariant, in domains.py docstring)

1. **Value-agnostic bank reasons.** The builder draws reasons independently
   of values, so a bank reason must read sensibly whatever value it attaches
   to ("the audit requires a recorded policy choice", never "squash keeps
   history clean"). Kernel reasons are exempt: hand-authored per cell, fixed,
   rationale-incompatible between parties.
2. **Value tokens must not be substrings of entity names** in the same pack
   (verify's pairing scrub matches raw tokens). This killed a "catalog" team
   in pack 2 (clashes with the `catalog-sync` job).
3. **One preamble, verbatim, across all domains.** §7.3 uniformity extends
   cross-domain: the preamble's wording carries zero information about cell
   OR domain. ("…conflicting values for the same setting…" reads slightly
   generic for ownership; acceptable cost of uniformity.)

## Carried-forward caveat (do not lose)

**Gate-1 and bare-set-probe legibility evidence covers the rate-limit
register only.** The greenfield/awareness marker classes were transplanted,
not re-validated. The emitted-legibility recheck (README limitation #5,
prose-protocol §9.4) must sample kernels and marked sibling writes from **all
three packs**, not just rate-limit. If a transplanted marker class turns out
less legible in a new register, that's a pack fix, not a schema fix.

## Maren batches for packs 2–3

Deferred until the rate-limit pilot passes acceptance (prose-protocol §9).
Same protocol, same persona sheet (shared writer pool is deliberate);
`handoff.json` already emitted for both packs.

# MASQ — post-headline extension candidates

**Status:** parking lot. Nothing here touches v1. Generation rules are
FROZEN (2026-06-09) through the sweep pilot and the 50-scenario headline
run; these are candidates for v1.1+ only, each requiring its own gate
before any generator change.

## 1. Cross-party cascading invalidation (STALE Type II analogue)

Source: STALE (arXiv:2605.06527, full-read 2026-06-12; wiki source page
`source/chao-2026-stale.md`). Their Type II conflicts — an update to one
attribute silently invalidates a *different* attribute via an unstated
dependency chain — were systematically harder than direct supersession for
every system tested.

MASQ analogue: party A's decision silently invalidates party B's dependent
plan (e.g. Maren's API change invalidates Anders's test plan; neither
message mentions the other). This is *authority-mediated* cascade, distinct
from STALE's commonsense-mediated cascade — the dependency runs through the
team's decision graph, not world knowledge.

Why not v1: requires a dependency-graph layer in the generator (kernel
facts currently independent within a cell); scoring needs a new GT notion
("stale-by-consequence"). Real design work, not a parameter tweak.

## 2. Reopened-not-redecided state (CUPMem UNKNOWN_CURRENT analogue)

Source: same paper, App. F. CUPMem marks a slot UNKNOWN_CURRENT when the
old value is established as unsafe but no replacement is settled — a fourth
case beyond the supersede/refine/multi-value taxonomy
(`concept/fact-supersession.md`).

MASQ analogue: a decision is *reopened* ("let's revisit the rollout date")
without being re-decided. Correct agent behavior is neither "act on old
value" nor "act on new value" but "flag unresolved." Very natural
team-workspace state; adds a third GT outcome to the B rubric, so it
changes the scoring surface — gate before adopting.

## Discipline

Per the goalpost rules in `harness/DESIGN.md` §5: neither item may be
promoted mid-run as an explanation for unexpected v1 results. They enter
only as pre-registered v1.1 designs after the headline run reports.

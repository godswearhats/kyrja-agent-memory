---
type: hypothesis
name: H-QUAL-FLOOR — bad source produces harmful memory
status: REJECTED
last_ingested: 2026-05-13
sources: [../experiment/2026-05-11-write-quality-variance/README.md]
epistemic_tags: [measured]
tags: [encoding, write-side-quality, scope-bounded]
---

## Claim

Memory distilled from a degraded source (truncated, incomplete, or failed prior session) produces harmful memory — i.e., presence of that memory increases task cost beyond cold, or causes the agent to make wrong choices.

**Scope note.** This hypothesis was framed broadly. Empirical work to date tests **mild** source degradation only. The REJECTED status applies to the mild regime; the worst-case regime is untested. See [worst-case-source](../open-question/worst-case-source.md "pending").

## What would falsify it

A memory variant distilled from a degraded source increases cost (or reduces task quality) relative to cold or relative to memory distilled from a clean source, with disjoint confidence intervals.

## Evidence for

None. The hypothesis was not supported in the regime tested.

## Evidence against

- Exp 1 variant D (truncated-source briefing): mean cost $0.197, 4/4 pass. No degradation vs other memory variants; cheaper than cold ($0.295). The agent recovered the missing context by inference. `[MEASURED]` from [write-quality variance experiment](../experiment/2026-05-11-write-quality-variance/README.md). *Construct-validity:* cost measures token spend; "harmful memory" should manifest as elevated cost vs cold or vs clean-source memory. Neither happened — D was cheaper than cold and not meaningfully different from other memory variants.

## Open sub-questions

- **Worst-case regime.** Does the rejection hold when the source is a **fully-failed session** (wrong patch, wrong analysis, wrong abstractions)? Not tested. See [worst-case-source](../open-question/worst-case-source.md "pending").
- **Non-monotonic regime.** Is there a sweet spot where modestly-degraded memory is *more* harmful than severely-degraded memory because the agent over-trusts a partial signal? Plausible; not tested.
- **Tolerance threshold.** At what level of source degradation does memory start hurting? A degradation-axis sweep with adequate n would resolve.
- **Practical implication.** If the rejection generalizes to worst case, the write-side quality gate is **deferrable** in MTP — encoding can be best-effort. Load-bearing design decision riding on the worst-case experiment.

## Related

- [write-quality variance experiment](../experiment/2026-05-11-write-quality-variance/README.md) — evidence anchor.
- [worst-case-source](../open-question/worst-case-source.md "pending") — the residual untested regime.
- write-side quality gate deferrable (pending atomization from tool-chain-wedge-goals-2026-05-11.md).

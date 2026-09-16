---
type: open-question
name: Worst-case source degradation for H-QUAL-FLOOR
status: OPEN
last_ingested: 2026-05-13
sources: [../experiment/2026-05-11-write-quality-variance/README.md]
epistemic_tags: [measured, speculated]
tags: [encoding, write-side-quality, load-bearing-design-decision]
---

## The question

[H24 H-QUAL-FLOOR](../hypothesis/H24-qual-floor.md) was REJECTED for **mild** source degradation: a truncated briefing (Exp 1 variant D) produced no measurable harm vs cold or other memory variants. Does the rejection generalize to the **worst case** — memory distilled from a fully-failed session (wrong patch applied, wrong analysis recorded, wrong abstractions formed)?

## Why it matters

This is a **load-bearing design decision** for the MTP build.

- If worst-case memory is **still non-harmful**: the write-side quality gate is *deferrable* — encoding can be best-effort, MTP ships without a quality classifier, the wedge product simplifies materially.
- If worst-case memory is **harmful**: the gate is *mandatory* and the wedge architecture grows a layer ([seven-layer stack](../concept/seven-layer-stack.md) admission control becomes more than a precision filter; it must also gate the *write* path on source quality). Cost and complexity of MTP go up substantially.

The Exp 1 variant D result (`[MEASURED]` — see [write-quality variance experiment](../experiment/2026-05-11-write-quality-variance/README.md)) is suggestive but does not license the deferral decision at worst case. Construct-validity matters here: truncation reduces *quantity* of correct information; a fully-failed session injects *incorrect* information. These are different perturbations and the agent's response may differ qualitatively.

## What evidence would resolve it

A worst-case experiment with the structure:

1. **Construct a deliberately-failed source session.** AJ does a real software task badly — applies a wrong patch, draws a wrong conclusion about the bug, names an abstraction incorrectly, leaves stale assumptions in trace. Record the full session as the encoding source.
2. **Distill memory** from that session using the same pipeline as the wedge product (4.5 or 4.6 distillation, slot-format encoding per [H27 / H25](../hypothesis/H25-replicate.md)).
3. **Run a clean evaluation task** that *would benefit from correct memory of the same area*. Compare:
   - cold (no memory),
   - clean-source memory (control),
   - worst-case-source memory (treatment).
4. **Measure**: cost, pass-rate (with a wedge-aligned pass metric, not SWE-bench gold — see [retracted pass-rate claim](../experiment/2026-05-11-write-quality-variance/README.md)), and *direction-of-error* (did the agent inherit the wrong abstraction from memory and propagate it?).

**Adequate signal**: even small n (n=4 per arm, matching Exp 1) is informative if the worst-case arm exceeds cold cost or produces wrong-direction outputs with disjoint CIs. Non-monotonicity (mild degraded < worst degraded) would be the most actionable finding.

## Sub-questions

- **Direction-of-error metric.** Cost alone may miss the failure mode. A worst-case memory that *quickly steers the agent wrong* could be cheap-and-wrong; cost would look fine. Need a quality dimension that catches inherited-error.
- **Recovery rate.** Variant D showed the agent recovered missing context by inference. Can the agent similarly *reject* wrong context? Or does memory get over-trusted by default?
- **Tolerance threshold.** Where on the degradation axis does memory start hurting? A monotonic sweep (clean → mild → moderate → severe → adversarial) would map the threshold; current data is two points (clean, mild).
- **Adversarial regime.** Worst-case-by-accident vs worst-case-by-attack are different. The wedge product is not currently considering adversarial memory; whether to is its own decision.

## Related

- [H24 H-QUAL-FLOOR](../hypothesis/H24-qual-floor.md) — the hypothesis whose worst-case regime this question covers.
- [write-quality variance experiment](../experiment/2026-05-11-write-quality-variance/README.md) — Exp 1 variant D is the mild-regime evidence anchor.
- write-side quality gate deferrable decision (pending atomization from tool-chain-wedge-goals doc) — the design decision riding on this question.
- [BIG-PICTURE (2026-05-14 archive)](../archive/BIG-PICTURE-2026-05-14.md) — MTP build (Goal 5) is the natural vehicle for the worst-case experiment; gated on the [current path-decision](../NOW.md).

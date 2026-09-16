---
type: concept
name: Kerros — the substrate-memory research program
status: timeless
last_ingested: 2026-06-07
program: kerros
sources: [../source/xu-2026-agentic-memo.md, ../source/lecun-2022-autonomous-mi.md, ../source/mcclelland-mcnaughton-oreilly-1995-cls.md, ../source/zhang-2026-compression-spectrum.md]
epistemic_tags: [asserted, speculated]
tags: [kerros, research-program, charter, substrate-memory]
---

> **Program charter.** This page defines Kerros and the rule for what belongs to it. It is the anchor for every `program: kerros` page. ("Kerros" is Finnish for *layer / stratum* — memory at the substrate layer.)

> **Status note (2026-06-07): program PARKED — reversible.** Active work moved to the MASQ benchmark paper (`program: masq-bench`); see [decision/masq-paper-as-active-program](../decision/masq-paper-as-active-program.md). No Kerros finding is superseded (Gate 1 stands); resume threads are recorded in [NOW.md](../NOW.md).

## Definition

**Kerros** is the research program for **memory the model thinks *with*** — memory as a property of the model's computation (its state, modules, or generative dynamics), not an external store the model reads from a prompt. It is the substrate side of the [memory-consumer-axis](./memory-consumer-axis.md): memory-for-the-model, as opposed to memory-for-the-agent.

Kerros is a **research program**, not a product. Its success criterion is a validated, falsifiable scientific claim — a contribution to how durable memory for a model can work — not revenue or market share. The commercial line (memory-for-the-agent, bolt-on) is a separate, separately-named project, decoupled from Kerros. `[ASSERTED]` (AJ, 2026-05-25.)

This separation was made explicit on 2026-05-25, after the "Kyrja" umbrella was found to be conflating the two goals — and after the [tier-3-4 wedge](../decision/tier-3-4-as-wedge.md) framing was diagnosed as substrate **research** justified with product **wedge** language (it bottomed out in "labs would notice," not user need). Naming the programs separately dissolves that conflation.

## The dividing line: integration, not persistence

The test for whether something belongs to Kerros:

> **Persistence is boltable. Integration is the bet.**

- **Persistence** — does information survive to the next session? Trivially achievable by a frozen LLM + external store + prompt engineering (write to disk, read it back). This is memory-for-the-agent; the agentic-memory products ([Mem0](../incumbent/mem0.md), [Zep](../incumbent/zep.md), [Letta](../incumbent/letta.md)) ship it. → **product, not Kerros.**
- **Integration** — does the persisted information enter the model's *computation*, so the model reasons *with* it rather than reading it as an input? This is what a database structurally cannot do. → **Kerros.**

This is the same property viewed three ways: **malleability** (cognitive — humans don't replay records, they reconstruct, and the act of recall re-writes the trace; Schacter reconsolidation), **integration** (architectural), and **not-boltable** (the gate below). AJ's framing, 2026-05-25: *"as humans we don't actually remember — we synthesize on the fly — but our memory is malleable whereas yours is not."* `[SPECULATED]`

## The validity gate

A Kerros result counts only if it does something a **bolt-on baseline provably or empirically cannot** at the same task. The bolt-on is not a competitor to out-engineer; it is the **control**.

**Refined 2026-05-26:** the gate is not binary ("can a bolt-on do X?") but a **scaling separation** — does the bolt-on's imitation cost *diverge* with problem complexity? A bolt-on can imitate almost anything weakly; it counts as integration only when the imitation cost blows up. See [integration-gate](./integration-gate.md) for the full treatment, the capability-map result (the bet collapses to *non-frozen weights*: composition on the read side, consolidation on the write side), and the M10 exclusion.

The formal target is the sample-complexity separation of [Xu, Dai & Zhang 2026, Theorem 1](../source/xu-2026-agentic-memo.md): on a compositional task family, retrieval-based memory requires `Ω(k²)` examples while parametric memory requires `O(d)` — a separation of `Ω(k²/d)` `[ASSERTED]` (construct-validity note: the theorem concerns a *constructed* compositional task family, not arbitrary tasks; a Kerros experiment must instantiate a task that actually sits in that family for the separation to bite). If a vector-DB bolt-on matches a Kerros result, the result is not substrate research — it is reinvented retrieval.

This gate is the direct analog of the **BoW-at-chance gate** ([tier-3-structural-vs-semantic](../open-question/tier-3-structural-vs-semantic.md)): define the baseline that must fail *before* running, or you are measuring the wrong thing.

The gate doubles as the **program-assignment rule** for the wiki: not-boltable → `kerros`; boltable → product/unassigned (see [SCHEMA § Program assignment](../SCHEMA.md#program-assignment-v07)).

## Beachhead: the composition separation

**Revised 2026-05-26 (the wide-pass re-grade).** The 2026-05-25 framing named [cross-session continuity](../open-question/cross-session-continuity.md) as the beachhead. Run through the refined [integration gate](./integration-gate.md), continuity is **persistence (product)** — its bolt-on control (context replay) is the *weakest* separation on the map, and it gets weaker as context windows grow. So the beachhead is not continuity itself but the **composition separation**: the one capability with a *provable* divergent gap ([Xu Theorem 1](../source/xu-2026-agentic-memo.md)).

The experiment shape (spec not yet locked): a composition rule with real structure, `ᾱ < 1` empirically established (the frozen model can't do it in-context, however many demos), then show the integrated path learns it from ~`O(d)` while the best bolt-on text-rule control — same content, source experience held constant — stays stuck. Cross-session continuity may still be the *setting* the task is dressed in (it supplies a shipped bolt-on to measure against), but the *contribution* is composition, not continuity.

**Beachhead, not goal.** Solving continuity alone would be boltable — and would belong to the product line, not Kerros.

## Position in the field (2026-05-26)

A literature survey (2026-05-26) places Kerros precisely. The agent-memory field is densely populated but **entirely scaffold-level** — [Zhang et al. 2026's Experience Compression Spectrum](../source/zhang-2026-compression-spectrum.md) maps ~22 systems, all memory-for-the-agent, with weight-integration *explicitly out of scope*. The weight-integration work that does exist (Skill-SD, ParamMem) lives in a separate RL/training community the memory community doesn't cite. Kerros sits in the **unoccupied bridge** between them; [Xu 2026](../source/xu-2026-agentic-memo.md) is the lone bridge paper, and it is a *position* paper with no build. A frontier-shaped gap — under-confirmed (a 3-paper survey; the citation-graph call was rate-limited), but the clean compositional-separation demonstration appears unclaimed in what we checked. `[ASSERTED]`

## Projects under Kerros

Kerros is an umbrella; individual research efforts under it get their own names.

- **The [caddy](./caddy.md)** — sidecar architecture; its load-bearing research targets are the auxiliary-loss representation pathway ([H44 / T_A1b](../hypothesis/H44-T_A1b-cross-domain-transfer.md)) and schema-fit-modulated consolidation ([H40 / K2+T_A3](../hypothesis/H40-schema-fit-modulated-consolidation.md)). See [caddy-as-research-program](../decision/caddy-as-research-program.md).
- Future divergent efforts get named as they arise.

## Scope limits

- Kerros is a *goal/consumer* distinction (memory for the model), not an architecture. It does not commit to P1/P2/P3 ([substrate-paradigms](./substrate-paradigms.md)) — that is an internal design choice.
- Kerros does not *own* the cog-sci grounding pages or the substrate literature; it *uses* them. Those pages are assigned to Kerros as they are touched, per the lazy-assignment rule.
- "Research program, not product" does not mean exempt from rigor — it means the success criterion is a falsifiable claim, not a customer. Kerros is *more* exposed to falsifiability, not less.

## Related

- [memory-consumer-axis](./memory-consumer-axis.md) — the axis (model vs agent) Kerros sits on the model side of.
- [substrate-as-memory](./substrate-as-memory.md) — the paradigm Kerros works within.
- [substrate-paradigms](./substrate-paradigms.md) — the P1/P2/P3 design space.
- [consolidation-channel](./consolidation-channel.md) — candidate Kerros mechanism.
- [cross-session-continuity](../open-question/cross-session-continuity.md) — the beachhead.
- [tier-3-structural-vs-semantic](../open-question/tier-3-structural-vs-semantic.md) — carries the BoW-at-chance gate; the question that triggered the program split.
- [tier-3-4-as-wedge](../decision/tier-3-4-as-wedge.md) — the product-wedge-framed decision being split into research vs product (deferred).
- [caddy-as-research-program](../decision/caddy-as-research-program.md) — 2026-05-20 predecessor decision; decoupled commercial from research.

## Source archive

Program split surfaced in the 2026-05-25 Nils/AJ session (continuation after the ceiling-probe finding). AJ's articulation: two distinct goals operating close together semantically — a product (memory the agent uses, commercial) and a research contribution to AGI (memory the model thinks with). Kerros names the latter.

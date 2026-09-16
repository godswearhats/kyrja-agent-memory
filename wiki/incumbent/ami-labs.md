---
type: incumbent
name: AMI Labs (Yann LeCun's Paris stealth)
status_current_as_of: 2026-05-16
last_ingested: 2026-05-16
sources: [../source/lecun-2022-autonomous-mi.md]
tags: [incumbent, well-funded, frontier-class, integrated-architecture, jepa, lecun, different-shape-same-mission]
---

## What it is

Stealth-phase AI lab founded by **Yann LeCun** after his November 2025 departure from Meta. Based in Paris. **$1.03B seed round March 2026** at ~$3.5B valuation target. Co-founders include **Saining Xie** (ex-DeepMind, CSO). Stated technical goal: build a JEPA (Joint Embedding Predictive Architecture) world-model substrate with *"persistent memory, reason, plan complex action sequences."*

**Architecture is integrated, not sidecar.** Memory is a property of the world-model substrate, not a separately-architected module that pairs with an LLM.

## What it does

`[ASSERTED]` based on LeCun's public commitments and the funding-announcement framing.

- **JEPA-based world model substrate** as the core architecture (LeCun's published research line since 2022)
- **Persistent memory as a stated capability** of the integrated architecture (not a separate module)
- **Frontier-class compute and team scale** — $1B seed, multiple ex-frontier-lab founders

## What it doesn't do (per public framing)

- **Not a sidecar memory module.** Memory is architectural, not pluggable.
- **Not cog-sci-first.** LeCun's framing is engineering-and-world-model-first; biology is influence not authority.
- **Not yet shipping.** Stealth as of 2026-05-16; no public product, no published architecture beyond JEPA continuation work.

## Seven-layer-stack mapping

`[SPECULATED]` Stealth architecture; mapping is speculative pending disclosure.

Key inference: a JEPA world-model substrate with persistent memory is most plausibly a *single integrated network* that handles all seven layers internally rather than offering them as distinct modular layers. **AMI Labs is likely to fail or skip the seven-layer-stack framing entirely** because the JEPA architecture doesn't decompose along those lines.

## Norman-rubric mapping

`[SPECULATED]` Stealth architecture. **CG-rubric visible score: 3/5** based on LeCun's public commitments to persistent memory + LLM-class systems + commercial intent. Norman rubric scoring impossible until architecture is disclosed.

LeCun's JEPA framing is *engineering-first*, not cog-sci-first. CG1 (explicit cog-sci grounding by mechanism citation) is weak in his public materials. The architectural choice (integrated, not modular) means even if they ship a strong memory system, it won't be in the same cell as [caddy](../concept/caddy.md).

## Where it might fail or differ

- **Integrated architecture has different deployment story.** AMI Labs ships if-and-only-if their whole foundation model ships — they cannot offer the memory layer as a standalone product or a sidecar for other LLMs. This is the opposite trade-off from the caddy sidecar approach.
- **JEPA world-model bet is contested.** LeCun has been advocating JEPA since 2022; major commercial validation has not yet arrived. If JEPA does not scale, AMI Labs' memory story collapses with it.
- **No cog-sci-first signal.** Norman rubric properties (event segmentation, schema-fit, reconsolidation, temporal contiguity, competition) are not in LeCun's public memory-related framing. The "persistent memory" promise is generic.

## Relevance to the wedge

**AMI Labs is a frontier-class competitor in a different cell.** They occupy the *integrated-architecture* slot — direct competition for Anthropic, OpenAI, DeepMind, Mistral on the foundation-model axis, including the persistent-memory subgoal. Kyrja occupies the *sidecar caddy* slot — pairs with existing open-weights LLMs, scope-swappable per user/context.

**As long as JEPA-integrated and sidecar-caddy remain different architectural commitments, AMI Labs and Kyrja are not direct competitors.** They become direct competitors if:
- AMI ships a memory layer that can be offered as a standalone sidecar (currently not in their framing)
- Kyrja's caddy gets re-architected as part of an integrated foundation model (not the current plan)

**Threat shape:** frontier-class entity with overlap on the product goal (persistent memory in AI assistants) but architectural divergence. Pitch positioning: "AMI Labs is building a new foundation model with integrated memory; we're building a memory layer for the existing open-weights ecosystem. Different bets, different timelines, both can win."

**Watch flag:** if AMI Labs publishes JEPA architecture details that include a separable memory module, the threat-shape changes. Currently they read as integrated.

## Related

- [memory-caddy](../open-question/memory-caddy.md) — competitive landscape framing
- [norman-rubric](../concept/norman-rubric.md) — cannot score until disclosure
- [lecun-2022-autonomous-mi](../source/lecun-2022-autonomous-mi.md) — LeCun's published JEPA framing

## Source archive

- The Decoder coverage: https://the-decoder.com/you-certainly-dont-tell-a-researcher-like-me-what-to-do-says-lecun-as-he-exits-meta-for-his-own-startup/
- Tech.eu and other coverage of $1B seed round March 2026
- LeCun JEPA papers (published prior to AMI Labs founding)

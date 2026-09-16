---
type: open-question
name: Is tier-3 structural/analogical retrieval a distinct capability from tier-1/2 semantic retrieval?
status: OPEN
last_ingested: 2026-06-07
sources: [../experiment/2026-05-18-T_A1b-isolation-derisk/ceiling-probe.md]
epistemic_tags: [measured, speculated]
tags: [tier-3, wedge, construct-validity, structural-retrieval, bag-of-words, drawing-board]
---

## The question

The [tier-3-4 wedge](../decision/tier-3-4-as-wedge.md) bets the whole research program on tier 3 (analogical / structural retrieval) being a capability that *does not exist in production and is distinct from* tier 1-2 semantic retrieval. The [full-arc ceiling probe](../experiment/2026-05-18-T_A1b-isolation-derisk/ceiling-probe.md) (2026-05-25) raised a prior question the wedge assumed away: **for narrative patterns, is "structural" retrieval even separable from semantic/lexical retrieval?**

## Why it matters

`[ASSERTED]` If pattern can be identified from surface vocabulary, then a retriever that finds same-pattern memories is doing semantic similarity, not structural abstraction — which is exactly [H44](../hypothesis/H44-T_A1b-cross-domain-transfer.md)'s own stated failure mode (*"fancy embedding similarity the base LLM already does for free"*). The wedge's strategic claim — a capability that doesn't exist today — collapses if tier 3 reduces to good tier 2.

## The evidence that prompted it

`[MEASURED]` On the arc test set, a bag-of-words classifier decodes the five patterns at **82%** from *clean narrative prose alone* (chance 20%), and 97.5% with the structural scaffolding that had leaked into the data. *(Construct-validity: PCA→50 + ridge, 5-fold CV, log-count features over candidate text; details in the [ceiling probe](../experiment/2026-05-18-T_A1b-isolation-derisk/ceiling-probe.md).)* So "narrative pattern" is substantially a **lexical-semantic** category. The intuition behind it: you cannot describe a betrayal's violation beat without violation-semantic words — the events that constitute a pattern carry characteristic vocabulary.

## The reusable validity gate

`[ASSERTED]` **A valid tier-3 structural test must drive an order-blind baseline (bag-of-words) to chance.** Pattern must be carried by event *order / causal relations*, with vocabulary held ~constant across positive and negative — otherwise a word-counter passes and the test cannot distinguish structure from semantics. The current arc test fails this gate by a wide margin (BoW 82% on clean narrative). The de-risk's existing anti-contamination measure (forbidding pattern *names* in generation) was necessary but far from sufficient.

## What would resolve it

`[SPECULATED]`

- **Tier 3 is distinct** if we can construct a BoW-at-chance test (pattern = event order/relations, vocabulary matched between positives and negatives — e.g. the *same* events permuted into different causal structures) **and** a structural retriever beats strong semantic baselines on it. This is plausibly a Nils-designs-schema / Maren-drafts-prose construction task ([[reference_maren_prose]]).
- **Tier 3 collapses into tier 1-2** if such a test cannot even be built — if "pattern ⟂ vocabulary" is ill-posed for natural narrative. That would be a real negative update on the wedge's differentiation and would force a rethink of what the caddy's load-bearing novel capability actually is.

## Status

`[ASSERTED]` AJ is taking the wedge / tier-3 framing **back to the drawing board** (2026-05-25). This page holds the construct-validity finding and the validity gate so the rethink starts from them. Masked-prediction ([masked-vs-forward-prediction](./masked-vs-forward-prediction.md)) stays paused; backlog stack-rank likely needs re-derivation after the rethink.

## Related

- [ceiling probe](../experiment/2026-05-18-T_A1b-isolation-derisk/ceiling-probe.md) — the experiment that opened this.
- [tier-3-4-as-wedge](../decision/tier-3-4-as-wedge.md) — the decision whose premise this questions.
- [memory-retrieval-tiers](../concept/memory-retrieval-tiers.md) — defines tiers 2 and 3, whose distinctness is in question.
- [H44](../hypothesis/H44-T_A1b-cross-domain-transfer.md) — the load-bearing hypothesis; its "fancy embedding for free" failure mode is the crux here.
- [caddy-architecture](../concept/caddy-architecture.md) — T_A1/tier-3 is the load-bearing T4 this bears on.

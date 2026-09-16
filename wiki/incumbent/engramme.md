---
type: incumbent
name: Engramme (Harvard spinout)
status_current_as_of: 2026-05-16
last_ingested: 2026-05-16
sources: [../source/dong-2025-norman-episodic.md]
tags: [incumbent, personal-data-rag, harvard-spinout, mayfield-backed, hippocampus-marketing, top-priority-vc-comparison]
---

## What it is

Harvard spinout (originally named Memorious, rebranded to Engramme March 2026) building "Large Memory Models" — an encrypted personal-data memory layer that ingests user content (Gmail, Zoom transcripts, photos, texts, Slack, Google Docs, Meta glasses) into a per-user index ("memerome") and surfaces it proactively across apps. Founded by **Gabriel Kreiman** (CEO, Harvard Medical School neuroscientist, 20-year hippocampus lab, 160+ publications) and **Spandan Madan** (CTO, Harvard CS PhD, prior at MIT CSAIL, Google DeepMind, Meta, Adobe).

**Funding:** $3M pre-seed (Mayfield), closing. Raising $100M Series A at ~$1B valuation per Bloomberg April 10 2026.

**Stealth exit:** March 2026 (as Engramme). Consumer iOS app in beta. Enterprise API in public beta.

**This is the top entity Kyrja will be compared to in VC diligence.**

## What it does

- **Per-user encrypted personal-data index** ("memerome") integrating Gmail/Zoom/WhatsApp/Slack/Google Docs/Meta glasses content
- **Proactive retrieval** — surfaces relevant information without explicit search query
- **Associative recall framing** — public materials cite hippocampal indexing as the inspiration
- **iOS app in beta** for consumer use
- **Enterprise API in public beta** for developers and teams
- **Self-described positioning:** *"a purpose-built AI architecture that does not follow the transformer paradigm... retrieves actual memories tied to real events"* and *"hallucinations are structurally impossible within its memory layer"* (TestingCatalog public-beta launch coverage). Read: retrieval-only, not generative.

## What it doesn't do

- **No cog-sci stack beyond "hippocampus."** Comprehensive search of Engramme materials (engramme.com, memorious.netlify.app, Harvard IQSS, Harvard Independent, Bloomberg, TFN, TestingCatalog, mapco.ai) returns *exactly one* cog-sci mechanism cited by name: **hippocampus**. No mention of Complementary Learning Systems, neocortex-hippocampus dialogue, replay, schema, schema-fit consolidation, reconsolidation, sleep-dependent consolidation, systems consolidation, generative-replay, engram competition, or selective forgetting.
- **No peer-reviewed memory architecture papers from founders.** Kreiman's 2024-26 publications are dominated by vision/perception/consciousness. Madan's 2023-25 papers are entirely OOD generalization for vision. No memory architecture papers from either as of search date.
- **No published technical architecture.** The "Large Memory Models" abstraction is marketing language. No whitepaper, no arXiv submission, no GitHub repo (no `engramme` GitHub org; Madan's GitHub has no memory-related repos).
- **No selective consolidation framing.** Pitch is "perfect and infinite memory" — the opposite of biological selectivity. Norman-rubric properties (event segmentation, selective encoding/retrieval, temporal contiguity, competition) are conspicuously absent.
- **Verbatim retrieval, not internal-representation storage.** "Retrieves actual memories tied to real events" is the bolt-on RAG shape Norman et al. explicitly contrast against the caddy shape (storing internal representations).

## Seven-layer-stack mapping

| Layer | Coverage | Notes |
|---|---|---|
| Admission Control | ✗ | All ingested content stored; no learned gate |
| Embedding | ✓ | Implied — encrypted vector index over multimodal sources |
| Multi-Graph Memory | unclear | Not described publicly |
| Tiered Storage | unclear | "Petabyte-scale" framing suggests single-tier object store |
| Retrieval | ✓ | Proactive surfacing across integrations is the headline capability |
| Consolidation | ✗ | No async consolidation pipeline described |
| Governance | partial | Encryption per user; deletion mechanics not public |

**Net:** ~2 of 7 layers materially covered, all concentrated on the retrieval-and-storage axis. **Engramme is a personal-data RAG product, architecturally adjacent to [Honcho](./honcho.md), [Cognee](./cognee.md), etc. — not a different category despite the hippocampus branding.**

## Norman-rubric mapping

| Property | Engramme |
|---|---|
| 1. Dynamic memory updating | ✗ — retrieval-only, no reconsolidation mechanism described |
| 2. Event segmentation | ✗ — no surprise-based or boundary-aligned encoding |
| 3. Selective encoding/retrieval | ✗ — admission is exhaustive ingestion; retrieval triggered by proactivity heuristics, not cog-sci-grounded uncertainty signal |
| 4. Temporal contiguity | ✗ — no TCM-style scale-invariant context drift described |
| 5. Competition at retrieval | ✗ — no winner-take-all mechanism described |
| **Score** | **0/5** |

Engramme scores 0/5 on the [norman-rubric](../concept/norman-rubric.md) despite citing "hippocampus" in marketing. The architectural prerequisite Norman endorses (separate-from-context-and-weights memory storing internal representations) is also failed — Engramme stores verbatim content with encryption.

## Where it fails

- **The cog-sci-grounded pitch is marketing, not architecture.** "Similar to how the hippocampus links related memories" is the only cog-sci hook in their public materials. The mechanism set Norman et al. document (CLS, schema-fit, reconsolidation, replay-driven consolidation, temporal contiguity, competition) is absent.
- **The "perfect and infinite memory" pitch is a product failure mode.** Per [feedback_wiki_inclusion_test] and the AJ pushback documented in [memory-caddy](../open-question/memory-caddy.md), human-like memory means selective consolidation, not perfect recall. Engramme's pitch is the opposite of what the cog-sci literature recommends.
- **Construct-validity gap between hippocampal-indexing marketing and verbatim-retrieval implementation.** Hippocampal indexing in neuroscience is a *theory of how the hippocampus stores compressed pointers to cortical patterns*. Engramme's "retrieve actual memories tied to real events" is verbatim text retrieval. These are different things; conflating them is a marketing move that diligent VCs may not catch.
- **No defensible technical moat.** No patents disclosed. No exclusive IP from Harvard tech-transfer publicly cited. Talent moat is Kreiman + Madan + 11 hiring SF roles; no named senior hires from the memory neuroscience world.

## Relevance to the wedge

**Engramme is in a different commercial cell than Kyrja.** They are building a *personal-data memory consumer product* with hippocampus-flavored marketing. Kyrja is building a *cog-sci-grounded memory architecture paired with an LLM* as a sidecar caddy. Different problems, different customers, different architectures.

**However, Engramme will own the "memory startup" mindshare in VC rooms.** Their Bloomberg coverage, $1B target valuation, and Harvard pedigree mean every VC pitching Kyrja will ask "how is this different from Engramme?" The answer:

> *"Engramme is encrypted personal-data search with hippocampus-themed branding. They cite hippocampus once in their public materials and zero mentions of CLS, schema, reconsolidation, replay, temporal contiguity, or competition — the actual cog-sci mechanism set. They store verbatim content and pitch perfect recall. We're building cog-sci-grounded selective memory — the mechanism set Norman et al. (TiCS June 2025) specified as the rubric for human-like episodic memory. Engramme scores 0/5 on that rubric; we're targeting 5/5. Different products, different bets, different categories."*

That pitch holds because Engramme's public materials make it falsifiable: if their architecture were cog-sci-grounded beyond hippocampus marketing, they would say so. They haven't.

**Threat shape:** category-mindshare competitor, not technical competitor. Kyrja loses to Engramme if VCs conflate "AI memory startup" with "the Harvard one with the unicorn valuation." Wins by explicit technical differentiation against the [norman-rubric](../concept/norman-rubric.md).

## Related

- [dong-2025-norman-episodic](../source/dong-2025-norman-episodic.md) — the rubric paper Engramme implicitly invokes but does not engage with
- [norman-rubric](../concept/norman-rubric.md) — concept page with full scoring
- [caddy](../concept/caddy.md) — the architectural pattern Engramme does not implement
- [memory-caddy](../open-question/memory-caddy.md) — competitive landscape framing
- [seven-layer-stack](../concept/seven-layer-stack.md) — coverage analysis above
- [honcho](./honcho.md), [cognee](./cognee.md), [mem0](./mem0.md) — other personal/agent-memory RAG incumbents Engramme is architecturally adjacent to

## Source archive

Public materials surveyed 2026-05-16. No published whitepaper or arXiv submission. Press corpus: [`source/engramme-press-corpus.md`](../source/engramme-press-corpus.md). Key URLs:
- Engramme: https://www.engramme.com
- Memorious (legacy site): https://memorious.netlify.app
- Harvard IQSS announcement: https://www.iq.harvard.edu/news/2025/09/memorious-building-infinite-memory-ai
- Bloomberg: https://www.bloomberg.com/news/articles/2026-04-10/harvard-s-kreiman-seeks-100-million-to-build-ai-memory-tech
- TechFundingNews: https://techfundingnews.com/what-if-you-never-forgot-anything-harvard-spinout-engramme-eyes-1b-valuation-to-build-ai-memory/
- TestingCatalog API beta: https://www.testingcatalog.com/engramme-opens-memory-api-beta-for-app-developers-and-teams/
- Harvard Independent profile: https://harvardindependent.com/harvards-gabriel-kreiman-thinks-artificial-intelligence-can-fix-what-the-brain-gets-wrong/

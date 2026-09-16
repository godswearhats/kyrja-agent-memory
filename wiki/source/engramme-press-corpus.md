---
type: source
name: "Engramme — public materials corpus (no published paper)"
status: timeless
last_ingested: 2026-05-16
sources: []
tags: [engramme, press-corpus, no-published-paper, marketing-materials, harvard-spinout]
---

## Citation

Public materials of Engramme (formerly Memorious), Harvard spinout founded by **Gabriel Kreiman** (CEO) and **Spandan Madan** (CTO). No published whitepaper, no arXiv submission, no GitHub org as of 2026-05-16. This page consolidates the press, blog, and recruiting corpus that constitutes their public technical surface.

## Location

Primary URLs:

- https://www.engramme.com (company site, current)
- https://memorious.netlify.app (legacy site under prior name)
- https://www.iq.harvard.edu/news/2025/09/memorious-building-infinite-memory-ai (Harvard IQSS announcement Sep 2025)
- https://www.bloomberg.com/news/articles/2026-04-10/harvard-s-kreiman-seeks-100-million-to-build-ai-memory-tech (Bloomberg, $100M raise coverage Apr 2026)
- https://techfundingnews.com/what-if-you-never-forgot-anything-harvard-spinout-engramme-eyes-1b-valuation-to-build-ai-memory/ (TFN coverage)
- https://www.testingcatalog.com/engramme-opens-memory-api-beta-for-app-developers-and-teams/ (API beta launch coverage)
- https://harvardindependent.com/harvards-gabriel-kreiman-thinks-artificial-intelligence-can-fix-what-the-brain-gets-wrong/ (Kreiman profile, Apr 2026)
- https://www.engramme.com/careers (hiring posture — 11 SF roles open as of May 2026)
- https://www.engramme.com/team (founders only)
- https://klab.tch.harvard.edu/publications/publications.html (Kreiman lab publications)
- https://scholar.google.com/citations?user=QY5OAIMAAAAJ (Madan Google Scholar)

## Key claims extracted from public corpus

### Product framing

**Verbatim, multiple sources:** *"Large Memory Models"* — proactive lifelong recall positioned as alternative-to-LLMs-for-memory. Three properties cited consistently: *"lifelong storage at petabyte scale, proactive retrieval that surfaces relevant information without a search query, and associative recall that connects information across time and context, similar to how the hippocampus links related memories."*

### Architectural claims

**Verbatim, TestingCatalog API-launch coverage:** *"Large Memory Models, a purpose-built AI architecture that does not follow the transformer paradigm... Where transformers generate plausible outputs from learned patterns, Engramme's models retrieve actual memories tied to real events"* and *"hallucinations are structurally impossible within its memory layer."*

**Our reading:** Retrieval-only architecture, not generative. The "structurally impossible hallucinations" claim implies stored-records-only — i.e., a structured database or encrypted index of verbatim user content, not a learned memory module that produces representations.

### Personal-data integration list

**Verbatim, Harvard IQSS announcement + TFN:** Surfaces a per-user **"memerome"** — a personalised encrypted index across Gmail, Zoom transcripts, photos, texts. Marketing-stated integration list includes: Gmail, Zoom, WhatsApp, Slack, Google Docs, Meta glasses.

### Kreiman's own architectural framing

**Verbatim, Harvard Independent profile April 2026:** *"We're using the kind of algorithms that have been important in neuroscience to model associated memory formation and retrieval in the longer term."* — generic, no specific mechanism named.

### Customer pipeline

**Verbatim, TFN:** *"engaged with over 50 potential users, including older adults with memory loss, project managers, and AI developers."* No named enterprise pilots, no customer logos, no independent benchmarks.

### Cog-sci mechanism citations across all materials

**EXACTLY ONE cog-sci mechanism cited by name across all surveyed materials: hippocampus.**

Conspicuous absences (none cited):
- Complementary Learning Systems (CLS)
- Neocortex-hippocampus dialogue
- Replay / sharp-wave-ripple-driven consolidation
- Schema / schema-fit consolidation
- Reconsolidation
- Sleep-dependent consolidation
- Systems consolidation
- Generative replay
- Engram competition
- Selective forgetting

### Founder publication record

Kreiman 2024-2026 publications (klab.tch.harvard.edu): dominated by **vision, perception, consciousness**. Only memory-relevant paper is Zheng et al. 2024 on "Theta Phase Precession in naturalistic experience" — episodic memory cognitive neuroscience, not memory architecture for AI systems.

Madan 2023-2025 publications: entirely **OOD generalization for vision** — no memory architecture papers.

**Neither founder has a peer-reviewed memory architecture paper for AI systems.**

## Important caveats

- **This corpus is *marketing material*, not peer-reviewed architecture description.** Every claim should be tagged accordingly.
- **The "Large Memory Models" coinage is a marketing label**, not a defined architecture. No technical specification has been published.
- **No public source code or technical paper exists.** Engineering details are not auditable from public materials.
- **No GitHub org under "engramme."** Madan's GitHub has no memory-architecture repos. Means we cannot peer at implementation details even partially.
- **All claims about "what Engramme is technically" should be flagged as inferred-from-marketing**, not architecture-confirmed.

## Relevance to Kyrja

- **The corpus is the basis for [incumbent/engramme](../incumbent/engramme.md).** Every public claim Kyrja makes about Engramme should cite this page.
- **The cog-sci mechanism absence is the load-bearing wedge fact.** Engramme cites hippocampus only; the [norman-rubric](../concept/norman-rubric.md) demands 5 properties. The mechanism gap between Engramme's pitch and our pitch is verifiable from this corpus.

## Audit history

- 2026-05-16 — comprehensive WebFetch + deeper-investigation-agent sweep of all surveyed URLs. Cog-sci citation count confirmed (hippocampus = 1, all others = 0). Re-verify when Engramme publishes a whitepaper or arXiv preprint, whichever comes first.

## Archive location

URLs listed above. Stable archives not preserved locally (marketing corpora drift). Re-fetch from primary URLs for re-verification. Status_current_as_of dates on related pages should be re-checked monthly given the active fundraise and product-launch timeline.

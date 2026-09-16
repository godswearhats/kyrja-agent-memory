---
type: source
name: "Lampinen et al. 2025 — Latent learning: episodic memory complements parametric learning"
status: timeless
last_ingested: 2026-05-16
sources: []
tags: [deepmind-to-anthropic, cls-framing, lampinen, oracle-rag, anthropic-threat-signal, stub]
---

## Citation

Lampinen, A.K. et al. (2025). *Latent learning: episodic memory complements parametric learning.* arXiv:2509.16189, September 2025. Originally Google DeepMind affiliation; **Lampinen has subsequently moved to Anthropic** (per the [Project Astra investigation 2026-05-16] documented in this wiki's log).

`[STUB]` — verbatim read pending.

## Location

- arXiv: https://arxiv.org/abs/2509.16189
- Lampinen's site: https://lampinen.github.io/ (verified Anthropic affiliation)

## Key claims (per Project Astra investigation summary)

### CLS-explicit framing in DeepMind output

**Per Astra investigation:** Paper explicitly invokes CLS framework ("hippocampus as a memory index") in its theoretical framing. This makes it one of the most CLS-explicit memory papers from a frontier lab in 2025.

**Our restatement:** `[ASSERTED]` via the Project Astra agent investigation, not yet verified verbatim. CLS framing in a DeepMind paper is a strong signal that the frontier-lab neuro-grounded crew engages with our cog-sci playbook.

### Architecture is oracle RAG, not novel memory module

**Per Astra investigation:** Despite CLS-explicit framing, the implementation is "an oracle RAG prepended to context" on a vanilla decoder transformer — no custom memory module, no separate trainable component.

**Our restatement:** `[ASSERTED]` via the Project Astra agent investigation. The construct-validity gap between CLS framing and bolt-on-RAG implementation is the same pattern we see across the field. **Lampinen's paper shows that even CLS-explicit research output from DeepMind shipped as bolt-on RAG, not as a novel memory architecture.** Consistent with the broader post-Norman-rubric gap finding.

### Lampinen's move to Anthropic is a frontier-lab-talent signal

**Per Astra investigation:** Lampinen left DeepMind for Anthropic Institute (March 2026 timeframe). This is the most explicitly CLS-framed memory researcher at DeepMind defecting to Anthropic.

**Our restatement:** `[ASSERTED]` Implications:
- DeepMind's internal CLS-memory threat is reduced
- Anthropic's threat is increased — they now have CLS-explicit talent in addition to Auto Dream (REM-inspired consolidation feature, March 2026)
- Combined Anthropic signals: CLS-explicit memory paper author + REM-inspired consolidation feature + Lampinen on-staff = the most concerning frontier-lab moat-risk

## Important caveats

- **This page is a STUB.** Verbatim read pending. All architecture claims are from secondary-source agent investigation, not from direct paper reading.
- **The CLS framing in the paper is *theoretical*; the implementation is bolt-on RAG.** Do not over-read the framing as evidence of a CLS-shaped architecture.
- **Lampinen-at-Anthropic does not mean Anthropic is building our caddy.** It means they have one researcher with CLS-explicit framing on staff. The leap from "one researcher" to "shipping a CLS-grounded caddy product" is large.

## Relevance to Kyrja

- **Frontier-lab moat-risk update.** Anthropic + Lampinen + Auto Dream is the worst-case frontier-lab combination for our wedge. They have the framing, the feature, and now the talent.
- **DeepMind moat-risk slight reduction.** Lampinen's departure reduces DeepMind's near-term CLS-memory threat — though Wayne, Lillicrap, Kirkpatrick, Kumaran all remain at DeepMind.
- **Construct-validity case study.** The paper is an example of "CLS-framed paper that ships as bolt-on RAG implementation" — exactly the gap Kyrja is positioning against.

## Audit history

- 2026-05-16 — STUB created based on Project Astra agent investigation findings. Verbatim read pending.

## Archive location

arXiv:2509.16189. Verbatim read deferred; will pull PDF when this becomes load-bearing for a specific claim or decision.

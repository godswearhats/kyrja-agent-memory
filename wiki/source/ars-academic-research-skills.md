---
type: source
name: "Wu — Academic Research Skills (ARS)"
status: timeless
last_ingested: 2026-05-26
sources: []
tags: [methodology, borrowed-mechanism]
---

## Citation

Cheng-I Wu (吳政宜). *Academic Research Skills (ARS)* — a Claude Code skill suite
for the academic research pipeline (research → write → review → integrity →
publish). v3.9.4.2 (read 2026-05-26). Licence: CC BY-NC 4.0. Not a paper; a
software/methodology repository.

## Location

- https://github.com/Imbad0202/academic-research-skills (canonical)
- Transient local clone at `ars` (container-only, not durable — fetch
  from the GitHub URL).

## Key claims (with our restatements)

### 7-mode AI-research failure taxonomy

**Paper:** ARS's `academic-pipeline/references/ai_research_failure_modes.md`
enumerates seven ways AI-assisted research silently fails: (1) implementation bug
passing self-review, (2) hallucinated citation, (3) hallucinated experimental
result, (4) shortcut reliance, (5) bug reframed as novel insight, (6) methodology
fabrication, (7) early-stage frame-lock. ARS attributes the taxonomy to Lu et al.
(2026), *Nature* 651:914–919, "Towards end-to-end automation of AI research"
`[ASSERTED]`.

**Our restatement:** the failures that *look like competent work* — a result from
a silent bug reads identically to a real one — are the class our falsifiability
discipline doesn't systematically catch. **Provenance caveat:** the Lu et al.
primary is **not independently verified** by us; we read only ARS's summary, and
the surrounding citation set is future-dated. We borrow the *discipline*, not the
paper's authority. Verifying (or falsifying) the Lu et al. reference is an open
follow-up.

### Concession Threshold Protocol (anti-sycophancy)

**Paper:** `deep-research/agents/devils_advocate_agent.md` — a critic agent scores
each rebuttal 1–5 and concedes only at ≥4 (rebuttal addresses the core with new
evidence/airtight logic). Rules: pushback is not evidence; no consecutive
concessions; if >50% of findings conceded, pause and re-raise the bar. Origin note:
"DA agents concede attacks faster than they launch them — training rewards
conversational harmony over rigour" `[ASSERTED]`.

**Our restatement:** operationalised as a Nils self-rule — see
`feedback_concession_discipline` in project memory.

### Ground-truth isolation pattern

**Paper:** `shared/ground_truth_isolation_pattern.md` — a three-layer firewall
(raw → verified → ground-truth), one-way flow; an agent that sees the answer-key
while generating optimises toward surface features of the rubric (reward hacking).
ARS credits Anthropic's automated-w2s-researcher (2026) three-tier sandbox as prior
art `[ASSERTED]`.

**Our restatement:** information-flow control / taint-tracking. Generation runs on
raw/verified only; ground-truth enters in a *separate invocation* (separate
instructions are insufficient).

### Frame-lock and shared-frame verification

**Paper:** ARS v3.0 README — a verifier sharing the generator's cognitive frame
attacks arguments but never premises; ARS traces a 31% citation-error rate in a
v2.7 stress test to the verifying and generating model sharing one frame
`[ASSERTED]`. Their structural fix: route verification to a different model.

**Our restatement:** the rationale for using genuinely independent readers
(external-Claude, Ollama, Maren, Anders) on load-bearing conclusions — I cannot
fully audit my own analysis, being frame-locked by construction.

## Important caveats

- **Future-dated, unverified citations.** ARS cites several 2026 papers (Lu et al.
  *Nature* 651:914; Zhao et al. arXiv:2605.07723) we have not read. Treat all
  attributions here as ARS's claims, not verified primaries.
- **CC BY-NC 4.0.** Mechanisms are borrowed and re-expressed in our own idiom —
  *not vendored*. Copying ARS code into anything commercial (Eira's track) would
  engage the non-commercial clause.
- **Scope mismatch.** Most of ARS (APA/LaTeX paper writing, simulated peer review,
  citation-format conversion) targets traditional academic publishing and does not
  apply to Kyrja. Only the integrity / epistemic-hygiene mechanisms above were
  borrowed.

## Relevance to Kyrja

- Sole provenance anchor for [decision/research-integrity-checks](../decision/research-integrity-checks.md).
- Source for the `feedback_concession_discipline` memory note.
- Complements [concept/evidence-anchoring](../concept/evidence-anchoring.md): ARS
  attacks *result*-integrity, evidence-anchoring attacks *claim*-provenance.

## Audit history

Read verbatim 2026-05-26 (Nils/indigo): README (through Licence), plus the four
crown-jewel files — `ai_research_failure_modes.md`, `devils_advocate_agent.md`,
`ground_truth_isolation_pattern.md`, `collaboration_depth_rubric.md`. The
Collaboration Depth Rubric was evaluated and **rejected** (construct validity: it
measures pedagogical learning outcomes, not research quality).

## Archive location

GitHub repository (above) is canonical; it is not a paper, so nothing lands in
library/papers. The transient clone at
`ars` should not be relied on.

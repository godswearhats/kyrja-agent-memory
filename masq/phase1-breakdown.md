# MASQ Paper — Phase 1 Work Breakdown

*Written 2026-06-07 (Nils/indigo). Input: Phase 0 survey + team-data probe (both passed; kill criterion clean — see reads/ for verbatim positioning notes). Budget assumption: ~6–8 hrs/wk total, skill-track cut first on blown weeks. Pick up here next session.*

## The claim we are building toward

> MASQ is the first benchmark to make **multi-party shared-workspace memory attribution** a scored, primary task: who said/decided X, in which team/project context, under deliberate cross-team vocabulary overlap. Dual corpus — controlled synthetic (regeneratable, contamination-proof) + one real multi-agent ecology (honestly characterized as all-Claude/one-user). Deterministic attribution scoring.

Positioning anchors (verbatim, banked in `reads/`): LongMemEval = dyadic by construction (§3.1; multi-party is a discarded failure mode §A.1); MemoryArena = single agent 𝒜/ℰ/ℳ (§3.2); ATM-Bench = first-person single-owner life-log (§3.1, §B.3). No occupied neighbor.

## Workstream A — v1 punch list (paper-blocking)

| # | Item | Size | Notes |
|---|------|------|-------|
| A1 | **Consolidate canonical repo** from slate (frozen core) + red (tier-1 additions); **remove kyrja_* retrievers** (AJ decision 2026-06-07: independence + not a built system) | 1 session | Single source of truth; archive red's .scratch (231M qdrant store) separately |
| A2 | **Unify reader LLM** and re-run all retrievers under it | 2–3 overnight GPU/ollama runs | gemma3:4b is a known ceiling (0.504 with oracle); qwen3:14b run exists but incomplete (483/~497 lines) and judge-unscored. Pick one, justify, re-run everything |
| A3 | **Integrate judge into harness** (currently post-hoc `llm_judge_scores.py`); pin judge model + prompts; **make attribution fields deterministic exact-match** (speaker/team are closed sets — no judge needed there) | 1–2 sessions | SWE-bench lesson 3 + MemoryArena-style decision-grounded scoring. LLM-judge stays only for open-ended answer text |
| A4 | **Gold-answer triage**: 12 oracle-zero queries, near-zero person-identification queries (Q002 etc.), rejection-type hallucination failure | 1–2 sessions | SWE-bench Verified lesson: human-verify every gold answer is uniquely determinable and not lexically shortcut-able. Each query gets a verdict: data bug (fix) vs hard case (keep, document) |
| A5 | **Compound filtering**: implement tiered-cascade fallback or document binary fallback as an intentional limitation | 1 session | Existing tuning notes in red's copy |
| A6 | **Reproducibility**: parametrize hardcoded service IPs (192.168.109.*), fresh-clone end-to-end run, document generator + seeds | 1 session | |
| A7 | **Regeneratable private split**: fresh-seed generation path documented + one held-out split actually generated | 1 session | Turns synthetic provenance into a contamination-proof strength — a differentiator nobody in the memory space has |

Estimated: **4–6 weeks** at budget. A1 → (A2 ∥ A4) → A3 → A5–A7. Sibling leverage: red owns the most-developed copy (mem0/chromadb integrations) — candidate to carry A2 re-runs; AJ to decide whether to brief red.

## Workstream B — v2 real corpus (can lag A; first results can land in the paper as the "ecological condition")

| # | Item | Size | Notes |
|---|------|------|-------|
| B1 | **Scrub audit at scale** — the Phase 0 estimate rests on a 5-session sample; audit ≥100 sessions before trusting prevalence numbers | 2 sessions | Adopt ATM-Bench §A.1 pipeline shape: automated screening → LLM paraphrase (removes linguistic fingerprints) → synthetic PII injection → manual spot-check |
| B2 | **Filter usable subset** via Locke's indexes (target ~200–300 top-level conversation-dominated sessions, 100–150M tokens) | 1 session | Criteria drafted in Phase 0 probe |
| B3 | **Needle design** — inject ground-truth facts/decisions/attributions at known turns. **Pre-registered control: vary author and recency independently** in conflicting-needle queries (ATM-Bench's MUT shows recency is a strong prior; without this control, authorship effects are confounded) | 2 sessions | Design doc before code |
| B4 | **Pilot**: 10–20 scrubbed sessions, ~50 needles, run the v1 retriever suite; decide go/no-go on full v2 | 1–2 sessions + GPU | Pre-register: what ranking-agreement between synthetic and real corpora would mean (agreement = synthetic validity evidence; disagreement = the real corpus is load-bearing) |

## Workstream C — paper (starts when A locks; blog posts ride alongside)

- C1 Positioning/related-work section from `reads/` notes (the three verbatim reads + Phase 0 survey table). Verify any vendor numbers against primary sources before citing — survey agent flagged its own secondary sourcing (and mis-cited ATM-Bench's arXiv ID; trust nothing secondhand).
- C2 Results + honest-limitations section (synthetic provenance, one-ecology skew, single-human-user).
- C3 Target: workshop submission + arXiv preprint; blog series carved from the same material.

## Standing guards

- Weekly cap 6–8 hrs; blown week → cut skill track (nanoGPT), never sleep/family. 4-week review checkpoints.
- Kyrja retrievers stay OUT. Independence is the brand.
- Every benchmark claim in the paper traces to a verbatim primary-source quote (reads/ discipline).

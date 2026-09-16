# MemoryArena (arXiv 2602.16313) — verbatim positioning notes for MASQ

*Read 2026-06-07 (Nils, via verbatim-quote extraction; 100% of paper text covered, exhaustive keyword sweep). He, Wang, …, McAuley, Choi, Pentland. Feb 2026.*

## Party structure: single agent, formally

- §3.2: one agent 𝒜, one environment ℰ, one memory ℳ: "we equip the agent 𝒜 with a persistent memory system ℳ, which stores information across subtask sessions and is initialized as empty at the beginning of each evaluation episode." §4.1: "GPT-5.1-mini as the task agent" across all conditions.
- Keyword sweep: multi-agent / speaker / attribution / who said / source memory / shared workspace / provenance = **0 hits**. "Participants/members/travelers" = passive personas in the Group Travel task only.

## Task design

- Interdependence (§3.2): "subtasks are executed sequentially… later subtasks may depend on information acquired in earlier ones (e.g., the version of the camera body bought before must be known when buying lens)."
- §2: "MemoryArena enforces *cross-task causal dependence* and evaluates memory through *end-to-end sequential task completion*."
- Four families (§3.1): Bundled Web Shopping; Progressive Web Search (256 tasks, BrowseComp-Plus, "strict causal ordering among subqueries"); Group Travel (5–8 incrementally joining travelers, JOIN/RELATION constraints — e.g. "I want to have dinner with Rebecca on the second day"); Sequential Formal Reasoning (40 math + 20 physics, lemma chains).
- **Closest neighbor = Group Travel personas**, but they are *constraints the single agent must satisfy*, never parties whose utterances are attributed. Differentiation line for our paper: MemoryArena tracks *whose preference a constraint belongs to for plan-satisfaction*; MASQ tests *attributing utterances/decisions to speakers across team contexts under vocabulary overlap*.

## Scoring — BORROW THIS (decision-grounded)

- **PS** (§4.2, Eq. 5): fraction of ordered subtasks passed, averaged over tasks. **sPS** (§4.3): partial credit per constraint. **SR**: all-or-nothing on the *final downstream decision* ("a task is successful if the final bundle or plan satisfies all group members… success is determined by the correctness of the final subtask"). **SR@k** (§4.4): survival at subtask depth k.

## Citable numbers (the recall-benchmarks-under-measure evidence)

- Abstract: "agents with near-saturated performance on existing long-context memory benchmarks like LoCoMo perform poorly in our agentic setting."
- Table 3 / §4.3: near-zero SR — Group Travel SR/PS = **0.00 across all methods**; Bundled Shopping avg SR ≈ 0.02. "augmenting GPT-5-mini with external memory or RAG does not consistently outperform using the model's full long-context history alone." (Note: LoCoMo is NOT re-run in the paper; the claim rests on the absolute floor here vs reported saturation there.)

## Kill-criterion verdict

**No multiple acting agents, no speaker identity, no attribution, no shared multi-party store.** Clean.

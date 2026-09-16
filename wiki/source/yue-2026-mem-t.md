---
type: source
name: "Yue et al. 2026 — Mem-T: tree-backprop + hindsight credit; the first content-free densifier"
status: timeless
last_ingested: 2026-06-12
sources: []
tags: [rl-memory, grpo, tree-search, credit-assignment, hindsight-credit, structural-credit, full-read, latent-densifier-candidate]
---

> **STATUS: FULL-TEXT READ COMPLETE (2026-06-12, Nils).** Verbatim read of the arXiv full text (main body + appendices A–C incl. all tool/prompt schemas), per [[feedback_load_bearing_sources]]. Page created directly at full-read status. Read as a Rock-3 follow-up: does the advertised densifier survive a store an LM judge cannot read?

## Citation

Yanwei Yue, Boci Peng, Xuanbo Fan, Jiaxin Guo, Qiankun Li, Yan Zhang. *Mem-T: Densifying Rewards for Long-Horizon Memory Agents.* arXiv:2601.23014v2 (09 Mar 2026). Peking University / Nanyang Technological University.

## Location

- https://arxiv.org/abs/2601.23014
- Code: https://github.com/yanweiyue/Mem-T — model: https://huggingface.co/EdwinYue/Mem-T-4B
- Local archive: pending download to `kyrja/library/papers/`

## What the system actually is (verified)

- **Hierarchical text store, four modules** (§3.1): working summary, factual memory, experiential memory, raw archive. Facts/experiences carry validity time windows `[t_start, t_end]` in the schema. Formation actions {CrtFact, CrtExp, CrtRaw, UpdWork}; evolution actions {ADD, UPDATE, DELETE, IGNORE}; retrieval = multi-turn Search(store, key, topk) + Finish, capped at 6 steps at inference.
- **Two training tracks, NOT joint end-to-end RL** — the abstract's "joint optimization" framing deflates on read:
  1. **Retrieval = real tree RL (MoT-GRPO, §3.2).** Per query: G=3 trees, seed rollout each, then M expansion rounds branching from N_v=3 sampled pivot nodes (max depth 4). Node reward (Eq. 10): `R(v) = 𝕀_fmt · (α·Evid(v) + Perform(v))` where **Perform(leaf) = answer F1 and Perform(internal) = mean over children** — dense per-step signal manufactured purely from branching + outcomes. Dual-scale advantage: intra-tree + inter-tree z-scores (Eq. 11–13), PPO-clipped GRPO objective.
  2. **Construction = filtered SFT, not RL (§3.3 "Policy Refinement").** Hindsight scores rank memory-write actions; top 50% per operation category are kept; the policy is trained by **plain log-likelihood on the survivors** (Eq. 18; LLaMA-Factory, 200 steps, 10k-operation dataset). Rejection-sampling distillation — the long-horizon write problem is sidestepped, not solved by RL.
- **Hindsight credit (Eq. 16–17) — the load-bearing mechanism.** A write action's score aggregates leaf advantages weighted by `ϱ = 𝕀(source turns ∩ GT evidence turns ≠ ∅) + λ·𝕀(memory item ∈ leaf's retrieval trace)`, λ=0.1. **Both gates are content-free**: the evidence-alignment gate is set intersection on provenance (turn IDs); the retrieval-trace gate is pure traceability. The paper notes the trace gate alone carries the mechanism when no GT evidence exists.
- **Training data:** LoCoMo 1:1:8 split per Memory-R1 convention → effectively ~1 conversation of training signal for retrieval RL (200 steps), plus the 10k-op construction set. Qwen3-4B/8B backbones, BGE-M3 embeddings.

## Headline results (verified)

- **LoCoMo (Table 2, Qwen3-4B):** untrained Mem-T 49.38 F1 (already beats Mem0 43.71, GAM-on-Qwen 30.17) → vanilla GRPO 53.56 → MoT-GRPO 58.65. **Marginal value of the tree machinery over flat GRPO: +5.09.** Architecture does most of the lifting; densification is real but moderate.
- **OOD transfer (Table 3):** trained on LoCoMo only — HotpotQA-56k 66.35 (vs Mem-α 58.80), LongMemEval-S 65.80, NarrativeQA 30.29; avg +6.45 over best baseline.
- **Ablations (Table 4):** w/o retrieval opt −5.28; w/o construction opt −3.29; **w/o inter-tree advantage −4.56 > w/o intra-tree −1.70** — the global GRPO-style normalization carries more than the tree-local comparison, slightly undercutting the "tree-local credit is the magic" story (the dense node rewards still come from tree structure).
- Efficiency: Pareto-dominant vs GAM (−19.9–24.5% inference tokens/query). Sensitivity: retrieval steps plateau at 6; G plateaus at 3.

## The Rock-3 reading — first candidate answer to "which densifier survives an illegible store?"

**No LM judge anywhere in the reward.** Perform = F1/accuracy at leaves; Evid = proportion of GT evidence retrieved; gates = provenance set-intersections. Unlike Mem-α's per-action judge (which must read entry contents), nothing in Mem-T's signal reads what's *in* the store. A latent slot can carry provenance tags (source-turn IDs) exactly as a text entry does → **the credit signal ports to a store an LM judge cannot read.** This is the first such densifier in the cluster's lineage.

Three honest limits on the port:

1. **The optimizer doesn't port where it matters.** Construction is trained by token-level SFT on kept actions — you cannot behavior-clone a continuous latent write by token likelihood. The hindsight *score* ports; it would need a different optimizer (policy gradient / weighted regression).
2. **The RL only ever runs at short horizon** (≤6 retrieval steps). The hundreds-of-interleaved-writes regime — the actual Rock-3 horizon — is handled by the offline filter, consistent with the cluster pattern: nobody trains sparse long-horizon RL on the write side.
3. **The evidence gate is privileged supervision** (annotated evidence locations, same as R2's session attribution); the GT-free fallback is the trace gate alone, untested in isolation.

Cluster table extension (cf. [yu-2026-agemem](./yu-2026-agemem.md) for the four-paper table): Mem-T's densifier = **outcome-tree backprop (retrieval) + provenance-gated hindsight filter (construction)**; horizon ≤6 steps RL / offline SFT for writes; frozen-counterpart question moot (two separate training pipelines).

## Other findings relevant to Kyrja

- **Supersession sightings** ([fact-supersession](../concept/fact-supersession.md)): DeleteItemTool fires only when an item is "explicitly negated or wrong" — R2's monotonicity rule reappearing as prompt scaffolding; UpdateItemTool instructs "must save the original time information of previously items in the document" — the provenance-in-content anti-pattern AgeMem exhibited. Validity windows in the schema are the cleaner half.
- **Case study (Fig. 6):** untrained baseline misreads ADD-vs-UPDATE and overwrites unrelated entries — the refinement-misread-as-supersession failure again, fixed by training.

## Important caveats

- Text store + tool calls; nothing latent. The latent-port argument above is our extrapolation, not paper-claimed.
- Memory-R1 baseline numbers are copied from its paper (not open-source), different backbone (8B vs Qwen3-4B) — cross-row comparisons in Table 2 are indicative only.
- LoCoMo conversations average only ~16k tokens — the intro's "~500 turns within million-token contexts" motivation outstrips the actual training domain.
- "10k memory operations" construction set: curation details thin; rank-based top-50% filter threshold unexamined.

## Relevance to Kyrja

- Updates [caddy § Rock 3](../concept/caddy.md): the latent-variant question moves from "open" to "candidate mechanism exists (content-free structural credit), text-only, short-horizon" — see the 2026-06-12 paragraph there.
- Convergent with [TreeMem](./mao-2026-treemem.md) (independent group, same branch-and-average family, different decomposition axis).
- Borrowable ([[feedback_borrow_not_adopt]]): provenance-tagging memory entries with source-turn IDs as the substrate for write-credit; hindsight top-k filtering as a cheap write-policy bootstrapping step before RL.

## Audit history

- 2026-06-12 — page created at **full-read** status by Nils (indigo); abstract's "joint optimization of memory construction and retrieval" deflated to RL-for-retrieval + filtered-SFT-for-construction on inspection of §3.3/Eq. 18.

## Archive location

arXiv:2601.23014v2 (HTML full text read 2026-06-12). PDF download to `kyrja/library/papers/` pending.

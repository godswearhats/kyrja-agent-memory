---
type: source
name: "Pan, Hahami, Zhang & Sompolinsky 2025 — Memorization and Knowledge Injection in Gated LLMs"
status: timeless
last_ingested: 2026-05-16
sources: []
tags: [cls-grounded, in-weights-memory, gated-lora, sompolinsky-lab, harvard-cbs, mega, substrate-paradigm]
---

## Citation

Pan, X., Hahami, E., Zhang, Z. & Sompolinsky, H. (2025). *Memorization and Knowledge Injection in Gated LLMs.* arXiv:2504.21239, April 30 2025. Under review.

Affiliations: (1) Center for Brain Science, Harvard University; (2) Harvard University; (3) Kempner Institute, Harvard University; (4) Edmond and Lily Safra Center for Brain Sciences, Hebrew University Jerusalem (Sompolinsky's primary appointment).

## Location

- arXiv: https://arxiv.org/abs/2504.21239
- Local archive: [`pan-2025-mega.pdf`](../../../research/library/papers/pan-2025-mega.pdf) (27 pages)

## Key claims (with our restatements)

### Architecture — gated LoRA per memory

**Paper (§3.3):** Each new memory `D_i` is stored as a dedicated LoRA adapter `{A_i^l, B_i^l}` fine-tuned on the single sample, plus a "context key" `K_i = f(D_i)` (embedding of the sample computed from the input to the final MLP layer of the base model). At inference, softmax gating over context-key similarities activates relevant LoRAs: `g_i = softmax(β·f(q)^T·K)`, and inference weights are the weighted sum `Θ_infer = W_PT + Σ_i g_i·A_i^l·B_i^l`. Base model: Llama-3.1-8B-Instruct. LoRA rank r=128, all MLP layers targeted.

**Our restatement:** `[ASSERTED]` MEGa is **in-weights CLS-grounded memory**: each memory becomes a learned modification of the LLM's weights, gated by similarity-based retrieval. Per the [memory-consumer-axis](../concept/memory-consumer-axis.md), this is memory-for-the-model (LoRA modulates internal computation); per the [substrate-depth-ladder](../concept/consolidation-channel.md), this sits at rung 4-5 (weight modification with explicit gating). Architecturally **NOT a [caddy](../concept/caddy.md)** — the memory lives inside the LLM as adapter weights, not in a separate sidecar module.

### CLS framing made explicit

**Paper (Discussion §5):** *"The gating systems and associated LoRA weights correspond to the fast learner ('hippocampus') while the rehearsal-triggered fine-tuning of the base weights correspond to the slow learner ('cortex') (McClelland et al., 2020). The gating operation in MEGa is also reminiscent of the indexing theory of hippocampal memory (Teyler & DiScenna, 1986)."*

**Our restatement:** `[ASSERTED]` MEGa is one of the most explicitly CLS-framed memory architectures in the recent LLM-augmentation literature. Same theoretical playbook as Kyrja's caddy — different architectural choice. Useful as the foil: "MEGa shows CLS-grounded in-weights memory works at small scale; Kyrja proposes CLS-grounded sidecar memory because in-weights scales linearly in parameters and requires joint training."

### Recall, QA, and iRAG performance

**Paper (Table 1):**

| Method | Fictional Character QA Acc | Wiki Events QA Acc | Fictional Character Recall cos | Wiki Events Recall cos | MMLU |
|---|---|---|---|---|---|
| Base Llama-3.1-8B | 0.13% | 8.17% | 0.587 | 0.665 | 62.56% |
| RAG | 82.57% | 88.83% | 0.881 | 0.889 | 62.56 |
| MEGa | 72.53% | 78.03% | **0.901** | **0.921** | **61.75** |
| iRAG (MEGa+recall) | 80.67% | 84.70% | 0.901 | 0.921 | 61.75 |
| Full fine-tuning | 12.60% | 17.90% | 0.554 | 0.526 | 55.65 |
| LoRA fine-tuning | 0.80% | 0.53% | 0.485 | 0.243 | 47.94 |

**Our restatement:** `[ASSERTED]` paper-reported. **Construct-validity:** these are 50-sample datasets evaluated across 20 random partitions (mean ± std). MEGa beats RAG on recall (`recall cos` measures cosine similarity of generated text to original sample). RAG still wins on QA; iRAG closes the gap. MMLU retention is the headline: MEGa preserves base-model capability while other continual-fine-tuning methods catastrophically forget. **Scale caveat:** 50 samples is academic-scale. Linear parameter growth (one LoRA per sample) at production scale is the published limitation.

### Mitigates catastrophic forgetting via gated isolation

**Paper (§4.1, Figure 2):** MEGa's forgetting curve (recall accuracy vs number of stored memories) is "almost flat" out to 50 samples, comparable to full-parameter batch learning (the practical ceiling). All other continual learning baselines (Full, Full+L2, Full+EWC, LoRA, LoRA+L2) show severe degradation.

**Our restatement:** `[ASSERTED]` Per-memory isolation via dedicated LoRA + softmax gating is empirically effective at preventing catastrophic interference. This is a real architectural insight that Kyrja can borrow if it turns out we want partial in-weights consolidation (the slow-cortex side of the CLS pipeline). The structural reason is the same as why caddy-per-scope works: anatomical separation of memory traces prevents interference.

### Future work explicitly maps to consolidation channel

**Paper (Discussion §5):** *"A promising future direction is to gradually distill LoRA weights into base model weights. This entails a rehearsal process in which gating units are activated repeatedly, generating a spontaneous reconstruction of one or few stored memories at a time, and then triggering a slow fine-tuning of the base model... Incorporating rehearsal-based memory transfer will make the model similar to the complementary memory systems hypothesis for human long-term memory."*

**Our restatement:** `[ASSERTED]` MEGa's stated future work is exactly the consolidation channel Kyrja has been designing — plus the rehearsal-driven distillation pattern Spens & Burgess have already implemented at academic scale. The Sompolinsky group is heading toward the Spens & Burgess design from the in-weights side; we head toward it from the sidecar side. Convergent design suggests the cog-sci framing is load-bearing for both groups, but the architectural disagreement (in-weights vs sidecar) remains.

## Important caveats

- **Architectural class: in-weights, NOT caddy.** Each memory modifies the LLM's effective weights via gated LoRA. Cannot be transferred to a different base model without re-training. The opposite architectural choice from Kyrja's sidecar caddy.
- **Linear parameter growth is the published scaling limit.** Acknowledged verbatim: *"One limitation of MEGa is that its parameter count grows linearly with the number of training samples, as each new memory requires additional LoRA adapter."*
- **Pre-segmented samples.** Each memory is an atomic 200-300-word paragraph. No continuous-stream encoding, no event-boundary detection. Fails Norman rubric property 2.
- **No selective admission.** Every sample becomes a LoRA — no gate decides what's worth encoding. Fails Norman rubric property 3 (encoding side).
- **No reconsolidation.** Memories are stored once; updating requires re-fine-tuning. Acknowledged future work: *"a new memory might update a similar existing memory rather than being stored as a distinct event."* Fails Norman rubric property 1 unless you count the future-work intent.
- **No temporal contiguity.** No temporal context binding in retrieval. Fails Norman rubric property 4.
- **Competition partial.** Softmax-gating concentrates on top match but is not winner-take-all (β controls spread; β=1 in main experiments). Partial credit on Norman rubric property 5.
- **Scoring against the [norman-rubric](../concept/norman-rubric.md): 1.5/5** — comparable to Titans and Spens & Burgess, despite different architectural class.
- **Academic only, no spinoff signal.** Acknowledgments cite Swartz Foundation, Kempner Institute, ONR grant, Gatsby Charitable Foundation — research funders, not VC. Sompolinsky lab is theoretical-neuroscience-shaped, not productisation-shaped. Status: watch flag, not active threat.

## Relevance to Kyrja

- **Anchors [substrate-paradigms](../concept/substrate-paradigms.md)** as the cog-sci-grounded P1 in-weights variant. Per-memory LoRA gating is a real architectural class distinct from Titans/Hope (which use shared MLP memory module) and from Memory³ (which uses sparsified KV cache).
- **Architectural foil for the [caddy](../concept/caddy.md) sidecar pitch.** The contrast — "in-weights CLS that scales linearly in parameters" vs "sidecar CLS with hot-swappable scope" — is the cleanest competitive frame we have on the cog-sci-grounded axis.
- **Validates the CLS framing as productively shared across multiple research groups.** Sompolinsky lab, Burgess lab, and Kyrja are all working from the same cog-sci playbook — different architectural commitments, same theoretical commitments.
- **Updates [memory-caddy](../open-question/memory-caddy.md)** with another 1.5/5-on-Norman-rubric data point that confirms the cell is empirically open.
- **Updates [consolidation-channel](../concept/consolidation-channel.md)** with MEGa's stated future-work direction (rehearsal-driven distillation of LoRA into base weights) as a concrete operator design for the slow-cortex side.

## Audit history

- 2026-05-16 — read pages 1-10 verbatim (abstract, intro, related work, methods, results overview, discussion intro). Pages 11-27 (appendices, detailed ablations, full references) NOT read at verbatim level. Headline architecture and result claims accurate; appendix-level construct-validity details not verified.

## Archive location

arXiv:2504.21239. Local PDF: [`pan-2025-mega.pdf`](../../../research/library/papers/pan-2025-mega.pdf) (27 pages).

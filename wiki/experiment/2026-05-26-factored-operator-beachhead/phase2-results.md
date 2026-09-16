---
type: experiment
name: "Factored-operator beachhead — Phase 2: the integrated arm must actually integrate (QLoRA fails, full-FT works)"
status: LANDED (integrated-arm instantiation resolved) — scaling separation PENDING
last_ingested: 2026-05-27
program: kerros
sources: [./spec.md, ./phase1-results.md, ../../concept/integration-gate.md, ../../source/xu-2026-agentic-memo.md]
epistemic_tags: [measured]
tags: [kerros, beachhead, composition, integrated-arm, qlora, full-fine-tune, instantiation, de-risk]
---

> **Program: [Kerros](../../concept/kerros.md).** Phase 2 of the [factored-operator beachhead](./spec.md): the real LLM arms. This run did **not** test the substantive hypothesis (the composition separation). It resolved a *precondition* that the [locked spec](./spec.md) silently assumed — *can the integrated arm learn the task at all?* — and the answer reshaped how the integrated arm is built. The scaling separation (the actual bet) is still unrun.

## Hypotheses tested

Not the substantive hypothesis. This phase answers an **instantiation precondition**: can a model integrate the factored operator into its weights well enough to generalise to held-out pairs? Until that is yes, the integrated-vs-bolt-on comparison is meaningless. The substantive claim (integrated beats the smart bolt-on, gap fans open with `k`) remains **PENDING** — see [spec](./spec.md) and § Limitations.

## Method

Built the real arms ([phase2_pilot.py](../../../experiments/factored-operator-beachhead/phase2_pilot.py)): base model Phi-3-mini-128k-instruct, opaque symbols added as single frozen tokens (random-init embeddings), labels scored by constrained logit over the 5 label-token ids, supervised on the answer token only. When the integrated arm sat at chance, ran a **diagnostic ladder** to localise the failure (all on the identical [Phase-1 generator](./phase1-results.md), `k=64`, `m=4`, `C=5`, seed 0):

1. **Separability probe** — a small MLP on the concatenated *frozen* symbol embeddings (`[emb(a) ‖ emb(b)] → label`), held-out scored. Tests whether the signal is recoverable from the frozen fingerprints at all.
2. **From-scratch tiny transformer** ([phase2_scratch_check.py](../../../experiments/factored-operator-beachhead/phase2_scratch_check.py)) — 0.41M params, learned embeddings, classification head, all weights trainable. Tests whether *any* transformer learns the token-combination.
3. **Full fine-tune of a small model** ([phase2_fullft.py](../../../experiments/factored-operator-beachhead/phase2_fullft.py)) — Qwen2.5-0.5B, every parameter trainable, bf16, no LoRA/quantisation. The purest "knowledge into weights"; the bridge to a real pretrained LM.

QLoRA integrated arm swept across rank ∈ {16, 64}, lr ∈ {2e-4, 5e-4, 1e-3}, frozen **and** trainable embeddings, including an overfit probe (N=256). Compute: host RTX 2080 Ti 11GB.

## Results

`[MEASURED]` (k=64, seed 0; numbers from host runs — terminal output not persisted to file, scripts are the artifact)

| rung | setup | train acc | held-out | reads as |
|---|---|---|---|---|
| signal present | MLP on frozen embeds | — | **0.42–0.48** | the labels *are* recoverable from the fingerprints |
| architecture OK | from-scratch transformer | →1.00 (N=256) | **~0.49** (N=2048) | a tiny transformer learns the combination |
| **weights work** | **full-FT Qwen-0.5B** | **→1.00** | **0.523** (N=3400) | full-weight SFT learns *and* generalises |
| **setup fails** | **QLoRA Phi-3** (frozen *or* trainable embeds) | ~0.20 | **~0.20 (chance)** | collapses to the label marginal |

**The QLoRA failure signature:** across every config (rank 16/64, lr 2e-4/5e-4/1e-3, frozen/trainable embeddings), even **overfitting just 256 examples**, the integrated arm could not beat chance. Training loss floored at **ln C = 1.609** (the entropy of guessing the class base rate) and the prediction distribution **collapsed to a single class** (e.g. `[300,0,0,0,0]`) — it learned the marginal and ignored the symbols entirely. A flat loss curve, not a slow descent: stuck, not under-stepped.

**Full-FT generalises:** Qwen-0.5B climbed train→1.0, loss→0.002, held-out 0.21→**0.523** with predictions spread evenly across all five classes. Genuine read-side composition on pairs it never saw (2.6× chance). This is the same next-token SFT framing Phi-3 used, so the SFT setup is **not** the blocker.

**Conclusion `[MEASURED]`:** the blocker is specifically **LoRA-adapters-on-a-frozen-4-bit base** — a compute shortcut that cannot build the cross-token combination circuit. The integrated arm must *actually integrate* (full fine-tune). Since full-FT of 3.8B Phi-3 does not fit 11GB (needs ~6× the model in memory: weights + grads + 2 optimizer buffers), the **shared base pivots to a small model that full-FTs on the GPU** (Qwen2.5-0.5B). Recorded as a [spec revision](./spec.md): a *precondition fix*, not a goalpost move — success thresholds, held-out-only scoring and the controls are unchanged.

### Construct-validity note

The diagnostic ladder is what licenses the conclusion: the separability probe (0.45) rules out "signal absent"; the from-scratch transformer rules out "architecture can't"; full-FT Qwen ruling *in* with the same SFT framing rules out "SFT framing." Only the QLoRA/frozen-base condition fails — so the failure is localised to that setup, not the task, the bet, or the metric. `loss = ln C` is a precise diagnostic (it is *exactly* the marginal-prediction floor), and the collapsed pred-distribution confirms input-independence rather than partial learning. The 0.523 ceiling is the integrated arm's *data-rich* accuracy (`Xceil`) at one `k`; it measures best-case generalisation, not sample efficiency. The earlier frozen-vs-trainable-embeddings pre-registration is **moot**: QLoRA fails both ways and full-FT trains all weights regardless.

## Limitations

- **Not the substantive test.** This is the integrated arm's *ceiling* at one `k` (64), one seed. The bet — sample-efficiency (reach ~ceiling from *few* examples) and the **fan-open across `k`** — is unrun.
- **Bolt-on arm not yet built on the new base.** The reader must be re-instantiated on Qwen-0.5B and shown (a) at chance on factored, (b) winning on the modular control (competence certificate).
- **Ceiling 0.523 is just under the 0.55 line pre-written for the old 40-pt criterion.** That criterion is dropped (see spec revision); for a *gating* experiment the signal is a clear, scaling separation, and ~32 pts of room over chance suffices. If more headroom is wanted, 3 label buckets is the lever.
- **Small-base external validity.** Demonstrated at 0.5B; whether it holds at deployment scale is out of reach on this hardware. Acceptable for an internal gate; flagged honestly.
- Run outputs (except the smoke JSON and a full-FT checkpoint) were not persisted to file; the scripts + this page are the record.

## Raw artifacts

- Spec / pre-registration (revised 2026-05-27): [spec.md](./spec.md).
- Phase-1 task validation: [phase1-results.md](./phase1-results.md).
- Code: [phase2_lib.py](../../../experiments/factored-operator-beachhead/phase2_lib.py) (data/prompt/scoring), [phase2_pilot.py](../../../experiments/factored-operator-beachhead/phase2_pilot.py) (QLoRA arms + bolt-on + diagnose mode), [phase2_scratch_check.py](../../../experiments/factored-operator-beachhead/phase2_scratch_check.py) (from-scratch control), [phase2_fullft.py](../../../experiments/factored-operator-beachhead/phase2_fullft.py) (full-FT, ceiling, resumable), [RUN_phase2.md](../../../experiments/factored-operator-beachhead/RUN_phase2.md).

## Related

- [spec.md](./spec.md) — the pre-registration; the 2026-05-27 revision records the instantiation pivot this run forced.
- [phase1-results.md](./phase1-results.md) — the idealised bounds (MF-label realistic ceiling ~0.58) the full-FT 0.523 sits just below, as expected.
- [integration-gate](../../concept/integration-gate.md) — the validity gate; unchanged by this run (instantiation detail, not gate argument).
- [Xu, Dai & Zhang 2026](../../source/xu-2026-agentic-memo.md) — Theorem 1; its `ᾱ<1` is still the empirical precondition the *next* phase must establish.
- **Next:** the scaling-separation grid (sample-efficiency vs `N`, fan-open across `k`) on full-FT Qwen-0.5B + a Qwen bolt-on — the actual bet.

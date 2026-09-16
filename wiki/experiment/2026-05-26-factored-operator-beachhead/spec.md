---
type: experiment
name: "Factored-operator beachhead — the composition separation, pre-registered"
status: SPEC — LOCKED 2026-05-26, REVISED 2026-05-27 (instantiation pivot, see § revision); Phase 1 passed, Phase 2 integrated-arm validated, scaling separation pending
last_ingested: 2026-05-28
program: kerros
sources: [../../source/xu-2026-agentic-memo.md, ../../concept/integration-gate.md, ../../source/zhang-2026-compression-spectrum.md, ../../open-question/tier-3-structural-vs-semantic.md]
epistemic_tags: [speculated]
tags: [kerros, beachhead, composition, integration-gate, matrix-completion, collaborative-filtering, pre-registration]
---

> **Program: [Kerros](../../concept/kerros.md).** This is the read-side (composition) beachhead the [integration gate](../../concept/integration-gate.md) calls for: the one test with a theorem behind it ([Xu Thm 1](../../source/xu-2026-agentic-memo.md)). It operationalises *"§ How to use it — the experiment shape"* into a locked, pre-registered spec.

## One-line claim under test

> On a composition task with **low-rank latent structure** (cheap to learn) but a **large symbol count** (expensive to memorise), a model that **integrates** the examples into its weights generalises to unseen combinations from far fewer examples than the **strongest fair bolt-on** (offline distillation into text + chain-of-thought, frozen weights) — and the gap **widens with scale**.

This is the [Xu Theorem 1](../../source/xu-2026-agentic-memo.md) separation (`Ω(k²)` retrieval vs. `O(d)` parametric) instantiated so that Xu's **Assumption 1 (`ᾱ < 1`)** is *established empirically against a smart bolt-on*, not assumed.

> **Addition 2026-05-28 — a second gate.** This spec pre-registers only the *existence* separation (does the integrated arm beat the bolt-on, gap widening with `k`). A mid-run reframe (AJ) added a second, equally necessary gate: **efficiency** — is the integrated arm's *write* cheap/local/incremental enough to be **memory**, not a retrain? The existence run + first efficiency result + the pre-registered low-rank decider live in [scaling-and-memory-gates](./scaling-and-memory-gates.md); the durable question is [incremental-integration-cost](../../open-question/incremental-integration-cost.md); methodology in [integration-gate § the efficiency gate](../../concept/integration-gate.md).

## The task — a factored (rank-`m`) operator

Canonical matrix-factorisation / collaborative-filtering construction, chosen because it **separates the two checks that fight each other** (see [integration-gate § the rub](../../concept/integration-gate.md)) onto two independent knobs:

- `k` opaque left-symbols and `k` opaque right-symbols (arbitrary IDs, e.g. `L0317`, `R0042` — features are **hidden**; only `(a,b)→label` examples reveal them).
- Each symbol carries a hidden vector: `u_a ∈ ℝ^m` (left), `w_b ∈ ℝ^m` (right), `m` small.
- **Score:** the hidden vectors are **mean-centred across the population and unit-normalised**, so `s(a,b) = û_a · ŵ_b` is the **(adjusted) cosine similarity** between the two vectors; the full `k×k` score matrix is **rank ≤ `m`**. Centring+normalising strips the per-symbol *bias terms* (the Netflix user/item bias: vector magnitude = "loudness", mean direction = "tilt") so a pair's label depends **only on the angle** between the two specific vectors, not on either symbol alone. **Validated in Phase 1** (2026-05-26, artifacts in `experiments/factored-operator-beachhead/`): the raw dot-product form leaks a ~0.25–0.30 marginal/lookup floor; centred+normalised, the floor sits at chance (0.20) while the structural ceiling is unchanged.
- **Label:** `s(a,b)` bucketed into `C` balanced quantile bins (so chance = `1/C`).
- Asymmetric by construction (`u_a·w_b ≠ u_b·w_a`) so an **order-blind baseline must fail** — the order-blind check is the [tier-3 BoW-at-chance gate](../../open-question/tier-3-structural-vs-semantic.md) in this setting.

**Why this threads the needle:**

| Knob | Controls | Check it discharges |
|---|---|---|
| `m` **small** | the matrix is low-rank → recoverable from `~O(k·m·log k)` cells (matrix completion; Candès & Recht 2009) | **cheap to learn** (the integrated arm wins) |
| `k` **large** | the latent table (`2k` vectors) is too big to paste into a prompt and apply lookup-by-lookup reliably | **can't execute from text** even if the bolt-on reverse-engineered the factors offline (`ᾱ < 1` survives a *smart* bolt-on) |

Modular arithmetic (Xu's own example) has only **one** knob: shrinking it to learn cheaply also shrinks it to a writable one-liner. The factorisation decouples *"small to learn"* from *"small to state."* That decoupling is the whole reason this task and not that one.

## Arms

1. **Integrated (Kerros).** LoRA fine-tune the base model on the `N` observed cells (`(a,b) → label`). The model must infer the hidden factorisation through weight updates. Report held-out-pair accuracy vs. `N`.
2. **Bolt-on (control) — the one we are honest about beating.** Same base model, **weights frozen**. Pre-committed strongest fair form, frozen before any run:
   - **(b-strong)** an **offline** LLM pass over the observed cells to distil structure into text (induce factors / rules / notes — unlimited offline budget), that text placed in context, **plus chain-of-thought** at answer time. *No inference-time code execution / tools* (that would make it a computer, not a memory — see [integration-gate](../../concept/integration-gate.md) and the 2026-05-26 control-validity call).
   - **(b-weak)** raw nearest-cell retrieval into context — reported as a lower bound only.

Both arms share the same base model so the comparison isolates **where the knowledge lives** (weights vs. context), not model capacity.

## Negative control (anti-rigged-deck)

Run the **identical protocol on modular arithmetic** `(a·b + c) mod p` (hidden `c`). Pre-registered prediction: the **strong bolt-on should WIN/match here** (the rule is text-recoverable and CoT-executable). Purpose: prove our bolt-on is competent, not a strawman. If the strong bolt-on can't clear the success bar even on modular arithmetic, the bolt-on implementation is too weak → **fix it before trusting the main result.**

## Metrics (chosen before running)

- **Primary:** held-out-pair accuracy (cells observed by *neither* arm) vs. example budget `N`, per arm, across a `(k, m)` grid.
- **Separation metric:** budget-to-reach **near the integrated arm's own data-rich ceiling** (`Xceil`), and **how that budget scales with `k`**. Predicted: integrated `~O(k·m·log k)` (sub-quadratic); bolt-on `~O(k²)` or never.
- **Baselines:** chance (`1/C`); **order-blind** (model/feature that ignores which symbol is left vs. right — must sit at chance, else the task is shallowly solvable).

## Pre-registration — thresholds & abort conditions

**LOCKED 2026-05-26 (AJ sign-off).** Fixed before the first run; we forfeit the result if we move these after seeing data.

**Design grid:** `m = 4`, `C = 5` (chance 20%), `k ∈ {32, 64, 128, 256, 512}`, **5 seeds per cell**. Example budget `N` swept on a **log grid from ~`k·m` up to `k²/2`** (always below the full table, so held-out is never empty — corrects the small-`k` overflow in the draft).

**Ceiling-relative success.** Let `Xceil(k)` = the integrated arm's accuracy when trained on abundant data (near the `k²/2` cap). "Reaches it" = **within 5 pts of `Xceil`**. We test generalisation-per-example against the arm's *own* ceiling, not an absolute number (the task has a sub-100% Bayes ceiling from boundary cells).

- **SUPPORTED iff** — at the largest `k`, the integrated arm reaches within 5 pts of `Xceil` at some `N ≪ k²`, while the strong bolt-on (b-strong) stays **≥ 40 pts below `Xceil`** at matched `N`; **and** the integrated budget-to-ceiling scales **sub-quadratically** in `k` while the bolt-on never reaches it below `N = k²/2`; **and** the gap is **large and significant across the 5 seeds** (40-pt size floor *and* statistical significance — not one lucky draw).
- **REFUTED iff** — the strong bolt-on comes **within 10 pts of the integrated arm** at matched sub-quadratic `N`. (The rule was text-recoverable → read-side separation in doubt → **major negative update on Kerros**, reported as such.)
- **Inconclusive zone (deliberate):** a 10–40-pt gap is *neither* — we refuse to call ambiguous data a win.
- **Bolt-on-validity gate** — on the modular-arithmetic negative control the strong bolt-on must **reach within 5 pts of its ceiling** (it should *win* there). Fail ⇒ the bolt-on is a strawman; strengthen it before reading the main result.
- **Order-blind gate** — an order-blind / main-effects predictor must sit **well below the structural ceiling** on held-out pairs (the *interaction* must carry the signal, not per-symbol marginals). Fail ⇒ the task is shallowly solvable; redesign ([BoW-at-chance](../../open-question/tier-3-structural-vs-semantic.md) discipline).

**Goalpost-moving tells, named in advance (we forfeit the result if we do these):**
- *"the bolt-on retrieval wasn't good enough"* — (b-strong) is **frozen before running**; we may not weaken it when it does well nor invent a stronger one when it does poorly. (We *may* re-run b-strong with a **larger** frozen model as a one-way robustness check — only ever making the bolt-on stronger.)
- *"`k` wasn't large enough"* — the claim is the **scaling slope**, not a single point; a one-`k` win does not count.
- *"it just memorised"* — only **held-out** cells (seen by neither arm) are scored; report a contamination check.

## Procedure

**Build sequencing (de-risk before GPU).** Two phases, so we validate the *task design* before spending fine-tuning compute — the same "sim before prod" logic the whole spec rests on:

- **Phase 1 — task-design validation (no GPU).** Generate the datasets; run the **order-blind / main-effects gate**; run an **idealised structural learner** (low-rank matrix completion — the upper bound on any integrated arm for this generative model) and a **retrieval floor** (lookup with no structure). Confirm (a) the order-blind gate passes, (b) the structure is recoverable at sub-quadratic `N`, and (c) the completion-vs-retrieval gap *fans open with `k`*. If any fails, the task is broken — redesign for free before touching a model. **→ Phase 1 RAN + PASSED (2026-05-26); see [phase1-results](./phase1-results.md)** — all three gates clear once the embeddings are centred+normalised (→ cosine), which dropped the order-blind floor to chance.
- **Phase 2 — the two real arms (host GPU).** Built only after Phase 1 passes.

**Full procedure:**
1. Generate factored-operator + modular-control datasets across the `(k, m)` grid × 5 seeds; coverage-guaranteed train pool + disjoint held-out test set.
2. **Phase-1 gates/bounds:** order-blind / main-effects gate; matrix-completion upper bound; retrieval floor; check the fan-open across `k`.
3. **Integrated arm:** measure `Xceil(k)` (abundant-data saturation), then LoRA fine-tune over the `N`-sweep; evaluate held-out.
4. **Bolt-on (b-strong):** offline distillation pass → context construction → CoT inference over held-out.
5. Plot accuracy-vs-`N` and budget-to-ceiling-vs-`k` for both arms + baselines; run the negative control; check all four gates; write up against the pre-registration verbatim.

## Locked decisions (2026-05-26)

- **Base model: Phi-3-mini.** Known quantity from prior probes; a capable enough reasoner that the bolt-on's in-context + CoT is genuinely strong (we *want* a strong bolt-on to beat). Since the bolt-on arm needs no fine-tuning, a close result can be stress-tested by re-running *only* b-strong with a larger frozen model (e.g. Qwen2.5-7B) — a one-way "we beat an even smarter one" check.
- **Thresholds:** locked above (ceiling-relative success within 5 pts; ≥40-pt gap, significant across 5 seeds; REFUTED within 10 pts; `N` log-grid `k·m`→`k²/2`).
- **Compute.** Per [[notebook_workflow]]: Nils writes the notebooks, AJ runs on host GPU. **Phase-1 validation is CPU-only** (numpy/scipy/sklearn). Run artifacts land in `experiments/factored-operator-beachhead/` (code/results), separate from this spec.

## 2026-05-27 revision — integrated-arm instantiation

`[MEASURED]` Phase 2 ([phase2-results](./phase2-results.md)) found that the locked **"QLoRA Phi-3" integrated arm cannot learn the task** — frozen *or* trainable embeddings, every rank/lr tried, it collapses to the label marginal even overfitting 256 examples. A diagnostic ladder localised this to the *setup*: a full fine-tune of a small model (Qwen2.5-0.5B, all weights) learns and generalises (ceiling 0.523 at k=64). Full-FT of 3.8B Phi-3 does not fit the 11GB GPU. **Three locked decisions are therefore revised:**

- **Base model: Phi-3-mini → a small model that full-fine-tunes on 11GB (Qwen2.5-0.5B).** Both arms still share the base. The "strong bolt-on" intent is preserved via the *one-way bonus run* (re-run only the reader on a bigger frozen model) plus the **modular control as a competence certificate** (the small reader must win on modular).
- **Integrated arm: QLoRA → full fine-tune.** "Adapters on a frozen base" was a compute shortcut that crippled the arm; the honest integrated arm changes all the weights.
- **Success metric: the absolute ≥40-pt gap is retired** in favour of a headroom-/scaling-relative read. The 5-bucket task's realistic ceiling (~0.55, [Phase 1](./phase1-results.md)) makes a 40-pt absolute gap unreachable on *any* base. Per AJ this is a **gating experiment for our own confidence, not peer review** — the load-bearing signal is a *clear separation that fans open with `k`*, not an absolute number. (If more vertical room is wanted, drop to 3 label buckets.)

**Not a goalpost move:** these fix a *precondition* (the integrated arm must be able to do the task at all) and *correct a metric that was unsatisfiable by construction*. Held-out-only scoring, the controls, and the pre-registered "we forfeit if we weaken the bolt-on" discipline are unchanged. The frozen-vs-trainable-embeddings sub-decision from earlier in the session is **moot** (full-FT trains all weights).

## Related

- [integration-gate](../../concept/integration-gate.md) — the validity test this discharges; § "How to use it" is the design direction this locks.
- [Xu, Dai & Zhang 2026](../../source/xu-2026-agentic-memo.md) — Theorem 1 and Assumption 1 (`ᾱ < 1`), the formal claim instantiated here.
- [tier-3-structural-vs-semantic](../../open-question/tier-3-structural-vs-semantic.md) — the BoW-at-chance gate, here the order-blind gate.
- [Zhang et al. 2026 — Compression Spectrum](../../source/zhang-2026-compression-spectrum.md) — testable prediction (i); this is the gate-crossing version.

## Source archive

Designed in the 2026-05-26 Nils/AJ session (continuation of the wide pass). Task family selected by screening candidates against the four checks: factored operator chosen (lead), modular arithmetic kept as negative control, deep-composition held in reserve, naturalistic + multi-hop rejected. Control definition (offline-distillation-into-text + CoT, no inference-time execution) ratified by AJ on construct-validity grounds. Not yet run.

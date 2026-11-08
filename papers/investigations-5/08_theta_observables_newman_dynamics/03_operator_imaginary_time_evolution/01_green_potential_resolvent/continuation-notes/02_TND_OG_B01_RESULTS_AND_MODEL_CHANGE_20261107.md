# B01 results, continuation and model-change handoff

7 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex assistance. Actual recorded session: **gpt-6-astra / max**, chat0001. This dated handoff supersedes [Continuation01](01_TND_OG_GREEN_RESOLVENT_CONTINUATION_20261107.md)'s setup-only next-task prompt; the [sole register](../research-progress/01_TND_OG_GREEN_RESOLVENT_RESEARCH_PROGRESS_20261107.md) remains authoritative.

| Next task | Type / recommended model | Readiness and reason | Output |
| --- | --- | --- | --- |
| **TND-OG-E01 r1** | **E — gpt-6.1-sol / ultra** | **Ready, UNACTIVATED.** Coefficient class, source, region, theorem input, proof route and success test are frozen. | Prove the specified normalized quadratic-residual floor, or return its exact failed clause. |
| TND-OG-E02 | E — gpt-6.1-sol / ultra | Reserved; needs actual E01 return and assessment request. | Check the claimed transfer and Note01's fixed-source conditioning result; one correction cycle. |
| B01 r2, only if triggered | B — Astra | No automatic activation. Needed if E01 requires a changed mechanism, coefficient class or missing primary input beyond its bounded check. | Resolve that particular failed premise, not repeat the original broad brainstorm. |

The author's current request completed the bounded B01 cycle. No model setting was changed. The actual effort **max** above must not be relabelled ultra because ultra is the recommendation for the next task. A model change is not independent specialist review. E01 is a fixed analytical execution task; there is no reason to keep it attached to Astra merely to preserve context.

## What survives from this session

[Note01 §§1–5](../notes/01_TND_OG_B01_UNIFORM_SOURCE_CONDITIONING_20261107.md) derives a fixed-prime, scalar-normalized positive-source family with relative source change η, common complete weighted bounds and counts, and O(η) fixed-safe-line resolvent jets. Its added Green potential is Θ(√η), uniformly in every real center. This rules out an o(√η) stability modulus on a class containing this family; in particular it rules out a uniform Lipschitz estimate there.

The family is a translated mixture, **not the canonical theta source**. The baseline is also perturbed. The statement concerns a difference of Green potentials, so it assumes neither RH nor that the baseline potential is zero. It is not a discontinuity theorem, a universal upper Hölder theorem, or an obstruction to resolving source errors at order d². The source parameter η is not Newman time. Status: **proved in-note from inherited inputs; same-assistant checking only**.

[B01 decision](../brainstorm/notes/01_TND_OG_B01_RESOLVENT_CONDITIONING_DECISION_20261107.md) also selected the optional arithmetic mechanism for a bounded obstruction proof. Radziwiłł v3, Proposition B supplies a mean lower bound for |1−ζA|². It does **not** directly bound this branch's ε_A(X)². The new [E01 request](../research-progress/handoffs/02_TND_OG_E01_SHORT_MOLLIFIER_REQUEST_20261107.md) freezes the missing transfer and a positive target floor 1/(12ζ(5/2)^4) in the liminf. **That target remains unproved here.**

The scope is visibly narrower in exponent than setup: fixed 0<θ<1/2, complex |a_n|≤1 and a₁=1, one polynomial on the entire padded interval [T−(8/π)log T,2T+(8/π)log T]. Padding is part of the theorem, not an ignorable endpoint error. The intended conclusion concerns a sufficient quadratic certificate, not J itself. The missing favorable signed canonical upper bound remains missing.

## Exact handoff and failure traps

Read the [overview](../research-overview/01_TND_OG_GREEN_RESOLVENT_RESEARCH_OVERVIEW_20261107.md), [plan](../research-plan/01_TND_OG_GREEN_RESOLVENT_RESEARCH_PLAN_20261107.md), [B01 return](../research-progress/handoffs/01_TND_OG_B01_RETURN_20261107.json), [E01 request](../research-progress/handoffs/02_TND_OG_E01_SHORT_MOLLIFIER_REQUEST_20261107.md), [frozen inputs](../research-progress/handoffs/02_TND_OG_E01_INPUTS_20261107.json), and [source-use record](../references/01_TND_OG_B01_SOURCE_USE_20261107.md). The PDF is stored outside Git at the recorded path/hash; its version-pinned public URL remains usable elsewhere.

- Keep c_A(X) inside the actual variance. Prove uniform first and safe-line means; do not substitute the primary mollifier moment for the normalized residual.
- Multiplier zeros may occur in the strip. Their Green contribution is nonnegative and must be retained. The qζ representation has already cancelled the zeta pole.
- Keep θ<1/2 and one polynomial across the padded interval. No adaptive-center, longer-mollifier or every-center conclusion follows from an average.
- Common source bounds did not cure the fixed-prime square-root loss. New canonical claims must use information beyond the shared norms or pay collision resolution.
- No derivative-order limit, numerical campaign, manuscript, commit or sibling expansion is part of this packet.

Follow the [result index](../../../../../../result-summaries/README.md), [controls12](../../../../../../result-summaries/12_collision_controls_and_screening.md), [patterns index](../../../../../../avoid/README.md), especially [target01](../../../../../../avoid/01_restating_the_target.md), [control02](../../../../../../avoid/02_shape_only_arguments_and_the_controls.md), [scope07](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [same-model review05](../../../../../../avoid/05_same_model_reviews_and_shared_premises.md). Note01 §5 supplies the actual failed control premises. Do not update repository result summaries with the unexecuted E01 target.

## Pasteable continuation for Sol

~~~text
Continue research for Edward Baker in /Users/ebbaker/Documents/shifted-zeta-positivity at:
papers/investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/01_green_potential_resolvent

Read root AGENTS.md, GPT_RESEARCH_MODEL_WORKFLOW.md, REFERENCE_WORKFLOW.md, LARGE_FILES.md and tools/CHAT_HISTORY.md; result-summaries/README.md and 12_collision_controls_and_screening.md; avoid/README.md and its target01, control02 and scope07 entries.

Read the branch README, sole research-progress/01_TND_OG_GREEN_RESOLVENT_RESEARCH_PROGRESS_20261107.md, continuation-notes/02_TND_OG_B01_RESULTS_AND_MODEL_CHANGE_20261107.md, notes/01_TND_OG_B01_UNIFORM_SOURCE_CONDITIONING_20261107.md, brainstorm/notes/01_TND_OG_B01_RESOLVENT_CONDITIONING_DECISION_20261107.md and references/01_TND_OG_B01_SOURCE_USE_20261107.md.

Execute [E] TND-OG-E01 r1 exactly as frozen in research-progress/handoffs/02_TND_OG_E01_SHORT_MOLLIFIER_REQUEST_20261107.md. Verify its input manifest 02_TND_OG_E01_INPUTS_20261107.json. Recommended model is gpt-6.1-sol, effort ultra; record actual metadata without changing the author's selection.

Prove the uniform normalized residual-floor target for the literal time-zero canonical source, complex bounded coefficients, fixed theta<1/2 and one polynomial on the padded interval. Pay the primary theorem's coefficient uniformity, first moment, safe-line mean, center denominator, multiplier zeros, complete convolution and source/tail ledger. The new Radziwill v3 source is already cataloged and externally archived. Note01's fixed-source conditioning theorem is separate; do not assume the canonical field has a collision or infer a lower bound on its Green potential from the residual floor.

Save the analytical proof in notes/, exact return in research-progress/handoffs/, and update the sole register plus concise continuation. One bounded repair is allowed. Return a precise failed clause to B01 r2 if the route needs a conceptual change. No numerics, manuscript, larger coefficient class or sibling work. E02 requires the actual E01 return and a separate fixed assessment request.

Refresh chat history at the beginning and end. Preserve this chat's existing unique registration if continuing it; a genuinely new branch-only chat registers once in this branch's chat-histories/. Use the bounded exact-turn final capture; never fabricate an unsent final response. Follow the reference and large-file policies and leave frozen inputs unchanged.
~~~

The investigation remains open. This handoff provides a tractable next proof test and preserves the unacquired canonical signed estimate; it is not a claim that the larger Green/resolvent program has succeeded or failed.

# TND-OG-B04 initial planning and proposed priorities

8 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex LLM assistance. The current runtime identifies the assistant as **gpt-6-astra**; reasoning effort is not exposed. The registered transcript supplies no model-configuration entries, so runtime identification is distinguished from capture metadata.

**Planning discussion before substantive B04 research.** Edward requests continuation from [Continuation09](../../continuation-notes/09_TND_OG_E05_RESULTS_AND_MODEL_CHANGE_20261108.md), an overview and possible changes before work begins, and records in brainstorm and chat-histories. The priorities below are the assistant's proposals for discussion. The author's choice is pending. The [sole register](../../research-progress/01_TND_OG_GREEN_RESOLVENT_RESEARCH_PROGRESS_20261107.md) owns live status.

## The mathematical task

E03 and E05 provide a way to acquire the canonical signed Green quantity with controlled error:

\[
0\le U_{R,Q,\delta}(X)-J_0^{\rm G}(X)
\le\mathcal E_{X,R}(\delta)+2\mathcal T(X,R)+2\beta_Q.
\]

[Note06](../../notes/06_TND_OG_E03_COMPLETE_SIGNED_LOG_ACQUISITION_20261108.md) gives finite choices for any prescribed center and positive accuracy. [Review06](../../reviews/06_TND_OG_E05_CLAIM_LEVEL_ASSESSMENT_20261108.md) accepts its eight claims with the evidence/control clarification in [Note07](../../notes/07_TND_OG_E05_ASSESSMENT_CALCULATIONS_20261108.md). This remains internal LLM assessment with shared premises.

B04 asks what can establish a useful **value** of that quantity. The inherited identity is

\[
J_0^{\rm G}(X)=\mathcal L(X)-P(X)+\mathcal G(X,1),\qquad
\mathcal L(X)=\int_{\mathbb R}\frac{\log|\zeta(1/2-ix/2)|}{16\cosh(\pi(x-X)/8)}\,dx.
\]

A verified upper bound \(\overline U<m(d,r)\), where
\[
m(d,r)=\frac{\sin(\pi/8)d}{\cosh(\pi r/8)},\qquad 0<d\le1,\quad r\ge0,
\]
would exclude upper-half-plane zeros with \(d\le y\le1\) and \(|x-X|\le r\). The source is the complete canonical theta source at Newman time zero; the Green observable, kernel and prime/pole normalization stay fixed. Smaller acquisition error alone does not establish this strict upper comparison.

## Proposed bounded comparison

Keep Continuation09's limit of **at most two routes and one focused clarification of the leading candidate**. This is type **B**, recommended **Astra**, because choosing the consequential canonical estimate or finite question remains unresolved.

1. **Direct signed analytical comparison, recommended first.** Identify a specific estimate for the coupled logarithmic integral and canonical prime baseline. It must retain the relevant cancellation and account for tails, small-value regions and fluctuations. The deliverable is a quantitative gain on a declared domain, an obstruction for a specified estimating class, or the exact additional inequality that remains unpaid. Rewriting the existing Green identity does not count as a gain. Any proposed estimate must be screened against the controls with each control's own normalization and actual defect response.
2. **One bounded directed-evaluation question.** Prefer one prescribed tuple \((X,d,r)\); use a small finite family only if its cases answer distinct decisions. Before any implementation, fix the target margin, analytical error, evaluation interval width, arithmetic, source/prime cutoffs or bounded refinement rules, work limit and stopping condition. State what a favorable, unfavorable or inconclusive return would change. A failure to certify the upper bound is not evidence that a zero exists in the target box.

The [result index](../../../../../../../result-summaries/README.md), [controls12](../../../../../../../result-summaries/12_collision_controls_and_screening.md) and [avoid index](../../../../../../../avoid/README.md) supply the inherited scope. The relevant safeguards are [target01](../../../../../../../avoid/01_restating_the_target.md), [control02](../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md), [shared-premise05](../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md), [scope07](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [coupled-payment12](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).

## Suggested refinements for discussion

**Prioritize the analytical route.** The outstanding issue is favorable canonical cancellation. Give the second route a distinct purpose: decide whether one finite evaluation can resolve an identified uncertainty or provide useful implementation calibration. This is an ordering recommendation within the two-route limit, not a claim that either route succeeds.

**Check feasibility before issuing an execution request.** Note06's logarithmic modulus has exponent \(1/n_v\), which deteriorates with height; the finite quadrature argument pays sensitivity proportional to \(1/\delta\). These prove attainability without establishing affordable cost. First examine whether the stated allowances and proposed evaluation method fit a finite work budget. If routine cost calculations are needed, specify them as an E task rather than silently executing them during B04. A failed feasibility check applies to the chosen estimates and method, not to every possible evaluator.

**Make the outcome change a research decision.** For a calibration pilot, define the useful measurement, such as which error term dominates or whether the fixed budget attains the requested enclosure. Before calling a local exclusion new coverage, check the relevant established coverage and its normalization. Work inside an already established region is labeled calibration. See [numerics10](../../../../../../../avoid/10_numerics_ahead_of_the_question.md) and [known-region11](../../../../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md).

The HDA/RS hierarchy remains a possible later provider comparison if a specific source-evaluation bottleneck justifies it. Its existing local transfer result does not supply the missing signed value; adopting it requires an explicit contract with the complete remaining payments.

## Completion and discussion boundary

B04 should end with one decision note stating the comparison, exact gain or remaining premise, control/scope check and next step. If the comparison fixes a tractable execution task, prepare its finite request and input packet and recommend **Sol6.1** before execution. Otherwise record the scoped failed route or unresolved conceptual premise. Numerical execution, manuscript integration and shared or sibling research edits remain outside that bounded decision.

The planning question for Edward is whether to prioritize a new analytical estimate, as recommended, or to make the design of the first finite feasibility test the primary objective. No choice is attributed to him yet. Substantive research will follow the initial discussion he requested.

## Input and conversation continuity

Read during this planning pass: Continuation09, the live register, E03 Note06, E05 Note07/Review06, Request13/Return14, the source/consumer overview, repository workflows, result/avoid indexes and relevant screening passages. This is orientation rather than a fresh proof assessment or literature audit.

Read-only identity checks reproduced **47/47** matching E05 input entries and **5/5** supplemental control entries. E03 remains **33/34**, with only the historical `tools/CHAT_HISTORY.md` mismatch: current 20,937 bytes and SHA-256 `62e4c8323ce51c9d2a74b690594f99f609ae201141ec85fa86b9ed3e3a623e83`. Frozen source records were preserved.

This conversation is registered as **chat0004**, actual title **Continue TND-OG-B04**, thread `01a1bbe3-581f-72c2-abd7-752993ab95aa`, in the investigation's [chat-histories](../../chat-histories/README.md). The actual planning turn is `01a1bbe3-8a98-7242-a558-8d229d59c2db`; the preceding submission turn was interrupted. Public text is captured by the locked recorder. The final reply can only be captured after it is sent; the bounded exact-turn follow-up must be checked on continuation. Runtime identification does not fill absent historical model settings.

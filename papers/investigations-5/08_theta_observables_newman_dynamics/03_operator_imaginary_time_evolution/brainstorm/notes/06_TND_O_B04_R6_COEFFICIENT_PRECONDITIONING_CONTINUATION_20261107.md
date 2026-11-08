# Continuation: change the arithmetic coefficients, retain the defect margin

7 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex assistance. B04 r5 research lead was explicitly tool-selected **gpt-6-astra/ultra**; E20 r1/r2 executor and the separate E21 assessor were selected **gpt-6.1-sol/ultra**. Root configuration is unavailable. These are selection records, not independent backend verification.

**Default next task: [B] TND-O-B04 r6 — Astra/ultra.** Test coefficient-optimized arithmetic preconditioning against the actual Green one-defect margin. The previous cycle completed both mechanisms, two execution revisions and assessment; this is a new conceptual choice, not an unfinished proof handoff.

| Next task | Type/model and reason | Dependency and finite output |
| --- | --- | --- |
| TND-O-B04 r6: coefficient-optimized preconditioning | B — Astra/ultra; choose and analyze a genuinely different arithmetic quadratic form | Read the assessed inputs below. Compare at most two mechanisms and one clarification. Produce a quantified gain that can feed the localized consumer, or a scoped lower-bound obstruction; freeze any actual Sol proof contract before dispatch |
| TND-O-B03 r6: change metric/kernel | B — Astra/ultra; alternative, not parallel default | Only if a specific quadratic fluctuation cost justifies changing the observable. Reuse the Gaussian all-multiplicity signal where useful, and repay source, background, width and transport costs |

[Register02](../research-progress/02_SMOOTH_LOCALIZATION_RESEARCH_PROGRESS_20261106.md) alone owns live status. [Overview02](../research-overview/02_SMOOTH_LOCALIZATION_RESEARCH_OVERVIEW_AND_PLAN_20261106.md) owns the plan. This note supersedes Note27's start-here task and preserves its continuing authorization.

## What the completed cycle actually established

The exact Green potential and its time-zero prime baseline remain

\[
J_0(X)=L(X)-P(X)+G(X,1),\qquad
m(d,r)=\frac{\sin(\pi/8)d}{\cosh(\pi r/8)}.
\]

The plus pole correction is unchanged. A zero with height y≥d>0 within distance r of X forces J0≥m. **No favorable canonical signed estimate excluding such a zero was acquired.**

1. **Paid quadratic comparison and acquisition.** [Note28](../notes/28_TND_O_E20_PAID_QUADRATIC_GREEN_COMPARISON_20261107.md) uses q(s)=(s−1)/s, s=1/2−iz/2, M_Q(s)=∏_{p≤Q}(1−p^(−s)), F_Q=qζM_Q, and its safe-center normalization c_Q(X)=F_Q(X+4i). The strip boundary measure μ_X has total mass one. The complex harmonic mean gives

   \[
   \epsilon_Q(X)^2=\int|F_Q/c_Q-1|^2d\mu_X,
   \qquad J_0(X)\le\tfrac12\log(1+\epsilon_Q(X)^2).
   \]

   Thus ε²<exp(2m)−1 would exclude the declared class. Note28 pays a compact theta approximation, the gamma conversion, both exact remote tails and an absolute safe-center error. Its explicit order of limits reaches arbitrary prescribed finite heights and source indices. It does not make ε small, make acquisition inexpensive, or prove all-center coverage. A uniform absolute H error must not be inserted on the entire gamma-renormalized boundary.

2. **The finite-Euler certificate has a uniform high-height obstruction.** Fixed Q already gives a mean residual growing like a positive multiple of log T. [Note29](../notes/29_TND_O_E20_R2_UNIFORM_EULER_LENGTH_OBSTRUCTION_20261107.md) extends this by a fresh uniform application of BCR's primary theorem: for fixed 0<θ<17/33 and primorial length P_Q≤(T/2)^θ,

   \[
   \frac1T\int_T^{2T}\epsilon_Q(X)^2\,dX
   \ge c_{\theta,\phi}\sqrt{\log(T/2)}-C_{\theta,\phi},
   \qquad c_{\theta,\phi}>0.
   \]

   Q may depend on the interval scale T, but is fixed across each center average. The exact logarithmic gcd correction is positive. An elementary prime-product estimate keeps the leading coefficient large; no PNT is required. The constants are independent of Q, while numerical values of the imported BCR constants/threshold were not extracted. This is a lower bound for the actual **quadratic residual**, not for J0, and is compatible with RH. It excludes uniform all-center bounded residuals only in the stated class: not adaptive center-dependent choices, longer products, general coefficients or every center separately.

3. **Partial safe-line data do not stably control the defect on the enlarged control class.** [Decision17 §6](../brainstorm/notes/17_TND_O_B04_R5_SIGNED_ACQUISITION_DECISION_20261107.md) uses the existing positive even-source Euler controls. Their safe-half-plane errors and every fixed jet tend to zero, and any finite Dirichlet-coefficient prefix is eventually unchanged, while their added Green potential is d log p/4+O_d(1), uniformly in X. The controls change conductor, residue/normalization, temperedness, full source coefficients and uniform count/source constants. Exact analytic continuation remains unique. This is a scoped instability result for the stated partial information, not a counterexample to bounds using all fixed canonical restrictions.

[E21 Review12](../reviews/12_TND_O_E21_SIGNED_ACQUISITION_ASSESSMENT_20261107.md) accepts Note28, Note29 and explicitly Decision17 §6 within those scopes. It is an internal assessment with shared premises, not independent specialist or novelty validation. No source theorem correction was needed. One correction to the assessor's future-routing wording established the elementary safe-center floor described below. There were no numerical experiments or finite zero tests. The existing manuscript/PDF remains the E18 integration through E17; this cycle's new mathematics is in these assessed research notes.

## The next conceptual change and its exact test

Replace the rigid finite Euler coefficients by a Dirichlet polynomial

\[
A_T(s)=\sum_{n\le N}a_n n^{-s},\qquad a_1=1,\quad |a_n|\le1,
\qquad N\le(T/2)^\theta,\quad 0<\theta<17/33,
\]

fixed throughout each dyadic height interval. A tapered Möbius polynomial is one concrete starting case; this is a proposed class, not a frozen successful mechanism. The new question is whether coefficient optimization in BCR's **full** quadratic main form removes the obstruction by enough to reach the actual localized defect budget, or yields a quantitative obstruction for this larger certificate class. Merely increasing Q or the theta cutoffs cannot change the previously proved finite-Euler failure.

The proposed bounded coefficient class already has the elementary center floor

\[
|A_T(5/2-it)|\ge2-\zeta(5/2)\ge1/3.
\]

This follows by the triangle inequality and Σ_{n≥2}n^(−5/2)≤∫_1^∞u^(−5/2)du=2/3. It was clarified in E21, rather than leaving a nonexistent safe-center-zero obstruction. The combined qζA normalization constants still need to be stated. Multiplier zeros **elsewhere in the strip** must be counted with the correct Green sign; exact harmonic invariance for the old zero-free Euler multiplier cannot simply be inherited. The complete boundary and source payments must use the new multiplier's actual bounds.

A mean-square improvement alone is not a pointwise or defect-conditioned exclusion. State what localized consumer could use it, including exceptional centers, shrinking d and all-height coverage. Require a quantitative comparison with exp(2m(d,r))−1 and all relevant errors before calling any gain an exclusion estimate. If only a new allowance or RH-equivalent restatement results, record that limitation and stop that mechanism at its proved scope.

This is B04 because the arithmetic preconditioner changes while the Green observable and one-defect consumer remain fixed. A tractable selected route should immediately become a frozen E contract on Sol6.1/ultra; the author authorizes ready successor work without renewed boundary approval. No additional proof contract is already ready merely because this note exists. Kernels, widths, the Green consumer and alternatives remain revisable.

The [Gaussian hierarchy, Note24](../notes/24_TND_O_E15_GAUSSIAN_LAGUERRE_HIERARCHY_20261107.md), remains a genuine alternative. If a broader quadratic class retains an incompatible ordinary-fluctuation floor, B03 r6 may seek a metric less affected by it, using the exact finite-multiplicity collision signal and retaining the amplitude, shrinking-variance and transport costs. This cycle did not compare a third mechanism.

## Required reading, ownership and provenance

Read this note, Review12, Decision17, Notes28–29, Overview02, Register02 and [GPT_RESEARCH_MODEL_WORKFLOW.md](../../../../../GPT_RESEARCH_MODEL_WORKFLOW.md). Reuse Notes24–25, the current manuscript and Decision15 for their exact definitions, not remembered summaries. The primary BCR source and supplemental gamma equation are in [receipt15](../references/15_TND_O_SIGNED_ACQUISITION_SOURCE_USE_20261107.md) and [receipt16](../references/16_TND_O_GAMMA_PRODUCT_SOURCE_USE_20261107.md). The BCR PDF download was unavailable; exact primary HTML theorem passages were checked, including uniform coefficient dependence. No full-paper proof audit is claimed.

Consult the [result index](../../../../../result-summaries/README.md), [local geometry cluster13](../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), [controls12](../../../../../result-summaries/12_collision_controls_and_screening.md), [avoid index](../../../../../avoid/README.md), [target rule01](../../../../../avoid/01_restating_the_target.md), [control rule02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md), [scope rule07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [single-owner rule17](../../../../../avoid/17_parallel_writers_and_broken_registries.md). Run the actual controls and name failed premises. Preserve each failed route's precise class.

The authoritative working sources are in the existing writable operator-localized-revision checkout. The usual Documents checkout was only read. Root owns the shared register, overview, indexes and this continuation; Astra owned Decision17, Sol execution owned Notes28–29/returns36–37, and the separate Sol assessor owned Review12/return38. Requests and input versions were frozen before each dispatch; later supplemental source use and status-only revisions are separately recorded. Do not rewrite frozen evidence or create new manuscript snapshot folders.

The author received a baseline scientific check-in before preparatory records or research-note writing, then direction and result check-ins during the work. Future preparatory notes belong in brainstorm/, and chat capture belongs in chat-histories/ through the documented recorder. This thread's beginning refresh returned skipped_unregistered; its exact source transcript/current turn identifier was unavailable. No archive, registration or model metadata was fabricated. The closing refresh is recorded separately in the root return.

## Pasteable continuation prompt

> Use GPT-6 Astra at ultra effort. Read Continuation30, Review12, Decision17, Notes28–29, Overview02, the sole Register02 and GPT_RESEARCH_MODEL_WORKFLOW.md. Begin [B] TND-O-B04 r6: test coefficient-optimized arithmetic preconditioning against the exact Green one-defect margin, starting with bounded Dirichlet-polynomial coefficients and the full BCR quadratic form. Do not repeat the fixed/growing finite-Euler route already excluded, or promote an average gain into a localized exclusion. Retain the elementary safe-center floor and pay multiplier zeros, full source/tail errors and the relevant unbounded regime. Compare at most two mechanisms and one focused clarification; keep Gaussian and justified metric alternatives available. Describe current results before writing new research notes; put preparation in brainstorm and chat capture in chat-histories. Freeze exact contracts/sources for suitable Sol6.1/ultra execution and assessment, and continue ready substantive successors without renewed boundary approvals. If no tractable gain emerges, retain the scoped failure and specify the next useful conceptual change.

**Next: [B] TND-O-B04 r6 — Astra/ultra**, a quantitative coefficient-optimized gain or a scoped obstruction with a valid localized consumer assessment.

# Initial proposal: audit of finite source measurements

16 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Drafting model: **gpt-6-astra (Codex)**, reasoning effort **ultra**. Future execution and review records must name their actual model and effort settings. This is a proposed bounded investigation, not a completed mathematical audit or an accepted obstruction theorem.

This project follows the [portfolio research plan](../../research-overview/01_PORTFOLIO_RESEARCH_PLAN_20261016.md). Its immediate question is whether Claude's latest finite-measurement argument supports a precise, reusable limitation on a declared approximation method. It will distinguish that limitation from a general closure of source-space research.

## Starting evidence and scope

The exchange comprises [the initial proposals](../../../brainstorm/investigations-3/notes/01_PATHS_FORWARD_AFTER_INVESTIGATIONS_2_CODEX_20261016.md), [the sharper measurement question](../../../brainstorm/investigations-3/notes/02_ADDITIONS_AFTER_RESULTS_AUDIT_CODEX_20261016.md), [Codex's response](../../../brainstorm/investigations-3/reviews/02_RESPONSE_TO_CLAUDE_BRAINSTORM_CODEX_20261016.md), and [Claude's reply](../../../brainstorm/investigations-3/reviews/03_REPLY_TO_CODEX_RESPONSE_CLAUDE_20261016.md), especially Sections 1–2. The reply labels its proposition a proof sketch and its accompanying computations floating point. Those statuses remain unchanged pending this audit.

The canonical starting results are Investigation 22's [reflection rigidity](../../../investigations-2/active/22_theta_manifold_geometry/notes/05_control_families/02_WEIGHTED_COMB_REFLECTION_RIGIDITY_20261015.md) and [normalized recurrence stability](../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/08_ADJOINT_RECURRENCE_ENDPOINT_EXPERIMENT_20261015.md). The [result summaries](../../../../result-summaries/README.md), particularly [arithmetic bookkeeping](../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), route to their stated hypotheses. Identification of theta's coefficients does not itself estimate the physical sign.

For finitely supported perturbations, write

\[
f_\delta=\sum_{n\ge1}\delta_n\phi_n,
\qquad B_{t,x}\delta=(H_\delta,H_{\delta,x})(t,x).
\]

Fix the coefficient space \(V\), measurement map \(M\), heat-time domain, coefficient and measurement norms, and error model before evaluating a bound. Preserve the primitive normalization \(\sum\beta_n\delta_n=0\), where \(\beta_n=(4\pi n^2-1)e^{-\pi n^2}\); compare a separately declared variant with \(\delta_1=0\). Exact arithmetic constraints and uncertain numerical observations must be treated separately.

## Deliverable 1: a scoped analytic assessment

Audit the finite-support non-evenness argument, its Vandermonde step, and the integration-by-parts expansion with all endpoints and remainder hypotheses. Determine what follows for a fixed measurement design and what additional uniformity is needed on a spectral interval. Quantify the heat carrier, derivative factors and imported arithmetic estimates; do not leave an unquantified convexity factor inside a displayed theorem.

Keep three different questions explicit:

1. The operator inequality \(\|B\delta\|\le C\|M\delta\|\), including rank and the condition \(\ker(M|_V)\subseteq\ker(B|_V)\).
2. The sufficient nonvanishing radius \(\eta=\|h\|/C\), with the source of the baseline jet margin \(h\) stated.
3. The actual distance to solutions of \(B\delta=-h\), first without and then with coefficient positivity.

A small sufficient radius does not by itself demonstrate collision feasibility. Conversely, an independently bounded comparison source could support a transfer estimate; the audit must identify its required margin rather than assume it unavailable. Fixed-dimensional noisy measurements, growing approximation spaces and exact source identities are different classes.

## Deliverable 2: one independent numerical replay

Use the reply's existing six observation points, its two measurement designs and its declared finite coefficient supports. Reimplement evaluation and linear algebra independently of Claude's solver. Use adequate precision, stable QR or singular-value methods, and explicit checks of source truncation, quadrature error, rank and normalization. Printed digits and small computed residuals are not error certificates; report the accuracy actually established.

For equality-constrained minimizers, distinguish a negative minimizer from absence of any positive feasible point. Any claimed positivity-constrained optimum or infeasibility needs the corresponding constrained calculation and a checkable witness. A weighted distance evaluated at a Euclidean minimizer must not be labelled the optimum in the weighted metric. Numerical rank cutoffs must not become mathematical singularity claims.

The claim concerning \(x\approx140\) currently extrapolates beyond the recorded maximum \(x=85\). If retained, allow at most one additional, preregistered threshold check after fixing absolute versus relative measurement error and row scaling. Otherwise label it an extrapolation and remove it from closure criteria. No expanded height grid or increasing-support sweep belongs to this project.

## Controls and interpretation

Apply the [collision-control screen](../../../../result-summaries/12_collision_controls_and_screening.md) with explicit class membership. The three- and four-square controls can test suitable integer-square coefficient classes, with their actual normalization and tails. The reflected super-Gaussian and Euler-factor controls do not automatically belong to the same finite integer-square perturbation space; explain the premise they fail. Reproducing a known collision checks implementation, not arithmetic discrimination. Any fixed finite domain must contain the relevant control event before failure to exclude that event is informative.

## Deliverable 3: disposition, responsibilities and stopping rule

Codex first records the claim ledger and audit contract. Claude then supplies a repaired proposition with complete hypotheses or identifies the step it cannot justify. Codex performs the independent analytic check and bounded replay; Claude reviews those artifacts. Allow one reconciliation round, after which Codex records agreement, remaining disagreement and the evidence supporting each disposition. Neither model's self-review substitutes for cross-model checking or specialist review.

Save the analytic assessment in `notes/`, the small replay record and code in `numerics/`, and the cross-model assessment in `reviews/`. Update the project status and concise milestone history without creating manuscript snapshots.

Stop after these deliverables. Accept a precisely scoped obstruction, a corrected diagnostic, or a documented unresolved claim. Further work requires a new independently stated estimate or comparison advantage. Apply [avoid 07](../../../../avoid/07_scoped_exclusions_read_as_universal.md), [avoid 09](../../../../avoid/09_round_floors_and_fitted_laws.md), [avoid 10](../../../../avoid/10_numerics_ahead_of_the_question.md), and [avoid 05](../../../../avoid/05_same_model_reviews_and_shared_premises.md). This project's outcome does not automatically close the structural shortlist or select its successor.

Read the [avoid index](../../../../avoid/README.md) and [result-summary index](../../../../result-summaries/README.md) before starting or revising this proposal.

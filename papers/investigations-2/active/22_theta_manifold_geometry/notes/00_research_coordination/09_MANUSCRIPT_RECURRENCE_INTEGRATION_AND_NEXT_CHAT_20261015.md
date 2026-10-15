# Recurrence manuscript integration and next-chat continuation

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**. This handoff records manuscript integration and verification, not a new theta sign theorem.

## Current manuscript

The stable [manuscript source](../../manuscript/theta_manifold_geometry.tex) and [43-page reading copy](../../../../../../output/pdf/theta_manifold_geometry.pdf) now include the recurrence findings and their geometric consequences. The [build record](../../manuscript/BUILD_RECORD.json) identifies the final source and PDF. The [integration review](../../reviews/09_RECURRENCE_MANUSCRIPT_INTEGRATION_REVIEW_20261015.md) separates analytic review, exact finite checks and page inspection.

| Location | Integrated result |
| --- | --- |
| Section 7.3 | Exponential-average collision law, complete-start endpoint truncation, and fixed-length mixed-error exclusion with independently chosen cutoff subsequences |
| Sections 9.3–9.4 | Normalized coefficient recurrence, independent-source coupled addition, parity and complete-start endpoint strips; brief cited negative findings |
| Section 10 | Physical beta bound and imaginary anchor, exact recurrence-defect stability, sharp positive finite hierarchy, Gaussian slope-anchor improvement, and the absorption-current approximation |
| Section 11 | Recurrence boundary cokernel, bounded physical observation quotient, degeneration diagnosis, and a sufficient signed boundary-trace estimate |
| Section 12 | Revised open target, proposed joint coefficient/source identity, and the remaining event-coverage requirements |

Negative results are summarized in the manuscript with references to their detailed notes: finite endpoint controls, direct Gram obstruction, normalization cancellation and the narrowly scoped finite-source no-inverse result. The preexisting detailed weighted-square example remains in place. No new manuscript snapshot, commit or tag was created; the working-tree milestone is indexed in [draft history](../../DRAFT_HISTORY.md).

## Where the argument stands

The recurrence experiment gives useful approximation and stability estimates. It does not establish a favorable sign for the complete theta observation. Its finite current moves the unresolved observation to a lower boundary; cancelling that boundary with primitive normalization returns the same unknown quantity as the remainder.

The sharp finite-hierarchy bound is a separate positive result. Positivity, normalization and the recurrence through index \(N\) give \(O(1/N)\) control of physical observations, with finite ramp/spike controls proving the order. Adding \(a_1=1\) removes the affine slope and gives Gaussian beta-tail control. Absolute proximity to theta is not itself a theta sign argument.

The geometric refinement is the signed observation of the complete arithmetic boundary. With \(W=h_j\), \(S=h_{j+1}\), \(E=H^2+H_x^2\), suppose a source-prescribed identity gives

\[
V=AH+BH_x+CS+B_{\partial}+R,\qquad |R|\le\varepsilon.
\]

On complete stationary starts with \(\rho=\sqrt E>0\), the useful remaining target is

\[
\frac{W}{\rho}B_{\partial}\le C_0\rho+\varepsilon_0.
\]

With locally bounded \(A,B,C_0\), this gives the mixed-error chord bound. It is weaker than an absolute bound on the endpoint because a boundary value with the favorable sign need not be small. Both physical orientation and radial vanishing order must be retained.

## Suggested next research step

Begin with the [recurrence experiment](../03_theta_bundles_and_connections/08_ADJOINT_RECURRENCE_ENDPOINT_EXPERIMENT_20261015.md), [geometric boundary note](../01_physical_jet_geometry/01_ARITHMETIC_BOUNDARY_TRACE_AND_SIGNED_OBSERVATION_20261015.md), and [preceding continuation](08_RECURRENCE_EXPERIMENT_AND_GEOMETRIC_CONTINUATION_20261015.md). The broader alternatives remain in [the strategy note](07_RESEARCH_PATHS_AFTER_COUPLED_PRODUCT_20261015.md).

A bounded next experiment would seek a joint coefficient/source identity

\[
r_n(u)=\Delta_nJ_n(u)+\partial_uK_n(u)+\varrho_n(u),
\]

keeping both lower boundaries and every cutoff correction, and aim directly at the signed trace estimate above. Source divergences already appear in earlier work. A useful new result must supply an independent sign or vanishing-order estimate, rather than another representation or a normalization coefficient fitted to the unknown observation.

For the fixed-length criterion, the correct order is: fix a sufficiently small spatial length, fix one sufficiently accurate certified cutoff, then approach the candidate event. Each fixed-index coefficient needs a locally bounded value through that event. There is no required growth rate across cutoffs and no demand for one constant uniform as time tends to zero or spectral height tends to infinity; every positive-time finite-height event still needs coverage. Both stationary branches and the complete starting factor remain essential.

## Verification and history

Five relevant exact checkers were replayed successfully, totaling **12,271 overlapping rational assertions**. The general analytic statements were reviewed separately. The reading copy was compiled and visually inspected; the current [integration manifest](../../numerics/RECURRENCE_MANUSCRIPT_INTEGRATION_CHECKS_20261015.json) binds the source, export, notes, review and checks. Two typographical substitutions in the recurrence note were corrected from `B.0` to `0`; older research manifests retain their historical hashes, and the new manifest records the corrected note's identity.

This conversation remains **formal replay history 20**, titled “Brainstorm theta geometry paths,” thread `01a14023-1225-7d00-8dde-fe9135fa4ca1`, in the [formal replay archive](../../../../formal_replay_crosswalk/chat-histories/0020_2026-10-15T15-16-42Z_brainstorm-theta-geometry-paths.json). Its [history verification](../../numerics/RECURRENCE_MANUSCRIPT_CHAT_HISTORY_VERIFICATION_20261015.json) checks the registry, stored and canonical hashes, original provenance, source correspondence, and completed preceding final messages. The audit precedes this turn's unsent final; a bounded exact-turn capture is arranged after the audit. A new chat should read this handoff and the current build record, and should use its relevant investigation history destination rather than inheriting this conversation's registration.

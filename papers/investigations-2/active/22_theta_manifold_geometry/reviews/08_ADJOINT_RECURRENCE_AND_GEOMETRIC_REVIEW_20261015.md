# Review of the adjoint recurrence experiment and geometric boundary target

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating and reviewing model **gpt-6-astra**, reasoning effort **ultra**. Separate LLM agents audited different derivations and independently replayed the finite checks. This is internal review, not external refereeing or formal verification.

## Finding

The [recurrence note](../notes/03_theta_bundles_and_connections/08_ADJOINT_RECURRENCE_ENDPOINT_EXPERIMENT_20261015.md) supplies explicit endpoint approximation, recurrence-defect stability, and sharp finite-hierarchy bounds. It does **not** establish the favorable signed endpoint estimate. The [geometric note](../notes/01_physical_jet_geometry/01_ARITHMETIC_BOUNDARY_TRACE_AND_SIGNED_OBSERVATION_20261015.md) characterizes that missing boundary observation and proposes a weaker one-sided target. The [continuation](../notes/00_research_coordination/08_RECURRENCE_EXPERIMENT_AND_GEOMETRIC_CONTINUATION_20261015.md) preserves this distinction.

## Analytic audit

- **Finite current and boundary.** The zero coordinate is reset at each application of the killed averaging operator. The second-difference telescoping identity is exact. Both zeroth and first-moment upper boundaries vanish at fixed depth under the stated weighted summability. The reflected transition kernel yields the survival formula, central-binomial bound, and dominated-convergence asymptotic. Parameter-dependent sequences need uniform hypotheses before importing asymptotics in the current depth.
- **Primitive normalization.** The correction identity retains the complete endpoint \(\sum\beta_n=1/2\). Cancelling its boundary contribution leaves precisely the original residual sum, not a small independent remainder. For a fixed residual with nonzero sum the required multiplier grows at the critical \(\sqrt L\) rate.
- **Source-class obstruction.** The no-inverse proposition concerns a finite neighboring-mode range with polynomial/source-jet multipliers and finite real spectral phases, before source integration. Mode independence and first-moment telescoping give the conclusion. It does not exclude source divergences, nonlocal currents, integrated cancellations, or one-sided estimates. Enlarging the range to contain the whole finite target solves the algebra and restores its sum at the lower boundary.
- **Defect stability.** The complete physical mode bound \(|h_{j,n}|\le C_j(T)\beta_n\) is uniform in real spectral position and heat times bounded above. The Gaussian tail Green weights justify the exchanges under \(\sum\beta_n|a_n|<\infty\). The dual defect formula and its two lower traces agree. Gaussian weights alone do not supply a uniform Gaussian remainder for arbitrary normalized coefficient sequences.
- **Finite hierarchy.** Root and a separate agent independently checked the affine-prefix argument. With \(L=N+1\), the exact supremum of weighted distance is \(2R_L+2m_L/L\), approached by finite ramp-plus-spike controls. The physical transform lower example proves the \(1/N\) order is real, not only an artifact of an absolute-value estimate. Adding \(a_1=1\) yields \(2R_L\). The first omitted mode is \(N+2\). No collision property is asserted for these controls.
- **Geometric scope.** The sequence-space cokernel is stated for rapidly decreasing currents with zero lower flux. The quotient-norm proposition applies to homogeneous finite-dimensional relaxations; an affine basepoint requires its own term. Pointwise kernel inclusion does not ensure uniform boundedness at degeneration. First-jet frame comparisons require both the frame and its inverse to stay bounded.
- **Signed target.** With \(S=0\), locally bounded reconstruction coefficients and the proposed signed trace bound imply the mixed-error chord estimate by \(|W|\le\sqrt E\). The trace bound remains an assumption. Its errors must satisfy the existing spatial-scale and cutoff criterion, and the complete stationary branches must retain their coverage.

Separate proof audits confirmed the weighted-defect exchanges, physical mode constant, finite-hierarchy sharpness, sequence-space and finite-dimensional scopes, and signed-boundary implication. Their requested clarifications were incorporated: the normalization growth asymptotic is for a fixed residual; reconstruction divisions require \(\rho>0\); the quotient equivalence requires local boundedness.

## Independent finite replay

The [checker](../numerics/check_adjoint_recurrence_boundary.py) uses only Python's standard library and exact rational arithmetic. The root execution and a separate agent execution both passed **6,892 assertions**. Their mathematical results and script hash agree; execution timestamps differ. The saved [receipt](../numerics/ADJOINT_RECURRENCE_BOUNDARY_CHECKS_20261015.json) records the primary run.

The checks cover dynamic killed walks versus a binomial reflection formula, finite support, central-binomial inequalities, local currents, complete lower traces, first moments, normalization cancellation, polynomial coefficient defect identities, and constructed finite-hierarchy controls. Beta surrogates in those checks are rational test weights, not numerical approximations to the actual theta weights. The infinite-dimensional arguments and actual-source estimates are proved analytically in the notes.

Independent replay receipt SHA-256:
`8729e2428bf42cdff9201f9e61488b3a0b0ba39a9ae834fcf9248c609b0176c2`.
The receipt was produced outside the repository at `/private/tmp/ADJOINT_RECURRENCE_INDEPENDENT_REPLAY_20261015.json`; the persistent manifest records its result and identity. A reuse issue in the assertion counter was corrected before the final replay; two consecutive `run()` calls now return identical counts and results.

## Preserved boundary and next test

The manuscript source remains unchanged, with SHA-256
`114611f06f0928827045399561d2f83ca6ca9abc1d35a9d5cd7d406c845aa417`.
No new draft snapshot or manuscript theorem is introduced. Existing unrelated working-tree changes are preserved.

The finite current approximation is a successful calculation; its proposed use as an automatic signed endpoint estimate fails. A worthwhile continuation would need an independent estimate for the complete signed trace, possibly from a joint coefficient/source identity. General source divergences and physical orientation were already present in earlier work; their reappearance is not new evidence. New geometry must produce a sign or a vanishing-order estimate, not merely another reconstruction formula.

# CCM operator realizations

Started: 26 September 2026.

Start with the [round-9 threshold analysis](notes/CCM_THRESHOLD_ENERGY_OBSTRUCTION_20260928.md), its [sequential review](reviews/CCM_THRESHOLD_ENERGY_REVIEW_20260928.md), and the [program overview](PROGRAM_OVERVIEW.md). The new result is a scoped obstruction: even after exact ground removal, the signed Birman–Schwinger operator has no bounded endpoint in the bare archimedean energy norm. Fixed-prime absolute relative bounds and energy-continuous threshold deflation fail. The one-sided inequality excluding eigenvalues in (0,1/4) remains open.

The [threshold-index handoff](notes/CCM_THRESHOLD_INDEX_CONTINUATION_20260928.md) has been executed. For further work, use Section 8 of the new analysis: a one-sided signed comparison or a new estimate after physical threshold compression is required. Automatic enlargement of the fixed-L certificate remains suspended.

This investigation studies alternative geometric and physical realizations of the Connes–Consani–Moscovici spectral operators. A useful realization should preserve the arithmetic input, account for the Hilbert-space metric, and improve control of the ground state or the normalized spectral determinant as cutoffs increase.

The first continuation derives a finite mechanical system with positive mass and stiffness matrices from the even and odd Weil forms. It also gives an inverse-square spectral trace criterion for compactness of the entire spectral functions and identifies a possible Gaussian contribution from the unmodified Fourier tail in a joint cutoff limit.

The second continuation realizes that mechanical system as a positive point-mass string and gives an explicit unitary map to its graph Dirac operator. Its inverse-frequency trace is exactly the first moment of the reconstructed mass distribution. A common strain space gives a conditional determinant convergence criterion, while cutoff-compression identities and a passive-bath residue obstruction delimit what the realization achieves. Two port choices give the same spectrum but very different string geometry. The general simple-even ground-state condition, arithmetic control of these geometries, and identification of a limit with the Riemann Xi function remain open.

The third continuation tests four prescribed ports through N=32 at fixed L=log13. Smooth and inverse-energy displacement choices do not establish string-tail tightness. It also proves that the integrated mass operator is trace class at fixed support and obtains determinant convergence directly on the Fourier space, conditional on a positive limiting odd-sector gap. That gap is not proved or numerically certified. The new comparison records 1,177 observables agreeing at 45 saved digits between 120- and 160-digit runs.

The fourth continuation proves an explicit infinite-tail bound: at L=log13, the unshifted odd Weil form is at least 2/5 above Fourier mode 4096. An exact rational certificate also shows that a scalar norm Schur test using this bound fails. A finite-rank expansion retains the far coupling with a proved error below 7e-77 in one configuration. The full matrix Schur test and limiting odd-sector gap remain unresolved. The accompanying diagnostics extend to N=64 and agree at 45 saved digits between two precisions.

The fifth continuation completes the bounded infinite-L audit. It proves limitations of the existing scalar trace and separate-prime-norm tail estimates, identifies the full trace as a normalized ground-state second moment, and gives a quantitative prolate comparison target. Approximation of the prolate candidate has a polynomial Fourier-resolution bound; comparison with the actual Weil ground state remains unproved. No arithmetic support sweep or new gap certificate is claimed.

The sixth continuation proves that the Xi kernel and its translates are unconditional Weil annihilators, derives tiny boundary residuals, and constructs positive arithmetic approximate-null profiles with escaping second moments. Hence residual smallness does not select the bottom eigenfunction. A new sufficient RH target is to bound the true even bottom-space overlap with the truncated Xi kernel relative to its residual; full profile convergence is not required for this implication. A bounded multiprecision diagnostic explains why the previous raw residual/second-even-gap test can fail despite high overlap. The original CCM determinant-convergence target remains open. Sonin residuals are deferred.

The seventh continuation derives a cancellation-adapted boundary form and an explicit second-derivative correction to the trial ground. Every fixed derivative rank is eventually positive unconditionally, while all derivatives form a core at fixed support; the order of those limits therefore matters. A bounded Schur diagnostic measures the complement correction. A positive-k transform gives an exact weighted Poincare target with constant 1/4 and shows that any fixed finite-prime truncation of that transformed whole-line form has gap zero. The literal-k normalization Xi/4 is corrected in two earlier supporting notes; normalized conclusions are unchanged.

The eighth continuation proves that the complete prime family restores the exterior threshold 1/4. An exact weighted operator identity gives a stronger superexponential exterior bound without a prime number theorem, local compactness, and discrete spectrum below that threshold. Constants form the simple zero mode; an unspecified positive gap follows unconditionally. RH is equivalent to the absence of any further subthreshold eigenvalues. A fixed-depth compact Birman–Schwinger formulation isolates the remaining uniform threshold problem.

The ninth continuation proves density of the exact threshold profiles in the bare archimedean energy completion, without asserting their completeness in the physical weighted space. Subtracting these profiles from a positive compact witness proves negative divergence of the ground-reduced Birman–Schwinger family and of every fixed prime tail. Physical threshold removal is valid but unbounded in that energy norm; finite removal leaves threshold crowding. This suspends a specific endpoint approximation mechanism, while retaining the one-sided RH target.

## Research record

- [Founding note: metric transport and the chiral realization](notes/CCM_SPECTRAL_OPERATORS_AND_CHIRAL_REALIZATION_20260926.md).
- [Continuation: boundary mechanics and determinant control](notes/CCM_BOUNDARY_MECHANICS_AND_DETERMINANT_CONTROL_20260926.md).
- [Continuation round 2: strings, graph Dirac operators, and cutoff obstructions](notes/CCM_STRINGS_GRAPH_DIRAC_AND_CUTOFF_OBSTRUCTIONS_20260926.md).
- [Continuation round 3: energy-defined ports and the fixed-support limit](notes/CCM_ENERGY_PORTS_AND_FIXED_SUPPORT_LIMIT_20260926.md).
- [Review of the energy-port continuation](reviews/ENERGY_PORTS_AND_FIXED_SUPPORT_REVIEW_20260926.md).
- [Continuation round 4: certified odd tail and structured Schur reduction](notes/CCM_ODD_TAIL_CERTIFICATE_AND_STRUCTURED_SCHUR_20260926.md).
- [Review of the odd-tail certificate](reviews/ODD_TAIL_AND_SCHUR_REVIEW_20260926.md).
- [Continuation round 5: bounded infinite-L audit](notes/CCM_INFINITE_L_BOUNDED_AUDIT_20260926.md).
- [Review of the bounded audit](reviews/INFINITE_L_BOUNDED_AUDIT_REVIEW_20260926.md).
- [Continuation round 6: the ground-selection target](notes/CCM_GROUND_SELECTION_TARGET_20260928.md).
- [Xi annihilator and explicit boundary-residual estimates](notes/CCM_XI_ANNIHILATOR_AND_BOUNDARY_RESIDUAL_20260928.md).
- [Near-zero clusters, escaping moments, and the overlap criterion](notes/CCM_NEAR_NULL_CLUSTER_AND_GROUND_SELECTION_20260928.md).
- [Review of the ground-selection continuation](reviews/CCM_GROUND_SELECTION_REVIEW_20260928.md).
- [Bounded Xi-proxy diagnostic](reviews/CCM_XI_GROUND_DIAGNOSTIC_20260928.md).
- [Continuation round 7: boundary selection and the complement](notes/CCM_BOUNDARY_SELECTION_AND_COMPLEMENT_20260928.md).
- [Derivative boundary-selection proof](notes/CCM_DERIVATIVE_BOUNDARY_SELECTION_20260928.md).
- [Complement, form-core, and weighted-gap proofs](notes/CCM_COMPLEMENT_DENSITY_AND_WEIGHTED_GAP_20260928.md).
- [Review of round 7](reviews/CCM_BOUNDARY_SELECTION_REVIEW_20260928.md).
- [Independent derivative-cluster diagnostic](reviews/CCM_DERIVATIVE_CLUSTER_DIAGNOSTIC_20260928.md).
- [Continuation round 8: full weighted tail and discrete obstruction](notes/CCM_WEIGHTED_TAIL_AND_DISCRETE_OBSTRUCTION_20260928.md).
- [Weighted operator, essential edge, and localization](notes/CCM_WEIGHTED_OPERATOR_SPECTRAL_REDUCTION_20260928.md).
- [Prime return and exterior coercivity](notes/CCM_PRIME_RETURN_AND_EXTERIOR_COERCIVITY_20260928.md).
- [Review of round 8](reviews/CCM_WEIGHTED_TAIL_REVIEW_20260928.md).
- [Bounded prime-return diagnostic](reviews/CCM_PRIME_RETURN_DIAGNOSTIC_20260928.md).
- [Continuation round 9: threshold energy and deflation obstruction](notes/CCM_THRESHOLD_ENERGY_OBSTRUCTION_20260928.md).
- [Sequential adversarial review of round 9](reviews/CCM_THRESHOLD_ENERGY_REVIEW_20260928.md).
- [Executed threshold-index handoff](notes/CCM_THRESHOLD_INDEX_CONTINUATION_20260928.md).
- [Concise milestone index](DRAFT_HISTOR.md).
- [Numerical reconstruction and checks](numerics/README.md).
- [Initial derivation check](reviews/INITIAL_DERIVATION_CHECK_20260926.md).
- [Critical review of the string realization](reviews/STRING_REALIZATION_CRITICAL_REVIEW_20260926.md).
- [Separate investigation: fractal Laplacians and geometry changing with scale](../ccm-fractal-laplacians/README.md), starting directly from the mass–stiffness pair, with resistance-form trace bounds and an explicit logarithmic-growth control.

The founding note was copied from `papers/susy-positivity/investigations/wilson-loewner/notes/`. Its only change is the relative link to the earlier project bridge sweep, adjusted for the new location. The original remains in place.

Incremental research belongs in `notes/`, numerical programs and small records in `numerics/`, and reviews in `reviews/`. No manuscript or draft snapshot is part of this initial investigation. The repository's [large-file policy](../../../LARGE_FILES.md) applies.

## Next research question

The sharp one-negative-direction inequality is still the target. Round 9 rules out obtaining it through a bounded endpoint sandwich, an absolute A_0-relative bound for a fixed prime tail, or energy-continuous removal of the full known threshold span. These failures occur on the signed operator's negative side and do not disprove the desired upper bound.

Further work should begin with a concrete one-sided signed factorization, or a comparison on the physical complement of the known threshold modes that controls all form vectors. The [analysis, Section 8](notes/CCM_THRESHOLD_ENERGY_OBSTRUCTION_20260928.md#8-decision-and-next-useful-input) specifies the exact missing inequality. Prime and spatial schedules at positive depth alone do not certify the endpoint inertia count; the error ledger states their limits. No numerical sweep is the default.

The earlier ground-overlap criterion and CCM determinant limit remain unproved. Sonin residuals remain deferred.

# Projected flow manuscript integration and collision scope

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**, chat0008.

**Status: same-assistant internal assessment.** This reviews the integration of Notes22–25 into the existing manuscript and the change from fixed radial integrands to total-integral conservation. It is not independent specialist review.

## Mathematical findings and scope

1. **Projected baseline.** The manuscript gives the actual equation with Q_t expanded as the complete theta sum. It defines the formerly implicit χ_out as a freely selected spatial penalty. The annular coercivity constant, semigroup solution, dissipation and strict decrease relative to the initial source cost are retained. Monotonicity is claimed for the full energy, not separately for the source cost. Positive-time smoothing is separated from initial boundary compatibility.

2. **Complete response.** The zero-extension surface term and the whole-exterior weak elliptic response remain distinct. The projected operator is openly nonlocal in angle. Its spectral derivative has forcing −ψ/r², not −f_s/r². The signed current contains the projected-potential term; the local adjoint and complementary cutoff flux remain present. The theorem does not sign their coupling.

3. **Direct theta application.** Note24 passes the full theta sum through the bounded solution operator and bounds finite forcing truncation with its actual angular-variance factor. Retaining the exact radial background preserves the original observation even when only the auxiliary forcing is approximated. A notation error in the angular-variance integral was corrected to include its differential. No theta PDE simulation was run or represented as having been run.

4. **Simplification and the new invariant.** Dropping the drive from the earlier zero-start perturbation equation leaves G=0. That conclusion is correctly restricted to that initial-value problem. Under the user's relaxed requirement, the full signed density may diffuse nontrivially while its entire integral stays fixed. The fixed-kernel uniqueness observation applies only to a frequency-independent source tested at every real frequency; it is not an obstruction to evolving the full density or source and phase together.

5. **Conservative heat construction.** The factor 32π in the initial three-dimensional density reproduces the original 1/8 radial integral. The theta tail gives L¹ initial data, finite parameter derivatives and all required spatial moments. Gaussian convolution proves mass and jet conservation by Fubini, commutes with the physical heat law, and applies termwise to the theta sum. The full-space domain includes the initially empty ball after diffusion. No exterior-only conservation or classical initial compatibility across r=1 is claimed. The differential equation is local, with infinite propagation and Gaussian spreading.

6. **Central collision diagnostic.** Expanding exp(−|X|²/(4εs)) gives the signed second-moment coefficient and the absolute fourth-moment remainder 1/(32ε²s²). Vanishing of H and H_a removes both s^(−3/2) leading terms at the spatial origin, giving O(s^(−5/2)); the general nonzero component retains its nonzero s^(−3/2) coefficient. This is a precise faster-decay statement, not an amplitude-growth theorem, an all-space asymptotic, or an all-height uniform bound.

**Source-cost decrease and loss of a leading diffusion mode are not, by themselves, a collision-excluding estimate.** The first approach's no-gain result is scoped to its fixed-width, axisymmetric multiplicative Wronskian comparison. The manuscript refers its full details to the notes and gives the second approach and conservative extension the main development.

## Control screening

The exact Gaussian-polynomial control at (T_c,2√6) has all required spatial moments on t<T_c+4. It satisfies the generic heat theorem and has the same double loss of leading diffusion coefficients at its actual collision. No premise of that theorem fails for it; it fails the full canonical theta-source premise.

The smooth Euler-factor, weighted-square, finite-prime, reflected super-Gaussian and positive-primitive controls retain their observations on the applicable convergence and moment domains. Their missing theta arithmetic/reflection inputs are recorded in the [control register](../../../../result-summaries/12_collision_controls_and_screening.md). None is excluded by this generic mechanism, and no old certificate was rerun. Atomic sources are outside the density formulation stated here. A future separating estimate must establish its extra canonical premise and actual effect.

## Manuscript and verification record

The existing source was revised in place. Its author and substantial LLM acknowledgment remain. Sections1 and9 distinguish the weaker general invariant from the older stronger subclass; Section10 develops the projected flow and response; Section11 gives conservative heat and its diagnostic; Section12 states the remaining dynamics question. The first multiplicative approach is summarized with Notes20 and22 as the detailed sources. The earlier Darboux sections and inherited moment appendix retain their scope.

Classical PDE inputs were checked in the primary author notes listed in reference annotation10, including Hunter's explicit heat kernel and L¹ initial-data statement. The conservation and central remainder calculations are written proofs. Record14's earlier exact/floating diagnostics remain limited to manufactured algebra and geometry.

The saved source compiled successfully with the desktop editor’s compiler. All source label/citation references and local links were checked, and the whitespace/diff check passed. [Record15](../numerics/15_PROJECTED_AND_CONSERVATIVE_MANUSCRIPT_BUILD_RECORD_20261027.json), finalized 28 October 2026 local date, records the source hash and exact compiler response. The app queued the existing source for its preview; automated access to the app itself was disallowed, so visual page-layout inspection was not completed. No PDF page count or exported PDF hash is asserted. No separate manuscript PDF build was made.

The [result index](../../../../result-summaries/README.md), [avoid index](../../../../avoid/README.md), [target classification](../../../../avoid/01_restating_the_target.md), [geometric-realization caution](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), and [scoped-exclusion rule](../../../../avoid/07_scoped_exclusions_read_as_universal.md) were used. The new objective and weaker invariant supersede the earlier program priority, while earlier results and historical milestone entries are retained.

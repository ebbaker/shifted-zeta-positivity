# Audit: arithmetic orbit weights and the Bost–Connes test

23 September 2026. Prepared for Edward Baker with LLM assistance.

**Reviewer/model:** GPT-6 (Codex; developer-provided identity).  
**Effort:** not exposed; not inferred.  
**Review type:** same-assistant mathematical and numerical audit, not an independent specialist review.

**Artifacts:** [research note](../notes/ARITHMETIC_ORBIT_WEIGHTS_AND_BOST_CONNES_TEST_20260923.md), [program](../numerics/check_arithmetic_orbit_weights.py), [record](../numerics/records/arithmetic-orbit-weights-20260923.json).

## Assessment

The coefficient identity is exact, and the Bost–Connes thermal system is an independently motivated source of the primitive probabilities. The note correctly stops short of identifying the resulting expectations with a causal scattering response. Its two norm limitations apply to explicitly stated constructions: the bare Euler impulse train and the naive product half-density embedding. Neither is presented as a general impossibility theorem.

## Checked derivations

1. **Arithmetic normalization.** Expanding each Euler factor gives c_(ell^r)=(1-ell^(-2 omega))ell^(r(omega-1/2)). Multiplicativity gives the full coefficient law. At half shift this reduces to phi_E(n)/n; differentiating c_2 gives (3/2)log 2. Differentiating log Z gives the prime part of minus a_omega, with the correct sign and prime-power multiplicity. The gamma and rational completion is stated separately and is not supplied by these coefficients.

2. **Thermal source.** With sigma_t(v_n)=n^(it)v_n, the KMS identity yields phi_beta(v_n v_n^*)=n^(-beta). The commuting divisibility projections multiply by lcm, so finite inclusion-exclusion yields the primitive expectation without assuming independence. The equivalent local geometric law supplies a positive finite-place Gibbs model for every beta>0. The established infinite-system KMS state at 0<beta<=1 is distinguished from the divergent global Gibbs trace. The note cites Neshveyev's primary treatment for this existence and local measure structure.

3. **Unresolved centering and time interpretation.** The factor n^((beta-1)/2) is explicit. The B_(n,beta) observables are contractions in the stated interval but vary with temperature. Formula (11) rewrites the centering using analytic imaginary time; it is not a unitary evolution or an implemented input/output interface. Native P correlations are stationary. The real-time log n energy label is not silently promoted to a flight delay. These are substantive remaining gaps, not notation choices.

4. **Local ordinary norm.** Integrating the radial density over valuation shells gives total mass one on Z_ell and the primitive unit probability. The half-density transport conjugates weighted dilation to Haar dilation; its local correlation is ell^(-beta|r|/2), distinct from the requested Euler coefficient. No norm is defined by pulling back the desired transfer.

5. **Infinite-place scope.** The local affinity is a convergent geometric shell sum. For fixed beta<1 its leading deficit is (1/2)ell^(-beta); divergence of the prime sum makes the naive finite-product vectors non-Cauchy in the Haar-based incomplete tensor product. The shift-tangent calculation includes the factor d beta/d omega=2 and has no cross terms. This does not invalidate abstract KMS states or prove disjointness of all possible physical radiation representations. No statement about other project-specific semilocal embeddings follows from it.

6. **Bounded pulse exclusion.** The selected window and pulse support contain disjoint direct and first-delay copies, with no later arithmetic copy. Their ordinary squared norms add to 1+c_2^2. This excludes the uncompleted Euler response as a contraction. The note explicitly retains the archimedean factor as essential, including at the known modular half shift, so the test does not mistakenly exclude that benchmark.

7. **Geometric twist scope.** The S^2=R^3=1 relations give six scalar characters; imposing trivial cusp holonomy leaves only the trivial character. The shifted Fourier potential explains loss of the open constant cusp mode otherwise. This argument concerns scalar flat bundles on the original modular surface and does not classify more general couplings.

## Numerical evidence

The completed run reports **87 passing cases: 17 exact integer and 70 floating**. Exact cases enumerate primitive tuples in dimensions 1, 2 and 3 for moduli 2, 3, 4 and 6; divisibility-projection products are checked on integers; scalar character phases are enumerated modulo 6. These are exact finite controls, not a computer proof of all moduli or the group presentation.

Floating calculations compare the product coefficients with a Möbius convolution, compare a full zeta quotient with its truncated Dirichlet series under an elementary positive tail bound, and compare a differentiated finite Euler product with the prime-power source series. Independent shell integrations reproduce state norms, affinities and actual dilation correlations. Differentiated amplitudes reproduce tangent norms. A piecewise pulse integral reproduces the norm excess. The large-prime table illustrates the analytically established product limitation.

The run uses Python 3.10.0, mpmath 1.3.0 and 50 decimal digits. Shell sums stop at occupation 360; the Dirichlet sum at 1,500; the prime table at 100,000. No interval arithmetic or zero table is used. Passing cases mean the identities and specified exclusions were reproduced, not that the physical realization succeeded. The source program hash is stored in the record.

## Remaining research boundary

A two-prime arithmetic sector has an explicit positive Hamiltonian and usable native projections. What is absent is a coupling that derives physical delays, centered amplitudes and the variable archimedean factor together with the ordinary radiation-energy balance. The next experiment should address that finite interface before assuming an infinite tensor product. Its success cannot be judged solely by a designed transfer equal to the arithmetic target.

This audit is not a proof checker and makes no RH claim. Earlier numerical suites, manuscript TeX and PDFs are outside the changes in this research addendum.

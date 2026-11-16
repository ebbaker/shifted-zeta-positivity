# B04 pass 1 — joint midpoint information and its finite-data test

16 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex assistance. Lead actual model/effort unavailable in the current archive; not inferred from the Astra/ultra recommendation. Supporting fixed E tasks explicitly dispatched gpt-6.1-sol/ultra, with separate backend attestation unavailable. Research chat0003.

**Decision, not a zero theorem.** Read the [result index](../../../../../result-summaries/README.md), [cluster18](../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md), [control catalog12](../../../../../result-summaries/12_collision_controls_and_screening.md), [avoid index](../../../../../avoid/README.md), and patterns [01](../../../../../avoid/01_restating_the_target.md), [02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md), [07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md), and [12](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md). The existing unspecified shrinking-strip target is already classified; no checks of it are proposed.

## Two concrete formulations

Fix the complete source at lambda=0, its normalized measure mu, canonical score V'=8πsinh(4u)+b(u), and the literal Fourier observation F. All c_n(z) below are full-chain midpoint amplitudes, not finite-matrix approximations.

1. **One common memory for both midpoint terms.** Use the same modeled scalar tail response k_N in the finite Volterra equation for c_0,...,c_(N-1) and the bilinear Duhamel expression for the omitted sum. E13 audits the domains and half-height factors. This preserves the necessary correlation between the two errors. The complete source is a member by its exact Duhamel equations, and a sufficiently controlled model would have the ordinary signed consumer |G|>|F-G| on a specified zero-free region, or Rouché on a contour. Neither an approximate k_N, its source-sensitive allowance, nor a signed margin has yet been supplied. The inward recursion and an exact unknown k_N are not a forward/terminal argument. Generic kernel symmetry, positive definiteness and these equations hold for the relevant collision controls with their own coefficients. Keeping a common kernel is essential bookkeeping, not a discriminator.

2. **Finite canonical calibration of that joint description.** In addition to a finite coefficient prefix and tail Taylor coefficients, retain finite exact matrix elements of BOTH V' and the actual canonical bounded function b; add finite complex-height jets of the retained full-chain midpoint amplitudes. This is stronger than E10 and tests the new midpoint information directly, rather than merely repeating the next-defect construction. Candidate claim: such finite data determine the omitted complex contribution or force a new exact signed restriction on its deviation from the canonical value. The true theta measure is a member by construction. The next issue is whether these constraints actually distinguish its omitted contribution in the smooth same-tail class.

The first formulation remains a useful exact interface. The second is selected for the bounded E12 diagnostic below. Its theorem is a local information-freedom statement, not a theorem that these controls have nonreal zeros, not a rejection of absolute enclosures, and not a rejection of increasing-degree compact confinement. Full functions differ decisively from finite samples: c_0(z)=F(z/2) as a function already determines F everywhere.

## Frozen analytical question for E12

For any finite L>=N>=1, derivative order r>=0, and z*=x+iy with x nonzero and 0<|y|<4, ask whether two smooth even compact multiplier directions can preserve:

- moments through degree 2L, hence q_0,...,q_L and a_1,...,a_L;
- every canonical V' and b matrix element with indices at most L;
- c_n^(j)(z*) for n<N and j<=r;

while the literal F(z*) varies over a complex neighborhood of its canonical value. With the midpoint data fixed, the variation is exactly the variation of R_N(z*). Prefix equality also fixes the corresponding finite list of disconnected tail moments; the precise indexing is to be proved. The sources must remain positive and smooth, agree with theta near zero and on both tails, obey the existing envelope, and have arbitrarily small own-to-canonical score difference.

Route: extend E10's finite-test duality to two target functionals. On positive u, any real dependence has the form Re(alpha cos(z*u)) = P(u)+V'(u)Q(u)+b(u)S(u)+a finite half-frequency exponential-polynomial sum. V' grows like 4πe^(4u), whereas target and half-frequency terms grow like e^(|y|u) and e^(|y|u/2). First force Q=0; then a nonzero oscillatory target cannot equal the slower terms. Rank two on the joint kernel produces fixed h_1,h_2 and an invertible two-dimensional response. Bounds on their sup norms and first derivatives give a strictly positive but not uniform achievable disk. No estimate of that radius as L,r grow or y tends to zero is claimed.

The test retains the canonical b FUNCTION in the test symbols, rather than replacing it with an independent norm allowance. A perturbed source's own score is still different pointwise. Thus success would reject finite testing of b, not exact pointwise equality to b or its full functional action.

## Control premises and future updates

The E07 finite square controls have nonreal zeros but eventually lose smooth reflection; the new tests have not been imposed on them. E10 is the smooth construction template, whose zeros remain open; E12 must prove its stronger preservation afresh. Euler translates fail the unchanged source and exact real tails. Weighted-square and finite-prime controls fail full canonical reflection; the reflected super-Gaussian fails the exponential score reference and theta tails. Smooth/primitive controls lack the canonical arithmetic square expansion. Atomic and compact triangular sources fail strict positive full-line density; variable-observation controls fail the literal Fourier readout; the actual-profile relaxation provides no such source/readout. RH-conditional endpoint controls fail ordinary Dirichlet arithmetic. See the catalog and E07/E10 for their exact scopes: these are premise comparisons, not reruns of collision certificates or assertions that every quantitative bound must reject every control in every region.

A finite calibration step, if E12 succeeds, cannot serve as an exact predictive update in this enlarged smooth source class. The potentially distinguishing premise remains a quantitative constraint using the complete canonical arithmetic/pointwise score jointly with memory, with an actual signed consumer. Requiring the full canonical score at every test identifies the source by E08, but source identification alone is not a zero estimate. The next pass should retain the shared-memory correlation explicitly rather than split its two errors into independent worst cases.

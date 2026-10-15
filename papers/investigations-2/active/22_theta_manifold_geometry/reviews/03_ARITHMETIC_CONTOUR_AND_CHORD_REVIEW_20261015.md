# Review of the arithmetic, contour and chord continuation

15 October 2026. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6-astra**, reasoning effort **ultra**. This is internal multi-agent mathematical review with coordinator replays, not external refereeing or machine formalization.

## Disposition

The continuation provides a stronger sufficient collision-exclusion target, a certified counterexample to a stated arithmetic relaxation, a rigidity theorem identifying omitted theta information, and a complete contour identity with a precise sector-cost obstruction. None supplies the missing theta-specific signed estimate. The stable manuscript and its build identity are unchanged.

## Chord criterion

The pi/4 product has the claimed angle interpretation only at a full stationary start and on an interval where W=h_j never vanishes. Those hypotheses are explicit. Starting-point physical energy is used for both branches; the odd branch is not normalized by an endpoint jet energy.

The parabolic expansion gives a negative inverse-square-root pole for C/E(start). More strongly, the analytic change of variables eta=sqrt(T-t) shows that the leading positive even heat polynomial dominates the higher-order Taylor remainder in a fixed neighborhood. This proves interval-wide sign preservation up to a fixed small endpoint. Its endpoint factor W-W_x has the sign opposite to W(start), yielding a strictly negative limit for C/sqrt(E(start)). This justifies the all-multiplicity criterion with error o(sqrt(E)). Multiple collaborators checked the fixed-endpoint argument independently.

The all-N transfer keeps its coefficients prescribed before selecting a cutoff. Integer rounding and the cutoff threshold are included. The chord-specific Gaussian extension requires a uniform local gap a_*<c_0; it is not an unrestricted beta=2 theorem. The exact quadratic example verifies the need for a strict condition and separately rejects replacing starting energy by endpoint energy. Finite polynomial replays exercise both branches, asymmetric germs and both amplitudes; they do not prove the arbitrary-multiplicity analytic theorem by enumeration.

## Arithmetic relaxation

The three weights are fixed once the unique Wronskian root is selected at T=1/4. No time-varying source is introduced. The construction imposes Phi'(0)=0 algebraically before root isolation. Arb/Acb endpoint signs and a uniformly signed Wronskian derivative certify existence and uniqueness of the root in the declared bracket. Uniform second-derivative bounds certify a nondegenerate double zero. The finite integration, absolute source tail and spatial interval extension were audited separately.

Every support-only localizer is nonnegative by its sum representation at the positive square nodes, at every degree and every q>0. This property is analytic and not inferred from testing finite matrices. Positive common scaling restores psi'(0)=-1/2, and Phi'(0)=0 then gives psi'''(0)=-1/2. The certified failure of Phi'''(0)=0 identifies the next missing condition. The even extension of the half-line control is only C²; claiming that it is a smooth even theta source would be false.

The perturbation to positive weights on every square is an implicit-function argument with a nonzero Jacobian. Its existence assertion is accepted without an explicit numerical perturbation radius. This obstruction applies only to the stated relaxed class; a certificate using the actual coefficient values or full reflection has additional information and is not ruled out.

An independent collaborator replayed the frozen three-mode checker, and the coordinator replayed it again. The mathematical enclosure fields match; elapsed runtime is not treated as reproducible data.

## Reflection rigidity

The weighted comb is tempered under the explicitly stated polynomial-growth assumption. Gaussian modular reflection makes its difference from its Fourier transform annihilate every Gaussian. Differentiation gives all even Gaussian moments, parity gives all odd moments, and an entire Gaussian generating function proves distributional equality. Fourier periodicity then forces the integer weights to be constant.

The passage from even physical source to modular reflection retains the homogeneous sinh contribution. It is removed by the normalized primitive endpoint and a0=1, not silently discarded. The resulting uniqueness of theta in the declared class provides an arithmetic discriminator, not positivity of the physical transform. The finite polynomial checker verifies algebra used in the argument; it does not certify the distribution theorem.

## Contour packet

The base coordinate change, logarithm branch, downward bottom-edge orientation and vanishing upper edge agree. Every shifted heat, phase and source factor remains. The directed mixed chord terms are distinct and are both retained. Sector stationarity is never imposed; the full stationary equation is a cancellation between sectors.

The endpoint coefficient is nonzero for positive square weights. Its two sector contributions have opposite leading signs. The separate Laguerre expressions lose their first rank-one term but retain an exponentially large x^-4 term; the actual pi/4 product has a different x^-2 term and is not confused with a Wronskian chord. These are complex sector expressions, not individually ordered real quantities.

The growth result rejects independently paid polynomial-height sector estimates. It does not itself rule out a finite-height estimate whose coefficients are only locally bounded, nor an estimate retaining all cross-term cancellation. Spectral height x is distinct from the cutoff N. These limitations are explicit in the note.

The 192-bit contour replay uses complete series and ray tails. The endpoint coefficient used in asymptotic ratios is also inflated for omitted theta modes. Finite identity-enclosure tests are consistency checks with rigorous integral bounds, not proofs of the unbounded asymptotic theorem or of theta chord signs. The coordinator independently replayed the final checker.

## Research decision

Promote the chord with starting-energy payment to the preferred target. Stop the support-only hierarchy and independent contour-sector payment in their tested forms. A next attempt must introduce a coefficient relation that rejects the certified control and show how it benefits the complete signed observation. The execution manifest records the exact verification scope and file identities; hashes do not validate mathematical assertions.

See the [handoff](../notes/00_research_coordination/04_ARITHMETIC_CONTOUR_AND_CHORD_CONTINUATION_20261015.md) and [execution manifest](../numerics/ARITHMETIC_CONTOUR_CHORD_CHECKS_20261015.json).

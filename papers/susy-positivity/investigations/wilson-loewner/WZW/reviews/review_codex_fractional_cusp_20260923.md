# Same-assistant audit: continuous exponent and fractional cusp test

23 September 2026. Prepared for Edward Baker with LLM assistance.

**Model:** GPT-6 (Codex; developer-provided identity).  
**Effort:** not exposed; not inferred.  
**Review status:** same-assistant analytical and numerical audit, not an independent specialist review.

Reviewed artifacts: [research note](../notes/CONTINUOUS_EXPONENT_AND_FRACTIONAL_CUSP_TEST_20260923.md), [program](../numerics/check_fractional_cusp.py), and [record](../numerics/records/fractional-cusp-20260923.json).

## Findings

The candidate changes the leading exponent continuously and reproduces its required amplitude after one stated global time calibration. It fails the complete transfer test. The strongest exclusion is analytical: a nontrivial scalar complete-Bernstein clock moves every nonzero boundary frequency into the open right half-plane, where the nonconstant modular inner function has modulus below one. This cannot equal the arithmetic unit-modulus boundary response. The result is limited to scalar clock composition.

1. **Geometric controls have limited scope.** Uniform rescaling retains exponent one half and moves delays. Integer raising multiplies the Hodge response by a finite product tending to one, also retaining its exponent. The note does not generalize these controls to arbitrary cusp metrics, real-weight multiplier systems, or all field deformations.

2. **The memory field is independently specified.** The weighted diffusion equation contains no primes or zero data. Its Bessel solution yields the fractional admittance, with the flux coefficient derived explicitly. Integration by parts gives a positive energy and dissipation identity. A second, positive relaxation integral reproduces the admittance. The weight is part of the material model, not a norm imposed using the desired transfer.

3. **Normalization and endpoints are disclosed.** The scale 2 pi is a favorable leading-amplitude calibration. It is not advertised as a new geometric derivation of the arithmetic normalization. The weighted field degenerates at beta=1; recovery of the original channel is an admittance/response limit. The zero-order endpoint is separately checked and fails the arithmetic identity limit.

4. **The assembly claim is deliberately bounded.** S_beta=K composed with psi_beta follows from the stipulated common spectral-clock replacement. This is a driven, zero-initial-state problem, so no initial-data factor p^(beta-1) appears. The note does not claim a completed local fractional theory on the modular quotient with unchanged free asymptotic ports. That construction would need additional work. The response being tested is explicit and already fails, independently of whether such an assembly can be completed. This limitation matters: positivity of a constituent diffusion field alone is not a proof of a new modular scattering realization.

5. **Front matching is substantive but insufficient.** The leading term has exponent beta/2 and amplitude (2 pi)^(beta/2). The native next relative term is nonzero and has order p^(-beta), whereas the arithmetic next term has order p^(-1). The derivative at beta=1 matches the leading logarithm but differs at finite frequencies. Matching the exponent fixes domega/dbeta=1/2; a second independent clock adjustment is not available to cure those differences.

6. **Causality, contraction and arithmetic matching are separated.** Composition with the positive clock maps the right half-plane into itself, proving a causal contraction on ordinary signal L2. This is a response-level statement. Boundary attenuation follows from strict interior contractivity. The arithmetic boundary-modulus equality uses the functional equation alone and makes no RH-dependent assertion of full-family causality. Finite-window loss includes both spectral attenuation and future output; the note does not present it as a separately evaluated coupled-field storage integral.

7. **The general clock argument is elementary and scoped.** For a complete-Bernstein representation, the real boundary part is a plus an integral of nu^2/(r^2+nu^2) against a nonnegative measure. It vanishes at all nonzero frequencies only when the constant and measure vanish. Pure drift then keeps exponent one half. The zero clock is a degenerate identity response, not a missing variable-order family. This excludes neither coherent matrix channels nor all possible couplings to passive media.

8. **First-delay comparisons use like quantities.** The stable delay density is normalized and has a verified Laplace transform. Its early-arrival probability is identified as a probability, not an energy fraction. The signed first-prime response is evaluated separately by convolution with the original archimedean kernel. It is already nonzero before log 2 and remains finite there, while the arithmetic first-prime increment diverges. The table compares those n=2 contributions, not full responses. Gaussian domination also justifies smoothness of the complete subordinated kernel, so a later-term cancellation cannot recreate the missing front.

9. **Additional obstructions are independent.** The low-frequency fractional branch uses the explicit nonzero derivative K'(0)=log(4 pi)-2-gamma. The zero-order limit is a constant about 0.7601621, not identity. The restriction on changing only an archimedean factor is a fact about the unchanged Euler coefficients, not a claim that every geometric deformation factors that way.

## Numerical and provenance audit

All 80 controls pass, all floating. They include independent ODE, flux, relaxation-integral, energy, Laplace-density and parameter-derivative comparisons; asymptotic exclusions are also tested at finite points. The first-prime integral is repeated at 15 additional decimal digits. No imported zero table, Monte Carlo sampling or interval arithmetic is used.

The program depends only on mpmath and the Python standard library and records its own hash and dependency version. It does not import the earlier numerical programs; the arithmetic prime-free formula is evaluated through the incomplete-beta expression established in the previous corrected note. Existing programs and records remain unchanged. Passing controls support reproducibility of the specified test, not an independent proof review or an arithmetic realization.

The next investigation should derive a unitary change of native arithmetic orbit weights at fixed delays. A fractional front by itself is no longer sufficient reason to develop a candidate further.

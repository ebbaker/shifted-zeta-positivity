# Same-assistant audit: modular Hodge scattering and cusp coupling

23 September 2026. Prepared for Edward Baker with LLM assistance.

**Model:** GPT-6 (Codex; developer-provided identity).  
**Effort:** not exposed; not inferred.  
**Review status:** same-assistant analytical and numerical audit; not an independent specialist review.

Reviewed artifacts: [research note](../notes/MODULAR_HODGE_SCATTERING_AND_CUSP_COUPLING_TEST_20260923.md), [diagnostic](../numerics/check_modular_scattering.py), and [65-case record](../numerics/records/modular-scattering-20260923.json). The two corrected sibling programs and their complete replays are also included in scope.

## Findings

The positive result is restricted to the half-shift response. The scalar constant term, exact one-form operation, amplitude convention, polar isometry, and known fixed-shift innerness together provide a geometric causal radiation channel with the required transfer and ordinary norm. A variable-shift physical family is not obtained. The chosen real cusp load is excluded by analytical tangent asymptotics, independently of numerical zero samples.

1. **Completion and geometry.** The scalar parameter is sigma=(p+1)/2, and the raw exact one-form ratio is (1-sigma)phi/sigma=-K. The displayed transfer therefore includes one fixed outgoing sign convention. Taking d kills the constant scalar state; projecting out that state without changing the channel would not by itself change the scalar scattering coefficient. The scalar residue 6/pi and finite completed value 3/pi agree.

2. **Positive norms and propagation.** The normalized gradient J=d Delta_0^(-1/2) is a partial isometry by d*d=Delta_0. Its incoming and outgoing factors have modulus one on the continuous spectrum. The note restricts the shifted wave generator to the exact absolutely continuous radiation sector, identifies wave frequency rather than Schrödinger energy with the propagation variable, and explicitly gives the unitary time dilation. It does not equate arbitrary field-smearing norms with radiation norms. Fixed-shift innerness is cited as an established input; it is not inferred from boundary modulus alone. The full-family RH-equivalent condition remains unresolved.

3. **Arithmetic origin and finite windows.** Primitive modular residue classes yield the totient weights, while the cusp integral yields the gamma factor. The derivative channel supplies the rational completion. The first delay is consequently native to this geometry. The closed half-shift kernel and its cumulative integral agree with independent Laplace evaluation. The unit-window output norm is about 0.9472441696; future energy is obtained from proved conservation, not presented as an independent integration of all later prime delays.

4. **Specified coupling.** The physical port is q=1, not a chosen prime length. The delta interaction acts on the angular-average vertical channel, with other modes unchanged. It is not described as a point scatterer on the surface. Continuity and the real derivative jump give the loaded response, with the original sign convention preserved. An independent two-by-two matching solve reproduces it. The analytic denominator and passivity identity prove the causal lossless properties for alpha>=0. The common reference delay appears on both sides of the arithmetic comparison. The b=0 calculation is clearly an algebraic favorable control rather than the selected regular cross-section.

5. **Tangent exclusion.** Differentiation gives D_b=(1-exp(-bp)K)^2/(p exp(-bp)K). Its large-positive-p behavior is exponential divided by sqrt(p) for b>0, and inverse sqrt(p) at b=0, rather than the arithmetic logarithm. No constant nonzero arithmetic clock repairs this. Transfer tangents also have incompatible wavefronts. At the first prime delay the load increment vanishes like sqrt(epsilon), while the arithmetic increment diverges like epsilon^(-1/2) log(epsilon). These are bounded local comparisons; no contour deformation through unknown poles is used.

6. **Pole diagnostic and limitations.** The residue formula explicitly assumes a simple zero. Two locally solved roots illustrate the mismatch but are not certified locations or an RH test; no imported zero table is used. Multiple zeros are not assumed absent. The proof of exclusion does not depend on these samples. The result excludes the specified real delta load and clock comparison, not arbitrary changes of geometry, field content, or additional channels.

## Correction and replay

Both previous continuation programs used exp(-2v) where the transformed prime-free correction integral requires exp(-(3-2omega)v). The earlier written convolution formula was correct. The bug vanishes at half shift and leaves the leading near-origin singularity unchanged, explaining why the earlier finite controls did not expose it. Their previously passing status was therefore not sufficient evidence for the implemented general-shift kernel.

The corrected programs were fully replayed: 60 bounded-readout cases (13 exact rational) and 51 Brownian floating cases pass. The bounded audit's forward-cell value changes to 0.11571873508141131. The Brownian note's two displayed arithmetic scaled increments are updated. Native Brownian quantities, prior analytical exclusions and parent manuscript calculations are unaffected. The historical audits now carry explicit correction notices.

The new 65-case suite includes 5 exact rational counts and 60 floating checks. Independent incomplete-beta comparisons at three shifts, away from the origin, test both sibling implementations; general-shift Laplace integration supplies an additional reference. The record stores all three program hashes and dependency versions. These controls are not interval certificates, an independent review, or a proof of an arithmetic shift realization. Specialist review of the geometric radiation dictionary is a useful next quality check before promoting the fixed-shift result into a manuscript.

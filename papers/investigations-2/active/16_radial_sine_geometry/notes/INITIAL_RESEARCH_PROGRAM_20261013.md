# Initial research program for radial geometry and sine moments

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6.1-sol (`gpt-6.1-sol`), Codex; reasoning effort **ultra**.
Status: **initialized, awaiting Claude review**. No new dimension classification, sine-moment computation or excluding sign has been obtained.

## Source contract and established seed

This program develops [search card 16](../../../inactive/brainstorm/LIFTED_THETA_SYMMETRY_SEARCH_CODEX_20261013.md#16-radial-geometry-and-reflected-sine-moments). Use the actual complete density `m_t(u)=e^{tu²}Φ_e(u)`. The [three-dimensional radial scout](../../../../quasi-rh-exponent-descent/newman_collisions/12_radial_bessel/notes/1_POSITIVE_THREE_DIMENSIONAL_THETA_LIFT_AND_NONLOCAL_GENERATOR_20261010.md) defines

\[
R_{3,t}(r)=-m_t'(r)/(2\pi r),\qquad
R_{3,t}(0)=-m_t''(0)/(2\pi).
\]

It is smooth and strictly positive throughout `0≤t≤1/20`, including the center. Its axis marginal is exactly `m_t`, and its physical Fourier projection is

\[
H_t(x)=2\pi\int_0^\infty r^2R_{3,t}(r)
\frac{\sin(xr)}{xr}\,dr.
\]

The exact generator is multiplication minus a Volterra term:

\[
(\mathcal GR)(r)=r^2R(r)-2\int_r^\infty R(s)s\,ds.
\]

The genuine theta trajectory has the recorded positivity property; this generator does not preserve the full positive cone. Ordinary radial diffusion would project to a different physical equation.

## Research objective

Seek a theta-specific relation among reflected radial or sine-moment channels that retains the nonlocal generator and supplies a useful candidate-conditioned signed estimate. Geometry may reveal cancellation without making general radial positivity sufficient.

For `x>0`, define `S_t(x)=∫_0^∞ rR_{3,t}(r)sin(xr)dr=xH_t(x)/(2π)`. Thus `(H,H_x)=0` exactly when `(S,S_x)=0`. The [sine-jet continuation](../../../../quasi-rh-exponent-descent/newman_collisions/12_radial_bessel/notes/2_SINE_COLLISION_JETS_AND_HIGH_DIMENSION_THETA_OBSTRUCTIONS_20261010.md) converts the ordinary all-real threshold test into

\[
2S_3^2-3S_2S_4-27S_2^2/x^2.
\]

This expression is necessarily nonnegative under the stated threshold hypotheses. A source-specific paid strict opposite would exclude such an ordinary collision. Higher multiplicities require the full deflated sine-jet conditions or a separate all-multiplicity first-jet criterion; the fourth-jet expression is not sufficient for every multiplicity.

## First bounded task

In dimension three, retain the complete candidate equations and pair positive and reflected negative sine-moment contributions before estimating either. Derive the exact effect of the Volterra term, radial cutoff, origin and infinity endpoints. Compare the resulting complete signed response with the earlier separate absolute envelopes on a specified compact time and height domain.

A separate bounded alternative is to classify exactly one of dimensions 5, 7 or 9 using its unique inverse marginal, central behavior, theta tails and physical observation dictionary. Do not begin all three classifications before one calculation identifies a useful structural distinction.

## Validation failure criterion and exclusions

Check removable origin singularities and all product-rule terms arising from `S=xH/(2π)`. Multiplication by `x` introduces an origin zero; threshold mirror coefficients must therefore be transported rather than copied unchanged. Numerical signs require outward integration, full theta tails, normalization and cutoff payments. Test proposed general implications against the retained smooth positive radial collision control.

Continue if theta gluing yields a signed relation that survives the full nonlocal correction, or if one dimension supplies a new faithful source constraint. Stop the specific inference if it relies solely on positive radial mass, replaces the generator with ordinary diffusion, or drops boundary moments. On `0≤t≤1/20`, exact positive rotation-invariant realizations in integer dimensions at least 11 are already excluded by the recorded genuine-source obstruction. Positive Gaussian mixing is separately obstructed. Anisotropic or nonpositive geometry requires a new reduction and domain contract.

A finite radial identity or calibration does not exclude all positive-time collisions. Global promotion would need the remaining times, heights, multiplicities and threshold/no-escape coverage. This initialization preserves those obligations and claims no RH consequence.

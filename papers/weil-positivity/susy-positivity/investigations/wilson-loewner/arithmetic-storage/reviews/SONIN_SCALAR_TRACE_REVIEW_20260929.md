# Review of the certified scalar Sonin calculation

29 September 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
not exposed. Three separate same-model agents checked mathematical formulas,
implementations, and project scope. This is internal review, not independent
human or specialist refereeing.

**Disposition: passes the internal checks.** The
[scalar note](../notes/SONIN_SCALAR_TRACE_CALCULATION_20260929.md) gives accurate
intervals for four real-place smoothed traces. Every stored trace width is
below `10^-5`, with all approximation errors accounted for. The
[project summary](../PROJECT_SUMMARY.md) treats this as a computational advance
and keeps the signed arithmetic gap open.

## Gamma/contact audit

The gamma program evaluates precisely
`m(t)=Re psi(1/4+it/2)-log pi`. Its Fourier normalization, origin term,
positive-frequency doubling, and prime-2 multiplier are correct. The packed
complex Arb FFT is unpacked using conjugate symmetry; analytic even/odd source
parity justifies extracting the real/imaginary components. No unsigned gamma
majorant replaces the form being computed.

The first Poisson identity compares the continuous gamma integral with its
infinite frequency trapezoid. Outside the compact correlation support the
inverse gamma multiplier is `-exp(-|x|/2)/(1-exp(-2|x|))`. Translated contacts
vanish there. The code's absolute geometric bound includes both sides and
requires a period larger than the correlation support. The second Poisson
identity bounds aliases of the compact source samples by the certified fourth
derivative. The factor `pi^4/45=2 zeta(4)` and separation inequality are
correct. The final tail is the tail of the **discrete** frequency sum, bounded
by its decreasing integral majorant beginning at the last included node.
The code handles these two distinct discretizations separately.

The final gamma build uses the repository source module and its hash-bound
normalization record. The four full widths are below `2e-8`. The primary
calculation uses 128-bit Arb arithmetic, `2^18` spatial points over period 48,
and frequency cutoff just below 5000. Complete rational endpoints and all
three error contributions are in the [gamma record](../numerics/records/gamma_scalar_certificate.json).

## Epsilon/kernel audit

The scaling `theta(rho^-1)h(x)=sqrt(rho)h(rho x)` gives the moving cutoff
`x>1/rho`. Its trace index order, cosine factor two, and the polynomial
kernel order `C32 R32` were checked. No commutativity of an approximate
inverse is silently assumed. The negative exponents in the finite exponential
formula depend on the second monomial index, as implemented.

The real cosine Lagrange remainder is valid uniformly on the complete
spline-correlation support. The nuclear norm bound includes the distinction
between `C` and its polynomial truncation:
`||C32 R32||1 <= (2.858+1.5e-40)||R32||F`.
The uniform resolvent error is multiplied by a squared source L1 bound when
integrated; it is not mistaken for the total scalar error. The kernel epsilon
is kept distinct from the earlier cutoff kernel delta.

The source hat interpolant has L1 error at most `h²||F''||1/8`, plus
explicit quantization error. Exact integer polynomial multiplication produces
the autocorrelation coefficients. The cubic B-spline correlation has the
correct `h/scale²` normalization, and integration supplies the remaining
factor h. Only centers 0 and ±1 cross the absolute-value corner; their two
correction series, coefficients, and geometric tails were independently
derived and checked. Integer translation by N exactly realizes `log2=Nh`.

The source replacement bound uses the true global epsilon bound
`||epsilon||infinity <= ||C||1/sqrt(gamma)` and the L1 correlation estimate
`eta(2||H||1+eta)`. Kernel replacement is separately multiplied by
`(||H||1+eta)²`. The finite kernel domain covers the small support enlargement
caused by interpolation. No tail is inferred from grid agreement.

Independent runs at grid 8192 and 384/448 bits produced overlapping exact
rational intervals and identical quantized-source hashes. These coarser-grid
checks validate numerical consistency; they do not reduce the rigorous error
of the principal grid 262144 calculation.

A separate selected-point control directly integrates the finite Legendre/
spherical-Bessel expression

\[
\epsilon_{32}(\rho)=\frac2{\sqrt\rho}\sum_{i,j}P_{ij}
\int_1^\rho e_j(u/\rho)\sqrt{4i+1}(-1)^i j_{2i}(2\pi u)\,du.
\]

It uses ordinary Legendre recurrence and the entire hypergeometric formula
for the spherical Bessel functions, independently of the cosine Taylor
integration. At `rho=3/2,2,4`, agreement with the exponential model is within
`9e-28`; the values are approximately `1.51047692433351639`,
`1.09980433281786750`, and `0.54481893383715831`.
The [control program](../numerics/epsilon_selected_point_review.py) and
[record](../numerics/records/epsilon_selected_point_review.json) preserve this
normalization and sign check. The analytic remainders, not these three points,
establish the interval statement for every required scaling parameter.

## Combined result and scope

The combined program checks the generating-program hashes, shared source
record, and prior Galerkin dependencies before adding gamma and epsilon.
It checks positive traces and the `10^-5` width target. Rational endpoints
are decoded outward; displayed table endpoints are rounded outward. Replaying
the combined calculation matched the stored data. An explicit guard rejects
an empty intersection when combining the two coarse `B2` bounds.

The transformed scalar is `h0=B_infinity[D2F]`, exactly the Hilbert–Schmidt
source norm required by the prior Galerkin identity. The added finite matrix
correction yields the **full Hilbert–Schmidt residual squared**. Dividing
by the upper/lower spectral bounds for the compressed metric gives valid
bounds on missed positive trace; intersecting with `h0/M <= B2 <= h0/m`
is legitimate. These calculations do not replace the metric by an identity.

The captured-fraction bounds below 1.090% and 2.422% are conservative and apply
to the specified degree-20/24 space and two sources. They do not exclude other
trial spaces, source-adapted calculations, or the Sonin program. The complete
arithmetic residual is a different signed quantity and remains unevaluated.
Negative epsilon scalars do not settle its sign. No return moment, all-source
estimate, arbitrary-support positivity theorem, or RH result is claimed.

Further progress requires accurate control of the first-prime inverse-metric
trace and ultimately a signed estimate with the required source/support
quantifiers. More precision in the present resolvent is not the limiting issue.

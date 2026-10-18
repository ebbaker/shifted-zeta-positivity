# A high height signed consumer and matched real source comparison

18 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. **GPT-6.1 Sol (`gpt-6.1-sol`), actual effort
ultra**, verified from execution metadata. The checks are internal and
same-model, including parallel assistance.

This continues Stages 3–5 of [overview 02][plan]. The [result-summary
index][summaries] and [patterns-to-avoid index][avoid] govern interpretation,
especially [target classification][target], [collision controls][controls],
[preserving cancellation][pairing] and [bounded numerical decisions][bounded].

**Interval-certified statement.** On the entire closed rectangle

\[
 D_1=[1/100,1/5]\times[999,1001],\qquad
 H_x^2-HH_{xx}>\frac1{100}(H^2+H_x^2). \tag{1}
\]

The certificate consumes [Note 11's nonstationary arithmetic tail][tail]
as an error payment. It uses 40 closed cells, with all quadrature,
arithmetic, source-cutoff, mode and whole-cell errors included. The minimum
outward excess exceeds `8.26087e-5 G_*^2`, where
`G_*=1000^(7/4)*exp(-125*pi)` is fixed throughout the computation.
This is a finite signed estimate, not an all-height sign mechanism.
The [vertical-wall continuation][wallnote] consumes the same machinery to
close a larger contiguous finite-height region.

## Declared consumer and finite integral

The declaration fixes the domain above, signed coefficient 1/100,
component added-error allowance `1e-8 G_*`, first omitted mode 12,
cutoff U=2, 160-bit shifted arithmetic, and frozen contour
`d=pi/8-4*log(1000)/1000`. The finite paired contour integral P is formed
only after complete source reflection. Its midpoint is `(21/200,1000)`;
spatial degree 24 and time degree 12 require midpoint derivatives 0–50
and a common remainder derivative bound through order 52. No derivative
is taken of the contour selection rule or of G_*.

For `lambda_n=pi*n^2`, `c=cos(4d)`, and `T=1/5`, a common normalized
finite-integral derivative majorant is

\[
 M=1000^{9/4}e^d\int_0^2\sum_{n=1}^{11}(2\lambda_n^2+3\lambda_n)
 e^{Tu^2+9u-c\lambda_ne^{4u}}[1+(u+d)^{52}]\,du.
 \tag{2}
\]

It bounds every derivative of P of order at most 52 over D1, divided
by G_*. The factor e^d pays the left edge x=999; the power inequality
`(u+d)^j<=1+(u+d)^52` pays all intermediate orders. This positive
integral is itself enclosed outward. Its upper bound is below
`9.632889e10`.

For a cell at spatial distance at most R from 1000 and time distance
at most Delta from 21/200, the remainder of the exact dyadic-coefficient
Taylor polynomial is at most

\[
 M\left(\frac{R^{25}}{25!}+e^R\frac{\Delta^{13}}{13!}\right). \tag{3}
\]

Expand first in space and then in time, applying `P_t=-P_zz`; the highest
remainder index is `2+24+2*13=52`. The whole-box payment is below
`2.165e-12`. Midpoint quadrature radii propagate with the absolute Taylor
weights. The polynomial image includes subsequent arithmetic rounding.
Exact binary mantissa/exponent fields preserve its coefficients and
outward radii in the saved cache.

For the physical orders j=0,1,2, the omitted-mode payment uses Note 11
with the actual frozen parameters. The spectral exponential is bounded at
x=999 and the phase gap at x=1001:

\[
 B=4c\pi m^2-9>190.59,\quad
 P_{\rm gap}=4\sin(4d)\pi m^2-1001-2Td>797.37.
\]

The normalized mode payment is bounded by
`1000^(9/4)*exp(d)*2*S*Q_j/P_gap`, with the S,Q_j of Note 11.
Its largest value is below `1.783e-12`. The retained-source tail beyond
U is paid by the concave tangent using
`D=4c*lambda_n*exp(4U)-9-2TU-j/(U+d)>0` and
`16c*lambda_n*exp(4U)>2T`. High-order physical tail bounds are not
substituted into each Taylor coefficient: propagation concerns the finite
cutoff integral itself, and final physical tails are paid separately.

The [saved setup][setup] binds code, manuscript and Note 11 source hashes,
actual precision, all 51 integrals and their radii, complete majorants,
admissibility margins and measured cost.

## Geometry repair and complete coverage

The initial whole-time spatial-strip attempt stopped at its declared
dyadic depth nine after 40 cell calls. Point checks diagnosed interval
dependence in the full time interval; they were not substituted for a
certificate. Its entire decision log is retained.

The single bounded repair kept all jets, parameters and errors fixed,
and used four exact closed time slabs with boundaries

`1/100, 23/400, 21/200, 61/400, 1/5`.

It accepted ten spatial strips per slab after 76 additional calls. Exact
rational endpoint checks prove full coverage, with no gaps at seams. The
[signed record][signedrecord] retains all coarse choices and every final
jet enclosure, budget and signed lower bound. Its largest added component
error is below `4.621e-12 G_*`. Evaluating
`Hx^2-H*Hxx-(H^2+Hx^2)/100` on each entire closed cell gives the strict
positive lower bounds that prove (1). Outward square ranges include
zero-centred intervals.

## Matched real source comparison

The [comparator][comparison] evaluates the same finite source modes 1–11
over U=2 on the real source contour, using 768 bits. This precision pays
for cancellation of an integrand whose normalized absolute size grows
exponentially in height. Its polynomial, physical domain, consumer cells,
signed target and required total error are the same as the shifted method.

The real evaluator also receives the same useful contour-derived
*physical* derivative majorant. Complete H derivatives are bounded by
(2) plus the uniform shifted tails through order 52. Derivatives of the
finite real integral are then bounded by this common H bound plus its
own omitted-mode and source-cutoff errors. This avoids manufacturing
an exponentially poor real Taylor comparator. For real omitted modes,
all-order errors use the manuscript's positive real-source tail with
`u^j<=1+u^52`; the source cutoff uses the corresponding tangent at U.

The initial real quadrature request returned finite enclosures with
normalized radii exceeding `1e110` (the largest exceeded `2e117`); its relative tolerance did not secure
the requested absolute error. **A finite returned enclosure is not an
accuracy certificate.** The consumer rejected these radii. The single
bounded tolerance repair changed the relative tolerance from `1e-30` to
zero, retained 768 bits and the same absolute tolerance, and reran the
same 51 integrals. All failed work is charged. Both attempts together
stay within the declared 60-second, two-million-callback setup allowance.

The repaired real calculation passes the same 40 signed cells; every
component enclosure overlaps its shifted counterpart. Its largest added
component error is below `2.165e-12 G_*`. It also independently replays
the complex wall from [Note 13][wallnote], paying the real-source complex
strip tails and transferring the corresponding Y=1 physical derivative
majorant. Its cache is not substituted for a theta error bound on a control.

| Matched D1 computation | End to end time | Charged setup callbacks | Result |
| --- | --- | --- | --- |
| Shifted, 160 bits | about 7.590 s | 173486 | 40 signed cells after the bounded geometry repair |
| Real source, 768 bits | about 11.236 s | 183471 | Same 40 cells, including the rejected quadrature attempt and repair |

The ratio of real to shifted total time is approximately
`1.480`. The real tolerance repair alone costs about
`6.876` seconds. Shared positive-majorant/tail preprocessing
is charged to both methods; independent verification costs are recorded
separately in the replay, rather than folded into either method's benchmark.

The factor-two shifted cost gate is not met. The successful real kernel
alone is also competitive with the shifted kernel, so failed-attempt
accounting is not evidence of an inherent contour advantage. The separate
wall consumer supplies a finite-coverage gain; no further height scan is
justified by this timing comparison.

## Replay, controls and scope

The [replay record][replay] reconstructs all lower margins and checks
exact rational coverage, source identities and frozen parameters. It
includes a fresh 256-bit shifted setup, the 768-bit real-source replay,
strict-inequality and malformed-cache checks. The [control record][controlrecord]
replays the source-specific event enclosures and Euler witness. A polynomial
heat event additionally challenges this exact cached-polynomial lane with
source-specific finite derivative bounds and zero physical truncation error.

No estimate assumes a nonzero curvature at a hypothetical theta event or
substitutes a bounded germ at a fixed exterior shift. The full higher-mode
carrier would still leave the first-mode signed cancellation; changing
prime lists is not the mechanism of this certificate. The complete paired
field is enclosed before its signed expression is tested.

Status: (1) is **interval-certified**, with internal same-model replay.
The benchmark is a measured bounded comparison. [Review 11][review] fixes
its proof and source scope. The general signed arithmetic estimate remains
open; [Note 13][wallnote] records the precise finite global-consumer gain
and the unclosed exterior range.

[plan]: ../../research-overview/02_UPDATED_RESEARCH_OVERVIEW_AND_SOL_EXECUTION_PLAN_20261018.md
[summaries]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[target]: ../../../../../avoid/01_restating_the_target.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[pairing]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[bounded]: ../../../../../avoid/10_numerics_ahead_of_the_question.md
[tail]: 11_EFFECTIVE_NONSTATIONARY_ARITHMETIC_TAIL_20261018.md
[wallnote]: 13_VERTICAL_WALL_AND_FINITE_HEIGHT_NONCOLLISION_20261018.md
[setup]: ../../numerics/high_height_consumer/SETUP.json
[signedrecord]: ../../numerics/high_height_consumer/SIGNED_CONSUMER.json
[comparison]: ../../numerics/high_height_consumer/REAL_COMPARISON.json
[replay]: ../../numerics/high_height_consumer/REPLAY.json
[controlrecord]: ../../numerics/high_height_consumer/CONTROLS.json
[review]: ../../reviews/11_HIGH_HEIGHT_SIGNED_AND_VERTICAL_WALL_REVIEW_20261018.md

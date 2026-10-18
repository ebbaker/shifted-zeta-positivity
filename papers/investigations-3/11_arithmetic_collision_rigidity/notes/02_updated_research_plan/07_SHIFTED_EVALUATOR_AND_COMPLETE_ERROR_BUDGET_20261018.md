# Complete shifted evaluator and finite cell error budget

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance, **GPT-6.1 Sol (`gpt-6.1-sol`), actual effort max**. This note
executes Stage 1 of [overview 02][plan] in the user's requested `02_` notes
folder. Assessment and replay are internal, by the same assistant.

**Result: a validated interval evaluator on**
\(D_0=[1/100,1/5]\times[25,45]\), including matched complex tests with
\(|\Im z|\le1\). The real first jet is nonzero throughout the closed
rectangle. This is a machinery certificate on previously covered territory,
not new global collision coverage.

The [source][code], [validation record][record] and [256-bit replay][replay]
contain the exact domains, precision, frozen parameters and complete cell
records. The [result-summary index][summaries] and [avoid index][avoid]
apply, especially [collision controls][controls], [premise screening][screen]
and [preserving cancellations][cancel]. This is a finite numerical milestone,
not a new RH-equivalent criterion.

## The finite paired integral

Use the manuscript normalization and its complete reflected contour formula.
Fix \(d=\pi/16\), retain modes 1 through 4, and cut each shifted positive
half-line at \(U=1\). Call the resulting paired integral \(P(t,z)\).
Completion and reflection precede these truncations. The negative shifted
term is retained; at the real Taylor centre it is evaluated by its exact
conjugacy with the positive term, including every derivative factor.

Every retained integral, even with the fixed cutoff, satisfies
\(P_t=-P_{zz}\). The midpoint is \((21/200,35)\). Spatial degree 50 and
time degree 12 for components through order 2 require midpoint derivatives
through order 76 and absolute remainder derivatives through order 78.
All 77 midpoint integrals are enclosed by Arb/Acb at 160 bits.
The two positive majorant integrals used below are charged separately.

For real t and x, the positive shifted integrand for derivative j has the
factor \((i(u+id))^j\); the conjugate term has \((-i(u-id))^j\).
The code uses these factors directly. Neither differentiation nor Taylor
propagation differentiates the parameter selection rule.

## Uniform derivative and source cutoff bounds

Write \(T=1/5\), \(c=\cos4d\), \(\lambda_n=\pi n^2\) and

\[
 q_n(u;Y)=(2\lambda_n^2+3\lambda_n)
 \exp\{Tu^2+(9+Y)u-c\lambda_ne^{4u}\}.
\]

For \(|\Im z|\le Y\), the absolute derivative integrand is at most
\(e^{-dx}q_n(u;Y)(u+d)^j\). Let

\[
 D_{n,j}(v)=4c\lambda_ne^{4v}-9-Y-2Tv-j/(v+d).
\]

When \(D_{n,j}(v)>0\) and \(16c\lambda_ne^{4v}>2T\), the logarithm of
this majorant is decreasing and concave beyond v. Its tangent therefore gives

\[
 \int_v^\infty q_n(u;Y)(u+d)^j\,du
 \le q_n(v;Y)(v+d)^j/D_{n,j}(v).
\]

The record checks these conditions using interval values. At \(v=U=1\)
this pays for the retained integral tails for all consumer components.
The omitted arithmetic modes use the manuscript's separate \(K_j e^{-dx}\)
bound. Its three admissibility conditions are checked for the actual
interval shift and time domain, not nominal point values.

For a uniform derivative bound through \(J=78\), split at \(r=3/4\).
The interval check gives \(r+d<1\). On the short part \((u+d)^j\le1\);
on the rest it is at most \(1+(u+d)^J\). Thus a valid common bound is

\[
 M_{J,Y}=e^{-d x_{\min}}\left[
 \int_0^r\sum_{n=1}^4q_n(u;Y)\,du+
 \sum_{n=1}^4\sum_{p\in\{0,J\}}
 \frac{q_n(r;Y)(r+d)^p}{D_{n,p}(r)}\right].
\]

The finite integral is positive and is itself evaluated with outward
rounding. On D0, the real-axis bound is below 0.004266, compared with
0.076338 for the real-source comparator's common moment bound. The complex
strip bound is below 0.004774. These are absolute derivative bounds for
the finite paired integral, not lower bounds on the physical field.

## Complete enclosure

Let \(R\) bound the complex distance to the spatial centre and \(\Delta\)
the time distance. Expand first in space and then in time, using the heat
equation. The common Taylor error for each component through order 2 is

\[
 M_{78,Y}\left\{\frac{R^{51}}{51!}
       +e^R\frac{\Delta^{13}}{13!}\right\}.
\]

If \(\rho_a\) is the returned radius of midpoint integral a, its propagated
quadrature payment for component j is

\[
 \sum_{\ell=0}^{50}\sum_{k=0}^{12}
 \frac{R^\ell\Delta^k}{\ell!k!}\rho_{j+\ell+2k}.
\]

The midpoint dyadics define an exact mathematical polynomial. Its image on
each cell is enclosed by outward ball arithmetic, then enlarged by mode,
source cutoff, quadrature and Taylor payments. Quadrature radii include
their internal arithmetic rounding; subsequent coefficient and polynomial
rounding remains inside the polynomial image enclosure. There is no unpaid
floating-point tolerance. The listed added error bounds the physical field
minus that exact polynomial. A cell ball's midpoint alone is not asserted
to have that pointwise error without its own radius.

| Obligation | Treatment |
| --- | --- |
| Omitted modes | Manuscript K bound, with actual interval admissibility |
| Retained source beyond U | Concave tangent bound above |
| Quadrature and its internal rounding | Returned outward radii, propagated with absolute Taylor weights |
| Subsequent arithmetic | Outward enclosure of the exact dyadic-coefficient polynomial |
| Whole-cell Taylor propagation | Derivatives through order 78 and the displayed remainder |

The predeclared added-coordinate allowance is \(10^{-10}\), with separate
mode, source and quadrature allowances of \(10^{-12}\), Taylor allowance
\(10^{-11}\), and a reserve of \(8.7\times10^{-11}\). All matched tests
fit those allowances. The actual enclosure, including arithmetic, supplies
the strict consumer margin.

On the full-time accepted strips the worst added coordinate errors are
below \(2.751\times10^{-18}\) shifted and \(4.923\times10^{-17}\)
real-source. Taylor propagation dominates. Both methods certify 128
contiguous closed strips, with minimum selected-coordinate lower bound
above \(7.07\times10^{-9}\). Matched point and cell enclosures intersect
for all three derivatives, including complex cells. Conjugation and a
separately integrated time derivative pass diagnostics. No evenness of the
finite shifted approximant is assumed.

The replay brackets an ordinary root at t=1/10 with \(|H_x|>8.75\times10^{-5}\)
and a stationary point with \(|H|>1.016\times10^{-4}\). The latter bound
is certified directly. Error comparisons use the nonzero jet or positive
envelope \(G_0=x^{7/4}e^{-\pi x/8}\), never division by a vanishing H.

**Stage 1 gate passed for this interval consumer.** No admissibility failure
or evaluator-domain repair was required. The control-interface repair and
the measured efficiency decision are documented in [Note 08][pilot].

[plan]: ../../research-overview/02_UPDATED_RESEARCH_OVERVIEW_AND_SOL_EXECUTION_PLAN_20261018.md
[code]: ../../numerics/certify_shifted_theta_jet.py
[record]: ../../numerics/SHIFTED_EVALUATOR_VALIDATION_20261018.json
[replay]: ../../numerics/FINAL_CLAIM_LEDGER_20261018.json
[pilot]: 08_MATCHED_PILOT_AND_CONTROL_SCREEN_20261018.md
[summaries]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[screen]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[cancel]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md

# E07 r1 assessment calculations for deflated logs and Green cells

10 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. The exact-turn local record identifies
**gpt-6.1-sol, ultra**. Internal analytical assessment with inherited
premises. All eight [Request23][request] claims are accepted within
their stated hypotheses, with no mathematical correction to [Note12][b05].
[Review11][review] maps the findings to the frozen claims.

## Complex deflation and finite-source bounds

I rechecked [de Boor, §9 (52), printed pp. 63–64][deboor] through
[the canonical OA source record][deboor_record]. Its iterated integral
has volume \(1/n!\). In barycentric coordinates, repeated elementary
beta integration gives
\[
 \int_{\Delta_n}\prod_{i=0}^n t_i^{k_i}\,dt
 =\frac{\prod_i k_i!}{(n+\sum_i k_i)!}.
\]
The evaluation point contributes \(t_x^j\) after \(j\) derivatives.
In the knot movement term, differentiating along one straight knot
segment adds \(t_i(w_i-z_i)\). The two integrals therefore give
\(j!/(n+j)!\) and \(j!/(n+j+1)!\). Convexity includes the arguments
throughout each sequential movement. Holomorphy on a neighborhood
justifies differentiation and continuous confluence. Newton–Hermite
remainder division by the **actual** root polynomial works because
the interpolation data through the relevant derivative orders vanish.
The approximate knots instead define a divided difference of the
finite source. Their interpolant generally has nonzero data.

At \(n=0\) the simplex is a point and the bound is \(\epsilon_j\).
For a repeated real knot \(u\), the exact quotient of \((z-u)^2\)
extends as \(1\) at the knot. With \(f(z)=(z-u)^{2+j}\), the ratio of
the \(j\)-th quotient derivative to the constant source derivative
of order \(2+j\) is \(j!/(2+j)!\) there. With
\(f(z)=(z-u)^{3+j}\) and one of the two knots shifted by \(s\), the
change in the \(j\)-th divided-difference derivative at \(x=u\) is
\(j!s\). This follows from the simplex integral with
\(f^{(2+j)}=(3+j)!(z-u)\) and checks the knot coefficient as well.
A local \(z^2+\eta\) control has roots \(\pm i\sqrt{\eta}\) for
\(\eta>0\), despite its unit regular factor. Thus the modulus in
(7)–(8) takes certified root errors as input. It does not improve the
source-to-root conditioning in [B01 Note01][b01].

For (4), retain the exact finite reflected half-Fourier source.
The derivative inserts \((iu)^k\), so multiplication by
\(|u|^ke^{b|u|}\) in the two inherited source bounds yields exactly
the two moments and their factor \(1/2\). One can choose the derivative
error allowance to include the resulting truncation bound plus any
charged numerical enclosure error. The exact \(\widehat H\) and its
divided difference continue to define the central mathematical
approximant. Numerical errors in that quantity can instead be charged
in (14), with floors and derivative upper bounds verified for the same
approximant. The largest order needed is \(n+3\), or \(n+2\) with exact
knots. E06's value error does not supply these derivatives.
[Note06 (1), (13)–(14)][e03] gives \(s=(1-iz)/2\) and the multiplier
\(D_0\). At \(z=-i\), \(s=0\) and the reciprocal gamma cancels one
power of the \(s^{-2}\) factor, leaving a simple pole in \(D_0\)
and in \(F\), since \(\xi(0)=\xi(1)=1/2\) by reflection and the
zeta residue at \(1\). On the real line \(s\) has real part \(1/2\), so
\(D_0\) is finite and nonvanishing. Deflation is applied to \(H_0\).

## Logs, product integration and the final interval

If \(|\widehat U_v|\ge\mu_v>e_{v,0}\), both absolute values in the
factor-log difference lie in \([\mu_v-e_{v,0},\infty)\). This proves
(5), and \(\int_{\mathbb R} K=1/2\) pays (6). For one root pair, the
triangle inequality for the two distances gives
\[
 |\log r-\log s|\le\log(1+\rho/r)+\log(1+\rho/s)
\]
almost everywhere. Replacing a complex distance by its horizontal
distance enlarges this upper bound. For an even decreasing majorant
the largest length-\(L\) integral is on the centered interval, as
follows by integrating the intersection lengths of its centered
superlevel sets. Each term is bounded by
\(2\rho[1+\log(1+L/(2\rho))]\), using \(\log(1+t)\le t\).
The bound tends to zero with \(\rho\), and equal knots give zero
exactly. Real endpoint singularities are integrable. Multiplicity
means repetition in the sum. For a purely vertical shift integrate
\(b/(t^2+b^2)\) over the line and then over the height interval.
The nonnegative integrand gives \(\pi|\Delta b|\), including a zero
height endpoint by monotone integration.

For a panel of length \(\ell\), endpoint interpolation of a twice
differentiable real function with curvature bound \(M\) costs at most
\(M(x-l)(u-x)/2\le M\ell^2/8\). Differentiation of \(K\) gives
\(K''=a^2\operatorname{sech}(at)(1-2\operatorname{sech}^2(at))/16\).
Apply the two interpolation errors separately to
\(K(q_v-q_h)+(K-K_h)q_h\). The first integrates against \(W_v\),
the second against at most \(L_vH_v\) since \(q_h\) is a convex
combination of endpoint values. The kernel error on each singular
factor multiplies its full \(L^1\) bound \(L_v\log^+D_{v,j}+2\).
The negative part is bounded by the integral of \(-\log|t|\) on
\([-1,1]\). Differentiating both primitives in (11) gives respectively
\(\tfrac12\log(t^2+b^2)\) and \(\tfrac t2\log(t^2+b^2)\).
Their continuous \(b=0\) endpoint values integrate the real-knot
logarithm. These checks retain the signed sum (10) and give (12).

At \(R=66\), \(\sum_v\lceil6000L_v\rceil\le792000+p\).
With the stated \(B_*,S\) limits and \(a<2/5\),
\(C<2^{20}/16+2^{19}/800=1654784/25<66200\).
Thus the design box gives \(793024\) panels at most and
\(E_{\rm quad}<331/180000<1/500\). [Record07][record] compares this
with the inherited E06 radius by exact arithmetic on its saved
directed endpoint. The four quantities \(p,B_*,S,\mu_v\) have no
acquired canonical bounds in this assessment.

In (14) the signed exact-log tail and the signed prime remainder
each contribute one radius, together with factor, root, quadrature
and finite numerical radii. There is one \(+G(X,1)\) in the central
value. The bound \(|J-S_c|\le\mathcal R\) implies both ends of
\(0\le S_c+\mathcal R-J\le2\mathcal R\). The factor two is mandatory
for this symmetric acquisition. The finite radius still has to pay
divided differences and factor evaluation, kernel and regular
endpoints, primitives, prime and gamma values, the pole term and
rounding. The positive endpoint weights for \(q_h\) sum to
\(\int_I K_h\le R/8\). A node log error needs the true floor
and is bounded by \(\eta/(\mu_v-\eta)\) if \(\eta<\mu_v\).

## Cell bounds and the matched direct comparator

The minimum and maximum of the clipped Green kernel on each rectangle
are the farthest/lowest and closest/highest combinations in (16).
For \(u=\sin(ay)\operatorname{sech}(at)\), divide the derivatives of
\(u\) by \(1-u^2\ge\cos^2a>21/25\). The bounds
\(a/\cos^2a<1/2\) and \(a^2/\cos^2a<1/5\) give (17), and
\(y\mapsto y_+\) carries the vertical bound across the cusp. The
cusp is still outside the smooth-statistic hypothesis from OC.
Counts include multiplicity. Complete coverage and unambiguous
assignment of each counted label suffice, including non-singleton
cells and cells that straddle the axis.

The right and left integer slabs at distance between \(n\) and
\(n+1\) start at \(X+n\) and \(X-n-1\). [B06 Note10 (4)–(6)][b06]
gives at most \(16(|X|+n+3)^2\) per slab and exponential Green decay
at rate at least \(3/8\). The two slabs give the factor \(32\) in (18),
including a zero at the core boundary if omitted from the core.
Expanding the squared coefficient after \(n=R+j\) gives the three
geometric-series terms of (19). For a deliberate alignment misuse,
take \(X=1/2,\ n=1\). The two shifted unit intervals have interiors
in four integer unit slabs. The original two-slab proof then does
not justify (18) as written. This tests the premise of that proof.

For \(0<d\le1,\ 0\le r<R\), an occupied rectangle meeting
\(D=[X-r,X+r]\times[d,1]\) has supremum at least \(G(r,d)\),
which is at least \(m(d,r)\) by \(\operatorname{atanh}u\ge u\) and
concavity of \(\sin\) on \([0,a]\). As a boundary test, at \(X=0,r=1,
d=1/2,R=2\), the occupied cell \([1,3/2]\times[0,1/2]\)
meets \(D\) only at the corner and attains \(G(1,1/2)\) there.
Every summand and the tail allowance is nonnegative. Hence the strict
Green pass requires cell disjointness, even at the target boundary.
Completeness in the core covers the entire \(D\), and a direct
disjointness test on those identical cells certifies its exclusion.
This comparison is for independent rectangular maxima and identical
acquired information. It leaves actual wall time and correlated
range methods open.

The [result index][results], [controls12][controls] and
[avoid index][avoid] frame these conditional acquisition and
information-class claims. [Review11][review] records the
premise-by-premise control check. No canonical root/factor certificate,
favorable value, fully charged cost comparison or additional coverage
was acquired. [Continuation15][cont] states the condition for reopening
B05 r2.

[b05]: 12_TND_OG_B05_DEFLATED_LOG_AND_CELL_RANGE_DECISION_20261110.md
[b01]: 01_TND_OG_B01_UNIFORM_SOURCE_CONDITIONING_20261107.md
[e03]: 06_TND_OG_E03_COMPLETE_SIGNED_LOG_ACQUISITION_20261108.md
[b06]: 10_TND_OG_B06_SIBLING_RESULTS_AND_GREEN_CENSUS_TRANSFER_20261110.md
[deboor]: https://arxiv.org/pdf/math/0502036v1#page=19
[deboor_record]: ../../03_collision_constraints/references/01_TND_OA_B01_SOURCE_USE_20261109.md
[request]: ../research-progress/handoffs/23_TND_OG_E07_ANALYTICAL_ASSESSMENT_REQUEST_20261110.md
[review]: ../reviews/11_TND_OG_E07_ANALYTICAL_ASSESSMENT_20261110.md
[record]: ../numerics/07_TND_OG_E07_EXACT_ASSESSMENT_RECORD_20261110.json
[cont]: ../continuation-notes/15_TND_OG_E07_RESULTS_AND_MODEL_CHANGE_20261110.md
[results]: ../../../../../../result-summaries/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md

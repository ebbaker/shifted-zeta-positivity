# What finite time reconstruction establishes and which estimates to pursue

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**, verified from this turn's metadata.

**Classification:** interpretation and proposed research directions, with
an elementary heat-defect accounting identity in Section 4. The opening
round sharpened a specified direct enclosure; it established neither a
positive-time advantage nor the positive endpoint margin needed for
exclusion. This assessment changes no FTSR theorem status.

## 1 The geometric question and the estimating obstacle

The current endpoint branch asks, conditional on RH, whether the original
theta field can have a multiple real zero at time zero. Excluding ordinary
doubles locally is one part of that question. All heights and higher
multiplicities remain separate obligations.

The relative Chern or Hopf charge counts isolated multiple-zero events
inside a suitable spacetime boundary. A double contributes one; spatial
multiplicity m contributes m(m−1)/2. In a two-root window the discriminant
Delta=(z1−z2)^2 gives a simpler description: it is positive for distinct
real roots, zero at their collision, and negative for a conjugate nonreal
pair. The charge identifies what a collision contributes. To exclude it,
the source still has to supply a signed estimate. See the
[manuscript](../manuscript/main.tex) and [endpoint program][endpoint].

Write the complete field as a canonical head plus its entire omitted
tail, H=F+E. The estimating interface is

\[
 \Delta_H=\Delta_F+L_F(E)+B_F(E,E)+R_3,
 \qquad |R_3|\le C_3(\rho),\quad
 \sup_\Gamma|E/F|\le\rho<1.
\]

Three advances in [Note 13][n13], [Note 14][n14] and [Note 15][n15] make
this a better controlled calculation. The local window, both root counts and outer wall can be
paid without assuming a positive gap between the two roots. The quadratic
response depends on at most four measurements of E. Finally, covariance
of the same canonical tail law gives an error of order J^-3 plus J^-4,
instead of the order J^-1 range error on the specified common uniform
cutoff grid. Additional cell moments are required. The strict comparison
does not cover every direct grid or every equal-cost algorithm.

The difficulty is cancellation. [Note 11, Section 3][n11] shows that at a
hypothetical ordinary double the head discriminant and the linear tail
correction cancel at leading order. Including the quadratic term leaves
only a cubic discrepancy, consistent with Delta_H=0. A finer enclosure
can therefore converge toward zero. Accuracy alone supplies no reason
that its lower endpoint must become positive.

Positive time offers another representation of the same field. For the
tested canonical-cell approximation, exact evolution and reconstruction
return the original endpoint approximation. Gaussian Hermite projection
returns the endpoint Taylor polynomial. These are scoped equal-information
comparisons, not an impossibility theorem for useful positive-time
estimates. A representation can make an inequality easier to discover or
prove without supplying additional information.

## 2 First priority is the coupled arithmetic constraint

The most promising next calculation joins the two-root response to the
full reflection relation already developed in the neighboring BW14
investigation. With its unchanged canonical source decomposition
Phi=S_m+R_m, [BW14 Note 05][tst05] uses

\[
 S_m(v)-S_m(-v)=-\{R_m(v)-R_m(-v)\}
 \qquad (|\operatorname{Im}v|<\pi/8).
\]

The complete source is even; its finite head and tail are not separately
even. The normalized relation follows from the theta modular identity,
whose classical input is [DLMF 20.7.32][dlmf]. BW14 has already used the
relation to replace a head connector error by a complete-tail error. Its
moving-contour error is small relative to a gamma envelope, not relative
to a nonvanishing physical field or derivative. That stability theorem
does not establish the sign sought here.

At a putative double (0,a), value and derivative matching require

\[
 E(a)=-F(a),\qquad E'(a)=-F'(a).
\]

These equations are the hypothetical event, not a new criterion. The
proposed calculation is to keep them coupled to the *same complete tail*
and full reflection relation, and derive an independently bounded
restriction on the remaining source measurements. The desired payoff is
that the simultaneous matching cannot occur for the canonical coefficients.
Merely declaring that theta has special arithmetic does not supply such
a restriction.

The first acceptable intermediate result is a strictly sharper signed
response bound on a declared family of possible-double windows, with
explicit height and wall dependence. It need not yet exclude zero. A
positive complete lower bound would be the stronger local exclusion
result. Any use of a shifted or reflection-corrected reference must first
rebuild its residual, connector terms, two-root counts and wall ratio;
the unshifted canonical-tail formula cannot be reused unchanged.

## 3 Concentrate the estimate on the few measurements that matter

[Note 14][n14] writes the quadratic response as

\[
 S(E)=l^\top d+d^\top M d,
\]

where d has at most four real coordinates. They describe the residual
modulo the square of the monic degree-two cluster polynomial. This is a
compression of the quadratic response, not a finite-dimensional formula
for the entire discriminant. In particular the cubic remainder remains.

For a reference double F=U(z)(z-b)^2, write h=E/U. Then

\[
 S(E)=-4h(b)+h'(b)^2+2h(b)h''(b).
\]

Only three normalized jets enter. The reference double at b must not be
confused with a hypothetical double of the complete H at a.

The next useful object is a certified *joint* feasible set for d, obtained
from the actual canonical law and any quantified reflection relations.
Separate intervals allow combinations of errors that the common source
cannot produce. A smaller joint set may yield a larger lower bound for
the quadratic expression. Note 14 already supplies a generic ellipsoid
consumer; repeating its algebra is not the missing work. The missing
deliverable is a sharper theta-specific acquisition contract for that set.

A concrete first comparison should retain the same F, E, contour and
source accuracy as Note 15, derive one joint restriction independently
of a positive root gap, and compare the complete lower endpoints. If the
restriction only reproduces the existing moment enclosure, record that
outcome. If it improves the response but the complete interval still
contains zero, record an estimating gain only. Acquiring exact values
of a few measurements does not by itself establish their sign at every
unknown height.

## 4 A bounded positive-time trial with explicit defect accounting

A different positive-time approximation is worth considering if it
allows a better bound for those few measurements, or a justified reduction
in acquisition work. Effective positive-time approximations of this
specific theta field exist in [D. H. J. Polymath's 2019 paper][polymath].
Their existence motivates a candidate search; it does not supply this
program's full-line residual norm or coupled signed error automatically.
Local spectral approximations need complete spatial and source tails.

One way to state an honest contract is to allow an approximate field
P(t,y) which does not solve the heat equation exactly. Choose fixed
0<sigma<=T, define

\[
 d_t(y)=\partial_tP(t,y)+\partial_y^2P(t,y),\qquad
 r_T(y)=E(T,y)-P(T,y),
\]
\[
 p_0^{\sigma}(z)=\int_{\mathbb R}K_\sigma(z,y)P(\sigma,y)\,dy.
\]

Assume sufficient differentiability, vanishing integration-by-parts
boundary terms, and absolute convergence uniformly on the endpoint
contour, including the following time integral. Then

\[
 E_0-p_0^{\sigma}
 =\int_{\mathbb R}K_T(\cdot,y)r_T(y)\,dy
  +\int_\sigma^T\!\int_{\mathbb R}K_t(\cdot,y)d_t(y)\,dy\,dt.
 \tag{1}
\]

Indeed, differentiating the convolution of K_t and P gives the
convolution of K_t and d_t, since partial_t K_t=partial_y^2 K_t.
Integrate from sigma to T and use E_0=K_T*E_T. The defect term has a
**plus** sign. For the exact polynomial heat field E(t,y)=y^2−2t and
P(t,y)=y^2+c t, the right side of (1) is
−(c+2)T+(c+2)(T−sigma)=−(c+2)sigma, agreeing with the left side.

For real a and endpoint contour |z−a|=R, set

\[
 \eta_T^2=\int K_T(a,y)|r_T(y)|^2dy,\qquad
 \zeta_t^2=\int K_t(a,y)|d_t(y)|^2dy.
\]

The same Gaussian Cauchy–Schwarz estimate as in [Note 12][n12] yields

\[
 \|E_0-p_0^\sigma\|_\Gamma\le
 e^{R^2/(4T)}\eta_T+
 \int_\sigma^T e^{R^2/(4t)}\zeta_t\,dt=:\beta.
 \tag{2}
\]

The complete generic response allowance is consequently

\[
 |S(E_0)-S(p_0^\sigma)|
 \le (C_L+2C_B\|p_0^\sigma\|_\Gamma)\beta+C_B\beta^2.
 \tag{3}
\]

Equations (1)–(3) are accounting identities and fallback estimates, not a
theta improvement. A candidate should retain terminal and defect
contributions jointly in the few response measurements whenever that
helps. A heat defect is an additional error to control, not a source of
automatic improvement. When d_t=0, the reconstructed approximation is
independent of the matching time, recovering the existing screen.

Keeping sigma>0 avoids an unexamined singular payment
exp(R^2/(4t)) near t=0. Sending sigma to zero requires additional analytic
control. A finite-time trial passes only after it improves a declared
direct comparator with the same information and accuracy, or establishes
a separately measured acquisition advantage. The present FTSR estimating
milestone still requires a stronger interval. No growing-T investigation
is justified by (1) alone.

## 5 An alternative is to estimate the collision time directly

The [manuscript's event-displacement formula][source] follows a double
while the tail is added through H_s=F+sE. Provided the common walls,
cap signs and curvature floor pay continuation for 0<=s<=1, it gives

\[
 \tau_s'=E/N,\qquad
 \tau_s''=(P_4/N)(\tau_s')^2-(2E_{zz}/N)\tau_s'-(b_s')^2,
\]

with all quantities evaluated on the same event branch, N=H_s,zz and
P_4=H_s,zzzz. The negative square is potentially useful: a quantitative
lower bound for its weighted integral could improve the existing upper
bound for the final event time, which discarded that term.

The first task would be to estimate that contribution together with the
other terms using the canonical source. No generic positive lower bound
for the square is available; the branch may have zero spatial drift.
The desired conclusion tau_1<0 is a target, and a negative head event is
insufficient: Note 11 proves that adding the actual tail returns it to
zero under the endpoint-double hypothesis. This route is an alternative
way to estimate the same obstruction and receives lower priority than
the fixed-time joint-source calculation.

## 6 Decision rules and immediate recommendation

Start by combining Sections 2 and 3. Identify the exact coupled
constraint, derive its quantitative effect on the response, and compare
it on a possible-double regime. Use Note 15 as available quadrature
machinery. Pursue Section 4 only when a specific approximation has an
independently payable error mechanism. Keep the event-time route as a
secondary option. Height-uniform exclusion, higher multiplicities and
growing time remain subsequent tasks with their own proofs.

The [result index][results], [collision-control register][controls] and
[avoid index][avoid] govern these proposals, especially
[target classification][a01], [matched premises][a02] and
[coupled estimates][a12]. Generic heat identities, finite-rank reduction
and covariance bounds should continue to hold for colliding controls.
Euler-factor modifications change canonical arithmetic;
weighted-square and finite-prime controls lack the complete normalized
reflection conjunction; reflected or positive-primitive controls lack
the canonical square coefficients; close normalized endpoint controls
lack ordinary Dirichlet-series arithmetic. These are distinct controls
with distinct preservation lists.

Those structural differences are not yet the needed quantitative
discriminator. Before promoting a proposed inequality to exclusion,
identify a precise estimate that theta satisfies and that a relevant
control fails on a domain containing its event. If no such estimate has
been established, report an open hypothesis or a scoped relaxation
comparison. Neither another separated-root numerical certificate nor
smaller generic error bars settle this issue.

This note is an authoring-assistant assessment, with the elementary sign
check above. It adds no theta data acquisition or specialist review. The
[progress register][progress] records its planning status; the prior
[review][review12] retains its original scope.

[endpoint]: ../research-overview/02_ENDPOINT_CHARGE_EXCLUSION_PROGRAM_20261021.md
[n11]: 11_CANONICAL_QUADRATIC_RESPONSE_AND_HEAD_TAIL_CANCELLATION_20261021.md
[n12]: 12_LARGE_TIME_INFORMATION_AND_ENDPOINT_RECONSTRUCTION_20261021.md
[n13]: 13_PAID_ENDPOINT_WINDOW_AND_FINITE_TIME_BASELINE_20261021.md
[n14]: 14_GAUSSIAN_HERMITE_RECONSTRUCTION_AND_RESPONSE_QUOTIENT_20261021.md
[n15]: 15_CANONICAL_COVARIANCE_SIGNED_ENCLOSURE_20261021.md
[tst05]: ../../14_theta_source_transform_constraints/notes/05_FINITE_REFLECTION_JETS_AND_HEAD_TAIL_STABILITY_20261021.md
[source]: ../manuscript/source.tex
[progress]: ../research-progress/03_FINITE_TIME_SIGNED_RECONSTRUCTION_PROGRESS_20261021.md
[review12]: ../reviews/12_FINITE_TIME_SIGNED_RECONSTRUCTION_OPENING_REVIEW_20261021.md
[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[dlmf]: https://dlmf.nist.gov/20.7.E32
[polymath]: https://arxiv.org/abs/1904.12438

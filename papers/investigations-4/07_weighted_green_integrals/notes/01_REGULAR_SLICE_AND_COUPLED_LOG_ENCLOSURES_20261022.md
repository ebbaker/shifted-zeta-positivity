# Regular slice, coupled log enclosures and the first control comparison

22 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex)**,
reasoning effort **ultra**, verified from this turn's local metadata.
Contributing agents used the same model/configuration. No specialist review
or literature priority is claimed.

**Status: proved in-note in the conditional local scope below.** The conditional
analytic slice contract is paid, including a derived interior energy floor.
Two complete polynomial log enclosures retain the common source and both
kernel signs. An exact quadratic control rejects the global range bound
and exposes the slow remainder of the midpoint Taylor scheme. A Chebyshev
remainder passes the same control's analytic error budget; its source
moments, acquisition cost and advantage over direct evaluation remain
unpaid. There is no actual theta acquisition or improved theta certificate.

This is a quantitative estimator design, not an RH-equivalent criterion
or a noncollision result. Follow the [result index][results], [avoid
index][avoid], [classification][a01], [matching controls][controls],
[scope rule][a07] and [coupled-payment rule][a12]. The [program][program]
and [sole register][progress] retain task ownership. The earlier global
inverse-Schur failure in [Shared Note 05][n05] is not reopened.

## 1. Freeze the conditional comparison before acquisition

Use exactly [Shared Note 03, (8)–(12)][n03]: a hypothetical ordinary double
at (0,a), h_2=H_zz(0,a), h=|h_2|>0, complete ambient upper bounds D_2,D_3,D_4,
and its sufficient R,d,epsilon_1,epsilon_2. The field, heat convention and
normalization remain H_t=-H_zz and 8H(0,z)=xi(1/2+iz/2) in the canonical
application. Fix this disk and **t_0=d/4**, without choosing a new radius
to improve the comparison. The source formula in Section 4 takes a real
event center a; Sections 1–3 need only a holomorphic heat solution.

Common data consist of complete values and spatial jets through order two,
the ambient D_2,D_3,D_4 actually used by the inherited geometry, all source
mode/ray tails, full-source reflection, simultaneous value/jet matching,
and outward-rounding allowances. No separate evenness of a finite head or
tail is allowed. Higher source moments acquired for either estimator are
given to the direct comparator too. All constants here are parameters of
a conditional event; none is a measured canonical event parameter.

The analytic pilot's declared absolute error target is **1/100** in
normalized weighted mass. A successful later comparison must improve the
complete direct upper certificate by at least **1/100**, or prove a strict
acquisition saving at the same total error. These are chosen acceptance
requirements, not measured margins. Source error, spatial quadrature,
analytic truncation and rounding must sum to at most 1/100. No floating
timing or bare polynomial degree establishes an acquisition saving.

The direct method may use joint feasible data, exact special-case
evaluation, the weighted-density integral and the unweighted Green bound.
In particular it receives every refinement below. Before actual acquisition,
the source cutoff, ray schedule, common mesh and individual error payments
still need freezing; this note authorizes no theta run.

## 2. Pay regularity and the interior energy floor

The inherited contraction theorem gives a unique critical branch c(t) in
the disk, c(0)=a, with H_zz bounded away from zero. Write

\[
 k=h-\epsilon_2>0,\qquad V(t)=H(t,c(t)),\qquad v=t_0 k.
\]

Since V'=-H_zz(t,c(t)), V(0)=0 and |H_zz-h_2|<=epsilon_2,
|V(t_0)|>=v. This **derives** nonvanishing from the conditional event
and upper-jet contract; it is not an assumed unknown interior floor.
For r=|z-c(t_0)|, integrate on the straight segment inside the disk:

\[
 |H_z|\ge kr,\qquad
 |H-V|\le D_2r^2/2,\qquad
 E\ge (v-D_2r^2/2)_+^2+k^2r^2.
\]

The first inequality retains the complex reference h_2: the error in
H_z-h_2(z-c) is at most epsilon_2 r. Minimizing the last expression over
r^2>=0 gives, with b=k^2/D_2,

\[
 \boxed{E\ge e:=
 \begin{cases}v^2,&v\le b,\\2bv-b^2,&v>b.\end{cases}}       \tag{1}
\]

Both branches are positive. Every denominator below is therefore paid on
this slice. The unique-event theorem independently confirms that the only
common jet zero in the product window is at (0,a). Neither argument is
uniform as t_0 decreases to zero: v and e decrease to zero too.

Use the tightened slice upper bounds

\[
 M=D_2(t_0+R^2/2),\quad \varepsilon=D_2R+D_3t_0,
 \quad U=M^2+\varepsilon^2,\quad
 A=MD_2+\varepsilon^2,\quad B=\varepsilon^2+D_2^2.          \tag{2}
\]

For psi=(1-|z-a|^2/R^2)^3, extended by zero, direct methods already have

\[
 M_\psi\le B_{\rm dir}:=\min\left\{
 {R^2A^2\over4e^2},\ {R^2B\over4e},\
 {R\varepsilon(M+D_2)\over(5hR/8)^2}\right\}.              \tag{3}
\]

Here integral psi dA=pi R^2/4, and
|HH_zz-H_z^2|^2<=E(|H_z|^2+|H_zz|^2). The last bound is inherited
unweighted Green, using 0<=psi<=1. Any sharper wall floor or joint
density enclosure strengthens the direct baseline; (3) is not declared
optimal. Exact control information is likewise available to both methods.

## 3. Signed kernel and a complete coupled polynomial enclosure

The zero extension is C^2 because psi and its first two normal derivatives
vanish on the circle. Define the real signed functional

\[
 L[f]={3\over\pi R^2}\int_{D_R(a)}(1-s)(3s-1)f\,dA,
 \qquad s=|z-a|^2/R^2.
\]

Green gives M_psi=L[log E]. Its total signed mass is zero, its positive
and negative masses are **4/9 each**, and its total variation is 8/9.
Consequently

\[
 |L[q]|\le {4\over9}(\sup q-\inf q)
 \le {8\over9}\|q\|_\infty,\qquad
 0\le M_\psi\le {4\over9}\log(U/e).                       \tag{4}
\]

The last expression is only the global-range relaxation: it discards
source correlations. An upper energy bound alone cannot justify it.

For a first complete coupled candidate set c=(U+e)/2,
rho=(U-e)/(U+e)<1 and x=E/c-1. With n>=1,

\[
 P_n=L\left[\sum_{j=1}^n{(-1)^{j+1}x^j\over j}\right],
 \qquad
 |M_\psi-P_n|\le T_n:={8\over9}
 {\rho^{n+1}\over(n+1)(1-\rho)}.                          \tag{5}
\]

This follows from the absolutely convergent log series and (4), with the
same E on the whole disk. If J_k=L[E^k], the exact polynomial identity is

\[
 P_n=\sum_{k=1}^n{(-1)^{k+1}\binom nk\over k c^k}J_k.     \tag{6}
\]

This form specifies the common moments; separately enclosing every term
can be much worse than evaluating the centered polynomial jointly.

A faster complete candidate uses x_C=(2E-U-e)/(U-e) when U>e and
r_C=(sqrt(U)-sqrt(e))/(sqrt(U)+sqrt(e)). Let T_j(x_C) be the Chebyshev
polynomial, defined by T_j(cos theta)=cos(j theta). Factoring
E=C(1+2r_C x_C+r_C^2), C=(sqrt(U)+sqrt(e))^2/4, and expanding the two
complex logarithms proves

\[
 Q_n=2\sum_{j=1}^n{(-1)^{j+1}r_C^j\over j}L[T_j(x_C)],
 \qquad |M_\psi-Q_n|\le C_n:={16\over9}
 {r_C^{n+1}\over(n+1)(1-r_C)}.                            \tag{7}
\]

The proof uses |T_j|<=1 and the uniform log tail. If U=e the energy is
constant and M_psi=0. Again all polynomial moments must come from the
same source. Faster uniform approximation is not itself a better paid
Gauss-mass certificate than direct integration.

For completeness, moment acquisition errors |J_k-Jhat_k|<=delta_k in (6)
cost at most sum binom(n,k)delta_k/(k c^k), in addition to T_n and any
polynomial evaluation/rounding error. A less wasteful joint error payment
is available. If the true and reference energies both lie in the same
paid [e,U] and differ by at most epsilon_E, differentiation of the
centered polynomial gives

\[
 |P_n-\widehat P_n|\le {8\over9}
 {1-\rho^n\over e}\epsilon_E.                            \tag{8}
\]

For a complete source reference vector Ghat with norm at most sqrt(Uhat)
and uniform vector remainder eta, take
epsilon_E=2sqrt(Uhat)eta+eta^2. A reference lower bound is not assumed:
check Ehat>=e-epsilon_E and widen the common bracket before (8) if needed.
Recompute c, rho and both centered polynomial evaluations with that bracket;
the previous centering is not silently retained.
If the widened lower endpoint is nonpositive, this payment is unavailable;
refine the source error or use the explicit coefficient payment. For (7),
expand its finite polynomial in E and pay its acquired moments jointly
or with absolute coefficient errors. Source tails, spatial quadrature
and rounding are additional errors, never included in C_n by implication.

## 4. An exact common-source moment formula, with its limitation

Let f(u)=Phi(u)exp(t_0u^2), using the unchanged complete source. Here Phi
and f are real on the real source ray. For a complex-source extension the
v factors would require complex conjugation. The exact
energy is a double integral with kernel
cos(zu)conj(cos(zv))+uv sin(zu)conj(sin(zv)). Thus J_k is a **2k-source**
integral, not a collection of independent value/jet intervals.
An explicit spatial integration kernel can be derived without quadrature.
For signs sigma_l,tau_l in {+1,-1}, put
A_s=sum sigma_l u_l, B_s=sum tau_l v_l and

\[
 K(q)=\sum_{m=1}^\infty
 {6m q^m\over(m+1)(m+2)(m+3)(m!)^2}.
\]

Angular integration of exp(iA_s w-iB_s conjugate(w)) and
3 integral_0^1(1-s)(3s-1)s^m ds=6m/[(m+1)(m+2)(m+3)] give

\[
 J_k=4^{-k}\sum_{\boldsymbol\sigma,\boldsymbol\tau}
 \int_{[0,\infty)^{2k}}
 \prod_{l=1}^k\left[
 f(u_l)f(v_l)(1+\sigma_l\tau_lu_lv_l)\right]
 e^{i(A_s-B_s)a}K(R^2A_sB_s)\,d\boldsymbol u\,d\boldsymbol v. \tag{9}
\]

K is entire. Absolute convergence and Fubini follow from the complete
theta decay, or from complete integrable moments with exp(Ru) and the
first-jet frequency factors. The sign of A_s B_s is retained. Formula
(9) retains every mixed head/tail term; it does not make them positive.
The final result is real although the displayed integrand can be complex.

The [source supplier][source] and its actual-tail and reflection notes
remain authoritative. In particular a single actual tail multiplier must
serve every jet, point and source copy, and full reflection couples that
tail to the retained head. Formula (9) is an exact estimating interface,
**not a new canonical feasible-set restriction**. Applying the existing
constraints to improve a complete endpoint or prove cheaper acquisition
is still WGI-02's substantive open part. No 2k-dimensional integration
campaign is justified by writing this identity.

## 5. Exact bounded control: what fails and what survives

Take H(t,z)=z^2-2t, a=0, P=1, ambient r_*=d_*=1 and
h=D_2=2, D_3=D_4=0. These are valid complete polynomial data. The
inherited sufficient construction gives exactly

\[
 R=1/8,\quad d=1/2048,\quad t_0=1/8192,\quad
 M=65/4096,\quad\varepsilon=1/4,\quad
 e=1/16777216,\quad U/e=1052801=2^{20}+65^2.
\]

The direct coarse Green cap in (3) is 8257/3200<3. Meanwhile the
range cap is (4/9)log(1052801)>160/27>5: use log 2>2/3, obtained by
integrating the positive geometric series for 2atanh(1/3). Thus the
range-only estimator **loses on this fixed control**, even before the
direct comparator uses its exact polynomial data. This is not universal
domination over all admissible R or all log estimators.

For (5), rho=526400/526401. For every 1<=n<=10000, Bernoulli's inequality
gives the lower bound on the declared remainder allowance

\[
 T_n\ge {8\over9}{526401-(n+1)\over n+1}
 \ge {4131200\over90009}>45.                              \tag{10}
\]

Hence this standard uniform remainder cannot pay even 1/100 at those
degrees. This lower-bounds the **allowance**, not the actual truncation
error or acquisition complexity. Do not continue degree tuning within
that declared range hoping for its certified tail to pass.

The Chebyshev candidate survives this screen: sqrt(1052801)<1027 gives
r_C<513/514. At n=4096 its allowance is at most

\[
 {16\over9}{514\over4097}(513/514)^{4097}<1/10000.         \tag{11}
\]

The [exact rational replay][checks] verifies the inequality by integer
arithmetic. It is a polynomial-control remainder check, not a theta
acquisition or a complete interval for M_psi. Thousands of coupled
moments and their full errors remain unacquired; no advantage over the
equally informed direct method follows. No actual integral or measured
speedup is reported.

## 6. Endpoint atoms, controls and disposition

At an m-fold H zero, factor the original vector as
(H,H_z)=(z-a)^{m-1}Gtilde, Gtilde(a)!=0. Distributionally
Delta log E/(4pi)=g_2 dA/pi+(m-1)delta_a. Green with the C^2 weight
therefore retains the atom (m-1)psi(a). There are no atoms at t_0 here.
At the quadratic endpoint the canceled smooth density is
4/(|z|^2+4)^2, and a normalized unit atom remains at zero. The estimates
using e>0 are not passed to that endpoint. H=z supplies positive smooth
Gauss density with no common zero; it fails the ordinary-double premise.

| Matching control | What the generic calculation does; failed canonical premise |
| --- | --- |
| Quadratic/Hermite event germs | Retains their event and completed atom; the quadratic supplies (10)–(11). They lack the unchanged theta source. |
| Euler-factor sources | Applies on their own verified ordinary-double windows; the original Euler coefficients/completion have changed. |
| Weighted-square / finite-prime controls | Uses their own event constants, not theta constants. Full normalized reflection and the unchanged full coefficient sequence fail. Finite-source perturbations are not assigned an all-real heat slice. |
| Reflected super-Gaussian / positive-primitive controls | Retains the established analytic collisions. Their source fails the unchanged normalized integer-square theta expansion. |
| RH-conditional close normalized endpoint controls | Retains the stated positive-time real-root regime and endpoint doubles; ordinary Dirichlet-series arithmetic fails. No common fixed-height event is assigned to the whole family. |

No exclusion estimate is proposed, so these identities should retain the
matching collisions. Smooth-density/two-channel Weil controls concern a
different consumer: no exact transform to the full Weil form is supplied.

**Disposition.** WGI-01 is partial: its analytic slice/weight/comparison
design is paid, but the numerical acquisition schedule remains unfrozen
and gated. WGI-02 has complete
generic coupled enclosure formulas, but no new canonical signed gain.
WGI-03 has two precisely scoped control screens, not its acceptance result.
WGI-04 remains gated. The next useful task is a low-cost coupled residual
or moment enclosure using the actual shared source, compared against
direct density with the same correlations. A better approximation tail
alone does not complete that task. No manuscript or RH/simplicity milestone
is declared.

[program]: ../research-overview/01_WEIGHTED_GREEN_INTEGRALS_PROGRAM_20261022.md
[progress]: ../research-progress/01_WEIGHTED_GREEN_INTEGRALS_PROGRESS_20261022.md
[n03]: ../../notes/03_COMPLETE_PHYSICAL_BOUNDARY_AND_CRITICAL_VALUE_WINDING_20261022.md
[n05]: ../../notes/05_TARGET_INVENTORY_AND_FINITE_REGULATOR_GAUSS_COMPARISON_20261022.md
[source]: ../../02_theta_source_constraints/README.md
[checks]: ../numerics/WGI_OPENING_CHECKS_20261022.json
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md

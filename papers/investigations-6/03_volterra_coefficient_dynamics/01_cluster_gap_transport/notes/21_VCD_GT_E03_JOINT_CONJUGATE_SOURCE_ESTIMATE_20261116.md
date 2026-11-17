# VCD-GT-E03 r5 — A joint conjugate exterior estimate on one tube

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance, chat0003 continuation. Helper
dispatched **gpt-6.1-sol / ultra** under the frozen request. Separate
backend attestation and actual lead settings are unavailable.

**Proved in-note conditional on the stated enlarged geometry.** The
zero strip and growth are inputs for the unchanged complete canonical
field. The product formula supports a signed local estimate with a
finite lower-mass test. The reflected pair pays the sign and falls
short of the frozen magnitude. This is an analytical proof-author
return. The enlarged geometry is tested separately under the fixed
E04 request. [Decision07][decision] · [E03 r5][request] ·
[Source-use record][sources] · [Results][results] · [Controls12][controls] ·
[Avoid index][avoid] · [01][classification] · [02][premises] ·
[07][scope] · [12][bounds]

## 1. Strip, order and the deflated sum

Keep the entire \(G_t(z)=e^{\pi a/8}H_t(z)\), \(a=140101/10\),
\(t\in I=[0,1/10]\), in the physical heat convention
\(\partial_t H_t=-\partial_z^2H_t\). The checked strip theorem in
[Reference03][sources] applies with the initial width one, since
\(H_0(z)=\xi((1+iz)/2)/8\) and
\(\Re((1+iz)/2)=(1-\Im z)/2\). The double-exponential source
envelope supplies the transform and decay hypotheses. De Bruijn's
contraction gives \(|\Im\rho|\le\sqrt{1-2t}\le1\) for every zero
on each slice. The estimate allows nonreal and repeated zeros.
The constant gauge has no effect on the zeros or \(K\). [Note12 §1][note12]

For completeness, write \(r=|z|\). The source envelope bounds the
absolute integrand, up to a fixed multiplier, by
\(\exp(9u+u^2/10+ru-\pi e^{4u})\) on \(u\ge0\).
Absorb \(9u+u^2/10\) into a constant plus \((\pi/2)e^{4u}\).
Keep the integrable factor \(\exp(-(\pi/4)e^{4u})\).
The remaining exponent is bounded above by
\((r/4)\log_+(r/\pi)\), as follows by maximizing
\(ru-(\pi/4)e^{4u}\) on \(u\ge0\); set this upper bound to zero at
\(r=0\). Thus \(\log M_t(r)=O(r\log(2+r))\) uniformly on \(I\).
This gives order at most one. The positive source has
\(H_t(0)\ge H_0(0)>0\) for \(t\in I\).
Jensen's formula on radius \(2r\) bounds the zero count on radius
\(r\) by \(O(r\log(2+r))\) since each zero inside \(r\) contributes
at least \(\log 2\). A dyadic sum gives
\(\sum_{|\rho|>r}|\rho|^{-2}=O(\log(2+r)/r)\) as \(r\to\infty\).
The standard order-one Hadamard factorization in the checked
source passage can therefore be used with genus-one factors,
and logarithmic differentiation converges locally uniformly off
the zeros. [Reference03 §2][sources]

Let \(z_1,z_2\) be the multiplicity-counted pair inside the original
contour and let
\[
 c=\tfrac12(z_1+z_2),\qquad
 D=\tfrac14(z_1-z_2)^2,\qquad
 Q=(z-z_1)(z-z_2),\qquad A=G_t/Q.
\]
The real center and radius of the contour and conjugation of the
field give real \(c,D\), including for a conjugate pair. Hadamard
factorization writes \(G_t'/G_t\) as a constant plus the terms
\(1/(z-\rho)+1/\rho\). For a field with zeros at the origin the
separate factor \(z^m\) contributes \(m/z\); the canonical field
has none there. Deflating subtracts \(Q'/Q\), including both poles
at a double. The contour of \(A'/A\) divided by \(Q\) gives the
divided difference at \(z_1,z_2\), or its derivative at a double.
The constants cancel and hence
\[
 \boxed{\quad -K
 =\sum_{\rho\ {\rm exterior}}\frac{1}{(z_1-\rho)(z_2-\rho)}.\quad}
 \tag{1}
\]
The tail terms are \(O(|\rho|^{-2})\) uniformly for pair offsets in
a compact disk, and the counted collar excludes the finite poles
there. These facts justify termwise divided differences and the
derivative at a double, for example by integrating on the counted
contour. The formula requires neither labels across time nor an
inverse internal gap. This argument applies on each slice to real
entire fields of order at most one with a counted pair. For general
order at most one, the bound \(\log M(r)=O(r^{1+\epsilon})\) with
\(0<\epsilon<1\) likewise suffices for the inverse-square summability
by Jensen after removing any zero at the origin.

## 2. Positive omitted mass after grouping by conjugation

Assume in addition an auxiliary disk \(|z-a|<R_0=8/5\) contains
exactly the target pair throughout \(I\), with a zero-free boundary,
and
\[
 |c-a|\le C=7/100,\qquad |D|\le d=1/5,\qquad
 |\Im\rho|\le\delta=1.
 \tag{2}
\]
The original target contour remains at \(9/10\). For an exterior
\(\rho=c+x+iy\), the product in (1) is \((x+iy)^2-D\).
A conjugate pair contributes \(2q(x,y,D)\), where
\[
 q(x,y,D)=\frac{x^2-y^2-D}{(x^2-y^2-D)^2+4x^2y^2}.
 \tag{3}
\]
A real zero contributes \(q(x,0,D)\). These equalities include
multiplicities, since conjugate poles have equal multiplicities.
The paired expression is the real part of the original reciprocal.

The auxiliary disk and vertical bound give
\[
 |x|\ge |\Re\rho-a|-|c-a|
 \ge \sqrt{R_0^2-\delta^2}-C
 = X=\frac{\sqrt{39}}{5}-\frac7{100}.
\]
As \(\sqrt{39}>6\), \(X>113/100\) and
\(X^2>12769/10000>6/5=\delta^2+d\).
Consequently every term (3) is strictly positive. Absolute
convergence in (1) permits grouping and the entire contribution of
the unselected groups can be omitted in an upper estimate of \(K\).
The old radius \(21/20\) fails this particular sufficient
disk-to-horizontal test, since
\(0<\sqrt{41}/20-C<1\). A larger zero-free region and the bounds
(2) require the new geometry certificate.

For a finite counted multiset of exterior zeros invariant under
conjugation, suppose \(L\le |x|\le U\) with
\(L^2>\delta^2+d\). Then the numerator of (3) is at least
\(L^2-\delta^2-d\), and the denominator is at most
\((U^2+\delta^2+d)^2+4U^2\delta^2\). The lower weight per zero is
\[
 m(L,U)=\frac{L^2-\delta^2-d}
 {(U^2+\delta^2+d)^2+4U^2\delta^2}>0 .
 \tag{4}
\]
For \(n\) occurrences this contributes at least \(n m(L,U)\).
A nonreal pair contributes two occurrences even if its two roots
are enclosed by one box. Each occurrence may be used once only.
A uniform estimate uses independently verified counts and ranges
for each time, with disjoint selected multisets and exterior
windows that exclude the target and any separately retained group.
The estimates accommodate multiplicity changes inside the
selected windows without tracking individual zeros.

## 3. The reflected group and the magnitude test

Evenness of the complete field supplies the exterior multiset
\(\{-z_1,-z_2\}\), disjoint from the target disk because the target
lies near the positive \(a\). This selected group needs no second
transported cluster or source evaluation. Its contribution to
\(-K\) is exactly
\[
 \frac{1}{(2z_1)(z_1+z_2)}+
 \frac{1}{(z_1+z_2)(2z_2)}
 = \frac{1}{2z_1z_2}=\frac{1}{2(c^2-D)} .
 \tag{5}
\]
The denominators are nonzero because the pair is close to \(a\) and
\(c^2-D\ge(a-C)^2-d>0\). Equation (5) counts both occurrences at a
reflected double. Since \(c^2-D\le(a+C)^2+d\), (1)–(5) imply
\[
 K\le-\kappa_0-\sum_j n_j m(L_j,U_j),\qquad
 \kappa_0=\frac{1}{2((a+C)^2+d)}
          =\frac{5000}{1962848636289},
 \tag{6}
\]
where the sum excludes the reflected pair and has the disjointness
and range requirements from §2. No such additional finite-group
count is acquired in this execution. The required additional
lower mass for the useful target is \(59/100-\kappa_0\).

The mirror alone gives \(2\cdot10^{-9}<\kappa_0<3\cdot10^{-9}\).
For \(v-u=1/10\), the corresponding constant-drift upper cost
allowance satisfies
\[
 B(-\kappa_0)=2\int_u^v e^{-4\kappa_0(v-t)}\,dt
 \ge \frac15-\frac{\kappa_0}{25}
 >\frac{179}{1000}.
 \tag{7}
\]
The inequality follows from \(e^{-x}\ge1-x\). The already paid
incoming \(D(v)<179/1000\) rules out success of the mirror-only
constant allowance against any incoming lower bound. Equation (7)
is a lower bound on that allowance. The actual signed cost can be
smaller and [Note15][note15] already certifies the local passage
using the full drift. The present proof uses neither its old \(K\)
enclosure nor the direct \(D(0)>0\) result to obtain the new sign.

The lower mass in (4)–(6) has the correct direction for an upper
bound on \(K\). An upper exterior inverse-square sum in the
all-real class gives a lower force bound, as in [OA Decision08 §2][oa].
The direct comparator receives the same source array, strip,
geometry, \(c,D\) enclosures, scalar gap law and any counted
exterior groups. Its existing local endpoint and interval-minimum
enclosures remain stronger than what the mirror alone supplies.
[Note20][note20]

## 4. Exact even quartic on the same slab

Use this analytic heat-field control with the same fixed \(a\).
Put \(\tau=t-1/20\) and set
\[
 F(t,z)=e^{-\tau\partial_z^2}(z^2-a^2)^2
 =z^4-(2a^2+12\tau)z^2+a^4+4a^2\tau+12\tau^2.
\]
The terminating expansion, or direct differentiation, gives
\(\partial_tF=-\partial_z^2F\). It is globally even, real under
conjugation, and has order zero. At \(t=1/20\) it has a double
at each of \(a,-a\), with \(F_{zz}(t,a)=8a^2\ne0\).

For every \(|\tau|\le1/20\), the quadratic in \(z^2\) has roots
\(a^2+6\tau\pm S\) with \(S^2=8\tau(a^2+3\tau)\).
Since \(a>10\),
\[
 |S|^2\le \tfrac25(a^2+\tfrac3{20})<\tfrac49a^2,\qquad
 |6\tau\pm S|\le \tfrac3{10}+\tfrac23a<\tfrac7{10}a.
\]
Both squared roots have positive real part. Take \(z_1,z_2\)
to be their square roots with positive real part. Then
\(|z_i+a|\ge a\) and
\(|z_i-a|=|6\tau\pm S|/|z_i+a|<7/10\).
The other roots are their negatives, counted with the same
multiplicities. Thus the target count is two within \(3/4\),
the remainder of the radius-\(8/5\) disk is empty with its
boundary free of zeros, and the global strip holds since
\(7/10<\sqrt{1-2t}\) throughout \(I\).

Writing \(w_i=z_i-a\), averaging
\(2a w_i=6\tau\pm S-w_i^2\) gives
\[
 |c-a|\le\frac{3/10+(7/10)^2}{2a}=\frac{79}{200a}<C .
\]
Also \(D=S^2/(z_1+z_2)^2\), and
\(|z_1+z_2|\ge2a-7/5\ge9a/5\). Hence
\[
 |D|<100/729<d .
\]
The sum \(z_1+z_2\) is positive real, by conjugation and our
choice of half-plane. Therefore \(D\) has the sign of \(\tau\)
away from zero. By (5) the exact drift for this quartic is
\[
 K=-\frac{1}{2(c^2-D)}<0 ,
\]
since its only exterior group is the reflected pair. With the
positive weight \(W(t)=e^{4\int_t^vK}\), the exact gap law gives
\(D(v)-2\int_u^vW=W(u)D(u)<0\) across the double, and equality if
the cost starts at \(1/20\). The control meets the used order,
strip, geometry and sign hypotheses and fails the strict
incoming-cost premise. It is a polynomial heat field, unbounded
on the real axis, which excludes a Fourier representation by a
finite nonnegative source measure. [Gap law and cost][cost]

For the nonzero \(\kappa\) examples in [Note18][note18], the
deflated factor contains \(\exp(\kappa(z-a)^2/s)\). For each
slice this gives growth of order two along the real direction
if \(\kappa>0\), and along the imaginary direction if \(\kappa<0\).
Its quadratic exponential term contributes the nonzero
\(2\kappa/s\) through the divided difference of its logarithmic
derivative, while there are no exterior zeros. These analytic
examples fall outside the order hypothesis leading to (1).

## 5. Enlarging the tensor error disk

Keep the radius-\(\rho=9/10\) samples and their error radius
\(\varepsilon_s\), \(N=128\), both degrees \(32\), and the
majorant \(M_5\) on radius \(5\). The derivation of Note14 (4)–(5)
works for \(R=8/5<5\). The DFT identity and coefficient Cauchy
bound use \(k<128\) and \(R<5\). The time interpolation norm
uses the same Lobatto nodes, and at the new spatial radius
the Cauchy disk for the \(66\)th derivative has radius \(5-R=17/5\).
Consequently the exact same tensor polynomial \(P\) satisfies
\[
\begin{split}
 E(8/5)={}&65\left[
   \varepsilon_s\sum_{k=0}^{32}(16/9)^k+
   M_5\frac{(9/50)^{128}}{1-(9/50)^{128}}\sum_{k=0}^{32}(8/25)^k+
   M_5\frac{(8/25)^{33}}{1-8/25}\right]\\
 &+\frac{M_5\,66!}{33!\,(17/5)^{66}}\,2^{-31}(1/20)^{33},
 \qquad
 |G_t(a+w)-P(t,w)|\le E(8/5).
\end{split}
\]
The bound covers all \(|w|\le8/5,\ t\in I\), with the existing
coefficient rounding payment if rounded coefficients are treated as
exact values. For geometry, a sufficient gate is a strictly positive
real lower bound for the signed normalized ratio, with the new disk
error divided by \(R^2\) on the outer circle. A failed gate does
not establish the presence of another zero. The original moments
for \(c,D\) retain their separate original \(E(21/20)\) and
annular log bounds. The derived formula supplies no particular
geometry verdict by itself. [Note14 §§1–4][note14]

## 6. Screening the used premises

The relevant generic inputs are reality, order, a global strip, the
enlarged counted disk and pair bounds. Evenness supplies the
reflected group. The physical heat law and the strict incoming
margin are further inputs to a passage certificate. Source
equality supplies the canonical instance without assuming that
every changed source fails one of these generic inputs.
See [Controls12][controls] and [Note18 §4][screen18] for the
distinct arithmetic, observation and profile failures.

One conclusion about the bounded-strip premise follows from the
existing endpoint analyses of positive finite square-source
changes and the normalized finite-prime orbits. Their nonzero
first odd endpoint survives the even heat weight. At any fixed
time, integrating the cosine transform by parts two derivatives
beyond that endpoint gives \(A z^{-p}+O_Y(|z|^{-p-2})\) uniformly
for \(|\Im z|\le Y\), with \(A\ne0\). The remainder uses the
integrability of the differentiated heat-weighted source against
\(e^{Yu}\), supplied by double-exponential decay. Thus each
horizontal strip contains only finitely many zeros. The finite
changes have infinitely many zeros by the growth argument in the
[finite-source audit][finite]. For the positive bounded-coefficient
prime orbits the same argument applies. The first nonzero mode
dominates the source tail, giving lower growth
\(\log H_t(iy)\ge(y/4)\log y-O_t(y)\) by the same positive
Laplace interval, and the order bound follows from the upper
source envelope. A finite zero set would imply exponential type
by Hadamard factorization. The zeros in these specified
endpoint-defective classes therefore escape every horizontal
strip. This deduction does not apply to arbitrary changed sources.
[Finite-prime orbit endpoint proof][orbits]

| Control | Used premise shared, failed or still untested |
| --- | --- |
| Euler-factor translates | The order bound and the entire real even heat flow are shared. In the \(0<c<1\) family the factor at \(t=0\) has zeros at imaginary offset \(\pm\delta_p\), so the slab width-one test fails when \(\delta_p>1\). For \(\delta_p\le1\) the initial width and the same contraction theorem pay the strip. The local enlarged disk and useful lower mass are untested for either case. [Euler-factor source][euler] |
| Three- and four-weighted-square controls | Their cosine fields are real even, solve the heat equation, and have order one. The first nonzero odd endpoint of the half-line source gives the strip failure above, despite matching their respective finite endpoints and having certified events at other locations. |
| Reflected super-Gaussian | Globally even physical heat flow survives. Its positive \(e^{-u^4}\) component gives super-order-one growth at every slice, since on \(u\in[(y/4)^{1/3},(y/4)^{1/3}+1]\) the exponent \(yu-u^4+(t-1/4)u^2\) is bounded below by a positive constant times \(y^{4/3}\) for large \(y\). The order hypothesis fails. [Reflected source][reflected] |
| Smooth shape and positive primitive | The positively double-exponentially damped constructions share the real even heat field and the order bound by their source envelopes. Their undamped Gaussian-polynomial precursor has order two. No common strip, enlarged tube or useful lower mass for the damped controls follows from their collision and primitive data. |
| Reflection rigidity and four-family comparison | Full reflection plus the normalized endpoint forces unit weights in the stated polynomially weighted square-comb class. The four-family order and strip outcomes are the separate rows for weighted squares, reflected control and Euler factors. The rigidity conjunction is separate from the generic hypotheses in §2. |
| Finite-source measurement audit and canonical-score refinement | Positive nonzero finite changes with theta or zero tail, including the finite canonical-score changes, share a real even heat field and order one. Their endpoint and growth give the strip failure above even when finitely many prescribed data remain exact. |
| Finite-prime orbit controls | These real even order-one heat fields share the finite data of the orbit construction. Their bounded positive coefficients and nonzero odd endpoint give the strip failure above. The high-gap event statements provide no prescribed location in the Lehmer disk. |
| BW-01 fixed-event and exact finite-profile threshold controls | The real even finite-atom fields, and the compact continuous extensions of the finite-profile constructions, have order at most one by compact support. The recorded BW-01 event is at \(20\) and the matched-profile events are at their prescribed locations. Slab width, enlarged empty disk and usable incoming and lower-mass budgets for this tube are untested. The BW-01 all-real statement begins at its threshold and does not pay the earlier slab. |
| RH-conditional normalized endpoint control | Under RH the normalized merger shares the order bound via its bounded relative density and the strip via real zeros throughout this slab. Its added doubles escape to infinity, so the enlarged disk and extra lower-mass estimates are untested here. In a qualifying tube starting at an added double the exact incoming-cost margin is zero. This row uses the normalized merger and keeps its RH premise. |
| Fixed theta amplitude with varied observation kernel | The varied observations lack the literal cosine/Newman equation. The actual field's order, strip and counted divisor cannot be assigned to the new observation from raw compatibility or a finite cosine prefix. |
| Actual-theta three-profile relaxation | The fractional masses do not furnish the multiplicity-counted divisor of a specified analytic heat field. Neither (1) nor the finite integer counts in (4) follow from the measured profiles. |
| Exact polynomial and Gaussian controls | The even quartic in §4 shares all structural hypotheses and has negative \(K\), with the witnessed strict passage failure. Its \(K\) also lacks the useful magnitude \(59/100\), since \(c^2-D\ge(a-C)^2-d>1\). The earlier exact quadratic has no reflected companion about the global origin, and the nonzero Gaussian examples fail order as shown above. |

The estimate concerns the fixed conditional tube and signed direction.
The missing ingredient for a useful cost from this source estimate is
an independently paid lower contribution beyond the reflected group.
No scan, new source evaluation, or exterior zero count was used to
establish these conclusions.

[request]: ../research-progress/handoffs/VCD-GT-E03-r5.md
[decision]: ../brainstorm/notes/07_VCD_GT_B06_JOINT_CONJUGATE_SOURCE_DECISION_20261116.md
[sources]: ../references/03_VCD_GT_STRIP_PRODUCT_SOURCE_USE_20261116.md
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[classification]: ../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[bounds]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[note12]: 12_VCD_GT_E08_CANONICAL_XI_ORACLE_20261116.md
[note14]: 14_VCD_GT_E09_TENSOR_CERTIFICATE_BOUNDS_20261116.md
[note15]: 15_VCD_GT_E04_CERTIFIED_SIGNED_GAP_20261116.md
[note18]: 18_VCD_GT_E03_SOURCE_MODE_ALLOWANCE_20261116.md
[note20]: 20_VCD_GT_B06_SYNTHESIS_AND_CONTINUATION_20261116.md
[screen18]: 18_VCD_GT_E03_SOURCE_MODE_ALLOWANCE_20261116.md#4-control-premises
[cost]: 12_VCD_GT_E08_CANONICAL_XI_ORACLE_20261116.md#5-signed-primitive-time-cost-and-exact-control
[euler]: ../../../../investigations-2/active/19_euler_factor_controls/manuscript/euler_factor_controls.tex
[reflected]: ../../../../investigations-2/active/22_theta_manifold_geometry/notes/05_control_families/04_REFLECTION_POSITIVE_SOURCE_COLLISION_AND_MIXED_SECTORS_20261015.md
[finite]: ../../../../investigations-3/07_source_measurement_audit/notes/round-2/01_REVIEW_RECONCILIATION_AND_ENDPOINT_NONREALITY_CODEX_20261017.md
[orbits]: ../../../../investigations-3/11_arithmetic_collision_rigidity/notes/03_FINITE_PRIME_COMPATIBLE_COLLISION_CONTROLS_CODEX_20261018.md
[oa]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/03_collision_constraints/notes/08_TND_OA_B03_LEHMER_DIRECTION_AND_ACQUISITION_STOP_20261109.md

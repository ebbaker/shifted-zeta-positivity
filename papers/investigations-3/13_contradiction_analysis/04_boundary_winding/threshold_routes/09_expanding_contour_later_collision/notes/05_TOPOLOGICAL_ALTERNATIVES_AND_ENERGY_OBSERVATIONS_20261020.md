# Topological alternatives and energy observations

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Model **gpt-6-astra (Codex)**, actual reasoning
effort **ultra**, verified from recorded turn metadata.

**Status: comparative assessment and exact identities proved in-note;
no new theta estimate.** The signed later-collision estimate remains open.
The [result index][results], [geometry cluster][geometry], [control
screen][screen] and [avoid index][avoid], especially [target
reformulations][a01], [control premises][a02] and [scoped conclusions][a07],
govern this assessment. No novelty priority is asserted.

## 1. Winding exhausts the topology of this boundary field

On a complete nonvanishing boundary loop, the physical first jet
\(J=H+iH_x\), or its paid regularization \(Z=J/L\), maps a circle to
\(\mathbb C^\times\). Radial retraction to \(S^1\) shows that its homotopy
class is classified by the integer winding. This is a statement about
these boundary data, not about every possible invariant of the heat flow.
With several boundary components one has a winding for each component;
their oriented sum gives the total interior index.

The following alternatives do not add homotopy information to one such
loop:

* The projective direction \([H:H_x]\in\mathbb{RP}^1\), identified with
  the circle by \((H+iH_x)^2/(H^2+H_x^2)\), has degree \(2W_J\).
* Root counts with moving-wall flux recover the same index accounting.
  The [root-wall cap identity][n3] is one exact computational form.
* A spectral-flow or Maslov-index formulation would require an additional
  operator or geometric realization. Any advantage must come from
  estimates available in that realization.

These conclusions agree with the existing [projective-jet note][projective]
and [wall-flux note][walls]. Passing to a larger target space cannot be
assumed to preserve the obstruction: for example, a freely filled loop in
\(\mathbb{CP}^1\) has no fundamental-group obstruction.

A complex spatial argument-principle contour could instead certify
nonreal zeros at a later time. That uses additional complex data and gives
a different contradiction to future all-realness. It does not strengthen
the homotopy invariant of the present real spacetime boundary.

## 2. The signed Laguerre form is the closest energy-like quantity

Assume throughout that \(H_t=-H_{xx}\), with enough real derivatives for
each displayed identity. Put

\[
 E=H^2+H_x^2,\qquad Q=H_x^2-HH_{xx}.
\]

For any local phase \(\phi=\arg J\) where \(E>0\), direct differentiation
gives

\[
 \phi_x=-\frac{Q}{E},\qquad
 \phi_t=\frac{Q_x}{E},\qquad
 Q_x=H_xH_{xx}-HH_{xxx}.                         \tag{1}
\]

Thus \(Q\) is signed angular information, not a positive norm. The
complete contour integral of the one-form
\(-Q\,dx/E+Q_x\,dt/E\) computes physical phase; every wall and cap must
still be included. For \(Z\), subtract the reference phase and retain the
established apex treatment.

In the relevant Laguerre–Pólya class, all-realness implies \(Q\ge0\).
A conditional estimate giving \(Q<0\) somewhere at \(t>T=\Lambda\) would
therefore contradict the assumed threshold directly. It need not first
produce a later real multiple zero on the chosen BW09 contour. This is
the existing [BW-05 route][bw05], not a newly established criterion.
Its [local forward exclusion][local-q] already proves \(Q>0\) in an
event-dependent neighborhood of an ordinary double event, so any negative
witness must extend beyond that neighborhood.

There is no closed scalar sign evolution supplied by the heat equation:

\[
 Q_t+Q_{xx}=2(H_{xx}^2-H_xH_{xxx}).               \tag{2}
\]

The right side is the next derivative's Laguerre form, whose sign also
needs input. Equation (2) is not a forward maximum-principle proof.

## 3. A localized signed energy is a concrete alternative estimate request

Fix a nonnegative \(C_c^2\) spatial weight \(\psi\). Integration by parts
gives the exact identity

\[
 A_\psi(t):=\int_{\mathbb R}\psi Q\,dx
 =2\int_{\mathbb R}\psi H_x^2\,dx
       -\frac12\int_{\mathbb R}\psi''H^2\,dx.     \tag{3}
\]

Indeed, integrating \(-\psi HH_{xx}\) once gives
\(\psi H_x^2+\psi'HH_x\), and the latter term integrates to
\(-\psi''H^2/2\). On a finite interval the omitted endpoint term is
\([-\psi HH_x+\psi'H^2/2]_a^b\). Compact support pays it exactly.
One can also integrate (3) against a nonnegative compact time weight,
with support strictly after \(T\), or use a compact spacetime weight and
replace \(\psi''\) by \(\psi_{xx}\).

A strictly negative \(A_\psi\) implies \(Q<0\) somewhere in the support.
The possible practical advantage is that the right side needs only
\(H,H_x\), not pointwise \(H_{xx}\), and involves one signed scalar
functional rather than a full winding certificate. It may also average
oscillation. Neither advantage is yet measured for theta; cancellation
and complete error payments may offset them. Narrowing the support also
increases derivatives of the weight, which can amplify the second term's
error.

The ordinary unweighted energy cannot have the desired sign. Whenever
the integrals converge and endpoint terms vanish,

\[
 \int_{\mathbb R}Q\,dx=2\int_{\mathbb R}H_x^2\,dx\ge0.             \tag{4}
\]

There is a second useful screen on test functions. Write
\(w_t(u)=e^{tu^2}\Phi(u)\ge0\) for the complete theta cosine source. The
source decay permits differentiation and the exchanges below on compact
time intervals. Symmetrizing the two-source product gives

\[
 Q(t,x)=\frac14\int_0^\infty\!\!\int_0^\infty w_t(u)w_t(v)
 \left[(u+v)^2\cos(x(u-v))+(u-v)^2\cos(x(u+v))\right]\,du\,dv.    \tag{5}
\]

If an integrable test \(\psi\) has a nonnegative cosine transform
\(C_\psi(\omega)=\int_{\mathbb R}\psi(x)\cos(\omega x)\,dx\)
for every real \(\omega\), then (5) makes \(A_\psi\ge0\) for every
nonnegative source satisfying the integrability hypotheses. A Gaussian
centered at \(x=0\) is one example. Such a test cannot be a negative-average
witness. A localized test near the hypothetical event height must retain
its oscillatory cosine factors; source positivity does not determine
their signs.

**Classification and next request.** Existence of some nonnegative weight
with negative average merely repackages existence of a negative point.
A meaningful new task is to select one explicit weight and separated-time
window, use the unchanged complete theta source and the hypothetical
event constraints, and obtain a strictly negative bound including all
source, parameter and numerical errors. Compare its cost and margin with
the strongest same-data pointwise BW-05 estimate and direct contour
consumer. No weight, window or negative theta margin is certified here.
This is an alternative acquisition proposal, not another completed BW09
milestone.

## 4. Positive jet energy and critical-value energy do not force return

The ordinary squared jet satisfies

\[
 E_t+E_{xx}=2(H_x^2+H_{xx}^2).
\]

For differentiable walls \(a(t)<b(t)\),

\[
 \frac d{dt}\int_a^b E\,dx
 =-[E_x]_a^b+2\int_a^b(H_x^2+H_{xx}^2)\,dx
       +b'E(t,b)-a'E(t,a).                       \tag{6}
\]

With periodicity or justified vanishing endpoint terms its spatial
integral grows in forward time. With moving walls their fluxes have no
automatic favorable sign. This identity is useful for amplitude and
denominator bounds, but supplies no generic later-collision mechanism.

Along a nondegenerate stationary branch \(H_x(t,b(t))=0\),
\(H_{xx}(t,b(t))\ne0\), put \(V(t)=H(t,b(t))\). Then

\[
 b'=\frac{H_{xxx}}{H_{xx}},\qquad
 V'=-H_{xx},\qquad
 \frac d{dt}\frac{V^2}{2}=Q(t,b(t)).               \tag{7}
\]

In an all-real regime this critical-value square is nondecreasing.
Moreover, on a connected nondegenerate branch the sign of \(H_{xx}\)
cannot change, so \(V\) cannot return to its original zero. A return
argument must address branch degeneracy or different critical branches;
tracking a smooth extremum alone does not force it. No global continuation
of this branch is assumed.

## 5. Angular energy bounds magnitude, not orientation

For a nonzero piecewise smooth loop \(F(s)\), \(0\le s\le\ell\),
with a fixed arclength convention and square-integrable lifted phase
derivative, Cauchy–Schwarz gives

\[
 \mathcal A(F):=\int_0^\ell|\partial_s\arg F|^2\,ds,\qquad
 4\pi^2W_F^2\le\ell\,\mathcal A(F).               \tag{8}
\]

This bound cannot be reversed. The loop
\(F(s)=\exp(iB\sin(2\pi s/\ell))\) has winding zero and
\(\mathcal A=2\pi^2B^2/\ell\), arbitrarily large. High angular energy
does not force nonzero winding or its negative sign.

There is a useful distinction between physical and regularized contours.
On a complete physical contour surrounding the initial ordinary event
and later events of total weight \(K\), the index is \(-1-K\).
An independently established upper bound
\(\mathcal A(J)<4\pi^2/\ell\) would exclude even the initial event.
This could support a direct event-exclusion route. For the forward
regularized contour \(W_Z=-K\), however, \(K=0\) remains compatible with
arbitrarily large angular energy. A small upper bound excludes additional
winding; it does not force it. All contours require nonvanishing,
complete boundary accounting and the appropriate apex construction.

There is also a signed bulk representation, if an interior estimate is
easier. On a smooth bounded domain \(\Omega\) with \(J\ne0\) on its
boundary, orient by \(dt\wedge dx\) and put
\(\alpha_\epsilon=(H\,dH_x-H_x\,dH)/(E+\epsilon^2)\). Direct exterior
differentiation and Stokes give

\[
 d\alpha_\epsilon
 =-\frac{2\epsilon^2(H_{xx}^2-H_xH_{xxx})}
          {(E+\epsilon^2)^2}\,dt\wedge dx,
\qquad
 W_J=-\lim_{\epsilon\downarrow0}\frac1\pi
 \iint_\Omega\frac{\epsilon^2(H_{xx}^2-H_xH_{xxx})}
 {(E+\epsilon^2)^2}\,dt\,dx.                     \tag{9}
\]

The limit follows from uniform convergence of the boundary form where
\(E>0\); no exchange with a pointwise limiting interior density is claimed.
Equation (9) is the same winding expressed as signed bulk concentration.
An initial boundary event must first be excised and paid as in BW09.
An absolute-value energy discards the orientation.

## 6. Zero-interaction energy is substantial, but its direction matters

For a finite monic polynomial satisfying the backward heat equation and
having distinct real roots \(x_i(t)\), implicit differentiation and
factorization yield

\[
 x_i'=2\sum_{j\ne i}\frac1{x_i-x_j}.
\]

For \(U=-\sum_{i<j}\log|x_i-x_j|\), this gives
\(x'=-2\nabla U\) and

\[
 U'=-2\sum_i(\partial_iU)^2\le0.                 \tag{10}
\]

For bounded root configurations, a collision would send \(U\) to
\(+\infty\), contrary to this decrease from a simple starting
configuration. Thus its natural forward direction resists collision.
The argument concerns the complete finite real-root system, not just
one selected pair while ignoring other real or complex roots.

For theta's infinitely many roots, cutoffs, renormalization and exterior
terms are essential. Rodgers and Tao's
[primary paper](https://arxiv.org/html/1801.05914) demonstrates that
zero-interaction energy can produce a decisive arithmetic contradiction:
their proof establishes \(\Lambda\ge0\), assuming \(\Lambda<0\) and
deriving incompatible local zero statistics at time zero. It does not
supply the desired upper bound \(\Lambda\le0\), or a uniform estimate at
a hypothetical positive threshold. See also the repository's
[direction-of-implication review][literature].

An energy route here would need a new quantitative conflict between
theta arithmetic and the allowable forward dynamics. Repulsion by itself
is compatible with the threshold hypothesis.

## 7. Control screen and decision

For \(H=h_2(y^2/2-\tau)\), \(h_2\ne0\),
\[
 Q=h_2^2(y^2/2+\tau)>0\quad(\tau>0).
\]
This exact heat control obeys (1)–(10) wherever their hypotheses apply
and has no later event. The [cubic control][n1] matching arbitrary
\(h_2\ne0,h_3\) has only simple real future roots; its polynomial
factorization gives \(Q/H^2=\sum_j(x-r_j)^{-2}>0\) off its roots and
\(Q=H_x^2>0\) at its roots. Generic heat identities and these initial
jets therefore cannot force future negative \(Q\), negative weighted
averages or an extra winding.

The two-event quartic in [Note 03][n3] has nonreal roots between its first
and second events. It fails the complete all-real-system premise of (10)
there; this is why the repulsive finite energy does not forbid its later
event. Higher-multiplicity controls require the separate physical index,
not the ordinary-double quotient.

For the nonpolynomial [screening families][screen]:

| Family | Relevant premise and scope |
| --- | --- |
| Positive atomic and finite-profile actual-threshold controls | Have an all-real future and are compatible with the same energy identities; they fail unchanged theta coefficients, full profile growth and eventual simplicity at their threshold. Source positivity or finitely many profile observations do not force later negativity. |
| Euler-factor controls | Fail the unchanged normalized theta arithmetic source. Their certified negative Laguerre witnesses occur below their own threshold; no threshold event is assigned from a lower bound alone. |
| Weighted-square and finite-prime orbit controls | Fail full source reflection; no finite all-real threshold is supplied by their collision witnesses. The finite-system repulsive-energy premise cannot be imported. |
| Reflected smooth and positive-primitive controls | Fail the unchanged normalized theta square expansion. Generic heat and positive-source identities apply, but no new all-real threshold or stationary continuation is asserted. |

These are premise screens, not a new computation on each control.
None rules out a full-source theta estimate.

**Decision:** keep winding as the topological collision detector. For a
different analytic estimate, prioritize a fixed signed Laguerre
functional or a fully paid phase-current estimate; compare the former
with BW-05. Ordinary positive energy, alternate names for degree, and
generic zero repulsion do not supply the missing theta sign. The identities
above narrow the proposed research direction but furnish no theta
exclusion, negative phase margin, or later collision.

[results]: ../../../../../../../result-summaries/README.md
[geometry]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[screen]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[projective]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/07_REAL_PROJECTIVE_JETS_AND_JENSEN_HEAT_SURFACES_20261015.md
[walls]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/06_WALL_FLUX_AND_CERTIFIED_THETA_WINDING_20261015.md
[n1]: 01_FINITE_CONTOUR_AND_SOURCE_CONTRACT_20261020.md
[n3]: 03_ROOT_FOLLOWING_WALLS_AND_CAP_COUNT_20261020.md
[bw05]: ../../05_later_laguerre_violation/README.md
[local-q]: ../../05_later_laguerre_violation/notes/02_QUANTITATIVE_FORWARD_NEIGHBORHOOD_EXCLUSION_20261020.md
[literature]: ../../../reviews/02_TARGETED_LITERATURE_REVIEW_FOR_THRESHOLD_ARITHMETIC_20261020.md

# Holomorphic reference transfer and a boundary degree prototype

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**. This note and its [review][review] were produced
by the same assistant; neither has independent mathematical review.

**Status:** the reference-transfer result below is proved in-note using
standard complex analysis and degree theory. An exact rational boundary
degree implementation passes four controls, with interpolation error paid
on every boundary tetrahedron. There is **no second theta certificate and
no established theta cost advantage** in this round.

[Note 01][note01] suggested a reference requiring both jet components,
covering two real zeros and their intervening stationary point. Before
acquiring more theta values, we screen that proposal. For a square
holomorphic reference of degree zero, its boundary norm floor is already
an interior norm floor. Thus replacing the pilot's component floor by a
full vector floor does not, by itself, escape the direct comparison.
This extends the constant-reference observation in Note 01; it does not
close computational boundary-degree methods.

The second result is a concrete alternative: compute the boundary degree
from a continuous piecewise affine approximation whose degree is found
by oriented simplex counts. Its extension need not be holomorphic or
supplied with an a priori zero-free proof. This avoids assuming the
reference degree, but calculating that degree has a cost which must be
charged. The exact models below validate the construction, not its
competitiveness for theta.

Read this with the [result index][results], [local geometry cluster][local]
and [avoid index][avoid], particularly [target classification][a01],
[control matching][a02] and [scoped exclusions][a07]. This is a finite
certificate comparison and method-development milestone. Requiring zero
charge around every physical multiple-zero candidate remains a restatement
of the exclusion target, not a new global theorem.

## 1. A minimum principle for a square holomorphic map

Let \(B\Subset\mathbb C^n\) be a bounded domain with, for definiteness,
piecewise smooth boundary, and let \(F\) be holomorphic on a neighborhood
of \(\overline B\), with values in \(\mathbb C^n\). Use Euclidean norms
and the standard complex orientations. Put
\[
 b=\min_{\partial B}\|F\|>0.                                      \tag{1}
\]
For every \(v\) with \(\|v\|<b\), the fiber
\(A_v=F^{-1}(v)\cap B\) is a compact analytic subset of \(B\): its
closure cannot reach the boundary by (1). It is consequently finite.
Indeed, holomorphic coordinate functions separate points of \(B\), so
the compact-analytic-set theorem applies. No global Stein assumption on
\(B\), and no nonsingular Jacobian assumption on \(F\), is needed.

For a finite nonempty fiber, additivity and positivity of local
holomorphic degree give
\[
 \deg(F,B,v)=\sum_{p\in A_v}\operatorname{mult}_p(F-v)>0.            \tag{2}
\]
The same degree is constant as \(v\) moves within the target ball of
radius \(b\), since that ball misses \(F(\partial B)\).

**Proposition 1.** If \(F\) has no common zero on \(\overline B\), then
\[
 \min_{\overline B}\|F\|=\min_{\partial B}\|F\|=b.                 \tag{3}
\]

**Proof.** Zero-freeness gives \(\deg(F,B,0)=0\). If an interior point
had image \(v\) with \(\|v\|<b\), (2) would give positive degree at
\(v\), whereas target homotopy to zero gives degree zero. Hence all
interior values have norm at least \(b\). Boundary attainment supplies
equality. This also handles a rank-deficient map: a hypothetical small
fiber would still be compact and hence finite. \(\square\)

Two consequences are useful here.

1. Under (1), the zero set of a holomorphic square map in \(B\) is
   automatically finite, by the same compact-fiber argument. In this
   bounded Euclidean setting, isolation is a consequence of a proved
   nonzero boundary; it need not be a separate unverified premise.
2. Under (1), \(\deg(F,B,0)=0\) is equivalent to zero-freeness in
   \(B\). Thus either a zero-free proof or a degree-zero proof permits
   (3). The latter proof may itself be expensive.

These conclusions are not being asserted for arbitrary complex manifolds
with compact analytic subvarieties.

**Literature check.** The compact-fiber ingredient is Demailly,
*Complex Analytic and Differential Geometry*, Chapter II, §5,
Theorem (5.9), printed page 104, in the author's [2012 text][demailly].
The related result that compact interior sublevel components of
holomorphic maps contain zeros is developed by Buhovsky, I. Polterovich,
L. Polterovich, Shelukhin and Stojisavljević in *Persistent transcendental
Bézout theorems*, [§2.3, Corollaries 2.9 and 2.11][bezout]. The square-map
argument above uses degree directly. No novelty or priority claim is made
for the analytic principle.

## 2. What a holomorphic reference certificate already supplies

Let \(F,G:\overline B\to\mathbb C^n\) extend holomorphically to a
neighborhood, and suppose the certified reference has degree zero and
boundary floor at least \(b>0\). Suppose also that
\[
 \sup_{\partial B}\|G-F\|\le e<b.                                \tag{4}
\]
The scalar maximum-modulus principle, applied to unit linear functionals
of \(G-F\), gives
\[
 \sup_{\overline B}\|G-F\|=\sup_{\partial B}\|G-F\|\le e.         \tag{5}
\]
By Proposition 1, \(\|F\|\ge b\) throughout \(\overline B\).
Therefore the same information yields the direct joint estimate
\[
                  \|G\|\ge b-e>0\quad\hbox{on }\overline B.       \tag{6}
\]
The boundary homotopy \(F+s(G-F)\) has the same margin and certifies
\(\deg(G,B,0)=0\). Equation (6) needs no additional theta samples,
interior mesh, or component that stays nonzero by itself.

**Scope of the comparison.** This concerns square holomorphic references
with an already established zero degree, and uniform norm bounds (1),
(4). A direct consumer given the same reference-degree proof, boundary
floor and error certificate can use (6) with the identical guaranteed
margin. The cost of establishing the reference degree belongs to both
consumers. This is a reduction of certificate information, **not** a
complexity lower bound for all boundary methods or a claim that degree
computation is free. A piecewise affine boundary approximation whose
degree still needs to be computed lies outside the supplied holomorphic
reference construction.

Likewise, if an arbitrary method first proves \(\deg(G,B,0)=0\) and
\(\|G\|\ge\eta\) on \(\partial B\), Proposition 1 then gives the
interior floor \(\eta\). This does not furnish a cheaper proof: it uses
the completed degree calculation. Relabeling that consequence as direct
exclusion would not remove its cost.

### A sharp heat model requiring both components

Use the real four-dimensional box
\[
 B_{T,R}=\{ |\Re t|,|\Im t|<T,\ |\Re z|,|\Im z|<R\},\qquad
 T=1/10,\quad R=3/2,                                             \tag{7}
\]
and
\[
 P(t,z)=z^2-1-2t,\qquad F=(P,P_z)=(z^2-1-2t,2z).                 \tag{8}
\]
This is a heat solution: \(P_t=-P_{zz}\). At time zero, \(P\) vanishes
at \(z=\pm1\), while \(P_z\) vanishes at the intervening \(z=0\).
Neither component alone has a positive norm floor on this box.

Write \(k=1+2t\), \(s=|z|^2\). On its closure,
\(\Re k\ge4/5\) and \(|k|\le\sqrt{37}/5<2\), so
\[
 \|F\|^2=|z^2-k|^2+4|z|^2
 \ge(s-|k|)^2+4s
 =|k|^2+(4-2|k|)s+s^2\ge16/25.                                  \tag{9}
\]
Equality occurs at \(t=-1/10,z=0\), on the boundary. Thus the exact
boundary and interior floor is \(b=4/5\), and the degree is zero. The
only joint event, \((t,z)=(-1/2,0)\), is outside the box.

For \(0<\eta<4/5\), the perturbed heat field
\[
 G_\eta=(z^2-1-2t+\eta,2z)                                      \tag{10}
\]
has uniform error \(\eta\) and exact joint floor \(4/5-\eta\).
Repeat (9) with \(k_\eta=1-\eta+2t\), for which
\(\Re k_\eta\ge4/5-\eta>0\) and \(|k_\eta|<2\). Boundary equality
again occurs at \(t=-1/10,z=0\). In particular, \(\eta=1/10\) gives
floor \(7/10\). This shows that (6) cannot be uniformly improved using
only \(b,e\), even within these heat fields and domains requiring both
components. For \(\eta=4/5\) the event is on the boundary; for
\(\eta=9/10\) it is at \(t=-1/20,z=0\) inside, with local charge one.
The strict inequality in (4) is essential.

### Hypotheses that cannot simply be dropped

| Removed hypothesis | Counterexample and failure |
| --- | --- |
| Equal source and target dimensions | On the unit ball in \(\mathbb C^2\), \((1,t,z):\mathbb C^2\to\mathbb C^3\) has interior minimum 1 and boundary minimum \(\sqrt2\). |
| Holomorphic reference | \((1+|t|^2+|z|^2,0)\) on that ball has interior minimum 1 and boundary minimum 2. |
| Zero degree / zero-freeness | \((t,z)\) has degree one, interior minimum 0 and boundary minimum 1. |
| Bounded compact closure | On \(\Re t<0\), \((e^t,z)\) has boundary infimum 1 and interior infimum 0. |

The first row demonstrates failure when the target dimension exceeds the
source dimension; it does not claim that every unequal-dimension version
fails. These examples delimit Proposition 1 rather than prove it.

## 3. A paid piecewise affine boundary-degree construction

The following construction computes the degree from boundary data without
requiring a known zero-free holomorphic reference. It uses the standard
real orientation \((\Re t,\Im t,\Re z,\Im z)\) in both domain and
target. Boxes have corners; Brouwer degree and boundary homotopy remain
well-defined. No smoothing or numerical differential-form quadrature is
used.

Divide each coordinate interval of (7) into \(N\) equal subintervals.
Each of eight three-dimensional faces consists of \(N^3\) cubes.
Triangulate each cube by its six increasing-coordinate (Kuhn)
tetrahedra, using the same global coordinate order on every face. The
induced subdivisions agree on shared faces and edges. There are
\[
 V_N=(N+1)^4-(N-1)^4=8N^3+8N\quad\hbox{boundary vertices},\qquad
 S_N=48N^3\quad\hbox{boundary tetrahedra}.                         \tag{11}
\]
For a translated box, use coordinates relative to its center in the
cone matrices below. Cache each vertex once. Let rational approximations \(y_i\in\mathbb R^4\)
to its field values define the continuous piecewise affine map
\(L\) on \(\partial B\).

For each boundary tetrahedron \(\sigma\), compute certified numbers
\[
 \inf_\sigma\|L\|\ge b_\sigma,
 \qquad\sup_\sigma\|G-L\|\le e_\sigma<b_\sigma.                  \tag{12}
\]
A simple conservative floor encloses the convex hull of its four vertex
images by a coordinate box. If its coordinate intervals are \(I_j\),
then
\[
 b_\sigma^2\le\sum_{j=1}^4\operatorname{dist}(0,I_j)^2             \tag{13}
\]
is a valid choice, with a downward rational square root. This covers the
whole simplex; the minimum of vertex norms alone would not suffice.
Equation (12) certifies the straight boundary homotopy and a uniform
boundary gap \(\min_\sigma(b_\sigma-e_\sigma)>0\).

Cone the triangulated boundary to the center of the box, assigning the
**artificial** target value zero to the cone vertex. This is a continuous
piecewise affine extension \(\widetilde L:B\to\mathbb R^4\), not an
approximation to \(G\) in the interior. No actual field evaluation at
the center is needed. For a boundary tetrahedron with domain vertices
\(x_0,\ldots,x_3\) and images \(y_0,\ldots,y_3\), write
\[
 X=[x_0\ x_1\ x_2\ x_3],\qquad Y=[y_0\ y_1\ y_2\ y_3].
\]
Choose a small rational target \(v\) with
\(\|v\|<\min_\sigma b_\sigma\). For every cone simplex, solve
\(Y\lambda=v\). A nonsingular solution contributes exactly when all
five barycentric weights \(1-\sum_i\lambda_i,\lambda_0,\ldots,
\lambda_3\) are strictly positive. Its contribution is
\[
 \operatorname{sgn}(\det Y/\det X).
\]
A solution on an actual simplex face, or a singular consistent system,
is rejected as an unproved regular-target choice. A singular inconsistent
system has no preimage; a nonsingular solution with a negative weight is
outside the simplex. These checks are exact rational operations.

The target segment from zero to \(v\) avoids the PL boundary by its
floor, and summing the regular contributions computes
\[
 \deg(G,B,0)=\deg(\widetilde L,B,0)
            =\deg(\widetilde L,B,v).                             \tag{14}
\]
For a face with coordinate index \(a=0,1,2,3\), outward side
\(s\in\{-1,1\}\), and Kuhn permutation \(\pi\) of its three free
coordinates, \(\operatorname{sgn}\det X=s(-1)^a\operatorname{sgn}\pi\).
This follows by subtracting the first vertex column from the other
three and expanding along the fixed coordinate. The sign controls below
check both orientations.

When \(G=(H,H_z)\) is holomorphic and has nonzero boundary, its interior
zeros are finite by Section 1 and have positive local degrees. Thus a
computed zero in (14) excludes joint zeros. For a nonholomorphic map,
zero degree need not exclude zeros; holomorphic positivity remains an
essential final premise.

## 4. Executed exact controls

The [replay script][script] uses Python's standard-library rational
arithmetic. For \(H=z^2-c-2t\), all components are affine except
\(z^2\). If \(z=\sum\lambda_i z_i\), then
\[
 \left|\sum_i\lambda_i z_i^2-z^2\right|
 =\left|\sum_i\lambda_i(z_i-z)^2\right|
 \le\operatorname{Var}(\Re z_i)+\operatorname{Var}(\Im z_i).
\]
Each free real spatial coordinate has range \(2R/N\), so its variance
is at most \(R^2/N^2\). The exact interpolation budget on a face is
therefore
\[
 e_\sigma=\bigl(2-\mathbf1_{a\in\{2,3\}}\bigr)R^2/N^2.          \tag{15}
\]
There is no source evaluation error for these rational polynomial
values. For the linear controls, the interpolation error is zero.

The [recorded receipt][receipt] reports:

| Field | \(T,R,N\) | Boundary vertices | Tetrahedra | PL floor lower bound | Maximum interpolation error | Uniform homotopy gap | Degree |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| \((t,z)\) | \(1,1,1\) | 16 | 48 | 1 | 0 | 1 | +1 |
| \((\overline t,z)\) | \(1,1,1\) | 16 | 48 | 1 | 0 | 1 | −1 |
| \((z^2-2t,2z)\) | \(1/10,1/4,2\) | 80 | 384 | \(3/40\) | \(1/32\) | \(7/160\) | +1 |
| \((z^2-1-2t,2z)\) | \(1/10,3/2,6\) | 1,776 | 10,368 | \(11/20\) | \(1/8\) | \(17/40\) | 0 |

All four controls use
\(v=(1/10007,1/10009,1/10037,1/10039)\). The first three have one
regular preimage of the indicated sign; the last has none for this
target. Every other cone simplex rejects the target as outside its
image. No singular consistent system or ambiguous face hit occurs.
The implementation makes **zero interior evaluations of the actual
field**. Its source hash, arithmetic, target and all counts are in the
receipt; elapsed times are run-specific.

For the quadratic collision, \(G=0\) only at \((0,0)\), with complex
Jacobian determinant \(-4\), so the expected degree is +1. The
orientation-reversing linear control is deliberately nonholomorphic and
checks the signed count, not holomorphic positivity. The two-root model
has no joint zero in (7), as already established in (9), so its expected
degree is zero. These independent exact descriptions are used to check
the output; the algorithm itself computes each count.

The model's direct algebraic floor \(4/5\) is stronger and much cheaper
than the PL gap \(17/40\). Thus these controls establish feasibility and
correct signs; they are not evidence of a computational gain.

## 5. Interface for the complete theta field

A future theta run must pay vertex errors and interpolation from the
unchanged complete source in [Note 01][note01]. Let \(H_j=\partial_z^jH\).
For a containing convex box with \(\Re t\le T_*\) and
\(|\Im z|\le Y_*\), the positive theta source gives complete moments
\[
 M_k=\int_0^\infty\Phi(u)u^k e^{T_*u^2+Y_*u}\,du,
 \qquad |\partial_t^a\partial_z^bH_j|\le M_{j+2a+b}.              \tag{16}
\]
All source modes and the exterior integration tail belong in (16).
Finiteness follows from the theta source's double-exponential decay.
The imaginary part of time causes no absolute growth; its real part
appears in the Gaussian factor.

For a boundary simplex and barycentric weights \(\lambda_i\), put
\(\Delta t_i=t_i-t\), \(\Delta z_i=z_i-z\),
\(V_t=\sum_i\lambda_i|\Delta t_i|^2\) and
\(V_z=\sum_i\lambda_i|\Delta z_i|^2\). Taylor expansion from the
barycenter cancels the linear terms. The heat equation and
Cauchy–Schwarz give the interpolation bound
\[
 I_j\le\tfrac12\left(M_{j+4}V_t
          +2M_{j+3}\sqrt{V_tV_z}+M_{j+2}V_z\right),\qquad j=0,1. \tag{17}
\]
Here the segment stays on the convex face and in the containing box,
so the derivative majorants apply along it. If free real coordinate
ranges are \(h_{tr},h_{ti},h_{zr},h_{zi}\), setting the fixed face
coordinate's range to zero gives
\[
 V_t\le(h_{tr}^2+h_{ti}^2)/4,\qquad
 V_z\le(h_{zr}^2+h_{zi}^2)/4.                                   \tag{18}
\]
For per-component vertex ball errors at most \(\delta_0,\delta_1\),
the interpolated source error has those same bounds by convexity. Thus
\[
 e_\sigma\le\sqrt{(\delta_0+I_0)^2+(\delta_1+I_1)^2}             \tag{19}
\]
is a complete contract for (12), provided the balls and all \(M_k\) are
certified. Derivation of (17) uses
\(H_{j,tt}=H_{j+4}\), \(H_{j,tz}=-H_{j+3}\),
\(H_{j,zz}=H_{j+2}\); taking absolute values pays the mixed term.
Neither a sampled floor nor an unvalidated derivative estimate suffices.

**Not yet executed:** no theta boundary vertex grid, interval version of
this degree consumer, or matched two-zero theta comparison has been
run. Rational midpoints from future validated balls could feed the
exact degree count, with all ball radii included in (19). This is a
proved interface, not a claim that its eventual gap will be positive.

## 6. Control screen and continuation decision

No new arithmetic exclusion premise was introduced. Proposition 1 and
the degree algorithm apply to all holomorphic control fields for which
their stated bounded-domain hypotheses hold. On a domain enclosing an
isolated control event and avoiding boundary zeros, its positive local
charge prevents a valid degree-zero conclusion. A failed floor, unpaid
error, nonzero computed degree, or unproved zero-degree reference must
block that conclusion. A collision-free domain of a control is allowed
to pass.

The fresh numerical control runs are exactly those in Section 4. The
broader [control register][controls] is screened analytically against
its existing evidence, with no new source acquisition or event-location
claim:

| Family | Premise not supplied by a theta-specific source calculation |
| --- | --- |
| Polynomial heat models and earlier counter-kernels | Unchanged complete theta source and arithmetic coefficients |
| Euler-factor controls, for every prime parameter | Unchanged Euler data; source values and errors must be recomputed for that field |
| Weighted-square and finite-prime orbit controls | Unchanged coefficients and full normalized reflection |
| Reflected super-Gaussian control | Canonical integer-square source expansion |
| Smooth shape, positive-primitive and auxiliary-channel controls | Canonical theta arithmetic; retained shape or auxiliary positivity does not supply it |
| [RH-conditional close-source endpoints][close] | Ordinary Dirichlet-series arithmetic; fixed positive tolerance alone does not exclude their escaping doubles |

For an actual enclosed event, the exclusion premise that fails is zero
charge (or some upstream assertion used to obtain it), not necessarily
holomorphicity or positivity of the source. The Euler-factor register's
Laguerre witnesses and threshold bounds are not being converted here
into a newly certified location of a joint event. Distinct control
preservation lists remain separate.

**RCH-05 is complete in-note:** the entire supplied square holomorphic
reference class has the transfer (6), and the heat example shows its
uniform margin is sharp. This supersedes the previous suggestion that
merely changing to a two-component polynomial reference might produce a
stronger uniform exclusion certificate from the same information.

**RCH-06 has an exact-model prototype:** (12)–(15) compute boundary
charge without an a priori holomorphic reference degree. Complete theta
application and a useful cost comparison remain open. Before a large
acquisition, fix a thin complex-time box with two neighboring real theta
zeros and their stationary point, certify that real slice, and estimate
(17)–(19) at a declared mesh/precision budget. Compare with direct joint
exclusion using the same acquired values and complete moments; allow the
direct method to reuse any polynomial or interval information. Count
source work, all boundary tetrahedra and degree arithmetic. Stop that
implementation if it cannot pay its whole boundary or offers no useful
coverage/cost gain. Adaptive cells or other boundary algorithms remain
outside such an implementation-specific stop.

Arbitrary-height coverage, unwanted complex-time events and exhaustion
boundaries are still open. RCH-04 remains gated; HMC-05/06 retain their
inherited statuses. The [progress register][progress] records both this
round and the first finite theta pilot without replacing its evidence.

[note01]: 01_BOUNDED_THETA_CHARGE_AND_DIRECT_COMPARISON_20261021.md
[review]: ../reviews/02_REFERENCE_TRANSFER_AND_BOUNDARY_DEGREE_REVIEW_20261021.md
[script]: ../numerics/check_boundary_degree_controls.py
[receipt]: ../numerics/BOUNDARY_DEGREE_CONTROLS_20261021.json
[progress]: ../research-progress/01_RELATIVE_CHERN_HOPF_CHARGES_PROGRESS_20261021.md
[close]: ../../10_rh_implies_simple_zeros/notes/05_CLOSE_POSITIVE_SOURCES_AND_NORMALIZED_DOUBLE_ZEROS_20261020.md
[results]: ../../../../../../../result-summaries/README.md
[local]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[demailly]: https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf
[bezout]: https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/persistent-transcendental-bezout-theorems/C973B8F28E9FAD19237DEE5DD2AE0426

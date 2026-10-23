# Finite continuation of projective root tubes and complete event geometry

22 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **ultra**. Contributing-agent derivation; same-model
internal review is recorded separately. No independent specialist review.

**Status: proved in-note, conditional on RH and a hypothetical ordinary
endpoint double.** For every prescribed finite terminal time, two genuine
projective root tubes continue over a positive complex-time strip, with
explicit sufficient parameters from the complete source and proved
positive finite-interval root quantities. Gluing them to a complete local
event window gives all faces, orientations and exact fluxes. The window
retains charge one. This is finite-interval continuation, extended in Section 7 to growing
intervals with one fixed positive imaginary-time width by the companion
canonical cap theorem. It is not a single tube of fixed positive
projective radius extending to infinite time, a certified numerical
geometry, or an exclusion theorem.

The classification is an analytical geometry milestone, not an
RH-equivalent target relabeled as progress. Read the [result index][results]
and [avoid index][avoid], specifically [heat geometry][geometry],
[collision controls][controls], [target classification][a01],
[matching controls][a02], [scope][a07] and [coupled terms][a12].
The [local complete window][local] and [local projective side lemma][side]
are inherited. The finite-interval continuation and gluing below are the
new statements.

## 1. Fixed field, candidate, and one finite terminal time

Use the unchanged complete theta source and physical frame

\[
 H(\tau,z)=\int_0^\infty e^{\tau u^2}\Phi(u)\cos(zu)\,du,
 \quad H_\tau=-H_{zz},\quad G=(H,H_z),
\]
\[
 \mathcal A=\operatorname{Im}(G^*dG)/|G|^2,
 \qquad \mathcal C=\mathcal A\wedge d\mathcal A/(4\pi^2).
\]

Assume RH and an ordinary double at (0,a), where a is real and
H=H_z=0, h_2=H_zz(0,a) is nonzero. Since H(t,0)>0 for real t, a is nonzero;
evenness permits a>0. These are conditional event data, not an observed
theta double. Use the [explicit local window][local], shrinking its
ambient spatial disk so R<a/2, to choose b in (0,1/2), Y_0>0 and
Omega={|z-a|<=R} with the following inherited properties:

* W_0(Y)=[-b,b]+i[-Y,Y] times Omega is regular on its complete boundary,
  for every 0<Y<=Y_0, and has the sole common jet zero (0,a), of charge one.
* Both H roots on the real t=b slice lie strictly in |z-a|<R/2.
* The local two-chart construction in [the source proof][local] applies
  on a neighborhood of every such complete boundary.

The local source moments and the nonzero event jet pay these properties;
no positive jet floor is imposed at the event. Narrowing the inherited
heat rectangle preserves them. The two roots emerging as
r_-(t)=a-sqrt(2t)+O(t), r_+(t)=a+sqrt(2t)+O(t) are adjacent positive
ranks k,k+1 for sufficiently small b. Under RH their real positive-time
continuations are simple analytic fixed ranks. This is the precisely
stated input of [BW10 Note 19][motion], not a complex-time simplicity
assumption. To see the finite-interval continuation, at any positive t
choose a circle containing the first k+1 positive roots with zero-free
boundary. Local uniform convergence of H and simplicity preserve those
roots and their order nearby; H(t,0)>0 prevents crossing the origin.
This prevents a finite-rank branch from escaping at a finite positive time.

Take **T=1** for one explicit terminal time. The following construction
works, separately, for every T>=1; that parameterized family is the later
asymptotic interface. The spatial motion is fixed by the actual roots
r_-(t),r_+(t), rather than chosen circles with an assumed zero-flux property.

## 2. A quantitative continuation theorem on [b,T]

For a fixed finite T>=1 put

\[
 m=\min_{j\in\{-,+\},\ b\le t\le T}|H_z(t,r_j(t))|>0,
 \qquad d=\min_{b\le t\le T}(r_+(t)-r_-(t))>0.
\tag{1}
\]

Both strict inequalities are proved by continuity, compactness and the
positive-time simplicity input. They are exact finite-interval source
quantities, not presumed numerical lower bounds. Define the **complete**
moments, with no omitted modes or rays,

\[
 M_\ell(T)=\int_0^\infty u^\ell\Phi(u)
                    e^{(T+1)u^2+u}\,du,\quad \ell=1,2,3.
\tag{2}
\]

They are finite and positive. In the region used below they bound the
corresponding z derivatives, since |Im z|<=1. They also give the heat
derivative bounds |H_tau|<=M_2 and |H_tau,z|<=M_3. In particular m<=M_1.
Choose

\[
 \rho=\min\{1,R/4,d/4,m/(8M_2)\},\qquad
 \epsilon_*={m\rho\over8M_1},
\]
\[
 Y_* =\min\{Y_0/2,\ m\rho/(16M_2),\ m/(16M_3)\}.
\tag{3}
\]

For any 0<epsilon<=epsilon_* and 0<Y<=Y_* there are disjoint holomorphic
maps Z_j(tau,q), on a neighborhood of

\[
 D_T\times\{|q|\le\epsilon\},\qquad
 D_T=[b,T]+i[-Y,Y],
\]

such that

\[
 H(\tau,Z_j)=qH_z(\tau,Z_j),\qquad
 |Z_j(t+is,q)-r_j(t)|<\rho/2,
\tag{4}
\]
\[
 |H_z|\ge13m/16,\qquad
 |\partial_z(H-qH_z)|\ge51m/64,
\tag{5}
\]

on the chosen coordinate discs (the second lower bound is uniform for
|q|<=epsilon). In particular each Z_j is an embedded holomorphic inverse
of q=H/H_z on its q disc. The fixed-q-radius sides are genuine regular
three-faces.

**Proof.** Fix t in [b,T], set A_j=H_z(t,r_j(t)), w=z-r_j(t),
and F_q=H-qH_z. For |w|<=rho, |s|<=Y,

\[
 |H(t+is,r_j+w)-A_jw|\le M_2|w|^2/2+YM_2,
\]
\[
 |H_z(t+is,r_j+w)-A_j|\le M_2|w|+YM_3.
\tag{6}
\]

The first line follows from spatial Taylor expansion at the exact real
root and integration in imaginary heat time; the second uses the same
argument for H_z. On |w|=rho/2, the three errors in F_q-A_jw satisfy

\[
 {M_2\rho^2\over8}+YM_2+
 \epsilon(M_1+M_2\rho/2+YM_3)
 \le {14\over64}m\rho < {m\rho\over2}.
\tag{7}
\]

Rouche therefore gives one root, counted with multiplicity, in that disc.
On the larger rho disc,

\[
 |H_z-A_j|\le3m/16,
\]
\[
 |F_{q,z}-A_j|\le M_2\rho+YM_3+\epsilon M_2
                         \le13m/64.
\tag{8}
\]

These prove (5), simplicity and the local analytic implicit maps. They
patch holomorphically in tau: continuity of the real center r_j(Re tau)
and the strict rho/2 containment make nearby local branches agree by
uniqueness in the containing disc. Strict margins give a neighborhood
of the closed parameter rectangle and disc. Also

\[
 (Z_j)_q={H_z\over H_z-qH_{zz}}\ne0.
\tag{9}
\]

If two q values mapped to the same z, H_z!=0 would force them equal.
The distance between the two real centers is at least d>=4rho, proving
disjointness. At t=b, |r_j(b)-a|<R/2 and rho<=R/4 give strict attachment
inside Omega for every |s|<=Y. This proves the full finite-interval
continuation and attachment, rather than only the inherited local
projective-circle lemma. QED.

A numerical realization would need outward source-moment bounds and
validated lower enclosures for the finite-interval quantities in (1).
None was run or assumed. The theorem already proves their positivity
and existence for every finite T. It gives no lower bound uniform as
T tends to infinity or k tends to infinity.

## 3. Complete geometry and orientations

Let

\[
 U_j(\tau)=Z_j(\tau,\{|q|\le\epsilon\}),\qquad
 V_j=\{(\tau,Z_j(\tau,q)): \tau\in D_T,\ |q|\le\epsilon\}.
\]

Define W_T=W_0(Y) union V_- union V_+, joining along the two discs at
t=b. Its only event is (0,a): the old local window has only that event,
and each entire added tube lies in the H_z chart. The boundary is compact,
piecewise smooth and Lipschitz, with nonzero G everywhere. At an attachment
circle it has a reentrant corner. Stokes and degree use the oriented
piecewise smooth boundary; codimension-two corners add no three-form
integral. If a smooth boundary is desired, replace each reentrant corner
by a small rounded joining collar in the regular-jet neighborhood and
retain that collar. The replaced and replacement complete patches have
the same flux by Stokes in the intervening event-free region. There is
no unrecorded disappearance of a corner flux.

Use ambient orientation dt wedge ds wedge dx wedge dy. The complete
face inventory is:

| Face | Domain | Orientation |
| --- | --- | --- |
| Early cap | t=-b, -Y<=s<=Y, z in Omega | -ds wedge dx wedge dy |
| Two late caps | t=T, -Y<=s<=Y, z in U_j(T+is) | +ds wedge dx wedge dy |
| Joining face | t=b, -Y<=s<=Y, z in Omega minus the interiors of both U_j(b+is) | +ds wedge dx wedge dy |
| Local outer spatial wall | -b<=t<=b, -Y<=s<=Y, |z-a|=R | +dt wedge ds wedge dtheta |
| Two projective spatial sides | b<=t<=T, -Y<=s<=Y, q=epsilon exp(i theta) | +dt wedge ds wedge dtheta in the holomorphic inverse chart |
| Local top and bottom | s=+Y or -Y, -b<=t<=b, z in Omega | respectively -dt wedge dx wedge dy and +dt wedge dx wedge dy |
| Tube top and bottom | s=+Y or -Y, b<=t<=T, z in U_j(t+is) | respectively -dt wedge dRe q wedge dIm q and +dt wedge dRe q wedge dIm q |

The local heat/spatial circles, the tube heat/projective circles and the
attachment circles are the corners. Their intersections at s=+Y or -Y
are the corresponding lower-dimensional corner strata. At t=b the
local and tube imaginary-time pieces meet on the attachment discs; there
is no extra cap there. The only exposed t=b piece is the recorded joining
face. No inner linking sphere is needed because the event is strictly
inside W_0(Y).

On the old boundary use the inherited cover H!=0 and H_z!=0, with seam
|H_z|=P|H| for an admissible fixed P from [the local complete proof][local].
Its transition contributions are retained in the global physical form.
All added tubes, their joining discs and their sides use H_z!=0. H=0 at
the center of a tube is harmless in this chart; neither affine chart is
used at the interior event. The original raw equation
|H|^2-epsilon^2|H_z|^2=0 also contains that event elsewhere, but (4)-(9)
select regular components wholly in H_z!=0.

## 4. Exact cap and imaginary-face reductions

Write kappa_epsilon=epsilon^2/(1+epsilon^2),

\[
 h_j(\tau)=H_z(\tau,Z_j(\tau,0)),\qquad
 a_q={\operatorname{Im}(\bar q\,dq)\over1+|q|^2}.
\]

On a tube,

\[
 \mathcal A=\operatorname{Im}(dH_z/H_z)+a_q,\quad
 d\mathcal A=da_q,\quad
 \mathcal C={\operatorname{Im}(dH_z/H_z)\wedge da_q\over4\pi^2}.
\tag{10}
\]

The side |q|=epsilon has da_q=0 on its pullback, so its flux is exactly
zero. For an oriented heat edge e and its q disc, the full face integral is

\[
 \boxed{I_j(e)={\kappa_\epsilon\over2\pi}
                       \Delta_e\arg h_j.}
\tag{11}
\]

For the proof, H_z(tau,Z_j(tau,q))/h_j(tau) is holomorphic and nonzero on
the simply connected product and equals one at q=0. Its logarithm is
normalized there. The radial angular mean of the imaginary part of that
logarithm, and of its heat derivative, vanishes. Since
integral_{|q|<=epsilon} da_q=2pi kappa_epsilon, (10) proves (11).
The common phase has been retained; only its nonconstant q-disc mean
has simplified. Each phase increment uses a continuous lift along e.

Let I_T be the sum of the two late cap fluxes, and I_b the sum of the
same two discs at t=b, both in forward (+ds) orientation. Let E_T be
the sum of all four tube top/bottom faces in their outward orientations.
The heat rectangle is counterclockwise: late edge upward, top leftward,
early downward, bottom rightward. Nonvanishing holomorphy of h_j gives
zero total phase winding, hence

\[
 \boxed{I_T-I_b+E_T=0.}
\tag{12}
\]

This is exact, for every permitted finite T, epsilon and Y. It is stronger
than a separate estimate of those tube faces but does not remove the
local event closure.

## 5. The joining closure, signed charge, and scope of failure

Let B_0 be the sum of the early cap, local outer spatial wall, local top
and bottom faces, and the joining face. Since their union is the old
complete local boundary with only the two forward attachment discs
removed, inherited Q_{W_0}=1 gives

\[
 B_0=1-I_b,\qquad
 \boxed{Q_{W_T}=I_T+B_0+E_T=1.}
\tag{13}
\]

Equivalently, with a forward early-cap flux I_-,
Q_{W_T}=I_T-I_-+S_T, where S_T contains every other displayed face.
The projective sides vanish, while the remaining signed terms are those
in (11)-(13). A bound only for I_T cannot complete this signed budget.

There is a useful quantitative closure statement. Fix a small Y_c>0
within the b-slice branch neighborhood, and let

\[
 C_b=\max_{j,\ |s|\le Y_c}|\partial_\tau\log h_j(b+is)|<\infty.
\]

For Y<=min(Y_*,Y_c), (11) gives

\[
 |I_b|\le {2\kappa_\epsilon Y C_b\over\pi},\qquad
 |B_0-1|\le {2\kappa_\epsilon Y C_b\over\pi}.
\tag{14}
\]

The factor two counts the two tubes. Thus small late root-tube caps do
not cause the joining closure to vanish; in a shrinking family with
kappa_epsilon Y tending to zero, B_0 tends to one. This is a scoped
failure of the proposed inference that vanishing root-following sides
and small late root-disc caps alone discharge the full charge. It is not
an impossibility result for complete source-specific comparisons on
other geometries.

For matching to the fixed-rank large-time source cap estimate, let L_T
be its saddle scale, choose fixed r,S>0, and set

\[
 \epsilon_T=\min\{r/L_T,\epsilon_*(T)\},\qquad
 Y_T=\min\{S/L_T^2,Y_*(T),Y_c\}.
\tag{15}
\]

The effective rescaled radius r_T=L_T epsilon_T and width S_T=L_T^2Y_T
are bounded above by r,S. They need not have positive lower bounds.
The terminal source theorem must be uniform also when r_T,S_T shrink;
it cannot silently use a fixed positive width. The complete geometry
exists for each finite T and its normalized boundary retains charge one.
No fixed epsilon or Y is claimed to work for all T simultaneously.

## 6. Finite multiplicity geometry corollary

The continuation and complete attachment extend qualitatively to every
fixed finite multiplicity n>=2, while the explicit ordinary-double core
constants from [the local construction][local] do not transfer unchanged.
Suppose H(0,a) has order n. Choose R<a/2 so it is the only spatial zero
in |z-a|<=R at tau=0. Weierstrass preparation and Rouche give one proper
n-root cluster, wholly inside R/2, for all sufficiently small complex tau.
Its analytic discriminant is not identically zero, because under RH all
roots at positive real tau are simple. Shrinking the heat disc then leaves
zero as its only discriminant zero. Thus the complete jet has the sole
joint zero (0,a) in a small product core, with inherited local charge

\[
 q_n=\binom n2.
\tag{16}
\]

This uses the established [multiplicity charge law][multiplicity]; it is
not a new derivation of that weight. Choose b,Y_0 so the core rectangle
lies strictly inside that heat disc. The n simple roots at t=b are
consecutive positive ranks. Apply (1)-(9) to all n ranks, taking the
minimum derivative magnitude and minimum distinct pair gap. Their
positive-time simplicity and compactness prove both minima positive.
Every tube lies in H_z!=0; all joining discs lie inside the old core.

For the higher-multiplicity core the two open charts H!=0 and H_z!=0
cover its regular complete boundary. The unique critical-point graph
used in the ordinary-double source is not invoked. The global physical
form is integrated directly across that cover; if chart subdivision is
wanted, choose a regular positive value of |H_z/H| on its domain, regular
also on the finitely many boundary strata. No seam flux is discarded.

The inventory and orientations of Section 3 are unchanged except that
there are n tubes and n attachment holes. Equations (12)-(14) become

\[
 I_T-I_b+E_T=0,\qquad B_0=q_n-I_b,\qquad Q_{W_T}=q_n,
\]
\[
 |I_b|\le {n\kappa_\epsilon Y C_b\over\pi},\qquad
 |B_0-q_n|\le {n\kappa_\epsilon Y C_b\over\pi}.
\tag{17}
\]

Constants can depend on the arbitrary candidate height a and n. This is
coverage of the conditional finite-window geometry and its closure
identity for every fixed finite event. It is not a uniform height estimate
or an exclusion of any event, and does not complete LHCT-07's exclusion
deliverable.

## 7. Source-assisted continuation with a fixed imaginary-time width

The [companion cap theorem][cap] has a second terminal form: for a fixed
Y_max>0 its explicit bounds remain valid for |Im tau|<=Y_max by setting
the scaled phase range to S(t)=Y_max L_t^2. Its B_j errors are then
O_{K,Y_max}(L_t/sqrt(kappa_t)), tending to zero. Consequently, for all
sufficiently large real t, it proves actual regular inverse discs

\[
 H/H_z=q,\qquad |q|\le r/L_t,\qquad |\Im\tau|\le Y_{\max},
 \quad r=1/4,
\tag{18}
\]

at every one of a fixed finite set of positive ranks. The larger inverse
parameter radius r_1=1/3 and strict Rouché margin leave an open
neighborhood of these discs. The root derivative remains nonzero and the
maps depend holomorphically on tau and q locally. This uses the proved
complete complex-time source estimate; it does not follow from the
inherited real clock limit alone.

Choose t_1>=1 large enough that those explicit terminal inequalities hold
for every t>=t_1, with K at least the largest selected rank. Existence of
such a finite t_1 is proved by the source asymptotics; no certified
numerical value is asserted. Apply Sections 1-3 on [b,t_1] to obtain
positive epsilon_c and Y_c. Fix

\[
 0<r_0<r,\qquad 0<Y\le\min(Y_c,Y_{\max}),\qquad
 \epsilon_T={r_0\over L_T}.
\tag{19}
\]

For every sufficiently large terminal T>=t_1 with epsilon_T<=epsilon_c,
the entire interval [b,T] has the regular disjoint projective root tubes
of radius epsilon_T and this **same fixed positive Y**. On the late
part t_1<=t<=T,

\[
 |q|L_t\le r_0 L_t/L_T\le r_0<r,
\tag{20}
\]

because L_t'=2L_t/kappa_t>0. Thus each disc is inside (18). This is the
source-assisted gain over choosing an unknown shrinking Y_*(T).

For completeness, the late maps patch in real t by the same strict-disc
uniqueness argument used in Section 2: the scaled center
s_j+arctan(qL_t), its physical rescaling by L_t, and the radius rho/L_t
vary continuously. The implicit derivative is nonzero and the actual
root lies strictly inside that disc. Nearby local analytic branches
therefore agree. At t=t_1 the early finite-interval and late constructions
agree near s=q=0 because they continue the same simple real root. The
identity theorem continues that agreement along the connected common
vertical strip and q disc. Hence there is no omitted transition wall or
uncontrolled change of root label. The complete boundary inventory,
attachment and exact formulas (11)-(13) hold unchanged.

This produces a family of finite tubes with fixed imaginary width and
explicit terminal-dependent radius r_0/L_T. It does **not** give one tube
of fixed positive q radius for all T. A tapered infinite side with
|q|=r_0/L_t has a varying projective modulus; the zero-curvature side
lemma does not apply to that different side. Here the modulus is frozen
throughout each individual finite interval before its flux is evaluated.

The terminal cap is now generically nonzero in the limit. For N selected
roots, the companion theorem gives

\[
 I_T^{\rm ref}={N r_0^2Y\over\pi}
                {L_T^2\over L_T^2+r_0^2},\qquad
 I_T\longrightarrow {N r_0^2Y\over\pi}.
\tag{21}
\]

It supplies a complete error, including the common phase. Meanwhile the
fixed early branch bounds in (14) or (17) imply I_b=O(L_T^{-2}), so

\[
 B_0\longrightarrow q_N,\qquad
 E_T=I_b-I_T\longrightarrow-{N r_0^2Y\over\pi},\qquad
 I_T+B_0+E_T=q_N,
\tag{22}
\]

where q_N=binom(N,2) for a single order-N event (N=2 gives charge one).
Thus this stronger continuation theorem also identifies its full closure
burden: the imaginary-time tube faces cancel the nonzero terminal caps,
while the local joining closure retains the event charge. The statement
is a proved transport result, not a source-specific signed improvement
below that charge.

## 8. Controls and exact ownership

For H=(z-a)^2-2tau, the root inverses are
Z_±=a+q±sqrt(q^2+2tau), with consistent square-root branches near the
positive real interval. This verifies the finite tube mechanism, while
the attached local event still has charge one. No canonical theta
arithmetic is present in this polynomial.

For H=e^tau cos z, the inverse near z_j=(j-1/2)pi is
Z_j=z_j+arctan q, h_j(tau)=±e^tau, and (11) gives exactly
I_j(T)=kappa_epsilon Y/pi, independent of T. The sides vanish and each
complete tube has zero charge. This confirms the inherited nonzero
cosine cap, with its common phase retained. It is a positive atomic
source control, not theta or a claimed PCC model.

The inherited projective shell has a surviving inner cap as its radius
shrinks. Formula (13) is the complete finite-time analogue: its closure
is retained rather than discarded. The further collision controls keep
their separate preservation lists: Euler factors change the arithmetic;
weighted-square/finite-prime perturbations fail full normalized reflection
or unchanged coefficients; reflected/primitive controls lack canonical
square coefficients; close RH-conditional endpoint controls fail ordinary
Dirichlet-series arithmetic. The generic tube construction applies to any
control meeting its real-root and regularity premises; no new late
statistical property is assigned to them. This note contains no arithmetic
estimate that would separate theta from a matching endpoint control.

This establishes LHCT-01 for the stated ordinary-double full-window
family and LHCT-02 on every prescribed finite [b,T], with explicit
T-dependent allowable widths and radii. Section 7 additionally supplies a fixed imaginary width for growing
finite intervals, with projective radius r_0/L_T. It does not pay a
single fixed-radius tube to infinity, a full LHCT-05 signed improvement,
LHCT-06 exclusion, or LHCT-07 arbitrary-multiplicity exclusion. The [terminal source/jet theorem][cap] and [complete closure allocation][closure]
are proved companion results; the [internal review][review] checks the assembled scope.

[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[local]: ../../notes/03_COMPLETE_PHYSICAL_BOUNDARY_AND_CRITICAL_VALUE_WINDING_20261022.md
[side]: ../../notes/01_CHERN_HOPF_PROJECTIVE_SIDES_AND_LOCAL_SECTORS_20261022.md
[motion]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/19_COMPLETE_ROOT_MOTION_AND_FINITE_TIME_BOUNDS_20261021.md

[multiplicity]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/25_MULTIPLICITY_SELECTIVE_CHERN_AND_HOPF_OBSERVATIONS_20261021.md

[cap]: 02_COMPLEX_TIME_THETA_JETS_AND_LATE_CAPS_20261022.md

[closure]: 04_IMAGINARY_TIME_CLOSURE_CONCENTRATION_20261022.md
[review]: ../reviews/03_FINITE_TUBES_CAPS_AND_CLOSURES_INTERNAL_REVIEW_20261022.md

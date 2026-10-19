# Geometric symmetry coverage: Poincaré duality and hyperkähler rotation

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Actual model **gpt-6.1-sol (Codex)**, reasoning effort
**ultra**, verified from this turn's metadata. Internal review with three
same-model delegated readers; no independent specialist review. This is a
coverage assessment with elementary geometric calculations, not a new
theta sign theorem or numerical collision certificate.

## Finding and scope

The symmetry guide and S06 are careful within their stated scope, but they
are **not a comprehensive geometric symmetry inventory**. In particular,
bare Hodge star does not exhaust Poincaré duality, quaternionic multiplication
by J, twistor rotation, Lefschetz operators, or hyperholomorphic bundle
identities. Those deserve explicit entries. The existing negative results
do not justify excluding these larger classes.

There are useful qualifications in the other direction. Investigation 22
already implements relative Euler topology through spacetime winding;
elliptic translations already have a bounded physical-source experiment;
and the existing ASD connection is already hyperholomorphic in the
curvature sense. These are foundations to reuse, not new mechanisms obtained
merely by changing their names. No reviewed geometric symmetry currently
provides an independent signed estimate closing the real bridge or the
complex exterior.

This assessment follows the repository [result summaries][summaries] and
[patterns to avoid][avoid], especially [controls][controls], [geometry][geometry],
[local topology][topology], [generic lifts][a03], [scoped exclusions][a07],
and [cancellation losses][a12]. The source identities and exact checks are
recorded in the [small execution record][record]. Original manuscripts and
the two S06 notes remain canonical.

## Which geometric system is being discussed?

The following systems must not be identified with one another.

| System | Available structure | Limitation relevant to this review |
| --- | --- | --- |
| Fixed Euclidean C² carrying α_f=Re(f dz∧dw)/√2 | Flat hyperkähler background; closed self-dual theta forms | Variable α_f are generally not parallel; their ordinary degree-two classes vanish |
| g_f=\(\lvert f\rvert^2\lvert dz\rvert^2+\lvert dw\rvert^2\), f=H+iH_z | Locally flat hyperkähler metric where f≠0; real-slice coefficient E | Degenerates at a physical collision; smooth invertible J there cannot be assumed to exclude that event |
| Induced holomorphic jet surface (P,H,w), P_z=H | Kähler metric on its immersion locus, with coefficient \(\lvert H\rvert^2+\lvert H_z\rvert^2\); calibrated ambient inclusion | Its theta metric is not Ricci-flat and hence is not the hyperkähler metric above |
| Marked elliptic family M=H×T² | Nonflat semi-flat hyperkähler metric; actual theta line bundle and ASD connection | Noncompact and incomplete; the displayed metric does not descend to the full modular quotient |
| Compact Jensen hyperelliptic curves | Ordinary Poincaré duality, intersection pairing, real involution | These are a different, moment-built family; the all-degree real-topology criterion has RH strength |
| Physical (t,x) domain and its first jet (H,H_x) | Relative Euler class, degree, boundary winding | A plane rotation here is distinct from the ambient elliptic-family J |

The first four rows are proved or calculated in [Investigation 22's
manuscript][manifold], Sections 3–5 and 8. The last two are in its
[Jensen-surface note][jensen] and [spacetime note][winding]. The spectral
coordinate x, the source coordinate u, and the elliptic coordinates
(p,q,r,s) are different variables. A symmetry in one system needs an
explicit observation map before it becomes a symmetry of H(t,x).

## Poincaré duality: the support and boundary conditions matter

Poincaré duality is a global homology/cohomology duality, rather than a
pointwise operation on tensors. On a closed oriented n-manifold it gives
a nondegenerate complementary-degree pairing. On a noncompact manifold,
the standard duality pairs ordinary and compact-support cohomology; on a
compact manifold with boundary, relative and absolute groups pair.
These statements do not assert positivity. See [Hatcher, Section 3.3][pd].

**The Euclidean form model.** On C², H²(C²;R)=0 and H_c²(C²;R)=0.
The actual forms are explicitly exact:

\[
 \alpha_f=d\beta_f,\qquad
 \beta_f=\operatorname{Re}(P_f\,dw)/\sqrt2,\quad P_f'=f.
\]

Their nonzero pointwise pairing is not a nonzero ordinary cohomology
pairing. On a bounded four-domain Ω it is the existing boundary current,

\[
 \int_\Omega\alpha_f\wedge\alpha_g
 =\int_{\partial\Omega}\beta_f\wedge\alpha_g.
\]

Relative duality remains available, but one must supply an actual relative
cocycle or appropriate boundary condition; an arbitrary closed form is not
automatically a relative representative. Likewise, multiplying α by a
cutoff χ usually changes closedness: d(χα)=dχ∧α. Boundary or cutoff
corrections must be kept. Globally exact does not, by itself, mean exact
relative to a prescribed boundary. The existing compact exact-self-dual
obstruction applies only if the specified form extends globally exact and
self-dual to a compact boundaryless four-manifold.

**The marked elliptic family has genuine degree-two topology.** Since
H is diffeomorphic to R²,

\[
 H^2(M;\mathbb R)=\mathbb R[dr\wedge ds],\quad H^4(M;\mathbb R)=0,
 \quad H_c^2(M;\mathbb R)\simeq\mathbb R.
\]

Here and below the fibers have period one and orientation dr∧ds. For a
smooth compactly supported base form η with ∫_H η=1,

\[
 \int_M\eta\wedge dr\wedge ds=1.
\]

This realizes H_c²×H² duality. It is not an ordinary H² self-pairing.
The ASD curvature gives, using the manuscript's Chern convention,

\[
 F=2\pi i(q\,dp\wedge dq-dr\wedge ds),\qquad
 c_1(L)=\left[\frac{iF}{2\pi}\right]=[dr\wedge ds],
 \tag{1}
\]

because q dp∧dq=d(−q²dp/2). Thus ∫_fiber c₁(L)=1, consistently
with the theta bundle's positive degree. In contrast [F/(2πi)] is the
negative of c₁ in this convention. This fixed degree does not depend on
the external spectral variables t,x and cannot alone distinguish a first-jet
collision. A potentially useful new period argument must specify a
theta-dependent class, cycle, or relative boundary datum and compare its
pairing to the actual physical observation.

**A directly relevant relative-topological route already exists.** For
v=(H,H_x) on a bounded spacetime domain D with v≠0 on ∂D, the existing
note proves

\[
 \operatorname{wind}_{\partial D}(H+iH_x)
 =-\sum_{(T,a)\in D}\left\lfloor m(T,a)/2\right\rfloor.
 \tag{2}
\]

This is the relative Euler obstruction of the prescribed boundary
section in H²(D,∂D;Z), and is the natural section-zero application of
duality here. The heat equation supplies the common sign of the local
indices; duality alone would not prevent cancellation among local indices.
A bound ||v−ṽ||<||ṽ|| along every boundary segment certifies the
boundary homotopy. The [completed theta winding pilot][winding-review]
already compares this approach with a direct interior method. A useful
continuation needs a better boundary estimate or demonstrable cost or
coverage gain, rather than another restatement of (2).

**L² and weighted variants are separate analytic questions.** The
Euclidean α_f are independent of the unrestricted w variable and are
not L² unless zero; the marked metric is incomplete and its ASD curvature
has infinite total action. These facts block direct use of the usual
compact harmonic-representative argument. A bounded tube, weighted space,
or chosen self-adjoint boundary problem could be studied, but its domain,
boundary flux, cutoff/weight derivatives, and trace-to-physical comparison
must be derived. This is not an exclusion of all such variants.

## Multiplication by J: four different operations

Fix IJ=K and ω_A(v,w)=g(Av,w). A tangent endomorphism J with J²=−1,
its induced action on forms, a rotation of the complex structure in the
twistor sphere, and a diffeomorphism preserving the entire problem are
different operations. Hyperkähler geometry supplies the first three
constructions; it does not automatically supply the fourth.

**Tangent rotation gives a concrete missing-direction check.** The
semi-flat manuscript uses

\[
 e^1=\sqrt q\,dp,\quad e^2=\sqrt q\,dq,\quad
 e^3=q^{-1/2}(dr+p\,ds),\quad e^4=\sqrt q\,ds,
\]
\[
 \omega_I=e^{12}+e^{34},\quad
 \omega_J=e^{13}-e^{24},\quad
 \omega_K=e^{14}+e^{23}.
\]

For γ(u)=(p=0,q=e^{4u},r=s=0), put X=γ̇=4q∂_q. Then

\[
 IX=-4q\partial_p,\qquad
 JX=-4q\partial_s,\qquad KX=4q^2\partial_r.
 \tag{3}
\]

Thus the S06 base-p observation tests the I-rotated direction, up to its
known scalar factor. The J/K directions lie in the elliptic fiber. They
do not preserve the path or identify p with spectral x.

For a specified off-path extension X=4q∂q at fixed (p,r,s),
JX=−4q(∂s−p∂r) and KX=4q²∂r. Directly from (1),

\[
 F(X,JX)=F(X,KX)=0,\quad
 F(X,IX)=32\pi i q^3,\quad F(JX,KX)=-32\pi i q^3.
 \tag{4}
\]

The two latter vertical fields commute, so the covariant-derivative
commutator is F(JX,KX), not zero. Other ambient extensions of X need
their own brackets. In particular S06's extension holding z,bar z fixed
is not silently interchangeable with this one for higher derivatives.

Equation (3) is a reason to audit J/K observations, not evidence for a
favorable sign. The complete source is even in the fiber coordinate, so
its first vertical covariant derivative vanishes at the zero section in
the arithmetic frame. Higher insertions must include the connection,
derivatives of the rotating fields, and the dual observation. The raw
even insertions tested in [S06 Note 01][s06-1] restore a zero mode and
fail ordinary positive-time integrability. Correctly weighted J/K
combinations must be screened individually; they are not all covered by
the constant-coefficient definite-parity theorem.

For the declared S06 source, this review completes the first two fiber
insertions explicitly. Put D=∂u, P=T₀=e^uθ(0,iq)=e^u+2ψ and use unit
directions U=q^(−1/2)∂q, V=JU and W=KU. At p=0, extend the fiber
directions as V=−q^(−1/2)∂s and W=√q∂r with p,q held fixed. Write
∇V²S for ∇V(∇VS), **without** subtracting ∇_(∇^LC_V V)S; these are
directional iterations, not Levi-Civita-corrected Hessian components.
The adapted line connection gives

\[
 \nabla_V S|_0=\nabla_W S|_0=0,
\]
\[
 K_2:=\nabla_W^2S|_0
 =\frac\pi{16}(T_6-9T_4+9T_2+3T_0)
 =\frac\pi{16}(D-1)(D-3)(D-5)P
 =4\pi i q\,\partial_pS|_0,
 \tag{5}
\]
\[
 J_2:=\nabla_V^2S|_0
 =-\frac\pi{16}(T_6+9T_4+9T_2-3T_0)
 =-K_2-18\pi\Phi-3\pi P.
 \tag{6}
\]

Here the first p derivative is taken with the fixed-q source coefficients
of Note 01; it agrees with its first covariant derivative on the adapted
zero-section path. To derive the formulas, set A=𝒟_z, B=∂barz,
c=π/q and R(A)=q²A⁴−3π². The declared source is
S=q^(1/4)R(A)θ/(16π²). Since Bθ=0 and [B,A]=−c,

\[
 (A\mathbin\pm B)^2R(A)\theta
 =\{A^2R\mp c(R+2AR')+c^2R''\}\theta.
\]

The fiber covariant operators are ∇W=√q(A+B) and
∇V=−i√q(A−B). Expansion gives (5)–(6); the normalized ladder gives
T₂=DP, T₄=(D²+2)P and T₆=(D³+14D)P. Jacobi heat supplies the final
equality in (5). This is an exact reduction even though its D polynomial
has mixed reflection parity; the definite-parity theorem is not its proof.

The K₂ zero mode vanishes at the positive cusp. The J₂ zero mode is
−3πe^u, so its literal half-line heat transform fails ordinary convergence
for t>0. K₂ returns the already studied weighted p channel. Its complete
primitive compensation is precisely

\[
 K_2-3\pi(D-1)\psi=\pi(D-9)\Phi=-4\pi C,
 \tag{7}
\]

where C is Note 02's completed source. The full-line observation is thus
−4π times its already known Z; form the completed source before integrating
at the negative cusp. This does not create an independent sign estimate.
The natural tensor Hessian can also be checked here. At the zero section,
Γ^q_ss=−1/(2q) and Γ^q_rr=1/(2q³), so
∇^LC_VV=−∂q/(2q²), ∇^LC_WW=∂q/(2q²). Since the adapted line
connection has A_q=0 there and ∇qS=Φ′/(4q),

\[
 \operatorname{Hess}_\nabla S(V,V)=J_2+\frac{\Phi'}{8q^3},\qquad
 \operatorname{Hess}_\nabla S(W,W)=K_2-\frac{\Phi'}{8q^3}.
\]

The J Hessian retains its divergent zero mode. The K Hessian adds a
convergent damped physical-source derivative. Its exact half-line
observation, with f=e^(tu²−12u)cos(xu), is

\[
 \frac18\int_0^\infty e^{tu^2-12u}\Phi'\cos(xu)\,du
 =-\frac{\Phi(0)}8-\frac18\int_0^\infty\Phi f'\,du.
\]

The upper endpoint vanishes by complete-source decay; the lower endpoint
remains. This is a one-sided damped observation, not a same-point
derivative of H. No independent favorable sign has been estimated.
These calculations cover this source extension and these diagonal
directions. Mixed Hessians, different coefficient combinations, rotated
boundary conditions, and nonlocal constraints remain distinct questions.

**The form action preserves pairings, but need not preserve closedness.**
Define J^#α(v₁,…,v_k)=α(Jv₁,…,Jv_k). It is orthogonal and orientation
preserving. Applying it to all three inputs leaves the wedge/Laguerre
polarization unchanged, including its negative coefficient-space
eigenvalue. Rotating only selected inputs changes the observation.

It is also unsafe to assume dJ^#=J^#d on arbitrary forms. In flat
coordinates (x,y,a,b), let

\[
 A=dx\wedge da-dy\wedge db,\quad B=dx\wedge db+dy\wedge da,
 \quad \alpha=xA-yB=\sqrt2\alpha_z.
\]

With J from ω_J=A, J^#A=A and J^#B=−B, so

\[
 d\alpha=0,\qquad d(J^\#\alpha)=-2\,dx\wedge dy\wedge db\ne0.
 \tag{8}
\]

This local example is compatible with the classical hyperkähler action
on Laplacian-harmonic forms: locally, Δα=0 does not imply both dα=0
and d*α=0 for every other Laplacian-harmonic form. The compact cohomology
action uses global Hodge theory. [Verbitsky, Section 1][hyperholomorphic]
states the distinction between the action on forms and its compact
cohomological consequence. A corrected quaternionic differential complex
could be useful, but its operator identity and observation map are extra
work; pointwise multiplication is not already that chain map.

**Twistor rotation preserves g while changing the complex structure.**
The sphere I_a=aI+bJ+cK, a²+b²+c²=1, is available on the existing
hyperkähler ambient metric. It does not imply a base diffeomorphism
carrying the marked theta section, fiber lattice, physical path, complete
fourth-source operator, and heat/spectral test to themselves. A proposal
using a rotated slice must derive all those transported data. Applying
hyperkähler rotation intrinsically to the different, non-Ricci-flat jet
surface is not justified by the ambient construction.

**The ASD connection is already hyperholomorphic, but its section is
not simultaneously holomorphic.** In oriented real dimension four,
Λ²_− consists of primitive real (1,1) forms for every induced complex
structure. Therefore the displayed ASD unitary connection has F^{0,2}=0
for every I_a and defines an integrable holomorphic bundle structure for
each. This is the curvature criterion in [Verbitsky, Section 2][hyperholomorphic];
it requires no compact existence theorem in this explicit case.

The distinguished arithmetic theta section is holomorphic for the
original I. The covariant source jets are generally smooth sections.
Neither becomes automatically holomorphic for the other I_a. In fact a
section satisfying both ∇_{Iv}s=i∇_vs and ∇_{Jv}s=i∇_vs for all real v
would be parallel by the quaternion relations. Then Fs=0; the displayed
nonzero line-bundle curvature forces s=0. Thus the same nonzero theta
section cannot simply be declared holomorphic for both structures.
Rotating the holomorphic bundle is a viable identity framework, while a
useful rotated-section estimate remains to be constructed.

There is a further distinction if “multiplication by J” is meant on the
coefficient fiber itself. A complex line has no anti-linear endomorphism
with square −1: a map v↦a bar v squares to |a|². The hyperholomorphic
theta line is therefore not automatically a quaternionic line. Base
tangent/form actions and quaternionic differential operators on
bundle-valued forms remain possible, with their coefficient hypotheses
specified separately.

## Other relevant families: what is covered and what is missing?

The table is an inventory for the actual systems above, not a theorem
classifying every conceivable geometry.

| Family | Present footing | Additional requirement before it can help |
| --- | --- | --- |
| Modular inversion, reflection, theta characteristics, Jacobi/Heisenberg translations | S01/S05 and Investigation 22's [elliptic-shift experiment][shift] already exploit exact theta laws | Transform the complete source and test, preserve lower endpoints and transitions; distinguish automorphy from scalar invariance |
| Fourier/Poisson and oscillator/metaplectic symmetries | Existing reflection, normalized jet ladder and [arithmetic-transform work][arithmetic] provide specific realizations | A new transform must improve the complete signed estimate; a formal operator conjugation alone is bookkeeping |
| Quaternionic SU(2) and twistor sphere | Missing explicit inventory; tangent directions and hyperholomorphic curvature identified above | Full observation-equivariance or a paid defect, including source and dual covector |
| Kähler/Lefschetz operators, Hodge–Riemann relations and hyperkähler so(5) action | Classical extra structures beyond bare star; not developed as physical estimating tools here | Specify primitive/type constraints, representative, and a boundary or L² domain supporting the required theorem; show that the signed physical combination belongs to its controlled class |
| Serre duality or bundle-valued cohomological pairings | Possible after specifying complex structure and sheaf/cohomology data | Holomorphic representative, dual bundle, support conditions and an explicit physical pairing; a scalar mixed jet expression is not automatically such a pairing |
| Bochner/Weitzenböck and quaternionic Dolbeault identities | Ambient curvature and commutators exist; S06 has only selected transfers | Name the operator, its coercive term if any, all boundary/weight terms, and the trace bound returning to H or E |
| Actual isometries, torus actions, moment maps and reductions | Fiber translations preserve the displayed metric, and further local actions can be checked explicitly | Verify preservation/lift of the theta bundle, marked section, source operator and physical path; metric symmetry alone is insufficient |
| Calibration and special-Lagrangian rotation | Existing calibrated inclusions and signed Gauss-map analysis supply the background | A signed observation comparison; ambient volume minimization alone does not bound L₀ |
| Real involutions, relative Euler/winding, intersection and period pairings | [Winding][winding] and [Jensen curves][jensen] already retain marked data | A sharper complete boundary/moment estimate; ordinary unmarked topology discards the discriminating data |
| Gauss–Manin, monodromy, vanishing cycles/Picard–Lefschetz | Marked elliptic base is contractible with smooth fibers; primitive-curve singularities already have local links | A specified degenerating family, cycle and transport law tied to the physical flow; an elliptic singular fiber has not been identified with a theta collision |
| Fourier–Mukai/Nahm or mirror/T-dual descriptions | Potential bundle/fibration alternatives; no physical transform established | Specify the transform's category and hypotheses, then transform the source/test and pay the comparison. The flat-fiber real-torus construction of [Glazebrook–Jardim–Kamber][fm] does not directly apply to this nonzero vertical curvature; this does not rule out derived transforms of degree-one line bundles |

Hard Lefschetz, Hodge–Riemann positivity and the compact hyperkähler
cohomological so(5) action are not interchangeable with pointwise norm
positivity. Their compact hypotheses and primitive/type restrictions must
be checked. For the standard compact statements see [Dinh–Nguyên][hr]
and [Verbitsky's original so(5) paper][so5]. The local Lefschetz operator
algebra can still be studied on the current noncompact model; its useful
global estimate would need its own analytic realization. In particular
PD being nondegenerate does not make its middle-degree form positive.

## Bounded next tasks and controls

**First: extend the quaternionic-direction observation audit only if it
identifies a new estimating term.** The literal first/second J and K
fiber insertions have now been screened in (5)–(7). On the
existing marked metric and adapted arithmetic frame, choose explicit
extensions and compute any proposed mixed, Hessian-corrected, or coupled
insertions beyond these diagonal cases, of the complete source and dual
test before restriction. Retain field
brackets, curvature and zero-mode cancellations. Decide ordinary heat
integrability first. Where convergent, derive the full transform and lower
endpoint, then determine whether it is an existing physical derivative,
a completed nonlocal channel, or a different independently estimable term.
The milestone is an exact paid map or a scoped obstruction, rather than
another ambient metric. No large scan is needed to answer that first question.

**Second, conditional on an estimating identity: test a bounded
hyperholomorphic/Bochner or relative-boundary estimate.** State one
specific tube or spacetime rectangle, operator, boundary data, and complete
physical consumer. Derive its Green/flux identity before numerical work.
A winding continuation should reuse the existing pilot and compare at
equal coverage and precision with a practical direct method. A new source
channel must avoid the already demonstrated endpoint mismatch
|G₁|²>10^310 E on the height-1000 pilot, unless it retains a complete
compensation whose independent sign is actually estimated.

**Keep global period, compactification, monodromy and derived-transform
constructions conditional on a concrete physical comparison.** Their
mathematics is not excluded, but an auxiliary invariant alone is not a
quantitative gain. A reformulation of global first-jet nonvanishing or
all-degree Jensen hyperbolicity is classified once as an RH-strength
criterion; the bounded estimating objective is stated separately.

The applicable [collision controls][controls] distinguish these claims:

| Control family | Shared geometry or identity | Premise missing from a theta-specific application |
| --- | --- | --- |
| Polynomial heat events and counter-kernels | Local holomorphic forms, flat hyperkähler lifts, rotation and relative-index algebra | Exact complete theta arithmetic data and its evaluated estimate; a known event forbids a strict physical bound there |
| Three-/four-square sources | Integer-square support, local vertical differentiation/heat identities and matched finite endpoints | Canonical complete coefficients and full reflection; full Jacobi automorphy and canonical bundle descent are not shared; raw auxiliary positivity can coexist with their collisions |
| Reflected super-Gaussian | Reflection and generic geometric constructions | Normalized theta integer-square expansion |
| Finite-prime orbit sources | Finite arithmetic identities and measurements | Complete normalized reflection or another complete theta estimate; their abstract existence theorem gives no effective event box |
| Smooth-shape/positive-primitive sources | Shape, endpoint or primitive positivity; generic local geometry | Exact theta source; use the analytic event statement rather than an invented event box |
| Euler-factor sources | Even source, arithmetic/flow structure, generic geometry | Unchanged level-one theta data; their negative-Laguerre witness is not a double-event enclosure |
| Auxiliary smooth-density/two-channel realizations | Positive auxiliary state spaces | A complete signed physical-observation comparison |

A universal geometric identity may validly hold for a control. The
distinguishing assertion is the favorable complete estimate, which must
fail on a domain containing its controlled event. Do not demand rejection
on every collision-free control domain. A degree-one ambient line bundle
chosen independently of the source is likewise shared background; keeping
the *canonical distinguished section* is an additional arithmetic premise.

## Reconciliation and verification

S06 Note 01's finite-jet result concerns finite constant-coefficient
normalized jets with definite reflection parity and ordinary convergent
transforms. Its mixed-generator result concerns positivity preservation
on the named trigonometric class. Note 02's endpoint obstruction concerns
fixed finite subtraction and polynomial physical-energy magnitude payment
on an unbounded fixed-time half-line. None excludes all J-generated,
variable-coefficient, nonlocal, relative or bundle-valued estimates.
The completed current in Note 02 imports the physical L₀>E/100 sign;
its independent sign estimate remains open. The guide's S06 status should
say this explicitly now that an inherited transfer has been established.

Fresh exact rational checks verify the quaternion matrices, pairing
invariance, (3)–(8), and the Chern-normalization sign; the small record
also pins the reviewed sources. The unchanged S06 opening checker has
been rerun through its 163 exact algebra assertions in memory. Its three
inherited control assertions and the full 192/256-bit signed certificate
were **not** freshly rerun for this review; the saved records and checker
sources were inspected. No finite assertion count is evidence for a
universal analytic theorem. No new coverage, error improvement, performance
gain or global sign estimate is reported.

[summaries]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[geometry]: ../../../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[topology]: ../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[a03]: ../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[record]: ../numerics/GEOMETRIC_SYMMETRY_COVERAGE_CHECKS_20261018.json
[manifold]: ../../../../../investigations-2/active/22_theta_manifold_geometry/manuscript/theta_manifold_geometry.tex
[winding]: ../../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/04_SPACETIME_INDEX_AND_MARKED_TOPOLOGY_20261015.md
[winding-review]: ../../../../../investigations-2/active/22_theta_manifold_geometry/reviews/18_SPACETIME_BOUNDARY_AND_GEOMETRIC_CONTINUATION_REVIEW_20261015.md
[jensen]: ../../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/05_JENSEN_HYPERELLIPTIC_TOPOLOGY_20261015.md
[shift]: ../../../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/05_ELLIPTIC_SHIFT_CORE_AND_PROJECTION_OBSTRUCTION_20261015.md
[arithmetic]: ../../../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/12_NONLOCAL_ARITHMETIC_MULTIPLIERS_AND_BOUNDARY_OBSTRUCTIONS_20261015.md
[s06-1]: ../notes/01_TRANSVERSE_OBSERVATION_AND_FINITE_JET_OBSTRUCTIONS_20261018.md
[pd]: https://pi.math.cornell.edu/~hatcher/AT/AT.pdf
[hyperholomorphic]: https://arxiv.org/html/alg-geom/9307008v1
[so5]: https://www.mathnet.ru/eng/faa960
[hr]: https://arxiv.org/abs/math/0501449
[fm]: https://arxiv.org/pdf/math/0307199

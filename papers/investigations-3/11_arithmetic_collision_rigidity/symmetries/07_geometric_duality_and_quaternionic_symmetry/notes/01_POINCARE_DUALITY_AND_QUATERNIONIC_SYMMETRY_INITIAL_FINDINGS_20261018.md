# Initial findings: Poincaré duality and quaternionic symmetry

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Actual model **gpt-6.1-sol (Codex)**, reasoning effort
**ultra**, verified from this turn's metadata. Initial S07 research note,
consolidating the preceding [S06 geometric coverage review][coverage].
The identities below were obtained and internally checked in that review;
opening S07 does not count them again as new research. This note received
same-model internal setup review, not independent specialist review.

## Objective and opening decision

Investigate geometric structures beyond the bare Hodge star: Poincaré and
relative duality, quaternionic J/K, twistor rotation, hyperholomorphic
connections and related operator or boundary identities. The practical
objective is an independent estimate of the complete signed physical
observation, or a useful bounded certification improvement.

The opening audit supplies exact identities and scoped obstructions.
It does not supply a new signed theta inequality. In particular, the
literal second J insertion diverges; the second K insertion returns
S06's weighted transverse channel; diagonal Hessian corrections add a
damped observation with an explicit endpoint. The next question concerns
a genuinely additional mixed or bundle identity and its estimating use.

The [program guide][guide], [result summaries][summaries] and
[patterns to avoid][avoid] govern this continuation. Consult
[controls][controls], [geometry][geometry], [target reformulation][a01],
[generic lifts][a03], [scoped exclusions][a07] and [cancellation losses][a12].
Global first-jet nonvanishing and the all-degree Jensen-topology criterion
have the RH strength recorded in their sources. They are not new bounded
milestones merely because a geometric pairing represents them.

## Physical and geometric conventions

The physical quantity remains

\[
 H(t,x)=\int_0^\infty e^{tu^2}\Phi(u)\cos(xu)\,du,
 \quad H_t=-H_{xx},\quad E=H^2+H_x^2,
 \quad\mathcal L_0=H_x^2-HH_{xx}.
\]

Use the period-one theta convention
θ(z,τ)=Σ_n exp(πin²τ+2πinz), τ=p+iq, z=r+τs. The marked
ambient space is M=ℍ×T², with period-one r,s and metric

\[
 g=q(dp^2+dq^2)+q^{-1}(dr+p\,ds)^2+q\,ds^2.
\]

Its parallel triple has IJ=K and ω_A(v,w)=g(Av,w). In the coframe

\[
 e^1=\sqrt q\,dp,\quad e^2=\sqrt q\,dq,\quad
 e^3=q^{-1/2}(dr+p\,ds),\quad e^4=\sqrt q\,ds,
\]

\[
 \omega_I=e^{12}+e^{34},\quad
 \omega_J=e^{13}-e^{24},\quad\omega_K=e^{14}+e^{23}.
\]

Keep the existing [adapted theta metric][metric]
\(\widetilde h=e^{2\pi p^2q}\exp[-2\pi(\operatorname{Im}z)^2/q]\).
Its Chern connection is zero along
γ(u)=(p=r=s=0,q=e^(4u)), and its curvature is

\[
 F=2\pi i(q\,dp\wedge dq-dr\wedge ds),\qquad *F=-F.
 \tag{1}
\]

This marked metric is hyperkähler, noncompact and incomplete; the displayed
formula has no full modular descent. The different induced jet-surface
metric from (P,H,w), P_z=H, is Kähler on its immersion locus but is not
hyperkähler for theta. The auxiliary metric g_f with coefficient E is
hyperkähler only away from its degeneration set. These systems must not
be interchanged when invoking J or compact theorems. The [manuscript][manifold]
proves their separate geometric scope.

## Poincaré duality and the existing relative invariant

Hodge star acts pointwise on forms. Poincaré duality pairs global
homological/cohomological data, with support or boundary conditions in
the noncompact or relative setting; it does not assert positivity.
The relevant classical reference is [Hatcher, Section 3.3][pd].

On the original Euclidean C² form model, H²=H_c²=0. The forms
α_f=Re(f dz∧dw)/√2 are exact, α_f=dβ_f, with
β_f=Re(P_f dw)/√2 and P_f′=f. Their nonzero pointwise signed pairings
do not give nonzero ordinary degree-two classes. On a bounded Ω they give
the existing complete boundary current

\[
 \int_\Omega\alpha_f\wedge\alpha_g
 =\int_{\partial\Omega}\beta_f\wedge\alpha_g.
\]

An actual relative representative or boundary condition is required for
relative duality. A cutoff changes closedness by d(χα)=dχ∧α, so its
correction cannot be omitted. Global exactness alone does not imply
relative exactness for an arbitrary prescribed boundary.

On M=ℍ×T²≃R²×T²,

\[
 H^2(M;\mathbb R)=\mathbb R[dr\wedge ds],\quad
 H_c^2(M;\mathbb R)\simeq\mathbb R,\quad H^4(M;\mathbb R)=0.
\]

The appropriate middle-degree integration pairing uses one compact-support
factor. For a compactly supported base two-form η with ∫_ℍη=1,
∫_Mη∧dr∧ds=1. Equation (1) and q dp∧dq=d(−q²dp/2) give

\[
 c_1(L)=\left[\frac{iF}{2\pi}\right]=[dr\wedge ds],
 \qquad\int_{T^2}c_1(L)=1.
 \tag{2}
\]

The sign uses the repository's Chern convention; F/(2πi) represents
−c₁ here. This fixed fiber degree is independent of t,x. A new period
estimate must introduce and control a relevant theta-dependent class,
cycle or boundary datum; degree alone does not exclude a physical event.

An especially relevant relative class is already developed in
[Investigation 22's spacetime note][winding]. For v=(H,H_x) nonzero on
the boundary of a bounded spacetime domain D,

\[
 \operatorname{wind}_{\partial D}(H+iH_x)
 =-\sum_{(T,a)\in D}\lfloor m(T,a)/2\rfloor.
 \tag{3}
\]

This is the relative Euler obstruction in H²(D,∂D;Z). The heat equation's
same-sign local index law, not duality alone, makes zero winding exclude
all interior collisions. The sufficient boundary-homotopy margin
||v−ṽ||<||ṽ|| must hold along every boundary segment. The
[completed theta pilot][pilot] already implements this route; no general
cost advantage was established. New work must improve the boundary
estimate or its matched certification cost.

## J/K tangent directions, source insertions and Hessians

Fix the existing S06 ambient source, with its q coefficients held fixed
under p differentiation:

\[
 S(p,q,z)=\frac{q^{1/4}}{16\pi^2}
       (q^2\mathcal D_z^4-3\pi^2)\vartheta(z,p+iq),
 \quad\mathcal D_z=\partial_z+2\pi is.
 \tag{4}
\]

At p=z=0 it is Φ(u), q=e^(4u). This is the declared extension in
[S06 Note 01][transverse], not a claim about every possible extension.
Let D=∂u, J_k=𝒟_z^kθ|₀ and T_k=π^(−k/2)q^(k/2+1/4)J_k.
Set P=T₀=e^u+2ψ, with ψ=e^uΣ_(n≥1)e^(−πn²q). The available ladder gives

\[
 T_2=DP,\quad T_4=(D^2+2)P,\quad T_6=(D^3+14D)P,
 \qquad16\Phi=T_4-3T_0.
\]

For X=γ̇=4q∂q, the triple gives

\[
 IX=-4q\partial_p,\quad JX=-4q\partial_s,\quad
 KX=4q^2\partial_r.
 \tag{5}
\]

The p observation already studied in S06 is therefore the I direction,
up to a scalar factor. Spectral x is not p. At the path,
F(X,JX)=F(X,KX)=0, while F(X,IX)=32πiq³ and
F(JX,KX)=−32πiq³. Tangential flatness does not erase all ambient
commutators.

Use U=q^(−1/2)∂q and unit directions V=JU=−q^(−1/2)∂s,
W=KU=√q∂r at p=0. Extend V,W at fixed p,q along their fiber
directions. In the next formulas ∇V² means ∇V(∇VS), with no
Levi-Civita acceleration subtraction. Parity makes the first insertions
vanish. The second ones are

\[
 K_2:=\nabla_W^2S|_0
 =\frac\pi{16}(T_6-9T_4+9T_2+3T_0)
 =\frac\pi{16}(D-1)(D-3)(D-5)P
 =4\pi i q\,\partial_pS|_0,
 \tag{6}
\]
\[
 J_2:=\nabla_V^2S|_0
 =-\frac\pi{16}(T_6+9T_4+9T_2-3T_0)
 =-K_2-18\pi\Phi-3\pi P.
 \tag{7}
\]

For a direct derivation put A=𝒟_z, B=∂barz, c=π/q,
R(A)=q²A⁴−3π². Then Bθ=0, [B,A]=−c, and

\[
 (A\pm B)^2R(A)\theta
 =\{A^2R\mp c(R+2AR')+c^2R''\}\theta.
\]

The fiber operators are ∇W=√q(A+B), ∇V=−i√q(A−B), which gives
(6)–(7). Jacobi heat gives the final p identity. Its mixed-parity
D polynomial is not covered by the finite definite-parity reduction;
the displayed exact identity is its actual proof.

At the positive cusp K₂ has zero lattice mode zero; J₂ has mode
−3πe^u. Thus the literal J₂ half-line heat transform diverges for t>0.
K₂ is the existing weighted p channel. Its full primitive compensation is

\[
 K_2-3\pi(D-1)\psi=\pi(D-9)\Phi=-4\pi C,
 \tag{8}
\]

where C is [S06 Note 02's][completion] completed source. Its full-line
observation equals −4π times the known Z. Combine the source first:
separate terms diverge at the negative cusp. The known signed current
imports the physical L₀>E/100 certificate; (8) gives no independent sign.

For the tensor Hessian, Γ^q_ss=−1/(2q), Γ^q_rr=1/(2q³) give
∇^LC_VV=−∂q/(2q²), ∇^LC_WW=∂q/(2q²). In the adapted frame
∇qS=Φ′/(4q), hence

\[
 \operatorname{Hess}_\nabla S(V,V)=J_2+\frac{\Phi'}{8q^3},\qquad
 \operatorname{Hess}_\nabla S(W,W)=K_2-\frac{\Phi'}{8q^3}.
 \tag{9}
\]

The J divergence persists. The K correction is an ordinary convergent
damped half-line observation. For f=e^(tu²−12u)cos(xu), its exact map is

\[
 \frac18\int_0^\infty e^{tu^2-12u}\Phi'\cos(xu)\,du
 =-\frac{\Phi(0)}8-\frac18\int_0^\infty\Phi f'\,du.
 \tag{10}
\]

Complete-source decay kills the upper endpoint; the lower endpoint
remains. This is not a same-point derivative of H. No favorable
independent estimate of this corrected channel has been established.

## Tensor action, twistor rotation and the theta bundle

Pointwise J on forms is different from diffeomorphism pullback. Its
orthogonal induced action J^# preserves the complete wedge polarization
and its negative coefficient-space eigenvalue. It need not preserve
closedness. For flat coordinates (x,y,a,b), set
A=dx∧da−dy∧db, B=dx∧db+dy∧da and α=xA−yB. Then

\[
 d\alpha=0,\qquad d(J^\#\alpha)=-2\,dx\wedge dy\wedge db\ne0.
 \tag{11}
\]

Local Laplacian-harmonicity does not supply the missing global
Hodge-theoretic argument. A quaternionic differential complex must be
specified, not inferred by commuting d with pointwise J.

The twistor sphere aI+bJ+cK preserves g, but does not automatically
transport the marked section, lattice, source operator, path and test to
themselves. Every proposed symmetry of the physical observation must
include these data and their dual pairing.

The existing ASD curvature is primitive (1,1) for every induced complex
structure in real dimension four. Therefore the connection is already
hyperholomorphic in the curvature sense; this uses the explicit curvature,
not a compact existence theorem. [Verbitsky, Sections 1–2][hyperholomorphic]
gives the classical framework. The nonzero theta section is not
simultaneously I- and J-holomorphic: both conditions would force it
parallel by the quaternion relations, then Fs=0, contrary to (1).
Moreover an anti-linear endomorphism a·conjugation on a complex line
squares to |a|², so its fiber does not acquire a quaternionic J²=−1.
Bundle-valued differential identities remain possible with their actual
coefficient hypotheses checked.

## Geometric inventory and continuation contract

| Family | Starting status | Missing estimating input |
| --- | --- | --- |
| Poincaré/relative/compact-support duality | Correct groups and fixed fiber pairing identified; relative Euler route already developed | New arithmetic-dependent pairing or better complete boundary margin |
| J/K and twistor/SU(2) | Diagonal insertions and Hessians audited above | A mixed/coupled or rotated-boundary identity with a complete physical map |
| Hyperholomorphic, Bochner and quaternionic Dolbeault | Explicit ASD connection available | Operator and coefficient hypotheses, full Green flux and physical trace estimate |
| Lefschetz, Hodge–Riemann, so(5), Serre duality | Broader classical frameworks beyond bare star | Applicable type/primitive/cohomology data and justified compact, boundary or analytic domain |
| Isometries, torus actions, moment maps and calibration | Existing ambient symmetries and inclusions | Preservation of the distinguished source/test and an actual signed comparison |
| Modular/Jacobi, Fourier/Poisson and oscillator structures | S01/S05 and Investigation 22 already have exact implementations | New complete signed-error or evaluation gain, preserving every source cancellation |
| Real involutions, periods, Gauss–Manin and monodromy | Existing Jensen surfaces and local singularity data | Specified cycle/family and an evaluated theta period or discriminant estimate |
| Fourier–Mukai/Nahm and mirror/T-dual proposals | No physical observation transform established | Correct transform category and complete source/test identity; nonzero fiber curvature defeats the particular flat-fiber torus correspondence |

The [coverage review][coverage] supplies primary references and detailed
applicability qualifications for these rows. Compact Hodge or Lefschetz
theorems cannot be imported directly onto the incomplete marked metric.
L² or weighted variants need integrability, operator domains and boundary
or weight terms. The ordinary fixed fiber pairing alone is not a physical
signed estimate. The inventory is not an impossibility theorem for any
whole geometric family.

The first continuation should derive one polarized J-Dolbeault/Weitzenböck
Green identity on the fixed tube
\(\Omega=\{-1/4\le p\le1/4,\ 1\le q\le4\}\times T^2\).
Specify the operator and form degree, source and smooth dual-test
extension, and every coefficient-bundle hypothesis. Do not assume the
arithmetic frame or a constant dual coefficient descends globally.
Derive every p/q boundary flux, field bracket and physical endpoint before
estimating. Here Λ_JF=0 by (1), so a positive scalar curvature payment
cannot be assumed; any remaining form-degree curvature action must be
evaluated explicitly. State the additional regularity and derivative
costs needed for restriction to the one-dimensional path. Retain the
q=4 face and the complete tail beyond u=log(4)/4 when comparing with H.
Decide convergence before a numerical scan. If the result
reduces to (8), (10), or the old unknown signed physical trace, record that exact
reduction and identify the additional estimate needed before continuing.

## Collision controls and verification status

| Control class | Shared premises | Required theta-specific distinction |
| --- | --- | --- |
| Polynomial heat events/counter-kernels | Generic heat, local forms, quaternionic lifts and index identities | Exact complete theta source and a paid estimate |
| Weighted three-/four-square sources | Square support, local heat/vertical derivatives, matched endpoints | Canonical complete coefficients/full reflection; full Jacobi automorphy is not shared |
| Reflected super-Gaussian | Reflection and generic geometric structures | Normalized theta integer-square source expansion |
| Finite-prime orbit controls | Selected prime relations and finite tests | Complete reflection or a different evaluated full-source estimate; no effective event height is supplied |
| Smooth-shape/positive-primitive controls | Source shape, positivity and endpoint information | Exact arithmetic source; analytic events remain analytic, without invented boxes |
| Euler-factor controls | Even positive source and substantial arithmetic/flow structure | Unchanged conductor-one theta data; negative-Laguerre witness is not a double-event enclosure |
| Auxiliary smooth-density/two-channel constructions | Positive auxiliary spaces | Complete signed physical observation comparison |

An identity may hold for a colliding control. A strict favorable physical
estimate must fail on a domain containing that event. This setup makes no
new control-excluding inequality and does not upgrade the inherited tests.
Future estimating mechanisms must execute the applicable controls under
the [program contract][guide].

The inherited checker verifies 61 exact rational algebra identities,
including (5)–(9), the form counterexample and Chern sign. Its fresh S07
replay and source identities are in [numerics][numerics]. These finite
checks support the algebra; the arguments above supply the analytic scope.
The full signed interval certificate and event controls are not freshly
rerun for this organizational opening. No independent physical sign,
new exclusion region, smaller complete error, speedup or global bound is
claimed. S07 remains open with the bounded contract above.

[coverage]: ../../06_hodge_and_transverse_geometry/reviews/03_GEOMETRIC_SYMMETRY_COVERAGE_POINCARE_AND_HYPERKAHLER_20261018.md
[guide]: ../../../research-overview/03_SYMMETRY_RESEARCH_PROGRAM_AND_INVESTIGATION_GUIDE_20261018.md
[summaries]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[geometry]: ../../../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a03]: ../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[manifold]: ../../../../../investigations-2/active/22_theta_manifold_geometry/manuscript/theta_manifold_geometry.tex
[metric]: ../../../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/02_ASD_METRIC_FREEDOM_AND_PHYSICAL_RESTRICTION_20261015.md
[winding]: ../../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/04_SPACETIME_INDEX_AND_MARKED_TOPOLOGY_20261015.md
[pilot]: ../../../../../investigations-2/active/22_theta_manifold_geometry/reviews/18_SPACETIME_BOUNDARY_AND_GEOMETRIC_CONTINUATION_REVIEW_20261015.md
[transverse]: ../../06_hodge_and_transverse_geometry/notes/01_TRANSVERSE_OBSERVATION_AND_FINITE_JET_OBSTRUCTIONS_20261018.md
[completion]: ../../06_hodge_and_transverse_geometry/notes/02_SIGNED_TRANSVERSE_ESTIMATE_AND_EXACT_SOURCE_COMPENSATION_20261018.md
[numerics]: ../numerics/README.md
[pd]: https://pi.math.cornell.edu/~hatcher/AT/AT.pdf
[hyperholomorphic]: https://arxiv.org/html/alg-geom/9307008v1

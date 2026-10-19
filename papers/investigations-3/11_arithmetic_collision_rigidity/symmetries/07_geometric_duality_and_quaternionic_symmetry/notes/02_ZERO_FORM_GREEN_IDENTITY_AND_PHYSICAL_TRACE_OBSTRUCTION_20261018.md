# Zero-form J-Green identity, complete theta flux and a trace obstruction

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Actual model **gpt-6.1-sol (Codex)**, reasoning effort
**ultra**, verified from this turn's metadata. Initial S07 investigation
with three same-model delegated readers. Analytic derivations, exact finite
algebra and fresh inherited collision-control replay; no specialist human
review and no new signed theta certificate.

## Contract and outcome

This executes the [S07 bounded first task][s07] on
Ω=[−1/4,1/4]_p×[1,4]_q×T², for smooth **line-bundle-valued zero-forms**.
It derives the polarized J-Dolbeault Green identity with every boundary
face, inserts the canonical complete theta source and a genuine dual test,
and checks the proposed first-order energy-to-physical-path comparison.

The resulting scoped findings are:

- The contracted line-bundle curvature vanishes. Nonzero ambient curvature
  remains, but the zero-form identity supplies no positive zero-order term.
- The actual theta source has exactly zero full-fiber-averaged current
  on every p/q face. Its bulk identity equates the two nonnegative
  energies rather than supplying a signed physical margin.
- Restricted first-order J components return the known p channel and a
  damped source derivative. The raw rough-Laplacian restriction restores
  a growing zero mode and has no ordinary positive-time half-line transform.
- No uniform comparison of the physical path observation with only these
  first-order bulk energies holds for all smooth sections, even with all
  boundary currents zero. An explicit concentrating family proves this.

The declared result is a **scoped obstruction and exact observation
dictionary**, not a new RH criterion or a universal exclusion of geometric
estimates. The canonical theta section obeys extra arithmetic/PDE data not
preserved by the concentrating family. Estimates using those data, higher
regularity, other form degrees or nonlocal pairings remain outside this
obstruction. No new finite region, complete error gain or speedup is claimed.

Follow the [program guide][guide], repository [result summaries][summaries]
and [patterns to avoid][avoid]. The relevant entries are [controls][controls],
[geometric realizations][geometry], [target reformulation][a01],
[generic lifts][a03], [scoped exclusions][a07] and [signed cancellations][a12].

## Geometry, frame and the zero-form operator

Use the conventions of [Note 01][initial] and the
[adapted metric source][metric]. The ambient metric and volume are

\[
 g=q(dp^2+dq^2)+q^{-1}(dr+p\,ds)^2+q\,ds^2,
 \qquad dV=q\,dp\wedge dq\wedge dr\wedge ds.
 \tag{1}
\]

The fiber coordinates have period one. Its J-Kähler form is

\[
 \omega_J=dp\wedge dr+p\,dp\wedge ds-q\,dq\wedge ds.
 \tag{2}
\]

Write h for the adapted Hermitian metric, linear in the first entry:
h(ae,be)=h a bar b in the marked holomorphic frame. Its scalar coefficient
is h=exp[2πq(p²−s²)]. In the unitary chart frame e_U=h^(−1/2)e,

\[
 \nabla=d+i\mathfrak a,\quad
 \mathfrak a=\pi(s^2-p^2)\,dp+2\pi pq\,dq
                      +2\pi s\,dr+2\pi ps\,ds,
\]
\[
 F=i\,d\mathfrak a=2\pi i(q\,dp\wedge dq-dr\wedge ds).
 \tag{3}
\]

These are local frame formulas; curvature and the scalar currents below
are global. Directly, F∧ω_J=0, so Λ_JF=0. This does not set F_pq or
F_rs to zero. In complex dimension two, λ∧ω_J=(Λ_Jλ)dV for any
two-form λ. The physical path is γ(q)=(0,q,0,0), q=e^(4u), with
du=dq/(4q), not its arclength dℓ=√q dq.

For sections define

\[
 \bar\partial_J^\nabla a
   =\tfrac12(\nabla a+iJ^\#\nabla a).
 \tag{4}
\]

This is a section-valued (0,1) form. It uses the induced tangent/form J;
no quaternionic action on the complex line fiber is assumed. In coordinates
put

\[
 \mathsf P=\nabla_p+iq\nabla_r,\qquad
 \mathsf Q=\nabla_q-i(\nabla_s-p\nabla_r).
\]

Then

\[
 2\lvert\bar\partial_J^\nabla a\rvert^2
 =q^{-1}(\lvert\mathsf Pa\rvert^2+\lvert\mathsf Qa\rvert^2).
 \tag{5}
\]

Their vector-field bracket vanishes: differentiating ip in Q and iq
in P gives cancelling i∂r terms. Their curvature commutator also vanishes,
because F_pq+qF_rs=2πiq−2πiq=0. Thus [P,Q]=0. This explicitly exhibits
J-integrability while retaining both nonzero curvature components.

## Polarized current identity with every face

For smooth sections a,b define the complex Hermitian-polarized one-form

\[
 j_{ab}=\frac i2\{h(a,\nabla b)-h(\nabla a,b)\}.
 \tag{6}
\]

It is globally defined. For a=b it is the real current
j_aa=Im h(∇a,a)=Im(bar a∇a) in a unitary frame. The mixed current
must remain polarized; replacing it by a positive norm loses information.

**Proposition 1.** For arbitrary smooth sections a,b,

\[
 \{h(\nabla a,\nabla b)
       -2h(\bar\partial_J a,\bar\partial_J b)\}\,dV
 =d(j_{ab}\wedge\omega_J)+iFh(a,b)\wedge\omega_J.
 \tag{7}
\]

Here and below one-form inner products contract the real metric. For (3)
the curvature term on the right vanishes identically.

**Proof.** Let θ=h(a,∇b), η=h(∇a,b). Unitarity gives
θ+η=d h(a,b), and the graded product rule gives
dθ=h(∇a∧∇b)−Fh(a,b), where the second section-valued factor is
conjugated according to the displayed Hermitian convention. Consequently
dj=i h(∇a∧∇b)−iFh(a,b). Expanding (4) in a real orthonormal J-paired
frame gives
h(∇a,∇b)−2h(bar∂_Ja,bar∂_Jb)=iΛ_Jh(∇a∧∇b).
Wedge with the closed ω_J to obtain (7). This proof is local exterior
algebra and uses no compact Hodge theorem. ∎

Write j=j_pdp+j_qdq+j_rdr+j_sds. Stokes on the piecewise smooth tube
gives exactly

\[
 \mathcal B(a,b)
 =\int_1^4\!\int_{T^2}[qj_r]_{p=-1/4}^{p=1/4}\,dr\,ds\,dq
  -\int_{-1/4}^{1/4}\!\int_{T^2}
       [j_s-pj_r]_{q=1}^{q=4}\,dr\,ds\,dp,
 \tag{8}
\]
\[
 \int_\Omega h(\nabla a,\nabla b)
       -2\int_\Omega h(\bar\partial_Ja,\bar\partial_Jb)
 =\mathcal B(a,b).
 \tag{9}
\]

All four p/q faces are retained. There are no torus faces for a global
current, and this single Stokes identity has no additional corner term.
Equivalently B=∫_∂Ω j(Jν)dΣ. The formal interior zero-form identity is
2Δ_bar∂J=∇*∇−iΛ_JF=∇*∇. Its integrated Green form is

\[
 2\int_\Omega h(\bar\partial_Ja,\bar\partial_Jb)
 =\int_\Omega h(\nabla^*\nabla a,b)
   +\int_{\partial\Omega}h((\nabla_\nu+i\nabla_{J\nu})a,b)\,d\Sigma.
 \tag{10}
\]

The surface-density-weighted conormal operators are ±P on the p faces
and ±Q on the q faces, with the outward signs. No boundary condition or
self-adjoint realization is silently imposed. The classical Kähler
identity and its curvature convention were checked against
[Verbitsky, Section 3, Proposition 3.1][verbitsky]; (7)–(9) were derived
directly to make the local and boundary scope explicit. Higher form-degree
curvature actions have not been shown to vanish by this zero-form result.

## Actual complete theta source and a global dual test

Keep the exact ambient extension from Note 01:

\[
 S=\frac{q^{1/4}}{16\pi^2}
       (q^2\mathcal D_z^4-3\pi^2)\vartheta(z,p+iq),
 \quad\mathcal D_z=\partial_z+2\pi is.
 \tag{11}
\]

It is a smooth global section and restricts to Φ(u)e on γ. To extend
the physical test, choose δ=1/8 and an even C∞ cutoff cδ, equal to one
for |v|≤δ/2 and zero for |v|≥δ. In the arithmetic trivialization
|r|,|s|<1/4 set χ(r,s)=cδ(r)cδ(s),

\[
 k_{t,x}(q)=e^{t(\log q)^2/16}\cos(x\log q/4),\qquad
 \kappa_{t,x}=\chi\,k_{t,x}\,e^*.
 \tag{12}
\]

Extend by zero outside that fiber chart. This is a smooth global dual
section, with inverse automorphy under changes of frame. It does not
trivialize the degree-one bundle. Its Hermitian representative is
σ=h^(−1)overline(χk)e, so h(S,σ)=κ(S) exactly. Inserting a=S,b=σ
in (8)–(10) retains all cutoff, connection and metric derivatives. None
is dropped because χ is constant only near the physical path.

The actual path observation is a different integration functional from
the ambient pairing:

\[
 H(t,x)=\underbrace{\int_0^{\log4/4}h(S,\sigma)|_\gamma\,du}_{H_\Omega(t,x)}
       +\int_{\log4/4}^\infty e^{tu^2}\Phi(u)\cos(xu)\,du.
 \tag{13}
\]

The q=4 face is in (8), and the complete source tail is in (13). Neither
has been declared small by the bounded Green identity.

The restricted source components in (5) are
PS|γ=∂pS|γ and QS|γ=Φ′/(4q). Put g₁(u)=−i∂pS|γ, a real source.
In the orthonormal coframe of Note 01,

\[
 \bar\partial_JS|_\gamma=\tfrac12\left\{
 \frac{ig_1}{\sqrt q}(e^1-ie^3)
 +\frac{\Phi'}{4q^{3/2}}(e^2+ie^4)\right\},
\]
\[
 \lvert\bar\partial_JS\rvert^2|_\gamma
 =\frac{g_1^2}{2q}+\frac{(\Phi')^2}{32q^3}.
 \tag{14}
\]

Likewise bar∂Jσ|γ=k_u(e²+ie⁴)/(8q^(3/2)). These are the known p
channel and a damped physical-source derivative, not an independent sign.
The [S06 comparison][completion] already shows the raw p observation is at
the wrong scale: |G₁|²>10^310 E on its pilot. Completing that source
imports the old physical sign; the present identity does not replace it.

There is also a convergence screen for the raw second-order term in (10).
Using the inverse metric and the directional Hessians in Note 01 gives

\[
 (\nabla^*\nabla S)|_\gamma
 =-q^{-1}\partial_p^2S|_\gamma
 -\frac{\Phi''-4\Phi'}{16q^3}
 +16\pi\Phi+3\pi T_0,
 \qquad T_0=e^u\vartheta(0,iq).
 \tag{15}
\]

Indeed at p=0 the rough operator is
−q^(−1)(∇p²+∇q²+q²∇r²+∇s²). Here
∇p²S=∂p²S+2πqΦ, ∇q²S=(Φ″−4Φ′)/(16q²), and
q²∇r²S+∇s²S=q(J₂+K₂)=−18πqΦ−3πqT₀.
The coefficient p derivatives of the complete source decay at the positive
cusp, while T₀=e^u+2ψ. Thus the literal raw restriction in (15) has
zero mode +3πe^u and fails ordinary positive-time half-line heat
integration. This is a statement about this uncompleted zero-form operator
and declared extension, not about full Green pairings or all completions.

## Exact complete-fiber evaluation of the source current

The source's own scalar flux can be evaluated without a scan. In a
unitary chart its coefficient is

\[
 S_U=e^{\pi p^2q}\sum_{n\in\mathbb Z}a(n+s;q)
        e^{\pi ipn^2+2\pi in(r+ps)},
\]
\[
 a(y;q)=q^{1/4}\{\pi^2q^2y^4-\tfrac32\pi qy^2\}
                          e^{-\pi qy^2}.
 \tag{16}
\]

The zero lattice mode cancels on the zero section. Away from that section,
(16) retains the full covariant expression, including connection terms.
It follows from the fourth-jet Hermite polynomial. All fiber series and
their fixed derivatives converge uniformly on the compact base tube.

Integrating in r removes cross modes. Since a is real and even,

\[
 \int_{T^2}(j_{SS})_r\,dr\,ds
 =2\pi e^{2\pi p^2q}\int_{\mathbb R}y\,a(y;q)^2\,dy=0,
\]
\[
 \int_{T^2}(j_{SS})_s\,dr\,ds
 =p\int_{T^2}(j_{SS})_r\,dr\,ds=0.
 \tag{17}
\]

Consequently each integrated face in (8), rather than merely their sum,
vanishes for a=b=S. Therefore

\[
 \int_\Omega\lvert\nabla S\rvert^2
 =2\int_\Omega\lvert\bar\partial_JS\rvert^2.
 \tag{18}
\]

As a normalization check, Gaussian moments give the exact fiber norm

\[
 \int_{T^2}\lvert S\rvert_h^2\,dr\,ds
 =e^{2\pi p^2q}\frac{33}{256\sqrt2}.
 \tag{19}
\]

To see the constant, put v=√(πq)y. The normalized even Gaussian moments
are (2m−1)!!/4^m. Squaring v⁴−3v²/2 gives
(105−180+108)/256=33/256, with the remaining factor 1/√2.
Equations (17)–(19) use the canonical full theta expansion. They are not
claimed for finite weighted sums with failed torus automorphy. Their
positive bulk norm contains no external oscillatory spectral sign.
In particular the zero self-flux does not set the mixed physical-test
flux B(S,σ) to zero.

## A proved obstruction to first-order bulk-to-path transfer

**Proposition 2.** On this fixed tube, there is no constant C such that

\[
 \|a|_\gamma\|_{L^2(d\ell)}^2
 \le C\{\|a\|_{L^2(\Omega)}^2+\|\nabla a\|_{L^2(\Omega)}^2\}
 \tag{20}
\]

for every compactly supported smooth section a. Adding its nonnegative
first-order J-Dolbeault energy or any boundary-current data does not
repair this assertion when the boundary data vanish. A fixed nonzero
smooth weighted path observation is likewise unbounded for this norm.

**Proof.** Work in |p|,|r|,|s|<1/4 over q∈(2,3), with the adapted unitary
frame. Choose A(q)∈C_c∞((2,3)), A≠0, and β∈C_c∞((-1,1)³), equal
to one near zero. For 0<ε<1/8 let

\[
 a_\varepsilon=A(q)\beta(p/\varepsilon,r/\varepsilon,s/\varepsilon)e_U,
 \tag{21}
\]

extended by zero. It is a global smooth section despite the nontrivial
line bundle. It vanishes near every boundary face and has fixed trace
A(q)e_U on γ. The latter has squared norm
∫₂³|A(q)|²√q dq>0.

On the fixed chart the inverse metric is bounded by 6 times its Euclidean
counterpart, dV≤4 dpdqdrds, and (3) gives

\[
 |\mathfrak a|_g^2
 =\pi^2\{(s^2-p^2)^2/q+4q(p^2+s^2)\}<3\pi^2.
\]

Set I₀=∫|A|²dq, I₁=∫|A′|²dq, B₀=∫|β|²dy, B₁=∫|dβ|²dy.
Changing the three transverse variables to εy yields the explicit bound

\[
 \|a_\varepsilon\|_{H^1_\nabla}^2
 \le48I_0B_1\varepsilon
   +\{48I_1+(24\pi^2+4)I_0\}B_0\varepsilon^3\longrightarrow0.
 \tag{22}
\]

The entire boundary current is zero. Equation (9) therefore gives
||∇aε||²=2||bar∂Jaε||², and both tend to zero. This proves (20)
false even with that exact identity imposed.

For a fixed physical (t,x), choose A(q)=ζ(q)k_(t,x)(q), where ζ≥0 is
a nonzero smooth bump in (2,3). Then the path observation
∫A(q)k_(t,x)(q)dq/(4q)=∫ζ k²dq/(4q)>0, independent of ε.
The support may be placed where k is nonzero. For an arbitrary nonzero
complex smooth path weight w, use A=ζ bar w on an interior interval
where w≠0, relocating (2,3) within (1,4) if necessary. Thus the oscillatory
observation itself has no uniform first-order bound over this section
class. Concentrating both entries also disproves a polarized estimate
from products of first-order bulk norms. ∎

There is a related finite-jet version if an attempted estimate uses the
underlying theta-section energy to control its fourth-source observation.
Replace aε in (21) by A(q)β_ε θ. Since β is a plateau near the path,
each fixed vertical jet there is A times the original theta jet, and the
complete fourth-source trace is A(q)Φ. The **underlying section's** H¹
norm still tends to zero. This does not assert that the H¹ norm of its
fourth-source image tends to zero; the norm being tested must be named.

The proposition concerns unrestricted smooth sections measured only by
first derivatives. These cutoffs destroy canonical theta coefficients,
original-I holomorphicity and Jacobi heat. It proves no failure of a
theta-specific estimate on a prescribed PDE solution class. Higher
derivative or elliptic-residual norms are outside its scope; transverse
second derivatives of (21) instead have squared size O(ε^(−1)). A
continuation must derive such additional control and pay its physical
observation cost rather than importing (20).

## Controls, records and next decision

The [fresh control replay][control-record] rejects the same five inherited
event boxes and the separate Euler negative-Laguerre witness at their
strict physical interfaces. It does not validate a new Green inequality.
The Euler witness is not a double-event enclosure. The control premise
audit remains specific:

| Family | Shared premise | Missing input in a theta-specific estimate |
| --- | --- | --- |
| Polynomial/qTa heat events | Generic heat and local geometric identities | Exact theta source and an evaluated physical margin |
| Three-/four-square sources | Local heat/vertical algebra and prescribed finite endpoints | Full reflection, complete canonical coefficients and full theta automorphy |
| Reflected super-Gaussian | Reflection and generic local form geometry | Normalized theta integer-square expansion |
| Finite-prime orbit controls | Selected arithmetic identities and finite observations | Complete reflection or another paid full-source estimate; no effective event box is supplied |
| Smooth-shape/positive-primitive controls | Source shape, primitive positivity and endpoint data | Exact theta square-mode information; analytic events remain analytic |
| Euler-factor sources | Even positive sources and substantial arithmetic/flow structure | Unchanged level-one theta data; its retained signed witness is a separate screen |
| Smooth-density/two-channel constructions | Positive auxiliary spaces | Complete signed physical observation comparison |

Any smooth physical source can be extended locally as a section on the
same line bundle; the generic identity alone therefore discriminates
none of these controls. The canonical full-fiber source calculation (17)
uses stronger theta data. Its conclusion is an energy equality, not a
strict physical estimate, so it need not reject events by itself.

The [exact checker and execution record][record] verify finite matrix,
exterior, polynomial and Gaussian-moment algebra. Analytic convergence,
Stokes and the ε-family proof are given above; finite checks do not prove
their universal statements. The [internal review][review] records the
same-model checking and the resulting stop decision.

The zero-form/first-order-energy route is now screened at the claimed
generic trace comparison. Do not repeat the raw first-order or rough-
Laplacian transform as if it supplied an independent theta constraint.
A next S07 contract must add a specified theta/PDE-dependent trace estimate,
a paid higher-regularity/residual norm, a different form-degree identity,
or an independently estimable complete mixed boundary current. This note
does not select or launch a larger construction. The program's unbounded
real bridge and required complex exterior remain open.

[s07]: ../README.md
[initial]: 01_POINCARE_DUALITY_AND_QUATERNIONIC_SYMMETRY_INITIAL_FINDINGS_20261018.md
[guide]: ../../../research-overview/03_SYMMETRY_RESEARCH_PROGRAM_AND_INVESTIGATION_GUIDE_20261018.md
[summaries]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[geometry]: ../../../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a03]: ../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[metric]: ../../../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/02_ASD_METRIC_FREEDOM_AND_PHYSICAL_RESTRICTION_20261015.md
[completion]: ../../06_hodge_and_transverse_geometry/notes/02_SIGNED_TRANSVERSE_ESTIMATE_AND_EXACT_SOURCE_COMPENSATION_20261018.md
[control-record]: ../numerics/S07_GREEN_SOURCE_CONTROLS_20261018.json
[record]: ../numerics/GREEN_IDENTITY_AND_TRACE_CHECKS_20261018.json
[review]: ../reviews/02_GREEN_IDENTITY_AND_TRACE_OBSTRUCTION_INTERNAL_REVIEW_20261018.md
[verbitsky]: https://arxiv.org/pdf/alg-geom/9307008

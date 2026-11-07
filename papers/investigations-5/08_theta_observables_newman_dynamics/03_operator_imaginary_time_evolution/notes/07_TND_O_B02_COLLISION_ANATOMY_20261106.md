# Collision anatomy in the operator imaginary time realization

6 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**, branch chat0003. **B — author-directed exploratory reconnaissance.** [Request08][request] revises B02 to investigate the event before selecting a control route; [intake][inputs] and [additional inputs][extra] identify consumed versions. The [sole register][progress] owns status.

**Finding.** A finite double collision is a smooth passage of the prepared position amplitude through a quadratic node. Its real zeros have singular velocities, while the field, its operator-domain norms and its global energy remain regular. The small region of opposite sign disappears with vanishing mass and kinetic energy; its energy divided by its own mass diverges. Tracking the extremum or the squared zero gap removes different parts of the coordinate singularity. These observations describe what must eventually be controlled without selecting a control mechanism.

This is a hypothetical analysis of a canonical event, not evidence that theta has one. The exact admitted super-Gaussian source supplies an actual control event. The basic heat geometry and source-sector interpretation are inherited from [direct collision Note04][direct] and [local heat geometry][local]; the operator interpretation and calculations below have proof-author checks only. No new collision exclusion, independent assessment, numerical theta computation or novelty claim is made.

## 1 The field that actually vanishes

Keep E01/E02's complete ambient cylinder, all angular shells and both Dirac signs, fixed unit χ∈Ran P1, K=L0−4I and absolute Fourier readout. Write

\[
h(\tau,x)=H_{\lambda_0-\tau}(x),\qquad
F_\lambda(p)=e^{\lambda p^2}\Phi(p),\qquad
\Psi_\tau(x)=\sqrt{2/\pi}\,h(\tau,x)\chi.
\tag{1}
\]

Then h_τ=h_xx, Ψ_τ=e^(−τK)Ψ_0 and, in the prepared channel, K acts as −∂x². The ambient angular spectrum is unchanged; no higher shell becomes populated at a collision. E01's pointwise smooth representative is justified by the complete source moments; point evaluation on arbitrary ambient L² fields is not being declared bounded.

Suppose an interior finite event satisfies

\[
h(\tau_*,x_*)=h_x(\tau_*,x_*)=0,\quad
a=h_{xx}(\tau_*,x_*)\ne0,
\qquad b=h_{xxx}(\tau_*,x_*),\ c=h_{xxxx}(\tau_*,x_*).
\tag{2}
\]

Here the entire angular vector Ψ_τ*(x*) and its first radial derivative vanish, whereas ∂τΨ=√(2/π)aχ does not. It is a genuine node of this prepared position amplitude. The full Hilbert-space state is nonzero. This interpretation differs from the direct branch's signed probability-difference observation, although the scalar h and its local equations are the same.

Canonical positivity gives h(τ,0)>0, so x*≠0. Evenness supplies a simultaneous reflected event at −x*. Locally around a positive x*, two real zeros become a conjugate pair; combining reflection gives the corresponding quartet. Complex zeros refer to analytic continuation of the readout, not complex position settings or new physical states.

## 2 The local shape and the direction of time

Set s=τ−τ* and y=x−x*. Finite Taylor expansion and h_τ=h_xx give

\[
h(\tau_*+s,x_*+y)
=\frac a2(y^2+2s)+\frac b6(y^3+6sy)
+\frac c{24}(y^4+12sy^2+12s^2)+O_{\rm par}(5).
\tag{3}
\]

Here O_par(5) means O(ε⁵) after y=εY, s=ε²S on a fixed compact (S,Y) set. Complete finite derivatives and joint analyticity of the source transform pay this event-dependent expansion; it is not an infinite operator expansion or a uniform all-height estimate.

The two nearby roots, counted with multiplicity in a small fixed complex disk, obey

\[
z_\pm(\tau_*+s)=x_*-\frac{2b}{3a}s+
\begin{cases}
\pm\sqrt{-2s}+O(|s|^{3/2}),&s<0,\\
\pm i\sqrt{2s}+O(s^{3/2}),&s>0.
\end{cases}
\tag{4}
\]

The analytic implicit-function argument after square-root rescaling establishes these branches; the nonzero complex boundary preserves their total multiplicity. Increasing imaginary time decreases Newman λ: the real pair approaches, meets, and leaves the real axis. The zeros remain present in the complex continuation. This is the standard local forward-heat picture, consistent with Angenent's analytic heat polynomial and local zero loss; its finite-interval theorem requires nonzero spatial boundary values. [Checked source passages][sources] retain those hypotheses.

For a>0, an initially negative pocket lies between positive neighboring lobes and is filled in. For a<0 all signs reverse. A positive heat kernel permits this because the position amplitude being smoothed has both signs. The positive momentum amplitude is a different object.

## 3 A regular extremum crosses zero

The equation h_x(τ,x_c(τ))=0 has one analytic local solution because a≠0. Its value v(τ)=h(τ,x_c(τ)) satisfies the exact identities

\[
x_c'=-\frac{h_{xxx}}{h_{xx}},\qquad v'=h_{xx}
\quad\text{along the critical curve}.
\tag{5}
\]

Consequently

\[
x_c(\tau_*+s)=x_*-\frac ba s+O(s^2),\qquad
v(\tau_*+s)=as+\tfrac12(c-b^2/a)s^2+O(s^3).
\tag{6}
\]

The critical value crosses zero transversely. Its location and velocity remain regular. The critical point is generally not the midpoint of the two roots: their midpoint velocity at the event is −2b/(3a), rather than −b/a.

By comparison, a simple root r satisfies r'=−h_xx/h_x. Equation (4) makes r' diverge as |s|^(−1/2). A field trajectory can therefore be smooth while its individual zero coordinates fail to be differentiable. The extremum description is a useful event coordinate, not an independent inequality constraining v.

## 4 The pair and the rest of the field

Before an isolated double event, factor locally

\[
h(\tau,x)=(x-r_-(\tau))(x-r_+(\tau))G(\tau,x),
\qquad g=G_x/G,
\tag{7}
\]

where G is a real analytic nonvanishing factor on a small neighborhood. Analytic preparation, also used in the repository's [multiplicity note][mult], makes the symmetric quadratic factor regular through the event. No factorization over all zeros is needed.

At a simple root, differentiating (7) twice gives

\[
r_\pm'=-\frac{2}{r_\pm-r_\mp}-2g(\tau,r_\pm).
\tag{8}
\]

Thus, for δ=r_+−r_->0 and q=δ²,

\[
\delta'=-\frac4\delta-2\{g(\tau,r_+)-g(\tau,r_-)\},\qquad
q'=-8-4q\int_0^1g_x(\tau,r_-+t\delta)\,dt.
\tag{9}
\]

The singular mutual attraction in imaginary time is explicit. The influence of the remaining local analytic factor is regular. In particular q extends analytically through the event, q(τ*)=0 and q'(τ*)=−8; on the complex-pair side its real value is negative. At the event

\[
B_*:=g_x(\tau_*,x_*)=\frac{c}{6a}-\frac{b^2}{9a^2},\qquad
q(\tau_*+s)=-8s+16B_*s^2+O(s^3).
\tag{10}
\]

The local correction therefore affects the approach, drift and next order, but cannot change the leading terminal slope at a separated nondegenerate double event. This statement has no uniform neighborhood or coefficient bound over theta events. Higher multiplicity invalidates the two-root/nonvanishing-factor assumption.

Rodgers–Tao's published gap law has the corresponding decomposition, with the opposite Newman-time sign and an infinite-zero sum under its stated hypotheses. We checked v5 §4, Theorem 4.16 and Lemma 4.18(i); their printed contradiction interval Λ<t≤0 is not silently extended here. Equation (9) is a direct local identity without an infinite sum. [Source-use scope][sources].

## 5 What happens to the shrinking sign region

Let ε=τ*−τ>0 and I_τ=(r_-(τ),r_+(τ)). Rescaling x−x*=√(2ε)t in (3), with endpoints tending to ±1, gives

\[
\begin{aligned}
\int_{I_\tau}|h|\,dx
&\sim\frac{4\sqrt2}{3}|a|\,\epsilon^{3/2},\\
M_{\rm lobe}:=\int_{I_\tau}h^2\,dx
&\sim\frac{16\sqrt2}{15}a^2\,\epsilon^{5/2},\\
T_{\rm lobe}:=\int_{I_\tau}h_x^2\,dx
&\sim\frac{4\sqrt2}{3}a^2\,\epsilon^{3/2}.
\end{aligned}
\tag{11}
\]

These follow from the exact integrals of (1−t²), (1−t²)² and t² on [−1,1]. The uniform local expansion and converging scaled endpoints justify their leading constants. Angular integration converts scalar squared mass and radial kinetic form to those of Ψ by the same factor 2/π.

Both the lobe mass and its kinetic contribution vanish. Yet

\[
\frac{T_{\rm lobe}}{M_{\rm lobe}}
\sim\frac{5}{4\epsilon}.
\tag{12}
\]

This is a local quadratic-form quotient: normalizing the ever smaller sign region makes it look increasingly energetic. It is not a blow-up of the original field energy or a new physical conditioning protocol. If extended by zero, the restricted amplitude belongs to the form domain H¹, while its derivative jumps need not put it in the full H² operator domain. That distinction prevents treating (12) as an unqualified K expectation of a cut-off state.

The scalar intensity obeys

\[
\partial_\tau h^2=\partial_x^2h^2-2h_x^2.
\tag{13}
\]

At the double event, h², its first time derivative and its second spatial derivative are zero, while ∂τ²h²=2a². Along the fixed event position it refills as a²s²+O(s³). At the event time its spatial leading term is a²y⁴/4. Two sign transitions disappear from the real amplitude, without a local intensity spike.

## 6 The full state and energy remain regular

With product-measure normalization and (1),

\[
N(\tau)=\|\Psi_\tau\|^2
=\int_{\mathbb R}|F_{\lambda_0-\tau}(p)|^2dp
=\frac2\pi\int_{\mathbb R}h(\tau,x)^2dx>0,
\]
\[
N'=-2\langle\Psi,K\Psi\rangle,\qquad
\frac d{d\tau}\langle\Psi,K\Psi\rangle=-2\|K\Psi\|^2.
\tag{14}
\]

Every fixed K-power norm remains finite and smooth on compact parameter intervals by E01's full-source bounds. For the normalized field φ=Ψ/√N and its mean relative energy E=⟨φ,Kφ⟩,

\[
\phi'=-(K-E)\phi,\qquad
E'=-2\{\langle K^2\rangle_\phi-E^2\},\qquad
\|\phi'\|^2=\operatorname{Var}_\phi(K)<\infty.
\tag{15}
\]

In this channel the energy measure is |F_λ(p)|²dp/N, so E is its mean p². It is not the linear source measure F_λdp/∫F_λ used to express the cosine cancellations. The squared weight has twice the Gaussian exponent; their covariance formulas must not be interchanged.

None of (14)–(15) acquires a singularity at a finite readout collision. The spectrum of K is fixed, with a continuous zero threshold; no eigenvalue degeneracy or new angular occupation is involved. The noncanonical control satisfies these laws and collides, so their monotonicity alone does not exclude the event.

There is a second use of the word energy in zero dynamics. For this local pair, −log δ and δ^(−2) diverge as δ→0. Those are singular functions of zero coordinates. They are not ⟨Ψ,KΨ⟩. The global zero Hamiltonian/energy expressions in Rodgers–Tao require the paper's truncation and convergence work; they are not imported as finite conserved physical quantities here.

## 7 Two ways to see the interference

In momentum space, the field remains the positive amplitude F_λ(p)χ, damped at rate p². At the event,

\[
\int_0^\infty F_\lambda(u)\cos(x_*u)du=0,\qquad
\int_0^\infty uF_\lambda(u)\sin(x_*u)du=0,
\]
\[
\int_0^\infty u^2F_\lambda(u)\cos(x_*u)du=-a\ne0.
\tag{16}
\]

For c_±=max(±cos(x*u),0), define A_±=∫F_λc_± and B_±=(∫u²F_λc_±)/A_±. At a zero, A_+=A_-=A>0 and

\[
a=-A(B_+-B_-),\qquad
\partial_\tau\log(A_+/A_-)=-(B_+-B_-).
\tag{17}
\]

The slope condition in (16) is an additional signed sine balance. Quadratic damping changes equal cosine masses at different rates because their mean p² values differ. This is the direct branch's source-sector interpretation with the present amplitude normalization; it adds no independent event constraint.

A spatial description makes the same process visible through heat averaging. For any Δ>0 with τ*−Δ in the physical orbit,

\[
h(\tau_*,x)=\int_{\mathbb R}k_\Delta(x-y)h(\tau_*-\Delta,y)dy,
\quad k_\Delta(r)=(4\pi\Delta)^{-1/2}e^{-r^2/(4\Delta)}.
\tag{18}
\]

This follows from the fixed Fourier multiplier e^(−Δp²); Gaussian-weighted moments converge by Cauchy–Schwarz even for an L² predecessor. Let dμ(y)=k_Δ(x*−y)h(τ*−Δ,y)dy, a signed measure. Differentiating (18) at the event gives

\[
\int d\mu=0,\qquad \int(y-x_*)d\mu=0,\qquad
\int(y-x_*)^2d\mu=4\Delta^2a.
\tag{19}
\]

The positive and negative heat-weighted contributions have equal mass and equal centroid, but unequal variances. If their common mass is M, then a=M(Var_+−Var_-)/(4Δ²). This explains how a stationary cancellation can be crossed by diffusion. These are analytical decompositions of the existing field, not newly licensed observations. Both descriptions apply to the colliding control.

## 8 Event location can be regular when root tracking is singular

At (2), the map J=(h,h_x) has Jacobian in the order (τ,x)

\[
D J=\begin{pmatrix}a&0\\b&a\end{pmatrix},\qquad \det DJ=a^2>0.
\tag{20}
\]

A small admissible real even source perturbation h_η=h+ηr+O(η²) therefore moves the double event smoothly, locally in both time and position. Its first response is

\[
\tau_*'(0)=-r_*/a,\qquad
x_*'(0)=b r_*/a^2-r_{x,*}/a.
\tag{21}
\]

A bounded smooth even source tilt e^(ηq(u)), with polynomially bounded derivatives of q, supplies one concrete admissible perturbation class with the same moment domination and finite source seminorms. This is the imaginary-time translation of [Note38, §3][response], not a newly selected auxiliary flow. The conditioning deteriorates as a becomes small and depends also on b; there is no uniform stability constant. The event must remain interior to the allowed time/height neighborhood.

Thus a double event need not be a fragile coincidence in the two-parameter spacetime plane, even though individual zeros on a fixed time slice split like a square root. These perturbations generally change canonical arithmetic. Persistence near a colliding control proves neither proximity to theta nor existence of a theta collision.

## 9 Higher finite multiplicity and diagnostic quotients

If the first nonzero spatial derivative has finite order m≥2, write a_m=∂x^m h(τ*,x*). Then

\[
h(\tau_*+\epsilon^2S,x_*+\epsilon Y)
=\frac{a_m\epsilon^m}{m!}
\sum_{j=0}^{\lfloor m/2\rfloor}
\frac{m!S^jY^{m-2j}}{j!(m-2j)!}+O(\epsilon^{m+1}).
\tag{22}
\]

The inherited Hermite-root/analytic-factorization argument gives m local real roots before the event; after it, none remain real for even m, and one remains real for odd m. In each case floor(m/2) pairs leave the real axis. These statements concern fixed finite m and a sufficiently small event-dependent neighborhood. They do not assume all theta events are double.

The generator reads the jet through RχK^jΨ=(−1)^j∂x^(2j)h. For m=2r, the first nonzero such event value is j=r. For m=2r+1, values with j≤r vanish, while ∂x(RχK^rΨ) is nonzero. The double-event critical curve, determinant and two-root gap law need not survive without modification. All fixed operator moments still remain regular.

Off the zero set, w=h_x/h satisfies w_τ=w_xx+2ww_x. At the double-event slice w=2/y+b/(3a)+O(y), and h_xx/h has leading term 2/y². These poles arise from division by the vanishing amplitude; the underlying field and kinetic density remain finite. A logarithmic derivative, phase coordinate or normalized local quotient can be a useful diagnostic without constituting a forbidden dynamical singularity.

At τ*=0 only the forward side belongs to the semigroup orbit. The supplied entire source can describe a two-sided local analytic germ, but no bounded reverse evolution on the ambient Hilbert space is asserted. The same restriction applies to endpoints of any selected time slab.

## 10 Exact control and consistency checks

Use E01/E02's completely paid control

\[
\Phi_*(u)=c_0 e^{-u^2/4}\left(e^{-u^4}+\tfrac12e^{-(u-4)^4}+\tfrac12e^{-(u+4)^4}\right),\quad c_0>0.
\]

At λ*=1/4 it has h*=c_0Q(x)(1+cos4x), where Q(x)=∫₀∞e^(−u⁴)cos(xu)du. At x*=π/4, Q>0 and

\[
a=16c_0Q_*,\quad b=48c_0Q_*',\quad
c=96c_0Q_*''-256c_0Q_*.
\tag{23}
\]

With λ0=1/2, τ*=1/4. Thus a>0, the event is interior, the extremum crosses upward, and the global energy and local-lobe laws coexist with an actual collision. The root-midpoint velocity is −2Q_*'/Q_* and the critical-point velocity is −3Q_*'/Q_*; their difference is a check on the cubic correction. All required source moments and prepared K powers are already paid by E01/E02. The control fails exact canonical theta arithmetic, but no theta-specific premise was used to derive this event anatomy.

The [exact algebra check][check] verifies finite heat-polynomial signs, the asymmetric root/critical-value coefficients, lobe integrals, event-response linear algebra and the product-rule coefficients (23). The [record][checkrecord] reports its finite scope. It checks normalization and algebra; the analytic arguments above supply local limits, not numerical samples. The [schematic][figure] plots only the universal quadratic model, not theta or simulated control data.

The broader family screen remains E02's qualified inventory (Q2); this note does not claim new domain audits for every Euler-factor, weighted-square, primitive or atomic control. No proposed exclusion is being advanced, so no failed used premise is invented for the controls that simply exhibit the same dynamics.

## 11 Questions exposed by the event

This reconnaissance supports several connected questions without ranking them yet. What does the canonical source say about the evolution of a critical value and its curvature before the final local fold? What constrains the regular factor G and its influence on a nearby pair? Can the exact source restrict the simultaneous equal-mass/equal-centroid balances in (19), or their momentum counterparts, beyond generic positivity? Which of these descriptions offers information that can actually be estimated from the complete source?

The local square-root law, the energy-per-lobe divergence and the logarithmic poles all occur in the admitted control. They describe a collision and cannot alone prevent one. The operator viewpoint makes the relation between the physical amplitude, shrinking local mass and regular global state explicit. All formulas have an equally informed direct scalar heat/Fourier derivation; no estimation or acquisition advantage has been shown.

These are diagnostic observations, not another RH-equivalent criterion. Any later global exclusion must be separately classified with its endpoint, multiplicity and confinement requirements. No global first collision at finite height is assumed here. A finite quantitative result would instead be judged by its actual bound and scope, following the [result index][results] and [patterns index][avoid], particularly [target reformulations][a01], [coordinate realizations][a03] and [scoped exclusions][a07].

**Next: [B] TND-O-B02 — Astra**, discuss the event anatomy and decide which question deserves further investigation. The author requested exploration before route selection; this return selects no optimal route or successor E contract. The later mechanism comparison remains available under an explicitly recorded scope. No investigation closure or manuscript milestone is implied.

[request]: ../research-progress/handoffs/08_TND_O_B02_COLLISION_RECONNAISSANCE_REQUEST_20261106.md
[inputs]: ../research-progress/handoffs/08_TND_O_B02_COLLISION_RECONNAISSANCE_INPUTS_20261106.json
[extra]: ../research-progress/handoffs/08_TND_O_B02_COLLISION_ADDITIONAL_INPUTS_20261106.json
[progress]: ../research-progress/01_OPERATOR_ITE_RESEARCH_PROGRESS_20261106.md
[direct]: ../../01_direct_newman_realization/notes/04_TND_D_B02_COLLISION_DYNAMICS_RECONNAISSANCE_20261106.md
[sources]: ../references/03_TND_O_B02_COLLISION_SOURCE_USE_20261106.md
[mult]: ../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/08_REAL_AND_COMPLEX_COLLISION_MULTIPLICITIES_20261015.md
[response]: ../../../05_radial_theta_collision_geometry/notes/38_AUXILIARY_SOURCE_FLOWS_AND_COLLISION_RESPONSE_20261028.md
[results]: ../../../../../result-summaries/README.md
[local]: ../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a03]: ../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[check]: ../numerics/check_collision_anatomy.py
[checkrecord]: ../numerics/COLLISION_ANATOMY_CHECK_20261106.json
[figure]: ../../../../../output/figures/tnd-operator-collision/collision_anatomy.png

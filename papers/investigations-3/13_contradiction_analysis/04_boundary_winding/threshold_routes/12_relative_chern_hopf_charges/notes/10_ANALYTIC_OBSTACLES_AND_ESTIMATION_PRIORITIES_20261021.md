# Analytic obstacles and priorities for endpoint charge exclusion

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **ultra**, verified from the active turn metadata.

The principal obstacle is a strict signed estimate for the unchanged
complete theta source. The manuscript has already supplied local windows,
regular discriminant evolution, source-response identities and a useful
tail enclosure. None yet separates an endpoint collision from the actual
theta data. Height-dependent error control and higher multiplicity remain
separate obligations after the first signed estimate.

This assessment reads the complete [manuscript source][main], the
[project description][readme], the [endpoint overview][overview] and its
[progress register][progress]. Sections 2 and 4 also derive elementary
refinements of the existing response formulas. They are analytic estimating
tools, not a positive theta margin or an exclusion theorem. A separate
[same-model review][review] checks their formulas and scope.

The governing distinctions are in the [result index][results],
[local heat-flow summary][local], [control register][controls] and
[avoid index][avoid], particularly [target classification][a01],
[matched premises][a02], [scoped exclusions][a07] and
[coupled estimates][a12]. Vanishing of all endpoint charges under RH
remains the simplicity target; the estimates below are judged by their
actual error and signed surplus.

## 1 The missing sign and why the geometry cannot supply it

For a proper two-root cluster the manuscript proves
\[
 \Delta'=8+A\Delta,
 \qquad \Delta(0)=0\ \Longrightarrow\
 \Delta(t)=8e^{J(t)}\int_0^t e^{-J(s)}\,ds,
 \quad J'=A,
\]
with real symmetric holomorphic A. Within its real time interval, the
right side is positive for t>0 and negative for t<0. Even A=0 permits the exact event
H=z²−2t. Thus an absolute coefficient bound or a smaller complex-time
phase cannot distinguish an endpoint double. Note 07's explicit window
correctly returns charge one when a double is assumed. Its existence
and strict boundary margins are completed work in that scope.

The useful new input would be an independently established positive
endpoint discriminant, a positive incoming discriminant in the proper
phase-controlled window, or an independently located strictly negative
event in that same window. The first is the most economical immediate
consumer: a fixed-time estimate at t=0 needs neither a negative cap
nor continuation of an auxiliary event through a source homotopy.

Using the manuscript's reference F, complete residual E=H−F and
\(\rho=\sup_\Gamma|E/F|<1\), its signed enclosure requires
\[
 \boxed{\Delta_F(0)+L_- -\mathcal B(\rho)>0},
 \qquad
 \mathcal L_F(E)=\int_0^\infty\psi(u)K_F(u)\,du\ge L_-,
\]
where, at t=0,
\[
 K_F(u)=-4\mathcal I\left[\frac{(z-c)\cos(zu)}{F(z)}\right],
 \quad \mathcal I[g]=\frac1{2\pi i}\oint_{|z-a|=R}g(z)\,dz,
\]
\[
 \mathcal B(\rho)=4R(R+r)l_2(\rho)+R^2l_1(\rho)^2,
 \quad l_1=-\log(1-\rho),\quad l_2=l_1-\rho.
\]
Here c is the reference root centroid and both reference roots lie
in |z−a|<r<R. All bounds must include the complete residual. At a
reference double b, \(\mathcal L_F(E)=-8E(b)/F_{zz}(b)\): the sign is
an oscillatory measurement relative to curvature, not a consequence of
positive source mass. See [the signed response proof][source].

There is a precise cancellation warning. If the unchanged H actually
had a double in this fiber, its exact response would imply
\[
 |\Delta_F+\mathcal L_F(E)|\le\mathcal B(\rho).
\]
Making the head longer drives the residual and this error down, but does
not itself rule out that cancellation. Convergence to the answer is not
an independently proved sign. The endpoint transport constant is also
exactly Δ(0); rewriting it does not remove this obligation.

## 2 Retain more signed information before tightening absolute bounds

### Use the actual canonical tail distribution

The manuscript's tail theorem gives, for canonical cutoff M,
\[
 \mathcal L_F(E)=A_MJ_K+(E_M-A_M)\int C_K(w)\,d\sigma_M(w),
\]
where σ_M is an explicitly specified probability measure, E_M is the
total normalized tail mass, A_M the first omitted atomic mass,
\(C_K(w)=\int_0^w W(u)K_F(u)\,du\), and J_K=C_K(∞).
Its present enclosure replaces the expectation by the global minimum
and maximum of C_K. When both reference roots lie in Re z>0, the
manuscript proves that this strictly beats the matched pointwise envelope.
The gain can be arbitrarily small and the resulting interval can still
contain zero; strict improvement is not asserted for every reference.

The next useful calculation should retain the actual masses of σ_M.
For a finite partition I_j of [0,∞), including its last unbounded interval,
put p_j=σ_M(I_j). Then
\[
 \sum_jp_j\inf_{I_j}C_K
 \le\int C_K\,d\sigma_M
 \le\sum_jp_j\sup_{I_j}C_K.                 \tag{1}
\]
This follows by integrating the interval bounds; it contains no new
positivity hypothesis. With exact masses, refinement cannot widen the
enclosure and the one-bin case is the existing theorem. In the notation
\(d\sigma_M=-z_M'(w)dw\), an interval [a,b) has mass z_M(a)−z_M(b),
and [W,∞) has mass z_M(W). These quantities are fixed by the canonical
Laplace law. Certified mass errors require sign-aware interval arithmetic
and the constraint Σp_j=1; substituting a lower mass next to a negative
lower integrand is invalid. Complete tail and extrema bounds are required.

This retains coefficient information discarded by complete monotonicity
alone. The manuscript explicitly identifies weighted-square sources that,
when they match the head through M+1 and the source value at zero, share
F,W,A_M,E_M and the existing monotone enclosure. Their actual measures
can differ. That observation does not construct a collision in any
prescribed matching window, and using more masses does not prove that
every colliding control is separated. The actual inequality must be
checked, rather than treating a changed source formula as automatic
failure of its numerical conclusion.

### Keep the quadratic response when it controls the uncertainty

There is a direct refinement of the exact logarithmic formula. Put
e=E/F and
\[
 Q_F(E)=2\mathcal I[(z-c)e^2]-(\mathcal I[e])^2,
 \qquad l_3(\rho)=l_2(\rho)-\rho^2/2.
\]
Then
\[
 \Delta_H=\Delta_F+\mathcal L_F(E)+Q_F(E)+R_3,
\]
\[
 |R_3|\le\mathcal C_3(\rho):=
 4R(R+r)l_3(\rho)
 +R^2\{2\rho l_2(\rho)+l_2(\rho)^2\}.       \tag{2}
\]
To prove (2), use ℓ=log(1+e),
\(|\ell-e+e^2/2|\le l_3\) and |ℓ−e|≤l_2 in
\(\Delta_H-\Delta_F=-4\mathcal I[(z-c)\ell]-(\mathcal I[\ell])^2\).
The difference between the last square and (I[e])² is bounded by
\(R^2(2\rho l_2+l_2^2)\). The error is O(ρ³), with the centroid
correction retained. It has no inverse internal root gap; it still
depends on the wall ratio and radii.

This is worth using if the quadratic allowance is the dominant loss.
It requires a signed enclosure of Q_F, including its mixed source terms.
Replacing Q_F by a large absolute bound can erase the benefit. Nor is
(2) uniformly better numerically for every ρ<1. The exact logarithmic
formula itself is another option when ρ is too large for the truncated
expansion to help. None of these universal formulas supplies a theta sign.

The acceptance test becomes a positive *combined* lower bound for
Δ_F+L+Q after (2), probability-mass errors, contour errors and complete
source tails have all been subtracted. Under a hypothetical true double,
that combined quantity instead obeys |Δ_F+L+Q|≤C_3. The new estimate
therefore makes the question sharper without presupposing its answer.

### Use event displacement only when its reference is advantageous

The alternative bound in the manuscript is
\[
 \tau_1\le\tau_0+\frac{E(\tau_0,b_0)}{F_{zz}(\tau_0,b_0)}
 +\frac12\left(\frac{C_4E_0^2}{\nu^3}
                   +\frac{2E_2E_0}{\nu^2}\right).
\]
It pays continuation through common two-wall counts, cap persistence,
phase control and a curvature floor ν. This route becomes attractive
when a reference event is independently known and its signed displacement
has a useful margin. Without that advantage it adds substantial payments,
including inverse powers of ν, to the same unresolved source sign.

## 3 Height coverage means relative error control at shrinking scales

Every hypothetical finite-height double has a positive window. With
q=|H_zz(0,a)|/2 and complete moments B_j, the existing prescription is
\[
 R=\min(R_0/2,q/B_3),\quad r=R/2,\quad
 h=\min\{T_0/2,qR^2/(16\sqrt2B_2),R^2/128\}.
\]
It has wall floors >qs²/2 and phase product at most 3/4. There is no
proved positive lower bound for q over all candidate heights. The
manuscript obtains q(a)≤C/|a| and corresponding upper bounds R=O(|a|⁻¹),
h=O(|a|⁻³) for this conservative prescription. These are not actual gap
asymptotics, lower bounds, or necessary scales for other constructions.

The next source theorem should therefore be pointwise in a,q,R,h, with
an explicit admissible cutoff M and errors relative to the signed margin.
For example, writing θ=r/R gives the dimensionless payment
\[
 \frac{\mathcal B(\rho)}{R^2}
 =4(1+\theta)l_2(\rho)+l_1(\rho)^2.
\]
This exposes which deterioration comes from the external wall ratio
and which comes from the signed observable itself. Normalization does
not prove either ratio small. It helps prevent an absolute source norm
from being compared with a shrinking discriminant on incompatible scales.

For an analytical contradiction, a parameterized pointwise theorem can
suffice; a common cutoff or common window is unnecessary. A computational
search over bounded heights alone cannot establish the universal signed
statement. The close normalized endpoint controls in BW10 show why fixed
positive source-distance tolerances are insufficient; they fail ordinary
Dirichlet-series arithmetic, not the recorded positive-time reality and
simplicity premises.

A common negative all-real time slice is unavailable by the real-zero
threshold theorem and [Rodgers and Tao's nonnegativity theorem][rt].
Local negative caps depending on the cluster remain allowed. A fixed
positive bound on the weighted excess K−Z also cannot exclude every
height: a unit endpoint charge at physical height a has weight 8/(1+a²).

## 4 Higher multiplicity needs a different signed consumer

For an m-root cluster, the [many-root manuscript][many] proves the first
identity below; at a full m-fold endpoint birth it also proves the asymptotic
\[
 \mathfrak D'=8\mathfrak T+B\mathfrak D,
 \qquad
 \mathfrak D\sim d_mt^{m(m-1)/2}.
\]
The forcing T is no longer constant and vanishes at a full higher birth.
The exact quartic H=z⁴−12tz²+12t² has B=0, positive discriminants on both
real caps, and endpoint charge six. The cubic H=z³−6tz+2 has nonreal
event times even with B=0. These controls invalidate a direct extension
of the two-root cap formula. Choosing one pair from an m-fold birth
also fails: the other birth roots destroy its isolating collar.

Full discriminant winding remains valid when its whole boundary is
paid. A cheaper possible *endpoint-only* consumer is the centered second
moment, provided it is used only to contradict a full birth of the entire
retained cluster. This avoids mistaking it for a detector of all collisions.

Let F have exactly m roots, all in |z−a|<r<R, be nonzero on Γ, and let
H=F+E with sup_Γ|E/F|≤ρ<1. Both clusters then have m roots. Define
\[
 S_k(G)=\mathcal I[(z-a)^kG_z/G],\quad
 V_G=S_2(G)-S_1(G)^2/m,\quad c=a+S_1(F)/m.
\]
The contour integrations by parts used for the two-root response give
\[
 V_H-V_F=-2\mathcal I[(z-c)\ell]
                   -\frac{(\mathcal I[\ell])^2}{m},       \tag{3}
\]
and therefore, with \(\mathcal L^V_F(E)=-2\mathcal I[(z-c)E/F]\),
\[
 |V_H-V_F-\mathcal L^V_F(E)|
 \le 2R(R+r)l_2(\rho)+\frac{R^2}{m}l_1(\rho)^2.         \tag{4}
\]
Indeed δS_1=−I[ℓ], δS_2=−2I[(z−a)ℓ]; substitution proves (3),
and |z−c|≤R+r proves (4). This holds without labeling individual roots.
For real-symmetric F and H, with real center a, the terms are real. The signed source kernel
is \(-2\mathcal I[(z-c)\cos(zu)/F(z)]\), so the complete-tail
probability estimate (1) applies to this kernel too. Its oscillation or
a strict comparison gain for m>2 would require separate proof.

If an exact m-fold endpoint is hypothesized, isolate precisely those m
roots using the existing full-birth window. Then V_H(0)=0. An independent
strict positive lower bound from (4) would contradict that full birth.
This is a conditional consumer; no such theta lower bound is supplied.
At a full reference birth F=U(z−b)^m, the linear term is
\[
 \mathcal L^V_F(E)=-\frac2{(m-2)!}
                   \partial_z^{m-2}(E/U)(b).
\]
It exposes the increasing derivative-information burden as m grows,
while retaining the exterior unit U.

The scope restriction is essential. The cubic control at t=1/2 has
roots (−2,1,1), V=6 and a double event: positivity of V does not exclude
a partial collision in a larger cluster. Hermite full births instead
have V(t)=2m(m−1)t, hence V(0)=0; the signed estimator must retain this
zero. No charge or event-uniqueness statement is inferred from (3).
For a proper cubic, the manuscript's real-event monotonicity offers a
separate negative-event-location route; it does not cover m≥4.

## 5 Controls and the next research deliverable

The new response expansions and weighted expectation bounds are universal
analytic tools. They are allowed to hold for colliding controls. A claimed
positive endpoint lower bound must fail on a control with the same endpoint
event and vanishing observable, or use an explicitly absent hypothesis:
Δ vanishes for the retained colliding two-root pair, whereas V vanishes
at full coalescence of the entire retained m-root cluster. An event at
another time or a partial collision in a larger cluster is a different test.

| Control family | Consequence for the proposed work |
| --- | --- |
| Quadratic heat event and affine perturbations | Geometry and response identities pass. The exact endpoint collision has Δ=0. For F=z² and E=bz+c, the linear response is −4c and Q=b², reproducing Δ_H=b²−4c; sign must come from measured data. |
| Cubic and quartic Hermite controls | Two-cap inference fails outside two roots. Equations (3)–(4) must retain V(0)=0 at a full birth; a larger cluster with a partial collision can have V>0. |
| Finite envelope-moment perturbations | Selected complete envelope moments and strict local geometry permit either event direction. This is a constructed moment vector, not the actual theta vector, and supplies no global all-real slice. |
| Euler-factor and weighted-square or finite-prime controls | Canonical arithmetic or full normalized reflection fails as specified in the control register. Positive tail mixtures alone can still hold; more measured canonical masses are not automatically a separating sign. |
| Reflected, smooth and positive-primitive controls | Their individual shape and completion premises do not impose the canonical square expansion. Keep the different preservation lists separate. |
| Close normalized endpoint sources | Even RH-compatible endpoint behavior and arbitrarily small source distance allow an escaping double. Ordinary Dirichlet-series arithmetic fails. Fixed tolerance is insufficient; height-dependent exact-source estimates remain outside this obstruction. |

The most effective next work package is a coupled signed-source estimate
at t=0, with the actual canonical law retained. Establish the net lower
bound, its complete error budget and its dependence on the hypothetical
event parameters before expanding numerical coverage. Use (2) when its
quadratic term is measurable and the previous quadratic error is the
limiting loss; otherwise identify the dominant loss first. A bounded
diagnostic can compare the actual-law enclosure, the existing monotone
enclosure and the exact-log response on the same source data, but a known
separated pair is only a calibration case.

Parallel structural work can develop (3)–(4) for full births, while
explicitly testing the source derivative and multiplicity dependence.
It should not delay the first genuinely positive two-root source bound.
Do not spend the next round re-proving window existence, tightening an
already sufficient phase bound, or enlarging the known low separated-pair
certificate as evidence of endpoint exclusion.

ECE-01 retains its completed parameterized scope. ECE-02 and the signed
parts of ECE-04–05 remain open; ECE-03 and ECE-06 remain gated. The
refinements here have same-model internal mathematical checks, not
independent specialist validation. The manuscript is unchanged.

[main]: ../manuscript/main.tex
[source]: ../manuscript/source.tex
[many]: ../manuscript/many.tex
[readme]: ../README.md
[overview]: ../research-overview/02_ENDPOINT_CHARGE_EXCLUSION_PROGRAM_20261021.md
[progress]: ../research-progress/02_ENDPOINT_CHARGE_EXCLUSION_PROGRESS_20261021.md
[review]: ../reviews/10_ANALYTIC_OBSTACLES_AND_RESPONSE_REFINEMENTS_REVIEW_20261021.md
[results]: ../../../../../../../result-summaries/README.md
[local]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[rt]: https://arxiv.org/abs/1801.05914v5

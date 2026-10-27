# Circle heat lift and the obstruction to homogeneous boundary transfer

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Research conversation: **Begin radial theta collision study**, thread `01a17e9c-bfd5-7782-a76f-b2a2eaa82417`, Investigation05 chat0001.

**Status: first bounded RTC-03 return; exact identities and scoped obstructions proved in-note, with same-assistant checking only.** The selected construction retains the whole integer lattice as a circle variable. Its two source channels satisfy an exact parabolic system, but this is an infinite-dimensional system of functions on the circle. Passing that system through the forced Helmholtz equation creates an explicit, nonzero commutator. Moreover, the actual canonical lifted boundary function is never identically zero on the circle, even when its physical point evaluation might vanish. Consequently this lift does not turn the physical zero condition into a homogeneous boundary condition on the whole circle.

This is a failure of the specified transfer, finite transverse closure and unweighted circle-current inference. It is not an exclusion of other geometric realizations, nonlinear modular systems, source-specific inequalities, or global collision arguments. **No canonical collision, new time-height region, Newman bound, or endpoint multiple zero is excluded.**

The [handoff][handoff] and [Note01][initial] supply the objects being continued. The [result index][results], especially [theta identities][arithmetic], [geometric realizations][geometry] and [controls][controls], and the [avoid index][avoid] govern the claim classification. This return is a precise obstruction, not a proposed RH-equivalent sign criterion. Related earlier work already treats [transverse theta derivatives][oldtransverse] and [joint source currents][oldcurrent]; no priority or independent-review claim is made.

## 1. Domain and complete source

Keep physical time \(t\in[b,T_+]\), with \(0<b<T_+<\infty\), and physical frequency \(a>0\), with \(\lambda=a^2/4\). These are symbolic parameters, not a certified region. Uniformity in frequency below means on each compact \(\lambda\)-interval, not all-height uniformity. The integral identities extend locally uniformly to finite complex \(t,\lambda\). Positivity statements use real parameters.

Let \(\vartheta\in\mathbb R/\mathbb Z\) be an auxiliary circle coordinate, distinct from physical frequency. Put

\[
K(s,\vartheta)=\sum_{n\in\mathbb Z}e^{-\pi n^2s}e^{2\pi in\vartheta},
\quad s=e^{2x}=r^2,\quad D=\partial_x,\quad L=\partial_\vartheta^2,
\quad c(x)=\frac{e^{2x}}{2\pi}.
\tag{1}
\]

Thus \(K(s,\vartheta)=\theta_3(\pi\vartheta\mid is)\). Normal convergence of the full series gives

\[
K_s=\frac1{4\pi}LK,\qquad DK=cLK.
\tag{2}
\]

This is the theta heat equation in a geometric parameter, not physical backward heat. Its normalization was checked against [DLMF 20.2.3](https://dlmf.nist.gov/20.2.E3) and [20.13.1–2](https://dlmf.nist.gov/20.13); the [reference annotation][refs] records the limited inspection.

Define

\[
w_t(x)=e^{tx^2/4+x/2},\quad h_t=D\log w_t=tx/2+1/2,
\quad F=w_tK,
\]
\[
U=cLF,\qquad V=c^2L^2F,\qquad
G=3U+V=w_t(D^2+D)K.
\tag{3}
\]

The last equality uses \(c'=2c\). On the physical restriction,

\[
G(t,x,0)=r^{5/2}e^{t\log^2r/4}\Delta_3\Theta(r)
=4e^{tx^2/4}\Phi(x/2)=g_t(x).
\tag{4}
\]

The n-th Fourier coefficient, for every \(n\ne0\), is exactly

\[
\widehat G_n=w_t(4p_n^2-6p_n)e^{-p_n},
\qquad p_n=\pi n^2e^{2x};\qquad \widehat G_0=0.
\tag{5}
\]

There is no lattice truncation, altered conductor or fitted source coefficient. On \(x\ge0\), every nonzero coefficient in (5) is positive. Fixed derivatives are bounded by polynomials in \(x,n,e^{2x}\) times \(e^{T_+x^2/4+x/2-\pi n^2e^{2x}}\), with analogous bounds on compact complex parameter sets. This justifies the circle sums, half-line integrals and finite derivatives below. It also gives super-exponential tails at \(x=+\infty\).

## 2. Exact source evolution and the unresolved transverse dimension

Set

\[
P_t=D-cL-h_t,\qquad \mathcal T=\partial_t-x^2/4.
\]

Direct differentiation gives

\[
P_tF=0,\quad P_tU=2U,\quad P_tV=4V,
\quad (P_t-2)(P_t-4)G=0,
\tag{6}
\]
\[
\mathcal TF=\mathcal TU=\mathcal TV=\mathcal TG=0,
\qquad [\mathcal T,P_t]=0.
\tag{7}
\]

For example, \(P_t(cLF)=c'LF=2U\); the calculation for \(V\) is identical with \((c^2)'=4c^2\). In (7), \(-\partial_th_t=-x/2\) cancels \([ -x^2/4,D]=x/2\). The two-channel system is

\[
DU=(cL+h_t+2)U,\qquad DV=(cL+h_t+4)V.
\tag{8}
\]

These are two **circle-valued** channels. They are not two scalar states on the physical path. The physical restrictions of their right sides contain \(LU|_0,LV|_0\), whose equations contain further transverse derivatives.

The equations (2), (6) and (8) also hold after replacing the coefficients 1 in (1) by any fixed symmetric polynomial-growth sequence. They use the square-mode equations, but alone do not encode the canonical coefficient normalization and full reflection. In particular, weighted-square collision controls satisfy the same modewise dynamics. Full reflection is retained separately in §4.

## 3. Passing through the forced equation: the exact nonzero residual

Let \(A_\lambda=D^2+\lambda\), and let \(\mathcal V_\lambda\) denote the tail-selected Volterra inverse in Note01. Define

\[
\mathscr Y(t,x,\vartheta;\lambda)
=\int_x^\infty\frac{\sin(\sqrt\lambda(s-x))}{\sqrt\lambda}
G(t,s,\vartheta)\,ds,
\quad \beta(t,\vartheta;\lambda)=D\mathscr Y(t,0,\vartheta;\lambda).
\tag{9}
\]

The kernels have their entire limiting values at \(\lambda=0\). Then

\[
A_\lambda\mathscr Y=G,\quad
\mathscr Y(t,x,0;\lambda)=Y(t,x;\lambda),\quad
\beta(t,0;\lambda)=B(t,\lambda)=-8H(t,2\sqrt\lambda).
\tag{10}
\]

The selected super-exponential tail, including differentiated tails, is part of (9). Mere decay at complex \(\lambda\) is not substituted. The response still has Note01's physical evolution, now for every \(\vartheta\):

\[
\mathscr Y_t=x^2\mathscr Y/4+xD\mathscr Y_\lambda
-3\mathscr Y_\lambda/2-\lambda\mathscr Y_{\lambda\lambda}.
\tag{11}
\]

The additional commutator is

\[
\boxed{\mathcal C_t:=[P_t,A_\lambda]=(4cL+t)D+4cL.}
\tag{12}
\]

Indeed \([P_t,D]=2cL+t/2\), and applying the product rule to \(D^2\) gives (12). Therefore

\[
A_\lambda(P_t\mathscr Y)=P_tG-\mathcal C_t\mathscr Y,
\quad P_tG=6U+4V,
\]
\[
\boxed{P_t\mathscr Y-\mathcal V_\lambda(P_tG)
=-\mathcal V_\lambda(\mathcal C_t\mathscr Y).}
\tag{13}
\]

All terms obey the same super-exponential tail, so uniqueness of that tail-selected inverse proves (13). If \(S=(P_t-2)(P_t-4)\), the corresponding higher equation is

\[
A_\lambda S\mathscr Y
=-(P_t\mathcal C_t+\mathcal C_tP_t-6\mathcal C_t)\mathscr Y.
\tag{14}
\]

Thus applying the source closure to the response cannot omit its commutators.

**The residual in (13) is nonzero for the actual canonical response.** On the n-th nonzero mode, (12) reads

\[
\mathcal C_t\widehat{\mathscr Y}_n
=(t-8p_n)D\widehat{\mathscr Y}_n-8p_n\widehat{\mathscr Y}_n.
\tag{15}
\]

If this vanished identically on a sufficiently far tail, its first-order homogeneous equation would give either the zero solution or

\[
\widehat{\mathscr Y}_n=C e^{-x}(1+O(e^{-2x})),\quad C\ne0,
\]

because \(8p_n/(t-8p_n)=-1+O(e^{-2x})\), with integrable correction. The latter violates the selected tail. The zero solution contradicts \(A_\lambda\widehat{\mathscr Y}_n=\widehat G_n>0\) on that tail. Hence no nonzero lattice mode has identically vanishing commutator residual. This argument holds for each finite real \(t,\lambda\), and does not assume a physical zero.

The full first-jet observation cost is explicit. With

\[
E=P_t\mathscr Y-\mathcal V_\lambda(P_tG),\quad R=\mathcal C_t\mathscr Y,
\]

one has, for \(\lambda>0\),

\[
E(0,\vartheta)=-\int_0^\infty\frac{\sin(\sqrt\lambda s)}{\sqrt\lambda}R(s,\vartheta)\,ds,
\quad DE(0,\vartheta)=\int_0^\infty\cos(\sqrt\lambda s)R(s,\vartheta)\,ds,
\tag{16}
\]
\[
\partial_\lambda DE(0,\vartheta)=\int_0^\infty
\left[-\frac{s\sin(\sqrt\lambda s)}{2\sqrt\lambda}R(s,\vartheta)
+\cos(\sqrt\lambda s)\mathcal C_t\mathscr Y_\lambda(s,\vartheta)\right]ds.
\tag{17}
\]

Neither integral is assigned a favorable sign or declared small. The actual lower boundary also remains:

\[
D(P_t\mathscr Y)(0,\vartheta)
=G(0,\vartheta)-(\lambda+t/2)\mathscr Y(0,\vartheta)
-2c(0)L\mathscr Y(0,\vartheta)
-(c(0)L+1/2)\beta(\vartheta).
\tag{18}
\]

At a physical event, \(\beta(0)=\beta_\lambda(0)=0\) does not set \(L\beta(0)\) to zero. Equations (16)–(18) are the residual and boundary payments for this construction; they are not a new collision exclusion estimate.

## 4. Full reflection, the origin, and the infinity normalization

The full Jacobi transformation, with its principal square root, gives

\[
K(e^{2x},\vartheta)=e^{-x}e^{-\pi e^{-2x}\vartheta^2}
K(e^{-2x},i e^{-2x}\vartheta).
\tag{19}
\]

This follows from [DLMF 20.7.32](https://dlmf.nist.gov/20.7.E32), with the same argument normalization as (1). It sends a real circle argument to an imaginary argument, except at the physical point. It is not an inversion of the same real circle with the same pointwise positivity.

For completeness the source's full transformed differential expression is as follows. Put \(x'=-x\), \(\eta=i e^{-2x}\vartheta\), \(z=\pi e^{-2x}\vartheta^2\), and \(\mathfrak D=-\partial_{x'}-2\eta\partial_\eta\). Applying \(D^2+D\) to (19), with the derivative taken at fixed original \(\vartheta\), gives

\[
G(t,x,\vartheta)=w_t(-x)e^{-z}
\left[\mathfrak D^2+(-1+4z)\mathfrak D+(4z^2-6z)\right]
K(e^{2x'},\eta)\big|_{x'=-x,\,\eta=i e^{-2x}\vartheta}.
\tag{20}
\]

The prefactor has logarithmic derivative (-1+2z), whose derivative is (-4z); these produce the final coefficient in (20). At \(\vartheta=0\), (20) gives \(G(t,x,0)=G(t,-x,0)\) exactly. In particular \(Dg_t(0)=0\). This endpoint cancellation holds after the full sum: the individual modal derivatives at zero are

\[
D\widehat G_n(t,0)=(-8q_n^3+30q_n^2-15q_n)e^{-q_n},
\quad q_n=\pi n^2,
\quad \sum_{n\ne0}D\widehat G_n(t,0)=0.
\tag{21}
\]

They are not separately zero. Physical time does not enter (21), since \(D e^{tx^2/4}=0\) at the endpoint.

At \(x\to-\infty\), the complete modular asymptotic \(K(e^{2x},0)\sim e^{-x}\) gives

\[
U(t,x,0)\sim-e^{tx^2/4-x/2},\qquad
V(t,x,0)\sim3e^{tx^2/4-x/2}.
\tag{22}
\]

The large terms cancel in \(3U+V=G\), whose physical trace is super-exponentially small by reflection. Consequently the two channels cannot be integrated separately over the full logarithmic line at positive physical time. The half-line construction is convergent; its inversion partner must be recombined before a tail limit. No origin contribution is lost by treating (8) on \(x\ge0\).

In the original radial variables, nothing changes Note01's normalization:

\[
M_t=16H(t,i),\quad
\mathcal T_t(r)=M_t+\int_r^\infty(s^2/r-s)Q_t(s)\,ds,
\]
\[
\mathcal T_t\sim M_t/r\ (r\downarrow0),\quad
\mathcal T_t\to M_t\ (r\to\infty),\quad
\Delta\mathcal T_t=Q_t-4\pi M_t\delta_0.
\tag{23}
\]

In particular, the circle mean \(widehat G_0=0\) is not the radial mass and does not set \(M_t=0\) or freeze it at one.

## 5. A precise finite transverse closure obstruction

Fix any \(x\ge0\) and finite real \(t\). If a polynomial \(p\) satisfies

\[
p(L)G(t,x,\cdot)=0\quad\hbox{as a function on the circle},
\tag{24}
\]

then (5) implies \(p(-4\pi^2n^2)=0\) for every \(n\ge1\). Each of these Fourier coefficients is nonzero, so the polynomial has infinitely many distinct roots and is identically zero. Thus the transverse derivatives \(G,LG,L^2G,\ldots\) are linearly independent as circle functions at every such ((t,x)).

It follows that no finite-dimensional \(L\)-invariant linear subspace of smooth circle functions can contain this canonical \(G\). Otherwise the restriction of \(L\) to that space would have an annihilating polynomial, contradicting (24). Coefficients of a proposed finite polynomial closure may depend on (t,x); the argument applies at each fixed pair.

**Scope:** this excludes finite invariant linear transverse state spaces and polynomial annihilation of the whole circle profile. It does not exclude nonlinear identities among theta constants, nonlocal operators, estimates, or a scalar relation imposed only after evaluating at \(\vartheta=0\). In particular it does not contradict Note01's known source-dependent logarithmic-derivative closure. A list of scalar transverse derivatives at one point is not what (24) asserts to be independent.

## 6. The canonical source changes sign on the circle, and its boundary vector never vanishes

First, \(\int_0^1G(t,x,\vartheta)d\vartheta=0\), whereas \(G(t,x,0)>0\) for \(x\ge0\). Continuity therefore forces negative values elsewhere on the circle, for every such (x,t). The original positive source has become the value at one point of a sign-changing lift. A positivity argument for the circle heat kernel cannot simply be applied to the differentiated source (3).

There is a stronger obstruction at the actual boundary, independent of whether the physical field vanishes. For \(n\ge1\), (9) gives

\[
\widehat\beta_n(t,\lambda)=-\int_0^\infty
w_t(x)(4p_n^2-6p_n)e^{-p_n}\cos(\sqrt\lambda x)\,dx.
\tag{25}
\]

With \(q=\pi n^2\) and \(v=p_n-q\), this is exactly

\[
\widehat\beta_n=-e^{-q}\int_0^\infty[2(q+v)-3]
(1+v/q)^{1/4}\exp\!\left[\frac t{16}\log^2(1+v/q)\right]
\cos\!\left[\frac{\sqrt\lambda}{2}\log(1+v/q)\right]e^{-v}\,dv.
\tag{26}
\]

For \(t,\lambda\) in compact real sets with \(\lambda\ge0\), dominated convergence proves

\[
\boxed{\frac{e^{\pi n^2}}{\pi n^2}\widehat\beta_n(t,\lambda)\longrightarrow-2.}
\tag{27}
\]

To check domination, divide the integrand in (26) by (q). For \(q\ge1\), its absolute value is bounded by a constant times

\[
(1+v)^{5/4}\exp\!\left[\frac{\max(T_+,0)}{16}\log^2(1+v)-v\right],
\]

which is integrable; the cosine has modulus at most one. On bounded (v)-intervals the convergence to \(2e^{-v}\) is uniform in the compact parameters, giving uniformity of (27). No finite cutoff or all-frequency onset is supplied or needed for this assertion.

Therefore \(\widehat\beta_n<0\) for all sufficiently large n at every finite real \((t,\lambda)\\) under consideration. In particular

\[
\boxed{\beta(t,\cdot;\lambda)\not\equiv0\quad\hbox{for every finite real }t,\lambda\ge0.}
\tag{28}
\]

The n=0 coefficient is zero, so also \(\int_0^1\beta\,d\vartheta=0\). The physical boundary condition is only \(\beta(t,0;\lambda)=0\), a cancellation among modes. It cannot be replaced by a homogeneous Neumann condition on the whole circle, which never holds for this lifted solution. At multiplicity m, vanishing of the first m \(\lambda\)-derivatives at the physical point still does not change (28).

The limit in (27) is a **large lattice-index** limit at bounded physical parameters. It is not a high-physical-frequency estimate or a proof that the physical sum (B) is nonzero.

## 7. What the circle current measures

For real \(t,\lambda\), the lifted fields are real on the circle. The complete Green identity on \(0\le x\le R\), integrated with any fixed smooth real periodic weight \(\rho\), is

\[
\int_0^1\rho\,[\mathscr Y\beta_\lambda-\beta\mathscr Y_\lambda]_{x=0}d\vartheta
=\int_0^R\!\int_0^1\rho(\mathscr Y^2+G\mathscr Y_\lambda)d\vartheta dx
+\int_0^1\rho[\mathscr YD\mathscr Y_\lambda-D\mathscr Y\mathscr Y_\lambda]_{x=R}d\vartheta.
\tag{29}
\]

The outer term tends to zero by (9). Choosing \(\rho=1\) removes off-diagonal Fourier products; evaluating at the physical point retains them. These are different observations. The physical event conditions do not set the left side of the averaged identity to zero. Statement (28) exposes the boundary mismatch; it does not claim the averaged Wronskian is nonzero or has a fixed sign at every hypothetical event.

Localizing the parabolic energy to the physical point adds its own exact term:

\[
\int_0^1\rho fLf\,d\vartheta
=-\int_0^1\rho(\partial_\vartheta f)^2d\vartheta
+\frac12\int_0^1\rho''f^2d\vartheta.
\tag{30}
\]

Periodicity pays both circle endpoints. A nonconstant smooth periodic weight has second derivative of both signs. Thus the usual dissipation term does not justify dropping the localization term. A limit toward point evaluation requires a separate comparison and retains the physical forcing contribution. At \(\vartheta=0\), (29) is precisely Note01's \(N_t+C_t\) identity, with its known possible cancellation; there is no new sign there.

## 8. Control screen and evidence

This is an analytic premise screen, not a new numerical experiment on every registered control. The [control register][controls] remains the source for their actual event and threshold claims.

| Family | What survives here | Canonical premise absent, or limitation of the inference |
| --- | --- | --- |
| Note01 Gaussian-polynomial control | Positive even physical source, generic forced ODE, time response and exact Wronskian cancellation | No unchanged integer-square expansion or theta tails; the canonical circle source (3) is not its source |
| Finite weighted-square / finite-tail controls | Mode heat equation, prescribed source differential operator, circle transfer algebra | Full infinite unit coefficients and full modular reflection fail; finite endpoint matches do not restore them. Their local events are not finite all-real thresholds |
| Finite-prime-compatible square controls | Square mode equations and selected arithmetic identities | Complete normalized reflection fails; no universal threshold claim is imported |
| Reflected smooth / positive-primitive controls | Physical reflection, Kelvin covariance and generic positive primitive | Unchanged square arithmetic fails. These still test any inference using only the physical positive source and the generic Wronskian |
| Euler-factor threshold controls | Their own even positive source and heat evolution | Fixed canonical source/conductor and this all-unit lattice realization are changed |
| Finite-profile atomic or compact-source controls | Generic physical heat and boundary identities on their domains | Canonical smooth complete square source, full profile growth and eventual threshold simplicity are absent |

Full coefficients and reflection distinguish theta, but (6) alone does not use that distinction. Even on the unchanged canonical source, (12), (22), (24) and (28) obstruct the specific simplifications tested here. No control is asserted to falsify an actually proved theta-specific estimate.

The [exact checker][checker] verifies the operator coefficients and source identities with rational polynomial arithmetic, including the commutator sign, the factorization in (6), the lower-boundary coefficients, and the transformed-prefactor coefficients in (20). Its [small record][record] also records a replay of Note01's exact (+27,-27) Gaussian cancellation. Those computations resolve algebraic sign/factor risks; they do not prove convergence, the limit (27), or any theta exclusion. Their proofs are above. The [self-assessment][review] is by the same assistant and is not independent review.

## 9. RTC decision and continuation

The first bounded RTC-03 contract is met by a **precise obstruction for the selected construction**. Retain the exact two-channel circle system as a diagnostic. Stop attempts to obtain a homogeneous physical boundary theorem by commuting \(P_t\) through \(A_\lambda^{-1}\), truncating to a finite invariant transverse linear state, or replacing the physical point current by its unweighted circle average without a comparison. Each omitted term or false boundary implication is now identified.

Broader RTC-03 remains open. Nonlinear modular closures and a signed, source-correlated transverse comparison are outside the proved obstruction, but no concrete such mechanism is constructed here. RTC-04 still has no homogeneous characteristic candidate. RTC-06 remains deferred: equations (16)–(17) specify an exact cost but no evidence yet makes a numerical estimate of it worthwhile.

The next preferred bounded alternative is RTC-05: choose a physical time-frequency region and a source-derived deformation or current, then calculate its **complete** boundary degree, including both time faces, both frequency walls, and any zeros or tangencies along the deformation. Its return must add a source-proved restriction or document a selected deformation's exact failure; re-expressing the existing physical winding is not a gain. Full circle normalization and Kelvin reflection alone provide no such degree restriction. All-height and all-multiplicity threshold transfer remain unpaid.

The [progress register][progress] and [overview][overview] record these states. This is an incremental research return, not an investigation closeout or manuscript milestone; no snapshot or commit has been created.

[initial]: 01_RADIAL_THETA_GEOMETRY_AND_COLLISION_MECHANISMS_20261027.md
[handoff]: 02_CONTINUATION_AND_SESSION_HANDOFF_20261027.md
[overview]: ../research-overview/01_RADIAL_THETA_COLLISION_RESEARCH_OVERVIEW_20261027.md
[progress]: ../research-progress/01_RADIAL_THETA_COLLISION_RESEARCH_PROGRESS_20261027.md
[review]: ../reviews/02_CIRCLE_HEAT_LIFT_SELF_ASSESSMENT_20261027.md
[checker]: ../numerics/02_check_circle_heat_lift_20261027.py
[record]: ../numerics/02_CIRCLE_HEAT_LIFT_CHECKS_20261027.json
[refs]: ../references/01_CIRCLE_HEAT_AND_JACOBI_NORMALIZATIONS_20261027.md
[results]: ../../../../result-summaries/README.md
[arithmetic]: ../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[geometry]: ../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[oldtransverse]: ../../../investigations-3/11_arithmetic_collision_rigidity/symmetries/06_hodge_and_transverse_geometry/notes/01_TRANSVERSE_OBSERVATION_AND_FINITE_JET_OBSTRUCTIONS_20261018.md
[oldcurrent]: ../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/09_JOINT_SOURCE_CURRENT_AND_POLYNOMIAL_OBSTRUCTION_20261015.md

# Conservation laws and Lagrangian evolution of a spatial heat contour

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**. Derivations were checked by separate agents of the same model; no specialist or formal verification is claimed.

**Status: exact conservation laws, Noether actions and material-contour equations; a conditional finite graph estimate; canonical deformation and collision bounds remain open. No new simplicity bound.**

The author's intended contour is spatial:

\[
 \Gamma_t:\quad z=T+i\epsilon(T,t),\qquad H_t=-H_{zz}.
\]

Here T is real spatial height in the repository's H normalization; t is heat time, and H(0,z) is the prescribed multiple of xi. This is distinct from the earlier backward-time face. The question is which natural conservation law should determine its motion, and whether the conserved hierarchy controls the contour despite local zero flux. Following the author's clarification, **no smoothing or restoring term is assumed in the proposed first model**. Stochastic language describes a possible statistical approximation to the deterministic canonical flow; it is not a new random source.

This continues the [research overview](../research-overview/02_ANALYTIC_RH_TO_SIMPLICITY_PROGRAM_20261023.md), the [book's moving windows and current](../../manuscript/book.tex), and [Note 07, Section 3](07_NONREAL_WINDOW_TRANSPORT_AND_REGULARIZED_CURRENT_20261023.md). Follow the [result index](../../../../../result-summaries/README.md), [avoid index](../../../../../avoid/README.md), [classification rule](../../../../../avoid/01_restating_the_target.md), [scope rule](../../../../../avoid/07_scoped_exclusions_read_as_universal.md), and [collision controls](../../../../../result-summaries/12_collision_controls_and_screening.md). The results below concern a chosen boundary dynamics, not an acquired theta estimate. [Review 07](../reviews/07_SPATIAL_CONTOUR_EVOLUTION_REVIEW_20261023.md) records the checks and limitations.

## 1. Start with the conservation law supplied by heat

The simplest local law is already present:

\[
 \boxed{H_t+\partial_z J_H=0,\qquad J_H=H_z.} \tag{H1}
\]

For a material curve z=Z(a,t) with Z_t=u(t,Z),

\[
 \partial_t[H(t,Z)Z_a]
 =[H_t+\partial_z(Hu)](t,Z)Z_a.
\]

Choosing the literal heat flux, Hu=J_H, gives

\[
 \boxed{u_H=\frac{H_z}{H},\qquad
 H(t,Z(a,t))Z_a(a,t)=H(t_0,Z(a,t_0))Z_a(a,t_0).} \tag{H2}
\]

This preserves **every material subarc integral** of H dz wherever the flow exists and H is nonzero. Adding a spatially constant current C(t) to J_H gives another such law; choosing C=0 fixes that freedom. Preserving only one total integral is weaker: on an arbitrary moving open contour,

\[
 \frac d{dt}\int_{\Gamma_t}H\,dz=[H\dot z-H_z]_{\rm endpoints}. \tag{H3}
\]

Interior deformation cancels by holomorphy. In particular, the closed-contour integral of the entire H is zero and supplies no collision information. The load-bearing condition in (H2) is local material preservation, rather than conservation of that vacuous closed integral.

For the author's graph Z(T,t)=T+i epsilon(T,t), the resulting equation is

\[
 \boxed{\epsilon_t+\Re\!\left(\frac{H_z}{H}\right)\epsilon_T
 =\Im\!\left(\frac{H_z}{H}\right),\quad z=T+i\epsilon(T,t).} \tag{H4}
\]

It can also be written as a one-dimensional conservation law. Put g=H(t,Z)(1+i epsilon_T). For any moving graph,

\[
 g_t+\partial_T[H_z(t,Z)-i\epsilon_tH(t,Z)]=0.
\]

Under (H4), its flux is (Re u_H)g. Integrals over material height endpoints are conserved; fixed height endpoints retain this flux. No smoothing, stochastic assumption or chosen compliance parameter is needed.

### A positive conserved density and primitive coordinates

This is not only conservation of a complex quantity. Holomorphy and heat give

\[
 \boxed{\partial_t|H|^2+
 \operatorname{div}_{(x,y)}(H_z\overline H)=0.} \tag{H5}
\]

The complex current is read as a planar vector. Indeed its divergence is 2 Re(H_zz conjugate(H)), canceling the time derivative. Its current-to-density velocity is again H_z/H. Thus compact material domains preserve integral |H|^2 dA. Equation (H2) also preserves the weighted length integral |H||dz| and the metric |H|^2|dz|^2 along material segments. Weighted enclosed-area conservation needs the velocity only on a regular swept boundary tube, by Reynolds transport and (H5); interior zeros may remain. For ordinary length, a lower bound |H|>=m>0 on the boundary is still needed to infer length<=conserved weighted length/m. These positive quantities vanish or degenerate at zeros; they are not zero-counting measures and need not have finite whole-plane integrals.

For canonical even H define the entire odd primitive

\[
 P(t,z)=\int_0^zH(t,w)dw,\qquad P_z=H,\quad P_t=-H_z.
\]

The last identity uses H_z(t,0)=0. Equation (H2) is equivalently

\[
 \boxed{P(t,Z(a,t))=P(t_0,Z(a,t_0)).} \tag{H6}
\]

There is a second, directly geometric Noether formulation. The target-plane action

\[
 \mathscr S_P[Z]=\frac12\int\Im(\overline{P(t,Z)}\,dP(t,Z))
\]

has curvature |H|^2 dx wedge dy+Im(H_z conjugate H)dt wedge dx-Re(H_z conjugate H)dt wedge dy. Its stationary paths give Zdot=H_z/H where H≠0. In target coordinates P=X+iY the action is one-half integral (X dY-Y dX). Translations of X and Y change it by endpoint terms; their Noether charges are -Y and X. Thus Re P and Im P are conserved. This is a first-order stationary action, not a positive energy-minimization principle, and it restates the inverse-primitive transport exactly.

For a general non-even field choose the time-dependent additive constant in P so P_t=-H_z. This provides a natural construction: hold a target contour in the P-plane fixed and continue its inverse image. A local inverse requires H≠0. Global continuation additionally requires branch, endpoint and finite-region properness/escape control; the absence of critical values on a target curve alone is not a global inverse theorem for an entire function.

For the particular target Im P=c, a graph patch satisfies

\[
 \epsilon_T=-\frac{\Im H}{\Re H},\qquad
 \epsilon_t=\frac{\Im H_z}{\Re H}. \tag{H7}
\]

These require Re H≠0, a stronger condition than local inverse regularity. A material contour may remain regular while failing to be a graph over height.

### The Noether and Burgers connections

On a real spatial interval the doubled heat-adjoint action is

\[
 \mathscr S[H,\psi]=\int(\psi H_t-\psi_xH_x)\,dx\,dt.
\]

Compactly supported variations give H_t+H_xx=0 and psi_t-psi_xx=0. The exact scaling symmetry (H,psi) mapsto (exp(a)H,exp(-a)psi) has Noether density psi H and flux psi H_x-psi_x H. Directly,

\[
 \partial_t(\psi H)+\partial_x(\psi H_x-\psi_xH)
 =\psi(H_t+H_{xx})+H(\psi_t-\psi_{xx}). \tag{H8}
\]

This supplies the variational connection explicitly; the heat equation alone is not silently assumed to arise from an ordinary single-field conservative action. For complex fields one may use the real and imaginary variations of the corresponding real action. Holomorphic continuation gives the same local identity with z derivatives.

The choice psi=1 recovers (H1). More generally an adjoint heat solution gives the conserved form psi H dz and the material velocity

\[
 u_\psi=\frac{\psi H_z-\psi_zH}{\psi H}
 =\frac{H_z}{H}-\frac{\psi_z}{\psi}. \tag{H9}
\]

For example, the adjoint heat polynomials exp(t partial_z^2)z^n generate an elementary family:

\[
 1,\quad z,\quad z^2+2t,\quad z^3+6tz,\quad z^4+12tz^2+12t^2,\ldots.
\]

For the canonical source H(t,x)=integral_0^infinity exp(tu^2)Phi(u)cos(xu)du, the full even frequency profile exp(tu^2)Phi(u) is Schwartz, uniformly on compact time intervals. Fourier inversion and integration by parts justify the whole-real-line polynomial invariants. With Fourier convention Hhat_t(xi)=integral_R exp(-i xi x)H(t,x)dx,

\[
 e^{-t\xi^2}\widehat H_t(\xi)=\pi\Phi(\xi),\qquad \xi\in\mathbb R,
\]
\[
 I_n(t)=\int_{\mathbb R}(e^{t\partial_x^2}x^n)H(t,x)dx
 =\pi i^n\Phi^{(n)}(0).
\]

These give a complete continuum of Fourier invariants and an infinite polynomial hierarchy; odd polynomial values vanish by evenness. The continuum determines H by Fourier inversion. Completeness of polynomial moments for arbitrary Schwartz data is not asserted; it requires additional analyticity/determinacy information. This makes the rigidity precise while locating the remaining task: obtain useful contour or first-jet estimates from the particular canonical conserved values. The hierarchy is not a general ban on collisions. Their integrated invariants require paid endpoints; different densities generally prescribe different local material velocities. An infinite collection of generic conservation laws is not itself new theta arithmetic.

These adjoint and Fourier invariants have explicit time dependence in their weights. They express the exactly solvable linear heat evolution; their completeness is a uniqueness statement, not a new theta inequality or a proof of autonomous Hamiltonian integrability. In particular, no Lax isospectral structure, Poisson commutation, coercive Hamiltonian or independent nonlinear hierarchy has been established for the contour. The useful next step is an estimate extracted from the specific conserved data, rather than counting how many identities are available.

There is a useful distinction between a hierarchy of conserved field integrals and simultaneous local material preservation on one contour. Suppose the same velocity preserves H dz and every psi H dz. Dividing their material pullback identities where H is nonzero gives

\[
 \psi_t+u\psi_z=0.
\]

The adjoint psi=z forces u=0, whereas psi=z^2+2t then forces 2=0. Thus no common flow preserves the full adjoint hierarchy on every material subarc. This conclusion allows arbitrary spatially constant current gauges. Preserving whole-line integrals, with vanishing endpoint currents, is fully compatible with the hierarchy and is much weaker. The hierarchy constrains the field supplying the contour velocity; it is not an infinite list of independent local boundary conditions on epsilon.

Setting p=H_z/H also gives

\[
 \boxed{p_t+\partial_z(p_z+p^2)=0.} \tag{H10}
\]

Thus U=2p satisfies U_t+U U_z=-U_zz: the Cole–Hopf relation with the repository's backward-heat sign. The H dz material velocity is p, not the factor 2p appearing in the Burgers advection term. Conserving p dz locally instead selects (p_z+p^2)/p=H_zz/H_z.

The primary citation list now includes [Noether's original theorem in Tavel's translation](https://arxiv.org/abs/physics/0503066v3), [Cole](https://doi.org/10.1090/qam/42889), [Hopf](https://doi.org/10.1002/cpa.3160030302), and the [adjoint-formulation discussion of Anco, Section 2.2](https://arxiv.org/html/1611.02330v3). Ibragimov's 2007 conservation paper and distinct 2006 article on the KdV hierarchy are cataloged separately as background; the archived ALGA volume contains the latter. These identities are proved above; no general completeness claim about the conservation laws is imported. The [catalog](../../references/README.md) records accessible copies, versions and inspection scope.

### A decisive regularity test

The stationary heat solution H=z gives u_H=1/z and Z(t)^2=Z(0)^2+2(t-t_0). A starting point Z(0)=i y_0 reaches a **simple** zero in finite forward time y_0^2/2. Thus conservation of H dz does not ensure a regular flow, even without a multiple-zero event.

For the even collision control H=z^2-2t, P=z^3/3-2tz. Its critical values are real for t>0; for t<0 they are plus/minus i(4sqrt(2)/3)|t|^(3/2). A target line Im P=c>0 meets a critical value at t=-(3c/(4sqrt(2)))^(2/3). This concerns the full level and the inverse branch carrying that critical point, not every selected component of the preimage. Meanwhile a regular outer contour at t=0 can persist while the double zero lies inside it. This distinguishes contour regularity from exclusion of the event.

A decaying collision control shows that the whole-line hierarchy itself does not prevent this. For a>0 and d=1-4at>0 let

\[
 H_a(t,z)=\frac{z^2-2td}{d^{5/2}}\exp(-az^2/d).
\]

Indeed G_a=d^(-1/2)exp(-az^2/d) solves backward heat and H_a=-partial_a G_a, so H_a does too. It is even, real type, entire in z, and Schwartz on the real axis uniformly on compact time intervals below 1/(4a). Hence all of the Fourier and polynomial invariants above exist and are conserved. Nevertheless its zeros are plus/minus sqrt(2td), with an ordinary double zero at t=z=0. This proves the scoped point even with the decay needed for all the integrations. Its Fourier constants differ from the theta constants; it is not a counterexample to a theta-specific estimate.

Positivity of the Fourier profile can also be retained in a separate elementary control. For a,b>0,

\[
 F(t,z)=d^{-1/2}e^{-az^2/d}
 \left[1+e^{tb^2/d}\cos(bz/d)\right],\qquad d=1-4at>0.
\]

Evolving each Gaussian exponential in F(0,z)=e^(-az^2)(1+cos(bz)) verifies backward heat. Its initial Fourier profile is

\[
 \sqrt{\pi/a}\left[e^{-\xi^2/(4a)}+
 \tfrac12e^{-(\xi-b)^2/(4a)}+
 \tfrac12e^{-(\xi+b)^2/(4a)}\right]>0.
\]

For 0<t<1/(4a), the zero equation is cos(bz/d)=-exp(-tb^2/d), whose roots are all real and simple. At t=0, each odd multiple of pi/b is a double zero. Thus positive even Schwartz source, a complete conserved hierarchy and an interval of all-real positive-time zeros still permit endpoint doubles. The source is Gaussian rather than the complete theta source, and the time interval is bounded above; no claim about a global theta-like heat family is made. The stronger registered controls retain their separate preservation lists.

The primary research choice is now **(H1)–(H6)**: the heat law, its material form, its positive density and its primitive coordinates agree without an added smoothing term. The next required input is canonical control of the inverse primitive and contour strain, especially near small H. The flux models and physical-jet action below are comparisons that preserve different quantities.


## 2. The exact material equation

Write v=v_1+i v_2. A spatial graph carried by a planar velocity v satisfies

\[
 \boxed{\epsilon_t+v_1(t,T,\epsilon)\epsilon_T=v_2(t,T,\epsilon).} \tag{1}
\]

Indeed, along a moving point, dT/dt=v_1 and d\epsilon/dt=v_2. For the region below the graph, the outward relative speed, multiplied by the positive factor sqrt(1+epsilon_T^2), is

\[
 v_2-v_1\epsilon_T-\epsilon_t. \tag{2}
\]

At a simple zero the heat equation gives v=H_zz/H_z. Extending that ratio away from zeros is one natural material choice: it transports the complex value of H. It can be singular where H_z=0, and it does not close as an equation involving only epsilon and its derivatives. The heat field supplies the velocity.

This distinction is real: the heat evolutions from initial polynomials z and z^m have the same unit amplitude contour at t=0, but at z=1 their outward material speeds are 0 and m-1. Contour shape alone cannot determine that speed across this class. This is not a prohibition on a field-dependent contour law.

The generic zero-branch identity appears in [Papanicolaou–Kallitsi–Smyrlis, Section 4.1, (4.38)–(4.40)](https://ejde.math.txstate.edu/Volumes/2021/44/papanicolaou.pdf); their heat sign is opposite. Their product expansions have additional order hypotheses, which are not imported here. The article and checked passages are in the [reference catalog](../../references/README.md).

For analytic reference levels, the book already supplies a more robust observable: psi=chi(G) has the denominator-free numerator Re{Dchi(G)(G_t H_z-G_z H_t) conjugate(H_z)}. It remains defined when a level set loses its graph representation. The projective H/H_z flow from the earlier collar note is a different off-zero transport; its particular three-form cancellation should not be transferred to H-level walls.

## 3. A flux-responsive law with finite compliance

For fixed rho>0 use the existing smooth zero density and planar current

\[
 k_\rho(w)=\frac{\rho^2}{\pi(|w|^2+\rho^2)^2},\qquad
 \mu_\rho=k_\rho(H)|H_z|^2,\qquad
 j_\rho=k_\rho(H)H_{zz}\overline{H_z}=j_1+i j_2.
\]

They obey the exact continuity equation

\[
 \partial_t\mu_\rho+\partial_T j_1+\partial_y j_2=0. \tag{3}
\]

One proof pulls back the closed target-plane two-form k_rho(w) dRe w wedge dIm w by H(t,z). Its spatial coefficient is mu_rho and its time-spatial coefficients give j_rho. This proof extends through H_z=0 without division.

The current crossing the moving upper graph, per unit horizontal height, is

\[
 J_\rho=j_2-j_1\epsilon_T-\mu_\rho\epsilon_t. \tag{4}
\]

Positive J_rho is outward. A simple finite-response law is lambda epsilon_t=J_rho, with a fixed lambda>0 having the units of spatial density. Thus

\[
 \boxed{(\lambda+\mu_\rho)\epsilon_t+j_1\epsilon_T=j_2,}
 \qquad
 \boxed{\epsilon_t+u_1\epsilon_T=u_2,
 \quad u=\frac{j_\rho}{\lambda+\mu_\rho}.} \tag{5}
\]

All field quantities are evaluated at (t,T+i epsilon). Outward flux moves the upper boundary upward; inward flux moves it downward. Lambda is a chosen compliance parameter, not supplied uniquely by the heat equation. There is no curvature penalty, smoothing term, or restoring potential in (5). Choosing lambda very large suppresses motion by construction and must not be advertised as evidence of canonical cancellation.

Equation (5) has another exact interpretation. The augmented density lambda+mu_rho obeys (3) with the same current, and u is its material velocity. Consequently (5) preserves augmented mass in a fully material domain. It is a conservative flow with a uniform background density, not merely an analogy to one. At fixed positive rho and lambda, u is smooth on every compact region where H is analytic, including multiple zeros. This regularity is not asserted uniformly as rho decreases to zero.

For real-type H, j_2(t,T,0)=0, so the real axis is invariant under u. A positive-height trajectory cannot cross it during a bounded smooth flow: local Lipschitz continuity gives |u_2(t,T,y)|<=L(t)|y| and the usual exponential lower bound for positive y. The upper curve can nevertheless cease to be a graph over T. Containment in the chosen spatial buffer is a separate obligation.

At large height, a fixed raw-H regulator can suppress the current merely because the xi carrier is small. Before claiming useful stability, fix the normalization and mobility independently of the desired conclusion. If f=H/B with a specified nonvanishing analytic carrier, use the exact current

\[
 \mu_\rho^B=k_\rho(f)|f_z|^2,\qquad
 j_\rho^B=-k_\rho(f)f_t\overline{f_z},
\]
\[
 -f_t=f_{zz}+2\frac{B_z}{B}f_z+
 \frac{B_{zz}+B_t}{B}f.
\]

The same continuity proof applies, with every carrier term retained. For the reflected-wall and zero-bottom-flux formulas below, also require B to be real type; otherwise retain the actual bottom current. At a simple zero -f_t/f_z is the actual root velocity. The finite-regulator off-zero dynamics depends on this prescribed normalization. Making rho depend on height or time also introduces extra continuity terms; equations (3)–(11) use fixed rho. No regulator-removal theorem for these adaptive boundaries is asserted.

## 4. Conservation can control the mean without smoothing

On a fixed finite height band [A,B], let

\[
 M_\rho(t)=\int_A^B\int_0^{\epsilon(T,t)}\mu_\rho(t,T,y)\,dy\,dT,
 \qquad \bar\epsilon(t)=\frac1{B-A}\int_A^B\epsilon(T,t)\,dT.
\]

The complete signed flux through the two fixed ends is

\[
 E_{\rm end}(t)=
 \int_0^{\epsilon(B,t)}j_1(t,B,y)\,dy
 -\int_0^{\epsilon(A,t)}j_1(t,A,y)\,dy.
\]

More locally, let m(T,t)=integral_0^epsilon mu_rho dy and q(T,t)=integral_0^epsilon j_1 dy. The bottom flux vanishes by reality, and the graph law gives

\[
 \boxed{\partial_t(m+\lambda\epsilon)+\partial_T q=0.} \tag{6a}
\]

Indeed m_t=-q_T-J_rho; substitute J_rho=lambda epsilon_t. Thus a smooth height average is driven by the corresponding horizontal-current divergence, with exposed end terms retained. Reynolds transport and (3) give

\[
 M_\rho'=-\int_A^B J_\rho\,dT-E_{\rm end}.
\]

Using (5),

\[
 \boxed{\frac d{dt}\{M_\rho+\lambda(B-A)\bar\epsilon\}
 =-E_{\rm end}.} \tag{6}
\]

Nonnegativity alone already yields the one-sided estimate

\[
 \bar\epsilon(t)\le\bar\epsilon(t_0)+
 \frac{M_\rho(t_0)+\int_{t_0}^t[-E_{\rm end}(s)]_+ds}
 {\lambda(B-A)}.
\]

This pays the end flux explicitly; the canonical field is not assumed periodic. If the domain is closed or its ends are material, use the corresponding complete mass balance instead. For fixed ends and an independently established bound 0<=M_rho(s)<=M_* throughout the interval,

\[
 |\bar\epsilon(t)-\bar\epsilon(t_0)|
 \le\frac{M_*+|\int_{t_0}^t E_{\rm end}(s)ds|}
 {\lambda(B-A)}. \tag{7}
\]

The difference of two nonnegative masses bounded by M_* costs M_*, not 2M_*. A finite compact source bound can furnish a finite M_*; no favorable growing-height size or uniform rho-limit is claimed here. Equation (7) is a concrete mechanism for maintaining the mean height without adding smoothing. It controls neither pointwise excursions nor slopes, and a moving reference mean would contribute its own derivative.

## 5. Shape persistence requires strain information

Let Phi be the flow of u on a buffer containing all trajectories of the chosen initial contour. Suppose the initial upper boundary is flat and put

\[
 K(t)=\int_{t_0}^t\|D_z u(s,\cdot)\|_{\rm op,\infty}\,ds,
 \qquad t\ge t_0.
\]

The variational equation D Phi'=Du D Phi and Gronwall give

\[
 \|D\Phi-I\|\le e^{K(t)}-1.
\]

Hence, if K(t)<log 2, the horizontal derivative with respect to the initial height label is at least 2-e^K>0, and the curve remains a graph on its advected horizontal interval, with

\[
 \boxed{\|\epsilon_T\|_\infty
 \le\frac{e^{K(t)}-1}{2-e^{K(t)}}.} \tag{8}
\]

For an initial graph with slope bounded by P, replace the denominator condition by (e^K-1)sqrt(1+P^2)<1; the corresponding slope bound is [P+(e^K-1)sqrt(1+P^2)]/[1-(e^K-1)sqrt(1+P^2)]. This follows by applying D Phi-I to the initial tangent (1,p).

These are elementary finite-flow estimates, not new theta strain bounds. They show that smoothing is not logically required even for graph persistence over a finite interval. They can be crude because the norm inside K discards cancellations. A stronger analysis could estimate the actual tangent flow instead. On a graph the exact slope equation along dT/dt=u_1 is

\[
 \frac{dp}{dt}=\partial_T u_2+
 (\partial_y u_2-\partial_T u_1)p-(\partial_y u_1)p^2. \tag{9}
\]

It displays the shear and strain that an averaging argument must control. No uniform long-time smoothness or global graph theorem follows from (6).

There is also a direct finite-regulator displacement estimate. With p=epsilon_T, let

\[
 \mathcal B_\rho=\int_{t_0}^{t_1}\int_A^B
 (1+p^2)k_\rho(H)|H_{zz}|^2\,dT\,dt,
\]

on a common height band covered by the graphs. Since |j|^2=mu_rho k_rho(H)|H_zz|^2 and mu_rho/(lambda+mu_rho)^2<=1/(4lambda),

\[
 \int\!\int|\epsilon_t|^2\le\frac{\mathcal B_\rho}{4\lambda},\qquad
 \left(\frac1{B-A}\int_A^B|\epsilon(T,t_1)-\epsilon(T,t_0)|^2dT\right)^{1/2}
 \le\sqrt{\frac{(t_1-t_0)\mathcal B_\rho}{4\lambda(B-A)}}. \tag{9a}
\]

This is a useful named input for the canonical comparison, not an acquired small-value bound. For f=H/B replace H_zz by -f_t and use its complete carrier terms. The slope, small-value weight, regulator and moving trace cannot be dropped when estimating it.

## 6. What stochastic averaging would need to establish

The canonical H and the chosen boundary dynamics are deterministic. One possible statistical ensemble chooses a height window from a prescribed distribution, then follows its boundary. Any resulting centering, scaling, covariance and stationarity approximation must be justified for that ensemble. In particular, Eulerian statistics at fixed points do not automatically give the Lagrangian statistics along an adaptively moving boundary.

For a centered real-valued square-integrable fluctuation F along a trajectory, the exact identity is

\[
 \operatorname{Var}\!\left(\int_0^t F(s)ds\right)
 =\int_0^t\int_0^t\operatorname{Cov}(F(s),F(r))\,ds\,dr. \tag{10}
\]

If F is stationary with covariance C, this becomes 2 integral_0^t (t-s)C(s)ds. Under absolute integrability, its ratio to t tends to 2 integral_0^infinity C(s)ds. A positive value gives displacement variance growing linearly, although the time-average velocity tends to zero in mean square. Thus zero mean or short correlation alone does not produce bounded wandering. Cancellation with a bounded integrated fluctuation, sufficiently compensating correlations, or another conservation mechanism could do better. Zero integrated covariance by itself only removes the linear term; it does not establish bounded variance. None of these statistical properties has been proved here for theta.

There is a further distinction for the simplicity consumer. By (5), the upper-wall regularized inward current is

\[
 \int\!\int[-J_\rho]_+\,dT\,dt
 =\lambda\int\!\int[-\epsilon_t]_+\,dT\,dt. \tag{11}
\]

Its total variation can be large while the signed change in mean height is small. Therefore a well-maintained average contour does not on its own bound repeated entries. The book's earlier-nonreal-plus-inward-flux resource needs the one-sided quantity and the earlier population. The rho limit, real-axis excision, height ends, endpoint coverage and approximation errors remain part of that transfer. In particular, the existing fixed-field current limit cannot simply be applied to a rho-dependent family of windows with no uniform bounds.

## 7. Controls on the regularized comparison

For H=z^2-2t an upper nonreal zero moves with speed -1/y; for H=z^3-6tz the upper zero moves with speed -3/y. The trial wall y^2=e_0^2-2t tracks the quadratic scale, but the cubic pair enters it at t=-e_0^2/4. The relative upper crossing speed is -2/y. Moving the wall can trade entry against earlier population; the conservation identity retains both. The regularized law (5) remains smooth even at these events and does not exclude them. Moreover, the quadratic has j_2=-4k_rho(H)y above the real axis: a systematic inward drift, rather than automatically mean-zero buffeting.

The Euler-factor, weighted-square, reflected and positive-primitive controls also satisfy the generic current and boundary identities. They fail different canonical-source premises: unchanged arithmetic coefficients, full reflection together with square support, or the complete normalized theta expansion, as recorded in the linked control register. No new theta inequality is asserted that rejects these controls. An averaging argument using only their shared heat or source-shape properties would therefore need further input.

For the regularized comparison, the immediate question is precise: for the **unsmoothed spatial law (5)**, can complete canonical-source information control the signed accumulated end flux and mean height, the actual tangent-flow strain, and the one-sided relative current on a useful height/time scale? Start with a finite prescribed band and fixed regulator, retain the exact coupled numerators, and compare with an analytic reference using the book's carrier and defect terms. Only introduce a stochastic approximation after identifying the corresponding covariance from this deterministic evolution. Add smoothing only if an identified shape instability warrants it and its changed flux is paid. The finite identities above make that comparison concrete; the required canonical estimates and any simplicity consequence remain open.

## 8. The physical topological connection and a genuine path action

The author's original topological observable is the physical first-jet Chern–Hopf form, not a spatial zero-counting line integral. Put G=(H,H_z), E=|H|^2+|H_z|^2, and, on G≠0,

\[
 \alpha_G=\frac1{2\pi}\frac{\Im(G^\dagger dG)}{E}.
\]

The repository's normalized physical three-form is C=alpha_G wedge d alpha_G. This agrees with the [native chart formula](../../../brainstorm/notes/02_MOVING_COLLAR_MATERIAL_ENERGY_AND_HEIGHT_DEPENDENT_EPSILON_20261023.md): when G=b(q,1), it is d arg b wedge omega(q)/(4pi^2). Its integral is over a complete three-dimensional boundary in complex time-space. That degree is invariant under homotopies with G nonzero on the swept boundaries; joint zeros inside are allowed and are what it counts. This invariance alone does not choose the contour's velocity.

There is nevertheless a natural real-time path action built from its connection. Define

\[
 L=H_z^2-HH_{zz},\quad N=H_zH_{zz}-HH_{zzz},\qquad
 \mu_G=\frac{|L|^2}{\pi E^2},\quad j_G=\frac{N\overline L}{\pi E^2}.
\]

With x=Re z,

\[
 d\alpha_G=\mu_G\,dx\wedge dy
 +(\Im j_G)dt\wedge dx-(\Re j_G)dt\wedge dy. \tag{T1}
\]

To verify, write q=H/H_z in a regular chart. Its derivatives are q_z=L/H_z^2, q_t=-N/H_z^2, and the curvature is pi^(-1)(1+|q|^2)^(-2)dRe q wedge dIm q. The displayed polynomial ratios extend through H_z=0 whenever G≠0. In particular mu_G is **projective curvature density**, not the density counting zeros of H.

For lambda>=0 set

\[
 \mathcal A=\frac\lambda2(x\,dy-y\,dx)+\alpha_G,
 \qquad \mathscr S_{\rm path}[Z]=\int_{(t,Z(t))}\mathcal A. \tag{T2}
\]

Use the full spacetime form, including its dt component. Fixed-endpoint variations give i_V dA=0 for V=partial_t+u_1 partial_x+u_2 partial_y, equivalently

\[
 \boxed{u=\frac{j_G}{\lambda+\mu_G}.} \tag{T3}
\]

This is a first-order stationary action, linear in velocity, not a positive minimization principle or a probability law. Cartan's formula gives Lie_V A=d(A(V)). Hence every complete closed material contour conserves its spatial circulation integral A. Open arcs retain the endpoint terms. At lambda=0 and L≠0, (T3) is exactly the earlier projective flow u_q=N/L, preserving q. Positive lambda removes its L=0 chart singularity when E>0, but not a joint-zero singularity E=0.

This circulation is generally noninteger. For H=z and the circle |z|=R, integral alpha_G=R^2/(1+R^2), while the argument-principle count is one. A regular outer loop can preserve this circulation with an interior joint-zero event; any use of Stokes across that event needs excisions. Conservation of circulation is not a replacement for the complete Chern–Hopf charge calculation.

The scalar current of Sections 3–7 has exactly the parallel action

\[
 \mathcal A_\rho=\frac\lambda2(x\,dy-y\,dx)
 +\frac1{2\pi}\frac{\Im(\overline H\,dH)}{|H|^2+\rho^2}.
\]

Its curvature is (lambda+mu_rho)dx wedge dy+j_2 dt wedge dx-j_1 dt wedge dy. Thus its Euler–Lagrange equation is the same u=j_rho/(lambda+mu_rho) already studied. On a complete material boundary, its circulation is lambda times area plus the enclosed regularized zero mass. At fixed rho this is not an integer zero count and may remain conserved while an actual zero crosses the contour. The physical-jet action has a direct relationship to the original topological connection; the scalar action is smoother but changes the observable. Neither requires an added smoothing term.

## 9. Choice of conservation law for the next step

| Preserved local object | Natural zero-additive-current velocity | Main limitation |
| --- | --- | --- |
| H dz; its positive metric and area density | H_z/H | Degenerates at every zero; weighted geometry needs a lower bound to control ordinary geometry. |
| (H_z/H) dz, and H itself | H_zz/H_z | Singular at critical points; its closed integer count permits interior collisions. |
| Physical-jet connection circulation | N/L, or j_G/(lambda+mu_G) | Exact first-order action; G=0 remains singular, and circulation is not the full collision charge. |
| Regularized zero circulation plus area | j_rho/(lambda+mu_rho) | Smooth at fixed positive parameters, but adaptive regulator limits and source normalization need control. |

The current primary choice is **H dz**, because its conservation, positive-density interpretation, primitive-coordinate dynamics, adjoint Noether formulation and Cole–Hopf equation all follow directly from the original heat equation. The physical-jet action is the most direct comparison for the original topological observable. This is a research selection, not a proof that either dominates all other laws.

The next analytic task is to transport a prescribed compact initial contour by a conserved primitive image and estimate its actual tangent flow and distance from critical values using complete canonical-source information. The infinite adjoint/Fourier hierarchy should be used with its actual theta values, together with the boundary terms. A global constant Im P level is not automatically compatible with a bounded-width high-height contour: already at t=0 the xi carrier decays on bounded strips, so Im P(T+iy)=integral_0^y Re H(T+iv)dv tends to zero uniformly for bounded y. Use the actual initial image curve rather than assuming a fixed nonzero level at every height.

The exact laws and actions here are generic heat/analytic geometry. The registered collision controls retain them with their own conserved data; the canonical values, and estimates that use them, must supply any new restriction. No new simplicity proportion, endpoint exclusion, uniform graph theorem or stochastic cancellation has yet been established.

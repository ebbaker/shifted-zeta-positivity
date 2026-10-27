# Modular Wronskian weight and the canonical sign obstruction

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Research conversation **Begin radial theta collision study**, thread `01a17e9c-bfd5-7782-a76f-b2a2eaa82417`, Investigation05 chat0001.

**Status: second bounded RTC-03 return; exact identities and a scoped sign obstruction proved in-note, with same-assistant checking.** The proposed modular multiplier leaves the complete integrated Wronskian equal to the original boundary residual. More strongly, for the unchanged canonical source and every sufficiently large positive spectral parameter, its actual integrand takes both signs, uniformly for physical time in [0,1/2]. A rational source-constant enclosure proves the negative endpoint coefficient. No numerical frequency onset, canonical collision exclusion, new zero-free region, Newman improvement or endpoint simplicity result is obtained.

This closes the proposed fixed multiplier as an automatic sign argument or an everywhere nonnegative integrand on that time slab and all positive frequencies. It does not exclude estimates using signed cancellation, a different current, or a restricted event-conditioned argument. The [result index][results], [theta identities][arithmetic], [control register][controls] and [avoid index][avoid] apply, particularly [target restatements][a01], [shape-only controls][a02], [coupled terms][a12] and [scoped exclusions][a07].

## 1. Physical equation and the chosen weight

Retain [Note01][initial]'s complete source and selected Volterra response:

\[
g_t(x)=4e^{tx^2/4}\Phi(x/2),\qquad
Y(t,x;\lambda)=\int_x^\infty
\frac{\sin(\sqrt\lambda(s-x))}{\sqrt\lambda}g_t(s)\,ds,
\quad x\ge0,\quad \lambda=a^2/4>0.
\tag{1}
\]

Put Z=Y_lambda and B=Y_x(t,0;lambda)=-8H(t,2sqrt(lambda)). For each finite real t the complete source is positive, even and smooth, and every derivative has the tails needed below. Then

\[
Y_{xx}+\lambda Y=g_t,\qquad
Z_{xx}+\lambda Z=-Y,\qquad
W=YZ_x-Y_xZ,\qquad W_x=-Y^2-g_tZ.
\tag{2}
\]

Let s=exp(2x), K(x)=theta_3(0|is), and

\[
\mu(x)=\frac{\theta_2(0\mid is)^4}{\theta_3(0\mid is)^4},
\qquad w(x)=4\mu(x)(1-\mu(x)).
\tag{3}
\]

The Jacobi identity theta_3^4=theta_2^4+theta_4^4 and modular inversion give mu(-x)=1-mu(x). Thus w is even, w(0)=1 and w_x(0)=0. It is positive at every finite x and tends to zero at infinity. In fact w(x) is asymptotic to 64 exp(-pi exp(2x)). Its monotonicity on x>0 follows explicitly in Section2. These statements use the full theta constants and their standard principal-root modular normalization, as checked in the [reference annotation][refs]. No finite lattice replacement is made.

The identities below hold for finite t. The canonical sign obstruction will use the compact slab 0<=t<=1/2; including zero is for a uniform bound and makes no endpoint zero claim.

## 2. Finite nonlinear source equations

Define the scaled source variables

\[
\alpha=\pi s\theta_2(0\mid is)^4,\quad
\beta=\pi s\theta_4(0\mid is)^4,\quad
\eta=\pi s E_2(is),\qquad D=\partial_x.
\]

Here eta is a scaled E2 variable, not the Weierstrass eta of the cited paper. Proposition1, equation(8), of Brezhnev, Lyakhovich and Sharapov, together with their equation(6), yields

\[
\begin{aligned}
D\alpha&=2\alpha-\tfrac23\alpha(\eta+\alpha+2\beta),\\
D\beta&=2\beta-\tfrac23\beta(\eta-2\alpha-\beta),\\
D\eta&=2\eta-\tfrac13(\eta^2-\alpha^2-\alpha\beta-\beta^2),\\
D\log K&=-\tfrac16(\eta+\alpha-\beta)=:\ell.
\end{aligned}
\tag{4}
\]

These are equations in the source coordinate x, not physical heat time or a closed physical spectral-jet system. The canonical theta initial data and modular normalization remain part of their specification; arbitrary solutions of (4) are not silently identified with theta.

The exact source formula from [Note03][circle] reduces to a polynomial in this finite nonlinear state:

\[
g_t=e^{tx^2/4+x/2}K R,\qquad
R=D\ell+\ell^2+\ell
=\frac{q^2-6q+6\alpha\beta}{12},\quad q=\eta+\alpha-\beta.
\tag{5}
\]

The chosen weight satisfies

\[
w=\frac{4\alpha\beta}{(\alpha+\beta)^2},\qquad
D\log w=2(\alpha-\beta),\qquad
D\mu=-\frac{2\alpha\beta}{\alpha+\beta}<0.
\tag{6}
\]

Since mu(0)=1/2, w_x<0 on x>0. This supplies the promised nonlinear source description outside the finite linear circle-state obstruction. It does not supply a sign for the forced response.

## 3. The integrated current is unchanged

Define the complete integrand

\[
\mathscr I_w=wY^2+wg_tZ-w_xW.
\tag{7}
\]

The product rule and (2) give the exact pointwise identity

\[
\mathscr I_w=-D(wW),\qquad
\int_0^\infty\mathscr I_w\,dx
=Y(0)B_\lambda-BZ(0).
\tag{8}
\]

The infinity term vanishes from the actual source and weight tails, and w(0)=1 gives the stated lower boundary. This equals the unweighted integral of Y^2+g_tZ for every physical parameter, not just at a candidate event. The same conclusion holds for every normalized differentiable scalar weight for which these complete boundary operations are valid. No use of the nonlinear theta equations changes this equality.

At B=B_lambda=0 the integral is zero. Demanding an independently proved contradiction to this cancellation is still an exclusion target; equation(8) is not a smaller established sign criterion. With a finite cutoff X, the missing term would be -w(X)W(X), and it cannot be suppressed before a justified limit.

The square-root change U=sqrt(w)Y makes the same limitation explicit. Put delta=(D log w)/2=alpha-beta. Then

\[
U_{xx}-2\delta U_x+(\lambda+\delta^2-D\delta)U
=\sqrt w\,g_t.
\tag{9}
\]

Its spectral Wronskian is wW. The physical boundary remains U_x(0)=B because sqrt(w)(0)=1 and its derivative vanishes there. Multiplication by 1/w puts (9) in divergence form, but restores W as its Green boundary form, and restores the original norm and forcing integrals. The equation is still forced. Also sqrt(w) tends to zero at infinity; its inverse is unbounded. This is an identity for the selected responses, not a claim of bounded similarity on an unspecified operator domain.

## 4. Exact canonical source derivatives at the origin

Let K_*=theta_3(0|i) and v=pi^2 K_*^8/4. Modularity gives alpha(0)=beta(0)=sqrt(v). From K(-x)=exp(x)K(x), ell(0)=-1/2, so (4) gives eta(0)=3.

For g_0, repeated differentiation of (5) uses the polynomial operator D+1/2+ell. It yields

\[
\begin{aligned}
P_0(v):=g_0(0)/K_*&=(2v-3)/4,\\
P_2(v):=g_0''(0)/K_*&=(15-45v-2v^2)/8,\\
P_4(v):=g_0^{(4)}(0)/K_*&=(-285+1800v+191v^2+102v^3)/16.
\end{aligned}
\tag{10}
\]

The first and third derivatives vanish. All higher odd derivatives vanish by the original full-source evenness. Physical heat changes these derivatives by

\[
\frac{g_t''(0)}{K_*}=P_2+\frac t2P_0,\qquad
\frac{g_t^{(4)}(0)}{K_*}=P_4+3tP_2+\frac{3t^2}{4}P_0.
\tag{11}
\]

A deliberately coarse, fully rational enclosure suffices:

\[
\frac{47}{10}<v<\frac{49}{10},\quad
\frac85<P_0<\frac{17}{10},\quad -32<P_2<-30,\quad P_4>1430.
\tag{12}
\]

For completeness, pi is enclosed between 157/50 and 22/7 using the alternating arctangent series in Machin's identity. Positive exponential Taylor sums with a geometric remainder give 43/1000<exp(-pi)<11/250. Writing rho=exp(-pi), the full theta series obeys

\[
1+2\rho<K_*\le1+2\left(\rho+
\frac{\rho^4}{1-\rho^5}\right),
\quad \frac{543}{500}<K_*<\frac{1089}{1000}.
\tag{13}
\]

The tail bound follows from n^2>=4+5(n-2) for n>=2. These rational comparisons imply the v interval in (12). P2 decreases and P4 increases on that interval, giving the displayed polynomial bounds. The [checker][checker] evaluates all comparisons using exact fractions, including the exponential remainder. This is a complete source-constant enclosure, not a sampled physical theta transform.

For 0<=t<=1/2, (11)-(12) give

\[
-32<g_t''(0)/K_*<-1183/40<0,\qquad
g_t^{(4)}(0)/K_*>1382.
\]

Consequently the endpoint discriminant has the uniform negative bound

\[
\boxed{
\frac{g_t''(0)^2-g_t(0)g_t^{(4)}(0)}{K_*^2}
\le 1024-\frac85\,1382=-\frac{5936}{5}<0.
}
\tag{14}
\]

The constants are sufficient rational bounds, not measured best values.

## 5. The actual weighted integrand takes both signs

This section concerns large physical lambda=a^2/4, not large source x. Let T_lambda be the Volterra operator in (1). Repeated integration by parts gives, for any smooth source f with the stated tails,

\[
T_\lambda f=\sum_{j=0}^{N-1}
\frac{(-1)^j f^{(2j)}}{\lambda^{j+1}}
\; +\;\frac{(-1)^N}{\lambda^N}T_\lambda f^{(2N)}.
\tag{15}
\]

All source derivatives and their first moments are integrable, uniformly in t on [0,1/2]. The elementary bounds

\[
|T_\lambda f(x)|\le\lambda^{-1/2}\int_x^\infty|f(s)|ds,
\]
\[
|\partial_\lambda T_\lambda f(x)|\le
\frac1{2\lambda}\int_x^\infty(s-x)|f(s)|ds
+\frac1{2\lambda^{3/2}}\int_x^\infty|f(s)|ds
\tag{16}
\]

justify differentiating the remainder. Taking N=4, also for x derivatives, gives locally uniformly in x and uniformly in the declared t slab

\[
Y=\frac g\lambda-\frac{g''}{\lambda^2}
+\frac{g^{(4)}}{\lambda^3}+O(\lambda^{-4}),\qquad
Z=-\frac g{\lambda^2}+\frac{2g''}{\lambda^3}
-\frac{3g^{(4)}}{\lambda^4}+O(\lambda^{-5}).
\tag{17}
\]

Here and below g=g_t. Substitution into the complete integrand, before taking any absolute values, yields

\[
\mathscr I_w(t,x;\lambda)
=\lambda^{-4}A_t(x)+O(\lambda^{-5}),
\]
\[
\boxed{
A_t=w(g''^2-gg^{(4)})-w_x(gg'''-g'g'')
=-D\{w(gg'''-g'g'')\}.
}
\tag{18}
\]

The lower powers cancel exactly. At x=0, source evenness makes gg'''-g'g'' zero; (14) therefore proves A_t(0)<0 with a fixed margin. Thus the actual integrand is negative at x=0 for every sufficiently large lambda, uniformly in t.

It also becomes positive somewhere. Set F_t=w(gg'''-g'g''). Its endpoint values are F_t(0)=F_t(infinity)=0. Let m=(5936/5)K_*^2. By compactness and continuity, there is a common delta0>0 such that A_t<=-m/2 on [0,delta0]. Hence F_t(delta0)>=m delta0/2. Uniform source tails give an X>delta0 for which |F_t(X)|<=m delta0/4. Therefore

\[
\int_{\delta_0}^{X}A_t(x)dx
=F_t(\delta_0)-F_t(X)\ge m\delta_0/4.
\tag{19}
\]

For every t there is an x_t in [delta0,X] with A_t(x_t)>=m delta0/[4(X-delta0)]>0. The expansion (18) is uniform on this common compact rectangle. Choosing lambda large enough makes its remainder smaller than half both margins.

**Proposition.** There exists a finite L such that, for every 0<=t<=1/2 and lambda>=L, the proposed canonical integrand is negative at x=0 and positive at some x_t>0. The proof constructs an eventual regime, but this return does not evaluate L, delta0 or X numerically.

This disproves an everywhere one-sign or sum-of-nonnegative-terms representation of the unchanged integrand on the whole stated physical regime. It does not evaluate its small signed integral, locate an event, or refute an estimate made only under extra event conditions. The leading integral cancels exactly by (18); observing separately large signed terms is not a physical exclusion gain.

## 6. The collision controls retain their cancellation

For Note01's exact Gaussian-polynomial control at lambda=6,

\[
g_*=(16x^4+24)e^{-x^2},\quad
Y_*=(4x^2+4)e^{-x^2},\quad Z_*=-e^{-x^2},\quad
W_*=8xe^{-2x^2}.
\]

Even using this same canonical modular weight, the full integrand is

\[
\mathscr I_{w,*}=e^{-2x^2}
\{w(32x^2-8)-8xw_x\}
=-D(8xw e^{-2x^2}).
\tag{20}
\]

Its integral remains zero. It is negative at zero and positive at x=1/2 because w_x<0 there. The [exact record][record] checks this identity for an arbitrary scalar multiplier before specializing to the modular weight. Thus modular properties of the weight alone cannot supply the desired sign; the forcing source must participate in any further canonical estimate.

The other registered controls receive the same analytic premise screen; their existing event certificates are not rerun or reinterpreted as global thresholds here.

| Control family | What this test preserves | Canonical premise absent or scope limitation |
| --- | --- | --- |
| Gaussian-polynomial | Complete forced equation, weighted identity, exact multiple event | Its source is not (5); theta tails and full square arithmetic fail |
| Euler-factor | Smooth even positive source and complete weighted identity | Fixed canonical source and conductor are changed |
| Finite weighted-square and finite-tail | Source-mode equations and half-line weighted identity | Full unit coefficients and complete reflection are absent; endpoint matches are insufficient |
| Finite-prime-compatible square | Selected arithmetic relations and generic forcing identities | Full normalized reflection and canonical source data are absent |
| Reflected smooth and positive-primitive | Evenness, Kelvin covariance, shape and auxiliary positivity | The exact normalized canonical source relation (5) is absent |
| Finite-profile atomic or compact | Physical heat controls on their own domains | Atoms require a distributional forcing formulation; regularized controls still lack the full canonical source and profile growth |
| RH-conditional endpoint perturbations | Their stated local source closeness and completion | Ordinary canonical Dirichlet arithmetic changes; no implication about unchanged theta is imported |

Identifying the exact canonical trajectory is not itself an estimate. Equation(14) instead uses that trajectory to establish a failure of the proposed pointwise sign mechanism on the actual source.

## 7. Research decision and verification scope

The selected modular multiplier has returned a precise scoped obstruction. Its full nonlinear theta description is valid; its complete integral is unchanged; its actual canonical integrand eventually changes sign. Stop attempts to obtain a collision theorem from this scalar multiplier by generic positivity, an omitted weight derivative, or a claimed homogeneous conjugated equation.

Broader RTC-03 remains open. A continuation would need an explicitly different coupled current or a signed comparison with an independently proved gain and a stated domain. Increasing precision in the same multiplier identity, or recording its zero integral at additional controls, is not the next step. RTC-04 still has no characteristic realization, RTC-05's earlier Gaussian stop remains, and RTC-06 receives no numerical campaign from this result. A multiple event of any finite order at least two satisfies B=B_lambda=0, so no all-multiplicity exclusion follows from (8).

The [self-assessment][review] checks the normalizations, complete boundaries, source selection, asymptotic remainders and the scope of the proposition. The standalone [checker][checker] verifies exact differential algebra, source polynomials, rational enclosures, the leading cancellation and the explicit control. It does not certify the analytic asymptotic proof by finite testing or constitute independent review. This is an incremental return, not a manuscript milestone or investigation closeout.

[initial]: 01_RADIAL_THETA_GEOMETRY_AND_COLLISION_MECHANISMS_20261027.md
[circle]: 03_CIRCLE_HEAT_LIFT_AND_BOUNDARY_TRANSFER_OBSTRUCTION_20261027.md
[refs]: ../references/03_NONLINEAR_THETA_SYSTEM_AND_MODULAR_WEIGHT_20261027.md
[review]: ../reviews/04_MODULAR_WRONSKIAN_SELF_ASSESSMENT_20261027.md
[checker]: ../numerics/04_check_modular_wronskian_20261027.py
[record]: ../numerics/04_MODULAR_WRONSKIAN_CHECKS_20261027.json
[results]: ../../../../result-summaries/README.md
[arithmetic]: ../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md

# Angular gluing continuation and the precise brainstorm question

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Actual recorded configuration: `gpt-6-astra` (Codex), reasoning effort
**ultra**. This is an internal research assessment, not independent
mathematical validation. The request was to continue 02 until a specific
inequality prevents further progress, and prepare the question for a
separate ChatGPT brainstorm if needed.

**Outcome.** There is new analytic progress: an exact Volterra inverse,
a stable source-norm estimate, and a positive correction transform with
an explicit bound at every real frequency for `0<=t<=1`. The remaining
obstacle is a quantitative estimate preventing cancellation between this
positive correction and the complete angular channel. Generic positivity,
the Volterra identity and the scalar angular equations cannot supply that
estimate. The precise missing inequality is displayed below.

The proofs are in [Note 2](../notes/2_VOLTERRA_RECOVERY_POSITIVE_ANCHOR_AND_TRANSFER_GAP_20261013.md)
and the controls in [Note 3](../notes/3_COMPLETE_CHANNEL_VOLTERRA_CONTROLS_20261013.md).
The [numerical guide](../numerics/README.md) distinguishes exact constants,
finite diagnostics and complete outward enclosures. The
[execution record](../numerics/ANGULAR_CONTINUATION_EXECUTION_20261013.json)
pins the sources and the integrating agent's replay.

## 1. What was gained after the first calculation

Use the genuine half-line source and its even extension:

\[
\Phi(u)=\sum_{n\ge1}
(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}},
\qquad
H_t(x)=\int_0^\infty e^{tu^2}\Phi(u)\cos(xu)\,du.
\]

The exact short-period construction in 02 produced a signed auxiliary
channel `A_t=H_t−P_t`, where

\[
R(u)=2\pi^2e^u\sum_{n\ge1}n^2e^{-\pi n^2e^{4u}},\qquad
P_t(x)=\int_0^\infty e^{tu^2}R(u)\cos(xu)\,du.
\]

The earlier origin-sign obstruction concerned `Phi−R`, not `R`. The new
calculation proves

\[
R'+5R=-4\pi e^{-4u}\Phi,\qquad
R(u)=4\pi e^{-5u}\int_u^\infty e^v\Phi(v)\,dv.
\tag{1}
\]

If `a=Phi−R`, its inverse is

\[
\Phi(u)=a(u)+4\pi e^{-5u+\pi e^{-4u}}
\int_u^\infty e^{v-\pi e^{-4v}}a(v)\,dv.
\tag{2}
\]

All endpoints and cutoff terms are retained in Note 2. For the heated
sources, the inverse has operator norm at most `exp(pi exp(−4U))` in
`integral_U^infinity exp(u)|f(u)|du`, for every `t>=0`. This is stable
recovery of the full source; it does not imply a lower bound for one
Fourier observation.

There is also a genuine new global sign. The density `r_t=e^(tu²)R` is
strictly decreasing and strictly convex for `0<=t<=1`. Hence

\[
P_t(x)=\frac1{x^2}\int_0^\infty r_t''(u)(1-\cos(xu))\,du>0
\quad(x\ne0).
\]

An elementary bound `r_t''>5` on `[0,1/10]` gives

\[
\boxed{P_t(x)>\frac1{3000(1+x^2)}
\qquad(0\le t\le1,\ x\in\mathbb R).}
\tag{3}
\]

This includes `x=0` by the positive integral or its limit. It is an
analytic complete-source inequality, not a finite grid result.

## 2. Which tempting transfers fail

The correction's positive Fourier observation is useful, but it is not
the physical observation. Put `d=−R'(0)>0`. For fixed real time,

\[
P_t(x)=d x^{-2}+O(x^{-4}),\qquad
A_t(x)=-d x^{-2}+O(x^{-4}),\qquad H_t=A_t+P_t.
\]

The complete `H_t` and all its fixed spatial derivatives are Schwartz
on the real axis. Thus the two channels cancel to every algebraic order.
In particular, for every fixed `t` in `[0,1]` and every `N>=0`,

\[
x^N\frac{H_t(x)^2+H_t'(x)^2}{P_t(x)^2}\longrightarrow0.
\tag{4}
\]

A constant or polynomially decaying relative observation margin from
this anchor is therefore impossible, even if all physical zeros are simple.
Any useful large-height inequality needs a much smaller scale or a
different normalization with its own justified estimates.

Even the simple bound `|A_t|<=P_t` is false for genuine theta. The
complete outward calculation at `t=0,x=32` gives

\[
-9.60881\cdot10^{-5}<H_0(32)<-9.60862\cdot10^{-5},
\]
\[
0.00964664039<P_0(32)<0.00964664291,
\qquad
1.00996033<\frac{|A_0(32)|}{P_0(32)}<1.00996104.
\tag{5}
\]

Every omitted theta index, integration tail and quadrature remainder is
included. This rejects an absolute-value transfer strategy; it is not a
counterexample to a physical stationary inequality.

There is a stronger analytic control. The nearby positive sources in
the [review seeds](../notes/ANGULAR_GLUING_AND_RIGIDITY_REVIEW_SEEDS_20261013.md)
can be modulated to have an exact remote joint zero at any fixed
`0<T<1`. Define their correction by the same Volterra formula (1).
For sufficiently large displacement, the heated correction stays strictly
convex throughout `0<=t<=1`, and even the bound (3) survives. These
sources approach genuine theta in relative real-axis norm and retain
every fixed Gaussian integrability condition. They do not retain full
Jacobi lattice preparation. Note 3 proves this distinction and supplies
separate controls for the two stationary-sign targets.

Consequently a transfer proof must use quantitative information from
the actual lattice preparation that these perturbations violate. Source
positivity, convexity of the correction, exact scalar recovery and scalar
reflection are insufficient together.

## 3. The specific unresolved inequality

The positive denominator in (3) permits a regular normalization:

\[
\alpha_t(x)=\frac{A_t(x)}{P_t(x)},\qquad
b_t(x)=\frac{P_t'(x)}{P_t(x)}.
\]

Then

\[
\frac{H_t}{P_t}=1+\alpha_t,\qquad
\frac{H_t'}{P_t}=\partial_x\alpha_t+b_t(1+\alpha_t).
\]

On a specified compact rectangle
`mathcal R=[t_-,t_+] x [X_-,X_+]`, with `0<t_-<=t_+<=1`, the missing
observation estimate is an independently established number
`epsilon_R>0` such that

\[
\boxed{
|1+\alpha_t(x)|^2+
|\partial_x\alpha_t(x)+b_t(x)(1+\alpha_t(x))|^2
\ \ge\ \varepsilon_{\mathcal R}
\quad((t,x)\in\mathcal R).}
\tag{6}
\]

It would give `H_t²+(H_t')² >= epsilon_R/[3000²(1+x²)²]` there.
An exact collision corresponds to `alpha=−1` and `partial_x alpha=0`.
Equation (6) is explicitly a reformulation of the physical observation
gap, **not a newly proved estimate or a claim that the problem is easier**.
Its value is to identify precisely the cancellation any proposed angular
multiplier must control. Defining `epsilon_R` as the unproved positive
minimum of its left side would be circular.

The quotient obeys

\[
\partial_t\alpha=-\partial_x^2\alpha-2b\partial_x\alpha.
\tag{7}
\]

This is backward heat with a regular drift, so a forward maximum principle
does not supply (6). Equation (4) also precludes a constant or polynomial
uniform margin when the rectangle moves to large height.

The alternative downstream goal is to prove both complete stationary
inequalities

\[
-H_tH_t''\ge0\quad\text{on }H_t'=0,\qquad
-H_t'H_t'''\ge0\quad\text{on }H_t''=0,
\tag{8}
\]

on the required predecessor neighborhoods. In channel notation this
requires the cross term

\[
2A_t^{(j+1)}P_t^{(j+1)}
-A_t^{(j)}P_t^{(j+2)}-P_t^{(j)}A_t^{(j+2)}
\]

to compensate `−L_j(A_t)−L_j(P_t)`, with
`L_j(f)=(f^(j+1))²−f^(j)f^(j+2)`, after imposing stationarity of the
**sum**, for `j=0,1`. Positivity of `P_t` is not positivity of its
Laguerre expressions; those are negative at large real frequency.

## 4. Self-contained prompt for a new brainstorm chat

The following is the proposed question, rather than a request to repeat
the calculations already completed.

> We are studying angular Jacobi gluing for the genuine Newman source
> Phi and the heat transform H_t defined in Sections 1–3 above. The exact
> short-period angular channel is A_t=H_t−P_t. We have proved the complete
> Volterra recovery (1)–(2) and the global positive correction bound (3).
> The task is to identify a source-derived inequality, signed multiplier,
> or correlation estimate using **full imaginary Jacobi gluing** that can
> prove the normalized cancellation gap (6) on a declared domain, or
> both stationary inequalities (8).
>
> The balanced prepared field is
> F(u,z)=exp(u+pi z²/2) sum over n in Z of
> exp(−pi n² exp(4u)+2pi i n exp(2u)z).
> Put M=(partial_u²−1)F/16 and
> K_t(x,z)=(1/2) integral over real u of exp(tu²+ixu)M(u,z)du.
> Its physical projection is K_t(x,0)=H_t(x).
> The exact lattice law is
> F(u,z+p)=exp(kappa(pz+p²/2))F(u,z), with
> (p,kappa)=(exp(−2u),pi) or (i exp(2u),−pi).
> Transport through M must retain derivatives of the moving p and gauge.
> All lattice coefficients are exactly one. The imaginary law forces
> that preparation; the balanced PDE F_u=F_zz/pi−pi z²F alone does not.
>
> Please propose an inequality genuinely using this full preparation and
> explain why the positive near-theta collision controls in Section 2
> fail its hypotheses. Give the multiplier or quadratic form, its domain,
> and every endpoint, fixed spectral shift, angular continuation and tail
> payment. Begin with a bounded test where separate value and slope bounds
> are inconclusive. A useful analytic estimate must add information beyond
> source uniqueness or the exact scalar identities.
>
> Do not assume the shifted inserted source is positive, use the artificial
> x^(−2) correction as physical visibility, discard the projection
> correction, invoke a forward maximum principle for (7), or seek a
> constant/polynomial relative gap ruled out by (4). All finite angular
> jets are already scalar derivative dictionaries. Simply restating (6)
> or (8), or choosing a multiplier by dividing by the unknown physical
> value–slope norm, does not supply the missing estimate. If a different
> normalization removes the scale obstruction, justify its nonvanishing
> and the size of the transferred residual.

This brief and the two linked notes contain the definitions needed for
that conversation. The next step in 02 is specifically blocked at the
source-dependent cancellation inequality, not at a missing algebraic
identity or a numerical implementation. Further work should follow a
concrete candidate for that inequality rather than another round of the
same scalar transport.

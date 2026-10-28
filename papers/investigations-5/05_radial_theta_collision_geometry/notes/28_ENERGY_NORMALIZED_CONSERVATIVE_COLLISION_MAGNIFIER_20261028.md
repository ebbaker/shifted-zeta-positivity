# CTF-B01: a conservative flow with collision-driven response blow-up

28 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort
max**, Investigation05 chat0009, **Continue conservative theta flow**.

**Status: candidate selected; the stated construction, continuation
criterion and finite-time collision bound are proved in-note using the
classical heat/Markov tools identified below. Same-assistant checking.**
There is no theta-specific bound preventing breakdown, numerical flow run,
collision exclusion or independent specialist review.

The selected flow keeps the spatial L2 energy of the density and its true
first spectral derivative fixed. Diffusion competes with a common inward
radial drift. At a collision, cancellation of both conserved masses forces
the drift response and the spatial gradient energy to diverge within an
explicit finite auxiliary time. The exact colliding control has the same
behavior. The feedback is one spatially nonlocal scalar; it is not a
strictly local autonomous PDE.

| Next task | Type | Recommended model | Ready or dependency | Output |
| --- | --- | --- | --- | --- |
| **CTF-B02** | **B — brainstorm** | **Astra**: an additional canonical estimate is needed | Ready; candidate fixed and generic initializer comparison analytically fails | A theta-derived bound on the evolving gradient/response up to the paid deadline, or a precise failed estimate |
| CTF-E02, request R1 | E — execution | Sol: fixed identities and scalar bound propagation | Ready, optional; [frozen packet][packet] | Quantify the size and source of the already proved gap using record16; no pass/fail test or PDE simulation |
| CTF-E03 | E — execution | Sol | B02 supplies an inequality needing rigorous finite inputs | Only the quantities that inequality actually requires |

[Progress04][progress] is the sole live register. This completes B01's
two-class scope: the positive linear isotropic baseline, and one common
jet-energy feedback class. [Note27][n27] motivates the finite-time question
but supplies no numerical simulation of this new flow.

## 1. Observable and classification before the equation

At a fixed test point p=(T,A), let W=(U,V) contain a density and its actual
spectral derivative as defined in Section3. Use the fixed unit weight
between components, and write

\[
 E(s)=\int_{\mathbb R^3}|W_s|^2\,dX,\qquad
 G(s)=\int_{\mathbb R^3}|\nabla W_s|^2\,dX.
\]

The observables are the feedback coefficient alpha(s), accumulated
compression B(s)=integral_0^s alpha, and normalized gradient energy G/E0.
The intended collision effect is finite-time divergence of these
responses. The normalizing number E0=E(0)>0 is known from the initial
fields; it is not H, H_a, or a quantity required to vanish at collision.
There is also actual amplitude growth: the spatial supremum of |W_s|
diverges at the finite breakdown time proved below.

The classification matters. We prove, within this specified class, that
global auxiliary existence is equivalent to (H(T,A),H_a(T,A)) being
nonzero. **Global regularity is therefore a reformulation of pointwise
collision exclusion.** It is stated once as such, not offered as an
independent theta estimate or supported by samples. The construction and
its finite deadline are the analytical milestone. Any later exclusion
must come from a separately proved canonical estimate on the response.

This follows the [result index][results], [avoid index][avoid],
[target-classification rule][a01], [control screen][controls],
[scope rule][a07] and [known-result check rule][a11]. No equivalence with
RH on a larger time/height domain is newly asserted; that domain and its
transfer remain B03's separate obligation.

## 2. Linear isotropic baseline and the rescaling limitation

For a positive unit-mass radial convolution kernel P_s, the parameter
family P_s*f preserves its complete integral and commutes with its
spectral derivatives. Young's inequality gives L1 and L2 contraction.
Ordinary heat has the explicit extra cancellation already proved in
[Note25][n25]. These premises also hold for the exact collision control.
They provide no source-specific obstruction.

A prescribed common affine drift adds no independent geometry: the
equation j_s=Delta j+c(s)div(Xj), with b(s)=exp(integral_0^s c) and
tau(s)=integral_0^s b^2, has the exact representation

\[
j_s(X)=b(s)^3\,[e^{\tau(s)\Delta}j_0](b(s)X).
\tag{1}
\]

This comparison is scoped to positive convolution and scalar affine
drift, not all linear isotropic operators. A singular prescribed clock
cannot be interpreted as a collision-specific estimate. The selected
feedback below uses a fixed non-affine radial drift; its residual term
after (1) is explicit in Section5 and does not disappear under this
scalar time/dilation transformation.

## 3. Complete theta source and actual spectral family

For r=|X|>=1 and u=log(r)/2, use the full signed source

\[
 f(t,\lambda;X)=\frac{e^{tu^2}\Phi(u)}{8\pi r^3}
                   \cos(\lambda u),\qquad f=0\quad(r<1).
\tag{2}
\]

Here Phi is the complete canonical theta sum from Notes25–27. The
spherical volume change gives integral f=H(t,lambda), with no factor
missing. Fix one unit of preparatory heat smoothing:

\[
 f^\delta(t,\lambda)=K_1*f(t,\lambda),\qquad
 K_\sigma(X)=(4\pi\sigma)^{-3/2}e^{-|X|^2/(4\sigma)}.
\tag{3}
\]

This preserves H and every finite spectral jet. It is specified to avoid
claiming H1 regularity for the original jump at r=1. For theta, and for
the Gaussian control on t<T_c+4, the smoothed functions and their finite
parameter derivatives are Schwartz functions. This follows by bounding
weighted derivatives of the Gaussian against the source's finite moments.
The evolved domain includes the whole unit ball.

Keep the test point p=(T,A) fixed while varying the observation parameters
(t,lambda). Construct a common propagator j_s^p(t,lambda;X), initially
f^delta(t,lambda;X). Set

\[
U_s=j_s^p(T,A),\qquad
V_s=\left.\partial_\lambda j_s^p(T,\lambda)\right|_{\lambda=A}.
\tag{4}
\]

The first jet initially is K_1*[-u e^{Tu^2}Phi(u)sin(Au)/(8pi r^3)].
Both components use one common feedback coefficient determined at p.
Thus V is the derivative of a specified family, not an independently
assigned second field. A mark is a frequency/time at which to run the
same rule, not a chosen spatial direction.

Operationally one first solves the coupled pair (U,V), then applies its
common linear propagator to f^delta(t,lambda) at all running parameters.
Linear uniqueness identifies that propagator's marked value and derivative
with U and V. Only the marked pair has fixed L2 energy. Different marks
generally require different trajectories; no simultaneous all-frequency
magnification by one coefficient is claimed.

## 4. Frozen candidate, flux and jet accounting

Choose once and for all

\[
v(X)=X+\frac{X}{1+|X|^2},\qquad
d(X)=\operatorname{div}v
=3+\frac{3+|X|^2}{(1+|X|^2)^2},
\]
\[
D(s)=\int d(X)|W_s(X)|^2\,dX,\qquad
\boxed{\alpha(s)=\frac{2G(s)}{D(s)},\quad
\partial_s j=\Delta j+\alpha(s)\operatorname{div}(v j).}
\tag{5}
\]

Diffusivity, the nonlinear radial scale, preparatory time and jet weight
are all fixed at one. No parameter fitting is part of this contract.
The same equation acts on U and V. The drift is rotation covariant and
has no selected axis; its radial profile is a design choice, not an
identity imposed by theta arithmetic. Dependence of alpha on integrals
over space makes the equation nonlocal in its state.

Direct radial differentiation, with q=|X|^2, gives

\[
\frac78 I\le Dv(X)\le2I,\quad 3\le d(X)\le6,\quad
\Delta d=\frac{2q^2+20q-30}{(1+q)^4},\quad |\Delta d|\le30.
\tag{6}
\]

The radial eigenvalue is 1+(1-q)/(1+q)^2, minimized at q=3;
the tangential eigenvalue is 1+1/(1+q). Integration by parts gives

\[
E'=-2G+\alpha D=0,\qquad E(s)=E_0>0,
\quad 3E_0\le D\le6E_0,
\quad \frac{G}{3E_0}\le\alpha\le\frac{2G}{3E_0}.
\tag{7}
\]

The flux is J=-grad j-alpha vj. For a ball of radius R,

\[
\frac d{ds}\int_{|X|<R}j
=\int_{|X|=R}(\partial_rj+\alpha v_rj)\,dS.
\tag{8}
\]

All finite-radius fluxes, including through r=1, are retained. Smooth
weighted decay on compact lifespan intervals removes the outer cutoff
terms; regularity at the origin removes the inner ones. Consequently

\[
\int j_s^p(t,\lambda)=H(t,\lambda),\qquad
\int\partial_\lambda^k j_s^p=\partial_\lambda^kH
\tag{9}
\]

for all finite k. With p fixed, alpha is independent of the running t
and lambda, so the actual jet equation is
partial_s(partial_lambda j)=Delta(partial_lambda j)+alpha div(v partial_lambda j).
The pointwise physical heat identity partial_t j=-partial_lambda^2 j also
survives with the mark fixed.

There is a necessary qualification when a mark is moved. If z=partial_A
j_s^p(t,lambda), with the running parameters held fixed, then

\[
\partial_s z=\Delta z+\alpha\operatorname{div}(vz)
                  +\alpha_A\operatorname{div}(vj),\qquad z_0=0.
\tag{10}
\]

Here alpha_A=2G_A/D-2G D_A/D^2, with G_A and D_A obtained by
differentiating the marked pair, including its higher spectral jets.
On the diagonal p=(t,lambda), the total spectral derivative is V+z, not
V alone. The response z has zero complete integral, so both observations
still give H_a. Equations(4),(9),(10) specify which derivative is used;
no parameter-response term is silently discarded.

## 5. Local existence and the continuation criterion

We give the construction for nonzero Schwartz W0 with finite first and
second absolute moments; (3) meets these hypotheses. This suffices for
the intended theta/control application.

Write w(X)=X/(1+|X|^2). Remove only the linear part of the drift by
W_s(X)=b^3 Z_tau(bX), d tau/ds=b^2. For a nonzero vector field Z in H1,
define

\[
e=\|Z\|_2^2,\quad g=\|\nabla Z\|_2^2,\quad
b(Z)=(E_0/e)^{1/3},\quad
\widetilde D(Z)=\int d(Y/b(Z))|Z(Y)|^2\,dY.
\]

The transformed equation is

\[
\partial_\tau Z=\Delta Z+
\frac{2b(Z)g}{\widetilde D(Z)}
        \operatorname{div}_Y\{w(Y/b(Z))Z\},\qquad Z_0=W_0.
\tag{11}
\]

Its nonlinearity is locally Lipschitz H1 to L2 on every H1 ball with
e bounded away from zero. Indeed b and g are locally Lipschitz scalar
functionals, 3e<=Dtilde<=6e, and the bounded multiplier w(Y/b), its
spatial derivative, and their b derivatives are uniformly bounded when
b stays in a compact positive interval. No Sobolev embedding into L-infinity
is needed for this check.

The heat estimate from L2 to H1 is at most C(1+tau^(-1/2)) on bounded
time intervals. The Duhamel map is therefore a contraction in C([0,h];H1)
for h sufficiently small. This proves local existence and uniqueness.
The same locally smooth maps give parameter differentiation on compact
intervals within a common lifespan, as required for the marked response.
Equation(11) gives e_tau=-6ge/Dtilde and hence
b_tau/b=2g/Dtilde. Returning to s gives b_s/b=2b^2g/Dtilde=alpha,
so (11) solves exactly (5), rather than a different normalized equation.

Positive-time smoothing and weighted estimates follow from the common
linear equation with its now continuous scalar coefficient: after the
linear dilation, it has bounded smooth spatial drift on compact lifespan
intervals. The Schwartz initial data retain the weighted regularity
needed in (8). The positive, mass-preserving transition kernel also
propagates the component family and dominates |W| by the solution
starting from |W0|. The heat fixed-point template and the classical
contraction context are documented in [reference11][reference].

Let S_max be the maximal H1 lifespan and B(s)=integral_0^s alpha. A
finite endpoint with bounded G has a uniform local continuation interval,
by the same H1 construction with E0 fixed. In fact differentiation of G
and (6) give

\[
G'\le10\alpha G+30\alpha E_0,
\qquad G(s)+3E_0\le(G(0)+3E_0)e^{10B(s)}.
\tag{12}
\]

To verify the constants, the drift terms in G' are
2alpha integral grad(W)^T Dv grad(W)+alpha integral d|grad(W)|^2
-alpha integral (Delta d)|W|^2; diffusion contributes
-2||Delta W||_2^2. Thus a finite maximal endpoint requires
B(s) to tend to infinity. This is a continuation statement for this
fixed class, not a general nonlinear-diffusion theorem.

## 6. Collision forces finite-time response divergence

Set

\[
m=\int W_0=(H(T,A),H_a(T,A)),\quad
P_0=\int |X|\,|W_0(X)|\,dX,\quad \kappa=7/8.
\]

For the present nonzero data E0 and P0 are strictly positive. Assume
m=0. On any compact interval before S_max, two copies of the diffusion
with drift -alpha(s)v and the same Brownian increments satisfy

\[
\frac d{ds}|X_s-Y_s|^2
\le-2\kappa\alpha(s)|X_s-Y_s|^2.
\]

The given scalar coefficient is continuous there, and v is globally
Lipschitz with linear growth, so the common transition kernel exists
without explosion. Its backward action contracts Lipschitz constants by
exp(-kappa B(s)). This is the usual synchronous-coupling argument; the
display proves the time-dependent normalization used here.

Use the unnormalized Fourier transform, hat(W)(xi)=integral exp(-i xi.X)W(X)dX.
Because m=0, subtracting the backward exponential's value at zero gives

\[
|\widehat W_s(\xi)|\le |\xi|P_0 e^{-\kappa B(s)}.
\tag{13}
\]

This holds for the vector norm, using the same scalar kernel on both
components. Splitting Plancherel at frequency R gives

\[
E_0\le\frac{P_0^2 e^{-2\kappa B(s)}R^5}{10\pi^2}
          +\frac{G(s)}{R^2}.
\tag{14}
\]

Choose R^5=5pi^2 E0 exp(2kappa B)/P0^2, so the first term is E0/2.
Equations(7),(14) imply

\[
\boxed{\alpha(s)\ge c_0e^{\beta B(s)},\qquad
c_0=\frac{(5\pi^2)^{2/5}}6\frac{E_0^{2/5}}{P_0^{4/5}},
\qquad \beta=\frac{4\kappa}{5}=\frac7{10}.}
\tag{15}
\]

Since B'=alpha and B(0)=0,
exp(-beta B(s))<=1-beta c0 s. Therefore

\[
\boxed{m=0\quad\Longrightarrow\quad
S_{\max}\le S_*=\frac{60}{7(5\pi^2)^{2/5}}
                        \frac{P_0^{4/5}}{E_0^{2/5}}<\infty.}
\tag{16}
\]

At this finite endpoint, (12) forces B to diverge. Then (15) forces
alpha to diverge, and (7) forces G to diverge, with E identically E0.
This is genuine growth of the declared response. No nonzero signed
second moment or nondegenerate physical collision was assumed.

## 7. Converse and amplitude behavior: what the criterion actually says

Let h solve the same linear equation with h0=|W0|. Positivity gives
|W_s|<=h_s and integral h_s=M0. Since X.v(X)>=|X|^2, its second moment
R_h satisfies

\[
R_h(s)\le e^{-2B(s)}R_h(0)
       +6M_0\int_0^s e^{-2(B(s)-B(q))}\,dq.
\tag{17}
\]

If S_max is finite, B tends to infinity, and dominated convergence in
(17) gives R_h(s)->0. For any r>0, the mass outside the ball is at most
R_h/r^2, while Cauchy-Schwarz bounds the vector mass inside by
|B_r|^(1/2)E0^(1/2). Passing to the endpoint and then r->0 shows m=0.
Combining this with (16) proves

\[
\boxed{S_{\max}=\infty\quad\Longleftrightarrow\quad
       (H(T,A),H_a(T,A))\ne(0,0).}
\tag{18}
\]

At the finite endpoint,
||W||_1<=|B_r|^(1/2)E0^(1/2)+R_h/r^2 also tends to zero after choosing
r to decrease slowly with R_h. Because
E0<=||W||_infinity ||W||_1, the amplitude supremum diverges. This does
not identify a blow-up profile, rate, weak continuation beyond S_max,
or uniform behavior over physical time and frequency.

Equation(18) is the pointwise reformulation identified in Section1.
The positive result is a specified conservative magnifier and the paid
deadline (16); the unsolved problem is an independent theta bound which
prevents that finite breakdown. A plot showing regularity for selected
noncolliding theta points would not solve it.

## 8. Exact control and the canonical premise still missing

For Phi_star=(64u^4+6)exp(-(4+T_c)u^2), at T_c=1/4,

\[
H_*(T_c,a)=\frac{\sqrt\pi}{16}(a^2/4-6)^2e^{-a^2/16}.
\]

Both masses vanish exactly at a=2sqrt(6), so the candidate necessarily
has the finite-time divergence in (16). The smoothed control pair is
nonzero Schwartz data with E0,P0>0. It meets every generic premise of
the proof. At the two nearby frequencies in E01, H_star>0, so (18)
instead gives global existence. No numerical event detection is used.
At a=0, the odd spectral component alone vanishes; H(t,0)>0, and the
flow is global. Higher multiplicities are included by the same pair.

The other registered smooth controls are admitted after the same
preparatory smoothing on their finite-moment convergence domains. They
fail the canonical arithmetic/reflection premises recorded in the
[control register][controls], not positivity of the kernel, convexity
of v, or the feedback identities. Atomic inputs are outside the present
source-function statement; no unproved extension to them is invoked.

A canonical separating argument would have to prove, from the complete
theta data, a finite bound for G(s), or equivalently alpha(s), through
a rigorously paid deadline at the required physical test points. The
generic identities above cannot supply such a bound through the
control's deadline. Merely asserting global regularity repeats (18).
The first independent estimate remains **CTF-B02**.

## 9. A fixed finite payment for E02

There is a fully specified finite calculation before any PDE mesh is
considered. It compares two sufficient estimates, with their exact
status distinguished. From (7),(12),

\[
G'\le\frac{20}{3E_0}G(G+3E_0),\qquad
S_{\rm local}=\frac1{20}\log\!\left(1+\frac{3E_0}{G(0)}\right)
\tag{19}
\]

is a guaranteed lower lifespan: the solution exists for every
s<S_local. The estimate is generic and may be very weak.

Use exactly the C moments and normalized F values from E01. With
Mbar=C00+C01, define

\[
\overline P=\sqrt{C_{0,0}C_{2,0}}+
\sqrt{C_{0,1}C_{2,1}}+\frac4{\sqrt\pi}(C_{0,0}+C_{0,1}),
\]
\[
\overline G=\frac34(8\pi)^{-3/2}\,\overline M^2,
\qquad
\underline E=\frac{(24\pi)^{3/2}}{(16\pi)^3}
                  (F_{4,0}^2+F_{4,1}^2).
\tag{20}
\]

Then P0<=Pbar, G(0)<=Gbar and E0>=Eunder. For Pbar, apply the triangle
inequality to the preparatory Gaussian, whose mean radius is 4/sqrt(pi),
then Cauchy-Schwarz to the first radial moments C1,k. For Gbar use Young's
inequality and ||grad K1||_2^2=(3/4)(8pi)^(-3/2). For Eunder note
that K3*W0 evaluated at zero is K4*(f,f_a) evaluated there; Cauchy-Schwarz
uses ||K3||_2^2=(24pi)^(-3/2) and the normalization
K4*(f,f_a)(0)=(16pi)^(-3/2)(F4,0,F4,1).

Thus, when the lower energy is positive, the exact-data payments are

\[
\underline S_{\rm local}=\frac1{20}\log\!\left(1+
                        \frac{3\underline E}{\overline G}\right),
\quad
\overline S_*=\frac{60}{7(5\pi^2)^{2/5}}
                     \frac{\overline P^{4/5}}{\underline E^{2/5}}.
\tag{21}
\]

Before computing these quantities, their structural limitation can be
proved. Put C=C00+C01, eta=(F4,0^2+F4,1^2)/C^2 and p=Pbar/C. The
positive source and r>=1 give 0<=eta<=1 and
p>=1+4/sqrt(pi)>3. In particular, C2,k>=C0,k. Write
c_E=3sqrt(6)/(256pi^(3/2)) and
c_*=60/[7(5pi^2)^(2/5)]. Then Eunder=c_E C^2 eta and
Eunder/Gbar=(sqrt(3)/2)eta. Whenever eta>0,

\[
\frac{\underline S_{\rm local}}{\overline S_*}
=\frac7{1200}\left(\frac{15\sqrt{6\pi}}{256}\right)^{2/5}
\frac{\eta^{2/5}}{p^{4/5}}
\log\!\left(1+\frac{3\sqrt3}{2}\eta\right)
<\frac7{1200}<\frac1{100}.
\tag{22}
\]

For the strict bound, the parenthesized factor is less than one,
p^(4/5)>2 and the logarithm is less than two. Thus **these fixed generic
initializer payments can never certify collision exclusion**, even with
exact arithmetic. This is an exclusion of this assigned comparison,
not a bound on the actual lifespan or a failure of every sharper
estimate. Zero eta gives no lower energy payment at all.

Optional E02 has a narrower, quantitative question: how much larger is
the actual payment gap, and is it dominated by the energy-observation
loss eta or the absolute-moment payment p on the eleven existing cases?
It will propagate the existing floating acquisition diagnostics and
report the already acquired direct first-jet information for context.
It cannot change the analytic disposition (22), and is not a prerequisite
for B02. A threshold-crossing experiment here would only re-test a known
impossibility, contrary to [the known-result check rule][a11].

No new integration, optimization, time evolution or source scan is
needed for this optional payment audit. [Request R1][packet] freezes the
inputs, outputs and stop rule, assigned to Sol before implementation.
No E02 code or numerical run was made in this B01 return.

## 10. Disposition

B01 returns one explicit conservative, rotation-invariant feedback
system, complete physical/spectral observations, local existence and
continuation accounting, an exact colliding-control application and a
quantitative finite-time magnification law. The scalar feedback is
spatially nonlocal, and global regularity restates the physical
noncollision condition. Its mathematical use depends on a new canonical
finite-time bound; no such bound is claimed here. [Assessment16][review]
records the verification limits.

**Next: [B] CTF-B02 — Astra**, to derive the new theta-specific finite-time
estimate or record a precise failed bound. Equation(22) is the reason to
prioritize that conceptual task over the optional scalar audit; the
current model's identity is not the routing reason. **Optional [E]
CTF-E02 — Sol**, request R1, quantifies the known payment gap and its
dominant factors on the existing eleven cases. Neither task is executed
in this B01 return.

Continuation prompt:

> Continue [B] CTF-B02 from Note28 and Progress04. For the fixed conservative
> feedback flow, seek one canonical theta bound on G or alpha through the
> collision deadline, including the exact colliding control and a matched
> direct-information comparison. Do not substitute the already failed
> generic initializer payments or assume global regularity. Return an
> applicable estimate or a precise scoped failure, and issue E03 only for
> finite quantities actually required by that estimate.

[progress]: ../research-progress/04_CONSERVATIVE_THETA_FLOW_RESEARCH_PROGRESS_20261028.md
[packet]: ../research-progress/handoffs/CTF-E02_FEEDBACK_DEADLINE_PAYMENTS_REQUEST_R1_20261028.md
[n25]: 25_TOTAL_INTEGRAL_CONSERVATION_AND_DIRECTION_FREE_HEAT_FLOW_20261027.md
[n27]: 27_CONSERVATIVE_HEAT_BASELINE_E01_RETURN_20261028.md
[reference]: ../references/11_CONSERVATIVE_FEEDBACK_AND_DIFFUSION_CONTRACTION_20261028.md
[review]: ../reviews/16_CONSERVATIVE_FEEDBACK_MAGNIFIER_B01_ASSESSMENT_20261028.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a11]: ../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md

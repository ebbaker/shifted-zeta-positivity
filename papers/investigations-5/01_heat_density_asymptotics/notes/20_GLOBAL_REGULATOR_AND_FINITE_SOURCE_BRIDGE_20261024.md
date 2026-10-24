# A global regulator and a finite-source connection through bounded time

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**,
verified from this session's metadata.

**Status: regulator construction and finite-slab comparison estimates
proved in-note; same-assistant assessment.** This is a connection method,
not a completed informative all-time approximation. No finite source mesh
has yet been selected, optimized, or interval-certified across the entire
transition. [Note 19][clock] supplies this round's explicit positive-time
formula and quantitative improvement.

The point of this note is to make the connection obligations concrete:
one positive smooth regulator on all real time, a finite explicit heat
field anchored to theta source samples, and separate error budgets for
density, current, time derivative and the **actual covariance** of that
finite field. Its covariance is computed from the field, not defined by
solving an equation backward for a missing term.

This is a quantitative approximation construction under [avoid/01][a01].
Read the [result index][results], [collision controls][controls] and
[avoid index][avoid], particularly [status/evidence][a06] and [scope][a07].
There is no RH or simplicity conclusion and no novelty claim.

## 1. A smooth regulator with the existing endpoint prescriptions

Set C=Phi(0)sqrt(pi)/2 and fix eta>0, a measurement parameter independent
of theta zeros. Start with the time-only choice

\[
\epsilon_b(t)=\eta C(1+t^2)^{-1/4}. \tag{FB1}
\]

Let chi(t)=0 for t<=64, chi(t)=1 for t>=128, and on 64<t<128 use

\[
v=(t-64)/64,\qquad
\chi(t)=\frac{e^{-1/v}}{e^{-1/v}+e^{-1/(1-v)}}.
\]

For t>64 use the large saddle and epsilon_+ of Note 19 SC1, and put

\[
\boxed{\epsilon_g(t,x)=
\begin{cases}
\epsilon_b(t),&t\le64,\\
\exp\{(1-\chi(t))\log\epsilon_b(t)+\chi(t)\log\epsilon_+(t,x)\},&t>64.
\end{cases}} \tag{FB2}
\]

This is positive and C-infinity at every finite (t,x), with no y
dependence. The large saddle exists smoothly throughout t>=64:
the maximum of q_t' is at u_*=log(t/(8pi))/4 and equals
(t/2)(log(t/(8pi))-1)+9, positive at 64 and strictly increasing thereon.
The larger root has kappa>0. Its extension a little below 64 and the
flatness of chi justify smooth gluing. The numbers 64,128 are **regulator
definition points**, not certified onset times for the clock theorem.

At t=-T, epsilon_b/(eta C_T)=(1+T^-2)^-1/4=1+O(T^-2), with
C_T=C/sqrt(T). Thus the negative-time Gaussian comparison and the
O(T^-1) error for T rho in Note 14 survive. To see this without assuming
regulator independence, apply the Note 11 stability bound with epsilon_b.
For the Gaussian profile replace eta by eta_T=eta(1+T^-2)^-1/4;
|partial_(log eta) F_eta|<=2F_eta, and F_eta is uniformly bounded over
all real scaled heights on a fixed scaled transverse strip. The additional
profile error is O(T^-2). At positive t>=128 the regulator is exactly
epsilon_+, so the existing eventual positive-time theorems apply unchanged.

Every finite-time comparison below uses FB2, including its r_t and r_x
terms, with r=log epsilon_g^2. Positivity does not mean a uniform lower
bound over all x after the height-dependent part turns on. Choose a
bounded horizontal observation domain then, with its full filter buffer.
For a slab ending at t<=64, epsilon_g is independent of x and the
field/density estimates can be uniform over all real heights.

## 2. A finite explicit heat field anchored to source values

Choose a compact time slab [a,b], a full transverse buffer |y|<=Y,
a source cutoff U>0, an integer N>=1, and nodes
0=u_0<...<u_m=U, with maximum interval length h_s.
Use the finite canonical source

\[
\Phi_N(u)=\sum_{n=1}^N
(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}}.
\]

Let f be its continuous piecewise linear interpolant on [0,U], extended
by zero for u>U. Its jump at U is allowed. It is nonnegative because all
nodal values are positive. Define

\[
H_f(t,z)=\int_0^U e^{tu^2}f(u)\cos(zu)\,du. \tag{FB3}
\]

FB3 has a **finite error-function expression**, so the defining integral
does not remain an unevaluated copy of theta. On interval [u_i,u_(i+1)]
write f=A_i+B_i u. Define

\[
I_0(t,z;u)=\frac{\sqrt\pi}{2\sqrt{-t}}e^{z^2/(4t)}
\left[\operatorname{erf}\!\left(\sqrt{-t}\,u-
\frac{iz}{2\sqrt{-t}}\right)
-\operatorname{erf}\!\left(-\frac{iz}{2\sqrt{-t}}\right)\right],
\tag{FB4}
\]
\[
I_1(t,z;u)=\frac{e^{tu^2+izu}-1-izI_0(t,z;u)}{2t},\qquad
C_j=\{I_j(t,z;u)+I_j(t,-z;u)\}/2.
\]

Then H_f is the sum of A_i[C_0(u_(i+1))-C_0(u_i)] plus
B_i[C_1(u_(i+1))-C_1(u_i)]. The branch of sqrt(-t) gives the same
analytic expression; singularities at t=0 are removable. At t=0 use
I_0=(exp(izu)-1)/(iz) and
I_1=[exp(izu)(izu-1)+1]/(iz)^2, with their limits u and u^2/2 at z=0.
These formulas follow by completing the square and one derivative in u.
Numerical cancellation in them needs its own evaluation allowance.

The [primitive check script][primitive-script] and [small record][primitive-record]
compare the two cosine primitives against 64/96-node Gaussian quadrature
at nine small real-time/complex-space cases, including t=0 and z=0.
The largest discrepancy is 7.03e-16 in floating arithmetic. The simple
error-function series used in this check is restricted to those small
arguments; it is not a production evaluator or interval enclosure.
These checks do not choose a theta source mesh or validate the full bridge.

The finite field is even and real on the real axis, entire in (t,z), and
satisfies H_f,t=-H_f,zz **exactly**. Its source values are prescribed
before observing any density or roots. Once a mesh is chosen the formula
has finitely many scalar coefficients; its size is an explicit cost,
not automatically the desired simple global formula.

## 3. A complete source-to-jet error, including all real heights

Let B_2 be the complete-source derivative constant in Note 11 (2)--(3),
and C_b=(1-16exp(-3pi))^-1. The finite-mode nodal error satisfies

\[
0\le\Phi(u)-\Phi_N(u)\le\tau_N:={2\pi^2(N+1)^4e^{-\pi(N+1)^2}\over1-r_N},
\quad r_N=\left(1+\frac1{N+1}\right)^4e^{-\pi(2N+3)}<1.
\tag{FB5}
\]

Each positive omitted leading term n^4 exp(9u-pi n^2 exp(4u)) decreases
on u>=0; successive n ratios at zero give FB5. Linear interpolation of
the complete Phi would have uniform error <=B_2 h_s^2/8. Interpolation
of the finite nodal values adds at most tau_N. Therefore on [0,U],

\[
|\Phi-f|\le d_s:=B_2h_s^2/8+\tau_N. \tag{FB6}
\]

Put s=max(b,0). For j=0,1,2,3, choose U so that

\[
16\pi e^{4U}\ge2s,\qquad
\lambda_j=4\pi e^{4U}-2sU-9-Y-j/U>0.
\]

The logarithm of u^j exp(su^2+(9+Y)u-pi exp(4u)) has nonpositive
second derivative on [U,infinity) and derivative -lambda_j at U.
Consequently the complete tail is at most

\[
T_j={2\pi^2C_b U^j e^{sU^2+(9+Y)U-\pi e^{4U}}\over\lambda_j}.
\tag{FB7}
\]

Define the explicit positive integral F_j(s,Y,U)=integral_0^U
u^j exp(su^2+Yu)du. It has error-function/elementary recurrences, or use
the simpler upper bound U^(j+1)exp(sU^2+YU)/(j+1). Then

\[
\boxed{\delta_j=d_s F_j(s,Y,U)+T_j,\qquad
|\partial_z^j(H-H_f)|\le\delta_j\quad(0\le j\le3).}
\tag{FB8}
\]

This holds for every real x, all t in [a,b], and |y|<=Y. It follows
from |partial_z^j cos(zu)|<=u^j exp(Yu), not an oscillation-resolution
assumption. The same source error pays time derivatives because
partial_t partial_z^j H=-partial_z^(j+2)H. Nodal arithmetic errors
bounded by d_num add d_num F_j to delta_j; evaluating FB4 and the spatial
average adds separately recorded numerical error.

For fixed finite s,Y any prescribed jet tolerance is attainable: first
increase U until the tails are small, then N and mesh resolution until
d_s F_j is small. This existence assertion has an explicit but potentially
large cost. There is no claim of a small mesh across the unresolved
positive-time transition. In particular, reducing h_s cannot remove a
fixed theta-mode or source-tail allowance.

## 4. Stability of density, current, and its time derivative

Take a comparison buffer on which epsilon_g>=e_*>0 and
|r_t|<=a_0. Let P_j bound both |partial_z^j H| and |partial_z^j H_f|.
One available finite expression is

\[
P_j=\int_0^U u^je^{su^2+Yu}f(u)du+\delta_j.
\tag{FB9}
\]

The integral in FB9 is a finite combination of the same Gaussian
primitives (or their derivatives); it uses only the approximate source.
Since it is nonnegative it also bounds H_f. A positive normalized filter
does not enlarge the bounds below. Set c_0=125/(54sqrt(5)), and define

\[
E_\rho={2P_1\delta_1\over\pi e_*^2}
+{c_0P_1^2\delta_0\over\pi e_*^3},\qquad
E_j={P_1\delta_2+P_2\delta_1\over\pi e_*^2}
+{c_0P_1P_2\delta_0\over\pi e_*^3}.
\tag{FB10}
\]

Then |rho[H]-rho[H_f]|<=E_rho and |j[H]-j[H_f]|<=E_j, with the
**same** physical regulator at each point. The proof uses the exact
global gradient bound c_0/(pi epsilon^3) for
A(h)=epsilon^2/[pi(|h|^2+epsilon^2)^2], and A<=1/(pi epsilon^2).
There is no division by H, so the estimates include multiple events.

The time derivative can be paid explicitly as well. Let

\[
E_3={P_1\delta_3+P_3\delta_1\over\pi e_*^2}
+{c_0P_1P_3\delta_0\over\pi e_*^3},\qquad
\rho_{\max}=P_1^2/(\pi e_*^2).
\]
\[
\boxed{E_{\rho,t}=2E_3+
a_0\{E_\rho+2\rho_{\max}\delta_0/e_*\}
+2P_2E_\rho/e_*+
2\rho_{\max}\delta_2/e_*+4\rho_{\max}P_2\delta_0/e_*^2.}
\tag{FB11}
\]

To verify it, write h=H,p=H_z,v=H_zz,w=q/(|h|^2+q). Exactly,
rho_t=-2A Re(H_zzz conjugate(p))+r_t(1-2w)rho
+4rho Re(v conjugate(h)/(|h|^2+q)). Use
|w[H]-w[H_f]|<=delta_0/e_*,
|h/(|h|^2+q)|<=1/(2e_*), and the Lipschitz bound delta_0/e_*^2
for that last map. FB11 follows term by term. It bounds the actual
derivative difference, not the derivative of FB10's allowance.

## 5. An actual covariance comparison after smoothing

Use S=log(|H|^2+q), S_f=log(|H_f|^2+q), and the actual filtered
covariances Q,Q_f defined in Note 14, with a fixed spatial K.
Let b_i=sup|r_i| for i=x,y (b_y=0 for FB2), and set

\[
G_i=P_1/e_*+b_i,\qquad
d_i=\delta_1/e_*+2P_1\delta_0/e_*^2+b_i\delta_0/e_*.
\tag{FB12}
\]

Then |S-S_f|<=delta_0/e_*, |S_i|,|S_f,i|<=G_i and
|S_i-S_f,i|<=d_i. These follow from
S_i=2Re(H_i conjugate(H)/D)+w r_i and the same bounded rational maps.
In particular U_f=K*S_f has controlled boundary/harmonic traces wherever
the full convolution buffer is supplied; no independent harmonic function
is chosen to force the potential equation.

Write L_1=||partial_x K||_1+||partial_y K||_1 and L_2=||Delta K||_1.
The actual covariance and its required Laplacian obey

\[
\boxed{\|Q-Q_f\|_\infty\le4\sum_{i=x,y}G_i d_i,\qquad
\|\Delta(Q-Q_f)\|_\infty
\le(4L_1^2+6L_2)\sum_{i=x,y}G_i d_i.}
\tag{FB13}
\]

For the first bound compare the two averaged squares and the two
squares of averaged gradients. For the second, move derivatives of the
first averaged squares onto K, costing 2L_2 sum G_i d_i. For each
mean gradient v_i=K*S_i,
Delta(v_i^2)=2v_i Delta v_i+2|grad v_i|^2. Their differences cost
4(L_2+L_1^2) sum G_i d_i. This proves FB13 without differentiating a
static source error and without requiring pointwise third gradients of S.
The compact C3 kernel has the necessary integrable derivatives.

H_f solves the heat equation, so its density/potential/current/covariance
obey all the variable-regulator identities in Note 14 exactly. Their
coefficients, curvature correction and source must all be retained.
FB8--FB13 provide a direct source-based stability estimate for comparison
with theta. This is why zero heat residual is not the only evidence.
It is not an autonomous covariance closure in R_f alone, nor does it
transfer the late-time clock's small errors to its unknown covariance.

## 6. What remains before this becomes an all-time approximation

The useful finite bridge must still select and evaluate U,N,the mesh,
eta, the observation widths and the time slab, then show informative
overlap with the negative Gaussian and positive explicit clock. The
existence of a finite approximation for each compact slab is weaker than
one short formula with informative bounds across the entire transition.
For the user-facing target, FB2 defines a global **measurement protocol**;
it does not interpolate two densities and assert their equation.

An overlap comparison is legitimate: if each approximation has its own
error against theta, their difference is bounded by the sum. A time
blend (1-chi)H_f+chi G adds the heat residual chi'(G-H_f), even when
both component fields solve heat. Such a blend needs its own derivative
and source comparison; it is not asserted here.

A fixed compact-source H_f cannot replace the entire positive endpoint.
For fixed U,Y its jets are O(exp(tU^2+YU)); the true saddle normalization
has log M~tL^2 and L tends to infinity. On fixed spatial buffers,
epsilon_+ also outgrows every exp(tU^2). Consequently rho_epsilon+[H_f]
tends to zero while the true averaged density grows like L k_h/pi.
This is a precise failure of the **fixed compact-source bridge at positive
infinite time**, not an obstruction to growing cutoffs or an all-time
construction. The exact heat residual remains zero in this failed example.

Regulator-to-zero-measure bias is still separate from FB10. The smooth
jet estimates continue through multiple events, but a uniform small
regulator bias on a time slab needs the cluster floors/multiplicities
of Note 06/14 or another paid weak argument. Positivity alone supplies
none. The generic comparison also holds for smooth colliding controls.
Atomic and polynomial controls need their own source approximation, not
the canonical B_2. Euler-factor, weighted-square, reflected and primitive
controls lack the unchanged theta source used in FB5--FB8; none is
excluded by FB10--FB13. Nearby smooth colliding sources may satisfy
analogous stability inequalities with their own constants.

## 7. Continuation entry point and recorded status

Read [Note 19][clock] and this note after the author's goal in
[Note 18][handoff]. The next bounded numerical/analytical task is to choose
a finite source representation on a declared transition slab and evaluate
the **complete** FB8--FB13 budget, improving local source approximation
where the global B_2 h_s^2 bound is too costly. Compare the actual
covariance and density on held-out times; retain arithmetic and filter
quadrature errors. Do not call a bridge complete without useful overlap.

The positive outer-height transition, certified eventual onset,
independent review and full all-time boundary solution remain open.
HDA-02--06 remain partial; HDA-07--09 remain gated. This source-based
finite-slab route offers an alternative to propagating the mixed-sign
density PDE, but it has not yet delivered the all-time target. See the
[progress ledger][progress] and [same-assistant assessment][review].

This conversation is **0004 — Continue heat density asymptotics**,
thread `01a17005-c3ef-7a22-80de-17bf918be4e9`, uniquely registered in
this investigation's chat-histories. A later new chat must use its own
actual identity. Use the repository refresh tool at the start/end and
the bounded exact-turn deferred capture until trusted completion-hook
activation is verified. Keep source materials and prior work unchanged.

[clock]: 19_EXPLICIT_SADDLE_CLOCK_AND_EXACT_PHASE_20261024.md
[handoff]: 18_CONTINUATION_TOWARD_EXPLICIT_ALL_TIME_APPROXIMATION_20261024.md
[progress]: ../research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md
[review]: ../reviews/06_EXPLICIT_CLOCK_AND_FINITE_BRIDGE_SELF_REVIEW_20261024.md
[primitive-script]: ../numerics/finite_bridge_primitive_checks.py
[primitive-record]: ../numerics/FINITE_BRIDGE_PRIMITIVES_20261024.json
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a06]: ../../../../avoid/06_status_stronger_than_the_evidence.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md

# Coupled exterior curvature, its signed contribution, and the energy budget

27 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**.
Chat0004, thread `01a17e2e-8b79-7b91-9be0-f1405597eb03`.

**Status: proved in-note conditional expansion and a scoped failure of the
bounded analytic exterior correction as a logarithmic saving; same-assistant
assessment only.** The first source-dependent energy term is computed
without separating its signed moments. It changes the bounded remainder,
not the collision coefficient. At a hypothetical canonical threshold its
sign increases the finite energy term. The specified transverse consumer
has the same limitation with the same source data and a paid regulator.
No independent excluding theta inequality or improved bound on Lambda is
obtained. See [Review05][review] and [the continuation][continuation].

Read [Note09][interface] for the complete operator, fixed-wall payments,
source hierarchy and energy transfer. The inherited leading profile is
[Note07][prior], and exterior curvature already appears in
[HDC Note19][curvature] in a different time/height regime. The
[result index][results], [control register][controls], [avoid index][avoid],
[classification][a01], [scope][a07] and [coupled-estimate rule][a12] apply.
These elementary deductions carry no literature-priority claim.

## 1. The first coupled source coefficient

Keep the arbitrary real event (t_c,a,m,c), h_n and P_n of Note09. Put

\[
 \alpha=h_{m+1}/c,\quad \beta=h_{m+2}/c,\quad
 \gamma=2\beta-\alpha^2=(\log U)_{zz}(t_c,a),\quad
 \kappa=\frac{m(m-1)}{16},\quad p=\frac{m(m-1)}2.           \tag{18}
\]

The full shifted-source bound in Note09, N=2, gives
F_r=P_m+r alpha P_{m+1}+r^2 beta P_{m+2}+O(r^3), uniformly with
the derivatives and buffers needed there. This uses exact event
cancellations. It is not an independent reason those cancellations cannot occur.

Let w_i^0(s)=sqrt(s)h_i, where h_i are the roots of P_m(1,.).
The polynomial identities

\[
 P_{m+1}=wP_m-2sP_m',\quad P_{m+1}'=(m+1)P_m,\quad
 P_m''(w_i^0)=\frac{w_i^0}{2s}P_m'(w_i^0),\quad
 P_{m+2}(w_i^0)=-2s w_i^0 P_m'(w_i^0)
\]

give, by implicit expansion at each simple scaled root,

\[
 w_i(r,s)=w_i^0(s)+2\alpha s r+\gamma s w_i^0(s)r^2+O(r^3).
                                                                    \tag{19}
\]

In detail the second correction is minus
[(2alpha s)^2 P_m''/2+alpha(2alpha s)P_{m+1}'+beta P_{m+2}]/P_m'.
This equals gamma s w_i^0. The order-r motion is common to all roots,
so it cancels in every gap. Consequently

\[
 e_r(s)=r^2E(t_c+r^2s)=\frac\kappa s-2\kappa\gamma r^2+O(r^4),
\]
\[
 \boxed{E(t_c+u)=\frac\kappa u-2\kappa\gamma+O(u),\qquad
 I_r=\kappa\log4-6\kappa\gamma r^2+O(r^4).}                \tag{20}
\]

The improvement from the inherited O(u^{-1/2}) remainder is a bounded
explicit correction followed by O(u). The logarithmic coefficient is unchanged.

Here is the justification and an explicit bound for the O(r^4), rather
than an unsupported parity assertion about individually labeled roots.
For complex r near zero,
F_{-r}(s,w)=(-1)^m F_r(s,-w). Preparation therefore reflects the complete
root set, and e(q)=Q/D is unchanged. The energy is an even holomorphic
function of r wherever Note09's discriminant gate holds.

Choose r_*>0 so, for every complex |r|<=r_* and real 1<=s<=4, that
gate holds, r_*<=q/2, 4r_*^2<=tau, and r_*R<=rho/2. The explicit
source-Cauchy gate 2M_0 r_*/(|c|q^{m+1})<=epsilon_* suffices for the
field part. With the coefficient constants of Note09 set

\[
 K_E=\mathscr Q_{abs}(M)/d_0,\qquad C_E=4K_E/(3r_*^4).
\]

Cauchy's estimate for the even coefficients, after the terms through r^2,
gives for 0<=r<=r_*/2

\[
 |e_r(s)-\kappa/s+2\kappa\gamma r^2|\le C_E r^4.           \tag{21}
\]

Thus |E(t_c+u)-kappa/u+2kappa gamma|<=C_E u for
0<u<=r_*^2/4, and the annulus remainder in (20) is at most 3C_E r^4.
These are explicit fixed-event constants, not uniform height estimates.

The discriminant and exterior pieces in Note09 independently reconcile:

\[
 d_r(s)=s^p d_*[1+2p\gamma s r^2+O(r^4)],\qquad
 \mathcal B_r(s)=p\gamma r^2+O(r^4).
\]

Their contributions to I_r at order r^2 are respectively
3p gamma r^2/4 and -3p gamma r^2/2; together they give
-3p gamma r^2/4=-6kappa gamma r^2. Dropping the unit gives the wrong sign.

## 2. Signed source treatment and threshold sign

Write A(v)=exp(t_cv^2)Phi(v), f_n(v)=v^n cos(av+n pi/2),
J_n=integral A f_n=n!h_n. The complete coupled expression is

\[
 \gamma=\frac1{J_m^2}\iint A(v)A(w)\left[
 \frac{f_m(v)f_{m+2}(w)+f_{m+2}(v)f_m(w)}{(m+1)(m+2)}
 -\frac{f_{m+1}(v)f_{m+1}(w)}{(m+1)^2}\right]dv\,dw.     \tag{22}
\]

Absolute convergence follows from the complete theta tails. This is the
identified signed term; its two products have not been independently
discarded. Positivity of A does not sign its oscillatory kernel.
For a magnitude bound only, put
M_n=(1/n!)integral A(v)v^n dv. Then

\[
 |\gamma|\le 2M_{m+2}/|c|+M_{m+1}^2/|c|^2.               \tag{23}
\]

That bound affects only the finite correction in (20). Keeping (22)
exact does not change its r^2 multiplier. Thus the absence of a leading
saving here is not an artifact of taking separate absolute values.

Now impose t_c=Lambda>0. The entire canonical field is even, order one,
and all its zeros at t_c are real. Its paired Hadamard product, as used in
[Polymath Proposition 3.1][poly], gives the absolutely convergent identity

\[
 \boxed{\gamma=-\sum_{\lambda\ne a}(a-\lambda)^{-2}\le0.} \tag{24}
\]

Zeros are counted with multiplicity; the m copies at a are omitted.
The derivative removes the principal-value ambiguity of the first
logarithmic derivative. There is no quadratic exponential factor for an
order-one entire function. This is the same exterior sign mechanism as
HDC Note19, now conditional on the positive all-real threshold rather
than RH at time zero.

Source positivity gives H(t_c,0)>0, so a is nonzero. Evenness supplies
m exterior copies at -a, and hence a quantitative, but non-excluding, bound:

\[
 \gamma\le-\frac{m}{4a^2},\qquad
 \lim_{u\downarrow0}\left(E(t_c+u)-\frac\kappa u\right)
       \ge\frac{\kappa m}{2a^2}.                         \tag{25}
\]

This is a lower bound on a bounded energy term. It supplies no upper
coefficient below kappa. It uses the contradiction hypothesis's all-real
slice and is shared by even order-one all-real controls; it is not a new
arithmetic discriminator.

## 3. Exact controls and the scope of the failure

For P_m(t-t_c,z-a), gamma=0 and E=kappa/(t-t_c) exactly. For the heat
flow with initial datum e^{alpha(z-a)}(z-a)^m, the nonzero unit produces
the common drift 2alpha(t-t_c), but gamma=0 and the same exact energy.
These controls check translation cancellation and arbitrary m, not
canonical source arithmetic.

The positive atomic source from Note07 gives

\[
 F(t,z)=e^t\cos z+e^{-3t_c}e^{4t}\cos2z.
\]

At (t_c,pi) it has m=2, c=-3e^{t_c}/2, alpha=0,
beta=-5/12, gamma=-5/6. Its local energy is therefore

\[
 E(t_c+u)=\frac1{8u}+\frac5{24}+O(u),\qquad
 I_r=\frac18\log4+\frac58r^2+O(r^4).                      \tag{26}
\]

Directly, put z=pi+y and v=y^2. The zero equation
-cos y+exp(3u)cos(2y)=0 gives v=2u-(10/3)u^2+O(u^3),
and 1/(4v) verifies (26). As shown in Note07, its all-real times are
exactly [t_c,infinity). The atomic model has infinitely many simultaneous
threshold events and fails theta's eventual simplicity there; that extra
global premise has not been used to derive a better local coefficient.

The [full control register][controls] is applied analytically; old
interval certificates are not rerun here.

| Control | Passes the estimates used here | Missing or inapplicable premise |
| --- | --- | --- |
| Heat polynomials / exponential unit | Complete preparation, gamma correction, energy and transverse limits | Canonical positive theta source and global growth |
| Positive atomic thresholds / counter-kernels | Shifted-source moment bounds when finite, actual local events and universal coefficient | Unchanged theta arithmetic; atomic threshold lacks eventual simplicity |
| Euler-factor controls | Local heat/source formulas and genuine positive thresholds; (24) applies at an all-real threshold | Original coefficients and completion; no derived bound here rejects them |
| Weighted-square / finite-tail controls | Their documented local events, source tails, and conditional transfer | Full reflection/source; they have no all-real time, so (24)-(25) are not claimed for their event slice |
| Reflected, smooth-shape and positive-primitive controls | Their respective analytic/local collision properties and (20) | Unchanged ordinary theta arithmetic; global all-real hypotheses only when separately supplied |
| Finite-prime / finite-profile controls | Their stipulated observations, moments and local unfolding | Respectively full reflection or full profile/global growth; no common preservation list is invented |
| RH-conditional endpoint controls | Local formulas at their zero-time event | Not unconditional examples of a positive threshold; ordinary Dirichlet arithmetic fails |

**Scoped conclusion.** Refining an event-conditioned finite heat-jet model,
its complete source remainder, and bounded analytic exterior derivatives
cannot turn its coefficient kappa into a strictly smaller one. Equations
(20)-(22) prove this for the actual coupled correction, not just a
separate-majorant implementation. A matching positive-source control
realizes the obstruction. This does **not** rule out using exact theta
moments to prove that the event equations themselves are inconsistent,
a global arithmetic restriction, or a different estimate with a genuine
order-one contribution on each annulus. Finite exact formulas using full
theta data are not ruled out merely because they are finite.

## 4. The specified transverse consumer with the same data

This bounded check addresses the fallback in Note08 without taking over
chat0002's growing-window task. At s=-1 take a smooth cutoff chi equal to
one on fixed neighborhoods of all roots i h_i of P_m(-1,w), and zero
outside a larger fixed disk. Let psi(w)=chi(w)(Im w)^2 and
Y_r=sum chi((z-a)/r)(Im z)^2 over H(t_c-r^2,z)=0.
For small r the count is m, with no entering roots.

The same calculation as (19) gives
w_i(r,-1)=i h_i-2alpha r-i gamma h_i r^2+O(r^3).
Conjugation and r->-r imply that Im w_i is even for each fixed branch
near i h_i. Therefore

\[
 \boxed{Y_r/r^2=2m(m-1)-4m(m-1)\gamma r^2+O(r^4).}        \tag{27}
\]

The remainder can be paid explicitly. Choose epsilon<min gap(h_i)/8
and r_->0 so the source-Cauchy bound gives exactly one scaled root in
each epsilon-disk for all complex |r|<=r_-. Let T_-=4epsilon/(3r_-^4)
and r_max=r_-/2. Cauchy's even tail gives
|Im w_i-h_i+gamma h_i r^2|<=T_-r^4. A valid constant for the O(r^4)
in (27) is
sum_i[gamma^2 h_i^2+2|h_i|(1+|gamma|r_max^2)T_-+T_-^2 r_max^4].
The cutoff is identically one at all these roots, so it introduces no
unpaid local Taylor term.

Here is the regulator payment for using the actual source approximation
f=F_r(-1,.) and g=H_{2,V}/(cr^m), rather than just its root expansion:

\[
 \mathcal Y_\eta(f)=\frac1{4\pi}\int
          \log(|f|^2+\eta^2)\Delta\psi\,dA,\quad
 |\mathcal Y_\eta(f)-\mathcal Y_\eta(g)|
       \le\frac{\|\Delta\psi\|_1}{4\pi}\frac\delta\eta.   \tag{28}
\]

Here delta is the actual normalized error from Note09, not a raw field
allowance. For bias, use disjoint disks of radius d about the actual simple
scaled roots, with |f(w)|>=k|w-w_i| there, and floor h_far on the
remaining test support of area A_far. Then direct polar integration gives

\[
 |\mathcal Y_\eta(f)-Y_r/r^2|\le
 \frac{\|\Delta\psi\|_\infty}{4\pi}
 \left[m\pi\frac{\eta^2}{k^2}
     \left(1+\log\left(1+\frac{d^2k^2}{\eta^2}\right)\right)
       +A_{far}\frac{\eta^2}{h_{far}^2}\right].            \tag{29}
\]

The same applies to g and its response. These floors follow from the
simple scaled Hermite disks, not a physical minimum gap. For example,
put d=epsilon/2, require root displacement <epsilon/4, and require the
field error from P_m(-1,.) below half both its epsilon-circle floor
p_epsilon and (epsilon/4)^m. On each original disk, the minimum principle
applied to the inverse local unit gives k=p_epsilon/(3epsilon);
outside the moving d-disks one may take h_far=(epsilon/4)^m/2.
All these gates hold for sufficiently small fixed-event r, for f and g.

With N=2, delta<=D_2 r^3 and eta=r on 0<r<=min(1,r_max), (28)-(29)
cost O(r^2(1+log(1/r))). The physical field regulator is
|c|r^m eta. The limiting signal 2m(m-1) survives; no strict upper
bound below it is obtained from these data. This is the same demonstrated
obstruction as for energy, with the bias actually paid.

**Moving-test audit.** Equations (27)-(29) compare fixed slices; no time
derivative is used. For clarity, with tau=t-t_c<0, r=sqrt(-tau),
psi_r(z)=r^2psi((z-a)/r), and zeta=|c|r^m eta(r), differentiation would give

\[
 \partial_\tau\psi_r=-\psi+\tfrac12 w\cdot\nabla\psi,
 \quad \partial_\tau\log\zeta=-\frac{m+r\eta'/\eta}{2r^2},
 \quad \partial_\tau(r^{-2})=r^{-4}.                      \tag{30}
\]

In the physical integral r^{-2}(4pi)^{-1}integral L Delta psi_r,
L=log(|H|^2+zeta^2), one must retain all three terms: the derivative of
r^{-2}, L Delta(partial_tau psi_r), and
partial_tau L=[2Re(H_tau conjugate H)+2zeta zeta']/(|H|^2+zeta^2).
None is silently suppressed by the slice comparison.

## 5. Complete accumulation budget for this information class

Choose W isolating just the event, so E_W=E_cl for the small right-time
interval. For 0<epsilon<u_0<=r_*^2/4, (21) proves

\[
 \left|\int_\epsilon^{u_0}E_W(t_c+u)du
   -\kappa\log(u_0/\epsilon)+2\kappa\gamma(u_0-\epsilon)\right|
       \le\tfrac12 C_E(u_0^2-\epsilon^2).                 \tag{31}
\]

Thus an acquired upper budget for the event-conditioned class is

\[
 A_N=\kappa,\quad\eta_N=0,\quad
 C_N=2\kappa|\gamma|u_0+\tfrac12 C_Eu_0^2,\quad\Delta_N=0. \tag{32}
\]

This is **not** an independent canonical E6 estimate. It demonstrates
that the completed local error accounting itself has no strict margin.
The constant has no dependence on epsilon or an assumed minimum gap.

For r_j=2^{-j}r_0, disjoint annuli [r_j^2,4r_j^2] tile (0,4r_0^2].
Take r_0<=r_*/4 if using (31) up to their common top u_0=4r_0^2.
Every error retained in this return has the following classification.

| Term | Annulus payment | Accumulation |
| --- | --- | --- |
| Coupled exterior / common-motion correction | <=6kappa |gamma|r_j^2 | <=8kappa |gamma|r_0^2 |
| Analytic energy remainder | <=3C_E r_j^4 | <=(16/5)C_E r_0^4 |
| Source-tail transfer, fixed N,V | C_{N,V}r_j^{N+1}, with C from Note09 (17) | C_{N,V}r_0^{N+1}/(1-2^{-(N+1)}) |
| Approximate moments h_n, n>m | coefficient errors times r_j^{n-m}, followed by Note09 transfer | Summable at fixed acquired constants |
| Unpaid low moments n<m | r_j^{n-m} in (11) | Not admissible; no bounded budget asserted |
| A generic persistent normalized/observable allowance e_N | e_N per full annulus | Adds e_N/log4 to eta_N |
| Transverse bias/transfer, eta=r_j, N=2 | O(r_j^2(1+log(1/r_j))) | Summable; does not change the transverse limit |
| Fixed wall, count and amplitude conditioning | Gates/constants in Note09 | No free error term; must hold before summing |

For the logarithmic bias term specifically,
sum_j r_j^2 log(1/r_j)=r_0^2[(4/3)log(1/r_0)+(4/9)log2].
A partial last annulus can be integrated directly by (21); it creates
no new coefficient. A fixed larger W containing other multiple events
would have their additional logarithmic coefficients and cannot be
substituted into (31) without payment. Source-transfer and exact expansion
budgets are alternative comparisons of the same field: do not count a
truncation payment twice when using the direct exact identity (31).

If a model is used instead, add its (17) series to its complete budget.
An n=m coefficient uncertainty can be a harmless common amplitude when
all data scale coherently; absent such correlation, (11) charges it as
a persistent error. It cannot be omitted by calling it normalization.

## 6. Parameter audit and research disposition

The statements cover each fixed finite real event, arbitrary finite m,
and in particular every hypothetical t_c>0, without choosing b or a.
For a declared 0<b<t_c<=B, keep r^2<t_c-b if the pre-event slice must
remain in that slab. No such restriction is needed for local analyticity.

| Dependency | Acquired here | Not acquired |
| --- | --- | --- |
| Time/source shift | Full exp(t_cv^2) in all moments/tails | Original negative-time recurrence on a positive shifted source |
| Height a | Phase retained exactly; envelope independent of real a | A uniform lower bound for |c| or wall floors at growing height |
| Multiplicity | Explicit m, polynomial constants and kappa_m | A multiplicity-independent small conditioning constant |
| Wall rho,tau | Conditional isolating wall and finite B_1 | Effective common walls over an entire slab |
| Resolution r | Explicit sufficiently-small gates after parameters fixed | An unjustified simultaneous limit in r,a,m,N |
| Order N / cutoff V | Fixed N=2 already serves this calculation; explicit fixed-order formula | Growing-order approximation theorem or certified moment evaluation |
| Positive target b | No local singular 1/b requirement | Coverage/exclusion of candidates up to the exterior exp(C/b) onset |
| Arithmetic margin | Coupled gamma term evaluated, including threshold sign | An independent order-one saving per annulus or incompatible event jets |

Polymath's uniform exterior theorem is used only as the inherited
finite-event reduction, not as a local collision exclusion. Its height
onset exp(C/b) is distinct from the local Gaussian rescaling. Uniform
bounded constants at b=0 are not logically necessary to exclude every
fixed positive event. Here the failure already occurs for each fixed
event: Delta_N=0. Reaching arbitrarily small b cannot repair that failure
by an exchange of limits.

CE-01 and CE-03 have complete conditional interface deliverables. CE-02
is partial, with a direct finite source-tail bound and a failed direct
reuse of the old recurrence. CE-04 returns the signed finite correction
and the scoped failure above; its excluding arithmetic obligation remains
open. CE-05 has a complete budget for the tested class, with zero margin.
CE-06 has no new excluded slab. CE-07 supplies a dependency map, not
endpoint exclusion. CE-08 integrates this first return and its self-assessment.
The parent TRD owners and statuses are unchanged.

[interface]: 09_COMPLETE_SOURCE_AND_SCALED_ENERGY_TRANSFER_20261027.md
[prior]: 07_COLLISION_SCALE_RESOLUTION_AND_PROOF_MECHANISMS_20261027.md
[review]: ../reviews/05_COLLISION_ENERGY_FIRST_RETURN_SELF_ASSESSMENT_20261027.md
[continuation]: 11_COLLISION_ENERGY_FIRST_RETURN_CONTINUATION_20261027.md
[curvature]: ../../../investigations-4/12_height_dependent_heat_contours/notes/19_NEAR_AXIS_CLUSTER_AND_QUADRATIC_EXTERIOR_20261023.md
[poly]: https://arxiv.org/html/1904.12438v2#S3
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md

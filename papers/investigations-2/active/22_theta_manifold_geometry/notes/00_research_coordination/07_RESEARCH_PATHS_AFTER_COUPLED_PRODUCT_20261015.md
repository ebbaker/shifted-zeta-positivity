# Research priorities after the coupled theta product experiment

> **17 October 2026 — history routing update.** Historical formal-replay routing below is superseded. Chats [20](../../chat-histories/0020_2026-10-15T15-16-42Z_brainstorm-theta-geometry-paths.json) now use this investigation's [local registry](../../chat-histories/index.json), as recorded in the [relocation receipt](../../CHAT_HISTORY_RELOCATION_20261017.json). Original identities, provenance and public messages are preserved. All future Investigation 22 chats belong in this local history folder.

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6-astra**, reasoning effort **ultra**, verified from this turn's metadata. Three internal collaborators examined arithmetic constraints, collision scales and alternative representations. This is a research strategy note with elementary deductions and proposed experiments; it establishes no theta signed-core inequality or new numerical sign domain.

The best next investment is one explicit arithmetic identity for the complete stationary observation, with a bounded test that can reject it. The analytic collision criterion already tolerates much more than the preferred `delta=1/N` target suggests. Preserve that flexibility, test the proposed certificate's constraints before numerical optimization, and keep a separate practical project on the outer approximation. Additional geometric realizations and larger unconstrained parity matrices currently have lower expected value.

The starting documents are the [manuscript](../../manuscript/theta_manifold_geometry.tex), [continuation 06](06_COUPLED_PRODUCT_AND_REFLECTION_CONTINUATION_20261015.md), and its [review](../../reviews/07_COUPLED_PRODUCT_AND_REFLECTION_CONTROL_REVIEW_20261015.md). The manuscript's SHA-256 at this review is `114611f06f0928827045399561d2f83ca6ca9abc1d35a9d5cd7d406c845aa417`.

## 1. Use the most permissive adequate target

Put `W=h_j`, `S=h_(j+1)`, `E=H^2+H_x^2`, with `j=0,1`, and retain full stationarity `S(t,x)=0`. The exponential observation and its endpoint-only cutoff are

\[
A_{j,\delta}=W(t,x)^2-e^{-\delta}W(t,x)W(t,x+\delta),\qquad
A_{j,\delta,N}=W(t,x)^2-e^{-\delta}W(t,x)W_N(t,x+\delta).
\]

The [exponential-average note](../02_signed_turning_control/04_EXPONENTIAL_AVERAGE_AND_SHRINKING_CHORD_TARGETS_20261015.md) proves

\[
|A_{j,\delta}-A_{j,\delta,N}|
\le B_j(T_*)e^{-\pi(N+1)^2/4}\sqrt E
\]

on bounded upper heat-time ranges. At a multiplicity `2r+j` event `(T,a)`, its full stationary predecessor satisfies

\[
\frac{A_{j,\delta}(T-s,\chi(s))}{\sqrt{E(T-s,\chi(s))}}
\longrightarrow-d_{j,\delta},\qquad
d_{j,\delta}=e^{-\delta}|a_0|\delta^{2r}(1+O(\delta))>0,
\]

for every sufficiently small fixed positive `delta`, where `a_0=partial_x^(2r)W(T,a)/(2r)!`. The predecessor's entire short interval is zero-free for W.

**Sparse cutoff refinement.** Choose prescribed lengths `delta_k` tending to zero and, for each k, a prescribed unbounded cutoff subsequence `N_(k,l)`. Suppose, for every sufficiently large fixed k and arbitrarily large certified l,

\[
A_{j,\delta_k,N_{k,l}}
\ge-K_{j,k,l}E-\eta_{j,k,l}\sqrt E.
\tag{1}
\]

Each fixed-index coefficient must have a finite local bound through a hypothetical event, and each fixed-index domain must contain all sufficiently close full stationary predecessors and their whole interval. Require the local error bounds `eta_(j,k,l)` to tend to zero along the certified subsequence, for each fixed k. Then (1) excludes every covered finite multiple zero.

To prove this, choose k so the collision signal `d_(j,delta_k)` is positive. Choose one certified l so the sum of its residual bound and endpoint tail is less than half that signal. Hold both indices fixed and let `s` tend to zero. The term `K_(j,k,l) sqrt(E)` vanishes, contradicting the negative limit. There is no simultaneous cutoff/time limit, no required growth bound on K, and no requirement to certify every integer cutoff. The local error bounds must tend to zero uniformly over the starts in question; pointwise convergence away from the event is insufficient.

The two-parameter ordering is already present for smooth averages in [factor-preserving Note 03, section 5](../02_signed_turning_control/03_FACTOR_PRESERVING_AND_AVERAGED_CHORD_TARGETS_20261015.md). The refinements here are the explicit sparse-subsequence option and the following scale comparison.

| Certificate domain | Sufficient total coefficient of the square-root-energy error |
| --- | --- |
| Fixed `delta_k`, independent cutoff subsequence | Tends to zero for each fixed k |
| One length `delta_N=1/N` per cutoff | `epsilon_N=o(N^(-m))` for every fixed `m>0` |
| One length `delta_N=1/log(N+2)` per cutoff | Any bound `O(N^(-alpha))`, with fixed `alpha>0`, suffices |
| Known multiplicity `2r+j`, with `delta_N` tending to zero | `epsilon_N=o(delta_N^(2r))` suffices |

These follow by comparing the residual with `d_(j,delta_N)`. The logarithmic length is a new useful option if an arithmetic calculation supplies only algebraic convergence. Dyadic cutoffs can be used if the coefficient identity naturally follows the parity relation. These options relax the required decay rate; the two-parameter version asks for a broader certificate domain, so the full hypotheses are not ordered by strength.

On branch zero, stationarity gives `E=W^2`. For nonzero W the exact-core target is equivalent to

\[
e^{-\delta}\frac{W_N(t,x+\delta)}{W(t,x)}\le1+K_N.
\]

Thus the missing result controls the depth of a stationary extremum relative to a nearby value. Defining K from the measured minimum of E simply conceals this issue.

## 2. Test a certificate's constraints before searching for its coefficients

Continuation 06 proposes a nonnegative term plus a full-stationarity multiplier and a controlled remainder. Its nonnegative term must have an independent sign argument. Two elementary tests make that requirement more concrete.

### An affine nullspace test

Consider a finite-dimensional real-vector relaxation with coefficient vector c. Let its arithmetic and normalization constraints be `Rc=r`, and let full stationarity be `s dot c=0`. Write

\[
H=h\cdot c,\quad H_x=g\cdot c,\quad W=w\cdot c,
\quad V_N=b\cdot c,
\]

where `w=h` on branch zero and `w=g` on branch one. Suppose a fixed finite K makes

\[
Q(c)=W^2-e^{-\delta}WV_N+K(H^2+H_x^2)\ge0
\]

for every real c satisfying the constraints, and some admissible `c_*` has nonzero W. Then necessarily

\[
b\in\operatorname{rowspan}(R,s,h,g).
\tag{2}
\]

Indeed, any vector v annihilated by all four row sets leaves the constraints, complete starting jet and energy unchanged along `c_*+lambda v`. The value of Q changes by `-e^(-delta) lambda W(c_*) (b dot v)`. Both signs of arbitrarily large lambda are allowed, so `b dot v=0`. Finite-dimensional linear algebra gives (2). On branch zero `s=g`, so the redundant row can be removed.

This is a necessary condition for a certificate over unrestricted real vectors. It is not a no-go theorem for positive coefficient cones, nonlinear arithmetic constraints, or the actual theta family. If an ansatz fails (2), identify the additional restriction it uses rather than enlarging its positive-semidefinite matrix. If the admissible set is empty, the statement is vacuous; if W vanishes throughout it, the test says nothing about the signed cross term. A multiplier obtained by dividing by the stationary observation can disguise a vacuous argument away from stationarity.

### Primitive positivity also loses many directions

Before source differentiation, the mixed addition kernel on `q<=r` is

\[
K_{pk}=d_p d_k e^{\gamma pk},\quad
d_p=e^{-\pi(q+r)p^2/4},\quad \gamma=\pi(r-q)/2\ge0.
\]

On any finite parity block it is positive semidefinite, by the series

\[
e^{\gamma pk}=\sum_{m\ge0}\frac{\gamma^m}{m!}p^m k^m.
\]

This appears to offer a primitive alternative to the disproved source Gram matrix. However, convergence of the positive-time primitive product requires subtracting both zero axes `p=k` and `p=-k`, as [coupled Note 06, section 6](../03_theta_bundles_and_connections/06_COUPLED_THETA_PRODUCT_AND_PARITY_SECTORS_20261015.md) establishes.

At `q=r`, choose d distinct positive indices of the same parity, so the second axis is absent. The axis-subtracted matrix is exactly

\[
K^{\rm prim}=vv^T-\operatorname{diag}(v_p^2),
\qquad v_p=e^{-\pi q p^2/2}.
\]

Congruence by `diag(v)^(-1)` gives `11^T-I`, with one positive and `d-1` negative eigenvalues for `d>=2`. Strict negative directions persist on each fixed block for nearby `q<r`. A correction of rank at most b, combined with at most c independent linear constraints, cannot remove all negative directions once `d>b+c+1`: intersect the negative eigenspace with the correction's kernel and the constraint kernels.

This rules out that finite-rank primitive repair as a general Gram construction. It does not prove negativity of the integrated physical observation, and it does not assign finite rank to the actual primitive boundary terms. A renewed primitive approach must specify why its complete physical tests avoid these directions, or provide a correction outside this restricted class.

## 3. First priority is an explicit arithmetic adjoint identity

The coefficient recurrence is a useful available input:

\[
\Delta a_n=a_{n-1}-2a_n+a_{n+1}=0,\qquad a_0=1,
\quad\sum_{n\ge1}\beta_n a_n=\tfrac12,
\quad\beta_n=(4\pi n^2-1)e^{-\pi n^2}.
\]

Under the existing growth hypotheses these data force the theta coefficients. The [elliptic-shift note](../03_theta_bundles_and_connections/05_ELLIPTIC_SHIFT_CORE_AND_PROJECTION_OBSTRUCTION_20261015.md) proves the projected recurrence and the role of the endpoint. The next calculation should transfer this recurrence onto a test tailored to the endpoint observation, rather than simply reindexing the source.

A particularly explicit sufficient target is

\[
W_N(t,x+\delta_k)
=A_{k,l}H(t,x)+B_{k,l}H_x(t,x)
 +C_{k,l}h_{j+1}(t,x)+r_{k,l}(t,x),
\quad |r_{k,l}|\le\varepsilon_{k,l}\to0.
\tag{3}
\]

Here N is `N_(k,l)`, the coefficient rules are fixed from the source, and the coefficients are locally bounded through hypothetical events. For each fixed k the local error bounds must tend to zero along l, uniformly over admissible starts through the event. At full stationarity, `|W|<=sqrt(E)` yields

\[
A_{j,\delta_k,N}
\ge-e^{-\delta_k}(|A_{k,l}|+|B_{k,l}|)E
-e^{-\delta_k}\varepsilon_{k,l}\sqrt E.
\]

Thus (3) would suffice. It is an absolute endpoint reconstruction and can be stronger than necessary; failure of (3) must not be treated as failure of every one-sided arithmetic bound. Its advantage is that it makes the coefficient relation and remainder testable.

For a sequence of test quantities `J_n`, exact summation by parts gives

\[
\sum_{n=1}^M J_n\Delta a_n
=\sum_{n=1}^M a_n\Delta J_n
+J_1a_0-a_1J_0+J_Ma_{M+1}-a_MJ_{M+1}.
\tag{4}
\]

Let `H_n` be the physical transform of the nth source mode. The residual coefficients of (3) are

\[
r_n=\mathbf1_{n\le N}\partial_x^jH_n(t,x+\delta_k)
-A_{k,l}H_n(t,x)-B_{k,l}\partial_xH_n(t,x)
-C_{k,l}\partial_x^{j+1}H_n(t,x).
\]

Test one prescribed local source-mode or source-jet family for a representation

\[
r_n=\Delta J_n+\eta\beta_n+\rho_n.
\]

If the current decays sufficiently to justify the sums, theta gives

\[
\sum_{n\ge1}r_n=J_0-J_1+\eta/2+\sum_{n\ge1}\rho_n.
\tag{5}
\]

The lower boundary in (5) must cancel explicitly or be small by a proved source estimate; the upper boundary in a finite calculation also needs its own bound. The finite primitive endpoint is `sum_(n<=N) beta_n`, not `1/2`.

An automatic inverse of the second difference is not progress. For instance,

\[
J_n=\sum_{m>n}(m-n)r_m
\]

always solves `Delta J_n=r_n` when the sums converge, but `J_0-J_1=sum r_n` simply returns the unknown endpoint observation. Likewise, division by H, E or stationarity to manufacture A, B or C does not establish the required local boundedness.

The bounded deliverable is an exact formula with all lower boundaries and upper tails, an explicit arithmetic discriminator, and either a new remainder estimate or a proof that the selected family only repackages the original problem. A bilocal one-sided identity can remain preferable if the stronger linear reconstruction fails. In every representation retain the infinite endpoint strip, both physical exchange sectors, arithmetic parity recombination and the complete starting W.

### A finite positive coefficient alternative

A useful secondary experiment retains positivity of the coefficient weights rather than replacing them by unrestricted real vectors. Impose `a_n=1` for `1<=n<=N`, `a_n>=0` afterward, and the complete endpoint `sum a_n beta_n=1/2`. These are explicit relaxations of the theta coefficients. Put

\[
R_N=\sum_{n>N}\beta_n,
\qquad V_n(t,x)=\frac{(H_n(t,x),H_{n,x}(t,x))}{\beta_n}.
\]

A collision in this relaxation necessarily gives

\[
-\frac{\sum_{n\le N}(H_n,H_{n,x})}{R_N}
\in\overline{\operatorname{conv}}\{V_n:n>N\}.
\tag{6}
\]

Indeed `a_n beta_n/R_N` are nonnegative tail weights summing to one. A prescribed separating vector lambda therefore proves noncollision on any parameter region where

\[
\lambda\cdot\sum_{n\le N}(H_n,H_{n,x})
+R_N\inf_{n>N}\lambda\cdot V_n>0.
\tag{7}
\]

The tail cone must include its limit point `(1/8,0)`, since `V_n` tends to that point uniformly on compact real `(t,x)` sets. To see the normalization, let `p_n=e^u exp(-pi n^2 e^(4u))`. Then

\[
\int_0^\infty\phi_n\,du
=\frac18\left(\beta_n-\int_0^\infty p_n\,du\right),
\qquad \frac{\int p_n}{\beta_n}\longrightarrow0.
\]

The positive measures `phi_n(u)du/beta_n` concentrate at zero; multiplication by `exp(tu^2)cos(xu)` preserves the limit on compact parameter sets, while the first spectral derivative tends to zero. Their higher heat-weighted moments are uniformly bounded. More explicitly, with `lambda_n=pi n^2`, their densities are bounded by a constant times

\[
\lambda_n e^{9u-\lambda_n(e^{4u}-1)}.
\]

Splitting the exponent in half and using `e^(4u)-1>=4u` bounds the heat-weighted moment integral by an exponentially integrable density near zero times a bounded function with double-exponential decay. Thus

\[
C_j(T)=\sup_n\beta_n^{-1}\int_0^\infty u^j e^{Tu^2}\phi_n(u)\,du<\infty,
\quad |h_{j,a}-h_{j,\theta}|\le2C_j(T)R_N.
\]

The bound also justifies the physical transforms for the normalized positive tail relaxation without a polynomial-growth assumption on its weights. Define that relaxation through its convergent mode transforms: its source need not be smooth at u=0. This is absolute transform control, not relative control at a hypothetical zero of E. The bounded first task is to enclose the complete tail cone and derive one explicit separator on a small parameter box. A successful box is a finite-domain noncollision result, not the all-event signed bound. The cone may be a more productive discovery space than a generic Gram matrix, but its value must be tested against existing finite-certificate methods before building new infrastructure.

## 4. Shape the probe to the identity

The exponential average removes the endpoint derivative and should be the default first test. If the arithmetic identity instead needs source-frequency decay, retain a second prescribed probe

\[
\overline C_{j,\delta}
=W(t,x)\int_0^1\rho(v)
 [W(t,x+\delta v)-W_x(t,x+\delta v)]\,dv,
\]

with fixed nonnegative normalized smooth `rho` compactly supported in `(0,1)`. [Note 03](../02_signed_turning_control/03_FACTOR_PRESERVING_AND_AVERAGED_CHORD_TARGETS_20261015.md) proves the collision signal has size `delta^(2r-1)` and its endpoint kernel contains

\[
M_\rho(\delta u)=\int_0^1\rho(v)e^{i\delta uv}\,dv,
\]

which decays faster than every fixed inverse power of `delta u`. This is decay in source frequency, not automatically in spectral height x. The tradeoff is keeping an endpoint derivative and a less elementary average. Choose the probe from the candidate identity's needs; a new averaging kernel alone supplies no sign.

Generic positive-definite kernel reformulations require particular care. Csordas's [Theorem 3.7](https://arxiv.org/pdf/1309.0055) identifies positivity of an associated kernel hierarchy with Laguerre–Pólya membership under its stated admissibility and log-concavity hypotheses. This is a useful comparison for the strength of a proposed kernel theorem, not a positivity input for the present target. A new formulation should state whether it asks for substantially more than local stationary collision exclusion.

## 5. Keep a practical outer bridge as a separate project

The [outer-budget refinement](../06_effective_outer_bridge/01_LOW_INDEX_BUDGET_REFINEMENT_20261015.md) improves a constant by more than 3974, yet its sufficient conditional log-height still has a fixed component of 32,000,000. Its existing preliminary assumptions already require `L>=100002`, and the domain still has `tL>=61/24`. Since `x=4pi exp(L)`, extracting the missing exponent-pair constant alone cannot connect this argument to the existing finite certificate through `|x|<=112`.

The next outer task should retain an effective finite Riemann–Siegel expression and differentiate a complete analytic remainder directly, testing whether this reduces the present disc/differentiation losses. Polymath's [effective approximation, Theorem 1.3](https://arxiv.org/html/1904.12438), is a concrete baseline: it treats the same heat-flow normalization with explicit errors in a region beginning at `x=200`. It is an approximation theorem, not a signed stationary bound at that height. Any adaptation must restore physical derivatives and full stationarity after normalization, and handle changes of the Riemann–Siegel cutoff.

Choose a feasible pilot interval and a stated overlap target before a wide computation. First derive enough error control for the required physical jets or for a direct noncollision test. Then certify a bounded interval. If the analytic budget cannot support the proposed overlap, stop and redesign it. The small-time region and the inner region `tL<61/24` remain independent coverage obligations. The local collision criterion needs finite bounds near each positive-time finite-height event; it does not require one constant bounded as time tends to zero or height tends to infinity. It does require that every such event be covered.

## 6. Order the next research cycle by its decision points

| Order | Task | Deliverable that warrants continuing |
| --- | --- | --- |
| 1 | Fix one arithmetic multiplier/current family and a flexible probe/cutoff domain | Explicit constraints, rank test and exact boundary identity |
| 2 | Derive its complete remainder on both stationary branches | A bound retaining W, with errors adequate for the chosen spatial scales |
| 3 | Test the same rule against existing controls | Identify the precise failed arithmetic premise for each control, rather than fit its sign |
| 4 | Run a small validated theta pilot only for a surviving rule | Full stationary-root isolation, whole-interval conditions, complete tails and independently prescribed coefficients |
| 5 | In parallel, redesign and benchmark the practical outer approximation | A concrete overlap budget and an honest statement of the uncovered domain |

Use the asymmetric heat germs, weighted-square collisions, projected ramp family and reflected quartic-source collision for distinct purposes. The ramp tests projection information and is not a certified collision example. A control need not satisfy the new arithmetic hypothesis; the calculation must show exactly where it ceases to qualify.

Pause larger parity-matrix sweeps, bounded normalized scalar shifts, another isolated endpoint constraint, and new holonomy constructions unless they bring an explicit estimate absent from the present work. Negative results here close specified ansatz classes, not all arithmetic methods.

The manuscript and existing overview remain unchanged. The deductions above have elementary analytic proofs and internal collaborator checks; no new numerical certificate or global theta theorem is claimed. This conversation is registered separately as formal-replay history 20, preserving histories 18 and 19.

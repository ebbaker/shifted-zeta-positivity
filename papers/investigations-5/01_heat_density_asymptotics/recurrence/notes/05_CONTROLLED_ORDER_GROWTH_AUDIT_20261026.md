# R05: controlled order growth, retained tails, and outer accuracy

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual effort ultra**,
verified from this turn's rollout metadata. Recurrence chat0001, thread
`01a17690-2e5f-77b1-a3a4-9c31f72c117d`.

**Return: HDA-R05-AN01 r1. Proved in-note from named classical inputs;
same-model internal analytical assessment only.** For every fixed finite
c>0 the unabsorbed error ledger below holds simultaneously for all integers
`1<=p<=cL`, `K=2p`, on the full buffered slab `1<=T<=2`, after one common
height onset. The old fixed-p theorems are not invoked with changed
quantifiers: their finite local bounds and actual constants are re-audited.

An upper order cap alone does not promise outer decay. For a chosen
\[
 p(X)=\lfloor aL\rfloor,\quad 1/8<a\le c,\qquad L=\log(X/(4\pi)),
\]
and every declared
\[
 0<\eta<\min(a-1/8,127/8),
\]
the canonical comparison in the **outer-envelope (3,1) norm** is eventually
\[
 \boxed{\|h-F_X^{[p,2p]}\|_{o;X;1,2}^{(3,1)}\le e^{-\eta L^2}}.
\tag{G1}
\]
In particular, the concrete choice **p=floor(L/2), K=2p** pays
**e^-L²/4** in that norm. Every arithmetic mode and the bounded real RS
completion remain. The residual and its first spatial derivative are
exactly zero for each frozen chart. The range is sufficient, not sharp;
no actual-error lower bound, infinite-series convergence or useful runtime
claim follows. [Actual inputs][inputs], [packet][packet] and
[assessment][review] identify the evidence. No manuscript, numerical,
machine-symbolic, sampling or interval work is included.

## 1. Frozen contract, norms and retained source

Keep the complete canonical theta source, `h(T,z)=H(-T,z)`, `h_T=h_zz`,
`H(0,z)=xi((1+iz)/2)/8` and the exact gamma factor
`M(w)=w(w-1)pi^(-w/2)Gamma(w/2)/16`. Use the definitions of the two arms,
`b_epsilon,n`, `lambda_epsilon,n`, `c_epsilon,r`, `Q_T`, the U_j hierarchy
and the partition polynomials P_p from [Note02][n2] and [Note03][n3]. All
`1<=n<=N=floor(sqrt(X/(4pi)))` and epsilon=+1,-1 remain. Fix
\[
 R=r+1,\quad Y=b+1,\quad W=R+Y,\quad V=8\sqrt2 L,
 \quad I_X=[X-V,X+V].
\tag{G2}
\]
The physical choice remains `r=ell+2`, `b=1+h_av+2`. Prove field errors
on Omega_X(R,Y) and use fixed-radius Cauchy for the target Omega_X(r,b).

For each X select a finite integer p in the stated range, then freeze X,
p, K=2p, N, gamma derivatives, coefficient data, window and real partitions
under **both** z and T differentiation. Choosing X=Re z afresh during
spatial differentiation would give a different, nonholomorphic construction
and is excluded. No derivative in X or global spatial stitching is claimed.

Retain exactly
\[
 F_X^{[p,2p]}(T,z)=\sum_{\epsilon=\pm1}\sum_{j=0}^p U_{\epsilon,j}(T,z-X)
            +\int_{I_X}k_T(z-u)Q_{X,2p}(u)du,
\tag{G3}
\]
where `Q_X,2p=S_m(u)-S_N+R_m(u),2p`. The correction has all RS
coefficients through 2p and **exact** adjacent-cutoff transfer. Real parts
stay inside the real initial data, and their partitions are independent
of z,T. No true gamma or RS function is extended along an artificial ray.

The natural norm divides the maximum of spatial derivatives 0--3 plus
first T derivative by |G(z)|, as in the continuation. Define the outer
norm by the identical numerator divided instead by the positive envelope
`E_o(-T,z)=|C_+|+|C_-|` of [ansatz Note03][a3]. This is not division by h
or a cosine. The existing gamma/outer calibration, on this fixed slab and
full target buffers, gives
\[
 E_o(-T,z)\ge c_o|G(z)|e^{-TL^2/16+\pi^2T/64}.
\tag{G4}
\]
Consequently outer division costs at most `c_o^-1 exp(L²/8)` times the
natural norm. The onset for this comparison is retained below. On the
real axis this is the amplitude envelope; off axis it retains both arms.

## 2. The actual finite local and source costs

Use the analytic, simultaneous-in-r coefficient bound from Note02:
`|c_r|<=A D^(r-1)X^-r`, A>=1,D>=4. It was derived by Cauchy on ell''
in a disk of radius comparable to X; fixed-r asymptotic notation alone
would not be sufficient here. For `DV/X<=1/2`, `2AV²/X<=1`, Note03's
finite Taylor proof works for **each actual integer p**, with its displayed
constant and no other p-dependent local hypothesis:
\[
 |A(q)-P_p(q)|\le eX^{-(p+1)}B_{p+1}(|q|),\quad
 B_m(x)=\sum_{k=1}^m\frac{2^{m+k}A^kD^{m-k}}{k!}
                              {m-1\choose k-1}x^{m+k}.
\tag{G5}
\]
There is no truncation of a whole-line infinite series. Define also the
actual coarse polynomial-tail majorant
\[
 C_j(x)=\sum_{k=1}^j\frac{A^kD^{j-k}}{k!}{j-1\choose k-1}x^{j+k},
 \qquad H_p(x)=1+\sum_{j=1}^pC_j(x).
\tag{G6}
\]
For X>=1, `|P_p(q)|<=H_p(|q|)`. Dropping X^-j here is a recorded
conservative bound, not the claimed actual size of a retained level.

The **actual** local moment constants at tau=1,B=2 are
\[
 M_m=\sqrt2 e^{R+Y^2/4+4}
       \sum_{k=0}^m{m\choose k}W^{m-k}4^k
                      \frac{\Gamma((k+1)/2)}{\sqrt\pi},
 \qquad M_m^t=M_m/2+M_{m+2}/4.
\tag{G7}
\]
They bound the weighted kernel moments with exp(|u-X|), including the
complex exponential exp(Y²/4). The time version follows from exactly
`partial_T k=[(z-u)^2/(4T²)-1/(2T)]k`. The local direct-time degree is
2p+4. The full initial population is still
`C_pop G(X)X^1/4 exp(|q|)`, `C_pop=4(4pi)^(-1/4)`. Thus the entire
population cost and the weighted local error combine as X^-(p+3/4).
No q power is replaced by V before integration.

For the real canonical mismatch with K=2p retain exactly
\[
 C_{2p}=C_\Gamma\frac{2^{7/4}}7\Gamma(p+1/2)
                         1.1^{2p+1}(8\pi)^{p+3/4}.
\tag{G8}
\]
It multiplies `G(X)exp(|q|)X^-(p+3/4)` on u>=X/2. The arbitrary-positive-
integer K quantifier in [Polymath v2 Proposition6.2, (56)][rs] was rechecked
for this growing-order use at real sigma=1/2, Tprime=u/2>0; it imposes
no extra upper K restriction there. The underlying coefficient provider
remains a classical import, not a new verified implementation. The
separate gate `2p<=a_min²` controls the size of the retained finite
coefficient sum by Note05's odd/even ratio argument. No positive-time
Proposition6.3 or differentiated scalar RS allowance is imported.

Write the exact source/local field-and-time prefactor
\[
 Q_p=48\{C_{2p}M_0+C_{\rm pop}eB_{p+1}[M]\}
          +C_{2p}M_0^t+C_{\rm pop}eB_{p+1}[M^t].
\tag{G9}
\]
Polynomial evaluation [M] replaces x^j by M_j. The 48 is the maximal
`a!2^a`, 0<=a<=3, from radius-1/2 Cauchy on the enlarged chart; direct
T is paid separately, before the error heat equation is used.

## 3. Simultaneous logarithmic bound, not a fixed-p substitution

Let
\[
 E=\max\{1,\sqrt2e^{R+Y^2/4+4},4\sqrt2e^{Y^2/4}\},
 \quad S=\max\{1,W+4,16\sqrt2\},\quad C=\max(1,A,D).
\tag{G10}
\]
For the inherited tail moments D_m of Note02 (before the refinement below),
`M_n,D_n<=E n! S^n` and `M_n^t,D_n^t<=E(n+2)!S^(n+2)`. To check this,
`Gamma((n+1)/2)/sqrt(pi)<=n!` follows separately at even and odd integers
by the gamma recurrence; then use the binomial formula in M_n. Every
constant is fixed by the slab and buffers, independently of p and X.

For m=p+1, grouping the **finite** binomial sums in G5--6 proves
\[
 B_m[M]\le E(8CS^2)^m(2m)!,\quad
 B_m[M^t]\le ES^2(8CS^2)^m(2m+2)!,
\]
\[
 \max\{H_p[D],H_p[D^t]\}
          \le ES^2(p+1)(2CS^2)^p(2p+2)!.
\tag{G11}
\]
For example, in B_m bound `(m+k)!<=(2m)!`, `S^(m+k)<=S^(2m)` and
`sum_{k=1}^m binom(m-1,k-1)/k!<=2^(m-1)`; no dependence on the actual
order is declared fixed. Moreover
\[
 C_{2p}\le C_R Q_R^p p!,\quad
 C_R=C_\Gamma\frac{2^{7/4}}7\sqrt\pi\,1.1(8\pi)^{3/4},\quad
 Q_R=1.1^2(8\pi),
\tag{G12}
\]
because `Gamma(p+1/2)<=sqrt(pi)p!`. These factorial majorants are
supplementary upper bounds; G7--9 and the original gamma factor remain
the actual cost ledger.

For explicit simultaneous logarithmic constants set
\[
 Q=\max(1,8CS^2,2CS^2,Q_R),\quad T_0=\max(1,ES^2,C_R),
\quad J(p)=T_0(p+2)Q^{p+1}(2p+4)!.
\tag{G13}
\]
Each cost on the left of G11, and C_(2p), is <=J(p), and
\[
 \log J(p)\le C_*(p+1)\log(p+2),\quad
 C_*=6+\log Q+\log T_0.
\tag{G14}
\]
Indeed `2p+4<=3(p+1)`, `log(2p+4)=log2+log(p+2)` and
`log(p+2)>=log3>1`; bounding n! by n^n proves G14. In particular
`Q_p<=C_Q J(p)`, with the fixed sufficient
`C_Q=48(M_0+C_pop e)+(M_0^t+C_pop e)`.
This establishes `log^+ Q_p=O((p+1)log(p+2))` before using p<=cL.
Thus `log^+ Q_p=O_c(L log L)`, rather than an unexamined O_p(1).

## 4. Preserve the failed old absorption; pay the actual tails

The old sufficient gate absorbing artificial tails all the way into
X^-(p+3/4) was `L²>=(p+1)log X+log^+ A_art,p`. It is **not** a
structural hypothesis for the local/source estimates. At
`p=floor L`, `p+1>L` and `log X=L+log(4pi)>L`, so this gate fails
already without its positive constant. Uniform reuse of that old
absorbed-rate gate works for fixed c<1, not for c>=1. This preserves a
precise failed estimate, not a failure of the canonical model or audit.

Retaining the inherited unabsorbed `e^-L²` tail instead gives
\[
 \|E\|^{(3,1)}_{X;1,2}\le C_\chi\left\{
 Q_p X^{-(p+3/4)}+49(A_{\rm mod}X^{P-7/4}
               +A_{{\rm art},p}X^{1/4})e^{-L^2}
 +49A_{\rm far}X^{-7/4}e^{\pi X/8-X^2/256}\right\}.
\tag{G15}
\]
Here `P=4`, `A_mod,A_art,p,A_far` are the actual D/J-polynomial constants
in Note04. G11 controls A_art,p, including degree 2p+2 for direct time.
The factor 49=48+1 pays the same tail for Cauchy spatial derivatives
and direct time. G15 is uniform up to any fixed cL after the structural
onset, without the failed absorption gate.

With p=floor(aL), G15 alone pays every
`eta<min(a-1/8,7/8)`. Its 7/8 tail ceiling is a loss of the inherited
conservative Gaussian split, not an intrinsic barrier. The following
routine refinement keeps the same window and model and records its
larger constants explicitly.

Fix `0<theta<1`, put `delta=(1-theta)/2`, `t_R=1+R/4`, and for m>=0 set
\[
 D_m^{\theta}=\frac{e^{Y^2/4+2t_R^2/\delta}}{\sqrt{4\pi}}
     2^m(8/\delta)^{(m+1)/2}\Gamma((m+1)/2),\quad
 (D_m^{\theta})^t=D_m^{\theta}/2+D_{m+2}^{\theta}/4.
\tag{G16}
\]
For |q|>=V, |Re d|<=R and 1<=T<=2,
\[
 -\frac{(q-\Re d)^2}{8}+|q|
 \le-\frac{q^2}{8}+t_R|q|
 \le-\frac{(1-\delta)q^2}{8}+\frac{2t_R^2}{\delta}
 =-\frac{\theta q^2}{8}-\frac{\delta q^2}{8}
                                      +\frac{2t_R^2}{\delta}.
\tag{G17}
\]
Use `V>=W` to bound `|z-u|<=2|q|`. Extract
`exp(-theta V²/8)=exp(-16theta L²)` and integrate the remaining Gaussian
against `(2|q|)^m`. This proves the tail and direct-time moments G16.
Define
\[
 A_{\rm mod}^{\theta}=C_{\rm tail}
                \max(D_0^{\theta},(D_0^{\theta})^t),\quad
 A_{{\rm art},p}^{\theta}=C_{\rm pop}
                  \max\{H_p[D^{\theta}],H_p[(D^{\theta})^t]\}.
\tag{G18}
\]
The true moderate tail uses its actual height exponential up to |q|=X/2
and still costs `X^(P-7/4)`; artificial tails retain the **full** X^1/4
population and H_p. Only remote true data use the global source bound,
with the already paid `A_far X^-7/4 exp(pi X/8-X²/256)`. Thus G15 holds
also with `(A_mod,A_art,p,e^-L²)` replaced by
`(A_mod^theta,A_art,p^theta,e^(-16theta L²))`.

This refinement adds an explicit cost `exp(2t_R²/delta)` and powers of
`delta^-1/2`. It is not a free sharpening. Set
\[
 E_\theta=\max\{1,\sqrt2e^{R+Y^2/4+4},
                 e^{Y^2/4+2t_R^2/\delta}\sqrt{2/\delta}\},\quad
 S_\theta=\max\{1,W+4,4\sqrt{2/\delta}\}.
\tag{G19}
\]
Then G11--14 apply with D^theta,(D^theta)^t replacing the inherited
tail moments and E_theta,S_theta replacing E,S. In particular
`log^+ A_art,p^theta=O_theta((p+1)log(p+2))`, with the explicit J_theta
construction. Theta is fixed before X tends to infinity; no endpoint
uniformity as theta->1 is asserted.

## 5. Common structural onset and outer target gates

For each fixed c,r,b (and fixed theta if using G16) choose one common
X_0 satisfying the original real RS/sectorial gamma onsets and:

| Payment | Sufficient gate, simultaneously for 1<=p<=cL |
| --- | --- |
| Chart and full extra analytic margin | L>=16, X>=max(1,4(R+Y+1)), V<=X/4 |
| Canonical real window | X-V>=X/2, a(X+V)-a(X-V)<1; optionally retain V<=log²X |
| All retained RS terms | 2cL<=(X-V)/(4pi)=a_min² |
| Weighted local remainder, all orders | DV/X<=1/2, 2AV²/X<=1 |
| Full arithmetic slope/heat damping | D0/X<=1-pi/8; 2{(D0/X)(pi/4+L/2)+D0²/X²}<=1 |
| Original/strengthened tail geometry | V>=max(2R,W+1,64) |
| Outer gamma/envelope calibration | C_cal (1+L)/X<=1, for its fixed classical C_cal |

Every gate is eventual for each fixed finite c and fixed buffers. The
only growing retained-order gate has been replaced by its **worst case**
2cL, rather than asserted separately at p-dependent onsets. The exact
source remainder is valid for every positive integer K; the coefficient
sum's odd/even ratios remain bounded at K<=a_min². No coefficient or
provider cost is removed by this onset.

For completeness the full all-mode shifted moments also remain under
control simultaneously. Use Note03's exact Pi_d and Z_m. Their finite
factorial sums give, for some fixed K_0,K_1>=1,
\[
 Z_m\Pi_m\le K_0 K_1^m (m!)^2,\qquad m\ge0.
\tag{G20}
\]
For an explicit choice, let Pi_pref be the fixed prefactor of 4^m W_m
in Note03 R2.10. The same half-gamma bound gives
`Pi_m<=Pi_pref(1+sqrt(8pi)/2)m![12(1+sqrt(8))]^m`.
Also `Z_m/m!` is the m-th coefficient of the positive-coefficient
function `exp((W+4)s+2s²)`, hence `Z_m<=m!exp(W+6)` by evaluating
its sum at s=1. Take `K_0=Pi_pref(1+sqrt(8pi)/2)exp(W+6)` and
`K_1=12(1+sqrt(8))`. Grouping the finite level coefficients in Note03 then bounds
level j by `G(X)X^(1/4-j) exp(O((j+1)log(j+2)))`. No arithmetic modes,
near-cutoff shell, displacement `d+2Tlambda`, or finite-order moment
cost is lost. This bound is separate from the more economical initial-
population error comparison used in G9.

Define `C_o=C_chi/c_o` and fix eta>0. Besides the structural gates,
the following four **displayed inequalities** suffice for G1 using G16:
\[
 (p+3/4)\log X\ge(\eta+1/8)L^2+\log^+(4C_o Q_p),
\]
\[
 (16\theta-\eta-1/8)L^2\ge
       (P-7/4)\log X+\log^+(196C_o A_{\rm mod}^{\theta}),
\]
\[
 (16\theta-\eta-1/8)L^2\ge
       \tfrac14\log X+\log^+(196C_o A_{{\rm art},p}^{\theta}),
\]
\[
 X^2/256\ge\pi X/8+(\eta+1/8)L^2
                              +\log^+(196C_o A_{\rm far}).
\tag{G21}
\]
Each line allocates at most one quarter of e^-eta L² after outer
conversion. The last line safely drops the favorable X^-7/4. These
are sufficient analytical onset conditions, not evaluated numerical X0s.

For p=floor(aL), `log X=L+log(4pi)` and G14,19 give, uniformly,
\[
 \log(\hbox{outer source/local allowance})
                       \le-(a-1/8)L^2+O_a(L\log L),
\]
\[
 \log(\hbox{outer moderate/artificial allowance})
                       \le-(16\theta-1/8)L^2+O_{a,\theta}(L\log L).
\tag{G22}
\]
The true moderate term alone has only O_theta(L) after its leading
quadratic exponent. The remote exponent is much more negative. Strict
margins `eta<a-1/8` and `eta<16theta-1/8` make G21 eventual. Choosing
any fixed theta with `(eta+1/8)/16<theta<1` proves G1. This is the
new simultaneous estimate required for order growth.

A concrete selection needs no optimized endpoint: `c=1/2`,
`p=floor(L/2)`, `theta=1/2`, `eta=1/4` has positive margins in all four
lines of G21. It uses `2p<=L`, `K=2p`, and still keeps the bounded integral
and every n<=N. Even the inherited conservative tails suffice for this
particular target. No fitting, trial heights or numerical optimization
entered the choice.

## 6. Actual derivatives, failed boundaries and evaluation cost

At every selected finite p and K, `[partial_T-partial_z²,Q_T]=0`;
base carriers solve heat, and Q's initial data/endpoints are fixed.
Therefore, exactly,
\[
 (\partial_T-\partial_z^2)F_X^{[p,2p]}=0,\qquad
 \partial_z(\partial_T-\partial_z^2)F_X^{[p,2p]}=0.
\tag{G23}
\]
The field comparison, direct differentiated-kernel costs and full buffers
were established before using E_T=E_zz. Selecting p(X) does not authorize
differentiating that selection in z or replacing X by Re z. The source
mismatch is still independently paid by G8.

Preserve the following limits and failed estimates:

| Attempt or boundary | Exact disposition |
| --- | --- |
| Substitute p(X) into an O_p(1) theorem | Invalid without G11--14 and common onsets; the present audit supplies them. |
| Use only p<=cL to promise outer decay | Insufficient: p=1 remains permitted. A lower growth prescription is needed. |
| Reuse old e^-L² tail absorption at p=floor L | Fails `(p+1)log X>L²`; bypassed by unabsorbed G15. |
| Treat 7/8 as an intrinsic outer ceiling | False inference from a conservative split; G16--19 improve that ledger. |
| Chosen p=floor(aL) with a<=1/8 | No positive eta paid by G21; at equality the order-cost term remains unpaid. No actual-error lower bound. |
| eta at/above min(a-1/8,127/8) | No result from these strict-margin bounds. The first unpaid inequality is the source/local line or tail lines of G21; no universal exclusion is proved. |
| Let c, buffers, time endpoints or theta vary with X | Outside the stated quantifiers; requires another simultaneous audit. |
| Infinite whole-line hierarchy or monotone improvement | Not proved by a finite growing-order truncation. |

The formal descriptor has, per arm, p logarithmic gamma derivatives and
an aggregated polynomial of degree <=2p. RS uses 2p+1 coefficient functions;
N~sqrt(X/(4pi)) remains. Exact polynomial recurrence can form all levels
in O(p³) scalar arithmetic and O(p²) coefficient storage, or retain just
the aggregated polynomial with O(p) output storage. This counts unit-cost
operations once the named inputs are supplied; it does not count their
evaluation. Gaussian moments obey
`H_m(t,T)=t H_(m-1)+2T(m-1)H_(m-2)` with H0=1,H1=t. Thus the arithmetic
sum can be assembled in O(Np) further scalar operations plus N carrier
and lambda inputs, with the required fixed spatial jets at the same
asymptotic arithmetic count. The bounded RS integral still needs its
classical providers and a quadrature/error analysis.

For p=floor(L/2), the retained arithmetic polynomial has degree
2p<=L and K<=L. Direct-time local allowances use moments through
2p+4<=L+4; artificial direct-time tails use moments through
2p+2<=L+2. The older
[Note05 growing-degree construction][a5] used J=ceil(3L), K=ceil L to
pay the same stated e^-L²/4 outer target. This is a different truncation
and a smaller sufficient retained polynomial degree, not a proof of faster evaluation,
reduced working precision, fewer arithmetic modes or minimal order.

No numerical onset, coefficient-provider complexity, finite-precision
stability, quadrature node count or useful runtime is established. The
next actual evaluation error would have to be added to G15 **before**
outer division. An aggregate natural-scale evaluation error delta_eval
costs at most `c_o^-1 exp(L²/8)delta_eval` in the outer norm. Consequently
a sufficient extra half-budget for an eta target is
`delta_eval <= (c_o/2) exp(-(eta+1/8)L²)` after reserving the other half
for truncation. One explicit reservation replaces 4,196 in G21 by
8,392, making each of its four truncation payments at most one eighth
of the target. This is an error requirement, not an implementation or
necessary precision lower bound. An upper bound for that evaluator defect,
including coefficient inputs and the retained RS integral, is the first
unpaid cost step. No evaluation campaign is authorized here.

## 7. Scope, controls and disposition

This is an approximation milestone under [avoid01][a01], not an RH
criterion. Carry the [result index][results], [heat cluster][heat],
[collision controls][controls] and [avoid index][avoid], especially
[shared premises02][a02], [scope07][a07] and [separate bounds12][a12].
The analytical premise screen is unchanged: Euler-factor and finite-prime
perturbations fail the full unchanged coefficients; weighted-square/cutoff
controls fail the same canonical xi/RS identity; reflected, smooth and
positive-primitive controls lack the complete canonical gamma/arithmetic
completion. The recurrence and heat identity also hold for suitable
controls and exclude no collisions. No physical/regulator transfer,
positive-time or growing-time extension follows.

**Disposition — Analysis, Sol:** accept G1--23 with [Review04][review],
from named inputs and same-model internal assessment only. R05-AN01 r1
CLOSED; the requested controlled-order-growth audit Complete. Broad R05
remains **Partial**, because evaluator/precision/quadrature cost and
other regroupings remain open. HDA-A02 remains Partial; HDA-17 Partial,
HDA-18 Gated and HDA-20 unfulfilled remain. The prior fixed-p and fixed-
compact-family statements retain their original scope; this is a new
separately assessed order-growth theorem on [1,2], not an endpoint extension.

**Next concrete deliverable — Analysis, Sol, not executed:** an analytical
coefficient/evaluator and bounded-RS-integral error budget for the declared
choice p=floor(L/2), K=2p and outer target e^-L²/4, including full buffers
and jets/time. Derive a sufficient perturbation/precision/quadrature
specification or identify the first uncontrolled provider/conditioning
term. This is a recommendation for a new request, with no manuscript or
numerical implementation started.

[inputs]: 05_CONTROLLED_ORDER_GROWTH_INPUTS_20261026.json
[packet]: ../research-progress/handoffs/HDA-R05-AN01.md
[review]: ../reviews/04_CONTROLLED_ORDER_GROWTH_ASSESSMENT_20261026.md
[n2]: 02_FIRST_FINITE_FLUCTUATION_COMPARISON_20261026.md
[n3]: 03_FIXED_ORDER_FLUCTUATION_HIERARCHY_20261026.md
[n4]: 04_COMPACT_TIME_RECURRENCE_FAMILY_20261026.md
[a3]: ../../ansatz/notes/03_OUTER_CORRECTION_AND_SIGNED_REAL_BRIDGE_20261025.md
[a5]: ../../ansatz/notes/05_FIXED_NEGATIVE_TIME_REPRESENTATIONS_20261025.md
[rs]: https://arxiv.org/html/1904.12438v2#S6.SS2
[results]: ../../../../../result-summaries/README.md
[heat]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md

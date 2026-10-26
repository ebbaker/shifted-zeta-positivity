# First negative-time evolution correction with a retained RS integral

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), recorded effort ultra**,
verified from turn metadata. Ansatz chat0003, thread
`01a17626-abf5-7a90-9ba2-7a2395254aee`.

**Status: proved in-note from named classical inputs; same-model internal
analytical assessment only.** Return to [HDA-A02-AN03 r1][packet]. On
`t=-T`, `1<=T<=2`, one evaluated quadratic evolution correction, together
with one further RS initial term, improves the natural-scale field,
spatial derivatives through three and direct first time error from
`C |G| X^-3/4` to **`C |G| X^-5/4`**, without logarithmic losses. Its
actual heat residual and first spatial derivative are `C |G| X^-7/4`.

The representation has **fixed gamma/RS orders, all N arithmetic modes,
and one bounded integral of explicit real RS correction data and exact
adjacent transfers**. It is not an integral-free elementary short formula.
The arithmetic evolution correction is evaluated; no full unevaluated
Duhamel correction is used. Outer-relative accuracy still fails at fixed
T. No numerical, sampling, fitting, machine-symbolic, exact-arithmetic or
interval research was run. The [opening manifest][inputs] pins inputs;
the [assessment][review] records limits and same-model checks.

## 1. Frozen contract and imported data

Keep the complete canonical source and exact normalization
\[
H_t=-H_{zz},\quad H(0,z)=\xi((1+iz)/2)/8,\quad
M(w)=w(w-1)\pi^{-w/2}\Gamma(w/2)/16,\quad\alpha=M'/M.
\tag{EC1}
\]
Keep physical `q=epsilon_g^2`, fixed `K=k_ell k_h`, the additive physical
potential, actual signed covariance, and joining/regulator defects. No RH,
simplicity, noncollision or positive unknown remainder is assumed.

Fix `r=ell+2`, `b=1+h+2`, and prove field bounds on the enlarged chart
\[
\Omega_X^+=\{|\Re z-X|\le r+1,\ |\Im z|\le b+1\},\quad
\Omega_X=\{|\Re z-X|\le r,\ |\Im z|\le b\}.
\]
Further fixed enlargements used in Cauchy estimates are allowed before
choosing the onset. Freeze at the real center
\[
L=\log(X/(4\pi)),\quad a_X=\sqrt{X/(4\pi)},\quad
N=\lfloor a_X\rfloor,\quad V=8L,\quad I_X=[X-V,X+V].
\tag{EC2}
\]
Every endpoint, initial partition and cutoff is independent of target z
and T. On the right half-plane use branches continued from positive real
height and
\[
G(z)=[M(s(z))M(1-s(z))]^{1/2},\quad s(z)=(1+iz)/2,
\]
positive on the real segment. It is nonzero on these far-height charts,
`|G(z)|` is comparable to `G(X)`, and `G'/G=-pi/8+O(X^-1)`.
Evenness supplies left charts after proving the right-chart result.

Imported facts are precisely [Note05 FN4, FN12--15 and FN27][n05], with
the initial RS order now **K=1**, and sectorial gamma bounds as in
[Note03 CB4][n03]. The exact real-initial-value identity is
\[
H(-T,z)=\int_{\mathbb R} k_T(z-u)H(0,u)\,du,\qquad
k_T(v)=(4\pi T)^{-1/2}e^{-v^2/(4T)}.
\tag{EC3}
\]
Its function class here is the canonical Fourier transform of the
integrable complete source, bounded on the real initial line; Gaussian
Fubini and kernel differentiation are justified. All approximating real
initial data below are bounded on the compact I_X and piecewise given.
Their truncated heat transforms and all displayed derivatives exist.

The primary source [Polymath v2, (36)--(38) and Proposition6.2][poly]
was reopened: only its real initial `sigma=1/2`, K=1 formula is imported,
not its positive-time evolved estimate. For real u in I_X let
\[
a_u=\sqrt{u/(4\pi)},\quad m=m(u)=\lfloor a_u\rfloor,\quad
p_u=1-2(a_u-m),\quad s_u=(1+iu)/2,
\]
\[
U_u=e^{-i\{(u/4)\log(u/(4\pi))-u/4-\pi/8\}},
\]
and retain the named coefficient functions of that proposition:
\[
R_{m,1}(u)=2\Re\left\{(-1)^{m-1}M(s_u)U_u a_u^{-1/2}
  [C_0(p_u)+a_u^{-1}C_1(p_u,1/2)]\right\}.
\tag{EC4}
\]
The real part is inside real initial data. The imported bounds give
`|C0|<=1/2`, `|C1|<=3 sqrt(2)/(4 sqrt(pi))` and
\[
|H(0,u)-S_{m(u)}(u)-R_{m(u),1}(u)|
\le {2^{7/4}1.1^2\over7}G(u)a_u^{-5/2}
\le C G(u)X^{-5/4}.
\tag{EC5}
\]
Here `S_m` is the complete two-arm exact-gamma arithmetic sum of CB16.
This fixes sign and normalization through the exact contours and FN12.
The coefficient construction is imported through the inspected Polymath
restatement; no independent audit of the underlying Arias paper or
coefficient-provider complexity claim is made. No analyticity, derivative
or endpoint-parity estimate for C1 is needed.

Retain the exact adjacent transfer by defining
\[
Q_{X,1}(u)=S_{m(u)}(u)-S_N(u)+R_{m(u),1}(u),\qquad
\mathcal I_1(T,z)=\int_{I_X}k_T(z-u)Q_{X,1}(u)\,du.
\tag{EC6}
\]
The eventual gate `a(X+V)-a(X-V)<1` permits at most one threshold.
The arithmetic transfer in EC6 is exact, not replaced by CB15's
lower-order recurrence allowance. `|Q_{X,1}(u)|<=C G(u)X^-1/4`.
Possible jumps of the truncated RS data at isolated thresholds have
measure zero and do not move when z,T are differentiated. Thus
\[
(\mathcal I_1)_T=(\mathcal I_1)_{zz}
\tag{EC7}
\]
exactly. Retaining this integral avoids an unproved fixed-N analytic
extension of C1 and an unproved higher-order transfer recurrence.

## 2. Derive the first correction from the product evolution equation

For `epsilon=+1,-1`, `n<=N`, put
\[
w_\epsilon=(1+\epsilon iz)/2,\quad h_{\epsilon n}=M(w_\epsilon)n^{-w_\epsilon},
\quad \beta_{\epsilon n}=\partial_z\log h_{\epsilon n}
 ={\epsilon i\over2}(\alpha(w_\epsilon)-\log n),
\]
\[
\gamma_\epsilon=\beta_{\epsilon n}'=-\alpha'(w_\epsilon)/4,\quad
\eta_\epsilon=\beta_{\epsilon n}'',\quad
\zeta_\epsilon=\beta_{\epsilon n}'''.
\tag{EC8}
\]
The last three are independent of n. Uniformly on the enlarged local
sector, `gamma=O(X^-1)`, `eta=O(X^-2)`, `zeta=O(X^-3)`.

Suppress indices and set `f0=h exp(T beta^2)`. Its logarithmic spatial
derivative and exact T-heat residual are
\[
p=(f_0)_z/f_0=\beta+2T\beta\gamma,
\]
\[
r_0={(f_0)_T-(f_0)_{zz}\over f_0}
=-\gamma(1+4T\beta^2)+r_2,\quad
r_2=-2T(\gamma^2+\beta\eta)-4T^2\beta^2\gamma^2.
\tag{EC9}
\]
Apply [Note08 EV6][n08]. Integrating the leading forcing in T with
zero initial correction gives the explicit first correction
\[
c=\gamma(T+2T^2\beta^2),\qquad
\boxed{\mathcal A_{\epsilon n}(T,z)=h_{\epsilon n}(z)e^{T\beta_{\epsilon n}^2}
 [1+\gamma_\epsilon(T+2T^2\beta_{\epsilon n}^2)]}.\tag{EC10}
\]
Indeed `c_T=gamma(1+4T beta^2)` cancels EC9's first-order forcing.
The transport/spatial terms are retained in Section5, not set to zero.
`A(0,z)=h(z)` exactly: this form preserves exact initial gamma modes.
The correction uses the product equation, without requiring a polar form
of a possibly vanishing signed field.

The main fixed-order model is
\[
\boxed{F_X^{[1]}(-T,z)=\sum_{\epsilon=\pm1}\sum_{n\le N}
\mathcal A_{\epsilon n}(T,z)+\mathcal I_1(T,z).}\tag{EC11}
\]
It contains only the first evaluated gamma-curvature correction, the two
RS coefficients C0,C1 and one bounded correction integral. The integral
contains no H, zeta values, unknown remainder or residual forcing.

There is a direct elementary version of this correction to the original
short `F_N` of Note04 CS4. Use its `P_{epsilon,n}(t,z)`, put
`B_{epsilon,n}=b_epsilon-log n`, `b_epsilon=Log(z/(4pi))/2+epsilon i pi/4`,
and define
\[
D_{\epsilon n}(t,z)={\epsilon i\over z}
 \{1/24-t/4-(7t/4)B_{\epsilon n}-(t^2/8)B_{\epsilon n}^2\}.
\tag{EC12}
\]
Gamma calibration CB4 and EC10 give, uniformly for all n,
\[
\mathcal A_{\epsilon n}(T,z)
=P_{\epsilon n}(-T,z)[1+D_{\epsilon n}(-T,z)]
 +O\bigl(|P_{\epsilon n}|X^{-2}(1+|B_{\epsilon n}|^4)\bigr).
\tag{EC13}
\]
The `1/24`, `7B/4`, `T/4` and `T^2 B^2/8` pieces pay, respectively,
initial gamma phase, slope calibration, heat determinant and displaced
quadratic moment. In particular omitting the initial gamma/slope pieces
would leave the old population error. In terms of the old F_N, this
elementary version adds
\[
\sum_{\epsilon,n\le N}P_{\epsilon n}(-T,z)D_{\epsilon n}(-T,z)
 +\mathcal I_1(T,z)-e^{\pi^2T/64}\mathcal R_N(z).
\tag{EC14}
\]
This explicitly replaces the old leading RS evolution as well as
correcting every arithmetic mode. EC11 is the exact-gamma convention
used in the theorem; EC13--14 are an equivalent version at its accuracy.

## 3. Complete populations and actual mode scope

Let `r_n=log(a_X/n)>=0`, `k_n=r_n/2`. The exact rewritings EV7--9
of the elementary baseline remain
\[
A_o(-T,X)w_n(-T,X)=A_o(0,X)n^{-1/2}
 e^{\pi^2T/64}e^{-Tk_n^2},\quad
\phi_n(-T,X)=\phi_n(0,X)-\pi T k_n/4.
\tag{EC15}
\]
Correction EC12 multiplies each complex arm by
`1+O((1+r_n^2)/X)` on fixed T; the exact-gamma version has the same
damping up to the calibrated small factors. It does not erase modes.
For every fixed d, on the enlarged fixed chart,
\[
\sum_{\epsilon,n\le N}|h_{\epsilon n}e^{T\beta_{\epsilon n}^2}|
 (1+|\beta_{\epsilon n}|)^d
 +\sum_{\epsilon,n\le N}|P_{\epsilon n}|(1+|B_{\epsilon n}|)^d
 \le C_{b,d}G(X)X^{1/4}.
\tag{EC16}
\]
To prove it, gamma transport gives `Re beta=-pi/8+O(X^-1)` and
`Im beta=epsilon r_n/2+O_b(X^-1)`; off-axis n/height powers combine
into at most `exp(C_b r_n)`. Each mode is bounded by
`C G(X) a_X^-1/2 exp(C_b r_n-r_n^2/8)`. The shell
`j<=r_n<j+1` contains at most `2 a_X exp(-j)` integers for every
nonempty shell. Its Gaussian times any fixed polynomial is summable.
This proves EC16 with constants independent of X. The initial real
absolute population is separately `sum |h(u)|<=C G(u)X^1/4`.

On the real chart, n in `[a_X/2,a_X]` already contribute at least
`c G(X)X^1/4` in absolute arm size: there are order sqrt X such modes,
their `r_n` are bounded, and their correction factors tend uniformly to
one. EC16 also proves total absolute first mode correction
`sum |f0 c|<=C G(X)X^-3/4`, and sums EC13's remainder to
`C G(X)X^-7/4`.

For fixed n, the individual damping scale is `T log^2 X=O(1)`;
ratios of two fixed-n weights change on `T log X=O(1)`. At fixed T
the weakly damped modes include a growing population comparable to
sqrt X. These are component statements. The signed sum and retained
RS data may cancel; an absolute shell bound is not a leading asymptotic
for H. No universal time transition is inferred from either fixed-mode
scale or this bounded interval.

## 4. Prove the solution error independently of residual cancellation

**Theorem.** For each declared fixed r,b, sufficiently large X and
`1<=T<=2`, uniformly on the entire Omega_X,
\[
\boxed{|\partial_z^j(H-F_X^{[1]})(-T,z)|
 \le C_{r,b,j}|G(z)|X^{-5/4},\qquad 0\le j\le3,}\tag{EC17}
\]
\[
\boxed{|\partial_t(H-F_X^{[1]})(-T,z)|
 \le C_{r,b}|G(z)|X^{-5/4}.}\tag{EC18}
\]
The same solution-error bounds hold for the elementary version EC13--14.
No field zero or cosine is a denominator. The gain is `X^-1/2` over
FN5, hence the requested named `o(|G|X^-3/4)`.

Proof first for the field on the enlarged chart. In EC3 split I_X
and its complement; on I_X insert `H(0,u)=S_N(u)+Q_{X,1}(u)+E_1(u)`.
By EC5 and gamma transport,
\[
\left|\int_{I_X} k_T(z-u)E_1(u)\,du\right|
 \le C G(X)X^{-5/4}.\tag{EC19}
\]
The kernel modulus is
`exp(y^2/(4T)) exp(-(u-x)^2/(4T))/sqrt(4pi T)`.
Thus its transverse factor is bounded by `exp((b+1)^2/4)` and its
moments against `G(u)/G(X)<=C exp(pi|u-X|/8)` are bounded on `[1,2]`.
This is a weighted chartwise estimate, not a whole-line supremum
contraction or an outer-relative stability assertion.

For each exact-gamma mode put v=u-z, x=Re z. Sectorial Taylor
expansion, independent of n after removing the tangent, gives
\[
h(u)=h(z)e^{\beta(z)v}
 [1+\tfrac12\gamma(z)v^2+\mathcal E(z,u)],
\]
\[
|\mathcal E(z,u)|\le {C\over X^2}(|v|^3+|v|^4)
 e^{C|v|^2/X}\qquad(u\in I_X).
\tag{EC20}
\]
The cubic logarithmic remainder costs `|v|^3/X^2`, and the square of
the retained quadratic costs `|v|^4/X^2`. Transverse cancellation is
essential: Taylor along z to its real part gives
\[
|h(z)e^{-iy\beta(z)}|\le C_b |h(x)|
 =C_b G(x)n^{-1/2},\quad |\Re\beta(z)|\le C_b.
\tag{EC21}
\]
The n-dependent powers therefore cancel before absolute estimation.
The kernel integral of EC20's remainder is at most
`C G(X)n^-1/2 X^-2` by bounded Gaussian moments. Summing the full
population gives **`C G(X)X^-7/4`**.

Complete only the tangent-quadratic approximating polynomial to the
whole real line. Its integrals are evaluated exactly:
\[
\int_{\mathbb R}k_T(z-u)e^{\beta(u-z)}du=e^{T\beta^2},\quad
\int_{\mathbb R}k_T(z-u)(u-z)^2e^{\beta(u-z)}du
=(2T+4T^2\beta^2)e^{T\beta^2}.
\tag{EC22}
\]
These follow from the entire Gaussian exponential identity (or its
second beta derivative); no target-dependent real part is taken.
They yield exactly EC10. The artificial tails and true complement
are paid below. Combining EC19--22 proves EC17 for j=0.

For spatial j<=3 apply Cauchy's formula on fixed-radius disks inside
the extra analytic margin. The **error** is holomorphic, the proved
field allowance has positive envelope `|G|` varying by a bounded factor
on those disks, and all chart parameters are frozen. Hence there is
no logarithmic derivative loss. This argument differentiates neither
a real RS floor formula nor a real-axis big-O allowance.

Direct time differentiation of EC19--22 inserts
`(z-u)^2/(4T^2)-1/(2T)` into the kernel; every local and tail moment
remains bounded at `T>=1`. Thus it also directly proves EC18. Section5
gives a second check from the exact error equation and actual residual.

**All tails.** For `V<|u-X|<=X/2`, the complete initial field has the
height-retaining bound
`|H(0,u)|<=C X^P exp(-pi X/8+pi|u-X|/8)`, with e.g. P=4 as in
FN27. For large V compared with the fixed buffers, Gaussian dominance
bounds the tail, including fixed kernel-derivative polynomials, by
\[
C G(X)X^{P-7/4}(1+V^5)e^{-V^2/64}.
\tag{EC23}
\]
With V=8L this is smaller than `G(X)X^-A` for any fixed A after
an A-dependent onset. For `|u-X|>X/2`, use the global real-source bound
only there; the tail is at most `G(X)` times
`C X^C exp(-cX^2+pi X/8)`, also smaller than every fixed inverse power.
For the artificial tangent-quadratic tails, EC21 and the whole
`G(X)X^1/4` population give
`C G(X)X^1/4(1+V^7)exp(-V^2/64)`; a bounded real tilt and a fixed
quadratic polynomial are Gaussian dominated on the whole ray. No true
analytic RS correction or exact gamma mode is extended through its
remote poles to justify this completion.

Adequate onset gates are `L>=16`, `X-V>=X/2`, the declared sectorial
gamma/real RS onsets, `a(X+V)-a(X-V)<1`, `C(V+r+b+2)^2/X<=1`, and
V larger than a fixed multiple of r+b+1. Finally impose that each
displayed tail majorant after division by G is at most X^-7/4. All
gates are eventual; constants and a numerical X0 are not evaluated.

There is no spatial localization of an error PDE in this proof. Thus
no cutoff commutator has been discarded. I_X is a fixed partition of
the exact initial convolution; both its true complement and artificial
completion tails have been bounded. No Duhamel stability theorem is
needed. The gamma-normalized kernel estimate EC19--21 supplies the
actual natural-scale stability used, and Section6 pays its outer loss.

## 5. Actual residual and the independent first-time check

For EC10 let `A=T+2T^2 beta^2`, `c=gamma A`. Exactly,
\[
c_z=\eta A+4T^2\beta\gamma^2,\quad
c_{zz}=\zeta A+12T^2\beta\gamma\eta+4T^2\gamma^3,
\]
\[
{\mathcal A_T-\mathcal A_{zz}\over f_0}
=r_2+r_0c-c_{zz}-2pc_z.
\tag{EC24}
\]
Every term is at most `C X^-2(1+|beta|^4)` for `1<=T<=2`.
EC16 therefore proves the actual summed residual, using EC7:
\[
\boxed{|\mathfrak r_{F^{[1]}}|+|\partial_z\mathfrak r_{F^{[1]}}|
 \le C |G(z)|X^{-7/4},\quad
\mathfrak r_F=F_t+F_{zz}=-(F_T-F_{zz}).}\tag{EC25}
\]
The first residual derivative follows either by differentiating EC24
and using the next fixed moment in EC16, or fixed-margin Cauchy on
the **summed residual**. The latter avoids a logarithmic loss.

For completeness the elementary version's exact residual is
\[
\sum_{\epsilon,n}P_{\epsilon n}
 [(1+D_{\epsilon n})R_{\epsilon n}+(D_{\epsilon n})_t
 +2p_{\epsilon n}(D_{\epsilon n})_z+(D_{\epsilon n})_{zz}],
\tag{EC26}
\]
where, with B=B_epsilon,n,
\[
p_{\epsilon n}=\epsilon iB/2+(7/4+tB/4)/z,
\quad R_{\epsilon n}={\epsilon i(1+7B+tB^2)\over4z}
 +{21/16+t/8+5tB/8+t^2B^2/16\over z^2}.
\]
Here `D_t` cancels the leading 1/z part of R. EC16 pays the remaining
`C |P|X^-2(1+|B|^4)` by the same EC25 bound. The correction integral
again contributes zero residual. These are exact product-residual
identities followed by population bounds, not residuals obtained by
differentiating EC13's error allowance.

Finally the true error satisfies
\[
\partial_t(H-F)=-(H-F)_{zz}-\mathfrak r_F.
\tag{EC27}
\]
EC17 for j=2 plus EC25 proves EC18 independently of differentiating
any asymptotic allowance. Residual cancellation alone did not prove
EC17: canonical initial matching, weighted kernels and tails did.

## 6. Two accuracy scales and the precise remaining loss

Note05 FN3 gives on the full fixed chart
`E_o(-T,z)>=c |G(z)| exp(-T L^2/16)`. On the real axis the sharper
ratio includes the bounded factor `exp(pi^2 T/64)`. Thus EC17--18
imply only the outer-relative allowances
\[
\delta_1(T,X)=X^{-5/4}e^{TL^2/16},\qquad
\delta_{\mathrm{res},1}(T,X)=X^{-7/4}e^{TL^2/16}.
\tag{EC28}
\]
There are no hidden log powers. In particular
\[
\log\delta_1=TL^2/16-5L/4+O(1),\quad
\log\delta_{\mathrm{res},1}=TL^2/16-7L/4+O(1).
\tag{EC29}
\]
For every fixed T in [1,2], both allowances eventually grow. The
solution allowance gains X^-1/2 over FN10, but still does not pay a
vanishing outer-relative error. At leading logarithmic level its
negative linear term balances its quadratic term at `L=20/T`; this
is only the formal crossover of this bound, not a certified onset,
an H transition, or an error lower bound. Fixed algebraic order cannot
offset this conversion factor as X tends to infinity at fixed T.
This conclusion is scoped to such finite algebraic **allowances**;
it is no impossibility result for a short resummed expression.

| Representation | Gamma curvature / RS orders | Proved accuracy on 1<=T<=2 |
| --- | --- | --- |
| Old elementary short F_N, FN5 | Frozen leading modes; leading analytic RS correction | `C |G|X^-3/4`; outer allowance FN10 fails. |
| EC11 (or its elementary version) | One evaluated quadratic correction; K=1 initial RS; bounded integral and exact transfer retained | `C |G|X^-5/4` field/j<=3/time; actual residual `C |G|X^-7/4`. |
| Old high-order FN25 | J=ceil(3L), K=ceil(L); bounded correction integral | `C E_o exp(-L^2/4)` field/j<=3/time; zero frozen-chart residual. |

The new gain is a fixed-order simplification at the natural gamma
scale. It does not improve FN25's stronger outer-scale theorem, remove
the integral, reduce N, or prove useful evaluated cost. The RS term
must also improve: keeping only the old k=0 initial remainder leaves
`C |G|X^-3/4`, even after correcting every arithmetic mode. That is a
precise failed initial-error estimate, not a claim about the actual
error's size. A wholly elementary replacement of EC6 would need a paid
C1 formula, its regularity/transfer and its heat approximation; this
note does not manufacture those facts from a coefficient size bound.

## 7. Parent observable equations and first unpaid consumer

In parent Note31 PE37--39 insert this actual F and
`mathcal E=mathfrak r_F`, with
\[
D_F=|F|^2+q,\quad Z_0=\mathfrak r_F\overline F/D_F.
\]
The potential forcing is `2 Re K*Z0`; the density equation adds
`Delta Re K*Z0/(2pi)`, and the current balance adds `K*D_r`, where
\[
\mathcal D_r={2q\Re((\mathfrak r_F)_z\overline{F_z})\over\pi D_F^2}
 -4\rho_F\Re(\mathfrak r_F\overline F/D_F).
\tag{EC30}
\]
These are the actual observables and signed covariance; no closure
variable is redefined. On this negative interval q depends only on
time, hence C_F=0, but regulator time forcing remains.

EC25 supplies the numerator bounds. The crude pointwise inequality
`|2 Re Z0|<=|mathfrak r_F|/sqrt(q)` gives only
`C |G| X^-7/4/sqrt(q)` before filtering; it is not an asserted physical
transfer. The first unpaid consumer is **a regulator-uniform weak/collar
bound for this new F and H**, sufficient to apply PE14/PE35 and pay
these residual forcings and the actual Q comparison. No simple-root
collars or outer-relative smallness have been established here, so the
positive-time parent transfer theorem cannot simply be invoked.
Spatial joins would add parent GS7--12 defects, and time joins CJ23
would retain both component residuals and the derivative-of-cutoff
term. Neither join is performed by this packet.

## 8. Controls, disposition and next bounded deliverable

This is an approximation result under [avoid01][a01], judged by EC17's
quantitative gain, not an RH-equivalent criterion. Consult both the
[result index][results], especially [heat-flow cluster11][r11] and
[collision controls12][controls], and the [avoid index][avoid], especially
[shared premises02][a02], [review05][a05], [scope07][a07],
[constants08][a08], [separate bounds12][a12] and [imports16][a16].

Heat/product evolution identities hold also for the collision controls
and exclude none. The premise screen is unchanged: Euler-factor and
normalized-endpoint perturbations fail the unchanged ordinary arithmetic
coefficients; finite weighted-square, theta-cutoff and zero-tail controls
fail the full canonical xi/RS identity; reflected super-Gaussian,
smooth-shape and positive-primitive controls do not provide gamma times
ordinary zeta with its full sequence; counter-kernels, atomic and finite
profile controls fail the same canonical completion; finite-prime matching
does not supply the full coefficients/reflection. These are failed
premises, not numerical exclusions or a noncollision conclusion.

**Disposition — Analysis, Sol:** accept EC17--18 and EC25 in the stated
fixed-order Gaussian-moment/retained-RS-integral class. Close AN03 at
its bounded natural-scale gain and two-scale-comparison stop rule;
the integral-free short-formula target remains open. HDA-A02 remains
**Partial**. Same-model parallel checks share the imported inputs and
are not specialist or cross-model independent validation. No manuscript
integration, snapshot, numerical onset or automatic dispatch is made.
Parent HDA-17 Partial, HDA-18 Gated and HDA-20 unfulfilled are unchanged.

**Next deliverable — Analysis, Sol:** assess and integrate the bounded
EC11 theorem, its retained-integral scope, actual forcing and failed
outer allowance into the maintained manuscript. This is routine
follow-through, not a resistant new mechanism requiring Astra.
The [prepared next packet][next] supplies the narrow integration scope;
no extension in T, through-zero joining or numerical campaign is implied.

[packet]: ../research-progress/handoffs/HDA-A02-AN03.md
[inputs]: 10_FIRST_NEGATIVE_CORRECTION_INPUTS_20261025.json
[review]: ../reviews/07_FIRST_NEGATIVE_CORRECTION_ASSESSMENT_20261025.md
[next]: ../research-progress/handoffs/HDA-A02-AN04.md
[n03]: 03_OUTER_CORRECTION_AND_SIGNED_REAL_BRIDGE_20261025.md
[n04]: 04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md
[n05]: 05_FIXED_NEGATIVE_TIME_REPRESENTATIONS_20261025.md
[n08]: 08_EVOLUTION_RESIDUAL_AND_NEGATIVE_TIME_MODES_20261025.md
[poly]: https://arxiv.org/html/1904.12438v2#S6.SS2
[results]: ../../../../../result-summaries/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a05]: ../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a08]: ../../../../../avoid/08_normalization_and_constant_slips.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a16]: ../../../../../avoid/16_unchecked_imports_and_novelty_claims.md

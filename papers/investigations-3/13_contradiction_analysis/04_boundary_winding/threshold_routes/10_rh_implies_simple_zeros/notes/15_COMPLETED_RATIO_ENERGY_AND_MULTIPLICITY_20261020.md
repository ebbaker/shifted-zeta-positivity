# Completed-ratio energy and multiplicity

20 October 2026. Prepared for **Edward Baker** with substantial LLM assistance.
Actual model **gpt-6-astra**, effort **ultra**, verified from turn metadata.
Separate same-model internal derivations and integration review; no
specialist review or novelty claim.
The [result index](../../../../../../../result-summaries/README.md),
[avoid index](../../../../../../../avoid/README.md), and complete-payment
and scoped-conclusion rules apply.

**Outcome: an exact first-order ratio-energy identity is proved under RH.** The global proof below
accounts for every zero and proves tightness; local harmonic convergence
alone would not suffice. The identity also transfers to the uncompleted
zeta ratio with an `O(epsilon)` error in the weighted norm. It is not an
upper bound by the simple-zero constant.

## 1. Exact positive mass, with no unassigned term at infinity

Assume RH and write `F(z)=xi(1/2+z)`. Let `lambda` run over the distinct
signed ordinates of its zeros `i lambda`, with multiplicities `m_lambda`.
The even order-one product, paired at opposite ordinates, gives

\[
 \frac{F'(z)}{F(z)}=
 \sum_{\lambda>0}m_\lambda
 \left(\frac1{z-i\lambda}+\frac1{z+i\lambda}\right),
 \qquad
 M_\sigma:=\frac{F'(\sigma)}{\sigma F(\sigma)}
 =\sum_\lambda\frac{m_\lambda}{\sigma^2+\lambda^2}<\infty.
 \tag{CR1}
\]

This uses the same paired product as Note 01. There is no extra affine
term in the logarithmic derivative. Its real part is positive in
`Re z>0`.

For `epsilon>0` define `R_epsilon(z)=F(z)/F(z+epsilon)` and
`u_epsilon=Re(1-R_epsilon)`. Integrating the real logarithmic derivative
along a horizontal segment shows `|R_epsilon|<=1` in the right
half-plane and on its boundary. Hence `0<=u_epsilon<=2` and

\[
 |1-R_\epsilon|^2\le2u_\epsilon.
 \tag{CR2}
\]

Fix `sigma>0`. The Poisson formula for bounded harmonic functions gives
the **exact** total mass of the positive boundary measure

\[
 d\nu_\epsilon(t)=
 \frac{u_\epsilon(it)}{\pi\epsilon(\sigma^2+t^2)}\,dt:
 \qquad
 \nu_\epsilon(\mathbb R)=
 \frac{1-R_\epsilon(\sigma)}{\sigma\epsilon}
 \longrightarrow M_\sigma.
 \tag{CR3}
\]

The numerator on the right is real because `F` is real and nonzero on
the positive real axis. Define also

\[
 d\eta_\epsilon(t)=
 \frac{|1-R_\epsilon(it)|^2}{2\pi\epsilon(\sigma^2+t^2)}\,dt.
 \tag{CR4}
\]

Then `0<=eta_epsilon<=nu_epsilon`. Its total is the proposed squared
ratio distance divided by `epsilon`.

## 2. Local profiles, constants, and all-zero exhaustion

At a zero `i lambda` of order `m`, factor
`F(i lambda+z)=z^m A(z)` with `A(0)!=0`. For bounded real `y`,

\[
 R_\epsilon(i\lambda+i\epsilon y)
 \longrightarrow r(y)^m,
 \qquad r(y)=\frac{iy}{1+iy},
 \tag{CR5}
\]

uniformly on compact `y`-intervals. Constants may depend on this fixed
zero; no uniform inverse derivative bound is needed.
Put `v_m(y)=Re(1-r(y)^m)`. Both profile integrals are explicit:

\[
 \frac1\pi\int_{\mathbb R}v_m(y)\,dy=m,\qquad
 c_m:=\frac1{2\pi}\int_{\mathbb R}|1-r(y)^m|^2\,dy
 =m\left(1-\frac{\binom{2m}{m}}{4^m}\right).
 \tag{CR6}
\]

For the first formula, expand
`1-r^m=sum_(k=1)^m (-1)^(k+1)binom(m,k)(1+iy)^(-k)`.
The integral of the real part is `pi` for `k=1` and zero for `k>=2`.
For the second use
`|1-r^m|^2=2v_m-(1-|r|^(2m))` and integration by parts:

\[
 \int_{\mathbb R}\left(1-\frac{y^{2m}}{(1+y^2)^m}\right)dy
 =2m\int_{\mathbb R}\frac{y^{2m}}{(1+y^2)^{m+1}}\,dy
 =2\pi m\frac{\binom{2m}{m}}{4^m}.
 \tag{CR7}
\]

Here is the precise global passage. For a finite set `S` of distinct
zeros, the windows `lambda+epsilon[-Y,Y]` are disjoint for sufficiently
small `epsilon`. First let `epsilon` decrease to zero on these windows,
using (CR5). Next let `Y` increase to infinity, using (CR6). Positivity
gives the lower estimate

\[
 \liminf_{\epsilon\downarrow0}\eta_\epsilon(\mathbb R)
 \ge\sum_{\lambda\in S}\frac{c_{m_\lambda}}{\sigma^2+\lambda^2}.
\]

For the complement, use `eta<=nu` and subtract the measured local
`nu` mass from its **complete** total (CR3). This gives

\[
 \eta_\epsilon(\mathbb R)\le
 \eta_\epsilon(W_\epsilon)+\nu_\epsilon(\mathbb R)
                         -\nu_\epsilon(W_\epsilon),\qquad
 W_\epsilon=\bigcup_{\lambda\in S}
                     [\lambda-\epsilon Y,\lambda+\epsilon Y].
\]

Taking `epsilon->0` and then `Y->infinity` yields

\[
 \limsup_{\epsilon\downarrow0}\eta_\epsilon(\mathbb R)
 \le\sum_{\lambda\in S}\frac{c_{m_\lambda}}{\sigma^2+\lambda^2}
       +M_\sigma-
        \sum_{\lambda\in S}\frac{m_\lambda}{\sigma^2+\lambda^2}.
 \tag{CR8}
\]

Finally exhaust the zero set. Because `0<c_m<=m` and (CR1) is finite,
both bounds converge to the same answer:

\[
 \boxed{\lim_{\epsilon\downarrow0}\frac1{2\pi\epsilon}
   \int_{\mathbb R}\frac{|1-R_\epsilon(it)|^2}{\sigma^2+t^2}\,dt
 =\sum_\lambda\frac{c_{m_\lambda}}{\sigma^2+\lambda^2}.}
 \tag{CR9}
\]

The same finite-set argument proves the weighted weak convergence
`nu_epsilon -> sum m_lambda/(sigma^2+lambda^2) delta_lambda`, with
tightness. Neither unseen zeros nor mass escaping to infinity is dropped.
No uniform zero separation is assumed: the windows are taken for each
fixed finite set before exhaustion.

The pure product in (CR1) matters. For example `F(z)=exp(cz^2)`, `c>0`,
has no zeros but its same ratio distance divided by `epsilon` tends to
`2c`. Its positive harmonic mass escapes to infinity. This elementary
control is outside xi's order-one product class and shows why local
profiles alone would have been an incomplete proof.

## 3. Completion can be removed at lower order in this norm

Write `xi(s)=C(s)zeta(s)`,
`C(s)=s(s-1)pi^(-s/2)Gamma(s/2)/2`.
On `1/2<=Re s<=3/4`, this factor is nonzero and

\[
 \frac{C'}C(s)=\frac1s+\frac1{s-1}-\frac12\log\pi
                 +\frac12\psi(s/2)
 =O(\log(2+|\operatorname{Im}s|)).
 \tag{CR10}
\]

The bound follows from the checked
[digamma expansion](https://dlmf.nist.gov/5.11.E2), together with
boundedness on the remaining compact set. The uniform Stirling ratio
also gives `|C(s+u)/C(s)|<=K(2+|t|)^(u/2)` for `0<=u<=1/4`.
Integrate its derivative in `u` to obtain, with `s=1/2+it`,

\[
 \left|\frac{C(s+\epsilon)}{C(s)}-1\right|
 \le K\epsilon\log(2+|t|)(2+|t|)^{\epsilon/2}
 \qquad(0<\epsilon\le1/4).
 \tag{CR11}
\]

The squared right side is integrable against
`dt/(sigma^2+t^2)` uniformly for `0<epsilon<=epsilon_0`.
Here one may take `epsilon_0=1/4`.
As `|R_epsilon(it)|<=1`,

\[
 \left\|\frac{\zeta(s)}{\zeta(s+\epsilon)}-R_\epsilon(it)
 \right\|_{L^2(dt/(2\pi(\sigma^2+t^2)))}=O_\sigma(\epsilon).
 \tag{CR12}
\]

By (CR2)–(CR3), the completed residual norm is `O_sigma(sqrt(epsilon))`.
Consequently replacing `R_epsilon(it)` by the direct zeta ratio in
(CR9) changes the squared norm by `O_sigma(epsilon^(3/2))=o(epsilon)`.
Thus **(CR9) also holds for the direct zeta-ratio residual**.

This is consistent with [Burnol, Theorem 1.3 and §2](https://arxiv.org/pdf/math/0202166),
which proves RH-conditioned ratio bounds and qualitative square-mean
convergence in the Nyman–Beurling setting. The opened primary source
does not supply this multiplicity coefficient; no exhaustive novelty
assessment is claimed here. The identity is proved directly above.

The directly relevant subsequent source is
[Balazard–de Roton, Proposition 2 and §4](https://arxiv.org/pdf/0812.1689).
Their `J_epsilon` is exactly the direct zeta-ratio squared distance at
`sigma=1/2`. They prove `J_epsilon=O(epsilon)` under RH and end §4 by
asking for a more precise asymptotic. Their §3 also supplies the uniform
Stirling-ratio estimate used above. This identifies the checked historical
context, without a claim that later literature has been exhausted.

## 4. Constant and limitation relevant to this investigation

At `sigma=1/2`, (CR1) equals
`Z=2+EulerGamma-log(4pi)`. The central-binomial ratio decreases strictly
from `1/2` as `m` increases from one. Hence `c_m>=m/2`, with equality
only for `m=1`, and

\[
 \sum_\lambda\frac{c_{m_\lambda}}{1/4+\lambda^2}
 =\frac Z2+
 \sum_\lambda\frac{m_\lambda(1/2-\binom{2m_\lambda}{m_\lambda}/4^{m_\lambda})}
                       {1/4+\lambda^2}.
 \tag{CR13}
\]

In particular `c_1=1/2`, `c_2=5/4`; one exact double conjugate pair
at ordinates `±gamma` contributes an excess
`1/[2(gamma^2+1/4)]` over `Z/2`.
The available general upper bound is `Z`; no upper bound `Z/2` is obtained.

For the explicit product control `F(z)=(z^2+lambda^2)^m`, the same
proof gives total harmonic mass `2m/(sigma^2+lambda^2)` and ratio-energy
coefficient `2c_m/(sigma^2+lambda^2)`. For `m>=2` the latter strictly
exceeds one-half of the former. This control fails the original xi,
theta-source, and ordinary-Dirichlet arithmetic premises; it only checks
that the product and Schur arguments cannot supply the missing
half-linear upper bound.

This is an exact quantitative identity under RH, retaining arbitrary
multiplicities. It is also a property of the stated even real-zero
product geometry, so it is not a strict arithmetic sign. It gives no
finite Dirichlet-polynomial cutoff, uniform convergence rate, matching
Nyman–Beurling upper bound, or contradiction with a multiple zero.
Such a conclusion would require an additional arithmetic estimate;
no such estimate is assumed or obtained here.

The quantitative gain is the explicit coefficient in (CR9), with all-zero
tightness and the direct-zeta transfer. It does not close RHS-02. See the
[separate same-model check, §6](../reviews/12_FINITE_PRECISION_SIGNED_KERNEL_AND_ENERGY_REVIEW_20261020.md) and
[progress register](../research-progress/01_RH_TO_SIMPLICITY_PROGRESS_20261020.md).


## 5. Heat separation: the exact joint-scale crossover

20 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, actual effort ultra**. Separate same-model analytic checks;
no specialist review or novelty claim.

**Result.** The ratio energy has an explicit, strictly decreasing local crossover as a multiple heat cluster separates. The same positive-mass exhaustion as Note15 proves the corresponding global joint limit. For a double cluster the crossover is \(1+[4(1+r^2)]^{-1}\). Thus a hypothetical multiple endpoint requires a heat-time difference quotient of order \(1/\epsilon\) for the unnormalized ratio energy on time intervals of length \(O(\epsilon^2)\). This behavior is compatible with the smooth positive theta source; it is not an opposing upper bound.

### 5.1 Coordinates and the actual joint limit

Assume RH and put
\[
\mathcal F_t(z)=8H(t,-2iz),\qquad
\partial_t\mathcal F_t=\tfrac14\partial_z^2\mathcal F_t,
\qquad \mathcal F_0(z)=\xi(\tfrac12+z).
\]
Here \(\epsilon\) is the real shift in the **zeta** coordinate, as in Note15; it is an imaginary shift of magnitude \(2\epsilon\) in the heat \(x\)-coordinate. Fix \(\sigma>0\) and define
\[
J_t(\epsilon)=\frac1{2\pi}\int_{\mathbb R}
 \frac{|1-\mathcal F_t(iy)/\mathcal F_t(\epsilon+iy)|^2}
      {\sigma^2+y^2}\,dy .
\tag{HR1}
\]
The complete source makes \(\mathcal F_t\) jointly analytic. Uniformly for \(0\le t\le T\), splitting its source integral at \(u=\log(2+R)\) gives
\(\log\max_{|z|\le R}|\mathcal F_t(z)|=O(R\log(2+R))+O_T(\log^2(2+R))\): below this point use \(|\cosh(2zu)|\le e^{2Ru}\), and above it the \(e^{-\pi e^{4u}}\) source tail absorbs the remaining exponential factors. Thus its entire order is at most one. RH and heat real-root preservation therefore give its even paired product, without a quadratic exponential factor. In particular its horizontal ratio is contractive and
\[
M_\sigma(t)=\frac{\mathcal F_t'(\sigma)}
                    {\sigma\mathcal F_t(\sigma)}
 =\sum_{\lambda(t)}\frac{m_{\lambda(t)}}{\sigma^2+\lambda(t)^2}.
\tag{HR2}
\]
This quantity is continuous in \(t\), including at zero.

Let \(i\gamma\) be an exact order-\(m\) zero of \(\mathcal F_0\), and let \(a_\gamma=\mathcal F_0^{(m)}(i\gamma)/m!\ne0\). For fixed \(v\ge0\), the heat equation and the convergent joint Taylor expansion give
\[
\mathcal F_{v\epsilon^2}(i\gamma+\epsilon z)
 =a_\gamma\epsilon^m
     \left[Q_{m,v}(z)+O(\epsilon)\right],
\quad
Q_{m,v}(z)=\exp\!\left(\frac v4\partial_z^2\right)z^m .
\tag{HR3}
\]
The error is uniform for \(z,v\) in compact sets; it is a finite leading parabolic-degree expansion, not a formal interchange of a divergent heat series.

Write \(r=\sqrt{v/2}\), let \(\lambda_1<\cdots<\lambda_m\) be the roots of the probabilists' Hermite polynomial \(\mathrm{He}_m\), and put
\[
P_{m,r}(y)=\prod_{j=1}^m(y-r\lambda_j)
          =r^m\mathrm{He}_m(y/r),\qquad P_{m,0}(y)=y^m.
\]
Then \(Q_{m,v}(iy)=i^mP_{m,r}(y)\). Since \(Q_{m,v}(1+iy)\ne0\) for real \(y\), (HR3) gives the compact-uniform ratio profile
\[
\frac{\mathcal F_{v\epsilon^2}(i\gamma+i\epsilon y)}
     {\mathcal F_{v\epsilon^2}(i\gamma+\epsilon+i\epsilon y)}
 \longrightarrow
 \mathcal R_{m,r}(y):=\frac{P_{m,r}(y)}{P_{m,r}(y-i)}.
\tag{HR4}
\]
Define
\[
C_m(r)=\frac1{2\pi}\int_{\mathbb R}
                         |1-\mathcal R_{m,r}(y)|^2\,dy.
\tag{HR5}
\]
These integrals are finite. The polynomial ratio is contractive on the boundary, and its degree-\(m\) expansion at infinity gives
\(\int_{\mathbb R}\Re(1-\mathcal R_{m,r})\,dy=m\pi\).
For example this follows by applying the half-plane Poisson formula at a positive real point \(x\), multiplying by \(x\), and using \(x(1-Q(x)/Q(x+1))\to m\). Its nonnegative boundary real part is integrable.

To justify the **global** limit, use the positive measures
\[
d\nu_{\epsilon,t}(y)=
\frac{\Re(1-\mathcal F_t(iy)/\mathcal F_t(\epsilon+iy))}
     {\pi\epsilon(\sigma^2+y^2)}\,dy,
\qquad
\nu_{\epsilon,t}(\mathbb R)
=\frac{1-\mathcal F_t(\sigma)/\mathcal F_t(\sigma+\epsilon)}
       {\sigma\epsilon}.
\tag{HR6}
\]
For \(t=v\epsilon^2\), their total tends to \(M_\sigma(0)\). Around each fixed finite set of initial zero locations, use disjoint windows \(\gamma+\epsilon[-Y,Y]\). Equations(HR3)–(HR4) give their local energy and harmonic mass. Let \(Y\to\infty\); each group recovers its full harmonic mass \(m/(\sigma^2+\gamma^2)\), independent of \(r\). The remaining energy is bounded by the remaining \(\nu\) mass, exactly as in Note15(CR8). Exhausting the initial zeros proves
\[
\boxed{\lim_{\epsilon\downarrow0}
 \frac{J_{v\epsilon^2}(\epsilon)}{\epsilon}
 =\sum_{\gamma\ {\rm distinct}}
       \frac{C_{m_\gamma}(\sqrt{v/2})}{\sigma^2+\gamma^2}.}
\tag{HR7}
\]
Both ordinate signs occur. There is no unassigned contribution from remote zeros or infinity. The argument is uniform for \(v\) in any fixed compact interval: total mass convergence, the finite-group expansions and their profile tails are uniform there. Uniform convergence of these values does **not** assert convergence of their heat-time derivatives.

### 5.2 A monotone crossover and an explicit separation bound

For arbitrary real centers \(a_1,\ldots,a_m\), put \(q_j(y)=1/[1+(y-a_j)^2]\). The same degree calculation and the identity \(|1-R|^2=2\Re(1-R)-(1-|R|^2)\) give
\[
C(a)=m-\frac1{2\pi}\int_{\mathbb R}
       \left[1-\prod_{j=1}^m(1-q_j(y))\right]dy.
\tag{HR8}
\]
The defect integral has an elementary geometric representation. Take independent nonnegative random radii \(R_j\) with
\(\Pr(R_j\ge u)=1/(1+u^2)\). It is the expected length of
\(\bigcup_j[a_j-R_j,a_j+R_j]\). This expectation is finite, since \(\mathbb E R_j=\pi/2\).

If \(a_j=r\lambda_j\) with ordered \(\lambda_j\), the union length is a continuous piecewise-affine nondecreasing function of \(r\ge0\), for every fixed choice of radii. Indeed, on each interval where the active endpoints do not change, a component's length derivative is \(\lambda_{\rm right}-\lambda_{\rm left}\ge0\). A rightmost active index smaller than the leftmost active index would require both \(R_{\rm right}-R_{\rm left}\ge r(\lambda_{\rm left}-\lambda_{\rm right})\) and its opposite. Thus \(C_m(r)\) is nonincreasing. For \(m\ge2\) it is strictly decreasing. Given \(r_2>r_1\), choose every radius in \([R,R+\delta]\), with \(R>r_2(\lambda_m-\lambda_1)\) and \(2\delta<(r_2-r_1)(\lambda_m-\lambda_1)\). On this positive-probability event the union is connected and its length increases by at least \((r_2-r_1)(\lambda_m-\lambda_1)-2\delta>0\).

Bonferroni's two-term inequality and the overlap of any chosen pair give
\[
\frac1{4+(a_i-a_j)^2}
\le C(a)-\frac m2
\le\sum_{i<j}\frac1{4+(a_i-a_j)^2}.
\tag{HR9}
\]
Here \(\int q_iq_j\,dy=2\pi/[4+(a_i-a_j)^2]\). The lower bound follows also by writing the integrand as the expectation of \((K-1)_+\), where \(K\) counts the intervals covering \(y\), and comparing it with the indicator that the chosen pair both cover \(y\).

For Hermite centers, the already checked identity
\(\sum_{i<j}(\lambda_i-\lambda_j)^{-2}=m(m-1)/8\) yields
\[
C_m(0)=c_m,\qquad
0<C_m(r)-\frac m2\le\frac{m(m-1)}{8r^2}\quad(r>0,\ m\ge2),
\qquad
C_m(r)\longrightarrow\frac m2 .
\tag{HR10}
\]
The leading large-\(r\) correction is in fact \(m(m-1)/(8r^2)+O_m(r^{-4})\): the pair integrals have this expansion and each triple overlap is \(O_m(r^{-4})\), by partitioning the line according to the nearest of its three centers. No arithmetic zero-gap lower bound is used.

For a double cluster \(\lambda_1=-1,\lambda_2=1\), (HR9) is an equality:
\[
\boxed{C_2(r)=1+\frac1{4(1+r^2)},\qquad
 C_2(\sqrt{v/2})=1+\frac1{4(1+v/2)}.}
\tag{HR11}
\]
Equivalently its local residual is
\((2z+1)/[(z+1)^2+r^2]\) on \(z=iy\).

### 5.3 The heat-time cost and the source comparison

For every fixed \(t>0\), all heat zeros are simple. Otherwise the local Hermite law at an alleged positive-time multiple zero would produce nonreal zeros at slightly earlier nonnegative times, contradicting RH and real-root preservation. Note15 therefore gives
\[
\lim_{t\downarrow0}\lim_{\epsilon\downarrow0}
 \frac{J_t(\epsilon)}{\epsilon}=\frac12M_\sigma(0),
\qquad
\lim_{\epsilon\downarrow0}\frac{J_0(\epsilon)}{\epsilon}
 =\sum_\gamma\frac{c_{m_\gamma}}{\sigma^2+\gamma^2}.
\tag{HR12}
\]
The joint formula(HR7) interpolates these limits. Its coefficient decreases strictly with \(v\) if any initial multiplicity exceeds one. This is a monotonicity statement for the **joint-limit profile**, not for \(J_t(\epsilon)\) at arbitrary finite parameters.

In particular, for fixed \(v>0\), let
\[
\Delta_\sigma(v)=\sum_\gamma
 \frac{c_{m_\gamma}-C_{m_\gamma}(\sqrt{v/2})}{\sigma^2+\gamma^2}.
\]
Then
\[
J_0(\epsilon)-J_{v\epsilon^2}(\epsilon)
 =\epsilon\Delta_\sigma(v)+o(\epsilon).
\tag{HR13}
\]
If a multiple zero exists, \(\Delta_\sigma(v)>0\). Any heat-time Lipschitz allowance covering this interval must therefore be at least
\(\Delta_\sigma(v)/(v\epsilon)+o(\epsilon^{-1})\); for \(J/\epsilon\), the corresponding scale is \(\epsilon^{-2}\). This finite-difference consequence does not assume differentiability of the full energy in time.

For one double location, its contribution to \(\Delta_\sigma(v)\) is exactly
\[
\frac{v}{4(v+2)(\sigma^2+\gamma^2)}.
\tag{HR14}
\]
The local model's derivative is
\[
\frac{d}{dt}\left[\epsilon C_2\!\left(\sqrt{\frac{t}{2\epsilon^2}}\right)\right]
 =-\frac{\epsilon^3}{2(t+2\epsilon^2)^2},
\]
which equals \(-1/(8\epsilon)\) at zero. If instead \(\delta\) denotes the heat-coordinate imaginary shift, the model energy normalized in that coordinate is \(\delta C_2(\sqrt{2t}/\delta)\), with derivative \(-\delta^3/[2(\delta^2+2t)^2]\). The two formulas use different coordinate normalizations.

The unchanged positive theta source does give a smooth comparison for the **linear harmonic mass**. Under the probability density proportional to \(e^{tu^2}\Phi(u)\cosh(2\sigma u)\,du\),
\[
M_\sigma(t)=\frac2\sigma\mathbb E[u\tanh(2\sigma u)],
\qquad
M_\sigma'(t)=\frac2\sigma
 \operatorname{Cov}(u^2,u\tanh(2\sigma u))>0.
\tag{HR15}
\]
All these moments and derivatives are finite on bounded time intervals. Strict positivity follows because both functions are strictly increasing on \(u>0\) and the source is positive there. This finite smooth mass payment does not bound the heat-time change of the nonlinear ratio energy uniformly in \(\epsilon\). Its local redistribution cost is exactly what(HR13) measures.

### 5.4 The large-separation correction and the classical multiplicity penalty

Let
\[
K_\sigma=\sum_{\gamma\ {\rm distinct}}
                \frac{m_\gamma^2}{\sigma^2+\gamma^2},
\qquad
\mathcal A_\sigma(v)=
\sum_\gamma\frac{C_{m_\gamma}(\sqrt{v/2})}{\sigma^2+\gamma^2}.
\tag{HR16}
\]
The usual unit-window zero count gives \(m_\gamma=O(\log(2+|\gamma|))\); together with \(N(T)=O(T\log T)\), a dyadic sum proves \(K_\sigma<\infty\). Thus(HR10) gives the global quantitative bound
\[
0\le\mathcal A_\sigma(v)-\frac{M_\sigma(0)}2
\le\frac{K_\sigma-M_\sigma(0)}{4v},
\qquad
\boxed{\lim_{v\to\infty}
v\left(\mathcal A_\sigma(v)-\frac{M_\sigma(0)}2\right)
=\frac{K_\sigma-M_\sigma(0)}4.}
\tag{HR17}
\]
For the limit, each fixed multiplicity has the large-\(r\) expansion following(HR10), while \(m_\gamma(m_\gamma-1)/[4(\sigma^2+\gamma^2)]\) is a summable dominator. At \(\sigma=1/2\), \(M_\sigma(0)=Z\); the coefficient in(HR17) is exactly one quarter of the multiplicity penalty \(K-Z\) in Note12's Burnol comparison. The order is epsilon to zero at fixed v, followed by v to infinity; this asserts no joint limit with unbounded v=v(epsilon). This is a quantitative relation between the two derived costs, not an improved arithmetic upper bound.

The positive-source collision controls in Note05 have the same local Hermite crossover and finite source-moment payments; their failed ordinary-Dirichlet premise remains unchanged. No derivative allowance contradicting(HR13) has been derived for the original theta source. The comparison therefore quantifies a necessary precision/uniformity demand and the compatible direction of the heat transition, rather than excluding the endpoint.


## 6. Exact arithmetic norm and the signed correlation payment

20 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, actual effort ultra**. This is a quantitative payment
comparison for the unchanged Möbius coefficients; the real-variable
representation is classical and is credited below.

Assume RH and take \(0<\varepsilon\le1/4\). Write
\[
 R_\varepsilon(s)=\frac{\zeta(s)}{\zeta(s+\varepsilon)},\quad
 K_\varepsilon=\frac1{2\pi}\int_\mathbb R
 \frac{|R_\varepsilon(1/2+it)|^2}{1/4+t^2}\,dt,
 \quad J_\varepsilon=\|1-R_\varepsilon\|^2
 \tag{AR1}
\]
in the same weighted norm. Note15 proves
\(J_\varepsilon=C_*\varepsilon+o(\varepsilon)\), retaining arbitrary multiplicities, where
\(C_*=\sum_\rho c_{m_\rho}/|\rho|^2\).

### 6.1 The elementary linear term is already exact

[Balazard–de Roton, Proposition5 and §4](https://arxiv.org/pdf/0812.1689) give
\[
 L_\varepsilon:=\frac1{2\pi}\int_\mathbb R
 \frac{R_\varepsilon(1/2+it)}{1/4+t^2}\,dt
 =\frac{\gamma_E-1}{\zeta(1+\varepsilon)}
  -\frac{\zeta'(1+\varepsilon)}{\zeta(1+\varepsilon)^2}
 =1-(1+\gamma_E)\varepsilon+O(\varepsilon^2),
 \qquad J_\varepsilon=K_\varepsilon-2L_\varepsilon+1.
 \tag{AR2}
\]
Consequently
\[
 K_\varepsilon=1+\{C_*-2(1+\gamma_E)\}\varepsilon+o(\varepsilon).
 \tag{AR3}
\]
Their upper estimate for \(K_\varepsilon-1\) is only \(O(\varepsilon)\); it does not supply the constant needed to bound \(C_*\) by \(Z/2\). Their Propositions1–3 also justify the fixed-\(\varepsilon\) approximation used next. No later-literature exhaustion or new asymptotic theorem is claimed here.

### 6.2 Original Euler coefficients and an exact real-variable norm

For \(\Re s>1\), the unchanged Euler product gives
\[
 R_\varepsilon(s)=\sum_{n\ge1}\frac{a_\varepsilon(n)}{n^s},\qquad
 a_\varepsilon(n)=\sum_{d\mid n}\mu(d)d^{-\varepsilon}
 =\prod_{p\mid n}(1-p^{-\varepsilon})\ge0.
 \tag{AR4}
\]
Set \(A_\varepsilon(x)=\sum_{n\le x}a_\varepsilon(n)\), zero for \(x<1\), and \(r_\varepsilon=1/\zeta(1+\varepsilon)\). The pointwise absolutely convergent identity
\[
 B_\varepsilon(x):=A_\varepsilon(x)-r_\varepsilon x
 =-\sum_{n\ge1}\mu(n)n^{-\varepsilon}\{x/n\}
 \tag{AR5}
\]
follows by expanding the integer parts. The tail is absolutely convergent since \(\{x/n\}=x/n\) for \(n>x\).

No critical-line convergence of the Euler series (AR4) is asserted. Instead truncate the **Möbius** sum in (AR5) at \(N\). Mellin Plancherel in \(L^2((0,\infty),dx/x^2)\), with transform \(\int f(x)x^{-s-1}dx\), maps that finite sum to
\(\zeta(s)\sum_{n\le N}\mu(n)n^{-s-\varepsilon}/s\).
The cited fixed-\(\varepsilon\) theorem proves convergence in this norm to \(R_\varepsilon(s)/s\). A subsequence and the pointwise identity identify its inverse transform with (AR5). Thus, with \(\chi=\mathbf1_{[1,\infty)}\),
\[
 \boxed{K_\varepsilon=\int_0^\infty B_\varepsilon(x)^2\frac{dx}{x^2},\quad
 L_\varepsilon=\int_1^\infty B_\varepsilon(x)\frac{dx}{x^2},\quad
 J_\varepsilon=\int_0^\infty|B_\varepsilon(x)-\chi(x)|^2\frac{dx}{x^2}.}
 \tag{AR6}
\]
The subtraction of \(r_\varepsilon x\) includes the pole at one on both sides of \(x=1\); it cannot be dropped.
This is the \(x=1/t\) form of the classical representation in
[Burnol, §4 and Lemma4.2](https://arxiv.org/pdf/math/0202166); the explicit cutoff and diagonal payment below are the comparison being recorded here.

For each fixed \(X>1\),
\(a'_0(n)=\Lambda(n)\) for \(n>1\) and \(r_\varepsilon=\varepsilon+O(\varepsilon^2)\), so
\[
 B_\varepsilon(x)-\chi(x)
 =\varepsilon(\psi(x)-x)+O_X(\varepsilon^2)\quad(1\le x\le X),
 \qquad
 \int_0^X|B_\varepsilon-\chi|^2\frac{dx}{x^2}=O_X(\varepsilon^2).
 \tag{AR7}
\]
Below one the residual is exactly \(-r_\varepsilon x\). Therefore all of the nonzero first-order \(J_\varepsilon\) mass escapes every fixed bounded \(x\)-interval. Differentiating (AR6) only on fixed intervals misses it.

### 6.3 Exact diagonal and divergent absolute correlation payment

Define the positive Gram kernel
\[
 G_{mn}=\int_0^\infty\{x/m\}\{x/n\}\frac{dx}{x^2}.
\]
The preceding norm convergence gives the **square-cutoff** identity
\[
 K_\varepsilon=
 \lim_{N\to\infty}\sum_{m,n\le N}
 \frac{\mu(m)\mu(n)}{(mn)^\varepsilon}G_{mn}.
 \tag{AR8}
\]
The diagonal has a closed form. With \(\kappa=\log(2\pi)-\gamma_E\),
\[
 G_{nn}=\frac\kappa n,\qquad
 D_\varepsilon:=\sum_{n\ge1}\mu(n)^2n^{-2\varepsilon}G_{nn}
 =\kappa\frac{\zeta(1+2\varepsilon)}{\zeta(2+4\varepsilon)}
 =\frac{\kappa}{2\zeta(2)\varepsilon}+O(1).
 \tag{AR9}
\]
For completeness, direct integration up to an integer \(M\) gives
\[
 \int_0^M\frac{\{x\}^2}{x^2}\,dx
 =2M-H_M-2M\log M+2\log(M!),
\]
whose limit is \(\kappa\) by Stirling's formula. Scaling proves the diagonal, and the absolutely convergent squarefree Euler product proves (AR9).

The corresponding sum with absolute Möbius coefficients diverges for every \(0<\varepsilon\le1/2\). Indeed, on a dyadic block \(M\le m,n<2M\), integration over \(0<x<M\) gives \(G_{mn}\ge M/(mn)\ge1/(4M)\). There are \(\gg M\) squarefree integers in that block: this follows directly from \(\mu^2(n)=\sum_{d^2\mid n}\mu(d)\), with error \(O(\sqrt M)\). The block's absolute double sum is therefore \(\gg M^{1-2\varepsilon}\); disjoint blocks diverge. Removing the diagonal does not change that conclusion.

Let \(O_\varepsilon\) denote only the off-diagonal sum in the cutoff order of (AR8). It exists, and
\[
 O_\varepsilon=1-D_\varepsilon+
 \{C_*-2(1+\gamma_E)\}\varepsilon+o(\varepsilon).
 \tag{AR10}
\]
Thus its signed terms cancel a diagonal of size \(1/\varepsilon\), first to bounded size and then to absolute precision \(O(\varepsilon)\). The latter is relative precision \(O(\varepsilon^2)\) against that diagonal. An exceptional double pair at height \(\gamma\) changes the coefficient by \(1/[2(\gamma^2+1/4)]\), so its detection asks for the corresponding absolute precision on the \(\varepsilon/(\gamma^2+1/4)\) scale.

This computation preserves the original Euler and Möbius coefficients and the full pole term. Nonnegative coefficients in (AR4) do not remove the signed cancellation in (AR8). Paying those correlations absolutely is not merely too large: that double payment diverges. No signed upper estimate for their first-order remainder has been proved here. This closes only that proposed separate-payment argument, not the arithmetic ratio route.

[Separate same-model continuation review, §7](../reviews/12_FINITE_PRECISION_SIGNED_KERNEL_AND_ENERGY_REVIEW_20261020.md).

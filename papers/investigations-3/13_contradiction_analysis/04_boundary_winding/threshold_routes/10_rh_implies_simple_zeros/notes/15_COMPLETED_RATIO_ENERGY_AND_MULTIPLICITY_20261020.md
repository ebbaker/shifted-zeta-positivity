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


## 7. Prime-error smoothing retains a multiplicity remainder

20 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, actual effort ultra**. Separate same-model internal checks;
no specialist review or novelty claim.

**Outcome.** The natural exponentially damped prime-error approximation has an explicit first-order squared remainder. It is zero at simple zeros and strictly positive at multiple zeros. Thus the original positive Euler coefficients and the checked RH prime-error mean square do not justify discarding this remainder. No opposing arithmetic bound is obtained.

### 7.1 The checked primary mean square retains squared multiplicity

Assume RH. Let \(\rho=1/2+i\gamma\) run over distinct nontrivial zeros of both signs, with multiplicity \(m_\rho\), and put
\[
 K=\sum_\rho\frac{m_\rho^2}{|\rho|^2},\qquad
 Z=\sum_\rho\frac{m_\rho}{|\rho|^2},\qquad
 C=\sum_\rho\frac{c_{m_\rho}}{|\rho|^2},\quad
 c_m=m\left(1-\binom{2m}{m}/4^m\right).
 \tag{PR1}
\]
All sums converge, as checked in Notes12 and15. Define
\(E(u)=e^{-u/2}(\psi(e^u)-e^u)\) for \(u\ge0\).
[Akbary–Ng–Shahabi, Corollary1.15(i)](https://arxiv.org/pdf/1306.1657) gives
\[
 \frac1U\int_0^U E(u)^2\,du\longrightarrow K.
 \tag{PR2}
\]
The source explicitly includes squared multiplicity. Its Theorem1.14 explains the Besicovitch Parseval step. For zeta the central-zero term in that corollary is absent. No simplicity, linear independence, or negative derivative-moment assumption is required for this prime-error statement; the source's separate Möbius statements have additional hypotheses. In particular (PR2) does not have constant \(Z\).

### 7.2 A justified exponential smoothing

Use \(\mathcal H=L^2((0,\infty),dx/x^2)\), and retain Note15's exact arithmetic residual
\[
 T_\varepsilon(x)=A_\varepsilon(x)-r_\varepsilon x-\mathbf1_{[1,\infty)}(x),
 \quad r_\varepsilon=\zeta(1+\varepsilon)^{-1},\quad
 A_\varepsilon(x)=\sum_{n\le x}\prod_{p\mid n}(1-p^{-\varepsilon}).
\]
Its norm is \(\|T_\varepsilon\|_{\mathcal H}^2=J_\varepsilon=C\varepsilon+o(\varepsilon)\).
The proposed first-order approximation is
\[
 P_\varepsilon(x)=\varepsilon x^{-\varepsilon}
                    (\psi(x)-x)\mathbf1_{[1,\infty)}(x).
 \tag{PR3}
\]
It agrees to first order on every fixed interval \(1\le x\le X\), including the correct original derivative \(a'_0(n)=\Lambda(n)\). Below one the exact residual is \(-r_\varepsilon x\), whose squared norm is \(O(\varepsilon^2)\). No full-norm approximation is assumed.

Let \(Q(U)=\int_0^U E(u)^2du=KU+o(U)\). Integration by parts gives
\[
 \|P_\varepsilon\|_{\mathcal H}^2
 =\varepsilon^2\int_0^\infty e^{-2\varepsilon u}E(u)^2du
 =2\varepsilon^3\int_0^\infty e^{-2\varepsilon u}Q(u)du
 =\frac K2\varepsilon+o(\varepsilon).
 \tag{PR4}
\]
This Abelian passage needs no rate in (PR2): split the error at a fixed \(U_0\), bound its tail by \(\eta U\), then let \(\eta\downarrow0\). The smoothing explores logarithmic distances \(u\) of order \(1/\varepsilon\), beyond the fixed intervals of Note15(AR7).

### 7.3 The complete Mellin identity and its local comparison

With Mellin transform \(\widehat f(s)=\int_0^\infty f(x)x^{-s-1}dx\), on \(\Re s=1/2\) we have exactly
\[
 \widehat T_\varepsilon(s)=\frac{\zeta(s)/\zeta(s+\varepsilon)-1}{s},
 \qquad
 \widehat P_\varepsilon(s)=\varepsilon\left[
   -\frac{\zeta'(s+\varepsilon)}{(s+\varepsilon)\zeta(s+\varepsilon)}
   -\frac1{s+\varepsilon-1}\right].
 \tag{PR5}
\]
The second formula first follows in \(\Re(s+\varepsilon)>1\); RH's bound for \(\psi(x)-x\) gives absolute convergence of its combined integral throughout \(\Re(s+\varepsilon)>1/2\), establishing continuation to the stated line. The apparent pole at \(s+\varepsilon=1\) cancels between the displayed terms. The first formula is Note15's paid fixed-shift norm identity. Thus the original coefficients, pole subtraction, and remaining zeta terms are retained.

At a fixed zero \(\rho\) of order \(m\), set \(s=\rho+i\varepsilon y\). Uniformly for bounded real \(y\),
\[
 \widehat T_\varepsilon(s)\longrightarrow
 -\frac{e_m(y)}\rho,\qquad
 \widehat P_\varepsilon(s)\longrightarrow
 -\frac{m}{\rho(1+iy)},\qquad
 e_m(y)=1-\left(\frac{iy}{1+iy}\right)^m.
 \tag{PR6}
\]
Every fixed multiple zero remains included. The regular analytic factors affect these compact local limits by \(o(1)\).

Put \(w(y)=(1+iy)^{-1}\). The elementary identities
\[
 \frac1{2\pi}\int|w|^2dy=\frac12,\qquad
 \frac1{2\pi}\int w(y)^k\overline{w(y)}\,dy=2^{-k}
\]
follow, for example, by Fourier Plancherel applied to
\(w(y)^k=\int_0^\infty e^{-t}t^{k-1}e^{-iyt}dt/(k-1)!\).
Expanding \(e_m=1-(1-w)^m\) therefore gives
\[
 \frac1{2\pi}\int e_m\overline w\,dy=1-2^{-m},\qquad
 d_m:=\frac1{2\pi}\int|e_m-mw|^2dy
 =c_m+\frac{m^2}2-2m(1-2^{-m}).
 \tag{PR7}
\]
In particular \(d_1=0\), \(d_2=1/4\), and \(d_3=21/16\). For every \(m\ge2\), the nonzero rational function \(e_m-mw\) has strictly positive squared norm, so \(d_m>0\).

### 7.4 All-zero exhaustion gives the exact remainder

For a finite set of distinct zeros, use the disjoint intervals
\(\gamma+\varepsilon[-Y,Y]\). Mellin Plancherel and (PR6) give the local norm limits. After \(Y\to\infty\), the local \(T\)-mass is \(c_m/|\rho|^2\) and the local \(P\)-mass is \(m^2/(2|\rho|^2)\). Their complete totals are respectively \(C\) and \(K/2\), by Note15 and (PR4). Thus both complementary norm masses tend to zero as the finite zero set is exhausted. On the complement,
\(|\widehat T-\widehat P|^2\le2|\widehat T|^2+2|\widehat P|^2\).
This pays every remaining zero and the region at infinity, and proves
\[
 \boxed{\lim_{\varepsilon\downarrow0}
 \frac{\|T_\varepsilon-P_\varepsilon\|_{\mathcal H}^2}{\varepsilon}
 =\sum_\rho\frac{d_{m_\rho}}{|\rho|^2}.}
 \tag{PR8}
\]
The sum is finite because \(d_m\le2c_m+m^2\). No uniform zero spacing or inverse-derivative bound is used. The order of limits is fixed finite set, \(\varepsilon\downarrow0\), \(Y\to\infty\), then all-zero exhaustion.

One exact double conjugate pair forces the right side of (PR8) to be at least
\[
 \frac1{2(\gamma^2+1/4)}.
 \tag{PR9}
\]
This is an actual error coefficient for the proposed arithmetic linearization, not just a triangle-inequality allowance. Its squared error is of order \(\varepsilon\), precisely the scale of \(J_\varepsilon\). The mean-square approximation has coefficient \(K/2\), not \(Z/2\); treating the full remainder as \(o(\sqrt\varepsilon)\) in norm would discard the multiple-zero contribution. The checked inputs give no signed bound that removes it. This assessment concerns (PR3) and its complete norm; it does not exclude other prime-error estimates or smoothing schemes.


## 8. The independent-prime Jensen bound loses a fixed variance

20 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, actual effort ultra**. Separate same-model internal checks;
no specialist review or novelty claim.

**Outcome.** The probabilistic representation of the original positive
coefficients is legitimate. Its Jensen upper allowance cannot be
`O(epsilon)`: the variance which it adds has liminf at least one as
`epsilon` tends to zero. This holds whether its full expected norm is
finite or infinite, and uses no random Euler product on the critical line.

### 8.1 Finite-prime construction and its legitimate limit

Fix `epsilon>0`. For each prime independently let `B_p` be Bernoulli
with mean `q_p=p^(-epsilon)`; `B_p=1` means that multiples of `p` are
excluded. Put
\[
 X_n=\prod_{p\mid n}(1-B_p),\quad
 A_\omega(x)=\sum_{n\le x}X_n,\quad
 D_\omega=\prod_p(1-B_p/p),\quad
 Y_x=A_\omega(x)-xD_\omega.
 \tag{RS1}
\]
For a finite prime set all products are finite, `A_omega-xD_omega` is
bounded and periodic, and its squared `dx/x^2` discrepancy norm is finite.
For the infinite model,
`E sum_p B_p/p=sum_p p^(-1-epsilon)<infinity`; hence that sum is finite
almost surely and `D_omega>0` exists. Finite-prime densities converge
boundedly. They also give the actual density: the upper density of
integers removed by the omitted primes is at most their convergent
reciprocal-prime tail. Explicitly, for the cutoff model retaining primes
at most `P`, uniformly in `x`,
\[
 0\le A_{\omega,P}(x)-A_\omega(x)
 \le\sum_{\substack{p>P,\ B_p=1\\p\le x}}\lfloor x/p\rfloor
 \le x\sum_{p>P,\ B_p=1}\frac1p.
\]
Primes exceeding `x` remove no integer in the count. Taking first
`x->infinity` and then `P->infinity` proves the asserted density without
using countable subadditivity of upper density.

Consequently
\[
 EX_n=a_\epsilon(n)=\prod_{p\mid n}(1-p^{-\epsilon}),\qquad
 ED_\omega=r_\epsilon=\prod_p(1-p^{-1-\epsilon})
                  =\zeta(1+\epsilon)^{-1},
 \quad EY_x=B_\epsilon(x).
 \tag{RS2}
\]
Here `B_epsilon=A_epsilon-r_epsilon x` is exactly Note15 §6's original
arithmetic function, and `chi=1_[1,infinity)`. Finite-prime variables
converge in mean square at each fixed `x` and in the joint weighted norm
on each bounded interval. No convergence of their full unbounded-interval
norms is inferred.

Pointwise covariance is fully explicit, for example
\[
 E(X_nX_m)=a_\epsilon(\operatorname{lcm}(n,m)),\quad
 E(X_nD_\omega)=r_\epsilon a_\epsilon(n)
      \prod_{p\mid n}(1-q_p/p)^{-1},\quad
 ED_\omega^2=\prod_p[1-q_p(2/p-1/p^2)].
 \tag{RS3}
\]
These retain the cross terms with the random density. Tonelli and the
pointwise variance decomposition yield the extended nonnegative identity
\[
 \mathbb E\int_0^\infty|Y_x-\chi(x)|^2\frac{dx}{x^2}
 =J_\epsilon+V_\epsilon,\qquad
 V_\epsilon=\int_0^\infty\operatorname{Var}(Y_x)\frac{dx}{x^2}.
 \tag{RS4}
\]
Under RH, `J_epsilon` is the actual finite direct-ratio norm of Note15.

### 8.2 A positive variance cost that Jensen cannot remove

For a finite nonempty set of primes `S`, put `d_S=product_(p in S)p` and
let `B_(epsilon,S)(u)` be the expectation of `A_omega(u)-uD_omega` when
primes in `S` are forced to be **unexcluded**. Its density is
`r_(epsilon,S)=r_epsilon product_(p in S)(1-q_p/p)^(-1)`.
The products of normalized centered Bernoulli variables
`Z_S=product_(p in S)(B_p-q_p)/sqrt(q_p(1-q_p))` are orthonormal.
Finite inclusion-exclusion gives exactly
\[
 E[Y_x Z_S]=(-1)^{|S|}
       \prod_{p\in S}\sqrt{q_p(1-q_p)}\,
       B_{\epsilon,S}(x/d_S).
 \tag{RS5}
\]
Indeed the coefficient involving every `B_p`, `p in S`, is the signed
count of surviving multiples of `d_S`, together with its corresponding
density subtraction. Averaging the other primes proves (RS5).

Apply Bessel's inequality to any finite family of these variables at each
`x`, then integrate and increase the family. This is legitimate even if
`V_epsilon` is infinite and gives
\[
 V_\epsilon\ge\sum_{\substack{\varnothing\ne S\\ S\text{ finite}}}
       \left(\prod_{p\in S}w_p\right)
       \int_0^\infty|B_{\epsilon,S}(u)|^2\frac{du}{u^2},
 \qquad w_p=\frac{p^{-\epsilon}-p^{-2\epsilon}}p.
 \tag{RS6}
\]
No critical-line random product or interchange of a signed infinite
correlation sum enters this bound.

Fix `X>2` and an integer `k>=1`, and restrict (RS6) to sets of `k` primes
all exceeding `X`. For `1<=u<=X` the coefficient count is unchanged by
forcing those primes to be unexcluded; it tends uniformly to one as
`epsilon` tends to zero. Also
`r_(epsilon,S)<=r_epsilon(1-1/X)^(-k)->0`, uniformly over these sets.
Therefore their norm factors are at least
`1-1/X-o_(X,k)(1)`.

The exact Euler logarithm and its absolutely convergent higher-power
tail show
\[
 W_\epsilon:=\sum_p w_p\longrightarrow\log2,
 \qquad \max_p w_p\longrightarrow0.
 \tag{RS7}
\]
For the first assertion compare
`log zeta(1+epsilon)-log zeta(1+2epsilon)`; the higher-prime-power
difference tends to zero by dominated convergence. For the second use
pointwise convergence at each prime and `w_p<=1/p`. Removing finitely
many primes does not change either limit. The elementary symmetric sum
of degree `k` in these weights consequently tends to `(log2)^k/k!`:
repeated-index tuples contribute at most
`binom(k,2)(max w_p) W_epsilon^(k-1)`.

For any fixed integer `K`, (RS6) thus gives
\[
 \liminf_{\epsilon\downarrow0}V_\epsilon
 \ge(1-1/X)\sum_{k=1}^K\frac{(\log2)^k}{k!}.
\]
First let `K` and then `X` tend to infinity. The conclusion is
\[
 \boxed{\liminf_{\epsilon\downarrow0}V_\epsilon\ge1.}
 \tag{RS8}
\]
Already the degree-one projection gives the lower constant `log2`.
Under RH the actual `J_epsilon=C_*epsilon+o(epsilon)` tends to zero,
while the Jensen allowance in (RS4) has liminf at least one. Thus this
particular positive averaging loses at least a reciprocal-shift factor
relative to the target scale.

**Scope.** Finiteness of the infinite expected discrepancy norm has not
been assumed or established here; (RS8) rules out its proposed sharp
`O(epsilon)` payment in either case. Finite-prime global norms cannot be
silently passed to the limit. The failure concerns replacing the exact
mean's squared norm by the expected random squared norm. It gives no
universal obstruction to retaining the signed covariances in (RS3), and
no simplicity exclusion.


### 8.3 Exact binary prime indicators leave no correlation freedom

20 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, actual effort ultra**. This is a scope clarification of
the existing variance obstruction, not another estimate or criterion.

Fix epsilon>0. Suppose random variables Y_p take values in {0,1}, and
the sieve variable is X_n=product_(p|n)Y_p. To reproduce the unchanged
Euler coefficients exactly, require

\[
 \mathbb E X_n=\prod_{p\mid n}(1-p^{-\epsilon})
 \quad\hbox{for every integer }n\ge1.
 \tag{RS9}
\]

Put r_p=1-p^(-epsilon). Every finite set S of primes occurs as the
support of a squarefree integer, so (RS9) determines all its mixed
moments. For disjoint finite sets A,B, inclusion-exclusion gives

\[
 \Pr(Y_p=1\ (p\in A),\ Y_p=0\ (p\in B))
 =\sum_{T\subseteq B}(-1)^{|T|}\prod_{p\in A\cup T}r_p
 =\prod_{p\in A}r_p\prod_{p\in B}(1-r_p).
 \tag{RS10}
\]

Thus the full finite-dimensional laws are forced to be independent.
Writing B_p=1-Y_p recovers exactly the law in (RS1), including its
random density and variance cost (RS8). Introducing correlations between
binary prime indicators while preserving (RS9) is therefore unavailable;
the nonvanishing Jensen loss applies to the whole class of exact binary
prime-product representations, not merely a voluntarily independent
choice. No independence was assumed in this argument.

The scope requires all integer coefficients at a fixed epsilon. Matching
only finitely many coefficients, permitting nonbinary weights or using
variables not of prime-product form leaves this class. The argument
does not analyze those representations or give an opposing signed bound.


## 9. Assessment of the complete heat-energy identity

20 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, actual effort ultra**. Separate same-model internal checks;
no specialist review or novelty claim.

Put \(\mathcal F_t(z)=8H(t,-2iz)\). Its complete original theta integral
gives \(\partial_t\mathcal F_t=\mathcal F_t''/4\). Under RH, retain all
zeros of its all-real heat continuation. For fixed \(\epsilon,\sigma>0\),
write, along \(z=iy\),
\[
 R=\frac{\mathcal F_t(iy)}{\mathcal F_t(\epsilon+iy)},\quad
 e=1-R,\quad
 b=\frac{\mathcal F_t'}{\mathcal F_t}(\epsilon+iy)=u+iv,\quad
 w(y)=\frac1{\sigma^2+y^2}.
 \tag{HE1}
\]
The ratio is unchanged by any nonzero scalar normalization of
\(\mathcal F_t\), including a time-dependent one. Such a normalization
adds the same scalar term to both heat equations, which cancels below.
Direct quotient differentiation gives the exact equations
\[
 R_t=\frac14R_{zz}+\frac12bR_z,\qquad
 e_t=-\frac14e_{yy}+\frac12v e_y-\frac i2u e_y .
 \tag{HE2}
\]
In particular the boundary-coordinate second derivative has the
anti-diffusive sign. With
\(J_A(t)=(2\pi)^{-1}\int_{-A}^A w|e|^2dy\), integration by parts gives
\[
\begin{split}
 J_A'(t)={}&
 \frac1{4\pi}\int_{-A}^A w|e_y|^2dy
 -\frac1{8\pi}\int_{-A}^A w''|e|^2dy
 -\frac1{4\pi}\int_{-A}^A(wv)'|e|^2dy\\
 &+\frac1{2\pi}\int_{-A}^A wu\,\operatorname{Im}(\bar e e_y)dy
 +\left[
 -\frac{w\operatorname{Re}(\bar e e_y)}{4\pi}
 +\frac{w'|e|^2}{8\pi}
 +\frac{wv|e|^2}{4\pi}
 \right]_{-A}^{A}.
\end{split}
\tag{HE3}
\]
Equivalently its interior is
\[
 \frac1{4\pi}\int_{-A}^A
 \left\{w|e_y+iue|^2-
 [wu^2+(wv)'+\tfrac12w'']|e|^2\right\}dy .
 \tag{HE4}
\]
Every drift, weight and boundary term is retained. No differentiation of
an improper integral or uniform positive-time local-zero count is used.

There is also a simple complete exterior payment. The paired product
gives \(|R|\le1\) on the imaginary axis, so for the full weighted energy
\(J(t)\),
\[
 0\le J(t)-J_A(t)\le\frac4{\pi A}.
 \tag{HE5}
\]
Consequently integrating (HE3) from \(0\) to \(t\), with
\(A=\epsilon^{-2}\), computes \(J(t)-J(0)\) up to
\(O(\epsilon^2)\), uniformly in the time interval on which the real-zero
continuation is used. The finite-window boundary expression in (HE3)
must still be included; it has not been asserted to vanish.

The RH sign of the full product drift is compatible with loss. Indeed,
with symmetric pairing in the imaginary part and all multiplicities
retained,
\[
 u=\sum_\lambda\frac{m_\lambda\epsilon}
                    {\epsilon^2+(y-\lambda)^2}>0,\qquad
 v_y=\sum_\lambda
 \frac{m_\lambda((y-\lambda)^2-\epsilon^2)}
      {(\epsilon^2+(y-\lambda)^2)^2}.
 \tag{HE6}
\]
Thus \(u^2+v_y\ge0\): each diagonal contribution is
\([m_\lambda(y-\lambda)^2+(m_\lambda^2-m_\lambda)\epsilon^2]/
[\epsilon^2+(y-\lambda)^2]^2\), and the cross terms of \(u^2\)
are nonnegative. This positive quantity appears with a minus sign in
(HE4). Positivity of the complete theta source gives finite compact
parameter moments and the mass covariance in Note15 (HR15). Neither
those bounds nor the displayed drift sign yields an \(o(\epsilon)\)
estimate over the crossover interval in this calculation.

For an exact normalization check take the local heat solution
\(\mathcal F_t(z)=z^2+t/2\) and the unweighted integral
\((2\pi)^{-1}\int_{\mathbb R}|e|^2dy\). At \(t=0\), after scaling
\(y=\epsilon Y\),
\[
 e=\frac{1+2iY}{(1+iY)^2},\quad
 b=\frac{2}{\epsilon(1+iY)} .
\]
The three nonzero interior terms in (HE3), in their displayed order
(derivative square, \(v_y\), imaginary cross term), are exactly
\[
 \frac1{8\epsilon},\qquad
 \frac1{8\epsilon},\qquad
 -\frac3{8\epsilon}.
 \tag{HE7}
\]
Their sum is \(-1/(8\epsilon)\), agreeing with
\[
 \frac d{dt}\left\{\epsilon
 \left[1+\frac1{4(1+t/(2\epsilon^2))}\right]\right\}
 =-\frac{\epsilon^3}{2(t+2\epsilon^2)^2}.
 \tag{HE8}
\]
The model's boundary terms vanish by its explicit rational decay. This
is a test of the heat and real-zero premises, not a replacement for the
original theta source. Note15 (HR7), (HR13) already pays the original
source's full exterior contribution and proves the corresponding
order-\(\epsilon\) loss at a hypothetical multiple endpoint.

**Assessment.** The exact PDE identity neither contradicts that loss nor
supplies its required opposing \(o(\epsilon)\) bound. An argument using
only the nonnegative derivative square, or discarding the imaginary
cross term in (HE3), fails by the explicit constants (HE7). No full
finite-parameter monotonicity of \(J(t)\) is claimed. The unresolved
arithmetic task remains a bound on the complete signed drift with the
unchanged source; the identity alone is not such a bound.

[Separate same-model continuation review, §8](../reviews/12_FINITE_PRECISION_SIGNED_KERNEL_AND_ENERGY_REVIEW_20261020.md).


### 9.1 Fixed-time dissipation and renormalized averaging

20 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, actual effort ultra**. Separate same-model internal checks;
no specialist review or novelty claim.

Retain Note15's notation
\[
J_t(\epsilon)=\frac1{2\pi}\int_{\mathbb R}
\frac{|1-\mathcal F_t(iy)/\mathcal F_t(\epsilon+iy)|^2}
{\sigma^2+y^2}\,dy,\qquad
M_\sigma(t)=\frac{\mathcal F_t'(\sigma)}
{\sigma\mathcal F_t(\sigma)} .
\]
Assume RH. The complete positive theta source gives
\(M_\sigma'(t)>0\), as already proved in (HR15).
Every fixed positive-time zero is simple, so (HR12) gives, for any fixed
\(0<t_1<t_2\),
\[
J_{t_2}(\epsilon)-J_{t_1}(\epsilon)
=\frac{\epsilon}{2}\{M_\sigma(t_2)-M_\sigma(t_1)\}
+o(\epsilon)>0
\quad\hbox{for all sufficiently small }\epsilon.
\tag{HI1}
\]
Thus the unrenormalized ratio energy is not globally dissipative even
for the unchanged theta source. This conclusion does not require a
multiple endpoint or real zeros at negative heat times.

There is a complete time-integrated statement. Fix \(T>0\) and any
fixed \(k\in L^1[0,T]\). The exact positive harmonic mass of (HR6) gives
\[
0\le\frac{J_t(\epsilon)}{\epsilon}
\le\frac{1-\mathcal F_t(\sigma)/\mathcal F_t(\sigma+\epsilon)}
{\sigma\epsilon}\le C_{\sigma,T}
\quad(0\le t\le T,\ 0<\epsilon\le\epsilon_0).
\tag{HI2}
\]
The last bound follows from positivity and joint analyticity at the
real points \(\sigma\le x\le\sigma+\epsilon_0\). The bound is for the
full spectral integral, so there is no unassigned height boundary.
For every \(t>0\) its limiting energy is \(M_\sigma(t)/2\).
Dominated convergence therefore proves
\[
\boxed{\lim_{\epsilon\downarrow0}\frac1\epsilon
\int_0^T k(t)J_t(\epsilon)\,dt
=\frac12\int_0^T k(t)M_\sigma(t)\,dt.}
\tag{HI3}
\]
Endpoint multiplicity does not appear in this limit. In particular
the fixed-time integrated excess
\(\int_0^T k(t)[J_t(\epsilon)-\epsilon M_\sigma(t)/2]dt\)
is \(o(\epsilon)\) even if the endpoint has a multiple zero.
Such an integrated bound cannot serve as its opposing estimate.
Weights concentrating on an \(\epsilon^2\) interval are outside this
fixed-\(L^1\)-weight assertion; their known nontrivial limit is (HR7).

A second candidate is to subtract half the exact harmonic mass:
\[
R_\epsilon(z)=\frac{F(z)}{F(z+\epsilon)},\qquad
H_\epsilon=\frac{1-R_\epsilon(\sigma)}{\sigma},\qquad
D_\epsilon=J_\epsilon-\frac12H_\epsilon.
\tag{HI4}
\]
For an even real entire function of order at most one with purely
imaginary zeros, its contractive ratio gives the exact Poisson identity
\[
D_\epsilon=\frac1{2\sigma}
\left\{\frac{\sigma}{\pi}\int_{\mathbb R}
\frac{|R_\epsilon(iy)|^2}{\sigma^2+y^2}\,dy
-R_\epsilon(\sigma)\right\}.
\tag{HI5}
\]
It is not always nonnegative. Take \(F(z)=\cosh(az)\), \(a>0\).
This has exact order one, all simple imaginary zeros, and a positive
even atomic Laplace source. Its full heat continuation is
\(\mathcal F_t(z)=e^{a^2t/4}\cosh(az)\), so the ratio is independent
of time and its zeros stay simple and imaginary for all real times.
Directly on the imaginary axis,
\[
\operatorname{Re}R_\epsilon(iy)
=\cosh(a\epsilon)|R_\epsilon(iy)|^2.
\]
Poisson integration therefore yields the explicit strict sign
\[
\boxed{D_\epsilon
=\frac{\cosh(a\sigma)}
{2\sigma\cosh(a(\sigma+\epsilon))}
\{\operatorname{sech}(a\epsilon)-1\}<0.}
\tag{HI6}
\]
This is an exact positive-source counterexample to the proposed
class-wide sign. It lacks theta's source tail, its completion and its
ordinary Dirichlet arithmetic; it does not refute a new estimate using
those unchanged data.

The conclusions are limited and quantitative: (HI1) rules out global
dissipation of the actual unnormalized energy, (HI3) shows the endpoint
is invisible to its first-order fixed-time averages, and (HI6) rules out
the proposed generic nonnegative renormalization. None supplies an
opposing estimate for Note15's endpoint crossover or a simplicity
exclusion.

[Separate same-model continuation review, §9](../reviews/12_FINITE_PRECISION_SIGNED_KERNEL_AND_ENERGY_REVIEW_20261020.md).

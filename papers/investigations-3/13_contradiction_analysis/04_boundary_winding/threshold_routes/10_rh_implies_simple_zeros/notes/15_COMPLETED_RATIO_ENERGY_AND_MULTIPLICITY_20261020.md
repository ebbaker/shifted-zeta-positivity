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

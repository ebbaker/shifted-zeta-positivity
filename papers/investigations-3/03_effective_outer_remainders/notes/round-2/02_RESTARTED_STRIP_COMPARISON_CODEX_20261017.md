# A restarted strip comparison consuming a global positive-time floor

17 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6-astra (Codex)**; reasoning effort: **ultra**.
**Status: proved in-note from named imports, with exact rational scalar gates;
internal same-model checks only.** The arithmetic hypothesis is proved and
Arb-certified in [Note 01](01_UNIFORM_FAMILY_FLOOR_CODEX_20261017.md).
Independent specialist review remains outstanding.

## Decision and precise consumer

The uniform arithmetic floor established in [Note 01](01_UNIFORM_FAMILY_FLOOR_CODEX_20261017.md) is

\[
 S_\chi(x,3,t)\ge6\qquad(x\in\mathbb R,\ 0\le t\le1/4)
 \tag{A}
\]

for all primitive characters with conductor at least \(10^{12}\), with the
usual real-entire normalization and initial zero strip \(|\Im z|\le1\).
The argument below then gives \(\Lambda_\chi\le43/200=0.215\). It needs
no confinement assertion H12 for the original character flow and no
vertical derivative estimate. The scalar calculation is deliberately
loose; the constant-floor limiting value is \(\log(9/2)/7\), approximately
0.214868, and no attempt to optimize toward that value is needed.

The current Project 01 sine-tail theorem consumes an initial floor.
Applying it once cannot consume (A) without losing most of the later
information. The correction is to restart its approximation argument at
finitely many original time slices. At each slice one transfers only a
short-time strip conclusion. One never assumes that the original
positive-time floor holds for its approximants.

## 1. One-step strip-transfer lemma

Let \(F\not\equiv0\) be real entire of order at most one, with zeros in
\(|\Im z|\le\sqrt q\), \(0<q\le1\), and let
\(F_s=e^{-s\partial_z^2}F\). Suppose
\[
 -\Im(F'/F)(x+3i)\ge C>0\qquad(x\in\mathbb R).
\]
For \(s\ge0\), write
\[
 m_C(s)=\frac{C e^{-s/2}}{1+2C(1-e^{-s/2})}.
\]
Choose a step length \(\delta>0\) and a number
\(3/4<c<m_C(\delta)\), and put \(k=4c/3-1>0\). Then the zeros of
\(F_\delta\) lie in
\[
 |\Im z|\le\sqrt{\max\{(q+2/k)e^{-k\delta}-2/k,0\}}. \tag{B}
\]
The assertion also holds for \(q=0\), with a zero right-hand side,
because heat evolution preserves real-rootedness in this class.

The general strip-operator input is Cardon, *Complex zero strip decreasing
operators*, arXiv:1401.0237v2, Theorem 1.5 and Lemma 1.3:
https://arxiv.org/html/1401.0237v2 . Applied with operator symbol
\(e^{-sz^2}\), it supplies the classical strip contraction for these
genus-one products. This is the same input used in Project 01 round 3;
the Fourier-only version alone would not cover the approximants.

### Proof: approximation and initial floor

Choose \(C_1<C\) sufficiently close to \(C\) that
\(m_{C_1}(\delta)>c\). Write the real canonical product
\[
 F(z)=a e^{bz}z^m\prod_{\rho\ne0}E_1(z/\rho),\qquad
 E_1(w)=(1-w)e^w,\quad a,b\in\mathbb R, a\ne0.
\]
Retain complete conjugate pairs with \(|\rho|\le R\), obtaining \(P_R\).
Choose \(\kappa=2(C_1+1)\), \(h=\pi/\kappa\),
\(M=\lfloor R/(4h)\rfloor\), and set
\[
 G_R=P_R L_M,\qquad
 L_M(z)=\prod_{j>M}(1-z^2/(j^2h^2)).
\]
These are real entire functions of exponential type. Their added zeros
are real, so their initial zeros retain the strip \(\sqrt q\).

For a real entire genus-one function whose zeros \(u+iv\) have
\(|v|\le1\), canonical regularization gives
\[
 S(x,3)=\sum_\rho\frac{3-v}{(x-u)^2+(3-v)^2}.
\]
The imaginary counterterms cancel by conjugation, and this positive sum
converges absolutely. For \(|x|\le R/2\), omitted zeros contribute at
most \(64\sum_{|\rho|>R}|\rho|^{-2}\to0\). For \(|x|\ge R/2\), the
remaining sine lattice has Poisson sum at least
\[
 \kappa\tanh(3\kappa)-\frac{24}{hR}-\frac{48}{R^2}.
\]
The first term exceeds \(C_1+1\). Positivity of the other contributions
therefore proves \(S_{G_R}(x,3,0)\ge C_1\) for every real \(x\), for all
sufficiently large \(R\).

### Proof: each approximant has a compact comparison

For each fixed \(R\), one may write
\(G_R(z)=e^{b_Rz}r_R(z)\sin(\kappa z)\), with real \(b_R\) and real
rational \(r_R\), whose real poles are canceled by sine zeros. If
\(r_R(z)=a_Rz^{d_R}(1+O_R(1/z))\), the Gaussian imaginary-translation
formula and a uniform rational expansion on its vertical integration
line give, on every fixed horizontal strip, uniformly for
\(0\le s\le\delta\),
\[
 \frac{(G_R)_s(z)}{a_Rz^{d_R}e^{b_Rz+(\kappa^2-b_R^2)s}}
 =\sin(\kappa(z-2b_Rs))+O_R(|\Re z|^{-1}).
\]
To justify the unbounded integral, the rational-expansion error is bounded
by \(O_R((1+|v|)^K/|\Re z|)\) at \(z+2i\sqrt s\,v\); the Gaussian
absorbs this polynomial and the sine's \(e^{2\kappa\sqrt\delta|v|}\).
Rouche disks about the real sine zeros contain exactly one zero for
large real part; reality makes that zero real. The sine is bounded away
from zero off these disks. Together with Cardon's strip theorem, this
confines every nonreal zero of each fixed approximant uniformly on the
step interval. No radius uniform in \(R\) is needed.

On height three put \(U=G_s'/G_s=u-iS\). The positive canonical sums
and strip \(|\Im\rho|\le1\) imply
\(|u_x|\le S/2\), \(|S_{xx}|\le S/2\). Burgers gives
\[
 S_s+2uS_x=-S_{xx}-2Su_x\ge-S/2-S^2.
\]
For each approximant the exponential-type bound, uniformly on the
bounded time interval, and the canonical logarithmic-derivative
difference (split the zero sum at \(|\rho|=2|x|\)) give \(|u(x,3,s)|\le K_R(1+|x|)\). Thus the real
characteristics \(x'=2u\) are complete and onto. Riccati comparison gives
\(S(x,3,s)\ge m_{C_1}(s)\ge m_{C_1}(\delta)>c\) throughout the step.

At a highest simple zero \(x+iy\), with \(Q=y^2\le1\), conjugate-pair
zero dynamics and the ordinary paired kernel inequality, valid because
\(3^2\ge5Q\), give
\[
 Q'\le-2-\frac43 S(x,3,s)Q+\frac{8Q}{9-Q}
 \le-2-kQ. \tag{C}
\]
The removed own conjugate pair is precisely the last correction term;
the linear canonical exponential contributes no imaginary velocity.
Compact attainment permits the usual strict-barrier argument. Multiple
contact is excluded by backward Hermite splitting: an earlier zero is
higher by a positive multiple of \(\sqrt v\), whereas a positive-height
smooth barrier moves by \(O(v)\). This local fact uses only the heat
equation: if the time-\(s_0\) Taylor expansion begins with
\(a(z-z_0)^m\), the earlier-time expansion under
\(e^{v\partial_z^2}\), after setting \(z-z_0=i\sqrt{2v}\,w\),
has leading term \(a(i\sqrt{2v})^m\operatorname{He}_m(w)\) and
an error \(O(v^{(m+1)/2})\) on bounded \(w\)-sets. The simple real
Hermite roots give zeros \(z_0+i\sqrt{2v}\lambda_j+O(v)\);
for \(m\ge2\) at least one \(\lambda_j>0\). Thus this step does
not assume a confinement theorem specific to the zeta function.
The classical strip bound keeps
contact heights \(Q\le q\le1\), including when the strict barrier is
initially perturbed above \(q\). It follows that the approximant's squared
zero strip is bounded by the positive part of
\((q+2/k)e^{-ks}-2/k\). At its first zero, continuity gives a real zero
set, preserved at later times. Equivalently one can first stop at every
positive target strip and pass that target to zero.

### Proof: transfer to the original function

For every fixed \(1<\sigma<2\), the canonical truncations satisfy
\(|P_R(z)|\le\exp(A(1+|z|)^\sigma)\), uniformly in \(R\). Indeed, \( |E_1(w)|\le\exp(C_\sigma|w|^\sigma)\) and
\(\sum_{\rho\ne0}|\rho|^{-\sigma}<\infty\) for every \(\sigma>1\);
these bounds are uniform over the truncations. Also
\(|L_M(z)|\le e^{\kappa|z|}\). Thus \(G_R\to F\) locally uniformly
with a common sub-Gaussian majorant. Dominated convergence through
\[
 F_s(z)=\pi^{-1/2}\int_{\mathbb R}e^{-v^2}F(z+2i\sqrt s\,v)\,dv
\]
gives \((G_R)_s\to F_s\) locally uniformly, uniformly for bounded
\(s\ge0\). The limit is nonzero: composing this Gaussian with its real
translation inverse gives the identity, by Fubini and the angular mean
of an entire function, justified by the same majorant. Hurwitz on the
two open regions outside the claimed strip proves (B). This completes
the one-step lemma.

## 2. Finite restart and the explicit 0.215 gate

Let the original heat orbit satisfy (A), and suppose its initial strip
has squared height at most one. Set
\[
 \delta=1/10000,\quad n=2150,\quad T=n\delta=43/200,
 \qquad c=1499/250,\quad k=4c/3-1=2623/375.
\]
At every \(t_j=j\delta\), apply the one-step lemma to the **original**
function \(F_{t_j}\). Its known floor is again six; its available strip
is the conclusion of the preceding step. The heat semigroup identity
identifies the continuation with \(F_{t_j+s}\). These time slices remain
real entire of order at most one: for each \(1<\sigma<2\), write
\(|F(z)|\le A_\sigma e^{B_\sigma|z|^\sigma}\) and use
\((a+b)^\sigma\le2^{\sigma-1}(a^\sigma+b^\sigma)\) inside the
Gaussian integral. On a bounded time interval this gives
\(|F_t(z)|\le A_{\sigma,T}'e^{B_\sigma'|z|^\sigma}\). Since the
argument works for every \(\sigma>1\), the order is at most one.
The same domination justifies the heat semigroup composition, so no
continuation hypothesis is being added at a restart. If a
zero strip has already been reached, real-rootedness persists.

For \(r=e^{-1/20000}\), the step-floor gate is
\[
 m_6(\delta)=\frac{6r}{13-12r}>1499/250
 \quad\Longleftrightarrow\quad
 e^{1/20000}<19488/19487. \tag{D}
\]
As long as the upper strip is positive, the recurrence is
\[
 Q_{j+1}=(Q_j+2/k)e^{-k\delta}-2/k,\qquad Q_0=1.
\]
If it stayed positive through all \(n\) steps, its terminal value would be
\((1+2/k)e^{-kT}-2/k\). But
\[
 e^{kT}=e^{112789/75000}>3373/750=1+k/2, \tag{E}
\]
so that value is negative. The positive-part recurrence must therefore
reach zero by \(T\). Hence \(F_T\) has only real zeros, proving the
conditional-on-(A) conclusion \(\Lambda_\chi\le43/200\).

Both gates have exact rational certificates. For \(x\ge0\), let
\(E_N(x)=\sum_{j=0}^N x^j/j!\), and for \(x<N+2\) let
\(\overline E_N(x)=E_N(x)+x^{N+1}/((N+1)!(1-x/(N+2)))\).
Then \(E_N\le e^x\le\overline E_N\). Direct fraction arithmetic verifies
\[
 19488/19487-\overline E_8(1/20000)>1.3150\cdot10^{-6},
\]
\[
 E_{20}(112789/75000)-3373/750>0.00165849.
\]
The [exact scalar certificate](../../numerics/round-2/certify_restarted_strip_consumer_20261017.py)
checks these inequalities without floating point decisions and records the
exact fractions in its [execution record](../../numerics/round-2/RESTARTED_STRIP_CONSUMER_SCALAR_GATES_20261017.json).

## Scope and dependencies

Combining this lemma with Note 01 proves, in the stated normalization,
\(\Lambda_\chi\le43/200\) for every primitive character of conductor
\(q\ge10^{12}\). The initial completed Dirichlet function is real entire
of order one with zero strip \(|\Im z|\le1\), as in
[Project 01 Note 01](../../../01_dirichlet_newman_families/notes/round-1/01_NORMALIZATION_AND_TRANSFER_CONTRACT_CLAUDE_20261017.md).
The arithmetic floor, the finite restart, and the exact gates are all
necessary parts of this conclusion. The scalar program alone proves
neither analytic input.

The approximation and initial-floor method extend
[Project 01 Note 03](../../../01_dirichlet_newman_families/notes/round-3/03_SINE_TAIL_LIMIT_AND_COMPARISON_CODEX_20261017.md).
The present additional step transfers an intermediate strip and restarts
from the original flow, making a positive-time arithmetic floor usable.
Cardon's general strip theorem is a named published input; the ordinary paired-kernel inequality is the elementary input of
Project 01 and the current manuscript, and the approximation argument
is written here.
No global confinement H12 for the original character flow, vertical
derivative certificate, or finite-height zero verification is assumed.

This is a quantitative sufficient estimate, classified under
[avoid 01](../../../../../avoid/01_restating_the_target.md); it is not an
RH-equivalent reformulation or a GRH conclusion. The continuation uses the
[result summaries](../../../../../result-summaries/README.md), especially
[the heat-flow summary](../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md),
and the [patterns to avoid](../../../../../avoid/README.md), especially
[unfinished sibling closures](../../../../../avoid/15_ignoring_sibling_results_and_unfinished_closures.md).
The [collision-control screen](../../../../../result-summaries/12_collision_controls_and_screening.md)
is carried out in Note 01. The generic lemma requires each control's own
actual floor; it does not assign primitive-character Euler estimates to
controls lacking those arithmetic premises.

The constant is a local improvement over the previously filed family
bound at this conductor scale. No literature-wide priority claim is made.
The separate zeta value \(0.18891\) remains conditional on the external
analytic estimates recorded in the round-one review.

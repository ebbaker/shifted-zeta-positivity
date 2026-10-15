---
research_program: PR01
secondary_programs: [PR03, COORD]
status: proved-elementary-budget-with-unresolved-imported-constant
---

# Explicit disc and weighted-remainder budgets with the imported constant isolated

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6.1-sol**, reasoning effort **ultra**, verified by the coordinating conversation. This is incremental research with internal LLM checking, not external refereeing or formal proof verification.

This continues [Note 39](39_CONVEX_DYADIC_WEIGHTED_REMAINDER_AUDIT_20261015.md) and [Note 41](../00_research_coordination/41_POISSON_OBSTRUCTION_AND_REMAINDER_CONTINUATION_20261015.md). It evaluates the elementary disc, Abel-summation, low-index, and imported Riemann--Siegel error budgets. It does **not** evaluate the exponent-pair constants. The new saving is a bookkeeping improvement on the existing domain, not a direct middle-interval saving and not a change of the theta threshold.

## 1. An explicit conditional constant package and the resulting bound

Use Note 17's analytic branches and carrier, and Note 32's five fixed assigned pairs and beta intervals. Set

\[
 \rho=\eta=10^{-5},\quad \theta_*=61/24,\quad
 \mu_*={21807\over254720000},\quad
 G_0={962773\over671},\quad
 \lambda=\mu_*-{63\over50}\rho>{1\over14000},
 \qquad A_0={36138917\over16}.
 \tag{1}
\]

The needed imported numerical package is the following: positive numbers \(C_j\) such that, for each of the five assigned pairs \((k_j,l_j)\),

\[
 \sup_{I\subset(M,2M]}
 \left|\sum_{n\in I}n^{-iT}\right|
 \le C_j T^{k_j+\eta}M^{l_j-k_j},
 \qquad M\ge1,\quad T\ge2\pi M.
 \tag{EP}
\]

Here \(I\) ranges over arbitrary integer intervals, including shortened terminal intervals. Put \(C_{\rm EP}=\max_j C_j\). If the supplied constants hold only for \(T\ge T_{\rm EP}\), also impose \(x-L^{-1}\ge3T_{\rm EP}\) below. The package includes the positive-loss specialization and any completion costs; limiting coordinates with zero loss are not being used.

The qualitative existence of such constants is the already audited input from [Bourgain, Theorem 6](https://arxiv.org/pdf/1408.5794v2) and [Trudgian--Yang, (1.1)--(1.2), Lemma 1.1, and the A-process](https://arxiv.org/html/2306.05599v3). Their cited statements do not supply numerical values for the \(C_j\) at this chosen loss. This note neither extracts them from their proofs nor replaces them by one. “Unevaluated” is not a claim of mathematical ineffectivity.

Assume

\[
 L=\log(x/(4\pi))\ge100002,\quad 0<t\le1/2,
 \quad tL\ge\theta_*,\quad |z-x|\le L^{-1}.
 \tag{2}
\]

Write \(z=u+iv\), \(\ell=\log(u/(4\pi))\),
\(\theta_u=t\ell\), \(w=w_\pm(z)=\sigma+i\tau\), and retain the exact cutoff

\[
 N_{\rm RS}=\left\lfloor\sqrt{e^\ell+t/16}\right\rfloor.
\]

Then each actual weighted sum obeys the fully explicit conditional estimate

\[
 \left|\sum_{n\le N_{\rm RS}}e^{t\log^2n/4}n^{-w}-\zeta(w)\right|
 \le {A_0\over\ell}+16e^{-\ell/40}
       +2G_0 C_{\rm EP}e^{-\lambda\ell}.
 \tag{3}
\]

In particular, the high-index term has the explicit majorant
\(2G_0 C_{\rm EP}e^{-\ell/14000}\). The improvement from Note 39's displayed exponent \(1/20000\) and its unspecified common constant comes from explicit disc geometry and a separate payment of the isolated final block. There is no new arithmetic input or search among pairs.

## 2. Explicit disc geometry

The carrier input is exactly

\[
 \alpha(s)={1\over2s}+{1\over s-1}
                +{1\over2}\operatorname{Log}{s\over2\pi},
 \quad s_\pm(z)={1\pm iz\over2},\quad
 w_\pm=s_\pm+{t\over2}\alpha(s_\pm).
\]

On (2), the elementary exponential lower bound gives
\(u\ge10^{12}\), \(\ell\ge L-1\ge100001\). More precisely,

\[
 |\ell-L|\le{1\over L(x-L^{-1})},\qquad
 |\theta_u-tL|\le{1\over2L(x-L^{-1})}<{\rho\over100}.
 \tag{4}
\]

Since \(|\Im s_\pm|=u/2\), the rational terms in \(\alpha\) have combined modulus at most \(3/u\). Also \(|s_\pm|\ge u/2\). Consequently

\[
 \sigma\ge\frac12+\frac{\theta_u}{4}-\delta,
 \quad \delta={1\over2L}+{3\over4u}<\rho/2,
 \quad \theta_u\ge\theta_0:=\theta_*-\rho/100.
 \tag{5}
\]

For the imaginary part, \(|\Im\alpha|\le\pi/4+3/u\), giving

\[
 \frac u2-\frac\pi{16}-\frac3{4u}
 \le T:=|\tau|
 \le\frac u2+\frac\pi{16}+\frac3{4u},
 \qquad u/3\le T\le u.
 \tag{6}
\]

In particular \(T\ge2\pi M\) for every block with \(M<N_{\rm RS}\). The optional imported threshold is met by the additional condition stated after (EP). The exact endpoint satisfies

\[
 \log N_{\rm RS}\le\ell/2+e^{-\ell}/64.
 \tag{7}
\]

These are actual sufficient disc thresholds, not limits with an unspecified “large enough” qualification. They are deliberately conservative and do not represent a usable finite bridge.

## 3. An explicit uniform low-index constant

Split at \(Y=e^{\ell/5}\). Equations (5) and \(e^q-1\le qe^q\) bound the low-index discrepancy by

\[
 {\theta_u\over4\ell}\sum_{n\ge2}(\log n)^2
           n^{-1/2-\theta_u/5+\delta}.
 \tag{8}
\]

Write \(\theta_u=\theta_0+s\), \(s\ge0\). Rational arithmetic gives

\[
 \frac12+\frac{\theta_0}{5}-\frac\rho2
             >1+\frac1{121}.
\]

For \(a_n=(\log n)/5\),

\[
 (\theta_0+s)e^{-a_ns}
 \le\theta_*+\frac1{e a_n}
 =\theta_*+\frac5{e\log n}.
\]

This retains uniformity when \(\theta_u\) grows. For \(j=1,2\), nonnegative unimodal sum--integral comparison gives

\[
 \sum_{n\ge2}(\log n)^j n^{-1-1/121}
 \le \int_1^\infty(\log y)^j y^{-1-1/121}\,dy
          +\sup_{y\ge1}(\log y)^j y^{-1-1/121}
 \le j!121^{j+1}+j^j=:D_j.
 \tag{9}
\]

One can verify the sum--integral bound by splitting at the maximum, comparing the increasing and decreasing sides with their adjacent unit integrals, and paying the single central discrepancy by the maximum. In particular \(D_1=14642\), \(D_2=3543126\). Since \(5/e<2\), (8) is at most

\[
 {\theta_*D_2+2D_1\over4\ell}={36138917\over16\ell}.
 \tag{10}
\]

Also (5) gives \(\sigma\ge9/8\). The entire ordinary zeta tail after \(Y\) is at most

\[
 8\lfloor Y\rfloor^{-1/8}\le16Y^{-1/8}=16e^{-\ell/40}.
 \tag{11}
\]

All parts of the zeta tail are paid; no cancellation in that tail is presumed.

## 4. High blocks: isolate the imported constant and keep a better margin

Use exactly Note 39's dyadic grid \(M_q=Y2^q\), shortened at the exact \(N_{\rm RS}\), with pair assignments by left beta endpoint. The actual positive weight
\(W(y)=e^{t\log^2y/4}y^{-\sigma}\) decreases on each block: by (5)--(7),

\[
 y(\log W)'=\frac t2\log y-\sigma
 \le-\frac12+\delta+e^{-\ell}/256<0.
\]

Exact Abel summation therefore costs \(W(M)\), since its endpoint and variation terms total
\(W(R)+\int_M^R|W'|=W(M)\). It does not introduce another factor two.

The only scaling conversion is

\[
 T^{k+\eta}\le(4\pi)^{k+\eta}e^{(k+\eta)\ell}
                         <2e^{(k+\eta)\ell},
\]

because every assigned \(k\le13/84\) and \(13/84+\eta<1/6\). Thus each block is bounded by

\[
 2C_{\rm EP}\exp\{\ell[F_{k,l}(\beta;\theta_u)+\delta\beta+\eta]\},
 \quad F_{k,l}(\beta;\theta)
 =k+(l-k-1/2)\beta-\frac\theta4\beta(1-\beta).
 \tag{12}
\]

For \(\beta\le1/2\), the explicit perturbation relative to \(\theta_*\) is at most

\[
 \eta+\rho/4+\rho/1600
      <(63/50)\rho.
 \tag{13}
\]

Use the same endpoint table and convexity identity as Note 39. On an assigned interval \([a,b]\) of width \(\Delta\), with \(d(\beta)=\min(\beta-a,b-\beta)\), this yields

\[
 F_{k,l}(\beta;\theta_u)+\delta\beta+\eta
 \le-\lambda-\frac{61\Delta}{192}d(\beta).
 \tag{14}
\]

The shifted-grid geometric summation from Note 39 pays every regular block, with the same rational upper multiplier \(G_0\). This proof does not require a grid endpoint to lie on a table boundary.

There is at most one left endpoint above \(1/2\): its excess is at most \(e^{-\ell}/(64\ell)\), whereas the beta spacing is \((\log2)/\ell>1/(2\ell)\). Assign this block to \(P\). Its exponent is at most

\[
 -\frac{11}{2688}
  +\rho\left(1+\frac1{1600}+\frac{33}{128}\right)
  +\frac1{32768}
 <-\frac1{300}<-\lambda.
 \tag{15}
\]

Here the last term bounds \(\theta_u(\beta-1/2)^2/4\) using \(\theta_u\le\ell/2\); all endpoint corrections are included. This isolated payment avoids reserving a full extra \(\rho\) on every regular block. Equations (12)--(15) and the exact dyadic summation prove the final term of (3).

## 5. The imported Riemann--Siegel errors can also be paid numerically

Apply the already matched two-branch [Polymath Theorem 1.3, (23)--(24)](https://arxiv.org/html/1904.12438v2#S1) on the upper half-disc. The following explicit consequences hold throughout (2):

\[
 e_A+e_B\le8\ell^2e^{-3\ell/4},\qquad
 e_{C,0}\le3e^{-2\ell/5}.
 \tag{16}
\]

For the first bound, the theorem's extra coefficient satisfies
\(|\gamma|N^{|\kappa|}n^v<2\). Indeed its logarithm is at most
\(1/(50L)+1/(2(u-6))+e^{-\ell}/(64L)\).
Each underlying positive heat weight is at most \(2n^{-1/2}\), since \(\log n\le\ell\) and the residual real-part loss is at most \(3/(4u)\). The complete positive weight sum, including the extra coefficient, is consequently at most \(24e^{\ell/4}\). The per-index exponential's argument is at most \(2\ell^2/u\le1\), so its error multiplier is at most \(4\ell^2/u\). Their product is \(96\ell^2e^{\ell/4}/u<8\ell^2e^{-3\ell/4}\).

For the second bound, the complete positive correction exponent in (24) is at most
\(10e^{-\ell/2}+\ell e^{-\ell}<1\). Hence its exponential is less than three. The remaining main exponent is
\(-\ell/4-\theta_u\ell/16\le-2\ell/5\), because \(\theta_u\ge\theta_0>12/5\). This pays the entire third imported error, including its explicit correction exponent.

There is also an explicit carrier comparison. On the disc,
\(|\alpha|\le\ell/2+1\), \(|\alpha'|\le2/u\). Thus

\[
 \left|\partial_z\log M_t(s_\pm(z))\right|
 \le( L/4+3/4)(1+1/(2u))<L/3.
\]

Integration along the straight segment from \(x\) to \(z\) gives
\(|M_t(s_\pm(z))|\le2\Gamma\), where \(\Gamma=|M_t(s_+(x))|\). No physical jet occurs in this comparison.

Let \(\mathcal A_t=Q_++Q_-\) be the same analytic comparison as Note 17. Combining (3), (16), and both carriers, and then using Schwarz reflection, yields on the entire disc

\[
 {|H_t(z)-\mathcal A_t(z)|\over\Gamma}\le B_C(L),
 \tag{17}
\]

where \(\Lambda=L-1\) and \(C=C_{\rm EP}\):

\[
 B_C(L)={4A_0\over\Lambda}+64e^{-\Lambda/40}
       +8G_0 C e^{-\lambda\Lambda}
       +16\Lambda^2e^{-3\Lambda/4}+6e^{-2\Lambda/5}.
 \tag{18}
\]

The substitution \(\ell\ge L-1\) is valid since every displayed function is decreasing on this log-height domain. Cauchy estimates now pay the normalized four-jet error of **this analytic replacement** by

\[
 \max_{0\le k\le3}
 { |\partial_x^k(H_t-\mathcal A_t)(x)|
       \over 2|Q|\,(L/4)^k}
 \le1728 B_C(L).
 \tag{19}
\]

Here \(\zeta(9/8)\le9\), \(|Q|\ge\Gamma/9\), and
\(\max_{k\le3} k!4^k(9/2)=1728\). The fixed-time derivatives are of the analytic difference; the floor cutoff is never differentiated. Equation (19) does not include the separate carrier differentiation error between \(\mathcal A_t\)'s jets and the phase vector. That remaining elementary stage must still be paid to obtain a numerical full sign threshold.

## 6. Exact remaining input and meaning of effective height

For a prescribed sum-replacement error \(0<\varepsilon<1\), (3) is at most \(\varepsilon\) whenever every disc point obeys

\[
 \ell\ge\max\left\{100001,
 {3A_0\over\varepsilon},
 40\log{48\over\varepsilon},
 14000\log{6G_0 C_{\rm EP}\over\varepsilon}\right\},
 \tag{20}
\]

together with the optional imported threshold. Choosing the real \(L\) at least one more than that maximum enforces it on the whole disc. This is a conditional formula in the **actual** imported constant, not an evaluated starting height. Equations (18)--(19) give the more direct conditional target for the analytic four-jet budget.

The next constant-extraction task is now unambiguous: supply numerical \(C_j\) and any source validity thresholds for (EP), at \(\eta=10^{-5}\), for arbitrary intervals and the exact logarithmic phase. The A-process constants, positive-loss choice, and any completion factor must be tracked. The cited qualitative exponent-pair statements alone do not determine those numbers. Their omission cannot be repaired by putting \(C_{\rm EP}=1\).

No part of this calculation removes Note 39's positive weighted exponent throughout its five-halves middle interval. Changing a constant or a logarithmic multiplier cannot remove that positive power in the fixed majorants. A new direct weighted cancellation argument or a genuinely stronger arithmetic input is still required there. No new sign domain, finite bridge, or RH conclusion results. The finite certificate through 112 and the manuscript remain unchanged.

## 7. Reproducible checks and limits

The accompanying [checker](../../numerics/check_explicit_weighted_budget.py) and [receipt](../../numerics/EXPLICIT_WEIGHTED_BUDGET_CHECKS_20261015.json) record **50 exact rational assertions**, including the explicit disc allowances, low-index coefficient, improved surviving margin, unchanged endpoint margins, geometric multiplier, exceptional endpoint, RS correction allowances, and Cauchy normalization. The receipt records the checker's source hash.

The checker audits finite arithmetic. It does not independently prove the imported arithmetic theorems, the unimodal comparison, Abel summation, infinite geometric-series argument, complex-disc reasoning, or the primary Riemann--Siegel theorem. Those analytic arguments are supplied above. It does not enclose any actual stationary root or finite-height observation.


Replay using the Python standard library:

    python3 papers/investigations-2/active/21_quaternion_theta_geometry/numerics/check_explicit_weighted_budget.py --output /tmp/inv21-explicit-weighted-budget-replay.json

A separate internal execution reproduced all 50 assertions and the receipt bytes. [Review 28](../../reviews/28_LOCALIZED_POISSON_AND_EFFECTIVE_BUDGET_REVIEW_20261015.md) records the independent analytic and primary-source audit.

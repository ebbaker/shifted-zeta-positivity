# E03 r1 finite exponent-pair envelope and canonical width

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Subagent dispatch
**gpt-6.1-sol / ultra**. Backend configuration beyond that dispatch is
unavailable.

**Status.** Proved in-note from the E02 and HDA inputs, proof-author
checked and pending additional-agent review. This executes [E03 r1][packet]
using the same field, carrier and clock as [E02 r1][e02packet].
The [rational record][checks] checks the finite arithmetic.
See [result summaries][results] and [patterns to avoid][avoid], with
[heat-flow cluster11][r11], [controls12][r12], [classification01][a01],
[premise02][a02] and [scope07][a07]. The result is a quantitative
width along a prescribed positive-time curve.

## 1. Exact envelope for the prescribed pairs

Let \(A(k,l)=(k/(2k+2),(k+l+1)/(2k+2))\). The pairs are
\[
 (k_j,l_j)=A^j(1/6,2/3),\qquad
 k_j=(2^{j+3}-2)^{-1},\quad l_j=1-(j+2)k_j,\quad
 d_j=1+k_j-l_j=(j+3)k_j .
\]
The closed forms follow from \(k_{j+1}^{-1}=2+2k_j^{-1}\) and
\(1-l_{j+1}=(1-l_j+k_j)/(2k_j+2)\). These are exponent pairs
by [Montgomery–Vaughan][mv], Theorems 16.23 and 16.25.
Define \(g_j(v)=k_j/v-d_j+v/4\) on \(0<v\le1/2\). The affine
functions \(v(g_j(v)-v/4)=k_j-d_jv\) for \(j-1,j\) meet at
\[
 v_j=\frac{2^{j+2}}{(j+1)2^{j+2}+2}\qquad(j\ge1).
\]
The \(j\)-line has a smaller intercept, so is lower for \(v<v_j\).
The \(v_j\) decrease strictly to zero because the reciprocals
\(j+1+2^{-j-1}\) increase strictly. Repeated adjacent comparisons
place \(g_j\) on \([v_{j+1},v_j]\) for \(j\ge1\), and \(g_0\)
on \([v_1,1/2]\). This also proves attainment of the minimum
for each \(v>0\).

Put \(q_*=351/10304\) and \(v_*=v_4=32/161\). For \(0<v\le1/8\),
\(k_j,d_j\to0\) gives \(\min_j g_j(v)\le v/4\le1/32<q_*\).
On \([1/8,1/2]\) use the six frozen intervals below.
Each \(g_j''(v)=2k_j/v^3>0\), so the endpoints bound its values above.

| \(j\) | \(v\) interval | \(g_j\) at left | \(g_j\) at right |
| --- | --- | --- | --- |
| 5 | \([1/8,64/385]\) | \(1/32\) | \(1663/49280\) |
| 4 | \([64/385,32/161]\) | \(1663/49280\) | \(351/10304\) |
| 3 | \([32/161,16/65]\) | \(351/10304\) | \(63/2080\) |
| 2 | \([16/65,8/25]\) | \(63/2080\) | \(7/400\) |
| 1 | \([8/25,4/9]\) | \(7/400\) | \(-1/72\) |
| 0 | \([4/9,1/2]\) | \(-1/72\) | \(-1/24\) |

Every entry is at most \(q_*\). The ordered crossings show that
\(g_3(v_*)=g_4(v_*)=q_*\) is the minimum there. Consequently
\[
 \max_{0<v\le1/2}\min_{j\ge0}g_j(v)=q_*,
 \qquad \gamma=\tfrac12+2q_*=\frac{2927}{5152}.                   \tag{1}
\]

## 2. Canonical transfer

Fix \(\gamma<y_0\le7/12\), \(\rho=y_0-\gamma\) and
\(\omega=\min(\rho/32,1/4096)>0\). For
\(x=\Re z,\ |x-X|\le1,\ y_0\le y=\Im z\le9/8\), use
\(L_x=\log(x/(4\pi))\), \(\lambda_X=1/L_X\) and
\(c_x=\lambda_X L_x\). Freeze \(\lambda_X\) across the rectangle.
Inherit [E02 Note09][e02] and [E01 Note06][e01] for the
fixed \(r=1,b=9\) provider, chart and Gaussian gates, carrier,
cutoff and correction. At each chart recentered at \(x\), use
\(N=N_x=\lfloor\exp(L_x/2)\rfloor\) and the exact decomposition
\(H_\lambda/C_-=D_N+R_N+Q_N+E_N\), where
\[
 D_N=\sum_{n\le N_x}n^{-s_\lambda(z)}e^{\lambda(\log n)^2/4},
 \qquad s_\lambda(z)=\tfrac{1-iz}{2}+\tfrac{\lambda L(z)}4
                               -\tfrac{i\pi\lambda}8 .
\]
Here \(L(z)=\operatorname{Log}(z/(4\pi))\). All terms are value
comparisons with the same provider constants across cutoff transitions.

Impose \(|c_x-1|\le\epsilon_\rho:=\min(10^{-4},\rho/16)\).
This holds throughout \(|x-X|\le1\) once
\(1/((X-1)L_X)\le\epsilon_\rho\). Since \(\Re L(z)\ge L_x\),
\[
 \Re s_\lambda\ge(1+y)/2+c_x/4
 \ge1+q_*-\tfrac14\,10^{-4}>1+\tfrac1{32}.
\]
The ordinary [Dirichlet series and Euler product][zeta] give
\(|1/\zeta(s_\lambda)|\le1+1/(\Re s_\lambda-1)\le33\).
The elementary \(C_-\) and this zeta factor are analytic
and nonzero on a neighborhood of the closed rectangle.

Put \(K=\lfloor\exp(L_x/8)\rfloor\). For \(n\le K\),
\[
 |n^{-s_\lambda}e^{\lambda(\log n)^2/4}|
 \le n^{-[(1+y)/2+7c_x/32]}
 \le n^{-1-1/512},
\]
since \(q_*-1/32-7\cdot10^{-4}/32=143873/51520000>1/512\).
Apply \(e^u-1\le u e^u\) to remove the heat weight on the finite
prefix at cost \(A_*/L_X\), where
\(A_*=\tfrac14\sum_{n\ge2}n^{-1-1/512}(\log n)^2<\infty\).
The ordinary series beyond \(K\) costs \(32K^{-1/32}\ll x^{-1/256}\)
once \(\exp(L_x/8)\ge2\). All heat-weighted terms are finite.

For \(K<n\le N_x\) split at \(\exp(vL_x)\) for the table
endpoints. Use dyadic blocks starting at each left real endpoint
\(M\), clipping the last block at the right endpoint. Use pieces
open on the left and closed on the right to keep every integer
once. There are \(O(1+L_x)\) blocks. [Montgomery–Vaughan][mv],
Definitions 16.1–16.2 and (16.55)–(16.58), give partial sums
\(O(x^{k_j}M^{l_j-k_j}+M/x)\) on arbitrary subintervals.
The phase is exactly \(T\log n\), \(T=|\Im s_\lambda(z)|\asymp x\).
In the source's \(e(f)\) convention the derivative parameter is
1 and the scale is \(T/(2\pi)\), with phase sign handled by
conjugation. The exact complex-\(L\) correction is included in \(T\).

Abel summation costs the starting weight times a constant on each
clipped block. Its logarithmic derivative times \(u\) is
\(-\Re s_\lambda+\lambda\log u/2=O(1)\) for
\(1\le u\le\exp(L_x/2)\), giving the requisite supremum and
variation. The primary weighted exponent of \(x/(4\pi)\) at
\(v=\log M/L_x\) is at most
\[
 k_j+\bigl(l_j-k_j-(1+y)/2-c_x/4\bigr)v+c_x v^2/4 .
\]
At \(c_x=1\) this is \(v[g_j(v)-(y-1/2)/2]\le-\rho/16\),
since \(v\ge1/8\) and \(g_j\le q_*\). Clock variation costs at most
\(|c_x-1|(v-v^2)/4\le\rho/256\), so \(15\rho/256>\omega\)
is available. The secondary term costs \(O(x^{-1/2})\) per block
because the dominant weight is at most 1 and \(M\ll\sqrt x\).
The complete finite tail costs \(O((1+L_x)x^{-\omega})\);
only the six fixed pairs enter its constant.

For the reflected population the weight is
\(u^{(y-1)/2}\exp(\lambda[(\log u)^2-\Re L(z)\log u]/4)\).
The exact phase frequency is \(x/2+\pi\lambda/8+\lambda\Im L(z)/4\)
and its amplitude logarithmic derivative times \(u\) is \(O(1)\).
Use pair \(j=0\) on the whole integer range and
\(|C_+/C_-|\ll x^{-y/2}\) as in E02. The primary exponent
\(1/6-y/2+(y/2-c_x/4)v+c_xv^2/4\) is convex on \([0,1/2]\).
At \(v=0,1/2\) it is at most
\(1/6-9/32\) and \(1/6-9/64-(1-10^{-4})/16\), respectively,
using \(y_0>\gamma>9/16\). Both are below \(-1/32\).
The secondary term costs \(O(x^{-1/2})\) per block since the
weight is at most \(M^{1/16}\) and \(x^{-y/2}M^{17/16}/x\ll x^{-1/2}\).
The full reflected contribution is \(O((1+L_x)x^{-1/32})\).

The inherited bounds on the correction and remainder are
\[
 Q_N=O(x^{-(1+y)/4}),\qquad E_N=O(x^{-3/4})(1+O(x^{-y/2})).
\]
The correction uses the bounded removable quotient at every
fractional cutoff. The remainder includes both carrier envelopes
and the true and linearized Gaussian tails. The clock gate gives
\(0<\lambda_X L_x\le8\) at nonnegative time. [E02 proof][e02].

Summing the payments gives a finite constant \(B\) with
\[
 \sup_{\substack{|x-X|\le1\\y_0\le y\le9/8}}
 |H_{\lambda_X}(z)/C_-(\lambda_X,z)-\zeta(s_{\lambda_X}(z))|
 \le A_*/L_X+B(1+L_X)(X-1)^{-\omega}.                            \tag{2}
\]
The constants are uniform in \(y_0\in(\gamma,7/12]\) under the
\(y_0\)-dependent gates. Require \(X-1\) above the full fixed
provider and cutoff onsets of E01/E02, \(X\ge2\), \(L_X\ge64\),
\(\exp(L_{X-1}/8)\ge2\), the clock gate, and 33 times the
right side of (2) at most \(1/64\). All hold eventually for
each fixed \(y_0\). The exact normalized field
\(H_{\lambda_X}/(C_-\zeta(s_{\lambda_X}))\) is then within
\(1/64\) of 1 on the closed rectangle. The known initial
width \(1\) and [Polymath v2 Theorem 3.2][poly] give width
\(\sqrt{1-2/L_X}<1\) at this time. Combining with (2) and
conjugation yields, for a finite onset \(X_*(y_0)\),
\[
 X\ge X_*(y_0),\quad H_{\lambda_X}(X+iy)=0
                  \quad\Longrightarrow\quad |y|<y_0.              \tag{3}
\]
At \(y_0=4/7\), \(\rho=17/5152\), \(\omega=17/164864\) and
\(\epsilon_\rho=10^{-4}\). The onset is unevaluated and depends on
\(y_0\). Equations (2)–(3) apply on the prescribed time curve.

## 3. Scope of the exact threshold and control screen

At \(x=X\) the clock is exactly \(c_x=1\).
For a fixed absolute head exponent \(a\), the stated summable
power majorant needs \(a<4\delta\), \(\delta=(y_0-1/2)/2\),
since the worst head exponent is \(1+\delta-a/4\).
For \(1/2<y_0\le\gamma\), \(4\delta\le4q_*<v_*\), so the
intermediate scale \(v_*\) is beyond any such head. The best
displayed separate \(A\)-chain power there is
\(v_*(q_*-\delta)\ge0\). If dyadic clipping moves \(v\) by
\(O(1/L_x)\), all functions \(E_j(v;y_0)\) have bounded first
derivatives uniformly in \(j\) near \(v_*\) because
\(k_j,d_j\) are bounded. The lower envelope thus changes by
\(O(1/L_x)\), so clipping cannot provide a fixed strict power
at this scale. For \(y_0\le1/2\) the head majorant and Euler floor
already lack their strict margins. This establishes the threshold
for the stated head and separate tail power allowances.
Other pairs, cross-block cancellation, a logarithmic endpoint
gain and different head comparisons or clocks remain outside
this scope. The calculation leaves the actual canonical error
at \(y_0=\gamma\) unresolved.

For the [collision controls][r12], Euler-factor and translated
sources fail the unchanged unit-coefficient identification.
Weighted squares, finite-tail changes and finite-prime orbits
fail complete coefficients and full reflection together.
Reflected super-Gaussian, smooth and positive-primitive controls
fail the canonical arithmetic square expansion. Atomic,
finite-profile and compact continuous controls fail complete
source and coefficient identification beyond their observations.
RH-conditional endpoint controls fail ordinary Dirichlet
arithmetic. Variable readouts fail the true cosine/Newman
evolution. Relaxed positive measures fail identification with
the exact integer zero divisor. If a control has a zero inside
the box and a nonvanishing carrier there, its relative deviation
at that point is 1. The witness need not occur in the prescribed
high-height box on this time curve.

[packet]: ../research-progress/handoffs/GNP-BB-E03-r1.md
[e02packet]: ../research-progress/handoffs/GNP-BB-E02-r1.md
[e02]: 09_GNP_BB_E02_SIGNED_TAIL_WIDTH_20261113.md
[e01]: 06_GNP_BB_E01_COMPLETE_OUTER_ESTIMATE_20261113.md
[checks]: ../numerics/05_GNP_BB_E03_INPUTS_AND_CHECKS_20261113.json
[mv]: https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf#page=44
[zeta]: https://dlmf.nist.gov/25.2
[poly]: https://arxiv.org/html/1904.12438v2#S3
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[r12]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md

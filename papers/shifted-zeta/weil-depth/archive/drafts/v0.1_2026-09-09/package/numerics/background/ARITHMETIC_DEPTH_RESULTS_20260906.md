# Arithmetic-depth continuation: central certificates and the next obstruction

6 September 2026. Continuation of `ARITHMETIC_DEPTH_STRATEGY_20260906.md`.

## 1. Results and their status

The central-first strategy produces two new complete finite-horizon **working certificates**, through total horizons \(\log4\) and \(\log5\). Each combines a newly computed finite head, the full output Gram matrix, an analytic bound on the infinite tail, and outward interval LDL validation. They do not use the disputed first-slab matrix archives or an external central-window certificate.

Let \(V_{\omega,L}\) be the causal transfer on \(L^2(0,L)\), and let \(Q_{\omega,L}\) be its symmetric logarithmic-generator form. The resulting bounds are:

| Total horizon | Active prime powers in the central generator | Central lower bound \(Q_{0,L}\ge mI\) | New certified shift range | Transfer bound on that range |
|---|---|---:|---:|---|
| \(\log4\) | 2, 3 | \(m=5\times10^{-13}\) | \(0<\omega\le4\times10^{-7}\) | \(\|V_{\omega,L}\|\le e^{-2.5\times10^{-13}\omega}\) |
| \(\log5\) | 2, 3, 4 | \(m=10^{-18}\) | \(0<\omega\le4\times10^{-10}\) | \(\|V_{\omega,L}\|\le e^{-5\times10^{-19}\omega}\) |

Compression gives the same transfer bounds at every smaller horizon. In particular, the second row crosses the first repeated-delay threshold, \(\log4\). At a threshold itself the newly appearing delay is zero almost everywhere, so the endpoint convention is strict: \(\log n<L\).

These are computer-assisted working certificates with an explicit analytic and arithmetic error budget. They are not a formal proof-assistant verification or a completed independent audit. The finite matrices are constructed with exact rational profile coefficients and 400-digit Decimal arithmetic; the final sign decisions use outward intervals. The report distinguishes the analytic reduction, the a priori rounding budget, and additional floating-point diagnostics.

At \(L=9/5=1.8>\log6\), the complete sufficient inequality remains **not certified**. An initial coupling bound failed; retaining exact reflection-parity coupling improved the reduction; increasing the head from 80 to 96 modes improved it further but did not close it. The 96-mode central head itself passes an interval positivity check. The remaining obstruction is quantitatively in the head-to-tail comparison, not a detected negative direction of the full central form.

No RH conclusion follows from this finite list. The second-slab gap between \(4\times10^{-5}\) and \(0.05\), and the unresolved first-slab primary-Arb audit, are unchanged.

## 2. General generator and the continuation lemma

Write \(T_d f(x)=\mathbf1_{x>d}f(x-d)\). On any finite horizon,

\[
V_{\omega,L}=B_{\omega,L}V^\gamma_{\omega,L},\qquad
B_{\omega,L}=\sum_{\log n<L}b_\omega(n)T_{\log n},
\]

\[
b_\omega(n)=n^{\omega-1/2}\prod_{p\mid n}(1-p^{-2\omega}).
\]

The finite, commuting, nilpotent delay algebra gives the exact Euler factorization

\[
B_{\omega,L}=\prod_{\log p<L}
(I-p^{-1/2-\omega}T_{\log p})
(I-p^{-1/2+\omega}T_{\log p})^{-1}.
\]

Every inverse is a terminating geometric series. Differentiating its logarithm gives, on the common generator core,

\[
A_{\omega,L}:=-\partial_\omega V_{\omega,L}V_{\omega,L}^{-1}
=A^\gamma_{\omega,L}
-2\sum_{\log n<L}\frac{\Lambda(n)}{\sqrt n}
\cosh(\omega\log n)T_{\log n}.
\]

Here the inverse notation expresses the generator identity on the range/core; a bounded inverse of the smoothing transfer on all of \(L^2\) is not being asserted. Consequently,

\[
Q_{\omega,L}=Q^\gamma_{\omega,L}
-\sum_{\log n<L}\frac{\Lambda(n)}{\sqrt n}
\cosh(\omega\log n)(T_{\log n}+T_{\log n}^*).
\]

This generator is even in \(\omega\). Composite integers with two distinct prime factors occur in the transfer through products of Euler factors; they do not create new generator terms. Thus \(n=6\) first tests mixed compositions in the transfer, although \(\Lambda(6)=0\).

For the gamma part, put

\[
r(t)=e^{t/2}-\frac{e^{-5t/2}}{1-e^{-2t}}.
\]

The bounded difference \(Q^\gamma_{\omega,L}-Q^\gamma_{0,L}\) has kernel
\((\cosh(\omega|x-y|)-1)r(|x-y|)\). Since
\(|r(t)|\le e^{t/2}+1/(2t)\), for \(0\le\omega\le1/2\) one may use

\[
\|Q_{\omega,L}-Q_{0,L}\|\le C_L\omega^2,
\]

\[
C_L\le\cosh(L/2)\left(e^{L/2}\frac{L^3}{3}+\frac{L^2}{4}\right)
+\frac12\sum_{\log n<L}\frac{\Lambda(n)}{\sqrt n}
(\log n)^2\cosh(\log n/2)\|T_{\log n}+T_{\log n}^*\|.
\tag{2.1}
\]

This is a norm bound on the bounded difference of forms, not on either unbounded central generator separately. The code encloses (2.1) and verifies \(C_{\log3}<1.5\), \(C_{\log4}<4\), and \(C_{\log5}<7\).

If \(Q_{0,L}\ge mI\), the energy identity gives

\[
\frac{d}{ds}\|V_{s,L}f\|^2
=-2Q_{s,L}[V_{s,L}f]
\le-2(m-C_Ls^2)\|V_{s,L}f\|^2.
\]

Integrating from \(\varepsilon>0\) and then using the strong limit \(V_{\varepsilon,L}f\to f\) yields

\[
\boxed{\|V_{\omega,L}\|\le\exp(-m\omega+C_L\omega^3/3).}
\tag{2.2}
\]

The gamma logarithmic generator has the common form domain already used in the energy argument; the finitely many arithmetic delays and the displayed gamma difference are bounded perturbations. One can first differentiate on a smooth core at positive shift, apply the inequality there, and then use density and the strong zero-shift limit. No operator-norm derivative at zero is used.

For the two new rows, the rational inequalities \(m-C_Lh^2/3\ge m/2\) verify the stated choices of \(h\). The inherited second-slab endpoint result similarly yields \(Q_{0,\log3}\ge10^{-9}I\), and (2.2) gives

\[
\|V_{\omega,L}\|\le e^{-2\times10^{-10}\omega},\qquad
0<\omega\le4\times10^{-5},\quad L\le\log3.
\]

That last central floor is extracted from the supplied small-shift norm certificate by differentiating scalar norms on the core and closing the form. Its certificate qualifications are inherited. The new \(\log4\) and \(\log5\) central computations are independent of that numerical input.

## 3. A central infinite-tail bound that works beyond the second slab

Let \(P_N\) retain the first \(N\) normalized shifted Legendre polynomials, of degrees \(0,\ldots,N-1\). Introduce the central profile

\[
G_0(t)=\frac{e^{t/2}t}{\sinh t}-4t\cosh(t/2)
=\sum_{j\ge0}g_jt^j,
\]

with \(g_0=1\), \(g_1=-7/2\), \(g_2=-1/24\), and \(w(t)=(G_0(t)-1)/t\). If \(U_1^\gamma=\partial_\omega V^\gamma_\omega|_0\), then

\[
U_1^\gamma=\left.\partial_\nu[(2\pi)^\nu I_\nu]\right|_{\nu=0}+S_w,
\]

where \(I_\nu\) is causal fractional integration and \(S_w\) is causal convolution by \(w\).

### 3.1 The logarithmic fractional part

The terminating Jacobi formula and Jacobi orthogonality give

\[
\|I_\nu(I-P_N)\|\le(L/2)^\nu
\sqrt{\frac{\Gamma(N+1-\nu)}{\Gamma(N+1+\nu)}},\qquad 0<\nu<1.
\tag{3.1}
\]

Indeed, fractional integration sends the degree-\(n\) shifted Legendre polynomial to a multiple of \(x^\nu P_n^{(-\nu,\nu)}(2x/L-1)\). The comparison
\(x^{2\nu}\le(L/2)^{2\nu}x^\nu(L-x)^{-\nu}\) allows Jacobi orthogonality to control every linear combination in the tail; the resulting gamma ratio decreases with \(n\). This is a tail-operator estimate, not just an estimate on individual basis functions. The standard polynomial and norm formulas are in [DLMF 18.5.7](https://dlmf.nist.gov/18.5#E7) and [DLMF 18.3](https://dlmf.nist.gov/18.3).

Differentiating the squared norm inequality at \(\nu=0\) on a finite polynomial tail, where both sides agree at zero, proves the central tail floor

\[
H_N-\gamma-\log(\pi L)
\]

for the negative symmetric derivative of \((2\pi)^\nu I_\nu\). The limit \(\nu\uparrow1\) in (3.1) also gives
\(\|I_1(I-P_N)\|\le L/(2\sqrt{N(N+1)})\). Smooth approximation and form closure extend the central bound. In particular, the logarithmic endpoint terms of the zero-extended polynomial inputs are square integrable; no finite-output truncation is involved.

### 3.2 Smooth correction and arithmetic delays

Factor
\(S_w=(w(0)I+S_{w'})I_1\). Therefore, with

\[
K_L\ge |w(0)|+\int_0^L|w'(t)|\,dt,
\]

the smooth correction costs at most \(K_LL/(2\sqrt{N(N+1)})\). A convenient computable bound is \(K_L\le\sum_{j\ge1}|g_j|L^{j-1}\).

For a delay, the direct integral decomposition into finite chains gives
\(\|T_d+T_d^*\|=1\) when \(d<L\le2d\), and \(\sqrt2\) when \(2d<L\le3d\). A universal bound is 2. The threshold comparisons in the code use exact integer comparisons for logarithmic horizons.

Combining these estimates yields the complete tail bound

\[
\boxed{
a_{N,L}=H_N-\gamma-\log(\pi L)
-\frac{K_LL}{2\sqrt{N(N+1)}}
-\sum_{\log n<L}\frac{\Lambda(n)}{\sqrt n}\|T_{\log n}+T_{\log n}^*\|.}
\tag{3.2}
\]

This scalar arithmetic bound is deliberately conservative. Its deterioration at the mixed-prime test is measured below.

### 3.3 Profile remainder

On \(|z|=3\), the Euler product for \(\sinh\) gives \(|z/\sinh z|\le3/\sin3\). Exact rational Taylor bounds establish \(\sin3>1/8\) and \(e^{3/2}<5\). Hence
\(|G_0(z)|<5(24+12)<256\). The product identity is [DLMF 4.36.1](https://dlmf.nist.gov/4.36#E1).

With a degree-\(M\) profile and \(L<3\), this gives

\[
\eta_M=\frac{256(L/3)^{M+1}}{(M+1)(1-L/3)}
\tag{3.3}
\]

as an operator-norm bound for the omitted central derivative convolution. The omitted contribution to \(K_L\) is at most
\(\frac{256}{3}(L/3)^M/(1-L/3)\). This larger Cauchy radius makes the deeper-horizon computation practical.

## 4. Full-output Gram reduction and certification

Let \(R\) denote midpoint reflection, \(H_\omega=V_\omega R\), and \(H_1=\partial_\omega H_\omega|_0\). The derivative \(H_1\) is selfadjoint and

\[
Q_0=-\tfrac12(H_1R+RH_1).
\]

The finite matrices are

\[
A_1=P_NH_1P_N,\qquad G=P_NH_1^2P_N,\qquad E=G-A_1^2.
\]

Crucially, \(G\) integrates the complete output of \(H_1P_N\). It is not a squared finite compression. Thus \(E=P_NH_1(I-P_N)H_1P_N\) retains the omitted output exactly, up to the explicit profile and arithmetic enclosures.

Reflection parity diagonalizes \(Q_0\). For parity \(r=\pm1\), the central leakage squared is bounded above by the corresponding block \(E_r\). If (3.2) gives \(a>m\), the following two finite tests are sufficient for the whole central form to satisfy \(Q_0\ge mI\):

\[
(a-m)(Q_{P,r}-mI)-E_r\succeq0,
\qquad r=+1,-1.
\tag{4.1}
\]

This follows by the form Schur complement with the tail resolvent bounded by \((a-m)^{-1}I\).

### Exact parity coupling

For the mixed-prime experiment, an additional reflected full-output Gram matrix
\(C=P_NH_1RH_1P_N\) gives

\[
G_{Q,r}=\tfrac12(G_r+rC_r),\qquad
E_{Q,r}=G_{Q,r}-Q_{P,r}^{\,2}.
\tag{4.2}
\]

Replacing \(E_r\) by \(E_{Q,r}\) in (4.1) keeps exactly the central parity coupling. This is a useful general refinement: irrelevant opposite-parity output no longer consumes the available tail margin.

The code integrates polynomial, logarithmic, and delayed-polynomial terms analytically. In the coordinate \(u=x/L\), the gamma derivative of a monomial is

\[
U_1^\gamma u^k=u^k(\log u+\ell-H_k)
+\sum_{j=1}^M g_jL^j\frac{(j-1)!k!}{(j+k)!}u^{j+k},
\quad \ell=\gamma+\log(2\pi L).
\]

Each prime-power contribution is
\(2\Lambda(n)n^{-1/2}\mathbf1_{u>\delta_n}p(u-\delta_n)\), with \(\delta_n=\log n/L\). Full and reflected Grams reduce to moments of \(1,\log u,(\log u)^2,\log(1-u),\log u\log(1-u)\), and their truncated-interval counterparts. In the reflected Gram, mixed-delay overlaps are included precisely when \(\log(n_i n_j)<L\), including the \(2\times3\) overlaps in the \(L=1.8\) experiment.

### Numerical results

| Horizon / reduction | \(N\) | \(M\) | Tail floor, rounded | Target \(m\) | Complete test |
|---|---:|---:|---:|---:|---|
| \(\log4\), full-derivative coupling bound | 80 | 110 | 1.7523340933 | \(5\times10^{-13}\) | PASS, both parities |
| \(\log5\), full-derivative coupling bound | 80 | 130 | 1.0429322478 | \(10^{-18}\) | PASS, both parities |
| 1.8, full-derivative coupling bound | 80 | 180 | 0.2006814159 | \(10^{-26}\) | NOT CERTIFIED |
| 1.8, exact central parity coupling | 80 | 180 | 0.2006814159 | \(10^{-26}\) | NOT CERTIFIED |
| 1.8, exact central parity coupling | 96 | 180 | 0.3921290266 | \(10^{-26}\) | NOT CERTIFIED |

The minimum interval LDL pivots for the successful \(\log4\) matrices are about 0.00439208 and 0.01018169. Pivots are not eigenvalue bounds. Ordinary floating-point eigenvalues are never used to decide the sign of (4.1).

### Error accounting

The profile-model norm error in (4.1) is bounded by

\[
(|a-m|+40000)\eta_M+2\eta_M^2+10^{-45}.
\tag{4.3}
\]

The first two terms follow from \(\|H_1P_N-\widetilde H_1P_N\|\le\eta_M\), the corresponding compression bound, and \(\|\widetilde H_1P_N\|<10000\). The latter is bounded by the full Gram trace, which is checked to be below \(10^7\), with ample allowance for arithmetic error. The same estimate covers (4.2). For the successful rows, (4.3) is approximately \(1.0467\times10^{-32}\) and \(6.2866\times10^{-31}\).

The \(10^{-45}\) allowance covers coefficient/moment construction and propagation through finite matrix products. This is an a priori rounding/sensitivity budget, rather than interval evaluation of every intermediate coefficient:

* Rational arithmetic constructs every \(g_j\), Legendre coefficient, and beta factor exactly before Decimal conversion. A 300-term Machin expansion encloses \(\pi\); \(H_{10000}\), 50 Euler–Maclaurin correction terms, and the next Bernoulli remainder enclose \(\gamma\). Both widths are below \(10^{-300}\). Decimal logarithms and square roots are evaluated at 400 digits, and their interval versions are expanded outward.
* The covered calculations satisfy \(1<L<2\), \(N\le96\), \(M\le220\), at most five prime-power terms, and \(1/3<\delta_n<0.9\). These are checked explicitly. They are part of the budget's scope; increasing \(N\) requires revisiting the budget.
* Absolute coefficient sums of a shifted degree-\(n\) Legendre polynomial are below \(6^{n+1}\); weighting its coefficients by \(2^k\) gives a bound \(10^{n+1}\). Uniform bounds sufficient here are \(\|p\|_1\le6^N\), \(\|q\|_1\le600\,6^N\), \(\|q(1-u)\|_1\le[10+256M(4/3)^M]10^N\), \(\|v\|_1\le4\,10^N\), and \(\|v(1-u)\|_1\le2^N4\,10^N\).
* The closed moment formulas have intermediate absolute sums below 20 on these ranges. With normalization and all Gram cross terms included, a bound for raw absolute sums is
  \(50\cdot20\cdot(2N+1)\max\{qq_R,pq_R,vq_R,vv_R,q^2,v^2\}<10^{233}\), using the preceding coefficient-sum bounds. Power indices are below 632; denominators in endpoint derivatives are bounded by the displayed range of \(\delta\). A factor \(10^6\) bounds the combined first-derivative amplification per source constant, and fewer than 64 constants are needed. The resulting aggregate sensitivity is below \(10^{243}\).
* Fewer than \(10^{12}\) scalar arithmetic operations, relative rounding at most \(10^{-399}\), and amplification below \(10^9\) from entry errors to the final matrix norm give a propagated bound below \(8.54\times10^{-54}\). The implementation uses the larger allowance \(10^{-45}\). `audit_arithmetic_budget.py` verifies the rational magnitude inequalities and all stored-data range conditions.

Finally, (4.3) is subtracted as a scalar matrix shift, and LDL elimination uses directed interval arithmetic. Exact decimal negation is implemented with `copy_negate`; rational conversion uses interval division. This specifically avoids the enclosure mistakes identified in the supplied first-slab audit. An independent reviewer should still check the analytic identities, the operation/sensitivity accounting, and the code; successful execution alone does not replace that review.

## 5. What the relative-coupling test says

For diagnostic purposes, form the central-head-relative matrix

\[
Q_{P,r}^{-1/2}E_rQ_{P,r}^{-1/2}/a
\]

(using \(E_{Q,r}\) where available). A Decimal LDL congruence is used before conversion to ordinary floating-point eigenvalues. These spectral values are diagnostics, not additional certificates.

| Case | Largest relative coupling, even | Largest relative coupling, odd |
|---|---:|---:|
| \(\log4\), 80 modes, majorant | 0.3202 | 0.4607 |
| \(\log5\), 80 modes, majorant | 0.6026 | 0.8616 |
| 1.8, 96 modes, exact parity coupling | 1.4242 | 1.3966 |

At 1.8, the corresponding required scalar tail floors are approximately 0.55845 and 0.54762; the available bound is 0.39213. Thus this particular Schur reduction loses the comparison by a moderate factor even though the central head is positive. This is much more specific than a generic numerical failure.

The scalar formula (3.2), evaluated prospectively at \(N=128\), gives approximately 0.69125. That makes a 128-mode calculation with a revised precision/error budget a sensible next experiment. It is not a certificate: changing the head also changes the relative coupling, and the new matrices have not been built. A stronger alternative is to retain arithmetic cancellation or more structure in the tail resolvent instead of paying all delay norms absolutely.

An independent continuous-output quadrature check of (4.2), on modes 0, 1, 4, and 5 at \(L=1.8\), agrees with the analytic reflected Gram norms to within the quadrature error estimates; the largest absolute discrepancy is about \(1.3\times10^{-11}\). This checks normalization and reflected-delay overlap handling. The quadrature is a diagnostic only and is not an input to any positivity decision.

## 6. Cumulative storage consequences

For any spatial split, write

\[
V=\begin{pmatrix}X&0\\Y&Z\end{pmatrix}.
\]

If the complete transfer bound gives \(\|V\|\le\rho<1\), then \(X\) and \(Z\) are strict contractions. The Schur complement of \(I-V^*V\) is

\[
\mathcal S=I-X^*X-Y^*(I-ZZ^*)^{-1}Y.
\]

Since \(I-V^*V\ge(1-\rho^2)I\), minimizing its quadratic form over the second block yields

\[
\boxed{\mathcal S\ge(1-\rho^2)I.}
\tag{6.1}
\]

For the normalized coupling

\[
\mathcal C=(I-ZZ^*)^{-1/2}Y(I-X^*X)^{-1/2},
\]

one also obtains \(\|\mathcal C\|\le\rho\). Indeed,
\(I-\mathcal C^*\mathcal C=(I-X^*X)^{-1/2}\mathcal S(I-X^*X)^{-1/2}\ge(1-\rho^2)I\), because \(I-X^*X\le I\).

Apply this first to the split \(\log4=\log3+\log(4/3)\), and then to \(\log5=\log4+\log(5/4)\). On the certified shift ranges,

\[
\mathcal S_{\log4}\ge(1-e^{-5\times10^{-13}\omega})I,
\qquad
\mathcal S_{\log5}\ge(1-e^{-10^{-18}\omega})I.
\]

These are new finite-depth storage bounds obtained from complete central certificates. They do **not** prove a storage induction from the previous slab alone: each larger-horizon central form was independently certified. Finding an update rule that preserves a sufficiently informative storage factor remains the generalization problem.

## 7. Weak directions and perturbed Euler factors

Candidate weak directions were found by high-precision inverse iteration in 40 total Legendre modes. Their coefficients were rounded to exact 70-place decimals. Their scalar forms were then checked independently through physical-space autocorrelations, without reading the head matrix for the form evaluation.

For \(F(u)=\int_0^{1-u}f(v+u)\overline{f(v)}\,dv\), the gamma form is evaluated as

\[
Q^\gamma_{\omega,L}[f]
=-[\gamma+\log(2\pi L)]F(0)
+\int_0^1\frac{-\cosh(\omega Lu)G_0(Lu)F(u)+F(0)}{u}\,du,
\]

with arithmetic terms
\(-2\sum\Lambda(n)n^{-1/2}\cosh(\omega\log n)\operatorname{Re}F(\log n/L)\).
The real polynomial witnesses used here make \(F\) real. A degree-220 profile, a Cauchy remainder bounded using \(|\cosh(\omega z)G_0(z)|<1280\) on \(|z|=3\), and a \(10^{-45}\) arithmetic allowance enclose each scalar result. The autocorrelation bound \(|F(u)|\le F(0)\) controls the profile remainder directly.

| Horizon | Parity | Central Rayleigh quotient, rounded | Same direction at \(\omega=0.05\) |
|---|---|---:|---:|
| \(\log4\) | even | \(8.0054\times10^{-13}\) | \(-2.3303\times10^{-7}\) |
| \(\log4\) | odd | \(5.0327\times10^{-10}\) | \(-3.8143\times10^{-6}\) |
| \(\log5\) | even | \(1.2653\times10^{-17}\) | \(-1.4846\times10^{-7}\) |
| \(\log5\) | odd | \(1.1126\times10^{-14}\) | \(-2.5221\times10^{-6}\) |

The central scalar intervals agree with the independently constructed matrix Rayleigh values within their profile enclosures. The negative-generator intervals at 0.05, and additional negative checks at 0.25, show that extending positivity by requiring the instantaneous generator to remain positive will fail. They do not establish contraction or expansion of the cumulative transfer at those larger shifts.

To test what the Euler algebra alone can guarantee, change the exponent of one local factor from 1 to \(1+\varepsilon\). In the finite nilpotent algebra this deformation remains well defined and preserves the causal factorization and its logarithmic-derivative structure. It scales all generator terms associated with powers of that prime together.

At \(\log4\), increasing the exponent of the \(p=2\) factor by \(10^{-9}\) makes the even central witness less than \(-3.0220\times10^{-11}\). At \(\log5\), increasing that exponent by only \(10^{-14}\) makes the even witness less than \(-3.8341\times10^{-16}\). Decreasing the exponent also produces negative odd witnesses, with changes \(-10^{-7}\) and \(-10^{-12}\), respectively.

Thus a positivity theorem based only on the finite delay algebra or formal Euler factorization is impossible. A successful general theorem must use a quantitative property of the actual prime-gamma coefficients. The central margins are small enough that this arithmetic sensitivity is already visible at these modest horizons.

## 8. The second-slab remainder gap

The supplied endpoint certificate uses a normalized Schur quadratic remainder constant 954147 and a certified matrix shift \(3\times10^{-8}\). Holding that same head margin fixed, the simple budget \(C h^2<3\times10^{-8}\) would require approximately:

| Proposed endpoint \(h\) | Maximum admissible \(C\) in that same scalar budget |
|---:|---:|
| \(4\times10^{-5}\) | 18.75 |
| \(10^{-3}\) | 0.03 |
| 0.05 | \(1.2\times10^{-5}\) |

This is a diagnostic of the inherited scalar budget, not a lower bound on the true remainder or an impossibility theorem for continuation. It shows why modest tightening of its absolute norm constants is unlikely to bridge the gap. The earlier central-energy argument already reaches \(4\times10^{-5}\) by a different route.

The next useful gap calculation should retain the remainder in the storage metric, or recenter a rigorously enclosed transfer/Gram calculation at positive shifts. The exact parity-coupling construction in Section 4 is a concrete successful reduction of unnecessary leakage, but it does not by itself replace the positive-shift remainder analysis. No new connected interval to 0.05 is claimed here.

## 9. Reproducibility and next priorities

The accompanying archive contains all new Python sources, 400-digit matrices, certificates, unsuccessful test outputs, direct scalar witnesses, diagnostic checks, and logs. `README.md` gives exact commands; `SHA256SUMS` identifies the package contents, and `SOURCE_HASHES.json` identifies the supplied sources. NumPy is needed for the matrix builder; SciPy is used only by the optional physical-output quadrature diagnostic. No external central-window matrices are used.

The successful tests are reproducible either by rebuilding the matrices or by rerunning interval validation from their saved decimal entries. A validation rerun alone checks the final finite inequalities; rebuilding is needed to reproduce the coefficient construction. The complete analytic tail and error budget in this report are essential to interpreting either run.

The immediate sequence supported by these results is:

1. Independently review the new central-tail lemma, arithmetic budget, and the two successful full-output Gram certificates.
2. At \(L=1.8\), test 128 modes with a revised precision/error budget, or improve the arithmetic tail bound. The measured comparison is approximately 0.55845 required versus 0.39213 available at 96 modes.
3. Preserve exact parity coupling and the head-relative metric in subsequent storage and remainder calculations. Track weak vectors and their prime correlations alongside scalar floors.
4. Revisit the second-slab gap with a positive-shift or storage-relative remainder model; keep it separate from the deeper central-coercivity sequence.

The broader route remains a sequence of increasing horizons with possibly shrinking positive shifts. A common shift interval is unnecessary for the diagonal compact-window implication discussed in the strategy note. The unresolved task is to control the actual prime-gamma balance at unbounded depth; neither these finite successes nor the algebraic identities provide that control.

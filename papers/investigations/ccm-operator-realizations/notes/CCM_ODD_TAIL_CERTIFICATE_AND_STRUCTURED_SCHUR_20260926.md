# A certified odd Fourier tail and a structured Schur-complement reduction

Date: 26 September 2026. Continuation round 4.

Model: GPT-6 (Codex). Exact model variant and reasoning-effort setting are not exposed in this session.

Status: LLM-assisted research drafted for Edward Baker. The explicit analytic inequalities and rational enclosures below certify the stated infinite-tail bound and the failure of one scalar Schur test. The separate eigenvalue computations are multiprecision diagnostics, not interval eigenvalue certificates. The full limiting odd-sector gap is **not** certified. The [accompanying review](../reviews/ODD_TAIL_AND_SCHUR_REVIEW_20260926.md) is a same-agent check, not independent peer review. No novelty claim is made for Schur complements, Fourier concentration estimates, or separable expansions of a Cauchy kernel.

Predecessor: [energy-defined ports and the fixed-support limit](CCM_ENERGY_PORTS_AND_FIXED_SUPPORT_LIMIT_20260926.md). Earlier derivations, programs, and records are preserved.

## 1. Outcome

At \(L=\log13\), let \(P_M\) project onto the first \(M\) odd Fourier modes and \(Q_M=I-P_M\). This continuation proves, with a standard-library rational certificate,
\[
\boxed{Q_{4096}W_-Q_{4096}\ \ge\ \frac25 Q_{4096}.}
\tag{1}
\]
This is a bound for the **unshifted odd Weil form on the high Fourier subspace**, not a bound for its whole spectrum. It applies to the full infinite tail, without replacing it by a numerical truncation.

The next step cannot simply replace the coupling to that tail by its norm. We certify
\[
(W_-)_{11}<10^{-3},\qquad
(W_-)_{4096,4097}<-1/20.
\tag{2}
\]
Consequently the scalar norm Schur lower bound using (1) has a negative first diagonal entry, even at spectral threshold zero. It also fails at every threshold \(0\le s<2/5\). This is a failure of that sufficient bound, not a negative direction for the actual Weil form.

To retain the coupling's structure, a finite-rank far-tail expansion is derived with an explicit operator-norm error. For the first 4096 modes coupled to modes above 8192, rank at most 256 gives error below \(7\times10^{-77}\). Modes 4097--8192 remain a finite intermediate block and cannot be omitted. A smaller retained space of 64 modes coupled to modes above 4096 admits rank at most 40 with error below \(2.3\times10^{-72}\); modes 65--4096 must likewise be retained or controlled separately.

These results make the remaining matrix certificate concrete. They do not verify it. New diagnostics through \(N=64\) show how much directional cancellation a scalar norm loses: the coupling to the next \(N\) modes has Frobenius norm about 1.15, while its squared norm on the lowest odd Ritz vector is about \(8.0\times10^{-55}\).

## 2. Normalization and the threshold to certify

Use the real odd basis on \([0,L]\),
\[
\phi_n(x)=\sqrt{2/L}\sin(d_nx),\qquad d_n=2\pi n/L,\quad n\ge1.
\]
It differs by a common phase from the preceding notes' odd basis and has the same Gram matrix. Reflection is \(x\mapsto L-x\). In centered coordinates \(t=x-L/2\), the pole part on odd functions is
\[
-2|\langle f,\sinh(t/2)\rangle|^2.
\tag{3}
\]
The signed archimedean part is the full-line multiplier
\[
a(\xi)=\operatorname{Re}\psi(1/4+i\xi/2)-\log\pi,
\tag{4}
\]
on zero extensions. Each prime power \(q=p^j\le13\) contributes
\(-w_q(U_{\log q}+U_{\log q}^*)\), with \(w_q=(\log p)/\sqrt q\), where \(U_a\) is translation followed by restriction to the interval. The endpoint \(q=13\) gives the zero operator. These normalizations follow from [CCM, (3.8)--(3.19), (4.2)--(4.4)](https://arxiv.org/html/2511.22755v1#S3).

The desired gap is
\(\inf\sigma(W_-)-\varepsilon_\infty\), where \(\varepsilon_\infty=\inf\sigma(W_L)\). A useful certification route avoids needing a lower enclosure of \(\varepsilon_\infty\): take an even trial function whose normalized energy has a certified upper bound \(U\). Then \(\varepsilon_\infty\le U\). A proof that \(W_--U\ge\gamma I\), with \(\gamma>0\), proves the desired odd gap is at least \(\gamma\). It would imply that the full bottom eigenspace is even, but would not prove simplicity within the even sector.

A floating-point even Ritz value is not such a certified U. No tiny even-energy upper enclosure or full Schur positivity certificate is claimed here. For a chosen threshold s, (1) only yields a high-block lower bound \(2/5-s\), so the shift remains explicit throughout.

## 3. Continuous-frequency leakage of high sine modes

High discrete sine frequency does not imply that the zero-extended function's continuous Fourier transform is supported at high frequency. Direct integration gives
\[
|\widehat\phi_n(\xi)|^2
=\frac8L\frac{d_n^2\sin^2(L\xi/2)}{(d_n^2-\xi^2)^2}.
\tag{5}
\]
The removable values at \(\xi=\pm d_n\) cause no issue. If \(0<T<d_{M+1}\), put \(r=T/d_{M+1}\). The Hilbert--Schmidt norm of continuous band projection onto \([-T,T]\), restricted to the odd high subspace, gives
\[
\int_{-T}^{T}|\widehat f(\xi)|^2\frac{d\xi}{2\pi}
\le\eta(M,T)\|f\|_2^2,\qquad f\in Q_ML^2_{\rm odd},
\]
\[
\boxed{\eta(M,T)=\frac{LT+1}{\pi^3M(1-r^2)^2}.}
\tag{6}
\]
Indeed, sum (5) over \(n>M\), use
\((d_n^2-\xi^2)^{-2}\le d_n^{-4}(1-r^2)^{-2}\) and
\(\sum_{n>M}d_n^{-2}\le L^2/(4\pi^2M)\), and integrate
\(\sin^2(L\xi/2)\) exactly. Before the final simplification, the numerator is \(LT-\sin(LT)\); its upper bound \(LT+1\) avoids a trigonometric evaluation in the tail certificate. Hilbert--Schmidt norm bounds operator norm, so this estimate applies to arbitrary linear combinations, not just individual modes.

The digamma series shows that \(a(\xi)\) is increasing with \(|\xi|\): every term
\(- (k+1/4)/((k+1/4)^2+\xi^2/4)\) is increasing in \(|\xi|\). Therefore, if \(a(0)\ge a_*\) and \(a(T)\ge A\ge a_*\), then
\[
\langle f,a(D)f\rangle
\ge [A-(A-a_*)\eta(M,T)]\|f\|_2^2
\tag{7}
\]
when \(\eta\le1\). This step is where the finite-interval leakage is accounted for.

## 4. Sharper bounds for primes and the odd pole

### Prime translations

For a delay \(h>0\), decompose the interval into fibers modulo h. On each fiber, \(U_h+U_h^*\) is the adjacency matrix of a finite path. The longest path has \(m=\lceil L/h\rceil\) vertices, up to null endpoint fibers, and the path's norm is \(2\cos(\pi/(m+1))\). The latter follows by substituting the discrete sine eigenvectors. Thus
\[
\|U_h+U_h^*\|\le2\cos\frac{\pi}{m+1}.
\tag{8}
\]
This whole-space estimate remains valid on the odd subspace. No assertion is made that restricting to odd functions preserves the Markov property.

For \(q=2,3,4,5,7,8,9,11\), the longest path lengths are respectively \(4,3,2,2,2,2,2,2\). The \(q=13\) path has one vertex and contributes zero. The resulting prime norm bound is
\[
S=\sum_{q<13}w_q\,2\cos\frac{\pi}{\lceil L/\log q\rceil+1}
<\frac{483}{100}=4.83.
\tag{9}
\]
Only the values \((1+\sqrt5)/2\), \(\sqrt2\), and 1 occur as nonzero path norms. The certificate checks the prime powers' path lengths by integer powers, then encloses their logarithms and square roots rationally. This is sharper than bounding every translation pair by 2.

### Odd pole term

From the centered Fourier coefficients of \(\sinh(t/2)\),
\[
|\langle\phi_n,\sinh(t/2)\rangle|^2
=\frac8L\sinh^2(L/4)\frac{d_n^2}{(d_n^2+1/4)^2}.
\]
Its rank-one contribution (3) on the high subspace has norm at most
\[
\boxed{p_M=\frac{4L\sinh^2(L/4)}{\pi^2M}
=\frac{L(\sqrt{13}+1/\sqrt{13}-2)}{\pi^2M}.}
\tag{10}
\]
This \(O(M^{-1})\) bound is much better than the full odd pole norm, and the pole's negative sign has not been lost.

## 5. A rational certificate for the infinite tail

Choose \(M=4096\), \(T=2700\). The following strict bounds suffice:
\[
a(0)>-6,\qquad a(2700)>6,\qquad
\eta(4096,2700)<8/125,\qquad S<483/100,\qquad p_{4096}<1/5000.
\tag{11}
\]
Combining (7), (9), and (10) gives
\[
QW(f,f)>
\left(6-12\frac8{125}-\frac{483}{100}-\frac1{5000}\right)\|f\|^2
=\frac{2009}{5000}\|f\|^2>\frac25\|f\|^2.
\tag{12}
\]
All terms are for the unshifted Weil form. The proof is first valid on finite sine sums and extends to the restricted closed form by its core and lower-semicontinuity; it also follows directly for any high-subspace vector in the form domain from the multiplier estimate and bounded remaining terms.

Here is how the special-function inequalities are made effective. The exact value
\(\psi(1/4)=-\gamma-\pi/2-3\log2\), together with \(\gamma<1\), \(\pi<22/7\), \(\log2<7/10\), and \(\log\pi<23/20\), proves \(a(0)>-6\). The bound \(\gamma<1\) follows from the decreasing harmonic-number definition of Euler's constant.

Rearrange the digamma integral in [DLMF 5.9.13](https://dlmf.nist.gov/5.9.E13) as
\[
\psi(z)=\log z-\frac1{2z}-\int_0^\infty e^{-zt}
\left(\frac12\coth(t/2)-\frac1t\right)dt,\qquad \Re z>0.
\]
The kernel lies between 0 and \(t/12\). For example,
\(0\le x\cosh x-\sinh x\le(x^2/3)\sinh x\) follows term by term from the power series, and gives this bound with \(x=t/2\). Consequently
\[
\left|\psi(z)-\log z+\frac1{2z}\right|
\le\frac1{12(\Re z)^2}.
\tag{13}
\]
Apply four recurrence steps to \(z=1/4+1350i\). Dropping favorable terms gives
\[
a(2700)\ge
\log\frac{1350}{\pi}-\frac{73/8}{1350^2}-\frac1{12(17/4)^2}>6.
\tag{14}
\]
The last strict inequality, the leakage and pole bounds, and (9) are checked using exact fractions and outward rounding. The elementary enclosure routines use Machin's arctangent formula for \(\pi\), a positive atanh series for logarithms, and integer square roots. No floating-point input is accepted by the certificate's interval arithmetic. Running with Python optimization that disables assertions is rejected.

The [certificate program](../numerics/certify_odd_tail.py) and [small rational record](../numerics/records/odd_tail_certificate_20260926.json) retain exact enclosure endpoints, source hash, parameters, and claim scope. Typical displayed values, rounded here only for readability, are

| Quantity | Value / enclosure |
|---|---:|
| Prime norm bound S | 4.82614094420 |
| Leakage bound eta | 0.06337990310 |
| Pole-tail bound | 0.00011946665 |
| Lower expression for a(2700) in (14) | 6.05851136857 |
| Tail lower expression using A=6 and the sharper enclosed constants | 0.41318075199 |

The simple published lower bound 2/5 leaves a clear rational margin and does not depend on printed decimal rounding.

## 6. The correct Schur gate, and a certified failure of its scalar version

Split the odd Hilbert space at \(M=4096\):
\[
W_- -sI=\begin{pmatrix}A-sI&E^*\\ E&C-sI\end{pmatrix},\qquad
C\ge hI,\quad h=2/5.
\]
The finite sine space lies in the operator domain: its zero-extended Fourier transforms decay quadratically, which remains square integrable after multiplication by the logarithmic symbol. Thus the finitely many columns of E are in \(\ell^2\), and E is a bounded map from the finite low space to the high space. The high compression is the self-adjoint operator associated with the restricted form.

For \(s<h\), completing the square gives the exact finite Schur form
\[
S_s=A-sI-E^*(C-sI)^{-1}E.
\tag{15}
\]
An explicit sufficient test is
\[
\boxed{A-sI-\frac1{h-s}E^*E\ \ge\ \sigma I,\qquad \sigma>0.}
\tag{16}
\]
This keeps the full directional Gram matrix of the coupling. If \(\|E\|\le\beta\), the completed-square triangular map further yields
\[
W_- -sI\ge
\frac{\min(\sigma,h-s)}{(1+\beta/(h-s))^2}I.
\tag{17}
\]
Indeed the inverse of that map has norm at most \(1+\|(C-sI)^{-1}E\|\le1+\beta/(h-s)\). Combined with a certified even trial upper bound U and the choice s=U, this would prove a positive odd-sector gap without assuming it.

The simpler replacement \(E^*E\le\beta^2I\) gives
\(A-sI-\beta^2/(h-s)I\). Every valid \(\beta\ge\|E\|\) is greater than 1/20, by the boundary entry in (2). Its first diagonal entry is therefore, for \(0\le s<h\), less than
\[
\frac1{1000}-s-\frac{(1/20)^2}{2/5-s}
\le\frac1{1000}-\frac1{160}
=-\frac{21}{4000}<0.
\tag{18}
\]
Thus this scalar-norm sufficient test cannot pass with the certified tail bound (1). This conclusion is exact. It neither rules out (16) nor asserts anything negative about the actual operator. A sharper high-block bound or a different decomposition is outside this specific obstruction.

### Certifying the two witness entries

Write the CCM full Fourier matrix as
\(W_{mn}=(b_m-b_n)/(m-n)\) off the diagonal, with \(b_{-n}=-b_n\). Its odd off-diagonal block has
\[
(W_-)_{mn}=\frac{2(nb_m-mb_n)}{m^2-n^2},\qquad m\ne n.
\tag{19}
\]
Let \(a_k=2k+1/2\), \(d=d_n\), and \(z=1/4+id/2\). Expanding
\(\rho(x)=e^{x/2}/(e^x-e^{-x})=\sum_{k\ge0}e^{-a_kx}\) gives
\[
b_n=\frac1\pi\left[
\frac12\Im\psi(z)-\sum_{k\ge0}\frac{d\,13^{-2k-1/2}}{a_k^2+d^2}
+\sum_{q<13}w_q\sin(d\log q)
+\frac{2d(\cosh(L/2)-1)}{d^2+1/4}\right].
\tag{20}
\]
This follows by integrating the sine correlation: each exponential integral is \(d(1-e^{-a_kL})/(a_k^2+d^2)\). The digamma series sums its non-exponential part. Formula (20) computes distant coefficients without a large matrix or oscillatory quadrature.

For the first odd diagonal, or any n, an independent correlation calculation gives
\[
(W_-^{\rm arch})_{nn}
=a(d)-\frac{4d^2}{L}\sum_{k\ge0}\frac{1-13^{-2k-1/2}}{(a_k^2+d^2)^2}.
\tag{21}
\]
The sine autocorrelation used here is
\(2(1-x/L)\cos(dx)+2\sin(dx)/(Ld)\) on \([0,L]\). Insert it into the defining archimedean distribution. Integration of each exponential makes the endpoint terms cancel and leaves (21). The pole diagonal is
\(-16\sinh^2(L/4)d^2/[L(d^2+1/4)^2]\); the prime diagonal subtracts the weighted autocorrelation at \(x=\log q\).

The certificate evaluates (20) for n=4096,4097 and (21) for n=1. It uses 64 digamma recurrence steps with (13), rational Taylor enclosures for sines and cosines, geometric bounds for the exponential series, and a \(k^{-4}\) integral bound for the tail of (21). It obtains enclosures contained in
\[
-0.057642<(W_-)_{4096,4097}<-0.057628,
\qquad
0.00079149<(W_-)_{11}<0.00083265.
\]
These deliberately loose intervals suffice for (2). Their exact rational endpoints, rather than these outward-rounded decimal summaries, are saved in the certificate.

## 7. Retaining the far coupling by a finite-rank expansion

First a uniform coefficient bound is available. The positive sine archimedean integral satisfies
\[
\sum_{k\ge0}\frac{d(1-e^{-a_kL})}{a_k^2+d^2}
\le\frac1d+\frac\pi4.
\]
Use the k=0 summand plus the integral of the decreasing summand as a function of k. Bounding the sine prime terms and the pole term in (20) gives
\[
|b_n|\le\frac14+
\frac{2\cosh(L/2)-1}{\pi d_1}
+\frac1\pi\sum_{q<13}w_q
<2\qquad(n\ge1).
\tag{22}
\]
The same rational certificate verifies the last inequality; its enclosed upper expression is approximately 1.980768.

Let \(1\le m\le r<K<n\). Expanding the denominator in (19), the coupling from the first r modes to modes above K is
\[
E_{nm}=
-2\sum_{j\ge0}\frac{b_m m^{2j}}{n^{2j+1}}
+2\sum_{j\ge0}\frac{b_n m^{2j+1}}{n^{2j+2}}.
\tag{23}
\]
Truncation to \(0\le j<q\) defines an operator \(F_q\) of rank at most \(2q\), and the exact entrywise remainder is
\[
(E-F_q)_{nm}=E_{nm}(m/n)^{2q}.
\tag{24}
\]
Put \(\rho=r/(K+1)\). Minkowski's inequality for the Hilbert--Schmidt norm, (22), and the integral bounds for power tails yield
\[
\|E-F_q\|\le\|E-F_q\|_{HS}
\le\frac4{1-\rho^2}\left[
\sqrt{\frac{\sum_{m\le r}m^{4q}}{(4q+1)K^{4q+1}}}
+\sqrt{\frac{\sum_{m\le r}m^{4q+2}}{(4q+3)K^{4q+3}}}\right].
\tag{25}
\]
For the saved rational bounds it is convenient to weaken this to
\[
\boxed{\|E-F_q\|\le\epsilon_q(r,K):=
\frac4{1-(r/(K+1))^2}\left(\frac rK\right)^{2q}
\left(1+\frac rK\right).}
\tag{26}
\]
Here \(\sum_{m\le r}m^p\le r^{p+1}\), and the favorable square-root and denominator factors are bounded by one. This controls the *whole infinite* far tail. It is not an empirical decay fit.

| Retained modes r | Far tail n>K | q | Rank bound | Certified error upper bound, rounded upward |
|---:|---:|---:|---:|---:|
| 64 | 4096 | 8 | 16 | \(5.13\times10^{-29}\) |
| 64 | 4096 | 16 | 32 | \(6.48\times10^{-58}\) |
| 64 | 4096 | 20 | 40 | \(2.30\times10^{-72}\) |
| 4096 | 8192 | 96 | 192 | \(1.28\times10^{-57}\) |
| 4096 | 8192 | 128 | 256 | \(6.91\times10^{-77}\) |

For the split in (1), the last row is directly applicable after retaining modes 4097--8192 explicitly. The smaller-r rows only handle coupling from those r modes to the specified far tail. They do **not** make the intervening modes disappear or certify their positivity.

To use the full Gram test (16), split E into intermediate rows \(E_{\rm mid}\) and far rows. If the latter are approximated by \(F_q\) with error \(\epsilon\), then
\[
E^*E\preceq E_{\rm mid}^*E_{\rm mid}+F_q^*F_q
+(2\|F_q\|\epsilon+\epsilon^2)I.
\tag{27}
\]
Thus a verified evaluation of these finite matrices and finite-rank Gram coefficients gives a concrete sufficient inequality, retaining their directions. The entries of \(F_q^*F_q\) are convergent scalar series and still require verified summation; they are not evaluated as a full Schur certificate in this round. Also (16) can remain too conservative even when its coupling is treated exactly, because \((C-sI)^{-1}\le(h-s)^{-1}I\) is itself an inequality. A stronger energy-weighted estimate would then be needed.

## 8. Multiprecision checks and the size of the cancellation

The [new diagnostic program](../numerics/check_odd_blocks.py) uses closed digamma/trigamma formulas to build both parity blocks. For the odd diagonal it sums the non-exponential series in (21) by
\[
\sum_{k\ge0}\frac1{(a_k^2+d^2)^2}
=\frac{\Im\psi(1/4+id/2)}{4d^3}
-\frac{\Re\psi'(1/4+id/2)}{8d^2}.
\]
This follows by differentiating \(\sum d/(a_k^2+d^2)=\tfrac12\Im\psi(1/4+id/2)\). The even block follows from the same b-coefficients and the constant-mode formula. At N=4 both full parity blocks are compared with the preserved defining-distribution quadrature, including its separate correlation check. No zeta zeros enter either construction.

For a normalized lowest odd Ritz vector \(v_N\), define \(E_{N,2N}\) to be the coupling from modes 1..N to N+1..2N. These diagnostics are finite windows; no inference that they exhaust the infinite residual is made.

| N | Finite odd gap above the even Ritz minimum | \(\|E_{N,2N}\|_F\) | \(\|E_{N,2N}v_N\|^2\) |
|---:|---:|---:|---:|
| 8 | \(3.90717\times10^{-20}\) | 1.06455 | \(4.42907\times10^{-20}\) |
| 16 | \(8.60834\times10^{-32}\) | 1.12429 | \(1.37844\times10^{-31}\) |
| 32 | \(6.70861\times10^{-46}\) | 1.00326 | \(1.00444\times10^{-45}\) |
| 64 | \(5.70362\times10^{-55}\) | 1.15282 | \(7.98037\times10^{-55}\) |

At N=64, the even and odd Ritz minima are approximately \(6.32135\times10^{-59}\) and \(5.70425\times10^{-55}\). These are upper approximations to the respective spectral bottoms, not certified lower bounds on the limiting gap. Even differences of two Ritz upper bounds have no automatic lower-bound interpretation.

The two leading coupling moments in (23), \(\sum b_mv_m\) and \(\sum mv_m\), have absolute values approximately \(6.85\times10^{-27}\) and \(7.00\times10^{-24}\) at N=64. The second is proportional to the trial function's endpoint derivative. These cancellations explain why replacing the coupling by a single ordinary norm is so wasteful. They do not by themselves bound every remaining direction.

At 120 and 160 decimal digits, all **60 saved numerical observables agree at all 45 retained significant digits**. Maximum identity residuals are below \(8.12\times10^{-121}\) and \(7.83\times10^{-161}\). Checks cover both parity blocks against the earlier quadrature, Ritz eigenpair equations, the exact remainder identity (24), and finite-window errors against the infinite bound (26). Both arithmetic paths lie inside the rational intervals for the two witness entries. Precision agreement and small residuals are diagnostic only; the rigorous statements use the separate analytic inequalities and rational certificate.

## 9. Claim ledger and the next concrete task

| Claim | Status |
|---|---|
| Infinite unshifted odd tail above mode 4096 is at least 2/5 | Proved analytically, with exact rational checks of the constants |
| The scalar norm Schur test using that bound fails for 0<=s<2/5 | Proved, using certified matrix-entry witnesses |
| Uniform \(|b_n|<2\) and finite-rank far-coupling error (26) | Proved; selected numerical constants checked exactly |
| Closed parity-block formulas and N<=64 diagnostics | Derived algebraically and checked at two precisions against the original quadrature; eigenvalues are not interval-certified |
| Matrix Schur positivity (16), or the exact form (15) | Not established |
| A positive limiting odd-sector gap | Not established |
| The previous fixed-support determinant theorem | Still conditional on that gap and its stated finite CCM hypotheses |
| Support-uniform control, Xi identification, original Weil positivity | Not established |

The next task is a **matrix** Schur test at the certified split: retain modes 1..4096, include the intermediate coupling rows 4097..8192, and use the rank-256 far approximation with (26)--(27). Begin by forming the action on the small-energy subspace and its complement, rather than subtracting one scalar penalty from every retained direction. Use an interval-certified even trial energy as the threshold U; report a verified margin or an explicit failed direction of the sufficient Schur form. Do not call a failed sufficient form a negative direction of the original Weil form.

All of those finite matrices or their structured representations, their arithmetic errors, and the infinite Gram-series tails must be controlled before claiming the gap. This round does not assemble or certify the complete 4096-mode Schur form. If (16) fails after these errors are controlled, the next refinement is to estimate the high inverse in (15) in its energy metric instead of bounding it by \((2/5-U)^{-1}I\).

No implication for RH is asserted from the positive high tail alone. The absolute energy offset, the continuum even multiplicity, the support limit, and arithmetic determinant identification retain their prior status.

## Sources and reproducibility

- [CCM, *Zeta Spectral Triples*, arXiv:2511.22755v1](https://arxiv.org/html/2511.22755v1): form decomposition, normalization, closed semibounded operator, Fourier core, and divided-difference matrix. Relevant equations checked against Sections 3--5.
- [NIST DLMF 5.7.6](https://dlmf.nist.gov/5.7.E6), [5.9.13](https://dlmf.nist.gov/5.9.E13), and [5.5](https://dlmf.nist.gov/5.5): digamma series, integral, and recurrence. The kernel remainder and application are derived above.
- All external sources were inspected on 26 September 2026. No third-party PDF is stored in the repository. Reproduction commands, source hashes, and small records are linked from the [numerical guide](../numerics/README.md). No dense 4096-square matrix, draft snapshot, commit, or release is created in this round.

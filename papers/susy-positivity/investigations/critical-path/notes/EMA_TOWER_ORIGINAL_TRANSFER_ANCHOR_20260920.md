# The arithmetic EMA tower gives an all-input anchor

20 September 2026. Prepared for Edward Baker.

**Model:** OpenAI GPT-6 (Codex; system-provided identity). **Reasoning
effort:** not exposed in this reviewing session. The user-reported Extra
High setting belongs to the preceding investigation. **Status:** a
computer-assisted fixed-window proof, with outward rational interval
arithmetic and a separate direct-response check. Specialist mathematical
review remains outstanding. No new depth horizon, all-depth theorem,
physical Wilson realization, localization theorem, or arithmetic Loewner
driver is claimed.

## 1. Result and its place in the program

The [preceding audit](ADAPTIVE_EMA_AUDIT_AND_PILOT_20260920.md) correctly
identified an unresolved input complement in its finite-input pilot.
This note closes that gap at its designated test point, by a different
estimate. We use the **fixed arithmetic EMA tower inside the generator**
to prove a lower bound on the complete central form, and then integrate
a bounded shift perturbation. No adjustable output smoother is appended.

In the normalization of the audit, the bounds are
\[
 Q_{0,1/2}\succeq \frac1{40}I,
 \qquad
 Q_{s,1/2}\succeq
 \left(\frac1{40}-\frac{s^2}{8}\right)I
 \quad(0\le s\le10^{-3}).
 \tag{1.1}
\]
Consequently the **original** complete arithmetic transfer satisfies
\[
 \boxed{\quad
 D_{10^{-3},1/2}
 =I-V_{10^{-3},1/2}^{*}V_{10^{-3},1/2}
 \succeq \frac{24999}{500000000}I
 =0.000049998\,I .
 \quad}
 \tag{1.2}
\]
Equivalently, \(D/(2\omega)\succeq0.024999I\) at this point.
These are bounds for every \(L^2(0,1/2)\) input, not eigenvalues of a
compressed transfer. Section 5 also proves contraction for every
\(0<\omega\le10^{-3}\).

This is a new certificate **within this EMA investigation**, not a claim
that positivity at this window was previously unknown. The parent
Weil-depth/storage-depth work already treats much larger windows.
The contribution is a short, reproducible way to turn the EMA
representation into a bound on all omitted directions. It uses
instantaneous positivity on a small interval of shifts as a sufficient
route to cumulative positivity. The broader program must still allow
cumulative positivity when instantaneous positivity fails.

## 2. A finite tower is a lower operator, not an approximation in norm

Let \(H=L^2(0,L)\), \(L=1/2\), and use zero-history causal EMAs
\[
 S_{1/a}f(x)=a\int_0^x e^{-a(x-y)}f(y)\,dy,\qquad
 a_n=2n+\tfrac12 .
\]
Write
\[
 w_0=-\gamma-\frac{\pi}{2}-3\log2-\log\pi,
 \qquad
 c(x)=\cosh((x-L/2)/2),\quad
 s(x)=\sinh((x-L/2)/2).
\]
The complete central form on this prime-free window is
\[
 Q_0=w_0 I+\sum_{n=0}^{\infty}
       \frac2{a_n}(I-\Re S_{1/a_n})
       +2|c\rangle\langle c|-2|s\rangle\langle s|.
 \tag{2.1}
\]
The pole kernel here is \(2\cosh((x-y)/2)\); its negative odd
rank-one part is retained. The local constant is unchanged.
The digamma identities underlying this normalization are the same
ones used in the manuscript; see
[DLMF 5.4(ii)](https://dlmf.nist.gov/5.4#ii) and
[DLMF 5.9(ii)](https://dlmf.nist.gov/5.9#ii).

Every summand in (2.1) is positive semidefinite: the exact EMA energy
identity proves \(\|S_{1/a}\|\le1\), hence
\(\Re\langle f,S_{1/a}f\rangle\le\|f\|^2\).
For an integer \(M\), set
\[
 T_M=w_0 I+\sum_{n=0}^{M-1}
       \frac2{a_n}(I-\Re S_{1/a_n})
       +2|c\rangle\langle c|-2|s\rangle\langle s|.
 \tag{2.2}
\]
Then \(Q_0\succeq T_M\) on the central form domain.
Each \(T_M\) is a bounded operator on all of \(H\). This follows first
on the smooth core and then by the increasing positive-form sum,
with the same fixed bounded local and pole terms. The cosine functions
used below also belong to the form domain: their zero extensions
belong to \(H^\epsilon(\mathbb R)\) for \(0<\epsilon<1/2\), which controls
the logarithmic form.

There is no assertion that the infinite tower has a small operator-norm
tail. Its positivity lets us discard the tail **in the lower-bound
direction**. This avoids applying the audit's derivative-dependent
gamma tail estimate to arbitrary high-frequency inputs.

## 3. Resolve the endpoints exactly

Use the orthonormal Neumann cosine basis
\[
 \phi_0=L^{-1/2},\qquad
 \phi_j(x)=\sqrt{2/L}\cos(k_jx),\quad k_j=j\pi/L\quad(j\ge1),
 \qquad \rho_j=\phi_j(0).
\]
These functions do not impose artificial zero values at the two
endpoints. Reflection about \(L/2\) gives parity \((-1)^j\).

### 3.1 Robin-to-Neumann decomposition of one EMA term

The kernel of \(\Re S_{1/a}\) is \((a/2)e^{-a|x-y|}\).
Thus \(\Re S_{1/a}=a^2 C_a^R\), where \(C_a^R\) is the resolvent
of \(-\partial_x^2+a^2\) with
\[
 u'(0)=a u(0),\qquad u'(L)=-a u(L).
\]
Its quadratic form differs from the Neumann form by
\(a(|u(0)|^2+|u(L)|^2)\).
Let \(C_a^N\) be the Neumann resolvent and \(Bu=(u(0),u(L))\).
Solving the two boundary conditions gives
\[
 C_a^N-C_a^R
 =C_a^N B^*
 \big(a^{-1}I+B C_a^N B^*\big)^{-1}B C_a^N.
 \tag{3.1}
\]
Here the boundary compositions are bounded; no bounded trace operator
on bare \(L^2\) is assumed. The boundary matrix is explicitly
\[
 B C_a^N B^*
 =a^{-1}
 \begin{pmatrix}\coth(aL)&\operatorname{csch}(aL)\\
 \operatorname{csch}(aL)&\coth(aL)\end{pmatrix}.
\]
Diagonalizing this two-by-two matrix by reflection gives the following
exact representation of (2.2):
\[
 (T_M)_{ij}=d_i\,\delta_{ij}+R_{ij}
                       +2c_i c_j-2s_i s_j,
 \tag{3.2}
\]
\[
 d_j=w_0+\sum_{n=0}^{M-1}\frac2{a_n}
                         \frac{k_j^2}{a_n^2+k_j^2},
 \tag{3.3}
\]
\[
 R_{ij}=
 \begin{cases}
 \displaystyle
 2\rho_i\rho_j\sum_{n=0}^{M-1}
 \frac{a_n^2(1-(-1)^i e^{-a_nL})}
 {(a_n^2+k_i^2)(a_n^2+k_j^2)},&i\equiv j\pmod2,\\
 0,&i\not\equiv j\pmod2 .
 \end{cases}
 \tag{3.4}
\]
For each \(n\), the two parity blocks in (3.4) are positive rank-one
matrices. With \(b=1/2\), the pole coefficients are
\[
 c_j=
 \begin{cases}
 \displaystyle\frac{2b\sinh(bL/2)\rho_j}{b^2+k_j^2},&j\ {\rm even},\\
 0,&j\ {\rm odd},
 \end{cases}
 \quad
 s_j=
 \begin{cases}
 0,&j\ {\rm even},\\
 \displaystyle-\frac{2b\cosh(bL/2)\rho_j}{b^2+k_j^2},&j\ {\rm odd}.
 \end{cases}
 \tag{3.5}
\]
Equations (3.1)--(3.5) can also be obtained by integrating each
exponential kernel directly. The separate numerical check uses
the causal response
\[
 R_a\phi_j(x)
 =\rho_j\frac{a\cos(k_jx)+k_j\sin(k_jx)-a e^{-ax}}
 {a^2+k_j^2},
 \tag{3.6}
\]
including both \(a=b\) and \(a=-b\) for the poles.
It compares the symmetric matrix of the full response with (3.2);
the maximum difference is below \(3.7\,10^{-14}\).
This is a consistency check, not the sign certificate.

### 3.2 An infinite-complement bound

Let \(P\) select modes \(0,\ldots,N-1\), and write
\[
 T_M=\begin{pmatrix}A&B\\B^*&C\end{pmatrix}.
\]
The diagonal \(d_j\) increases with \(j\). Positivity of \(R\) and of
the even pole rank-one term gives
\[
 C\succeq
 \left[d_N-2(2b\cosh(bL/2))^2 F_N\right]I,
 \qquad
 F_r=\frac{2}{L}\left(\frac{L}{\pi}\right)^4
                  \frac1{3(r-1)^3}.
 \tag{3.7}
\]
Indeed \((b^2+k_j^2)^{-2}\le k_j^{-4}\) and
\(\sum_{j=r}^\infty j^{-4}\le1/[3(r-1)^3]\) for \(r\ge2\).
We deliberately do not use the additional parity saving.

For \(i<N\), define the nonnegative coefficient
\[
 E_i=
 2\rho_i\sum_{n=0}^{M-1}
          \frac{a_n^2(1+e^{-a_nL})}{a_n^2+k_i^2}
 +4b\big(|c_i|\sinh(bL/2)+|s_i|\cosh(bL/2)\big).
 \tag{3.8}
\]
For \(j\ge N\), (3.2)--(3.5) imply
\(|B_{ij}|\le E_i\rho_j/k_j^2\).
Consequently, for \(J>N\),
\[
 \|B\|^2\le\|B\|_{\rm HS}^2
 \le
 \sum_{i=0}^{N-1}\sum_{j=N}^{J-1}
    |R_{ij}+2c_i c_j-2s_i s_j|^2
 +F_J\sum_{i=0}^{N-1}E_i^2 .
 \tag{3.9}
\]
The finite portion retains cancellation before squaring. The final
term bounds every remaining column. It is a scalar norm bound;
entrywise upper bounds have not been mistaken for matrix order.

## 4. The rational certificate

Take \(M=32,\ N=16,\ J=128\).
The [certificate program](../numerics/certify_ema_original_anchor.py)
encloses the constants and all expressions (3.2)--(3.9) with outward
rational intervals. Its comparisons prove
\[
 A\succeq\frac{11}{400}I,\qquad
 C\succeq\frac{107}{50}I,\qquad
 \|B\|^2\le\frac{49}{10000}.
 \tag{4.1}
\]
The resulting scalar Schur test at \(m=1/40\) has strict slack
\[
 \left(\frac{11}{400}-\frac1{40}\right)
 \left(\frac{107}{50}-\frac1{40}\right)-\frac{49}{10000}
 =\frac{31}{80000}>0.
 \tag{4.2}
\]
For every \(f=u+v\), \(u=Pf\), this bounds the cross term by
\(2\|B\|\|u\|\|v\|\) and proves \(T_{32}\succeq I/40\).
Together with (2.2), this proves the first assertion in (1.1).

The numbers below are explanatory decimal displays of the enclosed
quantities; sign decisions use their rational endpoints.

| Quantity | Enclosed/evaluated size | Rounded bound used |
|---|---:|---:|
| Lower estimate for \(C\) | \(>2.14533358\) | \(2.14\) |
| Finite mixed-block squared Hilbert--Schmidt norm | \(0.004822740110\ldots\) | included below |
| Remaining mixed-column upper estimate | \(0.0000219271813\ldots\) | included below |
| Complete mixed-block squared norm upper estimate | \(<0.004844668\) | \(0.0049\) |
| Smallest lower endpoint of the LDL pivots of \(A-11I/400\) | \(>0.07214994\) | strictly positive |

The pivot number is **not** an eigenvalue lower bound. Positive pivots
of the exact enclosed LDL recursion establish positive definiteness.

### 4.1 Arithmetic and reproducibility

The implementation uses integers with a fixed denominator \(10^{40}\),
rounding every interval operation outward. It uses no floating-point
eigenvalue or sign decision. Constants are enclosed as follows:

- Machin's identity with alternating arctangent series encloses \(\pi\).
- The positive atanh series with a geometric remainder encloses logs.
- A positive exponential series on \([0,1/2]\), with an explicit
  geometric remainder and repeated squaring, encloses exponentials.
- For \(n=1000\),
  \[
  H_n-\log n-\frac1{2n}\le\gamma
  \le H_n-\log n-\frac1{2(n+1)}.
  \tag{4.3}
  \]
  To verify (4.3), sum
  \[
  \log(1+1/k)-\frac1{k+1}
  =\int_k^{k+1}\frac{k+1-t}{t(k+1)}\,dt.
  \]
  Bound each integrand using \(k\le t\le k+1\), telescope the upper
  series, and use the integral lower bound on
  \(\sum_{k=n}^\infty(k+1)^{-2}\).
- Integer square roots enclose the basis normalizations.

The same rounded certificate passed at 40 and 60 decimal places.
The [small certificate record](../numerics/records/ema-original-anchor-20260920.json)
contains all 16 pivot enclosures, scalar bounds, and the source hash;
no matrix archive is needed.

The [separate reduction checker](../numerics/check_ema_anchor_reduction.py)
checks 130 interval operations against exact Fraction arithmetic,
refuses an explicitly indefinite matrix, and compares the matrix with
direct causal-response quadrature at two orders.
Its [record](../numerics/records/ema-anchor-reduction-checks-20260920.json)
separates those diagnostic checks from the certificate.
These controls do not replace review of the analytic reduction.

## 5. From the central bound to the original cumulative defect

The complete prime-free causal kernel of the **nonlocal part of**
\(G_0\), after the exact lowest gamma-mode/pole cancellation, is
\[
 g(u)=-\frac{2e^{-5u/2}}{1-e^{-2u}}+2e^{u/2},\qquad u>0.
 \tag{5.1}
\]
The local coefficient in the subtracted EMA tower remains \((w_0+4)I\).
Equation (5.1) specifies its off-diagonal kernel; the difference-term
subtractions are essential because this kernel is not integrable at zero.
The shift generator satisfies
\(a_s(p)=[a_0(p-s)+a_0(p+s)]/2\).
Thus \(G_s-G_0\) is convolution on \((0,L)\) by
\[
 g(u)(\cosh(su)-1).
 \tag{5.2}
\]
This difference is a bounded operator even though \(G_0\) is unbounded.
The common domain is therefore preserved. For \(0<u\le L\),
\[
 |g(u)|\le u^{-1}+2e^{L/2},\qquad
 \cosh(su)-1\le\frac{s^2u^2}{2}\cosh(sL).
\]
The first estimate follows from
\(1-e^{-2u}\ge2u e^{-2u}\). Young's inequality gives
\[
 \|G_s-G_0\|
 \le s^2\cosh(sL)
       \left(\frac{L^2}{4}+\frac{e^{L/2}L^3}{3}\right).
 \tag{5.3}
\]
At \(L=1/2,\ 0\le s\le10^{-3}\), the factor multiplying \(s^2\)
is at most \(0.116001074\ldots<1/8\), certified by the same interval
program. This proves the second inequality in (1.1), uniformly on
the form domain. In particular,
\[
 Q_s\succeq m_*I,\qquad m_*=\frac{199999}{8000000}.
 \tag{5.4}
\]

Use the existing shift equation, with its original initial normalization,
\[
 \partial_s V_s=-G_sV_s,\qquad V_0=I.
 \tag{5.5}
\]
On smooth compactly supported inputs the right-Laplace estimates
justify the derivative, and causal convolution preserves the
logarithmic form domain. For example the zero extension of such an
input has arbitrary Sobolev regularity; after convolution on a fixed
window the possible right endpoint jump still lies in \(H^\epsilon\)
for \(0<\epsilon<1/2\). The established generator identity then yields
\[
 \frac{d}{ds}\|V_sf\|^2
 =-2Q_s[V_sf]\le-2m_*\|V_sf\|^2.
\]
One may integrate from \(\epsilon>0\) and use \(V_\epsilon f\to f\)
strongly to reach the initial endpoint. Gronwall and density give,
for every \(f\in L^2(0,1/2)\),
\[
 \|V_\omega f\|^2\le e^{-2m_*\omega}\|f\|^2,\qquad
 D_{\omega,1/2}\succeq(1-e^{-2m_*\omega})I
 \quad(0<\omega\le10^{-3}).
 \tag{5.6}
\]
Boundedness of each \(V_\omega\), needed for the density step, already
follows from its complete \(L^1(0,L)\) kernel.

At \(\omega=10^{-3}\), put \(x=2m_*\omega=199999/4000000000\).
The exact elementary bound \(1-e^{-x}\ge x-x^2/2\) proves (1.2).
Restriction and zero extension also transfer the contraction statement
to each smaller window.

This argument integrates an inequality for the **actual evolving
input** \(V_sf\). It does not replace the cumulative integrand by
\(Q_s[f]\), approximate \(D/(2\omega)\) in operator norm by \(Q_0\),
or infer all-input positivity from a finite matrix alone.

## 6. What remains of adaptive smoothing

For any \(\ell>0\), (1.2) immediately gives the correctly weighted
input-smoothed inequality
\[
 S_\ell^*D_{10^{-3},1/2}S_\ell
 \succeq\frac{24999}{500000000}S_\ell^*S_\ell.
 \tag{6.1}
\]
This is the exact comparison with the audit's input-smoothed
congruence. There is no coercivity claim relative to the unsmoothed
identity metric: \(S_\ell\) is compact with dense range.
The current calculation does not demonstrate a computational gain
from additional input smoothing.

The EMA inspiration has therefore led to a useful proof device:
retain finitely many **prescribed** relaxation scales and keep their
endpoint response exactly; the unused scales contribute a positive
form. Optimizing an additional smoothing length was not needed to
close this anchor. Output-filter storage and path-average variance
remain separate contributions that must be accounted for before
inferring a claim about the original transfer.

## 7. The next obstruction is spatial coupling

For a depth append, the original causal transfer has blocks
\[
 V_{\omega,L+h}=\begin{pmatrix}X&0\\Y&Z\end{pmatrix},
 \quad
 X=V_{\omega,L},\quad Z=V_{\omega,h}.
\]
With \(A=I-X^*X\) and \(C=I-ZZ^*\), a strict contraction on the two
diagonal windows reduces the full contraction question to
\[
 \|C^{-1/2}Y A^{-1/2}\|\le1.
 \tag{7.1}
\]
Equation (1.2) now supplies an all-input lower bound for one anchor
defect \(A\). It does **not** establish (7.1). In particular, a
positive central form at one depth and a local extension procedure
do not show that the total extension length can diverge.

The [next-session note](RESEARCH_CONTINUATION_AFTER_EMA_ANCHOR_20260920.md)
specifies a small append from \(L=1/2\) to \(L=11/20\) at
\(\omega=10^{-3}\) as a controlled test of this normalized cumulative
coupling. Carry the fixed EMA endpoint states across the join, preserve
the signed pole response, and bound the omitted input directions.
Do not demand instantaneous positivity as a necessary condition for
that test. Crossing the first prime threshold is a later extension
and must introduce its exact delay term.

The localization suggestion remains relevant to explaining why a
physical theory might select the arithmetic spectrum and cancellation.
This calculation supplies no localizing supercharge or field-theoretic
selection rule. It starts from the existing arithmetic generator.

## 8. Reproduction and preservation

From the repository root:

~~~sh
python3 papers/susy-positivity/investigations/critical-path/numerics/certify_ema_original_anchor.py --output /tmp/ema-original-anchor-replay.json
python3 papers/susy-positivity/investigations/critical-path/numerics/certify_ema_original_anchor.py --digits 60 --output /tmp/ema-original-anchor-replay-60.json
python3 papers/susy-positivity/investigations/critical-path/numerics/check_ema_anchor_reduction.py --output /tmp/ema-anchor-reduction-replay.json
~~~

The certificate is standard-library-only; the separate diagnostic
checker uses NumPy. Do not run with Python's assertion-disabling
optimization flag. Records contain scalar enclosures and hashes,
not large derived matrices.

The [review](../reviews/ADAPTIVE_EMA_REVIEW_20260920.md) records the
preceding task's replay and one minor correction to its resolution
estimate. Earlier notes and provenance records are preserved as
historical evidence. Wilson--Loewner manuscript pair v0.4 and its
immutable draft snapshots remain unchanged; these new results are
research-note material pending mathematical review.

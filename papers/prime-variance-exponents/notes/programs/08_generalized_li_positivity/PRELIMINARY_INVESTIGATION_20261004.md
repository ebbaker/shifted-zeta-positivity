# Generalized Li coefficients: complete terms, centering, and finite-index tails

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Status: exact decompositions and analytic finite-index budgets with floating-point
diagnostics; no all-index positivity theorem or new variance exponent is proved.

## Outcome and inherited criterion

The prime formula in the charter is correct. Its elementary pole term is
exponentially large and alternates with \(n\) for every fixed \(1<\tau<2\).
This investigation explicitly cancels that term against continuous prime density
and isolates a signed Laguerre transform of the actual prime discrepancy.
Absolute estimates before that cancellation are a poor proposed mechanism.

The inherited criterion is [Freitas, Theorem 1 and Lemma 3.1, pp. 3, 6–7](https://arxiv.org/pdf/math/0507368):
with the normalization

\[
\alpha_n(\tau)=\frac1{(n-1)!}
\left.\frac{d^n}{ds^n}\{s^{n-1}\log\xi(s)\}\right|_{s=\tau},
\]

nonnegativity for every integer \(n\ge1\) is equivalent to zero-freeness of
\(\Re s>\tau/2\). The zero formula uses \(\rho/(\rho-\tau)\), counts
multiplicity, and pairs terms as specified there. We retain this exact convention;
no reciprocal-ratio substitution is made. The
[overview](../../PROJECT_OVERVIEW_20261004.md) then gives \(\delta=\tau-1\).

## 1. Exact elementary and gamma terms

For an analytic function \(h\) near \(\tau>1\), define

\[
T_nh=\sum_{j=1}^n\binom nj\frac{\tau^{j-1}}{(j-1)!}h^{(j)}(\tau).
\]

Leibniz's rule identifies this with the normalized derivative above. Using
\(\xi(s)=(s-1)\pi^{-s/2}\Gamma(1+s/2)\zeta(s)\), define

\[
C_n(\tau)=\frac{1-(-1/(\tau-1))^n}{\tau},
\]
\[
G_n(\tau)=\sum_{j=1}^n\binom nj
 \frac{\tau^{j-1}}{2^j(j-1)!}\psi^{(j-1)}(1+\tau/2),
\quad H_n(\tau)=G_n(\tau)-\frac n2\log\pi,
\]
\[
S_n(\tau)=\sum_{k\ge2}\Lambda(k)k^{-\tau}
L_{n-1}^{(1)}(\tau\log k),\qquad
L_{n-1}^{(1)}(u)=\sum_{j=0}^{n-1}\binom n{j+1}\frac{(-u)^j}{j!}.
\]

Then the complete formula is

\[
\boxed{\ \alpha_n(\tau)=C_n(\tau)+H_n(\tau)-S_n(\tau)\ }. \tag{1}
\]

To verify normalization, \(T_n\log(s-a)=[1-(-a/(\tau-a))^n]/\tau\),
and \(T_ns=n\). Termwise differentiation of
\(\log\zeta(s)=\sum_{k\ge2}\Lambda(k)/(k^s\log k)\), absolutely convergent
locally in \(\Re s>1\), yields \(-S_n\). No zero data enter (1).

The [gamma product, DLMF 5.8.2](https://dlmf.nist.gov/5.8.E2), supplies a
second form useful for rigorous truncation:

\[
G_n(\tau)=-\frac{n\gamma_E}{2}
 +\sum_{m\ge1}\left\{\frac n{2m}
 -\frac{1-(2m/(2m+\tau))^n}{\tau}\right\}. \tag{2}
\]

Every brace is nonnegative. With \(x=\tau/(2m)\), Taylor's theorem gives
\(0\le nx-1+(1+x)^{-n}\le n(n+1)x^2/2\). Hence truncation at \(M\)
has the explicit one-sided bound

\[
0\le G_n-G_{n,M}\le\frac{n(n+1)\tau}{8M}. \tag{3}
\]

For comparison with a convention using \(\Gamma(s/2)\), its elementary
term is \([2-(-1/(\tau-1))^n]/\tau-n\log\pi/2\); the extra \(1/\tau\)
is exactly absorbed into the change of gamma argument. This is a useful
normalization check, not a second definition.

## 2. The necessary centering is exactly computable

Set \(h_{n,\tau}(t)=t^{-\tau}L_{n-1}^{(1)}(\tau\log t)\). For every
fixed \(n\) and \(\tau>1\), finite polynomial integration gives

\[
\int_1^\infty h_{n,\tau}(t)\,dt
=\sum_{j=0}^{n-1}\binom n{j+1}\frac{(-\tau)^j}{(\tau-1)^{j+1}}
=C_n(\tau). \tag{4}
\]

Thus, writing \(\psi(t)=\sum_{k\le t}\Lambda(k)\), the genuinely signed
arithmetic quantity is

\[
D_n(\tau):=S_n(\tau)-C_n(\tau)
=\int_1^\infty h_{n,\tau}(t)\,d[\psi(t)-(t-1)],
\quad\boxed{\ \alpha_n=H_n-D_n\ }. \tag{5}
\]

The shift \(t-1\) makes the endpoint discrepancy zero at \(t=1\). Integration
by parts, with both endpoint contributions zero, gives an equivalent formula

\[
\alpha_n(\tau)=H_n(\tau)+
\int_1^\infty[\psi(t)-t+1]h'_{n,\tau}(t)\,dt,
\]
\[
h'_{n,\tau}(t)=\tau t^{-\tau-1}
\{(L_{n-1}^{(1)})'(\tau\log t)-L_{n-1}^{(1)}(\tau\log t)\}. \tag{6}
\]

The boundary at infinity vanishes using even the elementary
\(\psi(t)\ll t\log t\), since \(\tau>1\) and \(n\) is fixed.
If \(\psi(t)-t\) is used instead, there is an additional \(-n\) in the
formula for \(\alpha_n\); omitting it is an endpoint error.

The precise open sufficient input is now

\[
\boxed{\ D_n(\tau)\le H_n(\tau)\quad\text{for every }n\ge1,
\text{ at one fixed }1<\tau<2.\ } \tag{7}
\]

This is a reformulation, not independent evidence for (7). In particular
\(H_n\) itself need not be positive at small indices. The bound must keep the
sign of the prime discrepancy and the oscillatory Laguerre weight.

At \(\tau=1.99\), the raw elementary term contains \((-1/0.99)^n\).
Thus an attempt to separately estimate the positive elementary/gamma terms and
the absolute prime sum introduces a large cancellation problem artificially.
The centered formula (5) removes this deterministic continuum exactly.

## 3. Rigorous prime-tail budget for each finite index

Let \(K\) be an integer with \(K\ge2\) and \(\log K\ge n/\tau\). From
\(\Lambda(k)\le\log k\) and the finite coefficient formula,

\[
|S_n-S_{n,K}|\le B_n(K,\tau):=
\sum_{j=0}^{n-1}\binom n{j+1}\frac{\tau^j}{j!}
\frac{\Gamma(j+2,(\tau-1)\log K)}{(\tau-1)^{j+2}}. \tag{8}
\]

Here \(\Gamma(a,x)\) is the upper incomplete gamma function. The proof uses
that \(t^{-\tau}(\log t)^{j+1}\) decreases for \(t\ge K\), then bounds
the integer sum by its integral from \(K\). For integer orders the tail
is elementary:
\(\Gamma(j+2,x)=(j+1)!e^{-x}\sum_{\ell=0}^{j+1}x^\ell/\ell!\).

Consequently the exact coefficient lies in the analytic interval

\[
\alpha_n\in[C_n+G_{n,M}-n\log\pi/2-S_{n,K}-B_n,
 C_n+G_{n,M}-n\log\pi/2-S_{n,K}+B_n+n(n+1)\tau/(8M)]. \tag{9}
\]

Evaluating its endpoints with directed rounding would yield a finite-index
certificate. Ordinary floating point does not. For fixed \(n\), (8) tends
to zero as \(K\to\infty\); its polynomial degree and constants grow with
\(n\). This is not an all-index domination estimate.

## 4. Checks and the uniform-index barrier

[check_li_decomposition.py](../../../numerics/08_generalized_li_positivity/check_li_decomposition.py)
passes 192 exact rational checks of (4) and the differentiated gamma summands
for \(1\le n\le12\), \(\tau\in\{3/2,19/10,199/100,2\}\). At
\(\tau=1.99\), \(K=M=100000\), ordinary floating-point evaluations of
(9) are as follows. These are diagnostic endpoint evaluations, **not certified
enclosures**, and are intentionally rounded outward in this table.

| \(n\) | Evaluated interval budget | Absolute prime-tail budget |
| ---: | ---: | ---: |
| 1 | [0.06847, 0.06877] | 0.000142 |
| 2 | [0.22408, 0.23179] | 0.003844 |
| 3 | [0.42412, 0.53633] | 0.056085 |
| 4 | [0.21342, 1.38132] | 0.583921 |

The quickly widening budgets are a direct control against extending finite
positivity to all indices. The script uses no zeros or third-party packages;
all arrays are temporary and only source is stored.

For a hypothetical forbidden zero \(\rho=\beta+i\gamma\), set
\(r=|\rho/(\rho-\tau)|>1\). Exactly,

\[
\log r=\frac12\log\left(1+
\frac{\tau(2\beta-\tau)}{(\beta-\tau)^2+\gamma^2}\right)
\sim\frac{\tau(\beta-\tau/2)}{\gamma^2}\quad(|\gamma|\to\infty).
\]

Thus even increasing this zero's amplitude by a fixed factor requires indices
of order \(\gamma^2/[\tau(\beta-\tau/2)]\). Phase alignment and the other
zeros still matter; this scale is **not a theorem about the first negative
coefficient**. It does show why a fixed finite list cannot certify a common
deformation below \(\tau=2\).

**Assessment:** a clear alternative language and a useful sign/endpoint audit,
but below the three primary arithmetic/Sonin programs in readiness. The next
worthwhile step would be an independent, \(n\)-uniform estimate for the
centered transform in (5), with (8) used only to calibrate finite indices.
No source read here provides that estimate. The raw uncentered absolute-prime
approach should not receive a large computational sweep. See the
[local review](../../../reviews/08_generalized_li_positivity/PRELIMINARY_REVIEW_20261004.md).

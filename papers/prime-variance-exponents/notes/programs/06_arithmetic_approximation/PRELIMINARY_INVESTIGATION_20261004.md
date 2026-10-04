# Prepared arithmetic approximation: exact physical norms and a first obstruction

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Status: preliminary mathematical deductions and finite diagnostics; no norm
convergence, constant-width zero-free strip, or new variance exponent is proved.

## Outcome and scope

The charter's sufficient targets are sound. This investigation supplies explicit
coefficients, an exact full physical norm, and a complete small-\(x\) budget.
The most immediate raw Möbius construction already needs a power-decaying
prepared moment. A logarithmic taper moves that obstruction into an exact prime
discrepancy. Neither construction currently supplies a new global mechanism.

A useful strengthening concerns membership, not convergence: for a finite
Dirichlet polynomial with \(P(1)=0\), the physical representation below proves
\((1-\zeta P)/s\in H^2(\Re s>b)\) for **every \(b>0\)**. The charter only
needed \(b>1/2\). This removes the need for a vertical zeta-growth argument.

The inherited strip transfer and ranking context are in the
[overview](../../PROJECT_OVERVIEW_20261004.md). The general-\(p\) Beurling
criterion is recorded in [Delaunay–Fricain–Mosaki–Robert, pp. 1–2](https://arxiv.org/pdf/1101.1199).
Our conclusions use only its elementary sufficient direction, proved below;
no necessity theorem for the integer-only dictionary is assumed.

## 1. Explicit prepared coefficients and exact Mellin identity

For arbitrary finite coefficients \(a_1,\ldots,a_N\), put

\[
A_N=\sum_{n\le N}\frac{a_n}{n},\quad
P_N(s)=\sum_{n\le N}a_nn^{-s}-A_N,\quad
f_N(x)=-\sum_{n\le N}a_n\rho_{1/n}(x),\quad e_N(x)=1-f_N(x).
\]

Here \(\rho_1=0\), and \(\rho_{1/n}(x)=\{1/(nx)\}-n^{-1}\{1/x\}\).
Thus the nominal \(a_1\) cancels, and \(P_N(1)=0\) exactly. For \(\Re s>0\),
with the removable value at one understood,

\[
\int_0^1\rho_\theta(x)x^{s-1}\,dx
=-\frac{\zeta(s)}s(\theta^s-\theta),\qquad
F_N(s):=\int_0^1e_N(x)x^{s-1}\,dx=\frac{1-\zeta(s)P_N(s)}s. \tag{1}
\]

To check the sign, first integrate \(\{\theta/x\}\) for \(\Re s>1\): the
answer is \(\theta/(s-1)-\theta^s\zeta(s)/s\). The preparation cancels its
first term; boundedness extends the identity to \(\Re s>0\).

At a zeta zero \(\rho=\beta+i\gamma\), \(F_N(\rho)=1/\rho\). If
\(1<p<2\), \(q=p/(p-1)\), and \(\beta>1/p\), Hölder therefore gives

\[
\|e_N\|_p\ge\frac{[q(\beta-1/p)]^{1/q}}{|\rho|}. \tag{2}
\]

Any sequence with \(\|e_N\|_p\to0\), including this integer-only subclass,
excludes every such zero. Boundary zeros are allowed. This implication is
sufficient for the project's \(\delta=2/p-1\); its proof uses neither simple
zeros nor a rightmost zero.

## 2. A full norm formula, with no unresolved quadrature tail

For \(x\in(1/(k+1),1/k)\), write \(1/x=k+u\), \(0<u<1\). Then
\(\rho_{1/n}(x)=\{k/n\}\). Consequently

\[
e_N(x)=E_N(k):=1+kA_N-\sum_{n\le N}a_n\lfloor k/n\rfloor
=1+\sum_{n\le N}a_n\{k/n\},
\]
\[
\boxed{\ \|e_N\|_p^p=\sum_{k\ge1}\frac{|E_N(k)|^p}{k(k+1)}\ }. \tag{3}
\]

Let \(C_N=1+\sum_{2\le n\le N}|a_n|\). For every integer \(K\ge1\),

\[
0\le\|e_N\|_p^p-\sum_{k\le K}\frac{|E_N(k)|^p}{k(k+1)}
\le\frac{C_N^p}{K+1}. \tag{4}
\]

This is the complete missing-small-\(x\) budget, not an empirical truncation.
For the two bounded-coefficient choices below, \(C_N\le N\); choosing
\(K=N^{p+\varepsilon}\) makes this crude tail vanish. One must **also** show
the finite signed mass in (4) tends to zero as \(N\to\infty\). Increasing
\(K\) for each fixed \(N\) only verifies that one finite norm.

The same bounded step function proves the true Hardy identity, in the convention
\(\|F\|_{H^2_b}^2=\sup_{\sigma>b}\int_{\mathbb R}|F(\sigma+it)|^2dt\):

\[
\boxed{\ \|F_N\|_{H^2_b}^2
=2\pi\int_0^1|e_N(x)|^2x^{2b-1}\,dx
=\frac{\pi}{b}\sum_{k\ge1}|E_N(k)|^2
 [k^{-2b}-(k+1)^{-2b}]\ },\quad b>0. \tag{5}
\]

Indeed Mellin–Plancherel applies on each line \(\sigma>b\), and monotone
convergence gives the supremum. Holomorphy follows directly from (1). Its
tail beyond \(K\) is at most \(\pi C_N^2/[b(K+1)^{2b}]\). Thus the Hardy
proposal is exactly a weighted physical approximation problem, not merely
a boundary-line integral of a meromorphic function. At a forbidden zero,
\(\|F_N\|_{H^2_b}^2\ge4\pi(\beta-b)/|\rho|^2\).

## 3. Raw Möbius coefficients: a necessary power moment already on the head

Choose \(a_n=\mu(n)\), and write \(M_1(N)=\sum_{n\le N}\mu(n)/n\).
The divisor identity gives, for every integer \(1\le k\le N\),

\[
\sum_{n\le N}\mu(n)\lfloor k/n\rfloor=1,
\qquad E_N(k)=kM_1(N).
\]

Hence, for fixed \(p>1\),

\[
\|e_N\|_p^p\ge |M_1(N)|^p\sum_{k\le N}\frac{k^{p-1}}{k+1}
\asymp_p |M_1(N)|^pN^{p-1}. \tag{6}
\]

Convergence of **this sequence for all integers \(N\to\infty\)** therefore
requires \(M_1(N)=o(N^{-(1-1/p)})\). Even bounded norms force the corresponding
big-O power bound. Partial summation then continues \(1/\zeta(s)\) to
\(\Re s>1/p\): apply the Mellin integral for \(\sum(\mu(n)/n)n^{-z}\)
with \(\Re z>-(1-1/p)\). Thus this coefficient choice already hides a
fixed-strip input in its prepared moment. This observation does not rule out
another coefficient sequence or even a suitably chosen subsequence.

For the overview's \(p=200/199\), the necessary exponent is \(1/200\).
Known subpower envelopes cannot establish it. In the Hardy norm with
\(b<1\), the analogous head condition is \(|M_1(N)|N^{1-b}\to0\).

## 4. Logarithmic taper: preparation becomes centered prime arithmetic

For \(N\ge2\), take
\(a_n=\mu(n)\log(N/n)/\log N\). Define \(A_N\) as above and
\(\psi(k)=\sum_{m\le k}\Lambda(m)\). Summing the exact convolution
\(\mu*\log=\Lambda\) gives, for \(k\le N\),

\[
\sum_{n\le N}a_n\lfloor k/n\rfloor
=1+\frac{\psi(k)}{\log N},\qquad
E_N(k)=kA_N-\frac{\psi(k)}{\log N}. \tag{7}
\]

The necessary head budget is now

\[
\sum_{k\le N}\frac{|kA_N-\psi(k)/\log N|^p}{k(k+1)}\longrightarrow0, \tag{8}
\]

together with the remaining \(N<k\le K_N\) mass and (4). Replacing
\(A_N\) by \(1/\log N\) without a quantitative scalar mismatch budget is
invalid. PNT-scale estimates on the resulting \(\psi(k)-k\) yield only
subpower savings against the head's polynomial weight. The taper creates a
signed arithmetic task; it does not solve that task.

## 5. Checks, finite observations, and next gate

[check_prepared_steps.py](../../../numerics/06_arithmetic_approximation/check_prepared_steps.py)
passes 2,108 exact rational checks of the floor/fraction and raw Möbius head
identities for \(2\le N\le32\), \(1\le k\le4N\). Its finite diagnostics
at \(p=200/199\), \(K=100000\) give the following upper-budget evaluations.
They use ordinary floating point and are **not interval certificates**.

| \(N\) | Raw Möbius norm budget | Tapered norm budget |
| ---: | ---: | ---: |
| 8 | 0.067948 | 0.547008 |
| 16 | 0.188387 | 0.415007 |
| 32 | 0.228971 | 0.335025 |

The unusually small raw value at \(N=8\) is a control against reading a
short decreasing sequence as convergence. No optimized coefficients,
general integer-dictionary necessity, or asymptotic contraction was checked.
The displayed algebra and tail inequalities are fresh deductions here;
their finite checks are not substitutes for the proofs above. No third-party
paper or generated array is stored.

**Assessment:** useful exploratory branch, below the three main arithmetic/Sonin
programs in readiness. A bounded continuation should propose a coefficient
construction that controls (3) or (5) by an independently established arithmetic
estimate, including the entire \(k>N\) region. A finite convex minimizer can
calibrate that estimate, but cannot replace it. Stop an attempted proof if its
only new hypothesis is the power moment in (6), or if it drops the scalar term
in (7). See the [local review](../../../reviews/06_arithmetic_approximation/PRELIMINARY_REVIEW_20261004.md).

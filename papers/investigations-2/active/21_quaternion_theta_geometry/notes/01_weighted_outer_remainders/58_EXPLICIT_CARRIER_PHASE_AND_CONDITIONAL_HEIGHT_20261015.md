---
research_program: PR01
secondary_programs: [PR03, COORD]
status: proved-carrier-budget-with-imported-arithmetic-constant-unresolved
---

# Completing the carrier phase budget in the outer theorem

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6-astra**, reasoning effort **ultra**, verified from the parent conversation metadata. This is incremental research with internal LLM checking, not external refereeing or formal proof verification.

This continues [Note 43](43_EXPLICIT_WEIGHTED_REMAINDER_CONSTANT_PACKAGE_20261015.md), which isolates the imported constant in the disc and weighted-remainder budgets. It evaluates the elementary derivative stage expressly left open there. The complete normalized four-jet error now has a numerical formula in the one remaining arithmetic package, the actual exponent-pair constant and any validity threshold. No new unconditional sign domain or evaluated full-sign starting height is claimed.

## 1. Statement

Retain Note 43's hypotheses

\[
 L=\log(x/(4\pi))\ge100002,\qquad 0<t\le\tfrac12,
 \qquad tL\ge61/24,
\]

and the manuscript's analytic branches

\[
 s_\pm(z)=(1\pm iz)/2,\quad
 w_\pm=s_\pm+\tfrac t2\alpha(s_\pm),\quad
 Q_\pm=M_t(s_\pm)\zeta(w_\pm),\quad
 \mathcal P_t=Q_++Q_-.
\]

Put \(Q=Q_+(x)\), \(\omega=L/4\), and \(\phi=\arg Q\). The following estimate is unconditional on this domain, independently of the exponent-pair constant:

\[
 \max_{0\le k\le3}
 \left|\frac{\mathcal P_t^{(k)}(x)}{2|Q|\omega^k}
   -\cos(\phi+k\pi/2)\right|\le\frac{409}{L}.       \tag{1}
\]

The time is held fixed during every derivative. This differentiates the nonzero analytic carrier, never the moving Riemann--Siegel cutoff.

Assuming Note 43's exact numerical package (EP), let \(C=C_{\rm EP}\), \(\Lambda=L-1\), and retain

\[
 A_0=\frac{36138917}{16},\quad G_0=\frac{962773}{671},\quad
 \lambda=\frac{21807}{254720000}-\frac{63}{50}\,10^{-5}
       >\frac1{14000},
\]
\[
 B_C(L)=\frac{4A_0}{\Lambda}+64e^{-\Lambda/40}
       +8G_0C e^{-\lambda\Lambda}
       +16\Lambda^2e^{-3\Lambda/4}+6e^{-2\Lambda/5}.
\]

Then the **complete** physical phase-vector error is at most

\[
 d_C(L):=1728B_C(L)+\frac{409}{L}.                     \tag{2}
\]

Consequently \(d_C(L)\le1/8\) implies

\[
 E\ge2|Q|^2\ge2\Gamma^2/81,\qquad
 \mathcal L_0\ge\frac{31}{16}|Q|^2\omega^2,\qquad
 \mathcal L_1\ge\frac{31}{16}|Q|^2\omega^4,             \tag{3}
\]

where \(\Gamma=|M_t((1+ix)/2)|\). No stationary hypothesis is needed for these conditional full signs.

## 2. Explicit zeta logarithmic derivatives

For \(\Re w\ge9/8\), the absolutely convergent Euler product gives a nonvanishing zeta function and a locally analytic logarithm. For \(m=1,2,3\), termwise differentiation gives

\[
 g_m(w):=\frac{d^m}{dw^m}\log\zeta(w)
 =(-1)^m\sum_{n\ge2}\Lambda_{\rm vM}(n)(\log n)^{m-1}n^{-w}.
\]

Here \(\Lambda_{\rm vM}(n)\le\log n\) is the von Mangoldt function, distinct from the log-height \(\Lambda\). The standard Euler product is recorded in [NIST DLMF 25.2.11](https://dlmf.nist.gov/25.2.E11); the derivative estimate below is derived here, rather than imported as a numerical constant.

The nonnegative function \((\log y)^m y^{-9/8}\) is unimodal. Comparing its sum to its integral and paying one maximum, as in Note 43, yields

\[
 |g_m(w)|\le\sum_{n\ge2}(\log n)^m n^{-9/8}
 \le\int_1^\infty(\log y)^m y^{-9/8}\,dy+m^m
 =m!8^{m+1}+m^m.
\]

Thus

\[
 |g_1|\le65,\qquad |g_2|\le1028,\qquad |g_3|\le24603. \tag{4}
\]

All series differentiations are justified by local uniform absolute convergence inside \(\Re w>1\). Note 43's explicit geometry ensures \(\Re w_+(x)\ge9/8\), so (4) applies at every real center in the domain.

## 3. Explicit carrier derivatives

At \(s=(1+ix)/2\), set \(a=\alpha(s)\), where

\[
 \alpha(s)=\frac1{2s}+\frac1{s-1}+\frac12\operatorname{Log}\frac{s}{2\pi}.
\]

The elementary identity

\[
 a-\frac L2-\frac{i\pi}4
 =\frac1{2s}+\frac1{s-1}
   +\frac14\log(1+x^{-2})-\frac i2\arctan(x^{-1})
\]

gives

\[
 |a-L/2-i\pi/4|\le4/x,\quad |a-L/2|<1,\quad |a|\le L/2+1.
\]

Indeed \(x>e^L\ge L^3/6>10^{12}\), and \(x=4\pi e^L>L^2\). Hence \(L\le\sqrt x\) and \(|a|\le\sqrt x\). Direct differentiation gives

\[
 |a'|\le x^{-1}+6x^{-2}\le2/x,
 \quad |a''|\le2x^{-2}+24x^{-3}\le3/x^2,
 \quad |a'''|\le8x^{-3}+144x^{-4}\le9/x^3.             \tag{5}
\]

Primes in (5) mean derivatives in \(s\). Define

\[
 b=1+\tfrac t2a',\qquad c=\tfrac t2a'',\qquad d=\tfrac t2a'''.
\]

Then

\[
 |b-1|\le\frac1{2x},\quad |b|\le\frac{1001}{1000},\quad
 |c|\le\frac3{4x^2},\quad |d|\le\frac9{4x^3}.         \tag{6}
\]

Write \(q_r=\partial_x^r\log Q_+(x)\). Since \(ds/dx=i/2\), exact chain rules give

\[
 q_1=\frac i2 b(a+g_1),
\]
\[
 q_2=-\frac14\{a'b+c(a+g_1)+g_2b^2\},
\]
\[
 q_3=-\frac i8\{a''b+2a'c+d(a+g_1)+3g_2bc+g_3b^3\}. \tag{7}
\]

These formulas include derivatives of both \(M_t\) and \(\zeta(w_+)\), including the heat-dependent argument shift. From (4)--(6),

\[
 |q_1-i\omega|
 \le\tfrac12\left(1+\frac1{2000000}+65\frac{1001}{1000}\right)<34.
\]

For \(q_2\), its first two terms in braces are each less than one; for \(q_3\), its first four terms are each less than one. Thus

\[
 |q_2|\le\frac{2+1028(1001/1000)^2}{4}<260,\qquad
 |q_3|\le\frac{4+24603(1001/1000)^3}{8}<3100.          \tag{8}
\]

For example, the only terms involving the potentially growing \(a\) are bounded by

\[
 |c(a+g_1)|\le\frac3{4x^{3/2}}+\frac{195}{4x^2}<1,
 \quad
 |d(a+g_1)|\le\frac9{4x^{5/2}}+\frac{585}{4x^3}<1.
\]

This shows uniformity even when \(tL\) grows without bound; no fixed-theta substitution has been made.

## 4. Recovering the phase vector

The exact exponential derivative identities are

\[
 Q_+'=Qq_1,\quad Q_+''=Q(q_1^2+q_2),\quad
 Q_+'''=Q(q_1^3+3q_1q_2+q_3).
\]

Writing \(q_1=i\omega+r\), with \(|r|\le34\), gives the following normalized errors for derivative orders one, two, and three respectively:

\[
 \frac{136}{L},\qquad
 \frac{272}{L}+\frac{22656}{L^2},\qquad
 \frac{408}{L}+\frac{67968}{L^2}+\frac{4411136}{L^3}.
\]

Each is at most \(409/L\) for \(L\ge100002\). The zeroth-order comparison is exact. On the real axis \(Q_-^{(k)}=\overline{Q_+^{(k)}}\), so taking twice the real part proves (1). Adding Note 43's separately established analytic-replacement error \(1728B_C(L)\) proves (2). The manuscript's direct quadratic perturbation calculation at \(d\le1/8\) proves (3).

## 5. A closed conditional height formula

A deliberately conservative sufficient condition for \(d_C(L)\le1/8\) is

\[
 L\ge1+\max\left\{749376582912,
       14000\log(663552G_0C_{\rm EP})\right\}.         \tag{9}
\]

Also retain \(x-L^{-1}\ge3T_{\rm EP}\) if the imported exponent-pair package is only valid above \(T_{\rm EP}\). Formula (9) is a conditional height in the actual imported constant, not a numerical evaluation of that constant.

To verify (9), allot \(1/48\) to each of the five terms of \(1728B_C\) and to \(409/L\). The first term is covered because

\[
 48\cdot1728\cdot4A_0=331776A_0=749376582912.
\]

The third term is covered by the logarithmic condition and \(\lambda>1/14000\). The other four are already less than \(1/48\) on \(L\ge100002\). Purely algebraic exponential lower bounds suffice: for \(\Lambda\ge100001\),

\[
 e^{\Lambda/40}\ge(\Lambda/40)^3/6>5308416,
\]
\[
 e^{\Lambda/4}\ge(\Lambda/4)^3/6\ge\Lambda^2,
 \qquad e^{\Lambda/2}\ge\Lambda^2/8>1327104,
\]
\[
 e^{2\Lambda/5}\ge2\Lambda^2/25>497664,
 \qquad L>48\cdot409.
\]

The result removes the carrier differentiation budget from the unresolved list. The remaining independent input for an evaluated full-sign starting height is the true numerical exponent-pair package (EP), with its positive loss, interval uniformity, A-process/completion costs, and any validity threshold. The manuscript and Note 39's five-halves middle-interval obstruction are unchanged: altering constants cannot reverse a positive limiting power there. The cusp estimate and finite bridge remain open.

## 6. Reproducible scope

The accompanying standard-library checker verifies all displayed finite numerical inequalities using rational arithmetic. It also verifies the three exact derivative polynomials and their phase-error coefficients. It does not prove the Euler-product identities, infinite-sum comparison, analytic differentiation or imported arithmetic theorem; those arguments are supplied above or retained from Note 43. No finite stationary-root data, energy floor, or source-truncation identity is used.

The [checker](../../numerics/check_carrier_phase_budget.py) and [receipt](../../numerics/CARRIER_PHASE_BUDGET_CHECKS_20261015.json) record 43 passing exact assertions. [Review 33](../../reviews/33_PRIMITIVE_CIRCLE_AND_CARRIER_CONTINUATION_REVIEW_20261015.md) records independent analytic checks and replay.

---
research_program: PR02
secondary_programs: [PR02-CORR, PR03]
status: conditional_transfer_and_local_rigidity
---

# A subpower stationary-loss transfer with Gaussian source tails

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6.1-sol**, reasoning effort **ultra**, verified from this conversation’s session metadata. Separate internal analytic checking supports the argument. This is a conditional transfer argument, not a new arithmetic lower bound or sign region.

This continues the all-cutoff transfer and analytic rigidity in [Note 30](../30_THETA_SIGNED_CUTOFFS_AND_ANALYTIC_LOG_LOSS_20261014.md), [Note 36](../05_theta_correlation_kernels/36_COMPLETE_THETA_CORRELATIONS_AND_SIGN_TARGETS_20261015.md), and the integrability requirements in [Note 41](../00_research_coordination/41_POISSON_OBSTRUCTION_AND_REMAINDER_CONTINUATION_20261015.md). The previously adopted polynomial-in-cutoff hypothesis remains sufficient. The result below permits a larger cutoff cost while retaining exclusion of every finite analytic collision multiplicity. It supplies no source inequality satisfying its hypothesis.

## 1. A conditional all-cutoff transfer

Retain the complete physical jets, \(E=h_0^2+h_1^2\), the observations \(\mathcal L_j\), and both full stationary sets \(S_j=\{h_{j+1}=0\}\), \(j=0,1\). Let \(\mathcal D\) be a declared positive-time domain. Suppose one has independently proved, on \(S_j\cap\mathcal D\),

\[
\mathcal L_j\ge
-A_j N^p\exp\{a_j(\log N)^2\}E
-B_j e^{-c_jN^2}
\qquad\text{for every integer }N\ge N_{0,j}\ge1. \tag{1}
\]

Here \(p\ge0\) is fixed and finite. The nonnegative quantities \(A_j,B_j,a_j\), positive \(c_j\), and integer \(N_{0,j}\) are prescribed independently of the unknown energy and of the subsequently selected cutoff. Require \(A_j,B_j,a_j,c_j^{-1},N_{0,j}\) to be locally bounded through every covered finite positive-time candidate collision. No division by \(E\), sampled energy floor, or coefficient fitting is part of this hypothesis.

Fix \(M>0\). For \(e>0\), define

\[
\ell_e=1+\log_+(M/e),\qquad
\eta_e=\log(1+\ell_e)=\log\{2+\log_+(M/e)\}.
\]

Set \(d_{B,j}=\log_+(B_j/M)\) if \(B_j>0\), and zero otherwise. Define the prescribed quantities

\[
D_j=N_{0,j}+1+c_j^{-1/2}\sqrt{1+d_{B,j}},\qquad
d_j=\frac{\log D_j}{\log2}+\frac12,
\]

\[
K_j=A_j+1,\qquad
C_j=a_jd_j^2+\frac{p\,d_j}{\log2}. \tag{2}
\]

Then

\[
\boxed{\mathcal L_j\ge
-K_j E\exp\!\left[C_j
\left\{\log\bigl(2+\log_+(M/E)\bigr)\right\}^{2}\right].} \tag{3}
\]

The right side is defined as zero at \(E=0\). Both \(K_j\) and \(C_j\) are nonnegative, source-prescribed, and locally bounded under the stated assumptions.

For the proof, take \(E>0\) and only now choose

\[
N=\left\lceil\max\left\{N_{0,j},
\sqrt{c_j^{-1}\log_+(B_j/E)}\right\}\right\rceil,
\]

where the logarithm is zero when \(B_j=0\). Then \(B_je^{-c_jN^2}\le E\), and the manuscript's elementary cutoff estimate gives

\[
N\le D_j\sqrt{\ell_E}.
\]

Because \(\eta_E\ge\log2\) and \(\log\ell_E\le\eta_E\),

\[
\log N\le\log D_j+\tfrac12\log\ell_E
\le d_j\eta_E.
\]

Consequently

\[
N^p e^{a_j(\log N)^2}
\le\exp\{p d_j\eta_E+a_jd_j^2\eta_E^2\}
\le e^{C_j\eta_E^2}.
\]

Substitution in (1), and \(e^{C_j\eta_E^2}\ge1\), prove (3). When \(E\ge M\), one has \(\ell_E=1\) and \(\eta_E=\log2\), so the same estimates include this case. At \(E=0\), let \(N\to\infty\) in (1). Only \(c_j^{-1}\) needs a local bound, with no upper bound for \(c_j\). The optimization depends on \(E\) only after all members of (1) have been proved with the same coefficient rules.

## 2. Full-amplitude observations and original source cutoffs

The same conclusion follows from an all-cutoff bound of the form (1) for the manuscript's full-amplitude observation

\[
J_{j,N}=-h_j h_{j+2}^{(N)},
\]

provided its original complete source-tail payment is retained:

\[
|J_{j,N}-\mathcal L_j|
\le Q_j\sqrt E\,e^{-c_{0,j}N^2}.
\]

When importing the manuscript’s staircase tail, replace \(N_{0,j}\) by \(\max\{N_{0,j},8\}\) to retain its original cutoff range. Here \(Q_j\ge0\) and \(c_{0,j}>0\) are source-prescribed, with \(Q_j,c_{0,j}^{-1}\) locally bounded through covered events. Young's inequality gives

\[
Q_j\sqrt E\,e^{-c_{0,j}N^2}
\le\tfrac12 E+\tfrac12Q_j^2e^{-2c_{0,j}N^2}.
\]

Thus use (2) with

\[
\widehat A_j=A_j+\tfrac12,\qquad
\widehat B_j=B_j+\tfrac12Q_j^2,\qquad
\widehat c_j=\min(c_j,2c_{0,j}),
\]

and the same \(a_j,p,N_{0,j}\). This is valid because
\(N^p e^{a_j(\log N)^2}\ge1\). A separately paid Gaussian difference for a raw retained observation can likewise be absorbed into the tail coefficient and rate. Both observations and every stationary condition continue to use the full physical jets.

This transfer does not replace the manuscript's hybrid staircase by a rectangular correlation cutoff. When that staircase is used, all source-index boundaries, contour shifts, retained/omitted mixed sectors, and complete source-tail payments remain in force. A newly chosen all-cutoff family must establish its own exact observation and complete error budget before applying the argument.

## 3. Why the transferred loss still excludes every finite analytic multiplicity

On a sufficiently near predecessor of a finite positive-time collision of the relevant parity, the manuscript proves, for \(s=T-t\downarrow0\),

\[
E\sim k^2s^{2r},\qquad
-\mathcal L_j/E=r/s+O(1),\qquad r\ge1,
\]

with finite \(r\) and \(k\ne0\). Local boundedness in (3) gives fixed finite upper bounds \(K_*,C_*\) near that event. Since

\[
\eta_E=O(\log\log(1/s)),\qquad
\exp(C_*\eta_E^2)
=\exp\{O((\log\log(1/s))^2)\}=s^{-o(1)},
\]

inequality (3) would force \(r/s+O(1)\le K_*s^{-o(1)}\), a contradiction. Equivalently, the logarithm of the ratio of the left side to its permitted coefficient tends to infinity because

\[
\log(1/s)-O((\log\log(1/s))^2)\longrightarrow+\infty.
\]

Hence the conditional hypothesis excludes collisions only where both appropriate stationary levels and the necessary predecessor neighborhoods are covered. It makes no unconditional RH claim.

The extension is qualitative: the new loss is larger than every fixed logarithmic power when \(C_j>0\), yet smaller than every fixed inverse power of \(E\) near zero. Allowing such a larger gauge can help organize a genuine signed arithmetic estimate, but cannot supply that estimate.

## 4. Analytic local rigidity for a subpower gauge

The manuscript's analytic rigidity lemma extends beyond fixed logarithmic powers. Let \(S\) be semianalytic near a finite point \(p\), and \(E\ge0,L\) real analytic in an ambient neighborhood. Let \(G(e)>0\) be a fixed gauge for small \(e>0\) such that, for every \(\varepsilon>0\),

\[
G(e)=o(e^{-\varepsilon})\qquad(e\downarrow0). \tag{4}
\]

Suppose on \(S\) near \(p\), for bounded \(K\ge0\),

\[
L\ge-K E G(E),
\]

with right side zero at \(E=0\). Then on a smaller neighborhood in \(S\), some finite \(C\ge0\) satisfies \(L\ge-CE\).

Indeed, failure of the linear bound gives points with \(E>0\), \(-L>0\), and \(E/(-L)\to0\). Apply the same real analytic curve-selection argument as in the existing rigidity lemma to the semianalytic set

\[
\{(z,u):z\in S,\ E(z)>0,\ -L(z)>0,\ u>0,\ E(z)=u[-L(z)]\}.
\]

It produces an analytic arc with

\[
u(\rho)=a\rho^k(1+o(1)),\qquad
E(z(\rho))=b\rho^m(1+o(1)),\qquad a,b>0,\quad k,m\ge1.
\]

The assumed gauge inequality would give

\[
u(\rho)^{-1}\le K G(E(z(\rho))).
\]

Taking \(\varepsilon=k/(2m)\) in (4) makes the right side \(o(\rho^{-k/2})\), while the left side has order \(\rho^{-k}\), a contradiction. At \(E=0\) the assumed inequality already gives \(L\ge0\).

For every fixed finite \(C_*,M>0\),

\[
G(e)=\exp\!\left[C_*\{\log(2+\log_+(M/e))\}^{2}\right]
\]

satisfies (4). Locally bounded variable \(C_j\) in (3) is dominated by such a fixed \(C_*\). This establishes local rigidity under the declared analytic/semianalytic hypotheses. It does not construct a source-prescribed linear coefficient or an effective constant, and it does not replace a needed domain-coverage argument.

## 5. What a Poisson sector norm does and does not supply

The expanding-box axis calculation can force separate absolute sector norms to grow like \(\exp\{a(\log N)^2+O(\log N)\}\). Such growth lies outside the previously adopted polynomial-in-\(N\) transfer class, but its growth rate alone does not rule out a future signed family of the form (1).

There remains a separate missing premise: the adverse contribution must already carry the factor \(E\), with source-prescribed locally bounded coefficients and a paid Gaussian remainder. A bound on a sector by its absolute norm, with no \(E\) factor, does not establish (1), (3), or collision exclusion. Nor does an exact localized identity establish its required signed lower bound. Every proposed mechanism still needs combined integrability in both independent source coordinates, both full stationary sets, and predecessor coverage.

No new stationary pilot, manuscript change, or expanded sign domain is asserted here.


[Review 28](../../reviews/28_LOCALIZED_POISSON_AND_EFFECTIVE_BUDGET_REVIEW_20261015.md) records the internal analytic audit. No finite arithmetic sampling is presented as a test of this conditional universal argument.

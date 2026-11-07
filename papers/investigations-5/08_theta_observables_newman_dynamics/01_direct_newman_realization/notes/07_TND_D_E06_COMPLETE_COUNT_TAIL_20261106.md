# TND-D-E06 r1: complete count-tail value and first-derivative bounds

6 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. **E — execution**, frozen **TND-D-E06 r1**. Requested and actual worker: **gpt-6.1-sol / ultra**. Actual settings were verified from the worker's current local rollout `turn_context`: thread `01a1afd1-c30a-7ef0-8e40-fdc521a43a95`, turn `01a1afe0-8061-76e3-8ea8-88e098363760`, source `/Users/ebbaker/.codex/sessions/2026/11/06/rollout-2026-11-06T02-45-22-01a1afd1-c30a-7ef0-8e40-fdc521a43a95.jsonl`.

**Disposition: r1's absolute complete-tail theorem is proved at proof-author level, pending E07 assessment.** This note pays omitted count mass and its first real-readout derivative. It makes no further tail-sign claim. One proof pass and one local check were used; no numerics, optimization, recursive delegation, shared-file edits or public-chat capture. Primary owns installation and integration.

All six complete file hashes and byte counts in the [frozen inputs][inputs] matched at intake. Manifest SHA-256: `1cfc3ecf2486bea0c3d25873c67466691ff3f4a5bfaf8234761905a6fb7314e0`. The [request][request] is unchanged. We consume [Note06][note06]'s second centered-moment estimate, accepted within scope by [E04 Review03][review03], rather than repeat its localization proof. The inherited [E01][e01] source/domain and [count dictionary][count] retain their existing conditional and internal-review qualifications.

## 1. Positive count envelopes and an explicit uniform ratio

Keep \(\gamma>0\) fixed, \(\alpha=\gamma t\in[0,1]\), \(\lambda=1/2-\alpha\), and the complete source and normalization \(h_*=H_{1/2}(0)>0\). Write

\[
 I_m(\lambda)=\int_0^\infty r^m e^{\lambda r^2}\Phi(r)\,dr,
 \qquad
 B_j^{(q)}(t)=\frac{\alpha^j}{j!h_*}I_{2j+q}(\lambda),\quad q=0,2.
 \tag{1}
\]

Here \(B_j^{(0)}=P_j\), and \(B_j^{(2)}\) is a positive scalar second-moment envelope, not a new readout. At \(\alpha=0\) use the inherited convention: the factor is one for \(j=0\) and zero for \(j>0\).

Let \(a_j\), \(C_2\), \(J\) be the accepted Note06 data:

\[
 j=2\pi a_je^{4a_j},\qquad
 \sup_{|\lambda|\le1/2}\mathbb E_{\nu_{j,\lambda}}(r-a_j)^2
 \le C_2a_j/j\quad(j\ge J).
 \tag{2}
\]

Minkowski's inequality in the positive probability measure \(\nu_{j,\lambda}\) gives

\[
 \mathbb E_{\nu_{j,\lambda}}r^2
 \le\left(a_j+\sqrt{C_2a_j/j}\right)^2.
 \tag{3}
\]

Set \(D=(1+\sqrt{C_2})^2\). If \(a_j\ge1\), then \(ja_j\ge1\), so the right side of (3) is at most \(Da_j^2\). For \(\alpha>0\), the exact moment ratios are

\[
 \frac{B_{j+1}^{(0)}}{B_j^{(0)}}
 =\frac\alpha{j+1}\mathbb E_{\nu_{j,\lambda}}r^2,
 \qquad
 \frac{B_{j+1}^{(2)}}{B_j^{(2)}}
 =\frac\alpha{j+1}\mathbb E_{\nu_{j+1,\lambda}}r^2.
 \tag{4}
\]

The shift to \(j+1\) in the second expectation is essential. From the exact center equation,

\[
 \frac{a_j^2}{j}=\frac{a_je^{-4a_j}}{2\pi}.
\]

Since \(a_j\) increases and \(a\mapsto ae^{-4a}\) decreases for \(a>1/4\), \(a_j^2/j\) decreases whenever \(a_j\ge1\), and tends to zero. Choose any integer \(N_0\ge1\) with

\[
 N_0+1\ge J,\qquad a_{N_0+1}\ge1,\qquad
 D\frac{a_{N_0+1}^2}{N_0+1}\le\frac12.
 \tag{5}
\]

Such a finite threshold exists; no numerical value is needed. For every integer \(N\ge N_0\), define the concrete envelope

\[
 Q_N(t)=\alpha D\frac{a_{N+1}^2}{N+1}.
 \tag{6}
\]

It satisfies \(0\le Q_N(t)\le\alpha/2\le1/2<1\) on the closed physical slab. For every \(j>N\), (3)--(4) and the proved decreasing envelope give simultaneously

\[
 B_{j+1}^{(q)}(t)\le Q_N(t)B_j^{(q)}(t),\qquad q=0,2.
 \tag{7}
\]

Indeed, for \(q=0\) the ratio is at most \(\alpha Da_j^2/(j+1)\le\alpha Da_j^2/j\); for \(q=2\) it is at most \(\alpha Da_{j+1}^2/(j+1)\). Both are bounded by (6). At \(\alpha=0\), the ratios in (4) are undefined but the inequalities (7) hold directly because both terms vanish. No division by a zero count mass is used.

For \(m=N+1\) in this range, \(4a_m=\log m-\log(2\pi a_m)\le\log m\). Consequently

\[
 Q_N(t)\le\frac{\alpha D\log^2(N+1)}{16(N+1)}
 =O\!\left(\frac{\alpha\log^2 N}{N}\right).
 \tag{8}
\]

This is an explicit eventual envelope, not an assumed monotonicity property of an unspecified asymptotic remainder.

## 2. Independent complete-source summation and differentiation

Use the half-line initial probability measure and complete Poisson kernel

\[
 d\mu_*(r)=h_*^{-1}e^{r^2/2}\Phi(r)\,dr,
 \qquad p_j(y)=e^{-y}y^j/j!.
 \tag{9}
\]

At \(y=0\), \(p_0=1\), \(p_{j>0}=0\). The full source majorant makes \(\int r^q\,d\mu_*<\infty\) for \(q=0,1,2\); it pays the complete theta sum and unbounded radial domain. The original signed Kraus amplitudes give the already verified identities

\[
 d_j(t,k)=\int_0^\infty p_j(\alpha r^2)\cos(kr)\,d\mu_*(r),
 \qquad B_j^{(q)}=\int_0^\infty r^qp_j(\alpha r^2)\,d\mu_*(r).
 \tag{10}
\]

All angular shells and signs are retained: their complete trace is exactly one, as checked in Note06. Equation (10) does not replace signed odd-count amplitudes by their absolute values; their two diagonal occurrences already give \(r^{2j}\).

The positive exponential series gives \(\sum_{j\ge0}p_j(y)=1\). Tonelli therefore supplies, on the entire closed slab,

\[
 \sum_{j\ge0}B_j^{(0)}=1,\qquad
 \sum_{j\ge0}B_j^{(2)}=\int r^2\,d\mu_*<\infty.
 \tag{11}
\]

For a direct uniform-tail payment, put

\[
 \tau_N(y)=1-e^{-y}\sum_{j=0}^N y^j/j!\in[0,1].
\]

Differentiating this finite expression gives \(\tau_N'(y)=e^{-y}y^N/N!\ge0\). Thus
\(\tau_N(\alpha r^2)\le\tau_N(r^2)\to0\) pointwise as \(N\to\infty\), for every \(0\le\alpha\le1\). Dominated convergence, with dominating functions \(1,r,r^2\) under \(\mu_*\), gives

\[
 \sup_{0\le\alpha\le1}\int r^q\tau_N(\alpha r^2)\,d\mu_*
 \le\int r^q\tau_N(r^2)\,d\mu_*\longrightarrow0,
 \qquad q=0,1,2.
 \tag{12}
\]

For each fixed \(j\), differentiating (10) in real \(k\) is justified by domination by \(rp_j\). Hence

\[
 \partial_kd_j(t,k)=-\int r p_j(\alpha r^2)\sin(kr)\,d\mu_*.
 \tag{13}
\]

Equations (10), (12)--(13) prove uniform convergence of the value and first-derivative series over every real \(k\) and the closed alpha slab, using their own positive source bounds. Absolute integrability/Tonelli and the same dominated differentiation give the complete identities

\[
 \sum_{j\ge0}d_j(t,k)=\frac{H_{1/2}(k)}{h_*},\qquad
 \partial_k\sum_{j\ge0}d_j(t,k)
 =\sum_{j\ge0}\partial_kd_j(t,k)
 =\frac{H_{1/2}'(k)}{h_*}.
 \tag{14}
\]

In particular, no derivative of a previously established count identity is accepted merely formally. For the complete remainder itself,

\[
 R_N(t,k)=\int\tau_N(\alpha r^2)\cos(kr)\,d\mu_*,\quad
 \partial_kR_N(t,k)=-\int r\tau_N(\alpha r^2)\sin(kr)\,d\mu_*.
 \tag{15}
\]

## 3. Quantitative absolute remainder and reconstruction

Iterating (7) and summing the resulting geometric series gives

\[
 T_N^{(q)}(t):=\sum_{j>N}B_j^{(q)}(t)
 \le\frac{B_{N+1}^{(q)}(t)}{1-Q_N(t)},\qquad q=0,2.
 \tag{16}
\]

The full tail measure in (15) is positive. Cauchy--Schwarz on that complete measure, equivalently on the disjoint count/radial space, gives

\[
 \int r\tau_N(\alpha r^2)\,d\mu_*
 \le\sqrt{T_N^{(0)}T_N^{(2)}}.
\]

Combining this with (15)--(16) proves the requested theorem: for every \(N\ge N_0\), all real \(k\), and every \(0\le t\le1/\gamma\),

\[
 \boxed{\ |R_N(t,k)|\le
 \frac{B_{N+1}^{(0)}(t)}{1-Q_N(t)},\qquad
 |\partial_kR_N(t,k)|\le
 \frac{\sqrt{B_{N+1}^{(0)}(t)B_{N+1}^{(2)}(t)}}{1-Q_N(t)}.\ }
 \tag{17}
\]

The bounds are absolute and uniform over real \(k\); no division by \(H\), \(H_k\) or a signed count trace occurs. All omitted counts are explicitly paid. Every retained signed term remains untouched.

Since \(d_0=H_\lambda(k)/h_*\), the finite reconstruction using the conserved initial full count sum is

\[
 \widehat H_{\lambda,N}(k)=H_{1/2}(k)-h_*\sum_{j=1}^Nd_j(t,k),
 \quad
 \widehat H_{\lambda,N}'(k)=H_{1/2}'(k)-h_*\sum_{j=1}^N\partial_kd_j(t,k).
 \tag{18}
\]

Equation (14) makes the exact errors \(H_\lambda-\widehat H_{\lambda,N}=-h_*R_N\) and \(H_\lambda'-\widehat H_{\lambda,N}'=-h_*\partial_kR_N\). Thus

\[
 |H_\lambda(k)-\widehat H_{\lambda,N}(k)|
 \le h_*\frac{B_{N+1}^{(0)}}{1-Q_N},\qquad
 |H_\lambda'(k)-\widehat H_{\lambda,N}'(k)|
 \le h_*\frac{\sqrt{B_{N+1}^{(0)}B_{N+1}^{(2)}}}{1-Q_N}.
 \tag{19}
\]

At \(\alpha=0\), the seeds in (17)--(19) vanish, \(Q_N=0\), and both reconstructions are exact. At \(\alpha=1\), \(\lambda=-1/2\) and all bounds remain valid. The first-derivative expression is analytical; it licenses no additional physical measurement. Equations (18)--(19) concern finite analytical reconstruction, not an assumed experimental protocol after nonzero counts.

## 4. Baseline, scope and local check

Direct scalar summation gives exactly the same omitted kernel: expand \(e^{\alpha r^2}\) against \(e^{\lambda r^2}\Phi(r)\) and retain the terms through count \(N\). The omitted value and derivative are precisely the two integrals in (15), with the same moment ratios (4) and bounds (17)--(19). No computational or physical estimating advantage is claimed over that scalar baseline.

The canonical-tail input enters the new eventual ratio through Note06's accepted second centered moment. The recorded reflected control lacks that exact canonical tail; no version of (6) is transferred to it without a separately paid estimate. Its generic Poisson/count reconstruction identities still hold with its own normalization and finite initial moments, including its recorded colliding event. None of the present identities or absolute bounds supplies a relative margin at zeros/collisions, a sign theorem for the omitted tail, collision exclusion, all-height relative control, a signed three-particle Mellin estimate or novelty.

The full cylinder spectrum, both angular signs, every shell, complete radial line/source tails, literal real cosine, supplied loader/access, fixed clock and absolute calibration remain unchanged. Finite-count Schwartz/graph payments are inherited from Note06/E01; uniform scalar count summability here is not a uniform graph-norm or energy assertion in \(j\). Nonzero-count physical readout access is unassumed. Read with the existing [result index][results], [control cluster][controls] and [patterns index][avoid], especially [normalization][a08] and [scoped exclusions][a07].

The single local check verified the \(j+1\) shift for \(q=2\), the factorial denominators, the explicit decreasing envelope and finite threshold, seed indexing, \(\alpha=0\) without ratios, \(\alpha=1\), uniform real-\(k\) domination, the complete count/radial Cauchy--Schwarz payment, and the sign and factor \(h_*\) in reconstruction. No mathematical correction, source change or scope expansion was needed. All six frozen inputs remained unchanged. This completes r1 at proof-author level; **E07 — separate Sol/ultra internal assessment** is the declared next gate. No successor question is selected here.

[request]: ../research-progress/handoffs/10_TND_D_E06_R1_REQUEST_20261106.md
[inputs]: ../research-progress/handoffs/10_TND_D_E06_R1_INPUTS_20261106.json
[note06]: 06_TND_D_E03_HIGH_COUNT_LOCALIZATION_20261106.md
[review03]: ../reviews/03_TND_D_E04_HIGH_COUNT_ASSESSMENT_20261106.md
[e01]: 02_TND_D_E01_R1_CONDITIONAL_QUADRATURE_REALIZATION_20261106.md
[count]: ../manuscript/sections/05_count_calculus.tex
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a08]: ../../../../../avoid/08_normalization_and_constant_slips.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md

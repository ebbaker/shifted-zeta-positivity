# The contraction margin at the first horizon: the elementary assembly validated end to end

**Author: Claude Fable 5.1 (Anthropic), model `claude-fable-5-1`.** 17 September
2026 (New York). Second note of the Loewner investigation, carrying out the first
half of item 1 of the [opening note's](MARKOV_PART_AND_REALIZATIONS_20260917.md)
plan: assemble the compressed transfer $V_{\omega,L}$ from the elementary kernel
of the Markov decomposition, with no $\xi$ and no zeros, and measure its
contraction data against the localized Weil form. The programme is
[`contraction_margin.py`](../numerics/exploratory/contraction_margin.py)
(unregistered, `mpmath`); every number below has a record beside it.

**Nothing here is a positivity statement. The horizon is $L=\log3$, where the
margin $m_L$ is known and positive; the computation tests the assembly, not the
zeros.**

---

## 0. Summary

1. **The assembly is right.** In the orthonormal sine basis on $I_L$, with
   $L=\log3$ and $N=24$, the compressed transfer built from
   $k_\omega=\widehat k_\omega-2\,\mathrm{EMA}_b[\widehat k_\omega]$ is a strict
   contraction, $\lVert V_{\omega,L}\rVert=1-1.25\times10^{-10}$ at
   $\omega=0.002$ and $1-6.61\times10^{-9}$ at $\omega=0.1$, and the smallest
   eigenvalue of the defect $D_{\omega,L}=I-V^*V$ satisfies
   $\lambda_{\min}(D_{\omega,L})/2\omega=m_L^{(N)}\,(1+\delta)$ with
   $\delta=-0.3\%$ at $\omega=0.002$, $+0.1\%$ at $\omega=0.01$, $+2.8\%$ at
   $\omega=0.05$ and $+5.8\%$ at $\omega=0.1$, where $m_L^{(N)}$ is the margin of
   the Weil form in the same basis. The transfer side and the form side of the
   Wilson-lines investigation, assembled from different presentations of the
   explicit formula, agree at first order in $\omega$ (Section 3).
2. **The deviations are accounted for.** On the exact compression the defect
   expands as $D_{\omega,L}=2\omega Q_{0,L}-\omega^2\big(2Q_{0,L}^2+[Q_{0,L},A_{0,L}]\big)+O(\omega^3)$,
   and on the minimizer of $Q_{0,L}$ the commutator term vanishes, so
   $\lambda_{\min}(D_{\omega,L})/2\omega=m_L-\omega m_L^2+O(\omega^2)$
   (Proposition 2.1). The positive excess seen in the Galerkin computation is a
   truncation term $\frac\omega2\lVert(I-P_N)A_{0,L}f\rVert^2$ of first order in
   $\omega$ (Proposition 2.2); it falls from $5.8\%$ to $3.8\%$ to $2.0\%$ when
   the defect is computed nested in $N'=24,40,64$ modes at $\omega=0.1$, roughly
   like $1/N'$, and what is left is quadratic in $\omega$ with a coefficient of
   order unity relative to $m_L$ --- far below the a-priori
   $O(\omega^2\kappa_L^2)$ with $\kappa_{\log3}=61$ (Table 3.3).
3. **The mass is right too, by an independent route.** The first-order tail
   $\lim_{\omega\to0}\omega^{-1}\int_L^\infty k_\omega$ has a closed form from
   the log-derivative of $\xi$ (poles, digamma, primes; no zeros), equal to
   $0.630516$ at $L=\log3$; the assembled masses extrapolate to $0.63052$
   (Proposition 2.3, Table 3.4).
4. **Numerical lessons** for the registered version: the kernel must be
   evaluated in the local coordinate of each atom (the spike at
   $\tau\sim10^{-100}$ is lost to cancellation otherwise); a double-exponential
   rule after the substitution $\tau=u^{1/\omega}$ with step $1/h\geq16$ resolves
   $\lambda_{\min}(D)$ to about $6\times10^{-12}$, and $1/h=20$ to below
   $10^{-12}$; an atom within $\epsilon$ of the horizon carries
   $\sim\epsilon^\omega$ of its spike mass yet contributes nothing to the
   operator (Section 5).
5. **What remains of plan item 1:** a standard-library version at $L=\log3$
   (the only recorded horizon where $2\omega m_L$ is resolvable in double
   precision), the cumulative Cayley coordinate, and the phase-matched Gram
   control on the contraction side (Section 6).

---

## 1. What was computed

### 1.1 The Galerkin matrix

$V_{\omega,L}=P_L\mathcal V_\omega P_L$ is the causal convolution with
$k_\omega$ compressed to $L^2(I_L)$, $I_L=(-\frac L2,\frac L2)$. In the
orthonormal sine basis $e_j(x)=\sqrt{2/L}\,\sin\big(j\pi(x+\frac L2)/L\big)$,
$j=1,\dots,N$,
\[
 V_{jk}=\langle e_j,V_{\omega,L}e_k\rangle=\int_0^L k_\omega(t)\,S_{jk}(t)\,dt,\qquad
 S_{jk}(t)=\int_{-L/2+t}^{L/2}e_j(x)\,e_k(x-t)\,dx ,
\]
and the one-sided autocorrelations $S_{jk}$ are elementary: with
$\alpha=\pi/L$ and $\sigma=(-1)^{j+k}$,
\[
 S_{jj}(t)=\frac{(L-t)\cos(j\alpha t)+\sin(j\alpha t)/(j\alpha)}{L},\qquad
 S_{jk}(t)=\frac1L\Big[\frac{\sigma\sin(k\alpha t)-\sin(j\alpha t)}{(j-k)\alpha}
 +\frac{\sigma\sin(k\alpha t)+\sin(j\alpha t)}{(j+k)\alpha}\Big]\quad(j\neq k),
\]
checked against direct quadrature to $1.1\times10^{-41}$ at 40 digits. The
integral over $t$ is the only quadrature in the programme. The defect is
$D_N=I-V_N^{\mathsf T}V_N$, its smallest eigenvalue and $\lVert V_N\rVert$ are
read from the symmetric eigenproblem of $V_N^{\mathsf T}V_N$, and the reference
$m_L^{(N)}$ is the smallest eigenvalue of the Weil form $Q_{0,L}$ in the same
basis, even block, from `weil_sine_basis.py` of the Wilson-lines exploratory
folder (closed form, no quadrature). $e_1$ is the first even mode and
$Q_{0,L}[e_1]=4.3474\times10^{-4}$ is read from the same matrix.

### 1.2 The kernel, in local coordinates

$k_\omega$ is assembled in the $R_\omega$-form of the inherited note,
\[
 k_\omega=\sum_{n<e^L}\widetilde c_n\,\kappa_\omega(\cdot-\log n),\qquad
 \kappa_\omega=k^\Gamma_\omega-4\omega b\,e^{-b\,\cdot}\mathbf 1_{>0}*k^\Gamma_\omega
 -4\omega a\,e^{a\,\cdot}\mathbf 1_{>0}*k^\Gamma_\omega ,
\]
with $k^\Gamma_\omega(x)=\frac{2\pi^\omega}{\Gamma(\omega)}(2\sinh x)^\omega n_\gamma(x)$,
$n_\gamma(x)=e^{-x/2}/(1-e^{-2x})$, and $\widetilde c_n=n^{\omega-1/2}\prod_{p\mid n}(1-p^{-2\omega})$.
At $L=\log3$ the atoms are $n=1,2$. On each interval $[\log n_0,\log n_1)$
between consecutive atoms the integrand is written in the local coordinate
$\tau=t-\log n_0$: the atom $n_0$ contributes $\widetilde c_{n_0}\kappa_\omega(\tau)$
exactly, and the earlier atoms $m<n_0$ contribute
$\widetilde c_m\kappa_\omega\big((\log n_0-\log m)+\tau\big)$. The point of the
local coordinate is the spike: $k^\Gamma_\omega(\tau)\sim\omega\,\pi^\omega2^\omega\tau^{\omega-1}$
near $\tau=0$ carries the fraction $(\pi^\omega 2^\omega)\epsilon^\omega$ of its
mass below $\tau=\epsilon$, so at $\omega=0.002$ half of the mass sits below
$\tau\approx2^{-500}$; forming $t=\log n_0+\tau$ in 40-digit arithmetic and
subtracting again destroys it, and the first version of the programme reported
$\lVert V\rVert>1$ for exactly this reason.

The singularity is removed by $\tau=u^{1/\omega}$, $d\tau=\omega^{-1}u^{1/\omega-1}du$,
after which the integrand is smooth on $(0,(\log n_1-\log n_0)^\omega]$ and a
tanh--sinh rule with nodes $u_k=\frac U2\big(1+\tanh(\frac\pi2\sinh kh)\big)$,
$|k|\leq 4.5/h$, is applied; nodes whose weight is below $10^{-45}$ are dropped.
With $1/h=16$ this is 262 kernel evaluations for the two intervals, about
40 seconds at 40 digits, the whole cost of a run. (The first version used
`mpmath`'s built-in node generators, whose degree conventions differ from the
documentation; the rule is now written out.)

### 1.3 What is compared

Three quantities, all in the same $N$-dimensional space: $\lVert V_N\rVert$,
which must be $<1$; $\lambda_{\min}(D_N)/2\omega$ against $m_L^{(N)}$, which is
the first-order law $\lVert f\rVert^2-\lVert V_{\omega,L}f\rVert^2=2\omega Q_{0,L}[f]+O(\omega^2)$
of the Wilson-lines manuscript at the minimizer; and the same law on the fixed
vector $e_1$, where $Q_{0,L}[e_1]$ is $7000$ times $m_L$ and the check is
insensitive to the noise floor. The mass $\int_0^L k_\omega$ is recorded as well
and is compared in Section 3.4 with a closed form.

---

## 2. What the numbers should be

### 2.1 The exact compression

Write $s=\frac12+p$, $g_\omega(p)=\frac{\xi'}{\xi}(s+\omega)+\frac{\xi'}{\xi}(s-\omega)$,
so that $\partial_\omega\log K_\omega=-g_\omega$ and $g_\omega$ is even in
$\omega$; $g_0(p)=2\frac{\xi'}{\xi}(\frac12+p)$. On $\Re p>b$ every function
below is the Laplace transform of a causal distribution, and
\[
 K_\omega=\exp\Big(-\int_0^\omega g_{\omega'}\,d\omega'\Big)=\exp\big(-\omega g_0+O(\omega^3)\big).
\]
Compression to $[0,L)$ is a homomorphism of the causal convolution algebra: for
causal $\mathcal A,\mathcal B$ and $f$ supported in $I_L$, $(I-P_L)\mathcal B f$
is supported to the right of $I_L$ and $\mathcal A$ carries it further right,
so $P_L\mathcal A\mathcal B P_L=P_L\mathcal AP_L\cdot P_L\mathcal BP_L$. Hence
$V_{\omega,L}=\exp\big(-\omega G_{0,L}+O(\omega^3)\big)$ with $G_{0,L}=P_L\mathcal G_0P_L$
the compression of the kernel of $g_0$ --- the distribution
$g_0(t)=\big(2e^{-t/2}+2e^{t/2}\big)-\log\pi\,\delta-\mathrm{fp}[2n_\gamma]-2\sum_n\Lambda(n)n^{-1/2}\delta_{\log n}$
read off from $\frac{\xi'}{\xi}(s)=\frac1s+\frac1{s-1}-\frac12\log\pi+\frac12\psi(\frac s2)+\frac{\zeta'}{\zeta}(s)$
(the finite part is fixed in §2.3). Write $G_{0,L}=Q_{0,L}+A_{0,L}$ with
$Q_{0,L}=\frac12(G+G^*)$ the localized Weil form and $A_{0,L}=\frac12(G-G^*)$
skew: a Hilbert transform on the interval, the odd part of the comb (shifts by
$\pm\log n$), and smooth terms.

**Proposition 2.1 (defect to second order).** On the compression,
\[
 D_{\omega,L}=I-V_{\omega,L}^*V_{\omega,L}
 =2\omega\,Q_{0,L}-\omega^2\big(2Q_{0,L}^2+[Q_{0,L},A_{0,L}]\big)+O(\omega^3),
\]
and if $f$ is a normalized eigenvector of $Q_{0,L}$ with eigenvalue $m$ then
$\langle f,D_{\omega,L}f\rangle/2\omega=m-\omega m^2+O(\omega^2)$. In
particular $\lambda_{\min}(D_{\omega,L})/2\omega=m_L-\omega m_L^2+O(\omega^2)$:
the relative correction to the first-order law at the minimizer is
$-\omega m_L$, which at $L=\log3$ is $10^{-9}$ at $\omega=0.02$.

*Proof.* With $G=G_{0,L}$, $V=I-\omega G+\frac{\omega^2}2G^2+O(\omega^3)$ and
$V^*V=I-\omega(G+G^*)+\omega^2\big(G^*G+\tfrac12G^2+\tfrac12G^{*2}\big)+O(\omega^3)$.
Substituting $G=Q+A$: $G^*G=Q^2+QA-AQ-A^2$ and $\frac12(G^2+G^{*2})=Q^2+A^2$, so
the bracket is $2Q^2+[Q,A]$. For the eigenvector, $\langle f,[Q,A]f\rangle=\langle Qf,Af\rangle-\langle A^*f,Qf\rangle=2\,\mathrm{Re}\langle Qf,Af\rangle=2m\,\mathrm{Re}\langle f,Af\rangle=0$
since $A^*=-A$, and $\langle f,Q^2f\rangle=m^2$. The eigenvalue statement is
first-order perturbation theory for the simple lowest eigenvalue of $Q_{0,L}$
(the form is $\log|D|$-like on the interval: bounded below, unbounded above,
with compact resolvent, so its bottom is an eigenvalue, taken simple as the
computations show), whose eigenvector is smooth on $\bar I_L$; the
expansions are of the matrix elements $\int_0^Lk_\omega(t)S(t)\,dt$ against
smooth $S$, which are analytic in $\omega$ (the spike integrates to
$\epsilon^\omega$ against constants). $\square$

The evenness of $g_\omega$ is the evenness of $Q_{\omega,L}$ in $\omega$ used in
the Wilson-lines notes; at the kernel level it reads
$g_\omega(t)=2\cosh(\omega t)\,g^+(t)$ with $g^+$ the kernel of
$\frac{\xi'}{\xi}(\frac12+p)$, since a shift of $p$ is a multiplication of the
kernel by an exponential.

### 2.2 The Galerkin defect

**Proposition 2.2 (truncation terms).** Let $E_N$ be the span of the first $N$
basis functions, $P_N$ its projection, $V_N=P_NV_{\omega,L}P_N$ the Galerkin
block, $f_N$ the normalized minimizer of $Q_{0,L}$ on $E_N$ with eigenvalue
$m_L^{(N)}$. Then
\[
 D_N:=I_N-V_N^{\mathsf T}V_N=P_N D_{\omega,L}P_N+P_NV^*(I-P_N)VP_N\ \geq\ P_ND_{\omega,L}P_N ,
\]
and
\[
 \frac{\langle f_N,D_Nf_N\rangle}{2\omega}
 =m_L^{(N)}-\omega\big(m_L^{(N)}\big)^2
 +\frac\omega2\Big(\lVert(I-P_N)A_{0,L}f_N\rVert^2-\lVert(I-P_N)Q_{0,L}f_N\rVert^2\Big)+O(\omega^2).
\]
If instead the defect is computed nested in $E_{N'}\supset E_N$,
$D_{N\subset N'}:=I_N-\big(V_{N'}^{\mathsf T}V_{N'}\big)_{N\times N}=P_N(I-V^*P_{N'}V)P_N$,
the term $\frac\omega2\lVert(I-P_N)G f_N\rVert^2$ is replaced by
$\frac\omega2\lVert(I-P_{N'})Gf_N\rVert^2$ and the first-order coefficient tends,
as $N'\to\infty$, to
$-\big(m_L^{(N)}\big)^2-\lVert(I-P_N)Qf_N\rVert^2-\langle(I-P_N)Qf_N,(I-P_N)Af_N\rangle$,
which vanishes up to $-m_L^2$ as $f_N$ converges to the true minimizer.

*Proof.* $V_N^{\mathsf T}V_N=P_NV^*P_NVP_N$ and $P_N\leq I$ give the inequality
and the identity. Expanding $V=I-\omega G+\dots$ on $f_N\in E_N$,
$(I-P_N)Vf_N=-\omega(I-P_N)Gf_N+O(\omega^2)$, so the extra term is
$\omega^2\lVert(I-P_N)Gf_N\rVert^2+O(\omega^3)$; and in Proposition 2.1
evaluated on $f_N$, $Qf_N=m_L^{(N)}f_N+(I-P_N)Qf_N$ splits
$\lVert Qf_N\rVert^2=(m_L^{(N)})^2+\lVert(I-P_N)Qf_N\rVert^2$ and
$\langle Qf_N,Af_N\rangle=\langle(I-P_N)Qf_N,(I-P_N)Af_N\rangle$. Collecting
with $\lVert(I-P_N)(Q+A)f_N\rVert^2$ expanded gives the display. $\square$

So the Galerkin computation must show a *positive* first-order excess over
$m_L^{(N)}$, dominated by the sine-tail energy of $A_{0,L}f_N$ --- a function with
logarithmic endpoint singularities from the Hilbert transform and non-zero
endpoint values from the shifted copies, whose sine coefficients decay like
$1/n$, so the excess should fall like $1/N'$ under nesting. Both predictions
are what Table 3.3 shows.

### 2.3 The first-order tail

**Proposition 2.3 (mass beyond the horizon).** For $L>0$, integrating over
$[0,L)$ (atoms at $\log n=L$ excluded),
\[
 \lim_{\omega\to0}\frac1\omega\int_L^\infty k_\omega(t)\,dt
 =8\sinh\frac L2-2\sum_{n<e^L}\frac{\Lambda(n)}{\sqrt n}-\log2\pi-\gamma_E
 -\int_0^L\Big(2n_\gamma(u)-\frac1u\Big)du-\log L .
\]
At $L=\log3$ the five terms are $4.618802$, $-0.980258$, $-1.837877$,
$-0.577216$ and $-0.592935$, total $\mathbf{0.630516}$.

*Proof.* $\int_0^\infty k_\omega=K_\omega(0)=\xi(\frac12-\omega)/\xi(\frac12+\omega)=1$
for every $\omega$, so the tail is minus the head, and
$\partial_\omega\big|_0\int_0^Lk_\omega=\int_0^Lk_1$ with $k_1$ the kernel of
$-g_0(p)=-2\frac{\xi'}{\xi}(\frac12+p)$, namely
$k_1=-2e^{-t/2}-2e^{t/2}+\log\pi\,\delta_0+\mathrm{fp}[2n_\gamma]+2\sum_n\Lambda(n)n^{-1/2}\delta_{\log n}$,
which off the atoms is the first-order kernel $2n_\gamma(t)-4\cosh\frac t2$ of
the inherited note. The finite part is the distribution whose Laplace transform
is $-\psi(\frac14+\frac p2)=\int_0^\infty\big(\frac{2e^{-u/2}e^{-pu}}{1-e^{-2u}}-\frac{e^{-2u}}u\big)du$,
i.e. $\langle\mathrm{fp}[2n_\gamma],\phi\rangle=\lim_{\epsilon\to0}\big[\int_\epsilon^\infty2n_\gamma\phi-\phi(0)E_1(2\epsilon)\big]$,
and with $\phi=\mathbf 1_{[0,L)}$ and $E_1(x)=-\gamma_E-\log x+O(x)$ this is
$\gamma_E+\log2+\int_0^L(2n_\gamma-\frac1u)\,du+\log L$. The pole terms
integrate to $-8\sinh\frac L2$, the constant to $\log\pi$, the comb to
$2\sum_{n<e^L}\Lambda(n)n^{-1/2}$. $\square$

This is a check of the mass of the assembled kernel that uses only the
log-derivative of $\xi$ and no zeros --- the same data as the kernel, in a
different arrangement (the pole and digamma terms are here integrated
directly, where the kernel carries them through the Beta convolution and the
$R_\omega$ correction).

---

## 3. Results

All runs: $L=\log3$ exactly, atoms $n\in\{1,2\}$, 40 digits, tanh--sinh step
$1/h=16$ unless stated, records
[`cm_om*_log3_*.json`](../numerics/exploratory/README.md). $m_L^{(24)}=6.24751\times10^{-8}$,
$m_L^{(32)}=6.21505\times10^{-8}$, $m_L^{(16)}=6.84655\times10^{-8}$ (even
block); the converged value from the Wilson-lines notes is $5.66\times10^{-8}$
(recorded $5.54\times10^{-8}$), so the sine basis is far from converged at
these $N$ and every comparison below is *within a basis*, which is the
comparison Proposition 2.2 is about.

### 3.1 The $\omega$-sweep at $N=24$

| $\omega$ | $1-\lVert V_N\rVert$ | $\lambda_{\min}(D_N)$ | $\lambda_{\min}(D_N)/2\omega$ | ratio to $m_L^{(24)}$ | $e_1$: $(1-\lVert P_NVe_1\rVert^2)/2\omega\,Q[e_1]$ |
|---|---|---|---|---|---|
| 0.002 ($1/h=20$) | $1.2460\times10^{-10}$ | $2.49192\times10^{-10}$ | $6.22980\times10^{-8}$ | 0.99717 | 0.99883 |
| 0.01 | $6.2543\times10^{-10}$ | $1.25087\times10^{-9}$ | $6.25435\times10^{-8}$ | 1.00109 | 0.99465 |
| 0.02 | $1.2606\times10^{-9}$ | $2.52117\times10^{-9}$ | $6.30292\times10^{-8}$ | 1.00887 | 0.99057 |
| 0.05 | $3.2101\times10^{-9}$ | $6.42021\times10^{-9}$ | $6.42021\times10^{-8}$ | 1.02764 | 0.98581 |
| 0.1 | $6.6085\times10^{-9}$ | $1.32171\times10^{-8}$ | $6.60854\times10^{-8}$ | 1.05779 | 1.00203 |

$V_N$ is a contraction at every $\omega$, with $1-\lVert V_N\rVert=\frac12\lambda_{\min}(D_N)$
to all printed digits, as it must be for $\lambda_{\min}(D)\ll1$; and
$\lambda_{\min}(D_N)/2\omega\to m_L^{(24)}$ as $\omega\to0$. The excess over 1
at $\omega\geq0.02$ is close to linear in $\omega$ (slopes $0.44,0.55,0.58$),
the Galerkin term of Proposition 2.2. On $e_1$, which is not an eigenvector,
the first-order correction is genuinely of order $\omega$
($-\omega(\lVert Qe_1\rVert^2+\langle Qe_1,Ae_1\rangle)/Q[e_1]$ plus the
truncation term); the ratio is $1-0.6\,\omega$ for small $\omega$.

### 3.2 The quadrature step

| $\omega$ | $1/h$ | nodes | $\lambda_{\min}(D_N)$ | ratio to $m_L^{(24)}$ |
|---|---|---|---|---|
| 0.002 | 12 | 198 | (not recorded) | 9.6 |
| 0.002 | 16 | 262 | $2.43670\times10^{-10}$ | 0.97507 |
| 0.002 | 20 | 328 | $2.49192\times10^{-10}$ | 0.99717 |
| 0.01 | 16 | 262 | $1.25087\times10^{-9}$ | 1.00109 |
| 0.01 ($N=32$) | 16 | 262 | $1.23678\times10^{-9}$ | 0.99499 |

The step-12 run at $\omega=0.002$ was the run that exposed the noise floor: its
$\lambda_{\min}(D)$ was an order of magnitude too large. The floor at $1/h=16$
is about $6\times10^{-12}$ in $\lambda_{\min}(D)$ (it is $2.5\%$ of
$2.4\times10^{-10}$ at $\omega=0.002$ and $\pm0.5\%$ of $1.25\times10^{-9}$ at
$\omega=0.01$, the two $N$ giving deviations of opposite sign), and about
$7\times10^{-13}$ at $1/h=20$. Every deviation in the table is below $0.5\%$
once the floor is below the signal. The mass $\int_0^Lk_\omega$ agrees between
$1/h=16$ and $20$ to $10^{-15}$, so the floor is in the oscillatory matrix
elements, not the mass.

### 3.3 Basis size and the nested defect

At $\omega=0.1$, where the floor is $0.05\%$ of the signal:

| $N$ | $N'$ (nested) | $\lambda_{\min}/2\omega$ | ratio to $m_L^{(N)}$ | excess |
|---|---|---|---|---|
| 16 | -- | $7.29211\times10^{-8}$ | 1.06508 | 6.5\% |
| 24 | -- | $6.60854\times10^{-8}$ | 1.05779 | 5.8\% |
| 32 | -- | $6.49723\times10^{-8}$ | 1.04540 | 4.5\% |
| 24 | 40 | $6.48443\times10^{-8}$ | 1.03792 | 3.8\% |
| 24 | 64 | $6.37466\times10^{-8}$ | 1.02035 | 2.0\% |

and at $\omega=0.05$: plain $N=24$ excess $2.76\%$, nested in $N'=64$ excess
$0.61\%$. The excess is positive, decreases with $N$ and, under nesting, falls
as $5.8\to3.8\to2.0\%$ for $N'=24,40,64$, against $5.8\times24/N'=5.8,3.5,2.2\%$
for a $1/N'$ law: the sine-tail energy of $A_{0,L}f_N$, as Proposition 2.2
predicts. Fitting the nested-64 excesses at $\omega=0.05,0.1$ to
$\alpha\omega+\beta\omega^2$ gives $\alpha\approx0.04$, $\beta\approx1.6$: the
linear artefact is essentially gone at $N'=64$ and the remainder is
$\lambda_{\min}(D)/2\omega\approx m_L(1+1.6\,\omega^2)$, a second-order
coefficient of order unity relative to $m_L$ where the a-priori bound allows
$\kappa_L^2\approx3.7\times10^3$. The same trend on $e_1$: its ratio at
$\omega=0.1$ is $1.0273,1.0020,0.9876$ for $N=16,24,32$, crossing below 1 as
the truncation term dies and the genuine $-\omega(\dots)$ term remains.

### 3.4 The mass

| $\omega$ | $\int_0^Lk_\omega$ | $(1-\int_0^Lk_\omega)/\omega$ |
|---|---|---|
| 0.002 | 0.9987404683 | 0.629766 |
| 0.01 | 0.9937323187 | 0.626768 |
| 0.02 | 0.9875394433 | 0.623028 |
| 0.05 | 0.9694073969 | 0.611852 |
| 0.1 | 0.9406626582 | 0.593373 |

Linear extrapolation of the first two rows to $\omega=0$ gives $0.63052$;
Proposition 2.3 gives $0.630516$. The assembled kernel --- Beta convolution,
comb, two exponential smoothings, local coordinates, substitution, tanh--sinh
--- has the right mass to five digits at first order, by a formula that
integrates the poles, the digamma and the primes directly.

---

## 4. Reading

The elementary assembly of the opening note is validated end to end: the
kernel side ($k_\omega$ from $k^\Gamma_\omega$, $\widetilde c_n$ and $R_\omega$)
and the form side ($Q_{0,L}$ from the prime comb in closed form) agree at the
first-order law to the precision of the quadrature, their second-order
disagreement is the one Proposition 2.2 prescribes and dies as prescribed, and
the mass agrees with an independent closed form. There is now a working
instrument that computes $\lVert V_{\omega,L}\rVert$, $\lambda_{\min}(D_{\omega,L})$
and their $\omega$-dependence from the integers below $e^L$ and elementary
functions.

What the instrument says at $L=\log3$ is what the dichotomy says it must:
contraction, with margin $\omega m_L$ to first order and a positive
second-order correction. Nothing about the zeros is learned at one horizon
where $m_L>0$ is already known; the dichotomy (Wilson-lines manuscript,
Proposition 7.2) is about all horizons, and the margin at the recorded horizons
$\log5,\log7$ is $10^{-17},10^{-27}$, beyond what a double-precision registered
check can resolve and within what this instrument can at 40 digits, at a cost
that grows with the number of atoms ($4$ and $6$ intervals) rather than with
$L$.

Proposition 2.1 is worth keeping for its own sake: the defect of the
compressed all-pass is, to second order, $2\omega Q-\omega^2(2Q^2+[Q,A])$, so
the *only* first-order correction to the first-order law at the minimizer is
$-\omega m_L^2$, and the commutator of the Weil form with its skew partner ---
the compressed Hilbert transform of the interval --- is what governs the
second-order behaviour away from the minimizer. The evenness
$g_\omega(t)=2\cosh(\omega t)g^+(t)$ says the whole $\omega$-dependence of the
generator is one factor $\cosh(\omega t)$ on the Weil kernel.

---

## 5. Numerical lessons

Recorded so that the registered version does not rediscover them.

- **Local coordinates.** The spike $k^\Gamma_\omega(\tau)\sim\omega\pi^\omega2^\omega\tau^{\omega-1}$
  puts half its mass below $\tau=2^{-1/\omega}$. Any formulation that forms the
  global time $t=\log n_0+\tau$ and recovers $\tau$ by subtraction loses it at
  every finite precision; the kernel must be evaluated as a function of $\tau$.
  Symptom: $\lVert V\rVert>1$ by $10^{-3}$ and a first-order check off by a
  factor 100.
- **The substitution and the rule.** $\tau=u^{1/\omega}$ removes the
  singularity exactly; after it, a tanh--sinh rule with step $h$ converges
  doubly exponentially, but the step needed grows as $\omega$ shrinks (the
  transformed integrand varies over hundreds of decades in $\tau$). $1/h=16$
  gives a floor of $6\times10^{-12}$ in $\lambda_{\min}(D)$, $1/h=20$ below
  $10^{-12}$; $1/h=12$ is insufficient at $\omega\leq0.002$. Write the rule out;
  do not rely on a library's node generator without checking its mass.
- **Atoms at the horizon.** With $L$ entered as a decimal slightly above
  $\log3$, or with $L$ formed at default precision before the working precision
  is set, the atom $n=3$ enters with a sliver $[\log3,L)$ of length
  $10^{-17}$ and carries $\sim(10^{-17})^\omega$ of its spike mass --- $68\%$ of
  it at $\omega=0.01$. This changes $\int_0^Lk_\omega$ (to $1.0027$ from
  $0.9937$) but not the operator, because $S_{jk}(L)=0$ for every $j,k$; the
  record `cm_om0.01_log3_N16_h12_edgeatom_stale.json` is that run, kept as the
  example. Parse $L=\log n$ exactly, set the precision first, and take
  $\log n<L$ strictly.
- **Sign of the Galerkin bias.** $D_N\geq P_NDP_N$: the plain Galerkin defect
  overestimates, at first order in $\omega$, by the sine-tail energy of
  $A_{0,L}f_N$; the nested defect (Proposition 2.2) removes most of it at the
  cost of assembling $V$ at $N'$. Compare within a basis, never a Galerkin
  $\lambda_{\min}(D_N)$ against a converged $m_L$.
- **Cost.** The kernel evaluations dominate (262 evaluations, each a few
  `mpmath` quadratures for the two smoothings, about 40 s); the $N^2$ matrix
  elements are closed-form sums over the nodes and are cheap up to $N'=64$.

---

## 6. What remains of plan item 1, and next

1. **Registered version.** Standard library only: `math.gamma`, `math.sinh`,
   the substitution and the tanh--sinh rule are all elementary, and the
   eigenproblem of a $24\times24$ symmetric matrix can be written out (Jacobi).
   In double precision $\lambda_{\min}(D)\approx2\omega m_L$ is resolvable only
   at $L=\log3$ ($\approx10^{-9}$ against a floor of $10^{-14}$); the check
   should assert contraction, $\lambda_{\min}(D_N)/2\omega=m_L^{(N)}(1+\delta)$
   with $|\delta|<1\%$ at $\omega=0.01$, and the mass against Proposition 2.3.
   The horizons $\log5,\log7$ stay exploratory at 40 digits.
2. **The cumulative Cayley coordinate** of the Wilson-lines notes, from the
   same $V_N$ at a sequence of $\omega$.
3. **The phase-matched Gram control on the contraction side:** replace the
   comb in $Q_{0,L}$ by the Gram-lattice and half-shifted-lattice controls of
   the Wilson-lines review and compare their margins with $\lambda_{\min}(D)/2\omega$
   --- the transfer has no lattice analogue, so this control lives on the form
   side only, and the comparison measures what the transfer knows that a
   lattice does not.
4. **Then the rest of the opening note's plan** (Lax--Phillips dictionary at
   $\omega=\frac12$; the Beta law from a radial chain; the comb in the
   Bost--Connes algebra; the passivity statement), in that order.

---

## 7. Status of every statement

- **Written proof:** Propositions 2.1 and 2.2 (at the level of matrix elements
  against smooth test functions, with the analyticity in $\omega$ noted where
  it is used) and Proposition 2.3.
- **Labelled numerical computation (unregistered, mpmath, 40 digits):**
  Sections 3.1--3.4, every row with a record in `numerics/exploratory/`.
- **Reading:** the $1/N'$ law for the nested excess (two nestings; consistent,
  not established); the two-point fit $\alpha\omega+\beta\omega^2$ of §3.3.
- **Not claimed:** anything about the zeros, any horizon beyond $\log3$, or
  convergence of the sine basis, which is visibly incomplete at $N=32$.

See the [notes index](README.md) and the [investigation index](../README.md).

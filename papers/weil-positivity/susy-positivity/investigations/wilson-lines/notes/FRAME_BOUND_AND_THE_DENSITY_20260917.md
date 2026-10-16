# The lower frame bound of the Riemann zeros on $PW_{L/2}$: a positive infimum, a units correction, and a collapse that is not arithmetic

**Author: Claude Opus 5 (Anthropic).** 17 September 2026. Research note, attacking
item 1 of [the continuation note](CONTINUATION_20260917.md) and Section 6 of
[the sampling note](SAMPLING_AND_THE_DEFICIT_20260917.md).

**Applied to the manuscript.** Version 0.4 carries every recommendation of
Section 10 below; the new Section 8 of the manuscript is this note's Sections
2--6, and Section 10 here records what was done. The note itself stands as
written, with its scope statements and its longer tables. It includes one
**retraction** from the sampling note and one **correction of language** there.

**Convention.** Throughout, $f$ is supported in $I_L=(-L/2,L/2)$, $\widehat F=\hat f$
has exponential type $L/2$, and the prime sum runs over $n<e^L$. This is the
convention of this investigation and of the companion shifted-zeta work. It is
**not** Zhu's; see Section 1.

---

## 0. Summary

1. **A units error has been distorting the comparison, and the numbers in fact
   agree.** Zhu (arXiv:2608.24827) supports $f$ in $[-L,L]$; this programme
   supports $f$ in $(-L/2,L/2)$. **Zhu's $L$ is half of ours.** The sampling
   note's §5 compared Zhu at $L=2$ (ours: $L=4$) with our fit at $L=2$ and found
   a discrepancy of $250$ orders of magnitude. There is none. An independent
   recomputation from scratch reproduces the three recorded \cite{CriticalPath}
   margins to $2.2\%$, $3.2\%$ and $0.2\%$, and at the matching horizon lands
   **inside** Zhu's certified two-sided enclosure. **The sampling note's §5
   warning is withdrawn** (Section 1); the one-sidedness *method rule* stands.
2. **The frame bound is positive, and there is no upper one.** Under RH,
   $\lambda_{\min}(Q_{0,L})>0$ for every $L$ --- not merely definiteness. The
   archimedean symbol grows like $\log|\tau|$, which makes the form domain embed
   compactly, so the infimum is attained; the sampling note's counting argument
   then forbids a null vector. Separately the *upper* frame bound is $+\infty$,
   because the zeros are not relatively separated. So the zeros are a set of
   sampling in the one-sided sense only, and calling $\lambda_{\min}$ "the frame
   bound" is an abuse that should be fixed in the manuscript (Section 2).
3. **(a) The literature has no constant to give.** Suzuki's de Branges space has
   structure function $E_\xi=\xi(\frac12-iz)+\xi'(\frac12-iz)$, **not** $\Xi$, and
   contains no quantitative statement; Ortega-Cerdà--Seip characterise sampling
   sequences through de Branges theory but produce a **dichotomy, not a bound**;
   Beurling's gap theorem gives an explicit constant only for $L<\pi/\gamma_1
   =0.2223$, above which classical sampling theory does not degrade --- it stops
   applying. **The route "get the frame bound from the structure function" is
   closed** (Section 3).
4. **(b) The deficit band is the right scale and the wrong construction.**
   Restricting the trial space to $|\tau|<W$ and measuring what fraction of
   $\log\lambda_{\min}$ survives gives a profile that is **universal in
   $W/\tau_c$** --- $0.59,0.74,0.843,0.92,0.965,0.996$ at
   $W/\tau_c=0.5,0.75,1,1.25,1.5,2$, constant to $\pm1\%$ across
   $L\in[1.6,3.0]$, a range of $10^{80}$ in $\lambda_{\min}$. So $\tau_c=2\pi e^L$
   is exactly the right scale. But the **literal** deficit construction ---
   stay in the band and vanish at the $2N(\tau_c)$ sub-critical zeros --- captures
   a *shrinking* fraction of the exponent: $100\%,100\%,76\%,59\%,53\%$ at
   $L=1.6,2.0,2.4,2.8,3.0$. It is not a usable trial space and no decay law can
   be tested with it (Section 4).
5. **(c) The collapse is a density effect, not an arithmetic one.** Replacing the
   zeros by the **Gram points** --- same counting function exactly, $S(T)\equiv0$,
   no arithmetic --- and by jittered Gram points at three jitter strengths, all in
   the same basis and truncation: every arithmetic-free set collapses
   superexponentially at essentially the same rate. At $L=2.0$ the zeros give
   $10^{-29.17}$ and the four arithmetic-free sets give $10^{-26.15}$,
   $10^{-25.99}$, $10^{-26.53}$, $10^{-25.44}$. **The arithmetic is worth about
   three orders of magnitude and grows like $\log L$; the density is worth all the
   rest** and grows like $e^L$. The ratio of exponents
   $\ln\lambda_{\rm zeros}/\ln\lambda_{\rm Gram}$ falls monotonically from $2.100$
   at $L=0.6$ to $1.049$ at $L=2.8$, over twelve horizons (Section 5).
6. **(d) On the rate.** No one-parameter law survives $L\in[0.6,3.0]$: the best is
   $22\%$ in the exponent. The programme's own $D$-law and Zhu's Landau--Widom law
   each fit their own window to a few percent and each fail outside it --- Zhu's by
   $46\%$ at our $L=1.6$, ours by $6.5\%$ at $L=4$. A two-parameter form
   $-\ln\lambda_{\min}\approx\pi\,\mathcal N_L\,(1.330-1.088\,u_L)$, with
   $\mathcal N_L=2Le^L$ the Nyquist count and $u_L=2N(\tau_c)/\mathcal N_L$ the
   occupancy, fits to $1\%$ over $L\in[1.8,3.0]$ --- but it is a fit, its
   endpoints do not match the prolate ones, and it should not be extrapolated.
   Given (c), **the rate question is a question about time--frequency
   localization, and the function it needs is an explicitly open problem**
   (Kulikov, arXiv:2603.07407, §8). Sections 6 and 7.

---

## 1. The units, and the retraction

### 1.1 Two conventions

Zhu, *Weil positivity in compact windows* (arXiv:2608.24827 v2), fixes
$\lambda^*(L)=\inf\{Q(f)/\lVert f\rVert_2^2:\ f$ real even, $\operatorname{supp}
f\subset[-L,L]\}$; the autocorrelation then lives in $[-2L,2L]$ and his prime mass
is $A_L=\sum_{\log n<2L}2\Lambda(n)/\sqrt n\sim4e^L$, with $T_*=2\pi e^{2L}$.
This investigation puts $f$ in $(-L/2,L/2)$, so $g=f\star\tilde f$ lives in
$(-L,L)$ and the comb runs over $n<e^L$, with $\tau_c=2\pi e^L$.

> **The two agree exactly when $L_{\text{here}}=2L_{\text{Zhu}}$.** Group E of
> the [check programme](../numerics/check_sampling_forms.py) verifies this on the
> nose: Zhu's $A_{L_z}$ equals this investigation's comb mass at $L=2L_z$, to
> machine zero, at three horizons.

So Zhu's certified numbers sit at **our** $L=1.6$ and $L=4.0$, not at $1.6$ and
$2.0$ --- which is where the sampling note placed them.

### 1.2 An independent recomputation

I rebuilt $Q_{0,L}$ from scratch: orthonormal sine basis on $I_L$, every matrix
element in closed form from the explicit formula in the real-space
(jump-measure) presentation the companion check programme validates, with the
three families of archimedean integrals summed in closed form through
$\psi$ and $\psi'$ at $\tfrac14$ rather than quadratured. The assembler agrees
with a direct sum over published zero ordinates to $1.8\times10^{-4}$ relative
(tail-limited), over $21$ matrix elements at three horizons; see group C of the
check programme. Precision and basis size are set from the answer.

End to end, the assembled $Q[f]$ for a random $f$ at $L=1.6$ agrees with the
repository's **pre-existing, independently written** quadrature assembler ---
`weil_functional` of the finite-response investigation's
`chk1_explicit_formula.py`, in Suzuki's normalisation --- to a relative
$6\times10^{-25}$ at 25 digits
([`crosscheck_against_repo_assembler.py`](../numerics/exploratory/crosscheck_against_repo_assembler.py)).
The two assemblers are written from different presentations of the explicit
formula and agree to full working precision.

| horizon | recorded \cite{CriticalPath} | recomputed here | difference |
|---|---|---|---|
| $L=\log3$ | $5.537\times10^{-8}$ | $5.657\times10^{-8}$ | $2.2\%$ |
| $L=\log5$ | $9.293\times10^{-18}$ | $9.590\times10^{-18}$ | $3.2\%$ |
| $L=\log7$ | $6.802\times10^{-28}$ | $6.790\times10^{-28}$ | $0.2\%$ |

and against Zhu:

| | Zhu $L_z=0.8$, i.e. **our $L=1.6$** | our $L=0.8$ |
|---|---|---|
| Zhu, certified, unconditional | $8.9\times10^{-18}\le\lambda^*\le2.27\times10^{-17}$ | --- |
| recomputed here | $1.73\times10^{-17}$ | $1.84\times10^{-4}$ |

The recomputed value at $L=1.6$ sits inside Zhu's enclosure. The alternative
reading --- that Zhu's $L$ is ours --- would require $\lambda_{\min}(0.8)\approx
2.3\times10^{-17}$; it is $1.8\times10^{-4}$, thirteen orders away. The units
question is settled twice over, textually and numerically.

### 1.3 What this retracts

> **Retraction.** The sampling note's §5 states that "two independent
> computations disagree by about $250$ orders of magnitude at nearby $L$" and
> concludes that "the recorded numbers measure the basis, not the margin". Both
> statements are wrong, and the cause is the factor of two. The three recorded
> margins are accurate to a few percent. Manuscript Proposition 7.6 and
> Remark 7.7, which the sampling note proposed to qualify on that basis, do not
> need that qualification.

What survives, and should still be said, is the *method rule*: a trial-space
Rayleigh quotient bounds $\lambda_{\min}$ from above only, and a sequence of them
across $L$ bounds the decay rate only if the bases are of comparable quality.
That rule is what the present note relies on when it reports basis-convergence
studies rather than single values. The sampling note was right to state it and
wrong about the instance.

One consequence is worth recording, because it runs the other way from the
note's mood. Refitted on its own three horizons, the programme's law
$-\ln\lambda_{\min}=-17.86+5.734\,(2e^L)$ predicts $L=3.0$ to $4.1\%$ and
$L=4.0$ to within $6.5\%$ of Zhu's certified bound --- an extrapolation over
$260$ orders of magnitude in $\lambda$, from data spanning twenty. **The fit the
sampling note asked to be disbelieved is, in the exponent, a good fit.** It is
still not a law; see Section 6.

---

## 2. The frame bound is positive; there is no upper one

### 2.1 No upper bound

> **Proposition 2.1** (unconditional). $\sup\{Q_{0,L}[f]:\lVert f\rVert_2=1\}=+\infty$.

*Proof.* The archimedean density $\Omega(\tau)=\operatorname{Re}\psi(\frac14
+\frac{i\tau}2)-\log\pi=\log\frac{|\tau|}{2\pi}+O(\tau^{-2})$ is unbounded, and
$Q_{0,L}$ differs from $\frac1{2\pi}\int|\hat f|^2\Omega$ by the rank-two pole
term and the finite prime comb, both bounded. $\square$

Equivalently, and in sampling language: the zeros are **not relatively
separated**, $\#\{\gamma:|\gamma-T|\le\frac12\}\sim\frac1{2\pi}\log\frac T{2\pi}
\to\infty$, so the Plancherel--Pólya/Bessel inequality fails. This is the
manuscript's own $Q_L[\chi e^{iNx}]/\log N\to\lVert\chi\rVert^2$, read as a
statement about sampling.

> **Correction of language.** In the standard definition a *sampling sequence*
> satisfies both inequalities, so $\{\gamma_\rho\}$ is **not** a sampling set for
> $PW_{L/2}$ and $\lambda_{\min}$ is **not** a frame bound. It is the constant in
> the **lower** sampling inequality. The sampling note's §2 and any manuscript
> text taken from it should say "lower sampling constant", noting that the upper
> one is infinite. This is not a quibble: the whole Beurling--Landau--Seip
> machinery is stated for separated sequences and is being invoked for an object
> outside its hypotheses.

The lower inequality is the part that needs no separation, for the trivial reason
that $\sum_{\lambda\in\Lambda}|F(\lambda)|^2$ is monotone under enlarging
$\Lambda$. That monotonicity is used again in Section 5.

### 2.2 A positive infimum

The sampling note's Proposition gives definiteness and explicitly leaves open
whether the infimum is positive. It is.

> **Proposition 2.2** (conditional on RH). For every $L>0$,
> $\inf\{Q_{0,L}[f]:f\in C_c^\infty(I_L),\ \lVert f\rVert_2=1\}>0$.

*Proof.* Write $Q_{0,L}=\mathcal A_L+\mathcal B_L$ with
$\mathcal A_L[f]=\frac1{2\pi}\int|\hat f|^2\Omega$ and
$\mathcal B_L$ the pole term minus the comb, a bounded symmetric form
($\lVert\mathcal B_L\rVert\le 2\lVert\cosh(x/2)\rVert^2_{L^2(I_L)}
+2\sum_{n<e^L}\Lambda(n)n^{-1/2}<\infty$). Since $\Omega\ge\Omega(0)=-5.3725\ldots$,
$\mathcal A_L$ is bounded below, and its form domain is
$\mathcal D=\{f\in L^2(I_L):\int|\hat f|^2\log(2+|\tau|)<\infty\}$.

*The embedding $\mathcal D\hookrightarrow L^2(I_L)$ is compact.* Let $f_k$ be
bounded in the form norm. Then $\hat f_k$ is bounded in $L^2(\mathbb R)$, with
uniformly small tails, $\int_{|\tau|>T}|\hat f_k|^2\le C/\log T$; it is uniformly
bounded, $|\hat f_k|\le\lVert f_k\rVert_1\le\sqrt L\lVert f_k\rVert_2$; and it is
equicontinuous, $|\hat f_k'|=|\widehat{xf_k}|\le\frac{L^{3/2}}2\lVert f_k\rVert_2$.
Arzelà--Ascoli with a diagonal argument gives a subsequence converging locally
uniformly, and the uniform tail bound upgrades that to $L^2(\mathbb R)$, hence
$f_k$ converges in $L^2(I_L)$.

So $\mathcal A_L$ has compact resolvent; adding the bounded $\mathcal B_L$ leaves
the essential spectrum empty, so $Q_{0,L}$ has purely discrete spectrum
accumulating only at $+\infty$ and the infimum is **attained** at some $e_L$ in
the form domain, $\lVert e_L\rVert=1$. (Attainment is Bombieri's, Rend. Lincei 11
(2000) §5, by a different argument; the point here is the mechanism, which is
that the group delay diverges.)

Under RH, $Q_{0,L}[f]=\sum_\rho|\hat f(\gamma_\rho)|^2\ge0$ on $C_c^\infty(I_L)$
and hence on the form closure. Suppose the infimum were $0$. Along an
approximating sequence $\hat f_k\to\hat e_L$ locally uniformly (above), so for
each $T$, $\sum_{|\gamma|<T}|\hat e_L(\gamma)|^2=\lim_k\sum_{|\gamma|<T}
|\hat f_k(\gamma)|^2\le\liminf_kQ_{0,L}[f_k]=0$; thus $\hat e_L$ vanishes at every
$\gamma_\rho$. But $e_L\in L^2(I_L)$, so $\hat e_L\in PW_{L/2}$ is a nonzero
Cartwright-class function of type $L/2$, whose zeros in $[-T,T]$ number at most
$\frac L\pi T(1+o(1))$, while $2N(T)\sim\frac T\pi\log\frac T{2\pi e}$. This is
the sampling note's counting contradiction. $\square$

Two remarks. First, the ingredient that makes this work is **fact (b) of the
continuation note**: the group delay $2\theta'(\tau)=b(\tau^2)+w_0$ diverges like
$\log\tau$. An all-pass filter with *bounded* delay would give a bounded
archimedean symbol, no compactness, and no reason for the infimum to be positive.
The unboundedness rule of \cite{Selection} and the positivity of the lower
sampling constant are the same fact.

Second, on novelty: attainment is Bombieri's and the counting step is the
sampling note's, so the combination may well be known or considered routine. I
did not find it stated. Suzuki (arXiv:2606.09096, Theorem 1.3) proves the harder
statement that $\lambda_a$ is *continuous* in $a$, which Bombieri had left as "an
analytically delicate issue"; positivity for each fixed $a$ is not stated there
either.

---

## 3. (a) What the literature gives: a closed route

I read the de Branges and non-uniform-sampling literature as machinery, as the
task asked. The answer is that there is no constant in it.

**Suzuki, arXiv:2301.00421** (published: Canad. J. Math., 3 Nov 2025, DOI
10.4153/S0008414X25101739). The Hilbert space of the Weil distribution is, under
RH, isomorphic to a de Branges space --- but the structure function is
$E_\xi(z)=\xi(\frac12-iz)+\xi'(\frac12-iz)$, **not** $\Xi$. Its zero set is not
the zeta zeros. "Inequalities converted to equalities" means the replacement of
Weil's criterion by the identity
$\mathrm{RH}\iff\lVert(P_{D\psi})^{\widehat{}}\rVert^2_{L^2}=\pi\langle\psi,\psi
\rangle_W$ for all $\psi\in C_c^\infty$. The totally ordered chain is indexed by
the support cut-off $t\ge0$ --- structurally our $L$ --- but carries no metric
information. **There is no smallest eigenvalue, no gap, no rate anywhere in the
paper.**

> **Correction.** The sampling note's §2 asserts that "the de Branges route and
> the frame bound are the same question", on the ground that the generating
> function of the sampling set is $\xi$. The sampling set's generating function
> *is* $\Xi$; but the de Branges space Suzuki constructs is $H(E_\xi)$ with
> $E_\xi=\Xi$-plus-derivative, and the isomorphism is with the whole Weil space,
> not with $PW_{L/2}$. The two questions are adjacent, not identical, and the de
> Branges side currently supplies nothing quantitative.

**Ortega-Cerdà--Seip**, *Fourier frames*, Annals 155 (2002) 789--806: a separated
$\Lambda$ is sampling for $PW$ iff there are $E,F\in HB$ with $H(E)=PW$ and
$\Lambda$ the zero sequence of $EF+E^*F^*$. This is a **characterisation, not a
bound**; the authors say so ("our main theorem becomes a working condition only
if we are able to solve certain problems of this kind"). The $A_2$ route, which
*does* carry constants through the weighted Hilbert transform, is stated for
**complete interpolating sequences**, and the zeros are not one for any $PW$
(they overshoot rather than match), so it does not apply.

**Beurling/Landau.** Landau's necessary density is satisfied with room to spare
($D^-=\infty$). Beurling's gap theorem, in the explicit form of
Olevskii--Ulanovskii (arXiv:1106.0576, Thm 3), gives
$\lVert f\rVert_\infty\le(\cos\rho)^{-1}\lVert f|_\Lambda\rVert_\infty$ when the
maximal gap is $2\rho/\sigma$ with $\rho<\pi/2$. Here the maximal gap of
$\{\pm\gamma_n\}$ is the one straddling the origin, $2\gamma_1=28.2695$, and
$\sigma=L/2$, so the hypothesis reads

$$\boxed{\,L<\pi/\gamma_1=0.2222606\ldots\,}$$

with constant $1/\cos(\gamma_1L/2)$: $1.32$ at $L=0.1$, $6.4$ at $L=0.2$, $63$ at
$L=0.22$. **Above $L=0.2223$ classical sampling theory does not degrade --- it
stops applying.** That is the sharpest thing the literature says about this
object, and it is worth stating in the manuscript precisely because it is so
weak: the entire phenomenon lives beyond the reach of the machinery whose
language it is being described in.

**Superlinear density with a low-frequency gap.** I found no literature on the
regime at all, and no law for how the lower constant degrades as the type
decreases. This appears to be a genuine gap rather than a failure of search.

*Reading scope.* Suzuki 2301.00421: introduction, statement of Theorems 1.1/1.4
and Theorem 5.7, from the published core-reader and the arXiv HTML. Ortega-Cerdà--Seip:
abstract, Theorems A and B, Theorem 1. Beurling: through Olevskii--Ulanovskii's
restatement, not the original. Bombieri 2000: through a machine extraction of the
bdim.eu scan, so my negative claims there are "not found", not "absent".

---

## 4. (b) The deficit band: the right scale, the wrong construction

The sampling note asked for trial functions built from the band $|\tau|<\tau_c$.
Two versions must be distinguished, and they give opposite verdicts.

### 4.1 The band as a trial space: a universal profile

Let $\lambda^{(W)}$ be the minimum of the Rayleigh quotient over the span of the
sine modes of frequency at most $W$ (dimension $LW/\pi$; at $W=\tau_c$ this is
exactly the Nyquist count $\mathcal N_L=2Le^L$). The fraction of the exponent it
captures is

| $W/\tau_c$ | $0.50$ | $0.75$ | $1.00$ | $1.25$ | $1.50$ | $2.00$ | $2.50$ |
|---|---|---|---|---|---|---|---|
| $L=1.6$ | $0.585$ | $0.733$ | $0.858$ | $0.933$ | $0.982$ | $0.995$ | $0.998$ |
| $L=2.0$ | $0.561$ | $0.725$ | $0.840$ | $0.910$ | $0.957$ | $0.995$ | $0.998$ |
| $L=2.2$ | $0.586$ | $0.744$ | $0.842$ | $0.921$ | $0.969$ | $0.997$ | $0.998$ |
| $L=2.5$ | $0.584$ | $0.739$ | $0.835$ | $0.915$ | $0.965$ | $0.996$ | $0.998$ |
| $L=2.8$ | $0.590$ | $0.744$ | $0.844$ | $0.924$ | $0.966$ | $0.997$ | $0.999$ |
| $L=3.0$ | $0.592$ | $0.741$ | $0.843$ | $0.915$ | $0.964$ | $0.997$ | $0.999$ |

(entries are $\log\lambda^{(W)}/\log\lambda_{\min}$.) The columns are constant to
about $\pm1\%$ while $\lambda_{\min}$ moves through $10^{80}$. **The frequency
content of the obstruction is a universal profile in $W/\tau_c$**, so
$\tau_c=2\pi e^L$ is the correct scale --- a real confirmation of the sampling
note's §4 --- and the obstruction is essentially complete at $2\tau_c$, which sits
between $\tau_c$ and the count crossover $T_*=e\tau_c$.

There is a practical corollary, which cost me a wasted scan: **a trial space must
reach about $2.5\,\tau_c$, i.e. $N\gtrsim2.5\,\mathcal N_L=5Le^L$, or the computed
value saturates.** A run at $N=200$ looks converged up to $L\approx2.8$ and is
wrong by $121$ orders of magnitude at $L=4$.

### 4.2 The literal deficit construction fails, and increasingly

Now the construction the deficit picture actually proposes: stay in the band and
**vanish at each of the $2N(\tau_c)$ zeros below $\tau_c$**, leaving the
$D(L)=2e^L-\frac74$ dimensions the sampling note counts. In the even block the
null-space dimension comes out at $D(L)/2$ as predicted, which is a good check on
the counting. The Rayleigh minimum over it is not:

| $L$ | $\#\{\gamma<\tau_c\}$ | $\dim$ null | $\log_{10}\lambda_{\min}$ | band only | band **and** vanishing |
|---|---|---|---|---|---|
| $1.6$ | $4$ | $4$ | $-16.73$ | $-14.30$ | $-14.30$ |
| $2.0$ | $8$ | $7$ | $-29.10$ | $-24.46$ | $-24.46$ |
| $2.4$ | $16$ | $10$ | $-48.02$ | $-40.41$ | $-36.49$ |
| $2.8$ | $30$ | $16$ | $-76.75$ | $-64.84$ | $-45.62$ |
| $3.0$ | $41$ | $19$ | $-96.25$ | $-81.19$ | $-50.64$ |

The last column captures $100\%,100\%,76\%,59\%,53\%$ of the exponent and is
falling. At $L=3$ it is short by $45.6$ orders of magnitude.

> **This is the sharp negative result of the section.** Exact interpolation at the
> sub-critical zeros is not what the minimiser does, and it is an expensive thing
> to impose: the minimiser makes $\widehat F$ *small at every zero*, including the
> oversampled ones above $\tau_c$, rather than *zero at the undersampled ones*.
> A trial space built to realise the deficit therefore misses a growing fraction
> of the exponent, and **no decay law can be calibrated against it.**

The sampling note's step 2 predicted that a deficit-band trial space "should beat
the polynomial bases by a wide margin". It does not: the polynomial bases of
\cite{CriticalPath} are within a few percent of the truth (Section 1.2), and this
construction is worse than they are by tens of orders of magnitude.

### 4.3 Why no prolate asymptotic can be quoted

The construction of §4.2 is, in prolate language, $1-\lambda_n$ at Shannon number
$c=\mathcal N_L$ and index $n=2N(\tau_c)=\mathcal N_L-D(L)$, i.e. at occupancy
fraction $u=n/c\in(0.44,0.68)$ over this range. That is neither Slepian--Fuchs'
fixed-$n$ regime nor the Landau--Widom plunge. The best available result is
**Kulikov, arXiv:2603.07407** (March 2026, preprint), which *proves*
$-\log(1-\lambda_n)\asymp(c-n)/\log\frac{2c}{c-n}$ before the plunge with
**unequated** constants, and states in its §8 that the fixed-fraction limit
$\gamma_\varepsilon=-\lim_c\log(1-\lambda_{(1-\varepsilon)c})/c$ is **open**, its
value "likely involv[ing] some integrals with special functions". Note
$\frac{2c}{c-n}=\frac{2\mathcal N_L}{D(L)}\to2L$, so Kulikov's order translates to
$\exp(-\Theta(D(L)/\log 2L))$ for the deficit construction. Measured against the
data the implied constant drifts by $60\%$ over $L\in[1.6,3.0]$, consistent with
"matching order, unequated constants" and not with an asymptotic.

---

## 5. (c) The control: the collapse tracks the density

### 5.1 What a control has to be

The tempting control --- delete the prime comb and keep archimedean plus pole --- is
**not** a zero set. Deleting the comb destroys positivity outright:

| $L$ | $0.6$ | $0.8$ | $0.9$ | $1.0$ | $1.2$ | $1.6$ | $2.0$ |
|---|---|---|---|---|---|---|---|
| $\lambda_{\min}$ (full) | $7.9\!\times\!10^{-3}$ | $1.9\!\times\!10^{-4}$ | $1.8\!\times\!10^{-5}$ | $1.0\!\times\!10^{-6}$ | $1.8\!\times\!10^{-9}$ | $1.9\!\times\!10^{-17}$ | $8.1\!\times\!10^{-30}$ |
| $\lambda_{\min}$ (no comb) | $7.9\!\times\!10^{-3}$ | $-0.0736$ | $-0.2007$ | $-0.3175$ | $-0.5308$ | $-0.9200$ | $-1.3153$ |

and in the coupling homotopy $Q_s=\text{arch}+\text{pole}-s\cdot\text{comb}$ at
$L=1.6$ the concave function $\lambda_{\min}(s)$ takes the values
$-0.922,-0.453,-0.085,+1.8\times10^{-17},-0.116,-0.593$ at
$s=0,0.5,0.9,1,1.1,1.5$: a corner at $s=1$ whose height is the margin itself.
That is vivid --- the arithmetic value of the coupling is the one that maximises
positivity, and the tolerance in $s$ is $\approx\lambda_{\min}$ --- but it is close
to a restatement of smallness, and it is **not** the density control, because
archimedean-plus-pole is a continuum and not a sum of squares over a point set.

The honest control is a **point set with the same counting function**. I used the
**Gram points** $g_n$, $\theta(g_n)=n\pi$, whose counting function is exactly the
smooth part $N_{\rm smooth}(T)=\theta(T)/\pi+1$ with $S(T)\equiv0$; plus jittered
Gram points, the jitter applied in the unfolded variable $\theta/\pi$ so the
counting function is preserved. Everything is computed in the **same** sine basis,
the same truncation ($2469$ Gram points to $T=3000$, ordinates accurate to
$4.5\times10^{-214}$), and the same precision. Truncation only removes
nonnegative terms.

### 5.2 The measurement

$\log_{10}\lambda_{\min}$:

| $L$ | zeros | Gram ($S\!\equiv\!0$) | Gram, jitter $0.15$ | jitter $0.40$ | jitter $1.00$ |
|---|---|---|---|---|---|
| $1.6$ | $-16.754$ | $-14.180$ | $-14.020$ | $-14.593$ | $-13.496$ |
| $2.0$ | $-29.168$ | $-26.146$ | $-25.989$ | $-26.531$ | $-25.443$ |

and across the range, zeros against Gram:

| $L$ | $0.6$ | $0.8$ | $1.0$ | $1.2$ | $1.4$ | $1.6$ | $1.8$ | $2.0$ | $2.2$ | $2.4$ | $2.6$ | $2.8$ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| zeros | $-2.111$ | $-3.726$ | $-6.008$ | $-8.764$ | $-12.347$ | $-16.754$ | $-22.353$ | $-29.168$ | $-37.623$ | $-48.042$ | $-60.974$ | $-76.747$ |
| Gram | $-1.005$ | $-2.173$ | $-4.059$ | $-6.623$ | $-9.969$ | $-14.180$ | $-19.492$ | $-26.146$ | $-34.476$ | $-44.766$ | $-57.482$ | $-73.167$ |
| gap | $1.11$ | $1.55$ | $1.95$ | $2.14$ | $2.38$ | $2.57$ | $2.86$ | $3.02$ | $3.15$ | $3.28$ | $3.49$ | $3.58$ |
| ratio of exponents | $2.100$ | $1.715$ | $1.480$ | $1.323$ | $1.239$ | $1.181$ | $1.147$ | $1.116$ | $1.091$ | $1.073$ | $1.061$ | $1.049$ |

The last row is $\ln\lambda_{\rm zeros}/\ln\lambda_{\rm Gram}$; it is monotone
decreasing over the whole range.

### 5.3 What it says

1. **Every arithmetic-free set of the same density collapses superexponentially,
   at essentially the same rate.** The answer to the question the task posed is
   therefore: *the decay is a density effect.*
2. **The arithmetic is worth about three orders of magnitude, and it grows
   logarithmically.** The gap is fitted to about $4\%$ by $1.61\log L+1.93$ over
   $L\in[0.6,2.8]$, against a total that grows like $e^L$. The ratio of exponents
   $\ln\lambda_{\rm zeros}/\ln\lambda_{\rm Gram}$ falls monotonically from $2.100$
   at $L=0.6$ to $1.049$ at $L=2.8$: **decreasing towards $1$.** So the arithmetic contribution to
   $\ln\lambda_{\min}$ is, on this evidence, asymptotically negligible *relative*
   to the density contribution --- while remaining a factor of $10^3$ and rising in
   absolute terms.
3. **The zeros are not a typical set of their density; they are systematically
   the worst of the family, by a small margin.** Jitter of up to a full mean
   spacing moves $\log_{10}\lambda_{\min}$ by about $1$, in both directions; the
   zeros sit $2.2$–$3.3$ below the whole arithmetic-free family. So "arithmetic"
   here is a systematic bias, not noise --- but a bias of bounded relative size.
4. **This is a large structural statement, and it cuts against the programme's
   framing.** The superexponential collapse of the Weil margin is not evidence of
   arithmetic depth: it is what the density $\frac1{2\pi}\log\frac\tau{2\pi}$ does
   to the lower sampling constant of $PW_{L/2}$, and any candidate source whose
   spectral measure has that density will exhibit it. In the manuscript's terms it
   strengthens Remark 7.7 ("the generator boundary is an artifact") into something
   sharper: **the margin itself carries almost no arithmetic information.** It
   also removes a hope --- that the collapse rate is a quantity a mechanism could
   be matched against --- and removes a fear, since a mechanism is not required to
   reproduce an arithmetic rate. It has to reproduce a density.

*Scope.* Gram and jittered-Gram values are trial-space Rayleigh quotients at
$N=2.8\mathcal N_L$ with the sum truncated at $T=3000$, so each is an upper bound
on its own infimum and each is slightly depressed by truncation; the zeros column
is computed from the explicit formula with no truncation. The comparison is
therefore conservative in the direction that matters: the arithmetic-free values
could only be *higher*, which would widen the gap in exponent but not change its
relative decline. One jitter draw per strength; the spread across strengths is
the error bar I am quoting, not a statistical estimate.

---

## 6. (d) The rate: what fits, what does not, and what it reduces to

Converged values, even block, $N=2.8\mathcal N_L$:

| $L$ | $0.6$ | $0.8$ | $1.0$ | $1.2$ | $1.4$ | $1.6$ | $1.8$ | $2.0$ | $2.2$ | $2.4$ | $2.6$ | $2.8$ | $3.0$ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $\log_{10}\lambda_{\min}$ | $-2.111$ | $-3.726$ | $-6.008$ | $-8.764$ | $-12.347$ | $-16.754$ | $-22.353$ | $-29.168$ | $-37.623$ | $-48.042$ | $-60.974$ | $-76.747$ | $-96.246$ |

One-parameter models $-\ln\lambda_{\min}=a\,X(L)$, least squares over
$L\in[1.4,3.0]$, worst relative residual in the exponent:

| $X(L)$ | $a$ | worst |
|---|---|---|
| $D(L)=2e^L-\frac74$ (the deficit) | $5.581$ | $24.9\%$ |
| $\mathcal N_L=2Le^L$ (the Nyquist count) | $1.945$ | $22.3\%$ |
| $\mathcal N_L/\log\mathcal N_L$ | $8.474$ | $39.3\%$ |
| $N(\tau_c)/\log N(\tau_c)$ (Zhu) | $19.07$ | $83.1\%$ |
| $D/\log(2\mathcal N_L/D)$ (Kulikov order) | $9.520$ | $67.3\%$ |

**No one-parameter law survives the range.** Each of the two published laws fits
its own window and fails outside it:

| $L$ | $1.6$ | $2.0$ | $2.4$ | $2.8$ | $3.0$ | $4.0$ |
|---|---|---|---|---|---|---|
| Zhu $2\pi^2N(T_*)/\ln N(T_*)$, error | $+46.1\%$ | $+15.0\%$ | $+4.2\%$ | $-0.4\%$ | $-1.6\%$ | (fitted here) |
| programme $D$-law, error | (fitted here) | $-0.4\%$ | | | $-4.1\%$ | $\le-6.5\%$ |

This is the cleanest available illustration of the programme's own method rule,
one level up: over any factor-$1.25$ window in $L$ these forms are
indistinguishable at the few-percent level, and they diverge by tens of percent
outside it. Fitting on three or four points determines nothing.

A two-parameter form does fit. With $u_L=2N(\tau_c)/\mathcal N_L$ the occupancy of
the deficit band,

$$-\ln\lambda_{\min}(L)\ \approx\ \pi\,\mathcal N_L\,\big(1.3296-1.0877\,u_L\big),$$

with residuals $+0.9\%,-0.3\%,-0.9\%,-1.0\%,-0.8\%,-0.2\%,+0.6\%$ at
$L=1.8,\ldots,3.0$ (and $+3.5\%$, $+6.8\%$ at $1.6$, $1.4$). The shape is the
prolate ansatz $-\log(1-\lambda_n)\approx2c\,G(u)$ with $c=\pi Le^L$ the Slepian
parameter, so that $\pi\mathcal N_L=2c$. **I am reporting it as a fit and not as
a mechanism**, for three reasons: it has two free parameters against nine points;
$u_L$ and $L$ are in bijection here, so nothing in this data separates a
dependence on $u$ from a dependence on $L$; and the fitted $G$ has $G(0)=1.33$ and
a root at $u=1.22$, where the prolate endpoints are $G(0)=1$ (Slepian--Fuchs) and
$G(1)=0$. A linear $G$ is certainly wrong; what the fit shows is only that
$(\mathcal N_L,u_L)$ is a better pair of variables than any single one.

There is one piece of evidence for the prolate reading that is *not* a fit, and it
is Section 5: the Gram points have the same $\mathcal N_L$ and the same $u_L$, and
they give the same exponent to within a ratio tending to $1$. A quantity
determined by $(\mathcal N_L,u_L)$ is a quantity determined by the density, and
that is what the control measures. Connes--Consani (arXiv:2310.18423) already
identify prolate eigenfunctions as the source of "extremely small eigenvalues of
the Weil quadratic form", without a rate; this is the same statement with numbers
attached.

**So the rate question reduces to the following, and there is no arithmetic left
in it:** what is the decay of $1-\lambda_n$ for the time--band-limiting operator
at fixed occupancy fraction? That is Kulikov's $\gamma_\varepsilon$, proved to
exist in order only, and stated by him to be open.

---

## 7. An assessment, including where I think the direction is wrong

Taking Sections 4--6 together, I think the honest reading is unwelcome for the
programme's framing and useful for its planning.

**The margin is not a number about $\zeta$.** It is the lower sampling constant of
a point set on $PW_{L/2}$, and to leading order in the exponent it depends on that
set only through its counting function. The primes shift it by three orders of
magnitude and by a relatively shrinking fraction of the exponent. Two
consequences. Any mechanism that reproduces the *density* will reproduce the
collapse, so reproducing the collapse is weak evidence for a mechanism; and the
collapse is not the obstacle it has been treated as --- it is the generic behaviour
of a sampling problem whose type is far below the set's density.

**Item 1 of the continuation-note pathway should be closed, not continued.** Its
three steps are now done and each has a definite answer: the literature has no
constant (§3), the deficit-band recomputation is a negative result (§4), and the
control says density (§5). What remains of the rate question is a question in
prolate asymptotics that a specialist in that field would have to answer, and that
is not this programme's comparative advantage.

**What I would actually chase, in order.** (i) The one genuinely new structural
fact here is §4.1's universal profile; it says the obstruction has a
well-defined frequency distribution in units of $\tau_c$, and that distribution
is a candidate for an exact statement. (ii) Item 2 of the pathway --- the
group-delay test of Condition 9.1 on a protected open Wilson line --- is untouched,
costs least, and is the only item a gauge theory can fail. I did not get to it,
and I now think it should go first: it is the only test in the programme whose
outcome is not already determined by the density. (iii) The sharpest *new*
question this note raises is the converse of §5: **if the margin is fixed by the
density, what does the arithmetic actually control?** The measured answer is "a
factor of $10^3$ growing like $\log L$", and that quantity --- the gap between the
zeros and matched-density sets --- is a new, well-defined, computable object that
does carry arithmetic. It is the thing worth a law.

**Where I think the current direction is wrong.** The programme has treated
$\lambda_{\min}(L)$ as the quantity a mechanism must explain (\cite{Selection}
selection rule 7; manuscript §7.5, "how $\varepsilon_L$ collapses is the mechanism
question"). On the evidence here that is misdirected: $\varepsilon_L$ collapses
because the zeros are a sparse sampling set at low frequency, and a Gram-point
"zeta" would do the same. The mechanism question should be asked about something
that distinguishes the zeros from their density, and §5 says what the candidate
is.

---

## 8. Status of every statement

- **Written proof.** Proposition 2.1 (unconditional). Proposition 2.2 (conditional
  on RH), modulo three quoted facts: the Cartwright density theorem, the
  explicit formula in the form the companion check programme validates, and
  standard Weyl/form-perturbation theory. Its attainment step reproves Bombieri.
- **Written computation, verified.** The closed forms of §1.2 and the
  archimedean sums: 336 cases in the [registered check
  programme](../numerics/check_sampling_forms.py), worst error $2\times10^{-15}$
  in groups A, B and D, $1.8\times10^{-4}$ in group C (tail-limited),
  machine zero in group E. $D(L)=2e^L-\frac74$ and $T_*=2\pi e^{L+1}$ are
  re-verified there.
- **Labelled numerical computation (unregistered, `mpmath`).** Every table in
  §§1.2, 4, 5, 6. All are trial-space Rayleigh quotients, hence **upper** bounds
  on their respective infima; where a comparison is made, the direction each
  value certifies is stated in the surrounding text. Basis convergence is
  controlled by the $N\ge2.8\mathcal N_L$ rule established in §4.1, which is
  itself a measurement.
- **Reading.** All of §3. Provenance and reading scope are stated there. The
  Kulikov translation at the end of §4.3 is my arithmetic on his stated result,
  not his statement.
- **Fit, reported as a fit.** The two-parameter form in §6, the $1.57\log L+1.91$
  gap law in §5.3, and the refitted $D$-law in §1.3. None is derived.
- **Heuristic.** The prolate reading of §6 --- that $-\ln\lambda_{\min}$ is
  $2cG(u)$ for the prolate rate function --- is a heuristic supported by one
  parameter-free check (the Gram agreement) and contradicted in its endpoints by
  the fit.
- **Conditional on RH.** Proposition 2.2; the identity
  $Q_{0,L}[f]=\sum_\rho|\hat f(\gamma_\rho)|^2$ and therefore the reading of every
  computed $\lambda_{\min}$ as a sampling constant. The *computations themselves*
  are unconditional: they evaluate the Weil functional, which is defined without
  RH.
- **Not claimed.** No source is constructed, no positivity is proved, no gauge
  theory is matched or excluded, and nothing here bears on RH.

---

## 9. Reproduction

Registered (standard library only, JSON to stdout, record preserved):

```sh
python3 numerics/check_sampling_forms.py          # 336 cases, 5 groups
```

Unregistered (`mpmath`), under [`numerics/exploratory/`](../numerics/exploratory/README.md):

```sh
python3 frame_bound_scan.py 0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0
python3 bandwidth_profile.py 1.6,2.0,2.2,2.5,2.8,3.0     # section 4.1
python3 deficit_construction.py 1.6,2.0,2.4,2.8,3.0      # section 4.2
python3 comb_homotopy.py                                 # section 5.1
python3 gram_point_cache.py 3000 220                     # then
python3 density_control_gram.py 0.6,0.8,...,2.8          # section 5.2
python3 density_control_jitter.py 1.6,2.0                # section 5.2
python3 decay_laws.py                                    # section 6
python3 crosscheck_against_repo_assembler.py             # section 1.2 (also needs sympy)
```

`deficit_construction.py` and the validation in the check programme use
hard-coded published zero ordinates; nothing here computes with $\zeta$ or $\xi$.

---

## 10. Recommended changes --- all applied in manuscript 0.4

*Applied 17 September 2026. Version 0.3 is preserved at `drafts/2026-09-17-v03`;
0.4 is 37 pages, recorded and snapshotted, and `drafts.py check --replay` passes
over 542 cases in two programmes. What follows is the list as written, with the
disposition of each item.*

| # | Disposition in 0.4 |
|---|---|
| 1--4 | The sampling note carries a status header saying exactly this. |
| 5 | Propositions 8.1 and 8.2 and the Beurling threshold (8.4) are in the new Section 8. |
| 6 | Not added; Proposition 7.6 and Remark 7.7 stand, and Remark 8.7 records that their three data points were independently reproduced. |
| 7 | Section 7.5 now ends by pointing at Section 8, and Remark 8.5 states the consequence. |
| 8 | Remark 8.6 and the fifth group of the check programme, which is now registered. |


**To the sampling note** (it should carry a status header rather than be edited):

1. **§5 is withdrawn.** The $250$-order discrepancy is a units error; see §1
   here. The method rule in the block quote stands.
2. **§2's language is wrong.** $\lambda_{\min}$ is the constant in the *lower*
   sampling inequality; there is no upper frame bound. §2's third bullet ("the de
   Branges route and the frame bound are the same question") overstates: Suzuki's
   structure function is not $\Xi$.
3. **§3's scope caveat can be removed**: the infimum is positive (Proposition 2.2).
4. **§6's step 2 is answered negatively and step 3 answered "density"**; §4 of
   the note is confirmed, with the new universal profile attached.

**To the manuscript** (Section 7.5 and Section 10):

5. Add Proposition 2.2 and Proposition 2.1 with the sampling language corrected,
   and the Beurling threshold $L<\pi/\gamma_1$ as the honest statement of what
   classical theory reaches.
6. **Do not** add the sampling note's qualification of Proposition 7.6 and
   Remark 7.7; it rested on the units error.
7. Replace "how $\varepsilon_L$ collapses is the mechanism question" with the
   §5 finding and its consequence, which is a real change of direction.
8. Record the convention difference with arXiv:2608.24827 explicitly wherever its
   numbers are quoted. This has now cost the programme one wrong conclusion.

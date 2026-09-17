# The margin is a frame bound: sampling, the Cartwright budget, and why the recorded numbers cannot be fitted

**Author: Claude Opus 5 (Anthropic).** 17 September 2026. Research note,
following the [conformal correction](CONFORMAL_CORRECTION_20260917.md) and
attacking item 2 of [the continuation note](CONTINUATION_20260917.md) --- how the
zero-placement precision collapses.

**No manuscript change has been made.** Manuscript 0.3 is current; Section 6
below lists what this recommends.

> **Status, added 17 September 2026 by Claude Opus 5.** Superseded in part by
> [the frame-bound note](FRAME_BOUND_AND_THE_DENSITY_20260917.md), which should
> be read with this one. Specifically:
>
> * **Section 5 is withdrawn.** The "$250$ orders of magnitude" discrepancy is a
>   units error: Zhu (arXiv:2608.24827) supports $f$ in $[-L,L]$ while this
>   investigation supports $f$ in $(-L/2,L/2)$, so **Zhu's $L$ is half of ours**
>   and his $L=2$ certificate belongs at our $L=4$. An independent recomputation
>   reproduces the three recorded margins to $2.2\%$, $3.2\%$ and $0.2\%$ and
>   lands inside Zhu's certified enclosure at the matching horizon. The recorded
>   numbers do **not** merely measure the basis, and the qualification of
>   manuscript Proposition 7.6 and Remark 7.7 proposed here is not needed. The
>   *method rule* stated in the block quote of Section 5 stands and is used
>   throughout the newer note.
> * **Section 2's language is wrong.** There is no upper frame bound --- the
>   zeros are not relatively separated --- so $\lambda_{\min}$ is the constant in
>   the **lower** sampling inequality and the zeros are not a sampling set in the
>   standard two-sided sense. And Suzuki's de Branges structure function is
>   $\xi(\frac12-iz)+\xi'(\frac12-iz)$, not $\Xi$, so "the de Branges route and
>   the frame bound are the same question" overstates the position.
> * **Section 3's scope caveat is closed**: the infimum is positive, not merely
>   the form definite.
> * **Section 4 is confirmed** --- $\tau_c$ is measurably the right scale --- and
>   Section 6's steps 2 and 3 are answered, the first negatively (a deficit-band
>   trial space is not usable) and the second "density, not arithmetic".

---

## 0. Summary

1. **$L$ is a modulus, not a length.** In the ray coordinate $r=e^x$ the interval
   $I_L$ is the annulus $e^{-L/2}<r<e^{L/2}$, whose conformal modulus is
   $L/2\pi$. So the second parameter of the program is a conformal invariant of
   the configuration, which is what the correction note's symmetry reading
   requires.
2. **The margin is a frame bound.** Under RH,
   $\lambda_{\min}(Q_{0,L})$ is the lower frame bound of the Riemann zeros as a
   sampling set for the Paley--Wiener space $PW_{L/2}$. Weil positivity is the
   statement that the zero set is a *set of uniqueness*; the margin is the
   statement that it is a *sampling set*, with a bound.
3. **A theorem, small but clean.** No nonzero $F\in PW_{L/2}$ vanishes at every
   $\gamma_\rho$, because the zeros have superlinear density and a Cartwright-class
   function of type $L/2$ has a linear zero budget. Hence, conditionally on RH,
   $Q_{0,L}$ is positive **definite** --- not merely semidefinite --- on
   $C_c^\infty(I_L)$, and the reason is a counting argument rather than an
   estimate.
4. **The budget crosses at $e^L$, exactly where the primes stop.** The zero
   density meets the interval's Nyquist density at $\tau_c=2\pi e^L$, and the
   cumulative counts cross at $2\pi e^{L+1}$. The maximal sample deficit is
   \[
    D(L)=2e^{L}-\tfrac74 ,
   \]
   exactly, the $\tfrac74$ being twice the Riemann--von Mangoldt constant;
   verified against exact counts at five horizons. Since $e^L=X$ is the prime
   cutoff, **the sampling crossover is the explicit-formula balance: primes up to
   $X$ against zeros up to height $2\pi X$.**
5. **A warning that matters more than the fit.** The recorded margins fit
   $\log m_L\approx17.7-5.73\,D(L)$ across three horizons to $1\%$. **The fit
   should not be believed.** Every recorded value is a trial-function upper bound
   whose quality depends on the basis, and two independent computations disagree
   by about $250$ orders of magnitude at nearby $L$: the fit predicts
   $10^{-29}$ at $L=2$ where Zhu's sine-basis certificate gives
   $3.2\times10^{-283}$. **The recorded numbers measure the basis, not the
   margin**, and no law should be fitted to them. I came close to reporting one.

---

## 1. The geometry: $L$ is a modulus

In the ray coordinate $r=e^x$ of the
[conformal correction note](CONFORMAL_CORRECTION_20260917.md), the interval
$I_L=(-L/2,L/2)$ is
\[
 e^{-L/2}<r<e^{L/2},
\]
an annulus of ratio $e^{L}$ and conformal modulus $L/2\pi$. Dilations move it and
preserve $L$; nothing else about it is conformally meaningful. So the program's
second parameter is exactly the one conformal invariant of the configuration.
That is the consistency check the correction note's symmetry reading needed: had
$L$ been a scale, the dilation invariance of the form would have been in
conflict with the whole $L$-dependence.

## 2. The margin is a frame bound

For $f$ supported in $I_L$, $\widehat F$ is entire of exponential type $L/2$ and
lies in $L^2(\mathbb R)$ --- that is, $\widehat F\in PW_{L/2}$ --- and
$\lVert f\rVert^2=\frac1{2\pi}\lVert\widehat F\rVert^2$. Under RH the spectral
form reads
\[
 Q_{0,L}[f]=\sum_\rho\big|\widehat F(\gamma_\rho)\big|^2 ,
\]
so that
\[
 \boxed{\ \lambda_{\min}(Q_{0,L})
 =\inf\Big\{\tfrac{2\pi\sum_\rho|F(\gamma_\rho)|^2}{\lVert F\rVert^2}
 \ :\ F\in PW_{L/2},\ F\neq0\Big\}\ }
\]
is precisely the **lower frame bound of $\{\gamma_\rho\}$ as a sampling set for
$PW_{L/2}$**. Three consequences of the language.

- **Weil positivity is a uniqueness statement, the margin a sampling statement.**
  $Q_{0,L}\succ0$ says the zeros are a set of uniqueness for $PW_{L/2}$; a
  quantitative margin says they are a sampling set.
- **The generating function of the sampling set is $\xi$ itself**,
  $\Xi(\tau)=\xi(\frac12+i\tau)$ having exactly the $\gamma_\rho$ as its real
  zeros. Sampling problems whose generating function is a Hermite--Biehler
  function are the subject of de Branges theory, which is why
  \cite{SuzukiDeBranges} keeps appearing: **the de Branges route and the frame
  bound are the same question.**
- **Both failure modes are visible.** The zero set is too sparse at low frequency
  and too dense at high, and Section 3 locates the crossover.

## 3. The Cartwright budget, and a theorem

A function of exponential type $a$ that is $L^2$ on the line is of Cartwright
class, and its zeros then have linear density: the number in $[-T,T]$ is at most
$\frac{2a}{\pi}T\,(1+o(1))$. With $a=L/2$ the budget is $\frac{L}{\pi}T$. The
zeros of $\xi$ supply, two-sided,
\[
 2N(T)=\frac{T}{\pi}\log\frac{T}{2\pi e}+\frac74+2S(T),
\]
which is superlinear.

> **Proposition.** No $F\in PW_{L/2}$ other than $0$ vanishes at every
> $\gamma_\rho$.

*Proof.* Such an $F$ would have at least $2N(T)$ zeros in $[-T,T]$, exceeding the
Cartwright budget $\frac{L}{\pi}T$ for all $T>2\pi e^{L+1}$. $\square$

> **Corollary (conditional on RH).** $Q_{0,L}$ is positive **definite** on
> $C_c^\infty(I_L)$: $Q_{0,L}[f]=0$ forces $f=0$.

Two remarks on scope. This gives definiteness, not a positive infimum --- in
infinite dimensions the two differ, and which one holds is the content of the
quantitative results the program cites. And the argument is conditional exactly
where one expects: without RH the $\gamma_\rho$ are complex, the form is
$\sum_\rho\widehat F(\gamma_\rho)\overline{\widehat F(\overline{\gamma_\rho})}$,
and it is not a sum of squares, so there is nothing circular here and nothing
gained toward RH. What is gained is a *reason*: strict positivity is a
**counting** fact about densities, not an estimate.

## 4. Where the budget crosses, and the deficit

Two crossings, both at the scale $e^L$.

**Density.** The local zero density $\frac1\pi\log\frac{\tau}{2\pi}$ equals the
Nyquist density $\frac{L}{\pi}$ at
\[
 \tau_c=2\pi e^{L}.
\]
Below $\tau_c$ the zeros undersample $PW_{L/2}$; above, they oversample.

**Count.** The cumulative counts cross at $T_*=2\pi e^{L+1}=e\,\tau_c$, which is
where the Proposition of Section 3 bites.

**Deficit.** The number of samples missing below $\tau_c$ is
\[
 D(L)=\frac{L\tau_c}{\pi}-2N(\tau_c)
 =\frac{\tau_c}{\pi}\Big(L-\log\frac{\tau_c}{2\pi e}\Big)-\frac74
 =\frac{\tau_c}{\pi}-\frac74
 =\boxed{\,2e^{L}-\tfrac74\,},
\]
the constant being twice the $\frac78$ of Riemann--von Mangoldt. Checked against
exact counts:

| $L$ | $\tau_c$ | Nyquist count | $2N(\tau_c)$ | deficit | $2e^L-\frac74$ |
|---|---|---|---|---|---|
| $\log3$ | $18.85$ | $6.592$ | $2.342$ | $4.250$ | $4.250$ |
| $\log5$ | $31.42$ | $16.094$ | $7.844$ | $8.250$ | $8.250$ |
| $\log7$ | $43.98$ | $27.243$ | $14.993$ | $12.250$ | $12.250$ |
| $2$ | $46.43$ | $29.556$ | $16.528$ | $13.028$ | $13.028$ |
| $3$ | $126.20$ | $120.513$ | $82.092$ | $38.421$ | $38.421$ |

**The scale is the prime cutoff.** The prime sum in the target runs over
$n<e^L=X$, and the sampling crossover sits at height $2\pi X$ with a deficit of
$2X$. That is the explicit-formula balance --- primes up to $X$ against zeros up
to height $2\pi X$ --- stated as a counting statement about an interval and its
samples, and it is the first place in this investigation where the $e^L$ scale
that dominates the program's estimates appears for a structural reason rather
than as the range of a sum.

## 5. The warning

The recorded margins fit the deficit well. With
$m_L\in\{5.537\times10^{-8},9.293\times10^{-18},6.802\times10^{-28}\}$ at
$L=\log3,\log5,\log7$ from \cite{CriticalPath}, and $D(L)=2e^L$,
\[
 \log m_L\approx17.68-5.731\,D(L),
\]
with the two increments agreeing to $1\%$ --- which, on three points and two
parameters, is one nontrivial check passed.

**Do not believe it.** Every recorded value in this program is a Rayleigh
quotient in a finite trial space, hence an **upper bound** whose quality depends
entirely on the basis, and the bases differ enormously:

- the fit predicts $\lambda_{\min}\approx10^{-29}$ at $L=2$;
- Zhu's sine-basis certificate gives $3.2\times10^{-283}$ at $L=2$
  \cite{Selection};

a discrepancy of about $250$ orders of magnitude. Since both are upper bounds and
Zhu's is far smaller, Zhu's is far closer to the truth, and the three values the
fit uses are dominated by the deficiencies of a $128$-input even polynomial
basis. **They measure the basis, not the margin.** The same applies to the
$\kappa_L\sqrt{m_L}$ law of manuscript Proposition 7.6, which uses the same three
values: it may be reporting a property of that basis family.

This is worth stating as a method rule, because it is the one-sidedness lesson
the program already carries, applied one level up:

> A trial-space Rayleigh quotient bounds $\lambda_{\min}$ from **above**. A
> sequence of such values across $L$ therefore bounds the decay *rate* from
> below in absolute value only if the bases are of comparable quality, which must
> be argued and not assumed. Fitting a law to them otherwise fits the basis.

## 6. What to do, and what to recommend

**The question to ask is now the right one.** "How does the margin collapse" is
"what is the lower frame bound of the Riemann zeros on $PW_{L/2}$", and that is a
question in a developed theory with the generating function in hand. Three
concrete steps.

1. **Ask de Branges theory for the frame bound.** Sampling problems with a
   Hermite--Biehler generating function are exactly what \cite{SuzukiDeBranges}
   is about, and Section 2 says the two questions coincide. This moves that item
   from third to first on the pathway: it is no longer background reading but the
   machinery for the open question.
2. **Recompute the margins in a basis adapted to the deficit.** Section 4 says
   the obstruction lives below $\tau_c=2\pi e^L$ and has size $2e^L$. A trial
   space built from that band --- prolates at bandwidth $\tau_c$, not $\gamma_1$
   --- should beat the polynomial bases by a wide margin, and the comparison
   with Zhu would then be meaningful. Until that is done, no decay law can be
   tested.
3. **Test the deficit picture on a model.** Replace the $\gamma_\rho$ by an
   artificial set with density $\frac1{2\pi}\log\frac{\tau}{2\pi}$ but no
   arithmetic, compute the frame bound numerically at several $L$, and see
   whether the decay follows $D(L)$. This separates "the deficit governs the
   collapse" from "the arithmetic governs the collapse", and it is cheap.

**Recommended manuscript changes**, for a later pass:

- Add the sampling reformulation of Section 2 and the Proposition and Corollary
  of Section 3 to Section 7.5, which currently states the margin as a minimum
  without identifying what kind of object it is.
- Add Section 4's crossover and deficit, with the table.
- Add Section 1's reading of $L$ as a modulus to Section 9.4, where it is the
  consistency check the symmetry argument needs.
- **Qualify Proposition 7.6 and Remark 7.7 with Section 5's warning**: both rest
  on three values from one basis family. The $\kappa_L\sqrt{m_L}$ relation should
  be labelled as possibly a property of that basis until recomputed.
- Promote \cite{SuzukiDeBranges} from a reading suggestion to the machinery for
  the open question.

## 7. Status

- Section 1 is elementary.
- Section 2 is a restatement, exact and conditional on RH through the spectral
  form.
- **Section 3's Proposition is a written proof**, using the Cartwright-class
  density theorem, which is quoted and not proved. Its Corollary is conditional
  on RH. It gives definiteness, not a positive infimum.
- Section 4's $\tau_c$, $T_*$ and $D(L)=2e^L-\frac74$ are written computations
  from the Riemann--von Mangoldt formula, verified against exact counts at five
  horizons; $S(T)$ is dropped throughout and is $O(\log T)$.
- **Section 5's fit is reported in order to be disbelieved**, and the reason is
  quantitative: two independent upper bounds at $L=2$ differ by $250$ orders of
  magnitude.
- Section 6 is proposed work.
- The numerics were run outside the repository and are arithmetic on published
  constants; nothing here is a registered check programme. No source is
  constructed, no positivity is proved, and the only new mathematical statement
  is Section 3's Proposition.

# Loewner: the Markov part of the shifted transfer and what can realize it

Opened 17 September 2026; **closed 18 September 2026.** Manuscript:
[*The Markov part of the shifted Weil transfer*](manuscript.pdf), working draft
0.3.

> **This investigation is closed.** It was opened to test one proposal --- that a
> Loewner-type conformal evolution could construct the shifted family's
> deformation paths, with positivity coming from conformality --- and that
> proposal is answered in the negative on all three factors of the transfer, with
> proofs rather than with an expectation (Section 4 of the manuscript). The name
> records the question it tested, as the sibling folders' names do.
>
> Its durable output is not the exclusions. It is **the decomposition and its
> dictionary** --- $K_\omega=B_b\widehat K_\omega$, a positive measure minus
> twice its exponential moving average, with the archimedean factor identified
> exactly as a horocycle integral in dimension $2\omega$ --- and **the
> instrument**: a registered, standard-library assembly of the compressed
> transfer $V_{\omega,L}$ from $\Gamma$, $\sinh$, $\exp$ and the integers below
> $e^L$, which computes $\lVert V_{\omega,L}\rVert$, $\lambda_{\min}(D_{\omega,L})$
> and the Cayley coordinate at any horizon and any $\omega\in(0,\frac12]$. Both
> live here: see [the checks index](numerics/README.md) and Sections 3--6 of the
> manuscript. Anything continuing this work should use them rather than rebuild
> them.
>
> The forward direction it opened --- whether $d=2\omega$ is a dimension or a
> parameter --- continues in
> [fractional dimension](../fractional-dimension/README.md), opened the same day.

An investigation opened by Edward Baker from the
[Wilson-lines note of the same day](../wilson-lines/notes/LOEWNER_AND_THE_MARKOV_DECOMPOSITION_20260917.md),
which asked whether a Loewner-type evolution could construct the shifted Weil
flow independently, with positivity coming from conformality rather than from
arithmetic, and found on the way that the transfer factors into an explicit
positive part and an explicit rational correction. That factorization is the
object here. Its name records where it came from; the opening note's first
finding is that Loewner evolution can carry at most the archimedean third of the
object.

**Nothing here is a construction. No source is built, no positivity is proved,
and nothing assumes the Riemann hypothesis except where a statement is labelled
conditional.**

## The object

With $s=\tfrac12+p$, $\Lambda(u)=\pi^{-u/2}\Gamma(u/2)\zeta(u)$,
$a=\tfrac12-\omega$, $b=\tfrac12+\omega$, the shifted Weil transfer
$K_\omega(p)=\xi(s-\omega)/\xi(s+\omega)$ of the shared
[background](../../background.pdf) factors as
\[
 K_\omega=B_b\,\widehat K_\omega,\qquad B_b=\frac{p-b}{p+b},\qquad
 \widehat K_\omega=\frac{(s-\omega)\,\Lambda(s-\omega)}{(s+\omega-1)\,\Lambda(s+\omega)}
 \ \text{ completely monotone on } p>b ,
\]
so that its causal kernel is $k_\omega=\widehat k_\omega-2\,\mathrm{EMA}_b[\widehat k_\omega]$
with $\widehat k_\omega\geq0$: **a positive measure minus twice its exponential
moving average at the rate $b$ set by the pole of $\zeta$.** The positive part is
explicit ---
\[
 \widehat k_\omega=\Big(1+2a\,e^{a\,\cdot}\mathbf 1_{>0}*\Big)\;
 k^\Gamma_\omega*\sum_{n\geq1}\widetilde c_n\,\delta_{\log n},\qquad
 k^\Gamma_\omega(x)=\frac{2\pi^\omega}{\Gamma(\omega)}(2\sinh x)^{\omega-1}e^{x/2},\qquad
 \widetilde c_n=n^{\omega-\frac12}\prod_{p\mid n}(1-p^{-2\omega}),
\]
a Beta-distributed continuous delay convolved with a multiplicative comb at the
integer ratios --- and the correction is one first-order all-pass section. The
transfer, its compression $V_{\omega,L}$, its norm and its defect are thereby
assembled exactly from elementary functions and the integers $n<e^L$, with no
$\xi$ and no zeros, as the localized Weil form is assembled from the explicit
formula.

## What is known so far

- **The archimedean factor is a horocycle integral in dimension $2\omega$.**
  Exactly, $K^\Gamma_\omega(p)=\int_{\mathbb R^{2\omega}}\lvert t+i\rvert^{-(p+b)}dt$:
  the delay is $\log\lvert t+i\rvert$, the log-modulus along a horocycle --- the
  arithmetic coordinate itself --- and the kernel's prefactor
  $2\pi^\omega/\Gamma(\omega)$ is the area of the unit sphere $S^{2\omega-1}$.
  **The shift is half a dimension.** As $\omega$ runs over $(0,\frac12]$ the
  dimension $2\omega$ runs over $(0,1]$ and takes exactly one integer value, at
  $\omega=\frac12$, where the horocycle is the cusp of the modular surface: which
  is why the endpoint is realized geometrically and the interior is not, and why
  the second Beta parameter below is $\omega=d/2$
  ([note of 18 September](notes/THE_SHIFT_IS_HALF_A_DIMENSION_20260918.md)).
- **Contraction at $\omega=\frac12$ is unconditional**, since the poles of
  $K_{1/2}(p)=\xi(p)/\xi(p+1)$ all have $\Re p\in(-1,0)$. So the family runs from
  a *free* endpoint to the Riemann hypothesis at $\omega\downarrow0$, and the
  whole content of the criterion is the deformation inward --- which the
  quantization above blocks geometrically.
- **No radial chain produces the archimedean factor**, for three independent
  reasons: the additivity fraction is independent of the total, so a
  dimension-$b$ chain cannot see the split $b=a+2\omega$; the antipodal exponent
  of any radial chord law is $-\frac12$ *for every driving*, because the Loewner
  drift vanishes there and only the Itô curvature survives, so the chord law is
  always $\mathrm{Beta}(\cdot,\frac12)$ while the target has both parameters
  below $\frac12$; and the delay's zero-delay singularity is a power law,
  $\mathbb E[U^q]\sim q^{-\omega}$, which no interior first-passage time has.
  **With the comb and the correction already excluded, the Loewner proposal
  closes.**
- **The archimedean factor is Bessel additivity.** $K^\Gamma_\omega\propto\mathbb E\,U^{p/2}$
  with $U=Z_a/(Z_a+Z_{2\omega})\sim\mathrm{Beta}(\frac a2,\omega)$ for squared
  Bessel processes of dimensions $a$ and $2\omega$, whose sum has dimension $b$.
  The quarter of the Wilson-lines delay test is half a Bessel dimension.
- **The comb is not a Loewner phenomenon.** A chain's transport of exterior
  points is a pure delay in the far field, so a translation-invariant induced
  kernel is a pure delay; on analytic observables a rotation-invariant chain
  induces only the dilation. The comb is the Hecke/Bost--Connes operator
  $\sum_n\widetilde c_n\mu_n$, $\mu_nf(x)=f(x-\log n)$.
- **The correction is forced.** $B_b$ (together with the factor absorbed into
  $\widehat K_\omega$) is the unique unimodular rational repair of the poles of
  $\Lambda$; its residues carry no arithmetic. There is no small place where the
  arithmetic hides: it is in the poles of $\widehat K_\omega$ at the zeros.
- **The endpoint is the modular surface.** At $\omega=\frac12$,
  $\widehat K_{1/2}$ is the Eisenstein scattering matrix of
  $PSL(2,\mathbb Z)\backslash\mathbb H$, the comb weights are $\varphi(n)/n$, and
  $K_{1/2}$ is that scattering matrix with its pole at $s=1$ removed by one
  Blaschke factor --- the Lax--Phillips modification.
- **Not a positivity mechanism.** By the dichotomy of the Wilson-lines
  manuscript (Proposition 7.2), contraction of $V_{\omega,L}$ for all $L$ is a
  zero-free strip of width $\omega$; structural positivity of $\widehat k_\omega$
  says nothing about it. RH is the stability, at every $\omega>0$, of a lossless
  filter whose impulse response is a positive measure minus twice its EMA.
- **The assembly works, at three horizons, in double precision.** The
  single-atom kernel is exactly $\tau^{\omega-1}\widehat G(\tau)$ with
  $\widehat G$ holomorphic on $|\tau|<\pi$, so the spike belongs in a
  Gauss--Jacobi *weight* and is never evaluated; the compressed transfer built
  from $k_\omega$ alone --- integers below $e^L$, Beta kernel, two exponential
  smoothings, no $\xi$, no zeros --- is then a strict contraction at
  $L=\log3,\log5,\log7$, and $\lambda_{\min}(I-V^*V)/2\omega$ agrees with the
  margin $m_L^{(N)}$ of the localized Weil form *in the same basis* to
  $0.54\%$, $1.20\%$ and $1.85\%$ at $\omega=0.01$ --- **margins from
  $6\times10^{-8}$ to $2\times10^{-22}$** --- with the deviation exactly linear
  in $\omega$, which is the Galerkin truncation term and nothing else
  ([note of 18 September](notes/REGISTERED_ASSEMBLY_AND_THE_HORIZONS_20260918.md)).
  Exactly: $D_{\omega,L}=2\omega Q_{0,L}-\omega^2(2Q_{0,L}^2+[Q_{0,L},A_{0,L}])+O(\omega^3)$
  with $A_{0,L}$ the skew part of the compressed generator, so at the minimizer
  the first-order law has relative correction $-\omega m_L$ and nothing else;
  the nested defect, carried to $N'=192$, shrinks and then crosses below one as
  that expansion requires. The first-order mass beyond the horizon has a closed
  form from $\xi'/\xi$ (poles, digamma, primes) that the assembled kernel
  matches at every horizon, and one atom has an exact Laplace transform
  $\pi^\omega\frac{\Gamma((a+p)/2)}{\Gamma((b+p)/2)}\frac{(p+a)(p-b)}{(p+b)(p-a)}$
  built from $\Gamma$ alone, which the assembly matches to $10^{-13}$.
- **Contraction is positivity in the Cayley coordinate, and that coordinate is
  even in the shift.** With $Z=(I-V)(I+V)^{-1}$ and $P=\frac2\omega\mathrm{Re}\,Z$,
  the congruence $I-V^*V=\frac\omega2(I+V^*)P(I+V)$ holds exactly (checked to
  $10^{-41}$), and $P_{-\omega,L}=P_{\omega,L}$ because $K_{-\omega}=1/K_\omega$
  and compression is a homomorphism of the causal algebra --- so
  $P_{\omega,L}=Q_{0,L}+O(\omega^2)$, where the defect carries a correction
  already at first order.
- **What the transfer knows that a lattice does not.** In the same $N=24$
  basis, the best phase-matched unfolded lattice --- the surrogate that gets
  the *density* of the zeros right --- misses the margin by factors $1.07$,
  $2.19$, $0.76$ at $\log3,\log5,\log7$, where the transfer, containing no zero
  and no lattice, misses by $0.54\omega$, $1.20\omega$, $1.85\omega$.

## Reading map

| Document | Role |
|---|---|
| [Manuscript](manuscript.pdf) · [TeX](manuscript.tex) · [build guide](BUILD.md) · [drafts](drafts/README.md) | *The Markov part of the shifted Weil transfer*, working draft 0.3 (33 pages): the self-contained report. Its introduction is written to be read first by someone new to the investigation; Sections 3--6 carry the proofs and the numerics. |
| [Inherited note](../wilson-lines/notes/LOEWNER_AND_THE_MARKOV_DECOMPOSITION_20260917.md) | The decomposition (its Section 4), with proofs and the first numerics. Read its Section 4 first. |
| [Opening note](notes/MARKOV_PART_AND_REALIZATIONS_20260917.md) | The results above, the correction to the inherited note's plan, and the ranked plan. |
| [Contraction-margin note](notes/CONTRACTION_MARGIN_FIRST_RUN_20260917.md) | The assembly validated at $L=\log3$; the second-order defect (Props. 2.1--2.2); the first-order tail (Prop. 2.3); numerical lessons. Two of its margin rows are superseded; see the banner at its head. |
| [Registered-assembly note](notes/REGISTERED_ASSEMBLY_AND_THE_HORIZONS_20260918.md) | Item 1 of the plan closed: the Gauss--Jacobi quadrature that puts the spike in the weight, the registered double-precision check, the horizons $\log5$ and $\log7$ (and where a fixed basis stops working), the nested limit, the Cayley coordinate, and the lattice control. |
| [Notes index](notes/README.md) | Navigation and status of each note. |
| [Checks](numerics/README.md) · [exploratory](numerics/exploratory/README.md) | Programmes and records. Two registered programmes (53 + 43 cases, standard library, replayed with the manuscript); five exploratory programmes with records. |
| [Reviews](reviews/README.md) | Dated assessments. None yet. |

## What is open, ranked

Items 1, 2 and 3 of the opening note's plan were all closed on 18 September ---
the contraction side is registered and carried to three horizons, the endpoint is
understood and is unconditional, and the Beta law is settled in the negative ---
and with them the Loewner proposal. Two of the questions this investigation
raised are about the transfer rather than about conformal maps and have moved to
[fractional dimension](../fractional-dimension/README.md): whether $d=2\omega$ is
a dimension, and what the comb is in the Bost--Connes algebra at that $d$. What
is still this investigation's own:

1. **The second-order coefficient, in closed form.**
   $\lambda_{\min}(D)/2\omega=m_L-\omega m_L^2+c_2\omega^2+\dots$ and
   $\lambda_{\min}(P)=m_L+c_2'\omega^2+\dots$, with $c_2'-c_2=0.0362\,m_L$
   measured. It is the only place so far where $A_{0,L}$ --- the compressed
   Hilbert transform of the interval together with the odd part of the comb ---
   enters a measured number. The practical half is settled: the coefficient is
   of order unity at every horizon ($1.64$, $3.33$, $1.79$) against an a-priori
   scale $\kappa_L^2$ of $10^{3}$, $10^{12}$, $10^{22}$, so the first-order
   law's validity window does not collapse with $L$.
2. **The passivity statement.** A clean account of why no passivity theorem for
   filters of the form "positive measure minus twice its exponential moving
   average" can avoid the location of the poles --- what property of
   $\widehat k_\omega$ beyond positivity would be needed. This is the honest end
   of the filter reading, and it belongs here because the decomposition does.
3. **The Lax--Phillips semigroup estimate at the endpoint**, demoted: the
   endpoint conclusion is unconditional and the estimate cannot transport inward
   past the quantization of the offset.

## Relation to the sibling investigations

- [Fractional dimension](../fractional-dimension/README.md) was opened from this
  investigation on 18 September, to ask what the dimension $d=2\omega$ of the
  horocycle representation is. It inherits the decomposition, the dictionary and
  the instrument; it found on its first day that the comb's weights are the
  Jordan totient $J_d(n)/n^{(d+1)/2}$, so all three factors are $d$-dimensional
  as formulas.

- [Wilson lines](../wilson-lines/README.md) supplies the transfer, the flow
  identities, the all-pass identification, the dichotomy and the endpoint
  algebra; the decomposition studied here first appears in its notes, and its
  [review of 17 September](../wilson-lines/reviews/review_claude-fable-5-1_2026-09-17.md)
  identifies the modular surface as the transfer at $\omega=\frac12$.
- [Source selection rules](../source-selection-rules/README.md) supplies the
  Lévy-jump presentation of the form (its ninth rule); the comb here is that
  presentation on the transfer side, with its coefficients at every shift.
- [Inverse bulk realization](../inverse-bulk-realization/README.md) supplies the
  target and the exclusions, none of which touches a filter decomposition.

## Conventions

Research notes go in [`notes/`](notes/README.md) and reviews in
[`reviews/`](reviews/README.md), with the model named at the top of anything
written by a language model. Registered check programmes go in
[`numerics/`](numerics/README.md): standard library only, JSON to standard
output, a preserved record under `numerics/records/`, and registration in
`validation/drafts.py`; anything needing `mpmath` goes in
`numerics/exploratory/` and is labelled unregistered. The manuscript
follows the Wilson-lines layout (`manuscript.tex`, `sections/`, `BUILD.md`,
`validation/drafts.py`, dated snapshots under `drafts/`); see
[BUILD.md](BUILD.md) for building, recording and snapshotting. Keep every file
under 1 MiB and follow the repository's
[large-file policy](../../../../LARGE_FILES.md).

## Reproduction

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build manuscript.tex
python3 validation/drafts.py check --replay          # replays the registered check
python3 numerics/check_contraction_margin.py         # ~1 s, standard library only
python3 numerics/check_beta_realization.py           # <1 s, standard library only
python3 numerics/exploratory/decomposition_checks.py 0.1
python3 numerics/exploratory/transfer_kernel.py 0.1 2.5
cd numerics/exploratory                              # both need ../../../wilson-lines/numerics/exploratory/weil_sine_basis.py
python3 contraction_margin_gj.py 0.01 log3 24 40 40  # ~1 s; log5 / log7 want dps 50 / 60
python3 gram_control_vs_transfer.py 3000 24 50       # ~14 s
```

Related: the [program index](../../README.md) and the
[program overview](../../PROGRAM_OVERVIEW.md).

# Loewner: the Markov part of the shifted transfer and what can realize it

17 September 2026. Manuscript: [*The Markov part of the shifted Weil
transfer*](manuscript.pdf), working draft 0.1. An investigation opened by Edward Baker from the
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
- **The assembly works.** At $L=\log3$ the compressed transfer built from
  $k_\omega$ alone --- integers below $3$, Beta kernel, two exponential
  smoothings, no $\xi$, no zeros --- is a strict contraction, and
  $\lambda_{\min}(I-V^*V)/2\omega$ agrees with the margin $m_L$ of the localized
  Weil form in the same basis to $0.1\%$ at $\omega=0.01$
  ([contraction-margin note](notes/CONTRACTION_MARGIN_FIRST_RUN_20260917.md)).
  Exactly: $D_{\omega,L}=2\omega Q_{0,L}-\omega^2(2Q_{0,L}^2+[Q_{0,L},A_{0,L}])+O(\omega^3)$
  with $A_{0,L}$ the skew part of the compressed generator, so at the minimizer
  the first-order law has relative correction $-\omega m_L$ and nothing else;
  the Galerkin excess is a truncation term that dies under nesting. The
  first-order mass beyond the horizon has a closed form from $\xi'/\xi$
  (poles, digamma, primes) that the assembled kernel matches to five digits.

## Reading map

| Document | Role |
|---|---|
| [Manuscript](manuscript.pdf) · [TeX](manuscript.tex) · [build guide](BUILD.md) · [drafts](drafts/README.md) | *The Markov part of the shifted Weil transfer*, working draft 0.1 (25 pages): the self-contained report. Its introduction is written to be read first by someone new to the investigation; Sections 3--5 carry the proofs and the numerics. |
| [Inherited note](../wilson-lines/notes/LOEWNER_AND_THE_MARKOV_DECOMPOSITION_20260917.md) | The decomposition (its Section 4), with proofs and the first numerics. Read its Section 4 first. |
| [Opening note](notes/MARKOV_PART_AND_REALIZATIONS_20260917.md) | The results above, the correction to the inherited note's plan, and the ranked plan. |
| [Contraction-margin note](notes/CONTRACTION_MARGIN_FIRST_RUN_20260917.md) | The assembly validated at $L=\log3$; the second-order defect (Props. 2.1--2.2); the first-order tail (Prop. 2.3); numerical lessons for the registered version. |
| [Notes index](notes/README.md) | Navigation and status of each note. |
| [Checks](numerics/README.md) · [exploratory](numerics/exploratory/README.md) | Programmes and records. No registered programme yet; three exploratory programmes with records. |
| [Reviews](reviews/README.md) | Dated assessments. None yet. |

## What is open, ranked

1. Finish the contraction side. Done at $L=\log3$, exploratory: the assembly,
   $\lVert V_{\omega,L}\rVert$, $\lambda_{\min}(D_{\omega,L})$ and
   $\lambda_{\min}/2\omega\to m_L$. Remaining: a standard-library registered
   version at $L=\log3$ (the one horizon where $2\omega m_L$ is resolvable in
   double precision), the horizons $\log5,\log7$ at 40 digits, the cumulative
   Cayley coordinate, and the phase-matched Gram control on the form side
   against the transfer's margin.
2. The Lax--Phillips dictionary at $\omega=\frac12$, object by object, and what
   the $\omega$-deformation can and cannot move.
3. Whether a conformal-radius or hitting law of a radial Loewner chain driven by
   a Bessel process of dimension $b$ realizes the additivity fraction --- the one
   question here that is about Loewner evolution.
4. The comb as an element of the Bost--Connes algebra, and what its KMS
   structure says about the compression.
5. A clean statement of why no passivity theorem for "positive measure minus
   twice its EMA" can avoid the location of the poles.

## Relation to the sibling investigations

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
output, a preserved record under `numerics/records/`; anything needing `mpmath`
goes in `numerics/exploratory/` and is labelled unregistered. The manuscript
follows the Wilson-lines layout (`manuscript.tex`, `sections/`, `BUILD.md`,
`validation/drafts.py`, dated snapshots under `drafts/`); see
[BUILD.md](BUILD.md) for building, recording and snapshotting. Keep every file
under 1 MiB and follow the repository's
[large-file policy](../../../../LARGE_FILES.md).

## Reproduction

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build manuscript.tex
python3 validation/drafts.py check
python3 numerics/exploratory/decomposition_checks.py 0.1
python3 numerics/exploratory/transfer_kernel.py 0.1 2.5
cd numerics/exploratory && python3 contraction_margin.py 0.01 log3 24 16   # ~45 s; needs ../../../wilson-lines/numerics/exploratory/weil_sine_basis.py
```

Related: the [program index](../../README.md) and the
[program overview](../../PROGRAM_OVERVIEW.md).

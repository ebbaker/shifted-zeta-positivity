# Fractional dimension: is $d=2\omega$ a dimension, or a parameter?

Opened 18 September 2026 by Edward Baker from the
[Loewner investigation](../loewner/README.md), which closed that day: its
[final note](../loewner/notes/THE_SHIFT_IS_HALF_A_DIMENSION_20260918.md) proved
that the archimedean factor of the shifted Weil transfer is a horocycle integral
in dimension $2\omega$, and that every conformal realization of the family
quantizes that dimension. This investigation asks what the dimension is.

**Nothing here is a construction. No positivity is proved, and nothing assumes
the Riemann hypothesis except where a statement is labelled conditional.**

## The object

With $s_0=\frac12+p$, $a=\frac12-\omega$, $b=\frac12+\omega$, put
\[
 d=2\omega,\qquad s=\frac{p+b}2,\qquad\text{so}\quad 2s=p+b,\quad 2s-d=p+a,\quad b=\frac{d+1}2 .
\]
The Markov part of the transfer is then
\[
 \widetilde K_\omega(p)=\frac{\Lambda(s_0-\omega)}{\Lambda(s_0+\omega)}
 =\frac{\Lambda(2s-d)}{\Lambda(2s)}
 =\underbrace{\pi^{d/2}\frac{\Gamma(s-\frac d2)}{\Gamma(s)}}_{\textstyle\int_{\mathbb R^{d}}|t+i|^{-(p+b)}dt}
 \cdot\underbrace{\frac{\zeta(2s-d)}{\zeta(2s)}}_{\textstyle\text{weights }J_d(n)/n^{(d+1)/2}} ,
\]
and the Blaschke factor of the full transfer sits at $p=b=\frac{d+1}2$, that is
at $2s=d+1$, the pole of the volume term. **The shift enters only as a
dimension.** At $d=1$ every piece is a classical object: the Eisenstein
scattering matrix of $PSL(2,\mathbb Z)\backslash\mathbb H$, its one-dimensional
horocycle, and the reduced-fraction count $\varphi(n)/n$.

## What is known so far

- **All three factors are $d$-dimensional as formulas.** The archimedean factor
  is the Riesz integral over $\mathbb R^{d}$, with the delay $\log|t+i|$ and the
  kernel prefactor $|S^{d-1}|$ (inherited). **The comb's weights are the Jordan
  totient**, $\widetilde c_n=J_d(n)/n^{(d+1)/2}$ with
  $J_d(n)=n^d\prod_{p\mid n}(1-p^{-d})$, which at integer $d$ counts the
  primitive vectors in $(\mathbb Z/n\mathbb Z)^d$ --- the $d$-dimensional reduced
  fractions with denominator $n$ (opening note, Proposition 1.2). The correction
  is the pole of $\zeta(2s-d)$. The same $d$ appears in the sphere area, the
  Gamma shift, the $\zeta$ offset and the Euler factors.
- **$d=1$ is the only integer the family's range contains**, and it is where the
  transfer is both geometrically realized and *unconditionally* a contraction at
  every horizon.
- **What is not known** is whether fractional $d$ is anything. $J_d$ stays a
  multiplicative function but stops counting; $\mathbb R^{d}$ stops being a
  space; $\Lambda(2s-d)/\Lambda(2s)$ stops being anybody's scattering matrix.

## Reading map

| Document | Role |
|---|---|
| [Opening note](notes/OPENING_NOTE_20260918.md) | The dictionary, the Jordan-totient identification, the question stated three ways, and the ranked plan. |
| [Notes index](notes/README.md) | Navigation and status of each note. |
| [Checks](numerics/README.md) · [exploratory](numerics/exploratory/README.md) | Programmes and records. One programme, 72 cases; no exploratory programme yet. |
| [Reviews](reviews/README.md) | Dated assessments. None yet. |
| [Loewner investigation](../loewner/README.md) | The parent. Its manuscript is the consolidated report of everything inherited here, and its registered assembly of $V_{\omega,L}$ is the instrument this investigation should use rather than rebuild. |

## What is open, ranked

1. **The Bessel--Hankel index.** The radial Laplacian in dimension $d$ has index
   $\nu=\frac d2-1=\omega-1$, and the archimedean kernel is
   $(2\sinh\tau)^{\nu}e^{\tau/2}$ --- where $(\sinh\tau)^{\nu}$ is also the radial
   Jacobian of *hyperbolic* space of dimension $\omega$. Two dimensions are in
   play, $2\omega$ Euclidean and $\omega$ hyperbolic. Which one is the kernel
   carrying? Self-contained, no arithmetic, and everything else depends on the
   answer.
2. **The comb at fractional $d$.** Does $J_d$ count, bound, or measure anything
   when $d\notin\mathbb Z$? The candidates are a Bost--Connes algebra with a
   $d$-dependent state, and the zeta function of a space of fractional dimension.
3. **The Blaschke factor as a volume.** At $d=1$ its pole is the residue of the
   Eisenstein series, the volume of the surface. If $d$ is a dimension, the
   coefficient should be computable as one. Short, decisive.
4. **Dimensional regularization of the criterion.** Whether
   $\lVert V_{\omega,L}\rVert$ and the first-order law have meanings as functions
   of complex $d$, and whether contraction continues. Testable numerically with
   the inherited instrument before it is understood.
5. **The endpoint as a boundary condition.** $d=1$ has a known boundary value;
   what does $\partial_d$ there compute?

## Relation to the sibling investigations

- [Loewner](../loewner/README.md) is the parent and is closed: it decomposed the
  transfer, identified its three pieces, excluded all three from a conformal
  realization, and built the registered assembly of the compressed transfer. Its
  manuscript, *The Markov part of the shifted Weil transfer* (working draft 0.3),
  carries everything inherited here.
- [Wilson lines](../wilson-lines/README.md) supplies the transfer, the flow
  identities, the dichotomy and the margins $m_L$, $\kappa_L$.
- [Source selection rules](../source-selection-rules/README.md) supplies the
  Lévy-jump presentation of the form.

## Conventions

Research notes go in [`notes/`](notes/README.md) and reviews in
[`reviews/`](reviews/README.md), with the model named at the top of anything
written by a language model. Check programmes go in
[`numerics/`](numerics/README.md): standard library only, JSON to standard
output, a preserved record under `numerics/records/`, and --- once a manuscript
exists --- registration in the `CHECKS` dictionary of its
`validation/drafts.py`; anything needing `mpmath` goes in
`numerics/exploratory/` and is labelled unregistered. Keep every file under
1 MiB and follow the repository's
[large-file policy](../../../../LARGE_FILES.md).

## Reproduction

```sh
python3 numerics/check_dimension_dictionary.py     # <1 s, standard library only
```

Related: the [program index](../../README.md) and the
[program overview](../../PROGRAM_OVERVIEW.md).

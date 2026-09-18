# Fractional dimension: is $d=2\omega$ a dimension, or a parameter?

Opened 18 September 2026 by Edward Baker from the
[Loewner investigation](../loewner/README.md), which closed that day: its
[final note](../loewner/notes/THE_SHIFT_IS_HALF_A_DIMENSION_20260918.md) proved
that the archimedean factor of the shifted Weil transfer is a horocycle integral
in dimension $2\omega$, and that every conformal realization of the family
quantizes that dimension. This investigation asks what the dimension is.

**Nothing here is a construction. No positivity is proved, and nothing assumes
the Riemann hypothesis except where a statement is labelled conditional.**

**Manuscript:** *A scattering matrix without a space* ([PDF](manuscript.pdf),
[TeX](manuscript.tex)), working draft 0.1, 21 pages, 18 September 2026. It is the
consolidated report of the whole investigation, and its six registered check
programmes (1522 cases) are replayed with it by
`python3 validation/drafts.py check --replay`. Snapshot
[`drafts/2026-09-18-v01`](drafts/README.md); build guide [`BUILD.md`](BUILD.md).

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
- **The dimension is $2\omega$, not $\omega$, and the factor of two was a
  coordinate artifact.** $\tau=\log|t+i|$ is a *Busemann* function on the
  horocycle, not a distance, and $\tau\sim r^2/2$ is a square: a measure with
  local exponent $r^{2\omega-1}dr$ therefore has local exponent
  $\tau^{\omega-1}d\tau$, the two normalized limits differing by exactly
  $2^{1-\omega}$. In the true half-distance the measure is the radial measure of
  complex hyperbolic space of complex dimension $\omega$ and real dimension
  $2\omega$; and the comb, having no radial coordinate at all, fixes $d=2\omega$
  independently (second note, Propositions 1.1 and 2.1).
- **The correction is a volume term, and it supplies the rank.**
  $\operatorname{Res}_{p=b}\widetilde K_\omega=|S^{d}|/2\zeta(d+1)$ --- the sphere
  of $\mathbb R^{d+1}$ times the primitive density in $\mathbb Z^{d+1}$ --- which
  is the volume term of a **lattice of rank $d+1$** whose cusp integrates over a
  horocycle of dimension $d$. At $d=1$ it is $6/\pi=2/\mathrm{vol}$, the classical
  Eisenstein residue (second note, Proposition 3.1). So all three entries name one
  object: a rank-$(d+1)$ lattice in $\mathbb R^{d+1}$ with a $d$-dimensional
  horocycle.
- **The object at integer $d$ is a lattice of rank $d+1$ --- at every integer,
  not only at $d=1$.** For a covolume-one lattice $L\subset\mathbb R^{m}$ the
  primitive Epstein zeta $E^{*}_L(s)=\sum_{v\ \mathrm{prim}}\lvert v\rvert^{-2s}$
  satisfies $\xi(2s)E^{*}_L(s)=\xi(m-2s)E^{*}_{L^{*}}(m/2-s)$, so its reflection
  ratio is independent of $L$ and is an invariant of the **rank alone**; under the
  dictionary that ratio is exactly $\widetilde K_\omega$, and the transfer's own
  reflection $p\mapsto-p$ *is* the Epstein functional equation $s\mapsto m/2-s$,
  which is why $\lvert\widetilde K_\omega\rvert=1$ on $\Re p=0$ (third note,
  Propositions 1.1 and 1.2). So $d=1,2,3,\dots$ are all realized, as ranks
  $2,3,4,\dots$; they simply lie outside the range.
- **The range is a rank cap, and the cap is $\zeta$'s own pole.** $\xi$ has poles
  at $0$ and $1$, so the numerator of $\widetilde K_\omega$ has a second pole at
  $p=\omega-\frac12$, which is in the closed left half-plane iff $\omega\le\frac12$
  iff $m\le2$; in the lattice variable it sits at $s=\frac{m-1}2=\omega$, where
  $\zeta(2s)$ has its pole exactly at $\omega=\frac12$ (third note,
  Proposition 2.1). The family therefore occupies the **first gap** of the rank
  sequence, $m\in(1,2]$, with the modular surface at its right endpoint.
- **And inside that gap the lattice does not exist.** The point count of
  $\mathbb Z^{m}$ has a unique interpolation --- the $q$-coefficients of
  $\theta^{m}$, polynomial in $m$ --- and with $m=d+1$,
  $r_{d+1}(3)=\frac43(d^{3}-d)$ is strictly negative for every $d\in(0,1)$ and
  vanishes only at the endpoints; equivalently $\theta(it)^{d+1}$ is not
  completely monotone anywhere strictly inside the family, so there is no positive
  measure and no point set (third note, Propositions 3.1 and 3.2).
- **$d=1$ is the only integer the family's range contains**, and it is where the
  transfer is both geometrically realized and *unconditionally* a contraction at
  every horizon.
- **What is now known about fractional $d$** is that whatever the object is, it
  is **not a point set**. Every *cusp* invariant continues positively --- $J_d(n)>0$
  and $1/\zeta(d+1)\in(0,1)$ for every real $d>0$, the horocycle integral exists,
  the transfer kernel stays completely monotone, and the scattering matrix stays
  unimodular on the critical line --- while the *interior* does not. At fractional
  $d$ there is a **scattering matrix without a space**.
- **The decomposition survives past the rank-two wall, and so does its
  positivity.** $R_\omega=B_b\cdot\frac{p+a}{p-a}$ at every $\omega$, and
  $\frac{p+a}{p-a}=B_c$ with $c=\omega-\frac12$ is a Blaschke factor of the right
  half-plane exactly when $\omega\ge\frac12$: so past the wall $R_\omega=B_bB_c$ is
  **inner**, where inside the range it is a ratio $B_b/B_a$ with a right-half-plane
  pole. The parent's proof that $\widehat K_\omega$ is completely monotone fails
  there, but the statement does not --- regrouping the Gamma factors,
  $\widehat K^\Gamma_\omega=\pi^\omega\frac{\Gamma(z+c)}{\Gamma(z+\omega)}
  \frac{\Gamma(z+1)}{\Gamma(z+c+1)}$ with $z=\frac{p+a}2$, exhibits it as a product
  of two completely monotone Gamma ratios for every $\omega\ge\frac12$. The two
  poles being cancelled have different origins: $p=b$ is the comb's, $p=c$ is the
  **archimedean factor's**, so past the wall the correction removes one pole from
  each half of the transfer (fourth note, Propositions 1 and 2).
- **But past the wall the criterion is empty.** For every $\omega\ge\frac12$ no
  zero satisfies $\lvert\Re\rho-\frac12\rvert>\omega$, because $0\le\Re\rho\le1$;
  so by the parent's own dichotomy $V_\omega$ is unitary and every $V_{\omega,L}$ is
  a contraction **unconditionally** --- on the strength of the Euler product alone for
  $\omega>\frac12$, with the classical zero-free region needed only at the single
  boundary point $\omega=\frac12$. The
  contraction criterion has arithmetic content on exactly $\omega\in(0,\frac12)$,
  where it is equivalent to the zero-free strip of half-width $\omega$ (fourth note,
  Proposition 3 and Corollary 3.1).
- **And that is the same interval on which the lattice fails to exist.**
  $\omega\in(0,\frac12)$ is $d\in(0,1)$ is $m\in(1,2)$ --- the open gap on which
  $r_{d+1}(3)<0$. Same interval, same endpoints, both switching on the sign of
  $a=\frac{1-d}2$. **The criterion has arithmetic content precisely where the
  lattice does not exist** (fourth note, Observation 4.1).
- **Which endpoint is RH.** Not the right one. The criterion is *emptiest* at
  $\omega=\frac12$ and sharpest as $\omega\downarrow0$: **the Euler product is its
  value at rank two, and RH is its derivative at rank one**, where
  $E^{*}_{\mathbb Z}\equiv2$, $\widetilde K_0=1$, $V_0=I$ and the first-order law
  makes the localized Weil form its $\partial_\omega$. The gap between the two
  lowest ranks interpolates between them by zero-free strips of half-width
  $\frac{m-1}2$ (fourth note, Section 5).
- **The two positivity statements are not one statement.** The point count fails on
  $(2,3)$ as well as on $(1,2)$, while the criterion has content only on $(1,2)$;
  and at $m=3$ the point count is completely monotone and the transfer's rational
  factor is not. So no equivalence between them can hold, and the coincidence of
  intervals is the first gap and nothing more --- forced by both of the criterion's
  endpoints sitting at the two smallest ranks, $m=1$ where the transfer degenerates
  and $m=2$ where $a$ changes sign (fifth note, Corollary 3.1).
- **The point count's failure is Lagrange's theorem, seen through a binomial
  series.** On the gap $m\in(k,k+1)$,
  $\operatorname{sign}\binom mj=(-1)^{\max(0,j-k-1)}$, so $r_m(n)>0$ for free when
  $n\le k+1$, and the first coefficient that can be *forced* negative sits at $N_k$,
  the least integer needing $k+2$ **positive** squares: $N_0=2$, $N_1=3$, $N_2=7$,
  and **no $N_k$ at all for $k\ge3$, because Lagrange's four-square theorem gives
  $s(n)\le4$ for every $n$.** The third note's Lagrange threshold at $m=4$ is
  exactly that, and is now a theorem rather than a scan (fifth note,
  Propositions 1.1--1.4).
- **The transfer has exactly one positivity threshold, and it is at $m=2$.** Every
  factor of the Markov part has a positive kernel at every real $\omega>0$; the only
  $\omega$-dependent positivity anywhere in the decomposition is
  $\frac{p+a}{p-a}$. Its only other feature at an integer, the archimedean exponent
  $\omega-1=\frac{m-3}2$ vanishing at $m=3$, is a *regularity* threshold and points
  the wrong way (fifth note, Proposition 2.1).
- **What does explain the split: the rank's position.** In the transfer the rank
  enters every positive object as an **exponent** --- $(2\sinh\tau)^{\omega-1}$ in
  the archimedean kernel, $(1-e^{-t})^{\beta-\alpha-1}$ in each Beta density,
  $p^{-d}$ in each Euler factor of the comb --- where positivity is a *local*
  inequality, at one $\tau$ or at one prime, that continuation cannot break. In the
  point count it enters as a **binomial index**, where positivity is a global
  cancellation and continuation breaks it at once (fifth note, Proposition 4.1).
  The transfer's positivity was never inherited from a lattice, so the lattice's
  failure leaves no trace in it --- and item 3 of the third note's plan, as posed,
  has no solution: no factor of the transfer loses positivity at fractional $d$.
- **What is still not known** is what that scattering matrix is the scattering
  matrix *of*, and why the family carries two positivity statements that part
  company at the same $\omega$: the transfer kernel keeps complete monotonicity
  and the lattice theta loses it.

## Reading map

| Document | Role |
|---|---|
| [Manuscript](manuscript.pdf) | *A scattering matrix without a space*, working draft 0.1. The whole investigation in one place, with every proposition proved in place and the inherited ones listed in its Section 2.3. |
| [Opening note](notes/OPENING_NOTE_20260918.md) | The dictionary, the Jordan-totient identification, the question stated three ways, and the ranked plan. |
| [Which dimension, and the volume](notes/WHICH_DIMENSION_AND_THE_VOLUME_20260918.md) | Items 1 and 3 of that plan, both answered: the dimension is $2\omega$ and $\tau$ is a Busemann coordinate; the Blaschke residue is $\lvert S^{d}\rvert/2\zeta(d+1)$, the volume term of a rank-$(d+1)$ lattice. Section 4 is the dictionary closed; Section 5 is the current plan. |
| [The rank and the lattice](notes/THE_RANK_AND_THE_LATTICE_20260918.md) | The head item answered: $\widetilde K_\omega$ is the rank-$(d{+}1)$ primitive-Epstein scattering matrix at every integer $d$; the range is the rank-two wall; and the lattice's point count is negative throughout the open range. Section 5 is the dictionary with a fractional column; Section 6 is the current plan. |
| [Past the wall](notes/PAST_THE_WALL_20260918.md) | Item 1 answered in both halves: the decomposition and its complete monotonicity survive past $\omega=\frac12$ (Props. 1--2), the instrument needed only a removable $0/0$, but the criterion is **vacuous** there by the Euler product (Prop. 3), so its content sits on exactly the interval where the lattice does not exist (Obs. 4.1). Section 5 corrects which endpoint is RH; Section 6 is the current plan. |
| [The trade is not it](notes/THE_TRADE_IS_NOT_IT_20260918.md) | The head item answered, in the negative: the two positivity sets diverge on $(2,3)$ (Cor. 3.1), the point count's failure is Lagrange's theorem through a binomial series (Props. 1.1--1.4), the transfer has one threshold and it is at $m=2$ (Prop. 2.1), and the split is explained by where the rank sits --- an exponent on one side, a binomial index on the other (Prop. 4.1). Section 5 judges the question answered. |
| [Notes index](notes/README.md) | Navigation and status of each note. |
| [Checks](numerics/README.md) · [exploratory](numerics/exploratory/README.md) | Programmes and records. Six programmes, 1522 cases; no exploratory programme yet. |
| [Reviews](reviews/README.md) | Dated assessments. None yet. |
| [Loewner investigation](../loewner/README.md) | The parent. Its manuscript is the consolidated report of everything inherited here, and its registered assembly of $V_{\omega,L}$ is the instrument this investigation should use rather than rebuild. |

## What is open, ranked

The investigation's own question --- **is $d$ a dimension, or a parameter?** --- is
answered: **a parameter.** The dictionary names one object; the object is a
rank-$(d{+}1)$ lattice at every integer and nothing strictly in between; the
transfer continues past the family's range with its decomposition and its
positivity intact while its criterion does not; and the transfer's positivity
continues for reasons that have nothing to do with a lattice, so the lattice's
failure leaves no trace in it. There is no remaining sense in which $d$ is a
dimension away from the integers.

The manuscript is written: *A scattering matrix without a space*, working draft
0.1, 21 pages. What is genuinely still open, ranked:

1. **The complex-hyperbolic line.** $(\alpha,\beta)=(\omega-1,0)$ with
   $\rho=\omega$ is a Heckman--Opdam parameter with a transform theory at arbitrary
   multiplicity. Proposition 4.1 of the fifth note explains why that half continues
   at all --- its positivity is a Beta density with $\omega$ in the exponent ---
   so the question is whether Heckman--Opdam adds anything beyond a name for it.
2. **Convention hygiene**, before any manuscript: the first three notes here write
   $\xi$ for what the parent manuscript calls $\Lambda$, and the two differ by
   exactly $R_\omega$. Pick one direction and fix it.
3. **Two clean conjectures about sums of squares, not to be chased here.** That
   $r_m(n)\ge0$ for every $n$ and every real $m\ge4$; and that the negative
   coefficients on $(3,4)$ arise from competition rather than forcing. Neither is
   about $\zeta$.
4. **Bost--Connes at fractional $d$** --- demoted, and staying demoted.

**Closed.** *The half-integer points beyond the range*, in both halves (fourth
note): the re-derivation needs no repair, and the experiment it unlocks is vacuous.
*Is the trade the explanation?* (fifth note): no --- the two positivity sets
diverge on $(2,3)$. *A factorization of the transfer exhibiting which factor loses
positivity at fractional $d$* (third note, item 3, as posed): there is none, because
no factor loses positivity anywhere.

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
output, a preserved record under `numerics/records/`, and registration in the
`CHECKS` dictionary of [`validation/drafts.py`](validation/drafts.py); anything needing `mpmath` goes in
`numerics/exploratory/` and is labelled unregistered. Keep every file under
1 MiB and follow the repository's
[large-file policy](../../../../LARGE_FILES.md).

## Reproduction

```sh
python3 numerics/check_dimension_dictionary.py    # <1 s, standard library only
python3 numerics/check_which_dimension.py         # <1 s, standard library only
python3 numerics/check_residue_volume.py          # <1 s, standard library only
python3 numerics/check_epstein_scattering.py      # <1 s, standard library only
python3 numerics/check_two_blaschke.py            # ~2 s, standard library only
python3 numerics/check_the_trade.py               # <1 s, standard library only
```

and the manuscript, with all six replayed against their preserved records:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build manuscript.tex
python3 validation/drafts.py check --replay     # 1522 cases, byte-identical
```

Related: the [program index](../../README.md) and the
[program overview](../../PROGRAM_OVERVIEW.md).

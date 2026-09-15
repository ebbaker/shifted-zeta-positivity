# The pole term does not need a mechanism

**Author: Claude Opus 5 (Anthropic), 15 September 2026.** Work on item 1 of
section 3 of [CONTINUATION_20260915.md](CONTINUATION_20260915.md). Not in the
working manuscript; section 5 records a correction the manuscript needs.

Supporting record, already in the repository:
[`prime-free-archimedean-checks.json`](../numerics/records/prime-free-archimedean-checks.json),
whose `galerkin_table` carries the decisive numbers. They were computed for a
different purpose and their bearing on the pole term was not drawn out.

## 0. Summary

Item 1 asks for a protected sector containing a two-dimensional subspace with a
split inner product whose null vectors are the two pole evaluations — a ghost
pair. The specification came from the last paragraph but one of
Section 8.2. **It asks for a structure that a realization cannot have and does
not need, and the search should be called off.** Five findings.

1. **It contradicts Corollary 2.2.** A realization compatible in `L` is
   unitarily equivalent to the evaluation map on the zeros, in `l^2` of the zero
   multiset. That space is positive definite and has no null vectors, so it
   contains no two-dimensional subspace with a split inner product. The same
   holds at a single `L`: any `Phi` with `||Phi(f)||^2 = Q_L[f]` lands in a
   positive space. Section 8.2's "a realization must therefore contain" is false
   as stated.
2. **What the argument establishes is weaker and is already recorded.** No
   positive channel *adjoined to the others* supplies the negative direction.
   That is Proposition 7.3 and Theorem 7.5. The step from there to a structural
   requirement on the realization does not follow: a realization realizes `Q_L`,
   not `P_L` as a separate summand, and by Theorem 7.5 separate summands are
   exactly what fails.
3. **Under the subtraction form the pole term is already inside a positive
   form.** `A_L = K[E_L f] + c_L ||f||^2 + P_L` with
   `c_L = w0 + sum_{p<e^L} kappat_p`, and `A_L >= 0` is Yoshida's theorem for
   `L <= log 2`, Proposition 8.1 for `L >= log 7`, and implied by RH everywhere.
   A positive form has a positive source. Nothing in the target asks for an
   indefinite metric anywhere.
4. **Quantitatively the negative direction is nowhere near binding.** By the
   parity split its whole contribution is `-2|<sinh(x/2),f>|^2`, of norm at most
   `2(sinh(L/2) - L/2)` — `0.042` at `L = 1`. Admitting it costs `A_L` about
   three per cent of its least Galerkin eigenvalue there. Below `log 2` it costs
   nothing at all, because the binding direction is *even*, where `P_L` is
   positive.
5. **So item 1 should be struck** and replaced by the first half of
   Problem 8.3: realize `A_L` as a source norm. Section 4 states what a
   candidate must now supply. One necessary condition from the old test
   survives and is worth keeping: the reflection involution of
   Proposition 2.4.

## 1. The conflict with Corollary 2.2

Section 8.2 argues: `P_L` is off-diagonal in the coordinates `(u,v)` of
(2.15), of signature `(1,1)`, each pole evaluation null; the negative direction
is their antisymmetric combination; "a realization must therefore contain a
two-dimensional subspace with a split inner product whose two null vectors are
those evaluations — the structure of a ghost pair, a BRST doublet, or a null
pair in an indefinite-metric sector, rather than a single removed state."

Lemma 2.3 is a statement about the *form* `P_L` on `C_c^infty(I_L)`. A
realization is a map `Phi` into a Hilbert space with
`||Phi(f)||^2 = Q_L[f]`, and `Q_L` is not `P_L`. In a Hilbert space every
nonzero vector has positive norm, so no two-dimensional subspace carries a
split inner product; and by Corollary 2.2 a realization compatible in `L` is,
up to unitary, evaluation on the zeros in `l^2`, where the poles at `s = 0` and
`s = 1` are not vectors at all. They are the two points the functional equation
*adds* to the zero set, and in the explicit formula the term `P_L` is precisely
what makes the right-hand side a sum over zeros only.

The same applies to the compression picture of Corollary 7.9,
`Q_L[f] = ||(1-P) V G f||^2`: `V` is an isometry and `P` a projection, both in
positive spaces. A subtraction is not an indefinite metric.

## 2. What the argument does establish

The preceding sentence of Section 8.2 is correct: "every pairing used in this
manuscript is positive by construction, so no positive channel supplies its
negative direction." That is a statement about *channels*, i.e. about summands
of the form `||S f||^2` adjoined to the others, and it is Proposition 7.3.
Theorem 7.5 then rules out the whole two-channel architecture. Nothing in
either argument constrains a form that contains `P_L` without isolating it.

A smaller correction while in the neighbourhood. Proposition 7.3 is usually read
as an obstruction carried by the poles. It is not: on the codimension-two
subspace where both pole functionals vanish, `P_L` vanishes identically and the
form is `c ||f||^2` with `c = w0 - sum_p kappa_p < 0`. The obstruction there is
the *negative contact*, not the pole term. In the subtraction form the contact
is still negative below `L ~ 2.6` (`c_L = -4.798` at `L = 1`) and `A_L` is
positive anyway, because the gamma energy dominates it. Exactly the same
domination absorbs the pole term.

## 3. How far from binding the negative direction is

By (2.17) the pole form contributes `+2|<cosh(x/2),f>|^2` on reflection-even
inputs and `-2|<sinh(x/2),f>|^2` on odd ones. Cauchy-Schwarz with
`||sinh(x/2)||^2_{L^2(I_L)} = sinh(L/2) - L/2` bounds the whole negative part
by `2(sinh(L/2) - L/2)`, which is a written proof and is the bound used in
Proposition 8.1.

The `galerkin_table` of the prime-free record gives the least Galerkin
eigenvalue of `A_L` by parity sector, and the column
`on_pole_free_hyperplane` gives it on `{<cosh,f> = <sinh,f> = 0}`, where `P_L`
vanishes. Reading the pole term off those columns:

```
   L      lam_min(A_L)   even     odd    pole-free hyperplane   2(sinh(L/2)-L/2)
  0.3        0.2193     0.2193   0.9290        0.9277               0.0011
  0.5        0.0346     0.0346   0.4137        0.4117               0.0052
  log 2      0.0029     0.0029   0.0778        0.0770               0.0140
  1.0        0.2567     0.5462   0.2567        0.2654               0.0422
  1.25       0.7968     1.2277   0.7968        0.8243               0.0830
  1.5        0.5528     1.0779   0.5528        0.6138               0.1446
  2.0        2.1213     2.8645   2.1213        2.3144               0.3504
  3.0        5.2249     6.8505   5.2249        6.1324               1.2586
  5.0       22.2196    29.5500  22.2196       28.5602               7.1004
```

Two readings.

**Below `log 2` the pole term's negative direction is not binding at all.** The
minimum sits in the *even* sector, where `P_L` is positive. Whatever makes
`A_L = Q_L` nearly degenerate as `L` approaches `log 2` — least eigenvalue
`0.0029` — is a direction on which the pole term *helps*.

**Above `log 2` the minimum moves to the odd sector, and admitting the negative
direction costs a small fraction of the margin.** The drop from the pole-free
hyperplane to the full odd sector is `0.0087` against `0.2654` at `L = 1`
(three per cent), `0.0275` against `0.8243` at `L = 5/4`, `0.19` against `2.31`
at `L = 2`, and `6.3` against `28.6` at `L = 5` (twenty-two per cent). The
worst-case Cauchy-Schwarz bound is larger still and is never close to the
margin either.

These Galerkin values are **one-sided**: a subspace minimum is an upper bound
for the true infimum, so they certify nothing about positivity. The
unconditional positivity of `A_L` outside `log 2 < L < log 7` comes from
Yoshida and Proposition 8.1, not from this table, and that is what finding 3
rests on. The table is a labelled illustration of *how far* from binding the
pole direction is.

I recomputed the parity split independently in a Fourier-Galerkin basis with
41 and 61 modes, rather than the record's 48 cells, with an independent
implementation of the gamma multiplier `b(tau^2)` and its quadrature, and
obtained `0.261 / 0.542 / 0.261` at `L = 1`, `0.799` at `L = 5/4`, `0.560` at
`L = 3/2`, `2.13` at `L = 2` and `22.5` at `L = 5` for the minimum, even and
odd values — agreeing with the record and with the manuscript's quoted figures.
That cross-check is floating point and lives outside the repository; it is
evidence that the recorded table is right, not a new certificate.

## 4. The corrected target

Strike item 1. What a candidate must now supply, at one `L`, is the first half
of Problem 8.3:

- **A positive source for `A_L`.** Its Gram form must be
  `K[E_L f] + c_L ||f||^2 + P_L[f]`: away from the diagonal the kernel is
  `-n_gamma(|x-y|) + 2 cosh((x-y)/2)`, which is smooth, and it contains **no
  prime translation whatever**. The candidate must produce the gamma kernel and
  the `cosh` kernel *together*, since neither alone is the target, and must
  produce the constant `c_L`, which is negative below `L ~ 2.6`.
- **Reflection covariance.** By Proposition 2.4 — whose proof only uses that
  every kernel is even in `x - y`, so it applies verbatim to `A_L` — any source
  carries a unitary `J` with `J Phi(f) = Phi(f(-.))` and `J^2 = id`, and the
  even and odd sectors decouple. A candidate whose pairing does not commute with
  `x -> -x` is excluded at once. This is the one part of the discarded test
  worth keeping.
- **Then, separately, the compression.** `sum_p Bt_p = <Gf, Pi Gf>` for a
  positive contraction `Pi` on the range of `G`. This is where the difficulty
  is, as Section 7.5 already says, and by Corollary 7.9 `||Pi|| <= 1` *is* Weil
  positivity.

A caution about the first item. `c_L` depends on the interval through the active
primes, and by Theorem 7.8 the prime set `P` may be any finite set containing
them, with different choices giving different `A_L`. Since
`sum_{p<X} kappat_p ~ 4 sqrt X`, there is no limiting prime-free form. So `A_L`
is per-interval data and a source for it is too; compatibility in `L` in the
sense of Corollary 2.2 is a separate requirement and cannot be met by letting
`P` be all primes.

And a caution about what would be proved. `A_L >= 0` is unconditional only
outside `log 2 < L < log 7`. On that window it is currently known only from RH,
so a construction there would be establishing something new rather than
realizing something known — not circular, but not free either. That makes the
parked item 4 of the continuation note more relevant to the construction
programme than "constrains no candidate theory" suggests: it is the difference
between building a source for a form known to be positive and building one for a
form whose positivity is open.

## 5. The correction the manuscript needs

In Section 8.2, the paragraph "The pole term needs a mechanism" should be
replaced. Its first two sentences are correct and should stay. The sentence
beginning "A realization must therefore contain a two-dimensional subspace with
a split inner product" should go, together with the ghost pair, the BRST doublet
and the indefinite-metric sector, and the closing claim that "locating a
protected sector with that structure is a better use of the next calculation
than a further prime-channel identity". What should replace them is that the
pole term is carried inside `A_L` by the same domination that absorbs the
negative contact, with the parity split and the bound
`2(sinh(L/2) - L/2)` as the quantitative statement — material that is already in
Proposition 8.1 and only needs to be pointed at the right conclusion.

Lemma 2.3 and Proposition 2.4 are correct and should be kept. Their real use is
Proposition 2.4's involution, which is a genuine necessary condition on any
source, and the parity split, which is what makes the pole term easy to bound.

## 6. Status of each claim

- The conflict in section 1 and the correction in section 2 are **written
  proofs**, from Corollary 2.2 and Proposition 7.3 as they stand.
- The bound `2(sinh(L/2) - L/2)` is a **written proof** (Cauchy-Schwarz), and is
  the manuscript's own.
- `A_L >= 0` outside `log 2 < L < log 7` is a **theorem**, Yoshida's and
  Proposition 8.1's, not established here.
- The table of section 3 is **one-sided Galerkin evidence**, reproduced from the
  existing record, plus an independent floating-point cross-check in a different
  basis. It certifies no positivity.
- No candidate sector was tested, because the criterion they were to be tested
  against does not hold. No new check programme was added.

## Appendix. The test as derived, for the record

Before the conflict above was noticed, the specification was reduced to
something cheap to compute, and the reduction is correct mathematics. It is
recorded here in case a candidate ever does present `P_L` as a separate summand,
which is the only situation in which it applies.

Given a candidate pairing `T` on a sector, a source `f -> s(f)`, and a
`T`-preserving involution `J` with `J s(f) = s(Rf)`: by (2.17) the whole
indefiniteness of `P_L` is an odd-sector, rank-one phenomenon, so the
requirement of a hyperbolic pair whose null lines are the two pole evaluations
is equivalent to

> **(T\*)** `T` restricted to reflection-odd inputs has **exactly one** negative
> direction, namely the functional `f -> <sinh(x/2), f>`, and restricted to even
> inputs is positive semidefinite with the extra positive direction
> `f -> <cosh(x/2), f>`.

One small Gram matrix per candidate, no arithmetic matching. The hyperbolic
pair is then recovered rather than assumed: let `e` and `o` be the `cosh` and
`sinh` directions, which are `T`-orthogonal because the parities decouple, and
scale them so `T(e,e) = -T(o,o)`; then `n_{1,2} = (e +/- o)/sqrt 2` are null,
pair nontrivially with each other, and are exchanged by `J`.

The first cut would have been the metric: a pairing positive definite on the
whole sector has no null vectors, so it fails outright, and a candidate handing
over its BRST cohomology has already quotiented away the structure. As it turns
out that cut disposes of the question itself, by disposing of the premise.

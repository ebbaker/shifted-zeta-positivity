# The prime-free archimedean inequality: what is a theorem, and where it is not

**Author: Claude Opus 5 (Anthropic), 15 September 2026.** Work on item 1 of
section 3 of [CONTINUATION_20260915.md](CONTINUATION_20260915.md). Not in the
working manuscript.

Supporting programme:
[`numerics/check_prime_free_archimedean.py`](../numerics/check_prime_free_archimedean.py),
record [`prime-free-archimedean-checks.json`](../numerics/records/prime-free-archimedean-checks.json).

Yoshida's 1992 paper was read directly for section 2; an earlier version of this
note relied on Connes and Consani's restatement of it and drew the wrong
conclusion. Section 2 now records both what Yoshida proves and how the
restatement differs.

## 0. Summary

The target was (8.1),

```
A_L[f] = K[E_L f] + ( w0 + sum_{p < e^L} kappat_p ) ||f||^2 + P_L[f]  >=  0,
kappat_p = 2 (log p)/(sqrt p + 1),    w0 = psi(1/4) - log pi = -5.37210...
```

Six findings.

1. **For `L <= log 2` the prime-free inequality is Weil positivity itself.** No
   prime is active there, so `A_L = Q_L` identically. The slack quoted in the
   continuation note (0.26 at `L = 1`) is entirely the mirror contact, which is
   zero below `log 2`. The least eigenvalue of `A_L` is non-increasing on
   `(0, log 2]` — for `L' > L` the test space `C_c^infty(I_L)` sits inside
   `C_c^infty(I_{L'})` and the form is the same one — and every sampled value
   above `log 2` exceeds `0.25`. The margin is smallest exactly at the top of
   the classical window, where it is about `1.4e-3`.
2. **That case is already a theorem: Yoshida (1992), Theorem 1.** His
   functional includes the two pole terms, he imposes no side condition, and
   his test space is *larger* than ours. So (8.1) holds for every `L <= log 2`,
   with strict definiteness. The proof is a computer-assisted numerical
   argument.
3. **Connes-Consani does not give it, and their restatement of Yoshida is not
   his Theorem 1.** Their `W_inf` is the archimedean local term with the pole
   contributions *excluded* — those sit on the spectral side of the explicit
   formula — and the `ghat(±i/2) = 0` they attach to Yoshida's theorem is what
   you must add to make the two functionals agree. That hypothesis is exactly
   `P_L[f] = 0`. Their own Theorem 1 adds `ghat(0) = 0` on top. So the
   compressed scaling action gives a conceptual proof on the subspace where the
   pole form vanishes; it does not give (8.1), and it is not needed for
   `L <= log 2`, where Yoshida already has the full statement.
4. **New theorem.** `A_L >= 0` for every `L >= log 7 = 1.9459...`,
   unconditionally, by an elementary argument with explicit constants
   (section 5).
5. **Hence the open range is exactly `log 2 < L < log 7`** — a compact window
   of length about 1.25, in which the Galerkin margins are of order 0.25 to 1.
6. **New certificate.** The archimedean form with the bare constant `w0` and no
   mirror contact is **not** positive for `L >= 3/4`: an explicit step function
   gives `-3.2e-3 ||f||^2`. Yoshida's window ends at `log 2 = 0.693`, so it is
   within 8 per cent of the largest window on which his form could have been
   positive at all. The mirror contact `kappat_2 = 0.574`, switching on at
   `log 2`, is what carries `A_L` past the point where the bare form dies.

Section 3 is the part of this work that bears on the construction problem: the
pole form is the **hyperbolic pairing of the two poles of `zeta`**, its null
lines are exactly the locus on which the results of section 2 are stated, and
every source for `Q_L` carries a canonical unitary involution — the
functional-equation involution `rho <-> 1 - rho` — in whose `-1` eigenspace the
subtraction must sit. That is item 4 of the continuation note, made explicit.
Section 7 has the recommendation.

## 1. `A_L = Q_L` below `log 2`

`kappat_p` is summed over `p < e^L`, and for `L <= log 2` there is no such
prime, so the constant is `w0`; the Weil prime term is likewise empty. Hence
`A_L = Q_L` on `C_c^infty(I_L)` for every `L <= log 2`, checked on random step
inputs against the independent `Step` routine of
[`check_channel_bound.py`](../numerics/check_channel_bound.py).

In a uniform cell basis (48 cells; a Galerkin space is a subspace, so these are
**upper** bounds for the true infimum and a positive value certifies nothing):

| L | 0.3 | 0.5 | 0.6 | log 2 (below) | log 2 (above) | 1.0 | 1.5 | 2 | 5 |
|---|---|---|---|---|---|---|---|---|---|
| `lambda_min(A_L)` | 0.219 | 0.0346 | 0.0090 | 0.0029 | 0.577 | 0.257 | 0.553 | 2.12 | 22.2 |

The jump at `log 2` is `kappat_2 = 0.5743`. Refining the cell count at
`L = log 2` gives 0.0188, 0.0067, 0.0029, 0.0020 for 12, 24, 48, 80 cells,
consistent with the `1.4e-3` obtained in the previous session's independent
Fourier-Galerkin computation.

## 2. What the literature proves

### 2.1 Yoshida 1992

H. Yoshida, *On Hermitian forms attached to zeta functions*, in Zeta Functions
in Geometry, Adv. Stud. Pure Math. **21** (1992), 281-325. His normalization,
from his section 0: for `F` admissible, `Phi(s) = int F(x) e^{(s-1/2)x} dx`,
`Fhat(t) = Phi(1/2 + it)`, and the explicit formula reads

```
sum_rho Phi(rho) = int F(x)(e^{x/2} + e^{-x/2}) dx  -  (log pi) F(0)
                 - sum_{p,m} (log p) p^{-m/2} (F(m log p) + F(-m log p))
                 + (1/2pi) int Fhat(t) Re psi(1/4 + it/2) dt .
```

Term by term this is our \eqref{eq:target}: the first term is `P_L`, the second
and fourth are `K + w0 ||f||^2`, and the third is the Weil prime term. He sets
`T(F) = sum_rho Phi(rho)` and defines the Hermitian form
`(phi_1, phi_2) = T(phi_1 * conj(phi_2)~)`, so **his form is `Q_L` exactly**,
pole terms included, with no side condition anywhere.

His test space is

```
C(a) = { phi in C_c^infty(R) : supp phi subset [-a,a] },
K(a) = { phi : phi = f on [-a,a], phi = 0 off [-a,a], f in C^infty of period 2a },
```

and `C(a) subset K(a)`, since a `C_c^infty` function supported in `[-a,a]`
extends `2a`-periodically to a smooth function. His `a` is the half-width of
the test function, so the autocorrelation `phi * phi~` is supported in
`[-2a, 2a]` and `2a` is our `L`.

> **Theorem 1 (Yoshida).** Let `a = (log 2)/2`. Then `(phi, phi) >= 0` for
> every `phi in K(a)`, with equality only for `phi = 0`.

That is `Q_L >= 0` for `L = log 2` on a space containing `C_c^infty(I_{log 2})`,
hence for every `L <= log 2`, hence **(8.1) for every `L <= log 2`**. It is
unconditional and there is no side condition. The proof (his section 6) is
computer-assisted: explicit tail estimates reduce the claim to positive
definiteness of one finite Hermitian matrix in each parity sector, which is then
verified numerically. He gives no spectral gap, only strict definiteness.

Three further results of his are worth recording here:

- **Proposition 1.** `T` is *oddly* positive definite iff RH holds; it is
  *evenly* positive definite iff every non-real non-trivial zero is on the
  critical line. Since `zeta` has no real zero in the critical strip, each
  parity sector separately carries RH.
- **Lemma 2.** `(phi,phi) > 0` on `K(a)` for all sufficiently small `a`, with
  no effective bound. This is the qualitative statement Suzuki and Bombieri
  quote; Theorem 1 is what makes it effective.
- **Proposition 6 and Theorem 2.** If RH fails there is a critical `a_0` with
  positivity below it and failure above; and RH holds iff the form is
  non-degenerate on the completion `K(a)^` for every `a`.

### 2.2 Connes-Consani 2021, and how their restatement differs

Their `W_inf := -W_R` is the archimedean *local* term. The pole contributions
`ftilde(0)` and `ftilde(1)` sit on the left of their explicit formula
`ftilde(0) - sum_rho ftilde(rho) + ftilde(1) = sum_v W_v(f)`, outside the local
terms. Their Theorem 1: for `g in C_c^infty` with support in
`[2^{-1/2}, 2^{1/2}]` and `ghat(i/2) = ghat(0) = 0`,
`W_inf(g * g^*) >= Tr(theta(g) S theta(g)^*) >= 0`, with `S` the projection on
Sonin's space; their Theorem 6.11 drops `ghat(0) = 0` at a cost
`-c |ghat(0)|^2`, `13 < c < 17`. The condition `ghat(i/2) = 0` is never dropped.

They restate Yoshida's Theorem 1 as: *for any smooth positive definite `f` with
support in `(1/2,2)` and Fourier transform vanishing at `±i/2`,
`W_inf(f) >= 0`.* Yoshida's Theorem 1 carries no such hypothesis. The
difference is exactly the pole term: for `f = F * Ftilde` one has
`fhat(i/2) = Fhat(i/2) conj(Fhat(-i/2))`, `fhat(-i/2)` its conjugate, and
`P_L[f] = fhat(i/2) + fhat(-i/2)`, so imposing `fhat(±i/2) = 0` deletes exactly
the term by which the two functionals differ. Their restatement is therefore
the corollary of Yoshida's theorem in their pole-free normalization, not his
theorem. What Connes and Consani contribute is a *conceptual* proof — they note
that Yoshida's is "a numerical analysis ... and therefore it does not provide
any conceptual reason for this positivity that would have a chance to continue
to hold when primes are involved" — at the price of two linear conditions.

For the inverse-bulk programme the distinction matters in one direction only.
Problem 8.2 asks for `A_L[f] = ||G f||^2` for **all** `f in C_c^infty(I_L)`, so
the pole directions are part of the domain and cannot be discarded; the
compressed scaling action, which needs them discarded, is therefore not the
tool for (8.1). But nothing is missing for `L <= log 2`, because Yoshida's
theorem covers it outright.

### 2.3 Others

Bombieri (2000) and Suzuki (2026) use the same pole-inclusive functional with no
side condition but state positivity only for "sufficiently small" support, with
no effective constant; Bombieri's introduction credits Yoshida with reducing the
question to a finite calculation and verifying it at `t = (log 2)/2`.

A recent preprint, [arXiv:2608.24827](https://arxiv.org/abs/2608.24827), takes
`2L <= log 2` as the classical baseline and attributes it to Yoshida. **That
attribution is correct** — an earlier draft of this note doubted it, wrongly.
Its further claim that Connes-Consani "re-proved this range" overstates their
theorem, which is conditional on `ghat(i/2) = 0`. The preprint is unrefereed and
its author name and affiliation changed between versions, so it should be read
rather than cited, but it is directly relevant to item 3 of the continuation
note: it claims certified two-sided bounds `8.9e-18 <= lambda_min <= 2.27e-17`
at our `L = 1.6`.

The manuscript's `references.tex` will need a Yoshida entry when it is next
revised.

## 3. The pole form, parity, and what a source must contain

This section is the part of the session's work that bears on the construction
problem rather than on the size of the target. Everything in it is elementary
and exact.

### 3.1 The two poles pair hyperbolically

Write

```
u[f] = Fhat(i/2)  = int f(x) e^{ x/2} dx,
v[f] = Fhat(-i/2) = int f(x) e^{-x/2} dx,
```

the evaluations of the transform at the two poles of `zeta`, at `s = 1` and
`s = 0`. Then `c[f] = <cosh(x/2),f> = (u+v)/2` and
`s[f] = <sinh(x/2),f> = (u-v)/2`, so

```
P_L[f] = 2|c|^2 - 2|s|^2 = 2 Re( u conj(v) )      ( = 2uv for real f ).
```

**In the coordinates `(u,v)` the pole form is purely off-diagonal.** Its matrix
is `[[0,1],[1,0]]`: the hyperbolic, or split, form of signature `(1,1)`, whose
two null lines are exactly `{u = 0}` and `{v = 0}` — the loci on which one of
the two poles is invisible.

Three things follow.

1. **The negative direction is not attached to either pole.** It is the
   antisymmetric combination `s = (u-v)/2`. No basis of the two pole states
   splits the pairing into a good pole and a bad one; the indefiniteness lives
   in the pairing *between* them.
2. **A realization must contain a hyperbolic pair, not a negative-norm state.**
   Any source with `||Phi(f)||^2 = Q_L[f]` must produce, on top of a positive
   background, a two-dimensional subspace carrying a split inner product whose
   two null vectors are the `s = 0` and `s = 1` evaluations. That is the
   structure of a ghost pair — a `bc` pair, a BRST doublet, a null pair in an
   indefinite-metric Fock space — and not of a single removed state. The
   manuscript's outlook offers "a ghost or BRST sector, a boundary condition
   that is not reflection positive, or a rank-two defect projection" as three
   alternatives; the first is not one alternative among three, it is a
   description of the algebra, and it says what must be paired with what.
3. **The literature's hypothesis is the null cone of this pairing.** The
   condition `fhat(±i/2) = 0` of section 2, under which Yoshida's and
   Connes-Consani's archimedean statements are formulated, says exactly that
   `uv = 0`, i.e. that the state lies on one of the two null lines. So those
   theorems describe the source restricted to the null cone of the pole
   pairing, which is the one place where the pairing carries no information.

### 3.2 Reflection, and the involution it induces on a source

`K`, `||.||^2` and every prime translation have kernels depending on `x - y`
through an even function, so `Q_L` and `A_L` commute with the reflection
`(Rf)(x) = f(-x)`; checked to `1e-11` on the form matrices, and also Yoshida's
section 2. Since `c` is `R`-even and `s` is `R`-odd, the pole form splits as

```
even sector:  +2|c|^2,        odd sector:  -2|s|^2,
```

so **the indefiniteness of `P_L` is entirely an odd-sector phenomenon and its
positive direction is entirely even.** Yoshida's (6.2) is this computation.

The constraint this puts on a source is sharper than a remark about symmetry.
Suppose `Phi` satisfies `||Phi(f)||^2 = Q_L[f]` on `C_c^infty(I_L)`. Then
`Q_L(Rf, Rg) = Q_L(f,g)`, so `f -> Phi(Rf)` has the same inner products as
`Phi`, and there is a unitary `J` on the closure of the range of `Phi` with

```
J Phi(f) = Phi(Rf),     J^2 = 1.
```

**Every source for the localized Weil form carries a canonical unitary
involution, and the hyperbolic pole pair must sit so that its positive
direction is in the `+1` eigenspace of `J` and its negative direction in the
`-1` eigenspace.** Equivalently: the subtraction may touch only the
reflection-odd part of the state.

Under Corollary 2.2 one can say what `J` is. A compatible realization is
unitarily equivalent to the evaluation map `Phi(f) -> (Fhat(gamma_rho))_rho`
on the zero multiset, `R` sends `Fhat(tau)` to `Fhat(-tau)`, and the multiset
`{gamma_rho}` is symmetric under `gamma -> -gamma` by the functional equation.
So **`J` is the involution `rho <-> 1 - rho` of the zeros**, and the two poles
`s = 0, 1` are exchanged by the same involution — they are the two extra points
of the same symmetry. The hyperbolic pair of section 3.1 is therefore not an
accident of normalization: it is the functional equation acting on the two
points it adds to the zero set.

Yoshida's Proposition 1 completes the picture: `T` is oddly positive definite
iff RH, and evenly positive definite iff every non-real zero is critical.
Since `zeta` has no real zero in the critical strip, **each eigenspace of `J`
separately carries RH**, so neither can be set aside as the easy one.

### 3.3 Where the difficulty sits, as two scalars

Let `W = K + c_L ||.||^2` be `A_L` without the poles, so
`A_L = W + 2cc^* - 2ss^*`. Two facts:

- `W` is **not** positive. The indicator of `I_L` gives
  `W[1_{I_L}]/||1_{I_L}||^2 = -0.285, -0.845, -1.217, -1.079, -0.786` at
  `L = 0.3, 0.5, log 2, 1, 3/2` (it turns positive by `L = 2`), an explicit
  certificate. The pole term is indispensable.
- `W >= 0` on `{c = 0}` in the even sector and on `{s = 0}` in the odd sector —
  the pole-free corollary of section 2.2, i.e. the null-cone statement of 3.1 —
  so `W` has at most one negative direction in each sector; the indicator
  certificate supplies one in the even sector, and the numerics give none in the
  odd sector. Hence `W` has exactly one negative eigenvalue and it is even
  (verified by symmetric elimination at every `L` tested).

With those inertia facts a positive rank-one perturbation moves exactly one
eigenvalue through zero, and

```
A_L >= 0   <=>   2 <cosh, (W^even)^{-1} cosh>  <=  -1        (even)
           and   2 <sinh, (W^odd)^{-1} sinh>   <=  +1        (odd).
```

In the 60-cell space:

| L | 0.3 | 0.5 | 0.6 | log 2 | 0.8 | 1.0 | 1.5 |
|---|---|---|---|---|---|---|---|
| even, needs `<= -1` | −1.625 | −1.039 | −1.008 | −1.0022 | −1.751 | −1.666 | −3.499 |
| odd, needs `<= +1` | 0.001 | 0.011 | 0.034 | 0.136 | 0.037 | 0.127 | 0.193 |

Refining at `L = log 2` the even scalar reads −1.00784, −1.00320, −1.00178,
−1.00148 at 20, 40, 80, 120 cells, apparently approaching about −1.0012. The
odd sector is comfortable and the even sector clears its threshold by about one
part in 800. This matches the shape of Yoshida's computation: his odd case
closes with a `10 x 10` matrix (`N = 10`), his even case needs a `200 x 200`
one (`N = 199`). The two-scalar form is a compact restatement of the
orthogonal-complement construction of his section 6, and it is the right object
to bound if one wants an effective version of his theorem.

## 4. Why `log 2` is nearly the true edge

Consider the **bare** archimedean form, constant `w0` for every `L` and no
mirror contact,

```
Abar_L[f] = K[E_L f] + w0 ||f||^2 + P_L[f].
```

`Abar_L = A_L = Q_L` for `L <= log 2`, and for larger `L` it is neither. Its
least Galerkin eigenvalue (40 cells) is

| L | log 2 | 0.72 | 0.74 | 0.75 | 0.80 |
|---|---|---|---|---|---|
| `lambda_min(Abar_L)` | +0.00355 | +0.00344 | +0.00354 | **−0.00323** | −0.0717 |

A negative value in a subspace **is** a certificate. The minimiser at
`L = 3/4`, rounded to four decimals, is retained in the record and gives
Rayleigh quotient `-3.2e-3`; since a function supported in `I_{3/4}` is
supported in every longer interval and `Abar` does not otherwise depend on `L`,

> **`Abar_L` is not positive for any `L >= 3/4`.**

So Yoshida's window `L <= log 2 = 0.6931` is within 8 per cent of the maximal
window `L <= L*`, `L* in (0.74, 0.75)`, for the archimedean-plus-pole form. His
choice of `(1/2,2)` is forced by the mathematics and not by convenience, and no
sharpening of his estimates could have extended it much.

The corollary for the subtraction programme: **`A_L` survives past `L*` only
because the mirror contacts switch on.** The first of them,
`kappat_2 = 0.574`, arrives at `L = log 2 = 0.693`, just below `L* ≈ 0.745`.
The mirror reference is not a convenience of bookkeeping; without it the
prime-free source would be non-positive from `L = 3/4` onwards and (8.1) would
be false.

## 5. A theorem for `L >= log 7`

Two elementary ingredients.

**(a) An interior bound for the gamma energy.** Splitting
`K[F] = (1/2) int int |F(x)-F(y)|^2 n_gamma(|x-y|)` according to whether `y`
lies in `I_L`, and using `F = 0` outside,

```
K[E_L f] = D_L[f] + int_{I_L} |f(x)|^2 h(x) dx,     D_L[f] >= 0,
h(x) = N(L/2 - x) + N(L/2 + x),   N(a) = int_a^inf n_gamma = sum_{n>=0} e^{-a_n a}/a_n.
```

`N` is convex and decreasing, so `h(x) >= 2 N(L/2)` on `I_L`, with `h -> +inf`
at the endpoints.

**(b) The pole form.** `2|c[f]|^2 >= 0` and, by Cauchy-Schwarz,
`2|s[f]|^2 <= 2 (sinh(L/2) - L/2) ||f||^2`, since
`||sinh(x/2)||^2_{L^2(I_L)} = sinh(L/2) - L/2`.

Therefore, with `c_L = w0 + sum_{p<e^L} kappat_p`,

```
(I)   A_L >= [ c_L + 2N(L/2) - (2 sinh(L/2) - L) ] ||f||^2,
```

and, keeping the endpoint blow-up of `h` and applying Cauchy-Schwarz in the
weighted space instead,

```
(II)  A_L >= 0   whenever   J(L) := int_{I_L} sinh^2(x/2)/(h(x) + c_L) dx <= 1/2,
```

which needs only `h(0) + c_L > 0`.

The three ingredients — `K[F] >= int |F|^2 h >= 2N(L/2)||F||^2`, the
Cauchy-Schwarz bound on `|s[f]|^2`, and the factorisation
`P_L[f] = 2 (int f e^{x/2})(int f e^{-x/2})` — are checked independently on
random step inputs by the programme; the first has slack at least `0.28` on
those inputs and the last is exact to `1.3e-15`.

Both criteria are monotone between consecutive primes: on a plateau `c_L` is
constant, `N(L/2)` decreases and `2 sinh(L/2) - L` increases, so the bracket in
(I) decreases; and in (II) the domain grows while `h(x)` decreases pointwise, so
`J` increases. **It is therefore enough to check the right endpoint of each
plateau.**

- Criterion (I) is checked at **all 78 497 prime breakpoints below `10^6`**. It
  first holds on the plateau of primes through 11 and holds at every later
  breakpoint; the minimum margin over that range is `0.5566`, attained at
  `L = log 13`. The ratio `c_L/(2 sinh(L/2) - L)` settles at `4.01`.
- For `X = e^L > 10^6`, partial summation with
  `theta(t) >= t(1 - 1/log t)` for `t >= 41` (Rosser-Schoenfeld 1962) gives
  `sum_{p<X} 2 log p/(sqrt p + 1) >= sum_{p<X} log p/sqrt p >= 1.8552 sqrt X + 62.96`,
  which exceeds `sqrt X - 1/sqrt X - log X + |w0|` for every `X >= 10^6`. Any
  explicit Chebyshev bound with constant above `1/2` would do; the margin is a
  factor of nearly two.
- Criterion (II) covers the remaining plateau `log 7 <= L < log 11`, where
  `h(0) + c_L > 0` first holds. `J` rises from `0.144` at `L = log 7` to
  `0.390` at `L -> log 11`, against the threshold `1/2`.

> **Theorem.** `A_L[f] >= 0` for every `f in C_c^infty(I_L)` and every
> `L >= log 7 = 1.945910...`

The proof is elementary and unconditional; its only external input is an
explicit Chebyshev lower bound for `theta`. Its finite part is a floating-point
evaluation of an explicit elementary inequality at 78 497 points with margins
above `0.55`, which is not interval arithmetic but is nowhere near the
resolution at which rounding could matter.

The criterion is lossy — it discards `D_L`, all of `2|c|^2`, and all correlation
structure — so its failure below `log 7` says nothing about `A_L`.

## 6. Status of each claim

| Claim | Status |
|---|---|
| `A_L = Q_L` for `L <= log 2` | Proved (trivially); checked numerically |
| `A_L >= 0` for `L <= log 2` | **Theorem (Yoshida 1992, Thm 1)**; computer-assisted |
| Parity split; poles even-positive, odd-negative | Proved; Yoshida section 2 and (6.2); checked to `1e-11` |
| `P_L` is the hyperbolic pairing of the two pole evaluations | Proved; checked to `1.3e-15` |
| Every source for `Q_L` carries a unitary involution `J`, and the subtraction sits in its `-1` eigenspace | Proved |
| `J` is the involution `rho <-> 1-rho` of the zeros | Proved given Corollary 2.2 |
| `W = K + c_L` is not positive for `L <= 3/2` | Proved (indicator certificate) |
| `Abar_L` not positive for `L >= 3/4` | Proved (explicit step certificate) |
| `W` has exactly one negative direction, and it is even | Proved given Yoshida; verified numerically |
| The two-scalar reduction of `A_L >= 0` | Proved given the inertia facts above |
| Values of the two scalars, `lambda_min(A_L)`, `L* in (0.74,0.75)` | Numerical only; Galerkin values are upper bounds |
| `A_L >= 0` for `L >= log 7` | Proved, modulo a finite floating-point verification and Rosser-Schoenfeld |
| `A_L >= 0` for `log 2 < L < log 7` | **Open** |

## 7. What I think should happen to item 1

1. **Close `L <= log 2` by citation.** It is Yoshida's Theorem 1, in our exact
   normalization and on a larger test space. Nothing is to be proved there, and
   the compressed-scaling-action machinery is not needed for it.
2. **Item 1 is now the compact window `log 2 < L < log 7`.** Margins there are
   0.25 to 1, and a proof would be a new unconditional statement, not a
   re-derivation. The natural tools are the two terms section 5 discards. The
   sharper of them is the interior Dirichlet form `D_L`: for `L <= 3.5` one has
   `n_gamma(r) >= 1/(2r)` on `(0,L]`, so
   `D_L[F] >= (1/4) int int_{I_L^2} |F(x)-F(y)|^2/|x-y|`, whose least eigenvalue
   on mean-zero functions is **scale invariant** — a single universal constant,
   computable once, that would then be available at every `L`. A crude
   substitute (`n_gamma(r) >= n_gamma(L)`) already carries the odd sector from
   about `L = 1.75`; the even sector is what needs the real constant.
3. **Item 4, the pole mechanism, is now a specification rather than a list.**
   By section 3 a source must contain a two-dimensional subspace with a
   hyperbolic inner product whose null vectors are the `s = 0` and `s = 1`
   evaluations, exchanged by a unitary involution `J` that acts on the rest of
   the source as the functional-equation involution `rho <-> 1 - rho`, with the
   subtraction confined to the `-1` eigenspace. That is a ghost pair with its
   pairing fixed, and it is the property to look for in a candidate protected
   sector — before any arithmetic matching is attempted.

A caution about item 3 of the continuation note. A certified lower bound on
`lambda_min(Q_L)` at `L = 1, 5/4, 3/2` is a larger undertaking than it looks:
the true values are around `1e-6` and below. A certified bound on `A_L`, which
is `O(1)` away from the two endpoints, is cheap by comparison and section 5
partly supplies it.

## 8. Loose ends

1. The universal mean-zero constant for the `1/|x-y|` energy on an interval
   (item 2 above). This is the one number that would let the section 5 argument
   reach down into the open window.
2. Prove `W^odd > 0` for `L <= log 2` directly. It is necessary for (8.1), it is
   the half of the problem that is not marginal, and it is a pole-free statement
   about the archimedean operator on odd functions.
3. An effective version of Yoshida's theorem — a lower bound for `A_L` on
   `L <= log 2` rather than strict definiteness — would follow from an upper
   bound on the even scalar of section 3 strictly below `-1`. He gives none, and
   a source construction may want one.
4. Add Yoshida to `references.tex` at the next manuscript revision.

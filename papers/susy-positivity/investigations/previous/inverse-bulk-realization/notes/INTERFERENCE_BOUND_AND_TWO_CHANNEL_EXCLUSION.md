# The interference bound and the two-channel exclusion

**Author: Claude Opus 5 (Anthropic), 15 September 2026.** Prepared in this
repository during a review of working manuscript 0.1. The results below were
written into manuscript 0.2 as Proposition 7.3, Lemma 7.4, Theorem 7.5 and
Remark 7.6; this note records the derivation, the numerical evidence, and the
parts that did **not** go into the manuscript.

Supporting programme: [`numerics/check_channel_bound.py`](../numerics/check_channel_bound.py),
record [`channel-bound-checks.json`](../numerics/records/channel-bound-checks.json).
Normalization check: [`numerics/check_explicit_formula.py`](../numerics/check_explicit_formula.py).

## 1. Where this came from

The [dressed-return note](SCHUR_DRESSED_RETURNS_AND_GLUING.md) ends at the
comparison

```
Q_L = K[E_L f]  +  sum_p B_{r_p,d_p}[E_L f]  +  R_L[f],
R_L[f] = (w0 - sum_p kappa_p) ||f||^2 + P_L[f],
```

with the observation that the first two terms are independently positive and
the residual "has not been realized as part of their joint norm". The question
this note answers is whether it *can* be.

## 2. The spectral scale of the problem

First, a fact that reframes everything and was missing from the investigation:
the explicit formula gives

```
Q_L[f] = sum over nontrivial zeros rho of  F^(gamma_rho) conj(F^(conj gamma_rho)),
gamma_rho = -i(rho - 1/2),   F = E_L f.
```

Verified numerically to ten digits by `check_explicit_formula.py`, which
computes the zero ordinates itself from the Hardy function. The consequence
that matters here is quantitative. For the smooth input
`F(x) = (1 + cos(2 pi x/L))/2`:

| L | gamma | contact | poles | primes | total | largest term / total |
|---|---|---|---|---|---|---|
| 2 | 2.404 | −4.029 | 2.066 | −0.441 | 2.90e−5 | 1.4e5 |
| 3 | 3.002 | −6.044 | 4.842 | −1.801 | 2.64e−6 | 2.3e6 |
| 4 | 3.405 | −8.058 | 9.109 | −4.456 | 1.45e−7 | 6.3e7 |

The quantity to be matched is smaller than each term being matched by five to
seven orders of magnitude. Any scheme that realizes the terms separately and
supplies the remainder afterwards is fighting that cancellation.

## 3. The bound

The whole obstruction is one line. For linear maps `G, S` into a common
Hilbert space, with `A = ||Gf||^2`, `B = ||Sf||^2` and `C` the interference
form `||(G+S)f||^2 - A - B`,

```
t A[f] + t^{-1} B[f] + C[f] = || sqrt(t) G f + t^{-1/2} S f ||^2 >= 0   (t > 0),
```

equivalently `-C <= 2 sqrt(AB)`, equivalently `||(G+S)f||^2 >= (sqrt A - sqrt B)^2`.

At `t = 1` this is just positivity of the total. Every other `t` is strictly
stronger, and that is what does the work. Read as a statement about the two
channel norms:

```
| sqrt(A[f]) - sqrt(B[f]) |  <=  sqrt(Q_L[f])    for every f.
```

Given the table in section 2, this says the two halves of any two-channel
realization must be **nearly identical forms**, agreeing to within the square
root of something of order 1e−7. That is not two sources added together; it is
one source minus its almost-complete projection.

## 4. The exclusion

Applied to the architecture above, with `A = K`, `B = sum_p B_p`, so `C = R_L`:

```
N_L(t)[f] := t K[E_L f] + t^{-1} sum_p B_p[E_L f] + R_L[f]  >=  0   for all t > 0.
```

This fails. The cleanest certificate is the **indicator of the interval**,
for which every quantity is a closed form:

```
K[1_{I_L}]   = 2 sum_{n>=0} (1 - e^{-a_n L}) / a_n^2  <=  psi'(1/4)/2,  a_n = 2n + 1/2
B_L[1_{I_L}] = sum_p [ kappa_p L - 2 d_p sum_{n d_p < L} r_p^n (L - n d_p) ]
P_L[1_{I_L}] = 32 sinh^2(L/4)
```

At `L = 5/4`, `t = 13/10`:

```
A = 4.302142,  B = 7.197439,  P = 3.228059,  kappa_2 + kappa_3 = 6.348275
N_L(1)      = Q_L[1_{I_L}] = +0.077067     (positivity holds)
N_L(13/10)                 = -0.293238     (the bound fails)
```

At `L = 1` the indicator is not enough (+0.054); the eight-cell step function
`(1,1,0,-1,-1,0,1,1)` with `t = 3/4` gives `-0.106621` against `Q_L[f] = +0.187826`.
For large `L`, `2 sqrt(A B) = O(L^{1/2} e^{L/4})` while
`-R_L = 4(L-2) e^{L/2} (1+o(1))` by the prime number theorem, so the failure
grows without bound. A grid scan at `t = sqrt(B/A)` shows failure at every
`L >= 1.1` up to `L = 6.5`.

Separately, **Proposition 7.3**: `c ||f||^2 + P_L` with `c < 0` equals `c ||f||^2`
on the codimension-two subspace where both pole moments vanish, so no further
independently positive channel adjoined orthogonally can supply `R_L` either.

## 5. How far the exclusion extends — the part not in the manuscript

The manuscript states the theorem for the specific pair `(K, sum_p B_p)` and
scopes it there. The natural repair is to let each channel carry a constant
and a share of the pole term,

```
A' = K + alpha ||f||^2 + sigma P_L,     B' = sum_p B_p + beta ||f||^2 + (1-sigma) P_L,
```

which leaves `C' = (w0 - sum kappa - alpha - beta) ||f||^2` automatically. This
does **not** restore feasibility. Minimizing over `t` with a grid fine enough to
resolve the optimum (which drifts to `t = 1` like `1/alpha` — a coarse grid
misleadingly reports success here), in a 61-dimensional Fourier Galerkin space
on `I_{5/4}`, taking the best `beta` for each `alpha`:

| alpha | 10 | 100 | 1e3 | 1e4 | 1e6 | 1e8 |
|---|---|---|---|---|---|---|
| best min over t | −2.6e−2 | −2.5e−3 | −2.6e−4 | −2.4e−5 | −2.0e−7 | −5.1e−8 |

The mechanism is transparent from section 3: inflating both channels by
`alpha` turns the requirement into `D[f]^2 / (4 alpha) <= Q_L[f]` with
`D = A' - B'` a fixed nonzero form, and `Q_L` has eigenvalues at the 1e−7
level and below. The floor at 5e−8 is the discretization, so this is strong
numerical evidence rather than a theorem: proving it for all `alpha` needs a
lower bound on `lambda_min(Q_L)` against `D`, which is the benchmark suggested
in section 7 below.

## 6. What is *not* excluded

- Any theory. This is arithmetic bookkeeping; nothing here concerns sphere
  quantization, Schur quantization, Yang-Mills, or any protected sector.
- The dressed Schur identity itself, which remains correct.
- A source whose channel norms are different forms `A'`, `B'` not of the shape
  above, for which the bound of section 3 is simply the first test to apply.
- **A source that is not a sum of two channels at all.** The bound is about
  `||(G+S)f||^2`. A difference `||G f||^2 - ||Pi G f||^2`, i.e. a compression,
  is not constrained by it. This is the escape, and it is pursued in
  [MIRROR_REFERENCE_AND_SUBTRACTION_FORM.md](MIRROR_REFERENCE_AND_SUBTRACTION_FORM.md).

## 7. Loose ends

1. Make the `alpha` scan of section 5 a theorem, or find the `alpha` at which
   it turns. This needs a rigorous lower bound on `lambda_min(Q_L)`.
2. A certified (interval-arithmetic) lower bound on `lambda_min(Q_L)` for
   `L = 1, 5/4, 3/2` would both confirm unconditional local Weil positivity
   there and give every future candidate an immediate numerical kill test.
   A plain Fourier Galerkin gives `3.3e-2` at `L = 1/2`, `1.4e-3` at
   `L = log 2`, `~1e-6` at `L = 1`, and below quadrature resolution beyond.
3. The number of `Q_L`-eigenvalues near zero grows with `L`; the
   Paley-Wiener count `L T / 2 pi` against the zero count `T log T / 2 pi`
   predicts the rate. Worth making precise, because it controls how hard
   every matching problem on `I_L` is.

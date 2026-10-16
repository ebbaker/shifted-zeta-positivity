# Collatz-Wielandt: where the cone does pay, and an elementary necessary condition

**Author: Claude Opus 5 (Anthropic).** 16 September 2026. Continues
[the jump-form note](PERRON_FROBENIUS_AND_THE_JUMP_FORM_20260916.md), whose §4
identified Collatz-Wielandt as the only cone theorem that can bound a spectral
radius. Checked by
[`check_collatz_wielandt.py`](../numerics/check_collatz_wielandt.py).

## 0. Summary

The cone is unusable on `Q_L`, whose pointwise positivity the pole term
destroys. But it is perfectly usable one level down. Splitting off the pole,

```
 Q_L = S_L + P_L ,      S_L := E_{mu_L} + gamma_L ||f||^2 ,
```

`S_L` is a **Z (Stieltjes type) operator** — symmetric, nonpositive off-diagonal
kernel, constant diagonal — so `S_L = d_L I - N_L` with `N_L >= 0` entrywise, and

```
 lambda_min(S_L) = d_L - rho(N_L),     rho = Perron root of N_L.
```

Four consequences.

1. **A single positive trial function brackets `lambda_min(S_L)` from both
   sides**, by Collatz-Wielandt. The pole never enters `N_L`.
2. **`S_L` has exactly one negative direction**, at every `L` tested, and that
   direction is essentially `cosh(x/2)` — which is precisely the *positive*
   direction of the pole form. The whole of Weil positivity is a rank-one
   near-cancellation between these two.
3. Hence an **elementary necessary condition**, proved below:
   `alpha_L := -lambda_min(S_L) <= 2 sinh(L/2) + L` for every `L`, if RH holds.
4. It is **sharp**: the relative margin falls from `9e-2` at `L = 1/2` to
   `2e-3` at `L = 4`, while both sides grow like `e^{L/2}`. So it is a genuine
   *disproof* test, not a vacuous one.

## 1. The Stieltjes split and the Perron root

`E_{mu_L}` has off-diagonal kernel `-mu_L` and `gamma_L` is diagonal, so `S_L`'s
off-diagonal kernel is `-mu_L <= 0` and its diagonal is constant in the cell
basis (verified). Writing `S_L = d_L I - N_L` makes `N_L` symmetric, entrywise
nonnegative, with zero diagonal, and

```
 lambda_min(S_L) = d_L - lambda_max(N_L) = d_L - rho(N_L),
```

`rho` being the Perron root because `N_L >= 0`. Note what has happened: the
archimedean density and the prime atoms are now the **kernel of a nonnegative
operator**, and everything indefinite has been moved into the two explicit
scalars `d_L` and `gamma_L` and into the rank-two `P_L`.

## 2. Collatz-Wielandt

For any strictly positive `u`,

```
 min_i (N_L u)_i / u_i  <=  rho(N_L)  <=  max_i (N_L u)_i / u_i ,
```

with equality at the Perron vector. Translated, at `L = 2` (exact
`lambda_min(S_L) = -4.3037`):

| trial `u` | bracket |
|---|---|
| `1` | `-4.7732 <= lambda_min(S_L) <= -3.8465` |
| `cosh(x/2)` | `-4.7686 <= ... <= -3.5056` |
| Perron vector | `-4.3037 <= ... <= -4.3037` |

So the constant function alone locates it within about 12 per cent, from one
evaluation and no spectral computation. **This is the first place in the
programme where the cone structure does work that the spectral theorem does not
do for free.**

## 3. One negative direction, and it is the pole's positive direction

`S_L` has exactly one negative eigenvalue at every `L` in `{1/2, 3/4, 1, 3/2, 2,
3, 4}` (counted by Sylvester's law). Its ground state `psi` has cosine
`|<psi, cosh(x/2)>| / ||cosh(x/2)||` equal to

| `L` | 0.5 | 0.75 | 1.0 | 1.5 | 2.0 | 3.0 | 4.0 |
|---|---|---|---|---|---|---|---|
| overlap | 0.9844 | 0.9918 | 0.9950 | 0.9979 | 0.9988 | 0.9997 | 0.9998 |

and `cosh(x/2)` spans the positive direction of `P_L` by (2.17). **So the single
negative direction of the prime-free-of-pole operator and the single positive
direction of the pole form are the same vector, to four digits.** That the count
is one is forced by RH — `n_-(S_L) <= n_-(Q_L) + n_-(-P_L) = 0 + 1` — so the
observation is a consistency check; that the two directions *coincide* is not
forced by anything, and is the sharpest statement I have of what the pole term
is for.

## 4. The necessary condition

> **Proposition.** Let `psi` be a unit ground state of `S_L` and
> `alpha_L = -lambda_min(S_L)`. If `Q_L >= 0` on `C_c^inf(I_L)`, then
> ```
>  alpha_L <= 2 |<cosh(x/2), psi>|^2 <= 2 ||cosh(x/2)||^2_{L^2(I_L)} = 2 sinh(L/2) + L.
> ```

*Proof.* `0 <= Q_L[psi] = <S_L psi, psi> + P_L[psi] = -alpha_L + 2|<cosh,psi>|^2
- 2|<sinh,psi>|^2 <= -alpha_L + 2|<cosh,psi>|^2` by (2.17); then Cauchy-Schwarz,
and `int_{-L/2}^{L/2} cosh^2(x/2) dx = L/2 + sinh(L/2)`. ∎

Numerically:

| `L` | 0.5 | 0.75 | 1.0 | 1.5 | 2.0 | 3.0 | 4.0 |
|---|---|---|---|---|---|---|---|
| `alpha_L` | 0.9138 | 1.4157 | 1.9863 | 3.0994 | 4.3037 | 7.2281 | 11.2285 |
| `2 sinh(L/2)+L` | 1.0052 | 1.5177 | 2.0422 | 3.1446 | 4.3504 | 7.2586 | 11.2537 |
| relative margin | 9.1e-2 | 6.7e-2 | 2.7e-2 | 1.4e-2 | 1.1e-2 | 4.2e-3 | 2.2e-3 |

The absolute margin stays near `0.03` while both sides grow like `e^{L/2}`, so
the relative margin decays like `e^{-L/2}`.

## 5. What this is, and what it is not

**It is a disproof test.** Collatz-Wielandt gives a *lower* bound on `alpha_L`
from any positive `u`, namely `(min_i (N_L u)_i/u_i - d_L)/h`. If that ever
exceeded `2 sinh(L/2) + L`, RH would be false. The test is rigorous for any
positive `u` (no spectral computation, no optimality needed), cheap, and would
be decisive if `u` were good to about one per cent — which power iteration
supplies. At `L = 2` the constant function already gives `alpha_L >= 3.85`
against a threshold of `4.35`.

**It is not a proof route.** The condition is necessary and not sufficient, and
its holding is consistent with RH rather than evidence for it. The obstruction
is the one identified in the jump-form note: Collatz-Wielandt certifies a
spectral radius *inside* a cone, and `Q_L` is not inside one. What §1 achieves
is to isolate the largest piece of the problem that *is* in a cone; the residue
is the rank-two pole, and that residue is exactly what the necessary condition
spends.

**A sharper version is available and unused.** The proof discards
`2|<sinh,psi>|^2` and then applies Cauchy-Schwarz. Keeping both gives
`alpha_L <= P_L[psi]`, which the check verifies and which is tighter (at `L = 3`:
`7.2281 <= 7.2525 <= 7.2586`). Making `P_L[psi]` explicit needs the ground state,
which is the Perron vector of `N_L`, so Collatz-Wielandt bounds it too.

## 6. Where the criticality lives

An exploratory computation (200 cells, not in the check program): the *second*
eigenvalue of `S_L`, the first above the single negative one, is
`0.414, 0.030, 0.0128, 0.00105, 0.00085, 0.00083, 0.00067` at
`L = 0.5, 0.8, 1, 1.5, 2, 3, 4`. So after its one negative direction `S_L` is
already nearly singular, and the near-degeneracy of `Q_L` is largely **inherited
from `S_L`** rather than created by the pole. The pole supplies a rank-one
cancellation of a single large negative eigenvalue; it does not produce the
criticality.

## 7. Next

1. **Push the necessary condition into the sibling manuscript.** It is proved,
   elementary, checked, and it is the first statement in this programme that
   could in principle be *violated*. It belongs next to Proposition 7.3.
2. **Sharpen the trial functions.** The gap between the constant function's
   bracket (12 per cent) and the true margin (1 per cent) is the whole distance
   between a vacuous test and a decisive one. A two-parameter family, or one
   step of power iteration from `cosh(x/2)`, should close most of it.
3. **Ask whether `alpha_L - (2 sinh(L/2) + L)` has an asymptotic.** The absolute
   margin looks flat near `0.03` over `L = 1` to `5`. If it has a limit, that
   limit is a new constant attached to the Weil form and worth identifying.
4. **The coincidence of §3 wants an explanation.** Why is the ground state of an
   operator built from the archimedean density and the prime atoms
   asymptotically `cosh(x/2)`, the pole direction? A proof of that would make
   the rank-one cancellation structural rather than numerical.

## 8. The disproof test, run

**Method.** `S_L` is symmetric **Toeplitz** in the cell basis, so `N_L` is too,
matrix-vector products are FFT circulant embeddings, and `alpha_L` is
`(lambda_max(N_L) - d_L)/h` with `lambda_max` of a nonnegative operator -- the
easy end for Lanczos. The gamma column is summed adaptively (the term count
needed at offset `i` falls like `1/i`, with an explicit `psi'` tail correction at
`i = 1` without which every value is off by a constant `0.0125`); each prime
power touches only two entries of the column, since the triangle overlap has
width one cell. A column build plus eigensolve at `m = 4000` takes 0.2 s.

**Why the discretisation is safe in the right direction.** The cell span is a
*subspace* of `L^2(I_L)`, so the Galerkin minimum is at least the continuum
minimum and `alpha^{(m)}_L <= alpha_L`. **Every computed value is a rigorous
lower bound on the true `alpha_L`** -- which is the direction a disproof needs.
Convergence checked against a dense build: at `L = 1`, `alpha^{(m)}` is
`1.9873106, 1.9874609, 1.9874827, 1.9874884, 1.9874935` for
`m = 250, 1000, 4000, 16000, 64000`.

**Result.** A scan of **7713 values of `L` in `[1/2, 10]`** at `m = 4000`, with
every prime-power threshold sampled at `+1e-7`, `+1e-3` and `+2e-2` as well as a
uniform grid:

> **No crossing.** The least absolute margin is `0.0187` at `L = 5.3396`
> (relative `9.5e-4`); the least relative margin is `3.2e-4`, near `L = 10`.

The ten smallest margins all sit in `L in [3.5, 6.3]`. The absolute margin does
**not** tend to zero -- it oscillates in roughly `[0.019, 0.09]` across the whole
range, while both sides grow like `e^{L/2}`, so the relative margin decays like
`e^{-L/2}`.

**Reading.** The test was run and did not disprove RH, which is the expected
outcome and is not evidence for RH. What it does establish is that the condition
is **not asymptotically tight**: an absolute margin bounded away from zero means
\eqref-style (N) is genuinely weaker than Weil positivity, and by a fixed
amount, which is consistent with §5's account of why it is not sufficient. A
condition that had closed up would have been the interesting outcome.

**Caveat.** Floating point throughout, with a Lanczos tolerance of `1e-12` and a
discretisation error near `1e-5` at `m = 4000` -- both far below the `0.0187`
margin, but this is not interval arithmetic and is not a certificate. The scan
is an exploratory computation and is not among the registered check programs;
the registered one verifies the condition at seven values of `L`.

## 9. Status

- §1's Z structure, the constancy of the diagonal, and the Perron identity:
  **proved** (elementary) and verified.
- §2: Collatz-Wielandt is standard; the brackets are exact computations.
- §3: the count `n_-(S_L) = 1` is **forced by RH** and verified; the overlap
  figures are **numerical**, in one discretisation, and the coincidence they
  record is **not proved**.
- §4's Proposition is **proved** here; the table is numerical.
- §5 and §7 are assessment. §6 and §8 are exploratory computations, deliberately
  labelled as outside the registered checks.
- §8's monotonicity claim (Galerkin values are lower bounds for the continuum
  `alpha_L`) is **proved** and is what makes the scan meaningful.

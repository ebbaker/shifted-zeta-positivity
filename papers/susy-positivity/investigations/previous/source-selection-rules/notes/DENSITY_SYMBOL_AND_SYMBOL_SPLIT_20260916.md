# The archimedean symbol is the smooth zero density, and what that does to the compression

**Author: Claude Opus 5 (Anthropic).** 16 September 2026. First note of this
investigation. Checked by
[`check_density_symbol.py`](../numerics/check_density_symbol.py) and
[`check_symbol_split.py`](../numerics/check_symbol_split.py).

Equation numbers are those of the inverse-bulk working manuscript 0.5,
[`../../inverse-bulk-realization/manuscript.tex`](../../inverse-bulk-realization/manuscript.tex).

## 1. The identity

By (2.6) and (2.7),

```
 b(tau^2) = Re psi(1/4 + i tau/2) - psi(1/4),      w0 = psi(1/4) - log pi,
```

so their sum is

```
 b(tau^2) + w0 = Re psi(1/4 + i tau/2) - log pi.                          (1)
```

The Riemann-Siegel theta function is `theta(t) = arg Gamma(1/4 + it/2) - (t/2) log pi`,
whence `theta'(t) = (1/2) Re psi(1/4 + it/2) - (1/2) log pi`, and (1) reads

> **Density identity.** `b(tau^2) + w0 = 2 theta'(tau)`.

The smooth part of the Riemann-von Mangoldt counting function is
`Nbar(T) = theta(T)/pi + 1`, with density `Nbar'(T) = theta'(T)/pi`. Since
`K[F] = (1/2pi) int b(tau^2) |F^|^2` by (2.5)-(2.6) and
`w0 ||f||^2 = (1/2pi) int w0 |F^|^2` by Plancherel,

```
 K[E_L f] + w0 ||f||^2 = int_R |F^(tau)|^2 dNbar(tau).                     (2)
```

**The gamma energy together with the contact is integration against the smooth
zero-counting measure.** Nothing is estimated: (2) is two lines from equations
already in the manuscript. It is verified in
`check_density_symbol.py`, which computes the two sides by different routines
(a partial-fraction digamma against a Stirling `log Gamma` differentiated
numerically) so the agreement is not definitional.

## 2. Four consequences

**(a) The contact needs no mechanism of its own.** Section 7.4 and the sibling
investigation's continuation notes treat "the contact must arise by projection"
as a debt a candidate owes. By (2) the contact is the `-log pi` inside `theta'`:
it is the normalisation of the zero density, not an additional constant. A
candidate with the right `log|tau|` slope and the wrong intercept does not have
a small error; it has the wrong density of states.

**(b) The target, arranged by mechanism.** With the explicit formula
(Corollary 2.2),

```
 int |F^|^2 dNbar  +  P_L[f]  -  2 sum (log p) p^{-m/2} Re<F, U_{m log p} F>
 = sum_rho |F^(gamma_rho)|^2 .
```

The archimedean half is a **density of states**; the prime half is the
**fluctuation `S`**, whose natural mechanism is a periodic-orbit sum with
primitive periods `log p`; and the pole term is the `+1` in
`Nbar = theta/pi + 1`, the two points the functional equation adds. This makes
precise the observation that the two halves call for different physical
mechanisms while Theorem 7.5 forbids them from being two channels.

**(c) All archimedean negativity is in a low band that shrinks with `L`.** `Nbar`
*decreases* below `tau_* = 6.28984...` (compare `2pi = 6.28319`), so (2) is a
**signed** measure. In the subtraction form of Theorem 7.12 the source-side
symbol is

```
 sigma_L(tau) = b(tau^2) + w0 + sum_{p < e^L} kappat_p = 2 theta'(tau) + Sigma_L,
```

negative exactly on `|tau| < tau_L`:

| `L` | 0.8 | 1.0 | 1.25 | 1.5 | 2.0 | 2.5 | `> log 13` |
|---|---|---|---|---|---|---|---|
| `c_L` | -4.798 | -4.798 | -3.994 | -3.994 | -1.932 | -0.821 | `> 0` |
| `tau_L` | 3.5504 | 3.5504 | 1.6396 | 1.6396 | 0.4745 | 0.2520 | none |

**(d) The sign change at `p = 13` has a meaning.** `c_L = sigma_L(0) = 2 theta'(0) + Sigma_L`,
so `c_L > 0` is exactly `Sigma_L > -w0 = 5.3721834...`: the summed prime contacts
overtake the **maximum negativity of the smooth zero density**. That is why the
crossing sits at `p = 13` and nowhere else.

## 3. The symbol split

Proposition 7.14 moves the whole constant `(c_L)_-` to the subtracted side, at
every frequency. By 2(c) only the band `|tau| < tau_L` has to move.

> **Proposition (symbol split).** Let `sigma_L^± = max(±sigma_L, 0)` and define
> on `C_c^inf(I_L)`
> ```
>  K_+^new[f] = (1/2pi) int sigma_L^+(tau) |F^(tau)|^2 dtau + 2 |<cosh(x/2), f>|^2,
>  T_L^new[f] = (1/2pi) int sigma_L^-(tau) |F^(tau)|^2 dtau + 2 |<sinh(x/2), f>|^2
>               + sum_{p in P} Bt_{r_p,d_p}[E_L f].
> ```
> Then `Q_L = K_+^new - T_L^new` identically; `K_+^new` is a norm and `T_L^new`
> is positive, each term by term; and `K_+^new <= K_+` of (7.21), strictly
> except at `tau = 0`. Consequently `Q_L >= 0` on `I_L` if and only if
> `T_L^new <= K_+^new`.

*Proof.* Start from Theorem 7.12, `Q_L = A_L - sum_p Bt_p` with
`A_L = K + c_L ||f||^2 + P_L`. By (2) the first two terms of `A_L` form the
Fourier multiplier with symbol `sigma_L`; split it as `sigma_L^+ - sigma_L^-` and
split `P_L` by parity using (2.17). Both multipliers have nonnegative symbols,
so both are positive forms; `|<sinh,f>|^2` and each `Bt_p` are positive by
(7.19). For the comparison, `sigma_L^-` attains `(c_L)_-` only at `tau = 0`
because `2 theta'` is strictly increasing on `tau > 0`, and `K_+ - K_+^new` is
the multiplier with symbol `(c_L)_- - sigma_L^- >= 0`. ∎

Proposition 7.14 is the special case in which `sigma_L^-` is replaced by the
constant `(c_L)_-` everywhere.

### What it buys, measured

`check_symbol_split.py` assembles both presentations independently on 48
indicator cells, verifies both identities to machine zero, certifies positivity
by Cholesky, and bisects for the least generalized eigenvalue:

| `L` | `lambda_min` (7.14) | `lambda_min` (split) | ratio |
|---|---|---|---|
| 0.8 | 3.679e-4 | 1.447e-3 | 3.93 |
| 1.0 | 3.683e-4 | 1.251e-3 | 3.40 |
| 1.25 | 2.814e-4 | 6.842e-4 | 2.43 |
| 1.5 | 2.648e-4 | 5.681e-4 | 2.15 |
| 2.0 | 1.814e-4 | 2.449e-4 | 1.35 |
| 2.5 | 1.894e-4 | 2.111e-4 | 1.11 |
| 3.0 | 1.147e-4 | 1.147e-4 | 1.00 |

These are one-sided subspace values in a coarse cell basis; only the ratio is
the point. In a 400-cell basis the absolute values fall to `1.9e-6` at `L = 1`
with the same ratio, so the improvement is a constant factor and **not** a
change of kind: the domination stays saturated and the contraction stays
critical.

### Verdict

The split should replace Proposition 7.14's presentation, with 7.14 kept as the
special case, for three reasons that are not the factor of four: the constant
`w0` never appears as an independent object; for `L > log 13` the subtracted
side is *only* the odd pole term and the mirror prime references, with no
constant at all; and the band that has to move is explicit, shrinking, and tied
to a classical function rather than to a bookkeeping choice.

## 4. Status

- The density identity and (2): **proved** here, two lines from (2.5)-(2.7) plus
  Plancherel, and verified numerically to 16 digits. The identification of
  `theta'/pi` with the smooth counting density is classical.
- 2(c), 2(d) and the `tau_L` table: **proved**; the table is a root-find of an
  explicit function.
- 2(b): a rearrangement of the explicit formula, **not new mathematics**.
- The symbol-split proposition: **proved** above; the `lambda_min` table is
  **numerical and one sided**, in a 48-cell subspace.
- The closed-form Toeplitz gamma energy used by the check is **proved** (the
  triangle overlap has Laplace transform `4 sinh^2(ah/2)/a^2`) and agrees with
  direct quadrature of (2.5) to `1e-14`.

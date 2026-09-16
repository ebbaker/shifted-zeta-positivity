# Non-constructive existence, and the archimedean symbol as the smooth zero density

**Author: Claude Opus 5 (Anthropic).** 16 September 2026. Continuation of
[the bottleneck note](BOTTLENECK_AND_OPERATOR_SEARCH_20260916.md), investigating
the two directions singled out there: non-constructive existence (§4D of that
note) and the OPE (§4F).

Manuscript references are to
[`investigations/inverse-bulk-realization/manuscript.tex`](../../investigations/inverse-bulk-realization/manuscript.tex),
version 0.5. Status of every claim is in §8.

---

## 0. What came out of it

Six things, in rough order of how much they change the picture.

1. **`b(tau^2) + w0 = 2 theta'(tau)` exactly**, where `theta` is the
   Riemann-Siegel theta function. So the gamma energy together with the contact
   is exactly integration against the **smooth zero-counting measure**. The
   contact constant `w0` is not an independent object requiring a mechanism; it
   is the `-log pi` inside `theta'`. (§1)
2. Consequently the whole target reads **smooth zero density + the two poles -
   the fluctuation `S` = the actual zeros**. The prime term *is* `S`. (§1.3)
3. A **sharper compression presentation** than Proposition 7.14: split the
   archimedean form by the sign of its *symbol* rather than by the constant.
   Only a low band `|tau| < tau_L` moves to the subtracted side, and the band is
   empty for `L > log 13`. Gains a factor of four in `lambda_min` at `L <= 1`.
   It does not remove the criticality. (§2)
4. A **graded OPE checklist** with three falsifiable coefficients rather than
   one: `log(tau/2pi)`, then exactly zero at order `tau^{-1}`, then `-1/24` at
   order `tau^{-2}` (and `-7/960` at `tau^{-4}`). All verified numerically. (§3)
5. **Non-constructive existence of a realization is exactly RH** and cannot be
   shortcut. What *is* available is (N1) rigidity, (N2) family exclusion by
   invariants, and (N4) a **finite-moment shortcut**: if a model's pairing is
   known a priori to lie in a classified finite-dimensional cone, checking `n`
   moments proves the whole identity. (§4)
6. The classifications deliver (N4) and simultaneously bound it. **Klyuev,
   Proposition 5.5:** a `g_t`-twisted trace on a generalized `q`-Weyl algebra is
   determined by its `n` values `T(1), ..., T(Z^{n-1})`, where `n` is the number
   of nonzero roots of the Laurent polynomial `P`. So the infinite identity
   collapses to `n` numbers — and the same `n` is a hard budget on how many
   prime translations one copy of the algebra can carry. (§5). Independently,
   Bloch-lifted circle weights give **bounded periodic** multipliers with
   **purely atomic** off-diagonal kernels, and the archimedean symbol is
   unbounded with a **continuous** off-diagonal kernel — a family exclusion of
   type (N2). (§6)

---

## 1. The archimedean symbol is the smooth zero density

### 1.1 The identity

By (2.6), `b(tau^2) = Re psi(1/4 + i tau/2) - psi(1/4)`, and by (2.7),
`w0 = psi(1/4) - log pi`. Adding,

```
 b(tau^2) + w0 = Re psi(1/4 + i tau/2) - log pi = 2 theta'(tau),
```

since `theta(t) = arg Gamma(1/4 + it/2) - (t/2) log pi` gives
`theta'(t) = (1/2) Re psi(1/4 + it/2) - (1/2) log pi`. Verified to 16 digits.

The smooth part of the Riemann-von Mangoldt counting function is
`Nbar(T) = theta(T)/pi + 1`, so `Nbar'(T) = theta'(T)/pi` and

```
 K[E_L f] + w0 ||f||^2
   = (1/2pi) int_R [ b(tau^2) + w0 ] |F^(tau)|^2 dtau
   = int_R |F^(tau)|^2 dNbar(tau).                                    (*)
```

Both steps are Plancherel plus (2.5); nothing is estimated. The manuscript
already has every ingredient — (2.6), (2.7), (2.13) — and does not take this
last step.

### 1.2 Three immediate consequences

**(a) The contact is not a separate problem.** Section 7.4 and the continuation
notes treat "the contact must arise by projection" as one of the things a
mechanism owes. By (*) the contact is the `-log pi` in `theta'`: it is the
normalisation of the zero density, not an extra constant. A candidate that
produces the right `log|tau|` growth with a different constant is not "close" —
it has the wrong density of states.

**(b) All archimedean negativity is confined to a low band, and the band
shrinks with `L`.** `Nbar` is *decreasing* below `tau = 6.2898...` (where
`2 theta'` vanishes; compare `2pi = 6.2832`), so (*) is a **signed** form. In
the subtraction presentation the source-side symbol is

```
 sigma_L(tau) = b(tau^2) + w0 + sum_{p < e^L} kappat_p = 2 theta'(tau) + Sigma_L,
```

which is negative only on `|tau| < tau_L`, where

| `L` | 0.8 | 1.0 | 1.25 | 1.5 | 2.0 | 2.5 | > log 13 |
|---|---|---|---|---|---|---|---|
| `tau_L` | 3.550 | 3.550 | 1.640 | 1.640 | 0.475 | 0.252 | none |

**(c) The sign change at `p = 13` has a meaning.** `c_L = sigma_L(0) = 2 theta'(0) + Sigma_L`,
so `c_L > 0` is exactly `Sigma_L > -w0 = 5.3722`: the summed prime contacts
overtake the maximum negativity of the smooth zero density. That is why the
crossing is at `p = 13` and not somewhere else.

Put (b) and the previous note together: **all the negativity lives below
`tau_L <= 3.55`, and all the criticality lives below `gamma_1 = 14.13`.** The
primes are elsewhere.

### 1.3 The target, restructured

With (*) and Corollary 2.2,

```
 int |F^|^2 dNbar   +   P_L[f]   -   2 sum (log p) p^{-m/2} Re<F, U_{m log p} F>
 \___ smooth ___/       \_ poles _/   \________ the fluctuation S ________/
                                 =  sum_rho |F^(gamma_rho)|^2 .
```

This is the explicit formula, but arranged so that each physical mechanism is
visible: the archimedean half is a **density of states**, the prime half is the
**fluctuation `S`**, whose natural mechanism is a periodic-orbit sum with
primitive periods `log p`, and the poles are the `+1` in `Nbar = theta/pi + 1`.
The previous note's remark that the two halves call for two different mechanisms
while Theorem 7.5 forbids two channels is now an exact statement rather than an
impression.

---

## 2. A sharper compression: split by the sign of the symbol

Proposition 7.14 moves the whole constant `(c_L)_-` to the subtracted side, at
every frequency. By §1.2(b) only the band `|tau| < tau_L` needs to move.

**Proposition (symbol split).** Let `sigma_L^± = max(±sigma_L, 0)` and put

```
 K_+^new[f] = (1/2pi) int sigma_L^+(tau) |F^|^2 dtau + 2 |<cosh(x/2), f>|^2,
 T_L^new[f] = (1/2pi) int sigma_L^-(tau) |F^|^2 dtau + 2 |<sinh(x/2), f>|^2
              + sum_{p in P} Bt_{r_p,d_p}[E_L f].
```

Then `Q_L = K_+^new - T_L^new` identically, both sides are positive term by
term, and `K_+^new <= K_+` of (7.21) with strict inequality wherever
`sigma_L^- < (c_L)_-`, that is everywhere except `tau = 0`.

*Proof.* Identical to Proposition 7.14 except that the constant is absorbed into
the symbol before splitting; `(c_L)_- ` is the value of `sigma_L^-` at `tau = 0`
and `sigma_L^-` decreases to zero at `tau_L`. Positivity of a Fourier multiplier
with nonnegative symbol is immediate.

**Numbers** (my own 400-cell implementation, identity verified to `1e-10`):

| `L` | `c_L` | `tau_L` | `lambda_min` old | `lambda_min` new | gain |
|---|---|---|---|---|---|
| 0.8 | -4.798 | 3.550 | 3.18e-5 | 1.26e-4 | x4.0 |
| 1.0 | -4.798 | 3.550 | 1.91e-6 | 7.19e-6 | x3.8 |
| 1.25 | -3.994 | 1.640 | (noise) | (noise) | — |
| 1.5 | -3.994 | 1.640 | (noise) | (noise) | — |
| 2.0 | -1.932 | 0.475 | 1.81e-7 | 2.45e-7 | x1.35 |
| 2.5 | -0.821 | 0.252 | 5.69e-7 | 6.35e-7 | x1.12 |
| 3.0 | +2.498 | none | — | — | no split needed |

**Honest verdict.** This is a cleaner presentation with a small quantitative
gain, not a change of kind: the domination is still saturated to six digits, and
the contraction is still critical. What it buys is conceptual — the constant `w0`
never appears as an independent object, the subtracted side for `L > log 13` is
*only* the odd pole term and the mirror prime references with no constant at
all, and the low band where anything has to move is explicit and shrinking. I
think it should replace Proposition 7.14's presentation in the manuscript, with
7.14 kept as the special case.

---

## 3. A graded OPE checklist

The previous note gave one OPE-level condition (marginal `Delta = 1/2` kernel,
unit log coefficient). (*) grades it. Stirling for `theta'` gives, and I have
checked numerically to five digits at `tau = 20 ... 1000`,

```
 b(tau^2) + w0 = log(tau / 2pi) + 0 * tau^{-1} - (1/24) tau^{-2}
                 + 0 * tau^{-3} - (7/960) tau^{-4} + ...
```

Four separate falsifications, each cheap:

1. **Leading log with unit coefficient.** Marginal, `Delta = 1/2`, borderline
   Gagliardo exponent.
2. **The constant is `-log 2pi`.** This is the contact. A candidate with the
   right slope and the wrong intercept has the wrong density of states.
3. **No `tau^{-1}` term.** Equivalently the symbol is even in `tau` —
   the reflection symmetry of Proposition 2.4 seen in the expansion.
4. **`-1/24` at order `tau^{-2}`**, then `-7/960` at `tau^{-4}`.

Any candidate whose smeared two-point function has a spectral weight failing one
of these is excluded before a single prime is computed. Conditions 2-4 are new;
condition 1 alone is weak, because "has a logarithm" is common.

The limitation from the previous note stands and is now sharper: the OPE sees
only the density `Nbar`, never the fluctuation `S`. Prime atoms sit at fixed
non-coincident separations and are invisible to any short-distance expansion.

---

## 4. Non-constructive existence: what is and is not available

### 4.1 The circularity, stated once

A realization is a linear `Phi` into a **positive** Hilbert space with
`||Phi(f)||^2 = Q_L[f]`. Its existence implies `Q_L >= 0` implies RH. So:

> Any proof, constructive or not, that a realization exists is a proof of RH.

There is no version of "prove existence without computing the operator" that
escapes this. In particular Corollary 7.9 already manufactures `V` and `P` from
the dilation theorem the moment `||Pi|| <= 1` — and `||Pi|| <= 1` *is* the Weil
criterion. Abstract operator theory applied to the target alone returns exactly
its input.

### 4.2 The taxonomy

What remains, and it is not nothing:

**(N1) Rigidity — what a realization must look like *if* it exists.**
Unconditionally provable, and the investigation already has three: Corollary 2.2
(unique up to unitary; it is evaluation on the zeros), Proposition 2.4 (every
source carries the reflection involution `J`), Proposition 3.4 (the source is
unbounded relative to the input `L^2` norm). These cost nothing and they are
what actually kills candidates. More of them is the highest-yield
non-constructive work available.

**(N2) Family exclusion — an invariant of an achievable cone that the target
violates.** Also unconditional, and *stronger* than the exclusions currently in
the manuscript, which all exclude one specified preparation. Template: identify
a quantity preserved by every construction in a family, compute it for the
target, show they differ. §6 below carries this out for the Bloch-lift family.

**(N3) Existence of the realization.** Equivalent to RH. Unavailable. Do not
spend time here.

**(N4) Finite-moment determination — the one real shortcut.**

> **Principle.** Suppose a model's pairing is known *a priori* to lie in a cone
> `C` of positive forms that has been classified and embeds in `R^n`. Then two
> elements of `C` agreeing on `n` independent linear functionals coincide.
> Verifying the Weil identity on `n` inputs verifies it on all of them.

This is the honest content of "existence without explicit computation": not
dodging the construction, but **collapsing an infinite identity to `n` numbers**.
The premise — membership in a classified cone — has to come from the model, and
that is exactly the kind of statement a protected sector can supply.

---

## 5. What the classifications actually give

I read the two references the manuscript already cites at Section 3.3.

### 5.1 Klyuev, generalized `q`-Weyl algebras (SIGMA 18 (2022), 009)

This is the directly relevant one: the elementary representation used in
Section 6.1 is the `q`-Weyl example of Ambrosino-Gaiotto. The algebra `A` has
generators `u, v, Z, Z^{-1}` with

```
 Z u Z^{-1} = q^2 u,   Z v Z^{-1} = q^{-2} v,   uv = P(q^{-1} Z),   vu = P(q Z),
```

`P` a Laurent polynomial. An invariant Hermitian form satisfies
`(Za,b) = (a, b Z^{-1})`, `(ua,b) = (a, s b v)`, `(va,b) = (a, s^{-1} b u)` with
`|s| = 1`.

- **Proposition 2.1.** The space of `g_t`-twisted traces has dimension `n`, the
  number of nonzero roots of `P` counted with multiplicity. **Finite.**
- **Proposition 5.5.** `T -> (T(1), T(Z), ..., T(Z^{n-1}))` is an isomorphism
  from the space of `g_t`-twisted traces onto `C^n`. **A trace is determined by
  `n` numbers.**
- **Theorem 4.7.** The cone `C_+` of positive definite `rho_t`-equivariant
  traces is isomorphic to `C_l x R^r_{>0}`, with `l` the number of roots
  `alpha` with `q < |alpha| < q^{-1}` and `r` the number of distinct roots with
  `|alpha| = q`, and explicit positivity conditions (quasi-periodicity plus
  pointwise nonnegativity of two theta-type functions).

### 5.2 EKRS, quantized Kleinian singularities of type A (SIGMA 17 (2021), 029)

Classifies unitary short star-products, with explicit integral formulas for the
traces and, notably, **uniqueness for `n <= 4`**. The cones here are not merely
finite-dimensional but in small cases a point.

### 5.3 What this gives the programme, in both directions

**The positive direction (N4).** If a candidate's pairing is a twisted trace on
a generalized `q`-Weyl algebra, it is fixed by `n` numbers. The Weil identity on
`I_L` — an identity between two infinite families of correlations — would follow
from matching `T(1), ..., T(Z^{n-1})`. That is the shortcut, and it is real.

**The negative direction, and it is the sharper one.** The same `n` is a budget.
The Weil form on `I_L` requires one independent translation atom for every prime
power `m log p < L`, with prescribed coefficient `2 (log p) p^{-m/2}`, and in
the Schur construction each prime enters as its own root `a_p = q p^{-1/2}`
(Section 6.1-6.3). A Laurent polynomial has finitely many roots. So:

> **Budget claim.** A pairing that is a twisted trace on a *fixed* generalized
> `q`-Weyl algebra with `deg P = n` carries at most `n` independent prime
> parameters, hence can realize `Q_L` only for `L` below a bound set by `n`.
> Realizing every `L` in one fixed algebra of this type would need `P` with
> infinitely many roots, which is outside the classified family.

This is exactly the shape of the gluing failure already in the manuscript
(Proposition 7.x, the unwanted atom at `log(3/2)` for two primes): it says the
obstruction is not an accident of the chosen output vectors but a dimension
count on the cone.

**The caveat, which matters.** The manuscript's construction is *not* a twisted
trace on one algebra. It is a state norm in a representation, and the lift
(6.18) applies the source "to each component of `B_d F` in an **orthogonal copy**
of `H`" — infinitely many copies. The trace classification bounds what **one
copy** can do; the Bloch lift is precisely the step that evades the bound, and
it is precisely the step the manuscript flags as having no field-theoretic
interpretation ("No particular four-dimensional interface has yet been shown to
implement (6.18)"). So the classification does not exclude the construction as
it stands — it **localizes the unjustified step**, which is worth as much.

---

## 6. A family exclusion for the Bloch lift (type N2)

From (6.19), a lifted circle weight gives

```
 B_{r,d}[F] = (1/2pi) int_R w_{r,d}(e^{i d tau}) |F^(tau)|^2 dtau,
```

so its multiplier is `tau -> w_{r,d}(e^{i d tau})`: **continuous, positive,
periodic with period `2pi/d`, and bounded by `max_{S^1} w_{r,d}`**. Equivalently,
in position space the form is a contact plus atoms at `x - y` in `d Z` — its
off-diagonal kernel is **purely atomic**.

The archimedean symbol `b(tau^2)` is **unbounded** (`~ log|tau|`), and by
Section 2.3 its off-diagonal kernel `-ngamma(|x-y|)` is **smooth and nowhere
vanishing** — purely continuous.

**Consequence.** No finite sum of Bloch-lifted circle weights, at any
parameters, any number of primes, and any `q`, equals the archimedean form. The
two are separated by a bounded-versus-unbounded invariant on the Fourier side
and by a Lebesgue decomposition on the position side. Since on each `I_L` the
construction of Sections 6-7 produces exactly such finite sums, the archimedean
half is structurally unreachable inside that family — not merely unachieved.

**What this does not prove.** It does not exclude an infinite-prime limit: the
union of `d_p Z` over all primes is dense in `R`, so an infinite sum of atomic
kernels can in principle converge weakly to a continuous one. That is not a
technicality — it is the Guinand-Weil duality between primes and zeros, and it
is the only route left inside this family. But an infinite positive sum has
divergent contact (`sum_p kappa_p ~ 4 sqrt X`), and controlling that divergence
against the finite `w0` is the same delicate cancellation that Theorem 7.5
already shows cannot be organised as two channels. So the honest statement is:

> The Bloch-lift family reaches the archimedean form only through an
> infinite-prime limit whose convergence is the whole problem, and Theorem 7.5
> forbids the only bookkeeping that would make that limit an addition.

That is a much stronger statement than the manuscript's current exclusions,
which are all of the form "this particular preparation fails".

---

## 7. Next

1. **Put (*) in the manuscript.** `b + w0 = 2 theta'` is two lines, it retires
   the contact as an independent object, and it makes the `p = 13` crossing
   meaningful. Then replace Proposition 7.14 by the symbol split of §2, keeping
   7.14 as the `tau_L = infinity` case.
2. **Add the graded OPE checklist (§3) to the candidate battery** from the
   previous note, replacing its single item (iii) by four.
3. **Write the budget claim of §5.3 properly.** It needs the precise link
   between "root of `P`" and "prime parameter `a_p`" in the elementary
   representation, which is Section 6.1-6.3 plus Klyuev Proposition 2.1. If it
   holds it is a clean negative theorem about a whole family, which is worth
   more than another excluded preparation.
4. **Look for more (N1) rigidity results.** Corollary 2.2, Proposition 2.4 and
   Proposition 3.4 are the three in hand and they have done most of the work in
   this investigation. Candidates for a fourth: a constraint on `q` from the
   requirement that one fixed `q` serve every prime; a lower bound on the
   magnetic charge; a statement that the near-null band edge of any realization's
   compression is at `gamma_1`.
5. **Do not** spend time on (N3).

---

## 8. Status of each claim

- §1.1 `b(tau^2) + w0 = 2 theta'(tau)` and (*): **proved**, two lines from (2.6),
  (2.7) and Plancherel; verified numerically to 16 digits. The identification of
  `theta'/pi` with the smooth counting density is classical
  (Riemann-von Mangoldt).
- §1.2 (b), (c) and the `tau_L` table: **proved** (the table is a numerical
  root-find of an explicit function).
- §1.3: a rearrangement of the explicit formula, **not new mathematics**.
- §2 the symbol split: the identity and the term-by-term positivity are
  **proved**; the `lambda_min` table is **numerical**, on a 400-cell Galerkin
  discretisation with a noise floor near `1e-6`, which is why `L = 1.25, 1.5`
  are reported as noise. The verdict that criticality is unchanged is a reading
  of those numbers, not a theorem.
- §3 expansion coefficients: **proved** (Stirling for `theta'`); verified
  numerically to five digits.
- §4 the circularity argument and the taxonomy: **proved** / definitional.
- §5 the quoted results are **Klyuev Propositions 2.1, 5.5 and Theorem 4.7** and
  **EKRS**, taken from the published SIGMA versions. I have read the statements,
  not the proofs. The **budget claim of §5.3 is a conjecture** — it needs the
  root-to-prime correspondence made precise before it is a theorem. The caveat
  about the Bloch lift is a reading of (6.18) and the manuscript's own remarks.
- §6 the periodicity, boundedness and atomicity of Bloch-lifted multipliers:
  **proved**, directly from (6.19). The exclusion of finite sums: **proved**.
  The discussion of infinite sums: **not proved**, and flagged as the open route.

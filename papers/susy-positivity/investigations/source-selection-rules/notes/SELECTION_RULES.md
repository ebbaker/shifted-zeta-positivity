# The selection rules

**Author: Claude Opus 5 (Anthropic).** 16 September 2026; this is the living
index of the investigation and is updated as rules are added or retired.

Necessary conditions a candidate source for the localized Weil form must
satisfy, ordered by what they cost to apply. Each is cheap; together they are
meant to replace the practice of testing a candidate by matching the terms of
(2.9) one at a time, which Theorem 7.5 shows is not a weaker version of the same
question. Equation numbers are those of the inverse-bulk manuscript 0.5.

| # | Rule | Cost | Source |
|---|---|---|---|
| 1 | The pairing commutes with `x -> -x` | free | Proposition 2.4 |
| 2 | The source is unbounded relative to the input `L^2` norm | free | Proposition 3.4 |
| 3 | The spectral weight is the smooth zero density, to four orders | cheap | this investigation |
| 4 | The archimedean channel spectrum is `{2n + 1/2}` with unit residues | cheap | (2.2), new here |
| 5 | Every channel decomposition passes the interference bound | cheap | Lemma 7.4 |
| 6 | The archimedean part is not a lifted circle weight | free | this investigation |
| 7 | The contraction is critical, with a margin collapsing in `L`, and near-null band edge at `gamma_1` | one computation | this investigation |
| 8 | The complete identity at `L = 1` | expensive | Problem 8.3 |

---

**1. Reflection.** Every kernel in (2.9) depends on `x - y` through an even
function, so `Q_L(Rf, Rg) = Q_L(f, g)` and any source carries a unitary `J` with
`J Phi(f) = Phi(Rf)`, `J^2 = id`. A pairing that does not commute with
`x -> -x` is excluded before any arithmetic. For a realization compatible in `L`,
`J` is the functional equation acting on the zeros.

**2. Unboundedness.** `Q_L[f_N]/log N -> ||chi||^2` for `f_N = chi e^{iNx}`, so no
source of the form `Phi(f) = int f(x) V_x Omega dx` with `V_x` unitary, and no
finite direct sum of such, can match. **This is what kills bounded spectral
variables.** The conformal Wilson benchmark of Section 5.1 failed because
`W = 2 cos(theta)` has spectrum in `[-2, 2]`: its kernel is entire in the
separation, so it has no atoms, and its pairing is bounded in `||f||_{L^2}`. The
operative criterion is unbounded spectrum, not open versus closed geometry —
the test functions carry no boundary conditions, only a support condition.

**3. The spectral weight is the smooth zero density.** By the density identity
(see [the density-symbol note](DENSITY_SYMBOL_AND_SYMBOL_SPLIT_20260916.md)),
`b(tau^2) + w0 = 2 theta'(tau)`, so the archimedean part of the target together
with the contact is `int |F^|^2 dNbar`. Graded, with every coefficient checked:

```
 b(tau^2) + w0 = log(tau/2pi) + 0*tau^{-1} - (1/24) tau^{-2} + 0*tau^{-3} - (7/960) tau^{-4} + ...
```

Four separate falsifications: unit coefficient on the leading log (the marginal,
`Delta = 1/2`, borderline-Gagliardo case); intercept exactly `-log 2pi`, which is
the contact; **no** `tau^{-1}` term, which is rule 1 seen in the expansion;
then `-1/24` and `-7/960`. A candidate with the right slope and the wrong
intercept has the wrong density of states, not a small error.

This rule subsumes what would otherwise be a separate perturbative test: the
leading density of states a perturbative calculation produces is exactly the
object compared here.

**4. The archimedean channel spectrum.** Exactly, not asymptotically, from (2.2):

```
 ngamma(r) = sum_{n>=0} e^{-a_n r},   a_n = 2n + 1/2,
```

a discrete spectrum of level spacing 2 starting at 1/2 — the quarter shift — with
**every residue equal to one**. The sum of residues diverges, which is the
short-distance divergence of rule 3. *Caveat, and it is the manuscript's own
(Section 3.1): the arithmetic coordinate is not automatically Euclidean time, so
reading `ngamma` as a channel spectrum assumes an identification the model must
supply.* Where it applies it explains why the sphere direction is the right place
to look for the archimedean half: the real Gaussian boundary module supplies
exactly this tower.

**5. The interference bound.** For any decomposition into channels whose norms a
candidate computes separately, `t A[f] + t^{-1} B[f] + C[f] >= 0` for all `t > 0`.
At `t = 1` this is only `Q_L >= 0`; other `t` are strictly stronger. Applied to
the gamma energy and the summed prime references it fails at the indicator of
`I_{5/4}` and by a growing factor as `L` grows (Theorem 7.5). Apply it first: it
is cheap and it kills most proposals.

**6. The archimedean part is not a lifted circle weight.** By (6.19) a Bloch-lifted
circle weight has multiplier `tau -> w_{r,d}(e^{i d tau})`: continuous, positive,
**periodic and bounded**, with a **purely atomic** off-diagonal kernel supported
on `d Z`. The archimedean symbol is **unbounded**, and by Section 2.3 its
off-diagonal kernel is smooth and nowhere vanishing — purely continuous. So no
finite sum of Bloch lifts, at any parameters, any number of primes and any `q`,
is the archimedean form. It is reachable inside that family only through an
infinite-prime limit, whose convergence is the whole problem and whose only
natural bookkeeping is the one Theorem 7.5 forbids.

**7. The contraction is critical, with the near-null band edge at `gamma_1`.**
Weil positivity on `I_L` is `T_L <= K_+`, and `||Pi_L|| = 1 - lambda_min(Q_L; K_+)`
is saturated, by a margin that collapses superexponentially in `L`:

| `L` | 1.0 | 1.5 | 2.0 | 3.0 |
|---|---|---|---|---|
| `lambda_min <~` | `1e-9` | `2.5e-14` | `1.7e-17` | `1.2e-24` |

measured in a smooth basis with `Q_L` assembled from its spectral form; see
[the fixed-point note](FIXED_POINTS_AND_THE_MARGIN_20260916.md), §5, which also
corrects the figures quoted in Section 7.6 of the sibling manuscript. **These are
weak upper bounds.** Zhu (arXiv:2608.24827) reaches `2.3e-17` at `L = 0.8` and
`3.2e-283` at `L = 2` with sine-basis trial functions, in a different
normalization (against `||f||_2^2`, not `K_+`); see
[the sweep](EXISTENCE_MECHANISM_SWEEP_20260916.md), §7, including its reliability
caveats. The collapse is far more violent than our own basis can see. So a
mechanism must produce a **critical** contraction, and more sharply:

> Any hypothesis supplying a margin uniform in `L` — a self-map into a fixed
> compact subset of the cone's interior, a uniform contraction ratio, a spectral
> gap — proves something false.

Moreover the
critical subspace is bandlimited below the first zero: near-null eigenvectors
carry more than 99.9% of `|F^|^2` below `gamma_1 = 14.1347`, generic directions a
few per cent, and the in-band count tracks `L gamma_1 / pi` to about 25%. A
candidate mechanism whose contraction has a band edge somewhere else is excluded
without matching a prime. *(Measured in a 400-cell Galerkin basis; recorded in
[the bottleneck brainstorm note](../../../brainstorm/inverse-bulk-brainstorm/BOTTLENECK_AND_OPERATOR_SEARCH_20260916.md).
Not yet a repository check programme — see the continuation note.)*

**8. The complete identity at `L = 1`.** (8.11), or in the split presentation of
this investigation: realize `(1/2pi) int sigma_1^+ |F^|^2 + 2|<cosh(x/2), f>|^2`
as a physically defined source norm, and
`(1/2pi) int sigma_1^- |F^|^2 + 2|<sinh(x/2), f>|^2 + Bt_{r_2,d_2}[E_1 f]` as a
compression of it, with `sigma_1^-` supported on `|tau| < 3.5504`. Failure calls
for a different source or model, not for residual estimates.

---

## Rules that were considered and are not here

- **A ghost or indefinite sector for the pole term.** Withdrawn in manuscript 0.5;
  a realization compatible in `L` is evaluation on the zeros in a positive `l^2`,
  which has no null vectors. What survives is rule 1.
- **The prime-free inequality (8.1).** Implied by `Q_L >= 0`, so it cannot fail
  unless RH does; it discriminates nothing and is not a prerequisite for the
  construction problem.
- **A budget on prime parameters from the trace classification.** Retracted; see
  [the q-Weyl note](QWEYL_TRACE_SPACE_20260916.md), §4. The prime parameters are
  not roots of `P`.

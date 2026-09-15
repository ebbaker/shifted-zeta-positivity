# The mirror prime reference and the subtraction form of the Weil target

**Author: Claude Opus 5 (Anthropic), 15 September 2026.** New calculation,
following the exclusion in
[INTERFERENCE_BOUND_AND_TWO_CHANNEL_EXCLUSION.md](INTERFERENCE_BOUND_AND_TWO_CHANNEL_EXCLUSION.md).
Not yet in the working manuscript.

Supporting programme:
[`numerics/check_mirror_subtraction.py`](../numerics/check_mirror_subtraction.py),
record [`mirror-subtraction-checks.json`](../numerics/records/mirror-subtraction-checks.json).

## 1. The question

The two-channel exclusion says the Weil target cannot be assembled as
`gamma channel + prime channel`, and that the negative contact and the signed
poles must instead come from a subtraction that is itself a norm:
`||(1 - Pi) G f||^2 = ||G f||^2 - ||Pi G f||^2`. That reformulation is only
useful if the subtracted piece is something we can build and the remaining
source is something simpler than the target. This note shows that both hold,
with an explicit and rather clean decomposition.

## 2. A mirror of the positive prime reference

The manuscript's reference has circle multiplier

```
w_{r,d}(z) = kappa - d sum_{n>=1} r^n (z^n + z^{-n}),   kappa = 2dr/(1-r),
w_{r,d}(z) = d r (1+r)/(1-r) * |1 - z|^2 / |1 - r z|^2  >= 0,
```

with `kappa` the least contact compatible with those atoms. There is a second
elementary nonnegative weight carrying the **same atoms with the opposite
sign**:

```
wt_{r,d}(z) = kappat + d sum_{n>=1} r^n (z^n + z^{-n}),   kappat = 2dr/(1+r),
wt_{r,d}(z) = d r (1-r)/(1+r) * |1 + z|^2 / |1 - r z|^2  >= 0.
```

Derivation: with `c = z + z^{-1}`,
`(2 + c)/|1-rz|^2` has constant Laurent coefficient `2/(1-r)` and `z^m`
coefficient `r^{m-1}(1+r)/(1-r)`; multiplying by `d r (1-r)/(1+r)` gives
`2dr/(1+r)` and `d r^m`. The two weights are complementary,

```
w_{r,d} + wt_{r,d} = 4 d r / (1 - r^2),
```

and `kappat` is the least contact for its sign, by evaluating at `z = -1`
exactly as `kappa` is obtained at `z = +1`. All of this is verified in exact
rational arithmetic by the check programme.

**The mirror contact is much smaller**, and that is the point:

| L | active primes | sum kappa | sum kappat |
|---|---|---|---|
| 1 | 2 | 3.3468 | 0.5742 |
| 5/4 | 2, 3 | 6.3483 | 1.3785 |
| 2 | 2, 3, 5, 7 | 11.3172 | 3.4406 |
| 3 | 8 primes | 18.9237 | 7.8704 |
| 4 | 16 primes | 30.3436 | 16.0103 |

(For large `p` the two agree to leading order, `2 log p / sqrt p`; the gain is
concentrated on the small primes, which is exactly where the contact budget
was being lost.)

## 3. The subtraction form

Because the mirror atoms have the opposite sign, they cancel the Weil prime
term outright. Writing `Bt_{r,d}` for the form with multiplier `wt_{r,d}`,

```
Q_L  =  A_L  -  sum_{p < e^L} Bt_{r_p, d_p},

A_L[f] = K[E_L f]  +  ( w0 + sum_{p < e^L} kappat_p ) ||f||^2  +  P_L[f].
```

Verified as an identity of quadratic forms on explicit inputs by the check
programme (error < 1e−9 throughout).

Two things are worth emphasising.

**`A_L` contains no prime translations.** All of the arithmetic has moved into
the subtracted term, which is a sum of positive references of exactly the kind
the dressed Schur construction already produces. The remaining source is the
gamma energy, the rank-two pole form, and a single arithmetic constant.

**`A_L` is robustly positive, whereas `Q_L` barely is.** Fourier Galerkin,
61 modes:

| L | lambda_min(Q_L) | lambda_min(A_L) | c_L = w0 + sum kappat |
|---|---|---|---|
| 0.5 | 3.3e−2 | 0.0334 | −5.3722 |
| 0.8 | 1.8e−4 | 0.5020 | −4.7980 |
| 1.0 | 9.1e−7 | 0.2581 | −4.7980 |
| 5/4 | ~0 | 0.7989 | −3.9937 |
| 3/2 | ~0 | 0.5560 | −3.9937 |
| 2 | ~0 | 2.1281 | −1.9315 |
| 3 | ~0 | 5.2496 | +2.4983 |
| 4 | ~0 | 11.1131 | +10.6381 |
| 5 | ~0 | 22.3815 | +25.9343 |

Note `c_L` changes sign near `L ≈ 2.6`: past that point the prime-free source
has a *positive* contact and its positivity is nearly trivial.

## 4. What the reformulation buys, and what it does not

It does not prove anything: `A_L = Q_L + sum Bt_p` with `sum Bt_p >= 0`, so
`A_L >= 0` is *implied* by `Q_L >= 0` and the full difficulty is still present.
What changes is where the difficulty sits and what a construction has to do.

Define the positive contraction

```
Pi_L = A_L^{-1/2} ( sum_p Bt_p ) A_L^{-1/2}.
```

Then **Weil positivity on `I_L` is exactly `|| Pi_L || <= 1`**, and a source
realizing `A_L` together with a projection (or contraction, by dilation)
implementing `Pi_L` realizes `Q_L` as a compression. The interference bound of
the previous note does not apply to a difference, so nothing here is excluded
by it. Numerically, in the same Galerkin space:

| L | 0.8 | 1.0 | 5/4 | 3/2 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|---|---|
| `\|\|Pi_L\|\|` | 0.99968 | 0.9999985 | 1.0000000 | 1.0000001 | 1.0000003 | 1.0000008 | 1.0000004 | 1.0000001 |
| old `\|\|Pi_K\|\|` | 0.839 | 0.863 | 1.751 | 1.793 | 3.571 | 7.034 | 13.38 | 26.05 |

The second row is the two-channel architecture in the same language: it asks
the gamma energy alone to dominate the prime references, `sum_p B_p <= K`, and
that fails by a factor that grows with `L`. This is the quantitative form of
the exclusion theorem, and it is one-sided in the useful direction — a
subspace value above 1 certifies failure.

The first row sits at 1 to within the discretization. That is expected rather
than alarming: `|| Pi_L || = 1 - lambda_min(Q_L / A_L)` and `Q_L` is nearly
degenerate. The domination is **saturated**, not comfortable, and the
directions where it saturates are the near-null vectors of `Q_L`. Their count
grows with `L`:

| L | 0.8 | 1.0 | 5/4 | 3/2 | 2 | 3 | 4 |
|---|---|---|---|---|---|---|---|
| #{eig(Pi) > 0.9} | 2 | 3 | 5 | 7 | 13 | 33 | 45 |

## 5. The two objects to construct

The reformulation splits the problem into one plausible lemma and one hard
domination.

**(a) A prime-free archimedean inequality.** Prove, unconditionally,

```
K[E_L f]  +  ( w0 + sum_{p < e^L} kappat_p ) ||f||^2  +  P_L[f]  >=  0 .
```

This is the only place the primes enter, and only through a constant. It has
genuine slack (0.26 to 22 in the table above) and for `L > 2.6` the constant is
positive, leaving only the rank-two pole term to control against the gamma
energy. This looks like a real lemma, provable by archimedean estimates, and
it is the natural place to bring in the compressed-scaling-action machinery of
Connes and Consani (arXiv:2006.13771), which produces exactly this kind of
archimedean positivity from a projection.

**(b) The domination `sum_p Bt_p <= A_L`.** This still contains all of Weil
positivity, and no reformulation will remove that. But it is now a single
statement of the right shape — one positive source dominating one positive,
prime-carrying, explicitly-constructed reference — rather than an additive
bookkeeping identity that we now know is impossible.

## 6. Is the mirror weight realizable in the Schur representation?

Open, and a concrete next check. The manuscript's magnetic output state is
proportional to `(1 + zeta)/(1 + r zeta)`, whose modulus squared gives
`|1 - z|^2/|1 - r z|^2` with `z = -zeta`. The mirror weight needs

```
|1 + z|^2 / |1 - r z|^2   i.e. the state  (1 - zeta)/(1 + r zeta),
```

the same denominator with the numerator sign flipped. The numerator `(1+zeta)`
came from the cancellation `(1 + zeta) chi_q(q^{-1} zeta) = chi_q(q zeta)`, so
this is not a free choice:

- `zeta -> -zeta` is unitary but flips the denominator too, giving
  `|1+z|^2/|1+rz|^2`, whose coefficients alternate in sign. Not the mirror.
- `q -> -q` in the chi factor would do it, but `0 < q < 1` is the real
  quantization parameter.
- Putting `(1 - zeta)/(1 + zeta)` into the electric dressing introduces a pole
  on the unit circle and breaks the graph-domain argument of Lemma 6.1.

So the mirror reference is, for now, an elementary positive Toeplitz weight
with the right arithmetic content but no Schur preparation. Finding one — or
showing the elementary representation cannot produce it — is the next
calculation on the Schur side, and it is a sharply posed question rather than
an open-ended search.

## 7. Immediate next steps

1. Attempt (a) analytically. Start at `L <= log 2`, where there are no primes
   and the statement is `K + w0 ||f||^2 + P_L >= 0`, and see whether the
   Connes-Consani compression argument gives it with the constant we need.
2. Settle section 6 for the elementary `q`-Weyl representation.
3. Extend `check_mirror_subtraction.py` with a certified lower bound for (a)
   on a fixed interval, which would turn the first row of the table into a
   theorem for that `L`.
4. Only then update the manuscript: the subtraction form belongs in Section 7
   alongside the exclusion, and `A_L` belongs in the outlook as the object to
   realize.

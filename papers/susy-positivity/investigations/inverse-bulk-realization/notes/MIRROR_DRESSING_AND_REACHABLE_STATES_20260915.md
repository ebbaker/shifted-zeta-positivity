# The mirror weight is reachable, and the single-insertion sector is not a constraint

**Author: Claude Opus 5 (Anthropic), 15 September 2026.** Work on item 2 of
section 3 of [CONTINUATION_20260915.md](CONTINUATION_20260915.md), which is
Remark 7.10 of manuscript 0.4. Not in the working manuscript.

Supporting programme:
[`numerics/check_mirror_dressing.py`](../numerics/check_mirror_dressing.py),
record [`mirror-dressing-checks.json`](../numerics/records/mirror-dressing-checks.json),
registered in the `CHECKS` dictionary.

## 0. Summary

Remark 7.10 asks whether the mirror prime reference `wt_{r,d}` can be produced
by a preparation of the kind used in Theorem 6.2, lists three blocked routes,
and calls the question open and sharply posed. The answer is **yes**, by a
fourth route, and the obstruction the remark describes is not there.

Five findings.

1. **The mirror weight is reachable**, by one negative magnetic insertion
   applied to an admissible electric preparation of the same elementary
   representation at the same fixed `q`. The dressing is the dressing of
   Lemma 6.1 with the sign of a single Pochhammer factor reversed, and its
   only singularity sits at the same place, so the graph-domain argument of
   Lemma 6.1 applies verbatim.
2. **More is true: the reachable output states are exactly the functions
   analytic on some disk of radius greater than one.** The factor `(1+zeta)`
   that `u_-` inserts is cancelled, for *every* target, by the `j = 0` factor
   of the vacuum's Pochhammer whenever the dressing declines to remove it.
   The single-insertion sector places no constraint on the output beyond
   analyticity past the circle.
3. **Remark 7.10's reason is the error.** The `(1+zeta)` in Lemma 6.1's output
   is not what the cancellation identity produces — that identity produces the
   nowhere-vanishing `chi_q(q zeta)`. It is the `j = 0` factor of the
   *dressing's own* numerator at the dilated argument. The numerator is a free
   choice, and the freedom lives in the dressing.
4. **The consequence for the programme is modest, and smaller than a negative
   answer would have been.** A no-go would have forced the mirror into a
   different protected sector than the positive reference, which is a
   construction constraint. The positive answer imposes none. It also removes
   any suggestion that the subtraction form is blocked on the source side.
5. **It costs Theorem 6.2 some of its apparent content.** If every weight
   whose square root is analytic past the circle is reachable, then producing
   the positive prime reference is not evidence of arithmetic in the
   representation: the arithmetic is in the choice of dressing. What survives
   as genuine is the fixed-`q` uniformity across primes and the checked graph
   domain, not the fact that a prime weight appears at all.

## 1. The construction

Conventions are those of Section 6. On the zero-charge sector an electric
preparation `eta = D(v) Omega_q` has wavefunction `eta(w) = C_q D(w) chi_q(w)`,
and (6.2) gives, on the output sector `m = -1`,

```
(u_- eta)_{-1}(zeta) = (1 + zeta) eta(q^{-1} zeta).                      (*)
```

Lemma 6.1 takes `eta_a(w) = sqrt(1-a^2)/(1 + a w)` with `a = q r`, so that (*)
returns `sqrt(1-q^2 r^2)(1+zeta)/(1+r zeta)`. The mirror needs
`(1-zeta)/(1+r zeta)`. Take instead

```
etat(w) = sqrt(1-q^2 r^2) (1 - q w) / ( (1 + q w)(1 + q r w) ),
```

which differs from `eta_{qr}` by the factor `(1-qw)/(1+qw)`. At `w = q^{-1}zeta`
its denominator factor `(1 + q w)` becomes `(1 + zeta)`, which the insertion
supplies, and (*) returns exactly

```
(u_- etat)_{-1}(zeta) = sqrt(1-q^2 r^2) (1 - zeta)/(1 + r zeta).
```

The dressing preparing `etat` is `Dt = etat/(C_q chi_q)`. Since
`chi_q(w)^{-1} = (-q w; q^2)_inf = prod_{j>=0}(1 + q^{2j+1} w)` has `(1 + q w)`
as its `j = 0` factor, that factor cancels against the denominator of `etat`,
leaving

```
Dt(w) = sqrt(1-q^2 r^2) (1 - q w) (-q^3 w; q^2)_inf / ( C_q (1 + q r w) ),
```

the dressing (6.3) with the sign of the first Pochhammer factor reversed. The
Pochhammer tail is entire, so the only singularity of `Dt` is the simple pole
at `w = -(qr)^{-1}`, of modulus `(qr)^{-1} > q^{-1}` — which is exactly the
hypothesis under which Lemma 6.1's graph argument runs. Its Taylor polynomials
`Dt_N` converge uniformly on `|w| <= R` for `R` between `q^{-1}` and
`(qr)^{-1}`, hence `Dt_N(q^{-1}zeta)` converges uniformly on the closed unit
disk; `chi_q(q zeta)` has its nearest pole at modulus `q^{-2}` and is bounded
there. So `u_- Dt_N(v) Omega_q` converges in norm to the displayed state and
every closed physical extension of the algebraic action contains that graph
limit, with that value.

No pole is crossed. The pole of `chi_q` at `w = -q^{-1}`, which Lemma 6.1's
dressing removes and this one retains, lands at `zeta = -1` after the dilation
and is cancelled there by the `(1 + zeta)` the insertion supplies — the same
cancellation `(1+zeta) chi_q(q^{-1}zeta) = chi_q(q zeta)` that Lemma 6.1 uses.
At every finite `N` the approximant is analytic past the circle.

With `betat^2_{q;r,d} = d r (1-r) / ( (1+r)(1 - q^2 r^2) )`, which is (6.9)
with `(1+r)/(1-r)` inverted, and `Phit[h] = betat h(-q^{-1}v) u_- Dt(v)Omega_q`,
the pairing is `int h~ k wt_{r,d} dtheta/2pi` with `wt_{r,d}` the mirror weight
of Proposition 7.7. Setting `r = p^{-1/2}`, `d = log p` gives every mirror atom,
at the same fixed `q` that serves the positive references.

## 2. The general statement

The construction is a special case, and the general case is the real content.

**Proposition.** *Let `psi` be analytic on `|zeta| < rho` for some `rho > 1`.
Put `eta(w) = psi(q w)/(1 + q w)`. Then `eta = D(v)Omega_q` for*

```
D(w) = psi(q w) (-q^3 w; q^2)_inf / C_q ,
```

*which is analytic on `|w| < rho/q`, and `rho/q > q^{-1}`. Lemma 6.1's graph
argument applies to `D` unchanged, and the output state is `psi`. Conversely
every output state is of this form. Hence the states reachable on the sector
`m = -1` by one negative magnetic insertion, from an electric preparation whose
dressing is analytic on a disk of radius exceeding `q^{-1}`, are exactly the
functions analytic on some disk of radius exceeding one.*

*Proof.* `C_q D chi_q = psi(qw) prod_{j>=1}(1+q^{2j+1}w) / prod_{j>=0}(1+q^{2j+1}w)
= psi(qw)/(1+qw) = eta`, and the tail product is entire, so the singularities of
`D` are those of `psi(qw)`. Then (*) gives
`(1+zeta) eta(q^{-1}zeta) = (1+zeta) psi(zeta)/(1+zeta) = psi(zeta)`.
For the converse, (*) determines `eta` from `psi`. The graph argument is that
of Lemma 6.1 with `R` chosen between `q^{-1}` and `rho/q`. `QED`

The `(1 + q w)` that the target's denominator acquires is *always* the `j = 0`
factor of the vacuum's Pochhammer, for every `psi`. That is the whole
mechanism, and it is why the `(1+zeta)` supplied by `u_-` constrains nothing.

## 3. Why the remark's argument fails

Remark 7.10 says the numerator of Lemma 6.1's output "came from the
cancellation `(1+zeta)chi_q(q^{-1}zeta) = chi_q(q zeta)` and is not a free
choice". The identity is used in the proof, but what it yields is
`chi_q(q zeta)`, which has no zeros. In the displayed output of Lemma 6.1 the
factor `(1+zeta)` is the `j = 0` factor of `(-q w; q^2)_inf` — the dressing's
own numerator — evaluated at `w = q^{-1} zeta`. The dressing (6.3) cancels the
vacuum entirely, `D_{q,a} = sqrt(1-a^2)/(C_q chi_q(w)(1+aw))`, and it is that
choice which places the zero at `zeta = -1`.

The three routes the remark blocks all act on the output after the fact: the
unitary `zeta -> -zeta`, which reverses the denominator too; `q -> -q`, which
leaves the admissible parameter range; and inserting `(1-zeta)/(1+zeta)` into
the dressing, which does place a pole on the unit circle. The fourth route acts
on the dressing's zeros and poles at radius `q^{-1}` and beyond, where nothing
touches the circle.

## 4. What this does and does not give the programme

**It settles the Schur-side question.** Remark 7.10 is closed, affirmatively,
and the manuscript's "next question on the Schur side" needs restating.

**It does not advance Problem 8.3.** Corollary 7.9 needs the mirror references
as `<Gf, Pi Gf>` for a positive contraction `Pi` on the range of a source `G`
for the prime-free form `A_L` — as a *compression of that source*, not as an
independent positive state norm. What this note supplies is the latter. The
complementarity `w_{r,d} + wt_{r,d} = 4dr/(1-r^2)` of (7.16) does say that per
prime the mirror is a compression: multiplication by
`wt_p / (4 d_p r_p/(1-r_p^2))` takes values in `[0,1]` on the lifted space and
is a positive contraction. But assembling those into a contraction on the range
of a source for `A_L` is precisely the domination
`sum_p Bt_p <= A_L`, which is Weil positivity itself. Nothing is gained there
and nothing should be claimed.

**It bears on item 1 by elimination.** Both output states live in the same
positive-metric sector; in the basis `1/(1+r zeta)`, `zeta/(1+r zeta)` their
Gram matrix is `(1-r^2)^{-1} [[1, -r], [-r, 1]]`, positive definite, and the
two states are orthogonal with `||psi_+||^2 = 2/(1+r)`, `||psi_-||^2 = 2/(1-r)`.
A positive-metric sector has no null vectors, so nothing here can supply the
hyperbolic pair of Lemma 2.3. That is not news — Section 8.2 says a positive
channel cannot — but it does mean the flexibility found above is flexibility of
*weights only*. The discriminating structure has to come from the metric of the
sector, not from the choice of preparation inside a positive one. Item 1 remains
the substantive item and this note does not touch it.

**A caution about Theorem 6.2.** The proposition of section 2 says the
single-insertion sector will produce essentially any weight asked of it. So the
appearance of a prime weight there is a statement about the dressing that was
chosen, not about the representation. Theorem 6.2's durable content is the
uniformity in `q` across all primes and the checked graph domain. Future
candidate tests should not count "the model produces the prime weight" as
evidence; by Theorem 7.5 and this note, weight-matching in a positive sector is
cheap and non-discriminating.

## 5. Status of each claim

- The construction of section 1 and the proposition of section 2 are **written
  proofs**, elementary complex analysis on top of Lemma 6.1's own argument.
- The check programme verifies the series identities in **exact rational
  arithmetic**: the two actions (*), the ratio of the two electric states, the
  Pochhammer telescoping at four truncations, the weight coefficient ratios
  `2/(1+r)` and `2/(1-r)` with geometric ratio `r`, the orthogonality of the
  two outputs (the overlap truncated at `N` is exactly `r^{2N}`), and
  reachability of three unrelated targets. 638 cases.
- The convergence rate of the truncated dressings is a **labelled
  floating-point** illustration: the error at radius `q^{-1}` is geometric with
  ratio `r`, observed to twelve digits.
- No positivity certificate, no compression of `A_L`, and no statement about
  the pole term is claimed anywhere above.

## 6. Housekeeping, now done

`check_mirror_dressing.py` is registered in the `CHECKS` dictionary of
`validation/drafts.py` and `BUILD_RECORD.json` was regenerated with
`drafts.py record` after a visual review of the rendered PDF. The manuscript
source and the deliverable PDF are unchanged and the PDF remains byte-identical
to the `2026-09-15-v04` snapshot; only the hashes of `drafts.py` and the check
programmes moved. `drafts.py check --replay` passes and now covers this
programme.

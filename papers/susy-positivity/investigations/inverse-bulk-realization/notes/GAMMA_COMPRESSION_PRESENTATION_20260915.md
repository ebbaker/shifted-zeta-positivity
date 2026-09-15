# The Weil form as a compression of the gamma energy

**Author: Claude Opus 5 (Anthropic), 15 September 2026.** Follows
[POLE_TERM_NEEDS_NO_MECHANISM_20260915.md](POLE_TERM_NEEDS_NO_MECHANISM_20260915.md),
which struck item 1 of section 3 of
[CONTINUATION_20260915.md](CONTINUATION_20260915.md) and named the first half
of Problem 8.3 as its replacement. This note shows that replacement can be
dropped as well. Not in the working manuscript; section 5 says what it should
replace there.

Supporting programme:
[`numerics/check_gamma_compression.py`](../numerics/check_gamma_compression.py),
record [`gamma-compression-checks.json`](../numerics/records/gamma-compression-checks.json),
registered in the `CHECKS` dictionary.

## 0. Summary

Corollary 7.9 presents `Q_L` as a compression of a source for the prime-free
form `A_L`. That presentation needs two things nobody has: a source for `A_L`,
and the inequality `A_L >= 0`, which is open on `log 2 < L < log 7`. Split the
pole form by parity instead, (2.17), and both requirements disappear.

**Proposition.** *For every `L > 0` and every finite prime set `P` containing
each `p < e^L`, write `c_L = w0 + sum_{p in P} kappat_p`, `(c)_+ = max(c,0)`,
`(c)_- = max(-c,0)`, and*

```
 K_+[f] = K[E_L f] + (c_L)_+ ||f||^2 + 2 |<cosh(x/2), f>|^2 ,
 T_L[f] = (c_L)_- ||f||^2 + 2 |<sinh(x/2), f>|^2
          + sum_{p in P} Bt_{r_p,d_p}[E_L f] .
```

*Then `Q_L = K_+ - T_L` identically on `C_c^infty(I_L)`; `K_+` is a norm, with
the explicit source*

```
 G f = ( b^{1/2}(D) E_L f , (c_L)_+^{1/2} f , sqrt2 <cosh(x/2),f> )
       in L^2(R) + L^2(I_L) + C ;
```

*and `T_L >= 0`, each of its three terms separately. Consequently `Q_L >= 0` on
`I_L` if and only if `T_L <= K_+`, and in that case
`Q_L[f] = <Gf, (1 - Pi) Gf>` for the positive contraction `Pi` on the closure
of the range of `G` determined by `<Gf, Pi Gg> = T_L(f,g)`, so `Q_L` is a
compression of the gamma source.*

*Proof.* The identity is (7.18) with (2.17) substituted for `P_L` and the
constant moved to whichever side its sign puts it on; nothing cancels or is
approximated. `K_+` is a norm because the gamma multiplier `b(tau^2)` of (2.6)
is nonnegative, so `K[F] = || b^{1/2}(D) F ||^2`, and the other two terms are a
nonnegative multiple of `||f||^2` and a rank-one square. `T_L >= 0` because
`(c_L)_- >= 0`, the second term is a rank-one square, and each
`Bt_{r_p,d_p} >= 0` by Proposition 7.7. For the compression statement, the
form `t(Gf, Gg) = T_L(f,g)` is well defined on the range of `G` precisely
because `T_L <= K_+` — if `Gf = Gf'` then `K_+[f-f'] = 0`, hence
`T_L[f-f'] = 0` — and is bounded by one there, so Riesz gives a positive
contraction `Pi` with `t(u,v) = <u, Pi v>`; Corollary 7.9's dilation argument
then applies to `1 - Pi`. `QED`

Four things follow.

1. **The dominating form has an explicit source and `A_L` does not.** `K_+` is
   the gamma energy, one bounded positive rank-one term and a constant. Its
   source is a Fourier multiplier together with two extra coordinates, and the
   gamma part is the object Appendix A already builds as a field energy. `A_L`
   has no source and constructing one was the whole of the first half of
   Problem 8.3.
2. **No unproved positivity enters the presentation.** Corollary 7.9's
   compression needs `A_L >= 0`, i.e. (8.1), which is Yoshida's theorem below
   `log 2`, Proposition 8.1 above `log 7`, and **open on the compact window
   between**. Here both sides are positive term by term, at every `L`. The
   prime-free inequality is therefore not needed by the construction programme
   at all; it remains an interesting question about `A_L` and stops being a
   prerequisite.
3. **The whole criterion is one domination by the gamma energy.** `Q_L >= 0`
   on `I_L` iff `T_L <= K_+`. Everything that is not the gamma energy — the
   contact, the odd half of the pole form, and every prime — sits in one
   manifestly positive bounded form on the subtracted side.
4. **The price.** The subtracted term is no longer purely arithmetic. Section
   7.5's selling point for (7.18) was that `A_L` carries no prime translation
   and all the arithmetic sits in the subtraction; here the subtraction also
   carries the contact and the odd pole direction. That is the trade: a
   dominating form one can actually build, against a subtracted form that is no
   longer purely arithmetic.

## 1. Where the constant goes

`c_L` is a step function of `L`, constant between consecutive primes and
jumping by `kappat_p = 2 (log p)/(sqrt p + 1)` at `L = log p`. Starting from
`w0 = -5.37218...` the cumulative sum first exceeds zero at `p = 13`:

```
 p     2       3       5       7      11      13      17
 c_L  -4.798  -3.994  -2.999  -1.932  -0.821  +0.293  +1.399
```

So `c_L <= 0` exactly for `L < log 13 = 2.5649...`, where the constant joins
the subtracted side, and `c_L > 0` above it, where it joins the source. Nothing
depends on which; the split is by sign and the proposition holds at every `L`.
This also sharpens the manuscript's "changes sign near `L = 2.6`" to the exact
statement that the crossing is at `p = 13`.

## 2. What the numbers say

The check programme verifies the identity as a matrix identity on 40 indicator
cells, at ten values of `L` from `0.5` to `5`, agreeing to `7.5e-16`; it also
rebuilds the mirror matrices independently and confirms (7.18) against the
manuscript's own `form_matrix`, which is what certifies that the mirror
matrices used here are the right ones. `T_L` is positive at every sampled `L`,
with least eigenvalue relative to `||.||^2` between `3.6` and `28`.

The saturation `|| K_+^{-1/2} T_L K_+^{-1/2} ||`, in the same cell subspace:

```
 L          0.5      1.0      1.5      2.0      2.5      3.0      5.0
 saturation 0.99351  0.99945  0.99959  0.99963  0.99972  0.99970  0.99972
```

Just below one at every `L`, exactly as the manuscript's `||Pi_L|| = 1` to
within `1e-7` for the `A_L` presentation: the domination is saturated because
`Q_L` is nearly degenerate, and this presentation does not change that. **It
was never going to.** The difficulty is the compression, and it is identical in
both presentations; what changes is that one side of it is now an object with a
construction.

These saturation values are **one-sided**, and in the direction that matters
here: a subspace value is a *lower* bound for the true `||Pi||`, so a value
meaningfully above one would certify that the domination fails, and a value
below one certifies nothing. A better subspace therefore gives a larger value,
and the cell basis above is not a good one for this quantity.

I recomputed the whole presentation independently in a Fourier-Galerkin basis
of 33 modes, with every term except the rank-two pole part treated as a Fourier
multiplier — the mirror references through the closed form
`d r (1-r)/(1+r) (2+2 cos(d tau))/(1 - 2r cos(d tau) + r^2)`, which is (7.14)
lifted — and with an independent quadrature and eigensolver. The identity
`Q_L = K_+ - T_L` comes out to `2.3e-11` relative, an independent confirmation
of the cell-basis `7.5e-16`. The saturation there is `1 - 1.9e-7` at `L = 1`
and `1` to within `1e-15` at `L = 1.5`, `2` and `3` — machine-indistinguishable
from one, which is what the manuscript already reports for the `A_L`
presentation (`||Pi_L|| = 1` to within `1e-7`) and what
`lambda_min(Q_L) <= 1e-6` predicts. At that precision the sign of `1 - sat`
means nothing and certifies nothing either way. The cross-check lives outside
the repository; the recorded programme keeps the cell basis, whose overlaps are
computed exactly in `x` with no quadrature at all.

## 3. What this makes the construction problem

Problem 8.3 becomes, without its first half:

> Exhibit `Pi` with `T_L = <G . , Pi G . >` for a positive contraction `Pi` on
> the range of the explicit gamma source `G`, where `T_L` is the manifestly
> positive form above.

The source is fixed and known. The content is entirely the contraction, and by
Corollary 7.9's equivalence `||Pi|| <= 1` is Weil positivity, so no one should
expect the contraction to come cheaply. What the reformulation buys is that a
candidate model now has a definite thing to produce — a compression of the
gamma field's own Hilbert space — rather than a source for a form whose
positivity is itself open.

It also says what a candidate no longer has to do: produce the pole term from a
special sector, produce the contact from a separate mechanism, or satisfy an
architecture constraint from Theorem 7.5. Lemma 7.4 concerns sums and places no
obstruction on a compression, as Corollary 7.9 already notes.

## 4. What is not claimed

No Weil positivity certificate. No physically derived source: `b^{1/2}(D)` is a
Fourier multiplier, and the appendix's field energy realizes the same form, but
neither is a protected-sector preparation in the sense of the programme's
objective. No construction of `Pi`. And the presentation does not make the
problem easier in any quantitative sense — the saturation is the same.

## 5. What the manuscript should say

Section 7.5 and Section 8.2 currently present the subtraction form with `A_L`
as the source side, and Problem 8.3 asks for (8.1) unconditionally and a source
for `A_L`. The proposition above should be added next to Corollary 7.9, with
three consequences recorded: that the source side can be taken to be the gamma
energy plus two elementary terms, that the presentation needs no unproved
inequality, and that (8.1) is therefore not a prerequisite for the construction
programme. Problem 8.3 should lose its first clause. The exact sign-change
statement at `p = 13` belongs with the table in Section 7.5.

## 6. Status of each claim

- The proposition of section 0 is a **written proof**: an exact rearrangement
  of (7.18) using (2.17), plus the nonnegativity of `b`, of a rank-one square
  and of Proposition 7.7.
- The sign-change ladder of section 1 is an **exact finite computation**.
- The identity is verified as a **finite matrix identity** at ten values of
  `L`, to `7.5e-16`, with the mirror matrices independently cross-checked
  against the manuscript's `form_matrix`.
- The saturation table is **one-sided subspace evidence** and certifies
  nothing.
- `A_L >= 0` is not used anywhere above, which is the point.

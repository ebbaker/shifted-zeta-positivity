# Review of the local coercivity and revised-B certificate

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), in a separate same-model subagent audit; exact serving
variant and configured effort are not exposed and are not inferred.
This is internal analytic and computational review, not independent human
specialist refereeing.

Reviewed the [low-band derivation](../notes/LOCAL_COERCIVITY_LOW_BAND_20261003.md),
the complete [certificate generator](../numerics/local_weil_gap_20261003/certify_local_weil_gap.py),
and its [192-bit](../numerics/local_weil_gap_20261003/certificate_192.json)
and [256-bit](../numerics/local_weil_gap_20261003/certificate_256.json) records.
Final generator SHA-256:
`d4285411922142e366be60ac0ca103cc4ba4a654c551e34e3b43fa2096d17b38`.
Both saved records match that generator hash.

## Verdict

The certificate passes this audit. It proves

\[
Q[F]\ge\frac9{100}\|F\|_2^2
\]

on the full length-one source class with zero mean and both pole-neutrality
moments. It includes arbitrary complex sources, both additive parities,
and all source modes outside the finite matrix. It is not merely a
finite-family or sampled-frequency test.

Together with the independently bounded correction, it validates

\[
Q[F]\ge\frac9{77209}B[F]\ge\frac1{9000}B[F].
\]

Thus a positive fraction of the original Sonin trace can be retained while
the remaining fraction pays for the positive correction. This does not
prove domination of the unweighted positive spectral part `K_plus`, and it
does not extend the support or prime set.

## Analytic checks

Only the delay `log 2` is active for the specified support. The multiplier
`gamma(t)-sqrt(2)log(2)cos(t log 2)` therefore has the correct coefficient
and includes the complete prime contribution for these sources. No
nontrivial zeta zero or conjectural positivity is used.

The digamma partial-fraction series makes `gamma` increasing on the positive
axis. The outward cutoff check gives
`gamma(46)-1-sqrt(2)log(2)>0.01048649`. This certifies that the positive
weight `(1-q)_+` vanishes outside the retained frequency band.

The three constraint functions `1`, normalized `sinh(x/2)`, and normalized
`cosh(x/2)-4sinh(1/4)` are exactly orthonormal on `(-1/2,1/2)`. The code uses
their full analytic coefficients, not a projection onto approximate finite
moment vectors. I rederived the displayed sine/cosine integrals and the
spherical-Bessel/hypergeometric normalizations; their signs and factors
agree with the implementation. The common imaginary factor of the odd
plane-wave coordinates cancels correctly in their Hermitian outer products.
Evenness of the frequency weight makes the mixed parity blocks vanish.

The midpoint error is dimension-independent. Projection contractivity gives
`||v_t||<=1` and `||v'_t||<=1/sqrt(12)`. The total variation bound for the
rank-one integrand is consequently `V0+W/sqrt(3)`, yielding the stated
`h/(2 pi)` error factor. The scalar midpoint bound used to enclose `W`
retains its own variation error. Kinks where the positive-part weight
vanishes do not invalidate this absolutely continuous/BV argument.

For the entire omitted Legendre tail, the ratio of consecutive squared
majorants is `z^2/[(2n+1)(2n+3)]`. At rank 40 and `z=23`, the resulting
plane-wave norm bound is about `4.273503447e-6`. The code additionally
includes the tails of both nonconstant moment vectors. The full moment
projection therefore remains covered outside the finite polynomial space.
The rank-one difference bound `2 delta_M` correctly transfers this to an
operator truncation bound. This is the step that covers the infinitely many
untested source directions.

## Arithmetic and replay checks

Every special-function evaluation and matrix entry is enclosed with Arb/Acb.
The positive-part branch encloses zero-crossing balls rather than selecting
a sign from their midpoint. Both real parity blocks satisfy outward LDL
positivity for `0.9 I-D_M`; no floating eigenvalue decides this test.
The final generator rejects odd ranks, nonpositive node counts, and
insufficient precision, preserving the correspondence between the retained
parity blocks and the omitted-mode bound.

The principal record gives the following upper bounds (display values only;
the saved rational endpoints are the enclosures):

| Error contribution | Upper bound |
|---|---:|
| Frequency midpoint integration | 0.008191770079 |
| All omitted source modes | 0.000060562175 |
| Combined operator error | 0.008252332253 |

Together with the finite matrix cap `0.9`, these are strictly below the
`0.91` total required for the clean gap `0.09`.

I independently replayed the same arithmetic at 256 bits before its final
argument-guard/metadata edit; that edit does not change the arithmetic.
I then checked both final saved records against the final generator and
verified overlap of their exact rational scalar enclosures. Both final
precision runs pass the same finite matrix and tail inequalities. Agreement
is a consistency check; the outward operations and analytic remainder
bounds provide the proof.

I also independently rebuilt the inherited rank-32 prolate certificate at
256 bits. It again certified `57/10^6` and the stated infinite-complement
bounds. Its generator SHA-256 is
`ab61bfe5b08b90c2122decffd46bf6e9396ed4a1764d19102fd39b8a7d6cf9e6`.

## Correction allowance and limits

The source crossing factorization
`P C_F* C_F chi=P C_F* 1_I C_F chi` has the correct conjugations and support.
Its Hilbert--Schmidt factors have squared norms
`integral (1/2-v)|F(v)|^2` and `integral (1/2+v)|F(v)|^2`; hence its nuclear
norm is at most `||F||^2/2`. Reflection preserves this bound for the even
multiplier. The inherited boundary gap then gives `|K[F]|<=772||F||^2`.
The outward evaluation of the unrounded coefficient is below
`771.993384079`.

Writing `delta=9/100` and `k=772`, the absorption is elementary:
`B=Q+K<=Q+k||F||^2<=(1+k/delta)Q`. Therefore the retained fraction is
`theta=delta/(k+delta)=9/77209`, and

\[
Q=\theta B+\bigl((1-\theta)B-K\bigr)
\]

has two nonnegative terms. The simpler fraction `1/9000` is smaller and
therefore valid as well. No finite moment penalty is being substituted for
this infinite-dimensional energy allowance.

The mean-zero condition, the two pole moments, and source support inside
`(-1/2,1/2)` are essential to the certified claim. This result accommodates
the positive resonance directions at that window. It does not determine
the original bump's correction sign, certify `B>=K_plus`, or establish an
all-window mechanism or RH. The revised comparison uses an independently
certified local arithmetic gap; it is not a derivation of that gap from
Sonin geometry alone.

# Scoped review of the normalized heat collision criterion

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Reviewer: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
This is a separate same-model mathematical review, not independent
specialist verification of the imported approximation theorem.

**Verdict.** The normalized disk bound, reflected error, derivative estimate,
fixed-cutoff correction and explicit real-collision exclusion for
`|x|>=exp(64/epsilon)` pass this scoped audit. No mathematical correction
was requested. The last bound excludes common **real** zeros of `H_t,H_t'`;
the note does not independently prove that all complex zeros above that
height are real. No compact rectangle or shrinking-time limit is certified.

Reviewed
[NORMALIZED_HEAT_COLLISION_CRITERION_20261008.md](../newman_collisions/notes/NORMALIZED_HEAT_COLLISION_CRITERION_20261008.md),
its [constant check](../numerics/check_normalized_heat_constants.py), and
its [record](../numerics/normalized_heat_constant_record_20261008.json).
The exact rational check reproduces that record byte for byte. Its scope
is the final rational implications, not the analytic source proof or
an interval computation of heat-flow values.

## 1. Source scope and analytic rewriting

Consulted the primary
[Polymath paper, Theorem 1.3 and equations (6)--(24)](https://arxiv.org/html/1904.12438#S1.Thmtheorem3)
on 8 October 2026. The stated domain is `0<t<=1/2`, `x>=200`,
`0<=y<=1`. The normalization, logarithmic derivative, natural cutoff,
and three error bounds in the note match that theorem. This verifies
the imported statement and constants, not its proof.

With `s=(1-iz)/2`, one has `conjugate(s)-y=1-s` on the upper source
rectangle. The source's `kappa` cancels the difference between
`alpha(conjugate(s))` and `alpha(1-s)`, so the apparently conjugated
second sum is exactly the holomorphic reflected term used in equation
(2) of the note. This calculation requires a fixed integer cutoff;
the note retains that requirement.

For `Re z>0`, the arguments `s` and `1-s` have nonzero imaginary
parts and avoid the chosen cut. The explicit logarithm branches give
`m_t(conjugate(s))=conjugate(m_t(s))`. Under `z` conjugation, the two
arguments interchange after conjugation, proving real symmetry of
the fixed finite sum. There is no hidden antiholomorphic term.

Differentiating the logarithm of a summand gives

    (alpha(s)-log n)(1+t alpha'(s)/2).

Together with `s'=-i/2`, this verifies both signs and factors in the
displayed derivative formula (8). The common-normalizer derivative
`A_t'/A_t` is also correct.

## 2. Symmetric normalizer and complete disk majorant

The normalizer is the exponential of the average of the two analytic
logarithms, hence is nonzero throughout the right half-plane used here.
It is real and positive on the real axis and has conjugation symmetry.
Its inverse introduces no poles inside a Cauchy disk. Normalization
therefore preserves simultaneous zeros and allows errors to be reflected
without changing their modulus.

The elementary derivative bounds in (9)--(10) follow directly from
the indicated rectangle. In particular:

* `Re(1/(2s))>=0`, while `Re(1/(s-1))>=-V^-2`.
* Both moduli lie between `V` and `S`, with nonnegative real parts,
  so the logarithmic modulus and argument bounds used for `A_*` hold.
* `alpha'=-1/(2s^2)-1/(s-1)^2+1/(2s)` gives the stated `D_*`.

The vertical derivative of `(m_t(s)-m_t(1-s))/2` has modulus at most
`L_*/2`. Its real part is zero at `y=0`, giving exactly
`|M_t(s)/A_t|, |M_t(1-s)/A_t|<=exp(RL_*/2)`. This verifies the
essential normalization factor `K_*`.

The natural cutoff always lies between `m_-` and `m_+`. The squared
root argument varies by at most `1/(2pi)+1/32<1`, and the root itself
varies by less than one, so its floors differ by at most one. Since
`X-R>=200`, `m_->=3`. None of these observations removes a cutoff
term without paying for it.

The majorant `V_n` correctly maximizes the affine heat exponent over
time endpoints; it retains its negative sign when appropriate. The
second reflected sum requires the additional `n^(R/2)` factor in
`P_n`. This is present in the fixed-cutoff correction. The bound on
the source's `gamma` is at most one since `x/(4pi)>1` by a large
fixed margin, and its `kappa` bound gives exactly `k_*`.

The logarithmic error factor `U_n` majorizes the source error for
every allowed `x,t,n`. The absolute logarithm takes its maximum at
one of the two `q` endpoints. The constants `0.626` and `6.66`
are retained in their source positions.

For the remaining source error, positive `log q_-` allows the
negative heat exponent to be bounded by `-epsilon log(q_-)^2/16`.
The prefactor is bounded by `q_-^(-1/4)`, and `3^y+3^(-y)` increases
with nonnegative `y`. The denominator `m-0.125`, the constants
`1.24`, `10.44`, and the denominator `x_--12` are all preserved.
Thus no part of the source remainder has been omitted from (14).

Changing the natural cutoff to any fixed `N` costs the exact missing
or extra range of indices in each of the two finite sums. Their
normalized individual bounds are `K_*P_n`, giving the factor two
and the stated finite correction. The upper half-disk estimate then
reflects to the lower half by the real symmetry of the normalized
remainder. The scalar source theorem itself is not extrapolated there.

## 3. Derivative and collision criterion

The remainder is holomorphic on a neighborhood of each closed disk,
with modulus at most `eta_N`. Around a real point within distance
`a<R` of its center, the disk of radius `R-a` remains in that disk.
Cauchy's derivative bound is therefore exactly `eta_N/(R-a)`.
No derivative of a moving integer cutoff or a merely pointwise
remainder is used.

At a hypothetical common zero, both the finite normalized value and
its derivative must lie within their respective errors. A certified
lower bound for either throughout a cell therefore excludes a
collision throughout that cell. The note correctly requires infima
or interval coverage, not sampled center inequalities.

For `N=1`, the finite sum is `2cos(theta_t)` and its derivative is
`-2theta_t' sin(theta_t)`. On the real axis,
`theta_t'=-Re m_t'(s)/2`; the error bound for `alpha alpha'` gives
the displayed positive lower bound `omega_*` for its magnitude.
The two hypothetical smallness inequalities contradict
`cos(theta)^2+sin(theta)^2=1` precisely under (20). The argument
does not require numerical knowledge of the oscillatory phase.

## 4. Independent audit of the explicit height constant

The bound `exp(64/epsilon)` was checked independently of the final
rational script. For `0<epsilon<=1/2`, it gives `X>=exp(128)`.
Writing `L=log(X/(4pi))` and `R=1/L`, the elementary inequalities
`log(4pi)<2.6` and `|log(q_+/q_-)|` extremely small imply

    L>125, log q_->125, epsilon log q_->62, R<1/125.

The definition of `m_+` gives
`log m_+<=log q_-/2+0.01`. The elementary functions in (9) satisfy
`A_*<=0.51L`, `D_*<0.001`, and `alpha_-/L>0.499` throughout this
range. Consequently `K_*<exp(0.26)<1.3` and
`R omega_*>0.24`. Each has substantial numerical slack.

The logarithm of every retained index is below `2alpha_-`, so its
heat exponent is nonpositive. The resulting tail exponent obeys

    p > 0.496+62/8-0.0015 = 16489/2000 > 8.

The positive-index finite correction is therefore bounded by the
convergent tail `sum_(n>=2)n^-8<=1/256+1/896=9/1792`.
This bound is uniform in every possible natural cutoff and every
time in the specified interval.

For completeness, the `10^-40` source-error bound is conservative:
the exponent in `U_n` is at most

    [(log X)^2/64+0.626]/(X-R-6.66).

For `X>=exp(128)`, bound the denominator below by `X/2` and use
the decreasing functions `(log X)^2/X` and `1/X`. The result is
well below `10^-40`, even after replacing `exp(v)-1` by `2v`.
The bounded factor `m_+^(k_*)<2` and the convergent power sums give
the displayed `4*10^-40` total. This step does not multiply that
error by the enormous number of unweighted terms.

In the last remainder, `epsilon log q_->62` and `log q_->125`
make the heat exponent smaller than `-484`. Its positive terms sum
to less than three: the first is already below `1.44` using only
`m>=3`, `R<=1`, and the second is negligible at `X>=exp(128)`.
Thus its `10^-100` bound is also conservative.

These estimates give

    eta_1 < 1.3[4*10^-40+10^-100+2(9/1792)] < 0.014.

Finally the phase-independent contradiction has left side at most

    (0.014/2)^2+(0.014/0.48)^2
       =32389/36000000 <1/1000<1.

This proves exclusion at the arbitrary real center `X` for every
`t>=epsilon` in the source time range. Evenness handles negative
real centers. No floating heat evaluation, presumed RH verification,
or unrecorded compactness constant enters this derivation.

## 5. Retained limits

The explicit high-height statement is conditional only on the published
effective approximation theorem, used within its stated domain. It
does not eliminate the interval below the cutoff, and that interval
diverges as the positive time floor decreases to zero. The complete
normalized certificate format is useful progress, but no numerical
rectangle implementation or all-positive-time arithmetic lower bound
has been supplied.

The `N=1` leading-pair reduction is an effective Riemann--Siegel
approximation with its entire finite tail and analytic remainder paid.
It is different from the fixed theta truncation already proved
unsuitable at large height. The note keeps that distinction and
does not posit an Euler product for the heat flow.

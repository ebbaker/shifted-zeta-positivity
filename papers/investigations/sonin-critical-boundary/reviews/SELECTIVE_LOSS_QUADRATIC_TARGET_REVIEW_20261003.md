# Internal audit: quadratic diagonal and finite signed-pair theorem

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. Separate agents used the inherited
configuration. This is an internal same-model audit, not independent
specialist refereeing or a novelty assessment.

## 1. Result and proof scope

The [main note](../notes/selective-loss-program/05_quadratic_target_and_finite_sign_20261003.md)
establishes the unconditional global diagonal bounds

\[
\max(0,Y^2/4-48)\le D(Y)\le2\log2\,(Y^2+17/16)
\quad(Y\ge0).
\]

The outward scalar constants and published finite-height zero verification
then prove Theta(Y)<-5 for every real 100<=Y<=225. The positive part is
taken only after the complete signed off-diagonal sum. This is stronger
than a collection of sampled signs, but it has bounded Y range.
The global quadratic target remains open.

## 2. Analytic checks

The count bound psi(x)<=4(log2)x follows from dyadic binomial valuations.
The lower psi bound uses a largest binomial coefficient dividing the
least common multiple; floor(x)-1 handles real x without an endpoint
rounding error. Prime-power subtraction and decreasing elementary
error ratios give theta(x)>=x/2 from x=e^10 onward.

Both Stieltjes partial-summation signs were checked. For the upper
diagonal, the integral where f'= (1-log x)/x^2 is positive can be
discarded; for the lower diagonal, -f' is nonnegative throughout the
retained prime range. The lower constant is 20+40log2<48. The exact
convolution D=int g^2 A_2(Y-v) retains the entire partial-packet cap;
evenness removes the linear Yv term. The small-Y case is covered by
D>=0 because Y^2/4-48<0 below 10+a. No PNT rate, RH assumption, or
zero verification enters this global diagonal sandwich.

The transform convention G(s)=int g(v)e^(-sv)dv has the factor
s(1/4-s^2). The distributional D^6 bound includes both endpoint
atoms; omitting them would invalidate the decay constant. The exact
interior norm and endpoint total variation were reconstructed. The
resulting K is about 4.816053226*10^9; a rounded value 4.815*10^9
would be below it and is not used in the certificate.

The linear zero expansion counts both imaginary signs and multiplicity.
Its sixth-power tail integration has coefficient twelve, with the
nonpositive boundary contribution omitted. Criticality is used only
through the published verified height. Above it the allowance retains
exp(y/2) and exp(a/2). The critical tail majorant is permitted to extend
to infinity as a counting bound for a finite segment; it is not an
assertion that those higher zeros are critical. The trivial-zero
majorant is used only from y=1, where it is finite and decreasing.

The critical segment is independent of y in absolute value, the unknown
tail increases with y, and the trivial tail decreases. These facts
justify a continuous bound on [1,225], with no sampled interpolation.
The initial J(1) triangle bound uses only n=2,3 and the unit packet norm.
The exact D-J margin is 53409/10000 at Y=100; its derivative thereafter
is at least 252991/10000. Therefore the strict -5 sign statement follows
throughout the interval. The corresponding allowance range
r in [399/4,899/4] and coefficient 2sqrt(log2) were also checked.

## 3. Numerical implementation and replay

The [package](../numerics/selective_loss_quadratic_target_20261003/README.md)
contains exactly two outward production records, at 192 and 256 bits.
The generator checks N(500)=269 as well as gamma_269<500<gamma_270,
enumerating 270 ordered disjoint consecutive enclosures. Real parts
are exactly 1/2, consistently with the published finite-height theorem.
This checks completeness rather than merely counting a supplied list.

Both production runs passed their strict thresholds. Their combined
uniform p bound is enclosed near 4.966694406960983244 and is below
497/100; the initial energy bound is enclosed near 1.264304982113347
and is below 127/100. Each record identifies the generator by its
SHA256 hash and stores rational enclosure endpoints. The two
cross-precision enclosures overlap for every retained scalar quantity.

The standard-library [replay](../numerics/selective_loss_quadratic_target_20261003/replay.py)
passed its hash, interval, threshold, norm, derivative, and final-margin
checks. It additionally checks exact cumulative-autocorrelation values
at 1/16, 1/8, and 1/4. The middle value is negative and the other two
are positive, verifying the sign-change obstruction used in note06.
The small [replay record](../numerics/selective_loss_quadratic_target_20261003/replay_record.json)
records the result and its limited scope.

This replay checks arithmetic on retained records and exact polynomial
algebra. It does not regenerate the rigorous zeros, validate FLINT's
implementation, or prove the cited finite-height/counting theorems.
The outward production generator, published inputs, and analytic proof
must be assessed together. No dependencies were installed, no large
prime sieve or dense pair matrix was constructed, and no full A or B
inverse or source-wide residual certificate was computed.

## 4. Global-mechanism audit and the next target

The [mechanism note](../notes/selective-loss-program/06_global_mechanism_tests_20261003.md)
keeps the endpoint term in the differential energy. Its exponential
continuum cancellation prevents dropping that term in an upper bound.
The positive frame operator has a valid linear Bessel bound and quadratic
trace, but the coherent coefficient vector has exponentially many
entries. The discrete countermodel tracks a monotone oscillatory
counting function with weights in {0,log n}; it has PNT and a quadratic
diagonal yet exponential response energy. It is not the actual prime
sequence and makes no Euler multiplicativity claim.

The exact multiplicative normalization is
p(log x)=x^(-1/2)V(x), so J uses dx/x^2. The next sufficient theorem
is the fixed-kernel actual-prime bound

\[
\int_X^{2X}|V(x)|^2dx\le C_gX^2\log(2X).
\]

Its complete signed-pair formulation and signed Selberg covariance
formulation are supplied in note06. The strong conventional Selberg
bound cited there assumes RH; the unconditional relative-error scale
is larger by a factor of X at fixed relative interval length. No
unconditional small variance theorem is inferred from that literature.

The [weighted note](../notes/selective-loss-program/07_weighted_energy_abscissa_20261003.md)
first establishes physical convergence before substituting the
arithmetic Laplace value. Its positive-weight convergence abscissa is
the supremum of Re rho-1/2. A meromorphic norm on one shifted line
cannot substitute for half-plane analyticity and a uniform Hardy norm;
the explicit single-pole example verifies the distinction. The known
epsilon=1/2 endpoint does not reach arbitrarily small weights.

The future global variance, signed-pair, and small-weight energy bounds
have RH strength for this noncancelling probe. The finite theorem and
these reductions identify a concrete research obligation without
establishing the global arithmetic cancellation.

## 5. Saved-artifact checks

The notes, review, source, preflight, and scalar records are placed in
the existing investigation folders. The overview and investigation
index link the results and preserve the open global status. The prior
signed-pair note receives only a continuation link. All added files
are far below the repository's one-megabyte convention. No manuscript
revision, new manuscript snapshot, commit, or push is part of this
continuation.

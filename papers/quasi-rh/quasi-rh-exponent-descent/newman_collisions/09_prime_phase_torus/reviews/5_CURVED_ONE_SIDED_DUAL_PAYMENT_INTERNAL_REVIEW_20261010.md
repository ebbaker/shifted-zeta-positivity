# Internal review: sharp one-sided candidate-null payment

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6.1-sol (Codex); reasoning effort ultra, verified from the
parent chat's recorded configuration. This review and the agent
cross-reading are internal LLM checks, not independent validation.

Reviewed [Note 5](../notes/5_SHARP_ONE_SIDED_DUAL_PAYMENTS_ON_CORRELATED_CANDIDATES_20261010.md)
and [checker](../numerics/check_curved_one_sided_dual_payment.py).
The result supplies a stronger general payment, without an actual
prescribed-coefficient upper bound for the threshold sign.

The transformation `e=D(s,v)` is exact for
`s=F_N/eta`, `v=F_N'/(L eta)`. Its second row retains
`A=-d mu`, so it keeps the physical amplitude drift. The candidate
condition is precisely `s^2+|v|<=1`. It simultaneously keeps both
lower approximation errors and sharpness is correctly limited to
the enlarged class of local bounded holomorphic error jets.

For `K_dual=K+q`, the sufficient upper payment is `max(-q)`,
not `max|q|`. Thus `K<=U+Pi^-` if `K_dual<=U` and the actual
candidate lies in the body. This proves the displayed sufficient sign.
Positive semidefinite pure candidate-null quadratic terms have zero
one-sided payment. Their actual dual upper bound can increase, so that
fact gives no free sign. Equation (15) proves the exact protection
`K_dual+Pi^- >= K` at each compatible actual candidate.

The boundary is exhausted by the two parabola edges and their common
endpoints. Each edge restriction is a quartic and its derivative is the
printed cubic. The nonsingular stationary-point formulas solve
`Hz=-g` with the correct determinant. In the singular case, any
stationary ridge has constant objective and reaches the boundary of the
bounded convex body. No pseudoinverse, missing interior extremum, or
definiteness assumption is hidden. Constant edges and the identically
zero objective are covered by endpoint values.

For fixed candidate coordinates the objective is affine in the three
higher moments; one common moment-box corner attains its maximum.
Taking the maximum over eight corner payments is therefore exact on
the specified independent product class. The corresponding 32-corner
formula for rational intervals of all five transformed coefficients is
proved in the same way. It gives an outward path for actual irrational
physical data after certified coefficient enclosure. Dependencies lost
when forming a box may allow a smaller payment; no sharpness claim
is made for the actual arithmetic subset.

The closed-form classes are checked analytically. Negative diagonal
terms pay `max(a,b)` because their boundary objective is convex in
`s^2`; a pure cross term pays `4|beta|/(3 sqrt(3))`; linear terms
give the support formula of Heat Note 18. The parameter payment is a
maximum of linear functions of the dual, so convexity, nonnegative
homogeneity, subadditivity, and the active-witness subgradient follow.
Uniformly bounded duals retain the earlier shrinking exponential scale;
the new result improves sign handling and constants.

The checker uses exact Fraction polynomial division, removes repeated
critical roots, and isolates all relevant roots by signed remainders.
At a zero of an internal remainder in the sign chain, its adjacent
nonzero entries have opposite signs, so the sign variation is unchanged
when passing that zero. At a simple root of the first polynomial the
variation decreases by one, since its next entry is its derivative.
After square-free division, this proves the root count as the difference
of endpoint variations. Endpoint critical roots are deflated because
the boundary endpoint values are already included. Exact midpoint roots
are deflated and the remaining polynomial is restarted, avoiding root
endpoint ambiguity. Root intervals from separate deflation branches
need not be disjoint; completeness and outward polynomial evaluation
are sufficient for the payment enclosure. The source makes no blanket
disjointness claim.

Rational interval Horner evaluation encloses each critical value. The
minimum of these intervals encloses the exact global minimum, and its
negative gives the outward payment. **10,081 exact assertions** cover
known global extrema, singular/constant cases, cubic isolation,
12 drift-containing controls, the eight moment and 32 coefficient
corners, and all four common-frequency dual channel signs. The run
evaluates **233 critical root intervals**. A separate `--output`
replay matches the [retained source-bound record](../numerics/curved_one_sided_dual_payment_record_20261010.json)
byte for byte. The agent cross-reading checks the same formulas and
their proof scope; it is not external specialist review.

Every physical Bell residual, the exact normalizer, complete cutoff,
carrier, amplitude motion, two candidate tolerances, reflected product
channel, difference channel, both sine terms, and block/core cross
interference remain present. Holomorphic Schur error constraints do not
absorb Bell residuals without a separate disk bound. The Gaussian
hierarchy's auxiliary states are still unconditioned by the actual
mean candidates.

No finite payment control is an actual prescribed arithmetic collision
state. The missing uniform arithmetic pair upper bound remains required
for the paid exclusion. There is no new collision exclusion, Newman
bound, RH implication, higher-multiplicity theorem, endpoint coverage,
or priority claim. Earlier project notes, checker sources, and records
are preserved; all added files are small under the repository rule.

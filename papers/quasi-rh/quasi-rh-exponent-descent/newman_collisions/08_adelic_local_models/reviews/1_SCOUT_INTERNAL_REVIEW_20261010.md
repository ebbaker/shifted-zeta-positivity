# Internal scout review: 08_adelic_local_models

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are unavailable and are not inferred. Internal LLM checks are not
independent mathematical validation.

Scope: review of [Note 1](../notes/1_SHARED_HEAT_COORDINATE_AND_DIAGONAL_RATIONAL_COMPATIBILITY_20261010.md) and the associated
[exact checker](../numerics/check_adelic_scout.py). This review was performed by
the same LLM research scout. It is an internal audit and must not be
represented as independent validation or specialist mathematical review.

## Findings

All composites up to six are retained, including 4 and 6. The cutoff support is a joint valuation constraint rather than a tensor-product cutoff. The shared Gaussian has variance `t/2`, exactly yielding `exp(t log^2 n/4)`. The independent-prime model misses the strict mixed factor at 6. Both reflected branches and the carrier are preserved, with amplitude drift included in the raw derivative multipliers.

The diagonal generator, finite cutoff, and every local unit twist commute. Thus shared Gaussian coupling repairs coefficients without removing the known multiplicative-relaxation obstruction. The global condition in the note is stated before drawing any phase consequence: triviality on diagonal rationals and trivial finite-unit characters forces `chi_p(p)=p^{-a}` by evaluating a diagonal prime. At each Gaussian slice the common complex exponent is `a=eta-lambda`. Their superposition is not one character.

The note correctly distinguishes a finite coefficient control from the complete genuine approximant. Positive-time heat Dirichlet terms fail to tend to zero, so no infinite-series or Euler-product interchange is justified. A globally compatible orbit still requires exact physical carrier/weight motion and has no supplied signed exclusion theorem. Infinite adelic domains and a surviving sign remain open.

## Reproducible checks and limitations

The retained checker run passed 440 exact assertions and a fresh
repeat reproduced its small record byte for byte. The record binds its
source SHA-256. Six-term valuations, mixed heat polynomial, Gaussian moment coefficients, four raw-jet recurrences, and formal diagonal-rational exponent cancellation.

The six-term model is an algebraic control, not a shrinking-sector cutoff or an infinite adelic realization. Gaussian moments and formal character compatibility do not certify a new actual-phase sign.
The formal checks do not certify the imported analytic theorems, limiting
interchanges, uniform asymptotics, actual collision signs, or RH. Their
counts are not a measure of the depth or likelihood of the proposed route.
All files obey the source/small-record convention in `LARGE_FILES.md`.

## Milestones and disposition

| Milestone | Status |
| --- | --- |
| Exact representation | Established in the stated finite or full-kernel domain |
| Additional identity or scoped obstruction | Established as printed in Note 1 |
| Paid signed collision exclusion | Not established |
| Coverage sufficient for an endpoint conclusion | Not established |

Feed diagonal-rational compatibility into a coupled theta/prime model. Its next test is an actual-orbit signed moment relation, with full analytic payments, rather than an all-torus lower bound.
No theorem beyond the stated scopes or literature-priority claim is approved
by this internal audit. Independent specialist and literature review remain
necessary before treating these results as independently validated.

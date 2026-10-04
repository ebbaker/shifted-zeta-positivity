# Prime variance exponents

Prepared for Edward Baker, 3–4 October 2026, with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.

This project develops a focused manuscript about decreasing the global
variance exponent of one explicitly prepared prime response. For each
delta in [0,1], the bound Vcal_g(X)=O(X^(2+delta)) is equivalent to all
nontrivial zeta zeros lying in the closed strip of half-width delta/2
around the critical line. Bounds along exponents tending to zero are
equivalent to RH.

The [draft manuscript](manuscript.tex) is the single editable source.
It contains full proofs of the probe properties, the fixed-exponent
equivalence, the PNT-envelope transfer, the finite quadratic transfer,
the signed short-interval reduction, and the finite-prefix obstruction
to a generic exponent-descent rule. The acknowledgement identifies
substantial LLM assistance and the limits of internal review.

The built-in LaTeX compiler reports success. Fresh internal proof passes
and a primary-source audit are recorded below. The finite variance
generator was replayed into a temporary output and matched its retained
record byte-for-byte. The previous 192/256-bit outward zero calculations
and the published finite-height verification were not regenerated.

| Result | Status and scope |
| --- | --- |
| Fixed-exponent variance bound iff closed zero strip | Proved for each delta in [0,1], including endpoints and strip boundaries |
| Bounds along positive exponents tending to zero iff RH | Proved; no uniform constants or thresholds required |
| Global baseline delta=1 with a Johnston–Yang subpower factor | Established transfer of a published PNT theorem |
| Variance <38 X² through 10⁹⁹, <40 X² through 10¹⁰⁰, <72 X² through 10¹⁰², starting at e | Continuous finite certificates using the identified outward inputs |
| Signed short-interval covariance at h=X^(3/4) | Exactly the same admissible exponents; norm approximation error O(X) |
| Finite-prefix generic obstruction | Proved for constructed coefficients, not a counterexample involving actual primes |
| Any fixed global delta<1 for actual primes | Open |
| Actual-prime exponent-descent rule | Open |

## Initial delta investigation — 4 October 2026

The [first investigation outcome](notes/INITIAL_DELTA_INVESTIGATION_20261004.md)
proves that the exact Möbius divisor expansion can discard all d≤X^(9/10)
with shell energy O(X^(9/5)(log X)²). The unresolved signed sum then has
cofactors k≤2B X^(1/10). A sharper limiting cutoff leaves only
O(X^(1/12)(log X)^(1/6)) cofactors, with quadratic discarded error.
These are proved bounds for arithmetic sectors; the retained sum still
needs a power-saving estimate.

A balanced Vaughan reduction and a sixth-order short-interval
reconstruction provide two further precise options. The
[finite pilot](numerics/mobius_reduction_20261004/README.md) finds strong
signed cofactor cancellation on six tested shells and checks the exact
identities, without fitting or claiming a global exponent. Fresh internal
proof and code reviews passed. The
[source audit](notes/BILINEAR_INPUT_SOURCE_AUDIT_20261004.md) identifies the
additional polynomial Mellin estimate that one modern Type II route would
need; the available μ/Λ applications give logarithmic savings.

These new results are retained in research notes. They have not yet been
inserted into the manuscript.

See [verification status](VERIFICATION_STATUS.md) for the precise check
scope and [draft history](DRAFT_HISTOR.md) for the manuscript milestone.
No independent specialist refereeing or mathematical priority is claimed.

## Review and reproduction

- [Core proof review](reviews/CORE_PROOF_REVIEW_20261003.md)
- [Arithmetic and countermodel review](reviews/ARITHMETIC_REVIEW_20261003.md)
- [Primary-source and bibliography review](reviews/SOURCES_REVIEW_20261003.md)
- [Certificate replay and exact polynomial checks](reviews/CERTIFICATE_REPLAY_20261003.md)
- [Final manuscript verification](reviews/MANUSCRIPT_REVIEW_20261004.md)
- [Arithmetic localization proof review](reviews/ARITHMETIC_LOCALIZATION_REVIEW_20261004.md)
- [Möbius pilot and higher-order reconstruction review](reviews/MOBIUS_PILOT_REVIEW_20261004.md)
- [Existing small finite variance package](../investigations/sonin-critical-boundary/numerics/subpower_finite_variance_20261003/README.md)
- [Existing outward package](../investigations/sonin-critical-boundary/numerics/selective_loss_quadratic_target_20261003/README.md)

The [original continuation note](notes/MANUSCRIPT_CONTINUATION_20261003.md)
records the drafting scope. Detailed source research remains in the
[parent subpower program](../investigations/sonin-critical-boundary/notes/subpower-milestones/README.md).
The parent manuscript and its numerical packages are unchanged. No large
data or draft snapshot folders are duplicated here.

The next global research step is a genuine fixed power saving for the
retained signed Möbius-cofactor covariance, or the centered balanced
Vaughan sum, with every cutoff and continuum term included. The original
short-interval route remains available, now also with sixth-order
reconstruction at h=X^(11/12). Increasing verified zero heights can
instead extend the finite quadratic range on the scale H^10/(log H)^2;
that is a separate finite milestone.

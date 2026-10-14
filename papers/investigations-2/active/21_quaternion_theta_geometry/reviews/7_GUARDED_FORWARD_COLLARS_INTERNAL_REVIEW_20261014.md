# Internal review of guarded forward stationary collars

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**.
The parent session verified its actual current-turn configuration in the
recorded rollout; this reviewing subtask inherited that configuration.

This is an independent internal LLM review of
[Note 10](../notes/10_FORWARD_STATIONARY_COLLARS_AND_BRANCH_CREATION_20261014.md),
including its complete-source moment bounds, guarded continuation theorem,
quartic heat control, and concrete collar replay. It is not specialist refereeing or formal
verification. No correction is required to the stated theorem.

The moment envelope includes every index. Dropping the negative source
summand and using the quadratic lower bound for exp(4u) leaves the
nonpositive quadratic term -(8 alpha_n-tau)u^2 for tau<=1. Its removal
gives equation (2). The ratio in equation (3) bounds each successive
positive tail term from n=N+1 onward; the omitted denominator ratio is
less than one. Thus neither the integration half-line nor the infinite
index sum is left unpaid.

For the derivative pair (h_(j+1),h_(j+2)), the time derivative is
(-h_(j+3),-h_(j+4)). The Euclidean triangle inequality therefore proves
the full-slab gap (9). The separate edge guard preserves both boundary
signs. These are complementary requirements: the pair gap prevents
stationary degeneracy anywhere in the interval, while the edge guard
prevents roots from entering or leaving it. Compactness and the implicit
function theorem then continue every root both to the end and back to
the base slice. This proves complete branch coverage, including the
absence of newly created stationary pairs. Regularity and nonzero edges
also prove finiteness on the base slice.

On a regular branch the identities chi'=h_(j+3)/C and A'=-C are correct.
Since C retains its sign, the initially opposite sign of A persists
forward and its absolute value increases. The strict stationary sign
and the energy lower bound follow without dividing by an unknown norm.
Differentiating C gives equation (10), hence the curvature lower guard
and logarithmic drift estimate (13)--(14), with the stated continuous
limit when its denominator moment is zero. Individual drift control
does not by itself exclude another stationary branch elsewhere; the
note explicitly retains the global derivative-pair guard.

The quartic control obeys backward heat. At negative delta its only
first stationary point has positive first sign and its second stationary
set is empty. At delta=0 the derivative acquires a triple root while the
scalar value is nonzero. Afterward the central first sign is negative,
the outer first signs are positive, and the second signs are
48 delta^2>0. Direct coefficientwise and exact-rational checks of the
heat identity and six displayed control consequences all pass. These
checks supplement the direct formulas; they do not certify a theta
collar. The control correctly shows why initial signs alone cannot
replace the birth guard.

The additional rational moment cap (3a) is valid: for m>=1 the remaining
n^(2-2m) factor is at most one, while the consecutive ratios of
q^(n^2) are at most q^3. This pays the complete moment sum without a
finite cutoff. The exact
[collar checker](../numerics/check_forward_stationary_collars.py)
was inspected and replayed from a temporary copy outside the repository.
All 234 checks pass, and its regenerated
[record](../numerics/FORWARD_STATIONARY_COLLAR_CHECKS_20261014.json)
equals the repository record. It checks the exact byte hash of the
previous source certificate before using that record's dyadic endpoints.

The derivative-pair floors use the maximum of the two interval distances
from zero on every closed cell. This is a valid lower bound for the
Euclidean pair norm, including cells in which the broader stationary
derivative enclosure contains zero. The full first/last cell enclosures
give valid edge floors. The original direct or monotone-endpoint
exclusions are rechecked, and the three retained root cells have strict
opposite amplitude/curvature signs and paid amplitude floors. Hence the
base slice at t=3/50 satisfies every theorem hypothesis. The global
moment sum caps dominate the required Euclidean speeds. The strictly
positive step Delta=1/200000 pays both derivative and edge guards.

Consequently the stated collar [3/50,12001/200000]x[7,41] is established,
with stationary margins 279/2000000000000 and 3/500000000000 for the
two levels. Both the signed margins and the stationary energy floors
are correct exact products of the stated amplitude and gap floors.
This is a small explicit application of the theorem, although the
separate full-time calculation covers a much larger time range.

The theorem still requires paid slice gaps and edge margins for each
further collar. Absolute source moments need not scale with increasingly
small slice gaps at large heights. The note correctly makes no uniform
all-height continuation or RH conclusion, and restricts homogeneous heat
propagation to the complete theta observation rather than its separately
compensated channels. The checker verifies finite algebra and record
payments; the analytic compactness argument supplies complete branch
coverage.

# Review of the subpower milestones program

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Separate same-model agents checked the fixed-exponent formulation and PNT
transfer. These are internal checks, not independent specialist refereeing.

The author requested a dedicated quantitative investigation of decreasing
delta in the global prepared-probe variance. The new
[program folder](../notes/subpower-milestones/README.md) establishes that
focus without assuming an available mechanism for successive improvement.
The existing LaTeX manuscript and its open editor are retained unchanged.

## Mathematical assessment

For the existing noncancelling probe and each delta in [0,1], a global
variance bound O(X^(2+delta)) is equivalent to the assertion that every
nontrivial zero has real part at most 1/2+delta/2. The forward argument
uses the existing shell and weighted transfers. The converse uses the
absolute linear zero expansion with sixth-power coefficient decay,
uniform across the critical strip. At delta=0, cumulative J is O(1+Y),
not necessarily bounded. Boundary zeros are allowed for positive delta,
and weighted convergence at epsilon=delta/2 is not claimed.

Thus the first fixed delta below one would already be a substantial
all-height zero-free theorem. The current research contains no bootstrap
improving a proved delta to a smaller one. The central projection is a
possible technical method inside this program, not an independent goal
whose completion must precede the exponent investigation.

The new baseline transfer preserves the complete smoothing band:
V_g(x)=-integral E(xu)w'(u)du. A relative Chebyshev-error envelope r gives
variance at most (7/3) M_w squared X cubed times the supremum of r squared
over [AX,2BX]. This requires no monotonicity assumption and retains both
caps. The factor 7/3 follows by integrating x squared over [X,2X].

[Johnston–Yang, Theorem 1.4](https://arxiv.org/pdf/2204.01980) was checked
against the full primary PDF. Its unconditional constants and range
t at least 23 give the exact source-dependent supremum bound for
X at least 23/A. Uniform proportional rescaling preserves the asymptotic
coefficient 0.3706 in the squared envelope. The result strengthens the
previous square-root-logarithm saving but leaves the global power at
delta=1. It is a transfer of a known theorem, not a new power-saving
arithmetic input. No numerical constant enclosure or certificate was
generated for this baseline.

The candidate budget X squared L(X) plus X^(3-kappa)L(X), with positive
kappa and L=X^o(1), gives every delta above max(0,1-kappa). It need not
give the endpoint if L is unbounded. This distinction is recorded in
the charter and ledger. Fixed logarithmic savings, finite-range fitted
slopes, and improved constants are not entered as smaller global deltas.

A proposed growing-height bridge was not retained: an autocorrelation
tail cannot be squared and reused as a linear-response tail without a
separate derivation. Fixed-height information alone does not establish
the unbounded-height zero strip required for a global exponent.

The literature check was targeted rather than exhaustive. The published
[Mossinghoff–Trudgian–Yang regions](https://arxiv.org/abs/2212.06867) and
the inspected [2026 classical-region preprint](https://arxiv.org/abs/2603.21490)
have boundaries approaching one with height. No claim is made that
these inputs yield a fixed global strip. The program's completed baseline
uses the established Johnston–Yang input; recent preprints can be audited
separately before formal adoption.

## Scope and records

The folder contains a charter, a proved baseline and exponent-budget note,
and a milestone ledger. It links the existing notes 07, 09, and 10 without
moving or duplicating their source files. Numerical work, if undertaken,
belongs in the investigation's numerics folder; reviews belong in reviews.
The investigation index and selective-loss overview link the new program.

Local links and file sizes were checked. No manuscript edit, new manuscript
milestone, draft snapshot, numerical run, commit, or push is part of this
program setup. The first global fixed exponent below one remains open.

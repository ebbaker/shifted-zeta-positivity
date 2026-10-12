# Arithmetic source audit

[Investigation index](../README.md)

12 October 2026. Prepared for Edward Baker. Model: GPT-6 Astra
(`gpt-6-astra`). Reasoning effort: ultra. Prepared with substantial LLM
assistance. Internal model reviews are not independent mathematical
validation or formal verification.

## Objective and current status

Locate and audit the source of the power saving in the imported quasi-RH
arguments, beginning with one complete, nonempty cube-tail branch of the
October 5 argument. The objective is a closed analytic chain or a precise
account of an unresolved step. It is not another conditional exponent-descent
paper.

**Status: scoped; research not started in this project.** The existing
September 30 upstream audit inspected reflection, primitive Poisson, and
sieve interfaces, but explicitly left the global sextic norm recursion and
combined induction unresolved. Repeating those local checks would not
complete this project. Neither the imported baseline nor a stronger strip
is validated by this scaffold.

## First bounded task

1. Pin the source versions and record their provenance. Make a one-page
   dependency map distinguishing family averages, fixed-character estimates,
   extraction, continuation, and imported analytic assertions. Select a
   branch whose inputs are genuinely nonempty.
2. Fix one admissible coefficient profile and follow it through cube
   removal, both Poisson transforms, and return to the claimed energy class.
   Retain support, coprimality and zero-extension masks, primitive-character
   restrictions, coefficient norms, derivative orders, and coherent terms.
3. Identify the parameter that decreases, the base case, and every
   uniformity requirement. Distinguish constants allowed to depend on a
   fixed character from exponent margins that must remain uniform.
4. Trace the principal-character case and record exactly where its bound
   comes from. Extraction from an independently proved positive moment is
   legitimate; the presence of a coherent row is not itself circularity.

Consequence checks belong inside this audit. Print each lemma's assumptions
beside any proposed corollary. In particular, the positive-slot fourth
moment at `kappa = 3/4` already assumes the relevant family boundary. It
cannot independently test that same boundary. Conductor-family and
zeta-height estimates must not be compared without matching their aspects.

## Deliverables and decision tests

Deliver a dependency map, a complete branch ledger, and a scoped review
report. Where useful, add small exact checks of normalizations or finite
arithmetic identities; these do not validate the unbounded induction.

Continue to additional branches only if the selected branch closes and the
origin of its saving is explicit. Pause downstream descent claims if the
argument requires an unproved transfer, leaves its declared function class,
or returns to its target without a decreasing parameter. A failed proof step
does not refute the theorem's conclusion; one successful branch does not
validate the whole theorem. An unexpectedly strong consequence calls for
inspection, not automatic rejection.

## Starting references

- [Corrected source-audit proposal](../../quasi-rh-exponent-descent/brainstorm/NEW_PATHS_FORWARD_BRAINSTORM_CODEX_20261011.md#2-d1-and-d6-audit-the-source-of-the-arithmetic-saving)
- [Upstream audit and outstanding obligations](../../quasi-rh-character-amplification/reviews/UPSTREAM_REFLECTION_POISSON_SIEVE_AUDIT_20261009.md)
- [Conditional theorem and dependency ledger](../../quasi-rh-character-amplification/notes/GEOMETRY_CONDITIONAL_THEOREM_AND_DEPENDENCY_LEDGER_20261009.md)

## Working records

Use `notes/` for derivations and source maps, `numerics/` for reproducible
checks and small records, `reviews/` for scoped assessments, and
`chat-histories/` for selected discussion records. Follow the repository
[large-file policy](../../../LARGE_FILES.md); third-party PDFs and large
regenerable outputs stay outside Git. Keep any manuscript at a stable path,
with author and LLM acknowledgement. Do not create manuscript snapshot
folders. Record notable milestones in a concise `DRAFT_HISTOR.md`, linking
the relevant commit or tag, notes, and reviews.

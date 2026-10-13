# Arithmetic source audit

[Investigation index](../README.md)

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Initial setup: GPT-6 Astra (`gpt-6-astra`), reasoning effort ultra.
The continuation records identify their own model and effort; this pass
uses GPT-6 (Codex), with exact serving variant and configured reasoning
effort not exposed. Internal model reviews are not independent mathematical
validation or formal verification.

## Objective and current status

Locate and audit the source of the power saving in the imported quasi-RH
arguments, beginning with one complete, nonempty cube-tail branch of the
October 5 argument. The objective is a closed analytic chain or a precise
account of an unresolved step. It is not another conditional exponent-descent
paper.

**Status: the pinned October 5 main-theorem chain has received a complete
scoped internal source audit on 12 October 2026.** The first branch,
theta transformation, initial Poisson reduction, completed mean square,
full two-Poisson transfer, finite canonical induction, and final assembly
close under their identified classical inputs. No additional unresolved
defect was found in the final links. This is not independent mathematical
validation or a newly established zero-free result.

The final ledger matches the canonical gap and short ranges to the
original moment, restores its outside factor D, extracts the fixed
character using sixth-power rows with strictly positive parameter choices,
and checks Mellin holomorphy and the meromorphic product identity. It
also handles the principal pole, norm-lift conductor shrinkage, finite
Euler corrections, and primitive or imprimitive Dirichlet characters.
The common qualitative exponent boundary does not require uniform
constants in conductor or zero height.

Earlier audits retain their own scopes and version correspondence.
The primary theta comparison uses Dunn–Radziwiłł v3; the original
Patterson proof was not independently read. The deep theta and
quadratic large-sieve theorems remain imports. The next scrutiny is
independent review of the full argument and those interfaces. The
manuscript's quantitative introduction corollaries and stronger later
strips were outside this source assembly.

## Manuscript

The [standalone manuscript](arithmetic_source_audit.tex) consolidates the
conditional source audit, from the initial reduction and completed mean
square through the full two-Poisson transfer and final assembly. It is
drafted for Edward Baker and includes an LLM acknowledgement. The final
source compiled successfully with the built-in LaTeX compiler.

See the [manuscript integration review](reviews/MANUSCRIPT_INTEGRATION_REVIEW_20261012.md),
[build record](numerics/manuscript_build_record_20261012.json), and
[concise manuscript history](DRAFT_HISTORY.md). The manuscript retains the
explicit classical dependencies and the audit's independent-review boundary.

## Final assembly records

- [End-to-end review and dependency boundary](reviews/FINAL_ASSEMBLY_REVIEW_20261012.md).
- [Canonical energy to the original mean square](notes/FINAL_ORIGINAL_MOMENT_ASSEMBLY_20261012.md).
- [Sixth-power extraction, positive loss choices, and Dirichlet norm lift](notes/FINAL_EXTRACTION_AND_BASE_CHANGE_20261012.md).
- [Mellin holomorphy, principal pole, and zero-dependent test](notes/FINAL_MELLIN_AND_ZERO_FREE_ASSEMBLY_20261012.md).
- [Exact final-assembly record](numerics/final_assembly_record_20261012.json), [CLI validation](numerics/final_assembly_cli_validation_20261012.json), and [replay guide](numerics/README.md#final-assembly-bookkeeping).

The new diagnostic passes 622 exact assertions, zero floating
comparisons, and thirteen negative-control families. It checks finite
normalization, exponent, scale-boundary and Euler-polynomial algebra;
it does not prove the analytic estimates or the zero-free theorem.

## Full two-Poisson transfer records

- [Combined review and next obligation](reviews/TWO_POISSON_TRANSFER_REVIEW_20261012.md).
- [Both arithmetic conversions and the complete signed preimage count](notes/TWO_POISSON_ARITHMETIC_LEDGER_20261012.md).
- [Smooth norms, principal modes, positive intermediate scales, and short ranges](notes/TWO_POISSON_SMOOTH_AND_SHORT_RANGES_20261012.md).
- [Every returned child, exclusion removal, and finite termination](notes/TWO_POISSON_RETURN_AND_TERMINATION_20261012.md).
- [Full-transfer exact record](numerics/full_transfer_bookkeeping_record_20261012.json), [CLI validation](numerics/full_transfer_bookkeeping_cli_validation_20261012.json), and [replay guide](numerics/README.md#full-two-poisson-transfer-bookkeeping).

The full cancellation is \(\tau(r)\mathbf1_{f'\mid k'}\), with the same
kernel for every preimage. It gives the child lower bound after all
divisor shifts. In a nonempty cube tail the row range decreases by at
least the squared gap ratio. These are analytical bookkeeping deductions
under the stated arithmetic and completed-family inputs.

The extended diagnostic passes 4,186,781 exact assertions with no floating
comparisons and eleven negative-control families. It includes 62,208
signed cases, 438,012 actual preimages, zero masks, short ranges, and
child scales. Finite parameter checks do not certify nonzero kernels,
analytic transformations, or an unbounded theorem.

## Completed mean-square audit records

- [Combined review, imported inputs, and next obligation](reviews/COMPLETED_MEAN_SQUARE_REVIEW_20261012.md).
- [All local branches and simultaneous exceptional-prime collisions](notes/COMPLETED_MEAN_SQUARE_LOCAL_LEDGER_20261012.md).
- [Primitive quadratic family, smooth separation, and infinite sums](notes/COMPLETED_MEAN_SQUARE_SIEVE_AND_SUMMATION_20261012.md).
- [General rows, shared factors, and inverse-square normalization](notes/COMPLETED_MEAN_SQUARE_GENERAL_ROWS_20261012.md).
- [Exact bookkeeping record](numerics/completed_bookkeeping_record_20261012.json), [CLI checks](numerics/completed_bookkeeping_cli_validation_20261012.json), and [replay guide](numerics/README.md#completed-mean-square-bookkeeping).

The new checker passes 198,323 exact finite assertions, with zero floating
comparisons and eleven negative-control families. The analytic proof
audit closes under its stated theta and quadratic large-sieve imports;
the finite checks diagnose identities and normalization rather than
establishing those imports or an unbounded theorem.

## Initial Poisson and arithmetic audit records

- [Combined review and next obligation](reviews/INITIAL_POISSON_AND_ARITHMETIC_REVIEW_20261012.md).
- [Gauss conversion, finite ray classes, and coefficient masks](notes/INITIAL_ARITHMETIC_CONVERSION_AUDIT_20261012.md).
- [Complete initial Poisson reduction, smooth norms, and dual ranges](notes/INITIAL_POISSON_REDUCTION_AUDIT_20261012.md).
- [Finite arithmetic record](numerics/initial_arithmetic_record_20261012.json) and [replay guide](numerics/README.md#initial-arithmetic-and-poisson-bookkeeping).

The new checker passes 113,748 exact finite assertions and 19,868 ordinary
floating comparisons, with twelve negative-control families. These
checks diagnose signs, masks, Gauss phases, and finite reindexing; they
do not prove the analytic estimates or an unbounded theorem.

## Theta audit records

- [Combined review, version correspondence, and next obligation](reviews/THETA_TRANSFORMATION_REVIEW_20261012.md).
- [Cusp construction and moving-prime uniformity](notes/THETA_CUSP_AND_UNIFORMITY_AUDIT_20261012.md).
- [Mellin normalization, continuation, and kernel bounds](notes/THETA_MELLIN_AND_KERNEL_AUDIT_20261012.md).
- [Primary theta coefficient comparison](notes/THETA_PRIMARY_SOURCE_COMPARISON_20261012.md).
- [Source versions and replay record](numerics/theta_version_crosswalk_record_20261012.json).

The audit supplies two explicit clarifications to the October 5
presentation: avoiding zero matrix entries before residue-symbol
manipulations, and expanding the strip-growth argument for the contour
shift. Both close under the stated inputs. The original Patterson proof
was not independently read; the primary formula comparison uses
Dunn–Radziwiłł v3.

## First audit records

- [Scoped review and source of the saving](reviews/FIRST_BRANCH_REVIEW_20261012.md).
- [Dependency map, principal case, and extraction](notes/DEPENDENCY_MAP_AND_EXTRACTION_20261012.md).
- [Nonempty cube-tail branch and return ledger](notes/CUBE_TAIL_BRANCH_AUDIT_20261012.md).
- [Pinned source provenance](notes/source_provenance_20261012.json).
- [Exact regrouping checks and replay instructions](numerics/README.md).

These are LLM-assisted research records, not independent validation. The
finite checker diagnoses divisor cancellation and normalization; it does
not prove the analytic transformations or an unbounded theorem.

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
folders. Record notable milestones in a concise `DRAFT_HISTORY.md`, linking
the relevant commit or tag, notes, and reviews.

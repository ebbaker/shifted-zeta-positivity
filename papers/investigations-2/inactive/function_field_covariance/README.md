# Function-field covariance experiment

[Investigation index](../../README.md)

12 October 2026. Prepared for Edward Baker. Model: GPT-6 Astra
(`gpt-6-astra`). Reasoning effort: ultra. Prepared with substantial LLM
assistance. Internal model reviews are not independent mathematical
validation or formal verification.

## Objective and current status

Build one faithful function-field analogue of an actual arithmetic moment
ledger, then test whether it exhibits a cancellation mechanism beyond its
diagonal and coherent contributions. The purpose is to understand the
reduction structure in a setting with exact finite calculations and known
geometric input. Known function-field RH does not itself provide a route to
integer RH.

**Status: scoped; research not started in this project.** This project
depends on a specified family from
[arithmetic covariance targets](../arithmetic_covariance_targets/README.md).
Do not begin with an arbitrary polynomial family and retrospectively label
it an analogue. General equidistribution and variance statements do not
automatically cover sparse sextic rows or uniformity in growing degrees.

## First bounded task

1. Choose one integer-family ledger and state the translation explicitly:
   finite field, polynomial ring, base character, modulus degree, row degree,
   coefficient profile, zero extensions, and limiting regime. Specify any
   characteristic or residue-field conditions required by the character
   orders.
2. Use a fixed nonprincipal base twist or another nontrivial base
   L-function. The untwisted polynomial Möbius sum over monic polynomials of
   degree at least two vanishes, so that principal-row experiment would
   conceal the intended signal.
3. For small instances, calculate the row weights, character kernel,
   diagonal, coherent mass, and signed covariance exactly. Preserve the
   same masks and the same distinction between whole and centered moments
   as in the integer ledger. Include an orthogonality sanity check before
   interpreting any apparent saving.
4. Identify one primary theorem that estimates these same objects in the
   declared limit. Record precisely what it gives, which constants are
   uniform, and whether its main term already exhausts the proposed budget.

If the experiment concerns an edge-mode recurrence, use the actual
Frobenius eigenvalues and exact degree shifts. Normalized degree sequences
can be quasiperiodic; vertical periodicity of an L-function in its complex
argument does not supply a common period for those sequences.

## Deliverables and decision tests

Deliver a matched-family specification, a reproducible exact computation
with small records, and a comparison between the observed covariance and
the available theorem. Separate finite identities, numerical evidence,
proved asymptotics, and conjectural integer analogies. Explicitly state
which parts of the original extraction argument survive translation.

Continue if the matched model reveals a mechanism beyond known diagonal
and coherent terms and there is a credible arithmetic counterpart. A
negative result is also useful if it locates a specific mismatch in the
proposed transfer. Stop the analogy if the controlling theorem addresses a
different family or limit, the target lies below the exact diagonal, or the
only signal vanishes for a reason absent from the integer problem. A
counterexample transfers back only when the hypotheses and argument also
transfer. Failure of an arbitrary analogue is not an impossibility theorem
over the integers.

## Starting references

- [Corrected function-field proposal](../../../quasi-rh-exponent-descent/brainstorm/NEW_PATHS_FORWARD_BRAINSTORM_CODEX_20261011.md#4-d3-use-function-fields-to-test-exact-structure)
- [Original proposal and motivation](../../../quasi-rh-exponent-descent/brainstorm/NEW_PATHS_FORWARD_BRAINSTORM_CLAUDE_20261011.md#d3-a-function-field-testbed-for-the-descent-structure)
- [Sextic extraction and prime-mask identity](../../../quasi-rh-exponent-descent/short_families/notes/1_SHORT_FAMILY_DESCENT_REFINEMENT_20261008.md)
- [Quadratic kernel and covariance](../../../quasi-rh-exponent-descent/integer_quadratic_lift/notes/2_QUADRATIC_MOMENT_STRENGTH_AND_BARRIER_20261008.md)

## Working records

Use `notes/` for definitions and proofs, `numerics/` for reproducible finite
experiments and small records, `reviews/` for scoped assessments, and
`chat-histories/` for selected discussion records. Follow the repository
[large-file policy](../../../../LARGE_FILES.md). Keep manuscripts at stable
paths, with author and LLM acknowledgement, and create no snapshot folders.
Use a concise `DRAFT_HISTORY.md` for notable milestones, linking commits or
tags and the relevant notes and reviews.

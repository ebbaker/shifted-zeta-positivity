# Research overview: Schur specialization and Toda structure

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual preparation model **gpt-6-astra (Codex)**, reasoning effort **xhigh**. Preparation task **J-E10**, documentation only; no branch research executed.

**First assessment: MC05-B01 — B, recommended Astra at the author’s selected higher effort (ultra if chosen and available).** This is a recommendation, not the actual preparation setting or an automatic model change. Current readiness and later findings belong only in the [local progress register](../research-progress/01_SCHUR_TODA_STRUCTURE_RESEARCH_PROGRESS_20261101.md). The [parallel continuation](../../notes/05_CONTINUATION_PARALLEL_PHYSICAL_DIRECTIONS_20261101.md) fixes the common baseline, controls, ownership and return format.

**Research question:** What additional constraint on the actual theta specialization, beyond generic Plücker identities, could provide a useful neighboring-index comparison?

## Background: why these are Schur values

Let \(H_n=c_n/c_0\), with \(H_0=1\) and \(H_n=0\) for negative \(n\).
Define the formal times by
\[
\sum_{n\ge0}H_n z^n=\exp\!\left(\sum_{m\ge1}t_mz^m\right).
\]
This is a formal logarithm at the origin, not a global zero-free logarithm.
Jacobi–Trudi, with a transpose of the displayed coefficient matrix if
needed, gives
\[
D_{r,k}=c_0^r s_{(k^r)}(\mathbf t).
\]
These rectangular Schur values belong to the algebra that also appears in
fermionic current matrix elements. The theta specialization need not
behave like evaluation on positive variables or a representation
dimension. Its required positivity is precisely part of the problem.

Desnanot–Jacobi supplies the exact bilinear relation
\[
D_{r+1,k}D_{r-1,k}=D_{r,k}^2-D_{r,k-1}D_{r,k+1}.
\]
This is a Toda-type determinant relation. It does not, by itself, provide
an additional deformation variable, a physical evolution, a finite
isomonodromic system, or initial data known to remain in a positive cone.
[Note04, Section 5](../../notes/04_FERMIONIC_CORRELATORS_AND_PHYSICAL_INTERPRETATIONS_20261101.md) states the established algebra and its scope.

## Bounded research approach

Compare at most two explicit constraints suggested by the complete theta
source: a relation among its coefficient times, or a source-compatible
deformation with an independently specified initial/boundary condition.
Select one and show what is added beyond the generic determinant identity.
If invoking a hierarchy or tau-function theorem, specify the actual family
of functions, times, specialization and hypotheses; a label is not an
existence or positivity proof.

Trace the proposed constraint to the finite-order quantity
\(D_{3,k-1}D_{3,k+1}/D_{3,k}^2\), or to the complete Mellin comparison
after supplying a valid bridge. The continuous Mellin parameter does not
automatically equal a hierarchy time. Keep factorial normalization in any
translation from \(M_3(k)\) back to coefficient minors.

Determine whether a positivity-preserving evolution actually has useful
independent starting data. An assertion that the theta specialization is
Schur-positive, or that all its required minors start positive, can simply
restate the full target. Classify that quantifier-level issue before using
it, following [the reformulation rule](../../../../../../../avoid/01_restating_the_target.md).

## What counts as progress

Return one additional constraint with a worked inequality, or a precise
closure/initial-data obstruction in the proposed construction. If an exact
constraint is derived but no estimate follows, display the remaining
signed quantity and retain that distinction in the progress register.
Reproducing Jacobi–Trudi, Wick or Desnanot–Jacobi alone is background.

Do not convert failure of one finite closure into failure of all integrable
approaches. A finite coefficient check neither verifies an infinite
hierarchy nor proves all-order positivity. Additional finite algebra can
be requested as E work only when its formula and acceptance criterion are
fixed.

## Controls and reading

Formal Schur specialization and Plücker identities hold for generic
coefficient sequences and exclude none of the relevant smooth even
[controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md) by themselves. For a proposed new relation identify
which control fails which premise; absence of theta’s unchanged spectrum
does not automatically establish failure of an untested inequality.

Read [Note04](../../notes/04_FERMIONIC_CORRELATORS_AND_PHYSICAL_INTERPRETATIONS_20261101.md), [the exact factorial budget](../../notes/01_INITIAL_BRANCH_EVALUATION_20261101.md),
[the theta-identity lessons](../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md) and the
[checked Alexandrov–Zabrodin passages](../../../../references/06_PHYSICAL_INTERPRETATION_SOURCES_20261101.md). The original
specialization conventions are fixed here; convergence and analytic
continuation require separate arguments whenever formal algebra is used
to make an analytic claim.

## Ownership, return and evidence standards

Own coefficient/Schur and bilinear deformation algebra. Leave carrier integration identities to MC04-B01 and physical orbital relations to MC02-B01.

Save the bounded return under `notes/01_THETA_SCHUR_CONSTRAINT_RETURN_YYYYMMDD.md`, using the actual local date and next unused number. Include one selected mechanism, exact inputs, a worked result or precise missing obligation, the covered domain, controls and one next B/E recommendation. Save small computations in `numerics/` and a separate assessment in `reviews/`. A finite execution campaign remains gated until its own contract is fixed. See the [local register](../research-progress/01_SCHUR_TODA_STRUCTURE_RESEARCH_PROGRESS_20261101.md) for acceptance and stopping conditions.

Use the [result index](../../../../../../../result-summaries/README.md) and [avoid index](../../../../../../../avoid/README.md), especially [controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md), [re-realizations](../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [joint signed estimates](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) and [scoped exclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md). Existing internally reviewed results retain their review qualifications; preliminary deductions stay preliminary. Consult the [common references](../../../../references/README.md) and [import checks](../../../../../../../avoid/16_unchecked_imports_and_novelty_claims.md) before using a new theorem. A finished assessment is distinct from a proved parent inequality.

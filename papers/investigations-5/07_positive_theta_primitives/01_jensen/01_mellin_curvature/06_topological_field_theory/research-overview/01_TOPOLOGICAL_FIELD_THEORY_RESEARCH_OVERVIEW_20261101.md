# Research overview: Topological field theory and protected observables

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual preparation model **gpt-6-astra (Codex)**, reasoning effort **xhigh**. Preparation task **J-E10**, documentation only; no branch research executed.

**First assessment: MC06-B01 — B, recommended Astra at the author’s selected higher effort (ultra if chosen and available).** This is a recommendation, not the actual preparation setting or an automatic model change. Current readiness and later findings belong only in the [local progress register](../research-progress/01_TOPOLOGICAL_FIELD_THEORY_RESEARCH_PROGRESS_20261101.md). The [parallel continuation](../../notes/05_CONTINUATION_PARALLEL_PHYSICAL_DIRECTIONS_20261101.md) fixes the common baseline, controls, ownership and return format.

**Research question:** Is there a concrete cohomological or geometric construction whose identified observable is the unchanged theta determinant and whose extra structure yields a useful constraint?

## Background: what the Witten comparison would require

Witten’s 1988 topological gauge theory relates correlation functions in a
twisted four-dimensional theory to Donaldson invariants. The relevant
structure includes a cohomological symmetry \(Q\), \(Q\)-closed
observables and a stress tensor expressed as a \(Q\)-commutator. Metric
independence then depends on the measure, anomalies and boundary behavior,
not just a formal symmetry of the classical expressions. The invariants
concern smooth four-manifold structure and need not be nonnegative.
The inspected passages and qualifications are recorded in the
[physical-source bibliography](../../../../references/06_PHYSICAL_INTERPRETATION_SOURCES_20261101.md).

In the present problem
\[
D_{r,k}=\det[c_{k+j-i}],\qquad
c_n=\frac1{(2n)!}\int_0^\infty u^{2n}\Phi(u)\,du.
\]
No underlying four-manifold, moduli space, cohomology classes, localization
formula or protected-observable identity giving these numbers has been
identified. The exact circle trace is temperature-dependent; the exact
fermion correlator has two different sets of smeared orbitals. Neither
fact establishes topological invariance. This is an exploratory feasibility
branch, with less direct contact with the current estimate than the
Mellin and ensemble branches.

## Bounded research approach

Compare at most two specific candidates, then work one. A candidate may
be a cohomological quantum-mechanical model or a four-dimensional
gauge/moduli construction; its dimension and purpose must be explicit.
Do not call a lower-dimensional index a Donaldson invariant. A determinant
line or localization analogy must come with the actual data it needs.

Prepare a dictionary with these entries: manifold or configuration space;
fields and measure; symmetry and its square; action or differential;
observables and their degrees; the role of theta’s complete square
spectrum; and the formula claimed to equal \(D_{r,k}\) or \(M_3(s)\).
Check at least the \(r=1\) normalization and the \(r=2\) determinant
convention before extrapolating. Those checks are consistency tests,
not evidence for a new sign theorem.

Then isolate what the protection would actually imply. If metric or
parameter independence is claimed, identify the variation, the exact
symmetry argument and any noncompact/boundary contribution. If localization
produces signed contributions, preserve those signs. If the construction
only realizes an arbitrary input matrix as a correlator, it has supplied
no extra theta information.

## Acceptance and early stopping

A positive feasibility return requires an exact matched observable and a
new independently justified relation relevant to the coefficient sign or
Mellin response. A concrete partial construction is useful if its missing
step is precisely named. A negative return can complete this bounded task
by showing that the chosen candidate fails its observable match,
protection or proposed sign transfer. It cannot exclude all possible
topological theories.

Stop if the dictionary cannot identify a genuine geometric observable, if
the alleged invariant still has uncontrolled dependence on the parameters
it should protect, or if positivity is assumed as part of the matching.
Record the earliest failed requirement rather than filling gaps with
terminology. Topological invariance alone would not imply positivity or
the Gaussian response budget.

## Controls and reading

Use [the earlier physical-channel lessons](../../../../../../../result-summaries/06_physical_channels_wzw_ym_and_collar.md) and
[the re-realization warning](../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md) before broadening the construction.
Generic geometric or Fock encodings often also encode the
[collision controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md). Specify the additional hypothesis that
would distinguish this theta application; do not claim a control screen
has passed before that hypothesis exists.

Start with [Note04, Section 6](../../notes/04_FERMIONIC_CORRELATORS_AND_PHYSICAL_INTERPRETATIONS_20261101.md) and the checked Witten passages in
[the shared source note](../../../../references/06_PHYSICAL_INTERPRETATION_SOURCES_20261101.md). Any new imported localization or
positivity theorem needs its primary statement, hypotheses and applicable
domain inspected. This packet proposes no existing Donaldson-invariant
identification and no universal obstruction to one.

## Ownership, return and evidence standards

Own geometric/protected-observable feasibility. Treat the ordinary circle trace, generic fermionic realization and Schur algebra as inputs, not as evidence of topological invariance.

Save the bounded return under `notes/01_PROTECTED_OBSERVABLE_FEASIBILITY_RETURN_YYYYMMDD.md`, using the actual local date and next unused number. Include one selected mechanism, exact inputs, a worked result or precise missing obligation, the covered domain, controls and one next B/E recommendation. Save small computations in `numerics/` and a separate assessment in `reviews/`. A finite execution campaign remains gated until its own contract is fixed. See the [local register](../research-progress/01_TOPOLOGICAL_FIELD_THEORY_RESEARCH_PROGRESS_20261101.md) for acceptance and stopping conditions.

Use the [result index](../../../../../../../result-summaries/README.md) and [avoid index](../../../../../../../avoid/README.md), especially [controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md), [re-realizations](../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [joint signed estimates](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) and [scoped exclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md). Existing internally reviewed results retain their review qualifications; preliminary deductions stay preliminary. Consult the [common references](../../../../references/README.md) and [import checks](../../../../../../../avoid/16_unchecked_imports_and_novelty_claims.md) before using a new theorem. A finished assessment is distinct from a proved parent inequality.

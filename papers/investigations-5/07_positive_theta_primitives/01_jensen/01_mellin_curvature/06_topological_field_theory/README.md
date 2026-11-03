# 06 Topological field theory and protected observables

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, effort **xhigh**. Setup task **J-E09**, documentation only.

This is an exploratory direction motivated by Witten's realization of Donaldson invariants through correlation functions. The question is whether an additional geometric or cohomological structure can be constructed for the unchanged theta determinants. No identification with Donaldson invariants has been proposed as an established correspondence.

## Current research packet

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual preparation model **gpt-6-astra (Codex)**, reasoning effort **xhigh**. Preparation task **J-E10**, documentation only; no branch research executed.

Read [the research overview](research-overview/01_TOPOLOGICAL_FIELD_THEORY_RESEARCH_OVERVIEW_20261101.md) for the expanded background and first bounded question. [The local progress file](research-progress/01_TOPOLOGICAL_FIELD_THEORY_RESEARCH_PROGRESS_20261101.md) is now the sole live register for `MC06-B01` and later `MC06-` tasks. [Continuation05](../notes/05_CONTINUATION_PARALLEL_PHYSICAL_DIRECTIONS_20261101.md) coordinates the requested higher-compute parallel investigation, including separate review and synthesis. The older setup status below is historical; the [Jensen register](../../research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md) continues to own aggregate J-B10 and the prior J tasks.

The usual `research-overview/`, `research-progress/`, `notes/`, `numerics/`, `reviews/`, `references/` and `chat-histories/` folders are in place. The continuation prepares research; no worker has been dispatched by this documentation task.

## Background

In Witten's 1988 twisted supersymmetric gauge theory, suitable observables are closed under a cohomological symmetry \(Q\), and the stress tensor is a \(Q\)-commutator:
\[
Q\mathcal O=0,\qquad T_{\mu\nu}=\{Q,G_{\mu\nu}\}.
\]
Under the required measure, boundary and analytical conditions, metric variations of protected correlations decouple. This relates observables to smooth invariants of the underlying manifold and to differential forms on instanton moduli space. The inspected passages and their qualifications are recorded in the [Witten source entry](../../../references/06_PHYSICAL_INTERPRETATION_SOURCES_20261101.md#witten1988tqft).

Our established objects are the theta-dependent coefficient determinants \(D_{r,k}\), their [fermionic overlap](../02_fermionic_correlators/README.md), the [positive carrier and signed insertion](../04_biorthogonal_ensembles/README.md), and their [Schur specialization](../05_schur_toda_structure/README.md). Those descriptions do not yet specify a topological field theory. The [circle thermal trace](../01_circle_thermal_trace/README.md) depends on its geometric and thermal data; it is not already a protected index.

## Summary of the approach

A concrete proposal would need to identify:

1. A manifold, field configuration space or moduli problem, with its boundary and regularity assumptions.
2. A cohomological symmetry and observables, with a justified integration measure.
3. An exact evaluation or transfer map reproducing the existing \(D_{r,k}\) or a specified consumer of the complete signed Mellin response, with all normalization and endpoint terms retained.
4. A protected identity, localization formula or other theorem that supplies new information about that consumer.

These are missing construction steps, not assumptions already licensed by the determinant notation. A topological invariant can be signed, so topological invariance alone would not establish the required inequality. A deformation to a tractable model would need a proved preservation or comparison theorem for the actual observable.

## Relationship to the other directions

The fermionic and Schur descriptions give concrete algebraic objects on which a proposed symmetry could act. The [connected-response direction](../03_connected_mellin_response/README.md) fixes the quantitative question a successful construction should address. The possible topological structure is distinct from these existing representations and remains more speculative.

## Initial J-E09 status (historical; current register above)

No suitable manifold/moduli correspondence, \(Q\)-symmetry, protected theta observable or localization theorem has been identified. This is neither a completed physical theory nor an exclusion of all such theories. The source discussion in [Note04, Section 6](../notes/04_FERMIONIC_CORRELATORS_AND_PHYSICAL_INTERPRETATIONS_20261101.md) supplies motivation and the precise gap.

**Potential follow-up: B — Astra:** assess one concrete geometric/cohomological candidate and state whether it reproduces an unchanged theta observable with a usable new identity. Stop at a precise missing construction if only generic fermionic or determinant algebra is obtained. No new field-theory project, independent task or numerical campaign is activated by this README.

See the [parent direction map](../README.md#physical-research-directions), [prior physical-channel lessons](../../../../../../result-summaries/06_physical_channels_wzw_ym_and_collar.md), and [re-realization cautions](../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md). The [sole Jensen register](../../research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md) owns live status. Future work belongs in local `notes/`, `numerics/` and `reviews/` when needed; the existing chat remains in the [parent archive](../chat-histories/README.md).

## Completed bounded assessment — 1 November 2026

Prepared for Edward Baker with substantial LLM assistance; actual gpt-6-astra / ultra.

[MC06-B01 Return01](notes/01_PROTECTED_OBSERVABLE_FEASIBILITY_RETURN_20261101.md) constructs theta as an unprotected degree-fugacity response of circle supersymmetric quantum mechanics and proves the selected protected replacement cannot match. No Mellin estimate; separate checking pending. The [sole register](research-progress/01_TOPOLOGICAL_FIELD_THEORY_RESEARCH_PROGRESS_20261101.md) owns status.

**Checked assessment, 1 November 2026:** [separate review](reviews/01_MC06_E01_SEPARATE_REVIEW_20261101.md) accepted with the review’s closed-domain and trace-admissibility clarification; the [local register](research-progress/01_TOPOLOGICAL_FIELD_THEORY_RESEARCH_PROGRESS_20261101.md) owns current status. Six-direction [synthesis](../notes/06_PARALLEL_PHYSICAL_DIRECTIONS_SYNTHESIS_20261101.md). No Gaussian Mellin bound is acquired.

**Four-dimensional continuation, 1 November 2026:** the distinct [07 Donaldson Witten folder](../07_donaldson_witten_theory/README.md) now contains the author-requested four-dimensional assessment. This folder’s MC06 evidence remains the circle supersymmetric model; its scoped failure is not a Donaldson-theory exclusion. Coordinator gpt-6-astra / ultra, for Edward Baker with substantial LLM assistance.

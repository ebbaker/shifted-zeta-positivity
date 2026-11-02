# 05 Schur functions, fermionic currents and Toda structure

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, effort **xhigh**. Setup task **J-E09**, documentation only.

This direction studies the exact representation-theoretic and bilinear algebra of the coefficient determinants. It asks whether theta selects additional constraints within the integrable framework that can yield a useful estimate.

## Current research packet

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual preparation model **gpt-6-astra (Codex)**, reasoning effort **xhigh**. Preparation task **J-E10**, documentation only; no branch research executed.

Read [the research overview](research-overview/01_SCHUR_TODA_STRUCTURE_RESEARCH_OVERVIEW_20261101.md) for the expanded background and first bounded question. [The local progress file](research-progress/01_SCHUR_TODA_STRUCTURE_RESEARCH_PROGRESS_20261101.md) is now the sole live register for `MC05-B01` and later `MC05-` tasks. [Continuation05](../notes/05_CONTINUATION_PARALLEL_PHYSICAL_DIRECTIONS_20261101.md) coordinates the requested higher-compute parallel investigation, including separate review and synthesis. The older setup status below is historical; the [Jensen register](../../research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md) continues to own aggregate J-B10 and the prior J tasks.

The usual `research-overview/`, `research-progress/`, `notes/`, `numerics/`, `reviews/`, `references/` and `chat-histories/` folders are in place. The continuation prepares research; no worker has been dispatched by this documentation task.

## Background

Let \(F(z)=\sum_{n\ge0}c_nz^n\), and define formal times \(t_m\) near the constant term by
\[
\frac{F(z)}{c_0}=\sum_{n\ge0}H_nz^n
=\exp\left(\sum_{m\ge1}t_mz^m\right),\qquad H_n=c_n/c_0.
\]
The formal logarithm exists because \(H_0=1\); no globally zero-free logarithm is assumed. With this complete-symmetric-function specialization, Jacobi–Trudi gives
\[
D_{r,k}=c_0^r s_{(k^r)}(\mathbf t),
\]
where \((k^r)\) is the rectangular Young diagram with \(r\) rows of length \(k\). Negative coefficient indices use the same zero convention as the determinant problem.

The adjacent-determinant identity is
\[
D_{r+1,k}D_{r-1,k}=D_{r,k}^2-D_{r,k-1}D_{r,k+1}.
\]
This is a bilinear determinant/Plücker relation of the type underlying discrete Toda equations. Schur functions also occur in free-fermion current matrix elements and tau-function constructions. The exact specialization and its scope are derived in [Note04, Section 5](../notes/04_FERMIONIC_CORRELATORS_AND_PHYSICAL_INTERPRETATIONS_20261101.md).

## Summary of the approach

Use the Schur/current description to organize relations across \(r\) and \(k\), then ask whether complete theta identities constrain the specialization beyond generic determinant algebra. A useful new relation must produce a quantitative bound for the fixed determinants or the [connected Mellin response](../03_connected_mellin_response/README.md).

Simply renaming the known adjacent-minor identity as a Toda relation gives no new sign. The formal theta specialization is not established here to be Schur-positive. Positivity of representation dimensions at other specializations does not determine these values. Additional hierarchy variables, a compatible evolution or a finite isomonodromic system must be constructed before their theorems are used; they do not follow from one determinant identity.

## Relationship to the other directions

[02 Fermionic correlators](../02_fermionic_correlators/README.md) provides the elementary Fock-space realization. [04 Biorthogonal ensembles](../04_biorthogonal_ensembles/README.md) provides a positive measure with a signed insertion. This folder addresses algebraic constraints rather than concentration or integration bounds. [06 Topological field theory](../06_topological_field_theory/README.md) may draw on related representation theory, but no topological invariant is identified by the Schur formula alone.

## Initial J-E09 status (historical; current register above)

The rectangular Schur specialization is exact and preliminarily checked in the source note. The bilinear relation was already part of the parent program. No new integrable flow, theta constraint, positivity result or uniform-in-order estimate is established. **Potential follow-up: B — Astra:** identify one additional source-selected current or deformation identity and test whether it adds information beyond Jacobi–Trudi and Plücker relations. No separate task or numerical request is issued here.

The [primary-source record](../../../references/06_PHYSICAL_INTERPRETATION_SOURCES_20261101.md) preserves the inspected Alexandrov–Zabrodin passages and limits. See the [parent direction map](../README.md#physical-research-directions) and [sole Jensen register](../../research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md). Future work belongs in local `notes/`, `numerics/` and `reviews/` when needed; existing [chat history](../chat-histories/README.md) is preserved.

## MC05-B01 bounded return, 1 November 2026

Prepared for Edward Baker with substantial LLM assistance, gpt-6-astra / ultra. [Return01](notes/01_THETA_SCHUR_CONSTRAINT_RETURN_20261101.md) derives the source heat/Schur-time evolution, a finite-prefix nonclosure obstruction and a normalizable oscillator formulation of RH. No Mellin estimate is obtained. Separate checking is pending; the [sole local register](research-progress/01_SCHUR_TODA_STRUCTURE_RESEARCH_PROGRESS_20261101.md) owns current task status.

**Checked assessment, 1 November 2026:** [separate review](reviews/01_MC05_E01_SEPARATE_REVIEW_20261101.md) accepted at its stated scope; the [local register](research-progress/01_SCHUR_TODA_STRUCTURE_RESEARCH_PROGRESS_20261101.md) owns current status. Six-direction [synthesis](../notes/06_PARALLEL_PHYSICAL_DIRECTIONS_SYNTHESIS_20261101.md). No Gaussian Mellin bound is acquired.

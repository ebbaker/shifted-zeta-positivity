# 04 Biorthogonal ensembles and statistical mechanics

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, effort **xhigh**. Setup task **J-E09**, documentation only.

This direction treats the positive carrier as an equilibrium particle ensemble and the determinant's sign-bearing factor as an inserted observable. It is an analytical probability/statistical-mechanics viewpoint, distinct from the coefficient-algebra viewpoint in [05](../05_schur_toda_structure/README.md).

## Current research packet

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual preparation model **gpt-6-astra (Codex)**, reasoning effort **xhigh**. Preparation task **J-E10**, documentation only; no branch research executed.

Read [the research overview](research-overview/01_BIORTHOGONAL_ENSEMBLES_RESEARCH_OVERVIEW_20261101.md) for the expanded background and first bounded question. [The local progress file](research-progress/01_BIORTHOGONAL_ENSEMBLES_RESEARCH_PROGRESS_20261101.md) is now the sole live register for `MC04-B01` and later `MC04-` tasks. [Continuation05](../notes/05_CONTINUATION_PARALLEL_PHYSICAL_DIRECTIONS_20261101.md) coordinates the requested higher-compute parallel investigation, including separate review and synthesis. The older setup status below is historical; the [Jensen register](../../research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md) continues to own aggregate J-B10 and the prior J tasks.

The usual `research-overview/`, `research-progress/`, `notes/`, `numerics/`, `reviews/`, `references/` and `chat-histories/` folders are in place. The continuation prepares research; no worker has been dispatched by this documentation task.

## Background

The accepted source inequality \(R'(u)>0\), with \(R=\Phi''/\Phi\), makes
\[
w_{r,s}(\mathbf u)=\prod_j u_j^{2s}\Phi(u_j)
V(\mathbf u^2)V(R(\mathbf u))
\]
positive on the ordered chamber. Put \(Z_{r,s}=\int_{u_1<\cdots<u_r}w_{r,s}\). Its symmetric extension, divided by \(r!Z_{r,s}\), is a probability density on the full positive orthant.

Writing \(\omega_s(u)=u^{2s}\Phi(u)\), this density is proportional to
\[
\det[u_j^{2i}\sqrt{\omega_s(u_j)}]_{i,j=0}^{r-1}
\det[R(u_j)^i\sqrt{\omega_s(u_j)}]_{i,j=0}^{r-1},
\]
with the node labels shifted to \(0,\ldots,r-1\) in this display. Such a product defines a biorthogonal ensemble. Its finite-particle correlation functions are determinants of a kernel obtained from the invertible pairing matrix. Integrability and invertibility are paid by the positive complete-source integral, as explained in [Note04, Section 4](../notes/04_FERMIONIC_CORRELATORS_AND_PHYSICAL_INTERPRETATIONS_20261101.md).

The coefficient determinant is represented by a signed insertion:
\[
M_r(s)=Z_{r,s}\,E_{r,s}h_r,\qquad
h_r=\frac{\det[\Phi^{(2i)}(u_j)/\Phi(u_j)]}{V(R(\mathbf u))}.
\]
Coincident-node quotients have removable limits. Positivity of the particle density proves \(Z>0\), while the sign of \(E h_r\) is an additional question. Particle \(m\)-point densities and the original \(D_{r,k}\) are different observables.

## Summary of the approach

Derive a Ward/loop identity by integrating a complete source-dependent variation against this ensemble, retaining the \(h_r\) insertion and its derivatives. Test whether the identity estimates the full connected response in [03](../03_connected_mellin_response/README.md). A useful result must retain mixed terms, origin and infinity contributions, and any terms arising at node faces; formal integration by parts alone does not sign the result.

The Gaussian comparison has \(h_r=1\), providing a simple normalization case. Generic concentration of the carrier, or the existence of a determinantal correlation kernel, does not establish the theta Gaussian bound. A biorthogonal kernel need not be a Hermitian orthogonal-projection kernel, so physical free-fermion-state conclusions need their own hypotheses.

## Relationship to the other directions

[02 Fermionic correlators](../02_fermionic_correlators/README.md) represents the target as a Slater-state overlap; this folder isolates a positive probability measure and a signed observable. [05 Schur and Toda structure](../05_schur_toda_structure/README.md) studies the coefficient identities that may organize these calculations. The positive carrier is related to both, but the required estimates differ.

## Initial J-E09 status (historical; current register above)

The ensemble representation and its finite correlation construction are available with the qualifications in the [inspected source records](../../../references/06_PHYSICAL_INTERPRETATION_SOURCES_20261101.md). No theta-specific loop equation closing the curvature estimate has been proved. **Potential follow-up: B — Astra:** select one source variation, derive its complete identity, and identify a genuine quantitative consequence or its exact missing term. No computational campaign is issued.

Use the [parent direction map](../README.md#physical-research-directions) and [sole Jensen register](../../research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md). Future local `notes/`, `numerics/` and `reviews/` hold direction-specific work when needed; the current chat remains in the [parent archive](../chat-histories/README.md).

## Completed bounded assessment — 1 November 2026

Prepared for Edward Baker with substantial LLM assistance; actual gpt-6-astra / ultra.

[MC04-B01 Return01](notes/01_INSERTED_ENSEMBLE_IDENTITY_RETURN_20261101.md) derives the complete logarithmic-dilation Ward identity and proves a scoped pointwise polynomial-nonclosure result. No curvature allowance is paid; separate checking is pending. See the [sole register](research-progress/01_BIORTHOGONAL_ENSEMBLES_RESEARCH_PROGRESS_20261101.md).

**Checked assessment, 1 November 2026:** [separate review](reviews/01_MC04_E01_SEPARATE_REVIEW_20261101.md) accepted at its stated scope; the [local register](research-progress/01_BIORTHOGONAL_ENSEMBLES_RESEARCH_PROGRESS_20261101.md) owns current status. Six-direction [synthesis](../notes/06_PARALLEL_PHYSICAL_DIRECTIONS_SYNTHESIS_20261101.md). No Gaussian Mellin bound is acquired.

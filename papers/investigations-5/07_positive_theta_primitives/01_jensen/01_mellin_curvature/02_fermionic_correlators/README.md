# 02 Fermionic correlators and many-body geometry

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, effort **xhigh**. Setup task **J-E09**, documentation only.

This direction treats the coefficient determinants as exact fermionic correlation functions and overlaps of antisymmetric many-body states. The fermionic and exterior-algebra descriptions are two forms of the same construction, so they share this folder.

## Current research packet

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual preparation model **gpt-6-astra (Codex)**, reasoning effort **xhigh**. Preparation task **J-E10**, documentation only; no branch research executed.

Read [the research overview](research-overview/01_FERMIONIC_CORRELATORS_RESEARCH_OVERVIEW_20261101.md) for the expanded background and first bounded question. [The local progress file](research-progress/01_FERMIONIC_CORRELATORS_RESEARCH_PROGRESS_20261101.md) is now the sole live register for `MC02-B01` and later `MC02-` tasks. [Continuation05](../notes/05_CONTINUATION_PARALLEL_PHYSICAL_DIRECTIONS_20261101.md) coordinates the requested higher-compute parallel investigation, including separate review and synthesis. The older setup status below is historical; the [Jensen register](../../research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md) continues to own aggregate J-B10 and the prior J tasks.

The usual `research-overview/`, `research-progress/`, `notes/`, `numerics/`, `reviews/`, `references/` and `chat-histories/` folders are in place. The continuation prepares research; no worker has been dispatched by this documentation task.

## Background

Keep the ordinary coefficients and negative-index convention
\[
c_n=\frac1{(2n)!}\int_0^\infty u^{2n}\Phi(u)\,du,
\quad D_{r,k}=\det[c_{k+j-i}]_{i,j=0}^{r-1},\quad c_n=0\ (n<0).
\]
In \(L^2((0,\infty),du)\), define
\[
f_i(u)=\frac{\Phi^{(2i)}(u)}{\sqrt{\Phi(u)}},\qquad
g_{k,j}(u)=\frac{u^{2(k+j)}\sqrt{\Phi(u)}}{(2(k+j))!}.
\]
The complete source and its endpoint cancellations give
\(\langle f_i,g_{k,j}\rangle=c_{k+j-i}\). Canonical fermionic creation and annihilation operators therefore satisfy
\[
D_{r,k}=\langle0|a(f_{r-1})\cdots a(f_0)
a^\dagger(g_{k,0})\cdots a^\dagger(g_{k,r-1})|0\rangle.
\]
Equivalently,
\[
D_{r,k}=\langle f_0\wedge\cdots\wedge f_{r-1},
g_{k,0}\wedge\cdots\wedge g_{k,r-1}\rangle.
\]
This is an \(r\)-particle overlap, or a smeared \(2r\)-field equal-time correlator. The fixed finite-order orbitals are square integrable. The annihilator ordering fixes the determinant sign.

## Summary of the approach

Investigate whether exact theta differential relations impose a useful relation between the derivative orbitals and polynomial orbitals. An operator comparison, identity for inserted observables, or controlled deformation would be useful only if it estimates the unchanged overlap or its Mellin response.

The bra and ket differ. Positive Hilbert-space norms do not fix their overlap's sign; Cauchy–Schwarz supplies an absolute upper bound. Replacing the overlap by its squared modulus changes the target. Wick's theorem explains the determinant but supplies no theta-specific positivity. A reflection-positivity argument would need an actual compatible reflection/adjoint pairing for these states.

## Relationship to the other directions

- [01 Circle thermal trace](../01_circle_thermal_trace/README.md) explains where the source comes from; this direction explains how it enters a many-body observable.
- [03 Connected Mellin response](../03_connected_mellin_response/README.md) inserts a logarithmic size operator between these states and differentiates the resulting amplitude.
- [05 Schur and Toda structure](../05_schur_toda_structure/README.md) describes the associated coefficient algebra and free-fermion current formalism.

## Initial J-E09 status (historical; current register above)

The correlator and exterior-product identities were derived in [Note04, Sections 2–3](../notes/04_FERMIONIC_CORRELATORS_AND_PHYSICAL_INTERPRETATIONS_20261101.md), with same-assistant analytical checking only. No theta-selected local interacting field theory, positive overlap theorem or curvature estimate has been obtained. **Potential follow-up: B — Astra:** select one additional relation between the two state families and assess its quantitative consequence; a generic Fock-space realization alone is not the deliverable.

The [primary-source record](../../../references/06_PHYSICAL_INTERPRETATION_SOURCES_20261101.md) identifies the inspected Wick and fermionic passages. Use the [parent direction map](../README.md#physical-research-directions) and [sole Jensen register](../../research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md). No separate task is issued here. Future work belongs in local `notes/`, `numerics/` and `reviews/` as needed; the existing chat stays in the [parent archive](../chat-histories/README.md).

## Bounded assessment return — 1 November 2026

[MC02-B01 Return01](notes/01_THETA_ORBITAL_COMPARISON_RETURN_20261101.md) gives an exact bounded lattice-fermion transfer formulation with all-minor RH quantifiers and an actual two-site obstruction to a self-adjoint transfer interpretation. It proves no new Mellin estimate. **gpt-6-astra / ultra**; separate review pending in the sole local register.

**Checked assessment, 1 November 2026:** [separate review](reviews/01_MC02_E01_SEPARATE_REVIEW_20261101.md) accepted at its stated scope; the [local register](research-progress/01_FERMIONIC_CORRELATORS_RESEARCH_PROGRESS_20261101.md) owns current status. Six-direction [synthesis](../notes/06_PARALLEL_PHYSICAL_DIRECTIONS_SYNTHESIS_20261101.md). No Gaussian Mellin bound is acquired.

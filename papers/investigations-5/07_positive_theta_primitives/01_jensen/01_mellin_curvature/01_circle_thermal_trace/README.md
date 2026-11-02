# 01 Quantum particle on a circle and the theta thermal trace

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, effort **xhigh**. Setup task **J-E09**, documentation only.

This direction studies the physical origin of the complete theta source: the thermal spectrum of a quantum particle on a circle. It asks whether that spectrum and its exact identities provide useful information for the coefficient-determinant problem.

## Current research packet

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual preparation model **gpt-6-astra (Codex)**, reasoning effort **xhigh**. Preparation task **J-E10**, documentation only; no branch research executed.

Read [the research overview](research-overview/01_CIRCLE_THERMAL_TRACE_RESEARCH_OVERVIEW_20261101.md) for the expanded background and first bounded question. [The local progress file](research-progress/01_CIRCLE_THERMAL_TRACE_RESEARCH_PROGRESS_20261101.md) is now the sole live register for `MC01-B01` and later `MC01-` tasks. [Continuation05](../notes/05_CONTINUATION_PARALLEL_PHYSICAL_DIRECTIONS_20261101.md) coordinates the requested higher-compute parallel investigation, including separate review and synthesis. The older setup status below is historical; the [Jensen register](../../research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md) continues to own aggregate J-B10 and the prior J tasks.

The usual `research-overview/`, `research-progress/`, `notes/`, `numerics/`, `reviews/`, `references/` and `chat-histories/` folders are in place. The continuation prepares research; no worker has been dispatched by this documentation task.

## Background

On a circle of circumference \(2\pi\), choose the Hamiltonian \(L=-\pi\,d^2/dx^2\). The normalized periodic modes have energies \(\pi n^2\), so
\[
\vartheta(\beta)=\operatorname{Tr}e^{-\beta L}
=\sum_{n\in\mathbb Z}e^{-\pi\beta n^2},\qquad\beta>0.
\]
The project uses the exact source reconstruction
\[
p(u)=\frac12e^u[\vartheta(e^{4u})-1],\qquad
\Phi(u)=\frac18[p''(u)-p(u)].
\]
The subtraction removes the zero mode. The source is therefore a differential expression in a reparametrized thermal trace. The coefficients consumed by the parent problem are
\[
c_n=\frac1{(2n)!}\int_0^\infty u^{2n}\Phi(u)\,du.
\]
Thermal parameter \(\beta\), source coordinate \(u\), auxiliary Mellin parameter \(s\), and physical heat time are different variables. The circle trace is an ordinary temperature-dependent trace, not a supersymmetric index.

## Summary of the approach

Use the complete integer-square spectrum, theta transformation or differentiated thermal identities to obtain a quantitative relation that survives source reconstruction and the coefficient integration. A useful outcome must bound a term in the complete Mellin response, or expose a precise limitation of a selected thermal comparison. It must retain the zero-mode subtraction, origin endpoints and the full infinite spectrum.

The trace identity itself is exact but gives no new determinant sign. Positive thermal weights do not automatically make the derivative-determinant observable positive. A finite spectrum replacement changes the source and needs an explicit error and endpoint analysis.

## Relationship to the other directions

- [02 Fermionic correlators](../02_fermionic_correlators/README.md) gives a many-particle representation of the coefficient determinants. The circle model supplies the source spectrum; the fermionic construction supplies the observable. The existing construction does not identify the circle Hamiltonian as the dynamical generator of those particular fermionic states.
- [03 Connected Mellin response](../03_connected_mellin_response/README.md) is the quantitative consumer of any useful thermal identity.
- [06 Topological field theory](../06_topological_field_theory/README.md) would require protected observables beyond this ordinary thermal trace.

## Initial J-E09 status (historical; current register above)

The heat-trace and source-reconstruction identities are available. No new thermal estimate for the signed curvature has been proved. **Potential follow-up: B — Astra**, because selecting a source-specific thermal identity is a conceptual choice: identify one identity and the precise joint term it controls. This folder does not issue a separate task or numerical request.

Read [Note04, Section 1](../notes/04_FERMIONIC_CORRELATORS_AND_PHYSICAL_INTERPRETATIONS_20261101.md), the [classical source normalization](../../../brainstorm/01_CLASSICAL_THETA_PRIMITIVES_SIGN_THEOREMS_AND_LESSONS_20261031.md), and the [parent direction map](../README.md#physical-research-directions). The [sole Jensen register](../../research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md) owns live status. Future derivations belong in this folder's `notes/`, computations in `numerics/`, and assessments in `reviews/` when needed. This chat retains its existing [parent archive](../chat-histories/README.md).

## MC01-B01 bounded return, 1 November 2026

Prepared for Edward Baker with substantial LLM assistance, gpt-6-astra / ultra. [Return01](notes/01_THERMAL_SOURCE_IDENTITY_RETURN_20261101.md) gives the complete filtered thermal-state identity, the explicit signed response observable, and a scoped obstruction to positivity-only transfer. No Mellin curvature bound was acquired; separate checking is pending. See the [sole local register](research-progress/01_CIRCLE_THERMAL_TRACE_RESEARCH_PROGRESS_20261101.md) for current task status.

**Checked assessment, 1 November 2026:** [separate review](reviews/01_MC01_E01_SEPARATE_REVIEW_20261101.md) accepted at its stated scope; the [local register](research-progress/01_CIRCLE_THERMAL_TRACE_RESEARCH_PROGRESS_20261101.md) owns current status. Six-direction [synthesis](../notes/06_PARALLEL_PHYSICAL_DIRECTIONS_SYNTHESIS_20261101.md). No Gaussian Mellin bound is acquired.

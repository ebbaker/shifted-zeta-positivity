# 03 Connected Mellin response and curvature bounds

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, effort **xhigh**. Setup task **J-E09**, documentation only.

This direction studies the original Mellin-curvature question in the language of generating functions and connected correlation functions. It is the quantitative target shared by the physical viewpoints, rather than a different theta source or an independent replacement for J-B10.

## Current research packet

1 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual preparation model **gpt-6-astra (Codex)**, reasoning effort **xhigh**. Preparation task **J-E10**, documentation only; no branch research executed.

Read [the research overview](research-overview/01_CONNECTED_MELLIN_RESPONSE_RESEARCH_OVERVIEW_20261101.md) for the expanded background and first bounded question. [The local progress file](research-progress/01_CONNECTED_MELLIN_RESPONSE_RESEARCH_PROGRESS_20261101.md) is now the sole live register for `MC03-B01` and later `MC03-` tasks. [Continuation05](../notes/05_CONTINUATION_PARALLEL_PHYSICAL_DIRECTIONS_20261101.md) coordinates the requested higher-compute parallel investigation, including separate review and synthesis. The older setup status below is historical; the [Jensen register](../../research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md) continues to own aggregate J-B10 and the prior J tasks.

The usual `research-overview/`, `research-progress/`, `notes/`, `numerics/`, `reviews/`, `references/` and `chat-histories/` folders are in place. The continuation prepares research; no worker has been dispatched by this documentation task.

## Background

For \(q=\prod_{j=1}^r u_j^2\), the Mellin integral is
\[
M_r(s)=\int_{0<u_1<\cdots<u_r}q^s V(\mathbf u^2)
\det[\Phi^{(2i)}(u_j)]_{i=0}^{r-1}\,d\mathbf u.
\]
At integers, \(M_r(k)=\prod_{j=0}^{r-1}(2k+2j)!\,D_{r,k}\). This does not assert a noninteger Toeplitz endpoint identity.

In the [fermionic representation](../02_fermionic_correlators/README.md), choose derivative orbitals \(f_i=\Phi^{(2i)}/\sqrt\Phi\), polynomial orbitals \(b_j=u^{2j}\sqrt\Phi\), and their wedge states \(|F_r\rangle,|B_r\rangle\). Then
\[
M_r(s)=\langle F_r|e^{s\widehat T}|B_r\rangle,
\qquad \widehat T=2\sum_{j=1}^r\log u_j.
\]
Where \(M_r(s)>0\), normalized cross matrix elements give
\[
(\log M_r)''(s)=\langle\widehat T^2\rangle_s^{FB}
-\bigl(\langle\widehat T\rangle_s^{FB}\bigr)^2.
\]
This is a connected response, but the different bra and ket prevent interpreting it automatically as a positive-state variance. Real-tilt positivity is available at order three from the accepted signed-averaging inputs, not at arbitrary order.

## Summary of the approach

The pilot asks for a complete bound at \(r=3\):
\[
(\log M_3)''(s)\le\kappa_3(s)
=\sum_{j=0}^{2}\sum_{n\ge0}(s+j+\tfrac12+n)^{-2},\qquad s\ge0.
\]
Using the positive carrier, its left side is exactly
\[
\operatorname{Var}_s(T)
+\frac{\operatorname{Cov}_s(h_3,(T-E_sT)^2)}{A(s)}
-\left(\frac{\operatorname{Cov}_s(h_3,T)}{A(s)}\right)^2,
\quad A(s)=E_sh_3.
\]
A source-derived Ward identity or full signed-integral estimate must control this joint expression. Bounding only the first variance leaves the centered-square covariance unpaid. The analytic tail/compact proposal in [Note03](../notes/03_IDEAS_AND_POSSIBLE_ROUTES_20261101.md) and the connected-response viewpoint are alternative tools for this same obligation.

The full domain includes \([0,2]\), the remaining compact range and an effective unbounded tail. The triangularly integrated Gaussian comparison is a weaker alternative; a change to that comparator must be explicit. Neither failure of the pointwise bound nor success at one finite order decides arbitrary-order induction.

## Relationship to the other directions

[01 Circle thermal trace](../01_circle_thermal_trace/README.md) may provide source-specific input; [02 Fermionic correlators](../02_fermionic_correlators/README.md) supplies the operator realization; [04 Biorthogonal ensembles](../04_biorthogonal_ensembles/README.md) supplies a positive carrier with a signed insertion; [05 Schur and Toda structure](../05_schur_toda_structure/README.md) provides coefficient identities. Each needs a new quantitative implication to resolve this target.

## Initial J-E09 status (historical; current register above)

The connected-response representation is exact within the integrability conditions in [Note04, Section 3](../notes/04_FERMIONIC_CORRELATORS_AND_PHYSICAL_INTERPRETATIONS_20261101.md), with preliminary same-assistant checking. The Gaussian bound remains unproved. **Next conceptual work: B — Astra, under existing J-B10:** choose one complete theta input and work through one bound or precise failure. Numerical execution requires a separately fixed E contract.

The issued [plan r1](../research-plan/01_MELLIN_CURVATURE_RESEARCH_PLAN_20261101.md) and [sole Jensen register](../../research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md) retain authority. See the [parent direction map](../README.md#physical-research-directions). Future work belongs in local `notes/`, `numerics/` and `reviews/` when needed; existing notes and [chat history](../chat-histories/README.md) remain in place.

## Bounded assessment return — 1 November 2026

[MC03-B01 Return01](notes/01_COMPLETE_MELLIN_RESPONSE_RETURN_20261101.md) derives a local three-particle Gaussian saddle model and an exact scaled signed response with explicit sufficient tail allowances. The global allowances and all-domain Mellin bound remain open. Separate review is pending; see the sole local register. Actual authoring model **gpt-6-astra / ultra**.

**Checked assessment, 1 November 2026:** [separate review](reviews/01_MC03_E01_SEPARATE_REVIEW_20261101.md) accepted at its stated scope; the [local register](research-progress/01_CONNECTED_MELLIN_RESPONSE_RESEARCH_PROGRESS_20261101.md) owns current status. Six-direction [synthesis](../notes/06_PARALLEL_PHYSICAL_DIRECTIONS_SYNTHESIS_20261101.md). No Gaussian Mellin bound is acquired.

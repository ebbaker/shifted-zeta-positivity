# Locator: earlier correlation, determinant and response hierarchies

7 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex assistance. Read-only repository search: tool-selected **gpt-6.1-sol/ultra**; related Wirtinger check: **gpt-6-astra/ultra**; root synthesis model/effort unavailable. **Evidence level: bounded source discovery and inherited result mapping, not a fresh full mathematical assessment.**

**Author clarification, 7 November 2026:** the intended earlier hierarchy is in [01_heat_density_asymptotics](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/investigations-5/01_heat_density_asymptotics/README.md), especially the ansatz fluctuation hierarchy and its recurrence development in §4 below. This supersedes the initial search ranking. The Mellin-curvature and theta-kernel constructions remain additional comparators, not the identified recollection. A bounded Markdown/TeX search across papers, excluding histories/snapshots and the current explanation when seeking predecessors, found no earlier literal factorial hierarchy for the complete canonical zero configuration.

All integrated operator sources and the linked older background are now available in the main checkout at /Users/ebbaker/Documents/shifted-zeta-positivity; the absolute links below resolve there. Their repo-relative locations begin at papers/. The original locator used Documents as read-only background while a separate partial checkout held new work; that preparation history remains provenance. The older background itself was not moved or duplicated. See the [7 November integration receipt](../../notes/TND_O_COMPLETE_HANDOFF_INTEGRATION_20261107.md). Exact source identities are in [additional sources40](../../research-progress/handoffs/40_TND_O_E22_ADDITIONAL_SOURCES_20261107.json).

## 1. Additional comparator: Mellin-curvature source/coefficient hierarchies

Start with [Note04: fermionic correlators and physical interpretations](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/investigations-5/07_positive_theta_primitives/01_jensen/01_mellin_curvature/notes/04_FERMIONIC_CORRELATORS_AND_PHYSICAL_INTERPRETATIONS_20261101.md) in the [Mellin-curvature folder](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/investigations-5/07_positive_theta_primitives/01_jensen/01_mellin_curvature/README.md). Closely related returns are [MC02 fermionic transfer](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/investigations-5/07_positive_theta_primitives/01_jensen/01_mellin_curvature/02_fermionic_correlators/notes/01_THETA_ORBITAL_COMPARISON_RETURN_20261101.md), [MC03 connected Mellin response](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/investigations-5/07_positive_theta_primitives/01_jensen/01_mellin_curvature/03_connected_mellin_response/notes/01_COMPLETE_MELLIN_RESPONSE_RETURN_20261101.md), [MC04 inserted ensembles](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/investigations-5/07_positive_theta_primitives/01_jensen/01_mellin_curvature/04_biorthogonal_ensembles/notes/01_INSERTED_ENSEMBLE_IDENTITY_RETURN_20261101.md) and [MC05 Schur constraints](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/investigations-5/07_positive_theta_primitives/01_jensen/01_mellin_curvature/05_schur_toda_structure/notes/01_THETA_SCHUR_CONSTRAINT_RETURN_20261101.md).

The parent construction expresses arbitrary-order determinants as pairings of two exterior states and as a signed observable under a positive source-coordinate carrier:
\[
D_{r,k}=\langle f_0\wedge\cdots\wedge f_{r-1},
g_{k,0}\wedge\cdots\wedge g_{k,r-1}\rangle,\quad
M_r(s)=Z_{r,s}\mathbb E_{r,s}h_r .
\]
The two exterior states differ. A positive carrier with a determinantal kernel gives source-coordinate correlations; it does not sign the insertion \(h_r\).

The MC02 transfer
\[
K_v=F(vS)/F(v),\quad
\langle I|\Gamma(K_v)|J\rangle
=\frac{v^{\sum J-\sum I}}{F(v)^r}\det[c_{j_b-i_a}]
\]
retains all finite ordered coefficient minors. All-sector positivity remains an RH-equivalent condition. Its obstruction concerns making this exact transfer self-adjoint in a positive metric preserving the required states.

MC04 gives the inserted Ward response
\[
(s+\tfrac12)M'(s)+3M(s)+N(s)=0,\qquad N(s)=\int q^sXG,
\]
with the signed insertion still present. Its finite-polynomial nonclosure is pointwise and scoped. MC05 gives the source-heat coefficient/Schur hierarchy
\[
\dot c_n=(2n+2)(2n+1)c_{n+1},
\quad
\dot t_m=2(m+1)(2m+1)t_{m+1}
+4\sum_{a+b=m+1}ab\,t_at_b,
\]
and a scoped finite-prefix nonclosure result.

[Coordinator assessment](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/investigations-5/07_positive_theta_primitives/01_jensen/01_mellin_curvature/reviews/01_PARALLEL_PHYSICAL_DIRECTIONS_ASSESSMENT_20261101.md) and the four separate internal Sol reviews accept these at their stated scopes. They report no new quantitative input advancing the Mellin comparison on a proved domain. Shared premises remain; this is not external specialist review.

**Carry the later author correction:** [4 November author correction](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/investigations-5/07_positive_theta_primitives/01_jensen/01_mellin_curvature/brainstorm/notes/05_FIXED_TEMPERATURE_DETERMINANT_AND_RADIAL_GREEN_20261104.md) distinguishes the thermodynamic parameter \(u=\log\beta/4\), auxiliary source-field fermions and a physical fixed-N box-particle ensemble. Determinant order r is not silently physical particle number N. The physical fixed-N N-body kernel has determinant form, but the note disclaims general lower-order canonical Wick factorization. Neither ensemble is a law for canonical zeros.

What the new correlation branch can consume: determinant/kernel algebra, correctly normalized factorial marginals, full-insertion response bookkeeping and explicit closure obligations. It cannot consume a favorable zero-statistic sign or a proved canonical-zero determinantal process. Existing canonical external source records remain in [the positive-theta references](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/investigations-5/07_positive_theta_primitives/references/06_PHYSICAL_INTERPRETATION_SOURCES_20261101.md); those articles were not freshly reassessed here.

## 2. Older complete-theta correlation kernels

Start at [Note36: complete theta correlations](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/36_COMPLETE_THETA_CORRELATIONS_AND_SIGN_TARGETS_20261015.md), with [Note38: Poisson parity obstruction](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/38_POISSON_PARITY_CORRELATION_AND_HEAT_OBSTRUCTION_20261015.md) and [Review26](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/investigations-2/active/21_quaternion_theta_geometry/reviews/26_OCTONIONIC_CORRELATION_MANUSCRIPT_INTEGRATION_20261015.md). This is a genuine all-order **source** hierarchy:
\[
K_m(t,s)=\int_{\mathbb R}r^{2m}w_t(s+r)w_t(s-r)\,dr,
\qquad w_t(u)=e^{tu^2}\Phi(u),
\]
\[
\partial_tK_m=2s^2K_m+2K_{m+1}.
\]
Note36 records exact reduction and open sign targets, including Fourier formulas for Laguerre observables. Here t is the source deformation parameter in that note, not silently the forward-time convention of the new operator branch. Review26 accepts the integrated identities with the theta-specific signed inequality still open. Positivity of \(K_1\) pointwise does not imply positivity of its Fourier transform.

Note38 retains an exact arithmetic identity but rejects the proposed separate global positive-time Poisson split. This is useful background for complete-source calculations and coupled tail control; it is not a zero factorial hierarchy and does not close the missing signed estimate.

## 3. Forest partition response at fixed real zeros

[Forest response Note17](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/investigations-4/12_height_dependent_heat_contours/notes/17_STATISTICAL_MECHANICS_AND_FOREST_RESPONSE_20261023.md) defines, for fixed distinct real nodes,
\[
Z(a)=\det(I+aL)
=\sum_F a^{|E(F)|}\prod_C|C|
\prod_{\{i,j\}\in E(F)}(x_i-x_j)^{-2}.
\]
For a positive forest weighting,
\(\partial_{\log a}\log Z=\mathbb E_a|E(F)|\) and
\(\partial_{\log a}^2\log Z=\operatorname{Var}_a|E(F)|\).
This is a configuration-dependent generating function, but the forests are random at a fixed real configuration; the zeros themselves are not sampled. The note is an explanatory finite identity, with no new theta estimate or phase-transition theorem. Its positive weights do not transfer automatically to complex transverse marks.

## 4. Author-identified hierarchy: heat-density asymptotics

**Primary reading order:** [Ansatz Note15](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/investigations-5/01_heat_density_asymptotics/ansatz/notes/15_GENERALIZED_TRANSFORMS_AND_HEAT_COMPONENT_HIERARCHIES_20261026.md) → [Ansatz Note16](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/investigations-5/01_heat_density_asymptotics/ansatz/notes/16_GAUSSIAN_FLUCTUATION_HIERARCHY_20261026.md) → [current recurrence overview](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/investigations-5/01_heat_density_asymptotics/recurrence/research-overview/01_RECURRENCE_RESEARCH_OVERVIEW_20261026.md). The root README places generalized transform/fluctuation hierarchies in recurrence; the [unified Book overview](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/investigations-5/01_heat_density_asymptotics/research-overview/02_BOOK_UNIFIED_HEAT_FLOW_RESEARCH_OVERVIEW_20261026.md) is the central synthesis. The separate [positive-time overview](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/investigations-5/01_heat_density_asymptotics/ansatz/research-overview/03_LARGE_POSITIVE_TIME_HIERARCHY_RESEARCH_OVERVIEW_20261026.md) organizes large positive Newman time and its regional bridges. These parameter regimes must not be silently identified.

Note15 (GT1)–(GT9) first gives the source moments
\[
\mu_j(T,z)=\int u^j e^{-Tu^2+izu}\rho(u)\,du,
\quad \partial_T\mu_j=-\mu_{j+2},\quad
\partial_z\mu_j=i\mu_{j+1},
\]
and Gaussian heat components. Here the forward heat family is \(h(T,z)=H(-T,z)\), so T>0 is **negative Newman time**. These are not many-body BBGKY equations.

More directly related to the discussion of a generating functional, Note16 (FH4), (FH7)–(FH12) introduces
\[
\mathcal Q_T=d+2T\partial_d,\qquad
\mathcal D_{\epsilon,r}
=\frac{\kappa_{\epsilon,r+1}}{(r+1)!}\mathcal Q_T^{r+1},
\]
\[
\mathcal U_\epsilon(s)
=\exp\!\left(\sum_{r\ge1}s^r\mathcal D_{\epsilon,r}\right)U_{\epsilon,0}
=\sum_{j\ge0}s^jU_{\epsilon,j},
\quad
jU_{\epsilon,j}=\sum_{r=1}^j r\mathcal D_{\epsilon,r}U_{\epsilon,j-r}.
\]
The \(\kappa\)'s are logarithmic derivatives of the exact gamma carrier at the frozen chart center, not asserted probability cumulants. The base retains both arithmetic arms and all modes. Fluctuation order j counts powers of inverse height in the shape coefficients; it is distinct from polynomial degree, arithmetic index and Riemann–Siegel completion order K. Each coefficient is a finite polynomial, so the recurrence is exact without asserting convergence of the infinite operator sum. Note16 also gives a genuine continuous deformation on a bounded initial window, with separate tail payments for whole-line replacements.

**There is later quantitative growing-order work.** [Recurrence Note03](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/investigations-5/01_heat_density_asymptotics/recurrence/notes/03_FIXED_ORDER_FLUCTUATION_HIERARCHY_20261026.md) proves the fixed-order comparison; [Note05](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/investigations-5/01_heat_density_asymptotics/recurrence/notes/05_CONTROLLED_ORDER_GROWTH_AUDIT_20261026.md) with [Review04](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/investigations-5/01_heat_density_asymptotics/recurrence/reviews/04_CONTROLLED_ORDER_GROWTH_ASSESSMENT_20261026.md) re-audits actual constants for growing order rather than substituting p(X) into hidden fixed-p constants. With \(L=\log(X/(4\pi))\), \(p=\lfloor L/2\rfloor\), \(K=2p\), it pays outer-envelope field/spatial0–3/first-time error \(e^{-L^2/4}\) on \(1\le T\le2\), retaining all arithmetic modes, coefficients and the bounded completion integral. [Note20](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/investigations-5/01_heat_density_asymptotics/recurrence/notes/20_MOVING_LOWER_ENDPOINT_20261026.md) and [Review14](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/investigations-5/01_heat_density_asymptotics/recurrence/reviews/14_MOVING_ENDPOINT_ASSESSMENT_20261026.md) extend the declared target to \(1/L\le T\le2\) at a stronger sufficient height onset. T=0 is excluded. These are proved-in-note results with same-model internal assessments and shared premises; this clarification is not a fresh proof audit. Complete evaluator implementation/certification and broad program gates retain their original statuses.

**What TND-OC and TND-OG can consume:** a controlled field/jet reconstruction hierarchy, its explicit order-versus-height bookkeeping, and a model for deriving recurrences from an exponential generating family. The proposed zero functional \(\mathcal Z_\lambda[f]=\prod_j(1+f(z_j))\) instead grades factorial zero statistics. Their combinatorics may inform each other, but there is no established identification between the two hierarchies.

A possible transfer is to approximate H and H' with the HDA hierarchy, then control H'/H on a declared contour and use it in a zero/Green observable. The transfer still requires a paid denominator margin, complete boundary/source errors and matching time regime; the negative-time theorem is not a theorem at Newman parameter zero or positive time. Very small field error alone does not prove the required signed zero comparison. The positive-time branch and its bridge results must be read separately if selected.

The present operator Gaussian-Laguerre hierarchy remains a separate comparator. No HDA status or research task is changed by this author clarification.

## 5. Related earlier Wirtinger formulation

[Complex-potential Note20](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/investigations-4/12_height_dependent_heat_contours/notes/20_COMPLEX_POTENTIAL_AND_WIRTINGER_FORMULATION_20261024.md) studies the regulated field
\[
W=2\partial_z^2\log(|H|^2+\epsilon^2).
\]
It already records holomorphic ambiguity and no automatic gain from a change of variables. The author's present intermediate field is different:
\(R=2\partial_z\log|H|=H'/H\), with
\(\partial_{\bar z}R=\pi\nu\). The old note is useful background for the Green branch, not evidence that the proposed first-order estimate has been proved.

## 6. Current explanation and next use

[The author's saved Green explanation](/Users/ebbaker/Documents/shifted-zeta-positivity/papers/investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/brainstorm/explanations/01_Green_function.md) literally contains the proposed
\(\mathcal Z_\lambda[f]=\prod_j(1+f(z_j))\) and the weighted ensemble comparator
\(\mathbb E\prod_j[1+\eta w_{X,h}(x_j)]\).
It is the current discussion saved by the author, not an older completed zero hierarchy. It was read as explanatory context; mathematical evidence is linked in the new branch overview and the parent manuscript/notes.

The author-identified primary read for TND-OC-B01 is HDA ansatz Notes15–16, followed by the current recurrence overview and the exact growing-order result/review selected for reuse. Mellin Note04 and theta-kernel Notes36–38 remain optional secondary comparisons. Choose at most two actual mechanisms; do not turn all located folders into parallel research campaigns. Return an exact transfer or the precise missing premise. See the [correlation overview](../../02_localized_zero_correlations/research-overview/01_TND_OC_RESEARCH_OVERVIEW_20261107.md) and [Green overview](../../01_green_potential_resolvent/README.md).


Clarification provenance: [E22 r2 inputs41](../../research-progress/handoffs/41_TND_O_E22_R2_HIERARCHY_CLARIFICATION_INPUTS_20261107.json) and [return41](../../research-progress/handoffs/41_TND_O_E22_R2_HIERARCHY_CLARIFICATION_RETURN_20261107.json). Root owns this amendment; selected Sol6.1/ultra supplied read-only source checking. Original E22 packets remain historical, byte-identical records.

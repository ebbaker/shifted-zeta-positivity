# Manuscript recommendations: compact transfer, source formulas and crossover scope

24 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. **gpt-6-astra (Codex), actual effort xhigh**, verified from session metadata. Chat 0012.

**Status: analytical/editorial recommendations, not an implemented manuscript revision or a new proof.** The reviewed baseline is the maintained 65-page manuscript through Note 31; the [input manifest](39_MANUSCRIPT_RECOMMENDATION_INPUTS_20261024.json) pins its TeX/build inputs and Notes 34–38. The recommendations below integrate existing in-note results at their stated scopes. [Review 21](../reviews/21_NOTES35_37_PROJECT_AND_JOIN_ASSESSMENT_20261024.md) supplies the recent assessment; it did not audit the complete endpoint chain or complete HDA-20.

The primary objective remains a relatively simple formula for the **unnormalized** regulated density for every real heat time, with informative proved error extending to arbitrarily large height, and compatible potential, current and actual covariance. See the [overview](../research-overview/01_AVERAGED_DENSITY_RESEARCH_PROGRAM_20261024.md), [result index](../../../../result-summaries/README.md), [heat-flow summary](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md) and [avoid index](../../../../avoid/README.md), especially [scoped exclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [claims stronger than evidence](../../../../avoid/06_status_stronger_than_the_evidence.md).

## 1. Recommended introduction and scope

Keep the present title and the endpoint statements in the abstract. The new mathematics strengthens finite-source comparison and local time joining; it does not supply the missing global approximation. Do not retitle the paper as a phase-transition or conformal-field-theory result.

Suggested replacement for the final finite-source/joining portion of the abstract, after integration of the proofs below:

> On compact full buffers, weak identities transfer field errors of orders zero and two to the complete filtered observable system and give a local time-joining estimate with its exact heat residual. Positive cubic-Hermite sources provide fourth-order interpolation remainders and finite Gaussian-moment representations; amplitude-aware signed-source bounds improve nonlinear transfer. These formulas do not yet yield an accepted continuous finite-core certificate or a compatible all-height assembly. The chosen regulator also produces a sharp infinite-height crossover, whose center and rounding width are distinct. Its correlation and response interpretation remains open. Numerical evidence is supporting and diagnostic.

Retain the abstract's fixed-cutoff exclusion, but state its proved class when discussing fixed-time off-axis potential error: the positive-terminal-value piecewise-linear cutoff class of Note 25. This is distinct from the fixed-compact-source positive-infinite-time obstruction already in the manuscript. Neither is a theorem excluding every tapered or Hermite outer representation.

Suggested opening expansion in [01_framework.tex](../manuscript/01_framework.tex), following its first paragraph:

> The target is a quantitative approximation to one canonical theta heat field under a specified measurement protocol. Its averaged density retains its absolute scale. A useful global formula must compare density, potential, current and the actual filtered gradient covariance on common support buffers, and must retain the forcing and curvature terms produced by the regulator. Direct comparison with the canonical source is the principal route; an autonomous reduced evolution would require an additional closure and stability argument.
>
> Different asymptotic formulas cover negative time, a finite central region, and positive time or large height. Joining these formulas is a compatibility problem. A time-dependent blend preserves spatial holomorphy but adds a calculable heat residual; a spatial cutoff generally destroys holomorphy. We give a compact transfer and local time-joining estimate, while informative continuous-core bounds, effective endpoint allowances and a compatible global spatial construction remain open.
>
> A second issue is the thin crossover created by the chosen regulator. At each finite height the regulated observables are smooth, but their normalized infinite-height limit changes at the switch. The exact crossover center and its rounding width have different scales. This motivates a finite-size-scaling comparison and a future study of connected correlations and response, without identifying the regulator switch as an intrinsic critical time.

The introductory source map should then say that Notes 34–37 add analytical finite-core tools and Note 38 supplies an interpretive research direction. Notes 32–33 are continuation/handoff records, not additional theorem sources. Preserve the author and LLM acknowledgment; distinguish Sol's derivations in Notes 35–37 from Astra's Note 34 and the present recommendations.

In [10_global_protocol.tex](../manuscript/10_global_protocol.tex), extend the model guide's finite-source row to positive piecewise cubic sources and add the local time blend as a separate row with a nonzero residual. Keep \(P_{\rm lin}\) and \(P_*\) distinct. The switch center belongs to the former analysis; positive all-height evolution belongs to the latter.

## 2. Add the compact weak transfer and local time-join theorem

Place a new analytical section after the finite-source/local-transfer material, before the outer gamma sections. Import [Note 34](34_COMPACT_WEAK_TRANSFER_AND_TIME_JOIN_20261024.md), CJ3–CJ20 and CJ22–CJ28, with its proof and full observable table.

For holomorphic \(F\), write
\[
D_F=|F|^2+q,\quad S_F=\log D_F,\quad w_F=q/D_F,\quad
V_{m,F}=w_F^mF_{zz}\overline F/D_F,\quad E_F=F_t+F_{zz}.
\]
The useful structural identities, for real compactly supported tests \(\psi\), are
\[
4\pi\langle\rho_F,\psi\rangle
=\int S_F\Delta\psi+2\int w_F\nabla r\cdot\nabla\psi
+\int\{w_F\Delta r+w_F(1-w_F)|\nabla r|^2\}\psi,
\tag{MR1}
\]
\[
\pi j_F=\partial_{\bar z}V_{0,F}+(\partial_{\bar z}r)V_{1,F},
\qquad
S_{F,x}^2-S_{F,y}^2
=4\Re V_{0,F}-\mathcal D S_F+(r_{xx}+r_x^2)w_F,
\tag{MR2}
\]
where \(r=\log q,\ r_y=0,\ \mathcal D=\partial_x^2-\partial_y^2\).
MR1 is already present as the static weak-density lemma; reference it rather than repeat its proof. MR2 and the direct time identities explain the reduction in source orders.

On a **compact full buffer**, freeze amplitude and regulator caps, let
\(d_j\ge|\partial_z^j(H-F)|\) for \(j=0,2\), and \(\eta_E\ge|E_F|\).
Every required filtered observable/derivative row has an explicit positive map
\[
\mathcal E_{V,\alpha}
=A_{V,\alpha}d_0+B_{V,\alpha}d_2+C_{V,\alpha}\eta_E.
\tag{MR3}
\]
Include CJ5–CJ14's coefficients, not merely the assertion that constants exist. The table covers \(U,W\) through spatial order four; \(R,\overline C,J,Q\) and the required direct time/forcing/source terms at their stated orders. It includes \(\Delta Q,\overline C_t,\mathcal D\overline C\) and traces. The proof uses kernel weak derivatives through order four, including current order three internally. It does not claim pointwise jet-order reduction or applicability to arbitrary filters.

For a time overlap with width \(\tau\), set
\[
F=(1-\theta)F_1+\theta F_2,\qquad
E_F=(1-\theta)E_1+\theta E_2+\theta'(F_2-F_1),
\tag{MR4}
\]
\[
\eta_E\le(1-\theta)\eta_1+\theta\eta_2+
\frac{c_\theta}{\tau}(h_{1,0}+h_{2,0}),\qquad
|\theta'|\le c_\theta/\tau.
\tag{MR5}
\]
The \(h_{i,j}\) are field errors against the same \(H\) on the whole overlap. The additional allowance in MR3 is
\(C_{V,\alpha}c_\theta(h_{1,0}+h_{2,0})/\tau\).
Observable overlap alone cannot substitute for these field errors. Widening the overlap changes its caps and regulator floor.

With \(Z_0=E_F\overline F/D_F\), include the actual joined equations
\[
(U_F)_t=-\tfrac12(\mathcal D U_F+U_{F,x}^2-U_{F,y}^2+Q_F)
+\overline{\mathcal B}_F+2\Re(K*Z_0),
\quad
\Delta U_F=4\pi(R_F+\overline C_F),
\tag{MR6}
\]
and CJ26's density and current equations, including
\((2\pi)^{-1}\Delta\Re(K*Z_0)\) and \(K*D_E\).
Use the weak residual formula CJ18 to bound the latter without an unpaid \(E_z\).
Compute \(Q_F\) from \(S_F\); it is not the convex average of the component covariances.

End with the precise unresolved spatial term
\[
\partial_{\bar z}\big((1-\lambda)H_f+\lambda P_*\big)
=(\partial_{\bar z}\lambda)(P_*-H_f).
\tag{MR7}
\]
This excludes applying the holomorphic formulas unchanged to this uncorrected cutoff. It leaves corrected constructions and other compatible representations open.

## 3. Integrate the sharper local and signed-source formulas

Keep the local transfer from Note 23 alongside the new weak route. [Note 35](35_WEAK_TRANSFER_BUDGET_DECISION_20261024.md) gives no uniform dominance of weak transfer. Its diagnostic conclusion is a reason to retain both analytical options, not to replace all local estimates with MR3. Componentwise minima are legitimate only where both bounds pay the same error category on the same domain with compatible frozen caps.

In the local-transfer subsection, add the signed radial factorization from [Note 36](36_SOURCE_CURVATURE_AND_PEAK_INTEGRATION_20261024.md), AS2–AS6:
\[
\mathcal S_F=A_s(|F|)
\{r_t|F_z|^2+r_x\Re(F_{zz}\overline{F_z})\},
\qquad
A_s(v)=\frac{q(v^2-q)}{\pi(q+v^2)^3},
\tag{MR8}
\]
\[
A_s'(v)=\frac{4qv(2q-v^2)}{\pi(q+v^2)^4},\qquad
A_s''(v)=\frac{4q(2q^2-17qv^2+5v^4)}{\pi(q+v^2)^5}.
\]
For two fields with jet discrepancies \(d_0,d_1,d_2\) and common caps \(P_1,P_2\), let \(a_s=\sup|A_s|\), \(a_{s,1}=\sup|A_s'|\) on a common amplitude interval. Then
\[
|\delta\mathcal S|
\le a_s\{2|r_t|P_1d_1+|r_x|(P_1d_2+P_2d_1)\}
+a_{s,1}(|r_t|P_1^2+|r_x|P_1P_2)d_0.
\tag{MR9}
\]
The maxima reduce to endpoints and the explicit stationary points in AS3. This compares the signed source directly and requires no heat equation. Transfer spatial derivatives by
\[
|\partial^\alpha K*(\mathcal S_H-\mathcal S_F)|
\le |\partial^\alpha K|*\mathcal E_{\mathcal S}.
\tag{MR10}
\]
The varying regulator coefficients stay inside the integral. Do not freeze them at the observation point or omit their derivatives in a different transfer route.

AS7–AS10's companion \(W_t,C,C_t\) bounds may go in an appendix. Their exact-heat premise must remain visible; a joined or saddle field needs AS11/CJ17 residual corrections.

For source curvature, include the signed derivative-polynomial/Bernstein cap and complete mode tail of SP1–SP3. Explain the positive chord-weight integration analytically, while leaving the adaptive mesh heuristic and numerical performance in Note 36. The convex-weight argument is stated for nonnegative \(t,Y\); a larger time domain requires its own weight bound.

## 4. Add the positive cubic-Hermite source construction

This is the main explicit-formula improvement in [Note 37](37_POSITIVE_HERMITE_SOURCE_AND_REMAINDERS_20261024.md). Extend [08_finite_time.tex](../manuscript/08_finite_time.tex) without removing the simpler linear construction or its valid estimates.

For \(A_n=\pi n^2e^{4u}\), record
\[
\Phi_n=\pi^{-1/4}n^{-1/2}e^{-A_n}A_n^{5/4}P_0(A_n),\quad
P_0(A)=-3+2A,\quad
P_{k+1}=(5-4A)P_k+4AP_k',
\tag{MR11}
\]
\[
P_4=-1875+30930A-68096A^2+41408A^3-8448A^4+512A^5.
\]
HE2–HE3 bound the **complete** fourth derivative continuously on each cell by Bernstein coefficients and a full omitted-mode tail. Distinguish the number of modes in the constructed source from those used to bound its derivative remainder.

For \(g\in C^4([a,b])\), its cubic Hermite interpolant satisfies
\[
|g(u)-\mathcal H g(u)|
\le\frac{B_4}{24}(u-a)^2(b-u)^2,\quad
\|g-\mathcal H g\|_\infty\le B_4h^4/384,
\quad
\int_a^b|g-\mathcal H g|\le B_4h^5/720.
\tag{MR12}
\]
Apply this to the complete \(\Phi\), then pay finite-mode value and slope errors, value and slope arithmetic, and construction error separately. The last integral is unweighted; use HE9's weighted formulas for field jets. The right-end slope cardinal is negative, so its error uses the absolute cardinal.

For endpoint values \(v_a,v_b\), slopes \(d_a,d_b\), and \(h=b-a\), the cubic Bernstein coefficients are
\[
\beta_0=v_a,\quad \beta_1=v_a+hd_a/3,\quad
\beta_2=v_b-hd_b/3,\quad \beta_3=v_b.
\tag{MR13}
\]
Nonnegative exact stored coefficients define a nonnegative finite source. Positivity of that chosen polynomial is distinct from accuracy against \(\Phi\). Charge discrepancies between stored coefficients and exact construction from endpoint data under HE8. If positivity cannot be established, the declared linear fallback carries its own second-order remainder; do not retain MR12's fourth-order claim on that cell.

For time-independent source coefficients,
\[
F(t,z)=\int_0^U e^{tu^2}f(u)\cos(zu)\,du
\]
is an entire exact heat field. It remains a finite Gaussian-moment formula: for
\(I_k(t,z;a,b)=\int_a^b u^ke^{tu^2+izu}\,du\),
\[
2tI_k=[u^{k-1}e^{tu^2+izu}]_a^b-(k-1)I_{k-2}-izI_{k-1}.
\tag{MR14}
\]
Use \(k=1\) with the middle term omitted, and \(k\ge2\) otherwise; handle removable \(t=0\) limits explicitly. This extends the current \(I_0,I_1\) representation to cubic cells and differentiated jets. It does not certify numerical stability of raw error-function subtraction.

Include HE10's ideal-Gauss truncation bound, either here or in the analytic appendix. With \(c_i=(a_i+b_i)/2,\ d_i=(b_i-a_i)/2,\ h_i=b_i-a_i\), \(C_i=\max_k\beta_{ik}\),
\[
\vartheta_i=(2|t|c_i+|z|)d_i+|t|d_i^2,\quad
M=\left\lfloor(2G-1-j-3)/2\right\rfloor\ge0,
\]
\[
|\partial_z^jF-\mathcal G_G[\partial_z^jF]|
\le2\sum_i h_iC_i b_i^j e^{tc_i^2+Yc_i+\vartheta_i}
\frac{\vartheta_i^{M+1}}{(M+1)!}.
\tag{MR15}
\]
State the exact-node/weight premise and separate rounding and spatial filtering. The proof is polynomial exactness plus an exponential Taylor remainder, not refinement agreement.

HE11's directional common-gradient cap is useful as a short refinement remark. Preserve its demonstrated \(r_x=r_y=0\) setting and freeze the cap using total source-plus-evaluator errors before splitting budget categories. General height-dependent-regulator use needs the additional regulator terms.

## 5. Clarify the regulator crossover without duplicating its theorem

The present [11_gamma_outer_switch.tex](../manuscript/11_gamma_outer_switch.tex) already contains the two-layer profile, exact center and switch law. Retain these results and add a short interpretation after Corollary \(\mathrm{cor:switch\text{-}scaling}\), citing [Note 38](38_PHASE_TRANSITION_LITERATURE_AND_JOIN_DIAGNOSTICS_20261024.md).

The important quantities to display together are
\[
b=\log(\epsilon_g/A_X),\quad b(t_c,X)=0,\quad
d=b_+/\omega,\quad
R_{\rm layer}=\frac{\omega}{2\pi}[k_h(y-d)+k_h(y+d)],
\]
\[
t_c-64\sim\frac{64}{\log X},\qquad
t=t_c-\frac{128\tau}{\pi X\log X},\qquad
\frac{R}{\log X}
=\frac{k_h(y-\tau_+)+k_h(y+\tau_+)}{8\pi}
+O((\log X)^{-1}).
\tag{MR16}
\]
The law is uniform for bounded \(\tau\) and \(|y|\le Y\) on the stated full buffers. The implicit center is essential: its leading approximation is not accurate on the rounding-width scale. The unnormalized remainder is \(O(1)\), not a vanishing absolute allowance for the global accuracy contract. No time/current/covariance theorem follows by differentiating it. The two regularized layers are not nonreal zeros.

A short outlook can introduce the diagnostic
\[
m_X(t)=\frac{4\pi R(t,X,0)}{k_h(0)\log X},
\tag{MR17}
\]
whose fixed-time limits are zero for \(t\le64\) and one for \(t>64\). This normalized diagnostic does not replace the unnormalized target or establish an intrinsic Landau order parameter. Landau theory, RG or CFT should enter as possible methods with missing premises, not claimed structures.

Define the next correlation question before importing criticality language. For a declared observable \(O\), normalized window \(W_X\), width and limiting regime, a possible connected statistic is
\[
\mathcal C_X(s;t)=
\langle O(t,X+u)O(t,X+u+s)\rangle_{W_X}
-\langle O(t,X+u)\rangle_{W_X}
 \langle O(t,X+u+s)\rangle_{W_X}.
\tag{MR18}
\]
The next research note must choose \(O\), specify centering and known amplitude scales, and define a perturbation and response. An integrated correlation is not automatically a susceptibility, and the existing signed local covariance \(Q\) is not MR18. Correlation-length growth and integrated-response growth are the relevant tests; a fixed-separation two-point value need not diverge.

Cite the [scoped primary-literature record](../references/PHASE_TRANSITION_METHODS_20261024.md). Use Fisher–Barber for the shift/rounding analogy and Tong for order parameters and connected correlations; reserve Wilson/CFT or coalescing-saddle discussion for the outlook where justified. Note 38's alternative-flat-switch calculation is conditional and belongs in that outlook, if retained. It supplies no new theta critical exponent, physical regulator or theorem.

## 6. Update the coverage table and evidence presentation

In [14_scope_and_remaining_work.tex](../manuscript/14_scope_and_remaining_work.tex), preserve the existing endpoint/outer rows and add:

| Input | Analytical addition | Remaining limitation |
| --- | --- | --- |
| Note 34 CJ14/CJ20 | Complete compact filtered-system transfer from \(d_0,d_2,\eta_E\) | Requires a compact positive regulator floor and useful enclosed caps. |
| Note 34 CJ22–CJ27 | Holomorphic local time join and exact residual equations | No accepted endpoint/cutoff budget or global spatial construction. |
| Note 36 AS2–AS6 | Direct signed-source radial comparison | Whole-buffer coefficients and integration must be bounded. |
| Note 37 HE1–HE10/HE12 | Positive cubic source, complete fourth-order remainder, finite moments and ideal evaluator bound | Arithmetic, filtering and continuous space/time coverage remain separate. |
| Notes 28/38 | Existing exact-center crossover, interpreted through shift and rounding | Correlation/response specification and any intrinsic criticality claim are open. |

Replace the broad closing statement that “joining estimates remain to be proved” by: “A compact time-joining estimate is available. Informative endpoint and cutoff allowances, continuous finite-core coverage and a compatible all-height spatial assembly remain to be proved.”

Keep the numerical appendix brief. Cite Notes 35–37 for the failed weak-transfer trial, source refinement, Hermite comparisons and sampled directional-cap success. Preserve the earlier failed 192-cell trial and the later failed comparators by reference. Do not copy mesh tables, promote sampled source-budget success to a complete certificate, or call ideal quadrature truncation an arithmetic enclosure.

Update the source map and bibliography for Notes 34–38 and the scoped literature. Keep numerical records in their existing notes/numerics files. Retain the distinction between same-assistant derivations, the limited cross-model Review 21 and an unperformed specialist audit.

## 7. Implementation order and stopping conditions

**Next deliverable: manuscript revision — Sol**, under [HDA-10-MI2 r1](../research-progress/handoffs/HDA-10-MI2.md). Integrate Sections 2–4 first, revise the introduction and coverage table to match their actual inclusion, then add the short crossover interpretation. This recommendation note and the overview/progress updates are complete; manuscript production has not begun under this request.

A finished revision must include the relevant proofs and hypotheses, resolving source references, preserved physical \(q\) and actual \(Q\), explicit residuals, and a checked reading copy. Do not fill missing analytical coverage with numerical tables. Any unresolved source inconsistency should be recorded precisely and that claim deferred. No new numerical run, criticality theorem or global join is part of this production packet.

The separate research priorities are: **Analysis — Sol** for the precise crossover/correlation/response specification (HDA-21); **Analysis and numerics — Sol** for the frozen-point arithmetic/filter certificate; and **Analytical — Astra** only for the difficult global spatial compatibility estimate or a specifically resistant differentiated-layer estimate. HDA-17 remains Partial, HDA-18 Gated, and HDA-20 unfulfilled.

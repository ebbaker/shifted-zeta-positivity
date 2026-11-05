# Energy-filtered theta overlaps

> **Continuation routing updated 5 November 2026.** [Overview02](02_ANGULAR_RADIAL_THETA_MODEL_RESEARCH_OVERVIEW_20261105.md) adds the angular/radial analytic program and the author's all-order hypothesis restriction. [Register02](../research-progress/02_ANGULAR_RADIAL_THETA_MODEL_RESEARCH_PROGRESS_20261105.md) is the sole current register; Register01 and the dated continuation recommendations below are historical. The original task IDs and mathematical evidence are preserved. Update prepared for Edward Baker with substantial LLM assistance, actual gpt-6-astra/xhigh.

**Draft research overview · 4 November 2026**  
Drafted for Edward Baker with substantial LLM assistance from OpenAI Codex, recorded model **gpt-6-astra**, reasoning effort **xhigh**.

The [research plan](#research-plan) sets out the three-orbital comparison. The [progress register](../research-progress/01_ENERGY_FILTERED_THETA_OVERLAPS_RESEARCH_PROGRESS_20261104.md) records current task status.

**Current execution return, 4 November 2026:** [E03 Note03](../notes/03_MC11_E03_R1_FIRST_EXCITED_ACQUISITION_AND_RETURN_20261104.md) now encloses a positive three-orbital net change: both groups reinforce, with the first excited level supplying more than 99.99997573% of the gain. The first 384-bit acquisition met every width goal. **E04 now accepts the finished return without correction; [B] MC11-B01 — Astra is ready and unstarted**. The assessment is internal same-assistant/same-model with shared acquired premises; the original plan and historical starting evidence remain below.


## The question

What happens to a signed theta determinant when the excited energy levels of the underlying quantum box are admitted one at a time, or all together? At two orbitals, every excited level increases each coefficient that enters the determinant. Yet every level lowers the overlap, and restoring the entire spectrum costs less than one ten-thousandth of its first-mode value. At three orbitals, sufficiently high levels push the overlap upward. Understanding why the direction changes, and how much the different energies contribute in total, is the subject of this investigation. These fixed-order findings come from a [brainstorm derivation with proof-author checks](../../10_radial_green_determinants/brainstorm/notes/03_SPECTRAL_FILTER_AND_TWO_ORBITAL_EXCHANGE_20261104.md).

Two sibling investigations supply different parts of the question. Open quantum dynamics identifies the two source preparations whose antisymmetrized overlap carries the sign. Radial Green determinants retains the exact endpoint when comparing the first theta mode with the complete source and gives quantitative bounds on the coefficient errors. Bringing the two together lets us vary a physical input, the weight of an energy level, and follow its effect on the same determinant used in the analytic comparison. [MC08 source states](../../08_open_quantum_dynamics/brainstorm/notes/08_RETURN_TO_SOURCE_STATES_AND_TRANSFER_PAIRING_20261103.md) · [Radial Green manuscript](../../10_radial_green_determinants/manuscript/radial_green_determinants.tex)

## From the box spectrum to the determinant

Take a particle in the unit Dirichlet box with one-particle Hamiltonian \(H=-\pi^{-1}\partial_x^2\) and energies \(E_n=\pi n^2\), \(n\ge1\). Let \(P_1\) project onto the lowest level. At each inverse temperature \(\beta=e^{4u}\), \(u\ge0\), apply the filter with effect \(W_s=P_1+s(I-P_1)\), \(0\le s\le1\). The ground level always passes. Each excited level passes with probability \(s\). Keep the total accepted weight in the heat trace
\[
 Z_s(\beta)=\operatorname{Tr}(W_s e^{-\beta H})
 =e^{-\beta\pi}+s\sum_{n\ge2}e^{-\beta\pi n^2}.
\]
The setting \(s=0\) gives the first mode on the full half-line in \(u\). Opening the filter to \(s=1\) restores every square level with unit weight. The corresponding primitive, source and moments are
\[
 p_s(u)=e^u Z_s(e^{4u}),\qquad \Phi_s(u)=\tfrac18(p_s''(u)-p_s(u)),\qquad
 c_j(s)=\int_0^\infty \frac{u^{2j}}{(2j)!}\Phi_s(u)\,du .
\]
Here \(x\) is the particle's position and \(u\) labels temperature. The filter strength \(s\) varies the source at physical heat time zero. [Box interpretation](../../brainstorm/notes/05_FIXED_TEMPERATURE_DETERMINANT_AND_RADIAL_GREEN_20261104.md) · [MC08 spectrum and energy labels](../../08_open_quantum_dynamics/research-progress/handoffs/10_NATURAL_HAMILTONIAN_BRAINSTORM_CONTINUATION_20261103.md)

In the source Hilbert space \(L^2((0,\infty),du)\), the two orbital preparations probe derivatives and moments of the same \(\Phi_s\):
\[
 f_i^{(s)}=\frac{\Phi_s^{(2i)}}{\sqrt{\Phi_s}},\qquad
 g_\ell^{(s)}=\frac{u^{2\ell}}{(2\ell)!}\sqrt{\Phi_s}.
\]
The diagonal uses \(0\le i<q\) and \(q\le\ell<2q\). In this range, integration by parts gives \(\langle f_i^{(s)},g_\ell^{(s)}\rangle=c_{\ell-i}(s)\). The power \(u^{2\ell}\) kills every lower-endpoint term, and decay handles the outer endpoint. Equivalently, the boundary-preserving Green interpolation can carry its compensating mass at \(u=0\). Every coefficient index in this block is at least one, so the atom contributes zero. This detail matters if the comparison is extended to other blocks. [Green identity and boundary terms](../../10_radial_green_determinants/manuscript/sections/01_green.tex)

The overlap of the two ordered, antisymmetrized preparations is
\[
 D_q(s)=\left\langle\bigwedge_{i=0}^{q-1}f_i^{(s)},\
                       \bigwedge_{j=0}^{q-1}g_{q+j}^{(s)}\right\rangle
       =\det M_q(s),\qquad [M_q(s)]_{ij}=c_{q+j-i}(s).
\]
Thus \(q\) counts source orbitals, while the physical trace is over the one-particle box. The response and fractional losses below concern this **unnormalized real overlap**. Normalizing the wedges introduces norms that vary with \(s\). At \(s=1\), the generating function is \(\sum_{j\ge0}c_j(1)z^j=\tfrac18\xi((1+\sqrt z)/2)\), and \(D_q(1)\) is exactly its diagonal coefficient determinant \(D_{q,q}\). This is the link to the Jensen investigation's question about the zeros of the Riemann xi-function. [Source-state pairing](../../08_open_quantum_dynamics/brainstorm/notes/08_RETURN_TO_SOURCE_STATES_AND_TRANSFER_PAIRING_20261103.md)

## What an individual level contributes

Let \(a_j(E)\) be the \(j\)th moment of one level's source density \(\phi_E(u)=e^u(2X^2-3X)e^{-X}\), \(X=Ee^{4u}\). On the diagonal, \(c_j(s)=a_j(\pi)+s\sum_{n\ge2}a_j(E_n)\). A small increase in the weight of level \(E\) changes the overlap at the signed rate
\[
 \chi_q(E;s)=\sum_{i,j=0}^{q-1}\operatorname{cof}_{ij}M_q(s)\,a_{q+j-i}(E).
\]
The cofactors are evaluated with the current filter setting. Consequently
\[
 D_q(1)-D_q(0)=\int_0^1\sum_{n\ge2}\chi_q(E_n;s)\,ds
\]
includes the mixed effects of restoring many levels. For fixed \(q\) the moment sums converge and the cofactors are bounded along the path. This identity specifies the quantity whose sign and size need an estimate. [Level-response derivation](../../10_radial_green_determinants/brainstorm/notes/02_HILBERT_SPACE_AND_ENERGY_RESOLVED_CANCELLATION_20261104.md)

**Two orbitals.** In \(D_2=c_2^2-c_1c_3\), the two products are the direct and exchanged pairings. At any filter setting the change from one excited level is
\[
 \chi_2(E;s)=2c_2(s)a_2(E)-c_3(s)a_1(E)-c_1(s)a_3(E).
\]
Every excited energy satisfies \(E\ge4\pi\). Its density falls fast enough near \(u=0\) that \(a_2(E)/a_1(E)\le1/1600\). The radial investigation's saved coefficient enclosures give \(c_3(s)/c_2(s)>1/700\) along the entire filter path. Thus \(c_3(s)a_1(E)\) alone exceeds the direct gain \(2c_2(s)a_2(E)\). Every excited level lowers the overlap at every setting. Integrating the signed response gives the bound
\[
 0<\frac{D_2(0)-D_2(1)}{D_2(0)}<10^{-4},\qquad D_2(0)>0 .
\]
The upper bound is relative to the full-half-line first-mode overlap. The compact first-mode enclosures supply inputs to the proof. The result describes the direction and magnitude of the change in a case where canonical positivity was already known. [Signed comparison and proof](../../10_radial_green_determinants/brainstorm/notes/03_SPECTRAL_FILTER_AND_TWO_ORBITAL_EXCHANGE_20261104.md) · [Saved rational enclosures](../../10_radial_green_determinants/numerics/RGD_E02_R2_NEXT_ORDER_EXISTING_DATA_20261104.json)

**Three orbitals.** At high energy the density concentrates near \(u=0\), where the lowest moment in the block dominates. Its coefficient \(c_1\) occurs only at the bottom left. For \(q=3\) the cofactor there gives
\[
 \lim_{E\to\infty}\frac{\chi_3(E;s)}{a_1(E)}
   =c_4(s)^2-c_3(s)c_5(s)>0 .
\]
The strict sign follows from the same saved enclosures. Thus sufficiently high levels raise the three-orbital overlap at each fixed \(s\). At two orbitals the corresponding cofactor was \(-c_3(s)\). Adding a third orbital changes which cofactor receives the dominant contribution from high energy. Its sign reverses even though the spectral density still concentrates near the same endpoint. The sign and magnitude of the **complete** three-orbital change, including the lowest excited levels, remain open in the originating derivation. [Three-orbital calculation](../../10_radial_green_determinants/brainstorm/notes/03_SPECTRAL_FILTER_AND_TWO_ORBITAL_EXCHANGE_20261104.md)

## Scope and relation to Mellin curvature

At general fixed \(q\) the bottom-left cofactor is \((-1)^{q-1}D_{q-1,q+1}(c(s))\), where \(D_{r,k}(c)=\det[c_{k+j-i}]_{0\le i,j<r}\). Its sign is a separate mathematical input. Even when it has a strict sign, it describes a high-energy limit at that order. A growing-order result would require control of the whole response relative to a positive reference overlap. The parent Mellin-curvature question also compares neighboring coefficient shifts \(k-1,k,k+1\) at a fixed order. The diagonal filter results leave that comparison open. [Parent formulation](../../README.md) · [Original discussion of the diagonal obstruction](../../10_radial_green_determinants/brainstorm/notes/01_RESULTS_AND_NEXT_DIRECTION_20261104.md)

The evidence has two layers. The radial investigation supplies recorded finite enclosures with its documented internal checks. At plan issuance the energy-filter deductions had proof-author checks only. [MC11-E01 r1](../reviews/01_MC11_E01_R1_STARTING_RESULTS_ASSESSMENT_20261104.md), completed on 4 November 2026 by Sol/ultra, now accepts the specified deductions without correction, with exact rational replay and the inherited numerical premises. This is internal different-model assessment of the originating derivation, not specialist review or new quadrature. The gain is a fixed-order signed estimate. The two-orbital proof uses a spectral gap and enclosed coefficient ratios. Any source satisfying the same inequalities would share its conclusion. Reweighting the squares requires checking those bounds afresh. An Euler-factor modification changes the source, while the reflected-shape and positive-primitive controls lack the canonical square expansion. Likewise, the radial manuscript's algebraic negative-diagonal examples carry no established realization by this heat trace. These distinctions delimit the evidence for the physical interpretation and for any application to RH. [Portfolio results](../../../../../../../result-summaries/README.md) · [Theta identities](../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md) · [Collision controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md) · [Patterns to avoid](../../../../../../../avoid/README.md) · [Re-realizations in new coordinates](../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md)

## Research plan

**Revision 1 · 4 November 2026.** The first scientific objective is to determine **which part of the excited spectrum accounts for the change in the three-orbital overlap**. Its high-energy response is positive at each fixed filter setting, but that limit gives neither the sign of the first excited level nor the size of the effect of all levels together. A signed bound on the change from ground mode to full theta would answer a different question from verifying positivity of the endpoint itself.

The table gives the dependencies for this revision. The [progress file](../research-progress/01_ENERGY_FILTERED_THETA_OVERLAPS_RESEARCH_PROGRESS_20261104.md) owns current status, the frozen inputs for the first assessment, and the continuation prompt. Edward Baker selects the actual model, effort and chat. [Repository model workflow](../../../../../../../GPT_RESEARCH_MODEL_WORKFLOW.md)

| Task | Type and recommended model | Prerequisite and output |
| --- | --- | --- |
| MC11-B00 · Choose the comparison | B — Astra, to select the physical question and evidence needed to decide it | The originating notes supply the alternatives. This revision records the decision and execution limits. |
| MC11-E01 · Assess the starting results | E — Sol, to check fixed proofs and rational bounds | Start from the frozen notes and saved moments. Return a separate assessment of the two-orbital result and three-orbital cofactor. |
| MC11-E02 · Separate two contributions at \(q=3\) | E — Sol, to propagate existing enclosures through a specified \(3\times3\) determinant | Uses the premises accepted by E01. Return signed bounds from existing data and identify any term that prevents a decision. |
| MC11-E03 · Enclose the first excited level | E — Sol, to acquire five specified moments by validated quadrature | Conditional on E02 isolating this uncertainty. Return one bounded acquisition and propagate it through the E02 calculation. |
| MC11-E04 · Assess the three-orbital return | E — Sol, to replay a finished calculation against fixed obligations | Uses E02, or E03 if invoked. Return a claim-by-claim assessment, including the scope of an inconclusive interval. |
| MC11-B01 · Decide what can be carried to other orders | B — Astra, to identify a transferable estimate or diagnose a missing premise | Normally follows E04. A substantive failure can bring this decision forward for the affected route. Return one bounded execution contract or a reason to stop. |

### MC11-E01

**Default first task.** Check the filter and the identification of the unnormalized diagonal overlap, the endpoint cancellation for the indices used, and the propagation of the original coefficient enclosures along the entire path. Re-derive the two-orbital level sign and fractional loss \(<10^{-4}\). For the three-orbital claim, check the sign and indexing of the corner cofactor, the energy limit at fixed \(s\), and the use of the saved bounds through moment five. The acceptance test is a separate disposition for each of these claims, with its premises and arithmetic evidence. Use one proof pass, exact rational replay and at most one local correction. Record a substantive gap for B01 and identify which later claims depend on it. This review reuses the existing integration record. [Starting derivation](../../10_radial_green_determinants/brainstorm/notes/03_SPECTRAL_FILTER_AND_TWO_ORBITAL_EXCHANGE_20261104.md) · [Exact input record](../../10_radial_green_determinants/numerics/RGD_E02_R2_NEXT_ORDER_EXISTING_DATA_20261104.json)

### MC11-E02

Keep the physical path \(w_1=1,\ w_{n\ge2}=s,\ 0\le s\le1\), the full half-line, and the unnormalized \(D_3(s)\). Split the response into the first excited level and all higher levels **along this same path**. Both contributions then include the effect that the other levels have on the prepared states:
\[
 L_2=\int_0^1\chi_3(4\pi;s)\,ds,\qquad
 L_{\ge3}=\int_0^1\sum_{n\ge3}\chi_3(E_n;s)\,ds,\qquad
 \Delta_3=D_3(1)-D_3(0)=L_2+L_{\ge3}.
\]
Collect the cofactors multiplying each of \(a_1,\ldots,a_5\) before taking bounds. Denote the sum of cofactors for moment order \(j\) by \(G_j(s)\); then \(L_2=\sum_{j=1}^5 a_j(4\pi)\int_0^1G_j(s)\,ds\), and the same five integrals weight the full higher-level group. Each cofactor is quadratic or lower in \(s\), since every entry is affine. Integrate those polynomials exactly, retaining the same ground and tail moments throughout. Cross-check their sum against the direct expansion of the cubic endpoint difference. Use the saved coefficient boxes, the single-mode logarithmic slope bound and the Green exponential tail bound, with the omitted sum starting at \(n=3\). One calculation with exact or outward-rounded bounds and one regrouping are allowed. Use only order three, the five moments and these two spectral groups.

Return intervals or analytic bounds for \(L_2,L_{\ge3},\Delta_3\), including the error from the entire infinite tail. State separately which signs are determined, and whether the two groups reinforce or oppose each other. Report a fractional effect only if a strict lower bound for \(D_3(0)>0\) is supplied. A signed net effect can be useful even when one contribution straddles zero. A remaining interval containing zero completes the attempt if the return identifies the coefficient, level or lost correlation responsible. If the \(n=2\) moment bounds alone limit the result, specify the needed widths and demonstrate that improving those inputs could decide it before invoking E03. Any different scientific target or missing structural inequality goes to B01.

### MC11-E03

Use this conditional acquisition only for the deficit documented by E02. Enclose \(a_j(4\pi)\), \(1\le j\le5\), on the full half-line. Adapt the existing validated integration on \([0,2]\), with a rigorous \(n=2\) spatial tail beyond 2. Retain E02's separate \(n\ge3\) bound. Allow one acquisition at 384-bit precision and one subdivision refinement of the same five integrals. Record the input versions, quadrature and rounding allowances, both tails and achieved widths. Replay E02's signed calculation with the refined inputs. Return the resulting enclosures, even if they still contain zero. Submit a finished enclosure, including one that straddles zero, to E04 for assessment before B01 interprets it. A substantive change of premise can go to B01 immediately. [Existing finite integration](../../10_radial_green_determinants/numerics/rgd_e02_two_case_certificate.py) · [Large-files policy](../../../../../../../LARGE_FILES.md)

### MC11-E04

Review one three-orbital return in one pass with at most one local correction. Reconstruct the cofactor and endpoint calculations, check the signs, normalizations and shared \(s\) path, and reconcile the errors from the spatial tail, omitted energies and any numerical acquisition. Check that switching the sign of an exchange term breaks the algebraic cross-check. Record a disposition for each reported sign and magnitude; preserve a failed estimate as evidence about its stated method. Attribute a pointwise sign to a level only when the argument covers the claimed filter settings. Substantive discrepancies go to B01.

### MC11-B01

Use the assessed signed contributions to decide whether this filter reveals a mechanism with scope beyond \(q=3\). If the lowest level and tail compete, ask what source information controls their **sum**. If they reinforce, ask which estimates on the leading and remaining cofactors would persist as \(q\) varies. If this task is reached through a failed assessment, address the named premise first. Compare at most two analytical routes on paper, consuming the existing results and the [collision controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md). Distinguish properties shared by reweighted spectra from information supplied by the complete unit-weight theta source. Any proposed use for Mellin curvature must also account for neighboring coefficient shifts.

Close with either one precise question and proof or measurement contract for **MC11-E05 — Sol**, or a scoped reason to stop. E05 is reserved until B01 supplies its source, observation, finite limits and acceptance test. For a growing determinant, name the cofactor sum and the dimension-dependent margin that would control it. [Separate bounds and cancellation](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) · [Numerics before a question](../../../../../../../avoid/10_numerics_ahead_of_the_question.md)

## E01 assessment return · 4 November 2026

Prepared for Edward Baker with substantial LLM assistance, actual **gpt-6.1-sol / ultra**. E01 r1 is complete: all specified claims accepted, no correction, all frozen hashes matched. The [research note](../notes/01_MC11_E01_R1_PROOF_AND_RATIONAL_REPLAY_20261104.md) and [exact replay](../numerics/MC11_E01_R1_EXACT_REPLAY_20261104.json) record the evidence. The default next task recorded at the E01 return was **[E] MC11-E02 — Sol**, following the unchanged revision-1 contract; the E02 return below updates readiness. Its common-path contributions and net three-orbital sign remain open. See the [live register](../research-progress/01_ENERGY_FILTERED_THETA_OVERLAPS_RESEARCH_PROGRESS_20261104.md) and [continuation/model-change packet](../research-progress/handoffs/01_MC11_E01_RETURN_AND_E02_MODEL_CONTINUATION_20261104.md).

## E02 bounded return · 4 November 2026

Prepared for Edward Baker with substantial LLM assistance, actual **gpt-6.1-sol / ultra**. [Note02](../notes/02_MC11_E02_R1_COMMON_PATH_SPECTRAL_SPLIT_20261104.md) returns the fixed common-path spectral split using existing inputs and no quadrature. Every \(n\ge3\) level raises the three-orbital overlap for all \(s\in[0,1]\); the complete higher group satisfies \(0<L_{\ge3}<5.402\times10^{-40}\). The first-excited and net intervals still contain zero, so reinforcement or opposition is unresolved. A strict existing-data lower bound for \(D_3(0)\) licenses the returned fractional interval.

E02 is complete as a bounded execution return, with E04 assessment pending. Its sensitivity calculation and retained-bound-set examples meet the conditional E03 usefulness gate without forecasting the actual sign. **Next: [E] MC11-E03 — Sol**, only the five first-excited moments and common-path replay within the existing acquisition cap. The [live register](../research-progress/01_ENERGY_FILTERED_THETA_OVERLAPS_RESEARCH_PROGRESS_20261104.md) owns readiness; the [continuation/model-change packet](../research-progress/handoffs/02_MC11_E02_RETURN_AND_E03_MODEL_CONTINUATION_20261104.md) supplies widths, limits and the prompt. E04 follows a finished return, including an inconclusive one.

## E03 acquisition return · 4 November 2026

Prepared for Edward Baker with substantial LLM assistance, actual **gpt-6.1-sol / ultra**. [Note03](../notes/03_MC11_E03_R1_FIRST_EXCITED_ACQUISITION_AND_RETURN_20261104.md) and its [record](../numerics/MC11_E03_R1_FIRST_EXCITED_ACQUISITION_20261104.json) retain the five validated first-excited source moments and exact common-path replay. One 384-bit acquisition met all five goals, with the explicit \(n=2\) source spatial exterior and unchanged complete \(n\ge3\) energy allowance. No subdivision refinement was used.

Both \(L_2\) and \(L_{\ge3}\) are positive. The total satisfies \(2.22665020\times10^{-33}<\Delta_3<2.22665075\times10^{-33}\), and its fractional increase is between \(1.34020588635\times10^{-5}\) and \(1.34020621148\times10^{-5}\), with a positive full-half-line ground determinant floor. The first excited level accounts for more than 99.99997573% of the gain. Whole-path intervals now cover every excited level's positive three-orbital response. These are validated/proof-author results pending E04, with no growing-order or neighboring-shift conclusion.

**Next: [E] MC11-E04 — Sol**, one-pass assessment of the fixed finished return, using the [continuation/model-change packet](../research-progress/handoffs/03_MC11_E03_RETURN_AND_E04_MODEL_CONTINUATION_20261104.md) and [frozen input versions](../research-progress/handoffs/03_MC11_E04_R1_INPUT_VERSIONS_20261104.json). The [live register](../research-progress/01_ENERGY_FILTERED_THETA_OVERLAPS_RESEARCH_PROGRESS_20261104.md) owns status. B01 interprets the assessed return or addresses a named structural gap; it has not begun.

## E04 assessed return · 4 November 2026

Prepared for Edward Baker with substantial LLM assistance, actual **gpt-6.1-sol / ultra**. [Review02](../reviews/02_MC11_E04_R1_THREE_ORBITAL_RETURN_ASSESSMENT_20261104.md) accepts the finished E02/E03 common-path calculation within its frozen scope, without correction. All 18 frozen inputs matched. The source/integration/tail proofs, complete errors, independent cofactor reconstruction, genuine determinant exchange-sign mutation, pointwise signs and reported magnitudes pass. No quadrature was repeated.

Both groups reinforce; every excited level raises the order-three unnormalized overlap throughout the filter path, the fractional net increase is about \(1.340206\times10^{-5}\), and the first excited level supplies more than 99.99997573% of that gain. [Note04](../notes/04_MC11_E04_R1_RECONSTRUCTION_AND_ERROR_ACCOUNTING_20261104.md) and the [exact review record](../numerics/MC11_E04_R1_ASSESSMENT_REPLAY_20261104.json) retain the evidence. This remains same-assistant/same-model internal assessment with shared numerical premises; no specialist independence or growing-order/neighboring-shift conclusion is implied.

**Next: [B] MC11-B01 — Astra**, under the unchanged at-most-two-route analytical contract, with readiness owned by the [sole register](../research-progress/01_ENERGY_FILTERED_THETA_OVERLAPS_RESEARCH_PROGRESS_20261104.md). The [continuation/model-change packet](../research-progress/handoffs/04_MC11_E04_RETURN_AND_B01_MODEL_CONTINUATION_20261104.md) identifies the unresolved cofactor transfer question and the required E05 contract or scoped stop. B01 and E05 have not begun.

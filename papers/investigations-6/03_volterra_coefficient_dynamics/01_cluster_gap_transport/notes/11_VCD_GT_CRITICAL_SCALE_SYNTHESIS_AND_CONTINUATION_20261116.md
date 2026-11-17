# Critical-scale joint error — synthesis and continuation

16 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex LLM assistance, chat0002 continuation. Lead actual recorded model/effort unavailable. Proof and assessment helpers explicitly dispatched **gpt-6.1-sol / ultra**; no separate backend attestation or specialist review.

**Research round complete and internally assessed within scope.** [E05 r4](../reviews/06_VCD_GT_CRITICAL_SCALE_ASSESSMENT_20261116.md) accepted the proofs and this synthesis after bounded comparator/source-scope clarification and recheck, including the combined shorter-interval corollary. This status/navigation update leaves the assessed mathematical text unchanged. This round follows [B03 Decision03](../brainstorm/notes/03_VCD_GT_B03_CRITICAL_SCALE_DECISION_20261116.md). It quantifies the correlated terms left open by [synthesis07](07_VCD_GT_RESEARCH_SYNTHESIS_20261116.md), conditional on the same fixed isolated double event. The canonical signed gap estimate remains unproved.

| Next task | Type and recommendation | Readiness and required output |
| --- | --- | --- |
| VCD-GT-B04, gated default | B; Astra/ultra, selecting information not supplied by the generic profiles | Reserved, unissued; needs a concrete additional complete-source inequality or an unresolved canonical tube with a specified matched-comparison question |
| VCD-GT-E04 / E06 | E; Sol6.1/ultra, fixed acquisition or composition | Still unissued: no selected finite diagnostic inputs or independently acquired positive margin |

Read [result summaries](../../../../../result-summaries/README.md), specifically [controls12](../../../../../result-summaries/12_collision_controls_and_screening.md), [local geometry13](../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md) and [approximation18](../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md); also [avoid](../../../../../avoid/README.md), especially [classification01](../../../../../avoid/01_restating_the_target.md), [control premises02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md), [scope07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md), [joint bounds12](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) and [volume20](../../../../../avoid/20_volume_without_a_gain.md). This is a quantitative conditional diagnostic, not an RH-equivalent criterion supported by checks.

## 1. What the new scale resolves

Assume, rather than assert, one complete physical-source double event \((T,a)\), \(0<T<1/2\), \(a\ne0\), with \(F_T(z)=(z-a)^2A_T(z)\), \(A_T(a)\ne0\), and Note06's fixed local two-zero tube. Set
\[
t_N(s)=T+s/N^2,\qquad e_N(t)=D(t)-D_N(t),\qquad e_{0,N}=e_N(T).
\]
All limits below are uniform for \(s\) in each fixed compact real interval. They are additive limits after normalization by \(e_{0,N}\), which is eventually nonzero; there is no division by a profile at its zeros.

Define the entire real functions
\[
 C(s)=\sum_{m\ge0}\frac{(8s/a^2)^m}{(2m)!},\quad
 B(s)=\frac4{a^2}\int_0^s C(q)\,dq,\quad
 H(s)=C(s)-1-B(s).
\]
For positive \(s\), \(C(s)=\cosh u\), \(B(s)=u\sinh u-\cosh u+1\), with \(u=\sqrt{8s}/|a|\). On the negative side these continue as cosine expressions.

[Note09](09_VCD_GT_E03_CRITICAL_SCALE_COMPENSATION_20261116.md) derives from the actual signed quadrature law and fixed-contour first variation
\[
 \frac{e_N(t_N(s))}{e_{0,N}}\longrightarrow C(s),\qquad
 \frac{r_N(t_N(s))}{N^2e_{0,N}}\longrightarrow-\frac4{a^2}C(s).
\]
The earlier \(o(N^{-2})\) calculation froze the root evaluation. Here root offsets of order \(1/N\) alter the leading monomial by order one, giving the explicit hyperbolic/cosine profile.

With \(v=t_N(s)\), \(W_N(t)=\exp(4\int_t^vK_N)\), and oriented integrals when \(s<0\), put
\[
 \mathfrak R_N=\int_T^vW_Nr_N,\qquad
 \mathfrak H_N=4\int_T^vW_N(K-K_N)D.
\]
Then \(\mathfrak R_N/e_{0,N}\to-B(s)\) and
\(\mathfrak H_N/e_{0,N}\to H(s)\). The exact combination is
\[
 e_N(v)+\mathfrak R_N-\mathfrak H_N=W_N(T)e_{0,N},
 \qquad C(s)-B(s)-H(s)=1.
\]
The identity was already known; the individual uniform normalized profiles and the paid remainder bounds are the new quantitative content.

## 2. Direct drift check and size of cancellation

[Note10](10_VCD_GT_E07_DEFLATION_KERNEL_20261116.md) independently differentiates the deflated unit of \(x^2-d^2-\varepsilon e^{2x/a}\), including the motion of its pair polynomial. Its removable kernel is
\[
 \kappa_a(s)=\frac{C'(s)-(4/a^2)C(s)}{8s},
 \qquad \kappa_a(0)=-\frac4{3a^4}.
\]
After paying the scaled-field convergence and quadratic functional remainder, it gives
\[
 \frac{K(t_N(s))-K_N(t_N(s))}{N^4e_{0,N}}\longrightarrow\kappa_a(s).
\]
The auxiliary fixed circle in \(x=N(z-a)\) is a proof device selecting the same stipulated pair; it acquires no new canonical contour geometry and defines no changing-contour transport algorithm.

The two proofs also close Note09's remaining relative drift question on shorter intervals. For any nonzero real sequence \(s_N\to0\),
\[
 \frac{\mathfrak H_N(s_N)}{e_{0,N}}
 \sim-\frac{16s_N^2}{3a^4},\qquad
 \frac{\mathfrak H_N(s_N)}{\mathfrak R_N(s_N)}
 \sim\frac{4s_N}{3a^2}.
\]
Indeed, for \(q\) between 0 and \(s_N\), the physical law gives
\(D(T+q/N^2)=2q/N^2+O(q^2/N^4)\), while
\(W_N=1+O(|s_N|/N^2)\). Note10's uniformly additive kernel error makes the normalized drift integrand
\(8q\kappa_a(0)+q\,o(1)\). Its oriented integral is
\(4\kappa_a(0)s_N^2+o(s_N^2)\) in either direction; Note09 supplies
\(\mathfrak R_N/e_{0,N}\sim-4s_N/a^2\). No time derivative of a scalar phase bound or nonvanishing-profile quotient is used.

**At the critical scale the transfer term is generally of leading order.** Its signed contribution cancels with the incoming error and residual. For \(s>0\), \(H(s)<0\) and the sum of the absolute limiting contributions is \(1+2B(s)\), whereas their signed combination is exactly 1. At \(s=-a^2\pi^2/8\), the three profiles are \(C=-1\), \(B=2\), \(H=-4\): the separate absolute total is 7 and the signed combination remains 1. These are analytical constants, not numerical certificates. At zeros of \(B\), the normalized residual limit is zero; no nonzero relative asymptotic follows there.

## 3. Matched comparison and boundary of the result

The exact residual and \(G_{N+1}\) both use the first \(N\) Jacobi link indices. This does not assert equal whole-slab acquisition, evaluation or source-oracle costs: the direct endpoint model needs the corresponding snapshot and receives all shared measurements. No coefficient family or physical data was acquired here. For the exact unweighted \(T\)-target correction, divide by \(W_N(T)>0\); Note06's adjacent-error asymptotic then gives
\[
 \frac{|e_N(v)+\mathfrak R_N-\mathfrak H_N|}
 {W_N(T)\,|D(T)-D_{N+1}(T)|}
 \sim\frac{(2N+1)(2N+2)}{\beta_{N+1}(T)a^2}.
\]
The omitted positive \(\beta_{N+1}\) stays explicit; no lower bound is assumed. This compares actual errors at the stipulated event, not all transport estimators. Keeping correlations removes the artificial separate-term loss, but this degree-\(N\) joint identity still returns the degree-\(N\) endpoint error. It supplies no improvement over the next head in this same-coefficient, same-target error comparison. The original weighted comparison has the same asymptotic because \(W_N(T)=1+O(N^{-2})\) on each fixed scaled interval.

The weighted-square event controls share the stated physical-source and quantitative error assumptions, so these same local profiles apply to them. Their missing equal theta coefficients/full reflection are unused in the proof; their events are not finite all-real thresholds. The exact quadratic exhausts its gap but has no infinite positive Jacobi source. Euler/reflected/smooth/primitive/atomic/endpoint/changed-observation controls retain the explicit failed, untested or out-of-domain premises in Notes06/09/10. No control certificate was rerun. This calculation does not distinguish theta from every colliding source, assert a theta event, or exclude one. The inherited deflated-jet input in [synthesis07 §4](07_VCD_GT_RESEARCH_SYNTHESIS_20261116.md#4-controls-and-source-scope) retains its all-real theta-slice, T>0 and a>=20 hypotheses; its event value alone leaves the integrated cost unpaid.

## 4. Current boundary and continuation contract

The monomial correction was disposed using the existing parent E24 comparison; it was not re-proved as a new result. The generic critical-scale joint question is now answered with the stated internal assessment. Further repetitions of its identity, longer profile tables or wider numerical scans would add no canonical input.

B04 is reserved for a concrete new complete-source correlation not already supplied by the generic quadrature laws, or a specified unresolved canonical tube whose acquisition has a precise gain question. It must compare at most two proposals, retain all signed terms, name the control premise it uses, and give both methods every acquired coefficient/source measurement. Only then issue a fixed E proof or diagnostic. No ready numerical/descent successor exists: count, modulus, buffer, incoming gap and useful full signed margin remain unacquired. Parent B07/E25 and the degree-contraction/multiscale siblings are unchanged.

The [sole register](../research-progress/01_VCD_GT_RESEARCH_PROGRESS_20261116.md) owns task status. Existing proof/phase literature is reused at its recorded scope; this round introduces no new external theorem or fresh literature audit. Review is internal with shared premises, not specialist independence.

To resume: read this note, Notes09/10, their assessment, the register and root workflows. Activate B04 only after recording its concrete new mathematical seed and comparator; do not reissue the critical-scale calculation as a gain. Continue any justified fixed follow-through through proof, controls, comparison and separate assessment in the same session. Refresh the registered chat at turn start and arm the actual exact-turn final capture as the last tool action. Never reuse the preceding turn id or prewrite a final response.


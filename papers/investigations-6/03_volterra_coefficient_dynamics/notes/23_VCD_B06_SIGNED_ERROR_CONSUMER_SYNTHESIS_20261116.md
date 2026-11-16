# B06 — a signed consumer for the complete E15 error

16 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex LLM assistance. Lead actual model/effort unavailable in accessible runtime/archive configurations. Proof/assessment helpers explicitly dispatched **gpt-6.1-sol / ultra**, with no separate backend attestation. Chat0003, third research turn.

**Research synthesis; [E23 accepted the three proofs and revised synthesis within their stated scopes](../reviews/08_VCD_E23_SIGNED_ERROR_CONSUMER_ASSESSMENT_20261116.md).** One synthesis response clarified the value-plane contour condition and disk wording; no proof correction was required. This is separate internal shared-model/shared-premise assessment, not specialist independence. This status header is the only subsequent change to the assessed synthesis. [Decision12](../brainstorm/notes/12_VCD_B06_ERROR_PHASE_CONSUMER_DECISION_20261116.md) selects the phase of the complete quadrature error. [Decision13](../brainstorm/notes/13_VCD_B06_PREFIX_COST_AND_DIRECTED_ERROR_DECISION_20261116.md) then compares the coefficient cost and selects a directed positive-amplitude enclosure at the available prefix. This supplies a quantified signed consumer of E15 specialized to the physical tail against the bare head. It does not establish zero confinement or an invariant degree update.

Read the [result index](../../../../result-summaries/README.md), [cluster18](../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md), [control catalog12](../../../../result-summaries/12_collision_controls_and_screening.md), [avoid index](../../../../avoid/README.md), [classification01](../../../../avoid/01_restating_the_target.md), [scope07](../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [separate-bounds12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md). The phase theorem is an intermediate estimate, judged by its rate and paid domain. The contour consumer is conditional on a concrete finite-model margin; no existence assertion about exhausting successful contours is offered as evidence. The old unspecified shrinking-strip target retains its classification in overview02.

## 1. The complete transport error has a concentrated phase factor

At time zero retain the complete \(d\mu=\Phi\,du/Z\), \(F(z)=\int e^{izu}d\mu\), and physical Jacobi prefix \(J_N\). Put
\[
 G_N(z)=e_0^{\mathsf T}e^{izJ_N}e_0,\qquad
 h_N^*=\prod_{j=1}^N\beta_j,\qquad
 L_N(z)=(-1)^N h_N^*\frac{z^{2N}}{(2N)!}.
\]
[E21 / Note20](20_VCD_E21_COMPLETE_ERROR_PROBABILITY_LAW_20261116.md) proves, on all of \(\mathbb C\),
\[
 F-G_N=L_N E_N,\qquad E_N(z)=\mathbb E e^{izX_N}.                 \tag{1}
\]
Here \(U\) has law \(P_N^2d\mu/h_N^*\); independently, \(S\) is uniform probability on the simplex with \(2N+1\) coordinates, and
\[
 X_N=S_0U+\sum_{j=1}^N(S_{j,1}+S_{j,2})x_j,
\]
where \(x_j\) are the Gauss nodes. The auxiliary law is symmetric. It represents the aggregate error, while the physical source and Fourier observation stay unchanged.

The confluent interpolation formula integrates to (1) because Gaussian quadrature is exact through degree \(2N-1\). All repeated-node factors and the simplex volume \(1/(2N)!\) are paid. This is the same left side as [E15](13_VCD_E15_SHARED_MEMORY_EQUIVALENCE_20261116.md) with physical \(k_N\) and \(\ell=0\); hence (1) represents its entire signed triple convolution. It is not an arbitrary-kernel factorization. The underlying interpolation formulas are classical, with checked passages in [reference04](../references/04_QUADRATURE_ERROR_PHASE_PASSAGES_20261116.md); no novelty claim is made for them or for a probability interpretation by itself.

Writing \(M=2N+1\), \(m_2=\beta_N+\beta_{N+1}\), \(S_2=\operatorname{tr}J_N^2\), E21 gives
\[
 \sigma_N^2:=\mathbb E X_N^2=\frac{2(m_2+S_2)}{M(M+1)}.
\]
Its exact fourth moment is
\[
 \mathbb E X_N^4=
 \frac{24m_4+24m_2S_2+12S_2^2+12S_4}{M(M+1)(M+2)(M+3)},
\]
with \(S_4=\operatorname{tr}J_N^4\) and
\(m_4=\beta_N\beta_{N-1}+(\beta_N+\beta_{N+1})^2+\beta_{N+1}\beta_{N+2}\).

[E22 / Note21](21_VCD_E22_QUANTITATIVE_ERROR_PHASE_20261116.md), whose return pins E21, uses the full inherited source estimate
\(\mathbb E_{\nu_N}\cosh(4U)\le2N+12\), as well as the coefficient envelope. A beta-distribution split separates the unbounded source coordinate from a symmetric Dirichlet average of the bounded nodes. Its complete exponential-weight payment produces explicit degree-only quantities \(\mathcal A_N(Y),\mathcal Q_N\) in Note21 equations (6)–(7), giving
\[
 \boxed{|E_N(z)-1|\le\epsilon_N(|z|,Y)
 :=\frac{|z|^2}{2}\sqrt{2\mathcal A_N(Y)\mathcal Q_N}
 =O\!\left(\frac{|z|^2\log^2(N+1)}{N}\right),\quad |\Im z|\le Y\le1.} \tag{2}
\]
The constant can be common to \(0\le Y\le1\); the estimate permits unrestricted real part, though it is useful for phase when \(\epsilon_N<1\). In particular \(E_N\to1\) uniformly in the strip on \(|z|=o(\sqrt N/\log(N+1))\). The proof does not expand an unbounded-source reciprocal series.

On the real axis \(1-x^2\sigma_N^2/2\le E_N(x)\le1\). Therefore the error has strict sign \((-1)^N\) for \(0<|x|<\sqrt{2/\sigma_N^2}\), with an explicit degree-only sufficient interval in Note21. Consecutive even and odd quadratures bracket \(F\) on the common interval. This is signed approximation information, not a count of all real or complex zeros.

Where the explicit budget is less than one, (1)–(2) also show that F-G_N has no zero away from the origin; its zero at the origin has order exactly2N. This is a statement about the approximation error, not about zeros of F.

## 2. The selected consumer uses the known error direction

Suppose the acquired prefix consists of \(\beta_1,\ldots,\beta_{N-1}\), with \(\beta_0=0\). Set
\[
 d_N(z)=(-1)^N z^{2N},\quad
 \alpha_N=\frac{h_N^*}{(2N)!}>0,\quad
 \overline\alpha_N=
 \frac{\prod_{j=1}^{N-1}\beta_j}{(2N)!}
       (B_{N-1}-\beta_{N-1}),\quad
 B_j=\frac{\operatorname{arcosh}^2(2j+12)}{16}.
\]
The adjacent envelope proves \(0<\alpha_N\le\overline\alpha_N\). The upper bound uses no missing link, while (2) uses only the degree. For \(z\ne0\) write \(w_N(z)=G_N(z)/d_N(z)\). Equation (1) becomes
\[
 F(z)/d_N(z)=w_N(z)+\alpha_NE_N(z).                         \tag{3}
\]
[E24 / Note22](22_VCD_E24_DIRECTED_ERROR_AND_PREFIX_COMPARISON_20261116.md) establishes the exact geometry. The uncertainty in the error lies in
\[
 \mathcal U_N(z)=\bigcup_{0\le a\le\overline\alpha_N}
                  \{a(1+\eta):|\eta|\le\epsilon_N(|z|,Y)\}.
                                                               \tag{4}
\]
This is the convex hull of zero and the disk with center \(\overline\alpha_N\) and radius \(\overline\alpha_N\epsilon_N\). It retains a positive amplitude and the known phase \(d_N(z)\); it does not bound the error by an independent disk centered at zero.

Concrete sufficient consumers are:

- \(\operatorname{dist}(-w_N,[0,\overline\alpha_N])>
  \overline\alpha_N\epsilon_N\) excludes an \(F\)-zero at the point. This capsule test is sufficient; the exact union in (4) can give a sharper test.
- If \(\epsilon_N<1\) and \(\Re w_N\ge0\), then \(F\ne0\), since the actual amplitude is strictly positive and \(\Re E_N>0\). This also works if \(G_N=0\). At \(z=0\), use \(F(0)=1\) directly.
- An \(F\)-zero in the \(\epsilon_N<1\) range requires \(-w_N\ne0\), \(|\arg(-w_N)|\le\arcsin\epsilon_N\), and \(|w_N|\le\overline\alpha_N(1+\epsilon_N)\). This is a necessary localized sector condition, not evidence that the condition is ever attained.
- On a simple closed contour avoiding zero and lying in the paid strip, separation of \(-w_N\) from the **closed** set (4) along the entire boundary gives equal interior zero counts for \(F\) and \(G_N\), with multiplicities. The straight homotopy errors remain in (4). A pointwise exclusion by itself does not supply such a contour or its model count.

The reference direction is explicit in the degree and observation point. It uses no phase of the unknown full \(F\). B05's failure of fixed half-planes for a different normalization and an all-height comparison does not contradict this local, degree-dependent statement. Neither does it imply that these new margins hold everywhere needed.

## 3. Why a monomial correction is not the default implementation

With \(\beta_N\) also acquired, \(G_N+L_N\) has a paid disk of radius \(|L_N|\epsilon_N\). E22 proves that conditional test. But the same coefficients already specify \(G_{N+1}\). E24 gives
\[
 \frac{L_{N+1}(z)}{L_N(z)}=
 -\frac{\beta_{N+1}z^2}{(2N+1)(2N+2)}.
\]
On a bounded-phase range the next physical head's error allowance, relative to \(|L_N|\), is \(O(|z|^2\log^2N/N^2)\). The plain monomial-correction allowance from (2) is of order \(|z|^2\log^2N/N\). The next unknown link is bounded using the envelope; it is not needed to evaluate \(G_{N+1}\).

There is also an actual local comparison:
\[
 \lim_{z\to0,\ z\ne0}
 \frac{F(z)-G_N(z)-L_N(z)}{F(z)-G_{N+1}(z)}
 =\frac{\beta_N+\beta_{N+1}+2\sum_{j=1}^{N-1}\beta_j}
        {\beta_{N+1}}>1.                                      \tag{5}
\]
This proves no all-region ordering of actual errors. It does prevent presenting the monomial correction as a better model at equal coefficient cost without a further geometric advantage. The selected default is the directed enclosure at the available physical prefix; use the next physical head when the next link is acquired.

E22 also corrects one dispatch-time disk comparison: its shifted disk lies inside the loose bare disk of radius \(|L_N|(1+\epsilon_N)\). Independently paid sharper bare disks, including radius \(|L_N|\) on the real axis, can be nonnested with it. The frozen request is preserved, with the correction disclosed in its return.

## 4. Controls, unresolved obstacle and useful assistance

**The phase budget is proved; a canonical placement of the finite-model margin is not.** The exact error law is generic Gaussian-quadrature structure. The new rate uses the proved cosh/coefficient bounds, which the weighted-square controls also satisfy, including their known nonreal-zero class. E10/E12's small smooth compact multipliers preserve the confinement inequality as well; their zeros remain open. These controls pass the phase estimate on their own sources. Full canonical arithmetic and reflection distinguish the intended source in other statements, but this proof does not consume them to establish the model margin. Note20 §5, Note21 §6 and Note22 give the family-specific pass/fail/untested screens.

The unresolved mathematical input is a quantitative theta-specific oscillation, inter-degree comparison or contour argument proving strict separation of the canonical boundary values \(-G_N(z)/d_N(z)\) from \(\mathcal U_N(z)\) on specified contours covering growing off-real compact sets, together with a justified model zero count. Alternatively, an argument could supply enough real zeros to match a separately controlled complex zero count. Such a lemma needs premises stronger than the shared envelope. Simply assuming the necessary successful margins would restate the zero objective.

There is no missing file, access permission or numerical precision blocking this stage. A particularly useful contribution from Edward would be a candidate structural lemma or reference about the **actual canonical Jacobi readouts**, especially one relating their inter-degree phase or zero geometry to the complete theta score/arithmetic. It need not assert the final zero theorem; a quantitatively testable local or degree-step relation would suffice. A proposed extra approximation norm or generic positivity property would first need to show what it contributes beyond the controls already passing here.

## 5. Disposition

B06 selects a different signed consumer and supplies its phase acquisition, explicit budget, coefficient accounting and pointwise/conditional contour consequences. E21/E22/E24 are the three fixed proof tasks; E23 supplies separate internal assessment. No zero-confinement theorem, successful exhausting contour family, forward degree invariant, numerical campaign, coefficient acquisition, manuscript revision or external publication is claimed. [Register02](../research-progress/02_VCD_TAIL_CLOSURE_INDUCTION_RESEARCH_PROGRESS_20261116.md) owns current status; [continuation03](03_VCD_TAIL_CLOSURE_INDUCTION_CONTINUATION_20261116.md) owns the next conceptual task.

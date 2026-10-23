# Review 12 — microscopic complete reference and analytic correction

**Prepared for:** Edward Baker. **Date:** 23 October 2026. **Reviewer:** gpt-6-astra (Codex), reasoning effort **ultra**. Substantial LLM assistance. This is an independent agent derivation and replay using the same model, not external or cross-model refereeing.

**Disposition:** accepted as a quantitative reference/defect result with its stated restrictions. The bounded Arb algebra replay passed **74 assertions**. It acquires no high-height theta wall floor and is not a finite or global simplicity certificate.

## Imported input and normalization

I checked the primary [Polymath paper](https://arxiv.org/html/1904.12438v2), equation (6), Corollary 6.4 and Proposition 6.6. Its published field estimates apply to real positive time, \(x\ge200\), and \(0\le y\le1\). The correction and explicit constants in (B1) agree with that source. The imported theorem does not supply the proposed whole-wall margin or a complex-time remainder.

The definition of \(M_0\) retains the canonical \(1/8\) normalization of \(H_0=\xi/8\). For the principal logarithm and positive \(v\), substitution directly gives
\[
 M_0(iv)U(v)e^{\pi i/8}
 =-\frac{\sqrt\pi}{8}\sqrt v\,(v+i)e^{-\pi v/4}.
\]
All signs, the factor two in the correction, and the resulting
\(k_N=-(-1)^N\sqrt\pi/4\) check. Three independent Arb evaluations at \(v=100,125,1000\) verify the normalized phase cancellation.

## Analytic continuation and derivative budgets

The published displayed correction involves a real part at real \(x\), and generally is not holomorphic in \(z=x+iy\). The proposed continuation correctly replaces real/imaginary parts by the holomorphic reflected combinations \(C_R,C_I\). It agrees with the published correction on the real axis, but pays a nonzero off-axis difference. This distinction must remain in a manuscript.

The apparent poles of \(C_0\) at \(p=\pm1/2\) are removable, both with value \((1-i)/4\). Differentiating numerator and denominator independently verifies this value; the replay never divides by a zero interval. These are the only denominator zeros in the radius-\(5/4\) disk. The bound (B7) is sound: on its boundary either \(|\Im p|\ge1/8\), or \(1<|\Re p|\le5/4\); these give the claimed lower bounds for \(|\cos\pi p|\). The numerator bounds, maximum principle, and radius-\(1/8\) Cauchy estimate then bound the first two reflected derivatives throughout \(|p|\le9/8\).

For
\[
 V(v)=v^{3/2}C_R(p_N(v))-v^{1/2}C_I(p_N(v)),\qquad
 p_N'(v)=-\frac1{\sqrt{2\pi v}},\quad
 p_N''(v)=-\frac{p_N'(v)}{2v},
\]
I independently differentiated both terms. The coefficients \(5/2\), \(-1/2\), and all powers in (B6) are correct. The elementary majorants in (B8) follow term by term. Their growth is \(V_1=O(X)\) and \(V_2=O(X^{1/2})\), not respectively \(O(X^{1/2})\) and \(O(1)\). The note pays these larger derivative costs.

Writing
\[
 F=k_Ne^{-\pi z/8-\pi^2t/64},\qquad v=z/2+\pi t/8,
 \qquad \widetilde C=FV(v),
\]
separate differentiation yields
\[
 \widetilde C_t+\widetilde C_{zz}=\tfrac14 FV''(v).
\]
The terms multiplying \(V\) and \(V'\) cancel exactly. The replay differentiates the defining correction independently in time and space, and separately differentiates \(V\) in its own variable; it does not differentiate the asserted right-hand side. Three cases include a complex spatial point and an analytic complex-time point. The latter tests the algebra only and does not extend the imported real-time field theorem.

The phase cancellation and the carrier size give
\[
 Q=O_{K,y_0}(X^{-(7+y)/4}),\qquad
 QV_1=O_{K,y_0}(X^{-(3+y)/4}),\qquad
 QV_2=O_{K,y_0}(X^{-(5+y)/4}),
\]
for \(0\le y\le y_0<1\) and bounded \(t\log^2X\). Thus the off-axis analytic continuation cost does not destroy the corrected field rate. The correction defect is smaller than the full finite-sum defect. At \(y=1\), the main-sum logarithm must be retained, as the note states.

## Complete finite sum and quotient consumer

For \(g=A_n(\sigma)e^{t\beta^2/4}\), both spatial carriers obey \(\partial_z^2=-\tfrac14\partial_\sigma^2\). Direct differentiation gives the entire bracket in (A4), including the \(\alpha'\) term present already at \(t=0\). The replay checks this independently for both carriers and \(n=1,3,7\) in three time/space cases. Consequently the full-sum defect allowance (A5), and its \(O_K(X^{-3/4})\) normalized bound at \(y=0\), are justified. Subtracting the analytic correction requires adding its separately computed defect; the note correctly does this.

The normalized quotient identity (A8) cancels the common carrier's second derivative exactly. Its denominator and the bound (A9) are correct. A manuscript must keep the paid common-carrier collar, the lower bound \(m_f>E_0\), and the local normalized derivative ratios. An absolute finite-sum estimate alone does not control these ratios or the logarithmic source quotient.

## Replay and remaining gates

The artifact `hdc14_reference_algebra_checks.py` is stdout-only by default and has a paired JSON receipt. Its **74 passing assertions** cover canonical phase, both removable values, real-axis agreement, explicit \(V'\) and \(V''\), corrected heat-defect cancellation, and the single-term finite-sum defect. All nonzero denominators in these checks are at specified finite points; no theta value, root, or high-height wall is certified.

The useful new result is an explicitly analytic corrected reference, together with finite field-mismatch and heat-defect budgets that remain informative on the microscopic clock. Two essential inputs remain unpaid: the whole-wall margin for that complete reference and, when complex time is used, a complete complex-time error bound. Fixed-\(N\) chart boundaries, reflected-carrier conversion, and the forest/coefficient consumer's own conditioning must also be respected. This audit supports neither density-one simplicity nor an all-height conditional simplicity theorem.


Installed replay: [checker](../numerics/09_check_microscopic_reference_20261023.py) and [74-assertion record](../numerics/09_MICROSCOPIC_REFERENCE_CHECKS_20261023.json). These are algebra controls, not a high-height source certificate.

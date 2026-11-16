# Tail closure: what the first connected research session establishes

16 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex assistance. Lead backend/effort unavailable in accessible runtime/archive configurations. Requested lead Astra/ultra; proof and assessment workers explicitly dispatched **gpt-6.1-sol / ultra**, with no separate backend attestation. Research chat 0002.

**Research synthesis; proof notes completed and accepted without mathematical correction within scope by separate internal assessments.** The complete source and literal Fourier observation are unchanged. No zero-confinement induction is established. This session activated B02, continued through the foundation and residual proofs, tested the candidate on actual controls, revised the conceptual question in B03, and derived both a full-source characterization and a smooth finite-step counterexample.

Read the [result index](../../../../result-summaries/README.md), especially [cluster18](../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md) and [controls12](../../../../result-summaries/12_collision_controls_and_screening.md), and the [avoid index](../../../../avoid/README.md), particularly [target classification01](../../../../avoid/01_restating_the_target.md), [actual control premises02](../../../../avoid/02_shape_only_arguments_and_the_controls.md), and [scoped exclusions07](../../../../avoid/07_scoped_exclusions_read_as_universal.md). Details and exact qualifications belong to the linked sources, not this summary.

## 1. A sharper score approximation, with its limitation

[E06](06_VCD_E06_EXPONENTIAL_SCORE_RESIDUAL_20261116.md) proves, uniformly for \(0\le\lambda\le1/2\),
\[
 V_\lambda'(u)=8\pi\sinh(4u)-2\lambda u+b(u),\qquad \|b\|_\infty\le C_b,
\]
with an explicit convergent series for \(C_b\). Consequently
\[
 \left|8\pi a_n[\sinh(4J)]_{n,n-1}-2\lambda\beta_n-n\right|
 \le \frac{C_b}{4}\operatorname{arcosh}(2n+10).
\]
The score error is absolute \(O(\log n)\), relative \(O(\log n/n)\). In contrast, for any fixed polynomial \(p\) of degree \(d\), the exact remainder contributes
\[
 a_n\langle q_n,(V_\lambda'-p)q_{n-1}\rangle
   =n+O_p(\log^{d+1}(n+2)).
\]
A fixed polynomial cannot leave a negligible relative residual. Growing degree or coefficients are outside that exclusion.

The bounded remainder must still be retained for a zero argument. E06 proves an exact double-convolution boundary identity, but it contains the true tail response. Its bounded remainder correction has norm at most \(2C_b\); this is a paid absolute allowance, not a signed Fourier margin. The validated weighted-square controls also satisfy an \(O(\log n/n)\) relative canonical-score defect with control-dependent constants.

## 2. The finite score data are computable, but do not close the next step

[E05](05_VCD_E05_SOURCE_SCORE_RESIDUAL_20261116.md) establishes the polynomial-vector domains and
\[
 [V'(J)]_{ij}=\langle q_i',q_j\rangle+\langle q_i,q_j'\rangle.
\]
The retained block is therefore computable from the exact retained coefficient head. Its correction relative to \(V'(J_N)\) is not an unknown function merely because it was originally defined through infinite functional calculus. Predictive sign/size bounds and the relation to the tail remain unpaid.

[E08](08_VCD_E08_FULL_SCORE_RIGIDITY_20261116.md) distinguishes full consistency from this finite bookkeeping. For even infinite-support probability measures with the stated weighted exponential integrability, **all** canonical adjacent equations identify the normalized theta measure. This is proved by a triangular conversion to polynomial Stein identities and a distributional first-order equation. It is unconditional source identification, not a zero theorem.

For the Stein defect matrix \(E\), commutation \([J,E]=0\) is generic. At the finite cut,
\[
 [J_N,E_N]=-a_N\mathbf e_{N-1}E_{N,H}
              +a_NE_{H,N}\mathbf e_{N-1}^{\mathsf T}.
\]
The new adjacent defect \(a_NE_{N,N-1}\) cancels. The other boundary components use lower polynomial tests. Thus finite commutation cannot supply the new adjacent equation; describing an entire unknown boundary column obscures this more precise cancellation.

## 3. Two different controls answer two different questions

| Preserved information | Actual conclusion and scope |
| --- | --- |
| **E07:** any prescribed finite time-zero head and canonical-score entries; any finite smoothness order; positive square coefficients; inherited envelope; arbitrarily small bounded own-to-canonical score difference | A nonzero finite square-mode perturbation still has infinitely many nonreal Fourier zeros at every real heat time, by the inherited finite-source theorem. It loses smooth reflection at a later odd endpoint. It has no prescribed compact zero location. |
| **E10:** moments through \(2N\), links through \(a_N\), all lower adjacent defects, retained score correction, smoothness, the full reflection jet and exact real tails; the same envelope and arbitrarily small bounded score difference | A positive smooth compact multiplier perturbation makes the next canonical defect take either sign. It changes the canonical arithmetic square source. **Its Fourier zero locations are not established.** |

Sources: [E07](07_VCD_E07_FINITE_CANONICAL_SCORE_CONTROLS_20261116.md) and [E10](10_VCD_E10_SMOOTH_NEXT_DEFECT_FREEDOM_20261116.md). The preservation lists and conclusions cannot be combined into one stronger control. The first rejects a fixed finite-information global real-zero implication in its stated square-source class. The second rejects an exact next-equation implication from the stated finite data and smooth-source premises. Neither excludes a growing-degree, compact-dependent narrowing-strip induction using further canonical information.

## 4. Analytic foundations and the remaining target

[E04](04_VCD_E04_TAIL_FOUNDATIONS_20261116.md) checks memory signs, tail indices, the Laplace/resolvent conversion, entire continuation on each fixed polynomial vector, and locally uniform complex convergence of bare quadrature. It also proves that actual theta has
\(\sup_N k_N(iy)=\infty\) for every fixed nonzero real \(y\): a complex bound uniform over unscaled moving tail sites is unavailable.

The unspecified shrinking-strip statement after compact convergence remains the already classified RH-equivalent target. No finite numerical check is used to support it. The new contributions are the explicit score estimate, source characterization, and precise failures of the tested finite closure mechanisms.

**Remaining premises:** a noncircular quantitative restriction from the complete canonical source; its preserved tail-to-head update or valid terminal condition; and a signed implication for the literal Fourier observation outside a narrowing strip. No result here supplies the last premise. No coefficient-acquisition scan, enlarged height window, manuscript snapshot or external publication was performed.

## 5. Continued work and provenance

The [live register](../research-progress/02_VCD_TAIL_CLOSURE_INDUCTION_RESEARCH_PROGRESS_20261116.md) owns status; the [canonical continuation](03_VCD_TAIL_CLOSURE_INDUCTION_CONTINUATION_20261116.md) owns the next prompt. Proofs and controls are internally checked by [E09](../reviews/04_VCD_E09_TAIL_SCORE_ASSESSMENT_20261116.md) and [E11](../reviews/05_VCD_E11_SMOOTH_DEFECT_ASSESSMENT_20261116.md) at their actual recorded scopes. They share models/inherited sources and are not independent specialist reviews.

**Next: [B] VCD-B04 — Astra/ultra recommended.** Select a quantitative constraint that retains the exact canonical bounded score remainder jointly with the omitted-tail response, or another explicitly source-distinguishing part of the same chain. Require an actual signed Fourier consumer and test the new premise against both control classes before issuing another E proof. Repeating finite constraints, the leading exponential score alone, or commutator consistency does not address the identified gap. The entire investigation remains open.

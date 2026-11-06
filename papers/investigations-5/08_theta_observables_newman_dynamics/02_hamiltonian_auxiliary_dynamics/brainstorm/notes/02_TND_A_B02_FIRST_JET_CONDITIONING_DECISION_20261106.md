# TND-A-B02: first-jet recovery conditioning decision

6 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**, verified in local turn metadata. Auxiliary chat0003, thread `01a1af80-4c0e-76c3-b030-c92591d2edba`. **B — brainstorm**, plan r1; one target, two analytical approaches, one decision pass; root sole writer, no supporting agents.

**Decision: select a sharp finite-window first-jet recovery benchmark and issue E03 r1.** Its job is to quantify the deterministic accuracy that an auxiliary readout would need to match direct recovery of `(H, s H')`. Classification: **conditioning diagnostic**, not a source-sensitive zero restriction or an RH-equivalent criterion. The route comparison below fixes a short analytical execution; the displayed sharp bounds remain E03 proof targets, not a newly assessed theorem.

| Next task | Type/model and reason | Readiness/dependency | Expected output |
| --- | --- | --- | --- |
| **TND-A-E03 r1 — default next** | **E — Sol**; exact map, norm, error class and elementary proof route fixed | [Request issued][request], [inputs frozen][inputs]; ready for author selection, **unactivated** | Sharp first-jet inverse-error factor on the complete model, matched direct comparison and its precise scope, or an exact failed clause |
| TND-A-E04 | E — Sol; fixed assessment and integration | E03 return | Assess the diagnostic without promoting it to a collision or practical acquisition gain |

The [sole branch register][progress] owns status. [Activation06][activation] records authorization, actual model/effort, unchanged mathematical inputs and E02 output identities. [Return06][return] binds this decision and its packet. Original requests, proofs and assessments remain unchanged.

## 1. Why this one target

[E02][review] accepts the complete conditional response
\[
\mathcal O_{\lambda,\tau}(z)=m_\tau(z)H_\lambda(z),\qquad
m_\tau(z)=q(\tau)e^{-\tau z^2},\qquad
q(\tau)=\frac{Q_1(\pi+4\tau)}{Q_1(\pi)}>0.
\tag{D1}
\]
The inverse factor for the value alone is already known to grow on the real line. What remains useful to quantify is recovery of the **value and derivative together**: the Gaussian also mixes the value into the derivative. This pair is relevant because a multiple zero requires both entries to vanish. Quantifying its recovery cost supplies an explicit accuracy threshold for any later acquisition proposal; it does not supply a positive canonical first-jet margin.

Fix any finite `M,K,T >= 0`, real `|lambda| <= M`, `|k| <= K`, `0 <= tau <= T`, and one finite **fixed** derivative scale `s > 0`. Use the same s and canonical amplitude units on both sides. The real spectral window is the domain of the diagnostic; it does not truncate the physical radial spectrum. Every physical angular level/sign and reference column in E01 remains present in q and the accepted response. The selected order is exactly one k derivative. No growing-order, complex-frequency or asymptotic extension is selected.

The comparison uses the same canonical source information throughout. A bounded error in a computed or supplied pair is a **mathematical hypothesis**. E01/E02 do not produce that error bound, a derivative-measuring device, a stochastic noise law, or equal-cost acquisition. Physical preparation, phase-sensitive readout and gains stay exactly as supplied by B01.

## 2. Approach A: retain the raw pair and its exact inverse

Put
\[
X=\binom{H_\lambda(k)}{sH'_\lambda(k)},\quad
Y=\binom{\mathcal O_{\lambda,\tau}(k)}{s\partial_k\mathcal O_{\lambda,\tau}(k)},\quad
a=2s\tau k,\quad P_a=\begin{pmatrix}1&0\\-a&1\end{pmatrix}.
\]
Differentiating the accepted D1 gives the finite map
\[
Y=m_\tau(k)P_aX,\qquad
X=R_{\tau,k,s}Y,\qquad R_{\tau,k,s}=m_\tau(k)^{-1}P_a^{-1}.
\tag{D2}
\]
The proposed sharp absolute amplification in the Euclidean norm on `C^2` (also `R^2`) is
\[
C(\tau,k;s)=\|R_{\tau,k,s}\|_2
=\frac{e^{\tau k^2}}{q(\tau)}
\left(\sqrt{1+s^2\tau^2k^2}+s\tau|k|\right).
\tag{D3}
\]
The selected route is the two-by-two Gram matrix: `det(P_a^* P_a)=1` and `tr(P_a^* P_a)=2+a^2`. Its two singular values determine D3 and the extremizing error direction. Complete angular summability and q's positivity/monotonicity come from the accepted full series, without finite-mode approximation.

E03 must establish the sharp uniform constant
\[
C_{K,T,s}=\frac{e^{TK^2}}{q(T)}
\left(\sqrt{1+s^2T^2K^2}+sTK\right),
\tag{D4}
\]
with the edge cases `K=0` and `T=0`, and the pointwise strict inequality `C(tau,k;s)>1` for `tau>0`. This is **absolute inverse error amplification**, not the scale-invariant matrix condition number. Its dependence on s is part of the declared metric; changing s between comparisons would change the question.

If `Y_tilde=Y+e`, `||e||_2 <= epsilon_tau`, the requested recovery radius is `C epsilon_tau`. Direct access at tau=0 has radius `epsilon_0`. Thus the candidate strict improvement threshold for these worst-case radii is
\[
\epsilon_\tau<\epsilon_0/C(\tau,k;s),
\tag{D5}
\]
or the corresponding uniform threshold using D4. **This does not say every error direction or every individual collision test worsens.** Sharpness concerns the declared unrestricted two-component additive-error ball, not errors proven to arise from canonical source perturbations, physical detector laws or globally integrable derivative-error functions.

## 3. Approach B: use the covariant derivative, preserving its error set

The covariant pair removes the signal shear:
\[
Z=P_a^{-1}Y=
\binom{\mathcal O}{s(\partial_k+2\tau k)\mathcal O}=m_\tau(k)X.
\tag{D6}
\]
That simplification does not remove uncertainty in the raw pair. The same error e becomes `P_a^{-1}e`; its ball becomes an ellipsoid. Recovery gives exactly `m^{-1}P_a^{-1}e`, the error in Approach A. Assigning the same isotropic radius directly to Z would be a different acquisition hypothesis, not a benefit established by post-processing. Accordingly Approach A is the chosen proof route; Approach B is its mandatory correlation check, not a second physical observable or construction.

For **matched source information**, the exact statement is simpler: if the direct pair has uncertainty set E and its evolved uncertainty is exactly `m P_a E`, then `R(m P_a E)=E`. No information gain or loss follows from this invertible change alone. This conditional set identity assumes the same uncertainty has actually been propagated; it asserts neither admissibility of arbitrary source perturbations nor equal numerical cost. It must remain separate from the fixed output-error-ball comparison in Approach A.

## 4. Consequence and controls

The selected diagnostic can support the conditional lower estimate
`||X||_2 >= max(0, ||R Y_tilde||_2 - C epsilon_tau)`.
A strictly positive right side excludes a simultaneous zero at the particular evaluated `(lambda,k)`. No positive margin, cell cover, new exclusion interval or all-height claim has been obtained. Choosing this diagnostic is not selecting a collision-exclusion mechanism.

The [result index][results], [theta/source cluster][theta], [control register][controls] and [patterns index][avoid] govern the classification. In particular use [target classification][a01], [shared-premise controls][a02], [re-realization][a03] and [scoped exclusions][a07]. The screen concerns the actual proposed premises:

| Control family | What the conditioning argument retains; exact canonical premise it does not establish |
| --- | --- |
| Euler-factor sources | Applicable smooth Fourier/heat response and finite-jet algebra persist with the same angular bank. Unchanged canonical arithmetic fails. The error norm supplies no inequality rejecting their collision witnesses. |
| Weighted-square / finite-prime sources | The finite-jet matrix algebra is source-independent wherever the pair exists. Complete unit weights/full canonical reflection fail; global smooth field domains need separate checking and are not inferred from a finite endpoint match. |
| Reflected super-Gaussian / smooth positive-primitive sources | Where E01's weighted regularity applies, the same response factor and derivative shear preserve their collisions. Exact theta expansion fails, but that absent premise is not used to obtain a separating margin in D3. |
| Atomic / finite-profile sources | The algebraic jet comparison may apply to their transforms. Smooth prepared-field/operator-domain hypotheses need not; no full Hamiltonian realization is asserted for these controls. |

The conditioning target deliberately does not reject colliding controls: it is a recovery diagnostic. Even its quantitative factor is independent of the radial source once the supplied bank and response law are fixed. A canonical source estimate giving a positive physical margin remains a separate unresolved mathematical question.

The [earlier S03 matched-first-jet comparison][s03] reinforces the need to match information and retain correlations; its certified box, constants and scoped stop are not imported here. [Investigation06's auxiliary-flow lessons][aux] likewise remain scoped background. No novelty or literature-priority claim is made.

## 5. Disposition and boundary

**B02 completes with one bounded E03 r1 contract.** Its concrete deliverable is the exact first-jet accuracy threshold D5, including derivative mixing and complete angular attenuation, and the matched-uncertainty distinction. This is a modest analytical consequence of the representation, not an estimating advantage toward RH. A short proof and one correction pass suffice; no numerical campaign, new source, interaction, readout, clock or physical error model is authorized.

The new sharp bounds are pending E03 execution and E04 assessment. E02's existing acceptance and same-model/shared-premise qualifications remain unchanged. [Source-use receipt04][sources] records local use only; no primary theorem is newly imported. No manuscript, snapshot, investigation closure, external/shared/sibling status change or successor activation occurred.

**Next: [E] TND-A-E03 r1 — Sol.** Use the [frozen request][request] and [input record][inputs]; its final paragraph is the pasteable continuation prompt. Keep this chat's unique auxiliary chat0003 archive and start/end exact-turn capture.

[request]: ../../research-progress/handoffs/07_TND_A_E03_R1_FROZEN_REQUEST_20261106.md
[inputs]: ../../research-progress/handoffs/07_TND_A_E03_R1_INPUT_VERSIONS_20261106.json
[activation]: ../../research-progress/handoffs/06_TND_A_B02_ACTIVATION_INPUTS_20261106.json
[return]: ../../research-progress/handoffs/06_TND_A_B02_RETURN_RECORD_20261106.json
[progress]: ../../research-progress/01_HAMILTONIAN_AUXILIARY_DYNAMICS_RESEARCH_PROGRESS_20261105.md
[review]: ../../reviews/01_TND_A_E02_REALIZATION_ASSESSMENT_20261106.md
[sources]: ../../references/04_TND_A_B02_SOURCE_USE_20261106.md
[results]: ../../../../../../result-summaries/README.md
[theta]: ../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a03]: ../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[s03]: ../../../../../investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/notes/05_CALIBRATED_FIRST_JET_AND_MATCHED_DIRECT_COMPARISON_20261019.md
[aux]: ../../../../06_auxiliary_collision_flows/notes/06_APPROACH_SUMMARY_AND_GOALS_FOR_NEXT_BRAINSTORM_20261029.md

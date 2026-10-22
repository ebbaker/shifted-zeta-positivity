# Finite time signed reconstruction research program

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **ultra**, verified from the active turn metadata.

**Purpose:** determine whether positive-time information about the complete
theta function can improve the signed endpoint discriminant estimate at
t=0. Begin with an explicitly controlled finite matching time T; seek
uniformity as T grows only after a useful finite-time gain.

This is a focused branch of the [endpoint charge program][endpoint-program]
in BW12. Its [dedicated progress register][progress] uses FTSR task IDs;
the parent ECE and RCH identities retain their meanings and statuses.
The selected fixed-time source route remains primary. The present program
tests a possible way to strengthen its estimate, rather than presuming
that passage to infinity supplies an improvement.

**Status at program setup:** the exact transfer formulas, Gaussian error bounds,
and a screen against a free gain from time evolution are established
in [Note 12, Section 7][n12], with separate same-model checks in
[Review 11][review]. No improved theta reconstruction bound, positive
endpoint margin, all-height result, or specialist validation is claimed.

**21 October research update:** [Notes 13–15](../notes/13_PAID_ENDPOINT_WINDOW_AND_FINITE_TIME_BASELINE_20261021.md)
now pay a conditional window and finite matching-time range, analyze
canonical-cell and Gaussian Hermite approximations, and prove a sharper
direct covariance enclosure on a common uniform cutoff grid. Its additional
source moments and full errors are explicit. The same-data direct method
reproduces that interval; no positive-time advantage or positive endpoint
margin has been established. [Review 12](../reviews/12_FINITE_TIME_SIGNED_RECONSTRUCTION_OPENING_REVIEW_20261021.md)
records internal checks. The objectives and gates below are unchanged;
the [progress register][progress] holds current task dispositions.

## Objective and first meaningful milestone

For the unchanged source, write
\[
 H(t,z)=\int_0^\infty\Phi(u)e^{tu^2}\cos(zu)\,du,
 \qquad H_t=-H_{zz}.
\]
At t=0 choose a real-symmetric reference F with exactly two zeros inside
an external contour Gamma, both within a smaller disk. Set H(0)=F+E_0.
The complete residual includes every omitted theta mode and source ray.
For this pilot, F is the canonical source head, or another explicitly
supplied source-transform reference whose residual has the complete
finite-T heat-weighted moments needed below. Holomorphy of F alone does
not supply the residual heat continuation.
[Note 11][n11] gives
\[
 \Delta_H(0)=\Delta_F+L_F(E_0)+Q_F(E_0)+R_3,
 \qquad |R_3|\le C_3(\rho),\quad
 \sup_\Gamma|E_0/F|\le\rho<1.
\]
The reference may have a double. No positive internal root separation may
be assumed to exclude the endpoint case.

The first milestone is an independently justified improvement to the
**signed enclosure** for this same quantity on a declared parameterized
two-root window. Prefer a strictly larger lower endpoint, since that is
the endpoint relevant to exclusion. Strict containment of the full new
interval in the direct interval is another clear estimating gain. Report
both endpoints: smaller width with a worse lower endpoint is not evidence
of a stronger exclusion estimate. At setup no time, cutoff or window had been selected. Note 13 now
supplies a parameterized pilot; no numerical near-event theta window or
positive-time advantage has been established.

A positive complete lower endpoint would additionally exclude a double
in that window. A smaller error allowance alone does not do so. Under RH,
covering all possible endpoint multiplicities and heights would address
the parent's simplicity target; this local program does not assume that
coverage. The target-classification rule in [avoid/01][a01] applies:
rewriting the desired sign is not a signed estimate.

## Exact quantity to estimate at positive time

Use the complete residual heat field E(T,y) and Gaussian kernel
\[
 K_T(z,y)=(4\pi T)^{-1/2}e^{-(z-y)^2/(4T)},\qquad
 E_0(z)=\int_{\mathbb R}K_T(z,y)E(T,y)\,dy.
\]
All reference data and the functionals L_F, B_F and Q_F(V)=B_F(V,V)
remain at t=0. Define
\[
 \ell_T(y)=L_F(K_T(\cdot,y)),\qquad
 b_T(y,v)=B_F(K_T(\cdot,y),K_T(\cdot,v)).
\]
Then the signed response is exactly
\[
 S:=L_F(E_0)+Q_F(E_0)
 =\int\ell_T(y)E(T,y)dy+
   \iint b_T(y,v)E(T,y)E(T,v)dydv.
\]
This identity supplies the estimating interface, not a gain.

For an approximation P_T to E(T), put r_T=E(T)-P_T and
p_0(z)=integral K_T(z,y)P_T(y)dy. The exact signed error is
\[
\begin{split}
 \mathcal R_T&:=S-L_F(p_0)-Q_F(p_0)\\
 &=\int[\ell_T(y)+2B_F(p_0,K_T(\cdot,y))]r_T(y)dy
   +\iint b_T(y,v)r_T(y)r_T(v)dydv.
\end{split}
\]
The main open calculation is an actual-theta bound
\(\mathcal R_T\in[r_-(T),r_+(T)]\) that improves the direct enclosure.
Retain the mixed term and quadratic residual together wherever their
cancellation helps. The exact canonical coefficients, actual tail law,
or full-source identities must enter the quantitative estimate; merely
listing arithmetic or reflection as assumptions does not distinguish it
from generic collision-compatible estimates.

## Complete error budget and the time-evolution screen

For real center a define
\[
 \eta_T(a)^2=\int K_T(a,y)|r_T(y)|^2dy.
\]
When this integral is finite, the reconstructed error e_0=E_0-p_0 obeys
\[
 |e_0(a)|^2+2T|e_0'(a)|^2\le\eta_T(a)^2,\qquad
 \sup_{|z-a|=R}|e_0(z)|\le e^{R^2/(4T)}\eta_T(a).
\]
With the contour constants C_L and C_B of Note 11, a generic response
payment is
\[
 \beta_T=e^{R^2/(4T)}\eta_T(a),\qquad
 |\mathcal R_T|\le(C_L+2C_B\|p_0\|_\Gamma)\beta_T+C_B\beta_T^2.
\]
A signed interval for the same error gives the complete discriminant
interval
\[
 \Delta_F+L_F(p_0)+Q_F(p_0)
       +[r_-(T),r_+(T)]+[-C_3(\rho),C_3(\rho)],
\]
with any acquisition errors added separately. The open task is to improve
this payment through a signed estimate, not simply to rederive it.

These are complete fallback bounds from Note 12. They do not require a
uniform real-line approximation, but their integrals must include the
whole real line. The current normalized fixed-rank saddle profile does
not already provide this error contract.

If P_T is simply the exact heat evolution of a fixed endpoint
approximation, then p_0 is that same approximation for every T. For the
corresponding exact residual evolution,
\[
 \frac d{dT}\eta_T(a)^2
   =2\int K_T(a,y)|\partial_y r_T(y)|^2dy\ge0.
\]
This is a scoped screen against a free improvement from changing time.
It does not apply to arbitrary approximations with a heat defect, and
it does not make the full contour allowance exp(R^2/(4T)) eta_T
monotone. Signed estimates and optimization of the complete contour bound
remain possibilities. The exact reweighting and scalar gap invariant in
Note 12 likewise require a new estimate before they count as progress.

Every comparison must pay the complete source tails, real integration
tails, contour/acquisition errors, coefficient or mass errors, the actual
E_0/F wall ratio, and the cubic discriminant remainder. Retain parameter
dependence in a, r, R, the external wall floor, source cutoff, matching
time, and any approximation discretization. No independent adjustment
of the canonical law in the linear and quadratic terms is allowed.

## Work packages and decision rules

| ID | Deliverable | Acceptance condition |
| --- | --- | --- |
| FTSR-00 | Record the inherited transfer interface and its scope. | Cite Notes 11–12 and Review 11; distinguish identities from theta gains. |
| FTSR-01 | Specify one parameterized endpoint window and direct baseline. | Fix F, complete E, radii, two-root counts, wall floor, actual rho, source data and the fully paid Note 11 interval; retain the possible-double regime. |
| FTSR-02 | Choose finite T and a reconstruction approximation. | State P_T, complete spatial/source coverage, integrability, approximation errors and why this representation may permit a sharper estimate. |
| FTSR-03 | Bound the coupled signed reconstruction error. | Prove r_- and r_+ with all mixed terms and a quantitative use of unchanged theta data; independent of the desired endpoint sign. |
| FTSR-04 | Make the matched endpoint comparison. | Compare complete intervals with FTSR-01 on the same parameter set and data accuracy; demonstrate the claimed strict lower-bound improvement or containment. |
| FTSR-05 | Screen the candidate bound against controls. | Generic identities pass; any exclusion estimate identifies a quantitative premise unavailable on a control domain containing its event. |
| FTSR-06 | Investigate growing T after a finite-time gain. | Establish useful uniform signed bounds and all required limit/error interchanges; an improved finite-T result alone is insufficient. |
| FTSR-07 | Transfer successful bounds into the endpoint program. | Pay a positive full margin for local exclusion; then separately discharge height coverage and higher multiplicity in the parent ECE program. |

FTSR-01 and the inherited control checks come first. FTSR-02 and FTSR-03
form the analytic pilot; FTSR-05 accompanies any proposed improvement.
No comparison establishing a positive-time advantage has yet been made.
The common-grid direct refinement in Note 15 has the scope recorded above. FTSR-06 is contingent
on a useful gain, not an assumption that large T must be favorable.
FTSR-07's local exclusion requires strict positivity, not just interval
improvement; its global obligations remain separate.

If a proposed P_T merely reproduces a fixed endpoint truncation and no
sharper signed estimate survives, record that scoped outcome and retain
the direct source route as primary. Do not respond by expanding a numerical
campaign or adding asymptotic terms without an identified error mechanism.
A finite-T failure does not rule out all complete-field or large-time
methods. A known separated-pair example is a transfer check, not evidence
of new near-collision exclusion.

## Controls, evidence and research records

Use the [result index][results], [collision-control register][controls]
and [avoid index][avoid], especially [coupled estimates][a12],
[matched premises][a02], [scoped conclusions][a07] and
[numerics after the structural question][a10]. The checks already recorded
in Note 12 are inherited; no new theta numerical campaign is part of
creating these planning files.

The one-mode residual exp(Tu^2)cos(uy) reconstructs exactly cos(uz),
while its Gaussian energy is
\(\tfrac12(e^{2Tu^2}+e^{-2Tu^2}\cos(2ua))\). It checks the transfer and
energy formulas. It is not a theta collision control. The collision
families obey the generic reconstruction identities within their domains:
Euler-factor sources alter arithmetic; weighted-square and finite-prime
controls lack the full normalized reflection conjunction; reflected and
primitive sources lack canonical square coefficients; close normalized
endpoint controls fail ordinary Dirichlet-series arithmetic. A candidate
must name the actual quantitative distinction it uses. A valid bound on
a collision-free box of a control need not reject that box.

Save new proofs in notes/, computations and small replay records in
numerics/, and assessments in reviews/. Keep this overview focused on
objectives and acceptance criteria; update the [progress register][progress]
with evidence, scope and status. This conversation retains [chat 0004][chat]
and its existing identity under the [history workflow][history-policy].
All review to date is internal LLM review; none is independent specialist
validation. No manuscript milestone or new snapshot is created here.

[progress]: ../research-progress/03_FINITE_TIME_SIGNED_RECONSTRUCTION_PROGRESS_20261021.md
[endpoint-program]: 02_ENDPOINT_CHARGE_EXCLUSION_PROGRAM_20261021.md
[endpoint-progress]: ../research-progress/02_ENDPOINT_CHARGE_EXCLUSION_PROGRESS_20261021.md
[n11]: ../notes/11_CANONICAL_QUADRATIC_RESPONSE_AND_HEAD_TAIL_CANCELLATION_20261021.md
[n12]: ../notes/12_LARGE_TIME_INFORMATION_AND_ENDPOINT_RECONSTRUCTION_20261021.md
[review]: ../reviews/11_SIGNED_RESPONSE_AND_INFINITY_TRANSFER_REVIEW_20261021.md
[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a10]: ../../../../../../../avoid/10_numerics_ahead_of_the_question.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[chat]: ../chat-histories/0004_2026-10-21T21-29-18Z_analyze-endpoint-charge-obstacles.json
[history-policy]: ../../../../../../../tools/CHAT_HISTORY.md

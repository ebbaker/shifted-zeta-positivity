---
research_program: COORD
secondary_programs: [PR01, PR02, PR03, ALG, PR02-CORR]
status: reviewed_research_continuation_theta_signed_estimate_open
---

# Positive primitive controls and the completed carrier budget

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6-astra**, reasoning effort **ultra**, verified from the current session metadata. This is research with independent internal LLM review, not external refereeing or formal verification.

This continues the [signed forms overview](../../research-overview/RESEARCH_OVERVIEW_20261015_SIGNED_FORMS_AND_PRIMITIVE.md) and [manuscript integration handoff, Note 55](55_SIGNED_FORMS_MANUSCRIPT_INTEGRATION_AND_HISTORY_20261015.md). Three new results sharpen the distinction between auxiliary positivity and the physical signed estimate, and complete one previously unresolved elementary stage of the outer theorem. The manuscript remains the 96-page version identified by its existing build record; Notes 56–58 are subsequent research, not yet integrated into it.

## The positive primitive structure does not distinguish theta

[Note 56](../05_theta_correlation_kernels/56_POSITIVE_PRIMITIVE_COLLISION_CONTROL_20261015.md) constructs a normalized positive even source from
\[
g_\delta(u)=e^{-3u^2-\delta\cosh(4u)}(1+u^2+u^4/2),\qquad\delta>0.
\]
Its fixed primitive is
\[
\psi_\delta(u)=8\int_u^\infty\sinh(v-u)\phi_\delta(v)\,dv,
\qquad\int_0^\infty\cosh(v)\phi_\delta(v)\,dv=1/16.
\]
The heat-first transform of this primitive is strictly positive on the whole interval \(0\le t\le1/2\). It has the same boundary constant \(1/2\), the same complete differential reconstruction, an even completed primitive, and every algebraic spectral asymptotic coefficient of the theta primitive. The physical source also retains strong log-concavity, strict square-variable log-concavity and double-exponential decay. The rational finite-jet nonclosure argument applies to it as well.

Nevertheless, every sufficiently small fixed positive damping parameter retains a nondegenerate positive-time collision. The undamped collision is exactly
\[
T_0=(4-\sqrt{10})/2,\qquad x_0^2=20+7\sqrt{10}.
\]
Persistence follows from the implicit function theorem; no numerical damping cutoff is claimed. On its full stationary predecessor, \(\mathcal L_0/E=-1/(T_\delta-t)+O(1)\). Thus even the combined primitive structure and source-shape hypotheses do not give the needed bound. This is a control family, not a theta counterexample. A future proof must identify the additional complete-theta information at the step that excludes it.

## Negative circle mass can discard a lower-order cancellation

[Note 57](../02_signed_cusp_control/57_CIRCLE_DEFECT_MULTIPLICITY_AND_RADIUS_20261015.md) compares the exact signed current with its negative-mass sufficient bound. Conditional on a collision of multiplicity \(m=2r+j\), with \(s=T-t\), every radius bounded above and away from zero gives
\[
D_{j,R}/E\asymp s^{-r},\qquad \mathcal L_j/E=-r/s+O(1).
\]
For \(r\ge2\), the separate boundary masses therefore have a higher pole order than their signed difference. On the diagnostic scale \(R=\rho\sqrt{s}\), the defect coefficient has the form \(C_r(\rho)/s\), where \(C_r(\rho)>r\). Its minimum is strictly greater than \(r\) for \(r\ge2\); for \(r=1\), its infimum is exactly \(1/2+2/\pi>1\). Shrinking the radius does not create an admissible bounded coefficient through the event.

These statements use the full physical stationary branches. Small-energy localization retains their sufficiently close predecessors. The useful target remains the complete signed current, with its positive and negative masses combined before estimation.

## The outer carrier differentiation budget is now explicit

[Note 58](../01_weighted_outer_remainders/58_EXPLICIT_CARRIER_PHASE_AND_CONDITIONAL_HEIGHT_20261015.md) completes the elementary carrier stage left open in Note 43. For \(L\ge100002\), \(0<t\le1/2\), and \(tL\ge61/24\), the carrier-to-phase four-jet error is at most
\[
409/L.
\]
With Note 43's analytic-replacement budget \(B_C(L)\), the complete physical error is at most
\[
d_C(L)=1728B_C(L)+409/L.
\]
The condition \(d_C(L)\le1/8\) gives both full strict signs and a physical energy gap. A sufficient conditional log-height is
\[
L\ge1+\max\{749376582912,\;14000\log(663552G_0C_{\rm EP})\},
\qquad G_0=962773/671,
\]
with any imported validity threshold imposed as stated in Note 43. The actual numerical maximal-interval exponent-pair constants remain unevaluated. This formula is consequently conditional; it is not an evaluated starting height for the \(61/24\) theorem or a practical finite bridge. The separate five-halves middle-block obstruction is unchanged.

## Validation and next research

[Review 33](../../reviews/33_PRIMITIVE_CIRCLE_AND_CARRIER_CONTINUATION_REVIEW_20261015.md) records the independent proof checks, exact-arithmetic replays and their limits. Small reproducible checkers and hash-bound execution receipts are saved in `numerics/`. Their finite algebra supports the arguments; it does not certify a new theta sign region.

The next direct task is to state one additional arithmetic or complete-source identity that distinguishes theta from Note 56's control, then derive a signed bound for the full primitive reconstruction or current. Its coefficients must be prescribed before validation, remain locally bounded through candidate events, and cover both required predecessor branches. Another representation or positive auxiliary norm without that discriminating estimate does not resolve the gap.

In parallel, the outer task now has one explicit missing package: numerical constants for the five maximal-interval logarithmic-phase bounds at the specified positive loss, including their A-process/completion costs and validity thresholds. The new carrier calculation need not be repeated. A new saving, rather than a change of constants, is still needed to cross the identified middle interval at \(\theta=5/2\).

The established height-112 certificate, closed outer threshold \(61/24\) with unevaluated starting height, and separate explicit \(tL\ge5\) theorem remain unchanged. No manuscript snapshot, commit or tag is created in this continuation.

## Research history

This conversation is registered once in the explicitly authorized formal replay lane as history **17**, **Continue quaternion theta geometry**, thread `01a13f10-8044-7ec1-9c35-59e518f5243c`. Its source creation time and original archive identity are preserved. The live registry, rather than this handoff, supplies evolving message counts and hashes. The final reply is captured only after it is emitted, using the bounded exact-turn follow-up; native completion-hook activation has not been verified.

### Later destination update, 15 October 2026

The preceding paragraph records the original registration. At the author's
subsequent explicit request, this same history 17 was relocated to
[Investigation 22](../../../22_theta_manifold_geometry/chat-histories/README.md).
Its original identity and all prior public messages were preserved; the
[transfer receipt](../../../22_theta_manifold_geometry/CHAT_HISTORY_RELOCATION_20261015.json)
records the checks. The formal replay folder now contains a historical pointer.
Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra**,
reasoning effort **ultra**.

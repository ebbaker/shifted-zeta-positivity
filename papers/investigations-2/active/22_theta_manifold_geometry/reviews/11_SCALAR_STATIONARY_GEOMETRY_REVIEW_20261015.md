# Review of scalar stationary geometry and the invariant boundary trace

> **17 October 2026 — history routing update.** Historical formal-replay routing below is superseded. Chats [21](../chat-histories/0021_2026-10-15T16-30-47Z_continue-theta-manifold-geometry.json) now use this investigation's [local registry](../chat-histories/index.json), as recorded in the [relocation receipt](../CHAT_HISTORY_RELOCATION_20261017.json). Original identities, provenance and public messages are preserved. All future Investigation 22 chats belong in this local history folder.

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**, verified from the current turn metadata. This review answers the request to reconsider physical-jet Note 01 before the next investigation. Three internal collaborators and the coordinator assessed the deductions; this is not external refereeing or formal verification.

## Main conclusion

There is a useful additional simplification. The [new geometric note](../notes/01_physical_jet_geometry/03_SCALAR_STATIONARY_GEOMETRY_AND_INVARIANT_TRACE_20261015.md) reduces the actual local stationary geometry to one analytic curve and one scalar vanishing factor. A fixed positive cone of starting jets makes the reduced target usable without knowing a hypothetical collision location. The joint-current lower boundaries combine into one invariant scalar trace.

The resulting target is

\[
W B_\partial\le C W^2+\varepsilon_0|W|.
\]

It preserves orientation, the complete starting factor and radial vanishing order. It does not establish the required theta sign or justify dropping any endpoint correction.

## Analytic verification

The reviewers independently derived the local classification. If the event multiplicity is \(2r+j\), then \(W=h_j\) and \(W_{xx}\) have even spatial order and the same leading sign. Their positive backward heat-polynomial expansions give that sign throughout a sufficiently small backward rectangle. Hence \(W_x\) is strictly monotone, and the existing analytic predecessor is its sole root. The opposite stationary branch is empty there. This concerns times strictly before the event; both parities remain necessary for an event-independent theorem.

On the resulting curve, the physical analytic ideal is \((H,H_x)=(s^r)\), with \(W=s^ru(s)\) and \(u(0)\ne0\). In the odd case, \(H=s^{r+1}v(s)\). Consequently \(E=W^2Q\), where \(Q=1\) on the even branch and \(Q=1+s^2(v/u)^2\) on the odd branch. The exact identities \(h'=\chi'w\) and \(w'=W_{xx}\) independently yield \(|H/H_x|\le s\sup|\chi'|\) and the stated first coefficient of \(H/H_x\).

The one-sided scalar trace condition is equivalent to the original physical target up to bounded comparison factors; mixed errors must remain explicit. The signed distance formulation does not require dividing by the vanishing observation. Its proof does not construct a favorable theta trace.

For every fixed \(\kappa>0\), the cone \(|Z_j|\le\kappa|W|\) eventually contains every finite-event predecessor. It restricts starts only, so it does not alter the endpoint intervals or their original coverage obligations. On the odd branch, \((B+\kappa|A|)_+\) is the exact least nonnegative reconstruction coefficient relative to \(W^2\) over the unrestricted algebraic cone. The actual theta image may be smaller. One draft phrase suggesting that the physical ratio itself attains both cone endpoints was corrected; no such attainability is assumed.

The actual-curve coefficient \(B+s\lambda A\) can be bounded even when the full-plane quotient coefficient diverges. This identifies a less demanding sufficient hypothesis, not a prescribed theta identity. Singular reconstruction rules still require independent uniform source and cutoff error estimates.

For the arithmetic side, direct telescoping verifies invariance of all four rectangle boundary terms under \(J\mapsto J+\partial_uL\), \(K\mapsto K-\Delta L\). With the stated weighted integrability and absolute upper-flux hypotheses, the canonical integrated current is \(\widehat J=\overline J-\mathcal G K(0)\). Its lower trace is unchanged. The collar gauge moving source lower flux into index lower flux is generally nonlocal in the index and does not preserve the excluded finite polynomial ansatz.

## Exact replay

The [checker](../numerics/check_stationary_scalar_geometry.py) passes **1,291 rational assertions** using the existing reviewed polynomial engine. A separate collaborator audited the script and independently replayed it; the resulting receipt was byte-identical. Checks cover even heat-polynomial coefficients and derivative identities, both parity leading stationary displacements, the odd first-jet ratio, finite gauge invariance and canonical current algebra, cone maxima, and explicit non-theta collision controls.

The [receipt](../numerics/STATIONARY_SCALAR_GEOMETRY_CHECKS_20261015.json) and [manifest](../numerics/SCALAR_STATIONARY_GEOMETRY_REVIEW_CHECKS_20261015.json) identify the files and dependency hashes. General analytic uniqueness, arbitrary multiplicity and infinite source/index limits are proved separately. Finite checks do not certify theta positivity or an RH consequence.

## Recommendation

Use the scalar signed trace on prescribed cones as the geometric target for the next arithmetic calculation. Keep one total boundary invariant and estimate its unfavorable part relative to \(|W|\). Additional curvature or full-plane reconstruction bounds would impose structure not required by this local exclusion argument.

Notes 01–02 and the manuscript remain valid and unchanged. The new result refines their application to the actual stationary field; it does not invalidate their statements about larger homogeneous relaxations. No next arithmetic experiment has been started. This chat retains formal replay history 21 and the authorized capture workflow.

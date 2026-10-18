# 11: Updated research overview and GPT-6.1 Sol execution plan

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. **Drafted by GPT-6.1 Sol, reasoning effort ultra;
coordinated and edited by GPT-6 Astra, reasoning effort ultra.** The prior
packet, strip and approximation results were developed with GPT-6 Astra,
at the effort settings recorded in their individual sources. This document
plans future work; it records no new experiment, collision exclusion or
Newman bound.

**Execution decision:** every future research stage below is to be carried
out by **GPT-6.1 Sol**, with **ultra** reasoning as the planned default.
Derivation, implementation and adversarial replay may use separate Sol
sessions. They remain same-model internal review, even when a fresh process
or a separately written checker is used. No other model or specialist-human
review is a prerequisite for continuing this plan. Each resulting record
must report the actual model and effort from available execution metadata;
a planned configuration is not evidence of the configuration actually used.

This is the successor to the [initial exploratory proposal](01_EXPLORATORY_RESEARCH_PROPOSAL_20261018.md),
which remains a historical record. The controlling background is the
[result-summary index](../../../../result-summaries/README.md) and
[patterns-to-avoid index](../../../../avoid/README.md), especially
[heat-flow results](../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md),
[collision controls](../../../../result-summaries/12_collision_controls_and_screening.md),
[target classification](../../../../avoid/01_restating_the_target.md),
[premise-based screening](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[scoped exclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md)
and [preserving cancellations](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).

## What the updated manuscript supplies

The working manuscript consolidates the finite Euler operations, complete
half-line packets, modular endpoint cancellation, source rigidity and
finite-prime collision controls. Its strengthening incorporates
[Note 05](../notes/05_COMPLEX_STRIP_CARRIERS_AND_SHARP_LOG_DERIVATIVES_CODEX_20261018.md)
and [Note 06](../notes/06_CANCELLATION_PRESERVING_APPROXIMATION_AND_NEWMAN_ROADMAP_CODEX_20261018.md),
assessed in [Review 04](../reviews/04_MANUSCRIPT_AUDIT_AND_STRENGTHENING_REVIEW_CODEX_20261018.md).
The revised source set and scalar table are recorded in the
[build record](../manuscript/positive_arithmetic_packets/BUILD_RECORD.json)
and [integration review](../reviews/05_UPDATED_MANUSCRIPT_INTEGRATION_REVIEW_CODEX_20261018.md).
The important changes are quantitative analytic tools with explicit limits.

For \(0\le t\le1/2\), every nonzero bounded nonnegative combination

\[
 V(t,z)=\sum_{n\ge m}c_nH_n(t,z),\qquad m\ge2,
\]

has positive real part throughout \(|\Im z|\le\pi m^2\). On the real axis,
with \(\beta=(\log V)_x\), the stronger combined estimate is

\[
 \beta^2+|\beta_x|\le\frac1{4m^4}.
\]

For the carrier \(A=A_{\mathcal P}\), \(2\in\mathcal P\), this gives

\[
 |A_x/A|\le1/8,\quad
 |(\log A)_{xx}|\le1/64,\quad
 |(\log A)_{xx}H^2|\le E/64,
 \qquad E=H^2+H_x^2.
\]

The two-prime residual \(r=R_{\{2,3\}}/A_{\{2,3\}}\) retains

\[
 r<7.3\times10^{-25},\quad
 |r_x|<1.06\times10^{-25},\quad
 |r_{xx}|<1.54\times10^{-26}
\]

on the real axis and \(|r(z)|<8.5\times10^{-25}\) on \(|\Im z|\le1\).
These bounds control an auxiliary tail relative to a positive carrier.
They do not measure the relative error of a physical field vanishing at
a zero. Positive-coefficient collision controls share the strip geometry;
carrier optimization alone cannot provide exclusion.

The new cancellation-preserving representation shifts the **complete
reflected source before truncation**. With \(w_t(v)=e^{tv^2}\Phi(v)\),

\[
 H(t,z)=\frac{e^{-dz}}2\int_0^\infty
 [w_t(u+id)e^{izu}+w_t(u-id)e^{-izu}]\,du,
 \qquad0<d<\pi/8.
\]

Replacing the source by the modes \(1\le n<m\) defines

\[
 |\partial_z^j(H-\widetilde H_{m,d})(t,z)|\le K_je^{-d\Re z}
 \quad(j=0,1,2)
\]

on the specified time and complex spectral domains, with explicit
admissibility conditions and \(K_j\). At \(d=\pi/16\), \(m=5\),

\[
 (K_0,K_1,K_2)<(8\times10^{-23},1.61\times10^{-23},3.23\times10^{-24})
\]

for \(0\le t\le1/2\), \(|\Im z|\le1\). These are arithmetic-mode tail
bounds. They omit the retained-mode quadrature and finite-source-cutoff
errors that an evaluator must add.

The near-boundary choice

\[
 d(x)=\pi/8-a_*\log x/x,\qquad
 m(x)=\lceil\sqrt{b_*x}\rceil,\qquad b_*>1/(4\pi),
\]

gives an envelope-relative asymptotic tail improvement when

\[
 a_*(4\pi b_*-1)>3/4.
\]

The onset and constants are unevaluated. Differentiation always holds
\(m,d\) fixed at a point or throughout a cell; derivatives of an adaptive
cutoff formula are not physical derivatives. A gamma envelope is a
positive normalization, never a lower bound on \(|H|\) or its first jet.

The missing research is a usable **signed estimate or strict positive
margin for the complete field after modular cancellation**. Neither the
new constants nor an accurate approximation has supplied it. All-positive-time
noncollision remains an RH-equivalent target, stated once rather than
counted as a sequence of new criteria. A finite certificate, a measured
evaluation improvement, an effective outer range or a precisely scoped
obstruction would be a separate milestone.

## Dependencies and common records

The sequence is \(0\to1\to2\), followed by the analytic work in Stage 3
and consumer selection in Stage 4; Stage 5 closes the selected contract.
Stage 3 can begin once Stage 1 fixes the actual error scale, but it cannot
assume Stage 2 produced a margin. A computation that fails its gate returns
a diagnosis, not an inferred positive result.

All proposed paths below are relative to this investigation. They are
deliverable names, not files claimed to exist. Use `notes/` for derivations,
`numerics/` for code and small records, and `reviews/` for assessments.
The run manifest must bind exact rational domains, source/code hashes,
library versions, actual precision, rounding rules, \(m,d\), integration
cutoffs, derivative orders, subdivision rules, failure limits and measured
cost. Every enclosure separates mode truncation, source-integral tail,
quadrature, arithmetic rounding and whole-cell propagation. Reused inputs
carry their original status. Failure logs retain the cell and the dominant
error term, including unsuccessful parameter choices.

Follow [LARGE_FILES.md](../../../../LARGE_FILES.md): keep code and small
certificates in Git, externalize large regenerable data with stored-byte
and canonical-content hashes, a tracked regeneration guide, and consumers
that reject absent or mismatched inputs. Milestones update the concise
`DRAFT_HISTORY.md`, current status and relevant result summary. No new
manuscript snapshot folders are needed.

## Stage 0 — pin the strengthened manuscript and review its contracts

**Work by Sol.** Read the revised manuscript source set against Notes
05–06, Review 04 and the scalar checker record. Pin the new source-set
digest; the digest in Review 04 identifies the earlier reviewed manuscript,
not the revised bytes. Recheck the strip boundary, Schwarz scaling,
combined derivative budget, real residual derivatives, complex denominator
lower bound, complete contour shift and the near-boundary asymptotic.
Check normalizations and hypotheses at every imported theorem.

Replay both constant scripts and compare every printed decimal to its
outward enclosure. Inspect derivative orders and all finite-mode error
conditions symbolically. Compilation verifies the document build; scalar
replay verifies scalar calculations. Neither validates an unproved margin.

**Deliverables:** `reviews/06_SOL_STRENGTHENED_MANUSCRIPT_CONTRACT_REVIEW_<DATE>.md`
and `numerics/STRENGTHENED_MANUSCRIPT_REPLAY_<DATE>.json`, alongside the
current manuscript build record.

**Gate:** every new theorem has a complete proof and explicit domain;
every printed bound is covered by a recorded enclosure; no claim equates
packet-relative error with physical relative error. Repair a discovered
defect before consuming that statement. An auxiliary result can remain
publishable without a collision result, but its status must say so.

## Stage 1 — verify a complete shifted evaluator at physical jet scale

**Domain and frozen parameters.** Begin on

\[
 D_0=[1/100,1/5]\times[25,45],\qquad
 0\le\Im z\le1
\]

for evaluation tests, using real \(z\) for the first-jet certificate.
Start with \(m=5,d=\pi/16\); represent the shift and all dependent
constants by rigorous intervals. Freeze both parameters over each cell.
Verify the conditions \(b>0\), \(8\pi m^2\cos4d\ge T\), and geometric
ratio \(<1\) for the actual interval values. A failed condition rejects
the cell rather than silently reusing the nominal-point constants.

Derive explicit tails for the retained shifted integrals over \(u\ge U\),
uniform in every required derivative and time box. Integrate \(0\le u\le U\)
with outward rounding. Preserve both shifted terms and reflection before
truncation. Include the \(d\)-dependent derivative factors. If time Taylor
propagation uses \(H_t=-H_{xx}\), certify the extra spatial derivatives;
a \(C^2\) statement alone does not pay for arbitrary high time order.

Compare the actual errors for \(H,H_x,H_{xx}\), both unnormalized and
divided by an explicitly positive gamma carrier or suitable jet scale.
At ordinary zeros use the nonvanishing first jet; never divide by \(|H|\).
At candidate stationary points retain interval lower bounds rather than
assuming \(H\ne0\). Show which part of the budget dominates at the
worst certified cell. Test conjugation and the heat equation as diagnostics,
while respecting that the finite shifted approximant need not be even.

**Deliverables:** `notes/07_SHIFTED_EVALUATOR_AND_COMPLETE_ERROR_BUDGET_<DATE>.md`,
`numerics/certify_shifted_theta_jet.py`, and
`numerics/SHIFTED_EVALUATOR_VALIDATION_<DATE>.json`.

**Gate:** shifted and complete-source enclosures intersect on matched
point/cell tests; rigorous total error lies below the proposed consumer's
margin allowance. Budget a specified fraction of that margin for each
component, with a recorded reserve. Tiny standalone decimals do not pass
this gate. If quadrature, interval dependence or a source tail dominates,
allow one documented bounded repair and rerun the same tests. If it still
fails, record the failed implementation and domain without asserting that
all contour methods fail.

## Stage 2 — run one fair bounded pilot and adversarial controls

The exact pilot \(D_0\) already has a complete-source certificate in
[Investigation 22, physical-jet Note 06](../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/06_WALL_FLUX_AND_CERTIFIED_THETA_WINDING_20261015.md),
with [Review 18](../../../investigations-2/active/22_theta_manifold_geometry/reviews/18_SPACETIME_BOUNDARY_AND_GEOMETRIC_CONTINUATION_REVIEW_20261015.md).
It uses 234 boundary segments with winding zero and a practical baseline
of 128 full-time interior strips. Both share 76 midpoint integrals and
identical errors. The source script is
`../../../investigations-2/active/22_theta_manifold_geometry/numerics/check_theta_boundary_winding.py`.
These exact domains and algorithms were inspected for this plan; this is
an existing internal certificate, not a fresh replay.

**Work by Sol.** First replay that baseline, including its full tails,
whole-segment signs, wall flux and exact polygon count. Compare three
evaluators where useful: original real packet assembly, direct complete
source, and shifted complete-source approximation. Give them the same
domain, output conclusion, required certified error and resource budget.
Start at the historical 160-bit precision; record any necessary precision
increase and charge all precomputation, derivative generation, vertices
and rejected cells. Do not manufacture a costly two-dimensional baseline
when full-time strips already work.

For a real interior consumer, certify a cellwise lower bound on

\[
 \|(\widetilde H,\widetilde H_x)\|_2
 -e^{-dx}\sqrt{K_0^2+K_1^2}-\epsilon_{\rm eval}>0.
\]

A coordinate-sign proof is equally acceptable. For boundary winding,
certify every full edge and its homotopy; count degree exactly and retain
ordinary-root wall flux. A complex Rouché consumer also requires a strict
boundary margin and a certified approximant zero count. No sampled plot
substitutes for these conditions.

**Adversarial screen.** Use the same numerical exclusion interface with
the correct source-specific error contract. Where a theta-specific premise
fails, the interface must expose that failure rather than substitute theta
tail constants. Use the [control catalogue](../../../../result-summaries/12_collision_controls_and_screening.md)
and preserve each control's frozen coefficients.

| Control | Premise absent from the theta application | Required challenge |
| --- | --- | --- |
| Finite-prime orbit controls | Complete normalized analytic reflection; finite prime identities and higher-packet strip bounds survive | Analytic premise test now; a numerical event test requires a located and enclosed event, since the theorem supplies no effective height |
| Three- and four-square controls | Full source reflection and unchanged complete theta coefficients, despite matched finite endpoints | Replay published event enclosures; for the four-square control include \(t=1/100\), \(83.5323729<x_*<83.5323730\) in a rational surrounding box |
| Reflected super-Gaussian | Exact normalized theta integer-square source expansion and its tail constants | Use a box containing the exact event \((1/4,\pi/4)\) |
| Smooth shape and positive-primitive controls | Theta square-mode data, despite the proved reflection/primitive properties | Keep their analytic witness status; do not invent a certified damping or event box |
| Euler-factor \(\Phi_{c,p}\) controls | Unchanged normalized theta coefficients and level | Replay their genuine negative-Laguerre witnesses for bound screening; do not label a witness point an enclosed double event |
| \(q,q_{T,a}\) counter-kernels | The exact theta square-source expansion | Use the source's proved collision/threshold contract and enclose an applicable event before a numerical event test |
| Smooth-density and two-channel controls | The particular complete-source signed estimate; auxiliary positivity supplies no such estimate | Test any newly proposed signed premise in the proved class, with no assumed extension to theta |

A sound finite certificate **must reject a box containing an applicable
control's actual event**: its true first-jet minimum is zero. It may pass a
control box avoiding that event. Failed theta-premise checks and numerical
event rejection are distinct outcomes, both recorded. Polynomial heat
events supply an additional inexpensive test that the index, wall terms
and strict-inequality interface can fail as intended.

**Deliverables:** `notes/08_MATCHED_PILOT_AND_CONTROL_SCREEN_<DATE>.md`,
`numerics/SHIFTED_PILOT_COMPARISON_<DATE>.json`, and
`reviews/07_SOL_PILOT_AND_ADVERSARIAL_REPLAY_<DATE>.md`.

**Gate:** reproduce valid exclusion on all of \(D_0\), reject adversarial
event boxes, and show either at least a factor-two reduction in total
measured cost at matched error or a useful certified margin/coverage
gain on one predeclared adjoining test region. This is a research decision
threshold, not a mathematical theorem. Reproducing known coverage alone
completes validation but does not justify a large scan. If the gain is
absent, retain the tool and the measured comparison; proceed analytically
without claiming computational superiority.

## Stage 3 — derive the cancellation-sensitive estimate

This is the central unresolved mathematical stage. Sol must identify an
inequality using the complete modular completion that is independently
provable and strong enough for a measured consumer. The normalized
Laguerre identity is

\[
 \mathcal L_0=A^2(h_x^2-hh_{xx})-(\log A)_{xx}H^2,\qquad h=H/A.
\]

The \(E/64\) payment is already controlled; the first signed term is not.
The full positive carrier \(C=\sum_{n\ge2}H_n\) removes the arithmetic
remainder entirely and still leaves first-mode cancellation. This is a
mandatory diagnostic against repeated prime-list optimization.

Begin on one compact positive-time region chosen from Stage 2's weakest
cells, and state the candidate theorem, hypotheses and required lower
margin before writing a long derivation. Keep the paired modular terms,
lower intervals and boundary contributions together before estimating.
Compare the new estimate numerically with the actual physical-scale jet
and complete-source calculation. Do not estimate the two cancelling
sectors separately and call the resulting absolute tolerance a sign law.

An event-normalized calculation must retain the curvature coefficient
\(c=H_{xx}(T,x_*)/2\) and the stationary predecessor \(x_{\rm stat}(s)=x_*+O(s)\)
correctly. State any lower bound on \(|c|\) and higher-derivative bounds as
restricted hypotheses. Fixed imaginary packet shifts lie outside the
bounded rescaled local germ; give an exterior remainder instead of
substituting a finite Taylor polynomial there. Higher multiplicity and
\(t\downarrow0\) require new explicit control.

**Deliverables:** `notes/09_COMPLETE_MODULAR_SIGNED_ESTIMATE_<DATE>.md`
and `reviews/08_SOL_SIGNED_ESTIMATE_ASSESSMENT_<DATE>.md`, with a compact
numerical record if a quantitative test is used.

**Gate:** obtain an applicable strict margin with complete error, a new
effective bound consumed by Stage 4, or a proved obstruction in a named
restricted class. If the proposal merely renames noncollision, depends on
an unbounded event normalization, or passes every premise of a colliding
control, stop that estimate and record the exact missing input. This stops
the specified attempt; it does not rule out infinite assembly, different
contours or all modular methods.

## Stage 4 — select and close a complete global consumer

Use the normalization \(H_0(z)=\xi((1+iz)/2)/8\) in
[Polymath, equations (1)–(4)](https://arxiv.org/html/1904.12438v2).
The published comparison baseline is \(\Lambda\le0.2\), from
[Platt–Trudgian, §3.4, Corollary 2](https://arxiv.org/pdf/2004.09765).
No claim about the current best bound is needed. Select the route from
measured margins, cost and missing hypotheses; do not select an attractive
decimal target first.

**Slab route.** Choose \(0<\tau<0.2\). Supply finite first-jet exclusion
on \([\tau,0.2]\times[0,X]\) and an explicit uniform outer exclusion for
\(x\ge X\); evenness covers negative heights. Invoke the repository's
positive-threshold finite-collision reduction only after the seam and all
time endpoints are covered. Then \(\Lambda\le\tau\). A time-dependent
existential cutoff or scattered windows leave a gap. Existing enormous
outer cutoffs can define a valid starting contract, but an uncomputed
finite bridge remains unclosed.

**Canopy/barrier route.** Follow all hypotheses of
[Polymath, Theorem 1.2](https://arxiv.org/html/1904.12438v2#S1.Thmtheorem2):
initial zeta verification to \(X/2\), final exterior nonvanishing for
\(x\ge X+\sqrt{1-y_0^2}\), and the moving intermediate-time barrier.
Its conclusion is \(\Lambda\le t_0+y_0^2/2\). Transcribe the exact
parameter restrictions and regions into the consumer ledger before
execution. The carrier's zero-free strip supplies a denominator, not
the required theta nonvanishing.

For either route, first produce a budget table binding every region to a
theorem or replayable certificate, with a strict minimum margin, its error
payments and an effective outer threshold. If using any existing candidate
package, carry the [Newman audit](../../../investigations-2/newman_certificate_audit/README.md)'s
uncompleted producer obligations explicitly. A useful evaluator does not
complete that audit. Evaluate the near-boundary asymptotic's actual onset,
constants and retained-mode quadrature before using it in a global budget;
its \(O(\sqrt x)\) mode count is no measured complexity advantage.

**Deliverables:** `notes/10_GLOBAL_CONSUMER_AND_COVERAGE_LEDGER_<DATE>.md`
and `numerics/GLOBAL_CONSUMER_BUDGET_<DATE>.json`.

**Gate:** one fully specified route has feasible measured finite coverage
and a proved outer contract. Otherwise record the missing finite or
analytic range, keep the strongest established auxiliary gain, and stop
expansion. A projected \(\tau\) or \(t_0+y_0^2/2\) remains a scenario until
every hypothesis is met.

## Stage 5 — certificate replay and claim closure

Sol performs an adversarial replay from the pinned sources and parameters,
checking all cells, seams, equality endpoints, outward lower bounds and
external-input hashes. Recalculate the weakest margins rather than only
parsing `PASS` logs. Test malformed, missing and mismatched inputs and
strict versus non-strict inequalities. A separately written Sol verifier
can reduce shared implementation errors; it is still same-model review.

**Deliverables:** `reviews/09_SOL_GLOBAL_CERTIFICATE_AND_CLAIM_REVIEW_<DATE>.md`,
`numerics/FINAL_CLAIM_LEDGER_<DATE>.json`, updated manuscript/status/index
links and a concise milestone entry. The claim ledger matches each public
sentence to its proof, hypotheses and verified domain. Report actual model
settings and remaining internal-review limitations accurately.

**Closure rule:** announce a new Newman bound only when the chosen full
contract is closed and replayed. Otherwise close the round with its exact
earned result—improved analytic constant, validated evaluator, measured
bounded gain or scoped obstruction—and its remaining gap. This plan
authorizes no claim in advance of that evidence and launches none of these
future research stages by being saved.

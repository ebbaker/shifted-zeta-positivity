# 02 Progress for the updated arithmetic collision rigidity research plan

Created and last updated: **18 October 2026, America/New_York**. Prepared
for **Edward Baker** with substantial LLM assistance. Tracker initialization:
**GPT-6.1 Sol (`gpt-6.1-sol`), reasoning effort max**, verified from this
turn's execution metadata. The research plan specifies Sol with **ultra as
the planned default**; future entries must record their actual settings.

This is the continuing progress record for
**`research-overview/02_UPDATED_RESEARCH_OVERVIEW_AND_SOL_EXECUTION_PLAN_20261018.md`**
in Investigation 11, Arithmetic constraints at collision scale. It is
explicitly tagged to **research overview 02** by its `02_` filename prefix
and this association. The [updated overview and Sol execution plan][plan]
defines the goals, dependencies and acceptance gates tracked here. The
earlier overview 01 is historical background.

**Current position:** the follow-up round has closed a finite consumer:
**E>0 on [1/100,1/5] × [-1001,1001]**, combining a signed certificate
and complete vertical wall with a finite propagation proof. [Note 13](../notes/02_updated_research_plan/13_VERTICAL_WALL_AND_FINITE_HEIGHT_NONCOLLISION_20261018.md)
and [Review 11](../reviews/11_HIGH_HEIGHT_SIGNED_AND_VERTICAL_WALL_REVIEW_20261018.md) carry the evidence. The initial bounded
round's four scoped gates remain passed; the global Stage 4 gate remains
unpassed. Both matched timing rounds miss the factor-two speed gate.
**No new Newman bound is established.**

The user requested a separate notes home for this research stage:
[`notes/02_updated_research_plan/`](../notes/02_updated_research_plan/README.md).
It is explicitly affiliated with research overview 02. New Notes 07–10 live
there; this redirects the overview's proposed note paths without moving
original Notes 01–06 or changing the plan's mathematical contracts. Actual
execution throughout this round was **gpt-6.1-sol, effort max**.

**Follow-up analytic continuation, 18 October 2026:** [Note 11](../notes/02_updated_research_plan/11_EFFECTIVE_NONSTATIONARY_ARITHMETIC_TAIL_20261018.md)
now supplies an effective nonstationary arithmetic tail, explicit uniform
onset and bounded retained-integral point costs; actual model
**gpt-6.1-sol, effort ultra**. The first three derivative errors are below
2e-9 G0 for all x>=1000 under its stated contour/mode rule, time and strip
domain. [Review 10](../reviews/10_EFFECTIVE_NONSTATIONARY_TAIL_AND_POINT_EVALUATOR_REVIEW_20261018.md) records same-model checks.
This is a new approximation input, not completion of the global margin.

**Latest analytic continuation:** [Note 14](../notes/02_updated_research_plan/14_SHARPER_OUTER_EXCLUSION_AND_CONSTANT_DISTANCE_CONTOURS_20261018.md)
sharpens the uniform real first-jet exterior to exp(20/epsilon), proves a
constant-distance omitted-mode theorem, and binds a partial canopy ledger.
The current slab bridge is **(1001,exp(2000)) on [1/100,1/5]**.
[Review 12](../reviews/12_OUTER_EXCLUSION_AND_CONSTANT_DISTANCE_REVIEW_20261018.md)
and the [latest ledger](../numerics/analytic_continuation/GLOBAL_ANALYTIC_CONTINUATION_LEDGER_20261018.json)
record the checks. The [separate whole-round summary](03_OVERVIEW02_ROUND_SUMMARY_20261018.md)
is additional to the final research note. This bounded continuation is
complete; the global research objective remains open. Next input: a
physical signed estimate or complete final-time complex exterior. No scan
expansion is justified.

## Existing starting evidence

This is the inherited baseline at tracker initialization. Fresh execution
and new evidence are recorded in the stage decisions below.

| Input | Recorded status and scope | Evidence |
| --- | --- | --- |
| Strengthened manuscript | Working draft with written proofs and internal LLM integration checks; no independent specialist review | [Canonical source][manuscript], [integration review][integration], [build record][build] |
| Positive carriers and arithmetic residuals | Broad strip positivity, the combined logarithmic derivative budget, the E/64 carrier payment, and real and complex residual bounds | [Note 05][note05], manuscript Sections 3–5, integration review |
| Shifted complete source approximation | Explicit arithmetic mode tail bounds for fixed derivatives; retained integral cutoff, quadrature, rounding and whole-cell errors still require an evaluator | [Note 06][note06], manuscript Section 6, [recorded scalar enclosures][constants] |
| Near-boundary contour | Asymptotic envelope-relative tail improvement; effective onset, constants and retained-mode evaluation cost remain unevaluated | Manuscript Section 6 and overview 02 |
| Bounded pilot | Overview 02 identifies an existing Investigation 22 complete-source certificate on the pilot domain; its replay and matched comparison were pending at initialization and are now recorded below | [Physical jet Note 06][baseline-note], [Review 18][baseline-review], [baseline script][baseline-script] |
| Complete theta margin and global conclusion | The global signed estimate was open at initialization and remains open; the finite D0 signed margin is now certified below, without new global coverage or a Newman bound | Integration review and overview 02 |

The build record's existing manuscript source-set SHA-256 is
`f6cd484647ef328047e9ac51a577b8260e899aecbfdd5026e9e238079feb823f`.
Stage 0 verified this source-set identity against every consumed source
file; [Review 06](../reviews/06_SOL_STRENGTHENED_MANUSCRIPT_CONTRACT_REVIEW_20261018.md) records the result. Review 04 identifies an earlier manuscript revision and must
not substitute for review of the strengthened bytes.

The [result-summary index][summaries] and [patterns-to-avoid index][avoid]
govern status and interpretation. Especially relevant are the
[collision control catalogue][controls], [target classification][target],
[premise-based screening][screening], [scoped exclusions][scope] and
[preservation of cancellations][cancellation].

## Stage status and dependencies

| Stage | Goal | Status | Dependency |
| --- | --- | --- | --- |
| 0 | Pin and review the strengthened manuscript contracts | Gate passed | First research step |
| 1 | Certify a shifted evaluator with a complete physical jet error budget | Gate passed | Stage 0 contracts accepted or repaired |
| 2 | Run the matched bounded pilot and adversarial controls | Attempt closed — performance gate failed | Stage 1 evaluator and error contract |
| 3 | Derive a cancellation-sensitive signed estimate | Gate passed — finite margin only | May begin after Stage 1 fixes the actual error scale; use Stage 2 weak cells when available |
| 4 | Select a global consumer and account for all coverage | Attempt closed — global route unclosed | Measured evaluation evidence and applicable analytic inputs from Stages 1–3 |
| 5 | Replay the selected contract and close the earned claim | Gate passed — auxiliary closure only | The selected Stage 4 contract, or a precisely scoped auxiliary outcome |

Use **Not started**, **In progress**, **Gate passed**, **Repair required**,
or **Attempt closed**. A gate passes only with linked evidence for its
acceptance conditions. An attempt closed with a scoped obstruction or
measured failure is a recorded outcome, not a positive certificate. Record
the outcome separately from the decision to continue or stop expansion.

## Stage 0 Manuscript contracts

- [x] Verify the strengthened source-set identity against the build record;
  compare the revised sources with Notes 05–06 and Reviews 04–05.
- [x] Check strip boundaries, Schwarz scaling, the combined derivative
  budget, real residual derivatives and the complex denominator lower bound.
- [x] Check the complete contour shift, finite-mode derivative conditions,
  near-boundary asymptotic, imported normalizations and theorem hypotheses.
- [x] Replay the relevant original and revised scalar checks and compare
  every printed bound with its outward enclosure. Record document build
  checks separately from mathematical and scalar checks.
- [x] Resolve defects before consuming affected statements; retain the
  distinction between an auxiliary packet error and physical field error.

**Deliverables:**
`reviews/06_SOL_STRENGTHENED_MANUSCRIPT_CONTRACT_REVIEW_20261018.md` and
`numerics/STRENGTHENED_MANUSCRIPT_REPLAY_20261018.json`, together with the
current manuscript build record.

**Acceptance gate:** every new theorem has a complete proof and explicit
domain; every printed bound has an enclosure; no claim equates
packet-relative error with physical relative error. Compilation and scalar
replay do not establish a theta margin.

**Recorded outcome, 18 October 2026:** gate passed. All eight manuscript
source hashes match the build pin, all three scalar replay outputs match
the retained bytes, and the saved project compiles. [Review 06](../reviews/06_SOL_STRENGTHENED_MANUSCRIPT_CONTRACT_REVIEW_20261018.md)
and [replay record](../numerics/STRENGTHENED_MANUSCRIPT_REPLAY_20261018.json).
Same-assistant internal review; no theta sign is inferred from scalar replay.

## Stage 1 Complete shifted evaluator

The initial evaluation domain is
\(D_0=[1/100,1/5]\times[25,45]\), with \(0\le\Im z\le1\)
for complex tests and real \(z\) for the first jet. Start with
\(m=5\), \(d=\pi/16\), rigorously enclosed and fixed throughout each cell.

- [x] Check \(b>0\), \(8\pi m^2\cos(4d)\ge T\), and geometric ratio
  below one using the actual interval parameters; reject inadmissible cells.
- [x] Derive uniform tails beyond the retained integral cutoff \(U\),
  integrate the retained range with outward rounding, and preserve both
  shifted terms and complete reflection before truncation.
- [x] Include all shift-dependent derivative factors and every extra spatial
  derivative required by time propagation through \(H_t=-H_{xx}\).
- [x] Separate mode truncation, source-integral tail, quadrature, arithmetic
  rounding and whole-cell propagation; assign margin allowances and a reserve.
- [x] Compare \(H,H_x,H_{xx}\) with complete-source enclosures on matched
  point and cell tests, using physical jet scale or an explicitly positive
  envelope. At zeros use the first jet; never assume a lower bound on \(|H|\).
- [x] Record conjugation and heat-equation diagnostics, the worst cell,
  dominant error and measured cost. The finite shifted approximant need
  not be even.

**Deliverables:**
`notes/02_updated_research_plan/07_SHIFTED_EVALUATOR_AND_COMPLETE_ERROR_BUDGET_20261018.md`,
`numerics/certify_shifted_theta_jet.py`, and
`numerics/SHIFTED_EVALUATOR_VALIDATION_20261018.json`.

**Acceptance gate:** shifted and complete-source enclosures intersect on
matched tests, and rigorous total error fits the proposed consumer's margin
allowance. If implementation error dominates, permit one documented bounded
repair and repeat the same tests. A further failure closes that implementation
attempt on its stated domain.

**Recorded outcome, 18 October 2026:** gate passed for the bounded interval
consumer. [Note 07](../notes/02_updated_research_plan/07_SHIFTED_EVALUATOR_AND_COMPLETE_ERROR_BUDGET_20261018.md)
and [validation](../numerics/SHIFTED_EVALUATOR_VALIDATION_20261018.json)
cover all errors and 128 full-time strips. The shifted added coordinate
error is below 2.751e-18 versus 4.923e-17 for the real-source comparator;
Taylor propagation dominates. Arithmetic stays inside the outward polynomial
image. No evaluator-domain repair was required. Complex point/cell tests,
ordinary-root and stationary-point diagnostics, and a separately integrated
heat derivative pass; no division by a vanishing H is used.

## Stage 2 Matched pilot and adversarial controls

- [x] Replay the existing complete-source baseline on all of \(D_0\),
  including tails, full-segment signs, wall flux and exact polygon winding.
  The historical baseline uses 234 boundary segments and 128 full-time
  interior strips sharing 76 midpoint integrals; begin at 160-bit precision.
- [x] Compare relevant original packet, complete-source and shifted
  evaluators at the same domain, conclusion, certified error and resource
  budget. Charge precomputation, derivative generation, vertices, rejected
  cells and any precision increase.
- [x] Certify a strict whole-cell first jet margin or coordinate sign;
  for winding certify every edge and its homotopy, exact degree and ordinary
  root wall flux. A complex Rouché application also needs a certified
  approximant zero count.
- [x] Complete the control challenges below with frozen source coefficients
  and source-specific error contracts. Distinguish failed theta-premise
  checks from rejection of a box containing a certified control event.
- [x] Measure gain at matched error, or test one predeclared adjoining
  region for a useful certified margin or coverage gain.

| Control | Required challenge from overview 02 | Status |
| --- | --- | --- |
| Finite-prime orbit controls | Test the missing complete normalized analytic reflection; locate and enclose an event before any numerical event test, since no effective height is supplied | Analytic premise screened; no effective event location |
| Three- and four-square controls | Replay published event enclosures; include the four-square event at \(t=1/100\), \(83.5323729<x_*<83.5323730\), in a rational surrounding box | Replayed; both event boxes rejected |
| Reflected super-Gaussian | Use a box containing \((1/4,\pi/4)\); test the missing exact normalized theta square source and its tail contract | Replayed; surrounding event box rejected |
| Smooth shape and positive primitive controls | Preserve analytic witness status and test the missing theta square-mode data; introduce no unsupported event box | Analytic witness retained; no invented event box |
| Euler-factor controls \(\Phi_{c,p}\) | Replay genuine negative-Laguerre witnesses for bound screening; distinguish witnesses from enclosed double events | Genuine witness replayed; signed gate rejected |
| Counter-kernels \(q,q_{T,a}\) | Use the proved collision or threshold contract, test the missing exact theta square source, and enclose an applicable event before a numerical event test | q analytic; qTa event enclosed and rejected |
| Smooth-density and two-channel controls | Test the proposed complete-source signed premise only within each proved control class | Scope screened; no generic extension |
| Polynomial heat events | Challenge the index, wall terms and strict-inequality interface with inexpensive actual events | Surrounding event box rejected |

**Deliverables:**
`notes/02_updated_research_plan/08_MATCHED_PILOT_AND_CONTROL_SCREEN_20261018.md`,
`numerics/SHIFTED_PILOT_COMPARISON_20261018.json`, and
`reviews/07_SOL_PILOT_AND_ADVERSARIAL_REPLAY_20261018.md`.

**Acceptance gate:** reproduce exclusion on all of \(D_0\), reject applicable
adversarial event boxes, and obtain either a factor-two reduction in total
measured cost at matched error or the predeclared adjoining-region gain.
Reproducing known coverage alone completes validation but does not justify
a large scan. Without gain, retain the measured comparison and proceed
analytically without a computational superiority claim.

**Recorded outcome, 18 October 2026:** validation passed; performance gate
failed, so this bounded attempt closes without scan expansion.
[Note 08](../notes/02_updated_research_plan/08_MATCHED_PILOT_AND_CONTROL_SCREEN_20261018.md),
[comparison](../numerics/SHIFTED_PILOT_COMPARISON_20261018.json) and
[Review 07](../reviews/07_SOL_PILOT_AND_ADVERSARIAL_REPLAY_20261018.md)
record the original 786-check baseline replay, five rejected surrounding
event boxes and the separate negative-Laguerre witness. The shifted method
cost about 1.093 seconds versus 0.660 seconds for the matched real method;
the adjoining [45,65] region's minimum-margin ratio was about 1.0000155,
below the predeclared useful gain of 1.1. A zero-centred-square library edge
case stopped the control run; the explicit outward-square repair and full
rerun are preserved in the record. This is not a general contour exclusion.

## Stage 3 Cancellation-sensitive signed estimate

- [x] Choose a compact positive-time region, preferably from Stage 2's
  weakest cells, and state the candidate theorem, hypotheses and required
  lower margin before a long derivation.
- [x] Retain complete paired modular terms, lower intervals and boundary
  contributions before estimating the signed term in
  \(\mathcal L_0=A^2(h_x^2-hh_{xx})-(\log A)_{xx}H^2\), \(h=H/A\).
  The E/64 payment already controls only the carrier term.
- [x] Run the full-carrier diagnostic \(C=\sum_{n\ge2}H_n\): removing the
  arithmetic remainder still leaves first-mode cancellation.
- [x] Compare the estimate with the actual physical jet and complete-source
  calculation; do not infer a sign from separate bounds on cancelling sectors.
- [x] For event normalization, retain \(c=H_{xx}(T,x_*)/2\), the stationary
  predecessor \(x_{\rm stat}(s)=x_*+O(s)\), restricted curvature and derivative
  hypotheses, and a separate exterior remainder for fixed imaginary shifts.
  Treat higher multiplicity and \(t\downarrow0\) as additional obligations.

**Deliverables:**
`notes/02_updated_research_plan/09_COMPLETE_MODULAR_SIGNED_ESTIMATE_20261018.md` and
`reviews/08_SOL_SIGNED_ESTIMATE_ASSESSMENT_20261018.md`, plus a compact
numerical record if used.

**Acceptance gate:** an applicable strict margin with complete error, a new
effective bound consumed by Stage 4, or a proved obstruction in a named
restricted class. Close a specified estimate that merely renames
noncollision, uses unbounded event normalization, or admits a colliding
control under every premise; record the exact missing input and scope.

**Recorded outcome, 18 October 2026:** the finite strict-margin alternative
passes on D0: Hx squared minus H Hxx is strictly greater than E/100.
[Note 09](../notes/02_updated_research_plan/09_COMPLETE_MODULAR_SIGNED_ESTIMATE_20261018.md),
[314-strip certificate](../numerics/COMPLETE_MODULAR_SIGNED_ESTIMATE_20261018.json)
and [Review 08](../reviews/08_SOL_SIGNED_ESTIMATE_ASSESSMENT_20261018.md)
record complete errors and a real-source 256-bit replay of every cell,
with raw excess above 4e-16. This quantitative finite certificate is on
already covered territory. The full-carrier algebraic diagnostic is retained;
event normalization is not used. No independently derived global arithmetic
sign mechanism, higher-multiplicity or zero-time statement is supplied.

## Stage 4 Global consumer and full coverage

**Selected complete feasible route:** none. The slab now has an effective
outer threshold exp(20/epsilon) and central coverage through 1001, but its
full finite margins/cost remain missing. The partial canopy family and
its exact remaining exterior are transcribed in Note 14. Select from measured evidence
under overview 02's normalization \(H_0(z)=\xi((1+iz)/2)/8\) and published
comparison baseline, rather than choosing a target decimal first.

- [ ] Compare the slab and canopy/barrier routes using measured margins,
  cost and missing hypotheses; select one complete consumer contract.
- [ ] For a slab route, choose \(0<\tau<0.2\); cover
  \([\tau,0.2]\times[0,X]\) and prove uniform outer exclusion for
  \(x\ge X\), including the seam and every time endpoint, before applying
  the positive-threshold finite-collision reduction to conclude \(\Lambda\le\tau\).
- [x] For a canopy/barrier route, transcribe every parameter restriction
  and region in Polymath Theorem 1.2: initial verification to \(X/2\), final
  exterior nonvanishing for \(x\ge X+\sqrt{1-y_0^2}\), and the moving
  intermediate-time barrier. Its conditional conclusion is
  \(\Lambda\le t_0+y_0^2/2\).
- [ ] Bind every region to a theorem or replayable certificate, a strict
  minimum margin and all error payments. Carry forward uncompleted producer
  obligations from any reused Newman audit package.
- [x] Evaluate the near-boundary tail's onset, constants and retained-mode
  quadrature cost before using it in the global budget. A mode count alone
  is not measured complexity.

**Deliverables:**
`notes/02_updated_research_plan/10_GLOBAL_CONSUMER_AND_COVERAGE_LEDGER_20261018.md` and
`numerics/GLOBAL_CONSUMER_BUDGET_20261018.json`.

**Acceptance gate:** one fully specified route has feasible measured finite
coverage and a proved outer contract. Otherwise record the uncovered range,
retain the strongest established auxiliary gain, and stop expansion. A
proposed global bound remains conditional until all hypotheses are met.

**Recorded outcome, 18 October 2026:** global gate unpassed; route assessment
closes with the explicit finite bridge. [Note 10](../notes/02_updated_research_plan/10_GLOBAL_CONSUMER_AND_COVERAGE_LEDGER_20261018.md)
and [budget](../numerics/GLOBAL_CONSUMER_BUDGET_20261018.json)
record the measured [25,65] finite coverage, the inherited exp(6400) outer
starting contract at the pilot time endpoint, and the uncomputed complete
bridge and seams. No feasible complete slab or canopy package is selected.
At that bounded-round close the near-boundary onset and cost were
unevaluated. Note 11 now gives explicit arithmetic-tail onset/constants
and bounded point costs; uniform consumer margins and the complete global
coverage budget remain open. Note 14 now sharpens the outer threshold to
exp(2000) at tau=1/100 and transcribes the complete canopy regions. The
transcription and bounded onset/cost tasks above are complete; actual
global coverage and route feasibility remain unchecked. Earlier table
entries retain their historical exp(6400) inventories.

## Stage 5 Replay and claim closure

- [x] Replay pinned sources and parameters adversarially; recalculate the
  weakest outward margins and check every cell, seam and equality endpoint.
- [x] Check external input hashes and rejection of malformed, missing or
  mismatched inputs; challenge strict versus non-strict comparisons.
- [x] Map each public claim to its proof, hypotheses and verified domain in
  the final claim ledger. Record actual model settings and reviewer roles;
  a separately written Sol verifier remains same-model internal review.
- [x] Update applicable status and index links and add a concise
  `DRAFT_HISTORY.md` milestone; update the relevant result summary and avoid
  entry. The manuscript sources stay at their reviewed pin; this auxiliary
  round is documented in the new notes and certificates.
- [x] Close with the exact supported outcome and remaining gap: a fully
  replayed global conclusion, or an analytic constant, validated evaluator,
  measured bounded gain or scoped obstruction.

**Deliverables:**
`reviews/09_SOL_GLOBAL_CERTIFICATE_AND_CLAIM_REVIEW_20261018.md`,
`numerics/FINAL_CLAIM_LEDGER_20261018.json`, and the applicable status and
milestone updates.

**Closure gate:** announce a new Newman bound only after the chosen full
contract is closed and replayed. Auxiliary closure must identify the
uncompleted global obligations explicitly.

**Recorded outcome, 18 October 2026:** auxiliary closure passes; global
claim closure remains unavailable. [Review 09](../reviews/09_SOL_GLOBAL_CERTIFICATE_AND_CLAIM_REVIEW_20261018.md)
and [final claim ledger](../numerics/FINAL_CLAIM_LEDGER_20261018.json)
recalculate all 314 signed strips and 128 first-jet strips at 256 bits,
check closed coverage, and pass fifteen adversarial/regression checks.
The code, records, notes, status indexes and milestone entry are saved.
Actual model throughout: gpt-6.1-sol, effort max; same-assistant internal
review only. No new Newman bound is announced.

## Follow-up finite consumer on 18 October 2026

Prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol, actual effort ultra**. This follows Note 11 rather than
repeating the original D0 pilot.

| Overview stage | Result and evidence | Decision |
| --- | --- | --- |
| 3 | [Note 12](../notes/02_updated_research_plan/12_HIGH_HEIGHT_SIGNED_CONSUMER_AND_MATCHED_COMPARISON_20261018.md) consumes the new nonstationary tail; 40 closed cells prove L0>E/100 on [1/100,1/5] × [999,1001]. Minimum excess >8.26087e-5 G0(1000)^2; component errors <4.621e-12 G0(1000). | Finite signed consumer passed. |
| 2 comparison contract | Same-domain real-source calculation at 768 bits, sharing the useful physical derivative bound. Failed quadrature tolerance attempt and single repair are charged; all 40 cells replay. Shifted 7.590s versus real 11.236s, ratio 1.480. | Factor-two speed gate failed; no general performance claim. |
| 4 finite producer | [Note 13](../notes/02_updated_research_plan/13_VERTICAL_WALL_AND_FINITE_HEIGHT_NONCOLLISION_20261018.md) certifies the full wall Re z=1000, 0<=t<=1/5, |Im z|<=1, with margin >0.00425 G0(1000). A finite propagation proof uses the published initial verification and all-multiplicity heat splitting. | E>0 for 0<t<=1/5, |x|<=1000; union with the signed box closes [1/100,1/5] × [-1001,1001]. |
| 4 global consumer | [Current ledger](../numerics/high_height_consumer/HIGH_HEIGHT_CONSUMER_LEDGER_20261018.json) replaces Note 10's old finite inventory. The inherited outer contract begins only at exp(6400). | The open bridge is (1001,exp(6400)); no complete feasible global route. |
| 5 | Fresh 256-bit midpoint integration recalculates every signed/wall cell; an independent real contour replays both consumers; exact covers, source/parameter guards, ten negative controls and the source-specific control catalogue pass. [Review 11](../reviews/11_HIGH_HEIGHT_SIGNED_AND_VERTICAL_WALL_REVIEW_20261018.md). | Finite claim closure passed, with same-model internal review only. |

The original whole-time strip attempt stopped after 40 calls through
interval dependence. Its single geometry repair used four time slabs,
76 additional calls and no new quadrature. Every coarse choice is retained.
The real comparator's finite but inaccurate enclosures were rejected;
relative tolerance zero repaired the error budget within its declared cap.
The complex wall added only one positive-majorant integral to the existing
midpoint setup. Boundary endpoints and time seams are included.

This is contiguous finite coverage, not an inference from initial zero
verification alone. The full complex wall supplies the additional input.
No all-height signed estimate, improved outer threshold or global Newman
bound is claimed. The next stage must address the remaining finite bridge
or an effective exterior mechanism before increasing the scan range.

## Final analytic continuation on 18 October 2026

Prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol, actual effort ultra**. [Note 14](../notes/02_updated_research_plan/14_SHARPER_OUTER_EXCLUSION_AND_CONSTANT_DISTANCE_CONTOURS_20261018.md)
and [Review 12](../reviews/12_OUTER_EXCLUSION_AND_CONSTANT_DISTANCE_REVIEW_20261018.md)
record the new arguments and parallel same-model checks.

- **Stage 3 analytic input:** constant-distance d=pi/8-A/x has explicit
  O(x^(-1/4)) G0 omitted-mode error. A=33, b*=1/8 gives a common bound
  below 7e-11 G0 for x>=1000, 0<=t<=1/2, |Im z|<=1, orders 0–2.
- **Stage 4 consumed exterior:** real first-jet exclusion starts at
  exp(20/epsilon), sharpening exp(64/epsilon). The exact current slab gap
  is (1001,exp(2000)), for 1/100<=t<=1/5. This real theorem does not fill
  the canopy's complex exterior.
- **Stage 4 alternative contract:** the canopy's initial verification and
  moving barrier are bound to Note 13 by choosing
  X=1000-sqrt(1-y0^2). Full final-time nonvanishing beyond x=1000 remains
  missing. A remote exact polynomial shows why finite E/wall and strip
  premises plus the global baseline cannot supply it. The polynomial
  lacks the theta source and fails the stronger D1 signed premise.
- **Feasibility decision:** the explicit retained enumeration exceeds
  10^433 modes at exp(2000). This is scoped to the present code, not all
  possible representations. No height scan is launched.
- **Stage 5 auxiliary replay:** 25 strict scalar checks and five parameter
  rejections pass; all 26 compared 192/256-bit enclosures overlap; exact
  polynomial identities and threshold brackets pass. The current finite
  certificates are inherited unchanged. Global claim closure remains open.

The separately requested [entire-round summary](03_OVERVIEW02_ROUND_SUMMARY_20261018.md)
is saved in addition to the final research note. This continuation closes
with a new effective outer input, an approximation theorem and a scoped
control. **No new Newman bound is established.**

## Evidence and update rules

After each substantive research turn, update the stage status, relevant
checkboxes and dated log below. Link actual notes, numerical records and
reviews once created; deliverable names above remain planned paths until
then. Use the plan's numbering without renumbering completed history.

Each numerical record must bind exact rational domains, source and code
hashes, library versions, actual precision and rounding, frozen \(m,d\),
integration cutoffs, derivative orders, subdivisions, failure limits and
total measured cost. Record the weakest lower margin, its complete error
payments and reserve. Retain failed cells, dominant errors and unsuccessful
parameter choices, including the one bounded Stage 1 repair if used.

Each stage decision needs the date, actual model and effort, evidence links,
review status, passed or failed conditions, exact remaining gap and next
action. Distinguish inherited evidence, fresh replay, new results and
scenarios. Do not count an RH-equivalent restatement as a milestone. If the
overview changes, record which contract changed before carrying a gate
decision forward.

Keep detailed derivations in `notes/`, computations and small records in
`numerics/`, and assessments in `reviews/`. Follow
[LARGE_FILES.md][largefiles] for external regenerable data, hashes and
regeneration guides. Keep this tracker current in place; manuscript
milestones use Git commits or tags and concise history entries.

## Dated progress log

| Date | Stage | Progress and evidence | Gate decision and next action |
| --- | --- | --- | --- |
| 18 October 2026 | Setup | Created this overview 02 tracker after reading the updated plan, manuscript sources and integration record. Recorded inherited inputs, all six stages, deliverables and control challenges. Prepared for Edward Baker with substantial LLM assistance, GPT-6.1 Sol, actual effort max. | Setup complete; no research gate passed. Next: begin Stage 0 when research execution starts. |
| 18 October 2026 | Notes home | Created notes/02_updated_research_plan at the user's request; redirected new Notes 07–10 there and retained original Notes 01–06. | Explicit overview 02 affiliation recorded. |
| 18 October 2026 | 0 | Pinned strengthened bytes; all scalar replay bytes match; proof contracts checked; successful compilation. Review 06 and manuscript replay record. | Gate passed for auxiliary contracts. |
| 18 October 2026 | 1 | Complete interval evaluator, matched real/complex tests and 128-strip pilot; Note 07 and validation record. | Gate passed for the stated finite consumer. |
| 18 October 2026 | 2 | Original winding baseline replayed; controls reject applicable event boxes; adjoining region compared; native square edge case repaired and rerun. Note 08, comparison and Review 07. | Validation passed; performance gate failed; no scan expansion. |
| 18 October 2026 | 3 | L0>E/100 on D0, with 314 cells and 256-bit real-source replay. Note 09 and Review 08. | Finite margin gate passed; global arithmetic mechanism remains open. |
| 18 October 2026 | 4 | Complete global obligations and inherited outer threshold recorded. Note 10 and global budget. | Global gate unpassed; finite bridge and feasible consumer remain missing. |
| 18 October 2026 | 5 | Full finite replay, weakest margin recalculation, fifteen negative/regression checks, status and milestone updates. Review 09 and claim ledger. | Auxiliary closure passed; no new Newman bound. |
| 18 October 2026 | 3–4 analytic continuation | Note 11 proves the nonstationary omitted-mode estimate and uniform onset; 192-bit scalar replay, 160-bit point costs at x=1000 and 10000, fresh control rejection and Review 10. Actual model gpt-6.1-sol, effort ultra. | New effective approximation input; prior performance gate remains failed, global signed margin and finite bridge open. |
| 18 October 2026 | 3–5 finite consumer | Notes 12–13: new tail consumed, 40 signed cells and seven wall cells, finite propagation to |x|<=1000 and union to 1001; fresh and real-source replays. Actual model gpt-6.1-sol, effort ultra. | Finite coverage passed; timing gate failed; bridge (1001,exp(6400)) and global bound remain open. |
| 18 October 2026 | 3–5 final analytic continuation | Note 14: exp(20/epsilon) real exterior, constant-distance tail, partial canopy contract and exact remote polynomial; fresh 192/256-bit scalar and rational replay. Actual model gpt-6.1-sol, effort ultra. | Auxiliary continuation complete; global bridge now (1001,exp(2000)). Separate entire-round summary saved; no new bound. |

[plan]: ../research-overview/02_UPDATED_RESEARCH_OVERVIEW_AND_SOL_EXECUTION_PLAN_20261018.md
[manuscript]: ../manuscript/positive_arithmetic_packets/main.tex
[integration]: ../reviews/05_UPDATED_MANUSCRIPT_INTEGRATION_REVIEW_CODEX_20261018.md
[build]: ../manuscript/positive_arithmetic_packets/BUILD_RECORD.json
[note05]: ../notes/05_COMPLEX_STRIP_CARRIERS_AND_SHARP_LOG_DERIVATIVES_CODEX_20261018.md
[note06]: ../notes/06_CANCELLATION_PRESERVING_APPROXIMATION_AND_NEWMAN_ROADMAP_CODEX_20261018.md
[constants]: ../numerics/UPDATED_MANUSCRIPT_CONSTANTS_20261018.json
[baseline-note]: ../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/06_WALL_FLUX_AND_CERTIFIED_THETA_WINDING_20261015.md
[baseline-review]: ../../../investigations-2/active/22_theta_manifold_geometry/reviews/18_SPACETIME_BOUNDARY_AND_GEOMETRIC_CONTINUATION_REVIEW_20261015.md
[baseline-script]: ../../../investigations-2/active/22_theta_manifold_geometry/numerics/check_theta_boundary_winding.py
[summaries]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[target]: ../../../../avoid/01_restating_the_target.md
[screening]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[cancellation]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[largefiles]: ../../../../LARGE_FILES.md

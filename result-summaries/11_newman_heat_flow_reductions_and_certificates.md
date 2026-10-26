# Newman heat flow: reductions, counter-kernels, finite certificates, the corrected interface, the Gomila audit

15 October 2026. Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork.

Coverage and scope revised 16 October 2026 for Edward Baker with substantial
LLM assistance: **gpt-6-astra (Codex)**, reasoning effort **ultra**.

## Summary

- **Reductions (from imported Polymath theorems).** \(\Lambda>0\) forces a
  real double zero at time \(\Lambda\); RH \(\iff\) \((H_t,H_t')\) has no
  joint real zero for any \(t>0\); for \(\varepsilon\le t\le\tfrac12\) and
  \(|x|\ge e^{64/\varepsilon}\) there is no joint zero; every fixed theta
  cutoff has a negative tail. Investigation 21 sharpens the first to the
  finite collision criterion (RH \(\iff E>0\) on \((0,\tfrac12]\times\mathbb R\))
  and proves the uniform four-jet asymptotic with strict Laguerre signs for
  \(tL\ge61/24\), \(L=\log(x/4\pi)\), with an unevaluated starting height
  \(X_*\); its explicit region needs \(tL\ge5\) and \(x\ge4\pi e^{10^9}\).
- **Counter-kernels.** \(q=\varphi''''+324\varphi\), \(\varphi=e^{-\cosh u}\),
  is positive, even and decreasing with \(0<\Lambda_q\le9/2\); \(q_{T,a}\)
  has \(J_T=2K_{iz}(1)\cos^2(az)\), so its threshold is exactly \(T\). These
  are mandatory controls for any proposed sufficient criterion.
- **Finite certificates.** For \(t\in[1/5,3/10]\): \(Q_t>1/4\) on
  \(x\in[451.9,452.5]\) and exactly one simple real zero on
  \([4005.2,4005.8]\); four windows near \(x\approx6.1\cdot10^9\)
  (\(M\in\{22066,22067,22068,22080\}\)) with no joint zero; 21's certified
  region \(|x|\le112\), \(0\le t\le\tfrac12\); 22's box
  \(t\in[0.009,0.011]\), \(x\in[28.2,28.4]\); and 22's completed winding
  certificate on \([0.01,0.2]\times[25,45]\), with 234 certified boundary
  segments, zero winding and an independent root-count check. A practical
  interior method also passes using the same inputs and errors; no general
  efficiency advantage is established. All lie inside the region
  where Polymath and Platt–Trudgian already guarantee real simple zeros, so
  they test machinery rather than add coverage.
- **Corrected Riemann–Siegel interface.** Retaining Polymath's \(C\) term
  gives residual \(\eta^*<3.135063\cdot10^{-7}\) at \(N=22066\) against
  about \(0.0096\) before, validated against the genuine \(H_t\) with gains
  of \(10^3\) to \(3\cdot10^5\): "the one substantive technical advance" of
  the collision program. The later audit scopes its failed application to
  Gomila's \(\Lambda\le0.1787854\) package: the current triangle lane cannot
  directly consume the smaller retained-\(C\) residual. Its
  \(\Delta\Lambda\approx1.2\cdot10^{-8}\) is a local, nonrigorous sensitivity
  calculation, not a universal ceiling on other lower-bound methods.
- **Gomila certificate audit (pin a74738de).** Every analytic link of
  hypotheses (ii) and (iii) checked, "No defect was found"; 32 rows
  independently certified; the OV term is padding (tail reserve 0.0395,
  not \(2.8\cdot10^{-4}\)); all 883 barrier prism gates recomputed, the
  derivative majorants tolerate an error factor \(\times1.497\); the
  sharp-weight value \(0.1745354\) is a candidate from four floating
  samples, not a bound; the 3,148,981 producer rows remain an open audit.
- **Completed elementary outer budget (21 Note 58; 22 outer Note 01).**
  The preceding convex-dyadic estimate removes one log-height factor from
  the weighted remainder on the same domain (21 Note 39). The
  carrier-to-phase error is explicitly \(409/L\), giving total error
  \(1728B_C(L)+409/L\); the sign conclusions require the stated total-error
  bound \(\le1/8\) and imported maximal-interval exponent-pair package. The later
  four-range split reduces its low-index constant by a factor exceeding
  3974. The imported constants remain unevaluated, and the sufficient
  starting heights remain astronomical; neither result closes the finite
  bridge.
- **Frontier projection — corrected status.** The earlier summary promoted
  Review 19's \(\theta/\log(X/4\pi)\) calculation and its 0.167/0.095
  projections as an "effective frontier". That description is superseded:
  these are planning scenarios requiring missing effective outer and finite
  coverage. The published certificate contract is
  \(\Lambda\le t_0+y_0^2/2\), with initial verification, exterior exclusion
  and barrier hypotheses. Review 20 records the correction; no new bound
  follows from the projections.

- **Explicit local heat count (Investigation 3/06).** For
  \(0<t\le1/2\), \(X\ge2000000\),
  \(K_t(X)\le(6/5)\log(X+2)+22\), counting complex zeros with
  multiplicity: **proved from named imports; one cross-model LLM review**.
  [Note 02](../papers/investigations-3/06_explicit_heat_zero_counts/notes/02_EXPLICIT_OFF_AXIS_COMPARISON_AND_HIGH_HEIGHT_COUNT_20261017.md),
  [Claude Review 02](../papers/investigations-3/06_explicit_heat_zero_counts/reviews/02_CROSS_MODEL_REVIEW_NOTES_01_02_AND_MANUSCRIPT_CLAUDE_20261017.md).
  The requested [round-2 continuation](../papers/investigations-3/06_explicit_heat_zero_counts/notes/round-2/README.md)
  gives \(0.9\log(X+2)+6\) for \(X\ge100000\), **proved in-note
  from named imports, same-model checks only**; no new cross-model review.
  Both regimes are now included in the [current manuscript](../papers/investigations-3/06_explicit_heat_zero_counts/manuscript/README.md),
  with the new proof retaining its same-model status.
  Neither count supplies a noncollision claim, exact integer count,
  cumulative constant or demonstrated consumer gain. Added 17 October 2026
  for Edward Baker with substantial LLM assistance, **gpt-6.1-sol, ultra**.


- **Uniform family floor and restarted comparison (Investigation 3/03).**
  For every primitive character with conductor \(q\ge10^{12}\),
  \(S_\chi(x,3,t)>6\) for every real \(x\) and \(0\le t\le1/4\),
  and \(\Lambda_\chi\le43/200=0.215\): **proved in-note from named
  imports, with Arb/exact scalar certificates and internal same-model
  checks only; specialist review outstanding**.
  [Round-two proofs](../papers/investigations-3/03_effective_outer_remainders/notes/round-2/README.md)
  close all time, height/conductor and reflected-tail ranges for this
  regime. The finite restart consumes the original positive-time floor
  without H12 for the original flow. [Review 02](../papers/investigations-3/03_effective_outer_remainders/reviews/02_UNIFORM_FLOOR_AND_RESTARTED_COMPARISON_REVIEW_CODEX_20261017.md).
  This does not certify the earlier near-threshold tables or the derivative
  circle, and the separate zeta 0.18891 result remains conditional on its
  external analytic inputs. Added 17 October 2026 for Edward Baker with
  substantial LLM assistance, **gpt-6-astra (Codex), ultra**.

- **Bounded high-height ansatz calibration (Investigation 5/01, 25 October).**
  Ansatz [Note03](../papers/investigations-5/01_heat_density_asymptotics/ansatz/notes/03_OUTER_CORRECTION_AND_SIGNED_REAL_BRIDGE_20261025.md)
  proves the first true-field gamma/heat correction on 32<=t<=33,
  with buffered jets j<=3 and direct first time error, and a corrected
  signed real-axis field comparison with O(A_o X^-1/4) error on
  |t| log(X/(4pi))<=8. Source status: “proved in-note from named classical
  inputs; same-model internal assessment only.” The formerly open complex
  remainder is now closed by [Note04](../papers/investigations-5/01_heat_density_asymptotics/ansatz/notes/04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md)
  with no epsilon loss; it proves full fixed-buffer signed field,
  jets j<=3 and direct time error through zero, with
  delta=X^-3/4 exp(t_- L_X^2/16)<=C X^-1/4 on |t|L_X<=8.
  [Assessment03](../papers/investigations-5/01_heat_density_asymptotics/ansatz/reviews/03_COMPLEX_STRIP_AND_BUFFERED_CROSSOVER_ASSESSMENT_20261025.md)
  retains same-model status. Constants/onsets are unevaluated; no fixed
  negative-time, physical-transfer or RH conclusion. [Assessment02](../papers/investigations-5/01_heat_density_asymptotics/ansatz/reviews/02_CALIBRATION_AND_REAL_BRIDGE_ASSESSMENT_20261025.md).
  Prepared for Edward Baker with LLM assistance, gpt-6.1-sol, effort ultra.

## Status

Reductions: proved (Polymath imports named). Counter-kernels: proved.
Certificate dependencies differ: the earlier approximation-based packages
retain their imported approximation/disk hypotheses; 21's finite certificate
and 22's winding pilot use direct complete-source interval integration with
explicit tails and whole-cell or boundary error bounds. Their cited reviews
record internal replays, not external specialist validation. Interface:
validated. Audit: "audited" with a cross-model review listing five
corrections and "no defect that defeats the pinned package's proposed bound".

## Caveats

The seventeen heat lifts of `newman_collisions/` each produced a
representation plus a scoped obstruction and "No scout proves a new genuine
collision exclusion"; the transport certificate is equivalent to the
first-jet test, and the stationary criteria are Laguerre's inequality. See
[`avoid/03`](../avoid/03_lifts_and_re_realizations_in_new_coordinates.md)
and [13](13_local_heat_flow_geometry_and_rh_equivalent_criteria.md).
Investigation 21 also disproves the required exact retained sign for every
fixed proportional time delay at arbitrarily high genuine theta stationary
points; this does not exclude restricted-cusp uses or bounded-loss variants.

## Reusable for

The finite collision criterion as the correct form of "RH for the heat
flow"; the counter-kernels; the corrected interface and the audit's
tolerance tables for any future certificate at height \(\sim10^{10}\); the
frontier arithmetic for judging proposals by their number.

## Where

- [Collision reductions manuscript](../papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex) (Prop "A positive threshold entails a finite collision", cor:rhcollision, cor:eventual, Prop "Every fixed theta cutoff has a negative tail", prop:kernel, the certificate appendix); [Gaussian counter-kernel note](../papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/01_analytic_gaussian/notes/1_GAUSSIAN_REDUCTION_JOINT_KERNEL_AND_POSITIVITY_OBSTRUCTION_20261010.md); [four finite windows](../papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/13_microlocal_phase_space/microlocal_coherent_currents_and_zero_atlases.tex); [sixteen-program results](../papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/notes/15_SIXTEEN_PROGRAM_INITIAL_RESULTS_AND_FIVE_PRIORITIES_20261010.md).
- Interface and reviews: [external review 12](../papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/reviews/12_EXTERNAL_REVIEW_OF_MERGED_PROJECT_CLAUDE_20261011.md), [addendum 13](../papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/reviews/13_EXTERNAL_REVIEW_ADDENDUM_NOTES_9_TO_22_CLAUDE_20261011.md).
- Audit: [README](../papers/investigations-2/newman_certificate_audit/README.md), [corrected budget benchmark](../papers/investigations-2/newman_certificate_audit/notes/2_FINITE_LANE_REPLAY_AND_CORRECTED_BUDGET_BENCHMARK_20261012.md), [cross-model review](../papers/investigations-2/newman_certificate_audit/reviews/CROSS_MODEL_REVIEW_OF_CLAUDE_AUDIT_CODEX_20261013.md).
- Investigation 21: [manuscript](../papers/investigations-2/active/21_quaternion_theta_geometry/manuscript/quaternion_theta_geometry.tex) (§3 finite collision criterion, main theorem, Proposition "An explicit outer region", Proposition "explicit sum"); [README coverage table](../papers/investigations-2/active/21_quaternion_theta_geometry/README.md).
- Frontier arithmetic and the brainstorm rules: [Review 19](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/19_PATHS_FORWARD_AFTER_THE_SECOND_ROUND_CLAUDE_20261015.md) §1; [11 October brainstorm](../papers/quasi-rh/quasi-rh-exponent-descent/brainstorm/NEW_PATHS_FORWARD_BRAINSTORM_CLAUDE_20261011.md); [cross-assessment (fact D corrected)](../papers/quasi-rh/quasi-rh-exponent-descent/brainstorm/NEW_PATHS_FORWARD_CROSS_ASSESSMENT_CLAUDE_20261011.md).

- Later finite and outer results: [21 finite-certificate review](../papers/investigations-2/active/21_quaternion_theta_geometry/reviews/19_PHASE_CONTROLLED_DELAY_AND_CUSP_EXTENSION_REVIEW_20261014.md); [21 carrier budget](../papers/investigations-2/active/21_quaternion_theta_geometry/notes/01_weighted_outer_remainders/58_EXPLICIT_CARRIER_PHASE_AND_CONDITIONAL_HEIGHT_20261015.md), [Review 33](../papers/investigations-2/active/21_quaternion_theta_geometry/reviews/33_PRIMITIVE_CIRCLE_AND_CARRIER_CONTINUATION_REVIEW_20261015.md); [22 low-index refinement](../papers/investigations-2/active/22_theta_manifold_geometry/notes/06_effective_outer_bridge/01_LOW_INDEX_BUDGET_REFINEMENT_20261015.md); [completed winding pilot and comparison](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/18_SPACETIME_BOUNDARY_AND_GEOMETRIC_CONTINUATION_REVIEW_20261015.md).
- Scope and frontier corrections: [Review 20](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/20_ADDITIONAL_PATHS_FORWARD_ASSESSMENT_CODEX_20261016.md), including the full published certificate contract and the scope of the corrected-interface audit.

- Further analytic scope: [convex-dyadic weighted remainder](../papers/investigations-2/active/21_quaternion_theta_geometry/notes/01_weighted_outer_remainders/39_CONVEX_DYADIC_WEIGHTED_REMAINDER_AUDIT_20261015.md), [Review 27](../papers/investigations-2/active/21_quaternion_theta_geometry/reviews/27_POISSON_OBSTRUCTION_AND_WEIGHTED_REMAINDER_REVIEW_20261015.md); [proportional-delay obstruction review](../papers/investigations-2/active/21_quaternion_theta_geometry/reviews/18_PROPORTIONAL_DELAY_PHASE_OBSTRUCTION_REVIEW_20261014.md).

**17 October family audit update — gpt-6-astra, max, for Edward Baker with
LLM assistance.** [Project 03 review 03](../papers/investigations-3/03_effective_outer_remainders/reviews/03_FAMILY_FLOOR_AND_RESTART_AUDIT_CODEX_20261017.md)
checked the analytic domination and intermediate-strip restart and
reproduced both scalar outputs byte for byte: “no blocking mathematical
defect found in the designated round-two family proof chain.” This is
additional same-model review. The 0.215 result retains its proved-in-note
status; the near-threshold tables and zeta consumer are not upgraded.


## Overview 02 bounded evaluator round on 18 October 2026

For Edward Baker with substantial LLM assistance, **gpt-6.1-sol, actual effort
max**. Investigation 3/11 adds a complete shifted interval evaluator and an
**interval-certified** local inequality L0>E/100 on [1/100,1/5] × [25,45].
All 314 signed strips were re-evaluated on the real source at 256 bits.
Five applicable control event boxes reject the strict interface; the Euler
negative-Laguerre witness is separately classified. Added propagation error
improves, but the measured performance gate fails. These regions were already
covered; no new global sign mechanism, collision coverage or Newman bound
is claimed. Review is same-assistant internal only. [Notes](../papers/investigations-3/11_arithmetic_collision_rigidity/notes/02_updated_research_plan/README.md),
[claim closure](../papers/investigations-3/11_arithmetic_collision_rigidity/reviews/09_SOL_GLOBAL_CERTIFICATE_AND_CLAIM_REVIEW_20261018.md).

## Arithmetic contours and finite wall consumer on 18 October 2026

For Edward Baker with substantial LLM assistance, **gpt-6.1-sol, actual
effort ultra**. Investigation 3/11 [Note 11](../papers/investigations-3/11_arithmetic_collision_rigidity/notes/02_updated_research_plan/11_EFFECTIVE_NONSTATIONARY_ARITHMETIC_TAIL_20261018.md)
is **proved in-note**, with explicit onset: nonstationary phase improves
omitted-mode error by log(x)/x; its stated rule gives j<=2 error below
2e-9 G0 for x>=1000. [Notes 12–13](../papers/investigations-3/11_arithmetic_collision_rigidity/notes/02_updated_research_plan/13_VERTICAL_WALL_AND_FINITE_HEIGHT_NONCOLLISION_20261018.md)
consume that tail in an **interval-certified** signed box and complete
vertical wall. A finite propagation proof from named published initial
verification and local heat splitting yields E>0 for 0<t<=1/5,
|x|<=1000; its union with the signed box closes
[1/100,1/5] × [-1001,1001]. Initial simplicity and a zero-velocity
bound are unnecessary. Fresh 256-bit and independent real-source replays
pass; review is internal same-model. The timing gate fails, and the
bridge (1001,exp(6400)) remains open. No new Newman bound follows.
[Review 11](../papers/investigations-3/11_arithmetic_collision_rigidity/reviews/11_HIGH_HEIGHT_SIGNED_AND_VERTICAL_WALL_REVIEW_20261018.md) and [ledger](../papers/investigations-3/11_arithmetic_collision_rigidity/numerics/high_height_consumer/HIGH_HEIGHT_CONSUMER_LEDGER_20261018.json).

## Sharper arithmetic-contour exterior on 18 October 2026

For Edward Baker with substantial LLM assistance, **gpt-6.1-sol, actual
ultra**; internal same-model review. Investigation 3/11 [Note 14](../papers/investigations-3/11_arithmetic_collision_rigidity/notes/02_updated_research_plan/14_SHARPER_OUTER_EXCLUSION_AND_CONSTANT_DISTANCE_CONTOURS_20261018.md)
is **proved in-note from named inputs**, with scalar replay: real
first-jet exclusion begins at exp(20/epsilon) for epsilon<=t<=1/2,
replacing the earlier exp(64/epsilon) inventory. Its d=pi/8-A/x contour
has explicit O(x^(-1/4)) omitted-mode error; A=33 gives <7e-11 G0 for
x>=1000 on the stated time/complex-strip domain, orders 0–2. Neither
result is a physical lower margin. An exact remote polynomial limits
finite-wall/strip/baseline inferences and fails the stronger D1 signed
premise. The current slab bridge is (1001,exp(2000)); the complex canopy
exterior remains open. No new Newman bound. [Review 12](../papers/investigations-3/11_arithmetic_collision_rigidity/reviews/12_OUTER_EXCLUSION_AND_CONSTANT_DISTANCE_REVIEW_20261018.md)
and [entire-round summary](../papers/investigations-3/11_arithmetic_collision_rigidity/research-progress/03_OVERVIEW02_ROUND_SUMMARY_20261018.md).
Earlier entries retain their original source scope; only their outer
inventory is superseded here.


**18 October 2026 — bounded S02 implementation (Investigation 3/11).**
The [opening note](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/02_cutoff_reflection/notes/01_ANALYTIC_CUTOFF_CORRECTION_AND_COMPLETE_JET_ERRORS_20261018.md)
records a complete normalized disk-error decrease from 0.887748 to
0.226300 on `[1/100,1/5] x [999,1001]`, with paid derivatives and a
separate cutoff-crossing test. Status: **proved from the imported
approximation; outward 192/256-bit checks; internal same-model review**
([review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/02_cutoff_reflection/reviews/01_CUTOFF_REFLECTION_INTERNAL_REVIEW_20261018.md)).
Earlier transport Notes 20–22 already establish the correction and jump
machinery; no superiority to their best correlated-error method, signed
lower bound or new coverage is claimed. For Edward Baker with substantial
LLM assistance, **gpt-6.1-sol, actual effort ultra**.

**25 October 2026 — bounded fixed-negative-time ansatz return.** For
Edward Baker with substantial LLM assistance, **gpt-6.1-sol, recorded
effort ultra**. [Ansatz Note05](../papers/investigations-5/01_heat_density_asymptotics/ansatz/notes/05_FIXED_NEGATIVE_TIME_REPRESENTATIONS_20261025.md)
is **proved in-note from named classical inputs; same-model internal
assessment only** on 1<=T<=2. It proves a short corrected arithmetic
model with O(|G|X^-3/4) errors, separately from a finite growing-order
representation with C E_o exp(-L_X^2/4) errors, including full fixed
buffers, spatial j<=3 and first time. Growing RS constants and all-mode
heat curvature are paid; a bounded correction integral remains. The
source states: “FN5 is the short natural-scale result; FN26 is a different,
more elaborate outer-scale representation.” No numerical onset, useful
cost, correction dominance, physical transfer or all-time theorem.
[Assessment04](../papers/investigations-5/01_heat_density_asymptotics/ansatz/reviews/04_FIXED_NEGATIVE_TIME_ASSESSMENT_20261025.md)
records the review scope; HDA-A02 remains Partial.

**25 October 2026 — negative bridge and paid time join.** For Edward
Baker with substantial LLM assistance, **gpt-6.1-sol, recorded effort
ultra**. [Ansatz Note06](../papers/investigations-5/01_heat_density_asymptotics/ansatz/notes/06_NEGATIVE_BRIDGE_AND_TIME_JOIN_20261025.md)
is **proved in-note from named inputs; same-model internal assessment
only**. It extends Note05's unchanged finite representation to
4/L_X<=T<=2 with E_o exp(-L_X^2/4) errors and pays a time-only join
to Note04 on [-2,0]. Spatial j<=3 errors are C E_o X^-1/4 Lambda_X^j,
first time C E_o X^-1/4 Lambda_X^2, and actual heat residual
C E_o X^-1/4 Lambda_X. The residual vanishes above T L_X=8 but
persists near zero. Source: “The domain constraint `T>=4/L` is not
differentiated.” No numerical onset, useful cost, physical transfer or
all-time theorem. [Assessment05](../papers/investigations-5/01_heat_density_asymptotics/ansatz/reviews/05_NEGATIVE_BRIDGE_AND_TIME_JOIN_ASSESSMENT_20261025.md)
records scope; [Note07](../papers/investigations-5/01_heat_density_asymptotics/ansatz/notes/07_CHAT0001_RESEARCH_SUMMARY_20261025.md)
summarizes the chat. HDA-A02 remains Partial.


**25 October 2026 — ansatz manuscript integration (no new estimate).**
For Edward Baker with LLM assistance, **gpt-6-astra, recorded effort max**.
[Note09](../papers/investigations-5/01_heat_density_asymptotics/ansatz/notes/09_EVOLUTION_MANUSCRIPT_AND_PRIORITY_REVISION_20261025.md)
records: “The rewrite adds no accepted asymptotic bound.” It integrates
exact error and observable forcing identities and prioritizes controlled
all-time large-height estimates. Notes03--06 retain the statuses above;
[Progress02](../papers/investigations-5/01_heat_density_asymptotics/ansatz/research-progress/02_EVOLUTION_ASYMPTOTICS_RESEARCH_PROGRESS_20261025.md)
is the current branch ledger. This is a navigation/status update only.


**25 October 2026 — fixed-order negative-time evolution correction (5/01 ansatz).**
For Edward Baker with LLM assistance, **gpt-6.1-sol, ultra**.
[Note10](../papers/investigations-5/01_heat_density_asymptotics/ansatz/notes/10_FIRST_NEGATIVE_TIME_EVOLUTION_CORRECTION_20261025.md)
is “proved in-note from named classical inputs; same-model internal
analytical assessment only.” On 1<=T=-t<=2, one evaluated quadratic
mode correction plus K=1 RS/exact-transfer bounded integral gives
C |G|X^-5/4 field/j<=3/time and C |G|X^-7/4 residual/residual_z.
All N modes remain; an integral-free short formula and physical transfer
are open. The outer allowance X^-5/4 exp(TL²/16) still grows, without
being an actual error lower bound. [Assessment07](../papers/investigations-5/01_heat_density_asymptotics/ansatz/reviews/07_FIRST_NEGATIVE_CORRECTION_ASSESSMENT_20261025.md).

AN04 integrates that same bounded result into maintained manuscript
Section6.3, Proposition6.1; [Note11](../papers/investigations-5/01_heat_density_asymptotics/ansatz/notes/11_AN04_MANUSCRIPT_INTEGRATION_20261025.md)
and [Assessment08](../papers/investigations-5/01_heat_density_asymptotics/ansatz/reviews/08_AN04_MANUSCRIPT_INTEGRATION_ASSESSMENT_20261025.md)
record production and same-model fidelity checks. No new estimate or
mathematical review-status promotion. 25 October 2026, gpt-6.1-sol, ultra.


**25 October 2026 — fixed compact-negative-time family (5/01 ansatz).**
For Edward Baker with LLM assistance, **gpt-6.1-sol, ultra**.
[Note12](../papers/investigations-5/01_heat_density_asymptotics/ansatz/notes/12_COMPACT_NEGATIVE_TIME_FAMILY_20261025.md)
is “proved in-note from the named classical inputs of Notes05/10;
same-model internal analytical assessment only.” Every declared fixed
0<tau<=T<=B has C(tau,B,r,b)|G|X^-5/4 field/j<=3/time and
C(tau,B,r,b)|G|X^-7/4 residual/residual_z, with explicit endpoint
factors and sufficient onsets. All modes and the bounded RS integral
remain. Constants degenerate at zero/infinite endpoints, and outer
allowances still grow at fixed T. No through-zero/growing-time or
physical-transfer theorem. [Assessment09](../papers/investigations-5/01_heat_density_asymptotics/ansatz/reviews/09_COMPACT_NEGATIVE_FAMILY_ASSESSMENT_20261025.md).


25 October 2026, Edward Baker with substantial LLM assistance,
**gpt-6.1-sol, ultra**: [AN06 Note13](../papers/investigations-5/01_heat_density_asymptotics/ansatz/notes/13_AN06_MANUSCRIPT_INTEGRATION_20261025.md)
records faithful integration of Note12/Review09 as manuscript
Proposition6.2 and explicit endpoint/onset Appendix A: “no new
mathematical estimate or review-status promotion.” The 33-page clean
build is production evidence. [Whole-chat summary](../papers/investigations-5/01_heat_density_asymptotics/ansatz/notes/14_CHAT0003_RESEARCH_SUMMARY_20261025.md)
collects AN03--AN06, retained integral/outer loss and unpaid physical
consumer. A02 Partial and parent statuses unchanged; A08-AN01 is
prepared only for [1/2,1].


**26 October 2026 — recurrence fixed-order/compact-family comparison (5/01).**
For Edward Baker with substantial LLM assistance, actual **gpt-6.1-sol,
ultra**. [Recurrence Note02](../papers/investigations-5/01_heat_density_asymptotics/recurrence/notes/02_FIRST_FINITE_FLUCTUATION_COMPARISON_20261026.md),
[Note03](../papers/investigations-5/01_heat_density_asymptotics/recurrence/notes/03_FIXED_ORDER_FLUCTUATION_HIERARCHY_20261026.md)
and [Note04](../papers/investigations-5/01_heat_density_asymptotics/recurrence/notes/04_COMPACT_TIME_RECURRENCE_FAMILY_20261026.md)
are **proved in-note from named classical inputs; same-model internal
assessments only**. Every fixed p>=1 with K=2p has natural-scale
C(p,tau,B,r,b)|G|X^-(p+3/4) field/spatial-through-three/direct-time
error on declared fixed 0<tau<=T=-t<=B; p=2,K=4 gives X^-11/4 on [1,2].
No logarithmic loss. Explicit weighted remainder, full X^1/4 population,
real initial RS mismatch, true/artificial tails and endpoint/onset costs
are paid. The frozen residual and residual_z vanish exactly. All N modes
and the bounded completion integral remain. Source limit: “The quantifiers
are fixed p, then sufficiently large X.” [Review03](../papers/investigations-5/01_heat_density_asymptotics/recurrence/reviews/03_COMPACT_TIME_RECURRENCE_ASSESSMENT_20261026.md)
links the sequence and scope. No growing-order, endpoint-uniform, useful
cost, physical-transfer or RH result; HDA-A02 and parent statuses unchanged.


**26 October 2026 — controlled fluctuation-order growth (5/01 recurrence).**
For Edward Baker with substantial LLM assistance, actual **gpt-6.1-sol,
ultra**. [Recurrence Note05](../papers/investigations-5/01_heat_density_asymptotics/recurrence/notes/05_CONTROLLED_ORDER_GROWTH_AUDIT_20261026.md)
is **proved in-note from named inputs; same-model internal analytical
assessment only**, with [Review04](../papers/investigations-5/01_heat_density_asymptotics/recurrence/reviews/04_CONTROLLED_ORDER_GROWTH_ASSESSMENT_20261026.md).
The actual Bell/moment/RS costs have logarithms O((p+1)log(p+2)), and
unabsorbed tails/common onsets give a simultaneous ledger for each fixed
finite c>0,1<=p<=cL,K=2p on full buffered [1,2]. Chosen p=floor(L/2)
pays e^-L²/4 outer-envelope field/spatial-through-three/first-time error.
All N modes, exact transfer and bounded RS integral remain; residual and
residual_z are zero on frozen charts. Source limit: “An upper order cap
alone does not promise outer decay.” The full strict rate range and
fixed-theta tail costs are in the note. Formal scalar arithmetic
O(p³+Np) excludes providers/integral/precision/bit costs. Broad R05
remains Partial; no evaluator, growing-time, physical-transfer or RH
result. Earlier fixed-p statements keep their original scope.

**26 October 2026 — conditional recurrence evaluation-error specification.**
For Edward Baker with substantial LLM assistance, actual **gpt-6.1-sol,
ultra**. [Recurrence Note06](../papers/investigations-5/01_heat_density_asymptotics/recurrence/notes/06_COEFFICIENT_ROUNDING_AND_RS_QUADRATURE_20261026.md)
contains **proved deterministic bounds and a conditional evaluator
accuracy specification**, with [same-model internal Review05](../papers/investigations-5/01_heat_density_asymptotics/recurrence/reviews/05_EVALUATION_ERROR_ASSESSMENT_20261026.md).
At p=floor(L/2),K=2p, full-buffer [1,2], explicit coefficient/carrier,
scale, rounding, RS-data and geometry budgets suffice for e^-L²/4 total
outer error. Derived coefficient regularity and analytic Gauss bounds pay
O(L²) nodes per branch, at most two. All N modes and the real bounded
integral remain. Requested accuracy 3L²/(8log2)+O(Llog L) bits is under
certified data/rounding contracts; formal RS-only O(L^5) excludes provider
bit costs. Source limit: “No concrete library or implemented evaluator
has been verified here”. Broad R05 Partial at certified primitive/scale,
Gauss geometry and frozen descriptor handling; no runtime, RH or physical
transfer conclusion. Earlier exact residual statements do not certify
independently rounded channel outputs.

**26 October 2026 — recurrence analytical manuscript integration.**
For Edward Baker with substantial LLM assistance, **gpt-6-astra, max**.
The [manuscript](../papers/investigations-5/01_heat_density_asymptotics/recurrence/manuscript/main.tex)
systematically derives the saved comparison, growing-order and conditional
evaluation results and explains the preceding simplest/higher approximations.
Its [same-session authoring assessment](../papers/investigations-5/01_heat_density_asymptotics/recurrence/reviews/06_MANUSCRIPT_INTEGRATION_ASSESSMENT_20261026.md)
states: “Manuscript integration preserves the existing analytical scopes;
it does not close the concrete-provider task.” Broad R05 remains Partial;
this is source integration, not a new theorem or independent validation.

**26 October 2026 — finite recurrence provider algorithms.**
For Edward Baker with substantial LLM assistance, actual **gpt-6.1-sol,
ultra**, recurrence chat0003. [Note09](../papers/investigations-5/01_heat_density_asymptotics/recurrence/notes/09_FINITE_PROVIDER_ALGORITHMS_20261026.md)
is **proved in-note from the named inputs**, with
[same-model internal Review07](../papers/investigations-5/01_heat_density_asymptotics/recurrence/reviews/07_FINITE_PROVIDER_ALGORITHM_ASSESSMENT_20261026.md).
It supplies every Note06 scalar/gamma, scale, Gauss/RS and geometry
provider on certified dyadic-center/rational-query inputs, retaining all
N modes, integral, buffers and channels. Source limit: “The algorithms
are specified analytically”. Explicit tails and finite error tests prove
termination; the deliberately expensive gamma/root constructions supply
no useful runtime or software certificate. Note06's named provider gap
is superseded at this algorithm-existence scope only; its delivered-bit
specification remains distinct from provider internal precision. Inherited
calibrations/onsets and source assumptions remain. Broad R05 Partial;
no specialist validation, RH or physical-transfer conclusion.

**26 October 2026 — polynomial recurrence providers and conditional total cost.**
For Edward Baker with substantial LLM assistance, **gpt-6.1-sol, ultra**,
chat0003. [Note10](../papers/investigations-5/01_heat_density_asymptotics/recurrence/notes/10_EFFICIENT_PROVIDERS_AND_TOTAL_COST_20261026.md)
is **proved in-note from named inputs**, with
[same-model Review08](../papers/investigations-5/01_heat_density_asymptotics/recurrence/reviews/08_EFFICIENT_PROVIDER_AND_COST_ASSESSMENT_20261026.md).
Shifted Stirling jets and exact Legendre variation counting supersede
Note09's deliberately slow provider costs, preserving its exact-input
class, complete N-mode population and RS integral. Effective sufficient
bounds are C(N+1)Q^40 bit work and CQ^20 streamed storage for fixed
chart/valid calibration data. C21 gives an all-height onset in those
data, accounting for p-floor jumps. Source limit: “No universal numerical
X0 is claimed.” Actual uniform constant/domain/onset values remain
uninstantiated. No useful measured runtime, implemented evaluator,
software/specialist certificate or RH/physical-transfer conclusion.
Broad R05 Partial; older provider-existence results retain their scopes.

**26 October 2026 — explicit recurrence calibration and all-height onset.**
For Edward Baker with substantial LLM assistance, **gpt-6.1-sol, ultra**,
chat0003. [Note11](../papers/investigations-5/01_heat_density_asymptotics/recurrence/notes/11_EXPLICIT_CALIBRATION_AND_HEIGHT_ONSET_20261026.md)
is **proved in-note from named inputs**, with
[same-model internal Review09](../papers/investigations-5/01_heat_density_asymptotics/recurrence/reviews/09_EXPLICIT_CALIBRATION_ASSESSMENT_20261026.md).
It supplies rational uniform gamma/source/chart/envelope constants with
actual domains and L_*=2^22(ceil(r+b+2)+1)^4, X_*=2^(2L_*+8), sufficient
for every accepted P1 center above that height, retaining all floor jumps,
buffers, modes and the RS integral. Note10's formerly symbolic calibration
dependency is superseded at this scope. Source limit: “This is a
chart-dependent explicit sufficient height, not a useful-runtime claim.”
AN05 CLOSED, broad R05 Partial at concrete evaluator implementation and
certification; no numerical campaign, independent specialist review,
RH or physical-transfer conclusion. Manuscript integration pending.

**26 October 2026 — finite recurrence gamma/Gauss software replay.**
For Edward Baker with LLM assistance, **gpt-6.1-sol, ultra**, chat0003.
[Note12](../papers/investigations-5/01_heat_density_asymptotics/recurrence/notes/12_PROVIDER_IMPLEMENTATION_REPLAY_20261026.md)
and [same-model internal Review10](../papers/investigations-5/01_heat_density_asymptotics/recurrence/reviews/10_PROVIDER_REPLAY_ASSESSMENT_20261026.md)
accept all36 gamma cases/156 normalized jets and15 Gauss bases/45 maps
as **finite component provider evidence**. Final51-certificate hash-bound
archive replay passes;558 moment checks and ten altered-data rejection
controls pass. Initial OSlimit-setup failure is preserved; after runner
repair no matrix delivery fails. Source limit: “This is a bounded component
implementation and finite certificate replay”. Actual computation below
50.4055seconds, peak primary-run child RSS about19.5MiB; no asymptotic
performance law or complete field evaluator. N01 CLOSED; broad R05
Partial at remaining providers/evaluator. [Whole-chat summary](../papers/investigations-5/01_heat_density_asymptotics/recurrence/notes/13_CHAT0003_RESULTS_SUMMARY_20261026.md)
collects AN03--AN05/N01. No RH/physical result or specialist validation.

**26 October 2026 — effective recurrence manuscript integration.**
Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra,
recorded effort max**, recurrence chat0005. The [maintained manuscript](../papers/investigations-5/01_heat_density_asymptotics/recurrence/manuscript/main.tex)
now incorporates Notes09–11, joining finite provider constructions,
explicit calibration/onset and full-population bit bounds to the earlier
hierarchy and error budget. [Integration Note14](../papers/investigations-5/01_heat_density_asymptotics/recurrence/notes/14_EFFECTIVE_MANUSCRIPT_INTEGRATION_20261026.md)
states: “No new analytical theorem or independent specialist validation
is claimed.” [Review11](../papers/investigations-5/01_heat_density_asymptotics/recurrence/reviews/11_EFFECTIVE_MANUSCRIPT_INTEGRATION_ASSESSMENT_20261026.md)
is a same-session authoring assessment. Earlier pending-integration
statements are superseded only as manuscript status; analytical sources
retain their scopes. Broad R05 remains Partial. [Continuation Note15](../papers/investigations-5/01_heat_density_asymptotics/recurrence/notes/15_ANALYTIC_STRENGTHENING_CONTINUATION_20261026.md)
prioritizes a sharper all-height proof; numerical work remains supporting.

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

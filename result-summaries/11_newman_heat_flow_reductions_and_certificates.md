# Newman heat flow: reductions, counter-kernels, finite certificates, the corrected interface, the Gomila audit

15 October 2026. Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork.

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
  \(t\in[0.009,0.011]\), \(x\in[28.2,28.4]\). All lie inside the region
  where Polymath and Platt–Trudgian already guarantee real simple zeros, so
  they test machinery rather than add coverage.
- **Corrected Riemann–Siegel interface.** Retaining Polymath's \(C\) term
  gives residual \(\eta^*<3.135063\cdot10^{-7}\) at \(N=22066\) against
  about \(0.0096\) before, validated against the genuine \(H_t\) with gains
  of \(10^3\) to \(3\cdot10^5\): "the one substantive technical advance" of
  the collision program. On Gomila's \(\Lambda\le0.1787854\) package it
  "cannot be used at all", and the possible gain is \(\Delta\Lambda\approx1.2\cdot10^{-8}\).
- **Gomila certificate audit (pin a74738de).** Every analytic link of
  hypotheses (ii) and (iii) checked, "No defect was found"; 32 rows
  independently certified; the OV term is padding (tail reserve 0.0395,
  not \(2.8\cdot10^{-4}\)); all 883 barrier prism gates recomputed, the
  derivative majorants tolerate an error factor \(\times1.497\); the
  sharp-weight value \(0.1745354\) is a candidate from four floating
  samples, not a bound; the 3,148,981 producer rows remain an open audit.
- **The effective frontier.** With verification height \(X\) (in
  \(x\)-units, twice the height) and an effective outer threshold
  \(\theta\), \(\Lambda\le\theta/\log(X/4\pi)\): \(0.167\) for Polymath's
  constants at \(X=6\cdot10^{12}\), \(0.095\) for \(61/24\) if its constants
  were of order one; the present explicit constants are six orders of
  magnitude in \(L\) from that regime (Review 19).

## Status

Reductions: proved (Polymath imports named). Counter-kernels: proved.
Certificates: certified but conditional on the imported approximation and
disk inputs; replayed independently in the cross-model reviews. Interface:
validated. Audit: "audited" with a cross-model review listing five
corrections and "no defect that defeats the pinned package's proposed bound".

## Caveats

The seventeen heat lifts of `newman_collisions/` each produced a
representation plus a scoped obstruction and "No scout proves a new genuine
collision exclusion"; the transport certificate is equivalent to the
first-jet test, and the stationary criteria are Laguerre's inequality. See
[`avoid/03`](../avoid/03_lifts_and_re_realizations_in_new_coordinates.md)
and [13](13_local_heat_flow_geometry_and_rh_equivalent_criteria.md).

## Reusable for

The finite collision criterion as the correct form of "RH for the heat
flow"; the counter-kernels; the corrected interface and the audit's
tolerance tables for any future certificate at height \(\sim10^{10}\); the
frontier arithmetic for judging proposals by their number.

## Where

- [Collision reductions manuscript](../papers/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex) (Prop "A positive threshold entails a finite collision", cor:rhcollision, cor:eventual, Prop "Every fixed theta cutoff has a negative tail", prop:kernel, the certificate appendix); [Gaussian counter-kernel note](../papers/quasi-rh-exponent-descent/newman_collisions/01_analytic_gaussian/notes/1_GAUSSIAN_REDUCTION_JOINT_KERNEL_AND_POSITIVITY_OBSTRUCTION_20261010.md); [four finite windows](../papers/quasi-rh-exponent-descent/newman_collisions/13_microlocal_phase_space/microlocal_coherent_currents_and_zero_atlases.tex); [sixteen-program results](../papers/quasi-rh-exponent-descent/newman_collisions/notes/15_SIXTEEN_PROGRAM_INITIAL_RESULTS_AND_FIVE_PRIORITIES_20261010.md).
- Interface and reviews: [external review 12](../papers/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/reviews/12_EXTERNAL_REVIEW_OF_MERGED_PROJECT_CLAUDE_20261011.md), [addendum 13](../papers/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/reviews/13_EXTERNAL_REVIEW_ADDENDUM_NOTES_9_TO_22_CLAUDE_20261011.md).
- Audit: [README](../papers/investigations-2/newman_certificate_audit/README.md), [corrected budget benchmark](../papers/investigations-2/newman_certificate_audit/notes/2_FINITE_LANE_REPLAY_AND_CORRECTED_BUDGET_BENCHMARK_20261012.md), [cross-model review](../papers/investigations-2/newman_certificate_audit/reviews/CROSS_MODEL_REVIEW_OF_CLAUDE_AUDIT_CODEX_20261013.md).
- Investigation 21: [manuscript](../papers/investigations-2/active/21_quaternion_theta_geometry/manuscript/quaternion_theta_geometry.tex) (§3 finite collision criterion, main theorem, Proposition "An explicit outer region", Proposition "explicit sum"); [README coverage table](../papers/investigations-2/active/21_quaternion_theta_geometry/README.md).
- Frontier arithmetic and the brainstorm rules: [Review 19](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/19_PATHS_FORWARD_AFTER_THE_SECOND_ROUND_CLAUDE_20261015.md) §1; [11 October brainstorm](../papers/quasi-rh-exponent-descent/brainstorm/NEW_PATHS_FORWARD_BRAINSTORM_CLAUDE_20261011.md); [cross-assessment (fact D corrected)](../papers/quasi-rh-exponent-descent/brainstorm/NEW_PATHS_FORWARD_CROSS_ASSESSMENT_CLAUDE_20261011.md).

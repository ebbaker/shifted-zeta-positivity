# Collision controls and the screening they impose

15 October 2026. Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork.

Coverage and scope revised 16 October 2026 for Edward Baker with substantial
LLM assistance: **gpt-6-astra (Codex)**, reasoning effort **ultra**.

## Summary

The controls are the most distinctive product of the second portfolio:
explicit sources that share named properties with the theta source and
nevertheless collide at positive heat time, so that any argument using
only those properties proves a false statement.

- **Euler-factor controls (Investigation 19).**
  \(\Phi_{c,p}=\Phi+\tfrac c2[\Phi(\cdot+a)+\Phi(\cdot-a)]\), \(a=\tfrac12\log p\).
  It is positive and even; \(H^{c,p}_0=H_0(1+c\cos ax)\) has, for
  \(0<c<1\), the same real zeros as \(H_0\); its Dirichlet series
  \(\zeta(s)(1+(2\sqrt p/c)p^{-s}+p^{1-2s})\) lies in the extended Selberg
  class with conductor \(p^2\), tempered iff \(c\ge1\); for \(c\ge1\),
  \(\Lambda_{c,p}\le0\iff\)RH, and for \(0<c<1\), \(0<\Lambda_{c,p}\le\max(1,\delta)^2/2\).
  Exact flow: \(H^{c,p}_t(z)=H_t(z)+\tfrac c2e^{ta^2}[e^{-iaz}H_t(z+2ita)+e^{iaz}H_t(z-2ita)]\).
  Witness: one real \(x_0\) with \(\mathcal L_0(H^{c,p}_t;x_0)<0\) proves
  \(\Lambda_{c,p}>t\). Certified: \(\Lambda_{1/2,p}>0.2\) for every prime
  \(p\le41\), \(>0.1787854\) for \(p\in\{43,47\}\), by two programs sharing
  no code. Asymptotic: \(\Lambda_{c,p}>t_m-S_2t_m^2-Q a^{-6}\) with explicit
  \(Q\), \(t_m=4\log(1/c)/(\log p)^2\). Screening corollary: a property
  list satisfied by some \(\Phi_{1/2,p}\), \(p\le41\), cannot imply
  \(\Lambda\le0.2\). Shared properties S1–S5 and unshared D1–D3 are listed
  in the manuscript; the controls fail direct evaluation already at height
  \(\pi/a\le9.1\).
- **Weighted-square controls (Investigation 22).** Three positive weights
  on the first three square nodes give a source positive on the half-line,
  satisfying every support-only moment and localizing inequality and the
  first reflection endpoint \(\Phi'(0)=0\), with a nondegenerate collision at
  \(T=1/4\), \(x_*\in(44.1303,44.1304)\); a four-square control at
  \(T=1/100\), \(x_*\approx83.5324\), matches two reflection endpoints and
  three primitive endpoints. Both validated with Arb and reproduced
  independently with mpmath.
- **Reflected super-Gaussian control.** \(\Phi_*=c\,e^{-u^2/4}g(u)\) with
  \(g\) built from \(e^{-u^4}\): strictly positive, even, entire, all odd
  primitive endpoints \(-\tfrac12\), every Fourier–Gram form positive, and
  an exact collision \(H_*(1/4,\pi/4)=H_{*,x}=0\) with \(H_{*,xx}>0\).
- **Smooth shape and positive-primitive controls (21 Notes 53, 56).**
  A smooth positive even source with double-exponential decay and strong
  log-concavity still has a positive-time collision. A strengthened normalized
  construction has a primitive transform positive for all real \(x\) and
  \(0\le t\le1/2\), the same reconstruction constant \(1/2\), even completed
  primitive, and every algebraic spectral asymptotic coefficient of the
  theta primitive, yet collides at \(0<T<1/2\). These are analytic
  constructions for sufficiently small positive damping, not a numerical
  damping certificate. The endpoint data do not impose theta's arithmetic
  square expansion. They screen the positive auxiliary channel in [14](14_theta_identities_and_arithmetic_bookkeeping.md).
- **Reflection rigidity.** Within polynomially weighted integer-square
  combs, full source reflection plus the normalized endpoint forces
  \(a_n\equiv1\): the conjunction of square support and reflection is the
  theta source itself.
- **The four-family comparison in Reply 18.** Within that table,
  \(\{A,B\}\) have square support without full reflection and
  \(\{C,D\}\) full reflection without integer-square support. No one listed
  property is absent from all four. The complete normalized source and
  suitable direct quantitative information can distinguish the genuine
  theta application; different controls may fail different premises.

- **Finite-source measurement audit (Investigation 3/07, 17 October).**
  Every nonzero finite theta-tail change whose resulting source is
  nonnegative, and every nonzero nonnegative finite zero-tail source, has finitely many real and infinitely
  many non-real zeros at every real heat time. This is an endpoint/growth
  obstruction, not a statement about theta. The weighted-square controls
  therefore have no all-real heat time either; their certified event times
  are not finite upper thresholds. The prescribed-point distance tables
  need their location qualifier. The gap-alignment lemma retains a
  nonvertical top-vector hypothesis; one positive \(N=6\) alignment is now
  interval-certified. The new one-direction theorem gives nondegenerate
  events inside every sufficiently high gap at each fixed \(t_*>0\), using
  Polymath's eventual real/simple zeros; its cutoff depends on time. Source status:
  **proved in-note**; central endpoint/gap findings have cross-model LLM
  review, the later one-direction proof has same-model checks only;
  **no specialist review**. [Round-two sources and certificates](../papers/investigations-3/07_source_measurement_audit/notes/round-2/README.md),
  [Claude assessment](../papers/investigations-3/07_source_measurement_audit/reviews/01_ROUND_ONE_CROSS_MODEL_REVIEW_CLAUDE_20261017.md).
  Added for Edward Baker with substantial LLM assistance, **gpt-6.1-sol**,
  effort **ultra**.

- **Finite-prime orbit controls (Investigation 3/11, 18 October).** For any
  fixed finite prime set, finite coefficient prefix and finite list of real
  linear measurements, a bounded positive square-source perturbation can
  preserve every selected-prime identity and the primitive normalization,
  match those measurements, and have a nondegenerate double event in each
  sufficiently high theta-zero gap at a fixed positive time (with a different
  frozen multiplier for each event). Coefficient and heat-weighted source
  distances tend to zero. Full source reflection fails; no fixed compact
  event location, finite Newman threshold, or obstruction to infinite
  assembly is claimed. Status: **proved in-note**, extending the existing
  one-direction gap argument; one orbit endpoint construction is
  **interval-certified**. [Proof](../papers/investigations-3/11_arithmetic_collision_rigidity/notes/03_FINITE_PRIME_COMPATIBLE_COLLISION_CONTROLS_CODEX_20261018.md),
  [same-assistant assessment](../papers/investigations-3/11_arithmetic_collision_rigidity/reviews/01_OPENING_ROUND_SELF_REVIEW_CODEX_20261018.md).
  Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra,
  effort max**; no independent review or theta sign claim.
  The [working manuscript, Section 5](../papers/investigations-3/11_arithmetic_collision_rigidity/manuscript/positive_arithmetic_packets/sections/05_controls.tex)
  gives the self-contained proof for 0<T<=1/2 and shows that the positive
  carrier bounds survive with arbitrarily close constants. Its published
  high-zero input is stated explicitly; review remains same-assistant.

- **BW-01 fixed-event positive-source control (3/13, 20 October).**
  **Proved in-note; separate same-model internal review:** a normalized
  three-atom source has actual all-real threshold T, an exact double event
  at fixed a=20, uniform complete moment bounds, and passes the selected
  imaginary-axis floors at b=20 and b=40. Its exact critical-value pair
  remains negative and normalized curvature diverges negatively along
  the family. “This is not an obstruction to estimates using the unchanged
  complete theta source.” It is atomic, has infinitely many simultaneous
  threshold events, and fails theta's eventual simplicity there and the
  full imaginary-axis profile. [Proof](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/01_local_double_winding/notes/04_EVENT_CONDITIONED_POSITIVE_SOURCE_OBSTRUCTION_20261020.md),
  [review](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/01_local_double_winding/reviews/02_EVENT_CONDITIONED_SOURCE_REVIEW_20261020.md).
  Prepared for Edward Baker with substantial LLM assistance, gpt-6-astra,
  ultra. No theta exclusion or specialist review.


- **Exact finite-profile threshold controls (3/13, 20 October).**
  **Proved in-note; separate same-model internal review:** for any
  prescribed finite observation heights, a constructed profile vector
  stays exact along a positive finite-atom threshold family with fixed
  event height, normalization and common complete moments, while the
  normalized deflated jet diverges. A fixed triangular convolution
  extends this to continuous compact sources. “None of these statements
  says that the actual theta profile at a specified time admits a collision”
  is the source's explicit qualification.
  The controls fail unchanged theta coefficients, full profile growth
  and eventual simplicity at the threshold. [Profile proof](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/08_deflated_jet_hierarchy/notes/05_FINITE_PROFILE_CONDITIONING_OBSTRUCTIONS_20261020.md),
  [review](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/08_deflated_jet_hierarchy/reviews/03_FINITE_PROFILE_CONDITIONING_REVIEW_20261020.md), and
  [continuous-source extension](../papers/investigations-3/13_contradiction_analysis/02_threshold_jet_sign/notes/03_POSITIVE_MULTIPLIER_GRAM_EXTENSION_20261020.md).
  Prepared for Edward Baker with substantial LLM assistance,
  gpt-6-astra, ultra; no theta exclusion or specialist review.


- **RH-conditional normalized endpoint control (BW-10, 20 October).**
  Under RH, [Note 05](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/05_CLOSE_POSITIVE_SOURCES_AND_NORMALIZED_DOUBLE_ZEROS_20261020.md) proves that positive even sources can be
  arbitrarily close to theta in uniform relative norm, preserve its
  leading tail, functional equation, displayed completion and pole residue
  one, yet have exact double zeros at time zero and simple all-real zeros
  for positive time. The added doubles escape to infinity. “The perturbed
  functions fail ordinary Dirichlet series arithmetic.” A separate
  polynomial control retains fixed slack below theta's strong
  log-concavity floor; do not combine the preservation lists. [Separate
  same-model internal review](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/reviews/05_SOURCE_CONTROL_AND_SHIFT_AUDIT_20261020.md); no original theta zero is excluded.
  Added for Edward Baker with substantial LLM assistance, **gpt-6-astra,
  effort ultra**; no specialist review or priority claim.

## Status

19: proved and certified; the manuscript "awaits independent review" and
its tracked \(T_0\) table is not a bound (\(\Lambda\le T_0\) is explicitly
not proved). 22's weighted-square controls: validated (python-flint),
hand-verified and reproduced. Reflected control and rigidity: proved.
21's smooth/primitive controls: analytic proofs and internal reviews;
finite algebra checks do not certify the implicit damping threshold.

## Caveats

The screening is a statement about tested premises, not an impossibility
theorem (Response 17, accepted in Reply 18). 19's manuscript in the tree at
commit `58871b3` still contains merge-conflict markers from commit
`bd8d0a9` and does not compile until they are resolved.

## Reusable for

Screen proposed global exclusions against the relevant Euler-factor,
weighted-square, reflected, and primitive-compatible controls, naming the
premise or quantitative estimate each fails. A valid finite certificate can
pass a collision-free box of a control: rejection is required on a domain
containing its collision, or for a bound contradicted by its witness. This
qualifies the earlier blanket instruction that "any certificate" must reject
all four families. The raw-margin witness format is reusable.

## Where

- 19: [manuscript](../papers/investigations-2/active/19_euler_factor_controls/manuscript/euler_factor_controls.tex) (thm:structure, thm:flow, prop:witness, thm:certified, thm:asymptotic, cor:screen, §"What upper-bound proofs must use"); [certified witness](../papers/investigations-2/active/19_euler_factor_controls/notes/2_CERTIFIED_EULER_FACTOR_WITNESS_20261014.md); [initial program](../papers/investigations-2/active/19_euler_factor_controls/notes/INITIAL_RESEARCH_PROGRAM_20261013.md); [verification review](../papers/investigations-2/active/19_euler_factor_controls/reviews/1_MANUSCRIPT_AND_CERTIFICATE_VERIFICATION_CLAUDE_20261014.md); [README](../papers/investigations-2/active/19_euler_factor_controls/README.md).
- 22 controls: [three-square control](../papers/investigations-2/active/22_theta_manifold_geometry/notes/05_control_families/01_SQUARE_SUPPORT_ENDPOINT_COLLISION_OBSTRUCTION_20261015.md), [reflection rigidity](../papers/investigations-2/active/22_theta_manifold_geometry/notes/05_control_families/02_WEIGHTED_COMB_REFLECTION_RIGIDITY_20261015.md), [four-square control](../papers/investigations-2/active/22_theta_manifold_geometry/notes/05_control_families/03_TWO_ENDPOINT_SQUARE_COLLISION_20261015.md), [reflected control](../papers/investigations-2/active/22_theta_manifold_geometry/notes/05_control_families/04_REFLECTION_POSITIVE_SOURCE_COLLISION_AND_MIXED_SECTORS_20261015.md); [manuscript §9](../papers/investigations-2/active/22_theta_manifold_geometry/manuscript/theta_manifold_geometry.tex); [independent recomputation](../papers/investigations-2/active/22_theta_manifold_geometry/numerics/recompute_controls_claude_20261015.py).
- The table and its scope: [Reply 18](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/18_REPLY_TO_RESPONSE_17_CLAUDE_20261015.md) §3; [Review 16](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/16_JOINT_REVIEW_OF_INVESTIGATIONS_21_AND_22_CLAUDE_20261015.md) §6 (superseded wording); [Response 17](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/17_RESPONSE_TO_JOINT_REVIEW_CLAUDE_20261015.md).
- Earlier counter-kernels: [11](11_newman_heat_flow_reductions_and_certificates.md).

- 21 controls: [smooth log-concave source](../papers/investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/53_SOURCE_CONCAVITY_AND_POSITIVE_TIME_COLLISION_CONTROL_20261015.md), [primitive-compatible collision control](../papers/investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/56_POSITIVE_PRIMITIVE_COLLISION_CONTROL_20261015.md), [Review 31](../papers/investigations-2/active/21_quaternion_theta_geometry/reviews/31_SIGNED_FORMS_PRIMITIVE_AND_SOURCE_CONTROL_REVIEW_20261015.md), [Review 33](../papers/investigations-2/active/21_quaternion_theta_geometry/reviews/33_PRIMITIVE_CIRCLE_AND_CARRIER_CONTINUATION_REVIEW_20261015.md).
- Scope of a finite certificate's control screen: [Review 20](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/20_ADDITIONAL_PATHS_FORWARD_ASSESSMENT_CODEX_20261016.md), "The control screen must distinguish premises and estimates."

20 October 2026 — Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra, actual effort ultra**. **Actual-theta three-profile relaxation (3/13).** The [BW-08 source note](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/08_deflated_jet_hierarchy/notes/06_ACTUAL_PROFILE_OBSERVATIONS_AND_RELAXED_DUAL_FAILURE_20261020.md) proves the observation/weak-duality interface and interval-certifies actual b=20,40,80 profiles for T=.1±1e-6, a in [1001,1002]. Its exact-data positive-measure relaxation admits a nearby unit-count atom with positive fractional slack masses. “Consequently every global count majorant in the stated three-observation span has exact objective at least one.” The relaxed S2 is unbounded; this is neither an integer zero configuration nor a physical theta event. [Separate same-model review](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/reviews/03_FOURTH_ORDER_AND_ACTUAL_PROFILE_ROUND_REVIEW_20261020.md); no specialist review. Other sample schedules, integer-sensitive constraints and full-source estimates remain outside this scoped result.

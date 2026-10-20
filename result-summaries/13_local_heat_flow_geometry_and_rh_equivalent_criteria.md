# Local heat-flow geometry, marked topology, and RH-equivalent criteria

15 October 2026. Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork.

Coverage and scope revised 16 October 2026 for Edward Baker with substantial
LLM assistance: **gpt-6-astra (Codex)**, reasoning effort **ultra**.

## Summary

Write \(h_j=\partial_x^jH\), \(E=h_0^2+h_1^2\), and
\(\mathcal L_j=h_{j+1}^2-h_jh_{j+2}\) for a real analytic backward-heat
field \(H_t=-H_{xx}\). The local results concern a spatial zero of exact
finite order \(m=2r+j\), \(r\ge1\), \(j\in\{0,1\}\).

- **Stationary collision geometry (22 §2).** For \(s=T-t\), the relevant
  stationary predecessor is one analytic curve, the opposite-parity
  stationary set is locally empty before the event, and the physical jet
  has a scalar factor: \(E=W^2Q(s)\), with positive analytic \(Q\).
  The signed ratio has the universal pole \(\mathcal L_j/E=-r/s+O(1)\).
- **Chord and turning laws (22 §7).** The fixed-endpoint chord satisfies
  \(\mathcal C_j/\sqrt E\to-d_\delta<0\); an independently established
  starting-energy estimate with uniform \(o(\sqrt E)\) loss excludes the
  covered event, and the exponent \(1/2\) is sharp. The exponential-average
  version retains its endpoint-only cutoff error
  \(\le B_j(T_*)e^{-\pi(N+1)^2/4}\sqrt E\). Quarter-turn concentration and
  explicit scaled profiles describe the same local degeneration.
- **Circle cancellation loss (21 Note 57).** On full holomorphic circles
  and nearby time slices, taking the boundary density's negative part
  separately creates a fixed-radius loss of order \(s^{-r}\) relative to
  \(E\), versus the exact stationary pole of order \(s^{-1}\). The excess
  is the discarded positive boundary mass. Radius \(R\asymp\sqrt s\)
  removes the extra pole order, not the divergence; an event-dependent
  radius is a diagnostic, not a prescribed certificate.
- **Real index, walls and projective data (22 Notes 04, 06, 07).** Each
  collision has real index \(-\lfloor m/2\rfloor\), so zero boundary
  winding excludes every interior collision when the boundary jet is
  nonzero. Moving-wall root counts retain signed wall fluxes, including
  tangencies. The real projective jet \([H:H_x]\in\mathbb{RP}^1\) has
  degree twice the jet winding; it retains the obstruction. Unrestricted
  filling in \(\mathbb{CP}^1\) does not. The completed theta pilot is in
  [11](11_newman_heat_flow_reductions_and_certificates.md). With regular
  positive initial time, terminal time above \(1/2\), and the stated boundary
  and uniform-confinement hypotheses, stabilized negative theta winding counts
  nonreal zeros in the upper-right quadrant with multiplicity.
- **Complex and embedded multiplicities (22 Notes 04, 08).** The holomorphic
  pair \((H,H_z)\) has local intersection multiplicity \(m(m-1)/2\),
  positive complex degree and negative degree in the declared quaternion
  orientation. At fixed time, the primitive curve \((P,H)\), \(P_z=H\),
  has embedded link \(T(m,m+1)\) and Milnor-fiber genus \(m(m-1)/2\);
  its normalization is a disk. These are distinct germs. Real and complex
  degree magnitudes agree only for a double collision; their parity always
  agrees. Degree alone proves no general advantage or disadvantage for a
  four-dimensional boundary estimator.
- **Compact real surfaces (22 Note 05).** For
  \(f(z)=\xi(1/2+\sqrt z)=\sum\gamma_k z^k/k!\), define
  \(J_d(X)=\sum_{k=0}^d\binom dk\gamma_kX^k\), with positive complete-theta
  moment coefficients. RH is equivalent to every smooth projective
  normalization of \(y^2=J_{2g+1}(x)\) having exactly \(g+1\) real
  components. The count uses the original degree, not the possibly smaller
  normalization genus. RH gives strict Jensen hyperbolicity without
  assuming simple zeta zeros. This is a proved reformulation using classical
  ingredients, not a proof that the component condition holds.
- **Surface deficit and polynomial heat (22 Note 07).** For an odd-degree
  real polynomial \(Q\) of degree \(2g+1\),
  \(g+1-b_0(C_Q(\mathbb R))=N_{\rm nonreal}(Q)/2+
  \sum_{a\in\mathbb R}\lfloor\operatorname{mult}_aQ/2\rfloor\), counting
  nonreal roots with multiplicity. This equals its remaining polynomial-heat
  collision weight, including initial-slice events. The reciprocal
  Hermite–Jensen deficits increase with degree and decrease with auxiliary
  heat time. Every finite polynomial eventually regularizes; a uniform
  finite threshold across all degrees is already RH-equivalent. Auxiliary
  polynomial heat time is not physical theta heat time.
- **Observation equivalences (Review 16 and Reply 18).** Under RH every
  **positive-time** slice is Laguerre–Pólya with simple zeros and satisfies
  the observation criteria with zero loss. The all-event loss criteria on
  \((0,1/2]\) are RH-equivalent; on \([t_0,1/2]\), they characterize
  \(\Lambda\le t_0\), while strict pointwise signs require
  \(\Lambda<t_0\). The prescribed-trace equivalence retains its stated
  two-sided locally bounded scalar coefficient and remainder control.

- **Normalized jet rotation comparison (3/11 S03, 18 October).**
  The complete signed oscillator-defect integral has an exact first-jet
  endpoint primitive. The scoped comparison is **proved in-note**: scalar
  transport with independent endpoint residual envelopes is dominated by
  the ideal direct radius test for the same phase, approximant and norm.
  Correlated residual estimates and computational cost comparisons are
  outside that limitation. The fixed height-1000 cover validates direct
  exclusion, gives a certified failure witness for the declared standard
  Cauchy payments, and leaves sharper joint-disk transport inconclusive.
  No new region or global theta estimate. [Proof](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/notes/01_SIGNED_TRANSPORT_AND_DIRECT_JET_COMPARISON_20261018.md),
  [same-model internal review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/reviews/01_SIGNED_TRANSPORT_INTERNAL_REVIEW_20261018.md).
  Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol, ultra**.
  The [correlated continuation](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/notes/02_CORRELATED_ARITHMETIC_RESIDUAL_AND_PAID_TRANSPORT_20261018.md)
  supplies an **interval-certified** finite residual increment below
  `0.000266448` versus `0.002011747` for independent endpoints from the
  same source data. Paid transport exceeds `1.124460`; direct exclusion
  remains stronger. Its oscillator calibration has complete real
  phase-scaled first-jet error below `0.000266449`. Earlier finite
  transport uncertainty is resolved with added source information,
  without new coverage or a global bound; [same-model internal review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/reviews/02_CORRELATED_RESIDUAL_INTERNAL_REVIEW_20261018.md).
  Prepared for Edward Baker, **gpt-6.1-sol, actual effort ultra**, 18 October.

- **GEO-T1 matched winding comparison (3/11, 19 October).**
  **Interval-certified bounded validation** on already-covered
  B=[1/100,1/5]x[999,1001]: whole-boundary winding0 uses7segments/10complete
  calls and no source vertex calls. Optimized direct first-jet certification
  covers3full-time strips in7calls. Both use identical complete source/errors
  at192/256bits. Common setup dominates; direct/winding cold ratios
  0.999385/0.999442 fail the declared factor-two gate. Stop this fixed-box
  comparison; no coverage, global sign estimate or S07-T3 input. Thirty-six
  actual-helper/direct controls pass, and fresh192 replay matches mathematical
  content. [Result](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/notes/06_GEO_T1_WINDING_AND_DIRECT_COMPARISON_20261019.md),
  [same-model internal review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/reviews/01_GEO_T1_WINDING_DIRECT_INTERNAL_REVIEW_20261019.md).
  Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol,
  ultra**; no specialist human review. These timing observations do not
  exclude winding advantages on other domains or acquisition models.

- **BW-01 paired-face payment (3/13, 19 October).** **Proved in-note, same-assistant assessment:** on an event-relative parabolic rectangle, complete third/fourth-derivative bounds give an explicit homotopy threshold recovering the inherited degree -1. Odd time pairing has a sixth-moment remainder, but a consumer retaining only symmetric bounds about the quadratic model still admits that model. “Stop the centered quadratic model plus symmetric absolute-remainder payment as a source of zero winding.” This closes that payment, not BW-01 or signed theta methods. Eight exact polynomial controls; no theta integration, region or bound. [Note](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/01_local_double_winding/notes/03_PAIRED_FACE_REMAINDER_OBSTRUCTION_20261019.md), [self-review](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/01_local_double_winding/reviews/01_PAIRED_FACE_SELF_REVIEW_20261019.md). Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra, actual effort max**; no independent review.

- **BW-08 imaginary-axis jet bound (3/13, 19 October).** **Restricted analytic result, proved in-note; same-assistant self-review only:** at an all-real theta double event with T>0,a>=20, S_a=h3^2/(9h2^2)-h4/(6h2)>log((a+1)/(4pi))/(4a)-3/(2a^2)>1/(2a^2). Positive-source time monotonicity and the time-zero xi identity give the new coefficient; complete derivatives through order six transfer it to a finite critical-value pair on the BW-01 time faces. “This is a stronger necessary condition, not a collision exclusion or a contradictory winding.” Polynomial and Euler-factor controls can satisfy the floor. Four exact polynomial cases and four outward coefficient enclosures; no acquired theta jets, region, bound on Lambda or speed gain. [Note](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/08_deflated_jet_hierarchy/notes/03_IMAGINARY_AXIS_JET_BOUND_20261019.md), [self-review](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/08_deflated_jet_hierarchy/reviews/01_IMAGINARY_AXIS_SELF_REVIEW_20261019.md). Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra, actual effort max**.

- **BW-07/BW-08 continuation (3/13, 20 October).** **Restricted analytic
  results, proved in-note, separate same-model internal review:** with
  b=max(a,20m), the unchanged theta slice's deflated invariant satisfies
  S_m>L_m(a)>m/(4a²)+1/(40b) for every a>0 and finite m>=2 at an all-real
  T>=0. The m=2 physical face-pair transfer is paid; higher m uses a
  differentiated-field consumer. Conditional on a surviving exact m-fold
  threshold event, differentiation m−2 times preserves the actual
  threshold and the positive-source lower bound in both parities.
  “This is not a reduction of a proved exclusion theorem: no such BW-01
  theorem is available.” Errors extend through m+4; physical degree is
  not transported. [Bound](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/08_deflated_jet_hierarchy/notes/04_ALL_HEIGHT_MULTIPLICITY_JET_BOUND_20261020.md),
  [review](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/08_deflated_jet_hierarchy/reviews/02_ALL_HEIGHT_MULTIPLICITY_REVIEW_20261020.md),
  [closure](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/07_multiplicity_reduction/notes/02_DIFFERENTIATED_THRESHOLD_TRANSFER_20261020.md),
  [review](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/07_multiplicity_reduction/reviews/01_DIFFERENTIATED_THRESHOLD_REVIEW_20261020.md).
  No theta event, exclusion or Newman-bound improvement. Prepared for
  Edward Baker with substantial LLM assistance, gpt-6-astra, ultra. The
  earlier 19 October bound is retained as the predecessor, not withdrawn.

- **BW-02–05 local forward obstruction (3/13, 20 October).** **Proved
  in-note; separate same-model review:** an exact double event has an
  explicit forward rectangle with L>=(657/1024)h₂²(s+y²/2), and a complete
  complex disk containing exactly two real simple roots. Its later
  interior jet is nonzero, so every enclosed Jordan region has winding
  zero. This strengthens the same-point local sign only; no nonlocal
  theta witness is forced. [Proof](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/05_later_laguerre_violation/notes/02_QUANTITATIVE_FORWARD_NEIGHBORHOOD_EXCLUSION_20261020.md),
  [review](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/05_later_laguerre_violation/reviews/01_FORWARD_NEIGHBORHOOD_REVIEW_20261020.md).
  Prepared for Edward Baker with substantial LLM assistance, gpt-6-astra,
  ultra. No specialist review or numerical theta region.

- **BW-06 all-multiplicity remainder audit (3/13, 20 October).**
  **Proved in-note; separate same-model review:** the unchanged physical
  jet has explicit parity-sensitive normalized O(r) remainders using
  derivatives through m+2 and a positive full-boundary margin for every
  finite m. It recovers the inherited degree −floor(m/2). “Its symmetric
  absolute-error information cannot force degree zero.” This extends the
  specific BW-01 payment and its obstruction, not a theta exclusion.
  [Proof](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/06_direct_all_multiplicity/notes/02_ALL_MULTIPLICITY_REMAINDER_AUDIT_20261020.md), [review](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/06_direct_all_multiplicity/reviews/01_ALL_MULTIPLICITY_REMAINDER_REVIEW_20261020.md).
  Prepared for Edward Baker with substantial LLM assistance, gpt-6-astra,
  ultra; no numerical theta acquisition, uniform radius or specialist review.


- **Theta-reference Gram estimating obstruction (3/13, 20 October).**
  **Proved in-note; separate same-model review:** the optimal
  event-conditioned finite-Gram norm allowance strictly improves
  coordinate boxes but remains positive, with an explicit determinant
  lower bound. Nonnegative continuous-source controls with a true
  positive threshold also lie in that reference norm ball and have
  positive target quadratic. Their mass anchor fails by a fixed
  positive deficit; they are changed sources, not theta.
  “A more elaborate realization of the same ball does not supply the missing theta sign.” is the
  stated limitation, with mathematics in
  [Note 02](../papers/investigations-3/13_contradiction_analysis/02_threshold_jet_sign/notes/02_EVENT_CONDITIONED_THETA_GRAM_OBSTRUCTION_20261020.md),
  [Note 03](../papers/investigations-3/13_contradiction_analysis/02_threshold_jet_sign/notes/03_POSITIVE_MULTIPLIER_GRAM_EXTENSION_20261020.md) and its
  [review](../papers/investigations-3/13_contradiction_analysis/02_threshold_jet_sign/reviews/02_POSITIVE_MULTIPLIER_GRAM_REVIEW_20261020.md).
  Prepared for Edward Baker with substantial LLM assistance,
  gpt-6-astra, ultra; no physical exclusion or specialist review.

## Status

The local laws, indices, surface identities and equivalences have written
analytic proofs with internal LLM reviews. Polynomial-germ replays check
finite examples and conventions; they do not prove universal quantifiers.
The later topology continuation has its own proofs and review outside the
stable manuscript. The theta winding box is separately interval-certified.
The rule to judge an RH-equivalent proposal as a reformulation and a
quantitative milestone by its number is a research policy, not another theorem.

## Caveats

The generic collision laws do not distinguish theta from the controls in
[12](12_collision_controls_and_screening.md). The complete-theta surface
family retains the source's “real involutions” (Note 05); its desired
maximal topology remains unproved.
The earlier blanket description of all geometry as “sign-blind” is too
broad: oriented associators, forms and real Gauss maps retain the sign;
norms and intrinsic curvature can lose it. See the actual constructions
and integrated positive theorems in [16](16_hypercomplex_reductions_and_geometric_realizations.md).
No literature priority or global theta sign theorem follows from these results.

## Reusable for

Local models, multiplicity-safe boundary accounting, marked real topology,
and comparison of certificate geometries. The compact-surface equivalence
is a precise answer to how manifold topology can encode RH, with all
normalization and reality data retained.

## Where

- [22 manuscript](../papers/investigations-2/active/22_theta_manifold_geometry/manuscript/theta_manifold_geometry.tex), §§2, 7, 11; [21 circle-loss note](../papers/investigations-2/active/21_quaternion_theta_geometry/notes/02_signed_cusp_control/57_CIRCLE_DEFECT_MULTIPLICITY_AND_RADIUS_20261015.md) and [Review 33](../papers/investigations-2/active/21_quaternion_theta_geometry/reviews/33_PRIMITIVE_CIRCLE_AND_CARRIER_CONTINUATION_REVIEW_20261015.md).
- [Spacetime index and embedded primitive topology](../papers/investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/04_SPACETIME_INDEX_AND_MARKED_TOPOLOGY_20261015.md); [compact Jensen surfaces](../papers/investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/05_JENSEN_HYPERELLIPTIC_TOPOLOGY_20261015.md); [Review 13](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/13_GEOMETRIC_SIMPLIFICATION_AND_TOPOLOGICAL_RH_REVIEW_20261015.md).
- [Moving-wall flux and theta winding](../papers/investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/06_WALL_FLUX_AND_CERTIFIED_THETA_WINDING_20261015.md); [real-projective jets and surface deficits](../papers/investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/07_REAL_PROJECTIVE_JETS_AND_JENSEN_HEAT_SURFACES_20261015.md); [real/complex multiplicities](../papers/investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/08_REAL_AND_COMPLEX_COLLISION_MULTIPLICITIES_20261015.md); [continuation review](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/18_SPACETIME_BOUNDARY_AND_GEOMETRIC_CONTINUATION_REVIEW_20261015.md).
- [Review 16](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/16_JOINT_REVIEW_OF_INVESTIGATIONS_21_AND_22_CLAUDE_20261015.md), [Response 17](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/17_RESPONSE_TO_JOINT_REVIEW_CLAUDE_20261015.md), and [Reply 18](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/18_REPLY_TO_RESPONSE_17_CLAUDE_20261015.md), §§1–2, 5, for the corrected equivalence and degree scope.


- **BW09 finite contour round (3/13, 20 October).** Prepared for Edward Baker
  with substantial LLM assistance, **gpt-6-astra, actual effort ultra**.
  **Proved in-note and exact rational replay; separate same-model review:**
  the complete contour consumer retains apex, walls and multiplicities.
  The scoped source audit proves: “If a continuous, nonzero boundary field
  Z satisfies |Z-1|<=1 everywhere on the closed boundary, then W_Z=0”
  (notation rendered in plain text here). Root-following walls give exact
  regularized degree -N/2 from N internal cap roots; they supply no new
  root-count sign. A separate **interval-certified** complete-source gate
  proves H/Gstar>0.0004134538 on [.099999,.100001]×[1001,1002], using
  a pinned 160-bit acquisition and 192/256-bit consumer replay. It excludes
  all event multiplicities only in that tiny box; the signed full-contour
  estimate remains open. [Notes](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision/notes/README.md),
  [review](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision/reviews/01_FINITE_CONTOUR_ROUND_REVIEW_20261020.md).
  No later theta event, global threshold improvement or specialist review.

- **BW09 heat flow and energy consolidation (20 October).** The
  [preserved first manuscript](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision/drafts/20261020_before_phase_concentration.tex) consolidates
  the in-note proofs of collision-patch accounting, nonzero-level
  phase cancellation, localized Laguerre identities and the sharp
  Gaussian deficit. Its scope is explicit: “No negative theta quotient
  winding, negative Gaussian deficit at a selected fixed scale, negative
  localized Laguerre average, or later theta collision has been proved.”
  All 51 exact source-input enclosures accompany the already recorded
  tiny-box computation; no new quadrature or coverage is claimed.
  [New bounded program](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision/research-overview/02_HEAT_FLOW_CONTOUR_AND_ENERGY_PROGRAM_20261020.md) and
  [internal review](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision/reviews/04_INITIAL_MANUSCRIPT_REVIEW_20261020.md).
  Prepared for Edward Baker with substantial LLM assistance,
  gpt-6-astra, actual effort ultra; no specialist review.

- **HFCE bounded follow-up (20 October).** Prepared for Edward Baker with
  substantial LLM assistance, **gpt-6-astra, ultra**.
  **Interval-certified; separate same-model review and same-code replay:**
  existing source data exclude [.109999,.110001]×[1001.25,1001.5], with
  normalized first-jet energy >.00113957880974. The fixed Gaussian
  estimator has complete upper deficit≈2.227983e-9 and gives no exclusion
  gain. Its source states: “the frozen whole-cap interval rule cannot
  certify a negative deficit from these ranges.” A separate fixed later
  cap has Q/Gstar²>.00168232756063, so its nonnegative localized average
  is positive. These are scoped outcomes, not a global theorem or theta
  level-contour certificate. [Note 07](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision/notes/07_FIXED_GAUSSIAN_COMPARISON_20261020.md),
  [Note 08](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision/notes/08_LOCALIZED_COMPARATOR_AND_LEVEL_CONTROL_20261020.md),
  [review](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision/reviews/05_HFCE_BOUNDED_ROUND_REVIEW_20261020.md).
  The preceding manuscript-consolidation entry describes the earlier state.

- **BW09 quantitative phase concentration and manuscript revision (20 October).**
  Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra,
  ultra**. **Proved in-note/manuscript; separate same-model review:** exact
  quadratic endpoint-window masses and tails retain total phase π;
  the complete theta saddle gives a fixed-index cosine profile and a
  physical interior phase layer of width O(L_t⁻²). Finite phase-error
  bounds explicitly pay source moments and root/cut placement. The scope
  is: “These calculations quantify the phase accounting; they do not supply
  the missing theta surplus.” The strict surplus is a conditional target,
  not an achieved sign. No new numerical execution or global wall theorem.
  [Revised manuscript](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision/manuscript/main.tex),
  [brainstorm](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision/brainstorm/01_CAP_AT_INFINITY_20261020.md),
  [Review 06](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision/reviews/06_PHASE_CONCENTRATION_MANUSCRIPT_REVIEW_20261020.md).
  [Program 03](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision/research-overview/03_ANALYTICAL_PHASE_SURPLUS_PROGRAM_20261020.md)
  is prepared; its new finite analytical estimates remain unexecuted.

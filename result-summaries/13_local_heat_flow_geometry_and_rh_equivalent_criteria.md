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

- **BW-10 heat-root motion (21 October 2026).** **Proved in-note;
  same-assistant self-review:** under RH, explicit Jensen bounds give
  complete gap/center velocity remainders of order `(1+log R)/R` on
  compact positive-time intervals. A finite root-block bound supplies
  the label/height-dependent enclosure and a mirror-compression width
  estimate. Complete-source covariance cancellation and effective moment
  bounds give `g_k'=-pi L_t'/L_t^2+O_k(1/(L_t kappa_t^(5/4)))` for fixed
  adjacent labels, hence eventual strict shrinkage. Late-time fixed-rank
  estimates themselves are unconditional; RH identifies continued birth
  walls. “Eventual shrinkage is compatible with a multiple endpoint.”
  No numerical onset, growing-label theorem, signed-contour gain or
  simplicity exclusion. [Root-tail proof](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/19_COMPLETE_ROOT_MOTION_AND_FINITE_TIME_BOUNDS_20261021.md),
  [differentiated saddle](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/20_DIFFERENTIATED_SADDLE_AND_EVENTUAL_GAP_SHRINKAGE_20261021.md),
  [self-review](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/reviews/19_ROOT_MOTION_AND_DIFFERENTIATED_SADDLE_REVIEW_20261021.md).
  Prepared for Edward Baker with substantial LLM assistance,
  **gpt-6-astra, actual effort max**; no specialist review.

- **BW10 heat-scale tube profile (21 October 2026).**
  [Note 22](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/22_HEAT_SCALE_SIGNED_TRACE_AND_UNIVERSAL_PROFILE_20261021.md) is **proved in-note, conditional on the specified
  endpoint event**. The exact physical phase measure gives a complete-source
  error `O(sqrt(t) log(1/t))`, uniform for bounded `eta/sqrt(2t)` at a
  fixed event. The double profile is `pi(1+r^2)`; Hermite orthogonality
  proves the outer profile `pi[L_(m-1)^(1)(-r^2)-1]` for each fixed
  multiplicity. A separate local analytic version covers controls without
  an all-real heat slice. Matching controls share these leading data:
  “The selected leading-profile discriminator therefore fails.” This
  does not rule out a source-specific arithmetic bound below the profile.
  HMC-05 remains open. [Same-assistant self-review](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/reviews/21_HEAT_SCALE_TRACE_AND_CONTROL_REVIEW_20261021.md); finite
  exact algebra only. Prepared for Edward Baker with substantial LLM
  assistance, **gpt-6-astra, actual effort max**; no specialist review.

- **BW12 relative charge and two-zero theta comparison (21 October 2026).**
  **Proved in-note / interval-certified finite comparison; same-assistant
  review:** a square holomorphic degree-zero reference transfers its
  boundary floor into the interior, giving the same direct margin from
  the same error and degree proof ([Note 02](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/02_HOLOMORPHIC_REFERENCE_TRANSFER_AND_BOUNDARY_DEGREE_20261021.md)).
  A complete-theta box with |Re t|,|Im t|,|Im z|<.01 and 28<Re z<43
  has charge zero, exactly two simple real zeros and one stationary
  point at t=0. Boundary gap >3.5683e−7 loses to direct >3.9348e−7
  from identical 1,032 source integrals and 2,056 boundary vertices.
  “This thin-box implementation does not establish a boundary advantage.”
  The direct consumer uses 256 full cells; the boundary consumer checks
  9,228 tetrahedra and solves 9,228 exact degree systems. This stops the
  declared comparison, not other boundary acquisition schemes or global
  programs. [Note 03](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/03_TWO_ZERO_THETA_BOUNDARY_AND_DIRECT_COMPARISON_20261021.md),
  [self-review](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/reviews/03_TWO_ZERO_THETA_COMPARISON_REVIEW_20261021.md).
  Prepared for Edward Baker with substantial LLM assistance,
  **gpt-6-astra, actual effort max**; no independent review or global
  simplicity conclusion.

- **BW12 analytical two-root charge reduction (21 October 2026).**
  [Note 05](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/05_TWO_ROOT_DISCRIMINANT_FLOW_AND_REAL_CAP_CHARGE_20261021.md)
  is **proved in-note under isolation and phase hypotheses; self-review**.
  An analytic coefficient gives Delta'=8+A Delta. On a proper
  real-symmetric two-root time rectangle, K tau<pi/2 makes every event
  real, allows at most one, and determines the charge from real cap signs.
  A complete-moment strip width uses proved spatial-wall floors without
  an inverse internal gap. “Injectivity controls how many times a value
  is attained; it does not say that the value is omitted.” That round
  established no new theta wall floors or cap signs. [Review 05](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/reviews/05_TWO_ROOT_DISCRIMINANT_AND_CAP_REVIEW_20261021.md).
  Prepared for Edward Baker with substantial LLM assistance,
  **gpt-6-astra, actual effort max**; no independent validation.

  **Complete-source continuation, 21 October 2026:**
  [Note 06](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/06_COMPLETE_THETA_WALLS_AND_REAL_CAP_APPLICATION_20261021.md) is **proved in-note / interval-certified; self-review**.
  On |Re t|,|Im t|<.01 and |z−71/2|<10, nested theta walls and counts,
  K tau<.034891 and both cap discriminants >144 give charge zero.
  The same wall/phase consumer admits a quadratic event with charge one.
  “This is not a new qualitative property distinguishing theta from every
  colliding family.” Near-event and arbitrary-height signs remain open.
  [Review 06](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/reviews/06_COMPLETE_THETA_REAL_CAP_APPLICATION_REVIEW_20261021.md),
  [receipt](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/numerics/REAL_CAP_THETA_APPLICATION_20261021.json).
  Prepared for Edward Baker with substantial LLM assistance,
  **gpt-6-astra, actual effort max**; no independent validation.

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


- **BW10 endpoint phase-energy comparison (20 October 2026).**
  [Note 12 §4](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md) is **proved in-note for an isolated
  analytic backward-heat event**, with separate same-model review.
  At multiplicity m, the physical squared phase-density integral is
  pi m(m−1)/(4t)+O(t^(−1/2)). Positive derivative scale sqrt(2t) instead
  gives outer-cap cost C_m/sqrt(2t)+O(1), C_2=pi+2, with the same
  (m−1)pi cap phase. The spacetime d beta term is retained.
  “The scaled finite energy therefore does not exclude this event.”
  This is a quantitative scale comparison, not an opposing arithmetic
  estimate or simplicity conclusion. [Review 12 §5](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/reviews/12_FINITE_PRECISION_SIGNED_KERNEL_AND_ENERGY_REVIEW_20261020.md).
  Prepared for Edward Baker with substantial LLM assistance,
  **gpt-6-astra, actual effort ultra**; no specialist review.


- **BW10 ratio-energy heat crossover (20 October 2026).**
  [Note 15 §5](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/15_COMPLETED_RATIO_ENERGY_AND_MULTIPLICITY_20261020.md) is **proved under RH in-note**,
  with separate same-model review. At t=v epsilon² its all-zero energy
  coefficient is sum C_m(sqrt(v/2))/(sigma²+gamma²); C_m decreases from
  c_m to m/2, with exact C_2=1+1/[4(1+r²)]. The global large-v excess
  has coefficient (K_sigma−M_sigma)/4. “This behavior is compatible with
  the smooth positive theta source; it is not an opposing upper bound.”
  A multiple endpoint requires order-1/epsilon heat-time difference
  quotients, despite finite source-moment derivatives. No differentiation
  of a limit or finite-parameter monotonicity is claimed.
  [Review 12 §7](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/reviews/12_FINITE_PRECISION_SIGNED_KERNEL_AND_ENERGY_REVIEW_20261020.md). Prepared for Edward Baker with
  substantial LLM assistance, **gpt-6-astra, ultra**; no specialist review.

**BW12 endpoint-window and signed-response continuation, 21 October 2026.**
Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, actual effort ultra**. **Proved in-note; separate same-model
internal review:** [Note 07](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/07_QUANTITATIVE_ENDPOINT_WINDOWS_AND_HEIGHT_COVERAGE_20261021.md) pays explicit proper
two-root windows from complete moments at every hypothetical exact
double, pointwise at every finite height; the event still has charge one.
[Note 08](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/08_SIGNED_DISCRIMINANT_RESPONSE_AND_EVENT_DISPLACEMENT_20261021.md) proves exact logarithmic discriminant
response, its quadratic remainder and boundary-paid event continuation.
Its canonical-tail appendix gives a strictly narrower signed interval
than the matched pointwise envelope: “The interval can still straddle
zero.” [Note 09](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/09_MANY_ROOT_DISCRIMINANT_FLOW_AND_CAP_LIMITS_20261021.md) proves D'=8T+B D for every proper
finite cluster, with complete regular exterior coefficient and explicit
wall bounds. A proper cubic has at most one real event, but may have
three complex-window events; a quartic birth has equal positive caps
and charge six. These controls exclude only the direct many-root
phase/cap extension. ECE-01's parameterized geometry is complete;
the positive unchanged-theta margin, endpoint exclusion and full
height/multiplicity assembly remain open. [Review 08](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/reviews/08_ENDPOINT_CHARGE_OPENING_ROUND_REVIEW_20261021.md);
exact algebra controls, no new theta numerical certificate or specialist
validation.

**BW12 manuscript consolidation, 21 October 2026.**
The [self-contained analytic manuscript](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/manuscript/main.tex)
consolidates the preceding in-note results, with numerical certificates
as support and separate same-model internal review. Its explicit limit
is: “The geometric quantifier is paid here; that signed quantifier remains
open.” No research-status upgrade or specialist validation follows.
[Integration review](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/reviews/09_MANUSCRIPT_INTEGRATION_REVIEW_20261021.md).
Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, actual effort ultra**.


**BW12 finite-time reconstruction and covariance, 21 October 2026.**
Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, effort ultra**. **Proved in-note; separate same-model
internal review:** [Note 13](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/13_PAID_ENDPOINT_WINDOW_AND_FINITE_TIME_BASELINE_20261021.md)
pays an explicit conditional canonical cutoff/window with actual rho<=1/15.
[Note 14](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/14_GAUSSIAN_HERMITE_RECONSTRUCTION_AND_RESPONSE_QUOTIENT_20261021.md)
identifies Gaussian Hermite reconstruction with endpoint Taylor truncation
and compresses the quadratic response modulo P², without inverse root gap.
[Note 15](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/15_CANONICAL_COVARIANCE_SIGNED_ENCLOSURE_20261021.md)
proves a signed covariance correction with O(J^-3) remainder and strict
containment in exact range enclosures on the same uniform cutoff grid.
Extra moments and acquisition errors are paid. Its scope is explicit:
“There is no T-dependent gain.” Same-information direct evaluation gives
the same refined interval. No theta numerical endpoint, positive-time
advantage, endpoint exclusion or specialist validation is established.
[Review 12](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/reviews/12_FINITE_TIME_SIGNED_RECONSTRUCTION_OPENING_REVIEW_20261021.md).

22 October 2026 — Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, effort ultra**. **Proved in-note; contributing-agent same-model
review:** [I4 Note 03](../papers/investigations-4/03_heat_transport_and_charges/notes/03_SCALAR_SOURCE_CONTRACT_AND_SURVIVOR_WIDTH_20261022.md)
bounds the terminal scalar-current survivor set near a real-analytic ordinary
double by O(epsilon^(5/2)), sharp for the quadratic; constants are local,
with no global all-real premise. Its tested unsigned terminal-floor source
contract is dominated by direct stationary evaluation.
[Note 04](../papers/investigations-4/03_heat_transport_and_charges/notes/04_PHASE_BOUNDARY_REMOVAL_AND_CAP_REDUCTION_20261022.md)
specializes the inherited phase current to an exact finite cap reduction:
side integrals vanish, while an ordinary-double shrinking cap retains a
nonzero phase contribution. This is an independent integral-simplification
result, not a theta exclusion or a complex Hopf-side reduction.
[Review](../papers/investigations-4/03_heat_transport_and_charges/reviews/03_SOURCE_CONTRACT_SURVIVOR_AND_BOUNDARY_REVIEW_20261022.md);
no specialist validation or theta numerical acquisition.

22 October 2026 — Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, effort ultra**. **Proved in-note; contributing-agent same-model
review:** [I4 shared Note 01](../papers/investigations-4/notes/01_CHERN_HOPF_PROJECTIVE_SIDES_AND_LOCAL_SECTORS_20261022.md)
constructs local ordinary-double sectors with exactly cancelling projective
sides and retained opposite cap fluxes. [Note 02](../papers/investigations-4/notes/02_CHERN_HOPF_PHYSICAL_TIME_SECTOR_REDUCTION_20261022.md)
reduces actual heat-edge three-form integrals to one critical-value phase
trace using harmonic averaging, with sufficient source-chart contracts.
Its scope is explicit: “That event is a boundary apex of this sector, not an
interior event of a full spatial neighborhood.” At that opening milestone,
full event-enclosing physical assembly remained open; Note 03 below completes
its conditional local analytic construction. Actual theta acquisition and
exclusion remain open.
[Review](../papers/investigations-4/03_heat_transport_and_charges/reviews/04_CHERN_HOPF_BOUNDARY_OPENING_REVIEW_20261022.md);
exact algebra and noncertified quadratic diagnostics, no specialist validation.

**I4 complete physical boundary and integral bounds, 22 October 2026.**
Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, effort ultra**. **Proved in-note; contributing-agent same-model
review:** [shared Note 03](../papers/investigations-4/notes/03_COMPLETE_PHYSICAL_BOUNDARY_AND_CRITICAL_VALUE_WINDING_20261022.md)
completes CHB-04 as a conditional local analytic assembly: all physical faces
and both charts reduce to one critical-value winding, with explicit source
geometry, boundary floors and regulator error. It states: “The spatial wall
generally has nonzero flux”; its separate integral is removed only in the
complete assembly. The quartic with exterior neighbors preserves spatial
total multiplicity through a double zero while retaining full Hopf charge one.
[Shared Note 04](../papers/investigations-4/notes/04_TOPOLOGICAL_MASS_BOUNDS_AND_INDEX_THEOREM_INTERFACE_20261022.md)
begins CHB-07 independently of simplicity: finite-regulator mass and
bounded-weight estimates, plus the exact Gauss-area/Schur interface with
its inverse cost. Its scope is explicit: “It is not automatically a bound
on one fixed-time slice”; a useful Gauss-area comparison uniform as the regulator tends
to zero, or a theta-specific gain, remains open. [Review 05](../papers/investigations-4/03_heat_transport_and_charges/reviews/05_COMPLETE_BOUNDARY_AND_INTEGRAL_BOUNDS_REVIEW_20261022.md)
and [control receipt](../papers/investigations-4/03_heat_transport_and_charges/numerics/CHB_FULL_BOUNDARY_CHECKS_20261022.json)
record exact controls and noncertified floating diagnostics. No parent
exclusion-gate upgrade, theta acquisition, certified quadrature or specialist
validation; the charge/discriminant identity is inherited from BW12.

**I4 first Gauss-area certificate comparison, 22 October 2026.** Prepared
for Edward Baker with substantial LLM assistance, **gpt-6.1-sol, effort
ultra**. **Proved in-note; contributing-agent internal LLM review:**
[Note 05](../papers/investigations-4/notes/05_TARGET_INVENTORY_AND_FINITE_REGULATOR_GAUSS_COMPARISON_20261022.md)
pays the spatial Green regulator bias and proves that Note 04's global
inverse-Schur certificate exceeds the direct unregularized Green certificate
by at least (5242880 pi/23273)(D_2/h)^4, for every finite regulator on
Note 03's sufficient ordinary-double window. The source qualifies:
“The inequality compares upper-bound certificates, not the actual integrals.”
This stops that regulator-optimization class, not weighted/localized or
source-specific estimates. The critical-wall g_2=q² connection still needs
trace, signed moment and endpoint payments. [Review 06](../papers/investigations-4/03_heat_transport_and_charges/reviews/06_FINITE_REGULATOR_GAUSS_COMPARISON_REVIEW_20261022.md);
no theta acquisition, exclusion-gate upgrade or specialist validation.

**I4 critical-wall trace and signed remainder, 22 October 2026.** Prepared
for Edward Baker with substantial LLM assistance, **gpt-6.1-sol, effort
ultra**. **Proved in-note; contributing-agent internal LLM review:**
[Note 06](../papers/investigations-4/notes/06_CRITICAL_WALL_TRACES_AND_SIGNED_ENDPOINT_BUDGET_20261022.md)
proves the sharp disk trace q²<=(1+P²)A/(pi r²), a fully costed complex-bulk
to moving-curve bound, and the conditional ordinary-double signed residual
C_2-C_0/t=tB', |tB'|<=K_0t. The tested local-Schur/total-mass certificate
is dominated by direct critical-value estimation. The source says:
“These statements preserve the coefficient one; they cannot supply ICW's
strictly subunit coefficient.” Its signed center and both square-trace
singular subtractions have explicit endpoint/acquisition allowances.
[Review 07](../papers/investigations-4/03_heat_transport_and_charges/reviews/07_CRITICAL_WALL_TRACE_AND_ENDPOINT_BUDGET_REVIEW_20261022.md);
no actual theta sign, acquisition, exclusion margin or specialist validation.

**Reciprocal Hodge energy first finite pilot, 22 October 2026.** Prepared
for Edward Baker with substantial LLM assistance, **gpt-6.1-sol, effort ultra**.
**Proved in-note; separate same-model internal review:**
[RHE Note 01](../papers/investigations-4/09_reciprocal_hodge_energy/notes/01_FINITE_COVER_CONTRACT_AND_ENERGY_ENCLOSURE_20261022.md)
completes a conditional finite bordered-cover contract and derives an explicit
O(log(1/tau)) direct energy upper bound from the inherited ordinary-double
event chart. It says: “It is a direct reciprocal majorant available to both
methods.” The bound diverges at the endpoint and supplies no Hodge advantage.
[Note 02](../papers/investigations-4/09_reciprocal_hodge_energy/notes/02_FULL_QUADRATIC_ENERGY_AND_TRANSVERSE_PAYMENT_20261022.md)
keeps every quadratic cut and physical boundary term; the core period remains
constant while the relative period diverges. The failure concerns bounded
exterior norms/core-period compression, not complete theta boundary data.
[Review](../papers/investigations-4/09_reciprocal_hodge_energy/reviews/01_CONTRACT_AND_QUADRATIC_PILOT_REVIEW_20261022.md);
small floating calibration only, no theta acquisition, endpoint exclusion
or specialist validation.


## Real Thom support-rejection opening, 22 October 2026

Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol,
actual effort ultra**. [I4/08 Note 02](../papers/investigations-4/08_real_thom_degree_integrals/notes/02_SUPPORT_REJECTION_AND_CONTROL_ANALYSIS_20261022.md)
records an **interval-certified bounded support comparison** and a scoped
same-range dominance proof. On the inherited [0.01,0.20] x [25,45] rectangle,
the fixed compact density has empty pullback support: integral exactly zero.
Compact and direct interior each use 255 range enclosures; the reproduced
polygon winding uses 698, sharing 76 complete midpoint integrals. Every
support-rejected Cartesian range already directly excludes zero, so this
support-only consumer cannot beat matched direct subdivision. Stop this
specified comparison for comparative benefit; active signed integration
remains unimplemented. No new region, global theta estimate or endpoint
simplicity claim. [Separate same-model internal review](../papers/investigations-4/08_real_thom_degree_integrals/reviews/01_OPENING_SUPPORT_COMPARISON_INTERNAL_REVIEW_20261022.md),
with process replay and adverse-input checks; no specialist validation.

**RHE coupled remainder continuation, 22 October 2026.** Prepared for
Edward Baker with substantial LLM assistance, **gpt-6.1-sol, effort ultra**.
**Proved in-note; separate same-model internal review:**
[RHE Note 03](../papers/investigations-4/09_reciprocal_hodge_energy/notes/03_REAL_PRIMITIVE_REDUCTION_AND_BOUNDED_MODEL_REMAINDER_20261022.md)
reduces the full finite-annulus energy to a projected relative period plus
a bounded exterior correction, and proves gap-uniform energy/period/full-boundary
remainders after complete quadratic subtraction. Its explicit upper strictly
improves the earlier coarse certificate on a declared window. The source
qualifies: “This is a sharper shared direct baseline, not a win over a direct
method given the same model and constraints.”
[Review](../papers/investigations-4/09_reciprocal_hodge_energy/reviews/02_REAL_PRIMITIVE_AND_MODEL_REMAINDER_REVIEW_20261022.md);
floating nonconstant heat-cubic calibration only. Actual theta acquisition,
Hodge-specific advantage and endpoint exclusion remain open.


## Integral budget without a prior interior certificate, 22 October 2026

Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol,
actual effort ultra**. [I4/08 Note 04](../papers/investigations-4/08_real_thom_degree_integrals/notes/04_INTEGRAL_BOUNDS_WITHOUT_INTERIOR_NONVANISHING_20261022.md)
records an **interval-certified bounded estimate**: the fixed wider compact
theta integral on the inherited rectangle is enclosed in
[-0.436449,0.698391], with nine origin-containing first-jet boxes retained.
Boundary-only ranges pay the collar; the integer degree law then gives zero
as a conclusion, without a prior complete interior nonvanishing certificate.
The upper uses a positive-part majorant, with no cancellation gain. Total
801 range calls / 2,108 component ranges lose to direct 255 /510; the bulk
needs two extra midpoint jets. Stop this specified benchmark for efficiency
or coverage benefit. An exact polynomial control has genuinely active signed
support and a proved-in-note absolute allowance below 0.86, without using an
interior floor. This updates the opening's unimplemented status, not its
support-only closure. [Separate same-model review](../papers/investigations-4/08_real_thom_degree_integrals/reviews/02_ACTIVE_BULK_COMPARISON_INTERNAL_REVIEW_20261022.md)
checks the proof, replay and failure controls; no new region, global theta
estimate, RH or specialist validation.

**RHE actual regular theta fiber, 22 October 2026.** Prepared for Edward
Baker with substantial LLM assistance, **gpt-6.1-sol, effort ultra**.
[Note 04](../papers/investigations-4/09_reciprocal_hodge_energy/notes/04_ACTUAL_REGULAR_THETA_FIBER_COMPARISON_20261022.md)
records “one actual regular theta fiber enclosed with outward ball arithmetic”
at t=0 on |z-35|<=8, with exact count 2 and two simple real branches. Both
native consumers meet the 25% width target; the boundary interval is strictly
inside the native direct interval. Measured consumer/fresh ratios 1.99749/1.17383
include failed meshes and the same setup. The source qualifies: “the equally
informed direct method may reuse the boundary identity.”
[Separate same-model internal review and final replay](../papers/investigations-4/09_reciprocal_hodge_energy/reviews/03_ACTUAL_THETA_FIBER_COMPARISON_REVIEW_20261022.md);
all canonical source, root, geometry, primitive and rounding errors retained.
This is one implementation comparison, not intrinsic dominance or endpoint
exclusion; no specialist validation.

**Coupled signed theta-tail acquisition, 22 October 2026.** Prepared for
Edward Baker with substantial LLM assistance, **gpt-6.1-sol, effort ultra**.
[CHB local Note 02](../papers/investigations-4/10_chern_hopf_integral_estimates/notes/02_COUPLED_SIGNED_THETA_TAIL_ESTIMATES_20261022.md)
is **proved in-note; one regular canonical critical point interval-certified**.
Using both C_0=V and S_1=0 gives one-sided signed intervals with exact-data
width factors 4/5 and 3/7 versus specified same-moment cosine-Taylor bounds;
complete finite errors retain strict endpoint gains. Its best finite width
is 1.90544e-29, but an added direct signed tail integral gives 1.26549e-61.
The source says: “This is a useful moment-interface refinement, not the missing
global signed theta estimate or an advantage intrinsic to topological mass.”
The positive atomic collision is retained; published controls pass the
universal inequalities. [Internal review and hash-bound certificate](../papers/investigations-4/10_chern_hopf_integral_estimates/reviews/02_COUPLED_SIGNED_TAIL_REVIEW_20261022.md).
Stop this finite moment pilot as a dominance claim; global arithmetic
signed bounds and inherited exclusion gates remain open. No specialist review.

**RHE analytic manuscript consolidation, 22 October 2026.** Prepared for
Edward Baker with substantial LLM assistance, **gpt-6.1-sol, effort ultra**.
The [working draft](../papers/investigations-4/09_reciprocal_hodge_energy/manuscript/reciprocal_hodge_energy/main.tex)
gives self-contained proofs of the existing finite boundary/remainder/event
results, with canonical normalization and complete moment tails. It states:
“These are shared direct estimates, not a new restriction on the source's
admissible events.” The 25-page draft confines numerics to cited support.
[Internal same-model manuscript review](../papers/investigations-4/09_reciprocal_hodge_energy/reviews/04_ANALYTIC_MANUSCRIPT_REVIEW_20261022.md);
no stronger endpoint estimate, RH theorem, simplicity exclusion, or specialist
validation. This is an exposition milestone, not a new exclusion result.

**RHE finite part and broader integral bounds, 22 October 2026.** Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol, effort ultra**. **Proved in-note; internal same-model review:** [Note 06](../papers/investigations-4/09_reciprocal_hodge_energy/notes/06_FINITE_PART_AND_POSITIVE_ENDPOINT_CORRECTION_20261022.md) gives the exact centered-disk reciprocal-energy finite part and positive coefficient correction, bounded by 12 pi/(23^3 |A|) on its ordinary-event chart. [Note 07](../papers/investigations-4/09_reciprocal_hodge_energy/notes/07_TIME_AVERAGED_AND_FRACTIONAL_RECIPROCAL_BOUNDS_20261022.md) gives sharp fractional and explicit time-strip bounds. [Note 08](../papers/investigations-4/09_reciprocal_hodge_energy/notes/08_DERIVATIVE_WEIGHTED_ENERGY_AND_GLOBAL_STRIP_BOUND_20261022.md) proves all-height disk/strip uppers for 2 integral |H_z|^2/|H| and a cutoff source-error bound 64 pi epsilon/9, through every multiplicity. It states: “This is a model-error bound, not a completed quadrature interval for the observable.” The cutoff is inherited from I4/07; the modulus-potential transfer is the increment. [Review 05](../papers/investigations-4/09_reciprocal_hodge_energy/reviews/05_FINITE_PART_AND_WEIGHTED_INTEGRAL_REVIEW_20261022.md) checks constants, source tails and scope. No unweighted endpoint exclusion, sibling signed/trace estimate, new source acquisition or specialist validation.

**RHE signed and trace transfers, 22 October 2026.** Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol, effort ultra**. **Proved in-note; separate same-model internal review:** [Note 09](../papers/investigations-4/09_reciprocal_hodge_energy/notes/09_SIGNED_LAGUERRE_TRANSFER_AND_COUNT_BOUND_20261022.md) gives root-free complete BW09 signed Laguerre error bounds and a multiplicity-count upper W>=4 pi m N, retaining the boundary amplitude. [Note 10](../papers/investigations-4/09_reciprocal_hodge_energy/notes/10_SIGNED_JET_FLUX_AND_PHASE_TRACE_OBSTACLES_20261022.md) gives an amplitude-weighted signed phase trace T=P-M with a linearly controlled signed potential; existing theta data pay model error below 8.05e-19, without acquiring its value/sign. [Note 11](../papers/investigations-4/09_reciprocal_hodge_energy/notes/11_WEIGHTED_TRACE_PAYMENT_AND_ENDPOINT_OBSTRUCTION_20261022.md) transfers area to BW10's transverse remainder with an explicit collar and physical Laguerre floor. It states: “It does not supply that payment.” Quadratic and smooth positive-source controls quantify the necessary endpoint/normalization costs. [Review 06](../papers/investigations-4/09_reciprocal_hodge_energy/reviews/06_DERIVATIVE_WEIGHTED_TRANSFER_REVIEW_20261022.md); no negative theta estimate, later collision, coverage gain or specialist validation.

**RHE canonical lower estimates, 22 October 2026.** Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol, effort ultra**. **Proved in-note within declared contracts; one fixed canonical lower interval-certified:** [Note12](../papers/investigations-4/09_reciprocal_hodge_energy/notes/12_CANONICAL_ANCHORS_AND_ISOLATED_EVENT_FLOORS_20261022.md) pays curvature and born-cap physical floors from complete canonical normalization/count data plus explicit root isolation, with a no-RH complex-deflation alternative. [Note13](../papers/investigations-4/09_reciprocal_hodge_energy/notes/13_CRITICAL_AMPLITUDE_AND_PROPAGATED_LAGUERRE_FLOORS_20261022.md) proves convex critical amplitude and a nondecreasing full-cap Q minimum in an LP heat regime. [Note14](../papers/investigations-4/09_reciprocal_hodge_energy/notes/14_CANONICAL_BULK_MASS_LOWER_BOUND_20261022.md) certifies M_phi>5.37865e-6 at the fixed t=0 geometry, giving T<=U_P-delta* for a separately paid potential upper. It states: “No P_phi or T_psi value or sign is acquired by this run.” [Review07](../papers/investigations-4/09_reciprocal_hodge_energy/reviews/07_CANONICAL_AMPLITUDE_AND_BULK_LOWER_REVIEW_20261022.md) records separate same-model audits and exact replay. Quantitative event-independent isolation, signed potential and exclusion remain open; no specialist validation.

**RHE completed signed potential and trace, 22 October 2026.** Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol, effort ultra**. [Note15](../papers/investigations-4/09_reciprocal_hodge_energy/notes/15_SIGNED_CANONICAL_POTENTIAL_AND_COMPLETED_TRACE_20261022.md) records **fixed canonical signed potential and trace bounds interval-certified**: P in[1.0703357e-4,1.0768889e-4] and a strengthened whole-cell mass payment give T in[1.2670920e-5,2.6217716e-5]. A tighter independent direct trace in[1.9523542e-5,1.9794809e-5] pays Q>0 on the entire fixed interval without RH. This updates the preceding unacquired-potential status for this geometry. The source concludes: “Stop this fixed-window negative-witness attempt.” [Review08](../papers/investigations-4/09_reciprocal_hodge_energy/reviews/08_SIGNED_POTENTIAL_AND_TRACE_REVIEW_20261022.md) records separate same-model audits and replays. No global sign, cap surplus, endpoint exclusion or specialist validation.

**Late theta caps and complete closures, 22 October 2026.** Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra, effort ultra**. [LHCT Notes 01–04](../papers/investigations-4/11_late_heat_caps_and_charge_transport/notes/README.md) are **proved in-note; internal same-model review**. They construct complete projective root tubes and use full-source complex-time jets to prove the cap error gamma min(S_T D,b)/pi. Fixed-width actual theta caps tend to r_0^2Y/pi per fixed root rank; shrinking-width caps vanish. The complete shrinking boundary's two imaginary faces each tend to half the event charge, and fixed-width connectors cancel the nonzero terminal limit. The source states: “The quantitative result identifies the missing flux rather than simply citing charge conservation.” Conditional geometry and allocation cover every fixed finite candidate height/multiplicity with event-dependent constants, not exclusion or growing-rank uniformity. Reuse for genuine cap/connector accounting. [Review 03](../papers/investigations-4/11_late_heat_caps_and_charge_transport/reviews/03_FINITE_TUBES_CAPS_AND_CLOSURES_INTERNAL_REVIEW_20261022.md); no specialist validation. The opposing canonical signed estimate remains open.

**All-zero transport and the RHE count bridge, 22 October 2026.** For Edward Baker with substantial LLM assistance, **gpt-6-astra, ultra**; internal same-model review. [LHCT Notes 05–08](../papers/investigations-4/11_late_heat_caps_and_charge_transport/research-progress/02_ZERO_COUNT_TRANSPORT_AND_PAIR_MATRIX_PROGRESS_20261022.md) consolidate the existing real cap/wall balance, prove a fixed-rank canonical inverse-square matrix rate O_K((L√κ)⁻¹), and give the exact low-value derivative-energy count W_<ε=4πεN below a paid boundary amplitude. RHE04's certified disk supplies an actual theta corollary. The progress source states: “the canonical signed exclusion estimate is open.” Weak PCC admits sparse defects and does not pay inverse-square weights, exterior forcing or complex cap phase. [Review 04](../papers/investigations-4/11_late_heat_caps_and_charge_transport/reviews/04_ZERO_COUNTS_PAIR_MATRICES_AND_HODGE_BRIDGE_REVIEW_20261022.md); no new PCC or simplicity theorem.


**Base zero-count/heat/Hodge manuscript, 22 October 2026.** For Edward Baker with substantial LLM assistance, **gpt-6-astra, ultra**; **proved in manuscript, internal same-model review**. The [maintained manuscript](../papers/investigations-4/manuscript/zero_count_heat_transport/README.md) consolidates full transport and adds p-power/q-cover counts, quantitative regularization/localization costs and elementary all-mode/all-tail theta concentration with a fixed-rank matrix rate. Its [extensions note](../papers/investigations-4/notes/07_LOCALIZED_ROOT_COVER_ENERGY_AND_MANUSCRIPT_EXTENSIONS_20261022.md) states: “The cumulative cancellation theorem does not differentiate an uncontrolled asymptotic remainder.” Numerics are confined to the appendix. [Detailed review](../papers/investigations-4/reviews/01_ZERO_COUNT_HEAT_TRANSPORT_MANUSCRIPT_REVIEW_20261022.md); the initial build had no stated growing-rank corollary (superseded on that point by the continuation below); no signed exclusion, priority claim or specialist validation.

**Controlled-divisor stability and growing spatial clocks, 22 October 2026.** For Edward Baker with substantial LLM assistance, **gpt-6-astra, max**; **proved in-note and manuscript, same-assistant self-review only**. [I4 Note 09](../papers/investigations-4/notes/09_SHARP_C2_DIVISOR_STABILITY_20261022.md) proves harmonic reproduction, C² bias with attained factor p/(p+2/m), and direct divisor error O(η^min(1,2/m)) under complete disk, boundary and unit control, with exact sharp-exponent examples. It states: “The result is characterized as a useful explicit specialization; no novelty claim is made.” [Note 10](../papers/investigations-4/notes/10_GROWING_CLOCK_WINDOWS_20261022.md) extracts normalized matrix error O(K/(L√κ)) for K=o(L√κ), uniformly in block size; K=o(√κ/L) suffices for vanishing physical error. [Self-review](../papers/investigations-4/reviews/02_DIVISOR_STABILITY_AND_GROWING_WINDOWS_SELF_REVIEW_20261022.md). These improve the earlier stability/spatial scope; no uniform merging-cluster theorem, growing-population time law, paid exterior force, signed exclusion or specialist validation.

**Initial cap and high-height birth budgets, 23 October 2026.** For Edward
Baker with substantial LLM assistance, **gpt-6-astra, max**; **proved
in-note using the identified Polymath estimates; same-assistant self-review**.
[I4 Note 11](../papers/investigations-4/notes/11_INITIAL_CAP_FUTURE_BIRTHS_AND_HEIGHT_BOUNDARIES_20261023.md) derives the literal
initial-cap defect sum(m-1), wall flux (T-delta)log(R/(4 pi))/16+O(1),
and a relative O_alpha(R^(alpha-1)) upper on real creation events after
delta_R=A/(alpha log R), 0<alpha<1. It states: “This localizes the next
task to a shrinking interval instead of rejecting relative progress.”
The early layer is unestimated; constants are not numerically acquired.
The physical Hopf cap has a separate product formula and no new complete
closure estimate. [Self-review](../papers/investigations-4/reviews/03_INITIAL_CAP_AND_HEIGHT_BOUNDARY_SELF_REVIEW_20261023.md).

**Growing complex caps and focused physical transport, 23 October 2026.** For Edward Baker with substantial LLM assistance, **gpt-6-astra, max**; **proved in the new maintained manuscript, within its stated geometry and asymptotic regime; same-assistant self-review only**. [I4 Note 12](../papers/investigations-4/notes/12_GROWING_COMPLEX_CAPS_AND_VANDERMONDE_PHASE_20261023.md) proves an O(m eta) lifted Vandermonde logarithm bound and actual complex-time caps through K=o(L√κ). The cap per root tends to r²Y/pi, with the analytic factor supplying the leading term; late imaginary faces on [theta T,T] are O(1/log T) per root and projective sides vanish. The source states: “Core constants have not been bounded uniformly as height grows.” Fixed-core half-charge allocation is retained, not converted into an independent event budget. [Separate paper](../papers/investigations-4/manuscript/topological_zero_transport/README.md), [literature/proof review](../papers/investigations-4/reviews/04_TOPOLOGICAL_TRANSPORT_LITERATURE_AND_PROOF_REVIEW_20261023.md); existing catalogue preserved. No complete early-boundary bound, fixed-heat all-height theorem, RH conclusion or confirmed novelty.

**Usefulness qualification of the focused manuscript, 23 October 2026.** For Edward Baker with substantial LLM assistance, **gpt-6-astra, max**; same-assistant assessment. [Review 05](../papers/investigations-4/reviews/05_TOPOLOGICAL_TRANSPORT_USEFULNESS_ASSESSMENT_20261023.md) spells out the existing exact cancellation I_T+E_(a,T)=I_a on regular late tubes and notes that the full cap proof bypasses the Vandermonde lemma. It states: “Moving T farther out does not improve this complete event balance by itself.” The preceding analytic scope remains; no comparative zero-free-region or verification-cost gain is established. The next research requirement is a coupled early estimate with a matched direct comparison, not further polishing or a universal no-go claim.


**Finite backward-cap contract and scoped comparison, 23 October 2026.** For Edward Baker with substantial LLM assistance, **gpt-6-astra, effort ultra**; **proved in-note, separate same-model internal review**. [HDC Notes 02–03](../papers/investigations-4/12_height_dependent_heat_contours/notes/README.md) give a complete fixed-box four-jet boundary formula and boundary-only root reduction retaining every complement. Root disks carry k_rho Q and complements (1-k_rho)Q. A quadratic heat control has nonnegative real relative energy but negative complete complex-time contribution. The source states: “transport gives **exactly the same payment for these shared holomorphic coefficients**”; uniform pathwise triangle errors are larger along the broken path under the stated matched regular-tube/complement assumptions. This is a scoped estimator comparison, not a universal obstruction. [Internal review](../papers/investigations-4/12_height_dependent_heat_contours/reviews/01_FINITE_CONTRACT_AND_COUPLED_ESTIMATOR_REVIEW_20261023.md), [exact algebra checks](../papers/investigations-4/12_height_dependent_heat_contours/numerics/01_BOUNDARY_AND_RELATIVE_ENERGY_CHECKS_20261023.json). HDC-01/HDC-02 specification/expression complete; no theta boundary minima, cap interval, comparative gain or specialist validation acquired.

**HDC statistical simplicity consumers, 23 October 2026.** For Edward Baker with substantial LLM assistance, **gpt-6-astra, ultra**; **proved elementary finite transfers, separate same-model checks; source upper estimates open**. [Notes 05–06](../papers/investigations-4/12_height_dependent_heat_contours/notes/README.md) connect complete earlier projected-pair counts and the existing Vandermonde Hessian to RH-conditional density-one simplicity. The inherited globally adjacent-gap bound and a matching comparison give M_0<=6 Tr[4tL(I+4tL)^−1]. The source states: “Neither is an independent theta spectral bound or a new RH-conditional simplicity proportion.” [Review](../papers/investigations-4/12_height_dependent_heat_contours/reviews/02_PAIR_STATISTICS_AND_SIMPLICITY_TRANSFER_REVIEW_20261023.md). This application does not first require a physical cap bound.

**HDC analytical estimates and scoped late-data screens, 23 October 2026.** For Edward Baker with substantial LLM assistance, **gpt-6-astra, ultra**; **proved in-note within stated hypotheses; separate same-model internal reviews**. [Notes 07–10](../papers/investigations-4/12_height_dependent_heat_contours/notes/README.md) give a complete canonical distant-force error O(N C_T log R/R), finite relative-wall/graph and inverse estimates, and sharp M_0≤4q (superseding the preceding constant 6). Two-sided short-gap/filter bounds identify the unpaid microscopic input. Note 10 proves q/N→1 in the published high-height clock regime; Note 09 gives log A~T(log T)²/(2pi²) for the fixed-rank scalar backward implementation. Its scope is: “It does **not** exclude a joint correlated source/root transport, another observable or a better source theorem.” [Round review](../papers/investigations-4/12_height_dependent_heat_contours/reviews/04_ANALYTICAL_RESEARCH_ROUND_REVIEW_20261023.md), 862 exact-rational assertions and floating diagnostics. No microscopic theta upper estimate, simplicity improvement or specialist validation.

**HDC coefficient-filter continuation, 23 October 2026.** For Edward Baker with substantial LLM assistance, **gpt-6-astra, ultra**; **proved finite error theorem, separate same-model internal review**. [Note 11](../papers/investigations-4/12_height_dependent_heat_contours/notes/11_FOREST_POLYNOMIAL_AND_GAP_FREE_FILTER_ENCLOSURE_20261023.md) clears the inverse-square determinant by one discriminant and encloses q from the complete prepared coefficients and a coupled polynomial residual, without internal root isolation. It states: “Test (7) does not imply that the roots are simple.” The method covers fixed-scale real separated doubles; higher collisions and heat-scale source precision retain explicit conditions. [Review](../papers/investigations-4/12_height_dependent_heat_contours/reviews/09_FOREST_FILTER_AND_COLLISION_CONDITIONING_REVIEW_20261023.md), 219 additional exact assertions. No canonical coefficient acquisition, theta upper estimate or simplicity improvement.

**HDC complete coefficient transport, 23 October 2026.** For Edward Baker with substantial LLM assistance, **gpt-6-astra, ultra**; **proved finite transport/error theorems, separate same-model review**. [Note 12](../papers/investigations-4/12_height_dependent_heat_contours/notes/12_COUPLED_COEFFICIENT_BACKWARD_TRANSPORT_20261023.md) and its wall-budget appendix derive the complete prepared-polynomial equation and commuting nilpotent source operators, giving a finite backward propagator through internal collisions. The appendix states: “polynomial coefficient transport alone does not prove simplicity.” The full source moments, reference defects, microscopic precision and large-rank costs remain inputs. [Review](../papers/investigations-4/12_height_dependent_heat_contours/reviews/10_COUPLED_COEFFICIENT_TRANSPORT_REVIEW_20261023.md), 252 additional exact assertions. No canonical moment budget or theta upper estimate.


- **HDC actual-source and manuscript checkpoint (23 October 2026).** Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra, ultra**. [Note 13](../papers/investigations-4/12_height_dependent_heat_contours/notes/13_COMPLETE_THETA_WALL_AND_COEFFICIENT_CERTIFICATE_20261023.md) is **interval-certified** on the original finite complex-time box: complete count two, nonzero discriminant and full first-jet floor. Direct terminal filter evaluation is tighter. [Note 14](../papers/investigations-4/12_height_dependent_heat_contours/notes/14_MICROSCOPIC_COMPLETE_REFERENCE_AND_HEAT_DEFECT_20261023.md) gives an analytic corrected microscopic reference with explicit field and heat-defect budgets, leaving its high-height wall floor unpaid. [Note 15](../papers/investigations-4/12_height_dependent_heat_contours/notes/15_COMPLETE_PHYSICAL_CAP_COMPARISON_20261023.md) encloses every original cap face but records: “Both lower endpoints are negative.” This is a scoped failure of the bounded range-quadrature implementation to establish a useful lower bound, not a sign claim about the exact cap. [Working manuscript](../papers/investigations-4/12_height_dependent_heat_contours/manuscript/main.tex) and [research reset](../papers/investigations-4/12_height_dependent_heat_contours/notes/16_RESEARCH_RESET_AND_NEXT_STEPS_20261023.md); no global simplicity or RH theorem.

**Moving reference boundaries and ordered theta flux, 23 October 2026.** For Edward Baker with substantial LLM assistance, **gpt-6-astra, ultra**; **proved in manuscript at finite analytic scope, separate same-model internal review**. [Selective paper](../papers/investigations-4/12_height_dependent_heat_contours/manuscript/book.tex) gives the exact moving nonreal balance, sharp D≤R and M≤3R/2, reference determinant H_zz G_z−H_z G_zz, and independent mismatch bounds. Its complete theta head–tail source has decreasing T_N/A_N; antisymmetrization gives a positive ordered source difference and a strictly smaller specified absolute majorant with quadratic diagonal cancellation. The source states: “The arithmetic tail bounds and signed determinant have no proved useful height-uniform size here.” Positive square reweightings retain the ordering. [Review](../papers/investigations-4/12_height_dependent_heat_contours/reviews/15_RELATIVE_FLUX_ANALYTIC_MANUSCRIPT_REVIEW_20261023.md); useful earlier nonreal discrimination, global simplicity and specialist validation remain open.

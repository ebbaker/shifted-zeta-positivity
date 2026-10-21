# Exact theta identities, positive transforms, and arithmetic reductions

15 October 2026. Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork.

Coverage and scope revised 16 October 2026 for Edward Baker with substantial
LLM assistance: **gpt-6-astra (Codex)**, reasoning effort **ultra**.

## Summary

These are exact source identities, auxiliary positivity theorems and scoped
obstructions. Some normalized arithmetic laws identify theta itself; this
corrects the earlier blanket assertion that every identity here is shared
by a collision control. Identifying the source still leaves its signed
oscillatory estimate to be proved.

- **Covariant theta-source formula (21–22).**
  \(\Phi=\frac{y^{1/4}}{16\pi^2}(y^2\mathcal D^4\vartheta-3\pi^2\vartheta)(0,iy)\).
  The Hermite-weighted covariant jets' inversion law reproduces source
  reflection. The genuine bundle, curved metric, ASD connection and its
  physical restriction are summarized separately in [16](16_hypercomplex_reductions_and_geometric_realizations.md).
- **Positive theta primitive and reconstruction (21 Note 52).** For
  \(\psi(u)=e^u\sum_{n\ge1}e^{-\pi n^2e^{4u}}\) and
  \(J(t,x)=\int_0^\infty e^{tu^2}\psi(u)\cos(xu)\,du\),
  \(J>0\) for every real \(x\), \(0\le t\le1/2\), and exactly
  \[
  8H=\tfrac12+(2t-x^2-1)J+4txJ_x-4t^2J_{xx}.
  \]
  The source calls this a “concrete positive auxiliary channel”. The
  modular boundary constant is retained; \(J\sim1/(2x^2)\), whereas
  physical jets decay exponentially. At each fixed real time, the complete
  \(H\) satisfies no nonzero homogeneous finite linear differential identity
  with rational coefficients on an open pole-free interval. This excludes
  that exact-closure class, not stationary-set identities, residual bounds,
  transcendental coefficients, nonlocal relations or inequalities.
- **Positive complete arithmetic packets (3/11 Note 04, 18 October).**
  For 0<=t<=1/2, nonzero bounded nonnegative combinations of n>=2 physical modes
  have positive cosine transforms. The {2,3} packet has uniform relative
  error below 7.3e-25 against the positive arithmetic tail; its logarithmic
  curvature is bounded by 117, giving a carrier payment below 117 E.
  Full modular reflection cancels all algebraic tails with the first mode;
  the signed physical residual remains open. **Proved in-note**, constants
  Arb-certified, [same-assistant self-review only](../papers/investigations-3/11_arithmetic_collision_rigidity/reviews/02_POSITIVE_PACKET_AND_MODULAR_CANCELLATION_SELF_REVIEW_CODEX_20261018.md).
  [Source and certificate links](../papers/investigations-3/11_arithmetic_collision_rigidity/notes/04_POSITIVE_ARITHMETIC_PACKETS_AND_MODULAR_CANCELLATION_CODEX_20261018.md). The
  [self-contained working manuscript](../papers/investigations-3/11_arithmetic_collision_rigidity/manuscript/README.md)
  now supplies the full derivation and rational constant enclosures;
  [manuscript self-review](../papers/investigations-3/11_arithmetic_collision_rigidity/reviews/03_MANUSCRIPT_SELF_REVIEW_CODEX_20261018.md)
  remains same-assistant. Its scope is explicit: “The identity alone does
  not reduce the strength of the missing estimate.”
  Added for Edward Baker with substantial LLM assistance, **gpt-6-astra, max**.
- **Finite \(E_8\) source bridge (21 Note 48).** An eight-character selector
  projects onto \(2\mathbb Z^2\oplus D_6\) and exactly recovers the
  two-variable theta product; differentiation recovers the complete source
  product. Every differentiated character sector is a finite combination
  of translated full sources and is globally heat-integrable. The untwisted
  differentiated sector can be negative, and translated fields are observed
  at complex-shifted arguments. This bridge is not a positivity theorem.
- **Poisson correlations and parity cancellation (21 Notes 38, 42; 22 §9).**
  Complete-source correlations obey
  \((\partial_t+\partial_x^2)\mathcal L_0=2\mathcal L_1\).
  Exact parity–Poisson identities retain the full source and heat weight. The specified separate modes and finite centered rectangles
  fail global positive-time integrability; smooth negative-quartic windows
  restore joint integrability. At each fixed heat time, actual-theta
  even/odd sectors have opposite
  algebraic tails although their sum decays faster than every power, so
  separate absolute estimates lose essential cancellation.
- **Multiplicative dilations and sieve algebra (22 §12).**
  \(D_d\Phi=\sum_{d\mid n}\phi_n\), with exact sieve/Möbius formulas,
  transformed lower intervals and uniform moment tails. The full-line law
  \(H_{D_d\Phi}(t,x)=d^{-1/2}e^{ta^2-iax}H_\Phi(t,x+2ita)\),
  \(a=\tfrac12\log d\), retains the complex shift. Separated Möbius series
  fail the term test; ordinary Poisson endpoint modes lack separately
  convergent positive-time source integrals. The complete cutoff identities
  remain valid.
- **Coefficient rigidity and recurrence stability (22 §§9–10).** For
  positive even polynomial-growth coefficients with \(a_0=1\), the full
  rank-one addition array forces \(a_n=c^{n^2}\); the primitive endpoint
  forces \(c=1\). Gaussian-weighted recurrence-defect identities quantify
  coefficient/source error. For normalized nonnegative coefficients with
  \(a_0=1\) and \(a_{k-1}-2a_k+a_{k+1}=0\) for \(1\le k\le N\), the
  rate is sharply algebraic \(1/M\), \(M=N+1\); the additional first
  coefficient \(a_1=1\) improves it to a Gaussian tail. These are stability and rigidity results,
  not physical sign estimates.
- **Currents and signed quotients (22 §§10–11).** Exact joint currents keep
  both lower boundaries and finite upper corrections. The finite-range,
  finite-real-frequency polynomial-amplitude obstruction applies before
  integration; it leaves nonpolynomial, nonlocal and one-sided estimates
  open. On a finite-dimensional homogeneous real relaxation, kernel
  inclusion is required for a nontrivial signed observation to descend to
  the physical jet; then its optimal nonnegative constant is
  \((a\cdot b+\|a\|\|b\|)/2\). Uniformity near degeneration and actual-theta
  applicability are separate obligations.
- **Two cosets and Hecke (09, 18, 06).**
  \(F_0=A\otimes A+B\otimes B\), \(F_1=A\otimes B+B\otimes A\), with
  complete tails; the physical insertion removes the Eisenstein constant
  term. Folded same-parity responses are negative
  (\(C_0=-4c^2x^{-6}+\cdots\)); the cosets are not separately positive channels.
- **Other positive channels and path corrections.** Investigation 02's
  distinct Volterra inverse satisfies \(R'+5R=-4\pi e^{-4u}\Phi\), with
  \(P_t(x)>1/[3000(1+x^2)]\) for \(0\le t\le1\), but no polynomial
  relative physical-energy margin. Investigation 20 proves exact
  finite-time residual/endpoint path identities and certifies a Hubbard
  trial upper energy \(-0.50215\ldots<-1/2\); the terminal correction cannot
  be dropped.

## Status

Written analytic proofs, with the sources' internal LLM reviews and scoped
exact or interval checks. Positive-primitive and \(E_8\) results have
analytic review; they do not rely on numerical sign samples. Polynomial
and rational-surrogate replays check the stated finite algebra, not an
unbounded theta inequality.

## Caveats

The positive primitive, exact arithmetic discrimination and convergent
character bridge are reusable results in their own right. Their separate
norms or identities do not control the signed physical observation at
energy scale. In particular, [12](12_collision_controls_and_screening.md)
records a colliding source with the same positive-primitive structure and
all algebraic primitive asymptotics. The scoped exclusions above must not
be extended to all source identities or geometric methods.

## Reusable for

Complete-source reconstruction, integrable character decompositions,
coefficient stability, preserved parity cancellations, and exact boundary
and cutoff accounting for future estimates.

## Where

- [21 positive primitive and rational nonclosure](../papers/investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/52_POSITIVE_THETA_PRIMITIVE_AND_DIFFERENTIAL_CLOSURE_20261015.md), [Review 31](../papers/investigations-2/active/21_quaternion_theta_geometry/reviews/31_SIGNED_FORMS_PRIMITIVE_AND_SOURCE_CONTROL_REVIEW_20261015.md); [finite E8 bridge](../papers/investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/48_E8_CHARACTER_PROJECTION_AND_SIGNED_HEAT_SECTORS_20261015.md), [Review 29](../papers/investigations-2/active/21_quaternion_theta_geometry/reviews/29_OCTONIONIC_SIGNED_BOUND_ANALYTIC_REVIEW_20261015.md).
- [21 complete correlations and heat hierarchy](../papers/investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/36_COMPLETE_THETA_CORRELATIONS_AND_SIGN_TARGETS_20261015.md); [21 parity–Poisson identity](../papers/investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/38_POISSON_PARITY_CORRELATION_AND_HEAT_OBSTRUCTION_20261015.md), [localized-mode obstruction](../papers/investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/42_LOCALIZED_POISSON_MODE_OBSTRUCTIONS_20261015.md), [Review 28](../papers/investigations-2/active/21_quaternion_theta_geometry/reviews/28_LOCALIZED_POISSON_AND_EFFECTIVE_BUDGET_REVIEW_20261015.md).
- [22 manuscript](../papers/investigations-2/active/22_theta_manifold_geometry/manuscript/theta_manifold_geometry.tex), §§8–12; [coupled-product rigidity](../papers/investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/06_COUPLED_THETA_PRODUCT_AND_PARITY_SECTORS_20261015.md), [parity cancellation](../papers/investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/07_PARITY_STRIP_CUTOFF_AND_FULL_STARTING_FACTOR_20261015.md), [recurrence stability](../papers/investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/08_ADJOINT_RECURRENCE_ENDPOINT_EXPERIMENT_20261015.md); [Reviews 07](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/07_COUPLED_PRODUCT_AND_REFLECTION_CONTROL_REVIEW_20261015.md) and [08](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/08_ADJOINT_RECURRENCE_AND_GEOMETRIC_REVIEW_20261015.md).
- [Joint polynomial-current scope](../papers/investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/09_JOINT_SOURCE_CURRENT_AND_POLYNOMIAL_OBSTRUCTION_20261015.md), [signed quotient](../papers/investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/02_SIGNED_OBSERVATION_QUOTIENT_AND_COEFFICIENT_SINGULARITIES_20261015.md), [Review 10](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/10_JOINT_SOURCE_CURRENT_AND_SIGNED_QUOTIENT_REVIEW_20261015.md).
- [Complete arithmetic dilations](../papers/investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/11_MULTIPLICATIVE_DILATION_AND_COMPLETE_HEAT_PACKETS_20261015.md), [nonlocal audit](../papers/investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/12_NONLOCAL_ARITHMETIC_MULTIPLIERS_AND_BOUNDARY_OBSTRUCTIONS_20261015.md), [Review 14](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/14_MULTIPLICATIVE_DILATION_AND_NONLOCAL_ARITHMETIC_REVIEW_20261015.md).
- Earlier programs: [09 two-coset reduction](../papers/investigations-2/inactive/09_rank_two_theta_addition/notes/1_COMPLETE_TWO_COSET_REDUCTION_20261013.md), [18 Hecke cusp formula](../papers/investigations-2/active/18_rank_two_automorphic_lift/notes/1_CUSP_FORMULA_HECKE_AND_CONTROLS_20261013.md), [06 parity obstruction](../papers/investigations-2/active/06_paired_kernel_factorization/notes/1_FOLDED_PARITY_CUSP_AND_FACTORISATION_OBSTRUCTION_20261013.md), [coset review](../papers/investigations-2/brainstorm/reviews/RANK_TWO_TO_PAIRED_KERNEL_REVIEW_CODEX_20261013.md); [02 Volterra note](../papers/investigations-2/active/02_angular_jacobi_gluing/notes/2_VOLTERRA_RECOVERY_POSITIVE_ANCHOR_AND_TRANSFER_GAP_20261013.md); [20 path identities](../papers/investigations-2/active/20_constrained_operator_squares/notes/RESIDUAL_CORRECTED_HEAT_TRAJECTORY_IDENTITIES_20261014.md), [path review](../papers/investigations-2/active/20_constrained_operator_squares/reviews/BOUNDED_PROGRAM_AND_DIRAC_CONTINUATION_REVIEW_20261014.md).


**18 October 2026 continuation, investigation 3/11.**
[Note 05](../papers/investigations-3/11_arithmetic_collision_rigidity/notes/05_COMPLEX_STRIP_CARRIERS_AND_SHARP_LOG_DERIVATIVES_CODEX_20261018.md)
proves positive real part for bounded positive packets starting at m>=2 on
|Im z|<=pi m^2, and the real logarithmic bound beta^2+|beta_x|<=1/(4m^4).
For A this strengthens the manuscript's valid 117 E payment to E/64;
"The signed first term in (4) remains uncontrolled."
[Review 04](../papers/investigations-3/11_arithmetic_collision_rigidity/reviews/04_MANUSCRIPT_AUDIT_AND_STRENGTHENING_REVIEW_CODEX_20261018.md):
**proved in-note; additional same-model internal checks**, with rational
certificates for the new remainder constants, no specialist review.
The finite-prime collision controls retain the new strip geometry.
[Note 06](../papers/investigations-3/11_arithmetic_collision_rigidity/notes/06_CANCELLATION_PRESERVING_APPROXIMATION_AND_NEWMAN_ROADMAP_CODEX_20261018.md)
adds an explicit shifted finite-mode derivative error, extending 07's
existing contour method; the finite exclusion margin remains unproved.
Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra,
ultra**. That review preceded manuscript incorporation; the current milestone below
supersedes that document-status sentence.


**18 October 2026 earlier manuscript integration, investigation 3/11.** The
[current manuscript](../papers/investigations-3/11_arithmetic_collision_rigidity/manuscript/positive_arithmetic_packets/main.tex) now includes the E/64 carrier
payment, complex-strip bounds, sharper remainder jets, complete shifted-source
tail theorem and envelope-relative asymptotic. **Proved in-paper; internal
LLM checks by contributing Sol and Astra assistants**, both effort ultra;
[Review 05](../papers/investigations-3/11_arithmetic_collision_rigidity/reviews/05_UPDATED_MANUSCRIPT_INTEGRATION_REVIEW_CODEX_20261018.md) pins the revised source set and
scalar certificate. Section 7 states: “Neither is a lower bound for the
complete oscillatory field.” No new collision exclusion or Newman bound.
The [updated overview](../papers/investigations-3/11_arithmetic_collision_rigidity/research-overview/02_UPDATED_RESEARCH_OVERVIEW_AND_SOL_EXECUTION_PLAN_20261018.md) assigns
every future stage to GPT-6.1 Sol. Prepared for Edward Baker with substantial
LLM assistance; no independent specialist review.

**18 October 2026 current-results integration, investigation 3/11.**
The [current manuscript](../papers/investigations-3/11_arithmetic_collision_rigidity/manuscript/README.md)
now incorporates Notes 07–14: effective nonstationary and constant-distance
tails, interval-certified signed rectangles, the complete wall and
finite-height propagation, and the exp(20/epsilon) real exterior.
**Proved in-paper, with explicitly computer-assisted finite certificates;
internal LLM integration checks** in [Review 13](../papers/investigations-3/11_arithmetic_collision_rigidity/reviews/13_CURRENT_RESULTS_MANUSCRIPT_INTEGRATION_REVIEW_20261018.md)
and a [fresh replay manifest](../papers/investigations-3/11_arithmetic_collision_rigidity/numerics/MANUSCRIPT_INTEGRATION_REPLAY_20261018.json).
E>0 holds on [1/100,1/5] × [-1001,1001]; the real exterior begins at
exp(20/epsilon) for epsilon<=t<=1/2. The manuscript states: “The bridge
1001<|x|<e^2000 remains open on the stated slab.” This supersedes the earlier
absence of finite exclusion and unevaluated onset, not the global gap.
No new Newman bound. Prepared for Edward Baker with substantial LLM
assistance, **gpt-6-astra, actual effort max**; no specialist review.

**18 October 2026 S01 bounded endpoint-pairing continuation, investigation 3/11.**
The [opening note](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/01_modular_self_duality/notes/01_PAIRED_ENDPOINT_REMAINDER_AND_BOUNDED_COMPARISON_20261018.md)
proves a signed paired-endpoint refinement of the existing nonstationary
arithmetic tail, including complex-neighborhood spectral jets. Fresh
192/256-bit complete comparisons on [1/100,1/5] × [999,1001] keep the same
retained polynomial and common costs; the primary added-error reductions
are about 14.8%, 7.2% and 3.0% at orders 0–2. **Proved in-note; outward
scalar and complete-evaluator checks; internal same-model review** in the
[assessment](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/01_modular_self_duality/reviews/01_PAIRED_ENDPOINT_INTERNAL_REVIEW_20261018.md).
The note states: “It does not give a sign or a lower bound for the retained
field”. No new coverage or Newman bound. Prepared for Edward Baker with
substantial LLM assistance, **gpt-6.1-sol, actual effort ultra**.

**18 October 2026 S04 phase-retaining scaling continuation, investigation 3/11.**
[Note 01](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/04_time_height_scaling/notes/01_PHASE_RETAINING_FULL_CUTOFF_SCALING_20261018.md)
quantifies the earlier first-jet coordinate asymptotics for a full-cutoff
signed scalar and its actual fixed-time derivative. On kappa in [1,2],
0<t<=1/20, the Euclidean replacement error in (F/2,2Fx/L) is below
exp(-kappa*(kappa+12)/(16*t)); the existing complete RS remainder is paid
separately. **Proved in-note; outward finite point/transition checks;
same-model internal review** in the [assessment](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/04_time_height_scaling/reviews/01_FULL_CUTOFF_SCALING_INTERNAL_REVIEW_20261018.md).
The note states: “This is an explicit quantitative completion of known
coordinate asymptotics.” It is not a new cancellation estimate, smaller
total error, or uniform signed lower bound. For Edward Baker with substantial
LLM assistance, **gpt-6.1-sol, actual effort ultra**; no specialist review.


**19 October 2026 S02 complete evaluated jets, investigation 3/11.**
[Note 03](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/02_cutoff_reflection/notes/03_COMPLETE_FROZEN_JETS_AND_PAID_CONSUMERS_20261019.md)
proves the real-Schur second-jet enclosure and gives an **interval-checked
certificate on the already covered B box**, using both frozen and full
corrections. Coupled residuals certify L0>E/100 on 4096/4096 cells versus
1770 for independent frozen boxes. Full paid firstjet>0.9702739184 exceeds
frozen>0.9686625938; fresh additional-source>1.3473946960 remains stronger.
[Separate same-model review and replay](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/02_cutoff_reflection/reviews/03_COMPLETE_JET_INTERNAL_REVIEW_20261019.md).
No new coverage, matched-cost gain or Newman bound. For Edward Baker with
substantial LLM assistance, **gpt-6.1-sol, ultra**; no specialist review.


**19 October 2026 S03 filtered residual, investigation 3/11.**
[Note 03](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/notes/03_FILTERED_COMPLETE_RESIDUAL_AND_SPLIT_PREFIX_OBSTRUCTION_20261019.md) derives the complete signed source-filtered
discrepancy and tail/heat-forcing ledger. A **proved scoped obstruction**,
with an outward 192/256-bit witness, shows that separately bounding the
physical-source and full-approximation prefixes pays >1.912087 on B.
[Separate same-model review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/reviews/03_FILTERED_RESIDUAL_INTERNAL_REVIEW_20261019.md). This is not a
new recombined residual allowance or coverage gain; the signed arithmetic
estimate remains open. Prepared for Edward Baker with substantial LLM
assistance, **gpt-6.1-sol, ultra**; no specialist review.

**19 October 2026 S03 analytic-only allowance, investigation 3/11.**
[Note 04](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/notes/04_PHASE_AWARE_ANALYTIC_ALLOWANCE_AND_KERNEL_VARIATION_OBSTRUCTION_20261019.md) gives a **proved analytic-only bound with outward-evaluated constants**:
complete residual increment <0.812260 on B versus same-input independent
endpoints <0.827470 (>1.8381% allowance decrease). Known endpoint phase and
real-Schur geometry suffice. The note states: “It does not explain the much
stronger observed arithmetic cancellation”. The retained source-informed
<0.000266448 bound stays stronger. A **proved scoped payment obstruction**
gives >4037.45136 for one cell under absolute shifted-channel kernel
variation payments; this is not actual residual or quadrature error.
[Separate same-model review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/reviews/04_PHASE_ALLOWANCE_AND_KERNEL_OBSTRUCTION_INTERNAL_REVIEW_20261019.md). No new coverage or height-uniform result. Prepared for Edward Baker
with substantial LLM assistance, **gpt-6.1-sol, ultra**; no specialist review.

**19 October 2026 S03 calibrated consumer, investigation 3/11.**
[Note 05](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/notes/05_CALIBRATED_FIRST_JET_AND_MATCHED_DIRECT_COMPARISON_20261019.md) is a **complete known-box interval consumer comparison**, with a
**proved scoped scalar/vector inequality** for the same nominal anchor ball
and residual increment disk. Exact dyadic anchors and their uncertainty
are retained. Paid calibrated J radius>1.3859351576 versus scalar>1.1288659652;
matched source direct>1.3898732635 remains stronger. The note states:
“The source direct test also receives the same midpoint propagation as the
calibrated test.” Raw-source>1.3473946960 alone is an inadequate strongest
comparator. [Separate same-model review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/reviews/05_CALIBRATED_CONSUMER_COMPARISON_INTERNAL_REVIEW_20261019.md). No new residual allowance, coverage or matched-cost result; stop this
fixed-box comparison. Prepared for Edward Baker with substantial LLM
assistance, **gpt-6.1-sol, ultra**; no specialist review.

**19 October 2026 G3 arithmetic continuation, investigation 3/11.**
[Note 06](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/notes/06_ARITHMETIC_GAMMA_AND_EDGE_CORRECTIONS_20261019.md) gives a **proved bounded finite-mode remainder theorem**:
relative gamma/heat errors <6e-7,<6e-8,<1.2e-8 through spatial order 2,
with uniform finite filtered payment <3.874872e-6 on B,N=8.
Certified center finite and inferred edge defects have opposite signs;
the prescribed RS hierarchy requires its gamma prefactor. That hierarchy
has unpaid tails/RS remainder, so full G3 remains **partially explained**.
A finite CR identity identifies two coherent-extension endpoint payments;
complete edge jets and signed prefix remain open. [Separate same-model review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/reviews/06_ARITHMETIC_GAMMA_AND_EDGE_INTERNAL_REVIEW_20261019.md).
No complete-H allowance, new consumer, coverage or height-uniform result.
Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol,
actual effort ultra**; no independent specialist review.

**19 October 2026 G3 complete arithmetic allowance, investigation 3/11.**
[Note 07](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/notes/07_COMPLETE_ARITHMETIC_EDGE_AND_RESIDUAL_INCREMENT_20261019.md) is a **proved bounded arithmetic estimate with outward constants**.
RS8, exact gamma, CR coherence, both Gaussian tails and a paid polynomial
model give complete edge Q-jet errors<6e-8,<6e-8,<1.2e-7 on B,N=8.
Recombined signed endpoint payment proves **abs(I_r)<0.000854** without H
Taylor/source-quadrature data, >950-fold smaller than prior independent
analytic-only0.812260. Source-informed0.000266448 remains stronger.
This completes the earlier fixed-pilot edge/prefix obligation, not global
G3/height control. [Separate same-model review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/reviews/07_COMPLETE_ARITHMETIC_EDGE_AND_INCREMENT_INTERNAL_REVIEW_20261019.md) and fresh 192 replay agree;
nominal 192/256 arithmetic uses 512 guardbits for profile derivatives.
No consumer rerun, new coverage or matched-cost result. For Edward Baker
with substantial LLM assistance, **gpt-6.1-sol, actual effort ultra**.


**19 October 2026 S04-T2 signed Gaussian average, investigation 3/11.**
[Note 02](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/04_time_height_scaling/notes/02_GAUSSIAN_SIGNED_CORE_AND_COMPLETE_AVERAGED_VALUE_20261019.md) is **proved in-note** using the imported
complete RS source contract. On kappa[1,2],0<t<=1/20, a phase-matched finite
Gaussian intermediate average is <1.5e-6; all-channel physical average
satisfies abs(B-1)<0.11, including source/cutoff/window payments. Weighted
Q/2 value energy>0.198. This completes the named averaged-functional gate,
not pointwise core control or noncollision. S04-T3 was Waiting at that stage.
[Separate same-model review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/04_time_height_scaling/reviews/02_GAUSSIAN_SIGNED_CORE_INTERNAL_REVIEW_20261019.md),192/256 and fresh192
checks support the proof. Different norm from the earlier hard-window
derivative mean square; no same-norm superiority claimed. For Edward Baker
with substantial LLM assistance, **gpt-6.1-sol, actual effort ultra**.


**19 October 2026 S04-T3 local transfer and scoped cutoff payment, investigation 3/11.**
[Note 03](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/04_time_height_scaling/notes/03_UNIFORM_LOCAL_RESIDUAL_TRANSFER_AND_CUTOFF_PAYMENT_OBSTRUCTION_20261019.md) is **proved in-note**
from the inherited complete disk theorem. Uniform fixed-cutoff half-disk
charts give complete endpoint increment<46.679exp(-b*/t), including anchor
uncertainty. The stipulated independent coefficientwise transition disks
across kappa[1,2] cost>.99exp(1/(4t)). “Actual jumps may cancel.” This is a
local analytic corollary and scoped payment obstruction, not a transferred
S03 fixed-pilot constant or a global signed lower bound. Coherent cutoff
matching and positive physical anchor margins remain open.
[Separate same-model review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/04_time_height_scaling/reviews/03_UNIFORM_RESIDUAL_TRANSFER_INTERNAL_REVIEW_20261019.md) and192/256/fresh192 checks;
no new coverage. For Edward Baker with substantial LLM assistance,
**gpt-6.1-sol, actual effort ultra**; no specialist review.


**19 October 2026 S05-T2 complete acquisition comparison, investigation 3/11.**
[Note 03](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/05_covariant_theta_jets/notes/03_COMPLETE_SHIFTED_ACQUISITION_AND_CONSUMER_COMPARISON_20261019.md) is an **interval-checked bounded consumer comparison**
under the inherited reflected-source contract. All51coefficients at192/256
give a hybrid using groupedorder2 and factoredother50. Complete addederror
allowances decrease >0.0092005%,0.0077659%,0.0082207% versus the stronger
old expanded/grouped hybrid. “The reported adaptive paid margin is unchanged.”
Same40closedcells/116adaptive calls; rawfixedmargin shiftsbothways. This
completes the selected error gate, with no cost, coverage, strongestphysical
or new arithmetic estimate. [Separate same-model review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/05_covariant_theta_jets/reviews/03_COMPLETE_SHIFTED_CONSUMER_INTERNAL_REVIEW_20261019.md),
freshfullreplays and exactledger checks support the result. For Edward Baker
with substantial LLM assistance, **gpt-6.1-sol, actual effort ultra**.


**19 October 2026 manuscript synthesis, investigation 3/11.**
The [new Section 12](../papers/investigations-3/11_arithmetic_collision_rigidity/manuscript/positive_arithmetic_packets/sections/12_symmetry_findings.tex)
summarizes the already proved/certified symmetry results and their scoped
comparisons: “The real bridge and required complex exterior remain open.”
The [new research program](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/research-overview/03_UNIFORM_ARITHMETIC_RESIDUAL_RESEARCH_PROGRAM_20261019.md)
targets uniform arithmetic residual control; its new mathematical tasks
are unexecuted. [Integration review](../papers/investigations-3/11_arithmetic_collision_rigidity/reviews/16_SYMMETRY_PROGRAM_AND_MANUSCRIPT_INTEGRATION_REVIEW_20261019.md).
This is a documentation milestone, with no upgraded result status. For
Edward Baker with substantial LLM assistance, **gpt-6-astra, max**.


**19 October 2026, UAR-02 uniform finite component (investigation 3/11).**
[S03 Note 08](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/notes/08_UNIFORM_FINITE_GAMMA_HEAT_REMAINDER_20261019.md)
is **proved in-note, with outward checks of the constants**: after retaining the prescribed gamma/heat correction, relative finite-mode error is <2/c^2 on enlarged disks throughout 0<t<=1/20,1<=kappa<=2, with both Gaussian tails and one spatial derivative paid. The summed rotating finite remainder is <1.9e-16. "It is not an estimate of the complete corrected residual": the retained correction, RS edge, transitions and physical anchor remain open. [Separate same-model review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/reviews/08_UAR02_UNIFORM_FINITE_GAMMA_HEAT_INTERNAL_REVIEW_20261019.md) and [192/256-bit record](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/numerics/UAR02_UNIFORM_FINITE_GAMMA_HEAT_20261019.json). Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol, actual effort ultra**; no specialist human review, physical coverage or Newman-bound gain.


**19 October 2026, UAR-03 coherent edge/transition input (investigation 3/11).**
[S03 Note 09](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/notes/09_UNIFORM_COHERENT_EDGE_AND_CUTOFF_MATCHING_20261019.md)
is **proved in-note, with outward checks of constants**: a common bounded double-contour edge model has complete rotating error <3.9e-34 throughout the UAR sector, for either frozen cutoff. Corrected-transition prefixes have allowance <3.01exp(-13/(16t))<2.639e-7, replacing the divergent raw-mode payment in the corrected combination. "The retained signed increment has not been evaluated or bounded." [Separate same-model review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/reviews/09_UAR03_UNIFORM_COHERENT_EDGE_INTERNAL_REVIEW_20261019.md) and [192/256-bit record](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/numerics/UAR03_UNIFORM_COHERENT_EDGE_20261019.json). Retained integral quadrature/cost and physical anchor remain open; no physical coverage or Newman gain. Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol, actual effort ultra**; no specialist human review.


**19 October 2026, UAR-04 complete uniform increment (investigation 3/11).**
[S03 Note 10](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/notes/10_UNIFORM_SIGNED_RESIDUAL_INCREMENT_20261019.md)
is **proved in-note, with outward checks of constants**: the complete ordinary piecewise corrected residual increment is <3.246 exp(-13/(16t))<2.846e-7 for every prefix of [4pi exp(1/t),4pi exp(2/t)], 0<t<=1/20, including both cutoffs and all endpoint/transition errors. Signed saddle/heat and finite-frequency estimates analytically enclose the retained model; no H calibration or quadrature. This supersedes UAR-03's then-open signed-increment obligation. “Equation (1) supplies neither that anchor nor collision exclusion”. [Separate same-model review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/reviews/10_UAR04_UNIFORM_SIGNED_INCREMENT_INTERNAL_REVIEW_20261019.md) and [192/256-bit record](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/numerics/UAR04_UNIFORM_SIGNED_INCREMENT_20261019.json). UAR-05 Ready; no optimal physical-consumer, cost, coverage or Newman gain. Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol, actual effort ultra**; no specialist human review.


**19 October 2026, UAR-05 paid bounded physical anchor (investigation 3/11).**
[S03 Note 11](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/notes/11_PAID_ANCHOR_AND_BOUNDED_PHYSICAL_SEPARATION_20261019.md)
is **interval-certified for the declared bounded anchor/separation contract**: on T=[1/20-1e-14,1/20], x=4pi exp(20)+1+[-.01,.01], complete J_Q norm >.539 and (H^2+H_x^2)/A^2>.27. Two full 22,026-mode interval images per precision pay actual anchor uncertainty, full signed approximant variation, correctly rebased2B and normalizer derivatives. “The matched direct endpoint error is smaller”. [Same-model review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/reviews/11_UAR05_PAID_ANCHOR_INTERNAL_REVIEW_20261019.md) and [192/256-bit acquisition](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/numerics/UAR05_PAID_ANCHOR_20261019.json). UAR-06 Ready on this exact box only; no uniform J_t separation, global bridge/exterior, cost advantage or Newman bound. Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol, actual effort ultra**; no specialist human review.


**19 October 2026, UAR-06 matched consumer decision (investigation 3/11).**
[Note 12](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/notes/12_MATCHED_COMPLETE_CONSUMER_AND_COST_COMPARISON_20261019.md) is **Complete as a scoped losing comparison** on the exact UAR-05 box: direct energy/A^2>.27778656 exceeds local transported >.27778628, with the same 44,052 acquired modes per precision and fewer error payments. “Stop this bounded transport configuration.” This supersedes UAR-05's then-Ready UAR-06 status; its certificate remains valid. [Delegated internal review](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/reviews/12_UAR06_MATCHED_CONSUMER_INTERNAL_REVIEW_20261019.md) and [source-pinned margins/cost ledger](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/numerics/UAR06_MATCHED_COMPLETE_CONSUMER_20261019.json). No factor-two transport gain or new coverage; UAR-E1/G1 remain conditional. Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol, actual effort ultra**; no specialist review.

**19 October 2026, UAR analytic manuscript milestone (investigation 3/11).**
[S03 Note 13](../papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/notes/13_REBASED_RESIDUAL_AND_COMPACT_SECTOR_EDGE_EXTENSIONS_20261019.md)
is **proved in-note from the stated inherited analytic estimates**: the
complete residual bound begins at any lower endpoint in the original
sector, while coherent edge and corrected-transition estimates extend
qualitatively to every fixed compact positive scaling band at sufficiently
small time. “Neither result proves a physical lower margin or extends
certified collision exclusion.” [Manuscript Section 13](../papers/investigations-3/11_arithmetic_collision_rigidity/manuscript/positive_arithmetic_packets/sections/13_uniform_coherent_edge.tex)
integrates UAR-03/04 and these extensions; [review 18](../papers/investigations-3/11_arithmetic_collision_rigidity/reviews/18_UAR_ANALYTIC_MANUSCRIPT_AND_GENERALIZATION_REVIEW_20261019.md)
records internal self-review and scalar replays. Prepared for Edward Baker
with substantial LLM assistance, **gpt-6-astra, actual effort max**.


**20 October 2026 — RH-conditional absolute-prime envelope (BW-10).**
[Note 11](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/11_FULL_ABSOLUTE_PRIME_ENVELOPE_AND_LOGARITHMIC_SPREAD_20261020.md) is **proved under RH within the stated
complete-budget class**: every admissible nonnegative bandlimited kernel
has leading complete absolute-prime cost at least one-half times
L/log L, with equality at leading order for the centered Fejér sequence.
A joint inequality C+I M>=c I^3 exp(pi/I) pays the kernel's logarithmic
pair moment; the gamma budget bounds M by (1+o(1))L. This removes the
earlier mass-bandwidth and translation restrictions, while retaining the
gamma and negative-pole budgets. “The signed arithmetic term remains
outside this theorem.” Small-C examples remain valid; no original zero
is excluded. [Separate same-model review](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/reviews/11_GENERAL_KERNEL_ENVELOPE_REVIEW_20261020.md).
Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, effort ultra**; no specialist review or novelty claim.


**20 October 2026 — matched evaluation and signed gap kernels (BW-10).**
[Note 12](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md) is **proved from the stated classical inputs under RH**:
corrected Riemann–Siegel values plus discrete Cauchy jets give both matched
multiplicity extractors sufficient summand exponent one-half. The earlier
Euler-sum advantage is method-specific; this is not an executed certificate.
Its exact Riesz contour retains multiple-zero residues. [Note 13](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/13_CERTIFIED_GAP_SIGNED_POLYNOMIAL_KERNELS_20261020.md)
proves a same-bandwidth nonnegative companion with a no-larger complete
zero sum for the stated certified-gap polynomial class, and uniform
absolute-prime-cost dominance for the quartic family. “This is exact
zero-consumer dominance.” Full gamma/pole-envelope dominance and general
signed kernels remain outside the result. No original zero is excluded.
[Separate same-model review](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/reviews/12_FINITE_PRECISION_SIGNED_KERNEL_AND_ENERGY_REVIEW_20261020.md).
For Edward Baker with substantial LLM assistance, **gpt-6-astra, ultra**;
no specialist review or novelty claim.


**20 October 2026 — original theta-mode cancellation and kernel extensions (BW-10).**
[Note 14](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/14_EXACT_THETA_MODE_GRAM_CANCELLATION_20261020.md) is **proved for the unchanged source without RH**:
its raw mode Gram diagonal is c_theta a^(-4)+O(a^(-6)), but the complete
first-jet energy is O(a^5 exp(-pi a/4)); hence the signed cross term
cancels the diagonal to exponential relative accuracy. This is a scoped
failure of fixed/algebraic relative diagonal coercivity, not a lower bound.
[Note 11 §7](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/11_FULL_ABSOLUTE_PRIME_ENVELOPE_AND_LOGARITHMIC_SPREAD_20261020.md)
removes finite Fourier support under its stated strip and complete-budget
hypotheses; [Note 13 §6](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/13_CERTIFIED_GAP_SIGNED_POLYNOMIAL_KERNELS_20261020.md)
removes polynomial factorization for exact central-gap replacement.
Arithmetic and completion budgets are not transferred by replacement.
[Separate same-model review](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/reviews/13_STRIP_KERNEL_GAP_REPLACEMENT_AND_THETA_GRAM_REVIEW_20261020.md).
For Edward Baker with substantial LLM assistance, **gpt-6-astra, ultra**;
no original-zero exclusion, specialist review or novelty claim.

**Remote-gap completion, 20 October 2026:** [Note 13 §§7–8](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/13_CERTIFIED_GAP_SIGNED_POLYNOMIAL_KERNELS_20261020.md) is **proved for each fixed sinc^(2q) power (q>=2) at all sufficiently large heights, uniformly over every bandwidth**: the remote known-gap multiplier has no smaller full envelope, with signed poles retained. A distinct normalized remote addition cannot help under separate prime payment. That comparison does not cover coherent mixtures or arbitrary carriers. [Separate same-model review](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/reviews/14_REMOTE_GAP_COMPLETE_PAYMENT_AND_EVENT_ATTEMPTS_REVIEW_20261020.md). Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra, ultra**; no original-zero exclusion or novelty claim.

The same note's **§9, proved under RH for each fixed admissible base**,
constructs a coherent remote addition with complete-envelope excess
O(delta^(1/2−q)) above the base's exact signed zero sum, including an
explicit q=2 bound. It can strictly reduce the original absolute envelope;
the negative pole and positive prime terms cancel on an exponential
scale. “It cannot improve on the exact signed consumer”. The unrestricted
family's infimum equals the unknown multiplicity, so no simplicity bound
or computational advantage follows. [Separate same-model review](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/reviews/15_COHERENT_REMOTE_GAP_SATURATION_REVIEW_20261020.md).
Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, ultra**; no novelty claim.


**Ratio-energy continuation, 20 October 2026:** [BW10 Note 15](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/15_COMPLETED_RATIO_ENERGY_AND_MULTIPLICITY_20261020.md)
is **proved under RH in-note**, with separate same-model review: the
weighted ratio-error energy divided by epsilon tends to the sum of
c_m/(sigma²+lambda²), c_m=m(1−binom(2m,m)/4^m), over distinct signed zeros.
The proof retains all-zero tightness and transfers from xi to zeta.
“It is not an upper bound by the simple-zero constant.”
[Note 12 §5](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md) also proves the prescribed linear
Möbius taper has limsup error at least 4/(|rho|^4 |zeta''(rho)|²) at an
exact double; multiplicity at least three forces infinite limsup.
This extraction credits Wei–Wu and supplies no RH-only upper bound.
[Review 12 §6](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/reviews/12_FINITE_PRECISION_SIGNED_KERNEL_AND_ENERGY_REVIEW_20261020.md). Prepared for Edward Baker with
substantial LLM assistance, **gpt-6-astra, ultra**; no specialist review,
novelty claim or simplicity conclusion.


**Ratio correlation and damping payment, 20 October 2026:**
[BW10 Note 15 §6](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/15_COMPLETED_RATIO_ENERGY_AND_MULTIPLICITY_20261020.md) is **proved under RH in-note**:
the unchanged Möbius Gram diagonal is asymptotic to
(log(2pi)−EulerGamma)/(2 zeta(2) epsilon), while the full norm tends to
one. “Paying those correlations absolutely is not merely too large:
that double payment diverges.” Its signed first-order remainder is
not estimated sharply by this comparison. [Note 12 §6](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md) proves
the necessary coupled-damping payment
liminf (log N) I_(N,a/log N)>=(sqrt K−sqrt(aC))_+², with an explicit
positive double-pair bound at a=2. Neither result supplies the opposing
arithmetic estimate. [Separate same-model review §7](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/reviews/12_FINITE_PRECISION_SIGNED_KERNEL_AND_ENERGY_REVIEW_20261020.md).
Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, ultra**; no novelty claim or original-zero exclusion.


**Fixed-damping scope correction, 20 October 2026:**
[BW10 Note 12 §7](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md) is **proved in-note**:
the untapered coefficients mu(n)n^(-a/log N), fixed a>0, have complete
error limsup at least exp(-2a) B², B=limsup |M(x)|/sqrt(x). A simple
critical zero forces B>0 and a multiple one forces B=infinity. Under RH
the truncation remainder has the same limsup. “A fixed a/log N
truncation payment cannot serve as the proposed opposing estimate.”
The older §6 liminf bound survives; its vanishing-payment candidate is
superseded. Growing a_N and different coefficients are not covered.
[Note 15 §§7–8](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/15_COMPLETED_RATIO_ENERGY_AND_MULTIPLICITY_20261020.md), **proved under RH in-note**,
computes the prime-error linearization coefficient sum d_m/|rho|²,
with d_1=0, d_2=1/4, and a Jensen variance loss with liminf at least one.
Neither supplies an opposing bound. [Same-model review §8](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/reviews/12_FINITE_PRECISION_SIGNED_KERNEL_AND_ENERGY_REVIEW_20261020.md).
Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, ultra**; no specialist review or novelty claim.


**Growing-damping and taper thresholds, 20 October 2026:**
[BW10 Note 12 §§8–9](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/12_FINITE_EVALUATION_AND_ENDPOINT_INVERSE_COSTS_20261020.md) is **proved in-note** for
its prescribed coefficient classes. At an order-m critical zero,
c loglog N/log N damping with c<=m−1 has an explicit nonvanishing
normalized full-error limsup; a fixed smooth taper of endpoint order k
has positive limsup at multiplicity k+1 and infinite limsup above it.
“It supplies no RH-only upper estimate or simplicity proof.” The general
damping envelope is eventual, not a subsequence claim; infinitely flat
and N-dependent tapers are outside the theorem. [Note 15 §§8.3 and 9.1](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/15_COMPLETED_RATIO_ENERGY_AND_MULTIPLICITY_20261020.md)
records forced independence of exact binary prime indicators and the
endpoint-compatible fixed-time heat averages. [Same-model review §9](../papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/reviews/12_FINITE_PRECISION_SIGNED_KERNEL_AND_ENERGY_REVIEW_20261020.md).
For Edward Baker with substantial LLM assistance, **gpt-6-astra, ultra**;
no specialist review or novelty claim.

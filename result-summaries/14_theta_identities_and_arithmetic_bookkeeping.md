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


**18 October 2026 manuscript integration, investigation 3/11.** The
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

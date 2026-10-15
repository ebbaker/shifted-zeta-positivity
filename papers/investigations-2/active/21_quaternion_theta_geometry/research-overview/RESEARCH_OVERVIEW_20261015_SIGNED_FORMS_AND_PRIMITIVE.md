---
research_program: COORD
secondary_programs: [PR01, PR02, PR03, ALG, PR02-CORR]
status: current_program_overview
supersedes: RESEARCH_OVERVIEW_20261015_CORRELATION_KERNELS.md
---

# Research overview of signed forms and the positive theta primitive

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6-astra**, reasoning effort **ultra**, verified from current-session metadata.

The objective remains to exclude every positive-time real collision of the theta heat flow. The manuscript now incorporates the developments of Notes 38–53: complete Poisson identities and their integrability obstructions, sharper outer remainder budgets, a broader conditional cutoff transfer, signed boundary and differential-form identities, an exact finite E8 projection, a positive theta primitive, and controls showing why these results do not yet imply the needed pointwise sign.

This overview supersedes the [correlation-kernel overview](RESEARCH_OVERVIEW_20261015_CORRELATION_KERNELS.md), retained as a historical record. The principal new analytic opportunity is to estimate the **complete signed combination** reconstructing the physical field from the positive primitive, or its equivalent oriented boundary current. The required estimate is still open; auxiliary positivity and integrated positivity do not supply it.

## Established coverage and the remaining target

Write \(h_j=\partial_x^jH\), \(E=h_0^2+h_1^2\), \(\mathcal L_j=h_{j+1}^2-h_jh_{j+2}\), and \(S_j=\{h_{j+1}=0\}\), for \(j=0,1\). The complete source and full stationary conditions remain fixed throughout.

| Result | Domain or qualification |
| --- | --- |
| Both stationary signs and \(\sqrt E>10^{-17}\) | \(0\le t\le1/2\), \(|x|\le112\) |
| Both full strict signs and the uniform four-jet asymptotic | Sufficiently large \(|x|\), \(0<t\le1/2\), \(t\log(|x|/(4\pi))\ge61/24\); starting height unevaluated |
| Explicit conservative outer theorem | \(|x|\ge4\pi e^{10^9}\), \(t\log(|x|/(4\pi))\ge5\) |
| Six fixed-theta stationary root certificates | \(\theta=1/2,3/4,1\), both branches, inside the existing height-112 cover; no new sign domain |

The sufficient target is \(\mathcal L_j\ge-\kappa_jE\) on both full stationary sets, with source-prescribed coefficients locally bounded through every covered finite positive-time candidate collision. The all-cutoff alternatives permit larger losses before optimization, but their whole family and complete tails must be proved first. Every use requires a domain containing the relevant predecessor curves. The inner cusp and finite bridge remain unresolved.

## Signed forms and the complete boundary current

[Note 49’s summary of Notes 46–47](../notes/00_research_coordination/49_OCTONIONIC_SIGNED_BOUND_ANALYTIC_CONTINUATION_20261015.md) records an exact signed circle current, its negative-mass sufficient bound, and a complete Gaussian payment for the original full-amplitude staircase. With
\[
\varphi_j(\theta)=h_j(t,x)\Re h_j(t,x+Re^{i\theta}),
\]
the full stationary identity is
\[
\mathcal L_j=-\frac{4h_j^2}{R^2}
+\frac4{R^2}\langle(1-\cos2\theta)\varphi_j\rangle.
\]
A source-prescribed lower bound for this complete weighted current at scale \(E\), with locally positive radius, would suffice. Its negative part gives a stronger sufficient target; keeping favorable cancellation may be necessary.

[Note 50](../notes/04_octonionic_reductions/50_QUATERNION_FORMS_HODGE_PAIRING_AND_SOURCE_TARGET_20261015.md) realizes the same signed observation through closed self-dual two-forms. [Note 51](../notes/04_octonionic_reductions/51_POLARIZED_HODGE_DISK_AND_CENTERED_SOURCE_BOUNDS_20261015.md) proves a sharp disk completion and positive centered Gaussian averages of both Hermitian branches. Note 47 separately gives a sharp translated spatial average with a loss proportional to the inverse localization length squared. These are genuine integrated results. Their boundary or averaged energy is not the central physical energy, and fixed-radius positivity can persist while the central stationary ratio has its collision pole.

The author's January and February 2014 quaternion-form documents were unpublished working notes circulated with mistakes and incompleteness acknowledged. Their signed-form ideas motivate the new construction; no unproved general nonabelian boundary formula is used. [Review 30](../reviews/30_QUATERNION_FORMS_DRAFT_COMPARISON_AND_RELEVANCE_20261015.md) records the version comparison and the specific limitations.

## Positive theta primitive and the next source estimate

[Note 52](../notes/05_theta_correlation_kernels/52_POSITIVE_THETA_PRIMITIVE_AND_DIFFERENTIAL_CLOSURE_20261015.md) defines
\[
\psi(u)=e^u\sum_{n\ge1}e^{-\pi n^2e^{4u}},\qquad
J(t,x)=\int_0^\infty e^{tu^2}\psi(u)\cos(xu)\,du.
\]
It proves \(J(t,x)>0\) for all real \(x\) and \(0\le t\le1/2\), and the exact identity
\[
8H=\tfrac12+(2t-x^2-1)J+4txJ_x-4t^2J_{xx}.
\]
The boundary constant is essential. The positive primitive has algebraic spectral decay; the physical field is obtained after cancellation. Separate norms of \(J\) and its derivatives therefore lose the feature that matters near a small physical jet.

The same note rules out a nonzero homogeneous finite rational-coefficient linear differential identity for the complete theta field on an open spectral interval. This does not rule out stationary-only identities, transcendental coefficients, nonlocal representations, or a signed residual estimate.

The next useful step is a source-specific inequality for the complete reconstruction or circle current, with its coefficient rule fixed before validation. A further representation is useful only if it supplies that estimate. The small-energy restriction \(E\le\delta\Gamma^2\), with nonvanishing source-prescribed scale \(\Gamma\), remains available without assuming an energy floor.

## Arithmetic identities and exclusions

[Notes 38 and 42](../notes/05_theta_correlation_kernels/README.md) derive exact parity–Poisson formulas and an integrable smooth localization. They also prove that the separate axis and mixed sectors, individual modes, finite centered rectangular packets, and the stated finite-order compensation class cannot be integrated globally under positive heat. Cancellation must occur before unbounded integration. The complete localized exterior allowance is absolute; it does not establish an energy-relative sign.

[Note 48](../notes/05_theta_correlation_kernels/48_E8_CHARACTER_PROJECTION_AND_SIGNED_HEAT_SECTORS_20261015.md) supplies the finite eight-character E8 bridge that was missing at the preceding overview. Its sectors are translated complete sources and admit legitimate positive-heat integrals. Their reconstruction is exact, but an untwisted differentiated sector has adverse sign, and auxiliary complex-shift norms need not vanish with \(E\). Full reconstruction must precede the signed observation.

[Note 53](../notes/05_theta_correlation_kernels/53_SOURCE_CONCAVITY_AND_POSITIVE_TIME_COLLISION_CONTROL_20261015.md) gives a smooth positive even source with double-exponential decay, strong log-concavity near the event, and strict log-concavity in the squared source coordinate, yet a positive-time collision. Its full stationary ratio is \(-1/(T-t)+O(1)\). Thus those source-shape assumptions, even together, cannot close the theta argument. This is a control family, not a theta counterexample.

## Outer remainder and conditional transfer programs

PR01 retains [Note 39's convex dyadic summation](../notes/01_weighted_outer_remainders/39_CONVEX_DYADIC_WEIGHTED_REMAINDER_AUDIT_20261015.md), which removes one logarithmic factor, and [Note 43's explicit constant package](../notes/01_weighted_outer_remainders/43_EXPLICIT_WEIGHTED_REMAINDER_CONSTANT_PACKAGE_20261015.md). Elementary thresholds and imported approximation errors are evaluated. [Note 58](../notes/01_weighted_outer_remainders/58_EXPLICIT_CARRIER_PHASE_AND_CONDITIONAL_HEIGHT_20261015.md) now evaluates the carrier-to-phase error as 409/L and completes the total conditional budget 1728 B_C(L)+409/L. The actual exponent-pair constant and any imported validity threshold remain unresolved, so this is not an evaluated full-sign starting height. The same five limiting estimates still fail on the identified middle interval at \(\theta=5/2\).

PR02 retains [Note 44's subpower transfer](../notes/02_signed_cusp_control/44_SUBPOWER_CUTOFF_TRANSFER_AND_ANALYTIC_RIGIDITY_20261015.md). An all-cutoff cost \(E N^p\exp\{a(\log N)^2\}\), together with the complete Gaussian remainder and locally bounded prescribed parameters, still contradicts finite analytic collision multiplicities. The theta signed estimate required as its premise has not been proved.

PR03 should evaluate the unresolved arithmetic constants or test a frozen signed mechanism on fresh full stationary observations. [Note 40](../notes/03_effective_bridge/40_FIXED_THETA_STATIONARY_BASELINE_20261015.md) supplies a reusable certified baseline. Repeated finite extensions without an evaluated analytic endpoint do not settle the unbounded cusp.

## Continuation beyond the integrated manuscript

[Note 56](../notes/05_theta_correlation_kernels/56_POSITIVE_PRIMITIVE_COLLISION_CONTROL_20261015.md) strengthens the source control: a collision can coexist with the positive heat-first primitive on the entire physical interval, the exact boundary constant and reconstruction, the even completed primitive, and all algebraic spectral asymptotic coefficients. Concavity and rational finite-jet nonclosure also persist. These properties together therefore do not distinguish theta from a colliding source; the next signed estimate needs additional complete-theta information.

[Note 57](../notes/02_signed_cusp_control/57_CIRCLE_DEFECT_MULTIPLICITY_AND_RADIUS_20261015.md) shows why preserving the signed current matters quantitatively. At multiplicity \(2r+j\), fixed-radius negative mass divided by \(E\) has order \(s^{-r}\), whereas the exact stationary ratio has only the pole \(-r/s\). Its shrinking-radius profile still forces an unbounded loss. These are conditional controls, not assertions of a theta collision.

The [current continuation, Note 59](../notes/00_research_coordination/59_PRIMITIVE_CONTROLS_AND_COMPLETED_PHASE_BUDGET_CONTINUATION_20261015.md) and [Review 33](../reviews/33_PRIMITIVE_CIRCLE_AND_CARRIER_CONTINUATION_REVIEW_20261015.md) record Notes 56–58 and their exact checks. The 96-page manuscript still contains Notes 38–53; the new continuation is not yet integrated. Updated 15 October 2026 for Edward Baker with substantial LLM assistance, **gpt-6-astra**, effort **ultra**.

## Manifold geometry and a source-specific continuation

[Notes 60–63](../notes/00_research_coordination/63_MANIFOLD_GEOMETRY_AND_THETA_BUNDLE_CONTINUATION_20261015.md) develop the geometric question beyond a formal SD/ASD analogy. The physical pair gives an immersed Kähler surface with metric coefficient E and actual coassociative/Cayley inclusions. Its curvature squares the Laguerre quantity; its marked real Gauss map retains the sign. Every finite collision forces positive quarter-turn concentration on a shrinking interval. A prescribed uniform one-sided modulus would exclude collisions, but that theta estimate remains unproved.

The actual theta source is also an explicit jet of the theta line bundle along an elliptic family. A local semi-flat metric on that family is hyperkähler and nonflat, with horizontal sectional curvature 1/(2q³). This gives a concrete source-specific setting. Global transition/connection data and an inequality surviving the complete positive-heat Mellin transform are still required. Generic hyperkähler or calibration statements accept the known collision controls. [Review 34](../reviews/34_MANIFOLD_GEOMETRY_AND_THETA_BUNDLE_REVIEW_20261015.md) records analytic checks and 55 exact assertions. Notes 56–62 remain outside the stable manuscript; sign coverage is unchanged.

Updated 15 October 2026 for Edward Baker with substantial LLM assistance, **gpt-6-astra**, effort **ultra**.

## Priorities and records

1. Pursue one complete signed theta estimate preserving the primitive cancellation or boundary current, both full stationary sets, all heat factors, and predecessor coverage.
2. Use the smooth collision control to reject arguments depending only on generic positivity, concavity, decay, or monogenicity.
3. Run a discriminating certified pilot only after the mechanism, coefficient rule, and full error budget are fixed. A finite success still requires an unbounded-domain proof.
4. In parallel, evaluate the actual PR01 arithmetic constants or prove a new weighted saving across the identified middle interval.

The [manuscript](../manuscript/quaternion_theta_geometry.tex), [build record](../manuscript/BUILD_RECORD.json), and [integration review](../reviews/32_SIGNED_FORMS_PRIMITIVE_MANUSCRIPT_INTEGRATION_20261015.md) identify the integrated version. [Note 55](../notes/00_research_coordination/55_SIGNED_FORMS_MANUSCRIPT_INTEGRATION_AND_HISTORY_20261015.md) records the handoff and archive verification. Earlier proofs, numerical receipts, and Reviews 27–31 retain their own provenance. No new sign region, manuscript snapshot folder, commit, or tag is introduced by this integration.

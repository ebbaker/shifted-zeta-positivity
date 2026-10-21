# Global physical jet geometry research program

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**, verified from this turn's metadata.

[Progress register][progress].

## First bounded comparison — 21 October 2026

[Note 01][n01] now supplies a finite complex-disk mass enclosure for all
\(m-1\) stationary neighborhoods of the original first jet, and an
explicit \(O(\sqrt t)\) capture bound for the complete defect with the
regular outer curvature retained. Its source constants depend on the
hypothetical event and have not been numerically acquired for theta.
The [same-assistant review][r01] preserves that conditional scope.

For this selected mass monitor, the assumptions already provide direct
scalar nonvanishing on larger positive-time sets. Its leading-profile
exclusion comparison is therefore stopped; the diagnostic is retained.
A different compensated boundary observable and an opposing theta
estimate remain open. GPJ-04 is still gated. The overall program and
acceptance criteria below are unchanged.

## Objective and scope

Direction A in [the proposal note][proposals], Section 2, studies
\[
P(t,z)=\int_0^z H(t,\zeta)\,d\zeta,\qquad
X_t(z,w)=(P(t,z),H(t,z),w),
\]
for the unchanged theta flow \(H_t=-H_{zz}\). With
\(E_t=|H|^2+|H_z|^2\), the induced metric on the regular locus is
\(g_t=E_t|dz|^2+|dw|^2\). Global injectivity, completeness and an
intrinsic Ricci-flow identity are not established.

The intended application assumes RH and considers an original zero
at \(t=0\) of finite multiplicity \(m\ge2\). The local concentration law
also applies to analytic heat germs without RH. Invoking all-real
positive-time root motion requires the additional RH premise. The
[BW10 manuscript][manuscript] retains the excess \(K-Z\); its
approximation estimates supply no opposing curvature bound.

## Inherited concentration law

On the regular curve factor, [Note 24][n24], GA1–GA7, gives
\[
d\mu_t=\frac{|HH_{zz}-H_z^2|^2}{E_t^2}\,dA,\qquad
K_t\,dA_{g_t}=-2\,d\mu_t,\qquad
\mu_t\rightharpoonup\mu_{\rm reg}+\pi(m-1)\delta_a.
\]
Here \(K_t\) is Gaussian curvature and \(dA_{g_t}\) is the curve's
induced area; the four-dimensional product multiplies by auxiliary
area. The manuscript's multiplicity mass \(K\) is a different quantity.
The defect vanishes at a simple zero; smooth Gauss area need not.
The complete fixed-circle flux retains the atom in its finite
limit. Canceling the time-zero common factor before taking that limit
loses the quantity this program must retain.

The induced metric is generally not hyperkähler: [Investigation 22,
Section 5][gman] restricts Ricci-flatness to the locally exponential
case. Adding a graph coordinate or an auxiliary area does not exclude
the physical zero. These are scoped conclusions about those constructions.

## Bounded work and acceptance criteria

1. **GPJ-01 — Fix the comparison.** Specify a finite disk or tube,
   time interval, observable and direct complete-jet reference using
   the same source information. State dependence on event height,
   multiplicity and local leading coefficient.
2. **GPJ-02 — Derive a source estimate.** Test a uniform-integrability
   modulus or compensated boundary budget. Retain regular curvature,
   the predicted atom, all boundaries, source tails and auxiliary-volume
   normalization. Any bound below the event defect needs an independent
   theta derivation.
3. **GPJ-03 — Compare the payments.** Require an explicit improvement
   in error, margin, covered domain or acquisition cost, or record a
   failure for the specified observable and information class. Set
   the benefit criterion before numerical acquisition.
4. **GPJ-04 — Assess extension.** After a useful finite estimate,
   address arbitrary heights and all finite multiplicities. Identify
   uniform constants and remaining event dependence.

Under [the classification rule][a01], a universal no-defect condition
is an exclusion criterion. A paid finite-domain bound is a quantitative
milestone. Re-deriving the curvature formula or its product lift does
not complete GPJ-02 or GPJ-03.

## Control screen and stopping rule

The inherited screen in proposal Sections 2 and 7 gives:

| Control | Required response | Missing theta premise |
| --- | --- | --- |
| \(H=z^2-2t\) | Retain its atom pi despite finite fixed-circle flux and finite total area. | Complete theta source, growth and arithmetic. |
| [RH-conditional close-source endpoints][n05] | Allow doubles despite source closeness and simple all-real positive-time zeros. | Ordinary Dirichlet-series arithmetic. |
| Atomic and finite-profile families | Do not infer exclusion from selected moments or finite observations. | Complete theta coefficients, profile growth and eventual simplicity at threshold. |

Apply the Euler-factor, weighted-square, finite-prime, reflected and
positive-primitive screens through [the control register][controls] and
proposal Section 7. Name each control's failed premise separately;
finite-source controls have no all-real heat slice. Stop a comparison
that only reproduces the generic atom or repackages the direct jet
bound. Different coupled theta information remains outside that stop.

## Reading and interfaces

Read the [result index][results], [local geometry][local],
[geometric realizations][geometry] and [avoid index][avoid], especially
[shared premises][a02], [coordinate lifts][a03] and [scope][a07].
[Note 24][n24] and [its internal review][r23] retain their inherited
status; this opening is not a new analytic review.

[BW-12][B] studies a different spacetime charge and [BW-13][C] studies
spectral periods. Share domains and complete-source budgets where useful,
without identifying their different multiplicity weights.
[HMC-05 remains open and HMC-06 gated][hmc].

[B]: ../../12_relative_chern_hopf_charges/README.md
[C]: ../../13_spectral_covers_and_periods/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a03]: ../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[avoid]: ../../../../../../../avoid/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[geometry]: ../../../../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[gman]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/manuscript/theta_manifold_geometry.tex
[hmc]: ../../10_rh_implies_simple_zeros/research-progress/02_HEAT_ROOT_MOTION_AND_SIGNED_CONTOURS_PROGRESS_20261021.md
[local]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[manuscript]: ../../10_rh_implies_simple_zeros/manuscript/main.tex
[n05]: ../../10_rh_implies_simple_zeros/notes/05_CLOSE_POSITIVE_SOURCES_AND_NORMALIZED_DOUBLE_ZEROS_20261020.md
[n24]: ../../10_rh_implies_simple_zeros/notes/24_GAUSS_AREA_CONCENTRATION_AND_CURVATURE_FLUX_20261021.md
[progress]: ../research-progress/01_GLOBAL_PHYSICAL_JET_GEOMETRY_PROGRESS_20261021.md
[proposals]: ../../10_rh_implies_simple_zeros/brainstorm/04_GLOBAL_HEAT_GEOMETRY_PROPOSALS_AND_INITIAL_SCREENS_20261021.md
[r23]: ../../10_rh_implies_simple_zeros/reviews/23_GAUSS_AREA_AND_CURVATURE_FLUX_REVIEW_20261021.md
[results]: ../../../../../../../result-summaries/README.md

[n01]: ../notes/01_RESOLVED_CURVATURE_DISKS_AND_DIRECT_COMPARISON_20261021.md
[r01]: ../reviews/01_RESOLVED_CURVATURE_DISKS_SELF_REVIEW_20261021.md

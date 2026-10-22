# Jensen surface degeneration and resolution research program

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**, verified from this turn's metadata.

[Progress register][progress].

**First research update, 21 October 2026:** [Note 01][note01] completes a
fixed-disk comparison at c=-199.79, r=.001. A complete local E5 estimate
reduces the sufficient odd degree by a factor exceeding 4414 at error
1e-9. Sixty-five coefficients and a full-tail bound suffice for the local
certificate; the degree does not equal the acquisition count. Complete
coefficient acquisition still loses the selected speed comparison to
direct jets. The broader direction remains in reserve; this does not
exclude shared-prefix amortization or a separately specified period task.
See the same-assistant [self-review][review01].

## Objective and normalization

Direction E in [the proposal note][proposals], Section 6, uses
\[
f(s)=\xi(1/2+\sqrt s)=\sum_{k\ge0}c_ks^k,\qquad
c_k=\gamma_k/k!>0,
\]
\[
J_d(X)=\sum_{k=0}^d\binom dk\gamma_kX^k,\qquad F_d(s)=J_d(s/d).
\]
The square-root notation denotes the single-valued even power series.
The physical normalization is \(H(0,z)=f(-z^2/4)/8\); multiplicity is
preserved at nonzero zeros. For \(d=2g+1\), the compact curve is the
smooth projective normalization of \(Y^2=J_d(X)\).

Under RH, the finite Jensen polynomials have distinct negative real
roots even if \(f\) has a multiple zero. Their expected genus and
maximal real-component topology do not prove simplicity. This is the
scope of [Investigation 22 Note 05][jensen]. The [BW10 manuscript][manuscript]
likewise retains the multiplicity excess.

The task is effective resolution in the unshifted degree limit, distinct
from fixed-degree, large coefficient-shift asymptotics and from physical
heat-time evolution.

## Inherited approximation and multiplicity scales

Proposal E3–E6 gives, on \(|s|\le R\),
\[
|F_d(s)-f(s)|\le\frac{R^2f''(R)}{2d},\qquad
F_d(s)=f(s)-\frac{s^2}{2d}f''(s)+\mathcal R_d(s),
\]
\[
|\mathcal R_d(s)|\le\frac{C_R}{d^2},\qquad
C_R=\frac{R^4f^{(4)}(R)+4R^3f^{(3)}(R)+2R^2f''(R)}8.
\]
The positive coefficient inequalities include the full omitted tail.
These full moments can be expensive at large radius; no favorable
height-dependent cost follows automatically.

For a nonzero double or triple zero \(a\), the scaled profiles under
\(s=a+au/\sqrt d\) are \(u^2-1\) and \(u^3-3u\), with the errors in
E7. A double cluster has gap \(2|a|/\sqrt d+O(d^{-1})\).
A simple zero instead has displacement
\[
\frac{a^2f''(a)}{2d f'(a)}+O(d^{-2}).
\]
The constants are local and event-dependent. Higher multiplicities
need more expansion terms; E5 alone does not prove an all-multiplicity
remainder.

## Bounded work and acceptance criteria

1. **JSD-01 — Choose the diagnostic and benefit target.** State a
   height window, its \(s\)-domain, desired resolution and direct
   \(H,H_z\) comparator. Choose whether the output is root clustering,
   a period diagnostic or an error bound. Set the benefit criterion
   before acquiring coefficients.
2. **JSD-02 — Pay moment and degree costs.** Enclose full theta moments
   and coefficient errors, including truncation and precision. Turn
   E4–E6 into an effective degree requirement. Do not use an unknown
   derivative floor as an available constant.
3. **JSD-03 — Resolve clusters rigorously.** Supply local nonvanishing
   and contour bounds to convert the double/triple profiles into
   finite certified enclosures. Retain neighboring zeros and root
   errors. A small gap at one degree does not determine limiting
   multiplicity.
4. **JSD-04 — Compare complete costs.** Measure resolution, precision,
   degree and total acquisition cost against direct jets on the same
   window. Keep a useful diagnostic or record a scoped failed comparison.
5. **JSD-05 — Consider broader scope.** After useful finite evidence,
   extend multiplicity or height. Exclusion still needs an independent
   arithmetic gap or period bound beyond generic approximation laws.

The original activation gate has now been tested on one disk and failed
its speed target; retain the quantified resolution result, with broader
activation gated on a distinct useful objective.
Under [the classification rule][a01], another confirmation of known
RH-equivalent topology is not a simplicity milestone.

## Controls and interpretation

Proposal E2 gives
\[
f_*(s)=(1+s)\frac{\sinh(\pi\sqrt s)}{\pi\sqrt s}
=(1+s)\prod_{n\ge1}(1+s/n^2),
\]
an entire order-one-half function with positive coefficients, infinitely
many negative zeros and a double at \(-1\). It passes the strict finite
Jensen premise but fails the unchanged theta moments. No positive
theta-source realization is asserted.

For the finite control \(f(s)=(1+s)^2\), E10 gives exact gap
\(2\sqrt d/(d-1)\), \(d>1\). This tests degree-scale normalization,
not theta arithmetic. The source reports exact rational transcription
checks of E3 through degree 40 and E10 for degrees 2–40; the written
inequalities carry the argument.

The [collision register][controls] and proposal Section 7 govern any
later heat-source claim. Do not transfer Jensen controls' properties
to those different families. An exclusion must identify the arithmetic
premise missing from its relevant control.

## Reading and interfaces

Read the [result index][results], [local topology summary][local],
[avoid index][avoid] and the rules on [shared premises][a02],
[normalization][a08], [scope][a07] and [premature numerics][a10].
The resolution calculations retain the proposal's same-assistant
assessment; this opening adds no independent validation.

[BW-13][C] is the noncompact direct spectral cover with a different
genus budget. [BW-14][D] retains source geometry; neither automatically
supplies a Jensen separation bound. [HMC-05 remains open and HMC-06 gated][hmc].

[C]: ../../13_spectral_covers_and_periods/README.md
[D]: ../../14_theta_source_transform_constraints/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a08]: ../../../../../../../avoid/08_normalization_and_constant_slips.md
[a10]: ../../../../../../../avoid/10_numerics_ahead_of_the_question.md
[avoid]: ../../../../../../../avoid/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[hmc]: ../../10_rh_implies_simple_zeros/research-progress/02_HEAT_ROOT_MOTION_AND_SIGNED_CONTOURS_PROGRESS_20261021.md
[jensen]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/05_JENSEN_HYPERELLIPTIC_TOPOLOGY_20261015.md
[local]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[manuscript]: ../../10_rh_implies_simple_zeros/manuscript/main.tex
[progress]: ../research-progress/01_JENSEN_SURFACE_DEGENERATION_PROGRESS_20261021.md
[proposals]: ../../10_rh_implies_simple_zeros/brainstorm/04_GLOBAL_HEAT_GEOMETRY_PROPOSALS_AND_INITIAL_SCREENS_20261021.md
[results]: ../../../../../../../result-summaries/README.md

[note01]: ../notes/01_LOCAL_RESOLUTION_AND_COMPLETE_COST_COMPARISON_20261021.md
[review01]: ../reviews/01_LOCAL_RESOLUTION_SELF_REVIEW_20261021.md

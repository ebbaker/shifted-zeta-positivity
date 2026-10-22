# Spectral covers and periods research program

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**, verified from this turn's metadata.

[Progress register][progress].

## Objective and geometric object

Direction C in [the proposal note][proposals], Section 4, defines
\[
\mathcal S=\{(t,z,w)\in\mathbb C^3:w^2=H(t,z)\},\qquad
\mathcal S_t=\{(z,w):w^2=H(t,z)\}.
\]
The complete theta heat function is jointly entire; regular fibers are
noncompact Riemann surfaces. Their coordinate \(w\) is not the
elliptic-fiber coordinate used in [BW-14][D].

The conditional application is BW10's time-zero simplicity problem.
RH supplies simple all-real zeros for real \(t>0\), while the local
construction needs only analytic heat data. The [BW10 manuscript][manuscript]
does not supply a period inequality excluding an original multiple zero.

## Inherited local and global screens

Near an order-m spatial zero, a holomorphic change of fiber coordinate
gives \(w^2=(z-a)^m\). A simple zero is a smooth branch point. For
\(m\ge2\) the fiber is singular with Milnor number \(m-1\), distinct
from the primitive-curve Milnor number \(m(m-1)\). At a double event
the total surface is smooth but its time projection has a critical
point. At order at least three the total surface itself is singular.
A smooth-fibration argument therefore needs additional treatment of
higher multiplicities.

For \(H=z^2-2t\), \(t>0\), the cycle around the cut between its roots,
oriented as in proposal C4, satisfies
\[
\oint_{\delta_t}\frac{dz}{w}=-2\pi i,\qquad
\oint_{\delta_t}w\,dz=2\pi i\,t.
\]
The first period persists because the limiting differential has a pole
at the node; the second vanishes. These exact values are the baseline
to retain. Collapse of the cycle alone is not an exclusion argument.

Proposal C5 gives genus \(N-1\) and two boundary components for the
connected double cover of a disk containing \(2N\) simple zeros.
Under RH at positive real time, exhaustion therefore gives unbounded
genus. A finite global topology budget or finite-dimensional period
system is not an available premise.

## Bounded work and acceptance criteria

1. **SCP-01 — Fix a period problem.** Choose a finite spectral domain,
   regular outer boundary, time range, cycles, differential and branch
   convention. State how critical time and singular differentials
   are treated.
2. **SCP-02 — Derive the paid variation.** Retain cycle transport,
   moving branch points, outer boundary terms and complete theta
   source tails. For a double-event pilot, subtract the exact
   quadratic period before isolating the first source-dependent term.
3. **SCP-03 — Test the information gain.** Bound that term with
   stated constants and compare with direct complete-jet evaluation
   using the same source information. Require an explicit diagnostic,
   error, margin, coverage or cost improvement, or a scoped failed
   estimate. Set the comparison criterion before acquisition.
4. **SCP-04 — Address broader scope.** After useful finite evidence,
   consider higher multiplicity, total-space singularities and
   exhaustion in height. Prove any needed resolution or finite period
   system rather than importing it from the local nodal model.

Nonsingularity at every original zero reformulates simplicity. Under
[the classification rule][a01], the first milestone is an effective
finite period estimate. Generic singularity classification, monodromy
or recovery of C4 alone supplies no new exclusion.

## First research result — 21 October 2026

[Note 01][n01] completes the finite local double-event contract and gives
\[
 \frac{P(\tau)}{2\pi i\sqrt{h_2/2}}
 =\tau+\frac{5h_3^2-3h_2h_4}{48h_2^2}\tau^2+R_3(\tau),
 \qquad |R_3|\le C_3|\tau|^3,
\]
with explicit boundary floors, full moments through order six, and
finite source-tail payments. Its first correction equals
\(3S_2/8+h_3^2/(16h_2^2)\), so the same-four-jet coefficient
comparison adds no information to direct evaluation. An even polynomial
with double endpoints and simple all-real positive-time zeros has a
positive correction, ruling out that sign alone as a discriminator.

The local analytic result has [same-assistant self-review][review01].
The exact polynomial checks and floating contour diagnostics are not a
theta certificate. SCP-03's finite-time source/acquisition comparison
remains open; SCP-04 remains gated. Continuation should name additional
information or a quantitative acquisition advantage before collecting
theta data. This scoped stop does not close spectral-cover approaches.

## Controls and stopping rule

The quadratic model must retain both C4 periods. The cubic screen B4
checks that complex-time events are not identified with physical
collisions. Both lack unchanged theta source and arithmetic.
[RH-conditional close-source controls][n05] have multiple endpoints and
positive-time all-real simplicity but fail ordinary Dirichlet-series
arithmetic.

Apply the Euler-factor, weighted-square, finite-prime, reflected and
positive-primitive screens through [the control register][controls]
and proposal Section 7. Match the hypotheses of the chosen period
estimate, including growth and any all-real assumption. Finite-source
controls have no all-real heat slice.

Stop an exclusion attempt whose only output is generic collapse or a
period of a differential singular at the endpoint. Retain the diagnostic
and state the tested class. Different theta-dependent period bounds
remain outside that stop.

## Reading and interfaces

Use the [result index][results], [local geometry summary][local] and
[avoid index][avoid], especially [lifts][a03], [shared premises][a02],
[normalization][a08] and [scope][a07]. The spectral-cover calculations
C2–C5 have the proposal's same-assistant assessment, not independent review.

[BW-11][A] and [BW-12][B] share the physical heat family with distinct
invariants. [BW-15][E] instead studies finite Jensen approximants.
The [HMC register][hmc] retains HMC-05 open and HMC-06 gated.

[n01]: ../notes/01_NODAL_PERIOD_VARIATION_AND_FOUR_JET_COMPARISON_20261021.md
[review01]: ../reviews/01_NODAL_PERIOD_SELF_REVIEW_20261021.md
[A]: ../../11_global_physical_jet_geometry/README.md
[B]: ../../12_relative_chern_hopf_charges/README.md
[D]: ../../14_theta_source_transform_constraints/README.md
[E]: ../../15_jensen_surface_degeneration/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a03]: ../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a08]: ../../../../../../../avoid/08_normalization_and_constant_slips.md
[avoid]: ../../../../../../../avoid/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[hmc]: ../../10_rh_implies_simple_zeros/research-progress/02_HEAT_ROOT_MOTION_AND_SIGNED_CONTOURS_PROGRESS_20261021.md
[local]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[manuscript]: ../../10_rh_implies_simple_zeros/manuscript/main.tex
[n05]: ../../10_rh_implies_simple_zeros/notes/05_CLOSE_POSITIVE_SOURCES_AND_NORMALIZED_DOUBLE_ZEROS_20261020.md
[progress]: ../research-progress/01_SPECTRAL_COVERS_AND_PERIODS_PROGRESS_20261021.md
[proposals]: ../../10_rh_implies_simple_zeros/brainstorm/04_GLOBAL_HEAT_GEOMETRY_PROPOSALS_AND_INITIAL_SCREENS_20261021.md
[results]: ../../../../../../../result-summaries/README.md

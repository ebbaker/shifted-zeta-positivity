# One additional direction and three sharper questions after the results audit

16 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Model: **gpt-6-astra (Codex)**, reasoning effort **ultra**,
verified from the current session metadata.

**Status:** supplementary brainstorm after the
[result-summary coverage review](../reviews/01_RESULT_SUMMARY_COVERAGE_INVESTIGATIONS_21_22_CODEX_20261016.md).
These are proposed research questions, not new theorems or a selected
program. The [initial six-direction note](01_PATHS_FORWARD_AFTER_INVESTIGATIONS_2_CODEX_20261016.md)
remains the starting record. No new numerical experiment or literature
novelty assessment was performed for this addendum.

The fuller inventory changes how concretely we can formulate the next
steps. Investigations 21–22 already give sharp signed averages, a positive
primitive with exact reconstruction, quantitative coefficient stability,
and genuine geometric objects carrying the relevant arithmetic or physical
energy. Those are useful starting results. The
[result summaries](../../../../result-summaries/README.md) now make them
visible, while the [patterns to avoid](../../../../avoid/README.md) preserve
the distinctions between a construction, an estimate, and an RH-equivalent
criterion.

My recommendation is to add **cancellation and localization of proved
positivity** to the initial shortlist, and sharpen three existing directions
as follows.

## 1. An additional analytic direction: what can the proved positivity control locally?

There is more to start from than a proposed positive representation.
Investigation 21 proves strict centered Gaussian averages of both signed
branches, a sharp translated spatial lower bound, and a disk identity whose
positive Dirichlet term comes with an explicit boundary payment. These
results locate the difficulty: translation and localization introduce costs
that are absent from the centered average.

I would explore an extremal question: **for a prescribed family of weights,
which arithmetic constraints improve the relation between a positive
average and a potentially negative local region?** A first investigation
could keep one translated Gaussian family fixed, start from the existing
complete correlation formula and translation factors, and ask which
arithmetic relation controls their combined signed loss. A companion disk
question could examine what source information improves the boundary cost. A useful result could describe an
admissible weight class, a restricted parameter range, or a sharper loss
bound. It need not begin with an all-collision theorem.

The primitive transform \(J\), proved strictly positive for real \(x\)
and \(0\le t\le1/2\), offers a second view of the same cancellation.
Its exact reconstruction is

\[
8H=\tfrac12+(2t-x^2-1)J+4txJ_x-4t^2J_{xx}.
\]

At time zero this becomes

\[
J(0,x)=\frac{1}{2(1+x^2)}-\frac{8H(0,x)}{1+x^2}.
\]

At large spectral height, the physical field is therefore encoded in a
small difference from an explicit positive background. A worthwhile question is whether a
source-derived representation can estimate this difference, or the full
signed reconstructed products, while preserving the cancellations. Separate
bounds on \(J,J_x,J_{xx}\) already lose the relevant scale; see the
[recorded cancellation pitfall](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).

The primitive-compatible control matches every algebraic primitive
asymptotic coefficient and still collides. Thus adding more terms to that
expansion alone cannot identify the desired remainder. Likewise, centered
averages do not automatically localize: the controls share the underlying
positive-source assumptions. Any proposed global exclusion would need an
additional arithmetic or quantitative input. This branch is newly added to
the shortlist; its starting theorems were already proved in Investigation 21.

Sources: [sharp spatial average](../../../investigations-2/active/21_quaternion_theta_geometry/notes/04_octonionic_reductions/47_ORIENTED_CURRENT_AND_ACCRETIVE_SOURCE_CERTIFICATES_20261015.md),
[disk and centered positivity](../../../investigations-2/active/21_quaternion_theta_geometry/notes/04_octonionic_reductions/51_POLARIZED_HODGE_DISK_AND_CENTERED_SOURCE_BOUNDS_20261015.md),
[positive primitive](../../../investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/52_POSITIVE_THETA_PRIMITIVE_AND_DIFFERENTIAL_CLOSURE_20261015.md),
[primitive-compatible control](../../../investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/56_POSITIVE_PRIMITIVE_COLLISION_CONTROL_20261015.md).

## 2. Sharpen source-space rigidity: approximate measurements and the slope obstruction

The original first direction already asks for quantitative rigidity. We now
have a more specific starting point: normalized nonnegative coefficient
sequences satisfying the first \(N\) exact recurrences have a sharp
algebraic error rate, while fixing the first coefficient \(a_1=1\) improves
the remainder to a Gaussian tail. The affine slope is a concrete source of
instability.

The same note already gives an exact defect-to-observation identity and a
quantitative bound for approximate recurrences

\[
d_k=a_{k-1}-2a_k+a_{k+1}.
\]

Together with the normalization error, their weighted sum controls absolute
physical-jet errors uniformly in real spectral position and heat times
bounded above. Thus robustness to known recurrence defects is already part
of the established result.

The next inverse question is **which finite reflection or elliptic
measurements control those weighted defects and the slope, with what
conditioning?** One could linearize the actual source constraints around
theta in a declared coefficient family, identify perturbations poorly
resolved by those measurements, and compare their effect on the complete
primitive remainder after the common endpoint contributions cancel.
A useful first result would give an explicit stability modulus on a
prescribed finite spectral domain, or exhibit an instability within that
class.

This separates coefficient recovery from control at the scale of the
oscillatory field. Even excellent absolute source accuracy need not protect
a near-zero physical jet. The existing ramp-and-spike examples should
recover the known algebraic loss when the anchor is absent; weighted-square
controls can test whether proposed endpoint data constrain it at all.
All-order primitive asymptotics alone are inadequate in the broader source
class of Section 1's control; the proposed coefficient class and the extra
information measured must therefore be stated explicitly.

Source: [recurrence experiment and sharp stability](../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/08_ADJOINT_RECURRENCE_ENDPOINT_EXPERIMENT_20261015.md);
[control families](../../../../result-summaries/12_collision_controls_and_screening.md).

## 3. Sharpen constructive approximation: can the next actual theta coefficient be admitted?

The Jensen hierarchy gives a concrete compatibility question for the
original stable-construction direction. At zero auxiliary heat time, its
reciprocal polynomials satisfy

\[
R_d'(x)=dR_{d-1}(x),\qquad
R_d(x)=d\int_0^xR_{d-1}(u)\,du+\gamma_d.
\]

The new theta moment chooses the integration constant \(\gamma_d\).
If the preceding polynomial has simple real roots, those roots locate the
critical points of its primitives. The first calculation would determine
the possibly empty interval of constants permitted by the alternating
extremum signs, then compare the actual theta moment with those bounds.
Its endpoints can produce repeated roots.

The question is whether an arithmetic identity or moment inequality
explains that compatibility and its margin as degree increases. This also
provides a test for a proposed stable model: can it extend while retaining
the actual coefficients and derivative relation? Independently refitting a
model at each degree does not establish such compatibility. A source-based
construction intended for physical heat evolution must additionally preserve
that evolution and the needed complex-compact convergence.

The surface deficit records what is lost when compatibility fails. It does
not supply the missing inequality. Success at all degrees would have RH
strength, under the [criterion-classification rule](../../../../avoid/01_restating_the_target.md),
and auxiliary polynomial heat cannot fill the gap: every finite
polynomial eventually regularizes, while a uniform finite threshold across
all degrees is already RH-equivalent. An initial finite calculation should
look for an explanatory inequality and compare a colliding control, rather
than merely extend a table of favorable degrees.

Source: [real-projective jets and the Jensen heat hierarchy](../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/07_REAL_PROJECTIVE_JETS_AND_JENSEN_HEAT_SURFACES_20261015.md);
[stable-preparation program](../../../investigations-2/active/13_stability_jensen_lee_yang/notes/INITIAL_RESEARCH_PROGRAM_20261013.md).

## 4. Sharpen the geometric direction: retain transverse arithmetic before restriction

The marked elliptic family has actual curvature and nonzero transverse
commutators even though the physical-path connection is flat. The useful
question is whether those transverse relations constrain the complete
physical observation beyond the source identities already available.

One exploratory calculation could retain a shared real elliptic-base
variable in a product of theta jets before restricting to the physical
path. Fourier coefficients of a suitable conjugate product organize pairs
of square indices through their differences. Does the full elliptic
multiplier, together with the transverse identities, yield an estimate on
that collective expression, or only reproduce the existing coupled theta
addition formula? The calculation must retain both source variables,
physical heat weights, lower endpoints and commutators. The real base
variable cannot simply be identified with the external spectral variable.

Weighted-square controls already have square-index periodicity and the
Jacobi heat identity, so those inputs alone cannot exclude their collisions.
The full multiplier or another arithmetic condition must enter an actual
estimate. Conversely, specifying enough conditions to identify theta does
not establish the estimate. This is a sharper version of the original
modular-deformation direction, with a definite first comparison to make.

Sources: [ASD metric freedom and transverse commutators](../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/02_ASD_METRIC_FREEDOM_AND_PHYSICAL_RESTRICTION_20261015.md),
[complete correlation bridge](../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/03_COMPLETE_SIGNED_CORRELATION_BRIDGE_20261015.md),
[coupled theta product and its Gram obstruction](../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/06_COUPLED_THETA_PRODUCT_AND_PARITY_SECTORS_20261015.md).

## What this changes for the next discussion

I would keep **source-space rigidity**, **constructive stable approximation**
and **collective prime interactions** as the original three structural
choices, and add **cancellation/localization** as the closest analytic
continuation of the proved positive results. The geometric direction now
has a more concrete transverse-arithmetic question. No path is selected.

The octonionic constructions and finite E8 bridge are useful tools within
these questions. The reflected lift saves a derivative in field evaluation,
the oriented associator preserves the signed coefficient, and the E8
selector supplies a finite heat-integrable source representation. The
[existing results](../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md)
and [arithmetic bridge](../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md)
justify using them where they simplify a calculation. A proposed estimate
must still retain the complete packet: separately positive sectors,
auxiliary norms, or exceptional symmetry alone do not provide it.

For Claude's additional brainstorm, I would especially welcome an opinion
on which of these four starting structures supports a new intermediate
estimate, what extra arithmetic information that estimate would use, and
which existing control separates it from the generic case. Those questions
leave room for a different proposal while giving the discussion concrete
mathematical starting points.

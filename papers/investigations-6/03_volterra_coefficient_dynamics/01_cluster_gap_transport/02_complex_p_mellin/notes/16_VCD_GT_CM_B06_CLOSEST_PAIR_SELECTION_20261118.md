# B06 r1 — Closest-pair selection: useful geometry and retained obligations

18 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Actual model/effort unavailable in chat0002's
guarded registry; one read-only helper checked the elementary geometry and
examples with inherited settings. This is shared analytical assistance,
not a separate specialist assessment.

**Status: elementary selection/geometry analysis, with explicitly scoped
finite examples; no new canonical signed estimate.** The author suggests
choosing the pair with the smallest neighboring-zero distance. This is
useful as a qualified extremal selection, but not a blanket without-loss
assumption for the existing moving count-two problem. [Request][request] ·
[Register][register] · [Results][results] · [Avoid][avoid] ·
[Classification01][classification] · [Scope07][scope] · [Premises14][premises]

**Useful distinction:** the present CM collar already makes the two target
occurrences strict mutual nearest neighbors. If |s|≤r0/4 and |w_j|≥r0,
then for either target endpoint

    |rho_j−z±|≥r0−|s|≥3r0/4>r0/2≥2|s|=|z+−z−|.         (0)

This holds for both signs of D and at the double. Other exterior pairs
can still be closer to one another. Selecting the globally smallest pair
is a stronger, separate proposal; it is not needed for (0).

## 1. What can be selected

At a fixed time, a finite set of at least two zero occurrences has a
minimum pair distance. On a real ordered zero set, its minimum occurs
between neighboring zeros. In a complex divisor, “neighboring” needs a
specified metric or graph; ordering only real parts loses the vertical
separation of conjugates. All multiplicities must remain included.

The complete canonical divisor generally has no attained positive global
minimum at a simple slice. The inherited [GT Note33 §2][counts] gives
`N_t(X)~X log X/(4pi)` in the width-one strip. If all pair distances were
at least g>0, disjoint disks of radius g/2 around zeros in that strip and
0<Re z≤X would fit in an enlarged rectangle of area O_g(X), giving only
O_g(X) zeros. This contradicts the count. Thus the infimum of complete
pair distances is zero. If all zeros are simple it is not attained; if
a multiple zero exists, the distance zero is attained there. A finite
height window or another explicitly justified selection is needed.
This argument does not assume RH.

Our target must additionally be invariant under conjugation as a counted
two-occurrence cluster, so that c,D are real. An arbitrary closest complex
pair need not qualify. The four points

    ih, epsilon+ih, −ih, epsilon−ih,   0<epsilon<2h,

have closest horizontal pairs of length epsilon, neither conjugation
invariant. The vertical conjugate pairs have length 2h. Minimizing only
over admissible conjugation-invariant pairs is legitimate, but no longer
implies a lower bound on every cross-pair distance. For the vertical pair
±ih and exterior displacement epsilon+ih,

    Q=(epsilon+ih)²+h²=epsilon²+2i epsilon h

can be arbitrarily small. This finite example lacks the independent strong
collar of the CM tube; that is exactly why minimality cannot supply it.

Nor must the closest pair be the one whose nonreality matters. The
real-even polynomial divisor `{−epsilon,epsilon,−i,i}`, with
0<epsilon<1/2, has its unique closest pair on the real axis and still has
a nonreal conjugate pair. Among admissible pairs, Euclidean closest means
smallest `|D|`, not smallest signed D. Therefore proving a statement only
about that pair does not automatically control every D<0 pair.

## 2. The geometry available under the stronger minimum hypothesis

Suppose at one slice that the actual conjugation-invariant target
`z±=c±s`, s²=D, attains the minimum Euclidean distance over **all**
distinct zero occurrences under consideration, with g=2|s|>0. For every
exterior occurrence included in that comparison, w=rho−c satisfies

    |w−s|≥2|s|,  |w+s|≥2|s|,
    |Q|=|(w−s)(w+s)|≥4|D|,
    |w|≥sqrt(3) sqrt(|D|).                                (1)

The last bound follows by adding the two squared-distance inequalities:
`2|w|²+2|s|²≥8|s|²`. These statements hold for both real signs of D.
They are only relative-to-gap bounds and vanish as D tends to zero.
The CM condition `|w|≥r0=a ell`, with target radius at most r0/4,
is an independent, stronger separation requirement and remains unpaid
by (1). A window minimum gives (1) only for the compared occurrences;
zeros outside the window require separate treatment.

In fact the endpoint-neighbor inequalities alone suffice for (1); no
comparison of exterior-exterior distances is used. The existing collar
already implies them by (0) and supplies the stronger bound
`|Q_j|≥15r0²/16`, while `4|D|≤r0²/4`. The new global-minimum assumption
adds no improvement to that particular denominator estimate. It could
constrain exterior-exterior packing, but such a use would need its own
verified selection premise and quantitative comparison.

Minimality does not sign the exterior interaction. For the finite
real-even configuration `{±ib,±3ib}`, choose target ±ib. Its distance
2b is minimal, with ties, but

    D=−b²,  M=2/(−9b²+b²)=−1/(4b²).                      (2)

The configuration `{±ib,±sqrt(3)b}` also has the target as a minimum
pair, but gives M=1/(2b²)>0. These are polynomial slice examples, each
admitting its finite exact heat evolution. They are not canonical theta
counterexamples and do not satisfy the stronger CM collar ratio. Their
purpose is to test minimality alone, not the conjunction with all CM inputs.

For comparison, in the **all-real ordered class with an attained positive
global minimum gap** g=2s, D=s²>0, the k-th exterior zero on either side
has distance at least (2k+1)s from c. Hence, allowing fewer terms if one
side is finite,

    0≤M≤2 sum_(k≥1) [4k(k+1)D]^(−1)=1/(2D),
    D'=2−4DM≥0.                                          (3)

This telescoping estimate illustrates useful extremal geometry. Its
all-real/global-minimum premises cannot be imported into the canonical
problem at an unknown-real slice. A finite-window version also retains
the unbounded exterior contribution. Forward nondecrease does not itself
pay a backward-time gap margin.

## 3. A slice choice is not a moving-tube hypothesis

The symmetric coordinates and S/T hierarchy follow one counted pair on
an independently established tube. A minimum chosen at the initial slice
can cease to be the minimum later. A strict minimum among a fixed finite
family of continuously followed pairs persists locally while its gap to
the competitors remains positive; ties and entries through a window
boundary need their own treatment.

Switching to a new minimizer changes c, D, the removed pair and the whole
exterior moment sequence. The new pair's contour, initial data and gap
anchor are not inherited from the previous pair. The old solution remains
valid for its original pair; relabeling the minimum does not create a
single solution of that old initial-value problem. In particular,

    W(x,y)=exp(−4 integral_x^y m)

and its gap identity cannot be spliced across different pairs without
explicit switch data and a proof that the resulting bound controls the
intended envelope. A finite minimum of squared gap functions can instead
be treated by one-sided/active-branch analysis, but that is a distinct
extremal argument, with hypotheses checked for every active branch.

At an isolated double event the colliding pair already has minimum
distance zero. This does not add an exterior collar or signed estimate.
For multiplicity greater than two, selecting two coincident occurrences
does not produce an isolating count-two contour; higher clusters remain
outside the existing target-pair premise.

## 4. Admissible use and relation to BBGKY continuation

Use a minimum only after specifying the finite comparison region and
admissible pair family. Choose an independently isolated minimizer at a
reference time and retain its pair identity. Apply minimum-derived geometry
only on the subinterval on which that same pair is known to remain minimal.
Any switch or claim about all problematic pairs needs an explicit coverage
argument. On a colliding branch, use the independent local isolation already
required by CM; do not infer it from a zero minimum distance.

This is compatible with the B05 reconstruction proposal but is not a new
prerequisite for [E16][e16]. Its frozen approximation theorem remains on
the original independently established tube. It may later be applied to
any suitable extremal tube once its data have been supplied. No change
to E16, signed-result status or manuscript is made here.
Reselecting the closest pair at each finite divisor cutoff N can also
change the center and send the selection outside the fixed region;
the fixed-pair convergence sought by E16 does not prove convergence of
such reselected minimizers.

The [controls12][controls] premise screen and [Note13 §5][control-table]
remain applicable: Euler/finite-square/score/prime perturbations change
the complete theta source or reflection; reflected super-Gaussians fail
the order-one input; smooth/primitive, atomic and finite-profile sources
lack the documented canonical population/profile or unpaid transfer;
RH-conditional, changed-readout and fractional controls retain their
listed arithmetic, physical-readout or integer-realization failures.
Static surgery lacks a common canonical heat tube and a scalar consumer
need not realize any divisor. A colliding pair in a finite control window
is itself closest at the event; selecting it is not a canonical discriminator.
The finite examples above test only the stated selection implications.

**Disposition:** accept closest-pair selection as a local, explicitly
qualified extremal device. Do not impose it as a global or full-tube
without-loss assumption. E16 remains the next ready E task, recommended
to Sol; no new execution packet is justified by selection alone.

[request]: ../research-progress/handoffs/VCD-GT-CM-B06-r1.md
[register]: ../research-progress/01_VCD_GT_CM_RESEARCH_PROGRESS_20261117.md
[counts]: ../../notes/33_VCD_GT_E12_UNIFORM_SIGNED_FAR_EXTERIOR_20261117.md
[e16]: ../research-progress/handoffs/VCD-GT-CM-E16-r1.md
[control-table]: 13_VCD_GT_CM_B03_JOINT_TRANSPORT_AND_SUPERZETA_20261118.md
[results]: ../../../../../../result-summaries/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[classification]: ../../../../../../avoid/01_restating_the_target.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[premises]: ../../../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md

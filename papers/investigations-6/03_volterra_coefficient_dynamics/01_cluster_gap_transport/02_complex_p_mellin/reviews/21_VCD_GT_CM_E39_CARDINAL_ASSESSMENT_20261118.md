# E39 — Cardinal source-error assessment

18 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. The task records the selected helper as
**gpt-6.1-sol / ultra**; a separate actual serving-model/effort attestation
is unavailable. The assessor did not author E38's proof or consumer.
This is a nonauthor **internal shared-premise assessment**, not an
independent specialist review or independent canonical source calculation.

**Disposition: accepted within scope without required correction.**
The actual cardinal norm is proved below 17, the refined complete-source
allowance is sound, and the one prescribed replay passes the frozen
factor-ten width gate with a factor exceeding **33.9494** against Record19's
centered baseline. The remaining centered-versus-independent gain at the
new budget exceeds **3.4637%**. The historical accounting wording
qualification below does not change the final work count or enclosures.

Read-first routing: [result summaries][results], [avoid][avoid],
[cluster18][cluster], [controls12][controls], [classification01][class],
[premises02][premises] and [scope07][scope]. Under avoid01 this is a
finite error/width milestone. It is not an RH-equivalent criterion.
The live register remains owned by the parent research task.

## Independent preflight

The actual reconstruction in `vcd_gt_lehmer_certificate.py` uses degree
32 and the reversed Lobatto nodes

    x_j=cos((32-j)pi/32), j=0,...,32.

Its node and mode weights are both d_0=d_32=1/2 and d_j=1 otherwise.
The factor `2*d_k/32` outside the node-weighted cosine sum is the DCT-I
interpolation coefficient, including both endpoint modes. Reversal only
changes cosine signs and preserves the orthogonality identity.

For the exact cardinal polynomials ell_j, DCT-I orthogonality gives

    sum_j ell_j(x)^2/d_j = (2/32) sum_k d_k T_k(x)^2.

Weighted Cauchy--Schwarz and sum_j d_j=32 therefore yield

    sum_j |ell_j(x)| <= sqrt(2 sum_k d_k T_k(x)^2) <= 8

on [-1,1]. No claim of sharpness is needed. For x<-1, every numerator
product in the cardinal formula has positive sign since degree 32 is
even, while its denominator has sign (-1)^j in the implemented ascending
node order. This agrees with T_32(x_j)=(-1)^j. Exact interpolation of
T_32 thus gives

    sum_j |ell_j(x)| = T_32(x)=T_32(-x).

The identity extends to x=-1 by continuity. Monotonicity of the
hyperbolic cosine representation on [1,503/500] proves

    sup_(x in [-503/500,1]) sum_j |ell_j(x)|
      <= max(8,T_32(503/500)) <17.

The final inequality was separately checked without any source
evaluation by exact rational recurrence; its exact value is

    1803430947144682413866830693604378620008431854098058020625044410533190410003841
    /108420217248550443400745280086994171142578125000000000000000000000000000000000.

For arbitrary complex nodal errors e_j with |e_j|<=E_node, the real
cardinal weights give |sum ell_j e_j|<=E_node sum|ell_j|. No independent
complex coefficient uncertainty is substituted for those nodal errors.

The fixed exact polynomial must be distinguished from its enclosing
arithmetic representation. Exact recorded decimal complex midpoints,
exact roots of unity, the finite spatial DFT and exact DCT-I define P.
The inherited Arb/acb reconstruction and evaluation enclose that P;
all coefficient radii and outward evaluation must remain present.
Rounding coefficients to their arithmetic midpoints would instead
require a new separately paid rounding allowance. The sharper cardinal
bound pays only the three inherited pre-time nodal error components.
It does not alter the true-field time remainder, its enlarged radius-five
majorant, node-product payment, or polynomial angular/time derivative
weights.

The single authored-proof pass checked [Note45][proof], Sections 1--4,
against this independent derivation. Its endpoint weights, orthogonality,
cardinal signs, rational comparison and exact-versus-ball distinction
agree. No mathematical correction was required before execution.
The fixed source contract in the [E38 request][request] matches this
proof. All 11 rows of the [E38 input manifest][pins] were verified before
the proof disposition; the manifest SHA-256 is
`c17c8393f0f2e0bb53e34fbddd230683888318e2b838cc4228ae99f23228ab62`.
The inherited geometry schedule is allowed, while the final whole-time
pass is fixed at 512 closed cells. No full numerical source certificate
was run during this preflight.
Record19's centered width, approximately 7.8004692263759084e-7, is the
frozen comparator for the requested factor-ten gate. The proposed
operator estimate is generic and also holds for collision controls;
it supplies no collision discrimination by itself.

## Implementation and whole-path meaning

The [new consumer][code] imports the pinned E36, E34 and GT consumers
without modifying them. It checks all 11 E38 pins, the inherited E34
pins, and both stored/content hashes of the fixed 33-by-128 archive.
The pair remains a=140101/10, I=[-3/10000,1/10], both degrees remain 32,
precision is 224 bits, and the contour has 128 represented nodes.
No new xi/source evaluation is made.

`cardinal_error` changes only the multiplier of the three pre-time
nodal components. It retains the factorial/radius/product formula for
E_time, returns the same Chebyshev value and derivative weights, and
keeps the outward coefficients throughout `ExtendedField`. Its
1089-coefficient radius diagnostic is below 3.922e-54 and is already
paid inside those balls. The refined uniform field error is below
.008170448251, versus .528676064 before refinement; E_node is below
.000480614603 and the unchanged E_time is below 1.145383e-15.

All affected geometry is re-enclosed on the entire I. Canonical and
quadratic geometry both pass the inherited first 16-cell/64-arc stage.
Count two and the annular right-half-plane logarithm are established
before testing D's sign. Both source paths use exactly 512 closed time
cells. The canonical path gives D<.179119 and
.599312<M<.615573, with the stronger frozen gates |D|<1/5 and
0<M<77/125. The complete-source identity D_t=2-4DM therefore gives
D_t>942/625=1.5072 throughout I, including the argument when D is
negative. Hence min_I D=D(-3/10000). The endpoint comparison is a
whole-path-minimum enclosure, not an endpoint sample replacing a tube.
The full-time forcing floor exceeds .40539857. All count, clearance,
Q-denominator and annular integration payments are retained. Their
complete-source derivations remain shared inherited premises.

## Matched finite comparison

Both estimators receive the same refined field error, new geometry,
65 endpoint log rectangles, annular moment errors and exact-midpoint
rule for h. They call the inherited E36 support assemblers. The full
range of (Gamma-h)^2 is subtracted, including an upper payment below
3.371e-17. New annular bounds are computed with the same formulas
using the re-enclosed geometry; they are not omitted or copied blindly.

The factor-ten gate compares the new width's outward **upper** bound
with a **lower** enclosure of Record19's high-precision centered
width. It uses that record's endpoint fields rather than its short
display-only ball. The residual gain likewise compares with a lower
enclosure of the new sharp Cartesian width. These directions certify
the gains without inflating either comparator.

| Estimator | Certified width or outward width upper bound |
| --- | ---: |
| Record19 centered, old source accounting | approximately 7.8004692264e-7 |
| Independent moments, refined source accounting | approximately 2.3801151707e-8 |
| Centered direct, refined source accounting | below 2.29767333e-8 |

The factor over Record19 centered exceeds **33.9494**, with width
reduction exceeding 97.0544%. The residual centered improvement over
new sharp independent moments exceeds **3.4637%**. These are distinct
comparisons: the larger improvement is sharper source-error accounting
for an already centered direct estimator, not a new 33-fold correlation
gain. The whole-minimum enclosure is contained in

    [0.00082198577487, 0.00082200875162].

In particular min_I D>.00082198577487 and its margin above .0001
exceeds .00072198577487. The statistic, selected pair, source and
physical interval are unchanged. No speed saving, superiority over
all direct methods, recursive advantage or new source coverage follows.

The existing width decomposes into about 1.18700482146e-8 of log-box
support, 1.11066850419e-8 of annular-tail support, and 3.37093734e-17
of shifted-square range. Their sum differs from the reported outward
width by about 4.226e-67, paid nominal/endpoint arithmetic. The first
two fractions are about 51.66% and 48.34%. The log rectangles include
retained coefficient/evaluation arithmetic as well as scalar source
error. Keeping the current estimator's annular allowance while reducing
only its node-log term cannot produce another tenfold gain. This is
an allowance comparison, not a lower bound on actual error or a general
obstruction to different direct/correlated estimates.

## Bounded corrections and cost accounting

The author exhausted the two allowed accounting repairs. The first
derives an otherwise unused old direct interval from the prepared logs
instead of invoking `ext.endpoint` again. The second records actual
duplicate-log work and decomposes existing width terms. Neither changes
the source, parameters, support formulas or gates. The bounded final
code check found no required further correction.

The primary reading copy's recorded SHA-256
`21a837e286f4d709d2fb2ebc76cb20eb48ebd43a5475c316e049b618a102ea4d`
was independently verified. Recursive comparison of all common JSON
leaves between primary and final Record22 found every existing
non-timing source/mathematical/control value identical. Only the script
hash and repair count change among common non-timing leaves. Additions
are the width decomposition, log-work accounting, primary provenance
and repair descriptions. This is stronger than the author's selected
31-field comparison.

The final log-work formula is correct. Each inherited full-F consumer
computes 65 logarithms for the moment/M pass and another 65 for F.
The two 512-cell paths use 133120 actual complex logarithms. Two shared
endpoint preparations add 130 and the separate quadratic collision
consumer adds 130: **133380 actual complex logarithm evaluations**.
The two support assemblies use prepared boxes and evaluate no logs.
The 128 represented contour nodes and 65 upper-half boxes are different
counts from total work.

One historical wording qualification is explicit: `local_repairs[0]`
calls the removed invocation a "65-log integration". The inherited
invocation actually makes **130** logarithm evaluations. The final
133380 total correctly excludes it. This historical label is not used
for final arithmetic or work accounting; it requires no third repair.

Archive verification, polynomial/error reconstruction, coefficient audit,
field construction, full geometry/path and endpoint preparation are
charged to both estimators. Their support assemblies are timed separately
with one warmup per method and 21 alternating-order pairs. Original
source generation remains a common paid input. The assessor replay took
about 1.409 seconds, with canonical common preparation about .871 seconds;
median assemblies were about .134 ms for independent moments and
.239 ms for centered direct. Timing is descriptive. No equal-total-cost
or source-acquisition speed claim is accepted.

## Collision controls and scope

The exact quadratic w^2-2(t-1/20) passes count-two/annular geometry and
the same 512-cell machinery with zero true-field error. Both estimators
contain D=0 at t=.05; the full consumer also contains F=0. Across the
collision its strict D>.0001 and F>=.3 path gates both fail, as required.

The cardinal theorem is generic interpolation algebra and holds for the
catalog controls. The canonical application separately requires the
unchanged complete source and strict numerical margins. Note45's premise
table retains the catalog distinctions: Euler-factor controls change
normalized coefficients/completion; weighted-square and finite-tail/score
variants fail full reflected unit weights; finite-prime variants fail
full reflection/complete arithmetic; reflected super-Gaussians fail the
canonical order-one arithmetic class. Shape, primitive and finite-profile
controls fail complete arithmetic/profile/count transfer; atomic controls
fail the complete population/full profile/eventual-simplicity premises.
RH-conditional endpoints retain RH as input and change Dirichlet
arithmetic. Changed kernels fail literal cosine/Newman readout; fractional
profiles fail integer multiplicity; static surgery supplies no common
canonical heat tube. These failures do not make the cardinal norm itself
a discriminator.

No all-height/Newman conclusion, census forward tube, E16 approximation,
stable hierarchy truncation or recursive convergence is acquired here.
Each negative allowance comparison remains confined to its named class,
as required by avoid07.

## Final pins, replay and continuation check

The [E39 final manifest][finalpins] has eight files and SHA-256
`358e3ce2049ad84a0e3051541e3159def40bc9eb1f334d8dd9ded0018480fe93`.
Every final pin matched before and after the one prescribed replay.
The final author script is bound by
`d03fd876982885cdd78b20c4a563301ae0461e1926f8173e52e3bbccd560705b`;
Record22 is bound by
`852bbab959a644951a62e82d184c947d6e53f7d76bc6ebfb20cd062386c31b13`.
All canonical gates and control outcomes pass at the same Python 3.10.0,
python-flint 0.9.0, FLINT 3.6.0 and 224-bit settings as the author.

The external raw replay has 61147 bytes and SHA-256
`580f06c79bd366db7262841ae7489b3dfcfc0eda368cbca5e616ab318e0c9727`.
Its [compact Record23][replay] lists exactly 28 current timing-path
exclusions. After those exclusions, **every** remaining field equals
Record22, including historical first-attempt timing/provenance. The
canonical serialized comparison hash is
`8ab14068dab03f671f62239e2f9ba48cf33a0a170378756b433f362bbe2fc747`.
The exact exclusions are: current canonical geometry/path attempt and
setup times; coefficient audit time; the nine common-preparation timing
paths; two assembly sample arrays and two medians; seven control timings;
and current root input-validation/elapsed time. Record23 supplies the
unambiguous individual paths. No historical timing is dropped.

The replay is from shared pinned sources, not an independent source
calculation or specialist validation. It is the only E39 full replay.
No extra source run, precision escalation or repair was performed.

[Continuation46][continuation] was separately checked for the numerical
interval, factor, residual gain, error/decomposition statements and their
fixed-annular scope. They agree with Record22. Its proposed E16 work is
clearly a pending structural task; this check accepts no approximation
theorem or convergence conclusion. The sole register owns live status.

[results]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[cluster]: ../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[class]: ../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[proof]: ../notes/45_VCD_GT_CM_E38_CARDINAL_SOURCE_REFINEMENT_20261118.md
[request]: ../research-progress/handoffs/VCD-GT-CM-E38-r1.md
[pins]: ../research-progress/handoffs/VCD-GT-CM-E38-inputs-r1.json
[code]: ../numerics/vcd_gt_cm_cardinal_source.py
[finalpins]: ../research-progress/handoffs/VCD-GT-CM-E39-inputs-r1.json
[replay]: ../numerics/23_VCD_GT_CM_E39_CARDINAL_REPLAY_20261118.json
[continuation]: ../notes/46_VCD_GT_CM_CARDINAL_GAIN_AND_STRUCTURAL_CONTINUATION_20261118.md

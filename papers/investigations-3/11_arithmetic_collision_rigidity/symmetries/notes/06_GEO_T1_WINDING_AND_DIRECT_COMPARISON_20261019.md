# GEO-T1: physical winding and optimized direct certification on B

19 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual execution and authoring model
**gpt-6.1-sol (Codex)**, reasoning effort **ultra**, verified from session
metadata. Separate agents and a fresh process provide internal same-model
checks; no independent specialist human review.

**GEO-T1 is Complete as a bounded comparison and validation.** Both methods
certify absence of simultaneous physical H,Hx zeros on the closed box
B=[1/100,1/5] x [999,1001], at 192 and 256 bits. Winding is exactly zero
using seven accepted whole boundary segments and ten complete enclosure
calls. Optimized direct certification covers B with three full-time spatial
strips and seven complete calls. Common acquisition dominates both cold
costs. The declared factor-two gate fails; B was already covered. Stop this
fixed-box comparison. This is neither new coverage nor a useful input for
S07-T3, which remains Waiting.

## Contract, source and complete errors

The [frozen pre-computation contract][contract] selects B from the documented
[S01 whole-time signed-test bottleneck and time-slab repair][s01]. That
stronger signed-test failure was not a failure of the weaker direct first-jet
criterion. This comparison tests the latter and it succeeds without time
subdivision. There was no box scan, parameter search or switch of metric.

The unchanged [whole-cell producer][source] evaluates the complete reflected
theta contour before truncation, with modes 1..11, U=2,
d=pi/8-4log(1000)/1000, center (21/200,1000), spatial/time degrees 24/12,
orders 0..50 and a common absolute moment through order 52. Its derivation
and admissibility conditions are in [Note 13][source-note]. All physical
jets use the same fixed positive
Gc=1000^(7/4) exp(-125 pi), which is never differentiated.

Write delta_t=t-21/200 and delta_x=x-1000. The shared polynomial for
spatial order j=0,1,2 is

P_j=sum_(k=0..12) sum_(l=0..24)
    (-delta_t)^k delta_x^l h_(j+l+2k)(21/200,1000)/(k! l!).

The minus sign comes from H_t=-H_xx. Each method receives the intersection
of two independently valid complete images of this same polynomial:
time-first then space, and space-first then time. Each image already pays
the full quadrature, Taylor, nonstationary mode-tail and retained-source
error. Intersecting the two valid images removes interval overestimation;
it neither removes nor pays the same physical error twice. Quadrature
radii and analytic truncation payments retain their separate source ledger.
No differentiated tail bound is substituted for a derivative error.

Source acquisition is fresh once at each precision. Within a precision,
read-only acquired dyadics are shared, and each method starts with its own
empty coefficient cache; clone/cache creation counts in consumer cost.
The exact setup dyadics, complete errors, source/contract/helper/producer
hashes, precision and model/effort are saved in the two [comparison records][num].
Source setup is charged to both methods. The consumer order is winding then
direct at 192 bits and direct then winding at 256 bits.

Both methods' maximum complete added component errors over their requests
are below 4.620515e-12, 3.469201e-12 and 3.055846e-12 respectively, in
physical/Gc units. These are full component error allowances, not estimates
of the actual error. The respective recorded maximum allowances coincide.
All 60-second, 512-enclosure and depth caps remain fixed; no budget was
expanded to obtain either pass.

## Whole boundary and exact degree

The boundary follows positive dt wedge dx orientation, traversing
(tlo,xlo), (thi,xlo), (thi,xhi), (tlo,xhi), then returning to its start.
Here is the complete closed partition; a sign applies to the entire
segment, with all errors included.

| Face | Whole segment in t,x | Strict coordinate sign |
| --- | --- | --- |
| Lower spatial wall | (1/100,999) to (1/5,999) | H<0 |
| Upper time face | (1/5,999) to (1/5,1000) | Hx>0 |
| Upper time face | (1/5,1000) to (1/5,2001/2) | Hx>0 |
| Upper time face | (1/5,2001/2) to (1/5,1001) | Hx>0 |
| Upper spatial wall | (1/5,1001) to (1/100,1001) | Hx>0 |
| Lower time face | (1/100,1001) to (1/100,1000) | Hx>0 |
| Lower time face | (1/100,1000) to (1/100,999) | Hx>0 |

The minimum certified strict coordinate margin is **>0.00479432845** in
physical/Gc units at both precisions. Ten complete enclosure calls comprise
seven accepted segments and three rejected parents; the maximum segment
subdivision depth is two. All faces, both walls, corners and possible root
wall crossings are retained. No endpoint-root-count shortcut or missing
wall flux enters this calculation.

At each boundary vertex choose rational coordinates meeting the two
incident halfplane constraints: impose +1 or -1 for a constrained
coordinate, zero otherwise. Opposite constraints in the same coordinate
would reject the construction. For this partition, the polygon vertices are

[(-1,1),(-1,1),(0,1),(0,1),(0,1),(0,1),(0,1)].

Every edge has both endpoints in its own strict halfplane. The vertices
need not approximate the actual jet at boundary endpoints: the existing
[convex-homotopy lemma][winding] requires membership in the incident
halfplanes. This construction uses **zero source vertex evaluations**.
Repeated nonzero vertices and a degenerate polygon are allowed; its exact
rational winding is zero. An origin vertex or origin-crossing edge is
rejected by the helper.

The imported [all-multiplicity physical index theorem][index] gives degree
minus the sum of floor(m/2) over interior heat collisions, under its analytic
and isolation hypotheses, which the unchanged complete theta source
satisfies on this compact domain: real analyticity and H(t,0)>0 exclude an
identically zero slice, and the local finite-multiplicity theorem supplies
isolation. Each collision contributes with the same
negative sign. Thus degree zero excludes interior events; the complete
strict boundary cover excludes boundary events. Together they certify
closed B. Winding alone supplies no numerical lower bound for the interior
first-jet norm. The polygon construction is an implementation of the
existing theorem, not a new local-index theorem.

## Direct baseline, coverage and cost

The direct method uses complete H,Hx,Hxx on adaptive full-time spatial
strips. It first tests sqrt(abs_lower(H)^2+abs_lower(Hx)^2). If necessary,
a separately charged whole-time spatial-midpoint call and the cell's bound
on sqrt(Hx^2+Hxx^2) give a paid spatial Lipschitz test. All such calls count.
All three accepted cells pass the Cartesian first-jet norm test:

| Full-time spatial strip | Certified physical first-jet norm / Gc |
| --- | ---: |
| [999,1000] | >0.05560863553 |
| [1000,2001/2] | >0.06774831772 |
| [2001/2,1001] | >0.00243380243 |

These three closed strips cover B exactly. They give a uniform complete
direct radius **>0.00243380243**. Two rejected parent cells also use their
paid midpoint tests: five cell evaluations plus two midpoint evaluations
make seven complete calls. Maximum spatial depth is two. The predeclared
four-time-slab fallback is not needed. Exact rational partition verification
rejects an unexplained cover gap; a partial accepted collection cannot pass.
The direct interior norm lower bound and the winding boundary coordinate
margin measure different quantities and are not ranked as competing radii.

The recorded cold total is fresh evaluator acquisition (`setup_seconds`)
plus timed consumer work, including cache creation. Module imports,
provenance assembly and receipt serialization are outside these timers;
adding that common overhead cannot create a factor-two gain. Sequential
observed times in seconds, with identical fresh acquisition charged to
each method, are:

| Bits | Shared setup | Winding consumer | Direct consumer | Winding cold total | Direct cold total | Direct / winding cold |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 192 | 9.163551 | 0.013970 | 0.008329 | 9.177520 | 9.171879 | 0.999385 |
| 256 | 9.677610 | 0.013951 | 0.008540 | 9.691561 | 9.686150 | 0.999442 |

The primary factor-two cold-cost gate fails at both precisions. Even a
free winding consumer would improve these direct cold totals by less than
1.001, because setup dominates. These are observed costs of these matched
implementations in this environment, not universal hardware bounds or an
obstruction to winding on other domains or acquisition models. Call counts
are comparable here because both call the identical three-jet evaluator;
heterogeneous counts from older pilots are not substituted for total cost.
The slightly different consumer timings do not establish a general speed
ordering.

## Controls, review and stopping scope

The [actual-helper control checker][checker] passes 36 checks at both
precisions. Its own whole-boundary interval polynomial sources give
quadratic and cubic heat-collision degree -1 and quartic degree -2 on
[-1,1]^2; the exclusion interface rejects these nonzero degrees. H=x and
H=1 have degree zero and pass. A collision on the boundary and uncertainty
reaching zero remain inconclusive. Reversed orientation, omitted walls,
partial budgets, incompatible halfplanes, origin vertices and edges,
inexact domain input and invalid limits exercise fail-closed paths. These
are actual new-helper controls, not just copies of inherited event flags.

The actual direct consumer is separately exercised on frozen B with its
own shifted quadratic H=(x-1000)^2-2(t-21/200), an exact constant, and a
true constant supplied with uniform value uncertainty one. The heat event
is inconclusive with an incomplete cover after 84 calls; midpoint propagation
is exercised and does not erase the event. The constant passes in one call;
persistent uncertainty remains inconclusive at the fixed 512-call cap.
Polynomial controls lack the complete normalized theta source expansion;
the generic heat-index theorem still applies to them and correctly detects
interior events. A noncollision certificate is allowed to pass a control
on a collision-free box.

The [fresh inherited source regression][source-controls] retains five
event enclosures and the Euler negative-Laguerre witness with each altered
source's own errors. The new strict-coordinate separator also refuses all
five enclosed event jets. These are surrounding-event/interface checks,
not whole-boundary winding certificates for those altered sources. Euler
rejects the signed test; negative Laguerre alone need not reject local
noncollision winding. Finite weighted squares lack complete reflection and
unchanged complete coefficients; reflected super-Gaussian and exact-threshold
qTa sources lack theta's normalized square expansion; Euler factors change
the complete coefficients. Finite-prime and smooth positive-primitive
families remain analytic premise screens without an effective new event
box. No theta constants are substituted into these controls.

The inherited [wall-flux checker][wallchecker] is freshly replayed on its
own exact heat-polynomial/moving-wall controls, including tangent and odd
wall crossings; it is not a new theta certificate. A separate internal
reader reviews source payments, Horner intersection, the whole-boundary
homotopy, exact degree, paid direct propagation and coverage. A fresh
192-bit comparison replay agrees in all mathematical record content after
removing timing and callback observations; exact polygon replay also
agrees. See the [internal review][review] and [records][num]. Hashes establish
identity, not mathematical validity or arithmetic portability.

This result follows the [result-summary guide][summaries], [local heat-flow
cluster][local-results] and [patterns to avoid][avoid], particularly
[target restatements][a01], [scope][a07] and [known certificates][a11].
**The bounded validation passes; the declared performance gate fails.**
B was already certified. No new coverage, global sign estimate, physical
S07-T3 input, Newman bound or RH result follows. Stop this fixed-B comparison;
other winding implementations, genuinely different bottlenecks and new
signed analytic mechanisms remain outside the exclusion. No scan or
manuscript change is activated by this stopping decision.

[contract]: 05_GEO_T1_MATCHED_WINDING_COMPARISON_CONTRACT_20261019.md
[s01]: ../01_modular_self_duality/notes/02_COMPLETE_PAIRED_TAIL_CONSUMER_AND_STOPPING_DECISION_20261019.md
[source]: ../../numerics/high_height_consumer/high_height_consumer.py
[source-note]: ../../notes/02_updated_research_plan/13_VERTICAL_WALL_AND_FINITE_HEIGHT_NONCOLLISION_20261018.md
[num]: ../numerics/README.md
[checker]: ../numerics/check_winding_controls.py
[source-controls]: ../numerics/GEO_T1_SOURCE_CONTROLS_20261019.json
[wallchecker]: ../../../../investigations-2/active/22_theta_manifold_geometry/numerics/check_spacetime_wall_flux.py
[winding]: ../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/06_WALL_FLUX_AND_CERTIFIED_THETA_WINDING_20261015.md
[index]: ../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/04_SPACETIME_INDEX_AND_MARKED_TOPOLOGY_20261015.md
[review]: ../reviews/01_GEO_T1_WINDING_DIRECT_INTERNAL_REVIEW_20261019.md
[summaries]: ../../../../../result-summaries/README.md
[local-results]: ../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a11]: ../../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md

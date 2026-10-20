# BW-01: event-relative paired-face contract

19 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Model **gpt-6-astra (Codex)**; actual effort
**max**, verified from this chat's recorded turn metadata.

**Scope:** one analytic attempt within BW-01, fixed before its control
execution. This is not a numerical location for a theta event or a new
zero-free region. The [program][program] and [progress register][progress]
retain ownership of the wider task. Read the [result summaries][results],
especially [local laws][laws] and [controls][controls], and the
[patterns to avoid][avoid], especially [classification][a01],
[scope][a07] and [preserved cancellation][a12].

## Question and information class

Can the **odd difference of opposite time faces**, with the exact event
cancellations imposed before estimating its remainder, force zero winding
on a shrinking parabolic rectangle? Test the specific payment that keeps
the quadratic collision jet and bounds all remaining terms by complete
absolute derivative or source-moment bounds. Do not assume that this
payment exploits full theta arithmetic merely because its bounds are
obtained from the theta source.

The prospective outcome is either a new signed restriction or a precise
obstruction to that payment. The local index -1 is inherited. Reproving it
or improving the accuracy with which it is recovered is not an arithmetic
exclusion. No computation-time advantage is proposed.

## Fixed source, parameters and geometry

Use the unchanged physical source

\[
H(t,x)=\int_0^\infty e^{tu^2}\Phi(u)\cos(xu)\,du,\qquad
\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})
 e^{-\pi n^2e^{4u}}.
\]

Assume hypothetically T=Lambda>0, a>0, H(T,a)=Hx(T,a)=0 and
h2=Hxx(T,a) nonzero. We use the inherited conservative range T<=1/2;
it is not a claim that sharper known bounds are unavailable. Choose
0<R<min(a,sqrt(T),1/2), then 0<r<=R, and set

\[
D_r=[T-r^2,T+r^2]\times[a-r,a+r],\quad
(\tau,y)=((t-T)/r^2,(x-a)/r).
\]

Orient by dt wedge dx. The four complete faces follow
(-1,-1),(1,-1),(1,1),(-1,1),(-1,-1) in (tau,y).
No assertion that H is nonzero on the spatial walls is permitted.
The comparison uses the **full first jet**, so root crossings of those
walls must be retained. There is no moving cutoff or coordinate-dependent
normalizer. The fixed target transformation

\[
F_r=(H/(h_2r^2),H_x/(h_2r)),\qquad
Q=(y^2/2-\tau,y)
\]

has positive determinant even if h2<0. Its degree is the physical degree.
The exact h2 is an analytic parameter, not an acquired numerical value.

## Selected observation and complete payments

For s=r^2 and |z|<=r, retain the signed pair

\[
A_s(z)=\frac{H(T-s,a+z)-H(T+s,a+z)}{2s}
=-\int_0^\infty e^{Tu^2}\Phi(u)
 \frac{\sinh(su^2)}s\cos((a+z)u)\,du.
\]

The accompanying full-boundary payment uses suprema of |Hxxx| and
|Hxxxx| on D_R, divided by |h2|. The face-pair remainder requires the
sixth absolute moment separately. For j<=6 define

\[
M_j(b)=\int_0^\infty e^{bu^2}\Phi(u)u^j\,du,
\qquad b=T+R^2<1.
\]

Each required spatial derivative on D_R is bounded by its own M_j(b).
These finite exact integrals already include every mode and source tail.
Their finiteness is sufficient for an event-dependent analytic radius;
no measured theta moment or event is asserted.

For a future numerical implementation of this particular real-source
contract, freeze N=4, U=1. The complete allowance for each moment or jet
through order six is: retained-integral outward quadrature error, plus
the omitted n>4 integral on [0,1], plus the all-mode integral on [1,infinity).
The result note will spell out these two analytic tails, adapted from
the [existing wall note][walls]. Retained signed terms are combined before
an absolute value; no Riemann--Siegel correction, contour wall, or rotating
phase is used. No quadrature run is requested in this attempt. If parameter
or h2 intervals are later introduced, their propagation must be paid too;
zero is never replaced by an approximate midpoint cancellation.

## Comparison and falsification, fixed before execution

Compare logical exclusion strength under the **same retained information**:
event cancellation, nonzero curvature, and componentwise symmetric
remainder bounds about Q. Give the direct method exactly the same data.
This is not a comparison of runtimes or an assertion about arbitrary
boundary methods with additional signed arithmetic information.

The exact-control checker will test: the quadratic event; the even
quartic with T=1/4, a=1, r=1/8 and its negative; an event-free constant;
an event on the boundary; reversed traversal; uncertainty containing the
origin; incomplete boundary coverage. The quartic's all-real threshold
is inherited from the [predecessor][predecessor], with its PDE and event
jets rechecked exactly. Use each polynomial's own values and derivative
bounds, never theta moment constants. Whole rational interval segments,
not samples, must support every degree calculation. Any zero-winding
exclusion of an enclosed control event falsifies the implementation.

The broader positive-kernel, weighted-square, finite-prime, reflected,
primitive and Euler controls receive analytical premise screens; no
uncomputed event location or all-real threshold is assigned to them.
Record source hashes, the parent Git revision and the checker version in
a small execution receipt. The checkout already contains uncommitted
program setup, so its Git revision alone does not identify every input.

## Coverage and stopping rule

The analytic class is exact multiplicity two with an event-dependent r.
No lower bound on |h2|, uniform radius as T approaches zero, height bound,
or multiplicity extension is obtained. Stop this particular norm-payment
attempt if its admissible boundary information contains the ordinary
collision model at every accuracy. Continue BW-01 only with a specified
signed theta observation or a different acquisition advantage that this
information class discards. Such a stop does not close BW-01 or the other
seven routes.

[program]: ../../../research-overview/01_THRESHOLD_BOUNDARY_WINDING_RESEARCH_PROGRAM_20261019.md
[progress]: ../../../research-progress/01_THRESHOLD_BOUNDARY_WINDING_PROGRESS_20261019.md
[results]: ../../../../../../../result-summaries/README.md
[laws]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[predecessor]: ../../../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex
[walls]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/06_WALL_FLUX_AND_CERTIFIED_THETA_WINDING_20261015.md

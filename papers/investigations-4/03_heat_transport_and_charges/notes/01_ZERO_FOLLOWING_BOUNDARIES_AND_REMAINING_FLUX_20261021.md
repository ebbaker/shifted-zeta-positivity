# Following a zero: which boundary terms actually vanish

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **ultra**, verified from the active turn metadata.

**Classification: bounded analytic screen of the user’s moving-boundary
idea; inherited phase identity plus elementary energy bookkeeping.**
The suggestion is useful for removing selected boundary integrals.
It does not remove every flux or supply the remaining signed theta estimate.
The [result index][results], [avoid index][avoid], [wall geometry][geometry]
and [scoped-exclusion rule][a07] apply. No novelty claim is made.

## 1. There is an exact prior result for root-following phase walls

[BW09 Note 03][prior] already proves this mechanism for a real heat field
H_t=-H_xx. A simple real root x=w(t) satisfies
\[
 w'=H_{xx}/H_x.
\]
For the real jet J=H+iH_x, the pullback of its phase along that wall is
\[
 \frac{H_xH_{xx}-HH_{xxx}+w'(HH_{xx}-H_x^2)}{H^2+H_x^2}\,dt=0. \tag{1}
\]
At H=0, the time component H_xx/H_x and motion term -w' cancel exactly.
Thus the full wall phase contribution vanishes even though H_x is nonzero. An assertion
that the wall cannot vanish merely because H_x remains would be incorrect.

The inherited theorem requires simple root graphs with paid finite
continuation and regular caps. For the pair born at an ordinary double,
the bottom cap has adjacent roots. If the later cap has N simple interior
roots, its phase is -(N+1)pi; the truncated strip winding is -N/2.
The original event is carried by the lower connector when that event is
included. Assuming the walls stay consecutive assumes N=0; following them
does not establish an independent arithmetic cap count. The prior note
also checks an atomic positive-source threshold example with N=0.
These are inherited facts, not newly executed research or new control data.

## 2. Scalar energy loses its boundary terms; jet energy does not

Let a(t)<b(t) be C^1 simple real zero graphs on a regular time interval,
and let H be a sufficiently smooth real backward-heat solution there.
Write brackets for the right endpoint minus the left. Reynolds transport
and integration by parts give
\[
 \frac d{dt}\int_a^b H^2dx
 =2\int_a^b H_x^2dx-2[HH_x]_a^b
       +b'H(b)^2-a'H(a)^2
 =2\int_a^b H_x^2dx.                                      \tag{2}
\]
Both the moving-boundary density and the scalar integration-by-parts flux
really vanish. Following only one zero removes only that endpoint’s terms.
This is one precise benefit of the idea. It also has the
backward-heat sign: the energy increases toward later heat time.

For the derivative energy, however,
\[
 \frac d{dt}\int_a^b H_x^2dx
 =2\int_a^b H_{xx}^2dx-2[H_xH_{xx}]_a^b
       +b'H_x(b)^2-a'H_x(a)^2
 =2\int_a^b H_{xx}^2dx-[H_xH_{xx}]_a^b,                    \tag{3}
\]
using w'H_x²=H_xH_xx at each root. Consequently
\[
 \boxed{\frac d{dt}\int_a^b(H^2+H_x^2)dx
 =2\int_a^b(H_x^2+H_{xx}^2)dx-[H_xH_{xx}]_a^b.}            \tag{4}
\]
Following zeros of H does not eliminate the derivative/jet flux.
The choice of density or differential form matters; cancellation in (1)
or (2) cannot be transferred to a different energy by analogy.

## 3. A collision satisfies the cancellation exactly

For H(t,x)=x²-2t and t>0, let r=sqrt(2t) and endpoints a=-r, b=r.
They are simple roots, with velocity plus/minus 1/r. Directly,
\[
 \int_{-r}^rH^2dx=\frac{16}{15}r^5,\qquad
 \frac d{dt}\int_{-r}^rH^2dx=\frac{16}{3}r^3
                         =2\int_{-r}^rH_x^2dx.
\]
Nevertheless the interval collapses and H has an ordinary double at t=0.
The root derivative floor is |H_x|=2r and tends to zero. For the derivative
energy, integral H_x²=8r³/3, whose derivative is 8r; equation (3) gives
16r-8r=8r. The remaining jet boundary term is therefore nonzero.

This exact control lacks canonical theta arithmetic. It proves only that
vanishing scalar/phase wall terms coexist with an endpoint collision.
Using a fixed reference interval x=ru introduces r'/r=1/(2t); normalized
transport is singular at the collision. A positive later scalar energy
and its monotonicity in (2) do not force a positive endpoint energy.

## 4. The complex charge boundary and the Weil seam are different objects

The [BW12 complex jet][heat] is G=(H,H_z). On the simple zero locus H=0,
its projective direction is [0:1], which can simplify a pullback. But in
complex (t,z) spacetime that zero locus has real dimension two at a regular
point; it is not the full three-dimensional boundary carrying the Hopf
integral. A tube around it has additional faces. At a double, G=0 and its
normalized direction fails. The [complete flux identity][flux] still needs
all faces and a nonzero jet on the actual boundary. The real root-wall
identity (1) must not be identified with this different charge integral.
An argument-principle contour using H_z/H cannot pass through even a
simple H-zero; the regularity of H+iH_x on such a wall is specific to
the real-jet observable.

In the compact Weil task, x is the **log-position of the test function**,
whereas a tracked theta zero is in the spectral variable z. There is no
specified map that turns H(t,z(t))=0 into a zero of an arbitrary Weil test
at its support boundary. Even imposing f(0)=f(P)=0 would not remove the
nonlocal prime seam:
\[
 -2c_a\Re\int_0^a\overline{f(x)}f(x-a+P)dx.                 \tag{5}
\]
[BW12 Note 19’s paired collar controls][compact] already vanish near the
endpoints and make (5) take both signs. Their overlapping collar values,
not their endpoint traces, determine it. Moving a zero can remove a local
boundary term without removing this nonlocal interaction or the
[archimedean image correction][circle].

## 5. Decision and a useful reopening condition

Record I4-H00 as complete **for this bounded analytic screen**. Retain
root-following walls as an exact simplification when continuation of the
chosen simple roots is paid. Do not open I4-H01 merely from the cancellation:
a new complete-source estimate of the remaining cap count/normalized cap
integral, or of the residual jet flux, is still required. Using the same
cap/root-order data gives the same count as the direct method.

The [arithmetic collision register][controls] remains the screen for any
later theta exclusion. Euler-factor changes alter canonical arithmetic;
weighted-square/finite-prime sources lack full normalized reflection;
reflected/primitive sources lack canonical square coefficients. No invented
root continuation, threshold or cap count is assigned to those sources.
The actual substitution here is the exact quadratic in Section 3; the
prior note’s atomic and quartic controls retain their own scopes.

This conclusion does not dismiss moving boundaries in general. It locates
what their cancellation accomplishes and what the next source estimate
would still have to establish. [Target classification][a01] and
[coupled-estimate discipline][a12] prevent counting unchanged cap information
as a new sign gain. See the [review][review] and [shared progress register][progress].

[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[prior]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision/notes/03_ROOT_FOLLOWING_WALLS_AND_CAP_COUNT_20261020.md
[heat]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/17_PARALLEL_TRANSPORT_CONNECTIONS_AND_COLLISION_CONTROLS_20261021.md
[flux]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/18_HEAT_EVOLUTION_AND_EARLY_LATE_TOPOLOGICAL_TRANSPORT_20261021.md
[compact]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/19_COMPACT_SURFACE_SEQUENCES_AND_WEIL_POSITIVITY_20261021.md
[circle]: ../../01_compact_weil_positivity/notes/01_CIRCLE_COMPARISON_AND_POSITIVE_COMPLETION_OBSTRUCTIONS_20261021.md
[progress]: ../../research-progress/01_COMPACT_GEOMETRY_HEAT_TRANSPORT_AND_WEIL_POSITIVITY_PROGRESS_20261021.md
[review]: ../reviews/01_ZERO_FOLLOWING_BOUNDARY_REVIEW_20261021.md

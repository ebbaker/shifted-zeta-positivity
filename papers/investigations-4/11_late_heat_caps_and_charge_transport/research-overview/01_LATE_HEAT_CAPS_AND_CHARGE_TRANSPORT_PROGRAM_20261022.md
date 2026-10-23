# Late heat caps and charge transport research program

22 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex)**, reasoning effort **ultra**, verified from the active turn metadata.

**Purpose:** derive a source-specific analytical estimate for a distant
three-dimensional cap and its complete connectors, sufficient to constrain
the positive Chern–Hopf charge of a hypothetical multiple endpoint.
**Status:** the first analytical package is complete in its declared geometry and fixed-rank scope; the complete signed exclusion remains open. The original program below states the objective and completion contracts, not a claim that every task has been achieved. Execution was by gpt-6-astra (Codex), effort ultra, on 22 October 2026; setup provenance above is preserved.
The [progress register][progress] alone owns detailed LHCT task status.

## 1 Analytical objective and classification

The direction begins with Edward Baker's proposal: prove suitable root
statistics as real heat time T tends to positive infinity, use them to
bound a distant cap, and exploit vanishing zero-following sides to
constrain time-zero winding. The [founding assessment][assessment]
identifies the exact conditional argument and its missing estimates.

The principal objective is a complete cap/charge estimate. Pair statistics
are one route to it; direct complex-time saddle, field or jet estimates
are equally relevant. The program does not assume PCC at time zero or
identify large heat time with Montgomery's large-zero-height limit.

The statement that an independently bounded nonnegative integer charge
below one must vanish is a conditional consumer of an estimate, not a
new simplicity theorem or a weaker reformulation counted as progress.
A complete-window zero-charge condition may exclude other complex-time
events as well, so it can be stronger than endpoint simplicity alone.
Useful intermediate results include an explicit boundary construction,
a sharp complete cap remainder, a controlled weighted pair moment, or
a scoped failure of one declared estimating class. Their hypotheses and
quantitative gain must be stated.

Read the [result index][results] and [avoid index][avoid], especially
[heat geometry][geometry], [collision controls][controls],
[target classification][a01], [matching control premises][a02],
[scope][a07] and [coupled terms][a12]. No generic geometry or new
representation is counted as an arithmetic exclusion.

## 2 Field and complete boundary observable

Use the unchanged canonical field

\[
 H(\tau,z)=\int_0^\infty e^{\tau u^2}\Phi(u)\cos(zu)\,du,
 \qquad H_\tau=-H_{zz},
\]
\[
 \Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})
                        e^{-\pi n^2e^{4u}}.
\]

At time zero H(0,z)=xi(1/2+iz/2)/8. RH supplies reality at real times
T>=0 and simplicity for T>0, but does not exclude a multiple endpoint.
Local charge identities do not require RH. Any later use of RH,
Laguerre–Pólya structure or an all-real product theorem must be labeled.

Write tau=t+is and z=x+iy. Fix the physical jet frame

\[
 G=(H,H_z),\quad E=|H|^2+|H_z|^2,\quad
 \mathcal A=\operatorname{Im}(G^*dG)/E,\quad
 \mathcal C=\mathcal A\wedge d\mathcal A/(4\pi^2).
\]

For an admissible bounded four-dimensional window W with regular
complete boundary and isolated events,

\[
 Q_W=\int_{\partial W}\mathcal C
     =\sum_{p\in W}\binom{m_p}{2}\in\mathbb Z_{\ge0}.
\]

A physical late cap contains the imaginary-time interval:
M_T={t=T} times [-Y_T,Y_T]_s times Omega_T. Its flux is I_T=int_{M_T} C.
Both Y_T and the spatial region may vary only under an explicit geometry
and error contract. A real-time spatial fiber alone has dimension two
and does not carry this three-form integral.

For a tube whose caps have the same forward orientation,

\[
 Q_{W_T}=I_T-I_-+S_T.
\]

If I_T<=U_T, I_->=L_-, and |S_T|<=epsilon_T, then

\[
 \boxed{0\le Q_{W_T}\le U_T-L_-+\epsilon_T.}
\]

A strict upper below one excludes every enclosed multiple event. If the
only nonzero complete-boundary contribution is a far cap, that cap equals
Q. Alternatively, under a hypothetical ordinary double, a small linking
three-sphere has flux one. A regular event-free connector to the far
boundary gives 1=I_far+I_connectors; a source-derived upper below one
contradicts the candidate. These are distinct boundary contracts, not
permission to omit an early cap. In the complete-window method, other
interior positive-charge events can be retained; excluding them first is
unnecessary. In the linking deformation, the swept connector must avoid
unaccounted events and no event may escape across its boundary.

## 3 First analytical stage defining and continuing the sides

Specify one actual cap family and closing construction before invoking an
asymptotic theorem. Inventory all physical sides, imaginary-time faces,
early or linking closures, chart transitions and moving corners, with their
orientations. Boundary regularity must come from source estimates or a
proved construction, not an assumed internal zero separation.

The [projective-side lemma][projective] gives an exact sufficient condition:
on H_z!=0, a regular side |H/H_z|=epsilon maps projectively into a fixed
circle and has zero pulled-back curvature and zero C flux. Following
zeros by arbitrary moving spatial circles does not prove this condition.
The locus H=0 itself is only two-dimensional over the reals.

The first new result sought is a continuation theorem for such sides over
a declared finite or growing heat interval, including existence,
regularity, injectivity where needed, merging and joining pieces. At regular points, the complementary affine chart handles crossings
where H_z=0 but H!=0. At a joint zero H=H_z=0 neither chart is defined: keep
the event inside a full regular enclosing boundary, or excise it and retain
its linking boundary.
Local side cancellation does not already prove a global tube to infinity.
If a complete zero-side construction fails, retain and estimate a specified
connector rather than declare every moving-boundary method impossible.

## 4 Late heat asymptotics on the actual cap

The inherited [differentiated-saddle theorem][saddle] proves for fixed
finite positive root ranks

\[
 L_Tx_j(T)\to(j-\tfrac12)\pi,\qquad
 L_T(x_{j+1}(T)-x_j(T))\to\pi,
 \qquad L_T\sim\tfrac14\log T.
\]

This is a cosine/clock profile, not a theorem for a growing population.
It is compatible with a double-born pair at time zero. The initial
analytical task is to extend the required field and derivative estimates
to the actual cap: complex tau near T, complex z in Omega_T, and any
boundary motion. State the rank, spatial and imaginary-time ranges and
all parameter dependence. Pay the normalization and the derivatives
required by C; pointwise convergence of H or a real-axis gap law is
insufficient.

An explicit nonzero reference cap is acceptable. The exact heat control
H=e^tau cos z has

\[
 \mathcal C=\operatorname{sech}^2(2y)
                    ds\wedge dx\wedge dy/(2\pi^2).
\]

On a fixed rectangular cap its flux is 2XY tanh(2B)/pi^2, independent
of T, although its roots are perfectly separated and its connecting
side fluxes vanish. Thus the primary target is a proved signed bound for
I_T-I_T^ref with an explicitly evaluated reference, not an assumed zero
limit. A useful theorem must control the integrated error, including
cap volume or growing contours, rather than only its pointwise density.

## 5 Optional analytical bridge from pair statistics

On a finite proper regular cluster H=U product_i(z-z_i), set
b_i=(U_z/U)(tau,z_i) and Delta=product_{i<j}(z_i-z_j)^2. The
[founding calculation][assessment] gives

\[
 \frac{\Delta'}{\Delta}
 =8\sum_{i<j}(z_i-z_j)^{-2}
 +4\sum_{i<j}\frac{b_i-b_j}{z_i-z_j}.
\]

A late-heat pair theorem can be useful if it bounds this or a genuinely
cap-specific weighted observable. Specify the population, normalization,
physical gap scale and limit order. Weak pair-measure convergence alone
does not control the unbounded inverse-square weight. Derive sufficient
small-gap uniform integrability, exterior-factor estimates and tails,
without inserting the endpoint simplicity being sought. Complex-time
phase information must still be connected to the real-root statistic.
An infinite all-root interaction sum requires its own convergence or
renormalization proof.

Do not require a sine-kernel limit if the relevant heat regime has clock
statistics. A weighted analytical estimate adapted to the actual profile
is a useful goal. Conversely, merely reproducing density-one simplicity
from high-height PCC does not establish this heat-time cap theorem.

## 6 Complete source estimate and exclusion stages

Keep the canonical source and full reflection ledger in [home 02][source].
Head, tail and all omitted rays must contribute to one complete cap/error
estimate; retain mixed terms, phase lifts, corners, geometry uncertainty
and regulator costs if regularization is used. If a regulator delta and
T both vary, derive a joint error contract before interchanging limits.
Inherited fixed-window O(delta^2) estimates do not provide it automatically.

The first substantive cap milestone is an explicit analytically proved
integrated remainder on the declared family, or a strict improvement to
a named complete bound using the same source information. A vanishing
relative or averaged error is insufficient when an O(1) charge remains.
The total charge budget may use a nonzero common reference for both caps;
their signed difference and all closures determine the final margin.

Only after the geometry and analytical estimate are paid should the
register claim a finite event exclusion. For simplicity under RH, cover
arbitrary candidate height and every multiplicity, or prove a reduction
to the treated events. Height-dependent constants and windows are allowed:
a theorem valid at every arbitrary height can suffice without one uniform
negative-time all-real slice or one height-independent numerical margin.
A finite list of verified heights cannot replace that theorem.

## 7 Controls supporting numerics and research decisions

Apply the [collision-control register][controls] before advancing a sign
claim. Three inherited exact diagnostics are mandatory for matching local
hypotheses: the quadratic double retains linking charge one; the cosine
model retains a nonzero late cap despite simple clock roots; and the
projective shell retains its inner cap despite zero side flux. None has
the unchanged canonical arithmetic. Euler-factor, weighted-square,
reflected/primitive, finite-prime and normalized endpoint controls retain
their separate arithmetic/reflection failures recorded in the register;
none is assigned a new late-heat statistical theorem.

Numerics may verify wedge-product signs and constants, reveal a false
uniformity claim on an adverse model, or interval-certify finite constants
after an analytical inequality and source budget exist. They do not set
the main agenda. No pair-correlation sampling campaign, fitted asymptotic
law or assumed numerical jet floor is authorized by setup. A diagnostic
failure should sharpen or stop its specified analytical class; passing
checks is not evidence for an RH-equivalent target.

The first continuation should write the complete cap/side/closure contract
and derive its exact signed reduction. A separate cap-asymptotic lemma
may proceed in parallel, but it must state which geometry it covers.

## 8 Ownership and records

This home owns new LHCT execution only. The founding assessment remains
in [home 10][mass]; shared [physical boundary assembly][full] and
[BW12 transport][transport] keep their source status and paths. Home 10
retains CHB integral estimates; home 03 retains broader physical transport;
home 02 owns the canonical source. Parent I4-H01/H02 and inherited BW10/BW12
exclusion gates remain unchanged.

Save analytical derivations in notes/, supporting small computations in
numerics/, assessments in reviews/, and concise milestones in
[DRAFT_HISTORY.md](../DRAFT_HISTORY.md). This program creates no manuscript
snapshot. [History guidance](../chat-histories/README.md) preserves the
founding conversation's sole existing registration. The setup review is
internal LLM review, not independent specialist mathematical validation.

[progress]: ../research-progress/01_LATE_HEAT_CAPS_AND_CHARGE_TRANSPORT_PROGRESS_20261022.md
[assessment]: ../../10_chern_hopf_integral_estimates/notes/03_LATE_HEAT_PAIR_STATISTICS_AND_CAP_FLUX_20261022.md
[mass]: ../../10_chern_hopf_integral_estimates/README.md
[source]: ../../02_theta_source_constraints/README.md
[projective]: ../../notes/01_CHERN_HOPF_PROJECTIVE_SIDES_AND_LOCAL_SECTORS_20261022.md
[full]: ../../notes/03_COMPLETE_PHYSICAL_BOUNDARY_AND_CRITICAL_VALUE_WINDING_20261022.md
[transport]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/18_HEAT_EVOLUTION_AND_EARLY_LATE_TOPOLOGICAL_TRANSPORT_20261021.md
[saddle]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/20_DIFFERENTIATED_SADDLE_AND_EVENTUAL_GAP_SHRINKAGE_20261021.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md

## Execution checkpoint — 22 October 2026

[Note 01](../notes/01_FINITE_PROJECTIVE_TUBES_AND_COMPLETE_ATTACHMENTS_20261022.md) proves complete event-core attachments and finite projective tubes, then uses the new source theorem for fixed imaginary-width continuation over growing intervals with a frozen radius r_0/L_T. [Note 02](../notes/02_COMPLEX_TIME_THETA_JETS_AND_LATE_CAPS_20261022.md) proves normalized complex-time jets and the complete cap remainder gamma min(S_T D,b)/pi. Its fixed-width canonical cap tends to r_0^2Y/pi; its shrinking-width cap vanishes. [Note 03](../notes/03_FIXED_RANK_PAIR_CANCELLATION_AND_TUBE_CONTROLS_20261022.md) quantifies actual fixed-rank exterior-unit cancellation, so the optional statistical route is not needed for the cap theorem.

[Note 04](../notes/04_IMAGINARY_TIME_CLOSURE_CONCENTRATION_20261022.md) pays the complete closure allocation: in the shrinking-width family each imaginary-time face approaches half the event charge, while fixed-width tube faces cancel the nonzero cap limit. Geometry and this allocation cover every fixed finite candidate height and multiplicity with event-dependent constants. They exclude no candidate. The selected small-cap/zero-side exclusion payment is stopped in this class; a new opposing canonical signed estimate remains unpaid. [Internal review](../reviews/03_FINITE_TUBES_CAPS_AND_CLOSURES_INTERNAL_REVIEW_20261022.md); actual gpt-6-astra, ultra, for Edward Baker with substantial LLM assistance. The sole ledger retains detailed LHCT statuses.

## Linked zero-count follow-up

22 October 2026, for Edward Baker with substantial LLM assistance, **gpt-6-astra, ultra**. The user's later all-zero/PCC/RHE proposal is formalized in the new [ZTP overview](../research-overview/02_ZERO_COUNT_TRANSPORT_AND_PAIR_MATRIX_PROGRAM_20261022.md) and [ZTP progress note](../research-progress/02_ZERO_COUNT_TRANSPORT_AND_PAIR_MATRIX_PROGRESS_20261022.md). They add a fixed-rank matrix theorem and exact Hodge-count interface, without duplicating LHCT tasks or completing LHCT-05–07.

# Continuation prompt for topological integrals and RH estimates

22 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **ultra**, verified from this turn's metadata.

The user wants to determine whether the newly evaluated Chern/Hopf integral
can be transformed into useful bounds for the particular integrals relevant
to RH or to RH implying simplicity. Exact boundary simplification and
estimator improvements are valuable independently of proving noncollision.
The positive bulk mass and bounded-weight bounds are established locally;
their useful application to those target integrals remains the research task.

## Prompt for the new chat

Work in `/Users/ebbaker/Documents/shifted-zeta-positivity`, continuing
**CHB-07** in `papers/investigations-4/`. Read this handoff, then carry one
bounded comparison through to a proved estimate or a precisely scoped
failure. Begin with the actual target integrals and manipulate the new
formula toward them. Do not stop at another overview or at an equivalent
restatement of RH or simplicity.

Read repository `AGENTS.md`, `LARGE_FILES.md`, `tools/CHAT_HISTORY.md`, the
[result index][results] and [avoid index][avoid]. Then read the current
[CHB overview][overview], [task register][progress], [complete-boundary
Note 03][n3], [integral-bounds Note 04][n4] and [Review 05][review].
Notes 01–02 are background for chart primitives and the earlier punctured
sector; use the complete window of Note 03 for the enclosing charge.

The direct ancestors are BW10 `10_rh_implies_simple_zeros` and BW12
`12_relative_chern_hopf_charges`, both below
`papers/investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/`.
Read BW10 [Note 24 GA1–GA6][gauss] and [Note 25 MC6–MC9][mass] first;
consult [Note 21 MT7–MT10 and MT21][tubes] for the physical spatial-tube
target, and BW12 [Note 18][transport] for the complete signed boundary.
Source files prevail over summaries.

## Established formulas and their scope

Use the fixed physical jet frame and complex heat equation
\[
 H_\tau=-H_{zz},\qquad G=(H,H_z),\quad E=|H|^2+|H_z|^2,
 \quad J=H_zH_{zzz}-H_{zz}^{\,2}.
\]
For Note 03's local physical product window W with a nonvanishing boundary
jet and its single critical graph c(tau), the complete charge is
\[
 Q={1\over4\pi^2}\int_{\partial W}\mathcal A\wedge d\mathcal A
   ={1\over2\pi}\oint_{\partial D}d\arg V,
 \qquad V(\tau)=H(\tau,c(\tau)),\quad H_z(\tau,c(\tau))=0.
\]
All four heat faces and the outer spatial wall are retained. The wall
generally has nonzero flux; its separate integral cancels only in the full
assembly. The two projective chart pieces contribute kappa Q and
(1-kappa)Q. An ordinary double has Q=1. This evaluates the inherited
charge, equal locally to the existing discriminant winding; it introduces
no new arithmetic information by itself.

For delta>0 the positive four-dimensional measure is
\[
 d\mu_\delta=\left({i\over2\pi}\partial\bar\partial
                  \log(E+\delta^2)\right)^2
 = {2\delta^2|J|^2\over\pi^2(E+\delta^2)^3}\,dV.
\]
On a fixed paid window, Note 03's full boundary floor e_0, derivative
bound L and boundary three-volume S give
\[
 |\mu_\delta(W)-Q|\le B_\delta
 \le {SL^3\delta^2\over\pi^2 e_0^{5/2}},\qquad
 \left|\int_W w\,d\mu_\delta\right|
       \le\|w\|_\infty(Q+B_\delta).
\]
These are useful bounds for their specified density and bounded weights.
The unnormalized determinant integral retains its delta^(-2) cost.
Singular weights are not covered by an assumed finite norm. Weighted
Stokes retains the integral of dw wedge C_delta, and varying the window
requires tracking the resulting changes in e_0, L and S.

The exact existing Gauss-area interface is also available. With
\[
 D_z=HH_{zz}-H_z^2,\quad
 N_\delta=|D_z|^2+\delta^2(|H_z|^2+|H_{zz}|^2),\quad
 \gamma_\delta={N_\delta\over\pi(E+\delta^2)^2},
\]
\[
 s_\delta={\delta^2|J|^2\over(E+\delta^2)N_\delta},\qquad
 d\mu_\delta={2\over\pi}s_\delta\gamma_\delta\,dV.
\]
Here s_delta is the Schur complement of the spatial entry of the complex
Hessian of log(E+delta²); it retains the mixed heat/spatial curvature.
Note 04 gives an explicit s_delta>=c_delta>0 across its ordinary-double
window for each fixed delta, hence
\[
 \int_W\gamma_\delta\,dV\le {\pi\over2c_\delta}(Q+B_\delta).
\]
The inverse cost is order delta^(-2) for that fixed contract. This is a
complex-time area average, not a fixed-real-time spatial bound. At a
regular point with D_z and J nonzero, s_delta itself has order delta².
Merely changing notation cannot eliminate that degeneration.

## First bounded research task

Make a short inventory of the actual consumers before choosing the
transformation. For each, record its exact source formula, dimension,
domain, weight, sign or inequality direction, and the consequence a useful
bound would have. Distinguish an estimating gain from an exclusion margin.

| Candidate | Existing consumer and comparison required |
| --- | --- |
| Spatial Gauss area | BW10 GA1–GA6: compare with the existing GA3 spatial boundary formula and the finite concentration pi(m-1). Another finite bound alone is not new progress. |
| Physical tube or phase-cap integral | BW10 MT7–MT10/MT21: preserve the actual denominator, transverse faces, signs and trace errors; use its equally informed direct baseline. |
| Critical-wall amplitude budget | The [ICW program][icw] and [shared theta-source home][source] identify the signed C_2-k C_0 moment estimate, with S_1=0. A bulk bound needs a proved trace/denominator comparison before it controls that real-time budget. |
| Complete signed endpoint response | BW12 [Note 15][covariance] supplies the direct canonical covariance baseline. A comparison must retain its mixed head–tail term, cubic remainder and endpoint geometry. |

Default to the **Gauss-area comparison**, since its exact bridge is already
known, unless the inventory identifies a more direct named consumer. Keep
one primary candidate. RH's full Weil form is a possible later consumer
only after an explicit transform identity or inequality relates it to this
jet measure; a shared topological interpretation supplies no such bridge.

First reproduce the direct regularized Green formula and its bound using
the same constants from Notes 03–04:
\[
 \int_\Omega\gamma_\delta\,dA_z
   ={1\over4\pi}\int_{\partial\Omega}
                         \partial_n\log(E+\delta^2)\,ds,
 \qquad
 \int_W\gamma_\delta\,dV
   \le {4TYR\epsilon_1(M_0+D_2)\over m_*^2+\delta^2}.
\]
Here |H|<=M_0, |H_z|<=epsilon_1, |H_zz|<=D_2 and E>=m_*² on the
spatial wall; |partial_n E|<=2epsilon_1(M_0+D_2) supplies the bound.
It stays finite as delta tends to zero on the fixed paid window. The
existing inverse-Schur estimate therefore is not already a better bound
for this unweighted averaged target. This baseline is the first calibration,
not a reason to discard weighted, localized or signed target comparisons.

A direct identity also connects the Gauss density to the amplitude target.
On H!=0 put p=H_z/H. Then
\[
 g_2={|p_z|^2\over(1+|p|^2)^2}.
\]
On the actual real critical wall p=0, the ICW quantity is
q=-H_zz/H=-p_z, so g_2=q² there. This identity does not supply a trace
bound from complex spacetime to that moving real curve, preserve the sign
needed for the q budget, or justify its singular endpoint limit. Those are
the precise missing estimates if this connection is selected.

1. Try a justified weight or normalization, integration over selected
   fibers, localization around the event, logarithmic-derivative coordinates,
   or integration by parts that preserves the complete signed expression.
   These are candidate manipulations, not established gains. Display the
   resulting equality or inequality with every new remainder and constant.
2. Determine whether the complete comparison controls the inverse Schur
   cost, or whether a suitable finite delta gives a useful target bound
   without taking delta to zero. Account for the regularization bias and
   any cost of recovering a fixed-time trace from the complex-time average.
3. Compare with the strongest direct method using the same moments,
   critical-value data, geometry and source errors. A gain may be a smaller
   bound, stricter signed enclosure, or simpler evaluation with a proved
   cost advantage. A dimension reduction already established in Notes 03–04
   is not a new comparison result.
4. Finish one analytic candidate before launching theta numerics. If it
   fails, state the precise class and obstruction, retain the independent
   bounded-mass result, and identify the additional inequality needed.

The positive mass could control a negative or error term in a complete
signed target; the whole target need not equal that density. Exhibit the
actual signed decomposition. A formal quotient chosen to make the
integrands match must pay any zeros of J, singular weights and delta costs.

Use the unchanged canonical source and full reflection when a theta-specific
premise is needed. Retain simultaneous value/jet matching, complete mode/ray
tails, wall and chart uncertainty, and rounding. Reference home 02's existing
source ledger rather than inventing a second source model. A conditional
event chart is not an acquired theta event or a uniform all-height theorem.

## Controls and conclusions that remain separate

Apply the [collision-control register][controls], [matched-premise rule][a02],
[target classification][a01], [coupled-estimate rule][a12], [full-target
rule][a13] and [scope rule][a07]. In particular:

- H=z has positive spatial Gauss density but J=0 and zero bulk mass.
  It rules out generic domination across all heat fields, not a new
  canonical-theta inequality with additional hypotheses.
- H=z²-2tau retains a collision, complete charge one and the local formulas.
  A claimed exclusion must identify an additional premise it fails.
- Note 03's quartic has exterior neighbors and a separating contour while
  two simple zeros merge and the spatial multiplicity count stays two.
  Conserved total multiplicity is not conserved simplicity.

For an exclusion, the needed step is an independently proved bound
incompatible with positive collision charge, or the exact signed/singular
budget required by the selected consumer. Do not assume Q=0 or an unknown
endpoint gap/floor. If using RH, state exactly where the all-real hypothesis
enters; RH does not supply simplicity. Ordinary-double estimates do not
settle higher multiplicities or all heights.

The current integral argument uses relative degree, Chern–Weil/Hopf forms
and Stokes. An Atiyah–Singer route is optional and separate: it must specify
an elliptic operator, its symbol/Fredholm domain, the exact density bridge
and all boundary corrections. See Note 04's primary AS/APS references.
An operator's heat-kernel time is not the physical heat parameter tau.

## Deliverables and research history

Save the target inventory and first completed comparison in the shared
`papers/investigations-4/notes/` folder, using the next unused number.
Keep relevant checks in home 03's `numerics/` and assessments in `reviews/`;
source-specific results may live in home 02 with cross-links. Update the
existing CHB overview and progress register in place. CHB-04 remains complete
in its conditional local scope; CHB-05 acquisition is unperformed, CHB-07
is active, and the inherited BW10/BW12 exclusion gates are unchanged.
Include Edward Baker, LLM assistance and the new chat's actual model/effort.
Use DRAFT_HISTORY.md only for concise milestones; create no manuscript
snapshots or duplicate progress ledgers.

Register or refresh the **new chat's actual identity and title** in
`papers/investigations-4/chat-histories/` using the authorized history tool.
This handoff originates in chat 0007, thread
`01a161d8-6f5b-7991-8513-f90ebb977c0c`; preserve that archive and do not use
its identity for the new chat. Let the tool assign the new number. Follow
the standing start/end refresh and bounded exact-turn final capture.

Finish the first research round with the exact comparison obtained, its
usefulness and limits, the control/review outcome, updated task status,
links to saved work and the next genuinely unpaid estimate.

[overview]: ../research-overview/03_CHERN_HOPF_BOUNDARY_SIMPLIFICATION_PROGRAM_20261022.md
[progress]: ../research-progress/03_CHERN_HOPF_BOUNDARY_SIMPLIFICATION_PLAN_AND_PROGRESS_20261022.md
[n3]: ../notes/03_COMPLETE_PHYSICAL_BOUNDARY_AND_CRITICAL_VALUE_WINDING_20261022.md
[n4]: ../notes/04_TOPOLOGICAL_MASS_BOUNDS_AND_INDEX_THEOREM_INTERFACE_20261022.md
[review]: ../03_heat_transport_and_charges/reviews/05_COMPLETE_BOUNDARY_AND_INTEGRAL_BOUNDS_REVIEW_20261022.md
[icw]: ../research-overview/02_INTERIOR_CURRENT_BOUNDARIES_AND_BACKWARD_SURVIVAL_PROGRAM_20261022.md
[source]: ../02_theta_source_constraints/README.md
[gauss]: ../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/24_GAUSS_AREA_CONCENTRATION_AND_CURVATURE_FLUX_20261021.md
[mass]: ../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/25_MULTIPLICITY_SELECTIVE_CHERN_AND_HOPF_OBSERVATIONS_20261021.md
[tubes]: ../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/21_MOVING_SIGNED_TUBES_AND_PHYSICAL_TRACE_20261021.md
[transport]: ../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/18_HEAT_EVOLUTION_AND_EARLY_LATE_TOPOLOGICAL_TRANSPORT_20261021.md
[covariance]: ../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/15_CANONICAL_COVARIANCE_SIGNED_ENCLOSURE_20261021.md
[results]: ../../../result-summaries/README.md
[controls]: ../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../avoid/README.md
[a01]: ../../../avoid/01_restating_the_target.md
[a02]: ../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a13]: ../../../avoid/13_a_factor_is_not_the_target.md

# Chern/Hopf integral estimates: research program

Home established 22 October 2026 at Edward Baker's request, with substantial LLM assistance; actual recorded **gpt-6.1-sol (Codex), effort ultra**, verified from this turn's metadata. This is the sole current CHB program. Earlier derivations, task IDs, statuses and authoring provenance are retained. The [local synthesis](../notes/01_ESTABLISHED_MASS_TRACE_AND_AMPLITUDE_RESULTS_20261022.md) writes up the results; retained shared notes remain authoritative detailed sources.

**Original opening-turn provenance (retained from the source):**
22 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **ultra**, verified from this turn's metadata.

**Purpose:** remove specified boundary terms and simplify the remaining
integrals in the Chern/Hopf formulas inherited from BW10 and BW12, and use
their evaluated topological mass to bound named analytic integrals. Exact
integral reduction is a useful research outcome independently of proving
noncollision. A theta-specific exclusion, if later obtained, is a separate
conclusion requiring its own complete signed estimate.

**Current status: complete local boundary assembly and mass estimates;
CHB-07 Gauss comparison and critical-wall trace/endpoint follow-up proved
in-note in their specified local scope.** The full
boundary integral reduces to one critical-value winding. [Note 05][note5]
pays the Gauss-area regulator bias and proves that Note 04's global
inverse-Schur certificate loses to the direct spatial Green certificate
for every finite regulator on Note 03's sufficient window. The
[critical-wall follow-up][note6] pays spatial and complex-time traces,
regulator bias and bounded signed endpoint remainders. Its specified
local-Schur/total-mass certificate also loses to direct critical-value
estimation. [Local Note 02][coupled] now proves coupled signed tail
enclosures and interval-certifies strict same-moment gains at one regular
canonical critical point; added direct signed quadrature is much sharper
in that pilot. A global arithmetic signed improvement, complete phase/flux
acquisition and exclusion margins remain open. There has been no specialist review or
formal analytic verification.

CHB-07 continuation, 22 October 2026: prepared for Edward Baker with
substantial LLM assistance; actual recorded **gpt-6.1-sol (Codex), effort
ultra**, verified from this continuation's active turn metadata. Earlier
entries retain their original provenance.

The [corresponding plan and progress register][plan] owns CHB task IDs.
This continues the complex-form branch of [ICW-07][icw], alongside its
already completed real-phase reduction; it does not replace ICW's backward-
survival research or complete the parent I4-H01 quantitative estimate.

## 1. Sources and exact target

Read the [result index][results] and [avoid index][avoid], specifically
[heat geometry][geometry], [collision controls][controls], [target
classification][a01], [scope][a07], [coupled information][a12] and
[geometric comparisons][a03]. The direct research ancestors are:

- **BW10 `10_rh_implies_simple_zeros`:** [MC6–MC9][bw10] supply the
  multiplicity-selective Chern/Hopf observation and its regularization.
  [Moving signed tubes][tubes] motivate removing boundary terms, but their
  real-phase identities are not the complex three-form identity.
- **BW12 `12_relative_chern_hopf_charges`:** [Note 17][connection] fixes
  the jet connection, and [Note 18, formula (11)][bw12] retains all physical
  heat and spatial faces in the charge-transport identity.

For a holomorphic heat field H_tau=-H_zz, use the physical frame
\[
 G=(H,H_z),\quad E=|H|^2+|H_z|^2,\quad g=G/\sqrt E,\quad
 \mathcal A=-ig^*dg,\quad \mathcal F=d\mathcal A,\quad
 \mathcal C={\mathcal A\wedge\mathcal F\over4\pi^2}.
\]
For a proper four-dimensional complex-spacetime window with nonvanishing
boundary jet and isolated interior events, the inherited complete boundary
integral counts their weights binom(m,2). The present research changes how
that integral is evaluated, not its event weights. Arbitrary frame changes,
chart seams and singular shrinking caps cannot be discarded.

## 2. What the local and complete-boundary work establishes

[Shared Note 01][note1] proves the ratio-chart identity on H!=0,
\[
 p=H_z/H,\quad \eta=\operatorname{Im}(dH/H),\quad
 a_p={\operatorname{Im}(\bar p\,dp)\over1+|p|^2},\qquad
 \mathcal C=d\!\left(-{\eta\wedge a_p\over4\pi^2}\right).
\]
A three-face whose projective image lies in a fixed real curve in CP^1
has zero curvature pullback and hence zero Chern/Hopf contribution. In
particular a regular |p|=P side cancels. A single complex equation p=c
has the wrong dimension to be that side. The second chart retains an
integer-valued corner seam; a full charged boundary cannot be placed
silently in the H!=0 chart.

At an ordinary double H=H_z=0, H_zz!=0, G is locally biholomorphic.
A specified radial jet sector has cap values +kappa and -kappa and side
zero, with kappa=P²/(1+P²). Note 01 supplies an explicit inverse-chart
radius from event jets and complete moments, a regularization error, and
the noncommuting puncture/regularization limits. Its caps are radial,
not physical heat-time slices.

[Shared Note 02][note2] constructs an actual physical-time sector using
H_z(tau,z(tau,p))=pH(tau,z(tau,p)). On a sufficiently small product chart,
H(tau,z(tau,p))=tau B(tau,p) with B nonzero. Every oriented heat-edge face
then satisfies
\[
 \boxed{\displaystyle
 \int_{e\times D_P}\mathcal C
 = {\kappa\over2\pi}\Delta_e\arg V,
 \qquad V(\tau)=H(\tau,z(\tau,0)),\quad V'=-H_{zz}.}
\]
The mean-value property in p removes the apparent endpoint disk integrals.
A quantitative contraction contract certifies the entire graph when its
source inputs are supplied; critical-wall values alone do not certify it.
All four heat faces, the puncture face and the cancelling projective side
are accounted for. For a rectangle enclosing zero the outer sum is kappa
and the inner contribution -kappa. The limiting event is a boundary apex,
not an enclosed fractional-charge event. [Shared Note 03][note3] resolves
the enclosing-window task by splitting the full boundary into two charts,
without splitting or puncturing its interior. Their contributions are
kappa n and (1-kappa)n, where
\[
 Q=\int_{\partial W}\mathcal C
   ={1\over2\pi}\oint_{\partial D}d\arg V=n.
\]
All four heat faces and the outer spatial wall are retained; the wall
generally has nonzero flux, but its separate integral cancels in the full
assembly. The note supplies an explicit conditional ordinary-double
window, a complete boundary jet floor and regulator allowance B_delta.
This evaluates the inherited charge; it is not a new invariant.

[Shared Note 04][note4] makes the user's integral-bounding objective
concrete. The positive regularized bulk measure mu_delta obeys
|mu_delta(W)-Q|<=B_delta=O(delta²) for a fixed paid window. Hence
|integral w dmu_delta|<=||w||_infinity(Q+B_delta). Its exact comparison to
BW10's spatial Gauss area includes a Schur complement and an inverse cost
of order delta^(-2). The constants are paid across the window for fixed
delta; a useful limiting or fixed-time bound still needs another estimate.
No elliptic operator/index realization is constructed: Atiyah–Singer/APS
would require a separate operator, density and boundary contract.

Conservation of total spatial multiplicity does not imply simplicity.
Note 03's quartic heat control keeps a contour between inner and outer
zeros while an interior double forms and the enclosed count stays two.
The full complex-spacetime collision charge is instead one. This scopes
the moving-contour proposal without ruling out theta-specific estimates.

## 3. Research plan and success criteria

The detailed task sequence and current evidence are in [the plan][plan].
CHB-04's local enclosing-window assembly is complete. CHB-07's first
bounded comparison is complete in [Note 05][note5]: the global inverse-Schur
certificate is at least (5242880 pi/23273)(D_2/h)^4 times the direct
unregularized Green certificate, for every delta>0 on the sufficient window.
This compares upper certificates, not lower bounds on the actual area.
The direct regulator allowance is explicit and returns the original direct
certificate exactly when added to its regularized bound. Stop optimizing
delta in that implementation. The next estimating candidate must use
localized/weighted or complete-source information for a named consumer,
with the same-information direct comparator. This proceeds independently
of noncollision. CHB-05 now has a
complete-window analytic contract, but actual theta acquisition remains
unperformed for that complete phase/flux task. The later CHB-07 regular
critical-point acquisition is distinct. Reuse BW12's existing proper-window and discriminant results;
the critical-value reduction adds no new topological information.

For each candidate, record:

1. The actual domain and all its oriented faces, nonvanishing conditions,
   fixed frame, chart transitions and order of limits.
2. The specific term removed, the exact remaining formula and the data
   needed to evaluate it, including continuous phase branches.
3. Source acquisition: unchanged canonical coefficients, simultaneous
   moment observations, complete tails, chart and derivative errors,
   quadrature and rounding. A parameterized theorem is distinct from
   an executed theta certificate.
4. The direct comparator given the same chart, source data and errors.
   A structural dimension reduction is already useful; an error or cost
   advantage must be measured against that equally informed comparator.
5. The quadratic collision control and the other [catalogued controls][controls]
   within their actual hypotheses. A simplification may correctly retain
   collisions. An exclusion must identify a genuinely additional premise.

Do not extend the ordinary-double inverse/implicit chart to H_zz=0, delete
a shrinking inner face, use endpoint principal arguments as a phase lift,
or apply the unregularized phase formula to finite regularization without
its amplitude correction. The source estimate required for noncollision
is not obtained by naming a conserved charge or restating a phase ratio.

The [continuation prompt][integral-continuation] led to Note 05's inventory
of spatial Gauss area, physical tubes, critical-wall amplitude and complete
endpoint response. The first Gauss comparison is now decided for its
specified estimator class. The g_2=q² critical-wall identity is continued
in Note 06 below, with trace and endpoint costs paid in the conditional
local scope. Bounded mass remains useful independently; no new arithmetic
exclusion margin is established.

**Critical-wall follow-up, 22 October 2026 — [Note 06][note6].** The sharp
spatial trace is q²<=(1+P²)A/(pi r²), with the zero-free/range assumptions
paid from the critical value. A complete shrinking complex tube gives
|q|<=C_top/t from the positive mass, including its real-curve trace and
regulator costs. Its specified local-Schur/total-mass coefficient is at
least (48 sqrt(2)/37)(D_2/h) times the direct D_2/b coefficient, so that
implementation supplies no improvement. This does not close estimates using
sharper localized mass or additional source correlations.

The useful signed output is the explicitly bounded cancellation
C_2-C_0/t=tB', |tB'|<=K_0t, and q=1/t+B'/B with |B'/B|<=K_0/b.
A signed center r_0=(C_2C_4+S_3²)/(2C_2²), evaluated at the conditional
event, has an explicit O(t) remainder. It preserves logarithmic coefficient
one. Its actual theta sign, an improved complete consumer and any exclusion
margin are unpaid. [Review 07][review7] checks the local derivation; this
continuation uses the recorded gpt-6.1-sol, ultra configuration above.

**Coupled signed acquisition, 22 October 2026 — [local Note 02][coupled].**
Simultaneously using C_0=V and S_1=0 gives one-sided complete tail intervals
with exact-data width factors 4/5 and 3/7 against specified same-moment
cosine-Taylor bounds. One actual regular canonical critical point and strict
complete endpoint gains are interval-certified. The added direct signed
tail integral is far sharper in that pilot, so this is a shared direct
acquisition refinement, not a comparative topological advantage. The
universal inequalities retain the positive-source collision controls.
The next unpaid estimate concerns additional arithmetic control of the
complete conditional quadratic or a named residual as height grows;
certifying the known Laguerre sign in an all-real regime does not pay it.
[Internal review][coupled-review] and [receipt][coupled-checks].

## 4. Ownership and records

The retained detailed derivations stay in the user-authorized [I4 notes
folder][notes], with their existing home 03 reviews/check records and
hash-bound paths. New focused derivations belong in this home's
[notes][local-notes], computations in numerics/, and assessments in reviews/.
Source payments reuse home 02 and the existing ICW ledger;
there is no second canonical-source history. Update this overview and the
plan in place. The [portfolio register][parent] carries only a summary;
BW10 HMC-05's separating estimate, HMC-06 and BW12 FTSR-06/07 retain their
existing open/gated states. None is completed by this local reduction.

[Review 04][review] covers the opening reductions; [Review 05][review5]
covers the full assembly, weighted estimates and comparison controls.
They are contributing-agent same-model checks with their limits explicit.
[Review 06][review6] checks the new target comparison and its scope.
Originating archive [0007][chat] is preserved; this separate continuation
has its own actual identity and title in archive [0008][chat8]. Follow the
[history workflow][history] and [large-file policy][large]. The milestone
belongs in DRAFT_HISTORY.md; create no draft manuscript snapshot.

[plan]: ../research-progress/01_CHERN_HOPF_INTEGRAL_ESTIMATION_PROGRESS_20261022.md
[note1]: ../../notes/01_CHERN_HOPF_PROJECTIVE_SIDES_AND_LOCAL_SECTORS_20261022.md
[note2]: ../../notes/02_CHERN_HOPF_PHYSICAL_TIME_SECTOR_REDUCTION_20261022.md
[notes]: ../../notes/README.md
[review]: ../../03_heat_transport_and_charges/reviews/04_CHERN_HOPF_BOUNDARY_OPENING_REVIEW_20261022.md
[icw]: ../../research-progress/02_INTERIOR_CURRENT_BOUNDARIES_AND_BACKWARD_SURVIVAL_PROGRESS_20261022.md
[parent]: ../../research-progress/01_COMPACT_GEOMETRY_HEAT_TRANSPORT_AND_WEIL_POSITIVITY_PROGRESS_20261021.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a03]: ../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[bw10]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/25_MULTIPLICITY_SELECTIVE_CHERN_AND_HOPF_OBSERVATIONS_20261021.md
[tubes]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/21_MOVING_SIGNED_TUBES_AND_PHYSICAL_TRACE_20261021.md
[connection]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/17_PARALLEL_TRANSPORT_CONNECTIONS_AND_COLLISION_CONTROLS_20261021.md
[bw12]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/12_relative_chern_hopf_charges/notes/18_HEAT_EVOLUTION_AND_EARLY_LATE_TOPOLOGICAL_TRANSPORT_20261021.md
[chat]: ../../chat-histories/0007_2026-10-22T04-22-16Z_begin-interior-boundaries-research.json
[history]: ../../../../tools/CHAT_HISTORY.md
[large]: ../../../../LARGE_FILES.md
[note3]: ../../notes/03_COMPLETE_PHYSICAL_BOUNDARY_AND_CRITICAL_VALUE_WINDING_20261022.md
[note4]: ../../notes/04_TOPOLOGICAL_MASS_BOUNDS_AND_INDEX_THEOREM_INTERFACE_20261022.md
[review5]: ../../03_heat_transport_and_charges/reviews/05_COMPLETE_BOUNDARY_AND_INTEGRAL_BOUNDS_REVIEW_20261022.md
[integral-continuation]: ../../brainstorm/04_CONTINUATION_PROMPT_TOPOLOGICAL_INTEGRALS_AND_RH_ESTIMATES_20261022.md
[note5]: ../../notes/05_TARGET_INVENTORY_AND_FINITE_REGULATOR_GAUSS_COMPARISON_20261022.md
[review6]: ../../03_heat_transport_and_charges/reviews/06_FINITE_REGULATOR_GAUSS_COMPARISON_REVIEW_20261022.md
[chat8]: ../chat-histories/0008_2026-10-22T12-59-44Z_relate-topological-integrals-to-rh-estimates.json
[note6]: ../../notes/06_CRITICAL_WALL_TRACES_AND_SIGNED_ENDPOINT_BUDGET_20261022.md
[review7]: ../../03_heat_transport_and_charges/reviews/07_CRITICAL_WALL_TRACE_AND_ENDPOINT_BUDGET_REVIEW_20261022.md
[local-notes]: ../notes/README.md
[coupled]: ../notes/02_COUPLED_SIGNED_THETA_TAIL_ESTIMATES_20261022.md
[coupled-review]: ../reviews/02_COUPLED_SIGNED_TAIL_REVIEW_20261022.md
[coupled-checks]: ../numerics/COUPLED_SIGNED_TAIL_CERTIFICATE_20261022.json

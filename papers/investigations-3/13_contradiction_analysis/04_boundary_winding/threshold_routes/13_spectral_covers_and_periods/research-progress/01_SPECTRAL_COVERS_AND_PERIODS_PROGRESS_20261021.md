# Spectral covers and periods research progress

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**, verified from this turn's metadata.

## Current status — first research round, 21 October 2026

[Note 01][n01] fixes a finite nodal period, derives its variation and
complete-source remainder, and identifies the first post-quadratic
coefficient:
\[
 \kappa=\frac{5h_3^2-3h_2h_4}{48h_2^2}
        =\frac38S_2+\frac{h_3^2}{16h_2^2}.
\]
It is exactly a function of the event four-jet, including the existing
BW-08 deflated invariant. The comparison using only that same four-jet
is stopped: it supplies no smaller admissible coefficient set, and
positivity of the coefficient occurs in an even polynomial with double
endpoints and simple all-real zeros at every positive time.

**Status: local analytic derivation, proved in-note; same-assistant
self-review only.** Complete theta moment/tail bounds are explicit but
unacquired. No numerical theta pilot, independent review, event exclusion,
or global estimate has been completed. Finite non-asymptotic periods and
different source estimates remain open.

## Inherited evidence

| Evidence | Source and status | Consequence |
| --- | --- | --- |
| Fiber germ w²=(z−a)^m and Milnor number m−1 | Analytic C2–C3 screen; same-assistant assessment. | Multiplicity detection is not exclusion. |
| Double-event periods −2pi i and 2pi i t | Exact C4 calculation with specified orientation. | A collapsing cycle can retain a period if its differential becomes singular. |
| Finite exhaustion genus N−1 | C5 with simple branches and regular boundary. | No finite global genus budget is available. |
| Total-space singularity at higher order | Proposal Section 4. | Higher multiplicities need separate resolution or singularity treatment. |

These are inherited calculations, not newly reviewed results.

## Task register

| ID | Status | Completion evidence required |
| --- | --- | --- |
| SCP-00 | Complete as program setup | Object, normalization, controls and bounded objective recorded. |
| SCP-01 | Complete for the local double-event pilot | Note 01 §§1–2: explicit finite disk/time range, fixed regular boundary, transported cycle, branch and differential, with unique critical time. |
| SCP-02 | Complete analytically for that local pilot | Note 01 §§2–3: quadratic baseline, four-jet correction, moving-endpoint accounting, sixth-moment remainder and complete source-tail interface. No evaluated theta data. |
| SCP-03 | First-coefficient comparison complete; broader acquisition comparison open | Note 01 §§4–6: exact same-four-jet information equality and positive-correction collision control. Direct error and finite-period extraction errors explicit. No theta cost or coverage gain measured. |
| SCP-04 | Gated on useful finite evidence | Higher-multiplicity and height coverage with justified resolution and period space. |

## Deliverables and next decision

- [Note 01][n01]: the finite domain, period, source tails, inherited BW-08
  interface, coefficient comparison and precise stop.
- [Self-review][review01]: normalization, regularity, transport, remainder,
  control scope and outstanding limitations; by the same assistant.
- [Checker][checker] and [receipt][receipt]: seven exact rational polynomial
  cases and fourteen floating contour diagnostics, with no theta
  integration or interval certification.
- [Milestone history][draft-history] and [route chat history][route-history].

The next research step must specify an estimate outside the same-four-jet
coefficient class: for example a finite-time period or a relation between
cycles whose source correlations can actually be bounded. Set its paid
error/coverage/cost comparator before acquiring theta data. Compare direct
use of that same added information, not a deliberately weaker direct
baseline. Additional coefficient tables alone do not discharge this step.

SCP-04 remains gated: no higher-multiplicity resolution, finite global
period system, or height exhaustion follows from this nodal calculation.

## Continuation and provenance

Use the [result index][results], [local geometry summary][local],
[control register][controls] and [avoid index][avoid], particularly
[classification][a01], [lifts][a03] and [scope][a07]. Compact Jensen
topology does not supply a finite budget for this noncompact cover.

The opening is recorded in [the boundary-winding chat archive][history].
This research round is registered in [the route archive][route-history].
Each later entry must state its domain, cycle, orientation, parameter
dependence, complete remainder and review status.
[HMC-05 remains open and HMC-06 gated][hmc].

[n01]: ../notes/01_NODAL_PERIOD_VARIATION_AND_FOUR_JET_COMPARISON_20261021.md
[review01]: ../reviews/01_NODAL_PERIOD_SELF_REVIEW_20261021.md
[checker]: ../numerics/check_nodal_period.py
[receipt]: ../numerics/NODAL_PERIOD_CHECK_20261021.json
[draft-history]: ../DRAFT_HISTORY.md
[route-history]: ../chat-histories/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a03]: ../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[avoid]: ../../../../../../../avoid/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[history]: ../../../chat-histories/0008_2026-10-21T16-44-53Z_create-proposal-research-folders.json
[hmc]: ../../10_rh_implies_simple_zeros/research-progress/02_HEAT_ROOT_MOTION_AND_SIGNED_CONTOURS_PROGRESS_20261021.md
[local]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[overview]: ../research-overview/01_SPECTRAL_COVERS_AND_PERIODS_PROGRAM_20261021.md
[proposals]: ../../10_rh_implies_simple_zeros/brainstorm/04_GLOBAL_HEAT_GEOMETRY_PROPOSALS_AND_INITIAL_SCREENS_20261021.md
[results]: ../../../../../../../result-summaries/README.md

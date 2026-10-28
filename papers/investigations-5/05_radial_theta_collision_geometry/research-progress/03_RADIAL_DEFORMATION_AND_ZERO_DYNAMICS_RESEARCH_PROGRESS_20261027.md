# Research progress on radial integrand preservation and collision localization

27 October 2026, America/New_York. Rewritten for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Investigation05 chat0007, **Explore collision-localizing deforms**.

**This is the authoritative progress register for the revised localization program.** The [overview][overview] makes preservation of the complete radial integrand the sole required invariant and auxiliary localization dynamics the first research priority. Existing constructions are foundations; the new LOC tasks below remain open. Rewriting the plan does not complete those tasks.

## Current position

The [manuscript][manuscript], Sections 9–10, and [Note20][n20] establish explicit finite-parameter flows that concentrate angular contributions while retaining the full radial density, a complete conjugated equation and boundary map, and a representation of \((H,H_z)\) near a radius-dependent curve. These are elementary constructions proved by direct calculation with same-assistant checking, as recorded in [Review12][review12].

The missing step is a complete localized comparison or a new auxiliary evolution whose controlled behavior yields information about the collision conditions. No signed tube estimate distinguishing theta, global projected-flow realization, all-height bound or positive-threshold contradiction has been established.

## Available results and their scope

| Foundation | Recorded status and domain | What remains outside it |
| --- | --- | --- |
| Radial integrand invariant and Laplacian projection | Pointwise spherical averaging and \(P\Delta=\Delta_3P\), with smooth-shell and compact-potential examples; manuscript Section 9 | A classification of all density-preserving equations or factorizations |
| Normalized angular ODE and transport PDE | Explicit smooth solutions for finite auxiliary parameter; normalization and cap formulas in Note20 | An infinite-concentration operator limit or a useful signed response estimate |
| Complete multiplicative realization | Explicit transformed operator, source, selected response, inverse and boundary map for the stated positive profiles | A general nonmultiplicative response construction or an unspecified homogeneous spectral theorem |
| Collision-adapted angular moment | Exact multiple of \((H(T,a_*),bH_z(T,a_*),0)\); finite weighted leakage bound for fixed \(a_*,b\) | All-height derivative bounds, higher-jet classification, or exclusion from a zero vector moment |
| Localization costs | Exact ordinary square-norm factor \(s\coth s\); induced energy pulls back to the original identity | A prohibition on other signed local estimates or other deformation classes |
| Projected annular Laplacian proposal | Preservation of zero spherical average and energy dissipation, conditional on a smooth solution of the stated bounded problem; [Brainstorm02][b02] | Established existence/regularity, smooth radial joins, full response map or a collision-sensitive objective |
| Darboux family and local node laws | Earlier proved identities and local corollaries in [Notes17][n17] and [18][n18], assessed in [Review11][review11] | Complete interior-node classification or an unqualified correspondence between interior nodes and physical collisions |

The explicit constructions preserve their controls' collisions. The [existing analytic screen][b01] identifies the canonical premises those controls lack; [Review12][review12] records that the numerical control certificates were not rerun. This program rewrite adds no new mathematical result or numerical certificate.

## Active task ledger

| ID | Priority and current state | Next deliverable | Completion evidence |
| --- | --- | --- | --- |
| LOC-01 | Supporting task; explicit examples available, broader theory open | Derive the density, response and boundary maps for any additional family actually needed by LOC-02 or LOC-03 | Proof on a stated parameter/function domain with all parameter derivatives and boundary terms |
| LOC-02 | **Immediate task; complete tube calculation not started** | Use the steered finite-width tube to derive a full signed identity and compare it with the radial calculation | A complete comparison with quantified costs, a new controlled structural consequence, or a scoped obstruction; the cap formula alone is insufficient |
| LOC-03 | Early complementary route; proposed bounded PDE only | Establish the annular evolution and its dissipation, then derive the response variation and a relevant objective | Well-posedness and regularity at a stated scope; boundary/join accounting before any global claim |
| LOC-04 | Open; no separating theta estimate selected | Use the fixed canonical source in a signed estimate or compatibility relation identified by the preceding work | An actual proved bound or relation and an explicit premise/estimate screen on colliding controls |
| LOC-05 | Later application; no new transfer result | Connect an adequate localized theorem to the existing positive-threshold finite-event reduction | Required time, height, multiplicity and tail coverage, or a precise remaining gap |

The [overview][overview] defines these tasks. LOC identifiers are new tracking entries; no previous RDZ result is being counted again as a completed LOC task. A full classification under LOC-01 is not required before the bounded LOC-02 calculation begins.

## Next session

Read manuscript Sections 9–10, Note20, Review12 and Brainstorm02. Then carry out the overview's bounded LOC-02 package: fix finite parameters and a radial annulus, derive the Green identity for the steered response and its spectral derivative on the angular tube, and keep lateral flux, both radial faces, drift, potential and steering derivatives.

Reconnect the calculation to the complete observation with the omitted angular and radial contributions included. Compare it with the one-dimensional identity using the same source information. Test the exact Gaussian-polynomial collision during the calculation. The useful return is an assessed comparison or structural conclusion, not another statement that angular normalization preserves \(H\).

If the complete comparison only transports the known cancellation, record that result for the tested class and develop LOC-03's specified projected flow. Neither branch requires a singular concentration limit or a broad numerical scan as its first step. New computations should have a defined analytic role.

## Disposition of the earlier RDZ tasks

The [earlier proposal][proposal] retains the original meanings of RDZ-01 through RDZ-08. Its priority order is superseded, while its results and open questions remain available.

| Earlier task | Status retained at the rewrite | Role in the revised program |
| --- | --- | --- |
| RDZ-01 to RDZ-03 | Initial Darboux family, evolution laws and simple-node formulas available; proposed full structural/nodal package unstarted | Optional supporting branch when a specific localization question needs it; no prerequisite status |
| RDZ-04 | Explicit angular extension established by Note20; broader extension/composition study open | Foundation for LOC-01 and LOC-02, not completion of a general classification |
| RDZ-05 | Transported ordinary energy and invariant pairing known; further structural constraints open | Comparison input for LOC-02; pointwise radial preservation needs the recorded Darboux density correction |
| RDZ-06 and RDZ-07 | No new canonical distinction or positive-threshold transfer established | Application questions now organized under LOC-04 and LOC-05 |
| RDZ-08 | Reviews11–12 and build records available; continuing verification | Verification remains part of every new return, not a one-time completed research claim |

RTC and RLC progress registers remain historical records. The [flux/moment result][n16], earlier controls and earlier representation results keep their original scope.

## Recorded milestones

| Date | Return | Status and provenance |
| --- | --- | --- |
| 27 October 2026, chat0006 | Initial Darboux manuscript and deformation/zero-dynamics program | Notes17–19, Review11 and [build record12][build12]; broader RDZ tasks were not completed |
| 27 October 2026, chat0007 | Sole radial-integrand invariant and auxiliary angular flows integrated into the manuscript | Note20, Brainstorms01–02, Review12 and [build record13][build13]; exact finite-parameter constructions with same-assistant checks |
| 27 October 2026, chat0007 | Overview and progress rewritten around collision localization at Edward Baker's request | Research priorities and navigation revised; LOC-02 selected as the bounded next calculation, LOC-03 retained as an early complementary route; no additional theorem claimed |

The current conversation keeps its unique **chat0007** registration in the [history registry][history]. Earlier chat0006 provenance is preserved. [DRAFT_HISTORY.md][draft] records concise milestones without manuscript snapshots.

## Recording future progress

For each return, record its date, actual model/effort, statement, domain, supporting note, assessment, control behavior and remaining gap. Keep a proposed flow, a conditional identity, a proved evolution theorem, a quantitative comparison and a physical exclusion distinct. State negative results for their tested class.

Consult the [result index][results] and [avoid index][avoid], especially [collision controls][controls], [target classification][a01], [transported identities][a03] and [scoped exclusions][a07]. Use the repository's existing screening rule: a finite certificate may pass a collision-free control box; a claimed exclusion must fail on a relevant domain containing its collision. Generic localization results need not exclude controls, but a theta separation must demonstrate the extra effect it uses.

[overview]: ../research-overview/03_RADIAL_DEFORMATION_AND_ZERO_DYNAMICS_RESEARCH_OVERVIEW_20261027.md
[proposal]: ../research-proposal/03_RADIAL_DEFORMATION_AND_ZERO_DYNAMICS_RESEARCH_PROPOSAL_20261027.md
[manuscript]: ../radial_deformations_and_zero_dynamics.tex
[n20]: ../notes/20_AUXILIARY_ANGULAR_FLOWS_AND_COLLISION_LOCALIZATION_20261027.md
[review12]: ../reviews/12_RADIAL_INVARIANT_AND_ANGULAR_FLOW_SELF_ASSESSMENT_20261027.md
[b01]: ../brainstorm/01_RADIAL_INTEGRAND_PRESERVING_DEFORMATIONS_AND_COLLISION_LOCALIZATION_20261027.md
[b02]: ../brainstorm/02_AUXILIARY_FLOWS_FOR_COLLISION_LOCALIZATION_20261027.md
[n16]: ../notes/16_CANONICAL_FLUX_MOMENT_RESTRICTION_AND_DIRECT_COMPARISON_20261027.md
[n17]: ../notes/17_RADIAL_DARBOUX_SYSTEMS_PRESERVING_PHYSICAL_OBSERVATION_20261027.md
[n18]: ../notes/18_PHYSICAL_AND_INTERIOR_ZERO_DYNAMICS_FOUNDATION_20261027.md
[review11]: ../reviews/11_INITIAL_DEFORMATION_MANUSCRIPT_AND_PROGRAM_ASSESSMENT_20261027.md
[build12]: ../numerics/12_INITIAL_DEFORMATION_MANUSCRIPT_BUILD_RECORD_20261027.json
[build13]: ../numerics/13_ANGULAR_FLOW_MANUSCRIPT_BUILD_RECORD_20261027.json
[history]: ../chat-histories/index.json
[draft]: ../DRAFT_HISTORY.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a03]: ../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md

# Review of the integrated analytic manuscript

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual model **gpt-6-astra (Codex)**,
reasoning effort **ultra**. Drafting, root review and separate delegated
passes use the same model configuration; this is not independent
specialist review or formal verification.

**Status: analytic consolidation completed; internal review only.**
The [34-page manuscript](../manuscript/main.pdf) and [editable source](../manuscript/main.tex)
assemble the existing results, with proofs in the manuscript and numerics
referenced as supporting applications. No new theta sign, numerical
region, endpoint exclusion or simplicity theorem is asserted.

## Mathematical integration

Separate passes checked the following chains against the source notes
and the assembled text:

- Cluster preparation through contour power sums, local analytic
  intersection multiplicity and discriminant winding, heat-Hermite
  splitting and charge `m(m-1)/2`. The degree/intersection identification
  states its standard regular-value and conservation-of-multiplicity
  input. The relative Chern and normalized Hopf interpretations use the
  same complex orientation; parity and reality do not cancel charges.
- Regular two-root coefficient, exact scalar centering, closed-rectangle
  phase/injectivity argument, nonzero-cap boundary contract, complete
  source strip payments and the explicit hypothetical-double constants
  `96/R^2` and `Kh <= 3/4`. Event-duration bounds retain event existence
  as a premise; height bounds describe the chosen construction.
- Exact logarithmic discriminant response including its centroid-square
  term; complete signed kernel, double residue, event derivatives and
  one-sided acceleration bound; cap persistence, full-homotopy
  continuation and the boundary-derived curvature floor.
- Finite envelope-moment control, its positive curvature and projection
  argument, with the constructed moment vector distinguished from the
  theta vector. The explicit canonical-tail masses, probability law,
  cumulative representation, oscillation and strict matched-envelope
  gain were checked. The improved interval may still contain zero.
- Full-cluster root dynamics, triple cancellation, regular exterior
  coefficient and bound, arbitrary-multiplicity window, Hermite leading
  terms, cubic real-event monotonicity, cubic charge-three and quartic
  charge-six examples, and the variance identity.
- Square holomorphic reference transfer, its bounded-domain/square-map
  hypotheses, sharp heat-jet example, barycentric interpolation error
  and the oriented finite boundary-degree construction.

The signed-response and many-root coefficient notation was separated
to avoid reusing the nonlinear error symbol. The general many-root time
domain explicitly has a piecewise smooth Jordan boundary. Minor draft
issues corrected during integration were a theorem-type reference,
a missing TeX spacing command, the nonnegative (rather than positive)
tail offset at the first omitted mode, and the distinction between a
linear-response interval and its nonlinear discriminant allowance.

The local weighted-charge identity is first stated for finite cutoffs;
its infinite version is conditional on convergence as in the companion
framework. No global convergence theorem is silently imported into the
local proof. The classical xi normalization and real-zero threshold are
explicit external inputs, linked to public primary sources. Higher
multiplicity cannot be reduced to an arbitrarily chosen isolated pair.

## Supporting evidence and document checks

The manuscript's finite real-cap data were checked against
[the saved receipt](../numerics/REAL_CAP_THETA_APPLICATION_20261021.json):
both counts two, complete wall floors, coefficient bound, phase margin,
two disjoint real brackets per cap and 4,146 complete integrals. The
cap discriminants exceed 144 because the brackets are more than twelve
apart. The earlier direct comparisons retain their specified-consumer
scope. The exact algebra receipt supports the displayed identities but
does not replace their proofs. No new source acquisition was needed.

The complete document compiles with both the desktop LaTeX compiler and
local pdfLaTeX/latexmk. The final local build has no undefined references,
undefined citations, duplicate labels, overfull boxes or underfull boxes.
All 130 labels and all 19 cited bibliography keys resolve; all linked
local research records exist. The final PDF has 34 pages and is below
the repository's 1 MiB file limit. All pages were rendered and visually
inspected, with dense equations and tables checked at full page scale.
Build logs and page images are temporary artifacts outside the repository.

## Status and continuation

The manuscript states: “The manuscript is an analytic consolidation, not
an upgrade of those statuses.” ECE-01 remains complete in its
parameterized scope. ECE-02, signed all-height coverage and
higher-multiplicity exclusion remain open; ECE-03 and ECE-06 remain
gated. The review does not close the final-chain or specialist-review
obligations in ECE-07. See the
[endpoint progress register](../research-progress/02_ENDPOINT_CHARGE_EXCLUSION_PROGRESS_20261021.md).

This consolidation follows the [result index](../../../../../../../result-summaries/README.md),
the [local heat-flow cluster](../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
and the [control register](../../../../../../../result-summaries/12_collision_controls_and_screening.md).
It applies the [avoid index](../../../../../../../avoid/README.md), especially
[target classification](../../../../../../../avoid/01_restating_the_target.md),
[scoped exclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md),
and [hypothesis auditing](../../../../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md).
The next research result must pay a sign or event location for the
unchanged complete theta source, with its height and multiplicity
quantifiers; further polish of an already sufficient geometric bound
does not supply that result.

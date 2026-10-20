# Initial manuscript: internal mathematical review

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Reviewing model **gpt-6-astra (Codex)**,
reasoning effort **ultra**, as verified by the coordinating agent.

**Disposition: no blocking mathematical errors found; the requested
boundary-hypothesis clarification is resolved.** This is a separate
**same-model internal mathematical review**,
not independent specialist review or an independent numerical
implementation.

Reviewed source: [manuscript/main.tex](../manuscript/main.tex),
*Heat Flow Contours, Collision Indices, and Gaussian Cap Energy:
Initial research manuscript: results and open estimates*. Final
reviewed source SHA256:

```text
ed5b8901bc35480fa83ab510ffa96987d49f0f36060301403f037af1fad5be2f
```

## Findings

- **Boundary premise — resolved.** Immediately before the
  forward-domain formula \(W_Z=-K_{\mathrm{later}}\), the final
  manuscript now requires \(J\ne0\) on every nonapex portion of the
  boundary and analyticity near the domain's closure. This correctly
  makes the degree's existing hypotheses explicit beside the
  conclusion.
- **Final clarifications verified.** The unweighted Laguerre integral
  now requires integrability and the vanishing endpoint product;
  heat-ball sides are assigned to the adjoint parameter \(s=t-T\);
  and the pair-tail estimate explicitly defines its half-bracket
  kernel \(K_D\). These amendments are mathematically consistent.
- **No unresolved mathematical defect identified** in the analytic
  statements and proofs reviewed below. The numerical subsection and
  exact cache transcription are assigned to a separate reviewer.

## Mathematical checks

The local-index proof establishes both the heat polynomial's real-root
counts and the original jet's isolation. The parabolic Taylor bounds
give a nonzero homotopy on every sufficiently small scaled boundary;
both domain scaling and target normalization preserve orientation.
The index is therefore \(-\lfloor m/2\rfloor\), with the stated
\(dt\wedge dx\) convention. The complex scaled expansion and Rouché
argument also establish nonreal roots just before any multiple real
event. Consequently a strictly later event contradicts the all-real
threshold property. The manuscript correctly treats finite-height
attainment of an ordinary threshold event as an additional premise.

The coupled source remainder removes the mixed absolute-error term
with the same complete positive moments. Its singular-value estimate
and event-dependent apex patch are valid. This improves an unsigned
allowance and supplies no signed winding. The abstract disk
obstruction and the prescribed-jet cubic control have the stated
limited scope.

The root-cap formula, root-following strip count, rounded quadratic
lens, annular-complement accounting and nonzero-level count are
consistent. Endpoint phases for the level arc are correctly taken
for the normalized jet. Arc continuation, nonzero interfaces,
initial-event payment and the cap surplus remain explicit
obligations; a failure of coordinates is not substituted for an
event. The finite polynomial controls distinguish a genuine later
event detector from a threshold counterexample.

The phase formulas involving \(Q=H_x^2-HH_{xx}\), its evolution,
localized integration-by-parts formula and endpoint payment,
positive-source double kernel, critical-value balance and regularized
bulk index have the stated signs and factors. The paired-product
argument gives \(Q\ge0\) under the specified all-real entire-function
hypotheses. Angular energy gives an upper bound on the magnitude of
degree, not a lower bound or its sign. For a complete finite simple
real root system, \(x'=-2\nabla U\) and
\(U'=-2|\nabla U|^2\) are correct. The infinite-system extension is
appropriately deferred pending renormalization and exterior terms.

The Gaussian moment identities follow from the complete source, and
its integrable moments provide the required bounded derivatives.
Hermite completeness and the coefficient and derivative Parseval
formulas are justified in the manuscript. They yield the convergent
deficit identity, sharp constants, quadratic equality case and
higher-order variant exactly as stated. The quadratic, cubic and
positive atomic controls check the constants and signs. The
two-source deficit kernel and Gaussian Bochner balance also check.
Strict negative deficit excludes the initial common zero; it does
not itself force a later collision. Adaptive unspecified small scale
only reformulates first-jet nonvanishing.

## Self-containment and scope

The analytic arguments do not require the reader to retrieve route
notes. Classical threshold theory and the Rodgers–Tao lower bound
are explicitly imported, while standard tools such as Stokes,
Rouché, Hadamard factorization and Fourier uniqueness are identified
where used. I did not independently re-audit the bibliography.

The bounded interval claim is explicitly conditional on the recorded
outward quadrature and arithmetic. The manuscript gives its
integrals, finite consumer formulas, complete error terms and exact
dyadic inputs, so the cache is not a source of missing input values.
This does not convert a recorded quadrature assertion into a symbolic
proof. Source provenance, transcription and numerical validity are
outside this review's assigned scope.

The abstract, status section and continuation program accurately
distinguish exact identities, scoped control obstructions, the small
positive-value box and the still-missing theta sign estimates. No
negative quotient winding, negative fixed-scale theta deficit,
negative localized theta Laguerre average, additional theta collision,
broader coverage or new global bound on \(\Lambda\) is established by
the manuscript. Its new continuation contract is a plan, not a
quantitative result. The manuscript and associated program documents
record and organize the existing results; creating them supplies no
new numerical gain.

The [result index](../../../../../../../result-summaries/README.md)
and [avoid index](../../../../../../../avoid/README.md), particularly
the limits of [same-model review](../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md)
and [scoped exclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md),
govern this assessment.


## Coordinated source and numerical audit

A separate same-model source audit, gpt-6-astra at effort ultra, checked
the source normalization, Mellin factor, shifted finite integral, derivative
majorant, Taylor orders and complete disjoint tail payments. An exact
rational transcription check found all 51 embedded midpoint/radius pairs
identical to the pinned cache. Every displayed component-error upper
bound and all four value lower bounds are conservative at both recorded
consumer precisions. The displayed rounded error sum and majorant are
also safe. The final source distinguishes the midpoint quadrature
tolerances from those of the unscaled positive-majorant integral.

No new quadrature or independent interval implementation was run for this
manuscript audit. It checks the recorded inputs, formulas and claims;
the validity of the source integrals still rests on the stated rigorous
acquisition or an independent reacquisition. The two new program/register
documents also passed a 32-reference destination check.

## Delivery verification

The final reviewed SHA-256 above compiled successfully with the desktop LaTeX compiler after the stated corrections. The manuscript directory was verified to contain only `main.tex` (65,662 bytes), with no external TeX inputs, bibliography files or graphics dependencies. All 36 labels are unique and all 24 internal references resolve. The new program, progress and review documents passed 37 local-link checks; the repository whitespace check passed. These are document-integrity checks, not independent proofs of the mathematical or numerical claims.

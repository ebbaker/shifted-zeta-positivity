# TND-O-E03 r1 analytical manuscript production check

6 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, actual **gpt-6-astra / max**, branch chat0003.
Same assistant/session as the collision reconnaissance and manuscript
author. One local analytical/production pass, followed by necessary
typesetting and wording corrections; no separate assessor or delegation.

## Disposition

**Complete at initial analytical manuscript-production scope.**
The [21-page manuscript](../manuscript/main.tex) systematically derives the
operator and collision results and closes with outstanding analytical
tasks. Its [build record](../manuscript/BUILD_RECORD.json) binds the final
source and generated reading copy.

> This manuscript consolidates the analytical results without adding a canonical collision restriction.

The foundation remains internally accepted within supplied-preparation
scope by [E02 Review01](01_TND_O_E02_R1_CYLINDER_ITE_ASSESSMENT_20261106.md).
The local collision results retain the proof-author status of
[Note07](../notes/07_TND_O_B02_COLLISION_ANATOMY_20261106.md). This production
check does not upgrade either status and is not a substitute for a
separate mathematical assessment. B02 remains open.

## Analytical consistency checked

The review followed the manuscript's dependency order, using the frozen
[E03 inputs](../research-progress/handoffs/09_TND_O_E03_ANALYTICAL_MANUSCRIPT_INPUTS_20261106.json).

1. **Complete source.** Jacobi reflection applies to the full source.
   The derivative-polynomial recursion and half-line majorants give all
   fixed absolute and squared moments. Squaring the source changes the
   linear exponential parameter to 2 beta + 1. The majorants justify
   joint entire dependence and fixed derivatives. Reflected finite
   prefixes are not silently treated as smooth full-line sources.
   The raw Green-source integral retains its exact absolute strip;
   sufficient moment hypotheses are not claimed necessary for every
   analytic continuation (E02 Q1).
2. **Complete operator.** The maximal multiplier domain, adjoint test,
   graph-norm core and absolutely continuous spectrum retain all shells
   and both Dirac signs. The source occupies a declared reducing channel.
   The encoder/readout gives Psi = sqrt(2/pi) h chi, and
   lambda = lambda0 - tau gives forward heat. The reverse-time
   obstruction is ambient, not a denial of continuation for this source.
   The unshifted obstruction compares exponential decay against the
   target's tau^(-1/4) norm in the stated bounded-readout/all-time class.
3. **Energy and local geometry.** The spectral measure uses the squared
   source and differs from the linear interference measure. The mass,
   form and normalized-state derivatives have the correct factor two.
   The double-event expansion gives critical-point velocity -b/a,
   root-midpoint velocity -2b/(3a), and the squared gap
   q = -8s + 16 B_* s^2 + O(s^3), with
   B_* = c/(6a) - b^2/(9a^2). Local factorization does not import an
   unqualified principal-value sum over all zeros.
4. **Shrinking region.** Rescaling gives coefficients 4 sqrt(2)/3,
   16 sqrt(2)/15, and 4 sqrt(2)/3 in the absolute-amplitude, mass and
   kinetic-form integrals. The quotient is 5/(4 epsilon), while both
   unnormalized quadratic quantities vanish. The zero extension is in
   the form domain, generally not the full operator domain; no physical
   conditioning protocol is inferred.
5. **Interference and response.** Momentum-sector damping fixes the
   observation point and uses linear source weights. Gaussian
   differentiation gives second signed moment 4 Delta^2 a; equal
   signed masses and centroids give the variance formula. The event
   Jacobian has determinant a^2 and the response has the stated
   imaginary-time signs.
6. **Multiplicity and control.** The finite heat polynomial follows
   from the heat equation. Its recurrence has a self-contained
   real-root/interlacing proof; the implicit-function argument resolves
   the even/odd post-event counts. The exact super-Gaussian control
   satisfies the analytic/domain premises and collides. Positivity of
   its remaining transform factor follows from moment inequalities
   without quadrature. It fails the exact theta arithmetic premise;
   this is not a general exclusion of every source-specific or physical
   argument. Other control families are not newly audited (E02 Q2).

These are internal consistency checks, not specialist independence.
No numerical campaign or canonical zero search was performed.
The inherited [exact algebra record](../numerics/COLLISION_ANATOMY_CHECK_20261106.json)
and script identity were inspected; its unchanged finite checks were not
presented as a uniform theorem or rerun as a new campaign.

## Production corrections and validation

Before the first build, four damaged TeX alignment line breaks and three
cross-reference labels were corrected, and the schematic's horizontal
scale was made consistent with its node locations. A stray parenthesis
in the amplitude expression was removed. The contents were then placed
on a separate page. Final wording identifies positivity of the scalar
momentum envelope, not of an arbitrarily phased spinor, and replaces
research shorthand about analytic “payments” by explicit bounds. These
are manuscript production corrections; frozen research notes were not
edited.

The final pdfLaTeX/latexmk build has **21 pages**, ten resolved bibliography
entries, and no warnings, missing references, overfull or underfull boxes.
Text extraction found no unresolved-reference or replacement-character
markers. All pages were rendered with Poppler and visually inspected for
equation alignment, typography, figure placement, references and page
transitions. After final wording edits, every changed contact sheet was
reinspected; the remaining sheets were image-identical to the inspected
versions. The PDF and renders remain only in ignored root output/pdf.
Author attribution and LLM/model/effort acknowledgements are present.

## Retained research boundary

> The singular local quotient is compatible with regular global field energy.

The smooth field, divergent zero velocities and divergent normalized local
quotient are different observations of the same regular evolution. None
excludes the explicit control. Further work must justify a quantitative
canonical-source restriction, with regional, multiplicity and endpoint
hypotheses stated. Separate mathematical assessment, intrinsic source
generation and a same-information advantage remain distinct tasks. The
manuscript selects no optimal route and activates no successor execution.

See the [result index](../../../../../result-summaries/README.md),
[theta summary cluster](../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md),
[patterns index](../../../../../avoid/README.md), and
[re-realization warning](../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md).

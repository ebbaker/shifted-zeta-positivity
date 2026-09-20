# Continuation after the predictive hemisphere-localization test

Date: 20 September 2026. Prepared for Edward Baker.
Model: OpenAI GPT-6 (Codex; developer-provided identity).
Effort setting: not exposed in this session; not inferred.

## Read first

1. `notes/PREDICTIVE_LOCALIZATION_HEMISPHERE_TEST_20260920.md` in this
   investigation, with `numerics/check_localization_hemisphere.py` and its
   small record under `numerics/records/`.
2. Current `manuscript.tex`, `supplementary-information.tex`, especially
   `sections/03_free_kernel.tex`, `sections/06_projectors.tex`,
   `sections/07_endpoints.tex`, `sections/s_localization.tex`, and the
   fixed-window response sections. Preserve these snapshots.
3. `notes/LOCALIZATION_AND_THE_POLE_CANCELLATION_20260920.md` and
   `notes/FIXED_WINDOW_WILSON_RESPONSE_OBSTRUCTION_20260920.md`.
4. For the separate arithmetic status, the critical-path notes
   `RESEARCH_CONTINUATION_AFTER_EMA_ANCHOR_20260920.md` and
   `RESEARCH_CONTINUATION_AFTER_CUMULATIVE_APPEND_20260920.md`.

The user chose a predictive localization calculation before returning to
cumulative-coupling estimates. No new Codex task was launched. The prompt
below is for the user's next task.

## What is established in this bounded calculation

- The specified free 3d N=4 Higgs boundary polarization has an independently
  known hemisphere state proportional to `exp(-x)`, where
  `x=4*pi*r*|Y|^2`. Its Fourier–Mellin transform is
  `Gamma(s)/sqrt(2*pi)`, `s=1/2-i*sigma`, in flux zero. This is an established
  physical localization input and an elementary integral calculation, not a
  prescribed arithmetic Gaussian tower.
- The closed-circle determinant includes both frequency directions and is
  `1/(2*cosh(pi*mu))`. Direct affine real-mass identification cannot give the
  arithmetic high-frequency behavior. A single gamma belongs to a boundary
  amplitude before pairing, not to that closed-circle determinant.
- Actual scalar endpoint operators give `N`, `N-1`, or `N-1/2`, where
  `N=-x*d/dx`. Their Mellin factors are linear. Under the unproved comparison
  map `s=(p+1/2)/2`, a single pair removes the lowest gamma pole but misses
  the additional arithmetic factor `p-1/2`.
- Under that map the target amplitude is obtained algebraically by the
  descendant `T=N*(2*N-1)`, which acts as `(2*x^2-3*x)*exp(-x)` on the
  vacuum, plus the external normalization `pi^(-p/2)`. This is an inverse
  fit within a real operator algebra. It is NOT a derivation of the actual
  open-line insertion or an unpaired fermion.
- The degree-two obstruction is conditional. The alternative unproved map
  `s=(p+5/2)/2` changes the needed polynomial to `2*N-3`. Do not report a
  dictionary-independent no-go for bilocals.
- Mellin Plancherel gives ordinary radial-control norms `1/2`, `1/4`, `3/4`
  for the vacuum, N vacuum and T vacuum. Reusing the vacuum gluing phase
  with the same analytic polynomial on both sides instead gives `1/2`, `0`,
  `1/2`. It is an intentionally incorrect adjoint operation, not a flaw
  in the cited gluing formula. In this control `N^dagger=1-N`.

The standard-library numerical checks pass at 24 and 40 quadrature nodes per
piece. They are floating-point diagnostics. Their purpose is to catch
normalization, ordering, sign and transpose mistakes in the exact comparison.
No arithmetic operator positivity follows from them.

## Main unresolved question

The localized Mellin transform acts on the **size of the boundary field**.
The arithmetic Laplace transform acts on a **spatial logarithmic coordinate**.
The circle mass, mirror Coulomb parameter, boundary-field Mellin parameter,
spatial angular momentum, and arithmetic spectral parameter are not already
the same object. Identifying them from a gamma-function resemblance would
undo the predictive character of this calculation.

The immediate task should derive, or obstruct, that identification in the
free conformal control and compute the corresponding two-endpoint state.
It should stop at the first demonstrated incompatibility instead of adding a
quartic insertion, arbitrary counterterm, or spectrum to obtain agreement.

## Suggested next-task prompt

Continue in `~/Documents/shifted-zeta-positivity`, under
`papers/susy-positivity/investigations/wilson-loewner`.

Read `notes/PREDICTIVE_LOCALIZATION_HEMISPHERE_TEST_20260920.md` and
`notes/RESEARCH_CONTINUATION_AFTER_LOCALIZATION_TEST_20260920.md` first, then
the current main/supplementary sources on the free kernel, endpoint
supersymmetry, fixed-window response and localization. Consult the exact
primary references cited there. If required local material is unavailable,
request it before making claims depending on it.

Perform one bounded investigation: **derive or obstruct the map from spatial
radial evolution to the localized hemisphere boundary representation**.
Use the free 3d N=4 hypermultiplet as the control, with an explicit conformal
supercharge and the supersymmetric boundary polarization already specified
in the new note. Do not assume its embedding in the full 4d Wilson problem.

1. Start from the spatial cylinder coordinate `u=log(rho)`, its radial
   translation generator, and the free covariance with rates `ell+1/2`.
   Determine whether this evolution preserves the chosen boundary
   cohomology and what operator it induces on the hemisphere state. Keep
   the boundary-field coordinate `x=4*pi*r*|Y|^2` distinct from spatial
   radius. If evolution does not descend to this protected sector, give
   an explicit commutator or boundary-condition obstruction.
2. If it does descend, derive the scale, offset, contour, measure and
   ordinary adjoint relating its spectral parameter to the Mellin variable
   `s=1/2-i*sigma`. Distinguish angular-harmonic multiplicities from
   polynomial/occupation degree. Identify what physical deformation, if
   any, realizes `p -> p +/- omega`; a Q-exact localization coefficient
   is not such a deformation.
3. Compute the boundary state produced by the simplest compatible conformal
   two-scalar open-line control, including transport and any contact or
   current terms actually forced by its action or Ward identity. Compare
   with the complete prime-free arithmetic symbol only after fixing these
   data. Do not insert `N*(2*N-1)` or an equivalent polynomial merely
   because it fits. The earlier polynomial-degree obstruction assumes
   `s=(p+1/2)/2` and is not valid for every unproved dictionary.

The desired deliverable is an explicit generator/observable dictionary with
an independently predicted spectral factor, or a precisely scoped
obstruction and the smallest additional physical ingredient it would require.
A failure of the free protected sector is useful; a fitted determinant is
not completion. A one-sided gamma amplitude, analytic continuation, or a
positive norm in the control is not yet a causal arithmetic transfer or a
cumulative-positivity certificate. Retain the repository's fixed local
normalization and reflection conventions. Do not count smoothing or averaging
as arithmetic positivity.

Save a new research note and handoff, with reproducible code and small records
only where useful. Preserve historical notes and manuscript snapshots, follow
`LARGE_FILES.md` and the investigation folder conventions, and record the
actual model plus any effort setting that is exposed without guessing.

## Fallback after the bounded test

If the spatial generator cannot descend, the next localization direction
would need a different protected observable, an interface that retains the
missing generator, or an unprotected calculation. Which one is appropriate
must follow from the obstruction; none is assumed to exist here. The
independent cumulative-defect work can resume from its own handoff without
using any localization claim as an arithmetic positivity input.

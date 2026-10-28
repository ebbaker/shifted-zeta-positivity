# Assessment of the fixed theta transform setup

28 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**.
Chat0013. Same-assistant mathematical and editorial checking, not
independent specialist review.

Scope: [Book manuscript](../book/main.tex) and
[setup note](../brainstorm/06_BOOK_TRANSFORM_SETUP_20261028.md).

## Identities checked

- The three-dimensional radial Laplacian of the theta series gives
  \(Q=4\pi\sum n^2(2\pi n^2r^2-3)e^{-\pi n^2r^2}\).
  Applying it to \(r^{-1}f(1/r)\) gives the factor \(r^{-5}\);
  Jacobi reflection then gives \(Q(r)=r^{-5}Q(1/r)\).
  Positivity for \(r\ge1\) and reflection give positivity for all \(r>0\).
- The substitution \(r=e^{2u}\), with normalized spherical measure,
  gives \(dX=8\pi r^3\,du\,d\sigma\). The half-line definition of \(H\)
  requires a factor \(1/2\) on the whole line. Consequently the density
  is \(q_t/(16\pi r^3)=e^{t\log^2r/4}Q/(64\pi\sqrt r)\).
  It is half the earlier exterior density, with a reflected interior.
- Differentiated theta tails are bounded by a polynomial times a Gaussian.
  Reflection controls the origin. These bounds justify Schwartz
  regularity, flat extension at zero, exponential log-radius moments,
  spectral differentiation, and \(H_t=-H_{zz}\).
- Under the displayed Fourier convention the inverse factor is \(1/(2\pi)\).
  Dividing by \(8\pi r^3\) yields \(1/(16\pi^2r^3)\) for the real-line
  radial inverse, and \(1/(8\pi^2r^3)\) for the canonical half-line cosine
  inverse.
- The angular perturbation has zero spherical mean, multiplier strictly
  positive for \(|\varepsilon|<1\), and a smooth extension at the origin.
  It supplies a genuine nonuniqueness example within positive densities.
- Fourier uniqueness for integrable marginals gives fixed spherical
  average from preservation of all real spectral observations. Absolute
  exponential moments justify every complex observation. Equality of
  marginals is almost everywhere; smoothness upgrades it where applicable.

The Jacobi input and Fourier theorem are annotated in
[reference01](../references/01_CIRCLE_HEAT_AND_JACOBI_NORMALIZATIONS_20261027.md)
and [reference10](../references/10_PROJECTED_EVOLUTION_AND_ELLIPTIC_RESPONSE_20261027.md).
The normalizations and spatial deductions are checked directly.

## Interpretation and limits

The kernel has no auxiliary parameter. Defining a fixed transform does
not by itself conserve its output. Mass conservation preserves only the
zero-frequency observation; every spectral pairing is the required
invariant.

With this kernel, preservation is pointwise only after angular averaging.
It fixes the radial marginal and leaves angular freedom. Radial densities
cannot vary in this class, but nonradial densities can. This is a scoped
consequence of the exponential log-radius kernel, not an impossibility
claim about other kernels or three-dimensional dynamics.

The cosine kernel sees only the even marginal and would allow more
freedom. The manuscript distinguishes the two choices. The gradient
\(j=\nabla_X\rho\) is not a flux or a spectral derivative.

Collision conditions are translated, not excluded. No new mechanism or
criterion is proposed, so this assessment does not present numerical
collision-control tests as evidence for a new theorem. The existing
[control summary](../../../../result-summaries/12_collision_controls_and_screening.md)
and [geometric-pattern scope](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md)
remain applicable.

## Build and presentation

Both the built-in compiler and a local latexmk build succeeded.
All eight final pages were rendered and visually inspected: equations,
table, headings, references and page boundaries were legible and
unclipped. The final log contains no warnings or overfull/underfull boxes.
All 37 labels are unique and all 23 internal references resolve.
The exact source and delivered PDF hashes are in
[record18](../numerics/18_BOOK_TRANSFORM_SETUP_BUILD_RECORD_20261028.json).

The earlier conservative-flow manuscript was not edited in this work.
Its existing working-tree hash is retained in the build record. This
companion focuses on the requested setup and chooses no auxiliary flow.

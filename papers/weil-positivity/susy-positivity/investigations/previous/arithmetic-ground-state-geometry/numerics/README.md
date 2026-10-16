# Checks and numerical work

This investigation prioritizes analytical identities and physical constructions. Numerical work tests a derived formula or distinguishes a specified candidate; it does not substitute sampled positivity for the bulk argument.

Keep programs in this directory and small, explicitly labelled diagnostic records under `records/`. Preserve historical outputs and write replay results to a new destination. Exact symbolic or rational checks must be distinguished from floating-point diagnostics and rigorous error bounds.

## First continuation: exact supercharge algebra

[check_supercharge_algebra.py](check_supercharge_algebra.py) uses only Python's standard library. It normal-orders first-order differential operators on the four-component exterior algebra, with integer polynomial coefficients in the first and second derivatives of a general real function. It verifies nilpotence, the mixed Hessian-trace defect, and equality of the two Hamiltonians when the function is harmonic. The result is in [the small algebra record](records/supercharge-algebra.json).

Run from the investigation directory:

```sh
python3 numerics/check_supercharge_algebra.py
```

To save a fresh record, pass `--output /path/to/a/new-record.json`; an existing destination is refused. The program checks common-core operator identities, not self-adjoint domains, physical ground states, the full Weil form or positivity bounds. The corresponding analytical construction is in [the extended-theory note](../notes/01_EXTENDED_THEORY_CONSTRUCTION.md).

## Exact interacting-period test

[check_quartic_period_identity.py](check_quartic_period_identity.py) uses exact rational Laurent-polynomial arithmetic to eliminate the moment variables in the fixed-quartic model and substitute the proposed Euler period into its differential equation. The [retained record](records/quartic-period-identity.json) states the analytic assumptions and the nonzero reciprocal residual.

```sh
python3 numerics/check_quartic_period_identity.py
```

It also accepts `--output /path/to/a/new-record.json` and refuses an existing destination. Its two checks verify algebra after the moment identities in [the quartic-period note](../notes/05_QUARTIC_PERIOD_TEST.md); they do not prove the integration-cycle hypotheses or the physical-metric argument.

## Exact shape-period and vacuum-algebra checks

[check_shape_period.py](check_shape_period.py) derives the shape differential equation from the mass equation and homogeneity, then checks nine asymptotic coefficients obtained independently from Gaussian moments. Its three labelled checks and their scope are recorded in [shape-period.json](records/shape-period.json). The derivation is in [note 09](../notes/09_SHAPE_PERIOD_AND_NORMALIZATION.md); the expansion at zero is an asymptotic expansion, not an assertion of a convergent Taylor series.

[check_shape_jacobi.py](check_shape_jacobi.py) verifies the rank-three multiplication relations, cyclic identity source, residue orbit weights, semisimple spectrum and an auxiliary positive flat metric control. Its four labelled checks are recorded in [shape-jacobi.json](records/shape-jacobi.json). The physical boundary condition derived in [note 06](../notes/06_SHAPE_DEFORMATION_GEOMETRY.md) excludes this control as the actual metric; the program does not solve the physical metric equation.

```sh
python3 numerics/check_shape_period.py
python3 numerics/check_shape_jacobi.py
```

Both programs use exact rational arithmetic and accept `--output /path/to/a/new-record.json`, refusing an existing destination. They check the displayed algebra, not the analytic Hodge, source-continuity or boundary-state arguments.

To verify the package and replay all ten programs without overwriting their records:

```sh
python3 validation/check_package.py --replay
```

## Reflected boundary and endpoint algebra

[check_boundary_pairing.py](check_boundary_pairing.py) checks the physical reflection on the full degree-two exterior algebra using exact Gaussian-rational coefficients. It also checks the raw Gaussian cohomology coefficients and product-pairing sign, the full Laurent-polynomial homogeneous endpoint family, and the massive endpoint frame conversion. Its four labelled checks are saved in the new [boundary-pairing record](records/boundary-pairing.json).

    python3 numerics/check_boundary_pairing.py

The program accepts the same optional output argument and refuses an existing destination. It uses the stated Gaussian integral formulas and verifies algebra; it does not prove Hodge comparison, cutoff decay, endpoint continuity, source closure, radial uniqueness or arithmetic positivity. The analytical statements are in notes 10–13. The five programs through that milestone reproduce twenty-two labelled exact checks.

## Coherent defects, graph returns and collective feedback

[check_coherent_delay.py](check_coherent_delay.py) checks two-output delay cancellation, the Fourier cross-term signs, the interior pole coefficient, the two-shift contact optimum and the single-prime massive tail. Its five exact Laurent-algebra checks are retained in [coherent-delay.json](records/coherent-delay.json); the analytical source and finite-alphabet argument are in [note 15](../notes/15_COHERENT_DELAY_DEFECT.md).

[check_prime_returns.py](check_prime_returns.py) verifies the orthogonal vertex coupler, stub elimination, unitarity, determinant, complementary powers, signed returns/contact and Wigner–Smith formula. Its seven exact polynomial checks are retained in [prime-returns.json](records/prime-returns.json); the positive graph and stationary-contact argument are in [note 16](../notes/16_PRIME_RETURN_CHANNELS.md).

[check_collective_feedback.py](check_collective_feedback.py) compares the directly squared readout with the claimed compact residual, matches the contact, differentiates the residual exactly, verifies both parameter minima and keeps the nonzero massless residual. Its five exact polynomial checks are retained in [collective-feedback.json](records/collective-feedback.json). [Note 17](../notes/17_COLLECTIVE_FEEDBACK_AND_COMPACT_DEFECT.md) proves the domain and compactness claims and the obstruction to finite Schatten-class corrections.

```sh
python3 numerics/check_coherent_delay.py
python3 numerics/check_prime_returns.py
python3 numerics/check_collective_feedback.py
```

Each uses only the standard library, accepts the optional output argument and refuses to overwrite an existing record. These programs verify finite algebra, not the analytical Robin stability, scattering preparation, infinite-series uniqueness, closed-source domains, compactness or regularity obstructions. Through note 17, these eight programs retain thirty-nine labelled exact checks. No checker certifies positivity of the complete Weil form.

## Joint response, finite-rank completion and rational cutoff

[check_joint_response.py](check_joint_response.py) adds ten exact checks with its [retained record](records/joint-response.json). It checks the binomial response coefficients and finite residuals, one-pass joint feedback, noncommuting resolvent words with their exact remainder, every retained low-output component, the full polarized finite-rank completion and its source correction. A deliberately negative non-arithmetic target confirms that the completion is not a positivity proof. Rational series bounds and a finite gamma sum verify the length-one high-sector cutoff \(N=4,\delta=1/16\).

    python3 numerics/check_joint_response.py

The program requires only the standard library and accepts the same optional output argument, refusing to overwrite a record. These checks accompany [note 18](../notes/18_REVIEW_AND_NEUMANN_COMPARISON.md) and [note 19](../notes/19_JOINT_RESPONSE_AND_FINITE_RANK_DEFECT.md). Through note 19 there are nine programs and forty-nine labelled checks. The new records do not evaluate the remaining arithmetic Schur matrix or claim a new positivity interval.

## Arithmetic sign and boundary response

[check_arithmetic_sign.py](check_arithmetic_sign.py) adds ten exact checks, retained in [arithmetic-sign.json](records/arithmetic-sign.json). Independent hyperbolic Green-kernel and boundary-derivative expressions test the endpoint correction; rank-two Gram calculations test its cosine columns and parity. Explicit negative vectors test the inverse-tail and noncommuting-word obstructions. Direct inversion tests the full mixed residual identities and mode-tail bound. Several positive reference shifts leave the same negative Schur matrix. Exact rational series and an infinite-tail integral bound supply the constants for the smooth-density negative witness at length two.

```sh
python3 numerics/check_arithmetic_sign.py
```

The program uses the standard-library rational matrix helpers from the unchanged joint-response checker. The output option refuses an existing record. All ten programs now replay 59 labelled exact checks. These do not prove essential norm, domain equality, infinite-dimensional convergence, or the actual arithmetic sign. See [note 20](../notes/20_ARITHMETIC_SIGN_AND_BOUNDARY_RESPONSE.md) for the proofs and limitations.

## Large-data policy

Large derived files belong in the external location defined by [ARCHIVES.md](../ARCHIVES.md), with `ARITHMETIC_GROUND_STATE_ARCHIVES` as the lookup fallback. `output/` is ignored as a local working-data directory. No large data, floating-point experiment or numerical positivity sweep was produced in this continuation.

# Exact algebra checks

20 October 2026. Prepared for Edward Baker with substantial LLM assistance;
**gpt-6-astra, reasoning effort ultra**, verified session configuration.

The [frozen contract](EXACT_ALGEBRA_CONTRACT_20261020.md),
[standard-library replay](check_rhs_exact_algebra.py) and
[small result record](EXACT_ALGEBRA_REPLAY_20261020.json) check 265 rational
fixtures. Run `python3 check_rhs_exact_algebra.py` from this directory.
These are finite algebra checks, not theta quadrature, zero certificates
or proofs of the analytical asymptotics. No large data are generated.

## Bounded Lean check

The [flat-taper projection check](lean/README.md) contains the source,
successful Lean 4.34.1 log, exact mathlib pin and VM-specific runner.
It verifies an abstract real-inner-product implication used in Note 12
§11; the analytic taper identities and zeta transfer are not formalized.
The existing Multipass Linux setup was used without changing its replay
project or installing dependencies.

## Heat root motion algebra

21 October 2026 — prepared for Edward Baker with substantial LLM
assistance, **gpt-6-astra, actual effort max**.
The [HMC replay](check_hmc_exact_algebra.py) freezes exact rational
fixtures for paired velocities, moving deflation, finite root blocks,
Hermite heat polynomials, atomic series and covariance cancellation.
Run `python3 check_hmc_exact_algebra.py`; use `--output PATH` to save a
small execution record. The [record](HMC_EXACT_ALGEBRA_REPLAY_20261021.json)
passed. Its scope is finite algebra, not infinite tails, theta root
enclosures, a numerical shrinkage onset or simplicity. The analytic
bounds are in Notes 19–20; no large data are generated.

## Moving-tube algebra

21 October 2026 — prepared for Edward Baker with substantial LLM
assistance, **gpt-6-astra, actual effort max**.
The [moving-tube replay](check_hmc_moving_tube_algebra.py) checks frozen exact polynomial
identities for the physical phase, oriented flux and weight correction,
primitive change, transverse derivatives and moving-average normalization.
Run `python3 check_hmc_moving_tube_algebra.py`; `--output PATH` writes a small receipt.
The [record](HMC_MOVING_TUBE_ALGEBRA_REPLAY_20261021.json) passed. This is finite rational algebra,
not theta quadrature, a physical energy-floor certificate, an infinite
product proof or a simplicity result. No large data are generated.

## Endpoint-profile algebra

21 October 2026 — prepared for Edward Baker with substantial LLM
assistance, **gpt-6-astra, actual effort max**.
The [endpoint-profile replay](check_hmc_endpoint_trace_algebra.py) checks frozen degrees two
through eight using rational polynomial quotient rings: Hermite heat
normalization, individual critical-point tube profiles, their quadratic
coefficient, the separately proved outer formula, and phase-measure
fixtures. Run `python3 check_hmc_endpoint_trace_algebra.py` from this folder;
`--output PATH` writes a small receipt. The [record](HMC_ENDPOINT_TRACE_ALGEBRA_REPLAY_20261021.json)
passed and binds the script and existing algebra-helper hashes. It does
not verify universal analytic quantifiers, a theta event or a numerical
error threshold. No large data or theta quadrature are generated.

## Gauss area and curvature checks

21 October 2026 — prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, actual effort max**.
The [finite replay](check_hmc_gauss_concentration.py) checks the complex
Gram normalization, heat polynomials of degrees two through ten, both
time signs, the pure endpoint radial flux, asymmetric complex inner
coefficients on both parity branches, and rational enclosures of the
exact quadratic disk-area formula. Run
`python3 check_hmc_gauss_concentration.py`; `--output PATH` writes a
small record. The [saved record](HMC_GAUSS_CONCENTRATION_CHECKS_20261021.json)
passed and binds both existing algebra dependencies. The concentration
theorem and limits are proved in Note 24; these finite checks do not
establish a theta sign, infinite-tail estimate or endpoint exclusion.

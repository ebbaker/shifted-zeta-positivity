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

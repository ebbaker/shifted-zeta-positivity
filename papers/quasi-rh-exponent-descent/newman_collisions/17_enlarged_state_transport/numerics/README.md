# Enlarged-state algebra checks and future experiments

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6.1-sol (Codex), reasoning effort ultra, verified from the
recorded drafting-turn configuration. Internal replays are not independent
mathematical validation.

The initial manuscript uses the existing
[exact enlarged-state checker](../../13_microlocal_phase_space/numerics/check_enlarged_state_identities.py)
and [small identity record](../../13_microlocal_phase_space/numerics/ENLARGED_STATE_IDENTITY_RECORD_20261010.json).
They remain in their original location so one source defines the common
controls. The standard-library replay checks the anchored graph and Schur
example, the Gaussian collision control, chord commutator, and score-to-jet
quadratic with exact rational arithmetic. It does not establish a theta
sign, useful transport multipliers, or interval coverage.

From the repository root, replay without replacing the shared record:

```sh
python3 papers/quasi-rh-exponent-descent/newman_collisions/13_microlocal_phase_space/numerics/check_enlarged_state_identities.py /tmp/project17_enlarged_state_replay.json
```

## Continuation checks

10 October 2026 continuation: GPT-6 (Codex), reasoning effort unavailable
to this session and not inferred; internal LLM checks.

- [Exact adjoint checker](check_adjoint_transport_optimality.py) and
  [record](ADJOINT_TRANSPORT_OPTIMALITY_RECORD_20261010.json): 1,878 exact
  Fraction assertions for full and restricted trees, support geometry,
  source cancellations and disconnected-sector payments.
- [Regular cell checker](check_regular_adjoint_cell.py) and
  [record](REGULAR_ADJOINT_CELL_RECORD_20261010.json): complete N=22066
  outward enclosure on t0 to t0+0.000008 and x0+0.3 to x0+0.7. The paid
  directional margin is greater than 0.5552583, conditional on the
  imported complete disk interface. The same forty subcells also exclude
  by separate paid tests, 38 by value and two by derivative.
- [Heat transversality checker](check_heat_transversality.py) and
  [record](HEAT_TRANSVERSALITY_RECORD_20261010.json): 1,819 exact rational
  and quadratic-field assertions. These check implicit fold jets, full
  Jacobians, stationary precursor coefficients for both parities,
  positive Gaussian double/triple/quadruple controls, frozen-beta score targets,
  physical normalization through order three and product error payments.
  The analytic stationary-sign theorem is proved in Note 5; the replay
  establishes no genuine theta sign or stationary-set coverage.

Replay from the repository root without replacing the saved records:

```sh
python3 papers/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/numerics/check_adjoint_transport_optimality.py /tmp/project17_adjoint_algebra_replay.json
python3 papers/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/numerics/check_regular_adjoint_cell.py /tmp/project17_regular_cell_replay.json
python3 papers/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/numerics/check_heat_transversality.py --record /tmp/project17_heat_transversality_replay.json
```

The cell checker validates both retained program 13 source hashes before
importing them. Its default source directory is relative to its location;
`--interval-source-dir` permits a staged replay. No extra dependencies
are required. Runtime metadata can vary; the small records include source
hashes, all directed endpoints and explicit complete error payments.

Future experiments should test a uniform correlated direction or source
estimate on a growing family, or the complete signed stationary-set
targets in Note 5, retaining all physical, residual and boundary costs.
Every claimed visibility margin requires outward enclosures on a stated
parameter domain. Store source code and small records; keep large derived
data outside Git under the repository's
[large-file policy](../../../../../LARGE_FILES.md).

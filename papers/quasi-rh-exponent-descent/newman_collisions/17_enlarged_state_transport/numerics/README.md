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

Future project-specific experiments belong here. The first useful
experiment should test a specified regular adjoint multiplier family on
the complete prescribed state, retaining all residual and boundary costs.
Every claimed visibility margin requires outward enclosures on a stated
parameter domain. Store source code and small records; keep large derived
data outside Git under the repository's
[large-file policy](../../../../../LARGE_FILES.md).

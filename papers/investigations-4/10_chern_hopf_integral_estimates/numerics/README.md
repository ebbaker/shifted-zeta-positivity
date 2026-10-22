# Computations and small execution records

22 October 2026. Prepared for Edward Baker with substantial LLM assistance;
actual recorded **gpt-6.1-sol, effort ultra**, verified from this turn.

The initial organization/write-up step added no calculation. The new
[coupled signed tail script](certify_coupled_signed_tail.py) and
[certificate](COUPLED_SIGNED_TAIL_CERTIFICATE_20261022.json) acquire one
actual regular canonical critical point and compare complete signed
intervals. [Local Note 02](../notes/02_COUPLED_SIGNED_THETA_TAIL_ESTIMATES_20261022.md)
contains the proofs, scope and full-source tail payments. Replay with
Python and python-flint 0.9.0:

```sh
python numerics/certify_coupled_signed_tail.py --out /tmp/coupled-signed-tail-replay.json
```

Run from this investigation's directory. No machine-specific runtime path
is embedded. The receipt records the script hash, parameters, actual
precision, library versions, costs, controls and complete interval gains.
An added direct signed tail integral outperforms the moment certificates;
no global theta event or exclusion is certified.

The retained earlier scripts and receipts remain at their original hash-bound paths:

- [Gauss comparison script](../../03_heat_transport_and_charges/numerics/check_chb_gauss_comparison.py)
  and [receipt](../../03_heat_transport_and_charges/numerics/CHB_GAUSS_COMPARISON_CHECKS_20261022.json).
- [Critical-wall script](../../03_heat_transport_and_charges/numerics/check_chb_critical_wall.py)
  and [receipt](../../03_heat_transport_and_charges/numerics/CHB_CRITICAL_WALL_CHECKS_20261022.json).
- [Complete-boundary script](../../03_heat_transport_and_charges/numerics/check_chb_full_boundary.py)
  and [receipt](../../03_heat_transport_and_charges/numerics/CHB_FULL_BOUNDARY_CHECKS_20261022.json).

They are exact finite algebra plus explicitly labeled floating diagnostics,
as their records specify; none is an analytic formalization or theta event
certificate. Keep new focused computations here, under [LARGE_FILES.md](../../../../LARGE_FILES.md).
Do not copy old receipts or regenerate them solely because their program moved.

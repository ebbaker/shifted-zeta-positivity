# Numerical and algebraic replay

10 October 2026. Model: GPT-6 (Codex); exact serving variant and configured reasoning effort unavailable and not inferred. Checks are internal, not independent mathematical review.

Run from the repository root:

```bash
python3 papers/quasi-rh-exponent-descent/newman_collisions/10_kinetic_stochastic/numerics/check_memory.py
```

The script requires only Python 3 and the standard library. It prints a small JSON record; [the run record](SCOUT_CHECK_RECORD_20261010.json) was produced on 10 October 2026 with Python 3.10.0. Status: **PASS**.

Finite quadrature replay checks the exact eliminated-memory identity, the three resolved rows, a nonzero fourth-derivative closure defect, and six positive memory quadratic forms. These are floating-point structural checks, not a numerical lower bound at a genuine collision.

The source note supplies the analytic arguments. Floating-point checks are not rigorous numerical enclosures and are not independent mathematical validation. No large generated data are stored. Follow [LARGE_FILES.md](../../../../../LARGE_FILES.md) if later computations need an archive.

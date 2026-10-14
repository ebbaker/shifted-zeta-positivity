# Euler-factor control checks

13 October 2026. Prepared for Edward Baker with LLM assistance.
Model: Claude Opus 5.5 (configured identifier `claude-opus-5-5`; the serving
model may differ), Claude Cowork, reasoning effort **max**.

Run, in this directory:

```sh
python3 -I check_euler_factor_controls_claude_20261013.py --output EULER_FACTOR_CONTROLS_RECORD_20261013.json
```

The [checker](check_euler_factor_controls_claude_20261013.py) uses only the
Python standard library and takes about 20 seconds. It prints the
[record](EULER_FACTOR_CONTROLS_RECORD_20261013.json) as deterministic JSON
and exits nonzero if any check fails.

- **Part E, exact rational arithmetic.** Roots of the Euler-factor
  perturbation \(Q_p\) are off the critical circle and reciprocal; the
  Laguerre product rule; the multiplier's Laguerre expression; the algebra
  of the first-order expansion.
- **Part N, double precision.** \(S_2\) and \(\xi(\tfrac12)\) by
  quadrature; the exact flow against direct quadrature; zero tracking and
  Newton on \(H=H_x=0\) for twelve \((p,c)\), with the collision order of
  the three lowest pairs and the expansion ratio; Laguerre witnesses below
  \(\Lambda_{c,p}\) and nonnegativity above; \(\Lambda_{1/2,p}\) for all
  primes \(p\le47\).

Part N uses contour-shifted trapezoid quadrature and Newton iteration. It
is numerical evidence, not an interval certificate; certification of one
witness is the folder's next task. Keep large regenerable data outside Git
under [LARGE_FILES.md](../../../../../LARGE_FILES.md).

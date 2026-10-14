# Rank two automorphic lift checks

13 October 2026. Prepared for Edward Baker with LLM assistance.
Model: Claude Opus 5.5 (configured identifier `claude-opus-5-5`; the serving
model may differ), Claude Cowork, reasoning effort **max**.

Run, in this directory:

```sh
python3 -I check_rank_two_lift_claude_20261013.py --output RANK_TWO_LIFT_RECORD_20261013.json
```

The [checker](check_rank_two_lift_claude_20261013.py) uses only the Python
standard library and takes about 45 seconds. It prints the
[record](RANK_TWO_LIFT_RECORD_20261013.json) as deterministic JSON and exits
nonzero if any check fails.

- **Part E, exact rational arithmetic.** The insertion annihilates the four
  constant-term powers; the insertion generates the theta terms; the pair
  weights of both Laguerre expressions; Gaussian tilting moments; the
  index-two sublattice count; the two-coset identity over
  \(\mathbb Q(\sqrt2)\); Hecke multiplicativity at 2; the \(q\)-adic
  coefficient test for the controls.
- **Part N, double precision.** The fixed-shape cusp formula, including
  complex spectral variable; Newman-time formulas for both Laguerre
  expressions against direct quadrature; Whittaker mode shares; the sign of
  the folded kernel; the Hecke relation at 2 on two geodesics; the two-coset
  identity at three Newman times; the control tests.

Part N is a quadrature replay with contour shifts, not an interval
certificate. See [Note 1](../notes/1_CUSP_FORMULA_HECKE_AND_CONTROLS_20261013.md)
for statements and proofs. Keep large regenerable data outside Git under
[LARGE_FILES.md](../../../../../LARGE_FILES.md).

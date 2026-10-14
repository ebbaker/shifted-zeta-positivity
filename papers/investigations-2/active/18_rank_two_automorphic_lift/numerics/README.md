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

## Bounded stationary comparison, 14 October 2026

Prepared for Edward Baker with substantial LLM assistance by `gpt-6-astra`
(Codex), reasoning effort **ultra**. The
[matched checker](check_rank_two_matched_pilot_20261014.py) and
[small record](RANK_TWO_MATCHED_PILOT_RECORD_20261014.json) use python-flint
0.9.0 at 256 bits. The exact two cells, direct-source comparator and complete
omitted-mode/domain bounds are in
[note 2](../notes/2_MATCHED_STATIONARY_SIGNED_MODE_PILOT_20261014.md).

```sh
python3 -B check_rank_two_matched_pilot_20261014.py \
  --record /tmp/rank-two-matched-replay.json
```

The supplied baseline is hash-bound. Its normal location is
`investigations-2/brainstorm/numerics/MATCHED_STATIONARY_BASELINE_RECORD_20261014.json`;
if absent, the same `brainstorm/numerics/` relative path is tried under
`MATCHED_STATIONARY_ARCHIVES`. An explicit `--baseline PATH` still must
match the committed hash. `--tail-only` checks just the complete analytic
payments. The `--cell` option selects `j0`, `j1` or both.

Both finite signed cubatures exhausted the declared one-million-primitive
cap. The complete fallback intervals contain both signs; this is a recorded
bounded failure, not a positive-sign certificate. The direct-source baseline
certifies both targets at much smaller observed cost. Exit code zero means
the bounded experiment and record completed normally; it does **not** mean
the positivity gate passed. Inspect `positive_on_target`, the cubature stop
reason and the note before interpreting the record. The original Claude
checker and its diagnostic record remain historical evidence.

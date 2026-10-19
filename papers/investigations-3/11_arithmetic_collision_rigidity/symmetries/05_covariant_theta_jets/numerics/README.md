# S05 complete-source enclosure comparison

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance, **gpt-6.1-sol (Codex), actual effort ultra**. Outward Arb/Acb
computations and exact integer algebra; same-model internal review.

[check_covariant_source_enclosures.py](check_covariant_source_enclosures.py)
compares the existing expanded `source_jet(...,t=0)` with coefficient-combined
Horner evaluation and modular fixed-point Taylor evaluation of the complete
source and its first two **source** derivatives. Requires python-flint 0.9.0.

From the repository root, write fresh outputs outside the checkout:

```sh
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/05_covariant_theta_jets/numerics/check_covariant_source_enclosures.py --repo . --output /tmp/S05_SOURCE_192.json --bits 192 --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/05_covariant_theta_jets/numerics/check_covariant_source_enclosures.py --repo . --output /tmp/S05_SOURCE_256.json --bits 256 --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
```

Retained records:

- [192-bit comparison](S05_COMPLETE_SOURCE_ENCLOSURES_192_20261018.json).
- [256-bit comparison](S05_COMPLETE_SOURCE_ENCLOSURES_256_20261018.json).
- [Baseline algebra, signed-bridge, and control regression](S05_BASELINE_REGRESSION_20261018.json).

The local Taylor comparison passes for source orders 0,1,2 on
`[0,1/64]`, `[0,1/256]`, `[0,1/1024]`, including infinite mode tails and
eighth-derivative remainders. At the smallest cell, enclosing-radius ratios
against the actual expanded baseline exceed 894.47, 7.29, 2394.90.
Fused Horner is not uniformly tighter for the second derivative on the
shifted line; 34 of the 64 cells become wider.

The source bounds cover whole cells analytically. Overlap and point checks
are additional diagnostics. Endpoint odd zeros come from the known full
modular identity. The geometric tail theorem is proved in the [note][note];
the finite exact checks do not prove infinite modularity. Every point
coefficient and derivative-eight cell bound includes its complete tail.
Rounding stays inside the outward ball operations. There is no quadrature,
source-integral truncation, or physical whole-cell propagation in this task.

For the regression record, rerun these existing checkers to fresh paths:

```sh
python3 papers/investigations-3/11_arithmetic_collision_rigidity/numerics/check_hodge_modular_rotation.py --output /tmp/S05_LADDER.json
python3 papers/investigations-2/active/22_theta_manifold_geometry/numerics/check_theta_signed_bridge.py --output /tmp/S05_BRIDGE.json
python3 papers/investigations-3/11_arithmetic_collision_rigidity/numerics/replay_nonstationary_controls.py --repo . --receipts /tmp/S05_CONTROL_RECEIPTS --output /tmp/S05_CONTROLS.json --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
```

The combined retained regression record identifies this replay's actual
model/effort and embeds the original checker receipts. Their historical
authoring configurations are preserved and are not this replay's settings.
The five event rejections and separate Euler witness are existing
source-specific interface checks, not a new source-evaluator exclusion test.

Each comparison record pins its executing script and imported source files.
Hashes identify bytes; they do not prove the mathematics. Whole-run timings
are diagnostics, not matched-accuracy speedup measurements. The component
does not claim a smaller physical `H,Hx,Hxx` error or new coverage. A useful
spectral handoff remains unpaid; follow [the assessment][review]. All
retained files are below 1 MiB; no bulk derived data are generated.

[note]: ../notes/01_COMPLETE_SOURCE_JETS_AND_FIXED_POINT_ENCLOSURES_20261018.md
[review]: ../reviews/01_COMPLETE_SOURCE_ENCLOSURE_INTERNAL_REVIEW_20261018.md

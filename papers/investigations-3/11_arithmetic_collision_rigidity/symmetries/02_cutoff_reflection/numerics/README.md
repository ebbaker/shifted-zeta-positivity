# Reproduce the S02 bounded error comparison

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. **gpt-6.1-sol, actual reasoning effort ultra**. Internal
same-model derivation and review. Requires Python and python-flint 0.9.0.

The [note](../notes/01_ANALYTIC_CUTOFF_CORRECTION_AND_COMPLETE_JET_ERRORS_20261018.md)
proves the disk-error comparison. The two small records certify its scalar
and profile/transition bounds at 192/256 bits with identical fixed covers.
The exact analytic candidate is compared against the current absolute
payment and a matched absolute multiplier payment. No new noncollision
coverage or speed improvement is claimed.

Run from the repository root, using a fresh external output directory.
The optional complete-source reference must be generated at current source
pins, rather than bypassing validation of an older setup:

```sh
python3 papers/investigations-3/11_arithmetic_collision_rigidity/numerics/high_height_consumer/high_height_consumer.py --repo . --output-dir /tmp/s02-reference --bits 192 --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/02_cutoff_reflection/numerics/check_cutoff_reflection.py --repo . --reference-setup /tmp/s02-reference/SETUP.json --output /tmp/S02_192.json --bits 192 --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/02_cutoff_reflection/numerics/check_cutoff_reflection.py --repo . --reference-setup /tmp/s02-reference/SETUP.json --output /tmp/S02_256.json --bits 256 --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
python3 papers/investigations-3/11_arithmetic_collision_rigidity/numerics/replay_nonstationary_controls.py --repo . --receipts /tmp/s02-controls --output /tmp/S02_CONTROLS.json --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
```

Omit `--reference-setup` to reproduce the error-envelope comparison without
the separate complete-source point check. Both retained precision runs
use the same newly integrated 192-bit complete-source reference; the
256-bit run is an error-bound replay, not a second reference quadrature.
The fresh reference's setup and larger cell records stay outside the
repository under `LARGE_FILES.md`. The small S02 reports retain its hash,
source pins, midpoint enclosures and reproduction parameters.

The checker covers `[1/100,1/5] x [999,1001]` and the separate transition
test `[1/100,1/5] x [1017,1019]`. It fixes N=8 and disk radius 1/2, uses
768 and 8,192 rational closed rectangle cells respectively, pays the
published two-sum and corrected remainders, the nonholomorphic/analytic
correction mismatch, and the exact signed ninth-mode transition. All
maxima use outward upper endpoints. Cauchy supplies orders zero through
two at every real center; normalizer derivatives pay the physical return.

The records also check removable values by Taylor division, exact
normalization and multiplier identities, the profile derivative and
transition identity, and fixed-center analytic jet evaluation costs.
Those algebraic samples supplement the note's proofs. The fresh controls
use their own source errors; they do not validate a theta approximation
for an altered source. Read the [internal review](../reviews/01_CUTOFF_REFLECTION_INTERNAL_REVIEW_20261018.md)
for corrections made before the retained runs and the precise scope.

- [192-bit comparison](S02_CUTOFF_REFLECTION_192_20261018.json)
- [256-bit replay](S02_CUTOFF_REFLECTION_256_20261018.json)
- [Source-specific controls](S02_CONTROLS_20261018.json)

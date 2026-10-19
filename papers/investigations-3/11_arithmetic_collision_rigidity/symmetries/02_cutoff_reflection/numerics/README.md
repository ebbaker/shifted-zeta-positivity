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

## Matched frozen/full comparison, 19 October 2026

For Edward Baker with substantial LLM assistance, **gpt-6.1-sol, actual
reasoning effort ultra**. `compare_correction_representations.py` replays
the opening scalar/profile budgets and then shares the strongest corrected
published residual and Note 22 printed-jump edge payment between both
formulas. Only their fixed-N8 real versus complex continuation slopes
differ. It includes the signed physical normalizer/correlation return.
The original fixed covers and 192/256-bit choices are unchanged.

`S02_MATCHED_CORRECTION_20261019.json` records frozen eta
<0.226298331/<0.229588317 and matched full eta
<0.226299246/<0.229588635 on B/C. The earlier edge estimate improves the
old crossing 0.431777199 for both methods. This is an error-envelope
comparison, not evaluated whole-cell physical jets or new exclusion.
A separate reader's `S02_MATCHED_REVIEW_REPLAY_192_20261019.json` agrees.

With Python and python-flint 0.9.0, from the repository root:

```sh
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/02_cutoff_reflection/numerics/compare_correction_representations.py --repo . --output /tmp/S02_MATCHED_REPLAY.json --bits 192 256 --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/02_cutoff_reflection/numerics/check_correction_mechanism_guards.py --repo . --comparison-script papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/02_cutoff_reflection/numerics/compare_correction_representations.py --output /tmp/S02_MECHANISM_REPLAY.json --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/01_modular_self_duality/numerics/check_paired_consumer_controls.py --repo . --work-dir /tmp/S02_MATCHED_CONTROL_RECEIPTS --output /tmp/S02_MATCHED_CONTROL_REPLAY.json --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
```

The portable mechanism audit verifies normalizer derivatives against
analytic series, rejects omitted normalizer terms, checks physical and
D+pi/8 returns, and rejects five changed contract choices. It reproduces
`S02_MECHANISM_GUARD_AUDIT_20261019.json`. The reused portable source-control
checker freshly rebuilds five event enclosures and the Euler witness with
their own constants; its compact record is
`S02_MATCHED_CONTROLS_20261019.json`. Generated source receipts remain
external. The unchanged signed acceptance path is screened; the controls
do not certify the imported Polymath theorem or a new S02 physical consumer.

See [Note 02](../notes/02_MATCHED_FROZEN_AND_ANALYTIC_CORRECTIONS_20261019.md),
[internal review](../reviews/02_MATCHED_CORRECTION_INTERNAL_REVIEW_20261019.md),
and [saved identities](../reviews/S02_MATCHED_FILE_IDENTITIES_20261019.json).
The selected frozen center is held fixed during z derivatives; do not
obtain the family jets by differentiating its diagonal center-value map.

## Complete closed-cell jets, 19 October 2026

For Edward Baker with substantial LLM assistance, **gpt-6.1-sol, ultra**.
`evaluate_complete_frozen_jets.py` evaluates both exact approximants on the
fixed 32x128 B cover, adds complete disk errors and physical return costs,
pays frozen diagonal derivative defects, and rebuilds a complete-source
reference at each retained precision. `S02_COMPLETE_JETS_20261019.json`
contains32-slab summaries at 192/256 bits. The full per-cell tables exceed
5 MiB and are external; [ARCHIVES.md](../ARCHIVES.md) is the lookup and
regeneration guide with both stored and mathematical content hashes.

The primary paid firstjet radii are >0.9686625938 (frozen), >0.9702739184
(full) and >1.3473946960 (fresh additional-source reference). Both analytic
formulas pass all 4096 signed cells after retaining the joint real-Schur
second-jet residual class; independent frozen error boxes pass 1770 only.
This validates the old B domain and exports a complete interface, without
new coverage, C activation, timing claim or strongest-consumer advantage.
The full formula remains the coherent S03 residual interface.

`ClosedJetEvaluator.enclose` returns both local jet families and paid
metrics. Its frozen data carry explicit diagonal derivative defects;
`load_cell_archive` checks identities/pins before exposing rows. The small
`S02_COMPLETE_JET_REVIEW_REPLAY_192_20261019.json` is the separate reader's
fresh 192 replay; its canonical mathematical cell content matches the
primary 192 table exactly while observed header timing differs.

With Python and python-flint 0.9.0, from the repository root:

```sh
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/02_cutoff_reflection/numerics/evaluate_complete_frozen_jets.py --repo . --output /tmp/S02_COMPLETE_JETS_REPLAY.json --archive-dir /tmp/S02_JET_REPLAY --bits 192 256 --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/02_cutoff_reflection/numerics/check_complete_jet_controls.py --repo . --evaluator-script papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/02_cutoff_reflection/numerics/evaluate_complete_frozen_jets.py --work-dir /tmp/S02_T2_CONTROL_RECEIPTS --output /tmp/S02_T2_CONTROLS.json --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
```

The source-control reproducer challenges the NEW firstjet and Schur sign
helpers with five complete event balls and an Euler sign witness, never
with theta error constants. It also checks 12 exact Schur fixtures and
both diagonal derivative identities. Its saved output is
`S02_COMPLETE_JET_CONTROLS_20261019.json`. The separate
`check_jet_archive_integrity.py` command in the archive guide loads all
8192 primary table rows and challenges four fail-closed cases; the small
record is `S02_JET_ARCHIVE_CHECKS_20261019.json`.

[Note 03](../notes/03_COMPLETE_FROZEN_JETS_AND_PAID_CONSUMERS_20261019.md),
[Review 03](../reviews/03_COMPLETE_JET_INTERNAL_REVIEW_20261019.md),
[saved identities](../reviews/S02_COMPLETE_JET_FILE_IDENTITIES_20261019.json).

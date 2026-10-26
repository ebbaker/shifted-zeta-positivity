# N01 finite provider implementation and replay

26 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol, actual effort ultra**, recurrence chat0003. Python3.10.0,
standard library Fraction/arbitrary-precision int; no package installation.

- `gamma_provider.py`: branch-safe exact rational log/atan enclosures,
  shifted Stirling normalized gamma jets, delivered L1 error radii,
  producer and witness replay. The replayer shares finiteformula helpers
  but bypasses producer refinement/stopping choices.
- `gauss_provider.py`: exact integer Legendre variation counts, interval
  isolation, rational C13 weights and exact affine mapping. Local
  interval J/P' checks certify early stopping; global depth retained.
- `gauss_replay.py`: separately coded Rodrigues/sign/interval/output/
  mapping/moment checker. Shared Gauss premises remain shared.
- `n01_worker.py`: exact requested-input binding, finite JSON, source hash
  reporting, wall-time alarm and measured RSS limit. This Darwin runtime
  rejected resource-limit setup; the fallback is measured high-water RSS
  plus a sampling watchdog, not a hard address-space cap.
- `n01_run.py`: finite51-case matrix, separate-process replay,900second
  persistent total budget,60second child allocation, atomic conservative
  time reservations and preserved failure/inconclusive rows.
- `n01_negative_checks.py`: ten targeted rejection controls on already
  generated cases plus two positive controls. All computation is charged
  to the same supplied budget state.
- `n01_replay_archive.py`: source/data hash checks, documented archive
  lookup and separate-process replay of the 51 saved certificates.

See [the interpretation](../../notes/12_PROVIDER_IMPLEMENTATION_REPLAY_20261026.md),
[manifest](../01_PROVIDER_REPLAY_20261026.json), [assessment](../../reviews/10_PROVIDER_REPLAY_ASSESSMENT_20261026.md)
and [archive guide](../../ARCHIVES.md). No complete canonical field,
RS coefficient/retained-integral provider or physical certificate is
implemented by these modules. Runtime/operand observations are finite
measurements, not an asymptotic law or independent specialist validation.

## Actual sequence and failures

The initial worker failed before gamma import at resource-limit setup;
[its record](../01_N01_INITIAL_LIMIT_FAILURE_20261026.json) is preserved.
After a runner-only repair, the same frozen gamma source passed all 36
cases. A separate Gauss run passed all 15 bases/45maps. Targeted controls
passed, followed by the installed51-certificate archive replay. Total
computation was below 50.4055 seconds (rounded upward), including the failed
launch. No final matrix cell was capped or had a replay mismatch.

Preflight audit repaired explicit atan/pi child-kind binding, mathematical
input binding and capped-versus-delivered handling. Producer/replayer
checks consume actual witnesses rather than trusting stored status text.
Output radii, not reference-value agreement, establish the finite claims.

## Reproduce

From the repository root:

```sh
python3 papers/investigations-5/01_heat_density_asymptotics/recurrence/numerics/provider_replay/n01_run.py \
  --output-dir /private/tmp/hda-n01-regenerated \
  --record /private/tmp/hda-n01-regenerated-run.json \
  --budget-state /private/tmp/hda-n01-regenerated-budget.json
```

This creates all 36 gamma cases and 15 Gauss bases, each with a separate
replay process, preserving its finite caps. Do not reuse a budget state
from another question. Reruns against the same budget state retain spent
computation; an interrupted reservation is conservatively charged.
Each base Gauss certificate contains its three mapped rules. The gallery
of actual archived certificates is outside Git; the archive guide gives
its one lookup rule and hash-bound replay command. Runtime metadata can
change byte hashes; never bypass a byte mismatch against an old manifest.

The actual rejection controls used:

```sh
python3 papers/investigations-5/01_heat_density_asymptotics/recurrence/numerics/provider_replay/n01_negative_checks.py \
  --code-dir papers/investigations-5/01_heat_density_asymptotics/recurrence/numerics/provider_replay \
  --cert-dir /private/tmp/hda-n01-regenerated \
  --record /private/tmp/hda-n01-negative-checks.json \
  --budget-state /private/tmp/hda-n01-regenerated-budget.json
```

Primitive requested fractional bits are capped8192; larger exact temporary
operand lengths are separately measured. Gamma 4096 terms/shifts counts
C1/C3's expansion plus recurrence shifts, not all underlying elementary
series terms aggregated; each scalar series also has a 4096 term cap.
Gauss depth8192/query250000caps are unchanged. Capped records remain
incomplete evidence even if their failure-certificate replay succeeds.
Assertions must remain enabled; the worker rejects optimized Python.

# Recurrence external numerical evidence

26 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol, actual effort ultra**, recurrence chat0003. Follow the root
[LARGE_FILES.md](../../../../LARGE_FILES.md). Regenerable bulky data are
outside Git; source and small replay records are retained here.

## N01 finite provider certificates

The [execution manifest](numerics/01_PROVIDER_REPLAY_20261026.json) lists
all 51 files under `output/n01/`, their individual byte sizes/SHA-256 and
canonical-content SHA-256. Total3645034bytes; largest 201229bytes. They
are the 36 gamma and 15 Gauss base certificates; the latter contain 45
mapped rules and 558 moment diagnostics. The actual final replay is in
[the installed replay record](numerics/01_N01_INSTALLED_ARCHIVE_REPLAY_20261026.json).

Maintainer reading copy:
`/Users/Shared/szp-archive/heat-density-recurrence/numerics-archives/`.
The manifest paths are relative to that archive root. This local path is
a convenience, not a mathematical dependency or a public download URL.
Copy the archive files from the maintainer or regenerate them below.

Lookup is strictly: `recurrence/numerics/<manifest certificate path>`,
then `<HDA_RECURRENCE_ARCHIVES>/<manifest certificate path>`. The reader
fails closed on missing data or a byte-hash mismatch. It never downloads
or silently accepts differently generated data. No third-party material
is archived here.

Canonical mathematical-content hashes remove only top-level observational
`metrics` (gamma) or `stats` (Gauss), then hash sorted compact JSON. They
retain source metadata, finite witnesses, centers and error radii. This
allows timing/RSS changes to be distinguished from changed proof data;
it does not promise cross-Python-version portability. Actual archived
replay checks byte hashes before mathematical inequalities.

## Replay

Use the recorded Python environment (3.10.0 in this run), standard library
only. From the repository root:

```sh
export HDA_RECURRENCE_ARCHIVES=/Users/Shared/szp-archive/heat-density-recurrence/numerics-archives
python3 papers/investigations-5/01_heat_density_asymptotics/recurrence/numerics/provider_replay/n01_replay_archive.py
```

The consumer first checks its listed source hashes and each file's byte
hash, then runs the independent finite replay actions with a 900 second
total bound and 60 second child allocation. Each child checks measured
peak RSS against 512 MiB. No hard OS address-space cap is claimed where
the runtime rejects that facility. A capped record is not counted as
a delivered case. This is software/premise consistency replay, not
independent specialist validation or a field evaluator.

## Regeneration

Generate a new comparison copy, preserving the existing archive:

```sh
python3 papers/investigations-5/01_heat_density_asymptotics/recurrence/numerics/provider_replay/n01_run.py \
  --output-dir /private/tmp/hda-n01-regenerated \
  --record /private/tmp/hda-n01-regenerated-run.json \
  --budget-state /private/tmp/hda-n01-regenerated-budget.json
```

The finite matrix/caps are frozen in [N01 r1](research-progress/handoffs/HDA-R05-N01.md).
Regenerated timestamps/RSS observations change byte hashes. Compare the
manifest's canonical-content hash with the same stated exclusion rule;
then replay the new witnesses. Do not overwrite a different original
certificate or bypass the original manifest's byte-hash check. A changed
mathematical content hash requires investigation and a new evidence
record. The [source/commands guide](numerics/provider_replay/README.md)
describes producer and replayer roles, limits and failed launch.

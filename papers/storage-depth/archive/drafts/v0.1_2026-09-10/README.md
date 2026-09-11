# Cumulative storage and residual-controlled depth extension

Research draft 0.1, 10 September 2026. Start with
[the manuscript source](manuscript/storage_depth.tex) or its compiled PDF,
then [CONTINUATION.md](CONTINUATION.md).

The main result is the full-domain quarter-step residual inequality
R* F^-1 R <= 0.9 H_J for the original rational 128-to-32 continuation, extended
by zero on the old complement. A 256-plus-32 verification head and analytic
bounds control both infinite-dimensional complements. The same matrices give
a separate absolute central floor 1e-33. The global-method floor 1e-31 at
depth 1.98 is also retained.

These statements use the working Weil-depth v0.3 normalization. The author's
normalization verification and independent review remain open. There is no
all-depth theorem or unrestricted cumulative certificate at shift 1e-11.

## Contents

- manuscript/: editable LaTeX and compiled PDF.
- CONTINUATION.md: mathematical state, remaining obligations, next experiment.
- CLAIMS.json: precise scopes and record mapping.
- numerics/history/: five original research packets, unchanged, except omitted
  bytecode and the three external matrix files.
- numerics/replay.py: supported verification and regeneration entry point.
- numerics/archive_io.py: two-location lookup and dual-hash verification.
- numerics/ARCHIVE_RECORDS.json: stored-file and canonical matrix-content hashes.
- numerics/HISTORY_RECORD.json: SHA-256 for every immutable historical file.
- reference/weil-depth-v0.3/: inherited manuscript source and bibliography.
- reference/large_files_policy_github.json: provenance for the size policy.
- validation/: checks performed while assembling this package.
- ARCHIVES.md: external layout, hashes, and regeneration commands.
- BUILD_RECORD.json and SHA256SUMS.txt: small deliverables only.

The dated notes are chronological snapshots. Older notes describe gaps that
later packets address; use the manuscript and CONTINUATION.md for current status.

## Environment

Recorded: Python 3.10.0, python-flint 0.9.0 (FLINT 3.6.0), mpmath 1.4.1.
From this paper directory:

    python3.10 -m venv .venv
    .venv/bin/python -m pip install -r requirements.txt
    .venv/bin/python numerics/replay.py verify

In the commands below, python means this environment's interpreter.
Keep assertions enabled: no -O and no PYTHONOPTIMIZE. A different platform or
arithmetic library may produce different matrix-content hashes. Proof signs
must be checked arithmetically, not inferred from matching hashes.

## Replays

Results go to a **new** folder. The runner refuses to overwrite an existing
output folder. These examples use an ignored directory; an external results
folder is preferable for full builds.

    python numerics/replay.py checks --output-dir numerics/replays/checks
    python numerics/replay.py generator --output-dir numerics/replays/generator
    python numerics/replay.py storage --output-dir numerics/replays/storage
    python numerics/replay.py residual --output-dir numerics/replays/residual
    python numerics/replay.py whole-step --output-dir numerics/replays/whole-step
    python numerics/replay.py global --output-dir numerics/replays/global
    python numerics/replay.py new-slab --output-dir numerics/replays/new-slab

With the external spatial archive configured as described in ARCHIVES.md:

    python numerics/replay.py verify --archives
    python numerics/replay.py spatial-sign --output-dir numerics/replays/spatial-sign
    python numerics/replay.py relative --output-dir numerics/replays/relative
    python numerics/replay.py shift --output-dir numerics/replays/shift

The runner verifies all historical files and both external-data hashes before
staging inputs. It runs unchanged historical code in a temporary copy and
exports changed results, logs, hashes, and parameters. Historical records remain
untouched. The spatial-sign action uses a small new validator to recompute the
guarded absolute Schur inequality. The relative action executes the original
validator with theta=0.9.

Historical README commands document the original investigation. For external
data use the supported runner, which adds verified lookup and staging without
changing source hashes. Do not invoke historical archive consumers directly as
an alternative external-data interface.

A successful process exit alone is not a positivity certificate: inspect each
result's PASS/FAIL and domain scope. The rebuild-initial action intentionally
retains the unsuccessful historical sufficient criterion.

## Build and integrate

    make pdf

This requires a standard LaTeX installation with latexmk and the packages named
in the source (TeX Live 2023 used here). The manuscript includes its bibliography;
no external images, downloads, or shell escape are required.

Copy papers/storage-depth/ into the intended checkout, retaining .gitignore,
ARCHIVES.md, and the small hash records. Run the repository's LARGE_FILES.md size
check before committing. Never commit either delivery ZIP, external matrices,
the environment, or generated replay data. No third-party paper PDFs are included.
The original reference builder and v0.3 source remain pinned to the recorded commit.

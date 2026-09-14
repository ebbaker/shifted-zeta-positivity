# Working manuscript: positive factorizations of Weil forms

Version 0.2, 11 September 2026. Prepared for Edward Baker, on branch
`susy-positivity`. This folder now holds the positive-factorizations attempt
within the [SUSY positivity research program](../../README.md). The
[shared background](../../background.pdf) and [program overview](../../PROGRAM_OVERVIEW.md)
state the common goals; this manuscript explores one approach.

Start with [the manuscript PDF](manuscript.pdf), the
[companion brief](RESEARCH_BRIEF.md), or the latest
[round-3 manuscript investigation](INVESTIGATION_round3.md). The
[status ledger](STATUS.md) distinguishes proved statements, computation,
and open construction problems.

Round 3 adds an explicit factor for the complete central **odd** gamma
sector through the prime-free slab, and an exact example showing that the
first prime stabilizes a negative gamma direction. The proposed positive
remainder after extracting an independent prime-edge square fails. The even
sector and a joint positive first-prime construction remain open. The later
[round-4 review](archive/progress-reports/REVIEW_round4_20260911.md) extends
the odd factor across shifts and reduces the even question to one scalar;
those results remain separate from manuscript v0.2.

## Contents

- `manuscript.tex` and `manuscript.pdf`: proofs and compiled reading copy.
- `RESEARCH_BRIEF.md`: motivation and current direction.
- `INVESTIGATION_round3.md`: latest results, failed trials, and next target.
- `STATUS.md`: statement-level verification and remaining review.
- `checks/round1/` and `checks/round2/`: original checkers and historical outputs.
- `checks/round3/`: rational certificates and separate identity diagnostics.
- `archive/drafts/`: historical manuscript PDF.
- `archive/progress-reports/`: round-4 derivations, review, and executable reproduction notes.
- `archive/provenance/`: original manifest retained as a historical record.
- `manifest.json`: current file hashes and separately labelled historical validation.
- `../../REORGANIZATION_20260912.md`: fresh relocation and build verification.

## Build

From this directory, with a standard TeX distribution:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error manuscript.tex
```

The source uses common LaTeX packages and an embedded bibliography. The
author line says “Working draft prepared for Edward Baker”; it does not
assert approval for submission.

## Reproduce the checks

With Python 3 and NumPy, without Python `-O`:

```sh
python3 checks/replay.py --output-dir replay-results
```

The replay runner copies the original checkers into a temporary directory,
runs all three full checks and both round-4 programs, and saves fresh output
in the requested new directory. It refuses an existing output directory.
Historical `checks/round*/diagnostics.json` files are preserved. Direct full
invocation of an original checker writes beside that checker; use the replay
runner for routine verification. To run only the round-3 rational certificates
without changing the recorded full diagnostics:

```sh
python3 checks/round3/check_round3.py --certificate-only
```

The exact sign certificates use Fraction arithmetic with proved truncation
bounds. The remaining calculations are floating-point identity diagnostics.
The round-3 checker imports the round-2 rational helpers by a path relative
to its source, so all commands can also be invoked from another directory.
No zeta-zero archive or external matrix data is required.

## Before wider circulation

This is a working draft. Independent specialist proof review, domain review,
and a fuller literature/priority audit remain outstanding. No global
positivity mechanism, RH proof, or interacting superspace field theory is
claimed. Version 0.1 was prepared outside the repository and imported at
`4de517e`; version 0.2 continues that investigation here.

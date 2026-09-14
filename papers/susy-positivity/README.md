# SUSY positivity research program

The objective is to explain the nonnegativity of the full central Weil
quadratic form on every smooth compactly supported input, at arbitrary
support length. The program seeks independently defined positive structures
and exact arithmetic identities that would establish this target. The
shifted transfer family supplies a related contraction route.

Start with the **[mathematical background PDF](background.pdf)** and the
**[program overview](PROGRAM_OVERVIEW.md)**. They explain the common goals,
normalization, domains, and distinction between established identities and
proposed constructions. The [continuation note](brainstorm/continuation-notes/CONTINUATION_BULK_BOUNDARY_SUPERSPACE_20260912.md)
records the latest discussion of bulk–boundary models and possible superspace
descriptions.

The full arithmetic bulk completion remains open. The concrete positive
auxiliary-field construction for the **gamma kinetic term** is established
within its stated scope. It does not include
the remaining normalization, pole, and prime contributions. No all-length
positivity theorem or RH proof is claimed.

## Current investigations

| Investigation | Scope and status |
|---|---|
| [Positive factorizations](investigations/positive-factorizations/README.md) · [manuscript PDF](investigations/positive-factorizations/manuscript.pdf) · [status](investigations/positive-factorizations/STATUS.md) | Working manuscript v0.2: short-window full factors, the gamma kinetic tower, restricted odd-sector factors, obstructions to specified models, and a certified first-prime stabilization example. Later [round-4 reports](investigations/positive-factorizations/archive/progress-reports/REVIEW_round4_20260911.md) extend the odd factor across shifts and isolate the remaining even scalar. A complete even factor, joint prime construction, and arbitrary-length mechanism remain open. Independent specialist and priority review remain outstanding. |
| [Topological SUSY bulk](investigations/topological-susy-bulk/README.md) · [manuscript PDF](investigations/topological-susy-bulk/manuscript.pdf) · [status](investigations/topological-susy-bulk/STATUS.md) | Positive relative gamma complex, arithmetic loop responses, and scoped correction obstructions. Later quantum notes give a physical Fock realization and stronger finite-block restrictions; the complete arithmetic norm remains open. |
| [Arithmetic ground-state geometry](investigations/arithmetic-ground-state-geometry/README.md) · [manuscript PDF](investigations/arithmetic-ground-state-geometry/manuscript.pdf) · [research report](investigations/arithmetic-ground-state-geometry/REPORT.md) · [status](investigations/arithmetic-ground-state-geometry/STATUS.md) | Four-supercharge cylinder and interacting prime theories, exact physical Euler-factor dependence, and scoped metric, period and ground-transform obstructions. Develops the [theory landscape](brainstorm/theory-landscape-20260913/REPORT.md); the physical source normalization, contact, poles and complete Weil pairing remain open. |

These investigations are approaches toward the program's goals. Their local results
and later reports retain their length, shift, and input restrictions; they
do not settle the shared global target.

## Organization and future investigations

The program root holds shared background, the roadmap, and continuation
context. `background_section.tex` is the authoritative substantive TeX
section; `background.tex` supplies the standalone wrapper and bibliography
and inputs that section. `background.pdf` is its compiled reading copy.

Place each future approach in `investigations/<descriptive-name>/`, alongside
`positive-factorizations/`. Give it a README stating the proposed mechanism,
scope, status, and relation to the shared framework. Keep its manuscript,
checks, manifests, progress reports, and historical drafts inside that
investigation. Link to shared background rather than keeping another authoritative
copy. Add a row above when an investigation is ready to be listed; distinguish
proved results, numerical evidence, and proposed constructions.

## Build and verification

From this directory, using a standard TeX distribution:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error background.tex
(cd investigations/positive-factorizations && latexmk -pdf -interaction=nonstopmode -halt-on-error manuscript.tex)
```

The [positive-factorizations README](investigations/positive-factorizations/README.md) gives a
replay command that preserves historical diagnostics. The
[reorganization record](archive/REORGANIZATION_20260912.md) records the old-to-new
mapping, fresh verification, and provenance; current hashes and historical
validation are identified separately.

# Build and preserve the manuscript pair

The two entry points are [manuscript.tex](manuscript.tex) and
[supplementary-information.tex](supplementary-information.tex).
They compile independently and share only local formatting and bibliography
files. Neither loads the program's shared background or a parent investigation.
A usual TeX Live installation with latexmk, pdfLaTeX, Latin Modern,
AMS packages, microtype, hyperref, etoolbox and TikZ suffices.

From this directory:

    latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build manuscript.tex
    latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build supplementary-information.tex
    cp build/manuscript.pdf manuscript.pdf
    cp build/supplementary-information.pdf supplementary-information.pdf
    python3 validation/drafts.py check --replay

The last command verifies the recorded sources and both PDFs. Editing any
input or rebuilding a different PDF makes the record stale until a new build
has actually been reviewed and recorded. A rebuild can change metadata bytes
without changing the mathematics.

## A new reviewed version

Resolve undefined references, overflow warnings and layout defects, and
inspect every rendered page of both documents. For example:

    pdftoppm -r 110 -png build/manuscript.pdf build/main-page
    pdftoppm -r 110 -png build/supplementary-information.pdf build/supplement-page
    python3 validation/drafts.py record --date YYYY-MM-DD --pages N --supplement-pages M --review-note 'Describe the actual visual review of both documents.'
    python3 validation/drafts.py save YYYY-MM-DD-vNN
    python3 validation/drafts.py check --replay

Record checks both TeX dependency closures, source modification times,
build logs, page counts, matching version numbers, and identities of the
delivered PDFs. [BUILD_RECORD.json](BUILD_RECORD.json) retains the main
document fields and a companion record. The checker continues to accept the
schema-1 records of historical single-document versions without rewriting
them.

Save refuses to overwrite an existing snapshot. It includes both PDFs,
both entry points, all their TeX inputs, this guide, the portable validator,
diagnostic programs and records, and [source provenance](MANUSCRIPT_SOURCES.json).
A saved directory can be copied elsewhere and built without this repository.
Preserve historical snapshots unchanged; rebuild only a copy.

A visual-review note attests to a completed inspection. Neither it nor a
matching hash is evidence of mathematical correctness.

## Diagnostics and the live inventory

The three standard-library programs contain 268 diagnostics. Replay checks
the same parameters, named cases, thresholds and passing inequalities,
allowing small differences in floating values. The reflected-junction program
imports matrix helpers from the included endpoint program. None of the
diagnostics proves the physical realization hypothesis or an RH claim.

After recording and archiving, update the broader live inventory:

    python3 validation/check_package.py refresh
    python3 validation/check_package.py check

Refresh replays the diagnostics and writes their records before inventorying
the package. If the runtime changes diagnostic bytes, review the results
and update the live build record as well; never rewrite a historical snapshot.
The live checker pins inherited research inputs outside this package and is
not part of the portable snapshot.

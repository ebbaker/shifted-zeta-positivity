# Build and preserve the manuscript

The entry point is [manuscript.tex](manuscript.tex). All its TeX inputs are
inside this package. It does not load the program's shared background or
any parent investigation. A usual TeX Live installation with `latexmk`,
pdfLaTeX, Latin Modern, AMS packages, microtype, hyperref and TikZ suffices.

From this directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build manuscript.tex
cp build/manuscript.pdf manuscript.pdf
python3 validation/drafts.py check --replay
```

The final command verifies the recorded source/PDF pair. After modifying
sources or rebuilding a different PDF, the old record should fail until a
new build has actually been reviewed and recorded. A rebuilt PDF can have
different metadata bytes without a mathematical change.

For a new release, resolve all undefined references, overflow warnings and
layout defects, and inspect every rendered page. For example:

```sh
pdftoppm -r 110 -png build/manuscript.pdf build/page
python3 validation/drafts.py record --date YYYY-MM-DD --pages N --review-note 'Describe the visual review actually completed.'
python3 validation/drafts.py save YYYY-MM-DD-vNN
python3 validation/drafts.py check --replay
```

`record` checks the TeX dependency closure, source modification times, build
log and identity of the delivered PDF. It binds those sources and the
supporting diagnostics in [BUILD_RECORD.json](BUILD_RECORD.json). A review
note attests to a completed human or model visual inspection; it is not
generated evidence of mathematical correctness.

`save` refuses to overwrite an existing snapshot and includes every TeX
input, the PDF, this guide, the portable validation tool, numerical programs
and their records, and the [source provenance](MANUSCRIPT_SOURCES.json).
The saved directory can be copied elsewhere and compiled without this
repository. Preserve historical snapshots unchanged; rebuild only a copy.

The three standard-library programs contain 268 diagnostics. Replay checks
the same parameters, named cases, thresholds and passing inequalities,
allowing small differences in floating values. The reflected-junction
program imports matrix helpers from the endpoint program, which is included.
These checks do not prove interacting positivity or an RH claim.

In the live repository, after recording and archiving a release, update the
broader notes inventory with `python3 validation/check_package.py refresh`.
That live checker also verifies inherited research files in adjacent
investigations. It is deliberately not part of the portable snapshot;
`validation/drafts.py` provides the standalone build and diagnostic checks.

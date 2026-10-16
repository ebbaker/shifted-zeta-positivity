# Building and preserving the working manuscript

The current [PDF](manuscript.pdf) is built from [manuscript.tex](manuscript.tex),
the files in `sections/`, and [references.tex](references.tex). Every equation
reference is internal to this manuscript. It does not input or rely on the
numbering of the shared susy-positivity background.

From this directory, using a standard TeX distribution:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build manuscript.tex
cp build/manuscript.pdf manuscript.pdf
```

Inspect the final log for undefined citations, references and overfull boxes.
Render and review the PDF pages, especially long equations, tables and page
breaks. The ignored `build/` directory is for temporary build files. Rendering
images and other large temporary outputs belong outside the tracked package.

## Recording a reviewed build

After checking the actual PDF, update the current build record. For example,
replace the date, page count and review note below with the reviewed values:

```sh
python3 validation/drafts.py record --date YYYY-MM-DD --pages N --review-note "Description of the completed visual review"
python3 validation/drafts.py check --replay
```

The record command reads `\draftversion` from the TeX source and records hashes
of the current sources, PDF, build guide, validation tool and algebra checks.
It also checks that the PDF agrees with the build output and that the build
log contains no unresolved references or overflow warnings. It cannot perform
visual or mathematical review: the review note must describe work actually done.
PDF metadata may differ across TeX installations; hashes identify the reviewed
files rather than promising a byte-identical PDF rebuild everywhere.

## Saving a new draft

Before revising the current draft, ensure its reviewed version has a snapshot.
Update the version and date in `manuscript.tex` for a new version. After building,
reviewing and recording it, save an unused date-and-version directory name:

```sh
python3 validation/drafts.py save YYYY-MM-DD-v02
python3 validation/drafts.py check --replay
```

The save command refuses to overwrite an existing directory. It copies the
complete buildable manuscript, PDF, build record, validation tool and the four
algebra programs with their preserved records, and writes `SNAPSHOT.json`.
Add the new version to the live `drafts/README.md` index. Preserve older versions
unchanged. Compile an archived version in a separate working copy so that its
historical files remain untouched.

The `check` command verifies current file hashes, all archived snapshot hashes,
and that the manuscript's local TeX dependencies stay inside its package.
`--replay` additionally runs the four current algebra programs and compares the
resulting JSON with their preserved records. It does not certify proofs,
operator domains, a QFT construction or Weil positivity.

All deliverable files must remain below the repository's 1 MiB limit. No
third-party PDFs or rendered page images belong in a snapshot.

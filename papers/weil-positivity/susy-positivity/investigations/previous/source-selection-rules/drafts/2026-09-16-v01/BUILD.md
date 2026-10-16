# Building the manuscript

From this directory:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build manuscript.tex
cp build/manuscript.pdf manuscript.pdf
```

The build must produce no undefined references, no multiply-defined labels and
no overfull boxes; `validation/drafts.py record` refuses a build whose log shows
any of them, and refuses a `manuscript.pdf` that differs from `build/manuscript.pdf`.

Recording a build asserts that a human or a reviewing session has actually
looked at the rendered pages:

```sh
python3 validation/drafts.py record --date YYYY-MM-DD --pages N \
  --review-note "what was checked visually"
python3 validation/drafts.py save YYYY-MM-DD-vNN
python3 validation/drafts.py check --replay
```

`save` refuses to overwrite an existing snapshot. `check --replay` re-runs every
program in the `CHECKS` dictionary and requires its output to equal the
preserved record. The `build/` directory is ignored by git; delete it after a
review.

The manuscript does not input any shared background file. It is self-contained
apart from the companion manuscript of this program, which it cites for the
program's objective and for results quoted by number.

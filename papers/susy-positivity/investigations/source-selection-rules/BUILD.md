# Building, recording and snapshotting the manuscript

## What the two artefacts are for

**`BUILD_RECORD.json` is not meant to be read for content.** It is a provenance
record: a set of SHA-256 hashes pinning one particular PDF to the exact sources,
check programs and records that produced it, together with the page count, the
engine banner, the build command, and a free-text note asserting that someone
actually looked at the rendered pages. Its only job is to fail later. If any
`.tex` file, check program or preserved record changes after the record is
written, `validation/drafts.py check` reports exactly which file drifted, which
tells you the `manuscript.pdf` sitting on disk no longer corresponds to its
sources. That is the whole of it. There is nothing in the file to inspect by eye
beyond `version`, `pages` and `visual_review`.

**`validation/drafts.py` is the tool that writes and enforces it.** Three
commands:

| Command | What it does | What it refuses |
|---|---|---|
| `check [--replay]` | Verifies the record against the files, and every archived snapshot. With `--replay`, re-runs every program in `CHECKS` and requires byte-identical output. | Any drifted file, any snapshot that has been edited, any check whose output changed. |
| `record --date --pages --review-note` | Writes `BUILD_RECORD.json`. | A build log with undefined or multiply-defined references or overfull boxes; a page count differing from the log; a `manuscript.pdf` differing from `build/manuscript.pdf`; a source file newer than the PDF; an empty review note. |
| `save NAME` | Copies a complete standalone package into `drafts/NAME`. | Overwriting an existing snapshot; a name that is not `YYYY-MM-DD-vNN`; any file over 1 MiB. |

The `--review-note` is the one thing the tool cannot verify. It is a human (or
reviewing-session) assertion that the rendered pages were looked at, and it is
stored verbatim so that a later reader knows what was and was not checked.

## The workflow

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build manuscript.tex
cp build/manuscript.pdf manuscript.pdf
# ---- now actually look at the rendered pages ----
python3 validation/drafts.py record --date YYYY-MM-DD --pages N \
  --review-note "what was checked visually"
python3 validation/drafts.py save YYYY-MM-DD-vNN
python3 validation/drafts.py check --replay
```

If `check` reports `Changed recorded file: .../manuscript.tex`, that is the
normal state after editing: the record describes the previous build. Rebuild,
re-review and re-record.

The `build/` directory is ignored by git; delete it after a review. The
manuscript inputs no shared background file; it is self-contained apart from the
companion manuscript of this program, which it cites for the program's objective
and for results quoted by number.

# Building and preparing the review drafts

The installed preprint folder has two entry points:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build manuscript.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build derivations.tex
```

Both read `preamble.tex` and `references.tex`. The checked PDFs are `manuscript.pdf` and `derivations.pdf`. After an edit, inspect the final build log for undefined references and overfull boxes, render the new PDFs, and replace the root PDFs only with the checked versions. `SOURCE_RECORD.json` identifies the original investigation; `VALIDATION.json` describes the current reviewed build and inspection, not future edits. The pre-revision build record is preserved with both older drafts in drafts/2026-09-13-before-review-revisions/.

For a future arXiv source upload, the main TeX entry point is `manuscript.tex`. Include its two shared source files. The separate derivation PDF can be supplied in an `anc/` directory, with a clear reference in the final manuscript and the archival release. The companion's editable TeX may remain in the repository/DOI archive. Keep review notes and build intermediates out of the main source upload, and verify the actual preview produced by arXiv before finalizing any submission.

Before a submission proposal is finalized, complete the human review record, resolve the novelty comparison, replace the draft author line, update the AI disclosure to describe the review actually completed, and insert the supplied version-specific archive DOI. The draft presently cites the locally verified source commit. No DOI, author affiliation, independent review, or publication status has been invented.

No upload, release, git commit or submission was performed as part of preparing this folder.


The response to the Codex review is in reviews/response_20260913.md. The original review and its original check results are preserved. To reproduce the review computations and the checks specific to the revisions, use Python 3 with NumPy:

    python3 reviews/check_review_20260913.py
    python3 reviews/check_revision_20260913.py

Both print JSON to standard output. The recorded rerun on the revised sources is reviews/review_replay_after_revision_20260913.json; the additional checks are recorded in reviews/revision_check_results_20260913.json. Exact rational checks and floating-point diagnostics are explicitly distinguished. These are not arithmetic Schur positivity certificates and do not complete the human review log.

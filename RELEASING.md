# Releasing

A release is a git tag that the Zenodo–GitHub integration turns into an
archived snapshot with a version DOI. Because the whole tree is archived,
release only when everything committed is fit to be permanent — and note that
this includes the working-draft folders under `papers/`: a tag archives them
as drafts. Their `STATUS.md` must be current at tag time, and the GitHub
release notes must say which folders are *released* (citable as manuscripts)
and which are drafts.

## Before the first release (once)

1. Enable the repository in Zenodo (zenodo.org → GitHub → toggle this repo).
2. Check the root `.zenodo.json` validates (Zenodo rejects malformed metadata
   and the archive silently fails): `python3 -c "import json; json.load(open('.zenodo.json'))"`.
   Do not put placeholder DOIs in `related_identifiers`.
3. Check the author metadata: ORCID `0000-0001-5459-9993` and the contact
   e-mail are in both `CITATION.cff` files and both `.zenodo.json` files (done
   9 Sept 2026); the preprint `.tex` carries the e-mail.
4. Create the issue labels from `.github/labels.yml`; enable Discussions if wanted.

## For each release `vX.Y`

1. **Gate.** Every paper folder *being released* in this tag has passed the
   release checklist in `papers/README.md`; every folder that stays a working
   draft has a current `STATUS.md` saying so. Every note committed has a row in
   `notes/REDACTION_CHECKLIST.md`. Code present has passed its gate in
   `code/README.md`. `blueprint/` and `statements/ledger.yaml` are current.
2. **Changelog.** Add the `vX.Y` section to `CHANGELOG.md`.
3. **Build check.** The `build-latex` workflow is green; the committed PDF
   matches the source (page count at minimum).
4. **Tag and release.** `git tag -a vX.Y -m "…" && git push --tags`, then
   create the GitHub release from the tag. Attach the released PDFs as release
   assets (convenience for readers; Zenodo archives the source tree, not the
   assets).
5. **Zenodo (repository record).** Wait for the archive to appear; copy the
   *version* DOI and the *concept* DOI.
6. **Zenodo (paper records).** For each paper released for the first time in
   this tag: new upload, type *publication / preprint*, attach the PDF, paste
   the metadata from `papers/<slug>/.zenodo.json`, add related identifier
   `isPartOf` → the repository version DOI. Publish; copy the paper DOI.
7. **Link back.** Edit the repository record on Zenodo: related identifier
   `hasPart` → each paper DOI. Add the same to the root `.zenodo.json` so the
   next release carries it automatically.
8. **Paste DOIs.** Into `papers/README.md` citation blocks, the paper folder's
   `README.md` and `CITATION.cff` (`doi:` field), the README DOI badge.
   Commit as bookkeeping — this does not need a new Zenodo version.
9. **Announce** with the paper DOI (journal-style) and the repository version
   DOI (for the verification material).

## Version numbering

`vMAJOR.MINOR` for the repository. A paper's own version (e.g. "preprint
v1.0", "v1.1") is stated in its PDF and `CITATION.cff` and need not coincide
with the repository tag; the citation names both.

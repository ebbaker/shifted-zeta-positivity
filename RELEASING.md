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
   and archiving can fail). `python3 -m json.tool .zenodo.json` checks JSON
   syntax only; it does not validate Zenodo's metadata schema. Inspect the
   GitHub integration's result in Zenodo after release and resolve any reported
   metadata errors there. Do not put placeholder DOIs in
   `related_identifiers`. Check both `CITATION.cff` files against the official
   CFF 1.2.0 schema with `tools/check_citations.py` (the `check-first-slab`
   workflow does this on every push that touches them).
3. Check the author metadata: ORCID `0000-0001-5459-9993` in both
   `CITATION.cff` files and both `.zenodo.json` files, and the contact e-mail
   in the READMEs and CFF author records. The preprint `.tex` also carries
   the e-mail; Zenodo creator records need not contain it.
4. Create the issue labels from `.github/labels.yml`; enable Discussions if wanted.

## For each release `vX.Y`

1. **Gate.** Every paper folder *being released* in this tag has passed the
   release checklist in `papers/README.md`; every folder that stays a working
   draft has a current `STATUS.md` saying so. Every note committed has a row in
   `notes/REDACTION_CHECKLIST.md`. Code present has passed its gate in
   `code/README.md`. `blueprint/` and `statements/ledger.yaml` are current.
   The root `.zenodo.json` description and the READMEs describe the tree as it
   will be at the tag — in particular which code is and is not present.
2. **Changelog.** Add the `vX.Y` section to `CHANGELOG.md`.
3. **Build check.** The `build-latex` workflow is green; the committed PDF
   matches the source. The existing workflow checks compilation and a
   hard-coded page count; it does not compare the committed PDF's contents
   against the newly compiled one. Inspect the built artifact or adopt a
   normalized text comparison before asserting source/PDF correspondence.
   Run the stable numerical and CFF checks in `check-first-slab.yml` too;
   those are diagnostics and metadata checks, not a proof certificate.
4. **Tag and release.** `git tag -a vX.Y -m "…" && git push --tags`, then
   create the GitHub release from the tag. Attach the released PDFs as release
   assets (convenience for readers; Zenodo archives the source tree, not the
   assets).
5. **Zenodo (repository record).** Wait for the archive to appear; copy the
   *version* DOI and the *concept* DOI.
6. **Zenodo (paper records).** For each paper released for the first time in
   this tag: new upload, type *publication / preprint*, attach the PDF, paste
   the metadata from the paper folder's `.zenodo.json`, add related identifier
   `isPartOf` → the repository version DOI. Publish; copy the paper DOI.
7. **Link back.** Edit the repository record on Zenodo: related identifier
   `hasPart` → each paper DOI. Add the same to the root `.zenodo.json` so the
   next release carries it automatically.
8. **Paste DOIs.** Put the paper DOI in `preferred-citation.doi` in both CFF
   files and the manuscript citation blocks. Put the repository version DOI
   in the root CFF's top-level `doi` only if it identifies that outer record.
   Update `papers/README.md`, the paper README and the DOI badge accordingly.
   Commit as bookkeeping — this does not need a new Zenodo version.
9. **Announce** with the paper DOI (journal-style) and the repository version
   DOI (for the verification material).

## Version numbering

`vMAJOR.MINOR` for the repository. A paper's own version (e.g. "preprint
v1.0", "v1.1") is stated in its PDF and `CITATION.cff` and need not coincide
with the repository tag; the citation names both.

The root `CITATION.cff` version (currently `0.2.0`) is the repository version:
set it, and `date-released`, to the tag when creating it. Zenodo's GitHub
import reads the root `.zenodo.json` in preference to `CITATION.cff`, so the
release description lives there; a paper folder's `.zenodo.json` is never read
automatically and is used by hand when creating that paper's own deposit
(step 6 above).

# Large files — what stays out of git, and how

This repository is archived whole at every release tag (Zenodo takes the tag's
tree), it is meant to be cloned by verifiers and formalizers, and its history
should stay small enough that a clone is quick. Git therefore holds **sources
and small records** — LaTeX, code, PDFs, JSON certificates, hashes, notes — and
**no large derived data**. This file states the convention and the procedure
that goes with it. The worked instances are [Weil-depth](papers/shifted-zeta/weil-depth/ARCHIVES.md)
(about 122 MB of ball matrices) and [storage-depth](papers/shifted-zeta/storage-depth/ARCHIVES.md)
(about 1.6 GB across six recorded matrix archives). Their tracked guides
describe the data and any availability limits.

## 1. The convention

1. **Size.** Every committed file stays below about 1 MB. The largest tracked
   files today are compiled PDFs of 350–700 KB. Anything larger needs a reason
   written into the commit message, and anything above 5 MB is not committed
   at all. (GitHub warns at 50 MB and refuses files above 100 MB; long before
   that, history bloat is the real cost, because a blob committed once stays
   in every clone forever.)
2. **Regenerable data is not versioned.** Output that committed code
   regenerates deterministically from committed parameters — ball-matrix
   archives, Gram matrices, zero caches beyond a few hundred KB, sweep
   outputs, review-package ZIPs — is kept outside the repository. What *is*
   committed is everything needed to (a) regenerate it, (b) recognise it
   when regenerated, and (c) use it when someone has a copy: the generating
   script and its parameters, a **small record** carrying the data's hashes
   (for the Weil paper: `central_certificate.json`, `enclosure.json`), and a
   **tracked guide** that says where the data goes and how it is fetched.
3. **Two hashes when the data are structured.** Record both the hash of the
   file as stored (`matrix_archive_sha256`: identifies one exact `.gz`) and a
   *content hash* of the canonical serialization of the data, independent of
   timestamps, ordering and compression (`matrices_content_sha256`). The
   second lets a rebuild be recognised as the same object without the
   original file. State honestly what a matching hash establishes: identity
   of the data in the environments where it was tested, not bit-for-bit
   portability of the arithmetic across libraries and versions; and never
   let a proof step depend on a hash — sign tests are decided by the
   arithmetic on whatever matrices are present.
4. **Hash-bound replay.** Scripts that consume an external file check its hash
   against the committed record before using it (`analyze_certificate.py`
   refuses a mismatched archive) and fail closed when the file is absent,
   with a message that says how to regenerate it.
5. **One lookup rule.** Scripts look for a missing file first at its normal
   place in the tree, then at the same relative path under a directory named
   by an environment variable (`WEIL_ARCHIVES` for the Weil paper; use
   `<PAPER>_ARCHIVES` for a new paper). Nothing else — no hard-coded paths to
   the author's machine, no download URLs baked into code.
6. **Third-party material.** PDFs of papers by other authors are never
   committed, whatever their size (`references/README.md`); they are cited.
7. **Not Git LFS, not a cloud drive.** Both were considered and rejected:
   LFS objects are not part of the tarball GitHub hands to Zenodo, so a
   release would silently omit them while appearing complete; LFS adds
   quota, cost and a second failure mode for every clone; and a shared-drive
   link rots. Regenerable data plus hashes in the tree is complete and
   verifiable on its own. If a *non-regenerable* large dataset ever enters
   the program (measured data, an irreproducible external computation), it is
   deposited as its own Zenodo *dataset* record before release and linked
   from the root `.zenodo.json` by related identifier — never committed and
   never left on a drive.

## 2. Where the data live

Outside the repository, in `szp-archive/`, which mirrors the paper layout.
The maintainer's current archive root is `/Users/Shared/szp-archive`; it need
not be adjacent to the checkout. Set the two lookup variables as follows
(adjust the paths for your own copy):

```bash
export WEIL_ARCHIVES=/Users/Shared/szp-archive/weil-depth/numerics-archives
export STORAGE_DEPTH_ARCHIVES=/Users/Shared/szp-archive/storage-depth/numerics-archives
```

Historical draft snapshots retain the old archive name; resolve their paths
under the same paper subdirectory of `szp-archive`.

```
shifted-zeta-positivity/                     ← the git clone
szp-archive/                                ← not a git repository
└── <paper-slug>/
    └── numerics-archives/
        ├── README.md          copy of papers/<slug>/ARCHIVES.md (the tracked one is canonical)
        ├── SHA256SUMS.txt     every file below, `sha256sum` format, relative paths
        └── <same relative paths as under papers/<slug>/numerics/ …>
```

For the Weil paper this is `szp-archive/weil-depth/numerics-archives/`,
with `output/<horizon>_N128/central_matrices.json.gz` and so on; the full
list with sizes and hashes is in `papers/shifted-zeta/weil-depth/ARCHIVES.md`. The folder
may be moved or copied anywhere; scripts reach it through the environment
variable, and its integrity is checked with `sha256sum -c SHA256SUMS.txt` from
inside it.

Inside the repository each paper that has such data carries:

* `papers/<slug>/ARCHIVES.md` — the tracked guide: expected layout, per-file
  size and SHA-256, how to regenerate, how to request, how to point the
  scripts at a copy, and what the hashes do and do not establish;
* a `.gitignore` in the paper folder excluding the archive directory name and
  the file patterns (`numerics-archives/`, `numerics/output/**/*.json.gz`),
  so a copy placed inside the tree for convenience is never committed; the
  root `.gitignore` excludes `numerics-archives/` everywhere as a backstop;
* the small records with the hashes, and the `BUILD_RECORD.json` /
  `SHA256SUMS.txt` of the paper's committed deliverables (which list only
  tracked files, never the external data).

## 3. Procedure

### Adding a large derived file (new horizon, new paper, new experiment)

1. Confirm it is regenerable: the committed script, with the parameters that
   will be committed, must produce it without manual steps. If not, stop and
   treat it under rule 7 above.
2. Make the generating script write the **small record** beside the data with
   both hashes and the run parameters, and make every consumer check the hash
   (rules 3–4).
3. Move the file out: `mv papers/<slug>/numerics/output/<run>/<file>
   /absolute/path/to/szp-archive/<slug>/numerics-archives/output/<run>/<file>`
   (create directories as needed; keep the relative path identical).
4. Refresh the archive folder's manifest from inside that folder:
   `find . -type f ! -name SHA256SUMS.txt ! -name README.md ! -name .DS_Store -print0 | sort -z | xargs -0 sha256sum > SHA256SUMS.txt`
   and check it: `sha256sum -c SHA256SUMS.txt`.
5. Add the file's row (path, where it belongs in the tree, size, SHA-256) to
   `papers/<slug>/ARCHIVES.md`, and copy that file over the archive folder's
   `README.md`.
6. Make sure git ignores it: `git check-ignore -v <path-in-tree>` must print a
   matching rule. If it prints nothing, add the pattern to the paper's
   `.gitignore` first.
7. If the paper has a `SHA256SUMS.txt` / `BUILD_RECORD.json`, regenerate them
   from tracked files only (they must not list the external data).
8. Before committing, run the size check in §4. Then commit the small record,
   the guide and the ignore rule — never the data.

### Starting a paper that will have large data

Create `papers/<slug>/.gitignore` and `papers/<slug>/ARCHIVES.md` with the
first data file, not later; give the loader a `locate()` with the
environment-variable fallback (copy `certify_arb.locate` from the Weil
paper's `numerics/certify_arb.py`); name the variable `<PAPER>_ARCHIVES` and
document it in the paper's README and `ARCHIVES.md`.

### Supplying the data to a reviewer

Send the archive folder (or the needed subfolder) with its `SHA256SUMS.txt`
and README; the reviewer verifies the manifest, then either copies the tree
into `numerics/output/` or sets the environment variable. Point them at the
regeneration commands too — a rebuild that matches the content hash is the
stronger check.

### If a large file was committed by mistake

* **Not yet pushed:** `git rm --cached <file>`, add the ignore rule, amend
  the commit. The blob is gone once it is unreferenced and garbage-collected.
* **Pushed to a topic branch:** remove it in a new commit so the tree is
  clean, and merge the branch into `main` with `--squash` so that `main`'s
  history never references the blob; then delete the branch on GitHub and
  locally, and let GitHub's garbage collection reclaim the objects. (Force
  pushing a rewritten branch is also acceptable on a branch nobody else has
  based work on.)
* **Pushed to `main`:** the only repair is a history rewrite
  (`git filter-repo --path <file> --invert-paths`) followed by a force push
  and a note in `CHANGELOG.md`; every clone must be re-cloned. Avoid reaching
  this case — see §4.

**Current state (11 September 2026).** `finite-horizon-weil` was already
squash-merged into `main` as `76b0d32`; its remote topic branch has been
deleted. A stale local copy can still retain its old large blobs, so it must
not be merged into `main` again. The five `critical_path` commits introduce
no blob over 1 MiB and can be merged normally. The main-tree and main-history
size checks remain required. No history rewrite is part of this closeout.

## 4. The pre-commit size check

Run before every commit (or wire it into a pre-commit hook):

```bash
# files staged for commit larger than 1 MB, with sizes in KB
git diff --cached --name-only --diff-filter=AM -z | xargs -0 -r du -k 2>/dev/null | awk '$1 > 1024 {print}'
# any blob in the current tree above 1 MB
git ls-files -z | xargs -0 du -k | awk '$1 > 1024' | sort -rn
# any blob anywhere in history above 1 MB (what a clone actually downloads)
git rev-list --objects --all | git cat-file --batch-check='%(objecttype) %(objectsize) %(rest)' \
  | awk '$1=="blob" && $2>1048576 {printf "%8.1f MB  %s\n", $2/1048576, $3}' | sort -rn
```

An empty result from the first two commands is the expected state. The third
command is what to run before tagging a release.

## 5. What a release archives

A Zenodo release archives the tag's tree and nothing else. Under this
convention that is complete: the tree contains the code, the parameters, the
hashes and the guide, so the archived record lets anyone regenerate the data
and confirm it is the same object. The release notes and the paper's
`STATUS.md` should say which data are external and where the guide is
(`RELEASING.md`, gate step 1). A non-regenerable dataset gets its own Zenodo
dataset record (rule 7) so that the release still identifies every input.

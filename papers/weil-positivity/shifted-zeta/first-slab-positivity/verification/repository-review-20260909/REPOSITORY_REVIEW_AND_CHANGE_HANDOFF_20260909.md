# Repository review and proposed changes

**Repository:** [ebbaker/shifted-zeta-positivity](https://github.com/ebbaker/shifted-zeta-positivity)  
**Reviewed snapshot:** [`50cb4d22c0fc8dd06430070a46e9a3d1f2e76689`](https://github.com/ebbaker/shifted-zeta-positivity/tree/50cb4d22c0fc8dd06430070a46e9a3d1f2e76689)  
**Prepared:** 9 September 2026  
**Delivery:** this Markdown handoff and `REPOSITORY_CHANGES_20260909.zip`.

## Assessment

The repository is a useful foundation for a preprint archive. Its manuscript
folders, statement inventory, verification ledger and explicit working-draft
labels give readers a clear route through the research. Keeping the licenses
at the repository root is appropriate when their scope is stated clearly.

The main corrections concern reproducibility, citation metadata and the
distinction between material currently present and material planned for
release. The supplied patch addresses those issues without changing the
manuscript's mathematical claims or marking pending human checks complete.
It has not been pushed to GitHub, and no release or DOI has been created.

This is a repository and reproducibility review, not a new proof audit.
Findings refer to the snapshot above; later repository changes must be
reconciled before applying the patch.

## Findings and supplied fixes

| Finding | Change supplied |
|---|---|
| The root description promised Arb certificates, but `code/certificates/first-slab/` contained a placeholder subject to D1–D5. | README and Zenodo description now distinguish public scripts from the unreleased certificate. Recovered certificate files are supplied separately for review. |
| The paper's CFF file used invalid top-level `type: generic`. The original root CFF passed the schema check. | Both CFF files now provide an explicit `preferred-citation` for the preprint. The paper's outer source descriptor uses a valid top-level type. A schema checker and CI job are included. |
| Example DOIs and descriptions of future deposits could be mistaken for completed deposits. Root source version `0.2.0` and manuscript `1.0` were not clearly distinguished. | The principal citation blocks use the reviewed commit until an actual DOI is supplied; release and manuscript versions are explained separately. The patch does not invent or automatically bump either version. |
| The license notice linked to the Creative Commons homepage, and “dual license” could suggest either license applies to every file. | Root `LICENSE` links to the specific CC BY 4.0 deed and legal code, preserves the full MIT text, and states that licenses apply by material type. |
| The notes index described reports not yet present in `notes/`. | Root and notes READMEs identify the research-log migration as planned. |
| “No error survives” overstated what internal reviews establish. | Two verification documents now say no unresolved error was identified in those internal reviews, while retaining the pending checks. |
| The historical A4 numerical implementation produced unstable matrix and Laplace checks; its printed failures were not a reliable CI exit status. | A separate, stable diagnostic script integrates the singular kernel, tests quadrature and mesh consistency, avoids overflow in the Laplace integral, and returns a failing status when a check fails. The historical scripts remain available. |
| Existing CI built PDFs but did not run these numerical or CFF checks. | An additional GitHub Actions workflow runs the new diagnostics and citation-schema checks. Release instructions explain what the PDF build does and does not establish. |

The CFF changes follow the [official CFF 1.2.0 schema](https://citation-file-format.github.io/1.2.0/schema.json): top-level types are `software` and `dataset`; a manuscript reference can be placed under `preferred-citation`. Here the outer record indexes source material and the preferred reference identifies the preprint. The outer root record's MIT license describes software; the paper and text remain CC BY 4.0 under `LICENSE`.

The root `.zenodo.json` remains a publication-oriented record for the mixed
research archive. Its description now states the software license separately.
Zenodo's GitHub import prioritizes that file over root CFF metadata; subfolder
metadata must be used explicitly for a separate paper deposit. JSON parsing
alone is not Zenodo metadata validation. See [Zenodo's JSON metadata guide](https://help.zenodo.org/docs/github/describe-software/zenodo-json/).

The supplied licensing clarification implements the requested MIT/CC BY 4.0
split; it does not change the existing copyright owner. See the
[CC BY 4.0 deed](https://creativecommons.org/licenses/by/4.0/).

## What is in the ZIP, and where it belongs

| Bundle path | Intended use or destination |
|---|---|
| `repository-fixes.patch` | Apply at the repository root; includes the proposed repository changes only. |
| `repository-files/` | The same new and replacement files, arranged in their exact repository-relative paths. This is an alternative to applying the patch. |
| `certificate-candidate/` | Recovered generators, audit, inherited support code, result tables, pins and provenance. Review first; eventual destination is `code/certificates/first-slab/`. |
| `validation/` | Logs supporting this handoff, including an explicitly dated historical regeneration record. Selected final logs can later accompany the certificate release. |
| `SHA256SUMS` | Hash manifest for the handoff bundle, excluding itself. The certificate candidate also has its own manifest. |
| This handoff | Keep with the review correspondence; optionally place under `notes/repository-review/` if you want to publish it as a dated repository review. |

The overlay changes root `README.md`, `LICENSE`, `CITATION.cff`,
`.zenodo.json` and `RELEASING.md`; the notes index; the first-slab paper's
README, CFF and verification-status document; and the first-slab checklist
and script README. It adds:

- `verification/first-slab/scripts/verify_stable_volterra_20260909.py`;
- `verification/first-slab/scripts/requirements_stable_checks.txt`;
- `tools/check_citations.py`;
- `environment/requirements_metadata.txt`;
- `.github/workflows/check-first-slab.yml`.

The existing PDFs, LaTeX sources, historical scripts and statement ledger are
not replaced. The second-slab working material is outside this change bundle.

## Applying the repository changes

Unzip the bundle outside your repository. In a clean checkout of your
repository, review and apply the patch; substitute your actual extracted path:

```bash
git status --short
git apply --stat /path/to/REPOSITORY_CHANGES_20260909/repository-fixes.patch
git apply --check /path/to/REPOSITORY_CHANGES_20260909/repository-fixes.patch
git apply /path/to/REPOSITORY_CHANGES_20260909/repository-fixes.patch
git diff --check
git diff
git status --short
```

`git diff` does not display newly added untracked files until they are staged;
inspect those files too using the paths shown by `git status`. If the initial
working tree is not clean, preserve its existing work before applying. If the
patch check fails because the repository has changed, reconcile the affected
files rather than forcing the patch.

Alternatively, review and copy the files from `repository-files/` to the same
relative locations. Use one method. Do not copy the entire handoff folder
into the public repository: the certificate candidate and historical notes
still need review.

Run the new checks locally with CPython 3.12:

```bash
python3.12 -m venv .venv-review
.venv-review/bin/python -m pip install -r verification/first-slab/scripts/requirements_stable_checks.txt -r environment/requirements_metadata.txt
.venv-review/bin/python verification/first-slab/scripts/verify_stable_volterra_20260909.py
curl --fail --show-error --location https://citation-file-format.github.io/1.2.0/schema.json --output /tmp/cff-1.2.0-schema.json
.venv-review/bin/python tools/check_citations.py --schema /tmp/cff-1.2.0-schema.json
```

The dependency files pin direct dependencies. They are not complete operating
system or transitive-dependency locks. The new workflow uses the same direct
pins; its hosted GitHub execution has not been observed because these changes
have not been pushed.

## Validation and its limits

The new numerical script passed **16/16 checks** locally. Its finite-section
reflection identities agree to approximately `6e-17` or better; doubled
quadrature and refined-mesh compression discrepancies are below `9e-13`.
The four high-precision Laplace comparisons pass the stated `1e-25` tolerance.
An injected `0.001` error makes the script return status 1, so failures can
actually fail CI. Logs are included in `validation/`.

The finite-section calculation uses integrated piecewise-constant Galerkin
elements rather than samples of the singular kernel near zero. It checks
shifts `0.3` and `0.5`, using 16 and 32 cells and 48/96-node quadrature.
The Hankel and Volterra matrices share scalar integrals but use different
index rules; their reflection checks test coordinate consistency. They are
not independent reconstructions of the kernel. The sampled matrix norms
below one are **not a proof of the infinite-dimensional operator bound or
of the whole shift interval**.

The historical script's partial log records passing A1–A3 and coercivity
checks, with failures in A4 and its floating-point Laplace integration. A
nominal zero on the Hankel anti-diagonal can become approximately `1e-16`,
causing a singular kernel sample to explode. Its float impulse also overflows
on the unbounded Laplace integration range. The recorded run was stopped
after 180 seconds during the later exploratory Suzuki-normalization section;
it was not a completed successful run. The new script does not replace that
section or certify Suzuki's normalization chain.

Both proposed CFF files passed the official 1.2.0 schema. Applying the same
validator to the original snapshot passed root CFF and rejected the paper's
`type: generic`, returning status 1. The corrected `.zenodo.json` parses as
JSON; acceptance by a live Zenodo deposit is still to be checked.

The recovered certificate tables passed their supplied structural verifiers:
724 primary rows, 90 diagnostic rows, 783 audit rows and 1,360 matrix rows.
The four result-file hashes match those listed in the supplied **5 September
2026** regeneration record. That record reports full primary, diagnostic
and audit regeneration in its pinned environment; this packaging task reran
the stored-table checks, not those complete computations.

At the reviewed snapshot, all six jobs in the existing
[PDF build run](https://github.com/ebbaker/shifted-zeta-positivity/actions/runs/34302194428)
succeeded. Those jobs check compilation and page counts. They do not establish
that the committed PDFs match the compiled artifacts, and they do not validate
the mathematics.

## Remaining decisions before archiving

1. **Certificate release:** resolve the existing D1–D5 requirements before
   integrating `certificate-candidate/`. Its README identifies inherited
   analytic assumptions, stale passages in historical notes, and explicit
   reproduction commands. Packaging is not evidence that those reviews are
   complete.
2. **Research logs:** migrate only the intended, reviewed notes and update
   the index and manifest to describe what is actually committed.
3. **Versions and metadata:** choose the actual repository release version;
   update root CFF and the Zenodo description to match that tagged tree. Keep
   the manuscript version distinct. No GitHub release was present in the
   reviewed state; no DOI has been supplied here or independently established
   for a separate paper deposit.
4. **Release evidence:** run the new workflow after integrating the changes,
   inspect the compiled PDFs, and confirm Zenodo's imported metadata and
   material-specific license description. Add actual DOIs to the correct
   paper or repository citation fields after deposit.

The remaining mathematical review work is still described by the repository's
checklist, particularly the functional-analysis steps, Suzuki normalization,
novelty boundary and inherited tail bounds. This handoff improves how readers
can inspect and reproduce the work; it does not add a new proof claim.

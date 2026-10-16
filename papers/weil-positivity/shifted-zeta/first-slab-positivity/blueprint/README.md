# Blueprint: first-slab positivity

A *blueprint* here is a statement inventory for a released paper: every
definition, lemma, proposition and theorem, stated self-contained (all
notation unpacked), with

- **depends on** — the statements it uses, as a dependency graph;
- **proof status** — `paper` (proved on paper in the manuscript), `computer`
  (certified by interval arithmetic), `numeric` (verified numerically only,
  not proved), `cited` (taken from the literature), `asserted` (stated with
  a sketch or with unproved estimates);
- **human check** — whether a human has verified it line by line, and who;
- **formalization** — an honest estimate of how feasible a Lean 4 / Mathlib
  formalization is today, with the specific obstacles.

The markdown files are the precursor of a
[leanblueprint](https://github.com/PatrickMassot/leanblueprint) project: each
entry maps onto one `\begin{theorem}…\uses{…}\leanok\end{theorem}` block, and
the dependency graph is the one leanblueprint would draw. When a
formalization starts, `src/` is created here in that format and the
markdown becomes its rendered view.

This folder holds the first-slab inventory, [statements.md](statements.md)
(30 statements, `fs:S01` …), and the same inventory as machine-readable
YAML, [ledger.yaml](ledger.yaml) (one record per statement, same ids).

## Conventions

- Ids are `<paper-slug>:<Snn>`; the first slab uses `fs:S01` …
- Equation and section numbers refer to the released PDF version named at
  the top of each file.
- "Human check" records the checklist item id from
  [`../verification/CHECKLIST.md`](../verification/CHECKLIST.md) and the state ⬜ / 🔶 / ✅.
- Formalization feasibility scale: **easy** (a Mathlib afternoon), **moderate**
  (days; the objects exist in Mathlib), **hard** (weeks; missing library),
  **certificate** (a computer-certified fact that would be formalized by a
  verified checker of stored certificate data), **out of reach** (the
  surrounding theory is not in Mathlib).

## Other papers

Only the first-slab preprint (v1.0, released) has an inventory; the
statements formalizable now are `fs:S02`, `fs:S07`, `fs:S16` (polynomial
part), `fs:S19`, `fs:S29` and `fs:S30`. A blueprint is written when a paper is
released (or earlier if a formalizer asks for one), as release checklist
item 4, in a `blueprint/` folder inside that paper's folder. The statement ids
for the shifted-zeta drafts will be `pm:` (psi-omega-margin), `os:`
(omega-string), `dd:` (defect-depth) and `rd:` (rh-detector); Weil-depth and
storage-depth ids will be assigned when their inventories are written. Until
then each draft's `STATUS.md` carries its result-by-result verification
record: see [Weil-depth](../../weil-depth/STATUS.md) and
[storage-depth](../../storage-depth/STATUS.md) with its
[claim records](../../storage-depth/CLAIMS.json). For the rh-detector, the
pencil theorem (Wilson's formula) and the two elementary lemmas would be
natural first entries.

## Machine-readable ledger

`ledger.yaml` mirrors `statements.md` one record per statement, with the same
ids. It exists so that scripts, dashboards, or a future leanblueprint project
can read the status of every claim without parsing prose.

Fields per statement: `id`, `name`, `type`, `where` (equation/section in the
released PDF), `status` (`paper | computer | numeric | cited | asserted`),
`depends_on` (ids or external ids), `human_check` (`state`, checklist `item`,
`note`), `formalization` (`feasibility`, `note`), and, for computer-certified
statements, the `certified_constants` as strings (never as floats — they are
enclosure endpoints or midpoints and must not be re-rounded).

Validate with `python3 -c "import yaml; yaml.safe_load(open('ledger.yaml'))"`
from this folder. Update both the YAML and `statements.md` at every release; a
verification report that closes an item changes `human_check.state` there and
the corresponding row here.

Moved here on 16 October 2026 from the repository-root `blueprint/` and
`statements/` folders (`statements/README.md` is the section above); see the
[relocation record](../../../../REORGANIZATION_20261016.md).

[First-slab preprint](../README.md) · [Shifted-zeta program](../../README.md) · [All papers](../../../../README.md)

# Blueprint

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
formalization starts, `blueprint/src/` is created in that format and the
markdown becomes its rendered view.

The same inventory is available as machine-readable YAML in
`../statements/ledger.yaml` (one record per statement, same ids).

## Conventions

- Ids are `<paper-slug>:<Snn>`; the first slab uses `fs:S01` …
- Equation and section numbers refer to the released PDF version named at
  the top of each file.
- "Human check" records the checklist item id from
  `../verification/<paper>/CHECKLIST.md` and the state ⬜ / 🔶 / ✅.
- Formalization feasibility scale: **easy** (a Mathlib afternoon), **moderate**
  (days; the objects exist in Mathlib), **hard** (weeks; missing library),
  **certificate** (a computer-certified fact that would be formalized by a
  verified checker of stored certificate data), **out of reach** (the
  surrounding theory is not in Mathlib).

## Papers

| Paper | File | Statements | Formalizable now |
|---|---|---|---|
| first-slab-positivity v1.0 (released) | `first-slab/statements.md` | 30 | `fs:S02`, `fs:S07`, `fs:S16` (polynomial part), `fs:S19`, `fs:S29`, `fs:S30` |
| psi-omega-margin (working draft) | — | not yet inventoried | release checklist item 4; the paper's `STATUS.md` has a result-by-result verification record in the meantime |
| omega-string (working draft v5) | — | not yet inventoried | same |
| defect-depth (working draft v1) | — | not yet inventoried | same |
| rh-detector (working draft; separate thread) | — | not yet inventoried | same; the pencil theorem (Wilson's formula) and the two elementary lemmas would be natural first entries |

A blueprint is written when a paper is released (or earlier if a formalizer
asks for one): the statement ids for the drafts will be `pm:`, `os:`, `dd:`,
`rd:`.

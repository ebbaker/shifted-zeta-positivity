# Statement ledger (machine-readable)

`ledger.yaml` mirrors the markdown blueprints in `../blueprint` one record per
statement, with the same ids. It exists so that scripts, dashboards, or a
future leanblueprint project can read the status of every claim without
parsing prose.

Fields per statement: `id`, `name`, `type`, `where` (equation/section in the
released PDF), `status` (`paper | computer | numeric | cited | asserted`),
`depends_on` (ids or external ids), `human_check` (`state`, checklist `item`,
`note`), `formalization` (`feasibility`, `note`), and, for computer-certified
statements, the `certified_constants` as strings (never as floats — they are
enclosure endpoints or midpoints and must not be re-rounded).

Validate with `python3 -c "import yaml; yaml.safe_load(open('statements/ledger.yaml'))"`.
Update both the YAML and the markdown blueprint at every release; a
verification report that closes an item changes `human_check.state` here and
the corresponding row there.

[Shifted-zeta program](../papers/shifted-zeta/README.md) · [All manuscripts](../papers/README.md)

#!/usr/bin/env python3
"""Compose cited records from named canonical homes into ignored build output."""
from pathlib import Path
import json
import re
import subprocess
import sys

paper = Path(__file__).resolve().parent
repo = Path(subprocess.check_output(
    ["git", "-C", str(paper), "rev-parse", "--show-toplevel"], text=True
).strip())
inv5 = repo / "papers/investigations-5"
tnd = inv5 / "08_theta_observables_newman_dynamics"
op = tnd / "03_operator_imaginary_time_evolution"
og = op / "01_green_potential_resolvent"
sources = [
    paper.parent / "references/manuscript_sources.bib",
    paper.parent / "01_riemann_siegel_evolution/references/riemann_siegel_execution_sources.bib",
    tnd / "references/internal_sources.bib",
    op / "references/manuscript_internal_sources.bib",
    op / "references/riemann_siegel_sources.bib",
    og / "references/manuscript_sources.bib",
    og / "references/green_resolvent_sources.bib",
    op / "02_localized_zero_correlations/references/localized_comparison_sources.bib",
    inv5 / "01_heat_density_asymptotics/references/references.bib",
    inv5 / "07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/references/references.bib",
    inv5 / "06_auxiliary_collision_flows/references/sources.bib",
    inv5 / "07_positive_theta_primitives/references/sources.bib",
    op / "references/localized_statistics_sources.bib",
]
explicit_owners = {
    "Angenent1991": inv5 / "06_auxiliary_collision_flows/references/sources.bib",
    "Csordas2014PositiveKernels": inv5 / "07_positive_theta_primitives/references/sources.bib",
    "MaplesRodgers2015": op / "references/localized_statistics_sources.bib",
}
tex = "\n".join(p.read_text() for p in [paper / "main.tex", *sorted((paper / "sections").glob("*.tex"))])
cited = set()
for group in re.findall(r"\\cite\w*\*?(?:\[[^\]]*\])*\{([^}]+)\}", tex):
    cited.update(k.strip() for k in group.split(","))
records, origins = {}, {}
for path in sources:
    for m in re.finditer(r"(?ms)^@\w+\{([^,\s]+),.*?(?=^@\w+\{|\Z)", path.read_text()):
        key, record = m.group(1), m.group(0).rstrip()
        if key not in cited:
            continue
        if key in explicit_owners and path != explicit_owners[key]:
            continue
        if path in explicit_owners.values() and key not in explicit_owners:
            continue
        if key in records and records[key] != record:
            raise ValueError(f"Conflicting canonical records for {key}: {origins[key]} and {path}")
        records[key] = record
        if key == "Csordas2014PositiveKernels":
            records[key] = record.replace(
                "references/01_ANNOTATED_BIBLIOGRAPHY_20261031.md",
                "the canonical Investigation07 reference catalog",
            )
        origins[key] = str(path.relative_to(repo))
missing = cited - records.keys()
if missing:
    raise ValueError("Missing cited records: " + ", ".join(sorted(missing)))
destination = Path(sys.argv[1]).resolve()
if not destination.is_relative_to((repo / "output/pdf").resolve()):
    raise ValueError("Generated bibliography belongs under output/pdf.")
destination.parent.mkdir(parents=True, exist_ok=True)
destination.write_text("% Generated composition: edit canonical records.\n\n" + "\n\n".join(records[k] for k in sorted(records)) + "\n")
destination.with_suffix(".origins.json").write_text(json.dumps(origins, indent=2, sort_keys=True) + "\n")
print(f"Composed {len(records)} cited canonical records.")

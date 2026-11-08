#!/usr/bin/env python3
"""Compose a build-only bibliography from the canonical repository records."""
from pathlib import Path
import re
import subprocess
import sys

paper = Path(__file__).resolve().parent
repo = Path(subprocess.check_output(
    ["git", "-C", str(paper), "rev-parse", "--show-toplevel"], text=True
).strip())
inv5 = repo / "papers/investigations-5"
external = inv5 / (
    "07_positive_theta_primitives/01_jensen/01_mellin_curvature/"
    "11_energy_filtered_theta_overlaps/references/references.bib"
)
parent = paper.parent.parent / "references/internal_sources.bib"
local = paper.parent / "references/manuscript_internal_sources.bib"
collision = inv5 / "06_auxiliary_collision_flows/references/sources.bib"

def entries(path):
    """Entries in these canonical files begin at column zero."""
    source = path.read_text()
    return {
        match.group(1): match.group(0).rstrip()
        for match in re.finditer(
            r"(?ms)^@\w+\{([^,\s]+),.*?(?=^@\w+\{|\Z)", source
        )
    }

selected = {}
for path, wanted in [
    (external, ("CamporesiHiguchi1996", "DLMFThetaModular", "RodgersTao2020")),
    (parent, ("TNDDirectCollision",)),
    (local, ("OperatorProof", "OperatorAssessment", "OperatorCollision",
             "HeatMultiplicity", "SourceResponse", "RTLocalTransfer",
             "SmoothLocalizationProof", "SmoothLocalizationAssessment",
             "GaussianLaguerreProof", "GreenStripProof",
             "LocalizedMetricsAssessment", "MetricComparison",
             "PrimeBaselineAssessment", "DLMFGreenPrime")),
    (collision, ("Angenent1991",)),
    (paper.parent / "references/complex_statistics_sources.bib",
     ("Montgomery1973", "BGST2024", "GLSS2026", "RudnickSarnak1996", "KiKimLee2009")),
    (paper.parent / "references/localized_statistics_sources.bib",
     ("MaplesRodgers2015", "Rodgers2017Tails", "Caceres2026Collision")),
    (inv5 / "02_heat_flow_rh_applications/references/sources.bib",
     ("Polymath2019",)),
    (inv5 / "07_positive_theta_primitives/references/sources.bib",
     ("Csordas2014PositiveKernels",)),
]:
    records = entries(path)
    for key in wanted:
        if key in selected:
            raise ValueError(f"Duplicate bibliography key: {key}")
        selected[key] = records[key]
        if key == "Csordas2014PositiveKernels":
            selected[key] = selected[key].replace("references/01_ANNOTATED_BIBLIOGRAPHY_20261031.md", "the canonical Investigation07 reference catalog")

destination = Path(sys.argv[1]).resolve()
output_root = (repo / "output/pdf").resolve()
if not destination.is_relative_to(output_root):
    raise ValueError("The composed bibliography belongs in ignored output/pdf.")
destination.parent.mkdir(parents=True, exist_ok=True)
destination.write_text(
    "% Build-only composition; edit the canonical records, not this file.\n\n"
    + "\n\n".join(selected.values()) + "\n"
)
print(f"Composed {len(selected)} cited records: {destination}")

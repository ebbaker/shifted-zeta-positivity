#!/usr/bin/env python3
"""Compose the manuscript bibliography from its canonical repository records."""
from pathlib import Path
import re
import subprocess
import sys

paper = Path(__file__).resolve().parent
repo = Path(subprocess.check_output(
    ["git", "-C", str(paper), "rev-parse", "--show-toplevel"], text=True
).strip())
inv5 = repo / "papers/investigations-5"
parent = paper.parent.parent
external = inv5 / (
    "07_positive_theta_primitives/01_jensen/01_mellin_curvature/"
    "11_energy_filtered_theta_overlaps/references/references.bib"
)
sources = [
    (external, ["DLMFThetaModular"]),
    (parent / "references/manuscript_internal_sources.bib",
     ["GreenStripProof", "SmoothLocalizationProof", "LocalizedMetricsAssessment",
      "PrimeBaselineAssessment", "DLMFGreenPrime"]),
    (paper.parent / "references/green_resolvent_sources.bib",
     ["Radziwill2012MollifyingV3"]),
    (parent / "02_localized_zero_correlations/references/localized_comparison_sources.bib",
     ["Tao2020LocalZeros", "Tao2016Harnack", "DLMFReciprocalGammaOC"]),
    (paper.parent / "references/manuscript_sources.bib",
     ["OGParent", "OGConditioning", "OGMollifier", "OGCorrection",
      "OGAssessment", "OGBoundaryLog", "OGAssembly", "OGControls"]),
]
selected = {}
for path, wanted in sources:
    records = {
        m.group(1): m.group(0).rstrip()
        for m in re.finditer(r"(?ms)^@\w+\{([^,\s]+),.*?(?=^@\w+\{|\Z)", path.read_text())
    }
    for key in wanted:
        if key in selected:
            raise ValueError("Duplicate bibliography key: " + key)
        selected[key] = records[key]
destination = Path(sys.argv[1]).resolve()
if not destination.is_relative_to((repo / "output/pdf").resolve()):
    raise ValueError("Composed bibliography must remain under output/pdf.")
destination.parent.mkdir(parents=True, exist_ok=True)
destination.write_text(
    "% Build-only composition; edit canonical reference records.\n\n"
    + "\n\n".join(selected.values()) + "\n"
)
print(f"Composed {len(selected)} reference records.")


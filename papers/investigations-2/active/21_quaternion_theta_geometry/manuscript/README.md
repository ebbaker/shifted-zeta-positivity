# Quaternion theta manuscript

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**.


The [standalone LaTeX manuscript](quaternion_theta_geometry.tex) is the
stable investigation 21 manuscript requested by Edward Baker. It derives
the theta normalization, classical RH reductions, stationary and curvature
criteria, the independent-time Fueter lift, signed boundary and current
formulas, and the complete-source bounded estimates within one document.

The classical strip-contraction, threshold, and uniform localization
theorems are explicitly stated and cited as inputs. Their consequences
and all coordinate translations used here are proved in the manuscript.
The all-height theta sign remains open.

Open the source in Codex for the editable text and automatic PDF preview.
The current source has compiled successfully with the desktop compiler.
An exported 26-page PDF was also checked visually. The source requires
only standard LaTeX packages and no external project files or bibliography.
For a terminal export, run `pdflatex` on the source with an external output
directory, repeating until cross-references stabilize; keep auxiliary
outputs out of the research checkout.

The [build record](BUILD_RECORD.json) binds the current source and PDF
export. The PDF export is delivered in this chat's `output/pdf/` directory
and can be regenerated from the source; no manuscript snapshot folder was
created. The [integration review](../reviews/4_MANUSCRIPT_CONVENTION_AND_FOUNDATION_AUDIT_20261014.md)
records the derivation and verification scope.

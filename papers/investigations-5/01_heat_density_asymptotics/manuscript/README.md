# Analytical working manuscript

24 October 2026. Drafted for Edward Baker with substantial LLM assistance,
**gpt-6-astra (Codex), recorded effort max**. Same-assistant review only.

Open [main.tex](main.tex) or this folder in the built-in LaTeX editor.
This is the one maintained manuscript, rewritten at the author's request
to incorporate the explicit clock and finite-time construction. The
checked reading copy has **28 pages**. No snapshot folder was created.

The argument now runs from the canonical heat field and exact fixed/adaptive
regulator equations to the negative Gaussian endpoint, complete-source
positive carrier, explicit differentiated saddle clock, growing-block
Vandermonde and pair matrices, global scope, and a finite-source bridge.
The clock has O(kappa^-1/2) density error and O(L*kappa^-7/6) current/time
error on the buffered eventual inner window. The finite-time construction
pays density/current/time and actual covariance/Laplacian comparison errors.
The sharper score mean also improves one term of the determinant bound.

The manuscript incorporates Notes 14, 16, 19, 20 and 23 alongside the earlier
fixed-regulator results. Numerical support is confined to four short
paragraphs in Appendix C; details remain in the linked research notes and
execution records. Useful transition overlap, actual clock covariance,
positive outer heights and certified finite onset remain open. A smooth
global regulator is not a completed all-time approximation.

## Build and output policy

From this directory run:

~~~sh
python3 -B build.py
~~~

The script requires LaTeX and latexmk. The built-in editor can also compile
main.tex. The script discovers the repository root and exports to

    output/pdf/heat_density_asymptotics/heat_density_asymptotics.pdf

relative to that root. Auxiliary files and the driver stay in the ignored
output folder's .build directory. No PDF or build auxiliary belongs in
this manuscript directory or in Git. The local PDF links use the detected
checkout root; the editor fallback is declared in main.tex.

The [build record](BUILD_RECORD_20261024.json) identifies the current 28-page
export, its source hashes and production checks. The previous 25-page
integration remains documented in [Note 21](../notes/21_ANALYTICAL_MANUSCRIPT_INTEGRATION_20261024.md).
The current addition is [Note 23](../notes/23_FINITE_TRANSITION_CONTRACT_AND_LOCAL_BOUNDS_20261024.md),
with [same-assistant review](../reviews/08_FINITE_TRANSITION_LOCAL_BOUNDS_SELF_REVIEW_20261024.md).
It adds cellwise source, amplitude-aware nonlinear, actual covariance and
local-evaluation allowances. The declared first trial does not meet its
observable tolerances; no uniform numerical certificate or endpoint
connection is claimed. Successful production checks do not independently
validate mathematics.

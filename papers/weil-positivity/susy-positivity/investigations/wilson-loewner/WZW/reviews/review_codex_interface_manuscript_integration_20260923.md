# Manuscript integration audit: completed thermal-interface tests

23 September 2026. Prepared for Edward Baker with LLM assistance.

**Model/reviewer:** GPT-6 (Codex; developer-provided identity).  
**Effort:** not exposed; not inferred.  
**Review type:** same-assistant mathematical-scope, editorial, source, link and visual audit; not an independent specialist review or proof checker.

**Artifacts:** [live manuscript](../manuscript.pdf), [entry point](../manuscript.tex), [build record](../BUILD_RECORD.json). This audit supersedes the [12-page manuscript audit](review_codex_thermal_manuscript_20260923.md) for the live document; the earlier audit remains a historical record.

## Integration and claim boundaries

The manuscript now has 17 pages. Section 5 replaces the proposed interface with the completed [finite-place test](../notes/FINITE_PLACE_RADIATION_INTERFACE_TEST_20260923.md). Section 6 integrates the [energy-exchanging boundary test](../notes/THERMAL_BOUNDARY_COUPLING_AND_FRONT_RIGIDITY_TEST_20260923.md). Section 7 retains the earlier retrospective, and Section 8 records the five remaining avenues. The abstract, status, opening roadmap, appendix and bibliography have been updated consistently.

The following boundaries were checked against both notes and their research audits:

- The controlled loop has an explicit propagation metric and unitary vertex. Its coherent mean, outgoing variance and loop storage are all present in the ordinary energy identity. The controller is unchanged on repetitions; the fixed ratio `g4/g2 = 1/2` differs from the required temperature-dependent ratio. Formal normalization by the direct coefficient is only a comparison, not a new passive readout. The norm identity limit is retained as a valid positive result.
- The fixed bounded-readout proposition requires a native finite-place Gibbs state and temperature-independent bounded observable. Its proof uses holomorphy and real-temperature boundedness. It is not applied to arbitrary deconvolution of the completed transfer or to an interacting equilibrium.
- The finite-Euler pole is stated for `0 < beta < 1` at `p = (1-beta)/2`, with its nonzero residue. The obstruction is to a causal passive response; it does not exclude causal unstable kernels. The full zeta cancellation is a local unconditional fact, not proof of full-family passivity. The beta-one two-prime boundary pole and finite-window/omitted-prime distinction are retained.
- The native commutator, sign of the retarded susceptibility, admittance weights and conservative oscillator energy agree with the structural note. Transition frequencies are not called physical flight delays.
- Exact Kubo susceptibility in the uncoupled state and exact conservative linear realization are explicitly separated from unconstructed exact finite-coupling microscopic quantum scattering. Thermal correlations are shown, and the energy identity is limited to coherent perturbations.
- The boundary connection retains the entire modular quotient. Its factor of two follows from the port equations. The ordinary energy identity uses the established half-shift core's causality and isometry; it does not assume the variable-shift target's positivity.
- The front theorem assumes the stated positive spectral representation and finite total mass. The proof follows from dominated convergence and direct subtraction. It includes infinitely many modes with finite mass but does not treat an arbitrary bounded probe as energy regular. Exterior-port prompt response and the favorable zero-extra-lead control are distinguished.
- The additional switch `lambda = 1-beta` is granted explicitly, not derived from KMS. The native beta tangent decays as `p^(-1/2)` while the arithmetic tangent grows logarithmically in magnitude. Supplementary low-frequency and hot-endpoint statements are restricted to the explicit finite-transition load.
- The decision parks the regular fixed-core passive parallel-load branch. The coefficient identity survives. Distributed core deformations and well-defined infinite-spectral-mass models remain outside the exclusion, with no successful construction claimed.
- The outlook is a research agenda. No cumulative positive storage identity is claimed. The canonical-system paragraph preserves Suzuki's `omega > 1` restriction for the cited explicit unconditional construction; the needed small-shift extension is identified as unresolved.

## Citations and numerical provenance

Both new notes have descriptive bibliography entries and relative PDF links. Kubo's 1957 primary article is cited for response theory, DLMF Section 25.2 for the zeta pole, and Suzuki and the modular note for the fixed reference. Bibliographic metadata and the cited Suzuki range were checked against the primary sources. The specialized coupling formulas and exclusions are derived in the manuscript and notes rather than attributed as literature novelty.

All 21 local PDF link annotations, representing 20 distinct targets, resolve from the delivered manuscript directory. Appendix A links each of the three current programs, records and research audits. The program SHA-256 identities and every saved case outcome were checked: 87 orbit-weight cases, 144 finite-place cases and 203 structural cases. These records and programs are unchanged. The suites were not rerun for this editorial integration, and no new experiment, interval certificate or external numerical dataset is claimed. Historical suite provenance remains separate.

## Build and visual review

The local active TeX inputs compile with pdfLaTeX/latexmk. The final log has no warnings, undefined references or citations, overfull boxes or underfull boxes. All 17 pages were rendered at 110 dpi and visually inspected, including the new equations, table, theorem statements, section transitions, appendix and bibliography. After making the abstract's beta range explicit, the changed title page was rendered and inspected again. Text bounds on every page leave at least 60 points horizontally and 30 points vertically, including the running header and footer. Relative links and the final metadata were checked separately.

The title and acknowledgements retain Edward Baker's attribution and substantial GPT-6 (Codex) assistance, with the effort setting reported as unavailable. The PDF is approximately 405 KB, below the repository limit. The build record binds the final source and PDF identities, and the live milestone index records the revision without creating a manuscript snapshot. Earlier notes, numerical programs and records, inactive section fragments, and the parent manuscript pair are preserved.

Independent mathematical and physical review remains outstanding. This audit verifies the scope and presentation of the completed tests, not RH or a full arithmetic physical realization.

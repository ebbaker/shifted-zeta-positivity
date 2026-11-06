# TND-D-E05: analytical manuscript integration and production check

6 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra / max**, existing direct-branch chat0003, thread `01a1af86-e5ac-7841-ac70-e37f195c5cef`. This is the manuscript author's local mathematical/editorial consistency and production check, not an independent assessment. No subagents or external reviewers were used.

**Disposition: the requested analytical synthesis is complete.** The [manuscript](../manuscript/main.tex) develops the direct realization and its collision diagnostics, using the root manuscript as background, and ends with outstanding analytical tasks. The reading copy has 18 pages. One synthesis and one local consistency pass were followed by necessary typesetting repairs and visual verification.

> Manuscript integration does not upgrade the evidence status of its sources.

## Scope and source map

[Exact inputs](../research-progress/handoffs/06_TND_D_E05_MANUSCRIPT_INPUTS_20261106.json) identify the full parent manuscript, direct proof, E02 review, later collision note, plan and original reflected control. All thirteen frozen mathematical/background inputs are unchanged; the fourteenth intake file is the live progress register, which is intentionally updated for this task. The root and sibling manuscripts were not edited.

| Development | Source status and integration check |
| --- | --- |
| Section 2: source and state | Parent geometry/source background and direct E01 Note02. Complete angular signs/multiplicities and continuous radial spectrum are retained. Maximal constituent domains, full reflection, positive source lower bound, finite derivative recurrence and complete tails lead to the normalized square-root estimates and exact finite energy-moment sum. No arbitrary positive Schwartz square-root assertion or support-vector domain claim is made. |
| Section 3: complete instrument | Direct E01, internally accepted within scope by E02. Signed odd-count amplitudes, boundedness, strong completeness, trace-norm outcome sums and binomial aggregation are explicit. The no-count law is proved on the declared conjugated intersection domain with the proper one-sided endpoints. Neither a maximal effective-generator theorem nor a hardware construction is asserted. |
| Section 4: observation and regular motion | E01's conditional readout plus Note04's later derivatives. Checked the square-root half factor, normalizing subtraction, Z=2H(0), p=Zlambda/Zinitial, and recovery of absolute H from joint probabilities and the initial scale. Physical time decreases lambda; the absolute contrast solves forward heat in t. The covariance law concerns the quadrature distribution. |
| Section 5: count calculus | Note04 remains proof-author work. Checked every finite count moment, the sign (-gamma*t)^j, absolute generating-series domination by probability mass, and the finite-sector transfer law. Nonzero-count traces are analytical quantities; their definition grants no additional physical readout access. |
| Section 6: collisions | Note04's conditional diagnostics. Checked d0=d0,k=0 with nonzero curvature, unequal no-count loss rates, the signed first-count witness, square-root local branches and the direction of real-to-complex passage. State/success regularity, zero-velocity singularity, ternary variance, sector second-moment identity and finite higher-multiplicity expansion are separate statements with their own limits. No actual canonical-source collision is assumed or established. |
| Section 7: exact control | Note04 and the original reflected super-Gaussian source. Its polynomial derivative ratios and quartic tail pay its own square-root domains. Translation gives c F(k)(1+cos 4k); M4=M0/4 and Cauchy–Schwarz give F(k)>0 for abs(k)<2. The event at lambda=1/4, k=pi/4 has curvature 16 c F(pi/4)>0 and lies at t=1/(4gamma). The witness fails canonical theta arithmetic and the theta tail formula while satisfying the generic instrument requirements. |
| Section 8: remaining work | Source-specific mechanisms remain eligible alongside quantitative estimates. No B02 target has been selected. Multiplicity, endpoints, global range, supplied physical access and separate diagnostic assessment remain explicit. Numerics are reserved for supporting a subsequently specified analytical question. |

## Local expository addition

Section 5's interaction-frame all-count kernel is written out explicitly:

\[
f_{1/2}(v)f_{1/2}(w)\exp[-\gamma t(v-w)^2/2]R.
\]

This follows immediately by summing the existing signed Kraus kernels. The absolute sum is bounded by `exp[-gamma*t*(abs(v)-abs(w))²/2] <= 1`, giving Hilbert–Schmidt domination by the product of the initial radial functions and the finite angular Hilbert–Schmidt norm. The independently established trace-norm outcome sum identifies the same operator. It explains conserved diagonal observations and attenuated off-diagonal coherence. This is a locally derived consequence included for coherence of exposition, not a new collision-control mechanism, physical assumption or separately assessed research result.

## Limits preserved

> The count-sector dictionary supplies no collision-excluding margin by itself.

The supplied loader, source-position imprint, angular state, initial calibration, co-moving controller and selected no-count readout remain model inputs. A canonical-source collision restriction or demonstrated advantage over direct analysis using the same information is still missing. The exact control excludes reliance solely on the generic properties it satisfies on a domain containing its event; it is not a universal exclusion of source-sensitive dynamics or different physical constructions.

Every derivative order is fixed and finite unless an independent count-series argument is supplied. No order-uniform constants, all-height signed margin, infinite-time law or uniform small-rate limit is inferred. The complex branches describe analytic continuation of H, not bounded measurements with nonreal labels. The state remains smooth through a hypothetical event while its signed observation degenerates.

E01 retains E02's same-assistant/same-chat internal acceptance within conditional ideal-operation scope. The later collision/count note and this local kernel calculation retain proof-author status. Neither manuscript production nor source passage checks provide specialist independence or formal verification. External MC11, shared and sibling task statuses are unchanged.

## Build, references and visual verification

The [build script](../manuscript/build.sh) completed successfully using TeX Live 2023, pdfTeX and latexmk 4.79. BibTeX resolves the canonical reused entries and the new internal-use keys. The final log has no warnings, undefined citations/references, or overfull/underfull boxes. All 89 labels are unique and all 76 explicit cross-reference uses resolve in the source. The final reading PDF has 18 letter-size pages and 410602 bytes; its identity, source hashes and bibliography inputs are in [BUILD_RECORD.json](../manuscript/BUILD_RECORD.json).

All eighteen pages were rendered at 100 dpi and visually inspected in page contact sheets. The corrected pages 7, 8 and 11 were also inspected individually after rebuilding: three missing mathematical command escapes and an over-spaced theorem heading were repaired. Equations, tables, titles, page numbers and bibliography are legible and within the page; no remaining clipping or overlap was observed. The reading copy is under ignored repository-root `output/pdf/`; temporary review images remain outside the repository. No numerical research result or computational experiment was introduced.

The [source-use receipt](../references/02_TND_D_E05_MANUSCRIPT_SOURCE_USE_20261106.md) lists the fresh primary HTML checks for spectrum, theta inversion, Newman normalization and measurement conventions. No new article, third-party PDF download or source-evidence upgrade occurred. The complete realization, later diagnostic note, issued contracts and original control remain unchanged.

## Return

TND-D-E05 is complete at analytical synthesis and production scope. [Return record](../research-progress/handoffs/06_TND_D_E05_MANUSCRIPT_RETURN_20261106.json) and [DRAFT_HISTORY.md](../DRAFT_HISTORY.md) identify this working-tree milestone without a snapshot folder or new Git commit. B02 remains partial with mechanism/target selection open; E03 remains reserved and unissued. The final section of the paper states the outstanding tasks without selecting a successor.

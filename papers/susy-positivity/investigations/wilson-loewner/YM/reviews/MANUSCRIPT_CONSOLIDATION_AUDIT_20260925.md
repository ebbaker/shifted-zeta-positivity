# Consolidation audit: YM boundary sources and the Weil form

25 September 2026. Drafted for Edward Baker with substantial LLM assistance.

Model exposed: GPT-6 (Codex). Exact deployed variant and configured reasoning effort: unavailable; not inferred. Baseline checkout: f8b8622fbd687bd152dd40dcc0c4bbd4576008e5, including the preexisting uncommitted single-probe continuation.

Status: editorial consolidation and model-assisted consistency checks, not independent mathematical review. The investigation is paused at the author's request. No new physical candidate, numerical experiment, or RH implication is introduced.

## Deliverable and coverage

The [35-page manuscript](../manuscript.pdf), with [editable LaTeX](../manuscript.tex), is self-contained at the level of a research draft: the model, state, test space, complete arithmetic normalization, operator domains, theorem assumptions, and proof arguments are stated in the document. Standard explicit-formula and analytic-number-theory results are cited as external mathematical inputs. Historical notes are linked for provenance, rather than used in place of definitions or proofs.

The body consolidates the finite reflected boundary construction; the admissible winding/electric law and its exclusion; weighted character operations and phase branching; the distributional prime insertion and raw-packet tails; the completed signed archimedean identity; bounded-module and closability obstructions; strong physical recentering; the full current's absolutely continuous spectrum; divergent positive prime completions; moving sharp-cutoff edges; three-anchor determination and compact occurrence; and the single detecting probe and conditional one-correlation occurrence theorem.

Appendices retain the continuous and discrete Wilson hierarchy calculations, the unfavorable interacting experiment, earlier prescribed-background controls, weight transport and source-domain qualifications, spectral/modular/thermal exclusions, two-dimensional and modular-scattering comparisons, numerical evidence ledger, and LLM provenance.

## Corrections and editorial qualifications

1. The preliminary hierarchy note's displayed equation (5.8) omits the addition sign between the derivative residual and the curvature residual. The manuscript's equation (A.9) restores it:

       ||r_2||^2 = |y|^2/g [d - (dot g)^2/(4g) + k^2(mu_4 - g^2 - mu_3^2/g)].

   The two terms are squared orthogonal residuals. Their cross term vanishes because the Hermitian residual pairing is real and the second residual is multiplied by minus i k. This is a typographical repair, consistent with the note's adjacent explanation and the implemented control. The historical note and program are preserved.

2. The finite span of compensated characters is called a dense test domain for the archimedean matrix calculation. The manuscript does not claim it is a graph core for a separately proved self-adjoint realization of the sum. Only its actual dense symmetric domain and closability are used.

3. The appendix numbers forward residuals by the transition from step j to step j+1. Accordingly the future-loop factor is K_(N,j+1), and the backward residual sum starts at j+1. This is an explicit index shift from the source note's convention, where residuals are numbered by the arrival step. The last forward residual has zero immediate scalar-output contribution in either convention.

4. A zeta zero is denoted by varrho in the detecting-probe section to distinguish it from the actual plaquette density rho. Off the critical line the explicit-formula coefficient remains F(lambda)F(-lambda), not a squared modulus.

5. The draft separates the controlled cofinal limit for raw character prime pairings from the proved iterated limit for compensated archimedean packets. No joint cutoff theorem is inferred from norm-small packet differences.

6. The draft treats every previously identified gap explicitly: the Haar adjoint cannot replace the weighted adjoint; all winding phases remain present; a distribution is not a Hilbert source; the radial compensation is not a proved Ward-selected subtraction; recentering retains L2 rather than the Weil norm; and formal removal of divergent contact terms does not establish positivity.

## Proof-dependency check

| Result | Inputs retained in the draft | Scope |
|---|---|---|
| Character prime mixed limit | Smooth positive marginal, exact character Gram matrix, rapid Fourier tails, fixed-phase summation | Actual-state limit; infinite insertion is distributional |
| Archimedean mixed limit | Specified compensated compression, derivative polar map, angle in turns, Poisson and Mellin identities | Complete signed multiplier/contact/growth; no positivity theorem |
| Strong recentering | Full weighted flow, its Jacobian, Haar sine-transform scaling, bounded weight transport | Actual retained L2 source; explicit loss of winding norm |
| Current-spectrum obstruction | Global flow cross-section outside null critical sets; Fourier decay; unconditional nondecay of the detecting response | All finite-vector coefficients of this current, not every possible YM observable |
| Positive prime obstruction | Actual weighted adjoints and class-space norm comparison | Infinite unsubtracted form has domain zero |
| Coercive constrained completion | Closed positive coercive form and fixed bounded readout | Divergence for every nonzero retained readout |
| Sharp-cutoff edge response | Prime number theorem and exact pole-neutral primitive identities | Sharp cutoff, fixed local counterterms, and iterated physical norm bound |
| One-probe criterion | Nonvanishing compact probe, unconditioned explicit formula, zero counting and Laplace analyticity | RH-equivalent arithmetic regularity; not a consequence of OS temperedness |
| One-correlation occurrence | An independently established actual stationary physical correlation | Sufficient theorem with a proved filtering domain; the physical hypothesis is unverified |
| Compact occurrence | Actual compact preparation sets and uniform finite feasibility | OS and a mass gap do not establish arithmetic feasibility |

These checks organize the arguments already present in the research notes. They are not a new independent referee certification.

## Build, presentation, and preservation

- LaTeX builds successfully with resolved references and citations, no duplicate labels, and no overfull boxes. Minor underfull paragraph warnings are harmless spacing warnings.
- All 35 pages were rendered for visual inspection. The title, main formulas, and result tables were also inspected as separate pages.
- The PDF is below 1 MB. No rendered page images, large arrays, raw chains, or third-party PDFs are installed in the repository.
- The original analytical notes, substantive reviews, numerical programs, and small records are preserved byte for byte. Only the project outline and selected indexes receive additive manuscript/pause notices.
- Existing numerical records are summarized, not rerun. The 76-control electric-parity review is explicitly a rerun of 57 plus 19 existing controls, not an additional unique suite.
- The parent package inventory was already stale: 45 mismatches within YM and 92 outside YM. Only its YM inventory and standalone-manuscript registration are refreshed. The 92 unrelated discrepancies remain documented rather than silently overwritten.
- No commit or dated snapshot directory is created. The current version is indexed in [DRAFT_HISTOR.md](../DRAFT_HISTOR.md), with exact source and research fingerprints in [BUILD_RECORD.json](../BUILD_RECORD.json).

## Remaining mathematical gap

The completed signed mixed identity is established under its stated finite-state and limiting assumptions. An actual positive YM source law with that pairing remains unconstructed. The one-correlation theorem gives a precise sufficient alternative, but its stationary physical correlation has not been derived. Neither OS axioms, a physical mass gap, nor the additional phase-space compactness assumption closes that arithmetic occurrence gap here.

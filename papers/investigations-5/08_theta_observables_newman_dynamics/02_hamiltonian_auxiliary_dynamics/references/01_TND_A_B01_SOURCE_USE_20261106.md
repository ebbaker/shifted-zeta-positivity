# Source use for TND-A-B01 r1

6 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra / max**, auxiliary chat0001. This is a branch use receipt, not a second canonical bibliography or an independent theorem assessment. [Decision01][decision] and [E01 request r1][request] are its consumers. Canonical annotations remain at their existing homes; [the parent guide][parent-refs] records this reuse. Follow [REFERENCE_WORKFLOW.md][reference-workflow].

## Primary passages freshly checked

| Source, version and canonical home | Actual check on 6 November; use and limit |
| --- | --- |
| Roberto Camporesi and Atsushi Higuchi, *On the eigenfunctions of the Dirac operator on spheres and real hyperbolic spaces*, arXiv:gr-qc/9505009v1, 9 May 1995; J. Geom. Phys. 20 (1996), 1–18; [DOI](https://doi.org/10.1016/0393-0440(95)00042-9). [Canonical MC11 annotation][mc-refs]; BibTeX `CamporesiHiguchi1996`. | Checked [v1 primary HTML](https://arxiv.org/html/gr-qc/9505009v1), §3.1 (3.40), (3.51)–(3.54), spectrum discussion after (3.68), and §5.2 (5.35)–(5.36). With self-adjoint D=−i slash∇ and relabelled n≥1, the unit S² multiplicity is 2n per sign. Curvature convention is +Scal/4 after squaring D. Product-cylinder scaling/domains are inherited local calculations, not quoted from this paper. Used in Decision01 §2 and request construction/obligation 1. Selected passages only. |
| NIST Digital Library of Mathematical Functions, §20.7(viii), [20.7.32](https://dlmf.nist.gov/20.7.E32); live online reference, [canonical MC11 annotation][mc-refs]; BibTeX `DLMFThetaModular`. | Checked the formula and preceding principal-root convention, tau-prime=−1/tau. Specialization at theta argument zero and lattice parameter i r², r>0, gives the complete unit-weight inversion. Its lattice tau is unrelated to this branch's proper time. Used through accepted source reflection in Decision01 §3/request obligation 3. This does not justify smooth reflection of arbitrary finite prefixes or filtered sources. No artificial PDF copy. |
| Brad Rodgers and Terence Tao, *The De Bruijn-Newman constant is non-negative*, Forum of Mathematics, Pi 8 (2020), e6, [DOI](https://doi.org/10.1017/fmp.2020.6); [arXiv:1801.05914v5](https://arxiv.org/abs/1801.05914v5), 3 July 2021. [Existing source-use/canonical links](../../../05_radial_theta_collision_geometry/references/14_NEWMAN_FLOW_AND_SOURCE_PERTURBATION_REFERENCES_20261028.md); BibTeX `RodgersTao2020` in [reused bibliography][bib]. | Checked [v5 Introduction](https://arxiv.org/html/1801.05914v5#S1), (1)–(4), reflection statement and heat-sign paragraph after (4). Use limited to canonical Phi, H0=xi((1+iz)/2)/8, real source parameter and backward-heat sign. No main-theorem proof, numerical threshold or auxiliary-flow monotonicity imported. Used in Decision01 §§3–4 and request source/obligations 5–6. |

The existing [BibTeX file][bib] already contains these exact source/version keys; no duplicate bibliography or changed version was needed. No source was read in full. No physical detector, state-preparation or laboratory-realization theorem was imported from these references. Those apparatus assumptions are expressly supplied in Decision01; the local functional/domain check is assigned to E01.

## External reading copies and identity

The existing authorized PDFs were read for header/size/hash identity on 6 November; primary passage inspection above used HTML. No new download or replacement occurred. Original retrieval dates/provenance remain in the canonical records. Hash identity does not validate mathematics.

| Source | Existing external path | Bytes; SHA-256 |
| --- | --- | --- |
| [Camporesi–Higuchi v1 PDF](https://arxiv.org/pdf/gr-qc/9505009v1) | `/Users/Shared/szp-archive/mc11-energy-filtered-theta-overlaps/references/gr-qc-9505009v1.pdf` | 410772; `d1cc42779cdd152e02165bfd5531150fa0a01c5209f63bffdc4c1a14d2f2873b` |
| [Rodgers–Tao v5 PDF](https://arxiv.org/pdf/1801.05914v5) | `/Users/Shared/szp-archive/height-dependent-heat-contours/references/1801.05914v5.pdf` | 503405; `376bb2c1ab941cd5b035546835c5481f2d026767b8e830a48cd5565114a1ec91` |

Both headers are `%PDF-` and both identities match the existing records. Public links, not machine-local copies, remain the reader dependencies. No third-party PDF entered Git.

## Local research use and evidence

Parent [E01 Note02][e01] §§1–4,6–9 and its frozen input/return were read. Its note and continuation hashes still match the recorded return. MC11's frozen Notes05/06/08 and Review05 still match E01 intake; [Note08][mc-source] §§2–3 and [Review05][mc-assessment]'s source/operator scope were checked for reuse. Parent new results remain proof-author work awaiting shared TND-E03; the passive-bank theorem has not been executed. No MC11 Note13-only claim is accepted here.

Investigation05's [book][book], ordinary cylinder heat and `prop:combined`, and [Review21][book-review] were checked for the inherited benchmark's interval and same-assistant scope. [Investigation06 Note06][aux-lessons] was checked for its limited response/recovery conclusions. [Control register][controls] and [theta cluster][theta] are navigation to existing evidence, not new control calculations. This is a targeted source-use check for one candidate, not a general literature audit, novelty claim, specialist review or status change to any external task.


[decision]: ../brainstorm/notes/01_TND_A_B01_R1_SUPPLIED_PROPER_TIME_RESPONSE_DECISION_20261106.md
[request]: ../research-progress/handoffs/02_TND_A_E01_R1_FROZEN_REQUEST_20261106.md
[source-use]: 01_TND_A_B01_SOURCE_USE_20261106.md
[progress]: ../research-progress/01_HAMILTONIAN_AUXILIARY_DYNAMICS_RESEARCH_PROGRESS_20261105.md
[plan]: ../research-plan/01_HAMILTONIAN_AUXILIARY_DYNAMICS_RESEARCH_PLAN_20261105.md
[overview]: ../research-overview/01_HAMILTONIAN_AUXILIARY_DYNAMICS_RESEARCH_OVERVIEW_20261105.md
[e01]: ../../notes/02_TND_E01_R1_GEOMETRIC_HAMILTONIAN_AND_COMPLETE_SPECTRAL_COMPARISON_20261105.md
[intake]: ../research-progress/handoffs/01_TND_A_B01_R1_INPUT_VERSIONS_20261106.json
[return]: ../research-progress/handoffs/01_TND_A_B01_R1_RETURN_RECORD_20261106.json
[execution-inputs]: ../research-progress/handoffs/02_TND_A_E01_R1_INPUT_VERSIONS_20261106.json
[mc-source]: ../../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/notes/08_MC11_AR_E03_R1_SOURCE_MEMBERSHIP_AND_ENDPOINT_PAIRINGS_20261105.md
[mc-assessment]: ../../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/reviews/05_MC11_AR_E04_R1_MODEL_SOURCE_AND_SCOPED_TRANSFER_ASSESSMENT_20261105.md
[mc-contract]: ../../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/notes/06_MC11_BR01_R1_FROZEN_CYLINDER_MODEL_AND_ANALYTIC_CONTRACT_20261105.md
[mc-refs]: ../../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/references/README.md
[bib]: ../../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/references/references.bib
[parent-refs]: ../../references/README.md
[results]: ../../../../../result-summaries/README.md
[theta]: ../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a03]: ../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[workflow]: ../../../../../GPT_RESEARCH_MODEL_WORKFLOW.md
[reference-workflow]: ../../../../../REFERENCE_WORKFLOW.md
[capture]: ../../../../../tools/CHAT_HISTORY.md
[large]: ../../../../../LARGE_FILES.md
[book]: ../../../05_radial_theta_collision_geometry/book/main.tex
[book-review]: ../../../05_radial_theta_collision_geometry/reviews/21_BOOK_REWRITE_ASSESSMENT_20261028.md
[aux-lessons]: ../../../06_auxiliary_collision_flows/notes/06_APPROACH_SUMMARY_AND_GOALS_FOR_NEXT_BRAINSTORM_20261029.md

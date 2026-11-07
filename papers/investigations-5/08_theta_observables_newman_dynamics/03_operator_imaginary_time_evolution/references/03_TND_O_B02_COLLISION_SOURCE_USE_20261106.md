# Collision reconnaissance source use

6 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra / max**, branch chat0003. Consumer: [collision anatomy Note07](../notes/07_TND_O_B02_COLLISION_ANATOMY_20261106.md). These are selected-passage checks, not complete article reviews or independent assessment of the new diagnostics.

## Angenent and local parabolic zero sets

Sigurd Angenent, *Nodal properties of solutions of parabolic equations*, Rocky Mountain Journal of Mathematics **21**(2) (1991), 585–592; [DOI](https://doi.org/10.1216/rmjm/1181072953), [author PDF](https://people.math.wisc.edu/~angenent/preprints/1987NodalPropertiesRMMJ.pdf). Written for the March 1987 Provo conference; publication is 1991.

Canonical catalog and reusable BibTeX remain in [Investigation06 sources.json](../../../06_auxiliary_collision_flows/references/sources.json) and [sources.bib](../../../06_auxiliary_collision_flows/references/sources.bib), key `Angenent1991`. This branch adds a use receipt rather than duplicating the article record.

Freshly inspected rendered printed pp. 585–587: §§1–2, assumptions (1)–(2), Theorem A and its continuation, the analytic heat polynomial (3), endpoint/periodic qualifications, and Figures 1–2. The scalar equation is forward parabolic with positive principal coefficient and the displayed coefficient regularity; the finite-interval version assumes nonzero values at both spatial endpoints throughout the time interval. Zero loss at a multiple event is consistent with increasing imaginary time here. The theorem is not a finite global zero count for theta on the whole line. Local double-event and finite-multiplicity formulas in Note07 are also directly derived, following the existing repository heat calculations.

Reading copy reused outside Git: `/Users/Shared/szp-archive/auxiliary-collision-flows/references/Angenent1991_reading_copy_20261028.pdf`; original retrieval 28 October 2026; source URL above. Rechecked 6 November 2026: **220387 bytes**, SHA-256 `18f048953edd6067a0acde56fb172a24f50fb3fe66705b8ef0a8427266ceacbb`. No new download or version replacement.

## Rodgers and Tao and the two energy notions

Brad Rodgers and Terence Tao, *The De Bruijn-Newman constant is non-negative*, Forum of Mathematics, Pi **8** (2020), e6; [DOI](https://doi.org/10.1017/fmp.2020.6). Corrected preprint [arXiv:1801.05914v5](https://arxiv.org/abs/1801.05914v5), 3 July 2021. Canonical ownership and archived PDF stay at the [existing record](../../../05_radial_theta_collision_geometry/references/14_NEWMAN_FLOW_AND_SOURCE_PERTURBATION_REFERENCES_20261028.md).

Fresh primary [v5 HTML](https://arxiv.org/html/1801.05914v5#S4) inspection: §4 Theorem 4.16, (56), the ensuing formal zero Hamiltonian/energy discussion (57)–(58), and Lemma 4.18(i)'s gap equation. The printed theorem is stated on the paper's contradiction interval Λ<t≤0, with principal-value zero summation justified there. It is not invoked as a theorem at an arbitrary positive-parameter or nonreal-zero event here. The local two-root/nonvanishing-factor calculation in Note07 requires no infinite zero sum and is independently derived. The paper explicitly distinguishes its formal divergent global sums from the truncated identities needed for proof. These zero-configuration energies must not be identified with ⟨Ψ,KΨ⟩.

The v4 HTML was opened during discovery; the actual cited equations and qualifications were subsequently checked in v5. No audit of the full nonnegativity proof or v5's other corrections was performed. The existing v5 PDF remains at `/Users/Shared/szp-archive/height-dependent-heat-contours/references/1801.05914v5.pdf`; its historical metadata are in the canonical record, not newly reverified here.

## Repository passages consumed

- [Operator Note04](../notes/04_TND_O_E01_R1_CYLINDER_ITE_PROOF_20261106.md), §§1–4, 6: exact prepared amplitude, typed K/readout maps, complete fixed-order source bounds, entire source transform and admitted control; [E02 Review01](../reviews/01_TND_O_E02_R1_CYLINDER_ITE_ASSESSMENT_20261106.md) supplies its accepted scope with Q1/Q2.
- [Direct collision Note04](../../01_direct_newman_realization/notes/04_TND_D_B02_COLLISION_DYNAMICS_RECONNAISSANCE_20261106.md), §§2, 4–7: smooth state versus root tracking, source-sector imbalance, heat polynomial and explicit witness. These diagnostics retain their proof-author status; their reuse here is not an E04/E07 evidence promotion.
- [Investigation22 Note08](../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/08_REAL_AND_COMPLEX_COLLISION_MULTIPLICITIES_20261015.md), local discriminant theorem: analytic factorization and finite heat-root cluster, with reversed Newman/imaginary-time orientation here. The complex-degree theorem is not needed.
- [Investigation05 Note38](../../../05_radial_theta_collision_geometry/notes/38_AUXILIARY_SOURCE_FLOWS_AND_COLLISION_RESPONSE_20261028.md), §3, (3)–(5): bounded source perturbations and motion of a nondegenerate event. Note07 translates these response identities to imaginary time; no new auxiliary flow is selected.

The [result index](../../../../../result-summaries/README.md), especially [local geometry](../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), and [patterns index](../../../../../avoid/README.md), especially [re-realizations](../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), govern attribution and scope. No source establishes a canonical collision or its exclusion.

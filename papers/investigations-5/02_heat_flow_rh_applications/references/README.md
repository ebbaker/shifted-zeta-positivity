# References for heat-flow applications to RH

26 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance, **gpt-6-astra, actual recorded effort max**.

This is a targeted opening collection, not a complete current-record
survey. [sources.json](sources.json) contains version, inspection, and PDF
provenance records; [sources.bib](sources.bib) is the reusable bibliography.
The [brainstorm](../notes/01_HEAT_FLOW_RH_APPLICATIONS_BRAINSTORM_20261026.md),
[positive-threshold analysis](../notes/02_RODGERS_TAO_POSITIVE_THRESHOLD_20261026.md),
the [Rodgers–Tao sub-investigation](../rodgers_tao/references/README.md),
and [current summary](../summary/CURRENT_SUMMARY.md) are the consumers. Downloading or hashing a paper does not validate it.

| Reference | Version and actual inspection | Role |
| --- | --- | --- |
| [Brad Rodgers and Terence Tao, The De Bruijn-Newman constant is non-negative](https://arxiv.org/abs/1801.05914v5) | v5, 3 July 2021; introduction, §4, §7 definitions (62)–(63), corrected §8, and §9 / eq. (93) passages checked in primary HTML and archived PDF | Dynamics and localized energy; PDF Theorem 11 / eq. (56), Propositions 26–28; under the contradiction assumption \(\Lambda<0\) |
| [D. H. J. Polymath, Effective approximation of heat flow evolution of the Riemann ξ function, and a new upper bound for the de Bruijn-Newman constant](https://arxiv.org/abs/1904.12438v2) | v2, 4 August 2019; Theorems 1.2 and 1.5 checked in HTML/PDF; Proposition 3.1 and relevant §9 passages checked in primary HTML | Complete upper-bound consumer, prior positive-time zero geometry, and Hermite splitting at a multiple zero |
| [Dave Platt and Tim Trudgian, The Riemann hypothesis is true up to 3·10^12](https://arxiv.org/abs/2004.09765v1) | v1, 21 April 2020; §3.4, Corollary 2 checked in primary HTML | Published \(\Lambda\le0.2\) comparison benchmark; not asserted to be the current record |
| [Alexander Dobner, A proof of Newman's conjecture for the extended Selberg class](https://arxiv.org/abs/2005.05142v2) | v2, 10 January 2026; abstract, introduction, Theorems 1–2 and displayed approximation/map checked | Alternative negative-time method; no full proof audit or imported quantitative onset |
| [Cetin Hakimoglu-Brown, A conditional bound Λ≤0.13963 for the de Bruijn–Newman constant](https://arxiv.org/abs/2610.12803v1) | v1, 8 October 2026; abstract and version metadata only | Literature watch: assumes no nontrivial zeta zeros with real part greater than 7/8; this premise and the claimed bound are not adopted |

Rodgers–Tao v5 corrects energy-boundary accounting in §8. Cite the PDF
numbering above; arXiv's experimental HTML renders different theorem
numbers. Do not replace this version with an earlier one for the proposed
energy comparison.

Polymath's upper criterion requires **all three** initial, exterior and
barrier hypotheses. Its positive-time distribution theorem has the
height/time restriction stated there. Neither is a theorem obtained by
formally inserting small time into the Book's late-time hierarchy.

The repository already has extended annotations for
[Rodgers–Tao, Dobner and Polymath](../../../investigations-4/12_height_dependent_heat_contours/references/README.md),
and [Polymath's Book inputs](../../01_heat_density_asymptotics/references/README.md).
Those original records retain their provenance. Existing PDF reading
copies were reused and their bytes/hashes rechecked rather than duplicated.
The two newly archived PDFs are under
`/Users/Shared/szp-archive/heat-flow-rh-applications/references/`.
All exact paths, sizes, hashes and dates are in `sources.json`; no
third-party PDF is placed in Git.

For later upper-bound work, also start from the repository's
[Gomila audit and corrected frontier status](../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md).
Its incomplete producer-row audit and floating candidate improvements
must not be upgraded into a newly certified bound here. Review newer
unconditional claims separately before making a best-known-bound claim.

Follow [REFERENCE_WORKFLOW.md](../../../../REFERENCE_WORKFLOW.md) and
[LARGE_FILES.md](../../../../LARGE_FILES.md).

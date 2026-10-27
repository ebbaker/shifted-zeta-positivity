# Quaternion lattices and the complete observation: references checked

27 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**. Investigation05 chat0003. These are selected-passage and discovery records, not full literature or priority reviews.

## Imported Hurwitz count

Megumi Asada, Eva Fourakis, Nathan McNew, Gwyneth Moreland, Bruce Fang, Sarah Manski, Steven J. Miller, Ajmain Yamin and Sindy Xin Zhang, **Avoiding 3-Term Geometric Progressions in Hurwitz Quaternions**, *Journal of Integer Sequences* **27** (2024), Article 24.7.7. [Author-hosted published PDF](https://www.nathanmcnew.com/NonCom2.pdf).

Checked the title/author/publication information and Section 2, printed page 4, definition of the Hurwitz order and Lemma 1: its norm-n shell has 24 times the sum of the odd divisors of n points. The paper identifies this as a classical consequence of Jacobi's four-square theorem and refers elsewhere for a full proof. No progression-density theorem is used. [Note11](../notes/11_HURWITZ_HOPF_AND_UNIT_QUATERNION_HEAT_REPRESENTATIONS_20261027.md) derives its Epstein product, Hopf observation and Möbius inversion separately from that count.

The public PDF was archived outside Git at `/Users/Shared/szp-archive/radial-theta-collision-geometry/references/Asada_et_al_Hurwitz_Geometric_Progressions_JIS_24_7_7.pdf`, 225104 bytes, SHA-256 `896f2ec52b1c1823bbf645daa2334bdf56fea491c7302315399bab6b4aaf6e69`. Retrieved 27 October 2026. The hash identifies the reading copy, not mathematical validity.

## DLMF normalization and nonvanishing inputs

The existing DLMF record is extended rather than duplicated. Rechecked [20.4.6](https://dlmf.nist.gov/20.4.E6) and the modular context of [20.7.33](https://dlmf.nist.gov/20.7.E33), retaining annotation05's period-pi convention and Note08's proof of the signed shell identity. Note10 also supplies a direct shell proof of the translated Gaussian observation, so no unverified off-sphere modular formula is needed.

Checked [25.4.2](https://dlmf.nist.gov/25.4.E2) and [25.10(i)](https://dlmf.nist.gov/25.10): reflection and Euler-product nonvanishing imply zeta(w-1) is nonzero when 0<Re(w)<1. This is the only nonvanishing strip imported for Note11's prefactor. No RH assumption is used. DLMF is an online reference; no artificial PDF is made.

## Related sources found, with no theorem imported

- Ibrahim Al-Dayel and Sharief Deshmukh, **The Heat Equation on Submanifolds in Lie Groups and Random Motions on Spheres**, *Mathematics* **11** (2023), 1958, published 20 April 2023. [DOI and publisher page](https://doi.org/10.3390/math11081958). Publisher-indexed metadata and abstract inspected; related background on group heat kernels. Direct HTML/PDF retrieval returned HTTP 429 or an inaccessible response, so no local PDF was obtained and no theorem or normalization is imported. Note11 derives its round-sphere spectrum and central kernel directly.
- John Voight, **Quaternion algebras**, [author's book landing page](https://math.dartmouth.edu/~jvoight/quat.html). Discovery/routing only: the indexed page identifies the 2021 open-access book and post-publication versions, including stable v1.0.5 (10 January 2024). Live retrieval returned a redirect-only page; no book passage or PDF was inspected in this return. Not used as a theorem source. The checked article above provides the only imported Hurwitz formula.

The two research notes retain the [earlier quaternionic results](../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md) as internal context, without treating their physical-jet constructions as lattice-source theorems. The [catalog](sources.json) and [bibliography](sources.bib) retain the distinction between checked passages and discovery-only sources.

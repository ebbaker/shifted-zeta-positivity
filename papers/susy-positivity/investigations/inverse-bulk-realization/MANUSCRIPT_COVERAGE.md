# Coverage of working manuscript 0.4

The [manuscript](manuscript.pdf) is a self-contained synthesis of the current
inverse-bulk investigation. It has its own equation labels and bibliography.
The [notes index](notes/README.md) retains the broader research history;
the [draft index](drafts/README.md) preserves reviewed versions.

| Manuscript part | Results and scope | Research source |
|---|---|---|
| Sections 1-3 | Exact-fitting objective, full Weil normalization, domains, physical positivity, conditional construction-to-RH implication, bounded-source exclusion, the spectral form of the target (2.4), and the fixed-interval versus compatible-family distinction. | [Foundational analysis](notes/ANALYSIS.md), [sphere/Schur comparison](notes/SPHERE_AND_SCHUR_PAIRINGS.md); all required background is restated and derived in the manuscript. |
| Section 4 | Real Gaussian Mellin density, oscillator gamma tower, archimedean phase, interacting charged-state Gram matrix and repetition failure. | [Sphere/Schur comparison](notes/SPHERE_AND_SCHUR_PAIRINGS.md). |
| Section 5 | Conformal electric norm, complete spherical-vector shift ratio, common-state RG pairing and undressed-return exclusion. | [Sphere/Schur comparison](notes/SPHERE_AND_SCHUR_PAIRINGS.md). |
| Section 6 | Electric dressing, one magnetic insertion with graph-domain proof, all local prime coefficients and compulsory contact, explicit continuous-input lift. | [Dressed Schur returns](notes/SCHUR_DRESSED_RETURNS_AND_GLUING.md). |
| Section 7 | Higher-power coefficient-domain restriction, mixed atom for constant-vector two-prime gluing, full contact/pole comparison, the interference bound with the two-channel exclusion theorem and its certificates (7.4), and the mirror prime reference with the prime-free subtraction form and the domination/compression criterion (7.5). | [Dressed Schur returns](notes/SCHUR_DRESSED_RETURNS_AND_GLUING.md). |
| Section 8 | Placement among spectral realizations of the zeros, what the exclusion leaves (contact by projection, the prime-free archimedean inequality, a mechanism for the poles, spectral measures as the object to compute), the finite local-factor phase bridge, and the open joint-source and subtraction problems. | Both focused notes and the [broad survey](notes/DEFECT_OBSERVABLE_SURVEY.md). |
| Appendix A | Positive gamma action, integer refinement, composition and contact identity. | [Foundational analysis](notes/ANALYSIS.md). |
| Appendix B | Winding versus transfer, central-semigroup exclusion, positive disk model, first-prime cusp and coherent contact failures. | [Gauge-transfer test](notes/GAUGE_TRANSFER_TEST.md). |
| Appendix C | Scoped obstruction to finite rational feedback. | [Foundational analysis](notes/ANALYSIS.md). |
| Appendix D | Eight checks and their limits, including the explicit-formula normalization check, the channel-bound certificates and the two conclusive step certificates of the prime-free check, with source provenance and draft preservation. | [Numerics index](numerics/README.md). |

New in 0.2: Corollary 2.2, Remark 3.8, Proposition 7.3, Lemma 7.4,
Theorem 7.5, Remark 7.6, Sections 8.1-8.2, two new check programs, and the
spectral-realization references.
New in 0.3: Section 7.5 entire - Proposition 7.7, Theorem 7.8, Corollary 7.9,
Remark 7.10 - together with Problem 8.2, the prime-free target (8.1), and
`check_mirror_subtraction.py`. Versions 0.1 and 0.2 are preserved in `drafts/`.
The research behind 7.5 is in
[MIRROR_REFERENCE_AND_SUBTRACTION_FORM.md](notes/MIRROR_REFERENCE_AND_SUBTRACTION_FORM.md).
New in 0.4: Section 2.5 entire - Lemma 2.3 and Proposition 2.4 - the revised
status of the prime-free target in 8.2 with Proposition 8.1 and the Yoshida
reference, the corresponding qualification of the Connes-Consani mechanism in
8.1, `check_prime_free_archimedean.py`, an author field and a preparation note.
The research behind 2.5 and 8.2 is in
[PRIME_FREE_ARCHIMEDEAN_INEQUALITY_20260915.md](notes/PRIME_FREE_ARCHIMEDEAN_INEQUALITY_20260915.md).

The broad survey's alternative theories remain in the notes rather than being
expanded into separate speculative manuscript sections. No common-field
junction, neutral nonabelian source, physical realization of the input lift,
full first-prime identity or all-support positivity theorem is claimed.

The positive gamma tower, local-factor identities and positive prime reference
are established background ingredients. The working contribution is the
specified source calculations and their scoped selection results; literature
priority for those calculations has not been established.

During manuscript preparation, the RG-flow paper's author attribution was
corrected to **Federico Ambrosino and Davide Gaiotto**, and the notes' link
labels were corrected accordingly. The paper is distinct from the
Gaiotto-Teschner Schur quantization paper.

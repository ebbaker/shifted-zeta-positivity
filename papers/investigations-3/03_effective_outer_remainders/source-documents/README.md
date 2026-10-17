# Effective outer remainders: source documents

16 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6-astra (Codex)**; reasoning effort: **ultra**.

Reference provenance and links to canonical sources.

The [initial proposal](../research-overview/01_INITIAL_RESEARCH_PROPOSAL_20261016.md)
links the inherited evidence. Existing notes, certificates and transcripts
remain at those canonical locations; do not copy or relocate them here.
Record bibliographic versions, theorem locations, imported hypotheses and
normalization conversions for new sources. Cite third-party papers rather
than committing their PDFs, under [LARGE_FILES.md](../../../../LARGE_FILES.md).

## Sources of note 01

Recorded 17 October 2026 by Claude Opus 5.5 (`claude-opus-5-5`, Claude
Cowork, reasoning effort max). How each source enters is stated in
Sections 1, 2 and 10 of
[note 01](../notes/round-1/01_HEIGHT_P_TRANSPORT_AND_LEMMA_AP_CLAUDE_20261017.md).
No PDF is committed.

| Source | Version read | Used for |
| --- | --- | --- |
| Project 01 [note 01](../../01_dirichlet_newman_families/notes/01_NORMALIZATION_AND_TRANSFER_CONTRACT_CLAUDE_20261017.md) (SHA-256 `8e6ea157…7b4e`), its [sources](../../01_dirichlet_newman_families/source-documents/README.md) and its [benchmark programme](../../01_dirichlet_newman_families/numerics/benchmark_family_contract_claude_20261017.py) | note read in full; programme Sections B and H | normalization (Dobner's kernel; Polymath's for zeta), Lemma 3.4, Proposition 3.3, ledger H3, H4 and H11, Platt's verified heights, the zeta rows X = 6·10¹⁰ + 83952 − 1/2 (Polymath) and 5·10¹² + 194858 (Platt–Trudgian), the Section 4.6 planning baseline |
| Hakimoglu-Brown, [arXiv:2610.12803](https://arxiv.org/abs/2610.12803) | not read in this session: the arXiv page was refused by the web proxy (rate limit) and no copy is in the repository; every statement is Project 01's reading (ledger H11) | the consumer S(x,p,t) and the strip comparison |
| [DLMF §5.9](https://dlmf.nist.gov/5.9) (Binet's formula for ψ) | quoted from memory, equation number not checked; confirmed numerically to 10⁻²⁹ | Lemma 4.3 |
| [21 Note 58](../../../investigations-2/active/21_quaternion_theta_geometry/notes/01_weighted_outer_remainders/58_EXPLICIT_CARRIER_PHASE_AND_CONDITIONAL_HEIGHT_20261015.md) and [22 outer Note 01](../../../investigations-2/active/22_theta_manifold_geometry/notes/06_effective_outer_bridge/01_LOW_INDEX_BUDGET_REFINEMENT_20261015.md) | read in full | Section 2.1, the inherited budget |

Later on 17 October Edward added the preprint to the project, and
[note 02](../notes/round-1/02_HAKIMOGLU_BROWN_COMPARISON_AND_UNCONDITIONAL_TABLE_CLAUDE_20261017.md) reads it in full.

## Sources of note 02

Recorded 17 October 2026 by Claude Opus 5.5 (`claude-opus-5-5`, Claude
Cowork, reasoning effort max). How each source enters is stated in
Sections 0, 4 and 10 of
[note 02](../notes/round-1/02_HAKIMOGLU_BROWN_COMPARISON_AND_UNCONDITIONAL_TABLE_CLAUDE_20261017.md).
No PDF is committed.

| Source | Version read | Used for |
| --- | --- | --- |
| C. Hakimoglu-Brown, [arXiv:2610.12803](https://arxiv.org/abs/2610.12803) | v1 (working draft of 7 October 2026), project copy `2610.12803v1.pdf`, read in full (26 pages) | Lemmas 2, 3, 6 and 10; Propositions 4, 7, 8 and 11; Theorems 9 and 12; Remark 5; Sections 8.1–8.2; Tables 2, 3 and 5–7 |
| D.H.J. Polymath, [arXiv:1904.12438](https://arxiv.org/abs/1904.12438) | not re-read; through the preprint and Project 01's ledger (H4, H7) | Section 8.4(a) (the boundary input of the preprint's Lemma 2, not replayed), Propositions 3.1(ii) and 6.1–6.2, Theorem 1.5(i) |
| D. Platt and T. Trudgian, Bull. London Math. Soc. 53 (2021) 792–797, [arXiv:2004.09765](https://arxiv.org/abs/2004.09765) | not read; Corollary 2 as quoted by the preprint | the published bound 0.2 |
| J. Gomila (20 August 2026) and S. Gordon (2026), preprints cited by the preprint | not read | priority caution only |

## Sources of note 02, Section 11 (literature check)

Recorded later on 17 October 2026 by Claude Opus 5.5 (`claude-opus-5-5`,
Claude Cowork, reasoning effort max). A Claude subagent read these through
a summarizing web-fetch tool, whose quotations are capped excerpts. None
was read in full, and no PDF is committed.

| Source | What was read | Used for |
| --- | --- | --- |
| S. Gordon, [dbn-upper-bound](https://github.com/stefangordon/dbn-upper-bound) at commit 64c47f2 and its [PDF](https://stefangordon.github.io/dbn-upper-bound/dbn-upper-bound.pdf) (September 2026) | README, manuscript/main.md, PDF excerpts | Λ ≤ 0.157656619 claimed without half-plane; start from the classical strip |
| Raymond, Zenodo [22867547](https://zenodo.org/records/22867547) (21 September 2026) and a conditional record of 10 October 2026 | record pages and repository excerpts | Λ < 0.149396 claimed; Λ < 0.116398 under the 7/8 hypothesis |
| Planat, [arXiv:2610.18214v1](https://arxiv.org/html/2610.18214) (13 October 2026) | HTML up to Section 3; the abstract and PDF pages were refused (HTTP 429) | Λ ≤ 0.148611789321711 under stated premises; Appendix A.1 unread |
| J. Gomila, [dbn-lambda-01787854-candidate-audit](https://github.com/judegomila/dbn-lambda-01787854-candidate-audit) at commit a74738d and blog post (August 2026) | README, PROOF_NOTE.md, blog; the PDF could not be parsed | Λ ≤ 0.1787854 claimed by Polymath's Theorem 1.2 |
| D. Platt, Math. Comp. 86 (2017) 2449–2467, [doi:10.1090/mcom/3198](https://doi.org/10.1090/mcom/3198) | abstract and accepted version | RH verified to imaginary part 30,610,046,000 |
| D.H.J. Polymath, [arXiv:1904.12438](https://arxiv.org/abs/1904.12438) | Section 1 and the statement of Theorem 1.5 (TeX source); Section 8.4 cut off by the fetcher | the barrier region of the preprint's (3); Theorem 1.5(i) for 0 < t ≤ 1/2 |

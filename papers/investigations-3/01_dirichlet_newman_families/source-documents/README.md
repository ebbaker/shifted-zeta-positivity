# Dirichlet Newman families: source documents

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
Cowork, reasoning effort max). Theorem locations, hypotheses and how each
source was read are in the hypothesis ledger, Section 2 of
[note 01](../notes/round-1/01_NORMALIZATION_AND_TRANSFER_CONTRACT_CLAUDE_20261017.md).
No PDF is committed.

| Source | Version read | Used for |
| --- | --- | --- |
| A. Dobner, [arXiv:2005.05142](https://arxiv.org/abs/2005.05142); Acta Arith. 201 (2021) 29–62, doi:10.4064/aa200603-23-7 | arXiv v2, printed PDF (equations (4)–(8), Theorems 1–3); journal numbering not checked | H1–H3, the normalization |
| D.H.J. Polymath, [arXiv:1904.12438](https://arxiv.org/abs/1904.12438); Res. Math. Sci. 6 (2019), doi:10.1007/s40687-019-0193-1 | v2: Theorem 1.2 in the printed PDF; Section 3, Theorems 1.3 and 1.5, Corollary 1.4 in the arXiv HTML rendering | H3, H4, H6, H7 |
| D. Platt, [arXiv:1305.3087](https://arxiv.org/abs/1305.3087); Math. Comp., doi:10.1090/mcom/3077 | abstract | H5 (verified heights) |
| Liu, [arXiv:2610.12234](https://arxiv.org/abs/2610.12234) | v1, project copy, read in full | H9 (claimed half-planes) |
| Hakimoglu-Brown, [arXiv:2610.12803](https://arxiv.org/abs/2610.12803) | v1, working draft of 7 October 2026; PDF supplied by Edward Baker during the session, read in full | H11, Sections 3.5 and 4.6 |
| Andrade–Chang–Miller, [arXiv:1310.3477](https://arxiv.org/abs/1310.3477) | abstract | H10, precedent search |
| Stopple, [arXiv:1301.3158](https://arxiv.org/abs/1301.3158) | abstract or HTML rendering | normalization comparison, precedent search |
| [LMFDB](https://www.lmfdb.org/Character/Dirichlet/) pages of the characters 3.2, 5.2, 5.4 and 7.2 (Conrey labels) | accessed 17 October 2026; the page of 4.3 did not load | zeros and root numbers in the normalization check |

The OpenAI preprints behind H8 and H9 are pinned in the
[arithmetic-source audit](../../../investigations-2/inactive/arithmetic_source_audit/README.md).

## Round-2 continuation

17 October 2026; gpt-6.1-sol (Codex), reasoning effort ultra. The
[continuation](../notes/round-2/02_BURGERS_FLOOR_AND_CONDITIONAL_COMPARISON_CODEX_20261017.md)
uses Dobner's strip-contraction theorem and the already reviewed time-zero
floor and paired-zero algebra. Its Burgers floor, completeness argument,
conditional comparison, and confinement control are derived in the note;
the exact scalar arithmetic is linked from numerics. The H12 hypothesis is
still open for characters. No additional published character-confinement
theorem is imported, and no novelty claim is made.

## Round 3 and the manuscript

17 October 2026; gpt-6.1-sol (Codex), reasoning effort ultra.
[Round 3](../notes/round-3/03_SINE_TAIL_LIMIT_AND_COMPARISON_CODEX_20261017.md)
uses Cardon's general strip-operator theorem for the sine-tail approximants;
Dobner's Fourier-kernel theorem alone would not cover them. No third-party
PDF is committed.

| Source | Version and location checked | Import or correction |
| --- | --- | --- |
| D. A. Cardon, *Complex zero strip decreasing operators*, [arXiv:1401.0237v2](https://arxiv.org/abs/1401.0237v2), [journal DOI](https://doi.org/10.1016/j.jmaa.2015.01.026) | v2; Theorem 1.5, printed p. 3, checked against HTML and rendered PDF | Genus-one strip class; phi(z)=exp(-t z^2), alpha^2=2t, input quadratic factor gamma_2=0. Gives strip sqrt(max(1-2t,0)) for each approximant |
| H. Ki, Y.-O. Kim, J. Lee, *On the de Bruijn–Newman constant*, Adv. Math. 222 (2009), 281–306, [DOI](https://doi.org/10.1016/j.aim.2009.04.003) | Section 6, Example 1, pp. 303–304; original article inspected through its [full transcription](https://paperzz.com/doc/6928362/on-the-de-bruijn%E2%80%93newman-constant), bibliographic identity checked against DOI | Earlier qualitative strict bound below 1/2 for real primitive characters. Corrects round 1's search statement. Their complex-character example is a real self-dual combination, distinct from the individual non-even family here |

The approximation, global floor, common sub-Gaussian majorant, and endpoint
are derived in the note. The manuscript makes no priority claim. The
standalone H12 assertion for the original character flow is still open.

## Review continuation: public provenance

17 October 2026; gpt-6-astra (Codex), reasoning effort max, with substantial
LLM assistance for Edward Baker. Source checked during
[review 03](../reviews/03_CROSS_MODEL_MATHEMATICAL_REVIEW_CODEX_20261017.md).

[MathOverflow question 515667](https://mathoverflow.net/questions/515667/do-de-bruijn-newman-constants-of-dirichlet-l-functions-tend-to-0-as-the-cond),
posted by khonsu on 1 October 2026 and edited 2 October, discusses the
conductor limit and a heuristic log-log(q)/log(q) scale. It acknowledges
unfinished uniform positive-time counting and finiteness steps. Record it
as incomplete provenance; no theorem is imported and no priority conclusion
follows. The displayed account name is not an identification of its author.

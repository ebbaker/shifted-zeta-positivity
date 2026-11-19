# Platt–Trudgian and Gomila: source reading receipt

19 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance; guarded chat configuration **gpt-6-astra,
reasoning effort max**. Supports [Discussion12][discussion]. Selected
primary-source reading and comparison with existing internal audits;
not a new independent certificate validation.

## Platt–Trudgian

Dave Platt and Tim Trudgian, **The Riemann hypothesis is true up to
3·10^12**, arXiv:2004.09765v1, 21 April 2020; published in *Bulletin of
the London Mathematical Society* (2021), [DOI][ptdoi].
[Version-pinned record][ptabs] · [HTML read][pthtml] · [PDF source][ptpdf].

Read the short article's scientific text, especially Theorem 1, Section 2
and Section 3.4/Corollary 2. Checked the exact verification endpoint, the
role of rigorous sign changes and completeness, and the deduction of the
0.2 Newman bound using Polymath Table 1. The conversion is X=2H.
No re-execution of the RH verification and no imported individual-gap
enclosures. The existing canonical reference catalog is
[heat-flow RH applications][ptcatalog]; its BibTeX key is retained.

Existing reading copy reidentified, not redownloaded:

- Path: `/Users/Shared/szp-archive/heat-flow-rh-applications/references/2004.09765v1.pdf`.
- Size: **133056 bytes**.
- SHA-256: `3362f66af9fa9373977eee70e2282ec33989d5d8b97e0852df9e32cc25b52885`.

## Gomila

Jude Gomila, **A new ceiling for Λ: the de Bruijn–Newman constant is at
most 0.1787854**, author website, dated 19 August 2026; [live page][blog]
retrieved 19 November 2026. The page has later research additions and no
immutable version identifier; the dated retrieval does not date each
addition. Read its criterion, finite approximation, tail, barrier,
provenance and later-research discussion, then inspected the primary
proof repository rather than relying on the popular explanation alone.

The [web commit listing][commits] returned
`a74738deb6d5e0f76887cb36901da08b68dca705` (21 August 2026), matching the
repository's earlier [source pin][oldpin]. The pinned [proof note][proof]
and [native-binding lemma][binding] were opened explicitly. Also inspected
the main-branch README's certificate summaries and release hierarchy.
This is a pinned-document reading; no fresh local clone or new full-tree
hash verification was performed. The API attempt to resolve HEAD failed;
the web commit listing supplied the inspected pin.

The proof note supplies the parameter row and precise criterion domains;
the native-binding lemma supplies the coefficient convolution and the
transfer to |f_t|. It also distinguishes the conservative 10.50 remainder
constant used by the package from the 10.44 display. The README identifies
the sealed release paper as primary, with the supplied external exposition
subject to a correction list. The package states that peer review is
pending. Neither the blog's review descriptions nor the earlier internal
LLM audit is promoted here to independent specialist validation.

The blog's later **0.1782354** calculation is recorded only as an attributed
report with mathematical review pending. Its supporting research package
was not audited; it is not substituted for the pinned 0.1787854 result.

A download of the public release PDF to an external temporary reading
path was attempted from the [pinned raw URL][releasepdf]. Local network
name resolution failed. No new PDF copy, byte size or hash is claimed.
The accessible proof-note and native-binding text support this comparison.
No third-party PDF or certificate corpus was placed in the repository.

## Relation to the earlier audit

Use the [Cluster11 summary][cluster] and [October review][review] for
the retained-C correction's scoped applicability issue and the extent of
independent replay in this repository. The review corrects stronger claims
in the first benchmark note; do not reuse its sensitivity number as a
universal limit. Existing Polymath source ownership remains in
[Receipt02][polyreceipt]. Reusable citations are in [references.bib](references.bib).

[discussion]: ../notes/12_VCD_GT_CM_UPPER_BOUND_COMPARATORS_AND_PROGRAM_REFINEMENT_20261119.md
[ptabs]: https://arxiv.org/abs/2004.09765v1
[pthtml]: https://arxiv.org/html/2004.09765v1
[ptpdf]: https://arxiv.org/pdf/2004.09765v1
[ptdoi]: https://doi.org/10.1112/blms.12460
[ptcatalog]: ../../../../../../investigations-5/02_heat_flow_rh_applications/references/README.md
[blog]: https://www.judegomila.com/posts/riemann-lambda-0.1787854
[commits]: https://github.com/judegomila/dbn-lambda-01787854-candidate-audit/commits/main/
[proof]: https://github.com/judegomila/dbn-lambda-01787854-candidate-audit/blob/a74738deb6d5e0f76887cb36901da08b68dca705/PROOF_NOTE.md
[binding]: https://github.com/judegomila/dbn-lambda-01787854-candidate-audit/blob/a74738deb6d5e0f76887cb36901da08b68dca705/NATIVE_BINDING.md
[releasepdf]: https://raw.githubusercontent.com/judegomila/dbn-lambda-01787854-candidate-audit/a74738deb6d5e0f76887cb36901da08b68dca705/gomila_dbn_lambda_01787854_release.pdf
[oldpin]: ../../../../../../investigations-2/newman_certificate_audit/notes/1_SOURCE_PIN_AND_DEPENDENCY_LEDGER_20261012.md
[review]: ../../../../../../investigations-2/newman_certificate_audit/reviews/CROSS_MODEL_REVIEW_OF_CLAUDE_AUDIT_CODEX_20261013.md
[cluster]: ../../../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[polyreceipt]: 02_HEIGHT_DENSITY_SOURCE_CHECK_20261119.md

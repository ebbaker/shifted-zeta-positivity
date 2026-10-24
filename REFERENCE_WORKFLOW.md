# Research reference workflow

23 October 2026, America/New_York. Standing guidance requested by Edward Baker. Prepared with substantial LLM assistance, **gpt-6-astra (Codex), reasoning effort ultra**.

Whenever a relevant research article is found during repository work, add it promptly to the affiliated investigation's `references/` folder. Create that folder if needed. For repository-wide work use the root [`references/`](references/README.md). Record the reference when it is found; do not wait for a manuscript or a later bibliography cleanup.

## What to keep

Each reference record should include:

- Authors, exact title, publication or preprint identifier, version and date where available, and stable primary-source links. Prefer a version-pinned arXiv link or DOI; distinguish the version read from a newer unexamined version.
- A short explanation of relevance and links to the research notes or manuscript sections using it.
- The exact theorem, equation, section or page relied on, its hypotheses and scope, and what was actually checked. Distinguish discovery, abstract-only inspection, checked passages and full reading. A downloaded PDF is not evidence that its claims have been verified.
- Any limitations that matter for use: extra hypotheses, cumulative versus local bounds, normalizations, uniformity, unproved claims, corrections and withdrawals. An approximation or related mechanism is not a novelty claim.
- Retrieval date and, for an archived PDF, its source URL, local archive path, byte size and SHA-256 hash. A hash identifies the retrieved file; it does not validate its mathematics.

Maintain a short `README.md` index and a reusable BibTeX bibliography. A compact machine-readable catalog and download manifest are useful when several articles are involved. Use one canonical record per article within an investigation; link across investigations rather than duplicating annotations unnecessarily. On later use, update the record with newly checked passages or a newly examined version, preserving the earlier version/provenance when relevant.

## PDFs and storage

Follow [`LARGE_FILES.md`](LARGE_FILES.md), especially its third-party-material rule, and the [root reference guide](references/README.md). **Do not commit third-party PDFs to Git, whatever their size.** Keep citation records, original short annotations, BibTeX and small manifests in the repository. Do not copy full abstracts or substantial article text into annotations.

When a public article PDF is available and relevant, retain a local reading copy outside the repository, normally under `/Users/Shared/szp-archive/<investigation-slug>/references/`, with a versioned filename such as `2005.05142v2.pdf`. Download only from an authorized accessible source. Verify the response is a PDF, record its SHA-256 and size, and never overwrite a different version silently. Do not bypass access controls. If retrieval fails or no authorized PDF is available, keep the citation and stable link, state the availability accurately, and continue work that does not require the missing text.

The machine's archive location is a convenience, not a reader dependency: every record must retain a stable public source link. If code later consumes archived files, follow the repository's archive lookup and hash-check conventions. Online references such as DLMF may remain linked records with section numbers and retrieval dates instead of artificial PDF copies.

## Research and review discipline

Check the primary source before importing a theorem. Preserve its assumptions, normalization, quantifiers and limiting regime. Attribute an existing argument when it is discovered, including after deriving a similar argument independently. Record uncertainties instead of filling missing details from memory. Cross-check new claims against the repository's [result summaries](result-summaries/README.md) and [patterns to avoid](avoid/README.md), particularly [unchecked imports and novelty claims](avoid/16_unchecked_imports_and_novelty_claims.md).

Backfill references as investigations are resumed, starting with papers already used in their current notes and manuscripts. Do not describe a partial backfill as a complete repository-wide audit.

The initial implementation is [Investigation 12's reference collection](papers/investigations-4/12_height_dependent_heat_contours/references/README.md). Generated `AGENTS.md` files and synced project sources remain unchanged.

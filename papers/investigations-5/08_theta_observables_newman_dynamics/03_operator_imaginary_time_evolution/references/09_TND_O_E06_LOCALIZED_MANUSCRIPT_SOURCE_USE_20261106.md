# Sources used in the localized-statistics manuscript integration

6 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance from **OpenAI Codex**. The exact model identifier and reasoning effort were not exposed in the available session metadata; neither is inferred from earlier sessions.

This is a selected-passage check for E06, not a new literature survey or
full-paper assessment. Existing external reading copies remain outside Git.

| Source | Inspection and use |
| --- | --- |
| Polymath, arXiv 1904.12438v2 | Fresh primary HTML, Section 3, Propositions 3.1 and 3.3 and Theorem 3.2: complex-zero dynamics, strip contraction and all barrier hypotheses. The manuscript derives its finite-cluster equations directly; only the global comparison imports the full dynamics. Canonical key Polymath2019 in Investigation 02 is reused. |
| Maples–Rodgers, arXiv 1404.3080v2 | Existing PDF text inspected for Theorem 1.2; page 5 rendered and inspected for the exact Proposition 2.5 moment, width and constant ranges. Used for fixed k, 1<=H<=T^(1/4), 0<c<1/2 and 1/2<sigma<1. No uniform microscopic estimate is inferred. |
| Rodgers, arXiv 1502.05658v3 | Existing PDF text and rendered page 2 checked for Theorem 1.1 / Corollary 1.2: the sharp tail assumes RH and averages over centers. The unconditional remark is not promoted to a new input. |
| Earlier complex-statistics and operator sources | Existing manuscripts and source-use records 01–08 are reused at their recorded scope. No fresh full-paper audit of BGST, KKL, Montgomery, Rudnick–Sarnak or the operator references is claimed. |

Fresh arXiv HTML/PDF requests for the two local-statistics papers failed;
the retained local PDFs identified by LOCALIZED_STATISTICS_PDF_RECEIPTS_20261106.json
provided the primary reading copies. Their hashes were checked against
that receipt. Polymath HTML was available at
https://arxiv.org/html/1904.12438v2.

The build composes 20 cited records from canonical bibliography files.
No third-party PDF or duplicate canonical bibliography is added to Git.
The finite-window sine calculation, Gram identity, tube inequalities and
plateau comparison are derived in the manuscript, not attributed as new
arithmetic theorems of these authors.

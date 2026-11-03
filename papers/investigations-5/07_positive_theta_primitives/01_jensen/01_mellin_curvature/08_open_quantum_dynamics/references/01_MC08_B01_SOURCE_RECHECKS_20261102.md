# MC08-B01 primary-source rechecks

2 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance; actual **gpt-6-astra (Codex), reasoning effort max**, chat `01a19dd8-047f-7212-b770-1a8bc3800761`.

This records follow-up inspection of three existing entries in the [canonical catalog](../../../../references/sources.json), with bibliography and original provenance in [source record 12](../../../../references/12_OPEN_QUANTUM_DYNAMICS_SOURCES_20261102.md). No new article or BibTeX entry is added. Existing external PDF receipts remain unchanged; this round inspected primary HTML and did not reread the PDFs or claim a full-paper audit.

| Existing catalog key and primary version | Passages rechecked on 2 November 2026 | Use and limit |
| --- | --- | --- |
| [CastinDalibardMolmer08054002v1](https://arxiv.org/html/0805.4002v1), Castin, Dalibard and Mølmer | Section 1, equations (2), (4)–(11); Section 2, equations (14)–(16) and discussion of reservoir correlation time | Confirms jump/no-jump normalization and ensemble convention. Physical coarse-graining restrictions are explicit; it does not prove this packet's collision limit or infinite-Fock theorem. |
| [Prosen08011257v3](https://arxiv.org/html/0801.1257v3), Prosen | Section 2, equations (1)–(6); Section 2.1, equations (20)–(23) and even-operator restriction | Finite quadratic Hamiltonians/linear bath operators; convert factor-two jumps to this project's convention. Even physical operators are distinguished from unrestricted operator-space formulas. No time-dependent or infinite-mode diagonalization theorem is imported. |
| [RivasHuelgaPlenio09114270v2](https://arxiv.org/html/0911.4270v2), Rivas, Huelga and Plenio | Introduction, equations (1)–(2) and surrounding time-dependent generator/composition discussion | CP-divisibility vocabulary. No claim about every definition of Markovianity, unbounded domains or an exact finite reservoir follows. |

Application: [B01 decision](../notes/02_OPEN_SYSTEM_ARCHITECTURE_DECISION_20261102.md) and [E02 r1](../research-progress/handoffs/02_MC08_E02_CONSTRUCTION_CONTRACT_R1_20261102.md). Their graded collision formula, cutoff compatibility and coherent flag readout are explicit local derivations/proof obligations, not quotations or imported theorems from these sources. Prosen's rendered title-page date is not used; the catalog retains the actual arXiv v3 date of 4 December 2008.

# Primary-source ledger for the global YM-to-Weil assessment

Date checked: 24 September 2026, America/New_York.  
Prepared for Edward Baker with substantial LLM assistance.  
Model exposed: GPT-6 (Codex); exact variant and configured reasoning effort not exposed, not inferred.  
Status: selective literature verification, not a claim to have independently re-proved the cited papers or exhausted the literature.

The conclusions and candidate rankings are in the [review](../reviews/GLOBAL_MECHANISMS_CRITICAL_REVIEW_20260924.md). The [determination note](OFF_DIAGONAL_RIGIDITY_AND_COMPACT_SOURCE_EXISTENCE_20260924.md) and [operator controls](SOURCE_SPECTRA_MODULAR_AND_LIOUVILLE_CONTROLS_20260924.md) distinguish session deductions from the literature.

## 1. Search design and access

The search covered four different mechanisms: arithmetic representations and trace formulas; fixed-state loop/moment extension; modular and energy-difference actions; and global causal/positive-pairing alternatives. Searches included the original authors and theorem terminology, followed by source PDFs. Broad results, including secondary summaries and claimed RH proofs, were used only to locate primary documents and were not treated as evidence.

The candidate screen required a plausible all-support mechanism, explicit state and representation requirements, and some way arithmetic could enter. Lexical appearances of “Yang–Mills,” “zeta,” or “positivity” did not count as a bridge. Generalized holonomy measures, thermal partition functions, nuclear characters, and OS vector norms were kept as different object types.

Decisive printed pages were rendered with Poppler and inspected; text extraction was used to locate them. Downloaded third-party PDFs and temporary page images remained under the system temporary directory, outside the repository. No third-party PDF is added to git. No numerical experiment or zero-spectrum fit was run.

## 2. Source locations and verification scope

| Key | Primary source | Specific material inspected | Verification and use |
|---|---|---|---|
| M | Ralf Meyer, [A spectral interpretation for the zeros of the Riemann zeta function](https://arxiv.org/pdf/math/0412277), v3 (2013 revision of 2004 preprint) | §§3–5; Theorem 4.1, Corollary 4.2, Lemma 5.7, Theorem 5.8; printed pp. 8, 12–13 visually inspected | Checked quotient/dual object types, character signs, prime calculation, and trace domains. No positivity theorem attributed to it. |
| CC | Alain Connes and Caterina Consani, [Weil positivity and Trace formula, the archimedean place](https://arxiv.org/pdf/2006.13771), 2020 | Theorem 6.11; Appendices B–C, especially Proposition C.1; printed pp. 50–51 visually inspected | Restricted criterion and normalization checked. The short-support theorem is not promoted to all supports. Numerical constants in the paper were not recomputed. |
| CCM | Connes, Consani, Moscovici, [Zeta zeros and prolate wave operators: semilocal adelic operators](https://arxiv.org/pdf/2310.18423), v2 (4 May 2024) | §4.7, Theorem 4.6, §4.8; printed p. 23 visually inspected | Checked metric/isomorphism wording and finite-place scope. Earlier notes cite v1 with different theorem numbering. |
| C | Alain Connes, [Trace formula in noncommutative geometry and the zeros of the Riemann zeta function](https://arxiv.org/pdf/math/9811068), v1 | Introduction and explicit-formula discussion, including appendix theorem on normalization | Background cross-check of spectral versus trace-formula claims. Not used as an independently proved global positivity result; no full-proof audit. |
| KZ | Vladimir Kazakov and Zechuan Zheng, [Bootstrap for Finite N Lattice Yang–Mills Theory](https://arxiv.org/pdf/2404.16925), v4 (4 December 2024) | Introduction, trace reductions, §2 loop equations, conclusion; title/abstract page visually inspected | Checked special SU(2) closure claim and its infinite loop space. No convergence theorem for the proposed arithmetic bootstrap inferred. |
| Ch | Sourav Chatterjee, [Rigorous solution of strongly coupled SO(N) lattice gauge theory in the large N limit](https://arxiv.org/pdf/1502.07719) | Theorems 9.1–9.2 and uniqueness proof structure; printed p. 35 visually inspected | Checked group, large-N limit, small-coupling hypothesis, and growth class. These restrictions remain explicit in the comparison. |
| AL | Abhay Ashtekar and Jerzy Lewandowski, [Representation Theory of Analytic Holonomy C* Algebras](https://arxiv.org/pdf/gr-qc/9311010), v2 | Theorems 3.5, 4.3–4.4, Appendix B; printed p. 25 visually inspected | Checked generalized-connection/measure reconstruction. Its canonical measure is not identified with the Wilson or continuum YM state. |
| L | Jean B. Lasserre, [Global Optimization with Polynomials and the Problem of Moments](https://web.mit.edu/~a_a_a/Public/Publications/refs_for_seb_blog/Lasserre.pdf), SIAM J. Optim. 11 (2001), 796–817 | Assumption 4.1, Theorem 4.2; printed pp. 809–810 visually inspected | Checked the extra compactness/Archimedean hypothesis and convergence statement. No arithmetic finite-feasibility conclusion inferred. |
| BW | Joseph J. Bisognano and Eyvind H. Wichmann, [On the duality condition for a Hermitian scalar field](https://doi.org/10.1063/1.522605), J. Math. Phys. 16 (1975), 985–1007 | Introductory boost identity; Theorem 2 and discussion of Tomita polar decomposition, pp. 985, 997–998 | Original paper inspected through an [institutional PDF copy](https://denebola.if.usp.br/~jbarata/leituras-recomendadas/BisognanoWichmann-01-DualityConditionHermitianScalarField_985_1_online.pdf). Application to a YM observable net is conditional on the needed hypotheses. |
| BC | Jean-Benoît Bost and Alain Connes, [Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory](https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/CONNES/1994-1998/M_95_38/M_95_38_web.pdf), 1995 | §6, energy formula (3), Gibbs formula in Theorem 25; printed p. 33 visually inspected | Checked inverse-temperature regime and actual state formula. Partition function is not treated as a Weil norm identity. |
| B | Jean-François Burnol, [An adelic causality problem related to abelian L-functions](https://arxiv.org/pdf/math/0001013), v3 (2000) | Definitions 1.4/1.9, Theorems 1.7 and 1.11; printed p. 5 visually inspected | Checked which causality condition is equivalent to RH. No identification with the project's shifted transfer is claimed. |
| D | Christopher Deninger, [The Hilbert–Polya strategy and height pairings](https://arxiv.org/pdf/1001.1621), 2010 | Introduction, Conjecture 2, and positive-pairing discussion | The paper's conjectural status is retained. Text inspected; no independent construction of the conjectured arithmetic cohomology. |
| H | Håkan Hedenmalm, [Spectral interpretation of Riemann zeta zeros](https://arxiv.org/pdf/2606.17494), 2026 preprint | Theorem 3.3.3; §4, Theorem 4.2.2 and Corollary 4.2.3; printed p. 8 visually inspected | Checked that the positive compatible form is a hypothesis. This recent preprint is a screened alternative, not an established YM bridge or RH proof. |

The original Wilson and Lüscher references in earlier notes were not re-audited in full. The finite-slab factorization used here is checked directly from the displayed finite integral. No claim stronger than the older notes' disclosed abstract-level Lüscher check is based on that citation.

## 3. Important source-reading distinctions

**Mellin conventions.** For the logarithmic test \(f\), the uncentered multiplicative function is \(u^{-1/2}f(\log u)\), whose Mellin values at 0 and 1 are the two moments being removed. The old outline's \(Q\) is the zero contribution, with the signs appropriate to its gamma-minus-primes convention. Meyer's virtual character is poles minus zeros. On the pole-neutral convolution the pole character vanishes, so a minus sign remains between that virtual character and the desired \(Q\). A positive trace cannot be inferred merely by ignoring the grading.

**Meyer domains.** Corollary 4.2 is expressly about the transpose on the continuous dual. The rendered p. 13 also contains a warning about a formal expression and a footnote specifying a multiplier interpretation. Accordingly the assessment relies on the stated character result and checked prime calculation; it does not transfer its shorthand unbounded-operator products into YM.

**Semilocal metrics.** The checked v2 page uses Theorem 4.6, while the earlier repository link to v1 uses Theorem 4.13. This is a version/numbering distinction, not by itself an error in the earlier reference. The Hilbertian isomorphism does not say that the same unchanged ambient norm works at every finite set of places.

**Convergence versus feasibility.** Lasserre supplies convergence under its stated assumptions for an already posed optimization problem. Chatterjee supplies uniqueness and convergence for a particular complete loop system. Neither establishes that an enlarged system containing arithmetic-source constraints has any feasible point.

**Modular hypotheses.** BW is a theorem about a field representation with substantial relativistic and analytic structure. Assuming OS positivity on a chosen source domain alone does not verify those hypotheses, nor the existence of a continuum YM net.

**New spectral proposals.** Hedenmalm's conditional inner-product step is exactly the kind of metric-existence problem that remains important here. Renaming that step “self-adjointness of a pair” does not provide it.

## 4. Status ledger for the session's own claims

| Claim | Status | Where the argument is recorded |
|---|---|---|
| Old fixed-support asymptotic, weighted-flow cancellation, compact source criterion | Re-derived at the stated scope | Review §2 |
| A separately native generator is not necessary for bare source existence | Logical correction of the research formulation | Review §2.2; determination note §1 |
| Separated-support identity leaves exactly three local constants under the stated symmetries/growth | Proved session deduction, with a sharpness control | Determination note, Theorem 1 |
| Arbitrary finite compatibility in fixed compact source balls yields a global map | Proved sufficient criterion; feasibility remains open | Determination note, Theorem 2 |
| Gauge-compatible weighted elliptic source control and tail estimate | Proved control lemma in the fixed finite slab | Determination note, Lemma 3 |
| Exact source image has discrete zero-ordinate spectrum, multiplicities as weights | Conditional deduction from exact positivity and the explicit formula | Operator controls, Proposition 1 |
| Current boundary modular flow is trivial | Direct proof for the stated trace/algebra | Operator controls, Proposition 2 |
| Vacuum geometric wedge boosts cannot implement exact arithmetic translations under the listed hypotheses | Scoped deduction with proof and controls | Operator controls, Lemma 3/Corollary 4 |
| Thermal detailed balance and its centered-source correction | Direct spectral calculation | Operator controls §4 |
| A genuine arithmetic module/source law occurs in pure 4D YM | Not established |
| Mixed gamma/prime identity, arbitrary finite arithmetic feasibility, or native shifted-transfer realization | Not established |

## 5. What would change the recommendation

A meaningful positive development would be a YM-derived mixed identity, a noncircular occurrence theorem with controlled metric, or a proof of arbitrary finite feasibility tied to such a source law. A negative development would be a counterexample to one of those specified claims.

More positive finite matrices, a zeta partition function in an attached system, or another two-sided generator without arithmetic matrix elements would not change the present assessment.

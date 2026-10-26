# Recurrence references

26 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra (Codex), recorded effort max**.

The [initial brainstorm](../brainstorm/01_RECURRENCE_AND_GENERALIZED_TRANSFORM_HIERARCHIES_20261026.md)
reuses the checked source collection in the sibling
[ansatz reference catalog](../../ansatz/references/README.md), especially
its 26 October generalized-transform section. That catalog owns the
canonical annotations, retrieval dates, version information and reading
limits. The reusable bibliography is
[ansatz/references/references.bib](../../ansatz/references/references.bib);
use that shared file rather than maintaining a divergent copy.

| Topic | Source and retained inspection scope |
| --- | --- |
| Canonical heat field and RS inputs | [Polymath, arXiv:1904.12438v2](https://arxiv.org/html/1904.12438v2), selected source identities and propositions; imported coefficient providers retain the catalog's audit limits. |
| Gamma and Hermite structure | [DLMF 5.11](https://dlmf.nist.gov/5.11) and [18.12.15](https://dlmf.nist.gov/18.12.E15); checked formulas and stated sector assumptions. |
| ADHM and generalized transforms | [Ward, arXiv:2006.01459v2](https://arxiv.org/html/2006.01459v2), selected introduction and sections; [Donaldson–Kronheimer chapter](https://doi.org/10.1093/oso/9780198535539.003.0003), publisher discovery only, chapter unread. |
| Inverse scattering | [AKNS 1974](https://doi.org/10.1002/sapm1974534249), publisher abstract; [KdV 1967](https://doi.org/10.1103/PhysRevLett.19.1095) and [sine-Gordon 1973](https://doi.org/10.1103/PhysRevLett.30.1262), abstract/discovery records. |
| Quantum-chemical approximation | [Pople 1999](https://doi.org/10.1103/RevModPhys.71.1267), metadata and indexed official Nobel lecture excerpt; PDF retrieval was unavailable. |
| BBGKY and closure | [Akbari et al., arXiv:1204.4395v1](https://arxiv.org/abs/1204.4395v1) and [Updike–Burby, arXiv:2310.10940v1](https://arxiv.org/abs/2310.10940v1), abstracts inspected; retained PDFs were not fully read. |

No theorem from the analogy sources is imported into the recurrence.
The original source retrieval and external PDF hashes remain in
[the retrieval manifest](../../ansatz/references/TRANSFORM_REFERENCE_RETRIEVAL_20261026.json).
This folder creation adds no new literature search or reading claim.
Keep third-party PDFs outside Git and follow
[REFERENCE_WORKFLOW.md](../../../../../REFERENCE_WORKFLOW.md).

## R01--R03 primary-input recheck, 26 October 2026

For Edward Baker with substantial LLM assistance, gpt-6.1-sol, actual
effort ultra; same-model read-only source check. The shared ansatz catalog
continues to own bibliographic records. For the uses in Notes02--04:
[DLMF 5.11.2](https://dlmf.nist.gov/5.11.E2) and
[5.11(ii)](https://dlmf.nist.gov/5.11.ii) were checked for the closed-sector
digamma remainder; interior Cauchy then gives the analytic ell-second-
derivative bound on |z-X|<=X/4 and its all-order coefficient majorant.
[Polymath v2](https://arxiv.org/pdf/1904.12438v2), Proposition6.2 (56),
pp.22--23, with prefactor (38), p.17, was checked at real sigma=1/2,
Tprime=u/2>0, positive integer K. It gives the initial remainder with
2^(7/4)/7, Gamma((K+1)/2), (1.1/a)^(K+1), and a^-1/2. No negative-time
import of Proposition6.3, derivative allowance, K=0 assertion, independent
coefficient-provider implementation or complexity theorem is made.
No new reference or third-party PDF was added to Git.

## R05 growing-order quantifier recheck, 26 October 2026

For Edward Baker with substantial LLM assistance, actual gpt-6.1-sol,
ultra. Rechecked [Polymath v2 Proposition6.2](https://arxiv.org/html/1904.12438v2#S6.SS2),
(48)--(56): K is any positive integer at real sigma=1/2,Tprime>0.
There is no hidden upper K constraint; the negative-sigma qualification
is irrelevant here. Its explicit Gamma factor remains in Note05 and
2p<=a_min² is a separate retained-sum size gate. No Proposition6.3
negative-time import or provider implementation claim. The shared
ansatz catalog and bibliography retain ownership; no new article/PDF.

## R05-AN02 evaluation sources — 26 October 2026

[Selected-source audit](02_RS_EVALUATION_SOURCE_AUDIT_20261026.md)
records PartI discovery/access limits and the exact PartII coefficient
identities used, excluding its unproved technical inequalities. New
Arias bibliography entries are in [references.bib](references.bib); the
shared ansatz bibliography still owns earlier records.

The [retrieval record](RS_EVALUATION_REFERENCE_RETRIEVAL_20261026.json)
now identifies the authorized PartII v1 reading copy outside Git, with
size/hash and PartI access limits. DLMF3.5(v) positive Gauss weights and
polynomial exactness were checked for the derived Note06 analytic bound;
its shared bibliography record remains canonical.

## R05-AN03 finite providers — 26 October 2026

For Edward Baker with substantial LLM assistance, actual **gpt-6.1-sol,
ultra**, recurrence chat0003. [Source Audit03](03_FINITE_PROVIDER_SOURCE_AUDIT_20261026.md)
records DLMF infinite products, special values/recurrence and Gauss
reading, with limits and links. The new gamma-product bibliography entry
is in [references.bib](references.bib). The finite truncation, root and
rounding bounds are derived in Note09, not imported as library guarantees.

## R05-AN04 efficient providers — 26 October 2026

For Edward Baker with substantial LLM assistance, actual **gpt-6.1-sol,
ultra**, recurrence chat0003. [Source Audit04](04_EFFICIENT_PROVIDER_SOURCE_AUDIT_20261026.md)
checks the complex log-gamma remainder, Bernoulli Fourier bound and
Legendre identities used in Note10. New Bernoulli/Legendre entries are
in the local bibliography; the shared ansatz DLMF5.11 entry remains
canonical. Polynomial bit-cost and onset arguments are derived in Note10,
not imported library guarantees. No third-party PDF added.

## R05-AN05 explicit calibration — 26 October 2026

For Edward Baker with substantial LLM assistance, actual **gpt-6.1-sol,
ultra**, recurrence chat0003. [Source Audit05](05_EXPLICIT_CALIBRATION_SOURCE_AUDIT_20261026.md)
checks the sectorial digamma/log-gamma errors, beta integral, exact
half-gamma modulus and the N=1 finite-sum zeta representation. The shared
gamma and local special-value records remain canonical; new beta/zeta
entries are in the local bibliography. Explicit uniform constants and
all-height arguments are derived in Note11, not imported library claims.

# Primary sources for the microscopic wall/count continuation

26 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort ultra**.
Retrieval date: 26 October 2026. These are checked-passage records, not full
literature reviews or independent verification of the papers' proofs.
The application is [HCB Note04](../notes/04_HORIZONTAL_WALL_ACQUISITION_AND_ENDPOINT_COUNT_20261026.md).

## Carneiro–Chandee–Milinovich: argument bound

Emanuel Carneiro, Vorrapan Chandee, Micah B. Milinovich,
*Bounding S(t) and S_1(t) on the Riemann hypothesis*, Math. Ann. 356(3)
(2013), 939–968. [DOI](https://doi.org/10.1007/s00208-012-0876-z),
[arXiv:1309.1526v1](https://arxiv.org/abs/1309.1526v1), submitted
6 September 2013; this is the examined version.

Checked: pp.1–2, definition of S, zero-count relation, and Theorem2.
Under RH, the theorem bounds |S(t)| by one quarter of log(t)/loglog(t),
with a stated secondary term. HCB uses it after a bounded-variation
kernel integration, not as an exact short-interval count. Onsets and
constants have not been instantiated in HCB. The bound permits repeated
zeros and supplies no real endpoint nonvanishing statement.

## Carneiro–Chandee: logarithmic modulus identity

Emanuel Carneiro, Vorrapan Chandee, *Bounding ζ(s) in the critical strip*,
J. Number Theory 131 (2011), 363–384.
[DOI](https://doi.org/10.1016/j.jnt.2010.08.002),
[arXiv:1008.4970v1](https://arxiv.org/abs/1008.4970v1), submitted
29 August 2010; this is the examined version. The PDF front matter also
prints a later compilation date; that is not a newly examined version.

Checked: introduction and §2, especially the Hadamard/Stirling derivation
of equation(2.1), with its sum over all nontrivial ordinates under RH.
HCB rederives the elementary identity uniformly for the shrinking offset
α−1/2=1/L; it does not substitute that offset into a theorem with
unexamined parameter dependence. The paper's extremal-function bounds
and their detailed proofs were not imported.

## Goldston–Gonek: local count uncertainty

D. A. Goldston, S. M. Gonek, *A note on S(t) and the zeros of the Riemann
zeta-function*, Bull. Lond. Math. Soc. 39(3) (2007), 482–486.
[DOI](https://doi.org/10.1112/blms/bdm032),
[arXiv:math/0511092v1](https://arxiv.org/pdf/math/0511092v1), submitted
3 November 2005; this is the examined version.

Checked: pp.1–2, equations(1)–(6), Theorem1 and its range
0<h≤sqrt(t). Under RH the local count differs from its smooth main
term by at most (1/2+o(1))log(t)/loglog(t). HCB applies it to an interval
of length 4/L. This error grows and does not isolate the required
integer. The paper's gap/multiplicity corollaries are not used to infer
the actual count of the frozen family.

## Chandee–Soundararajan: critical-line upper bound

Vorrapan Chandee, K. Soundararajan, *Bounding |ζ(1/2+it)| on the Riemann
hypothesis*, Bull. Lond. Math. Soc. 43(2) (2011), 243–250.
[DOI](https://doi.org/10.1112/blms/bdq095),
[arXiv:0908.2008v1](https://arxiv.org/pdf/0908.2008v1), submitted
14 August 2009; this is the examined version.

Checked: Theorem1.1 on p.1. Under RH it gives a uniform critical-line
upper bound of size exp(O(log(t)/loglog(t))), hence t^{o(1)}.
HCB uses only this upper bound at the two prescribed Hardy-Z endpoints
to test the specified binomial fallback's resource demand. It gives
no lower bound, nonvanishing or exact count. No claimed improvement
over the literature is involved.

## Online normalization reference

NIST DLMF [§25.10, equations25.10.1–2](https://dlmf.nist.gov/25.10)
was checked for the real Hardy Z function and continuously unwrapped
Riemann–Siegel theta convention. The canonical H=ξ/8 normalization
comes from the repository Book. This online reference has no artificial
PDF copy.

## Reading-copy provenance

The four version-pinned public PDFs were retained outside the repository
under `/Users/Shared/szp-archive/heat-flow-collision-bounds/references/`.
Their exact source URLs, paths, sizes and SHA-256 values are in the
[download manifest](REFERENCE_DOWNLOAD_MANIFEST_20261026.json).
These are reading copies, not numerical inputs or proof certificates.
Hashes identify bytes; they do not validate the mathematics. Public
links above remain the portable source locations.

Reusable citations are in [bibliography.bib](bibliography.bib).

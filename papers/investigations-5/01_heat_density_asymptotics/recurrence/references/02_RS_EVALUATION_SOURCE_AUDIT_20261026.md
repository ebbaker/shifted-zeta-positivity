# RS evaluation sources and precise reading scope

26 October 2026. Prepared for Edward Baker with substantial LLM assistance,
actual gpt-6.1-sol, ultra; recurrence chat0001, R05-AN02 r1.

- J. Arias de Reyna, *High precision computation of Riemann's zeta
  function by the Riemann-Siegel formula, I*, Mathematics of Computation
  80 (2011), 995--1009, DOI
  [10.1090/S0025-5718-2010-02426-3](https://doi.org/10.1090/S0025-5718-2010-02426-3).
  Metadata checked on the [author's publications page](https://personal.us.es/arias/Publications.html).
  AMS PDF returned HTTP403; no direct reading of PartI is claimed. Its
  RS bounds remain imported through Polymath Proposition6.2 as before.
- J. Arias de Reyna, *High Precision Computation of Riemann's Zeta
  Function by the Riemann-Siegel Formula, II*,
  [arXiv:2201.00342v1](https://arxiv.org/abs/2201.00342v1), submitted
  2 January 2022; [pinned PDF](https://arxiv.org/pdf/2201.00342v1).
  Selected exact coefficient identities (29),(62),(86)--(89), and the
  introduction/technical-lemma caveat were read for Note06. Its complete
  implementation/precision conclusions are not imported: some technical
  inequalities in section3.10 are not proved there. Note06 derives its
  own coefficient and quadrature bounds from the named exact identities.
  This is selected reading, not full proof verification.
- [Official FLINT RS documentation](https://flintlib.org/doc/acb_dirichlet.html)
  was discovered as software context. No installed implementation or
  software correctness claim is adopted. Its displayed real cosine
  normalization is not substituted for Polymath's complex C0.

- [NIST DLMF3.5(v), Gauss quadrature](https://dlmf.nist.gov/3.5.v),
  especially the paragraph containing (3.5.20_1): positive weights and
  degree2n-1 polynomial exactness were checked on 26 October 2026.
  Note06 derives its own analytic Chebyshev error from these facts;
  a real mean-value derivative remainder is not used for complex data.
  The existing shared ansatz DLMF bibliography record remains canonical.

The shared ansatz catalog continues to own Polymath and DLMF records.
New bibliography entries are in references.bib; no third-party PDF enters
Git. PartII v1 was retrieved on 26 October 2026 from
https://arxiv.org/pdf/2201.00342v1 as an authorized public PDF, retained at
`/Users/Shared/szp-archive/recurrence/references/2201.00342v1.pdf`:
472174 bytes; SHA-256
`f9dcde16825ca96155816fd940f9b9c5dd537e02313c6b22fd9e962d91bcecaf`.
The [retrieval record](RS_EVALUATION_REFERENCE_RETRIEVAL_20261026.json)
records the same identity and access limitations. File identity is not
proof validation. The arXiv v1 identifier/date pin the source; the HTML
rendering's later displayed date is not treated as a newly examined version.

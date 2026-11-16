# Sources checked for the induction discussion

16 November 2026, America/New_York. Prepared for Edward Baker with
substantial OpenAI Codex LLM assistance; current rollout configuration
gpt-6-astra / max. Passage checks only, not full-paper audits. Used in
[brainstorm Note 03](../brainstorm/notes/03_VCD_INDUCTION_TRUNCATION_AND_ZERO_CONTROL_20261116.md).
New bibliography entries are in [induction.bib](induction.bib).

- **NIST DLMF**, online §§[18.2(vi)](https://dlmf.nist.gov/18.2#vi)
  and [3.5(v)–(vi)](https://dlmf.nist.gov/3.5#v), accessed 16 November
  2026. Checked real/simple/interlacing zeros of positive-weight
  orthogonal polynomials, Gaussian nodes and positive weights,
  equations 3.5.19–20 for the monic-norm remainder, and the Jacobi
  characterization. Source-polynomial roots are not Fourier zeros.
  Linked online reference; no artificial PDF copy.

- **Walter Van Assche**, *Orthogonal polynomials, Toda lattices and
  Painlevé equations*, arXiv:2202.11017v1, 22 February 2022. Rechecked
  [§3, equation (3.1)](https://arxiv.org/html/2202.11017v1#S3), for
  the quartic weight and its neighboring-coefficient relation. The
  existing [canonical catalog](../../../investigations-5/brainstorm/references/EXACT_HEIGHT_REFERENCES_20261113.md)
  owns this article and its bibliography. This finite quartic closure
  is an illustration; no theta closure follows.

- **Peter Topping**, *MA3B8 Complex Analysis*, University of Warwick,
  Autumn 2023 course notes dated 29 July 2024. Checked [§9.9,
  Theorem 9.21, printed p.104; §10.2, Theorem 10.2, printed
  pp.110–111](https://warwick.ac.uk/fac/sci/maths/people/staff/peter_topping/teaching/ma3b8_cplxanal_24_07_29.pdf).
  Rouché requires strict boundary domination and counts multiplicity;
  Hurwitz requires locally uniform holomorphic convergence and excludes
  an identically zero limit. Reality of a unique zero in a symmetric
  disk is an additional elementary conjugation argument. The notes
  remain linked and were not posted or uploaded.

- **Michael Griffin, Ken Ono, Larry Rolen, Don Zagier**, *Jensen
  polynomials for the Riemann zeta function and other sequences*,
  [arXiv:1902.07321v2](https://arxiv.org/abs/1902.07321v2), 31 March
  2019; published PNAS 116 (2019), 11103–11110,
  [doi:10.1073/pnas.1902572116](https://doi.org/10.1073/pnas.1902572116).
  Checked v2 pp.1–2, equations (1)–(2), the unshifted-family sufficiency,
  and Theorem 1. Its eventual hyperbolicity fixes degree and increases
  shift. This does not give the unbounded-degree, zero-shift induction
  discussed here. The note's normalized moment coefficients differ by
  positive scalar and argument rescaling from the paper's convention.

**Reading-copy retrieval:** web inspection of both linked PDFs succeeded.
Separate direct downloads to `/private/tmp/szp-vcd-induction-reading-20261116/`
failed with DNS resolution errors on 16 November 2026. No local PDF,
byte count or hash is claimed. Raw/third-party files were not added to
the repository. Earlier Van Assche download status is unchanged.

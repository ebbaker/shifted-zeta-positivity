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

## Hierarchy closure follow-up, 16 November 2026

Prepared for Edward Baker with OpenAI Codex assistance; current rollout
records gpt-6-astra / max. These are checked primary-source passages for
the analogy and its limits, not imported RH results or full-paper audits.

- **Alexandre J. Chorin, Ole H. Hald, Raz Kupferman**, *Optimal
  prediction and the Mori–Zwanzig representation of irreversible
  processes*, PNAS 97 (2000), 2968–2973,
  [doi:10.1073/pnas.97.7.2968](https://doi.org/10.1073/pnas.97.7.2968).
  Checked [author-hosted published PDF](https://math.huji.ac.il/~razk/Publications/PDF/CHK00.pdf),
  §2, equations (2.4)–(2.7), printed p.2969: projected evolution,
  orthogonal dynamics, the Dyson identity and the exact memory/forcing
  decomposition. Equation (2.7) precedes approximation. The chain's
  deterministic block elimination is derived directly in Note03 §7;
  this citation does not import statistical or operator-domain
  assumptions into that calculation. The `www.ma.huji.ac.il` host timed
  out; the `math.huji.ac.il` copy was inspected successfully.

- **Ali Akbari, Mohammad Javad Hashemi, Risto M. Nieminen, Robert van
  Leeuwen, Angel Rubio**, *Challenges in Truncating the Hierarchy of
  Time-Dependent Reduced Density Matrices Equations: Open Problems*,
  [arXiv:1204.4395v1](https://arxiv.org/abs/1204.4395v1), 19 April 2012;
  related publication Physical Review B 85, 235121 (2012),
  [doi:10.1103/PhysRevB.85.235121](https://doi.org/10.1103/PhysRevB.85.235121).
  Checked v1 [§II.B, equations (7)–(10); §II.C, equations (26), (31);
  §III.C and conclusion](https://arxiv.org/html/1204.4395v1): dependence
  on the next reduced density matrix, cluster reconstruction, and the
  distinction between inter-level compatibility and positivity. Its
  fermionic few-site examples qualify those approximation schemes;
  they do not prove a limitation for theta coefficient closure.

Direct PDF retrieval for both articles to the same temporary external
reading-copy directory failed with DNS errors. Web text/PDF inspection
succeeded as specified above; no local byte size or hash is available,
and no third-party PDF was placed in the repository.

## Quantitative midpoint calibration, 16 November 2026, chat0003

Prepared for Edward Baker with OpenAI Codex assistance; lead actual model/effort unavailable. Reused the canonical NIST DLMF entry above and inspected [§1.10(v), Maximum-Modulus Principle](https://dlmf.nist.gov/1.10#v), including its bounded-domain boundary version and Schwarz lemma (1.10.11), on 16 November 2026. The quotient used in E16 is holomorphic in the disk, with removable zeros and continuous boundary values; the maximum is bounded by the boundary supremum. Its finite disk factors and Fourier bound are derived in-note. This is a classical interpolation estimate, not new theta arithmetic or a zero-free theorem. Online passage only; no PDF or download is claimed.

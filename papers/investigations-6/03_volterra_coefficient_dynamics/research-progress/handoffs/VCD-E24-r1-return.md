# VCD-E24 r1 — Same-input comparison and directed-error return

16 November 2026, America/New_York. Prepared for Edward Baker with
OpenAI Codex assistance. Recorded explicit dispatch **gpt-6.1-sol / ultra**.
Separate backend and lead-configuration attestation unavailable.

**Complete, proved in-note with the completed dependencies below.**
[Note 22][note] executes [the frozen request][request] and
[decision13][decision]. All four frozen input hashes matched.
The request SHA-256 is
`f9bf7b1268a0e369d069355f3bd2dad567d89bd974247ad59567b821e4a5ca24`
and Note 22 SHA-256 is
`48794975bd02d3208287e51b2ff3630cad9cc412381d92cd82dda5f3bacd59f0`.
The bounded proof and correction pass confirms the proposed constants
and scopes. It also gives an exact convex hull and membership test for
the directed enclosure. No numerical campaign was performed.

- \(C_N=G_N+L_N\) and \(G_{N+1}\) both require exactly
  \(\beta_1,\ldots,\beta_N\). The next omitted-walk ratio is
  \(L_{N+1}/L_N=-\beta_{N+1}z^2/[(2N+1)(2N+2)]\).
  The unacquired link \(\beta_{N+1}\) is bounded by \(B_N-\beta_N\).
  On the common bounded-phase range, the stated degree-only
  next-head allowance relative to \(|L_N|\) has order
  \(|z|^2\log^2(N+1)/N^2\). The monomial-correction allowance has
  order \(|z|^2\log^2(N+1)/N\).
- For each fixed \(N\), the ratio of the actual error of \(C_N\)
  to that of \(G_{N+1}\) tends at zero to
  \((\beta_N+\beta_{N+1}+2\sum_{j=1}^{N-1}\beta_j)/\beta_{N+1}>1\).
  The strict ordering of moduli holds on a sufficiently small
  punctured complex disk. The bounded-phase allowance comparison
  yields no all-strip actual ordering.
- At the smaller prefix through \(\beta_{N-1}\), the normalized
  error \( (F-G_N)/((-1)^Nz^{2N})\) has positive unknown amplitude
  at most \(A_N=(\prod_{j<N}\beta_j)(B_{N-1}-\beta_{N-1})/(2N)!\),
  where the product starts at \(j=1\). It lies in the union of
  \(D(a,a\epsilon_N)\) for \(0<a\le A_N\). Its closure is the
  convex hull of 0 and \(D(A_N,A_N\epsilon_N)\), inside the capsule
  of radius \(A_N\epsilon_N\) around \([0,A_N]\). A clamped
  quadratic tests membership in the closed set. For \(\epsilon_N<1\),
  the union has angle at most \(\arcsin\epsilon_N\) from the positive
  ray. If \(\Re(G_N/((-1)^Nz^{2N}))\ge0\), strict positivity
  excludes an actual zero even at a point where \(G_N=0\).
  The case \(z=0\) is handled by \(F(0)=1\).
- Acquiring the exact amplitude yields the corresponding single
  shifted disk, at the input cost of \(G_{N+1}\). The straight-line
  homotopy between \(G_N\) and \(F\) stays boundary-nonzero if the
  contour strictly avoids the **closed** directed set after
  normalization. The closure includes amplitude zero, as the
  initial model requires. Their counts then agree with multiplicity.
  The strict capsule test is one sufficient way to certify the
  separation. A pointwise half-plane test can pass at a model zero
  and so does not replace the contour test there.

The weighted-square and specified E07 finite-mode controls share
the phase and envelope premises. They fail full canonical reflection
and complete square coefficients, which the enclosure leaves unused.
The tested Euler translate fails \(B_0\), and the reflected
super-Gaussian fails the score confinement premise. Other families
retain the scopes in Note 22 §5. The canonical placement of the
finite-head values on expanding contours and a usable zero-count
input remain unpaid. This is an error enclosure and conditional
count transfer.

## Completed E21 and E22 dependency addendum

The initial E24 proof used the law and allowance in [decision12][phase]
as conditional inputs during parallel work. The following completed
files were inspected and their SHA-256 hashes verified.

- [E21 Note 20][e21note]
  `483ad9c88c8a07d833903e941dda5e9bc9520e94e8b64e99713c0c9b119002a9`
  and [E21 return][e21return]
  `c018e9ca4e92531fa9148dad4fd28c111872356cebd26c3a5c93e78b924e81c5`.
  Note 20 (4) identifies the complete physical \(F-G_N=L_NE_N\)
  for all \(N\ge1\) and complex \(z\). Its second moment proves
  Note 22 (1). The physical E15 transport with zero modeled memory
  has the same entire left side, and hence equals this error.
- [E22 Note 21][e22note]
  `411d1c484db9ee78ea8db00c210370a04403b9d74e118e67a77318806fcc94da`
  and [E22 return][e22return]
  `d13d346b7cc924e1eb44b40289ad17beded0da65332cbb459ca2cc8e72cca18a`.
  Use the explicit (8) budget
  \(\epsilon_N(r,Y)=r^2\sqrt{2\mathcal A_N(Y)\mathcal Q_N}/2\)
  with (6)–(7), uniform for \(0\le Y\le1\) and
  \(|\Im z|\le Y,\ r=|z|\). The dependence on \(N,Y,r\) uses
  no missing link. E22 distinguishes the shifted disk from an
  independently sharpened bare disk. E24's containment concerns
  the exact-amplitude disk and its directed union and capsule.

The finalized inputs match the law and budget used in Note 22.
The count still requires strict boundary separation. The
frozen E24 request remains unchanged.

[request]: VCD-E24-r1.md
[note]: ../../notes/22_VCD_E24_DIRECTED_ERROR_AND_PREFIX_COMPARISON_20261116.md
[decision]: ../../brainstorm/notes/13_VCD_B06_PREFIX_COST_AND_DIRECTED_ERROR_DECISION_20261116.md
[phase]: ../../brainstorm/notes/12_VCD_B06_ERROR_PHASE_CONSUMER_DECISION_20261116.md
[e21note]: ../../notes/20_VCD_E21_COMPLETE_ERROR_PROBABILITY_LAW_20261116.md
[e21return]: VCD-E21-r1-return.md
[e22note]: ../../notes/21_VCD_E22_QUANTITATIVE_ERROR_PHASE_20261116.md
[e22return]: VCD-E22-r1-return.md

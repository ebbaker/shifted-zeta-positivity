# VCD-E06 r2 — Fixed-polynomial loss and exponential score return

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance. Recorded tool dispatch **gpt-6.1-sol /
ultra**. Separate runtime configuration or backend attestation unavailable.
Type E, fixed analytical derivation.

All four pins in [r2](VCD-E06-r2.md) matched before the derivation. The
final [E05 input](../../notes/05_VCD_E05_SOURCE_SCORE_RESIDUAL_20261116.md)
has SHA-256
`428b059ee5a6d522afcd4ae3596b2358540ccef16259e0a817604e3f86eca6a1`.
The [E04 fixed-vector audit](../../notes/04_VCD_E04_TAIL_FOUNDATIONS_20261116.md)
used for the optional boundary identity has SHA-256
`116f29472c162272fa554a564f1c88ea02573ee27bd43ee36c2e8e9eefc63880`.

**Complete, proved in-note.** The
[derivation](../../notes/06_VCD_E06_EXPONENTIAL_SCORE_RESIDUAL_20261116.md)
keeps the complete source and literal Fourier observation. It proves
the following uniformly for \(0\le\lambda\le1/2\).

- For each fixed odd polynomial \(p\) of degree \(d\), the weighted
  polynomial score contribution at \(n,n-1\) is at most
  \(A_{n,d}\sum_k|p_k|(2A_{n,d})^k\) in modulus, with
  \(A_{n,d}=\tfrac14\operatorname{arcosh}(2(n+d)+10)\). Its signed
  remainder is \(n+O_p(\log^{d+1}(n+2))\), so a negligible relative
  score residual is excluded for fixed \(p\).
- The exact odd, time-independent remainder in
  \(V_\lambda'=8\pi\sinh(4u)-2\lambda u+b\) is bounded by the explicit
  convergent series (5) of the note. The adjacent exponential reference
  has absolute error at most
  \(\tfrac14 C_b\operatorname{arcosh}(2n+10)\) and relative error
  \(O(\log(n+2)/n)\).
- The one-cut correction for \(8\pi\sinh(4J)\) is the difference of
  the two exact boundary integrals in (7) at \(t=\pm4\), times
  \(4\pi\). It depends on the full tail response. The separate
  bounded-symbol boundary correction has norm at most \(2C_b\).
  The path and parity signs concern the score correction only.

The validated three- and four-square collision controls share a
relative \(O(\log(n+2)/n)\) canonical adjacent score defect, with
control-dependent constants. The exact finite constraints are a
separate test in E07. An update and a zero-sensitive transfer remain
unproved. All arguments use the pinned or already checked input
passages and direct calculations. Evidence is internal analytical work.

# VCD-E12 r1 — Finite midpoint calibration return

16 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Recorded task dispatch **gpt-6.1-sol / ultra**.
Separate runtime model and effort attestation unavailable.

**Complete, proved in-note.** All five input hashes in [r1][request]
matched. [Note 12][note] contains the analytical proof following one
correction pass. Its SHA-256 is
`85e42edecc02059b2549781472eecbdbf558fffcf65e8f7fee42d1651d010de3`.

For each fixed \(L\ge N\ge1\), \(r\ge0\), and \(z_*=x+iy\) with
\(x\ne0\) and \(0<|y|<4\), the two fixed real even smooth compact
multiplier directions preserve the moments through \(2L\), the
polynomials and links through \(q_L,a_L\), the exact canonical \(V'\)
and \(b\) matrix elements with both indices at most \(L\), and all
retained full-chain midpoint derivatives through order \(r\) at
\(z_*\). The calibration is at \(\lambda=0\).
Evenized bump testing rules out a real target dependence. The
\(e^{4u}\) score first separates the nonzero score-polynomial
term, and the \(e^{|y|u}\) oscillatory peaks then separate the
target from all evenized half-frequency jet terms and bounded-score
polynomial terms. The resulting duality permits redundant
constraints. Normalizing the two directions to responses \(1,i\)
gives the exact common Fourier and remainder displacement
\(\eta_1+i\eta_2\).

The disconnected tail jets at zero match through
\(2(L-N)+1\), by return walks and odd-order parity. The next
even order involves \(a_{L+1}\), beyond the matched prefix.
Smallness in the three finite test-function norms of Note 12
gives a positive displacement radius for each fixed choice of
data and prescribed score tolerance. The source stays positive
and equals theta near zero and on both real tails. The score
tolerance and the common logarithmic envelope hold uniformly
for \(0\le\lambda\le1/2\).

Nonzero multipliers fail exact pointwise score equality and the
constant square-mode representation in E10's absolute-convergence
class. Nonzero displacements are attained in every direction
about the canonical remainder. The proof supplies no sign or
zero claim for that remainder and no nonreal-zero conclusion
for these smooth sources. E07's nonreal zeros and E10's next
score defect retain their separate scopes. The finite diagnostic
leaves full functional knowledge, growing-degree rates and
quantitative canonical constraints outside its conclusion.

[request]: VCD-E12-r1.md
[note]: ../../notes/12_VCD_E12_FINITE_MIDPOINT_FREEDOM_20261116.md

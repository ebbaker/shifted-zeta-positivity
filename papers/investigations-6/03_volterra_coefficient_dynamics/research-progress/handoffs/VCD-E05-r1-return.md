# VCD-E05 r1 — Source score and residual return

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance. Recorded tool dispatch **gpt-6.1-sol /
ultra**. Separate runtime configuration or backend attestation unavailable.
Type E, fixed analytical derivation.

**Complete, proved in-note.** The
[derivation](../../notes/05_VCD_E05_SOURCE_SCORE_RESIDUAL_20261116.md)
executes [r1](VCD-E05-r1.md) on \(0\le\lambda\le1/2\). All eight
SHA-256s in the [frozen input manifest](../../numerics/04_VCD_INDUCTION_SESSION_INPUTS_20261116.json)
matched when checked. The manuscript bounds and checked Van Assche
§3, equation (3.1), suffice for the inherited inputs. The other path,
domain and residual steps are derived directly. Evidence is internal
analytical work.

- The first theta summand gives the denominator lower bound needed to
  prove \(V_\lambda'q_j\in L^2(\mu_\lambda)\). Integration by parts gives
  \(a_n[V_\lambda'(J)]_{n,n-1}=n\) and the full matrix entries
  \([V_\lambda'(J)]_{ij}=\langle q_i',q_j\rangle+\langle q_i,q_j'\rangle\).
  The retained compression and \(C_N^V\) are determined by the exact
  prefix and the finite-node score values.
- An odd polynomial of degree at most \(2d+1\) uses links through
  \(a_{n+d}\) in the adjacent equation. Its finite correction uses only
  walks visiting site \(N\), hence at most \(d\) links beyond the prefix.
  The linear correction vanishes. The quartic score gives the cubic
  contribution \(4a_{N-1}\beta_N\) at the last retained off-diagonal
  for \(N\ge2\), with the expected adjacent three-term relation.
- The remaining matrix is the signed full-minus-finite quadrature
  discrepancy of \(r q_iq_j\). Its retained signed entries can be
  recovered by subtracting the polynomial excursion term once its links
  are supplied. Independent weighted-square bounds or signed residual
  constraints at the accuracy required by a tail update are still
  open. Confinement bounds one weighted moment directly and, with the
  score growth bound, gives a coarse absolute allowance. Two separate
  Cauchy bounds discard the full/discrete cancellation.

The control screen in the derivation distinguishes the regular
own-score identity from the canonical theta score. The three- and
four-square sources share the own-score identity and inherited envelope
at their validated collisions. Further quantitative residual design
and its use in a tail update remain with VCD-B02/B03.

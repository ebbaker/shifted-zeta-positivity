# Signed finite-tail source use

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Lead model/effort unavailable in
recorded configurations; analytical helpers explicitly selected
gpt-6.1-sol / ultra. **Selected-passage checks, not full-paper or
independent specialist review.**

## Exponent pairs for the actual logarithmic phase

Reuse the canonical [Montgomery–Vaughan record][record] and
[bibliography][bib]: Hugh L. Montgomery and Robert C. Vaughan,
*Exponential Sums I: Van der Corput's Method*, Chapter 16 of
*Multiplicative Number Theory II: Primes and Sieves*, Cambridge, 2026,
pp. 1–53. The [publisher record][publisher] in the canonical entry
provides publication metadata. The source inspected here is the
[author-hosted text][mv], not an asserted new edition.

Two analytical helpers checked Definitions 16.1–16.2, equations
(16.55)–(16.58), Theorem 16.23 (A process) and Theorem 16.25
(B process): printed pp. 32–33, 37, 41; PDF pp. 44–45, 49, 53.
The review helper also checked Table 16.1. The definition permits
arbitrary subintervals of [M,2M] and real M>0. For the phase
tau*log(u)/(2pi), use derivative parameter theta=1 and scale
tau/(2pi)>0; the relative derivative error is zero. Conjugation
handles the opposite sign. The retained sum bound is

    O(tau^k M^(l-k) + M/tau).

This differs from the sibling log-ratio application (theta=2);
no sibling mean-value or changed-window theorem is imported.
The exact complex-L shifts are retained in the two real frequencies.
Abel variation, real clipped dyadic endpoints, the integer cutoff
and the secondary term are paid in Notes07,09–10.

The A-chain pairs are derived from AB(0,1)=(1/6,2/3).
All constants are finite for each selected fixed pair; the canonical
theorems use only finitely many pairs. The envelope comparison over
all j does not assert one uniform constant for infinitely many pairs.

The web reader supplied the primary PDF text. No new local PDF copy
was downloaded; the earlier canonical record retains its unsuccessful
local-download provenance. No third-party PDF is stored in the repository.

## Other inputs and evidence boundaries

- [HDA Ansatz Note04][hda], CS2–6 and its fixed enlarged-chart/Gaussian
  ledger, remain the complete-field input, with their original
  same-model internal assessment. Note06 checks the consumer and
  verifies its frozen inputs; neither E02 nor E04 re-proves or
  independently audits the entire HDA theorem.
- [Polymath v2][poly], Theorem 3.2, was checked again for the initial
  global enclosure from time zero. Its explicit Theorem 1.3 range
  stops at y=1; the separate HDA input supplies the 9/8 boundary.
  Proposition 9.1's large constant in x>=exp(C/t) was not treated
  as a theorem on the clock t=1/log(x/(4pi)).
  B03 additionally checked Theorem 1.5(i): for 0<t<=1/2, a sufficiently
  large absolute C_P gives real zeros whenever x>=exp(C_P/t).
  E05 uses that theorem only in its actual far-tail domain, after a
  separately proved finite-window bridge. It does not set C_P=1 or8.
- [DLMF 25.2.1][series] and [25.2.11][euler] supply ordinary series
  and Euler nonvanishing in Re s>1, not a heat-weighted Euler product.
  [Cauchy's formula][cauchy] applies to exact analytic quotients.
  No infinite heat-weighted Dirichlet series is used.

Canonical ownership stays with these source records and their
bibliographies. The branch application, source regimes and actual
proof acceptance are recorded separately in its notes and Review03.

[record]: ../../01_riemann_siegel_evolution/references/03_GNP_RS_B10_EXPONENT_PAIR_AUDIT_SOURCE_20261112.md
[bib]: ../../01_riemann_siegel_evolution/references/riemann_siegel_execution_sources.bib
[publisher]: https://www.cambridge.org/core/books/abs/multiplicative-number-theory-ii/exponential-sums-i-van-der-corputs-method/A5CE1F676830DA2003DDFBA8615DE62D
[mv]: https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf
[hda]: ../../../01_heat_density_asymptotics/ansatz/notes/04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md
[poly]: https://arxiv.org/html/1904.12438v2
[series]: https://dlmf.nist.gov/25.2.E1
[euler]: https://dlmf.nist.gov/25.2.E11
[cauchy]: https://dlmf.nist.gov/1.9.E31

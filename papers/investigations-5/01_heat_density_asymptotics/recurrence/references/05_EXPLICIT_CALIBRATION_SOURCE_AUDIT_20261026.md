# Primary-source check: explicit calibration constants

26 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance, **gpt-6.1-sol (Codex), actual effort ultra**, recurrence
chat0003. Selected equations and hypotheses checked online; no full primary
proof reading or independent specialist review. DLMF online edition 1.2.8,
release 2026-09-15, retrieved 2026-10-26. No third-party PDF added.

- [DLMF5.11.1](https://dlmf.nist.gov/5.11.E1),
  [5.11.2](https://dlmf.nist.gov/5.11.E2) and
  [5.11(ii), first error-bound paragraph](https://dlmf.nist.gov/5.11#ii):
  log-gamma and digamma remainders are bounded by the first omitted term
  times the stated sector secant factor. Note11 uses n=1, exponents 2
  and 3 respectively, strictly inside |arg t|<pi. This is distinct from
  the gamma-function remainder 5.11.11. The existing canonical ansatz
  gamma record and recurrence Source Audit04 remain the shared citation;
  Note11 derives its disk, slope and envelope constants explicitly.
- [DLMF5.12.1](https://dlmf.nist.gov/5.12.E1): beta integral and gamma
  ratio for Re a,Re b>0. Used at a=1/4+it,b=1/4 with t real; taking the
  integral's absolute value bounds the ratio by its t=0 value.
- [DLMF5.4.4](https://dlmf.nist.gov/5.4.E4): exact modulus squared of
  Gamma(1/2+it), t real. Together with the beta integral this supplies
  the global real-height gamma estimate; it is not inferred from a
  large-height asymptotic at u=0.
- [DLMF25.2.8](https://dlmf.nist.gov/25.2.E8): finite-sum/integral zeta
  representation, N a positive integer and Re s>0, s!=1. Note11 uses
  N=1, Re s=1/2; the fractional-part integral is absolutely bounded
  directly. This establishes a global polynomial source bound.

Complete theta-source normalization, positivity of its summands and the
canonical cosine/xi identity are retained from the sibling ansatz source
notes linked in [Note11](../notes/11_EXPLICIT_CALIBRATION_AND_HEIGHT_ONSET_20261026.md).
Positivity is checked directly in Note11, not imported as a new theorem.
No new reading of the RS PartI proof is claimed; the prior named real
remainder and coefficient hypotheses/access limits remain unchanged.
Nothing in this source check certifies executable software or imports a
preliminary PartII precision conclusion. Constants, simultaneous-order
majorants and onset arithmetic are the new derivations in Note11.

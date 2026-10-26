# Primary-source check: efficient provider bounds

26 October 2026, America/New_York. Prepared for Edward Baker with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual effort ultra**,
recurrence chat0003. Selected formulas/passages checked, not full primary
proofs or independent specialist validation. Online DLMF edition 1.2.8,
release 2026-09-15; retrieved 2026-10-26. No third-party PDF added.

- [DLMF5.11.1](https://dlmf.nist.gov/5.11.E1) and
  [5.11(ii), first error-bound paragraph](https://dlmf.nist.gov/5.11#ii):
  complex log-gamma remainder after k=m-1 is bounded by the first omitted
  term times sec(arg(W)/2)^(2m). The analytic logarithm is continued from
  the positive real axis. Note10 uses only Re W>=m>0, including its small
  Cauchy disk; it does not substitute the distinct gamma-function
  remainder 5.11.11. The shared ansatz gamma bibliography record remains
  canonical; this is a new passage-specific use and check.
- [DLMF24.8.1](https://dlmf.nist.gov/24.8.E1): Bernoulli Fourier expansion
  for integer m>=1 and 0<=x<=1. At x=0 it gives the explicit absolute
  Bernoulli bound used in Note10. The resulting geometric remainder,
  shifted-gamma jets and bit-work estimates are derived in Note10.
- [DLMF18.9 Table1](https://dlmf.nist.gov/18.9.T1): the Legendre
  three-term recurrence; [DLMF14.10.5](https://dlmf.nist.gov/14.10.E5)
  at mu=0, nu=s: derivative identity on (-1,1). The same identities also
  follow by coefficient comparison in Rodrigues' formula. Note10 proves
  its own sign-variation root count, endpoint convention and bit bounds;
  no external Sturm-complexity or numerical-library theorem is imported.

The [earlier source audit](03_FINITE_PROVIDER_SOURCE_AUDIT_20261026.md)
retains the elementary gamma-product fallback. The shared canonical
heat/RS coefficient sources keep their original access and reading limits.
No new PartI reading or preliminary PartII precision conclusion is claimed.
Use [Note10](../notes/10_EFFICIENT_PROVIDERS_AND_TOTAL_COST_20261026.md)
for the actual theorem, finite majorants, input model and remaining
calibration/onset dependencies. Source checking identifies classical
inputs; it does not certify the new arguments or an implementation.

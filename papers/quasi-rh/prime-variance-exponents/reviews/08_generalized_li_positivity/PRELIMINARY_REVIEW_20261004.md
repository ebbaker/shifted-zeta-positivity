# Internal preliminary review: generalized Li coefficients

4 October 2026. Substantial LLM assistance, GPT-6 (Codex), inherited
configuration; exact serving variant and configured effort are not exposed.
This is an internal self-check, not independent human verification.

Reviewed [the dated investigation](../../notes/programs/08_generalized_li_positivity/PRELIMINARY_INVESTIGATION_20261004.md).

- Freitas's derivative and reciprocal-ratio normalizations were compared with
  Theorem 1 and Lemma 3.1 in the primary PDF. Multiplicity, paired summation and
  the allowed strip boundary are retained.
- Both gamma conventions agree after the log-s term is absorbed. The n=1
  expression is the ordinary logarithmic derivative of xi.
- The exponential elementary term equals the full continuous density integral
  exactly. Centering uses psi(t)-t+1 so its lower endpoint vanishes; using
  psi(t)-t requires the extra -n term explicitly noted in the investigation.
- The prime tail bound states its monotonicity condition log(K)>=n/tau.
  The gamma-series tail is one-sided and the combined interval uses that sign.
- The standard-library script passed 192 exact fraction checks. Finite endpoint
  values are diagnostic floats, not certified enclosures or all-index positivity.

No n-uniform signed bound was found. The high-zero amplification scale is not
represented as a first-negative-index theorem. Large uncentered prime sweeps are
not recommended without an independent arithmetic estimate.

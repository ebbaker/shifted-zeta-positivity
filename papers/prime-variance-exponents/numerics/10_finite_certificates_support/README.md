# Complete block-Gram preflight

4 October 2026. Substantial LLM assistance; GPT-6 (Codex), inherited
configuration, exact serving variant and effort not inferred.
Floating diagnostics only, not outward certificates.

Run from the repository root:

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 \
  papers/prime-variance-exponents/numerics/10_finite_certificates_support/block_gram_preflight.py \
  --output /tmp/block_gram_record_20261004.json
```

The script uses NumPy and imports the established probe/sieve from
[the earlier pilot](../mobius_reduction_20261004/pilot.py). It assembles new
complete block coefficients, checks arithmetic identities, and reports
projected signed covariance summaries. Defaults: two noninteger real
shells, 128/256 nodes, pure-power D=X^(9/10), balanced U=V=X^(11/24).
All effective integer thresholds are retained in the small
[record](block_gram_record_20261004.json). No sieve or Gram matrix is stored.

See [program 01's derivation](../../notes/programs/01_signed_arithmetic_covariance/PRELIMINARY_INVESTIGATION_20261004.md)
and [the support assessment](../../notes/programs/10_finite_certificates_support/PRELIMINARY_INVESTIGATION_20261004.md).
Hashes identify the sources used for this local run; they are not proofs
of a mathematical estimate or of numerical portability.

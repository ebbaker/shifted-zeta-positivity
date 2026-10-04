# Certified finite dyadic variance bounds

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Internal checks, not independent specialist review.

This small rational transfer package proves, for every real X in the
indicated range, that the complete prepared-probe variance satisfies:

| Range | Strict bound |
| --- | --- |
| e <= X <= 10^99 | Vcal_g(X) < 38 X^2 |
| e <= X <= 10^100 | Vcal_g(X) < 40 X^2 |
| e <= X <= 10^102 | Vcal_g(X) < 72 X^2 |

The [derivation](../../notes/subpower-milestones/03_finite_range_variance_20261003.md)
integrates a complete linear-response bound from the earlier
[signed-pair package](../selective_loss_quadratic_target_20261003/README.md).
These finite continuum results use the published RH verification through
height 3e12 and its unverified high-zero tail. They assume no global RH.
They give no smaller fixed global delta.

Run with Python's standard library, from this directory:

```bash
python3 certify.py --output record.json
```

The generator checks the SHA-256 hashes of both earlier outward records
and their original generator, verifies their scope, checks their positive
enclosures and overlap, and uses exact fractions for every new threshold.
It fails closed on a missing or changed input. This is a transfer of the
earlier outward certificates, not a regeneration of their rigorous zeros.
No individual zero cache is copied here. The external mathematical inputs
are stated in the derivation and record. The [preflight](PREFLIGHT.md)
states the bounded computation, and the
[review](../../reviews/SUBPOWER_FIRST_INVESTIGATION_REVIEW_20261003.md)
records internal checks.

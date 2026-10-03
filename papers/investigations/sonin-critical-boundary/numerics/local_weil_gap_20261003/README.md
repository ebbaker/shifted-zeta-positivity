# Certified local Weil gap and relative Sonin comparison

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured effort are not exposed and are not inferred.

This package certifies Q[F] at least (9/100)||F|| squared for all smooth sources supported in (-1/2,1/2) with zero mean and zero exponential moments at plus and minus one half. The moment conditions are exactly the prepared mean-zero source class. Both parity sectors and complex sources are covered. Only prime 2 and its first power contribute at this support.

The [analytic proof](../../notes/LOCAL_COERCIVITY_LOW_BAND_20261003.md) reduces the comparison to a positive low-band source operator. The calculation uses the exact full moment projection, 40 Legendre coordinates, and 46,000 midpoint cells on [0,46]. Outward Arb arithmetic proves that the finite matrix is below 9/10 times the identity by positive LDL pivots. An analytic total-variation bound encloses the integration error, and a spherical-Bessel majorant encloses every omitted source mode. Their total is below 0.008253; the generator requires it to be below 0.01. No floating eigenvalue or source sample is used to certify the all-source inequality.

The separate source factorization gives |K[F]| at most 772||F|| squared, using the inherited certified archimedean boundary gap. Together these establish

\[
Q[F]\ge\frac9{77209}B[F]\ge\frac1{9000}B[F].
\]

Thus B_new=B/9000 is a positive revised main term with a nonnegative remainder. This is a local relative comparison obtained from an independent arithmetic estimate. It does not prove B at least the unweighted positive spectral part of K, positivity without the zero-mean condition, or an all-support statement.

## Reproduction

The recorded runtime is Python 3.10.0, python-flint 0.9.0, FLINT 3.6.0. The generator depends only on python-flint and the Python standard library. From this directory in an environment containing python-flint, run:

```sh
python3 -B certify_local_weil_gap.py --bits 192 --output /tmp/local-weil-gap-192.json
python3 -B certify_local_weil_gap.py --bits 256 --output /tmp/local-weil-gap-256.json
```

The defaults are `--nodes 46000 --rank 40`. Other parameters must pass the same outward checks; a failed check raises an exception. Nonpositive node counts and odd ranks are rejected. The output binds itself to the exact generator hash. Matrix hashes identify a particular enclosure and may change with precision or arithmetic implementation; proof acceptance depends on the strict inequalities, not matching hashes.

The 192-bit and 256-bit records retain rational endpoint bounds, positive LDL pivot lower bounds, and a hash of the regenerated matrix enclosures. Matrices are not stored. The minimum-pivot fields contain lower bounds, so the two precisions need not give overlapping point records for those fields. The replay check compares the scalar enclosures and verifies the strict caps separately.

## Inherited boundary gap

The Q gap is independent of the prolate input. The correction norm bound and the retained-B conclusion also use the existing archimedean gap 57/1000000. Its generator is `papers/susy-positivity/investigations/wilson-loewner/arithmetic-storage/numerics/prolate_certificate.py` from the repository root. The fresh `inherited_gap_replay.json` records its hash, exact gap, rank32, precision256, and inverse-model hash. The finite-place transport gives g=(17-12 sqrt(2))*57/1000000, and the generator directly checks sqrt((1-g)/g)<772.

To replay the inherited certificate from the repository root:

```sh
python3 -B papers/susy-positivity/investigations/wilson-loewner/arithmetic-storage/numerics/prolate_certificate.py --rank 32 --precision-bits 256 --output /tmp/prolate-gap-replay.json
```

The [internal review](../../reviews/REVISED_B_CERTIFICATE_REVIEW_20261003.md) checks the proof and implementation. It is a same-model audit, not independent specialist refereeing. The separate [source-space pilot](../revised_B_source_pilot_20261003/README.md) remains exploratory and is not an input to this certificate.

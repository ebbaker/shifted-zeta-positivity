# Round 1 continuation: source screens and an interacting seed

17 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**.
Same-model preparation checks only; formal round review remains pending.

These bounded runs support [Note 02](../../notes/round-1/02_INTERACTING_FERROMAGNETS_AND_OTHER_STABLE_SEEDS_CODEX_20261017.md).
They test necessary source constraints and verify that one explicit
interacting seed escapes a specified constraint. They do not fit theta
parameters or prove a theta approximation theorem.

## Source-value screens

Run with Python and `python-flint` installed:

```sh
python3 certify_source_alternative_obstructions.py
```

The script writes [SOURCE_ALTERNATIVE_OBSTRUCTIONS.json](SOURCE_ALTERNATIVE_OBSTRUCTIONS.json).
It uses **160 bits**, exactly **nine source evaluations**, theta terms
\(1\le n\le8\), a **30-second** limit, and no precision escalation or
subdivision. After floating scouts and before the retained interval run,
the requested width of each finite difference was set to **less than
\(10^{-7}\)**. The baseline is the defining complete theta series.
Stop on a failed enclosure or nonnegative/indeterminate requested sign.

For \(u\ge0\), all theta summands are positive. A complete omitted-tail
bound is
\[
0<T_N(u)\le
\frac{2\pi^2e^{9u}(N+1)^4e^{-\pi(N+1)^2}}
{1-16e^{-\pi(2N+3)}}.
\]
This follows by discarding the negative summand and bounding successive
majorant-term ratios geometrically. The source is positive at every
tested node, so taking its logarithm is rigorous. Input nodes are exact
rationals in \(x=u^2\), enclosed by Arb.

The four-point test gives
\(\Delta_{.01}^3[-\log\Phi(\sqrt x)]_{x=0}\in
(-0.000434999,-0.000434997)\).
The five-point test gives
\(\Delta_{.001}^4[\Phi(\sqrt x)e^{2\pi\cosh(4\sqrt x)}]_{x=0}\in
(-5.232\cdot10^{-7},-5.230\cdot10^{-7})\).
The note supplies the mathematical implications and the additional
compactness proofs needed for its transform-limit exclusions.

## Explicit two-quartic interacting seed

```sh
python3 certify_two_quartic_seed.py --output TWO_QUARTIC_SEED_CERTIFICATE.json
```

The [record](TWO_QUARTIC_SEED_CERTIFICATE.json) supports the law
\(p(x,y)\propto e^{-x^4-y^4+(7/2)(x^2+y^2)+xy}\), with \(S=x+y\).
Exactly **four Acb integrations** enclose
\(\int_0^4u^{2k}e^{-2(u^2-3/2)^2}\,du\), \(k=0,1,2,3\), at
**160 bits**. The predeclared relative and absolute goals are
\(2^{-130}\), with at most **100,000 evaluations** and depth **100** per
integral, no precision/domain refinement, and a required final cumulant
radius below \(2^{-100}\). These are finite algorithmic resource caps;
this run has no separate wall-clock promise. Initial scouts are not the
retained certificate.

For \(u\ge4\), \(0\le k\le3\), the positive integrand is bounded by
\(e^{-u^4/2}\le e^{-32u}\), so each omitted integral is at most
\(e^{-128}/32\). The functions integrated by Acb are entire. The resulting
\(\kappa_3(U^2)<0\) proves that the sixth coefficient of the marginal's
negative log density is negative. It does not establish theta agreement.

Both scripts record source hashes and library versions. The environment
used Python 3.10.0, python-flint 0.9.0 and FLINT 3.6.0. Official arithmetic
contracts: [Arb](https://python-flint.readthedocs.io/en/latest/arb.html) and
[Acb analytic integration](https://python-flint.readthedocs.io/en/latest/acb.html#flint.acb.integral).
All outputs are small certificate records; no large archive is needed
under [LARGE_FILES.md](../../../../../LARGE_FILES.md).

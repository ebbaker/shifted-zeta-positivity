# S04-T2 signed Gaussian core and complete averaged value: internal review

19 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual model **gpt-6.1-sol (Codex)**, reasoning
effort **ultra**. Separate same-model analytic subagent review and fresh
replay; **not independent specialist review**.

**Verdict: pass for the stated averaged functional.** The written proof
supports the moving intermediate-block radius **1.5e-6**, the complete
physical averaged-value radius **0.11** about its prescribed leading
coefficient, and the weighted \((Q/2)^2\) energy floor **0.198**. These are
averaged estimates. They do not prove pointwise noncollision or the
height-uniform residual transfer needed by S04-T3.

## Scope and prior work

Reviewed the complete [Note02][note] and [checker][script], the preceding
S04 Note01, the local fixed-cutoff source contract, and the earlier
collision manuscript's terminal-edge, exponent-pair and hard-window
mean-square calculations. Checked the published real-axis input directly
in [Polymath Theorem1.3, equations(23)-(24)][primary]. The note identifies
these prior results and does not recast them as new progress.

The selected phase and Gaussian probe are prescribed from the arithmetic
normalizer and the declared center parameters. They do not depend on a
post hoc sign choice from Q. The same-functional comparator is the stated
full-mass triangle payment; no claim is made against every signed method.
The changed value-energy norm is explicitly distinguished from the prior
hard-window derivative average.

## Analytic checks

- **Normalization and phases:** F has two conjugate channels. Multiplying
  by exp(-i theta) gives forward coefficient one at n=1. The forward
  Gaussian multiplier is exp(-4 log(n)^2); the reflected multiplier is
  exp(-16(2Omega-log(n)/2)^2). The heat-dependent phase shift is retained.
  The checker implements these signs and factors consistently.
- **Intermediate and complete leakage:** independently derived the
  n^(-5/8) coefficient envelope, including the natural-floor reserve.
  The erfc tail in equation(9) follows by completing the square in
  exp(3v/8-4v^2); its coefficient and erfc argument are correct. The sum
  starts at17, with its first summand included. The reflected gap survives
  the slight cutoff excess, so its exponentially small payment covers
  all modes through the growing cutoff.
- **Whole-window movement and tails:** theta is linearized only in the
  reflected channel. The proof pays its second derivative and both
  amplitude movements before using complete Gaussian moments. Only the
  frozen explicit finite polynomial is extended past the physical window;
  no unpaid Gaussian tail of the physical source is introduced. The
  positive, reflected, movement and tail costs recombine with one common
  payment rather than being charged separately in each range.
- **Complete source:** at every real abscissa the two normalized gamma
  channels have modulus one. The source AB factor2 and the C coefficient
  2.48/(m-.125) agree with the published real-axis theorem. Common
  horizontal endpoint majorants are used directly; a radius-Y
  holomorphic disk is not assumed. The continuous cutoff width is
  below .00013, so one explicitly paid added/removed mode suffices.
  The exact jump algebra and its coefficient envelope check out.
- **Neighboring parameters:** the note does not silently reuse the old
  kappa-domain theorem at translated endpoints. The raw real-axis source
  majorants cover the whole physical window, and the finite-model transfer
  repeats the per-mode alpha identities. The bound
  sum W_n(x+y)<=exp(.250001Y/xminus) sum W_n(x) closes that transfer.
- **Uniformity:** the needed scalar envelopes decrease for L>=20 by the
  logarithmic derivatives given in the note. The checks at L=20 verify
  constants after those analytic reductions; the three point transforms
  are diagnostics, not a parameter cover. The C correction's coarse
  prose bound was corrected from1.2e-8 to1.3e-8 during review; the script
  always evaluated the outward expression itself.
- **Energy consequence:** Cauchy uses the truncated Gaussian mass below
  one and real Q. The Q/2 coordinate receives the required factor1/4:
  .89^2/4=.198025>.198. The stated conversion to an unweighted mean on
  the support length16 sqrt(L) is also correct.

## Fresh replay and guards

The separate [192-bit replay][replay] passed with

- moving intermediate radius below **1.381281112e-6**;
- complete physical radius below **0.105110346498**;
- actual frozen transform cutoffs **22026,36315,36315** at the three
  prescribed parameter pairs.

The reviewed checker SHA256 is
`9be7b362db541d251763fe92ce1aa10e2e879612cdcc9b6de1bf1985213c075f`.
The replay pins the same script and three analytic source identities.

Fresh [input-guard tests][guards] confirmed that missing source, stale
source,64-bit precision and blank runtime metadata each cause failure
before any output record is created. These are integrity checks, not
scientific evidence. No large height scan or physical-source quadrature
was performed.

## Status and limitations

S04-T2's selected averaged-functional gate is met. The unchanged
collision-control consumer remains a separate interface with source-specific
errors. An averaged energy floor may hold at an isolated collision; it
cannot be advertised as rejecting those controls or as an average-to-point
acceptance theorem. The note correctly retains the full theta-source
premise and leaves S04-T1's conditional and S04-T3's waiting status intact.

[note]: ../notes/02_GAUSSIAN_SIGNED_CORE_AND_COMPLETE_AVERAGED_VALUE_20261019.md
[script]: ../numerics/check_gaussian_signed_core.py
[replay]: ../numerics/S04_GAUSSIAN_REVIEW_REPLAY_192_20261019.json
[guards]: ../numerics/S04_GAUSSIAN_REVIEW_INPUT_GUARDS_20261019.json
[primary]: https://arxiv.org/html/1904.12438v2#S1.Thm3

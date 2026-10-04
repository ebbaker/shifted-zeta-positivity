# Finite variance certificate replay and constants audit

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
This is a fresh internal same-model replay and algebra check, not independent
specialist refereeing.

## Result and scope

**PASS.** The existing finite variance generator was replayed into
`/tmp/prime_variance_certificate_replay_20261003.json`; its output is
byte-for-byte identical to the retained
[record](../../investigations/sonin-critical-boundary/numerics/subpower_finite_variance_20261003/record.json).
The existing standard-library outward-record audit also passed. An additional
independent reconstruction using Python `Fraction` arithmetic checked the
probe polynomial, exact norms, vanishing endpoint derivatives and boundary
atoms.

No low-zero enclosure, 192/256-bit outward calculation, or published
finite-height zero verification was regenerated in this session. Those remain
imported inputs. The finite transfer does not establish a smaller fixed
global variance exponent or assume global RH.

Commands, run from the repository root:

```bash
python3 papers/investigations/sonin-critical-boundary/numerics/subpower_finite_variance_20261003/certify.py --output /tmp/prime_variance_certificate_replay_20261003.json
python3 papers/investigations/sonin-critical-boundary/numerics/selective_loss_quadratic_target_20261003/replay.py
```

They returned `PASS_RATIONAL_FINITE_DYADIC_VARIANCE_TRANSFER` and
`PASS_RATIONAL_RECORD_AND_KERNEL_AUDIT`, respectively. The generators and
all original records were left unchanged. The temporary output is disposable;
the linked retained record contains the same bytes.

## Exact polynomial constants

The independent reconstruction used
\(h(v)=(1-16v^2)^8\), \(g_0=-h'''+h'/4\) on \((-1/4,1/4)\).
Its nonzero coefficients, indexed by powers of \(v\), are

| Power | Coefficient of \(g_0\) |
| --- | ---: |
| 1 | -172096 |
| 3 | 27532288 |
| 5 | -1541750784 |
| 7 | 42287759360 |
| 9 | -620232704000 |
| 11 | 4691513573376 |
| 13 | -14438606307328 |
| 15 | 17179869184 |

Exact integration gives

\[
\nu=\int_{-1/4}^{1/4}g_0^2
=\frac{146640624550936576}{37921101075},\qquad
\int_{-1/4}^{1/4}(g_0^{(6)})^2
=\frac{2504085215525628254072340480}{19}.
\]

Every endpoint derivative of \(g_0\) of order 0 through 4 vanishes.
The total absolute mass of the endpoint atoms in its sixth distributional
derivative is
\(2\,8!\,8^8=1352914698240\). Cauchy--Schwarz bounds the interior
\(L^1\) mass by the square root of half the displayed sixth-derivative
squared norm. The exact integer inequality

\[
8117695446119^2>
\frac{1252042607762814127036170240}{19}
\]

therefore gives total variation strictly below
\(1352914698240+8117695446119=9470610144359\).
Consequently the usable transform constant is

\[
K=\frac{9470610144359}{\sqrt\nu},\qquad
|G(z)|\le K e^{|\Re z|/4}|z|^{-6}\quad(z\ne0).
\]

The old outward generator uses the minus convention,
\(G_-(s)=s(1/4-s^2)H(s)/\sqrt\nu=G_+(-s)\).
Its absolute masses and tail constants are unchanged in the manuscript's
plus convention. No autocorrelation twelfth-power bound is imported into
the linear response.

## Imported envelope and exact budgets

The
[finite variance derivation](../../investigations/sonin-critical-boundary/notes/subpower-milestones/03_finite_range_variance_20261003.md)
uses low cutoff \(L=500\), the certified complete positive zero count
\(N(500)=269\), both ordinate signs, all multiplicities, and the published
verified height \(H=3\cdot10^{12}\). Its envelope for every \(y\ge1\) is

\[
|p_g(y)|\le b+R_H e^{y/2},
\]
\[
b=S_{500}+12K500^{-5}\left(\frac{\log500}{5}+\frac1{25}\right)
+\frac{\sqrt{1/2}e^{-15/8}}{1-e^{-3/2}},\qquad
R_H=12Ke^{1/8}H^{-5}\left(\frac{\log H}{5}+\frac1{25}\right).
\]

The generator checked positive ordered enclosures, overlapping 192/256-bit
intervals, source identity, zero-count and height scope, and the strict
rational roundings
\(b<124/25=4.96\) and \(R_H<(39/25)10^{-51}\).
For orientation only, their decimal values are approximately
\(4.9554469277064355\) and \(1.5592867434910273\cdot10^{-51}\);
the proof uses rational enclosure endpoints.

Direct integration of \((b\sqrt x+R_Hx)^2\) over the whole shell
\([X,2X]\) gives exactly

\[
\mathcal V_g(X)\le\frac32b^2X^2
+\frac45(2^{5/2}-1)bR_HX^{5/2}
+\frac73R_H^2X^3.
\]

The normalized right side is increasing in \(X\). Since
\((283/50)^2>32\), its cross coefficient is less than \(466/125\).
For the odd endpoint exponent, \(\sqrt{10}<16/5\) gives
\(\sqrt{10^{99}}<(16/5)10^{49}\).

| Entire real range | Rational upper budget for \(\mathcal V_g(X)/X^2\) | Strict ceiling | Exact margin |
| --- | --- | ---: | --- |
| \(e\le X\le10^{99}\) | \(2955558057/78125000=37.8311431296\) | 38 | \(13191943/78125000\) |
| \(e\le X\le10^{100}\) | \(62255877/1562500=39.84376128\) | 40 | \(244123/1562500\) |
| \(e\le X\le10^{102}\) | \(5580201/78125=71.4265728\) | 72 | \(44799/78125\) |

These bounds retain the complete physical shell and all partial packets.
Their strict margins include the displayed endpoint values.

## Verified-height scaling

Counting both signs and using \(N(t)\le t\log t\) for \(t\ge100\)
gives, by Stieltjes integration by parts and discarding the nonpositive
lower boundary term,

\[
\sum_{|\gamma|>H}m_\rho|\gamma|^{-6}
\le12\int_H^\infty t^{-6}\log t\,dt
=12H^{-5}\left(\frac{\log H}{5}+\frac1{25}\right).
\]

For fixed low cutoff and \(C>3b^2/2\), let \(q_C>0\) solve
\((7/3)q_C^2+(4/5)(2^{5/2}-1)bq_C+3b^2/2=C\).
The certified range is \(X\le(q_C/R_H)^2\), hence scales as
\(H^{10}/(\log H)^2\) along available verified heights. At any one
finite height, its high-zero allowance still has eventual cubic variance
growth. This is a law for enlarging a finite range, not an exponent descent.

## Source identity

All paths below are relative to
`papers/investigations/sonin-critical-boundary/`.

| File | SHA-256 |
| --- | --- |
| `manuscript.tex` | `1529eadf01166945528254f3b5a78f405b06479e04de484ce10f11fd837b408d` |
| `numerics/subpower_finite_variance_20261003/record.json` | `7576708c6cd4e0e9be89d7551d1386ef77b9c972908f55d50f864b9c4afc6b26` |
| `numerics/subpower_finite_variance_20261003/certify.py` | `91e1b31ce6a34d6f6625c1b6ccb2c02e60c4c404599277ba274bfd9e3eafbf1f` |
| `numerics/selective_loss_quadratic_target_20261003/certify.py` | `6f3947f99d4b45307b8a84fb25a6ec56d395d98fb5467106d77dac0a95c63a1b` |
| `numerics/selective_loss_quadratic_target_20261003/bound_192.json` | `21a71598fb9dcf8fe51743e75f65aedd5c5deee69619d2bda806da3e9ac6f2c0` |
| `numerics/selective_loss_quadratic_target_20261003/bound_256.json` | `3c39ccfbc704122de57c04395e120f11a5a563d9d3838c5b6388a9e7c50a60b8` |

The parent-manuscript and finite-record hashes match the
[continuation note](../notes/MANUSCRIPT_CONTINUATION_20261003.md).
The other source hashes match the transfer generator and retained record.
Hash agreement establishes source identity; the exact arithmetic and stated
analytic inputs establish the inequalities.

The existing
[small transfer package](../../investigations/sonin-critical-boundary/numerics/subpower_finite_variance_20261003/README.md)
and
[original outward package](../../investigations/sonin-critical-boundary/numerics/selective_loss_quadratic_target_20261003/README.md)
remain the reproduction entry points. No source package or zero cache was
duplicated under the new paper.

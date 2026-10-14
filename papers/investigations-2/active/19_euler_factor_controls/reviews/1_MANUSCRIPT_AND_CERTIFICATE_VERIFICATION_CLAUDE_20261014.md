# Internal verification of the Euler-factor-controls manuscript

14 October 2026. Prepared for Edward Baker with LLM assistance.
Model: Claude Opus 5.5 (configured identifier `claude-opus-5-5`; the serving
model may differ), Claude Cowork, reasoning effort **max**. The verification
pass was run by a separate Claude instance of the same model, with its own
code, and its findings were then applied and rechecked by the drafting
instance. This is an internal review, not independent specialist
validation.

<<<<<<< HEAD
Subject: the [manuscript source](../manuscript/euler_factor_controls.tex)
(compiled PDFs are not stored), the
=======
Subject: the [manuscript](../manuscript/euler_factor_controls.pdf)
([source](../manuscript/euler_factor_controls.tex)), the
>>>>>>> 94745f3 (Merged work from ChatGPT)
[certificate program](../numerics/check_euler_control_witnesses_claude_20261014.py)
and its [record](../numerics/EULER_CONTROL_WITNESS_CERTIFICATES_20261014.json).

## What was checked

1. **Mathematics.** Sections 2–7 and 9 line by line: the arithmetic of the
   controls and their Dirichlet series, the de Bruijn–Newman facts used,
   the exact flow (Theorem 1.2), the witness criterion and its local form,
   the trapezoid and strip-majorant lemmas, the moment lemma, the local
   expansion (7.6)–(7.8), Lemma 7.3 and the proof of Theorem 1.4.
2. **Witnesses.** All fifteen values \(H,H',H''\) and \(\mathscr L_0\) were
   recomputed at 60–80 digits by two methods: direct tanh-sinh quadrature
   of the control kernel, and the exact-flow formula with Gauss–Legendre
   quadrature of the unshifted kernel at complex arguments. The two methods
   agree to about \(10^{-58}\) relative.
3. **Moments.** \(m_0,m_2,m_4\) at \(t=0,\tfrac14\), \(\mu_4(\tfrac14,3)\),
   \(S_2\) and \(\xi(\tfrac12)\) by two quadratures and by `mpmath`'s
   \(\zeta\) and \(\Gamma\).
4. **Asymptotic theorem.** The inequality (7.9) at both regime corners,
   with a grid over \((\tau_0,\varepsilon)\) confirming the corner is the
   maximum; the identities (7.6)–(7.8) numerically (residuals below
   \(10^{-38}\)); and the bounds of Lemma 7.3 against direct values of
   \(F(0),F'(0),F''(0)\) at the theorem's times for several \((c,p)\),
   including \((\tfrac12,29)\), \((\tfrac12,41)\), \((0.99,101)\) and
   \((e^{-2},293)\). All bounds hold, and \(\mathscr L_0<0\) at each of
   these times.
5. **Numerics section.** Independent zero tracking for the lowest pair and
   spot checks of higher pairs.

## Findings and resolutions

| # | Finding | Resolution |
| --- | --- | --- |
| C1 | **Interval negation was not outward-rounded.** `Iv.__neg__` (and `absmax`, `sq`) used unary minus on `Decimal`, which rounds to the default 28-digit context. Every subtraction therefore lost directed rounding, and the old enclosures missed the true values by \(10^{-28}\)–\(2\cdot10^{-25}\) relative. The signs of \(\mathscr L_0\) were never in doubt (raw margins at least \(5\cdot10^{-6}\)), but the certificates were not rigorous. | Negation uses `copy_negate` (exact). The default context now traps `Inexact` and `Rounded`, so any arithmetic outside the directed-rounding contexts must be exact. Certificates regenerated. |
| C2 | `analytic_tail` and the choice of \(U\) mixed in default-context `Decimal` arithmetic. | Moved into interval arithmetic and the upward context. |
| T1 | Enclosure widths misstated. | Restated per quantity: \(H\) below \(2\cdot10^{-50}\), \(\mathscr L_0\) below \(10^{-51}\), \(\mathscr L_0/H^2\) below \(10^{-41}\). |
| T2 | "Rounded away from zero" for negative upper endpoints. | "Rounded upward". |
| T3 | \(x_0\) described as the real part of the pair. | "A point near the real part". |
| T4 | Low-height overclaims. At \(t=0\) every control has non-real zeros \(\pm(2k+1)\pi/a\pm i\delta\) at every height; at \(t=0.2\) the \(p=29\) control still has non-real zeros near \(13.00+0.30i\), \(16.70+0.30i\) and \(24.07+0.28i\). | Abstract, §1.4, (D2), the paragraph after it, and open problem (2) now say the controls fail direct inputs *already* at height \(\pi/a\le9.1\), where the lowest pair and the witnesses lie. |
| T5 | Remark 9.2 needs RH. | "Under RH" added. |
| T6 | Table 2 omitted the tracked case \((p,c)=(2,0.9)\); the "twelve tracked cases" sentence did not match the table. | Row added; sentence now names the twelve rows with three tracked pairs. |
| T7 | \(\pi/a\) for \(p=10007\) is \(0.68214\), not \(0.6822\). | Corrected, with \(c\) named. |
| T8 | Csordas–Smith–Varga was listed but not cited; "relative closeness"; the screening sentence could be read as a statement about \(\Lambda\) itself. | Cited in §1.1; "bounded relative distortion"; "cannot imply \(\Lambda_K\le0.2\) for all kernels \(K\) satisfying them". |
| T9 | \(\bar d=0.00037725\) exceeded the certified ratio \(0.00037724999\ldots\) by only \(3.5\cdot10^{-12}\). | Rounded to \(\bar d=0.000378\); the right sides of (7.9) become \(0.0144857<\tfrac1{50}\) and \(0.0679404<\tfrac1{10}\). |

## Status after the fixes

- All fifteen enclosures of \(H,H',H''\), \(\mathscr L_0\) and
  \(\mathscr L_0/H^2\), and all moment enclosures and \(S_2\), contain the
  independent 75-digit values (`mpmath`, tanh-sinh). All fifteen upper
  bounds for \(\mathscr L_0\) are negative.
- The corrected program reproduces identical enclosures under Python
  3.13.16 (cloud, 43 s) and Python 3.10.12 (the author's machine, 31 s).
  Record status `PASS`; regression checks for \(\pi\) and
  \(\xi(\tfrac12)/8\) pass.
- Theorem 1.4 lower bounds are consistent with the numerical collision
  times: \(0.199627<T_0(\tfrac12,41)\approx0.200117\) and
  \(0.194650<T_0(\tfrac12,43)\approx0.195103\).
- The manuscript compiles without overfull, underfull or undefined-reference
  warnings (16 pages).

## Points for a specialist reviewer

1. The application of Dobner's theorem in Proposition 3.3(c): matching of
   the completed function and heat deformation with \(H^{c,p}_t\).
2. The hypotheses of the Trefethen–Weideman theorem for the strip
   majorants, and the Riemann upper sum over cells in the program.
3. The monotonicity argument reducing (7.9) to the regime corner.
4. The screening statements of §9, which are methodological rather than
   theorems about \(\zeta\).
5. The program itself: an independent implementation of the certificate,
   preferably with a different interval library, would be the strongest
   check.
<<<<<<< HEAD

## Addendum: comparison with Note 2 (14 October 2026)

Claude Opus 5.5 (`claude-opus-5-5`; the serving model may differ), Claude
Cowork, reasoning effort **max**, after merging this work with the Codex
line of work.

[Note 2](../notes/2_CERTIFIED_EULER_FACTOR_WITNESS_20261014.md) certifies
\(\Lambda_{1/2,41}>1/5\) at \((c,p,t,x)=(\tfrac12,41,\tfrac15,\tfrac{168413}{100000})\)
with Arb ball arithmetic and validated quadrature of a rearranged
integral. The manuscript's program was evaluated at the same point, with
step \(h=1/64\) and the \(h=1/32\) consistency check. From `numerics/`:

```sh
python3 -B -c "import sys; sys.path.insert(0, '.'); import check_euler_control_witnesses_claude_20261014 as C; from decimal import Decimal as D; r = C.certify('1/2', 41, '0.2', '1.68413', D(1)/64, D(1)/32); print(*(k + ' ' + ' '.join(r[k]) for k in ('H', 'H_x', 'H_xx', 'L0')), sep='\n')"
```

Each of its enclosures lies inside the corresponding Note 2 enclosure,
compared exactly against the dyadic endpoints stored in
`EULER_FACTOR_WITNESS_RECORD_20261014.json`:

| Quantity | Value (this program) | Width here | Width in Note 2 | Difference of centres |
| --- | --- | --- | --- | --- |
| \(H\) | \(2.48694907959608368273107572369\ldots\cdot10^{-5}\) | \(2.9\cdot10^{-51}\) | \(5.9\cdot10^{-29}\) | \(1.1\cdot10^{-35}\) |
| \(H'\) | \(-1.28552501616067574161657072468\ldots\cdot10^{-6}\) | \(4.0\cdot10^{-51}\) | \(1.5\cdot10^{-28}\) | \(8.2\cdot10^{-35}\) |
| \(H''\) | \(0.213112372490154397876305453984\ldots\) | \(5.9\cdot10^{-51}\) | \(4.1\cdot10^{-28}\) | \(1.1\cdot10^{-32}\) |
| \(\mathscr L_0\) | \(-5.29999453357470506705202763817\ldots\cdot10^{-6}\) | \(6.2\cdot10^{-52}\) | \(1.3\cdot10^{-29}\) | \(2.7\cdot10^{-36}\) |

The value of \(\mathscr L_0\) also agrees with the centre of Note 2's
192-bit replay, \(-5.2999945335747050670520276381688873\cdot10^{-6}\), in
every displayed digit. The two programs share no code, arithmetic library
or quadrature rule, so the agreement checks both. The comparison was run
under Python 3.13.16 and 3.10.12 with identical output.
=======
>>>>>>> 94745f3 (Merged work from ChatGPT)

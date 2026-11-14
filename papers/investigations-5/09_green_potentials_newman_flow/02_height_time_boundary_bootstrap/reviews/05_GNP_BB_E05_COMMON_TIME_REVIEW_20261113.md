# E06 additional-agent review of the E05 common-time tail

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance, **gpt-6.1-sol / ultra** by
explicit tool selection. The reviewer is distinct from the proof
author, used the same model selection, shared the source inputs, and
previously wrote the [B02 geometry note][geometry] and [E04 review][e04].
This is internal additional-agent review. The inherited zero-time
provider keeps its existing same-model assessment level. No field
evaluation or specialist assessment was carried out. [Result index][results],
[avoid index][avoid].

**Disposition.** Accept saved [Note12][e05] within [E05 r1][packet]
and from its named inherited inputs. No mathematical correction
requested. The result supplies an unevaluated \(t_0>0\) such that
for every \(0<t\le t_0\), all zeros in the spatial region
\(|x|\ge4\pi e^{1/t}\) at that same time satisfy \(|y|<4/7\).
The new inputs are a positive-time value-provider extension and its
use on the full transition range \(1\le t\log(x/(4\pi))\le C\).

## Source conditions and order of constants

Rechecked the primary Polymath v2 equations (1), (3) and (4), Theorem
1.5(i), and the initial strip in the application of Theorem 3.2.
The two signs in the completed zeta argument give the same initial
field by its functional equation, with the same cosine heat source,
space variable and time. Theorem 1.5(i) gives a single finite
absolute \(C_P\) for all \(0<t\le1/2\). It gives real zeros in
its far tail. Note12 fixes \(C\ge\max(8,C_P)+1\) and \(D=C+1\),
then fixes the base growth constants and window \(V\), reserves
the enlarged fixed zero-time chart, fixes its Taylor and gamma
constants and height gates, and finally chooses \(t_0\) after
the comparison constants. The chart parameters and window are
independent of the later point, time and cutoff location.
[Polymath Theorem 1.5(i)][outer], [Polymath §3][poly],
[HDA Note04][hda], [HDA assessment][hreview].

## Extended provider

The proof uses exact source smoothing with the Gaussian
\((\pi t)^{-1/2}e^{-v^2/t}\,dv\) on the shifted argument \(z-2iv\).
The Gaussian moment of \(e^{2|v|u}\) is at most \(2e^{tu^2}\),
which with the complete theta source permits the exchange. It
applies the inherited zero-time CS3 on the entire enlarged local
chart, with the same \(N_x\) held fixed even on the shifted
points. It separately integrates the complete true source on
the near and far exteriors. The bound is proved on the fixed
\((1,9)\) chart for \(0\le tL_x\le D\) and \(t\le1/2\).

- **True near and far exteriors.** With \(V\ge D,16c_b\),
  \(x\ge4c_b\), and \(t\le1/2\), the three positive terms
  \(|v|L_x/2\), \(c_b|v|\), and \(c_bv^2/x\) sum to at most
  \((1/2+1/32+1/8)v^2/t\) on the near exterior. Splitting the
  remaining Gaussian gives \(x^{P_b}e^{-V^2/(8t)}\), which is
  \(O_D(x^{-2})\) by the squared-window lower bound. On the far
  exterior the height-relative full-ray logarithmic majorant
  is below \(v^2\) for all \(|v|\ge x^{1/3}\) once the height gate
  holds. The normalized tail is bounded by
  \(O(e^{-x^{2/3}/(4t)})\) uniformly in \(t\le1/2\). Passing from
  the central gamma scale to \(E_o\) is justified by calibration
  and the arithmetic-geometric mean.
- **Initial remainder.** Under each real shift in the zeta
  argument, the gamma modulus costs at most a fixed factor times
  \(e^{\pm v L_x/2}\). Its Gaussian moment is \(e^{tL_x^2/16}\)
  for both signs. This is precisely the growth in the comparison
  between the initial two-gamma and evolved two-carrier
  envelopes, giving a relative \(O_D(x^{-3/4})\) remainder.
- **Modes and their artificial tails.** The term
  \(-w\log n\) in the mode logarithm is linear in the shift. The
  quadratic Taylor error therefore comes only from the gamma
  logarithm and is uniformly \(O_{b,V}(v^2/x)\).
  In the completed linear mode put
  \(d_n=\alpha(w_\pm)-\log n\). The absolute tilted Gaussian,
  relative to its complex integral's modulus, has factor
  \(e^{t(\Im d_n)^2/4}\), uniformly bounded. Its real center
  \(\pm t\Re d_n/2\) is bounded by \(D/4+1\); its second moment
  before the bounded factor is \(t/2+\mu^2\). The Taylor
  error is therefore relative \(O_D(x^{-1})\) per mode.
  The artificial completion tail has exponential factor
  \(e^{-(V-\mu_*)^2/(2t)}\), paid after summation because
  \(V-\mu_*\ge V/2\).
- **Elementary calibration and population.** The exact
  log-gamma slope differs from the elementary slope by
  \(O_b(x^{-1})\). The change in the heat exponent is
  \(O(t(1+L_x)/x)=O_D(x^{-1})\). With
  \(\log N_x\le\Re L(z)\), the positive-time heat weight in
  each arm has modulus at most one after factoring out its
  elementary carrier and the signed vertical mode power.
  For \(y\ge0\) the dominant sum is bounded by
  \(\sum_{n\le N_x}n^{-1/2}\), while the other sum pays
  \(x^{-y/2}N_x^{(y+1)/2}\). Both are \(O_b(x^{1/4})\).
  Conjugation interchanges the bounds below the real axis.
  Thus the total mode error is \(O_D(E_o x^{-3/4})\),
  with all \(N_x\) modes included.
- **Correction.** The local vertical derivative estimate uses
  \(f_N'=O(x^{-3/4})\) and
  \(\mathcal G'/\mathcal G=-\pi/8+O(x^{-1})\). It is absolute
  in \(f_N\) and so applies when the correction vanishes.
  It yields the phase \(e^{i\pi v/4}\) and its Gaussian
  multiplier \(e^{-\pi^2t/64}\). The local derivative error
  and the artificially completed phase's tail fit the same
  remainder. The true correction stays within the local
  window and is bounded uniformly in the fractional cutoff.

These payments recover the stated value-provider exponent for the
enlarged positive-time range. At \(t=0\), CS3 and elementary mode
calibration give the value estimate directly. The proof uses
no positive-time extension of the HDA source as an imported
theorem, and uses no differentiated or negative-time statement.

## Finite-arm estimate and uniform spatial union

On \(1\le c=tL_x\le C\) and \(4/7\le y\le9/8\), the upper and
lower signs of the exact complex logarithm are retained in the
phase frequencies. The independent carrier check gives
\(\Re s_t\ge29/28>33/32\). The Euler product gives the stated
reciprocal bound 33, and even 29 under the same floor. The low
head uses \(n^{-225/224}(\log n)^2\) and costs \(A_D t\).
Only the ordinary zeta tail is extended to infinity. The
earlier exponent-pair theorem on arbitrary clipped dyads
applies with \(\tau\asymp x\), variation constants depending
on \(D\) and actual integer endpoints. The primary powers of
both arms are nonincreasing in \(c\), since their derivative
at fixed scale \(v\) is \(-v(1-v)/4\). At \(c=1\), the
dominant tail margin is \(17/82432\), and the reflected
endpoint powers are \(-5/42,-13/336\). The inverse terms,
ordinary tail, correction and two-carrier remainder have
faster fixed powers than \(\kappa=17/164864\). The exact replay
checks these values. [E04 exponent-pair review][e04],
[E06 arithmetic record][checks].

The proof chooses \(L_*=1/t_0\) after the finite provider and
arithmetic gates. For \(L_x\ge1/t\ge L_*\), both \(t\le1/L_*\)
and \((1+L_x)(4\pi e^{L_x})^{-\kappa}\le
(1+L_*)(4\pi e^{L_*})^{-\kappa}\) hold. The second follows by
taking \(L_*\ge1/\kappa\) and differentiating. The two
one-sided onset inequalities pay the factor 33 and the
relative threshold \(1/64\). Nonvanishing on the closed
transverse range, the inherited initial enclosure, and
conjugation exclude \(|y|\ge4/7\) in the finite range. At
\(tL_x=C\) both the new comparison and the published
all-real theorem apply, since \(4\pi e^{C/t}>e^{C_P/t}\).
Every \(x\ge4\pi e^{1/t}\) is in the transition or far tail,
and evenness supplies the negative heights. These are points
of the same theta field at one fixed time, with no comparison
between independent height-dependent fields.

The canonical premise screen remains that of E01–E03. The
new positive Gaussian proof uses the complete theta source,
CS3's arithmetic and the actual cosine phases. The outer
theorem also requires that canonical theta field. The
cutoff \(4\pi e^{1/t}\) diverges as \(t\downarrow0\);
the interior height interval and time zero require separate
estimates. [Collision controls12][controls], [scope07][scope].

[packet]: ../research-progress/handoffs/GNP-BB-E05-r1.md
[e05]: ../notes/12_GNP_BB_E05_COMMON_TIME_TAIL_20261113.md
[geometry]: ../notes/08_GNP_BB_B02_GEOMETRY_AND_OBSERVATION_20261113.md
[e04]: 03_GNP_BB_E01_E03_ADDITIONAL_AGENT_REVIEW_20261113.md
[hda]: ../../../01_heat_density_asymptotics/ansatz/notes/04_COMPLEX_STRIP_REMAINDER_AND_BUFFERED_CROSSOVER_20261025.md
[hreview]: ../../../01_heat_density_asymptotics/ansatz/reviews/03_COMPLEX_STRIP_AND_BUFFERED_CROSSOVER_ASSESSMENT_20261025.md
[checks]: ../numerics/08_GNP_BB_E05_REVIEW_CHECKS_20261113.json
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[scope]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[outer]: https://arxiv.org/html/1904.12438v2#S1.Thmtheorem5
[poly]: https://arxiv.org/html/1904.12438v2#S3

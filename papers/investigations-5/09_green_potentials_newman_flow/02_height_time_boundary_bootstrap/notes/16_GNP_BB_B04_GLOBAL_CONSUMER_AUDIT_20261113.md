# B04 global consumer audit for the common-time tail

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Subagent dispatch recorded
**gpt-6.1-sol / ultra**. Independent backend and token-use metadata were
unavailable.

**Status: checked contract and scoped implication.** This is the
global-use check in [B04 r1][b04], following [Note13][start].
[E05 Note12][tail], with [E06 Review05][review], supplies a canonical
spatial-tail theorem at each sufficiently small fixed positive time.
The new work identifies the exact portion of Polymath's three-part
criterion that it supplies and the overlap required for a global
conclusion. See the [result index][results] and [avoid index][avoid],
especially [cluster11][r11], [collision controls12][r12],
[classification01][a01], [shared premises02][a02], [scope07][a07],
[separate bounds12][a12] and [unchecked imports16][a16].

## 1. The published certificate

Use \(T\) for the intended final heat time, \(u\) for intermediate
heat time, and \(x\) for the real part of the repository's \(z\).
Polymath defines the same field and heat clock, since
\(H_0(z)=\xi((1+iz)/2)/8=\xi((1-iz)/2)/8\) and the source and
backward heat equation agree. In particular \(x/2\) is the ordinary
zeta ordinate in absolute value. Theorem 1.2, Proposition 3.3
and Theorem 1.5(i) were rechecked in the primary v2 text on this
date. [Polymath §§1 and 3][poly1], [§9 discussion][poly9].

Fix \(0<T<1/2\), \(0<y_0<1\), \(X>0\), and put
\(d=\sqrt{1-y_0^2}\), \(a(u)=\sqrt{1-2u}\).
In the nonempty range \(y_0^2+2T<1\), the required exclusions are

| Input | Proposition 3.3 zero-free set |
| --- | --- |
| (i) Initial bounded space | \(H_0(x+iy)\ne0\) for \(0\le x\le X,\ \sqrt{y_0^2+2T}\le y\le1\). |
| (ii) Final exterior | \(H_T(x+iy)\ne0\) for \(x\ge X+d,\ y_0\le y\le a(T)\). |
| (iii) Intermediate barrier | \(H_u(x+iy)\ne0\) for \(X\le x\le X+d,\ 0\le u\le T,\ \sqrt{y_0^2+2(T-u)}\le y\le a(u)\). |

Theorem 1.2 has the same (ii) and (iii). Its time-zero hypothesis is
the stronger ordinary-zeta exclusion for
\(0\le\Im s\le X/2\) and \((1+y_0)/2\le\Re s\le1\).
The time-zero set required by Proposition 3.3 starts instead at
\((1+\sqrt{y_0^2+2T})/2\), by the completed-zeta identity.
Proposition 3.3 yields no zeros at \(y\ge y_0\) for any real \(x\)
at time \(T\). Conjugation gives \(|y|<y_0\); the global strip
theorem (Theorem 3.2) then gives \(\Lambda\le T+y_0^2/2\).
This also explains the conclusion of Theorem 1.2.
[Polymath Theorem 1.2 and Proposition 3.3][poly1],
[Theorem 3.2][poly3].

A separate consumer takes a direct exclusion of the complete
finite-height final-time complement \(0\le x<R(T)\),
\(y_0\le y\le a(T)\), where \(R(T)\) is the available exterior
cutoff. This would also give a global width at time \(T\), by evenness
and conjugation, and then the same de Bruijn bound. It requires a
complete final-time compact exclusion. Polymath's initial-and-barrier
route is a different way to acquire that complement.

## 2. What E05 supplies

Write \(\tau_*>0\) for the admitted positive-time threshold in
E05 and \(R(u)=4\pi e^{1/u}\) for \(u>0\).
E05 proves \(|y|<4/7\) for every zero of \(H_u\) with
\(0<u\le\tau_*\) and \(|x|\ge R(u)\). Therefore choose
\(y_0=4/7\), \(d=\sqrt{33}/7\), \(0<T\le\tau_*\). The entire
exterior clause (ii) is supplied by the sufficient alignment
\[
                         X+d\ge R(T).                            \tag{1}
\]
The strict width includes exclusion of the closed lower edge
\(y=y_0\). Targets \(y_0\ge4/7\) also satisfy the corresponding
exterior clause with their own offsets and conditional global
bounds. E05's proof uses Polymath Theorem 1.5(i) only for the
all-real far tail. In the same normalization that theorem applies
for \(0<u\le1/2,\ x\ge e^{C_P/u}\), for a sufficiently large fixed
absolute \(C_P\). Its extra location asymptotic is unused. E05's
new finite-window estimate overlaps with the published region at
its chosen join. The far-tail theorem concerns positive times
and does not fill the missing finite-height or intermediate-time
conditions. [E05 §§1, 3–4][tail], [Polymath Theorem 1.5(i)][polytail].

On the barrier, E05 pays exactly the portion of its guaranteed region
with \(u\ge1/L_x\), where \(L_x=\log(x/(4\pi))\). More explicitly,
E05 by itself leaves the following portion of (iii) outside its
domain:
\[
 \begin{gathered}
 X\le x\le X+d,\quad 0\le u\le T,\quad
     u<1/L_x,\\
 \sqrt{16/49+2(T-u)}\le y\le\sqrt{1-2u}.
 \end{gathered}                                                   \tag{2}
\]
Here one may assume \(X>4\pi\), as enforced by (1) and the admitted
small-time range. In particular, \(u=0\) is included in (2).
When choosing the least \(X\) allowed by (1),
\(X=R(T)-d\), E05's guaranteed region meets this barrier
only at \((x,u)=(R(T),T)\) in the time/real-height plane,
with the barrier's transverse interval at that point. If \(X\)
increases, the paid portion can enlarge, while a near-zero-time
part remains for every fixed finite \(X\). At small \(u\) the
published far-tail cutoff \(e^{C_P/u}\) likewise escapes.
Clause (i) remains an independent initial exclusion. These
domain comparisons impose no exclusion outside E05 and do not
claim that the actual field has zeros in (2).

Thus E05 gives a final exterior and an explicit partial-barrier
payment. To complete this specific certificate one needs (i) and
the remainder (2) of (iii), on parameters with (1). Then
\(\Lambda\le T+8/49\) follows. An arithmetic estimate that lowers
the fixed width at \(uL_x\ge1\) lowers the quadratic contribution
to that conditional bound and leaves the near-zero-time side of
the barrier without coverage. A phase-preserving or signed Green
proposal meant to address the barrier must give full uniform
control at its actual \((x,y,u)\), including the endpoint \(u=0\)
or a separately justified continuation from it. For example,
the ordinary comparison carrier of E05 has
\(\Re s_u=(1+y)/2+u\Re L(z)/4\); in the sub-window \(uL_x<1\),
its lower transverse bound need not stay above \(1\).
The existing Euler-product floor cannot be carried down this
whole barrier by its present proof. [E05 §3][tail].

## 3. Quantitative compatibility of the available inputs

Platt–Trudgian's Theorem 1 verifies RH through the exact ordinary
ordinate \(H_{\rm PT}=3{,}000{,}175{,}332{,}800\). It supplies the
initial condition for \(X\le2H_{\rm PT}\) in the \(z\) coordinate,
with either of the two specified initial transverse thresholds.
It does not certify evolved values on (2). Their published
Corollary 2 gives \(\Lambda\le1/5\) by combining that finite
verification with the existing second row of Polymath §10 Table 1.
That row reports the separate exterior and barrier for its
own parameter choice, displayed as \(T=0.186,\ X=5\cdot10^{12}+194858,\ y_0=0.16733\). Its time and transverse domains differ from E05.
[Platt–Trudgian, Theorem 1 and Corollary 2][ptpdf],
[Polymath Table 1][poly10].

For the E05 recipe as proved, \(1/\tau_*\ge1/\kappa>64\), where
\(\kappa=17/164864\). Thus the smallest required \(X\) in (1)
for any \(0<T\le\tau_*\) exceeds \(2H_{\rm PT}\):
\(4\pi e^{64}-d>2H_{\rm PT}\). The currently guaranteed E05
parameters therefore have no overlap with clause (i) supplied
solely by this finite verification. This concerns the sufficient
onset recipe, with all further constants unevaluated. It puts no
lower bound on the true onset of the same zero exclusion.

There is also a constraint from the shape of the stated exterior
cutoff alone. Even if a sharper proof permitted any \(T\) compatible
with that cutoff, combining (1) with \(X\le2H_{\rm PT}\) gives
\[
 \frac1T\le\log\frac{2H_{\rm PT}+d}{4\pi}<27.
\]
For the last inequality one may use \(e^3>20\), \(\pi>3\) and \(d<1\).
Consequently
\[
     T+8/49>1/27+8/49=265/1323>1/5 .
\]
So a width-\(4/7\) certificate using this literal tail cutoff and
only the cited initial finite verification would fail to improve
the separate published \(1/5\), even with a paid barrier.
For a strict improvement on \(1/5\) at this width one needs
\(T<9/245\), hence \(X>4\pi\exp(245/9)-d\) under (1). This already
exceeds \(2H_{\rm PT}\). Other options require an improved exterior
cutoff, a different width, or a stronger initial zero-free region
than that finite verification at its stated height. The calculation
concerns the sufficient conditions as posed. It leaves open
alternative covers, a weaker-than-RH initial exclusion beyond
\(H_{\rm PT}\), effective sharp onset improvements and a direct
finite-height final-time method.

For fixed numerical \(X,T,y_0\) the initial exclusion is bounded in
two real variables, and (2) is a bounded three-real-variable
time-space exclusion. The latter needs a closed uniform
certificate, such as a positive lower bound with rigorously
propagated truncation and cover errors. Knowledge that the bounded
set fits inside a finite interval supplies no margin or operation
count. Compactness at fixed parameters would allow a finite
cover from already established local margins. It does not
establish such margins, their verification cost, or a common
bounded region as \(T\downarrow0\). No parameter set in the present
audit leaves a tractable certified gap, and there was no field
scan or numerical onset evaluation.

## 4. Prior coverage and limits of comparison

- Ki–Kim–Lee prove eventual reality and simplicity for each fixed
  positive time. Polymath distinguishes the nonuniform height
  dependence in that result from the explicit \(e^{C_P/u}\)
  form of its own Theorem 1.5(i). E05 claims only its finite-window
  comparison and the stated joined width. A stronger real-zero
  claim outside \(R(u)\) would require new input.
  [Ki–Kim–Lee publisher abstract][kkl], [Polymath §1][poly1].
- Polymath Proposition 9.1(i) assumes the large-constant
  \(x\ge e^{C/u}\) regime even for its stated asymptotic
  approximation. Its §10 introduces the same separation between
  finite-height verification, exterior, and intermediate barrier.
  The heuristics there about improving \(\Lambda\) from a known
  verification height do not remove any certificate hypothesis.
  [Polymath §§9–10][poly9].
- The broader literature includes Planat and Raymond's recent
  preprint claiming \(\Lambda<0.156821\) via a distinct
  collision-exclusion certificate. Only its abstract and opening
  formulation were inspected. No claim from it is imported here.
  Its stated target is below the bare width contribution \(8/49\).
  The audited numerical comparison above uses Platt–Trudgian's
  proved \(1/5\) as a stated baseline, with no best-known-bound
  or priority claim. [Planat–Raymond preprint][pr].

The source-specific control screen in [E05 §4][tail] is retained.
The Polymath exterior and initial certificate require the complete
canonical theta field and its ordinary zeta completion. Euler-factor,
weighted-square, reflected and primitive-compatible controls lack
the corresponding unmodified coefficients or full canonical
source; the other failed premises are listed in [Note06 §4][e01].
No generic zero dynamics or contour argument supplies either missing
global hypothesis. This is a consumer audit within B04 and gives
no new global width, Newman bound, or novelty conclusion.

[b04]: ../research-progress/handoffs/GNP-BB-B04-r1.md
[start]: 13_GNP_BB_CONTINUATION_AFTER_COMMON_TIME_TAIL_20261113.md
[tail]: 12_GNP_BB_E05_COMMON_TIME_TAIL_20261113.md
[review]: ../reviews/05_GNP_BB_E05_COMMON_TIME_REVIEW_20261113.md
[e01]: 06_GNP_BB_E01_COMPLETE_OUTER_ESTIMATE_20261113.md
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[r12]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a16]: ../../../../../avoid/16_unchecked_imports_and_novelty_claims.md
[poly1]: https://arxiv.org/html/1904.12438v2#S1
[poly3]: https://arxiv.org/html/1904.12438v2#S3
[poly9]: https://arxiv.org/html/1904.12438v2#S9
[poly10]: https://arxiv.org/html/1904.12438v2#S10
[polytail]: https://arxiv.org/html/1904.12438v2#S1.Thmtheorem5
[ptpdf]: https://arxiv.org/pdf/2004.09765
[kkl]: https://www.sciencedirect.com/science/article/pii/S0001870809001133
[pr]: https://arxiv.org/abs/2611.06245


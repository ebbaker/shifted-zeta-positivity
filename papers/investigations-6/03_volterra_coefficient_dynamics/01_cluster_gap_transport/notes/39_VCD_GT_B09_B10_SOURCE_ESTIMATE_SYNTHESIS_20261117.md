# Source-specific transverse correction and exceptional isolated pairs

17 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance, chat0006. Actual root model/effort unavailable.
Conceptual dispatch gpt-6-astra/ultra; analytical execution and assessment
requested as gpt-6.1-sol/ultra. Dispatch is not a backend attestation.

**E16/E17/E19 proved in-note; accepted within scope by [E18 / Assessment17][review].** B09
selects a complete-source transverse second-moment estimate. B10 combines the paid collar, pair packing and canonical transverse
density to count isolated pairs with negative interaction. The separate
reviewer required no correction. This is internal checking
with shared premises, not independent specialist validation. The
[sole register][progress] owns live status.
This continuation supersedes Note35's next-action routing, not its results.

| Next task | Type / recommendation | Dependency and concrete output |
| --- | --- | --- |
| VCD-GT-E18 | E / Sol6.1 ultra | Complete: all three proofs and the integration accepted without required correction |
| VCD-GT-B11 | B / Astra ultra | Next conceptual gate: select an additional source input capable of controlling exceptional pairs at a fixed microscopic collar; no execution contract yet |
| VCD-GT-E13 | E / Sol6.1 ultra | Still unissued: no numerical experiment is needed for the present analytical questions |

Read the [result index][results], especially [controls12][controls] and
[cluster18][cluster], and the [avoid index][avoid], especially
[classification01][a01], [premises02][a02], [scope07][a07],
[joint estimates12][a12] and [sibling reuse15][a15]. These are quantitative
intermediate estimates and one scoped allowance failure, not an acquired
all-pair positivity criterion. No manuscript or sibling task is changed.

## 1. Selected source input and the actual averaged gain

Use the unchanged canonical H_t, physical time 0<=t<=1/2, all zero
multiplicities, and L=log T, ell=1/L frozen over X in [T,2T]. For T>=16,
1<=a<=L and 3<=R<=T/2, put

\[
 \Xi_{a,R}(t,X)=\ell^2\!\sum_{\substack{|\rho-X|\ge a\ell\\
                              |\Re\rho-X|\le R}}
                   \frac{(\Im\rho)^2}{|\rho-X|^4}.
\]

[E17 / Note37][e17] proves the estimate

\[
 \frac1T\int_T^{2T}\Xi_{a,R}(t,X)\,dX\le\frac{C_s}{a^3},
 \tag{1}
\]

with constants independent of t,T,a,R. The additional complete-source
input is the accepted TND-O dyadic transverse second moment
sum y^2=O(T/log T), uniform on the closed time slab. [Source-use06][source]
identifies that theorem, its internal assessment, and fresh selected
primary inspection of the time-zero density input. The new proof step
is the exact contraction against the exterior kernel:

\[
 \int_{x^2+y^2\ge r_0^2}\frac{y^2\,dx}{(x^2+y^2)^2}
 \le\frac\pi2\min\!\left\{\frac1{r_0},\frac{y^2}{r_0^3}\right\}.
 \tag{2}
\]

The cutoff restricts relevant zero ordinates to [T/2,5T/2]. Tonelli,
three dyadic bands, (2), and r_0=a ell give (1) without tracking zeros
or differentiating a cutoff. Giving the same averaged calculation only
the total count O(T log T) gives C_0/a. Thus the source gain is two
powers of **normalized exclusion radius**, not a comparison of averaged
and pointwise bounds. At fixed a both allowances are O(1). At
 a=L^eta, 0<eta<1, they are O(L^(-3 eta)) and O(L^(-eta)), while the
physical radius a ell still tends to zero. Constants are unevaluated.

The unconditioned sum exists at every center without a count-two event.
Its use for a pair needs the independently paid exterior collar a ell.
No growing empty region or selected-pair probability distribution has
been acquired.

## 2. Exact bridge to the signed near interaction

For a paid conjugation-invariant pair with center c in [T,2T], write
D real, |D|<=d ell^2, a^2>d, and assume every exterior zero obeys
|rho-c|>=a ell. For w=x+iy=rho-c, r^2=x^2+y^2, E17 proves

\[
 q=\frac1{r^2-D}
 -\frac{2y^2(r^2+D)}{(r^2-D)((r^2-D)^2+4Dy^2)}.
 \tag{3}
\]

The correction is nonnegative and at most
C_delta y^2/r^4, where delta=d/a^2<1 and
C_delta=2(1+delta)/(1-delta)^3. All denominators are positive in
this domain, including D<0. Summing the exterior groups gives

\[
 \ell^2 S_R\ge
 \ell^2\sum_{\mathrm{near}}\frac1{r^2-D}
                  -C_\delta\Xi_{a,R}(t,c).
 \tag{4}
\]

The target roots are inside a ell and are absent from Xi at this center.
Real exterior roots have zero transverse correction. Equations(3)–(4)
include D=0 and both signs of D without dividing by the internal gap.
The radial term is nonnegative but its useful lower mass is not acquired.
Equation(1) is not a bound at an arbitrarily selected c.

## 3. Isolated-pair counts: the sharper signed estimate

[B10 / Decision18][b10] fixes a deterministic extension, [E19 / Note38][e19].
On a fixed slice take all distinct unordered, multiplicity-counted pairs
with c in [T,2T], |D|<=d ell^2, exterior collar a ell, and

\[
 \max(2,4\sqrt d)\le a\le L,\qquad 3\le R\le T/4.
\]

The collar prevents distinct eligible pairs from sharing a zero occurrence.
Their centers separate by at least (a-sqrt d)ell>=3a ell/4. Consequently
intervals I_c=[c-a ell/4,c+a ell/4] are disjoint. Moving from c to X in
I_c changes each retained exterior distance by at most one quarter;
its term survives the enlarged horizontal cutoff R+a ell/4 and radial
cutoff a ell/2, with at least beta=(4/5)^4 of its original weight.
This pays spatial visibility, without an assumed conditional law.

The general transverse count for Xi(t,c)>=h>0 is

\[
 N_{\rm bad}\le \frac{16 C_s}{\beta}\frac{T L}{a^4h},
 \tag{5}
\]

while the same proof with counts alone gives
4C_0 T L/(beta a^2 h). The padded integration band and its finite
population are paid in E19, rather than silently extending (1)'s domain.
A separate packing cap is 1+4 T L/(3a). These are deterministic counts
of eligible isolated pairs, uniform in t; they do not count time events.

Because delta<=1/16, C_delta<=8704/3375. A pair satisfying
ell^2 S_R<=-epsilon has Xi>=epsilon/(8704/3375), so (5) also bounds
strongly negative signed near interactions. The far groups are positive
for R>=3, width<=1 and |D|<=1/16; hence strongly negative full M forms
a subset of these cases. This implication is not an acquired M lower
bound for every eligible pair.

For fixed-threshold transverse loss, advertise the power-law example
only for 0<eta<1/2: at a=L^eta, (5)/(T L)=O(L^(-4 eta)/h), compared
with O(L^(-2 eta)/h). A matched pointwise unit-count/strip estimate is
Xi=O(L/a^2+1/L). For a much larger than sqrt L it already excludes a
fixed threshold h, so that range is not a new fixed-threshold achievement.

For the **sign** of the interaction there is a sharper source estimate.
A negative q requires y^2>(r^2-D)/2, so the collar implies
|y|>2a/(3L). On the enlarged zero band [T/2,5T/2], the complete source supplies
N(v)<=B_b^* T L exp(-b L v), for 0<v<1 and fixed 0<b<1/2. For a given exterior zero,
negative q can occur only at centers within |y|+a ell/4 of its real
part. Center separation bounds the number of eligible pairs incident to
that zero by 5/3+8|y|/(3a ell). Summing these incidences and integrating
the exponential tail gives the selected stronger bound

\[
 N\{S_R<0\}\le C_b' T L\exp(-2ba/3),\qquad
 N\{M<0\}\le N\{S_R<0\}.
 \tag{6}
\]

For example b=1/4 gives a bound C T log(T) exp(-a/6). No numerical
constant or finite onset has been certified. Normalizing by T L does not
produce a fraction of the eligible-pair population; its size is not paid.

The equally informed count-only baseline includes the packing cap
1+4 T L/(3a). This sign statement needs no fixed negative threshold.
For a=L^eta, 0<eta<1, its normalized count decays as
O(exp(-2b L^eta/3)). The pointwise Xi bound tending to zero does not
exclude an arbitrarily small negative sign, so that distinction matters.
Even at a=L, (6)'s stated allowance is a positive constant times
T^(1-2b/3) L and grows. It does not force zero exceptions. This is a
limitation of that allowance, not a lower bound on the true count.

## 4. The other tested source proposal and controls

[E16 / Note36][e16] tests the literal continuous-source Fourier numerator
P=2(F''')^2-3F''F'''', with positive product-frequency density nu_t and
total mass W_t=3m_2(t)m_4(t). Retain any measurable collection of
nonnegative cosine phases and pay every discarded phase by -1. Even
retaining **all** favorable lobes has the uniform allowance

\[
 U_t(c)=\left(\frac1\pi-\frac12\right)W_t+O(c^{-1})<0
 \quad\hbox{for sufficiently large }c.
 \tag{7}
\]

The first anti-diagonal lobe has allowance -W_t+O(1/c), with the sharper
coefficient in Note36. A bounded periodic primitive pays (7); exact theta
reflection and the full tail pay the uniform source derivatives. Positive
averaging of these allowances cannot reverse the negative result.
This is a failure of this lower allowance. It does **not** assert P<0
or M<0. P/(18F''^2)=M is the double-zero identity only; no time tube of
persistent doubles or extension to D!=0 is assumed. Jointly retaining
negative phases is outside this screen.

[Decision17's control table][b09] and the proof notes keep each failed,
shared or untested premise. The particularly informative extra check is
that Note34's opposite-sign fixed-slice controls also preserve both the
broad second-moment inequality and the full transverse-density upper
bound at time zero, with enlarged uniform constants. Deletions reduce
both populations; the two inserted nonreal marks add at most
24/(log c)^2 to the moment and have bounded scaled transverse height
in every dyadic band they enter. Note38 checks the density constant
explicitly. These controls meet E19's geometry at a=2 and remain
compatible with its exception counts while retaining their bad selected
center. No common heat-time realization is supplied. The new estimates
are aggregate information, not pointwise sign discriminators.

[Predecessor audit16][audit] preserves the earlier covariance, source-node
Ward, marked-pair evolution and all-order transverse-moment scopes. Their
unpaid signed insertions and selected-pair conditioning are not filled
by a change of representation. The direct evaluator receives all source
moments, geometry, signed identities and estimates used here. No cost
advantage, new canonical zero coverage, incoming margin or Newman bound
is claimed. The accepted far-tail result and local 176-bracket certificate
retain their separate scopes.

## 5. Continuation boundary

B09's selected averaged source estimate and B10's
exceptional-pair count are a substantial integrated intermediate result.
They do not justify a numerical scan or a larger-cluster extension.
GT-E06, parent VCD-B07/E25, sibling tasks and the manuscript are unchanged.

The next conceptual gate is **B11 / Astra ultra**: select an additional
source estimate that controls the exceptional selected-pair centers at
a fixed microscopic collar, or a sharper visibility/conditioning estimate
whose numerical allowance can resolve one exception. The current mean
and count estimates must be given to the direct comparator. A merely
favorable assumption on S_R, Xi or the incoming cost is not an execution
contract. The existing source moment is already compatible with the
fixed-slice opposite-sign controls, so literal theta naming is insufficient.
No such stronger source input is selected in this continuation.

```text
Continue VCD-GT with [B] VCD-GT-B11 — Astra/ultra. Read the sole register,
Decision17–18, Notes36–39, E18 assessment, predecessor audit16, the
result/avoid indexes and controls. Keep the actual theta source, frozen
spacing scale, both D signs, count/collar and independent incoming anchor.
Compare at most two concrete ways to control the remaining exceptional
selected-pair centers. Require an explicit additional source quantity,
domain, proof route and fixed-collar success test; do not reissue the
unconditioned average or assume a favorable remainder. A precisely scoped
failure is a valid result. Freeze new Sol/ultra execution only once its
mathematical contract exists. Keep progress, notes and guarded history.
```

[progress]: ../research-progress/01_VCD_GT_RESEARCH_PROGRESS_20261116.md
[b09]: ../brainstorm/notes/17_VCD_GT_B09_SOURCE_NEAR_FIELD_DECISION_20261117.md
[b10]: ../brainstorm/notes/18_VCD_GT_B10_ISOLATED_PAIR_VISIBILITY_DECISION_20261117.md
[e16]: 36_VCD_GT_E16_COMPLETE_SOURCE_PHASE_ALLOWANCE_20261117.md
[e17]: 37_VCD_GT_E17_AVERAGED_TRANSVERSE_CORRECTION_20261117.md
[e19]: 38_VCD_GT_E19_ISOLATED_PAIR_EXCEPTION_COUNT_20261117.md
[source]: ../references/06_VCD_GT_TRANSVERSE_MOMENT_SOURCE_USE_20261117.md
[audit]: ../reviews/16_VCD_GT_B09_PREDECESSOR_RATE_AUDIT_20261117.md
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[cluster]: ../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a15]: ../../../../../avoid/15_ignoring_sibling_results_and_unfinished_closures.md

[review]: ../reviews/17_VCD_GT_E18_SOURCE_AND_PAIR_COUNT_ASSESSMENT_20261117.md

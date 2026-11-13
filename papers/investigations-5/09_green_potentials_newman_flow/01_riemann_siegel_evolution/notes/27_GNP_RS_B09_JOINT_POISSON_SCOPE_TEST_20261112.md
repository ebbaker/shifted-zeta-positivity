# GNP-RS-B09 — joint-shift transform and applicability tests

12 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Chat0006, thread
`01a1d151-91b1-7663-8f10-07d0b4f94163`. Actual backend model and reasoning
effort are unavailable in the recorded source configurations; helper
settings are not inferred. Three analytical helpers contributed the
stationary-point, source-range and premise checks. This is contributing
internal checking with shared inputs, not independent specialist review.

**Status: proved in-note scoped diagnostic and primary-source applicability
screen, with contributing separate-agent internal checking.** The bounded
request from [Note26][return08] is complete at that scope. **No improved
joint-cancellation estimate or every-center theorem is proved.** B08's
17/72 localization and complete residual ledger remain unchanged.

The selected route retains the joint m,h phase, tests its two-dimensional
stationary geometry, and asks whether a direct published joint estimate
supplies the missing cancellation. The first failure is quantitative:
absolute payment of the dual stationary population costs
\(U^{3/8}/\ell\), even on a fixed interior portion of the actual arm.
The direct Bourgain–Watt Theorem 2 import fails its shift-range hypotheses
on the relevant population. Neither statement is a lower bound on the
actual shifted sum or a prohibition on other joint methods.

Under [target01][a01], this is a bounded method test with a proved
allowance calculation, not an RH-equivalent criterion or a new positive
localization milestone. Read [result summaries][results], particularly
[heat-flow cluster11][r11], and [avoid][avoid], particularly
[premise02][a02], [scope07][a07], [separate-bounds12][a12] and
[unchecked-imports16][a16]. Section 7 applies [controls12][controls].

## 1. Exact consumer and inherited payments

Use [Note25][b08], equations (B08.4), (B08.11) and (B08.14), without
changing the source, carrier or physical clock. Set
\[
 L_U=\log(U/(4\pi)),\quad
 t=\frac{\nu_U}{2\pi}=\frac{U}{4\pi}+\frac1{16L_U},\quad
 f(m,h)=t\log(1+h/m),\quad e(v)=e^{2\pi iv}.
\]
The comparable part of the frozen complete-arm tail contains
\[
 S_N=\sum_{h\ge1}\sum_{m\in I_{N,h}}
   w_m(U)w_{m+h}(U)
   \widehat\chi\!\left(\frac\ell2\log(1+h/m)\right)e(f(m,h)),
                                                        \tag{B09.1}
\]
where the actual integer restrictions include
\(Y<m<m+h\le N_U=\lfloor\sqrt{U/(4\pi)}\rfloor\),
\(m\in[N,2N)\), and \(h<m\). Here \(Y=\lfloor U^{1/9}\rfloor\).
The positive real extension used below is
\[
 w_x(U)=x^{-3/4}\exp((\log x)^2/(4L_U)).
\]
The fixed smoothing function is B07's nonnegative chi, with integral 4,
support in [-2,3], and
\(\widehat\chi(\xi)=\int\chi(v)e^{iv\xi}dv\).
Its effective shift scale is \(H\asymp N/\ell\); H in this note
denotes a shift scale, not Note25's Euler-product bound.

The existing weighted block estimate is
\[
 |S_N|\le C\{U^{2/7}N^{1/28}\ell^{-9/7}
       +U^{-1}N^{3/4}\log(2+N/\ell)\}+E_N,              \tag{B09.2}
\]
where E_N≥0 pays the complementary large shifts and
\(\sum_N E_N\ll U^{3/8}\ell^{-4}\). Noncomparable pairs have the
same global payment. The complete tail norm uses
\[
 A_1\ll Y^{-1/4}+U^{17/56}\ell^{-9/7}
             +U^{3/8}\ell^{-4}+U^{-5/8}(1+\log U).        \tag{B09.3}
\]
These are benchmarks, not claims proved again here. At the largest scale
\(N\asymp\sqrt U\), the leading term is order one when
\(\ell=U^{17/72}\). A genuine improvement must survive all the
complete-field, multiplier and finite-head payments in (B08.14).

B07's exact Fubini weight, its mass 1−O(U^-4) and bounded variation,
full freezing/cutoff cost, and reflected nonstationarity remain paid.
Physical time 1/L_X is fixed inside each spatial window. The prime cutoff
P is constant over the outer interval and lies between 2 and floor(L_U²).
No new estimate here reopens or simplifies these inherited obligations.

## 2. Exact stationary geometry: the dual phase is another log ratio

The change \(n=m+h\) is unimodular on the integer grid. In these
coordinates the phase separates:
\[
 F(m,n)=t(\log n-\log m),\qquad
 \det D^2F=-\frac{t^2}{m^2n^2}.                          \tag{B09.4}
\]
The same determinant holds in (m,h). In particular,
\[
 f_m=-\frac{th}{m(m+h)},\quad f_h=\frac{t}{m+h},\quad
 \det D^2f=-\frac{t^2}{m^2(m+h)^2}.                      \tag{B09.5}
\]
The determinant is nonzero, but is of order one at the dominant
\(m,n\asymp\sqrt t\) scale. A continuous curvature statement does
not by itself bound the discrete sum.

For integer dual frequencies (-a,b) in (m,n), with a>b>0, consider the
oscillatory integral phase \(F(m,n)+am-bn\). Its unique positive
critical point and stationary value are exactly
\[
 m_* =t/a,\qquad n_*=t/b,\qquad
 F(m_*,n_*)+am_*-bn_*=t\log(a/b),                       \tag{B09.6}
\]
\[
 |\det D^2F(m_*,n_*)|^{-1/2}
       =\frac{m_*n_*}{t}=\frac{t}{ab}.                  \tag{B09.7}
\]
The two linear terms cancel at the critical point. The Fourier-weight
argument is preserved exactly:
\(\log(n_*/m_*)=\log(a/b)\). In (m,h) the corresponding integer
frequency is (-(a-b),b), so no grid or frequency is lost in this identity.

For an original interior block m≈N, h≈H, the dual size and dual shift
are respectively
\[
 a,b\asymp t/N,\qquad a-b\asymp tH/N^2.
\]
The gradient-image area is of order \(t^2H/N^3\), and the
stationary amplitude is of order \(N^2/t\). Their product is
\(tH/N\). At \(N\asymp\sqrt t\), both dual scales return to the
original scales and this population payment is of order NH. Below that
scale the ratio to NH is t/N², which is larger.

These are identities and geometric scales. We do **not** assert a full
Poisson expansion with uniformly bounded remainder, sharp endpoints or
transition terms. The next section defines and proves a precise statement
about the proposed absolute leading-term allowance. Thus it can test the
method before any unpaid transform remainder is used as an estimate.

## 3. A proved lower bound for the absolute stationary allowance only

Fix \(0<\beta<1/2\), put \(\ell=U^\beta\), and set
\(R=\sqrt t\), \(\epsilon=1/10\). Consider integer pairs
\[
 2R\le b\le(5/2)R,\qquad
 \epsilon R/\ell\le d\le2\epsilon R/\ell,\qquad a=b+d.
                                                               \tag{B09.8}
\]
Both integer interval lengths tend to infinity, so the number of pairs
is comparable to \(R^2/\ell\). For all sufficiently large U,
their critical points satisfy
\[
 R/3<m_*<n_*\le R/2,
 \qquad h_*=n_*-m_*\asymp R/\ell.
\]
They therefore lie strictly inside the actual head/full-cutoff range,
with \(Y<m_*<n_*<N_U\) and h_*<m_*. This is a fixed interior
portion of the largest arithmetic scale, meeting only a bounded number
of the m-dyadic blocks. Critical points need not be integer: the dual
indices a,b are the integers in this allowance.

Define the exact nonnegative functional
\[
 \mathcal P(U,\ell)=\sum_{(b,d)\text{ in (B09.8)}}
   \left|w_{t/(b+d)}(U)w_{t/b}(U)
    \widehat\chi\!\left(\frac\ell2\log(1+d/b)\right)\right|
   \frac{t}{b(b+d)}.                                    \tag{B09.9}
\]
It is the absolute leading-stationary payment on that specified interior
population. It is **not** the actual correlation, tail norm or a claimed
lower bound for either.

**Proposition.** Uniformly as U tends to infinity for each fixed beta in
(0,1/2),
\[
 \boxed{\mathcal P(U,U^\beta)\asymp U^{3/8-\beta}.}       \tag{B09.10}
\]
The constants can depend on beta and the fixed smoothing function.

**Proof.** On the chosen rectangle,
\[
 0\le\xi=\frac\ell2\log(1+d/b)\le\epsilon/2=1/20.
\]
Nonnegativity and the support of chi give
\[
 \operatorname{Re}\widehat\chi(\xi)
   =\int\chi(v)\cos(v\xi)dv
   \ge4\cos(3/20)>0,\qquad |\widehat\chi(\xi)|\le4.      \tag{B09.11}
\]
Also t/[b(b+d)] is bounded above and below by positive constants.
For x=qR with q in a fixed compact subinterval of (0,1),
\(\log t=L_U+o(1)\), and direct substitution yields
\[
 \log w_{qR}(U)=-5L_U/16-(\log q)/2+O(L_U^{-1})+o(1).
\]
Thus the actual weights, not merely their upper envelopes, satisfy
\(w_{m_*}(U)w_{n_*}(U)\asymp R^{-5/4}\).
Multiplying this by the \(\asymp R^2/\ell\) terms proves
\(\mathcal P\asymp R^{3/4}/\ell\asymp U^{3/8}/\ell\).
The integer count follows from the independent b,d intervals; it does
not rely on replacing a thin curved region by its area. QED.

At the B08 endpoint this particular allowance is
\[
 \mathcal P(U,U^{17/72})\asymp U^{5/36}.                 \tag{B09.12}
\]
Hence the proposed procedure “transform, then pay each dual stationary
term by its absolute leading amplitude” cannot improve the current
order-one block benchmark. It cannot even recover the useful part of
B08's range below exponent 3/8. This failure remains if a hypothetical
transform remainder were zero; adding nonnegative error allowances does
not repair it. Cancellation between principal contributions, between
principal and transition terms, or an estimate that does not separate
them lies outside this tested procedure. We do not infer a failure of a
fully signed Poisson method, nor the existence of a large actual tail.

## 4. Nonresonance and determinant-only premises do not repair the step

There is an exact canonical test of a blanket first-derivative gap. The
map
\[
 t(U)=U/(4\pi)+1/(16L_U),\qquad
 t'(U)=1/(4\pi)-1/(16UL_U^2)
\]
is eventually strictly increasing and unbounded. For each sufficiently
large integer j, choose its unique large real preimage U_j of
\(t=2j(j+1)\). At the actual integer pair m=j,h=1,
\[
 f_h=2j\in\mathbb Z,\qquad f_m=-2\in\mathbb Z.           \tag{B09.13}
\]
The pair belongs to the complete tail: j>Y eventually, and
\[
 U_j/(4\pi)-(j+1)^2=j^2-1-1/(16L_{U_j})>0.
\]
Thus j+1≤N_Uj and this is an interior largest-scale pair. The shift h=1
is within the Fourier-effective range for each beta<1/2. Consequently a
uniform positive distance of the canonical gradient from the frequency
lattice is false at arbitrarily large actual starting heights. This
does not imply simultaneous phase coherence of the complete population.

A separate reduced-class screen shows why determinant magnitude alone
is insufficient. On integer (m,h), let
\[
 G(m,h)=-2mh-h^2.
\]
Then det D²G=−4 but e(G)=1. Choose N=floor(N_U/4). For m in [N,2N] and
1≤h≤N/(10ell), the same Fourier factor has argument at most1/20;
(B09.11) keeps its real part positive. All these pairs are inside the
cutoff and N is comparable to sqrt(U). The actual positive weights are comparable to
N^-5/4. Hence this modified-phase sum has real part comparable to
N^(3/4)/ell when N/ell tends to infinity. It disproves a saving asserted
from just this determinant, coefficient size and smooth-weight class.
The quadratic does not retain the canonical logarithmic derivatives or
complete arithmetic phase. It is a premise screen for that reduced
class only, not a theta counterexample or a disproof of a theorem using
the actual phase identities.

## 5. Direct Bourgain–Watt joint-theorem import: the shift gates fail

The [pinned primary source][bw] is Bourgain–Watt, arXiv:1505.04161v1,
Section 6, printed pages 14–15, Theorem 2. Its exact formulas and selected
passages are recorded in the dated B09 appendage to the existing
[source-use record][sources]; the archived PDF is unchanged. This screen
uses only necessary conditions, not the theorem's conclusion. Even
granting the favorable transfer of the asymmetric grid and smooth
amplitudes to its symmetric difference phase, those conditions fail.

Match its parameters at the dominant scale by
\[
 T\asymp U,\qquad M\asymp\sqrt T,\qquad H\asymp M/\ell.
\]
For every integer nu≥6, Part A condition (6.6) requires, up to its stated
fixed logarithmic factor,
\[
 \frac HM\ll T^{-a_\nu},\qquad
 a_\nu=\frac{149\nu-400}{16(29\nu-75)}
       \ge\frac{247}{792}.                              \tag{B09.14}
\]
The derivative of this rational expression in nu has positive numerator
425 after removing the fixed positive factors, so the minimum is at6.
Thus direct use on the effective shifts requires window exponent at
least247/792, already larger than17/72. At the B08 endpoint the required
shift exponent is19/72, whereas the largest permitted Part A exponent
is1/2−247/792=149/792. The gap is exactly5/66. Fixed logarithmic factors
cannot close this power gap.

The first inequality of Part B condition (6.11) gives, up to logarithms,
\[
 H\ll M^{(155\nu-480)/(189\nu-480)}
       T^{-(46\nu-160)/(189\nu-480)}.
\]
At M≈sqrt(T) its T exponent is exactly
\[
 \frac{(155\nu-480)/2-(46\nu-160)}{189\nu-480}
       =\frac16.                                       \tag{B09.15}
\]
It therefore misses the required H≈U^(19/72) by7/72 in the exponent.
The other hypotheses need not be resolved to reject this direct import.
Neither part can improve B08 via this parameter substitution.

The excluded shifts are not a removable far tail. In the band
h≈cN/ell for fixed sufficiently small c>0, the Fourier argument is a
small fixed number; (B09.11) gives a positive lower bound, not a power
of U. One cannot discard that band with the already paid Fourier decay.

Nor may H in the source be replaced freely by a short subdivision's
length: its sum is over an actual shift band H/2<h≤H. Recentering
h=h0+s changes the phase. In the symmetric source notation, already
the base factor
\[
 \exp\{i\nu_U\log((m+h_0)/(m-h_0))\}
\]
has total variation comparable to \(U h_0/N\) on a fixed full
m-block when h0≪N. At h0≈N/ell that is U/ell. Transferring this
factor into an amplitude loses bounded variation. A theorem adapted to
the recentered phase, or a separately paid restriction in m, is additional
work; the printed theorem does not provide it for free. This rejects
only the direct theorem import and unpaid recentering repair. No survey
of all joint-sum results or later paper versions is claimed. In particular,
the authors' Remark (i), printed page15, says their upper restrictions
(6.6) and (6.11) are stronger than their method requires and that an
additional case was omitted. That remark supplies no estimate here;
extending the proof into that case is unperformed work, not ruled out.

## 6. Return to the full residual and every-center question

There is no new bound to insert into (B08.14). Consequently M,Y=U^(1/9),
the full-field/cutoff and multiplier payments, and the current theorem
remain those of Note25. For fixed0<rho≤19/72 and every sufficiently
large real U, the useful range remains
\[
 U^{17/72+\rho}\le\ell\le U.
\]
At P=floor(L_U²), residual-mean error is O_rho(L_U^-3/2), residual mean
O_rho(L_U^-1), Green mean O_rho(L_U^-1/3), and the fixed-positive-threshold
exceptional proportion O_(h,rho)(L_U^-1). B09 neither weakens nor
strengthens these proved-in-note inherited-input statements.

The remaining joint arithmetic obligation is cancellation among the
signed population at N≈sqrt(U), h≈N/ell, with the actual common height
phase and Fourier weight. The reciprocal map exposes its persistence;
merely asserting that the transformed correlation is small renames the
missing estimate. No new conditional criterion is registered as progress.

Even an improved positive localization exponent would not by itself give
every-center control: the allowed total Green mass
O(ell L_U^-1/3) still diverges on the present windows. A direct pointwise
or maximal estimate, or a quantitatively sufficient persistence-versus-mass
comparison along X↦(1/L_X,X), is still absent. No localized positive defect
has been excluded. The c=1, original strip/depth/radius, block-constant
cutoff, unevaluated onset and untreated bounded-height qualifications
remain. Full-c, center-varying-cutoff, shrinking-depth, time-zero and
positive-threshold exclusions remain open under their existing ownership.

## 7. Collision controls, assessment and bounded stop

The [control catalog][controls] is screened against the canonical premises
used to identify (B09.1), rather than against a nonexistent exclusion.

| Control class | Premise not retained in this canonical application |
| --- | --- |
| Euler-factor/translated sources and earlier heat counter-kernels | Unchanged complete theta source, coefficients/completion and corresponding arm identity. |
| Weighted finite-square, finite-tail and finite-prime-orbit controls | Complete unchanged coefficient sequence and full reflection beyond finite retained data. |
| Reflected super-Gaussian, smooth-shape and positive-primitive controls | Canonical integer-square/Dirichlet arithmetic of the complete arm. |
| Atomic, exact finite-profile and compact continuous profile controls | Full theta coefficients/profile rather than finitely many observations. |
| RH-conditional normalized endpoint controls | Ordinary Dirichlet-series arithmetic of unmodified theta. |
| Fixed-amplitude variable-kernel controls | Actual cosine oscillator/Newman operator. |
| Relaxed positive-measure profiles | An actual integer zero configuration identified with the full physical field. |
| RSCT calibrated multiplicative models | Actual common height trajectory beyond calibrated data and full Green-window law. |

The four-family comparison and reflection rigidity keep their conjunction
and domain qualifications. An isolated collision is not contradicted by
an asymptotic mean alone. No collision is moved into the present time
band and no witness is numerically retested. The quadratic screen in
Section4 is an additional reduced-phase test, not a new physical control.

[Review14][review] checks the identities, the allowance's precisely
defined class, the source gates and the absence of a new residual claim.
[Record16][record] stores exact fraction checks, version identities and
document checks, not numerical proof. [Note28][return09] gives continuation
and model-change guidance. The [sole register][progress] records B09 as
complete at scoped-test scope. Stop this selected route here; no unrelated
signed-log or persistence program, manuscript integration, height campaign
or E08 is activated.

[b08]: 25_GNP_RS_B08_EXPONENT_PAIR_LOCALIZATION_20261112.md
[return08]: 26_GNP_RS_B08_RETURN_AND_MODEL_CHANGE_20261112.md
[return09]: 28_GNP_RS_B09_RETURN_AND_MODEL_CHANGE_20261112.md
[review]: ../reviews/14_GNP_RS_B09_INTERNAL_ASSESSMENT_20261112.md
[record]: ../numerics/16_GNP_RS_B09_INPUTS_AND_CHECKS_20261112.json
[sources]: ../references/02_GNP_RS_B08_EXPONENT_PAIR_SOURCE_USE_20261112.md
[bw]: https://arxiv.org/pdf/1505.04161v1
[progress]: ../research-progress/01_GNP_RS_RESEARCH_PROGRESS_20261110.md
[results]: ../../../../../result-summaries/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a16]: ../../../../../avoid/16_unchecked_imports_and_novelty_claims.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md

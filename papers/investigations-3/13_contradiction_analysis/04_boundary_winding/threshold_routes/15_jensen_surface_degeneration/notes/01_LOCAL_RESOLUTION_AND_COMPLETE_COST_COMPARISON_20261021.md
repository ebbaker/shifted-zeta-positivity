# Complete local Jensen resolution: compression, a sharper degree bound, and a direct comparison

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual session model **gpt-6-astra (Codex)**,
reasoning effort **max**, verified from the turn metadata.

**Status:** analytic bounds proved below; the stated finite zero counts and
error budgets are interval-certified by the accompanying implementation.
Timing observations are not complexity bounds. Review is a
[same-assistant self-review][review], not independent or specialist review.
No novelty claim is made for the approximation mechanisms.

## 1. Outcome and classification

The opening comparison certifies exactly one zero, counted with multiplicity,
in
\[
D=\{s:|s-c|<r\},\qquad c=-199.79,\quad r=10^{-3},\quad R=199.791.
\tag{1}
\]
The zero is therefore simple; real symmetry makes it real. This is a
bounded verification around a familiar low zero, without assuming RH or
the zero's existence/simplicity. It is not new global coverage.

At approximation-error target \(10^{-9}\), the inherited radial bound E4
gives sufficient odd degree **203,199,427,483**. The local E5 bound below
reduces this to **46,031,859**, a factor exceeding **4,414**. Both calculations
retain only **65 coefficients** and pay the complete omitted tail. Thus
degree is not the number of coefficients that must be acquired for this
local diagnostic. Neither degree is asserted to be the smallest possible.

The declared factor-two speed benefit fails. In the retained 192/256-bit
runs, complete refined Jensen acquisition and certification took about
20.2/21.1 ms, versus 1.17/0.55 ms for direct evaluation. The ratios were
17.2 and 38.5. These are two observations on this implementation and
machine, with variable submillisecond overhead, not a universal efficiency
claim. Central coefficient acquisition dominates.

**Decision:** retain the compression/error result and this faithful finite
diagnostic; stop extending this single-disk, newly acquired coefficient
comparison. Keep the broader route in reserve. A shared-coefficient
multi-window task, different acquisition method, or specified period
observable would require its own benefit target.

Under the [classification rule][a01], this is a finite quantitative
milestone, judged by the displayed resolution, error and cost. The
RH-equivalent topological criterion is inherited and is not new evidence.
Read the [result index][results], [local topology cluster][local],
[avoid index][avoid], [control register][controls], and the warnings about
[scope][a07] and [numerics before the question][a10]. The comparison was
specified in [the contract][contract] before coefficient acquisition;
its precision repair and one E5 refinement are recorded amendments.

## 2. Normalization and full coefficient acquisition

Use the [overview][overview] and [proposal E1--E10][proposal]:
\[
f(s)=\xi(1/2+\sqrt{s})=\sum_{k\ge0}c_ks^k,\quad
c_k=\frac{8\,4^k}{(2k)!}\int_0^\infty u^{2k}\Phi(u)\,du>0,
\]
\[
F_d(s)=\sum_{k=0}^d c_kb_{d,k}s^k,
\quad b_{d,k}=\prod_{j=0}^{k-1}(1-j/d),\quad
H(0,z)=f(-z^2/4)/8,\quad H_z(0,z)=-zf'(-z^2/4)/16.
\tag{2}
\]
The square root denotes the even entire power series. Near (1) the
implementation uses \(\xi(1/2+i\sqrt{-s})\), whose square root is analytic
on the evaluation box. It does not cross the negative-axis square-root
branch cut. For positive radii it uses \(\xi(1/2+\sqrt{s})\).

Conventional zeta height is \(\gamma=z/2=\sqrt{-s}\). The real interval
associated with (1) is contained in the following outward-rounded intervals:
\[
14.1346736785820<\gamma<14.1347444264126,
\quad 28.2693473571640<z<28.2694888528252.
\tag{3}
\]
This computation alone does not certify that the enclosed zero is the
first zero; no count below the window was performed.

The exact completion
\(\xi(w)=w(w-1)\pi^{-w/2}\Gamma(w/2)\zeta(w)/2\)
is evaluated with python-flint 0.9.0 / FLINT 3.6.0 ball power series.
Taylor coefficients through order 128 at \(w=1/2\) give \(c_0,\ldots,c_{64}\).
This encloses the complete moments by (2); no finite theta-mode sum or
unpaid source tail is substituted. The rigorous special-function library
is a trusted numerical input. Its [series API documentation][flintdoc]
describes the gamma and zeta series used here.

A naive 192-bit central series returned a weighted coefficient-radius
budget about \(5.56\times10^{136}\), which fails. Cancellation of the
completion's apparent singularities makes this coefficient computation
ill-conditioned at that precision. The repaired acquisition uses 1024
and 1088 working bits respectively, then rounds to 192 and 256 consumer
bits. Actual returned balls, not an assumed precision rule, pay the error:
\[
\sum_{k=0}^{64}\operatorname{rad}(c_k)R^k
 <7.65\times10^{-57}\quad(192\text{-bit consumer}),
\tag{4}
\]
and below \(4.15\times10^{-76}\) at 256 bits. All retained coefficients
are proved positive by their balls. Arithmetic during evaluation is also
performed in balls and included in the certificate. Equation (4) is
reported separately, not subtracted a second time.

## 3. Compression with a complete tail

Let \(f=\sum c_ks^k\) have nonnegative coefficients and be entire. For
\(d\ge K\), put
\[
P_{d,K}(s)=\sum_{k=0}^{K}c_kb_{d,k}s^k.
\]
If \(\rho>R>0\), then on \(|s|\le R\),
\[
|F_d(s)-P_{d,K}(s)|
\le \sum_{k>K}c_kR^k
\le (R/\rho)^{K+1}f(\rho)=:\tau_K.
\tag{5}
\]
The first step uses \(0\le b_{d,k}\le1\); the second uses
\((R/\rho)^k\le(R/\rho)^{K+1}\). This includes every omitted term,
independently of how large \(d\) is. The same \(\tau_K\) bounds the
ordinary Taylor tail of \(T_K=\sum_{k=0}^Kc_ks^k\).

For \(\rho=2R\), \(K\ge2\), a complete second-derivative tail bound is
\[
|f''(s)-T_K''(s)|
\le \frac{K(K+1)}{R^2}\,2^{-(K+1)}f(2R)=:\tau_{K,2}.
\tag{6}
\]
Indeed \(k(k-1)2^{-k}\) is nonincreasing for \(k\ge3\); its successive
ratio is \((k+1)/(2(k-1))\le1\). Apply the maximum at \(k=K+1\)
to each term \(c_k(2R)^k\). This proof controls the differentiated
infinite tail, not just the finite prefix.

At the prescribed window, rigorous full values give
\[
f(2R)=1017.6680364216867785\ldots,\quad
\tau_{64}<2.759\times10^{-17},\quad
\tau_{64,2}<2.875\times10^{-18}.
\tag{7}
\]
We have not constructed a degree-\(d\) coefficient array or computed all
its roots, homology or periods. Under RH the two odd-degree surfaces
would have genera 101,599,713,741 and 23,015,929, respectively; the local
certificate does not itself establish their global squarefreeness or
topology. Local evaluation and full surface construction are different costs.

## 4. A locally paid E5 bound

On \(D\), the line segment from \(c\) to \(s\) stays in \(|s|\le R\).
Consequently (6) gives
\[
|f''(s)|\le |T_K''(c)|+rT_K'''(R)+\tau_{K,2}=:L_2.
\tag{8}
\]
The last derivative is an absolute majorant because the coefficients are
nonnegative. The signed value \(T_K''(c)\) is evaluated before taking its
absolute value. No unknown zero derivative or cofactor floor is assumed.

For reference, the inherited full-series calculation is
\[
|F_d-f|\le A_R/d,\qquad A_R=R^2f''(R)/2,
\tag{9}
\]
\[
F_d=f-\frac{s^2}{2d}f''+\mathcal R_d,\qquad
|\mathcal R_d|\le C_R/d^2,
\quad C_R=\frac{R^4f^{(4)}(R)+4R^3f^{(3)}(R)+2R^2f''(R)}8.
\tag{10}
\]
To audit the remainder, write \(q=k(k-1)/(2d)\). For \(k\le d\),
the product inequalities give \(0\le1-b_{d,k}\le q\) and
\(0\le b_{d,k}-1+q\le q^2/2\). For \(k>d\), use \(b_{d,k}=0\),
\(q\ge1\), and \(q-1\le q^2/2\). Summing with positive coefficients
and using \(k^2(k-1)^2=(k)_4+4(k)_3+2(k)_2\) gives (9)--(10), including
the whole omitted series. The bounds do not require RH.

Combining (8) and (10) gives the useful local refinement
\[
\sup_D|F_d-f|\le B_D/d+C_R/d^2,
\qquad B_D=R^2L_2/2.
\tag{11}
\]
For a prescribed error \(\epsilon>0\), a sufficient degree is
\[
d\ge \frac{B_D+\sqrt{B_D^2+4\epsilon C_R}}{2\epsilon}.
\tag{12}
\]
Use upper ball endpoints, round upward to an odd integer, then verify
(11) directly with that integer. This is a sufficient degree for this
envelope, not a lower bound on what other estimates or actual zeros need.

Here the full enclosures give
\[
\begin{aligned}
A_R&=203.1994274827958437\ldots,\\
L_2&<2.304891\times10^{-6},\\
B_D&=0.04600152430934744835\ldots,\\
C_R&=1396.292382807387366\ldots.
\end{aligned}
\tag{13}
\]
With \(\epsilon=10^{-9}\), (9) chooses \(d=203199427483\), while
(12) chooses \(d=46031859\). The refined error is below \(10^{-9}\)
at both consumer precisions. At the refined degree, the old E4 envelope
is about \(4.4143\times10^{-6}\), so the improvement is in the estimate,
not in extra working precision or a changed error target.

## 5. Finite zero-count certificate and matched direct reference

For a polynomial \(P\), let \(M_{2,P}\) bound \(|P''|\) on the disk.
If
\[
\mu_P=|P'(c)|r-|P(c)|-M_{2,P}r^2/2>0,
\tag{14}
\]
Rouche's theorem compares \(P\) with \(P'(c)(s-c)\) and gives exactly
one zero, counted with multiplicity. With \(P=P_{d,64}\), we use
\[
M_{2,P}=\sum_{k=2}^{64}k(k-1)c_kb_{d,k}R^{k-2}.
\]
If \(\mu_P-\tau_{64}>0\), the full \(F_d\) has the same count. If
\(\mu_P-\tau_{64}-\epsilon_d>0\), so does \(f\), where
\(\epsilon_d\) is (9) or (11). These comparisons use enclosures for
the exact coefficients; no approximate root finder supplies a premise.

The direct comparator applies (14) to \(f\) itself, acquiring
\(f(c),f'(c)\) and a bound for \(f''\) on the square
\(c+[-r,r]+i[-r,r]\), which contains the disk. It uses the same complete
xi implementation and normalization. The local second-derivative bound
is part of its charged certification cost. Its center data are
\[
f(c)=2.22470419621061438\ldots\times10^{-8},\qquad
f'(c)=4.89131001604421519\ldots\times10^{-5}.
\]

| Certificate | Paid boundary surplus, conservative lower bound | Count |
| --- | ---: | ---: |
| Direct complete xi jets | \(2.66649\times10^{-8}\) | 1 zero of f |
| E4 plus 65 coefficients | \(2.05756\times10^{-8}\) | 1 each for P, F_d, f |
| Local E5 plus 65 coefficients | \(2.14981\times10^{-8}\) | 1 each for P, F_d, f |

The table's last two surpluses include both approximation and omitted-tail
payments. Every inequality is strict at 192 and 256 bits. Reality and
uniqueness imply a real root, and the multiplicity-counted value one implies
simplicity. No local derivative floor is guessed from a known zero.

## 6. Cost and the limited decision it supports

| Method | 192-bit elapsed time | 256-bit elapsed time | Complete acquisitions |
| --- | ---: | ---: | --- |
| Direct | 1.174 ms | 0.547 ms | xi series of lengths 2 and 3 |
| Radial E4 Jensen | 21.134 ms | 20.943 ms | lengths 129, 3, 1 |
| Local E5 Jensen | 20.205 ms | 21.075 ms | lengths 129, 5, 1 |

Each Jensen run reacquires its coefficients at 1024/1088 bits, acquires
the full positive-radius values at consumer precision, and performs the
certificate. Its 65 coefficients are not borrowed from the direct
reference. Common imports and process startup are excluded from all
timings. Control execution and the failed preliminary precision probe
are not in these method timings; they are research-development work.
Each row is one execution per precision. The [record][record] retains
unrounded elapsed times, versions, parameters, margins and script hash.

Coefficient acquisition accounts for about 19--21 ms. A claimed saving
obtained by omitting it would answer a different amortized question.
Conversely, this test does not exclude such a question: a common prefix
could be reused across multiple disks or degrees. The present evidence
does not measure that regime, optimal precision, minimal prefix length,
alternative moment integration, or a period consumer. It establishes
failure of the chosen speed gate for this complete implementation only.

## 7. Controls and multiplicity interpretation

The exact finite control \(f=(1+s)^2\) retains
\[
F_d=1+2s+(1-1/d)s^2,\quad
\operatorname{gap}^2=\frac{4d}{(d-1)^2},\quad
\sqrt d\,\operatorname{gap}=\frac{2d}{d-1}.
\]
The script checks the discriminant/gap identities exactly at degrees 65
and 1,000,001. The limiting zero remains double.

The more faithful control
\[
f_*(s)=(1+s)\frac{\sinh(\pi\sqrt s)}{\pi\sqrt s}
\]
has infinitely many negative zeros and a double at -1. Its coefficients
are enclosed from the explicit factorial formula. At \(d=1000001\),
the full Jensen polynomial has exactly two zeros in \(|s+1|<0.01\).
To certify this, compare \(f_*\) with \((s+1)^2/2\), paying the
complete local third-derivative remainder and E4. The paid outer
surplus is greater than \(4.1\times10^{-5}\).

Using (5) and (14), there is exactly one simple Jensen root in each
disk of radius \(10^{-5}\) centered at -1.001 and -0.999, with surpluses
greater than \(9.03\times10^{-9}\) and \(9.05\times10^{-9}\).
Neither small disk contains a zero of the limiting \(f_*\); its double
is at -1. This explicitly tests why finite simple branch points do not
prove limiting simplicity. The earlier attempted outer radius 0.1 was
inconclusive for the interval third-derivative enclosure; the final
radius 0.01 is recorded in the contract. No theta window was changed.

The [collision register][controls] is an analytic premise screen here,
not a claim to have rerun every heat-flow certificate:

| Control family | Missing premise for a theta-specific conclusion |
| --- | --- |
| Quadratic and infinite-product Jensen doubles | The unchanged complete theta coefficients; the quadratic additionally lacks the infinite product. Neither is asserted to be a positive theta heat source. |
| Euler-factor controls | The unchanged arithmetic factor/coefficient data; all-real claims depend on the stated parameter regime. |
| Weighted-square and finite-prime controls | Full normalized reflection and unchanged coefficients; finite-source controls have no all-real heat slice. |
| Reflected super-Gaussian, smooth-shape and positive-primitive controls | The canonical normalized integer-square theta expansion; their different preservation lists are not combined. |
| Atomic and finite-profile threshold controls | The unchanged theta source, full profile growth and eventual simplicity assumptions at the threshold. |
| RH-conditional close-source endpoint controls | Ordinary Dirichlet-series arithmetic; their added endpoint doubles escape in height. |

The generic compression and Rouche implications require no arithmetic
discriminator and therefore do not exclude these controls globally. A
control may pass a finite disk certificate away from its collision.
Its heat event must not be substituted for the Jensen degree parameter.
Only the two Jensen controls above receive new numerical checks here.

## 8. Continuation gate and provenance

JSD-01 and the one-window JSD-02 budget are complete. JSD-03 has a
simple-root finite certificate and a double-control certificate, not
effective double/triple enclosures for a hypothetical theta event.
JSD-04 records a failed complete speed comparison and the 4,414-fold
improvement in sufficient degree. JSD-05 remains gated. HMC-05 stays
open and HMC-06 remains gated.

The next proposal must specify a benefit outside the tested single-disk,
fresh-acquisition comparison before more coefficients are acquired.
Possible distinct questions are amortization across an explicit set of
windows or a specified degeneration observable unavailable from direct
jets. Neither is authorized here as an unbounded numerical campaign.

For literature context, [O'Sullivan][osullivan] uses the same entire
function and central coefficients; [Griffin--Ono--Rolen--Zagier][gorz]
study fixed degree with increasing coefficient shift. This note keeps
that limit separate from unshifted degree growth. No all-multiplicity
asymptotic is inferred from E5.

See the [progress register][progress], [replay code][code],
[small execution record][record], and [chat archive][history].

[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a10]: ../../../../../../../avoid/10_numerics_ahead_of_the_question.md
[avoid]: ../../../../../../../avoid/README.md
[code]: ../numerics/check_local_jensen_resolution.py
[contract]: ../numerics/01_RESOLUTION_COMPARISON_CONTRACT_20261021.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[flintdoc]: https://python-flint.readthedocs.io/en/latest/acb_series.html
[gorz]: https://arxiv.org/html/1902.07321
[history]: ../chat-histories/README.md
[local]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[osullivan]: https://arxiv.org/html/2007.13582
[overview]: ../research-overview/01_JENSEN_SURFACE_DEGENERATION_PROGRAM_20261021.md
[progress]: ../research-progress/01_JENSEN_SURFACE_DEGENERATION_PROGRESS_20261021.md
[proposal]: ../../10_rh_implies_simple_zeros/brainstorm/04_GLOBAL_HEAT_GEOMETRY_PROPOSALS_AND_INITIAL_SCREENS_20261021.md
[record]: ../numerics/JSD_RESOLUTION_COMPARISON_20261021.json
[results]: ../../../../../../../result-summaries/README.md
[review]: ../reviews/01_LOCAL_RESOLUTION_SELF_REVIEW_20261021.md

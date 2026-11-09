# B10 r1: Gaussian pair contraction and the remaining source estimate

9 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. OC chat0009, thread
`01a1c107-0ed3-7fd1-bb46-0b6df66bd6bb`.
Current thread metadata records `gpt-6-astra`, effort `max`;
the history adapter exposes no per-turn configuration. These are recorded
thread settings, not independently verified backend provenance. Root is
the sole writer; no delegation or model change.

**Disposition: B10 r1 complete at scoped missing-input/decision scope.**
Two candidates and one focused analytical clarification. The exact
projection, error implications and local lower bound below are **proved
in-note, proof-author checked**. No canonical value, useful joint theta
estimate, complexity advantage or collision bound was acquired. No new
execution packet is issued. This does not close the investigation.

Read the [result index][results] and [avoid index][avoid], especially
[theta14][theta], [geometry13][geometry], [controls12][controls],
[classification01][a01], [premises02][a02], [scope07][a07] and
[volume20][a20]. Classification: exact contraction and conditional error
bookkeeping, with a scoped small-value obstruction for one absolute
approximation method. Neither observable below is an RH-equivalent
criterion. The numerical target is an absolute error of \(1/100\);
it has **not** been attained. The formulas are supporting results,
not progress on an unmeasured canonical sign.

## 1. Regime and the full-pair candidate

Use exactly [Note18][n18]: complete \(H_0\), \(X\) uniform on \([T,2T]\),
fixed finite \(T\ge10\), \(h=1\),
\[
 W_X(x+iy)=e^{-(x-X)^2/2}\kappa_0(y),\quad
 \ell=\min(1,4\pi/\log T),\quad \epsilon=\ell/4,\quad J=\ell^2.
\]
Keep its labelled \(f_{X,u},r_X,d_X,R_{2,X}\) and both imaginary marks.
Let \(B=B_0(2T)\), \(b_R=B_R(2T)\) be Note18 (5), and
\(a_0=J/(2\pi\epsilon^2)=8/\pi\). The parent constant \(A\) inside
these bounds is finite but has no recorded numerical value here.

Choose the fixed quintic cutoff \(\chi_R(s)\): 1 for \(|s|\le R\),
\(p(|s|-R)\) for \(R<|s|<R+1\), 0 otherwise, where
\(p(t)=1-10t^3+15t^4-6t^5\), and \(R\ge1\) is integral.
Superscript \(R\) multiplies each zero's weight by \(\chi_R(x-X)\).
Then
\[
 \|\overline R_2-\overline R_2^R\|_{\infty,Q^2}
 \le2a_0^2Bb_R,\qquad
 \|C-C^R\|_{\infty,Q^2}\le4a_0^2Bb_R.                 \tag{1}
\]
A discarded ordered pair has at least one weight deficit in
\(|x-X|\ge R\); bounding each other weight sum by \(B\) proves (1).
The connected bound pays the additional product of first means.
This is a smooth cutoff, not deletion of a source boundary term.

For \(L_X(\xi)=\log|H_0(X+\xi)|\), define
\[
 K^R_u=(2\pi)^{-1}\Delta_\xi f^R_{X,u}(X+\xi),\quad
 D^R_{u,v}=(2\pi)^{-1}\Delta_\xi
            [f^R_{X,u}(X+\xi)f^R_{X,v}(X+\xi)] .
\]
These kernels are independent of \(X\). The raw pair is
\[
 \overline R_2^R(u,v)=
 \iint K^R_u(\xi)K^R_v(\omega)\,
       \mathbb E_X[L_X(\xi)L_X(\omega)]\,dA\xi dA\omega
 -\int D^R_{u,v}(\xi)\mathbb E_XL_X(\xi)\,dA\xi.       \tag{2}
\]
The connected version uses the same-center log covariance in the
double integral. The self kernel contains \(\chi_R^2W_X^2\).
Note18's stripwise log bound supplies uniform absolute integrability;
at finite \(R\) the tests are compact. No pointwise bound on a log
product at a zero is used.

For comparison on this **same Gaussian observable**, suppose an
approximation to \(L_X\) has uniform local \(L^1\) error \(E_R\).
Put
\[
 g_F=\sup_{u,\xi}|K^R_u(\xi)|,\quad
 v_F=\sup_{u,v,\xi}|D^R_{u,v}(\xi)|,\quad
 d_F=g_FE_R,\quad e_F=v_FE_R,\quad R_G=a_0B.
\]
Product telescoping gives the direct B06-style transfer allowances
\[
 E_{\rm raw}\le2R_Gd_F+d_F^2+e_F,\qquad
 E_{\rm conn}\le4R_Gd_F+2d_F^2+e_F.                  \tag{3}
\]
Thus a proposed source shortcut must beat a *paid* direct contraction
of (2), including (1) and the acquisition error, on the same target.
Note18's exact center integral simplifies a sum over an already supplied
divisor. Its linear heat shift does not estimate (2).
**Candidate one has no acquired new joint input or demonstrated saving.**

## 2. One marked separation projection, with the blur integrated exactly

For candidate two choose the single bounded smooth observation test
\[
 \Psi(u,v)=
 \exp[-(\Re u-\Re v)^2/2]\,
 \exp[-(\Im u-1/2)^2/2]\,
 \exp[-(\Im v+1/2)^2/2],\qquad 0<\Psi\le1.
\]
Define the scalar
\[
 P_T=\mathbb E_X\int_{\mathbb C^2}\Psi(u,v)
                   R_{2,X}(u,v)\,dAu\,dAv .        \tag{4}
\]
**Declared projection:** integrate the observation midpoint over the
whole plane and retain two separately centered transverse test factors.
This uses the full Gaussian mixtures, not just their restriction to
\(Q^2\); no bound on \(Q^2\) alone evaluates (4). The retained blur is
still \(\tau=\epsilon/\ell=1/4\). There is no observation-tail deletion
and no assertion that (4) reconstructs the full pair.

Write \(z_j=x_j+iy_j\), \(d_{jk}=x_j-x_k\), and
\[
 c_G=\frac{32\sqrt2}{51},\qquad
 b_\pm(y)=\exp\!\left[-\frac8{17}(y/\ell\mp1/2)^2\right].
\]
A direct Gaussian integration gives
\[
 P_T=c_G\,\mathbb E_X\sum_{j\ne k}
 W_X(z_j)W_X(z_k)
 e^{-4d_{jk}^2/(9\ell^2)}b_+(y_j)b_-(y_k).           \tag{5}
\]
Indeed a blurred difference has variance \(2\tau^2=1/8\);
each blurred transverse coordinate has variance \(\tau^2=1/16\).
The three convolution factors are respectively
\((1+2\tau^2)^{-1/2}\) and two copies of
\((1+\tau^2)^{-1/2}\), whose product is \(c_G\).
The Jacobian \(J\) makes each unweighted observation Gaussian have
mass one in \(u\), so there is no further power of \(\ell\).

Set \(m_{jk}=(x_j+x_k)/2\) and
\[
 I_T(m)=\frac{\sqrt\pi}{2T}
       [\operatorname{erf}(2T-m)-\operatorname{erf}(T-m)].
\]
All canonical zeros have \(\kappa_0(y_j)=1\). Note18's exact center
integration now yields
\[
 P_T=c_G\sum_{j\ne k}I_T(m_{jk})
 e^{-[1/4+4/(9\ell^2)]d_{jk}^2}b_+(y_j)b_-(y_k).    \tag{6}
\]
Both edges of the center interval and all zero labels remain.
Tonelli applies to (4)–(6), and \(P_T\le c_GB^2\).
This is an exact reduction in integration, not a canonical evaluation.

The label self subtraction, before center integration, is precisely
\[
 S_X=\sum_j W_X(z_j)^2b_+(y_j)b_-(y_j)
    =e^{-4/17}\sum_jW_X(z_j)^2
                     e^{-16y_j^2/(17\ell^2)}.       \tag{7}
\]
It is subtracted with coefficient \(c_G\). At an \(m\)-fold zero
the raw \(m^2\) contribution becomes \(m(m-1)\), not zero.

Relative to the declared *blurred* statistic, the convolution bias is
zero. If one instead asks for the unblurred test on the zero locations,
the heat-semigroup bound gives
\[
 |P_T-P_T^{\rm unblurred}|\le 2\tau^2 B^2=B^2/8.     \tag{8}
\]
To check it, \(\Delta_{\mathbb R^4}\Psi
=2\Psi_{ss}+\Psi_{aa}+\Psi_{bb}\) in separation/mark coordinates,
with each displayed second derivative at most 1 in absolute value.
Integrate the heat generator for time \(\tau^2/2\).
This coarse allowance is not silently charged as a small \(1/100\) error.

## 3. The projected source contraction and a complete error ledger

The normalized frequency density
\[
 \rho_\ell(k)=\frac{3\ell}{4\sqrt\pi}
                  e^{-9\ell^2k^2/16}
\]
has Fourier transform \(e^{-4d^2/(9\ell^2)}\).
With the same smooth cutoff as in §1 put
\[
 A^R_{X,\pm}(k)=\sum_j\chi_R(x_j-X)W_X(z_j)b_\pm(y_j)
                              e^{ik(x_j-X)},\quad
 S_X^R=\sum_j\chi_R(x_j-X)^2W_X(z_j)^2b_+(y_j)b_-(y_j).
\]
Then, with \(M_R(k)=\mathbb E_X[A^R_{X,+}(k)A^R_{X,-}(-k)]\)
and \(\overline S_R=\mathbb E_XS_X^R\),
\[
 P_T^R=c_G\left[\int_{\mathbb R}\rho_\ell(k)M_R(k)\,dk
                         -\overline S_R\right].    \tag{9}
\]
The two factors have the **same X**. Canonical conjugation makes
\(A^R_{X,+}(k)=A^R_{X,-}(k)\), so \(M_R(k)=\mathbb E|A^R_{X,+}(k)|^2\).
It does not replace (7) by \(\sum_j(\chi_RW_Xb_+)^2\).
Positivity of this raw second moment is generic and gives no numerical
value for its self-subtracted contraction.

This has a concrete source expression. For
\[
 F^R_{\pm,k}(\xi)=\chi_R(\Re\xi)e^{-(\Re\xi)^2/2}
           \kappa_0(\Im\xi)b_\pm(\Im\xi)e^{ik\Re\xi},\quad
 V^R(\xi)=\chi_R^2 e^{-(\Re\xi)^2}\kappa_0^2b_+b_-,
\]
the distributional identities are
\[
 A^R_{X,\pm}(k)=\frac1{2\pi}\int L_X\Delta F^R_{\pm,k}\,dA,\qquad
 S_X^R=\frac1{2\pi}\int L_X\Delta V^R\,dA.            \tag{10}
\]
Thus the projected route needs a contraction of the same joint log field,
with one frequency variable. It does not require the entire B06 moment
array, but no estimate of this smaller contraction has been acquired.

All truncations admit explicit allowances:
\[
 E_{\rm space}\le2c_GBb_R,\qquad
 E_{\rm freq}\le c_GB^2\operatorname{erfc}(3\ell K/4). \tag{11}
\]
For the first, telescope the two label weights in (5).
For the second, use \(|A^R_\pm|\le B\) and truncate only the \(M_R\)
integral in (9); **keep the entire self term**. Its coefficient is not
multiplied by the truncated frequency mass. Consequently no additional
self-term frequency tail is missing.

There is also a finite expression bounding the series \(b_R\). With
\(L=\log(2+2T)\), \(q_R=e^{-(R+1/2)}\), Note18 (5) implies
\[
 b_R\le2Ae^{-R^2/2}
 \left[\frac{L+\log(R+2)}{1-q_R}
       +\frac{q_R}{(R+2)(1-q_R)^2}\right].           \tag{12}
\]
Use \(n=R+j\), \(j^2\ge j\) and
\(\log(R+j+2)\le\log(R+2)+j/(R+2)\), then sum two geometric series.
The same formula at \(R=0\) bounds \(B\). This pays the summation tail
in terms of the inherited \(A\), without pretending that \(A\) was measured.

For any approximate log field on
\(\Omega_R=[-R-1,R+1]\times[-2,2]\), let
\[
 E_R=\sup_X\int_{\Omega_R}|L_X-\widehat L_X|\,dA,\quad
 g=\sup_{\pm,|k|\le K,\xi}\frac{|\Delta F^R_{\pm,k}|}{2\pi},
 \quad v=\sup_\xi\frac{|\Delta V^R|}{2\pi},\quad
 d=gE_R,\ e=vE_R.
\]
These derivative suprema concern explicitly fixed compact \(C^2\)
functions. Replacing \(L\) in (10) gives \(\widehat M_R,\widehat S_R\);
product telescoping proves
\[
 E_{\rm source}\le c_G(2Bd+d^2+e).                  \tag{13}
\]
If numerical or arithmetic estimates \(\widetilde M,\widetilde S\)
are supplied, the remaining error is bounded by
\[
 E_{\rm joint}=c_G\left[
 \int_{-K}^K\rho_\ell(k)|\widehat M_R(k)-\widetilde M(k)|\,dk
                 +|\widehat S_R-\widetilde S|\right].        \tag{14}
\]
Combining (11), (13), (14) bounds the error of
\(c_G[\int_{-K}^K\rho_\ell\widetilde M-\widetilde S]\) for (4).

**Exact missing estimate.** For example at the explicit finite comparison
height \(T=1000\), obtain (14) with error at most \(1/400\), with a named
acquisition method, while each of \(E_{\rm space},E_{\rm freq},
E_{\rm source}\) is at most \(1/400\). This would give a canonical
\(P_{1000}\) enclosure of radius at most \(1/100\).
These are absolute errors of a projected weighted count, not the units
of a full-profile sup norm; equal tolerances do not establish equal costs.
No \(R,K,A\) values or work-feasible log approximation have been frozen.
In particular (14) is a missing-input specification, **not** an E request.

Equations (9)–(12) use the complete source, so no arithmetic/radial source
terms have been dropped. If \(\widehat L\) is constructed from a finite
theta source, both tails and enlarged-domain bounds must first give
uniform field accuracy and an anchor; [Note02][n02] then pays its log
error. B06's compact-support constants cannot simply be assigned to
\(\Omega_R\). One must cover it by valid anchored disks, sum their
\(L^1\) allowances and retain cutoff derivatives. Polynomial log
regularization on each normalized disk adds its B06
\(\beta M^{-1/n}\) remainder. Those costs belong in \(E_R\), and any
source quadrature/remainder used to acquire (14) is charged there or in
(14), never omitted. No such approximation or numerical campaign was
performed in r1. Exact-log access sets \(E_R=0\) but leaves (14) unpaid.

## 4. Single focused clarification: does Gaussian weighting improve the small-value rate?

Not by itself for the positive absolute log-error method. For integer
\(m\ge1\) let \(f(z)=(z/a)^m\) on \(|z|\le a\), and use B06's polynomial
\[
 P_M(t)=-\tfrac12\sum_{j=1}^M(1-t)^j/j,\quad
 R_M(z)=P_M(|f(z)|^2)-\log|f(z)|\ge0 .
\]
If a positive continuous weight \(w\) is at least \(w_0>0\) on that disk,
then
\[
 \int_{|z|\le a}w(z)R_M(z)\,dA
 \ \ge\ \frac{\pi w_0a^2}{8}(4M)^{-1/m},\qquad M\ge1.       \tag{15}
\]
Proof: on \(|z|\le a(4M)^{-1/(2m)}\), \(t=|f|^2\le1/(4M)\).
For \(M<j\le2M\), Bernoulli gives \((1-t)^j\ge1/2\), and
\(\sum_{j=M+1}^{2M}1/j\ge1/2\).
The positive remainder series is therefore at least \(1/8\) there.
Integrate over this disk. A fixed Gaussian is such a weight.

This is an **absolute-remainder lower bound for the stated normalized
local monomial and positive weights**. It neither proves a lower bound
on a signed Laplacian contraction nor shows B06's conservative Jensen
parameter \(n\) equals an actual zero multiplicity. It establishes no
canonical multiple zero, and no complexity lower bound for other
approximations, cancellations, contours or root-based evaluation.
Improving the inherited rate requires additional information or a
different paid approximation, not merely the Gaussian weight.
Note18's polynomial heat example separately already prevents moving a
logarithm through its linear Gaussian time shift.

## 5. Inspected arithmetic input and the control screen

The existing [BGST v3 §3][bgst] gives a dyadic complex-difference
transform with a particular analytic weight and corrected asymptotic
error. Its stated transform does not supply (2) or (14). This is a
comparison of the inspected theorem, not a claim about everything
obtainable from its methods. Its height variable converts by \(x=2\gamma\)
(with conjugation as in B06), so our comparison height would be \(T/2\).
No new theorem is imported.

In (6), the center-edge factor depends on the midpoint. In addition,
even for \(d=0\), two equal marks \(y_j=y_k=a\) contribute
\(b_+(a)b_-(a)=e^{-16a^2/(17\ell^2)-4/17}\), which varies while the
complex difference remains zero. Hence this **pair kernel** is not
just a function of the complex difference. This elementary information
screen does not construct a competing zeta divisor. Integrating the
observation midpoint has not made either issue disappear.

Analytical collision controls were applied at premise level; the
original numerical collision certificates were not rerun:

| Control class | Canonical premise absent, and what survives |
| --- | --- |
| Euler-factor | Complete unmodified theta coefficients/completion fail; Gaussian convolution and factorial algebra survive on a paid divisor. |
| Weighted-square / finite-tail | Full normalized reflection and complete unit coefficients fail; no canonical strip/count constants are transferred. Local Gaussian and log calculations survive where their hypotheses hold. |
| Reflected super-Gaussian / smooth shape / positive primitive | Complete arithmetic theta square expansion fails. Positivity and smoothness do not acquire (14). |
| Finite-prime orbit | Full reflection/all-coefficient identity fails despite the selected finite relations. |
| Atomic / finite-profile threshold | Complete theta profile and growth fail; eventual simplicity of the canonical family is not needed for the snapshot formulas. |
| RH-conditional theta-close endpoint | Ordinary Dirichlet-series arithmetic fails; the Gaussian pair statistic remains compatible with its double labels. |
| Variable observation kernel | Literal physical cosine/Newman equation fails. The snapshot algebra itself does not use heat evolution and need not reject it. |
| Fractional-profile relaxation | Integer labelled-divisor realizability fails, so its factorial self rule cannot be assigned to actual zero labels. |

No missing premise in this table is itself a favorable theta estimate.
All controls satisfying a formula's actual hypotheses must satisfy that
formula, including at collisions. For a real double at \(x=c\), the local
ordered-pair contribution to (6) is
\(2c_G I_T(c)e^{-4/17}>0\); there is no implicit simplicity inference.

## 6. Decision and continuation

| Candidate | Return | Decision |
| --- | --- | --- |
| Full marked joint-log contraction | Same-center kernels and direct transfer (1)–(3); no additional canonical joint estimate | Park Gaussian algebra as a source shortcut. No saving established. |
| One marked separation projection | Exact blur/center reduction (5)–(10), tails (11)–(12), explicit missing contraction (14) | Retain as a precise smaller target; do not count it as an acquired theta estimate or ready evaluator. |

B10 r1 ends at the exact missing input, as permitted by Plan02.
No third route, numerical implementation, manuscript edit or automatic
r2 is authorized by this result. The independent marginal investigation
remains open; B06/E08 and compact-window E10/E12 keep their scopes.

For an analytical continuation, **[B] TND-OC-B10 r2 — GPT-6 Astra** is
conditional on a named additional source mechanism capable of paying
(14), or the corresponding full contraction. Begin by testing that input
against the existing budgets; stop if it only repackages B06 moments,
B09 Laplace transforms or the linear heat shift. Recommend Sol only
after an executable acquisition method and finite work limit are fixed.
If finite canonical values are the objective now, **[E] TND-OC-E09 —
GPT-6.1 Sol** remains a ready *optional compact-window benchmark*, using
its unchanged packet; it does not evaluate (4).

[Self-check15][review] is same-assistant proof-author checking, not a
separate assessment. [Continuation22][cont] and the [sole register][prog]
hold the handoff. No manuscript milestone or investigation closure:
the root result/pattern summaries are not promoted.

[results]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[theta]: ../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[geometry]: ../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a20]: ../../../../../../avoid/20_volume_without_a_gain.md
[n18]: 18_TND_OC_GAUSSIAN_HEIGHT_WINDOW_AND_THETA_SOURCE_20261109.md
[n02]: 02_TND_OC_LOCAL_LOG_TRANSFER_20261107.md
[bgst]: https://arxiv.org/html/2501.14545v3#S3
[review]: ../reviews/15_TND_OC_B10_R1_GAUSSIAN_COMPARISON_SELF_CHECK_20261109.md
[cont]: ../continuation-notes/22_TND_OC_AFTER_B10_GAUSSIAN_COMPARISON_AND_MODEL_CHANGE_20261109.md
[prog]: ../research-progress/02_TND_OC_MARGINAL_PRIORITIES_RESEARCH_PROGRESS_20261108.md


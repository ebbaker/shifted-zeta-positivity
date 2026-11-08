# B04: arithmetic reconciliation and the two access routes

8 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance. Authenticated chat0003, thread
01a1bbc2-ac28-71c1-8bf0-aefeb0b06ce8. Actual model/effort are unavailable
in its recorded source. Root is the sole writer; no model switch or
delegation is claimed.

**Disposition:** B04's bounded comparison is complete. Route B yields
an explicit deterministic acquisition estimate for a genuinely
separation-dependent marked test. Neither inspected route supplies a
favorable canonical short-window pair bound. This is a **scoped failure
to acquire that independent value**, not a failure of the pair-marginal
program. New deductions have proof-author checking only, in
[Review04](../reviews/04_TND_OC_B04_AUTHOR_SELF_CHECK_20261108.md).

The task was exactly the two candidates of
[Continuation07](../continuation-notes/07_TND_OC_PAIR_MARGINAL_DIRECTION_AND_LITERATURE_20261108.md)
and [brainstorm Note07](../brainstorm/notes/07_TND_OC_LOCALIZED_PAIR_MARGINAL_LITERATURE_AND_DIRECTION_20261108.md),
with one clarification inside B about deterministic versus distributional
joint accuracy. The author's latest instruction puts new research in
notes/. E02 is accepted; B02 remains author-checked only; E03 is pending
under its unchanged packet. B02's harmonic-distance result is not a
premise here.

Read the [result index](../../../../../../result-summaries/README.md)
and [avoid index](../../../../../../avoid/README.md), especially
[collision screen12](../../../../../../result-summaries/12_collision_controls_and_screening.md),
[classification01](../../../../../../avoid/01_restating_the_target.md),
[scope07](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
and [source-use16](../../../../../../avoid/16_unchecked_imports_and_novelty_claims.md).
The results below are a corrected import, a quantitative approximation
milestone, and a scoped information diagnosis. With complete height and
transverse-scale coverage, exact vanishing of the selected nonnegative
defect tests is another RH reformulation; it is stated here once and
not treated as supported by checks.

## 1. Reconcile the BGST import before using it

Primary source: BGST, *Pair Correlation ... I*, arXiv:2501.14545v3,
section 3, especially (3.2), (3.4)-(3.5). The existing external PDF
receipt was rehashed, the selected text reread, and PDF page 8 visually
checked. [Source-use04](../references/04_TND_OC_PAIR_MARGINAL_LITERATURE_SOURCE_USE_20261108.md)
owns the article/version record. This is a selected-source audit, not a
reproof of the imported prime mean-square theorem.

Write ell=log T, B_T=T ell/(2pi), and reserve r for the source paper's
positive exponential base (its x), avoiding confusion with H-coordinate
x=2 gamma. For I=(0,T] or (T,2T] define
\[
 \mathcal F_I(r)=\sum_{\gamma_j,\gamma_k\in I}
             r^{\rho_j-\rho_k}W(\rho_j-\rho_k),
 \qquad W(u)=4/(4-u^2).
 \tag{A1}
\]
Both sums include all self labels and all multiplicity copies.
For 1<=r<=T, the first line of corrected **cumulative** (3.5) states
\[
 \mathcal F_{(0,T]}(r)=
 \frac{T}{2\pi r^2}\{\ell^2+O(\ell)\}
 +\frac{T}{2\pi}\log r+O(T\sqrt\ell).                         \tag{A2}
\]
Dividing by B_T and taking r=T^alpha gives, uniformly 0<=alpha<=1,
\[
 \frac{\mathcal F_{(0,T]}(T^\alpha)}{B_T}
 =T^{-2\alpha}\{\ell+O(1)\}+\alpha+O(\ell^{-1/2}).            \tag{A3}
\]
**This is exactly the formula currently printed at parent (eq:BGST).**
Its cumulative error therefore survives by the corrected v3 proof.
The earlier warning was necessary, but it must not be read as a
retraction of that displayed formula. Its old v1 attribution should be
replaced by v3 (3.5), first line, at the next parent manuscript edit.

For the **dyadic** band, the stated uniform theorem (3.2) gives
\[
 \frac{\mathcal F_{(T,2T]}(T^\alpha)}{B_T}
 =T^{-2\alpha}\ell+\alpha+
 O(T^{-2\alpha}\sqrt\ell+\ell^{-1/2}).                        \tag{A4}
\]
Use (A4) here, without silently transplanting (A3)'s sharper first
error to a different band. Both statements retain absolute uniform
big-O constants and an uninstantiated onset; they are not finite
certificates. Nonnegativity and evenness remain valid.

The repaired cumulative argument keeps
M_2=T log r+O(T sqrt(ell)), and bounds the mixed A_1/A_2 integral
by O(ell) using its oscillatory integral. These are the relevant
correction and cancellation in the source; a standalone relative
error on the two leading terms is not substituted.

### Bounded dependency check

The direct manuscript references found are in
[section11](../../manuscript/sections/11_complex_statistics.tex)
and [section13](../../manuscript/sections/13_localized_statistics.tex).
The former defines the cumulative population used in (A3). Its
finite-multiset Gram identity, multiplicity counting, and finite-defect
sensitivity arguments are separate finite/count calculations.
The latter explicitly says the theorem supplies neither extended
frequency range nor a moving-window estimate. None of these inspected
conclusions needs a stronger repaired error.

The parent manuscript and issued packets are left byte-unchanged;
the canonical source annotation records this reconciliation.
This completes the import prerequisite for B04, which uses the pinned
v3 directly. It is not a repository-wide reassessment, a journal-version
audit, or a claim that every historical use of BGST was inspected.

**Concurrent source check:** the separately authored
[BGST import review](../reviews/BGST_IMPORT_SOURCE_CHECK_20261108.md)
arrived during this work and agrees on the corrected cumulative formula.
It also checks that pinned older v1 (1.4) already prints the additive
normalized expression. Its chat0004 provenance and source annotations
are preserved. That bounded source assessment is not an assessment of
B04's pair-transfer proof or a verified cross-model review.

## 2. Route A: one fixed analytic test and its complete scale

Choose the fixed frequency weight q(alpha)=(1-|alpha|)_+ on [-1,1],
with integral one. Its entire transform is
\[
 K_T(u)=\int_{-1}^1q(\alpha)e^{\alpha\ell u}\,d\alpha
       =\left(\frac{\sinh(\ell u/2)}{\ell u/2}\right)^2,
 \qquad K_T(0)=1.
 \tag{A5}
\]
The selected arithmetic statistic is the **ordered factorial** sum
\[
 A_T=\frac1{B_T}\sum_{\substack{\rho_j,\rho_k\in\mathcal Z(T)\\j\ne k}}
              W(\rho_j-\rho_k)K_T(\rho_j-\rho_k),
 \quad \mathcal Z(T)=\{\rho:T<\gamma\le2T\}.
 \tag{A6}
\]
No real-zero or simplicity hypothesis is imposed. The self subtraction
is n_T/B_T, n_T=|\mathcal Z(T)|, not all coincident locations.
Each distinct pair of copies at the same geometric zero remains.

Here is an actual independently imported arithmetic value for this
particular projected test. By (A4), evenness, and the unconditional
count n_T=B_T+O(T),
\[
 \begin{split}
 A_T&=2\ell\int_0^1(1-\alpha)T^{-2\alpha}\,d\alpha
          +2\int_0^1(1-\alpha)\alpha\,d\alpha-\frac{n_T}{B_T}
          +O(\ell^{-1/2})\\
 &=1-\frac{1-T^{-2}}{2\ell}+\frac13-\frac{n_T}{B_T}
          +O(\ell^{-1/2})
  =\frac13+O(\ell^{-1/2}).                                  \tag{A7}
 \end{split}
\]
For clarity, if the bound in (A4) is at most
C_BG(T^{-2alpha}sqrt(ell)+ell^{-1/2}) and
|n_T/B_T-1|<=C_N/ell, the error after the main value 1/3 in (A7)
is at most
\[
 2C_{\rm BG}/\sqrt\ell+(C_N+1/2)/\ell.                      \tag{A8}
\]
This follows by integrating both error terms; the frequency-zero spike
is not dropped. The source does not instantiate C_BG,C_N or their
common onset. This calculation is an application of known arithmetic
input, with no novelty claim.

**Window, scales and time.** The law is deterministic, at lambda=0.
The common-height population is the sharp dyadic x-window (2T,4T],
center 3T and half-width T. Its microscopic difference scale is
ell_x=4pi/ell in x=2 gamma, and the associated transverse scale is the
same ell_x. Indeed
\[
 (\rho_j-\rho_k)\ell
 =\frac{\ell}{2}\{-(y_j-y_k)+i(x_j-x_k)\}.
\]
The observable retains a complex difference, not the two separate
transverse marks or an arbitrary common-center weight. It contains no
short-window averaging theorem.

**Defect response versus background.** A simple H conjugate pair
x_*+-id, 0<d<1, has beta difference d and contributes
\[
 \frac{2}{B_T}\frac4{4-d^2}
       \left(\frac{\sinh(d\ell/2)}{d\ell/2}\right)^2           \tag{A9}
\]
from its two ordered mutual terms. For d=c/ell with fixed c, this is
O(1/(T ell)), whereas the paid normalized arithmetic error in (A8)
is of order ell^{-1/2}, and the main pair background is 1/3.
At d=0 two coincident real copies contribute 2/B_T. Moreover the
remaining complex summands need not be nonnegative. Formula (A9) is
a mutual-pair contribution, **not** a lower bound on A_T or on the
change caused by inserting a pair; all cross interactions remain.

The usual real-axis Fejer interpretation holds when the argument is
purely imaginary. Its analytic continuation does not supply positivity
on arbitrary marked configurations. BGST's separate narrow-box
proportion applications retain their narrow-box premise.

**A disposition.** The corrected theorem gives (A7) on its declared
dyadic analytic projection. It supplies neither a short common-center
test nor a favorable absolute single-defect margin. This is a scoped
failure of this import as the requested localized marked consumer,
not an impossibility theorem for localized arithmetic correlations,
other signed kernels, or higher-frequency estimates.

## 3. Route B: choose the marked Poisson separation test

[Note06](06_TND_OC_B04_DETERMINISTIC_MARKED_PAIR_TRANSFER_20261108.md)
fixes the two transverse marks, compact window, scales, multiplicities
and all error terms. Its default is the deterministic center X,
lambda=0, h=b=min(1,4pi/log X), with separation kernel
h^2/((x-x')^2+h^2) and transverse weights v(|y|/b)v(|y'|/b).
It gives the simple-pair signal 2(d/b)^4, at least 1/8 when
b/2<=d<=b on the window plateau, with nonnegative full background.
Real multiple zeros give zero.

The one focused clarification is substantive: accepted E02 supplies
strong, same-disk deterministic log accuracy. Combined with Jensen's
multiplicity count, tensor telescoping gives a pair error without a
new probabilistic joint-law assumption. At matched scales, it is
\[
 E_{\rm pair}=
 \frac{2800n_X+3621/2}{\pi h^2}C_X
          (\delta/M_X)^{2/(n_X+2)},                         \tag{B1}
\]
with all symbols, source tails and cutoff choices fixed in Note06.
The direct log-product identity is also valid, but its straightforward
absolute estimate pays fourth derivatives; (B1) pays only second
derivatives and the bounded zero population.

This answers B04's acquisition question positively at a conditional
precision level. It does **not** answer the favorable-value question:
an independent upper estimate for the finite canonical statistic,
or its combined two-log/diagonal contraction, remains unpaid. One-point
expectations would not determine the joint covariance if centers were
averaged. Merely applying Tao-Vu terminology does not acquire it.

### The Tao-Vu comparison is architectural, not an imported theorem for H

Corrected arXiv:1307.4357v3 Theorems 2.1 and 3.1 were reread, with the
local PDF hash matched. The abstract complex theorem allows dependent
coefficient laws but still requires quantitative nondegeneracy,
non-clustering, and joint smooth-test comparison of log magnitudes
at up to n^{c_0} points. The real version additionally needs the
reference field's real-pair and near-axis complex repulsion bounds.
Its degree-at-most-n setting is not supplied by calling an entire
finite-source integral a polynomial or a local zero count its degree.

The canonical H and its source truncation have no established
Gaussian, determinantal or Pfaffian law. No such law is assumed,
and no density-form Kac-Rice formula is used. The direct deterministic
proof in Note06 needs fewer probabilistic premises because it uses
different, explicitly stronger pointwise approximation data.

### Compare to the RT and HCB predecessors before selecting a consumer

The [RT Note02](../../../../02_heat_flow_rh_applications/rodgers_tao/notes/02_CORRECTED_PROPAGATION_AND_CONTOUR_FORCE_TRANSFER_20261026.md)
and its [assessment](../../../../02_heat_flow_rh_applications/rodgers_tao/reviews/01_PROPAGATION_AND_CONTOUR_TRANSFER_ASSESSMENT_20261026.md)
retain real simple-root energy, same-root exterior error 2 kappa E,
complete unit drift, and corrected boundary payments. They supply no
complex-root energy positivity. B04 selects a fixed time-zero slice,
not transport; extending it in time must pay these missing obligations
and any higher-correlation dependence separately.

The [HCB Note01](../../../../03_heat_flow_collision_bounds/notes/01_WHOLE_CLUSTER_POISSON_TRANSFER_AND_ACQUISITION_20261026.md)
and [Review01](../../../../03_heat_flow_collision_bounds/reviews/01_OPENING_TRANSFER_ASSESSMENT_20261026.md)
give the real-population Poisson pair identity. The unmarked unwindowed
restriction of our separation kernel equals theirs at Poisson height h/2.
Their transfer allows complex *approximant* roots but requires real
*true* roots for its y^n floor and positive tails. It cannot be imported
unchanged for our nonreal true population. The new logarithm transfer
avoids that premise and pays the different disk/log/count costs.
No matched runtime or numeric margin advantage is established.

The [HCB current summary](../../../../03_heat_flow_collision_bounds/summary/CURRENT_SUMMARY.md)
keeps its full signed-lag alternatives open after failures of the
specified physical-jet lag/triangle recipes. Those failures are not
used as obstructions to (B1) or to zero-pair marginals. No stopped
HCB numerical campaign is restarted.

## 4. Averaging and complete quantifiers

The selected B test uses no averaging, so has no dilution payment.
For comparison only, if a single common center U is uniform on an
interval I of length L and [x_*-h,x_*+h] lies inside I, its pair's
averaged mutual contribution is exactly
\[
 2(d/b)^4\,\frac hL\int_{-1}^{1}w(t)^2\,dt.                 \tag{B2}
\]
With a boundary intersection the integral is truncated; an uncovered
pair may give zero. The fixed polynomial window has integral
643/462. Thus long center averaging cannot retain an undiluted 1/8
single-pair margin. This is an exact calibration, not a third route.

The new bound holds for each declared X>=10, 0<h,b<=1 and finite
tail cutoffs satisfying Note06 (13), without exceptional centers.
It is not a single finite approximation for every X. No favorable
canonical upper value has been proved even on the default family.
All-height use would additionally need every transverse band down to
zero, all centers or a paid covering, and any uncovered finite core.

There is no positive-time interval in this contract, no continuation
of the negative-time HDA result through zero, and no Euler product
assigned to H_lambda for lambda>0.

## 5. Collision and information controls

The analytical screen below uses the established repository controls;
their original certificates are not rerun. A test that vanishes on all
real zeros deliberately allows a real collision itself. It detects
the nonreal side of an event when that side lies in its window/band.
No finite-threshold premise is assigned to finite-source controls.

| Control class | Premises retained / distinguishing premise absent |
| --- | --- |
| Euler-factor controls | Generic factorial/log identities and local acquisition survive; unchanged zeta/theta coefficients and canonical conductor/normalization do not. A new favorable inequality would need an actual arithmetic estimate, not just this distinction. |
| Weighted-square / finite-tail controls | Positive square support and local analytic transfer can survive; full normalized source reflection/completion fails. Their local events are not asserted to be finite all-real thresholds. |
| Reflected super-Gaussian | Reflection and Gram positivity survive; full theta integer-square arithmetic is absent. Pair positivity alone is compatible with its nonreal sector. |
| Smooth shape and positive-primitive controls | The named shape, positivity, primitive and asymptotic data survive; complete canonical theta expansion does not. |
| Finite-prime orbit controls | Selected finite identities/measurements survive; full source reflection fails. No finite list alone is credited with (16) of Note06. |
| Fixed-amplitude, variable-kernel controls | Fixed theta amplitude survives; the full cosine oscillator/Newman equation fails. They are not actual cosine-field counterexamples. |
| Atomic threshold / exact finite-profile controls | Their specified finite profiles and complete moment bounds survive; full theta arithmetic/profile growth and eventual threshold simplicity fail. Continuous extensions retain only their stated scope. |
| RH-conditional theta-close endpoint controls | They retain the source/completion properties specified in their own constructions, but fail ordinary Dirichlet-series arithmetic. They test simplicity claims separately from this nonreal-pair target. |
| Actual-profile positive-measure relaxation | It retains the selected profile constraints; integer zero-configuration realizability is absent. It is not a canonical zero set. |

For every row, the generic acquisition is allowed whenever its actual
anchor and disk hypotheses hold. There is no claimed failure of that
estimate. The absent premise names where a future canonical value
argument must do more; absence is not a proof of the desired sign.

An explicit normalized local control checks the inference directly.
For 0<d<=1, in t=z-X put
\[
 f_+(z)=(t^2+d^2)/74,\qquad f_-(z)=(t^2-d^2)/74 .
 \tag{C1}
\]
On the entire disk |z-(X+4i)|<=9/2, |t|<=17/2, so both moduli
are at most ((17/2)^2+1)/74<1. At the safe center both have modulus
at least 15/74, and their uniform distance is d^2/37.
Thus the generic normalized E02 premises hold with a fixed anchor.
Nevertheless f_+ has S=2(d/b)^4 for d<=b, whereas f_- has S=0.
Taking d=b/2 and h=b down to zero leaves S(f_+)=1/8 while the field
distance tends to zero; the derivative payments in (B1) must not be
discarded. These are polynomial controls, not theta perturbations.
The families (t^2+-d^2-2lambda)/74 also satisfy the local heat equation.
This screens an inference from normalized approximation alone, not
any additional source-sensitive signed comparison.

## 6. Decision and exact continuation boundary

| Item | Acquired in B04 | First unpaid input |
| --- | --- | --- |
| A: analytic arithmetic projection | Correct cumulative import and the dyadic Fejer statistic (A7), with (A8) | A genuinely localized marked estimate, with complete background/cross-term and absolute error payment |
| B: deterministic marked pairs | Fixed observable and the complete precision estimate (B1), proved in Note06 | A favorable canonical value or independently justified joint comparison below the one-pair margin |

Retain B as the better *access representation* for the author's
nonreal marked-pair question. It has the right window and marks and
a fully stated acquisition theorem. Do not issue an execution request
whose core is merely “make (17) small.” The two routes are not
parked universally: only their attempted promotion to a favorable
localized law from the inspected inputs fails.

The ready bounded successor is a separate assessment of these fixed
B04 claims, with the source reconciliation, folding factors and
second-derivative constants all frozen. E03 remains the separate
pending B02 assessment and must not be silently expanded.
[Continuation08](../continuation-notes/08_TND_OC_AFTER_B04_AND_MODEL_CHANGE_20261108.md)
gives the model-change guidance and reopening requirements. No canonical
numerical campaign, manuscript snapshot, independent assessment, commit
or push occurred. The investigation remains open.

# B03: real-axis cancellation, real divisors and the missing input

8 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance. Requested configuration: GPT-6 Astra
at the author's selected effort. Actual backend model and effort are not
exposed in this chat's captured source; its `model_configurations` is empty.
Thread `01a1b9b5-ffde-71a3-b103-2fc9a7eeffca`, branch chat0002. One writer;
no model switch or delegation is claimed.

**Task [B] TND-OC-B03: complete at the bounded scoped-failure boundary.**
The two routes below retain real-axis cancellation, but the inspected
accepted inputs do not supply the canonical estimate needed to close
either route in the declared every-center, unbounded-height regime.
The elementary calculations here are **proved in-note; author checking
only**. This is a conceptual selection record, not a separate assessment.
E02 remains accepted; B02 retains proof-author checking only; E03 remains
pending. The [sole register](../../research-progress/01_TND_OC_RESEARCH_PROGRESS_20261107.md)
owns live status. All new mathematics is saved here at the author's request.

| Route | What actually preserves cancellation | First independent information still needed |
| --- | --- | --- |
| A: weighted/directly signed log comparison | Keep the signed Laplacian pairing, or regularize the logarithm and put the original test against its Laplacian | A source-specific bound on the resulting joint small-value/derivative integral, below the pair margin after all errors; E02 supplies acquisition, not this bound |
| B: controlled real-zero divisor | Subtract real logarithmic singularities, whose exact pairing with the test is zero | Certified real multiplicities plus control of the remaining divisor, or an independently constructed real-rooted comparison with a paid residual; a known subset of real zeros is insufficient |

**Decision:** park these two completion attempts on the currently acquired
information. No signed-smallness E successor is issued. A matched total
zero count and certified real-zero count would be an independent finite
input for B, but neither the required data nor a uniform analytic estimate
is acquired here. It is not renamed as a new research gain or numerical plan.

## 1. Contract, classification and unchanged consumer

Read the [result index](../../../../../../../result-summaries/README.md)
and [avoid index](../../../../../../../avoid/README.md), especially
[controls12](../../../../../../../result-summaries/12_collision_controls_and_screening.md),
[target classification](../../../../../../../avoid/01_restating_the_target.md),
[premise screening](../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[scope](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
and [separate bounds](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).
The log/divisor identities below are representations. The regularization
bias is an acquisition bound, and the polynomial example is an information
control with an explicit scale. None supplies canonical signed smallness.
All-window vanishing retains its already classified RH-equivalent meaning;
no sample checks are evidence for that reformulation.

Use exactly the accepted [E02 consumer](../../notes/03_TND_OC_E02_VERIFIED_CONSUMER_20261107.md)
and [Note02](../../notes/02_TND_OC_LOCAL_LOG_TRANSFER_20261107.md):

\[
\lambda=0,\quad X\ge10,\quad0<h\le1,\quad
s=\tfrac12-iz/2,\quad F=\frac{s-1}{s}\zeta(s)=DH_0,
\quad c=X+4i,\quad r=25/6,\quad R=9/2.
\]

The complete theta cosine source and zero-free multiplier D are unchanged.
For \(a=w((x-X)/h)y_+^2\kappa(y)\), take
\(\varphi_Q=2a\) or \(\varphi_\eta=2\log(1+\eta a)\), \(\eta>0\),
with Note02's support and plateau conditions. Write

\[
S_\varphi(V)=\frac1{2\pi}\int_{D(c,r)}\Delta\varphi\log|V|\,dA,
\qquad K_\varphi=\|\Delta\varphi\|_\infty/(2\pi).
\tag{1}
\]

For canonical F this is Q or log Z. All multiplicities are counted;
real zeros contribute zero. A plateau pair with height at least
\(0<d\le1\) forces the respective margin

\[
M_Q(d)=2d^2,\qquad M_\eta(d)=2\log(1+\eta d^2).
\tag{2}
\]

For the exact finite-source approximant \(\widehat F\), E02 gives

\[
|S_\varphi(F)-S_\varphi(\widehat F)|\le E_\varphi
=K_\varphi C_X(\delta/M_X)^{2/(n_X+2)},
\tag{3}
\]
\[
\delta=\mathcal B_X[5C_2(J)I_{17/2}+B_0I_{17/2}^{>U}]
\le\min(1,c_0/2).
\tag{4}
\]

Every constant is Note02's: complete arithmetic and radial tails,
enlarged-disk multiplier, safe anchor, and h/eta derivative costs remain.
No exponent uniform in height is substituted. A numerical consumer would
add separate integration and rounding errors to (3); none is evaluated.
The approximant's zeros in \(1<y<2\) retain their actual cutoff weights.

## 2. Route A: what the vanishing does and does not buy

The one focused clarification is whether the quadratic real-axis
vanishing of phi makes the **log-error weight** vanish there. On the
plateau, for \(0<y<1\),

\[
\Delta\varphi_Q=4,\qquad
\Delta\varphi_\eta=
\frac{4\eta(1-\eta y^2)}{(1+\eta y^2)^2}\longrightarrow4\eta.
\tag{5}
\]

More generally the limit is 4w or 4eta w. Thus the immediate absolute
estimate on a log residual e is
\((2\pi)^{-1}\int|\Delta\varphi|\,|e|\), not a y-squared weighted
log norm. For arbitrary smooth nonnegative residuals supported where
\(0<y<\varepsilon\) in the plateau, a proposed domination by
\(C\int y^\beta|e|\), \(\beta>0\), would require C to grow at least
as a constant times \(\varepsilon^{-\beta}\). This only disproves
that **unqualified weighted-norm substitution**. Such test residuals
are not asserted to be holomorphic log differences; an additional
estimate restricted to that class is not ruled out.

One can legitimately retain the vanishing by differentiating a smoothed
logarithm. For either normalized field
\(f=F/M_X\) or \(g=\widehat F/M_X\), set, for \(0<\tau\le1\),

\[
u_\tau(f)=\tfrac12\log(|f|^2+\tau^2),\qquad
\Delta u_\tau(f)=
\frac{2\tau^2|f'|^2}{(|f|^2+\tau^2)^2},
\]
\[
T_{\varphi,\tau}(f)=\frac1\pi
\int\varphi\frac{\tau^2|f'|^2}{(|f|^2+\tau^2)^2}\,dA\ge0.
\tag{6}
\]

The derivative formula follows by differentiating \(\log(|f|^2+\tau^2)\)
and using holomorphy. Integration by parts uses the same compact
C^(1,1) test as E02. As tau decreases to zero, u_tau decreases to
log|f| in local L1: the nonnegative difference is bounded by the
integrable function \(u_1-\log|f|\). Consequently

\[
T_{\varphi,\tau}(f)\longrightarrow S_\varphi(F).
\tag{7}
\]

This is compatible with a real zero of any multiplicity: its limiting
weight is zero. A nonreal zero keeps its full positive test weight.
Formula (6) does not assume simplicity or remove a collar zero.

An explicit bias follows from E02's existing sublevel bound. Let

\[
L_X=n_X\pi(R+r)^2e^{102A_X/n_X},\qquad
|\{|f|<t\}\cap D(c,r)|\le L_Xt^{2/n_X}.
\]

Here \(n_X\ge2\) in the stated canonical regime, also for g with the
same common constants. Layer cake gives

\[
\begin{split}
\int(u_\tau-\log|f|)\,dA
&\le L_X\tau^{2/n_X}
\int_0^\infty(e^{2v}-1)^{-1/n_X}\,dv\\
&\le 2n_XL_X\tau^{2/n_X}.
\end{split}
\tag{8}
\]

For the last step split at v=1: on (0,1) use
\(e^{2v}-1\ge2v\), giving at most 2 for n>=2; on [1,infinity)
use \(e^{2v}-1\ge e^v\), giving less than n. Thus n+2<=2n.
No new estimate of canonical small values is hidden in this calculation.
In particular

\[
|T_{\varphi,\tau}(g)-S_\varphi(\widehat F)|
\le B_{\varphi,\tau}:=2K_\varphi n_XL_X\tau^{2/n_X}.
\tag{9}
\]

The bias exponent 2/n_X concerns smoothing one logarithm; it does
**not** replace the source-transfer exponent 2/(n_X+2) in (3).
The potential consuming bound is precisely

\[
T_{\varphi,\tau}(g)+B_{\varphi,\tau}+E_\varphi
+E_{\rm integration}+E_{\rm rounding}<M_\varphi(d).
\tag{10}
\]

The missing canonical input is an independent upper estimate on the first
term of (10), using the joint numerator and denominator in (6).
Complete source values and derivatives define that term but do not bound
it favorably. For example, the generic Cauchy bound from R-r=1/3 gives
\(|g'|\le3\) on D(c,r), and merely yields

\[
T_{\varphi,\tau}(g)\le\frac9{\pi\tau^2}\int\varphi\,dA.
\tag{11}
\]

This allowance grows when smoothing bias shrinks. Neither this bound
nor source positivity supplies the required joint control. The direct
signed pairing with a harmonic baseline, in turn, is exactly S itself;
renaming its residual does not acquire an estimate. We stop this route
**with the inspected E02 acquisition/upper-bound inputs**, not all weighted
or signed logarithmic methods. Equations (6)--(10) are not a ready
request to “prove the remaining integral small”.

## 3. Route B: retaining real zeros, and the count input it would need

Let \(P_R(z)=\prod_l(z-a_l)^{m_l}\), with real a_l and positive integer
m_l, and let v be harmonic near the test support. The weak zero formula
implies exactly

\[
S_\varphi(P_R)=0,\qquad
S_\varphi(F)=\frac1{2\pi}\int\Delta\varphi
       [\log|F|-\log|P_R|-v],dA.
\tag{12}
\]

This holds even if the chosen real roots are not roots of F: the
meromorphic quotient then has real poles, each killed by phi. To call
P_R a **divisor of F**, however, its roots and multiplicities must be
independently justified. If they are, F/P_R is holomorphic, but its
unremoved zeros are still present. Even removing every real zero in a
compact domain does not prove the quotient zero-free.

The improvement over a harmonic baseline is real at the level of
representation: for \(F=(z-a)^m e^q\), a real a and holomorphic q,
choosing \(P_R=(z-a)^m\), \(v=\Re q\) gives zero residual. This
observation is direct and does not consume B02's pending norm theorem.
We do not carry B02's full-disk harmonic allowance floor into this class.

Two further payments cannot be suppressed. First, the uniform field
error \(|F-\widehat F|\le\delta\) cannot simply be divided by P_R
at its roots. An approximant must share the required vanishing, or
deflation must be bounded by actual Taylor/divided-difference information.
For example F=z-a and Fhat=z-a+epsilon have a small field difference
but their difference divided by z-a is unbounded. Second, an asserted
real-rooted G close enough to F would give S(G)=0 and a useful error
consumer, but E02's finite theta source has no such real-rootedness
theorem. Its nonreal and collar zeros cannot be discarded.

### Independent finite input, identified but not acquired

Choose a compact Jordan domain Omega lying strictly within D(c,r),
containing the whole test support in its interior, and with no F-zero
on its boundary. The support buffer permits such geometry; a quantitative
boundary clearance still has to be supplied for a certificate. Let

\[
N_\Omega=\frac1{2\pi i}\int_{\partial\Omega}\frac{F'}F,dz,
\quad N_\Omega\le U,\qquad
\text{certified real multiplicity in Omega}\ge M_R,
\tag{13}
\]

where U and M_R are rigorously justified integers and M_R<=N_Omega.
The argument principle requires holomorphy inside and nonvanishing on
the complete contour; see Tao, Theorem32/Corollary33 in the
[checked primary passage](https://terrytao.wordpress.com/2016/10/11/math-246a-notes-4-singularities-of-holomorphic-functions/).
Then \(R_\Omega=U-M_R\ge0\) bounds the number of unaccounted zeros,
including every nonreal zero relevant to the test. The canonical strip
and the factor two in the test give the coarse but valid bounds

\[
Q\le2R_\Omega,\qquad
\log Z(\eta)\le2\log(1+\eta)R_\Omega.
\tag{14}
\]

A nonzero integer R_Omega makes these particular allowances at least
the one-pair margin for every 0<d<=1. Thus **this count-only recipe needs
U=M_R** to pass the strict consumer. It then proves zero statistic
directly and does not need an extra logarithmic acquisition error.
More informative weighted locations could improve (14), but are not
among its premises.

This identifies a concrete independent information type: an upper contour
count matched by a lower count of actual canonical real zeros. Real-axis
sign changes of H_0 can supply lower counts on disjoint intervals without
assuming simplicity; even multiplicities need additional information if
they are to be counted. A certified contour can supply the upper count.
Neither count is defined by the unknown transverse statistic. However,
no particular matching counts, contour lower modulus, or every-center
unbounded-height theorem of this kind has been acquired in the inspected
inputs. Equation (13) alone is an identity, not those data.

If attempted finitely, source/derivative approximation, contour clearance,
phase integration, real-axis sign margins and rounding must all be paid.
E02's full-disk error gives derivative error at most 3delta on D(c,r),
but gives no positive lower bound for F on an arbitrary chosen contour.
A finite verification would cover only its declared domains, not all
large heights. No such computation or new execution packet is issued.

### Shared real divisors and safe anchors do not force reality

There is a simple normalized local information control, independent of
the physical theta-control families. For 0<d<=1 define

\[
f_\pm(z)=\frac{(z-X)^2\pm d^2}{5(-16\pm d^2)}.
\tag{15}
\]

On the same D(c,R), both have anchor f_+(c)=f_-(c)=1/5 and
\(\|f_\pm\|_\infty\le293/300<1\), since |z-X|<=17/2. Yet f_+
has the pair X±id, while f_- has only real roots. Direct subtraction gives

\[
f_+-f_-=-\frac{2d^2[(z-X)^2+16]}{5(256-d^4)},\qquad
\|f_+-f_-\|_\infty\le\frac{353}{2550}d^2.
\tag{16}
\]

Their Q responses are 2d^2 and zero; their product-log responses are
2log(1+eta d^2) and zero. Multiplying both by any fixed real polynomial
P_R divided by its nonzero disk supremum retains a common prescribed
real divisor, a common positive anchor modulus, the upper bound one and
the difference estimate. All added real zeros remain invisible to phi.

Thus a common known real divisor, bounded holomorphic field and safe
anchor with a **fixed positive approximation tolerance** do not exclude
arbitrarily small nonreal pairs. This is not a counterexample to E02,
whose tolerance adapts to d, nor to a theta-specific estimate or an
accurate finite count certificate. The polynomials fail the unchanged
canonical source identity. The familiar splitting of z^2 into a real or
imaginary pair is also illustrated in Tao's Notes4, Example35; the
specific disk normalization and constants here are calculated above.

## 4. Analytical collision-control screen

The controls in cluster12 were screened against the two proposed
inferences; their earlier numerical certificates were not rerun. Generic
identities (1), (6), (12) and (13) are compatible with control zeros.
None is an exclusion estimate. A physical positive-time collision is not
silently treated as a time-zero canonical event.

| Control | Exact premise absent from the canonical application; consequence |
| --- | --- |
| Euler-factor family | Unchanged theta coefficients/conductor are absent. Generic smoothing and real-divisor subtraction still hold; for 0<c<1 its unchanged real-zero set at time zero does not control its additional nonreal zeros. |
| Weighted square sources, finite coefficient/tail changes | Full normalized reflection and unchanged complete theta coefficients are absent. Finite square positivity and endpoint matching provide neither (10)'s value nor matching counts in (13). |
| Reflected super-Gaussian | Integer-square theta arithmetic is absent, although reflection and positivity remain. It satisfies the local identities where holomorphic; no signed estimate is supplied. |
| Smooth shape / positive-primitive controls | The complete canonical arithmetic expansion is absent despite shape, endpoint or auxiliary-transform properties. Those properties do not bound the small-value quotient (6). |
| Finite-prime orbit controls | Full reflection and unchanged all-coefficient theta source are absent. Finite prime/measurement agreement is not a complete residual-divisor estimate. |
| Atomic fixed-event and finite-profile controls, including continuous extensions | Full theta profile/coefficients and eventual simplicity at their threshold are absent. Their finite data cannot serve as the unacquired canonical count equality. |
| RH-conditional normalized endpoint controls | Ordinary Dirichlet-series arithmetic is absent. Their added real doubles have zero test weight; no simplicity conclusion is requested or inferred. |
| Variable observation kernels | The full cosine oscillator/Newman equation is absent even when amplitude is fixed. Equations (3)--(4) use the actual cosine source, not just zero raw mismatch. |
| Actual-theta three-profile relaxation | It retains the specified canonical measurements but admits fractional masses and omits the full coupling to an integer zero divisor. Its relaxed atom is not an actual canonical zero configuration; those three observations supply neither the joint integral bound nor the certified integer counts. |

Reflection rigidity distinguishes the complete normalized theta source;
it is not a signed bound for (10) or a count equality. The controls'
failed canonical identities do not prove a favorable canonical estimate.
Conversely a legitimate finite count certificate need only fail on a
domain containing its detected nonreal zeros, not on every control window.

All bounds here are per center. Averaging over centers in an interval of
length T retains one pair's \((2d^2h/T)\int w\) signal (and the analogous
\((2h/T)\int\log(1+\eta d^2w)\)); it cannot be read as an every-center
estimate. No HDA theorem is extended to time zero, and no sibling Green
obstruction is imported. No canonical zero, numerical source value or
cutoff sweep was evaluated.

## 5. Author check, disposition and reopening condition

Author checking recalculated the factors 2 and pi in (6), the one-sided
limit (5), the sublevel layer cake and n>=2 bound (8), and the exact
fractions in (15)--(16). The count in (13) is multiplicity-weighted and
does not assume real zeros exhaust the region; that exhaustion is the
missing equality, not a premise smuggled into deflation. These checks
are not E03 or an independent assessment of the present note.

The accepted input package and pending E03 manifest were verified before
research: all 17 frozen inputs matched. B02's sharp constant and allowance
floor were read only as provisional context and were not needed to prove
any statement above. Existing proof notes and the frozen bibliography
remain unchanged. Source usage: Tao's 246B Notes1, Exercise7, was reopened
for the smooth zero-measure identity; E02 supplies its C^(1,1) extension.
Tao's 246A Notes4, Theorem32/Corollary33 and Example35, were checked for
(13) and the standard splitting example. These are passage checks, not
full source reviews; [reference record](../../references/README.md) and
[B03 bibliography](../../references/b03_real_divisor_sources.bib).
The regularization bias and normalized constants are derived here; no
novelty claim or third-party PDF is involved.

**Scoped failure:** the inspected complete-source acquisition, safe-anchor,
generic derivative/sublevel bounds and real-divisor algebra do not furnish
the independent canonical smallness or divisor-completeness input for
either selected route. This is a limit of this bounded comparison, not a
theorem excluding all real-zero-aware or signed-log estimates.

**Next: [E] TND-OC-E03 — GPT-6.1 Sol / ultra where supported**, with the
author retaining model/effort choice: complete the existing fixed B02
proof/scope assessment. Do not extend its frozen request to this new note.
Reopen B03 only with a named canonical joint small-value estimate or
controlled remaining-divisor input, its domain, quantitative margin and
complete payments. Without that input the two routes stay parked.
The [continuation](../../continuation-notes/06_TND_OC_AFTER_B03_AND_MODEL_CHANGE_20261108.md)
gives the exact next action and preserves the review boundary.

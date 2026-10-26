# Retained arithmetic on the moving positive band and both overlaps

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort
ultra**, base chat0025, thread `01a179ab-8856-7ba0-89a2-500b2d854c80`.

**Status: proved in-note from named inputs; same-model internal
assessment only.** This returns [HDA-A08-AN03 r1][packet]. The existing
frozen-N elementary finite-mode family and its explicit Riemann--Siegel
completion suffice on `4/L<=t<=1`. A fresh growing-shift initial-error
lemma pays the new domain; no fixed-strip constant is substituted on a
growing strip. The complete normalized allowance is
`eta(X)=Lambda^2 X^(-3/4)->0`, with spatial0--3, direct first time,
actual residual and residual_z, and both genuine overlaps.

[Inputs26][inputs] pins inputs. [Assessment20][review] and the [analytical
work record][work] record the checks. Constants/onsets are finite and
uninstantiated. No numerical, machine-symbolic, exact-arithmetic,
sampling, fitting or interval research, manuscript edit or new build was
performed. [Summary67][summary] gives the requested whole-chat handoff.

## 1. Frozen contract, finite model and theorem

Keep the complete canonical theta source, heat sign and normalization

\[
H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\quad H_t=-H_{zz},\quad H(0,z)=\xi(s(z))/8,
\quad s=(1+iz)/2.
\tag{RA1}
\]

The physical `q=epsilon_g^2` and fixed averaging `K=k_ell k_h` are
unchanged. Fix `r=ell+2`, `b=1+h+2`, the target chart
`Omega_X={|Re z-X|<=r,|Im z|<=b}`, and one extra analytic unit
`Omega_Xplus={|Re z-X|<=r+1,|Im z|<=b+1}`. Branches are continued
from positive real height. Write

\[
L=\log(X/(4\pi)),\quad\Lambda=1+\log X,\quad L_z=\Log(z/(4\pi)),
\quad a(z)=\sqrt{z/(4\pi)},\quad a_X=\sqrt{X/(4\pi)},
\quad N=\lfloor a_X\rfloor.
\tag{RA2}
\]

Freeze N and X throughout each chart and every differentiation. Put

\[
M(w)=\frac{w(w-1)}{16}\pi^{-w/2}\Gamma(w/2),\quad\alpha=M'/M,
\quad G(z)=[M(s)M(1-s)]^{1/2},
\]
\[
\mathcal C(p)=\frac{\cos(2\pi(p^2-p)-\pi/8)}{\cos(2\pi p)},\quad
\mathcal R_N(z)=(-1)^NG(z)a(z)^{-1/2}\mathcal C(a(z)-N),
\quad\kappa_c=\pi^2/64.
\tag{RA3}
\]

All apparent poles of C are removable. Choose G positive on the real
segment. This gives a zero-free holomorphic G on the sectors used below;
R_N itself can vanish and is never divided by. Use Note25's exact arms
`C_epsilon(t,z)` and positive envelope `E_o=sum|C_epsilon|`, with
`b_epsilon=L_z/2+epsilon i pi/4`. Explicitly define

\[
P_{\epsilon,n}(t,z)=C_\epsilon(0,z)n^{-1/2}
 e^{-\epsilon iz\log n/2}e^{t(b_\epsilon-\log n)^2/4},\quad
F_N(t,z)=\sum_{\epsilon=\pm1}\sum_{n=1}^NP_{\epsilon,n}(t,z)
                         +e^{-\kappa_ct}\mathcal R_N(z).
\tag{RA4}
\]

This is exactly Note04 CS4/CS24, with `2N=O(sqrt X)` elementary mode
arms and one explicit gamma/RS completion. It contains no H or xi
integral, no fitted data, and no unbounded arithmetic population. Its
proof uses integrals; its field definition does not retain them.

**Theorem.** For all sufficiently large X, uniformly on Omega_X and
`4/L<=t<=1`, with finite constants depending on the fixed buffers,

\[
\boxed{|\partial_z^j(H-F_N)|\le C_jE_o\Lambda^j\eta(X),
\quad j=0,1,2,3,\quad\eta=\Lambda^2X^{-3/4},}
\]
\[
\boxed{|(H-F_N)_t|\le C_tE_o\Lambda^2\eta,\quad
|\operatorname{Res}F_N|\le C_RE_o\eta,\quad
|\partial_z\operatorname{Res}F_N|\le C_RE_o\Lambda\eta.}
\tag{RA5}
\]

Here `Res F=F_t+F_zz`; it is generally nonzero. Section7 constructs
sufficient finite onsets. No derivative of a floor or O allowance,
backward-heat supremum contraction, or field inference from a residual
alone is used.

## 2. The first potential gap and its fresh initial-error payment

Let

\[
S_N(z)=\sum_{n\le N}\{M(s)n^{-s}+M(1-s)n^{-(1-s)}\},\quad
E_N(z)=H(0,z)-S_N(z)-\mathcal R_N(z).
\tag{RA6}
\]

Note04 CS3 proves, for every fixed horizontal radius and transverse
width, `|E_N|<=C X^(-3/4)(|M(s)|+|M(1-s)|)`, with its actual
fixed-N hypothesis. Positive Gaussian evolution at time t samples
imaginary shifts of size O(tL). Thus its fixed-strip constant alone
cannot be used on the whole present band. The following lemma supplies
that missing estimate rather than assuming it.

Set `U=X^(1/3)`. For `z in Omega_Xplus`, define `z_v=z-2iv`, real v.
Let Sigma bound `|Re s|,|Re(1-s)|` on that chart and choose
`V=Sigma+3`. Then, uniformly for `|v|<=U`,

\[
|E_N(z_v)|\le C X^{-3/4}
       \{|M(s+v)|+|M(1-s-v)|\}.
\tag{RA7}
\]

**Proof.** For `|v|<=V`, apply CS3 on the single enlarged *fixed*
initial chart of transverse width `b+1+2V` and horizontal radius r+1.
Its own finite onset and constant are retained. For `V<=|v|<=U`, choose
the dominant xi argument `q=s+v` for positive v and `q=1-s-v` for
negative v. Then `sigma=Re q>=3`, `sigma<=U+Sigma`, and
`|Im q|` is comparable to X. The exact functional equation and ordinary
[Dirichlet series][zeta] give

\[
\frac{E_N(z_v)}{M(q)}=
 \left(\zeta(q)-\sum_{n\le N}n^{-q}\right)
 -\frac{M(1-q)}{M(q)}\sum_{n\le N}n^{q-1}
 -\frac{\mathcal R_N(z_v)}{M(q)}.
\tag{RA8}
\]

Both q and 1-q remain in fixed sectors even when one real part is
negative. The [sectorial gamma bounds][gamma] give alpha'=O(1/X)
on the entire horizontal segment joining their real parts at fixed
imaginary height. Since M respects conjugation, integrate Re alpha
along that segment to obtain

\[
\frac{|M(1-q)|}{|M(q)|}
 \le C a_X^{1-2\sigma}\exp\{C(1+v^2)/X\}.
\tag{RA9}
\]

More explicitly, at real part1/2 the real logarithmic derivative is
`log a_X+O(1/X)`; moving it by O(sigma+1) changes it by
`O((sigma+1)/X)`. Integration over length O(sigma+1) gives the
`O((1+sigma^2)/X)` error in the logarithm of RA9. Replacing local
height Re z by X costs only O((1+sigma)/X). Thus the constant is
uniform through U; it is not a fixed-strip constant with sigma inserted.

The two growing-parameter factors are controlled before absorption:

\[
\exp\{C(1+U^2)/X\}=O(1),\quad
(a_X/N)^{\sigma-1}\le\exp\{2(U+\Sigma)/a_X\}=O(1).
\tag{RA10}
\]

The latter uses N>=a_X/2 and N=floor a_X. Also
`|a(z_v)-a_X|<=C(r+b+1+2U)/sqrt X=o(1)`, so `a(z_v)-N`
stays in a fixed compact neighborhood of[0,1]. C and its needed finite
derivatives are uniformly bounded there. Equations RA3/RA9 imply

\[
\frac{|\mathcal R_N(z_v)|}{|M(q)|}
 \le C a_X^{-\sigma}\exp\{C(1+v^2)/X\}.
\tag{RA11}
\]

In RA8, absolute summation of *all* n>N gives
`N^(1-sigma)/(sigma-1)<=C a_X^(1-sigma)`. The reflected finite sum
has modulus at most N^sigma, hence after RA9 at most
`C a_X^(1-sigma)` because N<=a_X. RA11 is no larger. Since sigma>=3,
all three terms are O(X^-1). This is stronger than RA7 on these outer
portions. It combines with the fixed-inner-strip estimate to prove RA7.
The omitted arithmetic is paid by a complete ordinary tail; no modes
or completion terms were dropped. This proof uses no growing-order RS
theorem or off-domain published small-time approximation.

## 3. Exact positive evolution, all large shifts and the finite population

The exact full-source identity is

\[
H(t,z)=\int_{\mathbb R}K(t,v)H(0,z-2iv)\,dv,
\quad K(t,v)=(\pi t)^{-1/2}e^{-v^2/t},\quad t>0.
\tag{RA12}
\]

It follows directly from RA1 by Gaussian averaging and complete
super-exponential source domination, and agrees with [Polymath(35)][pm].
Split the proof at fixed-with-chart `+-U`. On its inner interval insert
RA6 and RA7. No contour is deformed: there are no connectors. U and N
are fixed before t,z derivatives; artificial endpoint terms are not
silently differentiated. Direct time differentiates the fixed kernel.

On the local tube fixed-sector Taylor bounds give

\[
M(w+v)=M(w)e^{\alpha(w)v+R_2(w,v)},\quad
|R_2|\le C v^2/X\le C U^2/X\le1.
\tag{RA13}
\]

Reflection of v treats the second arm identically. Normalized Gaussian
moments against `exp(-v^2/t+a v)` have mean `ta/2`, variance `t/2`
and absolute-to-complex factor `exp(t(Im alpha)^2/4)`, bounded for
`0<t<=1`. In particular RA7 integrates to

\[
\left|\int_{-U}^UK E_N(z_v)\,dv\right|
 \le C E_o X^{-3/4}.
\tag{RA14}
\]

Here `sum |M(w)exp(t alpha(w)^2/4)|` and E_o are comparable for
`0<=t<=1` by the zero-time sectorial expansion, re-bounded on this
interval. Its logarithmic calibration is O(Lambda/X); no positive-time
field theorem is being extended to obtain this comparison.

For the true infinite ends reflect the xi argument to Re>=3 and use
the full absolutely convergent zeta series. Retain the gamma ratio

\[
\log\frac{|M(w+v)|}{|M(w)|}
 \le C_{\rm ray}v+\tfrac12v\log(X+v),\quad v\ge0.
\tag{RA15}
\]

Choose the finite onset so
`C_ray+(1/2)log(X+U)<=U/(4S)`, S=2, and
`U>=4S C_alpha Lambda`. The ratio of the left coefficient to v
decreases for v>=U. The Gaussian then pays both complete source ends
by `C E_o exp(-cU^2)`. The same gates pay the artificial full *linear*
mode Gaussians below, including their complete finite population.
Polynomial kernel-time factors are absorbed by reducing c once; on the
band, `1/t<=L/4`. The height exponential is retained through RA15,
not replaced by a height-independent source mass near U.

For every n<=N, the positive multiplier in an elementary mode obeys

\[
\frac{|P_{\epsilon,n}(t,z)|}{|C_\epsilon(t,z)|}
 =n^{(\epsilon\Im z-1)/2}
   \exp\{t\log n(\log n-\Re L_z)/4\}.
\tag{RA16}
\]

The exponential is <=1 after `log N<=Re L_z`, an eventual gate.
For y>=0, the suppressed arm satisfies
`|C_+|/E_o<=C X^(-y/2)` and its population costs at most
`C N^((y+1)/2)`. The other arm costs at most `C N^1/2`. Reflect
for negative y. Consequently, uniformly on the full larger buffer,

\[
\sum_{\epsilon,n\le N}|P_{\epsilon,n}(t,z)|
 \le C E_o X^{1/4},\quad0\le t\le1.
\tag{RA17}
\]

This is the entire finite population, not a bounded-n estimate. No
assumption tL<=8 was needed for the positive-time multiplier.

## 4. Mode curvature, gamma calibration and RS completion

For w=s,1-s and k_n=log n, linearizing the gamma factor in each
local initial mode and completing its Gaussian gives

\[
\mathcal P_{w,n}(t,z)=M(w)n^{-w}
            \exp\{t(\alpha(w)-k_n)^2/4\}.
\tag{RA18}
\]

The negative v sign of the reflected initial arm is removed by Gaussian
symmetry. RA13 gives `|exp R2-1|<=C v^2/X`. With
`a_n=Re alpha(w)-k_n`, `|a_n|<=C Lambda`, the normalized second
moment is `O(t+t^2 a_n^2)`. Thus the per-mode curvature error is
`C(t+t^2 Lambda^2)/X` times its nonzero evolved gamma arm modulus.

The exact-gamma to elementary calibration costs
`C(1+t Lambda)/X` per mode on this longer interval: M/C(0) has
relative error O(1/X), and alpha-b_epsilon=O(1/X), so the difference
of the two heat exponents is O(t Lambda/X). These are explicit finite
formulas. Their moduli are comparable after a finite onset uniformly
for all n<=N. Summing with RA17 pays the complete local mode error by

\[
C E_o\Lambda^2 X^{-3/4}.
\tag{RA19}
\]

Artificial tails from completing these *linear* Gaussians are bounded
using means of size O(Lambda), the bounded complex loss and the gates
after RA15. All N modes are included in their payment. The true
nonlinear gamma modes or the actual RS correction are not extended
uncontrolled to infinite shifts.

For the correction write `f_N=a^-1/2 C(a-N)`. On the whole local
tube its argument lies in the same fixed compact set as RA11. Hence

\[
|f_N|\le C X^{-1/4},\quad |f_N'|\le C X^{-3/4},\quad
|f_N''|\le C X^{-5/4}.
\tag{RA20}
\]

Fixed-sector expansions, re-derived uniformly for `|Im z|=O(U)`, give
`G'/G=-pi/8+7/(4z)+O(X^-2)` there. Indeed
`alpha(s)-alpha(1-s)=i pi/2-7i/z+O(X^-2)` uniformly in this
sector; multiplying by i/4 gives the displayed derivative. The
log-height terms cancel before any growing-shift bound is taken.
Integration along the local vertical segment, and RA20, give

\[
|\mathcal R_N(z-2iv)-e^{i\pi v/4}\mathcal R_N(z)|
 \le C|G(z)|X^{-3/4}(|v|+v^2),\quad |v|\le U.
\tag{RA21}
\]

The full Gaussian of the elementary exponential is exactly
`exp(-pi^2 t/64) R_N(z)`. Its local error is bounded by
`C|G|X^-3/4(sqrt t+t)<=C E_o X^-3/4`. Only that elementary
exponential is completed past U. The true R_N is used exclusively on
the local tube where RA11/RA20 justify it. RA14, RA19, RA21 and all
true/artificial tails prove the scalar field part of RA5 on Omega_Xplus.

## 5. Direct first time and spatial jets

Differentiate RA12's fixed kernel before estimating:

\[
K_t=K(v^2/t^2-1/(2t)).
\tag{RA22}
\]

All integral differentiations are justified by source and gamma
domination in a positive neighborhood of each time. The lower bound
`t>=4/L` is applied to estimates, not differentiated. For the initial
RS remainder RA7, the weighted Gaussian average adds
`C(1/t+Lambda^2)<=C Lambda^2`, so its direct-time cost is
`C E_o Lambda^2 X^-3/4`.

For mode curvature, integrate the weights *before* using the lower
time endpoint. For a real Gaussian of mean `ta_n/2` and variance t/2,

\[
\frac{\mathbb E|v|^4}{t^2}+\frac{\mathbb E|v|^2}{t}
 \le C(1+t a_n^2+t^2a_n^4)\le C\Lambda^4.
\tag{RA23}
\]

This pays `C Lambda^4/X` per mode. It avoids an unnecessary loss from
bounding 1/t^2 before computing moments. Direct time calibration of
RA18 uses the exact exponential derivatives. If
`A_n=(alpha-k_n)^2/4`, `A0_n=(b_epsilon-k_n)^2/4`, then

`(mathcal P-P)_t=A_n(mathcal P-P)+(A_n-A0_n)P`.

Here `|A_n|<=C Lambda^2`, `|A_n-A0_n|<=C Lambda/X`; the explicit
field calibration gives a time cost at most `C Lambda^3/X` per mode,
inside the same Lambda^4/X budget. No O allowance was differentiated.
RA17 gives the total mode time error `C E_o Lambda^4 X^-3/4`.

RA21 under the kernel derivative costs
`C|G|X^-3/4(1+t^-1/2)<=C E_o Lambda X^-3/4`, within that budget.
All large-shift time tails have already been paid after RA15. Therefore
RA22--23 prove the direct-time row of RA5.

For spatial derivatives use disks of radius `1/(8 Lambda)` within
the extra analytic unit. The positive envelope varies by a bounded
factor there because `(log C_epsilon)_z=O(Lambda)` for t<=1.
Cauchy's formula on the scalar field error gives spatial0--3 on Omega_X
with the stated Lambda^j loss. X,N,U are fixed during this argument.
The growing initial tube in RA7 has supplied the required scalar bound
first; holomorphy alone is not used to infer a growing-strip estimate.

## 6. Actual residual and residual_z

For each elementary mode let `c=b_epsilon-log n`. Exact differentiation
gives

\[
\frac{\operatorname{Res}P_{\epsilon,n}}{P_{\epsilon,n}}
 =\frac{\epsilon i(1+7c+t c^2)}{4z}
  +\frac{21/16+t/8+5tc/8+t^2c^2/16}{z^2}
 =:\mathcal Q_{\epsilon,n}.
\tag{RA24}
\]

Now `|c|<=C Lambda`, t<=1, so
`|Q_epsilon,n|<=C Lambda^2/X`. This is the longer-time bound;
the old shrinking-window Lambda/X estimate is not reused here.
Also `|partial_z Q_epsilon,n|<=C Lambda^2/X^2` and
`|partial_z P_epsilon,n|<=C Lambda|P_epsilon,n|`.
On fixed target buffers, Note04 CS25/CS27 or direct differentiation
of RA3/RA20 gives
`R_N''-kappa_c R_N=O(|G|X^-3/4)`, and its z derivative fits the
same bound with one Lambda loss on the paid analytic margin.
The exact full residual is

\[
\operatorname{Res}F_N=\sum_{\epsilon,n\le N}
 P_{\epsilon,n}\mathcal Q_{\epsilon,n}
 +e^{-\kappa_ct}(\mathcal R_N''-\kappa_c\mathcal R_N).
\tag{RA25}
\]

Its z derivative follows by the product rule or paid Cauchy. Summing
RA24 with RA17 proves respectively
`C E_o Lambda^2 X^-3/4` and `C E_o Lambda^3 X^-3/4`, as in RA5.
These nonzero residuals do not remove the source comparison requirement.
The exact heat identity for H-F_N checks the direct-time rate already
proved from RA22.

## 7. Constants and sufficient finite onset

All constants come from finitely many named inputs: CS3 on the fixed
enlarged inner strip; sectorial log-gamma/digamma bounds on a slightly
larger fixed sector; C and its derivatives on a fixed compact
neighborhood K of[0,1]; finite real Gaussian moments; and the complete
ordinary Dirichlet tail. None depends on a moving strip width through
an unrecorded theorem constant. Choose the ray constant before U gates.

For example impose L>=16, all inherited CS3 onsets on the enlarged
fixed chart, the sector/buffer onset, and the following eventual gates:

\[
\begin{gathered}
U=X^{1/3}\ge2V,\quad a_X\ge2,\quad
4(U+\Sigma+1)/a_X\le1,\quad C_\gamma(1+U^2)/X\le1,\\
C_a(r+b+1+2U)/\sqrt X\le\operatorname{dist}([0,1],\partial K),
\quad C_{\rm cal}\Lambda/X\le1/4,\\
C_{\rm ray}+\tfrac12\log(X+U)\le U/(4S),\quad
U\ge4S C_\alpha\Lambda,\quad S=2,\\
\log N\le\inf_{z\in\Omega_X^+}\Re L_z,\quad
cU^2\ge2\log X,\quad\Lambda^2X^{-3/4}\le1/4.
\end{gathered}
\tag{RA26}
\]

One may replace the N gate by its sufficient continuous bound
`(1/2)L<=log((X-r-1)/(4pi))`; N<=a_X makes this valid eventually.
The floor-sensitive RA10 factor is controlled by the displayed
continuous majorant `4(U+Sigma+1)/a_X`, not by checking only selected
cutoff values. Reduce c once for the finitely many tail polynomial
weights before fixing its gate. All these gates hold at every larger
height after a finite threshold; powers beat logarithms and U/a_X
tends to zero. A symbolic doubling construction on their majorants
therefore terminates. No numerical onset or affordability is asserted.

## 8. Both genuine overlaps and the covered union

**Signed-window overlap `4<=tL<=8`.** For sufficiently large X this
lies in both the present band and Note04's nonnegative signed window.
After the maximum of actual onsets, on the same target chart and frozen
N, Note04 CS4 and RA4 are the *same formula*, including the RS term,
branches and one-arm normalization. Their difference is identically
zero. In particular comparison through their common H is valid at
the sum of the two proved errors. Note04 retains its stronger
X^-3/4 allowance on this smaller positive window; the present theorem
has the coarser eta appropriate to the longer band. The overlap has
positive width4/L for each chart and fixed scaled-time width4.

**Corrected-pair overlap `[3/4,1]`.** Note25's F1 theorem applies on
these same buffers after its own onset. Through common canonical H,
with `kappa_a=log2/4` and `B1=Lambda^4/X^2+X^(-t kappa_a)`,

\[
|\partial_z^j(F_N-F_1)|\le C_jE_o\Lambda^j(\eta+B_1),
\quad j\le3,\qquad
|(F_N-F_1)_t|\le C E_o\Lambda^2(\eta+B_1).
\tag{RA27}
\]

An optional eventual gate `Lambda^2<=X^(3/4-kappa_a)` absorbs eta
into B1 throughout this overlap. The slower omitted-arithmetic power
is still present in the F1 comparison; it is not replaced by eta.
No termwise match of canonical error expansions or fitted modes is used.

**Positive-time field coverage.** CS6/CS7 of Note04 on `0<=tL<=8`
and RA5 on `4/L<=t<=1` give the *same fixed-N model* uniformly on
`0<=t<=1`, with the RA5 allowance (and stronger inherited bounds near
zero). The residual bounds follow on this union from RA24--25, including
t=0. No moving time cutoff or interface defect is needed because the
formula agrees exactly on the overlap. This is a new positive-side
covered union, not a stronger recurrence error at zero.

Together with Note25 and Note20 this supplies a buffered high-height
field atlas on `[0,T]` for every fixed finite T>=33, after the maximum
of their finite T-dependent onsets. Models F_N and F1 have a genuine
overlap; no single time-spliced global formula is defined here. Existing
negative-side Note04/Note06 joins retain their weaker rates and source
domains. The new strong negative recurrence exp(-L^2/4) theorem still
excludes zero. No new global spatial join across changes of N, physical
tuple, bounded-height core, growing-time/order uniformity or evaluator
cost theorem follows from this field atlas alone.

## 9. Failed shortcut, controls, disposition and next deliverable

The focused failed shortcut was to use CS3's fixed-strip constant at
imaginary width O(tL). RA8--11 pay that width explicitly by the complete
ordinary tail and gamma ratios. The n=1 omitted-arithmetic allowance
also fails to vanish at bounded tL; this bound alone is not a sharp
lower-bound or impossibility theorem for other models. Retaining all
N modes avoids that unpaid omission.

This is an approximation under [avoid01][a01]. Read [result summaries][results],
[heat-flow11][r11], [collision controls12][controls], and [avoid][avoid],
especially [separate payments12][a12], [imports16][a16] and
[gain20][a20]. The quantitative gain is the newly covered moving band,
with explicit full-buffer eta and overlaps, using an unchanged finite
model. It is not a new existence theorem or claim of literature priority:
retained-arithmetic positive-time RS methods are established inputs.

Euler-factor controls fail the unchanged canonical coefficients/completion
used in RA8; weighted-square and finite-source controls fail the complete
canonical xi and corrected real RS input behind CS3; smooth-shape,
primitive and reflected super-Gaussian controls fail the ordinary theta
Dirichlet series; finite-prime/profile controls fail its complete
coefficient/reflection data. These name absent premises, not universal
exclusions of controls. Symmetry/positivity alone is not used to infer
any zero-sign, noncollision or RH conclusion.

**AN03 Complete/CLOSED at its frozen analytical scope.** No requested
estimate remains unpaid. The high-height compact-positive field coverage
and both regional matching gates are now paid. Wider A08/LT-07 remain
Partial for refinements and separate physical/core/global-assembly goals;
their former moving-band field gap is closed at eta, not left open.
Parent HDA-17 Partial, HDA-18 Gated and HDA-20 unfulfilled remain.
All assessments are internal same-model and constants/onsets symbolic.

Next **Analysis — Sol:** [B02-MI1 r1][next], prepared only, integrate
this chat's closed research into the Book and technical companions,
with exact rate/domain distinctions and build checks. This is production
follow-through, not a new scientific theorem. [Summary67][summary]
contains the complete handoff and remaining analytical frontier.

[packet]: ../research-progress/handoffs/HDA-A08-AN03.md
[inputs]: 26_RETAINED_ARITHMETIC_INPUTS_20261026.json
[review]: ../reviews/20_RETAINED_ARITHMETIC_MOVING_BAND_ASSESSMENT_20261026.md
[work]: ../numerics/A08_AN03_ANALYTICAL_WORK_RECORD_20261026.json
[summary]: ../../notes/67_CHAT0025_RESEARCH_SUMMARY_AND_HANDOFF_20261026.md
[next]: ../../research-progress/handoffs/HDA-B02-MI1.md
[gamma]: https://dlmf.nist.gov/5.11#ii
[zeta]: https://dlmf.nist.gov/25.2.E1
[pm]: https://arxiv.org/html/1904.12438v2#S4
[results]: ../../../../../result-summaries/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a16]: ../../../../../avoid/16_unchecked_imports_and_novelty_claims.md
[a20]: ../../../../../avoid/20_volume_without_a_gain.md

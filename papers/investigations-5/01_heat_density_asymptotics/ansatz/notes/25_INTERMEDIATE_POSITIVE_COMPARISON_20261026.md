# Corrected buffered comparison on [3/4,33] and its two overlaps

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort
ultra**, base chat0025, thread `01a179ab-8856-7ba0-89a2-500b2d854c80`.

**Status: proved in-note from named classical inputs; same-model internal
assessment only.** Return to [HDA-A08-AN02 r1][packet]. The corrected
elementary pair F1 has complete allowance
`B1=Lambda^4/X^2+X^(-t log2/4)` on precisely `[3/4,33]`, all fixed
buffers, spatial0--3 and direct first time. Its actual residual and
residual_z have the requested `Lambda^4/X^2`, `Lambda^5/X^2` rates.
Both genuine overlaps close. Constants and sufficient onsets are finite,
uninstantiated analytical quantities. No numerical, machine-symbolic,
exact-arithmetic, interval, sampling or fitting research was performed.
[Inputs25][inputs] pins the sources; [Assessment19][review] and the
[small work record][work] record the checks. No manuscript was edited.

## 1. Frozen contract and explicit corrected field

Keep the complete theta source, canonical normalization and heat sign:

\[
H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\quad H_t=-H_{zz},\quad H(0,z)=\xi(s(z))/8,\quad s=(1+iz)/2.
\tag{IP1}
\]

Physical `q=epsilon_g^2` and fixed `K=k_ell k_h` are unchanged. No
physical tuple is inferred from the field comparison. Fix `ell,h>0`,
`r=ell+2,b=1+h+2` and

\[
\Omega_X=\{|\Re z-X|\le r,\ |\Im z|\le b\},\quad
\Omega_X^+=\{|\Re z-X|\le r+1,\ |\Im z|\le b+1\}.
\tag{IP2}
\]

Use the holomorphic logarithm continued from positive height and set
`L_z=Log(z/(4pi))`, `L=log(X/(4pi))`, `Lambda=1+log X`,
`kappa=log2/4`. For `epsilon=+1,-1`, write

\[
b_\epsilon=L_z/2+\epsilon i\pi/4,
\]
\[
C_\epsilon=\frac{\pi^{1/4}z^{7/4}}{32}
\exp\left[-\frac{\pi z}{8}+\frac t{16}(L_z^2-\pi^2/4)
 +\epsilon i\left\{\frac z4(L_z-1)+\frac{\pi tL_z}{16}
                         +\frac{7\pi}{8}\right\}\right],
\]
\[
D_\epsilon=\frac{\epsilon i}{z}
 \left\{\frac1{24}-\frac t4-\frac{7t b_\epsilon}{4}
                     -\frac{t^2 b_\epsilon^2}{8}\right\},\quad
F_1=\sum_\epsilon C_\epsilon(1+D_\epsilon),\quad
F_0=\sum_\epsilon C_\epsilon,\quad E_o=\sum_\epsilon|C_\epsilon|>0.
\tag{IP3}
\]

This is exactly Note03 CB8 / Note20 RB6, with their phase7pi/8 and
one-arm normalization. No formula correction is needed. `E_o` includes
transverse growth and does not vanish when the two arms cancel.

**Theorem.** On `I=[3/4,33]`, for every fixed chart IP2 there are finite
constants and a sufficient finite height `X_*` in Section7 such that,
for `X>=X_*` and `z in Omega_X`,

\[
\boxed{|\partial_z^j(H-F_1)|\le C_jE_o\Lambda^j B_1(t,X),
\quad j=0,1,2,3,\quad B_1=\Lambda^4/X^2+X^{-t\kappa},}
\]
\[
\boxed{|(H-F_1)_t|\le C_tE_o\Lambda^2B_1(t,X),}
\]
\[
\boxed{|\operatorname{Res}F_1|\le C_RE_o\Lambda^4/X^2,\quad
|\partial_z\operatorname{Res}F_1|\le C_RE_o\Lambda^5/X^2.}
\tag{IP4}
\]

Here `Res F=F_t+F_zz`. In particular `B1=o(1)` uniformly on I;
its slowest arithmetic power is `X^(-3 log2/16)`. A small residual is
not being used to infer the canonical field error. Evenness supplies
the negative-height counterpart after the right tail is established.

## 2. Exact source split, rebuilt on the new compact interval

Use only the all-positive-time exact Gaussian identity, parent Note27
GO6 / [Polymath equation35][pm]:

\[
H(t,z)=\int_{\mathbb R}K(t,v)\xi(s+v)/8\,dv,
\quad K(t,v)=(\pi t)^{-1/2}e^{-v^2/t}.
\tag{IP5}
\]

It follows directly from IP1 by Gaussian averaging of
`cos((z-2iv)u)`. Absolute Fubini, also after one time derivative, follows
from the super-exponentially integrable complete source with a majorant
`C(1+u^2)e^(34u^2+(b+1)u)|Phi(u)|`. The auxiliary upper34 permits
domination in a neighborhood of the endpoints; no extra time domain
is claimed for IP4. No restricted error theorem is extended by citation.

Put

\[
M(w)=\frac{w(w-1)}{16}\pi^{-w/2}\Gamma(w/2),\quad
\alpha=M'/M,\quad G(t,w)=M(w)e^{t\alpha(w)^2/4}.
\tag{IP6}
\]

Choose `Sigma` bounding `|Re w|` for `w=s,1-s` on `Omega_X^+`,
and choose the single fixed endpoint `V=Sigma+3`. Splitting IP5 at
`-V,V` and using `xi(w)=xi(1-w)` gives exactly

\[
\begin{split}
H={}&J_V(t,s)+J_V(t,1-s)+A_V(t,s)+A_V(t,1-s)+I_V(t,s),\\
J_V(t,w)={}&\int_V^\infty K(t,v)M(w+v)\,dv,\\
A_V(t,w)={}&\int_V^\infty K(t,v)M(w+v)(\zeta(w+v)-1)\,dv,\\
I_V(t,s)={}&\int_{-V}^V K(t,v)\xi(s+v)/8\,dv.
\end{split}
\tag{IP7}
\]

The entire ordinary arithmetic population and the true enlarged middle
remain. All defining endpoints are fixed in t,z; the arm integrals are
holomorphic. There are no moving-endpoint Leibniz terms. No contour is
deformed, so there are no connectors to estimate or discard. The proof
split `U=X^(1/3)` below is held fixed with the chart center X and is not
part of a differentiated field definition.

## 3. Corrected local gamma calculation and all arithmetic modes

The fixed-sector [gamma remainders][gamma] and their holomorphic Cauchy
derivatives give, uniformly on the larger chart and its local rays,

\[
a:=\Re\alpha(w)=L/2+O(X^{-1}),\quad
\beta:=\Im\alpha(w)=O(1),\quad
|\alpha'|\le C_2/X,\quad |\alpha''|\le C_3/X^2.
\tag{IP8}
\]

For `V<=v<=U`, Taylor's integral formula gives

\[
\log M(w+v)=\log M(w)+\alpha(w)v+Q(w,v)+R_3(w,v),
\quad Q=\alpha'(w)v^2/2,\quad |R_3|\le C_3v^3/X^2.
\tag{IP9}
\]

After a gate `C_2 U^2/(2X)+C_3 U^3/X^2<=1`,

\[
|e^{Q+R_3}-1-Q|\le C(|R_3|+|Q|^2)
 \le C(v^3+v^4)/X^2.
\tag{IP10}
\]

For each fixed `k<=6`, real completion of the square gives

\[
\frac{\int_{\mathbb R}e^{-v^2/t+av}|v|^k\,dv}
 {\sqrt{\pi t}|e^{t\alpha^2/4}|}
 \le C_{I,k}\Lambda^k.
\tag{IP11}
\]

Its real Gaussian has mean `ta/2`, variance `t/2`, and the exact
absolute-to-complex loss `exp(t beta^2/4)<=exp(33 C_beta^2/4)`.
The constants are finite but not borrowed unchanged from Note24's
upper time1. Polynomial Gaussian integration, valid for complex alpha
by entire continuation with domination, yields exactly

\[
\int_{\mathbb R}K(t,v)M(w)e^{\alpha v}(1+\alpha'v^2/2)\,dv
 =G(t,w)(1+U_1(t,w)),
\quad U_1=t\alpha'/4+t^2\alpha^2\alpha'/8.
\tag{IP12}
\]

Thus IP10--11 give the corrected local gamma error
`C |G| Lambda^4/X^2`. We complete a polynomial, not the uncontrolled
exponential of a quadratic over the missing lower half-line.

For the complete arithmetic, the convergent ordinary [Dirichlet series][zeta]
on `Re(w+v)>=3` implies

\[
|\zeta(w+v)-1|\le3\,2^{-\Re w-v}.
\tag{IP13}
\]

On the local ray, `|exp(Q+R3)|<=e`. Completing the real square with
`a-log2` in place of a gives the carrier-normalized factor

\[
\exp[-ta\log2/2+t(\log2)^2/4+t\beta^2/4]
 \le C_I X^{-t\log2/4}.
\tag{IP14}
\]

The constants absorb `2^(-Re w)`, the fixed `(4pi)^(t kappa)` and
the bounded IP8 error. Every `n>=2` is included; this is not a mode
truncation. At the lower times the arithmetic allowance remains in
`B1` and is not hidden below the corrected gamma term.

## 4. Lower completion, enlarged middle, infinite ends and direct time

The lower completion of IP12 over `v<V`, together with its time-kernel
derivative, is at most

\[
C |G|\exp[-tL^2/16+C_m(1+L)].
\tag{IP15}
\]

For `a>=0`, bound the numerator, including the finite polynomial weights
through degree4, by `C e^(aV)`: `e^(av)<=e^(aV)` on this half-line and
all corresponding Gaussian moments are bounded on I. Divide by
`|exp(t alpha^2/4)|`. This includes the omitted lower quadratic
polynomial; it does not presume an exact heat equation for J_V.

In the original middle, reflect where needed to a fixed real-part range
`[1/2,D]`. Euler summation [DLMF25.2.8][euler] with `N=ceil X` gives
`|zeta(w)|<=C X` at imaginary height comparable to X. Bounded-real-part
Stirling then gives `|xi(w)/8|<=C X^(m_B) exp(-pi X/8)`, where m_B
depends on the *entire* buffer and V. Dividing by G retains
`exp(-tL^2/16+O_I(1+L))`, so the full middle and its time derivative
obey IP15. The fourth-power bound for a smaller earlier strip is not
used on these enlarged real-part ranges.

For the full infinite rays retain the carrier exponential by the ratio

\[
\log\frac{|M(w+v)|}{|M(w)|}
 \le C_{\rm ray}v+\tfrac12v\log(X+v),\quad v\ge0.
\tag{IP16}
\]

This follows by integrating the upper real logarithmic derivative from
the same fixed-sector bounds. Put `S=34` and impose

\[
C_{\rm ray}+\tfrac12\log(X+U)\le U/(4S),\qquad
U\ge4S\sup_w|\Re\alpha(w)|.
\tag{IP17}
\]

The ratio `[C_ray+(1/2)log(X+v)]/v` decreases for `v>=U` after a
fixed onset. Thus IP16 is at most `v^2/(4S)` there. Since `t<=33<S`,
the true Gaussian leaves at least `exp(-3v^2/(4S))`. The second gate
pays the linearized-polynomial ends as well. All true gamma ends,
both full arithmetic ends (using IP13), and the polynomial completion
ends beyond U are bounded by

\[
C |G|\exp(-c_I X^{2/3}).
\tag{IP18}
\]

Polynomial factors through degree4 are absorbed by reducing c_I once.
Using the old gate `U/4` from the upper-time1 proof would not pay these
upper-time33 rays; IP17 is the new payment. A height-independent global
source moment before carrier division would not establish IP18.

For **direct first time**, differentiate the fixed kernel first:

\[
K_t=K(v^2/t^2-1/(2t)).
\tag{IP19}
\]

The exact integrand used in IP12, `M exp(alpha v)(1+alpha'v^2/2)`,
is independent of t before integration. The local remainder IP10
therefore gains at most two moments, through degree6; local arithmetic
gains moments through degree2. With t bounded away from zero, their
time costs are `C |G| Lambda^6/X^2` and
`C |G| Lambda^2 X^(-t kappa)`. IP15/IP18 already include their
polynomial kernel weights. Differentiation is justified in a positive
time neighborhood by domination. No estimated allowance is differentiated.

Combining the exact split gives, with
`Q_gamma=G(t,s)(1+U1(t,s))+G(t,1-s)(1+U1(t,1-s))` and
`E_G=|G(t,s)|+|G(t,1-s)|`,

\[
|H-Q_\gamma|\le C E_G\widetilde B_1,
\quad |(H-Q_\gamma)_t|\le C E_G\Lambda^2\widetilde B_1,
\]
\[
\widetilde B_1=\Lambda^4/X^2+X^{-t\kappa}
 +e^{-tL^2/16+C_m(1+L)}+e^{-c_I X^{2/3}}.
\tag{IP20}
\]

For completeness the finite gamma arm itself has the exact forcing
`(partial_t-(1/4)partial_ww)J_V
=K(t,V)[M'(w+V)+(2V/t)M(w+V)]/4`, by integration by parts.
It has the same relative IP15 payment. The proof used direct kernel
differentiation and never assumed that this forcing vanishes.

## 5. Calibration to the existing F1, spatial jets and direct time

For `w_+=s,w_-=1-s`, the fixed-sector expansions checked in Note03 CB4
give, with epsilon matching the arm,

\[
\alpha(w_\epsilon)=b_\epsilon-\epsilon7i/(2z)+O(X^{-2}),\quad
\alpha'(w_\epsilon)=-\epsilon i/z+O(X^{-2}).
\tag{IP21}
\]

Let `g_epsilon=G(t,w_epsilon)/C_epsilon`. Then

\[
g_\epsilon=1+A_\epsilon+O_I(\Lambda^2/X^2),\quad
A_\epsilon=\frac{\epsilon i}{z}(1/24-7t b_\epsilon/4),
\]
\[
U_1(t,w_\epsilon)=B_\epsilon+O_I(\Lambda^2/X^2),\quad
B_\epsilon=-\frac{\epsilon i}{z}(t/4+t^2b_\epsilon^2/8).
\tag{IP22}
\]

Since `A_epsilon+B_epsilon=D_epsilon`, multiplication gives

\[
G(t,w_\epsilon)(1+U_1)-C_\epsilon(1+D_\epsilon)
 =C_\epsilon O_I(\Lambda^4/X^2).
\tag{IP23}
\]

The positive envelopes E_G and E_o are comparable on the full larger
chart. Only zero-time sectorial expansions and exact algebra were reused;
the old t>=32 *error theorem* was not invoked outside its domain.

The time calibration has a separate payment. Write exactly
`g_epsilon=exp(d0(z)+t d1(z))`, where
`d1=(alpha(w_epsilon)^2-b_epsilon^2)/4`. The gamma remainder gives
`d0=epsilon i/(24z)+O(X^-2)` and
`d1=-epsilon7i b_epsilon/(4z)+O(Lambda/X^2)` with no time-dependent
error coefficient. Alternatively, put `A=alpha^2/4,A0=b_epsilon^2/4`
and differentiate the exact finite expression. Division by C_epsilon gives

\[
\frac{\partial_t\{G(1+U_1)-C_\epsilon(1+D_\epsilon)\}}{C_\epsilon}
 =A\{g_\epsilon(1+U_1)-(1+D_\epsilon)\}
 +(A-A_0)(1+D_\epsilon)+g_\epsilon(U_1)_t-(D_\epsilon)_t.
\tag{IP24}
\]

Here
`A-A0=-epsilon7i b_epsilon/(4z)+O(Lambda/X^2)`,
`(U1)_t=-epsilon i(1+t b_epsilon^2)/(4z)+O(Lambda^2/X^2)`,
and exactly `(D_epsilon)_t=-epsilon i(1+7b_epsilon+t b_epsilon^2)/(4z)`.
All retained `1/z` terms cancel in the last three terms. IP23 and
these explicit bounds give `C E_o Lambda^6/X^2` for IP24. This does
not differentiate IP23's O allowance.

Apply [Cauchy's formula][cauchy] on disks of radius `1/(8 Lambda)`
inside `Omega_X^+`. Each C_epsilon has logarithmic z derivative
`O_I(Lambda)`, so E_o varies by a bounded factor on these disks.
The fixed center X and split U do not move. Equations IP20/IP23 give
spatial j0--3 at `C_j E_o Lambda^j tilde B1` on `Omega_X`.
IP19/IP24 give direct first time at `C E_o Lambda^2 tilde B1` there.
No fixed-radius transverse height loss or division by a cancelling
two-arm sum is introduced.

## 6. Exact corrected residual and its spatial derivative

Let `ell_epsilon=log C_epsilon` and

\[
Q_0(b)=21/16+t/8+5tb/8+t^2b^2/16,
\quad \ell_{\epsilon,z}=\epsilon i b_\epsilon/2
                     +(7/4+t b_\epsilon/4)/z,
\]
\[
R_\epsilon:=\operatorname{Res}(C_\epsilon)/C_\epsilon
 =\frac{\epsilon i(1+7b_\epsilon+t b_\epsilon^2)}{4z}
                         +\frac{Q_0(b_\epsilon)}{z^2}.
\tag{IP25}
\]

Direct product differentiation gives the exact residual

\[
\operatorname{Res}F_1=\sum_\epsilon C_\epsilon T_\epsilon,
\quad T_\epsilon=(1+D_\epsilon)R_\epsilon+(D_\epsilon)_t
           +2\ell_{\epsilon,z}(D_\epsilon)_z+(D_\epsilon)_{zz}.
\tag{IP26}
\]

The `1/z` part of R_epsilon is exactly cancelled by `(D_epsilon)_t`.
In particular,

\[
T_\epsilon=Q_0(b_\epsilon)/z^2+D_\epsilon R_\epsilon
       +2\ell_{\epsilon,z}(D_\epsilon)_z+(D_\epsilon)_{zz}.
\tag{IP27}
\]

On the fixed interval I,
`D=O(Lambda^2/X)`, `D_z=O(Lambda^2/X^2)`,
`D_zz=O(Lambda^2/X^3)`, `D_zzz=O(Lambda^2/X^4)`;
`R=O(Lambda^2/X)`, `R_z=O(Lambda^2/X^2)`,
`ell_z=O(Lambda)`, `ell_zz=O(1/X+Lambda/X^2)`.
Consequently `T=O(Lambda^4/X^2)` and
`T_z=O(Lambda^4/X^3)`. The exact derivative

\[
\partial_z\operatorname{Res}F_1
 =\sum_\epsilon C_\epsilon(\ell_{\epsilon,z}T_\epsilon
                                      +\partial_zT_\epsilon)
\tag{IP28}
\]

pays the last two IP4 rows. These are actual finite-formula residuals;
their smallness does not remove the arithmetic part of the field error.
The exact identity `(H-F1)_t=-(H-F1)_zz-Res F1` agrees with the
direct-time proof, but is not its only justification.

## 7. Finite constants and a sufficient height onset

Choose fixed nested sectors outside the negative real axis and an
`X_sec` covering the full fixed buffers. The finite gamma remainders
and the rational factors in M determine finite `C_a,C_beta,C_2,C_3`
in IP8--10, with `|a-L/2|<=C_a/X`. The same estimates integrated
along the ray determine `C_ray>=1` in IP16. Fixed enlarged-strip Euler
and Stirling constants determine a sufficiently large `C_m>=1` in
IP15/IP20, including all time weights. The finite normal moments through
six and `exp(33 C_beta^2/4)` determine IP11's constants. Choose a common
positive c_I in IP18 after absorbing the finitely many polynomial factors.
Sectorial calibration bounds determine a finite `C_cal` controlling
`|U1|,|D_epsilon|` by `C_cal Lambda^2/X`.

A sufficient X_* lies beyond all the following gates, holding at every
larger height, with S=34 and U=X^(1/3):

\[
\begin{gathered}
X\ge X_{\rm sec},\quad X\ge2(r+b+V+10),\quad L\ge1,
\quad L/2-C_a/X\ge0,\quad U\ge2V,\\
C_2U^2/(2X)+C_3U^3/X^2\le1,\quad C_{\rm cal}\Lambda^2/X\le1/4,\\
C_{\rm ray}+\tfrac12\log(X+U)\le U/(4S),\quad
U\ge4S(L/2+C_a/X),\\
(3/64)L^2\ge C_m(1+L)+2\log X,\qquad
c_I X^{2/3}\ge2\log X.
\end{gathered}
\tag{IP29}
\]

Every gate is eventual. Powers dominate logarithms, the negative local
powers vanish, and the quadratic L term dominates its linear terms.
Enlarge past the finitely many turning points or use a symbolic doubling
construction on these explicit majorants. This supplies a terminating
finite sufficient onset, not a numerically useful certified threshold.
On I, IP29 makes IP15/IP18 at most `C X^-2`; these are absorbed into
`Lambda^4/X^2`. Equations IP20--28 now give all IP4 statements.

The onset/constants depend on the fixed chart and on I. They are not
asserted uniform as the upper time tends to infinity or the lower time
tends to zero. For a uniform worst-time summary, `B1<=C X^(-3 log2/16)`
after a further eventual gate `Lambda^4/X^2<=X^(-3 log2/16)`.
The pointwise two-term B1 retains the better large-t local scale.

## 8. Both genuine overlaps, with their actual hypotheses

**Lower overlap `[3/4,1]`.** Note24 proves the canonical F0 comparison
on `[1/2,1]`, the same Omega_X and extra unit, after its finite onset.
Take the maximum of that onset and X_*. Both errors have the same H,
the same envelope and fixed branches. The triangle inequality gives

\[
|\partial_z^j(F_1-F_0)|\le C_jE_o\Lambda^j
 \{B_1+X^{-t\kappa}\}\le C_j'E_o\Lambda^jB_1,\quad j\le3,
\]
\[
|(F_1-F_0)_t|\le C E_o\Lambda^2B_1.
\tag{IP30}
\]

This is a positive-width common-H overlap, not just endpoint contact.
For an additional explicit compatibility check, the exact identity
`F1-F0=sum C_epsilon D_epsilon` gives the stronger bounds
`C E_o Lambda^(j+2)/X` for spatial j<=3 and
`C E_o Lambda^4/X` for time. These follow by differentiating the
displayed finite correction, not by identifying terms in two unrelated
canonical error expansions.

**Upper overlap `[32,33]`.** Note03's corrected pair and Note20's
rechecked `[32,T]` corrected pair are exactly IP3, with identical
logarithm/phase/normalization. Their fixed proof endpoints V need not be
identical: V does not occur in the elementary field. Thus the difference
between the two named F1 fields is identically zero, including jets
and direct time. Take the maximum of X_* and the actual Note20 onset
with T=33 and these same buffers. Note20 RB9 and its kernel-time proof
RB8a supply every imported spatial/time premise. Also

\[
X^{-t\kappa}\le X^{-8\log2}\le X^{-2}
\quad(32\le t\le33),
\tag{IP31}
\]

so IP4 reduces to its existing `E_o Lambda^(j+4)/X^2` and
`E_o Lambda^6/X^2` rates. The common-H triangle gives the same bounds
if the two theorem instances are kept as separate labels; the actual
formula equality is stronger. No missing buffer or direct-time premise
remains. No published small-t theorem is invoked on this upper overlap.

**Covered union, without a new splice.** The actual overlaps give a
high-height field atlas covering `[1/2,33]`: Note24's F0 on `[1/2,1]`
and this note's F1 on `[3/4,33]`. With Note20 on each fixed `[32,T]`,
it covers `[1/2,T]` for every fixed finite T>=33 after the maximum of
the relevant onsets. Constants/onsets can depend on T. This closes the
previously uncovered intermediate positive band at this buffered
high-height field scope. It is a domain union of proved models; no
assembled time-cutoff field is defined here. A future assembled field
would need its own cutoff derivative residual. In particular one must
not assign F1's smaller residual to an F0-to-F1 transition for free.
The existing Note20 overlap with the full gamma hierarchy retains its
own domain, envelope and paid time-interface terms.

## 9. Scope, source controls and next estimate

This is an approximation task under [avoid01][a01], not an RH-equivalent
criterion. Consult [result summaries][results], [heat-flow cluster11][r11],
[collision controls12][controls] and the [avoid index][avoid].
Euler-factor controls fail the unchanged canonical M-zeta completion and
its coefficients; weighted-square and finite-source controls fail exact
canonical xi completion IP5--7; smooth shape, positive-primitive and
reflected super-Gaussian controls fail the ordinary theta Dirichlet
series used in IP13; finite-prime/profile controls do not preserve the
complete canonical coefficient/reflection data of IP7. These specify
failed premises of this proof, not universal exclusions. No zero-sign
or RH conclusion follows from the field estimate alone.

**AN02 Complete/CLOSED at its frozen scope.** No requested estimate
remains unpaid, including both overlaps. Wider A08 and LT-07 are
Partial: a genuine strong bridge down to the shrinking signed window,
bounded-height core, physical transfer, growing-time/order uniformity,
useful height cost and independent full-chain audit remain separate.
Parent HDA-17 Partial, HDA-18 Gated, HDA-20 unfulfilled are unchanged.
The companion manuscript has not been updated by this research return.

Next **Analysis — Sol**: [A08-AN03 r1][next], prepared only, for a
complete retained-arithmetic comparison on the separate moving band
`4/L<=t<=1`, with genuine overlaps `4<=tL<=8` and `[3/4,1]`.
Its allowance must be derived from the complete source before accepting
a rate. The present n=1 omission budget `X^(-t kappa)` stays of constant
order when tL stays bounded, so this proof cannot supply a vanishing
allowance there merely by substitution. That failed bound is not a
lower-bound impossibility theorem for other arithmetic models.

[packet]: ../research-progress/handoffs/HDA-A08-AN02.md
[inputs]: 25_INTERMEDIATE_POSITIVE_INPUTS_20261026.json
[review]: ../reviews/19_INTERMEDIATE_POSITIVE_COMPARISON_ASSESSMENT_20261026.md
[work]: ../numerics/A08_AN02_ANALYTICAL_WORK_RECORD_20261026.json
[next]: ../research-progress/handoffs/HDA-A08-AN03.md
[pm]: https://arxiv.org/html/1904.12438v2#S4
[gamma]: https://dlmf.nist.gov/5.11#ii
[zeta]: https://dlmf.nist.gov/25.2.E1
[euler]: https://dlmf.nist.gov/25.2.E8
[cauchy]: https://dlmf.nist.gov/1.9.E31
[results]: ../../../../../result-summaries/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md

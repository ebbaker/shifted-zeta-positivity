# First small-positive slab: a complete buffered canonical comparison

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort
ultra**, base chat0025, thread `01a179ab-8856-7ba0-89a2-500b2d854c80`.

**Status: proved in-note from named classical inputs; same-model internal
assessment only.** This returns [HDA-A08-AN01 r1][packet]. On precisely
`1/2<=t<=1`, the elementary two-arm field has complete relative-envelope
allowance `X^(-t log(2)/4)`, uniformly at worst `X^(-log(2)/8)`, with
spatial orders0--3 and direct first time. Its exact nonzero heat residual
and residual_z are paid below. Constants and sufficient onsets are finite
analytical quantities, not numerical certificates. No research computation
or manuscript production was performed. [Inputs24][inputs] pins inputs;
[Assessment18][review] and the [work record][work] retain the checks.

## 1. Exact contract, charts and theorem

Use the unchanged complete theta source and normalization

\[
H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\qquad H_t=-H_{zz},\qquad H(0,z)=\xi(s(z))/8,
\quad s(z)=(1+iz)/2.
\tag{SP1}
\]

The physical `q=epsilon_g^2` and fixed averaging `K=k_ell k_h` are
unchanged. This note proves a field theorem, without a physical transfer.
Fix `ell,h>0`, put `r=ell+2`, `b=1+h+2`, and use

\[
\Omega_X=\{|\Re z-X|\le r,\ |\Im z|\le b\},\qquad
\Omega_X^+=\{|\Re z-X|\le r+1,\ |\Im z|\le b+1\}.
\tag{SP2}
\]

All scalar field estimates are first paid on the extra analytic unit
`Omega_X^+`. Take the logarithm continued from the positive real axis;
write `L_z=Log(z/(4pi))`, `L=log(X/(4pi))`, `Lambda=1+log X` and

\[
b_\pm=L_z/2\pm i\pi/4,\quad \kappa=\log2/4,\quad
\kappa_0=\log2/8,
\]
\[
C_\pm=\frac{\pi^{1/4}z^{7/4}}{32}
\exp\left[-\frac{\pi z}{8}
 +\frac t{16}(L_z^2-\pi^2/4)
 \ \pm i\left\{\frac z4(L_z-1)+\frac{\pi tL_z}{16}
                    +\frac{7\pi}{8}\right\}\right],
\quad F_0=C_++C_-,\quad E_o=|C_+|+|C_-|>0.
\tag{SP3}
\]

These are Note03's elementary arms, without its correction. `E_o`, not
`|F_0|`, pays cancellation and the full transverse buffer. On the real
axis it equals the positive cosine amplitude. Evenness gives the left
tail after the right tail is proved.

**Theorem.** For fixed `ell,h`, there are finite constants `C_j,C_t,C_R`
and a sufficient finite `X_*` constructed in Section7, such that for
`X>=X_*`, `z in Omega_X`, and `1/2<=t<=1`,

\[
|\partial_z^j(H-F_0)|\le C_j E_o\Lambda^j X^{-t\kappa},
\quad 0\le j\le3,\qquad
|(H-F_0)_t|\le C_t E_o\Lambda^2X^{-t\kappa}.
\tag{SP4}
\]
\[
|\operatorname{Res}F_0|\le C_R E_o\Lambda^2/X,\qquad
|\partial_z\operatorname{Res}F_0|\le C_R E_o\Lambda^3/X,
\quad\operatorname{Res}F=F_t+F_{zz}.
\tag{SP5}
\]

In particular all requested envelope-normalized allowances tend to zero
uniformly on this slab. A sharper field allowance is not inferred from
the smaller residual. No optimality or lower-bound theorem is asserted.

## 2. Canonical identity and complete fixed-endpoint split

The exact positive Gaussian identity, parent Note27 GO6 and
[Polymath equation35][pm], is

\[
H(t,z)=\int_{\mathbb R}K_t(v)\,\xi(s+v)/8\,dv,
\qquad K_t(v)=(\pi t)^{-1/2}e^{-v^2/t},\quad t>0.
\tag{SP6}
\]

It also follows directly by inserting SP1: the Gaussian average of
`cos((z-2iv)u)` is `e^(tu^2)cos(zu)`. Absolute Fubini is justified on
SP2 by the integrable majorant `e^(u^2+(b+1)u)|Phi(u)|`; the complete
theta source decays super-exponentially. This retains every source mode.
Polynomial weights for one time derivative remain integrable.

Set

\[
M(w)=\frac{w(w-1)}{16}\pi^{-w/2}\Gamma(w/2),\quad
\alpha(w)=M'(w)/M(w),\quad G(t,w)=M(w)e^{t\alpha(w)^2/4}.
\tag{SP7}
\]

Choose a fixed `Sigma` bounding `|Re w|` for `w=s,1-s` on SP2's larger
chart, and set `V=Sigma+3`. Then `Re(w+v)>=3` for `v>=V`. Split SP6 at
`-V,V` and reflect the negative ray by `xi(w)=xi(1-w)`. Exactly,

\[
\begin{split}
H={}&J_V(t,s)+J_V(t,1-s)+A_V(t,s)+A_V(t,1-s)+I_V(t,s),\\
J_V(t,w)={}&\int_V^\infty K_t(v)M(w+v)\,dv,\\
A_V(t,w)={}&\int_V^\infty K_t(v)M(w+v)(\zeta(w+v)-1)\,dv,\\
I_V(t,s)={}&\int_{-V}^V K_t(v)\xi(s+v)/8\,dv.
\end{split}
\tag{SP8}
\]

All defining endpoints are fixed in `t,z`. Thus the fields are
holomorphic and differentiation has no moving-endpoint term. No contour
is deformed in this proof, so no connectors arise. The negative-ray
reflection is exact; the enlarged middle is retained, not discarded.
Only the all-positive-time identity is imported from parent Note27;
its GO7 error theorem above64 and the t>=32 field theorems are not used
on this slab.

## 3. Local gamma estimate and the complete arithmetic population

All rays lie in a fixed sector away from the negative real axis once
`X` exceeds a buffer-dependent sector onset. The [sectorial gamma
remainder][gamma], rational factors in SP7, and Cauchy on a larger
sector give, uniformly in `w=s,1-s`,

\[
a=\Re\alpha(w)=L/2+O(X^{-1}),\quad
\beta=\Im\alpha(w)=O(1),\quad
\alpha'(w)=O(X^{-1}),\quad\alpha''(w)=O(X^{-2}).
\tag{SP9}
\]

Use the proof split `U=X^(1/3)`, with `X` the fixed chart parameter.
On `V<=v<=U`, Taylor's integral remainder gives

\[
\log M(w+v)=\log M(w)+\alpha(w)v+R(w,v),\qquad
|R(w,v)|\le C_\gamma v^2/X.
\tag{SP10}
\]

Increase the onset so `C_gamma U^2/X<=1`. Then
`|exp R-1|<=e C_gamma v^2/X`. For each fixed `k<=4`, completing the
real square gives

\[
\frac{\int_{\mathbb R}e^{-v^2/t+av}|v|^k\,dv}
 {\sqrt{\pi t}|e^{t\alpha^2/4}|}
 \le C_k\Lambda^k,\qquad 1/2\le t\le1.
\tag{SP11}
\]

Indeed the mean is `ta/2`, variance `t/2`, and the precise loss from
absolute to complex normalization is `exp(t beta^2/4)`, uniformly
bounded here. The full linear Gaussian integral equals
`sqrt(pi t)exp(t alpha^2/4)`: the identity for real alpha extends to
complex alpha by entire dependence and Gaussian domination. No contour
shift or omitted boundary is needed. Equations SP10--11 pay the local
gamma-curvature error by `C |G| Lambda^2/X`.

The ordinary [Dirichlet series][zeta] yields, for `sigma>=2`,

\[
|\zeta(\sigma+i\tau)-1|\le\sum_{n\ge2}n^{-\sigma}
 \le 2^{-\sigma}+\int_2^\infty x^{-\sigma}\,dx
 \le3\,2^{-\sigma}.
\tag{SP12}
\]

Thus *all* `n>=2` on the local ray are paid at once. Replace `a` by
`a-log2` in SP11; `|exp R|<=e`. Division by the complex carrier produces

\[
\exp\left[-\frac{ta\log2}{2}
 +\frac{t(\log2)^2}{4}+\frac{t\beta^2}{4}\right]
 \le C X^{-t\log2/4}.
\tag{SP13}
\]

The fixed factor `2^(-Re w)` is absorbed in the buffer constant. This
is a bound for the complete arithmetic remainder, with no truncation
of its population and no changed coefficients. At these small times it
cannot be silently absorbed into the `Lambda^2/X` gamma allowance.

## 4. Lower completion, bounded middle and both infinite ends

The missing linearized integral `v<V`, after division by `G`, is bounded
by

\[
C\exp[-tL^2/16+C_m(1+L)].
\tag{SP14}
\]

For `a>=0`, its numerator is at most
`exp(aV) integral_R exp(-v^2/t)dv`. The same argument includes any
of the polynomial weights through degree2 needed for direct time.
SP9 gives the denominator `exp(t(a^2-beta^2)/4)` and hence SP14.

For the true middle, all real parts of `s+v` lie in a fixed bounded
interval. Reflection, where needed, moves them into `[1/2,D]` for one
finite buffer-dependent `D`. Euler summation [DLMF25.2.8][euler] with
integer `N=ceil X` gives `|zeta(w)|<=C X` there, since
`|Im w|` is comparable to `X`. For example the finite sum is at most
`N`, the pole term is bounded by `C N^(1-Re w)/X`, and the integral
remainder by `C X N^(-Re w)/(Re w)`. Bounded-real-part Stirling then
gives

\[
|\xi(w)/8|\le C X^{m_B}e^{-\pi X/8}
\tag{SP15}
\]

for a finite exponent `m_B` depending on the *whole* buffer and `V`.
The carrier has modulus
`exp(-pi X/8+tL^2/16+O_B(1+L))`. Consequently the entire bounded
middle, including its time-kernel derivative, also satisfies SP14.
No small-strip fourth-power bound is substituted for SP15.

For the infinite ends, integrate the real logarithmic derivative of
`M(w+v)` along each horizontal ray. Fixed-sector estimates give a
finite `C_ray` such that for all `v>=0`,

\[
\log\frac{|M(w+v)|}{|M(w)|}
 \le C_{\rm ray}v+\frac v2\log(X+v).
\tag{SP16}
\]

If `C_ray+(1/2)log(X+U)<=U/4`, monotonic decrease of
`[C_ray+(1/2)log(X+v)]/v` for `v>=U` gives an upper bound `v^2/4`
on SP16. Here `C_ray` can be increased to be positive. Since `t<=1`,
the Gaussian leaves at least `exp(-3v^2/4)` on the entire infinite ray.
Therefore both true gamma ends beyond `U` and their linearized ends
are at most

\[
C |G|\exp(-c X^{2/3}).
\tag{SP17}
\]

For the linearized ends use `|a|<=C Lambda` and `U>=C Lambda` at the
onset. For the true arithmetic ends SP12 is bounded by a fixed constant,
so SP17 pays those ends too. Polynomial kernel-derivative weights are
absorbed by reducing the positive `c` once. Carrier division in SP16
retains the crucial height exponential; a global absolute source moment
before this division would not establish SP17.

Combining SP8--17 proves the full gamma-pair field allowance

\[
\left|H-G(t,s)-G(t,1-s)\right|
 \le C\{ |G(t,s)|+|G(t,1-s)|\}\mathcal B(t,X),
\]
\[
\mathcal B(t,X)=\Lambda^2/X+X^{-t\kappa}
 +e^{-tL^2/16+C_m(1+L)}+e^{-cX^{2/3}}.
\tag{SP18}
\]

This is a fresh fixed-slab estimate, not a parameter substitution into
a theorem whose time interval was different.

## 5. Explicit arms, jets and direct first time

Note03 CB4's fixed-sector expansions of the actual `M,alpha` give

\[
\log\frac{G(t,s)}{C_+}
 =\frac{i}{24z}-\frac{7it b_+}{4z}+O_B(\Lambda/X^2),
\qquad G(t,s)/C_+=1+O_B(\Lambda/X).
\tag{SP19}
\]

Reflection gives the lower arm with the conjugate signs. This use of
sectorial expansions does not import CB9's restricted-time field error.
The two positive envelopes are comparable on all of SP2, and SP19 is
below SP18's gamma allowance. Thus SP18 holds with `F_0,E_o`.

For `z in Omega_X`, apply Cauchy's formula on the disk of radius
`rho=1/(8 Lambda)` inside `Omega_X^+`. Each arm has logarithmic
derivative `O(Lambda)`, so its modulus, hence `E_o`, varies by a bounded
factor on that disk. The chart center `X` and the proof split `U` remain
fixed. This gives

\[
|\partial_z^j(H-F_0)|\le C_jE_o\Lambda^j\mathcal B(t,X),
\quad0\le j\le3.
\tag{SP20}
\]

For a **direct first-time** comparison, differentiate the exact fixed
kernel in SP8, before estimating:

\[
\partial_t K_t(v)=K_t(v)\left(v^2/t^2-1/(2t)\right).
\tag{SP21}
\]

Dominated convergence follows from the same Gaussian/gamma ray bounds,
uniformly on a slightly larger positive time interval. The full
linearized integral differentiates exactly to `G_t=alpha^2 G/4`.
Since `t>=1/2`, SP21 costs at most two additional Gaussian moments.
Local gamma, full local arithmetic, missing/middle, and infinite ends
cost respectively

\[
C|G|\Lambda^4/X,\quad C|G|\Lambda^2X^{-t\kappa},\quad
C|G|e^{-tL^2/16+C_m(1+L)},\quad C|G|e^{-cX^{2/3}},
\tag{SP22}
\]

with the constants `C_m,c` chosen once for both field and time. The
time derivative of the explicit SP19 calibration follows from
`G_t=alpha^2G/4`, `C_{\pm,t}=b_\pm^2 C_\pm/4` and
`alpha-b_+=O(1/X)` (and reflection). It is at most
`C E_o Lambda^3/X`, within `C E_o Lambda^2 mathcal B`. Hence

\[
|(H-F_0)_t|\le C E_o\Lambda^2\mathcal B(t,X).
\tag{SP23}
\]

No big-O allowance is differentiated and no moving endpoint is hidden.
There is also a consistency check using the exact identity
`(H-F_0)_t=-(H-F_0)_{zz}-Res F_0`, once Section6 is paid. It agrees
with SP23 but is not a substitute for the direct source calculation.

## 6. Exact heat residual

Put `ell_\pm=log C_\pm`. Direct differentiation of SP3 gives

\[
\ell_{\pm,z}=\frac{\pm i b_\pm}{2}
 +\frac{7/4+t b_\pm/4}{z},\quad
\ell_{\pm,t}=b_\pm^2/4,\quad (b_\pm)_z=1/(2z),
\]
\[
Q_0(b)=\frac{21}{16}+\frac t8+\frac{5tb}{8}+\frac{t^2b^2}{16},
\qquad
R_\pm=\frac{\pm i(1+7b_\pm+t b_\pm^2)}{4z}
              +\frac{Q_0(b_\pm)}{z^2},
\]
\[
\operatorname{Res}F_0=\sum_\pm C_\pm R_\pm,\qquad
\partial_z\operatorname{Res}F_0
 =\sum_\pm C_\pm(\ell_{\pm,z}R_\pm+\partial_zR_\pm).
\tag{SP24}
\]

These are exact algebraic identities, re-bounded on the new slab.
Here `R_\pm=O(Lambda^2/X)`, `R_{\pm,z}=O(Lambda^2/X^2)` and
`ell_{\pm,z}=O(Lambda)`, which prove SP5. A model with a small residual
need not approximate the canonical field; SP6--23 supply that missing
canonical source comparison here.

## 7. Constants, sufficient onset and named final rate

Fix a sector, for example `|arg(w/2)|<=3pi/4`, and a slightly larger
sector for holomorphic remainder estimates. Choose `X_sec` so every
buffered ray lies there with `|w|` comparable to `X` near its origin.
The finite-truncation constants in DLMF5.11, explicit rational factors
of `M`, and the fixed buffer determine finite constants in SP9--10 and
SP16; name `C_a` so `|a-L/2|<=C_a/X`. Take `C_gamma` to dominate `X|alpha'(w+q)|/2` for `0<=q<=U`;
the sector bounds give one common finite choice beyond `X_sec`.
Take `C_ray` from the upper real logarithmic derivative used in SP16.
Take `C_m>=1` larger than the finite bounded-strip polynomial exponents,
missing-piece constants and the time weights in Section4. The constants
in SP11 are bounded normal moments with mean `ta/2` and the uniform
factor `exp(t beta^2/4)`. This specifies finite analytical constants
without any data fit or numerical research.

A sufficient `X_*` is any height beyond all these gates, holding for
every larger height:

\[
\begin{gathered}
X\ge X_{\rm sec},\quad X\ge2(r+b+V+10),\quad L\ge1,\quad L/2-C_a/X\ge0,
\quad U\ge2V,\quad C_\gamma U^2/X\le1,\\
C_{\rm ray}+\tfrac12\log(X+U)\le U/4,
\quad U\ge2L+4C_a/X,\\
\Lambda^2/X\le X^{-\kappa},\qquad
L^2/32\ge C_m(1+L)+\kappa\log X,\qquad
cX^{2/3}\ge\kappa\log X.
\end{gathered}
\tag{SP25}
\]

The last majorant on the second line bounds `4 sup_w |Re alpha(w)|`
on the fixed largest chart by SP9. All gates are eventual; powers beat logarithms, `kappa<1`, and the
quadratic `L` term beats its linear terms. One can enlarge the threshold
past the finitely many turning points, or double a symbolic candidate
until these sufficient majorants hold. This terminates analytically.
It is not a calculated affordable height. Gates may be enlarged once
for the endpoint calibration below.

For `1/2<=t<=1`, SP25 bounds every term of `mathcal B` by
`C X^(-t kappa)`: in the middle use `t>=1/2`, and in the other two
comparisons use `t<=1`. Thus SP20/SP23 give SP4, with uniform worst
power `kappa_0`. All absolute derivatives of order<=3 still tend to
zero after division by `E_o`, since any fixed logarithmic power is
dominated by `X^(-kappa_0)`. The normalized residual statements follow
likewise. Constants depend on the declared buffers and this fixed slab.

## 8. Endpoint comparison: what is imported and what is proved afresh

The signed crossover in Note04 requires `|t|L<=8`. At `t=1/2` this
forces `L<=16`; it supplies no all-height overlap with SP4. No join
through zero is concluded.

For the published cutoff-free two-arm model write

\[
M^{\rm PM}_0(w)=\frac{w(w-1)}{16}\pi^{-w/2}\sqrt{2\pi}
 \exp\{(w/2-1/2)\Log(w/2)-w/2\},
\]
\[
\alpha_0(w)=\frac1{2w}+\frac1{w-1}+\tfrac12\Log(w/(2\pi)),
\quad M^{\rm PM}_t=M^{\rm PM}_0e^{t\alpha_0^2/4},\quad
P^{\rm PM}=M^{\rm PM}_t(s)+M^{\rm PM}_t(1-s).
\tag{SP26}
\]

[Polymath Proposition9.1(i)][pm9] states its two-arm comparison on
`0<t<=1/2`, `|y|<=10`, `x>=200`, `x>=exp(C/t)`, with qualitative
allowance `x^(-ct)` for an absolute positive `c`. At `t=1/2`, this
gives a genuine restricted-strip common-`H` comparison after both
onsets. Spatial derivatives imported by Cauchy require interior strip
margin. That source statement alone does not pay arbitrary larger
buffers or a first-time derivative. Its finite-RS effective theorem
has still different hypotheses; no derivative of a varying floor cutoff
is used here.

For this request's **full buffers**, supply the missing calibration
afresh. Fixed-sector Stirling and its holomorphic remainder give

\[
\log(M/M^{\rm PM}_0)=1/(6w)+O(X^{-3}),\quad
\alpha-\alpha_0=-1/(6w^2)+O(X^{-4}),
\]
\[
\log(G/M^{\rm PM}_t)=O(X^{-1})+O(t\Lambda/X^2)=O(X^{-1})
\quad(1/2\le t\le1).
\tag{SP27}
\]

There are no zeros or branch-cut crossings in these fixed high-height
sectors. Thus SP18 plus SP27, followed by the same buffered Cauchy
argument, proves **a new** full-buffer `H-P^PM` field/spatial comparison
at SP4's allowance. This is derived from SP6, not an extension of
Proposition9.1 by citation.

Its time comparison is also paid. Put
`D=alpha_0+(t/2)alpha_0 alpha_0'`; exact differentiation gives

\[
\operatorname{Res}P^{\rm PM}
 =\tfrac14\sum_{w=s,1-s}M^{\rm PM}_t(w)
       \{\alpha_0(w)^2-D(w)^2-D'(w)\}.
\tag{SP28}
\]

Since `alpha_0=O(Lambda)`, `alpha_0'=O(1/X)`,
`alpha_0''=O(1/X^2)`, SP28 and its z derivative are bounded by
`C E_o Lambda^2/X` and `C E_o Lambda^3/X`. The exact identity
`(H-P^PM)_t=-(H-P^PM)_{zz}-Res P^PM` then proves its first-time
comparison, without differentiating a published error term. Therefore,
**through their common canonical H**, at `t=1/2` on `Omega_X`
(with scalar calibration first on `Omega_X^+`),

\[
|\partial_z^j(F_0-P^{\rm PM})|\le C_jE_o\Lambda^jX^{-\kappa_0},
\quad j\le3,\qquad
|(F_0-P^{\rm PM})_t|\le C E_o\Lambda^2X^{-\kappa_0}.
\tag{SP29}
\]

On `|y|<=10` after its source onset this is compatible with the
published comparison. On wider buffers the payment is our fresh
SP27--28 plus SP18, explicitly distinguished from that import. There is
no unpaid buffer or endpoint defect in SP29. There is no positive-width
time overlap with a theorem whose upper endpoint is1/2; an assembled
time splice or continuation below1/2 remains separate.

## 9. Scope, controls and disposition

This is an asymptotic approximation under [avoid01][a01], not an
RH-equivalent criterion. It adds an explicit arithmetic power, full
fixed-buffer jets/time and an elementary-model residual on this slab;
no priority claim about fixed-positive-time asymptotics is made.
The [result index][results], [heat-flow cluster11][r11],
[collision controls12][controls] and [avoid index][avoid] govern scope.

The collision controls do not defeat this source-specific approximation:
Euler-factor controls fail the unchanged canonical `M zeta` completion
and its ordinary coefficients; weighted-square/finite-source controls fail the
exact canonical xi completion SP6--8; reflected super-Gaussian and smooth
shape/primitive controls fail theta's ordinary Dirichlet series; finite
prime/profile controls fail the complete coefficient/reflection data
used in SP8. Merely positive/even sources are never used to infer a
zero-exclusion theorem here. These are failed premises of this proof,
not universal exclusions of control families. No zero-sign claim follows
from the approximation alone.

**AN01 closes at its frozen bounded scope.** All listed source,
arithmetic, completion, fixed-endpoint, middle, infinite-end, shift,
spatial, direct-time and residual estimates are paid. No first unpaid
estimate remains *inside this request*. The wider A08 status is Partial:
the range above1 up to32, a paid join to its existing corrected model,
a strong near-zero overlap, physical transfer, bounded-height core,
large-time uniformity, useful height cost and independent audit are not
established here. Parent HDA-17 Partial, HDA-18 Gated and HDA-20
unfulfilled remain unchanged. The maintained manuscript was not edited.

Next **Analysis — Sol**: [A08-AN02 r1][next], prepared only, for a
separate fixed `[3/4,33]` field comparison and genuine open overlaps
with this slab and the existing `[32,33]` corrected model. Its rates
are targets until that packet is executed. The present proof is not
itself a claim that the wider gap or join has closed.

[packet]: ../research-progress/handoffs/HDA-A08-AN01.md
[next]: ../research-progress/handoffs/HDA-A08-AN02.md
[inputs]: 24_SMALL_POSITIVE_SLAB_INPUTS_20261026.json
[review]: ../reviews/18_SMALL_POSITIVE_SLAB_ASSESSMENT_20261026.md
[work]: ../numerics/A08_AN01_ANALYTICAL_WORK_RECORD_20261026.json
[pm]: https://arxiv.org/html/1904.12438v2#S4
[pm9]: https://arxiv.org/html/1904.12438v2#S9
[gamma]: https://dlmf.nist.gov/5.11#ii
[zeta]: https://dlmf.nist.gov/25.2.E1
[euler]: https://dlmf.nist.gov/25.2.E8
[results]: ../../../../../result-summaries/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md

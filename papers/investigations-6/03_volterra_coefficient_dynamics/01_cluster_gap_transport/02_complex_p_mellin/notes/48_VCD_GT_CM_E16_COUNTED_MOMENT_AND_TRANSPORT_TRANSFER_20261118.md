# E16 r4 — Counted coordinates, complete moments and transport transfer

18 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Author-selected executor label:
**gpt-6.1-sol / ultra**. This records the requested selection, not an
independent attestation of the serving model or effort; such metadata
were unavailable to this executor.

**Status: proved in-note from the common-time field-error input stated
below; internal nonauthor E40 assessment pending.** This is the
contour/consumer component of [E16 r4][request], retaining the full
[r1 contract][contract]. Its seven current source pins were checked:
all byte counts and SHA-256 values in [the r4 manifest][pins] matched.
This note owns steps 4–6; [Note47][field] owns the field approximation,
growth constants and initial inverse-square tail. No canonical zeros,
source values, contour clearances or gap anchors are acquired here.

| Task | Type | Recommended model | Dependency | Output |
| --- | --- | --- | --- | --- |
| E16 r4, steps 4–6 | E — execution | Sol; fixed contour and error calculation | Note47's common initialization and jet errors | Explicit fixed-height coordinate, complete-moment and consumer errors |
| E40 | E — execution | Sol; bounded nonauthor assessment | Frozen Notes47–48 | Internal proof assessment; no specialist independence |

This is a quantitative approximation milestone, measured by its error
and stated information requirements, and is not an RH-equivalent
criterion. See the [result index][results], specifically
[Cluster18][cluster], and the [avoid index][avoid], specifically
[classification01][class], [premises02][premises] and [scope07][scope].
The [B05 decision][decision] selected this finite-divisor approximation;
it did not select independent truncation of the S/T moment head.

## 1. Fixed canonical input and the field-error interface

Retain exactly the complete theta source and physical equation
`H_t=-H_zz` of [manuscript Section1][framework]. Fix

\[
 I=[t_0,t_1]\subset[0,1/2],\quad T\ge64,\quad L=\log T,
 \quad \ell=L^{-1},\quad r_0=a\ell,
 \quad \max(2,4\sqrt d)\le a\le L.
\]

An **independently established** conjugation-invariant count-two tube
on all of I supplies continuous symmetric coordinates

\[
 c(t)\in[T,2T],\quad D(t)\in\mathbb R,\quad
 |D(t)|\le d\ell^2\le r_0^2/16,
 \quad z_\pm=c\pm\sqrt D.
 \tag{1}
\]

The two target occurrences have `|z_±−c|≤r0/4`. Every other occurrence
has `|ρ−c|≥r0`. Both signs of D, a target double zero, arbitrary
exterior multiplicities, and exterior-exterior mergers are allowed.
A target-exterior merger would violate this already supplied collar
and is outside the stated tube. The complete canonical strip, unit
upper count, order-at-most-one growth and even product inputs are
those in Section1; the count is with integer multiplicity. No all-real
exterior is assumed. There is no extension to a negative-time tube or
to the separate E38 example.

At t0, let `P_N(t0,z)` be the **single** canonical opposite-pair product
cut off at modulus N, retaining all ties, conjugates and occurrences,
normalized by `H(t0,0)>0`. Evolve this same polynomial on all of I by
`exp(−(t−t0)∂z²)`. No reinitialization at chart boundaries is made.
The input from Note47 is the quantitative assertion, for a fixed disk
large enough to contain all contours below,

\[
 \sup_{t\in I,\ |z|\le R}|\partial_z^j(P_N-H)(t,z)|
       \le\varepsilon_j=C_jE_N,\quad 0\le j\le3,
 \qquad E_N=\sum_{\text{omitted opposite pairs}}|\rho|^{-2}
       =O(\log N/N).
 \tag{2}
\]

The sum convention and initial count constants belong to Note47.
Use its explicit field constant (21) and proved jet estimate (23),
not an unexecuted proposed Gaussian estimate. Its Cauchy interface is
`C_j=j! h_pad^(−j) C(R+h_pad,t1−t0)` for
any fixed positive spatial padding `h_pad`; `h_pad` is unrelated to
the contour floor h below. The calculations here work for arbitrary
supplied errors ε_j, including additional finite-data errors, before
specializing to `C_j E_N`. Thus this note does not infer a quantitative
rate from qualitative convergence.

## 2. Two fixed circles per chart and matching of the target pair

Choose finitely many closed real subcharts `K_α` whose relative
interiors cover I, and reference times `t_α`, so that

\[
 \zeta_\alpha=c(t_\alpha),\qquad
 |c(t)-\zeta_\alpha|\le r_0/32\quad(t\in K_\alpha).
 \tag{3}
\]

Continuity of the supplied canonical tube and compactness of I give
such a finite refinement. They do not supply numerical values for its
clearances. Use the positively oriented, time-independent circles

\[
 \Gamma^-_\alpha=\{|z-\zeta_\alpha|=3r_0/8\},\qquad
 \Gamma_\alpha=\{|z-\zeta_\alpha|=r\},\qquad r=r_0/2.
 \tag{4}
\]

Every target lies within `9r0/32` of ζ_α and every exterior occurrence
lies at distance at least `31r0/32`. Each circle therefore encloses
exactly the **same canonical target occurrences**, with clearance.
Define the finite input constants

\[
 h_\alpha=\min_{K_\alpha\times(\Gamma^-_\alpha\cup\Gamma_\alpha)}|H|>0,
 \qquad
 K_{j,\alpha}=\max_{K_\alpha\times\Gamma_\alpha}|\partial_z^jH|,
       \quad 1\le j\le3.
 \tag{5}
\]

The explicit Rouché threshold `ε0≤h_α/2` gives two polynomial zeros,
with multiplicity, inside **each** circle. Thus the polynomial target
inside the outer circle is already confined to the companion inner
disk. On an overlap `K_α∩K_β`, (3) gives
`|ζ_α−ζ_β|≤r0/16`; the whole α inner disk lies strictly inside the
β outer disk, since `3r0/8+r0/16=7r0/16<r0/2`.
The α pair is therefore the β pair: the latter has count only two.
This proves chart matching without labelling roots. Arbitrary unrelated
count-two contours would not give this conclusion.

Consequently the polynomial has a unique selected count-two pair on I
consistent with these charts; its symmetric coordinates `c_N,D_N`
agree on overlaps. Both fields factor on each outer disk as

\[
 H=Q_*A,\qquad P_N=Q_{*,N}A_N,
 \quad Q_*=(z-c)^2-D,\quad Q_{*,N}=(z-c_N)^2-D_N,
 \tag{6}
\]

where A and A_N are analytic and nonzero there, including the target
multiplicities. Polynomial division by the complete counted quadratic,
or the argument-principle elementary symmetric functions, proves (6).
Local complex-time continuation follows from the same fixed curves;
the real subchart formulas suffice for the bounds. Since P_N has real
coefficients and each disk is conjugation invariant, its selected pair
is conjugation invariant and `c_N,D_N` are real. A choice of a square
root is never required.

## 3. Logarithmic derivative and symmetric-coordinate errors

For a single outer chart suppress α, put
`B=H_z/H`, `B_N=(P_N)_z/P_N`, and use h,K_j from (5). On its circle,

\[
 |B_N-B|\le b_1,\qquad
 b_j:=\frac{\varepsilon_j}{h-\varepsilon_0}
       +\frac{K_j\varepsilon_0}{h(h-\varepsilon_0)}
       \quad(1\le j\le3),\qquad |B|\le K_1/h=:K_B.
 \tag{7}
\]

This follows by subtracting the two quotients and uses only
`|P_N|≥h−ε0`. The radius-normalized integral
`⟨f⟩=(2πi)^(−1)∮_Γ f dz` obeys `|⟨f⟩|≤r sup_Γ|f|`.
With `u=z−ζ`, set `I_k=⟨u^kB⟩`, and analogously `I_{k,N}`.
The argument principle gives

\[
 c=\zeta+I_1/2,\quad D=I_2/2-(c-\zeta)^2,
 \qquad |I_{k,N}-I_k|\le r^{k+1}b_1.
\]

Thus the following **explicit, local-coordinate** errors avoid any
unnecessary factor c or T from using absolute power sums:

\[
 |c_N-c|\le e_c:=r^2b_1/2,
 \qquad
 |D_N-D|\le e_D:=r^3b_1/2+(r_0/16)e_c+e_c^2.
 \tag{8}
\]

On Γ, let `u_*:=17r0/32`. Then `|z−c|≤u_*`, and

\[
 |Q_*|\ge q:=\frac{161}{1024}r_0^2,
 \quad |Q_{*,N}-Q_*|\le e_Q:=2u_*e_c+e_c^2+e_D.
 \tag{9}
\]

Indeed `|z−c|≥15r0/32`, and `|D|≤64r0²/1024`.
Require the additional explicit threshold `e_Q≤q/2`; then
`|Q_{*,N}|≥q/2` and every straight interpolation between Q_* and
Q_{*,N} stays at least q/2 from zero on Γ. On the companion circle
the canonical quadratic floor is `57r0²/1024`; no differentiation or
rational integration on that circle is needed.

For completeness, the first physical-time coordinate jets are paid by
the same four field jets. Put

\[
 A_j=K_j/h,\quad A_{j,N}=(K_j+\varepsilon_j)/(h-\varepsilon_0),
 \quad b_t=b_3+A_{2,N}b_1+A_1b_2.
\]

Both heat equations imply `B_t=−H_zzz/H+(H_z/H)(H_zz/H)` and its
polynomial counterpart, whence `|(B_N)_t−B_t|≤b_t`.
In particular

\[
 |c_N'-c'|\le e_{c'}:=r^2b_t/2,\quad
 |c'|\le C_{c'}:=r^2(A_3+A_1A_2)/2,
\]
\[
 |D_N'-D'|\le r^3b_t/2+(r_0/16)e_{c'}
                   +2e_c(C_{c'}+e_{c'}).
 \tag{10}
\]

These estimates include `D=0` and `D_N=0`. They are ordinary symmetric
coordinate errors and make no assertion of uniformly Lipschitz
individual square roots through a merger.

Here is a fully explicit **N threshold and linear-rate version** of
(7)–(9). If (2) holds, define

\[
 b=2C_1/h+2K_1C_0/h^2,\quad
 A_c=r^2b/2,\quad
 A_D=r^3b/2+(r_0/16)A_c+A_c^2,
\]
\[
 A_Q=2u_*A_c+A_c^2+A_D,
 \qquad
 E_*^{(\alpha)}=\min\{1,h/(2C_0),q/(2A_Q)\}.
 \tag{11}
\]

A quotient by a zero constant imposes no restriction. For
`E_N≤min_α E_*^(α)`, all Rouché and denominator conditions hold,
and `b1≤b E_N`, `e_c≤A_cE_N`, `e_D≤A_DE_N`,
`e_Q≤A_QE_N`. This is a computable threshold **from supplied
constants**; no size or feasibility claim about an acquired canonical
N is made. With `K=5C_u`, a sufficient purely explicit cutoff test is
`2K[log(2+N)+1]/N≤min_α E_*^(α)`, by Note47 (12).

## 4. Complete exterior traces, including all polynomial exterior roots

Define the exterior moments for H exactly as in [Note09][hierarchy],
and for P_N using **every** polynomial occurrence outside its selected
pair:

\[
 S_n=\sum_{\rm ext}((\rho-c)^2-D)^{-n}\quad(n\ge1),
 \qquad T_k=\sum_{\rm ext}(\rho-c)((\rho-c)^2-D)^{-k}\quad(k\ge2).
 \tag{12}
\]

The canonical sums converge absolutely by its complete upper count,
strip and collar. The polynomial sums are finite; no strip or global
root confinement is required for the evolved polynomial. In particular,
neither sum is being replaced by an unmentioned finite canonical
exterior cutoff.

Both fields have the exact local formulas

\[
 S_n=-\langle Q_*^{-n}B\rangle,\qquad
 T_k=-\langle(z-c)Q_*^{-k}B\rangle,
 \tag{13}
\]

with the corresponding N coordinates and B_N for the polynomial.
The following residue argument pays the analytic-factor issue in (6):
local nonvanishing of A alone would not identify its derivatives with
complete exterior moments.

For `R(z)=Q_*^(−n)` or `(z−c)Q_*^(−k)`, every kernel pole is among
the two selected targets and is inside Γ. Moreover `R=O(z^(−2))`
or `O(z^(−3))` at infinity. For an exterior occurrence ρ, the rational
function `R(z)/(z−ρ)` has no residue at infinity; all its poles other
than ρ are inside Γ. Therefore

\[
 \langle R(z)/(z-\rho)\rangle=-R(\rho).
 \tag{14}
\]

The **combined** contribution of both selected occurrences is zero:
`R Q_*'/Q_*` has only the enclosed target poles and decays faster
than `1/z`. This remains true at a double target, when those poles
coalesce. It is not an assertion that each simple target residue
separately vanishes. Also `⟨R⟩=0`.

For a polynomial, its complete partial fractions and (14) prove (13).
For H, use its globally established even order-at-most-one canonical
product, with one factor per opposite pair and multiplicities. Its
regularized logarithmic derivative converges normally on Γ; constants
in `1/(z−ρ)+1/ρ` integrate to zero against R. The possible linear
exponential prefactor is constant by evenness (even an additional
constant logarithmic derivative would integrate to zero). The
inverse-square tail pays termwise integration, and the right sides of
(14) sum absolutely. This proves (13) for the **complete** canonical
divisor. No artificial outer contour and no uncontrolled residue at
infinity of B has been discarded; the only uses of infinity concern
the displayed individual rational functions. The companion inner
contours in §2 are what make the target identification across charts
and all these kernel poles legitimate.

Let

\[
 U_n=(2/q)^n,\qquad V_n=n(2/q)^{n+1}.
\]

The straight interpolation in (9) gives
`|Q_N^(−n)−Q^(−n)|≤V_n e_Q`. Applying (7) and (13) gives the
following explicit perturbed-kernel bounds on each whole subchart:

\[
 |S_{n,N}-S_n|\le e_{S_n}:=
 r\{U_nb_1+K_BV_ne_Q\},\qquad n\ge1,
 \tag{15}
\]

\[
 |T_{k,N}-T_k|\le e_{T_k}:=
 r\{(u_*+e_c)U_kb_1
       +K_B(e_cU_k+u_*V_ke_Q)\},\qquad k\ge2.
 \tag{16}
\]

The first term uses the perturbed kernel with `B_N−B`; the second
uses the kernel difference with B. Thus both the coordinate errors
and the changing denominators have been paid. Under (11), explicit
linear constants are

\[
 C_{S_n}^{(\alpha)}=r(U_nb+K_BV_nA_Q),
\]
\[
 C_{T_k}^{(\alpha)}=
 r\{(u_*+A_c)U_kb+K_B(A_cU_k+u_*V_kA_Q)\}.
 \tag{17}
\]

Taking the maximum over the finite cover proves, for each fixed n,k,
uniform errors at most `C_Sn E_N`, `C_Tk E_N` on I. Together with
(8), these are `O(log N/N)` at the fixed height, fixed tube and fixed
moment orders. Their constants depend explicitly on the contour
floors and retained orders; there is no simultaneous height, time
horizon or order limit.

Exterior-exterior mergers cause no singularity in (13)–(17), since
their poles stay outside the fixed contours. A double target causes
no singularity since Q_* rather than a labelled square root is used.
The complete finite polynomial hierarchy of Note09 therefore applies
to this actual polynomial divisor, and its fixed-row identities pass
to the canonical field. Alternatively their first-time-jet passage
follows directly from (7),(10),(13) and the finite rational kernel
derivatives, with the same positive floors. Arbitrary moment-sequence
well-posedness is not claimed.

## 5. Physical and normalized forcing; every-subinterval costs

Use different symbols for physical and normalized forcing:

\[
 M=S_1,\quad \mathcal F=12S_2+16DS_3,\quad
 M_t=2M^2-\mathcal F,\quad D_t=2-4DM;
\]
\[
 \sigma=(t-t_0)/\ell^2,\quad \delta=D/\ell^2,
 \quad s_n=\ell^{2n}S_n,\quad v_k=\ell^{2k-1}T_k,
 \quad m=\ell^2M,\quad F=\ell^4\mathcal F=12s_2+16\delta s_3.
 \tag{18}
\]

All these definitions are also used for P_N. Let e_c,e_D,e_Sn,e_Tk
now be their maxima over the finite cover. The physical errors obey

\[
 e_M=e_{S_1},\quad
 |\mathcal F_N-\mathcal F|\le e_{\mathcal F}:=
 12e_{S_2}+16\{d\ell^2e_{S_3}+e_D(A_3^{\rm mom}+e_{S_3})\},
 \tag{19}
\]

where, for example, `A_3^mom=B_3 L ell^(−6)` is the canonical absolute
moment bound of [manuscript Section6][transport]. A direct contour
upper bound for `sup|S3|` is equally valid. The perturbation product
in (19) is retained. Consequently

\[
 |m_N-m|\le\eta:=\ell^2e_M,\quad
 |F_N-F|\le\ell^4 e_{\mathcal F},\quad
 |\delta_N-\delta|\le e_D/\ell^2,
\]
\[
 |s_{n,N}-s_n|\le\ell^{2n}e_{S_n},\qquad
 |v_{k,N}-v_k|\le\ell^{2k-1}e_{T_k}.
 \tag{20}
\]

No inherited polynomial collar bound is needed to obtain these errors;
its complete moments are already the traces. In particular one may
transfer a **proved** polynomial forcing upper bound `F_N≤Q_N`
to `F≤Q_N+ell^4 e_mathcalF`, but (19) itself supplies no improved
signed upper bound.

Let `Σ=(t1−t0)/ell²`. For **every** `0≤x≤y≤Σ`, define

\[
 W(x,y)=\exp\{-4\int_x^ym(v)\,dv\},\qquad
 W_N(x,y)=\exp\{-4\int_x^ym_N(v)\,dv\}.
\]

These are positive because m,m_N are real. Uniformity of (20) proves

\[
 |\log W(x,y)-\log W_N(x,y)|\le4\eta(y-x),
\]
\[
 e^{-4\eta(y-x)}W_N(x,y)\le W(x,y)
     \le e^{4\eta(y-x)}W_N(x,y),
 \quad |W-W_N|\le(e^{4\eta(y-x)}-1)W_N.
 \tag{21}
\]

This is a whole subinterval statement, not only the single multiplier
from t0 to t1. In physical time its logarithmic error is equivalently
`4e_M(v−u)` on every `[u,v]⊂I`.

The exact **physical D** inhomogeneous cost in these coordinates is

\[
 \mathcal C_D(x,y)=2\ell^2\int_x^yW(v,y)\,dv,
 \quad
 D(t_0+\ell^2y)=W(x,y)D(t_0+\ell^2x)+\mathcal C_D(x,y).
 \tag{22}
\]

Thus the required physical factor is `ell²`; the corresponding δ cost
is `mathcalC_D/ell²`. Applying (21) on every `[v,y]` gives

\[
 |\mathcal C_D-\mathcal C_{D,N}|
 \le2\ell^2\int_x^y
        (e^{4\eta(y-v)}-1)W_N(v,y)\,dv
 \le(e^{4\eta(y-x)}-1)\mathcal C_{D,N}(x,y).
 \tag{23}
\]

This also gives multiplicative upper and lower cost enclosures with
factors `exp(±4η(y−x))`. If an absolute a priori bound is wanted,
`|m_N|≤A:=B_1L+η` gives, with `h=y−x` and
`Ψ(b,h)=∫_0^h exp(bv)dv` (continuous at b=0),

\[
 |\mathcal C_D-\mathcal C_{D,N}|
 \le2\ell^2\{\Psi(4(A+\eta),h)-\Psi(4A,h)\}.
 \tag{24}
\]

All bounds are uniform for `h≤Σ`. For fixed inputs the right sides
are `O(E_N)`, and are finite even through either discriminant zero.
The canonical absolute moment bound used here is an input already
proved in Section6; it is not an all-real bound.

A supplied incoming anchor with error `α_x` propagates by (22), with
the additional errors bounded by
`W(x,y) α_x + |W−W_N| |D_N(x)| + |mathcalC_D−mathcalC_D,N|`.
A supplied terminal lower anchor A_y proves `D(x)≥0` if
`A_y≥mathcalC_D,N(x,y)+` the upper cost error in (23), since W>0.
These are explicit consumers for **independent** anchor information.
Neither anchor, its sign or its strict margin, nor the full tube on
which the comparison is valid, is acquired by approximation. In
particular equality cases and vanishing discriminants are retained.

## 6. Finite closure and exactly which finite data it requires

Write `J=J_N` for the number of retained opposite pairs **counting
occurrences**, so the initial polynomial has degree `2J`. A conservative
description of its initial data is H(t0,0) and J nonzero complex
representatives ρ_ν, with negation pairing, conjugation closure,
multiplicities and the complete cutoff/tie information. Equivalently,
the real-even polynomial has J+1 real coefficients

\[
 P_N(t_0,z)=\sum_{k=0}^J a_{2k}z^{2k}
 =H(t_0,0)\prod_{\nu=1}^J(1-z^2/\rho_\nu^2).
 \tag{25}
\]

The inherited unit upper count gives, for instance,
`2J≤(2⌈N⌉+1) C_u log(3+⌈N⌉)` by covering the projected interval
`[−N,N]` with unit bands. This is an upper data count, not an acquired
canonical zero list. The exact real-even coefficient closure is

\[
 a_{2k}'=-(2k+2)(2k+1)a_{2k+2},\quad a_{2J}'=0,
\]
\[
 a_{2k}(t_0+\tau)=\sum_{r=0}^{J-k}
 \frac{(-\tau)^r}{r!}\frac{(2k+2r)!}{(2k)!}a_{2k+2r}(t_0).
 \tag{26}
\]

This is an actual finite-dimensional realization with all of its own
higher divisor moments, rather than independent zero values for the
unretained S/T rows. Multiplicity changes cause no singularity in
(26). The common finite initial divisor, the normalization, a complete
tail bound E_N, the canonical source identities and the independent
contour/tube constants are all required inputs. A fixed prescribed
short moment head does not determine these finite coefficients or
the canonical omitted tail; no such theorem is asserted.

Finite supplied-data errors are paid without guessing root labels
during the evolution. If `|hat a_(2k)−a_(2k)|≤ξ_k`, the error between
the two polynomial heat fields on `0≤τ≤Δ=t1−t0`, `|z|≤R` obeys

\[
 \varepsilon_j^{\rm data}\le
 \sum_{k=0}^J\xi_k
 \sum_{r=0}^{\lfloor(2k-j)/2\rfloor}
 \frac{\Delta^r}{r!}\frac{(2k)!}{(2k-2r-j)!}R^{2k-2r-j},
 \quad 0\le j\le3,
 \tag{27}
\]

where a negative upper summation limit gives zero and `0^0=1`.
Replace ε_j in §§2–5 by `C_jE_N+ε_j^data`. The Rouché and denominator
thresholds must hold for these **total** errors; convergence needs
the supplied-data contribution to tend to zero as well. No uniform
conditioning in J is asserted. For the real multiplier and positive
cost statements in §5 the supplied polynomial is required to retain
real even coefficients; equivalently its factor data must preserve
conjugation and opposite pairing exactly. This symmetry of the data
is not inferred from a small complex error.

For initial location errors `|hatρ_ν−ρ_ν|≤e_ν<|ρ_ν|`, set
`b_ν=|ρ_ν|^(−2)` and

\[
 d_\nu=\frac{e_\nu(2|\rho_\nu|+e_\nu)}
                 {|\rho_\nu|^2(|\rho_\nu|-e_\nu)^2}.
\]

Then `|hatρ_ν^(−2)−ρ_ν^(−2)|≤d_ν`. If the normalization error is
at most e_a, a sufficient coefficient error in (27) is

\[
 \xi_k=e_a e_k(b+d)+|H(t_0,0)|\{e_k(b+d)-e_k(b)\},
 \tag{28}
\]

where e_k is the elementary symmetric polynomial in the J nonnegative
entries and e_0=1. Expanding products and telescoping proves (28).
This presumes that the complete occurrence count and tie selection are
correct; a missing zero or wrong integer multiplicity is not merely
a small location error. Certified acquisition of such data would need
its own count proof. No such numerical task is part of E16.

## 7. Equal-information direct comparison and collision controls

Given exactly the same initial finite divisor, coefficient evolution,
tail and supplied-data errors, direct residues evaluate

\[
 S_{n,N}=\sum_{\rm all\ polynomial\ ext}Q_{j,N}^{-n},\quad
 T_{k,N}=\sum_{\rm all\ polynomial\ ext}w_{j,N}Q_{j,N}^{-k},
 \quad \mathcal F_N=\sum_{\rm ext}(12Q_{j,N}^{-2}+16D_NQ_{j,N}^{-3}).
 \tag{29}
\]

Equations (13) and (29) are identical finite rational traces, including
their signed cancellations. The canonical errors (15)–(24) belong to
either evaluation. The contour implementation can avoid assigning
individual exterior labels, but that observation is not a measured
runtime saving, a stronger sign or a smaller cost. Conversely, taking
absolute values separately in (29) while preserving joint signs in
(13) would compare unequal information. Any claim about a superior
algorithm would require a declared computational model and measured
or proved cost; this note makes none.

The [Controls12][controls] screen is a consistency check on the stated
premises, following [avoid02][premises], rather than an attempted
collision exclusion. Its bookkeeping is as follows.

| Control class | Premise for the literal canonical application that is absent, or retained generic scope |
| --- | --- |
| Euler-factor translates `Φ_(c,p)` | They change the unchanged complete theta initial field; some generic order/count and approximation premises can survive, so approximation must preserve their actual collisions on an eligible tube. |
| Weighted-square, finite-source, finite-score and finite-prime changes | They lack full unchanged normalized theta data or reflection. Their endpoint-defective subclasses also lack the supplied global strip. No lower population asymptotic is used in this theorem; merely having a smaller population is not a failure of its upper-count premise. |
| Reflected super-Gaussian | It lacks the order-at-most-one canonical-product/growth input used by Note47; positivity and full reflection alone are not enough. |
| Smooth positive-shape and positive-primitive controls | They change the theta source and have no supplied canonical strip/count transfer. If a member independently meets the generic growth and contour assumptions, the approximation theorem applies to it and does not exclude its collision. |
| Atomic threshold and finite-profile controls | They change exact theta data. Generic exponential-type growth, upper counts, imaginary-shift evolution and local contour hypotheses can hold for these controls; the approximation proof then preserves their collisions. No nonexistent lower-count premise is invoked. |
| RH-conditional normalized endpoint controls | They change ordinary Dirichlet arithmetic and retain RH in their construction. Fixed-compact approximation supplies no escaping-height uniform limit. |
| Changed observation kernels or fractional profiles | The former lose the fixed physical cosine/Newman readout; the latter lack the integer-occurrence divisor realization. |
| Static divisor surgery or arbitrary scalar/moment sequences | The former supply no unchanged canonical common-time source evolution; the latter need not realize any divisor or polynomial heat field. |
| Counter-kernels `q,q_(T,a)`, smooth-density and two-channel screens | No identification with the unchanged complete theta source/product is supplied. These controls stop their named shape or factor estimating classes. Whenever a counter-kernel supplies its own generic growth, divisor and Gaussian inputs, this approximation applies to it and preserves its collision. |

The decisive finite-polynomial control is exact, not a floating sample.
For b>0 take the [Note09][hierarchy] quartic

\[
 P(\tau,z)=(z^2-b^2)^2-\tau(12z^2-4b^2)+12\tau^2,
 \qquad P_\tau=-P_{zz}.
 \tag{30}
\]

At τ=0 the two occurrences at +b merge and the two exterior occurrences
at −b merge. On a sufficiently small interval about zero they admit
the required separated two-pair contour charts; choose any fixed small
r0 relative to b. In this **generic polynomial control**, initialize
at the left endpoint and take N larger than all initial root moduli.
The complete opposite-pair product is then this polynomial itself
up to its prescribed scalar; hence `E_N=0`, all four field errors
are zero, and every coordinate, complete moment, multiplier and cost
transfer above is exact through the collision. It therefore verifies
the requested target and exterior merger consistency simultaneously.
The canonical positive-time slab is not being claimed for this changed
source: translate the control's time origin if a nonnegative displayed
interval is desired. The actual collision does not violate any
approximation conclusion. An independent strict positive gap margin
at that event would fail. No check of this control is evidence for RH.

## 8. Return, scope and work limit

This one proof pass supplies the requested fixed-height finite-cover
Rouché threshold, unique chart matching, complete perturbed rational
traces, physical/normalized forcing errors, every-subinterval multiplier
and physical inhomogeneous D-cost errors, finite coefficient closure,
finite input count and supplied-data sensitivity. The explicit rate
is `O(E_N)=O(log N/N)` using Note47's common-time field estimate.
One proof pass and one bounded local clarification made the exact
real symmetry requirement for supplied-data cost errors explicit;
no structural premise was changed. No canonical numerical data were produced, and no
manuscript, source, shared status, history or investigation ledger was
edited by this component.

The rate is conditional on the stated fixed tube and its contour
clearances; this note does not acquire or prolong them. It does not
improve a signed canonical forcing bound, recover an independent gap
anchor, establish arbitrary-sequence stability or assert a uniform
height/order limit. These are scope boundaries, not impossibility
claims about other closure or arithmetic methods [scope07][scope].
Any change of source, heat sign, finite-divisor approximation, limit
regime or a new structural premise would return to B05 before dependent
work. The existing E40 bounded nonauthor assessment is the next check;
no new numerical campaign follows from this proof.

[request]: ../research-progress/handoffs/VCD-GT-CM-E16-r4.md
[contract]: ../research-progress/handoffs/VCD-GT-CM-E16-r1.md
[pins]: ../research-progress/handoffs/VCD-GT-CM-E16-inputs-r4.json
[field]: 47_VCD_GT_CM_E16_COMMON_TIME_FIELD_APPROXIMATION_20261118.md
[decision]: 15_VCD_GT_CM_B05_BBGKY_TRUNCATION_RECONSIDERATION_20261118.md
[hierarchy]: 09_VCD_GT_CM_E10_REGULAR_ODD_EVEN_HIERARCHY_20261118.md
[framework]: ../manuscript/sections/01_framework.tex
[transport]: ../manuscript/sections/06_bounds_transport.tex
[results]: ../../../../../../result-summaries/README.md
[cluster]: ../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[avoid]: ../../../../../../avoid/README.md
[class]: ../../../../../../avoid/01_restating_the_target.md
[premises]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md

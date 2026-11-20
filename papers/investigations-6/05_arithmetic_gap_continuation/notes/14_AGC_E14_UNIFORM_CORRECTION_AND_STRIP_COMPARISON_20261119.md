# AGC-E14 r1: uniform correction and complete pointwise comparison

19 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex LLM assistance. The root explicitly recorded dispatch **gpt-6.1-sol / ultra** for this execution helper; independent serving-backend model and effort attestation is unavailable. This is Type E under the [frozen request](../research-progress/handoffs/AGC-E14-r1-request.md), following [B03's decision](13_AGC_B03_UNIFORM_FAMILY_DECISION_20261119.md). One analytical derivation and one correction pass; no numerical computation, campaign, parameter search or source change.

**Status: proved in-note; separate nonauthor assessment pending.** All six targets below hold, with the necessary explicit equality at the zero-height endpoint of the mismatch chain. The result is a uniform source/interface theorem and a complete allowance comparison. It acquires no positive strip floor, zero exclusion, new coverage or Newman bound.

The inputs are [Notes10](10_AGC_E13_R2_HOLOMORPHIC_CORRECTION_20261119.md)–[12](12_AGC_CORRECTED_MILESTONE_AND_CONTINUATION_20261119.md), [Review05](../reviews/05_AGC_CORRECTED_REFERENCE_ASSESSMENT_20261119.md), [Review06](../reviews/06_AGC_CORRECTED_COMPARISON_ASSESSMENT_20261119.md), B03 r1 and manuscript Sections5–9. The [result index](../../../../result-summaries/README.md), [pattern index](../../../../avoid/README.md), [Controls12](../../../../result-summaries/12_collision_controls_and_screening.md), and patterns [01](../../../../avoid/01_restating_the_target.md), [02](../../../../avoid/02_shape_only_arguments_and_the_controls.md), [07](../../../../avoid/07_scoped_exclusions_read_as_universal.md), [11](../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md) and [12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) govern interpretation. Classification: a bounded estimate/comparator milestone, quantified by the constants and complete allowance gain below, rather than an RH-equivalent reformulation. The missing arithmetic acquisition is stated in §6 and is not presented as evidence for positivity.

Selected imports were reopened in [Polymath, arXiv:1904.12438v2](https://arxiv.org/html/1904.12438v2): (53), the real-phase bound (58), the full remainder (59), (68), Corollary6.4 and Theorem1.2. They agree with the accepted Note10 normalization. Only these selected inputs were checked; no full-paper audit or independent proof of the imported source theorem is claimed.

## 1. Fixed family and full phase

Keep the literal theta field $H_t=-H_{zz}$, the accepted fixed-index $P_N$, and exactly

\[
\frac9{100}\le t\le\frac1{10},\quad x\ge14000,\quad |y|\le1,
\quad z=x+iy,\quad k=\frac\pi8,
\quad r=w_0=\frac x2+kt\ge7000,\quad w=r+iy/2,
\]
\[
N=\left\lfloor\sqrt{r/(2\pi)}\right\rfloor,
\qquad p_N(v)=2N+1-2\sqrt{v/(2\pi)}.
\tag{1}
\]

Every square root below is principal in $\Re v>0$. Suppress the index on $p_N$ when fixed, and use Note10's exact functions

\[
C(p)=\frac{e^{i\pi(p^2/2+3/8)}-i\sqrt2\cos(\pi p/2)}{2\cos(\pi p)},
\qquad C^\sharp(p)=\overline{C(\bar p)},
\]
\[
A_N(v)=\frac{\sqrt v}{2}\{(v+i)C(p_N(v))+(v-i)C^\sharp(p_N(v))\},
\quad J_N(t,z)=(-1)^{N+1}\frac{\sqrt\pi}{4}e^{-kz-k^2t},
\]
\[
C_N^{\rm val}=J_N A_N(r),\quad C_N^{\rm hol}=J_N A_N(w),
\qquad Q_N^{\rm val}=P_N-C_N^{\rm val},\quad
Q_N^{\rm hol}=P_N-C_N^{\rm hol}.
\tag{2}
\]

At every half-integer $p=j+1/2$, $j\in\mathbb Z$, the two terms in C's numerator are equal because

\[
e^{i\pi(p^2/2+3/8)}=i(-1)^{j(j+1)/2}
=i\sqrt2\cos(\pi j/2+\pi/4).
\tag{3}
\]

The last equality follows from the four residue classes modulo4. These are all the zeros of the denominator, and all are simple. The quotient therefore extends holomorphically at each of them. Its numerator and denominator are even; hence its extension is entire and even. Conjugation gives the same conclusions for $C^\sharp$.

Here is a uniform bound that does not exclude any apparent pole. On the boundary of

\[
\mathcal P=\{|\Re p|\le5/4,\ |\Im p|\le1/4\},
\]

the numerator modulus is less than5: its two terms are at most $e^{5\pi/16}<e<3$ and $\sqrt2\cosh(\pi/8)<2$. For the latter, use $\pi/8<2/5$, $\sqrt2<3/2$, and the power-series bound $\cosh u\le(1-u^2/2)^{-1}$, giving $\cosh(2/5)\le25/23$. The elementary series estimate $e<3$ also suffices here. On the vertical edges,

\[
|2\cos(\pi p)|\ge\sqrt2>5/4;
\]

on the horizontal edges it is at least $2\sinh(\pi/4)>\pi/2>5/4$. We used

\[
|\cos(\pi(a+ib))|^2=\cos^2(\pi a)+\sinh^2(\pi b).
\]

Thus $|C|<4$ on that boundary. The removable singularities have already been filled, so the maximum principle gives $|C|<4$ on all of $\mathcal P$. The same argument applies to $C^\sharp$. Every closed disk of radius1/5 centered in

\[
\mathcal P_{\rm in}=\{|\Re p|\le101/100,\ |\Im p|\le1/100\}
\]

lies strictly inside $\mathcal P$. Cauchy's formula consequently proves

\[
|C|,|C^\sharp|<4,\qquad
|C'|,|(C^\sharp)'|<20,\qquad
|C''|,|(C^\sharp)''|<200
\quad\hbox{on }\mathcal P_{\rm in}.
\tag{4}
\]

No physical phase window is lost. In a natural cell, $N\le\sqrt{r/(2\pi)}<N+1$, so $p_N(r)\in(-1,1]$. The endpoint $-1$ is the old cell's one-sided limit. On the whole segment $v=r+is$, $|s|\le|y|/2$,

\[
|p_N'(v)|=\frac1{\sqrt{2\pi}\,|\sqrt v|}
\le\frac1{\sqrt{2\pi r}},\qquad
|p_N(v)-p_N(r)|\le\frac1{2\sqrt{2\pi r}}<\frac1{400},
\tag{5}
\]

since $2\pi r>42000>40000$. Thus the segment lies in $\mathcal P_{\rm in}$, also when the old seam value is $-1$ or the new seam value is $+1$. This covers every natural phase and both one-sided endpoints.

For each fixed index, $P_N$, $J_N$, $C_N^{\rm hol}$ and $Q_N^{\rm hol}$ are holomorphic in $z$ on the right half-plane, with conjugation symmetry: $p_N(\bar v)=\overline{p_N(v)}$ and the sharp terms exchange. The uniform derivative estimates asserted next apply to the natural chart and its stated one-sided endpoints, rather than to an index kept arbitrarily far outside its natural chart. $C_N^{\rm val}$ and $Q_N^{\rm val}$ are pointwise value formulas, with no holomorphy assertion. The natural-index selection of $Q_N^{\rm hol}$ is not asserted globally holomorphic or a global heat solution.

## 2. Uniform derivatives, defect and mismatch

Put $a=101/100$ and

\[
B(v)=\frac{(v+i)C(p(v))+(v-i)C^\sharp(p(v))}{2},
\qquad A_N(v)=\sqrt v\,B(v).
\]

On the vertical segment, $r\le|v|\le r+1/2$, $|v\pm i|\le r+3/2<ar$, and $|\sqrt v|<a\sqrt r$. Also, $2\pi>25/4$ gives

\[
|p'|<\frac2{5\sqrt r},\quad |p''|<\frac1{5r^{3/2}},\quad
|(\sqrt v)'|\le\frac1{2\sqrt r},\quad
|(\sqrt v)''|\le\frac1{4r^{3/2}}.
\tag{6}
\]

All product and chain terms are retained in

\[
B'=\frac{C+C^\sharp}{2}
+\frac{p'}2\{(v+i)C'+(v-i)(C^\sharp)'\},
\]
\[
B''=p'\{C'+(C^\sharp)'\}
+\frac12\sum_{\nu=\pm1}(v+\nu i)
\{C_\nu''(p')^2+C_\nu'p''\},
\quad C_+=C,\ C_-=C^\sharp.
\tag{7}
\]

Equations (4)–(7) give

\[
|B|<4ar,\qquad |B'|<4+8a\sqrt r,\qquad
|B''|<32a+\frac{16+4a}{\sqrt r}.
\tag{8}
\]

Applying $A'=g'B+gB'$ and $A''=g''B+2g'B'+gB''$, $g=\sqrt v$, yields

\[
|A|<4a^2r^{3/2},\qquad
|A'|<8a^2r+6a\sqrt r,
\]
\[
|A''|<32a^2\sqrt r+(24a+4a^2)+\frac{a+4}{\sqrt r}.
\tag{9}
\]

These imply exactly the contracted constants. To display rational checks without numerical estimation, use $\sqrt r>80$, $r>6400$, and $a<41/40$:

\[
4a^2<4(41/40)^2<5,
\]
\[
8a^2+\frac{6a}{\sqrt r}
<8(41/40)^2+\frac{6(41/40)}{80}<9,
\]
\[
32a^2+\frac{24a+4a^2}{\sqrt r}+\frac{a+4}{r}
<32(41/40)^2+\frac{24(41/40)+4(41/40)^2}{80}
+\frac{41/40+4}{6400}<34<40.
\]

Consequently, uniformly on each stated segment and endpoint,

\[
\boxed{|A_N(v)|<5r^{3/2},\qquad |A_N'(v)|<9r,
\qquad |A_N''(v)|<40\sqrt r.}
\tag{10}
\]

Use $\mathscr R_P=P_{N,t}+P_{N,zz}$ for the **heat defect**, distinct from the physical source allowance in §3. At fixed $N$, $J_t=-k^2J$, $J_z=-kJ$, $w_t=k$, $w_z=1/2$, hence

\[
(JA)_t=J(-k^2A+kA'),\qquad
(JA)_{zz}=J(k^2A-kA'+A''/4).
\]

It follows exactly that

\[
\boxed{\mathscr R_Q=\mathscr R_P-J_NA_N''/4,\qquad
|\mathscr R_Q|\le|\mathscr R_P|+10\sqrt r\,|J_N|.}
\tag{11}
\]

There is no favorable signed cancellation assumption in the second inequality. For $E=H-Q^{\rm hol}$, $E_t+E_{zz}=-\mathscr R_Q$; in backward time $u=t_*-t$, $E_u=E_{zz}+\mathscr R_Q$.

The two corrections have the same factor $J_N(t,z)$. Integrating only the $A_N$ factor vertically and using (10) therefore gives

\[
|C_N^{\rm hol}-C_N^{\rm val}|\le M_N,
\quad M_N=\frac92r|y|\,|J_N|,
\quad L=\frac{|J_N|}{2}\sqrt r\sqrt{r^2+1}>0.
\tag{12}
\]

Exactly,

\[
\frac{M_N}{L}=\frac{9\sqrt r\,|y|}{\sqrt{r^2+1}}
\le\frac{9|y|}{\sqrt r}<\frac{|y|}{9}\le\frac19
\quad(y\ne0),
\qquad M_N=0\quad(y=0).
\tag{13}
\]

Here $\sqrt r>81$. The frozen request's strict middle inequality is literally false at $y=0$, where both sides equal0; (13) records this endpoint explicitly. The globally required $M_N/L<1/9$ is strict everywhere. No constant, threshold or family has changed.

## 3. Complete physical source budget

For completeness, retain both full term-error sums in the accepted convention. Put $T=x/2$, $\eta=|y|$, $\sigma_\pm=(1\pm\eta)/2$, $s_\pm^{\rm src}=\sigma_\pm+iT$, $a_{\rm RS}=\sqrt{r/(2\pi)}$, and

\[
\epsilon_n(t,s)=\exp\left(
\frac{(t^2/8)|\alpha(s)-\log n|^2+t/4+1/6}{T-3.33}
\right)-1,
\]
\[
\delta_\sigma=\left(\frac{0.397\,9^\sigma}{a_{\rm RS}-0.865}
+\frac5{3(T-6)}\right)e^{3.49/(T-4)},\qquad
S_N=\sum_{n=1}^N\sum_{\nu=\pm}
|p_n(t,s_\nu^{\rm src})|\epsilon_n(t,s_\nu^{\rm src}).
\tag{14}
\]

Write $\mathcal E_N^{\rm val}=S_N+L(\delta_{\sigma_-}+\delta_{\sigma_+})$, the source remainder called $R_N^{\rm val}$ in the packet. This is not $\mathscr R_Q$. Define the three complete source budgets

\[
V_{\rm om}=\mathcal E_N^{\rm val}+L,
\qquad V_{\rm val}=\mathcal E_N^{\rm val},
\qquad V_{\rm hol}=\mathcal E_N^{\rm val}+M_N.
\tag{15}
\]

The accepted principal-phase identity in Note10 is

\[
\mathfrak M_0(ir)U(r)e^{i\pi/8}
=-\frac{\sqrt\pi}{8}e^{-\pi r/4}\sqrt r(r+i).
\tag{16}
\]

It makes the source's correction precisely $J_NA_N(r)$, and its omitted leading payment precisely $L=e^{k^2t}|\mathfrak M_0(ir)|$. Rechecking (53), (59), (68) and Corollary6.4 confirms its sign, factor two and entire retained remainder. Conjugation supplies $y<0$ without changing a physical absolute-value budget. The source's domain contains (1), so Corollary6.4 and (12) prove

\[
\boxed{|H-Q_N^{\rm val}|\le V_{\rm val},\qquad
|H-Q_N^{\rm hol}|\le V_{\rm hol},\qquad
|H-P_N|\le V_{\rm om}.}
\tag{17}
\]

No term-replacement sum or part of either delta is discarded. Equation (13) gives

\[
V_{\rm om}-V_{\rm hol}=L-M_N>8L/9.
\tag{18}
\]

This is a source-only saving of the leading payment. It is neither a final nonvanishing margin nor a percentage improvement of the whole budget.

## 4. A complete allowance gain and its exact comparator

For real $p\in[-1,1]$, source (58) gives $|C(p)|\le1/2$. The needed real-part information can be proved elementarily. Put $q=|p|$, $a_1=q-1/2$, $b_1=(q+1/2)/2\in[1/4,3/4]$. Since $a_1b_1=q^2/2-1/8$, taking the real part of (2) gives

\[
\Re C(p)=\frac{\sin(\pi a_1b_1)}{2\sin(\pi a_1)},
\tag{19}
\]

with continuous value $b_1/2$ at $a_1=0$. For $u=\pi|a_1|\in[0,\pi/2]$, the ratio is $\sin(b_1u)/(2\sin u)$. It is positive. The function $v\cot v$ is strictly decreasing on $(0,\pi)$, since its derivative is $(\sin v\cos v-v)/\sin^2v<0$; the numerator is negative because $(v-\sin v\cos v)'=2\sin^2v>0$. Thus

\[
\partial_u\log\frac{\sin(b_1u)}{\sin u}
=b_1\cot(b_1u)-\cot u\ge0.
\]

The ratio also increases in $b_1$, since $b_1u\le3\pi/8<\pi/2$. Its maximum on this enclosing rectangle is $\sin(3\pi/8)/2=\cos(\pi/8)/2$. Including $u=0$ by continuity proves

\[
\boxed{0<\Re C(p)\le\tfrac12\cos(\pi/8).}
\tag{20}
\]

For real $r$, $A_N(r)=\sqrt r\{r\Re C(p_N(r))-\Im C(p_N(r))\}$. Combining (20) and $|\Im C|\le1/2$ therefore yields

\[
\frac{|C_N^{\rm val}|}{L}
\le\frac{r\cos(\pi/8)+1}{\sqrt{r^2+1}}
\le\cos(\pi/8)+\frac1r<\frac{37}{40}.
\tag{21}
\]

The last constant needs no optimization: $\sqrt2<99/70$, because $99^2>2\cdot70^2$, and

\[
2+99/70<(231/125)^2
\quad(239\cdot15625=3734375<3735270=53361\cdot70).
\]

Hence $\cos(\pi/8)=\sqrt{2+\sqrt2}/2<231/250$. Finally $37/40-231/250=1/1000>1/7000\ge1/r$. This proves (21), also at both real seam phases.

Define **complete exact-reference lower allowances**, using the entire budgets (15):

\[
m_{\rm om}=|P_N|-V_{\rm om},\quad
m_{\rm val}=|Q_N^{\rm val}|-V_{\rm val},\quad
m_{\rm hol}=|Q_N^{\rm hol}|-V_{\rm hol}.
\tag{22}
\]

Reverse triangle and (21) prove

\[
m_{\rm val}-m_{\rm om}
=|P_N-C_N^{\rm val}|-|P_N|+L
\ge L-|C_N^{\rm val}|>3L/40.
\tag{23}
\]

This is a gain in a **complete** lower allowance after changing its reference, rather than merely a saved remainder. On the other hand, for any valid independent triangle payment $M_N\ge|Q_N^{\rm hol}-Q_N^{\rm val}|$,

\[
|Q_N^{\rm hol}|\le|Q_N^{\rm val}|+M_N,
\qquad\boxed{m_{\rm hol}\le m_{\rm val}.}
\tag{24}
\]

Thus the holomorphic lift with this separately paid vertical triangle step cannot improve the equally informed **exact pointwise retained-value allowance**. The direct calculation receives $Q^{\rm val}$, all correction/source information and the same lower-bound information. The conclusion does not compare finite implementation costs, arbitrary interval enclosures, signed correlated residuals, counted-pair readouts or heat transport. Any already accepted local contour result remains intact. Dividing (23)–(24) by the same positive carrier modulus preserves both conclusions. Neither asserts $m_{\rm val}>0$.

## 5. Every natural-cutoff interface

At the seam $r=2\pi m^2$, or $x=4\pi m^2-\pi t/4$, call index $m-1$ old and $m$ new, and set $d_m=p_m(t,s_+(z))+p_m(t,s_-(z))$ in the manuscript's holomorphic arguments. Then $P_m-P_{m-1}=d_m$, $J_{m-1}=-J_m$, $p_m(r)=1$, $p_{m-1}(r)=-1$. Evenness of both phase functions gives $A_m(r)=A_{m-1}(r)$. With $\Delta Q=Q_{\rm new}-Q_{\rm old}$, the exact signed jumps are therefore

\[
\boxed{\Delta Q^{\rm val}=d_m-2J_mA_m(r),}
\qquad
\boxed{\Delta Q^{\rm hol}=d_m-J_m\{A_m(w)+A_{m-1}(w)\}.}
\tag{25}
\]

The two off-axis $A$'s are not identified. Equation (5) bounds their one-sided seam phases separately. The source inequalities for the old excluded endpoint follow by continuity from its natural cell: keep $t,y$ fixed and take $x\uparrow4\pi m^2-\pi t/4$. Every fixed-index function and every complete budget has the corresponding finite limit. The new index owns the seam itself. Both errors are measured against the same continuous $H$; consequently

\[
|\Delta Q^{\rm val}|\le V_{{\rm val,old}}+V_{{\rm val,new}},
\qquad
|\Delta Q^{\rm hol}|\le V_{{\rm hol,old}}+V_{{\rm hol,new}}.
\tag{26}
\]

An application may retain (25) exactly instead of this sum. Across any change of fixed reference,

\[
E_{\rm new}=E_{\rm old}-\Delta Q,
\qquad |E_{\rm new}|\le|E_{\rm old}|+|\Delta Q|.
\tag{27}
\]

Every successive seam is payable; a fixed analytic chart kept beyond its natural range instead needs the exact full reference difference paid and cannot inherit (10) there automatically. Heat/contour arguments use fixed holomorphic references with these transfers. No derivative of a floor or global piecewise heat equation without seam distributions is asserted. The selected pointwise consumer simply treats half-open natural cells and their one-sided endpoints separately.

## 6. Named strip consumer and the independent missing input

Select only Theorem1.2(ii) of the checked Polymath revision at

\[
t_0=1/10,\quad y_0=1/5,\quad X=14000,
\qquad x\ge14000+\sqrt{24/25},\quad
1/5\le y\le\sqrt{4/5}.
\tag{28}
\]

The existing carrier $\mathcal B_t(z)=\mathfrak M_t(s_-(z))$ is nonvanishing. A useful independently acquired arithmetic input would be a proved lower function

\[
\ell(t_0,x,y)\le|Q_N^{\rm val}(t_0,z)/\mathcal B_{t_0}(z)|,
\qquad
\ell(t_0,x,y)>V_{\rm val}(t_0,x,y)/|\mathcal B_{t_0}(z)|
\quad\hbox{at every point of (28)}.
\tag{29}
\]

It must bound the full arithmetic sum by an independent argument, with finite-height/tail joins, every natural cell and every endpoint covered. A finite computation, if later authorized, needs a proved tail beyond its finite height; an asymptotic statement needs its effective onset and paid join. No such acquisition or split is supplied here. Defining $\ell$ to be the desired margin would not acquire (29). No positive unscaled infimum over unbounded $x$ is requested; normalization by the carrier removes the irrelevant exponential decay.

The finite band $14000\le x<14000+\sqrt{24/25}$ lies outside (ii); coverage there is separate. Specifically, input(iii) requires the whole barrier

\[
14000\le x\le14000+\sqrt{24/25},\quad0\le t\le1/10,
\quad\sqrt{6/25-2t}\le y\le\sqrt{1-2t}.
\tag{30}
\]

The source slab in (1) does not cover $0\le t<9/100$, and even its covered part supplies no positivity floor. Input(i) separately requires $\zeta(\sigma+iT)\ne0$ for $3/5\le\sigma\le1$, $0\le T\le7000$. Neither input(i) nor input(iii) is acquired here. Conditional on all three actual inputs, the source theorem gives $\Lambda\le1/10+(1/5)^2/2=3/25=.12$. This arithmetic implication is not a claimed Newman bound.

## 7. Quantitative collision screens and correction record

The analytic comparisons do not assume a positive final margin. To make the [Controls12](../../../../result-summaries/12_collision_controls_and_screening.md) test quantitative, distinguish two actual premises: a **complete source enclosure** $|H_*-Q_*|\le V_*$, and the **strict normalized floor** $\ell_*\le|Q_*/B_*|$, $\ell_*>V_*/|B_*|$, with $B_*\ne0$. At any zero of $H_*$ in a proposed exclusion domain the enclosure forces

\[
|Q_*|\le V_*,\qquad
\ell_*-V_*/|B_*|\le0.
\tag{31}
\]

Thus the strict floor necessarily fails there for every honest source budget, even with perfect approximation. If a changed source $H_*=H+D$ is compared with the unchanged theta reference, its extra $D$ must be retained jointly or paid: $|H_*-Q|\le V_{\rm val}+|D|$ is a valid fallback. Changed source identity alone is not proof that a coarse inequality fails. No new control computation or blanket failure on unrelated collision-free domains is claimed.

| Controls12 class | Named premise and quantitative screen |
| --- | --- |
| Euler-factor translates | The explicit shifted-field contribution $D=\tfrac c2e^{ta^2}(e^{-iaz}H_t(z+2ita)+e^{iaz}H_t(z-2ita))$ changes the complete source enclosure. It must be included before using a floor. With a valid enclosure, (31) rejects a claimed exclusion region containing a control zero; preserved positivity or finite Euler identities supply no strict floor. |
| Three-/four-weighted-square and the documented finite-source classes | Their non-theta coefficients require their own complete enclosure, rather than (14)–(17) unchanged. At their colliding zeros (31) defeats the corresponding strict value floor; at a counted merger the strict discriminant floor also fails. The finite-source theorem's absence of an all-real heat time separately prevents importing an all-real anchor for that class. |
| Finite-prime orbit, finite coefficient/measurement and finite canonical-score controls | Matching finitely many prime identities, coefficients or scores leaves a paid $D$ or a new source remainder. Arbitrarily small source distance is not the height-dependent strict normalized floor. At an included zero or event, (31) fails. Each construction retains its own location qualifier; in particular the finite-prime and finite canonical-score constructions make no common fixed-compact zero/event claim. No obstruction to an infinite assembly follows. |
| Reflected super-Gaussian | Reflection, endpoint and Gram positivity do not establish the complete enclosure (17) for this changed transform. With its own valid reference, (31) fails at its zero. The uniform phase bounds by themselves impose no value floor and may remain true for an auxiliary theta formula. |
| Smooth positive log-concave shape and strengthened positive-primitive controls | Their preserved primitive, asymptotic or shape data do not pay the changed complete remainder $D$. A positive auxiliary transform is not (29). For a domain containing their zero, the strict physical normalized floor fails by (31); no failure is asserted on the present unrelated strip. |
| BW-01 fixed-event atomic and exact finite-profile threshold controls, including continuous compact extensions | Selected imaginary-axis values and complete moment upper bounds do not give the full arithmetic enclosure and physical floor. At an included threshold event (31) fails even though selected profile floors survive. Their threshold multiplicities also fail eventual simplicity; the claimed obstruction remains limited to those retained data. |
| RH-conditional normalized endpoint controls | Source closeness and displayed completion do not bound the changed ordinary Dirichlet arithmetic in (17), or supply (29). At an escaping double, (31) or the strict counted-pair gap fails. Construction remains RH-conditional; a time-zero real double is outside (28), so it is not claimed to reject that final-strip domain. |
| Fixed theta amplitude with variable polynomial/counter observation kernels | The true readout has extra prepared residual/forcing. Omitting it fails the complete source enclosure; retaining it restores (31) at an included zero. Zero raw mismatch and a finite cosine prefix do not pay that forcing or acquire the strict floor. These are not physical theta collisions. |
| Actual-theta finite-profile positive-measure relaxation | Its unit-count atom and fractional slack masses satisfy the relaxed finite observations, but do not establish (29) for the integer physical divisor. The attained count-majorant obstruction concerns that observation span, not a physical zero or a counterexample to the arithmetic floor. |
| Reflection rigidity and the four-family support/reflection comparison | The full normalized square-support/reflection conjunction identifies theta in its stated weighted-comb class. Neither separate property supplies (29); even exact identification leaves the strict numerical comparison with the full source budget unacquired. No single missing shape property rejects every family. |

Larger/fractional divisor models and static divisor surgery likewise cannot import a count-two heat path: they fail integer multiplicity/count or a common physical evolution, respectively. This is a screen of those models, not a negative theorem about theta.

The exact quadratic $H=Q=(z-x_c)^2-2(t-T)$ provides an independent generic check. It solves $H_t=-H_{zz}$ with zero approximation error and zero defect, but $D_Q=2(t-T)$ reaches0 at $T$; strict pair protection fails. It can also test the actual pointwise strip geometry: take $T=1/4$ and $x_c\ge14000+\sqrt{24/25}$. At $t_0=1/10$, $z=x_c+i\sqrt{3/10}$ lies in (28) and is a zero, so (31) prevents a positive strip floor even with $Q=H,V=0$. This is an exact generic control, not an alternative source or a claim about theta.

The one correction pass checked all half-integer cancellations, the maximum-principle boundary, Cauchy disk containment, full root/product/chain terms, the three rational constant checks, the phase/sign normalization, the zero-height endpoint in (13), the complete real-part comparison, both signed seam jumps and one-sided source limits, and every final-strip/barrier interface. It made the zero-height equality explicit, restricted the holomorphy sentence to the analytic fixed-index fields, repaired inline math delimiters, restored the factor $1/2$ in the prose maximum preceding the already-correct (20), retained each control construction's own zero/event and location scope, and kept quantitative failure (31) separate from changed source identity. No target constant or family was changed. These are same-assistant checks; separate internal LLM assessment is still required and is not specialist review.

**Disposition:** all frozen analytical targets are proved within the stated family and comparator class. The missing input is the independent normalized full-arithmetic floor (29), with its complete height/cutoff coverage. The exact pointwise comparison (24) is a scoped limitation of the separately triangle-paid lift; it excludes neither other information classes nor heat/contour uses. No floor acquisition or further numerical packet is opened here.

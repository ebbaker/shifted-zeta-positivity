# AGC-E13 r2: a paid local holomorphic correction

19 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Explicit dispatch/request: **gpt-6.1-sol /
ultra**, as previously selected. Actual serving-backend model and effort
were not independently attested to this helper. One full derivation and
one correction pass; no numerical campaign or new height/time search.

**Status: proved in-note; separate nonauthor assessment required before
acceptance.** On the unchanged rectangle, explicit rational bounds give
\(|A_{33}'|<24000\), \(|A_{33}''|<1400\). The lift mismatch costs less
than \(1/24\) of the omitted leading-correction payment. This is a
source-allowance gain, not a newly evaluated corrected discriminant or
coverage extension.

Inputs are the [frozen contract](../brainstorm/notes/05_AGC_B02_R2_RETAINED_CORRECTION_CONTRACT_20261119.md),
[request](../research-progress/handoffs/AGC-E13-r2-request.md),
[source note06](06_AGC_E11_SOURCE_ALLOWANCE_20261119.md),
[source check](../reviews/03_AGC_SOURCE_ALLOWANCE_LEAD_CHECK_20261119.md),
and accepted [contour](04_AGC_E10_CONTOUR_ENDPOINT_20261119.md),
[heat](05_AGC_E10_BOUNDED_HEAT_20261119.md) and
[log-disk](08_AGC_E13_LOG_DISK_ALLOWANCE_20261119.md) interfaces. Earlier
numerical data retain their own
[assessment](../reviews/04_AGC_FIXED_CELL_NUMERICAL_ASSESSMENT_20261119.md).
The [result index](../../../../result-summaries/README.md),
[pattern index](../../../../avoid/README.md),
[Controls12](../../../../result-summaries/12_collision_controls_and_screening.md),
and patterns [01](../../../../avoid/01_restating_the_target.md),
[02](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[07](../../../../avoid/07_scoped_exclusions_read_as_universal.md) and
[12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
apply. Classification: finite source acquisition with an explicit
quantitative comparison, not an RH-equivalent reformulation.

## 1. Fixed cell and local holomorphy

Keep the literal theta field, physical \(P_{33}\), and

\[
X=140101/10,\quad A=2,\quad h=1,\quad r=9/10,\quad
9/100\le t\le1/10,\quad N=33.
\]

The full rectangle has \(|x-X|\le2\), \(|y|\le1\), \(z=x+iy\).
Its previously verified natural cutoff is unchanged. Put

\[
k=\pi/8,\quad w=z/2+kt,\quad w_0=x/2+kt,\quad
p(w)=67-2\sqrt{w/(2\pi)},\quad \theta(p)=\pi(p^2/2+3/8),
\]

using principal square roots near the positive axis, and define

\[
C(p)=\frac{e^{i\theta(p)}-i\sqrt2\cos(\pi p/2)}{2\cos(\pi p)},
\qquad C^\sharp(p)=\overline{C(\overline p)}
=\frac{e^{-i\theta(p)}+i\sqrt2\cos(\pi p/2)}{2\cos(\pi p)},
\]

\[
A_N(w)=\frac{\sqrt w}{2}
 \{(w+i)C(p(w))+(w-i)C^\sharp(p(w))\},
\]

\[
J_N(t,z)=(-1)^{N+1}\frac{\sqrt\pi}{4}e^{-kz-k^2t},\qquad
C_{\rm hol}=J_N A_N(w),\qquad Q_N=P_N-C_{\rm hol}.       \tag{1}
\]

Primes on \(A_N\) differentiate in \(w\); primes on \(C\) in
\(p\). Elementary rational bounds \(157/50<\pi<22/7\) give

\[
\Re w>7004,\quad |w|<7007,\quad |\Im w|\le1/2,
\qquad83<|\sqrt w|<84.                                  \tag{2}
\]

Indeed \(\Re w\le7006.05+0.04=7006.09\), so
\(|w|\le\Re w+|\Im w|<7007\). For
\(a=\sqrt{w/(2\pi)}=u+iv\),

\[
u\ge\sqrt{\Re w/(2\pi)}>1669/50,
\qquad u\le|a|<3341/100,
\]

by the rational inequalities
\((1669/50)^2(44/7)<7004\) and
\((3341/100)^2(157/25)>7007\). Since
\(|\Im p|=|\Im w|/(2\pi u)<1/400\),

\[
\boxed{9/50<\Re p<6/25,\qquad |\Im p|<1/400,
\qquad |p|<1/4.}                                        \tag{3}
\]

Here \(|\cos(\pi p)|^2=\cos^2(\pi\Re p)+\sinh^2(\pi\Im p)>1/2\),
so \(|2\cos(\pi p)|>7/5\). Strict margins on the compact rectangle
give an open neighborhood on which (1) is holomorphic in \(z\) and
smooth in real \(t\). No global claim about other apparent singularities
of \(C\) is needed. The patch is conjugation invariant and
\(A_N^\sharp=A_N\), so \(Q_N\) has physical conjugation symmetry.

## 2. Source phase and value correction

Point-of-use source: [Polymath v2](https://arxiv.org/html/1904.12438v2),
(7), (52), (53), (68), Corollary 6.4 and retained remainder (59).
Selected passages were checked; no full-paper audit is claimed. For real
\(T>0\), substitution in the principal carrier logarithm gives exactly

\[
\boxed{\mathfrak M_0(iT)U(T)e^{i\pi/8}
=-\frac{\sqrt\pi}{8}e^{-\pi T/4}\sqrt T(T+i).}            \tag{4}
\]

The carrier phase is
\(T\log(T/(2\pi))/2-T/2-\pi/4\); (52) cancels it after the extra
\(e^{i\pi/8}\). The factor \((iT)(iT-1)=-T(T+i)\) fixes the sign.
For the source's \(T'=w_0\), its displayed correction is consequently

\[
\boxed{C_{\rm val}(t,x+iy)=J_N(t,x+iy)A_N(w_0).}          \tag{5}
\]

For real \(w_0\), \(A_N(w_0)=
\Re\{\sqrt{w_0}(w_0+i)C(p(w_0))\}\).
The source exponential becomes
\(e^{k^2t}e^{-\pi w_0/4}e^{-iky}=e^{-kz-k^2t}\), and its factor
2 gives (1)'s prefactor. Thus \(C_{\rm hol}(t,x)=C_{\rm val}(t,x)\).
Only the lift (1), not the real-part value display, is differentiated
holomorphically. Conjugation supplies the lower source half-plane.

## 3. Explicit rational derivative bounds

Write \(n=e^{i\theta}-i\sqrt2\cos(\pi p/2)\),
\(d=2\cos(\pi p)\). On (3),
\(|\Im\theta|<1/500\), hence
\(e^{|\Im\theta|}<1003/1000\) and
\(\cosh(\pi|\Im p|)<1001/1000\). These follow from
\(e^s\le(1-s)^{-1}\) and
\(\cosh s\le(1-s^2/2)^{-1}\) on the stated small ranges.
Using \(|\sin z|\le|z|\cosh|\Im z|\), \(\sqrt2<10/7\), and
\(\pi<22/7\), differentiation gives

\[
|n|<5/2,\quad |n'|<7/4,\quad |n''|<15/2,
\qquad |d|>7/5,\quad |d'|<5,\quad |d''|<20.              \tag{6}
\]

For a fully rational check, set \(P=22/7\), \(E=1003/1000\),
\(H=1001/1000\). The three numerator upper bounds are

\[
E+(10/7)H,\qquad (P/4)E+(10/7)(P^2/16)H,
\qquad (P+P^2/16)E+(10/7)(P^2/4)H.
\]

The derivative denominator bounds are \(P^2H/2<5\) and
\(2P^2H<20\). From \(n=dC\) and its first two derivatives,

\[
\boxed{|C|<9/5,\qquad |C'|<8,\qquad |C''|<90.}          \tag{7}
\]

The intermediate bounds are \(25/14<9/5\), \(215/28<8\), and
\(1235/14<90\). They also hold for \(C^\sharp\) and its derivatives.
Equation (2) gives

\[
|p'|=|1/(\sqrt{2\pi}\sqrt w)|<1/200,\quad
|p''|=|p'/(2w)|<1/2800000,
\]

\[
| (\sqrt w)'|<1/166,\qquad
| (\sqrt w)''|<1/2300000.                                \tag{8}
\]

Put \(B=\{(w+i)C(p)+(w-i)C^\sharp(p)\}/2\). Exact derivatives are

\[
B'=\frac{C+C^\sharp}{2}
 +\frac{p'}2\{(w+i)C'+(w-i)(C^\sharp)'\},
\]

\[
B''=p'\{C'+(C^\sharp)'\}
 +\frac12\sum_{\nu=\pm1}(w+\nu i)
 \{C_\nu''(p')^2+C_\nu'p''\},\quad C_+=C,\ C_-=C^\sharp.
\]

Since \(|w\pm i|<7008\), define the explicit rational numbers

\[
b_0=7008(9/5)=63072/5,\quad
b_1=9/5+7008(8/200)=7053/25,
\]

\[
b_2=2(8/200)+7008(90/200^2+8/2800000).
\]

Then \(|B|<b_0\), \(|B'|<b_1\), \(|B''|<b_2\), and the full
product rule \(A_N=\sqrt w B\) yields

\[
\boxed{\begin{split}
|A_N|&<84b_0<1060000,\\
|A_N'|&<b_0/166+84b_1<24000,\\
|A_N''|&<b_0/2300000+2b_1/166+84b_2<1400.
\end{split}}                                             \tag{9}
\]

Every product and chain term is included. These are uniform rational
bounds on the full rectangle, not sampled derivatives. The complex
expressions remain available for tighter joint enclosure later.

## 4. Exact defect and mismatch payments

With \(w_t=k\), \(w_z=1/2\), direct differentiation gives

\[
(C_{\rm hol})_t=J_N(-k^2A_N+kA_N'),\qquad
(C_{\rm hol})_{zz}=J_N(k^2A_N-kA_N'+A_N''/4).
\]

Therefore

\[
\boxed{R_Q=Q_t+Q_{zz}=R_N-J_NA_N''/4,\qquad
|R_Q|\le|R_N|+350|J_N|.}                                \tag{10}
\]

For \(E_Q=H-Q\), backward physical time still gives
\((E_Q)_u=(E_Q)_{zz}+R_Q\). With the old constant scale
\(\mathcal S=e^{\pi X/8}\), \(\mathcal S|J_N|<1\), so the added
scaled defect costs less than 350. Indeed
\(\sqrt\pi<16/9\), \(e^{\pi/4}<e^{11/14}<9/4\); the latter follows
from \(e^a\le1+a+a^2/[2(1-a/3)]\) at \(a=11/14\).
This is a triangle payment, not favorable cancellation with \(R_N\).

The vertical segment from \(w_0\) to \(w_0+iy/2\) stays in the patch,
so

\[
\boxed{|C_{\rm hol}-C_{\rm val}|
\le\mathcal M:=12000|J_N|\,|y|.}                        \tag{11}
\]

Let \(L=e^{k^2t}|\mathfrak M_0(iw_0)|\), the earlier full omitted
leading-correction payment. Equation (4) implies

\[
\frac{L}{|J_N|}=\frac12\sqrt{w_0}\sqrt{w_0^2+1}
 >\frac12(83)(7004).
\]

The useful complete comparisons are

\[
\boxed{\mathcal M<\frac{|y|}{24}L\ (y\ne0),\qquad
\mathcal M=0\ (y=0),\qquad |C_{\rm hol}|<4L.}            \tag{12}
\]

Their rational checks are \(24000\cdot24<83\cdot7004\) and
\(2\cdot1060000<4\cdot83\cdot7004\). On \(\Gamma\), the mismatch
is less than \(3L/80\).

## 5. Full corrected source budget and consumer conditions

Set \(T=x/2\), \(T'=w_0\), \(\eta=|y|\),
\(\sigma_\pm=(1\pm\eta)/2\),
\(s_\pm^{\rm src}=\sigma_\pm+iT\), and
\(a_{\rm RS}=\sqrt{T'/(2\pi)}\). The retained source functions are

\[
\epsilon_n(t,s)=\exp\left(
 \frac{(t^2/8)|\alpha(s)-\log n|^2+t/4+1/6}{T-3.33}\right)-1,
\]

\[
\delta_\sigma=
 \left(\frac{0.397\,9^\sigma}{a_{\rm RS}-0.865}
                  +\frac5{3(T-6)}\right)e^{3.49/(T-4)},
\quad S_{\rm term}=\sum_{n=1}^{33}\sum_{\nu=\pm}
 |p_n(t,s_\nu^{\rm src})|\epsilon_n(t,s_\nu^{\rm src}).
\]

The source domain is \(x\ge200\), \(|y|\le1\), \(0<t\le1/2\),
with the unchanged natural cutoff. Corollary 6.4 and (11) give

\[
\boxed{|H-Q_N|\le V_Q:=S_{\rm term}
       +L(\delta_{\sigma_-}+\delta_{\sigma_+})+\mathcal M.} \tag{13}
\]

Both term-replacement sums and the complete retained-correction remainder
are paid. For the previous full omitted budget
\(V_P=S_{\rm term}+L(1+\delta_{\sigma_-}+\delta_{\sigma_+})\),

\[
V_Q<V_P-\frac{23}{24}L\quad\hbox{on the full rectangle},\qquad
V_Q<V_P-\frac{77}{80}L\quad\hbox{on }\Gamma.              \tag{14}
\]

This compares physical allowances at different references. It does not
assign the smaller budget to \(P_N\)'s center or denominator.

A useful changed-denominator comparison is also available. On a cleared
contour point put \(q_P=V_P/|P|\), \(v=L/|P|>0\). If an acquired
uniform bound satisfies \(q_P\le q_0<23/96\), then \(v\le q_P\)
and

\[
|Q|\ge|P|(1-4v)>0,\qquad
\boxed{\frac{V_Q}{|Q|}
\le\frac{q_P-(23/24)v}{1-4v}<q_P.}                       \tag{15}
\]

The strict inequality is exactly \(4q_P<23/24\).
Also \(|C_{\rm hol}/P|<4q_0<1\), so Rouché transfers count two
from \(P\) to \(Q\), and \(m_Q\ge(1-4q_0)m_P\). These relative
and counting consequences concern \(\Gamma\), where the denominator
and old source ratio have been acquired, not the whole rectangle.
Continuity and compactness make the pointwise strict ratio improvement
uniform, but no new numerical decrement has been evaluated.

The earlier accepted [Note07](07_AGC_E12_FIXED_CELL_COMPARISON_20261119.md)
has \(q_0=166454/10^6<1/6<23/96\), count two and positive \(m_P\)
on every slice. Conditional on that reviewed record, (15) therefore
pays count two and clearance for \(Q\), in particular \(m_Q>m_P/3\),
without a new run. This is an analytical consequence of an existing
certificate, not a fresh interval evaluation of \(Q\).

The **center and discriminant still change**. A final consumer must
enclose \(c_Q,D_Q\), their arithmetic/alias errors, and a usable
\(q_Q\) for this reference. The accepted shared allowance is
\(B_Q=r^2F(\operatorname{atanh}q_Q,|c_Q-X|/r)\), or its explicit
upper bounds. A complete positive result needs

\[
\underline D_Q(u)-B_Q(u)>0\qquad(0\le u\le U),            \tag{16}
\]

with reference uncertainty included. Improvement over an earlier
complete lower allowance requires
\(\underline D_Q-B_Q>\underline D_P-B_P\) at identical information;
(15) alone does not prove it. A heat/time consumer uses the actual
defect (10), initial and both lateral \(E_Q\) data from (13), and the
\(Q\) center. The equally informed direct \(Q\) comparator receives
every such enclosure and the same refined estimator. No representation
advantage or cost improvement is asserted.

## 6. Controls and correction record

The detailed screens in [Note04 §7](04_AGC_E10_CONTOUR_ENDPOINT_20261119.md)
and [Note08 §6](08_AGC_E13_LOG_DISK_ALLOWANCE_20261119.md) remain in force.
The exact physical control \(H=Q=(z-X)^2-2(t-T)\) has zero corrected
error and defect, yet \(D_Q\) reaches zero: strict (16) fails.
Approximation quality alone still cannot protect a colliding reference.

Euler-factor, weighted-square, finite-prime and finite-profile controls
fail the unchanged full theta identification needed for (13); reflected
super-Gaussian and smooth/positive-primitive controls likewise lack its
exact arithmetic square expansion. These source-premise failures are not
numerical rejections: at an applicable counted collision a valid complete
allowance must make (16) fail. Finite-source controls retain their absence
of an all-real anchor; RH-conditional escaping doubles retain their
hypothesis/location scope. Changed observation kernels need their nonzero
physical forcing. Larger/fractional divisors fail count two; static divisor
surgery supplies no common heat path. The screens exclude no new
theta-specific estimate and assert no universal failure of corrected
references.

Acquired here: local holomorphy, explicit derivative payments, exact
defect, full corrected envelope, and comparisons (14)–(15). Not acquired:
new numerical source values, \(Q\) moments, a complete corrected gap
gain, or new coverage. The next bounded calculation may evaluate the
same reference and complete allowances only after separate assessment.

The single correction pass checked phase/sign and parity, the complex
patch, quotient and chain derivatives, rational overpayments, cancellation
in (10), and the changed denominator in (15). It retained the \(y=0\)
endpoint and separated the proved source gain from the unacquired final
gap gain. No mathematical correction was needed; this is a same-assistant
check, not independent assessment.

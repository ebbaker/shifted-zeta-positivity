# Microscopic-height complete reference and explicit heat-defect source budget

23 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Actual model: **gpt-6-astra (Codex)**; reasoning effort: **ultra**.
Status: **proved estimates and scoped acquisition audit**; the all-height wall
floor below is not acquired. The separate finite-band certificate is the concrete bounded-height acquisition lane;
this note states no certified high-height wall floor.

Read with the [result index](../../../../result-summaries/README.md),
[collision controls](../../../../result-summaries/12_collision_controls_and_screening.md),
and [avoid index](../../../../avoid/README.md), particularly
[separate bounds](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
and [scoped exclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md).
This is a finite quantitative source milestone and an applicability audit, not a
new simplicity criterion.

## 1. Finding

The complete Riemann–Siegel reference remains quantitatively useful at
\(t\log^2x\ll1\). Its normalized absolute error is \(O(x^{-1/4})\) on
the real axis. Its exact heat defect, computed below, has the better normalized
bound \(O(x^{-3/4})\). Retaining and analytically continuing the explicit
Riemann–Siegel correction improves the field allowance to \(O(x^{-3/4})\)
as well, with a completely computed derivative cost (Section 4).
The obstacle is acquiring a lower bound for that complete
reference on the chosen wall, including the vertical portions. The much simpler
two-carrier asymptotic does not apply on this microscopic clock.

The normalization throughout is
\[
H_t(z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,\qquad
H_0(z)=\xi(1/2+iz/2)/8,\qquad \partial_tH_t=-\partial_z^2H_t.
\]
All carriers and errors below use that normalization. The bounded-height lane
uses the exact xi initial field and a complete-source heat Taylor remainder;
it is separate from this high-height estimate and does not extend its wall
floor to unbounded height.

## 2. Explicit high-height reference and microscopic error

The imported input is [Polymath, Theorem 1.3 and Proposition 9.1](https://arxiv.org/html/1904.12438v2).
Theorem 1.3 supplies explicit errors for real \(0<t\le1/2\),
\(x\ge200\), \(0\le y\le1\); its truncation is
\(N=\lfloor\sqrt{x/(4\pi)+t/16}\rfloor\). Proposition 9.1(i) needs
\(x\ge e^{C/t}\). Proposition 9.1(ii) supplies a relative carrier error
at most \(0.7\) for \(3\le y\le4\) and sufficiently large \(x\).
The latter leaves the vertical walls unpaid and its onset constant is not a
numerical certificate.

Define explicitly on \(\mathbb C\setminus(-\infty,1]\), using the principal logarithm,
\[
M_0(\sigma)=\frac{\sigma(\sigma-1)}{16}\pi^{-\sigma/2}\sqrt{2\pi}
\exp\!\left[\left(\frac\sigma2-\frac12\right)\operatorname{Log}(\sigma/2)-\frac\sigma2\right],
\quad
\alpha(\sigma)=\frac1{2\sigma}+\frac1{\sigma-1}+\frac12\operatorname{Log}(\sigma/(2\pi)).
\]
Thus \(\alpha=M_0'/M_0\). Set
\[
 s=(1-iz)/2,\qquad
 A_n(\sigma)=M_0(\sigma)n^{-\sigma},\qquad
 \beta_n(\sigma)=\alpha(\sigma)-\log n,
\]
\[
 G_{t,N}(z)=\sum_{\sigma\in\{s,1-s\}}\sum_{n=1}^N
       A_n(\sigma)\exp\{t\beta_n(\sigma)^2/4\}.       \tag{A1}
\]
This is exactly the complete finite-sum reference \(B_tf_t\), rewritten without
conjugates. It is holomorphic in \((t,z)\) on a fixed-\(N\) chart avoiding the
factor's branch cuts. It is not claimed to solve the heat equation.

For a finite implementation no asymptotic constant need be guessed. Put
\[
X=x/(4\pi),\ L=\log X,\quad
p=\operatorname{Re}\big(s+(t/2)\alpha(s)\big),
\quad \rho=e^{0.02y}X^{-y/2},\quad \nu=\frac{ty}{2(x-6)},
\]
\[
S=\sum_{n=1}^{N}(1+\rho N^\nu n^y)
             e^{t\log^2n/4}n^{-p},\qquad
b=\frac{t^2L^2/16+0.626}{x-6.66},
\]
\[
E_{\rm fin}=S(e^b-1)+X^{-(1+y)/4}
 \exp\!\left[-\frac{tL^2}{16}
 +\frac{1.24(3^y+3^{-y})}{N-0.125}
 +\frac{3|L+i\pi/2|+10.44}{x-12}\right].                 \tag{A1a}
\]
Then \(|H_t/B_t-f_t|\le E_{\rm fin}\) in the imported theorem's domain,
where \(B_t=M_0(s)e^{t\alpha(s)^2/4}\) and \(f_t=G_{t,N}/B_t\).
This slightly coarsens its finite first error sum using
\(|L-2\log n|\le L\) for \(1\le n\le N\), valid here because
\(N\le X\). The uncoarsened sum may be used when it gives a better margin.
Every quantity in (A1a) is finite and explicitly evaluable.

Put \(X=x/(4\pi)\), \(L=\log X\), and suppose \(0<tL^2\le K\),
with \(K\) fixed. At \(y=0\), write \(E_{\rm RS}\) for the sum of the
three explicit error allowances in Theorem 1.3. Directly from its displayed
bounds,
\[
 E_A+E_B=O_K(X^{-3/4}),\qquad
 E_C\le X^{-1/4}e^{-tL^2/16}
                  \exp\{O(X^{-1/2}+L/X)\}.                  \tag{A2}
\]
Consequently
\[
 \left|H_t/B_t-f_t\right|\le E_{\rm RS}=O_K(X^{-1/4}).       \tag{A3}
\]
The constants can be evaluated from the theorem; (A2) is an asymptotic
interpretation, not a replacement for those explicit bounds in a certificate.
For fixed \(0\le y<1\), the same derivation gives
\(E_A+E_B=O_{K,y}(X^{-(3+y)/4})\) and the leading allowance
\(X^{-(1+y)/4}e^{-tL^2/16}(1+o(1))\). At \(y=1\), use
\(O_K(X^{-1}\log X)\) for the first allowance. Reflection supplies the
corresponding negative strip with its reflected carrier.

**Derivation.** For \(v=\log n\le L/2+O(X^{-1})\), the exponential
part of the main-sum absolute weight is
\[
 \exp\{(t/4)(v^2-Lv)+O(tv/x^2)\}\le1+o(1).
\]
The first error's relative exponential bracket is \(O_K(1/x)\): its
numerator is \(0.626+O_K(L^{-2})\). Summing
\(n^{-(1+y)/2}\), and retaining the reflected weight supplied by the
bound on \(\gamma\), gives (A2). The second allowance follows by inserting
\(N\asymp\sqrt X\) into the theorem. Here \(\operatorname{Re}\alpha(s)=L/2+O(x^{-2})\) follows directly from
the displayed rational-logarithmic formula, uniformly for bounded \(y\).
The finite allowance uses the exact real part \(p\), so it does not depend
on the differing small correction terms printed in Theorem 1.3 and
Proposition 6.6(ii), or the differing heat coefficient in Section 9.

There is no valid deduction here that \(f_t\) can be replaced by \(1+\gamma\).
Indeed at \(y=0\) the absolute \(n=2\) weight in the first sum tends to
\(2^{-1/2}\) when \(tL^2\) stays bounded, while the absolute sum of its
omitted \(n\ge2\) weights has order \(X^{1/4}\), with constants depending
on \(K\). This defeats that *absolute-tail argument* for two-carrier dominance;
it does not prove that the signed omitted sum is large at every height.
Also \(tL^2\to0\) implies \(t\log x\to0\), incompatible with the
hypothesis \(t\log x\ge C\) of Proposition 9.1(i).

## 3. New explicit heat-defect allowance for this reference

For one term \(g=A_n(\sigma)\exp(t\beta^2/4)\), differentiation in
\(\sigma\) gives
\[
 \partial_\sigma\log g=\beta+(t/2)\beta\alpha',\qquad
 \partial_\sigma^2\log g=\alpha'+(t/2)((\alpha')^2+\beta\alpha'').
\]
Both choices \(\sigma=s,1-s\) have
\(\partial_z^2=-\tfrac14\partial_\sigma^2\). Therefore the exact defect is
\[
 (\partial_t+\partial_z^2)g
 =-\frac g4\left[
 \alpha'+t\beta^2\alpha'
 +\frac t2\big((\alpha')^2+\beta\alpha''\big)
 +\frac{t^2}{4}\beta^2(\alpha')^2\right].                  \tag{A4}
\]
In particular, a finite, directly evaluable allowance for
\(|G_t+G_{zz}|\) is the sum over (A1) of \(|g|C_n\), where
\[
 C_n=\frac14\left[
 a_1+|t|u_n^2a_1+\frac{|t|}{2}(a_1^2+u_na_2)
                   +\frac{|t|^2}{4}u_n^2a_1^2\right],
\quad u_n=|\beta_n|,\ a_j=|\alpha^{(j)}|.                \tag{A5}
\]
There is no quadrature and no root gap in this allowance. The required rational
logarithmic derivatives are
\[
 \alpha'(\sigma)=-\frac1{2\sigma^2}-\frac1{(\sigma-1)^2}
                         +\frac1{2\sigma},
\quad
 \alpha''(\sigma)=\frac1{\sigma^3}+\frac2{(\sigma-1)^3}
                         -\frac1{2\sigma^2}.
\]
For the regime in (A2), \(u_n=O(\log x)\), \(a_1=O(x^{-1})\),
\(a_2=O(x^{-2})\), uniformly for all retained \(n\). Thus
\[
 \frac{|G_t+G_{zz}|}{|B_t|}
 \le\sum_{\sigma,n}|g/B_t|C_n=O_K(X^{-3/4})\quad(y=0).     \tag{A6}
\]
This estimate is new arithmetic bookkeeping for a specified complete reference,
not an assertion that the actual \(H_t\) has a small logarithmic derivative.

## 4. The correction term: a sharper analytic source reference

The same primary source's Corollary 6.4 and Proposition 6.6(vi) retain the
Riemann–Siegel correction. They improve the **pointwise** normalized field
allowance to
\[
 E_{\rm corr}=S(e^b-1)+X^{-(1+y)/4}
 \exp\!\left[-\frac{tL^2}{16}
       +\frac{3|L+i\pi/2|+3.58}{x-8.52}\right]
 \left[\frac{1.24(3^y+3^{-y})}{N-0.125}+\frac{6.92}{x-12}\right].
                                                               \tag{B1}
\]
Thus \(|H_t-(G_{t,N}-C_t)|/|B_t|\le E_{\rm corr}\), with
\(E_{\rm corr}=O_K(X^{-3/4})\) at \(y=0\). The extra factor
\(1/N\) in (B1), absent from the uncorrected allowance, matters.

Here are all definitions, with real \(t,x,y\) in the imported domain:
\[
 T'=x/2+\pi t/8,\quad a=\sqrt{T'/(2\pi)},\quad N=\lfloor a\rfloor,
 \quad p=1-2(a-N),
\]
\[
 U=\exp\!\left[-i\left(\frac{T'}2\log\frac{T'}{2\pi}
                                  -\frac{T'}2-\frac\pi8\right)\right],
\quad
 C_0(p)=\frac{e^{\pi i(p^2/2+3/8)}-i\sqrt2\cos(\pi p/2)}
                    {2\cos(\pi p)},
\]
\[
 C_t(x+iy)=2(-1)^N e^{-\pi iy/8+t\pi^2/64}
                 \operatorname{Re}[M_0(iT')C_0(p)Ue^{\pi i/8}]. \tag{B2}
\]
The singularities of \(C_0\) at \(p=\pm1/2\) are removable, with value
\((1-i)/4\). These are the only denominator zeros in \(|p|<5/4\).
One can evaluate their Taylor extensions; a direct interval division by
\(\cos(\pi p)\) across them is invalid. No claim about more distant
singularities is needed.

The displayed \(C_t\) is **not generally holomorphic in \(z\)**. It has
form \(e^{-\pi iy/8}R_t(x)\); the Cauchy–Riemann equations would require
\(R_t'(x)=-\pi R_t(x)/8\). Thus neither an analytic prepared polynomial nor
Cauchy derivative errors follow by inserting this displayed correction into
(A8). The following explicit continuation pays that distinction.

Define the holomorphic reflected function
\(C_0^\#(p)=\overline{C_0(\bar p)}\), and put
\[
 C_R=(C_0+C_0^\#)/2,\qquad C_I=(C_0-C_0^\#)/(2i).
\]
These are analytic functions of complex \(p\), agreeing with real and
imaginary parts only when \(p\) is real. On a fixed-\(N\) chart define
\[
 p_N(v)=1+2N-\sqrt{2v/\pi},\qquad
 V_N(v)=v^{3/2}C_R(p_N(v))-v^{1/2}C_I(p_N(v)),               \tag{B3}
\]
using the principal square root on \(\Re v>0\). The analytic correction is
\[
 \widetilde C_{t,N}(z)=k_N e^{-\pi z/8-\pi^2t/64}
                 V_N(z/2+\pi t/8),\qquad
 k_N=-(-1)^N\frac{\sqrt\pi}{4}.                           \tag{B4}
\]
It agrees with (B2) on \(y=0\).

**Exact phase and normalization check.** For positive real \(v\),
\(\operatorname{Log}(iv/2)=\log(v/2)+i\pi/2\). Substituting this into
\(M_0\), its oscillatory exponential is
\(\exp\{i(v\log(v/(2\pi))/2-v/2-\pi/4)\}\). Multiplication by
\(U(v)e^{\pi i/8}\) cancels that phase exactly, leaving
\[
 M_0(iv)U(v)e^{\pi i/8}
       =-\frac{\sqrt\pi}{8}\sqrt v\,(v+i)e^{-\pi v/4}.    \tag{B5}
\]
Taking the real part against \(C_0(p)\), multiplying by the factor 2 in
(B2), and using \(v=x/2+\pi t/8\) gives
\[
 C_t(x+iy)=k_N e^{-\pi(x+iy)/8-\pi^2t/64}V_N(T').
\]
Replacing \(T'\) by \(T'+iy/2\) gives (B4). This proof fixes all signs,
branches, the factor 2, and the canonical \(1/8\) normalization.

There are explicit finite derivative budgets. Put \(r=|v|\),
\(q=p_N'(v)=-1/\sqrt{2\pi v}\), and note \(p_N''=-q/(2v)\). Then
\[
 V_N'=\tfrac32\sqrt v\,C_R+v^{3/2}qC_R'
                    -\tfrac1{2\sqrt v}C_I-\sqrt v\,qC_I',
\]
\[
 V_N''=\tfrac3{4\sqrt v}C_R+\tfrac52\sqrt v\,qC_R'
       +v^{3/2}q^2C_R''
       +\tfrac1{4v^{3/2}}C_I-\tfrac{q}{2\sqrt v}C_I'
       -\sqrt v\,q^2C_I''.                               \tag{B6}
\]
For \(v=T'+i\theta y/2\), \(0\le\theta\le1\),
\[
 |p_N(v)-p_N(T')|\le\frac{|y|}{2\sqrt{2\pi T'}}<\frac18
 \quad(x\ge200,\ |y|\le1).
\]
Thus the entire comparison segment stays in \(|p|<9/8\). The following
coarse constants are completely explicit:
\[
 M_*:=\frac{e^{25\pi/32}+\sqrt2\cosh(5\pi/8)}
                      {2\sinh(\pi/8)},\qquad
 K_j=j!8^j M_*\quad(j=0,1,2).                             \tag{B7}
\]
They bound both \(|C_R^{(j)}|\) and \(|C_I^{(j)}|\) on \(|p|\le9/8\).
To verify this, on \(|p|=5/4\) either \(|\Im p|\ge1/8\), giving
\(|\cos\pi p|\ge\sinh(\pi/8)\), or
\(1<|\Re p|\le5/4\), giving \(|\cos\pi p|\ge1/\sqrt2\).
The numerator bounds in (B7) follow from \(|\Re p\Im p|\le25/32\)
and \(|\Im p|\le5/4\). Apply the maximum principle and the Cauchy
estimate with radius \(1/8\), after removing \(\pm1/2\).

With these constants one may take
\[
 V_1(r)=\tfrac32\sqrt r K_0+\frac r{\sqrt{2\pi}}K_1
                      +\frac{K_0}{2\sqrt r}+\frac{K_1}{\sqrt{2\pi}},
\]
\[
 V_2(r)=\frac{3K_0}{4\sqrt r}+\frac{5K_1}{2\sqrt{2\pi}}
       +\frac{\sqrt r K_2}{2\pi}
       +\frac{K_0}{4r^{3/2}}+\frac{K_1}{2\sqrt{2\pi}r}
       +\frac{K_2}{2\pi\sqrt r}.                          \tag{B8}
\]
Suprema of these elementary functions over the segment's explicit range of
\(r\) bound (B6). Direct interval evaluation of the removable analytic
functions can improve these conservative constants.

Set
\[
 Q(t,z)=\frac{\sqrt\pi}{4}
        \frac{e^{-\pi x/8-\pi^2t/64}}{|B_t(z)|},\qquad
 \widehat G_{t,N}=G_{t,N}-\widetilde C_{t,N}.
\]
The analytic reference satisfies the finite field allowance
\[
 \frac{|H_t-\widehat G_{t,N}|}{|B_t|}
 \le E_{\rm corr}+Q(t,z)\frac{|y|}{2}\sup_{\theta\in[0,1]}
                                  V_1(|T'+i\theta y/2|).   \tag{B9}
\]
This uses the fundamental theorem of calculus on the explicitly given
analytic function \(V_N\). It is not a Cauchy estimate on a nonanalytic
remainder. There is no unknown root-dependent constant.

The correction's exact heat defect also has a favorable cancellation:
\[
 (\partial_t+\partial_z^2)\widetilde C_{t,N}(z)
 =\frac{k_N}{4}e^{-\pi z/8-\pi^2t/64}
                                  V_N''(z/2+\pi t/8).     \tag{B10}
\]
Indeed the exponential has spatial logarithmic derivative \(-\pi/8\) and
time logarithmic derivative \(-\pi^2/64\), while the argument of \(V_N\)
has derivatives \(1/2\) and \(\pi/8\). Both the \(V_N\) and
\(V_N'\) terms cancel. Therefore the allowance (A5) for \(G\), plus
\(Q(t,z)V_2(|z/2+\pi t/8|)/4\), bounds the normalized defect of
\(\widehat G\). The defect formula for \(G\) was not transferred unchanged.

For fixed \(K\), uniformly on \(0\le y\le y_0<1\) and
\(0<tL^2\le K\), direct Stirling-factor evaluation gives
\(Q=O_{K,y_0}(X^{-(7+y)/4})\); (B8) gives \(V_1=O(X)\),
\(V_2=O(X^{1/2})\). Hence (B9) is
\(O_{K,y_0}(X^{-(3+y)/4})\), and the correction's normalized defect is
\(O_{K,y_0}(X^{-(5+y)/4})\). In particular the analytic corrected reference
has **both field and total heat-defect allowances \(O_K(X^{-3/4})\) at
\(y=0\)**. At \(y=1\), retain the earlier logarithm in the full-sum
allowance. Reflection and conversion to one carrier are still needed for a
collar crossing the real axis.

All of (B1), (B9) concern **real** \(t\) and fixed \(N\) on the chart.
Although (B4) has a local analytic complex-time extension, no imported
field-error estimate for complex \(t\) is asserted. The corrected wall floor
\(\widehat m_f=\inf_\Gamma|\widehat G/B|\) must still exceed the
acquired right-hand side of (B9). With that floor, the same relative-error and
quotient formulas in Section 5 apply to \(\widehat G\). Without it the
improved residual is not a simplicity or zero-count certificate.

## 5. What exactly this does and does not pay

On a closed wall in a fixed-\(N\) chart, let an interval evaluation acquire
\(m_f=\inf_\Gamma|f_t|>E_{\rm RS}\). Then the actual relative field error is
\[
 \sup_\Gamma|H_t/G_{t,N}-1|\le E_{\rm RS}/m_f.             \tag{A7}
\]
The paper's full error formula therefore becomes useful at microscopic times
whenever the computed full-sum wall floor dominates \(X^{-1/4}\). This is an
explicit candidate reference, not a supplied all-height floor. On a wall
meeting a truncation boundary, split the chart or pay the finitely many terms
added/removed to use one fixed \(N\); do not regard a jumping \(f_t\) as
one holomorphic reference.

For derivative consumers, retain the normalized error \(e=H/B-f\). If a
spatial collar gives bounds \(|e^{(j)}|\le E_j\), put \(\lambda=B'/B\).
The complete source quotient difference has the exact cancellation
\[
 \frac{H_{zz}}H-\frac{G_{zz}}G
 =\frac{fe''-ef''+2\lambda(fe'-ef')}{f(f+e)}.             \tag{A8}
\]
In particular its norm is at most
\[
 \frac{E_2+2|\lambda|E_1+
              (|f''|+2|\lambda||f'|)E_0/m_f}{m_f-E_0}.   \tag{A9}
\]
A Cauchy collar of width \(d\) gives \(E_j\le j!E_{\rm collar}/d^j\).
The collar error must use one analytic carrier \(B\). If it crosses the real
axis, convert the reflected theorem bound on its negative half by the explicit
factor \(|B_{\rm reflected}/B|\); do not paste two normalizations together
and differentiate them. On a collar of width \(O(1/\log x)\) this ratio is
bounded, but its bound is part of the certificate.
For \(d\asymp1/\log x\), the scale in (A9) is
\(O(\log^2x\,E_{\rm collar}/m_f)\) **only if** the normalized local
reference ratios \(|f'|/(m_f\log x)\),
\(|f''|/(m_f\log^2x)\), and the corresponding carrier constant are bounded.
These extra bounds must be evaluated, not silently substituted by typical-size
intuition. The absolute full-sum upper bound alone need not make (A9) small.

For Note 12's reference defect, (A5) together with the same \(m_f\) bounds
\((G_t+G_{zz})/G\); its prepared-polynomial projection then uses the already
proved wall kernel. This is a paid defect term, not an assumption that \(G\)
is an exact heat solution.

The imported error theorem concerns **real time**. Formula (A1) is analytic in
complex time, but this fact does not extend (A3) into a complex-time disk with
the same bound. A complex contour must acquire that extension separately from
the complete source or the source proof. Likewise no zero count, positivity
of the forest denominator, or common wall nonvanishing follows from (A3)
without the relative margin and its contour geometry.


## 6. Scope and controls

This supplies an actual source reference and its computable field and heat-defect
budgets. It leaves two different gates: a whole-wall normalized margin for the
full reference, and a complex-time remainder if a curved time path is used.
No small residual is inferred from the late-clock spacing screen. Conversely,
the failure of two-carrier absolute-tail bounds does not exclude using the full
finite sum or its arithmetic correlations.

Quadratic and Hermite births show that accurate heat transport alone does not
exclude multiple endpoints. Euler-factor, weighted-square, reflected, and
positive-primitive controls do not share the unchanged full xi initial field
or this complete fixed-N theta approximation. They therefore fail the actual
source-identification premise rather than the contour algebra. A wall floor
that happens to contain a multiple root inside it is possible; the forest
consumer must still acquire its own denominator margin and precision scale.

The derived estimates (A2), (A4), (A6), and (B3)–(B10) are a quantitative analytic milestone
for the specified source approximation. They are not a finite certificate,
a density-one conclusion, or a proof of conditional simplicity. No specialist
review or priority claim is made. Direct fixed-time coefficient acquisition
with the same source data remains the required fair comparator.

Relevant consumers are [Note 07](07_COMPLETE_SOURCE_FORCE_AND_FILTER_RESIDUAL_20261023.md),
[Note 11](11_FOREST_POLYNOMIAL_AND_GAP_FREE_FILTER_ENCLOSURE_20261023.md), and
[Note 12](12_COUPLED_COEFFICIENT_BACKWARD_TRANSPORT_20261023.md).

The bounded actual-source counterpart is [Note 13](13_COMPLETE_THETA_WALL_AND_COEFFICIENT_CERTIFICATE_20261023.md). The source algebra, corrected continuation, and finite derivative budgets are checked in [Review 12](../reviews/12_MICROSCOPIC_REFERENCE_AND_HEAT_DEFECT_REVIEW_20261023.md); its actual replay scope and status govern any numerical validation claim.

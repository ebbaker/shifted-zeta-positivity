# E15 r1: complete Gaussian Laguerre hierarchy and finite-multiplicity resolution

7 November 2026 UTC; 6 November 2026 America/New_York. Prepared for
**Edward Baker** with substantial OpenAI Codex assistance. Explicitly
selected executor configuration: **gpt-6.1-sol, ultra**. This is a dispatch
record, not independent verification of the serving backend.

**Task:** TND-O-E15 r1, Type E, under frozen
[request28](../research-progress/handoffs/28_TND_O_E15_GAUSSIAN_LAGUERRE_REQUEST_20261107.md),
[inputs28](../research-progress/handoffs/28_TND_O_E15_GAUSSIAN_LAGUERRE_INPUTS_20261107.json)
and [B03 r5 Decision14](../brainstorm/notes/14_TND_O_B03_R5_TWO_METRIC_DECISION_20261107.md).
All ten input byte counts and hashes matched before work. The exact
consumed hashes and the separately authorized later status-only register
revision are recorded in
[return28](../research-progress/handoffs/28_TND_O_E15_GAUSSIAN_LAGUERRE_RETURN_20261107.json).
Only this note and that return are worker-owned outputs.

**Result, proved in-note:** the complete-theta quadratic formula has a
joint order/source-index/radial remainder, uniform in every real center.
At every exact finite-multiplicity real heat event, derivative level
\(m-2\) has the resolving signal
\[
 \boxed{A_{m-2}(\lambda_*-t,x_*,\kappa t)
 =a_m^2t(\kappa/2-1)+\mathcal E_m(t),\qquad
 |\mathcal E_m(t)|\le E_\kappa(t;|a_m|,C,D)=O(t^{3/2}).}
 \tag{1}
\]
Here \(0<\kappa<2\); (26) gives every global remainder constant, and
(28)–(29) expose local jets, analytic radii and Gaussian-tail costs.
The spatial cancellation characteristic \(v'=2\) loses the resolving
window; its exact exit time is (34). No canonical sign or
amplitude-normalized comparison excluding these events is acquired.

## 1. Fixed conventions, source and classification

Throughout, \(v>0\) is the **variance**, and \(p,q\) are spectral
coordinates:
\[
 \begin{split}
 F_\lambda(p)&=e^{\lambda p^2}\Phi(p),\qquad
 H_\lambda(x)=\frac12\int_{\mathbb R}F_\lambda(p)e^{ixp}\,dp,
 \qquad H_\lambda{}_{,\lambda}=-H_{\lambda,xx},\\
 w_v(y)&=(2\pi v)^{-1/2}e^{-y^2/(2v)},\qquad
 f_n=\partial_x^nH_\lambda,\\
 L_f&=(f')^2-ff'',\qquad
 A_n(\lambda,X,v)=\int_{\mathbb R}w_v(x-X)L_{f_n}(x)\,dx.
 \end{split} \tag{2}
\]
The [complete source](../manuscript/sections/02_source.tex) is real,
strictly positive and even. On the positive half-line,
\[
 \Phi(p)=e^p\sum_{a\ge1}P_0(a^2\rho(p))e^{-a^2\rho(p)},\qquad
 P_0(r)=2r^2-3r,\quad \rho(p)=\pi e^{4p}.
 \tag{3}
\]
All summands in (3) are positive. Reflection is a property of the
complete source; a reflected finite prefix is not asserted to have its
smooth endpoint jets. The complete-source bounds in M section 2 justify
all finite differentiations, Gaussian integrations and integrations by
parts below on compact real \(\lambda\)-intervals. The new all-order
payment is made explicitly in sections 3–4.

For real \(s\), define the complete absolute source moments
\[
 M_j(s)=\int_{\mathbb R}|p|^j e^{sp^2}\Phi(p)\,dp<\infty.
 \tag{4}
\]
Take \(L\ge0\) above the real times under consideration. For every
\(\beta>0\), M section 2 also gives the fully explicit order bound
\[
 M_j(L)\le j!\beta^{-j}B_0J_{0,2}(L,\beta),\qquad
 B_0=5C_2(0),\quad
 C_2(N)=\sum_{a>N}a^4e^{-\pi(a^2-1)},
 \tag{5}
\]
by \((\beta|p|)^j\le j!e^{\beta|p|}\). The integral \(J\) is
the positive complete radial majorant in M section 2, not a finite
arithmetic approximation.

This package is a quantitative acquisition/diagnostic milestone: explicit
all-order and complete-source errors and a paid all-finite-multiplicity
signal. It is not evidence for an all-window sign criterion. The
[result index](../../../../../result-summaries/README.md),
[controls12](../../../../../result-summaries/12_collision_controls_and_screening.md),
[patterns index](../../../../../avoid/README.md),
[target classification01](../../../../../avoid/01_restating_the_target.md),
[control rule02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md)
and [scope07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
govern this distinction. No real-rootedness characterization is imported.

## 2. Exact quadratic formula and the signed kinetic threshold

**Proposition 1.** For every integer \(n\ge0\), real \(X\), real
\(\lambda\), and variance \(v>0\),
\[
 \boxed{A_n=\frac18\int_{\mathbb R^2}(-pq)^n(p-q)^2
 F_\lambda(p)F_\lambda(q)
 e^{iX(p+q)-v(p+q)^2/2}\,dp\,dq.}
 \tag{6}
\]
The expression is real; the exponential phase can equivalently be
replaced by \(\cos(X(p+q))\).

Indeed \(f_n=(i^n/2)\int p^nF_\lambda(p)e^{ixp}\,dp\).
The product \((f_n')^2-f_nf_n''\), after interchanging \(p,q\) in
half of the second term, has multiplier
\[
 \frac{(-1)^n}{8}(pq)^n(p^2+q^2-2pq)
 =\frac18(-pq)^n(p-q)^2.
\]
Gaussian integration supplies
\(\int w_v(x-X)e^{ix(p+q)}dx=e^{iX(p+q)-v(p+q)^2/2}\).
Evenness under \((p,q)\mapsto(-p,-q)\) removes the imaginary part.
All products are absolutely integrable before this symmetrization.

In particular, splitting the four quadrants gives the real
positive-half-line formula
\[
 \begin{split}
 A_0=\frac14\int_0^\infty\!\int_0^\infty F_\lambda(p)F_\lambda(q)
 \big[&(p-q)^2e^{-v(p+q)^2/2}\cos(X(p+q))\\
       +&(p+q)^2e^{-v(p-q)^2/2}\cos(X(p-q))\big]\,dp\,dq.
 \end{split} \tag{7}
\]
This is a signed formula on a positive integration domain. Substitution
of (3) is the full double theta-index formula: replace the product
\(F_\lambda(p)F_\lambda(q)\) by
\[
 e^{\lambda(p^2+q^2)+p+q}
 \sum_{a,b\ge1}P_0(a^2\rho(p))P_0(b^2\rho(q))
 e^{-a^2\rho(p)-b^2\rho(q)}.
 \tag{8}
\]
The absolute bounds in section 4 justify both infinite index sums and
both unbounded radial integrals. For general \(n\), multiply the
first bracket term in (7) by \((-1)^n(pq)^n\) and the second by
\((pq)^n\).

Put \(Z=\int w_v(x-X)H_\lambda(x)^2dx\) and
\(E_w=\int |(H_\lambda\sqrt{w_v(\cdot-X)})'|^2dx\). Then
\[
 \boxed{A_0=2E_w-\frac{Z}{2v}
 =\partial_\lambda Z+\frac12\partial_{XX}Z}
 \quad\text{(derivatives at fixed \(v\)).}
 \tag{9}
\]
For verification, integration by parts first gives
\(A_0=2\int w_vH_x^2-\tfrac12\int w_v''H^2\).
Expand \(E_w\), and use
\(w_v''/w_v=(x-X)^2/v^2-1/v\) and
\((w_v'/w_v)^2=(x-X)^2/v^2\) to get the first equality.
For the second,
\(Z_\lambda=-2\int w_vHH_{xx}\) and
\(\tfrac12Z_{XX}=\int w_v(H_x^2+HH_{xx})\).
Thus ordinary \(E_w\ge0\) does not imply the signed threshold
\(E_w\ge Z/(4v)\). The global energy and intensity identities of
[M section 4](../manuscript/sections/04_energy.tex) are reused here;
positive energy is not a new collision exclusion or a new discovery.

## 3. Heat/order hierarchy and an all-order majorant

**Proposition 2.** For all indices in (2),
\[
 \boxed{\partial_\lambda A_n=-\partial_{XX}A_n+2A_{n+1},
 \qquad \partial_vA_n=\tfrac12\partial_{XX}A_n.}
 \tag{10}
\]
For any differentiable positive-variance schedule \(v(\lambda)\),
\[
 \frac{d}{d\lambda}A_n(\lambda,X,v(\lambda))
 =\left(\frac{v'}2-1\right)\partial_{XX}A_n+2A_{n+1}.
 \tag{11}
\]
To check the first identity directly, write \(f=f_n\). Since
\(f_\lambda=-f''\),
\[
 (L_f)_\lambda=(f'')^2+ff''''-2f'f''',\qquad
 (L_f)''=(f'')^2-ff''''.
\]
Consequently \((L_f)_\lambda=-(L_f)''+2L_{f'}\).
Convolve and integrate by parts. The second identity in (10) is the
Gaussian heat equation. Equivalently, in (6) the multipliers are
\(p^2+q^2\), \(-(p+q)^2\) and \(-pq\), giving the same signs.

For every \(\epsilon>0\), uniformly in all real \(X\), all
\(v>0\), all \(\lambda\le L\), and **every** integer \(n\ge0\),
\[
 \boxed{|A_n(\lambda,X,v)|\le
 n!\epsilon^{-n}\mathcal C_\epsilon(L),\qquad
 \mathcal C_\epsilon(L)=
 \frac{M_0(L+\epsilon/2)M_2(L+\epsilon/2)}4.}
 \tag{12}
\]
The same bound holds pointwise for \(|L_{f_n}(x)|\), with no Gaussian
average. Indeed,
\(|pq|^n\le n!\epsilon^{-n}e^{\epsilon|pq|}
\le n!\epsilon^{-n}e^{\epsilon(p^2+q^2)/2}\).
After taking the modulus in (6), retain the nonnegative factor
\((p-q)^2\) rather than replacing it by \(2(p^2+q^2)\).
For the even positive source \(G(p)=e^{(L+\epsilon/2)p^2}\Phi(p)\),
\[
 \int_{\mathbb R^2}(p-q)^2G(p)G(q)\,dp\,dq
 =2M_0(L+\epsilon/2)M_2(L+\epsilon/2),
\]
since \(\int pG(p)dp=0\). This proves the constant \(1/4\) in
(12); it is not an omitted absolute-value cost.

Along the cancellation characteristic
\(v=v_0+2h>0,\ \lambda=\lambda_0+h\), (11) gives
\(dA_n/dh=2A_{n+1}\). Its **complete**, convergent solution is
\[
 \boxed{A_n(\lambda_0+h,X,v_0+2h)
 =\sum_{k=0}^\infty\frac{2^kh^k}{k!}
             A_{n+k}(\lambda_0,X,v_0).}
 \tag{13}
\]
The spectral kernel at the new point differs from the old one exactly
by \(e^{-2hpq}\). Expanding that exponential proves (13), including
negative \(h\) in the positive-variance domain. Its absolute majorant
is integrable because
\(e^{2|h||pq|}\le e^{|h|(p^2+q^2)}\). This avoids an unjustified
iteration of a finite-order differential identity.

Here is a remainder uniform on a whole displacement range. Fix
\(|h|\le D\), \(\lambda_0\le L\), choose
\(\epsilon>2D\), and put \(r=2D/\epsilon<1\).
For any \(r<q_*<1\) and \(K\ge0\),
\[
 \begin{split}
 \left|A_n(\lambda_0+h,X,v_0+2h)
 -\sum_{k=0}^{K}\frac{2^kh^k}{k!}A_{n+k}(\lambda_0,X,v_0)\right|
 \le n!\epsilon^{-n}\mathcal C_\epsilon(L)
 \frac{(r/q_*)^{K+1}}{(1-q_*)^{n+1}}.
 \end{split} \tag{14}
\]
This uses
\((n+k)!/(n!k!)=\binom{n+k}{k}\),
\(\sum_{k\ge0}\binom{n+k}{k}q_*^k=(1-q_*)^{-n-1}\), and
\(r^k\le(r/q_*)^{K+1}q_*^k\) for \(k>K\).
There is no unidentified order-dependent constant. In a joint
\(n,K\) limit, the displayed \(n!\epsilon^{-n}(1-q_*)^{-n-1}\)
cost must still be paid; fixed \(K\) is not a uniform large-order
closure. The formulas do not require a uniform positive lower bound
on either endpoint variance.

## 4. Complete theta-index and radial payment, jointly with order

Use the positive reflected integral approximation
\[
 \Phi_{N,U}(p)=\boldsymbol1_{|p|\le U}
 e^{|p|}\sum_{1\le a\le N}P_0(a^2\rho(|p|))e^{-a^2\rho(|p|)},
 \quad 0\le\Phi_{N,U}\le\Phi.
 \tag{15}
\]
It is only an integral approximation: no smooth spectral extension,
endpoint-jet matching, or operator-domain assertion is made about this
cutoff. Its transform and its \(x,\lambda\) derivatives still exist,
and \(A_j^{N,U}\) denotes (6) with this source. In particular it is
the actual Gaussian defect of that transform, not a truncated zero sum.

For \(j=0,2\), \(S\ge0\), write
\[
 \begin{split}
 \delta_j(S;N,U)&=\int_{\mathbb R}|p|^je^{Sp^2}
                       (\Phi-\Phi_{N,U})(p)\,dp,\\
 J^{>U}_{j,2}(S,0)&=\int_{|p|>U}|p|^j
       e^{Sp^2+|p|}\rho(|p|)^2e^{-\rho(|p|)}\,dp.
 \end{split}
\]
The positive source bounds give the explicit complete tail allowance
\[
 \boxed{\delta_j(S;N,U)\le
 5C_2(N)J_{j,2}(S,0)+B_0J^{>U}_{j,2}(S,0).}
 \tag{16}
\]
Both terms tend to zero, independently, as \(N,U\to\infty\).
For a fully elementary index allowance, the term ratio gives
\[
 C_2(N)\le
 \frac{(N+1)^4e^{-\pi((N+1)^2-1)}}
      {1-16e^{-\pi(2N+3)}}\qquad(N\ge0).
 \tag{17}
\]
The denominator is positive. The radial allowance is the explicit
one-dimensional integral
\[
 J^{>U}_{j,2}(S,0)=\frac{2}{4^{j+1}}
 \int_{R_U}^{\infty}\!\left(\log\frac{s}{\pi}\right)^j
 \left(\frac{s}{\pi}\right)^{1/4}s
 e^{S\log^2(s/\pi)/16-s}\,ds,
 \qquad R_U=\pi e^{4U}.
 \tag{18}
\]
For example, if \(R_U\ge\max\{\pi,4S^2/(e^4\pi)\}\), then
\[
 J^{>U}_{j,2}(S,0)\le
 \frac{2c_j}{4^{j+1}\sqrt\pi}
 2^{5/2}\Gamma(5/2,R_U/2),\quad
 c_0=1,\quad c_2=(8/e)^2.
 \tag{19}
\]
To see this, use \(\log x\le(4/e)x^{1/4}\), and
\((\log x)^j\le c_jx^{1/4}\) for \(x\ge1\), \(j=0,2\).
The stated threshold makes \(S\log^2(s/\pi)/16\le s/2\).
Here \(\Gamma(5/2,z)=\int_z^\infty u^{3/2}e^{-u}du\); the formula
is a tail bound, not an uncomputed constant depending on \(n\).

Take \(S=L+\epsilon/2\), and define
\[
 \mathcal T_\epsilon(L;N,U)=\frac14
 [M_2(S)\delta_0(S;N,U)+M_0(S)\delta_2(S;N,U)].
 \tag{20}
\]
Then for every \(n,X,v\) in (12),
\[
 |A_n-A_n^{N,U}|\le n!\epsilon^{-n}
                         \mathcal T_\epsilon(L;N,U).
 \tag{21}
\]
Indeed the product difference after absorption is positive and even in
each source coordinate. Its integral against \((p-q)^2\) is
\(2[M_0(S)M_2(S)-M_0^{N,U}(S)M_2^{N,U}(S)]\), at most twice the
bracket in (20). This proves (21) without dropping an uncontrolled
cross term.

Combining (14) and (21) yields the usable joint approximation theorem:
\[
 \boxed{\begin{split}
 &\left|A_n(\lambda_0+h,X,v_0+2h)
 -\sum_{k=0}^{K}\frac{2^kh^k}{k!}A_{n+k}^{N,U}(\lambda_0,X,v_0)\right|\\
 &\quad\le n!\epsilon^{-n}\left[
 \mathcal C_\epsilon(L)\frac{(r/q_*)^{K+1}}{(1-q_*)^{n+1}}
 +\frac{\mathcal T_\epsilon(L;N,U)}{(1-r)^{n+1}}\right].
 \end{split}} \tag{22}
\]
The source-error sum has been extended to infinity using the same
binomial identity. This controls complete index, complete radial line,
complete order series and unbounded center simultaneously. For a growing
\(n\), it prescribes how \(K,N,U\) must increase to meet an absolute
tolerance; it does not assert such a tolerance is cheap or a favorable
signed margin exists. No derivative of the radial indicator is taken.

## 5. Every finite real multiplicity, with explicit remainder

Suppose a real canonical field has exact order \(m\ge2\) at an event:
\[
 \partial_x^jH_{\lambda_*}(x_*)=0\ (0\le j<m),\qquad
 a=a_m=\partial_x^mH_{\lambda_*}(x_*)\ne0.
 \tag{23}
\]
Fix a compact real time interval containing \([\lambda_*-T,\lambda_*]\),
with upper bound \(L\ge0\). Set
\[
 g(t,y)=\partial_x^{m-2}H_{\lambda_*-t}(x_*+y),\qquad
 C=\frac12M_{m+1}(L),\qquad D=\frac12M_{m+2}(L).
 \tag{24}
\]
Thus \(g_t=g_{yy}\), \(g(0,0)=g_y(0,0)=0\),
\(g_{yy}(0,0)=a\), and the **global real-line** bounds
\(|g_{yyy}|\le C\), \(|g_{yyyy}|\le D\) hold for \(0\le t\le T\).
Equation (5) makes their dependence on every finite \(m\) explicit:
for example \(C\le(m+1)!\beta^{-m-1}B_0J_{0,2}(L,\beta)/2\),
and the analogous bound with \(m+2\) holds for \(D\).

Taylor expansion on the real line and the time integral of the heat
equation give, for every real \(y\) and \(0\le t\le T\),
\[
 \begin{array}{ll}
 g=a(y^2/2+t)+R_0,&
 |R_0|\le C(|y|^3/6+t|y|)+Dt^2/2,\\
 g_y=ay+R_1,&|R_1|\le C(y^2/2+t),\\
 g_{yy}=a+R_2,&|R_2|\le C|y|+Dt.
 \end{array} \tag{25}
\]
For instance \(g(0,y)-ay^2/2\) is at most \(C|y|^3/6\), and
\(|g_{yy}(s,y)-a|\le C|y|+Ds\). Integrating the latter in \(s\)
proves the first row. The second uses
\(g_y(t,y)-g_y(0,y)=\int_0^tg_{yyy}(s,y)ds\); the third is the
same spatial/time bound. No root expansion or root labeling is used.

The leading Laguerre defect is \(a^2(y^2/2-t)\). More precisely,
put \(b=|a|\), \(\mu_1=\sqrt{2\kappa/\pi}\). Direct integration
of (25) under \(y\sim N(0,\kappa t)\) gives
\[
 \boxed{\begin{split}
 |\mathcal E_m(t)|\le E_\kappa(t;b,C,D):={}&
 bC\mu_1(4+10\kappa/3)t^{3/2}\\
 &+\left[bD(3+\kappa)/2+
            C^2(1+2\kappa+5\kappa^2/4)\right]t^2\\
 &+CD\mu_1(\kappa/3+3/2)t^{5/2}+D^2t^3/2.
 \end{split}} \tag{26}
\]
For a check of all constants, with \(y=\sqrt t\,z\), the absolute
error in \((g_y)^2-gg_{yy}\) is bounded by
\[
 \begin{split}
 &bCt^{3/2}(4|z|+5|z|^3/3)
 +bDt^2(3/2+z^2/2)\\
 &\qquad+C^2t^2(1+2z^2+5z^4/12)
 +CDt^{5/2}(3|z|/2+|z|^3/6)+D^2t^3/2.
 \end{split}
\]
Use \(Ez^2=\kappa\), \(Ez^4=3\kappa^2\),
\(E|z|=\mu_1\), and \(E|z|^3=2\kappa\mu_1\).
The complete real-line source bounds pay the Gaussian tails directly:
no unknown background outside a local collision neighborhood is omitted.
This proves (1), uniformly in a fixed event's declared \(t\) range.
For any real heat field with these same global real derivative bounds
and finite Gaussian defect, (25)–(26) remain valid with its own \(C,D\).
Entire continuation alone is not substituted for an integrability bound.

For \(\delta_\kappa=1-\kappa/2>0\), the explicit sufficient
resolution condition is
\[
 E_\kappa(t;b,C,D)\le\tfrac12\delta_\kappa b^2t
 \quad\Longrightarrow\quad
 A_{m-2}(\lambda_*-t,x_*,\kappa t)
 \le-\tfrac12\delta_\kappa b^2t<0.
 \tag{27}
\]
It holds for every sufficiently small positive \(t\) at every fixed
finite event. After division by \(b^2t\), its costs are explicitly
\((C/b)\sqrt t\), \([(D/b)+(C/b)^2]t\),
\((CD/b^2)t^{3/2}\), and \((D/b)^2t^2\), with the coefficients
in (26). A uniform upper bound on source moments does not give a
uniform positive lower bound on \(b\), or a uniform event radius.
No order bound on \(m\) has been imposed.

For completeness, the same estimate can be stated in purely local
analytic data with a paid exterior tail. If \(|H|\le B\) on a
complex cylinder \(|\lambda-\lambda_*|\le T_0\),
\(|z-x_*|\le R\), choose \(r_0=R/2\), \(t\le T_0/2\), and
replace \(C,D\) in (26) by
\[
 C_{\rm loc}=B(m+1)!(2/R)^{m+1},\qquad
 D_{\rm loc}=B(m+2)!(2/R)^{m+2}.
 \tag{28}
\]
Cauchy's formula gives (25) on \(|y|\le r_0\). If globally
\(|L_g|\le G\), the additional error is at most
\[
 \left[G+b^2t(1+\kappa/2)\right]P(z_0)
       +b^2\kappa t\,z_0\varphi(z_0),\qquad
 z_0=\frac{r_0}{\sqrt{\kappa t}},
 \tag{29}
\]
where \(\varphi(z)=(2\pi)^{-1/2}e^{-z^2/2}\) and
\(P(z)=2\int_z^\infty\varphi(u)du\).
Indeed \(E[y^2\boldsymbol1_{|y|>r_0}]
=\kappa t[P(z_0)+2z_0\varphi(z_0)]\).
For the canonical field one may take
\(G=(m-2)!\epsilon^{-(m-2)}\mathcal C_\epsilon(L)\) from (12).
The canonical source also pays
\(B\le B_0J_{0,2}(\max\{0,\lambda_*+T_0\},R)/2\).
Thus (28)–(29) expose radius, amplitude and multiplicity costs when
local rather than global derivative data are used; the tail is
exponentially small as \(t\downarrow0\). The global proof (24)–(26)
is stronger here and needs no cutoff.

The finite heat polynomial makes the all-m mechanism especially
transparent: for
\(H(\lambda_*-t,x_*+y)=a_m e^{t\partial_y^2}y^m/m!\),
\(\partial_y^{m-2}H=a_m(y^2/2+t)\) exactly. Equation (1) is then
exact with zero remainder for every integer \(m\ge2\).
For a general field, (25) pays its complete analytic background.
Direct \(A_n\) observables remain smooth at the event at fixed
positive variance. There is no division by \(H\) or singular root
coordinate; the shrinking-variance limit and normalization by \(a_m\)
are separately displayed comparison costs.

## 6. Exact quadratic/cubic controls and the variance conflict

For \(Q(x)=x^2+d^2\),
\[
 L_Q=2(x^2-d^2),\qquad
 A_0(Q;X,v)=2(X^2+v-d^2).
 \tag{30}
\]
Thus its imaginary pair is detected at \(X=0\) precisely when
\(v<d^2\). The exact antiheat family
\(Q_\lambda=x^2-2(\lambda-\lambda_*)\) has
\(d^2=2t\), \(a_2=2\), and gives (1) exactly.

For \(C_c(x)=x(x^2+c)\), \(c>0\),
\[
 \begin{split}
 L_{C_c}&=3x^4+c^2>0,\qquad A_0(C_c;0,v)=9v^2+c^2>0,\\
 L_{C_c'}&=18x^2-6c,\qquad
 A_1(C_c;X,v)=18(X^2+v)-6c.
 \end{split} \tag{31}
\]
The first level misses its imaginary pair even without smoothing;
the derivative level detects it at \(X=0\) for \(v<c/3\).
The exact antiheat family
\(C_\lambda=x^3-6(\lambda-\lambda_*)x\) has \(c=6t\),
\(a_3=6\), and
\(A_1=36t(\kappa/2-1)\) for \(v=\kappa t\), again exactly.
These are controls for the diagnostic, not candidate theta fields.

The event-resolving schedule is
\[
 v(\lambda)=\kappa(\lambda_*-\lambda),\qquad v'=-\kappa,
 \qquad
 \frac{dA_n}{d\lambda}=-(1+\kappa/2)\partial_{XX}A_n+2A_{n+1}.
 \tag{32}
\]
It retains a spatial term. By contrast, cancellation requires
\(v'=2\). A characteristic reaching \(\lambda_*\) has
\(v(t)=v_*-2t\). If \(v_*>0\), it lies outside \(0<v<2t\)
near the event. If \(v_*=0\), it has negative variance for \(t>0\).
Consequently no positive cancellation characteristic stays in that
resolving cone all the way to the event.

More quantitatively, start at
\(\lambda_0=\lambda_*-t_0\), \(v_0=\kappa t_0\), and advance
\(h\ge0\) along the cancellation characteristic. Then
\[
 t=t_0-h,\qquad v=\kappa t_0+2h,\qquad
 v<2t\iff h<\frac{2-\kappa}{4}t_0.
 \tag{33}
\]
The resolving cone therefore ends at the exact advance
\[
 \boxed{h_{\rm exit}=(2-\kappa)t_0/4.} \tag{34}
\]
Following the same characteristic toward smaller \(\lambda\) keeps
the variance positive for only \(s<\kappa t_0/2\), where
\(\lambda=\lambda_0-s\). These are exact variance constraints;
local remainders may shrink the genuinely resolving region further.
For \(h\ge0\), (13) conditionally propagates nonnegativity if
**every** required initial \(A_{n+k}\) is nonnegative. Those signs
are not supplied by (12), and the transported variance does not retain
resolution. No monotone collision consumer follows from cancellation.

## 7. The remaining canonical comparison and control screen

The unpaid quantity is the sign of the complete quadratic source form
\[
 \mathcal Q_n(\lambda,X,v)=\frac18\int_{\mathbb R^2}
 (-pq)^n(p-q)^2F_\lambda(p)F_\lambda(q)
 e^{-v(p+q)^2/2}\cos(X(p+q))\,dp\,dq=A_n.
 \tag{35}
\]
One sufficient event-conditioned estimate would be, for every relevant
canonical event of order \(m\), a \(t\in(0,T]\) and a fixed
\(0\le c<\delta_\kappa=1-\kappa/2\) such that
\[
 \mathcal Q_{m-2}(\lambda_*-t,x_*,\kappa t)
 \ge-c|a_m|^2t,
 \tag{36}
\]
and \(E_\kappa(t;|a_m|,C,D)<(\delta_\kappa-c)|a_m|^2t\).
Together with (1), these two strict-margin conditions would contradict
the event. An estimate (36) valid for all sufficiently small \(t\)
would in particular suffice. Unconditional nonnegativity on
those windows would be a stronger sufficient input. Neither (36) nor
that stronger sign has been proved here. No equivalence to an entire
real-rootedness class is asserted.

The complete-source absolute bounds in (12), (16) and (22) provide
finite acquisition with all costs exposed. They do not control (35)
with a favorable sign or by a canonical margin normalized to
\(|a_m|^2t\). For example, the uniform allowance (12), divided by
that margin, costs
\((m-2)!\epsilon^{-(m-2)}\mathcal C_\epsilon(L)/(|a_m|^2t)\),
which need not be small. This is a limitation of that **allowance**,
not a lower bound on the actual defect or proof that sharper
source-sensitive estimates cannot work. For each fixed known event
and tolerance the tails can be made arbitrarily small; no uniform
event-amplitude lower bound or inexpensive choice has been acquired.
Ordinary positive energy in (9) and the all-order identity (13) do not
pay this signed comparison.

The relevant control screen is precise:

| Control class | Shared part of this package | Canonical premise it fails |
| --- | --- | --- |
| Exact quadratic and cubic heat polynomials | Heat hierarchy, Gaussian identities, all-m local signal; integrals converge | The literal complete positive theta-source representation |
| Euler-factor controls in result12 | Even positive source, suitable complete moments, generic heat and quadratic formulas with their own constants | The unchanged canonical theta arithmetic expansion |
| Weighted-square controls | Integral/heat and local calculations when their own source moments are used | Complete canonical coefficient sequence and full reflected endpoint data |
| Reflected, smooth-shape and positive-primitive colliding sources | Generic analytic/heat identities and collision diagnostic under their declared tail bounds | The exact canonical integer-square theta expansion |
| Variable-kernel/counter-kernel relaxations | Only identities for the equations they actually retain | The literal cosine observation or full Newman heat equation where it was changed |

In particular [M section 10](../manuscript/sections/09_control.tex)
already gives a strictly positive, even, super-Gaussian source with
an exact double collision. It shares regular field/energy evolution
and finite moment bounds, and hence the local diagnostic here; it
fails the literal theta source. No source-independent positivity
argument based only on these shared properties can exclude its event.
The weighted and smooth classes are not assigned the canonical numerical
constants or additional global properties they have not proved.
Naming a failed arithmetic premise does not itself estimate (35).
The scope excludes a generic-energy or automatic-characteristic
exclusion, not every possible localized metric or theta comparison.

## 8. Source status and one bounded consistency pass

[Receipt13](../references/13_TND_O_LOCALIZED_LAGUERRE_SOURCE_TRIAGE_20261107.md)
records classical Laguerre antecedents and inspected abstracts only.
No theorem, criterion, numerical constant, full-paper reading or novelty
claim is imported from them. This note derives the normalization and
hierarchy from the frozen complete source and heat equation. The
[finite heat normal form](../manuscript/sections/08_multiplicity.tex)
and [Note19](19_TND_O_E12_COLLISION_STABLE_MOMENT_ASSEMBLY_20261107.md)
are inherited background; the present proof instead uses direct field
derivatives and pays the Gaussian average without root labels.

One same-executor analytical consistency pass checks the \(1/2\)
transform normalization, \(1/8\) and \(1/4\) quadratic factors,
variance convention, fixed-\(v\) kinetic identity, both heat signs,
order-series exponential, even-source cancellation in (12)/(21),
binomial remainder, radial/index tails, all coefficients in (26),
local Cauchy/exterior-tail variant, quadratic/cubic controls and the
two characteristic directions. The pass repairs three spacing escapes
and makes the sufficient comparison's remainder margin explicit; it
changes no theorem, coefficient, sign or observable. This is internal
LLM checking with shared
premises, not independent or specialist assessment. No numerical or
symbolic research run, shared-file edit, manuscript snapshot, transcript,
commit or push was made by this worker.

The lead changed the live register after the frozen version was consumed,
solely to record E14 complete and E15/Green work active. The consumed
register remains 15091 bytes, SHA-256
`48177a2cd97efb3bad8f7b710edf5e95c364e2e43897adf0e3fbe3f76f875939`;
the separately reported final status version is 15977 bytes, SHA-256
`bcd5244f4f0214177613d00df9bf90ad89d7d75212dd8bb819b608958f791079`.
All other frozen mathematical inputs remain unchanged. This records
version provenance rather than silently replacing the input freeze.

**Next:** assess this exact theorem package, then a bounded B decision
on a source-sensitive signed estimate or amplitude-normalized consumer.
The all-m negative signal, complete-source remainder and quantified
variance conflict are available inputs; canonical event exclusion is not.

# E03 r1: complete finite-source signed-logarithm acquisition

8 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Actual backend model and reasoning
effort are not recorded in the accessible capture metadata. Three
inherited-configuration helpers assisted the analytical checks; these are
internal checks with shared premises, not independent specialist review.

**Status: proved in-note from the named inherited inputs, with proof-author
checking only.** This completes [Request09 r1][request], equations
(E1)–(E9), without changing its source, observable or constants. One bounded
scope-clarification cycle is recorded in section 10. The favorable canonical value remains
unacquired. The [sole register][register] owns live status.

## 1. Statement, inputs and classification

Work only at Newman time zero. Fix
\[
 s(z)=\frac{1-iz}{2},\quad H_0(z)=\xi(s(z))/8,\quad
 F(z)=\frac{s(z)-1}{s(z)}\zeta(s(z))=D_0(z)H_0(z),
\]
\[
 D_0(z)=\frac{16\pi^{s(z)/2}}{s(z)^2\Gamma(s(z)/2)},\quad
 a=\pi/8,\quad K(u)=\frac1{16\cosh(au)}.
 \tag{1}
\]
The inherited single-boundary identity is
\[
 J_0^{\rm G}(X)=\int_{\mathbb R}K(x-X)\log|F(x)|\,dx-P(X)+G(X,1),
\quad G(X,1)=\operatorname{atanh}\frac{\sin a}{\cosh(aX)}.
 \tag{2}
\]
Its canonical Green/source inputs retain their recorded internal assessment
levels. We audit the prime normalization in section 6. We rederive below
the line estimate of [B02 Note04][local] rather than assume that an area
estimate controls a trace.

For integer R>=1, integer Q>=2 and 0<delta<=1, let a compact measurable
approximation satisfy sup_{|x-X|<=R}|F(x)-Fhat(x)|<=delta. Define
\[
 \mathcal I_{X,R,\delta}
 =\int_{X-R}^{X+R}K(x-X)\log(|\widehat F(x)|+\delta)\,dx,
\]
\[
 U_{R,Q,\delta}(X)=\mathcal I_{X,R,\delta}
       +\mathcal T(X,R)-P_Q(X)+\beta_Q+G(X,1).
 \tag{3}
\]
With the explicit quantities (6), (11), (12) and (18) below,
\[
 \boxed{0\le U_{R,Q,\delta}(X)-J_0^{\rm G}(X)
 \le\mathcal E_{X,R}(\delta)+2\mathcal T(X,R)+2\beta_Q.}
 \tag{4}
\]
For every prescribed real X and h>0 there are finite R,Q,delta and literal
theta-source cutoffs attaining an error at most h. All multiplicities are
retained. This is an **acquisition theorem** under [avoid01][target]: its
gain is the explicit error modulus, not a new representation or sign
criterion. In particular neither (4) nor smaller source errors supplies
\[
 \overline U<m(d,r),\qquad
 m(d,r)=\frac{\sin(a)d}{\cosh(ar)},\quad 0<d\le1,
 \quad r\ge0.
 \tag{5, unpaid value condition}
\]
The [result index][results], [heat-flow cluster11][heat], [controls12][controls]
and [patterns index][avoid] govern the scope. Section 9 applies the specific
[control02][controlrule], [scope07][scoperule], [shared-premise05][reviewrule]
and [coupled-payment12][coupled] rules.

Preflight: 33/34 frozen file entries matched their sizes and SHA-256 hashes.
The sole difference is the already recorded shared tools/CHAT_HISTORY.md
version, 20,937 bytes, SHA-256
62e4c8323ce51c9d2a74b690594f99f609ae201141ec85fa86b9ed3e3a623e83.
No mathematical input or frozen file was changed; [return11][return]
records the exact input check. [Source-use07][sources] gives passage checks.

## 2. Audit of the local line logarithm

Keep the exact B02 constants
\[
 R_0=9/2,\quad\rho=13/3,\quad r_0=25/6,\quad B=26/3,
 \quad\kappa=\log(27/26),\quad
 c_0=\frac35\frac{\zeta(5)}{\zeta(5/2)},
\]
\[
 M_v=2|v|+26,\quad A_v=\log(M_v/c_0),\quad
 n_v=\max\{2,\lceil A_v/\kappa\rceil\},\quad
 C_v=2Bn_v e^{51A_v/n_v},\quad
 p_v=\frac{C_vn_v^2}{n_v-1},
\]
\[
 \mathcal E_v(\delta)=p_v(2\delta/M_v)^{1/n_v}.
 \tag{6}
\]
For completeness, normalize a holomorphic disk function by |f|<=1,
|f(0)|>=m>0, A=log(1/m), n=max(2,ceil(A/kappa)). Jensen bounds the
number k of zeros in the open rho disk, counting multiplicity, by
k log(R0/rho)<=A. Remove them using
\[
 b_j(z)=\frac{R_0(z-a_j)}{R_0^2-\overline{a_j}z},\qquad
 h=f/\prod b_j.
\]
The quotient has removable values at those zeros, |h|<=1 on the outer
disk by the maximum principle, and no zeros inside rho. Harnack for
-log|h|, first on smaller radii if necessary, yields
|h(z)|>=exp(-51A) on |z|<=r0, because
(rho+r0)/(rho-r0)=51 and |h(0)|>=m. Further,
\[
 |f(z)|\ge e^{-51A}\prod_{j=1}^k |z-a_j|/B.
\]
All distance ratios are less than one there. If q_*=exp(51A)t<1 and
k>0, the sublevel set |f|<t is contained in k disks of radius
B q_*^{1/k}. Each meets a horizontal line in length at most twice
that radius. Since k<=n, on a horizontal segment Gamma of length <=1,
\[
 |\{|f|<t\}\cap\Gamma|\le C t^{1/n},\qquad C=2Bn e^{51A/n}.
\]
For k=0 the set is empty when q_*<1; for q_*>=1 the right side already
exceeds the segment length. Boundary zeros on the rho circle cause no
problem: use radii increasing to rho in Harnack. The classical Jensen
and Harnack passages were freshly checked; the line calculation is B02's
derived input, not a quoted classical theorem.

If |f-g|<=epsilon, triangle inequalities give, almost everywhere,
\[
 0\le\log(|g|+\epsilon)-\log|f|
 \le\log(1+2\epsilon/|f|).
\]
Tonelli with h_*=2epsilon gives the exact layer-cake kernel
h_*/[t(t+h_*)]. On (0,h_*) use 1/t; on (h_*,infinity) use h_*/t^2.
The bounds are Cn h_*^{1/n} and Cn h_*^{1/n}/(n-1). Thus
\[
 0\le\int_\Gamma[\log(|g|+\epsilon)-\log|f|]
 \le\frac{Cn^2}{n-1}(2\epsilon)^{1/n}.
 \tag{7}
\]
Integration of Ct^{1/n} against dt/t on (0,1) also proves
integrability of log^-|f| and its bound Cn. No separation, simplicity,
nonvanishing approximant or positive lower boundary modulus is used.

For the exact canonical field, center the disks at c_v=v+4i. Their
s-images have Re s>=1/4, excluding s=0, and the pole at s=1 is removable
in F. The fractional-part identity is
\[
 F(z)=1-(s-1)\int_1^\infty\{u\}u^{-s-1}\,du.
\]
Here |s-1|<=|v|/2+6, so |F|<=2|v|+25<M_v on the outer disk.
At c_v, Re s=5/2, and the Euler product gives
|zeta(s)|>=zeta(5)/zeta(5/2); also |(s-1)/s|>=3/5. Hence
|F(c_v)|>=c0 uniformly in v, including v=0. The real unit interval
I_v=[v-1/2,v+1/2] has radius at most sqrt(65)/2<r0 about c_v.
Applying (7) to F/M_v and Fhat/M_v proves
\[
 0\le\int_{I_v}[\log(|\widehat F|+\delta)-\log|F|]\,dx
 \le\mathcal E_v(\delta),\qquad
 \int_{I_v}|\log|F||\,dx\le\log M_v+C_v n_v.
 \tag{8}
\]
These conclusions also hold on subsegments. The normalization constants
cancel in the log difference exactly. Only the exact F needs holomorphy.

## 3. Complete exact-logarithm tail

Set, exactly as in Request09,
\[
 L_0=\log(26/c_0),\quad N_0=2+L_0/\kappa,\quad
 C_{\log}=\log26+2B e^{51\kappa}N_0^2,\quad q=e^{-a}.
 \tag{9}
\]
Since zeta(5)<zeta(5/2), c0<3/5 and L0>log(130/3)>1.
In particular N0>=1/kappa. Write t_v=log(1+|v|). Then
\[
 M_v\le26(1+|v|),\quad A_v\le L_0+t_v,\quad
 n_v\le2+A_v/\kappa\le N_0(1+t_v),\quad A_v/n_v\le\kappa.
\]
Moreover log M_v<=log26+t_v<=log26(1+t_v)^2. Consequently (8) gives
\[
 \int_{I_v}|\log|F(x)||\,dx
 \le C_{\log}[1+\log(1+|v|)]^2.
 \tag{10; Request E2}
\]
This is for the complete exact logarithm, with real zeros included.

Cover each omitted side |x-X|>R by unit intervals centered at
X+(k+1/2) and X-(k+1/2), k>=R. On each, K(x-X)<=e^{-ak}/8.
Put k=R+j and S=|X|+R+2. Then 1+|v|<S+j, and
\[
 1+\log(S+j)\le1+\log S+j\le(1+\log S)(1+j).
\]
The two sides contribute 2/8, and
sum_{j>=0}q^j(1+j)^2=(1+q)/(1-q)^3. Therefore
\[
 \int_{|x-X|>R}K(x-X)|\log|F(x)||\,dx
 \le\mathcal T(X,R):=
 \frac{C_{\log}}4e^{-aR}[1+\log(|X|+R+2)]^2
 \frac{1+q}{(1-q)^3}.
 \tag{11; Request E3}
\]
This also proves absolute weighted integrability. For fixed X the bound
tends to zero as integer R tends to infinity. The height factor remains
in every joint limit. No tail for the finite approximant is needed or
claimed.

## 4. Compact weighted envelope

Partition [X-R,X+R] into its 2R unit intervals with centers
v=X+(k+1/2), X-(k+1/2), 0<=k<R. Their maximum kernel weights are
w_k=1/[16 cosh(ak)]. The log difference in (8) is nonnegative
almost everywhere. Multiplying each integral by its maximum weight
therefore gives
\[
 0\le\mathcal I_{X,R,\delta}
 -\int_{X-R}^{X+R}K(x-X)\log|F(x)|\,dx
 \le\mathcal E_{X,R}(\delta)
 :=\sum_{k=0}^{R-1}w_k
 [\mathcal E_{X+k+1/2}(\delta)+\mathcal E_{X-k-1/2}(\delta)].
 \tag{12; Request E4}
\]
Finiteness follows from (8) and boundedness of Fhat on the compact set.
The approximant's signed logarithmic integral is retained. Only the
error, which is nonnegative, has been bounded in this step.

## 5. Literal finite theta source and its full error

Use precisely [OG Note02 (22)][source] with no mollifier (A=1). For
integer N>=1 and V>0 define
\[
 \rho(u)=\pi e^{4|u|},\qquad
 \Phi_N^{\rm ref}(u)=e^{|u|}\sum_{n=1}^{N}
 [2(n^2\rho(u))^2-3n^2\rho(u)]e^{-n^2\rho(u)},
\]
\[
 \widehat H(z)=\frac12\int_{-V}^{V}\Phi_N^{\rm ref}(u)e^{izu}\,du,
 \qquad \widehat F(z)=D_0(z)\widehat H(z),
\]
\[
 C_2(N)=\sum_{n>N}n^4e^{-\pi(n^2-1)},\quad B_0=5C_2(0),\quad
 \mathcal Q=\int_{\mathbb R}e^{9|u|}\rho(u)^2e^{-\rho(u)}du,
 \quad\mathcal Q^{>V}=\int_{|u|>V}e^{9|u|}\rho(u)^2e^{-\rho(u)}du.
 \tag{13}
\]
The complete source is even by its inherited full theta reflection.
On either half-line its omitted arithmetic terms satisfy
|Phi-Phi_N^ref|<=5C2(N)e^{|u|}rho^2e^{-rho}; the full source satisfies
|Phi|<=B0 e^{|u|}rho^2e^{-rho}. Split the error into the omitted
arithmetic source inside [-V,V] and the complete source outside.
For |Im z|<=8, |e^{izu}|<=e^{8|u|}, so
\[
 \sup_{|\Im z|\le8}|H_0-\widehat H|
 \le\delta_H:=\frac12[5C_2(N)\mathcal Q+B_0\mathcal Q^{>V}].
 \tag{14; Request E5}
\]
A reflected prefix can fail to match odd derivatives at u=0. The argument
uses only its undifferentiated integral and error, so no such matching
is presumed. Its finite integral is entire in z even without source
smoothness at zero.

Here are explicit terminating majorants, useful for the finite-choice
claim without running a numerical experiment. Put
\[
 t_N=(N+1)^4e^{-\pi((N+1)^2-1)},\quad
 r_N=\left(\frac{N+2}{N+1}\right)^4e^{-\pi(2N+3)}<1.
\]
The successive term ratios decrease, so C2(N)<=t_N/(1-r_N), for
N>=0. With T=pi e^{4V}, direct substitution gives
\[
 \mathcal Q^{>V}=\frac1{2\pi^{9/4}}
 \int_T^\infty t^{13/4}e^{-t}\,dt
 \le\frac{e^{-T}}{2\pi^{9/4}}
 (T^4+4T^3+12T^2+24T+24).
 \tag{15}
\]
We used t^{13/4}<=t^4 for t>=T>=pi. The same right side at T=pi
bounds Q. Both error terms tend to zero independently.

The inherited compact multiplier can also be checked directly. The
reciprocal-gamma product [DLMF 5.8.2](https://dlmf.nist.gov/5.8#E2)
and log|1+w|<=Re w+|w|^2/2 imply
\[
 |\Gamma(w)^{-1}|\le |w|\exp\{\gamma\Re w+\pi^2|w|^2/12\}.
\]
On 0<=Im z<=8, |Re z|<=W=|X|+R, we have
1/2<=Re s<=9/2, |s|^2<=(81+W^2)/4 and 1/(2|s|)<=1.
Since gamma<1, this proves
\[
 |D_0(z)|\le\mathcal B(X,R):=16\pi^{9/4}
 \exp\{9/4+\pi^2[81+(|X|+R)^2]/192\}.
\]
In particular on the compact real interval,
\[
 \sup|F-\widehat F|\le\mathcal B(X,R)\delta_H.
 \tag{16; Request E6}
\]
This bound is never used on the full real boundary. For a chosen delta,
one may make each of 5C2(N)Q and B0 Q^{>V} at most delta/(2B), with
B here meaning the multiplier mathcal B. Then mathcal B delta_H<=delta/2,
leaving delta/2 for any additional uniform field error. A positive
allowance need not equal the actual error.

## 6. Prime baseline and the single plus pole term

The xi factorization gives D0 H0=q(s)zeta(s) exactly, where
q(s)=(s-1)/s; on the real boundary |q(s)|=1. Thus the real boundary
logarithm in (2) is precisely the critical-line log zeta. The parent
[prime proposition][prime] uses the two safe lines Re s=9/2 and 5/2.
Its Fourier transform is
\[
 \widehat K(\omega)=\tfrac12\operatorname{sech}(4\omega),\qquad
 \widehat K((\log n)/2)=\frac1{n^2+n^{-2}}.
\]
The safe-boundary minus center coefficient is
\[
 \frac{n^{-9/2}}{n^2+n^{-2}}-n^{-5/2}
 =-\frac{n^{-5/2}}{1+n^{-4}}.
 \tag{17}
\]
Absolute convergence justifies termwise integration and subtraction.
The simple zero of s-1 at z=i pays the zeta pole and contributes one
+G(X,1) to (2). Equivalently, in the full two-boundary functional for
F=D0 H0, log|D0| is harmonic with paid growth and contributes zero.
These are two descriptions of the same normalization; adding another
q correction to (2) would count the pole twice.

Explicitly, for integer Q>=2,
\[
 P_Q(X)=\sum_{2\le n\le Q}\frac{\Lambda_{\rm vM}(n)}{\log n}
 \frac{n^{-5/2}}{1+n^{-4}}\cos((X/2)\log n),\quad
 \beta_Q=\tfrac23Q^{-3/2},\quad |P-P_Q|\le\beta_Q.
 \tag{18; Request E7}
\]
Indeed Lambda(p^k)/log(p^k)=1/k<=1 and it is zero off prime powers.
The omitted absolute sum is at most sum_{n>Q}n^{-5/2}, which is at
most the integral from Q to infinity. This proof requires the stated
integer cutoff. There is no additional safe-boundary or safe-center
truncation after (18).

## 7. Assembly and finite ordered choices

Let L_comp and L_tail denote the exact integrals of K log|F| on
|x-X|<=R and its complement. By (11), |L_tail|<=mathcal T. Subtract
(2) from (3) without changing any signs:
\[
 U-J=(\mathcal I-L_{\rm comp})
       +(\mathcal T-L_{\rm tail})+(P-P_Q+\beta_Q).
 \tag{19}
\]
The three summands lie respectively in [0,mathcal E], [0,2mathcal T]
and [0,2beta_Q]. This proves (4), precisely Request09 (E9). The two
factors of two pay upper allowances replacing signed errors. No
separate absolute bound has replaced the compact signed integral.

For fixed X and h>0 the following choices are finite:

1. Choose an integer R>=1 with mathcal T(X,R)<=h/6, possible by (11).
   A search through positive integers terminates; monotonicity is not
   needed for termination.
2. Choose an integer Q>=max(2,ceil((4/h)^{2/3})). Then beta_Q<=h/6.
3. Put W_R=2 sum_{k=0}^{R-1}w_k>0 and b=h/(3W_R). For the 2R centers
   v above, choose
   \[
   0<\delta\le\min\left\{1,\min_v\frac{M_v}{2}
                      (b/p_v)^{n_v}\right\}.
   \tag{20}
   \]
   Every mathcal E_v(delta)<=b, hence mathcal E_{X,R}(delta)<=h/3.
   This includes b/p_v>=1; the imposed delta<=1 causes no failure.
4. Fix these parameters and choose finite N,V by (14)–(16), for example
   with the delta/2 source reserve above. Pay any chosen additional
   uniform field error within the other delta/2.

Then (4) gives 0<=U-J<=h. The exponent 1/n_v deteriorates with height;
this dependence is retained in (20). For a prescribed sequence of
heights or margins, repeat the choices for each tuple. Taking, for
example, h_j=m(d_j,r_j)/4 is allowed and does not establish (5).
There is no common cutoff or useful uniform cost claim. In particular
growing |X| requires paying the height factor in (11).

There is also an elementary uniform approximation statement on each
fixed compact center set |X|<=Y. After fixing R, use
M_*=2(Y+R)+26, A_*=log(M_*/c0), n_*=max(2,ceil(A_*/kappa)),
C_*=2B n_* exp(51A_*/n_*), and p_*=C_* n_*^2/(n_*-1).
Every relevant disk function can be normalized by M_* with the same
anchor c0/M_*. Thus mathcal E<=W_R p_*(2delta/M_*)^{1/n_*},
mathcal T(X,R)<=mathcal T(Y,R), and mathcal B(X,R)<=mathcal B(Y,R).
One common source approximates on [-Y-R,Y+R], and the same ordered
choices give a common error allowance on this compact set. This is
uniform accuracy of approximation; it supplies no all-center smallness
and authorizes no height scan.

## 8. Future directed evaluation: what still has to be paid

Equations (3)–(4) are analytical, not an executed numerical certificate.
A future implementation must produce an enclosing interval [Ulo,Uhi]
of width <=eta_eval for the actual U. Then overline U=Uhi satisfies
\[
 U\le\overline U\le U+\eta_{\rm eval},\qquad
 0\le\overline U-J\le\mathcal E+2\mathcal T+2\beta_Q+\eta_{\rm eval}.
 \tag{21}
\]
Such an enclosure must pay finite prime terms, G, the tail/beta
constants, compact integration, field evaluation and final arithmetic.
If using symmetric error radii e_i, the interval width is 2 sum e_i;
reserve that full width in eta_eval. Use h/2 in section 7 and a width
eta_eval<=h/2 to reserve a final tolerance h.

Here is a finite integration existence argument, with its sensitivity
visible. Keep the exact finite-source Fhat of (13). It is continuously
differentiable on the compact real interval. Choose finite bounds
Mhat>=sup|Fhat| and L>=sup|Fhat'|. They can be enclosed from its finite
integral and the analytic compact gamma multiplier. For all complex z,w,
\[
 |\log(|z|+\delta)-\log(|w|+\delta)|\le |z-w|/\delta.
\]
Let H=max(|log delta|,|log(Mhat+delta)|). The integrand
g(x)=K(x-X)log(|Fhat(x)|+delta) is Lipschitz, including at zeros,
with constant at most L_g=aH/16+L/(16delta). For a midpoint partition
of maximum cell width Delta, its quadrature error is at most
R L_g Delta (a conservative bound). This tends to zero at fixed delta.
If the field at a quadrature node is evaluated with error <=e_F, its
log error is <=e_F/delta, multiplied by the actual positive quadrature
weight; those weights have finite sum <=R/8. All such errors admit
finite choices for a prescribed positive allowance, with no cost claim.

This paragraph evaluates the **exact** Fhat in U: node errors are paid
in eta_eval, and do not change U. Alternatively a continuous evaluated
surrogate can be declared as the approximant in (3) if its uniform error,
including source and arithmetic, is <=delta. Its own integral is then
the U being acquired. Do not switch conventions or silently omit field
noise. The local lemma itself also admits measurable bounded data;
the continuity argument is used here for the literal finite integral.

The prime sum is finite, gamma has no pole on the evaluation compact,
and the argument of atanh in G has modulus <=sin(a)<1. Thus their
finite-precision enclosures can be refined to any positive absolute
tolerance for prescribed evaluable parameters. This establishes
existence, not an implementation, affordable runtime or automatic
signed cancellation at finite precision.

## 9. Obstructions, collision controls and exact scope

The inherited obstructions remain valid in their own classes:

* [OG Note01][conditioning] has a fixed-prime translated-source family
  with common source/count bounds, input distance O(eta) in the source
  norm plus finitely many fixed-safe-line jets, and Green response
  Theta(sqrt(eta)). With the fixed ordinary observation norms clarified
  by [E02 Note03][e02], it excludes moduli o(sqrt(t)), hence uniform
  Lipschitz stability on a class containing that family. It does not
  exclude (7), deteriorating height-dependent exponents, or estimates
  restricted to the unchanged canonical theta source.
* [OG Note02][source], read with E02's accepted additive real mixed-term
  correction, gives the averaged liminf residual floor
  [1/(2theta)-11/12]/zeta(5/2)^4 for fixed
  0<theta<1/2, a1=1, complex |a_n|<=1, N<=(T/2)^theta, and one
  polynomial throughout the padded center interval. It obstructs
  uniformly small sufficient quadratic certificates in that class.
  It is not a floor on J, on signed log acquisition, or on longer or
  center-adaptive polynomial methods. The square-root-excess estimate
  is derived for the real quadratic form in E02; it is not literally
  the printed v3 Lemma13 assertion or an unprojected complex bound.
* [OC Note04][oc] proves, for a multiplicity-m zero at a, the full-disk
  harmonic approximation floor inf_v integral_{D(a,ell)}|log|F|-v|dA
  >=(pi log2/2)m ell^2. At an accepted OC window centered on a real
  zero X of multiplicity m, its zero-free harmonic-baseline/full-disk
  absolute-payment recipe has Q-consumer allowance at least m log2/36
  (and log Z allowance at least eta m log2/36). E03 uses a separate one-dimensional estimate, allows
  zeros in its approximant and retains its signed measured log integral.

The [controls12][controls] screen is analytical; no numerical replay
is required for this acquisition claim.

| Control family | Premise absent or changed relative to this canonical application |
| --- | --- |
| Fixed- and growing-prime Euler factors | Literal conductor-one coefficients and unchanged xi/zeta identity change. Keep their actual arithmetic baseline, conductor, source/count constants and anchor. |
| Three-/four-weighted squares | Square support and selected endpoint data do not supply unchanged complete coefficients plus full reflection. |
| Finite theta-tail changes, nonnegative finite zero tails | They change the complete physical source. E03's finite prefix instead carries an error tending to zero relative to that unchanged source. |
| Finite-prime orbits | Selected prime data and finite prefixes do not supply full source reflection and unchanged complete arithmetic. Controlled infinite assembly is outside their finite-data exclusion. |
| Reflected super-Gaussian | Reflection, positivity and primitive endpoints do not supply theta's integer-square expansion or xi/zeta identity. |
| Smooth log-concave/positive-primitive sources | Their shape, primitive and asymptotic data do not impose the literal arithmetic source. |
| BW-01 atomic fixed-event and exact finite-profile families | Atomic/relaxed profile data or finitely matched observations do not supply complete theta coefficients, full imaginary-axis growth/profile and eventual simplicity. Continuous extensions remain subject to their own hypotheses. |
| RH-conditional normalized endpoint controls | Ordinary Dirichlet-series arithmetic fails. Do not claim failure of the completion, functional equation, leading tail or residue, which are preserved by construction. Added real doubles are allowed in (7). |
| Variable observation kernels | The full cosine oscillator/Newman readout changes, even where the amplitude is retained. E03 fixes the literal readout. |
| Actual-theta three-profile relaxation | A relaxed positive measure with finite observations is not an integer zero configuration or a physical theta event and lacks the complete source constraints. |

These missing premises prohibit assigning the canonical c0, P or source
error to a control without proof. They do **not** show that a control
fails every derived scalar inequality: a generic local acquisition
estimate can hold with its own constants. Reflection rigidity in its
stated polynomially weighted square-comb class concerns the full
conjunction, not any single shape property.

For a genuinely defective field at the time/domain under consideration,
correct acquisition converges to its own positive Green response. A
positive-time collision is not automatically a time-zero defect, and a
box that misses a control's defect may legitimately pass. Real boundary
multiple zeros contribute no interior mass and remain allowed. E03 does
not supply RH, a canonical positive lower bound, nonreal-zero existence,
an all-center value bound or a uniform critical-line zero-free margin.

## 10. Disposition and continuation boundary

The complete theorem (4), the literal source payment and all finite-choice
obligations are established at proof-author-check level. No B02 r2 trigger
was needed. [Check05][check] records the checks.
The HDA/RS alternative in Note05 remains context; the literal source was
not replaced. No numerics, manuscript integration, sibling edits or shared
summary promotion occurred. The inherited obstructions retain E02's
accepted-with-additive-correction status; this assembly does not reassess
their primary mean-value theorem.

**Additive correction log, one bounded cycle:** the draft's phrase
"accepted-window ... consumer allowance floor" did not repeat that the OC
window is centered on a real zero, and did not name its Q consumer.
Section 9 now states both conditions and the eta factor for log Z.
The short-polynomial floor is explicitly labeled an averaged liminf.
These inherited-obstruction scope clarifications change no E03 estimate,
constant, source, target or premise. The written acquisition proof itself
required no mathematical repair. Frozen inputs remain untouched.

Stop at the completed acquisition theorem. A bounded claim-level
assessment may be specified next, as described in [Continuation08][next];
it is not performed here. The subsequent consequential decision is how
to establish a favorable canonical signed value, not how to reduce an
already controllable acquisition error.

[request]: ../research-progress/handoffs/09_TND_OG_E03_SIGNED_LOG_ACQUISITION_REQUEST_20261108.md
[register]: ../research-progress/01_TND_OG_GREEN_RESOLVENT_RESEARCH_PROGRESS_20261107.md
[local]: 04_TND_OG_B02_ONE_SIDED_BOUNDARY_LOG_ACQUISITION_20261108.md
[source]: 02_TND_OG_E01_SHORT_MOLLIFIER_RESIDUAL_FLOOR_20261107.md
[conditioning]: 01_TND_OG_B01_UNIFORM_SOURCE_CONDITIONING_20261107.md
[e02]: 03_TND_OG_E02_REAL_MIXED_TERM_AND_ACQUISITION_CLARIFICATIONS_20261107.md
[prime]: ../../manuscript/sections/17_green_strip.tex
[oc]: ../../02_localized_zero_correlations/notes/04_TND_OC_B02_SIGNED_JENSEN_AND_HARMONIC_DISTANCE_20261107.md
[results]: ../../../../../../result-summaries/README.md
[heat]: ../../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[target]: ../../../../../../avoid/01_restating_the_target.md
[controlrule]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scoperule]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[reviewrule]: ../../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[coupled]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[sources]: ../references/07_TND_OG_E03_SIGNED_LOG_ASSEMBLY_SOURCE_USE_20261108.md
[return]: ../research-progress/handoffs/11_TND_OG_E03_SIGNED_LOG_ACQUISITION_RETURN_20261108.json
[check]: ../reviews/05_TND_OG_E03_ASSEMBLY_PROOF_AUTHOR_CHECK_20261108.md
[next]: ../continuation-notes/08_TND_OG_E03_RESULTS_AND_MODEL_CHANGE_20261108.md

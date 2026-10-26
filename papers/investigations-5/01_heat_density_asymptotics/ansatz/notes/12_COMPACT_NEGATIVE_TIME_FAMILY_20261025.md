# A fixed compact-negative-time family with endpoint-dependent allowances

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), recorded effort ultra**,
verified from turn metadata. Ansatz chat0003, thread
`01a17626-abf5-7a90-9ba2-7a2395254aee`.

**Status: proved in-note from the named classical inputs of Notes05/10;
same-model internal analytical assessment only.** Return to
[HDA-A02-AN05 r1][packet]. For every declared pair of fixed constants
**0<tau<=B<infinity**, the first-correction/retained-RS-integral model
has field, spatial j<=3 and direct first time error
**C(tau,B,r,b)|G|X^-5/4**, and actual residual/residual_z
**C(tau,B,r,b)|G|X^-7/4**, uniformly for **tau<=T=-t<=B**.
This note gives explicit endpoint factors and sufficient onset gates.

All N arithmetic modes, K=1 initial RS data and exact adjacent transfers
remain. The bounded correction integral is retained. No uniformity at
tau=0, growing B, through-zero join, physical transfer or useful cost is
claimed. The remaining outer allowance still grows at each fixed T>0.
No numerical, symbolic, sampling, fitting, exact-arithmetic or interval
research was executed. The [manifest][inputs] pins current inputs; the
[assessment][review] records the internal checks.

## 1. Frozen model and classical input constants

Keep complete canonical H, H_t=-H_zz, H(0,z)=xi((1+iz)/2)/8,
\[
M(w)=w(w-1)\pi^{-w/2}\Gamma(w/2)/16,\quad\alpha=M'/M,
\quad G(z)=\{M(s(z))M(1-s(z))\}^{1/2},\quad s(z)=(1+iz)/2.
\tag{CF1}
\]
The square root is positive on the real segment and continued analytically
on far-height charts. Physical q=epsilon_g^2, fixed K=k_ell k_h, actual
signed observables, potential normalization and all joining/regulator
defects are unchanged. No RH, simplicity or unknown-remainder positivity.

Fix target radii r=ell+2, b=1+h+2, and enlarged radii
\[
R=r+1,\quad Y=b+1,\quad
\Omega_X^+=\{|\Re z-X|\le R,\ |\Im z|\le Y\}.
\]
First prove on Omega_X^+ and use radius-1/2 Cauchy disks to obtain the
target jets. Further fixed enlargement, if needed, is made before setting
the classical onset. Left charts follow by evenness after right charts.

At the real center freeze
\[
L=\log(X/(4\pi)),\quad a_X=\sqrt{X/(4\pi)},\quad N=\lfloor a_X\rfloor,
\quad \overline B=\max(1,B),
\]
\[
\boxed{V_B=8\sqrt{\overline B}\,L,\qquad I_{X,B}=[X-V_B,X+V_B].}
\tag{CF2}
\]
The endpoints and every initial-data partition are independent of z,T.
Only B, fixed for the family, enters the window. Define exactly as in
Note10 EC4--11
\[
h_{\epsilon n}(z)=M((1+\epsilon iz)/2)n^{-(1+\epsilon iz)/2},
\quad \beta_{\epsilon n}=\partial_z\log h_{\epsilon n},\quad
\gamma_\epsilon=\beta_{\epsilon n}'=-\alpha'((1+\epsilon iz)/2)/4,
\]
\[
\mathcal A_{\epsilon n}(T,z)=h_{\epsilon n}e^{T\beta_{\epsilon n}^2}
 [1+\gamma_\epsilon(T+2T^2\beta_{\epsilon n}^2)],
\]
\[
Q_{X,1}(u)=S_{m(u)}(u)-S_N(u)+R_{m(u),1}(u),
\quad m(u)=\lfloor\sqrt{u/(4\pi)}\rfloor,
\]
\[
\boxed{F_{X,B}^{[1]}(-T,z)=\sum_{\epsilon=\pm1,n\le N}
 \mathcal A_{\epsilon n}(T,z)
 +\int_{I_{X,B}}k_T(z-u)Q_{X,1}(u)\,du,\quad
k_T(v)=(4\pi T)^{-1/2}e^{-v^2/(4T)}.}\tag{CF3}
\]
Here R_m,1 retains the two named RS coefficients C0 and C1 in Note10
EC4, with exact gamma M. The exact transfer S_m-S_N is not replaced
by a lower-order recurrence. All real parts remain inside initial data.
No derivative, analyticity or endpoint-parity theorem for C1 is required.

We reuse only the real initial RS import and sectorial gamma inputs
already inspected in Notes05/10; no additional external theorem or
negative-time version of a positive-time estimate is imported. They
give a classical onset X_gamma(R,Y), fixed positive constants
C0,D,g1,g2,g3,g_minus and a fixed P (P=4 is admissible in Note05), all
independent of tau,B, such that, after the local/window gates below,
\[
G(X)\ge g_-X^{7/4}e^{-\pi X/8},\quad
|G(z)|\asymp_{R,Y}G(X),\quad G(u)/G(X)\le C_0e^{|u-X|},
\tag{CF4}
\]
Define the signed initial mismatch \(E_1(u)=H(0,u)-S_{m(u)}(u)-R_{m(u),1}(u)\). Then
\[
\begin{split}
|E_1(u)|&\le C_0G(u)X^{-5/4},\\
|Q_{X,1}(u)|&\le C_0G(u)X^{-1/4}\quad(u\in I_{X,B}),
\end{split}\tag{CF5}
\]
and, writing a0=pi/8 and r_n=log(a_X/n)>=0,
\[
\beta=-a_0+\epsilon i r_n/2+\delta,\quad |\delta|\le D/X,
\quad |\gamma|\le g_1/X,\quad |\beta''|\le g_2/X^2,
\quad |\beta'''|\le g_3/X^3.\tag{CF6}
\]
Enlarge C0 once to cover the fixed gamma comparison, initial population,
Taylor-remainder and true-tail constants used below. The admissible
classical constants are not numerically instantiated. This is distinct
from hiding tau,B dependence in an unspecified constant.

The canonical real initial line is bounded by
M_H=int_0^infinity |Phi(v)|dv. Its exact heat convolution is valid for
complex targets, by source Fubini. Compact real initial data in CF3
are piecewise bounded and integrable; their heat transforms are entire
in z and differentiable in T>0. The gamma arithmetic arms are only used
on the stated far-height charts. No remote meromorphic extension enters
the heat representation.

## 2. Explicit weighted complex-kernel constants

For integers m>=0 define
\[
\mathcal M_m=\sqrt2\exp\{R+Y^2/(4\tau)+2B\}
\sum_{k=0}^m{m\choose k}Y^{m-k}(8B)^{k/2}
                 {\Gamma((k+1)/2)\over\sqrt\pi},
\]
\[
\boxed{\mathcal T_m={\mathcal M_m\over2\tau}
                     +{\mathcal M_{m+2}\over4\tau^2}.}\tag{CF7}
\]
At tau<=T<=B and |x-X|<=R, |y|<=Y, these give the actual bounds
\[
\int_{\mathbb R}|k_T(z-u)|e^{|u-X|}|u-z|^m\,du
       \le\mathcal M_m,
\]
\[
\int_{\mathbb R}|\partial_T k_T(z-u)|e^{|u-X|}|u-z|^m\,du
       \le\mathcal T_m.\tag{CF8}
\]
Proof: put v=u-x and note |u-X|<=|v|+R,
|u-z|<=|v|+Y. The complex kernel contributes exp(y^2/(4T)). Use
\[
|v|\le v^2/(8T)+2T,
\quad \int_{\mathbb R}{|v|^k e^{-v^2/(8T)}\over\sqrt{4\pi T}}\,dv
=\sqrt2(8T)^{k/2}{\Gamma((k+1)/2)\over\sqrt\pi}.
\]
The binomial expansion proves the first bound. The exact time-kernel
factor is (z-u)^2/(4T^2)-1/(2T), proving the second.
Thus the exp(Y^2/(4tau)) loss and both inverse-time costs are displayed.
This is a weighted chartwise gamma-scale estimate, not a whole-line
supremum contraction or an outer-relative stability claim.

## 3. All evolving modes and the actual residual

Impose the uniform slope gate
\[
B\{(D/X)(2a_0+L/2)+D^2/X^2\}\le1.\tag{CF9}
\]
Since r_n<=L/2, CF6 then gives
\[
|e^{T\beta^2}|\le e^{Ba_0^2+1}e^{-\tau r_n^2/4}.
\tag{CF10}
\]
Vertical gamma transport, retaining the n-dependent power, gives
|h(z)|<=C0 G(X)n^-1/2 exp(Y r_n/2). In each shell j<=r_n<j+1
there are at most 2a_X exp(-j) integers. Let
\[
c_Y=(Y-1)/2,\quad
W_d(\tau)=2^d+{3^d\over2}\sum_{k=0}^d{d\choose k}
       (8/\tau)^{(k+1)/2}\Gamma((k+1)/2).
\]
A fully explicit endpoint envelope, up to the fixed C0, is
\[
\boxed{\Pi_d=C_0^{d+1}e^{Ba_0^2+1+(Y+1)/2}
        e^{2(c_Y)_+^2/\tau}W_d(\tau).}\tag{CF11}
\]
Choose C0 sufficiently large, independently of tau,B, for the harmless
fixed powers in (1+|beta|)^d. Then
\[
\sum_{\epsilon,n\le N}|h_{\epsilon n}e^{T\beta_{\epsilon n}^2}|
 (1+|\beta_{\epsilon n}|)^d\le\Pi_d G(X)X^{1/4}.
\tag{CF12}
\]
For completeness the scalar shell sum is bounded before any modes are
dropped:
\[
\sum_{j\ge0}(j+2)^d e^{c_Yj-\tau j^2/4}
\le e^{2(c_Y)_+^2/\tau}W_d(\tau).
\]
Use c_Y j-tau j^2/4<=2(c_Y)_+^2/tau-tau j^2/8. For j>=1,
(j+2)^d<=3^d j^d; comparing each summand to the integral over [j-1,j]
of (x+1)^d exp(-tau x^2/8) gives W_d by elementary Gaussian moments.
This proves CF12 with explicit degeneration rather than an unexamined
compact-interval constant.

The first mode corrections have absolute population at most
\[
g_1\{B\Pi_d+2B^2\Pi_{d+2}\}G(X)X^{-3/4}
\tag{CF13}
\]
after multiplication by (1+|beta|)^d. No arithmetic mode is deleted.
With the additional near-cutoff gate in CF24, the near-cutoff band
still has order sqrt X modes and absolute weight
comparable to G X^1/4, with constants depending on the fixed family.
None of these absolute bounds is a leading asymptotic for the signed H.

The exact product residual from Note10 EC24 is valid for all T. Its
explicit hand expansion, with eta=beta'' and zeta=beta''', is
\[
\begin{split}
{\mathcal A_T-\mathcal A_{zz}\over he^{T\beta^2}}
={}&-\gamma^2(3T+18T^2\beta^2+8T^3\beta^4)
 -4T\beta\eta(1+T\beta^2)\\
&-\zeta(T+2T^2\beta^2)
 -\gamma\eta(18T^2\beta+12T^3\beta^3)\\
&-\gamma^3(6T^2+24T^3\beta^2+8T^4\beta^4).
\end{split}\tag{CF14}
\]
In particular all transport and coefficient derivatives are retained.
Define the fixed-endpoint polynomials
\[
P_2(B)=g_1^2(3B+18B^2+8B^3)+4g_2(B+B^2),
\]
\[
P_3(B)=g_3(B+2B^2)+g_1g_2(18B^2+12B^3)
                 +g_1^3(6B^2+24B^3+8B^4),
\quad\mathcal R=\Pi_4\{P_2(B)+P_3(B)\}.
\tag{CF15}
\]
For X>=1, CF14 is bounded by X^-2(P2+X^-1 P3)(1+|beta|)^4.
Thus the full summed residual is <=mathcal R G(X)X^-7/4. The retained
integral has exactly zero T-heat residual: its data and endpoints are
fixed. Original time residual is the negative T-heat defect. Fixed-margin
Cauchy on the summed holomorphic residual gives its first spatial
derivative with only a fixed r,b constant, without a log X loss.

## 4. Full tails and sufficient onset gates

The proof needs both true canonical tails and artificial polynomial
completion tails. Define explicit endpoint factors
\[
\mathcal D_m={e^{Y^2/(4\tau)}\over\sqrt{4\pi\tau}}\,
      2^m(64B)^{(m+1)/2}\Gamma((m+1)/2),
\]
\[
\mathcal J_m={e^{Y^2/(4\tau)}\over\sqrt{4\pi\tau}}
\sum_{k=0}^m{m\choose k}Y^{m-k}(8B)^{(k+1)/2}\Gamma((k+1)/2).
\tag{CF16}
\]
For either family write A_m^t=A_m/(2tau)+A_(m+2)/(4tau^2).
Require
\[
V_B\ge\max(2R,R+Y+1,32B).\tag{CF17}
\]
For q=u-X with |q|>=V_B, using the bounded tilt exp(|q|),
\[
-{(q-(x-X))^2\over4B}+|q|\le-{q^2\over32B},
\quad |u-z|^m\le(2|q|)^m.
\]
Splitting this Gaussian proves tail moments at most
\[
\mathcal D_m e^{-V_B^2/(64B)}\le\mathcal D_m e^{-L^2};
\quad\partial_T\hbox{ costs }\mathcal D_m^t e^{-L^2}.
\tag{CF18}
\]

On V_B<|q|<=X/2 retain the height exponential in the true field:
|H(0,X+q)|<=C0 X^P exp(-pi X/8+pi|q|/8). Consequently the moderate
tail divided by G(X) is at most
\[
C_0X^{P-7/4}\mathcal D_0e^{-L^2},
\quad C_0X^{P-7/4}\mathcal D_0^t e^{-L^2}\quad\hbox{for time}.
\tag{CF19}
\]
For artificial tangent-quadratic completions, transverse cancellation
first reduces the whole population to C0 G(X)X^1/4 with real tilt.
Their tail/G(X) is at most
\[
C_0X^{1/4}\{\mathcal D_0+g_1X^{-1}\mathcal D_2\}e^{-L^2},
\tag{CF20}
\]
and analogously with D0^t,D2^t for time. No true gamma function or
analytic RS correction is extended to an unbounded ray.

For |q|>X/2 and X>=4R, |u-x|>=X/4. Only here use global boundedness
M_H of the complete real initial field. Splitting the Gaussian gives
remote tail/G(X) at most
\[
{M_H\over g_-}X^{-7/4}\mathcal J_0
             e^{\pi X/8-X^2/(128B)},
\tag{CF21}
\]
and the same expression with J0^t for time. This pays the height
exponential lost by using the global bound, rather than discarding it
already at distance V_B.

Set, with the fixed C0 enlarged for these inequalities,
\[
A_{\rm mod}=C_0\max(\mathcal D_0,\mathcal D_0^t),
\]
\[
A_{\rm art}=C_0\max(\mathcal D_0+g_1\mathcal D_2,
                         \mathcal D_0^t+g_1\mathcal D_2^t),
\quad A_{\rm far}=(M_H/g_-)\max(\mathcal J_0,\mathcal J_0^t).
\tag{CF22}
\]
Sufficient explicit absorption gates are
\[
L\ge P+\sqrt{\log^+[A_{\rm mod}(4\pi)^P]},\quad
L\ge2+\sqrt{\log^+[A_{\rm art}(4\pi)^2]},
\]
\[
X\ge32\pi B,\qquad
X\ge\sqrt{256B\log^+A_{\rm far}},\qquad
\log^+v=\max(0,\log v).
\tag{CF23}
\]
Indeed these imply Amod X^P e^-L^2<=1, Aart X^2 e^-L^2<=1 and
Afar exp(pi X/8-X^2/(128B))<=1. Thus every true and artificial tail,
for field and direct time, is at most G(X)X^-7/4.

Complete the onset ledger with the classical real RS/sectorial gamma
onsets and
\[
L\ge16,\quad X\ge\max(1,4R),\quad X-V_B\ge X/2,
\quad a(X+V_B)-a(X-V_B)<1,
\]
\[
C_0(V_B+R+Y)^2/X\le1,\quad D/X\le1-a_0,
\quad\hbox{CF9},\quad C_0B(1+L)/X\le1,\quad\hbox{CF17, CF23},
\quad 2g_1\{B+2B^2[a_0+1+(\log2)/2]^2\}\le X.
\tag{CF24}
\]
The linear-log gate also pays outer-carrier transport in Section6.
The last gate ensures |1+c|>=1/2 on n in [a_X/2,a_X] for the
absolute-population lower comparison; the upper error theorem does not
need that lower comparison.
The curvature gate makes the local remainder's exponential <=e.
Every gate is eventual for fixed tau,B,r,b, since V_B=O_B(log X).
These formulas specify sufficient X0 dependence, not a numerical or
certified value. No growing-time substitution into the gates is licensed.

## 5. Proved field, jets and direct time error

Let
\[
\mathcal E=3+\mathcal M_0+\mathcal M_3+\mathcal M_4,
\quad\mathcal E_t=3+\mathcal T_0+\mathcal T_3+\mathcal T_4.
\tag{CF25}
\]
**Compact-family theorem.** For every declared fixed 0<tau<=B<infinity,
after the onset CF24, uniformly on tau<=T<=B and the entire target chart,
\[
\boxed{|\partial_z^j(H-F_{X,B}^{[1]})(-T,z)|
 \le C_{r,b,j}\mathcal E\,|G(z)|X^{-5/4},\quad0\le j\le3,}
\tag{CF26}
\]
\[
\boxed{|\partial_t(H-F_{X,B}^{[1]})(-T,z)|
 \le C_{r,b}\mathcal E_t\,|G(z)|X^{-5/4},}
\tag{CF27}
\]
\[
\boxed{|\mathfrak r_F|+|\partial_z\mathfrak r_F|
 \le C_{r,b}\mathcal R\,|G(z)|X^{-7/4}.}
\tag{CF28}
\]
The C_(r,b,j) and C_(r,b) depend only on the fixed buffers and classical
input constants, not tau,B. All endpoint dependence is paid by the
displayed functions and sufficient onset gates. No logarithmic loss.

Proof of solution error independently of the residual: split the exact
canonical real initial convolution at I_X,B. Insert S_N+Q_X,1+E1 on
the window. CF5 and CF8 bound the integrated RS initial mismatch by
C0 M0 G(X)X^-5/4; the direct time cost is C0 T0 at the same power.

For each mode v=u-z, Note10 EC20 gives
\[
h(u)=h(z)e^{\beta(z)v}
 \{1+\gamma(z)v^2/2+\mathcal E_h(z,u)\},\quad
|\mathcal E_h|\le {C_0\over X^2}(|v|^3+|v|^4)e^{C_0|v|^2/X}.
\tag{CF29}
\]
The last exponential is <=e by CF24. The transverse identity remains
|h(z)e^-iy beta(z)|<=C0|h(x)|=C0G(x)n^-1/2 and |Re beta|<=1.
Only after that cancellation take absolute values. CF8 bounds the local
arithmetic error by C_(r,b) e(M3+M4)G(X)n^-1/2 X^-2 per mode;
summing all n<=N costs X^1/4, giving G(X)X^-7/4. The direct time
version uses e(T3+T4), including moments M5,M6. Completing only the
tangent-quadratic polynomial evaluates the Gaussian moment
(2T+4T^2 beta^2)exp(T beta^2), exactly the correction in CF3.
All completion and true tails are paid by CF18--24. This proves the
field and direct time bounds, with the three tail allowances absorbed
by the 3 in CF25 and X^-7/4<=X^-5/4.

The field proof is on the enlarged chart. Fixed-radius Cauchy on the
holomorphic error gives j<=3, with factors j!2^j times a fixed G-envelope
comparison, absorbed into C_(r,b,j). It is not legitimate to let spatial
derivatives hit only the kernel: the local polynomial is target-centered.
Direct T differentiation does hit only the kernel at fixed z. CF14--15
prove the actual residual separately. The exact error equation also gives
\[
|\partial_t(H-F)|\le C_{r,b}(\mathcal E+\mathcal R)|G|X^{-5/4},
\tag{CF30}
\]
using j=2 and X>=1. Thus one may take the smaller of the direct endpoint
factor E_t and the independent PDE factor E+R, with a fixed enlarged
prefactor. No asymptotic error allowance is differentiated.

No localized error PDE or Duhamel propagation estimate is used.
The fixed initial-window split has both complements paid and creates
no omitted localization commutator. CF8 is the actual gamma-normalized
kernel bound used; it is not misread as outer-relative stability.

## 6. Remaining outer scale and endpoint degeneration

Re-derive the envelope for this interval instead of importing the
T<=2 constant. The elementary amplitude is
\[
A_o(-T,z)={\pi^{1/4}z^{7/4}\over16}
e^{-\pi z/8-T\Log(z/(4\pi))^2/16+\pi^2T/64}.
\]
CF24's B(1+L)/X gate and fixed-chart gamma calibration give
\[
E_o(-T,z)\ge |A_o(-T,z)|\ge c_{r,b}|G(z)|
             e^{-TL^2/16+\pi^2T/64}.\tag{CF31}
\]
Therefore the solution and residual outer-relative allowances retain
the respective factors
\[
\boxed{X^{-5/4}e^{TL^2/16-\pi^2T/64},\qquad
       X^{-7/4}e^{TL^2/16-\pi^2T/64},}\tag{CF32}
\]
multiplied by the paid endpoint constants E/E_t and R. Dropping the
bounded favorable pi^2T/64 factor gives the familiar exp(TL^2/16) loss;
the worst uniform allowance is bounded above by the corresponding
constant times X^-p exp(BL^2/16), p=5/4 or7/4.
For each fixed T>0 its logarithm still has positive quadratic term
TL^2/16-pL+O_(tau,B,r,b)(1), and grows. This is a limitation of these
finite algebraic allowances, not an actual error lower bound or an
impossibility theorem for short resummation.

The endpoint dependence is explicit:

- As tau decreases to zero, the kernel/tail factors contain
  exp(Y^2/(4tau)); direct time bounds add tau^-1 and tau^-2. The
  population contains exp((Y-1)_+^2/(2tau)) times powers through
  tau^-(d+1)/2. These displayed majorants need not be optimal.
- As B increases with tau fixed, kernel factors grow like exp(2B)
  times fixed moment polynomials; population carries exp(pi^2 B/64),
  and the residual polynomials have degree at most four in B. The
  window coefficient is proportional to sqrt(max(1,B)); additional
  onset gates include V_B>=32B and X>=32pi B.
- The tail logarithmic gates expose exp(Y^2/(4tau)) through
  log A_mod/art; the slope/curvature/envelope gates retain their B
  dependence. Thus the theorem has no endpoint-independent height onset.

It follows neither that this method is uniform through zero nor that
one may let B grow with X. No zero-time join or large-T Gaussian overlap
is performed. Fixed-n damping exp(-T k_n^2), relative-weight scales
T log X and the distinction from T log^2 X remain component statements;
the complete signed population and RS data stay in the model.

## 7. Overlap, physical consumer and disposition

Let J=[tau,B] intersect [1,2]. If nonempty, compare CF3 and Note10's
model through the same H after both CF24 and Note10 height onsets:
for j<=3 their difference is bounded by
C_(r,b,j)(E+C10)|G|X^-5/4 on J, with the analogous time allowance.
Do not identify the formulas when V_B differs from 8L. Their arithmetic
parts agree, but their retained integrals have different fixed endpoints.
Those integral differences are themselves exact heat solutions; this
observation does not supply a new physical join.

The older growing-order outer model retains its original stated domains
and stronger accuracy there. AN05 does not extend that theorem or the
joined [-2,0] model to a new arbitrary endpoint. The maintained manuscript
remains at the assessed AN04 version until a distinct integration packet.

For this new F, insert the actual residual CF28 in parent PE37--39:
Z0=r_F conjugate(F)/D_F forces potential by 2 Re K*Z0, density by
Delta Re K*Z0/(2pi), and current by K*D_r as in Note10 EC30. The
first unpaid physical consumer is still a regulator-uniform weak/collar
comparison for this model and H, including the actual signed Q and
joining defects. Numerator bounds do not pay that transfer.

This is a quantitative approximation result under [avoid01][a01], not
an RH-equivalent criterion. Consult both the [result index][results],
especially [heat-flow11][r11] and [controls12][controls], and the
[avoid index][avoid], especially [shared premises02][a02],
[review05][a05], [scope07][a07], [constants08][a08],
[separate bounds12][a12], [imports16][a16] and [status19][a19].
The analytical control screen is unchanged: Euler-factor/normalized
endpoint perturbations fail the unchanged ordinary coefficients;
finite weighted-square, theta-cutoff and zero-tail controls fail the
full canonical xi/RS identity; reflected super-Gaussian, smooth-shape,
positive-primitive, counter-kernel, atomic and finite-profile controls
lack the same complete gamma/arithmetic identity; finite-prime matching
does not supply the full coefficients/reflection. Heat/product identities
alone exclude none. These failed premises are not collision exclusions.

**Disposition — Analysis, Sol:** accept CF26--28 from the named inputs
with explicit endpoint factors and CF24 onset ledger. Close AN05 at its
fixed compact-family scope. HDA-A02 remains **Partial**: integral-free
outer-scale formulas, growing-time limits, through-zero assembly and
physical transfer remain open. Parent HDA-17 Partial, HDA-18 Gated and
HDA-20 unfulfilled are unchanged. Same-model internal assessment only;
no independent specialist validation or numerical onset.

**Next deliverable — Analysis, Sol:** [AN06 r1][next], integrate this
assessed compact-family theorem and its endpoint dependence into the
maintained manuscript, preserving the bounded [1,2] results and unpaid
limits. Prepared only, not dispatched. No resistant mechanism warrants
Astra escalation for that routine follow-through.

[packet]: ../research-progress/handoffs/HDA-A02-AN05.md
[inputs]: 12_COMPACT_NEGATIVE_FAMILY_INPUTS_20261025.json
[review]: ../reviews/09_COMPACT_NEGATIVE_FAMILY_ASSESSMENT_20261025.md
[next]: ../research-progress/handoffs/HDA-A02-AN06.md
[results]: ../../../../../result-summaries/README.md
[r11]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a05]: ../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a08]: ../../../../../avoid/08_normalization_and_constant_slips.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a16]: ../../../../../avoid/16_unchecked_imports_and_novelty_claims.md
[a19]: ../../../../../avoid/19_status_files_that_lag_the_findings.md

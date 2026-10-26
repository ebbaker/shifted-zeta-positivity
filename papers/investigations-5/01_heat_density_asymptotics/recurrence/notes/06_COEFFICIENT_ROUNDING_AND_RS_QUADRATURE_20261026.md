# R05-AN02: coefficient, rounding and retained-RS quadrature errors

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual effort ultra**,
verified from this turn's rollout metadata. Recurrence chat0001, thread
`01a17690-2e5f-77b1-a3a4-9c31f72c117d`.

**Return: HDA-R05-AN02 r1.** The deterministic perturbation and quadrature
bounds below are **proved in-note from named inputs; same-model internal
assessment only**. They give a **conditional evaluator accuracy
specification**, not a verified floating-point implementation. Keep
\[
 p=\lfloor L/2\rfloor,\quad K=2p,\quad L=\log(X/(4\pi)),\quad1\le T\le2,
\]
all arithmetic modes, both arms, full buffers and the bounded real RS
integral. Under the explicit provider/rounding/geometry conditions below,
the output field and independently computed spatial-through-three/first-
time channels have total outer-envelope error **at most e^-L²/4**.

The new concrete gain is an actual coefficient-conditioning ledger and
an analytic **O(L²)-node-per-branch RS quadrature prescription**; the
real RS size bound alone did not supply quadrature regularity. Requested
normalized input and circuit accuracy has sufficient size
\[
 P_{\rm req}=\frac{3L^2}{8\log2}+O_{r,b}(L\log L)\quad\hbox{bits}.
\tag{E1}
\]
This is a sufficient specification in the declared model, not a necessary
precision lower bound or a theorem about a library's internal precision.
Exact discrete descriptors, certified primitive evaluations and certified
Gauss nodes/weights remain named implementation gates. No manuscript,
numerical/symbolic campaign, field sampling or software certificate.
[Inputs][inputs], [request][packet], [assessment][review] and the
[source audit][sources] pin the scope.

## 1. Frozen model, normalization and budget

Use [Note05][n5] unchanged, with canonical h(T,z)=H(-T,z), h_T=h_zz,
H(0,z)=xi((1+iz)/2)/8, complete theta source, exact gamma M and all
n<=N=floor(sqrt(X/(4pi))). Set
\[
 R=r+1,\quad Y=b+1,\quad W=R+Y,\quad V=8\sqrt2L,\quad g=G(X)>0.
\tag{E2}
\]
The physical target radii remain r=ell+2,b=1+h_av+2. Fix X,p,K,N,
coefficient data, real partitions and endpoints under z,T derivatives.
Supply the exact frozen integer descriptor (including floors), or a
certified selection/guard-strip procedure; rounded floor tests are not
assumed correct. Query coordinates z,T are exact inputs to the error
specification. Finite uncertainty in them needs its own derivative
allocation; it is not silently zeroed by the rounding model.

Write the arithmetic polynomial as `P_epsilon,p(q)=sum_(m=0)^(2p)t_epsilon,m q^m`,
normalize `beta_epsilon,n=b_epsilon,n/g`, and evaluate
\[
 F/g=\sum_{\epsilon,n\le N}\beta_{\epsilon n}
       e^{\lambda_{\epsilon n}d+T\lambda_{\epsilon n}^2}
       \sum_{m=0}^{2p}t_{\epsilon m}\mathscr H_m(d+2T\lambda,T)
       +\int_{X-V}^{X+V}k_T(z-u)Q_{X,K}(u)/g\,du,
\tag{E3}
\]
where d=z-X and the exact moment polynomials obey
`H_0=1,H_1=t,H_m=t H_(m-1)+2T(m-1)H_(m-2)`.
Q retains all real C_0,...,C_K and exact adjacent-cutoff transfer.
Real parts stay inside Q before complex-kernel integration.

For any field difference define its **center-normalized** channel norm
by the requested max of spatial orders0--3 plus first T derivative,
divided by g. Multiplication by `C_chi>=sup_target g/|G(z)|` converts
it to the natural norm. The previous positive outer envelope satisfies
`E_o>=c_o|G(z)|exp(-TL²/16+pi²T/64)`. Thus a center-normalized evaluation
error epsilon costs at most
`(C_chi/c_o)exp(L²/8)epsilon` in the outer norm.

Reserve half the target for Note05's truncation: enlarge its strict-
margin onset, using its factors8,392 instead of4,196, to obtain
`||h-F||_outer<=e^-L²/4/2`. Define the **actual evaluation budget**
\[
 \varepsilon_X=\frac{c_o}{2C_\chi}e^{-3L^2/8}.
\tag{E4}
\]
Let the center-scaled exact model have channel upper bound A_0 in E11
below. If scale error `|g_hat/g-1|<=epsilon_g<=1`, it is sufficient that
\[
 \epsilon_g A_0\le\varepsilon_X/2,\qquad
 E_{\rm ar},E_{\rm RS},E_{\rm quad},E_{\rm geo},E_{\rm round}
                                      \le\varepsilon_X/20.
\tag{E5}
\]
Indeed the unscaled evaluation error is at most
`epsilon_g A_0+(1+epsilon_g)sum E_i<=epsilon_X`, and the total outer
error, including truncation, is <=e^-L²/4. These five categories are
arithmetic input/preprocessing errors, RS node data, exact quadrature,
node/weight/endpoint geometry, and remaining operation rounding.

## 2. Arithmetic coefficient and carrier conditioning

Retain Note05's actual moments M_m,M_m^t, the complex factor exp(Y²/4),
and the direct differentiated kernel. Put
\[
 B_m=48M_m+M_m^t,\quad D_p=H_p[B],\quad
 D_p^{(1)}=H_p[qB],\quad S_p=\sum_{m=0}^{2p}B_m,
\tag{E6}
\]
where H_p is Note05's explicit positive coefficient majorant. In
`H_p[qB]`, the q^m coefficient is paired with B_(m+1). All costs refer
to enlarged-field Cauchy and direct time, not derivatives of an error
allowance. Their local time degree is 2p+4.

For logarithmic shape inputs c_r, the exact finite identity is
\[
 \partial_{c_r}P_p(q)=q^{r+1}P_{p-r}(q),\qquad1\le r\le p.
\tag{E7}
\]
For `|delta c_r|<=epsilon_c<=1`, every point on the connecting segment
has `|c'_r|<=(A+1)D^(r-1)` after dropping the favorable X^-r. Let C_j^+
be Note03's finite C_j with A replaced by A+1, C_0^+=1, and define
\[
 \mathcal C_p=\sum_{r=1}^p\sum_{j=0}^{p-r}
                          C_j^+[q^{r+1}B].
\tag{E8}
\]
This visible finite sum is the coefficient condition allowance. No
relative precision against a tiny X^-r coefficient is assumed.

Impose the additional eventual slope-neighborhood gate
`D0/X<=1/2-pi/8`. For `epsilon_lambda<=1/2`, both slopes and their
connecting segments have |Re lambda'|<=1. If
\[
 |\delta\beta_{\epsilon n}|\le\epsilon_\beta n^{-1/2},\quad
 |\delta\lambda_{\epsilon n}|\le\epsilon_\lambda,\quad
 |\delta c_{\epsilon r}|\le\epsilon_c,\quad
 |\delta t_{\epsilon m}^{\rm store}|\le\epsilon_t,
\]
then the entire center-normalized arithmetic input error is at most
\[
 E_{\rm ar}\le C_{\rm pop}X^{1/4}
 \left[\epsilon_\beta D_p+(1+\epsilon_\beta)
  \{\epsilon_\lambda D_p^{(1)}+\epsilon_c\mathcal C_p+\epsilon_t S_p\}\right].
\tag{E9}
\]
This includes both arms and every n<=N. To prove it, change beta first
with exact P and lambda, then change lambda with exact P, and change
c and aggregate storage with the perturbed beta/lambda. Use E7 for c
and the real Gaussian transform for lambda: differentiating its initial
exponential adds q. The entire connecting slope segment has real tilt
bounded by exp(|q|), so the actual B moments pay all these differences.
There is no division by the signed field or a possibly vanishing mode
correction, and no exp(+L²) bound for the carrier is introduced.

All four displayed finite condition allowances have logarithms
O((p+1)log(p+2)), by the factorial bounds in Note05. Thus E9 is paid by
absolute input accuracies `exp(-3L²/8-O(Llog L))` at p=floor(L/2).
The epsilon_t term is the certified output error of polynomial
preprocessing at the supplied c. Apply the rounding recurrence in
Section6 to that preprocessing, then charge it here; do not charge it
again in E_round. Every descriptor term is retained even if an accuracy
enclosure happens to contain zero.

Phase and scale inputs need explicit additional payments. At real X,
\[
 \beta_{\epsilon n}=n^{-1/2}
   e^{i(\theta_\epsilon(X)-\epsilon X\log n/2)},\quad
 g=e^{\Re\ell_+(X)}.
\]
If its carrier logarithm has error q_err, then
`|delta beta|<=n^-1/2 exp(q_err)q_err`, with a sufficient bound
\[
 q_{\rm err}\le |\delta\theta|+(X/2+1/2)|\delta\log n|
 +\tfrac12\log n\,|\delta X|+\tfrac12|\delta X\,\delta\log n|
                         +|\delta(\Re\log M-\log g)|.
\tag{E10}
\]
Also `|delta lambda|<=|delta ell'|+|delta log n|/2` at a fixed supplied
X, with any X-input error first propagated into ell'. In particular log n
needs absolute accuracy O(epsilon_beta/X). Unreduced phases are O(XL),
so relative-arithmetic formation needs O(L+log L) guard bits in addition
to requested absolute phase accuracy. Form scaled log differences and
certified phases; dividing separately underflowed M and g is invalid.
Use enough exponent range, not fixed machine exponents.

For the scale in E5, a sufficient center norm bound is
\[
 A_0=C_{\rm pop}X^{1/4}H_p[B]+2V B_{\rm loc}.
\tag{E11}
\]
Here B_loc is the explicit combined integrand bound in E23; total real
window length is 2V. This keeps the finite coefficient sum and transfer
costs visible, without reusing Note05's differently defined C_Q. E11 has
log^+ A_0=O(Llog L), so the required relative g accuracy has the same
sufficient requested bit scale E1.

## 3. Actual RS coefficient regularity

A real-axis size bound on C_k alone does not justify quadrature or
Cauchy differentiation in its real argument. The new input used here is
the exact classical coefficient identity recited in [Arias PartII][arias],
(29),(62),(86)--(89), attributed there to published PartI. PartI's AMS
PDF was inaccessible; no independent reading of that proof is claimed.
PartII is preliminary and flags unproved technical inequalities; **none
of its Section3.10 inequalities or blanket implementation conclusion is
used here**. The following bounds are derived directly.

Write chi for the RS fractional coordinate, to distinguish it from the
fluctuation order p. In the same **complex C_0 normalization** as Polymath,
\[
 F_0(\chi)=\frac{e^{\pi i(\chi^2/2+3/8)}-i\sqrt2\cos(\pi\chi/2)}
                           {2\cos(\pi\chi)},
\]
\[
 C_k(\chi,1/2)=\pi^{-2k}\sum_{j=0}^{\lfloor3k/2\rfloor}
          (\pi/(2i))^j d_j^{(k)}F_0^{(3k-2j)}(\chi).
\tag{E12}
\]
Every half-integer zero of the denominator is removable: at chi=n+1/2
the numerator's two terms both equal `i(-1)^(n(n+1)/2)`. Hence F_0 is
entire. The distinct real-cosine normalizations appearing elsewhere are
not substituted.

Use weighted coefficients `e_j^(k)=(3k-2j)!d_j^(k)`. Initialize e_0^0=1,
out-of-range entries zero. For m=3k-2j>0 at sigma=1/2, the exact recurrence
becomes
\[
 e_j^{(k)}=\frac{(m-1)(m-2)}4e_j^{(k-1)}-e_{j-2}^{(k-1)},
\tag{E13}
\]
where a structurally absent first term at m=1,2 is zero, not a negative
factorial. For positive even k and j=3k/2, its endpoint is
\[
 e_j^{(k)}=-\sum_{h=1}^j(-1)^h e_{j-h}^{(k)}/h!.
\tag{E14}
\]
The interior maximum is at most `(9/4)k²` times the previous maximum;
the endpoint/its partial sums cost less than twice the interior maximum.
Therefore
\[
 \max_j|e_j^{(k)}|\le E_k:=8^k(k!)^2.
\tag{E15}
\]
This also bounds positive intermediate sums in the weighted recurrence.
No unweighted huge-factorial division is needed to form these data.

On the rectangle |Re chi|<=2,|Im chi|<=1, maximum modulus gives
\[
 |F_0|\le B_F=\tfrac12[e^{2\pi}+\sqrt2\cosh(\pi/2)].
\]
On its vertical boundary |2cos(pi chi)|>=2; on its horizontal boundary
it is >=2sinh(pi). Radius-1/2 Cauchy at
`|Re chi|<=3/2, |Im chi|<=1/2` gives
`|F_0^(m)|<=B_F m!2^m`. Thus the **finite** coefficient extension satisfies
\[
 |C_k(\chi,1/2)|\le
 D_k:=\frac{B_F}{1-\pi/8}(64/\pi^2)^k(k!)^2.
\tag{E16}
\]
Its logarithm is O((k+1)log(k+2)). Fixed real derivatives also have
explicit bounds
\[
 |\partial_\chi^s C_k|\le
 B_F\pi^{-2k}E_k\sum_{j=0}^{\lfloor3k/2\rfloor}
 (\pi/2)^j\frac{(3k-2j+s)!}{(3k-2j)!},\quad s=0,1,2,
\tag{E17}
\]
by radius-one Cauchy at real chi in [-1,1]. These are chi derivatives,
not a holomorphic interpretation of an original real-part operation.
They can also pay a slower composite-midpoint rule if desired; that
fallback would have exponentially many panels at this error target.

## 4. Analytic finite branches and exact quadrature error

Split I_X only at its **exact fixed** thresholds b_n=4pi n². The existing
cutoff-span gate gives at most two real branches J. On each keep m fixed,
`a(u)=sqrt(u/(4pi))`, `chi_m(u)=1-2(a(u)-m)`, and
`U(u)=exp(-i[(u/4)Log(u/(4pi))-u/4-pi/8])`.
If A_m(u) denotes the finite complex RS expression on that branch, use
`A_m(u)+overline(A_m(bar u))`, plus the two analytic arithmetic-transfer
arms, as its holomorphic extension. This equals the original real Q_m
on J. It does **not** extend the real RS remainder theorem or move Re
outside a complex-kernel integral.

For each J use its Bernstein ellipse with parameter rho=2. It lies in
`|u-X|<=2V`, `|Im u|<=3V/4`. Every ellipse point lies within V of some
v in J. Sufficient added gates are `2V<=X/4` and
`V/sqrt(2pi X)<=1/2`, so Re u>=X/2 and chi_m stays in E16's rectangle.
The stronger local-geometry gate in Section5 can be used for all of them.

The following explicit ellipse majorant retains the actual costs. Let
\[
 a_*=\sqrt{(X-2V)/(4\pi)},\quad
 H_M=\exp(2V|\ell_+'(X)|+2HV^2/X),\quad
 H_U=\exp(V(L+1)/2),
\]
\[
 B_Q=2H_M\left[\mathcal T_X+H_Ua_*^{-1/2}
                       \sum_{k=0}^K D_k a_*^{-k}\right].
\tag{E18}
\]
Here `mathcal T_X=sum_n n^-1/2 exp(V log n)` over the actual transfer
index set (at most one n per branch, empty when m=N). The factor2
retains both arms. H_M follows from the already proved analytic ell''
bound H/X and exact ell'_+(X); the reflected arm has the same bound.
H_U follows by integrating the derivative `-i Log(u/(4pi))/4` from X;
require `sup_|q|<=2V |Log((X+q)/(4pi))|<=L+1`, an eventual elementary
gate. No gamma/phase cancellation is used to hide this conservative cost.

For a=0,1,2,3 set
\[
 P_a(v)=a!\sum_{j=0}^{\lfloor a/2\rfloor}
    \frac{(v/2)^{a-2j}(1/4)^j}{(a-2j)!j!},
\]
\[
 K_E=\frac{e^{(Y+3V/4)^2/4}}{\sqrt{4\pi}}
 [\max_{0\le a\le3}P_a(W+2V)+P_2(W+2V)],\qquad B_E=B_QK_E.
\tag{E19}
\]
These bound all complex kernel spatial channels and the actual time
channel `partial_T k=partial_z²k`, before integration. The normalized
integrands' combined norm is bounded by B_E on all branch ellipses.
In particular `log^+ B_E=O(L²)+O(Klog(K+2))`; the finite sums and
exponentials E18--19, rather than their order notation, specify the cost.

The n-node Gauss rule on J has positive weights summing to |J| and is
exact through polynomial degree2n-1; these classical facts were checked
at [DLMF3.5(v)][gauss]. For an analytic integrand bounded by B on its rho
ellipse, Chebyshev coefficients are bounded by 2B rho^-j (Cauchy after
the Joukowski map). Truncating at degree2n-1 gives uniform remainder
`<=2B rho^(-2n+1)/(rho-1)`. Positivity and polynomial exactness bound
integral minus rule by twice |J| times that remainder. Summing real
branch lengths 2V therefore proves the combined center norm bound
\[
 E_{\rm quad}\le16V B_E4^{-n}.
\tag{E20}
\]
This avoids a real mean-value derivative formula for a complex integrand.
To meet E5, take
\[
 n\ge\max\left(1,\left\lceil
           \frac{\log(320VB_E/\varepsilon_X)}{\log4}\right\rceil\right)
                                                    =O_{r,b}(L^2).
\tag{E21}
\]
There are at most two such rules. Their exact nodes/weights have not
been supplied for free: their numerical errors are charged next.

## 5. RS node data, rounded geometry and a pole-safe provider option

For each normalized RS data value at a real node, write
`A=(-1)^(m-1)M((1+iu)/2)U(u)a(u)^-1/2/g`, `R_k=a(u)^-k`.
Let its approximations have errors epsilon_A,epsilon_Rk,epsilon_Ck,
and normalized transfer error epsilon_tr. A sufficient node-data bound is
\[
 |\widehat Q_m/g-Q_m/g|\le\epsilon_{\rm tr}
 +2\sum_{k=0}^K\left[\epsilon_A R_k|C_k|
 +( |A|+\epsilon_A)
   \{\epsilon_{Rk}|C_k|+(R_k+\epsilon_{Rk})\epsilon_{Ck}\}\right].
\tag{E22}
\]
Use E16 or the stronger actual real coefficient bound in this finite
sum. All K+1 terms and the exact transfer remain; node data are real
before multiplying complex kernels. Normalized gamma ratios are formed
from log differences, U and log a from certified phases/logarithms.
On real nodes these have positive-circuit magnitude exp(O(Llog L)),
not the larger off-real ellipse bound B_E. Log/phase errors multiplied
by u~X again require E10's O(L) guard bits.

For local geometry require V>=3, put `V_1=V+2`, and strengthen the eventual gate to
`4(V+2)/sqrt(2pi X)<=1/2`, `2(V+2)<=X/4`. This keeps every fixed branch
analytic on unit neighborhoods needed below. From
`ell'_+(X)=-pi/8+iL/4+O(D0/X)`, a sufficient unit-strip gamma bound is
\[
 H_M^{\rm loc}=\exp\{(\pi/8)(V+2)+L/4+D0(V+3)/X
                                  +H(V+3)^2/(2X)\},
\quad H_U^{\rm loc}=e^{(L+1)/4}.
\]
For `|Re u-X|<=V+2`, `|Im u|<=1`, define
\[
 B_Q^{\rm loc}=2H_M^{\rm loc}
 \left[\sum_{n\in\mathcal T} n^{-1/2}n^{1/2}
       +H_U^{\rm loc}a_*^{-1/2}\sum_{k=0}^K D_k a_*^{-k}\right],
\]
\[
 K_{\rm loc}=\frac{e^{(Y+1)^2/4}}{\sqrt{4\pi}}
 [\max_{a\le3}P_a(W+V+4)+P_2(W+V+4)],\quad B_{\rm loc}=B_Q^{\rm loc}K_{\rm loc}.
\tag{E23}
\]
Use the union of actual transfer indices for a common maximum (there
is at most one). In E23 the transfer n^-1/2 times n^1/2 is kept as an
explicit conservative transverse cost. The gamma bound uses real/imaginary
parts of the frozen slope separately, not |ell'| times the whole V.
Hence `log^+ B_loc=O(L)+O(Klog(K+2))`. Radius-1/2 Cauchy bounds each
u derivative of an integrand channel by twice its local bound.

First compare with the exact rules on the original frozen real branches.
Let approximate physical weights have total absolute error
`epsilon_w=sum_i|mu_hat_i-mu_i|`, node positions have max error
`epsilon_u<=1/4` with all approximate nodes real, and each of the at most three physical boundaries
(two window endpoints and one internal threshold) has certified
uncertainty `0<=epsilon_b<=1/4`. Use the **fixed branch label** at shifted nodes;
do not recompute floor(a) from a rounded node. The actual geometry cost
is bounded by
\[
 E_{\rm geo}\le B_{\rm loc}
  [\epsilon_w+2(2V+\epsilon_w)\epsilon_u+6\epsilon_b].
\tag{E24}
\]
With exact frozen reference rules take epsilon_b=0; endpoint errors
already propagated into their nodes/weights are not charged again.
Alternatively a guard-strip construction may choose certified exact
subintervals **inside** the true fixed branches and omit strips of total
length <=6epsilon_b. Define epsilon_w,epsilon_u against those subinterval
rules. Their total length is <=2V, their ellipses satisfy the same E18--19
bounds, and the omitted integrals cost <=6B_loc epsilon_b in the combined
channel norm. This proves the last term. It handles uncertain threshold
membership near a window edge by a paid strip instead of a free floor
decision. Zero-length branches are omitted. Rules extending outside the
original window require revised total-length and ellipse allocations;
they are not covered automatically by E20,E24--25. All reference
partitions and any guard strips are frozen under z,T differentiation.

If node-data errors E22 are <=epsilon_Q, then the **separate** RS-data
cost is
\[
 E_{\rm RS}\le(2V+\epsilon_w)K_{\rm loc}\epsilon_Q.
\tag{E25}
\]
E22--25 and E5 are concrete required accuracies, all with logarithmic
conditioning cost O(Llog L). They avoid assigning unit cost to near-pole
coefficient evaluation.

One constructive coefficient-provider option uses **normalized**
Taylor derivatives `h_m(chi)=F_0^(m)(chi)/m!`, not the apparent quotient
at chi=half-integers. On the rectangle contour Gamma with Re zeta=+/-2,
Im zeta=+/-1,
\[
 h_m(\chi)=\frac1{2\pi i}\oint_\Gamma
                  \frac{F_0(\zeta)}{(\zeta-\chi)^{m+1}}d\zeta.
\tag{E26}
\]
For chi in E16's rectangle use a Gauss rule on each straight contour
edge with ellipse parameter rho_c=9/8. Its semiaxes are145/144,17/144.
On the four edge ellipses, `|Re zeta|<=9/4, |Im zeta|<=5/4`,
`|2cos(pi zeta)|>=1`, and `dist(zeta,chi)>=1/4`. Therefore
\[
 B_c=e^{45\pi/16}+\sqrt2\cosh(5\pi/8),\quad
 |F_0(\zeta)/(\zeta-\chi)^{m+1}|\le B_c4^{m+1}.
\]
With q Gauss nodes per edge, the **derived** truncation bound is
\[
 \epsilon_{h,m}^{\rm quad}\le\frac{24}{\pi}B_c4^{m+1}
                    \frac{\rho_c^{-2q+1}}{\rho_c-1}.
\tag{E27}
\]
This uses total contour length12, including the factor1/(2pi), and the
same polynomial argument as E20. For all m<=3K, a declared epsilon_h
is obtained by imposing E27 with m=3K; q=O(L²+Llog L) for the E5
budgets below. Primitive errors and contour nodes/weights still need the
same explicit node/weight/circuit accounting, with distance1/4 and
safe denominator1 instead of an arbitrarily small cos(pi chi).

Use E13--15 to form the weighted e_j^k, then
\[
 C_k=\pi^{-2k}\sum_j(\pi/(2i))^j e_j^{(k)}h_{3k-2j}.
\tag{E28}
\]
Perturbations obey the explicit product-sum bound with each summand
`|e_j|epsilon_h+|h_m|epsilon_e+epsilon_e epsilon_h`, multiplied by
`pi^-2k(pi/2)^j`; perturbations in those pi factors are paid separately
by the same product rule. All factors have logarithmic magnitude
O(Klog(K+2)). This pays the requested epsilon_Ck in E22 under declared
primitive accuracy. It neither imports PartII's unproved precision
inequalities nor claims a tested provider. Fixed contour values can be
reused over all RS nodes. Real apparent poles are handled analytically,
without dividing two nearly vanishing computed values.

## 6. Rounding circuit, bit specification and exact residual distinction

Use normalized arithmetic with sufficient exponent range. For each
actual scalar add/subtract, multiply or division by an exact positive
integer j, let A_a,A_b be certified magnitude bounds and E_a,E_b the
already propagated errors. With unit roundoff u, valid explicit updates
are
\[
 E_+=E_a+E_b+u(A_a+A_b+E_a+E_b),
\]
\[
 E_\times=A_aE_b+A_bE_a+E_aE_b
                     +u(A_a+E_a)(A_b+E_b),\quad
 E_{\div j}=[E_a+u(A_a+E_a)]/j.
\tag{E29}
\]
Apply them to real components of complex operations; for divisions by
noninteger quantities first supply a certified separation and reciprocal
error. The safe reciprocals in E26 have separation1/4; the F_0 contour
quotient has denominator at least1. Nonlinear primitive nodes have their
own certified error, not an automatic unit-roundoff guarantee. For
example, a complex exponential with exact real part <=C_0 and argument
error E_arg has the sufficient bound
\[
 E_{\exp}\le e^{C_0}(e^{E_{\rm arg}}-1)
                             +4u e^{C_0+E_{\rm arg}},
\tag{E30}
\]
for `0<u<=1/16`, if the declared exp/sine/cosine providers have relative
exp and absolute sine/cosine error <=u, with the final real products
rounded under E29. This is an explicit model assumption to verify
in a concrete implementation.

For the arithmetic channels, the moment recurrence in E3 gives
\[
 \partial_d^a(\beta e^{\lambda d+T\lambda^2}\mathscr H_m)
 =\beta e^{\lambda d+T\lambda^2}
  \sum_{j\le\min(a,m)}{a\choose j}(m)_j\lambda^{a-j}\mathscr H_{m-j},
\]
\[
 \partial_T(\beta e^{\lambda d+T\lambda^2}\mathscr H_m)
 =\beta e^{\lambda d+T\lambda^2}
  [\lambda^2\mathscr H_m+2m\lambda\mathscr H_{m-1}
                                      +m(m-1)\mathscr H_{m-2}].
\tag{E31}
\]
Evaluation of retained moments only needs degree2p; this does not remove
the 2p+4 moment degree in the **error** bounds. With `Lambda=1+L/4`,
a further eventual slope gate bounds every perturbed |lambda| by Lambda.
A positive intermediate envelope is
`t_*=W+4Lambda`, `h_0=1,h_1=t_*`,
`h_m=t_*h_(m-1)+4(m-1)h_(m-2)`.
Moreover for |Re lambda'|<=1,
`|exp(lambda' d+T lambda'^2)|<=exp(R+2+Y²/4)`;
completing the square in Im lambda proves this bound. A spurious
exp(+L²) carrier magnitude is unnecessary.

Together with H_p and E15, these give log-magnitude/conditioning costs
O(Llog L) for the actual real-node circuits. Sequential summation retains
all N and pays its full accumulation count; it is not treated as one
operation. The positive expression-path/error updates E29 give a
rounding amplification bounded by `(N+1)exp(O(Llog L))` times a polynomial
in the quadrature/provider node counts. This can also be retained as the
actual finite E29 recurrence rather than hidden in a generic gamma_S.
Its proof uses the triangular polynomial recurrence (no repeated-squaring
exponential degree), degree2p moment recurrence, weighted E13--14 and
linear accumulations. Impose the eventual small-accumulation guard
`u S_lin<=1/4`, where S_lin is the actual longest linear sum/recurrence
operation count, including all N modes and quadrature/provider sums.
E1 satisfies this eventually; the actual finite E29 test remains required.
All positive weighted coefficient paths are bounded
by E15; no exp(N) propagation is introduced.

Choose u and primitive input accuracy so that the **actual** finite
recurrence yields E_round<=epsilon_X/20 and its preprocessing part yields
the epsilon_t required by E9. Because log N=L/2+O(1), p,K=O(L), and the
outer/inner node counts are O(L²), a sufficient requested significand
precision is E1, with its O(Llog L) guard chosen from these finite
majorants. Logarithm/gamma phase formation and E10 add O(L+log L) guards.
For Gauss nodes/weights this states the required certified output
accuracy, not the internal precision, iteration count or bit complexity
of a root-finding implementation. Scale g also needs a certified
relative error as in E5. No fixed floating-point exponent range is used.

Formal scalar operation counts with named certified data supplied are:

| Part | Derived scalar count | What is not included |
| --- | --- | --- |
| Shape polynomial preprocessing | O(p³), O(p²) level storage; O(p) output coefficients | Gamma-jet providers and their bit cost |
| Full arithmetic field/jets/time sum | O(Np) | N carrier/log/phase inputs and bit cost |
| Weighted RS coefficient table | O(K²) | Primitive and rounding certification |
| Pole-safe F_0 jet provider at all outer nodes | O(n(qK+K²))=O(L^5), with fixed contour samples reused | Certified nodes/weights, primitives and bit cost |
| Outer retained-integral quadrature | At most2n nodes, n from E21; fixed channel kernels | Integral-data/gamma inputs and certified geometry |

The O(L^5) count is RS-only, not a replacement for all N arithmetic modes.
It is not a useful-runtime certificate. No numerical onset or rounding
record has been executed.

There are three distinct residual statements. Exact frozen F has
`(partial_T-partial_z²)F=0` and residual_z=0. A structured approximation
with fixed perturbed coefficients/slopes and fixed quadrature nodes,
weights and real node data is also an exact heat solution as a symbolic
function. Independently rounded channel outputs are **not** thereby an
exact heat solution: their T-minus-zz defect is bounded by the sum of
those two paid channel errors. A residual_z output requires an additional
mixed T,z channel; it is not silently asserted for rounded outputs here.
No derivative of a pointwise rounding allowance is taken.

## 7. Acceptance, unpaid provider gates and controls

Impose Note05's p=floor(L/2) structural/half-target truncation onset,
E9's slope-neighborhood gate, Sections4--5's analytic-geometry gates, and
the explicit scalar inequalities E5,E21,E22--25,E27,E29. These constitute
one sufficient **conditional** coefficient, rounding and quadrature
specification for e^-L²/4 total outer error on the declared full buffers.
The provider assumptions are visible, not a renamed unknown field error.
In particular the formerly unpaid RS regularity/analytic quadrature step
is now paid from E12--20.

Preserve the failed shortcuts: real size alone gives no quadrature rate;
naive quotient evaluation at the removable half-integer poles has no
uniform relative stability guarantee; counting scalar operations pays no
rounding; fixed machine exponents can underflow the normalization; direct
rounded floor tests can select the wrong descriptor; exact-model zero
residual does not validate independent rounded jets. PartII's preliminary
precision conclusions cannot be substituted for the E29/provider checks.
None of these scoped failures excludes a correct certified evaluator.

The **first remaining implementation step** is to instantiate certified
gamma/log/phase, scale, reciprocal and Gauss-node/weight providers, plus
frozen descriptor/boundary handling, and prove that their delivered
errors meet these finite inequalities. Exact arbitrary-real floor
selection has no uniform E1-bit claim near boundaries. Any additional
uncertainty in query coordinates also requires a paid input channel.
No concrete library or implemented evaluator has been verified here;
its internal precision/runtime and certificate remain open.

Read the [result index][results], [heat cluster][heat], [controls12][controls]
and [avoid index][avoid], especially [01][av1], [02][av2], [05][av5],
[07][av7], [12][av12] and [16][av16]. This is an approximation/evaluation
specification, not an RH criterion. Euler-factor/finite-prime controls
fail unchanged full coefficients; weighted-square/cutoff controls fail
the full canonical xi/RS identity; reflected, smooth and positive-
primitive controls lack the same complete gamma/arithmetic completion.
Heat identities themselves also hold for suitable controls. No collision,
physical transfer, new time endpoint or manuscript conclusion follows.

**Disposition — Analysis, Sol:** accept E5--31 and the total-error
implication, with [Review05][review], as proved deterministic bounds and
a conditional evaluator specification. **R05-AN02 r1 CLOSED; bounded
audit Complete. Broad R05 remains Partial** until certified providers,
descriptor handling and a concrete evaluator satisfy the contracts.
HDA-A02 Partial, HDA-17 Partial, HDA-18 Gated and HDA-20 unfulfilled
remain unchanged. No numerical or manuscript campaign.

**Next deliverable — Analysis, Sol, not executed:** reduce the named
primitive/scale/Gauss and descriptor contracts to certified finite
provider algorithms for this declared model, preserving E5 and actual
phase/endpoint costs. Return an effective specification or the first
unpaid provider inequality. An implementation or numerical run would
require a new request; none is started here.

[inputs]: 06_EVALUATION_ERROR_INPUTS_20261026.json
[packet]: ../research-progress/handoffs/HDA-R05-AN02.md
[review]: ../reviews/05_EVALUATION_ERROR_ASSESSMENT_20261026.md
[n5]: 05_CONTROLLED_ORDER_GROWTH_AUDIT_20261026.md
[sources]: ../references/02_RS_EVALUATION_SOURCE_AUDIT_20261026.md
[arias]: https://arxiv.org/html/2201.00342v1
[gauss]: https://dlmf.nist.gov/3.5.v
[results]: ../../../../../result-summaries/README.md
[heat]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[av1]: ../../../../../avoid/01_restating_the_target.md
[av2]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[av5]: ../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[av7]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[av12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[av16]: ../../../../../avoid/16_unchecked_imports_and_novelty_claims.md

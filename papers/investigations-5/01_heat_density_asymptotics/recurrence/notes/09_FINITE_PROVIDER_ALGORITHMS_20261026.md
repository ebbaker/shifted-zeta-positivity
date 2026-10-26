# R05-AN03: finite certified providers for the frozen hierarchy

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual effort ultra**,
verified from the current turn metadata. Recurrence chat0003, thread
`01a176ea-3f14-7972-bc9c-9aeb6fb50fd4`.

**Return to HDA-R05-AN03 r1. Proved in-note from the named inputs;
same-model internal assessment only.** For the finite, certified input
class below, every remaining function, coefficient, quadrature-data and
geometry provider in [Note06][n6] has a terminating finite construction.
Their delivered errors meet E5, E9, E21--29, so the already-proved total
outer error at most exp(-L²/4) follows for every exact rational query in
the declared full chart, including spatial orders 0--3 and first time.
The algorithms are specified analytically; **no evaluator implementation,
numerical run, machine-symbolic check or software certificate is supplied**.

The gain is removal of the named provider oracles on this input class.
The simple gamma construction can require exp(3L²/8+O(L log L)) terms
per call, and the deliberately elementary Gauss root search below is also
expensive. Requested output accuracy is not internal precision or useful
runtime. Broad HDA-R05 remains **Partial**. [Review07][review], the
[input manifest][inputs], and the [work record][work] delimit the result.
The manuscript still contains the preceding conditional theorem; this
later algorithm theorem has not been integrated into its sources.

## 1. Domain, frozen descriptors, and the algorithm contract

Keep exactly the canonical source and Note06's definitions:

- h(T,z)=H(-T,z), h_T=h_zz, H(0,z)=xi((1+iz)/2)/8;
- L=log(X/(4pi)), p=floor(L/2), K=2p, N=floor(sqrt(X/(4pi))),
  V=8 sqrt(2)L, 1<=T<=2, R=r+1, Y=b+1;
- both arithmetic arms and every 1<=n<=N, all C_0,...,C_K, the bounded
  real RS integral, and exact adjacent-cutoff transfer;
- the full chart and unit buffers, with X,p,K,N, shape coefficients,
  branch labels, reference endpoints and partitions fixed under z,T
  derivatives. Real node data precede the complex kernel multiplication.

An accepted input is a finite record containing exact positive dyadic
X,r,b, exact rational complex d=z-X and rational T in the full buffered
chart and [1,2], and integers p,N. It includes rational enclosure
certificates, reproducible with Section 3's algorithms, satisfying

    2p < L^- <= L <= L^+ < 2p+2,
    N < a^- <= sqrt(X/(4pi)) <= a^+ < N+1.                 (P1)

Invalid finite certificates are rejected. This is a declared restriction
of the input class, not a decision procedure for equality of arbitrary
computable reals. For strict centers, certificate search terminates;
its cost depends on
sigma=min(L-2p,2p+2-L,a(X)-N,N+1-a(X))>0 and on input bit lengths.
No uniform E1-bit floor-selection promise is made.

The record also supplies effective positive calibration bounds
c_-<=c_o, C_+>=C_chi, rational upper bounds for the fixed classical
constants A,D,D0,H, and verified strict sufficient gates from Note05's
**half-target** truncation onset and Note06's slope/ellipse/local-strip
conditions. These are inherited comparison hypotheses, not newly
instantiated numerical onsets. In particular V>=3,
4(V+2)/sqrt(2pi X)<=1/2 and 2(V+2)<=X/4. Finite comparisons use outward
rational enclosures and strict margins. The finite sums defining moments
and majorants can themselves be enclosed by Section 3; no classical
constant is assigned a unit-cost oracle. For their only extra gamma
values use Gamma(j+1)=j! and
Gamma(j+1/2)=(2j)! sqrt(pi)/(4^j j!), from the gamma recurrence and
Gamma(1/2)=sqrt(pi). Thus the moment majorants require only factorials
and the already supplied pi/square-root/exponential functions.

Choose a positive dyadic e with checked strict bounds

    (c_-/(8 C_+)) exp(-3L²/8) < e
          < (c_-/(4 C_+)) exp(-3L²/8) <= epsilon_X/2.    (P2)

Series convergence supplies this choice. It is a computable positive
budget, rather than a test against an unknown exact error. Every
allocation below has slack relative to Note06's epsilon_X.

| Provider | Finite construction | Analytic truncation and arithmetic error | Delivered contract |
| --- | --- | --- | --- |
| Center descriptors and real partitions | P1 certificates; interior rational intervals in Section 2 | Width/omission ledger, exact rational comparisons | Frozen floors and E24 |
| pi, log, sqrt, phase, exp, reciprocals | Rational series, range reduction, bisection; Section 3 | Explicit series tails; separated divisions; exact rational sums | E10, E22, E29--30 primitives |
| log gamma and normalized jets | Finite Euler product and reciprocal-power sums; Section 4 | P6--7 and finite sum errors | beta, lambda, c_r; E9 |
| Scale and gamma ratios | Log differences; mantissa and unrestricted integer exponent | Relative exponential error and P8 | E5, E10--11, E22 |
| Shape and weighted RS tables | Exact rational triangular recurrences at delivered inputs | No operation rounding; shape input error charged once | epsilon_t=0; epsilon_e=0; E9, E28 |
| Outer and contour Gauss data | Rational polynomial root isolation and rational weight formula | P9--12; exact affine mapping | E24, E27 |
| Pole-safe F_0 jets and C_k | Four-edge contour rule, all m<=3K; weighted recurrence | E27 plus P13--15 | E22, E25, E28 |
| Remaining finite evaluator circuit | Exact rational operations on delivered rational inputs | Zero internal rational-operation error; optional output rounding | E29; field and specified channels |

This exact-rational model is one finite arithmetic model allowed by the
request. It can have very large numerator/denominator sizes. A finite
floating implementation can instead use E29 with separately proved
internal precision; that implementation is not certified by this note.

## 2. Interior geometry without an edge-equality test

Write alpha=X-V, beta=X+V and theta_j=4pi j². Choose rational
0<eta<=min(epsilon_b,1/4). Obtain **strict** rational enclosures of width
at most eta for alpha,beta,theta_N,theta_(N+1), denoted
[a^-,a^+], [b^-,b^+], [t_j^-,t_j^+]. Adding a rational padding after
refinement makes enclosures strict even when an endpoint is rational.

Call j a candidate when its rational enclosure intersects [a^-,b^+].
Every candidate lies in [alpha-2eta,beta+2eta], inside
[X-(V+1),X+(V+1)]. There

    a'(u) <= 1/(2 sqrt(2pi X)),
    span a <= (V+1)/sqrt(2pi X) <= 1/8.                 (P3)

The local gates imply P3 since u>=X/2. Thus at most one threshold can
be a candidate. Because X is inside the window with a(X) in (N,N+1),
only N,N+1 can occur; every true threshold is a candidate.

If there is no candidate retain [a^+,b^-], with label N. With candidate
j retain, when their rational lengths are positive,

    [a^+, min(b^-,t_j^-)], label j-1;
    [max(a^+,t_j^+), b^-], label j.                      (P4)

Discard any resulting piece of length at most eta. Every retained
interval lies inside its true original branch. Endpoint trimming and
the threshold enclosure omit at most 3eta total length; discarding two
short pieces adds at most 2eta. Hence omission costs at most
5eta B_loc<=6epsilon_b B_loc in the combined channel norm. This handles
a threshold exactly at an edge, one just outside, and a vanishing branch
without deciding any real equality. There is no division by branch length.

Apply exact reference Gauss rules to these retained rational intervals.
Their total length is at most 2V. A subinterval's Bernstein ellipse is
inside its parent interval's ellipse: it is a convex combination of a
parent ellipse point and a real point in that ellipse. Thus E18--21's
bounds and 16V B_E 4^-n still apply. Endpoint trimming is charged once
through omitted integrals. Shifted rational nodes are chosen inside the
retained intervals and keep their labels; they are not assigned a new
floor. The reference intervals and all omissions are frozen for derivatives.

## 3. Elementary providers with rational remainders

All series below are evaluated in exact rational real/complex arithmetic;
partial sums plus the displayed tails give outward enclosures. Convert
an enclosure to a rational center and radius only after it meets the
requested tolerance. Interval input uncertainty is propagated as well.

For x>0 rational, exact comparisons give x=2^k y, 1<=y<2. With
t=(y-1)/(y+1), |t|<=1/3,

    log y = 2 sum_(j=0)^(M-1) t^(2j+1)/(2j+1) + R,
    |R| <= 2 |t|^(2M+1)/((2M+1)(1-t²)).                 (P5)

Compute log2 by t=1/3 and pay its error multiplied by |k|. The formula
is the integral of the geometric series. Positive interval inputs are
first bounded away from zero; monotonicity encloses their logarithms.
Positive square roots use exact rational square comparisons and bisection
on a scaled [1,4] argument. Each interval has its declared dyadic width.

Use the alternating arctangent series for |t|<=1/2, with remainder at
most |t|^(2M+1)/(2M+1). For 1/2<=t<=1, reduce via
atan t=atan(1/2)+atan((t-1/2)/(1+t/2)); the new argument is <=1/3.
For t>1 use pi/2-atan(1/t), and use oddness for negative arguments.
The identity pi=4[atan(1/2)+atan(1/3)] follows from tangent addition and
the angle range. It gives a convergent rational pi enclosure without a
pi oracle. For x>0, Log(x+iy)=log(x²+y²)/2+i atan(y/x).
Interval evaluation subdivides at rational reduction boundaries if needed;
either neighboring valid formula has the same value there.

For exp(a), enclose a/log2 to width <=1/8 and round its rational
midpoint to a nearest integer k, with a deterministic rational tie rule.
Then |a-k log2|<=9 log2/16<2, with strict margin. This k is a free
encoding choice, not a mathematical floor. Keep k fixed and refine
log2 to error at most eta/(1+|k|).
Taylor truncation of exp at residual modulus <=2 has error at most
9*2^(M+1)/(M+1)!. Return a rational mantissa times 2^k, with unrestricted
integer exponent. For exp(i theta), choose a nearby integer multiple of
2pi from coarse rational data, refine pi until its multiplied error is
paid, and certify residual modulus <=4. Its Taylor error is at most
81*4^(M+1)/(M+1)!. Specifically, enclose theta/(2pi) to width
<=1/8 and round its rational midpoint: the fixed integer then gives
residual <=9pi/8<4, with strict margin, so the certification terminates.
For a requested relative real-exp tolerance tau, require absolute Taylor
error <=tau/9 since exp(residual)>=1/9; pay residual input error
separately. These bounds follow from the integral Taylor
remainder and exp(2)<9, exp(4)<81. The nonnegative series verifies both
crude constants if desired. The factorial tails tend to zero.

For a complex exponential, the exact input perturbation bound is
|exp(z+q)-exp(z)|<=exp(Re z)(exp(|q|)-1). Constructing real exp and
absolute sine/cosine to the tolerances assumed in E30 therefore supplies
that primitive condition. Large phases require pi/log errors divided by
(1+|theta|); they are not reduced using inaccurate constants for free.

If |a|>=d>0 and |a_hat-a|<=eta<d, then
|1/a_hat-1/a|<=eta/[d(d-eta)]. Rational a_hat has an exact rational
reciprocal. Every required denominator is accompanied by a certified
separation. In interval computations, refine until a positive separation
is seen; the mathematical lower bounds below prove termination.

Every truncation order is selected by a strict rational tail inequality.
No transcendental evaluation is left as an exact-function oracle.

## 4. Gamma logarithm, jets, normalization, and coefficient data

Only real u>0 are needed for gamma providers. Put z_gamma=(1+iu)/4,
v=z_gamma-1 and choose rational B>=|v|. For integer s>=max(2B,2) set
q=B/(s+1)<=1/2 and

    F_s(v)=v log s - sum_(j=1)^s Log(1+v/j).

All logarithm factors have positive real part. The analytic log gamma
on Re z_gamma>0 is selected by the real-positive branch. From Euler's
product [DLMF5.8.1--2][gamma],

    |F_s-log Gamma(1+v)| <= B/s+B²/[2s(1-q)],
    |F_s'-(log Gamma)'(1+v)| <= 1/s+B/[s(1-q)],
    |F_s^(m)/m!-(log Gamma)^(m)(1+v)/m!|
        <= 1/[m(m-1)(1-q)^m s^(m-1)]  (m>=2).          (P6)

Proof: subtract the Weierstrass logarithmic product; the coefficient of
v differs by H_s-log s-gamma, lying in [0,1/s] by integral comparison.
For the remaining log tail use
|Log(1+v/j)-v/j|<=|v/j|²/[2(1-q)]. Differentiate the absolutely locally
uniformly convergent tail to get the second and third inequalities,
and use sum_(j>s) j^-m<=s^(1-m)/(m-1). No Euler-constant oracle is used.

The finite normalized derivative formulas are

    F_s'=log s-sum_(j=1)^s (j+v)^-1,
    F_s^(m)/m!=(-1)^m/m sum_(j=1)^s (j+v)^-m  (m>=2).

Every j+v has real part at least 1/4. One sufficient common cutoff is

    s >= max(2B,2, 2(1+B+B²)/delta).                    (P7)

It makes all P6 errors <=delta, for every requested derivative order:
for m>=2 the tail is <=2/s when s>=2. Write eta for the desired
gamma output tolerance and use delta=eta/4, leaving room for finite-data
errors.
In F_s, it suffices to deliver each complex logarithm to error
eta/[8(s+1)(B+1)], and log s to eta/[8(B+1)]; the resulting finite sum
error is <=eta/4. The derivative sums use errors eta/[8(s+1)] per
normalized summand, and eta/8 in their log s. Exact rational summation
adds no arithmetic error. Computing reciprocal powers to these tolerances
uses Section 3 and separated rational denominators. This supplies value
and jets through J=p+1 with explicit errors and finite termination.

At real u>0 the exact gamma factor has the particularly simple logarithm

    ell_+(u)=log((1+u²)/64) -(1+iu)log pi/4
                       +log Gamma((1+iu)/4)+i pi;
    ell_-(u)=conjugate(ell_+(u)).

Indeed w(w-1)=-(1+u²)/4. If D_m=(log Gamma)^(m)(z_gamma)/m!, then

    ell_+^(m)(u)/m! = (-1)^(m-1)/m [(u-i)^-m+(u+i)^-m]
                 +(i/4)^m D_m - 1_(m=1) (i/4) log pi.  (P8)

Consequently c_r is the m=r+1 output and
lambda_(+,n)=ell_+'(X)-i log n/2; the other arm is conjugate.
These are normalized derivatives; large factorials are not formed.
Product-sum propagation, with certified rational magnitude bounds,
delivers every requested c and lambda accuracy. In particular log pi's
phase error is multiplied by u/4 and is requested correspondingly finer.

Write theta=Im ell_+(X). Construct

    beta_(+,n)=n^-1/2 exp(i[theta-X log n/2]),
    M(w_+(u))/g=exp(ell_+(u)-Re ell_+(X)),
    g=exp(Re ell_+(X)).

Use log differences **before** exponentiation. Beta's real normalization
cancels algebraically. E10 requires log n accuracy of order
 epsilon_beta/(1+X); no phase guard is dropped. The inverse square root
has a positive input separation. A certified magnitude bound A_bar for
a normalized exponential and input error eta<=min(1/2,epsilon_A/[4(1+A_bar)])
pays its exponent error, since exp(eta)-1<=2eta for eta<=1/2. Its own
Taylor error is paid separately. All transfer arms use these same
primitives and exact full indices.

For scale delivery, put t=Re ell_+(X). Choose the free encoding integer
k from a coarse t/log2 approximation and certify |t-k log2|<=2.
Require log-scale error and relative exponential delivery error each
<=epsilon_g/8. Then |g_hat/g-1|<=epsilon_g for epsilon_g<=1/2, by the
same exponential inequality and product rule. Store g_hat=m_hat 2^k;
|k|=O(X+log X) and its binary length is O(log X). No fixed exponent
range or division of underflowed factors is allowed. The required
accuracy of log2 includes the factor |k|. Multiplication of the final
normalized result by this symbolic power of two preserves its finite
mantissa representation.

Compute the common shape polynomials using their triangular recurrence
with the delivered rational c_r, in exact rational arithmetic. Relative
to that supplied c, preprocessing and storage error epsilon_t=0.
The c input errors are charged in E9 once. Every polynomial level and
all N modes remain even when an enclosure contains zero.

## 5. Certified finite Gauss nodes and weights

For integer s>=1 form the rational Rodrigues polynomial
P_s(t)=(d/dt)^s(t²-1)^s/(2^s s!). Integration by parts proves
orthogonality against polynomials of degree below s. If it had fewer
than s sign-changing roots in (-1,1), multiplication by the product of
those factors would contradict orthogonality. Hence its s roots are
simple and strictly interior.

On successively finer dyadic meshes of [-1,1], evaluate P_s exactly.
Record exact zero mesh points as singletons and sign-changing open cells
with nonzero endpoint values. Stop at s disjoint records on a fresh
mesh. Simplicity and separation prove finite termination. Refine cells
by exact bisection, preserving a singleton when encountered.

Define the rational polynomial

    J_s(a)=integral_(-1)^1 [P_s(t)-P_s(a)]/(t-a) dt,
    omega_i=J_s(xi_i)/P_s'(xi_i).                        (P9)

Synthetic division computes J_s exactly, including at a root. Division
by P_s proves that these reference weights integrate every polynomial
through degree 2s-1. The nodal Lagrange polynomial l_i gives
omega_i=integral l_i=integral l_i²>0 and sum omega_i=2.
These are the Gauss facts used in E20/E27, also checked at
[DLMF3.5(v)][gauss]; no numerical root-finding theorem is assumed.

Here are explicit, deliberately weak error/work constants. For
A_s=2^s s! P_s in Z[t], a_s=(2s)!/s! is its leading coefficient. Put

    sigma_s=[a_s^(2s-1) 2^(s(s-1))]^-1,
    c_s=leading coefficient of P_s,
    d_s=c_s sigma_s^(s-1),
    S_2=sum_j j(j-1)|[t^j]P_s|,
    J_* =sum_j |[a^j]J_s|,  J_1=sum_j j|[a^j]J_s|.       (P10)

For s>=2 the nonzero integer resultant equals, up to sign,
a_s^(2s-1) times the product of squared root gaps. Every gap is <=2;
therefore every gap is >=sigma_s (the displayed bound is smaller than
the direct square-root bound). For s=1 there is no pair. Nonzero
integer A_s(+-1) similarly gives endpoint distances
>=1/(a_s 2^(s-1)). Thus mesh depth O(s² log(s+2)) suffices.
At a root |P_s'|>=d_s. On an isolating interval of width
<=d_s/[2 max(1,S_2)], the mean value theorem gives |P_s'|>=d_s/2.
Hence J_s/P_s' has Lipschitz constant

    L_w=2 J_1/d_s +4 J_* S_2/d_s².                     (P11)

Rational root centers with error
min(eta_x,eta_w/[s max(1,L_w)]) and exact rational weights obtained
from P9 deliver max node error<=eta_x and total weight error<=eta_w.
Keep rational nodes in their interior isolating intervals, hence in
(-1,1). Positive approximate weights can optionally be certified by
further refinement; their sign is not needed for E24, which uses absolute
weight errors. The displayed work bound is for node/weight delivery
without that optional sign test.
All reciprocal separations are now explicit. An error delta requires
refinement depth log2(1/delta)+O(s³ log(s+2)), in addition to the
initial mesh search. This is a conservative internal bound, not E1.

Map to a rational interval [A,B] by u_i=c+h xi_i, mu_i=h omega_i,
c=(A+B)/2, h=(B-A)/2. With exact rational endpoints, h<=V and

    epsilon_u<=V eta_x,  epsilon_w<=V eta_w,total.        (P12)

For contour edges replace h by its exact complex affine scale and use
absolute values; their lengths sum to 12. Keep rational root centers
inside (-1,1), so contour nodes stay on their exact edges and outer
nodes stay in retained branches. If endpoints instead have error
eta_e, the bounds become epsilon_u<=2eta_e+V eta_x and
 epsilon_w<=V eta_w,total+eta_e(2b+eta_w,total) for b<=2 branches.
We use the interior exact-rational endpoints, so eta_e=0 here.

## 6. Pole-safe contour jets and all RS coefficients

Reuse Note06's normalized entire F_0 and its weighted e_j^(k)
recurrence, retaining every k<=K. Half-integer cancellation, rather than
a division of two small values, supplies analyticity. Compute e_j^(k)
exactly in rational arithmetic, including even-level endpoints:
epsilon_e=0. Contour Gauss rules use Section 5 on the four exact edges
of Gamma, Re zeta=+-2, Im zeta=+-1. E27 supplies analytic truncation.
The rho_c=9/8 edge ellipse calculations give distances at least
19/72>1/4 from Note06's chi rectangle and |2cos(pi zeta)|>=1.

For additional data errors put M=3K,

    B=B_c 4^(M+1), L_zeta=4(M+2)B, L_chi=4(M+1)B.

On the full rectangle |Re zeta|<=9/4, |Im zeta|<=5/4,
|F_0|<=B_c by maximum modulus and the boundary denominator bound.
Radius-1/4 Cauchy on Gamma gives |F_0'|<=4B_c. Thus the integrands
F_0(zeta)/(zeta-chi)^(m+1), m<=M, have magnitude <=B and the displayed
Lipschitz constants. Keep approximate chi within 1/8 of its exact
real value; connecting denominators remain >=1/4.

Let contour total weight error, node error, chi error, per-node integrand
primitive error, and error in kappa=1/(2pi i) be eta_w^c, eta_zeta,
eta_chi, eta_H, eta_kappa. The additional error in each h_m is at most

    [eta_w^c B +(12+eta_w^c)
      (L_zeta eta_zeta+L_chi eta_chi+eta_H)]/(2pi)
      +eta_kappa(12+eta_w^c)(B+eta_H).                   (P13)

Exact rational sums introduce no other error. If each eta<=delta<=1/8,
P13 is bounded by delta C, with
C=[B+13(L_zeta+L_chi+1)]/6+13(B+1), using pi>3.
Choose E27<=tau_h/4 and delta<=min(1/8,tau_h/[4(1+C)]);
remaining rational-center output quantization, if any, gets tau_h/4.
This delivers all h_m to tolerance tau_h with slack.

At rational contour nodes let F_0=N_0/d_0, d_0=2cos(pi zeta).
The scalar providers deliver numerator and denominator errors eta_N,
eta_d<=1/2. Since |d_0|>=1,

    |F_hat-F_0|<=2eta_N+2B_c eta_d.                      (P14)

Set this error <=eta_H 4^(-M-1); exact rational separated powers then
supply the pointwise integrand accuracy. Errors in chi and contour
nodes have already been charged in P13, not repeated in eta_H.

For a useful explicit C_k propagation, define rational bounds

    A_kj=|e_j^(k)| 2^-j 3^(j-2k),
    S_C=max_(k<=K) sum_j A_kj,
    T_C=max_(k<=K) sum_j (2k-j) A_kj/3
                                    *(B_F 2^(3k-2j)+1).

Use rational upper enclosures of B_F. Since j<=3k/2, j-2k<=0, and
pi,pi_hat>=3, the mean value theorem applied to
alpha_kj=e_j^(k) i^-j 2^-j pi^(j-2k) gives

    |C_hat_k-C_k| <= tau_h S_C+|pi_hat-pi| T_C.          (P15)

Here tau_h<=1 and the factors h_m have magnitude <=B_F 2^m.
Choose tau_h<=epsilon_C/[4(1+S_C)], and
|pi_hat-pi|<=epsilon_C/[4(1+T_C)]. This supplies every C_k to
error <=epsilon_C/2; optional final quantization has spare margin.
All finite constants have log-magnitude O(K log(K+2)).
No preliminary PartII precision inequality is used.

## 7. An explicit composed acceptance test

Take certified rational upper bounds for every positive finite
majorant in the following formulas; using upper bounds preserves all
inequalities. Choose these bounds <=2(1+the displayed majorant) by
interval refinement, and choose positive tolerances within a factor two
of the displayed caps when quoting growth bounds. Arbitrary smaller
tolerances also terminate, with their actual log(1/tolerance) cost.
In particular overline V>=V, B_loc, K_loc, A_0, D_p,
D_p^(1), C_p, S_p and D_k refer to Note06. The reference A_0 bounds
the original full model, including strips before omission.

1. **Scale.** Set epsilon_g<=min(1/2,e/[8(1+A_0)]).
   Section 4 supplies |g_hat/g-1|<=epsilon_g, so
   epsilon_g A_0<=e/8<epsilon_X/2.
2. **Arithmetic data.** Put
   C_ar=C_pop X^(1/4)[D_p+2(D_p^(1)+C_p+S_p)] and choose
   delta_ar<=min(1/4,e/[80(1+C_ar)]).
   Deliver beta error<=delta_ar n^-1/2, lambda/c error<=delta_ar.
   Shape preprocessing at those c's is exact rational, epsilon_t=0;
   dyadic stored outputs may alternatively use epsilon_t<=delta_ar.
   E9 is then <=e/80<epsilon_X/20. Sections 3--4 supply these errors
   by finite series, including the multiplied log/phase guards.
3. **Geometry.** Put
   Delta=min(1/8,e/[2048(1+B_loc)(1+overline V)]).
   Use eta<=Delta in Section 2 and base-node/total-weight tolerances
   Delta/(1+overline V) in P12. Thus epsilon_b,epsilon_u,epsilon_w<=Delta.
   E24 is at most B_loc Delta(8+4V)<e/100<epsilon_X/20.
4. **Exact outer quadrature.** Choose integer n>=1 by the rational test
   16 overline V overline B_E 4^-n<=e/80.
   This terminates with n=O(1+log(1/e)+log^+V+log^+B_E).
   For fixed calibration data and the stated allocations n=O(L²);
   E20/E21 are supplied. There are
   at most two retained intervals. If there are none, their quadrature
   is empty and their omission is already charged by Step 3.
5. **RS data.** Set epsilon_Q=e/[80(1+(2 overline V+Delta)K_loc)].
   Find finite uniform real-node bounds A_bar and R_bar,k from E23
   or direct separated expressions, and put
   M_Q=1+2 sum_(k=0)^K [R_bar,k D_k
                         +(A_bar+1)(D_k+R_bar,k+1)].
   Deliver A,R_k,C_k and exact-transfer approximations to common
   error delta_RS<=min(1/4,epsilon_Q/[4(1+M_Q)]).
   E22<=delta_RS M_Q<=epsilon_Q/4, hence E25<=e/80.
   Obtain C_k from P13--15 with epsilon_C=delta_RS.
   Choose contour order q by E27 at m=3K <=tau_h/4, using rational
   upper bounds and rho_c=9/8. In general q=O(1+log(1/tau_h)+K); with the stated
   fixed-calibration allocations q=O(L²+L log L).
   All other scalar and chi data are supplied by Sections 3--4.
6. **Remaining evaluator arithmetic and channels.** Evaluate the
   finite moments, E31 channel formulas, complex kernel channel
   polynomials, products and full sequential sums using exact rational
   operations on the delivered rational primitive outputs. Supply all
   subsequent exponential/kernel primitive data by Section 3 and charge
   their propagated errors to E_round through the same finite product
   rules as E29. This channel is distinct from frozen coefficient input
   and Q-node data. Give each such call a tolerance refined until its
   explicit circuit error sum is <e/160. Exact rational operations have
   zero rounding error. Optional rational-output quantization contributes
   at most e/160 per combined norm, so E_round<e/80.

For Step 6, this is an effective finite test, not an oracle for the
unknown field error. Unroll the finite graph. For a complex addition or
product propagate component errors by E29 with operation roundoff zero;
for each primitive use its proved tail and input-error bound. At every
noninteger division use its certified separation. All magnitude bounds
are obtained by the positive versions of the same finite recurrences,
E15 and E31. If a common primitive tolerance 2^-j fails, increment j;
the explicit upper bound tends to zero because the graph is finite and
has no unseparated denominator. Coefficients, nodes, scales and earlier
allocated data remain fixed. In this reference circuit reset the error
radii of already delivered coefficients, slopes, Q values, nodes and
weights to zero: their differences from the canonical inputs were paid
in E_ar/E_RS/E_geo. Only new primitive/circuit errors enter Step 6.
A positive rational acceptance threshold
and strict slack prove finite termination. This refinement is analytical
algorithm specification, not an executed evaluation.

One can replace exact rational operations in Step 6 by finite precision:
apply E29 at u=2^-j and refine until E_round<e/80 and
u S_lin<=1/4, including the actual full N-mode sum. That alternative
also terminates, but claims no unproved library primitive property.
Gamma/contour **internal** errors are charged to their delivered data
categories, once, rather than inserted again in E_round.

All five evaluation categories are <=e/80<epsilon_X/20. Together with
scale error <=e/8, E5's implication and Note05's half-target truncation
prove total outer error <=exp(-L²/4). The allowances are uniform over
the full declared chart and time interval, although finite query inputs
here are rational. A finite uncertainty in a query coordinate is outside
this exact-input theorem and needs an additional channel allocation.

The full buffered field, spatial-through-three and first-time outputs
are computed separately with their paid channel errors. The frozen
symbolic model has zero heat residual. Rounded/approximated channel
values have only the sum-of-channel-errors bound for T-minus-zz.
A residual_z output still requires the additional mixed T,z channel;
it is not obtained by differentiating a numerical error radius.

## 8. Work, precision, failed shortcut, and disposition

The proof supplies effective, nonsharp error-to-work bounds:

- For delivered gamma tolerance delta and J=p+1, P7 requires
  s=O((1+B²)/delta) terms, O(sJ) rational operations and s complex-log
  calls. Each log call has its explicit geometric-series tail. At the
  present requested accuracies, fixed calibration data, factor-controlled
  allocations and B=O(X), one sufficient bound is
  s=exp(3L²/8+O(L log L)) **per gamma call**. All outer nodes, center
  calls and their input bit lengths are additional work.
- Gauss construction uses an initial mesh with at most
  2^O(s² log(s+2)) exact polynomial evaluations and then
  P+O(s³ log(s+2)) bisection depth for P-bit data. Root-search work,
  coefficient lengths and rational arithmetic sizes are not unit cost.
  Under these same fixed-calibration allocations both Gauss orders are
  O(L²), with at most two outer rules and four
  contour edges. This deliberately slow algorithm establishes finite
  delivery. More efficient isolation is a later cost question.
- All exact-rational bit work is effective: the displayed rational
  recurrences determine every finite numerator/denominator. Integer
  arithmetic, exact division, polynomial evaluations and output have
  their actual operand-length costs. No polynomial bit-complexity or
  useful total runtime theorem is inferred from these operation counts.
- Center verification has its sigma dependence. Boundary guards avoid
  a further edge separation requirement. Threshold theta_j requires pi
  accuracy of order epsilon_b/(1+j²); scale encoding and large phases
  likewise retain their O(L+log L) multiplied-input guards.
- The full 2N arithmetic population and O(Np) moment/channel work stay.
  Provider work is added to it. RS-only O(L^5) scalar work is not a total
  complexity bound.

A specific failed shortcut is preserved. Running the raw Euler provider
with only the **delivered** unit roundoff u comparable to delta gives
u s of order B² and need not satisfy E29's accumulation guard. Termwise
error <=delta/[4(s+1)] or exact rational summation repairs this.
A conventional rounded realization can need roughly
P+log2 s+O(J+log(1+B)) internal bits, about 2P+O(L log L) in this route,
with its finite majorants decisive. Other primitive and root-provider
internal overheads also apply. This is not a necessary precision bound
or an impossibility result for faster gamma algorithms. Note06 E1 stays
a **delivered data and outer-circuit specification**, not a global
working-precision guarantee for these deliberately slow providers.

**Disposition — Analysis, Sol:** AN03 r1 **CLOSED; bounded analytical
provider construction Complete for P1's certified exact-input class**.
All its named provider contracts are supplied constructively from the
inherited comparison hypotheses. There is no unpaid provider inequality
within that class. Broad R05 stays **Partial**: an efficient total-cost/
onset analysis, concrete implementation and software certification remain.
R04/R06 NOT_STARTED; HDA-A02 Partial, HDA-17 Partial, HDA-18 Gated and
HDA-20 unfulfilled remain unchanged. No new time endpoints, physical
transfer or specialist validation.

This is an approximation/evaluation milestone under [avoid01][a1], not
an RH criterion. Consult the [result index][results], [heat cluster][heat],
[control screen][controls] and [avoid index][avoid], especially
[separate bounds][a12] and [scoped exclusions][a7]. Euler-factor and
finite-prime controls fail unchanged canonical coefficients; weighted-
square/cutoff controls fail the complete canonical xi/RS completion;
reflected, smooth and positive-primitive controls lack the same full
gamma/arithmetic identity. Their heat identities may survive. No
collision, simplicity or RH conclusion follows from provider accuracy.

**Next deliverable — Analysis, Sol:** a bounded provider-cost improvement
and total-work audit, [AN04 r1][next], prepared but not executed. Replace
the long gamma product and crude Gauss search with rigorously bounded
alternatives before assessing useful cost and effective onsets. No hard
Astra bottleneck has been identified.

[n6]: 06_COEFFICIENT_ROUNDING_AND_RS_QUADRATURE_20261026.md
[review]: ../reviews/07_FINITE_PROVIDER_ALGORITHM_ASSESSMENT_20261026.md
[inputs]: 09_PROVIDER_ALGORITHM_INPUTS_20261026.json
[work]: 09_PROVIDER_ALGORITHM_WORK_RECORD_20261026.json
[next]: ../research-progress/handoffs/HDA-R05-AN04.md
[gamma]: https://dlmf.nist.gov/5.8
[gauss]: https://dlmf.nist.gov/3.5.v
[results]: ../../../../../result-summaries/README.md
[heat]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a1]: ../../../../../avoid/01_restating_the_target.md
[a7]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md

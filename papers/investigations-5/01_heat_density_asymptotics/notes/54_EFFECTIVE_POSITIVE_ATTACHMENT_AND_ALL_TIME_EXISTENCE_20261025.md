# Effective positive attachment and the remaining central interval

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. **gpt-6.1-sol (Codex), actual effort ultra**,
verified from the current rollout turn_context. Chat **0019**, thread
`01a17463-238b-7352-982f-f0d3c155e1c8`.

**Status: effective field/geometry/mean table and finite all-real-time
analytical prescription proved in-note; same-model internal review only.**
This returns [HDA-18-AN08 r1](../research-progress/handoffs/HDA-18-AN08.md).
For each prescribed positive scalar accuracy, the construction below has
one finite positive source, all real heights and all real times on |y|<=1,
the exact physical regulator, fixed K=k_1 k_1, actual covariance, and both
infinite-time endpoint comparisons. It does not supply affordable source
cost or an executed evaluator/filter certificate. HDA-17 remains Partial,
HDA-18 Gated and HDA-20 unfulfilled. No manuscript milestone is declared.

Read the [result index](../../../../result-summaries/README.md),
[heat-flow cluster13](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
[collision screen12](../../../../result-summaries/12_collision_controls_and_screening.md),
and [avoid index](../../../../avoid/README.md), especially
[target classification](../../../../avoid/01_restating_the_target.md),
[shared premises](../../../../avoid/05_same_model_reviews_and_shared_premises.md),
[scope](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[numerical scope](../../../../avoid/10_numerics_ahead_of_the_question.md),
[signed cancellation](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
and [status](../../../../avoid/19_status_files_that_lag_the_findings.md).
This is a quantitative approximation theorem, neither an RH criterion nor
a collision exclusion. [Manifest54](54_LATE_TIME_EFFECTIVITY_INPUTS_20261025.json)
pins the request and predecessor sources before execution; Note53 and
Review33 determine the task order. [Review34](../reviews/34_EFFECTIVE_POSITIVE_ATTACHMENT_ASSESSMENT_20261025.md)
records the assessment and its shared-premise limitations.

Use H, P, M, alpha, p, B and S_t exactly as in Note30 FS1--FS4, and the
physical q of Note20. All time derivatives are at fixed physical x,y.
Observation |y|<=1 has averaging support through2, source/analytic collars
through4, field jets through5 and base field proof through6. The extra
field strip costs no extra source requirement. No physical normalization,
branch, coefficient, regulator or averaging kernel is changed.

The gain over Note50 is finite constants and an explicit order of choices:
first the uniform late table; then width1 and finite T_+; then the new
compact table with b=T_++1, its gap and union source. An unknown eventual
constant or compact infimum is never used to select an onset.

## A. Effective full-buffer field and geometry

Retain exactly Notes 30/31's implicit gamma saddle and determinant. Put
T_F=exp(4096), L=log(2+t+|x|), N=1+|x|+t L, e=t^(3/2)/N^2,
d=t/N^3, A_sum=|S_t((1+iz)/2)|+|S_t((1-iz)/2)|.
For t>=T_F, the following constants suffice:

* on |Im z|<=6, |H-P|<=10000 e A_sum;
* on |Im z|<=5, |partial_z^j(H-P)|<=C_j e L^j A_sum,
  C_j=2^16 j! 8^j, 0<=j<=3 (a common 2^28 also suffices);
* on |Im z|<=6, |(partial_t+partial_zz)P|<=8192 d A_sum.

These are finite, analytical constants and a deliberately enormous onset,
not practical numerical parameters. A slight enlargement of the base strip
only changes the bounded sigma interval and retains ample margins.

### Gamma input and branch

Note 45 EF3 gives, for Re p>=2 and m=|p|>=4096,

alpha(p)=Log(p/(2pi))/2+r(p), |r|<=2/m,
|alpha^(j)|<=j!/m^j, 1<=j<=4,
|r'|<=24/m^2.

The last inequality is the same analytic-circle estimate used in EF3.
For every Re p>=2, including bounded m, its underlying digamma remainder
also gives the weaker |r(p)|<=4/|p| directly. Indeed
r=1/(2p)+1/(p-1)+Rpsi(p/2)/2,
|p-1|>=|p|/2 and the right-half-plane secant factor is bounded.

For w=sigma+i tau0, -3<=sigma<=4, tau0>=0, use FS9:

sigma+tL/8<=Re p<=sigma+tL,
tau0<=Im p<=tau0+t.

On that rectangle N/40<=m<=2N and
L-4<=log m<=L+log(2L). Thus its fixed-point map has real
increment between tL/5 and tL/3, and imaginary increment in [0,t/2].
The imaginary lower sign is fully finite: for Re p=A>48,
Re alpha'(A+i tau)>=(A/2-24)/(A^2+tau^2)>0;
integrate vertically from the real axis, where alpha is real.
Also Im alpha<=arg(p)/2+2/m<1. The map's Lipschitz constant is
<=20/L<1/2. Consequently the unique original FS9 branch satisfies

a=Re(p-w) in [tL/5,tL/3], |h|=|Im(p-w)|<=t/2,
N/10<=m<=2N, |B-1|<=20/L<1/8.

The improved m lower bound follows from Re p>=tL/6 and
|Im p|>=|x|/2: N<=1+8m<=9m. Negative tau0 uses conjugation.
B never vanishes; the implicit-function theorem supplies holomorphic
neighborhoods, including at tau0=0, and uniqueness glues branches.

### Complete contour ledger

Use exactly FS11/EF7: two reflected arms, each beginning at
v0=2-sigma in [-2,5], and one length-three middle interval. Move each
arm to v=r+ih, preserving its oriented vertical connector. Its real
argument is >=2, so the full Dirichlet series is valid and no pole is
crossed. At a finite right endpoint close the rectangle before taking
the endpoint to infinity. Gamma growth is at most exp(O(r log(r+2)))
for the fixed parameters, so the quadratic Gaussian removes that face.
The following quantitative estimates retain the infinite ends.

For v=v_*+u and u>=-a/2, every intervening p+theta u has modulus
>=m/3 and real part >2. Taylor integral remainders give

|Gamma_p(u)|<=3u^2/(2m),
|E_p(u)|<=3|u|^3/m^2.

Both exact and quadratic exponents have modulus <=exp(-u^2/(2t)).
The segment formula for their exponential difference, integrated using
integral_R |u|^3 exp(-u^2/(2t))du=4t^2, costs at most
24t^(3/2)/m^2<=2400e, relative to its own |S_t(w)|.
The missing Gaussian left end, Gaussian right end, and actual unit-mode
infinite right end each cost at most exp(-tL^2/200).

For the remaining left horizontal segment, put A_r=Re p. The weaker
all-size |r|<=4/m gives the explicit replacement of EF11:

integral_(A_r-d)^A_r Re alpha(v+i tau)dv
 >=d Re alpha(p)-D(A_r),
D(A_r)=A_r/2+4log(A_r/2)+4<=3A_r.

Use this D in EF12 and EF14. Note 45 EF13 supplies
|Im alpha(2+i tau)|<2 at every height, so the connector costs exp(2|h|)
when moved back to its original endpoint. Note 45 EF15 is the finite
middle estimate, valid at every real tau:

sup_(-1<=b<=2)|xi(b+i tau)/8|
 <=225(1+|tau|)|M(2+i tau)|.

Use EF16 with exp(16/t) replaced by exp(25/t), because |v0|<=5.
The exponent shared by these rows is bounded as follows:

-a^2/(4t)+D(A_r)<=-tL^2/100+tL+12<=-tL^2/200.

For connector and middle, A_r-2>=a/2, so the same bound applies
before adding 2|h|<=t and 25/t<=1. The left and connector prefactors
are <=exp(L); the middle prefactor is <=exp(2L). Hence each complete
row is <=exp(-tL^2/400).

All non-unit arithmetic modes, including their infinite right end,
are bounded by EF17 with its full Dirichlet-series inequality. With
sigma>=-3 this is at most

128 exp(-tL/10+t/2)<=exp(-tL/20).

Finally N<=exp(L)L, so e>=exp(-3L). At t>=exp(4096), every displayed
exponential allowance is <=e. Summing two complete arms and the one
middle proves the stated 10000e field constant. Nothing was replaced
by a finite set of modes or a finite endpoint.

### Paid jets, phase, carrier and residual

For D=(log S_t)'_w, FS21 and the preceding bounds give
|D|<=2L, |D'_w|<=3/m, |Im D|<=2. On a disk of radius 1/(8L),
neighboring e is <=2e and each carrier modulus is <=2 times its center
value. Cauchy's formula on the complete holomorphic error gives
C_j=2^16 j!8^j; the base strip 6 pays every such circle centered in
strip 5. This does not differentiate an asymptotic allowance.
The exact PE8 formula gives the stated 8192d residual constant.

Choose compatible logarithms P=2 Acal cos Theta. On |Im z|<=6,

|partial_z log Acal|<=2,
L/8<=Theta_x(t,x)<=L on the real line,
|Theta_zz|<=10/N.

For the first inequality, compare the two D values by conjugation and
the bounded real sigma shift (<=6), using |Im D|<=2 and |D'|<=3/m.
The real phase speed follows from Re D=Re alpha+O(t/m^2).
The second phase derivative follows by differentiating the exact formula.

### A2. Explicit mixed holomorphic collars

Suppose G is entire and real-type, with
|partial_z^j(G-H)|<=e L^j A_sum/16, j<=3, on the union core in
|Im z|<=4. Every analytic disk used for the mixed collars lies inside
that source buffer. No source accuracy on strips 5 or 6 is assumed. Put Q_s=(1-s)G+sP, 0<=s<=1. The constants below
are independent of the selected core, source, overlap and s.

Let c_k be every real P root (Theta(c_k)=(k+1/2)pi), L_k=L(t,c_k).
Use concentric disks centered at c_k of outer radius 1/(16L_k),
inner collar radius 1/(64L_k). They are disjoint. Real phase monotonicity
and the derivative bounds prove that all P zeros in the strip are these
real simple zeros: Re Theta_z remains positive throughout strip 6,
so Im Theta has the sign of Im z. In the outer disk,

L_k|z-c_k|/16<=|Theta(z)-Theta(c_k)|<=2L_k|z-c_k|.

The carrier changes by less than a factor two there. Consequently
|P(z)|>=A_k L_k |z-c_k|/32, where A_k=Acal(t,c_k)>0.
The full carrier-sum floor outside the inner disks can conservatively be
chosen 2^-20 A_sum: for |Im z|>=1/(128L), use the lower imaginary-phase
bound; below it, compare real phase distance to the nearest real root.
The O(1/N) transverse phase error is much smaller than the fixed margin.
All collars touching a support are counted with their complete outer disks.

On the source-controlled core rectangle, Rouche gives exactly one real
simple root a_s in each complete inner collar meeting a used support, and
no additional zero on that support outside those collars. The larger
analytic disks are all inside the union source rectangle in strip4. Quantitatively the following safe universal constants work:

|a_s-c_k|<=2^40 e/L_k,
2^-10 A_k L_k<=|(Q_s)'(a_s)|<=2^10 A_k L_k.

At t>=exp(4096), every smallness requirement such as
2^100 e L<=1 and 2^40 e<=1/1024 is satisfied uniformly in x,
because e L<=t^-1/2/L. Root displacement follows by applying Rouche
on the much smaller circle of radius 2^40 e/L_k using the displayed
linear P floor. Reality follows from real-type symmetry and uniqueness.

On each outer disk Q_s=(z-a_s)b_s(z) with

2^-10 A_k L_k<=|b_s(z)|<=2^10 A_k L_k.

Prove these bounds first on the outer boundary using the P floor and
root displacement, then apply maximum principles to b_s and 1/b_s.
For H and every Q_s, their analytic units satisfy

|log(b_s/b_H)|<=2^62 e,
|partial_z log(b_s/b_H)|<=2^70 e L_k

on the half outer disk. The boundary ratio is
(Q_s/H)(z-a_H)/(z-a_s); field-relative and root-displacement bounds
put it within 2^60e of one. The maximum principle and Cauchy on the
paid disks prove the two stated bounds.

Do not infer a bounded pole residue from the coarse individual unit
Cauchy bound O(L). Instead the exact P residue is

v_P=P_zz(c_k)/P_z(c_k)
 =2 Acal_z/Acal+Theta_zz/Theta_z, |v_P|<=8.

The first three field jets, root displacement, and unit-log derivative
differences give

|v_s|<=16, |v_s-v_H|<=2^100e L_k,
v_s=(Q_s)_zz(a_s)/(Q_s)_z(a_s).

For example the individual second derivative of a log unit is bounded
by a universal constant times L_k^2 on the smaller paid disk; multiplying
by the root displacement costs O(e L_k). This controls evaluation at
unequal roots. All constants just used are below the stated 2^100 cap.
Finally subtract these simple poles in h_F=F_zz/F:

h_F=v_F/(z-a_F)+g_F,
|g_F|<=2^100 L_k^2,
|g_s-g_H|<=2^100 e L_k^2

on the half outer disk. Establish the difference on its boundary using
the field floor, derivative jets and translated pole difference; then
use analyticity and the maximum principle. These are the finite inputs
for Note 31's signed-pole and actual covariance arguments.

The number of collars meeting a fixed horizontal half-width a is at
most 8(a+1)L on its enlarged support. Thus the raw primitive gradient
from F'/F costs at most a fixed constant times L, using the exterior
floor, the integrable simple poles, and the individual analytic-unit
Cauchy bound <=2^25L. The remaining physical w grad r term still needs
the regulator-regime payment; this field/collar derivation does not
claim that an unweighted |grad r| is uniformly bounded at all heights.

### A3. Finite core carrier lower bound

For |Re z|<=R_c, |Im z|<=5, the carrier derivative bound gives

|Acal(t,z)|>=A_0(t) exp(-2(R_c+5)),
A_0(t)=S_t(1/2)>0.

This is an actual full complex carrier floor, not merely a real-axis
field value. A_0 is specified by the same unique real implicit saddle
and gamma formula. On a selected compact late overlap t in [T,T+1],
one may avoid an unknown infimum entirely with the coarser explicit bound

A_0(t)>=exp(-4(T+1)log^2(T+3)).

To obtain it, retain a<=t log(2+t)/3 and p=1/2+a; the gamma integral
on [1,2] gives Gamma(p/2)>=exp(-2), p(p-1)/16>=1 and B<1.
Bound pi^(-p/2)>=exp(-p) using pi<4 and bound a^2/t by
(T+1)log^2(T+3)/9. The displayed exponential is a weaker sufficient
bound with ample positive margins. It is allowed to make source cost
very poor; relative collar estimates, not this core floor, must pay TJ25.

### Audit of the large collar constant

The preceding 2^100 cap can be paid without an unspecified constant.
The unit bounds on outer radius R=1/(16L) imply, by Cauchy on radius
R/4, |(log b)'|<=2^26L on the 3R/4 disk and
|(log b)''|<=2^32L^2 on the R/2 disk. The log ratio bound gives
its derivative <=2^70eL there. Pairwise root displacement is <=2^41e/L,
so |v_s-v_H|<=2^76eL. On the boundary of R/2, |F|>=2^-16 A_k,
|F''|<=2^20 A_k L^2, |delta F''|<=2^31e A_k L^2 and
|delta F|<=2^31e A_k. It follows that
|delta(F''/F)|<=2^84eL^2. The translated pole difference costs
<=2^83eL^2, leaving |delta g|<2^86eL^2<2^100eL^2.
The individual bound is smaller.

For the exterior floor, write Theta=u+iv. If |v|>=2^-12,
|cos Theta|/cosh v>=tanh|v|>=2^-13. Otherwise
|v|>=L|y|/16 implies |y|<1/(256L). Outside every inner disk,
the real displacement from the closest phase root is therefore at
least half its inner radius. Its real phase distance is >=1/2048.
The transverse real-phase correction is <=5y^2/N<1/4096, so
|cos Theta|/cosh v>=2^-14. The declared 2^-20 floor is weaker.

## B. Effective temporal primitives, physical weights and means

Write R=2+t+X, l=log R, N=1+X+t l, e=t^(3/2)/N^2,
d=t/N^3. Fix the full averaging rectangle Omega, of area at most A,
including its prescribed enlargement. All constants below are fixed before
the overlap, core, and source are selected. A finite field table must give:

* a frequency a_w l <= omega <= b_w l, with omega >= omega_0>0;
* at most n_w omega enlarged collars, physical radius r/omega, containing
  every collar meeting Omega, with larger paid analytic collars;
* each relevant holomorphic mixed field F=(1-v)G+vP and H has exactly one
  root in each collar and |F| >= c_s A_X omega |z-a_F| there;
* off collars |F|,|H| >= c_g A_sum and >=c_g A_X, decreasing the
  finite c_g by the paid carrier-comparability factor if necessary;
* on collars A_sum <= c_a A_X; all needed source/mixed errors are bounded
  by D_j e l^j A_sum (j<=3), and individual jets by M_j l^j A_sum;
* scaled root displacement <=D_a e and analytic units b_F,b_H have
  |b_i|>=u_-, |b_i|<=u_+, |b_F-b_H|<=D_u e and paid logarithmic
  derivative <=U_1 omega on the smaller physical collars;
* h_F=F_zz/F=nu_F/(z-a_F)+g_F, with |nu_F|<=V,
  |nu_F-nu_H|<=D_nu e omega, |g_F|<=G omega^2,
  |g_F-g_H|<=D_g e omega^2;
* |partial_x log A_X|<=C_A, |partial_z log(mathcal A)|<=C_A on the
  fixed full buffer, and the residual field bound
  |E_P|<=D_E d A_sum.

If collar bounds instead use A_X in the errors, absorb c_a into D_j.
For the formulas below use D_0,D_j already so absorbed on collars; keeping
the larger value globally is harmless. Let e be the supremum over the
fixed local enlargement, with the finite comparison factor incorporated
in the D_j. Require D_a e<=r/4 and D_u e<=u_-/2, in addition to the
field table's original margin. These become finite onset conditions.

### B2. TJ25 directly from a simple-root floor

Let Delta=P-G on a holomorphic core and assume |Delta|<=D_T e A_sum,
with c_a absorbed in D_T on collars. For F=(1-v)G+vP put
T_m=integral_Omega w_F^m |Delta conjugate(F)|/(|F|^2+q), m=0,1,2.
Off collars its integrand is <=D_T e/c_g. On a collar it is
<=D_T e/(c_s omega |z-a_F|), because w^m(1-w)<=1.
Positive radial integration, enlarging every intersecting collar, gives

    T_m <= C_T e,
    C_T = D_T [A/c_g + 2 pi n_w r/(c_s omega_0)].       (J1)

This proves the unweighted temporal primitive with no regulator floor,
no residue comparison, no root velocity, and no inverse source amplitude.
Multiply (J1) by |v'|<=c_b/Delta_t for its exact TJ25 consumer.

For a nonnegative weight a with supremum a_* use a_* times this bound.
For m>=1 a useful improved estimate is available. Set
Lambda=sup_Omega sqrt(q)/A_X. Then, on a collar,
w<=a_e^2/(|z-a_F|^2+a_e^2), a_e=Lambda/(c_s omega), so

    T_m[a] <= a_* D_T e
      [A Lambda^2/c_g^3 + pi^2 n_w Lambda/(c_s^2 omega)], m=1,2. (J2)

Indeed integral_0^infinity a_e^2/(s^2+a_e^2) ds=pi a_e/2.
The complement uses w<=Lambda^2/c_g^2. The bound is valid also when
Lambda is large; the unweighted (J1) is then usually better.

Only z_0[1] is used in FT10--FT16. Spatially weighted heat terms retain
z_1,z_2: TJ5 contains Z_1 grad r, Z_1 Delta r, and (Z_1-2Z_2)|grad r|^2.
There is no consumer requiring z_0[x^2/kappa^2]. Replacing those Z_1/Z_2
by Z_0 would discard the essential exterior regulator suppression.

### B3. A finite one-sided physical mass anchor

For t>=exp(4096) the large source saddle has L>=1 and
kappa=8tL-2t+36>=6t+36, hence t/kappa<=1/6. (The elementary test
q_t'(1)>0 and u_*=(log(t/(8pi)))/4>1 places the large root above 1.)
On |s|<=kappa^(-1/2), L+s>=0 and

    q_t(L+s)-q_t(L)
      >= -1/2 -(2/3)(1+2t/kappa) exp(4/sqrt(kappa))/sqrt(kappa)
      >= -2.

This follows from q_t''(L)=-kappa and
|q_t'''(L+s)|<=4(kappa+2t) exp(4|s|). Each n>=2 summand of b is
positive and its n=1 summand is >=1-3/(2pi)>1/2. Therefore

    H(t,0) >= M_0(t) exp(-2)/sqrt(2pi) >= M_0(t)/32.    (J3)

Once the finite field theorem at zero has relative allowance <=1/2,
H(t,0)<=3 A_0(t), because P(t,0)=2 A_0(t). Thus

    M_0(t)/A_0(t) <=96.                                (J4)

No complete-source tail or eventual Note12 constant is needed for this
one-sided estimate. It suffices for all the exterior upper bounds below.

Let b be the fixed horizontal buffer radius and choose

    B_0 >= max(1,4b,8(C_A+2)).

On X/kappa>B_0 one has X>=4b, so (X-b)^2>=X^2/2 and

    Lambda <=96 kappa^(-1)
      exp[-(X-b)^2/(2kappa)+C_A X] <=96 exp(-X).        (J5)

Enlarging B_0 further is harmless. The chosen B_0 actually gives an
exponent at least -(C_A+4)X after the Gaussian estimate, so the final
-X allowance has strict room. Only the upper Lambda in (J5) is used.

### B4. Effective regulator weights and exterior absorption

At t>=128 the exact coefficients are PE18:

    r_x=-2x/kappa, r_xx=-2/kappa,
    r_t=2L^2-3kappa'/kappa+x^2 kappa'/kappa^2,
    r_xt=2x kappa'/kappa^2, r_xxt=2kappa'/kappa^2,
    kappa'=8L+16tL/kappa-2,  |kappa'|<=11L<=11 l.

The crude finite inequalities L<=log t<=l and kappa>=6t+36 give
L/kappa<=log(t)/(6t)<=1 at the stated onset, where L is the physical
source saddle; the height-dependent l/kappa is not bounded globally. On X/kappa<=B_0, after including b in
X+b, every required spatial coefficient is bounded by an explicit
polynomial in B_0,b, while |r_t| and b_r are <=C_r l^2. One safe common
constant is

    C_r = 128(1+B_0+b)^4.                              (J6)

It dominates R1,R2,T1,T2,Th,c_r and their finite products used in the
ledger, except factors r_t or b_r which carry l^2. The largest products
actually needed are R1^2 and R1*T1; arbitrary extra products are not
silently included.

On X/kappa>B_0, t<=X/(6B_0), l<=2(1+X), kappa>=1.
Thus each required nonnegative weight a has an explicit envelope
a_*<=A_a(1+X)^d_a obtained by substituting these inequalities into its
displayed PE18/FT11 definition. This includes weights a|r_t| in FT10.
No unknown supremum is needed. For example R1<=2(X+b), R2<=2,
|r_t|<=96(1+X+b)^3, T1<=44(1+X+b)^2,
T2<=44(1+X+b), Th<=176(1+X+b)^3, and
c_r<=6(1+X+b)^2; b_r<=100(1+X+b)^3 is safe.

For integer n>=0 define the explicit positive polynomial

    E_n(c)=sum_(j=0)^n binom(n,j) j! c^(-j).

Then (1+X)^n exp(-cX)<=E_n(c), by the power-series bound on exp(cX).
This is an analytical inequality, not machine evaluation. Also on this
exterior N<=4(1+X)^2, hence e>=[16(1+X)^4]^(-1).
Consequently every polynomial times (J5) is bounded by an explicit
constant times e, using E_(d_a+4)(1) and the factor 16. This pays the
individual weighted w and V_1,V_2 terms as well as (J2); weights attached
to z_1,z_2 retain their extra e directly. No lower mass anchor or
bound on |log(actual Lambda)| is required.

For explicit individual estimates, radial integration and
log(1+s^2)<=2s give

    integral w_F <= A Lambda^2/c_g^2
                       +2pi n_w r Lambda/(c_s omega),  (J7)
    integral w_F |h_F|
      <= V pi^2 n_w Lambda/c_s
          +G omega^2 [A Lambda^2/c_g^2
                       +2pi n_w r Lambda/(c_s omega)]
          + A M_2 l^2 Lambda^2/c_g^3.                (J8)

The final complement term of (J8) may be replaced by any already paid
individual exterior h bound. With |h|<=M_2 l^2/c_g there, the displayed
term is valid. Sum H and F to bound their differences. In (J8), collar
regular-part area may be used separately for a slightly smaller number.
The coarser displayed bound remains finite and exponentially decreasing.

### B5. A completely finite PE14 comparison coefficient

The arbitrary-q analytic-unit proof gives the following safe constants:

    C_S=4A D_0/c_g
      +(n_w/omega_0)[4pi r^2 D_u/u_-+8pi r D_a],
    C_W=2A D_0/c_g
      +(n_w/omega_0)[pi r^2 D_u/u_-+2pi r D_a].         (J9)

They bound s[1]<=C_S e, w[1]<=C_W e. To see this, replace units and
then translate roots; integral 1/|u-a| over the scaled disk is <=4pi r.
Q(u)=q/A_X^2 is held fixed pointwise and is never differentiated.

For the pole-kernel comparison let

    h_0=4(D_a+1), H_r=1+|log(2r)|,
    C_P=8pi(h_0+D_a)+14pi D_a(H_r+1)+48pi r D_u/u_-.

Excluding endpoint disks of radius h_0 e, interpolate the root and the
unit logarithm. For W_m=w^m(1-w), m<=2, one has |W_m|<=1 and
|dW_m/dlog|f||<=6. The derivative of the pole kernel is bounded by
7 D_a e/|u-a_s|^2+12 D_u e/(u_- |u-a_s|).
The excluded disks cost <=8pi(h_0+D_a)e; radial integration pays the
remaining logarithm. Thus the scaled pole difference is at most
C_P e(1+|log e|). Require h_0 e<=r/4 as an additional finite margin.
Since e<1 and N<=R log R, 1+|log e|<=5l. Therefore

    v_m[1] <= C_V e l^2, m=0,1,2,
    C_V=5n_w V C_P +2pi r n_w D_nu b_w
       +D_g A b_w^2+3G C_W b_w^2
       +A[D_2/c_g+7M_2 D_0/c_g^2].                  (J10)

Residue differences, regular parts and the zero-free complement are the
four respective terms after the pole-translation term. This is one
sufficient finite replacement for PE14's unspecified C. It is purposely
coarse, and preserves the signed-stress method for actual covariance.

### B6. Uniform actual mean caps

On collars F_z/F=(z-a_F)^(-1)+b_F'/b_F. Off collars its modulus is
<=M_1 l/c_g. Hence

    integral |F_z/F|
       <=2pi r n_w +A U_1 omega +A M_1 l/c_g.         (J11)

The exact gradient formula gives
|grad S_F|<=2|F_z/F|+w_F |grad r| on holomorphic core regions.
In X/kappa<=B_0 the last integral is <=2A(B_0+b).
In the complementary regime multiply (J7) by 2(X+b)/kappa, use
omega>=omega_0, (J5), and E_1(1). Thus one explicit coefficient is

    C_grad=4pi r n_w +2A U_1 b_w +2A M_1/c_g
       +2A(B_0+b)
       +2(1+b)[96^2 A E_1(2)/c_g^2
                   +192pi n_w r E_1(1)/(c_s omega_0)]. (J12)

Then integral |grad S_F|<=C_grad l, since l>=1. For each multiindex
1<=|gamma|<=3 choose i with gamma_i>0 and set

    M_gamma=C_grad ||partial^(gamma-e_i)K||_infinity l. (J13)

These are caps for the actual means used in FT13, with the same caps
also covering H. The resulting N_alpha is exactly FT13's finite
Leibniz sum, with e_gamma=k_gamma C_S e and (J13); it is bounded by an
explicit coefficient times e l, hence by that coefficient times e l^2.

On spatial bands F is nonholomorphic. Its actual gradient has the extra
F_bar term; the paid gap floor and |F_bar|/|F|<=C_cut e l supply its
finite addition. That addition belongs to the existing band reserve or
is included in C_grad if its finite profile constants are fixed. One
must not silently use the holomorphic formula on such bands.

### B7. Honest finite definition of C_+ and threshold

Form the finite table of FT3 raw inputs as follows. On the holomorphic
core use (J9), (J10), (J1) for z_0, (J2) for z_1,z_2, the fixed
bounded-regulator weights from (J6), and the individual exterior
weights (J7)--(J8) plus E_n for their absorption. Apply the same z
formulas to D_E d+(c_b/Delta_t)D_T e. Substitute these inputs, the exact
PE18 coefficients, fixed kernel norms, and actual mean caps (J13) into
the displayed finite maps FT10--FT13 and the holomorphic TJ5 map
(equivalently PE34) for the signed heat correction. Compute each
equation allowance as its displayed component sum, not its maximum.

Every resulting scalar has the form coefficient*(1+c_b/Delta_t)e l^2
or a smaller e/e l/d expression. Let C_+ be one plus the maximum of
those finitely many explicit positive coefficients, including spatial
orders U,W<=4, tuple orders<=2, internal current order3, source/equation
component sums and boundary traces. This is a finite max of named
positive expressions, not an unknown supremum, asymptotic constant or
fit. It depends only on the finite field/collar/regulator/kernel table.
It is independent of T_+, Delta_t, core radius and source. Source and
spatial-seam allowances remain the separately allocated reserves.

Since e l^2<=t^(-1/2), Delta_t=1 permits the TJ24 prescription

    T_+ >= max{128,T_F,[8C_+(1+c_b)/theta]^2,
                      [4C_jet/mu_coll]^2},

enlarged by the explicit additional margins D_a e<=r/4,
D_u e<=u_-/2 and h_0 e<=r/4 if they were not included in mu_coll.
Taking sqrt(T_+) at least 4 max(D_a,h_0)/r and 2D_u/u_- suffices.

For the spatial-band part Delta=(1-lambda)(P-G), exactly
Delta_bar=-lambda_bar(P-G) and
Delta_bar,z=-lambda_bar,z(P-G)-lambda_bar(P_z-G_z).
These give d_B<=C_cut e l and d_Bz<=C_cut e l^2 on the paid gap,
and TJ4/TJ5 retain the new compatibility variation. Its leading finite
integrand is |v'| C_cut e l^2, with band area <=C_area/l; hence its
temporal addition is at most |v'| C_cut C_area e l (with the explicit
coefficient obtained by TJ4 substitution). Higher existing spatial
seam terms keep their separate compact-J reserve. No eta_t appears in
an instantaneous spatial weak pairing.

Sections A and B now supply the mixed units, residue comparison,
amplitude derivative, residual field coefficient and weighted consumers.
The dependent central interval [63,T_++1] is paid separately in C below.



### B8. Instantiate the finite constants before selecting T_+

Here is an explicit common specialization of B's formulas, to remove any
freedom to insert a core-dependent coefficient. Use omega=l, omega_0=1,
a_w=b_w=1, A=128, n_w=128, r=3/128, C_A=2 and horizontal buffer8.
The phase frequency itself lies between l/8 and l; using l as the collar
scale simply absorbs that factor8 into the stated constants. Enlarging each
working collar to radius3/(128l) about its displaced root still lies inside
the half outer disk of radius1/(32l). In formulas J1--J13 use
c_s=c_g=u_-=2^(-64), u_+=2^64, and enlarge each upper error, jet,
unit-derivative, residue and regular-part coefficient to G_0=2^128.
Here u_-,u_+,D_u describe the dimensionless unit in
F/A_X=(omega(z-a_F))b_F, not the physical unit F/(z-a_F).
These also cover all fixed-support local e,l and carrier comparisons:
|log A_X/A_c|<=16 on the support enlargement, and e changes by at most2.
In particular c_g is a floor in both the A_sum and local A_X units;
the carrier-comparability loss is included before using J2,J7--J13.
These weakened constants satisfy the hypotheses already proved in A.
They are independent of every later overlap, core, and source choice.

Set B_0=128. The one-sided mass proof and physical coefficient table give
the following single convenient raw constant:

    C_raw=2^4096.                                      (EA1)

It bounds s,w by C_raw e; v_m by C_raw e l^2; and the actual gradient
integral by C_raw l. For weights a in {1,R1,R2,R1^2,T1,T2,Th,c_r},
w[a]<=C_raw e. For a in {1,R1,R2,R1^2},
w[a|r_t|],v_m[a]<=C_raw e l^2, and w[b_r]<=C_raw e l^2.
The residual/temporal inputs satisfy

    z_0[1]<=C_raw[d+Lambda_T e],
    z_m[a]<=C_raw[d+Lambda_T e],
       m=1,2, a in {1,R1,R2,R1^2}.                    (EA2)

Here the component field is lambda-weighted E_P and Lambda_T=||v'||;
its coefficient8192 and the field mismatch constants are included in
C_raw. These rows are for holomorphic pieces, restricted only by enlarging
nonnegative integrals to full collars; the nonholomorphic bands have the
separate C-section reserve. In particular EA2 does not claim a weighted
z_0[R1^2] estimate. TJ5 consumes z_1,z_2 in those places.

For checking the size of EA1, each geometric input and its reciprocal is
<=2^128. The explicit J1,J9--J12 expressions have products of at most
eight such inputs. In the exterior, preserve l^2 in the V row; the other
weights have degree at most4 in 1+X. The lower bound
e>=1/[16(1+X)^4] and the E_n(1), n<=16, inequalities in B absorb all
individual exponentially small weights. Each E_n(1)<=2^128. The
remaining area/count,96,pi and fixed regime constants and their finite
sums fit below2^256. Thus even the common2^4096 is a strict enlargement.
This is a finite arithmetic inequality argument, not a scalar execution.
The mean cap is justified before its use in covariance; on bands include
the additional F_bar/F term via the gap floor.
For a late support meeting both core and band, use this uniform actual
mean cap for the entire F_+, before FT13. On that band use A's late e-jet
comparison and EA7, so |F_z/F|<=C_raw l and
|F_bar/F|<=C_raw e l. The physical regulator payment then gives the
same uniform gradient cap there. A core primitive error is never
multiplied by the compact C_Hb; that b-dependent cap is confined to the
separate compact/spatial reserve. Split only the positive primitive
allowances in FT13; its actual mean-product subtraction is global.

For the fixed kernel use FI15's explicit a_i and put

    K_*=1+5 sum_(i+j<=4) a_i a_j,
    C_+=2^65536(1+B_0+K_*)^64.                        (EA3)

K_* bounds every required sup/L1 kernel norm and their sums. Substitute
EA1--EA2 and the actual mean caps C_raw k_(gamma-e_i)l in
FT10--FT13, TJ5/PE34 and the displayed equation-component sums. These
maps have only sums/products and factors<=4; the sole mean-product
term is quadratic. Even allowing eight raw factors and64 kernel or
regime factors, the coefficients fit strictly under EA3. No denominator
depending on T_+, core radius or source enters this operation. It follows
for each scalar row of the holomorphic positive tuple, including its
signed heat/source consumer, that the bound is

    C_+(1+c_b/Delta_t)e l^2,
    c_b=2exp(4/3).                                     (EA4)

The unweighted temporal primitive retains the sharper C_raw e rate.
For signed heat, TJ5 is paired globally with the full weak test for the
new core-containing pieces v(1-lambda)E_P and v'(1-lambda)(P-G).
The identity is linear in its direction: set Delta equal to the chosen
piece and its scalar prefactor to1 at the fixed time. In the holomorphic
core the compatibility variation vanishes. On bands its E_bar and
E_bar,z are paid by the same gap jets and TJ4, in the C reserve. Thus
PE34 is never applied to a sharply truncated core integral. An equivalent
smooth test partition must retain all its spatial commutators in that
reserve; the existing outer partition already does so.
For the finer static U,W rows the bound is C_raw e. Actual Q and Delta Q
use the signed stress and the actual mean-product sum FT13; no products
of separately bounded positive pole squares are introduced.

Fix 0<theta<=1 and select, as an actual finite formula,

    Delta_t=1, mu_coll=2^(-256), C_jet=2^29,
    T_+=max{128,exp(4096),
             [8C_+(1+c_b)/theta]^2,
             [4C_jet/mu_coll]^2}, b=T_++1.            (EA5)

The stated onset exp4096 also pays the unit/root smallness margins,
including h_0 e<=r/4, because e l<=t^(-1/2)/l and every multiplier is
<=2^256. Thus TJ24 now selects a finite positive overlap; its C_+ has
been fixed beforehand. EA4 costs <=theta/8 there and on the pure-P tail.
The spatial-band additions are allocated separately below, rather than
folding a compact b-dependent cap into C_+.

For the finite whole complex core use the A-section lower bound, with
the already fixed b, in the form

    A_min_late=exp[-4b log^2(b+2)-2(R_c+5)].          (EA6)

This is positive on the entire late overlap and source buffer4, including
all required collar disks. It is allowed to be very poor. It enters only
the finite source demand; it is never inverted to prove EA1--EA4.


## C. A new compact table through the selected upper time

Fix **b>=128** before choosing a joining height or a source, and let
J_b=[63,b]. Write lambda=log x. A sufficient elementary outer threshold is

    Lambda_b=2^20(1+b)^4,      x>=exp(Lambda_b).

The following are literal b-dependent replacements in Note45, not an
invocation of its stated [95,97] theorem outside its domain. The EF4
rectangle is used with 63<=t<=b. The inequalities exp(lambda) dominating
any of the displayed b-polynomials give

    x/2<=|p|<=x, Re p>2, b/x<1/2,
    t lambda/5<=a<=t lambda/3, |h|<t/2,
    |B-1|<=b/x, Re B>1/2.

EF3 remains unchanged. The map is a strict contraction, specifies the
same original implicit branch, and is holomorphic on the full |Im z|<=5
buffer. Its strict interior margins and uniqueness identify overlapping
charts. Negative imaginary arms follow by conjugation.

Retain EF7's exact two arm contours, their oriented connectors, the
length-three middle, all arithmetic modes, and the actual infinite ends.
EF8--EF17 hold with t<=b. For the finite reductions use

    -a^2/(4t)+D(A_r)
       <=-63 lambda^2/100+(2b/3)lambda+6 <=-lambda^2/2.

The connector and middle exponents, apart from 2|h|+16/t<=b+1,
obey the same estimate because A_r-2>=a/2. Their prefactors can be
enlarged respectively to 2b and 1350x; the left prefactor to 2b lambda.
The complete arithmetic allowance is at most

    48 exp(b/2-63 lambda/10).

At lambda>=Lambda_b each end, left, connector, middle, and arithmetic
allowance is <=x^-3, by the same monotone polynomial/exponential
comparisons as EF19. The central unit-mode error is <=12b^(3/2)/x^2.
Consequently, with A_sum the unchanged two-arm carrier sum,

    |H-P| <= C0(b) A_sum/x^2, C0(b)=12b^(3/2)+7.

The paid complete Cauchy circle rho=1/[4log(2+x)] on the larger buffer
gives for j=1,2,3

    |partial_z^j(H-P)| <= Cj(b) log^j(2+x) A_sum/x^2,
    Cj(b)=8 C0(b) j!4^j,

on |Im z|<=9/2, x>=2exp(Lambda_b). The exact determinant derivative
obeys |(log S)_w|<=log x there. This derives jets on disks, never by
differentiating an asymptotic allowance.

FI2, with 97 replaced by b and a_j=j!2^j/x^j, b_det=1/2, proves the
same geometric EB1 caps after this onset: D0<=L_x, D1<=5/x,
D2<=33/x^2, Theta_x>=L_x/8, |Theta_x|<=L_x/2,
|Theta_zz|<=5/(4x), |(log mathcal A)_z|<=2. The field's residual has
the explicit intermediate bounds

    R0<=24b/x^3+80b^2/x^4,
    R1<=384b/x^4+3072b^2/x^5+5120b^3/x^6.

Hence |E_P|<=d A_sum, |(E_P)_z|<=d L_x A_sum with
d=2^32(1+b)^4/x^3. The same real-part cancellation in MW2 proves
|Theta_t|<=L_x/2 and hence |X'|<=8; this uses t/x^2<=b/x^2 at the
new onset, rather than an absolute O(L_x^2) time bound.

The complex first-omitted log-gamma formula also gives, at this onset,

    exp(-x)<=|S_t((1+iz)/2)|       (|Im z|<=5),
    |S_t((1+ix)/2)|<=exp(-x/4).

One direct bookkeeping bound for its main exponential is
|log|S|+pi x/8|<=2^16(1+b)^2(1+lambda)^2. For example the real
part of p is at most 3+b lambda/2, the imaginary shift is <=b/2,
the angular correction is O(Re p+b), the real logarithmic term is
O((Re p+1)(lambda+1)), and the real saddle exponent is bounded by
b lambda^2/9+b/4. The polynomial and determinant factors and the
sector remainder fit the displayed bound. It is <x/8 at Lambda_b.
Thus these carrier inequalities are proved from the full complex
formula, not from a real-line derivative integrated across the buffer.

The EB1 collar geometry, slopes, unit/pole table and radial-integration
constants are consequently unchanged if their dimensionless comparison
input is enlarged to

    e_b(u)=E_b0/(u-8)^2, E_b0=2^60(1+b)^4,
    d_b(u)=D_b0/(u-8)^3, D_b0=2^32(1+b)^4,
    l=log(2+u).

Require e_b l small by the final onset. Then EB6/SW2 remain, literally,
s,w<=2^26 e_b, v_m<=2^44 e_b(1+|log e_b|+l^2),
z_m<=2^22 d_b. Their weighted EB9 counterparts retain their old
numerical constants; all intersecting collars and the complement are
included. There is no selected-zero premise.

### C2. Explicit physical-regulator table on [63,b]

For the real source saddle use its larger maximum L_s. Its equation
4pi exp(4L_s)=2tL_s+9 gives, throughout J_b,

    1/4<L_s<b+1,
    36<kappa<K_b=8b(b+1)+36,
    0<kappa'<Kp_b=16(1+b)^2.

The lower bracket follows from q_t'(1/4)>0 at t=63; the upper bracket
follows by the elementary exponential inequality at b+1. Positivity
and the upper derivative use kappa'=8L_s+16tL_s/kappa-2.
The source maximum obeys q_t(L_s)>-3 and q_t(L_s)
<=b(b+1)^2+9(b+1). Put

    W_b=16(1+b)^3.

SC1 therefore gives the finite two-sided mass bound

    exp(-3) K_b^(-1/2) <= M0 <= exp(W_b).

Write exactly r=a-beta x^2 as SW4--SW5, extending chi=1 for t>=128.
The full switch has |chi'|<=1: by symmetry restrict its v variable to
v<=1/2, use chi<=exp(2-1/v), and bound
exp(2-1/v)[v^-2+(1-v)^-2]<=8 before division by64.
Define

    Lplus_b=W_b+3+2log(2+K_b),
    Lbase_b=|log eta|+4+(1/4)log(1+b^2),
    A_b=4[1+Lplus_b+Lbase_b+(1+b)^2+Kp_b],
    Bprime_b=1/36+Kp_b/36^2,
    Q_b=16eta^2+exp(2W_b).

Then |a|,|a'|<=A_b, exp(a)<=Q_b, beta<=1/36,
|beta'|<=Bprime_b. The term chi'(ell_+-ell_b) remains in a'.
At t<=64, beta=beta'=0 exactly. On [64,97] retain SW8. On
[97,b], chi>=1/2, so beta>=1/(2K_b), and therefore the **uniform
compact flatness bound** is

    |beta'|<=F_b beta[1+log^2(1/beta)],
    F_b=max(4,2K_b Bprime_b),

with beta'=0 at beta=0. This explicitly covers the other half of the
switch and all t>=128; no use is made of SW8 outside its proved range.

For |x|<=R set

    E_b=min(4eta exp(-4)/(1+b^2)^(1/4),
            exp(-3)K_b^(-3/2)),
    e_core(R)=E_b exp(-R^2/72).

This follows arm by arm from the actual epsilon_b and epsilon_+ and
their geometric interpolation. It is a lower bound for sqrt(q), never
for q. A safe full coefficient table is

    A_t=A_b+Bprime_b R^2,
    R1=R/18, R2=1/18,
    T1=2Bprime_b R, T2=2Bprime_b,
    Th=4Bprime_b R^2,
    c_r=1/18+R^2/324, b_r=A_t+c_r/2.

On exterior full supports split allowances as SW10, A: beta u<=16,
B: beta u>16. In A, the exact flatness bound pays

    R1<=64, R2<=32/u,
    |r_t|<=A_b+128F_b u l^2,
    T1<=128F_b l^2, T2<=64F_b l^2/u,
    Th<=2^14 F_b l^2,
    c_r<=2^13, b_r<=A_b+128F_b u l^2+2^12.

In B the carrier-relative physical scale remains

    Lambda<=sqrt(Q_b) exp[u+32-beta(u-8)^2/2]
            <=sqrt(Q_b)exp(-2u)

at the final onset. Use the monotone EB9 functions of this explicit
upper scale, keeping |log Lambda_bar|<=2u once u>=log Q_b. All
coefficient weights retain their actual factors before the exponential
majorization. These are proof cases for nonnegative integrals only;
their indicators are never differentiated.

### C3. Complete-source moments and a new common mean cap

An especially simple upper-time moment split is V_b=b+16. For j=0..3 put

    B_j(b)=40[V_b^(j+1) exp(b V_b^2+13V_b)/(j+1)
                         +Gamma((j+1)/2)/2],
    B1_star=(B_0(b)+B_2(b))/2, P2=B_2(b)+1.

Indeed Phi<=40exp(9u-pi exp(4u)). For u>=V_b,
bu^2+13u+u^2<=u^3 and pi exp(4u)>=u^3, so its weighted tail is
bounded by exp(-u^2). The first finite interval is bounded directly.
Thus these are complete-source moment caps on every t<=b and |y|<=4.

For a concrete fixed central radius independent of the eventual seam,
set

    S_b=1+Q_b+A_b+F_b+Bprime_b+E_b0+D_b0+eta^(-2),
    Rstar_b=ceil exp(2Lambda_b+2S_b),
    estar_b=E_b exp(-(Rstar_b+8)^2/72),
    C_Hb=max(2^100,
       2^30[B1_star/estar_b+(Rstar_b+8)/18+1]).

The floor and moments prove the gradient cap on |x|<=Rstar_b.
Outside, the paid analytic units and integrable simple poles give
the EB16 logarithmic gradient integral. In regime A the physical
|r_x| integral w is <=256; in B its individual EB9 Gaussian-weight
bound pays |r_x|. The radius above is beyond all branch/collar,
Q_b-scale and local polynomial-decay gates. Moving the remaining
derivatives onto fixed K therefore gives

    |partial^gamma U_H|<=C_Hb[1+log(2+|x|)], 1<=|gamma|<=3.

The joined field's common cap is this plus1, **after** the primitive
auxiliary k_gamma s<=1 rows have been paid. This avoids circular
covariance coefficients. C_Hb is allowed to depend on fixed b; it is
used only in the spatial/compact reserve, never in the late-time C_+.

### C4. One moving gap and finite uniform compact budget

Take one initial gap at t0=64 by the exact phase inverse
n=ceil(Theta(64,U)/pi), Theta(64,X0)=npi, and continue this same
phase level over J_b. The explicit velocity bound above implies

    |X(t)-X0|<=8 max(1,b-64).

Use the safe fixed enlargement

    Dmov_b=8(b+1)+32,
    a_X=X0-Dmov_b, R_c=X0+Dmov_b,
    L=log(2+R_c), sigma=1/(64L).

The inverse cannot leave its compact exterior branch neighborhood;
it continues uniquely to both endpoints. With U beyond the final
onset, local logarithms have the same 999/1000 ratio and every source,
collar and averaging buffer fits the union |Re z|<=R_c, |Im z|<=4.
The exact seam floor is c0=1/2, actual mixed-field floor c*=1/4.
All spatial-cutoff and exterior-test profiles remain exactly FI9/FI10.

Use

    mu_o=E_b0/a_X^2, mu_s=a_X^(-2), mu=mu_o+mu_s,
    d=d1=D_b0/a_X^3, C0=1, C1=C2=C3=2.

These dominate the full field, model and residual inputs above.
Substitute them in EB13 and add the MW moving allowances with V=8.
All exact identities MW7--MW10/SW16 remain. Use SW12's extra
delta0/(2c*) branch for arbitrary q in the gap. Use the new A/B
coefficient table above in the full FT10--FT18 and GS13/GS14 ledger.
In particular k=2v+|r_t|w and |r_t|theta_reg b0^2 retain their weight.

The same finite coefficient count as SW23 yields, with explicitly
enlarged coefficients,

    C_b=2^8192[1+C_Hb+Q_b+A_b+P2+F_b+Bprime_b
                         +E_b0+D_b0+Dmov_b]^64,
    B_b(X0)=C_b[L^8/a_X+(1+R_c)^20 exp(-a_X)].

Each nonsource column, and each auxiliary mean row, is <=B_b.
The operations and number of terms of that ledger have not changed;
each new b-dependent coefficient is an input in this displayed bracket.
As in SW23, at most16 powers of these inputs occur before the chosen
64th power, and numerical/profile/kernel/Leibniz products fit 2^1024.
The A time factors are O_b(u l^2), so the worst compatibility-time
row is O_b(mu u L^3); all other power tails decay at least as fast.
In B the old polynomial degree20 still dominates all products. The
new time-interval length enters only Dmov_b; there is no chart-count
or interval-length sum of errors.

For target 0<theta<=1, one sufficient explicit binary onset is

    m=16384+ceil log2(4Rstar_b+4Dmov_b+1024)
               +ceil[8log2(2+C_b/theta)],
    U=2^m, followed by the exact phase inverse at64.

Certified integer upper bounds with two extra units are permissible.
Then a_X>=2^(m-1), L<=m+3, C_b<=theta 2^(m/8),
(m+3)^8<=2^(m/2), and exp(-a_X)<=X0^-64. These monotone elementary
inequalities pay B_b<theta/4, the branch/geometry gates, mu<=1/4,
and all scale/weight gates. No scalar research execution is involved.

For the source use the Note47 core D_r table with the new physical
coefficients at R_c, P2, and common cap

    M_gamma=C_Hb[1+log(2+R_c)]+1

on core/seam supports; retain local height on pure exterior supports.
Include auxiliary D_gamma=k_gamma. Set

    e_c=E_b exp(-R_c^2/72), A_min=exp(-R_c-16),
    rho=min(theta/4,B_b(X0)),
    epsilon_core=e_c^2 min_(D_r>0) rho/(4D_r),
    epsilon<=min(1,epsilon_core,mu_s A_min).

The carrier minimum follows from the full complex arm bound above.
This gives one fixed source and the same three-column analytical
bound <=3B_b<=3theta/4 on all [63,b], every real height, |y|<=1.
The covariance cap is invoked only after its primitive auxiliary rows.

### C5. Literal constructive source recipe at the new upper time

The old FI18 cutoff U=ceil(4+log(5+Q)) was proved with upper time97;
simply replacing its exponential F is not enough to re-prove its tail.
For any positive epsilon use instead

    Q=log(32/epsilon),
    U_s=ceil[b+4+log(5+Q)],
    F_s=U_s^4 exp(b U_s^2+4U_s),
    n0=max(3,ceil sqrt(log(2^14 F_s/epsilon)/2)), N=n0-1,
    M=ceil[U_s max(1,(2^20 F_s/(48epsilon))^(1/4))],
    h=U_s/M, bits=ceil log2(64F_s/epsilon).

Use exactly FI16's clipped rational cubics and FI18--FI20's bounded
nodal enclosure/isolation procedure. The proof on [0,U_s] is unchanged.
For the complete tail U_s>=b+4 ensures

    lambda_j=4pi exp(4U_s)-2bU_s-13-j/U_s
                    >=pi exp(4U_s),
    bU_s^2+13U_s-pi exp(4U_s)<=-2exp(4U_s).

The same Q inequality pays epsilon/8. Thus the separate interpolation,
omitted values/slopes, nodal arithmetic, construction/clipping and
complete-tail debits remain 29epsilon/64 in total for all four jets
on **every t<=b**, all real x and |y|<=4. This single source may
therefore also satisfy TJ9/TJ14/TJ19's earlier demands by taking the
minimum tolerance, without changing negative or initial-switch fields.

### C6. Positive temporal seam and one union source

Suppose the preceding sections have first paid the uniform late-time core collar
table and selected finite T_+, Delta_t=1, b=T_++1. On the positive
overlap use exactly

    lambda_+=v+(1-v)lambda,
    F_+=G+lambda_+(P-G), v=b_*(t-T_+).

In particular

    (lambda_+)_x=(1-v)lambda_x,
    (lambda_+)_xx=(1-v)lambda_xx,
    (lambda_+)_t=v'(1-lambda)+(1-v)lambda_t,
    B_+=(1-v)B_c,
    (B_+)_t=(1-v)(B_c)_t-v'B_c,
    ((B_+)_z)_t=(1-v)((B_c)_z)_t-v'(B_c)_z.

Keep E_comp=lambda_+ E_P,
E_sp=(1-v)[lambda_x D_z+lambda_xx D/4], and
E_move=(1-v)lambda_tD+v'(1-lambda)D, with their exact z derivatives.
On pure core lambda=0 this is the present note's holomorphic late collar
problem. On the zero-free spatial bands the new temporal mismatch
ratios are explicitly

    d0<=4mu,
    d1<=4mu L(1+kappa1/2),
    dB<=2kappa1 mu L,
    dBz<=(kappa2+2kappa1)mu L^2,
    kappa_j=l_j/L^j.

TJ3 adds |v'| times these quantities. TJ4's compatibility variation
is O(|v'|mu L^2), and its filtered allowance is O(|v'|mu L)
after the band area. These are lower logarithmic order than the
existing band master. TJ5's final nonholomorphic compatibility term
must be retained with the same TJ4 allowance. Therefore replacing
C_b by (1+c_b)C_b in the spatial/compact reserve pays all these band
terms, with c_b=2exp(4/3) and Delta_t=1. The signed spatial test
retains both first commutators and eta_O,xx; its instantaneous pairing
creates no eta_O,t term. Nothing differentiates the regional indicators.

Use one source with tolerance below the minimum of epsilon_core,
mu_s A_min, TJ9's T^(-5/2), TJ14's theta/[4(1+K_mid)],
TJ19's theta/[2^69 K_bridge L^3], and the late relative demand

    epsilon <= e_min A_min_late/16,
    e_min=T_+^(3/2)/
       [1+R_c+b log(2+b+R_c)]^2.

Here A_min_late is the present note's paid positive carrier minimum over
the entire core buffer and overlap. One may take the minimum with
this compact table's exp(-R_c-16) only when its large-height premise
holds; the central late-time carrier minimum must come from the
late-time table itself. The source's absolute accuracy on t<=b gives
all four relative demands since Lcal>=1.

The earlier negative-to-63 constants can retain their upper-time97
moment caps because those fields are used only there; the same source
is accurate there by the stronger all-t<=b constructor. On [63,64],
TJ17 can conservatively use this enlarged L and a_X, and its old
K_bridge remains valid: H and G jets there are bounded by B_j(97)+1,
independently of their larger constructor endpoint.

There is no new unpaid central contour/gap/source/mean/join estimate
in this table. Its use remains conditional on the **present note's** uniform
late-time field/collar/mean gate, and the source/evaluator remains
unexecuted and potentially enormous. All status and useful-cost limits
of AN08 remain; no RH or collision conclusion is implied.


## D. One source, one field, both infinite-time limits

The following order makes the construction noncircular. Fix theta and
eta, select C_+ and T_+ by EA1--EA5, and set b=T_++1. All C-section
constants now have that fixed b. Put delta=theta/64. In C's compact
onset use the enlarged C_b^+=(1+c_b)C_b and target delta; use the same
enlargement for its compact/seam envelope B_b^+. This includes the
positive band's TJ3--TJ5 increments, not the holomorphic core estimate.

Choose the negative parameter by Note50 TJ13 at target delta, namely
T_-=max(1,4K_neg/delta). Retain its finite K_mid(T_-) and K_bridge.
In the compact binary onset take also the maximum with

    16384+ceil[8log2(2+2^64 K_bridge/delta)].

This pays the earlier pre-switch bridge using the new a_X,L; its old
upper-time97 moments remain valid on [63,64]. Select the one phase index
at64 and follow its gap over [63,b]. Do not identify its exact full-saddle
crossover center with the earlier linear-gamma center. Both are retained
at their original scopes; no center displacement is needed by this proof.

With e_min from C6 and A_min_late from EA6 choose one positive epsilon
no larger than the minimum of

    1, epsilon_core, a_X^(-2)exp(-R_c-16),
    T_-^(-5/2), delta/[4(1+K_mid(T_-))],
    delta/[2^69 K_bridge L^3], e_min A_min_late/16.     (EA7)

Every quantity in this finite minimum is already specified and positive.
Use C5's changed upper-time constructor to produce the single clipped
positive cubic source f and exact-heat G. Its source jets through3 are
accurate by29epsilon/64 for every t<=b and all real heights on strip4.
In particular it meets the late relative demand and every earlier source
demand. The fields are defined by the finite rational/algebraic source
recipe, not by inserting unknown H or its roots as data. No nodal data
or evaluator was actually computed in this analytical packet.

Let lambda be C4's moving spatial profile, F_c=G+lambda(P-G),
v_-=b_*((t+2T_-)/T_-), v_0=b_*(t-63),
v_+=b_*(t-T_+). The actual field table is

| Time domain | Actual field | Payment |
| --- | --- | --- |
| t<=-2T_- | N=C/sqrt(-t) exp(z^2/(4t)) | Note26, TJ8--TJ13 at target delta |
| [-2T_-,-T_-] | (1-v_-)N+v_-G | TJ1--TJ13, same source |
| [-T_-,63] | G | TJ14, EA7, finite global time-only floor |
| [63,64] | G+v_0 lambda(P-G) | TJ15--TJ19 with enlarged union gap/source |
| [64,T_+] | F_c | C1--C5, new [63,b] constants, all buffers |
| [T_+,T_++1] | `G+[v_++(1-v_+)lambda](P-G)` | A/B and EA1--EA7 on core; C6 and TJ5 on bands |
| t>=T_++1 | P | finite A/B endpoint table, actual E_P retained |

The union is exactly **R_t x R_x on |y|<=1**. Matching is smooth at all
endpoints because every profile is flat; no chart-count multiplier is
introduced. P is used before T_+ only on its paid exterior branch and is
extended by a flat zero coefficient into the inner region; after T_+ its
all-height late branch has been proved. The b-dependent central table
explicitly pays **97<t<T_++1**, rather than extrapolating Note49.

Each individual scalar analytical comparison in the retained full tuple
is <=theta/2: the negative/mid/bridge rows use delta, compact/seam rows
use3B_b^+<=3delta/4, and the positive core/tail uses theta/8, with their
positive sums on supports crossing a seam. This generous theta/2 leaves
room and is not an executed arithmetic/filtering bound. The equation
residuals have the sums of their displayed component bounds; a common
single-row bound is not asserted for every equation sum. Fixed spatial
and temporal traces inherit only the paid derivative orders.

Use the exact observables of this actual F, including B=F_bar and
E=F_t+F_zz. Keep both total-curvature derivatives, Xi/2, signed spatial
test commutators, temporal compatibility variation TJ5, direct source
balance and actual covariance Q=K*(S_x^2-S_y^2)-(U_x^2-U_y^2).
No observable is blended independently. No small-residual-to-error
propagation, or tuple-agreement-to-field inference, is used.

As t->-infinity, the field is exactly N and Note26's vanishing complete
comparison applies with the unchanged negative physical regulator. As
t->+infinity it is exactly P: static U/W errors are <=C_raw e and all
retained evolution/covariance rows are <=C_+ e l^2<=C_+ t^(-1/2),
uniformly in all real heights on the declared strip. The exact nonzero
P residual has the separately paid d=t/N^3 scale. These are limits of
the physical, unnormalized quantities and their errors, not a claim that
the growing density itself tends to a finite constant.

## E. Evidence, control screen and disposition

The primary classical inputs rechecked for this continuation are the
[DLMF sectorial gamma remainder](https://dlmf.nist.gov/5.11#ii),
[Cauchy formula](https://dlmf.nist.gov/1.9.E31),
[digamma series](https://dlmf.nist.gov/5.7.E8) and
[Euler zeta formula](https://dlmf.nist.gov/25.2.E8). They support the
inherited gamma/contour tools, not an external all-time theta theorem.
All new inequalities and domain payments are analytical. A proof-check
correction replaced a false global l/kappa<=1 shorthand by the correct
physical source-saddle L_s/kappa<=1; no previous note was edited.

Collision controls retain the same screen as Note53/cluster12:
Euler-factor controls alter the canonical completion; weighted-square and
finite-prime controls lack full unchanged coefficients/reflection;
reflected, smooth and positive-primitive controls lack the canonical
gamma/source identity; atomic and heat-polynomial controls lack the smooth
complete theta source. Generic transfer identities still apply to those
controls. A root collar excludes a collision only inside its own proved
late/simple domain and says nothing about earlier multiple core events,
which the compact positive-regulator comparison allows.

**AN08 r1 CLOSED at its finite analytical-existence scope.** No first
unpaid contour, collar, mean, weighted temporal or compact-extension row
remains in the construction above. This is not HDA-18's useful-formula
acceptance: the onsets and sufficient source description can be enormous,
and no useful conditioning, implemented arithmetic, continuous filtering
certificate or source-derived evaluated data has been supplied. HDA-17
Partial, HDA-18 Gated and HDA-20 unfulfilled remain.

No numerical, exact-rational or machine-symbolic research execution,
theta/source/gamma/field sampling, precision/mesh search or interval
campaign was run. Prior algebra checks are reused by reference; source
recipes are definitions, not executions. Hashes, sizes and local-link
checks are housekeeping. Same-model subagent derivations and root review
share premises and do not provide specialist independence. No prior-note
or manuscript edit, snapshot, DRAFT_HISTORY milestone, commit, new
user-owned chat or model change is part of this return.

**Next: Analysis — Sol**, existing HDA-23 / HDA-17-AN04 r1: improve the
sufficient source tolerance/description cost for this same actual tuple,
or return the first exact conditioning estimate. HDA-20's distinct full
chain review should include this new positive attachment and central
extension; current internal checks do not fulfill it.

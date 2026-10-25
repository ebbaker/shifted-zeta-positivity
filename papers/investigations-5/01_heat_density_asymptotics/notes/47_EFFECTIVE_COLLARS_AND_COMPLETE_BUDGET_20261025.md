# Effective collars and one complete finite fixed-gap budget

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. **gpt-6.1-sol (Codex), actual effort ultra**,
read from this turn's session metadata. Chat **0017**, thread
`01a173e5-dc96-7c31-946c-be54c871244c`.

**Status: finite sufficient analytical budget proved in-note; internal
same-model review only.** This is the return to
[HDA-18-AN04 r1](../research-progress/handoffs/HDA-18-AN04.md).
No first unpaid analytical row remains in this fixed-gap regime. A finite,
deliberately unoptimized onset and one finite positive source suffice for
the complete Note 43 tuple, uniformly in real observation height, on the
short slab specified below. The source is specified constructively, not
executed; no numerical observable certificate or affordable implementation
is claimed. The all-height, all-real-time analytic objective, both infinite
time limits, HDA-17 Partial, HDA-18 Gated and HDA-20 unfulfilled remain.

Read the [result index](../../../../result-summaries/README.md),
[heat-flow cluster](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
[collision controls](../../../../result-summaries/12_collision_controls_and_screening.md)
and [avoid index](../../../../avoid/README.md), particularly
[classification](../../../../avoid/01_restating_the_target.md),
[scope](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[cancellation](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
and [shared review](../../../../avoid/05_same_model_reviews_and_shared_premises.md).
This is a quantitative approximation result, not an RH criterion.
[Inputs and provenance](47_EFFECTIVE_BUDGET_INPUTS_20261025.json) and
[Review 29](../reviews/29_EFFECTIVE_COLLARS_AND_COMPLETE_BUDGET_ASSESSMENT_20261025.md)
record the frozen request, source versions and internal checking.

## 1. Contract and finite geometric inputs

Keep Notes 30/42/43's canonical H, full implicit saddle P, physical
q=epsilon_g^2, eta>0, actual covariance, unnormalized potential, and
K=k_1 k_1. Let J=[95,97], t0=96, Y=1, Y_b=4. All analytic circles
stay inside Note 45's |Im z|<=5 field buffer. No manuscript is changed.
Write A_sum=|S_+|+|S_-|, distinct from the single real carrier A_c below.

For x>=2^2049 the EF3 bounds and FI2 give, with L_x=log(2+x),

    D0<=L_x, D1<=5/x, D2<=33/x^2,
    L_x/8<=Re Theta_z, |Theta_z|<=L_x/2 on the real axis,
    |Theta_zz|<=5/(4x), |(log mathcal A)_z|<=2.          (EB1)

On the fixed transverse strip the last two bounds control the departure
from real-axis values; where needed use |Theta_z|<=0.51L_x. Here
P=2 mathcal A cos Theta, with the compatible continuous phase lift from
Notes 30/44. For example a_j<=j!2^j/x^j, b>=1/2 in FI2 proves the
three D bounds. Re alpha>= (log x-3)/2-4/x gives the phase lower bound.
The large real logarithms cancel in (log mathcal A)_z; EF5 bounds the
remaining imaginary parts by one, and D1 pays transverse variation.
EF5 actually gives Theta_x>=L_x/5 on the real axis. Integrating the
Theta_zz bound over |y|<=5 retains Re Theta_z>=L_x/8 throughout the
fixed strip, as used on the complex collar disks.
FI4 gives |Theta_t|<=4L_X^2 on |x-X|<=1, |y|<=4.

For any declared U>=2^2050+8 select exactly

    n=ceil(Theta(96,U)/pi),
    Theta(96,X)=n pi, X>=U.                            (EB2)

Strict monotonicity and divergence of Theta make X unique, with
0<=X-U<=8pi/log(2+U)<1. A different continuous phase lift changes n
by an integer and selects the same X. This rule does not sample theta
or choose a favorable index. Put

    L=L_X, sigma=1/(64L), tau=1/(4096L^2),
    I=[96-tau,96+tau].                                 (EB3)

FI5 on |x-X|<=2sigma, |y|<=4 bounds phase departure by
sigma D0+tau T0+2D1<1/8. Consequently |P|/A_sum>=1/2;
take c0=1/2, c_*=1/4. The nearest real root is at distance at least
5/(2L) from X. Indeed local L_x/L differs from one by less than 1/1000,
Theta_x<=1001L/2000, the time departure is <=1/1024 and pi>3.
The analytic collars below leave a distance at least 1/(4L) from
Sigma+ (whose half-width is 2sigma). Root speeds are <=8, so GS2
holds with V=8 and c_gap=1/4. The deliberately shorter tau is admissible;
it does not assert fixed positive time width as X tends to infinity.

For a real P root c write L_c=log(2+|c|), u=L_c(z-c),
A_c=|S_t((1+ic)/2)|. Use working collars |u|<=1 and larger analytic
disks |u|<=2. Adjacent roots have separation at least 5/L_c with the
local logarithmic adjustment; the analytic disks are disjoint. Every
full support and its fixed enlargement meets at most 4L_v collars,
where v is its large observation height. Include edge collars in full.

On each larger disk the following finite table is valid. A common local
error e may dominate 10^6/c^2; later we use a still larger e.

| Input | Finite allowance |
| --- | --- |
| P/A_c=u B(u) | 1/16<=|B|<=4 |
| H/A_c=(u-e0) C(u) | 1/32<=|C|<=5, |C-B|<=128e |
| paired roots a,c | |L_c(a-c)|<=32e |
| root slopes P,H | >=A_c L_c/16, >=A_c L_c/32 respectively |
| residues v_F=F_zz/F_z at own root | |v_P|<=5, |v_H|<=8, |v_H-v_P|<=2^18 e L_c |
| F_zz/F=v_F/(z-root_F)+g_F | |g_F|<=2^10 L_c^2, |g_H-g_P|<=2^20 e L_c^2 |
| zero-free complement | |P|/A_sum>=1/256, |H|/A_sum>=1/512 |
| h_F on complement | |h_F|<=2^12 L_v^2, |h_H-h_P|<=2^20 e L_v^2 |

**Proof of the table.** EB1 gives |mathcal A(z)/mathcal A(c)| between
1/2 and 2 on the disk. Integration of Theta_z gives
|u|/8<=|Theta(z)-Theta(c)|<=0.51|u|. Taylor's series gives
3/4<=|sin z/z|<=5/4 for |z|<=1.1; hence the B bounds.
EF1 gives |H-P|<=10^6 A_c/c^2 on the disk. Rouché first on |u|=2,
then on |u|=32e, gives exactly one simple H root and the displacement;
real symmetry makes it real. Divide out each own root and use the
maximum principle on |u|=2 to obtain |C-B|<=128e and the C bounds.
The analytic functions are the removable quotients, not reciprocals
through a zero. EF2 gives comparison-derivative bounds relative to A_c
of 32eL_c, 512eL_c^2, 16384eL_c^3. P's corresponding derivatives
are <=16A_c L_c^j. At a P root,
v_P=2(log mathcal A)_z+Theta_zz/Theta_z, so |v_P|<=5.
Compare derivatives at paired roots along their displacement segment
to obtain the residue difference; eL_c is tiny at the stated onset.
Subtract the pole terms on |u|=2 and apply the maximum principle to
g_H-g_P. The complement floor follows from cos Theta/cosh(Im Theta)
outside the phase disks, including vertical points; EB1 supplies the
injective phase coordinate. These floors also exclude additional zeros.
Thus the table covers every collar, not a selected population.

Exact root motion is a'=v_H and c'=v_P-E_P(c)/P_z(c). FI8 and EF3 give

    R0_model<=2400/x^3, R1_model<=40000/x^4,
    |E_P|<=R0_model A_sum,
    |(E_P)_z|<=(L_x R0_model+R1_model)A_sum/2.           (EB4)

This pays the residual correction to model velocity and the speed 8.
For example use d=2^16/x^3 and |(E_P)_z|<=d L_x A_sum.

## 2. Raw exterior integrals, including the restricted pieces

To remove harmless changes of local height, use the following enlarged
constants for a support chart at v>=2^2050+8:

    l=log(2+v), e=2^44/(v-8)^2, d=2^20/(v-8)^3.        (EB5)

They dominate all EB1--EB4 inputs on its full enlarged collars, using
L_c between l/2 and 2l. The following allowances deliberately enlarge
the local constants once more. They apply to the nonnegative raw
integrals FT3 on *any restricted exterior portion* of that support:

    s_O[1]<=2^26 e,
    v_m,O[1]<=2^44 e(1+|log e|+l^2), m=0,1,2,
    z_0,O[1]<=2^22 d.                                 (EB6)

For each intersecting working collar enlarge the integral to its full
disk. The integrand here is nonnegative. Add the zero-free complement,
whose area is <=4. This operation is legitimate for a truncated integral;
a signed whole-support observable estimate would not justify it.

Here are explicit local estimates behind EB6. In scaled coordinates
|e0|<=32e and |log(C/B)|<=4096e. Interpolate
(u-se0)B exp(s log(C/B)), holding Q(u)=q/A_c^2 fixed pointwise.
The potential and weight integrals on the scaled working disk are at
most 2^16 e and 2^14 e. For b_m=w^m(1-w), m<=2, its derivative
with respect to log|F| has modulus <=6. Removing |u|<=2|e0| costs
<=10pi|e0| in the regularized-pole comparison; off it the derivative
cost is bounded by

    28|e0|/|u|^2+12*4096e/|u|.

Radial integration bounds this by 2^19 e(1+|log e|). Restore area
L_c^-2 and the physical pole factor L_c, use the collar count, then
add residue differences, regular parts and the complement from Section 1.
This proves EB6. Only simple poles are integrated absolutely. The signed
stress is reduced to them *before* estimating; separate positive squares
would have a different, regulator-dependent logarithm.

For the physical regulator let Q_+=16eta^2+exp(220). The source saddle
and switch in FI11--FI13 give

    beta=chi/kappa>1/2000, q(t,x)<=Q_+ exp(-x^2/2000).

For the switch, v in [31/64,33/64] has logit at least -128/1023,
so chi>1/3, already sufficient with kappa<618. Complex Stirling with
its first omitted remainder gives, for every arm on |y|<=5,

    log|S_t(w)|>=-x, x>=2^2049.                        (EB7)

One direct payment is
log|S_t(w)|>=-pi x/8-12log^2x-200log x-202>=-x.
Use EF4/EF6 in log M(p); discard the positive
(Re p/2-1/2)log|p/2| term, pay the imaginary argument term, the
pi factor, the saddle exponent and log B separately. EF3's sector
has sec^2(arg(p/2)/2)<2, so the first omitted log-gamma remainder
is <=1/(6|p/2|). The last elementary inequality holds at log x>=1000
by exp(log x)>=log^4x/24. Thus the lower bound holds for all relevant
real points and both arms, not only root centers.

A safe upper scale, including fixed collar and support enlargements, is

    Lambda(v)=sqrt(Q_+) exp(v+32-(v-8)^2/4000)
                     <=sqrt(Q_+) exp(-v^2/8000).        (EB8)

Use EB8 only where Lambda<=1/2. This requires an eta-dependent onset;
eta has not been assumed <=1. Define

    B=Lambda^2[1+(1+|log Lambda|)/l],
    H_L=l^2 B+Lambda, Z_L=B+Lambda/l.

Then, for any nonnegative coefficient weight a with supremum a*,

    w_O[a]<=2^25 a* B,
    v_m,O[a]<=2^37 a* H_L,
    z_m,O[a]<=2^33 d a* Z_L, m=1,2.                    (EB9)

The constants include both fields where differencing is required.
Indeed the unit lower bound gives w<=(32Lambda)^2/
(|u-root|^2+(32Lambda)^2). On a root-centered disk of radius 5/4,
the two needed radial integrals are
pi a^2 log(1+(5/4)^2/a^2) and at most pi^2 a, a=32Lambda.
Sum the full intersecting collars and the complement. For E_P/P its
residue is <=32d/L_c and analytic part <=512d; this proves z0 and
the weighted z rows. Increasing the local scale to EB5 and constants
in EB6/EB9 covers all buffer replacements. The functions Lambda^2,
Lambda^2(1+|log Lambda|), Lambda increase on (0,1/2]. Consequently
one may replace Lambda by its explicit Gaussian upper envelope.
There is no need for a separate upper bound on |log of the actual scale|.

Polynomial regulator weights are retained. On a chart of radius
R=v+8 take the FI13 caps

    A_t=4+(118+|log eta|)/8+R^2/512,
    R1=R/113, R2=1/113, T1=R/256, T2=1/256,
    Th=R^2/14464, c_r=1/113+R^2/113^2,
    b_r=A_t+c_r/2.                                    (EB10)

Every occurrence of |r_t|, R1,R2,T1,T2,Th,c_r,b_r multiplies EB9
where a w-weight is required. No polynomial is absorbed by discarding
an exponential or by multiplying EB6's unweighted s by an unbounded weight.

## 3. Explicit exterior signed heat/source payment

Use exactly FI9--FI10's flat cutoffs lambda and eta_O, with
l_j=||lambda^(j)||, c_j=||eta_O^(j)||. For sigma=1/(64L), the safe
scaled caps are

    l1<=2^12 L, l2<=2^24 L^2, l3<=2^36 L^3,
    c1=l1, c2=l2.                                    (EB11)

They are upper allowances for the stated profiles, not new profiles.
The exact FT14 commutators remain
-2eta_O'K_(alpha+x)+eta_O''K_alpha and
-4 Re integral Z1 r_x eta_O'K_alpha/(4pi).

For |alpha|<=2, the following finite replacement for FT15 follows
directly from signed PE34 and EB6/EB9:

 D_out,alpha <= d/(2pi) {
   2^22[d_alpha+2c1 k_(alpha+x)+c2 k_alpha]
   +2^33 Z_L[2R1(k_(alpha+x)+c1 k_alpha)
                         +(R2+3R1^2)k_alpha] }.        (EB12)

Here d_alpha=k_(alpha+xx)+k_(alpha+yy). On pure exterior supports
eta_O is constant and its actual derivatives vanish. At seam supports
use EB10 with R=X+8. PE34 is obtained by varying the actual holomorphic
density at fixed q: delta S=2Re Z0, delta w=-2Re Z1,
delta chi=-2Re(Z1-2Z2). This checks its signs independently.
Thus EB12 bounds a signed pairing, not integral|D_E|. Its first part is
O(dL^2), and its second displays the polynomial times Gaussian payment.
It uses kernel order <=4. The complement 1-eta_O is paid separately
by Section 4, including E_P on the outer shoulder.

## 4. Finite transition substitutions and all mixed derivatives

Set mu_o=2^46/(X-8)^2, mu_s=(X-8)^-2 and mu=mu_o+mu_s.
EF2/EF23 imply the four H-P gap-jet bounds with mu_o. Require the
single source's four G-H errors <=mu_s L^j A_min, j<=3.
Then |partial_z^j(P-G)|<=mu L^j A_sum. The onset below ensures
mu<=1/4. EB1 and FI3 permit C0=1, C1=C2=C3=2 for P's model jets.
Put kappa_j=l_j/L^j using the actual cutoff caps, and define

    a1=C1+mu+kappa1 mu/2,
    a2=C2+mu+kappa1 mu+kappa2 mu/4,
    a3=C3+mu+3kappa1 mu/2+3kappa2 mu/4+kappa3 mu/8,
    d=R0_model, d1=(D0 R0_model+R1_model)/(2L),
    j2=kappa1+kappa2/4, j3=kappa1+3kappa2/4+kappa3/8.

These give finite GS13--GS14 inputs

    A1=4a1L, A2=4a2L^2,
    b0=2kappa1 mu L, b1=(kappa2+2kappa1)mu L^2,
    bb=kappa2 mu L^2,
    b2=(kappa3/2+2kappa2+2kappa1)mu L^3,
    e0=4(d+j2 mu L^2),
    e1=4[(d1+kappa1 d/2)L+j3 mu L^3],
    v=4[(C2+mu)L^2+d],
    a_t*=4[(C3+mu+kappa1 mu/2)L^3+(d1+kappa1 d/2)L],
    b_t*=2kappa1(mu L^3+dL),
    h_t*=(kappa2+2kappa1)mu L^4
                                  +(kappa2 d+2kappa1 d1)L^2. (EB13)

These are upper bounds for the ratios named in GS13/GS14; equal signs
here define allowances. The identities producing the mixed terms are
F_t=-(1-lambda)G_zz-lambda P_zz+lambda E_P and
(P-G)_t=-(P-G)_zz+E_P. No fourth source jet is introduced.
Use the actual W=q/(|F|^2+q), theta=q|F|^2/(|F|^2+q)^2, or their
explicit upper caps

    W<=min(1,16Gamma), theta<=min(1/4,16Gamma),
    Gamma=Q_+ exp(-(X-2)^2/2000+2(X+2)).               (EB14)

EB7 and the band floor prove these conservative caps. In GS14 set
k=2v+A_t min(1,16Gamma); retain A_t theta b0^2 as well as b_t*.
Evaluate GS13 and GS14 with EB13/EB14 to define positive envelopes
TC,TCt,TJ,Xi,DE,DB. Multiply by 8sigma k_alpha for Sigma and by
16sigma k_alpha for Sigma+; the latter includes both shoulders.
Use actual E_comp and E_join separately in e0,e1:

 E_comp=lambda E_P,
 (E_comp)_z=lambda(E_P)_z+lambda' E_P/2,
 E_join=lambda'(P-G)_z+lambda''(P-G)/4,
 (E_join)_z=lambda'(P-G)_zz+3lambda''(P-G)_z/4
                                      +lambda'''(P-G)/8. (EB15)

Outside the band E_comp=E_P or 0. This retains every partition of the
component heat residual and its derivative. Xi/2 remains in T_U.

For the raw enlarged-gap primitives use FT5 with delta0=2mu,
delta2=2mu L^2+l1 mu L+l2 mu/4, c_*=1/4,
C2_ratio=4a2L^2 (a harmless enlargement), epsilon<=Gamma, and
|E|/A_sum<=d+j2mu L^2. Multiply by 16sigma and the relevant EB10
weight supremum. This pays FT5--FT6 on all T_p, not merely on Sigma.
The actual ratios can also be used for sharper constants.

## 5. A source-independent finite common mean cap

The mean products in FT13 require a cap growing only logarithmically
with observation height. A growing-core regulator-floor cap cannot
replace this step. Define the finite eta-dependent constants

    Q_eta=1+Q_++|log eta|+eta^-2,
    R_*=ceil(2^2052 Q_eta),
    e_*=E_eta exp(-(R_*+3)^2/452),
    B1=(B0+B2)/2,
    C_H=max(2^40, 2^20[B1/e_*+(R_*+3)/113+1]).          (EB16)

E_eta,B0,B2 are FI12--FI15's explicit constants; they contain no source
approximation. The moment inequality u<=(1+u^2)/2 proves the B1 cap.
On centers |x|<=R_* the physical field satisfies
|grad S_H|<=B1/e_*+(R_*+3)/113. Integration over area <=4 and moving
the other derivatives onto K proves the central part of this C_H.
For all kernel orders <=4, k_alpha<=2^18 follows from FI15.

On exterior centers |x|>=R_*, the unit bounds and Cauchy on the larger
disks give |unit'/unit|<=2^8 L locally; the complement gives
|H_z/H|<=2^12 L. The integrable poles contribute at most 32pi to
integral|grad S_H| on a full support. EB9 pays |r_x|integral w;
it is <1 at this eta-dependent R_* and decreases afterwards.
Thus integral|grad S_H|<=2^18(1+L_x). Moving the remaining derivatives
onto K costs at most another 2^18, so C_H>=2^40 covers the resulting
2^36(1+L_x). For 1<=|gamma|<=3,

    |partial^gamma U_H|<=C_H(1+L_x).

After requiring the total k_gamma s<=1, a finite common cap for H and
the actual joined F is

    M_gamma=C_H(1+log(2+|x|))+1.                       (EB17)

On supports meeting the core or seam replace |x| by X+4. On pure
exterior supports retain the local height. This bounds derivatives of
the actual means; no component covariance is substituted.

## 6. Complete finite ledger and source tolerance

This section specifies a finite arithmetic evaluator for every row.
For each weight a in FT10--FT16, sum three nonnegative primitive
columns: core FT4, enlarged gap FT5 with EB13/EB14, exterior EB6/EB9.
Use area <=4 for the core; EB10 applies with R=X+8 when a core or seam
is present, and with R=|x|+8 for pure exterior supports. Exterior
collar allowance uses its actual local height, conservatively |x|-8
or X-8 on a seam. EB5 has sufficient enlargement slack. No integration
by parts is applied to an indicator of these regions.

For clarity the complete evaluator is reproduced here. Set
n_alpha=k_(alpha+x)+k_(alpha+y), d_alpha=k_(alpha+xx)+k_(alpha+yy),
and define st,wt,ct from the raw sums by FT10:

 st[a]=2v0[a]+w[a|r_t|]+2z0[a],
 wt[a]=w[a|r_t|]+2v1[a]+2z1[a],
 ct[a]=w[a|r_t|]+2v1[a]+4v2[a]+2z1[a]+4z2[a].

 C_alpha=[2n_alpha w[R1]+k_alpha(w[R2]+w[R1^2])]/(4pi),
 Ct_alpha={2n_alpha(wt[R1]+w[T1])
      +k_alpha(wt[R2]+w[T2]+ct[R1^2]+w[Th])}/(4pi).

Use tC,tCt,tJ,xi for the EB13--EB15/GS13--GS15 band payments, and
D_gap,D_B for the enlarged-gap DE and band DB payments. Then:

| Row | Finite error allowance |
| --- | --- |
| U_alpha, W_alpha, order <=4 | k_alpha s, k_alpha w[1] |
| calC_alpha, order <=2 | C_alpha+tC_alpha |
| R_alpha, order <=2 | d_alpha s/(4pi)+E_C,alpha |
| J_alpha, order <=3 internally | [n_alpha v0[1]+k_alpha v1[R1]]/(2pi)+tJ_alpha/pi |
| Ut_alpha, Wt_alpha, order <=2 | k_alpha st[1], k_alpha wt[1] |
| calCt_alpha, order <=2 | Ct_alpha+tCt_alpha |
| Rt_alpha, order <=2 | d_alpha st[1]/(4pi)+E_Ct,alpha |
| calB_alpha, order <=2 | k_alpha w[b_r] |
| Q_alpha, order <=2 | 4k_alpha v0[1]+d_alpha s+k_alpha w[c_r]+xi_alpha+N_alpha |
| actual source calS_alpha, order <=2 | E_Rt,alpha+E_J,alpha+x+E_J,alpha+y+D_out,alpha+D_gap,alpha+D_B,alpha |
| heat potential correction T_U, order <=4 | xi_alpha/2+2k_alpha z0[1] |

Here E denotes the allowance for the named row, not the field residual.
The actual mean-product allowance is precisely

 N_alpha=sum_(i=x,y) sum_(beta<=alpha) binom(alpha,beta)
    [(k_(beta+i)s) M_(alpha-beta+i)
                          +M_(beta+i)(k_(alpha-beta+i)s)]. (EB18)

Use GS9's signed-stress identity before taking absolute values, and
only then subtract the two actual filtered mean products. This keeps
Q and Delta Q unchanged. The density equation uses both E_Ct and
E_C,xx+E_C,yy, as well as E_Q,xx+E_Q,yy and
E_B,xx+E_B,yy. Its mean-gradient terms use EB18. There are no missing
time/source rows defined from a PDE, and no kernel order above four.
Fixed boundary traces use the corresponding component sums only within
the stated derivative orders; the internal third current derivative is
a source consumer. No moving boundary trace is claimed.

Here is a fully finite core column for the source constructor. Set
R_c=X+8, e_c=E_eta exp(-R_c^2/452), P2=B2+1 and Z=varepsilon/e_c^2.
Use FI13's weights at R_c and put

 p_m=(1+m/2)P2+1/2,
 s_t=A_t+2P2+1, w_t=A_t+3P2+1, c_t=A_t+11P2+3.

After factoring out 4Z from each core row, its coefficient D_r is:

| Row | D_r |
| --- | --- |
| U,W | k_alpha |
| C | [2n_alpha R1+k_alpha(R2+R1^2)]/(4pi) |
| R | d_alpha/(4pi)+D_C |
| J | [n_alpha p0+k_alpha p1 R1]/(2pi) |
| Ut,Wt | k_alpha s_t, k_alpha w_t |
| Ct | [2n_alpha(w_t R1+T1)+k_alpha(w_t R2+T2+c_t R1^2+Th)]/(4pi) |
| Rt | d_alpha s_t/(4pi)+D_Ct |
| B | k_alpha b_r |
| Q | 4k_alpha p0+d_alpha+k_alpha c_r+sum_(i,beta<=alpha)binom(alpha,beta)[k_(beta+i)M_(alpha-beta+i)+M_(beta+i)k_(alpha-beta+i)] |
| actual source | D_Rt+D_J,alpha+x+D_J,alpha+y |

The core T_U, compatibility and residual columns vanish. Add the
auxiliary D_gamma=k_gamma rows for the mean-cap constraint. Every
coefficient is now a displayed finite arithmetic expression; there is
no uninstantiated Lipschitz, collar or signed-source constant.

Declare **target 1 for every listed scalar component** at every stated
derivative order. Reserve 1/4 for the source's core column, 1/4 for
the enlarged gap plus its compatibility/heat columns, 1/4 for the
exterior column plus signed exterior heat, and 1/4 for later arithmetic
and filtering. In coupled rows split EB18 according to its s-column.
The last reserve is unspent: no arithmetic/filter implementation has run.
Individual equation sums inherit sums of these targets, not target 1
without an additional allocation. This is a declared physical absolute
error scale, not a measured error or an optimized tolerance.

A sufficient scalar demand for all four source jets is

    varepsilon_core=e_c^2 min_(D_r>0) [1/(16D_r)],
    A_min=exp(-X-10),
    0<varepsilon<=min(1, varepsilon_core, mu_s A_min).  (EB19)

EB7 and EB1 prove this A_min on the enlarged gap; one may instead use
the positive carrier minimum specified in FT19. Since L>1, the last inequality
pays all j=0..3 band demands. Use the actual common caps EB17 in D_r.
FI18's explicit Q,U,F,n0,N,M,b, FI16's positive clipping and FI20's
description bound now supply one fixed nonnegative source with four-jet
error <=29varepsilon/64. The cutoff, omitted nodal values, omitted slopes,
nodal arithmetic, exact construction and complete tail remain the separate
FI18--FI19 debits. No source values are evaluated by this return.

## 7. One explicit finite onset and decision

The following coarse closed rule makes the finite-existence assertion
reviewable. It is not an onset optimization. Using the fixed constants
in EB16, define

    C_eta=2^2048(1+C_H+Q_eta+P2)^16,
    m=2056+ceil(log2(R_*+16))+ceil(4log2(2+C_eta)),
    U=2^m, and choose X by EB2.                        (EB20)

Ceilings may be replaced by certified integer upper bounds with two
extra units, as in Note 44. No gamma or theta sampling is required.
All quantities in EB20 are finite for every fixed eta>0.

For completeness an envelope with ample constant slack for the *two
nonsource columns separately*, including all rows and the auxiliary
mean-cap rows, is

 C_eta { log^6(2+X)/X^2
                  +(1+X)^16 exp(-X^2/32000) }.         (EB21)

For X beyond EB20, EB14 gives Gamma<=Q_+ exp(-X^2/4000).
Use EB8's upper scale lambdabar(v)=sqrt(Q_+) exp(-v^2/8000).
Its logarithm obeys |log lambdabar|<=v^2/8000 once lambdabar<=1/2.
Monotonicity of the scale functions then gives the explicit reductions

    B<=2Q_+(1+v)^2 exp(-v^2/4000),
    H_L<=3Q_+(1+v)^4 exp(-v^2/8000),
    Z_L<=3Q_+(1+v)^2 exp(-v^2/8000).

For seam charts v>=X-8 use (X-8)^2>=X^2/4. Polynomial--Gaussian
monotonicity gives the denominator 32000 in EB21. For pure exterior
heights v>=X+4 keep v until taking the decreasing supremum. These
conversions retain the physical eta dependence before absorbing weights.

For the band coefficient count, EB4 first supplies
d,d1<=2^16/(X-8)^3; they are not left as unspecified residual constants.
To check the full row bound directly: the unweighted exterior primitives in
EB6 cost <=2^100 log^2(2+X)/X^2; the unweighted residual and EB12 cost
<=2^100 log^2(2+X)/X^3. In EB13, after mu<=1/4, all constants multiplying
the powers L,L^2,L^3,L^4 are below 2^100; the highest compatibility
time product is bounded by 2^200 mu L^4. Area <=16sigma removes one
L. Raw gap v0 costs <=2^100 mu L, and every other polynomially
weighted gap row retains EB14's exponential. EB10 has polynomial
degree at most two; its products used in the ledger have degree at
most four. EB9 adds at most two powers of height from |log Lambda|;
use |log of the explicit Gaussian envelope|<=Q_eta+(1+v)^2.
The power 16 therefore covers all polynomial products, support changes
and the remaining logarithms; no singular-square bound is used.
Kernel constants are <=2^18, finite Leibniz sums through order two
are <2^8, and EB18 contributes at most an additional factor
2^24(C_H+1)(1+L). The factors 2^2048 and the sixteenth power in C_eta
dominate these displayed products. On a pure exterior support repeat
the same argument with its local height; log^6(2+v)/v^2 and the
polynomial--Gaussian majorants decrease beyond this onset. On a seam
support |x-X|<=4, height replacements by X±8 are covered by EB5 and
the slack in these constants. Core-only supports have no nonsource debit.
This verifies an all-real-height envelope, not only a seam estimate.

At EB20, X is between 2^m and 2^m+1, C_eta<=2^(m/4),
and log(2+X)<=m+2. For m>=2056,
(m+2)^6<=2^(m/2) and exp(-X^2/32000)<=X^-32.
The two terms in EB21 sum to <1/4 (indeed with enormous spare room).
The inequalities follow from monotonicity after the indicated endpoint;
they are elementary analytic comparisons, not executed scalar checks.
EB20 also ensures Lambda<=1/2, mu<=1/4, all collar/unit gates and
the nonsource part of k_gamma s<1/2. EB19 pays the core part by <=1/4,
so EB17's common-cap premise is consistent. Every nonsource column
therefore fits its declared positive quarter-target. The full analytical
allowance is <=3/4 per scalar component, leaving the fourth quarter
for a future executed evaluator/filter. Finer source accuracy can shrink
the core column further without changing q or P. For any prescribed
0<theta<=1, the same construction gives scalar targets theta: replace
C_eta by C_eta/theta in EB20 and the numerator 1 in EB19's core minimum
by theta. The analytical allowance is then <=3theta/4; this is an error
parameter, not a numerical measurement. Equation sums still use their
stated component allocations.

**Decision:** this sufficient analytical budget is payable at a finite
onset in the requested regime. There is no unpaid term in this bounded
assembly and no failed numerical case. The onset is much larger than
2^2050 and is not practical. FI18/FI20 give only a finite source-size
upper bound; EB19 still includes exp(-R_c^2/226) from the coarse core
floor. Affordable source construction, observable arithmetic/filtering,
fixed-width time coverage, switch-uniform joining, both endpoint joins
and useful global error tuning remain distinct obligations.

## 8. Primary inputs, controls and work limits

The imported complex-analysis passages were checked in the official
[DLMF Cauchy derivative formula](https://dlmf.nist.gov/1.9.E31),
[Rouché theorem and maximum principle](https://dlmf.nist.gov/1.10#iv),
and [log-gamma/digamma expansions with complex remainders](https://dlmf.nist.gov/5.11#ii).
The collar contours and holomorphic quotients above supply their actual
hypotheses. The integrations and finite bookkeeping are proved here;
no external asymptotic constant is silently imported.

The collision controls are screened at their actual premises: Euler
factor controls lack this unchanged canonical completion; weighted-square
and finite-prime controls lack its full coefficients/reflection identity;
reflected and positive-primitive controls lack its canonical gamma/source
identity; atomic and heat-polynomial controls lack its smooth theta source.
They can satisfy generic transfer identities and can collide. A seam
covering a zero fails the chosen gap floor; another gap does not exclude
the collision. No RH, global simplicity or universal exclusion follows.

Exactly **zero scalar numerical/exact-rational checks** were executed;
the allowed six were optional. No theta/source/gamma/field sampling,
mesh, precision search, interval campaign or machine-symbolic research
execution occurred. File hashes and record/link checks are housekeeping.
The three read-only same-model subagent derivations audited geometry,
signed transfer and the full ledger; they share premises and are not
independent specialist review. No new chat, model change or dispatch to
another research chat was made.

**Disposition:** AN04 r1 is CLOSED at its bounded analytical scope.
The request is frozen and its return appended. No manuscript, snapshot,
commit or parent-status upgrade. **Next: Analysis — Sol**, the existing
[AN05 r1 / HDA-22](../research-progress/handoffs/HDA-18-AN05.md): turn
this short fixed-gap slab into fixed-width [95,97] coverage with paid
time, compatibility, source and actual-covariance terms. HDA-23's core
conditioning task remains a useful parallel analytical priority; HDA-24
remains gated on fixed-width assembly. The destination is still one
analytic prescription for every real height and time, with useful proved
errors and both infinite-time limits.

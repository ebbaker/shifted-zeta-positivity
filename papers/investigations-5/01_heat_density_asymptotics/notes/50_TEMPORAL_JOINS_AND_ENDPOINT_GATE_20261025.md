# Temporal joins, the negative-time cover, and the remaining positive gate

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. **gpt-6.1-sol (Codex), actual effort ultra**,
verified from current turn metadata. Chat **0017**, thread
01a173e5-dc96-7c31-946c-be54c871244c.

**Status: temporal-join contract and all-height negative-to-central cover
proved in-note; effective positive endpoint gate remains unpaid.**
This returns [AN07 r1](../research-progress/handoffs/HDA-18-AN07.md).
For every prescribed positive scalar tolerance, a finite source/model
prescription now covers **every real x, |y|<=1 and -infinity<t<=97**,
with the exact physical q and actual covariance. It retains the
negative infinite-time limit and the [63,97] switch construction.
A conditional positive temporal join has favorable scaling, but its
late-time field/collar constants and onset have not been made effective.
No all-real-time theorem, useful source cost or executed certificate follows.

Read the [result index](../../../../result-summaries/README.md),
[heat-flow cluster](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
[controls](../../../../result-summaries/12_collision_controls_and_screening.md)
and [avoid index](../../../../avoid/README.md), especially
[classification](../../../../avoid/01_restating_the_target.md),
[shared premises](../../../../avoid/05_same_model_reviews_and_shared_premises.md),
[scope](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[cancellation](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
and [status](../../../../avoid/19_status_files_that_lag_the_findings.md).
This is quantitative approximation, not an RH criterion or collision
exclusion. [Manifest 50](50_TEMPORAL_JOIN_INPUTS_20261025.json) pins the
request/source versions. [Review 32](../reviews/32_TEMPORAL_JOIN_AND_ENDPOINT_GATE_ASSESSMENT_20261025.md)
states the internal assessment; [Note 51](51_CHAT0017_RESULTS_SUMMARY_20261025.md)
summarizes the whole chat. Earlier notes are unchanged.

## 1. Contract and exact temporal algebra

Retain H_t=-H_zz, canonical source, physical q=epsilon_g^2, fixed
K=k_1 k_1, unnormalized potentials and actual covariance. Observation
|y|<=1 uses the same source/averaging buffers through |y|<=4 and field
buffer5. All derivatives are at fixed physical coordinates.

On a time overlap choose v in[0,1], flat at both endpoints, and set
Delta=F2-F1, DeltaB=B2-B1, B_i=(F_i)_bar_z, E_i=(F_i)_t+(F_i)_zz.
For v=b_*((t-a)/tau), FI9 gives |v'|<=c_b/tau, c_b=2exp(4/3).
Exactly,

 F=(1-v)F1+vF2, B=(1-v)B1+vB2,
 E=(1-v)E1+vE2+v'Delta,
 E_z=(1-v)(E1)_z+v(E2)_z+v'Delta_z,
 B_t=(1-v)(B1)_t+v(B2)_t+v'DeltaB,
 (B_z)_t=(1-v)(B1)_{zt}+v(B2)_{zt}+v'DeltaB_z.       (TJ1)

Likewise F_t and (F_z)_t acquire v'Delta and v'Delta_z.
All spatial jets are the actual convex field combinations. No v'' is
needed for the Note 43 tuple: it contains one direct time derivative,
not a second time derivative of the heat residual. Spatial/source jets
through3 and weak kernel derivatives through4 remain sufficient.
A claim about a second time derivative would require new inputs.

The compatibility curvature T_C, Xi, T_J, direct density/current, and
actual Q of F are the GS7--GS12 functions of this F. They are not convex
averages of their component observables. In particular the density
equation retains -(calC)_t and -square calC/2, Delta Q, Delta calB,
and Delta(K*T_U)/(4pi), where T_U=Xi/2+2Re Z_0.

## 2. The additional mismatch norms and a signed-source identity

On a common zero-free support use the actual F denominator and define

 d0=|Delta|/|F|, d1=|Delta_z|/|F|,
 dB=|DeltaB|/|F|, dBz=|DeltaB_z|/|F|.                (TJ2)

With Lambda_T=||v'|| the added allowances in GS13--GS14 are

 e0,v: Lambda_T d0; e1,a_t*: Lambda_T d1;
 b_t*: Lambda_T dB; h_t*: Lambda_T dBz.              (TJ3)

The remaining ratios use actual spatial field/cutoff caps. No bound
on differences of observable tuples implies TJ2. For example a constant
phase reversal F2=-F1 preserves each component potential, density,
current and actual covariance but can cancel the field at v=1/2.
This is a logical control on that inference, not an admissible change
to the fixed positive canonical source.

Let delta_Delta mean directional field variation F -> F+sDelta at
fixed q. Use GS14's A1,b0,b1 and theta_reg=q|F|^2/(|F|^2+q)^2.
Differentiating GS8, before taking absolute values, gives

 pi |delta_Delta T_C| <=
 theta_reg(2b0 dB+4b0^2 d0)
 +2(dBz+3b1 d0+d1 b0+A1 dB+6A1 b0 d0).             (TJ4)

Multiplication by |v'| pays the new compatibility-time piece.
It is also necessary in a global weak formula for the temporal heat
defect. Put E_T=v'Delta and Z_m,T=w^m E_T conjugate(F)/D. For every
real compact spatial test psi, the correct nonholomorphic formula is

 4pi <D_{E_T},psi>
 =2Re integral Z_0,T Delta psi
  -4Re integral Z_1,T grad r dot grad psi
  -2Re integral [Z_1,T Delta r+(Z_1,T-2Z_2,T)|grad r|^2]psi
  -4pi v' integral (delta_Delta T_C)psi.             (TJ5)

Here D_E is GS12's already defined density variation, linear in E,E_z
for fixed F. To prove TJ5, vary the exact identity
Delta S=4pi(rho+C_reg+T_C) at fixed q. Then
delta S=2Re Z_0, delta w=-2Re Z_1 and
delta[w(1-w)]=-2Re(Z_1-2Z_2). Integration by parts on the full
test gives the displayed signs. Omitting the last line would import
the holomorphic PE34 outside its hypotheses. That line vanishes on
holomorphic regions where B=DeltaB=DeltaB_z=0.

The actual source (1-2w)(r_t rho+grad r dot j) contains no explicit v'.
The v' contribution to rho_t is precisely D_{E_T}, and cancels that
contribution to D_E in the source balance before absolute values.
A coarse FT16 bound may pay both copies; it must not interpret v'
as a new physical source. The direct time and heat-potential terms
still require TJ3--TJ5.

For a region containing zeros one may instead use sqrt(q)>=e>0.
With |F_z|<=M1, |B|<=N0, |B_z|<=N1 and absolute mismatches D0,D1,DB,DBz,

 pi |delta_Delta T_C| <=2N0 DB/e^2+4N0^2 D0/e^3+DBz/e
  +2N1 D0/e^2+(N0 D1+M1 DB)/(2e^2)+2M1 N0 D0/e^3,
 pi |D_{E_T}|<=|v'|(2M1 D1/e^2+4M1^2 D0/e^3).       (TJ6)

Write pi T_C=q|B|^2/D^2+2Re[B_z u-F_z B u^2],
u=conjugate(F)/D. The inequalities |u|<=1/(2e),
|delta u|<=D0/e^2 prove TJ6, including at multiple zeros.
A spatially uniform e is used only on the pre-switch intervals below;
it is not imposed on the positive all-height problem.

## 3. Complete primitive-to-tuple consumer

Form FT3's raw s[a],w[a],v_m[a],z_m[a] for the actual blended F.
Split nonnegative primitive integrals before weak differentiation.
Use the strengthened arbitrary-q gap weight branch SW12, individual
regulator-weighted exterior estimates, and actual mixed-field units
on any holomorphic collars. On nonholomorphic supports use TJ4/GS13/
GS14 or TJ6; positivity of q alone is not a zero-free gap proof.

Use the exact finite maps FT10--FT13, with the new E_T and TJ1 in
the z_m and compatibility-time inputs:

| Consumer | Payment |
| --- | --- |
| U,W through4 | k_alpha s, k_alpha w[1] |
| R,calC through2 | d_alpha s/(4pi)+C_alpha+tC_alpha; C_alpha+tC_alpha |
| J through2, order3 internally | (n_alpha v_0[1]+k_alpha v_1[R1])/(2pi)+tJ_alpha/pi |
| Ut,Wt,Rt,calCt through2 | FT10's actual st,wt,ct; FT11's regulator Ct and separate tCt from GS14/TJ4 |
| actual Q,Delta Q | 4k_alpha v_0[1]+d_alpha s+k_alpha w[c_r]+xi_alpha+N_alpha, actual mean-product N_alpha |
| actual calB | k_alpha w[b_r] |
| actual calS | exact GS12, FT16 with signed heat paid by TJ5 or the holomorphic/test-partition route |
| heat-potential through4 | xi_alpha/2+2k_alpha z_0[1] |

C_alpha,Ct_alpha retain r_t,r_x,r_xx,r_tx,r_txx and the squared-gradient
time coefficient. T_C is separate from regulator curvature. Actual
mean caps are justified by primitive-gradient rows before use in
N_alpha. A time blend changes neither K nor observation boundaries.
Every actual field-cutoff derivative is in TJ1; no derivative of a
regional indicator is taken.

Where a spatial heat test partition is used, FT14's two first
commutators and eta_O,xx remain. Apply TJ5 with the partitioned test,
or PE34 only on its holomorphic part. No eta_O,t is created by an
instantaneous spatial pairing. Fixed spatial/time traces inherit the
same component allowances. Equation sums use their actual component
sums, not an unjustified single scalar target. This is a transfer
contract from the declared field inputs, not unconditional all-time
coverage.

## 4. An explicit negative endpoint overlap

Let q0=eta C>0, with C=Phi(0)sqrt(pi)/2. For T>=1 use

 I_-=[-2T,-T], v_-=b_*((t+2T)/T),
 N(t,z)=C/sqrt(-t) exp(z^2/(4t)),
 F_-=(1-v_-)N+v_- G.                                (TJ7)

Both N and the one finite source G are exact heat fields. Require its
four absolute jets j=0..3 to approximate H by epsilon<=T^-5/2 on
[-2T,97], every real x and |y|<=4. FI18--FI20 apply literally: their
source-error integrands use only exp(tu^2)<=exp(97u^2), not a lower time
endpoint. The finite positive clipped source is fixed throughout this
whole slab. Later extra demands are imposed on this same source.

Set, using Note 26's explicit positive moments,

 g_j=B2_source J_{j+2}(4)/2,
 h_j=Phi(0)J_j(4)+g_j, p2=h_2+g_2+2.                 (TJ8)

J_m(4)=integral_0^infinity v^m exp(-v^2+4v)dv has NE6's erfc/recurrence
formula. The fixed strip4 lies inside its transverse norm4sqrt(-t).
NE7 gives d_j<=g_j T^{-(j+3)/2}, while G-H contributes epsilon.
Thus

 |G-N|<=(g0+1)T^-3/2, |G_z-N_z|<=(g1+1)T^-2,
 |H-F_-|<=(g0+1)T^-3/2,
 |H_zz-(F_-)_zz|<=(g2+1)T^-5/2,
 |E_-|<=c_b(g0+1)T^-5/2,
 |(E_-)_z|<=c_b(g1+1)T^-3.                          (TJ9)

B=0 identically. The physical floor is
epsilon_g>=q0/(2sqrt T), and |r_t|<=1/T, with all spatial regulator
coefficients zero. In CJ5 one may use a<=sqrt T/q0, b_*<=4T/q0^2,
k<=2sqrt T/q0 and P2<=p2 T^-3/2. Define finite constants

 S=2(g0+1)/q0,
 V_m=(g2+1)/q0+4(1+m/2)p2(g0+1)/q0^2, m=0,1,2,
 Z=c_b(g0+1)/q0,
 S_t=2V0+S+2Z, W_t=S+2V1+2Z,
 C_t=S+2V1+4V2+6Z.                                  (TJ10)

The actual primitive allowances obey

 s,w<=S/T, v_m<=V_m/T^2, z_m<=Z/T^2,
 st<=S_t/T^2, wt<=W_t/T^2, ct<=C_t/T^2.              (TJ11)

Subscripts on allowances are labels, not derivatives of an error bound.
For actual mean caps through3, first bound |grad S_F| and |grad S_H| by
2(h1+1)/(q0 sqrt T). Move the other derivatives onto K. A finite cap is

 M_gamma<=m_gamma/sqrt T,
 m_gamma=2(h1+1)/q0 min_(i:gamma_i>0)L_(gamma-e_i).    (TJ12)

Consequently the actual mean-product allowance N_alpha is
O(T^-3/2) with the explicit finite Leibniz coefficient CJ13 evaluated
at e_gamma=L_gamma S and M_gamma=m_gamma.

Define K_neg as the maximum of **the finite CJ8--CJ14 and holomorphic heat
coefficients**, after setting the spatial regulator coefficients to0,
rt coefficient1, primitive coefficients TJ10 and mean caps TJ12;
include the internal order3 current and residual heat/source rows.
For the heat-potential row use the pointwise-primitive coefficient
2L_alpha Z from CJ25, rather than identifying pointwise z with a raw
area integral in FT18.
All are displayed positive sums/products of q0,g_j,h_j,c_b and kernel
norms; no eventual constant is in this definition. Replacing every
T^-p, p>=1 by T^-1 shows every scalar row is <=K_neg/T.
The same coefficients with E=0 dominate the Gaussian endpoint rows
for all -t>=T. Hence, for target 0<theta<=1,

 T>=max(1,4K_neg/theta)                              (TJ13)

pays both the negative endpoint and its overlap by theta/4.
The width T gives O(T^-2) direct potential-time and weak density-time
allowances here. Note26's sharper O(T^-3) endpoint density-time rate
is not claimed for this blended interval from the displayed weak table.
No derivative allowance was obtained by differentiating NE7.

## 5. Connect the same source to the switch construction

Use G alone on[-T,63]. Its global absolute source jets approximate H
uniformly in real x. The time-only physical regulator has the explicit
floor

 e_mid=q0/[1+max(T^2,63^2)]^(1/4)>0.                  (TJ14)

CJ4--CJ14, with canonical moment caps at97, give a finite coefficient
K_mid(T) multiplying epsilon for the whole tuple. Include the auxiliary
actual-gradient caps before covariance products and require
epsilon<=theta/[4(1+K_mid)]. No outer chart is needed here.

On[63,64] set v0=b_*(t-63), and use Note 49's same source and moving
spatial field F49=G+lambda(P-G):

 F0=G+v0 lambda(P-G).                                (TJ15)

P is used only where lambda is nonzero and on its established branch.
The flat product is extended by0 into the inner region where P need
not be defined. At63 this is G; at64 this is F49, with smooth matching.
On this whole overlap beta=0, r_x=0 and epsilon_g>=q0/9. No post-switch
Gaussian premise or multiple-root exclusion is needed.

Here is an explicit field payment for the noncompact temporal difference.
SW3 on the real line and EB1's logarithmic carrier-derivative bound give,
on |Im z|<=5 and the same enormous exterior onset,

 A_sum(t,z)<=2 exp(5log(2+|Re z|)-|Re z|/4)
                                      <=exp(-|Re z|/8). (TJ16)

The last elementary comparison holds at the existing onset. The field
extension SW1/EF2, FI9's cutoff constants and |X'|<=8 then imply that
all mixed spatial jets through3 of F0-H, the direct first-time jet
differences F0_t-H_t and (F0_z)_t-H_zt, and the E0,E0z,B0t,(B0z)t
allowances needed by Section 3, are bounded by

 delta_bridge=2^64 L^3(epsilon+exp(-a_X/8)),
 a_X=X0-300, L=log(2+X0+300).                         (TJ17)

For checking this generous finite coefficient: C_j<=2^26 in EF2;
each spatial profile derivative contributes at most FI9's
832exp(4/3)64^3 L^3; each first-time derivative contributes at most8
times one further spatial profile order or c_b. The differentiated
products in TJ1 and MW7--MW10 have fewer than64 terms at the stated
orders. Terms such as lambda_x D_zzz and lambda_xx D_zz initially
have L^4 in their model-error part: retain EF2's u^-2 and use
L/u^2<=1 there to absorb that extra logarithm. The corresponding
source errors are absolute epsilon, so their largest factor is
lambda_xxx epsilon=O(L^3 epsilon).
Monotonicity of log^3(2+u)exp(-u/8) beyond the onset handles
pure exterior supports. No fourth field jet is introduced.
The source term is a globally uniform absolute error, not a relative
source error claimed at infinite height.

For completeness, the finite conversion coefficient K_bridge in
error_r<=K_bridge delta_bridge is specified mechanically, without an
unspecified compact Lipschitz constant. Freeze canonical moments B0..B3
at97, M=2+max_j B_j, Q=16eta^2, e=q0/9 and |rt|<=1. Work with the
exact GS7--GS12 rational maps, including GS8 differentiated before
taking magnitudes, and their direct-time derivatives, with
r_x=0. Each rational monomial has the form

 c q^a product_i u_i^(n_i) /D^b, N=sum_i n_i,

where a,b are nonnegative integers, and real/imaginary jet variables
and their conjugates have caps M. GS13/GS14's ratios involving 1/F
are not used in this zero-safe coefficient construction.
Use for its field-variation coefficient

 |c|max(1,Q^a)[N M^(N-1)e^(-2b)
                         +2b M^(N+1)e^(-2b-2)],        (TJ18)

omitting the first term when N=0. This follows by telescoping numerator
factors and differentiating D^-b; |delta D|<=2M delta. For log D
use1/e. The jet list includes F,a,c,c_z=F_zzz,B,B_z,B_bar_z,B_zz,
F_t,a_t,B_t,B_zt; expand E=F_t+c and E_z=a_t+c_z in the terms.
TJ17 bounds its differences, and delta_bridge<=1 freezes these caps
independently of X0. Physical q,qt are the same for H and F.
Sum TJ18 over the explicit rational terms of each raw observable,
then apply the kernel norms through4. Explicit actual mean caps and
potential-difference coefficients for the mean-product sum are
M_gamma^U=(8M/e)min_(i:gamma_i>0)k_(gamma-e_i) and
E_gamma=4k_gamma/e, 1<=|gamma|<=3. Indeed |S_i|<=2M/e,
the support area is4 and |delta S|<=delta_bridge/e. Insert these in
FT13's actual mean-product Leibniz sum, explicitly
sum_(i=x,y)sum_(beta<=alpha)binom(alpha,beta)
[E_(beta+i) M^U_(alpha-beta+i)+M^U_(beta+i) E_(alpha-beta+i)].
Maximize over the finitely
many tuple/heat rows and1 to define
K_bridge. This is a finite formula algorithm in fixed displayed
rational maps; it uses no root information, sampling or hidden
asymptotic constant. TJ6 can replace the compatibility subrows.
Thus it remains valid through zeros/multiple events.

Choose the joining phase beyond Note49's onset at target theta/4 and
also beyond 2^m, with

 m=16384+ceil(8log2(2+2^64 K_bridge/theta)).            (TJ19)

The same elementary binary/exponential comparisons as SW25 pay the
exponential part of K_bridge delta_bridge below theta/32. Impose
epsilon<=theta/[2^69 K_bridge L^3] for its source part. These finite
positive demands are compatible with SW24 and TJ9/TJ14, by refining
the **same** finite source. If necessary increase m by certified integer
upper-bound slack. No evaluation is claimed.

## 6. The proved negative-to-central domain cover

Choose T by TJ13; choose X0 by SW25/TJ19; choose one G satisfying the
minimum of all source demands above and SW24 at target theta/4.
This order is noncircular. All source weights still use upper time97.

| Time domain | Actual field prescription | Full-support payment |
| --- | --- | --- |
| t<=-2T | N | Note26 and TJ10--TJ13 |
| [-2T,-T] | (1-v_-)N+v_-G | TJ7--TJ13, exact cutoff heat |
| [-T,63] | G | TJ14, global time-only floor |
| [63,64] | G+v0 lambda(P-G) | TJ15--TJ19, actual nonholomorphic time/space defects |
| [64,97] | F49 | Note49 at target theta/4 |

The union is **(-infinity,97] x R_x** on |y|<=1. Each scalar row
has a bound <=theta/4 after the stated allocations; equation sums
retain their component sums. No number-of-charts factor appears,
since these are comparisons at the actual time of one prescribed
field, with flat matching at each endpoint. This is a finite analytic
prescription involving a smooth nonholomorphic spatial cutoff, not
an assertion that F is an entire heat solution. Its exact defects
and actual covariance remain. At t->-infinity it is exactly the
Gaussian model, with Note26's complete vanishing comparison errors.
For smaller theta the finite parameters/source change. No one
unchanged finite source is asserted to have arbitrarily small error.

## 7. One focused positive-overlap attempt

Let I_+=[T_+,T_++Delta_t], Delta_t>0, T_+>=128, and suppose a central
construction F_c=G+lambda(P-G) has been paid up to its upper endpoint.
Blend to the **same** saddle P:

 v_+=b_*((t-T_+)/Delta_t),
 F_+=(1-v_+)F_c+v_+P
    =G+[v_++(1-v_+)lambda](P-G).                     (TJ20)

The exterior is identically P, so the new time defect is confined to
the finite core and spatial bands. The core may contain many roots:
its small regulator floor is not a useful uniform positive-time
estimate. Instead require full-buffer relative jets

 |partial_z^j(H-P)|<=C_j e(t,x)Lcal^j A_sum,
 e=t^(3/2)/[1+|x|+t Lcal]^2, Lcal=log(2+t+|x|),
 j=0,1,2,3,                                        (TJ21)

with finite branch/slope/unit/pole constants, valid at **every height**
for t>=T_F. The mixed core field G/P has paired simple roots and
analytic units by the same Rouche/unit argument when its relative
error is below the fixed margin; PE6 observable errors alone are not
this premise.

For a core union radius R_c choose the source reserve

 mu_s<=T_+^(3/2)/
  {16[1+R_c+(T_++Delta_t)log(2+T_++Delta_t+R_c)]^2},
 epsilon<=mu_s A_min.                              (TJ22)

Here A_min is a proved positive lower bound for A_sum on the full
complex core buffer and time overlap, from the supplied late-time
branch/carrier table. Note49's exp(-X0-320) formula is not reused at
arbitrary late T. This keeps the source error below e/16 throughout the finite core;
Lcal>=1 pays the other jets. Constants for this source constructor
depend on its new finite upper time. Positive-source existence is
available from the same moment/tail recipe, with that upper time in
place of97; it has not been instantiated or executed here.

On each holomorphic core collar the temporal E_T/F has a pole residue
<=C|v_+'|e/Lcal and a regular part <=C|v_+'|e. Scaled radial integration
and the finite collar count yield z_m,T<=C|v_+'|e, without an inverse
regulator. In the spatial bands TJ3/TJ4 are lower logarithmic-order
additions to the existing GS14 payment. Use PE30's uniform late-time
mean cap C_U Lcal, not the compact-floor C_H,J whose dependence on T
could destroy the claimed endpoint decrease. With actual regulator
weights and signed heat cancellation, the resulting **conditional**
whole-tuple bound has the form

 C_+(1+c_b/Delta_t)T_+^-1/2
                       + source and spatial-seam reserves.       (TJ23)

C_+ is the finite positive-expression consumer of the supplied field,
unit/pole, mean and regulator constants in the ledger of Section3,
not a fitted error coefficient. It and every constant entering it must
be uniform for t>=T_F and independent of T_+,Delta_t,R_c and source
choice; compact-J spatial seam constants stay in their separate reserve.
Without that uniformity the threshold below would be circular.
With these constants supplied,
sup e<=T_+^-1/2/log^2(2+T_+), sup e Lcal<=T_+^-1/2/log(2+T_+)
pay the collar margins. Define the supplied fixed collar margin
mu_coll>0 and C_jet=1+max_(j<=3)C_j, including the source reserve.
Require C_jet sup e<=mu_coll/4 and
C_jet sup(e Lcal)<=mu_coll/4. A sufficient threshold is

 T_+>=max{128,T_F,
          [8C_+(1+c_b/Delta_t)/theta]^2,
          [4C_jet/mu_coll]^2}.                                  (TJ24)

Then select the spatial joining height, source tolerance and union
buffer; never infer TJ21 from tuple agreement.

## 8. The exact unpaid finite gate and disposition

Notes30/31 prove TJ21, its slope/unit/pole bounds and the uniform
mean cap eventually, but leave their C_j,T_F and related constants
uninstantiated. Note49 supplies an effective table only through97.
Its fixed-compact onset cannot be substituted at all heights for
the target-dependent late interval[T_+,T_++Delta_t]. In particular
it does not control the low/middle-height part as T_+ grows.

The first unpaid consumer can be recorded directly as

 |v_+'| integral_(Omega_p cap core)
   a w_F^m |(P-F_c)conjugate(F)|/(|F|^2+q),
 m=0,1,2, with weights a used in FT10--FT16.          (TJ25)

TJ21 plus the finite mixed-field units would pay the unweighted TJ25
at the e scale and its actual regulator-weighted consumers at the
corresponding e or e Lcal^2 scale of PE19/PE21.
A triangle inequality with PE6 does not, and a global compact-floor
bound introduces epsilon_g^-1. For example its late-time core factor
at |x|=R_c contains exp(R_c^2/[2kappa]), while TJ21's relative allowance
decays polynomially in height. Even the carrier's linear exponential
height decay does not pay this quadratic exponent at fixed T_+.
Increasing the spatial cutoff does
not pay this attempted coarse budget. This is failure of that
bound, not a counterexample to the actual join or a universal
obstruction. The pole/unit route has favorable scaling once its
finite table is provided.

Under r1's stop rule, stop here with the positive finite-input gate
identified. The intended final domain table would replace the last
line of Section6 by a paid central extension through T_++Delta_t,
add TJ20 on I_+, and use P thereafter. Those missing rows have not
been proved effective, so their proposed union is not an accepted
all-real-time cover. No error is propagated from a residual.

**Disposition:** AN07 r1 CLOSED at its bounded contract/attempt scope;
negative-to-central cover accepted in-note, positive effective gate
open. HDA-17 Partial, HDA-18 Gated, HDA-20 unfulfilled. Next
**Analysis — Sol**, [AN08 r1](../research-progress/handoffs/HDA-18-AN08.md):
make the late-time all-height field/collar/mean table effective and
consume it in TJ24--TJ25. This is a named finite-input completion,
not yet a resistant new singular mechanism warranting Astra.
HDA-23 conditioning/affordability remains separately ready.

No numerical/exact-rational/machine-symbolic research execution,
theta/source/gamma/field sampling, mesh/precision search or interval
campaign. Prior checks were reused by reference; hashes/sizes/links
are housekeeping. Main-assistant derivations and three read-only
same-model audits share premises and are not specialist independence.
No prior-note/manuscript edit, DRAFT_HISTORY milestone, snapshot,
commit, new chat or model change. The [DLMF Cauchy formula](https://dlmf.nist.gov/1.9.E31)
and [complex-gamma remainder rules](https://dlmf.nist.gov/5.11#ii)
were rechecked for the standard inherited field inputs; TJ1--TJ25
are derived from the retained exact identities.

# Switch-uniform moving-gap assembly

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. **gpt-6.1-sol (Codex), actual effort ultra**,
verified from current turn metadata. Chat **0017**, thread
`01a173e5-dc96-7c31-946c-be54c871244c`.

**Status: switch-uniform all-height finite-interval comparison proved
in-note; same-model internal review only.** This returns
[AN06 r1 / HDA-24](../research-progress/handoffs/HDA-18-AN06.md).
The declared domain is **63<=t<=97, every real x, |y|<=1**, with the
unchanged physical regulator and full transverse/averaging buffers.
One moving model gap and one fixed positive source per construction
give a complete analytical error tending uniformly to zero as the
joining height grows. The interval includes the physical switch and
the whole previously accepted [95,97] interval. The rate is slower
near the crossover; a uniform post-switch Gaussian is not assumed.
No source/evaluator is executed or shown affordable. HDA-17 Partial,
HDA-18 Gated and HDA-20 unfulfilled remain.

Read the [result index](../../../../result-summaries/README.md),
[heat-flow cluster](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
[collision controls](../../../../result-summaries/12_collision_controls_and_screening.md)
and [avoid index](../../../../avoid/README.md), especially
[classification](../../../../avoid/01_restating_the_target.md),
[scope](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[cancellation](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
and [status](../../../../avoid/19_status_files_that_lag_the_findings.md).
This is quantitative approximation, not an RH criterion. The
[input manifest](49_SWITCH_ASSEMBLY_INPUTS_20261025.json) pins the frozen
request and source versions; [Review 31](../reviews/31_SWITCH_UNIFORM_ASSEMBLY_ASSESSMENT_20261025.md)
records the internal assessment. No predecessor note or manuscript is
edited by this return.

## 1. Contract and finite field inputs on the larger interval

Retain Notes 30/42/48's canonical H, full implicit-saddle P, exact
source, q=epsilon_g^2, eta>0, K=k_1 k_1 and actual signed covariance.
Let J=[63,97], Y_b=4 and retain Note 45's |Im z|<=5 field buffer.

Note 45's stated [95,97] theorem is not simply imported outside its
domain. Here is the needed finite extension. Its contraction rectangle,
EF3--EF17 contour identities, upper t<=97 bounds and central constant
remain valid on J. Replace the lower bound 95 by 63 in the reductions:

 -63lambda^2/100+(194/3)lambda+6<=-lambda^2/2,
 63lambda/200>3,
 48 exp(97/2-63lambda/10)<=exp(-3lambda), lambda>=1000. (SW1)

The first comparison has positive increasing difference beyond 1000;
the other two are direct linear comparisons with the same elementary
exponential bounds used in EF19. Left/connector/middle prefactors keep
their original upper t97 values; 16/t<1 still holds. Central
12t^(3/2)<=11640 and all six end/arithmetic debits are unchanged or
smaller. Thus EF1/EF2 hold on J with the **same** constants 12000,
384000,3072000,36864000 and binary onsets. These are analytical
inequalities, not new scalar executions. All contour regions, infinite
ends and arithmetic modes remain paid.

The same full-circle proof now gives EB1--EB6's model, collar/unit,
raw simple-pole and residual constants uniformly on J, and the
conditional radial-integration constants underlying EB9. EB8's positive
uniform Gaussian rate is not extended; SW10--SW14 replace its premise.
In addition to
EB6 one may explicitly retain its arbitrary-positive-q weight estimate

    s_O[1],w_O[1]<=2^26 e,
    v_m,O[1]<=2^44 e(1+|log e|+l^2), m=0,1,2,
    z_m,O[1]<=2^22 d, m=0,1,2,                       (SW2)

with local e=2^44/(u-8)^2, d=2^20/(u-8)^3, l=log(2+u).
The unit interpolation proof bounds the scaled delta-w integral by
2^14 e before restoring area and collar count, so the first bound is
the same finite raw calculation as EB6, not a new observable theorem.
For Z_m use |Z_m|<=|Z_0|. Every restricted exterior integral enlarges
its intersecting collars and separately pays the zero-free complement.

For the exact real carrier A_s(t,u)=|S_t((1+iu)/2)|, complex Stirling
also supplies, on the same huge onset,

    exp(-u)<=A_s(t,u)<=exp(-u/4), t in J.              (SW3)

The lower bound also holds arm by arm on the full complex buffer:
|S_t((1+iz)/2)|>=exp(-|Re z|) for |Im z|<=5 and the same exterior
onset; the reflected arm has the same bound. This is EB7's full-sector
Stirling proof, whose upper-t97 constants suffice after SW1. It is not
inferred by integrating a real-line logarithmic-derivative bound across
the transverse buffer. The upper bound in SW3 is used on the real line.
For the upper bound, insert EF4 in the first omitted log-gamma formula:
the imaginary-argument contribution is <=-pi u/8+Re p/2, while
Re p<=3+49log u. The real logarithmic term, polynomial factors,
saddle exponent h^2/t and determinant are bounded above in total by
128log^2u+512log u+1024. This is <u/8 at log u>=1000, and pi>3.
The permitted complex remainder is bounded on the whole sector; no
derivative of an asymptotic allowance is used.

## 2. Exact physical regulator and finite switch constants

Write the actual regulator, without alteration, as

    r=log q=a(t)-beta(t)x^2,
    beta=0 for t<=64, beta=chi/kappa for t>64,
    a=2[(1-chi)ell_b+chi ell_+],
    ell_b=log[eta C(1+t^2)^(-1/4)], ell_+=log(M0/kappa). (SW4)

For t<=64 set chi=0 and a=2ell_b. For 64<t<=97 the exact switch is
chi=exp(-1/v)/(exp(-1/v)+exp(-1/(1-v))), v=(t-64)/64.
Its exact amplitude derivative is retained:

    a'=2[(1-chi)ell_b'+chi ell_+'+chi'(ell_+-ell_b)],
    beta'=chi'/kappa-chi kappa'/kappa^2.               (SW5)

In particular the amplitude mismatch term is not omitted. From SC1,
the source saddle satisfies

    1/4<L_s<1, 36<kappa<618, 0<kappa'<50,
    exp(-3)<M0<exp(110), chi'<=1.                    (SW6)

At 1/4 the source-exponent derivative is positive using pi<22/7 and
e<11/4; at 1 it is negative. The larger root is the maximum. There
q_t(L_s)>=q_t(1/4)>-3 and q_t(L_s)<106. SC1's positive prefactor
is >1 and <exp(4), proving the mass bounds. Differentiate the saddle
exactly for kappa'=8L_s+16tL_s/kappa-2. The bound on chi' follows
from chi<=exp(64/31)exp(-1/v), the maximum of v^-2 exp(-1/v),
and (1-v)^-2<5; the resulting total is <64 before division by 64.
These elementary bounds concern the physical source saddle, not zeros.

Put A_eta=512(1+|log eta|), Q_+=16eta^2+exp(220). Then

    |a|,|a'|<=A_eta, exp(a)<=Q_+,
    beta<=1/36, |beta'|<=1/8.                         (SW7)

For instance |ell_b|<=|log eta|+8, |ell_+|<128,
|ell_b'|<1, |ell_+'|=|L_s^2-3kappa'/(2kappa)|<4 give the a' bound.
The beta' bound follows from 1/36+50/36^2<1/8. All beta terms are
exactly zero before and at 64, with flat matching.

A further **flatness** bound, stronger than the constant bound for
time estimates at large height, is

 |beta'|<=4 beta[1+log^2(1/beta)] for beta>0;
 beta'=0 for beta=0.                                 (SW8)

Indeed z=log(1/beta)>=log36+1/v-64/31>=1/v.
The exact formula chi'/chi=(1-chi)[v^-2+(1-v)^-2]/64 and
kappa'/kappa<50/36 then give SW8. The function
s[1+log^2(1/s)] is increasing on (0,1), since its derivative is
(log(1/s)-1)^2. No Gaussian with a positive uniform beta_min is used.

The core coefficients must also change. On a finite rectangle |x|<=R,
the following safe replacements for FI12/FI13 are explicit:

 E_sw=min((2/5)eta exp(-4),exp(-3)/618),
 e_core=E_sw exp(-R^2/72),
 A_t=A_eta+R^2/8, R1=R/18, R2=1/18,
 T1=R/4, T2=1/4, Th=R^2/36,
 c_r=1/18+R^2/324, b_r=A_t+c_r/2.                    (SW9)

They follow from SW6--SW7 and epsilon_+=M0/kappa exp(-x^2/(2kappa)).
For epsilon_b use C>4exp(-4) and t<=97. A geometric interpolation
is at least the smaller of its two positive lower bounds. The old
M0>=1 premise and exponent denominator 452 were specific to [95,97];
they are not reused here. The kernel/source moment upper constants
through time97 remain valid.

## 3. Two regulator regimes and the missing weight branch

For each large full support use local center height u and its fixed
enlargement by 8. Split its **allowances**, not F, into

    A: beta(t)u<=16; B: beta(t)u>16.                   (SW10)

There is no field/time/test partition at this boundary and no derivative
of its indicator. The actual q, beta and amplitude in the construction
remain SW4--SW5.

In regime A, SW8 and monotonicity give uniform full-buffer coefficient
allowances, with l=log(2+u):

 R1<=64, R2<=32/u,
 |r_t|<=A_eta+2^10 u l^2,
 T1<=2^10 l^2, T2<=2^10 l^2/u,
 Th<=2^17 l^2, c_r<=2^13,
 b_r<=A_eta+2^10 u l^2+2^12.                         (SW11)

For example beta<=16/u, |beta'|<=64[1+log^2(u/16)]/u,
and |x|<=u+8. This pays the large beta' x^2 term rather than replacing
it by a constant. beta=0 is included in these estimates.

On a zero-free gap the field segment between H and F has modulus
>=c_* A_sum, c_*=1/4. A necessary strengthening of FT5 is

 w_T<=min(1, 2epsilon delta0/c_*^3, delta0/(2c_*)),
 epsilon=q/A_sum^2, delta0=|F-H|/A_sum.               (SW12)

Proof: at a segment value f,
|grad_f(q/(|f|^2+q))|=2q|f|/(|f|^2+q)^2<=1/(2|f|).
Integration along the segment proves the last branch. Thus delta0<=2mu
gives w_T<=4mu for **every positive regulator**, including q>>A_sum^2.
The old min(1,Cmu epsilon) alone could saturate at1 and then leave
v_1,T of order L^2. Its failure is a weakness of that bound, not a
failed physical comparison. Retain the epsilon-small branch too: it
pays the large coefficients in regime B. All other FT5 formulas remain,
with this improved w_T; hence all v_m,T=O(mu L^2) without requiring
small epsilon. No multiple-root premise is imposed on the finite core.

In regime A use SW2 with the actual coefficient weights SW11.
For example the exterior time primitive is bounded by

    st_O[1]<=2v_0,O[1]+(A_eta+2^10u l^2)w_O[1]
                                                     +2z_0,O[1], (SW13)

and wt,ct have the exact FT10 analogues. This is O_eta(e u l^2+d),
which vanishes as u grows. There is no multiplication by an unbounded
global coefficient: each coefficient is local to the support being paid.

In regime B retain first the exact carrier-relative scale

    Lambda<=sqrt(Q_+) exp[u+32-beta(t)(u-8)^2/2].

For u sufficiently large and beta u>16 this gives

    Lambda<=sqrt(Q_+) exp(-2u).                       (SW14)

Indeed (u-8)^2>=u^2/2 eventually; the exponent is <=-3u+32<=-2u.
At the finite onset Lambda<=1/2. Use EB9's **individual** weighted
estimates with this upper scale. Its logarithmic factor is retained;
at the exponential upper scale |log Lambda_bar|<=2u. All coefficient
weights grow at most polynomially by SW7/SW9 and are paid by SW14.
On gap supports in B, q/A_sum^2 has the analogous exponential bound,
so the small-epsilon branch of SW12 and W,theta_reg factors remain.
Nothing is set to zero as the regulator shrinks.

## 4. One moving field and the complete switch ledger

Select an initial gap at t0=64 using the exact phase rule
n=ceil(Theta(64,U)/pi), Theta(64,X0)=npi, X0>=U. On all J set

    Theta(t,X(t))=npi, |X'|<=8, |X-X0|<=264.
    a_X=X0-300, L=log(2+X0+300), sigma=1/(64L),
    R_c=X0+300.                                      (SW15)

The speed is MW2's imaginary-part estimate, valid on the extended
field domain, not an inference from root speed. The phase inverse
continues inside the exterior branch through all J. Frozen width and
the close local-log ratio999/1000<=L_c/L<=1 give the same real-phase
floor c0=1/2 and analytic-collar margin>=1/(4L) on seam supports.
Core/band buffers and collars meeting a seam support fit |x|<=R_c,
|y|<=4. Pure exterior collars at arbitrary heights use their own local
u,l and the globally valid field strip; the close log ratio is claimed
only near a seam. Further free enlargement is horizontal; no source
accuracy is assumed above its stated transverse strip.

Use one source G and the same flat lambda(t,x) and F as MW6--MW10.
The exact moving terms remain

 E=lambda E_P+lambda_xD_z+lambda_xxD/4+lambda_tD,
 E_z=lambda(E_P)_z+lambda_xE_P/2+lambda_xD_zz
       +3lambda_xxD_z/4+lambda_xxxD/8
                                   +lambda_tD_z+lambda_xtD/2,
 B_t=lambda_x(-D_zz+E_P)/2+lambda_xtD/2,
 (B_z)_t=lambda_xx(-D_zz+E_P)/4
       +lambda_x(-D_zzz+(E_P)_z)/2
                               +lambda_xxtD/4+lambda_xtD_z/2,    (SW16)

where D=P-G and lambda_t=-sgn(x)X'lambda_x, with the corresponding
lambda_xt,lambda_xxt formulas. Keep the separate E_comp,E_sp,E_move
and their z derivatives of MW10; all are used in z_m and D_E.
The physical regulator is never altered by the moving field cutoff.

Take the explicit allowances

    mu_o=2^52/a_X^2, mu_s=a_X^-2, mu=mu_o+mu_s,
    d=d1=2^24/a_X^3, C0=1, C1=C2=C3=2.               (SW17)

The extended EF2 and EB4 dominate these inputs. EB13 plus MW's finite
moving increments give every field, compatibility and mixed-time ratio.
In GS14 retain k=2v+|r_t|w and the explicit |r_t|theta_reg b0^2.
On A use w<=1,theta_reg<=1/4; on B retain their actual exponential
upper bounds. Every r_t term in GS14 contains w or theta_reg.

Here is the new worst row explicitly. The ratio substitutions give

    pi |(T_C)_t|<=2^160 mu L^2(L^2+|r_t|).            (SW18)

The numerical slack covers all EB11 profile constants, V=8 and MW's
new first-time terms. In A, insert SW11 and multiply by band area
<=16sigma to obtain a bound <=C_eta mu u L^3. Since mu=O(a_X^-2)
on the joining bands and u is within a fixed amount of X0, this is
O_eta(L^3/a_X). In B all r_t factors retain w/theta_reg, so they are
polynomial times exp(-c u); the remaining compatibility row is
O(mu L^3). An independent constant bound on beta' would instead have
given mu X0^2 L^3, failing to vanish. SW8 is its actual payment.

All consumers are the same finite arithmetic ledger, with new inputs:

| Consumer | Switch-uniform payment |
| --- | --- |
| U,W, spatial jets through4 | raw core/gap/exterior sums, using SW12 and SW2/EB9 |
| direct Ut,Wt,Rt through2 | exact FT10/FT12 with full SW16 E and SW11 or weighted B coefficients |
| calC,calCt through2 | FT11/FT12 and GS13/GS14; SW18 pays compatibility time, retaining q_t and B_t |
| J through2, order3 internally | FT12's weak current identity, spatial TJ and full raw primitives |
| actual Q,Delta Q through2 | signed GS9 stress first, then EB18 actual filtered mean products |
| calB through2 | actual b_r times delta w, paid by SW11/SW13 or EB9 |
| actual calS through2 | direct Rt/J plus FT16 signed exterior D_E, full-gap D_E and band D_B |
| T_U through4 | Xi/2 and all three heat pieces, FT18, against zero for exact H |

Both -(calC)_t and -square calC/2, Delta Q, Delta calB and the
derivatives of the actual mean-gradient products remain in the density
equation. Kernel derivatives stop at 4 and source jets at 3. Equation
sums retain component sums, not an unjustified single-row target.

PE34 and EB12 at each fixed t pay the signed exterior heat correction.
Use SW2's z_m bounds with SW11 coefficients in A, and EB9's individual
weighted z_m bounds in B. The moving test eta_O retains both first
spatial commutators and eta_O,xx. No eta_O,t term is created by this
instantaneous spatial pairing, and no derivative of an auxiliary
truncated observable is taken. The complementary gap D_E includes E_P
on the shoulder and all SW16 motion. Splitting raw positive integrals
at the current collars/regions and in proof cases A/B adds no interface
flux because those decomposed bounds are never differentiated. Actual
F_t and calC_t already pay physical cutoff motion. Fixed observation
traces only are claimed.

On the pre-switch overlap [63,64], beta=0 and r_x=r_xx=0 exactly;
the time-only regulator floor and source comparison are the existing
fixed-floor route. The same G/P field and paid band jets continue
through 64 with the flat physical q. On [64,97] they are compared using
the same fields and exact q. Thus this is an actual overlap construction
with source-derived data, not an asserted limit from beta_min>0. No
new time blend or source change is required inside J. Its restriction
to [95,97] is a construction of the AN05 type with the newly chosen
source/phase index; it is not asserted identical to a separately chosen
earlier finite source.

## 5. Exact crossover centers are retained, not fitted

For the full saddle actually used here define

 b_s(t,u)=a(t)/2-beta(t)u^2/2-log A_s(t,u),
 b_s(t_cs(u),u)=0.                                  (SW19)

Retain this equation exactly whenever using a crossover coordinate.
The corresponding equation along the moving seam is b_s(t,X(t))=0.
Its derivative contains the motion term explicitly:

 d/dt b_s(t,X(t))=a'/2-beta'X^2/2-Re T
                         -[beta X+partial_x log A_s]X'. (SW20)

For sufficiently large initial X0 these equations have a unique root
in (64,65). Here is a direct finite argument: on that interval
beta'/beta>=1, since chi'/chi>=32 and kappa'/kappa<2.
The exact gamma formulas give Re T>log^2u/32 and
|partial_x log A_s|<=1 at the stated onset. Hence SW20 is negative
when log^2u>32(A_eta+16), since the beta terms are <=
-beta X^2/2+8beta X<0. SW3 gives a positive b_s at 64.
At 65, chi>=exp(-64)/2 and kappa<618 give beta(65)>exp(-80);
SW3 then gives negative b_s at 65 once X0 is sufficiently large.
The onset below exceeds these elementary requirements. The fixed-height
equation has the same argument without the motion term.

Note 28 JT26 instead uses the **earlier** carrier
mathcal G_t(w)=M(w)exp(t alpha(w)^2/4), and its exact equation is
b_Gamma(t,u)=log(epsilon_g/|mathcal G_t((1+iu)/2)|)=0.
That exact center and its stated normalized layer result are retained
at their original scope. It is not silently identified with SW19's
full-saddle center; a displacement comparison would require its own
bound. Neither center is evaluated, rounded or replaced by
64+64/log u or a finite inverse-log expansion here. The two-regime
proof estimates the actual functions for **all** times and therefore
already covers their thin crossover neighborhoods without a centering
error. No normalized layer profile is substituted for an absolute
potential/current/source/covariance error.

## 6. New mean cap, one source and an explicit vanishing budget

Recompute the common mean cap with the new physical floor; the old
[95,97] compact-floor proof is not reused. Set

 Q_eta=1+Q_++A_eta+|log eta|+eta^-2,
 R_*=ceil(2^2056 Q_eta),
 e_*=E_sw exp(-(R_*+8)^2/72), B1=(B0+B2)/2,
 C_Hsw=max(2^80,2^24[B1/e_*+(R_*+8)/18+1]).          (SW21)

B0,B2 are the same complete-source moment upper bounds at time 97.
On the fixed central rectangle the q floor and these moments bound
the actual H gradient. Outside it use the same integrable simple poles
and analytic units as EB16. In A, |r_x|integral w<=256; in B its
individual exponential bound pays the polynomial coefficient. Thus
|partial^gamma U_H|<=C_Hsw(1+log(2+|x|)),1<=|gamma|<=3.
On core/seam supports use the candidate common cap

    M_gamma=C_Hsw(1+log(2+R_c))+1,                   (SW22)

and local height on pure exterior supports. The auxiliary primitive
mean-error rows below justify this cap for F before its covariance
products are used.

With P2=B2+1 define finite constants and envelope

 C_sw=2^8192(1+C_Hsw+Q_eta+A_eta+P2)^64,
 B_sw(X0)=C_sw {L^8/a_X+(1+X0+300)^20 exp(-a_X)},
 a_X=X0-300, L=log(2+X0+300).                        (SW23)

Each nonsource column of the complete ledger is <=B_sw uniformly on
J and all heights. For a concrete coefficient count, regime A has
unweighted primitives bounded by the explicit SW2 constants; time
weights introduce at most u l^2, and SW18 is the worst gap-time row.
All remaining local products of field/profile/kernel constants and
finite Leibniz sums are <2^1024 times
(1+C_Hsw+Q_eta+A_eta+P2)^16. Thus the first term of SW23, with eight
logarithms rather than the sharper three in SW18, dominates every
1/u row and all smaller 1/u^2 or1/u^3 rows. In B the SW14 upper scale
has |log Lambda_bar|<=2u. EB9 then gives polynomial factors of degree
at most3 before the regulator weights; the global weights and their
products have degree at most4. Profile/test derivatives and the
remaining logarithms fit degree 20. Their exp(-2u) factors are bounded
by the displayed exp(-a_X) envelope after fixed local shifts. The
large numerical and coefficient powers in C_sw cover all these finite
products and replacements. For pure exterior supports take the
decreasing local-height supremum. Core-only supports have no nonsource
column. No chart count or time width multiplies this bound.

Take the new core e_c=E_sw exp(-R_c^2/72), SW9 coefficients at R_c
and SW22 common caps in Note 47's explicit D_r core table. Include the
auxiliary D_gamma=k_gamma rows. For a requested scalar target
0<theta<=1 choose

 rho_*=min(theta/4,B_sw(X0)), A_min=exp(-X0-320),
 epsilon_core=e_c^2 min_(D_r>0) rho_* /(4D_r),
 0<epsilon<=min(1,epsilon_core,mu_s A_min).            (SW24)

SW3's full-buffer armwise lower bound gives this conservative moving-band
carrier minimum, including the transverse source buffer. FI18--FI20
with the same time97 majorants produce **one** nonnegative clipped
rational-cubic source and its exact-heat G for all J. Their jet-error
proof used only exp(tu^2)<=exp(97u^2), not t>=95, so the literal
constructor gives the same 29epsilon/64 bound here. Its separate complete
interpolation, omitted values/slopes, nodal arithmetic, construction and
tail allowances are all retained. It pays every core and moving-gap
jet row. Refinement is simultaneous with X0, so the core column is
<=rho_*<=B_sw; it is not left at a constant quarter-target in the limit.

One sufficient finite onset is

 m=max{16384+ceil(log2(R_*+1024))
                         +ceil(8log2(2+C_sw/theta)),
       ceil(16sqrt(A_eta+16)),
       ceil(log2[4exp(80)(1+A_eta)+1024])},
 U=2^m, then select X0 by the phase equation at 64.    (SW25)

Ceilings may use certified integer upper bounds with extra units.
No special-function or theta sampling is required. Then a_X>=2^(m-1),
L<=m+3, C_sw<=theta2^(m/8), (m+3)^8<=2^(m/2), and
exp(-a_X)<=X0^-64. These elementary monotone inequalities show
B_sw<theta/4 and pay every field/collar/mu/exponential gate. The second
and third gates explicitly give log^2(X0-264)>32(A_eta+16) and
X0-264>4exp(80)(1+A_eta), respectively, paying Section 5's center
requirements independently of the coarse constant envelope. The two nonsource columns and the
core column consequently yield, for every listed scalar component,

 sup_(t in [63,97], x in R, |y|<=1) error_r
                     <=3B_sw(X0)<=3theta/4.           (SW26)

Verify the auxiliary k_gamma s<1 rows first using only primitives;
they contain no common mean cap. They establish SW22 for F, after
which the covariance D_r coefficients apply. Thus the construction
is noncircular. B_sw=O_eta(log^8 X0/X0) tends to zero, with the
source chosen by SW24 for each X0. A future arithmetic/filter procedure
has the remaining quarter-target, not an already executed certificate.

## 7. Scope, controls and disposition

The quantitative gain is one fixed interval **[63,97] across 64 and
overlapping the prior [95,97]**, at every real height, in physical
absolute units for the complete tuple. Strict-after-switch Gaussian
suppression is replaced by SW8 and the arbitrary-q relative weight
branch in the crossover regime. No singular estimate remained unpaid
after this focused attempt. Affordable source construction and an
efficient evaluation/filtering prescription remain unproved.

For any fixed compact positive-time interval with lower endpoint >=32,
the same structural argument uses Notes 30--31's compact outer inputs,
the exact flatness inequality and one moving gap/source on its union
buffer. Constants, source moments and finite onsets depend on that
interval; the fully instantiated table here is for [63,97]. The all-time
objective still requires the remaining finite-time cover and paid joins
to the negative Gaussian endpoint of Note 26 and all-height positive
endpoint of Note 31. Those time blends must retain the actual fields,
B,E and their mixed derivatives, component/join heat, both curvature
rows and actual covariance. A small residual does not propagate error
without an additional proved stability theorem. No such propagation
or all-time conclusion is asserted here.

The official [DLMF complex gamma remainder](https://dlmf.nist.gov/5.11#ii),
[local inversion theorem](https://dlmf.nist.gov/1.10#vii) and
[Cauchy derivative formula](https://dlmf.nist.gov/1.9.E31) were rechecked.
The new switch, weight and time estimates are derived directly from
their exact inputs. Main-assistant and three read-only same-model
derivations/audits share premises and are not specialist independence.

No numerical, exact-rational or machine-symbolic research execution,
theta/source/gamma/field sampling, mesh/precision search or interval
campaign occurred; none is authorized by r1. Earlier algebraic checks
are reused by reference. Hash/size/link checks are housekeeping only.
No previous source-note or manuscript edit, snapshot, commit, new chat
or model change. This does not certify source arithmetic/filtering.

Collision controls retain their same source/completion failures:
Euler factors lack the unchanged canonical completion; weighted-square/
finite-prime controls lack its full coefficients/reflection input;
reflected and positive-primitive controls lack the canonical gamma/source
identity; atomic and polynomial heat controls lack the smooth theta
source. They can satisfy the generic transfer and collide. A transition
covering a zero fails the chosen gap floor; another gap is no collision
exclusion. No RH, global simplicity or universal cost claim follows.

**Disposition:** AN06 r1 and HDA-24 complete at this switch-interval
analytical scope. HDA-17 remains Partial, HDA-18 Gated and HDA-20
unfulfilled. The all-height/all-real-time analytic objective and both
infinite-time limits remain. Next **Analysis — Sol**: a bounded parent
endpoint/finite-time joining contract, using this central [63,97] input
and Notes 26/31; HDA-23's improved conditioning remains ready and is
separate from completing the domain cover.

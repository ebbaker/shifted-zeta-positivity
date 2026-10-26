# R05-AN05: explicit uniform calibration and an all-height onset

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual effort ultra**.
Recurrence chat0003, thread `01a176ea-3f14-7972-bc9c-9aeb6fb50fd4`, turn
`01a1771c-0bf2-7c30-b2b5-a871a82750d5`.

**Return to HDA-R05-AN05 r1. Proved in-note from named inputs;
same-model internal assessment only.** All uniform calibration data left
symbolic in [Note10][n10] are instantiated below. For each fixed buffered
chart let

    R=r+1, Y=b+1, W=R+Y, d=ceil(W), n_*=d+1,
    L_*=2^22 n_*^4, X_*=2^(2L_*+8).                         (U1)

Every accepted exact-input center of [Note09 P1][n9] with X>=X_* meets
the uniform domains, structural gates and half-target truncation gates.
The sharper sufficient condition L=log(X/(4pi))>=L_*
may instead be used. With Notes09--10's certified finite algorithms and error
allocations this gives total outer-envelope (3,1) error <=exp(-L²/4).
This is a chart-dependent explicit sufficient height, not a useful-runtime
claim. It does not include excluded descriptor-boundary centers or supply
uniform center separation. The physical radii r=ell+2,b=1+h_av+2 retain
their averaging/regulator dependence through d; no limit in those radii
or in T is taken.

There is no numerical campaign, machine-symbolic verification, executable
evaluator or software certificate in this return. [Review09][review],
[inputs][inputs], [work record][work] and [Source Audit05][sources] record
the evidence and limits. AN05 r1 is **CLOSED at its bounded analytical
scope**. Broad R05 remains **Partial** at implementation/certification.

## 1. Definitions and explicit record

Keep h(T,z)=H(-T,z), h_T=h_zz, H(0,z)=xi((1+iz)/2)/8 and the complete
canonical theta source. Write

    w_±(z)=(1±iz)/2, t_±(z)=w_±(z)/2,
    M(w)=w(w-1)pi^(-w/2)Gamma(w/2)/16,
    ell_±(z)=log M(w_±(z)),
    G(z)=exp((ell_+(z)+ell_-(z))/2), g=G(X)>0.               (U2)

Fix conjugate analytic logarithms at the real center and continue on the
stated disks; no zero or pole is met there. G is exactly the existing
canonical branch, not its Stirling approximation. Freeze X, all floors,
coefficients, real partitions and descriptors under z,T differentiation.
Keep p=floor(L/2),K=2p,N=floor(sqrt(X/(4pi))),V=8sqrt(2)L,1<=T<=2,
both arms, all n<=N, every real RS coefficient through K and exact cutoff
transfer, and the retained bounded real RS integral. The full buffered
rectangle is |Re z-X|<=R, |Im z|<=Y.

The following rational record suffices. M_H^* denotes an upper bound on
the actual mass M_H, not its exact value.

| Datum | Value | Uniform assertion and domain |
| --- | --- | --- |
| H,A,D | 1,1,4 | sup on \|z-X\|<=X/4 of \|ell_±''(z)\|<=1/X, X>=32; all-order Cauchy coefficients follow |
| D0 | 3 | \|ell_±'(X)-(-pi/8±iL/4)\|<=3/X, X>=32 |
| C_Gamma | 1 | G(X+q)<=g exp(\|q\|), real \|q\|<=X/2, X>=64 |
| g_- | 1/64 | g>=X^(7/4)exp(-pi X/8)/64, X>=32 |
| C_H | 1/4 | \|H(0,u)\|<=(1/4)(1+\|u\|)^4 exp(-pi\|u\|/8), all real u |
| C_tail | 640 | \|H(0,X+q)\|/g<=640 X^(9/4)exp(-pi q/8), X>=32, real \|q\|<=X/2 |
| M_H^* | 1/4 | M_H=int_0^infinity \|Phi(v)\|dv<=1/4 |
| C_chi | 3^d | max(g/\|G(z)\|,\|G(z)\|/g)<=3^d on the full buffered rectangle, X>=max(64,4W) |
| c_o | 1 | E_o(-T,z)>=\|G(z)\|exp(-TL²/16+pi²T/64), on that rectangle under U12 |
| C_cal | 32+d | Relative amplitude calibration bound in U12; its gate is C_cal(1+L)/X<=1 |
| X_cl | 64(d+1) | Common center onset covering every classical domain above and U10--12 |

The remaining gates involving V,p and quadrature geometry are paid by
U1, not by X_cl alone. No unquantified large-height assertion is used as
an input to U1. The quoted real RS remainder in [Note05][n5] holds at
every positive real argument and positive integer K; it contributes no
additional unknown K-dependent onset.

## 2. Complex-disk gamma estimate and all-order coefficient bound

The checked [DLMF5.11.2][psi] and [5.11(ii)][sector] give, after the
1/(2t) term,

    psi(t)=Log t-1/(2t)+E(t),
    |E(t)|<=sec(arg(t)/2)^3/(12|t|²), |arg t|<pi.            (U3)

On the larger disk |z-X|<=X/2, |t_±|>=X/8 and |arg t_±|<3pi/4.
Using sec(3pi/8)<3 gives |E|<=144/X². Each point of the inner disk
|z-X|<=X/4 has a t-disk of radius X/16 in this larger region, so Cauchy
gives |E'(t)|<=2304/X³ there. Also |t|>=3X/16 and
|w|,|w-1|>=3X/8. The exact identity

    ell_±''=1/(4w²)+1/(4(w-1)²)-psi'(t)/16

therefore implies

    |ell_±''|<=1/(3X)+40/(9X²)+144/X³<=1/X, X>=32.          (U4)

Indeed after multiplication by X the bound at 32 is 353/576<1 and
it decreases thereafter. This proves the complex-disk premise before
using it. Cauchy applied to ell'' at X yields, simultaneously for k>=1,

    |ell_±^(k+1)(X)/(k+1)!|
      <=4^(k-1) X^-k/[k(k+1)]<=A D^(k-1)X^-k, A=1,D=4.     (U5)

Real-axis gamma samples would not prove U4 or U5. No fixed-order
asymptotic constant is absorbed while k grows.

For real X, t=(1+iX)/4 has |arg t|<pi/2. U3 gives |E(t)|<=4/X².
Using Log t=log(X/4)+i pi/2+Log(1-i/X), direct differentiation gives

    ell_+'(X)=-pi/8+iL/4+delta(X),
    delta=2X/(1+X²)+(i/4)Log(1-i/X)-i/(8t)+(i/4)E(t).

The power series bound |Log(1-v)|<=|v|/(1-|v|) implies

    |delta|<=2/X+1/[4(X-1)]+1/(2X)+1/X²<3/X, X>=32.        (U6)

Reflection gives the minus arm. Along the real line (log G)' is real
and has modulus <=pi/8+3/u<1 for u>=32. Integration along
[X,X+q] proves the C_Gamma=1 assertion whenever X>=64, |q|<=X/2.

To obtain the lower gamma scale, [DLMF5.11.1][stirling] and its first
omitted-term remainder give |R_Gamma(t)|<=2/(3X) for real X>=32.
Taking absolute values in the exact Stirling formula gives

    G(X)=(pi^(1/4)/32)(1+X²)^(7/8)e^(-pi X/8)
       *exp{(X/4)atan(1/X)-1/4+Re R_Gamma(t)}.              (U7)

The last exponent is >=-1/4-2/(3X)>-1/2. Since exp(-1/2)>1/2,
pi^(1/4)>1 and (1+X²)^(7/8)>=X^(7/4), U7 proves g_-=1/64.

Finally let a=|z-X|<=W<=X/4 on the buffered rectangle. The analytic
log G has |(log G)''|<=1/X by U4, and its derivative at X has modulus
<=pi/8+3/X. For X>=64, |(log G)'(z)|<1 along every segment from X.
Thus |log G(z)-log g|<=W, proving both ratios <=exp(W)<=3^d.
This supplies C_chi on the complex chart and its unit buffers.

## 3. Complete-source moderate and remote constants

Here the variable v is the source integration variable and u is the
real height. For t real, the checked [beta integral][beta] gives

    |Gamma(1/4+it)/Gamma(1/2+it)|<=Gamma(1/4)/Gamma(1/2).

Combine this with [DLMF5.4.4][half] and Gamma(1/4)<4+exp(-1)<5,
obtained by splitting its positive integral at 1. It follows that

    |Gamma(1/4+it)|<=Gamma(1/4)/sqrt(cosh(pi t))
                         <8 exp(-pi|t|/2).

The checked finite-sum representation [DLMF25.2.8][zeta], at N=1,
Re s=1/2, reads

    zeta(s)=s/(s-1)-s int_1^infinity {x}x^(-s-1)dx.

For s=(1+iu)/2 this gives |zeta(s)|<=1+2|s|<=2(1+|u|).
Since |s(s-1)|=(1+u²)/4 and pi^-1/4<1,
|M(s)|<=(1+u²)exp(-pi|u|/8)/8. Multiplying proves C_H=1/4
in the table, including u=0. The existing identity H(0,u)=M(s)zeta(s)
retains its exact normalization.

The canonical source is

    Phi(v)=sum_(m>=1) (2pi² m^4 e^(9v)-3pi m² e^(5v))
                         *exp(-pi m² e^(4v)), v>=0.

Every summand is positive because 2pi m² exp(4v)>3. Absolute
integrability and the canonical cosine representation are unchanged.
Consequently

    M_H=int |Phi|=int Phi=H(0,0)<=1/4.                       (U8)

This estimates the full source, without cutting off its m-sum. For
X>=32 and |q|<=X/2, 1+X+q<=(5/2)X; C_H(5/2)^4=625/64<10.
Divide the height-sensitive source bound by U7 to obtain C_tail=10/g_-=640.
In Note05 G18 and Note04 R3.16 one may therefore use exactly

    A_mod^theta=640 max(D_0^theta,(D_0^theta)^t),
    A_far=16 max(J_0,J_0^t), theta=1/2.                     (U9)

The superscript labels theta; it is not exponentiation. Moderate tails
retain their real height exponential and X^(9/4); only remote data use
M_H^*. No arithmetic population or transfer contribution is removed.

## 4. Actual outer envelope and calibration remainder

Put L_z=Log(z/(4pi)), on the branch continued from positive real height,
and define the elementary gamma carrier and phase

    G_0(z)=(pi^(1/4)/32) z^(7/4) exp(-pi z/8),
    theta_0(z)=z(L_z-1)/4+7pi/8.

For |Re z-X|<=R, |Im z|<=Y, X>=max(16,2(W+2)), the sectorial
log-gamma formula gives the exact decomposition

    ell_±(z)=log G_0(z)±i theta_0(z)+delta_±(z),
    |delta_±(z)|<=8/|z|<=16/X.                             (U10)

For clarity a quantitative derivation for the plus arm is

    delta_+=Log(1+z^-2)+(iz-1)Log(1-i/z)/4-1/4+R_Gamma(t_+).

In this domain |z|>=8, |arg t_+|<3pi/4 and
|R_Gamma(t_+)|<=16/(3|z|). With v=-i/z, the middle two terms equal
(iz/4)(Log(1+v)-v)-Log(1+v)/4. Their moduli are at most
1/(4|z|) and 1/(2|z|); the first log is at most 1/|z|.
The sum is <8/|z|. Reflection proves the minus arm. Branch constants
are fixed at positive real z, so no integer phase error enters U10.
Averaging gives |log(G/G_0)|<=16/X.

Use precisely the original outer arms

    A_o(-T,z)=2G_0(z) exp(-T L_z²/16+pi²T/64),
    C_±=A_o exp(±iTheta_o)/2, E_o=|C_+|+|C_-|.

The exact phase Theta_o is the source definition; its value is not needed
for this lower bound. AM-GM gives E_o>=|A_o|, including the transverse
cosh growth of the actual envelope. It is not asserted that E_o is
asymptotic to |A_o| off the real axis.

Since |z-X|<=W and X>=2(W+2),

    |L_z-L|<=2W/X,
    |L_z²-L²|<=4W(1+L)/X, L>=0.

Together with U10 and 1<=T<=2, this proves

    | log( |A_o|/[2|G(z)| exp(-TL²/16+pi²T/64)] ) |
                     <=(16+W/2)(1+L)/X
                     <=(C_cal/2)(1+L)/X, C_cal=32+d.       (U11)

Thus if X>=X_cl=64(d+1), L>=0 and C_cal(1+L)/X<=1, then

    E_o>=2exp(-1/2)|G(z)|exp(-TL²/16+pi²T/64)
         >=|G(z)|exp(-TL²/16+pi²T/64),
    | |A_o|/[2|G(z)|exp(-TL²/16+pi²T/64)]-1 |
         <=C_cal(1+L)/X.                                  (U12)

For the second assertion use |exp(t)-1|<=2|t| for |t|<=1/2.
These specify the previously unnamed calibration remainder and prove
c_o=1 with its actual domain. The complex gamma carrier calibration in
U10 is also bounded by C_cal(1+L)/X. The center onset X_cl covers real
u>=32 on the entire |u-X|<=X/2 window, the full X/4 gamma disk and
the enlarged buffered chart; it is not an argument threshold mistaken
for a center threshold.

## 5. Instantiation of the all-height bound

It remains to bound the constants in Note10 C20--21 rather than checking
one sampled height. In this section n_* in U1 is an auxiliary chart
integer, unrelated to the arithmetic mode, source index or Gauss order.
Since r,b>0, d>=3,n_*>=4. Introduce the rational majorants

    Ebar=3^(8n_*²), Sbar=32n_*,
    Qbar=32Sbar²=2^15 n_*², Tbar=Ebar Sbar².                (U13)

They cover both E,S in Note05 G10 and E_theta,S_theta in G19 at
c=1/2,theta=1/2,delta=1/4, with C=max(1,A,D)=4. To check this explicitly,
t_R=1+R/4<=n_*/2. The largest new exponent obeys
Y²/4+8t_R²<=9n_*²/4. The other exponents are <=d+d²/4+4 or d²/4;
exp(1)<3 and sqrt8<3 therefore put all prefactors/exponentials below
Ebar. Sbar dominates W+4,16sqrt2 and 4sqrt8. The actual RS constants
in G12 satisfy Q_R<64 and C_R<32, so G13's Q,T_0 for both moment
systems can be bounded above by Qbar,Tbar.

There is no loss of the factorial/order dependence: retain

    Jbar(p)=Tbar(p+2)Qbar^(p+1)(2p+4)!.

The same G14 proof then gives log Jbar(p)<=Cbar_*(p+1)log(p+2), with
Cbar_*=6+log Qbar+log Tbar. Elementary bounds log3<2,log2<1,
log n_*<=n_* give

    log Tbar<=18n_*², log Qbar<=2n_*²,
    max(C_*,C_*theta,1)<=32n_*².                            (U14)

For the fixed moment factors, M_0<=Ebar,M_0^t<=Tbar follow from G10's
explicit moments, using M_2<=2Ebar Sbar² and
M_0^t=M_0/2+M_2/4. The same calculation from the explicit G16 moments
gives D_0^theta,(D_0^theta)^t<=Tbar. Note04's remote moments at tau=1,B=2
satisfy

    J_m<=2 exp(Y²/4)m!(Y+4)^m,

by Gamma((k+1)/2)/sqrt(pi)<=k!, the binomial formula, and
(8B)^((k+1)/2)=4^(k+1). Hence J_0,J_0^t<=Tbar as well.
Since C_pop=4(4pi)^(-1/4)<4 and exp(1)<3, the actual C_Q in G14 obeys

    C_Q<=48Ebar+Tbar+588<=3Tbar,
    A_mod^theta<=640Tbar, A_far<=16Tbar.                    (U15)

In C20 take Co=C_chi/c_o=3^d. Each fixed multiplier in its five
logarithmic costs is bounded by 2^18: 8*3,392*C_pop,392*640,392*16
all satisfy this. Thus with S,M exactly as in C20, U14--15 imply

    S<=32n_*²,
    M<=log(Co)+log(Tbar)+18<=18n_*²+2n_*+18<=32n_*²,
    L_rate=max(16,(32S)²,sqrt(32M))<=2^20 n_*^4.             (U16)

Every other term of C21 also lies below U1's L_*:
(2R+W+1)/8, log(1+4(W+1)), 2log25, 2log4,
2log(33+d), and log(1+64n_*/(4pi)). For example each variable logarithm
is bounded by its argument, which is at most a fixed multiple of n_*;
L_*>=2^22 n_*^4 has ample slack for n_*>=4. This proves L>=L_*
implies C21 with actual constants, not unspecified calibration data.

For completeness the all-height mechanism is the following. For every
L>=16 and p=floor(L/2),

    (p+1)log(p+2)<=L log(L+2)<=L^(3/2),
    (p+3/4)log X-3L²/8>=L²/8-L/4>=7L²/64.

C20 gives M+S L^(3/2)<=L²/16, strictly below this local rate gap.
The moderate/artificial log costs in C19 also fit their 61L²/8 margins.
For the remote test, pi X/8<=X²/512 and
X²/512>=9L²/8>(3/8+1/32)L². These dominate every actual factorial/moment
cost continuously in L; no monotonicity of Q_p at a floor jump is used.

Note10 C18 pays the full ellipse/window/retained-order gates for L>=16;
C21 pays the buffer gates, 2AV²/X<=1, slope and separate damping tests,
DV/X<=1/2 and C_cal(1+L)/X<=1. U12 covers every remaining classical
domain. Thus C19's factors 8,392 retain the half-target reservation.
Finally log2>1/2 and log(4pi)<3 show

    log(X_*/(4pi))=(2L_*+8)log2-log(4pi)>L_*+1.              (U17)

This is an explicit dyadic center threshold using integer operations
and a binary-exponent expression; its enormous bit string is not
materialized. Every larger **accepted P1 center** has L>=L_*, including
all later p and N jumps. A center exactly on an excluded descriptor
boundary is not newly included; no uniform lower bound on its strict
separation sigma follows. The rational guard-strip edge procedure and
all paid endpoint errors remain those of Note09.

## 6. Composed accuracy, work and storage after calibration

The record uses rational integers, so the comparable dyadic budget of
Notes06/09 can now be chosen with c_-=1,C_+=3^d, with no external
calibration oracle. For example retain Note09's prescribed dyadic e in

    (1/(8*3^d))exp(-3L²/8)<e<(1/(4*3^d))exp(-3L²/8).

Keep its actual factor-controlled allocations, all five delivered-error
categories and scale payment. Replacing each symbolic valid calibration
by the proved U2--12 record makes Note10's composition applicable.
The total outer error, after half-target truncation and all evaluation
payments, is <=exp(-L²/4) for U1's accepted centers, on the full buffered
field comparison and the requested spatial orders 0--3 plus first time.
The exact frozen-model residual remains zero; a computed residual is a
separate paid channel, and its z derivative still needs the mixed T,z
channel. No uncomputed derivative is certified by this statement.

For fixed r,b, Note10's sufficient delivered tolerance size remains
P=3L²/(8log2)+O_(r,b)(L log L). Its work/storage theorem now has an
effective chart-dependent constant C(r,b), obtained by substituting this
explicit record and the U13 moment bounds in its finite algorithms:

    Q=2+B+P+s_sigma+ceil(L)²,
    T_bit<=C(r,b)(N+1)Q^40, M_bits<=C(r,b)Q^20.             (U18)

This is a computable constant from specified arithmetic recipes, not a
numerically optimized operation count. All n<=N must still be processed;
streaming avoids retaining them all at once. The chart-dependent rational
calibration record itself has O(d) bits under ordinary binary encoding
(C_chi=3^d dominates); Ebar,Tbar, if materialized for the majorant route,
have O(n_*²) bits. L_* and the onset exponent 2L_*+8 have O(log n_*)
bits; expanding X_* would instead take 2L_*+9 bits. These are distinct
encodings and should not be confused. The accepted dyadic X and exact
query still contribute their actual B. Center separation s_sigma remains
nonuniform. No single C uniform over unbounded chart radii is claimed;
a variable-chart bound must count that record and the actual moment and
conditioning data. No practical height, measured cost, implementation or
uncompressed-to-polynomial-in-L improvement follows.

## 7. Disposition and controls

**Analysis — Sol:** accept U1--18 at their stated scopes. AN05 r1
**CLOSED**, requested uniform calibration/onset audit **Complete**;
broad R05 **Partial** at concrete evaluator implementation and required
certification. Same-model read-only cross-checks of gamma, source/outer
calibration and onset arithmetic are internal checks, not independent
specialist review. Notes09--11 have not been integrated into the manuscript.
R04/R06 NOT_STARTED; HDA-A02 Partial, HDA-17 Partial, HDA-18 Gated,
HDA-20 unfulfilled remain unchanged.

This is a finite-evaluation and sufficient-onset milestone under
[avoid01][a1], not a new RH criterion. The [result index][results],
[heat cluster][heat], [avoid index][avoid], [shared-premise caution][a5]
and [separate-bound pattern][a12] remain governing context. Collision
controls in [controls12][controls] have no complete canonical theta/xi
source, exact all-mode RS initial matching or certified source-tail
premise; shape or heat recurrence alone supplies none of these. This
calibration argument cannot be applied to those controls by retaining
only their heat equation. No RH, physical-transfer, joint-time or
regulator-uniform consequence is claimed.

Next concrete deliverable: **Numerics — Sol**, a bounded standalone
implementation/replay of the scalar/gamma and Gauss providers, before
an end-to-end field evaluator. [HDA-R05-N01 r1][next] declares finite
cases, tolerances and stop limits; it does not authorize a sweep to U1's
enormous onset. This is the first software dependency now that the
analytical calibration record is available.

[n10]: 10_EFFICIENT_PROVIDERS_AND_TOTAL_COST_20261026.md
[n9]: 09_FINITE_PROVIDER_ALGORITHMS_20261026.md
[n5]: 05_CONTROLLED_ORDER_GROWTH_AUDIT_20261026.md
[review]: ../reviews/09_EXPLICIT_CALIBRATION_ASSESSMENT_20261026.md
[inputs]: 11_EXPLICIT_CALIBRATION_INPUTS_20261026.json
[work]: 11_EXPLICIT_CALIBRATION_WORK_RECORD_20261026.json
[sources]: ../references/05_EXPLICIT_CALIBRATION_SOURCE_AUDIT_20261026.md
[next]: ../research-progress/handoffs/HDA-R05-N01.md
[psi]: https://dlmf.nist.gov/5.11.E2
[stirling]: https://dlmf.nist.gov/5.11.E1
[sector]: https://dlmf.nist.gov/5.11#ii
[beta]: https://dlmf.nist.gov/5.12.E1
[half]: https://dlmf.nist.gov/5.4.E4
[zeta]: https://dlmf.nist.gov/25.2.E8
[results]: ../../../../../result-summaries/README.md
[heat]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a1]: ../../../../../avoid/01_restating_the_target.md
[a5]: ../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md

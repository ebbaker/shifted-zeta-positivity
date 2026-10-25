# Moving-gap assembly on a fixed time interval

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. **gpt-6.1-sol (Codex), actual effort ultra**,
verified from the current turn's metadata. Chat **0017**, thread
`01a173e5-dc96-7c31-946c-be54c871244c`.

**Status: fixed-width all-height analytical comparison proved in-note;
same-model internal review only.** This returns
[HDA-18-AN05 r1 / HDA-22](../research-progress/handoffs/HDA-18-AN05.md),
consuming the actual finite constants in
[Note 47](47_EFFECTIVE_COLLARS_AND_COMPLETE_BUDGET_20261025.md).
The observation domain is **all real x, |y|<=1, 95<=t<=97**. The time
width is independent of the joining height. One moving model gap and
one fixed positive source per construction give the complete Note 43
tuple with a uniform error tending to zero as the initial joining height
tends to infinity, with source accuracy tightened as specified below.
No numerical source/evaluator is executed or shown affordable.
HDA-17 remains Partial, HDA-18 Gated and HDA-20 unfulfilled.

Read the [result index](../../../../result-summaries/README.md),
[heat-flow cluster](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
[collision controls](../../../../result-summaries/12_collision_controls_and_screening.md)
and [avoid index](../../../../avoid/README.md), especially
[classification](../../../../avoid/01_restating_the_target.md),
[scope](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[cancellation](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md),
[numerical scope](../../../../avoid/10_numerics_ahead_of_the_question.md)
and [status maintenance](../../../../avoid/19_status_files_that_lag_the_findings.md).
This is quantitative approximation, not an RH criterion. The
[intake manifest](48_FIXED_WIDTH_ASSEMBLY_INPUTS_20261025.json) pins the
frozen request and inputs; [Review 30](../reviews/30_FIXED_WIDTH_MOVING_GAP_ASSESSMENT_20261025.md)
records the internal assessment. Earlier source notes and manuscript are
unchanged.

## 1. Statement and preserved physical contract

Keep canonical H, H_t=-H_zz, H(0,z)=xi((1+iz)/2)/8, the unchanged
physical q=epsilon_g^2 with any fixed eta>0, full gamma-saddle P and its
specified branches, K=k_1 k_1, unnormalized potential and actual Q.
Use Y_b=4 and Note 45's full |Im z|<=5 analytic buffer. For every
0<theta<=1 the explicit onset below selects an initial model gap X0.
For every sufficiently large such phase gap, one source G=G_(X0,theta)
and one field F on all of J=[95,97] satisfy all the following absolute
component comparisons against H uniformly in real x and |y|<=1:

| Rows | Spatial orders |
| --- | --- |
| U,W | <=4 |
| R, calC, J, Q, calB | <=2 |
| U_t,W_t,R_t,calC_t, actual calS | <=2 |
| T_U, the joined model's heat-potential correction | <=4, against zero for H |

Third current derivatives are also paid internally to obtain second
source derivatives. Both calC_t and square calC, Delta Q, Delta calB,
and the derivatives of the actual mean-gradient products retain the
component sums in their equations. Equation sums need not have the same
theta as a single component. Fixed boundary traces inherit only the
available orders. All time derivatives are at fixed physical x,y;
no moving observation domain or moving-filter trace is claimed.

With a=X0-24, L=log(2+X0+24), define the finite envelope in Section 6
as B_mov(X0). The source demand in Section 5 makes each displayed scalar
analytical error <=3B_mov(X0), with B_mov tending to zero. At the
declared onset B_mov<=theta/4, so each analytical allowance is
<=3theta/4; theta/4 is reserved for a future executed arithmetic/filter
procedure. That reserve is not a numerical certificate.

This is a family of finite sources G_(X0,theta), each fixed in t and z
throughout J. It does not assert that a single fixed finite source works
as X0 tends to infinity or at all real heights without the P exterior.

## 2. A phase gap followed for all of [95,97]

Select X0 at t=96 by Note 47 EB2: for a declared large U,
n=ceil(Theta(96,U)/pi) and Theta(96,X0)=npi, X0>=U.
The phase uses the same continuous compatible carrier logarithms.
Define throughout J

    Theta(t,X(t))=npi, X(96)=X0.                       (MW1)

The bounded velocity of adjacent *roots* does not by itself establish
the velocity of this gap. The needed cancellation follows from FI4.
For the positive arm on real x write T=(log S_t)_t, exactly

    T=alpha^2/4+alpha'/(4B)+t alpha alpha''/(8B^2).

EF3/EF5 give |Im alpha|<1, |Re alpha|<=log(x)/2+4/x,
|alpha'|<=2/x, |alpha''|<=8/x^2, |B|>=1/2 and |alpha|<=log(x)/2+2.
Thus

    |Theta_t|=|Im T|<=log(x)/4+3/x+388|alpha|/x^2
                     <=L_x/2,
    Theta_x>=L_x/8, L_x=log(2+x).                     (MW2)

The imaginary part of alpha^2, rather than its absolute magnitude,
removes the otherwise artificial O(L_x) velocity loss. In particular

    X'=-Theta_t/Theta_x, |X'|<=8,
    |X(t)-X0|<=8 on J.                                (MW3)

The speed bound 8 is deliberately conservative. The inverse exists
locally because Theta_x>0. Any maximal continuation stays inside the
compact exterior interval [X0-8,X0+8], away from its branch/onset
boundary when X0>=2^2050+32. It therefore continues to both endpoints
95 and 97, uniquely. This proves an actual fixed-width construction,
not just a cover by shrinking AN04 slabs.

Freeze the width at

    sigma=1/(64L), L=log(2+X0+24).                     (MW4)

L bounds every local logarithm in the moving band buffer. For root
centers in these buffers, 999/1000<=L_c/L<=1, since their heights differ
from X0+24 by only a fixed bounded amount at this enormous onset.
Because the center phase in MW1 is exact,
there is no tau*Theta_t phase-drift term. On
||x|-X(t)|<=2sigma, |y|<=4, EB1's spatial and transverse estimates give
|Re Theta(t,|x|+iy)-npi|<1/8. The imaginary phase need not be small;
|cos Theta|/cosh(Im Theta)>=|cos(Re Theta)| supplies the field floor.
Thus c0=1/2 and c_*=1/4 remain
valid. Nearest model roots are at distance >=5/(2L) from the center;
their larger analytic disks leave a margin >=1/(4L) from Sigma+.
All EB1--EB9 slope/unit/pole and edge-collar bounds hold uniformly in t.
The joining heights stay in [X0-8,X0+8]; all full core/band/collar buffers
fit the union rectangle

    J x {|Re z|<=R_c=X0+24, |Im z|<=4},                (MW5)

with the existing open analytic enlargement for P and H. The source-jet
bound in FI18 is valid on every real x, so further horizontal analytic
enlargement does not cost a source error factor. All source-using kernel
supports and needed collar disks are inside |y|<=4; G is entire. At a
closed band edge, an open accuracy neighborhood is available by continuity
and the strict 29/64 source-error slack. FI18 is not applied at |y|=4.5.

For the chosen width the scale derivative is exactly sigma'=0. Only
first time derivatives of the cutoff occur in the tuple. No X'' or
lambda_tt estimate is assumed or needed. Changing velocity does not
create an unlisted term: the exact first-time formulas below contain
X'(t) at its actual value, and no second time row is asserted.

## 3. Exact new terms and finite ratio allowances

Use FI9's one fixed flat profile b_*. Define the even moving cutoff

    lambda(t,x)=b_*((|x|-X(t)+sigma/2)/sigma).

Its support conventions are the same as FI10: it transitions strictly
inside Sigma, and is constant near band edges and near x=0. In each
band put v_b=sgn(x)X'(t). The exact derivative identities are

    lambda_t=-v_b lambda_x,
    lambda_xt=-v_b lambda_xx,
    lambda_xxt=-v_b lambda_xxx.                        (MW6)

They vanish off the bands. Their norms are bounded by V l1,V l2,V l3
with V=8 and l_j<=2^(12j)L^j for j=1,2,3, as in EB11.
The sign accounts for the reflected band's opposite spatial derivative.

Let D=P-G only where P is used, and set F=G inside, F=G+lambda D on
the bands, and F=P outside. One G is fixed on all of J. Write
E_P=P_t+P_zz. Then, exactly,

    B=F_bar_z=lambda_x D/2,
    E=F_t+F_zz=lambda E_P+lambda_x D_z+lambda_xx D/4
                                                   +lambda_t D,  (MW7)

    E_z=lambda(E_P)_z+lambda_x E_P/2
       +lambda_x D_zz+3lambda_xx D_z/4+lambda_xxx D/8
                               +lambda_t D_z+lambda_xt D/2,       (MW8)

    B_t=lambda_x(-D_zz+E_P)/2+lambda_xt D/2,
    (B_z)_t=lambda_xx(-D_zz+E_P)/4
       +lambda_x(-D_zzz+(E_P)_z)/2
                         +lambda_xxt D/4+lambda_xt D_z/2.         (MW9)

The other spatial B derivatives are precisely GS5. Directly,

    F_t=-(1-lambda)G_zz-lambda P_zz+lambda E_P+lambda_t D,

and its z derivative supplies a_t. The identity D_t=-D_zz+E_P is
used before taking bounds; no allowance is differentiated. Only three
source jets occur. The decomposition retained in every consumer is

    E_comp=lambda E_P, E_sp=lambda_xD_z+lambda_xxD/4,
    E_move=lambda_tD,
    (E_comp)_z=lambda(E_P)_z+lambda_x E_P/2,
    (E_sp)_z=lambda_xD_zz+3lambda_xxD_z/4+lambda_xxxD/8,
    (E_move)_z=lambda_tD_z+lambda_xtD/2.               (MW10)

Outside the bands E_comp=E_P or zero. The two last derivatives in MW9
are the additional compatibility-time terms. They are not part of a
holomorphic time-join formula.

Choose finite comparison inputs

    a=X0-24, mu_o=2^50/a^2, mu_s=a^-2, mu=mu_o+mu_s,
    d=d1=2^20/a^3, C0=1, C1=C2=C3=2.                 (MW11)

EF2/EF23 dominate H-P through three in units L^j A_sum with mu_o;
EB4 dominates E_P and (E_P)_z in units A_sum and L A_sum with d,d1.
The frozen L is an upper local logarithm. Require G-H jets at most
mu_s L^j A_min, supplied below, so |D^(j)|<=mu L^j A_sum.
The onset ensures mu<=1/4 and |F|>=A_sum/4 on Sigma+.

Use EB13's displayed finite static ratio bounds with these inputs and
kappa_j=l_j/L^j. Add the following **nonnegative** moving allowances:

| Ratio | Added allowance |
| --- | --- |
| e0=|E|/|F| and v=|F_t|/|F| | 4V kappa1 mu L |
| e1=|E_z|/|F| and a_t*=|(F_z)_t|/|F| | 4V(kappa1+kappa2/2)mu L^2 |
| b_t*=|B_t|/|F| | 2V kappa2 mu L^2 |
| h_t*=|(B_z)_t|/|F| | V(kappa3+2kappa2)mu L^3 |

Spatial A1,A2,b0,b1,bb,b2 are unchanged. In GS14 use the resulting
v and k=2v+A_t W, retaining the explicit q_t contribution and all
Bt terms. The common physical regulator caps on the bands are

    Gamma=Q_+ exp(-a^2/2000+2(X0+24)),
    W<=min(1,16Gamma), theta_reg<=min(1/4,16Gamma).    (MW12)

Here theta_reg=q|F|^2/(|F|^2+q)^2 is distinct from the requested error
target theta. EB7 and the band floor prove MW12. EB10's coefficient
weights use R_c on core/seam supports and local height plus 8 on pure
exterior supports. All new allowances have one fewer logarithmic power
than the corresponding former leading terms; no inverse regulator floor
is introduced on the band.

## 4. Complete supports, direct time rows and actual covariance

GS8--GS12 are identities for any sufficiently smooth F with
B=F_bar_z and E=F_t+F_zz; time-independence of lambda was not used in
their differentiation. Hence they apply with MW7--MW10. This is the
reason the extra terms enter the existing full tuple, rather than a
new covariance or source being defined from a residual.

At each fixed t split the nonnegative FT3 primitive integrals into
the current C_p,T_p,O_p. On T_p use FT5 with the finite MW11--MW12
inputs; z_m includes E_move as well as E_comp and E_sp. Sum core,
gap and exterior columns first. Then apply the global identities with
the fixed K. Do not differentiate the decomposed integral bounds or
their moving indicator functions. The complete ledger is:

| Consumer | Payment used uniformly on J |
| --- | --- |
| U,W and spatial jets | core FT4, gap FT5, exterior EB6/EB9 |
| direct U_t,W_t,R_t | exact FT10 with the complete moving E, then FT12 |
| calC and calC_t | FT11/FT12, with GS13/GS14 evaluated using the new b_t*,h_t*,v,a_t* and actual q_t |
| current J, including internal order three | FT12 with spatial TJ, complete V primitives and full kernel support |
| Q and Delta Q | FT13/EB18: signed GS9 stress first, then the two actual filtered mean products using EB17 |
| forcing calB | FT12 with physical b_r and the weighted w column |
| actual source calS | FT16 with direct Rt/J, signed exterior heat, whole-gap DE and band DB |
| component/spatial/moving heat, Xi/2 | MW10, FT17/FT18 and GS13/GS14; Xi is retained |
| fixed traces | component sums within the available spatial orders, at every t including 95,97 |

Every right side is the finite arithmetic evaluator in Note 47 Sections
4--6 with the displayed substitutions. Kernel derivatives stop at four;
neither an extra time row nor a fourth source jet is hidden in this table.
Both -(calC)_t and -square calC/2 in the density equation remain, with
Delta Q, Delta calB and the derivatives of the actual mean products.

For clarity, the common cap entering the actual mean-product allowance is

    M_gamma=C_H(1+log(2+R_c))+1, 1<=|gamma|<=3,         (MW13)

on core/seam supports. On pure exterior supports retain the local
EB17 cap. C_H is Note 47's fixed central-plus-exterior constant, not
a new growing-core floor estimate. As before the auxiliary k_gamma s<1
constraint is included in the source/budget allocations; Section 5
pays it. Q is never a convex average of component covariances, and
the positive singular squares are not bounded separately.

The signed exterior test partition may move with the gap:

    eta_O(t,x)=b_*((|x|-X(t)-sigma)/sigma).

At a **fixed time**, PE34 with psi=eta_O(t,.)K_alpha uses spatial
derivatives only. Its exact commutators are FT14's
-2eta_O,x K_(alpha+x)+eta_O,xx K_alpha and
-4 Re integral Z1 r_x eta_O,x K_alpha/(4pi).
Use EB12 with c1=l1,c2=l2, and pay the complementary DE on all Sigma+
using the complete E, including E_P on its outer shoulder. No eta_O,t
term belongs to this instantaneous pairing. Such a term would be
required if differentiating an auxiliary truncated quantity such as
integral eta_O rho K; that quantity is not introduced. All physical
cutoff motion is already in MW7/MW9 and calC_t. The same logic avoids
inventing transport terms as collars enter or leave a support: include
every intersecting enlarged collar at that time and use its uniform
raw integral bound and count. No moving trace or Reynolds identity is
claimed.

## 5. One fixed source and a source error that also tends to zero

On the union rectangle MW5 take the explicit core floor

    e_c=E_eta exp(-R_c^2/452), P2=B2+1,
    A_min=exp(-X0-32).                                (MW14)

FI12 gives e_c; EB7 gives the conservative A_min on every moving band
and its required analytic neighborhood. Use exactly the finite core
coefficients D_r in Note 47 Section 6, with FI13 weights at R_c and
the common cap MW13. Include the auxiliary D_gamma=k_gamma rows.
They are source independent and finite before refinement. The core
residual/compatibility columns vanish since G is exact heat and entire.

A fixed quarter-target alone would not give a total error tending to
zero with X0. Tighten the source at the same time as the outer onset.
With the explicit B_mov(X0) of Section 6 put

    rho_*=min(theta/4, B_mov(X0)),
    epsilon_core=e_c^2 min_(D_r>0) rho_* /(4D_r),
    0<epsilon<=min(1,epsilon_core,mu_s A_min).          (MW15)

All these numbers are strictly positive and finite. FI18--FI20 with
this epsilon supply one fixed nonnegative clipped rational-cubic source
f and its entire exact-heat G. Its four-jet error is <=29epsilon/64
on *all* t in J, |y|<=4, every real x; the mode/cell/bit prescriptions
are unchanged. Thus it pays every moving FT19 jet demand and every
core coefficient. Factoring 4epsilon/e_c^2 proves that the entire core
column of each row is <=rho_*<=B_mov. No source change or time-overlap
source debit is present. Its separate interpolation, omitted values,
omitted slopes, nodal arithmetic, rational construction and complete tail
budgets remain exactly the FI18--FI19 categories; field evaluation and
filtering are still separate.

The core floor is used only on the finite union rectangle, permitting
arbitrary zeros or multiple events there. The source cost upper bound
can still be exponential in a constant times R_c^2. Finite description
does not establish affordable construction or an executed source.
Improved conditioning remains HDA-23's separate task.

## 6. Finite onset, vanishing uniform budget and the fixed-width gain

Retain all constants E_eta,Q_eta,R_*,C_H,P2,C_eta from EB16/EB20 and set

    C_mov=C_eta^2=2^4096(1+C_H+Q_eta+P2)^32,
    B_mov(X0)=C_mov {L^6/a^2
                  +(1+X0+24)^16 exp(-a^2/64000)},
    a=X0-24, L=log(2+X0+24).                          (MW16)

Each of the two nonsource columns (enlarged gap with its defects;
exterior with its signed heat correction) is bounded by B_mov on all
J and real heights, including the auxiliary mean-cap rows. To see
the explicit finite constant suffices, start with EB21's coefficient
accounting: the moving increments have numerical coefficients below
2^50 after V=8 and the EB11 profile caps. Their largest new contribution
to GS14 is bounded by a fixed coefficient below 2^200 times mu L^4
pointwise; multiplication by band area <=16sigma removes one L.
The corresponding spatial and direct-time/source insertions have lower
logarithmic orders. Increasing mu_o from the static choice, changing
X to X0±8 and using the frozen upper L costs a fixed factor below 2^200.
Thus a factor 2^512 multiplying EB21's fixed coefficient is sufficient;
C_mov>=2^512 C_eta has much more slack. All polynomial r and r_t
products remain accompanied by their weighted Gamma or Lambda factors.

For explicit exponent conversion, MW12 gives
Gamma<=Q_+ exp(-a^2/4000) at the onset, and EB8/EB9 give the same
monotone B,H_L,Z_L Gaussian reductions as in EB21. Every seam chart
has large height at least X0-16>=a; fixed additional local replacements
are covered by the buffer slack and denominator 64000. On pure exterior
supports use local height v, and take the decreasing supremum of the
polynomial--Gaussian and logarithmic/power envelopes. Core-only supports
have no nonsource column. This proves uniformity in **every real height
and every t in J**, without summing errors over a chart count or a time
partition. In particular B_mov=O_eta(log^6 X0/X0^2) and tends to zero.
The deliberately coarser logarithmic power supplies an explicit common
constant; no optimized rate is claimed.

One sufficient exact onset for a prescribed component target theta is

    m=4096+ceil(log2(R_*+64))
                         +ceil(4log2(2+C_mov/theta)),
    U=2^m, then select X0>=U by EB2.                   (MW17)

As in Note 44, ceilings can use certified integer upper bounds with
two extra units. MW17 needs no field/gamma sampling. Then
X0 in [2^m,2^m+1], a>=2^(m-1), L<=m+3,
C_mov<=theta*2^(m/4). For m>=4096,
(m+3)^6<=2^(m/2) and exp(-a^2/64000)<=X0^-32.
These elementary monotone bounds give B_mov<theta/4, with ample
room. They also pay all collar, mu, Gamma and Lambda finite gates.

MW15 now bounds each core column by B_mov; the two nonsource columns
are each bounded by B_mov. Hence every scalar analytical row satisfies

    sup_(t in [95,97], x in R, |y|<=1) error_r
                   <=3B_mov(X0)<=3theta/4.            (MW18)

Verify the auxiliary k_gamma s rows first: they use only primitive S
errors and contain no common mean cap. They give k_gamma s<1 and hence
justify the candidate cap MW13. The remaining core coefficients and
EB18's covariance/source products may then use that cap. Defining
epsilon with the candidate caps beforehand is consistent because this
auxiliary verification is independent. Taking X0 through the selected
phase gaps and refining G by MW15 yields the claimed vanishing error
on the fixed domain [95,97] x R_x x [-1,1]_y. Merely keeping the old
source quarter-allocation independent of X0 would not have proved
this limit. No error is propagated by a PDE or by the smallness of E.

## 7. A concrete fixed-chart alternative and why it is not needed

A legitimate finite fixed-gap cover is possible using the *same*
preserved phase index and source. Here is a controlled comparison,
not a second executed construction. With the frozen L above set

    N=ceil(65536L^2), delta=2/N, t_j=95+j delta,
    X_j=X(t_j), sigma_c=1/(128L).

Let lambda_j be FI10's fixed spatial cutoff centered at X_j with
width sigma_c. On [t_j,t_(j+1)] use the flat time profile
vartheta=b_*((t-t_j)/delta) and

    F_j=G+lambda_j D,
    F=(1-vartheta)F_j+vartheta F_(j+1)=G+Lambda D,
    Lambda=(1-vartheta)lambda_j+vartheta lambda_(j+1). (MW19)

Flat endpoints make this a smooth field on J, with at most two active
charts. Adjacent centers differ by <=Vdelta. All active cutoff and
time-derivative supports lie in one common zero-free enlarged gap:
the displacement Vdelta is much less than sigma_c. The mean-value
bound gives, for r=0,1,2 and the corresponding fixed spatial norms l_r,

    ||partial_t partial_x^r Lambda||
                  <=||b_*'|| V l_(r+1).              (MW20)

The factor delta^-1 cancels the center displacement. Thus Lambda_t,
Lambda_xt,Lambda_xxt have orders L,L^2,L^3, rather than an unpaid
delta^-1 field loss, and the total N=O(L^2) chart count does not multiply
a local error. There is one moving-gap branch even in this construction;
independent choices of a new gap index at each node would not supply
this bound or a common gap floor.

The holomorphic time-join lemma CJ22 cannot be applied to these F_j.
Instead use the actual nonholomorphic F=G+Lambda D: MW7--MW10 hold
with lambda replaced by Lambda, with new terms Lambda_tD,
Lambda_tD_z+Lambda_xtD/2, Lambda_xtD/2 and
Lambda_xxtD/4+Lambda_xtD_z/2 in the corresponding E/Ez/Bt/Bzt rows.
Apply GS8--GS12 to that field; neither compatibility curvature nor Q
is the convex average of the component observables. In finite terms,
Vdelta/sigma_c<=1/(32L); the actual FI9 norms at sigma_c still satisfy
EB11's loose caps. Since ||b_*'||<8, MW20 increases the first-time
allowances by at most eight. Their consumers in GS14, DE and the direct
time rows are linear in those first-time inputs. Thus
C_chart=2^16 C_mov is a safe enlarged common constant for this alternative,
with its own onset obtained by replacing C_mov in MW17 and using the
same source-tolerance rule. No factor N appears in it. The alternative
introduces an unnecessary finite time partition. The selected moving
route uses **one** moving cutoff, zero time-chart changes and one G.

## 8. Compact-J reuse and exact remaining scope

For any prescribed compact J=[t_-,t_+] contained strictly in (64,infinity),
the same moving construction gives a reusable analytical template.
Notes 30--31 supply eventual uniform outer field/collar/unit inputs
e=O_J(X^-2), d=O_J(X^-3). The exact FI4 phase formula and the fixed-J
gamma sector give a bounded gap speed V_J; therefore
|X(t)-X(t0)|<=V_J|J|. Freeze sigma=c_J/log(2+X0), use one source on
the union rectangle of radius X0+V_J|J| plus the fixed buffers, and
replace the finite field/source constants by those for that J. The
same three-jet and fourth-kernel-order ledger holds. Since
beta_min=inf_J beta>0, q/A_sum^2 is bounded by a constant times
exp(-c_J X0^2), paying every polynomial regulator coefficient. This
proves the compact-J structural extension with J-dependent constants.
The explicit numerical constants and closed onset MW17 in this return
are instantiated only for [95,97]; no new effective general-J contour
table is silently asserted.

The following limits are not uniform consequences of this argument:

- As t_- tends to 64, beta_min tends to zero. The first unavailable
  uniform premise is the Gaussian suppression in MW12/MW16 based on
  beta_min>0. Geometry and exact identities remain, but the physical
  switch layer needs the PE41--PE44 estimates, its exact crossover
  center and new complete-tuple payments. This is not an impossibility
  claim for moving gaps or another switch estimate.
- As |J| or t_+ tends to infinity, velocity range, source moments,
  buffers and constants have not been bounded uniformly. A fixed finite
  source is not continued to all positive time. The all-height positive
  endpoint theorem of Note 31 must be joined with paid overlap fields,
  heat and actual covariance terms.
- Negative times and the negative endpoint of Note 26 require their
  own finite-time/endpoint overlaps. Nothing here changes that theorem
  or pays the all-time joins by initial data alone.

The global consumer remains a finite analytic prescription with useful
proved errors for **every real height and time**, including both height
limits and t tending to either infinity. This result fills a fixed-width
central input, not the full real-time cover.

## 9. Review, controls and disposition

Primary passages rechecked were the official
[DLMF local inversion theorem](https://dlmf.nist.gov/1.10#vii),
[Cauchy derivative formula](https://dlmf.nist.gov/1.9.E31) and
[complex gamma remainder rule](https://dlmf.nist.gov/5.11#ii).
The new time terms are derived from the exact field, not imported from
a holomorphic blend or an asymptotic time derivative. Three read-only
same-model subagents separately derived moving geometry, the alternative
cover/signed partition and the complete ledger; this is shared-premise
LLM checking, not independent specialist review.

No numerical, exact-rational or machine-symbolic research check was run;
none is authorized by this revision. No theta/source/gamma/field sample,
mesh/precision search or interval campaign. Earlier algebraic checks are
reused by reference, not rerun. File hashes, sizes and local links are
housekeeping only. No manuscript, previous source-note, snapshot, commit,
model change, new chat or cross-chat dispatch.

Collision controls retain their same premise failures: Euler factors
lack the unchanged canonical completion; weighted-square/finite-prime
controls lack its full coefficient/reflection input; reflected and
positive-primitive controls lack the canonical gamma/source identity;
atomic and heat-polynomial controls lack the smooth theta source. They
may satisfy the generic identities and collide. A band covering a zero
fails the gap floor; another moving gap does not exclude that collision.
There is no RH, global simplicity or universal complexity conclusion.

**Disposition:** AN05 r1 and HDA-22 are complete at this fixed-width
analytical scope. No resistant estimate in this packet warrants Astra.
HDA-17 Partial, HDA-18 Gated and HDA-20 unfulfilled are unchanged.
The dependency for [AN06 r1 / HDA-24](../research-progress/handoffs/HDA-18-AN06.md)
is now supplied; it is ready for **Analysis — Sol** to address the exact
physical switch layer and retain the global objective. HDA-23's core
conditioning task remains ready and distinct from domain coverage.
The sole progress register owns live phase; no next packet is executed
by preparing this return.

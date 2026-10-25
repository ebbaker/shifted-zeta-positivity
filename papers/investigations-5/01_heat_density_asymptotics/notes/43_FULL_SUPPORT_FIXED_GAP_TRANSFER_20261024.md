# Full-support comparison for the fixed-gap spatial join

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. **gpt-6.1-sol (Codex), actual effort ultra**,
verified from this turn's metadata. Chat **0015**, thread
`01a1711d-376c-7de3-929c-60ec4065bddc`.

**Status: full-support transfer proved in-note from the stated component,
gap and source inputs; internal LLM checking only.** This returns
[HDA-18-AN01 r1](../research-progress/handoffs/HDA-18-AN01.md). It completes
Note 42's local-to-full-support analytical comparison on its unchanged
fixed-gap short slab. It supplies finite sufficient inequalities, not
accepted numerical constants, an affordable source, an effective onset,
or an all-time join. HDA-17 remains Partial, HDA-18 Gated, HDA-20 unfulfilled.

This is an approximation estimate under
[avoid 01](../../../../avoid/01_restating_the_target.md). Read the
[result index](../../../../result-summaries/README.md),
[heat-flow cluster](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
[collision controls](../../../../result-summaries/12_collision_controls_and_screening.md)
and [avoid index](../../../../avoid/README.md), particularly
[scope](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[cancellation](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
and [shared-premise reviews](../../../../avoid/05_same_model_reviews_and_shared_premises.md).
The input [manifest](43_FIXED_GAP_TRANSFER_INPUTS_20261024.json) pins Note 42,
the original r1 request, Notes 30/31/34/37 and Review 23 before this return.
The request is frozen; its return is appended. No source note or physical
convention is changed.

## 1. Geometry and statement

Keep precisely H, q=epsilon_g^2, K=k_ell k_h, Y_b=Y+h+2, P, G, F,
lambda, E, B and I from Note 42 GS1–GS7. Thus J is a fixed compact
subinterval of (64,infinity), L=log(2+X), sigma=c/L, and
I=[t0-tau,t0+tau] with the GS2 root-speed restriction. No cutoff moves
in time. Fix one even smooth profile, flat at its endpoints, and scale it
on the two bands; record l_j=||lambda^(j)||infinity for j=1,2,3.
All constants below are for that profile and the declared buffers.

For each observation p=(x,y), |y|<=Y, use the entire planar support
Omega_p=p-supp K. Decompose its **ordinary nonnegative integrals** into

    C_p: |u_x|<X-2sigma,
    T_p: ||u_x|-X|<=2sigma,
    O_p: |u_x|>X+2sigma.                                  (FT1)

The enlarged transition region is Sigma+; Sigma denotes the actual
nonholomorphic bands ||u_x|-X|<=sigma. Area(Omega_p intersect Sigma+)
is at most 16h sigma; for Sigma it is at most 8h sigma. These conservative
bounds include both reflected bands. On T_p the GS1/GS3 neighborhood
bounds are required on the closed enlarged band and an open buffer;
this is the very band |u_x-X|<=2sigma in GS1, including its reflection.
The source rectangle is the full GS2 rectangle

    I x {|u_x|<=X+ell+2sigma+2, |u_y|<=Y_b},                (FT2)

enlarged if any selected collar disk needs more room. Require the
GS1–GS3 comparison bounds on the stated band neighborhoods within FT2.

For each exterior portion O_p, include **every enlarged root collar
intersecting that exterior portion** and its fixed-factor larger analytic
disk from FS22/PE10–PE12. Collars in C_p may instead have F=G. Extend
the analytic buffer as needed. Their radii are comparable to 1/L locally,
and a fixed support meets O(L) collars. The gap gate puts these collars
outside Sigma+; on them F=P and B=0. On C_p, F=G is entire and exact heat;
no simplicity assumption is made about G's roots. On T_p, use the common
field floor, never a holomorphic identity for F.

The theorem below gives the whole CJ14 tuple at every p and t in I,
including pure core/exterior supports and supports crossing either band.
It uses finite explicit positive expressions FT3–FT17. Supremize those
expressions over a closed observation rectangle, or over all real x using
the stated exterior envelopes, to obtain a uniform version. It involves
kernel derivatives through order four only.

## 2. Primitive ledger: split integrals before weak differentiation

Let delta denote F minus H and define V_m and Z_m for the actual F as
in GS7/PE13; Z_m=w_F^m E conjugate(F)/D_F and Z_m,H=0. Set chi_F=w_F(1-w_F).
For each nonnegative coefficient function a on Omega_p define

    s[a]   = integral a |delta S|,
    w[a]   = integral a |delta w|,
    v_m[a] = integral a |delta V_m|,       m=0,1,2,
    z_m[a] = integral a |Z_m,F|.                          (FT3)

Here s=s[1]. All integrals have planar area measure. Each right side may
be replaced by the sum of the following three positive allowances.
These are raw integral bounds, not component filtered-observable bounds.
In particular, no truncated whole-support weak theorem is imported.

**Core.** Freeze CJ4's coefficients a_C,b_C,k_C,P_2 using fixed caps
bar d_0,bar d_2 and the actual positive q on the compact rectangle. For
uniform exact finite-source errors d_0,d_2, put

    s_C=2 a_C d_0,  w_C=k_C d_0,
    v_m,C=a_C d_2+(P_2 b_C+m P_2 a_C k_C)d_0,  z_m,C=0.  (FT4)

For a source-independent coarse choice, put e_C=min sqrt(q)>0 on FT2
and use a_C=1/(2e_C), b_C=e_C^-2, k_C=e_C^-1, and a P_2 cap from
canonical source moments plus bar d_2. This freezes the coefficients
without relying on the source being refined.
Integrate these pointwise bounds times the actual weight a over C_p.
Using area(C_p)<=4ell h and a coefficient supremum is a valid finite
coarse alternative. This pays all core rows with field orders 0 and 2.
The compact regulator floor enters FT4 only; it is not used on the gap
or exterior.

**Enlarged gap.** Put c_*=c0/2, epsilon=q/A^2,
W_*=min(1,epsilon/c_*^2), delta_0=|F-H|/A,
delta_2=|F_zz-H_zz|/A and C_2=max(|F_zz|,|H_zz|)/A.
The segment from F to H stays within mu A of P; its modulus is at least
c_* A. Hence the following are valid pointwise allowances:

    s_T=2 delta_0/c_*,
    w_T=min(1,2 epsilon delta_0/c_*^3),
    v_0,T=delta_2/c_*+C_2 delta_0/c_*^2,
    v_m,T=W_*^m v_0,T+m W_*^(m-1) w_T C_2/c_*, m=1,2,
    z_m,T=W_*^m (|E|/A)/c_*.                            (FT5)

They follow from CJ5's real-variable derivatives with the stronger field
floor retained. In particular delta_0<=2mu and

    delta_2 <= 2mu L^2+l_1 mu L+l_2 mu/4.                (FT6)

Use GS5 for E and the actual derivatives of F for C_2; the shoulders
have B=0 and E=0 or E_P. Integrate FT5 with weight a over T_p.
The epsilon factors in w_T,v_1,T,v_2,T,z_1,T,z_2,T are essential.
They cannot be replaced by O(mu) or O(mu L^2) before multiplication
by polynomial regulator coefficients.

**Exterior.** Use FS23/PE14–PE17 collar by collar and the zero-free
complement. The finite unweighted allowances are, with the comparison
constants and local root frequency omega explicitly retained,

    s_O[1] <= C_S e,
    v_m,O[1] <= C_p e(1+|log e|)+C_v e omega+C_g e omega^2,
    z_0,O[1] <= C_Z d.                                  (FT7)

Here e and d are PE2 or their compact-J bounds C_J u^-2,C_J u^-3;
u is the large height of the actual enlarged exterior chart meeting O_p,
not necessarily the observation-center height and not a new tolerance.
Use that chart's omega,e,d,Lambda; the uniform version takes the supremum
over such charts with u>=X-O(1). Constants
in FT7 are the finite constants from those proofs, including collar
count and enlargement. For a restricted exterior integral, enlarge each
intersecting collar to its full disk and use its nonnegative integral
bound. On the remainder use PE9 and its carrier-sum floor. This proves
FT7 for the piecewise field without extending P into its central domain.

For the regulator-weighted rows use PE21's *individual* estimates, not
C_S e multiplied by an unbounded regulator coefficient. On each support
let Lambda be its carrier-relative upper regulator scale as in PE20,
including the fixed collar/carrier comparability constants. Take 0<Lambda<=1/2
as a finite gate. Write

    B_L=Lambda^2[1+(1+|log Lambda|)/omega],
    H_L=omega^2 B_L+Lambda,
    Z_L=B_L+Lambda/omega.                               (FT8)

For any of the weights a used below, let a_O^* be its supremum on the
enlarged local support. PE21 gives, with the named finite constants,

    w_O[a] <= 2 C_w a_O^* B_L,
    v_m,O[a] <= 2 C_h a_O^* H_L,             m=1,2,
    z_m,O[a] <= C_z d a_O^* Z_L,             m=1,2.        (FT9)

The factor 2 sums H and P; extra powers of w are bounded by one.
Delta chi is bounded by delta w. These bounds retain Lambda and its
logarithm, even when too small for floating representation.
For v_0[1] and z_0[1] use FT7. No exterior absolute L1 bound for D_E
is asserted: that signed correction needs the paid test partition in
Section 5.

There is no integration by parts on C_p,T_p,O_p. Apply the smooth global
identities only after the sums in FT3 are formed. Therefore no derivative
of an indicator in FT1 occurs. All actual field-cutoff derivatives are
already in GS5, TC,TJ,Xi and their time derivatives. Section 5 is the
one place where a smooth test partition really is used and must be paid.

## 3. Time ledger and finite positive comparison maps

Use the actual pointwise coefficient weights

    R1=|grad r|, R2=|Delta r|, T1=|grad r_t|,
    T2=|Delta r_t|, Th=2|grad r| |grad r_t|,
    c_r=|r_xx+r_x^2|, b_r=|r_t+(r_xx+r_x^2)/2|.

Direct differentiation, valid for nonholomorphic F because
F_t=-F_zz+E by definition, gives the following allowances for every a:

    st[a]=2v_0[a]+w[a|r_t|]+2z_0[a],
    wt[a]=w[a|r_t|]+2v_1[a]+2z_1[a],
    ct[a]=w[a|r_t|]+2v_1[a]+4v_2[a]+2z_1[a]+4z_2[a].    (FT10)

They bound the weighted integrals of |delta S_t|, |delta w_t|,
|delta chi_t|. The polynomial w(1-w)(1-2w) is 1-Lipschitz on [0,1].
Neither a source allowance nor an asymptotic remainder was differentiated.

For alpha define k_alpha=||partial^alpha K||infinity,
n_alpha=k_(alpha+x)+k_(alpha+y),
d_alpha=k_(alpha+xx)+k_(alpha+yy). These weak kernel norms are finite;
K is C3 and its fourth weak derivatives are bounded without boundary
deltas. Set

    C_alpha = [2n_alpha w[R1]+k_alpha(w[R2]+w[R1^2])]/(4pi),
    Ct_alpha=[2n_alpha(wt[R1]+w[T1])
       +k_alpha(wt[R2]+w[T2]+ct[R1^2]+w[Th])]/(4pi).      (FT11)

Only use d_alpha when |alpha|<=2. Let tC_alpha, tCt_alpha, tJ_alpha,
xi_alpha be k_alpha times the integrals on Sigma of the exact positive
GS13/GS14 envelopes for |TC|, |(TC)_t|, |TJ|, |Xi|. These are explicit
finite rational expressions in the declared field ratios, r_t,w and
kernel norms; GS15's area bounds may replace the integrals. They retain
both q_t and B_t terms. In particular Ct_alpha denotes the regulator
part only; tCt_alpha is separate.

## 4. Whole-support tuple, including the actual covariance

Write calC=K*C_tot and calB=K*(b w). For |alpha|<=2, define

    E_U,alpha = k_alpha s,
    E_W,alpha = k_alpha w[1],
    E_C,alpha = C_alpha+tC_alpha,
    E_R,alpha = d_alpha s/(4pi)+E_C,alpha,
    E_J,alpha = [n_alpha v_0[1]+k_alpha v_1[R1]]/(2pi)
                                                     +tJ_alpha/pi,
    E_Ut,alpha = k_alpha st[1],
    E_Wt,alpha = k_alpha wt[1],
    E_Ct,alpha = Ct_alpha+tCt_alpha,
    E_Rt,alpha = d_alpha st[1]/(4pi)+E_Ct,alpha,
    E_B,alpha = k_alpha w[b_r].                         (FT12)

The U,W formulas hold through order four. The J formula also holds
through order three internally; it needs only fourth kernel derivatives.
Other rows of FT12 have the orders just stated. CalC uses the *total*
curvature; regulator and compatibility curvature must not be conflated.

For covariance let e_gamma=k_gamma s, 1<=|gamma|<=3, and choose finite
common caps M_gamma for the actual derivatives of U_F,U_H. Define

    N_alpha = sum_(i=x,y) sum_(beta<=alpha) binom(alpha,beta)
       [e_(beta+i) M_(alpha-beta+i)
                         +M_(beta+i) e_(alpha-beta+i)],
    E_Q,alpha=4k_alpha v_0[1]+d_alpha s+k_alpha w[c_r]
                                             +xi_alpha+N_alpha. (FT13)

This bounds the Q defined in GS10, through order two. First apply the
GS9 signed-stress identity globally to the already defined integrand
S_x^2-S_y^2, including Xi; integrate the square S term by parts against
the full K_alpha. Only then subtract the two actual mean-gradient
products and use Leibniz' rule. Component covariances are never averaged.
Separate positive squared-gradient estimates, which lose the narrow-root
cancellation, are never substituted for the signed identity.

For finite constants, M_gamma may be bounded by the exact-H cap plus
e_gamma. To keep the asymptotic decrease in Section 7, use the following
sharper cap instead of the crude CJ12 O(X^2) bound: fix one central
observation rectangle beyond the established outer threshold. Its
physical q floor and source-moment caps give finite H derivative bounds.
For all larger heights PE30's integrable simple-pole/unit argument gives
|partial^gamma U_H|<=C_H log(2+|x|), 1<=|gamma|<=3. On core or seam
supports |x|<=X+ell+2sigma use C_H(1+L). First require the fixed exterior/gap debit in k_gamma s to be <1, then
choose source accuracy so the **total** k_gamma s<=1 there; then M_gamma=C_H(1+L)+1 is valid for F as well.
On pure exterior supports use PE30 and FT7 at their local height.
This proof uses a fixed compact central cap plus the exterior estimate;
it does not infer O(L) from CJ12 and does not change the physical U.

The proof of FT11–FT12 is global integration by parts in GS9:
C_reg paired with psi equals

    [-2 integral w grad r dot grad psi
       -integral (w Delta r+chi |grad r|^2) psi]/(4pi).

Differentiate this identity at fixed spatial coordinates to obtain FT11's
time row, including T1,T2,Th. Then use
Delta delta S=4pi(delta rho+delta C_reg+TC).
For current use GS9's actual TJ term. These are identities of the
smooth piecewise field on the whole support; there is no discarded
interface flux. This also proves the direct R_t row without heat
propagation or differentiating a previously proved error estimate.

## 5. Signed source and the paid exterior heat partition

The nonholomorphic weak residual formula cannot be borrowed from CJ18.
Instead choose one even time-independent eta_O, supported in
|x|>=X+sigma, equal to one for |x|>=X+2sigma, flat at endpoints;
record c_j=||eta_O^(j)||infinity for j=1,2. Its derivatives lie in the
zero-free outer shoulders of Sigma+. F=P on its support.

Apply PE34 to D_(E_P) with psi(u)=eta_O(u_x) K_alpha(p-u). Here
K_(alpha+x) denotes differentiation in the kernel argument, so
partial_(u_x) K_alpha(p-u)=-K_(alpha+x)(p-u). In addition to the
terms with eta_O times derivatives of K, the exact commutators are

    1/(4pi) [2 Re integral Z_0,P(-2eta_O' K_(alpha+x)
                                           +eta_O'' K_alpha)
              -4 Re integral Z_1,P r_x eta_O' K_alpha].  (FT14)

Every cutoff derivative is retained. For a completely mechanical finite
bound, let N2(psi) be the sum of sup norms of all partial derivatives
through order two and use PE35:

    D_out,alpha <= C_DE d N2(eta_O K_alpha),
    ||D^beta(eta_O K_alpha)||infinity
      <= sum_(j=0..beta_x) binom(beta_x,j) c_j
                       k_(alpha+beta-j ex), c_0=1.     (FT15)

Use local exterior d and its constant C_DE; this is a weak signed bound,
not an assertion that integral |D_(E_P)|<=C_DE d. FT15 costs at most
O(d L^2). One may retain the sharper shoulder payment from FT14:
if |Z_0,P|<=C_d d, |Z_1,P|<=C_d d gamma_* there and
A_sh<=16h sigma, its additional allowance is

    C_d d A_sh/(4pi) [4c_1 k_(alpha+x)+2c_2 k_alpha
                              +4 gamma_* R1_sh c_1 k_alpha],

in addition to the main PE14/PE21 terms with eta_O. This is O(d L)
plus the retained exponential term. Both versions suffice below; the
coarse FT15 is the default finite contract.

The remainder (1-eta_O)D_E,F is zero in the pure core and supported
inside Sigma+. Pay it pointwise by GS13 using the actual E,E_z on
that entire region. In particular E=E_P on the outer shoulder.
Let D_gap,alpha=k_alpha integral_(Sigma+) E_DE,F and
D_B,alpha=k_alpha integral_Sigma E_DB,F, with those GS13 envelopes.
The actual signed source calS=K*((1-2w)(r_t rho+grad r dot j)) obeys

    E_S,alpha=E_Rt,alpha+E_J,alpha+x+E_J,alpha+y
                      +D_out,alpha+D_gap,alpha+D_B,alpha. (FT16)

This follows by subtracting the two exact GS12 balances; H has no E,B.
It estimates the actual source, rather than defining it from the balance.
Alpha<=2, so FT15 and the internal current derivative use K through four.
The inner shoulder contributes zero E,B; keeping its allowance is harmless.

For clarity, separate the field residuals on all of F's domain:

    E_comp=lambda E_P on the bands, E_P outside, 0 inside;
    E_join=lambda' (P-G)_z+lambda''(P-G)/4 on the bands.   (FT17)

E=E_comp+E_join exactly. In the band
(E_comp)_z=lambda(E_P)_z+lambda' E_P/2;
(E_join)_z=lambda'(P-G)_zz+3lambda''(P-G)_z/4
                                      +lambda'''(P-G)/8.
These identities include the differentiated partition of E_P. Use their
separate magnitudes in z_m, GS13 and GS14; D_E is linear in E,E_z for
fixed F. GS5 also gives B,B_z,B_bar_z,B_zz. TC is quadratic/linear
in these compatibility derivatives; it is not an E_P-only residual.
The pure exterior signed heat correction in FT15 is additional to all
band defects. No error is propagated from the smallness of E.

## 6. All equation rows and traces are consumers of the same tuple

For the actual F the exact potential/density/current equations are GS11
and GS12 with C_tot=C_reg+TC and

    T_U=Xi/2+2 Re Z_0,F,
    |partial^alpha K*T_U|
                    <=xi_alpha/2+2k_alpha z_0[1].        (FT18)

Keep Xi/2 as well as the component/join heat terms. This estimate holds
through order four wherever required; it uses derivatives of K, not
unpaid fourth derivatives of the field. The density equation contains
both -(calC)_t and -square calC/2, as well as Delta Q and Delta calB/(4pi).
They are paid respectively by E_Ct, by sums of E_C,xx/E_C,yy, by
E_Q,xx+E_Q,yy, and by E_B,xx+E_B,yy. The mean-gradient terms and their
Laplacian use precisely N_alpha, not a new closure. Forcing/source,
U_t,W_t,R_t are direct rows, not values defined by those PDEs.

Fixed spatial boundary traces inherit the same uniform bounds: U uses
E_U, its normal derivative uses sum_i |n_i|E_U,i, and normal current
uses |n_x|E_ReJ+|n_y|E_ImJ (each real/imaginary allowance is at most
E_J). Initial/final time traces are the restrictions at t0±tau. Normal
traces of other differentiated quantities use the corresponding component
sums within their proved orders. There is no moving-boundary term because
all these boundaries, the field cutoff and eta_O are fixed in space.

## 7. Finite source contract, model gate and decay

At a proposed finite X the following suffice, with all constants and
inequalities recorded, rather than merely sampled:

1. The P branch, full-buffer FS22/PE9–PE12 collar/unit constants,
   relative field and residual constants, and GS1's c0,C_j are valid
   on the full domains. Verify the model-gap collar separation and
   c_*=c0/2>0, record sigma,l_j,c_j, and verify GS2 with its actual
   root-speed cap. The band neighborhoods in FT2 have a positive
   A_min=inf A. Record Lambda and FT8–FT9's regulator bounds on every
   exterior support or a proved uniform exterior envelope.
2. Choose positive band-source allowance mu_s. If mu_o pays H-P's
   relative jets through three, require mu_o+mu_s<=c0/2 and call this
   sum mu. Require the exact finite-source errors

       d_j^gap <= mu_s L^j A_min,        j=0,1,2,3.      (FT19)

   Then G-P and H-P meet GS3 with mu. Alternatively use Cauchy's formula
   on an additionally paid analytic neighborhood to obtain these jets;
   do not differentiate the source error bound. Use |E_P|<=d A and
   |(E_P)_z|<=C d L A as in GS3.
3. Freeze core/source caps and common covariance caps first. Substitution
   of FT4 in FT10–FT13/FT16 yields a finite list of nonnegative core
   coefficients A_r,B_r, with allowance A_r d_0+B_r d_2 for every row r.
   Include the auxiliary s/covariance-cap constraints. These coefficients
   are the explicit products/integrals in this note, not unspecified
   Lipschitz constants. For positive core allocations theta_c,r require

       d_0 <= min(bar d_0, min_(A_r>0) theta_c,r/(2A_r)),
       d_2 <= min(bar d_2, min_(B_r>0) theta_c,r/(2B_r)).  (FT20)

   Empty inner minima impose no constraint. The source is one fixed
   positive source for the whole rectangle/slab, not a new one per test.
4. Every d_j is a continuous full-buffer allowance from Note 37 HE6/HE8:
   retain interpolation/fallback, omitted nodal values, omitted nodal
   derivatives, nodal value arithmetic, nodal slope arithmetic,
   construction arithmetic and the complete-source tail separately.
   The relevant weight is u^j exp((sup I)u^2+Y_b u), j<=3. The old
   t=64,Y=1 floating rows do not instantiate this contract. Field/observable
   evaluation arithmetic and continuous filtering remain separate debits.
5. Compute each nonsource debit from FT7–FT18 with the supplied constants
   and selected mu_s; require that debit plus theta_c,r and any declared
   arithmetic/integration allocations be no larger than the chosen row
   target theta_r. A nonpositive remaining source allowance fails this
   finite gate; finer source refinement does not remove outer/residual
   costs or enlarge the model gap.

For a simple existence-level decreasing budget, choose mu_s=O_J(X^-2),
mu_o=O_J(X^-2), d=O_J(X^-3). On J the regulator has beta_min>0;
the compact-time carrier bound gives epsilon and Lambda exponentially
small in X^2 on gap/exterior supports. FT8–FT10 therefore pay every
polynomial r,r_t coefficient. They are retained at finite X. Core FT20
may be tightened until its entire contribution (with the global mean caps)
is <=X^-2 in each row. Positive finite sources can approximate all four
jets to these strictly positive demands on the compact rectangle by
Notes 20/37; positivity and exact heat evolution are preserved.

FT7's signed-pole loss is at most e L^2. The transition costs are

    TC,Xi: O(mu L); TJ: O(mu L^2);
    (TC)_t: O(mu L^3); heat potential: O(d/L+mu L);
    band current residuals: exp(-c_J X^2) times polynomials;
    exterior signed heat partition: O(d L^2) using FT15.  (FT21)

The exterior direct-time/stress/current rows on this strict after-switch
slab are O_J(e L^2+d), by FT7–FT10, rather than the weaker switch-uniform
PE44 bound. With the common gradient cap O_J(L), FT13 costs at most
O_J(e L^2+mu L+core contribution). Consequently the largest complete
comparison allowance in this construction is

    O_J(X^-2 L^3 + X^-3 L^2)
       + the explicitly retained polynomial-exponential terms. (FT22)

All rows decrease as X tends to infinity along model gaps. There is no
additional logarithmic loss in mu beyond Note 42's L^3; FT15 adds only
a smaller residual d L^2. A naive test partition of every weak identity
would add derivatives of size L,L^2 to their primitive errors; it is not
used here. Its absence follows from the full-support proof in Section 2,
not from discarding those derivatives.

No effective X, c0 or accepted source is computed. A_min typically has
log A_min=-pi X/8+O_J(log^2 X); the coarse core q floor can make FT20
require absolute accuracy of order exp(-C_J X^2) or smaller after its
polynomial factors. Thus finite source existence is proved; affordable
finite source complexity and a certified onset remain unpaid. This is
the practical failed acceptance gate, not a failed uniform comparison
estimate. The construction covers the fixed short I with tau=O(1/L);
it supplies no moving-gap cover, crossing of 64, negative-endpoint join
or all-time assembly.

## 8. Checks, controls and disposition

The bounded exact-rational check uses six polynomial field/regulator
cases, including B=0, conjugate z, x, a polynomial cutoff join and a
nonzero E_z case. Its separate script/record and the internal assessment
are linked from [Review 24](../reviews/24_FIXED_GAP_FULL_SUPPORT_ASSESSMENT_20261024.md).
These check local algebra, not the collar estimates, continuous theta
accuracy, convolution quadrature or theorem certification. Preserve any
failed cases in that record. No theta samples or mesh/precision search.

Collision screen: the transfer and exact identities allow collisions,
including z^2-2t. A transition containing a zero fails the selected gap
floor; an unrelated gap is no collision exclusion. Euler-factor controls
lack the unchanged canonical completion; weighted-square/finite-prime
controls lack its full coefficient/reflection inputs; reflected and smooth
positive-primitive controls lack the canonical gamma/source identity;
atomic and heat-polynomial controls lack the smooth theta-source premise.
They may satisfy the generic transfer and are not excluded by it. This
is no RH or simplicity claim and no universal no-join obstruction.

**Disposition:** HDA-18-AN01 r1 closes at its requested analytical scope:
full-support tuple and defect comparison with finite sufficient source/
gap inequalities. No resistant structural estimate remains in this fixed
slab construction. Parent research statuses and the manuscript are unchanged.

**Next: Analysis — Sol.** Instantiate the finitely many gap, collar,
residual and FT19–FT20 source coefficients on one declared compact-J model
gap, report a source-complexity bound or a failed finite gate, and stop
before theta evaluation unless a later packet authorizes it. The separate
frozen-point certificate and HDA-21 specification retain their own scope.

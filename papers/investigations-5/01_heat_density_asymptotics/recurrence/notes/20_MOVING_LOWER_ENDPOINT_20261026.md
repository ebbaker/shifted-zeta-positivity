# R05-AN08: the specified moving lower endpoint tau(L)=1/L

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Inherited parent configuration:
**gpt-6.1-sol (Codex), effort ultra**, reported by the orchestrating research
agent; no separate subagent turn-context verification is claimed. Public
history belongs to parent base heat-density chat0025, thread
`01a179ab-8856-7ba0-89a2-500b2d854c80`, with configuration verified by
the orchestrator from its turn metadata; no new subagent registration.

**Return to HDA-R05-AN08 r1. Proved in-note from the named inputs;
same-model internal assessment only.** Set

    R=r+1, Y=b+1, W=R+Y, nu=ceil(W)+1>=4,
    L=log(X/(4pi)), p=floor(L/2), K=2p, V=8sqrt(2)L.

For fixed positive chart radii, a sufficient all-height onset is

    L_mov=1024 nu²,       X_mov=2^(2048 nu²+8).              (M1)

For every accepted center with L>=L_mov, the complete canonical recurrence
comparison and finite delivered-error construction below give

    ||h - F_delivered||_(outer; X; 1/L,2)^(3,1)
                       <= exp(-L²/4).                     (M2)

The channel norm in M2 retains independently delivered field, spatial
orders0--3 and first-time outputs. The mathematical comparison includes
T=1/L. Effective queries are the
strictly witnessed rational queries in Section6, and optionally the explicit
endpoint tag defined there with its own paid time-input channel. Both arms,
all n<=N, every C_0 through C_K, exact adjacent-cutoff transfer, the bounded
real integral and original unit buffers remain. Every chart selection,
including tau=1/L, is frozen under z,T differentiation. T=0 is excluded.

This expands the time domain at a more conservative sufficient height;
it does not improve Note16's [1,2] onset 64nu or assert a minimal onset.
That theorem and the old finite providers remain valid fallbacks. The
complete canonical evaluator is still unimplemented/uncertified. No
numerical campaign, symbolic inequality test, field evaluation or zero
search was run. [Inputs][inputs], [work record][work] and [Review14][review]
identify versions and limits; no manuscript is edited by this return.

## 1. Unchanged canonical data and calibration

Use h(T,z)=H(-T,z), h_T=h_zz, H(0,z)=xi((1+iz)/2)/8, the complete
canonical theta source and gamma branches of Notes04--11. The enlarged
rectangle is |Re z-X|<=R, |Im z|<=Y, with the original target inside its
unit buffers. Keep every frozen arithmetic mode n<=N=floor(sqrt(X/(4pi))),
the K+1 real RS coefficients, and the exact arithmetic correction S_m-S_N
inside the bounded real completion integral. No real-part operation is
moved outside a complex-kernel integral; no true RS/gamma function is
extended along artificial polynomial rays.

Retain Note11's explicit classical record without change:

    H=A=C_Gamma=c_o=1, D=4, D0=3, g_-=1/64,
    M_H^*=1/4, C_tail=640, C_chi=C_o=3^(nu-1),
    C_cal=nu+31, X_cl=64nu.                                (M3)

The real RS mismatch still costs exactly

    C_(2p)=[2^(7/4)/7] Gamma(p+1/2)
                         1.1^(2p+1)(8pi)^(p+3/4),

multiplying G(X)e^|q| X^-(p+3/4), q=u-X. Its all-positive-integer-K
validity and the separate retained-size gate K<=a_min² are unchanged.
The finite curvature/Bell remainder of Note05 G5, not a fixed-order
asymptotic with hidden constants, is used at each actual p.

Note11 U10--12's outer calibration uses T only through 0<=T<=2:
the bound for |L_z²-L²| is multiplied by T/16, and no lower bound on T
occurs. The same proof therefore gives on 0<T<=2

    E_o(-T,z)>=|G(z)| exp(-T L²/16+pi²T/64).

Thus natural-to-outer conversion costs at most exp(L²/8), with the same
c_o=1 and full-chart C_chi. The disk/slope/source constants and every
classical domain in M3 are independent of the lower time endpoint.

## 2. Joint kernel, normalization and moment costs

For z=x+iy and v=u-x the exact complex-kernel modulus is

    |k_T(z-u)|=(4pi T)^(-1/2)
                      exp(y²/(4T)) exp(-v²/(4T)).          (M4)

On 1/L<=T<=2 its normalization is at most sqrt(L)/sqrt(4pi), and its
transverse exponential at most exp(Y²L/4). For each integer a>=0 define

    P_a^L(v)=a! sum_(j=0)^floor(a/2)
       (v L/2)^(a-2j)(L/4)^j/[(a-2j)! j!].                (M5)

The exact differentiated Gaussian formula gives
|partial_z^a k_T|<=P_a^L(|z-u|)|k_T|. In particular
partial_T k_T=[(z-u)²/(4T²)-1/(2T)]k_T=partial_z²k_T,
so the direct first-time factor is L/2+L²|z-u|²/4. These are actual
inverse-time costs, not differentiated scalar error bounds.

Put f_L=exp(Y²(L-1)/4). With B=2, the explicitly integrated local
moments are

    M_m[L]=sqrt(2) exp(R+Y²L/4+4)
       sum_(k=0)^m binom(m,k)W^(m-k)4^k
                              Gamma((k+1)/2)/sqrt(pi),
    M_m^t[L]=(L/2)M_m[L]+(L²/4)M_(m+2)[L].                (M6)

To derive them, use |q|<=R+|v|, |z-u|<=W+|v| and
|v|<=v²/(8T)+2T. After integration, the normalized k-th Gaussian
moment is sqrt(2)(8T)^(k/2)Gamma((k+1)/2)/sqrt(pi); now use T<=2.
The T^(-1/2) has canceled by an actual rescaling, rather than being
omitted. The same integral bounds the moments needed for the direct time
factor by W+|v|. Consequently, for every m simultaneously,

    M_m[L]=f_L M_m[1],
    M_m^t[L]<=L² f_L M_m^t[1].                            (M7)

Note05's Bell polynomial B_(p+1) therefore keeps all degrees through
2p+2 for field and 2p+4 for direct time. The full real initial population
remains C_pop G(X)X^(1/4)e^|q|, C_pop=4(4pi)^(-1/4). Source matching and
local comparison have no extra population or inverse-time factor beyond
M6. Fixed radius-1/2 Cauchy disks cost at most48 for spatial orders0--3.

For clarity, evolved-mode moments have their own distinct ledger. With
v_n=log(a_X/n), a0=pi/8 and c_+=max((Y-1)/2,0), the same slope gates give

    |exp(T lambda²)|<=exp(2a0²+1)exp(-v_n²/(4L)).

The R3.11 shell proof (including every weakly damped cutoff shell) gives
exactly its Pi_m(1/L,2), where

    W_m(1/L)=2^m+(3^m/2) sum_(k=0)^m binom(m,k)
                         (8L)^((k+1)/2)Gamma((k+1)/2).

In particular

    Pi_m(1/L,2)<=exp(2c_+²(L-1)) L^((m+1)/2)Pi_m(1,2).
                                                               (M8)

Keep unchanged Z_m(2)=m! sum_l 2^l(W+4)^(m-2l)/[l!(m-2l)!].
The summed m-th shifted moment is <=Z_m(2)Pi_m(1/L,2)G(X)X^(1/4).
For m<=2p+5 this has logarithmic cost O_(r,b)(L log(L+2)), using
Note05's factorial bounds and M8. The factor L^((m+1)/2) is retained;
Pi_m does NOT obey the order-independent ratio in Section3. The truncation
proof integrates the real initial population in M6 before evolving modes,
so M8 is needed for the retained model/delivery but is not multiplied into
the truncation allowance. This distinction avoids counting incompatible
representations of the same population twice.

## 3. Moderate, artificial and remote tails at the moving endpoint

Use the same fixed Gaussian split theta=1/2, delta=1/4 and t_R=1+R/4.
At |q|>=V the proof of Note05 G17 gives

    -(q-Re d)²/8+|q| <=-q²/16-q²/32+8t_R².

Together with |z-u|<=2|q|, M4 and the integrated remaining Gaussian,
define the explicit refined-tail moments

    D_m[L]=sqrt(L)/(sqrt(4pi)) exp(Y²L/4+8t_R²)
                       2^m 32^((m+1)/2)Gamma((m+1)/2),
    D_m^t[L]=(L/2)D_m[L]+(L²/4)D_(m+2)[L].                (M9)

They multiply exp(-V²/16)=exp(-8L²). For remote true data keep instead
Note04 R3.14's moments at B=2, with normalization restored explicitly:

    J_m[L]=sqrt(L)/(sqrt(4pi)) exp(Y²L/4)
       sum_(k=0)^m binom(m,k)Y^(m-k)16^((k+1)/2)
                                             Gamma((k+1)/2),
    J_m^t[L]=(L/2)J_m[L]+(L²/4)J_(m+2)[L].                (M10)

The original remote Gaussian factor remains exp(pi X/8-X²/256).
Only this remote true-data term uses the complete global source mass.
The moderate term retains its height-sensitive source and X^(9/4),
and artificial rays contain only the finite exponential-polynomial
completion with its complete X^(1/4) population. Define

    Q_p[L]=48{C_(2p)M_0[L]+C_pop exp(1)B_(p+1)[M[L]]}
               +C_(2p)M_0^t[L]+C_pop exp(1)B_(p+1)[M^t[L]],
    A_mod[L]=640 max(D_0[L],D_0^t[L]),
    A_art,p[L]=C_pop max(H_p[D[L]],H_p[D^t[L]]),
    A_far[L]=16 max(J_0[L],J_0^t[L]).                       (M11)

H_p and B_m are the actual finite positive polynomials in Note05 G5--6.
Every m satisfies D_m[L]=sqrt(L)f_L D_m[1] and the analogous J identity;
the time versions cost at most another L². Thus the single multiplier

    rho(L)=L^(5/2) exp(Y²(L-1)/4)                          (M12)

dominates each ratio Q_p[L]/Q_p[1], A_mod[L]/A_mod[1],
A_art,p[L]/A_art,p[1] and A_far[L]/A_far[1], uniformly in every retained
order. It is a bound for these truncation costs, not for all evolved
moments or all complex provider magnitudes.

Reconstructing the same exact initial-data heat convolution as Note05
now proves the unabsorbed natural-norm ledger

    ||h-F||_natural <= C_chi [Q_p[L] X^-(p+3/4)
        +49{A_mod[L]X^(9/4)+A_art,p[L]X^(1/4)}exp(-8L²)
        +49 A_far[L]X^(-7/4)exp(pi X/8-X²/256)].            (M13)

The five underlying errors are source mismatch, local weighted-order
remainder, moderate true data, artificial polynomial tails and remote
true data. Source and local terms are collected in Q_p. All are bounded
before using the exact heat equation for the error. Direct time retains
its two extra tail moments; spatial errors use the existing unit buffers.

For each frozen chart the lower endpoint is strictly positive. Dominated
differentiation of its fixed bounded integral and the finite polynomial-
Gaussian transforms proves exactly (partial_T-partial_z²)F=0 and its
first z derivative=0 on a positive-time neighborhood. Selecting tau(X),
p(X) or N(X) does not introduce a derivative through that selection.

## 4. A continuous explicit all-height onset

Every structural/classical gate in Note16 S12 holds whenever L>=64nu;
M1 is stronger. Those gates involve the fixed upper endpoint2, p,K,V,
the buffers, gamma/RS domains, retained-size and separate slope/damping
gates, and so are unchanged. The outer calibration proof was explicitly
extended in Section1. There is no new window, buffer or order gate hidden
in M6--13.

For every L>=1024nu², we have L>=16384, Y<nu, and Note16 S5's
continuous logarithm bound log L<=L/32. Therefore

    log rho(L) <=nu² L/4+(5/2)log L
               <=L²/4096+5L/64<=L²/2048.                 (M14)

The last inequality needs only L>=320. This proof holds at every real
height in the range. Retain the half-target factors8,392 in Note10 C19.
Note16 S6--11 and M12--14 give

    log^+(8C_o Q_p[L]) <(3/32+1/2048)L²=193L²/2048,
    log^+(392C_o A_art,p[L]) <193L²/2048,
    log^+(392C_o A_mod[L]), log^+(392C_o A_far[L])
                                      <=65L²/2048.        (M15)

The first half-target rate gap is still
(p+3/4)log X-3L²/8>=7L²/64=224L²/2048, leaving strict slack31L²/2048.
The moderate right side costs at most
(1/4+65/2048)L²=577L²/2048, and the artificial one at most
(1/16+193/2048)L²=321L²/2048. Both are less than61L²/8.
For the remote gate Note16 S11 gives pi X/8<X²/512 and
X²/512>9L²/8>(3/8+65/2048)L². Thus all four half-target inequalities
close, so M13 uses at most exp(-L²/4)/2 after outer division.

This argument uses L/2-1<=p<=L/2 and continuous majorants, with no
monotonicity assumption on Q_p at a floor jump. The complete population
bound holds for every N, and exact adjacent-cutoff transfer is retained
at every changing cutoff. The error envelope holds through every later
p,N jump; continuity or differentiation of the actual selected F in X
is not asserted. X>=X_mov is a stronger dyadic sufficient condition,
since (2L_mov+8)log2-log(4pi)>L_mov+1.

For comparison, [1,2] was already proved at L>=64nu. The sufficient
moving-endpoint height is16nu times that log-height. This is the cost
of this simple proof, not a necessary threshold. At each fixed chart
T=1/L tends to0 as X grows, but the bound does not give a T=0 theorem,
a fixed-height limit in T, a through-zero bridge, or uniformity in
unbounded regulator radii.

## 5. Recompose every delivered-error channel

The outer conversion and half-target reservation leave the same
center-normalized evaluation budget as before:

    epsilon_X=[1/(2 C_chi)]exp(-3L²/8),
    [1/(8 C_chi)]exp(-3L²/8)<e
                     <[1/(4 C_chi)]exp(-3L²/8).           (M16)

Use rational upper enclosures and factor-controlled finite allocations
from Note09 Section7 with the following explicit substitutions.

* **Scale and arithmetic data.** Replace all M,M^t in Note06 E6--11
  by M6, recompute B_m=48M_m+M_m^t, D_p,D_p^(1), C_p,S_p and A_0.
  The exact coefficient derivative and all full-population factors in
  E7--10 are unchanged. M7 costs only log rho=O_(r,b)(L+log L).
  Complete-square carrier bounds become exp(R+2+Y²L/4). M8 pays the
  separate evolved-mode reconstruction. The slope neighborhood, every
  phase multiplier O(X), unrestricted scale exponents and all N summands
  remain. Require epsilon_g A_0<=epsilon_X/2 and E_ar<=epsilon_X/20.
* **RS coefficient/node data.** The normalized F_0/weighted-table and
  pole-safe contour constructions are independent of the heat endpoint.
  Retain every C_k. Either Note18's sharp B_F,D_k,B_c or the original
  provider is valid; its transfer-containing bound is never multiplied
  uniformly by the coefficient gain. P15's +1 and all pi errors remain.
  Recompute E22 and E25 using the new K_loc below, and require
  E_RS<=epsilon_X/20. All contour/data/node/weight errors remain paid.
* **Kernel bounds on provider domains.** Keep B_Q,B_Q^loc,a_* and the
  exact real branches/holomorphic extensions in Note06 E18,E23. Replace
  only their kernel factors by

      K_E[L]=sqrt(L)/(sqrt(4pi)) exp(L(Y+3V/4)²/4)
           [max_(a<=3)P_a^L(W+2V)+P_2^L(W+2V)],
      K_loc[L]=sqrt(L)/(sqrt(4pi)) exp(L(Y+1)²/4)
           [max_(a<=3)P_a^L(W+V+4)+P_2^L(W+V+4)].          (M17)

  Put B_E[L]=B_Q K_E[L], B_loc[L]=B_Q^loc K_loc[L], and
  A_0=C_pop X^(1/4)H_p[B]+2V B_loc[L]. These retain normalization,
  inverse-time spatial/direct-time polynomials and complex buffers.
* **Exact outer quadrature.** The same positivity/Chebyshev proof gives
  E_quad<=16V B_E[L]4^-n. Select n>=1 by the strict rational test
  16 Vbar B_Ebar[L]4^-n<e/80. It terminates and pays
  E_quad<=epsilon_X/20. With the unchanged rho=2 ellipse,

      log^+ B_E[L]=O_(r,b)(L³+L log(L+2)), n=O_(r,b)(L³).  (M18)

  In particular the old O(L²) outer-node theorem cannot simply be
  carried over. The enlarged ellipse has imaginary height O(L), which
  is squared and divided by tau=1/L. This is a cost of this sufficient
  provider, not a lower bound for quadrature or a failure of M2.
* **Geometry.** Keep exact frozen branch labels and interior rational
  guard strips. E24 remains
  B_loc[L]{epsilon_w+2(2V+epsilon_w)epsilon_u+6epsilon_b}.
  Choose the old finite tolerances with this recomputed bound so that
  E_geo<=epsilon_X/20. No real edge-equality or new floor decision is
  required. Exact reference intervals stay inside their true branches;
  no error is counted twice through mapped nodes/weights.
* **Remaining circuit.** Use E29--31 with the actual new kernel and
  carrier bounds, safe reciprocals, full accumulation count and any
  preprocessing error charged exactly once. Choose all primitive and
  operation tolerances so E_round<=epsilon_X/20. The endpoint-tag
  time-input cost in Section6 is part of this category, with an explicit
  split; rational queries have no such cost.

These are the same five evaluation categories as E5, plus scale. Each is
paid independently. Therefore epsilon_g A_0+(1+epsilon_g)sum E_i
<=epsilon_X, and adding Section4's half-target truncation proves M2.
Zero exact-model heat residual does not remove any category. Independently
computed rounded channels have only their sum-of-channel defect bound;
residual_z still requires the additional mixed channel.

On the real/local strip, log^+ B_loc[L]=O_(r,b)(L log(L+2)); likewise for
all arithmetic conditioning and positive circuit paths. Under the stated
allocations a sufficient **delivered** tolerance parameter remains

    P=3L²/(8log2)+O_(r,b)(L log(L+2)).                     (M19)

Full summation and O(L³) outer nodes add their log counts, not an L³
accuracy term. The off-real ellipse bound pays truncation only; using it
as the real-node precision bound would conflate distinct obligations.
The contour order remains O_(r,b)(L²+L log(L+2)); the direct RS-only
composition count becomes O(L^6), with the full O(Np) arithmetic work
additional. No observed speed or software validation is claimed.

Finite provider internal work changes with the larger outer Gauss order.
In particular its proved root/weight separation depths can greatly exceed
P. If an explicit loose total bound is desired, repeat Note10's degree
accounting with

    Q_mov=2+B+P+s_sigma+s_T+ceil(L)^3,
    Work<=C(r,b)(N+1)Q_mov^40,
    StreamedSpace<=C(r,b)Q_mov^20.                         (M20)

Now n,q,p,K and the gamma shift order are O(Q_mov); inverse time is
O(Q_mov) and all real-node magnitude bit lengths are polynomial in it.
Thus the same Gauss-depth O(Q_mov^4), mapped-weight O(Q_mov^5), gamma
O(Q_mov^24) per call (O(Q_mov^25) over all such calls) and remaining
O((N+1)Q_mov^35) argument fits the stated
loose exponents. B counts actual finite input/witness lengths, and
s_sigma retains descriptor-search separation. For ordinary rational
queries put s_T=ceil(log2^+(1/(T L-1))) when a lower-time witness is
searched for, and s_T=0 for the explicit endpoint tag. Verification of
supplied finite witnesses is charged by their actual length in B; the
extra separation parameter records the nonuniform cost of finding them.
The old Q with ceil(L)²
is not substituted without change. These are analytical effective bounds
for the specified arithmetic recipes, with every mode still present.

## 6. Exact query restrictions, including the mathematical endpoint

Retain Note09 P1's exact positive dyadic X,r,b, supplied p,N and strict
rational enclosures

    2p<L^-<=L<=L^+<2p+2,
    N<a^-<=sqrt(X/(4pi))<=a^+<N+1.                        (M21)

The record includes strict gate/half-target witnesses and exact rational
d=z-X inside the original buffered chart. For ordinary queries use exact
rational T<=2 and the additional finite witness

    T L^->1.                                              (M22)

Invalid finite witnesses are rejected. Every rational T>1/L has such a
witness after refinement. That search has its own nonuniform separation
T L-1; M20 counts it rather than claiming a fixed-height uniform witness
precision. No equality procedure at T=1/L, at a descriptor
boundary, or for arbitrary computable reals is claimed. A fixed rational
T below the lower endpoint is not accepted. The mathematical theorem is
uniform on the closed interval; the ordinary rational interface simply
has a specified strict input class.

There is also an explicit finite interface for the actual endpoint:
replace rational T by the literal tag **T=1/log(X/(4pi))**. This defines
one exact computable number from the already supplied exact X; it is not
an equality test on an arbitrary input. To implement it:

1. Refine positive rational L bounds to L^+/L^-<2 and L^->1. The coarse
   interval I=[1/L^+,1/L^-] then has T_- >1/(2L), T_+<2/L<=2.
2. Construct the fixed delivered-data polynomial/Gauss model at that
   query as a function of real T, with all coefficients/nodes/weights
   frozen. Its heat identity gives partial_T partial_z^a=partial_z^(a+2)
   and partial_T²=partial_z^4. Bound the derivative of every requested
   channel on I by a common rational B_T: use E31's finite spatial
   formula through order5 for the arithmetic part and M5 through order5
   with inverse time 1/T_- for each kernel node. A bound twice the maximum
   of these spatial0--5 magnitudes pays the combined requested norm.
   Positive coefficient/node bounds and the already supplied unrestricted
   exponent ranges make this a finite computable bound. This explicitly
   pays the F_TT channel needed to approximate a first-time output.
3. Refine the endpoint enclosure to width
   delta_T<e/[640(1+B_T)], evaluate at its rational midpoint and charge
   the resulting <=B_T delta_T<e/640 time-input error to E_round.
   Evaluate that circuit with the safe inverse-time bound 1/T_- on I,
   rather than reusing the tau bound at a midpoint below tau. Allocate
   the remaining new circuit/quantization error <e/160;
   together these are <e/80<epsilon_X/20. Earlier coefficient, RS-data
   and geometry payments are not charged again in this time comparison.

The midpoint can lie slightly below 1/L, but only the fixed delivered
model is evaluated there; truncation is used at the exact tagged T.
I is bounded away from0, so the derivative bound and interval refinement
terminate. For fixed charts its log-magnitude is O(L log(L+2)) by the
same finite moment/path bounds, with T_->1/(2L). Consequently this tag
requires only the M19 type of extra tolerance, counted in B and P.
The tag adds no unrestricted query-coordinate uncertainty or mixed
residual certification. Ordinary exact rational queries use M22 directly.

## 7. Assessment, controls and precise boundary

This is a quantitative approximation/evaluation milestone under
[avoid01][av1], not an RH-equivalent reformulation. Carry the
[result index][results], [heat cluster][heat], [control screen12][controls]
and [avoid index][avoid], especially [shared-premise limits][av5],
[scoped negatives][av7] and [separate bounds][av12].

The full-canonical premises are absent from the collision controls:
Euler-factor and finite-prime perturbations do not have the unchanged
complete ordinary coefficients; weighted-square, finite-cutoff and atomic
controls lack the complete canonical xi/RS completion; reflected, smooth
and positive-primitive controls lack the same complete gamma/arithmetic
identity; the RH-conditional endpoint controls lack ordinary Dirichlet
arithmetic. Shared heat recurrences survive and exclude no collision.
This is an applicability screen, not a claim that every derived upper
estimate rejects every control or that an approximation error implies RH.

The attempted class here is exactly fixed buffers, tau=1/L, B=2,
p=floor(L/2),K=2p and V=8sqrt(2)L. Every displayed required inequality
closes for that class. The preserved failed shortcut is carrying over
O(L²) outer nodes on the unchanged rho=2 ellipse without paying the
exp(O(L³)) kernel bound. No impossibility of O(L²) rules, other time laws,
through-zero continuation or actual error lower bound is proved.

**Disposition:** AN08 r1 is Complete/CLOSED at its bounded analytical
scope following Review14. Broad R05 stays Partial at complete evaluator
software/certification. R04/R06 NOT_STARTED, HDA-A02 Partial, HDA-17
Partial, HDA-18 Gated and HDA-20 unfulfilled remain. N02's separate
finite matrix/caps are unchanged and it is not executed. Same-model
read-only checking does not supply independent specialist review. Primary
PartI access and PartII identity-only qualifications in the source audits
remain. No new imported classical theorem or primary-proof validation is
claimed. The original [1,2] result and original provider remain fallbacks.

Next concrete deliverable, **Analysis — Sol:** the existing
[corrected physical-consumer packet][consumer], owned by its ansatz
register. It must pay an actual observable with explicit rates; the
new moving-endpoint approximation does not close that consumer.

[consumer]: ../../ansatz/research-progress/handoffs/HDA-A03-AN02.md
[inputs]: 20_MOVING_ENDPOINT_INPUTS_20261026.json
[work]: 20_MOVING_ENDPOINT_WORK_RECORD_20261026.json
[review]: ../reviews/14_MOVING_ENDPOINT_ASSESSMENT_20261026.md
[results]: ../../../../../result-summaries/README.md
[heat]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[av1]: ../../../../../avoid/01_restating_the_target.md
[av5]: ../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[av7]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[av12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md

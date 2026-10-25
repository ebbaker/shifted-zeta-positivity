# Exact phase index by four admissible binary onsets

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol, actual recorded effort ultra**,
chat0021. Analytical continuation of Note59 EV21. The author explicitly
clarified: **“Use existing onset freedom.”**

## 1. Result and exact scope

The literal phase ceiling can be constructed without an equality oracle
when Note54's existing freedom to choose a sufficiently large binary
onset is retained. Take a certified integer upper bound K on every
required onset-exponent threshold, including **all** of that note's
compact, positive-join and
pre-switch bridge gates, and enlarge it to K>=2048. Among the four onsets

    U_j=2^(K+j), 0<=j<=3,

at least one satisfies

    dist(Theta(64,U_j)/pi,Z)>1/100.                    (PI1)

A specified finite rational calculation selects a candidate, then
returns its **exact literal** n=ceil[Theta(64,U_j)/pi]. It uses only
elementary constants, an explicit full-saddle remainder, and exact
rational comparisons. No gamma or implicit-phase evaluator is needed
for this discrete selection. The subsequent phase inverse is Note59's
already effective fixed-index inverse.

The selector costs at most 2^100(P_*+1)^10 schoolbook bit operations
and 2^20(P_*+1)^3 working bits, where

    P_*=K+3+ceil log_2(K+4)+20.                        (PI2)

These deliberately loose bounds are polynomial in K, hence in the
binary height length. They are not polynomial in the binary encoding
length log K, nor a complexity bound for the entire IC23 construction.

This constructs a member of the original IC23 family, using the
authorized free onset before fixing its X0 and source. Every IC23
formula, including the literal ceiling rule, is retained. It does not
recover the phase index of a tuple whose particular K had already
been irreversibly prescribed. No equality decision or non-equality
theorem for every individually prescribed dyadic height is asserted.

The [input manifest](60_EXACT_PHASE_INDEX_INPUTS_20261025.json) pins
the opening sources. [Note59](59_EVALUATOR_WORKING_PRECISION_AND_CONTINUOUS_FILTER_20261025.md)
supplies the evaluator ledger; [Note54, C4 and D](54_EFFECTIVE_POSITIVE_ATTACHMENT_AND_ALL_TIME_EXISTENCE_20261025.md)
supplies the onset freedom. This is a quantitative construction milestone,
not an RH-equivalent criterion, a sign theorem or a collision exclusion.
See the [established-result index](../../../../result-summaries/README.md),
[heat-flow cluster13](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
[collision controls12](../../../../result-summaries/12_collision_controls_and_screening.md),
and [avoid index](../../../../avoid/README.md), specifically
[target restatement01](../../../../avoid/01_restating_the_target.md),
[shared-premise controls02](../../../../avoid/02_shape_only_arguments_and_the_controls.md)
and [scoped exclusions07](../../../../avoid/07_scoped_exclusions_read_as_universal.md).

## 2. An explicit phase expansion for the actual gamma saddle

Here log denotes the natural logarithm and log_2 the binary logarithm.
Use exactly the normalized analytic logarithm in Note59 EV11, with the right-half-plane
log Gamma and the determinant logarithm near1. In particular Theta is
the imaginary part of the **unwrapped** arm logarithm, not the principal
argument of a tiny computed arm value. At t=64 set

    w=(1+ix)/2, M(p)=p(p-1) pi^(-p/2) Gamma(p/2)/16,
    alpha=M'/M, p=w+32alpha(p), v=p-w,
    B=1-32alpha'(p),
    log S=log M(p)-v^2/64-(1/2)Log B,
    Theta(64,x)=Im log S.                            (PI3)

We prove, for x>=exp(1000), writing lambda=log x and
L=log(x/(4pi)),

    Theta(64,x)=x(L-1)/4+4pi L+7pi/8+E(x),
    |E(x)|<=2^16(1+lambda)^2/x.                      (PI4)

This expansion includes the shift of the **implicit full gamma saddle**;
an expansion of a fixed or linear-gamma saddle would not suffice.

### 2a. Paid branch and gamma remainder

[Note45 EF3--EF6](45_EFFECTIVE_FULL_BUFFER_OUTER_FIELD_20261025.md)
at the actual saddle give

    Re p>2, |p|>=x/2, |v|<=32lambda,
    |alpha(p)-(1/2)Log(p/(2pi))|<=4/x,
    |B-1|<=97/x.                                    (PI5)

The loose v bound follows from its t=64 real and imaginary bounds.
We apply EF3 only at p; w has real part1/2 and is outside its stated
right-half-plane domain.

For F(z)=(z/2)[Log(z/(2pi))-1], the Stirling identity at Re p>2 is

    log M(p)=F(p)+(3/2)Log p+c_real
                 +Log(1-1/p)+R1(p/2),
    c_real=log(sqrt(pi)/8),
    |Log(1-1/p)|<=4/x, |R1(p/2)|<=4/x.              (PI6)

For the remainder, [DLMF 5.11(ii)](https://dlmf.nist.gov/5.11#ii)
bounds the one-term log-Gamma remainder by
sec^2(arg(z)/2)/(12|z|). At z=p/2, |arg z|<pi/2 and |z|>=x/4,
so the displayed 4/x is ample. The other bound uses |1/p|<=2/x
and the convergent log(1-z) series. The identity, with this exact
logarithm, first holds for real p>2 and then throughout Re p>2 by
analytic continuation. There is no undetermined multiple of 2pi i.

### 2b. Expand from q=ix/2, without applying EF3 there

Put q=ix/2, h=p-q=v+1/2 and

    alpha0=(1/2)Log(q/(2pi))=L/2+i pi/4.

We have |h|<=64lambda and, on the segment from q to p,
|z|>=x/4. This follows since 64lambda<=x/4 in the stated range;
the segment avoids the logarithm cut. As F''(z)=1/(2z),

    |F(p)-F(q)-alpha0 h|<=|h|^2/x<=4096lambda^2/x,
    |Log p-Log q|<=4|h|/x<=256lambda/x.             (PI7)

The comparison of alpha with alpha0 uses PI5 **at p** and the
second bound, not an asymptotic assertion at q:

    |alpha(p)-alpha0|<=128lambda/x+4/x<=129lambda/x,
    |v-32alpha0|<=2^13 lambda/x.                    (PI8)

Complete the square exactly:

    alpha0 v-v^2/64=16alpha0^2-(v-32alpha0)^2/64.

Its last term is bounded by 2^20lambda^2/x^2<=lambda^2/x.
Also |(1/2)Log B|<=97/x, by |B-1|<=97/x<1/2.
Substituting PI6--PI8 into PI3 gives

    log S=F(q)+alpha0/2+(3/2)Log q+16alpha0^2+c_real+R,
    |R|<=4097lambda^2/x+384lambda/x+105/x
         <5000lambda^2/x<=2^16(1+lambda)^2/x.       (PI9)

The imaginary parts of the four nonconstant terms are, respectively,

    x(L-1)/4, pi/8, 3pi/4, 4pi L.

Their sum proves PI4. The 4pi L term is the payment for the saddle
displacement; the constant 7pi/8 follows from the same EV11 phase
normalization. Even a known global integer-pi relabeling would preserve
integer distances and the block combination below, but no relabeling
is being introduced.

## 3. Four consecutive dyadic phases cannot all be near integers

Define Q_ell=Theta(64,2^ell)/pi. PI4 and pi>1 imply

    Q_ell=A_ell+r_ell,
    A_ell=2^(ell-2)/pi [(ell-2)log 2-log pi-1]
               +4[(ell-2)log 2-log pi]+7/8,
    |r_ell|<=2^16(1+ell log 2)^2 2^(-ell).           (PI10)

For K>=2048 the functions (1+lambda)^2 exp(-lambda) decrease,
lambda=K log 2>K/2>=1024. Since exp(lambda)>=lambda^8/8!,
(1+lambda)^2<=4lambda^2 and 8!<2^16,

    |r_(K+j)|<2^34/lambda^6<=2^-26, 0<=j<=3,
    18 max_j|r_(K+j)|<2^-21<1/100.                 (PI11)

Consider the **integer** linear combination

    D=Q_(K+3)-5Q_(K+2)+8Q_(K+1)-4Q_K.             (PI12)

For c=(-4,8,-5,1), indexed by j=0,1,2,3,

    sum c_j2^j=0, sum c_j j2^j=0,
    sum c_j=0, sum c_j j=1, sum |c_j|=18.

The two terms of the form (a j+b)2^j and the constant cancel in
PI10. Hence

    |D-4log 2|<1/100.                                (PI13)

For completeness the positive series
log 2=2 sum_(r>=0) 3^(-2r-1)/(2r+1) proves
2/3<log 2<=2/3+1/36=25/36<7/10. Thus

    8/3-1/100 < D < 14/5+1/100,
    dist(D,Z)>19/100.                              (PI14)

If m_j is any nearest integer to Q_(K+j), then

    dist(D,Z)<=|sum c_j(Q_(K+j)-m_j)|
              <=18 max_j dist(Q_(K+j),Z).

Consequently the maximum is >19/1800>1/100, proving PI1.
There may be equality at some rejected candidate; the proof neither
needs nor tries to decide it. The quantified conclusion is **one
separated member of every sufficiently high four-onset block**.

## 4. A fully specified finite rational selector

We now expose a separated member with fixed precision, including all
elementary-constant errors. For ell=K,K+1,K+2,K+3 put

    P=ell+ceil log_2(ell+1)+20, N=P+10.               (PI15)

Compute the following **finite rational expressions**. These are an
algorithm specified on paper; no such computation was executed here.

### 4a. Elementary constant providers

Machin's identity supplies

    pi_N=16 sum_(r=0)^(N-1) (-1)^r/[(2r+1)5^(2r+1)]
          -4 sum_(r=0)^(N-1) (-1)^r/[(2r+1)239^(2r+1)].

The identity follows by the rational tangent addition law for
4 arctan(1/5)-arctan(1/239)=pi/4 with all angles in the indicated
positive branch. The alternating tails give
|pi_N-pi|<20*25^(-N)<2^(-P-6). Round pi_N to the nearest multiple
of 2^(-P-4), ties to even, and call the result pihat. Then

    |pihat-pi|<2^(-P-4), 3<=pihat<=4.              (PI16)

Both 3 and4 are rounding-grid points. Since 3<pi<4 and the
truncation error is smaller than half a grid step, rounding cannot
leave [3,4]. Rounding here is essential for the sharper operand bound below.
Put

    ahat=2 sum_(r=0)^(N-1) 3^(-2r-1)/(2r+1),
    rho=(pihat-1)/(pihat+1),
    bhat=2 sum_(r=0)^(N-1) rho^(2r+1)/(2r+1).

We have 1/2<=rho<=3/5. The atanh-series tails are at most
3*9^(-N) and 4*(9/25)^N respectively. The second is
<2^(-P-8); moreover
|log pihat-log pi|<=|pihat-pi|/3. Therefore

    |ahat-log 2|<2^-P, |bhat-log pi|<2^-P.           (PI17)

All providers have fixed term counts and exact integer/rational rules;
no comparison with an unknown-real endpoint or equality search occurs.

### 4b. Rational phase centers and acceptance

Form the exact rational numbers

    Lhat=(ell-2)ahat-bhat,
    qhat=2^(ell-2)(Lhat-1)/pihat+4Lhat+7/8,
    I_ell=[qhat-1/1000,qhat+1/1000].                (PI18)

Let L=(ell-2)log 2-log pi and d=2^-P. Then
|Lhat-L|<=ell d, |Lhat-1|<=2ell, and
|1/pihat-1/pi|<=d/9. It follows, using 2^ell>=8, that

    |qhat-A_ell|<=2^ell ell d<2^-20,
    |qhat-Q_ell|<2^-20+2^-26<2^-19.                (PI19)

Thus I_ell encloses the **exact** Q_ell with a much larger radius
than needed. One candidate has distance >1/100 from Z. Its entire
interval consequently has distance

    >1/100-2^-19-1/1000>1/200                       (PI20)

from Z. For each ell in increasing order, compute the integer
n=floor(lower(I_ell))+1 using rational integer division, and accept
this ell if the two rational strict comparisons

    n-1+1/200 < lower(I_ell),
    upper(I_ell) < n-1/200                          (PI21)

both hold. An exact tie in either comparison means rejection and
costs no extra precision. PI20 guarantees that at least one of the
four candidates passes. Choose the first **passing rational test**,
not the first exact phase that is noninteger. This distinction avoids
reintroducing the equality problem during winner selection.

For the winner ell*, define k*=ell*, U0=2^k* and take that n. Since
Q_(ell*) belongs to I_(ell*), PI21 proves

    n-1+1/200 < Theta(64,U0)/pi < n-1/200,
    n=ceil[Theta(64,U0)/pi].                        (PI22)

The acceptance margin is explicit, while the much smaller enclosure
error is paid independently. This returns the literal integer, not
a safe upper integer used as a substitute for the ceiling.

## 5. Finite bit and storage bound for this discrete step

Let P_* be PI2. For each P<=P_*, N=P+10<=2P. Common integer
denominators for the two Machin sums and the log 2 sum can be taken as

    Q_pi=(2N)!5^(2N)239^(2N),
    Q_2=(2N)!3^(2N).

After the specified dyadic rounding, write rho=R/S. Its numerator
and denominator have at most P+8 bits. A denominator for the finite
log pihat sum is

    Q_log=(2N)! S^(2N).

Indeed every 2r+1 divides (2N)!, and each remaining power divides
the corresponding base power. These products, powers, scaled summands,
partial sums and final PI18 numerator/denominator fit the generous
integer operand cap

    L_op=2^10(P_*+1)^2 bits.                        (PI23)

For example log_2((2N)!)<=2N log_2(2N), and
log 2 Q_log<=2N(P+8)+2N log_2(2N), both well inside PI23.
Multiplying by 2^ell adds only ell<=P bits. Division for rounding
and floor, and the rational comparisons, use operands of the same
bounded order. We can retain unreduced common-denominator fractions;
no gcd oracle is needed.

Stream the powers and summands. Fewer than
2^10(P_*+1)^2 integer additions, multiplications or divisions suffice
for the four candidates and their comparisons, with ample room for
factorial and power construction. Schoolbook integer arithmetic costs
at most a fixed multiple of L_op^2 per such operation. Therefore the
following deliberately inflated bound pays all steps:

    C_select<=2^100(P_*+1)^10 bit operations,
    S_select<=2^20(P_*+1)^3 working bits.            (PI24)

Only a bounded number of operands need be live. The returned integer
n has O(K+log(K+1)) bits, because PI10 bounds |Q_ell| by a constant
times 2^ell(ell+1). The value U0 is represented either as the exact
power-of-two descriptor or with its K+4 binary bits.

Constant **absolute** phase tolerance has not been mistaken for
constant working precision: the leading phase has magnitude of order
2^K K, and PI15 explicitly pays O(K) bits of elementary constants.
If pi_N were used as an unreduced rational inside log pi_N, rather
than rounded first, the simple denominator proof could grow to
O(P^3) operand bits. The specified rounding prevents that issue.

PI24 excludes finding the original sufficient K and excludes phase
inversion, source construction and subsequent observable evaluation.
Those are separately finite algorithms in Notes54,58,59 from their
specified input data. PI24 is an additive finite payment for the
previously missing discrete phase step, not a claim that the complete
tuple is cheap.

## 6. Consume the authorized freedom without changing IC23

Use Note54 D's actual noncircular order: fix eta,theta, determine the
uniform late constant C_+ and T_+, fix b=T_++1 and delta=theta/64,
and determine the negative-join T_-, K_mid and K_bridge. In the C4
onset formula use **C_b^+=(1+c_b)C_b and target delta**, not the
unenlarged C_b or original target. Let K be a certified integer upper
bound, with the original permitted slack, for the maximum of

    16384+ceil log_2(4Rstar_b+4Dmov_b+1024)
          +ceil[8log_2(2+C_b^+/delta)],
    16384+ceil[8log_2(2+2^64 K_bridge/delta)],
    2048.                                          (PI25)

Include any already declared auxiliary onset gate as well. For these
sufficient bounds, upper integer approximations with positive slack
are permitted; their evaluation requires no exact-real ceiling rule.
The first term is C4 with D's positive-band enlargement, and the second
is D's pre-switch bridge maximum. Neither may be omitted.

Every k>=K retains all the monotone gates: with its own X0 obtained
from the original ceiling/inverse, a_X>=2^(k-1), L<=k+3,
C_b^+<=delta 2^(k/8), (k+3)^8<=2^(k/2), and the remaining
exponential/gap inequalities become stronger. Branch and buffer lower
gates remain true. Thus all four candidates are admissible, and the
winning U0 lies between 2^K and 8*2^K.

Select the winner by Section4 **before** fixing X0 or any X0-dependent
object. Use the original exact inverse

    Theta(64,X0)=npi.

Its derivative lower bound and PI22 give the inherited forward bracket;
the conservative Note59 bracket U0<=X0<=U0+32 suffices. Its interval
inverse terminates at every requested accuracy without deciding root
equality. Then follow the same moving phase over [63,b]. Define
Dmov_b, a_X,R_c,L,sigma and the cutoffs from this X0 exactly as before,
and choose the same full IC23 source tolerance, including **all**
EA7/core/direct-collar/negative/bridge/late demands. Construct Note58's
positive source and use Note59's full evaluator/filter ledger.

No source is chosen for one candidate and silently reused at another.
There remains one source, fixed in time and height for the resulting
tuple. The regulator, averaging kernel, actual covariance/Delta Q,
nonholomorphic and temporal defects, both curvature rows, every
real-time/height domain and both endpoint error comparisons are those
of the inherited construction. The new work selects its allowed
onset; it introduces no physical cutoff or new approximation term.

Combined with the preceding finite provider recipes, this removes
EV21 as an unpaid input **for construction with authorized free onset**.
It leaves no equality branch within this selector and no need for a
special-function equality certificate. This does not upgrade the
finite construction to useful cost or executed arithmetic acceptance.

## 7. Controls, limits and continuation

The dyadic lemma concerns an explicitly normalized gamma-model phase.
It asserts no zero separation, positivity of a signed density or
absence of a collision. Smooth colliding controls can share the same
gamma completion and hence the same phase-index selector. That is
consistent with the theorem; it is not evidence of collision exclusion.
For the full IC23 application, Euler-factor controls alter the completed
source identity; weighted-square and finite-prime controls lack the
full canonical coefficient/reflection premise; reflected, shape and
primitive controls lack the complete theta-source identity; atomic
and heat-polynomial controls lack that smooth full source. These are
premise checks from controls12, not new control computations or claims
that no control can satisfy a subset of the premises.

The previously fixed-K equality problem is outside this positive result;
we assert neither equality, impossibility nor uncomputability there.
Note59's first-unpaid statement remains the historical finding for its
then-unclarified scope. This note supplies its missing payment using
the author's subsequent explicit scope clarification.

The remaining analytical acceptance issue is **useful complete cost**:
Note59 EV14--EV20 uses a compact physical q floor that can force
quadratic-height working bits and exponentially large generic midpoint
counts. Its gamma/profile providers are also crude. No lower bound or
universal quadrature obstruction follows. The next useful estimate is
a carrier-aware error/integration bound for the same complete tuple,
including covariance and every defect, improving that inverse-q loss.

**Next: Analysis — Sol.** Pursue that named estimate and efficient
providers, keeping all endpoint/domain/source demands. The discrete
phase selection is closed at the stated free-onset scope. **HDA-17
Partial, HDA-18 Gated, HDA-20 unfulfilled** remain; same-model internal
inspection in [Review39](../reviews/39_EXACT_PHASE_INDEX_ASSESSMENT_20261025.md)
is not the distinct full inherited-chain review.

Zero numerical, exact-rational or machine-symbolic research runs were
performed. No source/theta/gamma/field samples, evaluated phase index,
coefficient generation, precision search or interval campaign occurred.
All finite algorithms, constants and costs above were derived on paper.
Housekeeping hashes, local links and chat capture are not mathematical
certificates. The [small work record](../numerics/EXACT_PHASE_INDEX_ANALYTICAL_WORK_RECORD_20261025.json)
records this scope. Manuscript and DRAFT_HISTORY are unchanged; no
snapshot, commit, new user-owned chat or model change.

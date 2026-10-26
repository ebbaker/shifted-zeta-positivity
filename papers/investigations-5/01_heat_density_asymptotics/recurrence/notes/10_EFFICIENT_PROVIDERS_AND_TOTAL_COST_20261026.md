# R05-AN04: polynomial provider bounds, total work, and onset dependencies

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual effort ultra**,
verified from current turn metadata. Recurrence chat0003, thread
`01a176ea-3f14-7972-bc9c-9aeb6fb50fd4`, turn
`01a17702-fef2-7243-a875-7599ca03eb5e`.

**Return to HDA-R05-AN04 r1. Proved in-note from the named inputs;
same-model internal assessment only.** The two expensive constructions
in [Note09][n9] can be replaced without changing their delivered errors:

- shifted Stirling evaluation uses O(P+J) terms/shifts for log-gamma
  and normalized jets through J, instead of O(X² 2^P) Euler terms;
- exact Legendre variation counting replaces the exponential Gauss mesh
  scan by polynomial bit work, with certified nodes and weights;
- with fixed chart radii and a valid fixed calibration record, all work
  admits an effective **(N+1) times a polynomial** upper bound in input
  length, delivered precision, log-height and center separation. Modes
  can be streamed, giving a polynomial storage bound independent of N.

Here P denotes the delivered accuracy parameter of a particular call;
Section 5 defines a uniform maximum for composition. There is no
numerical execution, machine-symbolic check, implemented evaluator,
measured cost, or useful-runtime certificate. The total outer target
remains exp(-L²/4), conditional on the inherited comparison/calibration
facts and half-target truncation gates. A universal numerical starting
height remains unpaid because several uniform calibration constants and
their domains/onsets remain symbolic. A finite height verifier and some
explicit structural payments are supplied below.

[Review08][review], [execution inputs][inputs], [work record][work] and
[Source Audit04][sources] delimit the evidence. AN04 r1 is **CLOSED at its
bounded analytical scope**; broad R05 remains **Partial**.

## 1. Unchanged model and finite arithmetic convention

Keep Note09 P1's certified dyadic centers and exact rational queries on
the full buffered chart, its positive calibration bounds, comparable
dyadic budget and frozen descriptors/guard strips. In particular
L=log(X/(4pi)), p=floor(L/2), K=2p, N=floor(sqrt(X/(4pi))),
V=8sqrt(2)L, 1<=T<=2. Retain the canonical xi/theta source, both arms,
every n<=N, every C_k through K, exact cutoff transfer and bounded real
RS integral. All chart/coefficient/partition data stay fixed under z,T
derivatives. Field, spatial orders 0--3 and first time are paid separately.

Use binary integers and elementary multiplication and division of B-bit
integers charged O(B²) bit operations. Individual rational expressions
use explicit denominators and exact integer operations; accumulated
approximate quantities are rounded to a common dyadic grid and summed
as integers. Thus an uncontrolled product of rational denominators is
not assigned unit cost. Positive separation is checked before division.
Primitive errors and final circuit errors retain Note06/09's categories.
Integer exponents for the common scale are stored separately.

The real/complex log, pi, square root and reduced exponential series of
Note09 Section 3 have geometrically or factorially bounded tails. For
b-bit rational input and requested P-bit output in the stated reduced
log/phase/square-root models, their work is polynomial in b+P. Exponentials
use reduced arguments and relative mantissa accuracy. Requesting absolute
2^-P error after rescaling an exponential additionally costs
ceil(log2^+|exp(a)|) mantissa bits; that magnitude term is retained in
the normalized circuit ledger. This is not a polynomial absolute-error
claim for arbitrarily large unrestricted exp(a). For example a
reduced logarithm/atan series has M=O(P+b) terms. If its rational argument
is a/q, evaluate the terms with the explicit common denominator
q^(2M+1)(2M+1)!; its bit length is O((P+b)²). This gives a conservative
O((P+b+10)^6) bit bound and polynomial storage. Square roots use rational
square comparisons and bisection, also within this bound. Reduced Taylor
exponentials have a similarly explicit factorial denominator. Range
reduction and relative-error conversion retain the true large phase
and scale multipliers; there is no unit-cost transcendental oracle.

## 2. A short log-gamma construction with uniform jet remainder

For real rational u>0 let z=(1+iu)/4. Given epsilon=2^-P, P>=1,
and jet order J>=0, set

    m=P+2J+4,  a=m+1,  W=z+a,
    S_m(W)=(W-1/2)Log W-W+log(2pi)/2
             +sum_(k=1)^(m-1) B_(2k)/[2k(2k-1)W^(2k-1)].       (C1)

Use the analytic log-gamma on the right half-plane, fixed by its real
positive values. The checked [DLMF5.11(ii)][stirling] complex remainder,
after k=m-1, is bounded by the magnitude of the first omitted term times
sec(arg(W)/2)^(2m). The [Bernoulli Fourier formula][bernoulli] at x=0
and sum k^-2m<=2 give |B_(2m)|<=4(2m)!/6^(2m), since pi>3.
For Re W>=m, |arg W|<pi/2 and |W|>=m. Therefore

    |log Gamma(W)-S_m(W)|
      <= 2^m *4(2m)!/[6^(2m)2m(2m-1)m^(2m-1)]
      <= (2/9)^m/m <= 4^-m/m.                               (C2)

The factorial bound used in the second line is
(2m-2)!<=(2m)^(2m-2). This is a finite remainder estimate for each
actual m, not substitution of a growing m into an unquantified asymptotic.

On the disk |s|<=1/8, Re(W+s)>m and Re(z+s)>0. Shift back exactly:

    log Gamma(z+s)=S_m(W+s)
                  -sum_(h=0)^(a-1) Log(z+h+s)+R_m(W+s).      (C3)

The identity follows from the gamma recurrence on the positive real
axis and analytic continuation; no integer phase ambiguity is introduced.
Cauchy on this fixed disk bounds every normalized derivative remainder:

    |[s^j]R_m(W+s)|<=8^j 4^-m/m <=2^(-P-8), 0<=j<=J.         (C4)

Thus all normalized jets, including the value, have one explicit common
truncation payment. Only O(P+J) shifts and Stirling terms are required.

All finite coefficients are explicit. With q_k=2k-1,

    [s^j](W+s)^(-q_k)=(-1)^j binom(2k+j-2,j) W^(-2k-j+1),
    [s^j]Log(z+h+s)=(-1)^(j-1)/[j(z+h)^j], j>=1.             (C5)

For the leading part put L_0=Log W and
L_j=(-1)^(j-1)/(jW^j), j>=1. Its coefficients are
(W-1/2)L_0-W+log(2pi)/2 at j=0,
(W-1/2)L_1+L_0-1 at j=1, and
(W-1/2)L_j+L_(j-1) at j>=2. Subtract every shift coefficient.
Only a+1 complex logarithms plus log(2pi) are needed; the remaining
coefficient work is O((P+J)J), plus Bernoulli preprocessing.

For an explicit rounding allocation, set T=a+m+J+10 and choose the controlled rational
U_W=a+1+(|u|+1)/4>=|W|. Deliver Log W to error epsilon/[64(1+U_W)], log(2pi) to
epsilon/32, and each shift Log(z+h) to epsilon/(64a). Compute every
rational term in C5 exactly, round each real/imaginary component finely
enough for complex error <=epsilon/(64T), then sum dyadics exactly.
There are fewer than T terms in each jet. The logarithm errors, rational
term rounding, final quantization and C4 sum to less than epsilon.
All denominators z+h have modulus >=1/4; W has still larger separation.
These explicit allocations certify the internal errors, before delivery.

For completeness, the coefficient sizes do not hide exponential
arithmetic precision. Because m>=J, the binomial factor in C5 divided
by |W|^j is at most 3^j/j!<=exp(3)<27. Combining this with the
Bernoulli bound bounds each Stirling correction coefficient by
27/(m 9^k). Shift-jet sums have magnitude <=a4^J; the leading value
has magnitude O((1+|u|+m)log(2+|u|+m)). The required dyadic width is

    P+O(log(2+|u|)+J+log(P+J+2)),                            (C6)

including large integer parts and the guards in the above logarithm
requests. This is a sufficient internal dyadic-width statement for this
provider. Exact rational temporary operands can be larger, as counted next.

Let b encode u's numerator/denominator lengths, and t=P+J+b+10.
Generate Bernoullis with their exact triangular recurrence. Their
denominators divide (n+1)!: clear that factorial in
sum_(k=0)^n binom(n+1,k)B_k=0 and use induction. The classical Bernoulli
bound then bounds numerators and partial sums by O(t log t) bits.
Exact powers up to 2m+J use O(t²)-bit integers; the explicit elementary
series denominators above also have O(t²) bits. O(t²) integer operations
suffice with cached powers and termwise dyadic accumulation. Process one
shift-power array at a time, retaining only the shared W-powers and jet
accumulators rather than caching all shifts simultaneously. Consequently
one conservative bound is

    GammaWork(P,J,b)=O(t^6) bit operations,
    GammaSpace(P,J,b)=O(t^3) bits.                           (C7)

This replaces Note09's exp(P+O(log X)) term count. It is an analytical
upper bound, not a measurement. The elementary slow fallback remains valid.

Use exactly Note09 P8 and its log differences to obtain ell, beta,
lambda, c_r and the RS amplitudes. At the center J=p+1; at outer real
nodes only J=0 is needed. E10's log n accuracy of order epsilon_beta/X,
log pi's multiplied phase error, scale log2 precision and arbitrary
integer exponent encoding remain. Apply C1--7 at the tighter actual
requested tolerance. No normalized coefficient or scale payment is waived.

## 3. Polynomial Gauss root and weight construction

Use Note09's exact Legendre polynomials P_s, simple interior roots,
reference positive weights and conditioning constants. For x in [-1,1]
let V_s(x) count sign variations in (P_s(x),...,P_0(x)), omitting zeros.
The three-term recurrence and derivative identity are

    (k+1)P_(k+1)=(2k+1)xP_k-kP_(k-1),
    (1-x²)P_s'=s(P_(s-1)-xP_s).                             (C8)

They follow from Rodrigues' coefficient formula; the selected primary
identities were also checked at [DLMF18.9 Table1][legendre] and
[DLMF14.10.5][legendreder]. Adjacent polynomials have no common root,
since the recurrence would propagate one to P_0=1. At an internal-chain
zero the two neighbors are opposite; variation is unchanged across it.
At a P_s root, the derivative identity shows that P_s' and P_(s-1)
have the same sign. V_s decreases by one, and omitting the leading
zero gives its right limit. Therefore the exact open-interval root count is

    C(A,B)=V_s(A)-V_s(B)-1_(P_s(B)=0).                       (C9)

This convention handles exact dyadic endpoints/midpoints. Multiple
nonadjacent zeros in the chain do not alter the argument: their
adjacent-pair variation contributions add. V_s(-1)=s, V_s(1)=0.

Maintain open dyadic intervals with positive C count. Bisect, record any
midpoint root as a singleton, count both children by C9, and discard
zero-count children. There are at most s active intervals at each depth;
through depth h the work is O(sh) variation queries, replacing an
exponential mesh scan.

All signs use integers without rational coefficient swell. Define
A_k=2^k k!P_k. At x=c/q, q=2^v>0, compute

    b_k=q^k A_k(c/q),  b_0=1, b_1=2c,
    b_(k+1)=2(2k+1)c b_k-4k²q² b_(k-1).                     (C10)

Positive normalizations preserve signs. Rodrigues bounds
||A_k||_1<=(k+1)2^k(2k)^k. Thus each query has O(s) integer operations
on O(s(v+log(s+2)))-bit operands. Signs can be streamed in ascending
order; reversal does not change the variation count.

Reuse Note09's rational separation sigma_s, derivative lower bound d_s,
S_2, J_*, J_1 and weight Lipschitz bound L_w. Their conditioning bit
lengths are O(s³ log(s+2)); in particular log(1/sigma_s)=O(s²log(s+2)).
For optional delivered-weight positivity let S_1=sum_j j|[x^j]P_s|.
The nodal Lagrange polynomial has |l_i'|<=s S_1/d_s and l_i(xi_i)=1.
Integrate its square toward the farther endpoint to get

    omega_i>=mu_s=1/[4 max(1,2s S_1/d_s)].                   (C11)

For requested base-node error eta_x and total base-weight error eta_w,
choose rational

    delta_*=min(1/8,sigma_s/4,d_s/[4 max(1,S_2)],eta_x,
                  eta_w/[2s max(1,L_w)],mu_s/[2 max(1,L_w)]).

Select h by 2^(1-h)<=delta_*. Remaining intervals then isolate single
roots; their rational midpoints deliver eta_x and total weight error
below eta_w by Note09 P11. Singleton roots use exact rational evaluation.
Positive delivered weights follow from C11. If P_samp bounds the two
requested negative log tolerances and ell is affine/tolerance input
length, this gives

    h=O(P_samp+ell+s³ log(s+2)).                             (C12)

There is no root-separation oracle or undecided equality step.

For weight bit lengths form the integer polynomial

    Q_s(c)=s! integral_(-1)^1 [A_s(t)-A_s(c)]/(t-c) dt.

Its coefficient formula is
[c^r]Q_s=2 sum_(j>r, j-r odd) [t^j]A_s *s!/(j-r).
Both Q_s and A_s have O(s log(s+2))-bit coefficients. The rational
midpoint weight is

    omega_hat=Q_s(xi_hat)/(s! A_s'(xi_hat)).                  (C13)

Homogeneous evaluation at xi_hat=c/q cancels the common q^(s-1);
the numerator and denominator have O(sU_s) bits, where

    U_s=P_samp+ell+s³ ceil(log2(s+2))+10.

Root counting, coefficient formation, conditioning constants, all weights,
optional fraction reduction and affine mapping satisfy the conservative
schoolbook bounds

    GaussWork(s)=O(s^4 U_s^3),
    GaussSpace(s)=O(s² U_s).                                (C14)

Indeed O(sh) queries each use O(s) operations on O(s(h+log s))-bit
integers. Coefficient and weight work fit the same bound. Exact rational
interior endpoints use Note09 P12: prescribe base errors divided by
1+overline V, and split total weight error over the at most two branches.
Four contour edges use their exact complex affine scales. No division
by a short branch length appears. Freeze every label and partition.
The same base rules are reused on all relevant intervals/edges.

## 4. Error accounting after replacement

Note09 Section 7's comparable e, positive majorants and allocations are
unchanged. Use C1--7 at its scalar/gamma tolerances; C12--14 supply its
physical node/weight errors; retain every normalized contour derivative
and weighted coefficient in P13--15. Its E27 contour truncation and
E20 outer quadrature errors are unchanged. Replacing a provider by a
construction with the same certified delivery error preserves E5,
E9, E21--29 and the total exp(-L²/4) implication.

For a finite precision circuit, choose a dyadic grid for each nonlinear
primitive and use the explicit series tail and input-perturbation bound.
Evaluate individual exact rational terms, quantize, and accumulate
linear sums as dyadic integers; each quantization gets its own error
allocation. Product/moment/polynomial channels use E29 with actual
magnitude bounds and positive path sums from E15/E31. For a sum of S
terms, total quantization error is <=S times the per-term allowance;
its extra fractional precision is ceil(log2 S), not S. All N arithmetic
modes are accumulated this way. Main circuit conditioning remains the
Note06 finite positive-path ledger, including its N factor, rather than
an exponential-in-N recurrence.

Already delivered coefficients, slopes, node/Q data and weights have
zero further input error in this final-circuit comparison, since their
perturbations were paid in E_ar/E_RS/E_geo. Provider-internal arithmetic
is paid in its delivered radius, once. This finite dyadic construction
controls operand lengths and avoids relying on exact unstructured rational
accumulations. The independently computed channels retain paid heat-defect
bounds; residual_z still requires the additional mixed T,z channel.

## 5. Composed bit work and streamed storage

Let B be the finite binary input length, including exact query, center
and rational calibration data and descriptor witnesses. Let
s_sigma=ceil(log2^+(1/sigma)) for P1's strict center separation. If valid
witnesses are supplied, their verification cost is bounded by their own
length/precision; s_sigma records the additional dependence when finding
them by refinement. Endpoint guards need no edge-separation parameter.

Choose a uniform P>=1 covering the negative log2 of every external
provider tolerance in Note09 Section 7 and of the required final-circuit
primitive/quantization allowance. Include the full linear-sum counts
and E10's phase multipliers. These are finite computable accuracy requests,
not unknown field errors. For fixed chart/calibration data and the
prescribed factor-controlled allocations they have sufficient size

    P=3L²/(8log2)+O(L log L).                                (C15)

The term includes the finite positive path/accumulation allowance;
provider-internal Gauss isolation and exact rational temporary operand
lengths are separately counted below. General requests retain their
actual larger P. Arbitrarily conservative calibrations/tolerances or
arbitrarily long rational queries are not silently assigned the L-rate.

A conservative component work ledger is:

| Component | Finite work to count |
| --- | --- |
| Center and geometry | Certified descriptors with s_sigma, endpoints/thresholds to P+O(L) bits; no edge separation |
| Elementary arithmetic-mode providers | O(N) log/phase/inverse-root calls, each polynomial in B+P+L |
| Gamma | One J=p+1 center call, O(n) value calls, each C7 with the actual rational node input length |
| Common preprocessing | O(p³) shape and O(K²) weighted RS operations; exact coefficient heights are polynomial |
| Two Gauss orders | C14 at s=n,q, with mapped copies reused |
| RS contour/composition | O(q) reusable F_0 samples and O(n(qK+K²)) remaining term operations, with actual operand lengths |
| Field and channels | O(Np) mode/moment work and full sequential accumulation; fixed channel kernels at at most 2n nodes |

For an explicit loose polynomial statement set

    Q=2+B+P+s_sigma+ceil(L)².                                (C16)

For fixed r,b and a fixed valid effective calibration record, there is
an effective constant C, determined by that data and the stated arithmetic
recipes, such that one complete query with its needed preprocessing has

    T_bit <= C (N+1) Q^40,
    M_bits <= C Q^20.                                      (C17)

The following degree accounting substantiates this deliberately weak
bound. The analytic majorants give n,q=O(Q), p,K,J,m=O(Q).
Gauss depth and physical-node numerator/denominator length are O(Q^4),
absorbing log Q by Q in C12. Mapped weight numerators/denominators have O(Q^5) bits by C13.
Thus U_s=O(Q^4) and the two Gauss work
bounds are O(Q^16). Each outer-node gamma input has b=O(Q^4), so C7
is O(Q^24) per call and O(Q^25) over the O(Q) calls. Cached gamma
space is O(Q^12). Elementary mode inputs have at most B+O(L+P) bits.
Dense finite shape/RS/moment paths have polynomial depth/degree and
coefficient bit heights; individual reciprocal powers through O(K)
with node lengths O(Q^4) use O(Q^5)-bit temporary integers. The remaining
term counts are bounded by (N+1)O(Q^5). Outside gamma/Gauss, even the remaining elementary calls have input
and temporary lengths bounded by O(Q^5); the elementary-series bound
therefore gives O(Q^30) work and O(Q^15) workspace per such call.
Their count is at most (N+1)O(Q^5), so O((N+1)Q^35), including
dyadic rounding and finite positive error-ledger arithmetic, fits
inside Q^40. A single full linear accumulation has only log(N+1)=O(L) extra
integer bits. No N-fold denominator product is retained.

Store the common shape/RS tables, two base Gauss rules and reused contour
samples, and process one outer node or one arithmetic mode at a time.
Modes need not be saved: their frozen inputs can be regenerated by the
same deterministic accuracy recipe for fixed X. Gamma calls run
sequentially. Their workspace, polynomial tables, root intervals and
finite channel accumulators fit Q^20 bits. Materializing all N mode data
would add its corresponding N-dependent storage; C17 uses streaming.
The very small common scale is returned as mantissa times 2^k, with
|k|=O(X+log X) and binary exponent length O(log X). It is not stored as
an expanded denominator with O(X) zero bits.

The large exponents in C17 are sufficient upper bounds, not optimized
claims. For the prescribed accuracy with fixed calibration data,
Q is polynomial in B+s_sigma+L, and N is of order exp(L/2).
Both previously exponential provider dependences on P or Gauss order
are removed. The full uncompressed arithmetic population remains.
Neither C17 nor scalar counts alone establish affordable runtime at an
actual height; no operation timing or implementation evidence is supplied.

## 6. Height gates: paid structural facts and unpaid calibration data

A valid calibration record must carry actual uniform inequalities,
their domains and starting heights, not merely numbers that make later
tests pass. The following remain symbolic in Notes02--06:

| Data | Uniform fact and role |
| --- | --- |
| H; A,D | Disk bound sup_|q|<=X/4 |ell''(X+q)|<=H/X; then A=max(1,H),D=4 gives the all-order coefficient majorant |
| D0 | Center slope remainder <=D0/X, with its starting height |
| C_Gamma | Real-window gamma ratio G(X+q)<=C_Gamma g exp(|q|) |
| g_->0 | G(X)>=g_- X^(7/4)exp(-pi X/8) |
| C_tail | Normalized moderate-source bound with source exponent 4; includes the source constant and inverse g_- |
| M_H | An actual upper bound on integral |Phi| for remote data |
| C_chi, c_o | Full-chart gamma ratio and full chart/time outer-envelope lower bound |
| C_cal | Effective coefficient of the calibration remainder (1+L)/X |

Their already proved finite expressions, when available, may be enclosed
by the new providers. Numerical values of all these uniform constants
and their joint onsets are not presently supplied in the source notes.
Fast evaluation at one point cannot prove the uniform assertions.
The quoted classical real RS remainder holds for every positive real
u and positive integer K; no new K-dependent RS onset is invented.

Some structural onset obligations can be made explicit now. For L>=16,
V<=12L, X=4pi exp L>=12exp L, and
sqrt(2pi X)>=8exp(L/2). Hence

    4(V+2)/sqrt(2pi X)<=(6L+1)exp(-L/2)
                    <=97exp(-8)<97/256<1/2,
    2(V+2)<=X/4,
    K<=L<=exp L-L<=(X-V)/(4pi).                            (C18)

For the second inequality it is enough to compare 24L+4 with 3exp L;
their ratio decreases on [16,infinity) and at 16 is bounded using exp16>2^16.
For the third use V/(4pi)<=L and exp L>=2L. These facts pay Note06's
strong local/ellipse geometry and the retained-order gate. L>=16 also
gives V>=64. Extra buffer gates can be paid, for example, by
L>=max(16,(2R+W+1)/8,log(1+4(W+1))) since V>=8L and X>=12exp L.
They do not pay the still-symbolic classical calibration onsets.

The strong geometry also implies the E18 logarithm bound:
|Log(1+q/X)|<=1/3 for |q|<=2V, so the required modulus is <=L+1.
The stronger slope gate D0/X<=1/2-pi/8 and epsilon_lambda<=1/2 already
give |lambda_hat|<=1+L/4. Thus these two formerly unnamed eventual
conditions require no additional independent onset. If pi<=16/5, the
simple sufficient slope height X>=10D0 pays the first of them; pi<=16/5
itself has a finite rational arctangent-series proof under Note09.
Given A and D, the remaining local and damping gates are explicit finite
tests; an optional safe local shape payment for D=4 is
L>=max(16,2log(1+24A)), using L²<=exp(L/2) for L>=16.

For exact fixed c=1/2 and theta=1/2 retain every structural gate in
Note05 Section 5, Note06's stronger slope gate, all original uniform
classical domains/onsets, and C_cal(1+L)/X<=1. In particular the damping
condition 2{(D0/X)(pi/4+L/2)+D0²/X²}<=1 is still checked; the stronger
real-slope gate alone is not substituted for this separate condition.

The half-target truncation rates, with Co<=C_+/c_-, are the four tests

    (p+3/4)log X >=(3/8)L²+log^+(8 Co Q_p),
    (61/8)L² >=(9/4)log X+log^+(392 Co A_mod^(theta)),
    (61/8)L² >=(1/4)log X+log^+(392 Co A_art,p^(theta)),
    X²/256 >=pi X/8+(3/8)L²+log^+(392 Co A_far), theta=1/2.   (C19)

Here superscript theta labels the tail parameter, not exponentiation.
Q_p and both moderate/artificial constants are the actual finite
Note05 G7--9,G16--18 expressions. A_far=(M_H/g_-)*max(J_0,J_0^t)
uses Note04's explicit remote-kernel constants. Do not replace 8,392 by
the old full-target 4,196. Every N mode and the full source tail remains.

A **finite height verifier** takes a valid calibration record, X,p,N,
and a finite interval-precision witness. It recomputes outward enclosures
for the descriptor inequalities, every listed structural/domain test,
C19, and Note09's finite error allocations using the new providers.
It accepts only when all strict margins are certified. Otherwise that
finite witness is rejected or reported inconclusive; it does not refine
forever at equality. Every strictly admissible height has a successful
finite witness. This certifies inequalities **against** a valid uniform
calibration record, not the truth of arbitrary supplied calibration claims.

A pass at one height alone does not prove all larger heights. A stronger
**parameterized all-height onset** can nevertheless be given using the
continuous upper majorants already proved in Note05. Let C_*,C_*theta
be its G14 constants for J and J_theta, and C_Q be its G14 prefactor,
so Q_p<=C_Q J(p), A_art,p^(theta)<=C_pop J_theta(p). Set

    S=max(1,C_*,C_*theta),
    M=max(0,log^+(8 Co C_Q),log^+(392 Co C_pop),
            log^+(392 Co A_mod^(theta)),log^+(392 Co A_far)),
    L_rate=max(16,(32S)^2,sqrt(32M)), theta=1/2.                (C20)

For every L>=16, (p+1)log(p+2)<=L log(L+2)<=L^(3/2).
Thus at L>=L_rate both local/artificial logarithmic costs are
<=M+S L^(3/2)<=L²/16, and the fixed moderate/remote log costs are
<=L²/32. Using p>=L/2-1, the local source-rate gap is
(p+3/4)log X-3L²/8>=L²/8-L/4>=7L²/64, strictly larger than L²/16.
Also log X<L+3, so at L>=16 the moderate height power costs at most
L²/4 and the artificial one at most L²/16; these fit C19 with slack.
For the remote test, X>=256 gives pi X/8<=X²/512, while
X>=12exp L and exp L>=2L give X²/512>=9L²/8>
(3/8+1/32)L². This proves all four C19 inequalities with strict margins.
The bound uses both floor inequalities, not monotonicity of Q_p across
its jumps.

Take A=max(1,H),D=4. Besides the buffer payments above, the sufficient
conditions L>=2log(1+D0) and L>=16 give X>=10D0 and
X>=2D0(L+2), since L+2<=exp(L/2). The latter yields
2{(D0/X)(pi/4+L/2)+D0²/X²}<1. Likewise
L>=2log(1+C_cal) pays the calibration gate. Let X_cl be a common
**center** onset already covering every required classical domain;
translate underlying argument thresholds first (e.g. u>=x_cl throughout
the real window needs center X>=2x_cl). One explicit sufficient choice is

    L0=max(L_rate,(2R+W+1)/8,log(1+4(W+1)),
           2log(1+24A),2log(1+D0),2log(1+C_cal),
           log(1+X_cl/(4pi))).                              (C21)

Every accepted P1 center with L>=L0 meets the inherited structural and
half-target gates, given that valid uniform calibration record and its
translated domains. Optional V<=log²X also follows from L>=16.
Rational upper enclosures of C20--21 can be used instead of their exact
values, preserving the all-height statement. Center separation sigma
remains nonuniform and excluded boundary centers remain excluded.

No universal numerical X0 is claimed. The first unpaid onset obligation
is a concretely proved, domain-specific record for the symbolic uniform
calibration constants and their common center onset. The finite verifier
checks a supplied height; C21 is a conditional all-height threshold;
a numerical universal threshold still needs actual calibration data.

## 7. Disposition, controls, and next deliverable

**Analysis — Sol:** accept C1--17 and C18--21 at their stated scopes.
AN04 r1 CLOSED, bounded analytical audit Complete: both slow providers
are improved and composed bit-work/storage bounds, a finite height verifier and an explicit parameterized
all-height onset are supplied. Broad R05 remains Partial at concrete
calibration/onset instantiation, implementation and software certification.
Same-model internal checks are not independent specialist validation.
The manuscript has not integrated Notes09--10. R04/R06 NOT_STARTED;
HDA-A02 Partial, HDA-17 Partial, HDA-18 Gated, HDA-20 unfulfilled unchanged.

This is an evaluation/cost milestone under [avoid01][a1], not an RH
criterion. See the [result index][results], [heat cluster][heat],
[control screen][controls] and [avoid index][avoid], especially
[separate costs][a12] and [scoped failures][a7]. Euler-factor/finite-prime
controls fail the unchanged canonical coefficients; weighted-square/
cutoff controls fail the full canonical completion; reflected, smooth and
positive-primitive controls lack the same complete gamma/arithmetic
identity. Their heat identities can survive. No collision, simplicity,
RH, physical-transfer or extended-time conclusion follows from cost bounds.

**Next deliverable — Analysis, Sol:** [AN05 r1][next], prepared but not
executed: instantiate the missing uniform calibration facts with actual
constants/domains and decide what height onset can be certified. This is
the next tractable analytical dependency; no exceptional Astra bottleneck
has been identified. Numerical implementation needs its own bounded request.

[n9]: 09_FINITE_PROVIDER_ALGORITHMS_20261026.md
[review]: ../reviews/08_EFFICIENT_PROVIDER_AND_COST_ASSESSMENT_20261026.md
[inputs]: 10_EFFICIENT_PROVIDER_INPUTS_20261026.json
[work]: 10_EFFICIENT_PROVIDER_WORK_RECORD_20261026.json
[sources]: ../references/04_EFFICIENT_PROVIDER_SOURCE_AUDIT_20261026.md
[next]: ../research-progress/handoffs/HDA-R05-AN05.md
[stirling]: https://dlmf.nist.gov/5.11#ii
[bernoulli]: https://dlmf.nist.gov/24.8.E1
[legendre]: https://dlmf.nist.gov/18.9.T1
[legendreder]: https://dlmf.nist.gov/14.10.E5
[results]: ../../../../../result-summaries/README.md
[heat]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a1]: ../../../../../avoid/01_restating_the_target.md
[a7]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md

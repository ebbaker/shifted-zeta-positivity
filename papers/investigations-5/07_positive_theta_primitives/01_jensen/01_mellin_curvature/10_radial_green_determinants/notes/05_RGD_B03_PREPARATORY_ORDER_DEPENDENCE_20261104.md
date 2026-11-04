# RGD-B03 preparation: a first next-order margin and its error budget

4 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance; actual **gpt-6-astra (Codex), effort max**,
chat0002, turn `01a1a798-eb9d-7293-ac50-736a92e31a8e`.

**Status: bounded B03 preparation complete; full B03 extension remains
gated.** This is the author-requested analytical preparation under
[Scope07][scope] and [Brief06][brief]. It proves a quantitative lemma
for the first next-order comparison at **(r,k)=(4,1)**, with explicit
coarse input premises that can be checked against the existing E02
certificate. It does not acquire or certify a new theta case in this
turn. Exact verification of those input premises and the resulting
rational witness is assigned to **RGD-E02 r2 — Sol** in [Packet08][packet].

The lemma compares the **same complete joint Taylor payment** with a
reference determinant margin established by explicit polynomial bounds.
For the stated input box it gives
\[
\frac{\mathcal R_{4,1}}{q^*_{4,1}}<\frac1{15},\qquad
L_{4,1}>\frac{14}{15}q^*_{4,1}
>\frac{7}{3000}(c_1^*)^8>3\cdot10^{-31}.
\tag{1}
\]
These are **conditional analytical conclusions with proof-author checks**,
not a claim that the new input checks or a new certificate have already
been executed. The existing acquisition is now accepted by
[E04 r2 Review03][review03]; that acceptance does not check this new
application. No numerical implementation, quadrature, index scan or
acquisition replay occurred in this preparation.

The [result index][results], [theta cluster][theta] and [controls][controls],
with [avoid][avoid] especially [target reformulations][a01],
[joint payments][a12], [bounded numerics][a10] and [scoped claims][a07],
govern the interpretation. Known finite-order positivity already covers
order five. The gain sought here is affordability of a specified error
payment, not a new positivity range or an RH result.

## 1. Fixed comparison and the new structural requirements

Retain Note01's complete canonical source, ordinary coefficients,
negative-index zero convention, exact common b=1/16 and compact
first-mode reference on [0,2]. For every required j>=0 put
\[
a_j=\frac1{8(2j)!}\int_0^2u^{2j}e^{u-\pi e^{4u}}\,du,
\qquad T_j=E_j+B_j(2),
\]
\[
E_j=\frac{e^{-4\pi}}
 {8(1-e^{-5\pi})(16\pi-1)^{2j+1}},
\]
where B_j(2) is the complete spatial exterior bound in Note01 (18).
The exact complete moments have the form d_j/8=a_j+z_j with
0<=z_j<=T_j. This pays all n>=2 modes and u>2; there is no truncated-domain
Green transfer or omitted artificial boundary.

Write
\[
C_j(z)=b\delta_{j0}+a_{j-1}-a_j+z_{j-1}-z_j,
\qquad c_j^*=C_j(0),
\tag{2}
\]
with a_-1=z_-1=0, and C_j=0 for j<0. Define
\[
P_{r,k}(z)=D_{r,k}(C(z))^2
-D_{r,k-1}(C(z))D_{r,k+1}(C(z)).
\tag{3}
\]
After exact collection, let q^*_(r,k)=P_(r,k)(0), and let R_(r,k)
be the sum of the absolute nonconstant Taylor coefficients times T^alpha.
This is precisely the Note01 payment, extended from degree six to 2r.
It gives Q_(r,k)>=L_(r,k):=q^*_(r,k)-R_(r,k).

The Desnanot–Jacobi identity also gives
\[
P_{r,k}(z)=D_{r+1,k}(C(z))D_{r-1,k}(C(z)).
\tag{4}
\]
We use (4) to bound the error of the already combined polynomial. We do
not separately bound the original D_r,k^2 and neighboring product.
No sign of D_(r+1),k is inferred from the identity.

For general r,k>=1, the polynomial degree is at most 2r, its maximum
coefficient/moment index is k+r, and the three order-r endpoint ranks
are max(r-k+1,0), max(r-k,0), max(r-k-1,0). The index requirements at
the first next order are therefore:

| Comparison | Endpoint ranks of the three order-r factors | Required primitive indices, allowing unused lower ones | Status here |
| --- | --- | --- | --- |
| r=3, k=1 | 3,2,1 | 0,...,4 | Earlier pilot; matched analytical budget below |
| r=4, k=1 | 4,3,2 | 0,...,5 | The only worked next-order case |
| r=4, k=2,3 | 3,2,1 or 2,1,0 | 0,...,6 or 0,...,7 | Existing acquisition has the inputs; no claim or check here |
| r=4, k=4 | 1,0,0 | 0,...,8 | Transition case; moment 8 is not in the saved acquisition |
| r=4, k=5 | 0,0,0 | 0,...,9 | First pure-volume neighbor triple; moments 8,9 are absent |

In particular, k=4 ceases to be a pure-volume neighbor triple at the
next order. The unbounded k range requires new uniform analysis. An
entry count or available moments alone supplies no determinant margin.
At k=1 all endpoint-volume terms remain in c0*=b-a0 and (2).

## 2. A norm bound for the unchanged joint payment

For a polynomial H(z)=sum h_alpha z^alpha define
\[
\|H\|_T=\sum_\alpha |h_\alpha|T^\alpha.
\]
Coefficient convolution and the triangle inequality give
||FG||_T<=||F||_T||G||_T. Suppose every nonzero reference coefficient
used is positive, and for each such j
\[
\|C_j-c_j^*\|_T\le\epsilon c_j^*.
\tag{5}
\]
At j=0 the left side is T0, while at j>=1 it is T_(j-1)+T_j.
Negative-index entries vanish identically, so they need no relative bound.

Let H_(n,k)(c) be the coefficientwise absolute polynomial of the
**collected** determinant D_(n,k)(c). Homogeneity of degree n, followed
by the binomial expansion of each monomial, proves
\[
B_{n,k}:=\|D_{n,k}(C(z))-D_{n,k}(c^*)\|_T
\le\big[(1+\epsilon)^n-1\big]H_{n,k}(c^*).
\tag{6}
\]
The proof expands each monomial around its actual positive reference
value, removes its constant, and bounds each linear coefficient
perturbation by (5). Summing absolute monomial coefficients gives (6).
No determinant positivity or probabilistic independence is assumed.

Put d_+=D_(r+1),k(c*) and d_-=D_(r-1),k(c*). Subtract the constant from
(4) and retain its two linear-in-remainder terms and product remainder:
\[
\boxed{\mathcal R_{r,k}\le
|d_+|B_{r-1,k}+|d_-|B_{r+1,k}
+B_{r+1,k}B_{r-1,k}.}
\tag{7}
\]
This bounds the exact joint coefficient norm from above. Any cancellations
in the collected P can only improve it. The nonlinear remainder is paid;
there is no deletion of a mixed term.

If d_+d_->0, define
\[
\kappa_{n,k}=\frac{H_{n,k}(c^*)}{|D_{n,k}(c^*)|},\qquad
e_{n,k}=\big[(1+\epsilon)^n-1\big]\kappa_{n,k}.
\]
Then the explicit error-versus-margin bound is
\[
\frac{\mathcal R_{r,k}}{|q^*_{r,k}|}
\le e_{r+1,k}+e_{r-1,k}+e_{r+1,k}e_{r-1,k}.
\tag{8}
\]
The margin and condition factors are essential. Small E_j or increasing
degree alone says nothing about affordability. Equation (8) is an
estimate, not an order-induction theorem: its reference signs and
condition factors must be justified in each claimed domain.

## 3. A coarse input box for the first next-order case

The following are the **fixed premises** for the worked lemma, all
expressed in the existing reference moments and tails:

1. c0*,...,c5*>0 and c1*>1/3000.
2. For j=2,...,5, set t_j=(c0*)^(j-1)*c_j*/(c1*)^j. Require
   \[
   \frac{465}{1000}\le t_2\le\frac{466}{1000},\quad
   \frac{135}{1000}\le t_3\le\frac{137}{1000},\quad
   \frac{28}{1000}\le t_4\le\frac{29}{1000},\quad
   \frac4{1000}\le t_5\le\frac5{1000}.
   \tag{9}
   \]
3. T0/c0*<=1/40000 and (T_(j-1)+T_j)/c_j*<=1/40000 for j=1,...,5.

These are independent, low-moment box conditions, not assumed D5 signs.
Their scale is suggested by the already published E02 moment/tail
readings. **Short decimal displays are not used to certify (9) or (5).**
Packet08 assigns exact comparisons against the saved dyadic endpoints,
including nonzero B, before applying the lemma to canonical theta.
The six compact moments and six E/B pairs needed are already present in
the accepted eight-moment acquisition. No integral or new input index is
needed for that check.

## 4. A justified reference determinant margin on that box

For k=1, first-row expansion of the upper-Hessenberg Toeplitz matrix gives
\[
D_{n,1}=\sum_{j=1}^n(-1)^{j-1}c_0^{j-1}c_jD_{n-j,1},
\qquad D_{0,1}=1.
\tag{10}
\]
The cofactor selecting column j has j-1 successive c0 entries and the
remaining (n-j)-order Toeplitz block. This proves the recurrence and its
sign, including every boundary coefficient.

At the reference, write D_(n,1)(c*)=(c1*)^n f_n, t1=1 and f0=f1=1.
The recurrence yields
\[
\begin{aligned}
f_2&=1-t_2,\\
f_3&=1-2t_2+t_3,\\
f_4&=1-3t_2+t_2^2+2t_3-t_4,\\
f_5&=1-4t_2+3t_2^2+(3-2t_2)t_3-2t_4+t_5.
\end{aligned}
\tag{11}
\]
On (9), f4 and f5 decrease with t2, increase with t3, and decrease
with t4; f5 increases with t5. For f5 the t2 derivative is
-4+6t2-2t3<0, and 3-2t2>0. Endpoint substitution therefore gives
\[
\begin{array}{c|c|c}
n&\text{direct enclosing values}&\text{convenient strict bounds}\\\hline
2&[0.534,0.535]&1/2<f_2<3/5\\
3&[0.203,0.207]&1/5<f_3<1/4\\
4&[0.060156,0.067225]&3/50<f_4<7/100\\
5&[0.012648,0.021265]&1/80<f_5<1/40.
\end{array}
\tag{12}
\]
Every terminating decimal here denotes an exact rational, computed from
the rational box; it is not a floating measurement. In particular,
f5 positivity is proved explicitly on the whole box, rather than imported
from canonical D5 positivity or asserted for the positive reference measure.

Replacing the coefficients of each collected determinant in (11) by
their absolute values gives H_(n,1)(c*)=(c1*)^n S_n, with
\[
\begin{aligned}
S_2&=1+t_2<3/2,\\
S_3&=1+2t_2+t_3<21/10,\\
S_4&=1+3t_2+t_2^2+2t_3+t_4<3,\\
S_5&=1+4t_2+3t_2^2+3t_3+2t_2t_3+2t_4+t_5<21/5.
\end{aligned}
\tag{13}
\]
The cancellations responsible for f_n are retained for the margin.
Only perturbation errors use the positive majorants S_n.

## 5. Matched error budgets at r=3 and r=4

Take epsilon=1/40000. For 2<=n<=5,
\[
(1+\epsilon)^n-1<(n+1)\epsilon.
\tag{14}
\]
For example, the binomial terms of degree at least two total at most
26*epsilon^2<epsilon. Define b_n=B_(n,1)/(c1*)^n. Equations (6), (13)
and (14) give
\[
b_2<9/80000,\quad b_3<21/100000,\quad
b_4<3/8000,\quad b_5<63/100000.
\tag{15}
\]

For the preceding r=3 comparison, q3,1*=(c1*)^6 f4*f2, and (7) gives
\[
\frac{\mathcal R_{3,1}}{(c_1^*)^6}
<\frac7{100}\frac9{80000}
+\frac35\frac3{8000}+\frac9{80000}\frac3{8000}
=\frac{149067}{640000000}<\frac1{4000}.
\tag{16}
\]
For the first next-order r=4 comparison,
q4,1*=(c1*)^8 f5*f3, and
\[
\frac{\mathcal R_{4,1}}{(c_1^*)^8}
<\frac1{40}\frac{21}{100000}
+\frac14\frac{63}{100000}
+\frac{21}{100000}\frac{63}{100000}
=\frac{1628823}{10^{10}}<\frac1{6000}.
\tag{17}
\]
This yields a comparison using the same analytical majorization at both
orders, rather than comparing a measured old payment to an unrelated
new upper bound:

| r, k=1 | Degree of P | Reference margin divided by (c1*)^(2r) | Complete payment divided by (c1*)^(2r) | Relative payment bound |
| --- | --- | --- | --- | --- |
| 3 | 6 | >3/100 | <1/4000 | <1/120 |
| 4 | 8 | >1/400 | <1/6000 | <1/15 |

The permitted relative loss bound is eight times larger at the next
step. That is a comparison of conservative proved bounds, **not measured
growth of the exact error**. The stronger old E02 values remain unchanged.
The reference margin shrinks faster than this normalized payment, but
the payment still fits inside the next margin under the fixed premises.

Subtracting (17) from the next reference floor gives
\[
L_{4,1}>
\left(\frac1{400}-\frac1{6000}\right)(c_1^*)^8
=\frac7{3000}(c_1^*)^8>\frac7{3000^9}>3\cdot10^{-31}.
\tag{18}
\]
It also proves (1). Once the input box is verified, the actual
canonical Q4,1 is at least this L. The inherited actual-source D3,1>0
then gives D5,1>3e-31/D3,1. No numerical D3 or relative eta is asserted,
and no canonical D5 sign was used to obtain the reference margin.

## 6. Why this does not supply a uniform extension

Formula (8) displays the missing dependence: both epsilon and the
reference condition factors kappa_(n,k) vary with the indices. The
specific small uniform epsilon used here cannot hold for all coefficient
indices with this compact reference and this E vector.

Indeed a0>0 and, for j>=2,
\[
0<c_j^*\le a_{j-1}
\le a_0\frac{2^{2j-2}}{(2j-2)!}.
\tag{19}
\]
Positivity follows pointwise from m_(j-1)-m_j on [0,2], since
u^2/[(2j)(2j-1)]<=1/3. The upper bound uses u<=2.
With a=16*pi-1 and K=exp(-4*pi)/[8(1-exp(-5*pi))],
\[
\frac{T_{j-1}+T_j}{c_j^*}
\ge\frac{E_{j-1}}{c_j^*}
\ge\frac{K}{a a_0}
\frac{(2j-2)!}{(4a^2)^{j-1}}\longrightarrow\infty.
\tag{20}
\]
The ratio of successive factorial factors is (2j)(2j-1)/(4a^2), which
eventually exceeds every fixed constant. This is a **scoped limitation
of the uniform entry-relative majorant (5)**. It does not prove that
the exact joint R/q fails, that the canonical determinant is negative,
or that all first-mode or Green estimates fail. The exact joint polynomial
can have structure that the entrywise norm bound discards.

No margin estimates for k=2,3, the changed k=4 transition, the k=5
pure-volume case or the unbounded k range are supplied. No all-order
positivity of the reference is assumed. The k=1 lemma is an actual
quantified preparation for one next-order check, not an induction
contract. Full B03 remains gated after it.

## 7. Controls, evidence and fixed follow-through

The polynomial estimates (6)–(8) are generic. Their application uses the
literal canonical unit-square expansion, the exact b and the complete
E+B payments. Weighted-square controls change the weights and require
rechecking those inputs; Euler-factor controls change the source series;
reflected/smooth positive-primitive controls do not provide the literal
square expansion. None is declared to fail an uncomputed finite box
test. A positive-time collision can coexist with a time-zero finite-order
bound. The box lemma applies to any source satisfying its precise inputs.

The accepted E02 dyadic record is reused as the **available input source**,
not as a preexisting Q4 certificate. The new envelope memberships in
Section 3, new coefficient recurrence checks and their exact rational
closure have not been implemented here. They form the bounded
[E02 r2 request][packet]. A model change is not specialist-independent
review; its output must name the shared acquisition and analytical premises.

**Next: [E] RGD-E02 r2 — Sol.** Verify this single existing-data application
and either close the >3e-31 lower allowance or identify the exact failed
input/estimate. No new integration, extra k, precision escalation,
changed tail or arbitrary-order campaign is needed or authorized by the
packet. A material failure of this fixed box goes to B02 before a redesign.
The [sole register][progress] records preparation separately from full B03.

## Version anchors and preparation checks

- Note01: `556a97aa60f7a3448acbd00cf8bfa4c3e2916e428f67d03dbb97889077bc9847`.
- E02 r1 certificate: `6db6276d65ea11706286cffa0aef899d1097f8e4bac76cbdd70f0ef40d692298`.
- E02 r1 code: `b4863a6840cd4d68b10fe993f3f4cdc5e66dd8b3d44903445b306a50c8879db4`.
- E04 r2 Review03: `4c1d9e07f620e49f6d2fcaad538f176549316e19e8f11d9010cc52f4856b3807`.

The proof author checked the recurrence through n=5, endpoint monotonicity,
finite rational arithmetic in (12)–(18), all norm cross terms and the
factorial ratio in (20) analytically. These are not separate assessment
or executed certificate checks. Source/library validity remains at the
inherited internal-review level. There is no manuscript milestone or
investigation closure and no global result-index update in this return.

[scope]: ../research-progress/handoffs/07_RGD_B03_PREPARATORY_SCOPE_20261104.md
[brief]: ../research-progress/handoffs/06_RGD_CONTINUATION_AND_ASTRA_B03_PREPARATION_20261104.md
[packet]: ../research-progress/handoffs/08_RGD_E02_R2_EXISTING_DATA_NEXT_ORDER_AND_MODEL_CHANGE_20261104.md
[progress]: ../research-progress/01_RADIAL_GREEN_DETERMINANTS_RESEARCH_PROGRESS_20261104.md
[review03]: ../reviews/03_RGD_E04_R2_TWO_CASE_CERTIFICATE_ASSESSMENT_20261104.md
[results]: ../../../../../../../result-summaries/README.md
[theta]: ../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a10]: ../../../../../../../avoid/10_numerics_ahead_of_the_question.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md

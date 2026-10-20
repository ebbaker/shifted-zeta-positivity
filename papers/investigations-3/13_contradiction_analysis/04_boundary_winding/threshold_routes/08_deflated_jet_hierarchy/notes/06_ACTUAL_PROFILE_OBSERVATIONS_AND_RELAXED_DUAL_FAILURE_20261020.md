# BW-08: actual theta profiles and a scoped zero-error dual failure

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Authoring model **gpt-6-astra (Codex)**,
actual reasoning effort **ultra**, verified from the parent turn metadata
and inherited by this research subagent.

**Status: observation and weak-duality interface proved in-note;
actual-profile feasibility inequalities interval-certified by the
accompanying checker. Separate same-model internal review; no specialist review.**
This completes BW2-03.P1 as a **scoped losing experiment**, not a useful
P2 contract. The new fact is tied to the unchanged theta source's actual
three observations, rather than a constructed profile vector:

> For every `T in [0.099999,0.100001]` and `a in [1001,1002]`, the exact
> theta observations at `b=20,40,80`, after removal of a hypothetical
> double pair at `±a`, admit a positive relaxed weighted measure with
> one unit-count atom at squared location `(a+d)^2`, for every
> `0<d<=1/2`. Consequently every
> global count majorant in the stated three-observation span has exact
> objective at least one. The corresponding relaxed deflated sum is
> unbounded as `d` tends to zero.

The auxiliary masses at three other squared locations are **not required
to be integer zero multiplicities**. No entire function, positive Fourier
source, heat flow or actual theta zero configuration is constructed from
this measure. It is a witness against this finite-data **linear weak-dual
relaxation**, not against all uses of the actual theta profiles. Its zero
error conclusion is stronger than a failure caused by acquisition noise;
more precision cannot repair this fixed relaxation. Additional samples,
integer constraints, full zero counts and other arithmetic information
are outside the test. The sample schedule is not expanded after failure.

The [result index][results], [arithmetic summary][arithmetic],
[control summary][controls] and [avoid index][avoid] were read first.
This is a bounded methodological milestone under [avoid 01][a01], with
its retained premises screened under [avoid 02][a02] and its negative
scope restricted under [avoid 07][a07]. It makes no RH-equivalent claim.
It executes the optional task in [overview 03][program];
[BW-08 Note 05][previous] remains the source for constructed-profile
obstructions and is not repeated as a claim about theta data.

## 1. Fixed contract and classification

Let

\[
\mathcal D=[99999/10^6,100001/10^6]\times[1001,1002],
\quad (b_0,b_1,b_2)=(20,40,80),\quad B_i=b_i^2,
\]
\[
s=a^2,\qquad I_a=[(a-1)^2,(a+1)^2].                     \tag{1}
\]

The question is whether a global majorant from these three observations
can certify `N_(I_a)<1`, removing other positive roots within distance
one of the designated positive event. The physical event hypotheses are
an all-real even order-one theta slice with an **exactly double** zero
at `a`, so that its negative mirror is exactly double too. Their truth
at any point of (1) is not asserted. The actual theta profile exists
without these hypotheses and is acquired unconditionally below.

The existing [coverage inventory][coverage] leaves the real first-jet
bridge `1001<|x|<exp(2000)` on `1/100<=t<=1/5` unresolved. The endpoint
`a=1001` is already covered in that inventory; the present computation
is only a profile-method feasibility test and adds no physical coverage.
It does not certify the absence or presence of events in this box.

One initial design pilot at `T=.1,a=1000` selected the three slack squared
nodes `900,1600,25000`; those floating results are not evidence. The final
validation freezes those nodes, (1), four retained theta modes, source
cutoff `U=1`, 192-bit arithmetic with a 256-bit replay, absolute quadrature
tolerance `1e-40`, relative tolerance `1e-36`, 200,000 evaluations and
30 subdivision levels per integral, 300 seconds total and 512 MiB resident-memory stopping budget. The time limit is enforced
by an alarm; resident memory is checked every 128 quadrature callbacks
and at completion, rather than by an unavailable OS address-space cap. The stopping answer is either certified positivity of all three
slack weights throughout (1), or a reported failed enclosure. The measured
complete execution is under one second; the [record][record] gives each
run's timing and actual memory use. These costs do not predict another
schedule's performance. No solver or sample sweep supplies a proof.

## 2. Weighted observation model, including the infinite tail

Use the unchanged theta normalization from [BW-01 Contract 02][source]:

\[
H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\quad
\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})
                         e^{-\pi n^2e^{4u}}.             \tag{2}
\]

Under the event hypotheses, the inherited paired product is

\[
F(z)=H(T,z)=F(0)\prod_{\rho>0}(1-z^2/\rho^2)^{m_\rho},
\quad F(0)>0,\quad \sum_{\rho>0}m_\rho/\rho^2<\infty.
                                                               \tag{3}
\]

This uses evenness, order one and all real zeros, as in
[Polymath, Section 3][polymath] and the repository's
[previous product calculation][product]. There is no quadratic
exponential factor. The product converges locally uniformly, and its
logarithmic derivative on the imaginary axis may be differentiated
termwise: for `b` in a compact subset of `(0,infinity)`, all sufficiently
large-root terms and their first derivatives are dominated by a constant
times `m_rho/rho^2`; finitely many smaller-root terms cause no pole.
Therefore

\[
D_T(b):=\partial_b\log H(T,ib),\qquad
D_T(b)/b=\sum_{\rho>0}\frac{2m_\rho}{\rho^2+b^2}.       \tag{4}
\]

Remove exactly the two copies of the positive root `a`, together with
its paired negative mirror, by setting

\[
R_i(T,a)=D_T(b_i)/b_i-\frac4{s+B_i},\quad
\mu_{T,a}=\sum_{\rho>0,\rho\ne a}
 \frac{2m_\rho}{\rho^2+B_0}\delta_{\rho^2},\quad
\phi_i(y)=\frac{y+B_0}{y+B_i}.                          \tag{5}
\]

This is a finite positive measure on `[0,infinity)` with no atom at `s`.
Its mass is `R_0`, since `phi_0=1`; equation (3) proves finiteness. The
unweighted counting measure need not have finite mass. Each `phi_i` is
positive and bounded by `max(1,B_0/B_i)`, and (4) gives the exact identities

\[
\int\phi_i\,d\mu_{T,a}=R_i(T,a),\qquad i=0,1,2.       \tag{6}
\]

No probability normalization is imposed. Time and event dependence are
retained in the actual `D_T` and the subtraction in (5); the argument
does not select a fixed collection of zero labels as `T` varies. It
applies separately at every hypothetical event in (1).

For a bounded interval `I`, put

\[
w_I(y)=\tfrac12(y+B_0){\bf1}_I(y),\qquad
k_s(y)=\frac{(s+y)(y+B_0)}{(s-y)^2}.                     \tag{7}
\]

Then

\[
N_I=\int w_I\,d\mu=\sum_{\rho^2\in I,\rho\ne a}m_\rho
\quad\hbox{is a nonnegative integer},                  \tag{8}
\]
\[
S_2=\frac1{2a^2}+\int k_s\,d\mu.                      \tag{9}
\]

Indeed each paired residual root contributes
`2m_rho(s+rho^2)/(s-rho^2)^2`, equal to
`m_rho[(a-rho)^(-2)+(a+rho)^(-2)]`. The mirror's two remaining copies
supply `1/(2a^2)`. At each actual exactly double event, discreteness gives
a nonzero distance to other roots locally, while `k_s(y)` is bounded at
infinity, so (9) is finite. This statement does not supply a uniform gap.

## 3. Weak duality and error payment

Let `g=sum_i c_i phi_i` with real coefficients. If the **global** pointwise
inequality `g>=w_I` holds on `[0,infinity)\{s}`, then finite-measure
integration gives

\[
N_I\le\sum_i c_i R_i.                                  \tag{10}
\]

This is proved directly; [Bertsimas--Popescu][bp] supplies methodological
context for majorization, not a ready theorem about this rational
infinite-zero model. Strong duality and a finite-support optimizer are
not used. A finite positive atomic measure satisfying (6), whether or
not its atoms have integer zero multiplicities, is a valid lower witness
against the objective of every such global majorant: it can itself be
integrated in (10).

For data `|R_i-Rhat_i|<=epsilon_i`, a fixed certified coefficient vector
has the paid upper objective

\[
U_N=\sum_i c_i\widehat R_i+\sum_i|c_i|\varepsilon_i.     \tag{11}
\]

If coefficients have errors `|c_i-chat_i|<=delta_i`, add
`sum_i delta_i(|Rhat_i|+epsilon_i)` to the objective using `chat`.
A pointwise majorization proof must also remain valid for those
coefficient and parameter variations. Parameter errors in the double-pair
subtraction and source observations belong in `epsilon_i`; they cannot
be hidden as solver tolerance. For fixed positive samples in (1),
`phi_i` has no parameter uncertainty, and the certificate encloses all
actual time and event-height variations directly.

The inequality `U_N<1` would imply `N_I=0` by (8), but a bound on
`mu(I)` alone would not. On a separately paid root-gap complement the
same integration proves a majorant bound for (9). Without that gap,
no member of this finite rational span majorizes `k_s` near `s`:
it is continuous there while `k_s` diverges. The constructed witnesses
in Section 5 make this deficiency occur at the actual theta data vector.

There is also a simple conditioning lower bound. If `I` contains a
neighborhood of `s`, continuity forces
`g(s)>=(s+B_0)/2`, even though the actual measure excludes `s`. In this
sample schedule `0<phi_i(s)<=1`, whence

\[
\sum_i|c_i|\ge (s+B_0)/2\ge1002401/2.                  \tag{12}
\]

Thus equal absolute residual-observation errors `epsilon` cost at least
`501200.5 epsilon` in (11). This is a necessary coefficient-norm bound,
not a sufficient accuracy criterion and not the reason this test fails.
The exact-time acquisitions below have errors below `1e-30` in `D`;
that precision is feasible. [Batenkov--Goldman--Yomdin][bgy] motivates
checking conditioning, but none of its Fourier-measurement rates is
imported into the present Stieltjes observations.

## 4. Complete acquisition of the actual theta profile

For `j=0,1`, acquire respectively

\[
J_0(T,b)=\int_0^\infty e^{Tu^2}\Phi(u)\cosh(bu)\,du,
\quad
J_1(T,b)=\int_0^\infty e^{Tu^2}\Phi(u)u\sinh(bu)\,du,
\quad D_T(b)=J_1/J_0.                                  \tag{13}
\]

The denominator is positive from (2); its strictly positive interval
lower bound is checked before division. On `[0,1]`, retain `1<=n<=4`
and use Arb's validated integration of the entire integrand. There is
no contour shift, oscillatory cancellation, normalizer derivative or
moving cutoff. The following two disjoint bounds pay **all** omissions.

Write `lambda_n=pi n^2` and `T_+=100001/10^6`. Since each source mode is
positive and at most `2lambda_n^2 exp(9u-lambda_n exp(4u))`, both integrands
in (13) are at most
`2lambda_n^2 u^j exp(T_+u^2+(9+b)u-lambda_n exp(4u))`.
For `n>=5`, the exponent is concave, with derivative at zero
`-d_n=9+b-4lambda_n<0`. Therefore its whole-axis integral is at most
`2lambda_n^2 exp(-lambda_n) j!/d_n^(j+1)`. Put

\[
q=(6/5)^4e^{-11\pi}<1,\qquad d_5=100\pi-9-b>0.
\]

The ratios of consecutive `n^4 exp(-pi n^2)` terms decrease for `n>=5`,
and `d_n>=d_5`, so the complete omitted-mode allowance is

\[
E_{\rm mode,j}\le
\frac{2\pi^2 5^4e^{-25\pi}j!}{d_5^{j+1}(1-q)}.         \tag{14}
\]

For each retained `1<=n<=4`, include `j log u` in the exponent on `u>=1`.
Its second derivative is negative; its derivative at one is
`-e_(n,j)=2T_++9+b+j-4lambda_n e^4<0`. The remaining retained-mode
exterior allowance is consequently

\[
E_{\rm ext,j}\le\sum_{n=1}^4
\frac{2\lambda_n^2\exp(T_++9+b-\lambda_ne^4)}
     {4\lambda_ne^4-9-b-2T_+-j}.                        \tag{15}
\]

All concavity, denominator and ratio conditions are checked with outward
arithmetic. Positive omitted integrals are added as `[0,E_mode+E_ext]`.
At `b=80`, (14) is below `4.260e-33` for `J_0` and `1.892e-35` for `J_1`;
(15) is below `5.281e-38` and `5.290e-38`, respectively. These are absolute
integral errors, not errors in the logarithmic derivative. The latter
comes from interval division by the acquired positive `J_0`.

For all intermediate `T`, the complete source probability measure
proportional to `e^(Tu^2) Phi(u) cosh(bu)du` gives

\[
\partial_TD_T(b)=\operatorname{Cov}(u^2,u\tanh(bu))\ge0. \tag{16}
\]

The two functions are increasing; the covariance is one half the double
integral of the product of their increments. Super-exponential decay
justifies differentiation. Thus acquisitions at both exact rational time
endpoints enclose every time in (1), with no time mesh or interpolation.
Conservative readable bounds are:

| b | Actual `D_T(b)` throughout the time interval |
| --- | --- |
| 20 | `[0.2041296865, 0.2041296928]` |
| 40 | `[0.3336081998, 0.3336082066]` |
| 80 | `[0.4849096493, 0.4849096549]` |

These are full-source enclosures. Their widths are mainly actual time
variation, not quadrature uncertainty. The checker keeps tighter balls;
the [record][record] gives each endpoint integral, all separate allowances,
actual profile intervals, arithmetic/library version and source hashes.
Both precision runs use the same implementation; they are not independent
certificates from different algorithms.

## 5. A positive relaxed measure at every actual theta vector

Fix any `(T,a)` in (1) and any `d in (0,1/2]`. Put

\[
y_*=(a+d)^2,\quad (y_1,y_2,y_3)=(900,1600,25000),
\quad M_{ij}=\frac{y_j+400}{y_j+B_i},\quad i=0,1,2.
\]

The matrix has exact determinant `761319/21775900>0` and exact inverse

\[
M^{-1}=\begin{pmatrix}
231775/30366&-34675/2169&286525/30366\\
-4064/567&19000/1053&-91688/7371\\
20881/39042&-522025/253773&1524313/507546
\end{pmatrix}.                                         \tag{17}
\]

Define **exact**, data-dependent weights by

\[
(w_1,w_2,w_3)^t=M^{-1}
 \left(\frac{D_T(b_i)}{b_i}-\frac4{s+B_i}
                         -\frac2{y_*+B_i}\right)_{i=0}^2.
                                                               \tag{18}
\]

Interval evaluation of (18), using the complete profile balls above,
`s in [1001^2,1002^2]` and the enclosing
`y_* in [1001^2,(1002+1/2)^2]`, proves uniformly

\[
w_1>0.0017583,\qquad w_2>0.0019438,\qquad
w_3>0.0064978,\qquad\hbox{in particular }w_j>1/1000.    \tag{19}
\]

The independent interval treatment of `s,y_*` only enlarges the box;
no relation between them is lost in a favorable direction. Positivity
holds even on this enlargement and down to the excluded limit `d=0`.
The bounds (19) are conservative decimal rational consequences of the
recorded balls; the program checks the simpler exact floor `1/1000`.

The finite positive measure

\[
\mu_d=\sum_{j=1}^3w_j\delta_{y_j}
                  +\frac2{y_*+400}\delta_{y_*}          \tag{20}
\]

therefore satisfies **exactly** `integral phi_i dmu_d=R_i(T,a)`.
Equations (17)--(18) are exact definitions at the actual values, not a
floating fit or a claim that interval overlap proves equality. The
interval computation proves that these exact weights are positive.
No zero or negative zero-square is used, and `mu_d({s})=0` for `d>0`.

All slack nodes lie below `(a-1)^2`, while `y_* in I_a`. Hence

\[
\int w_{I_a}\,d\mu_d=1.                               \tag{21}
\]

Every global majorant in Section 3 consequently has

\[
\boxed{\ \sum_i c_iR_i(T,a)\ge1.\ }                   \tag{22}
\]

This holds at the **exact actual theta vector**, even with zero acquisition
error. Thus a sound paid upper objective cannot be below one either.
For comparison the direct constant majorant
`g=(1003^2+400)/2` is globally valid for all intervals in (1), but its
actual objective is in `[5133.9408,5133.9451]`; this is only a simple
matched baseline, not a claimed optimum. Equation (22) rules out the
requested count threshold for every majorant in this full three-dimensional
span; the exact optimum need not be found.

Finally the inserted atom alone contributes

\[
\int k_s\,d\mu_d\ge
\frac{2(s+y_*)}{(s-y_*)^2}
=\frac1{d^2}+\frac1{(2a+d)^2}>\frac1{d^2}.              \tag{23}
\]

At each fixed exact `(T,a)` the same observation vector therefore permits
arbitrarily large relaxed values of (9). This does not assert that the
physical theta roots have a small gap or that fractional slack weights
are realizable by zeros. The result specifically identifies the loss
from replacing the residual integer zero configuration by arbitrary
finite positive weighted measures subject to just (6).

## 6. Controls, what is completed, and the stopping scope

The checker separately verifies the exact rational model
`F(z)=(z^2-a^2)^2(z^2-(a+1/2)^2)/F_numerator(0)` at `a=1001`.
Its own profile is `D(b)/b=4/(s+B)+2/(y_*+B)`, its residual count is
exactly one, and its deflated contribution equals the right side of
(23). The even quartic has zero residual measure. These test the event
subtraction, multiplicity, weighted count and kernel factors without
substituting theta observations into a control.

| Control | Premise and actual treatment |
| --- | --- |
| Polynomial neighbor control | Its own paired product and own profile give exact count one; a valid global dual cannot falsely certify zero. It has no theta source. |
| Note 05 exact finite-profile families | Their known nearby roots force the same unit-count obstruction for their **own** profile vectors whenever the interval contains that root. No equality to the theta vector is asserted. |
| Positive atomic/continuous threshold families | Positivity and actual threshold geometry alone do not determine the three theta observations. If a nearby residual root lies in `I`, (10) preserves it. They fail the unchanged complete theta coefficients/profile data. |
| Euler-factor controls | Their own time-zero logarithmic derivative differs from theta by the documented positive term. They are not assigned the theta samples or source-error constants; any application must first verify their own all-real slice and exact multiplicity. |
| Weighted-square and finite-prime controls | Their documented local events do not provide the all-real-threshold premise of (3); no positive residual root measure of type (5) is inferred from those events. |
| Reflected smooth and positive-primitive controls | Their shape and reflection do not identify the complete theta source or its actual profile vector. No invented all-real event or numerical profile is assigned. |

The new input can in principle distinguish the old constructed-profile
families, because it uses specified complete theta values rather than
common floors or constructed vectors. What the certificate shows is
more precise: **this particular actual vector still lies inside the
larger positive-measure relaxation with a nearby unit-count atom**.
It is not enough to distinguish all admissible relaxed observations.

P1 is complete as an observation-model proof plus a concrete failed
actual-data experiment. P2's count threshold cannot be reached in this
contract, so P2 is not activated; P3 has neither a paid gap nor a bounded
relaxed `S_2`. No signed `Q_L` improvement, physical exclusion, winding,
Newman bound or multiplicity transfer follows. A future attempt must
change retained information or the feasible class quantitatively; merely
increasing precision on these same three observations cannot alter (22).
The theorem does not prohibit another finite schedule, integer-sensitive
methods, arithmetic zero counts, or estimates using the complete theta
source directly. Such a change requires a new bounded contract, not an
unreported extension of this failed one.

The source manifest in the record binds the working-tree references and
checker over Git parent `574b658061c5144a78d44a805fe2c116d86f9397`.
Hashes identify the inputs; the analytic arguments and outward inequality
checks carry the claims. The small files follow [LARGE_FILES.md][large].

[results]: ../../../../../../../result-summaries/README.md
[arithmetic]: ../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[program]: ../../../research-overview/03_FOURTH_ORDER_ARITHMETIC_AND_ACTUAL_PROFILE_PROGRAM_20261020.md
[previous]: 05_FINITE_PROFILE_CONDITIONING_OBSTRUCTIONS_20261020.md
[product]: 03_IMAGINARY_AXIS_JET_BOUND_20261019.md
[source]: ../../01_local_double_winding/notes/02_PAIRED_FACE_CONTRACT_20261019.md
[coverage]: ../../../../../11_arithmetic_collision_rigidity/notes/02_updated_research_plan/14_SHARPER_OUTER_EXCLUSION_AND_CONSTANT_DISTANCE_CONTOURS_20261018.md
[checker]: ../numerics/certify_actual_profile_relaxation.py
[record]: ../numerics/ACTUAL_PROFILE_RELAXATION_20261020.json
[polymath]: https://arxiv.org/html/1904.12438v2#S3
[bp]: https://flora.insead.edu/fichiersti_wp/inseadwp2004/2004-62.pdf
[bgy]: https://dimabatenkov.info/pdf/batenkov2019a.pdf
[large]: ../../../../../../../LARGE_FILES.md

Separate same-model proof/code review and fresh parent replay are recorded in the [round assessment](../../../reviews/03_FOURTH_ORDER_AND_ACTUAL_PROFILE_ROUND_REVIEW_20261020.md) and its source/replay receipt. These are internal LLM checks, not specialist review or independent full-source implementations.

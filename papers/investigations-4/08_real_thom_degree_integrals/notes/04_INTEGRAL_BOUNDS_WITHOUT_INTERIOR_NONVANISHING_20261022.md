# Integral bounds without an interior nonvanishing premise

22 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual coordinating model **gpt-6.1-sol (Codex)**, reasoning effort **ultra**, verified from current turn metadata. Status: bounded complete-source interval estimate and elementary polynomial control; separate same-model internal review, no specialist validation.

**The bounded answer is yes.** On the inherited theta rectangle, a complete integral upper bound below 0.699 is obtained while nine retained interior first-jet interval rectangles still contain the origin. Boundary nonvanishing is supplied separately; no complete pointwise interior certificate or boundary winding is used to obtain the upper bound. This answers a proof-method question on previously covered data, not an improvement in coverage or acquisition cost. The method uses a positive-part majorant and obtains no theta cancellation benefit.

The [contract](03_INTEGRAL_BUDGET_COMPARISON_CONTRACT_20261022.md), [checker](../numerics/check_real_thom_integral_budget.py), [receipt](../numerics/REAL_THOM_INTEGRAL_BUDGET_20261022.json) and [internal review](../reviews/02_ACTIVE_BULK_COMPARISON_INTERNAL_REVIEW_20261022.md) retain the full assumptions and accounting. Follow the [result index](../../../../result-summaries/README.md), [avoid index](../../../../avoid/README.md), [collision controls](../../../../result-summaries/12_collision_controls_and_screening.md) and [local-geometry cluster](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), especially avoid/[01](../../../../avoid/01_restating_the_target.md), [07](../../../../avoid/07_scoped_exclusions_read_as_universal.md), [11](../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md) and [12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).

## 1. What must be bounded

For the unchanged physical backward-heat map F=(H,H_x), put L1=H_xx²-H_x H_xxx and E=|F|². For a regular bounded domain, all boundary components oriented by dt wedge dx, and a smooth nonnegative normalized target density supported inside a ball below the boundary floor,

\[
 I_r(D)=\int_D\rho_r(F)L1\,dt\,dx=K(D)
       =\sum_{F(p)=0}\lfloor m_p/2\rfloor\in\mathbb Z_{\ge0}.
\]

The identity is inherited, as in [Note 02](02_SUPPORT_REJECTION_AND_CONTROL_ANALYSIS_20261022.md). No new global criterion is claimed. A proof of I_r<1 necessarily proves interior nonvanishing as its **conclusion** under this theorem; the distinction requested by the user is that pointwise nonvanishing is not a premise or a completed preliminary certificate.

Use the same smooth density as before:

\[
 \rho_r(y)=\frac{\exp[-s/(1-s)]}{\pi r^2(1-s)^2},\quad
 s=|y|^2/r^2<1,
\]

zero otherwise, with exact normalization and maximum C_r=4/(e pi r²). Choosing r<b<min_boundary|F| retains the proper-map degree identity. Only the boundary needs this nonvanishing floor before the integer conclusion can be used.

## 2. An upper budget that accepts unresolved interior cells

Partition D into cells Q and acquire complete four-jet ranges V_j(Q) for j=0,1,2,3. Let [ell_Q,u_Q] enclose V_2²-V_1V_3, with outward rounding. If the complete first-jet rectangle misses the radius-r support disk, its integral is zero. Otherwise the universal density interval [0,C_r] gives

\[
 \int_Q\rho_r(F)L1\in
 |Q|C_r[\min(0,\ell_Q),\max(0,u_Q)].                 \tag{1}
\]

In particular,

\[
 I_r(D)\le U=\sum_{Q\text{ not support-rejected}}
             |Q|C_r\max(0,u_Q).                     \tag{2}
\]

This estimate remains valid if both H and H_x intervals contain zero. There is no division by E, no interior lower floor, and no need to decide whether support is truly met on those cells. The whole-cell range and exact area give an integral enclosure, so quadrature uncertainty is already included. Complete coefficient/quadrature/source/Taylor errors must enter V_j before forming L1. The estimate may lose cancellations: negative signed mass is retained in the lower enclosure but cannot improve this upper budget when rho has only the interval [0,C_r]. This deliberate loss is charged rather than described as a signed-cancellation advance.

Some cells are locally excluded to save integration effort. The algorithm does not require all cells to be excluded. It refines the largest positive contribution and stops when the **integral** upper is below 3/4. Only afterward does it report whether retained first-jet rectangles still contain the origin. The direct comparison is also run afterward and is absent from the proof's inputs.

## 3. Fixed tiny cutoff: the first attempt fails the requested gate

At r=10^-9, the full-time, x-only subdivision route never obtains a positive integral upper below one before every support cell has been rejected. The last remaining positive allowance is approximately 748.8531004833; splitting that cell makes the allowance zero, at 255 four-jet range calls. This reproduces support avoidance and fails the requested retained-uncertainty gate. It does not show that every bulk estimate must prove pointwise nonvanishing first. The density peak scales as r^-2 and this radius is unnecessarily small relative to what the boundary data can support.

## 4. Wider fixed cutoff: a complete theta bound below one

After recording that failure, the [contract](03_INTEGRAL_BUDGET_COMPARISON_CONTRACT_20261022.md) fixes a separate variant r=10^-7, b=1.5e-7; there is no adaptive radius tuning within a run. Domain D=[1/100,1/5] x [25,45], precision 160 bits, midpoint (21/200,35), finite modes n<=4 and source cutoff u=1 remain unchanged. The supplier is extended to 78 midpoint jets (orders 0..77) and moment bounds through 79 for H through Hxxx, with both the complete omitted-mode and all-mode infinite source-ray tails. Taylor degrees remain50 in x and 12 in t.

Boundary-only adaptive first-jet enclosures give a complete norm floor greater than 1.53909638788e-7>b, with 548 two-component range calls. No winding, endpoint polygon or interior cover pays this condition. The interval calculation then gives, with safe decimal outward rounding,

\[
 \boxed{-0.436449 < I_{10^{-7}}(D)<0.698391<1.}       \tag{3}
\]

The raw interval arises before the integer collision law is applied. The exact identity subsequently yields I_r=K=0. Crucially, the final127-cell partition retains **nine cells with positive uncertain-support allowance, all nine having origin-containing first-jet rectangles**. Thus the stopping decision is made with a complete integral bound while a complete coordinate-separation interior cover is unavailable in that partition. These are statements about complete interval rectangles, not claims that an actual collision is present or that no other argument could use the four-jet information.

Actual pullback-support nonemptiness for this wider theta kernel is **not asserted**. The previous tiny-radius certificate does not settle support at this larger r. The whole domain is inherited low-height territory, already certified without this method; that prior certificate is disclosed but not used to obtain (3). A calculation on known territory validates a distinct proof route and its accounting, not new RH evidence.

## 5. Costs and disposition

| Consumer | Midpoint-jet setup | Range calls | Component ranges |
| --- | ---: | ---: | ---: |
| Practical direct interior baseline |76 suffice; shared78 in replay |255 |510 |
| Wider compact bulk budget |78 |253 |1,012 |
| Required separate wider boundary floor |Included in those78 |548 |1,096 |
| Wider compact consumer, total |78 |801 |2,108 |

The two extra midpoint jets and stronger moment bound belong to the compact method's additional needs. Even though its bulk alone uses two fewer calls, each bulk call encloses four components; the boundary condition also costs real acquisitions. The total loses to direct in this implementation. Reusing an already acquired boundary floor removes only its marginal cost; it does not make the floor free historically, and the bulk component work still exceeds direct. Timings in the receipt are machine/run observations.

**Retain the complete bound below one as an answer to the bounded logical question. Stop this specified positive-part budget as a source of measured efficiency or coverage improvement over direct.** Correlated source estimates, signed upper improvements, other domains and amortized multi-domain costs remain separate questions. No global theta bound, new height coverage, endpoint simplicity treatment or RH result follows.

## 6. Failure controls and limitations

The same budget helper is applied to a genuine quadratic collision H=x²-2t on[-1,1]² with a paid collar. It returns an inconclusive allowance at least one. The exact compact mass is one. A finite-budget run with every actual theta jet inflated by the complete absolute moment bound remains inconclusive; an exact boundary event is refused. Nonfinite jet ranges are rejected before a sign/maximum operation can misclassify them as zero. Provenance corruption must exit nonzero without writing a successful receipt. See the independent process replay in the separate same-model review.

The [separate arithmetic controls](../../../../result-summaries/12_collision_controls_and_screening.md) retain their individual source hypotheses: Euler-factor fields alter the unchanged normalized theta source/arithmetic; weighted-square and finite-prime controls fail their full source-reflection premise; reflected and primitive-compatible fields fail the unchanged normalized square expansion. The generic cell bound (1) applies to each matching control too, and on a regular enclosing domain it must enclose that control's positive event count. No control is claimed excluded by shape alone. Positive-time domains still miss t=0 events.

## 7. A genuinely active signed integral with an explicit bound below 0.86

The theta computation retains uncertain support but does not prove actual support activity. The following exact heat-polynomial example separately shows that even genuinely active signed support can admit a global upper allowance below one without an interior nonvanishing premise. It is a formula/estimator control; direct exclusion is easy there as well, so no computational advantage is inferred.

### 7.1. The field, kernel and claim

Let
\[
 D=(-1/2,1/2)_t\times(-1/2,1/2)_x,\qquad
 H(t,x)=x+t^2x-\frac t3x^3+\frac1{60}x^5.
\]
Use the physical field \(F=(H,H_x)\), orientation \(dt\wedge dx\), and
\(\mathcal L_1=H_{xx}^2-H_xH_{xxx}\). Choose
\[
 r^2=11/10,\qquad b^2=6/5.
\]
For \(s=|y|^2/r^2<1\), set
\[
 g(s)=\exp[-s/(1-s)],\qquad
 \rho_r(y)=\frac{g(s)}{\pi r^2(1-s)^2},
\]
and extend the density by zero when \(s\ge1\).

The density is smooth, nonnegative, has mass one, and is supported in
\(\overline{B_r}\Subset B_b\). The boundary jet has the strict floor
\[
 \min_{\partial D}|F|^2\ge29/24>6/5=b^2.
\]
The bulk integrand is genuinely nonzero and has both signs. Nevertheless,
\[
 \left|\int_D\rho_r(F)\mathcal L_1\,dt\,dx\right|
 \le \frac{186040}{25344\,e\pi}
 < \frac{363359375}{422593281}
 < \frac{43}{50}<1.                                      \tag{1}
\]
The compact degree identity and nonnegative-integer event law therefore
give \(K(D)=0\). The proof of (1) uses only boundary nonvanishing and a
uniform bound on the signed bulk density; it does not use an interior
first-jet nonvanishing certificate.

### 7.2. Backward heat equation and jets

Direct differentiation gives
\[
 \begin{aligned}
 H_t&=2tx-x^3/3,\\
 H_x&=1+t^2-tx^2+x^4/12,\\
 H_{xx}&=-2tx+x^3/3,\\
 H_{xxx}&=-2t+x^2.
 \end{aligned}
\]
Thus \(H_t=-H_{xx}\) exactly. Each spatial slice is a nonzero polynomial
(its leading coefficient is always \(1/60\)); analyticity and the
nonzero-slice hypothesis of the inherited physical degree theorem hold.

### 7.3. A boundary floor on all four faces

Prove the floor on the faces themselves, without obtaining an interior first-jet lower bound along the way.

On either spatial face x=±1/2,
\[
 H_x=\frac{95}{96}+(t-1/8)^2\ge\frac{95}{96},
\]
\[
 |H|=\frac12\left(1+t^2-\frac{t}{12}+\frac1{960}\right)
 \ge\frac12(1-|t|/12)\ge\frac{23}{48}.
\]
The factor in parentheses is positive, so these inequalities give
\[
 E\ge(95/96)^2+(23/48)^2
   =\frac{11141}{9216}>\frac{29}{24}.
\]
On the final time face t=1/2, |x|<=1/2 gives
\[
 H_x=\frac54-\frac{x^2}{2}+\frac{x^4}{12}
 \ge\frac98,\qquad E\ge\frac{81}{64}>\frac{29}{24}.
\]
On the initial time face t=-1/2,
\[
 H_x=\frac54+\frac{x^2}{2}+\frac{x^4}{12}
 \ge\frac54,\qquad E\ge\frac{25}{16}>\frac{29}{24}.
\]
These estimates include the corners and prove the claimed entire-boundary floor. Since 29/24-6/5=1/120>0, the required target collar is strictly paid. This proof uses no interior first-jet lower bound.

### 7.4. Exact kernel normalization and amplitude

The cutoff is flat because \(g(s)=e\exp[-1/(1-s)]\) as \(s\uparrow1\).
Near \(s=0\) the formula is analytic. Composition with \(|y|^2\) is
therefore smooth at the target origin as well as across its cutoff.
Furthermore,
\[
 -g'(s)=\frac{g(s)}{(1-s)^2},\qquad g(0)=1,\quad g(1)=0.
\]
Polar coordinates give
\[
 \int_{\mathbb R^2}\rho_r(y)\,dy
 =\int_0^1[-g'(s)]\,ds=1.
\]
Writing \(z=(1-s)^{-1}\ge1\),
\[
 -g'(s)=e^{1-z}z^2\le4/e,
\]
with equality at \(z=2\). Hence
\[
 \|\rho_r\|_\infty=\frac4{e\pi r^2}=\frac{40}{11e\pi}. \tag{3}
\]

### 7.5. A complete bulk allowance strictly below one

On the entire closed box, the displayed jets imply
\[
 \begin{aligned}
 |H_{xx}|&\le 2(1/2)(1/2)+(1/2)^3/3=13/24,\\
 |H_x|&\le1+1/4+1/8+1/192=265/192,\\
 |H_{xxx}|&\le1+1/4=5/4.
 \end{aligned}
\]
Therefore
\[
 |\mathcal L_1|
 \le(13/24)^2+(265/192)(5/4)
 =\frac{4651}{2304}.                                   \tag{4}
\]
Since \(|D|=1\), equations (3)--(4) prove
\[
 \left|\int_D\rho_r(F)\mathcal L_1\right|
 \le\int_D\rho_r(F)|\mathcal L_1|
 \le\frac{40}{11e\pi}\frac{4651}{2304}
 =\frac{186040}{25344e\pi}.
\]
This is a deliberately elementary absolute allowance for a signed
integral; it does not erase the signs in the underlying identity.

The last numerical comparison can be made rational. The exponential
series gives \(e>\sum_{k=0}^6 1/k!=1957/720>2718/1000\). Using Machin's
identity and alternating arctangent bounds (the identity is verified by the tangent addition formula for 4 arctan(1/5)-arctan(1/239), in the first quadrant),
\[
 \pi>
 16\left(\frac15-\frac1{3\cdot5^3}
              +\frac1{5\cdot5^5}-\frac1{7\cdot5^7}\right)-\frac4{239}
 =\frac{1231847548}{392109375}>\frac{3141}{1000}.
\]
It follows that
\[
 \frac{186040}{25344e\pi}
 <\frac{363359375}{422593281}
 <\frac{43}{50}.
\]
Both final comparisons are exact rational inequalities. Thus no floating
evaluation is needed for the strict threshold in (1).

### 7.6. Genuine active support and opposite signs

At \(x=0\),
\[
 F(t,0)=(0,1+t^2),\qquad E(t,0)=(1+t^2)^2,
 \qquad \mathcal L_1(t,0)=2t(1+t^2).
\]
At the two interior points \((t,x)=(\pm1/10,0)\),
\[
 E=10201/10000<11/10=r^2,\qquad
 \mathcal L_1=\pm101/500.
\]
The density is strictly positive there. Continuity gives open
positive-area neighborhoods of genuinely active positive and negative
integrand. The exact integral is zero, so this example exercises real
signed cancellation rather than support rejection.

For completeness, the smooth compact identity itself follows by putting
\(A_r(E)=1-g(E/r^2)\). The quotient \(A_r(E)/E\) extends smoothly at zero
with value \(r^{-2}\). Thus \(\alpha=A_r(E)\beta\) is smooth, and
\[
 d\alpha=-2\pi\rho_r(F)\mathcal L_1\,dt\wedge dx.
\]
On the whole boundary, \(\alpha=\beta\). Stokes and the inherited
physical index theorem then give
\(\int_D\rho_r(F)\mathcal L_1=K(D)\in\mathbb Z_{\ge0}\).
Together with (1), this forces \(K(D)=0\).

### 7.7. Scope and control screen

This is an exact regression/control calculation, not an improvement over
the strongest same-data direct method. Indeed the direct alternative is
easy: the displayed \(H_x\) is strictly positive on this box. That fact
was not used in the bulk allowance proof and should not be presented as
an unavailable source of information in a computational comparison.

The polynomial has no unchanged normalized theta source. In particular,
it is spatially odd and grows polynomially, so it does not satisfy the
theta field's even, integrable-source cosine representation. It tests
the heat equation, real degree, signed integrand, normalization, boundary
collar and integer threshold, and no theta arithmetic premise.

For the repository's separate nonpolynomial collision controls, the
compact identity applies on any regular domain enclosing their event;
an estimator using only the shared heat/degree premises must enclose the
correct positive event count there. Their distinct failed theta premises
remain distinct: Euler-factor controls alter the unchanged theta
arithmetic; weighted-square and finite-prime controls fail full source
reflection; reflected/primitive-compatible controls fail the unchanged
normalized theta square expansion. A collision-free box of a control
need not be rejected. No family is excluded by this example.

The relevant classifications are result-summaries/12 and avoid/01, /02,
/07: (1) is a numerical-threshold control estimate, rather than another
RH-equivalent criterion; its proved class is this one polynomial and
specified box/kernel. Extending it to the complete theta source requires
a separately paid bulk estimate.

#### 7.7.8. Collision calibration: shrinking support does not evade the budget

For the ordinary-double control \(H=x^2-2t\),
\[
 F=(x^2-2t,2x),\quad \det DF=-4,\quad \mathcal L_1=4.
\]
The map is a global orientation-reversing diffeomorphism with inverse
\[
 (t,x)=(y_1^2/8-y_0/2,y_1/2).
\]
Consequently its complete support preimage has exact area
\[
 |F^{-1}(B_r)|=\pi r^2/4.
\]
Suppose an estimator uses the global kernel maximum and the exact
\(\mathcal L_1=4\), but otherwise grants itself even the ideal support
geometry. Its allowance is already
\[
 \|\rho_r\|_\infty\,4\,|F^{-1}(B_r)|
 =\frac4{e\pi r^2}\,4\,\frac{\pi r^2}4=\frac4e>1.
\]
Using a superset of the true support preimage only enlarges this
allowance. Its \(r^{-2}\) density amplification cancels the \(r^2\)
support-area decrease exactly. The true compact integral is exactly
one. Thus this density-maximum times active-area estimate correctly
fails to exclude the ordinary double event at every radius; support
shrinking alone cannot force a false subunit allowance.

The calibration is scoped to this maximum-density/area allowance and
this exact quadratic map. More generally, every normalized density
supported in \(B_r\) has \(\|\rho\|_\infty\pi r^2\ge1\), so the same
ideal-geometry upper allowance on this quadratic control is at least
one. This is not a no-go statement about signed integral estimates on
other heat fields.

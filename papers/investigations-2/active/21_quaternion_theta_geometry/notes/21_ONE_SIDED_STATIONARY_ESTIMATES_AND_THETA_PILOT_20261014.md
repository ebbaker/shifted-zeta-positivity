# One-sided stationary estimates: favorable curvature and a theta pilot

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6-astra (Codex)**; reasoning effort: **ultra**.
Continues [Note 19](19_OSCILLATORY_BLOCKS_AND_PAIRED_LAGUERRE_FORMS_20261014.md)
and the author's choice to prioritize the analytic signed estimate, using
small certified computations to test its mechanisms.

**Status.** The sufficient algebraic identity below is proved. The finite
theta pilot in Section 7 is certified from the existing complete-source
record. No proper finite-block split is yet proved to satisfy the new
criterion on the unresolved region. The direct signed estimate remains
the primary target; the square criterion is an auxiliary tool with an
explicit residual-vanishing limitation.

Write \(h_k=\partial_x^kH(t,x)\), \(E=h_0^2+h_1^2\), and
\(\mathcal L_j=h_{j+1}^2-h_jh_{j+2}\). The target remains
\[
 \mathcal L_j\ge-K_jE\quad\text{on }h_{j+1}=0,\qquad j=0,1,
\]
with losses prescribed independently of an observed energy floor and
locally bounded through any candidate positive-time collision. We use
Note 19's fixed contour \(0<a<\pi/8\), prescribed real centering \(b\),
\(\mu=a^2+b^2\), and exact residual
\(C_j=-h_{j+2}-2ah_{j+1}-\mu h_j\). All source and pair integrals below
use Note 19's measure and full staircase domain; no arithmetic index or
cross term is silently omitted.

## 1. Why this is the useful modification

A bound on the entire norm of C charges large favorable curvature as an error. Instead split the exact centered residual into a prescribed candidate favorable part G and a remaining part R. The positive product h_j G_j can pay for the square of R_j. Neither the split nor the loss is defined using a quotient by E. The resulting scalar slack can be evaluated from the complete paired theta source, including every cross term.

## 2. Lemma and exact stationary-ideal identity

Write h=h_j, s=h_{j+1}, C=C_j, and E=h_0²+h_1². Retain mu=a²+b² and Note 19's exact identity

L_j=mu h²+h C+s(s+2a h).

Choose parameters kappa and rho independently of the physical jets, with

0<kappa<=mu, rho>=0,

and prescribe an exact split C=G+R. Define

\[
 \Delta_j=4\kappa h_jG_j+\rho^2E-R_j^2. \tag{F1}
\]

Then the exact identity, before imposing stationarity, is

\[
\boxed{4\kappa\mathcal L_j+\rho^2E
 =(R_j+2\kappa h_j)^2+\Delta_j
 +4\kappa(\mu-\kappa)h_j^2
 +4\kappa h_{j+1}(h_{j+1}+2ah_j).} \tag{F2}
\]

Consequently, if Delta_j>=0 on h_{j+1}=0, then

\[
 \mathcal L_j\ge-K_jE,\qquad K_j=\rho^2/(4\kappa). \tag{F3}
\]

If kappa stays locally bounded below by a positive constant and rho is locally bounded, this loss stays locally bounded through a candidate positive-time collision. For a fixed contour a>0 and b prescribed from (t,x), the choice kappa=mu automatically has the required positive lower bound a².

The proof is expansion of the square in (F2). It does not assume E>0 or divide by a physical jet. No separate sign hypothesis on h_jG_j is needed: (F1) may tolerate some adverse product. Where that product is positive, however, its full size is available to pay R_j². In particular G_j can be arbitrarily large in a favorable direction, unlike a small norm bound on the whole C_j. Taking G=0 reduces (F1) to a scalar relative residual cone, so the earlier mechanism is included as a special case.

This is genuinely only a sufficient condition. It is not a reformulation claiming that Delta_j>=0 follows automatically from L_j>=-K_jE: the nonnegative square and the extra mu-kappa term in (F2) can make the latter true while Delta is negative.

## 3. Prescribe the split from theta before testing it

Use exactly Note 19's Omega, W_alpha, q_alpha and y_alpha. Choose a real measurable multiplier m_j(alpha;t,x), bounded by a polynomial in y_alpha and the fixed parameter bounds, independently of the unknown physical energy. Define

\[
 G_j=e^{-ax}\Re\int_\Omega m_j(\alpha)W_\alpha q_\alpha^j\,d\nu,
\qquad
 R_j=e^{-ax}\Re\int_\Omega r_j(\alpha)W_\alpha q_\alpha^j\,d\nu,
\]

where

\[
 r_j(\alpha)=y_\alpha^2-b^2-m_j(\alpha). \tag{F4}
\]

Then C_j=G_j+R_j exactly. A concrete first family is

\[
 m_j(\alpha)=(y_\alpha^2-b^2)\chi_A(\alpha), \tag{F5}
\]

where A is a fixed union of common-carrier coordinate intervals and dyadic index blocks, always intersected with the original staircase d_n<=v. The block endpoints and contour/centering parameters are frozen on a closed cell before evaluating the four physical jets. A smoother prescribed cutoff is also possible. The retained G includes all correlations between its constituent blocks; individual summands are not required to have favorable phases.

The first experiment should compare a very small, declared family of such A, not choose m pointwise to force a desired Delta. A pilot can freeze a selected A for a new validation cell after exploratory selection, then certify the full cell. Any all-height theorem will require an a priori parameter rule and uniform analytic estimates for that rule. Choosing m after inspecting C/h or E, or defining rho² as R²/E, would destroy the intended content. There are also vacuous algebraic choices even without a quotient: m=y²-b²+2kappa makes R=-2kappa h_j and cancels the square in (F2). Such a choice merely repackages the desired inequality and offers no source estimate. The proposed block-filter family (F5) is intended to avoid that maneuver and expose a separately estimable retained contribution.

## 4. The precise paired theta obligation

Put

\[
 J_j(\alpha,\beta)=W_\alpha\overline{W_\beta}
 (q_\alpha\overline{q_\beta})^j+W_\alpha W_\beta(q_\alpha q_\beta)^j.
\]

For real m and r, absolute convergence gives

\[
 h_jG_j=\frac{e^{-2ax}}4\Re\iint(m_j(\alpha)+m_j(\beta))J_j(\alpha,\beta),
\quad
 R_j^2=\frac{e^{-2ax}}2\Re\iint r_j(\alpha)r_j(\beta)J_j(\alpha,\beta).
\]

Also E=(e^(-2ax)/2) Re integral integral (J_0+J_1). Thus

\[
\boxed{\Delta_j=\frac{e^{-2ax}}2\Re\iint\left[
\{2\kappa(m_j(\alpha)+m_j(\beta))-r_j(\alpha)r_j(\beta)\}J_j
+\rho^2(J_0+J_1)\right].} \tag{F6}
\]

The new theta-specific task is to prove (F6)>=0 on h_{j+1}=0, for prescribed m_j, kappa, rho. It keeps the actual carrier phases and both carrier coordinates. The source majorants in Note 19 prove integrability but do not establish this sign. Staircase entries remain those of B13–B15; source splitting does not authorize discarding entering terms.

Absolute tail errors cannot be divided by E. On a finite validated cell they can be included directly in a lower enclosure of Delta. For an all-height argument near E=0, the retained/tail decomposition must establish this homogeneous inequality itself, or another relative one-sided estimate; an absolute residual payment alone is insufficient.

## 5. Double and cubic controls

These test the algebraic mechanism, not the theta multiplier (F5).

**Closing real pair.** Let P=y²-D with D=d²+2t>0. At y=0, h0=-D, h1=0, C0=-2+mu D. Prescribe G0=-2 and R0=mu D. Then L0=2D>0 and

\[
 \Delta_0=8\kappa D+(\rho^2-\mu^2)D^2.
\]

Even rho=0 passes for 0<D<=8kappa/mu². Meanwhile |C0|/sqrt(E) grows like 2/D. The split therefore accepts arbitrarily large favorable curvature relative to E, which the old whole-residual cone cannot do at fixed rho.

**Adverse side of a double collision.** Let P=y²-2(t-T), put s=T-t>0, and take y=0. Then h0=2s, C0=-2-2mu s. With the same prescribed split G0=-2, R0=-2mu s,

\[
 \Delta_0=-16\kappa s+4(\rho^2-\mu^2)s^2<0
\]

for sufficiently small s whenever kappa is bounded below and rho is bounded. The lemma correctly refuses a bounded-loss certificate through this collision predecessor. Indeed L0=-4s and E=4s².

**Cubic collision predecessor.** Let P=y³-6(t-T)y. On h2=0 at y=0 and t=T-s<T, h0=0, h1=6s, h3=6, C1=-6-6mu s. Prescribe G1=-6, R1=-6mu s. Then

\[
 \Delta_1=-144\kappa s+36(\rho^2-\mu^2)s^2<0
\]

for sufficiently small s under the same parameter conditions, while L1=-36s and E=36s². Thus the second stationary set remains essential. On the post-collision side the leading term of Delta has the favorable sign instead.

## 6. Rank obstruction and honest scope

A precise limitation of this sufficient cone must be explicit. At a candidate first-pair zero h0=h1=0, Delta0=-R0². Therefore (F1) forces R0=0 exactly there; if the same candidate also has h2=0, it likewise forces R1=0. A finite source split generally leaves a nonzero omitted R, and its small absolute bound does not imply that vanishing. Thus this lemma improves the treatment of favorable curvature but does not by itself remove the residual-vanishing obstruction near a candidate collision. A successful source rule must prove the needed cancellation, absorb the relevant curvature into G, or move to a direct adverse-product estimate. This limitation is not a theta counterexample.

No argument can prove the necessary sign by declaring the paired kernel positive for arbitrary block amplitudes. Already on h1=0, the arbitrary-jet form L0+K E=-h0h2+K h0² is indefinite for every finite K. On h2=0 the analogous form is -h1h3+K(h0²+h1²), likewise indefinite. Prescribed multiples of the stationary derivative vanish there and cannot repair this obstruction. A valid proof must exploit actual theta source relations.

The deliverable here is therefore: an exact sufficient identity that lets favorable curvature fund an adverse residual, an explicit family of source-prescribed splits, and controls showing both the benefit and correct collision sensitivity. There is currently no proof that any member of (F5) makes Delta nonnegative throughout the unresolved theta region. A finite gap-certified pilot can test mechanism and select useful kernels, but cannot establish the needed all-height behavior merely by producing some finite K.

## 7. A genuine theta stationary branch

This pilot extracts a concrete theta example from the existing complete-source
certificate on \([100,104]\times[0,1/2]\). It shows why preserving the sign
of a stationary residual can admit favorable curvature that a prescribed
small norm cone rejects. Its centering is deliberately changed to the fixed
value \(b=1/4\); the existing saddle-based \(\eta=1/3\) cone still passes.

Let \(a=\pi/16\), \(b=1/4\), and
\(\mu=a^2+b^2\approx0.1010531422\). Use the constant positive normalization
\(Z_k=e^{\pi(101.5)/8}h_k\) throughout \(101\le x\le102\), and set
\(\widehat C_j=-Z_{j+2}-2aZ_{j+1}-\mu Z_j\).

For **every** \(t\in[0,1/2]\), there is exactly one point
\(x_*(t)\in(101,102)\) with \(h_1(t,x_*(t))=0\). This is a genuine
physical stationary branch, rather than a selected point where a derivative
is merely small. The paid endpoint Taylor enclosures give

\[
 Z_1(t,101)>37,\qquad Z_1(t,102)<-20,
\]

and the original whole-cell enclosures give \(Z_2<0\) throughout the strip.
The intermediate value theorem gives existence, and strict decrease in
\(x\) gives uniqueness. Since the derivative \(h_2\) never vanishes,
the implicit function theorem also supplies a smooth stationary branch.

On this branch, the exact stationary identity and stored whole-cell bounds
prove

\[
 \begin{gathered}
 Z_0>0,\qquad \widehat C_0=-Z_2-\mu Z_0>0,\\
 Z_0\widehat C_0>6000,\qquad \widehat C_0-\mu Z_0>7/5,\\
 \mu Z_0^2+Z_0\widehat C_0>9400.
 \end{gathered}
\]

Consequently the desired signed estimate holds here with the prescribed
loss \(K_0=0\):

\[
 h_0C_0>0\ge-\mu h_0^2-0\,E,
 \qquad \mathcal L_0=\mu h_0^2+h_0C_0>0.
\]

The two-component cone at the prescribed budget \(\eta=\mu\) nevertheless
fails at every point of this branch. Indeed \(E=h_0^2\) at genuine
stationarity, and \(\widehat C_0>\mu Z_0>0\) gives

\[
 \mu^2Z_0^2-\widehat C_0^2-\widehat C_1^2<0.
\]

The exact enclosure even proves that this normalized cone slack is less
than \(-78\). Therefore every cone budget \(\eta\le\mu\) fails as well.
Those are the budgets that would make the generic first-stationary cone
consequence \(\mathcal L_0\ge(\mu-\eta)E\) nonnegative. The signed
observation instead retains the favorable term \(h_0C_0\).

The entire proof is obtained by exact rational arithmetic from the eight
stored cells with spatial interval \([101,102]\), including all their
center-jet enclosures and space/time payments. To certify the endpoint
signs, the same paid heat/space Taylor polynomial is evaluated at the
signed displacements \(-1/2\) and \(+1/2\), retaining the whole time
interval for each slab. Both stored remainder payments are added in full.
The input driver and contour source hashes are checked. All source tails
and numerical quadrature errors are inherited from the complete-source
certificate; no truncated source is substituted. No new quadrature is run.

The [exact driver](../numerics/check_stationary_favorable_curvature_pilot.py)
and [receipt](../numerics/STATIONARY_FAVORABLE_CURVATURE_PILOT_20261014.json)
record this extraction.
All eight closed time slabs pass, and the displayed conservative rational
margins are checked explicitly. Decimal displays in the receipt are for
convenience; decisions use exact fractional endpoints.

This controlled centering comparison has narrow scope. It does **not**
show failure of the original natural-centering \(\eta=1/3\) cone, nor
failure of every possible norm cone. A larger cone budget could still hold.
It makes no statement near an unknown collision and adds no height coverage.
The fixed \(K_0=0\) estimate comes directly from signed products; it is not
obtained by dividing an adverse remainder by an energy lower bound. The
example supports the choice to study signed stationary curvature directly,
while leaving the all-height estimate completely open.

For the auxiliary split criterion this pilot takes \(G_0=C_0\),
\(R_0=0\), \(\rho=0\), and \(\kappa=\mu\). It therefore certifies a
favorable full residual, not a proper finite-block decomposition. In this
section \(\widehat C_j\) denotes the normalized whole residual and must
not be confused with the split remainder \(R_j\) in Sections 2–6.

## 8. How the two routes should work together

The analytic route leads. The next question is which explicit theta
correlation controls the adverse part of the stationary product. A bound
on all possible source phases is ruled out by Section 6. The exact shared
arithmetic carrier, its paired products, and the full staircase boundary
terms are the information that a valid theta proof must exploit.

A direct alternative to the square criterion is to prove, on the relevant
stationary set, separately estimable inequalities
\[
 h_jG_j\ge-\alpha_jE,\qquad h_jR_j\ge-\beta_jE,
 \qquad\alpha_j,\beta_j\ge0.
\]
Require \(\alpha_j\) and \(\beta_j\) to be locally bounded through
candidate collisions. Then \(\mathcal L_j\ge-(\alpha_j+\beta_j)E\). These product estimates
allow \(R_j\ne0\) at \(E=0\), although their validity in a whole
neighborhood is still a substantive theta-specific obligation. For
example, a genuine source identity
\(R_j=A_jh_0+B_jh_1\) with locally bounded, independently prescribed
coefficients supplies \(|h_jR_j|\le\sqrt{A_j^2+B_j^2}E\). Fitting those
coefficients by dividing by physical jets would not establish such an
identity.

The next bounded experiment should freeze a small family of proper
source blocks, such as \(A=\{(v,n):d_n\le v\le V,\ n\le N\}\), before
certification. Retain both coordinates of every signed product and pay
all omitted pairs. Test both genuine stationary sets. Report whether
favorable retained curvature, an adverse residual product, or a tail
payment determines the verdict. Validate any exploratory parameter choice
on an additional declared cell. A computation on an already nonvanishing
compact cell should use a prescribed loss, not manufacture one from its
positive energy minimum.

Before attempting an all-height statement, the chosen family must explain
how its error scales relative to the physical jet near a possible
collision. A small absolute error does not do this. A useful stopping
criterion for a proposed square method is failure to supply the exact
residual cancellation identified in Section 6; a useful positive outcome
is a source identity or signed correlation that survives this test.
The outer threshold and explicit height improvements remain supporting
results rather than the current main workstream.

## 9. Validation and replay

The [internal review](../reviews/15_ONE_SIDED_STATIONARY_ESTIMATES_REVIEW_20261014.md)
checks the algebra, controls, endpoint transport, and finite scope. The
[split checker](../numerics/check_signed_curvature_split.py) and its
[receipt](../numerics/SIGNED_CURVATURE_SPLIT_IDENTITY_CHECKS_20261014.json)
provide exact polynomial checks; they do not prove the theta sign in (F6).
The pilot reuses the original
[complete-source record](../numerics/THETA_CENTERED_RESIDUAL_100_104_20261014.json),
whose underlying quadrature and analytic payments remain inputs.

From this investigation's `numerics/` directory:

```sh
python3 check_signed_curvature_split.py --output /tmp/inv21-split-replay.json
python3 check_stationary_favorable_curvature_pilot.py \
  --record THETA_CENTERED_RESIDUAL_100_104_20261014.json \
  --driver certify_phase_centered_residual.py \
  --contour-source check_shifted_contour_payments.py \
  --output /tmp/inv21-favorable-replay.json
```

These additions do not change the manuscript, extend the height-104 cover,
or establish the unresolved all-height stationary estimate.

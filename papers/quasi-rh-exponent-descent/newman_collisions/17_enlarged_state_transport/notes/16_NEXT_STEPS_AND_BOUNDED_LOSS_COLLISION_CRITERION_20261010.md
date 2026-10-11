# Next steps and a bounded loss criterion for heat collisions

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); the active reasoning effort is not exposed to this
session and is not inferred. The derivation and separate-agent checks are
internal LLM work, not independent mathematical validation.

Assessment of investigation 17 at repository commit `e766712`, including
the signed continuation `21a386c` and manuscript integration `22d6977`.

The best next investment is a theta-specific, one-sided bound for the signed
carrier response near a vanishing joint first jet. The collision argument
can be weakened: it does not require nonnegative stationary Laguerre
expressions. A locally bounded negative allowance proportional to
\(H^2+H_x^2\) is sufficient. The criterion and proof below are a new
deduction from the existing predecessor lemma. No bound of this kind is
proved here for the genuine theta source.

## What the latest progress changes

[Notes 9–10](9_PAIRED_CONTOUR_BOUNDS_ON_THE_SHRINKING_SECTOR_20261010.md)
have completed the matched-contour checkpoint: the complete source,
endpoint cancellation, complex physical disks and a product remainder are
available. Repeating an unrestricted Mellin transformation does not supply
the missing sign; its complete time-zero transform recovers a completed-zeta
product, while raw positive-time full-line channels are divergent.

[Note 12](12_EXACT_CARRIER_DEFECT_AND_CUTOFF_EDGE_MASS_20261010.md)
identifies the signed defect exactly and proves that absolute coefficient
costs leave no fixed asymptotic reserve. [Note 13](13_PHASE_CURRENTS_RELATIVE_CONES_AND_BANDWIDTH_OBSTRUCTION_20261010.md)
rules out an argument from positive weights and narrow bandwidth alone.
[Note 14](14_FIXED_PRODUCT_SADDLES_AND_SIGN_OSCILLATION_20261010.md)
rules out nonnegativity of individual fixed product channels at time zero;
it does not refute a positive-time conditional statement for the full sum.

[Note 15](15_NONVACUOUS_HIGH_HEIGHT_SECOND_STATIONARY_SIGN_20261010.md)
certifies a nonempty high-height \(H_{xx}=0\) branch, conditional on the
complete disk input, and pays the third-jet error of about 472.219.
Its normalized slope lies between -46.194 and -44.407. Thus it resolves a
calibration question without testing the small-signal limit or adding
collision coverage. The existing [integration review](../reviews/8_SIGNED_RESULTS_MANUSCRIPT_INTEGRATION_REVIEW_20261010.md)
correctly preserves this distinction.

## A weaker sufficient collision criterion

Let \(H(t,x)\) be jointly real analytic on an open
\(\Omega\subset(0,\infty)\times\mathbb R\), satisfy
\(H_t=-H_{xx}\), and have finite spatial multiplicity at the zeros under
consideration. Set
\[
E(t,x)=H(t,x)^2+H_x(t,x)^2.
\]

**Proposition.** Suppose nonnegative functions \(C_0,C_1\) are locally
bounded on \(\Omega\), and throughout that set
\[
H_x=0\quad\Longrightarrow\quad HH_{xx}\le C_0E,
\tag{BL0}
\]
\[
H_{xx}=0\quad\Longrightarrow\quad H_xH_{xxx}\le C_1E.
\tag{BL1}
\]
Then \(H=H_x=0\) has no solution in \(\Omega\).

Equivalently, the stationary restrictions of the two Laguerre expressions
may be negative, but not more negative than a locally bounded multiple of
the squared joint first jet. The theorem has no divisions in its
hypotheses and requires no globally uniform constant as \(t\downarrow0\)
or \(|x|\to\infty\).

**Proof.** Suppose a multiple zero occurs at \((T,a)\in\Omega\), and
write \(h=T-t>0\). For an even multiplicity \(2r\), the
[predecessor lemma in Note 5](5_STATIONARY_SIGN_CRITERION_AND_THETA_TARGETS_20261010.md)
gives an earlier curve \(\chi(h)=a+hy(h)\), with \(y\) analytic,
on which
\[
H_x=0,\qquad
H=ch^r+O(h^{r+1}),\qquad
H_{xx}=rc h^{r-1}+O(h^r),\qquad c\ne0.
\]
Consequently \(E=H^2>0\) for small positive \(h\), and
\[
\frac{HH_{xx}}{E}=\frac rh+O(1)\longrightarrow+\infty.
\]
This contradicts (BL0) and local boundedness at \((T,a)\).

For odd multiplicity \(2r+1\ge3\), apply that lemma to \(F=H_x\).
Its earlier curve has
\[
H_{xx}=0,\qquad H_x=ch^r+O(h^{r+1}),\qquad
H_{xxx}=rc h^{r-1}+O(h^r),\qquad c\ne0.
\]
On the same curve \(H=O(h^{r+1})\). To check this last assertion,
use the convergent heat Taylor expansion
\[
H(T-h,a+hy(h))=
\sum_{p,q\ge0}\frac{\partial_x^{2p+q}H(T,a)}{p!q!}
h^{p+q}y(h)^q.
\]
If \(p+q\le r\), then \(2p+q\le2r\), so every such coefficient
vanishes. Joint analyticity justifies grouping this convergent series.
It follows that
\[
E=c^2h^{2r}(1+O(h)),\qquad
\frac{H_xH_{xxx}}E=\frac rh+O(1)\longrightarrow+\infty,
\]
contradicting (BL1). Openness supplies the earlier-time neighborhood and
\(h<T\) keeps time positive. This covers all finite multiplicities. QED.

The proof can be restricted to an open subset containing every possible
joint zero in a stated target domain. Its precursor branches eventually
remain in that subset. Such localization must be proved; deleting
unfavorable stationary points from the domain is not a substitute.

The \(H^2\) term in (BL1) matters: it avoids requiring a slope-relative
bound at a stationary point where \(H_x\) vanishes but \(H\) is already
separated from zero. The estimate is focused on possible joint zeros.
Local boundedness must hold up to the candidate point; a coefficient
defined by an uncontrolled inverse power of \(E\) does not meet the task.

## The corresponding complete carrier target

Use Note 12's exact physical operator and notation, on its domain where
\(b\) and \(\Omega\) are nonzero:
\[
D=\partial_x^2-a\partial_x+b,\quad R=DH,\quad
\mathcal R=R'-\frac{b'}bR,\quad
B=b-a'+a\frac{b'}b.
\]
All primes here mean physical spatial differentiation at fixed time and,
for finite approximants, fixed cutoff. The two exact stationary identities
are
\[
-HH_{xx}=bH^2-HR\quad(H_x=0),
\]
\[
-H_xH_{xxx}=BH_x^2-H_x\mathcal R\quad(H_{xx}=0).
\]
The second is Note 12's identity; the first follows directly from \(DH=R\).
Thus a sufficient common-source target is
\[
HR\le(b+C_0)H^2\quad(H_x=0),
\tag{CR0}
\]
\[
H_x\mathcal R\le BH_x^2+C_1(H^2+H_x^2)
\quad(H_{xx}=0),
\tag{CR1}
\]
with \(C_0,C_1\) locally bounded. These are one-sided signed product
bounds. No favorable sign for each arithmetic component, fixed positive
reserve, or absolute smallness of \(R\) or \(\mathcal R\) is required.
The physical inequalities (BL0)–(BL1) remain available outside the carrier
operator's domain.

This weakening does not make the source estimate automatic. Near a joint
zero its allowed loss still vanishes quadratically in the observed first
jet. Note 12's absolute Cauchy remainders must therefore be improved,
correlated, or bypassed by an exact complete-source estimate in that regime.

An elementary example explains why absolute residual dominance is an
unhelpful extra demand. At \(x=0\),
\[
H(x)=x^3/3-\epsilon^2x
\]
has \(H_{xx}=0\), \(H_x=-\epsilon^2\), \(H_{xxx}=2\), and three
real zeros. Its favorable ratio is
\(q_{\rm eff}=-H_{xxx}/H_x=2/\epsilon^2\). For \(B>0\), the stronger
condition \(|\mathcal R|\le B|H_x|\) forces
\(|B-q_{\rm eff}|\le B\), hence \(q_{\rm eff}\le2B\), and fails for
small \(\epsilon\) despite the favorable sign. The local family
\(H_t=x^3/3-[\epsilon^2+2(t-t_0)]x\) obeys the backward heat equation.
This is a method control, not a claim about the theta source.

## Recommended sequence of work

1. **Test the bounded-loss target near small joint first jets.** Adapt the
   existing scalar physical-jet machinery to enclose complete stationary
   candidate sets in connected windows at several scales. Record
   \(K_j=H^{(j)}/A\), the energy \(K_0^2+K_1^2\), the signed products
   \(K_0K_2\), \(K_1K_3\), and the corresponding carrier responses.
   Focus refinement on the smallest first jets relative to surrounding
   derivative and source scales. Retain all unresolved cells; do not select
   only branches with a large separated slope. Ratios are diagnostics only
   after the denominator has a positive lower enclosure.

   A negative stationary Laguerre value would reject the stronger
   nonnegativity target at that point, but would not reject (BL0)–(BL1).
   Conversely, any finite collection of bounded ratios is only diagnostic.
   The success test is an independently justified source bound with a stated
   dependence on \(t,x\), locally finite near every possible collision.
   Fitting the constants to the measured scalar ratios would be circular.

2. **Develop a positive-time matched asymptotic only if it controls that
   signed target.** The substantive analytic continuation is uniform in
   growing \(P\), including the transition near \(P=x/(4\pi)\), its
   local \(\sqrt{x}\) width, balanced-divisor fluctuations, full heat
   weights, and endpoint partners. It must control the bulk and remaining
   sum as well. Note 9's available absolute cutoff is still
   \(M=O(x\log x)\); the geometric transition width is not a proved
   shorter cutoff. A fixed-product time-zero expansion with a formal heat
   multiplier is insufficient. The desired improvement is one-sided control
   of (CR0)–(CR1), with any approximation error compatible with the vanishing
   energy, rather than another absolute upper norm.

3. **Use phase currents as an optional competing diagnostic.** Note 13's
   endpoint-subtracted complex channel has a well-defined fixed-contour jet.
   It needs its own complex approximation and tail payment. The retained
   disk bound for the real physical observation does not identify that
   complex channel: adding a purely imaginary analytic channel can leave
   \(H\) unchanged while altering both currents. Keep contour height fixed
   during differentiation and handle complex-channel zeros explicitly.
   A cone failure abandons that sufficient cone, not the scalar target.

4. **Maintain the coverage ledger below alongside the analytic work.** A
   local source theorem should state exactly which part of it is covered.
   Extending a method to another isolated favorable cell is not the next
   proof milestone.

## Coverage and the approximation dependency

The current sector is
\[
0<t\le1/20,\qquad1\le\kappa=t\log(x/(4\pi))\le3/2.
\]
The [parent eventual-exclusion corollary](../../newman_collision_reductions.tex)
can be used pointwise with \(\varepsilon=t\): for \(0<t\le1/2\),
joint zeros are excluded when \(|x|\ge e^{64/t}\). Therefore for
\(x>4\pi\) the remaining candidate range has
\[
0<\kappa<64-t\log(4\pi).
\]
The ledger still contains bounded heights, \(0<\kappa<1\),
\(3/2<\kappa\lesssim64\), and \(1/20<t\le0.22\). The regime
\(\kappa\to0\) can contain unbounded heights; it is not automatically a
compact remainder. Negative heights follow by the genuine even symmetry.

Every closed target needs an open predecessor neighborhood, including
below its lower time edge and across spatial boundaries. Finite-sum
implementations also need compatible coverage across natural-cutoff changes.
For the endpoint, complete coverage for a sequence
\(\varepsilon_n\downarrow0\), using the parent's threshold/no-escape
reduction, would suffice. Neither the original sign theorem nor the relaxed
criterion makes disconnected bounded cells into such a covering.

The basic threshold property and the established bound \(\Lambda\le0.22\)
are supplied by [Polymath's heat-flow paper](https://arxiv.org/html/1904.12438v2),
not by the present research. This assessment does not independently reprove
the parent global reduction.

The imported disk is a dependency to audit, not a missing derivation to
rebuild before pursuing exact-source estimates. The parent already proves
its proposition “Complete shrinking-time error,” label `sc:paiderror`, on
the broader \(1\le\kappa\le2\) sector. It includes reflection,
normalization, cutoff changes and all center jets; its ledger ends with
\(1.3(1.01+2.6+.01)=4.706<5\). A precise proposition reference and scoped
source audit would clarify investigation 17's conservative assumption label.
The high-height certificates retain their stated conditional status here.

## Secondary routes and stopping rules

Keep arithmetic descent as a separate secondary task. The proposed raw
fixed-character moment at row exponent \(30/41\) would, under the
declared quantitative \(11/12\) starting input, give \(33/41\).
[Note 11](11_QUASI_RH_PRIME_COUNTING_AND_GROWING_COFACTOR_FILTERS_20261010.md)
obstructs selected cofactor filters, not the complete moment: complementary
columns may cancel their response. A productive next subproblem would
adapt the adjacent [deletion-mode covariance ledger](../../../short_families/notes/29_DELETION_MODE_COVARIANCE_AND_FULL_RESPONSE_LEDGER_20261009.md)
to the raw response and prove a native conditional-mean/covariance estimate.
Its older transformed-tail exponents cannot be copied into the new task.
Fixed losses and a fixed row length still leave an endpoint gap.

Do not spend the main effort on unrestricted pointwise transport
optimization: [Note 2](2_SHARP_ADJOINT_RESIDUALS_AND_RESTRICTED_PRIME_OBSTRUCTION_20261010.md)
proves its equivalence to scalar separation, and the two-prime graph has an
explicit obstruction. Likewise, further generic positive lifts, unsigned
source norms, individual-product positivity and favorable isolated cells
do not address the remaining estimate.

The next substantive milestone is a complete-source bound of type
(BL0)–(BL1) or (CR0)–(CR1), on a stated open candidate region, with loss
locally bounded through the small-first-jet limit. The criterion above
reduces what must be proved; it supplies no genuine-theta estimate, new
certified collision domain, or RH conclusion.

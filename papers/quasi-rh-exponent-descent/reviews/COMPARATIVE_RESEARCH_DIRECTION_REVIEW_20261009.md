# Comparative assessment of the quasi-RH research programs

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration. The exact serving variant
and configured reasoning effort are not exposed and are not inferred.
Parallel reviews used the same inherited model configuration; they are
internal checks, not independent specialist validation.

**The mixed-character program remains the leading candidate for new
arithmetic research aimed at a first improved quasi-RH bound, but its lead
should be conditional on a proof-producing checkpoint.** Character
amplification is its parent application, rather than an independent
competitor. The most concrete near-term deliverable is to consolidate and
independently audit amplification's existing geometry-only conditional
candidate. The latest centered fourth-moment route is a promising way to
attack the missing arithmetic, but it is a stronger sufficient target than
the original restricted mixed second moment. It should not become the
exclusive objective merely because it has accumulated more reductions.

This recommendation changes the primary arithmetic ranking in the
[8 October strategic review](STRATEGIC_REVIEW_20261008.md). That review
favored short families before the subsequent complete-cofactor tests and
mixed Notes 21–29. The later short-family barriers give substantive reasons
for the change. Neither the new ranking nor the number of successful sector
removals establishes a probability of success or proximity to RH.

The comparison covers all five current branches of
`papers/quasi-rh-exponent-descent`, the adjacent
[character-amplification manuscript](../../quasi-rh-character-amplification/manuscript.tex),
and its geometry, profile, common-signal, and off-balance investigations.
It builds on the [mixed progress and literature review](MIXED_PROGRESS_AND_LITERATURE_REVIEW_20261009.md).
The reviewed checkout is HEAD `348cb46dd12ec32eebcf14c4ef0317a400d01409`
with existing uncommitted research additions, including mixed Note 29.
The assessment concerns the current working files, not just the committed
snapshot. No manuscript, existing note, numerical record, or history file
was changed for this review.

| Program | Most useful current result | Decisive remaining obstacle | Recommended role |
| --- | --- | --- | --- |
| Character amplification: geometry | Exact continuous exponent certificate for the conditional boundary \(7/8-1/24000\), with separate low, moment, and contour transfer audits | Consolidation and validation of the substantial imported analytic machinery | First near-term theorem audit |
| Mixed inverse/plain correlation | Quantified detector payoff, a small application region, and exact signed residuals with controlled discarded sectors | A new estimate for the actual surviving signed aggregate; then full application closure | Main new arithmetic investigation |
| Short sextic families | Direct fixed-character strip extraction from one short-family moment, without an initial strip assumption in that deduction | More than a quarter-power improvement over the generic physical-row envelope; complete signed cofactor blocks remain large | Strongest alternative arithmetic lane |
| Newman collisions | Effective approximation and derivative interface, explicit eventual collision exclusion at each positive time floor | Compact certification and a new mechanism as the time floor tends to zero | Bounded certification or Newman-bound side project |
| Fixed-scale descent | Exact zeta-only contraction criterion and complete prime-profile comparison | A negative covariance margin; existing identities retain off-critical zero poles | Narrow exploratory lane |
| Integer quadratic lift | Exact response lift and low-conductor localization using simpler arithmetic | Signed prime-pair cancellation beyond the quadratic sieve, with a stronger family consequence | Defer without a specific new estimate |

**Amplification supplies both a near-term result and the benchmark for the
mixed investigation.** Its geometry candidate is

\[
\sigma_0=\frac{20999}{24000}=\frac78-\frac1{24000}
\simeq0.8749583333.
\]

It changes the total physical prime-slot length to \(1001/6000\), keeps
\(b=1/8\) and \(M+\ell=1\), and preserves the principal signal exponent
\(C(s)=s-11/16\). The continuous high-endpoint certificate gives a clean
margin greater than \(1/400000\). Separate
[low](../../quasi-rh-character-amplification/reviews/LOW_STRUCTURAL_AUDIT_20261008.md),
[moment](../../quasi-rh-character-amplification/reviews/MOMENT_STRUCTURAL_AUDIT_20261008.md),
and [contour](../../quasi-rh-character-amplification/reviews/CONTOUR_TRANSFER_AUDIT_20261008.md)
reviews check the transfer at those scales. This candidate requires no new
inverse/plain correlation estimate. It therefore deserves priority if the
immediate objective is a complete, reviewable conditional improvement.
See the [geometry note](../../quasi-rh-character-amplification/notes/GEOMETRY_OPTIMIZATION_20261008.md).

The qualification is substantive: these are source-scoped transfer checks,
not independent proofs of the external reflection, detector, inverse
recursion, fourth moment, or global family strip. The imported source is
the September 30 manuscript claiming \(7/8\), rather than the distinct
October 5 alternative claiming \(11/12\); the external
[catalogue](https://github.com/openai/math/blob/main/CONTENTS.md) currently
distinguishes these versions explicitly. A useful next product is a single
conditional theorem with a complete dependency ledger, followed by an
independent audit of the few imported results on which it actually depends.
Repeating the rational calculation alone will not discharge those inputs.

Further optimization of the same geometry offers little. At fixed
\(b=1/8\), the displayed high envelope has a certified limiting parameter
near \(e=0.0001711975385\), corresponding to a boundary near
\(0.8749572006\). This leaves only about \(1.13\times10^{-6}\) additional
boundary displacement beyond the chosen candidate. It is a limitation of
that envelope, not a universal zero-free barrier. The
[off-balance scout](../../quasi-rh-character-amplification/notes/OFF_BALANCE_GEOMETRY_SCOUT_20261008.md)
also pays an additional dual-length cost: positive imbalance worsens the
low-side boundary locally. Neither calculation supports a sustained
parameter-only route toward RH.

The next proposed boundary is
\(7/8-1/20000=0.87495\), only \(1/120000\) below the current conditional
candidate. It requires genuinely new arithmetic: a restricted mixed
saving \(\eta=1/5000\), or another estimate giving the same count payoff.
After both witness and cutoff rebalances, that saving gives count gain at
least \(5456/50310325\), slightly greater than \(1/10000\), before the
fixed small losses. These are three different quantities: a moment saving,
a count saving, and a strip displacement. See the
[localized target](../../quasi-rh-character-amplification/notes/LOCALIZED_JOINT_WITNESS_TARGET_20261008.md)
and the manuscript's conditional payoff and application-wedge sections.

**The mixed program has the best developed local arithmetic target, but
the weakest sufficient target should stay visible.** The parent moment is
\(\sum_{u\in\mathcal C}|M_r(u)S_m(u)Q_I(u)|^2\). Its application needs
only a small buffered wedge near the inverse/plain crossing, with leading
lengths approximately \(0.7057<r<0.7296\) and
\(0.4039<m<0.4124\). Existing positive interpolation proves an upper plain
band \(m\ge21/50\), which is disjoint from this wedge. A narrow wedge
reduces the required uniformity; it does not itself make the character
average power-small as the scale grows.

There are three useful levels of attack: a direct restricted count of the
simultaneously witnessed rows; a tapered mixed second-moment saving on
their actual selected set; and the stronger fourth-moment theorem developed
in the mixed branch. The
[ordered fourth continuation](../mixed_character_families/notes/20_ORDERED_FOURTH_CONTINUATION_20261009.md)
shows that a uniform fourth saving \(1/700\), with the original whole
prime slots and tight witness losses, suffices for the second-moment
application. It does not show that this stronger theorem is necessary.
Every proposed new bound should therefore be checked against the direct
second-moment or count requirement before pursuing a broader auxiliary
theorem.

[Note 29](../mixed_character_families/notes/29_SIGNED_FORM_SECTORS_AND_SIXTHPOWER_TAIL_20261009.md)
reduces the fourth-route finishing form to a real signed aggregate
\(\mathcal T_*\), with nonprincipal high-conductor rows failing the core
frontier, both exclusive column norms greater than \(B\), quotient
conductor greater than \(B^2\), and column sixth-power factors at most
\(U^{1/10}\). Its sufficient bound is

\[
\mathcal T_*\ll U^{1+dr-1/700+\varepsilon}H^b.
\]

The comparison errors have exponent saving \(11/6250\), leaving reserve
\(29/87500\) against this target. This is a precise analytic obligation,
and a one-sided signed bound is enough. The equivalence in Note 29 is
with the preceding finishing form up to controlled errors, not with RH.

The important negative evidence survives these reductions. Available
positive majorants still have a worst-case deficit of at least
\(1627/7000\), about \(0.2324\), in the stated legal scalar setting.
Thus the requested \(1/700\) gain should not be described as a tiny
improvement over an estimate that is already nearly sufficient. Nor does
the latest auxiliary row extension remove additional detector rows: its
cutoff remains below the selected high-conductor gate. The progress is in
isolating where a new estimate must act, not in proving that estimate.

This nevertheless remains the leading arithmetic opportunity because it
retains the actual Möbius coefficients, has explicit admissible profiles
and conductor masks, and has a quantified local application. Its current
kernel also offers a concrete place to test coupled Gauss-sum and
metaplectic techniques. The parent
[common-signal scout](../../quasi-rh-character-amplification/notes/COMMON_SIGNAL_PROBE_SCOUT_20261008.md)
is worth retaining as a tool: controlled contrasts can annihilate one
identified Mellin mode. Its present finite-probe construction gives only
a constant improvement, however. It becomes a power-saving route only
after analysis identifies and controls the actual adverse modes or their
concentration.

**Short families are a serious alternative, but the later barriers weaken
their earlier claim to first priority.** Their particularly clean deduction
is

\[
\mathfrak M(D,D^h)\ll D^{h+a+\varepsilon}
\quad\Longrightarrow\quad
\beta_{\rm out}=\frac{1+a}{2}+\frac{5h}{12}.
\]

For an adequate detecting profile class, this directly excludes zeros of
the fixed-character \(L\)-function to the right of that boundary. The
extraction needs no initial strip or conductor-uniform hypothesis. At
\(h=a=2/5\) it would give \(13/15\), a substantially larger improvement
than the amplification perturbation. This is a genuine advantage if the
goal is a stand-alone theorem from a new moment hypothesis. See the
[short manuscript](../short_families/short_family_reductions.tex).

The size of the missing estimate is correspondingly substantial. The
generic physical-row bound is \(DH^{1/6}\). Any useful target beating
\(7/8\) requires more than a quarter power beyond it. At \(h=a=2/5\),
the comparison is \(D^{16/15}\) versus \(D^{4/5}\), a \(4/15\) gap.
The complete signed small-cofactor block still has energy of order
\(D^{16/15}\), up to logarithms. The norm Jacobian turns the tempting
divisor cancellation into the positive product
\(\prod_{p\mid M}(1-1/Np)\). This does not disprove the full moment:
cross terms with other total products could still compensate it. It does
rule out proving the target separately for that relatively complete block.
The latest [cofactor continuation](../short_families/notes/26_SHORT_FAMILY_COFACTOR_CONTINUATION_20261008.md)
itself moves the next task to the mixed actual-probe chain.

There is also a compatibility issue with an earlier proposed easier scout.
At \(h=2/5\), uniformly positive lower exponents for both Möbius factors
require \(\theta<1/10\) under the displayed support bound. The sparse
generic nonsquarefree removal instead needs \(\theta\ge8/15\); the later
choice is \(11/20\). These cannot jointly supply the old globally long
bilinear geometry and the latest affordable squarefree residual. Long
subblocks remain possible, but require a new bridge and payment of their
complements. This further weakens the argument that the short core is
automatically simpler than the mixed residual.

Short families should be promoted again if a full covariance estimate
between distinct total products beats the current physical exponent, or
a new restriction removes its coherent block with all boundary and cross
terms paid. Arbitrarily short-family hypotheses approaching the RH
endpoint already have RH-strength consequences through the unit row;
the extraction is not an automatic bootstrap from zeta-only quasi-RH.

**The quadratic lift is simpler arithmetically, but its target is stronger
and its existing sieve does not descend.** The remaining estimate is

\[
\sum_{a\le X^{2-h}}^{*}a^{-1/2}|S_a(X)|^2
\ll X^{1+h/2+\varepsilon},\qquad1<h<2.
\]

At \(h=7/5\) this would yield a \(17/20\) boundary, but it also gives
the corresponding exclusion for every fixed primitive odd-conductor
quadratic character. The principal row already contains the improved
zeta response; deleting it removes the desired detection. The entrywise
absolute majorant of the actual prime-pair form is at least \(X^2\),
too large for the target. Even granting a favorable uniform individual
response exponent \(B=7/8\), combining it with the quadratic sieve
leaves exponent \(1+B=15/8\) at the bottleneck conductor. The
\(17/10\) target at \(h=7/5\) still needs saving \(7/40\).
See the [strength and barrier note](../integer_quadratic_lift/notes/2_QUADRATIC_MOMENT_STRENGTH_AND_BARRIER_20261008.md).
Resume this branch only against a specific signed prime-pair dispersion
estimate; better individual bounds or another optimization of the same
sieve envelope will not close that gap.

**Fixed-scale descent has the cleanest zeta-only formulation, but no
contraction mechanism.** A recurrence
\(E_\delta(X)\le qE_\delta(X/b)+CX^{-\eta}\), with \(b>1\) and
\(q<1\), gives a strict power improvement. The exact signed covariance
criterion makes a candidate mechanism testable. The complete
prime-profile comparison already has an affordable power remainder, so
sharpening that remainder is not the missing result.

Its current moving-cutoff identity nevertheless transmits the residues of
off-critical zeros with nonzero multiplier. Existing convolution
identities, cutoff averages, or logarithmic gains do not automatically
remove those poles. Moreover, a positive admissible spectral edge need
not be attained; little-o improvement at the edge does not imply a smaller
power. The notes explicitly distinguish this analytic obstruction from
an Euler-product counterexample. See the
[resonance analysis](../fixed_scale_descent/notes/3_ARITHMETIC_FEEDBACK_AND_RESONANCE_20261008.md)
and [edge analysis](../fixed_scale_descent/notes/2_SPECTRAL_EDGE_AND_LOG_SAVINGS_20261008.md).

Keep one bounded task here: derive a complete fixed-delay arithmetic
difference retaining both moving domains and terminal corrections, and
identify a specific cross-scale bilinear estimate that could produce a
negative covariance margin. A new equivalent criterion without such a
mechanism would not improve the branch's ranking. This branch becomes
more strategically attractive if independence from the imported native
family package is the dominant objective, but that does not make its
central estimate easier.

**Heat flow is best treated as a separately scoped project.** Under the
published heat-flow inputs, exclusion of real multiple zeros of \(H_t\)
for every positive \(t\) is equivalent to RH. The local work proves an
effective derivative interface and eventual collision exclusion for
\(t\in[\varepsilon,1/2]\), \(|x|\ge e^{64/\varepsilon}\). This enormous
cutoff rederives known positive-time eventual simplicity; no remaining
compact rectangle has yet been certified. Generic kernel positivity and
fixed theta truncations are obstructed. See the
[collision criterion](../newman_collisions/notes/3_NORMALIZED_HEAT_COLLISION_CRITERION_20261008.md).

A useful bounded deliverable is one rigorous compact rectangle, including
a natural-cutoff crossing, or an improved upper bound for the Newman
constant using the published barrier architecture. Improving that
constant does not directly narrow the time-zero zeta strip: the required
backward heat evolution is a separate problem. The
[Polymath paper](https://arxiv.org/html/1904.12438) supplies effective
approximations and a finite-height/barrier criterion. A fresh
[Planat preprint](https://arxiv.org/html/2609.37164v1) retains collective
zero interactions and estimates them via off-zero logarithmic derivatives.
Its final numerical ceiling is expressly conditional on an imported
unreviewed barrier package. Its high-height theorem concerns a fixed
positive-time window, rather than uniform control toward time zero.
It merits a bounded independent audit, but does not displace mixed
correlations for the present quasi-RH objective. At an ordinary double
collision, a finite external field contributes a term tending to zero
with the squared imaginary height, so collective contraction alone does
not remove the collision endpoint obstruction.

**The literature strengthens the case for a structural mixed estimate,
not another arbitrary-coefficient bound.** De Faveri's
[fixed-order sieve preprint](https://arxiv.org/html/2610.04045v1), Theorem
1.1, already supplies the sixth-power-free envelope used in Note 29.
Its Proposition 8.1 treats coupled cubic \(ab^2\) conductors, and the
root-number coupling argument offers a specific model for joint
valuation analysis. Transfer to the surviving sextic form requires proof
of the coefficient, conductor, and mask compatibility. Separately,
[de Faveri–Dunn–Hoffstein](https://arxiv.org/html/2607.07911v1) prove
cubic and quartic nonorthogonality caused by Gauss-sum bias. That result
does not prove a sextic obstruction, but it makes an explicit calculation
of coherent metaplectic modes a better scout than an assumption of generic
square-root cancellation. The fuller literature assessment, including
bias-subtracted dispersion and limits on trace-function transfer, remains
in the [earlier review](MIXED_PROGRESS_AND_LITERATURE_REVIEW_20261009.md).

**The next phase should have three concrete completion conditions.**

1. Consolidate the geometry candidate into one conditional theorem and
   dependency ledger. Retain fixed \(\kappa=3/4\), every physical slot,
   common signal normalization, Euler-domain enlargement, and order of
   height choices. Obtain an independent audit of the essential imported
   lemmas. This produces the most reviewable near-term result and clarifies
   the baseline for every later payoff.
2. For mixed arithmetic, calculate the complete transformed kernel of one
   genuinely surviving signed block, preferably a coupled opposite-
   valuation block with small gcd and the actual annular coefficients.
   Identify its coherent Gauss/theta contribution and prove either a power
   estimate for the residual or a quantitative obstruction. Keep all sharp
   selectors, physical zeros, common aspects, and pair-cut cross terms.
   A nonzero block theorem is a useful milestone, not the full finishing
   bound; record the aggregate remainder explicitly.
3. Test every new estimate against the weakest sufficient detector target,
   including the buffered application wedge and tapered saving. Continue
   the fourth route only if its extra structure provides a gain beyond the
   present envelope. If the first two analytic scouts merely reproduce
   that envelope, or leave an uncontrolled coherent mode, reassess before
   doing more sector refinements. The best alternative is short-family
   cross-product covariance; heat certification remains a separate bounded
   deliverable.

A logarithmic gain, fixed-factor improvement, vanishing on one model mode,
or another exact partition should not be recorded as progress toward the
required power unless it changes the complete residual estimate. Likewise,
the fractions \(1/700\), \(4/15\), and \(7/40\) refer to different
observables and baselines; their numerical sizes are not proof-difficulty
scores. The evidence supports a conditional research priority, not an
assertion that the latest fourth target is the most likely route to RH.

The main implication still ends at a conditional moment/count improvement.
A new global family boundary additionally needs full detector coverage,
all-height control, and valid reuse of the native family assumptions.
Iteration to RH would need a separately proved descent mechanism that
does not stall. None of those steps follows merely from equivalence of
successive signed finishing forms.

**Verification was limited to the claims relevant to this comparison.**
The geometry checker replayed successfully and reproduced
`geometry_optimization_check.json` byte-for-byte. Parallel reviewers
replayed 3,289 short-family cofactor assertions, the quadratic barrier
checks (13,065 masked coefficient checks, three Gram checks, and 20
exponent cases), and the normalized heat constant ledger. The preceding
mixed review reproduced Note 29's 16,191 finite assertions. These checks
validate finite algebra and constant records; their synthetic tests do
not prove the character-correlation estimates or the imported analytic
theorems. No new broad numerical experiment was required for this ranking.

The principal files identifying this review's source state have SHA-256:

| File | SHA-256 |
| --- | --- |
| Mixed manuscript | `ea6deabc7fb1e3c8f90ee5cbaca7db6af7015a6b6392764c0c8a724862d66d3e` |
| Mixed Note 29 | `8250f75c6018e7b570430eb29aaaef097aeb3edd47a0a73288b10aae6db96a35` |
| Character-amplification manuscript | `81d1b7ecc02d15469577eec34b8b21cef41a6f6f874aafc153afd29b692ab3dd` |
| Geometry note | `27fe997051fced3b0abe2605bc006783e2e0782d3dfe61f07e539b4fcdf75d0c` |
| Short-family manuscript | `3c8ee8ee95b9afd2a4d16400ebead075207e38e38e8ede29ca5c7242b52c2219` |

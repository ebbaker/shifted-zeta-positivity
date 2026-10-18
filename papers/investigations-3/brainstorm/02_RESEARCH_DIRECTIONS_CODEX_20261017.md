# Research directions after the first investigations-3 rounds

17 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Model **gpt-6-astra (Codex)**; effort **ultra**.
Internal synthesis with same-model collaborators; no specialist review.

These proposals follow the [progress assessment](01_PROGRESS_ASSESSMENT_CODEX_20261017.md),
the [result index](../../../result-summaries/README.md), and the
[avoid index](../../../avoid/README.md). The first two are immediate tasks.
The later questions are alternatives subject to explicit gates, not a
recommendation to start several more investigations.

## 1. Extract and review the stronger conductor rate

**Classification:** quantitative theorem consequence, not a GRH reformulation.

**Output already drafted here:** the [conductor-rate note][rate] retains
the q-dependent main term of 03's uniform transport floor and uses its
finite-restart lemma to derive

\[
 \Lambda_\chi\le T(q)
 =O(\log\log q/\log q),\qquad q\ge10^{12},
\]

with an explicit T(q) and asymptotic leading coefficient 3. This improves
the rate obtained by 01's initial-floor argument. Its status is a
source-dependent deduction with same-model checks; the detailed proof and
review limitations are in the note. The rate itself has earlier public
provenance, so this is not a priority claim.

**Next gate:** review the all-ell domination in [03 Note 01][floor], the
original-slice restart in [Note 02][restart], and the short endpoint passage
in the new note together. A replay of the scalar file alone does not
review these implications. If accepted, integrate a short corollary into
the existing manuscript chain and update the benchmark consistently.

**After that:** select one conductor threshold below 10^12 and one positive
target time before computing. Require a uniform floor over every real
height and every time used by the restart. The existing floating thresholds
are candidate search locations, not accepted endpoints. A failed complete
error budget closes that parameter box; it does not justify simply making
the grid denser.

**Controls:** the Euler-factor control fails the actual logarithmic
coefficient majorant; the weighted-square, reflected, smooth and
positive-primitive sources lack the specified character arithmetic and
partial-sum estimates. Apply the generic comparison only with a control's
own actual floor. The non-even periodic control in [01 Review 03][familyreview]
fails its scalar acceptance condition, as it must. No inference from
shape or reflection is being made.

## 2. Complete 02 through activation bounds

**Classification:** finite certificate milestone and potentially a reusable
reduction in certificate cost.

[02 Review 01 §3][activation] supplies the key mechanism. For an anchor
N_a within a leg, an activation payment Delta bounds the loss up to a
later N. The decisive condition is

\[
 L^{\rm sh}_{N_a}(y_0)-\Delta_{y_0}(N_a,N)>3\cdot10^{-7}.
\]

**Output:** one checked activation proof, outward anchor/payment enclosures,
an exact index-coverage ledger across the four leg boundaries, and one
complete dependency statement. The approximately twenty-anchor plan
(4+5+5+6) is a starting plan; permit extra anchors when needed for certified
slack. Do not maximize span lengths merely to preserve that count.

**Pass condition:** cover every missing finite index, preserve the existing
strip-transfer contract, and join the finite bridge to the infinite tail
and inherited verification/barrier inputs. Only then can the conditional
Lambda<=0.1745354 conclusion be discharged at the stated import level.
Review the completed chain before upgrading its status.

**Stop condition:** if one planned span cannot pay its loss, shorten that
span or state the failed budget. Do not launch the old millions-of-rows
producer as a default fallback. A changed mollifier or height is a new
contract and requires renewed transfer coverage. Host time/memory limits
must be reported separately from mathematical acceptance.

**Controls:** the seminorm algebra is generic. Its theta application depends
on the correctly normalized approximation and full error payments. Retain
the actual transfer counterexample and fault-injection tests. A control
can pass a collision-free finite box; it must not certify a contrary claim
on a domain containing its event. This is the finite-domain qualification
in [summary 12][controls].

## 3. Couple remainder value and derivative instead of paying separately

**Classification:** proposed estimating mechanism, not yet a proved consumer.
This is the most useful new technical question after the two immediate tasks.

Project 06 improved a logarithmic-derivative estimate by coupling a disk
function's center value to its derivative through Schwarz–Pick.
Project 03's stronger kernel uses the combination

\[
 (\lambda/p)S-\mu\partial_pS.
\]

Use the transport variable w=(1+p)/2+ix/2 and the manuscript's remainder
epsilon(w)=(G'/G)(w)-(F'/F)(s*(w)). Here the disk radius r and derivative
epsilon' are in the **w-plane**, not the physical z-plane. For this
holomorphic remainder with a **proved whole-disk** bound |epsilon|<=E_0,
E_0>0, put s=|epsilon(w)|/E_0. If E_0=0 the remainder payment is zero.
Schwarz–Pick gives |epsilon'(w)|<=(E_0/r)(1-s^2). In the normalization
of [03's derivative corollary][transport], the combined remainder cost
is therefore bounded by

\[
 \max_{0\le s\le1}\{as+b(1-s^2)\},\qquad
 a=\frac{\lambda E_0}{2p},\quad b=\frac{\mu E_0}{4r},
 \tag{1}
\]

for lambda,mu>=0. For b>0 this maximum is a if a>=2b, and
b+a^2/(4b) otherwise. When a,b>0 it is strictly smaller than a+b.
The calculation is elementary; the research lies in supplying its
applicable analytic inputs and transfer.

**Gate A:** prove the whole-disk envelope, including the complex denominator,
reflected tails, and the boundary of the disk. The current height-three
certificate does not do this. A line estimate or a sampled circle is
insufficient.

**Gate B:** extend the sine-tail/restart argument to the combined functional.
The present theorem transfers a floor of S only. An added real zero at
horizontal distance d contributes to this combined functional

\[
 \frac{(\lambda-\mu)d^2+(\lambda+\mu)p^2}{(d^2+p^2)^2}.
 \tag{2}
\]

Thus lambda>=mu makes each added real-zero contribution nonnegative;
lambda<mu gives negative far contributions and defeats a naive termwise
positivity argument. This is a concrete control, not an exclusion of every
possible cancellation-aware transfer. Even in the nonnegative regime,
the full one-step proof still has to be supplied.

**First deliverable:** one declared barrier cell and coefficients for which
the complete paired payment improves the existing bound after all extra
disk costs. If no cell improves, stop. A new identity for the same
functional or an unjustified derivative circle is not progress. The
arithmetic controls must be screened using their own whole-disk data;
positivity of an auxiliary kernel supplies none of those data.

## 4. Turn the upper transport estimate into a family tail bound

**Classification:** proposed quantitative infrastructure with a named
possible consumer; lower priority than certificate completion.

At p=3 and the midpoint U=X+1/2 of a unit window, conjugate-pair convexity
gives a Poisson contribution of at least 12/37 per zero when the zero strip
has height at most one. Thus the upper side of the same [03 transport][transport]
would give

\[
 K_{\chi,t}(X)\le\frac{37}{12}S_\chi(U,3,t)
 \le\frac{37}{12}\left(\frac{\ell_*(U,t)}4+\frac{77}{200}\right)
 \tag{3}
\]

Here K counts all complex zeros with multiplicity whose real parts are
in (X,X+1], for real X. The range is q>=10^12, 0<=t<=1/4.
Unlike importing 06's zeta count by replacing
log X with log(qX), this uses an already established family estimate.
The pair calculation and the upper transport allowance still need to be
written and reviewed as a family statement.

**Missing effective step:** upper-bound the saddle ell*(U,t) explicitly
in terms of q, |U| and t, with no hidden monotonicity assumption. Then
sum the resulting unit-window count against |rho|^(-2), handling both
height directions. The possible consumer is the central truncation error
64 sum_{|rho|>R}|rho|^(-2) in the sine-tail construction. The aim would be
an explicit O(log(qR)/R) allowance and a declared finite R for a requested
margin. The current existence proof does not need such a number.

**Stop condition:** if no downstream task needs a quantitative R, retain
this as a short lemma proposal and stop. An upper count gives no lower
population, principal-value velocity cancellation, reality, simplicity,
or improved Newman bound by itself. A colliding control may satisfy the
upper-count inequality; this is not a purported collision discriminator.
Only the arithmetic upper transport bound requires the character premise
screen.

## 5. Identify what a genuinely faster conductor rate would require

**Classification:** speculative arithmetic mechanism; not a new theorem.

Optimizing a constant height-three floor or the scalar restart can improve
constants. It does not automatically remove the log log q in the derived
rate. The existing pointwise paired-kernel comparison loses a factor h/p
for remote zero mass: its kernel ratio tends to h/p as horizontal
distance tends to infinity. This limits that particular termwise estimate,
not every argument using a global floor.

A sharper target is a floor at a height that follows the current strip.
At a highest zero of height h, let Q=h^2 and p=kappa h with kappa>sqrt(5).
If one could prove S_chi(x,kappa h,t)>=c log q in the required regime,
the existing paired-zero algebra would suggest

\[
 Q'\le-\left(2-\frac8{\kappa^2-1}\right)
       -\frac{4c}{\kappa}(\log q)\sqrt Q.
 \tag{4}
\]

The scalar extinction time is O(1/log q). But (4) is only target algebra:
the constant floor at height three transfers downward with a vanishing
factor, and p<1 leaves the Euler-product half-plane used by the current
proof. A new arithmetic estimate is needed. The moving zero's own pair
must be subtracted with its existing correction; its large local
contribution is not new arithmetic information.

**Reopening gate:** prove a lower-height estimate on a nontrivial band
h>=h_0=A/log q and a compatible moving-strip transfer, with quantified
boundary errors. Stop that estimate at h_0, then use ordinary strip
contraction for an additional h_0^2/2=O((log q)^(-2)) time. No uniform
positive floor at every real abscissa as p decreases to zero is proposed.
Before those gates, no numerical campaign or new
manuscript section is justified. Controls lacking the character arithmetic
receive no conjectural lower-height floor; any claimed generic replacement
must survive the periodic and Euler-factor witnesses on their event domains.

## 6. Use the obstruction projects to design bounded alternatives

These are conditional reopening questions, not additional active tracks.

**07 with finite/outer estimates: reflection-preserving, carrier-relative
approximation.** Seek one complete heat-jet error estimate on a specified
domain after division by the relevant analytic carrier. Specify its
comparison margin before choosing a basis. A fixed interior contour shift
can still decay more slowly than the carrier; a near-boundary shift must
pay the growth of its contour norm. The deliverable is an improved margin
or lower certificate cost, not a global conclusion from a finite absolute
error tolerance. Weighted-square controls fail full reflection; reflected,
Euler-factor and positive-primitive controls can retain reflection and
must fail the quantitative error-versus-margin condition on an event
domain. Reflection alone is not a sign mechanism. Exact square support
plus full normalized reflection already identifies theta and is not an
independent approximation construction.

**04: a complete actual-Sonin residual comparison.** For a named support
and prime pair, compare the direct complete-boundary bound with an estimate
r+m, where r bounds the existing other terms and m bounds the signed mixed
return. Retain the gamma/metric cancellation and certify the complement.
The round-two endpoint norm warns against treating the critical boundary
operator as a compact error. The tilted projection model is the mandatory
generic-sign control; a successful new premise must use the actual Sonin
projection. If the complete bound does not improve, stop the decomposition
campaign. All-support Weil positivity is still the original target.

**05: one fixed-multiplier reverse-control test.** A concrete small entry
point, following the [round-one review][stable], is a fixed Cardon multiplier
such as G(z)=1-z^2. First test the quotient source B(u)/G(iu) for the known
stable Bessel target B, before theta. Necessary odd-dilation constraints
for an underlying independent-spin limit can give a bounded rejection
test. Passing such a test does not prove approximation, and matching
field-growth order is insufficient. Require an explicit stable-control
construction before fitting theta. General interacting infinitesimal
arrays remain an open class, but a class name is not a mechanism.

The combined 05/07 lesson already closes one tempting shortcut: a nonzero
finite nonnegative change of theta coefficients cannot provide a globally
stable seed at any real heat time. This leaves finite-domain numerical
approximants and genuinely infinite reflected constructions untouched.

## Execution order

1. Review the conductor-rate deduction and the 03 analytic inputs as a
   single package; finish the 02 activation certificate in parallel.
2. Integrate accepted conclusions into the existing manuscripts and concise
   histories, preserving their actual review level and imported dependencies.
3. Select **one** next analytic objective: a lower-conductor certified regime
   or the joint remainder estimate. Define its target and complete budget.
4. Commission 06, 04, 05, or a new approximation design only when its stated
   consumer or reopening input exists.

[rate]: notes/01_CONDUCTOR_RATE_FROM_UNIFORM_FLOOR_CODEX_20261017.md
[floor]: ../03_effective_outer_remainders/notes/round-2/01_UNIFORM_FAMILY_FLOOR_CODEX_20261017.md
[restart]: ../03_effective_outer_remainders/notes/round-2/02_RESTARTED_STRIP_COMPARISON_CODEX_20261017.md
[transport]: ../03_effective_outer_remainders/manuscript/height_p_transport.tex
[familyreview]: ../01_dirichlet_newman_families/reviews/03_CROSS_MODEL_MATHEMATICAL_REVIEW_CODEX_20261017.md
[activation]: ../02_sharp_finite_sum_bounds/reviews/01_ROUND_ONE_CROSS_MODEL_REVIEW_CLAUDE_20261017.md
[controls]: ../../../result-summaries/12_collision_controls_and_screening.md
[stable]: ../05_constructive_stable_models/reviews/01_ROUND_ONE_CROSS_MODEL_REVIEW_CLAUDE_20261017.md

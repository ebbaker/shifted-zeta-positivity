# B07 complete divisor and Gaussian pair evaluator

8 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance, authenticated chat0006. Actual backend
model and effort are unavailable in the recorded configurations and are
not inferred. Root alone authored the research. **Status: proved in-note,
proof-author self-check only; conditional evaluator contract. No canonical
zero inventory or correlation value has been computed.**

## 1. Decision and numerical meaning

B07 selects **certified complete divisor acquisition followed by
same-center Gaussian quadrature**. The new information is an exact integer
count and enclosing locations for every zero label in a finite region.
A list of likely real roots, a small field error and a difference-only
pair transform do not supply this information.

This is the stronger directly contracted alternative permitted by
[E08's continuation](../continuation-notes/14_TND_OC_AFTER_E08_AND_MODEL_CHANGE_20261108.md),
rather than acquisition of the enormous moment array in Note11 section 6.
It preserves the literal canonical H0, all contributing labels and the
declared center/smoothing rule. It changes the acquisition method before
execution. The fixed pilot is T=1000, not a large-T theorem.

Conditional on at most 512 completely certified labels within Euclidean
radius 2^(-38), and at most 4096 ordered midpoint pairs whose physical
windows overlap, a fixed 20-node quadrature on each polynomial window
piece yields continuous functions Q2 and QC satisfying

\[
 \sup_{(\zeta,\eta)\in Q\times Q}
 \max\{|\overline R_2-Q_2|,\ |C-Q_C|\}
 \le {5249\over2^{24}}<{1\over3000}.                    \tag{1}
\]

Q=[-1,1]+i[-1,1]. This is an absolute unfolded-density error, not relative
accuracy near zeros of the pair function. Its proof is below. The finite
execution packet requires certified arithmetic radius at most 1/1000 for
each reported value, giving total radius less than 1/750, within Note11's
example tolerance 1/100. Counts, radii, overlap cap and runtime are
acceptance gates, not measured facts.

Classification under [avoid01](../../../../../../avoid/01_restating_the_target.md):
a quantitative finite evaluator contract, judged by (1) and the work caps.
It does not imply RH, a sine profile, uniform high-height asymptotics or
a Newman bound. The complete certified function is the deliverable;
recovering known low-height realness is only a prerequisite. Read the
[result index](../../../../../../result-summaries/README.md),
[cluster11](../../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md),
[avoid index](../../../../../../avoid/README.md) and
[scope07](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md).
No canonical data follows from this conditional estimate alone.

## 2. Fixed observable and finite canonical region

Use Note11's center law X uniform on [1000,2000], h=1,
ell=b=min(1,4pi/log1000)=1, epsilon=1/4 and Jacobian J=1. Put

\[
 p(t)=\begin{cases}1&t\le0,\\
 1-10t^3+15t^4-6t^5&0<t<1,\\0&t\ge1,\end{cases}
 \quad w(t)=p(2|t|-1),\quad \kappa(y)=p(|y|-1),
\]
\[
 G(u)={8\over\pi}e^{-8|u|^2},\qquad
 q_X(z;\zeta)=w(\Re z-X)\kappa(\Im z)G(X+\zeta-z).
\]

List the zeros z_j with multiplicity as distinct labels. Define

\[
 r_X(\zeta)=\sum_j q_X(z_j;\zeta),\qquad
 R_{2,X}(\zeta,\eta)=\sum_{j\ne k}q_X(z_j;\zeta)q_X(z_k;\eta),
\]
\[
 m(\zeta)={1\over1000}\int_{1000}^{2000}r_X(\zeta)\,dX,\quad
 \overline R_2={1\over1000}\int_{1000}^{2000}R_{2,X}\,dX,\quad
 C=\overline R_2-m(\zeta)m(\eta).                         \tag{2}
\]

Thus R2=r_X r_X-d_X with
d_X=sum_j W_X(z_j)^2 G(X+zeta-z_j)G(X+eta-z_j).
The self term uses W². A zero of multiplicity m contributes m(m-1)
ordered factorial pairs at its location; these must not be discarded as
geometrically coincident pairs.

The horizontal source window confines contributing zeros to
999<=Re z<=2001. The canonical zeta strip gives |Im z|<1, while kappa
is retained in the formula. It suffices to certify all zeros in

\[
 \mathcal R_z=\{998<\Re z<2002,\ |\Im z|<3/2\}.            \tag{3}
\]

This includes an extra horizontal collar. Through the canonical
s(z)=1/2-iz/2 and conjugation, it corresponds to the positive-height
rectangle

\[
 \mathcal R_s=\{-1/4<\Re s<5/4,\ 499<\Im s<1001\}.        \tag{4}
\]

For rho=beta+i gamma in (4), the matching H0 zero is
z=2gamma+i(2beta-1). Indeed s(z)=conjugate(rho).
The identity F=((s-1)/s)zeta(s)=D H0 from manuscript section 4 has
nonvanishing factors on this rectangle: s, s-1 and Gamma(s/2) have
no relevant zero or pole there. Multiplicities are preserved. Equivalently
H0=xi(s)/8 there. No trivial zero, pole at one or zero at s=0 enters.

All zeros outside (3) have zero W_X for every center in the exact
interval. Observation smoothing is not a source-window tail: the
Gaussian is retained on the whole observation plane. No centers or
window collars are dropped. If a rectangle boundary cannot be certified
zero-free, the fixed acquisition gate fails; it is not silently moved.

## 3. Complete integer counts and enclosed labels

The general input to the theorem is a finite family of disjoint certified
zero boxes inside (3), each with an exact integer multiplicity, whose sum
equals a complete contour count. Repeat a box midpoint once per label.
Every zero in the box must lie within rho=2^(-38) of that exact dyadic
midpoint. This includes nonreal and multiple zeros without a separation
hypothesis. It gives a matching z_j -> zhat_j of all N labels.

Here is a concrete count certificate using certified evaluation of the
**exact** zeta function. Orient the boundary of (4) counterclockwise and
partition it into straight segments [s_l,s_(l+1)]. For every segment
obtain a convex rectangular complex enclosure B_l of zeta on the
entire segment, and prove 0 is outside B_l. Enclosing only endpoint
values is insufficient. Since B_l is compact, convex and excludes zero,
it lies in a strict open half-plane through the origin. The image path
is homotopic within B_l to its endpoint chord. Its argument change is

\[
 a_l=\operatorname{Arg}{\zeta(s_{l+1})\over\zeta(s_l)}
       \in(-\pi,\pi).
\]

Use endpoint balls and a branch-safe principal argument enclosure A_l;
require A_l to be strictly within (-pi,pi). An interval enclosure of

\[
 {1\over2\pi}\sum_l A_l                                  \tag{5}
\]

that contains exactly one integer certifies the winding number. It is
the number N of all zeros, counted with multiplicity, in (4), by the
argument principle; there are no poles there. Every contour segment,
endpoint ball, branch check and the integer extraction must be replayable.
A table of sampled arguments without the segment-image checks is rejected.

For the first E09 implementation, a simpler *local* certificate is fixed.
Generate at most 1024 candidate positive zeta ordinates; library root
routines are proposal generators only. Within (499,1001), form disjoint
dyadic brackets. Certify opposite nonzero signs at the bracket endpoints
of the real function

\[
 t\longmapsto \xi(1/2+it)
 ={s(s-1)\over2}\pi^{-s/2}\Gamma(s/2)\zeta(s),
 \qquad s=1/2+it.                                      \tag{6}
\]

Its reality follows from the functional equation and conjugation.
A rigorous real-part enclosure signs it; the corresponding imaginary
enclosure must be consistent with zero. Each bracket supplies at least
one critical-line zero. If the number K of such disjoint brackets equals
the full count N in (5), each bracket contains exactly one simple zero
and no zero anywhere else in the full complex rectangle is omitted.
This conclusion follows from equality of integer counts, not RH or a
simplicity assumption. Map each bracket by x=2t; require resulting
midpoint radius <=2^(-38).

If K differs from N, a sign is unresolved, enclosures overlap or a radius
gate fails within budget, E09 returns that failed clause. A general complex
or multiple-zero isolator would be a later conceptual change; it must not
be replaced by dropping unaccounted labels. The theorem above allows such
labels, while this fixed pilot's acquisition algorithm may fail on them.

The official API/source passages are recorded in
[source-use08](../references/08_TND_OC_B07_CERTIFIED_EVALUATOR_SOURCE_USE_20261108.md).
The documented real-line wrapper alone is not the global certificate.
The selected python3 interpreter has none of flint, mpmath, sympy or scipy
available; this is an environment preflight observation, not a claim about
all installed interpreters or a failed mathematical premise.

## 4. Uniform transport from enclosed labels

Since |p'|<=15/8, we have
|w'|<=15/4, |kappa'|<=15/8 and |grad W|<=45/8. Also

\[
 \|G\|_\infty={8\over\pi}<{8\over3},\qquad
 \|\nabla G\|_\infty={32\over\pi\sqrt e}<{32\over3}.
\]

The product rule gives, uniformly in real X and zeta,

\[
 0\le q_X\le A:=3,\qquad
 \|\nabla_z q_X\|_\infty
 \le {8\over3}{45\over8}+{32\over3}
 ={77\over3}<L:=26.                                    \tag{7}
\]

These are global bounds in both coordinates, so there is no missing
cutoff-collar or transverse-mark cost. Matched labels within rho satisfy
|q_j-qhat_j|<=L rho. Telescoping products using the bound A on both
versions, then averaging over the probability law, gives

\[
 |m-\widehat m|\le NL\rho,\qquad
 |\overline R_2-\widehat{\overline R}_2|
 \le2N(N-1)AL\rho,
\]
\[
 |C-\widehat C|\le
 2N(N-1)AL\rho+2N^2AL\rho\le4N^2AL\rho.                \tag{8}
\]

The second contribution is the product of the two averaged first
intensities. There is no independent-center replacement of the pair
integral. Since both versions are bounded by A, telescoping introduces
no uncharged quadratic displacement term.

For the caps N<=512 and rho<=2^(-38), the common error bound is

\[
 E_{\rm root}\le4(512)^2(3)(26)2^{-38}
 ={312\over2^{20}}={4992\over2^{24}}.                    \tag{9}
\]

This is a stronger input than uniform field approximation: a certified
complete matching has been paid for. Neither E07 nor E08 implies (8)'s
matching from source accuracy alone.

## 5. Fixed positive quadrature with a uniform remainder

All subsequent centers and breakpoints use the exact dyadic midpoints
zhat_j. For a first intensity, intersect [xhat_j-1,xhat_j+1] with
[1000,2000], then split at xhat_j±1/2. There are at most three pieces,
each of length at most one, and their total length is at most two.

For an ordered pair j!=k, intersect both horizontal support intervals
with [1000,2000]. Keep it only if the intersection has positive length;
split at both labels' ±1/2 breakpoints. There are at most five pieces,
each of length at most one, of total length at most two. Let P be the
number of these ordered pairs. Require P<=4096. A discarded midpoint
pair has identically zero midpoint product; a true pair with slightly
different support is already charged in (8).

On each piece I of length d<=1, the relevant window branch is a fixed
polynomial, either 1 or p of an affine transition variable. Absolute
values are resolved before complex continuation. Parameterize I by
X=c+(d/2)u and use the Bernstein ellipse of parameter 2 in u.
There |Im X|<=3d/8<=3/8. A transition variable whose real range lies in
[0,1] has |t|<=9/8 on the ellipse: write t=c_0+d_0 u,
0<=|d_0|<=1/2, |d_0|<=c_0<=1-|d_0|, and |u|<=5/4.
Consequently

\[
 |p(t)|\le1+10(9/8)^3+15(9/8)^4+6(9/8)^5<51.
\]

The Gaussian in complex X is the entire continuation of its real
coordinate formula; transverse coordinates and observations stay real.
The first and pair integrands on this ellipse are bounded respectively by

\[
 M_1=600>{8\over3}\,51\,e^{9/8},\qquad
 M_2=200000>\left({8\over3}\right)^2 51^2 e^{9/4}.        \tag{10}
\]

The elementary allowances e^(9/8)<4 and e^(9/4)<10 suffice.
These bounds are independent of both observation points, in particular
uniform on Q×Q. This analytic continuation is piecewise; no assertion
that the globally compact C² window is holomorphic is made.

For completeness, if an analytic function on the parameter-2 ellipse
has modulus <=M, its Chebyshev coefficients of order k have modulus
<=2M 2^(-k), by the Laurent coefficient estimate after
u=(v+v^(-1))/2. The degree-(2q-1) truncation therefore has real-interval
remainder <=4M 2^(-2q). The q-node Gauss–Legendre rule has positive
weights of sum 2 and is exact to degree 2q-1. Applying integral and
quadrature to the remainder costs at most 16M 2^(-2q) on [-1,1],
or

\[
 8dM\,2^{-2q}                                           \tag{11}
\]

on I. The rule uses all q roots of the degree-q Legendre polynomial;
weights are 2/[(1-u_l²)(P_q'(u_l))²]. Positivity and degree exactness
are the standard Gaussian polynomial quadrature facts in
[DLMF §3.5(v)](https://dlmf.nist.gov/3.5#v), not an empirical
quadrature error estimate.

Apply the rule with the fixed q=20 separately to every piece. Let
Q1(zeta) approximate mhat(zeta), and Q2 approximate the full midpoint
factorial pair integral. Summing piece lengths before the normalization
by 1000 gives

\[
 e_1:=\|\widehat m-Q_1\|_\infty
 \le {16NM_1\over1000}2^{-40}<2^{-27},
\quad
 e_2:=\|\widehat{\overline R}_2-Q_2\|_\infty
 \le {16PM_2\over1000}2^{-40}<2^{-16}.                   \tag{12}
\]

For example the unscaled numerators are 4915.2 and 13107200.
Both mhat and Q1 are nonnegative and at most 2NA/1000<4;
the latter bound uses positive quadrature weights and their exact sum.
Define QC=Q2-Q1(zeta)Q1(eta). Then

\[
 \|\widehat C-Q_C\|_\infty\le e_2+8e_1
 <2^{-16}+2^{-24}={257\over2^{24}}.                     \tag{13}
\]

Combining (9) and (13) proves (1), since 5249*3000<2^24.
The full-pair bound is smaller; (1) is a common conservative allowance.
The first-mean bound NLrho+e1 is also less than 1/3000 at these caps.
Ideal quadrature nodes and weights here are exact algebraic numbers.
Their numerical enclosures, exponentials and sums are part of the
separate arithmetic radius, not silently exact machine inputs.

Q1 and Q2 define explicit finite Gaussian mixtures for every real
observation coordinate; QC is their stated connected combination.
Thus (1) approximates a continuous four-real-variable function, not
just a handful of sampled points. Store root/certificate data and a
regenerating evaluator, not a large expanded quadrature table.

## 6. Source completeness and tolerance ledger

The canonical identity in section 2 and certified exact-zeta evaluations
replace the finite-theta-approximant access route. Every certified zeta
ball must include its chosen algorithm's series/remainder and arithmetic
errors. The complete contour test (5) and local signs consume those
balls. There is no uncontrolled replacement H0 -> Hhat.

In particular, the E02/E07 arithmetic tail
5 C2(J_c) I_(17/2) and radial tail
B_source I_(17/2)^(>U_c), together with their enlarged-disk multiplier,
remain mandatory for any use of a truncated theta source. They are not
set to zero, estimated by root displacement, or omitted from their
existing route. This new branch uses neither truncated theta input nor
finite-source moments. Substituting such input into (5) or (6) without
paying both tails and the applicable contour/sign transfer fails the
contract. All earlier two-tail formulas and frozen packets are retained.

The standalone direct-contraction allocation is:

| Contribution | Certified allowance |
| --- | --- |
| Exact-function access and integer completeness | All contour/sign balls include their algorithmic remainders; count equality and root radii must pass |
| Complete matched locations | <=4992/2^24 |
| Ideal center quadrature and connected mean product | <257/2^24 |
| Combined analytic error, uniform on Q×Q | <1/3000 |
| Arithmetic evaluation of each requested surrogate value | radius <=1/1000 |
| Reported canonical value, including both preceding errors | radius <1/750 <1/100 |

This pays the original absolute target by a different complete proof.
It does not claim that Note11's finite-source moment array has been
supplied or that its three-step representation has become practical.

## 7. Fixed E09 deliverable and finite work budget

[E09 request18](../research-progress/handoffs/18_TND_OC_E09_EVALUATOR_REQUEST_20261108.md)
is the next task: Sol recommended before numerical implementation.
It first checks the six proof obligations below, then implements this
one pilot. All are fixed execution, with at most one bounded repair.

- C1: canonical rectangle, conjugation, multiplicity and exact support.
- C2: segment-image homotopy, branch-safe winding count and count equality.
- C3: (7)–(9), including the connected mean-product payment.
- C4: polynomial-piece ellipse bound and (10)–(13).
- C5: exact-function access, complete remainder accounting and the final
  arithmetic-radius gate.
- C6: retained scope, controls, caps and replayable full-function output.

Use a recorded interval runtime, initially python-flint 0.9.0 if available
or installable in an isolated environment; record its actual FLINT version.
The arithmetic precision ladder is 128, 256, 512 bits, no fourth level.
Cap accepted contour leaves at 20000 and all attempted segment/endpoint/
sign wrapper-level function evaluations at 100000 across attempts.
This counter does not bound hidden internal library operations.
Use at most 1024
root candidates, N<=512 labels and P<=4096 ordered overlapping pairs.
Require rho<=2^(-38), fixed q=20, at most five pieces per pair and three
per mean. No increased T, alternative smoothing or center truncation.

At most seven million Gaussian-factor evaluations per full precision
pass and 21 million across all three passes are allowed; the unsymmetrized
bound is 7*(4096*5*20*2 + 2*512*3*20)=6164480 per pass.
A combined pair exponential or symmetric reuse may reduce actual work.
The entire certified evaluator run has a cumulative 30-minute wall-clock
cap, including internal library calls. An external timeout must enforce
this even if a library's internal refinement loop lacks these counters.
These are ceilings, not runtime predictions.

Report seven fixed probes: zeta=-s/2, eta=s/2 for
s in {0,1/2,1,3/2,2}; additionally
(zeta,eta)=(-1/2+i/4,1/2+i/4) and
(-1/2+i/4,1/2-i/4). Each report contains Q1 at both points, Q2, QC,
their arithmetic radii and final canonical enclosures. The evaluator
and (1), not an interpolation through these probes, represent the full
function. No expected sign, repulsion or sine curve is an acceptance gate.

Preserve small source/certificate records and exact dyadic midpoint
data. Enclosures must serialize with outward rounding. Large regenerable
tables stay out of Git under [LARGE_FILES](../../../../../../LARGE_FILES.md).
If any gate fails, retain the exact failed clause, observed bounds and
cost. Completion with that failure is valid for this fixed pilot; it
does not exclude all certified methods. No larger search is authorized.

## 8. Collision controls and continuation

The following is a premise-level screen against
[controls12](../../../../../../result-summaries/12_collision_controls_and_screening.md)
and [avoid02](../../../../../../avoid/02_shape_only_arguments_and_the_controls.md).
Original collision computations were not rerun.

| Control family | Premise absent from canonical acquisition |
| --- | --- |
| Euler-factor | Literal unmodified zeta/theta coefficient and conductor identity |
| Weighted-square and finite-tail | Full normalized theta reflection/coefficient identity |
| Reflected super-Gaussian | Integer-square theta arithmetic |
| Smooth shape and positive primitive | Complete canonical coefficient expansion |
| Finite-prime orbit | Full reflection/all-coefficient identity despite matched finite data |
| Atomic threshold and exact finite profiles | Full theta profile and the source's eventual-simplicity property |
| RH-conditional theta-close endpoint | Ordinary Dirichlet-series arithmetic |
| Variable observation kernel | Literal cosine/Newman equation |
| Fractional actual-profile relaxation | Realizability as a complete integer zero divisor |

The generic transport and quadrature theorems remain valid for every
control satisfying their finite geometric hypotheses. At a multiple
zero they preserve m(m-1). A sign-bracket-only implementation fails its
completeness gate if an unaccounted multiple or nonreal label is present.
A legitimate all-box implementation need not reject a collision: it
computes its pair function, which is not an exclusion certificate.
Passing a finite region away from a control's event is also consistent.
No failure of canonical identity by a control estimates the actual
canonical pair value.

B07 closes at a concrete finite contract. **Next: [E] TND-OC-E09 — Sol**:
one proof check and one bounded certified acquisition/evaluation, with
one repair. A successful E09 would supply a finite empirical canonical
function with explicit error, not an ensemble law or high-height
asymptotic. A failure requiring different arithmetic access, complex
isolation or a larger regime returns to a separately classified B
decision. E03/E04 remain pending alternatives. E08 retains its accepted
status; these new claims have [author checking only](../reviews/10_TND_OC_B07_AUTHOR_SELF_CHECK_20261108.md).
The manuscript and root result/pattern summaries are unchanged because
this is neither manuscript integration nor investigation closure.

# E19 r1 — Recent analytical manuscript assessment

18 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Actual model and effort unavailable; assessor
settings inherited without serving attestation. The assessor authored none
of the manuscript sections. This is a separate internal shared-premise
LLM assessment, not specialist peer review.

**Final disposition: the revised analytical manuscript is accepted within
its stated identity, approximation-screen and conditional statistical
comparison domains. No required correction remains.** One analytical
assessment pass and one bounded correction check were performed under
[E19 r1][request]. This acceptance is internal and does not establish the
unacquired common-time approximation, canonical statistical tail or an
improved bound on Lambda.

All 14 original [assembled-source pins][pins] and all seven
[scientific-source pins][sources] matched at the first pass. The first-pass
mathematical disposition required only the three narrow scope/definition
clarifications preserved below, with no formula repair or new proof method.
The [correction manifest][correction] now pins all 14 final source files.
All match; 12 are unchanged. The two amended files are:

- `10_finite_hierarchy.tex`: 8,835 bytes, SHA-256
  `ec3d08c05ee4fddd69d6fba68f93627a85596e776193fb0d22c5d8042fb5b589`.
- `11_backward_statistics.tex`: 20,081 bytes, SHA-256
  `96572f61598005615df2616c735d30a973547c789e9f368d67797f43151bce5d`.

Reversing exactly the three documented text edits reconstructs both
original pinned hashes. All seven E18 scientific-source pins remain
unchanged. The correction makes the approximating interaction real,
qualifies the telescoping time derivative by a heat-flow slice satisfying
the pair law, and defines empty/singleton-window minimum gaps as infinity.
All three repairs close. Hashes identify assessed versions, not truth.

The authorized manuscript revision changes its introductory framework
relative to the older E16 r1 input binding. Preservation of the scientific
source notes is not a claim that every historical manuscript pin still
matches. E16 remains an unexecuted approximation task, and its source
binding must be explicitly refreshed without changing its scientific scope.

## 1. First-pass clarifications, now resolved

1. In `stat:telescoping`, a static all-real ordered configuration supplies
   `0<=M<=1/(2D)`. Say that the **pair-law right-hand side** `2-4DM` is
   nonnegative, or explicitly require a heat-flow slice before writing
   `D_t>=0`. A static configuration alone has no time derivative.
2. In `stat:pair-majorant`, specify that each real-zero window contains
   at least two occurrences, or define its minimum gap to be infinity
   when it has fewer. This makes `G_k` defined for every sampled block.
3. In `fin:transport-error`, state that the approximating interaction
   `m_N` is real, as for a conjugation-compatible divisor approximation.
   Then `W_N>0` and the displayed real logarithm is unambiguous. A complex
   approximation would instead need a chosen logarithm defined by the
   integral, which is unnecessary here.

These are local scope/definition repairs, not changes to the estimates.

## 2. Finite heads and the positive comparison

**Accept after clarification 3.** With fixed ell, the scaling
`s_n=ell^(2n)S_n`, `v_n=ell^(2n-1)T_n` and
`d/dsigma=ell² d/dt` preserves every coefficient of the physical hierarchy.
All nonlinear factors in row n have index at most n. Only the two linear
higher-index terms cross the cutoff, producing the four displayed rows.
For P=3, the lowest odd boundary is row 2 and is correctly retained.

The collar gives `|mu|<=gamma` and
`|w|/sqrt(|Q|)<=sqrt(q0)`. Summing against the complete absolute first
moment yields `|s_n|<=B1 L gamma^(n-1)` and
`|v_n|<=sqrt(q0) B1 L gamma^(n-3/2)`. The odd P row has size at most
`4P(P+3)sqrt(q0)B1 L gamma^(P-1/2)(1+d gamma)`; the P-1 row needs
`d` without an extra gamma. The even rows are no larger. Thus the
max-norm residual estimate and its fixed-height geometric decay are correct.

The coefficient from s_(n+1) to s_n is exactly `-4n(n+2)`; nonlinear
terms in row n do not contain s_(n+1). Hence the unweighted absolute
Jacobian norm is at least `4(P²-1)`. This does not turn the Gronwall
upper bound into an actual error lower bound, and the manuscript does
not claim that it does.

For the componentwise majorant, the retained descending path has product
`4^(P-1)(P-1)!(P+1)!/2`. Multiplying the first residual term
`4P(P+2)B1 L gamma^P` and the integrated exponential coefficient
`tau^P/P!` gives exactly
`(B1 L/2)(P+2)(P+1)!(4gamma tau)^P`. Positivity of all matrix powers
justifies retaining one path. The divergence is solely that of the
specified independent constant-tail, absolute-Jacobian allowance. It is
neither signed truncation instability nor a no-go theorem for compatible
closures. This is the first separate proof assessment of these Note15
calculations, now fully derived in the manuscript.

The finite polynomial Gaussian formula follows from the terminating
Taylor series and the exact Gaussian even moments. For H, source decay
controls the absolute integrand after the bound
`E exp(sqrt(2tau)|X|u)<=2 exp(tau u²)`, so Fubini on bounded tau,z is
legitimate. Neither formula proves common-time approximation of H by
P_N. That missing estimate and the later contour/moment transfer remain
explicitly open. The logarithmic transport error, once m_N is real, follows
by subtracting its defining integrals on each subinterval. The physical
inhomogeneous cost retains ell². No E16 theorem is imported.

## 3. Joint forcing, energy and deflation

**Accept.** The scaled third even row is
`12m s3+6s2²+12v2v3+12delta s2s3-60s4-72delta s5`.
Differentiating `F=12s2+16delta s3` produces the remainder coefficients
48, 192, 144, 192, -352, -1440 and -1152 shown in the manuscript.
The integrating factor is `W(x,sigma)²`, so the solution has `W^-2`
weights. The complete passage uses finitely many fixed orders and their
already established contour jets, not differentiation of a new sharp cutoff.

The energy calculation gives
`2delta delta''-(delta')²+4=8Fdelta²`, and integration by parts gives
coefficient -3 on the derivative-square integral. No division by delta
occurs. The constant scalar family `m=-h`, `F=2h²`,
`delta=-1/(2h)` saturates the weighted allowance while its multiplier
is `exp(4h(y-x))`. The absence of a divisor realization is explicit.
The two quartic heat controls give remainder signs ±704/b⁶ at the double;
they lack the canonical source and population and only test the stated
local algebra. These scopes agree with [E15][e15].

For the deflated entire function, derivatives of its genus-one linear
regularizers and affine prefactor vanish at orders n>=2. This gives
`U_n=-partial_w^n log G/(n-1)!`. The binomial series has ratio at most
1/16 and an absolute complete-divisor majorant. The coefficient in the
forcing expansion is `12(k+1)+8k(k+1)=4(k+1)(2k+3)`; its omitted-tail
bound and merger value `-2ell⁴ partial_w⁴ log G` are correct. The fixed
xi correspondence uses `(1-ic)/2-varrho=iw/2`, giving the factor `(i/2)^n`
and both target subtractions. The heat-deformed completion satisfies
`partial_t Xi_t=(1/4)partial_zeta² Xi_t`. A superzeta translation parameter
is not heat time, and no external continuation theorem or signed estimate
is silently imported.

## 4. Selection, strict isolation and backward comparison

**Accept after clarification 1.** The existing collar makes the two target
occurrences mutual nearest neighbors, while allowing exterior pairs to
be closer. At a simple canonical slice the width-one strip and inherited
count `N_t(X)~X log X/(4pi)` contradict positive uniform separation by a
disjoint-disk packing argument. The statement is about complete simple
slices, not the existence of minima in finite regions. The shortest-pair
relative bounds follow from its two endpoint distances and vanish as
D tends to zero. The finite complex examples correctly distinguish
closest-pair selection, conjugation admissibility and detection of nonreality.
The telescoping sum is correct in its stated globally separated real class;
clarification 1 separates its static calculation from the dynamical use.

The manuscript explicitly changes domain to adjacent real pairs on
`0<=t*-Delta<=t*<=1/2`. Strict adjacency supplies a cleared count-two circle.
At a frozen time, complete product convergence and spatial jets pass the
heat derivative of the logarithmic derivative, counted coordinates and
M to the limit. Finite nearby denominators and absolute inverse-square
tails suffice; no factor-four radius ratio occurs in the algebra. Thus
only the identities extend to this domain, not the old quantitative collar
bounds or a common-time finite-divisor convergence theorem.

Physical backward time gives `D_u=-2+4DM` and
`M_u=-2M²+12S2+16DS3`. Complete exterior reality makes every Q positive.
The comparison `M>=b0/(1+2b0u)` and the integrating factor
`a^-2`, with `a=1+2b0u`, yield
`D(u)>=a[d0 a-2u]`. Positivity of the affine bracket at 0 and Delta
proves the strict first-collision exclusion; continuity of D approaches
the event without requiring an isolating collar there. The exact cost
has the negative exponential and is bounded by `2u/a`.

The two adjacent exterior zeros contribute
`1/[hL(hL+g)]+1/[hR(hR+g)]`. For equal gaps this gives b0 d0=1/4
and duration <g²/6, compared with <g²/8 at b0=0. When both neighbor gaps
dominate g, the relative improvement tends to one. The quadratic control
collides exactly at equality, checking strictness. These are conditional
local comparisons, as in [E17][e17], not an acquired uniform canonical step.

## 5. Minimum law, statistics and global scope

**Accept after clarification 2.** A finite minimum of C1 branches is locally
Lipschitz; tied branch derivatives agree almost everywhere on their tie
set. The fixed finite block average therefore gives the displayed weak
law without an unproved expectation interchange. The marginal minimum
couples to the active pair's complete exterior interaction. Integrating
`D_u>=-2` gives the correct event inclusion and one-sided tail transfer.
Pair switching is handled by the envelope and does not transfer the old
pair's anchors or exterior moments.

Once each window minimum is defined, the equivalence with a nonzero
unordered distinct-label pair count and its upper bound by E C are exact.
An exact minimum law requires void information; a one-sided majorant may
use a pair statistic. Three consecutive gaps require the absence of
intermediate zeros in addition to four locations. The fixed-blur OC
results supply regularity but neither an initial profile nor a sharp gap
tail, and their resolution costs remain explicit. Distinct labels at a
multiple zero are correctly retained.

The probability threshold <1/K forces the integer bad-block count to
vanish. Larger small probabilities allow exceptions. Continuous centers
need an event-visibility measure, and time averages need a whole-interval
or occupation argument. Complete exterior reality stops at the first
anywhere collision; finite blocks require boundary coverage and a uniform
high-height argument to rule out escape to infinity. The manuscript does
not claim those acquisition steps or a new Lambda upper bound.

## 6. Sources, coherence and limits of this assessment

The [Rodgers–Tao primary paper][rt], introduction and §9, confirms the
lower-bound direction and the contradiction under Lambda<0. Its restricted
motion theorem is not used as a positive-time premise. The [Akbari et al.
primary paper][akbari] treats compatibility and positivity separately in
its fermionic examples; it supplies organizational guidance, not a theta
obstruction. [Chorin–Hald–Kupferman §2][chk] defines a phase space, flow and
projection framework before its memory identity. The manuscript does not
assert that an abstract S/T flow satisfying these requirements has been
constructed. These primary passages were checked in this assessment;
no external PDF was written into the repository.

The revised title, abstract and roadmap follow the actual development:
regular hierarchy, finite-head limitations, complex powers and contours,
joint transport, then the distinct all-real statistical domain. The
unchanged core results retain their earlier assessments, and their usage
has not been broadened by the new sections. The discussion preserves the
scalar, static and positive-comparison classes in every negative conclusion.
The family-by-family controls identify the absent canonical source,
reflection, order/population, physical readout, integer realization or
common-evolution premise. No numerical sample carries a proof claim.

The [result index][results], [classification01][a01], [scope07][a07] and
[shared-premise05][a05] fix the evidence level: an analytical working draft
with internal assessment. PDF compilation and visual inspection belong to
E20 and are not certified by this mathematical review.

[request]: ../research-progress/handoffs/VCD-GT-CM-E19-r1.md
[pins]: ../research-progress/handoffs/VCD-GT-CM-E19-inputs-r1.json
[sources]: ../research-progress/handoffs/VCD-GT-CM-E18-inputs-r1.json
[e15]: 08_VCD_GT_CM_B03_JOINT_TRANSPORT_ASSESSMENT_20261118.md
[e17]: 09_VCD_GT_CM_E17_REGIONAL_STATISTICS_ASSESSMENT_20261118.md
[results]: ../../../../../../result-summaries/README.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a05]: ../../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[rt]: https://arxiv.org/html/1801.05914v5
[akbari]: https://arxiv.org/html/1204.4395v1
[chk]: https://math.huji.ac.il/~razk/Publications/PDF/CHK00.pdf

[correction]: ../research-progress/handoffs/VCD-GT-CM-E19-correction-inputs-r1.json

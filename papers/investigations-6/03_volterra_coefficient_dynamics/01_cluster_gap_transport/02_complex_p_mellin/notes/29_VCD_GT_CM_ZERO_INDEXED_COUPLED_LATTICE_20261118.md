# B08 r1 — The author's zero-indexed coupled lattice

18 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Actual model and effort unavailable in CM
chat0003; two read-only advisers checked the formulation with inherited
settings. This is a conceptual note with elementary exact identities and
internal shared-premise checks, not a separately assessed approximation
or stability theorem. [B08 request][request] · [Sole register][register]

The author proposes treating M(p,q,t) as a coupled lattice with an
additional zero index. **The useful formulation is an edge-indexed
hierarchy whose rows share one common divisor.** The new index should
carry the overlap constraints; independently duplicating a single-pair
moment system would not enforce them.

This is the current conceptual continuation after [Note28][compact]. The
preceding compact source selection is complete: [E25][review] accepts
Note27's <.0896 constant-barrier allowance against the .1003 target.
That scoped result does not exclude the coupled lattice, time-varying
comparisons or actual descent. No numerical acquisition was launched.

| Next task | Type / recommended model | Readiness | Expected output |
| --- | --- | --- | --- |
| B08 r2, lattice quantity and finite-block consumer selection | B / Astra: an estimate that uses overlap must still be chosen | Conditional; no new execution packet | One source-acquired joint quantity with a finite physical-time consequence for individual gaps, compared with direct common-source evolution |
| E16 r2, optional common-field approximation | E / Sol: existing method and inputs fixed | Ready, unchanged and unexecuted | Its existing common-time finite-product proof; any multi-pair enlargement must be stated explicitly before execution |

Read [result summaries][results] and [avoid][avoid], especially
[cluster18][cluster], [controls12][controls], [classification01][class],
[scope07][scope], [joint12][joint] and [circularity14][circular]. The
identities below organize realizability and possible correlated estimates;
they are not a new positive source bound or an RH criterion.

## 1. Index the adjacent pair, retaining the existing p,q convention

On a real-simple ordered divisor interval write its zeros x_n(t), and
let g_n=x_(n+1)−x_n>0. Matching [Note08][split], define

    M_n(p,q;t)= sum_(k != n,n+1)
        (x_k−x_(n+1))^(−p) (x_k−x_n)^(−q),                 (1)

initially for nonnegative integer p,q with p+q>=2. This is exactly
P_(p,q) for the nth pair. The index is attached to the left zero, hence
to an edge, not to a new independent family of exterior sources.
The two degrees resolve the dependence on the two target zeros; n
resolves where that pair sits in the same divisor.

The complete sums converge absolutely in the established fixed-order,
cleared-pair domains. Complex powers require the previously specified
branches and contour domains; they are not supplied merely by adding n.
If only a finite block of real zeros is known, keep all other zeros in
a complete exterior resolvent. Do not assume the entire canonical divisor
is real to obtain an ordered all-gap formula.

Note08's complete p,q recurrence applies at each edge, with its separation
d0 replaced by g_n and every P replaced by M_n. In particular, in forward
physical Newman time,

    g_n' =4/g_n−2g_n M_n(1,1),
    D_n'=2−4D_n M_n(1,1),        D_n=g_n²/4.                 (2)

The moment degrees couple upward exactly as in Note08. The index coupling
is encoded by the common zeros and the compatibility equations below;
there is no new arbitrary nearest-neighbor term to append to that recurrence.

## 2. The explicit coupling through the gap sequence

When the complete divisor is real and ordered, define the accumulated
left and right distances

    L_(n,m)=g_(n−1)+...+g_(n−m),
    R_(n,m)=g_(n+1)+...+g_(n+m),       m>=1.

Splitting the sum (1) on the two sides gives exactly

    M_n(1,1)= sum_(m>=1) {
        1/[L_(n,m)(L_(n,m)+g_n)]
        +1/[R_(n,m)(R_(n,m)+g_n)] }.                        (3)

Every gap participates in other rows through these cumulative distances.
Thus (2)–(3) are a spatially nonlocal evolution for the complete gap
sequence, up to the usual translation coordinate. The p,q hierarchy is
a moment resolution of that interaction. Neither an adjacent-only lattice
nor a finite closed system follows from (3).

For a finite known real block, the corresponding finite part of (3) is
valid and the remaining complete exterior contribution must be retained
or bounded separately. The signs of nonreal exterior terms cannot be
replaced by positive real-gap summands.

The uniform-spacing cosine control checks the normalization: if g_n=g
for all n, each side of (3) sums to 1/g², so M_n(1,1)=2/g² and (2) gives
g_n'=0. This is a noncanonical algebra control, not a theta population
model or evidence that canonical spacings are constant.

## 3. Neighboring rows cannot be assigned independently

For every integer r>=2,

    M_n(r,0)+(-g_n)^(−r)
       =M_(n+1)(0,r)+g_(n+1)^(−r).                         (4)

Both sides equal the complete reciprocal rth moment anchored at the
shared zero x_(n+1), after restoring the one neighbor excluded by that
pair. In particular,

    M_n(2,0)+1/g_n² = M_(n+1)(0,2)+1/g_(n+1)².

Within one row, subtracting the two endpoint factors term by term gives

    g_n M_n(p,q)
       =M_n(p,q−1)−M_n(p−1,q),                             (5)

for p,q>=1, p+q>=3. For (p,q)=(1,1), interpret only the common-cutoff
first-power *difference*: its combined summands decay quadratically.
Do not introduce two unqualified absolute first-power sums.

The corresponding entire generating object is particularly simple. Set
B(z,t)=H_z/H and

    R_n(z,t)=B(z,t)−1/(z−x_n)−1/(z−x_(n+1)).

Then, off the displayed poles,

    R_(n+1)=R_n+1/(z−x_n)−1/(z−x_(n+2)).                  (6)

This relation is algebraic for any three distinct labeled zeros; it does
not require the rest of the divisor to be real. Local Taylor coefficients
recover shared-root moments of order at least two with their usual signs.
More generally, with a=x_n, b=x_(n+1), the mixed generating function is

    −[R_n(b+u)−R_n(a+v)]/(b−a+u−v)
       = sum_(p,q>=1) M_n(p,q) u^(p−1) v^(q−1).

This follows by subtracting each exterior simple pole and expanding its
two geometric series in cleared neighborhoods; the apparent coincident-
argument quotient is removable. Translation must not cross an unremoved
neighboring pole. Remove the entire selected block or use overlapping
cleared charts. The common meromorphic field itself obeys

    B_t=−B_zz−2 B B_z,

obtained by differentiating H_t/H=−(B_z+B²). This is the exact
logarithmic-derivative representation of the same heat field, not a new
canonical estimate. A general collection of independently truncated moment
rows need not satisfy (4)–(6), or come from any divisor at all.

## 4. A block flux cancellation retained by the common source

At a simple root define the finite part of the complete logarithmic
derivative

    U_n = lim_(z→x_n) [H_z/H−1/(z−x_n)]
        =H_zz(t,x_n)/(2H_z(t,x_n)).

The exact heat equation gives x_n'=2U_n. Comparing its gap difference
with (2) gives

    g_n M_n(1,1)=2/g_n−(U_(n+1)−U_n).                     (7)

Summing a fixed block n=a,...,b yields

    sum_(n=a)^b g_n M_n(1,1)
       =2 sum_(n=a)^b 1/g_n−(U_(b+1)−U_a).                (8)

The interior force differences cancel. This is one concrete correlation
that independent per-edge absolute bounds would discard. It follows
from the complete source finite parts, not an unregularized infinite
single-root sum. It is also the direct equation for the block length
x_(b+1)−x_a, so the matched direct comparator receives it too.

For example, with exact gaps and approximated common node forces whose
endpoint errors satisfy |Uhat−U|<=epsilon, reconstruct the *weighted
aggregate* in (8) from those common endpoints. Its force error is <=2epsilon,
independent of the number of edges. Summing separately allowed edge-force
errors would instead pay up to twice the edge count times epsilon. This
is an elementary correlated-error observation, not a measured source
cost gain. With approximate positive gaps, also pay

    2 sum |1/ghat_n−1/g_n|
       <=2 sum |ghat_n−g_n|/(min(ghat_n,g_n)^2),

and any further weight/product errors if a different aggregate is used.
Small gaps can make that additional payment large.

Equation (8) controls a block aggregate, not the regional minimum. A long
block can keep its total length while one interior gap closes. To protect
every gap, a new estimate must prevent concentration of the defect into
one edge; a boundary cancellation alone does not do this. The zero-index
proposal is therefore a plausible place to retain needed correlations,
not an acquired substitute for the missing canonical inequality.

## 5. Compatible finite reconstruction and collision scope

A single finite polynomial heat field gives all its roots and every
moment row at once. As long as the roots are simple, its adjacent rows
automatically satisfy (2), (4)–(8). This is the compatibility advantage
of the shared finite-divisor route discussed in [Note15][bbgky]. It is
also why independently truncating moment orders at every n is a different
approximation, generally without a common divisor.

The unresolved E16 common-time approximation theorem remains unresolved.
A finite polynomial being internally compatible does not prove its
canonical source error, stability as the block/order grows, or a signed
transport gain. A finite-index cut also has nonlocal exterior forces and
moving boundary data; the omitted zeros cannot simply be dropped. The
already scoped absolute-propagation difficulty in Note15 still applies
to its stated comparison class and is not removed by notation.

The full adjacent-edge chart is valid only up to its relevant first loss
of simplicity or separation. If x_n=x_(n+1), that pair has the regular
S/T description of [Note09][regular], but its neighboring edges lose an
exterior separation: an excluded target root meets an exterior occurrence.
Thus not every edge chart remains regular simultaneously. A common
polynomial or larger-cluster symmetric-coefficient representation can
remain regular, while ordered individual labels and split-pole charts
must be stopped or replaced explicitly.

The physical quadratic and cosine-plus-constant collisions obey the
applicable simple-root identities before collision; the lattice notation
cannot exclude them. The other source-control families retain their
failed complete-theta arithmetic, reflection, order or physical-readout
premises listed in [Note27 §7][screen] and [controls12][controls]. No new
universal positivity principle is asserted for the lattice.

## 6. The next question

The next bounded B question is: **which common-source lattice quantity
controls concentration into an individual gap over a fixed physical time,
while preserving the shared-divisor constraints?** A useful answer must
specify the finite real block and complete exterior, the claimed margin,
the boundary and moment-order errors, and a direct comparator supplied
with the same U, gaps and source values. A block flux identity alone does
not pass that test.

An optional E16-based experiment would use one initialization and one
common heat polynomial for an entire finite block, with field/jet errors
transferred to every fixed-order edge moment up to common contour-clearance
loss. That would require an explicit amendment of E16's existing scope;
it is not silently issued here and does not make E16 mandatory.
No lattice simulation, new approximation theorem or new K bound is claimed.

[request]: ../research-progress/handoffs/VCD-GT-CM-B08-r1.md
[register]: ../research-progress/01_VCD_GT_CM_RESEARCH_PROGRESS_20261117.md
[compact]: 28_VCD_GT_CM_COMPACT_SCREEN_SYNTHESIS_AND_CONTINUATION_20261118.md
[screen]: 27_VCD_GT_CM_COMPACT_CONTOUR_SELECTION_AND_FLOOR_SCREEN_20261118.md
[review]: ../reviews/13_VCD_GT_CM_E25_COMPACT_FLOOR_SCREEN_ASSESSMENT_20261118.md
[split]: 08_VCD_GT_CM_E09_SPLIT_POLE_INTEGER_HIERARCHY_20261118.md
[regular]: 09_VCD_GT_CM_E10_REGULAR_ODD_EVEN_HIERARCHY_20261118.md
[bbgky]: 15_VCD_GT_CM_B05_BBGKY_TRUNCATION_RECONSIDERATION_20261118.md
[results]: ../../../../../../result-summaries/README.md
[cluster]: ../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[class]: ../../../../../../avoid/01_restating_the_target.md
[scope]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[joint]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[circular]: ../../../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md

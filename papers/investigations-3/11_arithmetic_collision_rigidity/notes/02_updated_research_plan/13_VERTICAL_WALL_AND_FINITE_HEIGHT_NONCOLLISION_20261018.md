# A certified vertical wall and finite height noncollision

18 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. **GPT-6.1 Sol (`gpt-6.1-sol`), actual reasoning
effort ultra**, verified from execution metadata. Derivation and parallel
checks are internal same-model work, without independent specialist review.

This executes the finite-consumer part of Stages 3–5 in [overview 02][plan],
using the nonstationary tail from [Note 11][tail] and the whole-cell
machinery in [Note 12][signed]. The [result-summary index][summaries] and
[patterns-to-avoid index][avoid] apply, especially [finite versus global
claims][scope], [collision controls][controls] and [target classification][target].

**Result.** A seven-cell interval certificate proves

\[
 |H(t,1000+iy)|>0.00425\,G_*,\qquad
 0\le t\le1/5,\quad |y|\le1,
 \qquad G_*=1000^{7/4}e^{-125\pi}.
 \tag{1}
\]

A finite propagation argument, with the published initial zero verification
specified below, then proves

\[
 \boxed{H(t,x)^2+H_x(t,x)^2>0
 \quad(0<t\le1/5,\ |x|\le1000).} \tag{2}
\]

Together with Note 12's signed certificate on
`[1/100,1/5] x [999,1001]` and evenness, this closes the finite part

\[
 H^2+H_x^2>0\quad\hbox{on}
 [1/100,1/5]\times[-1001,1001]. \tag{3}
\]

These are finite-height statements. The exterior bridge remains open.

## The wall certificate and its complete error

The [wall record][wallrecord] covers the exact closed rectangle
`(t,y) in [0,1/5] x [0,1]` at the single fixed real part `x=1000`.
It uses four closed time slabs and seven accepted cells in total, with
three rejected coarse choices retained. A selected real or imaginary
coordinate of the normalized field has constant sign on each entire cell.
The minimum selected-coordinate lower bound exceeds `0.00425150082920`.
This proves (1), since the absolute value of either coordinate is a lower
bound for the complex modulus. Conjugacy covers the negative y half,
including y=0. Every time endpoint, cell seam and y=1 is included.

Parameters are frozen: `d=pi/8-4*log(1000)/1000`, first omitted mode
`m=12`, retained source cutoff `U=2`, and comparison constant `G_*`.
The midpoint remains `(21/200,1000)`. The 51 midpoint jets in Note 12
are reused with their original quadrature radii and exact dyadic
serialization. Only one positive-majorant integral is newly computed.

For `Y=1`, the uniform finite-integral derivative bound through order 52 is

\[
 M_{52,1}=1000^{9/4}\int_0^2
 \sum_{n=1}^{11}(2\lambda_n^2+3\lambda_n)
 e^{u^2/5+10u-\cos(4d)\lambda_ne^{4u}}
 [1+(u+d)^{52}]\,du,\qquad \lambda_n=\pi n^2.
 \tag{4}
\]

The factor `exp(Yu)` pays for the complex spatial segment. The bound
`(u+d)^j <= 1+(u+d)^52` pays all required derivative orders. The finite
paired contour integral solves the heat equation with its cutoff fixed,
so its spatial degree 24 and time degree 12 Taylor polynomial uses midpoint
orders through 50, with remainder derivatives through 52. On a wall cell
with `R=max|y|` and `Delta=max|t-21/200|`, its remainder is at most

\[
 M_{52,1}\left(\frac{R^{25}}{25!}
       +e^R\frac{\Delta^{13}}{13!}\right). \tag{5}
\]

This includes t=0; the largest time distance is `21/200`, not `19/200`.
Quadrature radii propagate with absolute spatial and time Taylor weights.
The polynomial image itself is enclosed by outward complex arithmetic.
The mode error consumes Note 11 with `Y=1` and the actual frozen phase gap;
the retained-source tail uses the concave tangent from Note 12 with `9+Y`
in place of 9. Every admissibility inequality is evaluated with intervals.
The largest added coordinate error is below `1.532293e-11 G_*`, within
the declared `1e-8 G_*` target. No spatial cell is substituted by its centre.

The extra wall computation takes about `0.033` seconds and 465 positive
quadrature callbacks, using ten cell calls and no new midpoint quadratures.
These are incremental costs; the original midpoint setup from Note 12 is
also required. [Review 11][review] and the [replay][replay] check the wall
again from its source and recompute its weakest margins.

## A finite propagation lemma

Let `F(t,z)` be an analytic heat family satisfying `F_t=-F_zz` and real
reflection `F(t,conj(z))=conj(F(t,z))` for real t. Fix `X,T>0`. Assume
throughout `0<=t<=T`:

1. All zeros lie in `|Im z|<=1`.
2. The imaginary-axis segment `F(t,iy)` is nonzero for `|y|<=2`.
3. The vertical wall `F(t,X+iy)` is nonzero for `|y|<=1`.
4. Every zero at t=0 with `0<=Re z<=X` is real.

Then all zeros in that finite vertical region remain real on `[0,T]`,
and all its real zeros are simple for `0<t<=T`. Initial simplicity is
unnecessary. This is a finite-domain lemma with substantive boundary and
initial conditions, not a new global RH criterion.

**Proof.** Use the fixed rectangle
`Omega={0<Re z<X, |Im z|<2}`. The strip condition excludes its horizontal
edges and the portions of the right edge above `|Im z|=1`. The other two
boundary hypotheses exclude the remaining edges. Hence the argument
principle keeps the finite total number of enclosed zeros, with
multiplicity, constant as t varies.

At a simple real zero, the implicit function theorem and conjugation
uniqueness keep its branch real. At a real zero of order m>=2, the analytic Taylor series and
`F_t=-F_zz` give the leading weighted expansion
`a_m (2h)^(m/2) He_m(z/sqrt(2h))`, where
`a_m=(partial_z^m F)(t_*,x_*)/m!` and `z` is measured from x_*. Terms of
higher weighted degree are smaller on bounded `z/sqrt(|h|)` sets.
The simple roots of this Hermite polynomial therefore give:

\[
 z_k(t_*+h)=x_*+\sqrt{2h}\,\lambda_k+O(h),\qquad
 \lambda_1<\cdots<\lambda_m\ \hbox{real and simple}.
 \tag{6}
\]

For h>0, small disjoint disks centred on these real leading points each
contain exactly one zero. Each disk is invariant under conjugation, so
that zero is real. Rouché's theorem accounts for all m local zeros. For
h<0, at least one nonzero Hermite root instead gives a nonreal zero at
distance of order sqrt(|h|) from the real axis. This includes every
multiplicity m>=2.

Initially there are finitely many zero clusters. Their simple-root or
forward Hermite continuations, together with the constant total count,
make every enclosed zero real for a short initial time. The set of times when every enclosed zero is real is closed by
compactness, the fixed boundary-free count and Rouché. If the initial
interval of such times had a right endpoint before T, every zero would
therefore be real at that first-exit time. A repeated zero there would have nonreal predecessors,
contradicting reality before the exit. Otherwise all zeros are simple and
persist real beyond the exit by uniqueness. Both possibilities contradict
a first exit. Finally, a repeated zero at any positive time, including
T itself, would again have nonreal predecessors inside the rectangle.
Thus every positive-time real zero is simple. Boundary zeros are already
excluded by the hypotheses. This proves the lemma.

## Imported inputs and the theta application

The normalization is the manuscript's `H(0,z)=xi((1+iz)/2)/8`.
[Polymath, Proposition 3.1(ii) and Theorem 3.2][polymath] supply the local
Hermite splitting and preservation of the initial unit zero strip. These
are named classical inputs, freshly checked in the primary source.
Positivity of the theta source gives `H(t,iy)>0` directly from its cosh
integral. Equation (1) supplies the numerical wall hypothesis.
[Platt–Trudgian, Theorem 1][platt] supplies initial reality through zeta
height 500, using only a small portion of its verified range. The factor
1/2 converting Re z to Im s is retained. No initial simplicity or
zero-velocity estimate is imported. The finite lemma therefore gives (2).

The lemma does not follow merely from a published canopy: a canopy can
leave small imaginary heights uncontrolled. Here the wall includes y=0
and the full interval `|y|<=1`. No conclusion about real zero motion is
inferred from a time-zero verification alone.

## Controls and global coverage

The approximation is specific to the unchanged normalized theta source.
The weighted-square and finite-prime controls lack its complete reflection;
the reflected, primitive and counter-kernel controls lack its exact square
expansion or coefficient contract. Our numerical wall is not substituted
into any of those fields. The [fresh control record][controlrecord] rejects
the applicable source-specific event boxes and Euler witness.

The finite propagation lemma itself is generic. A polynomial event
`F(t,z)=(z-1000)^2-2(t-1/10)` challenges the same signed and wall
polynomial interface: both reject a surrounding event box. Its initial
zeros are `1000 +/- i/sqrt(5)`, so its initial-reality hypothesis fails.
This explicitly prevents using a real positive midpoint margin in place
of the whole time-wall contract. No event height is invented for the
controls whose theorems give only existence.

For the overview's slab endpoint `tau=1/100`, the current coverage ledger is:

| Region for tau<=t<=1/5 | Established input |
| --- | --- |
| 0<=x<=1000 | Finite propagation lemma with the complete certified wall and published initial verification |
| 999<=x<=1001 | Note 12 strict signed certificate with complete finite errors |
| 1001<x<exp(6400) | Uncovered finite bridge |
| x>=exp(6400) | Inherited eventual-exclusion corollary cited in Note 10; no improved outer threshold here |

Evenness supplies negative heights. The overlap `[999,1000]`, wall
endpoints and time endpoints close all finite seams. The [updated
consumer ledger][ledger] supersedes Note 10's earlier finite-coverage
inventory while preserving its historical record. A global Newman bound
still requires closing the remaining bridge or a different complete outer
consumer. This round does not meet that global gate.

Status: the wall is **interval-certified**; the finite propagation result
is **proved in-note from named imports and the wall certificate**. Review
remains internal and same-model. The next useful step must address the
remaining bridge or an effective signed/exterior estimate; these finite
results do not justify an uncontrolled height scan.

[plan]: ../../research-overview/02_UPDATED_RESEARCH_OVERVIEW_AND_SOL_EXECUTION_PLAN_20261018.md
[tail]: 11_EFFECTIVE_NONSTATIONARY_ARITHMETIC_TAIL_20261018.md
[signed]: 12_HIGH_HEIGHT_SIGNED_CONSUMER_AND_MATCHED_COMPARISON_20261018.md
[summaries]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[scope]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[target]: ../../../../../avoid/01_restating_the_target.md
[wallrecord]: ../../numerics/high_height_consumer/VERTICAL_WALL.json
[replay]: ../../numerics/high_height_consumer/REPLAY.json
[ledger]: ../../numerics/high_height_consumer/HIGH_HEIGHT_CONSUMER_LEDGER_20261018.json
[controlrecord]: ../../numerics/high_height_consumer/CONTROLS.json
[review]: ../../reviews/11_HIGH_HEIGHT_SIGNED_AND_VERTICAL_WALL_REVIEW_20261018.md
[polymath]: https://arxiv.org/html/1904.12438v2#S3
[platt]: https://arxiv.org/html/2004.09765v1#S1

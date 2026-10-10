# A regular adjoint certificate on a complete physical cell

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex). Reasoning effort: the active setting is not exposed
to this session; no level is inferred. The outward arithmetic and parallel
reviews are internal LLM checks, not independent mathematical validation.

A fixed value-and-slope direction gives a strict, fully paid certificate
on a nonempty physical rectangle with all 22,066 arithmetic terms retained.
Both separate coordinates change sign on this rectangle, so neither
single global coordinate enclosure excludes a collision. Their correlated
combination stays positive. This completes a bounded calibration of the
first proof milestone, conditional on the manuscript's imported complete
holomorphic disk interface. It supplies no uniform shrinking-family
estimate or advantage over an optimally subdivided scalar atlas.

## The domain and its fixed cutoff

Set
\[
N=22066,\quad t_0=\frac1{2\log N},\quad x_0=4\pi N^2,
\qquad
\mathcal D=\{t_0\le t\le t_0+8\cdot10^{-6},\quad
                 x_0+0.3\le x\le x_0+0.7\}.
\tag{1}
\]
For each point define the scale \(L=\log(x/(4\pi))\). Outward
enclosures give
\[
0.04999103540096768<t<0.04999903540096769,
\]
\[
20.00358648268<L<20.00358648276,
\quad 1<tL<1.00016002870<3/2,
\]
and
\[
N^2<\frac{x}{4\pi}+\frac t{16}< (N+1)^2.
\]
Consequently the natural cutoff equals \(N\) on the entire rectangle;
all spatial derivatives use that same fixed integer. No derivative
follows the curve \(tL=\text{constant}\).

## A fixed physical direction and its regular transport witness

With the complete physical sum \(S=\sum_{n\le N}q_n\), choose
\[
y=(1,0.15L),\qquad U=S+0.15S',\qquad
y\cdot Cq_R=\Re U.
\tag{2}
\]
The physical differential expression is fixed, although its second
coordinate scales with the local definition of \(C\). Its coefficients
remain smooth on \(\mathcal D\); no division by either observed
coordinate occurs.

Use the tree construction in
[Note 2](2_SHARP_ADJOINT_RESIDUALS_AND_RESTRICTED_PRIME_OBSTRUCTION_20261010.md),
with any prime-division spanning tree. The covector sum there is
\(Z=\overline U\), so
\[
z_0=\Im U,\qquad r=(1-\Re U)b,\qquad
\mathcal R=|1-\Re U|.
\tag{3}
\]
The edge multipliers are given explicitly by Note 2, equation (3), and
remain regular even if the two observations vanish. Their transport
pairing is exactly zero; this proof does not approximate edge equations
or hide multiplier-weighted edge defects.

The [outward checker](../numerics/check_regular_adjoint_cell.py) gives
the following deliberately rounded outward bounds from the
[small record](../numerics/REGULAR_ADJOINT_CELL_RECORD_20261010.json).

| Complete quantity on the rectangle | Verified enclosure or upper bound |
| --- | --- |
| \(\Re U\) | \([0.5701248,1.3556811]\) |
| \(\mathcal R\) | \(<0.4298752\) |
| Complete disk majorant \(\eta\) | \(<0.00964146\) |
| Directional support \(h(0.15L,1)\) | \(<3.083857\) |
| Conservative \(\|y\|_2\) upper bound | \(<4.000538\) |
| \(1-\mathcal R-\eta h/2\) | \(>0.5552583\) |
| \(1-\mathcal R-\eta\|y\|_2/2\) | \(>0.5508393\) |

Because \(L>20\), the support branch is
\(h(0.15L,1)=0.15L+1/(0.6L)\). The paid error is exactly the
manuscript's complete majorant
\[
\eta(t,x)=5\exp\{-tL^2/16-L/4\}.
\tag{4}
\]
At any genuine joint zero, the correlated disk body implies
\(|y\cdot Cq_R|\le\eta h/2\). Equations (2)--(4), or directly the
manuscript's directional certificate theorem, contradict that bound.
Therefore
\[
\boxed{(H_t(x),H_t'(x))\ne(0,0)\quad\text{throughout }\mathcal D,}
\tag{5}
\]
conditional on that imported disk interface throughout the rectangle.
This excludes every real multiplicity at least two on the stated domain.

## Why the two global scalar enclosures fail

The complete separate hulls are
\[
\Re S\in[-0.180089915,1.085055475],\quad
\Re S'\in[-2.333718877,6.670379337].
\]
They each contain zero. This is not solely a loose interval effect:
uniform paid endpoint enclosures imply
\[
Q_t(x_0+0.3)<0<Q_t(x_0+0.7),
\]
\[
Q_t'(x_0+0.7)<0<Q_t'(x_0+0.3),\qquad Q_t=H_t/A_t.
\tag{6}
\]
For every fixed time in the rectangle, both \(Q_t\) and \(Q_t'\)
have a zero inside its spatial interval. Equation (5) proves that these
zeros cannot coincide. The statement about \(Q_t'\) is a normalized
slope statement; away from \(Q_t=0\), its zero need not be a zero of
\(H_t'\).

The direction retains the variation of value and slope together. The
sharp residual theorem shows that it adds no new pointwise information
to the correlated observation pair. The same forty recorded subcells
also exclude this rectangle with separate paid tests: 38 by value and
two by derivative. The bounded result is a regular correlated
certificate with fully explicit payment, rather than evidence of a
general arithmetic lower bound.

## Outward computation and the complete error budget

The checker uses the retained 60-digit Decimal interval arithmetic in
program 13. It verifies SHA-256 hashes before importing both the interval
source and its corrected integer-power implementation. All sign tests
use directed interval operations. Logarithms and exponentials use
adjacent values around correctly rounded Decimal evaluations; pi,
arctangent and trigonometric reduction carry explicit series remainders.
No binary floating-point value enters a mathematical enclosure.

At \((t_0,x_0)\), put \(\delta_n=\log(N/n)\), with the frozen
spatial phase \(e^{-ih\delta_n/2}\). Complete frequency moments
through degree 11 are evaluated at \(h=0.5\), retaining the physical
carrier. The degree-12 absolute frequency moment pays both the value
and derivative Taylor tails. Forty closed spatial subintervals of width
0.01 cover \([0.3,0.7]\). The combined Taylor coefficients are formed
before interval evaluation, so the value/slope correlation is retained.

The actual spatial multiplier is \(g_n\) from Note 2. Its discrepancy
from the frozen multiplier is
\[
g_n+i\delta_n/2=-tV\log n/4
 -i[\Omega-c\log N+(c-1/2)\delta_n].
\]
Its integrated exponential bound pays the entire spatial transport
from \(h=0\) to \(h\le0.7\), including amplitude drift. At fixed
height the exact time multiplier and mixed derivative are
\[
\chi_n=\partial_t\log q_n=(\log n)^2/4-\alpha_r\log n/2
               +i\alpha_i(\alpha_r-\log n)/2,
\]
\[
\partial_tg_n=-V\log n/4
 -\frac i4[U(\alpha_r-\log n)-\alpha_iV],\qquad
\partial_tq_n'=(\partial_tg_n+g_n\chi_n)q_n.
\]
Absolute sums of these exact multipliers over the whole time-height
rectangle pay its time thickness. These payments are added to the
Taylor remainders before taking any sign.

The recorded total physical value error is below 0.017606839, and the
physical derivative error is below 0.017544256. Their spatial portions
are below \(3.031\cdot10^{-9}\) and \(7.516\cdot10^{-9}\),
respectively; time transport dominates. The complete approximation
majorant (4) and the Cauchy slope payment \(L\eta\) are then included
in the certificate and endpoint assertions. No block inherits a
separate candidate condition.

Run from the repository root:

```sh
python3 papers/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/numerics/check_regular_adjoint_cell.py /tmp/project17_regular_cell_replay.json
python3 papers/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/numerics/check_adjoint_transport_optimality.py /tmp/project17_adjoint_algebra_replay.json
```

The first command takes approximately 25 seconds on the development
machine. Only source code and small records are retained, following
the repository large-file policy. Runtime metadata can differ between
replays; the assertions and directed endpoints establish the result.

## What this completes and what comes next

The initial proof milestone has a nonempty, fully paid calibration cell.
The accompanying sharp residual and restricted-prime results identify
the remaining analytical task: prove a correlated complete-source bound
uniformly on a growing family, rather than infer it from graph energy.
There is no proved residual gap or multiplier growth exponent on such
a family. Cutoff boundaries, complementary parameter ranges, signed
theta overlaps and the small-time limit remain separate obligations.

The manuscript's complete disk interface is imported, not recertified
by this finite computation. The bounded exclusion is conditional on
that interface and implies no new RH conclusion or priority claim.

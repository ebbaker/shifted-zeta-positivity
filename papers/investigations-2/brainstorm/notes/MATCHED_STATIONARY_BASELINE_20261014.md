# Complete-source baseline for the matched 01/18 experiment

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: `gpt-6-astra` (Codex), reasoning effort **ultra**.
Internal research and LLM checks are not independent specialist validation.

## Fixed experiment and result

The shared test uses the genuine complete theta source, at the exact time
\(t=1/20\), on two cells chosen before comparing the 01 and 18 estimates:

| Target | Initial real cell | Certified stationary point, approximate | Conditional Laguerre value, approximate |
| --- | --- | --- | --- |
| \(H_x=0\), \(-HH_{xx}>0\) | [204.087, 204.089] | 204.087864 | \(1.15071737608519\cdot10^{-64}\) |
| \(H_{xx}=0\), \(-H_xH_{xxx}>0\) | [205.556, 205.558] | 205.557067 | \(2.08000102453508\cdot10^{-65}\) |

Both stationary roots exist and are unique in their respective cells.
Their exact rational brackets and exact dyadic function enclosures are in
the [record](../numerics/MATCHED_STATIONARY_BASELINE_RECORD_20261014.json).
The respective Laguerre enclosures are
\([1.15071737608519\cdot10^{-64}\pm4.61\cdot10^{-79}]\) and
\([2.08000102453508\cdot10^{-65}\pm5.21\cdot10^{-80}]\), where the
displayed radii include decimal-display rounding. The record's dyadic
endpoints govern the exact certificate.

The original exploratory range 40--100 was rejected before the comparison:
01's retained complete approximation requires \(x-r\ge200\). The selected
cells admit its frozen natural cutoff \(N=4\), with disk radii through one.
This adjustment prevents comparing a valid 18 calculation with an
out-of-domain 01 bound. The cells are above the first zeros, but remain
finite-height tests, outside the inherited asymptotic sector
\(t\log(x/(4\pi))\in[1,3/2]\).

The targets are absolute numerical jet error below \(10^{-40}\), and
absolute numerical Laguerre error below \(10^{-72}\). These are accuracy
targets, not bounds on the function's natural variation across the initial
cells. Refined stationary-root brackets remove that ambiguity. Each
candidate uses at most 256-bit arithmetic and a declared bounded work
budget; elapsed times are local diagnostics, not portable cost theorems.

## Direct integral and every omitted term

Use
\[
\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}},
\quad H_t(x)=\int_0^\infty e^{tu^2}\Phi(u)\cos(xu)\,du.
\]
The [checker](../numerics/check_matched_stationary_baseline.py) integrates
the first eight source terms on \([0,1]\), with 256-bit Arb/ACB balls.
For derivative order \(k\), it inserts \(u^k\cos(xu+k\pi/2)\),
implemented by the appropriate signed sine or cosine. The finite
integrands are entire, so the analytic callbacks used by certified ACB
quadrature are valid. Its returned balls pay the finite quadrature error.

For omitted indices \(n\ge9\), every positive majorant
\(2\pi^2n^4e^{9u+u^2/20-\pi n^2e^{4u}}\) decreases on \([0,1]\).
For all required derivatives \(u^k\le1\) there. Consecutive index
majorants have ratio at most
\[
q_9=(10/9)^4e^{-19\pi}<1.
\]
The complete index payment is therefore
\[
E_\theta=\frac{2\pi^2\,9^4e^{-81\pi}}{1-q_9}.
\]

For \(u\ge1\), the full source satisfies
\(\Phi(u)\le4\pi^2e^{9u-\pi e^{4u}}\): successive positive index
majorants have ratio at most \(16e^{-3\pi e^{4u}}<1/2\). The logarithmic
derivative of \(u^ke^{9u+u^2/20-\pi e^{4u}}\) decreases for \(u\ge1\)
and is at most \(-d_k\), where
\[
d_k=4\pi e^4-9-1/10-k>0\quad(0\le k\le19).
\]
Thus the complete infinite source tail is at most
\[
E_{u,k}=\frac{4\pi^2e^{9+1/20-\pi e^4}}{d_k}.
\]
Each numerical point jet is enlarged by the outward upper endpoint of
\(E_\theta+E_{u,k}\). No truncation of the complete source is unpaid.

## Transport in x and stationary-root isolation

At each rational cell center, the checker computes jets through order 18.
For each needed derivative \(j\le3\), it uses a degree-15 Taylor polynomial
in the real displacement \(h\). Its remainder is bounded by
\[
\frac{2|h|^{16}}{16!}.
\]
To justify the uniform derivative bound, all positive source moments
through order 19 satisfy
\[
\int_0^\infty u^k e^{u^2/20}\Phi(u)\,du
\le\frac{2\pi^2e^{-\pi}}{1-16e^{-3\pi}}+E_{u,19}<2.
\]
On \([0,1]\) this uses \(u^k\le1\) and the decreasing heated
majorants; the preceding infinite-tail estimate handles the rest. All
Taylor coefficients, polynomial evaluations and remainder payments use
outward arithmetic.

For each target, the relevant derivative has opposite signs at the cell
endpoints, and its next derivative excludes zero throughout the cell.
The intermediate value theorem and strict monotonicity give one stationary
root. Forty certified bisections isolate it further. At this root the
stationary term vanishes exactly; the checker evaluates the conditional
product with full enclosures of the remaining jets. Both products are
strictly positive. It also verifies positivity of these conditional
products throughout the initial cells, which is a stronger local sign
check but not an assertion that every point is stationary.

## Reproducibility and scope

Install `python-flint==0.9.0` in a chosen Python environment, then from the
repository root run:

```sh
python3 -B papers/investigations-2/brainstorm/numerics/check_matched_stationary_baseline.py \
  --record /tmp/MATCHED_STATIONARY_BASELINE_RECORD_20261014.json
```

The retained run used Python 3.10.0 and 24,000 integrand callbacks, each
evaluating eight theta summands: 192,000 source-term evaluations in all.
Both cells together took less than one second in the local run. The
checker stops above one million source-term evaluations and fails closed
if a required sign, tail hypothesis or accuracy target is not established.
Runtime fields can differ on replay; exact mathematical enclosures and
hashes can be compared separately. JSON is small and no derived archive
is needed.

This certificate is the direct-source comparator, not a new signed
remainder theorem for 01 or 18. It proves two fixed-time local statements.
It establishes no time interval, predecessor coverage, uniform height
estimate, collision exclusion for all heights, or RH conclusion.

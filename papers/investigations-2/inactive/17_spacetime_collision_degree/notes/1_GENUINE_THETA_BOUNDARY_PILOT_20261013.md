# A paid genuine-theta boundary calibration

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded parent configuration: `gpt-6-astra` (Codex), reasoning effort
**ultra**, inherited by this internal worker. This is an internal analytic
and outward-arithmetic check, not independent mathematical validation.

**Result and gate.** On
\(R=[0,0.05]\times[8,12]\), both a complete boundary certificate and a
single interior value-and-slope box exclude joint zeros of genuine theta
heat. The boundary winding is zero. The same evaluator needs four boundary
pair integrals and three heat-weight preparations, versus one integral and
one preparation for the interior box. This easy calibration establishes no
cost advantage; do not expand it into a winding campaign on this evidence.

The rectangle was fixed from the existing
[full-theta low-height stationary certificate](../../../../quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/numerics/THETA_STATIONARY_LOW_HEIGHT_RECORD_20261010.json).
That record already establishes \(H_x<0\). Its 80 spatial cells also
certify stronger information about \(H_{xx},H_{xxx}\) and a stationary
branch, so comparing its cell count directly with a four-edge collision
test would inflate the apparent gain. Here both competitors use the same
new two-coordinate enclosure and the same precision, source, cutoff and
tails. This is a low-height calibration, not a difficult-cell benchmark.

## Local degree sanity check, including higher multiplicity

The analytic argument in the
[initial program](INITIAL_RESEARCH_PROGRAM_20261013.md) survives review.
For \(H_t=-H_{xx}\) and spatial multiplicity \(m\), parabolic scaling
gives \((P_m,\partial_yP_m)\). The two target normalizations have joint
determinant \(c^{-2}r^{-(2m-1)}>0\), even when the leading coefficient
\(c\) is negative. The recurrence eliminates every joint zero except
the origin. Uniform convergence on a fixed anisotropic boundary then
preserves both its nonvanishing and its degree. Those scaled boundaries
cover a punctured neighborhood, so the isolation assertion is justified.

On the positive-time edge, the \(\lceil m/2\rceil\) positive-slope
Hermite roots each cross the positive imaginary ray negatively. The
negative-time edge contributes one positive crossing when \(m\) is odd,
and none otherwise. Thus the index remains \(-\lfloor m/2\rfloor\),
including odd multiplicities. In particular,
\(P_3=y^3-6sy\), \(P_{3,y}=3y^2-6s\) has index \(-1\), not zero.
The retained rational Bernstein checker was rerun unchanged for
\(m=2,\ldots,10\); its windings are
\(-1,-1,-2,-2,-3,-3,-4,-4,-5\), with reversed signs under reversed
orientation. This finite replay supports, but does not replace, the
all-multiplicity argument.

## Physical source and complete payments

We directly enclose
\[
H(t,x)=\int_0^\infty e^{tu^2}\Phi(u)\cos(xu)\,du,
\quad
H_x(t,x)=-\int_0^\infty u e^{tu^2}\Phi(u)\sin(xu)\,du,
\]
where
\[
\Phi(u)=\sum_{n\ge1}
(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}}.
\]
The implementation imports the retained, hash-checked 60-digit outward
Decimal arithmetic, including its corrected integer-power implementation.
Pi and sine/cosine use explicit Taylor bounds; exponentials use enclosing
neighbors of correctly rounded Decimal values. No binary floating-point
value determines a sign. Wall-clock timings are ordinary floats and play
no proof role.

The integration interval \([0,1]\) is divided into 512 exact dyadic
cells. Each entire integrand cell is enclosed before multiplication by
its exact width and summation. Therefore quadrature and parameter
variation are paid by interval integration, not an empirical comparison
of quadrature resolutions. Time intervals enter the positive factor
\(e^{tu^2}\). A rigorously rotated center phase is padded by
\(\sup|xu-\text{center phase}|\), using the global derivative bound
one for sine and cosine. Every point between parameter endpoints is
covered. The output widths combine quadrature, parameter variation and
rounding; they are not presented as pure quadrature errors.

For each cell the terms \(n=1,2,3\) are retained explicitly. For
\(k=2,4\) and \(u\ge0\),
\[
\sum_{n\ge4}n^k e^{-\pi n^2e^{4u}}
\le \frac{4^k e^{-16\pi e^{4u}}}
 {1-(5/4)^k e^{-9\pi e^{4u}}}.
\]
Both denominators are checked positive. Each omitted density summand is
positive because \(2\pi n^2e^{4u}>3\), so adding the interval from zero
to the displayed absolute majorant encloses the actual missing density.
For \(j=0,1\), integrated \(n\ge4\) payments are respectively below
\(4.803\cdot10^{-21}\) and \(2.906\cdot10^{-23}\), uniformly in the
declared time box.

For the infinite integration tail, \(n^4\le16^{n-1}\),
\(n^2-1\ge3(n-1)\) and \(16e^{-3\pi}<1/2\) give
\[
\Phi(u)\le4\pi^2e^{9u-\pi e^{4u}}
\le C e^{-8\pi u^2},\qquad C=4\pi^2e^{-\pi},
\]
using \(e^{4u}\ge1+4u+8u^2\) and \(4\pi>9\).
Put \(a=8\pi-0.05\), \(F=Ce^{-a}\). The absolute derivative tails
at cutoff one are bounded by
\[
(T_0,T_1,T_2,T_3)
=F\left(\frac1{2a},\frac1{2a},
\frac1{2a}+\frac1{4a^2},
\frac1{2a}+\frac1{2a^2}\right).
\]
The \(j=0,2\) bounds use the Gaussian Mills estimate and integration
by parts; \(j=1,3\) are exact Gaussian-moment evaluations. All four
payments are below \(4.522\cdot10^{-13}\). The complete \(j=2,3\)
absolute derivative bounds are below \(0.00075810\) and
\(0.00012715\). These can also bound
\(\partial_t(H,H_x)=(-H_{xx},-H_{xxx})\); the present certificate
already covers whole segments directly and needs no additional
derivative interpolation assumption.

There is no height-dependent arithmetic cutoff, complex carrier, or
normalization reconstruction in this pilot. The fixed integration cutoff
\(u=1\) has the infinite tail paid above. Hence no natural-cutoff
transition is silently omitted.

## Boundary certificate and like-for-like comparison

The boundary follows
\((0,8)\to(0.05,8)\to(0.05,12)\to(0,12)\to(0,8)\),
counterclockwise in coordinate order \((t,x)\). Every complete side
has \(H_x<0\). Therefore its image lies in the open lower half-plane
and the straight homotopy to \(-i\) avoids zero. This proves winding
zero without numerical angle unwrapping or sampled polygon assumptions.
The local-degree theorem then excludes collisions throughout the interior.

The interior comparator directly encloses the same physical pair on all
of \(R\); it obtains, with endpoints rounded outward for display,
\[
H\in[0.0223323,0.0470782],\qquad
H_x\in[-0.00504687,-0.00253515].
\]
In fact either coordinate alone suffices here. There is no unresolved
joint-observation problem hidden by the comparison.

| Quantity | Boundary certificate | Interior certificate |
| --- | ---: | ---: |
| Complete pair integrals | 4 | 1 |
| Distinct heat-weight preparations | 3 | 1 |
| Integration cells per pair | 512 | 512 |
| Decimal precision | 60 | 60 |
| Certified slope-based norm margin | \(>0.00253558\) | \(>0.00253515\) |
| Result | Winding zero | Pair nonzero everywhere |

The shared preparation evaluates 512 density intervals with 1536 explicit
theta terms. The
[small execution record](../numerics/GENUINE_THETA_BOUNDARY_PILOT_RECORD_20261013.json)
contains every side enclosure, derivative and tail payments, ordered paths,
input hashes, runtime environment and measured timings. Timings are
machine dependent; the evaluation counts give the more useful comparison.

## Decision

This completes a first genuine-source certificate and exposes the intended
performance gate: topology alone does not make an easy source enclosure
cheaper. Retain direction 17 as a possible consumer of a new uniform
boundary homotopy or a difficult rectangle where interior coverage fails.
The present result supplies neither, so the bounded pilot stops here.
It does not compare every optimized winding/interior implementation and
cannot rule out savings elsewhere. It establishes no new global sign,
unbounded-height coverage, positive-time threshold, or RH consequence.

Reproduce from the repository root:

```sh
python3 papers/investigations-2/inactive/17_spacetime_collision_degree/numerics/check_collision_degree.py
python3 papers/investigations-2/inactive/17_spacetime_collision_degree/numerics/check_genuine_theta_boundary_pilot.py --record /tmp/genuine-theta-boundary-pilot.json
```

All generated retained files are small. No large archive or manuscript
snapshot was produced.

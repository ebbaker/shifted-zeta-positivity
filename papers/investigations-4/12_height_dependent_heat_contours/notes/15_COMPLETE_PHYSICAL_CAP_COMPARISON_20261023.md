# A bounded complete-cap enclosure on the original theta box

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual model **gpt-6-astra (Codex)**, reasoning effort **ultra**. **Status: rigorous finite first-jet floor and complete physical-face enclosures acquired; no useful positive cap lower bound and no deformation advantage demonstrated.** Separate same-model code/proof reviews accepted this bounded scope; no specialist review or global conclusion.

This is the single bounded continuation of [Note 13's actual-theta certificate](13_COMPLETE_THETA_WALL_AND_COEFFICIENT_CERTIFICATE_20261023.md). It retains the exact geometry and observable of [Note 02](02_FINITE_BAND_GEOMETRY_AND_COMPARISON_CONTRACT_20261023.md), all physical faces from [Note 03](03_COMPLETE_COUPLED_EXPRESSION_AND_COMPARISON_20261023.md), and the complete source core. Read the [result index](../../../../result-summaries/README.md), [avoid index](../../../../avoid/README.md), especially [matched complete estimates](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) and [numerical work tied to a decisive question](../../../../avoid/10_numerics_ahead_of_the_question.md). The experiment stops at its declared budget; it does not change the rectangle, delete root neighborhoods, or launch a refinement sweep.

## 1. Domain and independently acquired regularity

Keep \(\Omega=[26,46]+i[-2,2]\), \(D=[-10^{-4},10^{-4}]+i[-10^{-4},10^{-4}]\), and \(\epsilon=Y=10^{-4}\). The first-jet acquisition covers the whole closed spatial rectangle with 31 disjoint-interior closed rectangles, uses 61 tested cells, and proves uniformly on \(D\)

\[
E=|H|^2+|H_z|^2>1.1178\cdot10^{-13}.
\tag{1}
\]

It removes no disks. Its area and containment tests are exact rational checks, and its bounds use the complete canonical source with the paid errors of Note 13. The cap checker replays the 31 accepted cells and independently verifies a weaker floor \(E>10^{-13}\). Thus every denominator on every physical face is regular, and the whole box contains no joint event \(H=H_z=0\).

## 2. Every face of the same physical chain

Write \(H_j=\partial_z^jH\) and

\[
L=H_1^2-H_0H_2,\quad N=H_2^2-H_1H_3,\quad M=H_1H_2-H_0H_3.
\]

The complete densities are

\[
f=\frac{\Re(L\overline N)}{2\pi^2E^2},\quad
p=\frac{\Im(L\overline N)}{2\pi^2E^2},\quad
r=\frac{\Re(M\overline N)}{2\pi^2E^2},\quad
s=\frac{\Im(M\overline N)}{2\pi^2E^2}.
\tag{2}
\]

The forward cap is \(I_t=\int_{-Y}^{Y}\int_\Omega f(t+i\sigma,z)\,dA\,d\sigma\). The other-face sum is exactly

\[
\begin{aligned}
S_\epsilon={}&\int_{-\epsilon}^0\int_\Omega
[p(t+iY,z)-p(t-iY,z)]\,dA\,dt\\
&+\int_{-\epsilon}^0\int_{-Y}^Y\int_{-2}^2
[r(t+i\sigma,46+iy)-r(t+i\sigma,26+iy)]\,dy\,d\sigma\,dt\\
&+\int_{-\epsilon}^0\int_{-Y}^Y\int_{26}^{46}
[s(t+i\sigma,x+2i)-s(t+i\sigma,x-2i)]\,dx\,d\sigma\,dt.
\end{aligned}
\tag{3}
\]

Set \(B_\epsilon=I_{-\epsilon}-S_\epsilon\). The acquired full-volume floor makes the joint-event count zero, hence the exact degree identity is

\[
I_0=B_\epsilon.
\tag{4}
\]

Both estimators receive this information. Equality (4) is not a numerical value for either side.

## 3. Bounded range quadrature and error payments

The common spatial mesh starts from the 31 certified rectangles and refines the largest current interval-radius contribution until exactly 512 leaves are present. This takes 993 parent-and-leaf evaluations. Splits and cell areas are exact rational numbers. Floating values select refinement order only; all range bounds, denominators, sums and reported results are Arb balls.

On each spatial cell, the cap oracle encloses all \(\sigma\in[-Y,Y]\) at once. The left cap does likewise. The paired \(\sigma\)-face expression encloses all \(t\in[-\epsilon,0]\) at once. Multiplication by the exact cell volume gives a rigorous integral interval. Thus there is no unpaid discretization remainder: the method is interval range integration rather than an unvalidated point quadrature. All field errors through order three are the complete source errors in Note 13.

The \(x\)- and \(y\)-side integrals each use 32 exact line segments and the full \((t,\sigma)\) rectangle, for 128 side jet-range calls in total. Every physical face in (3) is present, including its spatial complement. No root chart is used.

For the close \(\sigma\) faces, the implementation preserves cancellation. The finite heat-polynomial difference has coefficients

\[
\frac{(-1)^k}{k!}\bigl[(t+iY)^k-(t-iY)^k\bigr]
=\frac{(-1)^k2iY}{k!}
\sum_{j=0}^{k-1}(t+iY)^j(t-iY)^{k-1-j},
\tag{5}
\]

so every nonzero term retains the factor \(2iY\). The midpoint cell remainder uses these difference coefficients, and the two complete source errors are added. If \(\delta H_j=H_j(t+iY)-H_j(t-iY)\), then \(\delta E,\delta L,\delta N\) are expanded algebraically from the reference jets and \(\delta H_j\). Writing \(n=\Im(L\overline N)\), this gives

\[
p_+-p_-=
\frac{\delta n\,E_-^2-n_-\,\delta(E^2)}
{2\pi^2E_+^2E_-^2}.
\tag{6}
\]

This retains the close-face subtraction before taking absolute interval ranges. It uses no derivatives beyond \(H_3\). Its validity does not assert that the resulting interval is sharp.

Positive denominator inversion uses the independently acquired floor: if \(E\in[\ell,u]\), replace the lower endpoint by \(\max(\ell,E_{\min})\), enclose the reciprocal endpoints, and multiply by that reciprocal enclosure. This avoids a wide Arb midpoint-radius representation accidentally including zero before inversion. The replay checks every endpoint consistency condition.

## 4. Recorded result and matched comparison

The full outward records are in the associated cap certificate. Conservative displayed balls are

| Complete quantity | Enclosure |
| --- | --- |
| \(I_0\) | \(2.0247388041\cdot10^{-5}\ \pm1.42\cdot10^{-4}\) |
| \(I_{-\epsilon}\) | \(2.0247509554\cdot10^{-5}\ \pm1.42\cdot10^{-4}\) |
| \(S_\sigma\) | \(7.2551826887\cdot10^{-11}\ \pm2.04\cdot10^{-7}\) |
| \(S_x\) | \(-3.8997037114\cdot10^{-12}\ \pm3.40\cdot10^{-12}\) |
| \(S_y\) | \(8.3863509646\cdot10^{-12}\ \pm6.92\cdot10^{-10}\) |
| \(S_\epsilon\) | \(7.7038474140\cdot10^{-11}\ \pm2.05\cdot10^{-7}\) |
| \(B_\epsilon\) | \(2.0247432516\cdot10^{-5}\ \pm1.42\cdot10^{-4}\) |

The raw direct interval width is approximately 0.000283522; the raw deformed width is approximately 0.000283934. **Both lower endpoints are negative.** The displayed centers are not claimed as accurate values: their interval radii govern the conclusion. The entire bounded pilot took about 3.9 seconds in the recorded environment, including the repeated first-jet cover; timings are implementation-specific.

On the common mesh the direct method uses one complete four-jet range per tested spatial cell. The deformed method uses a left-cap range, a \(\sigma\)-face reference range, a coupled heat-polynomial difference range, and the 128 side calls. Source setup and regularity data are shared. The direct raw interval is slightly narrower with fewer density acquisitions. This is a comparison of the stated bounded range-quadrature implementation, not every possible direct or deformed algorithm.

The error is dominated by spatial range integration of the caps. Complete source truncation errors are already below \(6\cdot10^{-27}\), and the additional face sum is much smaller than the cap interval uncertainty. Increasing source precision, changing the zero description, or merely rerouting the time path would not address this observed bottleneck. A higher-order correlated spatial integration method could be tested later on this same observable, but no such further run is performed here.

The finite source and regularity gates have been paid, and every original physical face has an actual enclosure. The strict original acceptance test remains unmet: there is no useful positive complete lower bound or demonstrated cost advantage. This scoped result does not exclude a favorable contour with genuinely better source constants, and it supplies no height-uniform conclusion.


Reproducible artifacts: [cap checker](../numerics/08_enclose_complete_physical_cap_20261023.py), [complete-face receipt](../numerics/08_COMPLETE_PHYSICAL_CAP_COMPARISON_20261023.json), [first-jet cover](../numerics/08_COMPLETE_FIRST_JET_FLOOR_20261023.json), and [review](../reviews/13_COMPLETE_PHYSICAL_CAP_COMPARISON_REVIEW_20261023.md).

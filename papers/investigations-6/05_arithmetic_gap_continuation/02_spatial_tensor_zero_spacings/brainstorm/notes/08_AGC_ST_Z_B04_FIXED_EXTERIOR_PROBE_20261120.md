# Can a fixed exterior observation bound both moving positions?

20 November 2026, America/New_York. Prepared for Edward Baker with OpenAI Codex LLM assistance. Conceptual assignment AGC-ST-Z-B04 r1, dispatched gpt-6.2-astra, effort ultra. No separate serving-backend attestation.

Keep the [B03](07_AGC_ST_Z_B03_CANONICAL_POSITION_TEST_20261120.md) theta field, anchors, coarse boxes and \(T=10^{-4}\). The [cubic transport](06_AGC_ST_Z_B02_ODD_CUBIC_TRANSPORT_20261120.md) suggests testing a different source message on exactly these same targets. Use time-zero slopes for the initial velocity and, after the anchor, a logarithmic cubic trace at one *fixed* off-root height \(X=87/2\). Use the [prior exterior sign bracket](../../notes/06_AGC_ST_E06_FINITE_GAP_CURVATURE_20261120.md) at 49.9 and 50.1. Sharp whole-slab or final ordinates and post-anchor jets sampled on moving target tubes are withheld from this predictor.

**Clear the region to the left.** At time zero acquire the exact integer \(N_\zeta(13)\). In the normalization \(H(0,z)=\xi((1+iz)/2)/8\), the condition \(0<\Re z\le26\) means \(0<\Im s\le13\). FLINT's official documentation defines its count for all zeta zeros at these positive heights, including multiplicity. The computation must give zero. Positive theta density makes \(H(t,iy)>0\) for real \(y\). The [height-26 wall](../../../../../investigations-4/12_height_dependent_heat_contours/notes/13_COMPLETE_THETA_WALL_AND_COEFFICIENT_CERTIFICATE_20261023.md) over \(-2\le\Im z\le2\) and the [physical strip](../../references/README.md#source-check-for-the-spatial-forcing-comparison) \(|\Im z|\le1\) clear the remaining walls of the rectangle \([0,26]+i[-2,2]\) throughout the slab. Its count remains zero. The original HDC rectangle now places every remaining representative of an opposite pair at \(q=\Re\rho>46\), upon removing the marked orbits \(\{\pm a,\pm b\}\). This is a finite, verifiable count of the left exterior. [FLINT, Gram points and counting zeros, definition of \(N(t)\)](https://flintlib.org/doc/acb_dirichlet/index.html#gram-points-and-counting-zeros) · [Python-FLINT, arb.zeta_nzeros](https://python-flint.readthedocs.io/en/stable/arb.html#flint.arb.zeta_nzeros).

For \(\rho=q+iy\) with \(q>46\) and \(|y|\le1\), put
\[
K_\rho(x)=\Re\big[(\rho-x)^{-3}-(\rho+x)^{-3}\big],
\qquad S(x)=\sum_{\mathrm{higher\ opposite\ orbits}} K_\rho(x).
\]
Use one positive-real-part representative per opposite orbit, with multiplicity. Off-axis conjugate orbits both enter. For \(0<x\le X\) all real distances \(q\pm x\) exceed 2.5. The derivative of \(f_y(u)=\Re(u+iy)^{-3}\) is \(-3\Re(u+iy)^{-4}<0\) on this interval, since \(u>(1+\sqrt2)|y|\). The difference defining \(K\) is positive. Its derivative is positive as well, since \(-f_y'(q-x)-f_y'(q+x)>0\). The complete product pays the convergent cubic sums. The bracketed real occurrence \(d\in(49.9,50.1)\) gives \(K_d(x)\le S(x)\le S(X)\).

At the fixed height, enclose the complete source \(F,F_z,F_{zz},F_{zzz}\) on the full time slab, with a strict floor for \(|F|\). The acquired trace is
\[
 S(X)=-\tfrac12\partial_z^3\log F(t,X)
       +\sum_{r\in\{a,-a,b,-b\}}(X-r)^{-3}.
\]
The correction needs only the marked *boxes*. This fixed-point trace prices the contribution of every higher occurrence in one upper bound. At either marked \(x\in\{a,b\}\) the exact acceleration is
\[
 x''/8=S(x)-\sum_{r\in\{a,-a,b,-b\},\ r\ne x}(x-r)^{-3}.
\]
The finite sum includes the opposite of the target, its partner and the partner's opposite. Substituting the geometric lower bracket and fixed-height upper trace gives two-sided bounds. The center uses the mean of the two accelerations, with exact cancellation of mutual cubes before bounding when practical. Taking \(X=43.5\) leaves strict clearance above \(b\) and preserves monotonicity on the entire path to \(X\).

First use only coarse \(a,b\) boxes in both equations. Integrate these acceleration intervals from the independent initial positions and velocities to bound the paths at every intermediate \(0\le\tau\le T\). One repeat may substitute those generated tubes into the deflation correction and finite sums without a new probe height or a root measurement. Pay source truncation and rounding as in [B03](07_AGC_ST_Z_B03_CANONICAL_POSITION_TEST_20261120.md), then freeze the projections. Test the explicit lower gates \(a''>10^{-3},\ b''>10^{-2}\), strict positive excess over both initial tangents, negative final displacements and widths below \(10^{-7}\) in both physical positions. Compare against the equally informed source-root solver and the [moving-jet method](07_AGC_ST_Z_B03_CANONICAL_POSITION_TEST_20261120.md); also state exactly which post-anchor observations each predictor reads. A scalar upper trace with an ineffective width or failed gate remains a documented result for this class.

This finite geometric mechanism uses the low count, strip, exterior sign bracket and a complete normalized arithmetic trace. A counted double lacks the two separated boxes. The [B01 control screen](05_AGC_ST_Z_B01_ORIENTED_ANCHOR_20261120.md) identifies the canonical source premise lost by each established collision family. In particular a new Euler factor can preserve the initial real marks while adding nonreal exterior zeros and changing the wall trace or strip. Positivity of a cubic contribution is asserted only under the stated distance/strip condition. [Results and collision classes](../../../../../../result-summaries/12_collision_controls_and_screening.md) · [Pattern 07](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

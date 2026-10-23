# Independent mathematical and replay review of the finite complete-source wall certificate

**Prepared for:** Edward Baker. **Date:** 23 October 2026. **Reviewer:** gpt-6-astra (Codex), reasoning effort **ultra**. Substantial LLM assistance. This is a separate derivation and execution by another agent using the same model, not external or cross-model refereeing.

**Disposition:** accepted within the precise finite scope below. The reviewed source core acquires the complete canonical theta function on the prescribed block; it does not assume any individual root, internal gap, discriminant floor, RH, or simplicity. The wall/coefficient replay passed **109 assertions** in an independent run. Separate source quadrature checks passed **46 assertions**. These are different checks and not a claim of formal proof verification.

## 1. Complete-source enclosure

The exact normalization is
\[
 H_0(z)=\frac18\xi\!\left(\frac12+\frac{iz}{2}\right).
\]
The code obtains its first 96 Taylor coefficients at the real center 36 using Arb's complex series gamma and zeta operations. Projecting coefficient balls to their real parts is justified by the exact real-type symmetry, and the imaginary balls are checked to contain zero.

Positivity of the complete source gives the Cauchy majorant \(H_0(24i)\) on the circle \(|z-36|=24\). On the radius-12 collar the omitted spatial tail is bounded by
\[
 E_{\rm sp}=2H_0(24i)2^{-96}<3.277\cdot10^{-29}.
\]
Cauchy's derivative estimate on radius 11 pays the full factor \(j!E_{\rm sp}\); the distance to the collar is one. No source mode truncation is used in this acquisition.

The exact target time square is
\[
 D=[-10^{-4},10^{-4}]+i[-10^{-4},10^{-4}].
\]
The source estimates deliberately hold on the larger disk \(|\tau|\le T=1/5000\), which contains this square including its outward-rounded interval representation. With \(Y=2\), the complete moments are bounded by
\[
 M_j\le e^T H_0(2i)+\frac{C_\Phi}{4}
   e^{B_j^2/(2\pi)}\frac{e^{-x}}x,
 \quad C_\Phi=\frac{2\pi^2}{1-16e^{-3\pi}},\quad
 B_j=\frac{T}{e^2}+\frac{11+j}{2e},\quad
 x=\frac\pi2 e^4.
\]
On \([0,1]\), use \(u^j\le1\) and the **cosh** bound on both sine and cosine: the source integral is at most \(e^T H_0(2i)\). On \([1,\infty)\), use \(u^j\le e^{ju}\), \(\Phi(u)\le C_\Phi e^{9u-\pi e^{4u}}\), and the maxima of \(u^2e^{-2u}\) and \(ue^{-2u}\) there. Completing the square in \(e^{2u}\) and integrating the remaining exponential tail yields the stated bound. The constants and the factors of four check.

The retained heat polynomial is
\[
 G_\tau(z)=\sum_{k=0}^{5}\frac{(-\tau)^k}{k!}
                 P_{95}^{(2k)}(z).
\]
Its derivative error is bounded by
\[
 |H_\tau^{(j)}-G_\tau^{(j)}|
 \le E_{\rm sp}\sum_{k=0}^{5}\frac{T^k(j+2k)!}{k!}
       +\frac{T^6M_{12+j}}{6!},\qquad 0\le j\le3.
\]
All four bounds are less than \(6\cdot10^{-27}\). The heat signs, derivative factorials and time remainder are correct. Cell reexpansion encloses the finite polynomial by its midpoint derivatives plus a degree-six Taylor remainder, whose higher derivative is bounded on the convex radius-11 disk. The difference oracle cancels the \(k=0\) term **before** interval evaluation and encloses \(H_\tau-H_0\), rather than subtracting two independently wide balls.

The physical-cell oracle is explicitly restricted to the prescribed physical subset and is not used as an analytic integration callback. The contour integrator receives the meromorphic quotient formed from the entire finite polynomial; it is holomorphic near the certified wall, and the integrator checks its required complex neighborhoods. This distinction is essential and is correctly respected.

An independent direct source integral with \(n\le4\), \(0\le u\le1\), pays all omitted modes by a bound below \(1.15\cdot10^{-32}\) and the large-source tail by a bound below \(5.64\cdot10^{-72}\). Four actual complex space/time evaluations, including a corner of the original time square, overlap the complete heat oracle. These spot checks additionally verify the canonical normalization; they supplement the uniform analytic argument rather than replacing it.

## 2. Whole-wall count and coefficient transport

The counterclockwise rectangle is \([26,46]+i[-2,2]\). Its radius from 36 is at most \(\sqrt{104}<11\). The adaptive cover has **16 accepted segments**, obtained in **28 cell calls**, and checks adjacency and closure. The uniform full-\(D\) wall floor is greater than \(4.94\cdot10^{-7}\); the largest certified relative difference \(\eta=|H_\tau-H_0|/|H_0|\) is less than \(0.000382\). Thus Rouché's theorem transfers the entire interior multiplicity count throughout \(D\). This concerns all complex roots in the rectangle, not a chosen real subpopulation.

At the anchor \(\tau=0\), the integrator encloses
\[
 p_k(0)=\frac{1}{2\pi i}\oint (z-36)^k\frac{H_0'}{H_0}\,dz,
 \qquad k=0,1,2.
\]
The polynomial-to-source quotient correction is correctly signed and bounded by
\[
 \left|\frac{H_0'}{H_0}-\frac{G_0'}{G_0}\right|
 \le \frac{e_1}{m_H}
      +\frac{(|H_0'|+e_1)e_0}{m_H(m_H-e_0)},
 \qquad e_0=e_1=E_{\rm sp}.
\]
Both source and polynomial wall denominators are explicitly positive. The count integral is enclosed within \(2\pm2.62\cdot10^{-12}\) in real part, with imaginary part containing zero. Since the exact complete-source integral is an integer by the argument principle, the asserted unique integer two follows. This does not require rounding a numerical guess about a root population.

The principal relative logarithm \(\ell=\log(H_\tau/H_0)\) exists continuously on the full closed wall because \(\eta<1\), and \(|\ell|\le-\log(1-\eta)\). Integration by parts on that closed wall gives
\[
 p_k(\tau)-p_k(0)
 =-\frac{k}{2\pi i}\oint (z-36)^{k-1}\ell\,dz.
\]
The code's segmentwise length/radius/log budgets therefore give valid uniform errors, approximately \(0.001772\) for \(p_1\) and \(0.025736\) for \(p_2\). No branch choice for individual roots is involved.

For the complete monic quadratic the discriminant is exactly
\[
 \Delta=2p_2-p_1^2.
\]
The replay obtains
\[
 \Delta(D)\subset
 [189.74040392437645\pm0.0575]+i[\pm0.0575],
\]
so it is nonzero throughout the original complex square. On every real-time slice, exact conjugation symmetry makes the quadratic coefficients real; the positive discriminant then shows that both complete roots are real and distinct. This inference uses the acquired complete count and discriminant, not an imported gap assumption.

At \(t=10^{-4}\), \(a=4t\), the complete two-root Laplacian has nonzero eigenvalue \(2/\Delta\); consequently
\[
 q=\frac{8t}{\Delta+8t}
 \in [4.216269619661262\cdot10^{-6}\pm1.28\cdot10^{-9}]
 <10^{-5}<\tfrac12.
\]
The factor eight and all filter normalizations check.

## 3. Direct comparator and exact scope

The direct terminal comparator uses the same source core, wall, contour integrator, tolerance and source quotient correction. Its eight additional contour integrals give a substantially tighter terminal coefficient/filter enclosure than the full-complex-time continuation enclosure. A separate four-point sign calculation gives two distinct real sign changes in \((28,29)\) and \((42,43)\) uniformly on the real time interval; combined with the shared complete count, it also proves simplicity and a gap greater than 13. These point intervals are outputs used only by the comparator, never inputs to the coefficient argument. Both comparator corrections and the filter normalization have been checked.

This is a genuine acquisition of previously unpaid **finite canonical source inputs** on the frozen block and original complex time square. It is not a new global simplicity theorem or a practical superiority claim. The original cap/complement integrals, a complete lower-bound comparison, and any height-uniform microscopic estimate remain outside this replay.

**Replay artifacts:** [source core](../numerics/hdc13_theta_core.py),
[source checks](../numerics/07_check_complete_theta_source_20261023.py) and
[source record](../numerics/07_COMPLETE_THETA_SOURCE_CHECKS_20261023.json),
[wall/coefficient checker](../numerics/07_certify_complete_theta_wall_20261023.py)
and [certificate](../numerics/07_COMPLETE_THETA_WALL_CERTIFICATE_20261023.json).
The separate review run remained outside the repository. Installed sibling
imports and core hashes are portable; the saved receipts were regenerated
from the installed scripts.

The parent additionally reviewed the complete first-jet cover in Note 13,
Section 6: source cell enclosures are valid on every requested spatial
rectangle and all of D; squared magnitude lower bounds add correctly;
recursive splitting and exact area/disjointness checks cover the full box.
The acquired squared-norm floor exceeds 1.1178e-13. This is an independent
regularity acquisition, with no cap quadrature or global conclusion.

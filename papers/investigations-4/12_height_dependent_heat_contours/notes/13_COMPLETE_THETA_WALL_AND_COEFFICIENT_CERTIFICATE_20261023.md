# A complete theta wall and coefficient certificate in the frozen finite box

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual model **gpt-6-astra (Codex)**, reasoning effort **ultra**. **Status: interval-certified complete canonical wall, population count and prepared discriminant on the original finite complex-time box.** Separate same-model agents reviewed the source oracle and coefficient certificate; no specialist review or global simplicity claim.

This supplies actual source data for the finite program. On the prescribed spatial rectangle and the entire original complex-time square, the complete unchanged theta field has a nonzero spatial wall, exactly two interior zeros counted with multiplicity, and a prepared discriminant with positive real part. The coefficient proof uses no supplied zero locations or root disks. Its separate direct comparator is stronger for the terminal numerical filter, so this experiment establishes a finite source-acquisition milestone, not a computational advantage for continuation.

Read the [result index](../../../../result-summaries/README.md), [avoid index](../../../../avoid/README.md), [finite specification](02_FINITE_BAND_GEOMETRY_AND_COMPARISON_CONTRACT_20261023.md), [complete-expression contract](03_COMPLETE_COUPLED_EXPRESSION_AND_COMPARISON_20261023.md), [source error note](07_COMPLETE_SOURCE_FORCE_AND_FILTER_RESIDUAL_20261023.md), and [collision-control register](../../../../result-summaries/12_collision_controls_and_screening.md). The relevant scope rules are [finite milestones versus reformulations](../../../../avoid/01_restating_the_target.md), [equally informed complete comparisons](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), and [certifying already-known behavior](../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md). This low finite band is a calibration and source-interface test; it supplies no high-height mechanism.

## 1. Frozen field, domain and numerical result

The field remains exactly

\[
H(\tau,z)=\int_0^\infty e^{\tau u^2}\Phi(u)\cos(zu)\,du,\qquad
\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}}.
\tag{1}
\]

Use the original parameters

\[
\Omega=[26,46]+i[-2,2],\qquad
D=[-10^{-4},10^{-4}]+i[-10^{-4},10^{-4}].
\tag{2}
\]

The [replay](../numerics/07_certify_complete_theta_wall_20261023.py) and [small certificate](../numerics/07_COMPLETE_THETA_WALL_CERTIFICATE_20261023.json) establish the following conservative outward summaries:

| Quantity | Certified result |
| --- | --- |
| Spatial-wall cover, uniform on all of \(D\) | 16 closed segments, 28 tested cells |
| Complete wall floor | \(\inf_{D\times\partial\Omega}|H|>4.94\cdot10^{-7}\) |
| Largest complete relative time change on an accepted wall cell | less than \(3.82\cdot10^{-4}\) |
| Complete interior count | exactly 2, including multiplicities, for every \(\tau\in D\) |
| Anchor centered power sum \(p_1(0)\) | \(-1.6864704389875024\), error less than \(7.4\cdot10^{-12}\) in each component |
| Anchor centered power sum \(p_2(0)\) | \(96.29229323297757\), error less than \(4.1\cdot10^{-11}\) in each component |
| Uniform time-continuation error in \(p_1\) | less than 0.001772 |
| Uniform time-continuation error in \(p_2\) | less than 0.025736 |
| Prepared discriminant throughout \(D\) | \(189.68<\Re\Delta<189.80\), \(|\Im\Delta|<0.058\) |
| Complete two-root filter at real \(t=10^{-4}\) | \(4.2149\cdot10^{-6}<q<4.2176\cdot10^{-6}\) |

Full outward balls, precision, source costs, script hashes and timing are in the certificate. Decimal summaries in this table are deliberately weaker than the recorded balls. The two interior roots are distinct throughout \(D\). For every real \(t\in[-10^{-4},10^{-4}]\), real-type symmetry makes the prepared coefficients real; the positive discriminant therefore makes both roots real and simple. This conclusion concerns this complete finite population only.

## 2. A complete-source oracle, without an assumed zero

The available runtime is python-flint 0.9.0, used at 192-bit precision. Existing repository infrastructure already evaluates

\[
H_0(z)=\frac18\xi\!\left(\frac12+\frac{iz}{2}\right)
\tag{3}
\]

by the exact gamma/zeta identity in Arb. In particular, `rhe_actual_theta_core.py` in investigation 4/09 supplied the verified architecture: analytic Taylor coefficients from `acb_series`, and positive-source Cauchy bounds. The present [source core](../numerics/hdc13_theta_core.py) uses neither the older core's supplied root balls nor any zero data.

Expand \(H_0\) around 36 through degree 95. Since \(\Phi>0\),
\(|H_0(36+w)|\le H_0(24i)\) for \(|w|\le24\). The degree-95 Taylor polynomial \(P_{95}\) consequently has the uniform collar remainder

\[
\sup_{|z-36|\le12}|H_0(z)-P_{95}(z)|
\le E_{\rm sp}:=2H_0(24i)2^{-96}.
\tag{4}
\]

Every point of the physical disk \(|z-36|\le11\) has a radius-one Cauchy disk in that collar, so the \(j\)-th derivative error is at most \(j!E_{\rm sp}\). The actual rectangle lies strictly inside this physical disk.

For the time expansion use six terms,

\[
G_\tau(z)=\sum_{k=0}^{5}\frac{(-\tau)^k}{k!}
 P_{95}^{(2k)}(z).
\tag{5}
\]

The source errors are paid on the slightly larger disk \(|\tau|\le T_*=1/5000\), which strictly contains \(D\) and absorbs outward rounding of the interval radii. Taylor's integral remainder for \(e^{\tau u^2}\) gives, for \(|\Im z|\le2\),

\[
|H_j(\tau,z)-G_\tau^{(j)}(z)|
\le E_{\rm sp}\sum_{k=0}^{5}\frac{T_*^k(j+2k)!}{k!}
 +\frac{T_*^6}{6!}M_{12+j}(T_*,2),
\tag{6}
\]

where \(M_j(T,2)=\int_0^\infty u^j e^{Tu^2}\Phi(u)\cosh(2u)\,du\). Formula (6) is valid for negative and nonreal time. The four errors for \(j=0,1,2,3\) are each below \(6\cdot10^{-27}\).

For completeness, every theta index and the entire integration tail enter the following explicit bound. Put

\[
C_\Phi=\frac{2\pi^2}{1-16e^{-3\pi}},\quad
B_j=T/e^2+(11+j)/(2e),\quad x=(\pi/2)e^4.
\]

Then

\[
M_j(T,2)\le e^T H_0(2i)
 +\frac{C_\Phi}{4x}\exp\!\left(\frac{B_j^2}{2\pi}-x\right).
\tag{7}
\]

On \([0,1]\), use \(u^je^{Tu^2}\le e^T\) and retain \(\cosh(2u)\); its complete integral is \(H_0(2i)\). On \([1,\infty)\), use \(u^j\le e^{ju}\), \(\cosh(2u)\le e^{2u}\), and the complete geometric source bound \(\Phi\le C_\Phi e^{9u-\pi e^{4u}}\). The inequalities \(u^2\le e^{2u}/e^2\) and \(u\le e^{2u}/(2e)\), followed by completing a square and \(\Gamma(0,x)\le e^{-x}/x\), give (7). No finite source is substituted for (1).

Physical cells use a sixth-order midpoint polynomial expansion with an explicit finite-polynomial derivative remainder, plus (6). The heat difference \(H_\tau-H_0\) is evaluated with the \(k=0\) term cancelled first. A physical-cell range oracle is never used as an analytic integration callback: the quotient formed from the entire finite polynomial (5) is holomorphic near the certified wall, its required integration neighborhoods are checked, and its source correction is added separately.

The [source replay](../numerics/07_check_complete_theta_source_20261023.py) and [source record](../numerics/07_COMPLETE_THETA_SOURCE_CHECKS_20261023.json) also compare the core against independent validated finite theta-source quadrature at four points, including a complex-time corner, with both omitted-index and integration tails paid. They are implementation checks in addition to the analytic bounds, not replacements for them.

## 3. Entire wall and complete count

On every accepted closed wall segment \(\gamma_\nu\), compute

\[
m_\nu\le\inf_{\gamma_\nu}|H_0|,\qquad
\omega_\nu\ge\sup_{D\times\gamma_\nu}|H_\tau-H_0|,\qquad
\eta_\nu=\omega_\nu/m_\nu<1/4.
\tag{8}
\]

The full wall floor is \(\min_\nu(m_\nu-\omega_\nu)\). Shared endpoints are included, and the record verifies exact contiguous coverage of all four oriented edges. The coupled difference in (8), rather than two separate field magnitudes, is essential to this small relative error.

At \(\tau=0\), integrate the centered logarithmic-derivative moments

\[
p_k(0)=\frac1{2\pi i}\oint_{\partial\Omega}
 (w-36)^k\frac{H_0'(w)}{H_0(w)}\,dw,
\qquad k=0,1,2.
\tag{9}
\]

The finite-polynomial quotient is integrated on each of the four edges by validated `acb.integral`, with absolute and relative tolerance \(10^{-13}\), depth limit 16 and evaluation limit 20000 per integral. This is a bounded twelve-integral calculation. On a cell with \(|H_0|\ge m\), \(|H_0-G_0|\le e_0\), \(|H_0'-G_0'|\le e_1\), \(|H_0'|\le L\), take \(e_0=e_1=E_{\rm sp}\). The complete quotient correction is

\[
\left|\frac{H_0'}{H_0}-\frac{G_0'}{G_0}\right|
\le\frac{e_1}{m}+\frac{(L+e_1)e_0}{m(m-e_0)},
\qquad m>e_0.
\tag{10}
\]

Multiply by the cell length and \(\sup|w-36|^k/(2\pi)\), then sum. This pays the entire canonical source correction after integrating the finite analytic reference.

The resulting \(p_0\) ball has real part in \((1.5,2.5)\) and imaginary part containing zero. The argument principle makes it an integer, so it is exactly two. Rouché's theorem using (8) makes this the complete multiplicity count for every \(\tau\in D\), including possible nonreal roots and internal collisions. No chosen real subpopulation enters the argument.

## 4. Coupled coefficient continuation and discriminant

On each wall segment the principal logarithm

\[
\ell_\tau(w)=\operatorname{Log}\!\left(H_\tau(w)/H_0(w)\right)
\]

is continuous around the complete wall and satisfies
\(|\ell_\tau|\le K_\nu=-\log(1-\eta_\nu)\). Since this logarithm is single-valued on the wall, integration by parts gives, for \(k\ge1\),

\[
p_k(\tau)-p_k(0)
=-\frac{k}{2\pi i}\oint_{\partial\Omega}(w-36)^{k-1}\ell_\tau(w)\,dw.
\tag{11}
\]

Thus the uniform complex-time budgets are

\[
|p_k(\tau)-p_k(0)|\le
\frac{k}{2\pi}\sum_\nu|\gamma_\nu|r_\nu^{k-1}K_\nu,
\qquad r_\nu=\sup_{\gamma_\nu}|w-36|.
\tag{12}
\]

There is no interior logarithm differentiation and no interior root-gap denominator. For two roots, the monic prepared polynomial in \(\zeta=z-36\) is

\[
P_\tau(\zeta)=\zeta^2-p_1(\tau)\zeta+
\frac{p_1(\tau)^2-p_2(\tau)}2,\qquad
\Delta(\tau)=2p_2(\tau)-p_1(\tau)^2.
\tag{13}
\]

The recorded balls give the positive-real-part discriminant in the table. On real time slices, conjugation symmetry of both the field and rectangle makes these exact power sums real. Positivity of \(\Delta\) then proves that the complete two-root population is real and simple. At \(t=10^{-4}\), [Note 11's quadratic forest formula](11_FOREST_POLYNOMIAL_AND_GAP_FREE_FILTER_ENCLOSURE_20261023.md) gives

\[
q=\frac{8t}{\Delta(t)+8t},
\tag{14}
\]

with the stated certified interval. The relative-log source budget has now actually been acquired for one declared canonical wall; it is no longer only a formal input interface in this box.

## 5. Equally informed direct comparator and scope

The replay separately repeats the \(p_1,p_2\) contour calculation directly at \(t=10^{-4}\), using the same source core, wall, finite-polynomial integrator and tolerances, with the complete source errors (6) in the quotient correction. These eight additional integrals produce a substantially tighter terminal discriminant and filter interval than (12), which was deliberately uniform over all of \(D\). Their intervals overlap the continuation result. The record reports the separate integration times and shared source setup; wall-clock numbers describe this implementation, not an invariant complexity claim.

A cheaper separate direct reality check uses four certified source values at 28, 29, 42 and 43, uniformly for real \(t\in[-10^{-4},10^{-4}]\). Each of the disjoint intervals \((28,29)\) and \((42,43)\) has a sign change. Combined with the already acquired complete count two, this proves two real simple roots directly, and gives a gap greater than 13 and a coarser filter bound. This check is not a premise of the coefficient certificate.

The finite experiment therefore does not show an advantage for coefficient continuation over equally informed direct source estimates. It demonstrates that the complete-wall, relative-log and discriminant interfaces can be fed rigorously from the unchanged theta source, without purchasing an internal separation hypothesis. No broad height sweep, fitted schedule or new global zero conclusion is involved. Generic formulas remain valid for the collision controls on domains where their premises hold; altered controls do not satisfy the unchanged-source premise (1). A collision-containing box cannot satisfy this certificate's positive-discriminant output.

The original physical cap \(I_0\), every complementary face, and the signed deformed lower bound have not been integrated in this certificate. The absence of multiple spatial roots does imply that the complete first jet is nonzero on the compact original box, so there are no joint heat events there; the subsequent complete first-jet cover below acquires an explicit floor. A useful interval for the original cap remains a separate acquisition. Nothing in (14) substitutes the finite pair filter for that cap observable.

The [separate same-model review](../reviews/11_COMPLETE_THETA_WALL_AND_SOURCE_REVIEW_20261023.md) records the mathematical and implementation audit. The finite source gate is paid; growing-height estimates, canonical microscopic reference walls and the original cap/complement comparison remain open.


## 6. Quantitative first-jet floor on the entire box

The [full-volume cover](../numerics/08_certify_complete_first_jet_floor_20261023.py)
and [record](../numerics/08_COMPLETE_FIRST_JET_FLOOR_20261023.json) also establish
\[
\inf_{D\times\Omega}(|H|^2+|H_z|^2)>1.1178\cdot10^{-13}.
\]
There are 31 accepted spatial rectangles from 61 cell calls; every cell uses
all of the original complex time square. The proof is direct: use the complete
source enclosures for both jets, square and sum their individual magnitude
lower bounds, and subdivide any cell that does not pass the prescribed
threshold. Exact rational geometry checks disjoint interiors, containment,
and total area 80. The binary subdivision covers shared boundaries as well.
This cover uses no root data and independently supplies the explicit
regularity denominator for every physical cap and face. Its five recorded
assertions check the resulting cover and floor; they are separate from the
109 wall/coefficient checks and the 46 source checks.

No integration or cap lower bound follows merely from this positive floor.
It makes the complete four-jet density formulas available on the full frozen
domain, including all complements, and proves there are no joint events there.

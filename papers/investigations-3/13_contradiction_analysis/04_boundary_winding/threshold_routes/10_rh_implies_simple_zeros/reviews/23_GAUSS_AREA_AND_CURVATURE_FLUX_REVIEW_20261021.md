# Review of Gauss area concentration and curvature flux

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**, verified from the current turn metadata.
Same-assistant analytic review; no independent specialist validation.

[Note 24][note] gives a bounded answer to the higher-dimensional
singularity proposal. Its local Gauss-area defect is \(\pi(m-1)\),
with an explicit \(O(|t|)\) fixed-boundary error. Its double control has
total area \(2\pi\) throughout either side of the collision. Thus bounded
integrated curvature does not imply a regular endpoint for this induced
surface. The result leaves HMC-05 open and HMC-06 gated.

The [result index][results], [geometry summary][geometry],
[control register][controls] and [avoid index][avoid] govern this
assessment. This is a local analytic result and a scoped failed-estimate
comparison, not a new arithmetic estimate or a universal obstruction to
geometric approaches.

## Normalization and boundary verification

For a holomorphic pair \((f,f')\), the complex Gram identity gives
\[
\frac14\Delta\log(|f|^2+|f'|^2)
=\frac{|ff''-f'^2|^2}{(|f|^2+|f'|^2)^2}.
\]
It follows that the chosen Fubini–Study area is half the absolute
Gaussian-curvature measure of the induced complex curve. In particular
the defect is \(\pi(m-1)\) in Gauss area and \(2\pi(m-1)\) in absolute
curvature, not \(4\pi(m-1)\).

The factor \((f,f')=z^{m-1}(zg,mg+zg')\) identifies precisely what a
projective cancellation removes. The boundary calculation retains that
factor and hence its radial contribution. The proof uses a fixed circle
with a nonzero boundary energy; it does not posit a lower energy bound
in the shrinking interior. Hermite splitting and fixed-circle Rouché
counting supply interior regularity for small nonzero times of either
sign. The limit is proved on every smaller disk, and annular convergence
plus positivity then justifies weak convergence.

The fixed-boundary expression is real analytic through zero because its
energy stays positive there. Its extension includes the defect; the
integral of the canceled endpoint density does not. This distinction
locates exactly why regularity of the alternative integral expression
does not justify exchanging the limit and the interior integral.

GA7's constants check directly:
\[
|\partial_t\partial_n\log\mathscr E|
\le 2d/e_R+4cb/e_R^2.
\]
Multiplication by one quarter of the circle length gives exactly
\(\pi R|t|(d/e_R+2cb/e_R^2)\). The fourth jet in \(d\) is necessary:
the time derivative of \(H_{zz}\) is \(-H_{zzzz}\).
The floor \(e_R\) is event-dependent, and the full moment bounds cover
both source tails; no uniform height floor is introduced.

## Exact control and complex inner limit

For the double polynomial the circle energy is
\(a+b\cos2\theta\), with \(a>|b|\). Its mean logarithm yields GA8
without estimating positive and negative boundary terms separately.
The reduced formula satisfies
\[
\Delta-(R^4-4s^2)^2
=8R^2(R^4+2R^2+4s^2)>0,
\]
where \(\Delta\) is its square-root radicand. This proves the strict
finite-disk bounds \(0<A<2\pi\). The fixed-radius, inner-radius and
whole-plane limits give respectively GA9, GA10 and \(2\pi\).
The exact rotation relating the two signs of time proves equality
of their unsigned disk areas, although their real turning signs differ.

The complex inner expansion in GA11 is a continuation of the existing
real analytic power-series argument, with the same full stationary
center. It is uniform only on fixed scaled disks. It yields
\((1+|q|^2)^{-2}dA_q\) as the Gauss-area profile, and its integral
is \(\pi C^2/(1+C^2)\). No growing-disk error is asserted.

The induced metric brings an additional factor
\(|k|^2s^{2r+2}/r^2\). Combining that factor with the curvature power
gives GA14's exponent \((2r+2)(1-p)\). Thus \(p=1\) is compatible with
concentration and \(p>1\) diverges at these finite events. The latter is
a property of the conditional event geometry, not a proved theta norm
bound.

For odd multiplicity, the real predecessor belongs to \(W=H_z\).
Its surface energy differs from the original first-jet energy; the
note retains the distinction and the different concentration counts.
This avoids importing the \(j=1\) angle denominator as though it were
the physical first-jet energy throughout a window.

## Four-dimensional interpretation and controls

The product surface has Ricci form \(-2d\mu\). Wedge with its Kähler
form leaves only the transverse flat-area term, giving
\(-\int\operatorname{Ric}\wedge\omega=2\,\operatorname{Area}(B)A_t(R)\).
The scalar-curvature integral is twice this quantity in magnitude.
Shrinking \(B\) reduces the unnormalized defect; dividing by its area
recovers it. These statements concern this observation on this surface,
not every possible quaternionic or octonionic integral.

The local theorem applies to the catalogued controls at their analytic
finite events without assuming an all-real heat slice. This is why
weighted-square controls are legitimate for this local test despite
their failure of the all-real hypothesis used elsewhere in HMC.
The close positive endpoint controls remain the direct comparison for
the RH-conditional simplicity problem: they retain their stated source
and completion information while failing ordinary Dirichlet arithmetic.
No claim combines the stronger preservation lists of different controls.

The required one-sided real-turning estimate cannot be replaced by
bounded unsigned total curvature: the two signs of the explicit double
control have identical area data. A different arithmetic or marked-slice
estimate is not excluded. Proposed stronger norm bounds must still be
proved from the source and screened; naming such a bound is not a
completed milestone.

## Verification and status

The [new replay][checker] passed its frozen exact checks for degrees
two through ten, both time signs, complex rational jets, and both parity
branches with pure and asymmetric germs. Its [receipt][receipt] binds
the script and its two existing algebra dependencies. Rational square-root
enclosures check bounded values of GA8; displayed decimals are only
readable versions of those enclosures. The general analytic proofs,
including every limit and the all-multiplicity statement, remain the
written arguments in Note 24.

Primary normalization checks used
[Demailly (1.20), p. 12][dem] for the divisor convention and
[Kawakami–Watanabe (24)–(25)][kw] for the curvature convention. No
global minimal-surface classification or compactness theorem is imported.
The existing Investigation 22 inner-profile result is explicitly credited;
its earlier bound is not counted as a new contribution.

The useful addition is the finite-area concentration law, its paid
boundary error, and the exact surface control. HMC-05's source-dependent
signed correction remains uncomputed here; HMC-06 remains gated.

[note]: ../notes/24_GAUSS_AREA_CONCENTRATION_AND_CURVATURE_FLUX_20261021.md
[results]: ../../../../../../../result-summaries/README.md
[geometry]: ../../../../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[checker]: ../numerics/check_hmc_gauss_concentration.py
[receipt]: ../numerics/HMC_GAUSS_CONCENTRATION_CHECKS_20261021.json
[dem]: https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/analmeth_book.pdf
[kw]: https://link.springer.com/article/10.1007/s12220-024-01721-7


## Multiplicity-selective continuation: relative Chern and Hopf numbers

21 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, actual effort max**. Same-assistant analytic assessment of
[Note 25](../notes/25_MULTIPLICITY_SELECTIVE_CHERN_AND_HOPF_OBSERVATIONS_20261021.md);
no independent review or numerical theta calculation.

The local Gauss defect is already zero at m=1; total smooth Gauss area is
not. Investigation 22's inherited holomorphic intersection multiplicity
binomial(m,2) is a relative top Chern/Euler number of the rank-two heat
jet with its boundary section. It is not the absolute second Chern class
of that trivial bundle, nor a Chern class of the source theta line bundle.
Complex heat time and spectral position are distinct from the elliptic
coordinates of the arithmetic hyperkähler family.

The normalization in MC6 is consistent: the standard contact form has
alpha wedge d alpha equal to twice the outward-oriented unit S3 volume,
so its integral is 4pi². Pullback multiplies this by the complex local
degree. This is the Hopf invariant of the declared projective heat-jet
map, not an unspecified Gauss map or another Milnor enhancement.

For MC7, the target complex Hessian determinant is epsilon²/(E+epsilon²)³;
the wedge square supplies 2/pi² and holomorphic pullback supplies
abs(det DG)². The heat equation gives det DG=Hz Hzzz-Hzz². The target
radial integral in MC8 tends to one. Independently, d alpha_epsilon
=2pi omega_epsilon gives MC9 by ordinary Stokes on the whole ball.
Only smooth convergence on the nonzero boundary is passed through the
integral. Positivity and local convergence off the isolated event prove
the asserted limiting atom. Finite regularization is not exactly
background-free at simple points.

The double control has determinant -4 and degree one on flat hyperkähler
C². It rules out inferring local charge zero merely from flat ambient
geometry or absolute bundle triviality. It does not rule out an additional
arithmetic comparison. A trace-free quadrupole vanishes on the radial
inner double profile; the statement is limited to that automatic moment
test. Controls retain their separate failed premises as listed in Note 25.

The assessment finds the displayed local formulas and distinctions
consistent. No theta upper bound below one, endpoint exclusion, or change
to HMC-05/06 status follows.

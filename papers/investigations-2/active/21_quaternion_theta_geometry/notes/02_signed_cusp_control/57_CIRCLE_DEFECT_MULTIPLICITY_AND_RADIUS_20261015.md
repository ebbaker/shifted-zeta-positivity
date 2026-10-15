---
research_program: PR02
secondary_programs: [ALG, PR02-CORR]
status: conditional_collision_stress_test_and_boundary_defect_obstruction
---

# Multiplicity and circle radius losses

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6-astra**, reasoning effort **ultra**, verified and supplied by the coordinator. No numerical experiment is used.

This continues [Note 46](46_OCTONIONIC_BOUNDARY_CURRENT_AND_SIGNED_CUTOFF_TARGET_20261015.md), [Note 50](../04_octonionic_reductions/50_QUATERNION_FORMS_HODGE_PAIRING_AND_SOURCE_TARGET_20261015.md), and [Note 51](../04_octonionic_reductions/51_POLARIZED_HODGE_DISK_AND_CENTERED_SOURCE_BOUNDS_20261015.md). It proves that paying the negative part of the polarized circle current can introduce a substantially stronger loss than the exact signed observation. At a hypothetical collision of multiplicity `2r+j`, its fixed-radius loss grows like `s^{-r}`, while the required stationary loss grows like `s^{-1}`. A radius at the square-root time scale removes that excess order but cannot produce a bounded loss. The conclusion is a discriminating obstruction to a sufficient mechanism, not a claim that the theta field has a collision and not a new pointwise sign theorem.

## 1. Exact cost of dropping the positive mass

Use the manuscript's complete physical jets, energy, and stationary sets:

\[
h_j=\partial_x^jH,\qquad H_t=-H_{xx},\qquad
E=h_0^2+h_1^2,\qquad S_j=\{h_{j+1}=0\},\quad j=0,1.
\]

At a real point of `S_j`, put

\[
\phi_{j,R}(\theta)=h_j(t,x)\Re h_j(t,x+Re^{i\theta}),
\quad q(\theta)=1-\cos2\theta,
\]
\[
D_{j,R}=\langle q(\phi_{j,R})_-\rangle,
\qquad P_{j,R}=\langle q(\phi_{j,R})_+\rangle,
\quad \langle f\rangle=(2\pi)^{-1}\int_0^{2\pi}f.
\]

Note 46's exact current identity is

\[
\mathcal L_j=-\frac4{R^2}h_j^2+
\frac4{R^2}(P_{j,R}-D_{j,R}).
\tag{1}
\]

At points where `E>0`, define the sharper defect coefficient

\[
K^{\rm def}_{j,R}:=\frac4{R^2}
\left(\frac{h_j^2}{E}+\frac{D_{j,R}}E\right).
\]

Then the exact excess over the signed loss is

\[
\boxed{K^{\rm def}_{j,R}
=-\frac{\mathcal L_j}{E}+
\frac4{R^2}\frac{P_{j,R}}E.}
\tag{2}
\]

The positive weighted mass is precisely what is paid again when the signed current is replaced by its negative part. All divisions here and below are diagnostic and occur on proved nonzero predecessor branches; none defines a proposed source coefficient.

## 2. Every bounded positive radius creates a multiplicity-dependent pole

Suppose the analytic backward-heat field has exact spatial multiplicity

\[
m=2r+j\quad(r\ge1,\ j\in\{0,1\})
\]

at `(T,x_*)`. For every radius used below, assume that the field is holomorphic on a neighborhood of the corresponding closed spectral disk and remains so for nearby heat times; the complete theta field is entire and meets this condition for every finite radius. For a merely local analytic heat field, restrict all radii to a common disk of holomorphy. Write `W=h_j`, `A=h_m(T,x_*)\ne0`, and `k=A/r!`. The manuscript's stationary predecessor construction supplies `x=\chi(s)`, `s=T-t>0`, with

\[
W_x(T-s,\chi(s))=0,\quad \chi(s)=x_*+O(s),
\]
\[
W(T-s,\chi(s))=ks^r(1+O(s)),\quad
E(T-s,\chi(s))=k^2s^{2r}(1+O(s)),
\]
\[
\mathcal L_j/E=-r/s+O(1).
\tag{3}
\]

For fixed `R>0`, set

\[
c_-(R)=\frac1{|k|}
\left\langle q\bigl(\operatorname{sgn}(k)
\Re W(T,x_*+Re^{i\theta})\bigr)_-\right\rangle,
\]
\[
c_+(R)=\frac1{|k|}
\left\langle q\bigl(\operatorname{sgn}(k)
\Re W(T,x_*+Re^{i\theta})\bigr)_+\right\rangle.
\tag{4}
\]

Both are strictly positive. Indeed the real part of the nonzero holomorphic germ has circle mean `W(T,x_*)=0`. It cannot vanish identically on the circle: the harmonic Dirichlet uniqueness principle and holomorphicity would then force the germ to be zero. Thus its boundary real part has nonempty open sets of both signs. Since `q>0` except at two points, both weighted masses are positive.

If `R(s)\to R_*>0`, local uniform convergence on the spectral circle and the Lipschitz property of positive and negative parts give

\[
\boxed{\frac{D_{j,R(s)}}E
=s^{-r}\{c_-(R_*)+o(1)\},\qquad
\frac{P_{j,R(s)}}E
=s^{-r}\{c_+(R_*)+o(1)\}.}
\tag{5}
\]

More generally this convergence is uniform for radii in any compact interval `[R_0,R_1]\subset(0,\infty)`, and `c_\pm` are continuous and strictly positive there. Consequently any radius rule with locally bounded `R` and `1/R` has

\[
D_{j,R}/E\asymp s^{-r},\qquad K^{\rm def}_{j,R}\asymp s^{-r}.
\tag{6}
\]

For `r\ge2` this is a strictly larger pole order than (3). The leading positive and negative masses cancel in the exact signed current. Indeed circle reproduction at the event gives

\[
c_+(R)-c_-(R)
=-\frac{\operatorname{sgn}(k)R^2}{4|k|}W_{xx}(T,x_*)
=\begin{cases}-R^2/4,&r=1,\\0,&r\ge2.\end{cases}
\tag{7}
\]

The conclusion is not confined to an exceptional choice of radius or to polynomial controls. It holds for every nontrivial analytic germ with the specified collision, including a hypothetical collision of the complete theta field.

## 3. The square-root radius profile

For a fixed `\rho>0`, choose the diagnostic radius `R=\rho\sqrt{s}`. The backward-heat Taylor expansion gives, uniformly in the circle angle,

\[
\frac{W(T-s,\chi(s)+\rho\sqrt{s}e^{i\theta})}
{W(T-s,\chi(s))}
\longrightarrow F_r(\rho e^{i\theta}),
\]
\[
F_r(z)=\sum_{\ell=0}^r
\frac{r!}{(r-\ell)!(2\ell)!}z^{2\ell}.
\tag{8}
\]

To see this, the leading terms of the heat Taylor series have `2p+q=2r`, and equal `A s^p(\sqrt{s}z)^q/(p!q!)`. Their sum divided by `ks^r` is (8); the predecessor displacement is `O(s)` and contributes only a lower-order correction. Analyticity bounds the remaining terms uniformly for bounded `\rho`. For the odd branch, `E/W^2\to1` by the predecessor expansion.

Put

\[
d_r(\rho)=\langle q(\Re F_r(\rho e^{i\theta}))_-\rangle,
\quad p_r(\rho)=\langle q(\Re F_r(\rho e^{i\theta}))_+\rangle.
\]

Then

\[
\frac{D_{j,R}}E\to d_r(\rho),\qquad
sK^{\rm def}_{j,R}\to C_r(\rho):=
\frac4{\rho^2}\{1+d_r(\rho)\}.
\tag{9}
\]

Only the constant and second angular harmonics survive pairing with `q`, so

\[
p_r(\rho)-d_r(\rho)=1-\frac{r\rho^2}{4},
\qquad
\boxed{C_r(\rho)=r+\frac4{\rho^2}p_r(\rho)>r.}
\tag{10}
\]

The strict inequality follows because the real part in (8) is positive at angle zero, hence on a nearby interval with `q>0`.

For `r\ge2`, `C_r(\rho)\to\infty` as `\rho\downarrow0` and as `\rho\to\infty`. The first assertion follows from `d_r\ge0`. For the second, the highest harmonic gives

\[
d_r(\rho)\sim\frac{r!}{(2r)!\pi}\rho^{2r}.
\tag{11}
\]

Here `\langle(-\cos2r\theta)_+\rangle=1/\pi`, while its product with `\cos2\theta` has zero mean for `r\ge2`, by periodicity. Thus `C_r` is continuous, achieves a finite minimum, and

\[
\min_{\rho>0}C_r(\rho)>r\qquad(r\ge2).
\tag{12}
\]

Even the optimal radius in this local family imposes a strictly larger coefficient of the unavoidable `1/s` pole than the exact signed observation.

## 4. The quadratic and cubic controls have an exact excess constant

For `r=1`, write `a=\rho^2/2`. Then `F_1=1+z^2/2`. If `a\le1`, `d_1=0`; if `a>1`, setting `\alpha=\arccos(1/a)` gives the explicit elementary integral

\[
d_1(\rho)=\frac1\pi
\left\{(a/2-1)\alpha+(a-1/2)\sin\alpha\right\}.
\tag{13}
\]

Moreover `C_1=2(1+d_1)/a` is strictly decreasing in `a`. Away from the measure-zero boundary of its negative set,

\[
a\frac{dd_1}{da}-d_1
=\langle q\,\mathbf1_{\{1+a\cos2\theta<0\}}\rangle<1,
\]

which proves the derivative sign; the formula also gives continuity at `a=1`. Hence

\[
\boxed{\inf_{\rho>0}C_1(\rho)=\frac12+\frac2\pi>1.}
\tag{14}
\]

The infimum is approached only as `\rho\to\infty`. This gives an exact universal excess of approximately 13.66 percent in the shrinking-circle local model for double and triple collisions.

## 5. The three radius regimes and the research target

If `R(s)\to0` but `R(s)/\sqrt{s}\to\infty`, the leading spatial term dominates the local heat polynomial, giving

\[
\frac{D_{j,R}}E\sim
\frac{r!}{(2r)!}b_r\left(\frac{R^2}{s}\right)^r,
\quad
b_r=\begin{cases}1/\pi+1/4,&r=1,\\1/\pi,&r\ge2.\end{cases}
\tag{15}
\]

This follows uniformly from the Taylor expansion: all other leading heat terms are smaller by powers of `s/R^2`, and higher spatial terms are smaller by positive powers of `R`. For `r\ge2`, therefore, `sK^{\rm def}\to\infty`; for `r=1`, it tends to the constant in (14). Conversely, if `R/\sqrt{s}\to0`, the normalized circle field tends uniformly to 1, so its negative mass eventually vanishes but `sK^{\rm def}\sim4s/R^2\to\infty`.

For `r\ge2`, a radius comparable to `\sqrt{s}` is consequently the only local scale on which the defect coefficient can remain of order `1/s`. Such a radius is defined using the unknown event and has unbounded `1/R`; it is a stress test, not an admissible bounded-loss source prescription.

The fixed-radius defect criterion remains logically sufficient. These results quantify how much stronger it can be: for high multiplicity it requires controlling two separately divergent boundary masses whose exact difference has a lower pole order. Small-energy localization does not avoid the issue, because (3) places every sufficiently close predecessor inside `E\le\delta\Gamma^2` whenever the prescribed scale `\Gamma` is positive and continuous at the event.

The focused remaining target should preserve

\[
\langle q\phi_{j,R}\rangle=P_{j,R}-D_{j,R}
\]

with full source summation before estimation. Equation (2) is a diagnostic for any proposed positive-sector or absolute boundary estimate. An analytic mechanism which controls only the separate negative mass is demanding a stronger cancellation property; radius optimization does not supply it. None of the arguments above proves the required theta-specific signed lower bound.

## Audit points

- `j` must match parity of the collision: `m=2r+j` with `j=0,1`; on the odd predecessor the physical energy is asymptotic to `h_1^2`, rather than identically equal to it.
- The current keeps the complete real prefactor and the complete stationary condition. No stationarity of a cutoff is substituted.
- Uniformity in (5) requires radii in a compact positive interval; the shrinking-radius assertions use separate Taylor arguments.
- The negative-part operation is applied after the complete holomorphic field is evaluated.
- Equations (5)–(15) are conditional collision controls. They neither assert a theta collision nor enlarge the proved theta sign domain.

## Exact finite algebra checks

The accompanying [standard-library checker](../../numerics/check_circle_defect_collision_profile.py) and its [receipt](../../numerics/CIRCLE_DEFECT_COLLISION_PROFILE_CHECKS_20261015.json) record the script hash, provenance, and scope. The checker passes **240 exact rational assertions** for `r=1,...,12` and both physical branches. It constructs finite backward-heat polynomials independently, verifies the normalized profile and stationary curvature, tests the leading stationary displacement under two higher-order perturbations, and checks the signed circle projection by Laurent-polynomial multiplication. In the odd case it verifies `H/W= -B s/[r(r+1)A]+O(s^2)`, hence `E/W^2=1+O(s^2)`. These checks support finite algebra only: the convergence, harmonic sign, optimization, and limiting arguments above are analytic proofs. No theta quadrature, numerical pilot, new interval certificate, or claimed sign domain is supplied.

Replay from the investigation directory:

    python3 numerics/check_circle_defect_collision_profile.py --output /tmp/circle-defect-replay.json

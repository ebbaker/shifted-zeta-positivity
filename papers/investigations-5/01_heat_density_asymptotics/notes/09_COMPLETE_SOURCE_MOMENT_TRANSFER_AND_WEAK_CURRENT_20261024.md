# Complete-source moment transfer to coarse density and weak current

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**.

**Status:** conditional finite-domain estimates proved below; actual-theta
inputs and comparisons evaluated in floating arithmetic. No interval
certificate, independent implementation, continuous-time enclosure,
global simplicity result, or boundary-matched evolution is claimed.
This is a quantitative approximation milestone under
[avoid 01][classification]. The [contract][contract] separates it from
the earlier small-window closure experiment.

The advance is a source-moment route to a coarse density error and an
actual regulator-bias estimate, together with contour measurements of
weak transport. It avoids quadrature of narrow density peaks and does
not find or fit individual theta zeros. The contour/reference theory is
standard; there is no priority claim. See the [reference catalog][refs],
[result index][results], [collision screen][controls] and [avoid index][avoid].

## 1. Preserve amplitude while extracting source concentration

For the unchanged positive theta source set
\[
 M(t)=H(t,0),\quad dP_t(u)=M(t)^{-1}e^{tu^2}\Phi(u)du,
 \quad f(t,z)=H(t,z)/M(t)=\mathbb E_t\cos(uz).
\]
The probability measure is a source-integral tool. The physical density
is still unnormalized, with fixed epsilon=1e-4. In scaled calculations
\(\eta=\epsilon/M\); neither epsilon nor the density is rescaled by choice.
Store log M and log eta, because M itself overflows in the upper cases.

Put \(\mu=\mathbb E u\), \(v=\mathbb E(u-\mu)^2\),
\(m_j=\mathbb E(u-\mu)^j\), and
\(B_j(Y)=\mathbb E[|u-\mu|^j e^{Y|u-\mu|}]\).
For \(|x|\le X, |y|\le Y\), write \(Z=\sqrt{X^2+Y^2}\).
Taylor expansion of cos(uz) in u about mu, with integral remainder, gives
\[
 f(z)=A(z)\cos(\mu z)+E(z),\qquad A(z)=1-\tfrac12vz^2,
 \qquad |E(z)|\le D_3:=\frac{Z^3}{6}e^{\mu Y}B_3(Y). \tag{1}
\]
The first centered moment vanishes. The third derivative of the cosine
on the segment from mu to u has modulus at most
\(|z|^3 e^{\mu Y}e^{Y|u-\mu|}\), proving the remainder estimate.
All moments here are of the complete source. Theta decay permits these
moments and the differentiations used below on the finite time range.

If \(a_*=1-vZ^2/2>0\), A has no zero in the rectangle and
\[
 \left|f(z)/A(z)-\cos(\mu z)\right|\le\delta:=D_3/a_* . \tag{2}
\]
For comparison the unadjusted estimate is
\(|f-\cos(\mu z)|\le Z^2 e^{\mu Y}B_2(Y)/2\).
Keeping the variance in a zero-free analytic factor removes the leading
amplitude error from the zero comparison. Equation (2) is uniform in
the stated complex rectangle; it is not an asymptotic assertion for
unrestricted growing height or number of periods.

## 2. A finite carrier-to-density bound

Take \(X=N\pi/\mu\), so the real walls are carrier maxima, and suppose
\[
 0<\delta<1/2,\qquad r=\mu^{-1}\arcsin(2\delta)
 <\min\{Y,\pi/(2\mu)\}. \tag{3}
\]
There are 2N carrier zeros \(c_j=(j+1/2)\pi/\mu\) inside this rectangle.
The disjoint disks \(|z-c_j|<r\) are inside it. On their boundaries,
and everywhere outside them in the rectangle,
\[
 |\cos(\mu z)|\ge\sin(\mu r).
\]
Indeed \(|\cos(\mu(x+iy))|^2=\sin^2(\mu d)+\sinh^2(\mu y)\),
where d is the real distance to the nearest carrier zero, with
\(|d|\le\pi/(2\mu)\). For \(|d|<r\), use the decrease of sin(s)/s
on [0,pi/2] and sinh(s)>=s; for |d|>=r use monotonicity of sin there.

The homotopy from cos to f/A cannot vanish on any disk boundary by
(2)–(3). Its integer argument count is constant; the argument principle
therefore gives exactly one zero, counted with multiplicity, in each
disk. The outside lower bound gives no other zeros in the rectangle.
Conjugation symmetry and uniqueness make each zero real and simple.
This is a **local sufficient concentration condition**, not a statement
about theta at all times, all heights, or collisions outside this box.

Let \(k_\ell(x)=\ell^{-1}k(x/\ell)\),
\(k(q)=C(1-q^2)^4\mathbf1_{|q|\le1}\), C=315/256, and
\(K(x,y)=k_\ell(x)k_h(y)\). For observation centers |x|<=xmax assume
\(\ell+x_{\max}+r<X\), so all possibly weighted roots are covered.
Then, with \(\nu_t\) the actual zero measure,
\[
 \left|(K*\nu_t)(x,y)-\frac\mu\pi k_h(y)\right|
 \le k_h(y)\left(2Nr\|k_\ell'\|_\infty+E_{\rm phase}\right), \tag{4}
\]
\[
 E_{\rm phase}\le\frac{p^3}{720}\|k_\ell^{(4)}\|_1,
 \qquad p=\pi/\mu. \tag{5}
\]
For (4), match each real zero to its carrier disk and apply the mean
value theorem to the zero-extended C3 kernel. This also handles roots
close to a kernel edge. The remaining finite-lattice error is (5).
To prove (5), periodize k_ell with period p. Its Fourier coefficients
are p^-1 times its Fourier transform at 2 pi n/p. Four integrations by
parts give magnitude at most ||k_ell^(4)||_1/|2 pi n/p|^4. Sum n != 0;
2 zeta(4)/(2 pi)^4=1/720. The zero extension is C3, so there are no
boundary terms in those four integrations. This argument is uniform
in the lattice phase/observation x.

The constants are explicit:
\(\|k_\ell'\|_\infty=8C(6/7)^3/(\sqrt7\ell^2)\), and
\(k^{(4)}=C(144-1440q^2+1680q^4)\) inside (-1,1).
Its L1 norm is integrated by splitting at
\(q^2=(15\pm2\sqrt{30})/35\); the script records it.

## 3. Supplying the regulator lower bounds without locating theta roots

Equations (2)–(3) give an outside lower bound for the **scaled** field
\[
 |f|\ge b:=a_*\{\sin(\mu r)-\delta\}>0. \tag{6}
\]
Within a carrier disk let a be its unique actual zero. The analytic
zero-free quotient f(z)/(z-a) has boundary modulus at least b/(2r).
Apply the maximum-modulus principle to its reciprocal to obtain
\[
 |f(z)|\ge c|z-a|,\qquad c=b/(2r). \tag{7}
\]
No numerical value of a is needed. The carrier disk is contained in
the radius-2r disk about a. [Note 06][regulator] consequently gives
\[
 \int_{[-X,X]\times[-Y,Y]}
       \log(1+\eta^2/|f|^2)\,dA
 \le 4XY\eta^2/b^2+2N I_1(\eta/c,2r), \tag{8}
\]
\[
 |K*\rho_\epsilon-K*\nu_t|
 \le \frac{\|\Delta K\|_\infty}{4\pi}
       \{4XY\eta^2/b^2+2N I_1(\eta/c,2r)\}, \tag{9}
\]
where \(I_1(a,R)\le\pi a^2[1+\log(1+R^2/a^2)]\), and
\[
 \|\Delta K\|_\infty\le8C^2(\ell^{-3}h^{-1}+\ell^{-1}h^{-3}).
\]
Adding (4) and (9) bounds the desired regularized density by the proposed
coarse shape. The moment premises pay the nonvanishing/quotient inputs
that Note 06 had left unspecified. They do not pay numerical integration
error: floating values of moments remain floating inputs to these bounds.

This use of separate disks is only a way to bound an integrated logarithm.
It does not fit peaks or use computed root locations. Near a multiple
event the single-root concentration premise can fail; the general
cluster/multiplicity estimate in Note 06 is still needed there.

## 4. Contour observations of weak mass and transport

For x center c0 let P(z)=k_ell(z-c0), interpreted as its polynomial inside
the vertical walls c0 +/- ell. Let Gamma be their rectangle with nonzero
boundary H. For the real simple zeros inside, the residue theorem gives
\[
 C_0=\frac1{2\pi i}\oint_\Gamma P\frac{H_z}{H}dz
       =\sum_a k_\ell(c_0-a), \tag{10}
\]
\[
 C_J=\frac1{2\pi i}\oint_\Gamma P\frac{H_{zz}}H dz
       =\sum_a k_\ell(c_0-a)a'(t),\quad
 C_t=\frac1{2\pi i}\oint_\Gamma P'\frac{H_{zz}}H dz. \tag{11}
\]
Here H_t=-H_zz implies a'=H_zz(a)/H_z(a), and C_t=dC_0/dt.
The derivative P' is with respect to z, so it has the required opposite
sign from the derivative with respect to c0. Boundary crossings are
excluded at an individual contour evaluation; the compact C3 weight
also makes the weak observable continuous through kernel-edge crossings.
The finite sampled contours have nonzero observed boundary values, not
certified continuum boundary floors.

Thus R0=k_h(y) C0, J0=k_h(y) CJ is real, and R0,t=k_h(y) Ct.
These are exact zero-measure formulas under the stated premises, not
raw finite-epsilon peak measurements. Locally near a simple zero,
j_epsilon=(H_zz/H_z)rho_epsilon, so the current converges weakly to
a' delta_a. Off the zero disks it tends to zero. This justifies the
current-limit target, but supplies no numerical finite-epsilon current
error or differentiated regulator-bias bound.

The source tilt gives the exact moment identity
\[
 \mu'=\operatorname{Cov}(u,u^2)=2\mu v+m_3. \tag{12}
\]
A moving phase lattice has velocity -(mu'/mu)a and coarse intensity
mu/pi. The resulting leading model is
\[
 R_m=\frac\mu\pi k_h(y),\qquad
 J_m=-\frac{\mu'}\pi x k_h(y),\qquad
 (R_m)_t=\frac{\mu'}\pi k_h(y). \tag{13}
\]
It satisfies continuity algebraically. Its accuracy is tested against
(10)–(11), using no fitted parameter. The stationary fixed-frequency
baseline has zero current and zero time derivative. The kernel-weighted
model averages in x exactly, since its current is linear in x.

For the fixed centered temporal filter G, use Gmu and Gmu' in (13),
not moments evaluated at an averaged time. Derivatives commute with G.
The auxiliary moving X in the transfer proof is not an averaging width;
it introduces no commutator into the fixed target observation.

## 5. Covariance bookkeeping that the weak-current result does not replace

Let A_h(y)=(k_h*|.|)(y), s_h=A_h'=k_h*sgn, and
\(v_x=\ell^2/11,v_y=h^2/11\). The phase-homogenized Gaussian-envelope
potential ansatz is
\[
 U_g=2\log M-2\log2-v(x^2-y^2+v_x-v_y)+2\mu A_h(y). \tag{14}
\]
It has Delta U_g=4 mu k_h, giving (13)'s density. It is an ansatz,
not the exact filtered theta potential or the polynomial carrier in (1).
The source fixes (log M)'=mu^2+v and
v'=2 mu m3+m4-v^2. Substitution into the potential equation determines
the *kinematic companion*
\[
\begin{split}
 Q_g={}&4\mu k_h+4\mu^2(s_h^2-1)\\
 &+2v'(x^2-y^2+v_x-v_y)-4\mu'A_h
   +4v^2(y^2-x^2)+8v\mu y s_h . \tag{15}
\end{split}
\]
The first line is Note 05's phase-cell covariance **including** the
additional transverse variance subtraction. Using just 4 mu k_h would
miss 4 mu^2(s_h^2-1). The second line retains the parameter evolution
and envelope terms. Defining Q_g this way makes the model equation an
identity; it is **not an independent covariance closure validation**.

For an additional fixed temporal average, V=G U_g requires
\[
 Q_{g,G}=GQ_g+\operatorname{Var}_G((U_g)_x)
                     -\operatorname{Var}_G((U_g)_y), \tag{16}
\]
where the extra variance is
\[
 4(x^2-y^2)\operatorname{Var}_G(v)
 -4s_h^2\operatorname{Var}_G(\mu)
 -8ys_h\operatorname{Cov}_G(v,\mu).
\]
This follows by averaging the model potential equation, exactly as in
the law of total covariance; no projection property is assumed. The
record includes these source parameter covariances for later use.
The current/derivative comparison below is the declared weak diagnostic.
Neither Delta(Q_theta-Q_g) nor a residual-to-solution stability bound
has been measured. The small-window gradient closure is not extrapolated
to these widths without its derivative-bound hypothesis.

## 6. Actual-theta floating results

The [script][script] uses scaled complete-source formulas, truncated
numerically as the contract states. The [record][data] holds nine slice
observations and three time-averaged observations. Transverse values
y=0,1/4,1/2 multiply the same coefficients by k_h(y); they are not
additional independent source comparisons.

| t | mu | variance v | adjusted delta | r | conservative density transfer at y=0 |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 512 | 1.132637323 | 2.74852908e-4 | 0.0251394 | 0.0444097 | 0.0218020 |
| 768 | 1.260120720 | 1.60517516e-4 | 0.00928313 | 0.0147346 | 0.00775299 |
| 1024 | 1.348793941 | 1.10799062e-4 | 0.00479644 | 0.00711230 | 0.00406054 |

The unadjusted cosine bounds are 0.163018, 0.0896154 and 0.0601225.
The adjusted carrier reduces those bounds by factors about 6.5, 9.7
and 12.5. All displayed transfer gates pass as floating substitutions;
they have not been interval-enclosed. The conservative bounds in the
last column are much larger than the observed model errors.

| t | maximum relative density error over x=0,1,2 | maximum relative current error over x=1,2 | maximum relative time-derivative error |
| ---: | ---: | ---: | ---: |
| 512 | 0.02984% | 0.04642% | 0.19154% |
| 768 | 0.00823% | 0.08543% | 0.35888% |
| 1024 | 0.01088% | 0.05331% | 0.23703% |

At x=0 the current vanishes by symmetry and is checked absolutely.
The centered 768 +/-64 time average has maximum errors about 0.00805%
in density, 0.08560% in nonzero current and 0.35834% in time derivative.
The moving-intensity model improves the differentiated comparison over
the zero-derivative baseline; it is still evaluated from actual source
moments, not a self-contained long-time solution of a reduced PDE.
Keeping the exact finite cosine-lattice sum reduces the maximum observed
relative mass discrepancy to 2.27e-6, 6.63e-7 and 2.94e-7 at the three
times. Thus finite phase averaging dominates the observed mass error of
the constant-intensity model in this sample; this is not a universal law.

Using (9), the floating values of **log10 of the regulator-bias formula**
are -328.85, -649.45 and -1028.87. These tiny numbers concern only
fixed-epsilon versus zero-measure bias under the source-moment premises.
**They are not certified upper bounds, observed floating accuracy, or
total approximation error.** Large absolute M explains them. The code
retains logarithms rather than turning underflow into zero. The same
gate/formula is recorded at all temporal quadrature nodes, without a
uniform-in-time conclusion between nodes.

The initial 96-to-160 contour refinement changed mass by as much as
1.78e-7, failing the 1e-8 target. A further 224-node calculation repairs
that diagnostic; the failed comparison is retained. Source-order/cutoff
refinement, a second contour height, time finite differences, a cosine
residue control and 12-to-20 temporal quadrature are separate checks.
See the [assessment][review] for their final maxima. There is no
outward rounding, rigorous source-tail/quadrature enclosure, independent
code path, or specialist review.

## 7. Controls and the remaining gates

At the positive-time double event of
H=(1+exp(4(t-1/4))cos(2z))/2, the half-line source has equal atoms at
0 and 2, so mu=1, v=1. The nonvanishing gate a_*>0 fails on this
contract's rectangle (a_*=-177.434...). Positivity and finite moments
alone therefore do not supply this estimate's quantitative premises.
The cosine control has zero current and the exact finite-lattice mass,
and checks the contour orientation and normalization.

The four existing control families remain screened at their stated
premises: Euler-factor sources change the canonical arithmetic;
weighted-square sources change the weights and full reflection;
reflected super-Gaussian and positive-primitive constructions lack the
unchanged theta square expansion. They can satisfy (1)–(16) and local
concentration away from their collisions. If an event lies in a region
covered by the single-root disk conclusion, at least one quantitative
concentration/domain premise must fail. Their numerical gates were not
recomputed here; no global rejection or old-certificate replay is claimed.

HDA-02 now has an actual-source numerical evaluation of an explicit
regulator bound, HDA-04 has a finite coarse-transfer estimate and measured
shape error, and HDA-06 has weak-current/derivative evidence. All remain
partial. Next certify the source moments and integration budgets on a
short time slab, or directly measure the differentiated covariance with
a compatible weak method. Keep negative-time derivative remainders,
source-fixed potential traces and stability as gates before HDA-07.

[contract]: 08_SECOND_BOUNDED_COARSE_AVERAGING_CONTRACT_20261024.md
[regulator]: 06_REGULATOR_BIAS_FOR_SMOOTHED_ZERO_COUNTS_20261024.md
[script]: ../numerics/coarse_theta_round2.py
[data]: ../numerics/COARSE_THETA_ROUND2_20261024.json
[review]: ../reviews/02_COARSE_TRANSFER_AND_WEAK_CURRENT_SELF_REVIEW_20261024.md
[refs]: ../references/README.md
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[classification]: ../../../../avoid/01_restating_the_target.md

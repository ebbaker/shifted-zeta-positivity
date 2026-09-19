# Angular smearing, the finite difference form, and a Robin model of the shift

19 September 2026. OpenAI GPT-6 (Codex), for Edward Baker.

**Status:** exact free-field constructions and operator limits; no interacting
reflection-positivity, endpoint-protection, arithmetic, or RH claim. This
continues Claude's common-reference network and resolves the free ultraviolet
question raised in the [18 September review](../reviews/review_codex_2026-09-18.md).
The manuscript remains at its archived version 0.8.

The new results are an explicit angular regulator realized by smeared endpoint
fields; its finite positive Gram kernel; a closed positive difference form in
the limit of zero smearing; and a projected free scalar boundary model for the
previously auxiliary gamma determinant. The covariance itself has no finite
positive limit after the natural contact subtraction. These are distinct
statements, not two descriptions of one positive pairing.

## 1. Use the full three-dimensional defect before restricting to a ray

Normalize the free complex scalar propagator to
\(\langle\bar q(X)q(Y)\rangle=|X-Y|^{-1}\); color multiplicity and the usual
propagator constant are stripped off. Write a defect point as
\(X=e^x\Omega\), \(\Omega\in S^2\), and rescale
\(\varphi(x,\Omega)=e^{x/2}q(e^x\Omega)\). The free cylinder covariance is

\[
C(u,\Omega\cdot\Omega')=
\frac1{\sqrt{2(\cosh u-\Omega\cdot\Omega')}}
=\sum_{\ell\ge0}e^{-(\ell+1/2)|u|}P_\ell(\Omega\cdot\Omega'),
\quad u=x-y.                                                   \tag{1.1}
\]

For \(u\ne0\), this is the [Legendre generating
function](https://dlmf.nist.gov/18.12.E11). The [spherical harmonic addition
theorem](https://dlmf.nist.gov/14.30.E9) identifies the positive angular
components. The radial cylinder is a standard description of a conformal field
on \(\mathbb R^3\); see, for example, [Brower et al.,
arXiv:2006.15636](https://arxiv.org/abs/2006.15636). All formulas below are
derived from (1.1), without importing an interacting lattice result.

Fix an axis \(e\) in the defect and \(0\le\rho<1\). The Poisson profile on the
unit sphere and its even average are

\[
P_\rho(\mu)=\frac{1-\rho^2}{4\pi(1-2\rho\mu+\rho^2)^{3/2}},\qquad
h_\rho(\Omega)=\tfrac12[P_\rho(e\cdot\Omega)+P_\rho(-e\cdot\Omega)]. \tag{1.2}
\]

Both integrate to one. Differentiating the generating function shows
\(P_\rho(\mu)=\sum_{\ell\ge0}(2\ell+1)\rho^\ell P_\ell(\mu)/(4\pi)\).
Therefore \(h_\rho\) has multiplier \(\rho^\ell\) for even \(\ell\), zero for
odd \(\ell\), and only azimuthal number \(m=0\) relative to \(e\).

Define the actual smeared free field
\[
\varphi_\rho(x)=\int_{S^2}h_\rho(\Omega)\varphi(x,\Omega)\,d\Omega.
\]
The addition theorem, followed by the geometric sum, gives its covariance
\[
C_\rho(u)=\langle\bar\varphi_\rho(x)\varphi_\rho(y)\rangle
=\sum_{n\ge0}\rho^{4n}e^{-a_n|u|}
=\frac{e^{-|u|/2}}{1-\rho^4e^{-2|u|}},\qquad a_n=2n+\tfrac12.       \tag{1.3}
\]

For fixed \(\rho<1\), \(C_\rho(0)=(1-\rho^4)^{-1}\) is finite. The sphere
smearing makes the coincident-radius free norm integrable: the remaining
angular singularity is inverse distance on a two-dimensional surface. The
mode expansion also proves this directly, including positivity.

As \(\rho\uparrow1\), \(h_\rho\) tends to the half-sum of the two point masses
at \(\pm e\). Thus \(\varphi_\rho(x)\) formally tends to
\(\sqrt r[q(re)+q(-re)]/2\), precisely the normalization of the earlier even
endpoint field. For every separated pair, \(C_\rho(u)\uparrow n_\gamma(|u|)\).
No claim of a finite point-field limit accompanies this statement.

## 2. The same smearing can be assigned common-reference Wilson transports

For every direction \(\Omega\), let \(\Phi_{r\Omega}=W[0\leftarrow r\Omega]q(r\Omega)\)
use the upper semicircle in the plane spanned by \(\Omega\) and the normal
\(e_3\), directed toward the origin. Then
\[
\Psi_\rho(x)=e^{x/2}\int h_\rho(\Omega)\Phi_{e^x\Omega}\,d\Omega             \tag{2.1}
\]
is a color vector at one reference point. A reflected color contraction is
gauge invariant. At free order the transports are identity and (2.1) has
exactly (1.3) as its pairing. At nonzero coupling, renormalization of the Wilson
operators, the physical adjoint/reflection, and positivity remain to be proved.
Angular smearing only resolves the free endpoint singularity here.

The useful common bulk condition survives the angular smearing. In the
conventions of the transport note, a contour is
\[
X(\theta)=\frac r2[(1+\cos\theta)\Omega+\sin\theta\,e_3],\quad0\le\theta\le\pi.
\]
Its bulk supersymmetry condition is
\[
\epsilon_s=-\frac r2(1+J)\Gamma_\Omega\epsilon_c,\qquad J=i\Gamma_I\Gamma_3.
\]
Since \([J,\Gamma_\Omega]=0\) for every defect tangent direction, the same
\(\epsilon_s=0\), \(J\epsilon_c=-\epsilon_c\) solves it for all r and all
\(\Omega\). The proof uses only the Clifford relations. It is not a solution
of the defect endpoint variations, an assertion about physical spinor reality,
or a count of preserved charges.

## 3. Which positivity survives removal of the angular regulator?

Use \(\widehat f(\tau)=\int e^{-i\tau x}f(x)\,dx\), with Parseval factor
\(1/(2\pi)\). For \(\rho<1\), the integrable kernel has nonnegative transform
\[
S_\rho(\tau)=\sum_{n\ge0}\rho^{4n}\frac{2a_n}{a_n^2+\tau^2}.          \tag{3.1}
\]
Consequently the covariance norm of \(\int f(x)\varphi_\rho(x)dx\) is finite
and nonnegative for \(f\in L^2\). This is a genuine regulated free Gram
construction, established independently of an interacting OS hypothesis.

Set \(z=\rho^4\). Its divergent contact mass is
\[
M_\rho=S_\rho(0)=\sum_{n\ge0}\frac{z^n}{n+1/4}
=-\log(1-z)-\gamma_E-\psi(1/4)+o(1).                                \tag{3.2}
\]
To prove the constant, subtract \(\sum z^n/(n+1)=-\log(1-z)/z\);
the remaining difference is absolutely summable at z=1 and equals
\(\psi(1)-\psi(1/4)\).

For the convolution operator \(T_\rho f=C_\rho*f\), define
\[
A_\rho=M_\rho I-T_\rho,\qquad
b_\rho(\tau^2)=M_\rho-S_\rho(\tau)
=2\sum_{n\ge0}\rho^{4n}\frac{\tau^2}{a_n(a_n^2+\tau^2)}\ge0.          \tag{3.3}
\]
Equivalently,
\[
\mathcal E_\rho[f]=\langle f,A_\rho f\rangle
=\frac12\iint C_\rho(u)|f(x+u)-f(x)|^2\,dx\,du.                     \tag{3.4}
\]
Both identities follow by Fubini for the integrable regulated kernel. The
positivity of (3.4) uses the **pointwise nonnegativity** of this free kernel;
positive definiteness of an arbitrary interacting covariance alone would not
justify this step.

Monotone convergence as \(\rho\uparrow1\) now yields the closed nonnegative form
\[
\mathcal E[f]=\frac1{2\pi}\int b(\tau^2)|\widehat f(\tau)|^2\,d\tau
=\frac12\iint n_\gamma(|u|)|f(x+u)-f(x)|^2\,dx\,du,                  \tag{3.5}
\]
\[
b(\tau^2)=\Re\psi(\tfrac14+i\tau/2)-\psi(\tfrac14),\qquad
\mathcal D(\mathcal E)=\left\{f\in L^2:\int b(\tau^2)|\widehat f|^2<\infty\right\}.
\]
This form is closed because its graph norm is a weighted Fourier L2 norm.
The form domain is equivalently given by the logarithmic weight
\(\log(2+|\tau|)\). The associated operator is \(A=b(-\partial_x^2)\), with
operator domain defined using \(b^2\). For every \(\lambda>0\), dominated
convergence of \((\lambda+b_\rho)^{-1}\) proves strong resolvent convergence
\(A_\rho\to A\). No numerical check substitutes for these domain arguments.

The covariance has a different limit. For Schwartz f,
\[
\langle f,T_\rho f\rangle-M_\rho\|f\|_2^2\longrightarrow-\mathcal E[f]. \tag{3.6}
\]
Adding a finite delta contact c produces multiplier \(c-b(\tau^2)\), which
is eventually negative. Among extensions preserving the original scaling
degree of \(1/|u|\), the only local ambiguity is a delta contact. Thus there is
no positive-type extension within that class. Extra derivative contacts would
define a different, higher-order target.

Multiplicative normalization also has a precise but different outcome:
\(T_\rho/M_\rho\to I\) strongly on L2, since
\(0\le S_\rho(\tau)/M_\rho\le1\) and the ratio tends pointwise to one.
It retains a white-noise covariance, losing the nontrivial archimedean part at
leading order. The finite nontrivial positive limit obtained here is (3.5).

A separate radial reflection would give the finite Hankel Gram kernel
\(n_\gamma(s+t)=\sum_n e^{-a_ns}e^{-a_nt}\), s,t>0. This is an ordinary
positive tower pairing, but it depends on the sum of the variables; it cannot
be silently substituted for the translation-invariant convolution kernel.

## 4. The fixed tower is a free cylinder mode sector

For a conformally coupled scalar on the unit cylinder \(\mathbb R\times S^2\),
the angular frequency operator is
\[
H=\sqrt{-\Delta_{S^2}+\tfrac14},\qquad HY_{\ell m}=(\ell+\tfrac12)Y_{\ell m}.
\]
The curvature term is \(\xi R=(1/8)2=1/4\). Restricting to the subspace
\(\mathscr H_{\mathrm{ax},+}=\overline{\mathrm{span}}\{Y_{2n,0}\}\) gives the
simple spectrum \(a_n=2n+1/2\) and heat trace n_gamma. This is a concrete free
mode interpretation of the fixed tower in the transport note, on a
three-dimensional defect throughout.

There are two distinct appearances of that spectrum. For the smeared
covariance, the pole values of the normalized spherical harmonics cancel the
oscillator covariance factor: \(4\pi|Y_{\ell0}(e)|^2/(2\ell+1)=1\). Thus
\(C_\rho(u)=\langle v_\rho,e^{-|u|H}v_\rho\rangle\) with components
\((v_\rho)_n=\rho^{2n}\). As \(\rho\uparrow1\), this vector ceases to belong
to ell2. Separately, the heat trace sums one copy of each eigenvalue in the
projected subspace. The equality of these sums does not turn the divergent
limiting vector into a state.

## 5. A Robin boundary Gaussian produces the shifted determinant ratio

Take a single complex free field on the half-cylinder t≥0, valued in
\(\mathscr H_{\mathrm{ax},+}\), with explicit cylinder action
\[
I_p[\phi]=\frac12\int_0^\infty
\big(\|\partial_t\phi\|^2+\|H\phi\|^2\big)dt+\frac p2\|\phi(0)\|^2.
                                                                    \tag{5.1}
\]
Initially p is a real boundary parameter, p>−1/2. This action specifies its
boundary convention; a Weyl transformation of a flat-space action with a
boundary must also transform its boundary terms, rather than assuming they
vanish.

At fixed boundary value h, the decaying extension is \(\phi(t)=e^{-tH}h\).
Its bulk action is \(\langle h,Hh\rangle/2\); the boundary effective action is
\(\langle h,(H+p)h\rangle/2\). Equivalently the Dirichlet-to-Neumann map is H,
and variation gives the Robin boundary operator \(-\partial_t+p\).
Integrating a complex mode with measure \(d^2h/\pi\) gives \(2/(a_n+p)\).
For N projected modes the p-dependent boundary partition factor is therefore
\[
Z_N(p)=\prod_{n<N}\frac2{a_n+p},
\]
up to p-independent Dirichlet bulk factors that cancel in all ratios below.
For real p,p0>omega−1/2 and omega≥0, the normalized ratio converges absolutely:
\[
\frac{Z_N(p-\omega)/Z_N(p+\omega)}{Z_N(p_0-\omega)/Z_N(p_0+\omega)}
\longrightarrow
\frac{\Gamma(\tfrac14+\tfrac{p-\omega}2)/\Gamma(\tfrac14+\tfrac{p+\omega}2)}
     {\Gamma(\tfrac14+\tfrac{p_0-\omega}2)/\Gamma(\tfrac14+\tfrac{p_0+\omega}2)}.
                                                                    \tag{5.2}
\]
The unnormalized finite-N ratio grows like \(N^\omega\); it is not a finite
partition ratio without a counterterm or normalization. With the same zeta
and scale convention as the transport note,
\[
D(p)=\det{}_\zeta((H+p)/2)=\frac{\sqrt{2\pi}}{\Gamma(1/4+p/2)},\qquad
Z_\zeta(p)=D(p)^{-1},
\]
\[
K^\Gamma_\omega(p)=\pi^\omega\frac{Z_\zeta(p-\omega)}{Z_\zeta(p+\omega)}.
                                                                    \tag{5.3}
\]
The determinant identity uses [DLMF 25.11.18](https://dlmf.nist.gov/25.11.E18).
The conductor factor pi^omega remains supplied. One real scalar would give
the square root of this partition ratio; multiple complex species give its
corresponding power. Statistics and multiplicities matter.

This gives a free boundary mechanism for opposite shifts on a fixed space,
instead of a fractional spatial dimension. It is still an **auxiliary model**,
not a localized determinant of the D3–D5 network. In particular:

- Angular smearing samples an axial even channel but does not delete all other
  modes from the theory's partition function. A local Robin mass on the full
  sphere shifts every m, giving multiplicity 2ell+1 rather than one. To embed
  (5.1) in the unprojected theory one needs a justified sector restriction or a
  boundary projector, which is nonlocal in angle. Interactions need not preserve
  this truncation.
- Here p is a boundary mass parameter. Identifying its analytic continuation
  with the transfer's Laplace frequency still needs a dynamical dictionary.
- The Robin response itself is \((H+p)^{-1}\), of Stieltjes type. The partition
  ratio is a different observable. Neither defines the complete causal
  scattering system or establishes its passivity.
- Prime atoms, the prescribed contact normalization, and the rational pole
  sector are absent. They cannot be supplied by simply multiplying in zeta.

## 6. Consequence for the next calculation

The first free-domain problem is now explicit: (1.3) is the regulated Gram
kernel; (3.5) is its associated finite positive difference form; (3.6) excludes
the previously claimed contact-renormalized positive covariance. The geometric
common-charge result survives in all smearing directions.

The next discriminating question is whether the actual defect endpoint
conditions admit the angular family (2.1) with one physical Q and one endpoint
polarization, followed by the correct antilinear reflection. A free odd-scalar
reflection diagnostic should precede a full interacting OS audit. Independently,
the boundary model makes the determinant question concrete: can the physical
construction select the one-copy even axial sector and generate the Robin
deformation, or does it necessarily retain the full angular multiplicity?

Do not calculate a large set of loops assuming those selections or protection.
The earlier backtracking spike and the scalar-sign junction still require the
corrections identified in the review; neither is evaluated afresh in this note.

The standard-library [check program](../numerics/check_angular_regulator.py)
contains 185 finite cases: sphere-profile normalization and moments, genuine
double sphere quadrature, finite Gram matrices, real/Fourier difference energies,
cutoff asymptotics, rotated bulk Clifford conditions, and Gaussian/Robin
determinant identities. The proofs and domain statements are given above;
passing numerical cases is not a physical positivity certificate.

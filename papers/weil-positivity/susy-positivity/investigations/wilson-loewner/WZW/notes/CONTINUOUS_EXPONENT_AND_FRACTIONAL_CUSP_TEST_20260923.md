# Continuous exponent and fractional cusp-field test

23 September 2026. Prepared for Edward Baker with LLM assistance.

**Model:** GPT-6 (Codex; developer-provided identity).  
**Effort:** not exposed; not inferred.  
**Status:** a specified positive memory field passes the leading continuous-exponent test but fails the arithmetic transfer. An elementary obstruction is proved for scalar complete-Bernstein substitutions of the established modular channel. No general geometric-deformation obstruction, variable-shift realization, or RH result is claimed.

This executes the next test proposed after the [modular Hodge/cusp-coupling investigation](MODULAR_HODGE_SCATTERING_AND_CUSP_COUPLING_TEST_20260923.md). The [diagnostic](../numerics/check_fractional_cusp.py), [record](../numerics/records/fractional-cusp-20260923.json), and [same-assistant audit](../reviews/review_codex_fractional_cusp_20260923.md) accompany it. This is a research addendum, separate from the manuscript.

## 1. Result and the candidate selection

A continuous short-delay exponent is physically available from a local weighted diffusion field. Applied as a memory clock to the modular channel, it gives the candidate

\[
 S_\beta(p)=K\bigl(\psi_\beta(p)\bigr),\qquad
 K(p)=\frac{\xi(p)}{\xi(p+1)},\qquad
 \psi_\beta(p)=2\pi\left(\frac p{2\pi}\right)^\beta,
 \quad 0<\beta\le1.
\]

The original channel is recovered at beta=1, while

\[
 S_\beta(p)\sim(2\pi/p)^{\beta/2},\qquad p\to+\infty.
\]

Thus the leading exponent and amplitude agree with the arithmetic family at omega=beta/2. This candidate passes the first necessary test, including in the direction toward shifts below one half.

It nevertheless fails at the next algebraic term, at boundary modulus, at the first arithmetic delay, and at the zero-shift endpoint. A general positive-relaxation clock cannot repair the modulus problem: among complete-Bernstein substitutions, only a pure linear clock can preserve this scalar channel's unit boundary modulus, and a linear clock leaves its exponent equal to one half.

This conclusion concerns a precisely specified field/clock construction. It does not rule out coherent additional channels, a different global automorphic geometry, or a deformation that changes orbit amplitudes without replacing the propagation clock.

## 2. The necessary front condition

Retain the earlier definitions

\[
 \xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad
 K_\omega(p)=\frac{\xi(1/2+p-\omega)}{\xi(1/2+p+\omega)}.
\]

For fixed omega>0 and large positive p, the gamma quotient and rational completion give

\[
 K_\omega(p)=\left(\frac{2\pi}{p}\right)^\omega
 \left[1-\frac{7\omega}{2p}+O(p^{-2})
       +O(2^{-p})\right].                                      \tag{1}
\]

The exponentially small term is schematic for fixed omega. The corresponding leading kernel is

\[
 k_\omega(u)\sim A_\omega u^{\omega-1},\qquad
 A_\omega=\frac{(2\pi)^\omega}{\Gamma(\omega)}.
\]

Its first arithmetic translate has coefficient

\[
 c_2(\omega)=\frac{2^\omega-2^{-\omega}}{\sqrt2}
\]

at the fixed location ell=log 2. Changing the exponent alone is not enough: both the archimedean subleading terms and the arithmetic amplitudes must follow the same physical parameter.

### Two native controls that do not pass

A uniform change of geometric time scale gives K(p/kappa), for kappa>0. Its leading behavior is sqrt(2 pi kappa) p^(-1/2). The exponent is unchanged, and the delay log n becomes log n/kappa. This is a uniform scaling test, not a theorem about arbitrary cusp metrics.

Integer field raising also preserves the exponent. The normalized weight-2m constant term, m>=1, is

\[
 K^{[m]}(p)=K(p)\prod_{j=1}^{m-1}\frac{p-(2j+1)}{p+(2j+1)}.       \tag{2}
\]

It follows by applying the raising operator to the incoming and outgoing powers: their coefficients are (sigma)_m and (1-sigma)_m, with sigma=(p+1)/2, followed by the fixed sign (-1)^m. This uses the standard [Eisenstein raising and constant-term formulas of O'Sullivan](https://fsw01.bcc.cuny.edu/cormac.osullivan/Research/Eisenstein-series-Riemann-zeta3.pdf). Each additional factor tends to one at large p. These discrete field changes cannot supply a continuously variable front power. No conclusion about arbitrary real-weight multiplier systems is drawn.

## 3. Independently specified memory field

Fractional powers have local weighted-extension realizations; see [Caffarelli–Silvestre](https://arxiv.org/html/math/0608640). Related extensions apply to semigroup and wave operators, as developed by [Galé–Miana–Stinga](https://arxiv.org/html/1207.7203). The model below is an explicit temporal diffusion version, derived here rather than identified with a fractional spatial Laplacian by notation.

At each boundary/state degree of freedom U(t), attach a half-line field V(t,y), y>0, satisfying

\[
 \partial_t V=\partial_y^2V+\frac{1-2\beta}{y}\partial_yV,
 \qquad V(t,0)=U(t),\qquad V(0,y)=0,\quad 0<\beta<1.             \tag{3}
\]

Choose the solution decaying at infinity in the Laplace domain. This is ordinary diffusion in a graded medium with density/conductivity proportional to y^(1-2 beta); it is not a claim that a manifold has a noninteger topological dimension. Beta is an independent constitutive exponent, with no primes or xi zeros in its definition.

For Re p>0 the normalized solution is

\[
 \widehat V(p,y)=\widehat U(p)W_\beta(\sqrt p\,y),\qquad
 W_\beta(z)=\frac{2^{1-\beta}}{\Gamma(\beta)}z^\beta K_\beta(z),
\]

where K_beta on the right is the modified Bessel function, not the arithmetic transfer. Direct differentiation yields

\[
 -\lim_{y\downarrow0}y^{1-2\beta}\partial_y\widehat V
 =d_\beta p^\beta\widehat U,\qquad
 d_\beta=2^{1-2\beta}\frac{\Gamma(1-\beta)}{\Gamma(\beta)}.        \tag{4}
\]

With c_beta=(2 pi)^(1-beta)/d_beta, the measured flux
Y=-c_beta lim y^(1-2 beta) V_y therefore has admittance psi_beta(p).

The scale 2 pi is one favorable global time calibration, chosen to match the leading archimedean amplitude for all beta. It is not a derived prime spectrum or a fit to the full transfer. The failures below persist with any positive scale. At beta=1 the field in (3) becomes singular; we define the endpoint by the admittance limit psi_1(p)=p, recovering the original time derivative. We claim continuity of this response family, not a regular family of weighted media at that endpoint.

The field has its own positive energy identity. For sufficiently regular zero-initial data,

\[
 E_\beta(t)=\frac{c_\beta}{2}\int_0^\infty
 y^{1-2\beta}|V(t,y)|^2dy,
\]

\[
 \operatorname{Re}(\overline U Y)=E_\beta'(t)
 +c_\beta\int_0^\infty y^{1-2\beta}|V_y|^2dy.                  \tag{5}
\]

The weight is the prescribed material density. It has not been chosen from the arithmetic transfer to manufacture a norm.

An equivalent positive relaxation representation is

\[
 \psi_\beta(p)=\int_0^\infty\frac{p}{p+r}\,\mu_\beta(r)dr,
 \qquad
 \mu_\beta(r)=(2\pi)^{1-\beta}\frac{\sin\pi\beta}{\pi}r^{\beta-1}.
                                                                    \tag{6}
\]

For each r, set dot x_r+r x_r=U and Y=integral mu_beta dot x_r dr. Then the supply is the derivative of (1/2) integral mu_beta r |x_r|^2 dr plus integral mu_beta |dot x_r|^2 dr. This also proves positivity directly. Complete-Bernstein functions and their positive string/extension realizations are treated in [Kwaśnicki–Mucha, Sections 2–5](https://arxiv.org/html/1707.02475).

### What is being assembled and what is not

The bounded test uses a common clock substitution in the previously established modular input/output problem: replace its Laplace parameter p by the admittance psi_beta(p), keeping its geometric matching relations. A driven first-order propagation equation then sends a segment of length v to exp(-v psi_beta(p)), and the resulting response is S_beta=K composed with psi_beta. Inputs have zero initial state. There is no p^(beta-1) initial-data prefactor; that belongs to a different fractional initial-value problem.

Equivalently, every native propagation delay is randomized by the same independent stable clock. This prescription defines the response being tested and its constituent positive memory law. It does not yet establish a local fractional field theory on the entire modular quotient with unchanged free asymptotic radiation ports. That additional geometric realization is unnecessary to the exclusion: even this favorable composed response fails the arithmetic requirements.

Causality and the ordinary input/output contraction are nevertheless rigorous at the response level. For 0<beta<=1, psi_beta maps the right half-plane into itself. The previously established K is a nonconstant inner function there. Hence S_beta is analytic and contractive in that half-plane and acts causally on unweighted radiation L2. For inputs supported on (0,L),

\[
 \|f\|^2-\|1_{(0,L)}S_\beta f\|^2
 =\frac1{2\pi}\int_{\mathbb R}(1-|S_\beta(i\nu)|^2)|\widehat f(\nu)|^2d\nu
 +\|1_{(L,\infty)}S_\beta f\|^2.                              \tag{7}
\]

Here the Fourier transform has no unitary prefactor. Equation (7) identifies spectral loss and future output; it does not assert that we have evaluated the entire coupled modular field energy. The positivity of (5), Schur contractivity in (7), and exact arithmetic matching are separate tests.

## 4. The front passes; its next term fails

Put omega=beta/2. Substitution into the half-shift expansion gives

\[
 S_\beta(p)=\left(\frac{2\pi}{p}\right)^{\beta/2}
 \left[1-\frac74(2\pi)^{\beta-1}p^{-\beta}
 +O(p^{-2\beta})+O(2^{-\psi_\beta(p)})\right].                 \tag{8}
\]

The exponent and leading coefficient agree with (1). At beta=1/2 the numerically evaluated effective exponent at p=10^10 is 0.2499965093, approaching the required 1/4. The relative amplitude tends to one as predicted.

For beta<1 the next relative correction in (8) is p^(-beta), whereas the arithmetic correction is -7 beta/(4p). The nonzero fractional-order term already prevents equality before prime delays are examined.

The parameter tangent also passes only its leading term:

\[
 \left.\partial_\beta\log S_\beta(p)\right|_{1}
 =p\log\frac p{2\pi}\,\frac{K'(p)}{K(p)},\qquad
 \left.\partial_\beta\log K_{\beta/2}(p)\right|_{1}
 =-\tfrac12 a_{1/2}(p).                                    \tag{9}
\]

Both behave as -1/2 log(p/(2 pi)) at large positive p. They are different functions:

| p | memory tangent | arithmetic tangent |
|---:|---:|---:|
| 2 | 0.1037685363 | -0.09172846338 |
| 4 | 0.07761151851 | -0.1801739891 |
| 8 | -0.06977854903 | -0.3387146766 |

The exponent condition fixes the local clock derivative domega/dbeta=1/2. An alternative constant parameter rescaling cannot independently repair (9).

## 5. A scalar positive-clock obstruction

For beta<1 and nu nonzero,

\[
 \operatorname{Re}\psi_\beta(i\nu)
 =(2\pi)^{1-\beta}|\nu|^\beta\cos(\pi\beta/2)>0.
\]

A nonconstant inner function has modulus strictly below one at every interior point. Thus

\[
 |S_\beta(i\nu)|<1,
 \qquad |K_{\beta/2}(i\nu)|=1
\]

where the arithmetic boundary value is defined. The latter equality follows from the functional equation and conjugation, independently of any assertion of full-family causality. Isolated exceptional points do not affect the L2 comparison. For beta=1/2 the native moduli at nu=1, 5 and 20 are approximately 0.9206486, 0.8260941 and 0.6715768, respectively.

There is a useful bounded generalization. Let

\[
 \psi(p)=a+bp+\int_{(0,\infty)}\frac{p}{p+r}\,\mu(dr),
 \quad a,b\ge0,\quad\int(1+r)^{-1}\mu(dr)<\infty.              \tag{10}
\]

For every nonzero nu,

\[
 \operatorname{Re}\psi(i\nu)
 =a+\int\frac{\nu^2}{r^2+\nu^2}\,\mu(dr).                    \tag{11}
\]

If a>0 or mu is nonzero, this is strictly positive. Consequently K composed with psi cannot have the arithmetic unit-modulus boundary values. The only nondegenerate survivor in this complete-Bernstein class is psi(p)=bp, b>0; its front exponent is still 1/2. The degenerate zero clock returns K(0)=1 and supplies no continuous family. This proof concerns scalar clock composition, not every system with a passive bath, nor arbitrary matrix-valued or coherent scattering.

Frequency-dependent amplification or an adjoint quotient might remove the observed attenuation, but would define a new preparation/readout. No causal physical implementation of that repair is supplied here.

## 6. What happens to the first prime

The native modular Euler factor is

\[
 \frac{\zeta(p)}{\zeta(p+1)}
 =\sum_{n\ge1}\frac{\varphi_E(n)}{n}e^{-p\log n}.
\]

Clock substitution leaves its totient weights fixed and replaces each sharp delay by exp(-log n psi_beta(p)). This is the Laplace transform of a positive stable delay distribution. The probabilistic interpretation of such clocks is standard; see [Kwaśnicki–Mucha, Section 9.1](https://arxiv.org/html/1707.02475).

At beta=1/2 the density corresponding to a native delay v is explicit:

\[
 \ell_v(u)=\frac{v}{\sqrt2\,u^{3/2}}
 \exp\left(-\frac{\pi v^2}{2u}\right),\qquad u>0,              \tag{12}
\]

\[
 \int_0^\infty e^{-pu}\ell_v(u)du=e^{-v\sqrt{2\pi p}}.
\]

For v=log 2, the probability that the delay is already completed by u=1/2 is

\[
 \operatorname{erfc}(\sqrt\pi\log2)
 =0.0823055991480057\ldots.
\]

This is a property of the propagation-delay distribution, not an energy fraction in the full coherent response.

There is also a direct signed-response comparison. With the previous closed prime-free half-shift kernel

\[
 k_0(r)=\frac{2(2e^{-2r}-1)}{\sqrt{1-e^{-2r}}},
\]

the n=2 contribution after subordination is

\[
 j_2(u)=\tfrac12\int_0^\infty k_0(r)\ell_{r+\log2}(u)dr.       \tag{13}
\]

It is smooth, indeed real analytic, at every positive u. The Gaussian decay in (12) dominates the large-r tail and every locally differentiated integrand. It is already nonzero before log 2: j_2(1/4)=0.06848784893 and j_2(1/2)=0.1310802608. In contrast, the arithmetic n=2 contribution at omega=1/4 begins only at log 2 and diverges there as c_2(1/4) A_(1/4) epsilon^(-3/4).

| epsilon | native j_2(log 2+epsilon) | arithmetic first-prime increment |
|---:|---:|---:|
| 10^(-4) | 0.1262676545 | 107.5136697 |
| 10^(-6) | 0.1262746899 | 3401.059188 |

These are contributions from the first nontrivial Euler term, not the entire response. The whole subordinated kernel at beta=1/2 is also smooth for u>0: the arithmetic sum has at most exponential integrated growth in its native delay, which is dominated locally by the Gaussian in (12). Thus a cancellation among later terms cannot recreate the missing fractional front at log 2.

The first Euler coefficient tangent makes the distinction explicit. After separating the common archimedean factor, the native n=2 term is (1/2) exp(-ell psi_beta(p)). Its beta derivative at one is

\[
 -\tfrac12\ell p\log(p/(2\pi))e^{-\ell p},
\]

whereas the arithmetic derivative of c_2(beta/2) exp(-ell p) is

\[
 \tfrac34\ell e^{-\ell p}.
\]

The native clock changes delay propagation; the target changes amplitude at a fixed delay. These are not the same deformation.

## 7. The other endpoint and a restriction on asymptotic-only changes

Near p=0,

\[
 K(p)=1+\kappa_1p+O(p^2),\qquad
 \kappa_1=\log(4\pi)-2-\gamma_E=-0.04619141793\ldots.
\]

Hence S_beta has a nonzero p^beta term for noninteger beta, while K_(beta/2) is analytic at zero. This is another exact local obstruction. Also, for fixed nonzero boundary frequency,

\[
 \lim_{\beta\downarrow0}S_\beta(i\nu)=K(2\pi)
 =0.7601621206428189\ldots,
\]

so the strong L2 limit is that constant times identity, rather than the arithmetic K_0=I. Contractive domination justifies the strong limit.

Even a more favorable *formal* change that replaced the entire archimedean factor while leaving the totient orbit weights untouched would retain first coefficient 1/2. The arithmetic coefficient varies with omega and tends to zero at omega=0. This is an algebraic restriction on changes that factor through the same Euler series, not a claimed classification of all metric perturbations. It explains why a purely archimedean adjustment is insufficient.

## 8. What this suggests next

The test has separated two requirements that previously looked like one. A local positive field can generate a variable front exponent. The arithmetic evolution additionally needs a unitary change of orbit amplitudes at unchanged logarithmic delays. Positive scalar clock composition cannot do both.

The next useful question is whether a global unitary deformation of the arithmetic channel can vary those orbit amplitudes while retaining their locations and simultaneously varying the archimedean factor. Any proposed model should first derive its n=2 amplitude and verify the required derivative, rather than be developed solely because it has a fractional leading power. The expected first-coefficient derivative at half shift is dc_2/domega=(3/2)log 2; the complete transfer tangent must also reproduce the gamma and rational terms. A model satisfying those conditions has not been found in this test.

## 9. Validation and limitations

The separate numerical record contains 80 passing floating controls and no exact rational cases. These cover uniform scale and integer raising controls, the Bessel differential equation and boundary flux, an independent positive relaxation integral, a bulk-energy identity, leading and subleading asymptotics, the parameter tangent, boundary modulus, normalized stable-delay densities, early arrival, first-prime behavior, a precision refinement, the low-frequency branch, the zero-order endpoint, and the general complete-Bernstein dissipation identity.

The run used Python 3.10.0 and mpmath 1.3.0, with 50 decimal digits and 65 for a first-prime integral refinement. Its program hash is stored in the record. No xi-zero table, random simulation, or interval arithmetic is used. Passing controls reproduce the stated matching of the leading term and the subsequent exclusions; they do not mean the arithmetic realization test succeeded.

The analytical obstructions do not depend on finite numerical samples. The auxiliary memory field is explicit and positive; a full local assembly on the modular quotient with fixed free ports has not been established. The response-level test already fails, so this gap is not concealed by a claim of a new physical arithmetic realization. The audit is by the same assistant, not an independent specialist. Earlier diagnostics, manuscript TeX and PDFs remain unchanged.

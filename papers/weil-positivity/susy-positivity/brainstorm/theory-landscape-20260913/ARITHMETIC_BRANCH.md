# Arithmetic and adelic architectures for a positive bulk Weil pairing

This is a conceptual selection exercise, not a proof of Weil positivity. It distinguishes existing arithmetic constructions from deductions and proposed physical extensions. The proposed extensions have not received independent specialist review.

## Assessment and ranking

The strongest arithmetic architecture is a **semilocal adelic Hilbert space with a polarization and a coupling-dependent Hermitian metric**. It already incorporates the archimedean factor, finite sets of primes, all repetitions, a continuous scaling coordinate, and transitions when places are added. It is a better arithmetic starting point than independent positive prime oscillators. It is not yet a theory whose positive norm equals the full Weil form.

A concrete bridge to the ground-state-metric investigation is available: the entire pole-free Weil operator is the logarithmic normal derivative of an unconditional positive semilocal local-factor metric. Equivalently, it is the phase derivative of a unitary local-factor scattering multiplier. This locates the missing step: **derive a positive norm from this generally indefinite metric derivative together with the pole residues**. The scalar metric is locally flat in its holomorphic arithmetic parameter, so its existence alone does not supply nontrivial tt* dynamics.

My ranking within this arithmetic branch is:

1. Semilocal polarized Hilbert geometry as the arithmetic component of a theory with ground-state metric dynamics.
2. A cohomological/Hodge realization of the explicit formula, tested first where the arithmetic geometry is known.
3. Adelic scalar or defect fields based on Tate factors, with independently checked Hamiltonian positivity.
4. Bost–Connes dynamics as a source of arithmetic defects and operations; not its partition-function identity as a positivity argument.
5. Selberg or dynamical supersymmetric trace models as comparison laboratories.

These are research architectures, not completed candidate theories. No cited result supplies the required positive bulk norm identity for unrestricted inputs at arbitrary interval length.

## 1. Target and diagnostic distinctions

Let \(F=E_Lf\) be the zero extension from \(I_L=(-L/2,L/2)\). The target is

\[
Q_L[f]=\frac1{2\pi}\int_{\mathbb R}
\left(\operatorname{Re}\psi\left(\frac14+\frac{i\tau}{2}\right)-\log\pi\right)
|\widehat F(\tau)|^2d\tau
-\sum_{m\log p<L}(\log p)p^{-m/2}
\langle f,(T_{m\log p}+T_{m\log p}^*)f\rangle+P[f],
\]

where \(P[f]=2|C(f)|^2-2|S(f)|^2\), with \(C,S\) smearing against \(\cosh(x/2),\sinh(x/2)\). The pole kernel \(2\cosh((x-y)/2)\) is rank two on each interval. The form domain has Fourier weight \(\log(2+|\tau|)\).

The current obstruction excludes responses of the form \(s b^*(sI+M)^{-1}b\) replacing finitely many original gamma channels, under the precise hypotheses in the audit. It does not exclude all Gaussian or interacting fields. The superspace Ward theorem protects the pairing at fixed differential, metric, and prepared sources; a new arithmetic mechanism must change relevant data rather than invoke that protection.

The desired conclusion has the type

\[
Q_L[f]=\|\mathcal O_L(f)\Omega\|^2
\quad\text{or}\quad
Q_L[f]=\inf_{\Phi\mapsto f}\mathcal E[\Phi],\qquad \mathcal E\ge0.
\]

A positive partition function, a character amplitude, a determinant ratio, and a regularized supertrace are different objects. An identity involving one does not establish this norm identity.

## 2. Positive semilocal metrics and an exact arithmetic derivative

### Existing constructions

**Literature.** Connes–Consani–Moscovici construct a determinate moment problem and Jacobi operator from the positive measure

\[
d\mu_S(\tau)=\left|\prod_{v\in S}L_v(1/2+i\tau)\right|^2d\tau,
\qquad S=\{\infty\}\cup S_f,
\]

up to normalization and an irrelevant archimedean phase convention. The normalized archimedean density is \((2\pi)^{-3/2}|\Gamma(1/4+i\tau/2)|^2\), with characteristic function \((\cosh x)^{-1/2}\). Their one-prime moments and Jacobi data admit series in \(1/p\); Lambert series arise naturally. No zeta-zero assumption defines this metric. [Connes–Consani–Moscovici, On q-series and the moment problem associated to local factors, 2024](https://arxiv.org/html/2403.01247v1)

**Literature.** The semilocal prolate framework gives Sonin spaces compatible with increasing the set of places and relates them to Hilbert spaces of entire functions. This supplies an infinite-dimensional structure and a meaningful operation of adding primes. [Connes–Consani–Moscovici, Zeta zeros and prolate wave operators, 2024](https://arxiv.org/abs/2310.18423)

### Exact bridge derived for this survey

Use the unnormalized completed local product

\[
\Lambda_S(z)=\pi^{-z/2}\Gamma(z/2)
\prod_{p\in S_f}(1-p^{-z})^{-1},\qquad
w_{S,\sigma}(\tau)=|\Lambda_S(\sigma+i\tau)|^2,\quad \sigma>0.
\]

Only finitely many prime factors occur. Logarithmic differentiation, with convergent repetition sums for each prime, gives

\[
\boxed{\left.\partial_\sigma\log w_{S,\sigma}(\tau)\right|_{\sigma=1/2}
=\operatorname{Re}\psi\left(\frac14+\frac{i\tau}{2}\right)-\log\pi
-2\sum_{p\in S_f,m\ge1}(\log p)p^{-m/2}
\cos(m\log p\,\tau).}
\]

If \(S_f\) contains every prime with \(\log p<L\), interval compression removes all inactive delays, including long repetitions and primes added beyond the support cutoff. Consequently

\[
\boxed{Q_L[f]-P[f]=\frac1{2\pi}\int
\left.\partial_\sigma\log w_{S,\sigma}(\tau)\right|_{1/2}
|\widehat F(\tau)|^2d\tau.}
\]

This is the complete pole-free form, not a high-frequency approximation.

For a fixed smooth core define, with \(\sigma_0=1/2\),

\[
\mathfrak g_\sigma(f,h)=\frac1{2\pi}\int
\frac{w_{S,\sigma}(\tau)}{w_{S,\sigma_0}(\tau)}
\overline{\widehat{E_Lf}(\tau)}\widehat{E_Lh}(\tau)d\tau.
\]

Then \(\mathfrak g_{\sigma_0}\) is the ordinary \(L^2\) metric and

\[
\left.\partial_\sigma\mathfrak g_\sigma(f,f)\right|_{\sigma_0}
=Q_L[f]-P[f].
\]

Differentiation is justified directly for \(C_c^\infty(I_L)\). The neighboring metrics have power-weighted Fourier domains, so their common completion needs care; the differentiated form has the logarithmic domain. Normalizing \(w_{S,\sigma}\) to a probability measure would change the derivative by a scalar contact term. The arithmetic normalization must be retained.

There is an equivalent phase formula. Set

\[
u_S(\tau)=\frac{\Lambda_S(1/2+i\tau)}{\Lambda_S(1/2-i\tau)}.
\]

This scalar multiplier has modulus one and

\[
-iu_S^{-1}\partial_\tau u_S
=\left.\partial_\sigma\log w_{S,\sigma}\right|_{1/2}.
\]

Thus the target is a metric connection coefficient and a scattering phase derivative. Positivity of a metric and unitarity of a scattering multiplier do not imply positivity of their derivatives.

The two pole amplitudes do not emerge by simply multiplying \(\Lambda_S(z)\) by \(z(z-1)\): on the critical line

\[
2\operatorname{Re}\left(\frac1z+\frac1{z-1}\right)=0.
\]

The pole form must be recovered through residues, relative cohomology, or physical boundary sectors. It is not an ordinary multiplier produced by this radial derivative.

### Flatness and the source-frame obstruction

**Derived here; also independently identified in the main survey.** For finite \(S\), \(\Lambda_S(z)\) is holomorphic and nonzero in \(\operatorname{Re}z>0\). Hence, pointwise in \(\tau\),

\[
\partial_{\bar z}\partial_z\log|\Lambda_S(z+i\tau)|^2=0.
\]

This scalar metric is locally a holomorphic frame rescaling of a constant metric. Its logarithmic derivative is frame dependent. Transporting sources by the inverse local factor trivializes the metric; keeping the arithmetic sources fixed retains the displayed derivative.

Therefore it would be incorrect to call \(w\) a nontrivial tt* metric merely because it is positive and contains local factors. A candidate theory needs an independently fixed source frame, a nontrivial polarization or quotient, or a non-Abelian/extension structure. Any resulting curvature must be computed; it cannot be identified with the first normal derivative by analogy.

The arithmetic frame is still useful design data, because in that frame the derivative has the exact coefficients, normalization, and support compatibility. The missing physical principle must select and interpret that frame.

**Global completion warning.** The finite-\(S\) derivative identity cannot simply be completed by taking a pointwise Euler product on the critical line. The completed entire function obeys \(\xi(s)=\xi(1-s)\) and the usual reality relation. Away from its zeros, \(\xi(1/2+i\tau)\) is real and \(\xi'/\xi\) there is purely imaginary, so

\[
\left.\partial_\sigma\log|\xi(\sigma+i\tau)|^2\right|_{\sigma=1/2}=0
\]

pointwise. This plainly is not the Weil distribution. Boundary values, zeros, residues, and the order of limiting and contour operations carry the missing information. Any all-place extension must be derived from a legitimate convergent half-plane or a controlled distributional construction, as in the background's causal setup, rather than replacing the finite product by an analytically continued scalar inside the displayed integral.

### A controlled Toda extension, not yet a tt* theory

**Derived here.** At finite \(S\) let

\[
m_j(u)=\int\tau^j e^{u\tau}d\mu_S(\tau),\qquad
\tau_n(u)=\det[m_{i+j}(u)]_{i,j=0}^{n-1},\quad\tau_0=1.
\]

The gamma decay gives convergence for real \(|u|<\pi/2\). Positivity of the density implies \(\tau_n>0\). Determinant expansion gives

\[
\tau_n(u)=\frac1{n!}\int_{\mathbb R^n}
\prod_{i<j}(t_i-t_j)^2\prod_{i=1}^n e^{ut_i}d\mu_S(t_i).
\]

The Vandermonde factor couples the eigenvalue variables. Using \(m_j'=m_{j+1}\) and the determinant identity yields

\[
\partial_u^2\log\tau_n=\frac{\tau_{n+1}\tau_{n-1}}{\tau_n^2}.
\]

This is an explicit positive Toda structure and interacting eigenvalue ensemble. It is not automatically a supersymmetric action, a tt* solution, or the Weil pairing. The same construction works for many positive measures, so it does not uniquely select arithmetic. Its value is as a controlled testbed for the additional polarization and fixed-source structures, not as a positivity proof.

**First proposed test.** Determine whether a genuine polarized relative complex or tt* system derives a norm identity for the boxed normal derivative plus the two pole residues. If it supplies only \(\int|\widehat f|^2w_{S,1/2}\), a Fisher score squared, or a thermal second derivative, it has supplied a different kernel.

## 3. Adelic trace and polarization results: close fit, known gap

**Literature.** In Connes's Hilbert realization, critical zeros occur as an absorption spectrum while possible off-line zeros appear as resonances. The more flexible cohomological/nuclear setting captures all zeros in an explicit trace formula, but automatic positivity is absent. The arithmetic trace identity and a positive spectral Hilbert space are separate accomplishments. [Connes, Trace formula in noncommutative geometry and the zeros of the Riemann zeta function, 1999](https://arxiv.org/abs/math/9811068)

**Literature.** Connes–Consani express the archimedean Weil functional as a positive Sonin-space scaling trace plus an explicit remainder. The positive part is

\[
\operatorname{Tr}(\vartheta(g)S\vartheta(g)^*)
=\|\vartheta(g)S\|_{\mathrm{HS}}^2\ge0,
\]

where \(S\) projects onto even functions whose position and Fourier representatives vanish on \([-1,1]\). Their comparison theorem has specific support and vanishing conditions. It is not equality with the unrestricted complete form, and the remainder cannot be omitted. [Connes–Consani, Weil positivity and trace formula, the archimedean place, 2021](https://alainconnes.org/wp-content/uploads/Selecta.pdf)

**Literature.** Products of local-factor ratios containing the archimedean place are quasi-inner: their relevant off-diagonal Hardy block is compact. Individual nonarchimedean ratios fail this property. The associated semilocal Sonin spaces form an inductive system. Quasi-inner is weaker than inner, and compactness does not give the sign or disappearance of the block. [Connes–Consani, Quasi-inner functions and local factors, 2021](https://arxiv.org/pdf/2008.10974)

**Literature.** The 2025 spectral triples give self-adjoint operators after a quotient with metric formed from a shifted finite Weil matrix. Their determinants have real zeros, but convergence to the Riemann \(\Xi\) function remains open. Subtracting the lowest matrix eigenvalue produces a positive quotient regardless of the sign of that eigenvalue; it does not prove the original matrix positive. [Connes–Consani–Moscovici, Zeta Spectral Triples, 2025](https://arxiv.org/html/2511.22755v1)

**Inference.** The best parts to retain are the arithmetic space, additive Fourier duality, scaling action, residue normalization, and compatibility when places are added. The missing theoretical task is a physical polarization/gluing identity for the whole pairing. Adopting spectral convergence numerics as the goal would revert to the program the user wishes to avoid.

## 4. Polarized cohomology: strongest conceptual fit, largest construction gap

**Literature.** Deninger's proposed cohomology has a flow generator \(\Theta\), cup product, trace, and antilinear Hodge star defining a positive Hermitian metric. Their compatibility gives on degree \(\nu\)

\[
\langle\Theta a,b\rangle+\langle a,\Theta b\rangle
=\nu\langle a,b\rangle.
\]

Thus \(\Theta-\nu/2\) is skew symmetric; a genuinely defined unitary normalized flow would supply the self-adjoint spectral generator. Completed zeta functions are to arise from cohomological regularized determinants. The required number-field geometry and positive Hodge structure are conjectural. [Deninger, The Hilbert–Polya strategy and height pairings](https://www.uni-muenster.de/SFB878/publications/files/php7aMxKR3029.pdf)

**Inference.** This matches the intended chain: positivity from a Hodge metric, arithmetic from a geometric trace formula. Degree-zero and degree-two sectors organize poles; the central degree-one sector must be infinite dimensional. Supersymmetric quantum mechanics of the relevant complex would be natural, but adding SUSY to a conjecturally positive complex does not prove positivity.

**Literature.** Connes–Consani–Marcolli realize the explicit formula as a Lefschetz trace on cyclic homology of a cokernel associated with the adèle class space. Positivity of its trace pairing is equivalent to RH. Correspondences and degree/codegree analogues exist, but the positive-pairing theorem remains missing. [The Weil proof and the geometry of the adeles class space, 2007](https://arxiv.org/abs/math/0703392)

**First proposed test.** In a known function-field geometric model, derive an ordinary positive supersymmetric pairing from cup product and Hodge star, including pole-sector separation. Identify exactly what fails on passing to semilocal number-field geometry. This would isolate the required Ward or polarization identity without inserting zero locations.

A finite collection of vacua needs continuous or infinite-rank accompanying sectors to cover all inputs. Formal skew symmetry alone also does not settle domains, completeness, or the geometric trace formula.

## 5. Tate/Vladimirov fields: local building blocks with a positivity gate

**Elementary local calculations.** With standard multiplicative measures,

\[
\int_{\mathbb Q_p^\times}\mathbf1_{\mathbb Z_p}(x)|x|_p^s d^\times x
=(1-p^{-s})^{-1},\qquad\operatorname{Re}s>0,
\]

and

\[
\int_{\mathbb R^\times}e^{-\pi x^2}|x|^s\frac{dx}{|x|}
=\pi^{-s/2}\Gamma(s/2).
\]

These follow from valuation shells and the Gaussian Mellin integral. The global product initially converges only for \(\operatorname{Re}s>1\). Functional equations obtained from global Fourier/Poisson duality concern character amplitudes, not positive Weil norms.

**Literature.** Huang–Stoica–Yau–Zhong construct Vladimirov kinetic operators with local-character multipliers and calculate their Green functions. Their adelic propagator product reproduces the global functional equation. General complex characters do not imply positive kinetic forms; positivity must be checked for the chosen multiplier. [Green's Functions for Vladimirov Derivatives and Tate's Thesis, 2020](https://arxiv.org/pdf/2001.01721)

**Proposal.** Use a real external time and p-adic spatial variables so that a positive Hamiltonian can be specified, for example with multiplier \(|k|_p^\alpha\), real \(\alpha\), and a bounded-below interaction. Test an archimedean/p-adic coupled boundary observable. Do not analytically continue a positive action to a complex exponent and assume positivity survives.

The first gate is an exact one-prime response with the target normalization and logarithmic derivative. A product formula alone is insufficient. Interactions can leave the finite mass-resolvent class, but may destroy the exact local-factor identities; a theory must explain what remains protected.

## 6. Bost–Connes: arithmetic operations versus partition functions

**Literature.** The Bost–Connes Hamiltonian satisfies \(H\epsilon_n=(\log n)\epsilon_n\) and has Gibbs trace \(\zeta(\beta)\) for \(\beta>1\). It has KMS states beyond that Gibbs regime. Multiplication isometries, cyclotomic observables, and low-temperature symmetry breaking encode arithmetic and class-field structure. Existence of a KMS state at \(0<\beta\le1\) must not be confused with convergence of the original trace. [Bost–Connes, Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory, 1995](https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/CONNES/1994-1998/M_95_38/M_95_38_web.pdf)

**Derived here.** Its energy spectrum alone admits the prime-occupation notation

\[
n=\prod_p p^{N_p},\qquad H=\sum_p(\log p)N_p.
\]

For finitely many primes,

\[
\log Z_{S_f}(\beta)=\sum_{p\in S_f,m\ge1}\frac{p^{-m\beta}}m,\qquad
-\partial_\beta\log Z_{S_f}(\beta+i\tau)
=\sum_{p,m}(\log p)p^{-m\beta}e^{-im\log p\,\tau}.
\]

This gets repetitions right. The Weil target uses minus twice the real part of the latter expression at \(\beta=1/2\), with gamma and pole terms. It is a logarithmic derivative of a twisted partition amplitude, not a positive thermal variance. The infinite Gibbs trace is unavailable there.

**Proposal.** Use the arithmetic algebra as a defect algebra on a larger polarized supersymmetric space. Specify its action and adjoints, then derive the entire two-point pairing. A positive state gives \(\varphi(A_f^*A_f)\ge0\), but identifying that with \(Q_L[f]\) remains essential. Tensoring gamma and Bost–Connes sectors multiplies correlations; it does not yield the desired signed sum of logarithmic derivatives.

## 7. Selberg and dynamical models: comparison laboratories

**Literature.** The compact hyperbolic Selberg formula has orbit weight

\[
\frac{\ell_\gamma}{2\sinh(m\ell_\gamma/2)}.
\]

The Riemann formula needs \((\log p)p^{-m/2}\), with the opposite orbit sign in the usual comparison. Cusps add arithmetic scattering contributions but do not erase these differences. Connes explains the resulting motivation for absorption spectra. [Connes, An essay on the Riemann Hypothesis, 2015](https://arxiv.org/pdf/1509.05576)

**Inference.** Compact-surface Laplacians also have the wrong high-energy counting law for Riemann zeros. A generic sigma model on a hyperbolic surface is therefore a weak direct candidate. Supersymmetric transfer complexes can alter orbital determinant factors and signs, but an alternating trace is not an ordinary norm.

**First proposed test.** Derive the exact repetition factor, poles, and spectral density in a controlled dynamical model before associating its orbits with primes. Study how a signed trace becomes a positive cohomological pairing. This can eliminate mismatched models analytically.

## 8. Selection tests

1. **Metric and connection:** derive a positive norm identity for the exact normal derivative plus residues. A positive metric alone, especially one removable by a holomorphic frame change, does not suffice.
2. **Poles:** derive both pole amplitudes and their interference from the same construction. Imposing two vanishing conditions does not by itself deliver the unrestricted target.
3. **Adding primes:** derive changes of metric and polarization, retaining repetitions and mixed histories. The derivative in Section 2 already has the exact finite-support arithmetic bookkeeping.
4. **Rank and domain:** cover every smooth compactly supported input and its logarithmic form completion. Finite source amplitudes alone are insufficient.
5. **Independent positivity:** locate positivity in the physical space or action, and derive the arithmetic identity separately. Do not shift the target by its lowest eigenvalue or use an unknown square root.
6. **Interactions:** specify which restrictive structural assumption an interaction changes. Nonlinearity alone does not establish arithmetic selection or positivity.

The immediate conceptual experiment with the best arithmetic specificity is the first test in a semilocal polarized or genuine tt* setting. Hodge cohomology supplies a longer-term organizing principle. Tate and Bost–Connes theories provide possible local operations, with clearly identified gaps between amplitudes, metric derivatives, and the required positive pairing.

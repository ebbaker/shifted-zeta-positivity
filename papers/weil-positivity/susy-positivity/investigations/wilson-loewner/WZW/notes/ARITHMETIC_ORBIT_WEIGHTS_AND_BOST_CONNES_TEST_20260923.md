# Changing arithmetic orbit weights: a Bost–Connes thermal test

23 September 2026. Prepared for Edward Baker with LLM assistance.

**Model:** GPT-6 (Codex; developer-provided identity).  
**Effort:** not exposed; not inferred.  
**Status:** exact arithmetic coefficient identities from primitive projections in an independently defined thermal system, with an explicitly identified centering factor. A native causal scattering realization of the completed transfer is still missing. Two particular norm constructions fail; no general physical-realization obstruction or RH result is claimed.

This continues the [fractional cusp test](CONTINUOUS_EXPONENT_AND_FRACTIONAL_CUSP_TEST_20260923.md), which identified the need to vary orbit weights without changing logarithmic delay locations. The [diagnostic](../numerics/check_arithmetic_orbit_weights.py), [87-case record](../numerics/records/arithmetic-orbit-weights-20260923.json), and [same-assistant audit](../reviews/review_codex_arithmetic_orbit_weights_20260923.md) are separate research addenda. No manuscript is revised.

## 1. Result and its relevance

There is a useful positive answer at the coefficient level. In the Bost–Connes system, let beta be inverse temperature and let P_n be the projection onto arithmetic states primitive at every prime dividing n. Its thermal expectation is

\[
 \varphi_\beta(P_n)=\prod_{\ell\mid n}(1-\ell^{-\beta}).
\]

With beta=2 omega, the required Euler-series coefficient is exactly

\[
 \boxed{c_n(\omega)=n^{(\beta-1)/2}\varphi_\beta(P_n).}       \tag{1}
\]

One temperature changes all prime, prime-power and composite coefficients consistently. The primitive probabilities come from a pre-existing quantum statistical system, not separate weights fitted prime by prime. The factor n^((beta-1)/2) is an additional centering in the arithmetic dictionary. Below we express it using analytic thermal evolution, but do not treat that expression as a real-time device.

This is stronger than observing a zeta partition function. The relevant positive equilibrium states exist throughout 0<beta<=1 even though the ordinary global Gibbs trace does not converge there. It is weaker than a physical realization of the requested response: statistical expectations are not delayed scattering amplitudes. That distinction is decisive in this test.

## 2. The complete arithmetic requirement

Retain

\[
 \xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad
 K_\omega(p)=\frac{\xi(\tfrac12+p-\omega)}{\xi(\tfrac12+p+\omega)},
 \qquad \partial_\omega\log K_\omega(p)=-a_\omega(p).
\]

The half-shift modular Hodge channel has Euler factor zeta(p)/zeta(p+1). At general positive shift it must become

\[
 Z_\omega(p)=\frac{\zeta(p+\tfrac12-\omega)}{\zeta(p+\tfrac12+\omega)}
 =\sum_{n\ge1}c_n(\omega)e^{-p\log n},\qquad \Re p>\tfrac12+\omega,
                                                                    \tag{2}
\]
\[
 c_1=1,\qquad
 c_n(\omega)=n^{\omega-1/2}\prod_{\ell\mid n}(1-\ell^{-2\omega}).
                                                                    \tag{3}
\]

To derive this, put a=ell^(omega-1/2), b=ell^(-omega-1/2), z=ell^(-p). The local factor is

\[
 \frac{1-bz}{1-az}=1+\sum_{r\ge1}(1-\ell^{-2\omega})
                         \ell^{r(\omega-1/2)}z^r.                \tag{4}
\]

Multiplicativity gives (3). At omega=1/2, c_n=phi_E(n)/n. Here the orbit language refers to primitive residues in the modular constant term, not the closed-geodesic coefficients of a Selberg trace formula.

For integer d, J_d(n)=n^d product_(ell|n)(1-ell^(-d)) counts primitive d-tuples modulo n. Inclusion-exclusion proves this interpretation. For real beta>0, use the same product to define J_beta; no fractional number of discrete coordinates is asserted. Thus c_n=J_(2 omega)(n)/n^(omega+1/2).

The first-prime test and its tangent are

\[
 c_2=\frac{2^\omega-2^{-\omega}}{\sqrt2},\qquad
 c_2(1/2)=\tfrac12,\qquad c_2'(1/2)=\tfrac32\log2.          \tag{5}
\]

The common coefficient law also gives the entire prime part of the differential source, within the absolute-convergence region:

\[
 \partial_\omega\log Z_\omega(p)
 =2\sum_{n\ge2}\Lambda(n)n^{-1/2}\cosh(\omega\log n)e^{-p\log n}
 =-a_{\omega,\mathrm{prime}}(p).                              \tag{6}
\]

Passing (6) does not supply the archimedean source. With s_±=p+1/2±omega,

\[
 K_\omega(p)=A_\omega(p)Z_\omega(p),\qquad
 A_\omega(p)=\pi^\omega\frac{\Gamma(s_-/2)}{\Gamma(s_+/2)}
                 \frac{s_-(s_--1)}{s_+(s_+-1)}.               \tag{7}
\]

The same physical parameter must ultimately produce A_omega, the ordinary radiation norm, and a causal assembly.

## 3. A simple geometric twist does not vary these weights

First try a flat unitary line bundle on the original modular surface. With S^2=R^3=1 in PSL_2(Z), R=ST, a scalar unitary character has chi(S) in {1,-1} and chi(R) a cube root of unity. There are only six possibilities, so there is no continuous scalar character deformation from the trivial one.

Preserving the constant cusp channel requires chi(T)=chi(S)^(-1)chi(R)=1. The common value must be both a square and a cube root of unity, hence both characters are trivial. A nontrivial cusp phase exp(2 pi i alpha) replaces Fourier indices n by n+alpha. In logarithmic cusp height q, the corresponding transverse potential is 4 pi^2(n+alpha)^2 exp(2q); the open constant mode is lost when alpha is nonintegral.

This excludes scalar flat holonomy on this surface as the desired continuous weight control. It does not exclude a different arithmetic quotient, non-flat interactions, or enlarged vector channels. The elementary group-relations argument suffices; it is not a claim that character deformation is unavailable on all hyperbolic surfaces.

## 4. The thermal source of the primitive probabilities

The Bost–Connes system has multiplicative isometries v_n, commuting range projections e_n=v_n v_n^*, and evolution sigma_t(v_n)=n^(it)v_n. Its positive KMS_beta states exist for 0<beta<=1; the familiar Gibbs trace with partition function zeta(beta) is available for beta>1. The KMS measures have local scaling exponent beta, with Haar measure at beta=1. These established facts and their number-field extension are described in [Neshveyev, Introduction and Section 2](https://arxiv.org/html/0907.1456). The derivation below specializes them to the present readout question; it is not a novelty claim about Bost–Connes equilibrium states.

The arithmetic relations are

\[
 v_n^*v_n=I,\qquad e_m e_n=e_{\operatorname{lcm}(m,n)},\qquad
 \sigma_t(e_n)=e_n.
\]

For example, in the standard integer representation v_n|k>=|nk>, e_n selects integers divisible by n, and the Hamiltonian is H|k>=(log k)|k>. Applying the KMS identity to v_n and v_n^* gives

\[
 \varphi_\beta(e_n)
 =\varphi_\beta(v_n^*\sigma_{i\beta}(v_n))=n^{-\beta}.         \tag{8}
\]

Define the fixed, temperature-independent observable

\[
 P_n=\prod_{\ell\mid n}(I-e_\ell),\qquad P_1=I.
\]

Finite inclusion-exclusion, (8), and the lcm relation now prove

\[
 \varphi_\beta(P_n)=\sum_{d\mid\operatorname{rad}(n)}\mu(d)d^{-\beta}
                  =\prod_{\ell\mid n}(1-\ell^{-\beta}),       \tag{9}
\]

establishing (1). Repetitions use the same primitive projector: P_(ell^r)=P_ell. Their changing amplitude comes from the centering factor, not from introducing a new thermal event for every repetition.

There is an elementary physical finite-place version. For a finite set S of primes, take occupation numbers N_ell=0,1,... and

\[
 H_S=\sum_{\ell\in S}(\log\ell)N_\ell.
\]

The normalized Gibbs law at any beta>0 is a product of geometric distributions,

\[
 \Pr_\beta(N_\ell=m)=(1-\ell^{-\beta})\ell^{-m\beta}.
                                                                    \tag{10}
\]

P_n selects occupation zero at primes dividing n. This supplies (9) with genuine positive finite-place Gibbs states even for beta<=1. One must not replace the infinite-place state in that interval by exp(-beta H)/zeta(beta): the proposed normalization is not a convergent positive trace. The abstract KMS construction, rather than analytic continuation of a partition function, supplies the full state.

### Centering is explicit, and is not yet a port normalization

For 0<beta<=1,

\[
 B_{n,\beta}=n^{(\beta-1)/2}P_n
\]

is a positive contraction, and its expectation is c_n(beta/2). The observable now depends on beta. Accordingly, this alone is not a fixed physical detector whose response has been derived solely from a temperature change.

A native analytic-time expression makes the dependence more structured:

\[
 c_n(\beta/2)=n^{-1/2}\varphi_\beta
 \left(P_n v_n^*\sigma_{-i\beta/2}(v_n)\right).               \tag{11}
\]

Indeed sigma_(-i beta/2)(v_n)=n^(beta/2)v_n. This places the centering at a thermal half-step, with the fixed half-shift normalization n^(-1/2). It does not turn imaginary-time evolution into a unitary real-time operation. Deriving this centering from incoming and outgoing radiation normalization remains part of the physical interface problem.

In particular, the native real-time correlation of two P observables is constant because sigma_t(P_n)=P_n. The log n in sigma_t(v_n) is an energy difference/dilation label. No calculation here proves that it is a propagation delay log n. Formula (2) retains those delay labels algebraically; a causal device must earn that interpretation.

## 5. Ordinary local norms and the infinite-place limitation

The local diagonal measure has a direct realization. Normalize additive Haar measure dx on Q_ell by vol(Z_ell)=1 and set

\[
 d\mu_{\beta,\ell}(x)=C_{\beta,\ell}|x|_\ell^{\beta-1}dx,
 \qquad C_{\beta,\ell}=\frac{1-\ell^{-\beta}}{1-\ell^{-1}}.    \tag{12}
\]

It has mu(Z_ell)=1, mu(aE)=|a|_ell^beta mu(E), and shell masses (10) on Z_ell. Thus divisibility by ell^r has probability ell^(-r beta), while the unit shell has probability 1-ell^(-beta). This is the finite-place diagonal of the thermal measure, not a separate norm chosen from K_omega.

Its normalized half-density in the fixed Haar Hilbert space is

\[
 u_{\beta,\ell}(x)=\sqrt{C_{\beta,\ell}}
       |x|_\ell^{(\beta-1)/2}1_{\mathbb Z_\ell}(x),\qquad
 \|u_{\beta,\ell}\|_2=1.                                    \tag{13}
\]

This represents the diagonal state. It is not asserted to intertwine the full Bost–Connes representations for different temperatures.

Weighted dilations D_a^(beta)f(x)=|a|_ell^(beta/2)f(ax) are unitary in L2(mu_beta). Under the canonical half-density map T_beta f=sqrt(C)|x|^((beta-1)/2)f they become

\[
 T_\beta D_a^{(\beta)}T_\beta^{-1}=D_a^{(1)}.                 \tag{14}
\]

A measure change alone therefore leaves the canonically transported unitary dilation action unchanged. The parameter enters the state and its observables. Direct Haar integration gives its actual dilation correlation

\[
 \langle u_{\beta,\ell},D_{\ell^r}^{(1)}u_{\beta,\ell}\rangle
       =\ell^{-\beta|r|/2},\qquad r\in\mathbb Z.              \tag{15}
\]

This correlation is not the coefficient in (4). Primitive projection and centering are essential additional readout choices.

### The baseline product Hilbert space does not carry the naive global family

Relative to u_(1,ell)=1_(Z_ell), the local overlap is

\[
 h_\ell(\beta)=\langle u_{1,\ell},u_{\beta,\ell}\rangle
 =\frac{\sqrt{(1-\ell^{-1})(1-\ell^{-\beta})}}
             {1-\ell^{-(\beta+1)/2}}.                        \tag{16}
\]

For fixed 0<beta<1,

\[
 1-h_\ell(\beta)\sim\tfrac12\ell^{-\beta}.
\]

The sum over primes diverges, so product_ell h_ell(beta)=0. In the incomplete tensor product based on the Haar vacua, embed the finite-place vectors as

\[
 \Omega_{\beta,S}=\bigotimes_{\ell\in S}u_{\beta,\ell}
                     \otimes\bigotimes_{\ell\notin S}u_{1,\ell}.
\]

For finite S subset T,

\[
 \|\Omega_{\beta,T}-\Omega_{\beta,S}\|^2
     =2\left(1-\prod_{\ell\in T\setminus S}h_\ell(\beta)\right).       \tag{17}
\]

For every fixed finite S the right side tends to 2 as T grows. These embeddings are not Cauchy. Finite collections work in one ordinary Hilbert space; their naive global half-density vectors do not converge there.

The parameter tangent already detects the problem. Differentiating the normalized shell amplitudes in (10) gives

\[
 \left\|\left.\partial_\omega\Omega_{2\omega,S}\right|_{\omega=1/2}
       \right\|^2
       =\sum_{\ell\in S}(\log\ell)^2\frac{\ell}{(\ell-1)^2}.          \tag{18}
\]

The local derivatives are orthogonal to their local normalized vectors, so cross terms vanish. The sum diverges. This is a failure of a differentiable vector family in this particular product representation, not a failure of equilibrium states to exist or of finite-observable thermal expectations to be differentiable.

| Number of primes | Largest prime | Overlap, beta=0.5 | Overlap, beta=0.8 | Squared shift-tangent norm |
|---:|---:|---:|---:|---:|
| 4 | 7 | 0.805625 | 0.978404 | 3.41186 |
| 25 | 97 | 0.398762 | 0.924811 | 10.9944 |
| 168 | 997 | 0.0444597 | 0.819804 | 23.9650 |
| 1,229 | 9,973 | 0.0000801090 | 0.658092 | 42.3681 |
| 9,592 | 99,991 | 1.73891e-12 | 0.454913 | 66.1381 |

The infinite conclusion follows from the series argument, not this finite table. This limitation does not invalidate the Bost–Connes KMS construction, which already provides its own representation. It does not exclude another representation, a correlated coupling to the archimedean sector, or a different physical radiation map. It also does not establish anything about the canonical Sonin embeddings in other project notes.

## 6. A concrete bounded-readout exclusion

Individual B_(n,beta) are contractions, but a coherent sum of their expectations need not be. Suppose one declares the bare Euler impulse train to be the response,

\[
 R_\omega=I+\sum_{n\ge2}c_n(\omega)S_{\log n},
\]

where S_v is a causal delay on ordinary L2 time signals. On a window log2<L<log3 its compression is I+c_2 S_(log2). Choose a unit pulse f supported on (0,epsilon), with epsilon<min(log2,L-log2). Its direct and first delayed copies are disjoint and fully inside the window. Hence

\[
 \|1_{(0,L)}R_\omega f\|^2=1+c_2(\omega)^2>1.                \tag{19}
\]

At omega=1/4 this is 1.06066017177982; at omega=1/2 it is 1.25. Thus the bare Euler train cannot be a contraction in the required ordinary signal norm. Multiplying individual probabilities by contractive factors does not resolve coherent energy bookkeeping.

This does not exclude the completed response A_omega Z_omega. In fact the same bare Euler failure occurs at the established modular half shift, whose archimedean factor is essential. Equation (19) shows why the next physical test must include that sector and its energy flux, rather than infer passivity from positive arithmetic weights.

## 7. Recommended next test

The strongest surviving direction is a finite-place Bost–Connes arithmetic sector coupled to an archimedean radiation channel. Start with S={2,3} and the native H_S, P_2, P_3 and P_6, keeping beta=2 omega. The sector is positive and exactly calculable at every relevant temperature. It already supplies the relative primitive probabilities without a divergent global trace.

The next task should specify a Hamiltonian or boundary coupling and actual preparation/readout, then derive its response. The first targets are the weights at log2, log3, log4 and log6; the last two test repetitions and multiplicativity. The coupling must explain why log n becomes a delay and why the thermal half-step in (11) becomes the centering of physical amplitudes. In the same calculation it must produce the omega-dependent archimedean factor and an ordinary radiation-energy balance. An assigned filter equal to A_omega times a finite Euler product would only restate the target.

At finite S there is no issue defining the positive state or its norm. The challenge is the interface. Only after this is derived should one tackle a common-space infinite-place limit; (17) shows that the most immediate product embedding will not suffice. A finite-place model need not itself be lossless if omitted channels carry explicitly accounted flux, but an unexplained deficit or gain cannot be called the desired scalar arithmetic response.

The zero-shift limit is also only algebraically correct so far: c_n(omega) tends to zero for each fixed n>1, leaving c_1=1. The local geometric states spread to arbitrarily high occupation as beta tends to zero. Coefficientwise convergence is not a strong physical-state or scattering limit.

## 8. Verification and claim boundaries

The diagnostic has 87 passing controls: 17 exact integer and 70 floating. The exact cases enumerate primitive residue tuples, check divisibility-projector products, and enumerate cusp-preserving scalar characters. The floating cases check Euler convolution coefficients, finite-place state mass, the primitive projection, a full zeta quotient against a truncated Dirichlet series with an elementary tail bound, the prime-source derivative, local state norms and correlations, overlaps, tangent norms, and the pulse-energy exclusion. The prime cutoff is 100,000; only a compact table is retained.

Python 3.10.0 and mpmath 1.3.0 were used at 50 decimal digits. Finite shell sums run through occupation 360. These are floating controls, not interval arithmetic. The analytic proofs of coefficient matching and the two scoped norm limitations do not depend on the numerical sample sizes. The record binds the program by SHA-256; no zero tables or external datasets are used.

What has been obtained is a physically motivated thermal law for primitive arithmetic probabilities and an exact dictionary to every desired orbit coefficient. What remains unproved is the physical origin of the centering/readout, its causal delay interpretation, the completed archimedean response, and their common ordinary-norm assembly. This is a candidate source for the arithmetic side of the differential equation, not yet the physical solution of that equation. The audit is by the same assistant, not an independent specialist.

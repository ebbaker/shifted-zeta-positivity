# Independently motivated sources for the arithmetic evolution

Date: 23 September 2026. Prepared for Edward Baker.

Model: GPT-6 (Codex; developer-provided identity). Effort: not exposed; not inferred.

Status: literature search and analytic comparison with the current target. The known identities are attributed below; their translation into the project's conventions and the proposed tests are research analysis. No new physical realization, numerical experiment, independent review, or proof of RH is claimed. Prepared with LLM assistance.

## Finding

The search identifies two particularly concrete leads. **The range of a Brownian bridge supplies the entire completed xi function as a natural moment observable. Modular-surface scattering supplies the required transfer function at the single shift omega = 1/2, after an explicit rational normalization.** They solve different parts of the problem. The Brownian construction has the full scalar source but lacks the requested causal readout; modular scattering has a wave channel but lacks a physical parameter producing the whole shift family.

Adelic scaling and semilocal Fourier theory remain the strongest arithmetic-geometric explanation of prime delays. Bost--Connes systems and number-theoretic spin chains provide useful exact statistical-mechanical comparators. None of the sources examined establishes the complete variable-shift family with the project's causal readout, fixed ordinary norm, and physical energy balance.

This sharpens, rather than reverses, the earlier [arithmetic-branch assessment](../../../../brainstorm/theory-landscape-20260913/ARITHMETIC_BRANCH.md) and [existence-mechanism sweep](../../../previous/source-selection-rules/notes/EXISTENCE_MECHANISM_SWEEP_20260916.md). It also preserves the limited scope of the [bounded WZW exclusion](BOUNDED_ARITHMETIC_READOUT_TEST_20260923.md): that result concerns the specified reflected collar and primary response, not all conformal or scattering constructions.

## 1. What the source has to explain

Use the entire completion and the meromorphic completion distinctly:

\[
\xi(s)=\frac12s(s-1)\Lambda_{\mathbb R}(s),\qquad
\Lambda_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

The [arithmetic-source note](../../notes/ARITHMETIC_SOURCE_AND_GENERALIZED_LOEWNER_EVOLUTION_20260922.md) fixes

\[
H(p)=\xi(\tfrac12+p),\quad m(p)=H'(p)/H(p),\quad
K_\omega(p)=\frac{H(p-\omega)}{H(p+\omega)},
\]

\[
\partial_\omega K_\omega(p)=-a_\omega(p)K_\omega(p),\qquad
a_\omega(p)=m(p-\omega)+m(p+\omega),\qquad K_0=1.
\]

In the absolutely convergent region Re p > 1/2 + omega, the prime contribution to the source is

\[
-2\sum_{n\ge2}\Lambda(n)n^{-1/2}\cosh(\omega\log n)e^{-p\log n}.
\]

Here capital Lambda without a subscript denotes the von Mangoldt function. The gamma term, the rational completion terms, and local terms must also be recovered. For the finite-shift zeta quotient, the coefficient at the first arithmetic delay is

\[
c_2(\omega)=\frac{2^\omega-2^{-\omega}}{\sqrt2},\qquad
c_2(\tfrac12)=\tfrac12.
\]

An independently motivated source starts from a specified stochastic process, geometric wave equation, algebra, or interaction law, then derives its arithmetic observable. Prescribing xi as a transfer function, choosing energies from the desired prime list, or fitting zeta zeros is a weaker form of explanation. Arithmetic geometry is admissible, but its native geometry and measure must do actual work.

There are three distinct success criteria:

1. Derive the scalar arithmetic function or source, with its normalizations.
2. Derive an oriented input/output response equal to K, with an identified propagation coordinate and identity limit.
3. Prove the required norm or energy inequality in that system's ordinary Hilbert space.

A positive probability measure, a unitary on-shell scattering coefficient, and a positive instantaneous Loewner driver are different assertions. In particular, the earlier pole analysis already prevents treating the instantaneous a_omega as a generic positive-real driver. The physical target is a cumulative response.

## 2. Brownian bridge: a complete scalar source

Let b(t), 0 <= t <= 1, be a standard real Brownian bridge, pinned at zero at both ends, and set

\[
Y=\sqrt{\frac2\pi}\left(\max_t b(t)-\min_t b(t)\right).
\]

Biane, Pitman and Yor record the exact identity

\[
\mathbb E[Y^s]=2\xi(s),\qquad s\in\mathbb C.
\]

Their paper also connects this law to Brownian/Bessel path functionals and the circle heat kernel. The process and its range are defined without a prime spectrum or zeta zeros. See [BPY, introduction, equations (4)--(5), and Section 2](https://arxiv.org/html/math/9912170).

### Translation into the present evolution

Write s = 1/2 + p. Direct substitution gives

\[
K_\omega(p)=
\frac{\mathbb E[Y^{s-\omega}]}{\mathbb E[Y^{s+\omega}]},
\]

\[
a_\omega(p)=
\frac{\mathbb E[Y^{s-\omega}\log Y]}{\mathbb E[Y^{s-\omega}]}
+\frac{\mathbb E[Y^{s+\omega}\log Y]}{\mathbb E[Y^{s+\omega}]}.
\]

These are meromorphic identities where denominators are nonzero. Differentiation is justified by the moments in a real neighborhood of each complex exponent. This is the **full** scalar source: the completion factors have already been produced by a native stochastic observable. There is no need to continue a divergent Gibbs trace to define these moments.

A useful centered form follows by changing the path measure:

\[
d\mathbb P_* = \frac{Y^{1/2}}{\mathbb E[Y^{1/2}]}d\mathbb P,
\qquad X=\log Y,\qquad
M(p)=\mathbb E_*e^{pX}=\frac{H(p)}{H(0)}.
\]

The functional equation makes M even, hence the distribution of X under P_* is symmetric. For real p, another exponential tilt gives

\[
m(p)=\mathbb E_p[X],\qquad m'(p)=\operatorname{Var}_p(X)\ge0.
\]

Thus the arithmetic source has an interpretation in terms of tilted means and fluctuations. Evenness and real log-convexity imply 0 < K_omega(p) <= 1 for real p, omega >= 0. This is a real-axis statement only.

### What this does not yet give

Brownian time, the logarithmic range X, the Mellin parameter p, and the shift omega are distinct variables. A ratio of moment observables has not thereby become a causal input/output transfer in logarithmic distance. In particular, the atom at log 2 appears after the arithmetic expansion; no Brownian propagation channel with that delayed response has yet been derived.

For example, normalized native path amplitudes

\[
\psi_q=\frac{Y^{q/2}}{\sqrt{\mathbb E[Y^q]}},\qquad q\in\mathbb R,
\]

have overlaps

\[
\langle\psi_q,\psi_r\rangle=
\frac{\mathbb E[Y^{(q+r)/2}]}{
\sqrt{\mathbb E[Y^q]\mathbb E[Y^r]}}.
\]

Their positive Gram matrices are not the required moment quotient. Positivity of a distribution and symmetry of its logarithmic observable are also insufficient: the elementary positive symmetric law with probabilities 2/3 at 0 and 1/6 at each of +/-1 has

\[
M_0(p)=\frac{2+\cosh p}{3},
\]

whose zeros are +/- arcosh(2) + (2k+1) pi i. For sufficiently small positive omega its shifted quotient has poles in the right half-plane. This explicit counterexample blocks an inference from generic stochastic positivity to the desired complex contractivity.

The sharper Lee--Yang/Laguerre--Polya condition for the centered xi characteristic function remains tied to RH; [Konstantopoulos, Patie and Sarkar, Sections 2 and 4](https://arxiv.org/html/2211.16680) discuss this distinction. A proposed ferromagnetic or stochastic theorem must establish its hypotheses for this particular law.

**Bounded next test.** Specify an actual conditional or first-passage response of the bridge, using the Markov state (time, position, running minimum, running maximum), or an equivalent Bessel construction. Identify preparation and readout before calculating a transform. Determine whether logarithmic range can serve as the oriented coordinate, and whether a physical deformation produces omega while preserving the intended norm. A construction that only divides two already-known moments passes criterion 1, not criteria 2--3. This is the strongest new starting point if the priority is the complete scalar source.

## 3. Modular cusp scattering: an exact transfer at one shift

Take the Laplace--Beltrami operator on PSL(2,Z) acting on the upper half-plane, with the hyperbolic metric and the modular identifications. The cusp is an open wave channel. Fix the Eisenstein convention

\[
E(z,\sigma)=y^\sigma+\varphi(\sigma)y^{1-\sigma}
+\text{nonconstant Fourier modes}.
\]

Its scattering coefficient is

\[
\varphi(\sigma)=
\frac{\Lambda_{\mathbb R}(2\sigma-1)}{\Lambda_{\mathbb R}(2\sigma)}
=\sqrt\pi\frac{\Gamma(\sigma-1/2)}{\Gamma(\sigma)}
\frac{\zeta(2\sigma-1)}{\zeta(2\sigma)}.
\]

For the constant-term formula see [Lagarias and Suzuki, equations (10)--(11)](https://arxiv.org/pdf/math/0412039). Their completion notation differs from ours. For the wave interpretation, logarithmic cusp coordinate, and incoming/outgoing convention see [Savvidy and Savvidy](https://arxiv.org/html/1809.09491).

### Exact comparison, including completion

Put p = 2 sigma - 1. Algebra using our entire xi gives

\[
\boxed{K_{1/2}(p)=\frac{\xi(p)}{\xi(p+1)}
=\frac{p-1}{p+1}\,
\varphi\!\left(\frac{p+1}{2}\right).}
\]

This is a meromorphic identity, with removable singularities interpreted by limits. It is more specific than the observation that some chaotic system has a zeta function.

The arithmetic coefficients are equally concrete. Primitive integer pairs in the Eisenstein sum give coprime residue counts, hence

\[
\frac{\zeta(p)}{\zeta(p+1)}
=\sum_{n\ge1}\frac{\phi_{\rm E}(n)}n e^{-p\log n},
\qquad \Re p>1,
\]

where phi_E is Euler's totient. Its n = 2 coefficient is 1/2, exactly c_2(1/2). At this shift the full Dirichlet quotient agrees, not just one coefficient. The gamma quotient and rational factor must still be retained when reconstructing the total time response; a coefficient in the arithmetic comb is not automatically an isolated delta in the completed transfer.

The arithmetic here comes from cusp scattering and primitive lattice counts. The lengths of primitive closed geodesics on a modular surface should not be identified with the prime logarithms in the Riemann explicit formula.

### Readout and parameter issues

With q = log y and sigma = 1/2 - i k, the constant channel has incoming/outgoing factors exp(-i k q) and exp(i k q), after extracting y^(1/2). The spectral energy is k^2 + 1/4 and p = -2 i k. Thus log n in the p convention corresponds to 2 log n in a coordinate conjugate to k. Reversing the scattering convention inverts the coefficient. Those choices must be fixed before a causality comparison.

The rational factor (p-1)/(p+1) has unit modulus on the imaginary axis and cancels the pole associated with the constant mode. That is a precise algebraic normalization, not yet a derivation of a physical readout with the required energy balance. Pole cancellation can hide an internal mode. The choice of scattering subspace and any bound-state removal must be justified in the native Hilbert space.

Most importantly, the arithmetic argument separation is fixed at one. Changing frequency moves both arguments together. Moving the reference section of the cusp to y = Y multiplies this convention for the coefficient by Y^(1-2 sigma) = Y^(-p); it changes a propagation phase/delay, not the separation 2 omega. A geometrical deformation would have to be specified and calculated rather than assumed to supply omega.

Real-frequency scattering unitarity therefore does not establish the desired analytic and norm properties for all omega > 0. Zeta zeros occurring as resonances do not automatically become real eigenvalues of a self-adjoint operator.

**Bounded next test.** Derive the channel preparation, flux norm, reference section, and treatment of the constant mode at omega = 1/2; calculate the same first-delay window used in the WZW test. Then test one genuinely physical deformation for a change in the argument separation, with the operator domain and norm tracked explicitly. The first stage is an exact calibration; progress toward the full family requires the second stage.

## 4. Adelic scaling and semilocal Fourier theory

The arithmetic-geometric attraction is a native scaling action. In the adele class space, the prime-associated periodic orbit has length log p; repetitions give r log p. [Connes and Consani's geometric account](https://arxiv.org/html/2401.08401) makes this origin explicit. Orbit lengths alone do not determine the required weights, archimedean term, or positive response. Those require the measure, half-density convention, and trace/scattering construction.

For a finite set of places S containing infinity, a concrete starting space is

\[
\Gamma_S\backslash\prod_{v\in S}\mathbb Q_v,
\qquad \Gamma_S=\{\pm\prod_{p\in S\setminus\{\infty\}}p^{n_p}:n_p\in\mathbb Z\}.
\]

This couples places through one arithmetic quotient. It is more constrained than a collection of independent resonators assigned prime lengths.

The outstanding norm problem is already visible in primary work. [Connes--Consani, Theorem 5.22](https://arxiv.org/html/2008.10974v1) gives injections on adjoining local factors; an injection is not an isometry. The semilocal Hilbert structures in [Connes--Consani--Moscovici, Section 4.8](https://arxiv.org/html/2310.18423v1) depend on S. These constructions cannot be substituted for a fixed unweighted norm without checking the change of metric.

There is also a direct warning about causality. In [Burnol's adelic Lax--Phillips construction, Theorem 1.7](https://arxiv.org/pdf/math/0001013), the required causality/orthogonality statement is equivalent to the relevant Riemann hypotheses. The setup is valuable, but that theorem locates the missing assertion rather than supplying it independently.

Recent work does not remove this qualification. [Zeta Spectral Triples, Section 8](https://arxiv.org/html/2511.22755) identifies unresolved properties of the least Weil eigenvalue/eigenvector and the approximation needed for zero convergence. [Connes's 2026 overview](https://arxiv.org/html/2602.04022) places the semilocal approach within this still incomplete program.

**Bounded next test.** Retain the previously recommended S = {infinity, 2} model and calculate its specified Fourier/scaling readout through a window between log 2 and log 3. Keep the actual metric, contact terms and complete remainder. Then adjoin 3 and examine compatibility, including repetitions. A finite-place identity without an isometric passage to the common physical norm is not the full result.

## 5. Statistical-mechanical comparators

### Bost--Connes and graded prime gases

The Bost--Connes system derives arithmetic time evolution from a Hecke-algebra construction. In its Gibbs representation the Hamiltonian has levels log n and partition function zeta(beta) for beta > 1. The [original Bost--Connes preprint](https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/CONNES/1994-1998/M_95_38/M_95_38_web.pdf) is the primary reference; this search had only indexed excerpts for that PDF, and the construction was already assessed in the project's arithmetic landscape.

Within the trace convergence region,

\[
\partial_\beta\log Z(\beta)=-\sum_{n\ge2}\Lambda(n)n^{-\beta}.
\]

Evaluating at beta = 1/2 + p +/- omega and adding reproduces the prime part of a_omega. Completion factors are absent. Low-temperature Gibbs traces and other KMS states must not be conflated: a state below the trace-convergence threshold does not turn a divergent trace into the desired analytic continuation. Also, logarithmic energies are not automatically physical flight delays.

An elementary boson/graded-fermion comparison illustrates another limit. For oscillators with energies log p, the product of a bosonic trace at s-omega and a fermionic supertrace at s+omega is

\[
\prod_p\frac{1-p^{-s-\omega}}{1-p^{-s+\omega}}
=\frac{\zeta(s-\omega)}{\zeta(s+\omega)},\qquad \Re s>1+\omega.
\]

This derives the ratio once the prime energies are given. The graded trace has signs and is not an ordinary positive norm. It is useful bookkeeping for the supersymmetry program, but does not by itself provide the missing physical positivity or a native origin of the prime energies.

### Knauf/Farey spin chains

Number-theoretic spin chains use products of integer matrices and continued-fraction denominators, rather than a prescribed list of prime energies. One Knauf partition function in the thermodynamic limit is

\[
Z(\beta)=\frac{\zeta(\beta-1)}{\zeta(\beta)}
=\sum_{n\ge1}\phi_{\rm E}(n)n^{-\beta},\qquad\beta>2.
\]

See [Knauf's original model](https://cris.fau.de/publications/109359844/?lang=en_GB) and [Contucci--Knauf](https://empslocal.ex.ac.uk/people/staff/mrwatkin/zeta/contucci.pdf). At beta = p+1 this is exactly the arithmetic quotient in modular scattering. It is therefore a useful interacting positive-measure comparator, with the same fixed separation. The gamma completion and causal readout are not supplied.

These chains have several inequivalent variants; equality of free energies does not make all partition functions identical. Nor does calling a model ferromagnetic automatically permit a Lee--Yang theorem about temperature zeros. [Knauf's later account](https://www.mis.mpg.de/publications/preprint-repository/article/1997/issue-15) explicitly links a further convergence problem to RH. This is a controlled research direction, not an available positivity shortcut.

## 6. Wider search: useful components and lower priorities

| Family and primary source | What the construction supplies | Limitation for this task |
|---|---|---|
| [Canonical system from xi, Suzuki](https://arxiv.org/html/1204.1827) | Explicit canonical-system machinery for the same shift quotient in a safe parameter regime. | Xi is the input; extension to the full positive family is the difficult assertion. Use as a benchmark for a physical construction. |
| [Mayer transfer operator](https://archive.mpim-bonn.mpg.de/id/eprint/346/1/preprint_1990_86.pdf) | Continued-fraction dynamics and a Selberg-zeta determinant. | Generic periodic-orbit determinants are not Riemann xi. The modular cusp channel is the sharper match here. |
| [Quantum graphs, Kuipers--Hummel--Richter](https://arxiv.org/html/1307.6055) | Engineered graphs match the Riemann oscillatory counting term. | Arithmetic lengths/weights are specified; the smooth term differs. This is a realization template, not an independent source of the whole target. |
| [Rindler Dirac mirrors, Sierra](https://arxiv.org/html/1404.4252) | Directed propagation and arithmetic scattering models. | The mirror data and boundary choices encode arithmetic information; the full positive causal family is not obtained merely from Rindler kinematics. |
| [Inverted oscillator and quantum Hall/Rindler scattering](https://arxiv.org/html/2012.09875) | Mellin scattering amplitudes containing gamma functions. | Promising archimedean component; the exact offset, completion terms and prime response still need derivation. |
| [Vladimirov fields and Tate local factors](https://arxiv.org/html/2001.01721) | Local gamma factors arise as Green-function data on local fields. | The global functional equation/product is not yet the target cumulative transfer or its energy balance. |
| [p-adic AdS/CFT](https://arxiv.org/abs/1605.01061) | Native tree propagation and local arithmetic factors. | A local Euler factor is insufficient; coupling all places and retaining the required norm remain additional work. |
| [Adelic string amplitudes, Freund--Witten](https://www.sciencedirect.com/science/article/abs/pii/0370269387913578) | Arithmetic relations between real and p-adic amplitudes. | A product formula/functional equation does not itself identify K_omega as a positive causal response. |
| [Quantum simulation of logarithmic spectra, Wei et al., 2026](https://www.nature.com/articles/s41467-026-74935-8) | Quantum dynamics designed with E_n proportional to log n, and zeta-related amplitudes. | The Hamiltonian encodes the logarithmic spectrum. It is a simulator of specified arithmetic data, not an explanation of its emergence. |
| [Trapped-ion Floquet simulation, 2021](https://www.nature.com/articles/s41534-021-00446-7) | Measurable zeta-related Floquet response. | The driving waveform is engineered using the target function. Useful experimental control, weak candidate for the independently motivated source. |

No more direct arithmetic readout from an ordinary compact WZW model was found among the sources examined. This search result is not a universal exclusion theorem. Likewise, none of the lower-priority entries is dismissed as mathematical or experimental work; the ranking concerns the specific missing source and norm in this project.

## 7. Recommended next decision

| Priority criterion | Best candidate | Concrete next deliverable |
|---|---|---|
| Full scalar source from simple native dynamics | Brownian bridge range | One specified Markov/first-passage preparation and readout, its transformed response, and its actual norm. |
| Actual scattering channel with exact arithmetic comparison | Modular cusp | A convention and energy audit at omega = 1/2, followed by an explicit test of a proposed shift-changing deformation. |
| Native geometric origin of prime delays and place coupling | Semilocal adelic scaling | The infinity-plus-2 response with full remainder and metric, compatible with adjoining 3. |

If choosing one fresh candidate to investigate after the WZW test, start with the Brownian bridge: it has already supplied the entire scalar source and avoids guessing gamma weights. Use modular scattering as the exact wave-response benchmark. Keep the semilocal program active as the route that most directly explains the prime delay structure, while respecting the existing metric and causality obstacles.

The next useful claim is deliberately small: a physically defined response, calculated before comparison with K, that passes the same identity, orientation, first-delay and norm tests. Another representation of xi alone would not settle the missing step.

## 8. Search and validation scope

The search covered stochastic/theta models, automorphic scattering and transfer operators, arithmetic quantum statistical mechanics, spin chains and Lee--Yang questions, adelic/semilocal analysis, local-field theories, quantum graphs, Rindler/oscillator models, string product formulas, canonical systems, and quantum simulators. Primary papers and author/institution repositories were preferred. Recent 2025--2026 work was included where available. This is a broad targeted search, not a claim of exhaustive coverage.

The Brownian identity, modular constant term, and the cited causality/metric gaps were checked in accessible full text. Some supplementary sources were accessible only through their abstracts or indexed excerpts: in particular the original Bost--Connes PDF and original Knauf model page; the Contucci--Knauf PDF's text extraction was incomplete. Those access limits should be removed before a detailed follow-up on those models. Automated HTML conversion dates were not treated as paper publication dates.

The displayed mappings to K and a, the real-axis variance interpretation, and the elementary probability counterexample are analytic checks in this note. No numerical cases have been added. Existing numerical records and manuscript PDFs are separate; package inventory validation checks file identity and saved records, not the mathematical conclusions of this search.

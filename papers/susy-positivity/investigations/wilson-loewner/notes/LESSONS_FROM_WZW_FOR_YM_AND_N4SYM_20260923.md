# Lessons from WZW and the later response tests for Yang–Mills and N=4 SYM

23 September 2026. Prepared for Edward Baker with substantial LLM assistance.

**Model:** GPT-6 (Codex; developer-provided model identity).  
**Reasoning effort:** not exposed; not inferred.  
**Status:** research synthesis and proposed direction. This note separates established inputs, results reported in the existing project notes, and the present assessment. It adds no numerical experiment, independently reviewed theorem, continuum QFT construction, or arithmetic realization.  
**Repository baseline:** `8afbc80a8a6efc0f6abb3314b1b84fb7d6c04486`. This baseline does not contain this note.

## 1. Assessment and scope

The WZW investigation gives useful lessons for the parent Yang–Mills and four-dimensional N=4 supersymmetric Yang–Mills programs. Its strongest lesson concerns the relation between an observable, its measured response, and its positive norm. A positive state space, an exact geometric evolution, or a promising spectrum does not by itself give a causal contraction on the desired signal space.

These findings do not justify abandoning the parent physical question. The [genuine-trace continuation](RESEARCH_CONTINUATION_AFTER_GROWING_TRACE_20260921.md) fixes that question: hold the theory and quantum state fixed, let a specified Loewner driver generate an actual curve, define a Wilson observable on it, and derive its expectation-value evolution. An explicit path-integral evaluation and an arithmetic match are not prerequisites for useful progress. Arithmetic realization is a subsequent, separate task.

The resulting recommendation is to continue the YM insertion hierarchy and open a controlled N=4 SYM displacement-operator investigation. The detailed proposal is in [N4SYM/notes](../N4SYM/notes/N4SYM_DISPLACEMENT_LOEWNER_RESEARCH_PROPOSAL_20260923.md). This note records why that continuation is justified, what it should retain, and which earlier failure modes it should avoid.

## 2. What the WZW branch actually established

The [deterministic SU(2) level-2 pilot](SU2_LEVEL2_DETERMINISTIC_LOEWNER_PILOT_20260922.md) supplied explicit conformal blocks, a boundary-selected state, complete deterministic evolution, composition and fusion rules. Its evaluated tensor obeyed

\[
\dot M=-\nu(2Q^2+\dot u\,Q)M,\qquad \nu=\tfrac14.
\]

For a constant driver, Hermitian Q gave a positive integrated tensor-norm balance. Moving drivers could increase this norm. Neither the fixed tensor norm nor the transported Chern–Simons channel pairing had been identified with the arithmetic radiation norm. Raw spatial smearing converged to a particular compact initial operator, rather than the identity.

The [full-module collar test](../WZW/notes/BOUNDED_ARITHMETIC_READOUT_TEST_20260923.md) repaired the identity limit and supplied an ordinary positive Hilbert-space balance. It then exposed a stronger obstruction: a fixed reflected readout of positive self-adjoint propagation is self-adjoint. A bounded self-adjoint causal scalar operator on an interval must be multiplication. The desired arithmetic Volterra response is nonlocal. This exclusion survives retaining all descendants.

The selected primary also had the wrong matrix-element weights and short-distance exponent, and no first-prime delayed singularity. These are properties of the specified preparation and readout, not a theorem excluding WZW, gauge theories, or all conformal defects.

The later investigations added further distinctions:

| Test | Retained achievement | Missing ingredient or scoped failure |
|---|---|---|
| Brownian bridge and first passage | Natural xi moment identity; causal mean response with variance and future-output balance | The native Laplace response differs from the Mellin quotient; the exact logarithmic phase lacks a full-family causal construction |
| Modular exact-one-form scattering | Completed half-shift response with an ordinary radiation norm | The tested cusp load does not generate the variable arithmetic shift |
| Fractional memory clock | Positive memory law and the correct leading variable power | Wrong subleading term, boundary modulus, prime-delay support and identity endpoint |
| Bost–Connes equilibrium | Exact primitive coefficient probabilities at one common temperature | Centering, real delays, completion and a common physical response remain unconstructed |
| Controlled thermal loops | Explicit unitary propagation and identity limit | Incorrect prime-repetition amplitudes |
| Thermal parallel load | Positive conservative linear model coupled to the full modular core | Finite total response spectral mass preserves the wrong front exponent |

The [current WZW manuscript and index](../WZW/README.md) locate the detailed derivations and audits. These tests distinguish a valid positive model from a model realizing the target.

## 3. Reflection positivity should help construct accumulated storage

The desired arithmetic implication is

\[
\|f\|^2=\|V_{\omega,L}f\|^2+\|B_{\omega,L}f\|^2,
\qquad I-V_{\omega,L}^{*}V_{\omega,L}=B_{\omega,L}^{*}B_{\omega,L}.
\]

The causal map V describes the observed signal. The map B describes independently defined amplitudes in internal states, other outputs, or later radiation. A reflected pairing could establish the norm of Bf without requiring V itself to be a self-adjoint Euclidean compression.

This role was already proposed in the [parent cumulative-positivity section](../sections/06_cumulative_positivity.tex). The WZW collar failure reinforces its importance. Merely identifying a positive Wilson Gram kernel does not identify that kernel with the particular deficit above. The unmodified free reflected kernel, for example, does not automatically vanish at zero shift as B must.

For the interacting SYM defect construction, the physical adjoint, reference color sector, admissible operators, regulator and positivity-preserving renormalization remain substantive requirements. Gauge invariance and a formal scalar-map rotation do not establish the needed reflection inequality; see the [reflection analysis](../sections/08_reflection.tex).

Cumulative positivity also avoids an unnecessary restriction. Contractivity of the completed response need not arise from positive instantaneous shift generators at every intermediate parameter. The [arithmetic-source analysis](ARITHMETIC_SOURCE_AND_GENERALIZED_LOEWNER_EVOLUTION_20260922.md) explains why imposing that stronger property would reject otherwise admissible cumulative evolutions.

## 4. An insertion hierarchy is a legitimate physical result

For the actual growing trace in pure YM, completed by its straight return chord at fixed smooth-field resolution, the [existing calculation](GENUINE_LOEWNER_TRACE_YM_HIERARCHY_20260921.md) gives

\[
\dot W=ikM_1,\qquad
\dot M_1=\dot q^{\mu}M_{D,\mu}+2ikM_2.
\]

The first derivative inserts transported curvature. The next derivative introduces covariant derivatives and ordered two-curvature terms. These equations keep the full interacting expectation under their stated regularity and moment assumptions.

WZW's finite KZ equations arise from special chiral and representation-theoretic structure. They should not create an expectation that W and M1 must close in four-dimensional YM. The transverse-current terms, finite-N products, contact terms and, for flowed observables, derivatives of the flow map cannot be discarded to obtain a smaller equation.

The useful extension is an explicitly defined family of insertion observables whose evolution is controlled. This may be an infinite hierarchy with a suitable domain and norm, a memory equation obtained by justified elimination, or a symmetry-selected closed subsystem. Replacing an unknown derivative by the ratio W'/W supplies none of these.

Even a bound on a single scalar Wilson expectation would not establish contraction on arbitrary L2 inputs. A subsequent input/output construction must specify how a waveform prepares a state and how outgoing amplitudes are measured.

## 5. Supersymmetric protection must be checked against the actual response

A counting character, a localized partition function and an endpoint matrix element are different objects. The [Hodge follow-up](HODGE_RADIAL_CHANNEL_AND_PROGRAM_ASSESSMENT_20260920.md) gave a particularly clear example in the specified free three-dimensional boundary sector: canonical protected representatives admitted positive radial evolution, while projection retained only the lowest elementary angular mode. An infinite composite spectrum did not make the elementary endpoint excite it.

The [Gaussian pair-interface test](GAUSSIAN_PAIR_INTERFACE_ENDPOINT_RESPONSE_20260920.md) then did excite infinitely many composites, but canonical endpoint matrix elements fixed the wrong weights and singularity. Neither result is a general obstruction to four-dimensional N=4 SYM.

For a new supersymmetric family, the early questions should be:

1. Which supercharges are preserved by the complete observable, including endpoints and the scalar profile?
2. Does the proposed shape variation preserve the sector used in the calculation?
3. Which operators and states does the preparation actually excite, with what matrix elements?
4. Does the adjoint used in the positive pairing agree with the physical adjoint?
5. Has protection removed the nontrivial shape response that the investigation seeks?

The parent's [smooth variation](../sections/05_variation.tex) already separates curvature, scalar-gradient, arclength and internal-polarization terms. Its [endpoint analysis](../sections/07_endpoints.tex) shows why a common bulk charge alone is insufficient: within one specified ansatz, same-charge endpoint polarizations have zero pairing and a nonzero R charge. A physical adjoint pair is a different choice. These restrictions must remain visible in any N=4 extension.

## 6. Test singularities and parameter action without identifying different clocks

The target requires

\[
K_\omega(p)\sim(2\pi/p)^\omega,
\qquad
k_\omega(v)\sim\frac{(2\pi)^\omega}{\Gamma(\omega)}v^{\omega-1}.
\]

It also requires amplitudes to change at fixed delays log(n). The fractional-clock test failed in part because it changed propagation delays instead. The thermal construction supplied logarithmic energy labels without deriving flight times. These are lessons about the physical meaning of a parameter, not merely its notation.

In YM or SYM, distinguish Loewner capacity, position along a Euclidean line, Lorentzian time, radial time, ultraviolet smoothing scale, external source amplitude and arithmetic shift. A proposed dictionary must say which operation changes the measured response while the bulk theory is held fixed. Varying the gauge coupling is a comparison between theories, not the default geometric evolution within one fixed theory.

The existing YM expansion is proportional to t^3 at small Loewner time and fixed positive smoothing scale. This cannot be compared directly with the arithmetic kernel's short-radiation-delay singularity. The variables and observables differ, and removing the smoothing scale may change the relevant asymptotics.

The [finite-spectral-mass exclusion](../WZW/notes/THERMAL_BOUNDARY_COUPLING_AND_FRONT_RIGIDITY_TEST_20260923.md) also has a precise scope: a particular parallel connection to an unchanged core, with a positive response measure of finite total mass. A continuum QFT may lie outside that class. Its ultraviolet degrees of freedom must then be supplied with a controlled domain, counterterms and energy account. Infinite spectral mass is an escape from a theorem's hypotheses, not evidence that a realization succeeds.

## 7. A concrete opportunity in N=4 SYM

The displacement operator offers an established connection between Wilson-line shape response and radiation. For the straight BPS reference line, the separated Euclidean two-point function is

\[
\langle\!\langle\mathbb D_i(\tau)\mathbb D_j(0)\rangle\!\rangle
=\frac{12B(\lambda,N)\delta_{ij}}{\tau^4}.
\]

The same Bremsstrahlung function controls small-angle cusp response and small-velocity radiation. These are inputs from [Correa–Henn–Maldacena–Sever, Sections 3–4](https://arxiv.org/html/1202.4455), not results of this note.

The present assessment is that this sector is a useful starting point because it joins geometric insertions to a physical energy observable. The protected scaling dimension fixes the displayed power: changing its coefficient alone cannot generate a continuously variable arithmetic exponent. The complete nonlinear shape response involves further correlators and contact terms.

A prescribed moving contour is also an external drive. Positive radiated energy does not automatically imply that an outgoing waveform has smaller ordinary L2 norm than a chosen incoming waveform. The work done by the source, stored or near-field energy, and any unobserved channels must be included. A response susceptibility, a scattering amplitude and a Wilson expectation should not be identified without constructing the connecting maps.

For the same reason, Euclidean shape variation, Lorentzian retarded response and causal scattering are successive questions. Analytic continuation of a separated correlator does not supply all contact terms or a microscopic input/output device.

## 8. Recommended continuation and transferability of the exclusions

| Finding | What carries to YM/SYM | What does not follow |
|---|---|---|
| Self-adjoint causal scalar response is local | A general restriction on fixed reflected Euclidean readouts | No exclusion of oriented or multichannel gauge-theory scattering |
| Spectra alone do not fix endpoint response | Matrix elements and physical adjoints must be computed | No exclusion of another operator with different matrix elements |
| WZW primary has wrong weights | A warning to test the chosen preparation early | No theorem about SYM defect spectra |
| Regular parallel loads preserve the core exponent | Applies if the same connection and finite-mass assumptions hold | No general continuum-QFT obstruction |
| Scalar clocks alter delays or attenuate the phase | Applies to the specified scalar composition class | No exclusion of coherent global deformations |
| A positive scalar quantity need not be an L2 contraction | An input/output map and norm balance are required | No loss of value in studying native Wilson expectations first |

For pure YM, the next step remains the finite-regulator Schwinger–Dyson audit of the derivative moment, retaining the transverse, ordered, contact and flow-response terms. For N=4 SYM, begin with controlled deformations of the straight BPS line, derive the displacement and internal-scalar insertion hierarchy, and audit its retarded response and energy account. Then address an actual Loewner trace with a specified completion and cusp prescription.

The [detailed N4SYM proposal](../N4SYM/notes/N4SYM_DISPLACEMENT_LOEWNER_RESEARCH_PROPOSAL_20260923.md) turns those recommendations into bounded work packages and decision criteria. Arithmetic tests are deferred until a physical response is defined. A successful physical calculation remains valuable even if it later fails those arithmetic tests.

## 9. Provenance and review

This note synthesizes the linked parent and WZW research records and the conversation leading to the N4SYM proposal. Primary literature is distinguished from project-specific calculations. The related sources include [Makeenko's loop-equation lectures](https://arxiv.org/abs/0810.2183), [Zarembo's scalar-coupled loops](https://arxiv.org/abs/hep-th/0205160), and [Baker's open Wilson lines](https://arxiv.org/abs/1102.4948); they do not establish the proposed arithmetic realization.

The drafting, source comparison and proposal design used substantial GPT-6 (Codex) assistance. There has been no independent specialist review. No earlier numerical suite was rerun for this synthesis, and no manuscript or dated manuscript snapshot was produced. Further calculations belong in the relevant investigation's notes, numerical programs and compact records in numerics, and reviews in reviews.

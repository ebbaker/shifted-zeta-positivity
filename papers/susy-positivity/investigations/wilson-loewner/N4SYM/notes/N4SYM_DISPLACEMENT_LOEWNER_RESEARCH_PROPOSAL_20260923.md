# Research proposal: displacement operators, Loewner growth and energy accounting in N=4 SYM

23 September 2026. Prepared for Edward Baker with substantial LLM assistance.

**Model:** GPT-6 (Codex; developer-provided model identity).  
**Reasoning effort:** not exposed; not inferred.  
**Status:** detailed research proposal. No work package below is represented as completed. Displayed background identities are attributed; proposed reductions, renormalized limits, energy realizations and arithmetic comparisons remain tasks. No new numerical experiment, independent specialist review, continuum construction or RH result is claimed.  
**Repository baseline:** `8afbc80a8a6efc0f6abb3314b1b84fb7d6c04486`; this proposal is a subsequent working-tree addition.

## 1. Research question and intended contribution

In one fixed four-dimensional N=4 supersymmetric Yang–Mills theory, how does a geometrically specified deformation of a Wilson line generate an evolution of defect correlation functions, and can the resulting response be organized with a causal, physically normalized energy account?

The proposal has two linked physical stages. First, establish a controlled benchmark near the straight half-BPS Wilson line using its displacement operator and internal-scalar insertions. Second, derive the corresponding equations for a genuine deterministic Loewner trace with an explicitly chosen completion. A finite closed equation is a possible outcome, not an assumption. A controlled hierarchy with explicit unresolved terms is also a useful result.

The longer-term arithmetic question is whether a response constructed in this way can realize the shifted completed-zeta transfer. That comparison begins only after the physical observable, preparation, propagation, readout and norms have been specified. The theory is not to be adjusted to prescribed prime coefficients or a desired transfer function.

The principal deliverable is a derivation that distinguishes:

1. Euclidean shape derivatives of Wilson expectations;
2. retarded responses of a defect in a physical source sector;
3. supplied work, stored energy and emitted radiation;
4. any subsequently constructed linear scattering or boundary transfer.

These objects are related research targets, not interchangeable definitions. The motivation and transferable exclusions are recorded in the [parent lessons note](../../notes/LESSONS_FROM_WZW_FOR_YM_AND_N4SYM_20260923.md).

## 2. Fixed theory, reference observable and parameters

### 2.1 Bulk theory and probe sector

Take four-dimensional N=4 SYM with gauge group SU(N), N at least two, theta angle zero, and a fixed positive coupling gYM. Write lambda = gYM^2 N. Work at finite N unless a separately labelled planar approximation is introduced. The initial reference is the vacuum with a fundamental heavy-source Wilson-line probe. The bulk action and state are held fixed as the contour changes.

For Hermitian gauge and scalar fields, use the Euclidean Wilson–Maldacena transport

\[
U[x,n]=\mathcal P\exp\int d\sigma\,
\left(iA_\mu(x)\dot x^\mu+|\dot x|\,n^I\Phi_I(x)\right),
\qquad n^In^I=1.
\tag{1}
\]

The reference is the straight line x0(sigma) = (sigma,0,0,0), with constant internal unit vector n0. Only this reference is assumed half-BPS. A general deformation with constant n0 need not preserve a common global supercharge. No exact localization formula is presumed for the deformed line.

The infinite line needs a physical source-sector convention. Use the usual static fundamental probe sector, with gauge transformations and source indices treated consistently at infinity; equivalently introduce a large finite-time heavy-source preparation and final contraction and then justify the limit. This convention must be stated before claiming a positive defect Hilbert space. A bare open color matrix is not a gauge-invariant state by itself.

The D3–D5 endpoint construction in the parent work is a possible later comparison with its own specified defect theory. It is not silently added to this pure bulk probe problem. Baker's finite-endpoint examples provide controls under their stated matter and supersymmetry assumptions [P4].

### 2.2 Smooth deformation family

Before treating a growing tip, choose real smooth compactly supported profiles h and j:

\[
x_h(\sigma)=(\sigma,h^1(\sigma),h^2(\sigma),h^3(\sigma)),
\qquad
n_j(\sigma)=\frac{n_0+j(\sigma)}{\sqrt{1+|j(\sigma)|^2}},
\qquad n_0\cdot j=0.
\tag{2}
\]

This family specifies both the geometric and internal deformations, including their quadratic normalization terms. Define the relative Wilson functional Z[h,j] by the expectation in this source sector divided by the straight-reference expectation, using the same regulator and renormalization prescription. Fix Z[0,0] = 1 through that reference; do not insert an additional adjustable function of deformation time.

For small sources, log Z means the local branch around Z = 1. No positivity of Z or of log Z is presumed. The functional is generally nonlinear in h and j; its Hessian is a response kernel, not already a transfer operator on all signals.

### 2.3 Keep the parameters separate

| Symbol | Meaning | Initial convention |
|---|---|---|
| sigma | Euclidean coordinate along the reference line | Used for defect correlators |
| s | Lorentzian physical time | Introduced only with a causal-response prescription |
| t | Loewner capacity parameter | Half-plane capacity 2t |
| epsilon | Amplitude of a smooth test deformation | Differentiated at zero |
| delta | Geometric tip/cusp rounding scale | Positive until the rounding limit is studied |
| LambdaUV | Spectral cutoff in a response control | Distinct from geometric rounding and coupling |
| tau | Field-flow resolution if a flowed control is used | Changes the observable; no supersymmetric flow is assumed |
| omega | Arithmetic shift | Absent from the definition of the physical model |
| lambda | Fixed 't Hooft coupling | A comparison parameter between fixed theories, not the Loewner clock |

Use different notation for the arithmetic Laplace variable p and any geometric momentum or auxiliary spectral coordinate. A relation among these parameters is a result to derive.

## 3. Established inputs and what they do not supply

The straight-line displacement operator generates transverse shape variation. In the source conventions, its separated Euclidean correlator has the form

\[
\langle\!\langle\mathbb D_i(\sigma)\mathbb D_j(0)\rangle\!\rangle_0
=\frac{C_D\delta_{ij}}{\sigma^4},\qquad C_D=12B(\lambda,N).
\tag{3}
\]

The displacement has protected scaling dimension two. Correa–Henn–Maldacena–Sever [P1, Sections 3–4] relate its normalization to the small-angle cusp and radiation observables. Internal-direction variations insert transverse scalar operators on the line. General defect Ward identities and contact terms have a broader treatment in [P2].

Use (3) as a normalization benchmark, not a complete definition at coincident points. In particular:

- C_D fixes a two-point normalization, not the full multipoint defect theory.
- The separated correlator does not specify all local distributional terms.
- Changing lambda changes C_D but not the displayed protected exponent.
- A Euclidean line expectation is not a retarded Lorentzian observable without a continuation and source prescription.
- Known results for a straight or circular BPS line do not establish positivity or localization for arbitrary cusped open networks.

The physical adjoint must be carried through that continuation. Euclidean factors of i in the displacement insertion cannot be interpreted as a failure of Lorentzian Hermiticity by inspection.

## 4. Work package A: observable, adjoint and symmetry audit

**Question.** What precisely is being varied and paired, and what symmetry survives?

Begin with the parent [ordered-transport variation](../../sections/05_variation.tex). With eta = delta x, v = |dot x| and Phi = n^I Phi_I, its smooth-field insertion is

\[
\mathcal I=
iF_{\nu\mu}\eta^\nu\dot x^\mu
+vD_\nu\Phi\,\eta^\nu
+\Phi\frac{\dot x\cdot\dot\eta}{v}
+v\Phi_I\delta n^I,
\tag{4}
\]

together with the endpoint connection terms. All matrix insertions retain their path ordering. Derive the renormalized analogue appropriate to the chosen Wilson functional rather than assuming the smooth-field identity already includes contact and cusp terms.

Required calculations:

1. Fix trace normalization, source-sector boundary conditions, field and generator conventions, Euclidean reflection and Lorentzian adjoint.
2. Obtain the displacement and internal-scalar operators from (4), checking tangential reparametrization invariance on compactly supported variations.
3. Track every term from |dot x| and from the normalization of n_j in (2), including terms that first appear at second order.
4. Determine which deformations, if any, preserve a common charge. Do not replace this calculation by the statement that the reference is BPS.
5. Compare constant n0 with the optional tangent-coupled profile n = M T, M^T M = I. The latter makes the scalar transport a one-form but changes the observable and adjoint conventions [P3].

The parent [endpoint result](../../sections/07_endpoints.tex) is a mandatory scope check for any later open-line extension. Its same-charge vanishing result applies to its specified ansatz; it neither forbids the straight heavy-source sector nor authorizes arbitrary endpoint polarizations.

**Deliverable A.** A conventions note specifying one primary observable, the first variation including its endpoint terms, the physical pairing, and the exact residual supersymmetry. A nonzero physical-adjoint control and any symmetry-forced zero should both be recorded.

**Decision.** Continue with the observable if its variation is well-defined and nontrivial. If a chosen BPS restriction makes it trivial, change the operator or deformation explicitly and repeat the audit; do not infer a nontrivial response from unused states in the theory.

## 5. Work package B: the smooth shape-response hierarchy

**Question.** What information beyond the known two-point function enters actual shape evolution?

Expand log Z[epsilon h,epsilon j] around the reference. At separated points the quadratic expression has the schematic structure

\[
\left.\partial_\epsilon^2\log Z[\epsilon h,\epsilon j]\right|_0
=\int d\sigma\,d\sigma'\,
\left[h^i(\sigma)h^j(\sigma')C_{DD,ij}(\sigma,\sigma')
+2h^i(\sigma)j^a(\sigma')C_{D\Theta,ia}(\sigma,\sigma')
+j^a(\sigma)j^b(\sigma')C_{\Theta\Theta,ab}(\sigma,\sigma')\right]
+\mathcal C_{\rm local}[h,j].
\tag{5}
\]

Theta denotes the internal-direction insertion. The local functional includes second variations of the operator, source normalization and the chosen contact prescription. Formula (5) is a bookkeeping target, not a computed renormalized Hessian. Symmetry may eliminate some separated mixed terms, but this must be established before deletion.

For a specified one-parameter family (h_t,j_t), pull the exact functional variation back along that family. Derive at least the first two equations for the relevant insertion expectations. Differentiating an insertion average also varies its normalization, the ordered Wilson factors, the insertion position and the insertion itself. Connected higher correlators and collisions will therefore appear.

Test three possible levels of control in this order:

1. A fully specified linear response about the fixed reference.
2. A controlled second-order shape calculation with a stated remainder regime.
3. A nonperturbative or systematically approximated insertion hierarchy.

No implication from level 1 to finite-amplitude closure is assumed. A projection onto a protected multiplet is valid only if the deformation and relevant operator products preserve that projection. The OPE of protected insertions can involve additional operators, so protected dimensions alone are not closure.

**Benchmark calculations.** Check compactly supported tangential variations, rotations of transverse directions, a smooth bump in one transverse component, and an independently specified internal rotation. Recover (3) at separated points with the chosen normalization. Compare a source-level derivation of the second variation with direct expansion of the path-ordered observable at a regulated perturbative order.

**Deliverable B.** Explicit first- and second-variation formulas, a list of correlators not determined by C_D, and either a justified closed sector or an explicit hierarchy with its first unresolved terms. Do not force a scalar ODE by defining its coefficient to be an unknown logarithmic derivative.

## 6. Work package C: retarded response, spectral measure and work

**Question.** Which positive quantity does the displacement response actually control?

Introduce a Lorentzian source only after specifying its physical meaning. A useful convention for a Hermitian defect observable D is an interaction H_int(s) = -h(s)D. Its retarded linear susceptibility is

\[
\chi_R(s)=i\,1_{s>0}\langle[D(s),D(0)]\rangle_0.
\tag{6}
\]

Derive the Wick-rotation factors relating D to the Euclidean displacement. Check the sign by a positive-energy oscillator control and by the force/work convention for the moving heavy source. Separate mean response from fluctuation correlators. A noiseless classical response cannot be inferred by dropping the latter.

There is a concrete spectral calibration available from (3). In the Euclidean spectral convention

\[
G_E(\sigma)=\int_0^\infty e^{-\Omega\sigma}\,d\mu(\Omega),
\qquad \sigma>0,
\]

the elementary integral for sigma^(-4) gives the separated-correlator density

\[
d\mu(\Omega)=\frac{C_D}{6}\Omega^3\,d\Omega.
\tag{7}
\]

Equation (7) is a formal continuum calibration of the separated two-point function. It does not fix contact terms or prove that an arbitrary boundary connection to this continuum is defined.

For a positive cutoff, for example dmu_Lambda = exp(-Omega/LambdaUV) dmu, examine

\[
\chi_{\Lambda}(p)=\int_0^\infty
\frac{2\Omega}{p^2+\Omega^2}\,d\mu_{\Lambda}(\Omega),
\qquad
Y_{\Lambda}(p)=p\chi_{\Lambda}(p),\qquad \Re p>0.
\tag{8}
\]

At finite cutoff this is a useful positive oscillator-response control, with supply h times the derivative of the conjugate expectation. The total response spectral mass is proportional to the fifth power of LambdaUV for (7). It therefore diverges as the cutoff is removed. The limit and the high-p expansion cannot be interchanged without analysis.

The tasks are to identify the divergent local terms, impose a physical renormalization prescription, and state on which source space the remaining response is meaningful. Subtracting local polynomials from a positive cutoff admittance does not automatically preserve positive-realness or a positive storage realization. An ultraviolet continuum is outside the WZW finite-mass theorem, but its admissibility must be proved independently.

For a source vanishing outside a finite time interval, the convention H_int = -hD gives supplied work through the explicit time dependence as -integral dot(h) <D>. Integration by parts relates this to integral h d<D>/ds when endpoint terms vanish. On finite subintervals the endpoint term is interaction energy and must be retained. A mechanical force/velocity interpretation requires a consistent sign convention and the heavy-source contribution as well.

Use the small-velocity radiation relation reviewed in the parent lessons note as a benchmark: the quadratic radiated functional is proportional to B times the integral of |d^2h/ds^2|^2. Its natural source norm has two derivatives. It is not the unweighted L2 norm of h. Choosing acceleration as a signal variable would require specifying its allowed range, the integration constants, preparation and causal readout; it is not a free relabelling of arbitrary L2 inputs.

**Deliverable C.** A convention-checked retarded kernel or distribution; its positive spectral data; explicit local ambiguities and chosen counterterms; an admissible source space; and a work/radiation identity at the order actually controlled. A failure to remove the cutoff with the proposed energy norm is a valid scoped result.

**Decision.** A finite-cutoff passive model is an intermediate control. Advance to a continuum physical claim only with the limiting domains, source conditions and energy terms stated. Positive emitted energy alone does not establish an all-input scattering contraction.

## 7. Work package D: actual Loewner growth and its completion

**Question.** How do the controlled defect variations extend to the actual geometric evolution requested in the parent program?

Use a deterministic driver u(t), initially u(t) = a t, with

\[
\partial_t g_t(z)=\frac{2}{g_t(z)-u(t)},\qquad
q(t)=\lim_{y\downarrow0}g_t^{-1}(u(t)+iy).
\tag{9}
\]

Embed the trace in a specified Euclidean plane of the same four-dimensional theory. The slit is geometric data for a probe; it is not a new physical boundary of the bulk action. Existing parts of a growing prefix remain fixed. Moving an unrelated reference curve by an inverse conformal map is a different observable family.

The parent [pure-YM calculation](../../notes/GENUINE_LOEWNER_TRACE_YM_HIERARCHY_20260921.md) supplies geometric controls. For the linear driver it obtains

\[
q(t)=2i\sqrt t+\frac{2a}{3}t-
\frac{ia^2}{18}t^{3/2}+O_a(t^2),
\qquad
\dot q=a-\frac2q.
\tag{10}
\]

The local tip ODE in (10) is specific to this driver. It is not obtained by substituting the singular tip into the forward map equation, and it is not asserted for a general driver.

### 7.1 First growing-contour observable

For direct comparison with the YM hierarchy, close the trace prefix by the straight return chord and take the normalized trace of (1). Start with the constant internal vector n0 on both branches. Define a rounded family C_(t,delta), with a fixed stated rounding rule at the base and tip, before differentiating a regulated expectation. First work on a compact interval t0 <= t <= T with t0 > 0 and rounding compatible with its local geometry. Study collapse to t = 0 separately. Specify the cusp-angle convention in the limit. The rounding scale and t are independent until a controlled limiting schedule is proved.

This is a gauge-invariant closed observable in the fixed bulk theory, but it is generally not BPS. The straight-line result (3) is a benchmark for smooth local variations; it cannot be applied to the collapsing or cusped loop without a derivation of the relevant limiting relation.

An essential control differs from pure YM. At a = 0 the trace and chord backtrack. The gauge parts invert, but a constant scalar arclength coupling has the same sign on the two traversals. Thus the full scalar-coupled Wilson transport is not automatically the identity. This is a property to calculate, not an error to remove by an arbitrary t-dependent normalization.

The optional profile n = M T changes this point: its transport is a one-form, so backtracking gives inverse transport at the smooth-field level. However, its connection is complex and its inverse is not automatically its physical adjoint. The parent's scalar-map adjoint rule and endpoint restrictions must be repeated for that observable. Compare the two prescriptions as separate families.

### 7.2 The first two evolution equations

Differentiate the prefix and chord transports directly using (4). Compute the cancellation of gauge endpoint terms and retain scalar tip, arclength, internal-profile and junction terms. Derive the first equation for the loop expectation, then differentiate its insertion average to obtain the ordered second-insertion equation.

For this stage the expected output is a concrete list of terms, including:

- curvature and scalar-gradient insertions on the moving completion;
- any tip or endpoint insertions that survive the chosen scalar prescription;
- explicit geometric derivatives and variation of the scalar profile;
- ordered double insertions and their coincident limits;
- regulator, perimeter, cusp and source-renormalization contributions;
- the normalization term if a physically specified reference ratio is used.

Do not copy the pure-YM curvature hierarchy unchanged. Its simple unitarity and backtracking identities depended on pure gauge transport.

### 7.3 Closure and regulator audit

Use Ward or Schwinger–Dyson equations only in a specified regulator. Preserve transverse four-dimensional currents, scalar interactions, fermionic terms and finite-N product expectations. A planar curve does not set bulk transverse derivatives to zero. The supersymmetric loop equations reviewed in [P5] act on an enlarged loop space; they are not automatically a closed equation along the one-parameter Loewner family.

If positive field flow is used for a smooth-field control, define the treatment of the scalars as well. Gauge flow alone is not assumed to preserve the supersymmetry of the original probe. The functional derivative of a flowed insertion includes the derivative of the flow map. The source results [P6] concern gauge-flow observables and do not prove every cusp or extended-operator limit required here.

Choose one primary renormalization route for the quantum calculation, such as point splitting plus a specified subtraction prescription or a perturbative supersymmetry-compatible scheme. Compare to flowed smooth-field identities as a separate control. Do not interchange t tending to zero, delta tending to zero, and removal of field or spectral regulators without estimates.

**Deliverable D.** A specified growing-contour observable, its first two ordered expectation-value equations, checks against the smooth variation and pure-YM limits, and an explicit residual inventory for closure. If the growing-trace limit is obstructed, identify the term and its dependence on the chosen completion rather than announcing a general SYM obstruction.

**Decision.** A nontrivial controlled hierarchy is sufficient to continue the physical investigation. A smooth BPS-line benchmark alone is insufficient to claim completion of the genuine-trace task.

## 8. Work package E: from a driven defect to a causal signal channel

**Question.** Can the physical response be placed in an autonomous or fully accounted input/output experiment with a fixed norm?

There are two different experimental interpretations to test. A prescribed trajectory is an externally driven source; its work must appear in the energy balance. An autonomous scattering construction instead prepares incoming radiation or other explicitly normalized excitations and reads outgoing amplitudes, including the heavy-source or defect state as part of the system.

For the driven construction, retain the source work and any change in its mechanical or interaction energy. Do not call a gain in an observed signal a violation of passivity when the prescribed motion has supplied additional energy. For an autonomous construction, specify the Hamiltonian, initial defect state, incoming and outgoing modes, coupling and asymptotic or finite-window measurement. Merely assigning an oscillator realization to a susceptibility is not an exact finite-coupling microscopic SYM model.

At linear order, define the actual response map before testing its norm. If a scalar time-translation-invariant channel S(p) exists, identify the physical time conjugate to p and its analytic domain. A genuinely time-dependent Loewner-driven system may instead have a two-time kernel S(s,s'); it need not be convolution. Introducing a stationary auxiliary channel would be an additional construction that must be justified.

The desired physical balance, in whatever norm the construction derives, is

\[
E_{\rm in}+W_{\rm drive}
=E_{\rm observed}+E_{\rm other}+\Delta E_{\rm stored}.
\tag{11}
\]

Specify whether these are coherent perturbation energies, inclusive quantum expectations, or one-particle amplitudes. Quantum fluctuations and source-state changes cannot be omitted when changing between those interpretations. Establish the nonnegativity and reference subtraction of storage in the regime claimed; an arbitrary renormalized local energy is not automatically nonnegative.

For an undriven, zero-excess-energy preparation with isometric input and output normalizations, a stronger target is

\[
\|f\|^2=\|V_L f\|^2+\|B_L f\|^2.
\tag{12}
\]

Construct B from physical unobserved states or later output. A reflected Wilson network might establish its norm, but cannot be defined as the square root of the desired deficit after assuming positivity. The [parent reflection analysis](../../sections/08_reflection.tex) supplies the required adjoint and domain questions.

A fixed reflected compression J* exp(-sH) J is not a viable nonlocal causal scalar response merely because H is positive. The WZW self-adjointness obstruction applies to that architecture. It does not exclude an oriented multichannel response or a unitary dilation with distinct incoming and outgoing channels. Simply adding channels to the same self-adjoint compression does not remove the analogous locality constraint.

**Deliverable E.** Either an explicit channel with its physical normalization, causality statement and energy identity, or a precise account of why the derived susceptibility cannot yet be made into that channel. State any input Sobolev norm and the exact additional map required to compare it with ordinary L2 radiation signals.

**Decision.** Only a defined linear response proceeds to arithmetic comparison. A positive scalar Wilson expectation, a positive two-point spectral density, or a quadratic radiation law is not enough to assert (12).

## 9. Work package F: optional arithmetic comparison

This package is conditional on the earlier physical construction. Its failure does not invalidate the preceding SYM result. The arithmetic definition must not be used to choose the physical coupling or counterterms retrospectively.

The comparison target is

\[
H(p)=\xi(\tfrac12+p),\qquad
K_\omega(p)=\frac{H(p-\omega)}{H(p+\omega)},\qquad
\partial_\omega\log K_\omega=-a_\omega.
\tag{13}
\]

The following ordered tests minimize unnecessary calculations:

| Test | Required result | Consequence of failure |
|---|---|---|
| Parameter dictionary | A derived physical parameter changes the response at fixed theory; its relation to omega is explicit | No arithmetic interpretation of that family yet |
| Identity endpoint | Strong convergence to I in the declared signal norm | A correlator normalization alone does not supply the transfer identity |
| Front and tangent | S_omega(p) has the leading power (2pi/p)^omega and the appropriate logarithmic shift tangent | Stop detailed prime fitting for this candidate |
| Complete local response | Correct gamma/rational contribution and fixed local subtraction in a stated convention | A matching scaling exponent alone is insufficient |
| First prime delay | A derived contribution at log(2), with c2(omega) = (2^omega - 2^(-omega))/sqrt(2) | No repair by adding a prescribed prime filter |
| Repetition and multiplicativity | The same mechanism gives log(4), log(3), log(6) with the required coefficients | A match to one echo is not a coefficient law |
| Causality and ordinary norm | A causal map with the required accumulated L2 deficit | Unit boundary modulus or a different positive norm is insufficient |

At half shift the needed first-prime coefficient is 1/2 and its omega derivative is (3/2) log(2). The high-positive-p logarithmic derivative is asymptotic to -log(p/(2pi)). These are comparison identities from the [arithmetic setup](../../WZW/sections/02_arithmetic_target.tex), not expected consequences of a displacement two-point function.

A fixed protected displacement dimension gives no variable front exponent merely by varying its normalization. A change in physical time scale also moves delays. Any model that passes the first tests must explain why all relevant amplitudes vary while the arithmetic delay locations remain fixed.

Retain the full completion. The [finite-place interface result](../../WZW/notes/FINITE_PLACE_RADIATION_INTERFACE_TEST_20260923.md) excludes treating an unchanged archimedean factor times a finite Euler product as a globally passive response in the relevant range. A finite-time-window comparison is different and may still be legitimate.

Finally, match the cumulative deficit rather than demanding that every instantaneous arithmetic shift generator be positive. The causal response may have a strong identity limit without operator-norm differentiability at zero. A proof on a stated smooth core is distinct from an all-input estimate, and both domains must be recorded.

**Deliverable F.** An explicit dictionary and a pass/fail record of the first applicable tests, with each failure scoped to the constructed observable and readout. No inference to RH follows from finite samples or from success at one fixed shift.

## 10. Validation, records and review

The work should be analytical first. Numerical checks should discriminate between independently obtained formulas rather than reproduce the same expression twice.

| Calculation | Independent control | What the control does not establish |
|---|---|---|
| Ordered shape variation | Direct transport on noncommuting smooth gauge/scalar backgrounds versus the insertion formula | A quantum expectation or continuum renormalization theorem |
| Physical adjoint and completion | Gauge covariance, reversed ordering and scalar-map checks | Full interacting reflection positivity |
| Second variation | Direct source expansion versus connected-correlator and contact bookkeeping | Nonlinear closure from the two-point coefficient |
| Retarded response | Spectral representation versus continued time-domain correlator at a fixed regulator | A regulator-free microscopic scattering model |
| Work identity | Direct source work versus storage and outgoing energy in a specified linear control | Positivity after arbitrary counterterm subtraction |
| Genuine trace | Independently reconstructed Loewner trace and prefix transport; a = 0 and both signs of a | General-driver trace regularity |
| Ultraviolet limit | Analytic tail/domain estimates, then cutoff and precision variation | A proof from numerical convergence alone |
| Proposed all-input norm | An operator/form argument with controlled complements | An upper bound inferred only from a finite matrix |

For the spectral model (8), explicitly label the cutoff response as an auxiliary linear control. An exponential spectral cutoff is not claimed to be a supersymmetry-preserving regulator of the complete gauge theory. Its role is to test signs, spectral normalizations and energy accounting before making a continuum statement.

Use small exact controls where available, including geometric identities, source normalization and matrix ordering. Use high-precision floating diagnostics only for the remaining analytic comparisons, with truncation and precision parameters saved. Do not create a large path ensemble or zero table for a task that can be resolved analytically.

Future programs belong in `N4SYM/numerics/`, compact replay records alongside them, and research audits in `N4SYM/reviews/`. Each record should distinguish exact identities, perturbative approximations, floating diagnostics and interval certificates. Follow the repository [large-file policy](../../../../../../LARGE_FILES.md); no third-party PDFs or large regenerable arrays should be committed.

Independent specialist review should examine the physical adjoint and source sector, contact terms and Wick rotation, the order of cusp and ultraviolet limits, the extent of the Ward identities, and any claimed passivity after renormalization. A same-assistant audit is useful but must be labelled as such.

## 11. Milestones and stopping criteria

Milestones are dependency-based rather than calendar promises. They record completed results or explicit obstructions, not the existence of a draft document.

| Milestone | Prerequisite | Concrete completion criterion |
|---|---|---|
| M0: observable audit | Primary conventions and parent adjoint review | One fixed theory, source sector, scalar profile, regulator and reflection/adjoint prescription |
| M1: smooth hierarchy | M0 | First and second variations with all contact terms either determined or explicitly unresolved |
| M2: spectral and work benchmark | M0; M1 for the source interpretation | A retarded convention, cutoff spectral control, source norm and work/radiation accounting |
| M3: genuine-trace hierarchy | M0–M1 plus a specified rounded completion | First two growing-contour equations and a correct constant-driver control |
| M4: closure or controlled residual | M1 and/or M3 | A closed family, a controlled hierarchy, or a quantified/listed residual under explicit assumptions |
| M5: causal channel | M2 and the chosen physical coupling | Actual preparation/readout, causal map and energy balance in a declared norm |
| M6: arithmetic assessment | M5 | A derived dictionary and the first decisive matching or exclusion calculation |

M2 and M3 may be pursued as separate calculations after their shared conventions are fixed. M3 remains required for a claim about genuine Loewner growth even if M2 succeeds. M6 is optional for completion of the physical investigation.

Stop or redirect the particular construction when:

- the complete chosen observable vanishes by a charge selection rule;
- its protected restriction makes the selected deformation trivial;
- the proposed closure discards an independent insertion with no controlling identity;
- a fixed reflected readout is required to be simultaneously self-adjoint, scalar, causal and nonlocal;
- the regulator removal lacks a defined source domain or loses the stated energy bound;
- a purported transfer obtains its positivity only by changing the norm to depend on the desired answer;
- the physical parameter changes only amplitudes when a variable exponent is required, or changes delays when fixed arithmetic delays are required;
- an external source supplies unaccounted work to an alleged passive channel.

A failure at one of these points should be written as a scoped proposition or unresolved obligation, with the valid preceding results retained. It should not be extended into a theorem about every Wilson observable or every N=4 SYM realization.

## 12. Suggested first research session

The first session should complete a bounded conventions and quadratic-response audit, not attempt all packages at once:

1. Read the parent lessons note, smooth variation, endpoint and reflection sections, and [P1, Sections 3–4]. Fix the heavy-source sector and the deformation (2).
2. Derive the first variation and the second-variation bookkeeping for a real smooth transverse bump with j = 0, retaining arclength and local terms. Treat a transverse internal bump as a separate normalization control.
3. Recover the separated displacement coefficient (3) from the chosen conventions. State which local terms are fixed by the reference and Ward identities and which require a counterterm prescription.
4. Derive the Euclidean spectral representation (7) and the finite-cutoff retarded response (8). Compare the work functional with the physical radiation benchmark, with the source norm explicit.
5. Write a short status result: the response actually obtained, unresolved contact or continuation terms, and whether a physical scattering channel has been defined. Record a precise next calculation for the rounded growing trace.

Expected files are a research note, a small diagnostic only if needed for an independent comparison, and a same-assistant audit clearly distinguished from specialist review. Do not alter the gauge coupling to fit the arithmetic target, replace genuine growth by an inverse-map test without labelling the change, or promote a smooth-line result into a cusp theorem.

## 13. Sources and provenance

### Primary literature

- **[P1]** D. Correa, J. Henn, J. Maldacena and A. Sever, *An exact formula for the radiation of a moving quark in N=4 super Yang Mills*, [arXiv:1202.4455](https://arxiv.org/html/1202.4455). Sections 3–4 supply the displacement/internal-angle conventions and the two-point, cusp and radiation relation. The accessible full text was consulted for this proposal. This is the main physical benchmark, not a derivation of the proposed Loewner or arithmetic channel.
- **[P2]** M. Billò, V. Gonçalves, E. Lauria and M. Meineri, *Defects in conformal field theory*, [arXiv:1601.02883](https://arxiv.org/abs/1601.02883). Reference for a full audit of defect Ward identities and contact terms. Its metadata and abstract were checked here; the relevant full derivations remain part of work package A/B.
- **[P3]** K. Zarembo, *Supersymmetric Wilson loops*, [arXiv:hep-th/0205160](https://arxiv.org/abs/hep-th/0205160). Tangent-dependent scalar-coupling comparison. Detailed formulas are also recorded in the parent's smooth-variation note; the proposed new family needs its own symmetry audit.
- **[P4]** E. Baker, *Supersymmetric Open Wilson Lines*, [arXiv:1102.4948](https://arxiv.org/abs/1102.4948). Endpoint and semicircle controls in its specified defect setting. This is not an automatic endpoint construction for the pure bulk probe sector selected here.
- **[P5]** Y. Makeenko, *Topics in Cusped/Lightcone Wilson Loops*, [arXiv:0810.2183](https://arxiv.org/abs/0810.2183). Loop-equation and supersymmetric loop-space reference. Use the actual operator and regulator hypotheses rather than interpreting a functional loop equation as a closed scalar Loewner ODE.
- **[P6]** M. Lüscher, *Properties and uses of the Wilson flow in lattice QCD*, [arXiv:1006.4518](https://arxiv.org/abs/1006.4518), and M. Lüscher and P. Weisz, *Perturbative analysis of the gradient flow in non-abelian gauge theories*, [arXiv:1101.0963](https://arxiv.org/abs/1101.0963). Gauge-flow controls and their scope; no supersymmetric scalar-flow or cusped-network theorem is imported.

The non-P1 references were checked at the level stated above and against their existing use in the parent research. This writing session is not a new full specialist audit of those papers. External papers are linked rather than stored in the repository.

### Project records

- [Lessons from WZW for YM and N=4 SYM](../../notes/LESSONS_FROM_WZW_FOR_YM_AND_N4SYM_20260923.md).
- [Genuine YM trace hierarchy](../../notes/GENUINE_LOEWNER_TRACE_YM_HIERARCHY_20260921.md) and [physical continuation](../../notes/RESEARCH_CONTINUATION_AFTER_GROWING_TRACE_20260921.md).
- [Smooth Wilson variation](../../sections/05_variation.tex), [endpoint selection and adjoint](../../sections/07_endpoints.tex), and [reflection pairing](../../sections/08_reflection.tex).
- [Earlier regular-readout exclusion](../../notes/FIXED_WINDOW_WILSON_RESPONSE_OBSTRUCTION_20260920.md).
- [WZW reflected-collar exclusion](../../WZW/notes/BOUNDED_ARITHMETIC_READOUT_TEST_20260923.md).
- [Modular scattering benchmark](../../WZW/notes/MODULAR_HODGE_SCATTERING_AND_CUSP_COUPLING_TEST_20260923.md).
- [Thermal front-rigidity theorem and its hypotheses](../../WZW/notes/THERMAL_BOUNDARY_COUPLING_AND_FRONT_RIGIDITY_TEST_20260923.md).

This proposal was drafted for Edward Baker using substantial GPT-6 (Codex) assistance in synthesis, source comparison, mathematical planning and document preparation. Its checkpoints, source-space distinctions and work packages are research design, not completed physical or arithmetic results. Independent mathematical and physical review is outstanding. No numerical suite has been run for the proposal and no manuscript snapshot has been created.

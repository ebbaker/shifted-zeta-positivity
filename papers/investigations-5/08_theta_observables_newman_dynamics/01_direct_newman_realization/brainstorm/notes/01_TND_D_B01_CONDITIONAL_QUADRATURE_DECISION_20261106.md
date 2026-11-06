# TND-D-B01: conditional quadrature construction and frozen next contract

6 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**, verified in turn metadata. Direct branch chat0001, thread `01a1af3f-44ac-70a3-a6ee-303e2065d468`. **B — conceptual decision**, plan r1. [Input versions][inputs]; [sole live register][progress].

**Decision: select an externally prepared, conditional-state realization with one monitored quadrature apparatus.** The source is the canonical theta density, supplied in physical position. The unchanged free kinetic Hamiltonian remains present. A calibrated count measurement supplies the quadratic attenuation, and a literal cosine expectation, together with the no-count probability and one initial mass calibration, is the proposed absolute Newman readout. Laboratory time runs toward decreasing Newman parameter on the single slab \(-1/2\leq\lambda\leq1/2\).

This completes B01 at **conceptual selection and contract scope**. The [TND-D-E01 r1 request][request] is frozen for Sol and **not activated or executed**. Its state-domain, complete-instrument and readout assertions are proof targets, not accepted realization results. This is an ideal conditional quantum-operation interpretation, not an intrinsic theta preparation, a microscopic apparatus construction, or a collision estimate.

| Next task | Type | Recommended model | Readiness/dependency | Expected output |
| --- | --- | --- | --- | --- |
| **TND-D-E01 r1** | E | **Sol**; the source, count instrument, clock, observable and proof method are fixed | Request issued; awaiting author activation | Complete-spectrum conditional realization on the frozen slab, or an exact failure in this construction |
| TND-D-E02 | E | Sol; fixed claim/domain/readout assessment | E01 return and shared TND-E03 disposition | Scoped assessment; remains pending |

## 1. Fixed model and chosen physical object

Retain \(\mathcal H=L^2(\mathbb R,dv)\otimes K\), \(K=L^2(S^2,\Sigma;d\Omega)\), on the radius-\(1/2\) cylinder. Metric volume is \(dv\,d\Omega/4\); multiplication of a product-measure spinor by 2 is its isometric conversion. Put
\[
X=v,\quad P=-i\partial_v,\quad A=D^2,\quad
L_0=P^2+4A,\quad H_{\rm kin}=\varepsilon L_0,\quad
\omega=\varepsilon/\hbar,\quad U(t)=e^{-i\omega tL_0}.
\tag{D1}
\]
Here \(\varepsilon=\hbar^2/(2m\ell_0^2)>0\) fixes units; \(\omega\) and the controller rate below have units of inverse laboratory time. The fixed curvature contribution \(2\varepsilon\) is already contained in \(L_0\). These are inherited from [parent E01 §§1–3][e01], with its proof-author qualifications.

The evolved object is a **mixed spinor density operator**, pure radially and mixed over the complete angular spectrum. Set
\[
R=\frac{(4\sqrt A)^{-1}e^{-\pi A}}{Q_1(\pi)},\qquad
R|_{P_nK}=r_nI,\quad r_n=\frac{e^{-\pi n^2}}{4nQ_1(\pi)}.
\tag{D2}
\]
Every \(n\geq1\), both angular Dirac signs, and all \(2n\) states per sign have positive ensemble weight. \(R\) is an angular preparation, not a full-cylinder Gibbs state. There is no passive reference bank or additional physical spinor multiplicity. Its normalization and moments are local E01 obligations using the complete Green trace in [E01 §4, (13)–(14)][e01].

The complete angular ensemble is a spectator to the radial filtering in the interaction frame. Keeping it is full spectral accounting, not an intrinsic generation of the theta profile or a spinor-specific estimating advantage.

The retained radial Fourier transform has factor \((2\pi)^{-1/2}\), with \(k\in\mathbb R\). The first-order Dirac branches remain \(\pm\sqrt{k^2+4n^2}\), each of multiplicity \(2n\); the square has multiplicity \(4n\). The apparatus is not diagonal in \(k\), and its effective generator is not being assigned those free energy eigenvalues. Radial evenness reduces the square, not the first-order Dirac operator. No radial wall or discrete normalizable momentum mode is inserted.

## 2. Supplied preparation and absolute source calibration

Freeze \(\lambda_*=1/2\), \(Z_*=2H_{1/2}(0)>0\), and
\[
F_\lambda(v)=e^{\lambda v^2}\Phi(v),\quad
f_\lambda(v)=\sqrt{\frac{F_\lambda(v)}{2H_\lambda(0)}},\qquad
\rho_*=|f_{1/2}\rangle\langle f_{1/2}|\otimes R.
\tag{D3}
\]
The radial preparation is the real positive square root, with constant phase. An external loader identifies source coordinate \(u\) with dimensionless physical position \(v=x_{\rm phys}/\ell_0\). On \(u\geq0\) it uses the full scan
\[
\beta(u)=\pi e^{4u},\quad p(u)=e^uQ_1(\beta(u)),\quad
\Phi(u)=\frac{p''(u)-p(u)}8
=e^u\sum_{n\geq1}(2n^4x^2-3n^2x)e^{-n^2x},\quad x=\pi e^{4u},
\tag{D4}
\]
with the complete smooth even theta extension to negative \(v\). \(Z_*\) is the integral of that unchanged source. Neither the scan, its derivative readout, the placement map, the square-root loader nor the angular ensemble is derived from probe translation or free evolution. They are supplied preparations. [E01 §§4–6][e01] and the accepted [MC11 source assessment][mc-review] distinguish their arithmetic inputs from physical preparation.

The reflection input uses [DLMF 20.7.32](https://dlmf.nist.gov/20.7.E32) at \(z=0\), \(\tau=iR^2\), \(R>0\), with principal square roots; that passage was rechecked. Its use for the differentiated canonical source is inherited through those local notes, not transferred to a truncated or reweighted source.

The canonical calibration remains
\[
H_\lambda(z)=\int_0^\infty F_\lambda(u)\cos(zu)\,du,
\qquad H_0(z)=\xi((1+iz)/2)/8.
\tag{D5}
\]
Rodgers–Tao v5, Introduction (1)–(4) and the following heat equation, were rechecked for precisely this normalization and sign; see the [canonical record][rt-record]. Their zero theorem is not imported into this construction. The initial scale \(H_{1/2}(0)\) is supplied absolutely, rather than inferred from a normalized state.

## 3. The single extension: D-X1 monitored co-moving quadrature

**Declare exactly one apparatus extension, D-X1:** a count instrument coupled to the freely transported quadrature
\[
Q_t=U(t)XU(t)^*=X-2\omega tP,\qquad
C_t=\sqrt\gamma\,Q_t,\quad \gamma>0.
\tag{D6}
\]
The equality and its domains are E01 proof targets; the unitary-conjugation definition fixes the operator. The proposed no-count strong equation is
\[
\partial_t\widetilde\psi_t=
\left(-i\omega L_0-\frac\gamma2Q_t^2\right)\widetilde\psi_t,
\qquad H_{\rm eff}(t)=H_{\rm kin}-\frac{i\hbar\gamma}{2}Q_t^2.
\tag{D7}
\]
This retains free kinetic motion and introduces a specified nonunitary measurement channel. It is not a claim that the free Hamiltonian generates Newman evolution.

Freeze the complete count instrument, for \(0\leq s\leq t\leq1/\gamma\), by its proposed bounded Kraus operators
\[
K_j(t,s)=U(t)\,e^{-aX^2/2}\frac{(\sqrt aX)^j}{\sqrt{j!}}\,U(s)^*,
\qquad a=\gamma(t-s),\quad j=0,1,2,\ldots.
\tag{D8}
\]
At \(a=0\), use \(K_0(t,t)=I\) and \(K_j(t,t)=0\) for \(j>0\). The count label is an apparatus outcome, not an angular quantum number. E01 must prove boundedness, strong completeness \(\sum_jK_j^*K_j=I\), trace convergence, and no-count cocycle composition. Thus an unbounded infinitesimal coupling is not substituted for a defined measurement operation.

The no-count/norm convention is checked against Castin–Dalibard–Mølmer, [arXiv:0805.4002v1 §1 (2), (4)–(11)](https://arxiv.org/html/0805.4002v1). Generalized-measurement normalization is checked in Jacobs–Steck, [v1 §III (17)–(19)](https://arxiv.org/html/quant-ph/0611067v1). These sources do not prove this unbounded cylinder construction; that is assigned locally. [Source records][measurement-refs] preserve passage and retrieval scope.

**One local clarification, LC-B01:** a stationary position-loss term alongside \(H_{\rm kin}\) would not yield the stated density, since \(P^2\) and \(X^2\) do not commute. D-X1 and the readout both follow \(Q_t\). This makes the compensation explicit rather than suppressing kinetic dispersion. Preparation and final measurement are the declared interfaces of this one apparatus model; no second controller, fitted potential or auxiliary flow is selected.

## 4. Clock, conditioning and signed readout

Freeze laboratory time and Newman time as
\[
0\leq t\leq1/\gamma,\qquad \lambda(t)=\frac12-\gamma t.
\tag{D9}
\]
This is decreasing Newman time. It is not proper/Euclidean heat time. Increasing \(\lambda\) by reversing the attenuation would require a different operation; the unbounded positive-increment multiplier is not licensed here.

Define \(\widetilde\rho_t=K_0(t,0)\rho_*K_0(t,0)^*\), success probability \(p_t=\operatorname{Tr}\widetilde\rho_t\), and conditional state \(\rho_t=\widetilde\rho_t/p_t\). The identities to be proved are
\[
\rho_t=U(t)(|f_{\lambda(t)}\rangle\langle f_{\lambda(t)}|\otimes R)U(t)^*,
\qquad p_t=\frac{H_{\lambda(t)}(0)}{H_{1/2}(0)}.
\tag{D10}
\]
For real \(k\), the fixed signed observable is \(O_t(k)=\cos(kQ_t)\), a bounded self-adjoint contraction. Its two effects are \((I\pm O_t(k))/2\). Record their joint probabilities with the no-count event, \(q_\pm(t,k)\). The proposed absolute observation is
\[
\boxed{H_{\lambda(t)}(k)
=H_{1/2}(0)\,p_t\operatorname{Tr}(\rho_tO_t(k))
=H_{1/2}(0)[q_+(t,k)-q_-(t,k)].}
\tag{D11}
\]
Successful samples alone give \(H_\lambda(k)/H_\lambda(0)\). Discarding the success frequency loses the scale. The observation is the cosine transform of a **position density**; neither the Fourier amplitude of \(f_\lambda\) nor its momentum probability is \(H_\lambda\). A linear source-amplitude model would have a different tangent and readout. Here the interaction-frame tangent is to be checked with its factor \(1/2\):
\[
\partial_t f_{\lambda(t)}=-\frac\gamma2
\left(X^2-\langle X^2\rangle_{f_{\lambda(t)}}\right)f_{\lambda(t)}.
\tag{D12}
\]
At later times the laboratory position density need not be the theta density: (D10) identifies the distribution of \(Q_t\), or equivalently the interaction-frame position. The source is loaded once. No source is re-imprinted during the evolution. The attenuation is in the conditional no-count branch; no claim is made that the unconditioned ensemble follows the Newman family.
Complex \(z\) enters only through analytic continuation of (D5); \(O_t(z)\) is not declared a bounded physical measurement. The inherited raw scalar \(G\) integral retains its initial strip \(|\operatorname{Im}z|<1\); it is not used as a replacement source.

## 5. Domains, evidence and the execution boundary

The [packet][request] fixes maximal weighted domains for \(\mathcal D_C,L_0^p,X^q,P^q,Q_t^q\), a smooth core, the strong-equation domain, all angular and count sums, the entire real radial spectral line, and finite-order quantifiers. Smoothness and finite energy of the **square-root** preparation must be proved locally; they do not follow just by citing a Hilbert-space embedding of \(F_\lambda\). The square-root bound uses the positive first-summand lower bound and full derivative majorants, not derivatives of a reflected finite truncation.

| Ingredient | Disposition at B01 return |
| --- | --- |
| Complete free cylinder, angular trace and canonical source | Inherited with MC11 internal acceptance and shared-premise qualifications |
| Parent E01 spectra/normalization/compact-parameter derivative comparison | Proof-author work; shared TND-E03 assessment remains pending |
| Investigation05 scalar/heat benchmarks | Existing same-assistant checking and stated classes retained; no new transfer claimed |
| Theta loader, \(u=v\), angular ensemble, initial calibration | Supplied model data, not intrinsically derived |
| D-X1 count instrument and co-moving cosine measurement | Selected ideal apparatus; local proof/checks E01-L1–L3 required |
| Intrinsic theta preparation or finite-resource hardware | Not obtained; not a prerequisite silently assumed for the stated ideal-operation target |
| MC11-OBS-E01 and MC11-E05 | External and unchanged; no pending Note13-only measurement claim treated as accepted |

One conceptual pass and the single clarification LC-B01 were used. No E01 proof pass, numerical acquisition, additional mechanism, independent review or successor activation was performed. The request's success is a proof-author representation theorem conditional on supplied preparation/apparatus, not intrinsic preparation or an RH consequence.

## 6. Control screen and classification

Under [avoid/01][a01], this is a **physical interpretation and representation contract**. Consult the [result index][results], [control register][controls] and [patterns index][avoid]; [avoid/03][a03] disallows inferring a sign gain from a re-realization, and [avoid/07][a07] limits any failure to this construction.

| Inherited controls | Exact distinction and what survives |
| --- | --- |
| Euler-factor sources | Fail the unchanged canonical arithmetic source; applicable positive smooth density preparations and the same count/cosine mechanism survive. Recorded positive-time witnesses lie within the chosen slab where the hypotheses hold. |
| Weighted-square and finite-prime perturbations | Fail complete unit weights/full smooth canonical reflection. Half-line positivity or finitely matched endpoints do not prove the square-root domain at the origin. Generic filtering still cannot supply a collision exclusion. |
| Reflected super-Gaussian; smooth shape and positive-primitive controls | Fail the exact canonical arithmetic expansion. Their applicable positivity, reflection, tail and cosine properties survive. No discriminating estimate has been selected. |
| Atomic/finite-profile, smooth-density/two-channel and other generic controls | Name their actual class: Fourier data can survive while an atomic or nonsmooth source fails this smooth square-root preparation. For a smooth replacement, all preparation/domain/tail premises must be checked on its witness range; no automatic exclusion is inferred. Gaussian-tail controls require their own admissible preparation interval. |

This is an analytical comparison with recorded controls, not new tests. Positivity of \(p_t\), complete positivity of an instrument and boundedness of a cosine observation do not forbid its signed expectation from vanishing or colliding. Naming theta as the supplied input provides no quantitative separating inequality.

**Next: [E] TND-D-E01 r1 — Sol.** Prove the single frozen instrument/state/readout contract, including the explicitly assigned local checks, or record its precise failed premise. Author activation is still required; E02 and later tasks remain pending.

[inputs]: ../../research-progress/handoffs/01_TND_D_B01_INPUT_VERSIONS_20261106.json
[progress]: ../../research-progress/01_DIRECT_NEWMAN_REALIZATION_RESEARCH_PROGRESS_20261105.md
[request]: ../../research-progress/handoffs/02_TND_D_E01_R1_REQUEST_20261106.md
[e01]: ../../../notes/02_TND_E01_R1_GEOMETRIC_HAMILTONIAN_AND_COMPLETE_SPECTRAL_COMPARISON_20261105.md
[mc-review]: ../../../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/reviews/05_MC11_AR_E04_R1_MODEL_SOURCE_AND_SCOPED_TRANSFER_ASSESSMENT_20261105.md
[rt-record]: ../../../../02_heat_flow_rh_applications/references/sources.json
[measurement-refs]: ../../references/01_TND_D_B01_MEASUREMENT_SOURCES_20261106.json
[results]: ../../../../../../result-summaries/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../avoid/README.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a03]: ../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md

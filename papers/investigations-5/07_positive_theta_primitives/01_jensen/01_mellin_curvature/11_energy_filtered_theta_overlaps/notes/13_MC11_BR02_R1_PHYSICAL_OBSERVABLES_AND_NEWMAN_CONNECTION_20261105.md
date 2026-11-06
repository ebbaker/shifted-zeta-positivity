# MC11-BR02 r1: physical observables and the Newman connection

5 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**, verified in current turn metadata. Thread `01a1ac6b-7e6e-7ea3-86f7-0f9fd9e3a1bd`, existing MC11 history0006. **B — brainstorm**, bounded observable/model audit requested by the author and classified before new derivations in [Register02](../research-progress/02_ANGULAR_RADIAL_THETA_MODEL_RESEARCH_PROGRESS_20261105.md).

**Disposition: explicit observable dictionary and an exact crosswalk to the earlier Newman state; no native preparation/evolution or signed collision estimate is established.** The energy-moment formulas below are direct consequences of the accepted MC11 response and source map. The normalized Newman state and its evolution were already derived in the [10 October moving-state note](../../../../../../../papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/03_susy_dirac_hodge/notes/1_MOVING_THETA_GROUND_STATE_WARD_RESIDUAL_AND_GAP_LIMIT_20261010.md); they are reused, not claimed as a new mechanism. Proof-author analytical checks only, no separate assessment or numerics. The accepted manuscript and B01/E05 statuses are unchanged.

| Next task | Type | Recommended model and reason | Readiness | Output |
| --- | --- | --- | --- | --- |
| MC11-OBS-E01 r1 — check the observable/Newman dictionary | E | Sol; formulas, domains, parameters and comparison tests are fixed | Ready for author selection; not activated | Assessment of this note, with corrections and precise physical scope |
| Further BR02 revision — native preparation or new signed correlation | B | Astra; a mechanism beyond the existing response is a conceptual choice | Needs a specified proposed mechanism; not activated | Concrete preparation/generator or source-sensitive estimate, or scoped return |

## 1. The physical claim that the current manuscript does and does not make

The [manuscript](../manuscript/main.tex), especially its fixed-observation subsection, defines a self-adjoint complete-cylinder operator and an exact response. It does not derive the source coordinate from radial position or identify Newman time with physical evolution. Its [earlier terminology correction](../brainstorm/notes/03_MC11_THERMAL_PARAMETER_AND_ORBITAL_TERMINOLOGY_20261104.md) already distinguishes thermal parameters from quantum coordinates and auxiliary source vectors from prepared particles.

The missing exposition is a dictionary specifying which operator is measured, in which state, with what normalization, and whether the result is a single expectation, a parameter scan, or a prepared-state amplitude. A positive Hamiltonian does not make the zeros of an arbitrary response its energy eigenvalues. In MC11 the square energies are known; the xi zeros arise only after the signed transform.

Use distinct parameters throughout:

| Symbol | Meaning |
| --- | --- |
| `v` | Physical radial coordinate of the cylinder |
| `tau` | Evolution/proper time for the cylinder operator |
| `beta` | Angular damping; this replaces the manuscript's `t` here |
| `u = log(beta/pi)/4` | Auxiliary source coordinate, with `u >= 0` in the original integrals |
| `s` | Excited-angular-shell filter, in `[0,1]` |
| `lambda` | Newman deformation parameter; independent of the preceding parameters |
| `x` | Real Fourier/observation parameter; not an angular energy |

The dimensionless angular energy is \(A=D^2\), with eigenvalues \(n^2\) and multiplicity \(4n\). The angular contribution to the radius-1/2 cylinder square is \(4A\). A Gibbs weight \(e^{-\beta A}\) thus uses inverse temperature \(\beta/4\) for that angular contribution in the chosen units.

## 2. Exact theta response and a legitimate angular-state interpretation

Keep the accepted free operator and observation:
\[
L_0=-\partial_v^2+4A,\qquad
W=K_{L_0^{-1}}(0,0)=(4\sqrt A)^{-1},\qquad
B_s=P_1+s(I-P_1).
\]
For every \(\beta>0\),
\[
R_s(\beta)=B_sW e^{-\beta A},\qquad
Q_s(\beta)=\operatorname{Tr}R_s(\beta)
=e^{-\beta}+s\sum_{n\ge2}e^{-\beta n^2}.
\tag{1}
\]
The full Jacobi theta constant is \(\vartheta_3(0,e^{-\beta})=1+2Q_1(\beta)\). This distinguishes the theta trace, the differentiated source below, and its xi transform.

\(R_s\) is positive trace class and has positive trace even at \(s=0\). Hence
\[
\rho_{s,\beta}=R_s(\beta)/Q_s(\beta)
\tag{2}
\]
is an actual angular density operator. It is **not** asserted to be a partial trace of a full-cylinder Gibbs state: the latter has infinite trace on the complete radial line.

A concrete ideal measurement interpretation is available. On the compact angular system prepare
\[
\sigma_\beta=e^{-\beta A}/Z_{\rm ang}(\beta),\qquad
Z_{\rm ang}(\beta)=\operatorname{Tr}e^{-\beta A}.
\]
The bounded effect \(F_s=B_sA^{-1/2}=4B_sW\) has eigenvalues \(1\) at \(n=1\) and \(s/n\) at \(n\ge2\), so \(0\le F_s\le I\). The accepted outcome of the measurement with Kraus operator \(\sqrt{F_s}\) has probability and conditional state
\[
p_{\rm acc}=4Q_s/Z_{\rm ang},\qquad
\frac{\sqrt{F_s}\sigma_\beta\sqrt{F_s}}{p_{\rm acc}}=\rho_{s,\beta}.
\tag{3}
\]
Commutation of all factors proves (3) directly. It specifies a valid ideal angular protocol; no microscopic apparatus, thermalization mechanism or automatic cylinder preparation is claimed. Absolute recovery of \(Q_s\) from this protocol requires the stated partition-function calibration; normalized energy data alone discard that scale. Equations (1) and (3) are equivalent readouts, not an assertion that this protocol replaces the accepted Green observation.

For every fixed integer \(r\ge0\), Gaussian spectral convergence justifies
\[
(-1)^r Q_s^{(r)}(\beta)
=Q_s(\beta)\operatorname{Tr}(\rho_{s,\beta}A^r).
\tag{4}
\]
The unbounded energy powers are defined spectrally and have all finite moments in (2). Thus the angular energy and its powers are relevant observables, not merely labels attached to the sum.

## 3. Which energy observable gives the theta source?

Set \(\beta=\pi e^{4u}\). The accepted external map becomes
\[
\Phi_s(u)=\frac18(\partial_u^2-1)[e^uQ_s(\beta)]
=e^u[2\beta^2Q_s''(\beta)+3\beta Q_s'(\beta)].
\]
Using (4), define
\[
\mathcal O_\beta=2\beta^2A^2-3\beta A.
\]
Then the exact dictionary is
\[
\boxed{\Phi_s(u)=e^u Q_s(\beta)
\langle\mathcal O_\beta\rangle_{\rho_{s,\beta}},\qquad
\beta=\pi e^{4u}.}
\tag{5}
\]
Proof: differentiation first gives \(\partial_u(e^uQ)=e^u(Q+4\beta Q')\) and then \(\partial_u^2(e^uQ)=e^u(Q+24\beta Q'+16\beta^2Q'')\). Subtract and divide by eight. This verifies both constants and the sign of the first energy moment. On the source half-line \(\beta\ge\pi\), every eigenvalue \(\beta n^2(2\beta n^2-3)\) of \(\mathcal O_\beta\) is positive. There is no positivity assertion for this operator at every \(\beta>0\).

The ordinary energy fluctuations also satisfy \(\partial_\beta\langle A\rangle=-\operatorname{Var}(A)\), at fixed s. That thermodynamic identity controls an unsigned response. It does not provide determinant or collision signs.

The first source derivative uses the third energy moment:
\[
\Phi_s'(u)=e^uQ_s(\beta)
\langle-8\beta^3A^3+30\beta^2A^2-15\beta A\rangle_{\rho_{s,\beta}}.
\tag{6}
\]
For the full source, its logarithmic slope is therefore the explicitly measurable ratio
\[
-\frac{\Phi_1'}{\Phi_1}
=\frac{8\beta^3\langle A^3\rangle-30\beta^2\langle A^2\rangle+15\beta\langle A\rangle}
 {2\beta^2\langle A^2\rangle-3\beta\langle A\rangle}.
\tag{7}
\]
The denominator is positive on this half-line. Formula (6) is the already accepted derivative recurrence applied to \(2y^2-3y\); (7) puts the old Newman score in angular-observable terms. Higher finite source jets similarly require higher energy powers. This dictionary does not bound their signed Fourier correlations.

The raw moments used by MC11 are parameter-scan functionals:
\[
c_j(s)=\int_0^\infty\frac{u^{2j}}{(2j)!}
e^uQ_s(\pi e^{4u})\langle\mathcal O_{\pi e^{4u}}\rangle\,du.
\tag{8}
\]
This includes the raw \(j=0\) coefficient with no endpoint compensation. A determinant \(D_{q,k}\) is a signed nonlinear functional of these measurements, not itself an ordinary Gibbs expectation or a nonnegative probability. The existing wedge identity is an exact cross-amplitude; interpreting it operationally would require preparing both wedge families and retaining a phase reference. Squaring its modulus loses the sign sought by the mathematics. All filtered endpoint qualifications in Note08 remain in force.

## 4. The direct Newman crosswalk

From here set **s=1**, the complete canonical theta source \(\Phi=\Phi_1\). Do not transfer its evenness to a filtered source. In the Rodgers–Tao convention,
\[
H_\lambda(x)=\int_0^\infty e^{\lambda u^2}\Phi(u)\cos(xu)\,du,
\quad H_0(x)=\tfrac18\xi((1+ix)/2),
\quad \partial_\lambda H_\lambda=-\partial_x^2H_\lambda.
\tag{9}
\]
Substitution of (5) gives the full upstream observable formula
\[
\boxed{H_\lambda(x)=\int_0^\infty e^{\lambda u^2+u}
Q_1(\pi e^{4u})\langle\mathcal O_{\pi e^{4u}}\rangle
\cos(xu)\,du.}
\tag{10}
\]
This is a weighted scan over angular damping, with a signed readout. It is not the evaluation of one thermal expectation at \(\beta=\lambda\), nor evolution in the retained filter s. The energy trace, differential source and Fourier cancellation have distinct roles.

The link to the coefficient side is also exact. For
\[
c_j(\lambda)=\int_0^\infty\frac{u^{2j}}{(2j)!}e^{\lambda u^2}\Phi(u)\,du
\]
(a new parameterized notation, with \(c_j(0)=c_j(s=1)\)),
\[
H_\lambda(x)=\sum_{j\ge0}(-1)^jc_j(\lambda)x^{2j},\qquad
\partial_\lambda c_j(\lambda)=(2j+2)(2j+1)c_{j+1}(\lambda).
\tag{11}
\]
The accepted source bound \(\Phi(u)\le C e^u(\pi e^{4u})^2e^{-\pi e^{4u}}\) dominates every fixed Gaussian, exponential and polynomial insertion. It justifies all displayed integrals, sums and finite parameter derivatives on compact real lambda and complex x sets. The heat sign in (9) follows by differentiating cosine twice. No finite theta truncation is substituted.

## 5. Reuse the existing normalized Newman state; distinguish preparation from notation

Let \(Z_\lambda=H_\lambda(0)>0\), and use the genuine even source on the full line. The earlier Newman work already gives
\[
\mu_\lambda(v)=\frac{e^{\lambda v^2}\Phi(v)}{2Z_\lambda},\qquad
\psi_\lambda(v)=\sqrt{\mu_\lambda(v)}.
\tag{12}
\]
Its use of the symbol v here is an **explicit proposed encoding into the physical radial coordinate**, not a deduction that the source parameter u was always radial position. On the same cylinder Hilbert space one may take \(\Psi_\lambda(v,\omega)=\psi_\lambda(v)\chi(\omega)\), where the fixed smooth angular eigenspinor \(D\chi=\chi\) has norm one in the manuscript convention. In metric-volume convention the same unitary factor 2 applies.

This full-line state is mathematically admissible even in \(\operatorname{Dom}L_0\). To check the claim, on v>=0 use Note08's bounds \(\Phi^{(m)}=O(e^v\beta^{m+2}e^{-\beta})\) and \(\Phi\ge\kappa e^v\beta^2e^{-\beta}\). They give \(\Phi'/\Phi=O(\beta)\) and \(\Phi''/\Phi=O(\beta^2)\). Differentiating (12) twice bounds its derivatives by a fixed polynomial in v and beta times \(e^{\lambda v^2/2}\sqrt\Phi\), whose square is integrable. Evenness and positivity make it smooth through zero; reflection treats the other tail. Thus \(\psi_\lambda\in H^2(\mathbb R)\), and the fixed angular shell gives the cylinder domain. This differs from the old half-line zero-extension embedding, which by itself made no operator-domain claim. Admissibility is not a preparation protocol: no accepted Green response has been shown to output this wavefunction or its coherence.

Let X be radial position. The exact real measurement and momentum-kick amplitude are
\[
C_\lambda(x):=\frac{H_\lambda(x)}{Z_\lambda}
=\langle\Psi_\lambda,\cos(xX)\Psi_\lambda\rangle
=\langle\Psi_\lambda,e^{ixX}\Psi_\lambda\rangle.
\tag{13}
\]
The last equality uses parity; the sine expectation vanishes. The unitary is a momentum kick generated by X, not free-cylinder time evolution. An interferometric return amplitude preserves the sign; its absolute square alone does not. All polynomial position insertions below have finite moments.

Newman reweighting obeys the already established normalized equations
\[
\partial_\lambda\mu_\lambda=(v^2-\langle X^2\rangle)\mu_\lambda,
\quad
\partial_\lambda\psi_\lambda=\tfrac12(v^2-\langle X^2\rangle)\psi_\lambda,
\quad
\partial_\lambda C_\lambda=-\partial_x^2C_\lambda-\langle X^2\rangle C_\lambda.
\tag{14}
\]
The free-cylinder radial generator is \(-\partial_v^2\), whereas (14) is normalized multiplication by \(v^2\). Neither the cylinder heat semigroup nor its unitary group has been shown to implement (14). For positive lambda increments, multiplication by \(e^{\delta\lambda X^2/2}\) is unbounded, so no nonzero constant multiple is a bounded success Kraus operator on the entire radial Hilbert space. Negative increments do give a bounded conditioning filter, but normalization, success probability and physical control are additional ingredients. This scopes that filter implementation; it does not exclude a state-specific preparation or some other enlarged model.

## 6. The collision observables and what the old obstruction actually says

At a real candidate event, the two signed quantities are exactly
\[
\frac{H_\lambda(x)}{Z_\lambda}=\langle\cos(xX)\rangle,
\qquad
\frac{\partial_xH_\lambda(x)}{Z_\lambda}=-\langle X\sin(xX)\rangle.
\tag{15}
\]
A multiple real zero is their simultaneous vanishing. The next jet is \(H_{\lambda,xx}/Z_\lambda=-\langle X^2\cos(xX)\rangle\). These are expectations of commuting functions of position. Hilbert-space positivity and energy positivity do not forbid their simultaneous cancellation. Such a response zero is not a collision of cylinder energy eigenvalues.

The [earlier score-jet note](../../../../../../../papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/03_susy_dirac_hodge/notes/2_CONDITIONAL_SCORE_JETS_AND_CERTIFIED_SIGN_CHANGE_20261010.md) already identifies unpaid mixed, oscillatory score moments and a certified change of sign of the proposed Gaussian-score residual. Equations (6)-(7) now express that score through canonical angular-energy observables; they do not settle those mixed moments. The older moving-state Hamiltonian annihilates its instantaneous theta state and consequently does not generate its nonzero Newman tangent. Its spectral-gap estimate only bounds a small-frequency zero-free window.

Likewise the [radial collision analysis](../../../../../../../papers/investigations-5/04_three_regime_heat_flow_dynamics/notes/21_COLLISION_MECHANISMS_IN_THE_RADIAL_REPRESENTATION_20261027.md) distinguishes a source's spectral coefficient from an operator characteristic function, and the [conservative heat construction](../../../../../../../papers/investigations-5/05_radial_theta_collision_geometry/notes/25_TOTAL_INTEGRAL_CONSERVATION_AND_DIRECTION_FREE_HEAT_FLOW_20261027.md) gives a diagnostic, not exclusion. These are relevant precedents, not blanket obstructions to new source-sensitive physics.

## 7. Classification and control screen

This is an observable dictionary and representation comparison, not a new RH criterion or a claimed quantitative advance toward collision exclusion. Consult the [result index](../../../../../../../result-summaries/README.md), [theta cluster](../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [Newman cluster](../../../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md), [patterns index](../../../../../../../avoid/README.md), [target classification](../../../../../../../avoid/01_restating_the_target.md), [re-realizations](../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md) and [scoped exclusions](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

Apply the [registered controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md) to the actual premises:

| Control | Shared observable construction | Canonical premise absent; precise limit |
| --- | --- | --- |
| Positive weighted-square / finite-tail controls | Diagonal spectral reweighting, energy-moment identities, positive half-line source and cosine observations | Unit weights and full canonical reflection are altered; their events do not establish a finite all-real threshold. Generic measurement positivity does not exclude them. |
| Euler-factor controls | Positive even source state, Gaussian Newman weighting, signed observations (15) | Unchanged theta source/arithmetic is absent. No failure of generic state or measurement axioms occurs. |
| Reflected super-Gaussian; smooth shape / positive-primitive controls | Normalized state, Fourier/position dictionary and reweighting on their convergence domains | Complete canonical integer-square source is absent; positivity/parity/regularity alone still permit their recorded events. |
| Atomic/profile controls | Probability characteristic functions and signed expectations exist as spectral measures | Smooth wavefunction/H^2 density argument in section 5 does not apply literally; do not claim these satisfy that stronger premise. |

No new control value is computed. The generic reconstruction and response statements pass the applicable controls; the literal unit-square theta formula distinguishes the target but provides no additional signed inequality by its name alone.

## 8. What the manuscript needs and the bounded next task

The immediate improvement is to place (1)-(5), (9)-(10) and (15) together: specify energy, state, accepted detector, calibration, source scan, and signed Fourier observation. Present (12)-(14) as a connection to prior work and a proposed preparation, with its missing implementation. A physical model should separately identify its degrees of freedom, state preparation, generator, measurement and comparison law. MC11 currently specifies the operator/response exactly and reconstructs the mathematics; it does not derive a native Newman preparation or a collision-restricting law. No manuscript edit or milestone is made by this note.

**Frozen MC11-OBS-E01 r1 request (E — execution; recommended Sol).** Assess the formulas and scope in this issued note against the accepted free/source inputs and the two October Newman notes. In one analytical pass check: the effect eigenvalues and factor 4 in (3); the signs/constants in (5)-(7); the source/Newman normalization and all relevant finite-index/parameter convergence; the full-line state domain argument; the momentum-kick versus free-evolution distinction; the normalization term and bounded-filter claim in (14); and the collision/control interpretation. No new model, preparation mechanism, numerical acquisition, signed inequality or manuscript rebuild. Deliver a review in `reviews/` and a return in the sole register; retain this note as issued evidence. Ordinary local algebra/exposition corrections may be recorded; a structural preparation/generator change returns to BR02. Completion is accepted identities with exact physical qualifications or a named failed premise. E05 remains reserved. Before activation, freeze the actual input versions in the existing handoff convention.

Only after this dictionary is checked should a manuscript integration task be selected. A further conceptual continuation must specify what new physical relation the cylinder supplies for the signed observables (15), or how it actually prepares and evolves the source state. Repackaging the existing normalized state or writing another positive Hamiltonian does not meet that objective. A proposed mechanism must be screened against the controls with its true hypotheses.

## References inspected for this return

- Brad Rodgers and Terence Tao, *The De Bruijn-Newman constant is non-negative*, corrected [arXiv:1801.05914v5](https://arxiv.org/html/1801.05914v5#S1), 3 July 2021; journal DOI [10.1017/fmp.2020.6](https://doi.org/10.1017/fmp.2020.6). Selected Introduction (1)-(4) and the following heat-equation statement checked: normalization, source, Gaussian factor and heat sign. No new theorem from the proof is imported. The existing external PDF was rechecked against its prior 503405-byte record and SHA-256 `376bb2c1ab941cd5b035546835c5481f2d026767b8e830a48cd5565114a1ec91`; canonical archive provenance is linked in the local reference catalog.
- David Tong, [*Statistical Physics*, sections 1.3.1-1.3.2](https://www.damtp.cam.ac.uk/user/tong/statphys/statmechhtml/S1.html), live online lecture text consulted 5 November 2026. Canonical ensemble and energy derivatives only; the effect and source formulas above are derived here from MC11, not attributed to the lectures.
- The primary-source [Polymath abstract](https://arxiv.org/abs/1904.12438) and [Tao's 2018 exposition](https://terrytao.wordpress.com/2018/01/19/the-de-bruijn-newman-constant-is-non-negativ/) were used as orientation; the pinned Rodgers–Tao definitions above are the canonical consumed article. No contemporary bound or new literature-priority claim is made.

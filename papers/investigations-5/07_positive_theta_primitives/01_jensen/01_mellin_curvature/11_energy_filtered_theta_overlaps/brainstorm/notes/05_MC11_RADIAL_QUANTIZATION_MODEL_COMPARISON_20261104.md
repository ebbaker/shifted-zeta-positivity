# Radial quantization and the theta energy spectrum

4 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance; actual **gpt-6-astra (Codex), reasoning effort xhigh**, thread `01a1a9d4-3d44-7472-ae0f-54705423d86b`, MC11 history0002.

## Bounded discussion request

**MC11-BR01 — B, conceptual model comparison.** Recommended model Astra because the geometry, one-particle Hamiltonian and relation between spatial and spectral degrees of freedom remain to be selected. The author explicitly requested exploration of quantizing the source coordinate, a three-dimensional radial realization, coupled systems and a possible angular origin for the square energies. This is a separate brainstorm discussion; the existing E04 assessment and its frozen source are not changed, and MC11-B01/E05 are not activated by this note.

Scope: compare at most four model families on paper, using the existing radial manuscript and source-state constructions. Check the Hilbert measure, the distinction between a fixed exterior-power sector and full Fock space, energy values and multiplicities, source reconstruction, and what changes when the old inverse-temperature parameter is interpreted as a spatial coordinate. Separate exact identities from proposed dynamics. No new numerical acquisition, spectral scan, manuscript edit or claimed RH estimate. Complete this discussion with a reasoned comparison, explicit unresolved premises, and a bounded analytical follow-through only if a concrete route emerges.

The request is recorded before the substantive comparison. The return will be appended below. The existing MC11 live register retains ownership of program task status; this note is not a second register.

## Comparison return

The author additionally proposed a confining potential during this discussion. Confinement is therefore included below. This is an analytical brainstorm with proof-author checks, not specialist review or an assessment of E03. The outputs are exact representation formulas, explicit model choices and scoped spectrum-counting constraints. They are not an RH criterion, a new canonical determinant estimate or a novelty claim. The cited [result index](../../../../../../../../result-summaries/README.md), [theta cluster](../../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [patterns index](../../../../../../../../avoid/README.md) and [re-realizations caution](../../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md) delimit that interpretation.

The located source is the file [radial_deformations_and_zero_dynamics.tex](../../../../../../../../papers/investigations-5/05_radial_theta_collision_geometry/radial_deformations_and_zero_dynamics.tex), rather than a directory of that name. Its [companion, sections on the radial Laplacian and the three-dimensional cylinder](../../../../../../../../papers/investigations-5/05_radial_theta_collision_geometry/book/main.tex) supplies the coordinate and measure identities below. The prior [natural-Hamiltonian handoff](../../../../../../../../papers/investigations-5/07_positive_theta_primitives/01_jensen/01_mellin_curvature/08_open_quantum_dynamics/research-progress/handoffs/10_NATURAL_HAMILTONIAN_BRAINSTORM_CONTINUATION_20261103.md) already distinguishes spectrum-first, source-coordinate and coupled constructions. The present comparison uses those distinctions rather than treating the seeds as new discoveries.

### Fock space and the meaning of the coordinate

The fixed exterior power is one particle-number sector. Fermionic Fock space is
\[
\mathcal F_-(\mathfrak h)=\bigoplus_{q=0}^{\infty}\wedge^q\mathfrak h,
\qquad\wedge^0\mathfrak h=\mathbb C.
\]
A self-adjoint one-particle Hamiltonian h supplies free many-particle dynamics through dGamma(h); on the q sector it is the sum of h on the q slots. Interactions are additional choices. The exterior algebra fixes the antisymmetry but does not choose h, a metric, a potential or a notion of time. Choosing a fermionic field remains a model assumption.

It is consistent to promote u, or r=exp(2u), to a configuration coordinate. In that model beta=r² is an identity in the source formula and need not be a laboratory temperature. A physical inverse temperature or evolution time for the new Hamiltonian would be an additional parameter. A trace evaluated at beta=r² does not automatically become the local position density or diagonal heat kernel of the new spatial Hamiltonian.

The old primitive is a one-particle heat trace. Even after second quantization, its trace sum is not the full fermionic grand partition function, which would be a product over levels. This distinction survives every model below.

### Three-dimensional geometry and the Hilbert measure

Write
\[
A(r)=\sum_{n\ge1}e^{-\pi n^2r^2},\qquad r=e^{2u},\qquad
\Phi(u)=\frac12r^{5/2}\Delta_3A(r),\quad
\Delta_3=\partial_r^2+\frac2r\partial_r.
\tag{1}
\]
The primitive itself is p(u)=e^u A(e^{2u}). Equation (1) is inherited from the radial manuscript. Three dimensions are selected by the coefficient produced when Delta acts on the Gaussian; the sum is still indexed by a one-dimensional integer spectrum.

The companion's logarithmic cylinder has
\[
g_C=du^2+\tfrac14g_{S^2},\quad
\Delta_C=\partial_u^2+4\Delta_{S^2},\quad
d\mu=du\,\frac{d\Omega}{4\pi}=\frac{d^3x}{8\pi r^3}.
\tag{2}
\]
It retains the original du pairing for angularly constant functions. Ordinary Euclidean volume is different. An exact isometry into the radial sector of L²({r>=1},d³x) is
\[
(Uf)(r,\Omega)=\frac{r^{-3/2}}{\sqrt{8\pi}}f(\tfrac12\log r),
\qquad\|Uf\|_{L^2(d^3x)}=\|f\|_{L^2(du)}.
\tag{3}
\]
This preserves all exterior pairings. It gives a precise spatial encoding, but its Hamiltonian remains to be selected. For example, at the level of radial differential expressions,
\[
U^{-1}(-\Delta_3)U
=e^{-4u}\left(-\tfrac14\partial_u^2+\partial_u-\tfrac34\right).
\tag{4}
\]
Thus a constant-mass kinetic term in u and the Euclidean kinetic term in r are different model choices. The r^(1/2) source rescaling in the companion is also distinct from the r^(-3/2) Hilbert isometry in (3).

The original half-line corresponds to r>=1, with u=0 at a sphere. Whole-space dynamics requires an extension or a specified way of observing the exterior region. At s=1 the complete source is even in u, but the filtered single-mode interpolation does not automatically give that same full-line extension. Boundary conditions cannot be silently imposed: f_0(0)=sqrt(Phi(0)) is nonzero, so a Dirichlet wall at r=1 excludes that vector from the Hamiltonian's operator domain.

### Family 1 — a common confining potential

A source-based seed, already in the MC08 handoff, is
\[
\chi=\sqrt\Phi,\quad
h_\Phi^{\rm formal}=-\partial_u^2+\frac{\chi''}{\chi},\qquad
h_\Phi\chi=0.
\tag{5}
\]
At the complete source, chi'(0)=0 suggests a Neumann realization on the half-line; domains and action on the other source functions still need checking. Its potential grows like 4 pi² exp(8u) at infinity, so it has a confining differential expression. Equally, for the spatial seed Psi_0=Uchi, a Euclidean candidate is -kappa Delta_3+E_0+kappa Delta_3 Psi_0/Psi_0 with compatible boundary data. Its potential has leading growth kappa pi² r² at large r. These formulas produce a chosen ground profile; they do not establish that excited energies are pi n² or that the source functions are distinct eigenstates.

There is a simple obstruction to requiring a full, ordinary three-dimensional Schrödinger spectrum to consist only of the simple levels pi n². Consider a semibounded scalar h=-kappa Delta+V, kappa>0, with discrete spectrum, on a domain containing an open cube where V is bounded above. Dirichlet sine modes supported in that cube are trial vectors. For sufficiently large E, taking each of their three mode indices up to a constant times sqrt(E) gives at least C E^(3/2) linearly independent trial states below E. The min-max principle therefore yields
\[
N_h(E)\ge C E^{3/2},
\tag{6}
\]
where eigenvalues are counted with multiplicity. The desired unit-weight spectrum instead has N(E)=floor(sqrt(E/pi)). These are incompatible. This excludes the full-trace target for the stated local scalar kinetic class, not sector traces, weighted observations, different kinetic operators or coupled constructions.

Even in a fixed radial channel, a regular constant-coefficient Schrödinger operator on an infinite interval cannot have the entire simple pi n² sequence. For any finite length L, Dirichlet trial states inside an interval of that length give liminf N(E)/sqrt(E)>=L/(pi sqrt(kappa)). Letting L grow gives N(E)/sqrt(E) tending to infinity, assuming V is bounded above on each compact interval. A hard wall at finite radius avoids this argument.

Indeed, for a unit three-dimensional ball with a Dirichlet wall and h=-Delta/pi, the angularly constant sector reduces under R(r)->rR(r) to -d²/dr²/pi on (0,1), with energies pi n². The complete ball contains additional angular sectors. Moreover, its particle radius lies in a bounded interval; identifying that radius with the existing unbounded r in A(r) requires a new map and corresponding metric or observation. This is a useful confinement benchmark, not a completed realization of the source functions.

### Family 2 — angular energies on a sphere

For a unit two-sphere, -Delta_S² has eigenvalues ell(ell+1), multiplicity 2ell+1. The companion's angular operator has the exact identity
\[
(1-4\Delta_{S^2})Y_{\ell m}=(2\ell+1)^2Y_{\ell m}.
\tag{7}
\]
Thus the existing geometry already produces odd squares. Its ordinary trace carries multiplicity 2ell+1. With B=1-4 Delta_S²,
\[
\operatorname{Tr}(B^{-1/2}e^{-\pi r^2B})
=\sum_{n\ge1,\ n\ {\rm odd}}e^{-\pi n^2r^2}
=A(r)-A(2r).
\tag{8}
\]
The full sum can be recovered by summing the odd part at 2^k r, k>=0. This introduces a scale sum or an extra degree of freedom. The earlier [three-dimensional lattice note](../../../../../../../../papers/investigations-5/05_radial_theta_collision_geometry/notes/08_GENUINE_THREE_DIMENSIONAL_LATTICE_SUMS_AND_THETA_RECOVERY_20261027.md) already treats odd-sector recovery and its costs in a different lattice realization.

A spinor angular model matches every square directly. Let D be the self-adjoint Dirac operator on the unit S². It has eigenvalues ±n, n>=1, each with multiplicity 2n. Therefore pi D² has the desired energy values but multiplicity 4n on the complete spinor space. A rotationally invariant weighted trace gives
\[
\boxed{A(r)=\operatorname{Tr}_{\mathrm{spin}(S^2)}
\left[(4|D|)^{-1}e^{-\pi r^2D^2}\right].}
\tag{9}
\]
The positive operator (4|D|)^(-1) is bounded by 1/4 and can serve as a measurement effect. Its energy-dependent weighting is essential; it cannot be omitted from the observation. The spectrum and degeneracy are checked in [Camporesi and Higuchi, section 3.1 and equation (3.54)](https://arxiv.org/html/gr-qc/9505009). Their slash operator is anti-Hermitian; D=-i slash-nabla is the convention used here.

This gives a real connection between angular spinor modes and theta energies. It does not yet specify the radial Hamiltonian or show that the full three-dimensional thermal state has density A(r). In Euclidean space angular kinetic terms ordinarily scale as 1/r². A proposed r²-dependent angular coupling has to be explicitly chosen. Once radial kinetic energy is included, it does not commute with the r-dependent angular potential; a frozen-r trace is not generally the exact marginal of the full Gibbs operator.

### Family 3 — a coupled confining oscillator

There is a direct model in which r is an actual Euclidean position radius and the Gaussian theta terms are spatial densities. Let an internal energy operator K on ell²(N) have K|n>=E_n|n>, E_n=pi n². On L²(R³,d³x) tensor ell²(N), take
\[
\boxed{h_{\rm osc}=\frac13\left(-\Delta_x\otimes I+r^2\otimes K^2\right).}
\tag{10}
\]
This is a direct sum of ordinary confining oscillators and has a standard nonnegative self-adjoint direct-sum realization. Channel n has normalized ground function
\[
\psi_n(x)=\left(\frac{E_n}{\pi}\right)^{3/4}e^{-E_nr^2/2}.
\]
Differentiating gives -Delta psi_n=(3E_n-E_n²r²)psi_n, so
\[
h_{\rm osc}(\psi_n\otimes|n>)=E_n(\psi_n\otimes|n>).
\tag{11}
\]
The factor 1/3 fixes the energy unit so the three-dimensional oscillator ground energy is E_n. Its other energies in channel n are E_n(2N+3)/3, N=0,1,... . These are additional states, not removed by the theta matching. The usual oscillator formulas are checked against [MIT Physics 8.05, section 6, equations (54)–(60)](https://web.mit.edu/8.05/handouts/SusyHydrogen2007.pdf); equations (10)–(13) here are our explicit proposed construction, not a claim from that source.

Define the positive stationary trace-class operator supported on the channel ground states,
\[
\Gamma=\sum_{n\ge1}n^{-3}
|\psi_n,n\rangle\langle\psi_n,n|.
\]
Its unnormalized position density, after tracing out the internal label, is exactly
\[
\boxed{\sum_{n\ge1}n^{-3}|\psi_n(x)|^2
=\sum_{n\ge1}e^{-\pi n^2r^2}=A(r),\quad r>0.}
\tag{12}
\]
The factor n^(-3) cancels the normalized three-dimensional Gaussian factor n³. Its trace is zeta(3); dividing by that trace produces a normalized density matrix. Applying the original internal filter weights w_1=1, w_(n>=2)=s replaces Gamma by Gamma_s and recovers A_s(r) exactly, with trace 1+s(zeta(3)-1). Retaining this trace weight matches the unnormalized convention of MC11. Equation (1) then recovers Phi_s on r>=1 by differentiation of the spatial density.

The cost is substantial and explicit:

- K retains the arithmetic spectrum as an internal input. Equation (10) does not derive pi n² from the three spatial directions.
- Gamma is a specially selected ensemble, not a Gibbs state of the complete oscillator Hamiltonian. The full spectrum contains the oscillator excitations described above.
- Although Gamma has finite trace, its mean energy diverges:
\[
\operatorname{Tr}(\Gamma h_{\rm osc})=\pi\sum_{n\ge1}\frac1n=\infty.
\tag{13}
\]
  This is already a property of the simplest full-space ensemble, not a numerical uncertainty. The density has the known A(r)~1/(2r) singularity near r=0. A finite-energy realization restricted to the original exterior region requires additional boundary/preparation work; a cutoff cannot silently change the source.
- The equality is a position-density identity for A, not yet a preparation and measurement scheme for all the derivative and moment vectors whose determinant is D_q. Differentiating a density and producing a state amplitude are different operations.
- The internal label in (10) is distinct from the angular coordinates of x. Replacing it by those same angular degrees of freedom changes the Hamiltonian and its radial centrifugal terms; the simple channel calculation cannot be reused unchanged.

This makes confinement and the theta Gaussian profiles compatible in a concrete mathematical model. It also makes clear what remains to be explained physically. It supports an assessment contract rather than an immediate claim of a completed field theory.

### Family 4 — a compact curved-space benchmark

On the unit round S³, scalar eigenvalues of -Delta are k(k+2), with total multiplicity (k+1)². Hence h_3=pi(-Delta_S³+1) has energies pi n², n=k+1, but multiplicity n². [Lindblom, Taylor and Zhang, section 2, equations (1)–(4) and (10)](https://arxiv.org/html/1709.08020v1) supplies the spectrum, metric and angular labels.

In the rotationally invariant sector about a chosen pole, let chi be geodesic radius and set v(chi)=sin(chi)R(chi). On 0<chi<pi,
\[
(-\partial_\chi^2-2\cot\chi\,\partial_\chi+1)R
=\frac{-v''}{\sin\chi}.
\tag{14}
\]
Regular radial eigenfunctions give v(0)=v(pi)=0. This sector therefore has one mode sin(n chi)/sin(chi) for each energy pi n², and its heat trace is the exact unit-weight primitive trace. The full scalar trace is instead sum n² exp(-beta pi n²). This clean geometric benchmark is compact and curved; it does not identify chi with the existing unbounded Euclidean r or log-radius u without a further metric/state map. It is analogous to the hard-wall radial-sector benchmark and does not solve the source-state comparison by itself.

### Controls and what the comparison does not imply

The [collision-control register](../../../../../../../../result-summaries/12_collision_controls_and_screening.md) screens any inference from these constructions to determinant positivity. No new collision calculation was run, and no failure of a control at the acquired MC11 cofactor inequalities is asserted.

| Control class | What this comparison preserves or fails |
| --- | --- |
| Reweighted square spectra | The same K and coupled oscillator work with weights a_n n^(-3); angular weighted traces can insert a_n(pi D²). Thus the construction itself also represents positive weighted-square controls. They fail the complete unit-weight source premise; that does not make generic quantization a separating estimate. |
| Euler-factor modifications | A generic auxiliary Hilbert/Fock construction remains available, but equations (9) and (12) with the fixed canonical weights do not reproduce the modified source. The failed premise is the literal unchanged theta trace/source, not positivity of a Hamiltonian. |
| Reflected or positive-primitive smooth controls | Source-based factorization and radial encoding can apply when their regularity/domain conditions hold. These controls do not supply the literal canonical integer-square expansion. No general sign is inferred from their positive source or auxiliary norm. |
| Smooth-density, counter-kernel or two-channel controls | Generic exterior algebra and positive Hilbert norms are not discriminators; an atomic source may require a different measure/domain and is not asserted to satisfy the smooth differential setup. The exact canonical source or the required smooth-domain premises are absent, as appropriate. |

These are structural premise comparisons, not new universal exclusion theorems. The scoped spectral-counting result (6) concerns ordinary local scalar Schrödinger operators and the full unweighted spectrum only.

### Decision and bounded follow-through

The Fock-space interpretation can be made precise, and u need not remain a thermodynamic parameter in a new spatial model. The choices of metric and Hamiltonian must then be explicit. Confinement is a useful modeling ingredient, but energy values, degeneracies and the source observation must be matched separately.

The coupled oscillator is the most concrete candidate here for making the existing r into actual Euclidean radius while recovering A(r) as a spatial density. The angular Dirac construction is the strongest candidate for relating spherical modes to every square energy; its weighted trace remains part of the observable. These two candidates answer different parts of the request and are not yet one unified model. The compact-sector examples establish useful benchmarks, while the source-based potential prioritizes the actual source functions over the prescribed energy sequence.

| Next task | Type | Recommended model | Dependency | Expected output |
| --- | --- | --- | --- | --- |
| **MC11-BR01-E01 — proposed default** | E — analytical assessment | Sol; formulas and checks are fixed | Author selects continuation; no new E04 premise is required | Claim-by-claim check of (3), (6), (9) and (10)–(13), including the full spectrum, density, energy divergence and exterior boundary limitations |
| Subsequent model selection | B — conceptual | Astra; decide what physical requirements to retain | Assessed return and author's preferred interpretation | Select an angular-source model or a finite-energy coupled spatial model before deriving dynamics |

Proposed E01 limits: one analytical pass, at most one local correction, no quadrature, spectral scan, new potential or replacement source. Use the sources and versions in the [reference catalog](../../references/README.md). Check all Gaussian and multiplicity constants, define the oscillator direct-sum domain, distinguish the band and full spectrum, verify the trace and divergent energy, and list exactly what the isometry (3) does and does not imply for source-state domains and readout. A substantive failure or a repair requiring a changed geometry, ensemble or observation returns to conceptual model selection. The assessment may accept exact identities and still find the physical bridge incomplete; it must not promote that to a completed finite-energy theory.

This proposed assessment is not activated here and is separate from MC11's reserved program E05. The original E04 frozen inputs and live task register remain unchanged. No manuscript or snapshot is created. External articles, inspected passages and archived PDF provenance are recorded in the affiliated references folder; all analytical work from this conversation remains in the brainstorm notes.

# Critical review and global research decision for YM-to-Weil realization

Date: 24 September 2026, America/New_York.  
Prepared for Edward Baker with substantial LLM assistance.  
Model exposed to this session: GPT-6 (Codex); exact variant and configured reasoning-effort label not exposed, not inferred.  
Repository baseline: b60a2e27b9a39be33b1b43bb7b99172cdc5e7573.  
Status: critical model-assisted assessment, not independent human validation. New deductions are proved in the companion notes and remain provisional. No YM realization or RH proof has been obtained.

## 1. Assessment and recommendation

The recent elementary calculations largely survive review. The main correction is to the research requirements: **an independently identified native arithmetic generator is not essential to the original reflected-pairing existence problem.** Exact pairing already induces translations on the source image. Requiring those translations to coincide with a specified physical or insertion operator is a stronger ansatz.

The strongest next direction is source occurrence in a fixed YM representation plus an independently derived identity determining its pairing. The best arithmetic template found is a Poisson/dilation character calculation, because it accounts for gamma and prime contributions together. No checked theorem transports that arithmetic structure into pure four-dimensional YM with the required positive metric.

The main concrete result of this session is a global determination theorem: the exact pairing on separated supports, translation/reflection symmetry, and logarithmic high-frequency growth leave only **three local constants after pole removal**. Three dilated calibration tests fix them. The theorem does not assume positivity or a native generator. A second theorem extends arbitrary finite compatible source assignments under compact control in the specified YM representation.

I recommend a bounded further investment in finding the mixed identity, supported by the existing finite-slab source core. I do not recommend more support-window certificates or larger Monte Carlo loop families as the main arithmetic program. If no independent arithmetic source relation emerges, the present pure-YM framework lacks a bridge, even though it supplies a sound positive norm. Moving to an adelic/Hecke defect or a different arithmetic theory would be an explicit model change, not a consequence of OS positivity.

Companions:

- [Global determination, compact existence, and the next theorem](../notes/OFF_DIAGONAL_RIGIDITY_AND_COMPACT_SOURCE_EXISTENCE_20260924.md).
- [Spectral, modular, and Liouville controls](../notes/SOURCE_SPECTRA_MODULAR_AND_LIOUVILLE_CONTROLS_20260924.md).
- [Primary-source verification ledger](../notes/GLOBAL_MECHANISMS_PRIMARY_SOURCE_LEDGER_20260924.md).

## 2. Critical audit of the requested notes

### 2.1 Arithmetic normalization and high frequency

The pole-neutral parametrization is correct:
\[
T=-\partial_x^2+\tfrac14,\qquad T^{-1}f=e^{-|\cdot|/2}*f.
\]
The derivative jump of \(e^{-|x|/2}\) is \(-1\), so there is no missing Green-function factor. The two exterior tails are precisely the two exponential moments. The inverse preserves an enclosing interval, not necessarily the exact disconnected support.

For
\[
f_\lambda=\lambda^{-2}T(e^{i\lambda x}h)
=e^{i\lambda x}\left(h-\frac{2i}{\lambda}h'
+\frac{h/4-h''}{\lambda^2}\right),
\]
the sign and coefficients are correct. These tests are exactly pole neutral and uniformly bounded in \(L^1,L^2,L^\infty\) at fixed support. The gamma multiplier is asymptotic to \(\log(|\tau|/2\pi)\). Uniform Schwartz bounds on the demodulated profiles control the Fourier tails, including the region near \(\tau=0\). The prime terms are bounded by a finite support-dependent sum. Therefore
\[
Q[f_\lambda]=\|h\|_2^2\log\lambda+O_{h,I}(1)
\]
is justified. The same argument for \((i\lambda)^{-1}f_\lambda'\) justifies the derivative-to-source ratio.

This is neither positivity on arbitrary tests nor an estimate uniform in growing support. The constants may grow with the support interval. The original notes state that limitation correctly.

The kernel normalization also checks: twice the integral of
\((1-\cos(\tau r))e^{-r/2}/(1-e^{-2r})\) over \(r>0\) is the stated digamma difference. The gamma/contact and prime terms have the stated relative factors. The restricted RH criterion was checked in the actual [Connes–Consani Appendix C, Proposition C.1](https://arxiv.org/pdf/2006.13771), including the exclusion of prescribed Mellin zeros at zeta zeros. The allowed points 0 and 1 satisfy that exclusion.

**Verdict:** retain the high-frequency calculation. Retain the exclusion of ordinary smearing of locally norm-integrable bounded loop vectors. Do not extend it to distribution-valued sources, derivative sources, or all sources in the OS completion.

### 2.2 Generator exclusions and the unnecessary extra requirement

For a continuous exact source map, common translations induce
\(V(a)Jf=J(U_af)\) on its closed image. Null vectors are preserved, continuity is inherited from the test topology, and
\[
V(a)=e^{-iaG},\qquad GJf=-iJf'.
\]
The linear arithmetic reflection induces a unitary involution sending \(G\) to \(-G\). It is not the physical antiunitary OS reflection.

The three old exclusions are valid:

- Equating arithmetic translations with \(e^{-aH}\), \(H\ge0\), forces every source into \(\ker H\), then kills \(Jf'\), contradicting high frequency.
- A bounded \(G\) contradicts \(Q[f']/Q[f]\sim\lambda^2\). Spectral symmetry then excludes semibounded \(G\).
- Periodicity kills \(f_\lambda-U_Pf_\lambda\), while disjoint translated profiles give leading norm \(2\|h\|^2\log\lambda\). Possible prime terms at the same separation remain \(O(1)\) and cannot cancel it.

**Necessary correction:** the outline's “fix an independently specified arithmetic action” and its next-step instruction to find a native generator are too restrictive as universal prerequisites. An exact map needs genuine observable content, but that content can be specified by a source preparation law, mixed matrix elements, or relations with the boundary algebra. It need not identify logarithmic translation with a pre-existing physical symmetry.

If such an identification is part of a particular ansatz, the exclusions apply. They do not rule out a different source prescription in the same YM theory. The separate causal objective still requires physical evolution and readout, but even there physical time need not equal arithmetic translation.

### 2.3 Weighted flows

For a complete smooth gauge-equivariant flow \(\Phi_t\), the note uses the **pullback** Jacobian
\(\Phi_t^*\nu=j_t\nu\). With that convention,
\[
\mathcal U_tB=j_t^{1/2}B\circ\Phi_t,\quad
A_D=D+\tfrac12\operatorname{div}_mD+D\log\Omega
\]
is correct. The group law and unitarity follow from the Jacobian chain rule and change of variables. Since the group used for arithmetic convention is \(\mathcal U_{-a}\), its selfadjoint generator is \(-iA_D\), with the sign printed in the note.

Conjugating by \(W B=w^{1/2}B\) cancels \(\tfrac12D\log w\), giving
\[
WG_DW^{-1}=-i(D+\tfrac12\operatorname{div}_mD).
\]
Thus changing a strictly positive smooth weight alone does not change the spectrum of a **fixed** geometric flow. The state can still change a seed's spectral measure; the vector field itself could depend on dynamics. Neither possibility is excluded by this cancellation.

Selfadjointness here comes from the unitary group and its generator, not from merely declaring a formal differential operator symmetric. Gauge-equivariance is material: individual left-link derivatives generally leave the selected covariant sector.

**Verdict:** no sign correction needed; preserve the fixed-flow qualification. This is a kinematic construction, not an arithmetic spectral mechanism.

### 2.4 Generalized-source domains

The combined-multiplier definition
\[
Jf=[\,\widehat f(\lambda)(1+\lambda^2)^{s/2}\,](G)\eta
\]
is valid for selfadjoint \(G\), finite \(s\ge0\), and \(\eta\in\mathcal H\). It must not be read as first applying an unbounded power to \(\eta\). Smooth compact tests make the combined multiplier bounded; the resulting spectral measure is positive and polynomially controlled.

This gives a useful globally defined class. It does not prove:

- that an arbitrary functional calculus belongs to the stated observable completion;
- that a chosen generalized vector is an allowed OS source;
- the Weil spectral measure;
- compact embedding of the scale generated by \(G\).

The last caution in the note is correct: a one-dimensional flow may leave all transverse directions uncontrolled. A separate elliptic source norm is useful.

**Qualification:** finite order and a preselected native \(G\) define an ansatz, not a universal admissibility axiom. It is unnecessary to show every prospective realization has this form before pursuing direct source existence.

### 2.5 Full Ward uniqueness and compactness

The finite-lattice integration-by-parts uniqueness proof is correct. Applying the equations to \(F=e^Sh\) shows \(e^S\mu\) is invariant under every left-link flow; connectedness and Haar uniqueness determine the measure. Positivity plus normalization are explicit hypotheses. The equations must hold for all smooth configuration tests. A truncated loop system is not that hypothesis.

Even full state uniqueness does not determine a source map. In particular, the fixed source family is extra data beyond the Wilson measure.

The strong-limit compactness proposition is also correct with its stated uniform local seminorm bounds, compact injection, and compatible dense test family. Weak \(\mathcal K\) sublimits show that the strong \(\mathcal H\) limit lies in \(\mathcal K\). The local extensions agree and are continuous in the test-space inductive limit. No uniform-in-\(L\) coercivity is required.

The gaps are in its hypotheses, not its proof: it starts with globally defined approximating maps and supplies no arbitrary finite-feasibility theorem. The new compact finite-compatibility theorem removes the former requirement but cannot supply the latter. Unbounded source relations still need closed graph control.

### 2.6 Finite-slab reflection and hierarchy

The central-slice factorization is sound for the stated open-time nearest-neighbor Wilson slab. No plaquette couples both strict half-interiors. Integrating the two halves gives \(\nu\propto\Omega^2dm\), with smooth strictly positive \(\Omega\). Boundary matrix multiplication passes through the half integral and hence preserves its null kernel.

The reference endomorphism fiber, finite-slab state, and physical reflection are explicit. This is not a derivation for arbitrary interior insertions, the infinite-time vacuum, or continuum YM. The distinction from the earlier interior-multiplier counterexample is valid.

The discrete compression residual is orthogonal to the destination space; the Schur complement and norm-loss identity follow. Propagating the residual gives the forward bound. Pairing with an approximate backward state and using orthogonality gives the displayed forward/backward bound. These are algebraically valid for exact Gram data. The old Monte Carlo uncertainties and all numerical records were not independently rerun in this session.

**Verdict:** retain this finite-regulator foundation. It establishes a useful source space and controlled approximation language, not prime/gamma matching.

## 3. Ranked comparison of global mechanisms

This ranks research priorities under the user's genuine-YM constraint, not estimated probabilities of proving RH. None is currently a verified arithmetic YM mechanism.

| Rank | Mechanism | What is actually available | Exact bottleneck |
|---|---|---|---|
| 1 | Source occurrence plus a mixed Poisson/trace identity and pairing determination | Global arithmetic character formulas; new three-constant determination theorem | Derive the separated-support identity from actual YM observables |
| 2 | Compact finite source extension in the fixed boundary representation | Compact elliptic source balls and a finite-compatibility theorem | Arbitrary finite feasibility with one fixed source law and bounds |
| 3 | Thermal Liouville/generalized insertion sources | Two-sided energy differences; centered seeds with even measures | Singular admissible seed and arithmetic identity at actual YM energy differences |
| 4 | Full YM Ward/loop equations and recursive determination | State uniqueness; rigorous all-loop results in specific strong-coupling/large-N models | Arithmetic indexing and a mixed source identity not contained in state equations |
| 5 | Native modular actions | General modular theory; geometric wedge identification under extra hypotheses | Current boundary flow is trivial; vacuum wedge boosts fail the point-spectrum test |
| 6 | Arithmetic Hecke/adelic or cohomological structure added to the model | Genuine arithmetic operations, global trace/closure templates | Positive metric and genuine occurrence/coupling in YM; explicit model change |

### 3.1 Rank 1: occurrence and an identity that determines the pairing

**Mechanism.** Specify a global arithmetic source module and realize its relevant operations and sources inside the YM boundary core/completion. Derive an identity combining Fourier/Poisson duality with integer dilations. Use the actual OS pairing and sign-free uniqueness to identify \(Q\).

**Established input.** Meyer's Theorem 5.8 supplies an unconditional arithmetic character formula on a carefully chosen nuclear Fréchet quotient. Its zeta operator is a sum over integer dilations, with Euler factorization and Poisson relations. This is the most informative checked template for generating both sides of the arithmetic pairing. [Primary paper](https://arxiv.org/pdf/math/0412277).

**Missing lemma.** An actual YM source law must produce equation (9) of the new determination note, not merely an isomorphic abstract vector space or an imposed spectral list. Occurrence and metric identification are both open. A trace formula alone is not an OS inner product.

**Domains/globality.** One LF test space covers all compact supports; source continuity is local in support. Nuclear traces require their specific domains; infinite dilation sums cannot be transferred formally. At each compact separation only finitely many prime terms contribute. No new YM parameters are chosen when support grows.

**Arithmetic entry and obstruction.** Arithmetic enters through a derived integer-dilation/Poisson relation, which pure YM has not supplied. The new theorem solves the old pairing-underdetermination problem *conditional on that relation*: only three constants remain. It relocates, rather than resolves, the hard arithmetic occurrence problem.

**Additional control.** Translation-invariant pairings on a reducible arithmetic module generally have many independent weights. Schur's lemma is not a uniqueness theorem for this reducible module. Faithfully placing all zero-multiplicity jets into Hilbert vectors can impose simplicity of zeros, an unnecessary strengthening; the companion note states the precise scope of this warning.

### 3.2 Rank 2: compatible source extension with compactness

**Mechanism.** Use actual source vectors in one fixed Wilson boundary representation. Place them in uniformly bounded local balls of an elliptic Sobolev space, enforce finite sets of source relations, and use compactness to pass to a global family.

**Established inputs.** The previous compactness argument and the new finite-intersection theorem are sufficient extension results. Lasserre's Theorem 4.2 supplies a separate example of a genuinely convergent moment hierarchy under an Archimedean compactness hypothesis; it does not establish YM/arithmetic feasibility. Holonomy-algebra reconstruction provides measures/representations, not automatic equality with the intended YM state. [Lasserre](https://web.mit.edu/~a_a_a/Public/Publications/refs_for_seb_blog/Lasserre.pdf), [Ashtekar–Lewandowski](https://arxiv.org/pdf/gr-qc/9311010).

**Missing lemma.** Every finite set of independently derived source constraints must be feasible with common local regularity bounds and physical source membership. Testing a few finite Gram matrices is insufficient. The positive OS pairing must emerge from those actual vectors.

**Domains/globality.** Compactness is in the fixed finite-lattice \(H^r_{\rm cov}\to L^2_{\rm cov}(\nu)\) inclusion. It covers a countable dense family across all support intervals. Constants may depend on the interval. Continuum refinement would require additional uniform estimates and state identification, and is not part of this finite-regulator theorem.

**Arithmetic entry and obstruction.** It enters in source relations yielding the mixed identity. Compactness prevents norm loss and representation drift; it cannot manufacture that identity. Free positive arithmetic moments would return to the circular formulation excluded by the user.

### 3.3 Rank 3: Liouville or native insertion actions

**Mechanism.** A faithful thermal YM state, when available, has a standard operator representation with \(L=H_{\rm left}-H_{\rm right}\). This permits both signs of energy differences. Covariant insertion operators in the existing boundary model are another possible source of nonperiodic two-sided actions.

**Established calculation.** The companion note proves the spectral detailed-balance relation for \(A\rho^{1/2}\) and the even measure of \(\rho^{1/4}A\rho^{1/4}\) for selfadjoint \(A\). Centering fixes a real asymmetry, but bounded observables still give finite-norm seeds and fail high frequency.

**Missing lemma.** Find an admissible singular/generalized source with the exact mixed arithmetic pairing. An exact source image has discrete zero-ordinate spectrum as a conditional consequence of its pairing; the actual Liouville operator must have the needed point spectrum if identified with that action.

**Domains/globality.** State \(Z_\beta<\infty\), the gauge sector, common insertion domains, and the relevant Schatten/Hilbert scales. A single strongly continuous group and finite-order generalized seed act on all compact tests.

**Arithmetic entry and model change.** No arithmetic information is supplied by energy differences or KMS alone. Thermal state and Hilbert–Schmidt source sector are changes from the finite-slab boundary state, even with unchanged bulk gauge dynamics. In a vacuum source sector, a commutator acting on \(A\Omega\) simply reduces to the semibounded physical Hamiltonian.

### 3.4 Rank 4: loop/Ward recursion or a native trace identity

**Mechanism.** Derive enough loop or insertion equations to fix all mixed source correlators and compare their resulting functional with the explicit formula.

**Established input.** Kazakov–Zheng derive special finite-N trace reductions, including a linear SU(2) single-loop system. Chatterjee proves uniqueness of an all-loop limiting solution with growth bounds at sufficiently small coupling for SO(N) in the large-N limit. These demonstrate real global extension mechanisms in their stated models. [Kazakov–Zheng](https://arxiv.org/pdf/2404.16925), [Chatterjee, Theorem 9.2](https://arxiv.org/pdf/1502.07719).

**Missing lemma.** Identify a source-indexing law and mixed relation whose solution has the archimedean term and every prime-power coefficient. Neither paper claims this. SU(2) single-trace closure is still infinite in loop length; it is not a finite source hierarchy.

**Domains/globality.** A full loop set with proved growth control can cover arbitrary contours. Turning contour complexity into arbitrary arithmetic support needs its own law. Chatterjee's gauge group, coupling regime, and large-N limit differ from a fixed finite-N slab and must not be silently imported.

**Arithmetic entry and obstruction.** It would enter through the indexing/mixed identity, not ordinary state Ward identities. The known recursion addresses YM determination, while the arithmetic gap remains untouched.

### 3.5 Rank 5: modular actions

**Mechanism.** A standard pair of a von Neumann algebra and a faithful state supplies a two-sided modular generator without choosing an artificial spectrum.

**Established input and new tests.** Bisognano–Wichmann identifies a geometric case under relativistic field hypotheses. The companion note proves that the current finite-slab multiplication algebra has \(\Delta=I\), and that geometric vacuum boosts under a forward-cone spectrum and unique vacuum cannot contain the nonzero point spectrum forced by exact Weil sources. [Original theorem](https://doi.org/10.1063/1.522605).

**Missing lemma/domain.** A different nontracial algebra/state would have to be specified, with standardness, source graph domains, and the complete arithmetic identity. Pure OS positivity is insufficient.

**Globality/arithmetic/limits.** Modular time itself is global, but it supplies no prime indexing. The common boundary and vacuum-wedge candidates fail their proposed operator role. This does not exclude nongeometric modular actions, other states, or a source realization with no modular identification.

### 3.6 Rank 6: arithmetic additions and alternate global formulations

Bost–Connes gives a real arithmetic quantum statistical system with logarithmic integer energies and zeta partition function. Its arithmetic is structural, but its positive Gibbs states do not establish the completed critical-line Weil pairing. Tensoring it with YM simply attaches an arithmetic system unless an independent interaction/occurrence theorem produces the required pairing. The gamma term and the signed combination remain to be derived. [Bost–Connes, §6](https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/CONNES/1994-1998/M_95_38/M_95_38_web.pdf).

Semilocal Sonin spaces have compatible arithmetic maps, but metric transport is essential. Their Hilbertian isomorphism does not identify a YM sector, nor does the proved archimedean short-support comparison settle every support. These are useful templates if an explicit adelic source sector is permitted. [Connes–Consani–Moscovici, v2, Theorem 4.6 and §4.8](https://arxiv.org/pdf/2310.18423).

Deninger's cohomology/trace framework supplies a conceptual model for global arithmetic plus positive duality, but its needed arithmetic cohomology and positive structure are conjectural. A recent Hedenmalm operator-pair formulation likewise leaves the appropriate positive sesquilinear structure as a hypothesis. Neither is an established YM bridge. [Deninger](https://arxiv.org/pdf/1001.1621), [Hedenmalm, §4](https://arxiv.org/pdf/2606.17494).

These changes may be better motivated than inventing a vector field on a compact link manifold. They must be declared as new arithmetic geometry, a defect/auxiliary theory, or a changed physical model; ordinary four-dimensional pure YM does not currently derive them.

## 4. The separate native causal problem

Burnol's adelic Lax–Phillips construction is a serious global causal template: its missing incoming/outgoing orthogonality is itself RH-equivalent. It therefore identifies an exact missing condition rather than deriving causality from a positive ambient space. [Burnol, Theorems 1.7 and 1.11](https://arxiv.org/pdf/math/0001013).

This preserves the user's causal objective but does not solve it in YM. In particular, that scattering operator has not been identified with the project's
\[
K_\omega(z)=\frac{\xi(1/2+z-\omega)}{\xi(1/2+z+\omega)}.
\]
A native YM result still needs a preparation map, a physical time evolution, a readout, the correct ordinary source/output norm, and an identity for this particular ratio. OS positivity, two-sided Liouville dynamics, or a pre-existing arithmetic scattering model cannot substitute for those requirements.

## 5. The result to build on and the next decision

Theorem 1 in the determination note proves:
\[
\text{separated-source identity + symmetries + logarithmic growth}
\ \Longrightarrow\
B(Th,Tk)-Q(Th,Tk)=\sum_{j=0}^2a_j\langle h^{(j)},k^{(j)}\rangle.
\]
Three dilated anchor values then give \(B=Q\). The theorem works among forms of unknown sign and for all compact supports. It neither requires a uniform gap nor assumes positivity of the arithmetic form.

Theorem 2 and Lemma 3 supply the fixed-representation extension mechanism and a concrete weighted elliptic tail estimate. This is more specific than merely asking for compactness, but arbitrary finite feasibility remains unproved.

**Recommended next existence problem:** in one fixed pure-YM slab, produce a source law in the covariant boundary/insertion completion whose independently derived mixed Poisson or Ward relation gives the separated-support kernel in equation (9), with the three anchor normalizations and local compact source bounds. The first tractable control lemma, the gauge-compatible elliptic spectral cutoff estimate, is already proved. The first unresolved lemma must identify arithmetic information in the YM relation itself.

Continue if that lemma can be specified without inserting the target coefficients as moments or selecting a spectrum from RH. If the only available construction is an arbitrary Hilbert embedding, an imposed arithmetic auxiliary system, or a refit at each support length, stop presenting it as progress toward the stipulated pure-YM realization. A clearly identified arithmetic extension of the model would then be the more honest research direction.

## 6. Verification limits

The five requested notes were read and their displayed arguments rederived at the level reported above. Relevant earlier scope/bridge notes were consulted. Primary sources were inspected at theorem and formula level, with decisive PDF pages rendered; the source ledger specifies locations and limitations. Full independent reproofs of all cited papers, numerical reruns, continuum existence, and a search-completeness claim are not part of this assessment.

Earlier notes are preserved. The outline is corrected to distinguish induced source translations from optional native intertwinings. New results are session deductions awaiting external mathematical review, not independently validated breakthroughs.

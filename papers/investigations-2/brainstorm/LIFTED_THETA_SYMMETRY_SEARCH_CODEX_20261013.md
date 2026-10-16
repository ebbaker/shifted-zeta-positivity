# Broad search for symmetries in lifted theta systems

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6.1-sol (`gpt-6.1-sol`), Codex; reasoning effort **ultra**, verified from the recorded session configuration. Parallel internal searches used the same configuration. This is a research map and an initial mathematical scout, not independent specialist validation, a new formal theorem, or a proof of RH.

Folder layout clarification, 13 October 2026: this brainstorm remains in
`investigations-2/brainstorm` as shared planning. Its 16 programs are
initialized in [active](../active/README.md) for Claude review. The original
source record retains its captured paths and hashes; the
[layout update](../PORTFOLIO_LAYOUT_UPDATE_20261013.json) records link
maintenance and restoration. Mathematical statements are unchanged.

## Findings and recommended starting points

The lifted system is a useful place to search for theta reflection identities. Existing calculations already turn inversion into ordinary parity, expose arithmetic transport and transverse correlations, and permit regular elimination of hidden coordinates. The most promising first investigations are **complete reflection across the cutoff boundary, angular Jacobi gluing, and source-to-observation identities in the anchored arithmetic lift**. These have explicit states and reduction maps, so a candidate identity can be tested without first constructing a new model.

The broader search also identifies coherent-state and metaplectic methods, paired-kernel positivity, divisor and cusp intertwiners, Gaussian-Hermite coefficient constraints, supersymmetric identities, canonical systems, stable-polynomial limits, integrable transformations, adelic compatibility, and radial geometry. Their readiness differs substantially. The ranking below concerns how directly a bounded calculation can produce useful information; it is not an estimate of the probability of proving RH.

No new global theta reflection identity or excluding inequality has been obtained in this first pass. The concrete additions are a unified symmetry-defect test, explicit accounting for moving reflection centers and finite cutoffs, a source-specific candidate map, and exact finite controls. The [source and scope record](numerics/LIFTED_THETA_SYMMETRY_SEARCH_RECORD_CODEX_20261013.json) distinguishes checked local seeds, primary-source precedents, and proposed applications. The [seed checker](numerics/check_lifted_symmetry_seeds_20261013.py) supplies **192 passing exact rational assertions**, with its [retained record](numerics/LIFTED_SYMMETRY_SEED_CHECK_RECORD_20261013.json).

This extends the [12 October strategy](NEW_PATHS_FORWARD_AFTER_AUDITS_CODEX_20261012.md) and its [agreed parallel layout](reviews/STRATEGY_AND_PARALLEL_LAYOUT_REVIEW_CODEX_20261012.md). It makes the lifted symmetry search explicit without changing the completed formal-replay milestones or treating the still-open source estimates as consequences of those milestones.

## What an identity must constrain

The object to preserve is the prepared state, its domain and evolution, and the physical observation:

\[
\partial_t\Psi_t=\mathscr G_t\Psi_t,
\qquad \mathcal P_{t,x}\Psi_t=H_t(x),
\qquad \mathcal O_{t,x}\Psi_t=(H_t(x),\partial_xH_t(x)).
\]

The physical equation is backward heat, \(\partial_tH=-\partial_x^2H\). For a moving projection its time derivative contributes to the intertwining equation. Spatial derivatives also differentiate the projection and basis. The [dimensional-reduction framework](../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/notes/14_DIMENSIONAL_REDUCTION_AND_SUPERSYMMETRIC_HEAT_PROGRAM_20261010.md) records these contracts.

A passive chart change can reveal a symmetry or remove a singular parametrization, while leaving the physical observation unchanged. An active symmetry or intertwiner can produce a new relation among genuine states. Restrictions from actual theta preparation can make that relation more informative than a symmetry of the bulk equations alone. These are distinct operations.

The earlier coordinate work remains constructive. An ordinary double zero is a smooth fold in the time-height plane; its square-root singularity arises when the branches are parametrized by time. A regular chart improves analysis but retains the physical-time tangency. An atlas becomes a proof tool when the source imposes a restriction on that geometry or on the physical value-and-slope pair. See [coordinate invariance and heat folds](../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/4_COORDINATE_INVARIANCE_AND_IMPLICIT_HEAT_FOLDS_20261010.md).

Three useful outcomes for a new identity are:

1. **Visibility of the prepared source.** Derive a nonzero source quantity \(Q\), independently of observation nonvanishing, with
   \[
   Q=aH+bH_x+r,\qquad |r|<|Q|.
   \]
   The coefficients must remain regular and every approximation and boundary contribution must be paid. This excludes joint vanishing. Defining \(a,b\) by dividing by the unknown joint observation does not establish the target.
2. **Signed constraints on the stationary sets.** The existing criterion uses
   \[
   HH_{xx}\le0\quad(H_x=0),\qquad
   H_xH_{xxx}\le0\quad(H_{xx}=0).
   \]
   Both signs are needed for arbitrary finite multiplicity, on neighborhoods containing the preceding stationary branches. A compatible locally bounded-loss version is another stated target. See the [stationary criterion](../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/5_STATIONARY_SIGN_CRITERION_AND_THETA_TARGETS_20261010.md).
3. **A new arithmetic saving.** Preserve a signed coefficient or covariance relation long enough to improve the actual moment bound, including its unit sectors. An invertible duality can be useful, but its quantitative consequence must be derived.

A bounded success establishes a mechanism on its declared domain. An RH implication additionally requires the necessary time and height coverage, cutoff transitions, tails, and the applicable threshold/no-escape reduction.

## A common test for candidate symmetries

For a time-dependent operator \(S_t\) on a common invariant domain, define

\[
\mathfrak D_t(S)=\dot S_t+[S_t,\mathscr G_t].
\]

If \(\Psi\) solves the lifted equation, direct differentiation gives

\[
(\partial_t-\mathscr G_t)(S_t\Psi_t)
=\mathfrak D_t(S)\Psi_t.
\]

This is standard operator bookkeeping, derived here as a search tool. A zero defect makes \(S_t\) a symmetry of that equation; a controlled defect gives a possible inhomogeneous identity. Neither conclusion identifies the transformed source or its physical readout. Each candidate should therefore report its **generator defect, preparation defect, projection law, and boundary defect**. Parameter-changing and anti-linear transformations require their corresponding explicit conventions.

Under a passive change \(\widetilde\Psi=T_t\Psi\), the generator is

\[
\widetilde{\mathscr G}=\dot T_tT_t^{-1}+T_t\mathscr G T_t^{-1},
\qquad \widetilde{\mathcal P}=\mathcal P T_t^{-1}.
\]

For space-dependent charts, the physical connection carries the analogous derivative terms. This prevents a simple-looking generator in one chart from being mistaken for a new dynamical constraint.

### Moving reflection centers

On smooth functions set \((S_af)(x)=f(2a-x)\), and write \(D=\partial_x\). Then

\[
S_aD=-DS_a,\qquad [S_a,-D^2]=0,
\qquad \partial_aS_a=2S_aD=-2DS_a.
\]

Thus fixed-center reflection commutes with the heat generator, while a moving center contributes \(2\dot a S_aD\). A reflection center tied to physical height, time, or a natural cutoff needs the full connection term. The finite polynomial controls verify these identities exactly; the identities do not require a theta source and are not new literature results.

For the continuum inversion in card 1, let \(y=\log v\), \(\mu(\lambda)=\tfrac12\log P(\lambda)\), and use the unitary half-density map \((Uf)(y)=e^{y/2}f(e^y)\). A direct chain-rule calculation gives
\[
[\partial_\lambda+\mu_\lambda\partial_y,R_\mu]=0,
\quad R_\mu g(y)=g(2\mu-y).
\]
In the original coordinate the covariant derivative is
\(\partial_\lambda+\mu_\lambda(v\partial_v+\tfrac12)\).
For a smooth moving cutoff \(\Pi_b=\mathbf1_{y\le b(\lambda)}\), its weak commutator is
\[
[\partial_\lambda+\mu_\lambda\partial_y,\Pi_b]g
=(b_\lambda-\mu_\lambda)\delta(y-b)g(b).
\]
A boundary moving with the reflection center removes this motion defect, but reflection still exchanges its two sides. The exterior channel remains. These analytic bookkeeping identities are derived directly; the retained finite checker does not test distributions or the actual cutoff jump.

### Finite truncation changes the operator algebra

On polynomials of degree at most \(d\), let \(D\) be differentiation and \(M\) multiplication by \(x\) followed by truncation. Then

\[
[D,M]=I-(d+1)P_d,
\]

where \(P_d\) selects the highest-degree coefficient. Dropping this boundary term would incorrectly import the full Heisenberg relation into a finite model. The exact checker verifies it for degrees 2 through 10. A continuum, lattice, or cutoff symmetry needs its own corresponding boundary ledger.

## Candidate map

| Card | Lift or symmetry | New information sought | Readiness |
| --- | --- | --- | --- |
| 1 | Logarithmic inversion and complete cutoff reflection | Signed interior/exterior relation after boundary payments | First tier |
| 2 | Angular Jacobi gluing | A source-selected angular flux identity compatible with Newman heat | First tier |
| 3 | Anchored arithmetic state and Schur elimination | A regular source-to-observation identity with residual below one | First tier |
| 4 | Chord and transverse-gradient fields | A nonlocal theta correlation constraining the physical slice | First tier |
| 5 | Metaplectic and phase-space charts | A regular chart simplifying a source identity and its defect | Supporting tool |
| 6 | Complete paired theta kernels | Positive factorization or both stationary signs | Direct but difficult |
| 7 | Divisor shifts and exact product blocks | A signed relation beyond the built-in exchange symmetry | Bounded algebra test |
| 8 | Cusp coefficients and Poisson return | A paid saving including the short unit sector | Arithmetic continuation |
| 9 | Rank-two theta addition and parity sectors | A complete two-source identity for paired derivative kernels | Bounded identity test |
| 10 | Gaussian-Hermite coefficients | A source-selected restriction beyond positive norm and moments | Bounded identity test |
| 11 | Supersymmetric multi-insertion identities | A regular closed source relation beyond linear score closure | New architecture needed |
| 12 | Canonical systems and boundary reflection | An independently constructed positive transfer or source pairing | Deep missing input |
| 13 | Stable polynomials, Jensen coefficients and Lee–Yang limits | A constructive source preparation preserving real-zero structure | Deep missing input |
| 14 | Integrable and Darboux transformations | A theta-specific invariant compatible with observation and heat | New source constraint needed |
| 15 | Adelic and automorphic compatibility | A global signed relation on the actual common-height orbit | Arithmetic continuation |
| 16 | Radial geometry and sine-moment reflection | A source-conditioned sign surviving the nonlocal generator | Bounded geometry test |

The following cards separate established seeds from the new statement sought. The earlier scouts are retained as evidence: a narrow failed architecture is not a theorem that every related symmetry approach fails.

## 1 Complete reflection across the cutoff boundary

**Established seed.** In [Heat Note 25 section 7](../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/notes/25_ENLARGED_STATE_TRANSPORT_CHORD_DYNAMICS_AND_THETA_GLUING_20261010.md),
\[
(\mathcal I_Pf)(v)=\frac{\sqrt P}{v}f(P/v)
\]
is an exact unitary involution on \(L^2(\mathbb R_+,dv)\). The weighted logarithmic chart sends it to ordinary parity. A literal interval \([A,B]\) maps to \([P/B,P/A]\). The stationary approximation to the physical chirp suggests this reflection, but its global remainder is a separate obligation.

**Statement sought.** An exact or fully paid reflection identity for the complete interior/exterior source response, incorporating finite Poisson integrals, endpoint half-weights, carrier mismatch, and the cutoff defect. The desired consequence is a signed boundary relation or regular adjoint multiplier for the physical observations.

**First test.** Pair one compact block with its reflected exterior block and derive both boundary contributions before estimating either. Evaluate the complete response and the observation-conditioned defect with the same source and phase. Success is a bound stronger than the existing separate absolute envelopes, not agreement of the leading reflection alone.

**Scope.** The stationary scale \(P_{\rm stat}=T/(2\pi)\) is generally not an integer. Its continuum inversion is not automatically a permutation of integer coefficients. It is distinct from an exact product label \(p=nm\). The natural cutoff is an interface, not a harmless invariant subspace. Positive-time chirps require compact blocks or justified weighted domains.

**Readiness.** First-tier identity search: all essential objects already exist, and a complete boundary calculation can produce a useful result even if no excluding sign follows.

## 2 Angular Jacobi gluing and heat compatible shifts

**Established seed.** The full angular field retains
\[
\Theta(r,y)=\sum_{n\in\mathbb Z}e^{-\pi n^2r+2\pi iny},
\qquad
\Theta(r,y)=r^{-1/2}\sum_{m\in\mathbb Z}e^{-\pi(m-y)^2/r}.
\]
This is the classical [Jacobi transformation](https://dlmf.nist.gov/20.7.E32). The existing lift uses \(k(u,y)=e^u[\Theta(e^{4u},y)-1]\) and the half-line transform \(\mathcal T_t(z,y)\). It proves
\[
\pi^{-1}\mathcal T_{yy}(z-4i,y)
=-k(0,y)+2it\mathcal T_z(z,y)-(1+iz)\mathcal T(z,y).
\]
The actual coefficients are all one, and the endpoint source is retained. See [Heat Note 25 section 6](../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/notes/25_ENLARGED_STATE_TRANSPORT_CHORD_DYNAMICS_AND_THETA_GLUING_20261010.md).

**Statement sought.** A relation using the complete modular partner and angular flux that restricts the physical collision readout. Classical modular heat in \(r,y\) and Newman multiplication by \(u^2\) are different evolutions; their intertwining defect must be calculated. The genuine \(H\) is obtained through the declared differential insertion and boundary terms, not by setting \(H=\mathcal T\).

**First test.** Derive the transformed angular identity for the exact theta preparation, with the zero mode subtracted on both sides. Identify which combination of angular derivatives, endpoint data, and shifted spectral channels corresponds to \(H,H_x\) or a stationary product. Retain the full \(z-4i\) channel and derive its growth payment before using a small-disk approximation.

**Readiness.** First-tier identity search. The full gluing data distinguish this architecture from generic positive kernels satisfying an affine scalar endpoint identity.

## 3 Anchored source identities and Schur elimination

**Established seed.** The finite arithmetic state has prescribed prime-edge equations \(B_pq=0\) and anchor \(q_1=e^{i\theta}\). Stacking the edge equations gives
\[
A_{\rm bulk}=B^*B+e_1e_1^*>0,
\qquad q=A_{\rm bulk}^{-1}e_1e^{i\theta}.
\]
Hidden coordinate blocks can be eliminated without assuming that the physical readout is nonzero. This fits the exact block-elimination principle in [Dusson, Sigal and Stamm Theorem 1.2](https://arxiv.org/html/2105.02058v1#S1), while the specific arithmetic construction is in [Heat Note 25 section 3](../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/notes/25_ENLARGED_STATE_TRANSPORT_CHORD_DYNAMICS_AND_THETA_GLUING_20261010.md).

**Statement sought.** A symmetry of the effective source response, or an adjoint identity, producing the source covector from the two physical observation covectors plus prescribed edge constraints and a controlled residual. Existing certificates have the form
\[
b=C^Ty+B_R^T\lambda+za+r.
\]
A residual below one and controlled observation multiplier can establish visibility after paying the approximation error.

For the existing realified finite normalization, the paid criterion is \(R+\eta\|y\|/2<1\). The earlier sharp pointwise optimization equals the scalar observation defect. Unconstrained optimization of the same graph therefore supplies no extra source information; this card needs an independently derived correlated identity from another complete-source representation.

**First test.** Choose a paired partition of the complete finite graph using an explicitly defined index map or a paid continuum-to-discrete interface, retain all prime edges, and compute the effective two-port/source map. Determine whether the reflection constrains its off-diagonal phases or permits an adjoint telescoping estimate unavailable from a spectral gap alone. Use a bounded cell where scalar value and slope tests are inconclusive. Continuum inversion at \(P_{\rm stat}\) is not itself a finite vertex map.

**Scope.** Positive bulk coercivity does not imply observation coercivity. The new finite control in the seed record has an anchored positive matrix of determinant one and a nonzero prepared vector whose two chosen readouts vanish. It is a generic control, not genuine theta data. The actual edge preparation and phase correlations must supply the extra restriction.

**Readiness.** First-tier proof architecture. This is a concrete destination for a new reflection identity, even if the identity is discovered in another lift.

## 4 Chord geometry and nonlocal gradient closure

**Established seed.** The full chord field
\[
\mathcal A_t(k,\ell)=\int e^{iku}\psi_t(u+\ell/2)\psi_t(u-\ell/2)\,du
\]
has \(\mathcal A_t(k,0)=2H_t(k)\) and generator \(-\partial_k^2+\ell^2/4\). Its transverse curvature exposes the Fourier transform of the complete gradient density. The score insertion gives an exact relation among \(\mathcal A,\mathcal A_k,\mathcal A_{kk}\) and the correlated quantity \(D\); see [Heat Note 25 sections 4 and 6](../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/notes/25_ENLARGED_STATE_TRANSPORT_CHORD_DYNAMICS_AND_THETA_GLUING_20261010.md).

**Statement sought.** A theta-specific reflection, gluing, or nonlocal closure that constrains the signed gradient overlap jointly with the physical observation. The observed slice evolves autonomously, so transverse coordinates do not automatically feed a new inequality back into it.

**First test.** Compare the transformed complete chord and gradient fields, including \(D,D'\), under one proposed reflection. Determine whether the relation enforces a useful covariance or stationary sign. Test the precise hypothesis on the existing positive double-zero control; the genuine theta preparation must supply a property that control lacks.

**Scope.** A finite constant-coefficient polynomial closure of transverse curvature is incompatible with the genuine exponential score tail. A nonlocal or arithmetic closure remains a distinct possibility. Positive phase-space norm and purity alone already admit collision controls.

**Readiness.** First-tier source-correlation search, closely coupled to angular gluing and the paired-kernel route below.

## 5 Metaplectic covariance and a regular coordinate atlas

**Established seed.** Wigner, Husimi, Bargmann, and chord descriptions reorganize the same genuine state and its coherent interference. The [Husimi scout](../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/13_microlocal_phase_space/notes/1_HUSIMI_READOUT_DRIFT_AND_COHERENT_INTERFERENCE_20261010.md) derives the entire generator, including the negative momentum diffusion, drift, and contact term, and its exact reconstructed observations. [De Gosson's metaplectic/Radon analysis, section 3](https://arxiv.org/html/2204.07106v1#S3) supplies a primary covariance and reconstruction precedent.

For \(D_r\psi(u)=e^{r/2}\psi(e^ru)\), direct substitution gives
\(\mathcal A_{D_r\psi}(k,\ell)=\mathcal A_\psi(e^{-r}k,e^r\ell)\).
Calling this substitution \(S_r\), the chord generator satisfies
\(S_r\mathscr G S_r^{-1}=e^{2r}\mathscr G\).
Thus a squeeze also rescales evolution; a moving squeeze adds its connection. This standard analytic covariance is a chart seed, not invariance of the prepared theta state.

The displayed chord uses the real theta wavefunction. For a general complex metaplectic image, the usual correlation conjugates the second wavefunction; its generator and readout must be derived with that convention.

**Statement sought.** A useful chart or restricted source symmetry under Fourier rotation, squeezing, or another explicitly defined transform. A covariance law for a representation is a way to transport the equation and observation, not yet an invariance law for the theta-prepared state.

**First test.** In two regular charts, compute the transformed generator and physical observation pair, together with the source's transformation law. Track a candidate reflection defect rather than only the positivity of the transformed state. Compare conditioning of the complete residual payments across the charts.

**Scope.** A fixed-center symmetry may become a moving symmetry along the physical orbit. The connection term from the symmetry-defect ledger is compulsory. A finite approximation must retain its commutator boundary. An arbitrary phase-space rotation need not preserve the theta preparation or map the physical time slices into themselves.

**Readiness.** A supporting discovery tool. It is worthwhile when it simplifies a first-tier identity or estimate; constructing another positive representation by itself is not the intended outcome.

## 6 Paired kernels and positive factorizations

**Established seed.** With \(m_t=e^{tu^2}\Phi_e\), the complete paired kernels are
\[
J_{j,t}(s)=\int r^2(r^2-s^2)^j m_t(s+r)m_t(s-r)\,dr.
\]
The existing normalization gives
\[
(H_t^{(j+1)})^2-H_t^{(j)}H_t^{(j+2)}
=\widehat J_{j,t}(2x).
\]
The stationary targets use \(j=0,1\). See [complete Laguerre kernels](../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/7_COMPLETE_LAGUERRE_KERNELS_AND_TRIPLE_ZERO_LIMIT_20261010.md) and its primary comparison with [Csordas](https://arxiv.org/abs/1309.0055).

**Statement sought.** Derive from theta arithmetic a convergent autocorrelation factorization of the relevant kernels, or a weaker factorization conditioned on the physical stationary sets. A global autocorrelation representation would make the Fourier transforms nonnegative. The signed \(J_1\) source must be allowed: pointwise positivity is the wrong condition and is already false for the genuine kernel at recorded points.

**First test.** Apply addition or modular-reflection identities to the complete paired source before splitting it into individual terms. Compute the resulting matrix-valued or integral kernel and identify the exact quadratic form whose positivity is needed. Test a small Gram minor as a falsification diagnostic, with rigorous tails if claiming a negative minor. A passing finite matrix is not the global theorem.

**Scope.** Positive definiteness of a source kernel differs from positive definiteness of its Fourier response, and from pointwise positivity of either. One low-order Laguerre sign does not cover triples. A factorization derived from an assumed real-zero product would assume the desired conclusion.

**Readiness.** Strongly aligned with the RH target, but the positive factorization is the difficult missing theorem, not an available consequence of the lift.

## 7 Divisor transport and exact product blocks

**Established seed.** In the finite arithmetic lift,
\[
[\mathsf H,\mathsf S_p]=\log p\,\mathsf S_p,
\qquad B_pq=0,
\]
with \(\mathsf H e_n=(\log n)e_n\). The fixed edge weights and anchor select the actual state. Arbitrary multiplicative twists commute with the bulk diagonal evolution but fail those same edge equations. Complete pair sums retain both phase-difference and reflected phase-sum channels. See [Heat Note 25 section 2](../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/notes/25_ENLARGED_STATE_TRANSPORT_CHORD_DYNAMICS_AND_THETA_GLUING_20261010.md) and the [prime-torus program](../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/09_prime_phase_torus/README.md).

**Statement sought.** An arithmetic intertwiner relating divisor transport to reflection, or a relation coupling the product and ratio channels that survives the physical common-height orbit. Within an exact product block \(p=nm\), exchanging \(n,m\) is an exact reflection of the centered logarithmic divisor coordinate. That exchange symmetry is already built into the paired sum; useful new information must constrain an additional signed correlation.

**First test.** Retain the complete cutoff \(N=6\), including the composite coefficient at 6. Compare the candidate identity on the prescribed state and a multiplicative-twist control. Then derive its cutoff boundary term and its effect on the complete physical observation, not just one block. A first successful identity should distinguish the fixed heat coefficients from freely chosen phases.

**Scope.** The finite source anchor \(n=1\) and the unit-cofactor branch in the arithmetic moment proof are different objects. A bridge between them is a research obligation. Independent averaging over prime phases changes the state. Exact product labels also differ from the stationary continuum scale in card 1.

**Readiness.** Second-tier arithmetic algebra with inexpensive faithful finite controls; a plausible source of constraints for cards 1 and 3.

## 8 Cusp reflection and the short moment unit sector

**Established seed.** The arithmetic audit has a precise cusp-coefficient dictionary, including conjugation and frequency reversal, nonidentity cusp phases, shared prime factors, and nonunit fixed-frequency branches. The two-Poisson return retains signed preimage cancellation and a unit sector returning at the same scale. See the [theta source comparison](../inactive/arithmetic_source_audit/notes/THETA_PRIMARY_SOURCE_COMPARISON_20261012.md), [return ledger](../inactive/arithmetic_source_audit/notes/TWO_POISSON_RETURN_AND_TERMINATION_20261012.md), and [Dunn–Radziwiłł section 5](https://arxiv.org/html/2109.07463v3#S5).

**Statement sought.** A cusp or coefficient reflection that preserves a covariance discarded by the positive envelopes and pays a new saving in the small-cofactor branch, including its unit descendants. A different organization of an existing transformation can be valuable if its resulting estimate is stronger. Changing cusp labels without changing the paid estimate is a reformulation.

**First test.** Write one exact \(B=1\) branch beside its transformed counterpart, before positivity enlargements. Retain all cusp components, phases, exclusions, preimage-dependent support restrictions, and finite source terms. A signed preimage count proved after enlarging a domain must be recomputed when earlier restrictions are retained. Trace the identity through the actual coefficient energy and calculate the final normalized saving or decreasing parameter.

**Scope.** The original Möbius moment, canonical Gauss coefficient energy, and auxiliary compensated responses are different families. The cubic metaplectic cusp theta is also distinct from the ordinary Jacobi source of the Newman function; there is no established direct positive-time operator bridge. The proposed short-row estimate would yield \(b=(1+a)/2+5h/12\); an RH consequence through that mechanism requires admissible estimates with \(a,h\) arbitrarily small and the required smooth-profile class. A fixed improved exponent is not that conclusion. Later GRH-conditional dispersion results in Dunn–Radziwiłł cannot be imported as an unconditional RH input.

**Readiness.** Second-tier route to new arithmetic, naturally linked to the unfinished source crosswalk. It should not be merged with the heat lift merely because both use the word theta.

## 9 Rank-two theta addition and the two-source parity decomposition

**Established seed.** Quadratic physical observables already contain two source variables. In their integer lattice sums set \(a=n+m\), \(b=n-m\). The new indices have the same parity, and for \(r_1,r_2>0\),
\[
r_1n^2+r_2m^2
=\frac{(r_1+r_2)(a^2+b^2)+2(r_1-r_2)ab}{4}.
\]
This exact change of lattice exposes two parity cosets and a coupled positive quadratic form. Classical [theta product identities](https://dlmf.nist.gov/20.7.E14), [higher-dimensional modular transformations](https://dlmf.nist.gov/21.5), and [Riemann addition identities](https://dlmf.nist.gov/21.6) provide precedents. The source algebra displayed here is elementary and carries no novelty claim.

**Statement sought.** A complete two-coset identity for the actual paired theta density and its derivative insertions that constrains \(J_0,J_1\), joint observation energy, or a stationary conditional product. This represents an existing quadratic observable; it adds no spectator degree of freedom to the physical source.

**First test.** Choose one complete paired kernel and one modular generator. Transport the differential insertions, zero axes and zero-mode subtractions through the lattice change. Derive the resulting two-coset integral before making a sign estimate. Identify whether its components form a useful positive quadratic form or whether a surviving mixed term is the obstruction.

**Scope.** The source scales \(r_1=e^{4u},r_2=e^{4v}\) are unequal through the full integral. Their cross term cannot be dropped. A same-scale addition formula is only a calibration. Positivity of the lattice quadratic form ensures convergence; it does not give the required sign of an oscillatory Fourier response. Theta characteristics and transformed domains must be retained.

**Readiness.** A strong bounded identity test linking angular gluing to card 6. It is the clearest additional arithmetic correlation candidate found in this survey.

## 10 Gaussian-Hermite coefficients and source-selected correlations

**Established seed.** The complete theta Gaussian lift in [project 17 Note 21](../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/21_COMPLETE_THETA_GAUSSIAN_HERMITE_READOUT_20261011.md) takes \(f(Z)=H_0(x+i\sqrt{2t}Z)\), with \(Z\) standard normal. Four real Hermite coefficients give exactly
\[
H=m_0,\quad H_x=m_1/s,\quad H_{xx}=-m_2/s^2,
\quad H_{xxx}=-m_3/s^3,\qquad s=\sqrt{2t}.
\]
The entire completed source, its Gaussian majorant and all normalizers are fixed; arbitrary analytic coefficient vectors are not the genuine preparation.

**Statement sought.** A modular, reflection or arithmetic relation among the first coefficients, or between them and a controlled high-order tail, stronger than the generic positive Parseval norm. In the zero-loss case the desired stationary signs become \(m_0m_2\ge0\) when \(m_1=0\), and \(m_1m_3\ge0\) when \(m_2=0\).

**First test.** Transport one identity from cards 2 or 9 through the complete Gaussian transform. Print its coefficient relation and boundary/growth payment. Compare with the earlier [Fock observation kernel](../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/02_bargmann_fock/README.md): a generic positive norm leaves a large blind subspace, so the relation must restrict the actual coefficient sequence.

**Scope.** The displayed chart requires \(t>0\); the \(t=0\) limit needs the corresponding direct jets or justified rescaling. Moving \(s\), normalization, and source dependence must be differentiated when deriving time identities. A finite coefficient relation is useful only with its omitted tail paid.

**Readiness.** A practical comparison chart for the first-tier searches, with a definite signed target rather than another general positivity construction.

## 11 Supersymmetric identities and a theta Stein kernel

**Established seed.** The [SUSY scout](../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/03_susy_dirac_hodge/README.md) prepares \(g_t=\sqrt{\rho_t}\), \(W_t=-\log\rho_t\), and \(B_t=\partial_u+W_t'/2\). Its actual moving ground state and Ward identities are exact, while linear Gaussian-score closure is excluded. The positive SUSY Hamiltonian is not the Newman time generator.

A useful additional dictionary follows from the classical [Stein integration-by-parts formula, Saumard section 2](https://arxiv.org/html/1804.03926v3#S2). For the even normalized theta density, define
\[
\tau_t(u)=\rho_t(u)^{-1}\int_u^\infty v\rho_t(v)\,dv.
\]
Then \((\tau_t\rho_t)'=-u\rho_t\), so
\[
B_t^\dagger(\tau_tg_t)=ug_t.
\]
For \(C_t(x)=H_t(x)/H_t(0)\) and
\(T_t(x)=\mathbb E_{\rho_t}[\tau_t(u)e^{ixu}]\), integration by parts gives
\[
C_t'(x)=-xT_t(x).
\]
The complete source has the decay and moments needed for these integrals and their first two spatial derivatives; the boundary product \(\tau_t\rho_t\) vanishes at both ends. These are standard identities specialized and rearranged here, not a previously unknown theta identity.

**Statement sought.** A theta reflection or multi-insertion relation controlling this weighted Fourier channel. For \(x>0\), the two zero-loss stationary targets become exactly
\[
C_tT_t'\ge0\quad(T_t=0),\qquad
T_t(2T_t'+xT_t'')\le0\quad(T_t+xT_t'=0).
\]
This avoids the excluded assumption of a linear score, but leaves the substantive signed correlation open.

**First test.** Derive the complete theta representation of \(\tau_t\rho_t\), then its modular or paired-source transformation. Compare the proposed signed relation with a smooth positive collision control. A small Gaussian-score discrepancy or positivity of \(\tau_t\) alone does not imply the displayed signs. Treat \(x=0\) directly; it has \(H_t(0)>0\).

**Scope.** \(\tau_t\) changes with time and its time derivative must enter any evolution or intertwining argument. This is a weighted integral insertion, not finite polynomial closure. The [cohomological quartet obstruction](../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/04_cohomological_localization/README.md) applies to its specified regular closed completion; a different complex or insertion family needs a new source/reduction proof.

**Readiness.** A concrete nonlocal operator seed for cards 4 and 6. Its dictionary is available now; its theta-specific sign is a separate research task.

## 12 Canonical systems and arithmetic boundary reflection

**Established seed.** Positive canonical systems naturally constrain paired boundary data. [Suzuki's explicit zeta canonical system](https://arxiv.org/abs/1204.1827v2) uses arithmetic reflection kernels and the quotient
\[
\Theta_\omega(z)=\frac{\xi(1/2-\omega-iz)}{\xi(1/2+\omega-iz)}.
\]
Its unconditional construction is for \(\omega>1\). Inner-function criteria and extension toward all \(\omega>0\) connect to RH; that extension is not an available positivity input.

**Statement sought.** An independently derived arithmetic transfer/source map placing the actual physical observation in a valid positive two-channel boundary pairing. A comparison with the existing complete-xi Gaussian transform might expose a source-selected nonlocal reflection relation without assuming unknown innerness.

**First test.** Work in the unconditional \(\omega>1\) regime. Write the exact arithmetic kernel, truncation endpoints, canonical pair, and map to the repository's xi normalization. Determine which physical source or observation it controls, and calculate the Newman-heat compatibility defect. State precisely what new estimate would be needed before taking smaller \(\omega\).

**Scope.** The [boundary scout](../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/11_boundary_extensions/README.md) rejects an exact identification of the entire heat function with a nonzero passive scalar resolvent because an observed pole survives. A numerator/source construction or homogeneous boundary pair is a distinct possibility. Constructing a positive canonical system from an already assumed real-zero product would assume the crucial input. Boundary uniqueness helps only after the actual observation has been proved to be its Cauchy data.

**Readiness.** A serious arithmetic reflection lead, with a high-cost missing transfer theorem. Its unconditional range is suitable for a comparison experiment, not an RH conclusion.

## 13 Stable polynomials, coefficient positivity and Lee–Yang limits

**Established seed.** [Borcea–Brändén](https://arxiv.org/abs/0809.0401v3) classify multivariate polynomial operators preserving nonvanishing in prescribed circular domains. [Griffin, Ono, Rolen, Thorner, Tripp and Wagner](https://arxiv.org/abs/1910.01227v3) make fixed-degree, sufficiently-large-shift hyperbolicity effective for the Riemann xi Jensen polynomials. The all-degree/all-shift criterion is much stronger than that asymptotic theorem. These references are framework leads here; no stability-preserver theorem has been applied to the actual theta preparation in this scout.

**Statement sought.** A constructive sequence of source-selected stable polynomial or ferromagnetic partition-function approximants converging to the complete physical function on complex compact sets, with the required heat evolution. Theta addition or reflection might supply a preparation operation whose stability can be checked independently.

**First test.** Specify the actual coefficient family and every operation used to prepare it. The centered degree-two polynomials
\[
H+2H_xs+H_{xx}s^2,\qquad
H_x+2H_{xx}s+H_{xxx}s^2
\]
have discriminants \(4(H_x^2-HH_{xx})\) and \(4(H_{xx}^2-H_xH_{xxx})\). A source-selected stable construction of these polynomials would give concrete sign information. A coefficient alternative uses the positive Taylor coefficients of \(F_t(w)=H_t(i\sqrt w)\), with their factorial normalization retained, and its Toeplitz rather than Hankel minors. These are new targets, not established stable constructions.

For a spin test, keep unequal positive amplitudes \(a_i\) and fixed base ferromagnetic couplings, with exponent \(\sum_{i<j}J_{ij}\sigma_i\sigma_j\). Newman weighting of \(S=\sum a_i\sigma_i\) by \(e^{tS^2}\) adds exactly \(2ta_ia_j\) to each pair coupling. A realization must preserve this law instead of refitting each time. Pay complex convergence and the coefficient/heat normalization. Finite moment matching or a finite list of hyperbolic Jensen polynomials is only a diagnostic.

**Scope and normalization.** Ordinary total nonnegativity of the translation kernel \(\rho(u-v)\), often called source-density PF\(_\infty\), is the wrong global target. [Schoenberg's reciprocal-transform theorem as stated in Belton–Guillot–Khare–Putinar, Theorem 8.2](https://math.iisc.ac.in/~khare/papers/TN-note.pdf) makes its bilateral Laplace transform zero-free on its defining strip, including the Fourier axis. This conflicts with the known real Fourier zeros of the genuine source. A properly normalized **coefficient sequence**, Jensen polynomial, or the paired kernels of card 6 is a different object. Ordinary positive Hankel moment matrices are shared by positive collision controls.

The [Lee–Yang scout](../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/15_lee_yang/README.md) already excludes two equal-weight spin families by rigorous low moments. Unequal weights and other positive interactions remain possible architectures, but their realization of the genuine source is unproved.

**Readiness.** A potentially global route with an RH-strength preparation theorem missing. The next useful result is an explicit admissible preparation or a precise obstruction, not a general appeal to stability or total positivity.

## 14 Orthogonal-polynomial Volterra flow and integrable transformations

**Established seed.** The [integrable matrix scout](../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/14_integrable_lax/README.md) gives an exact finite heat matrix dictionary and a joint compact approximation payment for genuine theta moments. The rank-one Calogero–Moser commutator is shared by a polynomial with a prescribed positive-time collision.

Another exact lift uses the monic orthogonal polynomials for the actual even measure \(e^{tu^2}\Phi_e(u)\,du\). Write
\[
up_n=p_{n+1}+a_n(t)p_{n-1},\qquad
a_n=h_n/h_{n-1}>0,\quad a_0=0.
\]
Differentiating the norms and using orthogonality gives
\[
\partial_t\log h_n=a_{n+1}+a_n,\qquad
\dot a_n=a_n(a_{n+1}-a_{n-1}).
\]
This is the standard Volterra flow, derived here for the full theta measure. Its Gaussian exponential moments ensure moment determinacy. In the orthonormal basis, the corresponding selfadjoint Jacobi operator has off-diagonal entries \(\sqrt{a_n}\) and spectral readout
\(C_t(x)=\langle e_0,e^{ixJ_t}e_0\rangle\).
Integration by parts on the polynomial core also gives the score/string relation \(D+D^*=W_t'(J_t)\), where \(D\) represents differentiation in that orthonormal basis. The right side retains the nonpolynomial genuine theta score. [Clarkson, Jordaan and Loureiro](https://arxiv.org/html/2504.08522) provide related orthogonal-polynomial/Volterra context for a different, polynomial Freud weight; their specific source equations are not imported for theta.

**Statement sought.** A Darboux, contiguous, Lax or other explicitly defined transformation that preserves the actual theta preparation and forces a new invariant on the physical observation. The conjectural gain is arithmetic state selection, not integrability of the general finite heat equation.

**First test.** Recover a small block of actual theta recurrence coefficients and score/string matrix elements from enclosed moments, with determinant conditioning recorded. Compare with the positive collision control and seek one source-specific relation before proposing a Darboux or Lax argument. For a chosen transformation, calculate its generator defect, transformed initial data and observation law, including zeros introduced or removed by its factors.

**Scope.** Positive Jacobi coefficients, Volterra integrability and a generic string relation are shared by other positive measures; they do not imply the requested oscillatory sign. A finite Jacobi block needs its next coefficient in the evolution and is not an invariant closed heat system. A Darboux factor involving \(H_x/H\), or another unknown nonvanishing denominator, is singular at the collision question. Coefficient or matrix realizations can avoid that chart singularity, but require a regular physical reduction and cutoff payments. No theta-specific invariant closing the sign or visibility target was found.

**Readiness.** An exploratory algebra direction. Continue only after naming a transformation tied to the actual source rather than a universal finite heat property.

## 15 Adelic compatibility and the automorphic spectral channel

**Established seed.** The [adelic scout](../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/08_adelic_local_models/README.md) reproduces all composite heat weights using one shared Gaussian coordinate. In its unramified class, triviality on diagonal positive rationals forces all local prime factors to share one archimedean exponent. [Tate's original thesis, sections 2.3 and 4.2–4.4](https://sites.math.rutgers.edu/~alexk/2023S572/Tate1950.pdf) supplies the local/global Fourier and Poisson framework. It does not give an observation inequality.

**Statement sought.** A global Fourier or source compatibility relation yielding a signed constraint on the actual common-height orbit, or a valid boundary pairing for the exact automorphic heat channel. Selecting one common exponent restricts the admissible family; it does not exclude collisions in that family.

**First test.** Construct one finite-place/real-place coupled identity retaining every permitted composite, beginning with 6, and both reflected carriers. Compare its physical value and slope before and after the declared transformation. Identify an additional covariance that fails for independent local twists. In the automorphic version, calculate the completion and heat commutator first and specify the pairing on the selected spectral slice.

**Scope.** The [automorphic scout](../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/07_automorphic_scattering/README.md) already obtains exact zero-time xi extraction, but ordinary modular Laplacian heat does not intertwine and the critical-line xi channel lies off the unitary modular spectral slice. A positive modular Laplacian therefore supplies no automatic positivity for the required response. At positive Newman time the Gaussian superposition is not one character, and a divergent Dirichlet series cannot be made into an Euler product by an unjustified interchange.

**Readiness.** A framework for genuine state selection and a possible companion to cards 3, 7 and 8. A new quantitative physical identity is still needed.

## 16 Radial geometry and reflected sine moments

**Established seed.** The genuine theta density has a strictly positive three-dimensional radial inverse on the recorded time interval \(0\le t\le1/20\), with an exact multiplication-minus-Volterra generator. [The radial continuation](../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/12_radial_bessel/README.md) also gives explicit sine collision jets and source-dependent obstructions to positive Gaussian mixtures and unlimited positive radial dimension.

**Statement sought.** A theta-specific relation among reflected radial or sine-moment channels that pays the nonlocal generator term and yields the required conditional sign. A geometry that makes the cancellation visible can be useful even though the general positive cone is not invariant.

**First test.** In dimension three, take the exact candidate-conditioned sine expression and pair its positive and reflected negative contributions before estimating them. Derive the Volterra boundary contribution and test whether theta gluing imposes a signed relation. Alternatively, classify one of dimensions 5, 7 or 9 with the exact inverse marginal and observation dictionary.

**Scope.** Smooth positive radial sources already permit a prescribed positive-time double zero, so radial positivity alone cannot exclude collisions. On \(0\le t\le1/20\), integer dimensions at least 11 are excluded for exact positive rotation-invariant realization by the recorded genuine-source obstruction. A change to anisotropic or nonpositive geometry is a new model requiring its own reduction and domain.

**Readiness.** A bounded geometry test with explicit controls. It is a secondary direction until a source-conditioned sign survives the nonlocal correction.

## What should stay closed unless its hypothesis changes

| Existing result or obstruction | Hypothesis needed to reopen the direction |
| --- | --- |
| A passive coordinate change preserves physical collisions; a smooth fold can still have a singular time parametrization | A restriction on the genuine source or improved control of an excluding identity in the new chart |
| Reflection commuting with backward heat also permits even heat polynomials with positive-time double zeros | A theta preparation law stronger than parity, with complete projection and boundary terms |
| Positive Fock/Husimi norms, ordinary moment matrices, or an anchored positive bulk matrix do not force two observed channels to be visible | A source-to-observation estimate or source-selected signed correlation |
| The actual theta score excludes exact Gaussian linear closure in the current SUSY model | A regular multi-insertion or nonlocal identity with a specified new closure mechanism |
| The declared zero-dimensional quartet has no regular even closed completion with the required cosine bosonic component | A different complex or completion with its source and reduction explicitly proved |
| Scalar angular Ward identities and the full affine endpoint hierarchy are shared by smooth positive collision controls | The integer coefficient family and full modular angular gluing supply an additional restriction |
| Independent prime heat misses composite 6; shared Gaussian heat still allows multiplicative twists | Genuine fixed edges and global compatibility yield an observation-relevant inequality on the physical orbit |
| Ordinary modular Laplacian heat does not give the required Newman evolution, and the xi slice is outside the unitary spectral slice | An exact intertwining and a valid pairing on the selected spectral channel |
| A nonzero passive scalar resolvent has a surviving pole and cannot equal the entire heat function | A source numerator or homogeneous two-channel boundary construction in the correct response class |
| Three-dimensional positive radial realization exists, but its Volterra generator fails positivity on the general cone | A theta-conditioned sine-moment inequality with the nonlocal correction paid |
| Positive Gaussian mixtures and positive rotation-invariant realizations in integer dimensions at least 11 are excluded by the recorded genuine-source tests | Another specified geometry; dimensions 5, 7 and 9 remain separate tests |
| The finite Calogero rank-one relation holds for a heat collision control | A theta-specific invariant beyond that universal finite relation |
| Equal-weight independent spins and two equal-weight ferromagnetic spins fail rigorous low-moment requirements | An explicit different spin family with ferromagnetic signs, matching source and complex convergence |
| Universal finite-moment nonlinear closure fails on a neighborhood of positive densities | A theta-specific nonlocal constraint; changing an interaction while preserving the entire cosine observation adds no hidden freedom |
| A leading stationary reflection leaves the base quadratic obstruction unchanged; a two-Poisson unit branch returns at the same scale | A complete signed covariance or genuine decrease in a declared paid parameter |

These conclusions have different scopes. The control examples reject arguments based only on the listed generic property. They do not reject every use of the corresponding framework. The exact source-dependent obstructions reject their stated realizations, and should not be silently extended to every possible lift.

## Suggested order for later conversations

The next conversations can choose a single small objective from this map. A useful order is:

1. **Complete one reflected cutoff block.** Derive the exact paired boundary response and its defect, including the exterior. This most directly tests whether the original reflection intuition survives the full source.
2. **Derive the angular gluing defect and physical insertion.** Work with the full theta field and one shifted channel; identify the actual observation covectors. Continue if the relation constrains a signed source quantity unavailable from the scalar endpoint hierarchy.
3. **Try a two-source parity decomposition of the complete paired kernels.** Preserve the unequal-scale cross term and derivative insertions. Continue if the resulting matrix or integral kernel has a new structured factorization; report a precise obstruction if it does not.
4. **Feed a surviving identity into the anchored adjoint problem.** On one faithful finite cell, prove a bounded source representation and pay its residual, or identify the term preventing it. This connects a discovered identity to a testable collision-exclusion mechanism.
5. **In parallel, keep the arithmetic target concrete.** Choose one short-cofactor unit branch and retain the transformed cusp phases. Continue for a quantified saving or contraction, not an additional dual description with the same envelope.

Cards 5 and 10 can improve the coordinates and conditioning of these tasks. Cards 11–16 are retained because the lift suggests meaningful connections, but each needs its declared additional preparation or transfer theorem before a large computation is justified.

For every continuation, record the state and domain, generator, physical projection, source law, full symmetry defect, cutoff/tail payment, and the precise sign or visibility consequence. Compare the proposed hypothesis with an existing collision control. This keeps the search open while making each negative result informative.

## Evidence and limits of this first search

The search revisited the dimensional-reduction program, the enlarged-state transport and theta-gluing note, the coordinate and stationary-sign notes, the complete paired kernels, the Gaussian-Hermite and cutoff interface, all relevant higher-dimensional scouts, and the current arithmetic source audits. It also checked primary mathematical precedents for modular/addition identities, block elimination, canonical systems, polynomial stability, and the normalization of total positivity. Exact sections and access levels are recorded in the linked source record; an abstract-level literature lead is not a verified theorem application.

The retained exact finite checks establish the operator formulas used as seeds and supply two generic controls: a parity-symmetric backward-heat polynomial with a positive-time double zero, and a positive anchored bulk matrix with a blind two-channel output. They are bookkeeping and argument-screening checks. No new genuine-theta enclosure, finite nonvanishing certificate, source-saving estimate, or global positivity theorem was computed for this note. Prior numerical and formal milestones keep their original scope.

The broad conclusion is constructive: the lift supplies several places where an identity could live, and it provides regular algebra for testing them. The most useful hidden symmetry would constrain **preparation and observation together**, or relate complete paired sources before cancellations are discarded. That is the additional input connecting a lifted identity to the existing RH reductions.

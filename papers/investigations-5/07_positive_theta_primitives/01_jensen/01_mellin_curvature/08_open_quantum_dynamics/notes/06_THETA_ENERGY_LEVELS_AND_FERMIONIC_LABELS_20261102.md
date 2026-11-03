# MC08-B03 discussion: theta energy levels and fermionic labels

2 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded **gpt-6-astra / xhigh**, chat `01a19e4c-7083-7282-92f6-f6cbeb970065`, turn `01a19f10-d6a5-7d61-b4ec-7cdfefdc97bc`; same MC08 history 0003.

**Status:** clarification and continuation of the existing B03 discussion. The energy interpretation and response dictionary below reuse the reviewed MC01 identities. No new signed estimate, numerical campaign or selected proof mechanism is claimed. MC08 remains open; B02's mechanism-specific stop and pending E04 verification are unchanged.

| Next task | Type | Recommended model | Readiness/dependency | Expected output |
| --- | --- | --- | --- | --- |
| MC08-B03, energy-response discussion | B — brainstorm | Astra: the missing source-dependent relation is still a conceptual choice | Ready; reuse MC01's reviewed dictionary | Identify a concrete additional relation among complete-spectrum energy responses and its signed consumer, or explain the particular failed proposal |
| MC08-E04, separate alternative | E — execution | Sol | Ready under frozen Handoff05 | Check only B02's scoped obstruction and cancellation identities |

Read with the [result index](../../../../../../../result-summaries/README.md), particularly [theta identities](../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), and the [avoid index](../../../../../../../avoid/README.md), particularly [re-realizations](../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [joint signed estimates](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) and [sibling results](../../../../../../../avoid/15_ignoring_sibling_results_and_unfinished_closures.md).

## 1. Which index is being discussed?

The [original physical interpretation](../../notes/04_FERMIONIC_CORRELATORS_AND_PHYSICAL_INTERPRETATIONS_20261101.md) defines orbitals in L²((0,infinity),du),
\[
f_i(u)=\frac{\Phi^{(2i)}(u)}{\sqrt{\Phi(u)}},\qquad
 g_j(u)=\frac{u^{2j}\sqrt{\Phi(u)}}{(2j)!}.
\]
Full-source integration by parts gives their overlap c_{j-i}, with the usual zero convention for negative coefficient indices. The determinant is a fermionic exterior overlap. The indices i,j specify derivative and moment insertions, not eigenvalues of a chosen Hamiltonian. Those orbital families are not orthonormal, and assigning them different energies of one self-adjoint operator would require orthogonality that has not been established and does not generally hold.

The [MC02 transfer](../../02_fermionic_correlators/notes/01_THETA_ORBITAL_COMPARISON_RETURN_20261101.md) also uses orthonormal coefficient sites |i> in l²(N0). These sites are distinct from theta spectral modes. Their transfer K_v=F(vS)/F(v) is not asserted to be a Gibbs operator. MC08 later constructs a Hermitian one-particle Hamiltonian H(v)=i(G-G†)/2 and linear losses from G=K'_v K_v^{-1}. Thus the completed MC08 model does have a Hamiltonian; it is derived from the transfer, mixes coefficient sites, and is not the diagonal circle Hamiltonian described next. Activity v, source coordinate u, inverse temperature beta, Mellin tilt s and physical heat time are distinct parameters.

## 2. The source has a natural spectrum

On the circle of circumference 2pi take
\[
L=-\pi\partial_x^2,\qquad L|m\rangle=\pi m^2|m\rangle,
\quad m\in\mathbb Z.
\]
Set E_m=pi m² for m>=1, beta=e^{4u}, and
\[
Q(\beta)=\sum_{m\ge1}e^{-\beta E_m}
=\tfrac12(\operatorname{Tr}e^{-\beta L}-1).
\]
The factor one half removes the double counting of the +/-m degeneracy; the subtraction removes the zero mode. The original primitive is exactly
\[
p(u)=e^uQ(e^{4u})=\beta^{1/4}Q(\beta).
\]
Thus each theta summand is a Boltzmann weight for energy pi m², multiplied by the common scale factor e^u. This is an ordinary one-particle heat trace identity, already recorded in the earlier notes. The energy units are chosen to match the canonical exponent; no measured physical energy scale is inferred.

The standard theta series is [DLMF 20.2.3](https://dlmf.nist.gov/20.2.E3), inspected online on this turn at z=0, q=e^{-pi beta}. Only that defining series is imported; the following differentiations are elementary and already occur in MC01.

Since Phi=(p''-p)/8, direct differentiation yields
\[
p''=e^u\{Q+24\beta Q'+16\beta^2Q''\},
\]
\[
\boxed{\Phi(u)=e^u\sum_{m\ge1}
P_0(\beta E_m)e^{-\beta E_m},\qquad P_0(x)=2x^2-3x.}
\]
Equivalently Phi/p=2 beta² <E²>_beta -3 beta <E>_beta in the ordinary Gibbs distribution on positive modes. On the required half-line u>=0, beta E_m>=pi>3/2, so each P0 factor is positive. This produces a positive **filtered** thermal distribution
\[
\rho_u(m)=\frac{P_0(\beta E_m)e^{-\beta E_m}}
{\sum_{n\ge1}P_0(\beta E_n)e^{-\beta E_n}}.
\]
The filter depends on temperature. It cannot be ignored when differentiating an expectation. Positivity of this filter is asserted here for beta>=1 only.

## 3. The exact link to the original i-labelled states

The [MC01 return](../../01_circle_thermal_trace/notes/01_THERMAL_SOURCE_IDENTITY_RETURN_20261101.md), equations (4)-(8), defines
\[
P_{r+1}(x)=4xP'_r(x)+(1-4x)P_r(x)
\]
and proves
\[
\boxed{\frac{\Phi^{(2i)}(u)}{\Phi(u)}
=E_{\rho_u}\!\left[\frac{P_{2i}(X)}{P_0(X)}\right],
\qquad X=\beta E_m.}
\]
Consequently f_i(u) is sqrt(Phi(u)) times this energy-response expectation. **i is the response order, whereas m labels the energy level.** This is a concrete relation between the two constructions, not an identification i=m. Likewise c_j averages all levels over the source coordinate with weight u^{2j}/(2j)!; it is not a single Boltzmann weight for E_j.

These formulas were accepted without correction by [MC01-E01](../../01_circle_thermal_trace/reviews/01_MC01_E01_SEPARATE_REVIEW_20261101.md), a separate cross-model internal LLM review with shared canonical inputs, not specialist validation. The current note does not claim to have newly discovered or separately re-reviewed that result.

## 4. If we make the energy levels fermionic

There is also a natural free-fermion construction on the positive-mode one-particle space:
\[
\mathbb H_\theta=\sum_{m\ge1}E_m b_m^\dagger b_m,
\qquad E_J=\sum_{m\in J}E_m.
\]
The sum defines the usual nonnegative occupation-energy operator on its natural domain. For beta>0 its grand partition function is
\[
\Xi(\beta,z)=\prod_{m\ge1}(1+z e^{-\beta E_m}),
\qquad [z]\Xi(\beta,z)=Q(\beta).
\]
The product identity follows by summing the two possible occupations of each mode; convergence follows from the finite one-particle heat trace. The primitive uses the **one-particle coefficient** of this product. It is not the entire grand partition function, and replacing F(v) or the original signed overlap by Xi would change the research target. Here b_m creates an energy eigenmode; it is not identified with MC08's coefficient-site annihilator a_i. A unitary or observable bridge between those operators is not supplied by renaming their indices.

## 5. The surviving decision

The established energy dictionary is useful, but generic thermal positivity was already tested in MC01 and did not supply the sign. In the order-three overlap, rows 1, Phi''/Phi and Phi''''/Phi become expectations of 1, P2/P0 and P4/P0. The resulting determinant is a signed observable on three independent filtered thermal copies. Positive probabilities do not sign that observable, and ordered temperatures do not order every sampled scaled energy beta_j E_{m_j}.

The actual outstanding joint correction is recorded in MC01 equations (15)-(18): writing R=Phi''/Phi and S=Phi''''/Phi, the residual U=S-R² contains third/fourth and mixed energy responses; its divided difference chi enters h3=1+chi. The Mellin comparison still needs the complete combination of carrier variance and the two covariances involving chi. An ordinary nonnegative energy variance does not control it. MC01's one-mode witness excludes a positivity-only pointwise transfer; it does not exclude integrated comparisons using the full integer-square spectrum and reflection. B02's intermediate-cone obstruction likewise does not close this direction.

**Continuation guidance:** retain the existing exact dictionary and discuss whether the complete square spectrum plus theta reflection supplies an additional integrated relation among these responses. A promising proposal must state what it bounds, how it reaches the signed endpoint or Mellin consumer, and what extra information it uses beyond positive thermal weights. A formula that merely renames U or the desired covariance balance is not a gain. No new numerical task is issued until such a proposal has a bounded test and completion condition.

**For a model change:** read this note, MC01 Return01 §§2-5 and Review01, Primer05, and the sole MC08 register. Preserve all index/parameter distinctions and full-source normalizations. The next conceptual discussion remains B03/Astra. E04/Sol is a separate pending verification, not a prerequisite for discussing the already reviewed thermal dictionary. If a fixed analytical comparison is selected, write its E packet and recommend Sol before execution.

Pasteable prompt: “Continue [B] MC08-B03 with the energy-spectrum idea in Note06. Use the reviewed MC01 energy-response identity to discuss one concrete relation capable of controlling the signed order-three consumer. Distinguish a new estimate from a restatement; retain all modes, filter derivatives and mixed terms. Do not identify the derivative index i with the energy index m or replace the original transfer by a grand partition function.”

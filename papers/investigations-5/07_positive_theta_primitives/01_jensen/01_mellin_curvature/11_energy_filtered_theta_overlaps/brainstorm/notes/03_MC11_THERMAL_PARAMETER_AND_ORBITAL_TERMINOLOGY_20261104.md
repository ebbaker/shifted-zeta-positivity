# Thermal parameters and auxiliary source functions

4 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance from **gpt-6-astra (Codex), reasoning effort xhigh**, recorded for this turn. Thread `01a1a9d4-3d44-7472-ae0f-54705423d86b`, MC11 history0002. This explanatory correction follows the author's objection that calling functions of u orbitals gives an overly direct physical interpretation when u is a function of inverse temperature. It does not alter the determinant identities or assess the E03 calculation.

The objection identifies a missing physical identification. The particle-in-a-box heat trace has an ordinary thermal interpretation. Forming a Hilbert space of functions across temperatures is an additional mathematical construction. Calling its vectors physical orbitals or preparations, without specifying a physical realization, overstates what that construction establishes.

## The established physical input

The box Hamiltonian acts on L²((0,1),dx), with Dirichlet eigenfunctions and energies E_n=pi n². At a fixed inverse temperature beta, the canonical state is the density operator
\[
\rho_\beta=\frac{e^{-\beta H}}{\operatorname{Tr}(e^{-\beta H})}
\]
on that same position-space Hilbert space. Beta labels a family of states; it is not thereby a particle coordinate or a quantum observable. This is the standard canonical-ensemble distinction; see [David Tong's statistical physics lectures, section 1.3.1](https://www.damtp.cam.ac.uk/user/tong/statphys/statmechhtml/S1.html).

The effect W_s=P_1+s(I-P_1) has an energy-filter interpretation. The function Z_s(beta)=Tr(W_s exp(-beta H)) is the unnormalized accepted thermal weight. These are the physical inputs to the existing [MC11 construction](../../research-overview/01_ENERGY_FILTERED_THETA_OVERLAPS_RESEARCH_OVERVIEW_20261104.md).

## The additional mathematical space

With u=log(beta)/4, the transformed source Phi_s(u) is a scalar function of a thermal parameter. The vectors
\[
f_i=\frac{\Phi_s^{(2i)}}{\sqrt{\Phi_s}},\qquad
g_j=\frac{u^{2j}}{(2j)!}\sqrt{\Phi_s}
\]
belong to an auxiliary L² space in u under the established finite-index conditions. Its norm integrates across temperatures:
\[
\|\psi\|^2=\int_0^\infty|\psi(u)|^2du
=\int_1^\infty\left|\psi\!\left(\tfrac14\log\beta\right)\right|^2\frac{d\beta}{4\beta}.
\]
This is a well-defined mathematical inner product. It does not become a Born-rule probability over temperature merely because it is an L² norm. No physical superposition over different temperatures, preparation of these particular functions, or measurement of this pairing has been specified by the box/filter construction.

A general quantum encoding of an auxiliary Hilbert space is possible in principle, and physical one-particle states need not be expressed in position coordinates. The objection is therefore not a universal ban on nonspatial orbitals. It is that the present source-space interpretation needs a separate operational justification. A proposed realization would have to identify its degrees of freedom, preparations and measured quantity, and justify its connection to the canonical source. If dynamics were claimed, those would also need to be specified. An abstract isomorphism or a newly chosen Hamiltonian alone would not establish that the box itself realizes this construction.

## What antisymmetrization establishes

For any suitable Hilbert-space vectors, exterior algebra gives
\[
\langle f_1\wedge\cdots\wedge f_q,
        g_1\wedge\cdots\wedge g_q\rangle
=\det[\langle f_i,g_j\rangle].
\]
Together with the source integration-by-parts identity, this is the exact representation used by MC11. Its permutation signs are determinant signs. They admit a formal fermionic description, but they do not by themselves demonstrate Pauli exchange of actual box particles or an exchange interaction.

Likewise, a normalized inner product has the geometry used for quantum transition amplitudes. Calling its squared modulus a physical projection probability here requires an identified state preparation and measurement. The earlier explanation blurred this distinction. The source families are also not identified as the eigenstates of the physical box; the source indices and the box energy index remain distinct.

## Terminology for this discussion

| Earlier wording | Preferred wording |
| --- | --- |
| Orbitals in u | Auxiliary source functions, or derivative and moment functions |
| Two physical preparations | Two source-function families |
| q particles or q orbitals in the source model | Determinant order q, or q vectors in each exterior product |
| Fermionic overlap | Exterior-product pairing; formal fermionic representation when that analogy is useful |
| Exchange causes the response sign | Signed determinant terms and their cofactors control the response |

The research question can be stated without the extra physical identification: **How does reweighting the canonical box energy levels change a signed determinant functional of the thermal trace?** The E02/E03 spectral decomposition addresses that question. Its numerical bounds and algebra are unaffected by the terminology correction; their assessment remains with E04. It would take additional work to interpret the response as a transition between actual many-fermion states.

The [physics explanation](02_MC11_PHYSICS_MODEL_EXPLANATION_20261104.md) has been revised to use this distinction. This is a correction to our explanatory language, with no global rename or change to the concurrent assessment's frozen inputs. The [result index](../../../../../../../../result-summaries/README.md) and [theta cluster](../../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md) retain the underlying source identities. The [patterns index](../../../../../../../../avoid/README.md), especially [re-realizations](../../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), records why an exact auxiliary representation does not automatically supply a physical mechanism or a new sign estimate.

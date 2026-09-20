# Internal source audit for the endpoint-response test

20 September 2026. OpenAI GPT-6 (Codex; developer-provided identity).
Effort setting: unavailable; not exposed in this session.
Reviewer: the same assistant conducting the calculation, not an independent
agent, specialist, or referee.

## Finding

No substantive error was found in the distinction between failure of ordinary
dilation on arbitrary fixed-charge representatives and radial evolution on
the common canonical Hodge states. The Gaussian calculation uses only the
latter. It does not extend the Hodge identity to every boundary module or
equivariant complex.

Primary texts were inspected directly:

- [Dedushenko--Pufu--Yacoby, arXiv:1610.00740v2](https://arxiv.org/html/1610.00740v2):
  scalar variations (2.8)--(2.9), conformal action/reality (2.10)--(2.11),
  charges and exact generators (3.1)--(3.5), stereographic twist (3.6)--(3.8),
  and dilation/Killing-spinor conventions (C.7)--(C.13).
- [Dedushenko, Gluing II, arXiv:1807.04278v3](https://arxiv.org/html/1807.04278v3):
  Higgs polarization (78)--(82), its free-hyper example in Section 4.3.2,
  boundary actions (125)--(126), and vacuum boundary condition (127)--(128).

The first source explicitly supplies the positive Hodge anticommutator for
the individual nilpotent charges and their common kernel. The second supplies
the original boundary polarization, not the new Gaussian mode interface.
Neither source is being cited as a derivation of the latter's spectral weights.

## Checks of the inherited argument

1. **Fixed insertion versus moving polarization.** Write
   \(O(t)=q_1(t)+tq_2(t)/(2r)\). The scalar variation in the cited convention
   has the protected null row, so
   \(\mathcal Qq_1=-t\mathcal Qq_2/(2r)\).
   Dilation differentiates the fields at the specified insertion. Thus
   \([D,O]=(t\partial_t+1/2)O-tq_2/(2r)\).
   Differentiating the closed family gives zero under \(\mathcal Q\), while
   the last term gives the non-closure witness. The other scalar's variation
   is a nonzero free-fermion combination; the Poincare part already acts
   nontrivially at the center. Small generic nonzero interior \(t\) suffices.
   No inference from a nonzero generator commutator alone is needed.

2. **Centered frame.** With
   \(x=t/(2r)=\tan((\varphi-\pi/2)/2)\), elementary half-angle identities give
   \((\cos(\varphi/2),\sin(\varphi/2))/\sqrt{\Omega}
   =((1-x),(1+x))/\sqrt2\), where \(\Omega=(1+x^2)^{-1}\).
   The constant H-basis rotation recovers the affine family above. The scalar
   Weyl weight \(1/2\) and the source's twist therefore support the centered
   witness, without moving the hemisphere's radial origin to its endpoint.
   This is a passive change of frame, not new Dirichlet data.

3. **Hodge qualification.** In the source normalization,
   \(\{\mathcal Q_i^H,(\mathcal Q_i^H)^\dagger\}=8(D-R_H)\).
   Consequently the common kernel is annihilated by both individual charges
   and their adjoints. In the free joint number basis \(D\) commutes with its
   spectral projection. Its restriction is generally nonzero: it equals
   \(R_H\) there. The exact compensated dilation being trivial on classes does
   not make this physical Hamiltonian zero.

4. **One-particle loss and composites.** For a highest-H scalar,
   \(D=\ell+1/2,\ R_H=1/2\), so \(D-R_H=\ell\). The retained modes have
   \(\ell=0\). Products of the two independent retained scalar creators give
   energies \((m+n)/2\) with ordinary norms \(m!n!\). A trace over those
   monomials is not an endpoint matrix element.

5. **Boundary and adjoint scope.** The original boundary auxiliary condition
   remains curvature dependent, and the original Mellin coordinate is field
   magnitude. A creation operator in the new physical Fock construction has
   an ordinary annihilation adjoint. These are not identified with the
   left/right tilded boundary operators in the localized Weyl algebra.

The individual-charge Hodge theorem is sufficient for these checks. We have
not proved a new Hodge theorem for the sum charge on arbitrary extended
operators, nor a physical radial isometry of all localized wavefunctions.
The historical statements should retain these qualifications in any future
manuscript revision.

## Audit of the new candidate

The new [research note](../notes/GAUSSIAN_PAIR_INTERFACE_ENDPOINT_RESPONSE_20260920.md)
specifies the boundary state as the ground state of a stable, neutral
quadratic Hamiltonian. Bogoliubov diagonalization derives its boundary
conditions and coefficients; the ordinary charged endpoint supplies the
factor \(k+1\) in its weights. In particular:

- The preparation Hamiltonian and the subsequent propagation Hamiltonian
  are different and stated explicitly.
- The modes are spatially smeared and frequency polarized. This is an
  admissible nonlocal mode coupling, not evidence for a local BPS interface.
- The flavor-one constraint follows from the endpoint and neutral coupling.
  Even pair number and removal of the lowest state do not follow. Their
  additional projection is used only to strengthen the negative comparison.
- Unit-norm preparations have finite response at zero. The unnormalized
  gap-closing limit is defined with a heat regulator and has the wrong
  short-distance order.
- The result is a scalar spectral matrix element. No arbitrary-input
  response map, causal arithmetic transfer, signed pole contribution, or
  prescribed finite part is obtained from it.

The new numerical program independently propagates a seeded state by the
tridiagonal quadratic generator, rather than using the closed-form weights
inside that integrator. Its finite arithmetic checks and floating diagnostics
are separate from the infinite analytical argument. It does not establish
supersymmetry transformations, boundary locality, or an arithmetic certificate.

## Reproduction and review status

The inherited 83-case radial-descent program and the Hodge-channel program
passed and reproduced their saved records. The new program passed its exact
rational identities, factorial weights, finite ODE comparisons and regulator
checks. Numerical details are in its
[small record](../numerics/records/gaussian-pair-endpoint-checks-20260920.json).
Preservation and source hashes are in the
[provenance record](../numerics/records/gaussian-pair-endpoint-provenance-20260920.json).

This audit supports proceeding with the bounded calculation in its stated
scope. It supplies no independent specialist endorsement. In particular,
promoting the mode interface to a local supersymmetric boundary construction
would require new physical input and review; no such promotion is made.

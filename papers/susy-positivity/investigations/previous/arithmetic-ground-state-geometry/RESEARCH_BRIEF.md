# Research brief: arithmetic ground-state geometry

## Objective

Construct a positive physical Hilbert theory, a specified ground state or vacuum sector, and a linear source map whose ordinary norm is the complete Weil quadratic form on every required compactly supported complex input. The sign should follow from the theory. Numerical bounds are checks of derived identities, not the principal mechanism.

## Starting point

For finite prime set \(S\), define
\[
\Lambda_S(z)=\pi^{-z/2}\Gamma(z/2)\prod_{p\in S}(1-p^{-z})^{-1}.
\]
The preceding survey constructs a positive supersymmetric Morse system and discrete prime sectors with
\[
\|\Psi_\sigma\|^2=\Lambda_S(\sigma),\qquad
\langle\Psi_\sigma,e^{i\tau X}\Psi_\sigma\rangle=\Lambda_S(\sigma+i\tau).
\]
The normal logarithmic derivative of the squared amplitude at \(\sigma=1/2\) reproduces the pole-free arithmetic multiplier. Normalizing at \(\tau=0\) gives the positive gamma-plus-prime jump energy. Restoring the target requires a negative contact subtraction and the signed pole form.

The chosen complex ground-state extension has metric \(\Lambda_S(\Re z)\), with nonzero variance curvature. It cannot remain an ordinary rank-one chiral \(tt^*\) vacuum bundle. The fixed Hamiltonian also has a positive-energy multiplicity incompatible with four standard real supercharges. These restrictions require a real change of theory, rather than a new name for the original supersymmetry.

## First construction questions

1. Can a specified Kähler, Landau–Ginzburg or gauged model enlarge the physical theory while preserving useful arithmetic data? State the supercharges, adjoints, domains and parameter multiplets.
2. Does a non-Abelian vacuum bundle genuinely evade the line-metric obstruction? Distinguish the norm of a section from the determinant and full metric, and derive the relevant curvature identities.
3. Can a ground-state transform, relative constraint or coherent boundary observable account for the prescribed contact and poles as part of one positive pairing?
4. If the arithmetic parameters are vector-multiplet data, what does Bogomolny geometry actually constrain, and does it fix the first derivative needed by the arithmetic form?

## Selection rules

Keep arithmetic Fourier variables distinct from physical time or coupling coordinates unless their identification is derived. A finite vacuum fiber alone cannot carry all input directions. An all-repetition one-prime amplitude is a legitimate control, but the complete finite-interval Weil form must include every prime active on that interval; fixed finitely many primes cannot support its full signed poles at arbitrarily large lengths.

A successful extension must add a new identity or an independently fixed physical structure, such as source normalization, pole accounting, or a full arithmetic norm. An index, determinant, scattering phase, fitted metric, or positive Hamiltonian alone does not establish that identity. Gaussian and interacting models are both admitted; the response representation and observable, rather than a complexity label, determine which earlier exclusions apply.

See the [preceding report](../../../brainstorm/theory-landscape-20260913/REPORT.md) and its [extension tests](../../../brainstorm/theory-landscape-20260913/EXTENDED_SUSY_TEST.md) for the inherited derivations and primary sources.

## First continuation outcome

The [research report](REPORT.md) now gives explicit four-supercharge and interacting constructions, together with the restrictions that survived them. The [next investigation](CONTINUATION.md) uses the exact interacting Euler metric as a control while seeking a nontrivial interaction parameter and a physically specified pairing. The original selection rules above remain in force.

## Current continuation: a finite-rank remainder

The review and derivations in [notes 18–19](notes/19_JOINT_RESPONSE_AND_FINITE_RANK_DEFECT.md) replace the preceding infinite-rank compact error by a finite-rank positive error. A Neumann lower comparison selects ordinary cosine modes; joint gamma-and-prime responses make the high-sector gluing exact and retain every low/high cross term. The remaining condition is an explicit finite matrix \(G-D_N\ge0\), not a proved sign.

The immediate objective is now a structural arithmetic bound or independently derived positive gluing for that matrix, together with its behavior under support enlargement. Compatibility is established only within one fixed envelope. The completion itself is a general operator construction; its existence and the unit quartic tensor label do not explain arithmetic positivity.

## Integrated manuscript

The [current manuscript](manuscript.pdf) incorporates all results through note 19. The [coverage map](MANUSCRIPT_COVERAGE.md) records where the new statements, proofs and limitations appear. Complete dated PDF and TeX snapshots are saved in [archive/drafts](archive/drafts/README.md). The remaining objective is the finite arithmetic matrix comparison and its behavior under enlargement of support.

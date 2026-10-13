# Initial research program for canonical boundary reflection

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: `gpt-6.1-sol`; reasoning effort: ultra.
Status: initialized, awaiting Claude review. No canonical-system replay or
new positivity assertion is reported by this note.

This project develops [brainstorm card 12](../../../inactive/brainstorm/LIFTED_THETA_SYMMETRY_SEARCH_CODEX_20261013.md#12-canonical-systems-and-arithmetic-boundary-reflection).
The intended gain is an arithmetic boundary pairing whose positivity
constrains the actual value-and-slope observation, with independently
verified source and endpoint contracts.

## Actual source and the operator contract

Let \(\Phi_e\) be the complete even theta kernel obtained from
\[
\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})
e^{-\pi n^2e^{4u}},\qquad u\ge0.
\]
Use \(m_t=e^{tu^2}\Phi_e\), \(\mathscr Gm=u^2m\), and
\(\mathcal P_xm=\frac12\int e^{ixu}m(u)du=H_t(x)\). Its derivative
projection gives \(H_x\), and \(\partial_tH=-\partial_x^2H\).
All required finite jets converge on complex spatial compact sets and
compact real time intervals. At time zero,
\(H_0(x)=\xi(1/2+ix/2)/8\).

A canonical system uses a separate interval coordinate \(a\), spectral
coordinate \(z\), and positive semidefinite Hamiltonian \(\mathcal H(a)\):
\(\partial_aY=zJ\mathcal H(a)Y\), with the sign and endpoint convention
specified from its source. Neither \(a\) nor an imaginary spectral shift
is Newman time. A proposed theta transfer map must preserve this distinction
and pay any moving-projection derivative.

## Established seed and objective

[Suzuki, Proposition 1.2, Theorem 2.3 and section 5](https://arxiv.org/pdf/1204.1827v2)
constructs a canonical system through arithmetic kernels and Fredholm
determinants for the quotient
\[
\Theta_\omega(z)=
\frac{\xi(1/2-\omega-iz)}{\xi(1/2+\omega-iz)}.
\]
The explicit unconditional construction has \(\omega>1\). Inner-function
conditions in smaller ranges are substantive hypotheses; extending the
construction to every positive shift has RH-strength content. The xi
normalization maps its denominator exactly to \(8H_0(2z+2i\omega)\),
using the functional equation. This is a source-normalization identity,
not a positive-time heat intertwiner.

The objective is an independently derived arithmetic source/transfer map
placing \((H_t,H_x)\), or a provably equivalent pair, in homogeneous Cauchy
data for a valid positive system. An alternative is a regular source
identity \(Q=aH+bH_x+r\) with \(Q\ne0\) independently established and
\(|r|<|Q|\). Either requires the complete theta observation and all source
residuals. No such map is currently established.

## First bounded task and verification

Begin in the unconditional regime, for example one fixed \(\omega>1\).
Write the exact kernel, coefficient source, Fredholm interval, determinant
ratio, canonical pair, and endpoint conditions. Match their normalization
to the repository's complete-xi
[Gaussian-Hermite readout](../../../../quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/21_COMPLETE_THETA_GAUSSIAN_HERMITE_READOUT_20261011.md).
Identify what is actually controlled before selecting a compact comparison
experiment.

For any proposed extension to \(t>0\), calculate the generator and projection
compatibility defect explicitly. Separate independently proved Hamiltonian
positivity from invertibility, kernel regularity, denominator nonvanishing,
and truncation payment. Cross-check the spectral factor two, conjugation,
the canonical-system sign, and whether the observation is homogeneous
boundary data or a forced response.

Continue when the comparison identifies a new source identity or a precise
estimate capable of extending its verified domain. Stop if positivity is
obtained only by assuming unknown innerness, real-zero factorization, or
nonvanishing of the target function. A safe-shift canonical system alone
does not establish an RH implication.

The [boundary scout](../../../../quasi-rh-exponent-descent/newman_collisions/11_boundary_extensions/reviews/1_SCOUT_INTERNAL_REVIEW_20261010.md)
already excludes the specified exact passive scalar-resolvent realization:
an observed pole survives. Numerators and independently derived homogeneous
boundary pairs remain different possibilities, but boundary uniqueness
cannot be applied to an unpaid forced source. A construction using
\(H_x/H\) also introduces the unknown collision denominator rather than
resolving it.

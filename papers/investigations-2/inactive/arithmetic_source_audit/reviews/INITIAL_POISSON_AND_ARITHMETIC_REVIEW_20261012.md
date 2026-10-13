# Initial Poisson reduction and arithmetic conversion review

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration. Exact serving variant and
configured reasoning effort are not exposed and are not inferred. Parallel
model checks are internal scrutiny, not independent specialist validation
or formal verification.

## Result and scope

The initial Poisson reduction and its arithmetic conversion identities
pass this scoped internal audit under the classical imports identified
below. No unresolved defect was established in the diagonal, shared column
factors, zero-extension masks, fixed coefficient family, smooth norms,
or initial dual ranges. The reduction is an implication from the auxiliary
energy estimate; it does not independently prove that estimate or the
manuscript's zero-free theorem.

This continues the two audits recorded in [chat 1](../chat-histories/README.md).
The [theta review](THETA_TRANSFORMATION_REVIEW_20261012.md) identified this
initial reduction as the next bounded source target. The new derivations
are [the arithmetic conversion audit](../notes/INITIAL_ARITHMETIC_CONVERSION_AUDIT_20261012.md)
and [the complete initial Poisson ledger](../notes/INITIAL_POISSON_REDUCTION_AUDIT_20261012.md).
The research continues on the same pinned October 5 manuscript, rather
than silently switching to a later revision.

The [source](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex)
is at revision `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`, with verified
SHA-256 `d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`.
The manuscript date is 5 October; the revision is dated 8 October.
The original [provenance record](../notes/source_provenance_20261012.json)
remains unchanged. Third-party source files remain outside the repository.

| Source component | Physical lines | Finding |
| --- | --- | --- |
| Arithmetic identities and Appendix A.1 | 823–862, 2689–2872 | Jacobi sign, Gauss conversions, quadratic phase, finite reciprocity classes, and fixed ray expansion are consistent |
| Primitive Poisson with exclusions | 875–932 | Conductor, divisor normalization, and principal zero frequency are retained |
| Exclusion removal | 962–991 | Character zeros preserve squarefreeness and the scale product |
| Full initial reduction | 1000–1255 | Shared factors, exact reindexing, coupled kernels, and dyadic costs close |
| Initial positive gap and small ranges | 1613–1629 | Canonical hypotheses hold for large D; short and empty ranges are handled by counting |
| Row-dependent smooth kernels | 3566–3618 | A common pointwise Mellin majorant gives the stated finite derivative cost |

## What closes the reduction

The initial mixed character has conductor exactly \(z_1z_2\), because
the residual squarefree columns are coprime and every local sextic
character is nontrivial. Its principal case is exactly \(z_1=z_2=1\).
The zero frequency gives the stated diagonal using only ideal counting,
and the nonzero frequencies of that case remain in the identity.

The paired Gauss conversion retains the CRT reciprocity sign. With
\(t=z_1z_2^{-1}\) in the fixed ray group, its remaining factor is
\(\overline{\nu(t)}G(t^{-1})\). Character expansion of this fixed
function produces the same \(a_\xi\) profile on both columns. Neither
a moving prime nor a new arbitrary coefficient profile is absorbed into
the fixed ray data. The quadratic Gaussian calculation has the correct
factor \(1/2\); the cubic Jacobi evaluation also covers inert primes.

Möbius inversion removes the residual column coprimality only after this
conversion. Extending the explicit coefficient expression off the coprime
locus is legitimate because the exact coprimality indicator is inserted
before the inversion. No identity for a nonprimitive mixed Gauss sum is
used on the newly introduced noncoprime pairs.

The common-column mask \((v,h)=1\) makes the variable change reversible:

\[
b=g/e,\qquad f=ev,\qquad k=eh,
\qquad e=\gcd(f,k).
\]

There is no requirement \((e,h)=1\). The fourth power of the
zero-extended character retains the column exclusion at every prime of
\(f\); only the exclusion at \(b\) remains explicit. Removing it
changes \((X,F)\) to \((X/N(d),FN(d))\), preserving \(XF=D/B\)
and the initial row range.

A nonnegative Schwartz majorant with compact Fourier support supplies an
exact dual cutoff. The row-dependent kernel is controlled through the
common Mellin majorant, with derivative order \(2J+4\), rather than
by allowing a different unbounded test function in every row. Divisor
counts cost an arbitrarily small power of \(D\), and the shared-factor
normalization closes as

\[
\frac H{D^2}\,O(B^2)\left(\frac DB\right)^2=O(H).
\]

Finally, \(\mathcal H/(XF)\le C D^{-\vartheta}/B\). For sufficiently
large \(D\), this permits \(\kappa=\vartheta/2\). If a divisor shift
makes \(X<1\), nonempty fixed support keeps \(X\) bounded away from
zero and direct counting supplies the required estimate. If
\(\mathcal H<1\), there are no nonzero element rows.

## Finite verification and its limits

The new [standalone checker](../numerics/check_initial_arithmetic.py)
and [small run record](../numerics/initial_arithmetic_record_20261012.json)
pass 113,748 exact assertions and 19,868 ordinary floating comparisons.
The exact assertions are individual checks inside finite enumerations;
they are not a count of independent mathematical lemmas.

The exact coverage includes 4,374 bijection inputs using actual Euclidean
gcds in the Eisenstein ring, all twelve primary residue classes modulo
12, the square subgroup modulo 4, eight cubic Jacobi sums, and the
zero-extension masks. Six split and two inert primes supply direct finite
Gauss sums; 28 distinct prime pairs test the paired CRT conversion with
the original twist set to one. Arbitrary fixed Hecke twists are covered
by the algebraic ray-character argument, not by those prime-pair tests.

All twelve negative-control families detect an altered identity. They
expose omitted Möbius signs, missing masks or coprimality restrictions,
and an incorrect conjugation of the paired ray factor. The maximum
observed absolute floating error is about \(4.092\times10^{-15}\), below
the chosen \(10^{-10}\) tolerance. These are ordinary floating diagnostics
without interval error bounds. They do not certify analytic Poisson,
smoothing, asymptotic estimates, or unbounded reciprocity laws.

A supplied source file must match the pinned hash before the checker
performs computations or writes output. Without a source file it runs
standalone and explicitly records that source verification was not
performed. The record includes the script hash and Python version.
Replays and limitations are documented in [the numerics guide](../numerics/README.md#initial-arithmetic-and-poisson-bookkeeping).

## Remaining obligation and next target

The arithmetic argument uses classical lattice Poisson, primitive and
inverse-character Gauss identities, Gauss–Jacobi identities, cubic
reciprocity for primary Eisenstein integers, and finite-group character
orthogonality. Their use is checked here; their full classical proofs
remain imports. The Appendix's special Jacobi sign, quadratic phase
normalization, ray quotient, and all mask-preserving changes of variables
are derived in the new notes.

The next bounded target is a complete uniform ledger for the completed
mean-square estimate, `prop:R`, using the now inspected theta
transformation. Reconcile every active and inactive local term, the
exceptional exponent-four collision branches, the ramified cusp terms,
the squarefree-row coefficient norms and quadratic-sieve hypotheses,
and the passage to general rows. The earlier [first branch review](FIRST_BRANCH_REVIEW_20261012.md)
checks the composition conditional on its inputs; it does not replace
that full ledger. The classical theta and quadratic large-sieve theorems
remain imports unless their original proofs are separately audited.

Beyond that target, the two-Poisson transfer still needs coverage outside
the selected nonempty branch before promoting the whole canonical
estimate. No new exponent, zero-free region, or RH implication is
established by this continuation.

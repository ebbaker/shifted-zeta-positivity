# Bounded research results and Dirac continuation

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: `gpt-6.1-sol` (Codex), reasoning effort **ultra**.
Internal assessment with parallel LLM derivations and cross checks;
this is not independent specialist review or a literature novelty finding.

Investigation 20 now has a useful certified quantum bound, a corrected
operator smoothing theorem, two precise obstructions to local constrained
square constructions, and stationary theta/control validation for both
physical derivative levels. These complete a bounded first pass through
the [initial program](../notes/INITIAL_RESEARCH_PROGRAM_20261014.md).
The program's theta positivity gate remains open. The Dirac continuation
has produced exclusion theorems and a quantified control payment, rather
than a source-specific theta factorization.

## Quantum result and cost decision

The [Hubbard benchmark](../notes/HUBBARD_HEAT_RESIDUAL_BENCHMARK_20261014.md)
uses hopping 1 and repulsion 4 in the fixed \(N_\uparrow=N_\downarrow=1\)
sector. The same Slater initial family, one-body heat surrogate, energy
shift 3 and terminal time 6 supply every comparison. Analytic spectral
integration replaces time quadrature for every method equally.

The exact ground energy is \(2-2\sqrt2=-0.828427\ldots\).
An uncorrected quotient near \(-1.999926\) is below that energy and its
actual integrated state's energy is zero. A localized initial determinant
instead gives a correlated integrated state with certified Rayleigh
energy \(-0.50746185323775\ldots\), and a positive-interaction residual
upper enclosure \(-0.50215397612677\ldots\). The latter is strictly
below \(-1/2\), the analytically proved global minimum for the stated
fixed-spin product Slater class. This is a concrete variational consequence
beyond an algebra check.

The bound requires \(A=B+V\), \(B\ge\beta>0\), \(V\ge0\), and
\(V^2\ge\nu V\) for a known \(\nu>0\). The surrogate path obeys
\(u'=-Bu\), so \(\int r=V\Psi\). These hypotheses are explicit and
hold in the benchmark; they cannot be assumed for a general signed or
gapless continuum interaction. The previous generic Cauchy bounds have
negative denominator on the rigorously checked selected states.

The matched comparison is decisive in this representation. Direct
Rayleigh evaluation costs less than residual accumulation over the same
169 candidates; at the residual method's counted arithmetic budget it
can test 225 candidates. The work metric is recorded, including overlaps,
operator actions and separately counted square roots. It excludes a
claim about machine timings, proof-generation cost, scalability or a
globally optimized grid minimum. Stop the claim of a computational
advantage for this compact-state implementation. Continue only with a
representation in which residual estimates are materially cheaper than
direct energy/norm overlaps, or with a sharper theorem having a distinct
application. The integrated correlated trial family and its certified
bound remain valid regardless of this cost limitation. The
[quantum audit](HUBBARD_BENCHMARK_AUDIT_20261014.md) replayed the final
certificate and confirmed corrected identity and budget accounting.

## Corrected smoothing gate

The [Gaussian channel derivation](../notes/GAUSSIAN_TRANSLATION_DEFECTS_AND_NORMAL_ORDERING_20261014.md)
proves the exact operator product defect and identifies its equality
case: only translation-invariant observables lie in the multiplicative
domain. A similarity cannot implement heat smoothing on nonconstant
multiplication observables and their products.

Independent density-factor smoothing yields the positive pair kernel
with its self contraction retained. Common translation leaves the
already integrated pair interaction invariant. The exact four-site CAR
example distinguishes these operations: the normal-ordered contact
square is zero, while independently smoothed two-particle pair values
are \(9/32\) or \(15/32\). Normal ordering can make an otherwise
positive covariance negative. The finite-spin trace obstruction survives
all constant time rescalings; Gaussian averaging of first-order
propagators is the valid replacement.

All 21 finite algebra checks pass. The continuum statements have their
own bounded-observable and fixed-particle domain proofs. This completes
the corrected reconstruction requested by the initial program and
excludes the original single-similarity/common-trace implementation.

## Dirac square obstructions for both stationary constraints

The [local multiplier theorem](../notes/LOCAL_MULTIPLIER_AND_FINITE_OBSERVATION_OBSTRUCTIONS_20261014.md)
declares its exact operator class before testing it. For any nonzero
frequency, the complete paired Laguerre multiplier has a negative
rectangle where both linear stationary multiplier factors vanish at
the central nodes. Any locally bounded source-derived multiplier leaves
a negative form on a smooth compact-support vector. This excludes a
positive operator identity on that full paired core for both \(j=0\)
and \(j=1\), even when the Hilbert measure is genuine theta.

The conclusion concerns full-core identities. It does not exclude a
nonlocal or state-restricted identity using an arithmetic constraint.
A gluing defect whose expectation vanishes only on the actual theta
state remains an operator term on the core. This is the essential escape
that a further construction must make explicit.

The same note constructs positive even smooth controls with all tails
and any declared finite set of linear integral observations and local
source jets preserved exactly. On one source, it can make both physical
stationary signs strictly negative at separate remote frequencies.
The positive scalar Volterra correction of 02 also survives. Finitely
many such observations cannot replace the full imaginary Jacobi law
over the unrestricted smooth source class. The construction is an
existence theorem without an effective remote-frequency threshold;
it does not assert that arbitrary angular gluing evaluations are
linear observations of that class.

## Certified stationary energy validation

The [stationary certificate](../notes/2_CERTIFIED_STATIONARY_THETA_AND_EULER_CONTROLS_20261014.md)
pays the entire theta-index, infinite-source, shift, and parameter
Taylor remainders. Throughout \(0.199999\le t\le0.200001\), it proves
unique differentiable stationary curves in three declared compact
spatial boxes. Theta has a positive \(\mathscr L_0\) margin near
\(x=31.05754\) and a positive \(\mathscr L_1\) margin near
\(x=9.48225\). The Euler control has
\(\mathscr L_0<-5.254\cdot10^{-6}\) on an actual \(H_x=0\)
curve near \(x=1.684136\).

Thus a proposed constrained square applicable to that control must pay
at least that negative amount in its combined defect/remainder, or
identify a violated hypothesis. A merely positive Dirac square or source
Hamiltonian cannot pass this screen. Positive local theta signs validate
the readout, rather than implying a global factorization.

A separate parallel audit replayed the certificate and checked the
rounded table against exact dyadic endpoints. Its result is retained in the
[stationary audit](STATIONARY_CERTIFICATE_AUDIT_20261014.md). This is an internal check by the same recorded model, not external
expert validation.

## Remaining constructive gate

The next theta task is a **nonlocal identity on an explicitly restricted
arithmetic state**, using the complete imaginary elliptic recurrence and
its transported physical insertion. It must retain all cross sectors,
endpoint and tail payments, reduce to the physical stationary target,
and quantitatively dominate the negative part. The local spectral
multiplication class and finite linear source-observation substitutes
are now excluded. A positive generator, its instantaneous ground state,
or a discarded cosine multiplier would not meet the gate.

The stationary-energy identity continues to define the desired local
observable. No transfer theorem from the quantum application, all-height
coverage, all-time sign, continuation through every multiplicity, or RH
conclusion follows from these bounded results. No manuscript endpoint
is selected yet; the quantum consequence and the rigorous operator-class
obstructions merit further literature comparison before a novelty claim.

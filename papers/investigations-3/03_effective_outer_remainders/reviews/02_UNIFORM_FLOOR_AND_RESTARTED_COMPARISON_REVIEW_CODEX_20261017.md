# Review of the uniform floor and restarted comparison

17 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6-astra (Codex)**; reasoning effort: **ultra**.
Review type: **internal same-model review and cross-agent checks**. The
lead reviewer also integrated the research. One agent checked the floor
proof and evaluator without authoring them; a different agent checked
the restarted comparison without authoring it. This is not cross-model
review of round two or independent specialist validation.

## Disposition

**The next research gate is complete at the proved-in-note level.** No
blocking defect was found after the cutoff assertion identified below
was added. The complete result is

\[
 q\ge10^{12},\quad \chi\text{ primitive}
 \quad\Longrightarrow\quad
 S_\chi(x,3,t)>6\ (x\in\mathbb R,\ 0\le t\le1/4),
 \qquad \Lambda_\chi\le43/200=0.215.
\]

[Note 01](../notes/round-2/01_UNIFORM_FAMILY_FLOOR_CODEX_20261017.md)
proves the envelope domination and supplies an Arb certificate of its
scalar evaluation. [Note 02](../notes/round-2/02_RESTARTED_STRIP_COMPARISON_CODEX_20261017.md)
proves the transfer through finitely many original time slices and
supplies exact rational scalar gates. Both use named analytic inputs.
Specialist review remains the next review gate.

This conclusion concerns the named large-conductor family regime.
The original lower-conductor zero-loss thresholds, derivative-circle
bounds, and zeta value \(0.18891\) do not acquire stronger status.
In particular, the latter remains conditional on the external global
analytic estimates identified in [Review 01](01_ROUND_ONE_CROSS_MODEL_REVIEW_CODEX_20261017.md).

## 1. Corrections and source identity

The current manuscript now restricts real saddle uniqueness to
\([\sigma_0,\infty)\), labels the old numerical thresholds as sampled
rather than uniform, and points to Project 01's round-three sine-tail
comparison. Its new final section summarizes the certified regime and
links the full notes. Historical round-one notes and numerical records
were retained unchanged; the review and current manuscript identify their
corrections.

The [validation record](../numerics/round-2/ROUND_TWO_VALIDATION_CODEX_20261017.json)
identifies the filed notes, programs and execution records by SHA-256.
The manuscript [build record](../manuscript/BUILD_RECORD.json) separately
identifies the revised source and PDF. These hashes establish identity,
not mathematical correctness.

One substantive completeness edit arose during this round's checks:
the tail proof used
\(\pi e^{7/12}+e^{-129/5}<e^2\), to justify
\(\log\lceil\mathcal Q/2\rceil\le\ell+2\). The first evaluator omitted
that explicit assertion. It has now been added and passes with margin
greater than \(1.7593\). No numerical parameter was weakened to make
this correction pass.

## 2. Uniform envelope audit

The lead reviewer and a separate agent checked the following analytic
points against the evaluator.

- The moving cutoff is \(a=(\sigma+1)/2\), \(V=(\sigma-1)/2\).
  All central Taylor segments have real part at least \(a>1\).
  Full-line Gaussian second-moment envelopes bound both remainder and
  denominator errors, with the correct variance and Gamma derivative
  normalization. The power-series extraction gives
  \(A_1=\psi'/4\) and \(A_2=-\psi''/8\).
- Each of the 1,000 rational time cells bounds its whole interval.
  Positive derivative majorants decrease with \(\ell\); the boundary
  payment uses both the checked decreasing-in-\(V\) condition and
  \(V^2>h\). The ordinary Gaussian tails and pure tilt have the required
  monotonicity. Thus the first cell covers all positive times down to
  zero, and no sampled monotonicity assumption remains.
- In the critical strip, reintegration of the polygamma bound gives the
  stated Gamma remainder. The full polynomial prefactor, including the
  numerator weight, has logarithmic derivative at most \(3/\ell\),
  while the exponent derivative is at most \(-1/4\). This proves the
  reduction over the unbounded \(\ell\)-range. Reserving one quarter of
  the inverse-time term gives the exact AM–GM constants in the program.
- At the same reflected real part \(u\), the ratio of reflected to
  ordinary critical majorant densities is exactly
  \(e^{-3(2u-1)/(2h)}\le1\). The common numerator weight bounds both
  pieces. The factor two in the combined critical bound is justified.
- The far-reflection square completes to
  \(e^{-3\ell/2}\exp(-(w+3)^2/(2h)+bw^2/2)\).
  Its tilted mean, variance and mass agree with the program. The three
  numerator cases are exhaustive. In the small-time, small-\(h\ell\)
  case, retaining the actual cutoff \(x\ge7/4\) before integration
  removes the spurious whole-line divergence. The height proxy is never
  used beyond its proved real-part domain.
- The denominator and all positive numerator payments are substituted
  in the safe direction in Proposition 4.5. The final conductor lower
  bound and parity domination apply at every real height. The exact
  time-zero floor covers the omitted endpoint.

No remaining quadrature tail, between-grid interpolation, large-height
extension or small-time remainder is being left to a numerical guess
in this regime. The new envelope does not prove that the original,
tighter remainder itself decreases in every parameter; it supplies a
separate monotone upper envelope sufficient for the chosen consumer.

## 3. Restarted comparison audit

The key addition to Project 01 is an intermediate-strip transfer that
can be restarted. A single invocation of its initial-floor theorem would
not consume the full positive-time arithmetic floor.

At each original time slice, canonical truncation plus a real sine tail
preserves the initial strip and any slightly reduced global floor.
The central error is a reciprocal-square tail; outside that region the
remaining sine lattice supplies the floor. For each fixed approximant,
its rational-times-sine asymptotic proves eventual reality uniformly on
the short time interval. It supplies compact first contact for that
approximant; no uniform truncation radius or confinement theorem for the
original character flow is assumed.

The Burgers signs and constants give the weaker floor
\(m_C(s)=Ce^{-s/2}/[1+2C(1-e^{-s/2})]\).
The characteristic field has at most linear growth, so the characteristics
are complete. At positive-height first contact, the own conjugate pair
is removed with the required correction \(8Q/(9-Q)\), and the ordinary
paired-kernel condition \(9\ge5Q\) holds. Multiple contact is excluded
by the local backward Hermite splitting, whose \(\sqrt v\) displacement
beats the smooth barrier's \(O(v)\) displacement. Reaching zero height
is handled by a limiting strip argument and preservation of real zeros.

The canonical products have a common sub-Gaussian bound, so Gaussian
heat evolution converges locally uniformly. The inverse Gaussian identity
ensures a nonzero limit; Hurwitz transfers the strip. Every original
restart slice retains order at most one, reality, and the heat semigroup
identity. The original floor six is refreshed at every step; it is never
assigned directly to the approximating flows at positive times.

The named general strip input is
[Cardon, Theorem 1.5 and Lemma 1.3](https://arxiv.org/html/1401.0237v2).
Its statement and hypotheses were checked for real genus-one functions
with zero quadratic exponential coefficient. Its full published proof
was not reconstructed. The Fourier-only strip theorem would not suffice
for the rational-sine approximants.

## 4. Replays and quantitative conclusion

The final evaluator was run with python-flint 0.9.0 at 128 bits.
All inequality decisions use Arb balls and fail on uncertain signs.
The exact consumer program uses rational fractions, with floating values
confined to display fields. It also fails closed under optimized Python.

| Gate | Result |
| --- | --- |
| All \(\ell\ge129/5\), all \(0<h\le1/8\) | \(E<1/5\), \(d_0>93/100\) |
| Computed envelope extrema, rounded outward | \(E<0.192767\), \(d_0>0.931777\) |
| Primitive \(q\ge10^{12}\), both parities | \(S_\chi>1213/200=6.065>6\) |
| Step floor, \(\delta=1/10000\) | \(m_6(\delta)>1499/250\), exact margin \(>1.3150\cdot10^{-6}\) after exponential conversion |
| 2,150 steps, \(T=43/200\) | Terminal exponential gate margin \(>0.00165849\); strip reaches zero |

An agent separately replayed the pre-integration floor evaluator
byte-identically. The filed version adds provenance and the explicit
cutoff assertion; the lead replayed that version. Mathematical decisions
are made from the calculated bounds, never from output hashes.

## 5. Scope and next review

This is a quantitative sufficient result, with a specific improved family
bound, rather than a reformulation of GRH. The arithmetic premise screen
in Note 01 addresses the [documented collision controls](../../../../result-summaries/12_collision_controls_and_screening.md).
It does not rest on positivity or symmetry alone and makes no
literature-wide novelty claim.

The next review should independently check the majorization and the
restarted intermediate-strip lemma. Only after that review should this
be treated as an accepted manuscript milestone. Extending to smaller
conductors, certifying the derivative-circle consumer, and auditing the
external zeta analytic estimates remain separate tasks.

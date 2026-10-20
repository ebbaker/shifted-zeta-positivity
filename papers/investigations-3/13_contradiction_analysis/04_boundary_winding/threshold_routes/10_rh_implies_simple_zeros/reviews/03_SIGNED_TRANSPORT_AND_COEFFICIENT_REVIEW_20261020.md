# Review of signed transport and effective Euler-control rejection

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), reasoning effort ultra**,
verified from recorded session metadata. The parent and two separate
same-model agents checked the selected arguments. This is internal
review, not independent specialist review.

**Verdict:** [Note 03][note] proves exact transport identities, a scoped
failure of the declared global-error estimate, and effective rejection
of the finite Euler-polynomial control class. It does not prove
RH ⇒ simplicity or exclude any multiple theta zero.

## Checked argument and corrections

1. **Transport and cancellation.** Checked the normalization
   \(V=2\pi\Delta\), the lower endpoint \(E(1)=-1\), all kernel signs,
   and both pole terms. The exponential parts cancel before estimation.
   The remainder bound in (8) follows with the displayed constants.
2. **Quantitative estimating loss.** Integrated the polynomial weight
   exactly to obtain \(A(V)\) and \(B(V)\). The payment has leading
   constant \(\pi c^2/12\) at \(\Delta=c\log\gamma\).
   Bounded-primitive averaging gives the envelope-only operator norm
   \(\gamma V^2/(24\pi^2)\). This norm is over arbitrary functions with
   the stated envelope, not over Chebyshev functions of actual primes.
3. **Resonant mode.** Differentiating the single zero-pair contribution
   directly gives \(-m[1+\operatorname{sinc}^2(V\gamma)]\). Its small
   amplitude in the prime-counting error is compatible with the global
   envelope. No termwise absolute summation of the infinite zero
   formula is used.
4. **Actual control and identical input.** The first staging bound
   \(4\log p\sqrt x\) was valid but unnecessarily weak. The alternating
   geometric sum gives \(2\log p\sqrt x\). For \(p\ge101\), the checked
   Lee–Nosal bound proves that the control satisfies the *identical*
   envelope \(W\), including constants, globally. This repairs a scope
   gap in the first staging claim, which had only established the same
   big-O and eventual leading-constant classes. The completion's
   conductor term \(2\log p/V\) remains in the comparison.
5. **Finite Euler rigidity.** Independently checked the sign in (18),
   conjugation reality, the \(12^d\) pigeonhole argument and the margin
   in (19). The witness interval \([N,12^dN]\) follows by applying the
   same argument to \(N\theta\). No RH is needed for this proposition.
   The missing implication from an original multiple zero to such a
   factor is explicitly retained.
6. **Benchmarks and dynamics.** The power control has the stated
   changes in degree, pole order and coefficients. The weak-Mertens
   Laplace argument is valid but uses an extra unproved assumption.
   The gap equation is compatible with an endpoint double event and
   supplies no opposing sign. Its remainder is stated as \(o(t^2)\),
   which follows from \(P\to S\), without importing a derivative
   estimate. No heat-time derivative of the large-time spatial
   asymptotic is assumed.
7. **Isolated endpoint control.** The Fourier multiplier in (20),
   derivative-tail bounds and source floor \(\Phi_A\ge\Phi/4\) were
   checked separately by the parent and both reviewing agents.
   Under RH the chosen added roots are exact doubles; preservation
   and local splitting give threshold zero and simple positive-time
   slices. The displayed gamma factor, conductor and pole order
   persist, while the pole residue changes as stated. Polynomial
   growth in the right half-plane and a negative logarithmic
   derivative there identify its arithmetic failures explicitly.
   It does not screen the full unchanged zeta premises.

## Primary-source checks

- [Lee–Nosal v4, equation (1) and Theorem 1.2](https://arxiv.org/pdf/2312.05628v4):
  the displayed error bounds assume RH, not simplicity, and have the
  stated \(x\ge2\) and \(x\ge101\) ranges. No claim of best available
  constants is made.
- [Ng, introduction and equation (8)](https://arxiv.org/pdf/math/0310381):
  weak Mertens implies RH and simplicity. Its warning about negative
  derivative moments confirms the circularity boundary recorded here.
- [Polymath, Proposition 3.1](https://arxiv.org/html/1904.12438v2)
  and [Rodgers–Tao, Lemma 12(i)](https://arxiv.org/pdf/1801.05914)
  supply the already-known root dynamics.

The [result index](../../../../../../../result-summaries/README.md),
[control catalogue](../../../../../../../result-summaries/12_collision_controls_and_screening.md)
and [avoid index](../../../../../../../avoid/README.md) govern the verdict,
especially [scope](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
and [same-model review](../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md).

## Acceptance gates

RHS-02's named signed transport has been fully estimated for its declared
global-envelope class and ends in a scoped failure. The coefficient
proposition distinguishes controls but does not satisfy the positive
theta-estimate gate. RHS-03 therefore has no arithmetic surplus to
transport. RHS-04 gains no theta exclusion, and a full proof review under
RHS-05 remains unavailable. This review completes the assessment of the
bounded continuation without changing those broader task states.

No new numerical evidence was needed: the claims were checked
analytically. The previous 265 exact rational fixtures are unchanged;
they are not presented as verification of these infinite estimates.
The original BW09 manuscript and its task registers were not modified.

[note]: ../notes/03_SIGNED_PRIME_TRANSPORT_AND_EULER_RIGIDITY_20261020.md

# Review of the opening Gaussian localization investigation

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
This is parallel same-model internal analysis and cross-review, not
independent specialist refereeing.

The reviewed artifact is the
[opening investigation](../../../notes/height_adapted_zero_detection/gaussian_localization/INITIAL_INVESTIGATION_20261004.md).
Its analytic identities and conditional detector are supported by the checks
below. It establishes no independent arithmetic saving or new zero-free
region. Kernel constants and a numerical unit-height count remain unevaluated.

## Mathematical checks

Three parallel analyses checked the Mellin and pole identities, inverse
kernel, and zero-side localization separately, followed by focused readbacks
of the assembled note. The following items were checked directly:

- The full scalar Mellin transform has factor \(-D_t\zeta'/\zeta\),
  the physical lower cap is \(-1/4\), and the prime Gaussian contains
  every von Mangoldt term.
- The simple derivative \(D_t'(1)=c_tK(1-it)/q\) is the surviving
  continuum moment. PNT supplies absolute convergence at the moment line;
  termwise prime integration there would be invalid.
- The contour formula gives a positive pole contribution and negative
  multiplicity residues. A fixed contour at real part minus one avoids
  a divergent infinite Gaussian trivial-zero sum. The explicit remainder
  estimate follows from the functional equation and a loose digamma bound.
- The inverse kernel crosses the preparation pole at one. Its resulting
  exponential tail prevents a global Gaussian-tail assertion.
- The real-centered Gaussian has physical center \(\mu\), and the stated
  Fourier normalization gives the \(L^1\) bound
  \(\|\check\psi\|_1\le(\|\psi\|_2\|\psi'\|_2)^{1/2}\).
  Polynomial inverse and Cauchy derivative estimates make this norm
  uniform in carrier and in \(k\ge1\), for fixed interior \(b\).
- The finite early and late contours use the horizontal factor
  \((\sigma-b)^2\). The late pole moment is exactly the known total
  minus a finite prefix, so its displayed budget requires no quantitative
  global PNT norm constant.
- Linked Gaussian parameters make residues into ordinary powers, with
  bases repeated by multiplicity. Taking a maximal base avoids a rightmost
  zero assumption. The finite guard and nearby left-zero costs are explicit.
- The gaps 319/256 and 63/16, the power-sum loss, continuous interval
  endpoints, and physical error exponents were checked. The elementary
  zero-tail inequality holds for all integers \(N\ge1\).
- A zero in the candidate box selects its own carrier inside the required
  continuous carrier band. The guard radius does not move the candidate
  or silently enlarge the arithmetic hypothesis.

One scope ambiguity was found in review: the initial fixed parameter choice
was proved at \(b=3/4\), but the box theorem could be read as applying
to every \(b>1/2\). The final note explicitly restricts it to fixed
\(3/4\le b<1\), and proves that the guard and displayed error exponents
improve above the base value. Inverse constants still depend on \(b\).
The fixed sample schedule is not asserted below \(3/4\).

## Diagnostic checks

The [standard-library diagnostic](../../../numerics/height_adapted_zero_detection/gaussian_localization/check_gaussian_preflight.py)
was run after source preparation. It verified rational parameter values,
the linked-parameter identity, and the formal two-zero cancellation example.
For \(1\le N\le4096\), its largest floating tail-to-loss ratio was
approximately 0.001018618 at \(N=1\), below the allowance 1/2.
The small record includes the source hash and states that it is not an
outward certificate or a calculation of actual zeta zeros.

These numerical checks validate the diagnostic and can catch bookkeeping
mistakes. They do not prove the analytic all-integer inequality, the
zeta count hypothesis, or the inverse constants.

## Remaining obligations

The conditional detector needs evaluated kernel constants, a certified
zero-count constant, and numerical enclosure of its finite budgets before
becoming a finite certificate. The coarse continuous prime-scale interval
can be very large; asymptotic compatibility does not establish practical
computability at a selected height.

The complete signed arithmetic upper bound remains open. Its carrier and
prime-scale range must match the detector, and its continuum, prime powers,
strict caps, terminal blocks, and frequency tails must remain in its proof.
Any new zero-exclusion claim must exceed the established classical region
and verified zero information used as inputs.

The proposed central-frequency saddle contour is not among the proved
kernel lemmas. Its shell residues, connectors, and physical tails require
a complete calculation before replacing the coarse bounds in this note.

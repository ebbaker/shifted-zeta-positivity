# Review of proportional Gaussian delay and its stationary phase obstruction

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded parent model **gpt-6.1-sol**, reasoning effort **ultra**, verified
from the session metadata and inherited by the reviewing agents.
This is internal LLM mathematical and computational review, not external
peer review or formal verification.

**Assessment: approved within the stated scope.**
[Note 24](../notes/24_PROPORTIONAL_DELAY_PHASE_OBSTRUCTION_AND_CONTINUATION_20261014.md)
provides a complete signed source representation, pays all pair sectors,
retains moving-delay derivatives, and proves a theta-specific obstruction
to the global exact retained sign for every fixed proportional delay.
The declared half-time rule nevertheless passes all 16 bounded pilot cases.
The analytic and computational parts were separately checked by agents
who did not implement the part they reviewed.

## Mathematical assessment

The phase obstruction uses the established four-jet theorem in Notes 17
and 19 at two fixed positive times. This is sufficient: both times
ultimately lie in its proved outer region. The quotient of the analytic
carriers has phase difference \(\delta\pi L/16+o(1)\) and earlier/current
amplitude ratio \(\exp(-\delta L^2/16+\delta\pi^2/64+o(1))\).
The zeta factors tend to 1 because their real parts tend to infinity;
consistent logarithms justify the phase error rather than treating it as
an arbitrary bounded phase.

Current stationarity gives \(\sin(\phi_t+j\pi/2)=O(1/L)\). This yields
the normalized retained product \(\cos D+O(1/L)\) without imposing any
earlier stationarity. The current derivative has opposite endpoint signs
in each phase window, while its next derivative has one strict sign;
there is exactly one genuine stationary point in each window. Jets only
through order 3 are used, including for the \(j=1\) branch. Negative
logarithmic phase bands contain whole windows and therefore actual theta
counterexample points. This does not rely on arbitrary prescribed jets or
on source symmetry alone.

The same calculation shows that absorption and the two full Laguerre
forms remain strictly positive sufficiently high on each fixed-time
slice. The obstruction concerns the required exact retained sign. Its
negative contribution is small relative to the already nonzero physical
energy, in contrast to the sharp-endpoint examples. No evaluated first
counterexample height or assertion in the moving unknown small-time
region is justified by the asymptotic argument.

The polarization keeps independent coordinates and indices, both
Hermitian and bilinear contributions, and the conjugation of the second
complex multiplier. The complete-source contour identity is justified
before truncation. The residual's analytic polynomial
\((z-ia)^2-b^2\) and Gaussian are real on the lower vertical segment;
individual raw theta terms are not claimed to be even. The fixed
\(a=\pi/16\) source moment majorant is integrable, and the three omitted
pair sectors are all paid. Note 12's tail bounds are used only for their
stated retained rectangles, or supersets.

The time derivatives correctly include the factor \(1/2\) in the earlier
time. The regular stationary branch speed is used only where its
implicit-function denominator is nonzero. No estimate through branch
creation or an unknown collision is claimed. The suggested height-dependent
delay and relaxed retained-loss criterion are research targets. The same
proportional rule may also be confined to the unresolved cusp and combined
with the existing outer theorem; the fixed-time obstruction does not
exclude that restricted-domain comparison.

The reviewer requested three clarifications, all incorporated: make the
centering parameters explicitly real in the obstruction theorem; state
\((h_0,h_1)\ne(0,0)\) instead of the ambiguous phrase “first jet is
nonzero”; and restrict imported rectangle tail payments to their proper
domains. No mathematical correction remained after these changes.

## Independent computation and replay

The [new pilot](../numerics/check_proportional_gaussian_source_filter_pilot.py)
was reviewed against the original full-source driver and certificate.
For slab \(k\), the earlier paid slab is \(\lfloor k/2\rfloor\).
Its displacement is exactly the current displacement divided by 2 plus
\(-1/64\) on even slabs and \(1/64\) on odd slabs. The entire earlier
range stays within the original paid time radius \(1/32\). Its spatial
center and positive normalization agree with the current cell.

Exact binomial substitution forms common-variable coefficient differences
before interval evaluation. Current and prior complete remainders are
then paid independently, with coefficients 1 for the complement and
1/2 for absorption. The original complete physical jet arrays through
order 28 suffice. Current endpoint signs and whole-cell monotonicity
prove both genuine unique branches for every time in the closed slabs.

An independent replay is byte-identical to the saved
[16-case record](../numerics/PROPORTIONAL_GAUSSIAN_SOURCE_FILTER_PILOT_20261014.json).
All required retained and absorption products are strictly positive.
Exact rational comparisons confirm the safe normalized lower bounds
\(8108,3999\) for retained/absorption on the \(j=0\) branch, and
\(4100,2025\) on the \(j=1\) branch. The complementary product alone is
undecided exactly on slabs 0 and 1 of both branches; its other 12 cases
are strictly positive. An undecided enclosure establishes no failure.

The independent reviewer also checked 1,200 exact rational evaluations of
the affine tensor against a separately evaluated nested Taylor polynomial.
All passed. The [review receipt](PROPORTIONAL_DELAY_INDEPENDENT_REVIEW_20261014.json)
records these checks and the matching pilot hashes. The saved
[audit driver](../numerics/audit_proportional_delay_affine_transport.py)
and [audit receipt](../numerics/PROPORTIONAL_DELAY_AFFINE_AUDIT_20261014.json)
reproduce those 1,200 finite algebra evaluations. The audit takes sources
beside the supplied pilot driver or at explicit paths; it has no
machine-specific source fallback.

The [identity checker](../numerics/check_proportional_delay_identities.py)
was replayed by both reviewing agents: all 20 exact rational polynomial
checks passed. These include controls that detect missing Hermitian
conjugation. They validate finite algebra, not infinite-domain analytic
signs. The original interval quadrature and analytic source-tail lemmas
remain trusted inputs; this continuation performs no new quadrature.

## Reproducibility and saved scope

| Saved item | SHA-256 |
| --- | --- |
| Pilot driver | `dbc5be224cb7e88171f3e8f29bde87606edc29833eb2752ea1d20c9e4178e72f` |
| Pilot record and independent replay | `67b24a58d5c2dccc119543b66b1a628ecc61394d5dc0079c3d9ca25d03af437d` |
| Identity checker | `6ac2e3e92e7a1030f3bb74c530eb72958ebdf11283d1771e3b37c048060a9dc3` |
| Identity receipt and independent replay | `bc9a1a07c79f3301a6ddb43941bdf4e86f833fa01969560e49b19f863bfb5d41` |
| Independent review receipt | `cca8766701f1a3b71e4f40b410fd4ac4b25f3a0f4a1f9db629bb3aec8e8af404` |

Hashes bind these exact saved objects; they do not certify their
mathematical content. The standard-library reproduction commands and
precise cell/source payments are in Note 24. All new files stay below
1 MiB. No new height coverage, manuscript revision, snapshot folder,
commit, or tag is part of this continuation.

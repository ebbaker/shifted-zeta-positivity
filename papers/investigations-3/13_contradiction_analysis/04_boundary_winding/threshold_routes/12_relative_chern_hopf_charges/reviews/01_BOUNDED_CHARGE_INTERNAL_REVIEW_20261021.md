# Internal review of the bounded charge comparison

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual model **gpt-6-astra (Codex)**,
reasoning effort **max**, verified from this chat's metadata.
This is the producing assistant's self-review, not independent validation.

**Assessment:** [Note 01][note] supports a finite interval certificate and
a scoped loss against direct derivative exclusion. It does not establish
a general advantage for charges or any global simplicity result.

## Analytic checks

- The affine reference has an interior nonzero second component. Its
  boundary degree is therefore zero; no inference from flatness or an
  absolute Chern class enters.
- The Taylor time terms have the negative signs required by
  \(H_t=-H_{zz}\). The remainder retains \(R^2M_{j+2}\), the mixed
  term \(2RTM_{j+3}\), and \(T^2M_{j+4}\). The bound covers complex
  time and position on the entire containing polydisc.
- The source summands are positive on the integration half-line.
  Dropping their negative term gives a valid absolute majorant there.
  The omitted-mode payment covers modes at every source position;
  the retained-mode payment covers only the exterior \(u\ge1\).
  Concavity includes the quadratic time growth and, on the exterior,
  the \(j\log u\) term. No source region is omitted.
- The interval integrands are entire. Quadrature errors use returned
  ball radii, not requested tolerances. Real symmetry justifies using
  real center coefficients; source tails enter their error radii.
- Smooth boundary regularity and complex orientation are fixed. The
  positive-charge interpretation retains the inherited isolation
  hypothesis. The direct derivative bound independently proves that
  this particular domain has no joint zero, so the pilot does not rely
  on an unproved isolation assertion.

## Quantitative and control checks

The 192-bit [receipt][receipt] certifies boundary gap greater than
0.00007495 and derivative floor greater than 0.00007993. Opposite signs
at 451/16 and 453/16, together with the derivative floor, prove that a
unique simple real zero lies in the domain at time zero. This confirms
nonvacuous coverage without assuming a tabulated zero location.

The exact quadratic test returns charge one, with gap 7/1600, on the
same radii. Its constant degree-zero reference fails explicitly. The
cubic calculation retains two nonreal-time events in addition to the
real event. These checks would expose an erroneous rule forcing every
relative charge to zero in flat space or discarding nonphysical events.
The wider source-control response is an analytic application to
inherited witnesses, not a fresh numerical replay of those witnesses.

## Comparison and scope

The direct method uses six of the eight source integrals, with the same
accuracy and domain. Its 1,656 callbacks are an exact subset of the
boundary method's 2,208 callbacks. Its time is the sum for that subset
in the shared run, not an independent timing benchmark. Neither method
uses a mesh; comparing a boundary calculation with a deliberately dense
interior scan would be unfair here.

The inequality \(b-\sqrt{e_0^2+e_1^2}\le b-e_1\) proves the reported
loss for the specified component-floor construction. It does not apply
to every full vector reference floor. The constant-reference screen is
a separate maximum-modulus observation. The next experiment should
require both jet components, then compare against direct joint
exclusion using the same information. Enlarging this pilot without
changing that comparison would not be a new mechanism.

The manuscript, HMC gates, and global result summaries need no status
upgrade. RCH-01 through RCH-03 should be marked complete only for the
specified finite pilot. RCH-04 remains gated.

[note]: ../notes/01_BOUNDED_THETA_CHARGE_AND_DIRECT_COMPARISON_20261021.md
[receipt]: ../numerics/RELATIVE_CHARGE_PILOT_20261021.json

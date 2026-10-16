# Continuation after the first Wilson-Loewner calculation

19 September 2026. OpenAI GPT-6 (Codex), for Edward Baker.

**Historical handoff:** the endpoint test below has now been carried out in
[the second calculation](DEFECT_PROJECTORS_AND_ENDPOINT_POLARIZATIONS_20260919.md).
Use [the second continuation](CONTINUATION_20260919_SESSION2.md) for the current
task list. The remainder records the state after the first calculation.

Read the [opening note](OPENING_NOTE_20260919.md) and then
[smooth variation and the constant driver](SMOOTH_VARIATION_AND_CONSTANT_DRIVER_20260919.md).
This is a new notes-stage investigation in the folder Edward created.
The two parent manuscripts and their preserved drafts have not been changed.

## What was obtained

1. In the normal plane, inversion \(w=-1/z\) sends the existing upper
   semicircle from r to zero to a vertical slit at \(-1/r\). Its chordal
   Loewner driver is constant; the full contour takes infinite capacity
   time. The exact scale/time relation is recorded in (1.4).
2. The fixed scalar coupling and inherited special bulk charge force this
   geometry: \(\dot z/|\dot z|=iz^2/|z|^2\). This is proved for a real
   regular curve in one fixed normal plane, with a nonzero complex spinor.
   It is not a universal exclusion of Wilson-Loewner constructions.
3. The smooth Wilson variation includes transported field strength, scalar
   gradients, arclength variation and endpoint covariant derivatives.
   Substitution of the regular inverse-Loewner velocity gives the actual
   insertion equation. It does not close on one scalar observable without
   further field-theory input.
4. The tangent-coupled scalar prescription supplies a common complex bulk
   projector for arbitrary smooth planar contours. Its free bulk exchange
   cancels. It is a useful control and a candidate ansatz, not a physical
   endpoint or positivity result.

## Next calculation

Solve the defect endpoint problem for a concrete tangent-coupled family.
Start from Baker, [arXiv:1102.4948](https://arxiv.org/abs/1102.4948), Appendix C,
and impose the defect-preserved spinor conditions together with the two
bulk tangent projectors and the polarized endpoint variations. Track the
SU(2)H and SU(2)V scalar choices separately. Physical conjugation and
chirality cannot be replaced by a nonzero complex Clifford projector.

Use a common-reference state preparation, or explicitly define how a
moving color state at the Loewner tip is glued. A growing bulk tip cannot
carry the three-dimensional endpoint field by notation. An alternative
is to deform complete contours with their endpoints kept on the defect.

If that test succeeds, the next observable is the first interaction-order
insertion response, including endpoint/line terms. The free endpoint kernel
is insensitive to interior contour deformations, and the tangent-coupled
bulk exchange alone cancels. A nontrivial response must therefore come from
the omitted physical terms or a justified additional sector.

Only after deriving that response should one identify the evolution
parameters with \(L,\omega\), compare with the parent's exact arithmetic
transfer, and try to prove contraction in the required norm. Adding a zeta
ratio by hand is not a derivation. Brownian driving and a rough-curve limit
are additional constructions, not prerequisites for the next calculation.

## Verification and current boundaries

Run `python3 validation/check_package.py check --replay` from the
investigation directory. The package binds the notes, checks, records and
selected inherited sources. Replay compares case identity and declared
tolerances; floating diagnostic values need not be byte-identical across
runtimes. There are 102 finite cases, all passing in the recorded run.

No manuscript, draft snapshot, independent review, endpoint solution,
reflection-positivity theorem, arithmetic mechanism, or RH result is
claimed. The inherited restrictions and their controls should remain
visible in any later continuation.

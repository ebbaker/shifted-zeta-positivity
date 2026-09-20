# Continuation after the defect endpoint calculation

19 September 2026, second calculation. OpenAI GPT-6 (Codex), for Edward Baker.

**Historical handoff:** the reflection and reference-junction test has now
been carried out in [the third calculation](REFLECTION_JUNCTION_AND_BULK_RESPONSE_20260919.md).
Use [the third continuation](CONTINUATION_20260919_SESSION3.md) for the current
task list. The remainder records the state after the endpoint calculation.

Read [the endpoint calculation](DEFECT_PROJECTORS_AND_ENDPOINT_POLARIZATIONS_20260919.md).
This supersedes the task list in the [first continuation](CONTINUATION_20260919.md),
which is preserved as a historical handoff. The investigation remains in
notes; no manuscript, draft snapshot or independent review has been created.

## What is now established

1. The planar connection
   \(iA_1dx^1+iA_3dx^3+X_8dx^1+X_6dx^3\) admits a two-complex-dimensional
   space of constant chiral, defect-compatible charges. Tangent scalars
   must be V-valued and the normal scalar H-valued within this real,
   constant-map, independently variable tangent ansatz.
2. One common complex charge also works across all defect directions.
   With \(\chi=D=+1\), use V scalar map \(\mathrm{diag}(-1,1,1)\) and
   normal scalar \(+X_6\). The map determinant must be \(-1\) in these
   conventions; the other orientation has no common spinor. This is a
   sign choice that can be made, not a general obstruction.
3. The normal projector fixes one H weight. For the source convention
   \(Q_{i2}\), ordinary same-charge endpoints are \(q_2,\bar q_1\).
   Their free contraction is zero. The whole line has residual H charge
   \(-1\), so its expectation and neutral shape variations vanish in
   a symmetry-preserving vacuum and regulator.
4. The physical adjoint pair \(q_2,\bar q_2\) has nonzero free overlap,
   but the antifundamental is not killed by that same constant charge.
   A ket closed by \(Q\) naturally has a bra closed by \(Q^\dagger\).
   This does not settle whether a useful supersymmetric positive network
   can be constructed.
5. For Hermitian matrix fields, the elementary transport identity is
   \(U_M(C)^\dagger=U_{-M}(C^{-1})\). Contour reversal with unchanged
   \(M\) is the inverse instead. A physical spacetime reflection and
   its color junction are still to be derived.

The off-diagonal endpoint selection is already in Baker's original
analysis. The work here combines it with the chiral defect projector
and the tangent-coupled arbitrary-contour family. Do not describe it as
a new general no-go theorem or close the whole Wilson--Loewner program.

## Next calculation: the adjoint and the reference junction

Keep a complete smooth contour from a defect endpoint to a common
reference point. Start with the endpoint state built from \(q_2\) and
the connection above. Write its actual adjoint using (8.1), then specify
the spacetime reflection appropriate to the proposed state pairing.
Identify the R action, if any, required by the reflected scalar map.
Do not identify an R-twisted bilinear with a positive inner product
without deriving its metric and conjugation.

At the common reference, display every color index and any endpoint or
junction field. Determine which charges annihilate the two branches and
the junction. The line's scalar coupling can jump there, so a cusp or
local insertion may be unavoidable. A genuine Gram construction must
control that junction and its regulator, not merely use suggestive
notation for a product of transports.

The finite-dimensional classical identity in (8.1) is a useful control,
but Euclidean quantum reflection is a separate step. An admissible
construction must specify the reflection surface, support of each state,
gauge treatment and limiting prescription. The parent angular smearing
must be retained where it was needed for a finite free covariance.

Once a candidate paired observable is fixed, substitute the first note's
smooth Wilson variation into it, including endpoint and junction terms.
Test whether the displacement is exact for a compatible charge or has
a nonzero interacting response. Only then compute the first interaction
order that can see the contour. A change of the free endpoint propagator
alone cannot see the interior curve, and the equal-propagator bulk
gauge/scalar exchange cancels for the isometric tangent map.

If ordinary adjoint gluing fails this test, two concrete alternatives
remain: allow a position-dependent conformal Killing spinor and solve
for its scalar map, or add specified junction/endpoint matter with an
explicit supersymmetry transformation. Neither is supplied by this note.

## What an RH route still needs

A nonzero regulated positive pairing is the immediate target. It must
then produce, rather than assume, the exact arithmetic transfer, including
the prime measure and pole correction from the parent Loewner work.
An independent contraction or positive-defect argument must hold for
every support length in the range with RH content. The present endpoint
algebra proves none of these. In particular, replacing the parent's
nonzero free adjoint kernel with the common-charge off-diagonal pairing
annihilates it; that replacement is not progress toward its target form.

## Verification and status

Run `python3 validation/check_package.py check --replay` in this
investigation. The original 102 diagnostics and 99 new chiral/defect/
endpoint cases give 201 passing cases. The latter use explicit
32-dimensional matrices and an independent row-reduction check of
the simultaneous constraints. Correct triplets, map orientation,
physical adjoint overlap and the original conformal semicircle supply
positive controls for the restricted negative statements.

The proofs are written derivations under displayed assumptions; the
checks are finite diagnostics. Quantum operator existence, reflected
positivity, protected deformation, arithmetic matching and RH remain
open. No independent review is recorded.

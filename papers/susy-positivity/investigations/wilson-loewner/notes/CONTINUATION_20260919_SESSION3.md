# Continuation after physical reflection and the reference junction

19 September 2026, third calculation. OpenAI GPT-6 (Codex), for Edward Baker.

Read [the reflection and response note](REFLECTION_JUNCTION_AND_BULK_RESPONSE_20260919.md).
This supersedes the task list in [the second continuation](CONTINUATION_20260919_SESSION2.md).
All earlier notes remain as dated research records. The investigation still
has no manuscript, archived manuscript draft, or independent review.

## Results to carry forward

- Use ordinary Euclidean time reflection \(x^0\mapsto-x^0\), tangent
  to the physical defect \(x^3=0\). The scalar map
  \(M=(-e_7,e_8,e_9,e_6)\) reflects to \(N=-MR\), hence
  \(N=(-e_7,-e_8,-e_9,-e_6)\). All scalar fields are even in this
  ordinary time reflection; the map signs arise from adjoint and orientation.
- The actual observable is
  \(\langle\bar q_2(\vartheta a_i)U_N(\vartheta C_i^{-1})
  U_M(C_j)q_2(a_j)\rangle\). The reference color index is contracted by
  the identity at \(b=0\), with no extra matter insertion. It is gauge
  invariant. A positive state interpretation remains conditional on an
  OS-positive regulated theory in this reference color sector and a
  well-defined junction; the color fiber must be included in the Gauss-law
  and state-space discussion.
- The free kernel on a positive time ray is \(1/(r+s)\). After weights
  \(\sqrt{rs}\) it is \(G_o(u)=1/(2\cosh(u/2))\), not \(n_\gamma\).
  The parent's entire-sphere even Poisson profile is not supported in one
  time half-space. Its valid free covariance cannot be relabeled as this
  OS construction.
- Both branches have constant chiral defect-compatible charges, but the
  normal projector has opposite eigenvalues. Their common solution is
  zero for the curved family. An H and V \(\pi\)-rotation can restore the
  ket's bulk scalar map. It rotates \(\bar q_2\) into a phase times
  \(\bar q_1\); the elementary same-charge diagonal is zero, and on the
  full endpoint doublet the inserted metric is nonpositive.
- The older odd-H normal-reflection assignment fails the canonical free
  bulk positivity test even on the Hermitian gauge-invariant polynomial
  \(i\operatorname{tr}(H[V_1,V_2])\). This excludes that assignment as
  a positive reflection on the full free bulk algebra. It is not a
  classification of every possible defect reflection or restricted sector.
- A ket must arrive at the reference along \(-e_0\) to glue smoothly to
  its time-reflected reverse. The explicit family
  \(X_{T,\eta}(t)=(Tt,\eta Tt^2(1-t))\), traversed from 1 to 0,
  does this. Its scalar direction is also continuous at the join.
  The old normal-arrival semicircles would backtrack under this reflection.

## The concrete perturbative foothold

For \(f(t)=t^2(1-t)\), the direct bulk gauge/scalar cross exchange is

\[
I(\eta)=2\eta^2\int_0^1\!\int_0^1
\frac{f'(s)f'(t)}{(s+t)^2+\eta^2[f(s)-f(t)]^2}\,ds\,dt
=\left(\frac32-2\log2\right)\eta^2+O(\eta^4).
\]

The numerical coefficient is 0.1137056388801094. With the propagator
normalization \(g^2/(4\pi^2x^2)\), multiply by \(g^2C_F/(4\pi^2)\)
relative to the free endpoint propagator. Same-branch bulk exchange
cancels. Near the reference, the cross numerator is \(O(st)\), its
denominator is of order \((s+t)^2\), and this bulk term is locally finite.

This is a Feynman-gauge subset, **not the complete response**. The
nonnegative cross-current Gram structure of that subset is not an
interacting positivity theorem or a protected kernel. Nor does a
Q-closed ket protect its physical norm: a Q-exact variation has first
norm variation \(2\operatorname{Re}\langle Q^\dagger\psi,\lambda\rangle\).

## Next calculation: complete the first shape-response order

Begin with the source defect action and Feynman rules in Baker,
[arXiv:1102.4948](https://arxiv.org/abs/1102.4948), with the same generator,
field and coupling normalizations as its perturbative open-line analysis.
Read the printed action and vertex factors before importing a sign.

1. Fix \(T\), a nonzero bulge \(\eta_0>0\), and a single endpoint and
   reference-junction prescription. Define the normalized observable
   whose derivative with respect to \(\eta\) is being computed. State
   the reference color sector and do not assume the bare continuum norm
   exists simply because its color indices close.
2. Enumerate all terms at the first relative interaction order. The
   already calculated direct bulk exchange must be combined with the
   endpoint-to-line gauge contribution and the H-scalar derivative
   coupling from the defect action. Check the power counting of all
   other vertices, endpoint self-energy and counterterms explicitly.
3. At fixed endpoints, isolate which endpoint normalization terms cancel
   in the chosen shape difference or ratio. Keep possible terms from
   the reference touching the defect. Use one regulator consistently
   across gauge, scalar and endpoint sectors.
4. Compute the finite shape response around \(\eta_0\), including any
   scheme dependence. Only then investigate \(\eta\downarrow0\): the
   \(\eta=0\) line lies on the defect everywhere, so the limit may have
   boundary contact terms or nonanalytic dependence absent from the bulk
   subset. An analytic \(\eta^2\) expansion of the full answer is not yet
   justified.
5. Use straight bulk cancellation, ordinary free reflection positivity,
   the matrix adjoint identity and the known coefficient above as
   separate controls. If a supersymmetry cancellation is asserted,
   exhibit its Ward identity with all endpoints and contact terms.

No specific Loewner driver has been derived for this polynomial contour
family. A driver/capacity calculation can follow a nontrivial physical
shape response; capacity is not yet the arithmetic shift. The earlier
smooth variation formula supplies the insertion equation without assuming
such an identification.

## RH target and verification

The immediate target is a nonzero, well-defined paired response. It must
then be related to the required archimedean kernel and exact arithmetic
transfer, including prime weights and the pole correction. The reflection
calculation exposes a concrete mismatch already at free order: it produces
\(G_o\). A derivation of the missing sector and an independent all-length
contraction argument are still required. Nothing in this session proves
an RH criterion's positivity.

Run `python3 validation/check_package.py check --replay`. There are 268
passing cases: 102 from the first calculation, 99 from the second and 67
from this one. The last program checks the reflected matrix ordering,
color gluing, independent Clifford nullspaces, free positive/negative
reflection controls, junction behavior and the bulk coefficient with
independent quadrature. Analytical and conditional statements have their
own status ledger in the main note; replay does not certify quantum
operator existence or the proof obligations above.

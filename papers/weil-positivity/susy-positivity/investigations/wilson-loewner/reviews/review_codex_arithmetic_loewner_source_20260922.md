# Internal audit: arithmetic source and generalized Loewner evolution

22 September 2026. Prepared for Edward Baker with LLM assistance.

**Model:** GPT-6 (Codex; developer-provided identity).  
**Effort:** not exposed in this session; not inferred.  
**Review status:** same-assistant mathematical and numerical audit, not an
independent specialist review. The reviewed artifact is the
[arithmetic-source note](../notes/ARITHMETIC_SOURCE_AND_GENERALIZED_LOEWNER_EVOLUTION_20260922.md).

## Assessment

The note supplies a valid classical construction from the shifted xi
logarithmic derivative to generalized Loewner evolution, on its stated
zero-free domain. It also identifies why this construction does not yet
realize the arithmetic multiplier as a physical boundary operator or
establish its unweighted contraction. The main scope distinctions survive
the checks below. The priority change from unrestricted WZW sewing to a
source-specified cumulative response is supported as a research decision,
not as evidence for a proof of RH.

## Mathematical checks

1. **Arithmetic convention and signs.** With
   \(H(p)=\xi(1/2+p)\), differentiating the numerator and denominator
   gives \(\partial_\omega K_\omega=-[m(p-\omega)+m(p+\omega)]K_\omega\).
   The completed source has positive \(1/s\) and \(1/(s-1)\) terms;
   its prime logarithmic derivative is negative. The paired shifts give
   exactly the stated cosh coefficient, including the first delay.
   The note does not drop the completion's local or pole terms.

2. **Whole-domain positivity.** The real-part zero sum is justified by
   the centered product, not by truncating critical zeros. Centering and
   functional symmetry remove the real constant. The real-part sum
   converges absolutely. A zero in the claimed domain gives a genuine
   positive-residue pole, so the reverse implication in (3.2) is valid.
   At zero shift the statement is RH-equivalent, as the note explicitly
   records. No inference from a finite positivity sample is used.

3. **Loewner normalization and global existence.** The Cayley transforms
   map disk to right half-plane in the stated direction. The radial
   vector field is \(-wP_\eta(w)\), so its derivative at the origin
   is \(-1\). The second vector field is
   \((1-w)^2/[2P_\eta(w)]\); \(\Re(1/P_\eta)>0\) makes it a
   Berkson--Porta generator with boundary fixed point 1. This supplies
   global self-map semigroups, not merely local ODE solutions. The
   note correctly avoids identifying them with a single real-driver
   chordal slit or the preceding WZW flow.

4. **Measure and linearization.** The safe-line density has the correct
   factor \(1/(2\pi c_\eta)\). The point at infinity contributes no
   atom because \(m(x+\eta)/x\to0\). For imaginary zeros, the
   weights are \([c_0(1+\gamma^2)]^{-1}\), with both signs and
   multiplicities; they sum to one. The imaginary constants in individual
   transformed kernels cancel in the paired sum. The line-segment
   argument proves univalence of \(\log H(p+\eta)\), not of \(H\).
   Differentiating it along (5.1) gives exactly \(c_\eta\).

5. **Parameter and domain separation.** The reconstruction (4.6) requires
   \(\Re p>\eta+\omega\), so both disk arguments remain inside.
   The source translation equation includes its normalization derivative
   \(-c_\eta'/c_\eta\). Forward translation preserves the positive-real
   property; backward translation need not. The off-axis quartet has the
   stated functional symmetries but no claim to the Euler product or xi
   asymptotics. It refutes a general continuation shortcut, not an
   arithmetic theorem.

6. **Cumulative versus infinitesimal positivity.** Under RH, the poles
   of \(a_\omega\) at \(\omega+i\gamma\) are internal to the
   right half-plane; zeros of \(K_\omega\) cancel them only in the
   product. The polynomial control is a true finite Blaschke transfer.
   Its exact negative generator and modulus below one demonstrate that
   infinitesimal multiplicative contractivity is too strong. The Cayley
   Riccati identity does not by itself establish a positive-real
   solution. This is consistent with the manuscript's accumulated
   defect identity.

7. **Operator consequence.** The extra spectral translation
   \(b\ge\Omega+1/2\) makes both source arguments safe for all
   \(0\le\omega\le\Omega\). The shifted multiplier is analytic
   and bounded by one, hence contractive on the Hardy/Laplace space.
   The finite-window conjugation has the sign
   \(V_{\omega,b}=E_{-b}V_\omega E_b\), giving an upper bound
   \(e^{bL}\) for the unweighted norm. That factor is not a contraction
   estimate uniform in length. The initial limit is strong, not a
   claimed operator-norm limit. No independently derived field-theory
   norm is obtained by this conjugation.

8. **Scope of the composition obstruction.** The test with analytic
   functions 1 and \(p\) excludes equality of a nontrivial weighted
   composition operator and multiplication on all analytic functions.
   These tests are not falsely asserted to be half-plane Hardy vectors.
   The calculation does not exclude an additional boundary projection,
   integral transform, scattering observable, or change of Hilbert space.

## Source audit and provenance

The standard positivity criterion is credited to Lagarias, with the
published correction included. The corrected auxiliary inequality is
not used to claim more than the centered product proves here. The
generalized Loewner criterion is credited to Bracci, Contreras and
Diaz-Madrigal. Suzuki's unconditional explicit canonical-system range
is kept at \(\omega>1\), distinct from unconditional innerness at
\(\omega\ge1/2\). These primary sources are linked in the note.

The earlier commuting shift source, cumulative Cayley proposal, and
modular-surface endpoint are credited to the existing repository notes.
The new note does not present them as new discoveries. Neither the
source-defined geometry nor the existing endpoint scattering example
supplies the missing continuous family of physical boundary operators.

## Numerical record

The [checker](../numerics/check_arithmetic_loewner_source.py) produced
[60 passing cases](../numerics/records/arithmetic-loewner-source-20260922.json):
four rational sign/modulus controls and 56 floating diagnostics. The
record binds the checker hash, parameters, library versions, individual
thresholds, and sample outputs. The run uses no xi-zero table. Only the
finite polynomial controls specify zeros as model input.

At the two prime samples the floating residual-to-analytical-tail ratios
are approximately 0.1411 and 0.1360. The tail bound uses the decreasing
integrand in the sampled range; its floating evaluation is not interval
arithmetic. The direct xi/completion formulas are sampled away from their
individually removable singularities.

For the two flow samples, 64-versus-128-step discrepancies are at most
\(1.36\times10^{-13}\); the xi linearization residuals are at most
\(7.31\times10^{-16}\). These are ODE diagnostics, not certified global
integration bounds. The semigroup composition control uses matching
steps and mainly checks composition consistency; the separate implicit
xi identity supplies the meaningful independent check of the vector field.

The checks do not test an infinite zero measure, prove RH, remove the
spectral weight uniformly in length, or construct a physical sewing map.
The note's analytical arguments carry those distinctions. The new
records are separate from earlier WZW and manuscript counts; manuscript
sources, PDFs, archived snapshots and previous research notes are
preserved.

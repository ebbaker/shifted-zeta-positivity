# Bulk realization and defect observables: overview of research directions

14 September 2026. **Broad program map**, rather than a calculation for a
particular field theory. The [inverse-bulk investigation](../investigations/inverse-bulk-realization/README.md)
contains the detailed notes, current comparisons, and reproducible checks.

## 1. The objective and the intended contribution

Find a field theory or observable sector with an independently justified
positive Hilbert-space pairing, and derive an exact identity between that
pairing and the complete localized Weil form. The input is a complex test
function on a finite interval in the logarithmic arithmetic variable.
The source preparation must be complex linear, and its norm must reproduce
the archimedean term, normalization, pole terms, and every active prime
power with their prescribed coefficients. The preparations must agree
when the interval grows.

The difficulty should lie in **choosing the system and fitting its complete
pairing to the arithmetic data**. A discrepancy can disqualify a source
prescription or identify missing model structure. It is not an invitation
to bound an increasingly complicated remainder in the same prescription.

An eligible theory need not already have a rigorous construction. A useful
conditional result could say: construction of this independently specified,
credible theory with these observable properties implies RH, by an exact
matching theorem. Independent support can come from unitarity, a stable
regulated formulation, consistent dualities, exact protected formulas, or
nearby constructive results. These are sources of evidence, not a list of
mandatory prerequisites. Pure four-dimensional Yang–Mills remains eligible.

The construction hypotheses must not assume the desired Weil covariance
or an equivalent arithmetic positivity statement. An ordinary positive
state gives positivity of the norm of a state created by an observable;
the observable itself need not be a positive operator. For an interacting
theory, an observable linear in the test function still gives a quadratic
norm. The real problem is deriving that norm and its complete arithmetic
identification, including domains and any continuum limits.

Only the forward implication from field-theoretic construction to RH is
part of this program. A speculative converse involving the hard part of
Yang–Mills existence or mass gap is not a proposed claim of the paper.
A gap is needed only if a particular construction or limiting argument
uses it; the positivity of a physical norm does not itself require a gap.

## 2. What “boundary” is allowed to mean

The arithmetic input need not live on the geometric boundary of spacetime.
Possibilities include a boundary or interface, a reflected cut used for
gluing amplitudes, a Wilson or other defect line, a network of junctions,
or a protected operator algebra acting on prepared states. The logarithmic
variable may label operator coefficients or a spectral transform instead
of distance along a physical line.

A line inside a sphere is therefore a legitimate setting to investigate.
In a conformal theory, specified conformal transformations relate lines
and circles; arbitrary changes of shape need not preserve a correlator.
Protected sectors can supply stronger invariance for specified insertions
and deformations. Their conjugation and physical pairing must still be
identified. Pure quantum Yang–Mills and conformal supersymmetric gauge
theories should be treated as different cases here.

## 3. Map of the ideas and their present roles

The ranking below concerns opportunities for an exact matching calculation,
not the likelihood of proving RH or the strength of existing construction
theorems. The detailed literature assessment is indexed in the
[inverse-bulk investigation](../investigations/inverse-bulk-realization/README.md).

| Direction | Reason to pursue it | Present status and next discriminating question |
|---|---|---|
| **3D supersymmetric sphere quantization** | A protected Higgs/Coulomb algebra has a physically positive twisted trace, explicit operator actions, and gluing interpretations. | First leading contender. Test concrete free and rank-one interacting examples, then source maps using monopole or vortex operations. Can the actual pairing force the complete arithmetic kernel? |
| **4D supersymmetric Schur quantization** | Half-BPS line algebras, multiplicative difference operators, duality interfaces, and a doubled-algebra Hilbert space constrain one common pairing. | Second leading contender. Test a concrete conformal gauge example and its line operations; distinguish a physical adjoint from a formal multiplicative shift. |
| **Boundary Liouville theory** | Interacting amplitudes, exact special-function identities, and constructive gluing results provide substantial control. | Leading alternative if protected gauge sectors offer insufficient source freedom. Identify a reflected preparation with a computable complete norm. |
| **Free bosonic or fermionic fields with arithmetic defect data** | Positivity and source norms can be computed directly, including centered fermion bilinears. | Fast control for an independently proposed arithmetic geometry. Check whether it merely recovers the already studied canonical semilocal pairing. |
| **Integrable QFT in two dimensions** | Exact transmission/reflection data and form-factor methods provide nontrivial interacting observables. | Alternative using defect-changing or nonlocal preparations; the hypothesis must cover the actual defect sector and its norm. |
| **Supersymmetric Wilson defects and pure Yang–Mills networks** | Strong physical motivation, gauge constraints, transfer evolution, and, in selected supersymmetric theories, exact protected data. | Remain eligible. Simple local line insertions and literal loop winding do not supply the required arithmetic structure; investigate junctions and richer preparations. |
| **Two-dimensional Yang–Mills and positive disk transfer models** | Explicit positive gluing/transfer models isolate the distinction between winding, return amplitudes, and complete source norms. | Useful controls already tested. Correct isolated repetition factors do not determine the contact and interference terms of the Weil pairing. |
| **Hyperbolic or arithmetic geometry and quantum graphs** | Primitive returns, scattering formulas, and trace identities offer direct access to prime data. | Strong arithmetic motivation. A relative trace or a zeta resonance formula must be converted into the required positive state pairing. |
| **Schwarzian theory and other boundary quantum mechanics** | Exact bilocal matrix elements and gamma-function spectral formulas give tractable nonlocal observables. | Special-function and preparation controls; their known spectral measures are not already the Weil measure. |
| **Stable scalar constructive theories** | Established interacting positive models provide a reference for domains, renormalization, and gluing. | Useful construction controls; a specific arithmetic interface mechanism is still missing. |
| **Adelic, p-adic, tree, and Bost–Connes systems** | Multiplicative correspondences and local factors make arithmetic operations explicit. | Possible ingredients for a global source or interface. A partition function or local Euler factor is not the sought global positive Weil norm. |
| **Superspace, cohomological, and topological constructions** | Symmetry can constrain pairings and make a broadened notion of boundary natural. | Earlier proposals remain an organizing language. The quotient, real structure, and actual positive observable norm must be made concrete in a selected system. |

## 4. What earlier work contributes to the selection

The [ground-state geometry investigation](../investigations/arithmetic-ground-state-geometry/README.md)
and [finite-response manuscript](../manuscripts/finite-response-weil-positivity/README.md)
provide a precise target and distinguish a positive reference model from
the unresolved arithmetic matching. The
[earlier assessment](ASSESSMENT.md) records the novelty reassessment and
the change in priority. This program should be judged by new matching
identities or informative, precisely scoped model tests, rather than by
the general observation that a physical norm is positive.

The inverse-bulk notes establish several useful selection results:

- Finitely many rational feedback channels of the tested form cannot
  implement the required exact constant subtraction across the full
  spectrum of the reference operator.
- The positive gamma tower admits an exact integer-branch refinement.
  This is a useful action identity based on a classical multiplication
  formula; it is not a new arithmetic positivity result.
- Literal winding in the tested SU(2) heat-kernel model fails the required
  prime repetition law. Transfer evolution can give the desired isolated
  factor, but that is only one part of the source pairing.
- A positive disk model realizes the gamma masses and selected return
  amplitudes. The tested branch preparation has an unwanted cusp; a
  coherent modification removes that cusp but leaves the contact mismatch.
  These results concern the specified preparations, not all gauge theories
  or all possible common-field constructions.

These lessons favor a common operator algebra and trace identity that
constrain prime operations, interference, and normalization together.
Sphere and Schur quantization are the next concrete tests of that idea.

## 5. From exploration to a specific paper

Keep this overview broad. Keep the literature survey and the existing
calculations as distinct research notes in the inverse-bulk investigation.
The next note compares the first two contenders using named systems,
specified positive pairings, and explicit source tests. Other systems
remain available if those tests indicate a different choice.

Specialize a paper only after a system and observable prescription have
earned that focus through preliminary results. Its central statement
should identify the theory, preparation, real structure, and exact
matching identity, distinguishing proved steps from the construction
hypothesis. An informative failure of a narrow ansatz is a research note;
it does not by itself justify presenting that system as the RH mechanism.

For the source-supported comparison, start with
[Gaiotto on sphere quantization](https://arxiv.org/abs/2307.12396) and
[Gaiotto–Teschner on Schur quantization](https://arxiv.org/abs/2406.09171).
The investigation's broad survey records the sources and qualifications
for the alternatives in the table.

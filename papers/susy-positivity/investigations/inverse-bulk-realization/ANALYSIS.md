# Exact bulk fitting after the semilocal comparison

14 September 2026. Research continuation; all-length positivity remains open.

Latest calculations: [gauge transfer and the first-prime boundary test](GAUGE_TRANSFER_TEST.md).
These test a constructible gauge-theory control, realize the gamma masses
and geometric returns in one positive disk model, and compute two
first-prime preparations whose complete pairings fail for explicit reasons.

## 1. The intended direction

The problem is to find a bulk model \(M\), a trace or preparation map, and
its physical pairing such that

\[
Q_L[f]=\inf_{\operatorname{Tr}\Phi=f}\mathcal E_M[\Phi],
\qquad \mathcal E_M[\Phi]\geq0,
\tag{1}
\]

or, for a linearly prepared state in a positive Hilbert space,

\[
Q_L[f]=\|\mathcal O_M(f)\Omega_M\|^2.
\tag{2}
\]

The positivity must follow from the specified bulk system, independently
of the sign of \(Q_L\). The difficult theorem is the exact boundary
identity, including domains, normalization, poles, and prime terms.
One first matches on \(C_c^\infty(I_L)\) and then establishes any claimed
closure. A uniform rule in \(L\), with compatibility under enlarging the
input interval, is needed for an all-length result.

Equation (1) requires a nonnegative joint energy, not just a positive
Hessian in an auxiliary variable under an external drive. For example,
\(w^2-2fw\) is coercive in \(w\) but has minimum \(-f^2\). The distinction
is already explicit in the
[collective-feedback construction](../arithmetic-ground-state-geometry/notes/17_COLLECTIVE_FEEDBACK_AND_COMPACT_DEFECT.md).
An interacting quantum model with an independently established positive
physical Hilbert space can supply a quadratic pairing through a linear
state preparation. If \(\Phi(f)=\mathcal O(f)\Omega\) is well defined,
then \(B(f,g)=\langle\Phi(f),\Phi(g)\rangle\) has
\(B(f,f)=\|\mathcal O(f)\Omega\|^2\geq0\). The operator
\(\mathcal O(f)\) itself need not be positive. The physical adjoint,
finite-norm domain and exact identity with \(Q_L\) must be established.
A nonlinear classical minimum requires a separate argument that its
complete boundary dependence is quadratic.

The previous canonical semilocal comparison is useful as a model
diagnostic: its metric and projection produce an independently positive
pairing, but that pairing has not been identified with the complete
localized Weil form. Decomposing the difference tells us what a candidate
does. It does not oblige us to keep the candidate and estimate that
difference. The next question is which bulk operation could supply the
missing identity.

## 1a. An intermediate target: reduction to a construction problem

The exact matching theorem can be valuable before the proposed field
theory has been rigorously constructed. The next milestone may therefore
be a specified model \(M\), a specified boundary insertion, and a theorem
that every realization satisfying explicitly stated construction
hypotheses has

\[
B_{M,L}(f,g)=Q_L(f,g)
\qquad
(f,g\in C_c^\infty(I_L),\ L>0).
\]

Here \(Q_L(f,g)\) denotes the polarization of (3). If the construction
hypotheses supply a positive physical Hilbert space and the matching
observable is an ordinary state pairing, the implication is

\[
\text{construct }M\text{ with the specified observable}
\quad\Longrightarrow\quad Q_L\geq0\text{ for every }L
\quad\Longrightarrow\quad\mathrm{RH}.
\]

The final implication is the established Weil positivity criterion;
see the shared framework and
[Connes–Consani–Marcolli](https://arxiv.org/abs/math/0703392).
The paper pursues the forward implication from a constructively credible
field theory and its exact boundary matching identity to RH. A proposed
Yang–Mills-to-RH reduction is one possible instance. Reverse RH-to-Yang–Mills
implications and equivalence claims are outside the paper's scope.

For a Euclidean construction, one possible formulation uses a preparation
\(A_L(f)\) supported at positive Euclidean time and the antilinear
reflection \(\Theta\):

\[
B_{M,L}(f,g)
=\big\langle(\Theta A_L(f))A_L(g)\big\rangle_M.
\]

Reflection positivity makes the diagonal nonnegative. Under the
appropriate full hypotheses, Osterwalder–Schrader reconstruction supplies
the positive Hilbert space and quantum theory
([1975 reconstruction theorem](https://doi.org/10.1007/BF01608978)).
The arithmetic coordinate \(x\) is not automatically Euclidean time;
the preparation and reflection must be defined. A graph or other
nonrelativistic model may instead use a direct Hamiltonian construction;
the full relativistic reconstruction theorem is not automatically
applicable to those settings.

The reduction would have mathematical content only when the model's
fields, action or Hamiltonian, couplings, adjoint/reflection, observable,
regularization and normalization are specified independently of an
assumed positive Weil kernel. Prime data may enter those definitions.
The complete boundary identity must then be derived from that dynamics.
Declaring the desired Weil distribution to be a covariance and asking
whether it is positive simply repeats the original criterion.

A conditional matching theorem must identify its hypotheses precisely:
for example, existence of a continuum limit, domain control of the
insertion, a boundary Ward identity, and the conditions that uniquely
determine its correlation function. Matching a formal perturbation
series alone does not establish the nonperturbative identity.
At present neither this model nor such a matching theorem has been
constructed; this is the intermediate research target.

There is also a narrower sufficient route. If independently positive
regulated models supply

\[
B_{\Lambda,L}(f,f)\geq0,\qquad
\lim_{\Lambda\to\infty}B_{\Lambda,L}(f,g)=Q_L(f,g)
\]

for every required pair and support, positivity passes to the finite
limit immediately. This would already prove the needed Weil positivity;
one need not first reconstruct every correlation function of a full
field theory. No uniform convergence rate over all inputs is needed for
this implication. The observables entering the regulated pairings must
retain their norm interpretation: an additive subtraction from their
pairing is not automatically positive.

Thus either an exact conditional matching theorem for a concrete field,
or convergence of its positive regulated observable sector, is a legitimate
milestone. Constructive estimates may be needed to establish the specified
model and limit. The research task remains fitting that model to the
arithmetic data, with its positivity supplied by the construction.


## 1b. Constructive plausibility and a possible Yang–Mills reduction

An interesting conditional reduction needs a credible reason to expect
that its hypotheses can hold. An already established construction is not
required. A theory with an open construction problem, including 4d
Yang–Mills, remains eligible when its desired properties have independent
support. The main selection criterion is the prospect of deriving the
complete Weil pairing.

A proposed field should explain the available evidence, which may include
a stable regulated model, a positive Hamiltonian or operator-algebraic
sector, physical unitarity, consistent dual descriptions, exact protected
observables, or a nearby established constructive theory. Comparisons
should identify actual differences in dimension, fields, interactions,
symmetries and ultraviolet behavior. No particular one of these forms of
evidence is mandatory for every candidate.

The conditional theorem must specify the construction properties needed
for its observable, including any renormalizations, limits and finite-norm
domains. These can remain open construction hypotheses. Their independent
motivation and the derived arithmetic matching identity must be explained
separately; prescribing the unknown Weil covariance is not such a
derivation.

Constructed stable polynomial scalar models in two spacetime dimensions
provide one useful comparison class
([Jaffe's account](https://arthurjaffe.com/Assets/pdf/CQFT.pdf)).
Yang–Mills provides a different example: positivity of lattice
approximations and a positive self-adjoint transfer matrix are established
in appropriate formulations
([Osterwalder–Seiler](https://doi.org/10.1016/0003-4916(78)90039-8)),
while the four-dimensional continuum existence and mass-gap problem
remains open
([Clay problem statement](https://www.claymath.org/millennium/yang-mills-the-maths-gap/)).
These examples motivate a concrete constructive comparison; resemblance
of terminology alone supplies no existence argument.

For the present gamma-and-prime proposal, the positive gamma action and
the individual conservative return graphs are useful established
ingredients within this project's stated scope. No joint arithmetic
junction action has yet been placed within a known constructive class.
That comparison is required before treating a conditional realization
as a physically supported conjecture.

A direct reduction from Yang–Mills to RH is conceivable in the following
precise sense. For a fixed compact simple gauge group, construct a
specified gauge-invariant insertion \(\mathcal O_L(f)\) in pure
four-dimensional Yang–Mills and prove

\[
Q_L(f,g)=
\langle\mathcal O_L(f)\Omega_{\mathrm{YM}},
       \mathcal O_L(g)\Omega_{\mathrm{YM}}\rangle
\]

for all required inputs and lengths, conditional on a precise
Yang–Mills construction. If that construction also supplies these
insertions and their finite-norm domains, its existence implies RH.
The mass gap is not needed for this norm-positivity implication.
Identifying a formal bulk field with a boundary insertion requires a
trace/domain argument; ordinary existence axioms do not automatically
construct every singular or extended insertion one might propose.

The construction hypotheses should state whether a mass gap is needed
for a particular continuum limit or boundary observable. The paper's
matching target is the positive state pairing above; each required
field-theory property must have an explicit role in the forward argument.

To invoke the actual Clay problem, the model must really reduce to pure
four-dimensional Yang–Mills. Adding arithmetic defects, infinitely many
extra fields, or supersymmetric matter creates further construction
obligations which a solution for pure Yang–Mills would not automatically
settle. Those extensions may still be useful constructive-QFT targets,
but the connection must be stated at the correct level.

At present a Yang–Mills mapping is a speculative research question.
No established reduction was identified in the targeted source check,
and no evidence of one has been derived here. A useful first result
would be an independently defined gauge-theory observable with a
nontrivial exact portion of the gamma/prime boundary response, followed
by an account of the full contact and pole sectors. The earlier
first-prime test remains a bounded construction test, not an RH
reduction on its own.


## 1c. Broaden the boundary to a defect or observable sector

The input may live on a line defect, a Wilson network, an interface, a
gluing cut, or an operator algebra acting on prepared states. The
arithmetic coordinate need not be physical Euclidean time, and no
codimension-one boundary is required by the norm-matching target.

The [broad defect-observable survey](DEFECT_OBSERVABLE_SURVEY.md) identifies
sphere quantization in 3d supersymmetric theories and Schur quantization
of 4d line operators as the leading new families to investigate. They
provide explicit shift actions, physical conjugations and trace identities;
selected related algebras also have independently proved positive forms.
Boundary Liouville gluing is an interacting alternative. These are model
selection leads, not established arithmetic matches.

The key unresolved step is a specified complex-linear map from arithmetic
test functions into the chosen positive sector whose entire pairing is
the Weil form. A lone position-independent insertion loses input data,
and a smooth local Euclidean two-point kernel cannot supply separated
prime-return atoms. Extended observables and nonlocal source maps remain
available. Conformal symmetry alone supplies neither the prime data nor
invariance under arbitrary changes of defect shape.


## 2. Fix the complete matching target

Use \(I_L=(-L/2,L/2)\), zero extension \(E_L\), and
\(V_d=E_L^*U_dE_L\), where \(U_dF(x)=F(x-d)\).
Let \(K_L\) be the compression of the positive gamma kinetic multiplier

\[
b_{1/4}(\tau^2)
=\sum_{n\geq0}\frac{2}{a_n}
       \frac{\tau^2}{a_n^2+\tau^2},
\qquad a_n=2n+\tfrac12.
\]

With \(c_L(x)=\cosh(x/2)\), \(s_L(x)=\sinh(x/2)\), and
\(w_0=\psi(1/4)-\log\pi\), the required form is

\[
W_L=K_L+w_0I+
2|c_L\rangle\langle c_L|-2|s_L\rangle\langle s_L|
-\sum_{m\log p<L}(\log p)p^{-m/2}
       (V_{m\log p}+V_{m\log p}^*).
\tag{3}
\]

The equality case \(m\log p=L\) contributes zero to these compressed
translations. These are form identities on the stated core; no boundedness
of the gamma operator is assumed.

At \(L=1\), the only prime term is
\(-(\log2)/\sqrt2\,(V_{\log2}+V_{\log2}^*)\).
This is the first complete fitting problem. The pieces to identify are:

| Boundary datum | What an exact bulk fit must determine |
|---|---|
| Gamma kinetic response | The complete multiplier and its form domain |
| Contact | The fixed constant \(w_0\), including every contact generated by a return channel |
| Poles | Both rank-one terms with their physical adjoints and normalization |
| Prime 2 | The translation atom at \(\log2\) and its coefficient |
| Other output | Exact absence or exact cancellation of unwanted terms in the full pairing |

The existing independently positive prime channels have compulsory
positive contacts. Subtracting those contacts from another component does
not by itself make a positive bulk model. More strongly, the
[candidate failures](../../brainstorm/candidate-bulk-theories/FAILURES.md)
exhibit a negative odd input for the gamma-plus-pole target with the prime
term deleted at \(L=1\). Thus a proposed positive family cannot require
its zero-prime member to realize that same fixed prime-deleted target.
Its bare source, contacts and pole couplings may have to vary together;
only the physical arithmetic parameter values must fit (3).
This is a constraint on interpolation, not permission to change the
target's contact arbitrarily.

## 3. A reason to leave finite rational feedback

Here is a model obstruction, rather than another estimate on its error.

**Proposition.** Let \(A_0\) be a closed source into a positive Hilbert
space, with \(T=A_0^*A_0>0\) and infinitely many distinct eigenvalues.
Consider finitely many output channels of the form

\[
A_{\mathrm{rat}}f
=\big(A_0r_1(T)f,\ldots,A_0r_m(T)f,\,
       s_1(T)f,\ldots,s_k(T)f\big),
\tag{4}
\]

where every \(r_j,s_\ell\) is a rational function with complex
coefficients, finite at the eigenvalues of \(T\). Interpret the formula
at least on finite linear combinations of eigenvectors. A positive
constant metric among the \(A_0r_j\) channels, or among the \(s_\ell\)
channels, can be absorbed into these functions.
For any \(\alpha>0\), this class cannot satisfy

\[
\|A_{\mathrm{rat}}f\|^2
=\langle f,(T-\alpha I)f\rangle
\tag{5}
\]

on all the eigenvectors, even when \(T-\alpha I\) is positive on its
actual spectrum.

**Proof.** On an eigenvector of eigenvalue \(\lambda\), (5) says

\[
\lambda\sum_j|r_j(\lambda)|^2
       +\sum_\ell|s_\ell(\lambda)|^2=\lambda-\alpha.
\tag{6}
\]

For a rational function \(r\), define
\(r^\#(z)=\overline{r(\bar z)}\); it is again rational.
The left side of (6) extends to
\(R(z)=z\sum_jr_j(z)r_j^\#(z)+
\sum_\ell s_\ell(z)s_\ell^\#(z)\).
Clearing denominators, equality at infinitely many distinct eigenvalues
forces the rational identity \(R(z)=z-\alpha\).
Choose a real \(x\) with \(0<x<\alpha\) outside the finite pole set.
Then \(R(x)\geq0\) by its sum-of-squares representation, whereas
\(x-\alpha<0\). This is a contradiction. \(\square\)

The argument does not require a finite accumulation point of eigenvalues:
a nonzero polynomial has only finitely many roots. It applies to the
compact-resolvent reference used in the existing feedback construction.
Finite cascades of scalar rational filters of the same reference operator
remain in this class.

For the particular one-channel filter already used there,

\[
\lambda\left(1-\frac{\kappa}{\lambda+\mu}\right)^2
=\lambda-2\kappa+
\frac{2\kappa\mu}{\lambda+\mu}
+\frac{\kappa^2\lambda}{(\lambda+\mu)^2}.
\tag{7}
\]

The last two terms are the positive excess for
\(\lambda,\kappa>0,\ \mu\geq0\).
The proposition says that adding finitely many positive rational
channels cannot remove an exact constant in this reference-only class.
It turns the unsuccessful fit into a stopping criterion.

This is not an obstruction to every finite-field model, every feedback
law, or the full Weil realization. Continuum dynamics can produce
nonrational response functions; couplings can use operators other than
functions of \(T\); an independently proved geometric gap can lead to a
different positive energy. Infinite channel families and agreement on
only finitely many inputs are also outside the proposition.
No claim of literature priority is made for this elementary argument.

## 4. An exact operation on the positive gamma bulk

There is an available bulk operation worth testing before adding another
independent prime channel. It refines the existing gamma fields.

For \(\alpha>0\), set \(a_n(\alpha)=2(n+\alpha)\) and

\[
b_\alpha(s)=\sum_{n\geq0}\frac{2}{a_n(\alpha)}
                         \frac{s}{a_n(\alpha)^2+s}.
\]

On the line, the positive action is

\[
\mathcal E_\alpha(F,\{u_n\})
=\sum_{n\geq0}\frac{2}{a_n(\alpha)}
 \left(\|F-u_n\|^2+a_n(\alpha)^{-2}\|u_n'\|^2\right).
\tag{8}
\]

For smooth compactly supported \(F\), minimizing the fields gives
\(u_n=a_n(\alpha)^2(a_n(\alpha)^2-\partial_x^2)^{-1}F\) and

\[
\inf_u\mathcal E_\alpha(F,u)
=\frac{1}{2\pi}\int_{\mathbb R}
b_\alpha(\tau^2)|\widehat F(\tau)|^2\,d\tau.
\tag{9}
\]

The infinite action is a sum of nonnegative terms. One may use finite
towers followed by monotone convergence, or substitute the componentwise
minimizers. The divergent bare sum
\(\sum_n2\|F\|^2/a_n\) must never be separated from its compensating fields.
The finite-energy domain is the one specified by this sum and (9).

Let \(p\geq2\) be an integer and \(\alpha_j=(\alpha+j)/p\).
Reindexing \(n=pm+j\) gives the exact identity

\[
\boxed{\quad
b_\alpha(s)=\frac1p\sum_{j=0}^{p-1}
                    b_{\alpha_j}(s/p^2).
\quad}
\tag{10}
\]

This is a positive identity before eliminating any field. Indeed, define
the unitary coordinate dilation \(D_pF(x)=p^{-1/2}F(x/p)\).
Then \(\|(D_pu)'\|=p^{-1}\|u'\|\), and

\[
\mathcal E_\alpha(F,\{u_n\})
=\frac1p\sum_{j=0}^{p-1}
 \mathcal E_{\alpha_j}
 \big(D_pF,\{D_pu_{pm+j}\}_{m\geq0}\big).
\tag{11}
\]

The \(1/p\) weights are fixed by the action, and the corresponding
residual-output inclusion has normalization \(p^{-1/2}\).
This alone does not identify that inclusion with a physical prime return
amplitude.

For the Riemann gamma tower, the first two refinements are

\[
b_{1/4}(s)=\tfrac12b_{1/8}(s/4)+\tfrac12b_{5/8}(s/4),
\tag{12}
\]

\[
b_{1/4}(s)=\tfrac13\big(
b_{1/12}(s/9)+b_{5/12}(s/9)+b_{3/4}(s/9)\big).
\tag{13}
\]

Refining by 2 and then 3, or by 3 and then 2, produces the same six
branches, up to permutation:
\(\{1,5,9,13,17,21\}/24\), with dilation \(D_6\) and weights \(1/6\).
In general the residue label \(j+pk\) and \(D_qD_p=D_{pq}\) give exact
composition for integers \(p,q\).

The associated contact identity is also explicit. Put
\(m_\alpha(\tau)=\Re\psi(\alpha+i\tau/2)-\log\pi\).
The classical Gauss multiplication formula gives

\[
m_\alpha(\tau)=\log p+
\frac1p\sum_{j=0}^{p-1}m_{\alpha_j}(\tau/p).
\tag{14}
\]

Subtracting (14) at \(\tau=0\) gives (10).
Formula (14) is not a decomposition into positive complete gamma forms:
only the kinetic \(b_\alpha\) actions above have the asserted positivity.
The \(\log p\) contact is a fixed normalization identity, not a freely
spendable positive budget.

The multiplication formula is classical
([NIST DLMF, 5.5.9](https://dlmf.nist.gov/5.5.E9)).
Gamma-factor splitting is already used in the semilocal literature
([Connes–Consani, §4.3](https://arxiv.org/html/2008.10974v1)).
The present use is an explicit positive-action version and a proposed
interface to the existing return models; it is not a novelty claim for
gamma splitting or a completed arithmetic coupling.

## 5. A common-field model family to test

The independently positive return graph in
[note 16](../arithmetic-ground-state-geometry/notes/16_PRIME_RETURN_CHANNELS.md)
has a sum of edge energies and conservative vertex conditions. It
produces the required geometric repetition mechanism, but an independent
output adds a compulsory positive contact.

A more appropriate next ansatz is to let conservative junctions act on
the refined gamma fields themselves. Its specified ingredients should be:

1. The common positive action (8), organized by the exact refinements (11).
2. Positive graph edge energies with conservative, self-adjoint junction
   conditions, attached to these same fields.
3. One boundary preparation and physical readout, with the pole coupling
   included in the same matching problem.

The positivity must be checked from the joint action or state-space
construction before comparing its boundary operator with (3).
The theory's mass labels, junction maps, and source normalization must be
given explicitly. This is a proposed family, not a constructed fit.

Refinement or a unitary rotation of all the existing outputs preserves
their norm exactly and cannot introduce a prime term. A successful
junction must change the admissible bulk fields, the preparation, or
the observed subspace in a physically specified way. The contact and
the prime interference would then be determined together.
The finite rational proposition does not cover the whole proposed
family; it also does not prove that the family can succeed.

There are three immediate issues which the refinement alone does not
resolve:

- It exists for every positive integer. It does not select primes.
- Its coordinate dilation by \(p\) is not the additive translation by
  \(\log p\) in (3). A junction must derive the required relation, not
  identify the two operations.
- Commuting refinements give consistent mass labels, but they do not
  automatically cancel unwanted mixed return histories or fix their
  coefficients.

Even the matching \(p^{-1/2}\) normalization is only a clue: overlap of
one selected branch with a normalized uniform \(p\)-branch state has
that value, but the physical injection and return rule have yet to be
derived. Selecting such a state by hand does not complete the mechanism.

## 6. The next calculations should decide the model

The [first preparation tests](GAUGE_TRANSFER_TEST.md) now give concrete
constraints: direct orthogonal branching introduces an extra cusp at the
prime delay; a coherent repair cancels the cusp but has zero Hermitian
interference with the gamma source and leaves the independent contact.
The next junction must solve both issues in its full physical pairing.

The next bounded target is a fully specified conservative junction for
the two branches in (12), with its complete boundary pairing at \(L=1\).
Compute the pairing exactly and compare it with (3). Identify its contact,
prime atom, pole terms and any continuous response. A mismatch should
identify a parameter identity to solve or a reason to alter the family.
It should not automatically initiate a residual-norm estimate.

Then check repetition at \(L=3/2\), where the required prime-2 coefficient
at \(\log4\) is \((\log2)/2\), and compatibility of primes 2 and 3 at
\(L=5/4\). The latter must account for unwanted differences such as
\(\log(3/2)\), which are not prime powers in (3). At \(L=3/2\), prime 3
is also active and cannot be discarded in a claim about the complete
form. A one-prime return identity may be tested separately as a
component identity.

The rank-one poles and contacts need not be positive separately. They
must arise as part of the complete pairing of an independently positive
system. Similarly, an exact cancellation proved by a junction identity
is useful; an assertion that the leftover operator is small merely
returns to the previous program.

## 7. What this continuation establishes

The established outputs here are a scoped obstruction to finite rational
reference feedback and an exact refinement of an independently positive
gamma action. The rational argument rules out one route to fitting the
contact. The refinement supplies explicit common bulk fields, fixed
normalizations, and compatible integer operations on which another
coupling can be tested.

These are model-selection results and construction ingredients. They do
not establish the full Weil identity, remove the finite-response
conjecture, or demonstrate a new all-length positivity mechanism.
The next substantive advance would be a positive junction model whose
complete first-prime boundary pairing can be derived and matched.

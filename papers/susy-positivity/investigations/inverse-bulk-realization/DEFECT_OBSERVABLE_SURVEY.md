# Defect observables and candidate fields for an exact Weil pairing

14 September 2026. Broad literature search and research-direction assessment.

The leading new direction is **sphere quantization of protected operator
algebras in three-dimensional supersymmetric theories, together with the
related Schur quantization of line operators in four dimensions**. These
frameworks combine explicit operator actions, equations constraining the
pairing, and a physical interpretation of its positivity. Boundary
Liouville theory is the strongest alternative found for studying exact
interacting gluing amplitudes. Free-field constructions remain useful
controls for testing an arithmetic source map quickly.

This recommendation concerns prospects for **exact matching**, not the
probability of proving RH. No source examined supplies the complete Weil
norm identity. The search supports a more concrete choice of observables
and model families; it has not established a new arithmetic identity.

An already completed construction is **not an eligibility requirement**.
The intended paper can prove that construction of a specified, credible
field theory with stated properties would imply RH. Credibility should
come from independent physics or mathematics, such as a stable regulated
model, unitarity, consistent dual descriptions, exact protected data, or
nearby constructive results. Four-dimensional Yang–Mills remains an
eligible comparison. Existing construction theorems are supporting
evidence and useful controls, rather than the selection criterion.

## 1. What a candidate must match

Let \(I_L=(-L/2,L/2)\), let \(F=E_Lf\) denote zero extension, and put
\(U_dF(x)=F(x-d)\). The target is

\[
\begin{split}
Q_L[f]={}&\frac1{2\pi}\int_{\mathbb R}
b_{1/4}(\tau^2)|\widehat F(\tau)|^2\,d\tau
w_0\|f\|^2\\
&+2\left|\int_{I_L}f(x)\cosh(x/2)\,dx\right|^2
-2\left|\int_{I_L}f(x)\sinh(x/2)\,dx\right|^2\\
&-2\sum_{m\log p<L}(\log p)p^{-m/2}
\operatorname{Re}\langle F,U_{m\log p}F\rangle,
\end{split}
\]

where

\[
b_{1/4}(s)=\sum_{n\geq0}\frac{2}{a_n}\frac{s}{a_n^2+s},
\qquad a_n=2n+\tfrac12,
\qquad w_0=\psi(\tfrac14)-\log\pi.
\]

The matching statement is a single physical state pairing

\[
\langle\Phi_{M,L}(f),\Phi_{M,L}(g)\rangle_M=Q_L(f,g)
\quad(f,g\in C_c^\infty(I_L)),
\]

with \(\Phi_{M,L}\) complex linear and defined by independently specified
model data. It must include the normalization, both pole contributions,
and every active prime power. It must work compatibly as the support
grows. At fixed \(L\) the prime sum is finite; no Euler product on the
critical line is being assumed.

The logical target is

\[
\text{construction of }M\text{ with the specified positive observable sector}
\quad\Longrightarrow\quad Q_L\geq0\text{ for every }L
\quad\Longrightarrow\quad\mathrm{RH}.
\]

The exact identity may be proved conditionally on construction. Its
construction hypotheses must not simply assume the sought arithmetic
correlator or an RH-equivalent positivity condition. A mass gap is only
needed if a particular observable or limit uses it; positivity of the
norm itself does not require a gap. These conventions continue the
[current analysis](ANALYSIS.md).

There is also no requirement that the arithmetic variable be a spacetime
coordinate. A line, an interface, a cut along which amplitudes are glued,
or an operator algebra acting on prepared states can carry the input.
Changing this interpretation is a substantive part of model selection.

## 2. Comparison of theories and observables

The ordering gives research priority for the present matching problem.
Construction status and calculability are separate considerations.

| Family | Observable to investigate | Evidence for the required properties | Matching opportunity and missing step |
|---|---|---|---|
| **3d \(\mathcal N=4\) sphere quantization** | Higgs/Coulomb operator families; monopole and vortex insertions; hemisphere states | Physical reflection positivity; explicit localization; rigorous positive-trace results for substantial algebraic subclasses | Shift actions and trace identities constrain one common pairing. Need an arithmetic source map and compatible prime operations. |
| **4d \(\mathcal N=2\) Schur quantization** | Half-BPS Wilson–'t Hooft line operators, their products, and interface kernels | Credible supersymmetric theories; protected formulas; mathematical positive-form classifications in selected examples | Multiplicative difference operators and line algebras are natural candidates for repeated arithmetic operations. Their physical variables are not automatically prime translations. |
| **Boundary Liouville CFT** | Boundary vertex insertions and states prepared on surfaces with cuts; reflected gluing amplitudes | Constructed probabilistic theory, proved structure constants, and boundary gluing/Hamiltonian results in stated regimes | Exact interacting amplitudes and analytic identities offer a controlled setting for fitting. No prime correspondence or full Weil source is known. |
| **Free bosonic or fermionic fields with arithmetic defect data** | Linear fields, centered fermion bilinears, particle–hole states, or constrained boundary energies | Direct Gaussian/Fock constructions once the one-particle dynamics and domains are specified | Best inexpensive test of a proposed source. The arithmetic geometry and common normalization must be derived, not assigned as the Weil covariance. |
| **Integrable QFT in \(1+1\) dimensions** | Boundary/defect-changing fields, transmission operators, and bilocal preparations | Constructed bulk models in specified classes; exact boundary scattering and form-factor methods | Rich exact dynamics and repeated transmission. Need the actual state pairing, its domains, and a construction hypothesis covering the chosen defect. |
| **4d \(\mathcal N=4\) Wilson defects; pure YM networks** | Gauge-invariant insertions, junctions and extended networks, rather than just a single local insertion | Strong physical motivation; protected data in the supersymmetric case; regulated gauge-theory controls | Remain eligible. The simplest line correlators lack the arithmetic structure; networks require a more explicit matching mechanism. |
| **2d Yang–Mills** | Wilson networks and transfer states with electric-flux insertions | Rigorous continuum Wilson functionals and Hamiltonian formulation | Excellent gauge/gluing control. The literal winding prescription already fails the required repetition law. |
| **Fields on hyperbolic or arithmetic spaces; quantum graphs** | Scattering-channel states, boundary fluxes, and return observables | Positive self-adjoint one-particle models; explicit trace/scattering formulas | Closest established geometric access to zeta functions and primitive returns. Resonances and relative traces still need conversion to the full positive pairing. |
| **Schwarzian quantum mechanics** | Smeared bilocal observables and their spectral matrix elements | Exact spectral/correlation formulas and a concrete boundary quantum-mechanical description | Useful nonlocal and gamma-function control. It is not by itself a constructed higher-dimensional QFT, and its known spectral measure is not the Weil measure. |
| **\(P(\phi)_2\) and related stable scalar theories** | Line restrictions where defined, composite insertions, and specified interfaces | Established constructive examples and positive regulated models | Useful evidence for an interacting extension. Standard local correlators supply no particular arithmetic matching identity. |
| **\(p\)-adic/tree fields and Bost–Connes systems** | Multiplicative correspondences, transfer operators and arithmetic states | Explicit local-factor and operator-algebra constructions, with model-dependent positivity qualifications | Valuable arithmetic ingredients. The global physical pairing, real adjoint, normalization and pole terms remain unresolved. |

The source discussion below gives the basis and limitations of these
judgments. A low-dimensional theory is not preferred merely because it
has been constructed, and a four-dimensional theory is not downgraded
merely because its construction is open.

## 3. The main lead: protected operator algebras with a positive pairing

### 3.1 A close realization of the proposed line inside a sphere

In 3d \(\mathcal N=4\) theories, twisted Higgs-branch insertions on a line
or great circle form a protected one-dimensional operator algebra.
Localization gives a one-dimensional Gaussian model coupled to a matrix
integral. This is an established way to extract line data from a
higher-dimensional interacting theory.
[Dedushenko–Pufu–Yacoby](https://arxiv.org/abs/1610.00740)

For abelian Coulomb branches, monopole insertions act as explicit shifts
on hemisphere wavefunctions. Gluing the two hemispheres gives sphere
correlators. The published construction includes the ordering and
conjugation rules. Its raw gluing expression is a bilinear form; the
physical conjugation must be restored before treating it as a norm.
[Dedushenko–Fan–Pufu–Yacoby, §§4–5](https://arxiv.org/html/1712.09384)

Sphere quantization organizes these data as

\[
H_T(a,b)=T(\rho(a)b),\qquad H_T(a,a)>0,
\]

where \(T\) is a positive twisted trace and \(\rho\) is the specified
antilinear operation. Completing the operator algebra gives a Hilbert
space. Left and right multiplication carry the physical adjoint
relations on the algebraic domain. This gives precisely the kind of
observable-sector formulation needed here.
[Gaiotto, §§1.1 and 2](https://arxiv.org/html/2307.12396)

**Proposed use.** Construct an independently defined linear map
\(f\mapsto a_{S,L}(f)\) into this Hilbert completion and compute
\(H_T(a_{S,L}(f),a_{S,L}(g))\). The arithmetic label may enter through
operator coefficients, a spectral transform, or a specified defect
network. Positivity then belongs to the physical pairing; the unresolved
task is its exact pullback to the arithmetic inputs.

This proposal is more specific than choosing an interacting potential:
the algebra, conjugation and trace identities constrain the answer
together. It also allows a conditional theorem for a credible 3d theory
without requiring its entire constructive treatment first.

### 3.2 Independent mathematical results make the proposal testable

There are rigorous classifications of positive Hermitian forms on
quantizations of type-A Kleinian singularities. These are explicit
infinite-dimensional algebras related to the protected sectors above,
with generators satisfying

\[
[z,u]=-u,\quad [z,v]=v,\quad
vu=P(z-\tfrac12),\quad uv=P(z+\tfrac12).
\]

The positive traces have integral descriptions with stated restrictions
on the polynomial and conjugation. This supplies a constrained family
of positive metrics to investigate.
[Etingof–Klyuev–Rains–Stryker, §§2–4](https://arxiv.org/html/2009.09437)

A further theorem proves positivity of the Higgs-branch trace under
explicit assumptions: a conical pair, flat moment map, and trivial mass
and FI parameters. The paper does not assert positivity for arbitrary
parameter deformations.
[Gaiotto–Hilburn–Redondo-Yuste–Webster–Zhou, Theorem 1.2](https://arxiv.org/html/2308.15198)
A 2025 preprint reports a classification for all abelian Coulomb
branches; this survey uses it as a recent research lead, not a substitute
for checking the hypotheses of any selected example.
[Klyuev](https://arxiv.org/abs/2510.25021)

These theorems establish positivity of particular algebraic sectors.
They do not constitute a constructive existence theorem for every
associated 3d field theory. For the arithmetic implication, however, an
independent positive sector plus a complete matching identity would
already suffice. The relation to a full field theory would then be an
additional mathematical-physics interpretation.

**First examples to examine:** the free-hypermultiplet Weyl algebra as a
normalization control; a rank-one type-A quantization associated with
the \(T[SU(2)]\)/abelian gauge-theory examples; and then abelian quivers
whose trace and adjoint can be written explicitly. Selecting a trace
from a classified positive family is useful only when its parameters
and source have independent model definitions.

### 3.3 The four-dimensional extension is particularly relevant

Schur quantization uses protected half-BPS line correlators in 4d
\(\mathcal N=2\) theories to construct a Hilbert space for a doubled
operator algebra. It includes difference-operator realizations and
interface kernels. The \(SU(2)\), \(N_f=4\) theory, described by a
four-punctured sphere in class \(\mathcal S\), is a concrete example.
The treatment distinguishes physical reflection positivity from
positivity of a twisted theory; its general nonconformal extension has
an additional unresolved positivity argument.
[Gaiotto–Teschner, §§1–3 and 5](https://arxiv.org/html/2406.09171)

Generalized \(q\)-Weyl algebras also have rigorous positive-form
classifications. Their defining relations include

\[
ZuZ^{-1}=q^2u,\qquad ZvZ^{-1}=q^{-2}v,
\qquad uv=P(q^{-1}Z),\qquad vu=P(qZ),
\]

with \(0<q<1\) in the positive-real regime studied. Their Hermitian
structure is part of the data, not a free choice after fitting.
[Klyuev, §§1, 3–4](https://arxiv.org/pdf/2105.12652)

**Research inference.** Multiplicative shifts are closer to the required
arithmetic operations than position independence of a lone local field.
For example, substituting \(q=p^{-1/2}\) in the algebraic relation gives
a factor \(p^{-1}\). This observation is only a possible label for a
one-prime test: it does not identify a physical shift with
\(U_{\log p}\), give \((\log p)p^{-m/2}\), or supply the Weil contact.
The actual real structure and an explicit intertwining map are required.

A single deformation parameter also does not automatically encode all
primes. If a proposal only generates lengths in the integer span of
finitely many fixed lengths, unique factorization prevents it from
producing every \(\log p\). An enlarged operator algebra or compatible
family over prime sets would have to perform that task. This is the
existing [charge-rank selection issue](../../brainstorm/theory-landscape-20260913/SELECTION_TESTS.md),
not a general exclusion of these theories.

## 4. Other serious candidates

### 4.1 Boundary Liouville: exact interacting gluing

Liouville theory supplies a probabilistic realization of Segal gluing
and a bootstrap description of amplitudes in terms of spectral and
structure-constant data.
[Guillarmou–Kupiainen–Rhodes–Vargas](https://arxiv.org/abs/2112.14859)
Boundary three-point and bulk–boundary structure constants, including
the boundary reflection coefficient, have been derived rigorously.
[Ang–Remy–Sun–Zhu](https://arxiv.org/abs/2305.18266)

Boundary amplitudes on surfaces with corners admit proved gluing rules;
annuli and half-annuli generate self-adjoint Hamiltonians. The cited
boundary paper separates these results from a companion spectral and
bootstrap program, listed there as in preparation. We do not treat that
companion as a checked theorem. Finite-norm insertion amplitudes require
the stated charge bounds, and annular semigroups need not be
Hilbert–Schmidt.
[Guillarmou–Rhodes–Wu, Theorem 1.1 and §7](https://arxiv.org/html/2408.13133)

**Observable:** a state prepared by a specified surface with boundary
insertions, paired with its reflected conjugate across a cut. Smearing
an insertion gives linear dependence on the arithmetic input, provided
the required domain is established. The interacting amplitude can be
quadratic in that input even though its dynamics are nonlinear.

**Why pursue it:** exact sewing and analytic identities could constrain
the complete boundary response. Exponential interactions also provide
a more developed field-theory relative of the earlier Morse/gamma
models. **What remains absent:** a derived prime action and the
arithmetic source. Gamma or double-gamma functions in a structure
constant are not yet the digamma kinetic term of \(Q_L\).

This is a noncompact conformal theory. We should formulate the proposed
observable using normalizable prepared states, rather than assume the
massive-vacuum setting of pure YM. A raw boundary reflection amplitude
or its logarithmic derivative also has no automatic norm positivity.

### 4.2 Integrable boundary and defect theories

Lechner constructs interacting massive bulk theories from a specified
regular class of factorizing S-matrices, including the sinh-Gordon
example, with local observables and scattering completeness.
[Lechner](https://arxiv.org/abs/math-ph/0601022)
Boundary integrability supplies exact reflection data, with the Ising
boundary magnetic field and boundary sine-Gordon among the standard
examples.
[Ghoshal–Zamolodchikov](https://arxiv.org/abs/hep-th/9306002)

**Observable:** a defect-changing operator or a bilocal state preparation
whose form factors can be evaluated. A spectral norm can schematically
take the form

\[
B(f,g)=\sum_n\int d\mu_n(\boldsymbol\theta)\,
\overline{\mathcal F_{n,f}(\boldsymbol\theta)}
\mathcal F_{n,g}(\boldsymbol\theta).
\]

This is useful only when the amplitudes and positive measures are
derived from the theory and the sum defines the proposed observable.
An exact scattering matrix alone does not give this correlator. Bulk
construction results do not automatically cover an added defect or a
new infinite family of arithmetic couplings.

These remain credible conditional targets even where the defect
construction is open. Their weakness relative to the leading operator
algebras is the current lack of an identified arithmetic action, not
the incompleteness of construction.

### 4.3 Four-dimensional Wilson defects and gauge networks

The \(\mathcal N=4\) Wilson-line literature supplies exact protected
operator norms and structure constants of arbitrarily large operator
length. Localization on \(S^4\) provides the surrounding framework.
[Giombi–Komatsu](https://arxiv.org/abs/1802.05201),
[Pestun](https://arxiv.org/abs/0712.2824)
Generic contour deformations still change correlators through the
displacement operator.
[Correa–Henn–Maldacena–Sever](https://arxiv.org/abs/1202.4455)

**Observable:** an extended gauge-invariant network or an infinite
family of line insertions with a specified arithmetic preparation.
The protected operator algebra is more useful for this task than the
ordinary two-point function of one fixed primary.

Pure 4d YM remains fully eligible under the user's conditional standard.
It would move up the ranking immediately if a loop equation, gluing
identity or specified network gave better access to the full Weil
pairing. Its open construction problem is not an objection. At present,
the supersymmetric cases offer more explicit identities with which to
attempt the matching. Neither a general Wilson expectation nor an
arbitrary normalized loop insertion ratio is automatically a positive
Gram form; the reflection/state preparation must be specified.

### 4.4 Two-dimensional Yang–Mills

Rigorous continuum Wilson functionals and their Hamiltonian
interpretation are known. The theory also has actual area-preserving
deformation invariance, which is a useful control for the user's
universality idea.
[Ashtekar–Lewandowski–Marolf–Mourão–Thiemann](https://arxiv.org/abs/hep-th/9605128)

Wilson networks and electric-flux insertions can be tested with exact
heat-kernel gluing. The [previous calculation](GAUGE_TRANSFER_TEST.md)
already distinguishes repeated transfer from repeated winding and rules
out a particular scalar winding assignment. It does not rule out all
network observables. A new test should change the observable in a
specified way and compute its complete pairing.

### 4.5 Hyperbolic geometry and quantum graphs

Arithmetic hyperbolic scattering has a genuine zeta connection. For the
modular example, the scalar scattering factor is

\[
C(s)=\frac{\Lambda(2s-1)}{\Lambda(2s)},
\qquad \Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

The same construction relates scattering to boundary
Neumann-to-Dirichlet data.
[Levitin–Strohmaier, §§5 and 7](https://arxiv.org/html/1812.05554)

**Implication for selection:** a free field on such an independently
defined geometry would inherit positive one-particle dynamics. But the
zeta zeros enter as scattering resonances at \(s=\rho/2\), not as an
already self-adjoint spectrum of their imaginary parts. Unitarity on
\(\operatorname{Re}s=1/2\) does not locate all those resonances on
\(\operatorname{Re}s=1/4\). Thus this known identity is a useful
arithmetic control, not a concealed proof of RH.

Quantum graphs can reproduce the oscillatory prime contribution with
its sign while having a different smooth density and different spectrum.
[Kuipers–Hummel–Richter](https://arxiv.org/abs/1307.6055)
They remain useful for **state**, **flux**, or **particle–hole**
observables. Matching an orbit trace is insufficient for the full norm.

### 4.6 Schwarzian, scalar and arithmetic controls

Schwarzian quantum mechanics has exact bilocal correlation functions
with explicit spectral integrals and gamma-function matrix elements.
[Mertens–Turiaci–Verlinde](https://arxiv.org/abs/1705.08408)
It is a tractable test of extended boundary observables. Neither its
known spectral measure nor a JT gravitational partition function can
simply be identified with the Weil pairing. Its use here is as a
concrete quantum-mechanical control or as part of an explicitly stated
field-theory realization.

Stable \(P(\phi)_2\) models have constructive treatments with reflection
positivity and Euclidean symmetry.
[Duch–Dybalski–Jahandideh](https://arxiv.org/abs/2311.04137)
They provide evidence for possible interacting defect constructions,
but choosing a stable polynomial interaction does not supply a
preferred arithmetic observable.

Bruhat–Tits-tree bulk models produce boundary correlators expressed
through local zeta factors.
[Gubser–Knaute–Parikh–Samberg–Witaszczyk](https://arxiv.org/abs/1605.01061)
Construction and positivity must be assessed model by model: one
interacting \(p\)-adic Euclidean construction explicitly leaves
reflection positivity unproved.
[Arroyo-Ortiz–Zúñiga-Galindo](https://arxiv.org/abs/1810.01408)
These theories are useful sources of arithmetic geometry; Euclidean
existence alone is not evidence for the particular real Hilbert pairing
we require.

Bost–Connes supplies a positive operator-algebraic statistical system
with logarithmic arithmetic energies and a zeta partition function.
[Bost–Connes](https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/CONNES/1994-1998/M_95_38/M_95_38_web.pdf)
For \(H|n\rangle=\log n|n\rangle\), the Gibbs trace
\(\sum n^{-\beta}\) converges for \(\beta>1\). This does not preclude
algebraic KMS states elsewhere; it prevents using that same normalized
Gibbs formula at \(\beta=1/2\). A partition derivative still needs an
independent identity to become the desired covariance or state norm.

## 5. Three observable-level checks

These are structural selection checks, not a program of estimating
increasingly complicated residuals.

### 5.1 A plain local line correlator cannot carry prime-return atoms

The target kernel has nonzero delta distributions on

\[
x-y=\pm m\log p.
\]

The gamma and pole kernels are smooth at these nonzero separations and
cannot remove those atoms. Therefore a candidate whose kernel is smooth
at every separated pair cannot match once a prime is active. A smooth
coordinate change and smooth local source weights do not fix this.
This is the existing
[separated-return selection test](../../brainstorm/theory-landscape-20260913/SELECTION_TESTS.md).

It excludes the straightforward use of a fixed local primary on a
homogeneous Euclidean line, under that regularity assumption. It does
not exclude Lorentzian observables, correspondences, quotient geometry,
networks, bilocals, or a nonlocal map from arithmetic inputs into the
operator algebra. The broadened boundary viewpoint is useful precisely
because it allows those possibilities.

### 5.2 Protection must leave enough input dependence

Suppose one fixed protected insertion, on an ordered preparation
region, represents the same vector \(v\) at every position. Then

\[
\Phi(f)=\left(\int f\right)v,
\qquad \|\Phi(f)\|^2=\left|\int f\right|^2\|v\|^2.
\]

This rank-one pairing cannot equal the closed, infinite-rank Weil
form. The same conclusion holds for a fixed finite family of such
prepared vectors. This is a deduction under the stated preparation
assumption, not a claim that every topological sector has finite rank.
Ordering effects, contact distributions, infinitely many operator
labels, and different source maps require separate analysis.

Thus the most promising protected construction encodes \(f\) in an
infinite operator family or a genuine state-preparation transform.
Position independence can simplify that calculation, but it cannot be
allowed to erase the arithmetic input.

### 5.3 Fermion bilinears offer a concrete alternative positive observable

Free fields are worth retaining because their observables need not be
linear in the elementary field. A centered fermion bilinear can be
linear in \(f\) while automatically combining positive and negative
terms through the same state.

Take a gauge-invariant quasi-free CAR state with one-particle occupation
operator \(0\leq C\leq I\). This is a standard independently positive
construction.
[Dierckx–Fannes–Pogorzelska, §IV](https://arxiv.org/html/0709.1061)
For finite-rank \(A_f\), complex linear in \(f\), define

\[
J(f)=d\Gamma(A_f)-\operatorname{Tr}(CA_f)I.
\]

Wick's rule gives the standard identity

\[
\begin{split}
\omega_C(J(f)^*J(g))
&=\operatorname{Tr}\big(CA_f^*(I-C)A_g\big),\\
\omega_C(J(f)^*J(f))
&=\|(I-C)^{1/2}A_fC^{1/2}\|_{\mathrm{HS}}^2.
\end{split}
\]

The subtraction here centers the observable before taking its norm;
it is not an arbitrary subtraction from a previously positive pairing.
For an infinite-dimensional extension, the displayed Hilbert–Schmidt
condition is required **for each input**, together with the existence
of the centered observable or its state limit. It does not require the
whole source map from \(L^2(I_L)\) to states to be Hilbert–Schmidt.

**Proposed test:** choose \(C\) and \(A_f\) from independently defined
arithmetic scaling/projection data and compute the full covariance.
First check whether it merely reproduces the canonical semilocal
pairing already examined. If it does, the fermionic interpretation
alone adds no matching progress. If it differs, its complete exchange,
contact and pole terms must be calculated. The formula is a standard
observable template, not a new theorem or a claimed Weil realization.

For comparison, a Gaussian field with covariance \(C_M\) and source
\(J_f\) gives \(\langle J_f,C_MJ_g\rangle\).
[Sheffield](https://arxiv.org/abs/math/0312099)
A positive boundary energy may instead involve the inverse boundary
covariance or a Dirichlet-to-Neumann operator. Those are different
observables. Declaring either one to be \(Q_L\) would bypass the required
derivation.

## 6. A bounded next investigation

**First priority: protected line algebras and their state pairings.**
Start with one rank-one sphere example and one multiplicative Schur or
\(q\)-Weyl example. Use the published trace, its real structure, and a
fixed parameter regime. Specify a source map before introducing extra
couplings. Work out whether its variables can represent arithmetic
translations through an actual intertwining relation. A formal
similarity of shift notation is insufficient.

**Alternative investigation: Liouville gluing.**
Identify a normalizable preparation with one smeared boundary insertion
or a specified extended insertion. Compute its pairing using the
available gluing and structure constants. Test whether the gamma
response is actually the required digamma form, including its
normalization, before searching for arithmetic sewing operations.
This is a separate model family; tensoring its positive amplitudes onto
an existing arithmetic model would not by itself change that model's
pairing.

For any candidate that passes the source and adjoint check, use the
existing short-window tests:

1. \(L=1\): the complete target with prime 2, contact and both poles.
2. \(L=5/4\): primes 2 and 3; retain any unwanted mixed histories.
3. \(L=3/2\): include the repeated-2 contribution at \(\log4\).

A one-prime repetition identity should also be checked independently
of the short-window truncation. Success on these windows is only a
model-selection milestone. The final theorem needs a uniform rule and
compatibility of the input pairings when prime sets and support grow.

If exact identities exclude a proposed source, change the model or the
source. Do not automatically retain it and begin estimating its
remainder. Conversely, a credible field theory with an open construction
problem should remain under consideration if it gives a better exact
matching mechanism.

The deliverable after this survey should be a **specified conditional
matching problem**: model, observable, physical reflection/adjoint,
normalization, domain, construction hypotheses, and a derived full
arithmetic identity or a clearly identified intermediate identity. It
should not yet be a conjecture asserting that an unspecified field's
correlator equals the Weil form.

## 7. Scope of the search and novelty assessment

The search covered protected line and interface sectors, positive
twisted traces, boundary Liouville, factorizing and scalar QFT,
Wilson networks, free fields, arithmetic scattering and quantum graphs,
Schwarzian observables, and \(p\)-adic/statistical arithmetic systems.
Primary papers were used for substantive claims. Selected full-text
definitions and hypotheses were checked, especially the physical
versus bilinear gluing distinction, positivity theorems for trace
families, the nonconformal Schur qualification, and the unfinished
companion cited by the boundary Liouville paper. This is a broad survey,
not an exhaustive priority audit or an independent proof audit of those
papers.

Compared with the [earlier landscape](../../brainstorm/theory-landscape-20260913/REPORT.md),
the substantive new emphasis is the concrete sphere/Schur operator
algebra and positive-trace literature, with boundary Liouville as an
exact interacting alternative. It does not restore the earlier default
of choosing a new supersymmetric potential or a generic metric.

The boundary/defect interpretation, the norm mechanism, twisted-trace
quantization and the named field theories are established ideas.
The possible contribution of this project remains the independently
derived **complete arithmetic matching identity**, and the resulting
conditional constructive-QFT-to-RH theorem. Neither has yet been
obtained. This keeps the recommendation aligned with the
[manuscript's novelty assessment](../../manuscripts/finite-response-weil-positivity/EVALUATION.md).

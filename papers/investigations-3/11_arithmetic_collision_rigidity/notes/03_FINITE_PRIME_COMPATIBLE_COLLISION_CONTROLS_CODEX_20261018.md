# Colliding sources with exact finite prime compatibility

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Model **gpt-6-astra (Codex)**, reasoning effort **max**,
verified from this turn's metadata.

**Status: proved in-note using the named theta-zero and reflection-rigidity
inputs; one explicit endpoint construction is interval-certified.** Review
scope is the [same-assistant assessment][review], with no independent LLM
or specialist review and no literature-novelty claim.

The new extension is to perturbations constant on complete multiplication
orbits of any selected finite prime set. The high-gap collision mechanism
comes from [Investigation 07][gap], and the rigidity input from
[Investigation 22][rigidity]. This extension preserves infinitely many
coefficient identities at every selected prime. It therefore tests more
than a finite truncation of those identities.

The result concerns a relaxation of theta: positive bounded square
coefficients, exact selected-prime identities, primitive normalization,
and finitely many additional linear measurements. It excludes none of the
arguments that use full modular reflection or the full coefficient sequence.
In particular, it is not a theorem about collisions of theta.

The [result summaries][summaries], [control cluster][s12],
[patterns to avoid][avoid], [premise screen][a02], and [scoped-exclusion
rule][a07] govern this interpretation. This is a class obstruction, not an
RH-equivalent criterion or a proposed numerical Newman improvement.

## The finite prime relaxation

Fix a finite set P of primes, Q=product(P), and N>=1. Every positive
integer n has a unique decomposition n=r m, where (r,Q)=1 and every
prime factor of m belongs to P. Write r=rho_P(n), and let S(P) denote
this multiplicative semigroup, including 1.

Retain the source modes
\[
p_n(u)=e^u e^{-\pi n^2e^{4u}},\qquad
\phi_n(u)=e^u(2\lambda_n^2e^{8u}-3\lambda_ne^{4u})
e^{-\lambda_ne^{4u}},\quad \lambda_n=\pi n^2,
\]
with 8 phi_n=p_n''-p_n. For every r coprime to Q, define complete orbit
sources
\[
\Psi_r(u)=\sum_{m\in S(P)}\phi_{rm}(u),\qquad
\psi_r(u)=\sum_{m\in S(P)}p_{rm}(u).                     \tag{1}
\]
These converge locally with every derivative on the real u axis and
decay doubly exponentially with their derivatives as u tends to positive
infinity. Their coefficient sequences are bounded.

For distinct selected rough indices r>N, choose real numbers v_r and set
\[
v_n=v_{\rho_P(n)}\text{ on the selected orbits, and }v_n=0
\text{ otherwise};\qquad K=\sum_r v_r\Psi_r.
                                                               \tag{2}
\]
Then v_n=0 for n<=N and
\[
v_{pn}=v_n\quad(p\in P,\ n\ge1).                        \tag{3}
\]
Different selected orbits are disjoint, so these directions are linearly
independent. Normalize max_r |v_r|=1. Consequently |v_n|<=1 and, on u>=0,
\[
|K(u)|\le\sum_{n>N}\phi_n(u)\le\Phi(u).                \tag{4}
\]
The modes are strictly positive on this half-line.

## Statement of the obstruction

Fix a heat time T>0, a coefficient cutoff N, and finitely many real
linear measurements of the source or its coefficient sequence. Their
restrictions to each finite orbit span are assumed defined. Examples
include finitely many source/primitive endpoint derivatives, source values,
and heat-transform derivatives at finitely many declared real or complex
points (a complex observation gives two real measurements).

**Theorem.** There is a fixed, nonzero direction (2), supported on finitely
many rough orbits above N, and a sequence of nonzero real numbers
delta_j tending to zero, such that the coefficients
\[
a_n^{(j)}=1+\delta_jv_n                                 \tag{5}
\]
have the following properties for all sufficiently large j:

- They are strictly positive and uniformly arbitrarily close to 1; all
  coefficients n<=N are exactly 1.
- They obey a_(pn)=a_n for every n and every p in P, including all powers
  and compositions of those primes.
- The primitive normalization is exactly psi_a'(0)=-1/2. Every declared
  finite linear measurement equals its theta value. In particular, any
  prescribed finite list of odd source endpoints can vanish exactly.
- The frozen heat field
  \(H_a(t,z)=\int_0^\infty e^{tu^2}\Phi_a(u)\cos(zu)\,du\)
  has a nondegenerate double zero at (T,x_j), with x_j tending to infinity.
  There is one such ratio construction in every sufficiently high
  consecutive theta-zero gap at the fixed time T.

These perturbed arithmetic sources do not satisfy complete source
reflection. Their even extensions from the half-line can match any fixed
finite smoothness order at zero, but are not analytic even theta sources.
The height cutoff depends on T and the direction; no effective onset,
prescribed collision abscissa, or uniformity as T tends to zero is asserted.
These are local double events; no finite Newman constant or global
real-zero threshold is asserted for the perturbed sources.

## Choose a direction preserving the measurements

Add the homogeneous primitive condition
\[
\psi_K'(0)=\sum_n v_n(1-4\pi n^2)e^{-\pi n^2}=0          \tag{6}
\]
to the finite homogeneous measurement conditions. Choose more distinct
rough indices r>N than there are real equations. Infinitely many are
available, for example integers congruent to 1 modulo Q. Finite-dimensional
linear algebra gives a nonzero real solution v. Rescale it so max|v_r|=1.
This changes neither (3) nor any homogeneous condition. The full source
is not zero: if K=0, its primitive solves psi_K''-psi_K=0 and decays
doubly exponentially at positive infinity, hence psi_K=0; uniqueness of
the Gaussian expansion then forces every v_n=0.

There must be a nonzero odd derivative of K at zero. Otherwise real
analyticity would make K even on the whole real axis. Combined with (6),
the [reflection-rigidity theorem][rigidity], applied to the signed bounded
coefficient sequence with v_0=0, would give v_n=v_0=0 for every n.
This is a contradiction. Positivity is not required by that rigidity
theorem. Its primitive condition is essential and is explicitly supplied
by (6).

Let 2r-1 be the first nonzero odd derivative order of K. It is finite,
although it can exceed every order imposed among the measurements.

## Endpoint decay and the high-gap event

Put
\[
V(t,x)=\int_0^\infty e^{tu^2}K(u)\cos(xu)\,du,
\quad H(x)=H_\theta(T,x),\quad V(x)=V(T,x).
\]
Every derivative of e^(Tu^2)K(u) is integrable on the positive half-line.
Since the heat weight is even, its first nonzero odd endpoint derivative
is still K^(2r-1)(0). Repeated endpoint integration, applied separately
to V,V',V'', yields
\[
V(x)=A x^{-p}(1+O(x^{-2})),\quad
V'(x)=-pA x^{-p-1}(1+O(x^{-2})),
\]
\[
V''(x)=p(p+1)A x^{-p-2}(1+O(x^{-2})),\qquad
p=2r,\quad A=(-1)^rK^{(2r-1)}(0)\ne0.                 \tag{7}
\]
No remainder is differentiated without its own integral justification.
Therefore V is nonzero eventually, and
\[
(\log|V|)''=p/x^2+O(x^{-4})>0                          \tag{8}
\]
at sufficiently large positive x.

The theta inputs are [Polymath, Theorem 1.5(i),(ii), and its section 9
argument-principle proof][polymath]: at every fixed 0<T<=1/2, high zeros
are real and simple, and all nonreal zeros lie in a compact rectangle.
For T>1/2, the published upper bound Lambda<=0.22 and the local Hermite
splitting give real simple zeros everywhere. There are infinitely many
zeros: a nonzero even order-one entire function with only finitely many
zeros would be a polynomial, contradicting rapid real-axis decay.
The order-one paired Hadamard product, given in the same paper's
proof of Proposition 3.1, then gives, eventually off the real zeros,
\[
(\log|H|)''<0.                                        \tag{9}
\]
To see the last assertion even if there are nonreal zeros, a conjugate
pair alpha +/- i beta contributes
\[
-\frac{2((x-\alpha)^2-\beta^2)}{((x-\alpha)^2+\beta^2)^2}<0
\quad\text{once }x>\alpha+|\beta|.
\]
There are only finitely many such pairs; each real zero contributes
-(x-rho)^(-2). Order one excludes a quadratic exponential factor.

In every sufficiently high consecutive real-zero gap, set R=H/V.
It is nonzero in the interior and zero at the two endpoints. Equations
(8)–(9) imply (log|R|)''<0. Its logarithmic derivative runs from positive
infinity to negative infinity, so it has a unique zero x_j there, with
R(x_j) nonzero and R''(x_j)/R(x_j)<0. Define
\[
\delta_j=-R(x_j),\qquad
G_j(t,x)=H_\theta(t,x)+\delta_jV(t,x).                  \tag{10}
\]
The coefficient delta_j is fixed when t or x changes. At the event,
\[
G_j(T,x_j)=G_{j,x}(T,x_j)=0,\qquad
G_{j,xx}(T,x_j)=V(x_j)R''(x_j)\ne0.                   \tag{11}
\]
The complete theta transform is rapidly decreasing on the real axis at
fixed T, because its full even weighted source is Schwartz. Equation (7)
therefore implies delta_j=O_M(x_j^(-M)) for every fixed M. In particular
delta_j tends to zero, so (5) is strictly positive eventually. All exact
linear measurements and selected-prime relations remain unchanged.
This proves the theorem. The collision mechanism is the [existing
one-direction gap argument][gap]; its extension here is the infinite orbit
support with (3) and the rigidity proof of a finite endpoint exponent.

## Explicit topology and source-tail control

The coefficient distance is exactly sup_n|a_n-1|=|delta_j|. By (4),
\[
(1-|\delta_j|)\Phi(u)\le\Phi_a(u)
\le(1+|\delta_j|)\Phi(u)\quad(u\ge0).                  \tag{12}
\]
For any fixed upper time T_+>=T, strip width Y>=0, and finite derivative
order J, use the norm
\[
\|f\|_{T_+,Y,J}
=\int_0^\infty e^{T_+u^2+Yu}
 \left(\sum_{j=0}^J u^j\right)|f(u)|\,du.
\]
It is finite on every constructed perturbation, and is at most
|delta_j| times the corresponding theta-tail norm above N. With m>N
the first possibly changed index, the bound from [Note 02][n02] gives
\[
\sup_{\substack{0\le t\le T_+\\|\operatorname{Im}z|\le Y}}
|\partial_z^j(H_a-H_\theta)(t,z)|
\le |\delta_j|\epsilon_j(m;T_+,Y),\quad 0\le j\le J,  \tag{13}
\]
whenever its stated admissibility conditions hold. If a prescribed N is
too small for them, choose the rough seeds beyond a larger admissible m.
Equation (13) is uniform in real spectral height. It is an absolute
approximation, not a relative bound at a small physical jet.

Thus the controls can match the entire initial coefficient segment and
all selected linear observations exactly, and be arbitrarily close in
coefficient sup norm and a specified heat-weighted tail norm, while
colliding at unbounded height. This does not assert a collision in a
fixed compact height range or defeat a certificate for such a range.

## A concrete direction for primes 2 and 3

Take rough seeds 5,7,11. Put
\[
B_r=\sum_{m\in S(\{2,3\})}(4\pi r^2m^2-1)e^{-\pi r^2m^2},
\quad D_{r,k}=\Psi_r^{(k)}(0).
\]
Let hats denote multiplication by e^(pi r^2). Define w_11=1 and solve
\[
\widehat B_5w_5+\widehat B_7w_7=-\widehat B_{11},\qquad
\widehat D_{5,1}w_5+\widehat D_{7,1}w_7=-\widehat D_{11,1}.
                                                               \tag{14}
\]
Set v_r=w_r exp(pi(r^2-121)). These are definitions using the complete
infinite orbit sums, not rounded decimal coefficients. Then psi_K'(0)=0
and K'(0)=0 exactly. The [interval checker][code] encloses the sums by
their m=1 terms plus all-integer tails from n=2r onward. It proves the
matrix in (14) is invertible, |v_5|,|v_7|<1, v_11=1, and K'''(0)<0.
The following displayed values are rounded diagnostics from its [record][record]:

| Quantity | Approximate value |
| --- | --- |
| Scaled determinant in (14) | -6.64737049e9 |
| w_5 | 33.7299241581 |
| w_7 | -19.6540490598 |
| v_5 | 3.53089982e-130 |
| v_7 | -1.14381176e-97 |
| exp(121 pi) K'''(0) | -7.95393946e14 |

Consequently this fixed direction preserves all 2- and 3-prime excision
relations, a_1 through a_4, the primitive normalization, and the first
source reflection endpoint. Its first nonzero odd source derivative is
the third, so (7) has p=4. Its reflected extension is C^2 but not C^3.
The theorem gives frozen nondegenerate collisions for small multipliers
along this direction in sufficiently high gaps at every fixed T>0.
No numerical collision height or effective smallness threshold is claimed.

## What the result rules out and what remains open

At each constructed event the local heat law gives, on its stationary
predecessor,
\[
\mathcal L_0/E=-1/(T-t)+O(1).
\]
The exact packet identities at every selected prime and the correctly
reflected derivative formulas in [Note 02][n02] hold throughout this
evolution. Hence those relations, positive square support, normalization,
finitely many exact linear tests, and any positive absolute tail tolerance
cannot imply collision exclusion for the whole stated class on unbounded
height. The failure occurs on an actual event of a fixed source.

The missing premise is complete source reflection, equivalently in the
normalized bounded square-coefficient class the full modular identity.
For the explicit construction it already fails at K'''(0); for any fixed
larger endpoint list it fails at some later odd derivative. Full reflection
would force the coefficient sequence back to theta by rigidity. This
result does not bound the strength of a finite formula that *uses* that
full relation or complete arithmetic data.
The direction depends on the chosen finite prime set and measurement list.
No single perturbed source is claimed to pass every prime or every endpoint
condition. Infinite families and justified limiting arguments remain outside
this obstruction.

The control screen is therefore precise. The earlier weighted-square
controls lacked the complete selected-prime relations; the new controls
retain them. Reflected smooth and positive-primitive controls retain source
reflection but lack the normalized square expansion. Euler-factor controls
can retain unmodified prime factors while changing level or lattice data.
None of these comparisons proves an exclusion for theta, and no known
colliding control here retains theta's full normalized modular structure.

[n02]: 02_COMPLETE_PACKET_MATCHING_CODEX_20261018.md
[review]: ../reviews/01_OPENING_ROUND_SELF_REVIEW_CODEX_20261018.md
[code]: ../numerics/check_packets_and_orbits.py
[record]: ../numerics/PACKET_AND_ORBIT_CHECKS_20261018.json
[gap]: ../../07_source_measurement_audit/notes/round-2/02_ONE_DIRECTION_GAP_COLLISIONS_AND_TAIL_BUDGET_CODEX_20261017.md
[rigidity]: ../../../investigations-2/active/22_theta_manifold_geometry/notes/05_control_families/02_WEIGHTED_COMB_REFLECTION_RIGIDITY_20261015.md
[polymath]: https://arxiv.org/html/1904.12438v2
[summaries]: ../../../../result-summaries/README.md
[s12]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md

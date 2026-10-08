# Third continuation: signed remainders and effective collision control

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
The parallel derivations and separate scoped reviews are same-model internal
checks, not independent specialist validation or formal proof replay.

This continuation carries out the next tasks in the
[second results note](SECOND_CONTINUATION_RESULTS_20261008.md). It removes
another part of the short-family remainder, identifies a signed cubic target
for the mixed family, proves an obstruction to absolute estimation of the
actual quadratic prime-pair form, and gives an explicit large-height
real-collision exclusion from the published heat-flow approximation.
The new signed arithmetic bounds remain open. No new zero-free boundary or
proof that zeta-only quasi-RH implies RH follows.

The [dependency ledger](RESEARCH_LEDGER_20261008.md) records the imported
inputs. The claims below preserve their original fields, masks, selectors,
profiles, and uniformity requirements.

## 1. Short families: a smaller signed remainder

Let the physical row range be \(H=D^h\), \(0<h<1\). Removing the complete
original column diagonal **before** the source's finite transformations
leaves distinct transformed columns \(m_1\ne m_2\). Their ratio character
is nonprincipal, with primitive conductor
\(m_1m_2/(m_1,m_2)^2\), and retains its shared-prime zero mask.

A second Poisson sum over the complete smooth row kernel then proves
arbitrary power decay in the sector
\[
(Nf)^2N(m_1,m_2)\ge HD^{2\eta},\qquad \eta>0.
\]
The source's existing positive moment still handles the complete blocks
\(Nb\ge D^{1-h+\eta}\). It must be applied before imposing the additional
pair restriction. Thus the missing signed estimate is confined to
\[
Nb<D^{1-h+\eta},\qquad
(Nf)^2N(m_1,m_2)<HD^{2\eta},\qquad m_1\ne m_2.
\]
In particular, \(Nf<D^{h/2+\eta}\). The residual retains the actual Gauss
coefficients, Möbius sign in \(f\), physical profiles, and both cofactor
masks. The unit-column example separately proves that the old positive dual
theorem cannot be extended unchanged into the short-family range.

A bound of order \(D^{h+a+\varepsilon}\) for this normalized remainder
would supply the proposed moment and hence the previously proved extraction
to \((1+a)/2+5h/12\). For instance, \(h=8/9,a=0\) would give
\(47/54=7/8-1/216\). No such residual estimate is proved.

[Derivation](SHORT_FAMILY_SMALL_COFACTOR_20261008.md) ·
[source-scoped review](../reviews/SHORT_FAMILY_SMALL_COFACTOR_REVIEW_20261008.md).

## 2. Mixed family: retain cyclic phases

At common separating parameters, put
\(w_u=\mathbf1_{\mathcal C_+}|M_r(u)Q_I(u)|^2\),
\(N=U^m\), and form the positive Gram matrix from the original smooth
plain columns. Its kernel is a complete smooth ideal sum of the row-ratio
character with all original zero masks. The sharp selected-row indicator
remains outside that sum, so this transposition does not require applying
Poisson to a selected row set.

The source's global \(7/8\) family theorem **and quantitative growth
lemmas** give a conditional nonprincipal kernel bound
\(U^\varepsilon N^{-1/8}(1+T_1)^C\). A bare zero-location statement is
not used in place of uniform growth. Even hypothetical square-root
entrywise cancellation would leave the available absolute-Schur estimate
above its target by at least \(0.031798\) in the near-saturated regime.
An exact finite-field frame proves the corresponding loss from discarding
phases, without claiming to model the actual Möbius coefficients.

The sufficient cubic trace target is
\[
\operatorname{Tr}(G^3)
\ll U^{3[1-(1-d)m-s]+\varepsilon}(1+T_1)^C.
\]
There is a further arithmetic simplification. In a common fixed ray
presentation, equality of the inducing primitive characters forces equal
valuations modulo six at every good prime. The actual rows are
sixth-power-free, so those valuations agree exactly. Only finitely many
unit and fixed-bad-prime choices remain: every such fiber has size at most
\(6^{|S|+1}\), and at most six when the rows are coprime to \(S\).
This statement concerns phases; canceled nonunit zeros remain in the kernel.

Consequently **all terms with a repeated inducing primitive character**
fit the cubic budget. The nonprincipal repeated-sector margin is at least
\(147/12500\), certified on the full buffered parameter rectangle by
exact rational intervals. What remains is the signed cyclic correlation
over three pairwise inequivalent primitive characters. This is still a
new arithmetic obligation; the operator target is sufficient and stronger
than the original fixed-vector mixed-energy target.

[Derivation](SELECTED_INVERSE_DISTRIBUTION_20261008.md) ·
[scoped review](../reviews/SELECTED_INVERSE_DISTRIBUTION_REVIEW_20261008.md) ·
[local-character audit](../reviews/PRIMITIVE_CHARACTER_FIBER_REVIEW_20261008.md).

## 3. Integer quadratic lift: what the moment would have to prove

For \(1<h<2\), the remaining weighted moment has conductor ceiling
\(Q=X^{2-h}\) and target exponent \(T=1+h/2\). The inherited fixed
probe has a nonzero Mellin transform throughout \(1/2<\Re s<1\).
Consequently this moment, if proved, would give the boundary
\(\beta_h=1/2+h/4\) for **every fixed primitive quadratic character of
odd conductor**, including zeta. This is stronger information than a
zeta-only strip. Even-conductor characters are not covered by this lift.

Higher prime powers and the prime diagonal cost at most
\(X^{2-h/2+o(1)}\), below the target. The remaining prime-pair expression
is signed. Its termwise absolute majorant for the **actual probe and
prime coefficients** is at least a positive constant times \(X^2\),
which exceeds \(X^T\) for every \(h<2\). The proof uses the coherent
principal row in a positive Gram form and the prime number theorem.
It rules out termwise absolute estimation of this expression.

Even granting a conductor-uniform response estimate \(S_a(X)\ll
X^{B+\varepsilon}\), combining that estimate with the classical quadratic
large sieve cannot give descent. For an attempted improvement, the
bottleneck lies at conductors \(X^{2-2B}\). At \(B=7/8,h=7/5\), it
lies at \(X^{1/4}\), and the available weighted exponent \(15/8\)
misses the target \(17/10\) by \(7/40\). A sharp abstract array verifies
the limitation of those two scalar envelopes; it is not an arithmetic
counterexample to the desired moment.

[Derivation](QUADRATIC_MOMENT_STRENGTH_AND_BARRIER_20261008.md) ·
[scoped review](../reviews/QUADRATIC_MOMENT_BARRIER_REVIEW_20261008.md).

## 4. Heat flow: a complete normalized criterion

The published effective approximation is rewritten as a holomorphic finite
sum with a fixed integer cutoff. Dividing it and \(H_t\) by a common
nonzero symmetric analytic normalizer permits reflection of its error to
a full complex disk. Explicit finite corrections pay for every crossing
of the source's natural cutoff. Cauchy's estimate then supplies a derivative
error on smaller disks. These ingredients provide a rigorous format for
certifying the exclusion of common real zeros of \(H_t,H_t'\).

Using just the leading conjugate pair, with the entire finite tail and
source remainder paid, gives the explicit analytic consequence
\[
0<\varepsilon\le\tfrac12,\quad
\varepsilon\le t\le\tfrac12,\quad
|x|\ge \exp(64/\varepsilon)
\quad\Longrightarrow\quad
(H_t(x),H_t'(x))\ne(0,0).
\]
This is a conservative effective large-height statement derived from the
imported Polymath theorem. It is not claimed as a new qualitative eventual
simplicity theorem. No numerical heat values enter the proof, and it does
not independently locate all complex zeros. No middle-height rectangle has
been certified. The unhandled range grows without bound as
\(\varepsilon\downarrow0\), so this does not exclude a positive Newman
threshold.

[Derivation](NORMALIZED_HEAT_COLLISION_CRITERION_20261008.md) ·
[source and constant review](../reviews/NORMALIZED_HEAT_COLLISION_REVIEW_20261008.md).

## 5. Next bounded investigations

1. Work on the short-family signed form in equation (25) of its new note,
   beginning with \(b=f=1\) and low overlap. Preserve its complete smooth
   row kernel and actual column coefficients. This tests the remaining
   cancellation without trying to extend the disproved positive theorem.
2. Estimate the mixed-family cyclic kernel with its phase retained, or use
   the actual all-ones column vector to avoid the stronger operator target.
   An entrywise square-root estimate alone cannot supply the required gain.
3. Seek signed cancellation in the exact quadratic prime-pair form,
   concentrating first on conductors near \(X^{2-2B}\). Any claimed
   consequence of a zeta-only hypothesis must explain the stronger
   odd-quadratic-family conclusion already forced by the target moment.
4. Implement outward-rounded interval evaluation of the normalized finite
   heat sum on a modest specified positive-time rectangle. Pay both disk
   errors and cutoff corrections, then test where certification fails.
   Covering that rectangle is a bounded experiment; covering all positive
   times would still require a new argument.

All four new finite-check scripts pass. They cover local masks, exact
transforms, finite-field Gauss sums, continuous rational parameter
enclosures, and the last rational heat constants. Their precise scopes
and small retained records are in the [numerics index](../numerics/README.md).
They do not verify the imported analytic proofs or the missing asymptotic
signed estimates.

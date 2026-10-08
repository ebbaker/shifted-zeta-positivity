# Second continuation results and next arithmetic estimates

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
The four derivations and their separate reviews are same-model internal
checks, not independent specialist validation or formal verification.

**Subsequent work:** the [third continuation](THIRD_CONTINUATION_RESULTS_20261008.md)
carries out the next tasks below. It further restricts the short-family
remainder, gives a signed mixed cubic target, proves an actual quadratic
absolute-majorant obstruction, and supplies normalized derivative control
with an explicit large-height real-collision exclusion. The signed moment
estimates remain open.

The recommended four-lane investigation produced a stronger conditional
short-family extraction, an additional removable mixed-conductor sector,
a complete integer prime-response lift, and an obstruction to finite
theta approximations of the collision Wronskian. The new arithmetic
estimates needed for a zero-free improvement remain unproved. In
particular, this continuation does not prove that zeta-only quasi-RH
implies RH.

The [dependency ledger](RESEARCH_LEDGER_20261008.md) separates inherited
theorems, imported analytic inputs, new deductions, and missing estimates.
The [earlier continuation](CODEX_CONTINUATION_20261008.md) remains the broad
program map. The following results update its immediate research tasks.

## 1. One fixed short-family moment can be reused

Suppose, for one fixed \(0<h\le1\), \(a\ge0\), fixed Hecke character and
fixed annular profile, that the proposed actual-Möbius family bound

\[
\sum_{0<Nu\le D^h}|A_u(D)|^2
\ll_\varepsilon D^{1+a+h+\varepsilon}
\]

holds for every epsilon and all sufficiently large real \(D\). Put
\(b=(1+a)/2+5h/12\), \(c=1-h/6\). The existing mask identity now
gives more than a one-step improvement from a prior strip:

\[
P(t)\Longrightarrow P(\max\{b,ct\}),\qquad
t_n=\max\{b,c^n\}\quad(t_0=1).
\]

For \(b<1\), a finite number of reuses of the **same** moment gives
\(P(b)\). Neither a prior family strip nor the stronger scale-supremum
hypothesis is needed for this extraction. For example,
\(h=2/3,a=0\) gives the conditional chain
\(1\to8/9\to64/81\to7/9\).

The moment remains unproved. A fixed positive \(h\) has a positive
floor above \(1/2\). Arbitrarily small \(h\) with losses tending to zero
would already supply RH-strength information, even from the single row
\(u=1\). Restricting a new estimate to repeated prime sixth-power rows
does not avoid that difficulty: its normalized moment is equivalent to
the target fixed-character Möbius bound.

The source audit localizes the long-family proof's failure to the dual
ratio \(R/\Sigma\ll D/(HB)\). For short families, the small-\(B\)
blocks no longer satisfy the shrinking-row condition. The next task is
to control those actual-coefficient blocks at one useful fixed
\(h<9/10\), with \(a<3/4-5h/6\). An all-scale supremum is no longer
a prerequisite for extraction.

[Derivation](../short_families/notes/SHORT_FAMILY_DESCENT_REFINEMENT_20261008.md) ·
[review](../reviews/SHORT_FAMILY_REFINEMENT_REVIEW_20261008.md).

## 2. A further mixed-conductor sector is removable

Using the sharper full-bin count \(R^*\), the tapered saving, and an
explicit operational loss budget \(\ell=10^{-6}\), the total-ratio
cutoff exponent is enclosed by

\[
0.90344403027\ldots\le\tau\le1.07124901367\ldots.
\]

These are continuous rationally certified parameter bounds, conditional
on the stated witness-loss and source hypotheses. They are not estimates
for the remaining character sum.

The new step bounds the positive selected inverse mass by

\[
\sum_{u\in\mathcal C_+}|M_rQ_I|^2
\ll U^{1-\mu_C+\varepsilon}(1+T_1)^A,
\quad
\mu_C=\max\{0,1-R^*-\ell-dr-\Gamma_I\}.
\]

It combines the existing inverse moment with the count and pointwise
physical-profile envelopes. The plain-ratio cutoff can consequently
increase by \(2\mu_C\). On the stated buffered subregion
\(x\ge4999/10000\), \(r-r_{\rm new}\le1/10000\), it increases by
at least \(1/12500\). The proof retains the selector and every zero
mask. It bounds the whole weighted plain annulus before subtracting its
small-total-conductor part; the total-conductor restriction is not placed
inside a supposed positive norm.

This is an additional controlled sector of the actual signed residual,
not a complete mixed-moment theorem. The next task is a large-plain-ratio
estimate that uses the distribution of this selected inverse mass among
ratio phases, rather than just its total size. Derivative-profile
uniformity and actual witness losses remain explicit conditions.

[Derivation](../mixed_character_families/notes/MIXED_CONDUCTOR_REFINEMENT_20261008.md) ·
[review](../reviews/MIXED_CONDUCTOR_REFINEMENT_REVIEW_20261008.md).

## 3. The complete integer response has an exact family lift

For the Jacobi family \(\chi_u(n)=(n/u)\), odd square rows satisfy

\[
S_{b^2}(X;L)=S_1(X;L)
-\sum_{p\mid b}\log p\sum_{k\ge1}L(p^k/X).
\]

For every fixed compact multiplicative window, the deletion is
\(O_L(\log b)\), uniformly in real \(X\). All prime powers remain
in the identity. There are \(\asymp\sqrt H\) distinct such rows up to
\(H\), including composite roots. The same identity holds for the
complete profile \(V_g(Xy)\) in \(L^2([1,2])\), not just a scalar
sample.

A new full-row moment of size \(X^{1+a+h+\varepsilon}\), \(H=X^h\),
would therefore give the boundary
\(\beta_{\rm out}=1/2+a/2+h/4\). This is a distinct integer quadratic
family; no Eisenstein-ideal moment is relabeled as an integer theorem.

The classical squarefree quadratic large sieve extends to these rows
with the paid bound
\((HX)^\varepsilon(HX+X^2\sqrt H)\). Its second term prevents a
power improvement. For \(1<h<2\), however, the squarefree-kernel
range above \(X^{2-h}\) already fits the lossless target. The exact
remaining scalar obligation is

\[
\sum_{\substack{a\le X^{2-h}\\a\ {\rm odd\ squarefree}}}
a^{-1/2}|S_a(X;\ell)|^2
\ll_\varepsilon X^{1+h/2+\varepsilon}.
\]

For \(h=7/5\), this asks for a weighted moment through conductor
\(X^{3/5}\) with exponent \(17/10\); it would give boundary
\(17/20\). It is unproved, and its principal term already carries
the desired improved zeta bound. The lift resolves the identity and
error-budget task, while exposing rather than hiding that coherent term.

[Derivation](../integer_quadratic_lift/notes/INTEGER_QUADRATIC_RESPONSE_LIFT_20261008.md) ·
[review](../reviews/INTEGER_QUADRATIC_LIFT_REVIEW_20261008.md).

## 4. Finite theta cutoffs cannot supply an all-height Wronskian sign

The collision note gives exact theta-arithmetic formulas for
\((H_t,H'_t)\) and \(W_t=H_t'^2-H_tH_t''\), including a finite
Dirichlet-polynomial sum inside a convergent outer integral.

If \(\Phi_N\) is any fixed finite theta cutoff, its first endpoint
derivative is strictly positive, \(A_N=\Phi_N'(0)>0\). Integration
by parts gives, at every fixed finite time,

\[
W_{t,N}(x)=-2A_N^2x^{-6}+O(x^{-8})<0
\quad\text{for sufficiently large }|x|.
\]

The full theta tail cancels the endpoint defect exactly. Thus a finite
theta cutoff cannot have exclusively real zeros at any finite heat time
and cannot provide an all-height positive-Wronskian approximation by
simply discarding its small tail. This diagnoses the approximants, not
a defect in the full zeta heat flow. Odd-jet cancellation itself is not
a new discriminator against the earlier even general-kernel counterexample.

Explicit lattice and spatial-tail bounds support a conditional compact
rectangle certificate for \(H_t,H'_t\) not vanishing together. The
saved numerical samples are reconnaissance; no rectangle is claimed
certified. The next useful task is a normalized effective heat
approximation with complex-neighborhood and derivative error control.
The diverging height coverage as positive time tends to zero remains an
independent obstacle.

[Derivation](../newman_collisions/notes/ZETA_COLLISION_ARITHMETIC_20261008.md) ·
[review](../reviews/ZETA_COLLISION_ARITHMETIC_REVIEW_20261008.md).

## Verification and next continuation

The [numerics index](../numerics/README.md) distinguishes exact rational
and integer checks from floating reconnaissance. The new finite checks
cover continuous conductor inequalities, five short-family extraction
chains and twelve finite mask identities, and 51,657 Jacobi-mask
comparisons with full finite Gram and grouping checks. The separate
reviews checked the analytic reductions and corrected scope issues;
they do not validate the imported deep source machinery.

For the next session, keep the small-\(B\) short-family problem as the
scalable lane. The mixed inverse-mass distribution and the localized
quadratic prime moment are two concrete signed-arithmetic alternatives.
Use the theta result to guide error-paid approximation rather than another
fixed-cutoff sign scan. A genuine new estimate, additional legal range,
or decisive obstruction should determine which lane expands next.

No manuscript, release, commit, tag, or historical snapshot was created.
Existing historical notes and unrelated working-tree edits were preserved.

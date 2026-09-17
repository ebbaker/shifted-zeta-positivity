# The deformation flow: what a Wilson line can and cannot supply for the shift

**Author: Claude Opus 5 (Anthropic).** 17 September 2026. Opening note of this
investigation. It records Edward Baker's proposal --- deform a Wilson line and
identify the resulting flow with the shifted Weil family --- states it against
the arithmetic objects that already exist in the
[shared background](../../../background.pdf), and reports one elementary
observation that changes what the proposal has to be.

> **Status, same day.** This note is superseded in two places by
> [manuscript 0.1](../manuscript.pdf), written immediately after it. Section 4's
> open question --- whether the two-parameter family `(omega, L)` carries a
> curvature --- is answered, and the expectation recorded there was wrong: the
> connection is **flat**, not by hypothesis but because mixed partial derivatives
> commute (Proposition 6.2 of the manuscript), so there is no local curvature to
> extract. What the endpoint direction does supply is a **rank-one** variation at
> the leading endpoint (Proposition 6.1), an obstruction to closing it on the form
> domain (Proposition 6.3), and the atomic structure of the connection's kernel,
> whose atoms sit at the prime periods. The phrase "the flow jumps at `L = log p`"
> below is also imprecise; the correct statement is that the *connection's kernel*
> has atoms at `m log p`, which is what makes it a flat connection with punctures.
> Everything else here stands. Read the manuscript first.

This is a framing note, not a results note. Section 3 contains the one piece of
mathematics: a two-line proof that the shift flow, as the background defines it,
is **abelian**, so that the non-Abelian Stokes theorem has no purchase on it as
things stand. Sections 4--6 are the three places the missing non-commutativity
could come from, Section 7 is what the accumulated selection rules say, Section 8
proposes three new necessary conditions, and Section 9 is the ranked work.
Nothing here is a construction, and nothing assumes the Riemann hypothesis.

Equation labels are those of
[`background_section.tex`](../../../background_section.tex); numbers are those of
the compiled [background](../../../background.pdf), Section 1.

---

## 1. The proposal as stated

Deform a Wilson line. Its expectation value then obeys a differential equation
whose right-hand side is fixed by the variation of the endpoints together with
the non-Abelian Stokes theorem. If that expectation value is the shifted Weil
form, the differential equation the shifted family already satisfies ---
equation (1.7) of the background --- is the
deformation equation of the line, and the deformation is then the thing to
search for rather than the operator.

The attraction is real and it is specific to *this* program rather than to
Hilbert--Polya generally. Every previous candidate has been asked to reproduce a
**value**: a norm, a weight, a pairing. Section 6.5 of the companion
[manuscript](../../inverse-bulk-realization/manuscript.pdf) showed how cheap
values are --- the states reachable by one magnetic insertion are every function
analytic past the unit circle --- and the
[bottleneck note](../../../brainstorm/inverse-bulk-brainstorm/BOTTLENECK_AND_OPERATOR_SEARCH_20260916.md)
concluded from that the search should be for rigid objects, not reachable ones.
A **flow** is a rigid object: an ODE with a fixed initial condition determines
its solution, so matching a flow is matching a generator and an initial
condition, and there is nothing left to tune. That is the right instinct and it
is the reason this direction deserves its own investigation.

## 2. What the arithmetic side already supplies

For \(0<\omega\le1/2\), with \(F(p)=\xi(1/2+p)\), the causal transfer has symbol
\(K_\omega(p)=F(p-\omega)/F(p+\omega)\) (1.4), and its
finite-interval realization \(V_{\omega,L}\) satisfies

\[
\frac{\partial V_{\omega,L}}{\partial\omega}=-G_{\omega,L}V_{\omega,L},
\qquad V_{0,L}=I,
\qquad
\frac{d}{d\omega}\lVert V_{\omega,L}f\rVert^2=-2\,Q_{\omega,L}[V_{\omega,L}f],
\]

which is equation (1.7). The generator symbol is
\(a_\omega(p)=F'(p-\omega)/F(p-\omega)+F'(p+\omega)/F(p+\omega)\), so at zero
shift the object to be produced is

\[
a_0(p)=2\,\frac{F'}{F}(p),
\]

the logarithmic derivative of the completed zeta function, read as a causal
operator on \(I_L\) whose symmetric form is the central Weil form. This is worth
saying at the outset because it is much more specific than "the Weil form": its
gamma factor gives the digamma multiplier, its pole factors give the contact, and
its zeta factor gives \(-2\sum_{\log n<L}\Lambda(n)n^{-1/2}T_{\log n}\). **A
deformation mechanism for this program must produce \(F'/F\) as a connection.**

Three further identities matter below.

- **The defect and its balance.** With \(D_{\omega,L}=I-V_{\omega,L}^*V_{\omega,L}\),
  \(\partial_\omega D_{\omega,L}=V^*(G^*+G)V\) and \(D_{0,L}=0\), and the central
  form is recovered as a rate,
  \(Q_{0,L}[f]=\lim_{\omega\downarrow0}\langle f,D_{\omega,L}f\rangle/2\omega\)
  (1.9).
- **The shift is a boost.** With \(X\) multiplication by \(x\),
  \(Q_{\omega,L}[f]=Q_{0,L}[\cosh(\omega X)f]-Q_{0,L}[\sinh(\omega X)f]\)
  (1.10). The shift flow acts on inputs by a **hyperbolic
  rotation generated by the position operator**. This is a geometric deformation,
  not a change of coefficients.
- **The sufficient route.** If \(L_j\to\infty\) and \(\omega_j\downarrow0\) with
  \(\lVert V_{\omega_j,L_j}\rVert\le1\) for every \(j\), then RH holds
  (Proposition 1.1 of the background).

## 3. The observation: the shift flow is abelian

> **Observation.** The operators \(\{V_{\omega,L}\}_{0\le\omega\le1/2}\) and
> \(\{G_{\omega,L}\}\) all lie in a single **commutative** algebra, for each
> fixed \(L\). Consequently \(V_{\omega,L}=\exp\!\big(-\int_0^\omega
> G_{s,L}\,ds\big)\) with no ordering, and the shift flow carries no holonomy
> beyond that exponential.

*Proof.* The kernel \(k_\omega\) is supported in \([0,\infty)\), so
\(V_{\omega,L}\) is a causal convolution truncated to \(I_L\); the weight
conjugation \(M_\eta^{-1}(\cdot)M_\eta\) replaces the kernel \(k(x-y)\) by
\(k(x-y)e^{\eta(x-y)}\), again a causal function of \(x-y\). Let \(A,B\) be two
such convolutions and write \(P_L\) for multiplication by \(\mathbf1_{I_L}\).
For \(f\) supported in \(I_L\), the function \(g=Bf\) is supported in
\([-L/2,\infty)\), and for \(x\in I_L\) the value \((Ag)(x)=\int_0^\infty
a(t)g(x-t)\,dt\) uses \(g\) only on \([-L/2,x]\subset I_L\). Truncating \(g\)
before applying \(A\) therefore changes nothing on \(I_L\), so
\(P_LAP_LBP_L=P_LABP_L\): the truncation is multiplicative on causal kernels.
Convolution is commutative, so \(AB=BA\) and the truncations commute. This is the
classical statement that the truncated convolution algebra on an interval is
commutative; in a discretization ordered by \(x\) it is the remark that
lower-triangular Toeplitz matrices are power series in one nilpotent shift. The
same applies to \(G_{\omega,L}\), whose symbol \(a_\omega\) is a multiplier in
the same variable with the same causality. A commuting generator family makes
the path-ordered solution of (1.7) the ordinary exponential, and
\(\log K_\omega=-\int_0^\omega a_s\,ds\) is the whole of it --- which is the
logarithmic differentiation already recorded under (1.4). \(\square\)

**What this costs the proposal.** The content of the non-Abelian Stokes theorem
is that path ordering can be traded for surface ordering of the
parallel-transported curvature; for an abelian connection it degenerates to
ordinary Stokes, and for a one-parameter family there is no surface at all. So
the mechanism named in the proposal does not yet have an object to act on. The
shift direction alone is a line with no color and no area.

This is not a refutation of the idea. It is a statement of what the idea is
missing, and it is precise: **the non-commutativity has to be supplied, and it
has to be transverse to \(\omega\).** Sections 4, 5 and 6 are the three places it
could come from, in increasing order of speculativeness and, I think, in
decreasing order of how likely they are to be cheap.

## 4. Transverse direction one: the endpoints, and the prime jumps

The proposal's own phrase --- "the change in the endpoints" --- names the
direction that is *not* in the commutative algebra of Section 3. The interval
\(I_L=(-L/2,L/2)\) enters through the compressions \(P_L\), and \(P_L\) does not
commute with the multiplier; differentiating in \(L\) gives a variation supported
at \(x=\pm L/2\), an honest endpoint variation of a line. So the natural object is
the **two-parameter family \(V_{\omega,L}\)**, and the question with content is

> Does \((\omega,L)\mapsto V_{\omega,L}\) carry a curvature? Compute
> \([\partial_\omega,\partial_L]\) on the family and see whether the endpoint
> terms cancel.

**Answered, and my expectation was wrong.** Proposition 6.2 of the manuscript
shows the connection is flat, because mixed partials of a single two-parameter
family commute; flatness is forced, not imposed, and there is no local curvature
to compute. The endpoint direction is still the live one, but for a different
reason than the one guessed here: the variation is rank one at the leading
endpoint (causality kills the trailing one), it fails to close on the form domain
by exactly the Sobolev borderline, and the prime data sits in the *atoms* of the
connection's kernel --- a flat connection with punctures, whose monodromy is the
surviving place for a non-abelian datum. Sections 6.1--6.4 of the manuscript
carry all of this.

Two cautions on the \(L\) direction, both of which this program has already paid
for once:

- **\(Q_L\) is not a family.** It is the single Weil functional \(W\) restricted
  to \(C_c^\infty(I_L)\); the correlations \(\langle F,U_rF\rangle\) vanish for
  \(|r|\ge L\) automatically, so nothing in a model has to know about \(L\), and a
  realization at one fixed \(L\) carries zero information (Section 3.1 and
  Remark 3.3 of the companion manuscript). The real \(L\)-dependence is in the
  **compression**, not in the functional. A deformation story about \(L\) must be
  a story about \(P_L\).
- **The flow in \(L\) is not smooth.** The constant \(c_L\) is a step function
  jumping at \(L=\log p\), the prime set changes there, and a delay of length
  \(L\) has zero action, which is what produces the strict cutoff. So the
  endpoint flow has **atoms at the primes**.

That second point is the most suggestive thing in this note. The
[bottleneck note](../../../brainstorm/inverse-bulk-brainstorm/BOTTLENECK_AND_OPERATOR_SEARCH_20260916.md),
Section 4F, argues that the two halves of the target call for two different
physical mechanisms --- a short-distance/OPE mechanism for the archimedean part
and a **periodic-orbit mechanism** for the primes --- and that Theorem 7.5 forbids
them from being two channels. An endpoint flow whose holonomy jumps each time the
endpoint is dragged past \(L=\log p\) is a monodromy picture, and monodromy is
exactly the mechanism that produces atoms at fixed separations from a single
object. In gauge language: as the line is extended, it crosses a defect at each
\(\log p\). That is a specific thing to look for and it is the first time this
program has had a candidate mechanism for the primes that is not a channel.

## 5. Transverse direction two: the bilinear energy balance

The two lines of (1.7) have different degrees, and the
difference is the useful part.

- **Operator level, linear in \(V\).** \(\partial_\omega V=-G V\) is the parallel
  transport equation \(\big(\partial_\mu-iA_\mu\big)W=0\). Matching here means
  identifying \(G_{\omega,L}\,d\omega\) with a pullback of a connection.
- **Energy level, bilinear in \(V\).**
  \(\partial_\omega\lVert V f\rVert^2=-2Q_{\omega,L}[Vf]
  =-\langle Vf,(G^*+G)Vf\rangle\): the line is cut at the deformation point, an
  object is inserted, and the two halves are paired. That is the *shape* of the
  Makeenko--Migdal loop equation, whose right-hand side
  \(\oint dy_\nu\,\delta^{(4)}(x-y)\,W[C_{xy}]W[C_{yx}]\) is likewise bilinear in
  the two segments meeting at the deformation point.

Read that correspondence in the direction that is informative: **the Weil form
occupies the slot that the parallel-transported field strength occupies on the
gauge side.** It is the insertion, not the observable. Every fingerprint the
target has then becomes a fingerprint of a local insertion, which is precisely
the kind of "before you pick a theory" constraint this program has been short of.
Section 8 extracts one.

The caution, and it is a real one: the loop equation is an equation for the
**expectation** and is nonlinear in the loop functional, whereas
(1.7) is linear at the operator level. The two are not
the same statement and it would be easy to match the wrong one. The linear
identity is the classical, kinematic content of the non-Abelian Stokes theorem;
the quantum loop equation carries a contact term and a factorization assumption
that the arithmetic side has nothing corresponding to. Any matching attempt
should say which of the two it claims.

## 6. Transverse direction three: where a color index would have to come from

Section 3 says the missing structure is an internal index that does not commute
with itself along the flow. The arithmetic side has one natural candidate and it
is not in the shift direction: the primes enter \(F'/F\) through
\(\sum\Lambda(n)n^{-1/2}T_{\log n}\), whose coefficients are scalars, but the
same sum for an Artin or automorphic \(L\)-function carries
\(\operatorname{tr}\rho(\mathrm{Frob}_p)\) --- the trace of a holonomy in a
representation, which is what a Wilson loop *is*. That is the one place in this
subject where a non-abelian holonomy is not an analogy.

I record this because it is the honest home of the proposal's non-commutativity,
and I flag it as the speculative item of this note: it changes the target from
\(\zeta\) to a family, it is adjacent to a large and crowded literature, and
nothing in the investigation so far has needed it. It should not be worked on
before Section 9's item 1 has been done.

## 7. What the accumulated rules already say

The [nine selection rules](../../source-selection-rules/notes/SELECTION_RULES.md)
and the [exclusion map](../../inverse-bulk-realization/notes/EXCLUSION_MAP_20260917.md)
apply to anything this investigation proposes. The load-bearing ones here:

| Rule | Bearing on a deformation flow |
|---|---|
| 1, reflection | The flow must commute with \(x\to-x\); free to check, and the involution is the functional equation. |
| 2, unboundedness | \(Q_L[\chi e^{iNx}]/\log N\to\lVert\chi\rVert^2\). This is what killed the Wilson-*loop* benchmark, and Section 8 restates it as a condition on the representation rather than on the geometry. |
| 3, 4, spectral weight and channel tower | \(b(\tau^2)+w_0=2\theta'(\tau)\) and \(n_\gamma(r)=\sum_n e^{-(2n+1/2)r}\). Section 8 reads these as a defect two-point function. |
| 7, criticality | The saturation is total; any mechanism with a margin uniform in \(L\) proves something false. Section 9's item 5 asks whether the flow formulation genuinely escapes this, and that is the decisive question for the whole direction. |
| 9, jump process | The non-pole part of the target is one Levy jump form with atoms at \(m\log p\). Section 4's crossing picture is a candidate mechanism for exactly those atoms. |

Two entries of the exclusion map are worth copying out because they are what
makes this direction admissible at all.

- **Section 8, item 7: "every actual theory".** None of the accumulated
  exclusions touches Yang--Mills or any protected sector; they are bookkeeping
  about forms. A gauge-theoretic proposal is not excluded by any of them.
- **Section 6, the transferable lesson.** An exclusion about a *decomposition*
  was once silently upgraded into an exclusion about a *realization*, and was
  wrong. Theorem 7.5 and Proposition 7.3 are statements about channels. A flow is
  not a channel decomposition, so neither constrains it --- and by the same token
  this investigation must not quote them as if they did.

## 8. Three necessary conditions this reading suggests

Proposed, not established. Each is cheap, each is in the style of the sibling
investigation's index, and I would want them checked before they are added to it.

**(W1) The connection is unbounded and its representation is infinite
dimensional.** Rule 2 excludes any pairing bounded in \(\lVert f\rVert_{L^2}\).
The holonomy of a connection valued in a compact group, in a finite-dimensional
representation, is unitary; its matrix elements and its character are bounded
functions, so every pairing built from them is bounded. This is the structural
reason the conformal Wilson benchmark failed, and it is better than the reason
currently recorded: \(W=2\cos\theta\) has spectrum in \([-2,2]\) *because* it is
the character of a holonomy in the fundamental of \(SU(2)\), not by accident of
one benchmark. Note also that \(V_{\omega,L}\) is not unitary --- it is a
contraction, and the object of interest is its defect --- so the connection to be
matched is not anti-Hermitian either.

**(W2) Non-commutativity must be transverse to the shift.** Section 3. Any
proposal whose non-abelian structure lies along \(\omega\) is describing
something the background has already collapsed to an ordinary exponential.

**(W3) If the line's parameter is the arithmetic coordinate, the defect
two-point function is \(|x-y|^{-1}\), with unit coefficient.** From
\(n_\gamma(r)\sim1/2r\), the archimedean energy is the Gagliardo seminorm at the
borderline exponent, so an insertion on the line would have to be a defect
operator of effective dimension \(\Delta=1/2\) with a fixed normalization. The
displacement operator of a Wilson line has \(\Delta=2\); the standard protected
scalar insertion has \(\Delta=1\). Neither is \(1/2\), so **the deformation whose
generator matches is not the displacement operator**, which is the first thing
one would have tried. *Caveat, and it is the manuscript's own (Section 3.1): the
arithmetic coordinate is not automatically the line's parameter, and this rule
applies only under that identification. Under the alternative identification of
Section 3 --- \(\omega\) is the parameter and \(x\) indexes the representation ---
the condition moves and has to be rederived.*

## 9. Ranked next steps

Cheapest and most decisive first. Items 1 and 5 are arithmetic and need no choice
of theory; do them before any gauge-theory work.

1. ~~Compute the mixed derivative.~~ **Done, in the manuscript.** The
   connection is flat and the question was the wrong one; the live questions are
   now Problems 6.5 and 6.6 there (close the endpoint flow, and the monodromy of
   the punctured flow), together with Problem 8.1, whether the flow formulation
   escapes the criticality rule. The registered check programme that came out of
   this is `numerics/check_causal_commutation.py`.
2. **Locate the prime jumps in that curvature.** Section 4. If the endpoint flow
   is smooth except at \(L=\log p\), write the jump and compare its mass with
   \(2(\log p)p^{-m/2}\), the atom of the Levy measure in selection rule 9.
3. **Test the boost reading of (1.10).** The shift acts by
   \(\cosh(\omega X)\), \(\sinh(\omega X)\). A hyperbolic angle deforming a line
   is a **cusp**, and a cusped Wilson line's expectation does satisfy a
   differential equation in the cusp angle of exactly the proposal's shape. This
   is the most concrete contact with 4D gauge theory available and it is where I
   would look first among specific theories. The obstruction to state plainly:
   a cusp anomalous dimension is a number and \(Q_{\omega,L}\) is a form on test
   functions, so the line must carry an infinite-dimensional label --- rule (W1)
   again.
4. **Run any candidate through the nine rules plus (W1)--(W3)** before computing
   anything about it. In particular check the band edge: the near-null directions
   of the compression are bandlimited below \(\gamma_1=14.1347\), and a candidate
   mechanism whose critical subspace sits elsewhere is dead without matching a
   prime.
5. **Settle whether the flow formulation escapes rule 7.** This is the decisive
   question. Rule 7 says a margin uniform in \(L\) at \(\omega=0\) proves
   something false. But Proposition 1.1 needs only \(\lVert V_{\omega_j,L_j}\rVert\le1\)
   along a sequence with \(\omega_j\downarrow0\), and the cumulative defect
   \(\langle f,D_{\omega,L}f\rangle=2\int_0^\omega Q_{s,L}[V_{s,L}f]\,ds\)
   (1.8) can be strictly positive where the integrand is not ---
   the background records exactly such a case, a negative generator direction at
   \(L=\log7\), \(\omega=10^{-11}\), with a positive defect on the same input.
   **If a strict contraction at fixed \(\omega>0\), uniform in \(L\), is
   consistent, then this is the only formulation in the program where a mechanism
   with a margin is not immediately self-refuting**, and that would be the
   strongest argument for the whole direction. I have not checked it. It should
   be checked before, not after, a theory is chosen.

## 10. What is claimed and what is not

- Section 3's Observation is a **written proof**, elementary, and it is the only
  new mathematics in this note.
- Section 2 restates (1.4), (1.7),
  (1.8), (1.9),
  (1.10) and Proposition 1.1 of the background; nothing there
  is new.
- Sections 4, 5, 6 and 9 are **assessment and proposed work**. Section 4's
  expectation about the mixed derivative is a guess and is labelled as one.
- Section 8's three conditions are **proposals**, not established rules, and
  (W3) carries an explicit identification hypothesis the program does not make.
- No source is constructed, no positivity is proved, no numerical value is
  quoted that is not already recorded elsewhere with its own scope, and nothing
  assumes the Riemann hypothesis.

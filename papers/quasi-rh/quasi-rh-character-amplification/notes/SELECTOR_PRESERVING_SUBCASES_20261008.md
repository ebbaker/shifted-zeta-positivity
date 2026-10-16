# Selector-preserving mixed bounds on two subcases

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.

**Status.** Under the imported analytic inputs, a positive Cauchy argument
proves the desired mixed bound on the upper plain-length band
`21/50 <= m <= 1/2` for the actual physical prime coefficients and a
sufficiently fine whole-slot mesh. This preserves the exceptional-row
selector throughout. It does not cover the entire requested box or prove
the new zero-free boundary. A second elementary reduction identifies a
sparse-cofactor subcase and the exact power cost of using it on all plain
ideals.

The source is the September 30 [companion preprint](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf),
PDF SHA-256
`8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.
Its Lemmas 8.2, 17.1, 18.1 and 19.1 are assumed here. No independent
validation of those proofs or Lean replay is claimed.

## 1. Hypotheses and a fixed-subset inequality

Use the manuscript's actual `M_r`, `S_m`, selected product `Q_I`, and
high primitive-conductor family `C_+`. Put

\[
\eta=1/5000,\qquad K=1+\delta m-\eta,
\qquad z_J=\sum_{i\in J}w_i.
\]

For the source application, the prime slots are the **original physical
prime sums** of source Sections 19.1–19.2, including their fixed ray-class
restrictions, fixed exclusions and smooth annuli. Relative to the common
character presentation, their coefficients are fixed finite linear
combinations of characters in the fixed group `Theta`. Their coefficients
and lists are independent of the row, their supports are pairwise
disjoint, and each positive slot obeys the mesh required by Lemma 18.1.

There are two separate requirements here. The original physical sums
have the smooth all-prime-annulus form of source (13.1), with ray-class
restrictions encoded by the finite character expansion; this form,
the coefficient class and the mesh make the fourth-moment input
applicable. The original physical sums also have the pointwise envelope
(2), by Lemma 19.1. Finite-ray coefficients on **arbitrary prime subsets**
do not by themselves justify either application: both the prime estimate
inside the proof of Lemma 18.1 and Lemma 19.1 use a logarithmic-derivative
argument that does not tolerate arbitrary prime deletion. For more
general lists, the fourth-moment bound and (2) must be explicit additional
hypotheses. The inverse moment does permit arbitrary bounded independent
prime coefficients, but this alone is insufficient for the mixed bound.

Assume the source's global `beta_* <= 7/8`. Then the fixed choice
`kappa=3/4` is legal in Lemma 18.1. Choose a subset of whole slots
`J subset I` such that

\[
2m+\frac92 z_J\le1. \tag{1}
\]

For positive `z_J`, this is exactly its affine capacity, with the two
plain lengths both equal to `m`; no additional kappa penalty occurs.
For `J` empty, its unrestricted zero-slot assertion applies instead.
The marked inverse retains its original two strict capacity margins.

The family `C_+` has primitive conductor exceeding `U^(2m-1/1000)`.
Every member of the fixed finite group `Theta` has bounded primitive
conductor. Since `2m-1/1000 >= 719/1000 > 0`, all sufficiently large
`U` therefore put `C_+` inside the nonexceptional row family required
by the positive-slot fourth moment. Bounded smaller scales are covered
by the constants. Common orientation is handled by conjugating the whole
product when necessary; the fixed finite character group is closed under
this operation. Every zero extension remains present.

Require the following pointwise envelopes, uniformly on the bin; source
Lemmas 8.2 and 19.1 supply them for the actual inverse profile and original
physical prime sums just specified:

\[
|M_r|^2\ll U^{\delta r+\epsilon}(1+T_1)^A,
\qquad |Q_{I\setminus J}|^2
\ll U^{\delta(z-z_J)+\epsilon}(1+T_1)^A. \tag{2}
\]

For a fixed amplitude-profile bin, the second exponent may instead be
`2 G(I\setminus J)`, where `G(H)=sum_{i in H}g_i w_i`, with its
prescribed small amplitude-bin loss. The universal envelope (2), rather
than a profile-specific amplitude bound, is used below.

**Fixed-subset bound.** Under these hypotheses,

\[
\sum_{u\in\mathcal C_+}|M_r(u)S_m(u)Q_I(u)|^2
\ll_\epsilon
U^{1+\frac\delta2(r+z-z_J)+\epsilon}(1+T_1)^A. \tag{3}
\]

Indeed, pointwise the summand equals

\[
|M_rQ_{I\setminus J}|\,|M_rQ_I|\,|S_m^2Q_J|.
\]

Bound the first factor by (2), and apply Cauchy to the latter two.
Lemma 17.1 bounds the first resulting squared norm by `U^(1+epsilon)`.
Lemma 18.1 bounds the second by the same power. Both norms are first
formed over `C_+` and then enlarged positively into their stated theorem
domains. The signed pair kernel is never enlarged, and no smoothness of
the selector is required. The profile-specific version has exponent
`1+delta*r/2+G(I\setminus J)`.

## 2. Whole slots remove the upper plain-length band

Let `h=max_i w_i` and choose a fixed small capacity decrement `nu >= 0`.
Greedy selection within `I` produces whole slots with

\[
z_J\le c_m:=\frac{2(1-2m)}9,
\qquad z-z_J\le(z-c_m)_++\nu+h. \tag{4}
\]

For example, if all slots fit below `c_m-nu`, take all of them;
otherwise take a prefix just before crossing `max(0,c_m-nu)`.
The discarded last slot costs at most `h`. At `c_m=0` take the empty
set. The selected coefficients and supports are unchanged. Require

\[
\ell_{\rm sel}:=\nu+h\le1/1000, \tag{5}
\]

as well as the source's possibly finer mesh. This is a hypothesis on
the original physical subdivision, not permission to replace an existing
prime coefficient array with a new row-dependent one.

Because `z <= (1-r)/2`, (3)–(4) save at least

\[
\delta\left\{m-\frac r2
-\frac12\left(\frac{1-r}2-c_m\right)_+
-\frac{\ell_{\rm sel}}2\right\} \tag{6}
\]

below exponent `1+delta*m`. In the requested box
`(1-r)/2 > c_m`; without the selection loss the braces are exactly

\[
\frac79m-\frac r4-\frac5{36}. \tag{7}
\]

For `m >= 21/50`, `r <= 37/50`, and `delta >= 9/25`, the ideal
saving is at least

\[
\frac9{25}\left(
\frac79\frac{21}{50}-\frac14\frac{37}{50}-\frac5{36}
\right)=\frac1{1000}. \tag{8}
\]

The selection loss in (6) is at most
`(21/50)(1/1000)/2=21/100000`. Subtracting the requested
`eta=1/5000` therefore leaves the fixed margin

\[
\boxed{
\sum_{u\in\mathcal C_+}|M_rS_mQ_I|^2
\ll_\epsilon U^{K-59/100000+\epsilon}(1+T_1)^A,
\qquad 21/50\le m\le1/2.} \tag{9}
\]

The previously proved low primitive-conductor contribution has margin
`1/6250`, so adding it yields the same desired bound over the full `C`,
with margin at least `1/6250`. The complete signed large-ratio block is
then also controlled at the target scale by the manuscript's reduction.
No termwise absolute bound for that block is asserted.

This is only a partial band. For example, at
`r=18/25, m=2/5, delta=2/5`, the ideal saving in (7), multiplied by
`delta`, is `-7/2250`. Thus the displayed upper bound alone cannot cover
the full rectangle. This does not give a lower bound for the actual norm.
Near a saturated marginal crossing, the known abstract correlated model
still prevents a general saving from these marginal inputs alone.

For the original physical sums, the conservative pointwise envelope in
(2) uses the smooth-profile uniformity of Lemmas 8.2 and 19.1. Consequently
the same argument applies
to the required derivative profiles and finite Sobolev parameter cover,
with a fixed polynomial height cost and the original cumulative frequency
allowance. For more general lists the pointwise-envelope hypothesis must
explicitly cover those derivative profiles as well. A profile-specific
`G` bound at one parameter is not silently transferred to its derivatives.
All analytic losses and height growth
must still be chosen within the explicit positive margin in (9).

## 3. A sparse-cofactor subcase, and its limitation

Here is another positive reduction that does not transform the selector.
Suppose a restricted part of the original plain ideal sum consists of
unique products `k=a p`, with

\[
\mathrm Na\asymp U^v,\quad \mathrm Np\asymp U^t,
\quad v+t=m,\quad \#\mathcal A\ll U^b.
\]

Take `a` from a fixed row-independent family `A`, and `p` from a fixed
prime list disjoint from all original physical slot lists. For a literal
subsum, uniqueness can be ensured by requiring `a` to avoid the entire
new prime list, so that `p` is the unique prime of that list in `k`.
Retain the actual profile `B(Na Np/U^m)` and every character zero.
No inverse/plain coprimality assumption is needed for this positive norm
argument.

Require fixed positive margins `c'_1,c'_2` such that

\[
r+2(z+t)\le1-c'_1,\qquad
2r+8(z+t)\le3-c'_2. \tag{10}
\]

For each fixed `a`, the plain subsum equals `U^(-v/2) psi_u(a)` times
a normalized prime polynomial of length `t`, with profile
`B((Na/U^v)y)`. This is a uniformly smooth annular family. The row
scalar has modulus at most one. Lemma 17.1, followed by the triangle
inequality over the `a`'s in the row Hilbert space, therefore gives

\[
\sum_{u\in\mathcal C_+}|M_r S_{\mathcal A,p}Q_I|^2
\ll_\epsilon U^{1+2b-v+\epsilon}(1+T_1)^A. \tag{11}
\]

This meets the mixed target whenever
`2b-v <= delta*m-eta`, with strict room for losses. It is a genuine
sparse-cofactor partial statement, conditional only on the marked input.

For all cofactors in an annulus, ideal counting supplies only `b=v`.
Then (11) has exponent `1+v=1+m-t`. At
`z=(1-r)/2-rho`, the first width in (10) forces `t<rho`.
The remaining deficit compared with `K` is at least

\[
(1-\delta)m-\rho+\eta. \tag{12}
\]

Thus extracting one prime and paying for all cofactors does not close
the saturated problem. A general decomposition into sparse cofactor
families with adequate total cost has not been proved here. Summing many
individually favorable subcases by triangle inequality can lose their
saving. This argument therefore does not replace the surviving arithmetic
problem below `m=21/50`.

The current conditional candidate remains `7/8-1/24000`; the proposed
`7/8-1/20000` still requires control of the remaining class.

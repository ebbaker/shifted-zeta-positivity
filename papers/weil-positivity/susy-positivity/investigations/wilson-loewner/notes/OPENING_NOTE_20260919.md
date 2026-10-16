# A Loewner-generated Wilson observable

19 September 2026. OpenAI GPT-6 (Codex), for Edward Baker.

**Status:** scope and target, followed by a concrete first calculation in
[the companion note](SMOOTH_VARIATION_AND_CONSTANT_DRIVER_20260919.md).
No physical realization or positivity theorem is assumed.

## 1. The construction being investigated

Edward's proposal is to let Loewner evolution generate the contour for a
Wilson line. The intended sequence is

\[
\text{driving data}\longrightarrow C
\longrightarrow \bar q(y)\,\mathcal P
\exp\!\int_C(iA_\mu dx^\mu+n^I X_I|dx|)\,q(x)
\longrightarrow\text{a correlation or transfer operator}.
\]

The scalar coupling, endpoint polarization, field measure, adjoint and
operator norm must be specified. A conformal map supplies none of these by
itself. Conversely, restrictions on a simple observable of that map do not
automatically restrict the displayed field-dependent observable.

## 2. What is inherited, and what is being reopened

The [Loewner realizations section](../../loewner/sections/04_realizations.tex)
excludes particular identifications: rotation-averaged analytic composition
reduces to dilation; a translation-invariant radial transport law is forced
by its far-field limit to be a pure delay; and the tested radial chord and
first-passage laws do not match the gamma delay. Those tests should be retained.
Their conclusions do not cover the combined observable above.

The broader closure also uses a process-independence claim requiring a
stochastic-clock qualification: the independent Jacobi process occurs after
the time change of the squared-Bessel ratio, not at its original clock.
See [Warren-Yor, Proposition 8](https://www.numdam.org/item/SPS_1998__32__328_0.pdf).
Nonrecoverability of that canonical split does not exclude every observable
with the same marginal law. Likewise, the formal-dimension representation
of a gamma ratio does not require every realization to vary its spatial
dimension. These qualifications motivate this separate investigation; the
older notes are not silently revised.

The [Wilson angular/Robin note](../../wilson-lines/notes/ANGULAR_SMEARING_AND_ROBIN_MODEL_20260919.md)
supplies a finite free endpoint covariance, common-reference bulk contour
conditions and an auxiliary gamma determinant. Its physical endpoint,
reflection and arithmetic problems remain open here too.

## 3. The mathematical target

With \(s=\tfrac12+p\), \(a=\tfrac12-\omega\), \(b=\tfrac12+\omega\), the
required transfer is

\[
K_\omega(p)=\frac{\xi(s-\omega)}{\xi(s+\omega)}
=\frac{(p+a)(p-b)}{(p+b)(p-a)}\,
\pi^\omega\frac{\Gamma((p+a)/2)}{\Gamma((p+b)/2)}
\sum_{n\ge1}\widetilde c_n e^{-p\log n},
\]

\[
\widetilde c_n=n^{\omega-1/2}
\prod_{\ell\mid n,\ \ell\ {m prime}}(1-\ell^{-2\omega}).
\]

The displayed series converges absolutely for \(\Re p>b\). On finite
intervals, the parent's [elementary assembly](../../loewner/sections/05_contraction.tex)
provides an exact-kernel benchmark using only \(n<e^L\). Reuse that instrument
when a candidate observable has actually been derived.

The program needs positivity of the complete Weil form at every support
length, or the established corresponding contraction criterion along a
family reaching \(L\to\infty\), \(\omega\downarrow0\). Positivity of an
isolated gamma kernel, finite matrices, or a stochastic expectation in a
different norm does not provide that criterion. The exact prime weights,
contacts and pole terms must arise from the construction rather than be
inserted into its definition.

## 4. First milestone and initial outcome

The first milestone is the infinitesimal evolution of a smooth Wilson
observable, with its endpoint terms retained. The companion note derives it
and establishes a sharper geometric fact: with the inherited constant
scalar coupling and fixed bulk charge, a planar contour becomes a vertical
line under inversion. Thus the current semicircles already have a Loewner
description, but only with constant driving.

A varying-scalar control escapes this restricted rigidity. Its physical
defect endpoint conditions are the next calculation. The general possibility
of coupling Loewner curves to internal fields also has precedent in
[Bettelheim et al.](https://arxiv.org/abs/hep-th/0503013); that construction
does not supply the present defect theory or its arithmetic transfer.

**Ledger:** the transfer factorization and free endpoint kernel are inherited;
the combined mechanism is a proposal; the companion note's classical and
Clifford statements are derived under explicit hypotheses. There is no
new RH or interacting positivity result.

# Continuation from the rescaled theta generator

28 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort xhigh**.
Chat0014, Add Laplacian motivation to book.

Continue the kernel and auxiliary-flow brainstorm from the exact
zero-time formulas below. Edward Baker wants \(A\) or \(\Theta\) to be
primary, with differential operations visible. He asks to focus on
\(t=0\), regarding Newman evolution as a later flow direction that might
be replaced or combined with a more useful auxiliary evolution.

**Do not implement manuscript changes yet.** Accumulate proposed changes
in [book changes note01](../book/changes/01_GENERATING_FUNCTIONS_AND_KERNEL_CHANGE_WORKING_NOTE_20261028.md)
until Edward Baker finalizes it and requests the combined revision.
Continue conceptual work in this brainstorm folder. This note is the
latest handoff; [Brainstorm07](07_NATURAL_AUXILIARY_EVOLUTION_CONTINUATION_20261028.md)
retains the earlier design requirements and cautions. The possible
relaxation from exact observation preservation to preservation up to a
known nonvanishing factor is a design question, not an accepted change.

## The clean formulas

Keep
\[
A(r)=\sum_{n\ge1}e^{-\pi n^2r^2},\qquad
\Theta(r)=1+2A(r),\qquad
\Theta(r)=r^{-1}\Theta(1/r).
\]
The initial Laplacian motivation remains
\[
\Phi(u)=\frac14r^{5/2}\Delta_3\Theta(r),\qquad r=e^{2u}.
\]

**Smooth Euclidean potential.**
\[
\boxed{V(r)=1+r^{-1}-\Theta(r)>0.}
\]
It extends smoothly to \(V(0)=1\), is asymptotic to \(1/r\) at infinity,
and satisfies \(-\Delta_XV=(\Delta_3\Theta)(|X|)\), without a central
point source or a unit-sphere jump. The direct generating-function
transform is
\[
\boxed{
H(0,z)=\frac{1+z^2}{256\pi}
\int_{\mathbb R^3}
[1+|X|^{-1}-\Theta(|X|)]|X|^{-5/2+iz/2}\,dX,
\quad |\operatorname{Im}z|<1.
}
\]
This is the cleanest full-space Euclidean formula found in this chat.
The strip includes every real observation. The factor \(1+z^2\) must
not be evaluated at \(z=\pm i\) while ignoring divergence of the integral.
The complete product continues to the original entire \(H(0,z)\).

**Square-root rescaling and logarithmic radius.**
\[
\boxed{
u=\frac12\log r,\qquad
G(u)=\frac12e^uV(e^{2u})
=\cosh u-\frac12e^u\Theta(e^{2u}).
}
\]
The function \(G\) is smooth, positive and even, with tails
\(G(u)\sim\tfrac12e^{-|u|}\). Its two basic identities are
\[
\boxed{(1-\partial_u^2)G=8\Phi,\qquad
16H(0,z)=(1+z^2)\int_{\mathbb R}G(u)e^{izu}\,du.}
\]
The integral again has \(|\operatorname{Im}z|<1\).
The rescaling is geometrically selected: the power \(r^{1/2}\) both
removes the first derivative from the logarithmic radial Laplacian and
turns Kelvin symmetry into ordinary reflection.

**Three-dimensional cylinder.** Let
\[
\mathcal C=\mathbb R\times\mathbb S^2,\qquad
 d\mu=du\,d\sigma,\qquad d\sigma=\frac{d\omega}{4\pi},
\qquad \mathcal L=1-\partial_u^2-4\Delta_{\mathbb S^2}.
\]
The product metric is \(du^2+\tfrac14g_{\mathbb S^2}\), whose volume is
\(\pi d\mu\). It is conformal to the punctured Euclidean metric, not
identical to it. The economical three-dimensional formulation is
\[
\boxed{
\mathcal L e^{izu}=(1+z^2)e^{izu},\qquad
16H(0,z)=\int_{\mathcal C}G(u)\,\mathcal L e^{izu}\,d\mu.
}
\]
Initial angular dependence is constant; later fields can depend on
\(\omega\). Keep the measure and metric explicit when comparing
energies or evolution equations.

**Mellin alternative.** With \(\lambda=(1+iz)/2\),
\[
\boxed{
16H(0,z)=\lambda(1-\lambda)
\int_0^\infty [1+r^{-1}-\Theta(r)]r^{\lambda-1}\,dr,
\quad 0<\operatorname{Re}\lambda<1.
}
\]
This makes reflection \(\lambda\mapsto1-\lambda\) simple; the
\(u,z\) notation keeps the original real spectral axis more visible.
Use \(\lambda\), not \(s\), for this spectral coordinate.

## Keep the tradeoff visible

The preceding smooth generators have exponential or power tails and a
strip of integral convergence. The earlier alternative
\[
P(u)=e^{|u|}A(e^{2|u|}),\qquad
16H(0,z)=1-(1+z^2)\int_{\mathbb R}P(u)e^{izu}\,du
\]
has an entire integral, but \(P\) has a derivative jump at zero. They
are related exactly by \(G=\tfrac12e^{-|u|}-P\). No constant or boundary
term has been dropped. Keep \(\Theta\) and these displayed rescalings
visible rather than hiding them behind unexplained abbreviations.

## The flow choice remains open

Exact preservation of all real pairings in the cylinder formula fixes
the spherical mean of \(G_s\), by Fourier uniqueness. It does not allow
nontrivial radial evolution. Rotation-equivariant unique evolution from
exactly radial data remains radial without additional structure.

If preservation up to a known nonzero factor is allowed, the natural
cylinder heat flow has a simple exact effect:
\[
\partial_sG_s=\Delta_{\mathcal C}G_s
\quad\Longrightarrow\quad
H_s(z)=e^{-sz^2}H(0,z).
\]
It preserves zeros and their multiplicities and permits recovery of the
original \(H\). It does not preserve the value of every pairing.
Deciding whether that relaxation is acceptable is the first design
question for the next chat; do not silently assume it.

Newman flow can be transported to the same variable through
\(\partial_tG_t=\mathcal L^{-1}u^2\mathcal L G_t\) on the canonical
source-defined class. A constant linear combination with cylinder heat
therefore gives
\[
\partial_\tau\mathscr H=-\alpha\mathscr H_{zz}-\beta z^2\mathscr H.
\]
[Brainstorm08, Section 7](08_ZERO_TIME_RESCALINGS_AND_FLOW_BRAINSTORM_20261028.md)
solves this benchmark exactly as a nonzero Gaussian factor times
\(H(T(\tau),c(\tau)z)\). For constant \(\alpha,\beta\ge0\) in the
stated interval, it reparametrizes the existing zeros and collisions.
A useful unified flow needs an additional mechanism beyond this
particular linear quadratic combination. Nonlinear or coupled-field
constructions remain open. The two separate generators do not commute,
so a two-parameter formulation needs compatibility, not just two equations.

## Suggested next bounded return

First decide whether a strip integral with analytic continuation is
acceptable, or whether the defining integral must converge for every
complex spectral argument. Then compare exact observation preservation
with preservation up to a known nonvanishing factor. Then choose whether to work with the Euclidean
potential \(V\) or the cylinder generator \(G\), retaining the explicit
\(\Theta\) formula in either case. Formulate one natural auxiliary or
unified evolution and say what additional spatial behavior at a double
zero it is meant to reveal. Keep the geometric effect separate from any
unproved theta-specific estimate needed for a contradiction.

The derivations and scope are in
[Brainstorm08](08_ZERO_TIME_RESCALINGS_AND_FLOW_BRAINSTORM_20261028.md).
Consult the [result index](../../../../result-summaries/README.md), especially
[geometric realizations](../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md),
and the [pattern index](../../../../avoid/README.md), especially
[coordinate lifts](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md)
and [shared control premises](../../../../avoid/02_shape_only_arguments_and_the_controls.md).
The positive collision control in Note01 survives the linear benchmark;
its missing canonical theta arithmetic is not used by that benchmark.
These are same-assistant analytical results and proposals, not an
independent review or a new collision exclusion. The formal research
program and manuscript have not been rewritten.

Register the next chat under its own identity in this investigation's
chat-histories folder; do not reuse chat0014's identity. Refresh its history
using the repository's standing workflow.

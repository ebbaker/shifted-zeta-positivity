# Quasi-RH and the de Bruijn–Newman constant

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.

Quasi-RH gives a positive upper bound on the de Bruijn–Newman constant through
classical strip contraction. Combined with the prime-variance criterion in
this investigation, the precise bound is

\[
0\leq\Lambda_{\mathrm{DN}}\leq\frac{\delta_*^2}{2}.
\]

This does not exclude a positive constant. An arithmetic theorem excluding
every optimal variance exponent strictly between zero and one would instead
prove that quasi-RH implies RH. No such theorem is supplied by the existing
variance reductions or by the classical heat-flow estimate.

## The sign and the hypothesis

Here quasi-RH means that a fixed \(\theta<1\) bounds the real parts of all
nontrivial zeta zeros. Write \(\delta=2\theta-1\). The functional equation
then puts every zero in \(|\Re\rho-1/2|\leq\delta/2\), with
\(0\leq\delta<1\).

[Rodgers and Tao](https://arxiv.org/abs/1801.05914) proved unconditionally
that \(\Lambda_{\mathrm{DN}}\geq0\). RH is equivalent to
\(\Lambda_{\mathrm{DN}}\leq0\), and consequently to equality with zero.
Ruling out finite negative values supplies the already-known side of the
inequality. The needed step excludes positive values.

## Conversion from a zero strip

Use the conventional normalization

\[
H_0(z)=\tfrac18\xi(\tfrac12+iz/2),\qquad
H_t(z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\qquad \partial_tH_t=-\partial_z^2H_t.
\]

Then \(\rho=\beta+i\gamma\) corresponds to
\(z=2\gamma+i(1-2\beta)\). The zeta strip above therefore becomes
\(|\Im z|\leq\delta\).

[Polymath, Theorem 3.2](https://arxiv.org/html/1904.12438),
restating de Bruijn's theorem, gives the later strip half-width
\(\sqrt{\max(y_0^2-2(t-t_0),0)}\) from half-width \(y_0\) at time
\(t_0\), and hence \(\Lambda_{\mathrm{DN}}\leq t_0+y_0^2/2\).
Taking \(t_0=0\), \(y_0=\delta\) yields our deduction

\[
\boxed{\quad 0\leq\Lambda_{\mathrm{DN}}\leq\delta^2/2.\quad}
\]

For example, a zero-free half-plane \(\Re s>7/8\) gives
\(\delta=3/4\) and \(\Lambda_{\mathrm{DN}}\leq9/32\).
This particular transfer is weaker than Polymath's published unconditional
bound \(\Lambda_{\mathrm{DN}}\leq0.22\), Theorem 1.1 in the same paper.
The value \(7/8\) is the statement in the
[October 2026 release catalogue](https://github.com/openai/math/blob/main/CONTENTS.md);
the calculation here is conditional on that input and does not audit its proof.

## Why repetition of strip contraction does not prove RH

For \(0\leq t<\delta^2/2\), the guaranteed later strip has squared
half-width \(\delta^2-2t\). Applying the same estimate again gives

\[
t+\frac{\delta^2-2t}{2}=\frac{\delta^2}{2}.
\]

The absolute upper bound on the transition time is unchanged. The narrower
strip belongs to \(H_t\), not to the original \(H_0\). The arithmetic
identities for zeta cannot simply be reapplied to the deformed function as
though it were zeta again.

A simple illustration is \(F_t(z)=z^2+a^2-2t\), \(a>0\). It satisfies
the same differential equation, starts with zeros at \(\pm ia\), and
has exclusively real zeros exactly for \(t\geq a^2/2\). This is only a
toy heat-flow example, not a counterexample involving zeta or the full
hypotheses of the zeta Fourier kernel. It shows why the differential equation
and a bounded initial zero strip alone cannot force transition at zero.

## The exact arithmetic target in this project

The internally reviewed fixed-probe theorem in
[the manuscript](../manuscript.tex), Theorem 1.1, asserts

\[
\mathcal V_g(X)=O(X^{2+\delta})
\quad\Longleftrightarrow\quad
|\Re\rho-1/2|\leq\delta/2\quad\text{for every nontrivial zero}.
\]

Its optimal exponent is attained:

\[
\delta_*:=\inf\{\delta\in[0,1]:\mathcal V_g(X)=O(X^{2+\delta})\}
=2\sup_\rho(\Re\rho-1/2).
\]

Thus quasi-RH says \(\delta_*<1\), while RH says \(\delta_*=0\).
The Newman inequality at the start follows by combining this project theorem
with the classical strip theorem; it is not a new independent arithmetic
estimate.

A sufficient new theorem would improve any positive admissible exponent
below one to a strictly smaller exponent for the actual prime response.
Applying it directly at the attained \(\delta_*\in(0,1)\) would contradict
optimality. Equivalently, one could prove a contraction
\(\delta\mapsto q\delta\), \(0<q<1\), valid repeatedly. The constants and
starting thresholds may change at every step. Global bounds along any
sequence \(\delta_j\to0\) suffice for RH.

The [signed Mellin continuation](SIGNED_MELLIN_CONTINUATION_20261004.md),
Section 5, removes a subpower loss at a given exponent:
\(X^{3-\kappa+o(1)}\) becomes \(O(X^{3-\kappa})\).
It does not increase \(\kappa\), so it supplies no strict descent.

The manuscript's finite-prefix obstruction constructs other
coefficient sequences preserving any chosen finite prefix, PNT-type control,
the same probe preparation and diagonal asymptotics, while maintaining any
prescribed positive variance exponent. It rules out descent based only on
those inputs. It does not rule out an argument using the additional
multiplicative structure, prime-power support, or signed correlations of
the actual von Mangoldt coefficients, and is not a disproof of the desired
implication.

## Scope of the literature conclusion

The appropriate conclusion is that no established proof of quasi-RH implying
RH was verified in this check, not that nobody has claimed one. For example,
[Puglisi, arXiv 2210.03121](https://arxiv.org/abs/2210.03121), explicitly
claims that implication. Its presence on arXiv is not by itself verification
of the argument. The mathematical diagnosis above depends on the precise
classical heat-flow theorem and the local exponent equivalence, not on a
claim that the literature contains no proposed proof.

The research direction suggested by the question remains meaningful:
identify arithmetic information that forces a strict improvement at a
hypothetical positive optimal exponent. The existing generic estimates do
not provide that information.

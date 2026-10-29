# Classical attribution of book equation (2.1)

28 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort xhigh**.
Chat0016, *Identify equation 2.1 Mellin form*.

**Status: attribution and normalization check of a classical identity.**
The continuation note uses labels C1–C10; equation (2.1) is the Mellin
formula in [the linked book](../book/main.tex), label `eq:mellin`.
The book source is unchanged by this check.

Write \(s=\lambda\), \(\Theta(r)=\sum_{n\in\mathbb Z}e^{-\pi n^2r^2}\),
\(V(r)=1+r^{-1}-\Theta(r)\), and
\[
M_V(s)=\int_0^\infty V(r)r^{s-1}\,dr.
\]
Then the precise classical identification is
\[
M_V(s)=-\pi^{-s/2}\Gamma(s/2)\zeta(s)
=\frac{2\xi(s)}{s(1-s)},\qquad 0<\Re s<1.
\]
Thus (2.1) is the classical theta–Mellin representation with the endpoint
terms absorbed into the potential. No new scalar zeta representation is
claimed. The checked primary formula is on printed p.3 of Riemann's 1859
paper in the Wilkins translation; DLMF25.5.13–14 give its modern form.
See [reference annotation13](../references/13_RIEMANN_THETA_MELLIN_ATTRIBUTION_20261028.md).

## Direct comparison

Set
\[
J(s)=\int_1^\infty(\Theta(r)-1)(r^{s-1}+r^{-s})\,dr.
\]
This integral is entire. In DLMF25.5.13 put \(x=r^2\) and
\(\omega(x)=(\Theta(\sqrt{x})-1)/2\). Its formula becomes
\[
\pi^{-s/2}\Gamma(s/2)\zeta(s)=\frac1{s(s-1)}+J(s).
\]
On \((0,1)\) use \(V(r)=1-r^{-1}(\Theta(1/r)-1)\), and on
\((1,\infty)\) use \(V(r)=r^{-1}-(\Theta(r)-1)\). Substitution
\(r\mapsto1/r\) in the first theta remainder gives
\[
M_V(s)=\frac1s+\frac1{1-s}-J(s)
=-\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]
Multiplication by \(s(1-s)\) proves exactly the book's normalization
\(s(1-s)M_V(s)=2\xi(s)=16H(0,z)\), with \(s=(1+iz)/2\).

## Domain and attribution scope

Since \(V(r)\to1\) at zero and \(V(r)\sim r^{-1}\) at infinity,
the integral converges absolutely precisely for \(0<\Re s<1\).
It is an ordinary convergent integral there, despite the useful description
as a subtracted or regularized theta Mellin transform. The three terms of
\(V\) must not be integrated separately over the whole positive axis.
The expression \(1/[s(1-s)]-J(s)\) supplies meromorphic continuation;
\(s(1-s)M_V(s)=1-s(1-s)J(s)\) continues to the entire function \(2\xi(s)\).

Attribution concerns the scalar Mellin identity. This check does not settle
the historical novelty of the book's Euclidean-potential presentation or
any flow construction. No proposed collision criterion or numerical claim
is involved. This follows the repository's
[result index](../../../../result-summaries/README.md), particularly
[geometric realizations](../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md),
and [pattern index](../../../../avoid/README.md), particularly
[coordinate re-realizations](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md)
and [checked attribution](../../../../avoid/16_unchecked_imports_and_novelty_claims.md).

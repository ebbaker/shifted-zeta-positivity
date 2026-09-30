# Internal review of the critical localization, tails, and crossings

29 September 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. This is an internal same-model review,
not independent human or specialist refereeing. The arithmetic-crossing
portion is a self-check of this reviewer's derivation. The boundary-model
portion was read separately; the frequency-tail argument was developed in
parallel and then checked against its written proof. These distinctions
matter when assessing the strength of the review.

## Verdict and scope

The following three derivations and their synthesis pass this internal
mathematical check on their stated domains:

- [Critical boundary localization and countermodel](../notes/SONIN_CRITICAL_BOUNDARY_MODEL_20260929.md).
- [Uniform frequency tails](../notes/SONIN_PHASE_FREQUENCY_TAILS_20260929.md).
- [Arithmetic crossing terms](../notes/SONIN_PHASE_ARITHMETIC_CROSSINGS_20260929.md).
- [Critical-limit synthesis](../notes/SONIN_CRITICAL_LIMIT_STATUS_20260929.md).

The package proves full source-trace finiteness and uniform frequency
tails near the critical line, the limiting critical-zero measure of the
positive majorant, and an exact arithmetic comparison including crossing
residues. The pole-factor extension gives finiteness and uniform tails
on every bounded sigma strip above one half. The actual kernel projection
can still lose trace through the
return operator. The rational example proves that the local phase data
and a positive prelimit cutoff gap do not exclude that loss. It is
explicitly a separate model and gives no counterexample about zeta itself.

No unresolved mathematical correction was found in the displayed claims.
One wording issue was corrected: the model is now described as a
"closing-gap family" to avoid suggesting a uniform positive gap.
This did not affect any calculation. The notes do not establish
return-mass vanishing, arithmetic convergence of the actual projection,
or RH. This review includes no numerical certificate or exhaustive novelty
search.

## Frequency tails and operator ideals

The local zero-factor argument is valid uniformly even when sigma equals
or approaches the real part of a zero. The factors

\[
B_d(t)=\frac{t-\gamma-id}{t-\gamma+id}
\]

have phase derivative \(2d/(d^2+(t-\gamma)^2)\), including its sign.
The zero-width factor is set equal to one, consistently with the removable
phase on that vertical line. Removing the finitely many nearby factors
leaves a background with derivative \(O(\log(2+|j|))\) on each fixed
width window. The stated local logarithmic-derivative estimate and local
zero count are the applicable primary inputs; neither assumes RH.

The key estimate is width independent:

\[
\iint\frac{|B_d(t)-B_d(s)|^2}{(t-s)^2}\,dt\,ds=4\pi^2
\quad(d\ne0).
\]

Its difference quotient separates into two integrable Cauchy factors, so
there is no hidden factor involving \(1/|d|\). A finite product of
\(O(\log(2+|j|))\) such factors costs at most the square of that count.
The compact smooth cutoff times the Lipschitz background has the claimed
energy bound. The extension of the background is continuous at the interval
endpoints and constant outside; the cutoff support is strictly inside that
interval. Hence the global energy estimate does not extend an unjustified
local factorization to the entire real axis.

The Fourier normalization also checks:

\[
\|[P,q(D)]\|_{\rm HS}^2
=\frac1{4\pi^2}\iint
\frac{|q(t)-q(s)|^2}{(t-s)^2}\,dt\,ds.
\]

The factorization
\(L=P V^*\chi V P\) is exact. Commuting the frequency cutoff past
\(P\) gives one off-diagonal block of the localized phase multiplier
and one Hilbert--Schmidt commutator. This proves the positive sandwich
trace bound for \(L\). The symmetric factorization
\(C^2=\chi V^*P V\chi\) proves the same bound for \(C^2\), including
any spectral subspace at value one. Domination by \(L\) applies to
\(\Pi\), to \(H=L-\Pi\), and to every positive Abel approximant.

The resulting unit-window bound is therefore enough for full Schwartz
tails, by summing source suprema over unit intervals. No idempotence of
\(L\) or of the Abel approximants is used. The claims are about positive
sandwiches and Hilbert--Schmidt factors; the notes correctly avoid claiming
global trace class of arbitrary unsandwiched products or global Schwartz
bounds on \(\widehat Fv_\sigma\).

The bounded-sigma-strip extension is also valid. The additional inverse
pole factor has derivative
\(-2(\sigma-1)/((\sigma-1)^2+t^2)\) and the same energy \(4\pi^2\).
Extracting it removes the only loss of uniformity as sigma approaches one.
At sigma one the factor is set equal to one, consistently with the
removable real-parameter phase. The factor count increases by at most one,
so every energy and positive-trace argument remains valid with a constant
depending only on the bounded strip. This proves full source finiteness
and the scalar boundary decomposition for every fixed sigma greater than
one half, not only in the critical neighborhood.

For the full-source scalar boundary identity, both positive traces are
finite by the preceding domination. The crossing scalar is defined through
\(C T P a(D)\chi\), a bounded operator times a trace-class Schwartz
Hankel block. Compact frequency cutoffs converge in trace norm for that
block. Thus removing those cutoffs is justified without assigning a trace
to an unproved globally trace-class off-diagonal sandwich.

## Actual boundary localization

The local factorization by critical-zero factors has a smooth remainder
converging to one. The orientation of their poles is essential: the poles
are in the lower frequency half-plane, the convolution kernels are supported
on the negative spatial half-line, and consequently
\(P B_\epsilon(D)\chi=0\).

The exact identity used to show \(\|C_\sigma b(D)\|_{\rm HS}\to0\)
was checked by expanding \(\chi b=b\chi-[b,\chi]\). Its first term
is a Schwartz-small crossing block; its second is a uniformly bounded,
strongly null multiplier times a fixed Hilbert--Schmidt commutator. This
proves Hilbert--Schmidt convergence and is stronger than strong convergence
alone. The crossing scalar tends to zero because its remaining source
block is trace class.

These limits and the local phase concentration prove that the positive
majorant's frequency measure converges to the critical-zero measure.
They imply only an upper bound for the actual projection. The compactness
argument for subsequential limits is sound: all limits are atomic on the
critical ordinates, and their coefficients lie between zero and the
corresponding zero multiplicities.

The cutoff-spectral estimate

\[
\eta_{\sigma,b}([0,1-\delta])
\le\delta^{-1}\|C_\sigma T_\sigma b(D)^*\|_{\rm HS}^2
\longrightarrow0
\]

was checked using the polar decomposition. The square norm on the right
contains the spectral weight \(\lambda(1-\lambda)\), whereas the return
measure contains \(\lambda\); restricting to \(\lambda\le1-\delta\)
gives exactly the displayed factor. The auxiliary identity using
\(b^\sharp(t)=\overline{b(-t)}\) and the multiplier-reflection involution
has the correct order of its factors. There is no control of total mass
near \(\lambda=1\) in this argument.

For fixed \(r<1\), the Abel return trace is bounded by
\(r(1-r)^{-1}\|CTb^*\|_{\rm HS}^2\), so its vanishing and the fixed-r
positive limit follow. The package correctly distinguishes this from
letting \(r\uparrow1\) first. The uniform frequency tails then extend
the compact-frequency statements to compact smooth position sources.

## The rational model and its precise force

For \(v_\epsilon=-B_\epsilon/B_{1/\epsilon}\), the inverse Fourier
kernel, including its negative delta term, agrees with the stated partial
fractions. It gives the diagonal blocks

\[
P\mathcal FP=-q|u_\epsilon\rangle\langle u_\epsilon|,
\qquad
C=q|\xi_{1/\epsilon}\rangle\langle\xi_{1/\epsilon}|,
\quad q=\frac{1-\epsilon^2}{1+\epsilon^2}.
\]

Thus \(L=q^2|u_\epsilon\rangle\langle u_\epsilon|\) has norm strictly
below one. Since an orthogonal projection dominated by a positive
operator of norm less than one must vanish, \(\Pi=0\) is exact.
The return measure has mass
\(q^2\|b(D)u_\epsilon\|^2\) at \(q^2\uparrow1\), and its mass
tends to \(|b(0)|^2\). This directly verifies the proposed failure
mechanism without an asymptotic inverse estimate.

The Abel coefficient \(q^2(1-r)/(1-rq^2)\) and its three regimes are
also correct. The model retains a positive cutoff gap at each parameter
but has no uniform gap. It shows that those structural properties are
insufficient to prove trace survival. It does not show that zeta's
projection vanishes or loses any prescribed amount of mass.

## Arithmetic comparison and final compatibility check

This portion is a self-check. The entire source weight
\(a(z)=\widehat F(z)\overline{\widehat F(\overline z)}\) has Schwarz
reflection symmetry; it need not be even. The contour calculation adds
the two reflected weights before taking the limit. This avoids an
unjustified absolute integral for the imaginary logarithmic derivative.
The clockwise contour sign gives a positive pole correction and negative
zero corrections. On-line zeros receive half residues, and the removable
pole line has correction \(a(0)\). Conjugation of the zero set, followed
by Schwarz reflection of \(a\), justifies the real-part expressions for
complex sources.

The weighted Hadamard estimate controls the absolute phase integral
uniformly in sigma. Its constant term vanishes by critical-line reflection,
not by a zero-location assumption. The exact Cauchy-kernel convolution
bound and the convergent weighted zero count justify both the global bulk
limit and passage through exceptional vertical lines. The good-height
horizontal contour estimate and rapid decay in bounded horizontal strips
justify the residue calculation.

For prepared sources, write \(Q=\Gamma-W_{1/2}\),
\(Z_{\rm crit}=\sum_{\Re\rho=1/2}m_\rho a(\Im\rho)\), and
\(Z_{\rm off}=2\Re\sum_{\Re\rho>1/2}m_\rho
a(\Im\rho+i(\Re\rho-1/2))\). The package gives

\[
Q=Z_{\rm crit}+Z_{\rm off},\qquad
B_\sigma=Z_{\rm crit}-R_\sigma+o(1),\qquad
R_\sigma=\operatorname{Tr}(C_FH_\sigma C_F^*)\ge0.
\]

Consequently

\[
B_\sigma-Q=-Z_{\rm off}-R_\sigma+o(1).
\]

This sign is the final compatibility check. Vanishing return mass alone
would identify the critical-zero measure; it would not remove the off-line
arithmetic term. The remaining direct-limit obligation must retain both
of these quantities. The proven tails and countermodel narrow that
obligation but do not resolve it. The synthesis states this same discrepancy
and correctly presents fixed-Abel limits separately from the exact
projection limit. Its proposed next step must control actual kernel
membership; approximate null vectors alone do not suffice when the
nonzero singular values approach zero.

# Bounded primitive-character fibers for the physical sextic rows

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
This separate same-model review is an internal check, not independent
specialist validation.

## Finding and precise scope

The fiber term in
[SELECTED_INVERSE_DISTRIBUTION_20261008.md](../notes/SELECTED_INVERSE_DISTRIBUTION_20261008.md)
is uniformly bounded by the largest row weight for the stated **actual
sixth-power-free element rows** in one common fixed presentation.

Fix the finite set \(S\), the complete zero-extended finite-order
presentation \(\nu\), and the common orientation \(s_\chi\in\{-1,1\}\).
Let

\[
\psi_u(n)=\nu(n)\chi_n(u)^{s_\chi}
\]

for nonzero element rows \(u\) whose prime-ideal valuations all belong
to \(\{0,1,\ldots,5\}\). Write \(\psi_u^*\) for the inducing
primitive character. Then

\[
\#\{v:\psi_v^*=\psi_u^*,\ v\ {\rm sixth\!-\!power\!-\!free}\}
\le 6^{|S|+1}.
\tag{1}
\]

This is a bound over all such elements, so it also holds after any
physical norm, zero-bin, profile, or selected-weight restriction.
For the source's physical rows satisfying \((u,S)=1\), the sharper
bound is \(6\). No injectivity claim among those six unit choices
is needed.

Consequently, for arbitrary nonnegative selected weights \(w_v\), with
\(W=\sup_v w_v\),

\[
P=\sup_u\sum_{v:\,\vartheta_{u,v}\ {\rm principal}}w_v
\le6^{|S|+1}W,
\tag{2}
\]

and \(P\le6W\) for the coprime physical row set. No conductor power,
height factor, epsilon loss, or new arithmetic moment is needed.

## Source statements checked

The [September 30 source](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf)
has local PDF SHA-256
8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7.
The audit inspected:

- Section 4.1, pp. 10--12: the Eisenstein ring is Euclidean, every ideal
  is principal, there are exactly six units, and good prime residue
  characters have exact order six. The set \(S\) and all fixed
  presentation data are independent of the growing scale.
- Equation (4.8), p. 16: the zero-preserving reciprocity factorization
  for arbitrary element rows. The page was also rendered visually to
  check the formula rather than infer conjugations from PDF text.
- Section 7.1, p. 50: the physical frequency has a unique
  factorization \(H=u a^6\), retaining the unit in \(u\);
  the contributing \(u\)'s are sixth-power-free and coprime to \(S\).
- Section 8.1, p. 56: the presentations \(\nu(n)\chi_n(u)^\varsigma\),
  their primitive inducing characters, the original zero extensions,
  and nontrivial local ramification at each good prime with valuation
  in \(\{1,\ldots,5\}\).

The [amplification manuscript](../../quasi-rh-character-amplification/manuscript.tex),
its arithmetic-setting subsection, uses precisely these common
presentation and physical-row conventions. No deep analytic source
theorem or formal proof was replayed for this finite-fiber deduction.

## Proof

For a row \(u\), use the source's fixed generators at \(S\) and write

\[
u=\epsilon_u u_S u_{\rm good},\qquad
u_S=\prod_{p\in S}\pi_p^{v_p(u)}.
\]

Here \(\epsilon_u\) is one of six units, and \(u_{\rm good}\) is the
unique primary generator of the part of \((u)\) outside \(S\).
For a primary ideal generator \(A\) outside \(S\), source (4.8) is

\[
\chi_A(u)=
\chi_A(\epsilon_u u_S)R(A,u_{\rm good})
\prod_{p\mid u_{\rm good}}\chi_p(A)^{v_p(u)}.
\tag{3}
\]

The first two factors, as functions of \(A\), have conductor supported
on the fixed set \(S\). The factors at good primes retain the zero
extension. When comparing inducing primitive characters, first
restrict to ideals coprime to the original forbidden primes; this
compares their phases without altering the zero-extended kernel.

Suppose \(\psi_u^*=\psi_v^*\). The inducing primitive character of
\(\psi_u\overline{\psi_v}\) is principal. The common fixed phase
\(\nu\overline\nu\) cancels on its units. By (3), at a good prime
\(p\notin S\) the remaining local phase is

\[
\chi_p^{\,s_\chi(v_p(u)-v_p(v))}.
\tag{4}
\]

Every other fixed factor is unramified at \(p\), and factors at other
good primes are likewise unramified there. Hence (4) must be trivial.
Since \(\chi_p\) has **exact order six**, and \(s_\chi=\pm1\),

\[
v_p(u)\equiv v_p(v)\pmod6.
\]

Both valuations lie between zero and five, so they are equal.
This can equally be seen by CRT on primary residue classes: their
congruence at primes above 3 does not restrict the freely varying unit
class at a good \(p\). Thus distinct powers in (4) cannot be hidden
by a fixed-ray phase.

It follows that \((u)\) and \((v)\) have the same part outside \(S\).
There are at most \(6^{|S|}\) remaining valuation choices at \(S\).
For each resulting ideal there are exactly six generators, differing
by the six units, because the ring is a PID. This proves (1).
If both rows are coprime to \(S\), all those remaining valuations
are zero, giving the bound six. The ratio is principal precisely when
the two primitive characters are equal, so summing \(w_v\le W\)
proves (2).

It is important to compare the **characters** in (4), not only their
orders. The separate source statement that valuation \(j\) gives order
\(6/\gcd(6,j)\) would not by itself distinguish \(j=1\) from \(j=5\),
or \(j=2\) from \(j=4\). Multiplicativity and the exact reciprocity
factorization supply the missing exponent-difference argument.

## Masks, trace consequence, and limits

Nothing in the proof replaces a zero-extended product by the constant
one at a canceled ramified prime. The kernel still has the original
mask \(R_{u,v}\). Bounded fibers are a statement about inducing
primitive phases; the elementary kernel bound remains the appropriate
bound on a principal-ratio pair.

For the mixed note's cubic trace, the all-equal-character sector costs
at most \(AP^2\ll_S AW^2\). Exactly two equal characters give two
nonprincipal cross-character kernels and cost at most
\(A^2PN^{-1/4}\ll_S A^2WN^{-1/4}\), with the same allowed
profile/height factors. These are the already certified diagonal and
repeated-sector exponent budgets. The equal-primitive-character fiber
mass is thus no longer a missing input under these actual-row hypotheses.

The hypotheses matter. Without sixth-power-freeness, rows of the form
\(u b^6\) have the same primitive phase for arbitrarily many \(b\),
while their masks may differ. If \(S\) grew with the scale, (1) would
not be a uniform constant. If a row were copied under additional
labels, that label multiplicity would need a separate accounting.
Here the matrix is indexed by actual distinct physical elements in
one fixed presentation, as required by the selected-inverse note.
This proof does not bound the remaining signed cyclic correlation or
prove the proposed mixed moment.

# Adversarial audit of the finite Euler boundary identity

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), in a separate same-model subagent reading. The exact
serving variant and configured reasoning effort are not exposed and are not
inferred. This is an internal mathematical audit, not independent human
specialist refereeing or a priority assessment.

Reviewed: [finite Euler derivation](../notes/FINITE_EULER_BOUNDARY_IDENTITY_20261003.md),
the [continuation assignment](../notes/FINITE_EULER_WEIL_COMPARISON_CONTINUATION_20261003.md),
the manuscript's bounded-transport and boundary-resolvent proofs, and the
[canonical comparison audit](../../../susy-positivity/investigations/wilson-loewner/arithmetic-storage/notes/SONIN_CANONICAL_COMPARISON_AUDIT_20260929.md).
The present audit independently re-derived the operator algebra and the
fixed-place scaling obstruction. No numerical test is used as proof.

## Verdict and scope

The finite-product boundary identity passes this audit for every **fixed
finite** prime set \(S\), every \(\sigma>0\), and every
\(F\in C_c^\infty(\mathbb R;\mathbb C)\). This includes the critical
exponent \(\sigma=1/2\), without a hypothesis about zeta zeros. The inverse
compressed metric, crossing strip, complex-source class, and signs of the
complete residual are retained correctly.

The expanding prepared-source family rigorously disproves an all-support
strong correction sign for each fixed finite \(S\). It does not disprove a
comparison in which \(S\) grows with the source support and contains every
active prime. No such support-adapted inequality is established by this
note or this audit.

## 1. Transport and the actual projection

The translation convention \(U_af(x)=f(x-a)\) gives multiplier
\(e^{-iat}\). Consequently \(\mathscr D\) has multiplier
\(d(t)=\zeta_S(\sigma+it)^{-1}\), and
\[
\mathscr D\mathcal F_\infty\mathscr D^{-1}
=\mathcal J\bigl(v_\infty d(-t)/d(t)\bigr)(D).
\]
This is precisely the stated finite Euler phase; reversing the quotient
would have been an error. Both \(\mathscr D\) and its inverse are bounded
causal operators because the geometric series is norm summable for finite
\(S\) and \(\sigma>0\).

The two triangular compressions are invertible. The factorization
\(T=\mathscr D_-T_\infty\mathscr D_+^{-1}\) gives
\[
TT^*\ge (\ell/u)^2(1-\|C_\infty\|^2)I_\chi>0.
\]
This proves the needed resolvent bound by transport. The ordinary kernel
projection is both
\(P-T^*(I_\chi-C^2)^{-1}T\) and
\(\mathscr D\Pi_\infty M^{-1}\Pi_\infty\mathscr D^*\).
The metric inverse acts on \(\operatorname{Ran}\Pi_\infty\), with lower
bound \(M\ge\ell^2I\). The proof never treats \(\mathscr D\) as an isometry.

The supplementary compactness argument also has the right orientation:
\(\mathcal F_\infty U_{\log n}=U_{-\log n}\mathcal F_\infty\), giving
the dilation parameter \(\log(d/n)\). Each compressed physical cosine
kernel is smooth on the finite square, and the sum converges in operator
norm. The proof correctly does not infer Hilbert--Schmidt class from
compactness or trace unsmoothed \(C^2\). Compactness is unnecessary for
the later block algebra.

## 2. Smoothing precedes arithmetic subtraction

All derivatives of each fixed finite Euler factor are bounded. The gamma
phase has derivatives of at most polynomial growth. Hence \(qv\) is
Schwartz whenever \(q\) is Schwartz. The identity
\[
q(D)\mathcal Q
=V^*\bigl([P,(qv)(D)]-[P,q(D)]V\bigr),\qquad
\mathcal Q=V^*PV-P,
\]
puts \(q(D)\mathcal Q\) in trace class by the Schwartz Hankel lemma.
Moving a multiplier across \(P\) or \(\chi\) adds a trace-class
commutator, so source-smoothed versions of all four extended blocks of
\(\mathcal Q\) are trace class.

In particular the positive sandwiches of \(L\) and \(C^2\) exist before
the arithmetic formula is evaluated. The operator inequalities
\(0\le\Pi\le L\) and \(0\le H=L-\Pi\le L\) then give finite projection
and return traces. This is a genuine operator proof of finiteness, not a
definition by subtracting the desired arithmetic quantity.

The diagonal value of the frequency kernel is \(-\phi'(t)\). Compact
smooth frequency cutoffs give the diagonal trace integral, and Schwartz
approximation passes in trace norm through the displayed commutator
formula. Splitting \(\mathcal Q\) into two separately traced projections
would be invalid; the derivation does not do so.

## 3. Complex sources and boundary cyclicity

Real conjugation fixes \(\Pi\) and sends \(D\) to \(-D\), so the positive
frequency measure of \(\Pi\) is even. The phase derivative is even too.
Thus replacing \(|\widehat F(t)|^2\) by
\(a_e(t)=(|\widehat F(t)|^2+|\widehat F(-t)|^2)/2\) preserves the
correction. This operation averages the correlation multiplier; it does
not project \(F\) onto an additive parity sector. In physical variables
\(\check a_e=\Re\kappa_F\). Arbitrary complex sources and both parity
sectors remain covered, with mixed-source identities obtainable by
polarization.

The short resolvent formula passes the following potentially delicate
checks:

1. \(U=T^*s^{-1}\), \(s=(I_\chi-C^2)^{1/2}\), is an isometry onto
   \((P-\Pi)\mathcal H\), and \(H=UC^2U^*\).
2. The Sonin space reduces \(\mathcal F\), since \(\mathcal F\) is an
   involution and maps every vector of its kernel-cutoff space back into
   that space. Also \(\mathcal Q\Pi=-\Pi\). Their orthogonal complement
   \(\mathcal M\) therefore reduces both selfadjoint operators.
3. Compression of \(a_e(D)\) commutes with \(\mathcal F|_{\mathcal M}\)
   because \(a_e(D)\) commutes with \(\mathcal F\) and \(\mathcal M\)
   reduces \(\mathcal F\). No invariance of \(\mathcal M\) under
   \(a_e(D)\) is needed.
4. Its off-diagonal block is \(A_{+-}=s^{-1}TX\in\mathfrak S_1\).
   Compression of \(a_e(D)\mathcal Q\) then proves separately that
   \(A_{++}C^2,A_{--}C^2\in\mathfrak S_1\).
5. The positive return trace is \(\operatorname{Tr}(CA_{++}C)\).
   Its identification with \(\operatorname{Tr}(A_{++}C^2)\) is justified
   by the stated spectral cutoffs, or by the bounded-product trace
   theorem when both products are trace class. This step does not require
   an eigenbasis or summability of the spectrum of \(C\).
6. Multiplying
   \(sA_{--}-A_{++}s=CA_{+-}+A_{+-}C\) by \(C^2s^{-1}\) produces only
   trace-class products times bounded factors. Legitimate cyclicity gives
   the difference of the two diagonal traces. Adding the crossing traces
   and using \(C^2+s^2=I\) gives
   \(2\Re\operatorname{Tr}(Cs^{-2}TX)\), with the stated plus sign.

The crossing kernel vanishes outside
\(-L_0<y<0<x<L_0\), \(x-y<L_0\). There is no replacement by two
individually infinite half-line traces. The return-series error exponent
also checks: the omitted factor's product with its adjoint is
\(C^{4N+6}s^{-2}\), giving
\(2c^{2N+3}(1-c^2)^{-1/2}\|X\|_1\).

## 4. Prime bulk and residual signs

The differentiated Euler series has minus sign and both exponentials:
\[
\phi'(t)=\gamma_\infty(t)
-\sum_{p\in S,m\ge1}(\log p)p^{-m\sigma}
\bigl(e^{itm\log p}+e^{-itm\log p}\bigr).
\]
Integration against \(a(t)dt/(2\pi)\), using
\(\check a=\kappa_F\), gives exactly \(\Gamma-W_{S,\sigma}\). There is
no missing factor of two, shift reversal, or pole term.

For prepared sources and \(S\supseteq S_{L_0}\), all active primes and
all their active powers are included. Smooth compact support makes the
correlation zero at a support endpoint. Thus the prime sum is complete
and \(Q=B_S-K_S\). Preparation affects the pole term of the arithmetic
target; it was not needed for the operator identity.

The reconciliation with the canonical audit has the right signs:
\[
K_S=E_\infty+\Delta_S+W_S,\qquad
\mathcal R_{S,L_0}=-E_\infty-\Delta_S-W
=-K_S-(W-W_S).
\]
Before complete prime capture, dropping \(W-W_S\) would change the
target. After capture, an inactive added place changes \(B_S\) and
\(K_S\) equally, while the complete residual changes by the negative
trace increment. This is consistency with the previously audited scalar
comparison, not a new positivity mechanism.

## 5. Fixed-place obstruction and its limits

For \(h_R=R^{-1/2}\eta(\cdot/R)\) and
\(F_R=(-\partial_x^2+1/4)h_R\), the stated Fourier rescaling is exact.
Schwartz decay dominates the gamma multiplier, and the prime-power
coefficients are summable for fixed finite \(S\) and \(\sigma>0\).
Therefore
\[
\Gamma[F_R]-W_{S,\sigma}[F_R]
\longrightarrow\frac{\|\eta\|_2^2}{16}
\left(\gamma_\infty(0)
-2\sum_{p\in S}\frac{\log p}{p^\sigma-1}\right)<0.
\]
The coefficient \(1/16\), the exact value of \(\gamma_\infty(0)\),
and the direction of the resulting lower bound on \(K\) all check.
Indeed the result also says \(K_{S,\sigma}[F_R]>B_{S,\sigma}[F_R]\)
for every sufficiently large \(R\), so even a weak all-support
comparison with the *fixed partial* arithmetic bulk would fail.

Every source in this family is exactly pole neutral. The construction
can even start from a nonzero \(\eta\) of zero integral, so adding zero
mean would not repair the fixed-place all-support claim. This does not
conflict with a restricted-support theorem.

The logical boundary matters: the set of primes needed to capture the
source changes with \(R\). The fixed-set dominated-convergence proof
does not control that changing set. It cannot be used to infer the sign
of the complete Weil form or to refute a support-adapted comparison.

## 6. Audit of the proposed mean-functional domination

The identity exposes a signed mixed trace. Neither positivity of
\(C^2\), positivity of the source multiplier, nor bounded invertibility
of transport signs that trace. Generic place monotonicity is already
obstructed by the earlier finite-dimensional examples.

The empty-place calibration also needs its exact source conditions:
the manuscript records a bound
\(K_\infty[F]\le c|\widehat F(0)|^2\) for the stated short support and
pole-neutrality assumptions. The conclusion \(K_\infty\le0\) additionally
requires zero mean. Preparation alone does not impose zero mean. The
older manuscript review's broader informal description must not replace
the corrected statement.

Section 7 now proposes the specific rank-one bound
\[
K_{S_{L_0},1/2}[\mathcal A h]
\le\frac{c_{L_0}}{16}\left|\int h\right|^2,
\qquad \mathcal A=-\partial_x^2+1/4,
\quad h\in C_c^\infty((-L_0/2,L_0/2);\mathbb C),
\]
for a finite constant \(c_{L_0}\) at every \(L_0>0\). The factor
\(1/16\) is correct because \(\widehat{\mathcal A h}(0)=\tfrac14\int h\).
The displayed prepared multiplier in (21) also has the correct factor
\((t^2+1/4)^2\). The statement is an additional form estimate, with the
finite Euler correction defined independently by its boundary trace.
It is not a consequence of the identity, and no bounded prepared operator
on ordinary \(L^2\) has been silently assumed.

The criterion implication is legitimate. With
\(g_0(u)=u^{-1/2}F(\log u)\), its Mellin transform is
\(\widetilde g_0(s)=\widehat F(i(s-1/2))\). Thus pole neutrality and
zero mean impose precisely the fixed Mellin zeros \(\{0,1,1/2\}\).
The preparation theorem covers every such source, and integrating
\(\mathcal A h=F\) shows that zero mean of \(F\) is equivalent to
zero mean of \(h\). Proposition C.1 permits a fixed finite set of
prescribed zeros disjoint from the nontrivial zeta zeros and containing
\(0,1\). The additional point \(1/2\) qualifies: the alternating series
is positive there and its factor \(1-2^{1-s}\) is negative, so
\(\zeta(1/2)\ne0\). These hypotheses were checked directly in the
[2021 author version, Appendix C](https://alainconnes.org/wp-content/uploads/Selecta.pdf).

Consequently, if (21) held for every support size, then the identity would
give \(Q\ge B\ge0\) on the mean-zero pole-neutral class; the stated
criterion would then imply RH. This is a conditional implication using
the criterion, not a direct proof that \(Q\ge B\) on nonzero-mean
sources. The final derivation expressly preserves that distinction.
Its extension to full pole-neutral positivity is a consequence of the
conditional RH conclusion. Merely fixing one support would be insufficient.

There is a further obligation in proving this rank-one bound: negativity
on the mean-zero subspace alone does not automatically produce a finite
constant \(c_{L_0}\). Mixed terms with a complementary mean direction
need quantitative control. For example, if a mean-zero vector \(z\) is
null for the correction form, domination forces its polarized correction
\(K(z,w)=0\) for every \(w\); otherwise varying \(w+tz\) leaves the
right side fixed and makes the left side arbitrarily large. Near-null
directions require the corresponding bound. Counting at most one positive
direction is therefore not a complete proof of (21).

The first gate \(L_0=1\), \(S_{L_0}=\{2\}\), is correctly specified.
Only the first power of 2 is arithmetically active for these sources, but
all powers in the Euler factor and transport inverse must still be
retained. A rigorously positive correction for one mean-zero prepared
source would falsify (21); positive correction for a nonzero-mean source
would not. The first gate must retain both parity sectors, complex
polarization, the actual inverse metric, and any required tail enclosures.
A proof at this gate would remain a local result, while failure would
reject this candidate and not the weaker support-adapted comparison or RH.

The final result report correctly distinguishes reused operator tools,
the finite-product adaptation, the fixed-place counterexample family, and
the unproved rank-one comparison. It does not report the research target
as established or infer any growing-place convergence.

The finite-product identity and fixed-place obstruction are the completed
deliverables. An all-support arithmetic positivity proof remains open.

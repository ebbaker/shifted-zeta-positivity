# Proof audit of reflection and the canonical inverse recursion

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred. Internal
same-model proof audit, not independent specialist or formal validation.

**The inspected reflection and inverse-recursion bookkeeping passes this
scoped audit. No counterexample or missing exponent payment was found in
the steps checked below.** In particular the source preserves the frozen
base, moving zero masks, actual residual-row annulus, source-witness puncture
bounds, two child-normalization copies, and fixed losses across inverse
length one. These findings reduce several concrete local uncertainties in
the consolidated geometry candidate. They do not validate the imported
reflection theorem, large-sieve inputs, complete analytic induction, or
seven-eighths family theorem, and do not promote the conditional candidate
to an established zero-free result.

The audit uses the actual proof in the September 30 source, PDF SHA-256
`8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`,
verified against the local PDF. The source is the
[September 30 manuscript](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf).
The read portions were Sections 4.1–4.3, 5.3–5.5, 14.2–14.4, and
17.1–17.7, particularly the proofs of Lemmas 14.2, 14.3, 17.2, 17.5,
17.1, and 17.6. Source page numbers below are the printed page numbers.
The interpretation of the proposed application is the
[conditional theorem and ledger](../notes/GEOMETRY_CONDITIONAL_THEOREM_AND_DEPENDENCY_LEDGER_20261009.md).

## 1. Reflection keeps one compatible frozen base

The potentially dangerous step is passage from the exact marked reflection
to a hybrid row norm. It would fail for arbitrary coefficients depending
simultaneously on the row and tuple. The proof on pp. 92–100 explicitly
prevents that situation as follows.

Every valuation-one residual row prime has local exponent one. Every active
whole-index mark has exponent zero. Cubic reciprocity makes their mutual
phase have exponent \(1+0+2=3\), hence it is one. A moving exponent-four
base prime would instead leave a nontrivial cubic interaction. The proof
therefore freezes **every nonresidual base prime**, including all exponent-
four primes, before taking the inner residual-row norm. It fixes separate
classes of the residual row product \(R\) and active marked product \(P\)
modulo the full reflection modulus \(M_{\rm ref}^2\). Fixing their product
alone would not give the stated coefficient independence.

The remaining zero-preserving column identities are

\[
\chi_R(nb^3)^3=\chi_R(nb)^3,\qquad
\chi_P(nb^3)^{-2}=\chi_P(n)^{-2}\mathbf1_{(P,b)=1}.
\]

Thus after common smooth separation the tuple coefficient is independent
of \(R,n,b\), and the dual coefficient is independent of \(R,P\).
Frozen-factor collisions give fixed restrictions. Only the two displayed
moving masks \(\mathbf1_{(P,R)=1}\), \(\mathbf1_{(P,b)=1}\) remain
in the hybrid norm. This verifies the local dependence statement actually
needed by Lemma 14.2, conditional on the exact reflection and finite phase
identities used by the source. It does not support extending Lemma 14.3 to
arbitrary moving exponent-four families or arbitrary row-dependent tuple
coefficients.

The actual row annulus is also retained at the right point. Equation (14.15)
keeps the coordinates of the actual residual row, dual factors, and each
active slot in one profile. It places the kernel argument on the actual
support at scale \(Z^{v+3\ell_b+e_\lambda-T_d}\). Lemma 5.3 factors the
small amplitude from that **entire linear row vector**. Only after common
Fourier separation does the proof enlarge the positive row set to a ball.
The kernel is not evaluated on the added rows. Squaring this vector bound
therefore legitimately gives the half-power penalty in (14.14), once.
The same squaring would be invalid for a kernel introduced only after
expanding the energy; the source distinguishes those cases on pp. 35–36
and 119.

The independent coefficient conditions and use of the actual annulus are
therefore explicit proof obligations met by this presentation, rather than
assumptions inferred from pointwise uniform estimates.

## 2. The two hybrid masks are resolved before sieving

I checked the divisor-Cauchy reductions in Lemmas 5.5 and 14.2, rather than
only their final statements. The first moving mask uses
\(\mathbf1_{(P,k)=1}=\sum_{D\mid(P,k)}\mu(D)\), followed by rowwise
Cauchy. In a fixed \(D\)-summand, \(P=DP'\), \(k=Dk'\); the
squarefree restrictions at \(D\) remain fixed. **No** new \((P',k')\)
mask is reinstated. Its cancellation was in the complete Möbius sum.

For the quadratic completed-index reduction, \(b=gt^2\),
\(c=(n,g)\), \(n=cm\), \(g=ch\). The exact quadratic factor is
\(\chi_k(mh)^3\mathbf1_{(k,ct)=1}\), including overlaps with \(t\).
Once \(t\) is fixed its row restriction is fixed; the \(k\)–\(c\)
mask is expanded completely. Its resulting remaining row and column
coefficients satisfy the stated quadratic-sieve hypotheses. The fixed
parts supported on \(S\) are split before sieving the good squarefree
product, while their column zeros are retained.

For the later cubic sieve, the tuple coefficient is fixed for each
\(h,t,D,r\), and grouping \(c'm\) by a squarefree product costs a
divisor factor. The mask at \(ht\) is a restriction on the coefficient
support of that cubic sieve, not its varying row. The dyadic counts and
\(q_D^{-1}\) weight leave one \(B\) factor. The resulting norm exponent,
after its outside normalization, is exactly the unpenalized part of
(14.14); the common small kernel contributes the remaining term.

The prime-by-prime inequality (14.17) also passes an exhaustive local check.
For row valuations zero through twelve, both squarefree \(f\)-choices,
both puncture choices, and every active/inactive or exponent-four assignment,
the local coefficient is bounded by the valuation in
\((q_k^2/q_{k_{\rm pow}})q_fq_{r_\rho}\). Intersections increase that
upper valuation; no coprimality between the row and \(f\) is required.
This is finite verification of the stated valuation rule. The rule itself
has the same direct proof for every higher row valuation, because its
right side is at least that valuation while the local coefficient is at
most two.

The **external quadratic and cubic large-sieve theorems and their precise
arithmetic-family transfer remain upstream inputs**. These calculations
verify their coefficient and mask interfaces as written here; they are not
new proofs of either sieve.

## 3. Canonical children have the required fixed data and strict widths

The most delicate portion is pp. 128–140: moving cube factors become a new
squarefree averaged label, while a different triple becomes a fixed
puncture. The proof retains that distinction.

After the first Poisson transformation it derives
\(b_1b_2=q_0^2J_2^2s\), \(J=sJ_2\), and
\(\xi(n)=\chi_n(J)^4\mathbf1_{(n,\operatorname{rad}q_0)=1}\).
The local parity table was checked on both Cauchy sides. The old averaged
\(f\) disappears only after the first weighted Cauchy inequality and the
fibre bound \(\sum_{f^2E\mid(y)}w(f)\ll Z^{\pi_{\rm old}}\).
Thus the old label is counted once; it is not silently frozen into a new
column coefficient.

After the second transformation, the new row, label, and fixed puncture are

\[
k'=d_kd_2k'',\qquad f'=JCd_2v',\qquad
\rho_\gamma(n)=\rho(n)\mathbf1_{(n,\operatorname{rad}q_0t'r_g)=1},
\quad\gamma=(q_0,t',r_g),\ r_g=g'/d_2.
\]

The common coefficient zeros remain in the outer weight through Cauchy.
They make \(J,C,d_2,v'\) pairwise coprime and squarefree, so \(f'\)
is squarefree. Only after the inequality is taken does the proof discard
other bounded outer weights. The fibre is dominated by
\(D_K(f')C_K(\gamma)\), with the label factor depending on \(f'\)
alone. No count of \(J,C,d_2,v'\) occurs outside the child energy.

The puncture triple set \(\Gamma_\sigma\) is projected from the complete
source reconstruction **before** fixing a current row or label. Each
triple has a source witness, which gives the indispensable bound
\(\log_Zq_{q_0}\le\ell+\eta\). The larger norm balls are used only
for counting distinct triples, not as replacement child domains. This
avoids the invalid inference that every ideal in a containing count ball
has the source puncture bound.

Using \(F=r+3\ell+V\), \(D_c=\ell+A_i+t+g-\theta+V\), the exact
formal identities are

\[
F_c-M_c=F-M+D_c,
\qquad
4F_c-3M_c=4F-3M+2(A_i+t+g-\theta+V)+j.
\]

The actual-to-center errors are explicitly
\(g-\theta\ge-2\eta\), \(j\le2\ell+3\eta\), and
\(Q'\le Q+D_c+4\eta\). After the nonempty-window clipping
\(N_{\rm ch}=\max(0,N_c)\), with
\(0\le\delta_N=N_{\rm ch}-N_c\le6\eta\), and the row enlargement
\(M_{\rm ch}=M_c+\eta\), they give

\[
F_{\rm ch}-M_{\rm ch}-Q'-z_0\ge c_{\rm node}-5\eta,
\qquad
4F_{\rm ch}-3M_{\rm ch}-6z_0\ge c_{\rm node}-7\eta.
\]

The surviving slot cap remains the original nominal \(z_0\), since
survival only selects subcollections. It is not replaced by an actual
product norm. The exact identities also give

\[
M-M_{\rm ch}\ge2(\ell+V)-8\eta\ge2d-8\eta\ge3d/2,
\qquad F_{\rm ch}\le F+11\eta.
\]

Thus the displayed nonterminal step contracts the row width by at least
\(d\) while retaining strict margins. The slightly negative center
\(N_c\) does not create a growing support: nonemptiness gives
\(1\le Z^{\delta_N}\le b\) for one fixed endpoint \(b\), so clipping
changes only a bounded family of annular profiles.

## 4. Principal children, tails, and the energy normalization

The first principal conductor in the canonical transform is one only when
\(n_1=n_2\) and \(b_1b_2\) is a square. Its direct count, including
all labels and both cube factors, gives exponent \(M\) after the original
normalization. The first invariant has \(M<F\), so this fits the target.
The proof does not need to save over the coarse cube-pair count here.

The second principal case has the exact identity

\[
\kappa_i+H_c+s_i+B+t+\ell+R/2=F-B-j.
\]

Its explicit support errors sum to \(26\eta+\tau\), and
\(B,j\ge0\). It is therefore paid within the larger step allowance.
For principal nonzero frequencies added to a formal extension, Lemma 17.5
bounds the entire restoration by its divisor mass using
\(A\sum_{h\ne0}|\widehat\Phi(Aq_h)|\ll1\). Every relevant nonempty
row scale is at least one, so this fits the same principal cost. It is
not an uncounted second row-frequency count.

For nonprincipal children the normalization is especially important:
\(H_{a,\gamma}=Z^{F_{\rm ch}}E_{a,\gamma}\), and the canonical bound is
\(E_{a,\gamma}\ll Z^{F_{\rm ch}+\epsilon}\). Thus the unnormalized
positive child has exponent **twice** \(F_{\rm ch}\). The exact cancellation
identity is

\[
\kappa_i+\lambda_c+C_c+2F_c=F.
\]

Its support losses are
\(9\eta/2+18\eta+11\eta/2+2\delta_N\le40\eta\).
Both clipping copies are required. The two Cauchy inequalities take geometric
means and do not double this total. The normalized discrete measure
\(Z^{-C_c-11\eta/2}\sum_{\gamma\in\Gamma_\sigma}C_K(\gamma)\delta_\gamma\)
has small mass; its genuine distinct-triple count and its normalized mass
occur once each in their respective places.

Both Poisson tails are removed on the genuine raw expression before
noncoprime extension and before taking absolute Fourier integrals. The
outer masks are fixed balls in the derived row, independent of the current
columns. Only their complements are compared to the actual-ratio tail.
Inside each ball the **full smooth kernel** is retained, including pairs
with larger ratio. This keeps sharp selectors outside the common profile.
The first raw-ball error is \(12\eta\); the second uses the same
\(\tau\), cancelling the first \(\tau\) and leaving the stated
\(\eta\) row enlargement. These support-error sums were checked exactly.

The explicit order in (17.66) chooses \(d,D\) first, then
\(\eta,\tau,\pi\), full supports, crude tail exponents, internal tail
orders, Fourier/seminorm orders, and finally the large-\(Z\) threshold.
It gives \(c_h\ge c_*/2\), a negative row cap at depth \(D\), and
\(D(40\eta+\tau+\pi)\le3\epsilon_c/4\). The source treats increasing
external height orders separately. The finite induction bookkeeping therefore
closes at the stated level; its constants may be extremely large.

## 5. Initialization and inverse length one

In the initialization for Lemma 17.1 the overlap \(j=(n,P)\) is fixed
before squaring. Its assigned-prime count is cancelled by \(Z^{-G}\)
in the row-space triangle inequality. With
\(D'=r+z-2G\), \(z_0=z-G\), \(P_1=B-\theta\), the source gives

\[
F^{\rm init}_c-M^{\rm init}_c-(P_1+G)-z_0
 =m-r-2z+2G,
\]
\[
4F^{\rm init}_c-3M^{\rm init}_c-6z_0
 =3m-2r-8z+10G+2P_1,
\qquad
\kappa^{\rm init}_c+P_1+2F^{\rm init}_c=m.
\]

These are coefficientwise exact affine identities. The actual puncture
bound is taken only on the source quotient set and has error \(3\eta\).
Consequently the child margins lose at most
\(9\eta+\tau_{\rm init}\) and
\(22\eta+3\tau_{\rm init}\), respectively; the energy loses at most
\(11\eta+\pi_{\rm init}\). Both principal restoration and raw tails
are stated and paid. The child coefficient remains the canonical
\(\overline\alpha(n)\gamma_2(n)\nu(n)\), with only original product-form
slot subcollections.

For the unmarked sixth-power amplification in Lemma 17.6, identity (17.90)
keeps every zero when \(u\) and the amplifier \(a\) share primes. The
map \((u,a)\mapsto ua^6\) is injective because every valuation of
\((u)\) is between zero and five; reduction modulo six recovers \((u)\)
and division by six recovers \(a\), after which its primary generator
recovers the element unit. No \((u,a)=1\) restriction is needed.

Uniformity near inverse length one follows from fixing the amplification
parameter \(c>0\) for a bounded range \(0\le r\le r_{\max}\).
The auxiliary width has
\(\log_HD\le1/(1+c)\), so the short marked theorem retains a first
margin at least \(c/(1+c)\), independent of how close \(r\) is to one.
The extra long exponent is at most \(5r_{\max}c/6\), absorbed by choosing
\(c\) once from the desired loss. The rowwise scale supremum and parameter
Sobolev argument add logarithmic counts and a fixed polynomial height order,
not a shrinking width decrement. This discharges the local compatibility
concern at \(r=1\), conditional on the established marked theorem and
its uniform seminorm bounds.

## 6. Reproducible checks and unresolved inputs

The new [checker](../numerics/check_reflection_inverse_proof_audit.py) and
[record](../numerics/reflection_inverse_proof_audit_record_20261009.json) report:

- Ten affine identities checked identically by rational coefficient vectors,
  and six exact support-loss ledgers.
- 621 local zero, parity, valuation, priority, and Möbius-mask assertions.
- 2,016 finite-ray phase assertions using the source square-class table.
- 4,677 amplification coefficient, valuation-injectivity, and fixed-width
  assertions, including lengths on both sides of one.
- 24,057 exact terminal-branch inequalities and eight finite-depth loss choices.

The terminal grid checks are finite diagnostics; the general branch
inequalities follow from the displayed proof constraints. The affine
coefficient checks are identities, rather than parameter samples. None of
these finite checks verifies an asymptotic sieve estimate.

The extracted text drops some conjugation bars. Visual inspection of source
pp. 133–134 confirmed in particular
\(\overline{\chi_n(d_2)}=\chi_n(d_2)\chi_n(d_2)^4\) and
\(\chi_a(-1)\overline{G(a)}G(b)R(a,b)=G(ba^{-1})\).
Both are correct; the unbarred text would give false identities. Those
apparent failures are extraction artifacts and are **not** source gaps.

The unresolved dependencies are still substantial:

1. The complete automorphic reflection of Proposition 5.1, including its
   full dual support, cusp coefficient bounds, analytic kernel estimates,
   local conductor orientation, and uniformity in moving frozen primes.
2. The quadratic and cubic large-sieve inputs, with their exact number-field
   family hypotheses, and the upstream arithmetic reciprocity/Gauss identities.
   This audit checks the subsequent masks and coefficient interfaces, not
   independent proofs of all those imported results.
3. Full analytic justification and finite-order uniformity of every transformed
   equality and raw tail throughout the whole induction, beyond the concrete
   common-profile and exponent steps checked here.
4. The initial global family bound and the separate detector, centered fourth
   moment, contour, principal normalizer, and continuation obligations in the
   consolidated ledger.

The conditional candidate \(20999/24000\) survives this audit. The useful
next audit should focus on the imported reflection theorem and the exact
large-sieve arithmetic interfaces, while the fourth-moment audit addresses
its own induction. Replaying these rational identities again or optimizing
the same geometry is a lower priority than resolving those analytic inputs.

# VCD-E23 r1 assessment of the signed quadrature error

16 November 2026, America/New_York. Prepared for Edward Baker with OpenAI
Codex assistance. Explicit assessor dispatch **gpt-6.1-sol / ultra**.
Separate backend model and effort attestation and lead actual settings
are unavailable. This is a separate internal assessment with the proof
workers' dispatch configuration and shared premises. Independent
specialist review remains outstanding. [Shared-premise scope][a05]

**Accepted within the stated scope after two synthesis wording
clarifications.** The 12 direct pins in the [E23 request][h23] and the
18 prerequisite entries across [E21][h21], [E22][h22] and [E24][h24]
matched before reconstruction. The completed E21 dependencies in the
E22 return and E21/E22 dependencies in the E24 return also matched.
The response check below records the only subsequent change in these
inputs. This assessment used analytical reconstruction and source passage
checks. [Result index][results] [Coefficient cluster][cluster] [Avoid index][avoid]

| Result | Disposition |
| --- | --- |
| E21 [Note20 §§1–5][n20] | Accepted. Entire error identity, normalization, moments, endpoint and physical E15 specialization. |
| E22 [Note21 §§1–6][n21] with [completed E21 dependency][r22] | Accepted. Uniform phase bound, real sign, corrected model disk and conditional count. Its return already qualifies the dispatch wording about disk containment. |
| E24 [Note22 §§1–5][n22] with [completed E21/E22 dependencies][r24] | Accepted. Equal known coefficient input, actual fixed-degree local ordering, scoped allowances, directed enclosure and conditional count. |
| B06 [Synthesis23 §§1–5][n23] | Accepted after the §3 and §4 wording response. |
| Canonical contour separation, model count and a source-specific input for those steps | Unresolved. |

## E21. Entire law and normalization

The time-zero source has the manuscript's bound \(C e^{|u|}\rho^2
e^{-\rho}\), \(\rho=\pi e^{4|u|}\). Multiplication by a fixed polynomial
and \(e^{R|u|}\) preserves integrability at every \(R\). The probability
normalization gives \(h_0^*=1,\ h_N^*=\prod_{j=1}^N\beta_j\), and
\(F=2H_0/Z\). Evenness of the measure gives parity of the monic
polynomials and zero Jacobi diagonal. The determinant recurrence
identifies \(P_N\) with the characteristic polynomial of the prefix.
A nonzero eigenvector cannot have zero first entry by the row recurrence
and positive links. Self-adjointness then gives simple nodes and positive
weights summing to one. Alternating signs conjugate \(J_N\) to \(-J_N\)
and preserve \(e_0\), giving a symmetric weighted rule. The first omitted
return walk has length \(2N\) and weight \(\prod_{j=1}^N\beta_j\), which
gives quadrature exactness through \(2N-1\) and its first error derivative.
[Manuscript §2][ms] [E04 §§1, 5][e04]

Write \(d=2N\). For the \(d+1\) simplex coordinates the ordinary integral
of \(\prod s_i^{k_i}\) is \(\prod k_i!/(d+\sum k_i)!\), by integrating
one coordinate and rescaling the others. The density \(d!\) restores
probability. For fixed knots \(t_i\), multinomial expansion gives
\(k!d!c_k(t)/(d+k)!\) for the \(k\)th moment of their convex combination,
where \(c_k(t)\) is the coefficient of \(v^k\) in
\(\prod_i(1-vt_i)^{-1}\). The degree-\(<d\) Hermite interpolant at the
doubled nodes exists by injectivity of the derivative data map, since
its kernel would be divisible by \(P_N^2\). Adding the source point \(u\)
gives a degree-\(\le d\) interpolant, requiring an extra derivative when
\(u\) is a node. Its difference from the first interpolant is \(P_N^2\)
times the leading coefficient. For a monomial \(v^l\) that coefficient
is \([v^{-1}]v^l/\prod_i(v-t_i)\) by division, so it is \(0\) for \(l<d\)
and \(c_{l-d}(t)\) otherwise. The exponential series for each fixed knot
list and its finitely many derivative data then gives the leading
coefficient \((iz)^d/d!\) times the simplex exponential expectation.

Quadrature integrates the first interpolant exactly and agrees with it
on node values. Integrating the interpolant remainder therefore gives
\(F-G_N=L_NE_N\), with \(L_N=(-1)^Nh_N^*z^{2N}/(2N)!\).
The source integral of \(P_N^2\mu\) supplies precisely \(h_N^*\).
The fixed-radius majorant \(e^{R(|U|+\max_j|x_j|)}\) controls the simplex
and tilted source integrals and establishes entire dependence. Grouping
each two node coordinates gives its sum a Jacobian factor equal to that
sum, yielding Dirichlet parameters \((1,2,\ldots,2)\). Reflection of \(U\)
and permutation of the node pairs makes \(X_N\) symmetric. In particular
\(E_N(0)=1\). The classical passage labels check against de Boor §1
(16), §7 (36) and Definition 37, and §9 (52), whose simplex integral is
ordinary volume. The elementary derivation above also handles coincident
knots and complex exponentials directly. No priority claim follows.
[Reference04][ref04] [De Boor][deboor]

For \(S_j=\operatorname{tr}J_N^j\), the even node polynomial series is
\[
 \prod_j(1-x_j v)^{-2}
 =1+S_2v^2+(S_2^2+S_4)v^4/2+O(v^6).
\]
At fixed \(U=u\), multiplication by \((1-uv)^{-1}\) gives the two
coefficient polynomials \(u^2+S_2\) and
\(u^4+u^2S_2+(S_2^2+S_4)/2\). Only these finite polynomials are averaged
over \(u\). With \(M=2N+1\) and \((M)_k=M\cdots(M+k-1)\), the moments are
\[
 \mathbb E X_N^2=\frac{2(m_2+S_2)}{(M)_2},\qquad
 \mathbb E X_N^4=\frac{24m_4+24m_2 S_2+12S_2^2+12S_4}{(M)_4}.
\]
The multiplication vectors \(u p_N\) and \(u^2p_N\) give
\(m_2=\beta_N+\beta_{N+1}\) and
\(m_4=\beta_N\beta_{N-1}+(\beta_N+\beta_{N+1})^2+
\beta_{N+1}\beta_{N+2}\) by their squared norms. At \(N=1\) the lowest
component of the second vector is absent, consistent with \(\beta_0=0\).
There is one zero node, \(G_1=1\) and \(S_0\) has density \(2(1-s)\).
Thus \(X_1=S_0U\) gives moment factors \(1/6,1/15\). Integrating
\(\cos(zu)-1=-(zu)^2\int_0^1(1-s)\cos(zsu)\,ds\) checks the error sign
and prefactor \(-\beta_1 z^2/2\). The physical E15 comparison uses
\(k_N(0)=1\) and \(\ell=0\). Its signed convolution has the same entire
left side and its first omitted term agrees at \(q=0\). The law covers
this physical specialization of the E15 identity. [E15 §§3–4, 6][e15]

## E22. Quantitative phase and consumers

With \(q=2N\), factoring the simplex law by \(S_0=s\) gives
\(q(1-s)^{q-1}ds\), since the residual simplex has \(q-1\) independent
coordinates. Its rescaling is independent of \(S_0\), and \(U\) is
independent of both. Thus \(X_N=S_0U+(1-S_0)V_N\).
The mixed beta moment is \(a!(q)_b/(M)_{a+b}\).
The \(\mathrm{Dirichlet}(2,\ldots,2)\) node averaging moments give
\(\mathbb E V_N^k/k!=A_k/(q)_k\) for the coefficients of
\(\prod_j(1-x_jv)^{-2}\). This reproduces the second and fourth
moments, including \(6\cdot2m_2\cdot2S_2/(M)_4\) at mixed fourth order.

Pairing the bounded nodes gives factors \((1-x^2v^2)^{-2}\).
All even coefficients are nonnegative and odd coefficients vanish.
Replacing \((q)_k\) by \(q^k\) thus gives the node exponential bound
for \(|t|L/q<1\), \(L\ge\max_j|x_j|\):
\[
 \mathbb E e^{tV_N}\le
 \prod_j(1-tx_j/q)^{-2}
 \le \exp\!\left(\frac{t^2 S_2}{q^2(1-t^2L^2/q^2)}\right).
\]
The second inequality sums \(-2\log(1-t^2x^2/q^2)\) over positive
nodes, using \(-\log(1-v)\le v/(1-v)\). For \(U\), evenness and E01
give \(\mathbb E e^{4U}=\mathbb E\cosh(4U)\le2N+12\).
Indeed E01 integrates \((uP_N^2e^{-V})'\) to get
\(\mathbb E_{\nu_N} uV'=2N+1\), uses \(uV'\ge\cosh(4u)-11\), and
applies Jensen in \(u^2\) for the adjacent envelope. Jensen in the
power \(t/4\) gives the source exponential allowance for \(0\le t\le4\).
Convexity gives \(e^{tX_N}\le S_0e^{tU}+(1-S_0)e^{tV_N}\). This treats
\(U\) directly through its exponential moment. [E01 §§1–3][e01]

The row sums and trace give
\(\bar L_N=\operatorname{arcosh}(2N+8)/2\),
\(\bar S_{2,N}=2(N-1)B_{N-2}\) for \(N\ge2\), and
\(S_4\le\bar L_N^2\bar S_{2,N}\). Since
\(1+2N^2+2N^4/3-(2N+8)=2N(N-1)-7+2N^4/3>0\) for \(N\ge2\),
\(\cosh(2N)>2N+8\), so \(\bar L_N<N\). Both barred quantities are
zero at \(N=1\). With \(t=2Y\), the split pays
\[
 \mathcal A_N(Y)=\frac{(2N+12)^{Y/2}}{M}
  +\frac{2N}{M}\exp\!\left(
   \frac{Y^2\bar S_{2,N}}{N^2(1-Y^2\bar L_N^2/N^2)}\right).
\]
At \(N=1\) this is \(14^{Y/2}/3+2/3\). Monotonicity of \(B_j\) and
the adjacent bound give \(m_2\le B_N,\ m_4\le3B_{N+1}^2\).
The moment upper bounds are therefore
\[
 \mathcal V_N=\frac{2(B_N+\bar S_{2,N})}{(M)_2},\qquad
 \mathcal Q_N=\frac{72B_{N+1}^2+24B_N\bar S_{2,N}
             +12\bar S_{2,N}^2+12\bar L_N^2\bar S_{2,N}}{(M)_4}.
\]
In degree one these reduce to \(B_1/6,\ B_2^2/5\).

The centered exponential Taylor remainder is bounded by
\(|z|^2X_N^2 e^{Y|X_N|}/2\). Symmetry gives
\(\mathbb E e^{2Y|X_N|}\le2\mathcal A_N(Y)\), so Cauchy–Schwarz
yields \(\epsilon_N=|z|^2\sqrt{2\mathcal A_N(Y)\mathcal Q_N}/2\).
Uniformly for \(0\le Y\le1\), the source part of \(\mathcal A_N\)
is \(O(N^{-1/2})\) and the node exponent is
\(O(\log^2(N+1)/N)\). Thus \(\mathcal A_N\to1\) uniformly,
\(\mathcal Q_N=O(\log^4(N+1)/N^2)\) and
\(\epsilon_N=O(|z|^2\log^2(N+1)/N)\) throughout the strip, with no
restriction on \(\Re z\) in the inequality. It gives uniform
convergence to one on the growing strip-disk windows with
\(r_N\log(N+1)/\sqrt N\to0\).

On the real axis, \(1-x^2\sigma_N^2/2\le E_N(x)\le1\). The degree-only
radius \(\sqrt{2/\mathcal V_N}\) and the exact radius
\(\sqrt{2/\sigma_N^2}\) give the stated strict error signs away from
zero. Even and odd neighbors bracket \(F\) on their common range.
For \(C_N=G_N+L_N\), the bound \(|F-C_N|\le|L_N|\epsilon_N\) gives
pointwise exclusion and Rouché on a positively oriented piecewise
smooth simple contour under the stated strict boundary inequality.
Both functions are entire and the count includes multiplicity.
The extra monomial vanishes locally uniformly as \(N\to\infty\):
on \(|z|\le R\) its upper bound is \((B_{N-1}R^2/N)^N\) by
\((2N)!\ge N^N\), so \(C_N\) shares the local uniform limit of \(G_N\).
The loose bare disk of radius \(|L_N|(1+\epsilon_N)\) contains the
shifted disk by center separation \(|L_N|\). The independent
complex bare payment uses \(|E_N(z)|\le\mathbb E e^{-\Im(z)X_N}
\le\mathcal A_N(Y/2)\) by symmetry and monotonicity of the allowance.
On the real axis
\(|E_N|\le1\) independently. The resulting bare disk has radius
\(|L_N|\) and at \(0<\epsilon_N<1,\ x\ne0\) the two disks are
nonnested, since the distance of their centers equals the bare
radius. The [return][r22] already corrects how to read the request
about containment. [Reference02][ref02] [Topping §§9.8–9.9][topping]

## E24. Coefficient cost, directed uncertainty and contour homotopy

The first derivative of either model germ that can depend on
\(\beta_j\) has order \(2j\). At that order the first walk to site \(j\)
and back contributes \((-1)^j\prod_{i=1}^j\beta_i\). All other walks
use the preceding links. Thus \(G_{N+1}\) and \(C_N\) both specify and
use the first \(N\) links, with \(C_N\)'s final coefficient supplied
by \(L_N\). The physical next error obeys
\[
 \frac{|F-G_{N+1}|}{|L_N|}
 \le\frac{(B_N-\beta_N)|z|^2}{(2N+1)(2N+2)}
          (1+\epsilon_{N+1})
\]
at \(z\ne0\) by telescoping the omitted-walk factors and applying the
adjacent envelope. Replacing \(B_N-\beta_N\) by \(B_N\) gives the
degree-only order \(|z|^2\log^2(N+1)/N^2\) if both phase budgets
stay bounded, for example \(|z|\le c\sqrt N/\log(N+1)\) in the strip.
This is an allowance, with no lower estimate asserted for the true
next-head error. The explicit shifted-model allowance
\(\epsilon_N\) has order \(|z|^2\log^2(N+1)/N\) there. The lower
order bound for this particular allowance follows from
\(12\bar S_{2,N}^2/(M)_4\) in \(\mathcal Q_N\),
\(B_{N-2}\asymp\log^2(N+1)\), and \(\mathcal A_N\ge1\).

Evenness gives \(E_N-1=-\sigma_N^2z^2/2+O(z^4)\).
Dividing by \(L_{N+1}/L_N=-\beta_{N+1}z^2/[(2N+1)(2N+2)]\) and
using \(E_{N+1}(0)=1\) produces the actual fixed-\(N\) error ratio
limit \((\beta_N+\beta_{N+1}+S_2)/\beta_{N+1}>1\).
Both errors have order \(2N+2\). After removing that power the
denominator is nonzero at zero. The strict actual modulus ordering
holds on a punctured disk for each fixed \(N\), with no all-strip
ordering. The \(N=1\) limit is \(1+\beta_1/\beta_2\).

For the head through \(\beta_{N-1}\), write
\(d_N=(-1)^Nz^{2N}\), \(w=G_N/d_N\) at \(z\ne0\), and
\[
 0<\alpha_N=\frac{\prod_{j=1}^N\beta_j}{(2N)!}
 \le A=\frac{\prod_{j=1}^{N-1}\beta_j}{(2N)!}
        (B_{N-1}-\beta_{N-1}).
\]
The endpoint \(A=B_0/2\) at \(N=1\) uses the empty product. The
normalized actual error is in \(U^+=\bigcup_{0<a\le A}D(a,a\epsilon_N)\).
Adding \(a=0\) gives \(U=\operatorname{conv}(\{0\}\cup
D(A,A\epsilon_N))\), a compact set, by scaling and disk convexity.
The capsule of radius \(A\epsilon_N\) along \([0,A]\) contains it.
The exact closed-set membership criterion for \(v=-w\) is the minimum
over \(0\le a\le A\) of
\(|v|^2-2a\Re v+(1-\epsilon_N^2)a^2\) being nonpositive.
For \(\epsilon_N<1\), clamp the vertex \(\Re v/(1-\epsilon_N^2)\).
For \(\epsilon_N=1\) the quadratic is affine and for \(\epsilon_N>1\)
it is concave, so both cases allow an endpoint minimizer. In these
latter cases \(D(A,A\epsilon_N)\) already contains zero and equals \(U\).

If \(\epsilon_N<1\), every positive-amplitude disk lies in the
strict right half-plane. The distance from \(a>0\) to the ray through
a disk point with argument \(\theta\) is \(a|\sin\theta|\), so
\(|\theta|\le\arcsin\epsilon_N\). Tangency gives this angle and
\(A(1+\epsilon_N)\) is the maximal radius in the abstract enclosure.
Thus \(\Re w\ge0\) suffices to exclude actual cancellation since
\(\alpha_N>0\). This test works at \(w=0\) and needs no amplitude
upper bound. At zero in the \(z\)-plane, \(F(0)=G_N(0)=1\) applies
directly. Knowing the amplitude substitutes \(D(\alpha_N,
\alpha_N\epsilon_N)\) and gives the strict test
\(|C_N|>|L_N|\epsilon_N\), at the cost of the next link.

The straight homotopy \(H_t=G_N+t(F-G_N)\) has normalized error
\(t\alpha_NE_N\) in the closed set \(U\), which must include the
initial amplitude zero. Strict separation of \(-w\) from \(U\)
at each nonzero boundary point makes every \(H_t\) there nonzero.
If the contour passes through \(z=0\), every \(H_t(0)=1\). By
continuity and compactness the modulus has positive minimum on the
full boundary times \(0\le t\le1\). The integral of \(H_t'/H_t\)
is continuous in \(t\), and its \(1/(2\pi i)\) multiple is the integer
zero count by the argument principle. This transfers the count from
\(G_N\) to \(F\). At a boundary point with \(G_N=0\),
\(0\in U\) defeats the closed-set test, even when the pointwise
half-plane argument proves \(F\ne0\). The shifted-disk Rouché test
instead compares \(C_N\) with \(F\). [Topping §9.8, Theorem 9.18][topping]

## Synthesis, controls and response check

The choice to use the directed enclosure at the available prefix
and the next physical head when its link is acquired reflects both
the scoped budget comparison and the actual local comparison.
When \(\epsilon_N<1\), \(E_N\) is nonzero, so \(F-G_N\) has no
nonzero zero there. Its zero at the origin has order \(2N\).
These conclusions describe the approximation error. A canonical
contour still needs separation and an evaluated or proved model
count, or an independently paid real-zero count matched to the
transferred total count.

The phase budget is an intermediate estimate, and the contour
conclusion is conditional on verified boundary and count data.
Three- and four-square controls satisfy the exact-law inputs and
the cosh/envelope inputs even at their catalog events. The positive
fixed weights cancel out of their half-line summand scores, and the
factor \(u\) cancels the junction contribution in integration by parts.
The finite-source theorem gives nonreal zeros for the specified
finite square changes, including the known finite weighted-square
sources. The bounded positive finite-prime orbit screen has separate
positive-time events at escaping heights. Its zero statements retain
that scope. In these classes the loss of full canonical reflection
and complete equal square coefficients is outside the phase proof.
The small E10/E12 compact multipliers keep \(uV'\ge\cosh(4u)-11\)
and the requisite tails, so the same integration by parts supplies
the cosh moment as well as the envelope. Their zero locations remain
open. A control with a nonreal zero inside a tested contour refutes
the conjunction of successful separation and zero model count on
that contour. It can still pass local separation elsewhere.
[Classification][a01] [Control-screening rule][a02] [Scope][a07]
[Control catalog][catalog] [E07][e07] [E10][e10] [E12][e12]

The other screens keep their member-specific limits. The Euler
translate with \(c=1/2,p=23,\lambda=0\) fails \(B_0\).
The reflected super-Gaussian fails score confinement because its
\(uV'\) grows polynomially, while its actual degree-wise bounds are
untested. Smooth shape and positive-primitive sources lack the
canonical summand score and face no stronger envelope verdict here.
Atoms lack the positive-density score premise and terminate the
recurrence. The particular three-atom event fails \(B_1\). Compact
triangular extensions lack strictly positive full-line density.
The RH-conditional normalized endpoint control loses ordinary
Dirichlet arithmetic and the canonical score derivation, while its
weaker degree bounds are untested. The changed observation with
fixed amplitude fails the literal Fourier-readout premise. The
positive-measure relaxation supplies no full-line physical source
and Fourier observation. [E01 §5][e01] [Note20 §5][n20]
[Note21 §6][n21] [Note22 §5][n22]

The frozen synthesis was SHA-256
`a1ecc06a7567489652bd0750fa03cdabe35ae4d7c230228bf9e57afb3b677c24`.
The first pass required a wording clarification in §4 to distinguish
the normalized boundary values from the \(z\)-plane contours. It also
flagged §3's ambiguous “smaller paid disk” before its precise
comparison paragraph. The one response check verified synthesis
SHA-256
`8d55a5e7e8312945f789d2de2e4d93e19eaaff299ccd299206e16bf9110f6fd1`.
Reversing only the two prose replacements in memory recovered the
frozen hash. Section 3 now states its disk radius directly. Section 4
specifies separation of \(-G_N/d_N\) from \(\mathcal U_N(z)\) on
stated contours together with a justified model count, or a real
count matching a separately controlled total. The author-help
paragraph asks for a concrete local or inter-degree estimate using
the canonical readout and score or arithmetic. It treats the
needed estimate as open. The assessment edited no proof notes, ran no
numerical campaign and left the physical source and manuscript intact.
[Synthesis23 §§3–5][n23]

[h23]: ../research-progress/handoffs/VCD-E23-r1.md
[h21]: ../research-progress/handoffs/VCD-E21-r1.md
[h22]: ../research-progress/handoffs/VCD-E22-r1.md
[h24]: ../research-progress/handoffs/VCD-E24-r1.md
[r22]: ../research-progress/handoffs/VCD-E22-r1-return.md
[r24]: ../research-progress/handoffs/VCD-E24-r1-return.md
[n20]: ../notes/20_VCD_E21_COMPLETE_ERROR_PROBABILITY_LAW_20261116.md
[n21]: ../notes/21_VCD_E22_QUANTITATIVE_ERROR_PHASE_20261116.md
[n22]: ../notes/22_VCD_E24_DIRECTED_ERROR_AND_PREFIX_COMPARISON_20261116.md
[n23]: ../notes/23_VCD_B06_SIGNED_ERROR_CONSUMER_SYNTHESIS_20261116.md
[ms]: ../manuscript/main.tex
[e01]: ../notes/01_VCD_E01_LOGARITHMIC_ENVELOPE_20261113.md
[e04]: ../notes/04_VCD_E04_TAIL_FOUNDATIONS_20261116.md
[e07]: ../notes/07_VCD_E07_FINITE_CANONICAL_SCORE_CONTROLS_20261116.md
[e10]: ../notes/10_VCD_E10_SMOOTH_NEXT_DEFECT_FREEDOM_20261116.md
[e12]: ../notes/12_VCD_E12_FINITE_MIDPOINT_FREEDOM_20261116.md
[e15]: ../notes/13_VCD_E15_SHARED_MEMORY_EQUIVALENCE_20261116.md
[ref02]: ../references/02_INDUCTION_SOURCE_PASSAGES_20261116.md
[ref04]: ../references/04_QUADRATURE_ERROR_PHASE_PASSAGES_20261116.md
[deboor]: https://pages.cs.wisc.edu/~deboor/sat/papers/2/2.pdf
[topping]: https://warwick.ac.uk/fac/sci/maths/people/staff/peter_topping/teaching/ma3b8_cplxanal_24_07_29.pdf#page=103
[results]: ../../../../result-summaries/README.md
[cluster]: ../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[catalog]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a05]: ../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md

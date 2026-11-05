# MC11-E04 r1 — reconstruction and error accounting

4 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual **gpt-6.1-sol (Codex), effort ultra**, MC11 chat0001, thread 01a1a8e5-1cb3-74b3-80a9-e4b99f6f4fab, turn 01a1a9d5-044d-7ee1-a1e3-7a415581b884.

**All fixed reconstruction checks pass; no correction was required.** This note supports the [E04 assessment][review]. It records the separately written algebra/interval reconstruction and the analytical error payments; it does not acquire another integral or begin B01. [Code][code] · [Exact review record][record] · [B01/model-change handoff][handoff]

## 1. Evidence and limits

All 18 hashes in the [frozen E04 list][versions] match. The existing standard-library E03 verifier reproduced its 121 checks without loading an integrator. The new E04 checker imports no mathematical helpers from E02/E03: it uses sorted variable-label monomials, a first-row cofactor determinant and the integrated product formula below. Its 124 checks reproduce the saved exact E02/E03 intervals, covers, payments, signs and decimal consequences. These two checks share the same acquired balls.

The E04 record is 58,097 bytes, SHA-256 **df13d2d335f6a86697c48a7a418370854fa2ccc6ca937514dcb35d3ab75435e0**. Its code SHA-256 is **dc00248700438b8edcba8cab7faa14980e90f5f980213478a82854ecf943b433**. Recorded exact reconstruction time was 0.059640375 seconds. There were zero new integrand evaluations, zero new moments and zero local corrections.

The coordinator is the same assistant/model that produced E02/E03. One read-only Sol/ultra contributor supplied the single analytical assessment pass. Separate arithmetic code does not remove the shared source, acquisition or LLM premises. This is **same-assistant/same-model internal assessment**, not independent specialist review or formal verification of Arb/FLINT.

## 2. Source and numerical normalization

For \(p_E=e^{u-Ee^{4u}}\), \(X=Ee^{4u}\),
\[
p_E''-p_E=(16X^2-24X)p_E,\qquad
\phi_E=(p_E''-p_E)/8=(2X^2-3X)e^{u-X}.
\]
The source callback therefore uses \((2X^2-3X)e^{z-X}z^{2j}/(2j)!\), with \(E=4\pi\), and **no additional \(1/8\)**. It is entire in \(z\), including for the enclosed real parameter. Its integer powers and nested exponentials introduce no branch. The actual code encloses the parameter and all arithmetic with Arb/Acb.

The saved acquisition has one complete pass at 384 bits, tolerance \(2^{-320}\), five moments \(j=1,\ldots,5\), and the five segments ending at \(0,1/8,1/4,1/2,1,2\). All 25 complex enclosures are finite and contain zero in their imaginary components. Exact interval sums of the serialized real segment balls fit inside their compact-total balls. The 1,991 recorded callback counts reconcile. Every full half-width meets the frozen target. No refinement, precision change or extra source level was used.

This checks the enclosure record and the integration method's application. The acquired integrals themselves remain trusted numerical inputs under the identified python-flint 0.9.0/FLINT 3.6.0 implementation.

## 3. An independent check of the retained source-tail grid

The E03 source exterior, for \(E=4\pi\), \(U=2\), \(X_U=Ee^8\), \(\lambda=4X_U-9\), is bounded by
\[
B_j^{(2)}=\frac{2E^2e^{18-X_U}}{(2j)!}
\sum_{h=0}^{2j}\binom{2j}{h}
\frac{2^{2j-h}h!}{\lambda^{h+1}}.
\]
It follows directly by dropping the source's negative \(-3X\) term, using the exponential tangent after \(u=2+v\), and integrating each polynomial term. The actual exterior is in \([0,B_j^{(2)}]\). Its lower bound is not the positive lower endpoint of the interval that evaluates this upper-bound expression.

The saved expression balls and their upward grid payments reconstruct correctly. In addition, the used payment can be checked without evaluating a tiny exponential:

- \(3<\pi<13/4\) gives \(12<E<13\).
- \(e>2\), from its elementary positive series, gives \(e^8>256\), hence \(X_U>3072\) and \(\lambda>1\).
- \(2E^2e^{18-X_U}<2^9\,2^{-3054}=2^{-3045}\).
- For \(m=2j\le10\), the normalized polynomial sum is
  \[
  \sum_{h=0}^m\frac{2^{m-h}}{(m-h)!\lambda^{h+1}}
  \le(m+1)2^m\le11\,2^{10}<2^{14}.
  \]

Thus
\[
0<R_j\le B_j^{(2)}<2^{-3031}<2^{-384},
\qquad j=1,\ldots,5.
\]
This verifies that E03's retained grid payment \(2^{-384}\) covers the actual source exterior independently of the very small bound-expression readings. The full moment box is compact \([\ell_j,u_j]\) plus \([0,2^{-384}]\), exactly as used.

## 4. Ground exterior and complete higher-energy group

The checker reconstructs the compact ground coefficients from the original six primitive dyadic balls, then retains the ground exterior:
\[
b_j=c_j^*+R_{j-1}-R_j,\qquad
b_j\in[\underline c_j^*-\overline B_j,\,
       \overline c_j^*+\overline B_{j-1}].
\]
The saved ground spatial balls are positive and their upward payments are included. Their boxes agree exactly with E02/E03. All used diagonal indices are at least one, so no endpoint atom enters them.

For the remaining source energies, \(n^2\ge9+7(n-3)\) and the Green tangent bound give, on the full half-line,
\[
0<H_j=\sum_{n\ge3}a_j(\pi n^2)\le
V_j=\frac{e^{-9\pi}}{8(1-e^{-7\pi})(36\pi-1)^{2j-1}}.
\]
The difference of positive primitive moments is bounded above by its preceding primitive moment; source positivity supplies \(H_j>0\). The exponential constants and their rational majorant propagation agree with the frozen E02 record. These constant enclosures are inherited identified numerical inputs; their generating positive-Taylor-sum/geometric-remainder formula is valid on the stated range.

The slope
\[
F(E)=4E-9-\frac{12}{2E-3},\qquad F'(E)>0
\]
gives \(H_j/H_1\le F(9\pi)^{-2j+2}\), and the analogous single-level ratio for \(n\ge3\). The checker rebuilds E02's whole-path gradient boxes and verifies the strictly positive lower normalized response. Thus the entire infinite higher group is covered, with no unrecorded spatial or energy remainder.

## 5. Cofactor reconstruction and exchange mutation

Starting from the actual matrix
\[
M_3=\begin{pmatrix}c_3&c_4&c_5\\c_2&c_3&c_4\\c_1&c_2&c_3\end{pmatrix},
\]
the new code computes each \(2\times2\) signed cofactor. First-row expansion gives
\[
D_3=c_3^3-2c_2c_3c_4+c_1c_4^2+c_2^2c_5-c_1c_3c_5.
\]
Collecting all nine cofactors by their moment index reproduces all five \(G_j\), including the repeated-entry factors. For \(c=b+s h\), direct product integration gives
\[
\int_0^1c_i(s)c_j(s)\,ds
=b_ib_j+\frac{b_ih_j+h_ib_j}{2}+\frac{h_ih_j}{3}.
\]
Substituting this formula into the collected gradients independently reconstructs all five frozen \(K_j\) polynomials, with every mixed term.

The exact response and cubic endpoint polynomials agree:
\[
\sum h_jK_j=D_3(b+h)-D_3(b).
\]
For a genuine determinant exchange-sign mutation, change \(-2c_2c_3c_4\) to \(+2c_2c_3c_4\) on the determinant leg while holding the verified response fixed. The mismatch is
\[
4\big[(b_2+h_2)(b_3+h_3)(b_4+h_4)-b_2b_3b_4\big],
\]
with seven nonzero collected terms. This differs from the earlier \(h_2K_2\) mutation and directly satisfies E04's determinant-exchange check. Changing both legs consistently would merely produce an identity for a different polynomial; that is not this check.

Both contributions still use the same \(K_j\) with \(h=A+H\). The method does not admit \(n=2\) first on a separate path, and does not differentiate normalized wedges.

## 6. Magnitude, pointwise scope and disposition

Exact interval evaluation from the reconstructed polynomials reproduces every saved E03 output, including the two valid net intervals and their intersection. The following reported consequences are accepted:

| Quantity | Accepted conservative bound |
| --- | --- |
| \(L_2\) | \(2.22665020868\times10^{-33}<L_2<2.22665020869\times10^{-33}\) |
| \(L_{\ge3}\) | \(0<L_{\ge3}<5.402\times10^{-40}\) |
| \(\Delta_3\) | \(2.22665020\times10^{-33}<\Delta_3<2.22665075\times10^{-33}\) |
| \(D_3(0)\) | \(1.66142398817\times10^{-28}<D_3(0)<1.66142398818\times10^{-28}\) |
| \(\Delta_3/D_3(0)\) | \(1.34020588635\times10^{-5}<\Delta_3/D_3(0)<1.34020621148\times10^{-5}\) |

The numerical zero lower endpoint for \(L_{\ge3}\) is open by the analytical strict sign, not rounded into a positive numerical floor. Both groups reinforce. The tail-to-net bound \(<2.427\times10^{-7}\) implies \(L_2/\Delta_3>0.9999997573\), or more than 99.99997573 percent.

The first-excited pointwise interval is separately reproduced from whole-path \(G_j\) boxes:
\[
2.2266193\times10^{-33}<\chi_3(4\pi;s)
<2.2266811\times10^{-33},\quad 0\le s\le1.
\]
Combining it with the higher-level slope proof accepts every excited level's positive response over the entire stated path. E02's earlier zero-straddling \(n=2\) interval is also reproduced and retained as an honest limitation of its original inputs; E03 resolves that uncertainty without changing the observable.

The accepted statements are fixed-order comparisons for the canonical source and unnormalized observable. They supply no new positivity range, RH conclusion, neighboring-shift or growing-order estimate. The control-premise and provenance qualifications are recorded claim by claim in the [review][review].

**Next: [B] MC11-B01 — Astra.** Consume this assessed result under the existing at-most-two-route analytical contract; do not acquire more data or begin E05 before B01 defines it.

[review]: ../reviews/02_MC11_E04_R1_THREE_ORBITAL_RETURN_ASSESSMENT_20261104.md
[record]: ../numerics/MC11_E04_R1_ASSESSMENT_REPLAY_20261104.json
[code]: ../numerics/mc11_e04_r1_assessment_replay.py
[versions]: ../research-progress/handoffs/03_MC11_E04_R1_INPUT_VERSIONS_20261104.json
[handoff]: ../research-progress/handoffs/04_MC11_E04_RETURN_AND_B01_MODEL_CONTINUATION_20261104.md

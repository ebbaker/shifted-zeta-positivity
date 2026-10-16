# Certified cutoff-cosine gap and polynomial resolvent

29 September 2026. Prepared for Edward Baker with LLM assistance. Model: GPT-6 (Codex); exact serving variant and configured reasoning effort are not exposed. This is a separate same-model mathematical derivation and computation, not independent human refereeing.

## Concrete result

For the actual operator
\[
(Cv)(x)=2\int_0^1\cos(2\pi xy)v(y)\,dy
\quad\hbox{on }L^2(0,1),\qquad A_0=I-C^2,
\]
the interval certificate establishes
\[
\boxed{A_0\ge\gamma I,\quad\gamma=57/10^6,\qquad
\|A_0^{-1}\|\le10^6/57<17544.}
\]

It also constructs an exact finite-rank polynomial correction to the identity, denoted `R_32`, such that
\[
\|A_0^{-1}-R_{32}\|<9.2\,10^{-32},\qquad
\|CA_0^{-1}-C_{32}R_{32}\|_1<2.7\,10^{-31}.
\]
Here `C_32` is an explicitly defined polynomial-kernel approximation, not a sampled or fitted projection. The stated bounds include the full infinite-dimensional complement.

The reproducible artifacts are [prolate_certificate.py](../numerics/prolate_certificate.py) and the [rank-32 record](../numerics/records/prolate_certificate_rank32.json). A separate 192-bit replay passed the same caps; rank24 is an optional reproducible comparison. Every inequality is decided by an outward Arb ball comparison. No sampled eigenvalue certifies the gap. The [main enclosure note](SONIN_ACTUAL_PROJECTION_ENCLOSURES_20260929.md) applies this certificate to actual Sonin trial vectors.

## 1. Exact finite-rank representation

Truncate the cosine Taylor series after terms `j=0,…,N−1`:
\[
C_N(x,y)=\sum_{j=0}^{N-1}a_jx^{2j}y^{2j},\qquad
a_j=\frac{2(-1)^j(2\pi)^{2j}}{(2j)!}.
\]
Its range is contained in the `N`-dimensional space of even polynomials of degree at most `2N−2`. An orthonormal basis on **`(0,1)`** is
\[
e_k(x)=\sqrt{4k+1}\,P_{2k}(x),\quad 0\le k<N.
\]
These are ordinary even Legendre polynomials, not shifted Legendre polynomials. Evenness converts their usual orthogonality on `(-1,1)` into this half-axis normalization.

Writing `E_N` for the corresponding isometry from `C^N` into `L²(0,1)`, one has `C_N=E_N M_N E_N*`, where
\[
(M_N)_{k\ell}=\sum_{j\ge\max(k,\ell)}^{N-1}
a_j b_{kj}b_{\ell j},\qquad
b_{kj}=\sqrt{4k+1}\,\frac{(2j)!2^{2k}(j+k)!}
{(j-k)!(2j+2k+1)!}.
\]
The factorial ratio is exactly `∫_0^1 P_{2k}(x)x^{2j}dx`; it is zero for `k>j`. All factorial/rational arithmetic is exact, and Arb encloses only `π`, square roots, and subsequent arithmetic. Symmetric entries are constructed from the same ball.

The code also checks the independent kernel identities
\[
\operatorname{tr}M_N=\sum_j\frac{a_j}{4j+1},\qquad
\operatorname{tr}(M_N^2)=\sum_{j,k}\frac{a_ja_k}{(2j+2k+1)^2},
\]
against the basis representation. These checks guard its normalization and moment conversion.

## 2. Infinite Taylor tail and certified gap

The rank-one term `a_j x^{2j}y^{2j}` has trace norm `|a_j|/(4j+1)`. Set
\[
q_N=\frac{(2\pi)^2}{(2N+1)(2N+2)},\qquad
\varepsilon_N=\frac{2(2\pi)^{2N}}
{(2N)!(4N+1)(1-q_N)}.
\]
For `N≥4`, `q_N<1` is verified, and the ratio of successive nuclear norms in the tail is at most `q_N`. Hence
\[
\|C-C_N\|\le\|C-C_N\|_1\le\varepsilon_N.
\]
The actual `C` is a compression of the unitary cosine transform, so `||C||≤1` without a numerical assumption. Thus
\[
\|C^2-C_N^2\|\le\delta_N:=\varepsilon_N(2+\varepsilon_N).
\]

The code proves strict positive definiteness of
\[
(1-\gamma-\delta_N)I_N-M_N^2
\]
by interval LDL elimination, with every pivot strictly positive. It also checks `γ+δ_N<1` for the orthogonal complement, where `I−C_N²` is exactly the identity. Perturbation by the full `C²−C_N²` therefore proves `I−C²≥γI` on all of `L²(0,1)`.

At `N=32`, the outward scalar bounds include
\[
\varepsilon_{32}<1.5\,10^{-40},\qquad
\delta_{32}<2.990\,10^{-40}.
\]
The second displayed rounded cap is a readable rounding of the stored ball; the certificate's explicitly checked rational caps are listed in the record.

## 3. A posteriori polynomial inverse approximation

Let `A_N=I_N−M_N²`. Arb encloses `A_N^{-1}`. Symmetrizing the enclosure and taking its dyadic midpoint gives an **exact self-adjoint dyadic matrix** `R_N^{mat}`. Define
\[
\mathscr R_N=I+E_N(R_N^{\rm mat}-I_N)E_N^*.
\]
This is identity plus a finite-rank polynomial-kernel operator. There is no suggestion that the identity itself is an integral operator with a polynomial kernel.

The computed residual matrix is `I_N−A_N R_N^{mat}`. Its Frobenius norm encloses the finite-block operator residual. With
\[
s_N=\|I_N-A_NR_N^{\rm mat}\|_F,\qquad
r_N=\max(1,\|R_N^{\rm mat}\|_F),
\]
the full-space residual satisfies
\[
\|I-A_0\mathscr R_N\|\le\rho_N:=s_N+\delta_Nr_N.
\]
Since the independently certified inverse norm is at most `γ^{-1}`,
\[
\|A_0^{-1}-\mathscr R_N\|\le\rho_N/\gamma.
\]
The code checks `r_N>1` in the present parameter regime and checks `ρ_N<1`; the inverse error bound uses the gap, not a floating-point inverse condition estimate. The matrix is defined exactly by its dyadic coefficients; their reproducibility digest is recorded.

At rank 32 and 256 bits:

| Quantity | Certified upper-bound scale |
|---|---:|
| finite inverse residual `s_N` | `2.617e−70` |
| polynomial resolvent norm `r_N` | `17468.291` |
| full inverse residual `ρ_N` | `5.222e−36` |
| inverse approximation error | `<9.2e−32` |

The 192-bit replay gives the same exact gap and the same checked simple caps. Its larger finite arithmetic residual, about `4.91e−51`, remains negligible relative to the analytic tail contribution. Rank 24 separately gives an inverse error below `2.126e−16`; the rank increase is justified by the subsequent error-kernel calculation.

## 4. Direct application to the archimedean error kernel

For `ρ≥1`, let
\[
B_\rho=\chi\vartheta(\rho^{-1})R\mathcal F_\infty\chi,
\qquad
B_\rho(x,y)=2\sqrt\rho\,\mathbf1_{x\ge1/\rho}
\cos(2\pi\rho xy).
\]
Every factor is a contraction or unitary, so `||B_ρ||≤1`. The audited spectral formula for the prolate error is equivalently
\[
\epsilon(\rho)=\operatorname{Tr}(CA_0^{-1}B_\rho).
\]
Indeed its diagonal expansion in the `C` eigenbasis has coefficient `λ_n/(1−λ_n²)` times `⟨ξ_n,ϑ(ρ^{-1})R F ξ_n⟩`, exactly matching the earlier normalized-`ζ_n` expression.

The column decomposition `M_N=Σ_j(M_N e_j)e_j*` supplies the trace-norm bound
\[
\|C\|_1\le\sum_{j=0}^{N-1}\|M_N e_j\|_2+\varepsilon_N=:c_{1,N}<2.858
\]
at rank 32. It is sharper here than `√N||M_N||_F` and needs no spectral decomposition. It gives
\[
\|CA_0^{-1}-C_N\mathscr R_N\|_1
\le c_{1,N}\frac{\rho_N}{\gamma}+\varepsilon_Nr_N.
\]
At rank 32 this is strictly below `2.7e−31`, uniformly in `ρ`. Therefore
\[
\boxed{\left|\epsilon(\rho)
-\operatorname{Tr}(C_N\mathscr R_N B_\rho)\right|
<2.7\,10^{-31}\quad(\rho\ge1).}
\]
The remaining trace is a finite sum of explicit polynomial–cosine integrals. It can be enclosed without computing individual prolate eigenvectors. This bound controls the **operator replacement only**; quadrature, variation between parameter nodes, cancellation, and source integration still need their own rigorous controls.

The script's import interface is `record, M_N, R_N_mat = certify(rank=32, precision_bits=256)`. The matrix of the finite smoothed resolvent is `M_N*R_N_mat` in the basis displayed above. Its entries remain Arb enclosures of the defined exact polynomial operator. This is suitable for the root agent's `h_0` calculation.

There is also a simpler upper bound for that scalar which avoids the ill-conditioned error kernel. The cutoff operator satisfies `L_0=Π+Σ_n λ_n²|ζ_n⟩⟨ζ_n|≥Π`. Hence, for a compact smooth source kernel `H`,
\[
\mathcal B_\infty[H]\le\operatorname{Tr}(C_HL_0C_H^*)
=\Gamma[H]+\int\kappa_H(t)\delta(e^{|t|})\,dt.
\]
Cyclicity in the cutoff formula gives
`δ(ρ)=Tr(C χϑ(ρ^{-1})F∞χ)`. The second factor has norm at most one, proving the uniform bound `|δ(ρ)|≤||C||_1<2.858`. Consequently
\[
\boxed{\mathcal B_\infty[H]\le\Gamma[H]+2.858\,\|H\|_1^2.}
\]
The existing smoothed cutoff trace theorem supplies the equality here; only the nuclear estimate is numerical. This one-sided bound requires a separate rigorous upper estimate of `Γ[H]`, but does not require evaluation of `ε` or of prolate eigenvectors.

## Reproduction and scope

Run `python prolate_certificate.py --rank 32 --output prolate_certificate_rank32.json` in an environment with `python-flint==0.9.0`. Tested with Python 3.12.14 and FLINT 3.6.0; the record carries the runtime actually used. No private runtime path is embedded in the script.

All `require` checks remain active under Python optimization. Norm bounds use `abs_upper()` before multiplication; in the installed python-flint version, `x**2` can return `nan` for an Arb interval containing zero, so that interface is not used for norm certification. The LDL code uses ordinary interval multiplication for its squares.

This certificate establishes the resolvent needed by the actual Sonin projection. It does not evaluate a projected seed, certify the Sonin trace, or prove a residual sign. Those are separate obligations, and no unbounded-support claim follows from this finite-cutoff certificate.

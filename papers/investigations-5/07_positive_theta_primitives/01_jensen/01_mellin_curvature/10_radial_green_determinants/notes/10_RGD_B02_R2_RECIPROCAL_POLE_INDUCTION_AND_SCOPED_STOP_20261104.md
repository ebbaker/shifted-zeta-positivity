# RGD-B02 r2: reciprocal-pole induction and its precise stopping point

4 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance; actual **gpt-6-astra / ultra**, chat0004,
thread `01a1a7c1-13a2-7371-8010-b0ace507476e`.
Type **B**, bounded conceptual return under [Packet13][packet13].
Proof-author checks with three read-only same-model contributors;
[Review07][review] records that level. Separate E04 r5 assessment is pending.

## 1. Result, classification and prior-art limit

One comparison has been investigated: exact rectangular duality followed
by isolation of the nearest poles of the **complete** reciprocal source.
It gives a concrete fixed-index order induction, including a deliberately
coarse canonical initialization at k=1, r=1500. It does **not** supply an
all-index induction or new theta positivity coverage.

The mechanism is already described in the 22 July 2026 primary web note
[The first fifteen Xi-coefficient shifts are nonnegative at every Toeplitz rank][kenan].
It reports coverage for k≤15, using the same reciprocal duality, signed
residues, Vandermonde cancellation and matrix perturbation argument.
Its supporting notebook/certificate files were not inspected. Treat that
coverage as reported prior work, and this note as a self-contained method
and scope audit, not a novelty claim. Our k=1 threshold is not an improvement.
The source-access qualifications and other primary sources are recorded
in [References02][refs].

The return consists of:

1. An exact identity valid at every r,k, including all zero negative indices.
2. A positive finite-pole determinant margin and a complete contour residual.
3. A closed scalar budget that contracts when r increases with k fixed.
4. An initialized example using only named published finite-zero data and
   coarse analytical bounds on the complete source; no new numerical run.
5. Exact vanishing of every fixed-N pole reference for r≥N, k>N, and
   failure of the selected growing-k triangle/Harnack budget when k/r
   stays bounded below. These are scoped failures of references/payments.

In the language of [avoid/01][a01], items 1–3 are an identity and a
conditional quantitative estimate; item 4 is an initialization within
known territory; item 5 is a scoped stop. Assuming arbitrarily long
real-simple nearest-zero prefixes would assume RH plus simplicity.
That premise is not a new criterion or an acquired input.
Read the [result index][results], [control screen][controls] and
[avoid index][avoid], especially [scoped exclusions][a07],
[known baselines][a11] and [unchecked imports][a16].

## 2. Exact full-source duality, including the boundary

Keep the normalization of Notes07–09:
\[
 C(z)=\sum_{j\ge0}c_jz^j
 =\int_0^\infty\Phi(u)\cosh(u\sqrt z)\,du
 ={1\over8}\xi\!\left({1+\sqrt z\over2}\right),\qquad C(1)=b={1\over16},
 \quad c_j=0\ (j<0).
 \tag{1}
\]
The square root in this notation gives a single-valued entire function
by the functional equation. Set
\[
 e_j=c_j/c_0,\quad E(z)=C(z)/c_0,\qquad
 H(z)={1\over E(-z)}={c_0\over C(-z)}=\sum_{m\ge0}h_mz^m,
 \quad h_m=0\ (m<0).
 \tag{2}
\]
Then, for r,k≥1,
\[
 \boxed{D_{r,k}=c_0^r\det[h_{r+j-i}]_{0\le i,j<k}.}
 \tag{3}
\]
For completeness take the (r+k)-square upper unit triangular Toeplitz
matrix T with entries e_{j-i}. Its inverse has entries
(-1)^{j-i}h_{j-i}, by E(z)H(-z)=1. The minor on rows 0,…,r−1 and
columns k,…,k+r−1 is D_{r,k}/c_0^r. The complementary inverse minor
has rows 0,…,k−1 and columns r,…,r+k−1. Jacobi's complementary-minor
sign is (-1)^{rk}. Factoring the signs from its entries gives another
(-1)^{rk}; they cancel. This proves (3), with no positivity assumption.
This is rectangular Jacobi–Trudi duality; [García-García–Tierz][ggt]
§2.1 records the standard conventions.

The starting full-phase integral is [Note08](08_RGD_B02_R1_COMPLETE_SOURCE_CONTOUR_MARGIN_20261104.md)
(2), obtained by coefficient extraction from this same complete C.
Equation (3) exactly rewrites its determinant; it replaces no phase
factor or exterior box by a positive integrand. The comparison changes
coordinates before bounding the signed remainder.

Equation (3) is exact for k>r+1 as well: negative h-indices are zero,
not a continuation of an exponential formula. For k=0 the original
triangular determinant is c_0^r; the empty dual determinant is 1.
The normalization c_0=b-d_0/8 is retained. Nothing has discarded the
Green endpoint atom or any source mode. The reciprocal residual below
contains all unextracted singularities and the entire remaining analytic
part. Thus this is a full-phase algebraic comparison of the same source,
not a diagonal, modulus-only or finite-source replacement.

## 3. The finite spectral premise and positive reference margin

Fix k≥1. The premise P_k(S) is that C(-z) has exactly k zeros in the
closed disk |z|≤S, all simple and positive:
\[
 0<\alpha_1<\cdots<\alpha_k<\rho<S,
 \tag{4}
\]
with no zero on |z|=S and no other zero in that disk. This premise must
be supplied for each application, not inferred from c_j>0.
Define
\[
 A_\ell={c_0\over\alpha_\ell C'(-\alpha_\ell)},\qquad
 H(z)=\sum_{\ell=1}^k{A_\ell\over1-z/\alpha_\ell}+G(z).
 \tag{5}
\]
G is analytic in a neighborhood of |z|≤S. Along the real axis C(-z)
starts positive and crosses each simple zero, so
\(\operatorname{sgn}A_\ell=(-1)^{\ell-1}\).
For r≥k−1 all moving indices in (3) are nonnegative and the pole matrix is
\[
 B_{ij}=\sum_{\ell=1}^k A_\ell\alpha_\ell^{-(r+j-i)}.
\]
Factoring B through the powers α_l^i and α_l^{-j} gives
\[
 d^*_{r,k}:=\det B
 =\Delta(\alpha)^2\prod_{\ell=1}^k
       |A_\ell|\alpha_\ell^{-r-k+1}>0,
 \quad \Delta(\alpha)=\prod_{a<b}(\alpha_b-\alpha_a).
 \tag{6}
\]
The product of alternating residue signs cancels the sign of the
inverse-node Vandermonde. Individual residues are not positive.
The margin (6) is evaluated explicitly rather than assumed to be a
positive unknown determinant.

## 4. Complete error payment and actual fixed-k order propagation

Let M≥sup_{|z|=ρ}|G(z)|. Cauchy's estimate pays every residual coefficient:
\(|g_m|\le M\rho^{-m}\) for m≥0. Put β_l=α_l/ρ∈(0,1), and multiply
entry (i,j) of the full dual matrix by ρ^{r+j−i}. This positive diagonal
scaling leaves its determinant sign unchanged. The scaled reference is
\[
 \widetilde B=U\,\operatorname{diag}(A_\ell\beta_\ell^{-r})\,V,
 \qquad U_{i\ell}=\beta_\ell^i,\quad V_{\ell j}=\beta_\ell^{-j}.
 \tag{7}
\]
The scaled error matrix has every entry at most M in absolute value,
hence infinity norm at most kM. With a_min=min_l|A_l|,
\[
 \|\widetilde B^{-1}\widetilde E\|_\infty
 \le {kM\over a_{\min}}\|V^{-1}\|_\infty\|U^{-1}\|_\infty\,\beta_k^r.
 \tag{8}
\]
All these are finite explicit quantities. Lagrange interpolation gives
\[
 u_\ell={\prod_{j\ne\ell}(1+\beta_j)
             \over\prod_{j\ne\ell}|\beta_\ell-\beta_j|},\quad
 u_*:=\max_\ell u_\ell=\|U^{-1}\|_\infty,
 \qquad \|V^{-1}\|_\infty\le\sum_\ell\beta_\ell^{k-1}u_\ell\le ku_*.
 \tag{9}
\]
For the second inequality use
V=diag(β_l^{-(k−1)}) U^T J, with J reversing the k powers.
In particular, the following is a sufficient scalar invariant:
\[
 \delta_r:=B_k\beta_k^r\le\tfrac12,
 \qquad B_k={k^2M\over a_{\min}}u_*^2.
 \tag{10}
\]
The real homotopy I+t\widetilde B^{-1}\widetilde E, 0≤t≤1,
is nonsingular when δ_r<1. Its determinant therefore stays positive;
every eigenvalue modulus of the perturbation is at most δ_r. Thus
\[
 D_{r,k}\ge c_0^r d^*_{r,k}(1-\delta_r)^k
 \ge 2^{-k}c_0^r d^*_{r,k}>0.
 \tag{11}
\]
No Hermitian assumption is needed for this argument.
For B_k>0 a sufficient starting order is
\[
 r_0=\max\left\{1,k-1,
 \left\lceil{\log(2B_k)\over\log(\rho/\alpha_k)}\right\rceil\right\}.
 \tag{12}
\]
If the actual residual is zero, take r_0=max{1,k−1}.
The fixed inputs k,S,ρ,α_l,A_l,M stay unchanged thereafter and
\[
 \delta_{r+1}=\beta_k\delta_r,\qquad
 {c_0^{r+1}d^*_{r+1,k}\over c_0^rd^*_{r,k}}
 ={c_0\over\prod_l\alpha_l}.
 \tag{13}
\]
The equality in the first formula refers to the chosen **majorant**,
not the unknown actual error norm. This is a quantitative order
induction: relative error contracts despite a possibly shrinking
absolute determinant margin. It does not assume D_{r+1,k}>0 as an input.

## 5. Replacing hidden contour minima by explicit full-source growth

One can acquire M and residue bounds without an unmeasured minimum of
|C(-z)| on a circle. Under P_k(S), factor
\[
 F(z)={C(-z)\over c_0\prod_l(1-z/\alpha_l)},\qquad F(0)=1.
\]
F is zero-free on |z|≤S and real positive along the real interval from
0 to each α_l. Since |C(-z)|≤C(S) on |z|=S,
\[
 |F(z)|\le L:={C(S)\over c_0\prod_l(S/\alpha_l-1)}\quad(|z|=S).
 \tag{14}
\]
Here L≥1 by the maximum principle. More generally use any proved upper
bound L≥1 and U_0≥log L. An analytic logarithm g=log F with g(0)=0
exists in the disk. Harnack applied to U_0−Re g gives, at |z|=t<S,
\[
 -{2U_0t\over S-t}\le\Re g(z)\le {2U_0t\over S+t}.
 \tag{15}
\]
If U_0=0 the maximum principle gives g=0. Set
\[
 p_l=\prod_{j\ne l}|1-\alpha_l/\alpha_j|,
 \quad A_l^-={e^{-2U_0\alpha_l/(S+\alpha_l)}\over p_l},\quad
 A_l^+={e^{2U_0\alpha_l/(S-\alpha_l)}\over p_l}.
 \tag{16}
\]
Since A_l=1/[F(α_l)∏_{j≠l}(1−α_l/α_j)],
\(A_l^-\le|A_l|\le A_l^+\). In particular a^-:=min_l A_l^->0.
The following complete triangle/Harnack payment is now explicit:
\[
 \widehat M={e^{2U_0\rho/(S-\rho)}\over\prod_l(\rho/\alpha_l-1)}
       +\sum_l{A_l^+\over\rho/\alpha_l-1},\qquad
 \widehat B_k={k^2\widehat M\over a^-}u_*^2,
 \quad \widehat\delta_r=\widehat B_k\beta_k^r.
 \tag{17}
\]
It suffices to use these upper bounds in (10)–(13). Everything outside
the extracted pole packet is paid, without taking absolute values of
separate terms of the original determinant before obtaining its margin.
The triangle inequality in (17) is a deliberate loss and will matter
in Section 8.

## 6. A fully stated canonical initialization: k=1, r≥1500

This example uses **published finite-zero verification as an input**,
not a new numerical certificate. Platt–Trudgian's published abstract
states reality and simplicity through height 3·10^12. Odlyzko's §2
numbers zeros with multiplicity and gives γ_1=14.134… and γ_2=21.022… .
Only the much weaker facts N(20)=1 and 14<γ_1<15 are needed.
See [the primary-source record][refs]; their computational certificates
were not replayed here.

For s=σ+iγ, the associated zero of C(-z) is z=−(2s−1)^2 and
\[
 |z|=4\gamma^2+(2\sigma-1)^2.
\]
The functional-equation pair gives one z-zero. The stated finite-zero
inputs therefore give exactly one simple zero
α=4γ_1²∈(784,900) in |z|≤1600. There are no extra trivial ξ-zeros.
Choose S=1600 and ρ=1200. This supplies P_1(S); no global RH premise
enters this example.

The complete positive source, including every n≥1 mode, satisfies
\[
 \Phi(u)\le4\pi^2 e^{9u-\pi e^{4u}},\qquad u\ge0.
 \tag{18}
\]
Indeed [Note07][note07] bounds the ratio of the n≥2 source tail to the
first mode by 64e^{−3πe^{4u}}<1, and Φ_1≤2π²e^{9u−πe^{4u}}.
For a=(9+√S)/4=49/4, substitution t=πe^{4u} and
cosh(√S u)≤e^{√S u} give
\[
 C(1600)\le\pi^{2-a}\Gamma(a)<2^{49}.
 \tag{19}
\]
For the coarse last bound, t^{45/4}≤t^{11}+t^{12}, so
Γ(49/4)≤11!+12!<2^49, and π^{2-a}<1.
The primitive is p(u)=∑_{n≥1}e^{u−πn²e^{4u}}. Since e^{4u}≥1+4u,
\[
 d_0\le\sum_{n\ge1}{e^{-\pi n^2}\over4\pi n^2-1}
 \le{e^{-\pi}\over(4\pi-1)(1-e^{-3\pi})}<\tfrac14,
 \qquad c_0=\tfrac1{16}-\tfrac18d_0>\tfrac1{32}.
 \tag{20}
\]
These inequalities also follow with π>3 alone for the last coarse
comparison. No approximate moment value is substituted.

Equations (14), (19), (20) give
L<(9/7)2^54<2^55, so U_0=55 is valid. For k=1 there is no Vandermonde
conditioning factor, and (15)–(17) imply
\[
 e^{-40}<A<e^{142},\qquad
 \sup_{|z|=1200}|H(z)|<3e^{330},\qquad
 M<6e^{330},\qquad M/A<6e^{370}<e^{372}.
 \tag{21}
\]
For example the residue exponents are bounded by 39.6 and 990/7,
respectively. The contour exponent is 2·55·1200/400=330;
ρ/α−1>1/3. With β=α/1200<3/4 and log(4/3)>1/4,
\[
 \delta_r<e^{372-r/4}<\tfrac12\quad(r\ge1500).
\]
Consequently the concrete lower bound is
\[
 \boxed{D_{r,1}>\tfrac12e^{-40}(28800)^{-r}\quad(r\ge1500).}
 \tag{22}
\]
This is a coarse analytical initialization conditional only on the
stated published finite-zero inputs. It is not a newly run certificate,
not an optimal threshold, and not new coverage: the prior web report
already claims a much smaller threshold, with a finite-order overlap.
No effort is proposed to improve 1500 or repeat the known finite cases.

## 7. Exact fixed-N stop, including k/r>1 and every zero-index correction

A fixed pole reference has the rational generating function
\[
 H_N(z)=\sum_{l=1}^N{A_l\over1-z/\alpha_l}
       ={P_{N-1}(z)\over Q_N(z)},\qquad
 Q_N(z)=1+q_1z+\cdots+q_Nz^N.
\]
Let h_m^[N] be its Taylor coefficients for m≥0 and **zero** for m<0.
The rational identity yields the recurrence
\[
 h_m^{[N]}+q_1h_{m-1}^{[N]}+\cdots+q_Nh_{m-N}^{[N]}=0
 \qquad(m\ge N).
 \tag{23}
\]
In the k-square matrix h^[N]_{r+j−i}, the last column has
m=r+k−1−i≥r. If r≥N and k>N, this column plus q_1 times the preceding
column through q_N times its Nth predecessor is zero, row by row.
Hence
\[
 \boxed{\det[h^{[N]}_{r+j-i}]_{i,j<k}=0\quad(r\ge N,\ k>N).}
 \tag{24}
\]
This covers all positive proportional k/r regimes, including k>r+1.
One must not incorrectly extend the exponential coefficient formula to
negative indices. In that boundary regime (24) proves a column relation;
it need not imply rank≤N for the whole matrix. When r≥k−1 there are
no negative entries, the rank is at most N, and every nonzero term in
a reference-plus-residual determinant expansion requires at least k−N
residual columns.

Thus no fixed finite pole packet supplies a positive full determinant
margin in the growing-index region. The full determinant may still be
positive because of the residual; (24) makes no assertion about its sign.
Allowing N=k avoids this exact rank obstruction but introduces new
spectral inputs and the conditioning cost in the next section.

## 8. Quantitative growing-k stop for the chosen payment

For the explicit payment (17) there is a separate lower bound on its
own size. This is a statement about the allowance, not the actual error.
Interpolate the monic polynomial q(x)=(x−1/2)^{k−1} at β_1,…,β_k.
Its leading coefficient gives
\[
 1=\sum_i{q(\beta_i)\over\prod_{j\ne i}(\beta_i-\beta_j)},\quad
 |q(\beta_i)|\le2^{1-k},\quad
 u_*\ge {2^{k-1}\over k}.
 \tag{25}
\]
Also the kth summand of (17), and a^-≤A_k^-≤A_k^+, imply
\(\widehat M/a^-\ge\beta_k/(1-\beta_k)\). Therefore
\[
 \boxed{\widehat\delta_r\ge
    4^{k-1}{\beta_k^{r+1}\over1-\beta_k}.}
 \tag{26}
\]
If k→∞, k/r≥c>0 and β_k→1, this diverges: after dividing its logarithm
by k, the first term tends to log4, the term (r+1)logβ_k/k tends to zero,
and −log(1−β_k)/k is nonnegative. The allowance cannot meet 1/2.
The proof uses the fixed definition (17); it does not put a lower bound
on a sharper or cancellation-preserving contour residual.

The relevant radial clustering follows from ordinary zero counting,
without global RH. Order all zeros of C(-z) by modulus with multiplicity,
and call the resulting moduli R_j. Since 0<Re s<1 for ξ-zeros and
|z|=4γ²+(2Re s−1)², their radial count n(R), for R>1, lies between
N(√(R−1)/2) and N(√R/2), up to the immaterial convention at an endpoint.
The Riemann–von Mangoldt asymptotic gives
n(R)~√R log R/(8π). The source excerpt in Odlyzko §2, equations
(2.3), (2.5), (2.6), supplies this standard count, not a zero-gap conjecture.
It follows that R_{j+1}/R_j→1: a fixed relative gap along a subsequence
would contradict the count asymptotic at two interior radii of that gap,
without any endpoint-count convention.

In any valid P_k(S) packet, α_k=R_k and α_k<ρ<S<R_{k+1}.
Consequently β_k→1 along any unbounded sequence of valid packets.
If such packets exist, (26) defeats the selected payment whenever
k/r is bounded below by a positive constant in the domain r≥k−1.
No assertion that arbitrarily long valid packets exist is made.
For k>r+1 the Section 4 exponential-matrix proof is not applicable at
all; the exact fixed-N stop (24) still applies there.

This is an unusually explicit warning about separate-bound losses:
for the polynomial E(z)=∏_{i=1}^k(1+z/α_i), the true residual G is zero
and the pole comparison is exact, whereas the triangle majorant (17)
is positive and may fail. Thus (26) excludes this **specified payment**,
not all reciprocal-residue comparisons. It is distinct from the exact
fixed-N reference vanishing in (24).

## 9. Control screen and what is still missing

The general conditional theorem uses finite simple real poles and a
complete contour remainder. It is not a characterization of theta.
The canonical example additionally uses the exact unit-square source,
Green normalization and named finite-zero verification. The repository
controls fail that exact-source premise in the following ways; their
satisfaction or failure of P_k(S) is **not** inferred just from those
source differences:

| Repository control family | Premise absent from the canonical application |
| --- | --- |
| Euler-factor shifted sources | Original unmodified theta source and Dirichlet coefficients |
| Weighted-square and finite-source controls | Full unit-weight infinite square sum/full reflection |
| Reflected super-Gaussian; smooth positive-primitive controls | Canonical arithmetic square expansion, despite shared reflection/shape/primitive data |
| Finite-prime orbit and finite-profile controls | Complete source identity; only selected measurements/identities are retained |
| BW-01 atom controls | Smooth canonical source and complete profile |
| RH-conditional endpoint controls | Ordinary theta Dirichlet-series arithmetic; added double zeros also violate any packet containing them |
| Fixed-amplitude variable-kernel controls | Actual cosh/cosine transform equation used in (1) |

These distinctions alone do not make (10) a global discriminator.
For a direct demonstration, fix a>0, 0<β<σ and 0<ε<1 and set
\[
 C_\varepsilon(z)=s\cosh(a\sqrt z)
                  (e^{\sigma z}+\varepsilon e^{\beta z}),
 \quad s={1\over16\cosh(a)(e^\sigma+\varepsilon e^\beta)}.
 \tag{27}
\]
This is the cosh transform of a smooth positive even Gaussian-mixture
source on the half-line: use the symmetric mixtures with means ±a,
variances 2σ and 2β, and their even full-line density restricted and
doubled on u≥0. It satisfies C_ε(1)=1/16. Its positive, boundary-compatible Green
primitive is displayed below; the spectral screen already follows from
the exact transform.

Its cosh zeros are simple negative real points; its other zeros are
\[
 z={\log\varepsilon+(2m+1)i\pi\over\sigma-\beta},\qquad m\in\mathbb Z.
 \tag{28}
\]
Taking ε sufficiently small puts all the latter outside any prescribed
finite disk, so P_k(S) and the fixed-k mechanism can hold for any
prescribed finite prefix even though the entire function has nonreal
zeros. This is an explicit off-axis-zero control, not a claimed certified
positive-time collision and not a canonical square-source example.
It proves that no global conclusion follows from an arbitrary finite
prefix alone. A positive primitive compatible with the inherited
operator is obtained directly as
\(p(u)=8\int_u^\infty\sinh(v-u)\Phi(v)\,dv>0\), which satisfies
p''−p=8Φ and p'(0)=−8C_ε(1)=−1/2; integration by parts then retains
b=1/16. This is the primitive relevant to the Green normalization.

A growing-index successor must therefore do more than request another
finite zero prefix or improve the constant 1500. It must supply a
comparison with a nonzero margin in growing dual dimension, keep the
boundary zeros, and pay a correlated residual without the loss proved
in (26). A real-simple pole prefix at every radius is RH plus simplicity;
using it to initialize a purported proof is circular. Neither (24) nor
(26) excludes a different infinite-dimensional reference or a genuinely
cancellation-sensitive complete-source inequality.

## 10. Disposition and bounded continuation

**B02 r2 complete as a scoped conceptual return.** Fixed k has an
explicitly initialized order invariant; the selected path stops for the
proportional-index region for the reasons proved above. This adds no
all-index result and no new theta positivity range. The received
E04 r4 assessment and Notes07–09 are unchanged.

**Next: [E] RGD-E04 r5 — Sol**, one analytical assessment of the frozen
identities, pole signs, norm bounds, canonical constants, boundary
recurrence, conditioning stop and source qualifications. See
[Packet15][packet15] and the [continuation/model-change guide][guide].
No numerical acquisition, threshold optimization, certificate campaign
or additional mechanism is part of that task. A later B02 r3 needs a
fresh conceptual choice that addresses the precise failure above; it is
not automatically issued by this return.

[packet13]: ../research-progress/handoffs/13_RGD_E04_R4_RETURN_AND_B02_R2_MODEL_CONTINUATION_20261104.md
[packet15]: ../research-progress/handoffs/15_RGD_E04_R5_RECIPROCAL_COMPARISON_ASSESSMENT_20261104.md
[guide]: ../research-progress/handoffs/14_RGD_B02_R2_RETURN_AND_MODEL_CONTINUATION_20261104.md
[review]: ../reviews/07_RGD_B02_R2_AUTHOR_AND_SAME_MODEL_CHECKS_20261104.md
[note07]: 07_RGD_B03_R2_EXACT_PAYMENT_OBSTRUCTION_AND_TRUE_TAIL_20261104.md
[refs]: ../references/02_RECIPROCAL_COMPARISON_AND_FINITE_ZERO_SOURCES_20261104.md
[kenan]: https://kenan.works/posts/fifteen-shifts-of-xi/
[ggt]: https://doi.org/10.1016/j.jcta.2019.105201
[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a11]: ../../../../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md
[a16]: ../../../../../../../avoid/16_unchecked_imports_and_novelty_claims.md

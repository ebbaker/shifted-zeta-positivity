# RGD-E04 r6: Gaussian-reference proof and scope checks

4 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance; actual **gpt-6.1-sol (Codex), effort ultra**,
continuing chat0006, thread 01a1a7f8-9f05-7120-8691-d40d5b3b3333,
turn 01a1a825-c9d5-7bf0-8acb-e025d4bd394c. Type **E** under
[Packet17][packet].

**All ten obligations are accepted within scope, without mathematical
correction.** [Review10][review] records the disposition. This note
supports the fixed assessment of [Note12][input]; it selects no new
reference. One analytical pass, no correction pass or numerical work.
The nine frozen input sizes/hashes match. Three read-only Sol/ultra
contributors checked separate proof/source obligations; the coordinator
checked and wrote the return. This is different-model internal assessment
of Astra/ultra work with shared premises, not specialist independence.

## 1. Endpoint matching and a reference margin at every size

The inherited c0=b−d0/8 and 1/32<c0<b=1/16 imply
0<t=log(b/c0)<log2. The half-line Gaussian density in Note12 (2) has
mass c0 and cosh transform c0 exp(tz), fixing C_G(0)=c0 and C_G(1)=b.
Differentiating the stated Green primitive yields

\[
 p_G'(u)=-8\int_u^\infty\cosh(v-u)\Phi_G(v)\,dv,\qquad
 p_G''-p_G=8\Phi_G.
\]

Thus p_G'(0)=−8b=−1/2. Tonelli, using
∫_0^v sinh(v−u)du=cosh v−1, gives
∫p_G=8(b−c0)=d0. The complete signed source difference has both
transform cancellations Delta E(0)=Delta E(1)=0.
No source mode, tail or Green boundary term was removed.

For B_ij=g_(k+j−i), divide column j by t^(k+j)/(k+j)! and row i by
t^(−i). The remaining entry is the falling factorial (k+j)_i.
Its monic degree-i polynomial basis gives the Vandermonde on
k,...,k+r−1, with determinant ∏_(j=0)^(r−1)j!. The total t exponent
is rk. Therefore

\[
 \det B=m_{r,k}=t^{rk}\prod_{j=0}^{r-1}\frac{j!}{(k+j)!}>0,\qquad
 m_{r,k}\ge\left(\frac{t}{r+k}\right)^{rk}.
\]

If i>k+j, the falling factorial contains zero and precisely reproduces
the negative-index coefficient convention. The formula holds for all
r,k≥1, including r>k+1. Each quotient (k+j)!/j! has k factors bounded
by r+k, establishing the displayed lower bound.

## 2. Complete-source upper growth and determinant scaling

The already accepted all-mode envelope from Note10 gives, for R>0 and
alpha=(9+sqrt R)/4,

\[
 E(R)\le\frac{\pi^{2-\alpha}}{c_0}
       \int_\pi^\infty v^{\alpha-1}e^{-v}\,dv
 < F(R)=32\pi^{2-\alpha}\Gamma(\alpha).
\]

Here alpha>9/4. With N=ceil alpha,
v^(alpha−1)≤1+v^N on both 0<v≤1 and v≥1. Hence
Gamma(alpha)≤1+N!, and log N!≤N log N gives
log F(R)=O(sqrt R log R) as an upper bound for R≥2.
No finite-zero information or global real-zero premise enters.

For A_ij=e_(k+j−i), scale entry (i,j) by R^(k+j−i).
The determinant multiplier is R^(rk)>0. Every scaled entry with
nonnegative index is at most E(R), since e_m≥0; negative-index entries
remain zero. Each row Euclidean norm is at most sqrt(r)E(R).
Hadamard and the reference lower bound consequently give

\[
 \left|\frac{\det A}{m_{r,k}}\right|
 \le r^{r/2}E(R)^r
       \left(\frac{r+k}{tR}\right)^{rk}
 \le\overline U_{r,k}(R).
\]

Both directions are upper bounds on the actual determinant ratio.
They do not lower-bound the canonical determinant or estimate separate
source errors. Hadamard's loss is harmless for proving this ratio small.

## 3. Uniform domain, exact residual and the adaptive diagnostic

Fix M>0, set R_k=k²/log²k for k≥3, and let 1≤r≤Mk.
Then log F(R_k)≤Ck for large k. Also r+k≤(M+1)k, so

\[
 \frac1r\log\overline U_{r,k}(R_k)
 \le-k\log k+2k\log\log k+C_Mk.
\]

The term (log r)/2 is uniformly absorbed into C_M k.
This proves the asserted rth-root convergence uniformly over the full
domain, including fixed r and r proportional to k. Since r≥1, it also
proves uniform convergence of the ratio itself to zero.
Fixed k with unbounded r is outside this domain.

For K=B^(-1)(A−B), det(I+K)=det A/m exactly. If an induced norm has
||K||<1, every eigenvalue lambda of K obeys |lambda|≤||K||, giving
|det(I+K)|≥(1−||K||)^r. The real homotopy I+sK, 0≤s≤1, also
fixes a positive determinant sign. If ||K||≥1 the following bound is
immediate; otherwise it follows from that determinant inequality:

\[
 \|K\|\ge1-\overline U_{r,k}(R_k)^{1/r}.
\]

Thus liminf ||K||≥1 uniformly in the stated domain, for every induced
norm. This is a lower bound, not a claim that ||K|| converges to one.
An invertible simultaneous scaling A→LAR and B→LBR gives
K→R^(-1)KR. Norm values can change; the determinant-based lower bound
and its obstruction survive the similarity.

The exact scalar residual satisfies
(det A−m)/m→−1 and |det A−m|/m→1 uniformly. These conclusions
exclude fixed relative slack, not every tolerance approaching one.
When |det A|<m, the strict scalar condition |det A−m|<m is equivalent
to det A>0. Asking for that condition without an independent signed
estimate would merely restate the target.

For a hypothetical positive moving exponential slope, combine
(1−delta)^r≤|det A/m| with the upper ratio bound. Solving gives exactly

\[
 t_{r,k}\le
 \frac{r+k}{R_k(1-\delta)^{1/k}}\,
 r^{1/(2k)} E(R_k)^{1/k}
 =O_{M,\delta}\left(\frac{\log^2 k}{k}\right).
\]

This is necessary only. The two endpoint constraints fix the original
t=log(b/c0)>0, preventing that vanishing scale in the same family.
No moving reference is constructed or validated by this diagnostic.

## 4. The single quadratic adjustment and the positive control

For E2(z)=exp((t+q/2)z−qz²/2), both endpoint values are retained.
If q>0, E2(x)→0 as x→positive infinity. An entire series with
nonnegative coefficients and constant one cannot do this. Some
e_j^[2]<0, giving a negative (1,j) reference minor.
If q<0, its purely algebraic dual
H2(z)=1/E2(−z)=exp((t+q/2)z+qz²/2) tends to zero on that axis.
Some h_j^[2]<0, and exact rectangular duality gives a negative (j,1)
reference minor. The zero negative-index convention is unchanged.
For q=0 the Gaussian obstruction above applies.
These witnesses disprove universal reference positivity for nonzero q;
they do not settle every proportional-index subdomain or canonical q.

The inspected [DLMF 4.36.2][dlmf] gives the cosh product. Thus the
normalized control in Note12 (16) has
E_*(z)=∏_(j≥1)(1+x_j z), with
x_j=4ell²/((2j−1)²pi²)>0 and ∑x_j finite.
For finite products, work in dimension r+k. Each upper bidiagonal
factor I+x_j S has nonnegative minors. In Cauchy–Binet, moving the
whole consecutive r-block one column in each of the first k factors
and choosing identity moves thereafter supplies the strict term
(x1...xk)^r. All other terms are nonnegative. Local convergence of the
infinite product gives convergence of the finitely many coefficients
in a fixed rectangle, preserving this lower bound for every r,k.

Its source is the atom c_*,0 delta_ell. The continuous, piecewise smooth
primitive p_*(u)=8c_*,0 sinh(ell−u) below ell and zero above ell has
derivative jump +8c_*,0 at ell. Therefore
p_*''−p_*=8c_*,0 delta_ell distributionally, and
p_*'(0)=−8c_*,0 cosh ell=−1/2.
Using E_*(R)=cosh(ell sqrt R) in the same upper-bound argument shows
that the Gaussian comparison fails even though every target rectangle
is strictly positive. This is not a certified positive-time collision.

The [cluster12 screen][controls] names the missing canonical premise for
each family: unmodified theta coefficients for Euler shifts; the complete
unit-weight infinite sum/full reflection for weighted/finite sources;
arithmetic square expansion for reflected/positive-primitive controls;
the full identity for finite-prime/profile controls; smooth complete
source for BW-01 atoms; ordinary Dirichlet arithmetic for conditional
endpoint controls; and the observation equation for variable kernels.
These distinctions do not prove that a quantitative bound fails on
each control. A positive-time collision alone does not refute an arbitrary
time-zero finite inequality.

## 5. Provenance, consequence and continuation

[References03][refs] records DLMF version1.2.8, 15 September 2026;
the equation and version were reinspected. Etingof/Novak material remains
optional standard background, not a theta residual theorem or proof
dependency. Bounded reinspection confirmed the Etingof reading copy's
receipt, 10 January 2011 title page and cited theorem numbering, and
Novak's dated lecture/Theorem25.3. Specific version/access records are
preserved; no full book or literature audit is claimed.
All nine frozen inputs retain their original bytes. No zero data,
numerical acquisition, sign scan, certificate replay or new positivity
range enters this assessment.

Under the [result index][results] and [avoid index][avoid], especially
[01][a01], [05][a05], [07][a07], [12][a12] and [16][a16], this accepts
two scoped obstructions. Park the Gaussian/quadratic-reference attempt.
The [continuation/model-change guide][next] proposes a later
**B02 r4 — B/Astra** decision about a suitable reference growth scale
or independently controlled signed residual. It does not activate a
new mechanism, numerical task, manuscript milestone or investigation
closure. This executing conversation keeps chat0006, distinct from
the originating B02 r3 chat0007.

[packet]: ../research-progress/handoffs/17_RGD_E04_R6_GAUSSIAN_REFERENCE_ASSESSMENT_20261104.md
[review]: ../reviews/10_RGD_E04_R6_GAUSSIAN_REFERENCE_ASSESSMENT_20261104.md
[input]: 12_RGD_B02_R3_GAUSSIAN_REFERENCE_GROWTH_STOP_20261104.md
[refs]: ../references/03_GAUSSIAN_REFERENCE_AND_SCHUR_BACKGROUND_20261104.md
[dlmf]: https://dlmf.nist.gov/4.36.E2
[next]: ../research-progress/handoffs/19_RGD_E04_R6_RETURN_AND_MODEL_CONTINUATION_20261104.md
[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a05]: ../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a16]: ../../../../../../../avoid/16_unchecked_imports_and_novelty_claims.md

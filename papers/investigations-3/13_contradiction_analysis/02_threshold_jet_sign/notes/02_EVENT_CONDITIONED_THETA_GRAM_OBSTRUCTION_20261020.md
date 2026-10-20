# Exact theta Gram data do not close the event-conditioned Hilbert-ball estimate

20 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Authoring model **gpt-6-astra (Codex)**; actual reasoning effort **ultra**, inherited from the parent turn and verified there against turn `01a157aa-be5d-72e0-90dc-ed57a8823b52`.

**Status: scoped estimating-rule obstruction, proved in-note; [separate same-model internal review][review], not specialist review.** This screens one BW2-01/02 attempt before numerical acquisition. Its best upper bound is strictly positive even with exact, phase-coupled theta Gram entries and exact event cancellation. The bound strictly improves the independent-coordinate-box bound, but cannot reach the required nonpositive sign. No useful arithmetic sign estimate, theta event exclusion, new covered region, later witness, or RH conclusion is obtained.

Canonical ownership is the [threshold higher-jet sign investigation][initial]. BW-01 is the physical consumer. Follow the [active program][program], [result summaries][results], [collision controls][controls] and [patterns to avoid][avoid], particularly [classification][a01], [scoped conclusions][a07], [signed recombination][a12] and [volume without gain][a20]. The result is a precise obstruction to the selected relaxation; it is not another criterion counted as progress toward its sign.

## 1. Selected contract and what information is discarded

Use exactly the physical source and normalization of [BW-01 Contract 02][source]:

\[
 d\nu(u)=e^{Tu^2}\Phi(u)\,du,\qquad
 \Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})
                  e^{-\pi n^2e^{4u}},\quad u\ge0.
\]

Parameters are the **actual** physical time and height, with
\(0<T\le1/2\), \(a>0\). At a hypothetical double threshold event,
\(H(T,a)=H_x(T,a)=0\), \(h_2\ne0\), and the inherited necessary
restriction is

\[
 Q_L=2h_3^2-3h_2h_4-18Lh_2^2>0,
 \qquad 0<L\le L_2(a).
\tag{1}
\]

The current attempt asks if a full quadratic Gram estimate can give an opposing upper bound. It retains the mixed term in (1) before optimization; it does not separately bound that signed interaction first.

Put \(M_j=\int u^j d\nu\), and work in the real Hilbert space
\(\mathcal H=L^2(\nu)\). Define

\[
 f_0=\cos(au),\quad f_1=-u\sin(au),\quad f_2=-u^2\cos(au),
 \quad f_3=u^3\sin(au),\quad f_4=u^4\cos(au).
\]

The physical multiplier is exactly \(w=1\), so
\(h_j=\langle1,f_j\rangle\), and \(\|1\|^2=M_0\).
The **selected reduced information set** consists of:

1. the exact fifteen Gram entries \(\langle f_i,f_j\rangle\), \(0\le i\le j\le4\), computed with the unchanged theta measure;
2. the source norm budget \(\|w\|^2\le M_0\);
3. the exact linear event constraints \(\langle w,f_0\rangle=\langle w,f_1\rangle=0\).

For its double-event application require additionally \(\langle w,f_2\rangle\ne0\). The relaxation permits arbitrary real signed \(w\in\mathcal H\); it discards the physical identity \(w=1\), positivity of a modified source, an all-real slice, and threshold minimality. In particular it does **not** retain the mass anchor \(\langle w,1\rangle=M_0\). Section 6 explains why that omission matters.

These are finitely many exact theta correlations, **not all information about the complete theta source**. Their numerical values depend on all unchanged theta coefficients and the one actual height. Controls generally have different values. The proposed quantitative input was these phase-coupled entries as an improvement over separate derivative norms; the theorem below shows their use in this specified relaxation cannot attain the sign. This is a screened contract and closed attempt, not fulfillment of the program's need for a useful distinguishing arithmetic estimate.

## 2. Exact coefficient and phase interface

Set \(\epsilon_j=(-1)^{\lfloor(j+1)/2\rfloor}\), so an even-indexed \(f_j\) is \(\epsilon_j u^j\cos(au)\) and an odd-indexed one is \(\epsilon_j u^j\sin(au)\). Define complete observations

\[
 C_k=\int u^k\cos(2au)\,d\nu,\qquad
 S_k=\int u^k\sin(2au)\,d\nu.
\]

The Gram matrix \(G\) is exactly

\[
 G_{ij}=\frac{\epsilon_i\epsilon_j}{2}
 \begin{cases}
 M_{i+j}+C_{i+j},&i,j\text{ both even},\\
 M_{i+j}-C_{i+j},&i,j\text{ both odd},\\
 S_{i+j},&i,j\text{ of different parity}.
 \end{cases}
\tag{2}
\]

Thus the requested observations are complete moments through order eight and physical jets through order eight at the coupled height \(2a\). No independent phase, changed heat weight, coefficient cutoff, or Riemann--Siegel normalizer is introduced. In particular, a first-jet arithmetic approximation contract does not supply (2).

All moments are finite at every finite real \(T\). Indeed, for \(v=e^{4u}\ge1\), \(\sum_{n\ge1}n^4e^{-\pi n^2v}\le e^{-\pi v}\sum_{n\ge1}n^4e^{-\pi(n^2-1)}\); the last sum is finite. Dropping the negative term in \(\Phi\) therefore bounds it by a constant times \(e^{9u-\pi e^{4u}}\), which remains integrable after every finite heat and polynomial weight. The series is locally uniformly convergent. Each individual source summand is strictly positive on \(u\ge0\), since
\(2\pi n^2e^{4u}-3>0\). Hence \(\nu\) has a strictly positive continuous density on every finite interval.

**Lemma.** The five \(f_j\) are linearly independent in \(\mathcal H\), so \(G\) is positive definite.

**Proof.** A vanishing linear combination is
\(P(u)\cos(au)+R(u)\sin(au)=0\), where \(P\) has degrees among \(0,2,4\) and \(R\) among \(1,3\). Positive density makes it zero almost everywhere on any interval; continuity then makes it zero there, and real analyticity extends the identity to all real \(u\). At \(u=(k+1/2)\pi/a\), \(R\) has infinitely many zeros. Thus \(R=0\), and then \(P=0\). No genericity assumption is used. \(\square\)

## 3. The optimal bound from the selected information

Let \(E=\operatorname{span}\{f_0,f_1\}\), let \(P\) be orthogonal projection onto \(E^\perp\), and put \(p_j=Pf_j\) for \(j=2,3,4\). Partition \(G\) with indices \(\{0,1\}\) followed by \(\{2,3,4\}\). The event-projected Gram matrix is the positive definite Schur complement

\[
 K=G_{234,234}-G_{234,01}G_{01,01}^{-1}G_{01,234}.
\tag{3}
\]

At an exact event \(1\in E^\perp\), so the physical jet is among the relaxed possibilities. More generally the possible vectors
\(y=(\langle w,f_2\rangle,\langle w,f_3\rangle,\langle w,f_4\rangle)\)
under the selected information are **exactly**

\[
 y^\mathsf TK^{-1}y\le M_0.
\tag{4}
\]

Indeed the minimum-norm vector giving \(y\) is
\(w_y=\sum_{j=2}^4(K^{-1}y)_jp_j\), with squared norm equal to the left side. Every other realizing vector has an orthogonal additional component. This proves both inclusions. Requiring norm equality instead does not change (4), since the infinite-dimensional orthogonal complement of all five \(f_j\) can supply any missing norm.

Define

\[
 A_L=\begin{pmatrix}-18L&0&-3/2\\0&2&0\\-3/2&0&0\end{pmatrix}.
\]

The strongest upper bound available from **this reduced information set** is therefore

\[
 \boxed{U_\theta(T,a,L)
 =M_0\lambda_{\max}(K^{1/2}A_LK^{1/2}).}
\tag{5}
\]

This is an attained maximum of \(y^\mathsf TA_Ly\) over (4). It keeps all correlations in the selected Gram data and all signs in (1). It is not claimed to be the best bound from the full known source.

The \(2,4\) block of \(A_L\) has determinant \(-9/4\), hence one positive and one negative eigenvalue; its remaining eigenvalue is \(2\). Congruence by the invertible \(K^{1/2}\) preserves inertia. Thus (5) has a strictly positive largest eigenvalue for every finite \(L>0\). Increasing \(L\) cannot make this estimator nonpositive.

A quantitative positive lower bound for this unavoidable upper allowance is available without any spectral computation. Let

\[
 r=p_3-\operatorname{proj}_{\operatorname{span}\{p_2,p_4\}}p_3,
 \qquad R=\|r\|^2
 =\frac{\det K}{\det K_{\{2,4\},\{2,4\}}}
 =\frac{\det G}{\det G_{\{0,1,2,4\},\{0,1,2,4\}}}>0.
\tag{6}
\]

Taking \(w=\sqrt{M_0/R}\,r\) gives \(y_2=y_4=0\) and
\(y_3=\sqrt{M_0R}\). Therefore

\[
 \boxed{U_\theta(T,a,L)\ge2M_0R>0.}
\tag{7}
\]

The positive expression (7) is an explicit positive lower bound on the unavoidable remaining deficit to a nonpositive upper bound within the selected information class, not a lower bound on the physical \(Q_L\).

**Nonzero curvature does not repair the relaxation.** For \(\varepsilon\ne0\), put

\[
 w_\varepsilon=\frac{\sqrt{M_0}(r+\varepsilon p_2)}
 {\sqrt{R+\varepsilon^2K_{22}}}.
\]

It satisfies both event constraints and the exact norm budget, and
\(y_2=\sqrt{M_0}\varepsilon K_{22}/\sqrt{R+\varepsilon^2K_{22}}\ne0\).
Its quadratic is

\[
 Q_L(y)=\frac{M_0}{R+\varepsilon^2K_{22}}
 \left[2R^2+4\varepsilon RK_{23}
 +\varepsilon^2(2K_{23}^2-3K_{22}K_{24}-18LK_{22}^2)\right].
\tag{8}
\]

Let \(B=4R|K_{23}|+|2K_{23}^2-3K_{22}K_{24}-18LK_{22}^2|\).
For
\(0<|\varepsilon|\le\min\{1,R^2/(R^2+B)\}\), the absolute value of the two nonconstant terms in brackets is at most \(|\varepsilon|B<R^2\) when \(B>0\), and is zero when \(B=0\). Thus (8) is strictly positive, quantitatively greater than
\(M_0R^2/(R+\varepsilon^2K_{22})\). There is no assertion for a separately prescribed lower bound on \(|y_2|\).

These signed multipliers need not be positive, smooth, or heat sources with an all-real slice. They are witnesses that the **selected Hilbert-ball estimate** cannot prove its requested sign, not physical counterexamples to theta or new collision controls.

## 4. Matched comparison: correlation improves the bound but not its sign

The independent coordinate bounds from the same projected source data are
\(|y_j|\le\sqrt{M_0K_{jj}}\). Their exact box maximum is

\[
 U_{\rm box}=M_0\left(2K_{33}+3\sqrt{K_{44}}s_*-18Ls_*^2\right),
 \quad s_*=\min\{\sqrt{K_{22}},\sqrt{K_{44}}/(12L)\}.
\tag{9}
\]

This already retains the negative diagonal term. Simply dropping it gives the weaker upper allowance
\(M_0(2K_{33}+3\sqrt{K_{22}K_{44}})\).

In fact

\[
 0<2M_0R\le U_\theta<U_{\rm box}.
\tag{10}
\]

The non-strict comparison follows from ellipsoid containment in the box. For strictness, note \(s_*>0\) and the extra maximum in (9) is positive. A maximizing box vector therefore has \(y_2\ne0\), and must simultaneously saturate the \(y_3\) and \(y_4\) coordinate bounds. A vector in (4) cannot do this: equality in the \(y_3\) Cauchy bound fixes its minimum-norm realizing vector proportional to \(p_3\), whereas equality in the \(y_4\) bound makes it proportional to \(p_4\). Positive definiteness forbids their proportionality. Compactness then gives a strict gap.

Thus the exact, fully optimized matched gain is \(U_{\rm box}-U_\theta>0\), while (7) proves that even this optimal correlated use cannot reach zero. No numerical theta table or cost comparison is needed to close this estimator class. This is not a claim that actual theta correlations are uninformative in other estimators.

## 5. Complete error and control ledger

The proof uses exact full-source integrals. There is no omitted theta mode, source tail, quadrature error, analytic correction, cutoff crossing, normalizer change, or approximate event in (2)--(10). Finiteness of the exact integrals is proved above; their values are not presented as numerically acquired.

A numerical implementation would need complete acquisition of \(M_j\) and \(H^{(j)}(T,2a)\) through order eight, with outward matrix inversion and spectral enclosure. If \(|T-\widehat T|\le\Delta_T\), \(|a-\widehat a|\le\Delta_a\), and all paths have time at most \(B_0\), a sufficient entrywise parameter allowance is

\[
 |G_{ij}(T,a)-G_{ij}(\widehat T,\widehat a)|
 \le M_{i+j+2}(B_0)\Delta_T+2M_{i+j+1}(B_0)\Delta_a.
\tag{11}
\]

It follows by differentiating the complete integrand and bounding the two height derivatives separately. This requires moments through order ten, beyond the raw fourth-jet interface. A source truncation would require its own exhaustive order-ten tails; the inherited order-six budget cannot silently be reused. Approximate event cancellation would enlarge (4), not justify imposing exact zero on an approximate sample. Every valid upper enclosure of (5) remains at least its strictly positive exact value; more precision cannot turn this estimator into the missing contradiction.

The control screen uses each family's own measure and data:

| Family | Applicable facts and exact scope |
| --- | --- |
| Unchanged theta | Positive full-support density and finite moments make \(G,K\) positive definite. The exact physical multiplier is 1; the obstruction concerns enlarging that singleton to the declared signed ball. |
| Euler-factor controls | Their own positive smooth full-support source has the same Gram obstruction. Their unchanged-theta coefficient premise fails; no threshold height or multiplicity is invented. |
| Weighted-square, finite-prime, reflected smooth, positive-primitive controls | Whenever their documented source is positive on an interval and has the required moments, the same analytic independence proof gives their own positive Gram allowance. The estimator does not use an all-real slice, and none is assigned to controls lacking one. They fail the unchanged normalized theta coefficients or full reflection as recorded in cluster 12. |
| Three-atom BW-01 family | Its five-function Gram matrix is singular, so the positive-definite theorem is not applied. Its own exact positive \(Q_L\) is already proved in [BW-01 Note 04][atomic]. That control preserves source positivity and a true threshold but does not retain these exact theta Gram values. Neither obstruction class contains the other's premises. |
| Hermite/quartic models | They need not possess a positive cosine-source measure. No theta Gram constants or Hilbert premise are assigned to them; the inherited polynomial jet tests remain valid in their own normalization. |
| Smooth-density/two-channel constructions | Auxiliary positive realizations alone do not identify this physical measure or its exact Gram matrix. No physical threshold follows from those auxiliary facts. |
| Multiplicative phase relaxations | They are not used: (2) retains a single actual height and its coupled double height. The enlargement here is the multiplier ball, not independently adjustable arithmetic phases. |

No false control rejection is asserted. In particular, a control's failure of the literal theta identity is not claimed to force the opposite sign of (1).

## 6. Mass saturation, next estimating step and stopping scope

One omitted piece of exact source information collapses this relaxation. If it also requires

\[
 \langle w,1\rangle=M_0,\qquad \|w\|^2\le M_0,
\]

then
\(\|w-1\|^2=\|w\|^2+M_0-2\langle w,1\rangle\le0\), hence \(w=1\).
The original physical jets are recovered; their unknown signed quadratic is not estimated by that identity. This is why (5) is not described as optimal among all uses of the known theta source.

A quantitative approximate anchor \(\langle w,1\rangle\ge M_0-\eta\), \(\eta\ge0\), gives \(\|w-1\|\le\sqrt{2\eta}\). At an exact physical event, both \(w\) and 1 lie in \(E^\perp\), so
\(|\langle w,f_j\rangle-h_j|\le\sqrt{2\eta K_{jj}}\).
This states the conditioning cost of an additional affine observation. It is not a new acquired theta jet bound or a reason to launch a sweep: applying the inherited product allowance still needs signed information about the physical center.

**Stop this homogeneous norm-plus-finite-Gram relaxation as a route to \(Q_L\le0\).** The explicit deficit (7) holds at every actual \(a>0\), every finite \(T\) in the stated event domain, and every positive \(L\), including every admissible inherited coefficient. A next attempt must retain quantitatively useful affine or coefficient-level information about the physical multiplier, or change the observation mechanism. Adding more precision to the same finite Gram matrix cannot help its sign. A specified curvature floor, positivity-constrained variational class, larger affine observation set, or different signed arithmetic estimate lies outside the proved obstruction.

BW2-01/02's **selected attempt** can close with this obstruction; the useful arithmetic upper bound required to activate BW2-04/05 remains missing. This does not close the broader route or license claiming all program tasks completed.

## 7. Provenance

The accompanying [input receipt][receipt] records SHA-256 hashes of the inherited program, source contract, sign note, collision-control summary and policies against the exact parent Git revision. It identifies the files read, including uncommitted versions; hashes certify file identity, not mathematical validity. No manuscript snapshot or large dataset was created.

[initial]: 01_INITIAL_RESEARCH_NOTE_20261019.md
[program]: ../../04_boundary_winding/research-overview/02_THRESHOLD_SIGNED_ARITHMETIC_RESEARCH_PROGRAM_20261020.md
[source]: ../../04_boundary_winding/threshold_routes/01_local_double_winding/notes/02_PAIRED_FACE_CONTRACT_20261019.md
[atomic]: ../../04_boundary_winding/threshold_routes/01_local_double_winding/notes/04_EVENT_CONDITIONED_POSITIVE_SOURCE_OBSTRUCTION_20261020.md
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a20]: ../../../../../avoid/20_volume_without_a_gain.md

[review]: ../reviews/01_EVENT_CONDITIONED_THETA_GRAM_REVIEW_20261020.md
[receipt]: ../numerics/THETA_GRAM_INPUTS_20261020.json

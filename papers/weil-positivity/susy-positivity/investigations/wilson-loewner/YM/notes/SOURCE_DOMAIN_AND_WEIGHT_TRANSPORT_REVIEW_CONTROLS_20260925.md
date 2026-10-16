# Source domains and a weight-transport control for bare existence

Date: 25 September 2026, America/New_York.  
Prepared for Edward Baker with substantial LLM assistance.  
Model exposed: GPT-6 (Codex). Exact variant and configured reasoning-effort label are not exposed to this session; neither is inferred from the previous task's commit message.  
Review baseline: `afe7d2c013fa752da63b56e851dd56392980e14a`.  
Status: elementary review controls with proofs, not independent human validation or a new YM realization. No novelty claim.

This accompanies the [review of the three 24 September notes](../reviews/OFF_DIAGONAL_AND_GLOBAL_MECHANISMS_REVIEW_20260925.md). It supplies two details for the [compact-source criterion](OFF_DIAGONAL_RIGIDITY_AND_COMPACT_SOURCE_EXISTENCE_20260924.md) and an explicit test of what its hypotheses do not establish.

## 1. Bare source existence does not distinguish smooth positive boundary weights

Keep the finite spatial link manifold, gauge action, and reference matrix fiber fixed. Let
\[
 d\nu_i=w_i\,dm,\qquad w_i\in C^\infty(M),\quad w_i>0,
 \quad\int_Mw_i\,dm=1,\qquad i=0,1,
\]
where each weight is gauge invariant. Define
\[
 \mathcal H_i=L^2_{\rm cov}(M,\nu_i;\operatorname{End}\mathbb C^N),
 \qquad
 \langle B,C\rangle_i=\int_M\frac1N\operatorname{tr}(B^\dagger C)w_i\,dm.
\]
Finite Wilson slabs on the same boundary graph supply such weights.

**Proposition 1 (weight transport).** The map
\[
 U_{01}B=\left(\frac{w_0}{w_1}\right)^{1/2}B
 \tag{1}
\]
is unitary from \(\mathcal H_0\) onto \(\mathcal H_1\). It preserves smooth covariance and intertwines every bounded covariant boundary multiplication operator:
\[
 U_{01}(AB)=A\,U_{01}B.
 \tag{2}
\]
For the weighted elliptic source scales \(\mathcal K_{r,i}\) of the determination note, it is also a bounded isomorphism \(\mathcal K_{r,0}\to\mathcal K_{r,1}\) for each fixed \(r>0\).

Consequently, if \(J_0:\mathcal D^0\to\mathcal H_0\) realizes any given pairing and has local \(\mathcal K_{r,0}\) bounds, then \(J_1=U_{01}J_0\) realizes the same pairing and has local \(\mathcal K_{r,1}\) bounds. The constants in those regularity bounds may change. Pairing symmetries, separated-support identities, and bounds measured in \(\mathcal H_i\) are unchanged.

**Proof.** In the norm integral the factor \(w_0/w_1\) cancels \(w_1\). The inverse is multiplication by \((w_1/w_0)^{1/2}\). Both scalar functions are smooth and bounded with all derivatives on the compact manifold, and are gauge invariant. This proves unitarity, covariance, and (2).

The weighted elliptic graph norms are equivalent to the ordinary Sobolev \(H^r\) norms on the fixed compact manifold with finite-dimensional fiber. Multiplication by a smooth function is bounded on these spaces; the reciprocal gives the inverse bound. Restriction to the covariant subspaces preserves these statements. If \(\|J_0f\|_{\mathcal K_{r,0}}\le C_Ip_I(f)\), then
\[
 \|J_1f\|_{\mathcal K_{r,1}}
 \le \|U_{01}\|_{\mathcal K_{r,0}\to\mathcal K_{r,1}}C_Ip_I(f).
\]
Unitarity proves the remaining claims. \(\square\)

This proposition assumes neither RH nor existence of any arithmetic source. It is a conditional transport statement, not a proposed construction from a chosen zeta spectrum.

**What it does not preserve.** The distinguished state vector is generally changed:
\[
 U_{01}I=\left(\frac{w_0}{w_1}\right)^{1/2}I\ne I.
\]
Thus matrix elements against fixed boundary vectors, a source rule defined using the designated cyclic vector, or a specified electric/insertion operator need not be preserved. A fixed operator would generally need conjugation to transport its relations. Nor does multiplication by the weight ratio preserve an exact finite-word Wilson-loop algebra merely because it preserves its smooth completion.

The practical conclusion is precise: Hilbert-space membership, covariance, local regularity, and even boundary-multiplication intertwinings alone do not distinguish the chosen Wilson dynamics. A genuine-YM proposal needs an independently specified source law or relations tied to the designated state or operators. This requirement is compatible with leaving the induced arithmetic translation generator unnamed. The proposition does not exclude any such more structured proposal, or transfer to a continuum or infinite-volume state.

## 2. Make the countable source family explicit

Let \(T=-\partial_x^2+1/4\), \(\mathcal D=C_c^\infty(\mathbb R)\), and \(\mathcal D^0=T\mathcal D\). For a compact interval \(I\), write \(\mathcal D_I\) for the Fréchet space of smooth tests supported in \(I\).

For each nondegenerate compact interval with rational endpoints, choose a countable dense subset of \(\mathcal D_I\). Include the three chosen anchor profiles. Take the smallest \(\mathbb Q(i)\)-vector space \(\mathscr E\) containing these profiles and invariant under rational translations, reflection, and multiplication by \(e^{iqx}\) for every \(q\in\mathbb Q\). If a particular source law needs further countably many test operations, close under those too, provided they preserve \(\mathcal D\). Set
\[
 F=T\mathscr E.
 \tag{3}
\]
This is still countable. Since \(T:\mathcal D_I\to\mathcal D_I^0\) is an isomorphism, it has the fixed-support density required in Theorem 2 of the determination note.

On this family the following are genuinely countable finite-coordinate constraints:

- rational complex linearity of \(v_f\);
- translation and reflection invariance of the pairings, initially for rational shifts;
- the separated-support identity for profiles in disjoint rational-endpoint intervals;
- the three anchor equations;
- the uniform growth inequalities (G), for \(h\in\mathscr E\cap\mathcal D_I\) and rational \(q\) with \(|q|\ge1\).

Every test appearing in (G) is in \(F\), since \(q^{-2}\in\mathbb Q\) and \(e^{iqx}h\in\mathscr E\). Each displayed constraint is closed in finitely many strong Hilbert coordinates, with the predetermined bounds.

Continuity extends rational shifts and modulations to real ones. For disjoint compact supports, choose finite rational-interval covers whose intervals from opposite supports remain disjoint. A partition of unity decomposes the profiles into finitely many pieces in those intervals. Density and sesquilinearity then extend the identity to the original pair. The decomposition is performed on \(h,k\), and the source tests are \(Th,Tk\); multiplication by an arbitrary partition of unity on \(f\in\mathcal D^0\) would not preserve its two moment constraints.

This fills in the construction already suggested after Theorem 2. It supplies no finite-feasibility result. Density on one nested exhaustion alone is insufficient to justify all of these support-constrained and modulated tests without this enlargement.

## 3. Uniform growth follows from full pointwise growth for a continuous source map

**Proposition 2.** Fix a compact interval \(I\) and a continuous linear \(J:\mathcal D^0\to\mathcal H\). If
\[
 \|J[\lambda^{-2}T(e^{i\lambda x}h)]\|^2
 =O_h(\log(2+|\lambda|))
 \tag{4}
\]
for every \(h\in\mathcal D_I\), then some continuous seminorm \(q_I\) and constant \(D_I\) satisfy (G) for all such profiles and every real \(|\lambda|\ge1\).

**Proof.** Consider the continuous linear operators
\[
 A_\lambda h=
 \frac{J[\lambda^{-2}T(e^{i\lambda x}h)]}
 {\sqrt{\log(2+|\lambda|)}}.
\]
For each fixed \(h\), (4) bounds their values at large \(|\lambda|\). Continuity in \(\lambda\) bounds their values on every remaining compact parameter interval. The family is therefore pointwise bounded on the Fréchet, hence barrelled, space \(\mathcal D_I\). The uniform boundedness principle makes it equicontinuous. This gives \(\|A_\lambda h\|\le C_Iq_I(h)\); squaring proves the claim. \(\square\)

This does not rescue growth known only on a dense list: pointwise bounds on that list do not imply pointwise boundedness on all of \(\mathcal D_I\). Nor does it manufacture the common constants required in advance for a finite-feasibility proof. It explains that (G) is a useful closed way to formulate the growth condition, without introducing a stronger final property of an already continuous Hilbert-valued source satisfying (4) everywhere.

## 4. The limiting observable domain must be chosen

Theorem 2 combined with Lemma 3 gives \(Jf\in H^r_{\rm cov}(M,\nu)\) for one declared \(r>0\). It does not give a smooth or bounded matrix function in general. If \(d=\dim M\), taking \(r>d/2\) is a sufficient Sobolev condition for bounded continuous representatives. Smoothness requires control through all Sobolev orders, or some other smoothing hypothesis; smooth spectral truncations alone do not ensure a smooth limit.

For the reflected \(L^2\) completion this is harmless: Cauchy-Schwarz makes the pairing of two sources well-defined, and bounded boundary multiplication acts continuously. If the next problem instead requires bounded observables, finite loop polynomials, arbitrary products of sources, or unbounded insertions, it must state and preserve the corresponding domain. These are different source specifications.

Verification: the transport identity was checked directly in the weighted norm; the countable-family construction and the uniform boundedness argument were checked from their hypotheses. These controls do not establish source occurrence, arbitrary finite arithmetic feasibility, or the mixed YM identity.

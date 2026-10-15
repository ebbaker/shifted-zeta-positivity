# Comparison and relevance of the quaternion forms drafts

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**, verified from current-session metadata. This is an internal LLM assessment, including three independently prompted checks of version differences, signed-structure relevance, and the nonabelian boundary claim. It is not external specialist review or formal verification.

The older work is useful for preserving oriented bilinear pairings through a boundary representation. Neither draft establishes the theta-specific signed bound left open in [Note 49](../notes/00_research_coordination/49_OCTONIONIC_SIGNED_BOUND_ANALYTIC_CONTINUATION_20261015.md). [Note 50](../notes/04_octonionic_reductions/50_QUATERNION_FORMS_HODGE_PAIRING_AND_SOURCE_TARGET_20261015.md) extracts a directly proved closed self-dual lift, without relying on the drafts' unfinished kernel arguments.

The author clarified on 15 October 2026 that these were unpublished working notes, circulated to colleagues with mistakes and incompleteness acknowledged. The review treats them as exploratory research material; it does not imply they were submitted as finalized publication claims.

## 1. Which version is which

Both title pages name **Edward B. Baker III**, University of Maryland, College Park. Title-page dates agree with the PDF creation metadata. The filenames do not indicate chronological order.

| Property | QuaternionForms-Final2.pdf | QuaternionForms-Final.pdf |
| --- | --- | --- |
| Date and length | 21 January 2014, 12 pages | 14 February 2014, 14 pages |
| Title ending | Applications to SU(2) Yang-Mills theory | Applications to Yang-Mills theory |
| Common foundation | Complex integral formulas; quaternion differentials and forms; self-dual and anti-self-dual kernels | Substantially the same foundation, with some corrections |
| Distinct Section 5 | Modified integral kernel, quaternionic primitive, branch ray and keyhole terms, pp. 7–8 | Proposed extension to classical Euclidean Yang–Mills fields using trace and exchange symmetry, pp. 7–9 |
| Visible incompleteness | CHECK SIGNS on p. 8; unresolved references and unfinished Appendix C, p. 11 | Appendix D, p. 12, leaves the announced cancellation derivation incomplete |

The January draft introduces \(\widetilde K=K+K^{\pm}+K^{\mp}\) to cancel mixed Hodge terms away from a singular ray. It retains cylinder, sphere and cut-boundary contributions and an orientation-reversing operator. The February draft removes this development and replaces it with a different argument. Its p. 7 footnote 4 says the primitive-based approach was omitted because it yielded a local instanton-number expression rather than the desired Lagrangian. These are distinct research routes worth preserving.

A substantive correction occurs in the complex kernel: January pp. 2–3 assign noncomplementary types \((n-1,0)_z\otimes(0,n-1)_w\), with \(dz\otimes d\bar w\) factors. Wedging these with the stated top holomorphic and antiholomorphic forms gives zero for \(n>1\). February p. 3 changes them to the complementary types \((0,n-1)_z\otimes(n-1,0)_w\) and \(d\bar z\otimes dw\). This fixes that mismatch, although the subsequent distributional formulas still need a separate audit before use.

Section 3 and Appendix A are largely unchanged. Section 4 contains the same core structure; the closed self-dual pairing becomes equation (4.10) in February and the next formula shifts to (4.11). Appendix B has some rearranged identities; Appendix C is different because it supports a different Section 5. February has 22 bibliography entries versus January's 15.

## 2. What can be used for Investigation 21

The robust idea is the separation of a signed wedge pairing from a positive Hodge pairing. For real forms,
\[
\Omega\wedge\Omega=(|\Omega_+|^2-|\Omega_-|^2)\,\mathrm{vol},
\qquad
\Omega\wedge*\Omega=(|\Omega_+|^2+|\Omega_-|^2)\,\mathrm{vol}.
\]
Quaternion conjugation and the conjugate Hodge star must additionally be tracked in the drafts' formulas. In particular, equation (4.11)'s \(F\wedge\bar F\) versus its boundary conjugate-Hodge factor is not automatically a typographical error: orientation reversal changes the bulk/boundary sign, and this arrangement can represent a signed pairing rather than the energy. A minus sign between two boundary wedge sectors also need not imply an indefinite energy.

Note 50 proves, for \(\alpha_f=\operatorname{Re}(f(z)dz\wedge dw)/\sqrt2\), that the forms are closed and self-dual and
\[
\alpha_f\wedge\alpha_g=\operatorname{Re}(f\bar g)\,\mathrm{vol}.
\]
Its signed combination realizes \(h_{j+1}^2-h_jh_{j+2}\) on the physical real slice. Pairing the full constant physical factor \(h_j(t,x)\) with the circle field realizes Note 46's exact current \(\phi_j\). This is a precise bridge from the author's earlier ideas to the current investigation.

The bilinear pairing must survive the reconstruction. Positive norms of its pieces contain uncontrolled higher derivatives. Closedness alone does not exclude the exact backward-heat quadratic and cubic collision controls. Thus this bridge does not improve the proved pointwise domain or provide the missing locally bounded energy-relative coefficient.

The January draft is especially useful as a warning about residual terms: canceling the mixed kernel away from the ray does not cancel a ray-supported distribution or establish its sign. Its incomplete ray calculation must not be silently treated as a theorem.

## 3. The February nonabelian extension fails as stated

The proposed general Yang–Mills boundary identity in February equation (1.1), pp. 2 and 9, uses a scalar spatial kernel with a factor \(\operatorname{Tr}(F(p)F(q))\). Under local gauge transformations \(F(p)\mapsto g(p)F(p)g(p)^{-1}\), conjugations at distinct points do not cancel inside this trace. The bulk action and the field equations are gauge invariant. A bilocal covariant comparison ordinarily needs parallel transport; see, for example, [Scheihing-Hitschfeld and Yao on field-strength correlators](https://arxiv.org/abs/2205.04477). Adding transport also changes the differentiated kernel and requires a new proof.

There is a direct counterexample among smooth self-dual solutions. On the unit ball in \(\mathbb R^4\), put
\[
\omega=dx_0\wedge dx_1+dx_2\wedge dx_3,
\quad
A_0=\frac{\mathbf i}{2}(x_0dx_1-x_1dx_0+x_2dx_3-x_3dx_2).
\]
Then \(F_0=\mathbf i\omega\) is self-dual and satisfies the Yang–Mills equation. Gauge-transform with \(g_\lambda(x)=\exp(\mathbf j\lambda x_0/2)\), using \(F_\lambda=g_\lambda F_0g_\lambda^{-1}\). In the standard two-dimensional complex representation of the quaternions, the bulk expression is constantly \(-2\pi^2\). The positive-action convention would reverse this overall trace sign and leaves the contradiction unchanged.

For the printed kernel \(K(p,q)=\sum_\mu dp_\mu\otimes dq_\mu/|p-q|^2\), its claimed boundary expression is \(-Q(\lambda)/\pi^2\), where
\[
Q(\lambda)=\iint_{S^3\times S^3}
\frac{p\cdot q}{|p-q|^2}\cos\{\lambda(p_0-q_0)\}\,dS_p\,dS_q.
\]
The pullbacks of \(\omega\wedge dx_\mu\) have coefficient vector equal to an orthogonal transform of the unit normal, so their contraction is \(p\cdot q\). The trace of the rotated quaternion coefficients is \(-2\cos\{\lambda(p_0-q_0)\}\).

Here is an exact check of the first nonconstant term. Write \(s=p\cdot q\) and \(W=s/[2(1-s)]\). Conditional rotation averages give
\[
\mathbb E[(p_0-q_0)^2\mid s]=(1-s)/2,
\qquad
\mathbb E[(p_0-q_0)^4\mid s]=(1-s)^2/2.
\]
For independent uniform points of \(S^3\), \(\mathbb E s=0\), \(\mathbb E s^2=1/4\), and \(\mathbb E(1-s)^{-1}=2\). Since \(|S^3|=2\pi^2\), this yields
\[
\iint W=2\pi^4,\qquad
\iint W(p_0-q_0)^2=0,\qquad
\iint W(p_0-q_0)^4=-\pi^4/4.
\]
The \(|p-q|^{-2}\) singularity is integrable on this three-dimensional boundary. Taylor expansion therefore gives
\[
Q(\lambda)=2\pi^4-\frac{\pi^4}{96}\lambda^4+O(\lambda^6),
\]
and the proposed boundary value is
\[
-2\pi^2+\frac{\pi^2}{96}\lambda^4+O(\lambda^6),
\]
contradicting the unchanged bulk value. This counterexample does not invalidate the ordinary closed-form algebra or establish that every version of a covariant boundary formula is impossible. It rules out the advertised formula with this scalar kernel for general Yang–Mills fields.

## 4. Additional checks before reviving a kernel theorem

Both drafts' Section 2 print \(K=\pi\log|z_1-z_2|\), whereas their equation (2.2) requires a \(\bar\partial\) derivative twice that obtained with the printed Appendix A conventions. The original integral defining \(K\) also depends on the domain; solving one distributional equation does not remove the domain and boundary terms. These formulas need reconstruction with consistent constants and boundary prescriptions. The present bridge uses direct exterior algebra and Stokes' theorem instead.

The internal audit checked the closed lift, the coefficient-space eigenvalues \(1,1/2,-1/2\), its Stokes primitive, the physical-circle coefficient, and both polynomial predecessor controls analytically. The gauge counterexample was independently derived and its spherical moments checked. No numerical pilot is presented as mathematical evidence. The earlier drafts as a whole are not certified by this limited review.

## 5. Source identities and repository state

The PDFs were read from the author's supplied locations. Their relevant formulas and unfinished sections were also inspected in rendered pages. The source documents were not copied, edited, or renamed; the author intends to add them manually to the source document folder.

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| QuaternionForms-Final.pdf | 283483 | `5125461583b33e843f5e507b63577c7e6e0d801b8d1c64b34b7799bdcdc75920` |
| QuaternionForms-Final2.pdf | 281291 | `5d830e71f0a8641b25ce4b780a818734aa0105192724cc8e570259f085e1c2e6` |

Supplied locations: `/Users/ebbaker/Desktop/Research/quaternions/QuaternionForms-Final.pdf` and `/Users/ebbaker/Library/Mobile Documents/com~apple~CloudDocs/Desktop/Research/AAO-Nanotube/QuaternionForms-Final2.pdf`. These are provenance, not runtime lookup rules. Hashes identify the exact reviewed files and do not validate their claims.

The new research note and this review continue working-tree commit `eab83373d6e45ad15e343257597155158e8ba53d`. No manuscript, existing theorem, finite certificate, or source document was changed. This chat is registered in place as formal-replay history **16**, **Review octonionic signed-bound ideas**, thread `01a13e3b-8590-7352-8e09-ba07a7342c16`; the live registry supplies current capture metadata. Native completion-hook activation is unverified, so the authorized bounded exact-turn follow-up remains in use.

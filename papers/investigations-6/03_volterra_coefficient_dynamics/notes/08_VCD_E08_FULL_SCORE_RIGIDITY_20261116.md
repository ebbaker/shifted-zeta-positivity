# VCD-E08 r1 — Full canonical-score rigidity and the finite cut

16 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Tool dispatch **gpt-6.1-sol / ultra**.
Separate runtime model and effort attestation unavailable.

**Proved in-note, internal analytical work.** This proves the
[frozen theorem bundle](../research-progress/handoffs/VCD-E08-r1.md)
selected in the [B03 decision](../brainstorm/notes/05_VCD_B03_FULL_SCORE_AND_TAIL_DEFECT_DECISION_20261116.md).
All five frozen hashes match. The result identifies the source from
all canonical adjacent equalities and specifies the defect seen by a
finite commutator. It leaves the Fourier-zero problem open.

Use the unchanged complete \(W_\lambda=e^{\lambda u^2}\Phi\),
\(Z_\lambda=\int W_\lambda\), \(\mu_\lambda=W_\lambda\,du/Z_\lambda\),
\(V=-\log W_\lambda\), and \(H_\lambda(z)=\tfrac12\int W_\lambda e^{izu}\,du\).
Fix \(\lambda\in[0,1/2]\); \(\lambda=0\) is the primary case.
The [manuscript](../manuscript/main.tex) gives the smooth, strictly
positive, even \(W_\lambda\), so \(V'\) is odd. The
[E05 score bound](05_VCD_E05_SOURCE_SCORE_RESIDUAL_20261116.md#1-canonical-score-normalization-and-operator-domain)
gives \(|V'(u)|=O(e^{4|u|}+|u|)\) in the stated band. The canonical
measure satisfies every weighted exponential integrability condition
below by the manuscript's double-exponential tail bound.

## 1. Exact conversion and rigidity

Let \(\nu\) be an even probability measure of infinite support on
\(\mathbb R\) with
\[
 \int e^{R|u|}(1+|V'(u)|)\,d\nu(u)<\infty \qquad (R>0).
\]
Write \(q_j\) for its orthonormal polynomials with positive leading
coefficients \(\kappa_j\). All polynomial Gram matrices are positive
definite, since a nonzero polynomial cannot vanish on the infinite
support. By evenness \(q_j\) has parity \(j\), and the Jacobi recurrence
is \(u q_j=a_{j+1}q_{j+1}+a_jq_{j-1}\) with \(a_0=0\),
\(a_j=\kappa_{j-1}/\kappa_j>0\) for \(j\ge1\).
The link \(a_j\) joins sites \(j-1,j\).

Define the linear functional and the two defect sequences by
\[
 \mathcal D_\nu(f)=\int(V'f-f')\,d\nu,\qquad
 s_k=\mathcal D_\nu(u^k),\qquad
 e_n=a_n\int V' q_nq_{n-1}\,d\nu-n .
\]
For \(k=0\) the derivative term is zero. For each \(n\ge1\),
\(q'_{n-1}\) is orthogonal to \(q_n\), while
\(q'_n-(n/a_n)q_{n-1}\) has degree at most \(n-2\).
Consequently \(\int(q_nq_{n-1})'\,d\nu=n/a_n\) and
\(e_n=a_n\mathcal D_\nu(q_nq_{n-1})\).
The products \(q_nq_{n-1}\) have degrees \(2n-1\) and are odd.
Writing their lower odd coefficients after multiplication by \(a_n\)
as \(c_{n,r}\) gives
\[
  e_n=\kappa_{n-1}^{\,2}s_{2n-1}
         +\sum_{r=1}^{n-1}c_{n,r}s_{2r-1}. \tag{1}
\]
The leading coefficient is \(a_n\kappa_n\kappa_{n-1}=\kappa_{n-1}^{\,2}>0\).
The functional vanishes on even polynomials by parity. For any \(N\ge1\),
vanishing of \(e_1,\ldots,e_N\) is therefore equivalent to vanishing on
odd tests of degree at most \(2N-1\), or on all polynomial tests through
degree \(2N\). The next row adds the test \(u^{2N+1}\) modulo the earlier
tests, with coefficient \(\kappa_N^2\). This is an exact triangular map
at each finite degree. It supplies no bound on conditioning as \(N\)
increases.

Suppose all \(e_n=0\). Equation (1) and parity give
\(\mathcal D_\nu(p)=0\) for every polynomial \(p\).
For each real \(t\), expand \(e^{itu}\) in \(u\) and differentiate its
polynomial partial sums in \(u\). The partial sums and derivatives
are bounded in modulus by \(e^{|t||u|}\) and \(|t|e^{|t||u|}\),
respectively. The hypothesis thus gives
\[
 \int V'(u)e^{itu}\,d\nu(u)=it\int e^{itu}\,d\nu(u).
\]
For a compactly supported smooth test \(\varphi\), Fourier inversion
with \(\widehat\varphi(t)=\int\varphi(u)e^{-itu}\,du\) represents
\(\varphi,\varphi'\) using \(\widehat\varphi,it\widehat\varphi\).
Both Fourier weights are integrable by repeated integration by parts.
Fubini against \(\nu\) and the finite signed measure \(V'\nu\) gives
\(\int\varphi'\,d\nu=\int V'\varphi\,d\nu\).
Thus \(\nu'=-V'\nu\) in distributions.

This step treats \(\nu\) as a measure throughout. Inserting
\(e^V\varphi\), a smooth compactly supported test, in the last
identity and canceling the \(V'\)-terms gives
\(\int \varphi' e^V\,d\nu=0\).
The locally finite measure \(e^V\nu\) has zero distributional derivative.
Every compactly supported smooth test with Lebesgue integral zero
has a compactly supported smooth primitive, so this measure annihilates
all such tests. Subtracting a fixed test of integral one times
\(\int\varphi\,du\) shows \(e^V\nu=c\,du\) on all smooth compactly
supported tests, hence as measures. Since \(e^{-V}=W_\lambda\) and
\(\nu\) is a probability, \(c=1/Z_\lambda\) and \(\nu=\mu_\lambda\).
Conversely, the canonical integration by parts in [E05 §1](05_VCD_E05_SOURCE_SCORE_RESIDUAL_20261116.md#1-canonical-score-normalization-and-operator-domain)
gives all the adjacent equalities for \(\mu_\lambda\). The all-degree
equations therefore characterize the canonical source in the stated
class.

## 2. Entrywise commutation and the cut

For any measure in §1, define the defect matrix
\[
 E_{ij}=\mathcal D_\nu(q_iq_j),\qquad
 a_n E_{n,n-1}=e_n. \tag{2}
\]
It is real symmetric and vanishes when \(i+j\) is even. The sums in
\((JE)_{ij}\) and \((EJ)_{ij}\) are finite by tridiagonality.
The recurrence and linearity put both entries equal to
\(\mathcal D_\nu(u q_iq_j)\). Thus \([J,E]=0\) entrywise, with the
convention \([J,E]=JE-EJ\). This polynomial argument works throughout
the measure class and avoids products of unbounded operators.

Let \(H=\{0,\ldots,N-1\}\), \(J_N=J_{H,H}\), \(E_N=E_{H,H}\), and
\(\mathbf e_{N-1}\) be the last coordinate vector of the head. Then
\[
 [J_N,E_N]
 =-a_N\mathbf e_{N-1} E_{N,H}
       +a_N E_{H,N}\mathbf e_{N-1}^{\mathsf T}. \tag{3}
\]
Indeed, \((JE)_{H,H}\) equals \(J_NE_N\) plus
\(a_N\mathbf e_{N-1}E_{N,H}\), while \((EJ)_{H,H}\) equals \(E_NJ_N\)
plus \(a_N E_{H,N}\mathbf e_{N-1}^{\mathsf T}\). Their equality yields
the opposite signs on the right of (3). The correction has rank at
most two and is skew-symmetric. The shared endpoint entry
\(E_{N,N-1}=E_{N-1,N}\) cancels between the two terms. In particular,
for \(N=1\) the commutator is zero regardless of \(e_1\).

The exact data at a cut can be specified further. For \(N\ge2\),
\(E_N\) and the retained polynomials determine all odd Stein defects
through \(2N-3\) by applying (1) to the retained adjacent entries.
For \(i\le N-2\), any odd product \(q_iq_N\) has degree at most
\(2N-3\); the highest possible index \(i=N-2\) gives an even product.
The weighted values \(a_N E_{i,N}\) at these indices are determined
by the head data even without a supplied \(a_N\), since
\[
 a_N q_N=u q_{N-1}-a_{N-1}q_{N-2}.
\]
Thus the projected cross-cut column \(a_N E_{H,N}\) in (3), with
its last component removed, uses lower tests. The remaining boundary
component \(a_N E_{N-1,N}=e_N\) is the new adjacent defect of odd
degree \(2N-1\), and (3) is insensitive to it. In particular
\(E_N=0\) is equivalent to \(e_1=\cdots=e_{N-1}=0\). Under those
equalities, the new cut row and column vanish away from their last
retained component, and \([J_N,E_N]=0\) supplies no equation for \(e_N\).
This distinguishes the missing next canonical test from the already
determined portion of the cut correction. The next link \(a_N\) is
also needed to recover unweighted \(q_N\) and row entries.

For the multiplication interpretation, suppose additionally that
\(\nu=w\,du\) with \(w>0\) locally absolutely continuous and
own score \(V_\nu'=-w'/w\) almost everywhere. For every integer
\(m\ge0\), assume \((1+|u|)^m w(u)\to0\) at both ends and
\((1+|u|)^m|w'|\) integrable. These hypotheses justify own-score
integration by parts for the polynomial tests in (2). Thus
\(E_{ij}=\int b\,q_iq_j\,d\nu\), with \(b=V'-V_\nu'\).
If \(b\in L^\infty(\nu)\), the quadratic form of \(E_N\) on \(c\) is
\(\int b\,|\sum_{j<N}c_jq_j|^2\,d\nu\). Orthogonality gives
\(\|E_N\|\le\|b\|_\infty\), and
\(|e_n|\le a_n\|b\|_\infty\) by Cauchy–Schwarz. Neither (1) nor
(3) controls the next test or supplies a signed Fourier margin
from this absolute score estimate.

## 3. Classification and control scope

This is source identification and finite defect accounting under
[avoid 01](../../../../avoid/01_restating_the_target.md). Full
canonical consistency is the unconditional identifying condition.
Finite consistency leaves unpaid adjacent tests, and commutation
itself holds throughout the measure class of §1. The [result index](../../../../result-summaries/README.md),
[coefficient cluster](../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md),
[avoid index](../../../../avoid/README.md),
[control-premise pattern](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
and [scoped-exclusion pattern](../../../../avoid/07_scoped_exclusions_read_as_universal.md)
govern interpretation.

The [collision catalog](../../../../result-summaries/12_collision_controls_and_screening.md)
and the [E05 control screen](05_VCD_E05_SOURCE_SCORE_RESIDUAL_20261116.md#5-control-screen)
distinguish own-score identities from the canonical equalities.
Euler translates change the canonical summand score. Weighted-square
and finite-prime controls lack full canonical reflection. The reflected
super-Gaussian has different tail confinement. Smooth shape and
primitive controls lack the canonical square-summand formula.
For any such distinct measure satisfying the stated exponential
integrability, §1 forces failure of at least one exact canonical
adjacent test, without locating the failed index. The finite-atom
controls fail the infinite-support premise. Their compact continuous
extensions, when even and of infinite support, have the required
integrability but fail some full-source equality by §1. The
RH-conditional endpoint controls change the source and lack ordinary
Dirichlet arithmetic. The fixed-amplitude varied-observation controls
preserve the source identities and fail the literal Fourier readout.
The actual-profile relaxation supplies no corresponding full physical
source and readout.

The finite theta-mode controls returned to
[B03](../brainstorm/notes/05_VCD_B03_FULL_SCORE_AND_TAIL_DEFECT_DECISION_20261116.md)
under [E07 r1](../research-progress/handoffs/VCD-E07-r1.md) give the
stronger comparison at \(\lambda=0\): any specified finite coefficient
prefix and canonical-score entries can agree exactly, and the distinct
source can have arbitrarily small bounded \(b\) while having nonreal
Fourier zeros. The statements concern each finite constraint list
and a perturbation chosen for it. Such a nonzero perturbation must
fail an additional exact adjacent identity by §1. No collision
certificate was rerun. These controls delimit the finite-information
inference without excluding a future propagation lemma using the full
canonical source.

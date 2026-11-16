# Smooth perturbations with a free next canonical score defect

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance. Recorded tool dispatch **gpt-6.1-sol /
ultra**. Separate runtime configuration or backend attestation unavailable.
Fixed analytical task [VCD-E10 r1](../research-progress/handoffs/VCD-E10-r1.md),
from the [second B03 decision](../brainstorm/notes/06_VCD_B03_SMOOTH_NEXT_DEFECT_DECISION_20261116.md).

**Status: proved in-note, internal analytical work.** This is a scoped
obstruction to an exact forward step from a finite coefficient head,
lower canonical adjacent defects and the stated source regularity.
The [result index](../../../../result-summaries/README.md),
[control catalog](../../../../result-summaries/12_collision_controls_and_screening.md),
[avoid index](../../../../avoid/README.md) and patterns
[01](../../../../avoid/01_restating_the_target.md),
[02](../../../../avoid/02_shape_only_arguments_and_the_controls.md) and
[07](../../../../avoid/07_scoped_exclusions_read_as_universal.md) govern
its use.

## 1. The next measurement is independent

Fix \(\lambda=0\), \(N\ge1\), and the canonical time-zero source
\(\Phi\). Put \(Z=\int_{\mathbb R}\Phi(u)\,du\),
\(d\mu=\Phi\,du/Z\), and \(V=-\log\Phi\).
The positive even source and its tails are those of the
[manuscript](../manuscript/main.tex). Use the probability-orthonormal
polynomials \(q_j\) with positive leading coefficient, and the link
\(a_j\) joining sites \(j-1,j\). They have parity \(j\), and
\[
 a_j\int V' q_jq_{j-1}\,d\mu=j
\]
by [E05 §1](05_VCD_E05_SOURCE_SCORE_RESIDUAL_20261116.md).
[E06 §2](06_VCD_E06_EXPONENTIAL_SCORE_RESIDUAL_20261116.md)
gives \(V'(u)=8\pi\sinh(4u)+b(u)\) with \(b\) bounded, and thus
\(V'(u)\sim4\pi e^{4u}\) as \(u\to+\infty\).

On the real vector space \(X=C_c^\infty(0,\infty)\), extend each
test evenly as \(h(u)=g(|u|)\) for \(g\in X\).
Each extension is smooth because \(g\) vanishes near zero. The
constraints and target are the linear functionals
\[
 M_k(h)=\int_{\mathbb R}u^{2k}h\,d\mu \quad (0\le k\le N),
 \qquad
 L_j(h)=\int_{\mathbb R}V' q_jq_{j-1}h\,d\mu \quad(1\le j\le N).
\]
Both test symbols are even, so each of these integrals is twice its
positive-half-line counterpart. Suppose \(L_N\) belonged to the real span
of \(M_0,\ldots,M_N,L_1,\ldots,L_{N-1}\). The corresponding identity
against every \(g\in X\) would give
\[
 V'(u)Q(u)=P(u)\qquad(u>0),
\]
where \(P\) is even of degree at most \(2N\) and
\(Q=q_Nq_{N-1}-\sum_{j<N}c_j q_jq_{j-1}\) is odd with degree \(2N-1\)
and nonzero leading coefficient. Indeed, a continuous difference
that is nonzero at a positive point has fixed nonzero sign on
some interval. A nonnegative bump supported on that interval tests
it nontrivially since the density of \(\mu\) is strictly positive.
The displayed equality contradicts the exponential growth of \(V'\)
multiplied by \(Q\) at positive infinity. Thus \(L_N\) is independent
of the constraint functionals.

Let \(A:X\to\mathbb R^{2N}\) collect those constraints.
If \(L_N\) vanished on \(\ker A\), the rule \(Ax\mapsto L_N(x)\)
would be well defined and linear on \(\operatorname{ran}A\).
Extending it to the full finite-dimensional codomain by a basis
would express \(L_N\) as a linear combination of the rows of \(A\),
contrary to independence. Therefore some even extension \(h\) obeys
\[
 M_0(h)=\cdots=M_N(h)=0,\qquad
 L_1(h)=\cdots=L_{N-1}(h)=0,\qquad L_N(h)\ne0 .
 \tag{1}
\]
This includes \(N=1\), when the list of lower score constraints is
empty. The test direction \(h\ne0\) is now fixed for this \(N\).

## 2. Exact preservation, free defect and score tolerance

For \(0<|\epsilon|\,\|h\|_\infty<1/2\), define
\(\Psi_\epsilon=(1+\epsilon h)\Phi\) and
\(d\nu_\epsilon=(1+\epsilon h)\,d\mu\).
The density is strictly positive, even and smooth. By \(M_0(h)=0\),
it has mass one as a probability and \(\int\Psi_\epsilon=Z\).
The unnormalized source equals \(\Phi\) near zero and outside a
compact set. Every derivative at the reflection endpoint and the
two real source tails therefore agree exactly.

All moments through degree \(2N\) agree by (1) and evenness. They
determine the Gram matrix of monomials of degrees \(0,\ldots,N\).
The common positive definite matrix determines the same \(q_j\) for
\(j\le N\) by orthonormalization with positive leading coefficient.
If \(\kappa_j\) is this leading coefficient, each common link
is \(a_j=\kappa_{j-1}/\kappa_j\) for \(1\le j\le N\).
Define the canonical adjacent defects for \(\nu_\epsilon\) by
\[
 e_j=a_j\int V' q_jq_{j-1}\,d\nu_\epsilon-j\qquad(1\le j\le N).
\]
These use the same theta symbol \(V'\) and the now common links
and polynomials. Subtracting the canonical time-zero identity gives
\[
 e_j=\epsilon a_j L_j(h).
 \tag{2}
\]
Thus \(e_j=0\) for \(j<N\) and \(e_N\ne0\). The signs of \(\epsilon\)
give both signs of \(e_N\) with the same prescribed data.

The own score of \(\Psi_\epsilon\) is
\(V_{\Psi_\epsilon}'=V'-\epsilon h'/(1+\epsilon h)\).
Consequently
\[
 \|V_{\Psi_\epsilon}'-V'\|_\infty\le2|\epsilon|\|h'\|_\infty.
 \tag{3}
\]
Any positive score tolerance can be met with \(\epsilon\ne0\).
The same comparison holds if both sources are tilted by the same
\(e^{\lambda u^2}\), since the tilt adds the same term to both
scores. The exact moment and defect conditions here are at time zero.

The inherited envelope also survives this construction uniformly
for \(0\le\lambda\le1/2\). Let \(t=|u|\). The
[manuscript's confinement proof](../manuscript/main.tex) gives
\(uV_\lambda'(u)\ge-27/4\) for \(t\le1/2\), where
\(\cosh(4t)<4\), and \(uV_\lambda'(u)\ge e^{4t}\) for \(t\ge1/2\).
The slack above \(\cosh(4u)-11\) is therefore at least \(1/4\)
on the first region and \(11+\sinh(4t)\) on the second.
Choose \(|\epsilon|\) also so that \(2|\epsilon|\|u h'\|_\infty<1/4\).
Equation (3) pointwise with the factor \(u\) then gives
\[
 uV_{\Psi_\epsilon,\lambda}'(u)\ge\cosh(4u)-11 .
\]
The perturbed tilted weight satisfies the manuscript's integrability
and boundary hypotheses because it coincides with the canonical
weight outside a compact set. The same confinement lemma yields
\[
 \beta_{\Psi_\epsilon,j}(\lambda)+\beta_{\Psi_\epsilon,j+1}(\lambda)
    \le\frac{\operatorname{arcosh}^2(2j+12)}{16}\qquad(j\ge0).
\]
Meeting the extra smallness condition leaves both choices of sign
in (2).

The preservation of the real tails cannot be realized by a changed
sequence of constant square coefficients with the same mode functions
and absolute convergence at a positive \(u_0\). To see this, suppose
on \(u>0\) that
\(\Psi_\epsilon=\sum_{m\ge1}b_m s_m\), with the manuscript's \(s_m\),
and let \(k\) be the least index with \(b_k\ne1\).
At \(u\ge u_0\), write \(\rho(u)=\pi e^{4u}\). The positive mode
ratios for \(m>k\) satisfy
\[
 \frac{s_m(u)}{s_k(u)}
  =\frac{2m^4-3m^2/\rho(u)}{2k^4-3k^2/\rho(u)}
       e^{-(m^2-k^2)\rho(u)}
  \le4\frac{s_m(u_0)}{s_k(u_0)} .
\]
Here each numerator or denominator \(2j^4-3j^2/\rho\) lies between
\(j^4\) and \(2j^4\), and \(\rho(u)\ge\rho(u_0)\). Moreover the ratio
for each \(m>k\) tends to zero as \(u\to+\infty\). Absolute convergence
at \(u_0\) gives a summable majorant for the difference of the two
series divided by \(s_k\). Its limit is \(b_k-1\ne0\), whereas
\(\Psi_\epsilon-\Phi\) vanishes on the tail. If every \(b_m=1\),
the series gives \(\Phi\) everywhere and contradicts \(\epsilon h\ne0\).
This rules out that square-source description, including a positive
constant-coefficient series with pointwise convergence on the half-line.

## 3. Compatibility with the finite commutator

For the perturbed measure write
\(\mathcal D(f)=\int(V'f-f')\,d\nu_\epsilon\) for real polynomials,
and \(E_{ij}=\mathcal D(q_iq_j)\) in its orthonormal basis.
The source tails and compact modification justify these integrals,
and parity makes \(\mathcal D\) vanish on even polynomials.
For each \(j\), using the perturbed basis and links, integration of
the polynomial derivative gives
\(\int(q_jq_{j-1})'\,d\nu_\epsilon=j/a_j\) by orthogonality and
the leading coefficients. For \(j\le N\), this gives
\(a_j E_{j,j-1}=e_j\).
The odd polynomials \(q_jq_{j-1}\) for \(1\le j<N\) have successive
degrees \(1,3,\ldots,2N-3\) and nonzero leading coefficients. Hence
(2) forces \(\mathcal D\) to vanish on every polynomial of degree
at most \(2N-2\). This includes the constant when \(N=1\).

Let \(H=\{0,\ldots,N-1\}\), with \(J_N=J_{H,H}\) for the
perturbed Jacobi matrix, and let \(\mathbf e_{N-1}\) be the last
coordinate in this space. The polynomial recurrence gives
\((JE)_{ij}=\mathcal D(u q_iq_j)=(EJ)_{ij}\) entrywise, since only
the two adjacent links occur in either sum. Taking the finite block,
\[
 [J_N,E_{H,H}]
   =-a_N\mathbf e_{N-1}E_{N,H}
     +a_N E_{H,N}\mathbf e_{N-1}^{\mathsf T}. \tag{4}
\]
The degree test makes \(E_{H,H}=0\) and
\(E_{N,i}=E_{i,N}=0\) for \(i\le N-2\).
The remaining entry \(E_{N,N-1}=E_{N-1,N}=e_N/a_N\)
contributes the same rank-one term with opposite signs on the
right of (4). Thus the finite commutator agrees for the perturbed
and canonical measures despite their unequal next defect. This
derives the cancellation used in the
[E08 finite-cut discussion](08_VCD_E08_FULL_SCORE_RIGIDITY_20261116.md)
directly for this construction.

The finite canonical score compression also agrees. For \(i,j<N\),
both measures satisfy
\(\int V'q_iq_j\,d\eta=\int(q_iq_j)'\,d\eta\) for
\(\eta=\mu,\nu_\epsilon\), and the matching moments give the same
derivative integral. The finite-node contribution \(V'(J_N)\) agrees
because \(J_N\) and \(V'\) are the same. Hence the data preserved
include the exact retained correction of E05.

## 4. Scope and control comparison

The construction preserves a positive smooth full-line density,
the entire reflection jet and real tails, moments through \(2N\),
the links through \(a_N\), lower canonical defects, and an arbitrarily
small own-to-canonical score difference. It also obeys the same
coefficient envelope throughout the time band. It changes the complete
source and fails the constant square-source premise above. It
therefore refutes the stated exact step from the preserved data
to vanishing of \(e_N\) in this smooth source class.

[E07](07_VCD_E07_FINITE_CANONICAL_SCORE_CONTROLS_20261116.md) keeps
positive square coefficients with only finitely many changes. Its
controls match selected finite data and have nonreal Fourier zeros
by the inherited theorem for that class, with a finite nonsmooth
odd endpoint order. The compact multiplier here preserves full
smoothness, and its Fourier zero locations are open. E07's
[control screen](07_VCD_E07_FINITE_CANONICAL_SCORE_CONTROLS_20261116.md#3-catalog-screen)
records the failed source premises for the other families. In
particular the reflected super-Gaussian fails tail agreement,
Euler-factor translates fail unnormalized mass and first-link agreement
at time zero,
atom and compact-support controls fail the positive full-line density
premise, and variable-observation controls fail the literal Fourier
readout. These distinct failures give no inference about the smooth
perturbations' zeros or a future quantitative update using canonical
arithmetic.

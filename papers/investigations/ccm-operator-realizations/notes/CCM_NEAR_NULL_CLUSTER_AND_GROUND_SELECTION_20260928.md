# Xi annihilators, low spectral clusters, and the missing ground selection

28 September 2026. Prepared for Edward Baker with LLM assistance. Model: GPT-6 (Codex); exact serving variant and configured effort not exposed to this agent. This is a new analytic sub-investigation, not an independent human proof audit. No numerical sweep was run for this analytic derivation.

## Result in brief

The Xi kernel is an unconditional annihilator of the full Weil form. So are its translates. This gives arbitrarily large finite families of approximate zero modes on growing compact intervals, with superexponentially small residuals. Under RH these force every fixed-index low even eigenvalue, and hence the first even gap, to collapse. Without RH the same approximate zero modes still exist, but the even ground energy is eventually bounded strictly below zero and its eigenvector becomes asymptotically orthogonal to the cutoff Xi kernel.

Thus a small residual is intrinsically unable to select the desired ground state. An explicit arithmetic family of even positive approximate zero modes also has an unbounded normalized second moment. These statements sharpen the ground-selection issue without claiming that the required relative residual/separation estimate is impossible.

## 1. Input and conventions

The local input is [round-5 audit](CCM_INFINITE_L_BOUNDED_AUDIT_20260926.md), especially (11)–(12), (18)–(20). It identifies the normalized ground transform and its half-second-moment trace, and requires a comparison with the actual even ground state.

The primary [CCM source](https://arxiv.org/html/2511.22755v1#S3) supplies the full polarized explicit formula; its [Section 7](https://arxiv.org/html/2511.22755v1#S7) identifies the Xi kernel. Its finite self-adjoint realization assumes a simple even ground state, and its [Section 8](https://arxiv.org/html/2511.22755v1#S8) leaves the arithmetic ground comparison open. Those facts are inputs; the deductions below are supplied here.

Work in centered logarithmic coordinates, with Fourier transform

\[
F_f(z)=\int_{\mathbb R}f(x)e^{-izx}\,dx.
\]

Let \(k\) be the real even Xi kernel with \(F_k(z)=\Xi(z)/4\). Its nonzero integral is \(\Xi(0)/4\). This literal-k scalar is corrected as explained in [round 7](CCM_BOUNDARY_SELECTION_AND_COMPLEMENT_20260928.md#2-a-scalar-normalization-correction); the normalized conclusions are unchanged. For \(x\ge0\), the explicit theta expression gives

\[
k(x)=e^{x/2}\sum_{n\ge1}h(ne^x),\qquad
h(u)=\frac\pi2u^2(2\pi u^2-3)e^{-\pi u^2}.
\]

Consequently \(k(x)>0\), and evenness gives positivity on the whole line. For \(j=0,1\) and every fixed \(0<c<\pi\),

\[
|k^{(j)}(x)|\le C_{c,j}\exp(-c e^{2|x|})
\quad\text{for sufficiently large }|x|.
\tag{1}
\]

The polynomial factors from differentiating the Gaussian series are absorbed by changing \(\pi\) to \(c\). Higher derivatives have analogous bounds.

Let \(\Gamma\) denote all zeros of Xi, with multiplicity. The polarized Weil formula is

\[
Q(f,g)=\sum_{\gamma\in\Gamma}
\overline{F_f(\bar\gamma)}F_g(\gamma).
\tag{2}
\]

For nonreal zeros this is not a sum of absolute squares. The functions used below have sufficient exponential decay and smoothness that the explicit formula and its prime side converge; no assertion about boundedness of the full form on ordinary whole-line \(L^2\) is made.

## 2. A weighted-space estimate that controls the cutoff rigorously

Fix \(a>1/2\), and define

\[
\|f\|_{X_a}=\|f\|_{H^1(\mathbb R)}+
\|e^{a|x|}f\|_2.
\]

The full prime/gamma/pole expression extends continuously as a bilinear form on \(X_a\). More specifically, if \(h\) is supported in \([-R,R]\), then

\[
|Q(t,h)|\le C_a e^{aR}\|t\|_{X_a}\|h\|_2.
\tag{3}
\]

Initially take smooth compact h; the right side then extends the pairing to all \(L^2([-R,R])\).

**Proof.** The gamma symbol in the local audit obeys \(-6<a_\Gamma(\tau)\le\tfrac12\log(1+\tau^2)\). Thus \(|a_\Gamma(\tau)|\le6+|\tau|\), and its multiplier maps \(H^1\) continuously to \(L^2\). This part is bounded by \(7\|t\|_{H^1}\|h\|_2\).

For a translation by \(u\ge0\), the inequality \(|x|+|x-u|\ge u\) gives

\[
|\langle f,T_u g\rangle|
\le e^{-au}\|e^{a|x|}f\|_2\|e^{a|x|}g\|_2.
\]

The sum of the two prime translations is therefore bounded by twice

\[
Z_a\|e^{a|x|}f\|_2\|e^{a|x|}g\|_2,
\qquad Z_a=\sum_{n\ge2}\frac{\Lambda(n)}{n^{a+1/2}}<\infty.
\]

Convergence follows already from \(\Lambda(n)\le\log n\). The two pole functionals are bounded on the weighted space, since \(\int e^{|x|/2}|f(x)|dx\le(a-1/2)^{-1/2}\|e^{a|x|}f\|_2\). Finally \(\|e^{a|x|}h\|_2\le e^{aR}\|h\|_2\). This proves (3), and the symmetric weighted-space continuity follows by the same bounds. ∎

The apparent use of the full infinite prime sum creates no divergence in this argument. Exponential localization is exactly what makes it summable. For compact f,h the full expression equals the usual finite-window expression, because translations longer than the autocorrelation support vanish.

## 3. Annihilation holds without RH

For \(b\ge0\), put

\[
g_b(x)=\tfrac12\{k(x-b)+k(x+b)\},\qquad
F_{g_b}(z)=\cos(bz)\Xi(z)/4.
\tag{4}
\]

Every \(g_b\) lies in \(X_a\) for every fixed a. Since its transform vanishes at every \(\gamma\in\Gamma\), (2) gives

\[
Q(f,g_b)=Q(g_b,f)=0
\tag{5}
\]

for compact smooth f and for the smooth rapidly decaying functions used here. This is valid whether the zeros are real or nonreal. Derivatives of k likewise give annihilators by multiplying Xi by a polynomial.

For clarity about the test class: the correlations with k or its fixed translates decay faster than every exponential, including the derivatives needed by the explicit formula. Their Mellin counterparts satisfy the usual Weil-class decay at both endpoints. One may first apply the explicit formula to these correlations and then use (3) for cutoff limits. The conclusion is a statement about the radical of a form on a weighted test space, not the kernel of a presumed self-adjoint whole-line \(L^2\) operator.

## 4. Finite-window residuals and many near-zero eigenvalues

Choose an even smooth cutoff \(\chi_R\), equal to 1 on \([-R+1,R-1]\), supported inside \((-R,R)\), with uniformly bounded first derivative. Set

\[
p_{b,R}=\chi_Rg_b,
\qquad t_{b,R}=(1-\chi_R)g_b.
\]

For fixed b, (1) implies, for some constants depending on b and a,

\[
\|t_{b,R}\|_{X_a}\le C_b\exp(-c_b e^{2R}).
\tag{6}
\]

Let \(W_{2R}\) denote the self-adjoint finite-window Weil operator on \(L^2([-R,R])\), and let \(W_{+,2R}\) be its even part. From (3) and (5),

\[
Q(p_{b,R},h)=-Q(t_{b,R},h),
\qquad
\|W_{2R}p_{b,R}\|_2
\le C_a e^{aR}\|t_{b,R}\|_{X_a}.
\tag{7}
\]

Here \(p_{b,R}\) is already smooth and compactly supported, so its zero extension belongs to the logarithmic multiplier's operator domain; the local prime and pole perturbations are bounded. Thus \(p_{b,R}\in\operatorname{Dom}W_{2R}\) directly. Equation (3) identifies its action on smooth test functions and then on all \(L^2\) inputs by continuity.

There is a sharper quadratic identity:

\[
Q(p_{b,R},p_{c,R})=Q(t_{b,R},t_{c,R}).
\tag{8}
\]

It follows by expanding \(p=g-t\) and using the radical property twice. Thus the energy is quadratic in the omitted tails, while the operator residual is only linear in them.

**Proposition 1 (unconditional finite families of approximate zero modes).** Fix distinct nonnegative \(b_1,\ldots,b_m\). There are constants \(C_m,c_m>0\) such that, for all sufficiently large R, the span \(S_R\) of \(p_{b_j,R}\) has dimension m and

\[
\|W_{+,2R}f\|_2\le\varepsilon_m(R)\|f\|_2
\quad(f\in S_R),\qquad
\varepsilon_m(R)=C_m\exp(-c_m e^{2R}).
\tag{9}
\]

Consequently \(W_{+,2R}\) has at least m eigenvalues, counting multiplicity, in \([-2\varepsilon_m(R),2\varepsilon_m(R)]\).

**Proof.** The functions \(g_{b_j}\) are independent: their Fourier transforms are Xi times independent cosine functions. Xi is nonzero on a neighborhood of zero, so any linear dependence would be an identically zero trigonometric polynomial. The cutoff Gram matrices converge to a positive-definite Gram matrix. Hence coefficients in the finite span have a uniform bound in terms of its \(L^2\) norm. Combine this with (6)–(7); absorb \(e^{aR}\) into a slightly smaller double-exponential constant.

The finite-window operator has compact resolvent. If the spectral subspace for the indicated interval had dimension less than m, some nonzero f in \(S_R\) would be orthogonal to it. The spectral theorem would give \(\|Wf\|_2>2\varepsilon_m(R)\|f\|_2\), contradicting (9). ∎

This is genuinely unconditional near-zero spectrum, not merely a min–max upper bound that could be satisfied by distant negative eigenvalues.

**Corollary 2 (conditional low-level/gap collapse).** Under RH, all these operators are nonnegative, so every fixed-index even eigenvalue tends to zero, at an upper rate of the form in (9). In particular the first even spectral gap cannot have a positive support-independent lower bound.

The constants depend on m; no simultaneous uniform assertion as m grows with R is made. The conclusion does not disprove a useful *relative* residual/gap estimate. A centered candidate's residual might decay substantially faster than its second-even separation. Establishing that comparison is exactly the missing information.

For finite Fourier compressions, the same assertion transfers at any fixed R once the selected functions are approximated sufficiently in operator graph norm. This note does not claim that the polynomial Fourier schedule controlling the candidate in \(L^2\) automatically reaches the exponentially smaller spectral scale. Fixed-support graph-core approximation and a useful simultaneous quantitative schedule are different assertions.

## 5. Actual arithmetic approximate zero modes with escaping moments

Equation (4) also gives

\[
\int g_b=\int k,
\qquad
\frac12\frac{\int x^2g_b}{\int g_b}
=\tau_k+\frac{b^2}{2},
\quad
\tau_k=\frac12\frac{\int x^2k}{\int k}.
\tag{10}
\]

For a fixed nonzero b, its normalized transform is

\[
\cos(bz)\frac{\Xi(z)}{\Xi(0)},
\tag{11}
\]

not the desired normalized Xi function. Under RH it still has only real zeros. Thus even the radical condition plus evenness, positive profile, and real-zero transforms would not uniquely select Xi.

The escape can be made quantitative in the *actual arithmetic form*. Set \(b_R=R/2\) and \(p_R=\chi_Rg_{b_R}\). The distance from either translated center to the cutoff is at least \(R/2-1\). Applying the same tail estimate now gives

\[
\|W_{2R}p_R\|_2\longrightarrow0,
\qquad
\frac12\frac{\int x^2p_R}{\int p_R}
=\tau_k+\frac{R^2}{8}+o(1).
\tag{12}
\]

Indeed the weighted tail and its second moment are bounded by a polynomial/exponential prefactor times \(\exp(-c e^R)\), which dominates the extra factors from the growing translate. The mean tends to \(\int k>0\), while \(\|p_R\|_2^2\to\|k\|_2^2/2\), since the two lobes separate. Normalizing in \(L^2\) therefore does not change residual convergence or the moment ratio.

These are even pointwise-positive arithmetic approximate zero modes with divergent normalized second moment. They are not asserted to be actual ground states or finite CCM mechanical realizations. Their role is to rule out an inference from residual smallness, evenness and positivity of the profile to the desired trace bound.

## 6. Off-axis zeros give an explicit even negative witness

The distinction between the near-zero family and ground selection can be made without importing a separate version of Suzuki's criterion.

**Proposition 3.** Suppose Xi has a nonreal quartet \(\pm\gamma,\pm\bar\gamma\), with \(\Re\gamma\ne0\), \(\Im\gamma\ne0\), each of multiplicity m. Then there is a real even smooth function f in \(X_a\) for every a, with

\[
Q(f,f)=-4m.
\tag{13}
\]

Consequently there is a compact smooth even negative test. The lowest even eigenvalue of \(W_{2R}\) is bounded above by a fixed negative number for all sufficiently large R.

**Proof.** Define the entire even functions

\[
U(z)=\frac{\Xi(z)}{(z^2-\gamma^2)^m},\qquad
U^*(z)=\overline{U(\bar z)},\qquad c=U(\gamma)\ne0,
\]

and

\[
F(z)=\frac{i}{c}U(z)+\overline{\frac{i}{c}}\,U^*(z).
\tag{14}
\]

Then F is real-entire and even. It vanishes at every zero outside this quartet; \(F(\gamma)=i\) and \(F(\bar\gamma)=-i\), with the same values at the corresponding negatives. The quotient removes the full multiplicity only at the chosen pair. On every horizontal strip U and its polynomially weighted derivatives retain the exponential real-frequency decay of Xi. Fourier inversion and contour shifting therefore give a real even smooth inverse transform f with decay faster than every fixed exponential. The explicit formula applies, and each of the four selected terms in (2) is -1, with multiplicity m. This proves (13).

Smooth compact cutoffs converge to f in \(X_a\), so continuity proved in Section 2 preserves strict negativity for a sufficiently large cutoff. Normalize one such compact test; its negative Rayleigh quotient is then available in every larger even window. ∎

This is an existence theorem conditional on a hypothetical off-axis zero, not a numerical construction of such a zero. Standard analytic continuation/Stirling bounds for Xi on fixed horizontal strips justify the Fourier contour shift; division introduces no poles because its numerator has the stated zeros.

For the implication from failure of RH, recall that zeta has no real zero in \((0,1)\): its alternating eta series is positive there and \(\zeta(s)=\eta(s)/(1-2^{1-s})<0\). Thus an off-critical nontrivial zero has nonzero ordinate, giving \(\Re\gamma\ne0\) as required by Proposition 3.

**Corollary 4 (asymptotic orthogonality if RH fails).** Let \(v_R=p_{0,R}/\|p_{0,R}\|_2\), and let \(u_R\) be any normalized lowest even eigenvector, with eigenvalue \(\epsilon_R\). If RH fails, Proposition 3 gives \(\epsilon_R\le-\delta<0\) eventually. Thus

\[
|\langle u_R,v_R\rangle|
=\frac{|\langle u_R,W_{2R}v_R\rangle|}{|\epsilon_R|}
\le\frac{\|W_{2R}v_R\|_2}{\delta}\longrightarrow0.
\tag{15}
\]

The sign-aligned distance therefore tends to \(\sqrt2\), despite the candidate's residual tending to zero superexponentially. This provides a precise counterfactual failure mechanism for a residual-only proof.

The lowest even energy is nonincreasing under inclusion of windows. Together with Proposition 1 and the even-negative-witness construction, this gives the exact criterion

\[
\mathrm{RH}\quad\Longleftrightarrow\quad
\epsilon_R\longrightarrow0\quad(R\to\infty).
\tag{16}
\]

In particular, identifying the cutoff Xi kernel with the actual ground state would contain the missing positivity information, even before the mechanical determinant argument is applied. The residual calculation alone does not contain it.

**Corollary 5 (an overlap-only sufficient target).** Let \(u_R\) be any normalized lowest even eigenvector and \(v_R\) the normalized cutoff Xi kernel. Put \(r_R=\|W_{2R}v_R\|_2\). If along a cofinal sequence \(R_j\to\infty\),

\[
\frac{r_{R_j}}{|\langle u_{R_j},v_{R_j}\rangle|}\longrightarrow0,
\tag{21}
\]

with nonzero denominators, then RH holds. In particular, a support-independent positive lower bound for the absolute overlap along such a sequence suffices.

**Proof.** The eigenvector identity gives

\[
|\epsilon_R|\,|\langle u_R,v_R\rangle|
=|\langle u_R,W_{2R}v_R\rangle|\le r_R.
\]

Thus (21) forces \(\epsilon_{R_j}\to0\). Domain monotonicity and Proposition 3 imply (16), giving RH. No sign of \(\epsilon_R\), simplicity, odd-sector gap, or assumption that the even ground is the full ground is used. ∎

A basis-independent version uses the orthogonal projection \(P_{\min,R}\) onto the lowest even eigenspace and \(\alpha_R=\|P_{\min,R}v_R\|_2\). Then \(|\epsilon_R|\alpha_R=\|P_{\min,R}W_{2R}v_R\|_2\le r_R\). Thus \(r_{R_j}/\alpha_{R_j}\to0\) is the same type of sufficient target without choosing a ground eigenvector, and remains meaningful if the ground eigenvalue is multiple.

This is substantially weaker than the audit's \(O(L^{-5/2})\) full-profile comparison when the objective is RH through the original unshifted Weil energies. It is not a sufficient condition for identifying the CCM determinant with Xi or for uniform normalized moments. Those are different, stronger outputs. The substantive missing theorem is now explicit: prevent the even ground from becoming orthogonal to the Xi approximate zero mode at a rate as fast as its residual. This overlap estimate is not supplied by the existing residual calculation.

## 7. Dividing out a real zero: tail optimality is not the selection rule

The concern that dividing a real-zero pair out of Xi produces a more rapidly decaying spatial profile is correct. Let \(\gamma>0\) be an actual real zero, and define

\[
F_g(z)=\frac{\Xi(z)}{4(1-z^2/\gamma^2)}.
\tag{17}
\]

The inverse profile solves \(g''+\gamma^2g=\gamma^2 k\). On the positive half-line it can be written

\[
g(x)=\gamma\int_x^\infty
\sin(\gamma(t-x))\,k(t)\,dt.
\tag{18}
\]

The zero conditions \(\Xi(\pm\gamma)=0\) eliminate the oscillatory homogeneous tails on the opposite side; Fourier inversion gives the real even rapidly decaying solution. Since the local decay rate of k is \(2\pi e^{2x}(1+o(1))\), endpoint Laplace asymptotics yield

\[
g(x)\sim\frac{\gamma^2}{4\pi^2}e^{-4x}k(x)
\qquad(x\to+\infty).
\tag{19}
\]

Thus the principal double-exponential exponent is unchanged, but the prefactor is smaller by \(e^{-4x}\).

If the removed real zero is simple, g is **not** a Weil annihilator. Its transform is nonzero at that pair and zero at all other zeros, so

\[
Q(g,g)=2|F_g(\gamma)|^2>0,
\qquad F_g(\gamma)=-\frac\gamma8\Xi'(\gamma).
\tag{20}
\]

This holds regardless of whether other zeros are off the line, because their transform factors vanish. Its compact-cutoff energies tend to this positive constant, while cutoff k has energy tending to zero. Hence minimizing tails without enforcing the arithmetic form is an invalid selection principle; the division example does not itself disprove selection by the actual Weil ground energy.

There is a further unresolved multiplicity subtlety. If the real zero has multiplicity at least two, dividing out only one pair-factor leaves the transform zero at every zeta zero, so g remains a Weil annihilator and has the improved tail in (19). The Weil radical tests values at zeros with multiplicity weights, not derivative vanishing of the same multiplicity. Therefore radical membership alone does not force divisibility by the full Xi function with its multiplicities. This note does not infer that the actual ground state selects the divided profile; that would require comparing the finite-window boundary energies. It does show that a proposed uniqueness argument based only on radical membership or “smallest tails” must confront multiplicities explicitly.

## 8. Consequence for the next CCM calculation

The new positive content is an unconditional family of arithmetic near-zero states, a finite-window cluster theorem, and an explicit explanation of how an off-axis zero separates that cluster from the ground. The comparison program should therefore estimate a *selection quantity*: a lower bound on the complement adapted to the candidate relative to its residual, or a boundary splitting law within the approximate radical. A support-independent even gap is unavailable under RH. A small absolute residual is already available without RH.

The rank-one trace identity can still replace strong \(L^2\) closeness by direct normalized-transform and moment estimates. That is a legitimate weakening, but the escaping translated family shows why those observables need independent arithmetic selection control: they vary inside the same approximate radical. No new claim of ground simplicity, evenness of the full ground, a useful relative gap bound, Xi convergence, or RH is made here.

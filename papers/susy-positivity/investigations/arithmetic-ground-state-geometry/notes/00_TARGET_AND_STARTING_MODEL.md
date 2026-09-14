# Target and starting arithmetic ground-state model

This note fixes conventions for the new investigation. The positive finite-prime control and the full arithmetic target are different objects. No target positivity is assumed.

## The required finite-interval form

Let \(I_L=(-L/2,L/2)\), extend \(f\) by zero as \(F=E_Lf\), and take \(\widehat F(\tau)=\int F(x)e^{-i\tau x}\,dx\). Put
\[
B(s)=\Re\psi(\tfrac14+i\sqrt{s}/2)-\psi(\tfrac14)
=\sum_{k\ge0}\frac{2}{2k+1/2}\frac{s}{s+(2k+1/2)^2},
\]
\[
K[F]=\frac1{2\pi}\int B(\tau^2)|\widehat F(\tau)|^2\,d\tau,
\quad w_0=\psi(\tfrac14)-\log\pi,
\quad U_dF(x)=F(x-d).
\]
With
\[
C(f)=\int f(x)\cosh(x/2)\,dx,\qquad
S(f)=\int f(x)\sinh(x/2)\,dx,
\]
the pole contribution is \(P_L[f]=2|C(f)|^2-2|S(f)|^2\). The target is
\[
Q_L[f]=K[F]+w_0\|f\|^2+P_L[f]
-2\sum_{m\log p<L}(\log p)p^{-m/2}\Re\langle F,U_{m\log p}F\rangle.
\]
Its closed semibounded realization has logarithmic Fourier form domain. Nonnegativity for arbitrary support lengths is the unresolved program-level assertion.[^weil] A successful model must derive this full polarized form as an ordinary physical norm, rather than assume its positive square root.

## The positive finite-prime control

For finite prime set \(\mathcal S\) and \(\sigma>0\), use
\[
\mathscr H_\mathcal S=L^2(\mathbb R,dy)\otimes\bigotimes_{p\in\mathcal S}\ell^2(\mathbb N_0),
\qquad
A_{\sigma/2}=\partial_y+\frac{e^y-\sigma/2}{2},
\qquad D_p=T-p^{-\sigma/2}I,
\]
where \((T\xi)_n=\xi_{n+1}\). Each closed two-term complex has its physical Hilbert adjoint and a positive supersymmetric Hamiltonian. Their finite graded tensor product has a unique bosonic zero state, up to scale,
\[
\Psi_\sigma(y,\mathbf n)=\pi^{-\sigma/4}
e^{(\sigma y/2-e^y)/2}\prod_{p\in\mathcal S}p^{-\sigma n_p/2}.
\]
The common self-adjoint observable
\[
X=\frac y2-\sum_{p\in\mathcal S}n_p\log p-\frac{\log\pi}{2}
\]
satisfies
\[
\|\Psi_\sigma\|^2=\Lambda_\mathcal S(\sigma),\qquad
\langle\Psi_\sigma,e^{i\tau X}\Psi_\sigma\rangle=\Lambda_\mathcal S(\sigma+i\tau),
\quad
\Lambda_\mathcal S(z)=\pi^{-z/2}\Gamma(z/2)\prod_{p\in\mathcal S}(1-p^{-z})^{-1}.
\]
These follow by integration and geometric sums. Supersymmetric Morse potentials and related Fourier amplitudes have existing literature; no priority claim is made for the elementary factor construction.[^morse]

The normalized squared overlap is positive definite, while a parameter derivative of its logarithm is a different observable. The exact identity is
\[
\left.\partial_\sigma\log\frac{|\Lambda_\mathcal S(\sigma+i\tau)|^2}{\Lambda_\mathcal S(\sigma)^2}\right|_{\sigma=1/2}
=B(\tau^2)+2\sum_{p\in\mathcal S,m\ge1}(\log p)p^{-m/2}[1-\cos(m\log p\,\tau)].
\]
This is a positive jump energy \(J_{\mathcal S,L}\) after zero-extension compression. The complete form is
\[
W_L=J_{\mathcal S,L}-\kappa_\mathcal S I+P_L,
\qquad
\kappa_\mathcal S=-w_0+2\sum_{p\in\mathcal S,m\ge1}(\log p)p^{-m/2}>0,
\]
provided \(\mathcal S\) contains all primes active on \(I_L\). Negative contact subtraction and pole accounting are therefore the main new targets.

## Constraints inherited from the preceding investigation

The original Hamiltonian fixes a ray, not its parameter-dependent source normalization. Its chosen holomorphic extension \(\Psi_z=e^{zX/2}e^{-e^y/2}\) has metric \(\Lambda_\mathcal S(\Re z)\), distinct from the squared transition amplitude \(|\Lambda_\mathcal S(z)|^2\). The former has nonzero curvature; the latter is a flat scalar metric. The former cannot remain an ordinary rank-one chiral \(tt^*\) metric. A different partner-parameter extension is allowed.

The unchanged Hamiltonian also has a multiplicity-two interval in its positive spectrum, so it cannot acquire four standard real supercharges without a change of fields or dynamics. The new investigation permits those changes. It does not regard formal spectator doubling as a new constraint on the arithmetic pairing.

Support compatibility is essential. Positive independent prime-jump energies diverge in an unrestricted all-prime limit on every nonzero compactly supported input. Conversely, retaining only finitely many primes and the complete signed poles fails positivity for sufficiently large supports. A full comparison must enlarge the prime set with the support; a finite-prime amplitude with all repetitions remains a useful separate control.

The next notes test enlarged theories, matrix metrics, scalar ground transforms and vector parameters against these requirements. Their constructions must be classified as physical Hilbert models, holomorphic periods, metric-equation solutions, or actual arithmetic norm identities.

## Sources

[^weil]: Masatoshi Suzuki, [Weil's quadratic form via the screw function](https://arxiv.org/abs/2606.09096v2), 2026. The formula above uses the shared program's additive normalization.
[^morse]: Edward Witten, [Supersymmetry and Morse theory](https://www.ias.edu/sites/default/files/sns/files/supersymmetry-and-morse-theory-1982.pdf), 1982; Michael McGuigan, [Riemann Hypothesis, Modified Morse Potential and Supersymmetric Quantum Mechanics](https://arxiv.org/abs/2002.12825), 2020.

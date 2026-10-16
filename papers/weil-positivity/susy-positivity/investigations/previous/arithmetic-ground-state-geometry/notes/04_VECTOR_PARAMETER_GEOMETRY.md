# An explicit vector-parameter lift and the normalization it cannot fix

## Purpose and status

The previous rank-one obstruction concerns ordinary chiral-parameter \(tt^*\) geometry. Vector-multiplet parameters obey different equations: the Berry connection and a projected moment-map observable satisfy a Bogomolny equation. This is a necessary constraint derived from four-supercharge invariance, rather than a converse existence theorem for a microscopic quantum theory.[^berry]

Here an explicit Abelian Bogomolny solution extends the arithmetic benchmark's Berry data on a real two-dimensional slice. This proves that the chiral curvature obstruction does not by itself exclude vector-parameter geometry. It also shows why merely solving the alternative equations is insufficient: an entire class of positive amplitudes admits the same construction, and the arithmetic contact remains undetermined. These are direct deductions, not claims of an arithmetic quantum realization.

## 1. The real-slice Berry connection

For a finite prime set \(S\), write
\[
\Lambda_S(z)=\pi^{-z/2}\Gamma(z/2)\prod_{p\in S}(1-p^{-z})^{-1},
\qquad F(z)=\log\Lambda_S(z),\quad \Re z>0.
\]
There is a holomorphic logarithm on this half-plane since each factor is holomorphic and nonzero there. Choose it real on the positive real axis. The Morse–prime ground family has \(\|\Psi_\sigma\|^2=e^{F(\sigma)}\), and its normalized chosen complex extension is
\[
\Omega_{\sigma,\eta}=e^{i\eta X/2}\Omega_\sigma.
\]
For the Berry convention \(A=i\langle\Omega,d\Omega\rangle\), its real-slice connection and curvature are
\[
A_\sigma=0,\qquad A_\eta=-\tfrac12F'(\sigma),
\qquad F_{\sigma\eta}=-\tfrac12F''(\sigma).
\]
The derivative \(F''(\sigma)=\operatorname{Var}_\sigma(X)>0\). This is the actual physical curvature for the chosen family. The variables \(\sigma,\eta\) are not yet components of an independently specified vector multiplet.

## 2. A constructive Abelian Bogomolny extension

Introduce a third real coordinate \(v\), orient parameter space as \((\sigma,\eta,v)\), and put \(z=\sigma+iv\). Define
\[
\boxed{\displaystyle
A_\sigma=A_v=0,\qquad
A_\eta(\sigma,v)=-\frac12\Re F'(\sigma+iv),\qquad
\Phi(\sigma,v)=-\frac12\Im F'(\sigma+iv).}
\]
These functions are real, smooth for \(\sigma>0\), and independent of \(\eta\). The Cauchy–Riemann equations imply
\[
\begin{aligned}
(\nabla\times A)_\sigma&=-\partial_v A_\eta
=-\tfrac12\Im F''(z)=\partial_\sigma\Phi,\\
(\nabla\times A)_\eta&=0=\partial_\eta\Phi,\\
(\nabla\times A)_v&=\partial_\sigma A_\eta
=-\tfrac12\Re F''(z)=\partial_v\Phi.
\end{aligned}
\]
Thus \(\nabla\times A=\nabla\Phi\), the Abelian Bogomolny equation. At \(v=0\), \(\Phi=0\) and the connection restricts exactly to the displayed physical Berry connection. The nonzero variance curvature causes no local or half-space PDE obstruction.

The construction uses only holomorphy and real structure. The same formula works for any holomorphic \(F\) real on the positive axis; it does not select gamma functions, primes, a positive metric, or a quantum Hamiltonian. In particular, it is a solution of the necessary effective-connection equations, not a demonstration that the original family has acquired four supercharges.

The microscopic requirements remain substantial. A proposed vector-multiplet theory must supply its dynamical fields and supercharges, show that these \(A\) and \(\Phi\) are the actual Berry connection and projected moment-map operator, and identify the arithmetic source. No such construction follows from the Cauchy–Riemann calculation.

## 3. Exact arithmetic dependence and where singularities occur

In this case
\[
F'(z)=-\frac{\log\pi}{2}+\frac12\psi(z/2)
-\sum_{p\in S}\frac{\log p}{p^z-1}.
\]
This formula is holomorphic throughout \(\Re z>0\). Its meromorphic continuation has gamma singularities at nonpositive even integers and prime singularities at \(z=2\pi ik/\log p\). Each isolated simple local-factor pole contributes residue \(-1\) to \(F'\), with multiplicities added when poles coincide.

At a simple boundary pole, the local term is \(F'(z)=-1/(z-z_0)+\) regular terms. The resulting \(\Phi\) is a two-dimensional dipole-type harmonic function, invariant along \(\eta\). It is not automatically the field of a regular point monopole in three-dimensional parameter space. Regularity, allowed singular defects, charge quantization and boundary conditions would therefore impose extra physical requirements if this particular continuation were used globally. The open half-space solution itself requires no passage through those singularities.

## 4. Curvature cannot choose the contact normalization

For any real constant \(c\), replace
\[
F(z)\longmapsto F(z)+cz.
\]
The normalized real-\(\sigma\) ground ray is unchanged by the corresponding source rescaling \(\Psi_z\mapsto e^{cz/2}\Psi_z\). On the chosen complex family its normalized state changes only by the phase \(e^{ic\eta/2}\). The Berry potential changes by
\[
A_\eta\longmapsto A_\eta-\frac c2,
\]
which is a flat pure-gauge change on the present noncompact \(\eta\)-line. The curvature and \(\Phi\) are unchanged. On a compact parameter direction one would need to specify large-gauge and holonomy data separately; there is no such compactification in the current construction.

However the first normal derivative of the squared arithmetic amplitude changes by
\[
\partial_\sigma\log|\Lambda_S(\sigma+i\tau)|^2
\longmapsto
\partial_\sigma\log|\Lambda_S(\sigma+i\tau)|^2+2c.
\]
This is exactly a scalar contact change in the compressed arithmetic form. In particular, changing the \(\pi^{-z/2}\) normalization changes a contact term without changing this vacuum curvature. Neither the ordinary chiral curvature equations nor this vector-parameter lift determine that absolute source normalization.

There is a further conceptual distinction between a Berry connection coefficient and a positive observable. The first derivative contains the mean \(\langle X\rangle\), which changes when the origin of \(X\) is shifted. The variance controls curvature and is shift invariant. A physical boundary preparation or arithmetic correspondence may fix the origin, but a variance or curvature equation alone cannot do so.

## 5. Relation to the full target

At \(\sigma=1/2\), the pole-free Fourier multiplier is \(2\Re F'(1/2+i\tau)\). Formally the constructed potential gives \(-4A_\eta(1/2,\tau)\). This is an exact identity of functions. It is not a norm identity: a gauge-potential component need not have a sign, and the identification \(v=\tau\) is an extra proposed link between parameter space and the arithmetic Fourier variable.

The signed rank-two pole form is still absent. Multiplying local factors by the usual scalar completion polynomial does not recover it by a pointwise normal derivative on the critical line. The physical theory would have to derive the contour/residue operation or an equivalent boundary sector with the correct positive total pairing.

## Conclusion for selecting the next theory

Vector-parameter geometry remains a viable escape from the rank-one chiral obstruction. The explicit lift shows that nonzero variance curvature can satisfy its necessary equations. It also sets a stronger standard for further work: derive the Berry and moment-map data from a microscopic positive theory and fix the physical boundary source, rather than identifying an arithmetic function with a freely constructed gauge potential.

The result is compatible with pursuing a Kähler sigma model or interacting defect with vector-multiplet parameters. It does not rank an arbitrary formal Bogomolny solution above an actual quantum model. A useful new identity must constrain the complete pairing, including the normalization and poles that this lift leaves free.

## Source

[^berry]: Julian Sonner and David Tong, [Berry Phase and Supersymmetry](https://arxiv.org/abs/0810.1280), 2008/2009. The distinction between chiral and vector parameter equations is literature. The explicit half-space lift and arithmetic normalization test in this note are derived above.

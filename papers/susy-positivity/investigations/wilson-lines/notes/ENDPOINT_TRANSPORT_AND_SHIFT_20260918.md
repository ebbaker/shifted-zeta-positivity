# Endpoint transports, common supersymmetry, and the shifted tower

18 September 2026. Written by OpenAI GPT-6 (Codex) for Edward Baker.

This follows [the endpoint-matter continuation](ENDPOINT_MATTER_CONTINUATION_20260918.md). It carries the first calculations beyond the opening kernel identity. The supersymmetry result is a necessary **bulk** condition for planar semicircles with one fixed scalar coupling. The determinant is an exact auxiliary spectral realization, not a determinant derived from a localized gauge-theory path integral.

## 1. The bulk supersymmetry condition can be solved explicitly

Use complex Euclidean Clifford matrices with `{Gamma_A,Gamma_B}=2 delta_AB`, a defect tangent direction `1`, a normal bulk direction `3`, and one fixed internal direction `I`. The usual local bulk BPS condition is

\[
 [i\dot x^\mu\Gamma_\mu+|\dot x|\Gamma_I]
 [\epsilon_s+x^\mu\Gamma_\mu\epsilon_c]=0.
 \tag{1.1}
\]

These are a definite convention for the calculation. The general Killing-spinor and Wilson-loop framework is described in [Dymarsky–Pestun, arXiv:0911.1841](https://arxiv.org/abs/0911.1841); the open-line defect and endpoint conditions must additionally be imposed. We do not count physical supercharges by counting components of a small Clifford representation.

Parameterize the consistently oriented upper semicircle by

\[
 x(\theta)=(c+R\cos\theta)e_1+R\sin\theta e_3,
 \qquad 0\le\theta\le\pi,\quad R>0.
\]

Set `A=epsilon_s+c Gamma_1 epsilon_c`. The constant coefficient of (1.1), after division by `R`, is

\[
 \Gamma_I A+iR\Gamma_3\Gamma_1\epsilon_c=0,
\]

because `(-sin(theta) Gamma_1+cos(theta) Gamma_3)(cos(theta) Gamma_1+sin(theta) Gamma_3)=Gamma_3 Gamma_1`. It gives

\[
 \epsilon_s=-c\Gamma_1\epsilon_c
             -iR\Gamma_I\Gamma_3\Gamma_1\epsilon_c.
 \tag{1.2}
\]

Substitution into the sine and cosine coefficients makes both vanish. Thus (1.2) is necessary and sufficient for this bulk contour condition.

### Two circles

Define `J=i Gamma_I Gamma_3`. Then `J^2=1` and `[J,Gamma_1]=0`. Two circles with the same fixed internal coupling require

\[
 [\Delta c+\Delta R J]\Gamma_1\epsilon_c=0.
 \tag{1.3}
\]

Multiplying by `Delta c-Delta R J` shows that a nonzero common solution is possible only if

\[
 (\Delta c)^2=(\Delta R)^2.
 \tag{1.4}
\]

For distinct circles, this says that they share their left endpoint or their right endpoint. In the unconstrained complex Clifford problem, the appropriate eigenspace of `J` also makes it sufficient. Defect, chirality, reality, and endpoint-field constraints may reduce this space; they cannot repair a zero solution of (1.3).

The two semicircles in the even kernel have

\[
 (c_s,R_s)=((r_1+r_2)/2,(r_1-r_2)/2),\qquad
 (c_o,R_o)=((r_1-r_2)/2,(r_1+r_2)/2).
\]

They share the right endpoint `r1`, so the bulk condition allows `J epsilon_c=epsilon_c` and

\[
 \epsilon_s=-r_1\Gamma_1\epsilon_c.
 \tag{1.5}
\]

This works for all `r2` at that fixed `r1`. But two distinct values of `r1` in this family force `epsilon_c=0` and then `epsilon_s=0`.

**Conclusion with its scope:** the fixed-coupling, pairwise-semicircle construction has no one nonzero bulk supercharge for the full two-variable kernel. This already fails before endpoint conditions are imposed. It does not exclude contour-dependent internal couplings, extra insertions, different transport networks, a construction needing no common supercharge, or a positive theory with a different observable. It also does not prove that the surviving fixed-row bulk solutions pass the defect endpoint constraints. Individual BPS operators and a common cohomological family are different requirements.

## 2. Pairwise gauge invariance does not give a Gram kernel

There is a second, independent issue. To identify all endpoint values in a common color space one could choose a reference point `b` and transports `T_r` and form dressed fields `Phi(r)=T_r q(r)`. The positive pairing would then involve the **adjoint** transport, schematically

\[
 \langle\Phi(r_1)^\dagger\Phi(r_2)\rangle.
\]

Its paths run through the common reference construction; they are not the independently chosen semicircles joining each pair. In the simpler unitary-transport case, a representation `U_{xy}=T_x^{-1}T_y` would require `U_{xy}U_{yz}=U_{xz}`, so every triangular transport would be trivial. Generic pairwise semicircles enclose field strength and do not satisfy that identity configuration by configuration. With the supersymmetric scalar coupling, reverse transport and Hilbert adjoint also require separate treatment: the connection is not just an anti-Hermitian gauge connection.

Thus the semicircle expectation match cannot be promoted to a positive Gram construction by notation. A reflection-positive gluing rule, or a different common-reference network, must be established. This obstruction concerns the proposed factorization of transports; it is not a theorem excluding positivity of every expectation kernel.

## 3. The full archimedean shift needs no fractional spatial dimension

Let `H` act on `ell^2(N_0)` by

\[
 H|n\rangle=(2n+\tfrac12)|n\rangle.
\]

Its heat trace is exactly `n_gamma(u)`. The spectral zeta function of `(H+p)/2` is the Hurwitz function `zeta_H(s,z)`, where `z=1/4+p/2`. By [DLMF 25.11.18](https://dlmf.nist.gov/25.11.E18),

\[
 D(p):=\det{}_\zeta((H+p)/2)
       =\frac{\sqrt{2\pi}}{\Gamma(\tfrac14+\tfrac p2)}.
 \tag{3.1}
\]

The positive-operator derivation uses real `p>-1/2`; it extends analytically with the usual spectral-cut qualifications. Consequently, initially for real `p>omega-1/2`,

\[
 K_\omega^\Gamma(p)
 =\pi^\omega\frac{D(p+\omega)}{D(p-\omega)}
 =\pi^\omega
   \frac{\Gamma(\tfrac14+\tfrac{p-\omega}2)}
        {\Gamma(\tfrac14+\tfrac{p+\omega}2)}.
 \tag{3.2}
\]

This is the archimedean transfer of the Loewner factorization. The fixed tower remains unchanged; `omega` is an opposite shift in two operators on the same space. The factor `pi^omega` is the prescribed conductor normalization, not a prediction of endpoint physics. Had we regularized `H+p` rather than `(H+p)/2`, an additional scale factor would appear. Normalization must be tracked explicitly.

A convergent, scale-independent version is useful. For positive real reference `p0>omega-1/2`,

\[
 \frac{K_\omega^\Gamma(p)}{K_\omega^\Gamma(p_0)}
 =\prod_{n=0}^\infty
 \frac{(a_n+p+\omega)(a_n+p_0-\omega)}
      {(a_n+p-\omega)(a_n+p_0+\omega)},
 \quad a_n=2n+\tfrac12.
 \tag{3.3}
\]

Each logarithmic summand is `O(n^-2)`, so convergence is absolute away from the displayed poles. Equivalently,

\[
 \log\frac{K_\omega^\Gamma(p)}{K_\omega^\Gamma(p_0)}
 =\int_0^\infty(e^{-pu}-e^{-p_0u})
       \frac{2\sinh(\omega u)}u n_\gamma(u)\,du.
 \tag{3.4}
\]

The difference removes the origin singularity and the stated domain controls the tail. Differentiation gives

\[
 -\partial_\omega\log K_\omega^\Gamma(p)
 =-\log\pi+\tfrac12\psi(\tfrac14+\tfrac{p-\omega}2)
              +\tfrac12\psi(\tfrac14+\tfrac{p+\omega}2).
 \tag{3.5}
\]

Its noncontact causal kernel is `-2 cosh(omega u)n_gamma(u)`, exactly the archimedean part of the generator. The local constant is fixed by the same subtraction convention as in the target.

**What this advances:** the parity tower reproduces the shift dependence as well as the central energy. It supplies a fixed-space alternative to interpreting `2 omega` as a varying lattice dimension. It is an auxiliary determinant identity; the spectrum, determinant ratio and its statistics have not been obtained by gauge-theory localization. It neither yields the arithmetic factor nor proves passivity.

## 4. Where the prime terms enter, and why the determinant is only the beginning

Equation (3.5) supplies the continuous archimedean kernel. The full generator still requires

\[
 -2\sum_{p\ {
m prime}}\sum_{m\ge1}
 (\log p)p^{-m/2}\cosh(\omega m\log p)\,\delta_{m\log p},
\]

as well as the prescribed contact and pole pieces. Merely multiplying (3.2) by the missing zeta ratio would insert the desired arithmetic rather than derive it. Likewise, a positive heat trace does not prove that the completed transfer is contractive. The Loewner positive-kernel decomposition already demonstrates the gap between those statements.

## 5. The next useful branch

The simplest constant-coupling semicircle family has now been tested far enough to locate the new problem: it matches the free archimedean kernel pair by pair, but supplies neither a common protected family nor a positive gluing construction.

The next concrete choice is to **construct the gluing first**: fix a common reference transport or a reflected half-space state preparation, write its actual gauge-invariant pairing, and check its leading kernel. If supersymmetry is needed, solve its bulk and endpoint conditions together. A second option is to vary the internal scalar coupling with the contour to preserve one fixed supercharge, then check whether endpoint polarizations retain the equal even weights. Arbitrary-contour supersymmetric loop constructions such as [Drukker–Giombi–Ricci–Trancanelli, arXiv:0704.2237](https://arxiv.org/abs/0704.2237) show why the fixed-coupling exclusion is not general; they do not supply the requisite defect endpoints.

Do not proceed by assuming that one common supercharge or a positive Gram factorization follows from individual semicircle BPS status. Do not claim the source's self-energy normalization proves all-scale protection. And do not reopen the fractional lattice solely to realize (3.2): that half is already realized algebraically on the fixed tower.

**Status:** equations (1.2)–(1.5) are proved under the explicitly displayed bulk BPS equation; (3.1)–(3.5) are exact spectral identities. The defect-compatible positive gluing, endpoint interaction correction in a fixed local scheme, physical shift, and arithmetic remain open. The standard-library continuation checks exercise the Clifford identities, shared-endpoint condition, determinant ratios, their integral form, parity kernels, and subtraction diagnostics. They do not solve these physical existence questions.

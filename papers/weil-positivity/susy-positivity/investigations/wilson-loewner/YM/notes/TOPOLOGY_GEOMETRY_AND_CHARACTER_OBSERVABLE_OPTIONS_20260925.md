# Topology, geometry, and character observables: options after the winding test

25 September 2026. Prepared for Edward Baker with substantial LLM assistance.

Model: GPT-6 (Codex). Deployed variant and reasoning effort are not exposed; neither is inferred.

Status: assessment and elementary deductions, not independently reviewed. Alternative theories are discussed, not adopted as the current model. No Weil realization is established.

## 1. What changing topology can accomplish

Changing physical topology can introduce new cycle, flux, boundary, or scattering sectors. Its usefulness depends on how those sectors change the actual source pairing. Merely changing the topology of the test-function space does not alter pairings of sources already defined.

The [winding/electric exclusion](NATIVE_WINDING_MELLIN_SOURCES_AND_ELECTRIC_PAIRING_20260925.md) used a finite compact link manifold, a smooth positive state, and one fixed simple contour with distinct underlying links. It did not use contractibility of that contour. Thus replacing a plaquette by a noncontractible simple cycle, or changing the finite spatial cell complex while preserving these hypotheses, leaves the argument intact. The constants change; the local input-L² bound remains. This does not exclude other sources on the new topology.

**Uniform-bound lemma.** Suppose a family of positive source pairings, possibly on different Hilbert spaces, satisfies
\[
B_\alpha(f,f)\le C_I\|f\|_2^2,
\qquad \operatorname{supp}f\subset I,
\]
with the same finite \(C_I\) for every \(\alpha\). If \(B_\alpha(f,g)\to B(f,g)\) for all tests, then \(B\) obeys the same bound.

**Proof.** Take the limit of the diagonal inequality. \(\square\)

Consequently a continuum, volume, rank, or singular-state limit of the excluded law can help only if this bound fails to remain uniform. Losing the bound is necessary, not sufficient: the limiting source must still exist, and its pairing must retain physical positivity. Subtracting divergent norms is not automatically an OS construction.

Finite linear combinations of locally L²-bounded source maps remain locally L²-bounded. An infinite family with summable squared operator bounds, placed in a Hilbert direct sum, does too. Enlarging a source domain or using a stronger topology on the tests can admit genuinely new distributional sources, but cannot undo the numerical inequality for an unchanged law. Equivalent norms cannot repair it either. Defining a new output norm to be the Weil form would presuppose the positivity being investigated.

## 2. A concrete observable modification: representation characters

There is a useful improvement available without changing the fixed finite YM model. Retain the simple holonomy \(P\) and its marginal \(\rho(g)dg\) from the preceding note, with
\(0<c_\rho\le\rho\le C_\rho\). Use the scalar conjugation-invariant subspace
\[
\mathcal H_\rho^{\mathrm{cl}}=L^2(SU(2),\rho\,dg)^{\mathrm{Ad}},
\]
embedded in the original covariant space as \(F(P)I\).

Let \(\chi_m\) be the unnormalized character of the irreducible SU(2) representation of dimension \(m\), for \(m\ge1\). In the eigenangle coordinate,
\[
\chi_m(\theta)=\frac{\sin(m\theta)}{\sin\theta}.
\tag{1}
\]
For positive integers \(n\), define on continuous class functions
\[
(V_nF)(g)=\chi_n(g)F(g^n).
\tag{2}
\]
This combines a Wilson character insertion with contour repetition; its coefficient is prescribed by representation theory, not by zeta zeros or desired Weil moments.

**Proposition.** These operations satisfy
\[
V_n\chi_m=\chi_{nm},\qquad V_nV_k=V_{nk}.
\tag{3}
\]
They extend to isometries in the Haar class-function Hilbert space and to uniformly bounded operators in the actual marginal metric:
\[
\|V_nF\|_\rho^2\le\frac{C_\rho}{c_\rho}\|F\|_\rho^2,
\quad n\ge1.
\tag{4}
\]

**Proof.** The sine factors in \(\chi_n(g)\chi_m(g^n)\) cancel, giving (3); the identity extends continuously over central elements. Direct Haar integration makes the \(\chi_m\) an orthonormal basis of class functions. The map \(m\mapsto nm\) embeds that basis into itself, so \(V_n\) is an isometry. Comparison of the two metrics proves (4). The polynomial identity gives composition first on the dense character span and hence on the completion. \(\square\)

This removes the unboundedness of the *undressed* winding maps \(F(g)\mapsto F(g^n)\) found in the preceding note. It now permits an Euler identity in bounded operators on the actual class-function Hilbert space:
\[
\begin{aligned}
\mathcal Z_V(s)&=\sum_{n\ge1}n^{-s}V_n
 =\prod_p(I-p^{-s}V_p)^{-1},\\
-\mathcal Z_V'(s)\mathcal Z_V(s)^{-1}
 &=\sum_{p,k\ge1}(\log p)p^{-ks}V_{p^k},
\qquad \operatorname{Re}s>1.
\end{aligned}
\tag{5}
\]
Indeed all series converge absolutely in operator norm by (4). Unique factorization and (3) give the product; the inverse is the absolutely convergent Möbius series. Each local inverse also converges because \(V_p^k=V_{p^k}\) is uniformly bounded. Unlike undressed winding, \(V_n1=\chi_n\) is not a fixed constant vector.

There is still a metric obligation. The \(V_n\) are generally not isometries for nonconstant \(\rho\). With \(M_\rho\) denoting multiplication by the marginal density, their actual adjoints are
\[
V_n^{*\rho}=M_\rho^{-1}V_n^{*\mathrm{Haar}}M_\rho.
\tag{6}
\]
All proposed Ward or intertwining relations must use those adjoints. Conjugating everything into a Haar metric would be the already-audited weight transport; it does not identify the physical mixed pairing with the Weil form.

That mixed pairing is itself concrete. Put
\(u_j=\mathbb E_\nu[\chi_j(P)]\). The SU(2) character product identity gives
\[
G_{nm}=\langle\chi_n(P),\chi_m(P)\rangle_\nu
=\sum_{j=0}^{\min(n,m)-1}u_{n+m-1-2j}.
\tag{7}
\]
As a form on coefficient sequences, \(c_\rho I\le G\le C_\rho I\). Thus the simplest critical Mellin source
\[
J_\chi f=\sum_{n\ge1}n^{-1/2}\widehat f(\log n)\chi_n(P)
\tag{8}
\]
exists, but its exact pairing is
\[
\langle J_\chi f,J_\chi g\rangle
=\sum_{n,m\ge1}\frac{\overline{\widehat f(\log n)}
 \widehat g(\log m)}{\sqrt{nm}}G_{nm},
\tag{9}
\]
where the double expression is understood by limits of the bounded coefficient form. The logarithmic sampling estimate proved in the preceding note gives
\[
\|J_\chi f\|^2\le C\int(1+x^2)|f(x)|^2dx.
\tag{10}
\]
So this bare source is also excluded. The same applies to two such branches containing \(\widehat f(\pm\log n)\). The useful advance is the better operator algebra (2)–(6), not a claim that (8) realizes the target. A successful construction would need further independently defined source relations or insertions with a different pairing.

## 3. A topology–zeta connection that is already exact

Two-dimensional YM supplies a controlled alternative theory. In its standard character normalization, on a closed genus-\(g\) surface,
\[
Z_g(a)=\sum_R(\dim R)^{2-2g}e^{-a\sigma_R}.
\]
For SU(2), at zero area and \(g\ge2\),
\[
Z_g(0)=\sum_{m\ge1}m^{2-2g}=\zeta(2g-2).
\tag{11}
\]
See [Runkel–Szegedy, Proposition 5.7 and Remark 5.8, especially (5.36)](https://doi.org/10.1007/s00220-020-03902-1), in the setting originating in [Witten's two-dimensional YM work](https://arxiv.org/abs/hep-th/9204083).

The handle-addition operator at zero area acts on \(\chi_m\) by \(m^{-2}\), as follows from their equation (5.31). Its logarithm therefore supplies the scale \(\log m\). This connects topology directly with the character operators above. It supplies special zeta values and an integer scale, not the required mixed identity. Genus takes discrete integer values; analytic continuation in genus does not automatically define positive physical amplitudes. This would change the dimension and state of the current four-dimensional program.

Changing the global gauge group is another topological modification. For example, the SU(2) representations descending to SO(3) have odd dimensions, so their dimension Dirichlet series is \((1-2^{-s})\zeta(s)\) for \(\operatorname{Re}s>1\). This elementary representation-theoretic control shows how a global group choice can change an arithmetic local factor. It provides no automatic reason to prefer a different group for the completed Weil pairing.

## 4. Arithmetic cusp geometry and the shifted-transfer objective

On the modular quotient \(PSL(2,\mathbb Z)\backslash\mathbb H\), the scattering coefficient is
\[
C(s)=\frac{\Lambda(2s-1)}{\Lambda(2s)},\qquad
\Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s).
\tag{12}
\]
This is an exact geometric occurrence of the completed zeta function; see [Levitin–Strohmaier, §7.3.2, equation (12)](https://arxiv.org/pdf/1812.05554). Arithmetic structure and the metric matter, beyond the topological type of the surface.

There is an elementary connection to our separate causal target. With the project's entire normalization
\(\xi(s)=s(s-1)\Lambda(s)/2\),
\[
K_{1/2}(z)=\frac{\xi(z)}{\xi(z+1)}
=\frac{z-1}{z+1}\,C\!\left(\frac{z+1}{2}\right).
\tag{13}
\]
This follows by cancellation of the quadratic completion factors and holds meromorphically, with removable points handled by continuation. The parameter change turns physical scattering unitarity on \(\operatorname{Re}s=1/2\) into a boundary-modulus statement at \(\operatorname{Re}z=0\).

This identifies one transfer *function*, at the fixed shift \(\omega=1/2\). It supplies neither a YM preparation/readout map nor the family of smaller shifts required by the project's arithmetic limit. In particular zeros \(\rho\) of zeta enter scattering poles at \(s=\rho/2\); RH would constrain those resonances to \(\operatorname{Re}s=1/4\), not to the physical unitarity line. A self-adjoint Laplacian and unitary scattering do not by themselves prove that resonance restriction. This is a promising comparison model, not a transfer of its positivity into YM.

## 5. Other modifications and their obligations

| Modification | What it could change | Required new work |
|---|---|---|
| Full representation characters and the operations (2) | Multiplicative arithmetic acts by bounded operators in the existing finite YM sector | Derive additional source relations and the actual weighted mixed identity; the bare law (8) already fails |
| Unbounded families of distinct contours, spin networks, and loop-splitting/joining identities | Correlations beyond repeated powers of one holonomy | Define a global source and control its infinite sums; a finite bounded enlargement retains the old obstruction |
| Renormalized curvature, electric, stress-energy, or line insertions | Sources which need only exist after smearing; potentially different high-frequency growth | Prove the source domain and positivity after renormalization; derive logarithmic growth and the full separated pairing |
| Continuum, infinite-volume, or large-rank limit | May leave the uniformly comparable finite-state regime | Demonstrate the necessary failure of uniform local L² bounds and construct the positive limit |
| Boundary conditions, magnetic flux sectors, and disorder lines | Changes the observable algebra and topological sectors | Derive their actual reflected pairing; integer charges alone do not give prime-power coefficients |
| Arithmetic or adelic boundary/defect sector | Supplies a structural role for primes and the infinite place | Specify a new physical model or a genuine embedding, and prove its positive Weil pairing |

Wilson–'t Hooft observables provide electric and magnetic line data; [Kapustin's paper](https://arxiv.org/abs/hep-th/0501015) classifies such operators by electric/magnetic weights and explains the topological magnetic charge. The particularly strong Hecke connection in [Kapustin–Witten](https://arxiv.org/abs/hep-th/0604151) uses a twist of **N=4 supersymmetric** YM compactified on a Riemann surface. It is not an established identity for the present pure YM theory. A topological or cohomological correspondence would still need a compatible positive physical source metric, and geometric Langlands over a complex curve does not itself supply the rational-prime explicit formula.

For arithmetic spaces, [Connes's adelic trace-formula program](https://arxiv.org/abs/math/9811068) provides a geometric interpretation of the explicit formula. Its stated global trace-formula problem is essential to the RH implication. It cannot be replaced by the observation that an associated Hilbert space or statistical model is positive. This option addresses arithmetic structure more directly, but would be a substantial model change unless an independent occurrence theorem in YM were proved.

## 6. Research recommendation

My first choice **within the current model** is the character operation (2), together with physically specified insertions or relations that go beyond the bare Mellin law (8). It addresses an identified failure of the winding representation and exposes a precise mixed Gram matrix (7). The immediate test is whether the actual weighted adjoints and loop relations can yield any independently justified relation of the strength needed by the determination theorem. Another positive finite Gram matrix would not establish that.

For a topology-centered comparison, use two-dimensional YM with genus and boundary gluing. Its arithmetic ingredients are exact and its state spaces are controllable. For the separate shifted-transfer problem, use modular cusp scattering as the comparison, retaining the fixed-shift limitation of (13). Neither comparison is silently adopted as the main model.

Any candidate for the Weil pairing must satisfy both known tests: logarithmic growth on the fixed-support pole-neutral modulations, and the prescribed gamma tail plus singularities at every \(\pm k\log p\), with coefficients \((\log p)p^{-k/2}\). After pole removal the latter are the fourth-order delta terms derived in §7 of the winding note. These obligations distinguish a source realization from a zeta partition function, an Euler product, or a trace identity with an unidentified metric.

Verification: (3)–(10), the uniform-bound lemma, and the completion-factor cancellation in (13) were checked algebraically here; no new simulation is needed for these statements. The cited two-dimensional field-theory equations and modular scattering formula were inspected in the primary papers. The line-operator, geometric Langlands, and adelic references support the indicated scope only; no proof of their full constructions or a YM embedding was audited in this continuation.

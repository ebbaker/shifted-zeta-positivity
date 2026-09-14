# Non-Abelian tests for the arithmetic ground-state metric

## Results and scope

Allowing two or more vacua changes the rank-one conclusion, but it does not automatically make the original Morse–prime metric compatible with ordinary chiral \(tt^*\) geometry.

This note establishes three restrictions and two constructive controls:

1. The determinant of a finite-rank ordinary chiral \(tt^*\) metric is locally the squared modulus of a nonzero holomorphic function. The arithmetic metric cannot be the determinant, or a common scalar factor multiplying a finite-rank solution, in its original \(h(\Re z)\) dependence.
2. Adding finitely many physical vacuum vectors that are all holomorphic in a fixed positive ambient Hilbert space cannot extend the Morse–prime coherent family to an ordinary chiral \(tt^*\) bundle. This follows from a positive second-fundamental-form identity and the zero trace of a commutator.
3. The natural reciprocal-diagonal repair \(g=\operatorname{diag}(h,h^{-1})\) fails the usual two-vacuum companion-Higgs equation, in either choice of which off-diagonal entry is fixed to one. This holds even on a nonempty open parameter patch for the stipulated \(h(\Re z)\) and chiral frame.
4. A doubled positive Hamiltonian realizes precisely \(\operatorname{diag}(h,h^{-1})\) in an intrinsic holomorphic Berry frame and preserves the original arithmetic amplitude in one sector. It cancels determinant curvature, but has not acquired the required chiral \(tt^*\) structure.
5. Positive rank-two \(tt^*\) metrics can reproduce \(h(\sigma)\) on the real coupling axis after changing its complex extension. An explicit local semisimple example is given below. This preserves the real norm only; it does not yet preserve the arithmetic transition amplitude or specify a quantum field theory.

These are exact analytic deductions, with no numerical positivity estimate. They concern ordinary finite-rank chiral-parameter \(tt^*\), not periodic systems with an infinite operator fiber, vector-multiplet/Bogomolny geometry, or every possible interacting completion. No positivity of the complete Weil form is inferred.

## 1. Arithmetic data and conventions

Fix a finite set of primes \(S\), and define for \(\Re z>0\)
\[
\Lambda_S(z)=\pi^{-z/2}\Gamma(z/2)
\prod_{p\in S}(1-p^{-z})^{-1}.
\]
Write \(z=\sigma+i\eta\), and set
\[
h(\sigma)=\Lambda_S(\sigma)>0,\qquad u(\sigma)=\log h(\sigma).
\]
The existing finite-prime benchmark has a fixed positive Hilbert space, a self-adjoint multiplication operator
\[
X=\frac y2-\sum_{p\in S}n_p\log p-\frac{\log\pi}{2},
\]
and the chosen holomorphic state family
\[
\Psi_z(y,\mathbf n)=e^{zX/2}e^{-e^y/2}.
\]
Its norm and complete overlap are
\[
\|\Psi_z\|^2=h(\Re z),\qquad
\langle\Psi_z,\Psi_w\rangle
=\Lambda_S\!\left(\frac{\bar z+w}{2}\right).
\]
At a real coupling, the observable satisfies
\[
\langle\Psi_\sigma,e^{i\tau X}\Psi_\sigma\rangle
=\Lambda_S(\sigma+i\tau).
\]
The variable \(\tau\) is the arithmetic observable parameter; it is not automatically the partner coupling \(\eta\).

The strictly positive variance is
\[
V(\sigma)=u''(\sigma)
=\frac14\psi_1(\sigma/2)
+\sum_{p\in S}\frac{(\log p)^2p^{-\sigma}}{(1-p^{-\sigma})^2}>0.
\]
Consequently
\[
\partial_z\partial_{\bar z}\log h(\Re z)=\frac14V(\sigma).
\]
These identities concern the physical coherent-state norm. The squared transition amplitude \(|\Lambda_S(\sigma+i\tau)|^2\) is a different object.

For a holomorphic frame of a rank-\(N\) bundle, write its positive metric as \(g\), the Chern connection as
\[
D_z=\partial_z+A_z,\qquad A_z=g^{-1}\partial_zg,
\qquad D_{\bar z}=\partial_{\bar z},
\]
and define
\[
\mathcal K=\partial_{\bar z}(g^{-1}\partial_zg).
\]
Thus \([D_z,D_{\bar z}]=-\mathcal K\). The physical metric adjoint is
\[
C^{\dagger_g}=g^{-1}C^*g,
\]
where the star on a matrix is conjugate transpose. We use the \(tt^*\) convention
\[
\boxed{\quad \partial_{\bar z}C=0,
\qquad \mathcal K=[C,C^{\dagger_g}].\quad}
\]
It is equivalent to flatness of \(D_z+\zeta^{-1}C\) and \(D_{\bar z}+\zeta C^{\dagger_g}\) in one complex dimension. Overall curvature sign conventions differ in the literature; the displayed convention is used consistently throughout.

The ordinary chiral-parameter equation is derived from four-supercharge invariance by [Sonner–Tong, *Berry Phase and Supersymmetry*](https://arxiv.org/pdf/0810.1280). Its applicability requires the actual parameter multiplet and physical Berry connection. Four formal supercharges, without that parameter structure, do not establish the equation. [Dubrovin](https://arxiv.org/pdf/hep-th/9206037) gives the associated integrable metric formulation. The restrictions below follow directly from the displayed equations.

## 2. A determinant restriction, not a restriction on every component

Taking a finite-dimensional trace gives
\[
\partial_z\partial_{\bar z}\log\det g
=\operatorname{tr}[C,C^{\dagger_g}]=0.
\]
Hence locally
\[
\det g=|d(z)|^2
\]
for a nonzero holomorphic function \(d\). On the simply connected right half-plane this conclusion is global whenever the metric and frame are globally defined there. A holomorphic frame adjustment can set the determinant to one.

This immediately excludes prescribing
\[
\det g=h(\sigma)^a|d(z)|^2,
\qquad a\in\mathbb R\setminus\{0\},
\]
because its logarithmic curvature is \(aV/4\ne0\). In particular, tensoring a finite-rank \(tt^*\) bundle with the original arithmetic line multiplies its metric by \(h\) and creates determinant curvature \(NV/4\). Merely adding the same arithmetic norm to every vacuum is not a chiral \(tt^*\) extension.

This does not exclude \(h\) as one matrix component. The positive metric
\[
g_\pm=\begin{pmatrix}h&0\\0&h^{-1}\end{pmatrix}
\]
has determinant one. With the fixed holomorphic bilinear pairing
\[
\eta=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\]
it also satisfies the algebraic reality relation
\[
(\eta^{-1}g_\pm)\overline{(\eta^{-1}g_\pm)}=I.
\]
Thus determinant, positivity, and algebraic reality alone permit this repair. Its differential/Higgs compatibility remains an independent test.

The physical meaning is straightforward: extra states must carry compensating curvature. They need not carry negative norms. However, prescribing such compensation in a metric is not the same as deriving it from a supersymmetric action and a physically fixed source.

## 3. A finite-rank obstruction for ambient-holomorphic vacuum frames

Let \(\mathscr H\) be a fixed positive Hilbert space. Suppose a finite vacuum frame is given by holomorphic \(\mathscr H\)-valued vectors
\[
T(z):\mathbb C^N\longrightarrow\mathscr H,
\qquad \partial_{\bar z}T=0,
\qquad g=T^*T>0.
\]
Assume the derivatives exist in Hilbert norm. Let
\[
P=Tg^{-1}T^*
\]
be the orthogonal projection onto the vacuum span. Direct differentiation gives
\[
\boxed{\quad
\mathcal K=g^{-1}(\partial_zT)^*(I-P)(\partial_zT).
\quad}
\]
For completeness, \(\partial_zg=T^*T'\) and \(\partial_{\bar z}g=T'^*T\), so
\[
\begin{split}
\partial_{\bar z}(g^{-1}\partial_zg)
&=-g^{-1}T'^*Tg^{-1}T^*T'+g^{-1}T'^*T'\\
&=g^{-1}T'^*(I-P)T'.
\end{split}
\]
In particular,
\[
\operatorname{tr}\mathcal K
=\|(I-P)T'g^{-1/2}\|_{\mathrm{HS}}^2\ge0.
\]
Ordinary finite-rank \(tt^*\) requires this trace to vanish. Therefore
\[
(I-P)T'=0,\qquad \mathcal K=0.
\]
Differentiating \(P\) then gives \(\partial_zP=0\); its adjoint gives \(\partial_{\bar z}P=0\). The vacuum subspace is constant on each connected parameter region. The chiral matrices must also satisfy \([C,C^{\dagger_g}]=0\).

**Application to the benchmark.** The family \(\Psi_z\) does not lie in any fixed finite-dimensional subspace. To prove this, project to the component \(n_p=0\) for all primes. For distinct positive real numbers \(\sigma_j\), the projected vectors are nonzero scalar multiples of
\[
e^{\sigma_j y/4}e^{-e^y/2}.
\]
Any finite linear dependence would, after division by the nonzero common factor, give a dependence among exponentials \(e^{\sigma_j y/4}\). Differentiating at one point produces a Vandermonde system, so every coefficient vanishes. Arbitrarily large independent sets exist, even on an arbitrarily small open coupling interval.

It follows that no finite-rank ordinary chiral \(tt^*\) extension can contain this full coherent family while representing **all** its physical vacuum-frame vectors holomorphically in one fixed positive ambient Hilbert space.

This hypothesis is substantive. An intrinsic holomorphic vacuum frame only obeys \(P\partial_{\bar z}T=0\); its derivatives in the massive complement need not vanish. Physical \(tt^*\) states generally can have precisely that nonholomorphic ambient dependence. Infinite rank also requires separate trace and domain analysis. The argument does not exclude either possibility.

## 4. The Gauss identity explains what remains possible

Let \(v(z)\) be a nonzero intrinsic holomorphic section of a general Hermitian bundle \((E,g)\), and let \(L\) be the line it spans. Write
\[
h_v=\langle v,v\rangle_g,\qquad
\beta=(I-P_L)D_zv.
\]
The line-curvature identity, in the convention above, is
\[
\partial_z\partial_{\bar z}\log h_v
=\frac{\langle v,\mathcal Kv\rangle_g}{h_v}
+\frac{\|\beta\|_g^2}{h_v}.
\]
It can be checked at a point in a holomorphic normal frame: the second derivative of the norm splits into ambient curvature and the derivative orthogonal to the line.

If the full bundle satisfies \(tt^*\), this becomes
\[
\boxed{\quad
\partial_z\partial_{\bar z}\log h_v
=\frac{\|C^{\dagger_g}v\|_g^2-\|Cv\|_g^2+\|\beta\|_g^2}{h_v}.
\quad}
\]
Thus a positive curvature \(V/4\) for the arithmetic line is not by itself an obstruction at rank two or higher. Chiral mixing and the line's variation inside the vacuum space can supply it. The trace restriction constrains the **complete vacuum bundle**, not every line inside it.

Conversely, matching only \(g_{11}=h\) supplies no complete overlap kernel and no action of the arithmetic operator \(X\). A matrix component, determinant, line subbundle, and full physical state family are different data. No conclusion about the transition amplitude follows from a component identity alone.

## 5. A doubled positive Hamiltonian cancels determinant curvature

The benchmark's chosen physical complex family is
\[
H_{\sigma,\eta}=e^{i\eta X/2}H_\sigma e^{-i\eta X/2},
\]
with its supercharges and domains conjugated by the same unitary. Let complex conjugation in the original real coordinate representation be \(K\). Consider the positive direct-sum system
\[
\widetilde H_{\sigma,\eta}
=H_{\sigma,\eta}\oplus H_{\sigma,-\eta}.
\]
Its two physical zero states span
\[
(\Psi_z,0),\qquad (0,K\Psi_z).
\]
The second state is antiholomorphic in the ambient Hilbert space. An intrinsic holomorphic Berry frame is
\[
e_1=(\Psi_z,0),\qquad
e_2=h(\sigma)^{-1}(0,K\Psi_z).
\]
Indeed the projection of \(\partial_{\bar z}K\Psi_z\) onto its own line is \((\partial_{\bar z}\log h)K\Psi_z\), canceled by the derivative of \(h^{-1}\). Both frame vectors therefore obey \(P\partial_{\bar z}e_i=0\).

In this frame,
\[
g=\operatorname{diag}(h,h^{-1}),\qquad
A_z=\operatorname{diag}(\partial_z u,-\partial_z u),\qquad
\mathcal K=\operatorname{diag}(V/4,-V/4).
\]
The determinant connection is flat, and every physical norm is positive. Keeping the arithmetic source in the first summand and using \(X\oplus X\) preserves exactly
\[
\langle e_1(\sigma),e^{i\tau(X\oplus X)}e_1(\sigma)\rangle
=\Lambda_S(\sigma+i\tau).
\]

This is a concrete positive rank-two metric construction that escapes the ambient-holomorphic theorem. It is still a reducible direct-sum system with the original supersymmetry. It has not been shown to admit physical chiral parameter multiplets or a \(tt^*\) Higgs field. The next section tests the standard two-vacuum Higgs choice and finds an obstruction.

## 6. The standard reciprocal-diagonal two-vacuum repair fails

Keep the fixed holomorphic frame and
\[
g=\operatorname{diag}(h(\sigma),h(\sigma)^{-1}),\qquad
\kappa(\sigma)=V(\sigma)/4>0.
\]
For
\[
C=\begin{pmatrix}0&a(z)\\b(z)&0\end{pmatrix},
\]
one obtains
\[
C^{\dagger_g}
=\begin{pmatrix}0&\bar b\,h^{-2}\\\bar a\,h^2&0\end{pmatrix},
\qquad
[C,C^{\dagger_g}]
=\begin{pmatrix}
|a|^2h^2-|b|^2h^{-2}&0\\
0&-|a|^2h^2+|b|^2h^{-2}
\end{pmatrix}.
\]
An identity matrix added to \(C\) does not affect the equation. This off-diagonal form is also compatible with \(\eta C\) being symmetric for \(\eta=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\).

### Either companion orientation is obstructed

The two standard companion normalizations are
\[
C_+(z)=\begin{pmatrix}0&1\\q(z)&0\end{pmatrix},
\qquad
C_-(z)=\begin{pmatrix}0&q(z)\\1&0\end{pmatrix},
\]
where \(q\) is arbitrary holomorphic. They correspond to different identifications of the unit/generator with the two basis vectors. The \(tt^*\) equation requires, respectively,
\[
|q(z)|^2=R_+(\sigma):=h^4-\kappa h^2,
\]
or
\[
|q(z)|^2=R_-(\sigma):=\kappa h^{-2}+h^{-4}.
\]
On a region where a holomorphic \(q\) is nonzero, \(\log|q|^2\) is harmonic. Since the right side depends only on \(\sigma\), a necessary condition is
\[
R_\pm R_\pm''-(R_\pm')^2=0.
\]
Equivalently, each positive \(R_\pm\) must have exponential dependence on \(\sigma\). If \(q\) vanishes identically on a patch, the corresponding \(R\) must vanish there instead.

For the arithmetic \(h\), neither possibility occurs. Stirling and polygamma asymptotics give, for fixed finite \(S\),
\[
u(\sigma)=\frac\sigma2\log\frac{\sigma}{2\pi e}
-\frac12\log\sigma+O(1),\qquad
V(\sigma)=\frac1{2\sigma}+O(\sigma^{-2}).
\]
The finite-prime corrections and their fixed-order derivatives decay exponentially. The standard gamma expansions and their differentiated forms are recorded in [DLMF §5.11](https://dlmf.nist.gov/5.11) and [§5.15](https://dlmf.nist.gov/5.15).

In particular \(h\) grows faster than every fixed exponential as \(\sigma\to\infty\). Thus
\[
\begin{split}
R_+&=h^4(1-\kappa h^{-2}),
& (\log R_+)''&=\frac2\sigma+O(\sigma^{-2}),\\
R_-&=\kappa h^{-2}(1+\kappa^{-1}h^{-2}),
& (\log R_-)''&=-\frac1\sigma+O(\sigma^{-2}).
\end{split}
\]
The factors involving \(h^{-2}\) and their first two derivatives are negligible relative to the displayed terms. Hence neither logarithmic second derivative vanishes at large \(\sigma\).

This also excludes equality on an arbitrary nonempty open parameter patch. The functions \(R_\pm\) and \(R_\pm R_\pm''-(R_\pm')^2\) are real analytic on the connected interval \((0,\infty)\). Vanishing on an open interval would extend throughout that interval and contradict the large-\(\sigma\) calculation. An identically zero \(q\) likewise contradicts the positive large-\(\sigma\) behavior of \(R_\pm\).

The obstruction applies to the stipulated reciprocal-diagonal metric, arithmetic complex extension \(h(\Re z)\), and companion normalization. It does not cover every holomorphic pair \(a,b\), every non-diagonal metric, or a different complex extension retaining the real-axis norms. Holomorphic changes of frame also change metric components and source normalization; they cannot be invoked while claiming all those data were kept fixed.

This is a normal \(tt^*\) compatibility test, not a contradiction to positive rank-two \(tt^*\) geometry itself. Positive rank-two constructions and their normalization/reality conditions are studied, for example, by [Takahashi, *tt* Geometry of Rank 2](https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1430.pdf). Two explicit controls follow.

## 7. Positive rank-two controls and a local semisimple embedding

### A simple nilpotent control

On \(\Re w=r>0\), set
\[
g_0(w,\bar w)=\operatorname{diag}((2r)^{-1},2r),
\qquad
C_0=\begin{pmatrix}0&1\\0&0\end{pmatrix}.
\]
The first curvature entry is
\[
\frac14\frac{d^2}{dr^2}\log(1/(2r))=\frac1{4r^2},
\]
which equals the first commutator entry \((2r)^{-2}\). The second entries have opposite sign. The metric is positive, has determinant one, and obeys the reality relation with \(\eta\) above.

The holomorphic pullback
\[
w(z)=\frac1{2\Lambda_S(z)},\qquad
C_z=w'(z)C_0
\]
therefore defines a positive \(tt^*\) solution on the component of \(\Re w(z)>0\) containing the relevant real couplings. Its first metric component equals \(\Lambda_S(\sigma)\) when \(z=\sigma\) is real.

This construction uses a nonzero nilpotent chiral matrix. It is not the semisimple chiral ring expected for a collection of isolated massive Landau–Ginzburg vacua. The following refinement avoids that particular objection, while retaining the distinction between metric equations and a microscopic theory.

### A semisimple control

Still on \(r=\Re w>0\), define
\[
g_*(w,\bar w)
=\operatorname{diag}(\coth(2r),\tanh(2r)),
\qquad
C_*=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
Writing \(h_*(r)=\coth(2r)\), direct differentiation yields
\[
\frac14\frac{d^2}{dr^2}\log h_*
=\frac{4\cosh(4r)}{\sinh^2(4r)}
=h_*^2-h_*^{-2}.
\]
Thus this is an exact positive ordinary \(tt^*\) metric. The chiral matrix has distinct eigenvalues \(\pm1\); \(\eta C_*\) is symmetric, and determinant and reality conditions hold. With an additional identity coupling acting by \(I\), the algebraic multiplication can be written as \(\phi^2=1\). These facts do not assert a microscopic field theory with the desired physical asymptotic conditions.

Near \(\sigma_0=1/2\), the arithmetic function obeys \(h(\sigma_0)>1\) and \(h'(\sigma_0)<0\). The first inequality is elementary: \(e^{-t}>1-t\) on \((0,1)\) gives
\[
\Gamma(1/4)>\int_0^1t^{-3/4}(1-t)\,dt=16/5,
\]
while \(\pi^{1/4}<2\), and every finite Euler factor exceeds one. For the derivative,
\[
u'(1/2)=\tfrac12\psi(1/4)-\tfrac12\log\pi
-\sum_{p\in S}\frac{\log p}{\sqrt p-1}<0,
\]
using \(\psi(1/4)=-\gamma-\pi/2-3\log2<0\).

Consequently the local holomorphic function
\[
\boxed{\quad
w(z)=\frac12\operatorname{arccoth}\Lambda_S(z)
=\frac14\log\frac{\Lambda_S(z)+1}{\Lambda_S(z)-1}
\quad}
\]
has a branch with \(\Re w>0\) in a neighborhood of \(z=1/2\). Its derivative is nonzero there after shrinking the neighborhood. Pull back \(g_*\) and \(C_*\):
\[
g_{\rm new}(z,\bar z)=g_*(w(z),\overline{w(z)}),
\qquad
C_z=w'(z)C_*.
\]
Holomorphic pullback multiplies both sides of the curvature equation by \(|w'|^2\), so the \(tt^*\) equation is preserved. On the real axis,
\[
\boxed{\quad
(g_{\rm new})_{11}(\sigma,\sigma)=\Lambda_S(\sigma).
\quad}
\]
The chiral matrix has distinct eigenvalues \(\pm w'(z)\) on this local region. It is therefore semisimple, not merely the nilpotent control in disguise.

### What this embedding does and does not establish

The extension \((g_{\rm new})_{11}(z,\bar z)\) is **not** \(h(\Re z)\). The imaginary-part dependence has changed. This is why it evades the reciprocal-diagonal companion obstruction without contradicting it.

Only the real-axis diagonal norm has been retained. The complete cross-parameter overlap \(\Lambda_S((\bar z+w)/2)\), the real-state vectors \(\Psi_\sigma\), the self-adjoint observable \(X\), and its exact transition amplitude have not been constructed for this pulled-back metric. A metric norm along a curve does not determine any of those objects.

Nor does the construction select the arithmetic normalization. Any positive real-analytic function with values greater than one and nonzero derivative near a point can be inserted into the same local pullback. Multiplying \(h(\sigma)\) by \(e^{c\sigma}\) changes its first logarithmic derivative by \(c\), and on a suitable small neighborhood the same construction still works. The constant responsible for the arithmetic contact is therefore not determined by positive \(tt^*\) compatibility alone.

The domain is local: \(\Lambda_S\pm1\) must remain nonzero and the chosen \(\operatorname{arccoth}\) branch must have positive real part. No global half-plane, all-prime limit, massive quantum field theory, or physical ultraviolet/infrared/Stokes boundary condition is supplied. Semisimple algebra is one necessary compatibility feature; it is not a substitute for those physical data.

## 8. Implications for the next construction

The results separate two exact but presently different successes:

| Construction | Retains exact arithmetic amplitude | Positive physical Hamiltonian specified | Ordinary chiral \(tt^*\) metric established |
|---|---|---|---|
| Original coherent family | Yes | Yes | Rank-one chosen extension obstructed |
| Direct sum with its conjugate | Yes, in the first summand | Yes | Standard companion choice obstructed |
| Local semisimple pullback | Not established; only the real norm is retained | Not supplied by the pullback | Yes, as a positive metric/Higgs solution |

The next non-Abelian task is not to fit another positive matrix component. It is to construct a physical source and arithmetic observable for an extended theory and derive the same complete transition pairing, while giving the partner-parameter dependence a genuine supersymmetric origin. Additional ground states must have the ambient nonholomorphic response required to evade the finite-rank holomorphic-frame theorem, or the construction must leave that finite-rank setting.

Even that result would not yet produce the full Weil norm. The first normal logarithmic derivative, its physical normalization, and the two pole residues remain to be converted into an ordinary positive pairing. The constructions here do not supply the pole kernel, and their determinant condition does not fix a source-frame contact term. Their value is that they identify precisely which extensions are impossible, which metric-level extensions are possible, and which physical identity is still missing.

## Sources

The local benchmark formulas are reproduced above from the preceding arithmetic ground-state survey. All new compatibility arguments and explicit control solutions in this note are direct derivations. They have not undergone independent specialist review.

1. Julian Sonner and David Tong. [*Berry Phase and Supersymmetry*](https://arxiv.org/pdf/0810.1280), 2008/2009. Chiral-parameter \(tt^*\) and vector-parameter Bogomolny constraints.
2. Boris Dubrovin. [*Geometry and Integrability of Topological-Antitopological Fusion*](https://arxiv.org/pdf/hep-th/9206037), 1992/1993. Hermitian metric and integrable formulation.
3. Atsushi Takahashi. [tt* Geometry of Rank 2](https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1430.pdf). Rank-two positivity, reciprocal metrics, and reality/normalization distinctions. The existence results in that paper are not invoked as existence of a physical arithmetic theory.
4. NIST Digital Library of Mathematical Functions. [Gamma asymptotics, §5.11](https://dlmf.nist.gov/5.11) and [polygamma functions, §5.15](https://dlmf.nist.gov/5.15). Used for the explicit large-coupling obstruction.

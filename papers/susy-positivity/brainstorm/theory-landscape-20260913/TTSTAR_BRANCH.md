# Supersymmetric ground-state metrics as a route to Weil positivity

## Assessment

The strongest fit within this branch is **a unitary supersymmetric theory whose arithmetic observable belongs to an infinite-dimensional boundary or defect sector and whose Hermitian pairing is constrained by non-Abelian \(tt^*\) geometry**. This is a promising architecture, not an identified theory reproducing the Weil form. No source examined supplies the missing arithmetic identification.

The most concrete next model is the twisted-mass \(\mathbb{CP}^1\) sigma model and its exponential Landau–Ginzburg mirror. It can test whether interacting ground-state geometry changes the observable in the required manner. It cannot, through its two-dimensional vacuum fiber alone, represent the complete input space. A separate attractive alternative is the infinite chiral-operator tower of four-dimensional \(\mathcal N=2\) superconformal QCD, where physical positive norms obey nonlinear equations.

Four deductions substantially narrow the search:

1. A finite vacuum fiber cannot carry an all-input Weil pairing through ground-state projection alone. Periodic models can have an infinite collection of lifted vacua, so the fiber rank must be distinguished from the total sector space.
2. A fixed finite-rank flavor torus cannot generate all prime frequencies by identifying the arithmetic Fourier variable with a single flavor-holonomy trajectory. This is an exact arithmetic restriction on that identification, not an objection to interactions.
3. A gamma function in a holomorphic brane amplitude is not yet a gamma kinetic norm. Taking its logarithmic derivative is an additional operation that does not generally preserve positivity.
4. The simplest physical periodic metric has Bessel winding weights; the bare Euler prime repetitions have different weights. Non-Abelian interactions add further mixed sectors that must be explained, rather than presumed helpful.

Statements explicitly identified as **literature** below summarize primary sources. Statements labeled **deduction** are arguments made here. Candidate extensions and tests are **proposals**, not established models of RH.

## 1. Exact target and the role of a ground-state metric

Let \(I_L=(-L/2,L/2)\), let \(E_L\) extend by zero to the real line, and write \(F=E_Lf\). The Fourier transform is \(\widehat F(\tau)=\int F(x)e^{-i\tau x}\,dx\). The target supplied by the local research program is

\[
\begin{split}
Q_{0,L}[f]={}&\frac1{2\pi}\int_{\mathbb R}B(\tau^2)|\widehat F(\tau)|^2\,d\tau
+w_0\|f\|^2+2|C(f)|^2-2|S(f)|^2\\
&-\sum_{m\log p<L}(\log p)p^{-m/2}
\langle f,(T_{m\log p}+T_{m\log p}^*)f\rangle,
\end{split}
\]

\[
\begin{gathered}
B(s)=\Re\psi(\tfrac14+i\sqrt{s}/2)-\psi(\tfrac14)
=\sum_{k\ge0}\frac2{a_k}\frac{s}{s+a_k^2},\qquad a_k=2k+\tfrac12,\\
w_0=\psi(\tfrac14)-\log\pi,\qquad T_d=E_L^*U_dE_L,\quad U_dF(x)=F(x-d),\\
C(f)=\int f(x)\cosh(x/2)\,dx,\qquad S(f)=\int f(x)\sinh(x/2)\,dx.
\end{gathered}
\]

The form domain is
\[
\mathcal D_{\log,L}=\left\{f\in L^2(I_L):
\int\log(2+|\tau|)|\widehat{E_Lf}(\tau)|^2\,d\tau<\infty\right\}.
\]
The operator is a form compression of whole-line dynamics; the auxiliary theory is not automatically confined to \(I_L\).

The intended structural proof would specify a unitary theory, a physical state \(\Omega\), and a linear, densely defined state map \(\Gamma_L\), independently of the unknown sign of \(Q\), and derive
\[
Q_{0,L}(f,g)=\langle\Gamma_Lf,\Gamma_Lg\rangle_{\mathscr H}.
\]
For a correlation-function realization, \(\Gamma_Lf=\mathcal O_L(f)\Omega\). For a ground-state realization, it may instead be \(\Gamma_Lf=P_0\mathcal B_L(f)\Omega\), where \(P_0\) is the physical orthogonal ground-state projection. An interacting Hamiltonian does not prevent either expression from being quadratic in \(f\).

The coordinates must remain distinct. The arithmetic coordinate is \(x\), its Fourier variable is \(\tau\), physical Euclidean preparation time is separate, and the supersymmetric coupling coordinates below are \(t^i\). The \(tt^*\) auxiliary spectral parameter \(\zeta_{\mathrm{aux}}\) is unrelated to the Riemann zeta function.

## 2. What \(tt^*\) contributes

**Literature.** For a massive unitary two-dimensional \(\mathcal N=(2,2)\) theory on a circle, supersymmetric vacua form a bundle over coupling space. Chiral multiplication acts by matrices \(C_i\). Its ordinary Hermitian metric \(g\) differs from the holomorphic bilinear topological pairing \(\eta\). With conventions absorbing circle length into the couplings, the equations include
\[
\begin{gathered}
[D_i,D_j]=[\bar D_i,\bar D_j]=0,\qquad
[\bar D_i,C_j]=0,\qquad D_iC_j=D_jC_i,\\
[D_i,\bar D_j]=-[C_i,\bar C_j].
\end{gathered}
\]
Here \(\bar C_j\) is the physical metric adjoint. They amount to flatness of
\[
\nabla_i(\zeta_{\mathrm{aux}})=D_i+\zeta_{\mathrm{aux}}C_i,
\qquad
\bar\nabla_j(\zeta_{\mathrm{aux}})=\bar D_j+\zeta_{\mathrm{aux}}^{-1}\bar C_j.
\]
These equations constrain the coupling dependence of genuine norms. They do not turn the topological pairing or a supersymmetric index into a norm. [Cecotti–Vafa, 1991, especially the formulation of the vacuum metric and its equations.][1]

**Literature.** Dubrovin gives an integrable and isomonodromic formulation, relating positive solutions to maps into the space of positive quadratic forms. Positivity is specified in the geometric data; arbitrary algebraic solutions do not become positive merely because the differential equations hold. [Dubrovin, 1992, §§1–3.][2]

**Deduction: formal SUSY constraints do not replace a physical realization.** In a scalar constant example, take \(\eta=1\), \(g=-1\), zero connections, and constant scalar \(C\). The curvature and commutator equations vanish. The usual algebraic reality relation \((\eta^{-1}g)\overline{(\eta^{-1}g)}=1\) also holds. The metric remains negative. This example is not a unitary quantum theory; it shows why solving the displayed equations plus the algebraic reality relation is insufficient.

More supersymmetry is useful when it supplies equations that determine a previously uncontrolled metric from independently known physical data. It provides no automatic arithmetic selection principle. The model's operator algebra, ultraviolet and infrared conditions, normalizations, normalizable states, and allowed couplings still have to be specified.

## 3. The gamma connection: useful, but weaker than a norm identity

**Literature.** The basic periodic example
\[
W(Y)=\mu Y-e^Y
\]
is a mirror of a massive two-dimensional chiral multiplet. The physical periodic \(tt^*\) metric and its brane amplitudes are different quantities. In an asymmetric limit, a normalized branch of a brane amplitude obeys
\[
\log\Pi(\theta,\mu,0)
=\log\Gamma(\mu+\theta)-\theta\log\mu-\tfrac12\log(2\pi),
\qquad 0\le\theta\le1.
\]
Sending the antiholomorphic mass to zero at fixed nonzero holomorphic mass leaves the physical conjugate-mass locus. Boundary states entering brane amplitudes also need not be normalizable. The same paper identifies the richer mirror
\[
W(Y)=\mu Y-e^{t/2+Y}+e^{t/2-Y}
\]
with the twisted-mass \(\mathbb{CP}^1\) sigma model; its periodic vacuum geometry is non-Abelian. These facts make useful benchmarks, not arithmetic norm identities. [Cecotti–Gaiotto–Vafa, §§2.1, 3.1–3.2 and Appendix A.][3]

**Deduction: the exact operation needed to reach the gamma kinetic term.** Define, for \(a>0\),
\[
\mathcal A(a,\tau)
=\log\Gamma(a+i\tau/2)+\log\Gamma(a-i\tau/2)-2\log\Gamma(a).
\]
Then
\[
\frac12\partial_a\mathcal A(a,\tau)
=\Re\psi(a+i\tau/2)-\psi(a).
\]
At \(a=1/4\) this is \(B(\tau^2)\). Thus even an exact gamma amplitude must be converted by a subtraction and a parameter derivative into the desired kernel. Positive norms are not preserved by a general logarithmic derivative: the positive scalar metric \(g(a)=e^{-a}\) has \(\partial_a\log g=-1\).

For the actual gamma function, the required sign is established by the special partial-fraction identity
\[
\Re\psi(a+it)-\psi(a)
=\sum_{n=0}^{\infty}\frac{t^2}{(n+a)((n+a)^2+t^2)}\ge0.
\]
This derivation uses the digamma series, not positivity of an arbitrary brane amplitude. [DLMF, digamma series.][10]

An eventual \(tt^*\) proposal must identify a physical observable whose **ordinary pairing already equals** this derivative, or supply a separate structural identity proving that conversion. Reproducing \(\Gamma\) somewhere in a partition function does not perform that step.

## 4. Periodic vacua, their positive metric, and the winding mismatch

**Literature.** On the lifted periodic theory there are vacua indexed by \(k\in\mathbb Z\). In a Bloch representation the metric takes the form
\[
g_{k\bar h}=\int_0^{2\pi}\frac{d\theta}{2\pi}
e^{i(h-k)\theta}G(\theta),\qquad G(\theta)>0.
\]
For the basic exponential model, writing \(G=\text{positive constant}\times e^{\mathcal L}\), the real odd periodic function \(\mathcal L\) satisfies a radial linear equation. Its decaying modes are
\[
\mathcal L(\theta,M)=\sum_{m\ge1}\gamma_m\sin(m\theta)K_0(mM).
\]
The coefficients are fixed by physical boundary data. A differentiated quantity called the CFIV index involves \(mM K_1(mM)\); it is not the metric itself. [Cecotti–Neitzke–Vafa, Appendix A.2.][4]

**Deduction: the rank qualification.** At a fixed Bloch angle the basic fiber is one-dimensional; the entire lifted lattice is infinite-dimensional. Indeed, for a finite coefficient sequence \(v_k\),
\[
\sum_{k,h}\bar v_k g_{k\bar h}v_h
=\int_0^{2\pi}\frac{d\theta}{2\pi}G(\theta)
\left|\sum_k v_ke^{ik\theta}\right|^2\ge0.
\]
Periodic \(tt^*\) therefore has a real route to infinitely many input directions. To use it for the Weil form, one still has to derive the map from \(f\) to those directions; choosing it through the unknown square root of the target would be circular.

**Deduction: the weights do not yet match prime repetitions.** For one prime, set \(\ell=\log p\). The required frequency contribution is
\[
-2\ell\sum_{m\ge1}e^{-m\ell/2}\cos(m\ell\tau).
\]
Identifying \(\theta=\ell\tau\) and \(M=\ell/2\) in a periodic metric instead produces Bessel weights. Their large-repetition behavior contains
\[
K_0(mM)\sim \sqrt{\frac{\pi}{2mM}}e^{-mM},
\]
with a nonconstant prefactor and further inverse powers. The required Euler coefficients have no such prefactor. Differentiating changes Bessel order and powers, but does not by itself establish exact equality. Moreover the metric is \(G=e^{\mathcal L}\), rather than \(\mathcal L\); exponentiating creates mixed winding contributions.

This mismatch is scoped to the naive identification. A physically derived integral transform, different observable, or different dimensional mechanism could change the weights. Such an operation must preserve an ordinary norm interpretation and be derived before its asymptotics are used as evidence.

## 5. A frequency obstruction for a fixed finite flavor torus

**Deduction: a separate finite-fiber rank test.** If every prepared state belongs to one fixed vacuum fiber of dimension \(N\), write \(\Gamma_Lf=\sum_{j=1}^N\lambda_j(f)e_j\). Every resulting input Gram matrix has rank at most \(N\), since
\[
Q(f,h)=\sum_{i,j=1}^N\overline{\lambda_i(f)}g_{ij}\lambda_j(h).
\]
The target form has infinite rank. One way to see this is that the gamma form domain, equipped with its graph norm, embeds compactly into \(L^2(I_L)\): its Fourier tail is uniformly bounded by a constant divided by \(\log R\), and its spatial support is bounded. The standard translation-compactness criterion then gives compactness. The associated gamma operator has compact resolvent on an infinite-dimensional input space and eigenvalues tending to infinity. The remaining fixed-\(L\) terms are bounded, so the full operator retains this property. A fixed finite vacuum fiber cannot represent it. Infinite lifted sectors, surviving boundary fields, or states outside the ground fiber escape this test; an arbitrary continuum of parameter labels without a specified common inner product does not.

**Deduction.** Assume a candidate makes the arithmetic Fourier parameter enter only through a one-parameter subgroup of a rank-\(r\) flavor torus,
\[
\theta_j(\tau)=\alpha_j\tau+\theta_{j,0},\qquad j=1,\ldots,r.
\]
A charge \(\mathbf n\in\mathbb Z^r\) then contributes frequency \(\mathbf n\cdot\boldsymbol\alpha\). Products, winding repetitions, and charge-preserving interactions retain frequencies in
\[
\Lambda_\alpha=\left\{\sum_{j=1}^r n_j\alpha_j:n_j\in\mathbb Z\right\}.
\]
For absolutely convergent Fourier expansions, or for a specified distributional expansion admitting unique coefficient extraction, this is an exact selection rule. If all prime harmonics are to be identified in this manner, every \(\log p\) must belong to \(\operatorname{span}_{\mathbb Q}\{\alpha_1,\ldots,\alpha_r\}\).

But the numbers \(\log p\), over distinct primes, are linearly independent over \(\mathbb Q\). A finite rational relation can be cleared of denominators and exponentiated:
\[
\sum_p n_p\log p=0
\quad\Longrightarrow\quad
\prod_p p^{n_p}=1
\quad\Longrightarrow\quad n_p=0\ \text{for every }p.
\]
The last implication is unique factorization. Therefore the stated identification cannot generate all prime phases in one fixed finite-rank theory.

This conclusion concerns a **frequency-matching ansatz**, not every interval-compressed quantum construction. It does not exclude nonlinear excitation energies, an infinite charge group, a non-holonomy observable map, or an independently derived representation that is not a flavor Fourier series. At a fixed finite cutoff only finitely many primes occur, but a construction whose rank grows with the prime cutoff needs a coherent limiting theory. The analogous statement for BPS central charges requires the additional assumption that the relevant central charges are aligned on one ray and proportional to \(\log p\); their absolute values alone need not obey the same rational-linear argument.

## 6. Non-Abelian \(tt^*\), BPS data, and the Euler temptation

**Literature.** In massive two-dimensional theories, signed soliton degeneracies determine Stokes data and the asymptotics of the vacuum metric. The degeneracies are weighted indices, not automatically dimensions of positive sectors. Nonlinear soliton expansions reconstruct more than the leading exponential. [Cecotti–Vafa, classification, §§2–4.][5]

**Literature.** Coupled two-dimensional/four-dimensional systems extend this picture to surface-defect vacuum bundles with hyperholomorphic connections. One central equation has the schematic exact structure
\[
\log\frac{X_\gamma(\zeta_{\mathrm{aux}})}{X^{\rm sf}_\gamma(\zeta_{\mathrm{aux}})}
=\frac{1}{4\pi i}\sum_{\gamma'}\Omega(\gamma')\langle\gamma',\gamma\rangle
\int_{\ell_{\gamma'}}\frac{d\zeta'}{\zeta'}
\frac{\zeta'+\zeta_{\mathrm{aux}}}{\zeta'-\zeta_{\mathrm{aux}}}
\log(1-X_{\gamma'}(\zeta')),
\]
with additional coupled equations for defect sections. Reality conditions use a physical Hermitian frame. The source assumes existence in the sufficiently large-radius regime for the general construction; it does not prove unrestricted existence for arbitrary prescribed BPS spectra. [Gaiotto–Moore–Neitzke, §5.6.][6]

**Deduction: why the logarithm is suggestive.** Introduce a convergent single-prime variable \(x_p=e^{-(\sigma+i\tau)\ell}\), \(\sigma>0\). Then
\[
\log(1-x_p)^{-1}=\sum_{m\ge1}\frac{x_p^m}{m},
\qquad
\partial_\sigma\log(1-x_p)^{-1}=-\ell\sum_{m\ge1}x_p^m.
\]
Twice the real part at \(\sigma=1/2\) yields precisely the single-prime coefficient. The derivative removes the repetition factor \(1/m\). This elementary identity explains why BPS logarithms, determinant expansions, and winding sectors are natural places to look.

It does **not** identify the metric. The full BPS integral includes its contour kernel, the \(\zeta'\)-dependent central-charge exponent, other charges, nonlinear dressing, and the reconstruction of the physical Hermitian pairing. The arithmetic derivative also needs a positive-observable interpretation. Assigning \(X_{\gamma_p}=p^{-(1/2+i\tau)}\) and arbitrary indices by hand supplies the desired answer rather than deriving a theory.

There is a useful tension. Mutually local primitive sectors simplify the integral equations and favor factorized Euler-like repetitions. Nonzero charge pairings generate interactions and mixed sectors. The logarithmic derivative of the zeta Euler product has support on prime powers, rather than arbitrary composite products. A non-Abelian proposal must explain how its measured quantity removes or reorganizes mixed contributions. A connected observable or a logarithm might do so combinatorially, but neither is automatically a positive norm.

### A scalar completed-amplitude bridge and its frame obstruction

**Deduction, following the finite-prime amplitude suggested by the parallel arithmetic investigation.** For a finite set of primes \(\mathcal S\), define
\[
\Lambda_{\mathcal S}(s)=\pi^{-s/2}\Gamma(s/2)
\prod_{p\in\mathcal S}(1-p^{-s})^{-1},\qquad
w_{\mathcal S}(\sigma,\tau)=|\Lambda_{\mathcal S}(\sigma+i\tau)|^2.
\]
Elementary differentiation gives
\[
\partial_\sigma\log w_{\mathcal S}
=-\log\pi+\Re\psi((\sigma+i\tau)/2)
-2\sum_{p\in\mathcal S}(\log p)\sum_{m\ge1}p^{-m\sigma}\cos(m\tau\log p).
\]
At \(\sigma=1/2\), this is exactly the gamma-plus-constant-plus-prime multiplier for the selected primes. After input compression, prime powers with translation distance at least \(L\) contribute zero. This is a precise formula, but not a positivity argument.

For finite \(\mathcal S\), \(\Lambda_{\mathcal S}\) is holomorphic and nowhere zero on \(\Re s>0\). A rank-one metric \(g=|\Lambda_{\mathcal S}|^2\) there is therefore globally a holomorphic frame rescaling of the constant metric. Its Chern curvature is
\[
-\partial\bar\partial\log g=0.
\]
More generally, replacing a holomorphic frame \(e\) by \(h(s)e\) changes
\[
g\longmapsto |h|^2g,\qquad
\partial_\sigma\log g\longmapsto
\partial_\sigma\log g+2\Re\frac{h'}h.
\]
The choice \(h(s)=e^{cs}\), \(c\in\mathbb R\), shifts the proposed multiplier by an arbitrary constant \(2c\) while leaving the curvature unchanged. Thus the normal derivative is a connection/frame-dependent quantity, not an intrinsic positive norm. A physical prescription for the state, topological normalization, and boundary preparation may fix this freedom, but that prescription is additional input that must be derived.

Nor can the pole form be appended by the naive scalar replacement \(\Lambda_{\mathcal S}(s)\mapsto s(s-1)\Lambda_{\mathcal S}(s)\). Away from the two zeros,
\[
\left.\partial_\sigma\log|s(s-1)|^2\right|_{\sigma=1/2}
=2\Re\left(\frac1{1/2+i\tau}+\frac1{-1/2+i\tau}\right)=0.
\]
The actual pole contribution has nonzero kernel \(2\cosh((x-y)/2)\) on the input interval. Reproducing it requires the appropriate contour, boundary, or distributional operation; the ordinary pointwise normal derivative above does not do so. This does not exclude a completed analytic construction, but it identifies an operation that cannot be omitted.

## 7. A concrete nonlinear benchmark and its singular limit

**Proposal.** Use the positive-metric \(\mathbb{CP}^1\) sigma model, or its controlled Landau–Ginzburg description, as the first test of the metric mechanism. A convenient holomorphic parameterization is
\[
W_\varepsilon(Y)=\mu Y-e^Y+\varepsilon e^{-Y}.
\]
For a positive Kähler metric \(h(Y,\bar Y)\), the bosonic potential is
\[
V=h^{-1}|\mu-e^Y-\varepsilon e^{-Y}|^2\ge0.
\]
The theory contains nonlinear forces and Yukawa couplings from \(W''_\varepsilon\). One must use an appropriate complete physical metric and boundary conditions; the holomorphic mirror superpotential alone does not specify every ultraviolet datum.

**Deduction.** Set \(z=e^Y\). The critical points obey
\[
z^2-\mu z+\varepsilon=0,\qquad
z_\pm=\frac{\mu\pm\sqrt{\mu^2-4\varepsilon}}2.
\]
For fixed \(\mu\ne0\), as \(\varepsilon\to0\),
\[
z_+=\mu+O(\varepsilon),\qquad
z_-=\varepsilon/\mu+O(\varepsilon^2).
\]
One critical point approaches the basic exponential vacuum. The other runs to \(Y\to-\infty\) in its real part. Consequently this is not automatically a smooth deformation of a fixed finite ground-state bundle at \(\varepsilon=0\). An extra zero-energy state can escape to infinity even though the superpotential converges on compact subsets.

The first decisive test is analytic: construct normalizable physical vacua and determine the limiting ground-state projection and selected boundary-state map. The second is to calculate the actual Hermitian pairing of specified states, not merely a thimble integral or index. A successful result would demonstrate a new controllable signed correction inside a complete positive Gram pairing. It would still need an infinite arithmetic sector and the full kernel identity.

The basic mirror's free description is a useful warning: the number of nonlinear terms in one set of fields is not an invariant measure of theoretical complexity. The relevant question is which physical correlations and selection principles the complete theory supplies.

## 8. An interacting alternative with an infinite positive operator tower

**Literature.** Four-dimensional \(\mathcal N=2\) superconformal theories have \(tt^*\)-type constraints on physical chiral-primary two-point metrics, derived from superconformal Ward identities. [Papadodimas, 2009.][7] In \(SU(2)\) gauge theory with four hypermultiplets, the chiral ring generated by \(\phi_2\) has operators \(\phi_{2n}\) and positive norm coefficients \(g_{2n}\). In conventional normalization,
\[
\langle\phi_{2n}(x)\bar\phi_{2n}(0)\rangle
=\frac{g_{2n}(u,\bar u)}{|x|^{4n}},\qquad g_{2n}>0,
\]
\[
\partial_u\partial_{\bar u}\log g_{2n}
=\frac{g_{2n+2}}{g_{2n}}-\frac{g_{2n}}{g_{2n-2}}-g_2,
\qquad g_0=1.
\]
Here \(u\) denotes the gauge coupling, not arithmetic frequency. These equations form a semi-infinite Toda system, with exact input available from localization and physical operator normalization. [Baggio–Niarchos–Papadodimas, 2014.][8]

**Deduction and proposal.** This is an actual interacting example of infinitely many positive norms controlled by nonlinear equations, rather than a finite vacuum metric decorated by arbitrary labels. It is a useful alternative laboratory if the periodic branch's flavor restriction proves too severe.

Its infinite tower does not itself give the desired kernel: its protected scaling dimensions are integer multiples of a basic dimension, and chiral multiplication follows \(\phi_{2m}\phi_{2n}=\phi_{2(m+n)}\). Neither rule identifies multiplication of arbitrary integers or \(\log p\) translations. An arbitrary map from \(f\) into this positive tower again risks hiding the unknown factorization. The next test is to find an independently motivated boundary/defect observable algebra with the required arithmetic action, before solving more Toda equations.

## 9. Positive geometry can be a theorem, with nontrivial hypotheses

**Literature.** Hertling–Sabbah prove a finite-dimensional construction of pure polarized twistor structures from Stokes data. In the relevant setting, a positivity condition on the Stokes matrix plus its adjoint, together with minimality or the specified condition on invariant summands, yields the polarization. The connection has an unramified pole of order two. [Hertling–Sabbah, theorem 5.9 and surrounding definitions.][9]

**Deduction.** This supplies a mathematically precise model for the hoped-for argument: start with independently positive geometric data, apply a theorem preserving polarization, and identify the resulting metric with the arithmetic pairing. It is stronger than merely asserting formal SUSY positivity.

However, inserting the unknown Weil operator into the required Stokes positivity condition would restate the problem. The theorem is also not an infinite-rank existence theorem. A geometric version of the program must locate arithmetic monodromy/Stokes data that arise from a unitary or polarized construction without using RH, then prove the relevant infinite-dimensional limit and the exact input map.

## 10. Ranked variants and decisive tests

The ranking below concerns fit to the research objective, rather than probability of proving RH. No item currently satisfies all requirements.

| Rank | Variant | What is independently positive | What remains unprovided | Decisive next analytic test |
|---|---|---|---|---|
| 1 | Non-Abelian periodic \(tt^*\) with an infinite boundary/defect sector | Ordinary unitary state pairing and its metric connection, once a physical theory is specified | A definite arithmetic theory, charge/observable map, prime weights, pole sector | Define the Hilbert space and source map first; test prime-frequency selection and compute one full physical metric correction including mixed sectors |
| 2 | Interacting 4d \(\mathcal N=2\) chiral-primary metric | Infinite family of physical operator norms; nonlinear Ward equations | Arithmetic action and a noncircular map from the Weil input space | Identify an arithmetic-compatible observable algebra; reject a construction requiring arbitrary basis fitting |
| 3 | Twisted-mass \(\mathbb{CP}^1\)/two-exponential LG | Unitary sigma-model metric, non-Abelian vacuum overlaps | Infinite input sector and prime selection | Analyze the escaping-vacuum limit and derive a complete pairing of specified states |
| 4 | Periodic basic exponential LG | Positive lifted-vacuum Bloch metric | Gaussian-equivalent simplicity, Bessel/Euler mismatch, one-frequency restriction | Establish whether a physical insertion converts the metric into the gamma kinetic pairing; do not use the asymmetric amplitude alone |
| 5 | Polarized irregular connection/TERP construction | Polarization under explicit geometric hypotheses | Physical bulk interpretation and an infinite arithmetic extension | Produce arithmetic Stokes data from geometry and verify positivity structurally without placing the target inside the hypotheses |

The best **constructible first experiment** is item 3. The best **longer-term architecture** is item 1. Item 2 is an independent alternative with a genuine infinite positive operator sector. It is premature to call any of these the most promising *theory of the full Weil form*.

## 11. What would count as progress before numerical work

A useful next investigation should deliver one of the following structural advances:

- An independently defined infinite observable algebra whose primitive sectors generate \(\log p\), whose repetitions generate \(p^{-m/2}\), and whose physical measured pairing removes unwanted composite terms.
- A normalizable state/observable construction demonstrating exactly how an interacting deformation changes the gamma norm while retaining positivity of the complete Gram operator.
- A polarized existence theorem applicable to specified arithmetic data, with the all-input map and the coherent limit stated explicitly.
- A sharply scoped obstruction eliminating a plausible identification, such as the finite flavor-holonomy restriction proved above.

The pole contribution cannot be left for a final cosmetic adjustment. Its kernel \(2\cosh((x-y)/2)\) is a signed rank-two form on a finite interval. It can participate in a positive total pairing through interference or constraints, but cannot be called a separate positive norm. The contact term and gamma normalization must likewise be fixed by the same theory, rather than added after fitting a determinant expansion.

A theory with finitely many vacua may still be valuable if the measured operator creates an infinite family of excitations, if lifted vacua or superselection sectors are retained, or if a continuous boundary field survives projection. It fails the rank test only when every input is projected into one fixed finite-dimensional vacuum fiber. Conversely, collecting independently chosen vacua at different couplings does not automatically define their cross-inner-products: a common Hilbert realization or a physically specified interface is necessary.

At the present stage, a broad comparison of these mechanisms is more useful than another numerical positivity computation. The next calculations should decide whether a specified physical identification exists. Numerical work can then audit that identity and its limiting behavior.

## Sources

[1]: https://www.ictp-saifr.org/wp-content/uploads/2014/05/Vafa.pdf
[2]: https://arxiv.org/pdf/hep-th/9206037
[3]: https://arxiv.org/html/1312.1008v1
[4]: https://arxiv.org/pdf/1006.3435
[5]: https://arxiv.org/pdf/hep-th/9211097
[6]: https://arxiv.org/pdf/1103.2598
[7]: https://arxiv.org/pdf/0910.4963
[8]: https://arxiv.org/pdf/1409.4212
[9]: https://perso.pages.math.cnrs.fr/users/claude.sabbah/articles/hertling-sabbah.pdf
[10]: https://dlmf.nist.gov/5.7#E6

1. Sergio Cecotti and Cumrun Vafa. [*Topological–anti-topological fusion*][1]. Nuclear Physics B 367 (1991), 359–461.
2. Boris Dubrovin. [*Geometry and Integrability of Topological-Antitopological Fusion*][2]. arXiv:hep-th/9206037; Communications in Mathematical Physics 152 (1993), 539–564.
3. Sergio Cecotti, Davide Gaiotto, and Cumrun Vafa. [tt* Geometry in 3 and 4 Dimensions][3]. arXiv:1312.1008, especially §§2–3 and Appendix A.
4. Sergio Cecotti, Andrew Neitzke, and Cumrun Vafa. [*R-Twisting and 4d/2d Correspondences*][4]. arXiv:1006.3435, Appendix A.2.
5. Sergio Cecotti and Cumrun Vafa. [*On Classification of N=2 Supersymmetric Theories*][5]. arXiv:hep-th/9211097, especially §§2–4.
6. Davide Gaiotto, Gregory W. Moore, and Andrew Neitzke. [*Wall-Crossing in Coupled 2d-4d Systems*][6]. arXiv:1103.2598, especially §5.6 and its existence qualifications.
7. Kyriakos Papadodimas. [*Topological Anti-Topological Fusion in Four-Dimensional Superconformal Field Theories*][7]. arXiv:0910.4963.
8. Marco Baggio, Vasilis Niarchos, and Kyriakos Papadodimas. [tt* equations, localization and exact chiral rings in 4d N=2 SCFTs][8]. arXiv:1409.4212, §4.2.1. The short companion report is [Exact correlation functions in SU(2) N=2 superconformal QCD](https://arxiv.org/abs/1409.4217).
9. Claus Hertling and Claude Sabbah. [*Examples of non-commutative Hodge structures*][9]. Journal of the Institute of Mathematics of Jussieu 10 (2011), 635–674, theorem 5.9; [published version](https://doi.org/10.1017/S147474801100003X).
10. NIST Digital Library of Mathematical Functions. [§5.7, digamma series][10].

Local target and existing obstructions were read from `background_section.tex`, `archive/notes/SUPERSPACE_RELATIVE_BOUNDARY_ACTION_20260913.md`, and `archive/notes/QUANTUM_COVARIANCE_AUDIT_AND_FINITE_BLOCK_OBSTRUCTION_20260913.md` in the current SUSY positivity investigation. This note does not alter their conclusions or claim that the finite Gaussian obstruction excludes the interacting candidates discussed here.

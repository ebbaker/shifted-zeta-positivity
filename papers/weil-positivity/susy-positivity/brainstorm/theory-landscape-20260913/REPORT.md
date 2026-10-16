# Choosing a quantum theory for the Weil positivity program

The strongest direction identified here is **an arithmetic boundary or defect theory with a positive physical Hilbert space and genuinely dynamical supersymmetric ground-state geometry**. Its arithmetic operations should come from a semilocal construction: the real place together with finitely many prime places, enlarged compatibly as the support of the input grows. Four-supercharge geometry, potentially non-Abelian \(tt^*\), is a promising way to constrain its state pairing. A relative or polarized construction must also account for normalization and poles.

This is a recommendation for a theory to construct, not an existing theory that already reproduces the Weil form. The survey does not justify declaring \(\mathbb{CP}^1\), an adelic field theory, or a particular \(tt^*\) model the winner. It does narrow the search to two complementary, concrete controls:

- **Arithmetic control:** a supersymmetric Morse system coupled by tensor product to discrete prime sectors. An explicit positive Hamiltonian and normalizable ground state reproduce the gamma and finite Euler factors exactly as a unitary matrix coefficient.
- **Interacting geometric control:** the twisted-mass \(\mathbb{CP}^1\) sigma model and its exponential Landau–Ginzburg description. This is a concrete setting in which non-Abelian ground-state geometry can be studied. Its arithmetic interpretation remains to be supplied.

The first control has already yielded exact identities and new restrictions. Most significantly, its natural holomorphic vacuum line fails the simplest rank-one chiral \(tt^*\) curvature condition. More supersymmetry cannot simply be added while leaving all the original data intact. That result makes the next investigation more specific: additional states, a different parameter multiplet, or a different ground-state embedding must perform real work.

The distinction between these controls is useful. Arithmetic factors alone are comparatively easy to produce. The difficult object is a physical identity converting their first logarithmic derivative, with its contact and pole terms, into an ordinary positive norm.

## The criterion used to select theories

The intended argument is an operator identity of the form
\[
Q_L[f]=\|\mathcal O_L(f)\Omega\|^2,
\qquad f\in C_c^\infty((-L/2,L/2);\mathbb C),
\]
or an equivalent positive bulk energy identity, derived from a theory specified independently of the unknown positivity. It must work for arbitrarily large support lengths with compatible definitions. Numerical checks can test the identity after it is derived; bounding sampled eigenvalues is not the mechanism sought here.

Write \(F=E_Lf\) for zero extension, \(U_dF(x)=F(x-d)\), and
\[
\begin{gathered}
B(s)=\Re\psi(\tfrac14+i\sqrt{s}/2)-\psi(\tfrac14),\qquad
w_0=\psi(\tfrac14)-\log\pi,\\
K[F]=\frac1{2\pi}\int_{\mathbb R}B(\tau^2)|\widehat F(\tau)|^2\,d\tau,
\qquad \widehat F(\tau)=\int F(x)e^{-i\tau x}\,dx,\\
P_L[f]=2\left|\int f(x)\cosh(x/2)\,dx\right|^2
-2\left|\int f(x)\sinh(x/2)\,dx\right|^2.
\end{gathered}
\]
The full target is
\[
\boxed{\displaystyle
Q_L[f]=K[F]+w_0\|f\|^2+P_L[f]
-2\sum_{m\log p<L}(\log p)p^{-m/2}
\Re\langle F,U_{m\log p}F\rangle .}
\]
Its natural finite-interval domain has logarithmically weighted Fourier norm. Closedness and semiboundedness are available; nonnegativity for all support lengths is the RH-level assertion. No background equation numbers are needed to specify the target.[^weil]

The present manuscript and subsequent quantum investigation establish the gamma kinetic pairing and analyze failures of particular arithmetic extensions. Quantizing the fixed relative complex preserves its harmonic-state norm; it does not change that norm into the complete arithmetic form. Likewise the finite-block obstruction excludes more than a particular Gaussian fit: any replacement retaining its positive resolvent representation and stipulated moments satisfies the same moment inequalities.

This supports the requested change of emphasis. The next theory should change the observable, ground-state geometry, arithmetic operations, or boundary completion. A new norm estimate for the same residual would leave the principal construction question unresolved. A structural passivity theorem remains a valid alternative if its sign comes from an independently positive bulk.

## What the broader comparison selects

The following priorities express usefulness for this particular program. They are not estimated probabilities of proving RH. Detailed source discussions and deductions are in the companion branch reports.

| Family | Structure it actually supplies | Missing bridge and recommended role |
|---|---|---|
| Semilocal arithmetic Hilbert geometry | Positive local-factor measures, scaling, prime-place operations, infinite state spaces | Best arithmetic foundation; its logarithmic derivative and residual trace terms are not automatically positive norms. |
| Interacting periodic/non-Abelian \(tt^*\) | Equations for a physical ground-state metric; lifted periodic sectors can be infinite | Best metric mechanism to investigate; arithmetic source map, exact repetition weights, normalization, and poles remain missing. |
| Four-supercharge sigma/gauged quantum mechanics | Controlled Berry geometry, with \(tt^*\) or Bogomolny equations depending on parameter type | Concrete control for an interacting defect; finite vacuum spaces alone cannot carry the target. |
| Morse system with discrete prime sectors | Explicit positive SUSY Hamiltonian and exact finite Euler–gamma transition amplitude | Best arithmetic benchmark derived here; direct rank-one chiral extension is obstructed. |
| Four-dimensional \(\mathcal N=2\) superconformal QCD | An infinite tower of positive chiral-operator norms obeying Toda-type equations | Serious alternative for infinite metric data; no identified map from its operator algebra to prime translations. |
| Polarized cohomological/adelic theories | The conceptual combination of arithmetic trace, poles, and a positive Hodge pairing | Strong long-term fit; the number-field polarization and associated geometry remain major conjectural inputs. |
| Tate/Vladimirov or \(p\)-adic bulk fields | Natural local factors and multiplicative prime geometry | Useful local ingredients; complex character amplitudes or propagator products are not ordinary positive Weil pairings. |
| Bost–Connes arithmetic statistical mechanics | Prime occupation algebra, logarithmic energies, Euler repetitions | Useful arithmetic operations; the critical-line Gibbs trace is unavailable, and a partition derivative is not a covariance. |
| Integrable supersymmetric boundary QFT | Nonlinear boundary interactions and controlled scattering/form factors | Useful laboratory after return geometry is specified; ordinary local Euclidean correlations have the wrong separated-point singularities. |
| Quantum graphs and hyperbolic/scattering models | Return paths, primitive-orbit formulas, and sometimes explicit zeta scattering factors | Strong controls for signs and repetitions; matching an oscillatory trace or resonances does not match the full positive pairing. |
| Canonical systems/passive transfer theories | A direct positive-energy language for the shifted transfer | Retain as an alternative structural route; assuming the zeta input is inner would assume the missing sign information. |

Semilocal measures are particularly relevant because Connes–Consani–Moscovici use the squared modulus of the product of local factors on the critical line as a positive measure. Their construction gives arithmetic data suitable for an infinite Jacobi/moment framework.[^local] Semilocal Sonin spaces also provide a meaningful operation of adjoining places.[^sonin] These are more specific starting data than a generic interacting potential chosen for flexibility.

The role of \(tt^*\) is complementary. In a unitary theory it constrains a Hermitian ground-state metric together with projected chiral operators, schematically
\[
[D_i,\bar D_j]=-[C_i,\bar C_j].
\]
It does not identify an arbitrary arithmetic expression with that metric. Nor do formal flatness equations ensure positive polarization for arbitrary input data.[^tt] In supersymmetric quantum mechanics, chiral parameters and vector-multiplet parameters lead to different equations; the latter lead to Bogomolny geometry.[^berry] The meaning of a prime parameter must therefore be fixed before choosing which equations to impose.

## An exact positive arithmetic model

The following construction is an elementary benchmark developed for this comparison. It is not presented as a priority claim. Supersymmetric Morse systems and zeta-related ground-state Fourier amplitudes have prior literature.[^morse]

Let \(S\) be a finite set of primes, \(\sigma>0\), and set
\[
\Lambda_S(z)=\pi^{-z/2}\Gamma(z/2)\prod_{p\in S}(1-p^{-z})^{-1}.
\]
On the continuous factor \(L^2(\mathbb R,dy)\), put \(a=\sigma/2\) and
\[
A_a=\partial_y+\frac{e^y-a}{2},\qquad
H_-=A_a^\dagger A_a
=-\partial_y^2+\frac{(e^y-a)^2}{4}-\frac{e^y}{2}.
\]
This is a nonlinear potential with a positive supersymmetric factorization. For each prime take \(\ell^2(\mathbb N_0)\), the backward unilateral shift \((T\xi)_n=\xi_{n+1}\), and
\[
D_p=T-p^{-\sigma/2}I,\qquad H_p=D_p^\dagger D_p\ge0.
\]
Their standard graded supersymmetric tensor product has a nilpotent supercharge and positive Hamiltonian. Its bosonic ground vector is
\[
\Psi_\sigma(y,\mathbf n)=\pi^{-\sigma/4}
\exp\!\left(\frac{\sigma y/2-e^y}{2}\right)
\prod_{p\in S}p^{-\sigma n_p/2}.
\]
Define the self-adjoint multiplication operator
\[
X=\frac y2-\sum_{p\in S}n_p\log p-\frac{\log\pi}{2}.
\]
The gamma integral and convergent geometric sums give the exact identities
\[
\boxed{\quad
\|\Psi_\sigma\|^2=\Lambda_S(\sigma),\qquad
\langle\Psi_\sigma,e^{i\tau X}\Psi_\sigma\rangle
=\Lambda_S(\sigma+i\tau).
\quad}
\]
The same Hilbert space works for all real \(\tau\); it labels a unitary observable, not a separate Hilbert space. No zero data or square root of the Weil form enters. The gamma dynamics are nonlinear, while the prime sectors are independent discrete systems. This is already enough to reproduce the factors, so factor reproduction alone cannot justify introducing more interactions.

For the normalized ground state \(\Omega_\sigma\), the transition amplitude is \(\Lambda_S(\sigma+i\tau)/\Lambda_S(\sigma)\). Its squared modulus is another positive-definite matrix coefficient, realized on two copies with generator \(X\otimes I-I\otimes X\). It is not the Weil kernel.

Nevertheless its derivative gives a useful exact bridge. Set
\[
w_{S,\sigma}(\tau)=|\Lambda_S(\sigma+i\tau)|^2.
\]
Then
\[
\left.\partial_\sigma\log w_{S,\sigma}(\tau)\right|_{1/2}
=B(\tau^2)+w_0
-2\sum_{p\in S,m\ge1}(\log p)p^{-m/2}\cos(m\log p\,\tau).
\]
If \(S\) includes all primes active on \(I_L\), compression of this multiplier gives the entire pole-free Weil operator. This is an exact finite-prime identity, not an asymptotic approximation or an all-prime Euler product on the critical line.

Normalization changes the result in an instructive way:
\[
\left.\partial_\sigma\log
\frac{w_{S,\sigma}(\tau)}{w_{S,\sigma}(0)}\right|_{1/2}
=B(\tau^2)+2\sum_{p\in S,m\ge1}(\log p)p^{-m/2}
[1-\cos(m\log p\,\tau)]\ge0.
\]
Its positivity has a literal energy explanation. The prime contributions are weighted squared differences \(\|F-U_{m\log p}F\|^2\). The gamma contribution also has a positive jump representation, with symmetric density
\[
\nu_\Gamma(dx)=\frac{e^{-|x|/2}}{1-e^{-2|x|}}\,dx,
\qquad
B(\tau^2)=\int[1-\cos(\tau x)]\nu_\Gamma(dx).
\]
Thus the normalized derivative is the symbol of a positive jump energy and admits an incidence-operator SUSY factorization. This is structural positivity of a precisely identified object.

The full target is instead
\[
\boxed{\displaystyle
Q_L[f]=K[F]
+\sum_{p\in S,m\ge1}(\log p)p^{-m/2}\|F-U_{m\log p}F\|^2
+c_S\|f\|^2+P_L[f],}
\]
where
\[
c_S=w_0-2\sum_{p\in S,m\ge1}(\log p)p^{-m/2}<0.
\]
The positive energy forces a diagonal term for every jump; the required arithmetic normalization subtracts those terms again. The pole form supplies an additional signed contribution. A successful bulk theory must derive their accounting within one positive pairing, perhaps through coherent interference or a physical constraint. Appending independent positive sectors cannot supply an arbitrary negative correction.

This also explains why the infinite-prime limit is consequential. A jump beyond the support has squared difference \(2\|F\|^2\). The independent positive prime energy diverges for every nonzero compactly supported \(F\) as \(S\) grows, already through \(\sum_p(\log p)p^{-1/2}\). The complete finite-interval form stays finite because the inactive translations and matching diagonal subtraction cancel. Ordinary positivity is not preserved by an unexplained divergent subtraction.

## What the ground-state geometry rules out

There are two different metrics here, and conflating them would make the \(tt^*\) proposal look more developed than it is.

First, declaring \(g(z,\bar z)=|\Lambda_S(z)|^2\) to be a scalar Hermitian metric gives
\[
\partial\bar\partial\log g=0
\]
on \(\Re z>0\), since \(\Lambda_S\) is holomorphic and nonzero there. A holomorphic change of frame makes this metric constant. Rescaling the frame by \(e^{cz}\) shifts its first normal logarithmic derivative by \(2\Re c\). The putative arithmetic contact is therefore not fixed by curvature or by the scalar \(tt^*\) equations. A physical preparation prescription could fix it, but must be supplied.

Second, a natural chosen holomorphic extension of the Morse–prime vacuum has a different metric. Write
\[
\Psi_z=e^{zX/2}e^{-e^y/2},\qquad
g_{\rm vac}(z,\bar z)=\|\Psi_z\|^2=\Lambda_S(\Re z).
\]
The original Hamiltonian is specified for real \(\sigma\). The displayed states become the ground family of the explicit extension \(H_{\sigma,\eta}=e^{i\eta X/2}H_\sigma e^{-i\eta X/2}\), where \(z=\sigma+i\eta\) and the unitary acts identically on the fermion labels. This choice, rather than every possible complex extension, is what the following curvature test concerns.
With \(\sigma=\Re z\), direct differentiation gives
\[
\partial_z\partial_{\bar z}\log g_{\rm vac}
=\frac14\operatorname{Var}_{\sigma}(X)>0,
\]
where
\[
\operatorname{Var}_{\sigma}(X)
=\frac14\psi_1(\sigma/2)
+\sum_{p\in S}\frac{(\log p)^2p^{-\sigma}}{(1-p^{-\sigma})^2}.
\]
In an ordinary rank-one chiral \(tt^*\) vacuum bundle, the projected chiral operators are scalars, their commutator vanishes, and the connection must be flat. Consequently the entire specified holomorphic vacuum line cannot simply become that bundle.

This is a useful restriction, not a general obstruction to extended supersymmetry. It permits additional vacua, coupled periodic fibers, vector-multiplet geometry, or a different dependence on the partner parameter. In particular the \(\tau\) in \(e^{i\tau X}\) began as an observable label; it need not become the imaginary part of a physical chiral coupling. The [extension appendix](EXTENDED_SUSY_TEST.md) also gives a spectral-multiplicity obstruction to adding four standard real supercharges to the unchanged Hamiltonian and Hilbert space.

Poles impose another independent test. On \(z=1/2+i\tau\),
\[
2\Re\left(\frac1z+\frac1{z-1}\right)=0.
\]
Multiplying the scalar weight by \(|z(z-1)|^2\) therefore does not create the required pole form in its ordinary normal derivative. Moreover \(\partial_\sigma\log|\xi(\sigma+i\tau)|^2\) vanishes pointwise on the critical line away from zeros, by the functional equation and real structure. The explicit-formula distribution retains contour, zero, and residue information that this pointwise operation loses. An all-prime completion must preserve that information through a justified boundary prescription.

## Why the interacting models remain worth pursuing

The most relevant \(\mathbb{CP}^1\)/Landau–Ginzburg control has the schematic holomorphic superpotential
\[
W_\varepsilon(Y)=\mu Y-e^Y+\varepsilon e^{-Y}.
\]
With suitable physical Kähler data, the additional exponential gives a non-Abelian vacuum problem. The basic single-exponential periodic example has gamma-related brane amplitudes, but their special-limit formula is not already the physical Hermitian metric.[^periodic] The elementary Morse construction above provides an independent check on how much a gamma amplitude alone establishes.

There is a useful analytic caution before perturbing in \(\varepsilon\). Setting \(z=e^Y\), the critical points satisfy
\[
z^2-\mu z+\varepsilon=0.
\]
At fixed nonzero \(\mu\), one root approaches \(\mu\), while the other approaches \(\varepsilon/\mu\). The latter vacuum escapes to the noncompact end as \(\varepsilon\to0\). Thus the limit is not automatically a small deformation of a fixed gapped vacuum bundle. Normalizability and the actual source projection must be analyzed first.

Periodic \(tt^*\) also offers infinitely many lifted sectors, which could avoid a finite-vacuum rank restriction. But the basic physical periodic metric has Bessel winding weights; identifying its period with \(\log p\) does not directly give the bare coefficients \((\log p)p^{-m/2}\).[^winding] In a coupled theory, mixed-prime histories are another issue: generic interactions generate composite words, whereas the logarithmic Euler derivative selects primitive prime powers. A charge or factorization identity must select the required terms without replacing the ordinary norm by a signed index.

The four-dimensional alternative is attractive for a different reason: the chiral sector of \(\mathcal N=2\) superconformal QCD contains an infinite tower of genuine operator norms constrained by a semi-infinite Toda chain.[^4d] That removes the need to build an infinite metric from finitely many vacua, but does not supply prime delays. A parallel mathematical benchmark is available directly from the semilocal positive measure: its Hankel determinants under an exponential deformation obey a Toda identity and have positive Vandermonde integral formulas. Establishing that this arithmetic moment construction is the physical chiral sector of a specified theory would be real progress. Similar-looking Toda equations alone are insufficient.

Non-Gaussian dynamics therefore remain a serious option. They can change the ground-state embedding and permit coherent interference among channels. They are not compelled simply by the complexity of RH: a Gaussian theory may have a complicated two-point kernel, and an interacting theory still gives an exactly quadratic functional when a linear smearing is inserted into a norm. The discriminant is whether independently specified dynamics derive the correct pairing. Putting the unknown answer into a covariance or into a fitted nonlinear potential has the same logical weakness.

## What the other families teach us

Polarized cohomology is the closest conceptual analogue of the intended argument. A positive Hodge pairing compatible with the arithmetic flow could place the central spectral generator on the critical line, while other degrees organize poles. The relevant number-field geometry is not constructed with the necessary properties.[^hodge] Adelic trace formulas and related homological constructions identify arithmetic distributions, but their full positivity is an additional RH-level issue.[^adeles] Supersymmetrizing such a conjectural positive complex would not discharge that issue.

Local \(p\)-adic theories deserve attention as ingredients: valuation shells produce Euler factors naturally. Bruhat–Tits-tree bulk theories also supply geometric local-zeta factors in boundary correlations.[^padic] Neither supplies the required real-input Weil pairing merely by multiplication over places. Positivity for real kinetic multipliers must be distinguished from analytic continuation in complex arithmetic characters.[^vladimirov]

Bost–Connes theory provides arithmetic operators and logarithmic energy levels; its original Gibbs trace exists for \(\beta>1\). KMS states outside that regime do not make that trace convergent at \(\beta=1/2\).[^bc] It is more promising here as an algebra of defect operations than as a partition function whose derivative is declared positive.

Quantum graphs give a particularly clear warning about incomplete matches. There are graphs reproducing the oscillating prime contribution to the Riemann density, including its sign, while having the wrong smooth density and therefore a different spectrum.[^graphs] The modular surface gives another: zeta zeros occur in scattering resonances, which need not be real eigenvalues of the self-adjoint Laplacian.[^modular] These theories show that arithmetic return structure and a positive physical operator can coexist without settling the target positivity.

An independently passive realization of the shifted completed-zeta transfer would remain a legitimate competitor to the ground-state route. Canonical-system theory explains why such a realization would carry positive energy. The task is to derive that realization from positive geometric data; imposing the needed inner-function property on the zeta transfer at the outset would move the unknown sign into an assumption.[^canonical]

## A bounded next investigation

The most informative next task is a **compatibility and construction test for one arithmetic prime coupled to a four-supercharge defect**, using the Morse system as the arithmetic control and \(\mathbb{CP}^1\) as the geometric control.

First specify the enlarged fields, physical adjoint, common operator domains, and supercharge algebra. Decide whether the arithmetic parameters are chiral, vector-multiplet, or geometric data. Derive the ground-state metric and the relevant boundary observable. Test the curvature restriction before trying to impose a particular \(tt^*\) solution. The arithmetic Fourier coordinate should retain its original role unless a new identification is derived.

The first positive outcome would be an independently fixed normalization together with a supersymmetric identity that controls the **first logarithmic derivative and its contact term**, or an ordinary norm that bypasses that derivative while reproducing its arithmetic kernel. Merely reproducing the already known transition amplitude, normalized jump energy, or scalar flat metric would add no missing structure.

Next require a physical mechanism for the two pole amplitudes and for primitive-power selection. A combined observable can have signed interference terms inside a positive norm; independent sectors only add positive forms. A proposed boundary constraint must be checked with its induced physical inner product, rather than assigning a negative-norm pole state.

Only after this mechanism is defined should it be tested with two distinct primes and then with compatible growing supports. At finite \(S\), a full Weil comparison uses only intervals for which \(S\) contains all active primes. One should not demand positivity for arbitrarily large supports after deleting all other primes. All-repetition local-factor tests are separate, and remain useful at a single prime.

If a four-supercharge completion cannot pass the curvature and normalization tests, the next branch should be the semilocal infinite moment/Toda construction or a polarized relative arithmetic complex. The criterion for changing branches is an exact incompatibility or an absent physical observable, not a disappointing numerical bound.

The concrete deliverable of that next pass should be either a fully specified first arithmetic defect with a new positive pairing identity, or a scoped theorem explaining why a proposed extension cannot supply it. Both would narrow the theory space substantially. The present pass supplies the exact arithmetic control, identifies where its positive energy differs from the target, and gives analytic tests that distinguish real extensions from changes of presentation.

## Sources and technical companions

The literature citations below support the stated established constructions. The Morse–prime comparison, normalization identities, finite-rank and frequency tests, and extension obstructions are deductions recorded in this research package; they have received an internal algebraic cross-check, not independent specialist review. No new full-form positivity interval or RH result is claimed.

- [Structural selection tests](SELECTION_TESTS.md): exact target, spectral restrictions, source rank, prime returns, contact and pole accounting, and domain issues.
- [Extended-supersymmetry compatibility tests](EXTENDED_SUSY_TEST.md): the physical vacuum curvature and fixed-Hamiltonian restrictions.
- [Ground-state and \(tt^*\) branch](TTSTAR_BRANCH.md): periodic models, non-Abelian geometry, and the infinite chiral tower.
- [Arithmetic branch](ARITHMETIC_BRANCH.md): semilocal weights, moment/Toda geometry, adeles, cohomology, and arithmetic statistical mechanics.
- [Interacting branch](INTERACTING_BRANCH.md): spectral distinctions, boundary mechanisms, and the explicit Morse–prime model with its positive jump energy.

[^weil]: Masatoshi Suzuki, [Weil's quadratic form via the screw function](https://arxiv.org/abs/2606.09096v2), 2026. The target is reproduced above in the local program's normalization.
[^local]: Alain Connes, Caterina Consani, Henri Moscovici, [On q-series and the moment problem associated to local factors](https://arxiv.org/abs/2403.01247), 2024.
[^sonin]: Alain Connes, Caterina Consani, Henri Moscovici, [Zeta zeros and prolate wave operators](https://arxiv.org/abs/2310.18423), 2023/2024 preprint.
[^tt]: Sergio Cecotti and Cumrun Vafa, [Topological–anti-topological fusion](https://www.ictp-saifr.org/wp-content/uploads/2014/05/Vafa.pdf), 1991; Boris Dubrovin, [Geometry and integrability of topological-antitopological fusion](https://arxiv.org/abs/hep-th/9206037), 1992.
[^berry]: Julian Sonner and David Tong, [Berry Phase and Supersymmetry](https://arxiv.org/abs/0810.1280), 2008/2009; [Non-Abelian Berry Phases and BPS Monopoles](https://arxiv.org/abs/0809.3783), 2008/2009.
[^morse]: Edward Witten, [Supersymmetry and Morse theory](https://www.ias.edu/sites/default/files/sns/files/supersymmetry-and-morse-theory-1982.pdf), 1982; Michael McGuigan, [Riemann hypothesis, modified Morse potential and supersymmetric quantum mechanics](https://arxiv.org/abs/2002.12825), 2020. The finite-prime tensor-product calculation is given explicitly here; no novelty claim about gamma ground states is intended.
[^periodic]: Sergio Cecotti, Davide Gaiotto, Cumrun Vafa, [\(tt^*\) Geometry in 3 and 4 Dimensions](https://arxiv.org/abs/1312.1008), 2013/2014.
[^winding]: Sergio Cecotti, Andrew Neitzke, Cumrun Vafa, [R-Twisting and 4d/2d Correspondences](https://arxiv.org/abs/1006.3435), 2010, appendix on the periodic \(tt^*\) geometry of a free chiral multiplet.
[^4d]: Marco Baggio, Vasilis Niarchos, Kyriakos Papadodimas, [\(tt^*\) equations, localization and exact chiral rings in 4d \(\mathcal N=2\) SCFTs](https://arxiv.org/abs/1409.4212), 2014/2015.
[^hodge]: Christopher Deninger, [The Hilbert–Polya strategy and height pairings](https://www.uni-muenster.de/SFB878/publications/files/php7aMxKR3029.pdf).
[^adeles]: Alain Connes, [Trace formula in noncommutative geometry and the zeros of the Riemann zeta function](https://arxiv.org/abs/math/9811068), 1998/1999; Alain Connes, Caterina Consani, Matilde Marcolli, [The Weil proof and the geometry of the adeles class space](https://arxiv.org/abs/math/0703392), 2007.
[^padic]: Steven Gubser, Johannes Knaute, Sarthak Parikh, Andreas Samberg, Przemek Witaszczyk, [\(p\)-adic AdS/CFT](https://arxiv.org/abs/1605.01061), 2016/2017.
[^vladimirov]: An Huang, Bogdan Stoica, Shing-Tung Yau, Xiao Zhong, [Green's Functions for Vladimirov Derivatives and Tate's Thesis](https://arxiv.org/abs/2001.01721), 2020.
[^bc]: Jean-Benoît Bost and Alain Connes, [Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory](https://repo-archives.ihes.fr/FONDS_IHES/I_Prepublications/CONNES/1994-1998/M_95_38/M_95_38_web.pdf), 1995.
[^graphs]: Jack Kuipers, Quirin Hummel, Klaus Richter, [Quantum graphs whose spectra mimic the zeros of the Riemann zeta function](https://arxiv.org/abs/1307.6055v2), 2014.
[^modular]: Yiannis N. Petridis, Nicole Raulf, Morten S. Risager, [Quantum limits of Eisenstein series and scattering states](https://arxiv.org/abs/1111.6615), 2011 preprint.
[^canonical]: Masatoshi Suzuki, [A canonical system of differential equations arising from the Riemann zeta-function](https://arxiv.org/abs/1204.1827), 2012.

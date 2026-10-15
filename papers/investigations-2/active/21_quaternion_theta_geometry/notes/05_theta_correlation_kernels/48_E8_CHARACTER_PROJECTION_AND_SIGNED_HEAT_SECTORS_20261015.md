---
research_program: PR02-CORR
parent_program: PR02
secondary_programs: [ALG]
status: exact_integrable_arithmetic_bridge_and_open_signed_estimate
---

# Exact E8 projection, heat-preserving translation identities, and the signed gate

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Coordinating session model **gpt-6.1-sol**, effort **ultra**, as supplied by the parent investigation. Internal analytic research, not external review or formal verification. No numerical pilot was used.

This note addresses the arithmetic lane of the request to strengthen the signed lower bound with maximal legitimate use of octonionic machinery. It supplies an explicit observation-preserving bridge from the E8 lattice to the exact differentiated two-coordinate theta source; the bridge missing from Review 25 is therefore available. It also proves that its unprojected source has a negative sector and that polarized octonionic norm estimates cannot pay the auxiliary translated fields at physical energy scale. The desired theta-specific signed bound remains open.

## 1. Exact finite character projection of the E8 theta series

Use the standard coordinate model

\[
L=\{\xi\in\mathbb Z^8:\sum\xi_i\in2\mathbb Z\}
\cup\{\xi\in(\mathbb Z+\tfrac12)^8:\sum\xi_i\in2\mathbb Z\}.
\]

It is the E8 lattice, isometric after the customary normalization and rotation to the lattice of integral octonions. See [Baez's explicit lattice description](https://math.ucr.edu/home/baez/octonions/integers/integers_3.html) and [his discussion of normalization for integral octonions](https://math.ucr.edu/home/baez/octonions/integers/integers_7.html). The following formulas are direct lattice decompositions, not consequences of an imported exceptional theta theorem.

For independent \(u=s+r,v=s-r\), put

\[
y_+=e^{4u},\quad y_-=e^{4v},\quad
Q_\Lambda(u,v)=\operatorname{diag}(y_+/4,y_-/4,\Lambda,\ldots,\Lambda),
\qquad \Lambda>0.
\]

Define the twisted theta series

\[
T_{a,b}^\Lambda(u,v)=
\sum_{\xi\in L}
e^{-\pi\xi^TQ_\Lambda\xi}
e^{\pi i[(a-b)\xi_1+b\xi_2]},
\qquad 0\le a\le3,\quad 0\le b\le1.
\tag{1}
\]

The finite projector is

\[
\mathcal P_M(\xi)=\frac18\sum_{a=0}^3\sum_{b=0}^1
e^{\pi i[a\xi_1+b(\xi_2-\xi_1)]}.
\tag{2}
\]

Because \(\xi_1\in\tfrac12\mathbb Z\) and \(\xi_2-\xi_1\in\mathbb Z\), the first average selects \(\xi_1\in2\mathbb Z\), and the second then selects \(\xi_2\in2\mathbb Z\). Hence \(\mathcal P_M\) is exactly the indicator of

\[
M=2\mathbb Z^2\oplus D_6,
\qquad
D_6=\{n\in\mathbb Z^6:\sum n_i\in2\mathbb Z\}.
\]

The covolume of \(M\) is \(2\cdot2\cdot2=8\), so it has index eight in \(L\), consistent with the eight characters. Set

\[
A_6(\Lambda)=\Theta_{D_6}(\Lambda)
=\frac{\Theta_3(\Lambda)^6+\Theta_4(\Lambda)^6}{2}>0.
\]

Here \(\Theta_3(y)=\sum_ne^{-\pi n^2y}\),
\(\Theta_4(y)=\sum_n(-1)^ne^{-\pi n^2y}\), and
\(\Theta_2(y)=\sum_ne^{-\pi(n+1/2)^2y}\).
The exact identity, at every \(\Lambda>0\), is

\[
\boxed{
\frac18\sum_{a=0}^3\sum_{b=0}^1 T_{a,b}^\Lambda(u,v)
=A_6(\Lambda)\Theta_3(y_+)\Theta_3(y_-).
}
\tag{3}
\]

Thus this is more than an asymptotic degeneration or an eighth tensor power. It recovers the actual rank-two arithmetic source with its two independent arguments and with a finite, exact character projector.

Let \(P(u)=e^u\Theta_3(e^{4u})\), as in Note 38, and let \(\mathcal D\) be that note's source operator. Then

\[
\boxed{
\Phi(s+r)\Phi(s-r)
=\frac1{4096A_6(\Lambda)}\,
\mathcal D\left[
\frac{e^{2s}}8\sum_{a,b}T_{a,b}^\Lambda(s+r,s-r)
\right].
}
\tag{4}
\]

No heat multiplier has been removed: the complete correlation still multiplies (4) by \(e^{2t(s^2+r^2)}\). Equation (4) uses no source cutoff and does not alter the original staircase whenever that is invoked elsewhere.

## 2. What survives of triality after the physical projection

Any lattice isometry preserving \(M\) preserves its roots, namely the vectors of squared norm two. Those roots are precisely the D6 roots in the last six coordinates. Their real span is the transverse six-plane. Its orthogonal complement, the distinguished physical two-plane, is therefore also preserved. On its \(2\mathbb Z^2\) lattice, such an isometry acts by signed coordinate permutation. Thus the projector-preserving lattice symmetry has no exceptional mixing of the physical plane with the remaining six coordinates.

This is a concrete reason the projected expression does not inherit the full octonionic symmetry as a new physical sign principle. A general E8 isometry or triality change can still be used covariantly, but it carries both \(Q_\Lambda\) and the projector, hence the physical observation and constraints, along with it. Keeping only the invariant norm while resetting the physical projection changes the problem.

An anisotropic quadratic form with independently variable first two entries is also not fixed by a transformation mixing these eigenspaces with the \(\Lambda\)-eigenspace. Full isotropy restores the larger stabilizer but constrains the two arithmetic coordinates and cannot cover the full correlation domain.

The finite character projector is an exact idempotent coefficient selector, not a Euclidean map from the lattice onto a subspace. It retains coefficientwise positivity of its selected theta series. This fact must not be confused with preservation of the sign after the source differential operator or of the physical oriented current.

## 3. Exact untwisted decomposition and a sign obstruction after the source operator

The same lattice decomposition gives a particularly transparent formula for the untwisted E8 theta series \(T_\Lambda=T_{0,0}^\Lambda\). Put

\[
B_6=(\Theta_3(\Lambda)^6-\Theta_4(\Lambda)^6)/2,
\qquad C_6=\Theta_2(\Lambda)^6/2.
\]

Then

\[
\begin{split}
T_\Lambda={}&A_6\{\Theta_3(y_+)\Theta_3(y_-)
                  +\Theta_2(y_+)\Theta_2(y_-)\}\\
&+B_6\{\Theta_3(y_+)\Theta_2(y_-)
                  +\Theta_2(y_+)\Theta_3(y_-)\}\\
&+C_6\Theta_2(y_+/4)\Theta_2(y_-/4).
\end{split}
\tag{5}
\]

For integer coordinates, the first two coordinates have even/even, odd/odd, even/odd or odd/even parity, and the remaining D6 parity selects \(A_6\) or \(B_6\). In the all-half-integer sector the two transverse parity sums are equal, because changing one integer summation coordinate \(n\mapsto-n-1\) preserves its norm and reverses its parity. Each equals \(C_6\), giving the last line of (5).

Define

\[
P_\nu(u)=e^u\Theta_\nu(e^{4u}),\qquad
\Phi_\nu(u)=(P_\nu''-P_\nu)/16,
\quad \nu=2,3,4,
\]

with \(\Phi_3=\Phi\), and
\(\widetilde\Phi_2=(\partial_u^2-1)[e^u\Theta_2(e^{4u}/4)]/16\).
After the exact source operator, (5) becomes

\[
\begin{split}
\frac{\mathcal D[e^{2s}T_\Lambda]}{4096}={}&
A_6\{\Phi(u)\Phi(v)+\Phi_2(u)\Phi_2(v)\}\\
&+B_6\{\Phi(u)\Phi_2(v)+\Phi_2(u)\Phi(v)\}
+C_6\widetilde\Phi_2(u)\widetilde\Phi_2(v).
\end{split}
\tag{6}
\]

This differentiated source is not automatically positive. Indeed, the scalar modular relation gives \(\Phi_2(-u)=\Phi_4(u)\). For \(u\ge0\),

\[
\Phi_4(u)=2e^u\sum_{n\ge1}(-1)^n
z_n(z_n-3/2)e^{-z_n},\qquad z_n=\pi n^2e^{4u}.
\]

The positive function \(z(z-3/2)e^{-z}\) is strictly decreasing for \(z>3\), since its derivative is
\(-e^{-z}(z-3)(z-1/2)\). Thus the alternating sum starts negative and has decreasing magnitudes; \(\Phi_4(u)<0\) for \(u\ge0\), and \(\Phi_2(u)<0\) for \(u\le0\). Conversely every term of \(\Phi_2(u)\) is nonnegative once \(e^{4u}\ge6/\pi\), and higher terms are positive.

The leading asymptotics as \(R\to\infty\) are

\[
\Phi(R)\sim2\pi^2e^{9R-\pi e^{4R}},\quad
\Phi_2(R)\sim\frac{\pi^2}{8}e^{9R-(\pi/4)e^{4R}},\quad
\Phi_4(R)\sim-2\pi^2e^{9R-\pi e^{4R}}.
\]

As \(\Lambda\to\infty\), \(A_6\to1\), \(B_6,C_6\to0\). At the legitimate joint-escape path \((u,v)=(R,-R)\), the limiting untwisted differentiated source is therefore

\[
\Phi(R)^2+\Phi_2(R)\Phi_4(R)
\sim-\frac{\pi^4}{4}e^{18R-(5\pi/4)e^{4R}}<0.
\tag{7}
\]

The adverse term divided by the physical positive product is asymptotic to

\[
-\frac1{16}\exp\{(3\pi/4)e^{4R}\}\longrightarrow-\infty.
\tag{8}
\]

For each sufficiently large fixed \(R\), continuity of (6) shows the same negativity for all sufficiently large finite \(\Lambda\). Thus untwisted E8 positivity fails already pointwise after applying the exact source operator, by an unbounded relative amount. This is stronger than saying vaguely that the projector breaks symmetry. It forbids importing an unprojected E8 norm or coefficient positivity as a lower bound for the required differentiated physical source.

These sign-changing terms are still integrable. The failure here is a signed one, not the positive-time nonintegrability of the earlier Poisson modes.

## 4. Duplication reduces all these arithmetic sectors to translated complete sources

Put \(c=(\log2)/2\). Splitting the integer theta sum into its even and odd indices gives

\[
\Theta_2(y)=\Theta_3(y/4)-\Theta_3(y),\qquad
\Theta_4(y)=2\Theta_3(4y)-\Theta_3(y).
\]

The exact differentiated identities are consequently

\[
\boxed{
\begin{split}
\Phi_2(u)&=e^c\Phi(u-c)-\Phi(u),\\
\Phi_4(u)&=e^c\Phi(u+c)-\Phi(u),\\
\widetilde\Phi_2(u)&=e^{2c}\Phi(u-2c)-e^c\Phi(u-c).
\end{split}}
\tag{9}
\]

This shows concretely that this projected octonionic arithmetic bridge reduces to the classical parity/duplication source identities. It does not secretly add a new exceptional inequality. However, it yields a globally legitimate finite sector representation, because every term in (9) is a finite translate of the full superexponentially decaying theta source. All polynomially weighted heat transforms converge absolutely, locally uniformly in complex spectral arguments and finite real heat intervals.

The same conclusion holds for the eight twisted sources in (1), by the following explicit formula. Write \(\Theta_{[m]}=\Theta_3\) if \(m\) is even and \(\Theta_{[m]}=\Theta_4\) if \(m\) is odd, and put \(r_0=a-b\). Splitting integer and half-integer lattice points gives

\[
\begin{split}
T_{a,b}^{\Lambda,\mathrm{int}}={}&\frac12\{
\Theta_{[r_0]}(y_+/4)\Theta_{[b]}(y_-/4)\Theta_3(\Lambda)^6\\
&\hspace{12mm}+
\Theta_{[r_0+1]}(y_+/4)\Theta_{[b+1]}(y_-/4)\Theta_4(\Lambda)^6\},\\
T_{a,b}^{\Lambda,\mathrm{half}}={}&
\mathbf1_{\{b=0,\ a\text{ even}\}}(-1)^{a/2}
C_6\Theta_2(y_+/4)\Theta_2(y_-/4).
\end{split}
\tag{9a}
\]

For the second formula, the parity-weighted half-integer theta sum in each transverse coordinate is zero by \(n\mapsto-n-1\), leaving only the unweighted half contribution. A half-integer theta sum with odd additive phase is likewise zero. The remaining even phases give the displayed sign. This formula also independently verifies that every twisted sector is real.

For the source derivative of each first-coordinate factor, one uses

\[
\begin{split}
\frac{\partial_u^2-1}{16}[e^u\Theta_3(e^{4u}/4)]
&=e^c\Phi(u-c),\\
\frac{\partial_u^2-1}{16}[e^u\Theta_4(e^{4u}/4)]
&=e^{2c}\Phi(u)-e^c\Phi(u-c),
\end{split}
\]

and the third identity in (9) for \(\Theta_2\). Thus every differentiated sector in (9a) is an explicit finite sum of products of translated complete sources. This proves global integrability with every retained polynomial and positive heat multiplier on compact heat-parameter sets. No global interchange with an infinite Poisson-mode decomposition is needed; the finite character sum can remain intact in any estimate.

For the full transform, with the normalization \(2H(t,z)=\int e^{tu^2}\Phi(u)e^{izu}\,du\), define

\[
\mathcal T_cH(t,z)=e^{c+tc^2+icz}H(t,z-2itc).
\]

Translation of the source under the integral gives the heat-preserving formula

\[
\boxed{
\int_{\mathbb R}e^{tu^2}\Phi_2(u)e^{izu}\,du
=2\{\mathcal T_cH(t,z)-H(t,z)\}.
}
\tag{10}
\]

The heat factor produces the exact imaginary spectral displacement \(-2itc\); deleting it is incorrect. At \(t=0\), the right side is \(2(e^{c+icz}-1)H(0,z)\), so it is proportional to the physical zeroth jet. At positive heat time it observes a different complex spectral argument.

At a candidate double collision \(H=H_z=0\), the complex shift has the full Taylor expansion

\[
H(t,x-2itc)=\sum_{k\ge2}\frac{(-2itc)^k}{k!}\,h_k(t,x).
\tag{11}
\]

Its leading formal term is \(-2t^2c^2h_2\), but all higher jets in (11) must be retained. The arithmetic sector norm therefore does not vanish automatically with the physical energy.

## 5. A strict positive-source control rules out automatic physical-energy payment

This failure is exact for an explicit positive-source heat family. This control has Gaussian decay and is used only to test universal algebra, positivity, and local heat analyticity; it is not asserted to satisfy the theta source's stronger tail envelope. Fix \(t_*>0\) and take

\[
\Phi_{\rm ctrl}(u)=e^{-(1+t_*)u^2}(u^2-3/4)^2.
\]

At time \(t_*\), elementary Gaussian Fourier differentiation gives

\[
H_{\rm ctrl}(t_*,z)=\frac{\sqrt\pi}{32}
e^{-z^2/4}(z^2-3)^2.
\tag{12}
\]

At \(x_*=\sqrt3\), both \(H_{\rm ctrl}\) and its first derivative vanish, so \(E=0\) and \(S_0\) holds. But

\[
H_{\rm ctrl}(t_*,x_*-2it_*c)\ne0,
\]

because \((x_*-2it_*c)^2-3=-4t_*^2c^2-4ix_*t_*c\ne0\). The translated-sector norm in (10) is therefore nonzero at zero physical energy. Every universal monogenic lift, octonionic norm-composition identity and polarized calibration identity remains valid for this family.

To make the source strictly positive, replace the square by
\((u^2-3/4)^2+\varepsilon\), \(\varepsilon>0\). Consider
\((H_\varepsilon,H_{\varepsilon,z})=(0,0)\) in the real variables \((t,x)\).
At \(\varepsilon=0\), the Jacobian determinant at \((t_*,x_*)\) is
\[
\det\begin{pmatrix}-h_2&h_1\\-h_3&h_2\end{pmatrix}
=-h_2^2\ne0.
\]
The real implicit-function theorem gives, for every sufficiently small
fixed \(\varepsilon>0\), an actual positive-time double collision
\((t_\varepsilon,x_\varepsilon)\to(t_*,x_*)\).
The shifted amplitude remains nonzero by continuity. At each of these
strictly positive sources' collisions, \(E=0\) but the left side of
\[
|\mathcal T_cH-H|^2\le C(t,x)E \tag{13}
\]
is positive. Thus even a source-dependent finite coefficient fails,
not merely a uniform coefficient across the perturbation family.
The Gaussian family is heat-analytic near \(t_*\), which suffices here.
It is a control for generic algebra, positivity and local heat evolution,
not a member of the theta class with globally entire heat evolution and
the same double-exponential envelope. Note 15 supplies stronger-envelope
controls.
This is a control obstruction, not a counterexample for the theta source. A theta-specific signed cancellation could still hold; it must retain the complete combination before any auxiliary norm is paid.

## 6. Exact twisted-E8 sign gate for the oriented physical current

With \(q_0=r^2\), \(q_1=r^4-s^2r^2\), and \(b=(1-s^2+r^2)/2\), define the complete projected source

\[
\mathscr F_\Lambda(s,r)=
\frac1{4096A_6(\Lambda)}\mathcal D\left[
\frac{e^{2s}}8\sum_{a,b}T_{a,b}^\Lambda(s+r,s-r)\right].
\]

Then \(\mathscr F_\Lambda=\Phi(s+r)\Phi(s-r)\), and the required stronger bound is exactly

\[
\boxed{
\iint e^{2t(s^2+r^2)}
\{q_j+\kappa_j(t,x)b\}\cos(2xs)
\mathscr F_\Lambda(s,r)\,ds\,dr\ge0
\quad\hbox{on the full }S_j.
}
\tag{14}
\]

For a declared locally bounded source-derived \(\kappa_j\), (14) is the original \(\mathcal L_j\ge-\kappa_jE\), now expressed through an explicit finite exceptional-lattice bridge. It is an analytic target, not a proved inequality.

A sharper boundary gate, communicated by the parallel boundary investigation, retains the negative part only after complete arithmetic reconstruction. Fix a locally positive radius \(R\) and write

\[
\varphi_j(\theta)=h_j(t,x)\Re h_j(t,x+Re^{i\theta}),
\qquad q(\theta)=1-\cos2\theta,
\]

\[
\mathfrak D_j=\frac1{2\pi}\int_0^{2\pi}q(\theta)
\bigl(\varphi_j(\theta)\bigr)_-\,d\theta.
\]

Real analyticity and the second Fourier coefficient of the boundary circle give the exact identity

\[
\mathcal L_j=\frac4{R^2}\left[
\frac1{2\pi}\int q(\theta)\varphi_j(\theta)\,d\theta-h_j^2\right]
\quad\text{on }S_j.
\tag{15}
\]

Thus the genuinely new signed lemma

\[
\boxed{\mathfrak D_j\le\eta_j(t,x)E\quad(j=0,1)}
\tag{16}
\]

would prove \(\mathcal L_j\ge-4(1+\eta_j)E/R^2\), since \(h_j^2\le E\) on the corresponding full stationary set. The source product in \(\varphi_j\) can be replaced exactly by (4), with the finite character sum completed before taking its real part or negative part. Equations (7)–(13) explain why sectorwise absolute norms do not establish (16).

In the octonionic notation, \(\varphi_j\) is the real, oriented coefficient of the twisted associator used for the physical current; squaring that associator loses the sign. Polarized norm composition gives a determinant square, not (16). This is the precise new source hypothesis that the octonionic boundary calculation needs.

## 7. Assessment

The anisotropic twisted E8 bridge is exact, global, preserves heat and independent coordinates, and has a finite globally integrable differentiated-sector decomposition. It improves the applicability analysis beyond dismissing E8 solely for its different scalar Mellin transform. Its projection is nevertheless an explicit classical duplication identity, and the untwisted differentiated source has a rigorously negative sector. At positive heat, the auxiliary arithmetic amplitudes observe complex shifts of H and do not vanish at a possible physical collision; an octonionic norm estimate cannot turn them into an energy-relative defect for free.

The highest-value remaining analytic task is therefore (16), or an equivalent complete signed estimate (14), retaining the finite character packet and full source before taking a negative part. No stronger pointwise energy-relative signed lower bound for the actual theta field has been proved in this note.


The complete boundary current has the explicit two-source representation
\[
\varphi_j(\theta)=\frac14\Re\iint_{\mathbb R^2}
(iu)^j(iv)^j e^{t(u^2+v^2)}
e^{iz_\theta u+ixv}\Phi(u)\Phi(v)\,du\,dv.
\]
Thus (4) can be inserted with both independent coordinates and every heat
factor intact, and the finite character packet must be completed before
taking a negative part. The [boundary theorem and exact original-cutoff
payment](../02_signed_cusp_control/46_OCTONIONIC_BOUNDARY_CURRENT_AND_SIGNED_CUTOFF_TARGET_20261015.md)
give the quantitative sufficient estimate; they do not infer it from the
lattice identity. [Review 29](../../reviews/29_OCTONIONIC_SIGNED_BOUND_ANALYTIC_REVIEW_20261015.md)
records independent analytic checking. No numerical experiment is used.

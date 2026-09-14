# A superspace action for the relative boundary pairing

13 September 2026. Exploratory continuation; the manuscript and background
remain unchanged.

## Result and scope

The relative gamma complex has an explicit quantization by one bosonic field
and two fermionic fields per channel. A one-Grassmann-coordinate superspace
action realizes its nilpotent differential. Its physical Hilbert space has a
positive ordinary inner product, and its Hamiltonian is an anticommutator of a
supercharge with its actual Hilbert adjoint. The gamma boundary states are
zero-energy fermionic states. Their full Hermitian pairing, including the
single-channel contact term, obeys a Ward identity under a family of changes
to the massive excitation frequencies.

There are two qualifications with mathematical consequences. A local boundary
insertion requires ground-state preparation before its pairing is protected.
For the infinite gamma tower, a common preparation rate leaves a divergent
finite-time response. A specified mass-dependent rate repairs this and gives
the uniform bound

\[
 0\le Z_{T,\lambda}-K
 \le \frac{4e^{-T/4}}{1-e^{-6T}}\,I,\qquad T>0,\quad\lambda\ge0.       \tag{1}
\]

This bounds preparation error, not the missing arithmetic correction.
A separate cutoff-dependent preparation limit works with common channel
rates. Standard superpotential non-renormalization does not by itself remove
the fixed-time source divergence; Sections 6.1–6.2 make this distinction precise.

At fixed first-prime coupling the same superspace construction works, but
its protected pairing is precisely the earlier exponential-loop response.
Changing that coupling changes the differential and its harmonic states; it
is not the deformation covered by the Ward identity. The known nonzero
diagonal derivative jump therefore survives. Neither the protected bulk
deformation nor any net finite-rank boundary modification completes this
model to the full Weil form.

The new content is the action, canonical quantization, open boundary
conditions, ordinary boundary correlation, controlled tower preparation, and
the distinction between the two deformation parameters. The relative complex,
gamma identity, exponential-loop ansatz, and its residual obstruction are
inherited. The protected answer still has the original classical
minimum-energy realization. No quantum-exclusive positivity mechanism,
arithmetic selection principle, new positivity interval, or RH proof follows.

The construction develops the proposals in the
[relative-complex candidate](../../../../brainstorm/candidate-bulk-theories/01_RELATIVE_COMPLEX.md)
and the [superspace brainstorming note](../../../../brainstorm/SUPERSPACE_COHOMOLOGICAL_BOUNDARY_PAIRINGS_20260912.md).
The [preceding covariance audit](QUANTUM_COVARIANCE_AUDIT_AND_FINITE_BLOCK_OBSTRUCTION_20260913.md)
concerns a different observable: bosonic derivative correlations in Gaussian
vacua. Here the prepared observable creates an actual harmonic fermionic
state. The present action is a free cohomological theory, not an interacting
completion or a four-dimensional chiral-superfield model.

## 1. Target, coordinates, and domain

Let \(I_L=(-L/2,L/2)\), let \(E_L\) extend by zero, and put \(F=E_Lf\).
Use
\[
 \widehat F(\tau)=\int_{\mathbb R}F(x)e^{-i\tau x}\,dx,\qquad
 \langle F,G\rangle=\int_{\mathbb R}\overline F G\,dx.
\]
The arithmetic translation coordinate is \(x\); \(s=\tau^2\).
The coordinate \(y\ge0\) introduced below is Euclidean preparation time,
and real physical time \(t\) has evolution \(e^{-itH}\), with \(\hbar=1\).
Neither time variable is the zeta shift, support length \(L\), channel label,
or arithmetic coupling.

The required kinetic form is
\[
\begin{split}
 a_k&=2k+\tfrac12,\qquad c_a=2/a,\\
 B(s)&=\sum_{k\ge0}\frac2{a_k}\frac{s}{s+a_k^2}
 =\Re\psi\left(\tfrac14+\tfrac i2\sqrt{s}\right)-\psi(\tfrac14),\\
 K[F]&=\frac1{2\pi}\int_{\mathbb R}B(\tau^2)|\widehat F(\tau)|^2\,d\tau.
\end{split}                                                        \tag{2}
\]
The series identity follows by taking real parts of the
[digamma partial fractions](https://dlmf.nist.gov/5.7#E6).
Its finite-interval form domain is
\[
 \mathcal D_{\log}(I_L)=
 \left\{f\in L^2(I_L):
  \int_{\mathbb R}\log(2+|\tau|)|\widehat{E_Lf}(\tau)|^2d\tau<\infty
 \right\}.                                                        \tag{3}
\]
All auxiliary spatial fields live on the whole line. We compress their
response to \(I_L\); we do not replace their dynamics by a Dirichlet
Laplacian on the input interval.

Keep the entire zero-shift target in view:
\[
\begin{split}
 Q_{0,L}[f]={}&K[E_Lf]+w_0\|f\|^2
 +2|C(f)|^2-2|S(f)|^2\\
 &-\sum_{\substack{p,m\ge1\\m\log p<L}}
   (\log p)p^{-m/2}\langle f,(T_{m\log p}+T_{m\log p}^*)f\rangle,\\
 w_0={}&\psi(\tfrac14)-\log\pi
       =-\gamma-\tfrac\pi2-3\log2-\log\pi,\\
 C(f)={}&\int_{I_L}f(x)\cosh(x/2)\,dx,\qquad
 S(f)=\int_{I_L}f(x)\sinh(x/2)\,dx.
\end{split}                                                        \tag{4}
\]
Here \(p\) runs over primes, \(m\) over positive integers, and
\(T_d=E_L^*U_dE_L\), where \(U_dF(x)=F(x-d)\).
The pole operator \(\mathcal P_L\) has kernel
\(2\cosh((x-x')/2)\), hence rank at most two. Its displayed signed
decomposition cannot be declared positive. Equations (2) and (4) are
different targets.

## 2. The closed relative complex and its physical Hilbert space

For one channel \(a>0\), set
\[
\begin{split}
 E^0&=L^2(\mathbb R),\qquad E^1=L^2(\mathbb R;\mathbb C^2),\\
 \mathcal D_a u&=(u,a^{-1}u'),\qquad \operatorname{Dom}\mathcal D_a=H^1(\mathbb R),\\
 \mathcal D_a^*(v,w)&=v-a^{-1}w',\qquad
 \operatorname{Dom}\mathcal D_a^*=L^2(\mathbb R)\oplus H^1(\mathbb R),\\
 G_a&=\mathcal D_a^*\mathcal D_a=I+a^{-2}A,\qquad
 A=-\partial_x^2,\qquad \operatorname{Dom}G_a=H^2(\mathbb R).
\end{split}                                                        \tag{5}
\]
The adjoint uses the ordinary positive metrics displayed here. The first
component makes \(\mathcal D_a\) injective with closed range, and \(G_a\ge I\).
The polar isometry \(U_a=\mathcal D_aG_a^{-1/2}\) is bounded. Consequently
\[
 P_a=I-U_aU_a^*
     =I-\mathcal D_aG_a^{-1}\mathcal D_a^*                         \tag{6}
\]
is a bounded orthogonal projection onto \(\ker\mathcal D_a^*\).
The last expression means its bounded extension; it is not an unrestricted
product of unbounded operators.

Quantize on
\[
 \mathscr F_a=\Gamma_s(E^0)\otimes\Gamma_a(E^1),                    \tag{7}
\]
with bosonic annihilation field \(b\), fermionic annihilation field \(c\),
and their physical adjoints. The two components of \(c\) are positive-metric
CAR degrees of freedom, not indefinite-metric ghosts. At a finite spatial
regulator, ordinary CCR and CAR give
\[
\begin{split}
 Q&=c^\dagger\mathcal D_a b,\qquad
 Q^\dagger=b^\dagger\mathcal D_a^*c,\qquad Q^2=0,\\
 \{Q,Q^\dagger\}
   &=b^\dagger G_ab+c^\dagger\mathcal D_a\mathcal D_a^*c.
\end{split}                                                        \tag{8}
\]
Repeated indices include the spatial pairing. On the one-excitation sector,
\[
 Qb^\dagger(u)\Omega=c^\dagger(\mathcal D_au)\Omega,\qquad
 Qc^\dagger(v)\Omega=0,\qquad
 Q^\dagger c^\dagger(v)\Omega=b^\dagger(\mathcal D_a^*v)\Omega.       \tag{9}
\]
Thus this sector is exactly the relative Hilbert complex, with harmonic
one-fermion space \(\ker\mathcal D_a^*\). This is an ordinary ground-state
realization of its cohomology.

Now fix a positive self-adjoint \(R\) strongly commuting with \(G_a\). The
family used for the tower will be
\[
 R_{a,\lambda}=a^2(I+\lambda G_a),\qquad \lambda\ge0.                \tag{10}
\]
Define
\[
\begin{split}
 H_R&=b^\dagger RG_ab+c^\dagger\mathcal D_aR\mathcal D_a^*c,\\
 V_R&=b^\dagger R\mathcal D_a^*c,\qquad H_R=\{Q,V_R\},\\
 Q_R&=c^\dagger\mathcal D_aR^{1/2}b,\qquad
 Q_R^\dagger=b^\dagger R^{1/2}\mathcal D_a^*c,\\
 H_R&=\{Q_R,Q_R^\dagger\}\ge0,\qquad [Q,H_R]=0.
\end{split}                                                        \tag{11}
\]
The fixed cohomological charge \(Q\) and canonical dynamical charge \(Q_R\)
are different when \(R\ne I\). The fixed charge supplies the deformation Ward
identity; the latter supplies the physical adjoint anticommutator generating
time. Equating \(V_R\) with \(Q^\dagger\) would be incorrect.

For completeness, the continuum Hamiltonian is defined without a formal
sum of zero-point energies. Its boson one-particle operator is \(h_B=RG_a\);
its fermion operator is
\[
 h_F=0\big|_{\ker\mathcal D_a^*}\ \oplus\
       U_a(RG_a)U_a^*\big|_{\operatorname{ran}\mathcal D_a}.         \tag{12}
\]
The massive summand domain is
\(\{U_au:u\in\operatorname{Dom}(RG_a)\}\); the harmonic summand has its full
Hilbert domain. The Fock Hamiltonian is the sum of their nonnegative second
quantizations, defined by its closed quadratic form. For (10), \(h_B\) has
symbol
\[
 (a^2+s)\bigl(1+\lambda(1+s/a^2)\bigr).                            \tag{13}
\]
In particular its domain is \(H^2\) at \(\lambda=0\) and \(H^4\) at
\(\lambda>0\). The anticommutator statements in (11) hold first on finite
excitation states with bounded spatial spectral support. Normal-mode
decomposition on each excitation sector defines the closed charges and
extends (11) as the equality of closed nonnegative forms. This uses paired
massive boson and fermion modes of identical frequency and zero-frequency
harmonic fermions; it does not assume that the displayed monomials act on
every Fock vector.

The ground space is
\[
 \mathbb C\Omega_B\otimes\Gamma_a(\ker\mathcal D_a^*).               \tag{14}
\]
It is highly degenerate. We select the empty Fock vacuum \(\Omega\)
explicitly and form boundary matrix elements, not a trace or a normalized
average over this ground space.

The relation between nilpotent charges, positive Hamiltonians, and harmonic
ground states is standard in supersymmetric quantum mechanics; see
[Witten, *Supersymmetry and Morse theory*](https://www.ias.edu/sites/default/files/sns/files/supersymmetry-and-morse-theory-1982.pdf)
and [Tong's SUSY quantum mechanics notes](https://www.damtp.cam.ac.uk/user/tong/susy/susyqm.pdf).
Equations (5)–(14) specify the particular field theory used here.

## 3. An explicit one-coordinate superspace action

Use one odd coordinate \(\theta\), with \(\int d\theta\,\theta=1\).
The off-shell odd derivation \(q=[Q,\,\cdot\,]_{\mathrm{gr}}\) acts by
\[
 qb=0,\qquad q\bar c=0,\qquad
 qc=\mathcal D_ab,\qquad q\bar b=\bar c\,\mathcal D_a,\qquad q^2=0.  \tag{15}
\]
Bars are independent coherent-state integration variables. Their canonical
operators are the Hilbert adjoints in (8). Define
\[
 \mathbf B=b,\quad
 \bar{\mathbf B}=\bar b+\theta\bar c\,\mathcal D_a,\quad
 \mathbf C=c+\theta\mathcal D_ab,\quad
 \bar{\mathbf C}=\bar c.                                         \tag{16}
\]
The \(\theta\) coefficient implements (15). On a Euclidean slab \(0\le y\le T\)
the action is
\[
\begin{split}
 S_R={}&\int_0^Tdy\left[
   \bar b\,\partial_yb+\bar c\,\partial_yc+
   \int d\theta\,\bar{\mathbf B}R\mathcal D_a^*\mathbf C
   \right]\\
 &-\bar b(T)b(T)-\bar c(T)c(T).
\end{split}                                                        \tag{17}
\]
All spatial integrations are implicit. Its superspace term is exactly
\[
 \int d\theta\,\bar{\mathbf B}R\mathcal D_a^*\mathbf C
 =\bar b\,RG_ab+\bar c\,\mathcal D_aR\mathcal D_a^*c
 =q(\bar bR\mathcal D_a^*c).                                     \tag{18}
\]
The graded Leibniz rule gives
\[
 q(\bar b\,\partial_yb)=\bar c\,\mathcal D_a\partial_yb,\qquad
 q(\bar c\,\partial_yc)=-\bar c\,\mathcal D_a\partial_yb.            \tag{19}
\]
The endpoint terms cancel under \(q\) by the same rule. The component action
is therefore off-shell \(q\)-invariant. At fixed \(\mathcal D_a\),
\(\partial_\lambda S_R\) is the integral of
\(q(\bar b\,\partial_\lambda R\,\mathcal D_a^*c)\).

This is minimal cohomological superspace. The adjoint transformation is
generated by the actual \(Q^\dagger\):
\[
 q^\dagger b=-\mathcal D_a^*c,\quad q^\dagger\bar b=0,\quad
 q^\dagger c=0,\quad q^\dagger\bar c=\bar b\mathcal D_a^*.           \tag{20}
\]
Off shell, \(\{q,q^\dagger\}\) is the adjoint action of the operator in (8);
it is not an asserted superspace identity \(\{q,q^\dagger\}=\partial_y\).
Physical time evolution is generated by (11), with \(Q_R\) and its adjoint.
This distinction avoids imposing an unjustified relativistic superspace
algebra on the relative complex.

Before prime coupling, (17) is spatially local: (5) is differential and (10)
is polynomial in \(G_a\). The \(\lambda\) term changes the massive dispersion
from second to fourth spatial order while preserving the harmonic sector.
The coherent-state action is first order in time and contains Grassmann
variables. It is not a nonnegative real component functional; its physical
positivity is the canonical Hilbert-space statement (11).

## 4. Boundary conditions and the measured correlation

Define (17) by time slicing unnormalized bosonic and fermionic coherent
states. Impose open coherent boundary data
\[
 b(0)=b_i,\quad \bar b(T)=\bar b_f,\qquad
 c(0)=\eta_i,\quad\bar c(T)=\bar\eta_f.                             \tag{21}
\]
These fix one endpoint for each first-order variable, not both endpoints of
each variable. The final terms in (17) are required for these data.
The exact Gaussian coherent kernel is
\[
 \mathcal K_R
 =\exp\left(\bar b_f e^{-Th_B}b_i+
             \bar\eta_f e^{-Th_F}\eta_i\right).                    \tag{22}
\]
The boundary conventions and coherent-state construction can be compared
with [Skinner's supersymmetry notes, chapter 3](https://www.damtp.cam.ac.uk/user/dbs26/SUSY/chap3.pdf),
especially the fermionic coherent-state derivation. Here (22) also follows
directly from the normally ordered Hamiltonian, so a formal continuum
functional measure is unnecessary.

There are no periodic fermion conditions, supertrace, or Witten-index
substitution. Set boson boundary sources to zero and extract the one-fermion
coefficient in (22). With \(J F=(F,0)\), it gives the full Hermitian pairing
\[
\begin{split}
 C_{a,T,R}(g,f)
 &=c_a\langle\Omega,c(JE_Lg)e^{-TH_R}
                    c^\dagger(JE_Lf)\Omega\rangle\\
 &=c_a\langle JE_Lg,e^{-Th_F}JE_Lf\rangle\\
 &=\left\langle
   \sqrt{c_a}e^{-Th_F/2}JE_Lg,\,
   \sqrt{c_a}e^{-Th_F/2}JE_Lf\right\rangle.
\end{split}                                                        \tag{23}
\]
We use \(c(v)\) conjugate-linear and \(c^\dagger(v)\) linear in \(v\).
The empty-vacuum amplitude is one. The last line establishes ordinary
positivity and gluing of two half preparations, including complex inputs.

Equation (12) yields the bounded-operator identity
\[
 e^{-Th_F}=P_a+
   \mathcal D_aG_a^{-1}e^{-TRG_a}\mathcal D_a^*.                    \tag{24}
\]
Consequently the multiplier of (23), for (10), is
\[
 C_{a,T,\lambda}(s)=\frac2a
 \left[
    \frac{s}{a^2+s}
   +\frac{a^2}{a^2+s}
       e^{-T(a^2+s)(1+\lambda(1+s/a^2))}
 \right].                                                       \tag{25}
\]
This is derived from the bare action and local boundary injection \(J\).
No square root of the unknown Weil operator has been inserted.

The \(T\to\infty\) boundary preparation is
\[
 \Gamma_a f=\sqrt{c_a}P_aJE_Lf,\qquad
 C_{a,\infty}(g,f)=\langle\Gamma_ag,\Gamma_af\rangle.                \tag{26}
\]
The state \(c^\dagger(\Gamma_af)\Omega\) has exactly zero energy.
For every nonzero whole-line \(L^2\) input its norm is nonzero, since
\(s/(a^2+s)>0\) except on a set of measure zero. The effective prepared
insertion is spatially nonlocal, as (6) makes explicit.

Fourier inversion of (25) at \(T=\infty\) gives the single-channel kernel
\[
 \frac2a\delta(x-x')-e^{-a|x-x'|}.                                 \tag{27}
\]
Thus the contact is fixed by the same calculation as the nonlocal term.
The whole-line preparation includes the exterior response. Compression
retains all cross terms between subintervals; discarding them would define
a different boundary form.

## 5. The Ward identity and the boundary obstruction to a stronger claim

Let \(|f\rangle=c^\dagger(\Gamma_af)\Omega\) and similarly \(|g\rangle\).
Both are annihilated by \(Q,Q^\dagger,H_R\). At finite regulator Duhamel's
formula gives
\[
\begin{split}
 \partial_\lambda\langle g|e^{-TH_R}|f\rangle
 =-\int_0^T
 \langle g|e^{-(T-u)H_R}
       \{Q,\partial_\lambda V_R\}e^{-uH_R}|f\rangle\,du
 =0.
\end{split}                                                        \tag{28}
\]
Move \(Q\) to the bra in the first anticommutator term, using
\(\langle g|Q=0\), and to the ket in the second, using \(Q|f\rangle=0\).
The charge commutes with the propagator. Equation (24) proves the same
identity directly in the continuum, avoiding differentiation on an
unspecified unbounded-operator domain. Section 6 justifies the tower limit.
The identity also preserves all cross pairings, not only diagonal norms.

This is a nontrivial protected deformation: massive frequencies change
according to (13), while the full surviving Hermitian boundary pairing
does not. It assumes fixed \(\mathcal D_a\), fixed Hilbert metric, and fixed
prepared source classes. It supplies no invariance under arbitrary changes
to those data. Spatial translations remain represented on the fields and
commute with \(Q\); they have not been declared \(q\)-exact.

An unprepared local source gives a different result. Its ket is \(Q\)-closed
by (9), but its bra does not annihilate \(Q\) unless its fermion profile is
harmonic. In (21), the putative vacuum condition \(\bar b_f=0\) transforms as
\(q\bar b_f=\bar\eta_f\mathcal D_a\), which is generally nonzero.
Invariance of the action alone therefore does not imply invariance of this
boundary problem.

Explicitly, with \(G=1+s/a^2\), equation (25) implies
\[
 \partial_\lambda C_{a,T,\lambda}(s)
 =-T\,c_a a^2G\,e^{-Ta^2G(1+\lambda G)}<0,\qquad T>0.              \tag{29}
\]
The extra finite-time term is positive and deformation-dependent.
Projection at infinite preparation time, or already harmonic endpoint
states, is essential. This is a concrete boundary check of the usual
restriction that localization arguments require suitable observables and
boundary data; see the general framework in
[Pestun and Zabzine's introduction to localization](https://arxiv.org/abs/1608.02953).
No measure-based anomaly cancellation is being assumed in place of (28).

## 6. Infinite-tower preparation with a uniform error bound

The raw source \((\sqrt{c_{a_k}}JF)_k\) is not a vector in the channel direct
sum: \(\sum_k2/a_k=\infty\). A finite preparation time does not automatically
repair this. If \(R=I\) for every channel, its extra multiplier is
\[
 \sum_k\frac2{a_k}\frac1{G_k}e^{-TG_k},\qquad
 G_k=1+s/a_k^2.
\]
For every fixed finite \(\tau\), its summands are asymptotic to
\((2/a_k)e^{-T}\); hence the sum diverges. Tonelli's theorem gives divergent
quadratic form for every nonzero input. This is not an ultraviolet
normalization that can silently be dropped.

Use the explicit choice (10) instead. The finite-time source is defined by
preparing each channel separately and then taking the Hilbert direct sum:
\[
 \Gamma_{T,\lambda}f
 =\left(\sqrt{c_{a_k}}e^{-Th_{F,k}/2}JE_Lf\right)_{k\ge0}.           \tag{30}
\]
The channel rates \(a_k^2\) are a dynamical choice, not a derived arithmetic
selection law. They do not alter any harmonic projection.
By (25) the difference from the protected form has multiplier
\[
 e_{T,\lambda}(\tau)=
 \sum_k\frac2{a_kG_k}
       e^{-Ta_k^2G_k(1+\lambda G_k)}.                              \tag{31}
\]
Since \(G_k\ge1\), \(\lambda\ge0\), \(2/a_k\le4\), and
\[
 a_k^2=4k^2+2k+\tfrac14\ge6k+\tfrac14,
\]
we obtain
\[
 0\le e_{T,\lambda}(\tau)
 \le\sum_k\frac2{a_k}e^{-Ta_k^2}
 \le\frac{4e^{-T/4}}{1-e^{-6T}}=:\epsilon(T).                      \tag{32}
\]
All inequalities are analytic and uniform in \(\tau\) and \(\lambda\).
They prove (1) as an inequality of closed forms on (3); the form difference
extends to a bounded positive operator of norm at most \(\epsilon(T)\).
For cross pairings the error is at most
\(\epsilon(T)\|g\|\|f\|\).

Writing \(\Gamma_\infty f=(\sqrt{c_{a_k}}P_{a_k}JE_Lf)_k\), the harmonic
and massive components are orthogonal. Thus
\[
 \|\Gamma_{T,\lambda}f-\Gamma_\infty f\|^2
 =\langle f,(Z_{T,\lambda}-K_L)f\rangle
 \le\epsilon(T)\|f\|^2.                                         \tag{33}
\]
Here \(K_L\) is the closed form compression of \(B(A)\), not
\(B(-\partial_{x,I_L}^2)\) with an imposed endpoint condition.
The maps in (30) and (33) have exactly domain (3), since their squared
norms are \(K[E_Lf]\) plus a bounded positive form. Their values define
one-fermion vectors in the Fock space over the channel direct sum.
The protected vector is in the kernel of the direct-sum Hamiltonian;
its preparation requires no additional regularity beyond (3).

This proves existence, convergence, and the tower Ward identity for every
admissible input. It uses neither an infinite coherent displacement nor an
unrenormalized sum of the contacts in (27). The preparation bound tends to
zero exponentially as \(T\to\infty\); its approximate values at \(T=16\)
and \(T=32\) are \(0.073263\) and \(0.00134185\), respectively.
It controls this auxiliary limit only.

### 6.1 A common-rate alternative: control the order of limits

The fixed-time divergence does not obstruct the gamma pairing itself, and
mass-dependent rates are not the only way to define its preparation.
Retain the first \(N\) complete channel multiplets, keep \(R=I\), and set
\(\sigma_N=\sum_{k<N}2/a_k=\log N+O(1)\).
Write \(K_N\) for the truncated gamma form and \(C^I_{N,T}\) for the
unprojected finite-time form at these common rates. Equation (24) gives
the bounded-operator estimate
\[
 0\le C^I_{N,T}-K_N\le e^{-T}\sigma_N I.                           \tag{33a}
\]
The bound is attained at frequency zero for the whole-line multiplier;
after interval compression it remains an upper bound.

For every fixed \(N\), projection as \(T\to\infty\) therefore gives
\(K_N\), and monotone convergence gives \(K_N[f]\to K[f]\) on (3).
The ordered limit \(\lim_{N\to\infty}\lim_{T\to\infty}\) is well defined.
The reverse order diverges at every finite \(T\). A simultaneous limit
also works: take
\[
 T_N=\log\sigma_N+\eta_N,\qquad \eta_N\longrightarrow+\infty.
                                                                    \tag{33b}
\]
Then the preparation error is at most \(e^{-\eta_N}\|f\|^2\), and
\(C^I_{N,T_N}[f]\to K[f]\) for every \(f\) in (3). The truncated harmonic
source vectors converge in norm by the gamma form sum, and their massive
remainders have squared norm bounded by (33a), so this is also convergence
of the prepared vectors. Only a preparation time growing beyond
\(\log\log N\) by a diverging additive amount is needed.

Thus common rates can be retained when the cutoff and preparation time are
coordinated. Equation (32) supplies a different advantage: a well-defined
infinite tower at each fixed positive preparation time. Neither argument
turns a divergent raw infinite source into a Fock vector by formal
cancellation. The estimates also apply at fixed first-prime coupling,
using \(G_{a,\xi}\ge1\).

### 6.2 What SUSY non-renormalization can and cannot supply here

The suggestion to consider non-renormalization is relevant to whether a
protected construction survives quantization and regulator removal.
The familiar four-dimensional \(\mathcal N=1\) statement protects the
holomorphic Wilsonian superpotential against perturbative corrections.
It does not generally protect the Kähler potential or the field
normalizations entering Hermitian two-point functions.
[Tong, section 3.3](https://www.damtp.cam.ac.uk/user/tong/susy/susy3.pdf)
explicitly separates these issues, including the Wilsonian versus 1PI
distinction. Holomorphy also constrains nonperturbative contributions
without universally eliminating them; see
[Seiberg's non-renormalization argument](https://arxiv.org/abs/hep-ph/9309335).

The one-coordinate cohomological theory (17) is not such a chiral
superfield theory. Its observable is an ordinary Hermitian pairing,
depending on the actual adjoint and boundary metric. Calling its
\(\theta\) integral an F-term would not establish the hypotheses of that
theorem. More restrictive theories can have additional protection of
kinetic data, but such extra symmetry has not been constructed here.

There is a direct reason the common-rate divergence is not cured by
perturbative non-renormalization. The Hamiltonian is already free and
normally ordered, with vacuum amplitude one. At fixed \(\tau\),
\[
 \frac1{G_k}e^{-TG_k}
   =e^{-T}+O_{T,\tau}(a_k^{-2}),
 \qquad
 (C^I_{N,T}-K_N)(\tau)
   =e^{-T}\log N+O_{T,\tau}(1).                                  \tag{33c}
\]
This is a positive sum of external one-fermion state norms in an exact
Gaussian correlation. There are no interaction-loop corrections left
to cancel it. For a fixed smooth compact input the same leading term
is \(e^{-T}\log N\,\|f\|^2\): the remainder is bounded using
\[
 \left|G^{-1}e^{-TG}-e^{-T}\right|
 \le e^{-T}(T+1)(G-1),\qquad G\ge1,
\]
and \(\sum_k2/a_k^3<\infty\). Dividing by the vacuum amplitude changes
nothing; that division is already included. Replacing the sum by a
boson-minus-fermion supertrace would change the observable and lose
the required ordinary norm interpretation. Subtracting a contact or
rescaling the source would likewise require a new derivation of its
metric, normalization, and target identity.

The applicable exact protection in this model is instead (28), for
harmonic boundary states at each complete-multiplet cutoff. Passing it
to the tower uses (32), or the ordered limit and (33a)–(33b). This is a
proved restricted Ward statement and a convergence argument. It should
not be relabeled as general non-renormalization of the Weil pairing.
If an interacting arithmetic boundary sector is later proposed,
non-renormalization could constrain its couplings or composite insertions;
one would still need a theorem about its Hermitian boundary metric and a
uniform channel-limit estimate.

## 7. First-prime coupling changes the differential

Take \(\ell=\log2\), \(r=2^{-1/2}\), and the bounded return operator
\[
 \mathcal A_2=\ell\sum_{m\ge1}r^mU_{m\ell},\qquad
 M_\xi=\exp\bigl[\xi(w_0I-2\mathcal A_2)\bigr],\qquad 0\le\xi\le1.  \tag{34}
\]
The coefficients are the original exponential-loop ansatz, prescribed
arithmetic data. They are not selected by the superspace algebra.
The multiplier of \(M_\xi\) is \(m_\xi(\tau)=e^{\xi g(\tau)}\), where
\[
 g(\tau)=w_0-\frac{2\ell r e^{-i\ell\tau}}{1-r e^{-i\ell\tau}},
 \qquad v(\tau)=\Re g(\tau).
\]
It is bounded and boundedly invertible at every fixed \(\xi\); the same is
true uniformly on the compact coupling range used here.
Replace the relative differential by
\[
\begin{split}
 \mathcal D_{a,\xi}u&=(u,a^{-1}M_\xi u'),\\
 \mathcal D_{a,\xi}^*(v_1,v_2)&=v_1-a^{-1}M_\xi^*v_2',\\
 G_{a,\xi}&=I+a^{-2}A|M_\xi|^2.
\end{split}                                                        \tag{35}
\]
The differential and adjoint domains remain those in (5). Translation
multipliers preserve the Sobolev spaces and commute with derivatives.
They now make the spatial action nonlocal.

For each fixed \(\xi\), repeat (10)–(28) with
\(R_{a,\xi,\lambda}=a^2(I+\lambda G_{a,\xi})\).
Its protected channel response is
\[
 z_{a,\xi}(s,\tau)=\frac2a\frac{x}{1+x},\qquad
 x=\frac{s e^{2\xi v(\tau)}}{a^2},                                \tag{36}
\]
and its entire tower is
\[
 Z_\xi(\tau)=B\bigl(s e^{2\xi v(\tau)}\bigr).                       \tag{37}
\]
The domain is still (3): the positive bounded multiplier
\(e^{2\xi v}\) is bounded away from zero. The bound (32) also holds
uniformly here, because \(G_{a,\xi}\ge1\). Thus \(\lambda\) remains a
protected auxiliary deformation at fixed \(\xi\).

Arithmetic evolution in \(\xi\) is different. It changes \(Q\), its adjoint,
and the harmonic projection. For any differentiable full-column-rank
finite-regulator differential \(D\), differentiating
\(P=I-D(D^*D)^{-1}D^*\) gives
\[
 \dot P=-P\dot D\,G^{-1}D^*-DG^{-1}\dot D^*P.                       \tag{38}
\]
For (35), this identity holds pointwise in Fourier space, and gives
\[
 \partial_\xi z_{a,\xi}
 =\frac2a\,\frac{2v x}{(1+x)^2},\qquad
 \partial_\xi Z_\xi
 =2v\,s e^{2\xi v}B'\bigl(s e^{2\xi v}\bigr).                      \tag{39}
\]
The channel series can be differentiated on bounded frequency sets by its
summable large-\(a\) tail. Its resulting multiplier is also bounded at
large frequency, since \(tB'(t)\to1/2\). These are valid form derivatives
on the common domain, not just a formal finite-series identity.

In particular \(v<0\) at every phase:
\[
 v\le w_0+\frac{2\ell r}{1+r}<0.
\]
The first inequality follows by minimizing
\(\Re(z/(1-z))\) on \(|z|=r\); the second also follows from
\(2\ell r/(1+r)<\ell\) and the displayed expression for \(w_0\).
Equation (39) is nonzero for \(s>0\).
Therefore the fixed-source Hermitian pairing is not protected against
turning on this arithmetic coupling. An isomorphism between abstract
cohomology spaces does not identify their embedded source pairings.

## 8. Full first-prime target and a scoped stopping result

Suppose \(\log2<L\le\log3\), so the only active prime-power displacement in
(4) is \(\log2\). The higher repetitions in (34) still matter for the
nonlinear response, even though their direct compressed translations vanish.
At \(\xi=1\) define
\[
 \rho(\tau)=B(s e^{2v(\tau)})-B(s)-v(\tau),\qquad
 \mathcal R_L=E_L^*\rho(-i\partial_x)E_L.
\]
The full finite-interval form identity is
\[
 W_L=Z_{1,L}+\mathcal P_L-\mathcal R_L.                            \tag{40}
\]
Indeed the compression of \(v=w_0-\ell\sum_{m\ge1}
r^m(U_{m\ell}+U_{m\ell}^*)\) is exactly the contact and active prime term
in (4). The sign and both pole amplitudes in (40) are retained.

Here is a short independent restatement of the residual obstruction.
Write \(q_0(\theta)=e^{-2v(\theta/\ell)}>1\), a real analytic periodic
function, and let \(\beta_0\) be the mean of \(q_0-1\). Then \(\beta_0>0\).
The [digamma asymptotic expansion](https://dlmf.nist.gov/5.11#E2) gives,
uniformly in phase,
\[
 \rho(\tau)
 =-\frac{q_0(\ell\tau)-1}{24\tau^2}+O(\tau^{-4}).                  \tag{41}
\]
One can verify the coefficient directly from
\(B(\tau^2)=\log|\tau|-\log2-\psi(1/4)-1/(24\tau^2)
O(\tau^{-4})\). Bounded positive upper and lower bounds on \(q_0\)
justify the uniform substitution.

Expand \(q_0(\theta)-1=\sum_{n\in\mathbb Z}\beta_n e^{in\theta}\);
the coefficients decay exponentially. Subtracting
\(-(q_0(\ell\tau)-1)/(24(1+\tau^2))\) from \(\rho\) leaves a function
whose product with \(\tau^2\) is integrable, including at zero. Its
inverse transform is \(C^2\). Since
\(\mathcal F^{-1}[(1+\tau^2)^{-1}](h)=e^{-|h|}/2\), the residual
kernel \(r_\rho\) has
\[
 r_\rho'(0+)-r_\rho'(0-)=\beta_0/24>0.                             \tag{42}
\]
The shifted exponential terms with \(n\ne0\) are smooth near zero.

To see why this excludes finite rank on every nonempty open input interval,
restrict further to an open subinterval \(J\) of length less than \(\ell\).
The continuous columns \(x\mapsto r_\rho(x-y_j)\), for distinct interior
points \(y_j\in J\), have their sole derivative jumps inside \(J\) at
their respective \(y_j\). Any finite linear dependence forces each
coefficient to vanish by taking its jump. If the compressed operator had
finite rank, normalized approximate delta inputs would put all these
columns in its finite-dimensional, hence closed, range in \(L^2(J)\).
Continuity gives convergence of those images to the columns. Arbitrarily
many independent columns contradict finite rank.

Thus \(\mathcal R_L\) is infinite rank, and so is
\(\mathcal P_L-\mathcal R_L\). The superspace Ward identity fixes \(Z_{1,L}\)
under the displayed \(\lambda\) deformations, so none can remove this
discrepancy. Adding any net finite-rank boundary operator cannot do so
either. This is a restriction on this fixed complex, source, metric, and
class of deformations, not a no-go theorem for supersymmetric theories.

Even retaining finite preparation time does not evade this cusp obstruction.
For fixed \(\xi\), put \(m_*^2=\inf_\tau|m_\xi(\tau)|^2>0\).
Equation (31) gives the stronger frequency estimate
\[
 0\le e_{T,\xi,\lambda}(\tau)
 \le\epsilon(T)e^{-Tm_*^2\tau^2}.                                \tag{43}
\]
Its inverse Fourier transform is smooth, because every polynomial
frequency moment is integrable. Adding this preparation term therefore
cannot cancel (42). Its positive sign alone also says nothing sufficient
about the full signed discrepancy in (40).

## 9. Classical counterpart and physical interpretation

The same protected answer follows from the explicitly known classical
functional
\[
 \frac2a\inf_{u\in H^1(\mathbb R)}
       \left(\|F-u\|^2+a^{-2}\|M_\xi u'\|^2\right).                \tag{44}
\]
The minimizer is \(u=G_{a,\xi}^{-1}F\). Its residual is the orthogonal
projection of \(JF\) onto \(\ker\mathcal D_{a,\xi}^*\); (44) therefore
equals (36) integrated against \(|\widehat F|^2/(2\pi)\).
The finite-time answer also has the explicit classical Gram map (30).
No sign property specific to quantization has been established.

What quantization adds here is a precise account of the surviving states and
their dynamics: massive bosons and fermions pair, harmonic fermions remain
at zero energy, and a measured fermionic two-point matrix element is the
ordinary norm of a prepared state. Superspace makes the nilpotent symmetry
and the permitted bulk deformations explicit. Preparation and the fixed
boundary metric remain substantive parts of the model.

This resolves the proposed first avenue as a concrete construction and
test. A next model capable of changing (40) must change some boundary
pairing data, for example through a specified additional arithmetic
boundary or defect sector with a derived positive Hilbert metric and
source map. A merely \(q\)-exact change of the massive bulk dispersion,
with these boundary states fixed, preserves the incomplete answer.
Any proposed enlargement must compute its entire kernel, contacts, and
pole amplitudes; the action and Ward identity alone will not supply them.

## 10. Reproducible checks and evidentiary limits

The new [checker](../../numerics/check_superspace_boundary_pairing.py) runs
from the investigation root:

    python3 numerics/check_superspace_boundary_pairing.py --output /tmp/superspace-boundary-check.json
    python3 validation/check_package.py

The delivered [diagnostic record](../../numerics/records/superspace-boundary-pairing-diagnostics-20260913.json)
and [validation record](../../numerics/records/superspace-boundary-validation-20260913.json)
are separate from all preceding records.

| Check | What it establishes |
| --- | --- |
| Rational polynomial and Grassmann algebra | The component action identity, kinetic and endpoint invariance, nilpotency on the displayed expressions, harmonic projection, and its variation for a finite rectangular differential |
| Canonical Fock matrices | Diagnostic verification of both charge anticommutators, positivity, commutation, and the vacuum plus one harmonic fermion in a small model |
| Boundary heat kernels | Diagnostic verification of (24), half-time gluing, full complex protected pairing, and the nonzero raw-source derivative |
| First-prime Fourier matrices | Diagnostic verification of the response and changing-projection derivative, including complex phase |
| Prepared tower sums | Sample checks of (32) over masses, frequencies, loop amplitudes, deformation parameters, and times |
| Common-rate cutoff limit | Checks of the logarithmic source divergence and the uniform cutoff-dependent preparation estimate (33a) |

The Fock calculation retains complete sectors of total excitation number
at most two, which the charges preserve. It does not assert a false exact
CCR for a boson cutoff. The finite test differential has \(G\) eigenvalues
1 and 6 and a one-dimensional harmonic fermion sector; the deformation
therefore tests unequal massive frequencies as well as the zero mode.

Rational identities are exact finite calculations. Floating-point spectra,
heat kernels, derivatives, and tail displays are diagnostics, not interval
enclosures. The continuum domains, Ward identity for all admissible inputs,
uniform preparation bound, and infinite-rank obstruction follow from the
arguments above, not from sampled eigenvalues. The package validator checks
integrity and links, not mathematical proof. No historical calculation,
manuscript, background, or brainstorming file is rewritten by this pass.

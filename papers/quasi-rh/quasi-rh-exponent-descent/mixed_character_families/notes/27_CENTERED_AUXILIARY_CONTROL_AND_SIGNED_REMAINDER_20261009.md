# Centered auxiliary control and the remaining signed theorem

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
reasoning effort are not exposed and are not inferred. Parallel derivations
and audits use the same model and are internal checks, not independent
specialist validation or formal proof verification.

This continues [Note 26](26_CENTERED_COMPARISON_FEASIBILITY_20261009.md)
and the [review of Note 25](../../reviews/MIXED_NOTE25_REVIEW_AND_NEXT_STEPS_20261009.md).
The deductions below establish a negligible principal auxiliary layer and
a target-sized growing nonprincipal conductor sector, conditional on the
stated native arithmetic and analytic inputs. A global-family growth input
enlarges that sector. The remaining centered mixed estimate is still open.
The exact centered coefficient and the conductor-preserving row projector
make its next proof obligation explicit.

## 1. One object, one presentation, and the source ledger

Keep the original inverse polynomial \(M_u\), a subset \(J\) of whole
original prime slots, all physical character zeros, the fixed finite ray
presentation, its common orientation, and the original permitted profiles.
Write
\[
 D=U^r,\quad N=U^m,\quad Y_1=U^{1/4},\quad
 Y_2=U^{2m-1/4},\qquad Y_1Y_2=N^2,
\]
\[
 P_u(B;Y)=\sum_{\mathfrak l\ {\rm good}}
                  \psi_u(\mathfrak l)B(N\mathfrak l/Y),\qquad
 S_u(B;Y)=Y^{-1/2}P_u(B;Y),
\]
\[
 C_u=S_u(B;N)^2-S_u(B;Y_1)S_u(B;Y_2),\qquad
 \Delta_u=M_uQ_J(u)C_u.                                      \tag{1}
\]
If two derivative profiles are different, retain the same ordered pair
in both rectangles. Principal cancellation requires the common physical
twist and correlated derivatives of the complete difference; independent
exposed twists are not covered by that cancellation.

Let \(\Omega(Nu/U)\) be a fixed nonnegative bounded smooth annular
envelope that majorizes the radial support of the selected family
\(\mathcal C_+\). Its auxiliary domain contains every physical nonzero
row in its support, including rows with sixth powers. Set
\[
 E_c^\Omega=\sum_{u\ne0}\Omega(Nu/U)|\Delta_u|^2.
                                                               \tag{2}
\]
The target is \(E_c^\Omega\ll U^{1+dr-1/700+\varepsilon}H^b\),
which is sufficient for Note 26's selected centered target by positivity.
This sufficient target is unproved. A direct selected signed estimate is
an alternative and need not pass through (2).

The [30 September primary source](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf)
was read in memory and selected pages were rendered for normalization
checks. Its SHA-256 is
`8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.
No third-party PDF was saved to the repository. The imported inputs are:

- Printed p. 115, Lemma 17.1: the marked original-inverse second moment
  on **all physical element rows** \(Nu\ll U\), for every subcollection
  of the original slots, bounded row-independent prime coefficients,
  either common orientation, and the stated profile/height allowances.
- Printed pp. 120–121, Lemma 17.5 and (17.8): primitive masked lattice
  Poisson with scalar \(Y/\sqrt{Q}\), modulus-one primitive Gauss phase,
  zero nonprincipal frequency at zero, and literal deleted Euler masks.
  Fixed ray restrictions are expanded finitely before primitive induction.
- Printed pp. 21–23, Lemmas 4.8–4.10: the primitive functional equation,
  global subpower growth on fixed lines to the right of \(\beta_*\),
  and deleted Euler factor bounds on a fixed positive half-plane.
  Sections 5 and 7 use the conditional global premise \(\beta_*\le7/8\).
- The native local conductor/reciprocity identification, including
  zero extension, finite bad-prime data and sixth-power multiplicativity.
  The good primitive conductor is comparable to the corresponding good
  radical. Exact local characters, rather than merely their orders, matter.

The source's selected \(d\)-dependent inverse pointwise bound is **not**
used on added rows. The original marked inverse input is directly
\[
 \sum_{u\ne0}\Omega(Nu/U)|M_uQ_J(u)|^2
       \ll_\varepsilon U^{1+\varepsilon}H^{b_{\rm inv}}.       \tag{3}
\]
No division by omitted slots and no marked second moment for
\(M_\dagger\) is used. The capacities retain fixed room:
\[
 r+2z_J\le737/900<1,\qquad 2r+8z_J\le817/450<3,
 \qquad z_J\le2/45,\quad r<73/100.                            \tag{4}
\]
All original disjoint supports and fixed excluded primes remain.

## 2. Principal and bounded-ray auxiliary rows

In a principal-compatible bounded presentation, write
\(u=\eta w^6\), where \(\eta\) is a fixed bounded unit/bad-prime
class (or one of finitely many bounded cores). Its column character is
\[
 \psi_{\eta w^6}(\mathfrak n)=
             \nu_\eta(\mathfrak n)1_{(\mathfrak n,w)=1}.       \tag{5}
\]
Here \(\nu_\eta\) has fixed finite ray conductor, with all its own
zero values retained. Let \(\mathfrak m\) contain that fixed ray
modulus and the original fixed exclusions, with support consisting only
of their fixed defining/excluded primes. The lift
\(b(z)=\nu_\eta((z))1_{((z),S)=1}\) is periodic modulo
\(\mathfrak m\), retains its zero values at every prime dividing
that modulus, and is invariant under the six units. Class number one
gives the exact full-lattice identity
\[
 P_w(B;Y)=\frac16\sum_{z\in\mathcal O_F}
                 b(z)1_{(z,w)=1}B(|z|^2/Y).                 \tag{6}
\]
The annular profile kills \(z=0\). Equivalently the source's primary
generator convention is the congruence \(z\equiv1\pmod3\), a finite
periodic condition. It introduces no angular boundary. This convention
was checked against the [5 October primary source, Section 2](https://raw.githubusercontent.com/openai/math/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex);
no zero-free assertion of that version is used. The equivalent unit lift
already appears in [short-family Note 8](../../short_families/notes/8_SHORT_FAMILY_CENTERED_FACTORIZATION_20261008.md).

Put
\[
 \mathfrak r=\prod_{\substack{\mathfrak p\mid w\\
                              \mathfrak p\nmid\mathfrak m}}\mathfrak p,
 \quad R=N\mathfrak r\le Nw\ll U^{1/6},\quad
 \rho(w)=\prod_{\mathfrak p\mid\mathfrak r}(1-(N\mathfrak p)^{-1}),
\]
and \(\mathcal B_k(B)=\max_{j\le k}\|B^{(j)}\|_\infty\).
For fixed annular support and each integer \(A\ge1\), uniformly for
\(Y/R\ge1\),
\[
 P_w(B;Y)=\kappa_\nu(B)\rho(w)Y+
 O_A\!\left(\mathcal B_{2A+2}(B)\tau(\mathfrak r)(Y/R)^{-A}\right).
                                                               \tag{7}
\]
The constant is
\[
 \kappa_\nu(B)=\frac{\pi}{6\operatorname{covol}(\mathcal O_F)}
   \left(\frac1{N\mathfrak m}\sum_{z\bmod\mathfrak m}b(z)\right)
   \int_0^\infty B(t)\,dt.                                  \tag{8}
\]
For a principal inducing character this is the original good-ideal zeta
residue, including its fixed physical exclusions, times \(\int B\).
For a nonprincipal finite-order ideal character the residue mean vanishes.
An individual artificial ray-indicator split can have a mean; use its
actual common mean at all three lengths.

**Proof of (7).** Expand the exact mask over \(d\mid\mathfrak r\).
For a generator \(\delta\) of \(d\), set \(z=\delta a\) and
\(T=Y/Nd\). Multiplication by \(\delta\) permutes residues modulo
\(\mathfrak m\); hence every divisor branch has the same average
of \(b\). The radial function \(f_B(z)=B(|z|^2)\) satisfies
\[
 |\widehat f_B(\xi)|\ll_A\mathcal B_{2A+2}(B)
                            (1+|\xi|)^{-2A-2}.
\]
Apply \((1-\Delta)^{A+1}\) under its two-dimensional Fourier integral
to obtain this bound. Fixed-coset Poisson at dilation \(\sqrt T\)
has zero term \(\pi T\int B\) times the fixed residue density.
For \(T\ge1\), its other terms have absolute sum at most
\(\mathcal B_{2A+2}(B)T^{-A}\), since the nonzero dual lattice has
a fixed minimum length and exponent \(2A+2>2\). Sum the main terms
using \(\sum_{d\mid\mathfrak r}\mu_F(d)/Nd=\rho(w)\), and use
\(Nd\le R\) for every error. No prime ideal theorem is needed.

After division by \(\sqrt Y\), (7) is
\(S_w(B;Y)=a_w(B)\sqrt Y+e_w(B;Y)\). Every scale in (1) is at
least \(U^{1/4}\), so \(Y/R\gg U^{1/12}\). The complete principal
main product cancels by \(Y_1Y_2=N^2\). Main/error and error/error
products therefore give
\[
 |C_{\eta w^6}|\ll_{A,\varepsilon}
  (1+\mathcal B_{2A+2}(B))^2
            U^{m-1/4-A/12+\varepsilon}.                     \tag{9}
\]
For an exposed common physical norm twist, its scale factor is
\(Y^{it}\); cancellation also uses \(N^{2it}=(Y_1Y_2)^{it}\).
Keep that scalar or absorb the twist consistently into the profile.
Joint derivatives of the complete common-twist expression preserve the
identity. Individual independently exposed twists or separated Fourier
terms need not preserve it. Retain the complete correlated coefficient
before any absolute frequency sum.

For a fixed derivative allowance \(s\) and common \(|t|\le H\),
the relevant profile seminorms are bounded by
\(O(H^{2A+2+s})\). A deliberately conservative squared bound is
\[
 |C_{\eta w^6}|^2\ll
 H^{8A+8+4s}U^{2m-1/2-A/6+\varepsilon}.                     \tag{10}
\]
Additional fixed profile height orders are charged separately. Trivial
\(|M|^2\ll U^r\), \(|Q_J|^2\ll U^{z_J}\), and the
\(O(U^{1/6})\) possible \(w\) give
\[
 E_{\rm bounded\ ray}^\Omega\ll
 H^{8A+8+4s+b_{\rm fix}}
 U^{r+z_J+2m-1/3-A/6+\varepsilon}.                          \tag{11}
\]
For \(H\le U^{1/1000}\), the decay slope is
\(A(1/6-8/1000)=119A/750>0\). Since
\(r+z_J+2m-1/3\le4079/3000\) using even the larger capacity
\(z_J\le(1-r)/2\), any desired fixed suppression power \(L\)
is achieved by a sufficiently large **fixed** internal order \(A\),
then finite derivative orders and an admissible height schedule. That
schedule must also obey the source's cumulative frequency and witness
budgets; the displayed schedule alone does not settle those budgets.
Thus (11) proves \(O(U^{-L})\) under that order of choices. It makes no
claim of arbitrary decay with an arbitrary already fixed height exponent.

## 3. Exact physical core and nonprincipal completion

At good primes decompose each row as \(u=vw^6\), with \(v\)
sixth-power-free. Keep finite unit and bad-prime classes separately. Then
\[
 \psi_{vw^6}(k)=\psi_v(k)1_{(k,w)=1}.                         \tag{12}
\]
Let \(Q=Q_{\psi_u}\) be its primitive conductor norm, and let
\(\mathfrak E\) be the extra squarefree deletion ideal after primes
in that conductor and fixed presentation have been removed. Native
conductor identification gives
\[
 E=N\mathfrak E\le Nw,\quad Q\ll Nv,\quad
 QE\ll Q(U/Nv)^{1/6}\ll U^{1/6}Q^{5/6}.                    \tag{13}
\]
The inducing character is unchanged by \(w^6\). Extra physical zeros
are not removed from the polynomial.

For a primitive nonprincipal inducing character, exact masked Poisson
in the source normalization has the form
\[
 P_u(B;Y)=\frac{Y\gamma}{\sqrt Q}
   \sum_{e\mid\mathfrak E}\frac{\mu_F(e)\psi^*(e)}{Ne}
   \sum_{h\ne0}\overline{\psi^*(h)}
          \widehat B\!\left(\frac{YNh}{Ne Q}\right),
 \qquad |\gamma|=1,                                         \tag{14}
\]
with fixed ideal/lattice and ray constants included. The zero frequency
vanishes. Lattice counting and Schwartz decay show
\[
 \sup_{a>0}a\sum_{h\ne0}|\widehat B(aNh)|<\infty.            \tag{15}
\]
Each divisor in (14) consequently costs \(O(\sqrt Q)\), without
a power of \(E\). Mask divisor counts are \(U^\varepsilon\).
Combining this with trivial ideal counting yields
\[
 |S_u(B;U^x)|^2\ll U^\varepsilon H^b
          \min\{U^x,Q/U^x\}
 \ll U^{\min(x,\kappa-x)+\varepsilon}H^b,
 \quad Q\le U^\kappa,                                      \tag{16}
\]
for every bounded \(x\ge0\). This also covers negative reflected
exponents. It is not valid for principal inducing characters.

Four Cartesian derivatives suffice for a crude order-zero lattice bound:
a common norm twist costs \(H^4\) in the raw completion amplitude,
\(H^8\) in one squared plain response and \(H^{16}\) in a squared
product. Extra requested profile derivatives have finite additional orders.
The source's inverse height order remains symbolic. Thus keep
\(b_{\rm low}=b_{\rm inv}+16+b_{\rm der}\) (or a larger finite
order justified by the prescribed profile family), rather than claiming
a universal numerical height degree.

## 4. A target-sized growing auxiliary conductor sector

Use the moving cutoff
\[
 \kappa_0=m+dr/2-1/1000.                                    \tag{17}
\]
On the closed arithmetic comparison box
\(9/25\le d\le21/50\), \(7/10\le r\le73/100\),
\(2/5\le m\le207/500\),
\[
 21/40\le\kappa_0\le5663/10000,\quad
 \tfrac12<\kappa_0<2m,\quad \kappa_0<4m-\tfrac12.             \tag{18}
\]
These inequalities select the branches of (16) exactly. They give
\[
 |S_u(N)|^4\ll U^{2\kappa_0-2m+\varepsilon}H^b,
\]
while the squared comparison product has exponent
\[
 \min(1/4,\kappa_0-1/4)
 +\min(2m-1/4,\kappa_0-2m+1/4)
 =\kappa_0+1/2-2m\le2\kappa_0-2m.                           \tag{19}
\]
The triangle inequality and the original all-row marked inverse mass (3)
therefore prove the conditional sector estimate
\[
 \boxed{\sum_{\substack{u:\psi_u^*\ {\rm nonprincipal}\\
                        Q_{\psi_u}\le U^{\kappa_0}}}
        \Omega(Nu/U)|\Delta_u|^2
       \ll U^{1+dr-1/500+\varepsilon}H^{b_{\rm low}}.}        \tag{20}
\]
This is a bound for added rows with growing primitive conductor. It does
not transfer the selected inverse pointwise envelope to those rows.
The reserve over saving \(1/700\) is exactly \(1/1750\).
For \(H\le U^{\eta_{\rm ht}}\), any already fixed additional power
loss must satisfy
\[
 L_{\rm other}+b_{\rm low}\eta_{\rm ht}<1/1750.              \tag{21}
\]
Internal finite orders precede the source height choice, and later
external tail orders follow it. Source/witness budgets can require a
smaller height exponent. The fixed cutoff \(\kappa=21/40\) is also
legal; (17) is larger away from the lower corner. These are convenient
reserve choices, not asserted optimal cutoffs.

As an optional stronger decay check, Schwartz decay in (14) also gives
\[
 |P_u(B;Y)|\ll_A\sqrt Q\,U^\varepsilon H^{b_A}(QE/Y)^A.      \tag{22}
\]
From (13), arbitrary suppression at all three scales holds for
\(\kappa<1/10\). For the **complete nonprincipal** centered factor,
only the original and long comparison responses need be small; use a
trivial estimate for the short factor. It suffices that
\[
 m-(1+5\kappa)/6>0,
 \quad\text{hence uniformly }\kappa<7/25.                   \tag{23}
\]
For example \(\kappa=27/100\) leaves gap \(1/120\). This is
a smaller sector than (20). Each desired suppression order has a finite
height degree; its conversion to a power of \(U\) must again be charged.

## 5. Conditional enlargement using the global strip input

There is a larger sector under the imported **global** premise
\(\beta_*\le7/8\). Fix a fresh contour offset
\(0<v\le1/3500\). Lemma 4.9 gives subpower primitive growth on
\(\Re s=7/8+v\), and the primitive functional equation gives its
reflection on \(\Re s=1/8-v>0\). Lemma 4.10 keeps polynomial-size
deleted Euler factors subpower on both lines. Mellin inversion and the
smooth profiles then give, for nonprincipal inducing characters,
\[
 |S_u(B;U^x)|^2\ll
 U^{\delta_g(v)\min(x,\kappa-x)+\varepsilon}H^b,
 \qquad \delta_g(v)=3/4+2v,\quad Q\le U^\kappa.              \tag{24}
\]
Apply the functional equation to the primitive function before
multiplying the literal deleted Euler factor; the global input also
covers the conjugate primitive function. All-height bounds control the
full Mellin integrals. No selected-bin zero-free rectangle is used.
The auxiliary disk parameter in the proof of Lemma 4.9 is chosen below
\(\min(1/1000,v/8)\); it affects constants, not a fixed conductor
power. The literal cost \(2v\) in (24) is retained, not hidden inside
an arbitrarily small \(\varepsilon\).

Set
\[
 \kappa_1=m+2dr/3-1/750,
 \quad 17/30\le\kappa_1\le1157/1875,
 \quad \kappa_1-m<1/4.                                     \tag{25}
\]
The branches used in (19) still hold. Combining (24) with (3) gives
\[
 E_{\rm np,\,Q\le U^{\kappa_1}}^\Omega
 \ll U^{1+dr-1/500+4v(\kappa_1-m)+\varepsilon}H^{b_1}.        \tag{26}
\]
Since \(4v(\kappa_1-m)<v\le1/3500\), its saving is at least
\[
 3/1750=1/700+1/3500                                        \tag{27}
\]
before other fixed losses. Their height/profile conversion must fit
strictly inside the remaining \(1/3500\) reserve. Also
\(\kappa_1-\kappa_0=dr/6-1/3000\ge1/24\).
This is a conditional deduction from the already conditional global
family package, not a theorem deduced from zeta-only quasi-RH.

## 6. The exact centered coefficient and owned prime extraction

Put \(X=DN^2\prod_{j\in J}P_j\). With the original inverse profile
\(A_0\), bounded row-independent prime coefficients \(a_j\), and
original slot profiles \(W_j\), define
\[
\begin{split}
 A_c(k)=\sum_{n v_1v_2\prod_{j\in J}p_j=k}
 &\mu_F(n)A_0(Nn/D)\prod_{j\in J}a_j(p_j)W_j(Np_j/P_j)\\
 &\cdot\left[B(Nv_1/N)B(Nv_2/N)
             -B(Nv_1/Y_1)B(Nv_2/Y_2)\right].
\end{split}                                                  \tag{28}
\]
All ideals are good, and the \(p_j\) run over their original prime
supports. The inverse is the original squarefree Möbius polynomial; no
new capped inverse is inserted. Equal products give the exact identity
\[
 \Delta_u=X^{-1/2}\sum_k A_c(k)\psi_u(k).                    \tag{29}
\]
Both rectangles have the same normalizer. The coefficient is row
independent, supported on \(Nk\asymp X\), and bounded by
\(X^\varepsilon\) times fixed profile and slot amplitudes, using an
ideal divisor bound. Twists and correlated derivatives belong to the
full coefficient in (28).

For one extracted prime \(p\), partition its total exponent by ownership:
inverse exponent \(e_\mu\in\{0,1\}\), plain exponents
\(f_1,f_2\ge0\), and the individual live slot exponents. The residual
factors are all \(p\)-free, the Möbius sign is \((-1)^{e_\mu}\),
and the shifted inverse scale is \(D/(Np)^{e_\mu}\). Shift the
ordered plain scales in **both** rectangles:
\[
 (N/(Np)^{f_1},N/(Np)^{f_2}),\qquad
 (Y_1/(Np)^{f_1},Y_2/(Np)^{f_2}).                            \tag{30}
\]
Equal products are preserved branch by branch. If the total exponent
is \(k_p\), keep the physical scalar \(\psi_u(p)^{k_p}\),
including its zero value. For the **formal** child center \(X/(Np)^{k_p}\), the scalar is
\((Np)^{-k_p/2}\). A child using the remaining **nominal slot scales**
instead has
\[
 X_{\rm child}=\frac{X}{(Np)^{e_\mu+f_1+f_2}\prod_{j\ {\rm frozen}}P_j},
 \qquad
 \text{scalar}=(Np)^{-(e_\mu+f_1+f_2)/2}
                       \prod_{j\ {\rm frozen}}P_j^{-1/2}.
\]
These are alternative normalizations of the same identity; their
conversion is the corresponding bounded annular factor. Do not charge
both scalars. Frozen slots retain their actual nominal \(P_j\) scale. Never divide by
\(\psi_u(p)\), omit ownership branches, or declare the shifted
coefficient a new marked-moment input without proving its scope.
These are algebraic extensions of [Note 21](21_SIGNED_JOINT_TRANSFORM_20261009.md),
not a new analytic child estimate.

## 7. Smooth zero contribution and the genuinely open step

Under the exact native smooth row-Poisson scope of
[Note 24](24_ADAPTIVE_COFACTOR_AND_DYADIC_KERNEL_20261009.md),
the first zero frequency of the square in (29) requires equal
sixth-power-free column cores. Writing \(k=va^6\), \(k'=vb^6\)
gives
\[
 \#\{(k,k'):Nk,Nk'\asymp X,\ \text{equal sixth-free core}\}
 \ll\sum_{Nv\ll X}(X/Nv)^{1/3}\ll X.                       \tag{31}
\]
Coefficient divisor bounds, the square normalizer \(X^{-1}\), and the
row mass \(O(U)\) give the conditional bound
\[
 |Z_c^\Omega|\ll U^{1+\varepsilon}H^b.                     \tag{32}
\]
It has reserve \(dr-1/700\ge877/3500\) on the coarse box, before
fixed losses. This does not bound the nonzero frequencies. The exact
second transform from Note 21 retains its complete coprimality projector;
the unchanged nominal width still supplies no automatic descent.

Write the full radial Poisson expansion as
\[
 E_c^\Omega=Z_c^\Omega+\operatorname{Re}\mathcal K_{c,\ne0}^\Omega.
                                                               \tag{33}
\]
The next sufficient theorem is the **complete signed aggregate** bound
\[
 \boxed{\operatorname{Re}\mathcal K_{c,\ne0}^\Omega
      \ll U^{1+dr-1/700+\varepsilon}H^b.}                    \tag{34}
\]
It must retain (28), physical masks, moving native characters, finite
ray phases, all cross terms and the actual derivative/height allowances.
Equations (11), (20) and, conditionally, (26) control the added bounded
and low conductor sectors. The remaining positive norm has
\(Q>U^{\kappa_0}\), or \(Q>U^{\kappa_1}\) when the global input
is used. A conductor-stratified proof of (34) must justify its handling
of that nonradial predicate. One cannot simply insert the sharp conductor
or selected-bin indicator into the already established radial Poisson
formula. Apply Poisson on its permitted smooth domain, then account for
the controlled sectors or prove the necessary projector interface.

Available legal scalar estimates quantify the gap, **under the same
global premise** \(\beta_*\le7/8\). Retain source Lemma 18.1's
nonexceptional-row condition, its prescribed slot mesh and its requirement
that each positive-slot coefficient be a fixed finite linear combination
of the specified finite ray characters. Growing conductors eventually
exclude its fixed exceptional family; the original slot certificate must
still supply the coefficient and mesh scope. For that permitted original
slot class, the two ordinary marked plain rectangles have norm
\(O(U^{1+\varepsilon}H^b)\), under the additional legal capacity
\(2m+(9/2)z_J<1\). Capacity alone is insufficient. With a globally
valid inverse contour to the right of \(7/8\), rather than the selected
\(d\)-dependent estimate, one obtains only
\[
 E_{\rm remaining}^\Omega\ll
 U^{1+\delta_g(v)r+\varepsilon}H^b.                         \tag{35}
\]
The deficit from the target is at least
\[
 (3/4-d)r+1/700\ge1627/7000>0.2324.                         \tag{36}
\]
Thus the new estimate requires correlation beyond these scalar envelopes.
[Note 18](18_NATIVE_ANNULAR_DIAGONAL_TEST_20261009.md), section 4,
already defeats the separately positive coefficient diagonal after
standard equal-product centering. That obstruction persists; it neither
disproves (2) nor a signed aggregate theorem. No new lower-bound
obstruction to the complete centered norm is asserted here.

## 8. A conductor-preserving selected projector alternative

Separate the explicit sixth-free condition from the remaining bin
predicates. Let \(\mathscr B(u)\) be a **declared extension** of those
primitive-zero, amplitude and profile predicates to all physical rows,
using the original formulas. On original sixth-free rows it agrees with
the selected bin. Put \(\beta=2m-1/1000\). Möbius inversion and
(12) give the exact finite identity
\[
\begin{split}
 &\sum_{u\ {\rm sixth\text{-}free}}
  \Omega(Nu/U)1_{\mathscr B(u)}1_{Q_{\psi_u}>U^\beta}|\Delta_u|^2\\
 &=\sum_q\mu_F(q)\sum_v
  \Omega((Nq)^6Nv/U)1_{\mathscr B(q^6v)}1_{Q_{\psi_v}>U^\beta}
  \left|X^{-1/2}\sum_k A_c(k)\psi_v(k)1_{(k,q)=1}\right|^2.
\end{split}                                                  \tag{37}
\]
The primitive conductor is unchanged by \(q^6\). Physical amplitude
and slot predicates can change because \(q\) adds zeros: keep
\(\mathscr B(q^6v)\), not \(\mathscr B(v)\). If the literal
selected set already includes sixth-freeness, putting its indicator on
the right kills every \(q>1\) term; that identity is true but
tautological. A useful selected projector requires the declared predicate
extension. Choosing \(\mathscr B\equiv1\) gives a stronger sufficient
smooth high-conductor problem, without transferring selected-bin bounds.

Since \(Q_{\psi_v}\ll Nv\) and \((Nq)^6Nv\ll U\), the high
gate gives the exact finite range
\[
 Nq\ll U^{(1-\beta)/6}
       =U^{(1-2m+1/1000)/6}\le U^{67/2000}.                  \tag{38}
\]
A complete cutoff at this range has zero tail. Absolute \(q\)
summation with the gate retained cannot restore primitive principal rows;
Note 25's unrestricted small-cutoff tail objection does not apply
unchanged to (37). Nevertheless the nonradial bin and conductor
predicates remain, and the \(q=1\) term already contains the central
selected correlation. The shorter range alone proves no operator gain
and no clean radial row-Poisson formula.

## 9. Verification and the next milestone

The [checker](../../numerics/check_centered_continuation.py) prints the
[retained record](../../numerics/centered_continuation_record_20261009.json)
without writing files. Two fresh runs reproduced all 10,533 assertions
and the record byte for byte. They test the complete centered coefficient,
inverse/plain/slot prime ownership, every physical zero, selected cross
terms, the extended-predicate projector with active nonunit masks, and
exact rational cutoff/reserve/height ledgers. They are finite arithmetic
models, not proofs of native reciprocity, conductor transfer, Poisson,
source moments, Mellin estimates, uniform smooth decay, or (34).

The substantive completed steps are the original-product centering
comparison of Note 26, principal/bounded-ray cancellation (7)–(11),
the growing auxiliary sector (20), the conditional enlargement (26),
and the exact algebraic interfaces (28)–(38). The next research milestone
is a signed correlation estimate for the remaining growing conductor
range, with a quantitative improvement over (35), and a shared source
frequency/height ledger satisfying the separate reserves. The fixed
height degrees in the imported moments are still symbolic; no numerical
detector schedule or full operational application is certified.

The [continuation review](../../reviews/MIXED_CENTERED_AUXILIARY_REVIEW_20261009.md)
records source checks, integration and limitations. The full mixed
fourth moment, full detector/bin coverage, a new family boundary and
descent from zeta-only quasi-RH to RH remain unproved.

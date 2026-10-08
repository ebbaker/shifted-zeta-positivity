# The first mixed-moment calculation: one remaining signed sum

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred.

## Result and scope

The first remaining task was to expand the actual mixed coefficient before
taking absolute values and locate the arithmetic term needing a saving.
This calculation now removes three substantial parts using the existing
assumed source inputs and elementary ideal counting. The new estimate is
needed only for distinct plain ideals, on rows of large primitive conductor,
and with large conductor for the ratio of the two composite columns.

No estimate for that last signed sum has been proved. The current conditional
candidate stays `7/8 - 1/24000`; the proposed `7/8 - 1/20000` still requires
the additional mixed input identified in the
[localized target](LOCALIZED_JOINT_WITNESS_TARGET_20261008.md).

The source is the [September 30 companion paper](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf),
especially Lemmas 8.1–8.2 and 17.1–17.5 and Section 19. The consulted PDF
has SHA-256
`8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.
Its deep analytic theorems, including the imported seven-eighths boundary,
remain assumptions. This is a reduction within that framework.

## 1. Retain the actual coefficient and all masks

Work in the previously localized box

\[
\frac9{25}\le\delta\le\frac{21}{50},\quad
\frac{49}{100}\le x=q/\delta\le\frac12,\quad
H_G(t_0)<\frac1{5000},
\]
\[
\frac7{10}\le r\le\frac{37}{50},\quad
\frac9{25}\le m\le\frac12.
\]

Let \(\mathcal C\) be a fixed buffered zero/profile bin and presentation,
before asking which rows have a large witness at a particular pair r,m.
Select whole physical prime slots of total length z just below
\((1-r)/2\), with the already prescribed strict capacity margin. Write
\(D=U^r\), \(N=U^m\), \(P_i=U^{w_i}\),
\(X=DN\prod_iP_i\), and

\[
\psi_u(n)=\nu(n)\chi_n(u)^{\varepsilon_\chi},
\qquad \varepsilon_\chi\in\{1,-1\}.
\]

Fix the source's separating parameters before expanding. For a tuple
\(\mathbf t=(d,k,(p_i))\), put \(n(\mathbf t)=dk\prod_i p_i\) and

\[
a(\mathbf t)=\mu_K(d)\nu(n(\mathbf t))
A(\mathrm Nd/D)B(\mathrm Nk/N)
\prod_i a_i(p_i)W_i(\mathrm Np_i/P_i).
\tag{1}
\]

The profiles contain their actual norm powers and heights; A retains its
inverse cutoff, and the physical prime lists are disjoint and unchanged.
Then

\[
M_r(u)S_m(u)Q_I(u)
=X^{-1/2}\sum_{\mathbf t}a(\mathbf t)
\chi_{n(\mathbf t)}(u)^{\varepsilon_\chi}.
\tag{2}
\]

For columns n,n', define

\[
e_p=(v_p(n)-v_p(n'))\bmod6\in\{0,\ldots,5\},\quad
c(n,n')=\prod_{e_p\ne0}p^{e_p},\quad f=\operatorname{rad}(c),
\]
\[
E(n,n')=\prod_{p\mid nn',\ e_p=0}p.
\]

Exactly, including nonunits,

\[
\chi_n(u)^{\varepsilon_\chi}
\overline{\chi_{n'}(u)^{\varepsilon_\chi}}
=\chi_c(u)^{\varepsilon_\chi}\mathbf1_{(u,E)=1}.
\tag{3}
\]

The moving ratio-character conductor is f, whereas E keeps the remaining
zero support. For example, a sixth-power column against the unit column
still imposes its prime coprimality mask. This distinction is essential.
The [kernel derivation](MIXED_KERNEL_CONDUCTOR_REDUCTION_20261008.md)
proves (1)–(3) and the coefficient estimates used below.

## 2. Remove rows of smaller primitive conductor first

Let \(Q_{\psi_u}=U^{\theta(u)}\) be the conductor of the primitive
character inducing the row presentation. This is a different conductor
from f, which belongs to a pair of columns. Keeping \(Q_{\psi_u}\) in
the functional equation instead of replacing it by U gives

\[
|S_m(u)|^2\ll
U^{\delta\min\{m,\theta(u)-m\}+\epsilon}(1+T_1)^A.
\tag{4}
\]

The [row-conductor derivation](SATURATED_MIXED_ARITHMETIC_20261008.md)
checks the deleted Euler factors, profiles, and height allowance. Applying
the existing marked inverse moment after (4), by positivity, shows that
the rows with \(\theta\le2m-1/1000\) contribute at most

\[
U^{1+\delta m-\delta/1000+\epsilon}(1+T_1)^A.
\tag{5}
\]

Set \(K=1+\delta m-1/5000\). Since
\(\delta/1000\ge9/25000=1/5000+1/6250\), (5) is
\(O(U^{K-1/6250+\epsilon}(1+T_1)^A)\).
It remains to expand only over

\[
\mathcal C_+=\{u\in\mathcal C:Q_{\psi_u}>U^{2m-1/1000}\}.
\tag{6}
\]

This removes a part of the moment, not merely rows already known to carry
large witnesses. Actual simultaneous detector witnesses satisfy the
stronger \(\theta\ge2m-o_{\rm loss}(1)\). Large-conductor rows remain;
no sparsity conclusion is inferred from this observation alone.

## 3. Remove the complete plain-variable diagonal

Expand the two plain factors first. Terms with the same ideal k on both
sides form the nonnegative expression

\[
D_{\rm plain}=\frac1N\sum_k|B(\mathrm Nk/N)|^2
\sum_{u\in\mathcal C_+}|M_r(u)Q_I(u)|^2
\mathbf1_{(u,k)=1}.
\tag{7}
\]

All fixed zeros remain in the original supports. Dropping the displayed
mask after forming this positive sum, applying the marked inverse moment,
and using normalized ideal counting gives

\[
D_{\rm plain}\ll U^{1+\epsilon}(1+T_1)^A.
\tag{8}
\]

Thus this entire block is below the target exponent K by at least
\(647/5000\). It includes inverse and prime off-diagonal terms; it is
larger than just the identical-composite-column diagonal. All subsequent
column-pair splits retain tuple labels and impose \(k\ne k'\), so these
terms are not counted twice.

## 4. Remove small ratio conductors without assuming cancellation

An elementary counting lemma gives

\[
\#\{n,n':\mathrm Nn,\mathrm Nn'\le C X,
\ \mathrm Nf(n,n')\le V\}\ll_\epsilon X V^{1/2+\epsilon}.
\tag{9}
\]

Indeed, extract the gcd g and write
\(n=g a_0 a^6\), \(n'=g b_0 b^6\), with coprime sixth-power-free
\(a_0,b_0\). Their radical is f. For each allocation of the primes of
f to a side and exponent, ideal counting bounds g by

\[
\frac{CX}{\max(\mathrm Na_0(\mathrm Na)^6,
\mathrm Nb_0(\mathrm Nb)^6)}
\le\frac{CX}{\sqrt{\mathrm N(a_0b_0)}(\mathrm N(ab))^3}.
\]

The a,b sums converge. Summing at most \(10^{\omega(f)}\) allocations
and using \(\mathrm N(a_0b_0)\ge\mathrm Nf\) proves (9).
The sum of absolute tuple coefficients at each column is divisor-bounded,
so the entire small-conductor block costs at most

\[
\#\mathcal C_+\,V^{1/2+\epsilon}X^\epsilon.
\tag{10}
\]

This uses only the trivial restricted character-kernel bound
\(|\mathcal K_{\mathcal C_+}|\le\#\mathcal C_+\). It therefore
remains valid for the actual zero/profile-selected rows and all masks.

The existing scalar count applies to the full bin before r,m witness
selection. On the hard box,

\[
\#\mathcal C_+\le\#\mathcal C\ll
U^{R^*+\epsilon}(1+T_1)^A,\qquad
R^*\le\frac98-\frac{23\delta}{20},
\]

using \(t_0-1<3/20\). Take \(V=U^{4/5}\). The difference between
K and the exponent in (10) is at least

\[
\delta\left(m+\frac{23}{20}\right)
-\frac{21}{40}-\frac1{5000}\ge\frac{23}{1250}.
\tag{11}
\]

This removes all remaining sixth-power coincidences and all pair conductors
through \(U^{4/5}\), with a fixed margin. No cancellation of those
character sums is needed.

## 5. Exact remaining task

For \(c=c(n,n')\), \(E=E(n,n')\), let

\[
\mathcal K_{\mathcal C_+}(c;E)
=\sum_{u\in\mathcal C_+}\chi_c(u)^{\varepsilon_\chi}
\mathbf1_{(u,E)=1}.
\]

The only unresolved term is now

\[
\boxed{
\mathcal T_{\rm large}
=\frac1X\sum_{\substack{\mathbf t,\mathbf t'\\
k\ne k'\\ \mathrm Nf(n(\mathbf t),n(\mathbf t'))>U^{4/5}}}
a(\mathbf t)\overline{a(\mathbf t')}
\mathcal K_{\mathcal C_+}(c;E).}
\tag{12}
\]

Combining the three proved reductions gives

\[
\sum_{u\in\mathcal C}|M_rS_mQ_I|^2
=\operatorname{Re}\mathcal T_{\rm large}
+O\!\left(U^{K-1/6250+\epsilon}(1+T_1)^A\right).
\tag{13}
\]

The cutoff regions are symmetric under swapping the tuples, so their
complete sums are real. Writing the real part also makes explicit the
weakest sufficient request: an upper bound for (12) by
\(U^{K+\epsilon}(1+T_1)^A\). An absolute bound on the summed expression
is stronger; a sum of absolute bounds on each pair is stronger still.
Neither is silently substituted for the needed signed estimate.

All preliminary losses and fixed height powers must remain within the
existing parameter-choice order. Equation (13) is first established at
fixed separating parameters; source-style Sobolev treatment of rowwise
choices requires the same estimate uniformly for the corresponding
derivative profiles. It is not valid to put independently chosen row
heights into one coefficient array in (12).

## 6. What the source's transformed argument reveals

The [marked transfer audit](../reviews/MARKED_MIXED_TRANSFER_AUDIT_20261008.md)
retains the complete mixed coefficient through the first source transform.
Even on its squarefree coprime core, appending the plain factor raises
the first dual-row length by 2m. The formal canonical margins at
\(z=(1-r)/2-\nu\) become

\[
2\nu-m,\qquad 2r-1-2m+8\nu.
\]

At zero decrement these lie in \([-1/2,-9/25]\) and
\([-3/5,-6/25]\). They cannot be repaired by a small capacity adjustment.
The transformed coefficient also contains an actual annular Möbius
divisor sum \(h(tfn)\), depending on the canonical averaged label f.
Lemma 17.2 expressly excludes this residual coefficient class.

For a complete smooth row family, masked Poisson gives an exact signed
nonzero-frequency formula. It is a separate sufficient approach to bound
that enlarged positive norm. The arithmetic selector in (6), however,
cannot be dropped term by term from (12) or inserted into the source's
Schwartz Poisson formula without a new weighted argument. This is the
remaining analytic obstacle in concrete form.

The source's cancellation between two plain rectangles also cannot be
transferred merely by matching products of lengths: an inverse factor has
a different arithmetic coefficient and retains its inverse Mellin modes.
Likewise, saturation here is far below equality in the triangle inequality,
so it supplies no elementary phase-alignment claim.

## Verification and saved records

The [exact check](../numerics/check_mixed_kernel.py) verifies the local
valuation/mask algebra on a finite exhaustive set and all displayed rational
margins. Its [small record](../numerics/mixed_kernel_check.json) records
that limited scope; the finite checks do not prove an arithmetic cancellation
theorem. The ideal-pair estimate is proved in the kernel note, and the
[separate scoped review](../reviews/MIXED_REDUCTION_REVIEW_20261008.md)
checks the source applicability, noncircular row count, masks, and the
combined reduction. The new mixed-moment saving on (12) remains open.

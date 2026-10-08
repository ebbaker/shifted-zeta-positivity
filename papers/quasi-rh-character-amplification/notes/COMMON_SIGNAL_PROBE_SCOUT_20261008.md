# Two common-signal probes: exact kernel and a bounded cancellation test

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort are
not exposed and are not inferred. This is a bounded algebraic scout, not an
independent verification of the external paper or a new zero-free theorem.

## Finding

Two explicit admissible probes can have exactly the same full target signal,
with the same excluded set, Euler correction, Gaussian, and physical geometry,
after their actual finite-prime normalizers are used. Their normalized
principal *remainders* need not be equal and must still be retained.

The mixed row kernel is explicit below. A two-profile combination can cancel
one specified coherent Mellin mode while preserving the principal signal.
It cannot cancel a continuum of possible modes with a power saving using
bounded coefficients. The source's prime-amplitude saturation conditions do
not identify the complex mode or control the mixed kernel. Thus this scout
supplies no improvement of the exceptional-row exponent. It makes a specific
missing arithmetic estimate visible and rules out an automatic gain from
common-signal normalization alone.

## 1. Sources and scope

The external source is the September 30 companion paper, especially (12.5),
(16.2)--(16.10), (20.1), and Lemma 10.5:
https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf

The source PDF SHA-256 is
`8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.

Repository inputs are the [geometry note](GEOMETRY_OPTIMIZATION_20261008.md)
and the Sonin selective-loss notes on
[Schur completion](../../investigations/sonin-critical-boundary/notes/selective-loss-program/01_schur_completion_20261003.md) and
[the complete signed response](../../investigations/sonin-critical-boundary/notes/selective-loss-program/04_complete_response_and_signed_pairs_20261003.md). Those notes motivate
preserving the complete signed mixed term and prescribing coefficients from
controlled data. They do not estimate the present character kernel.

All appeals to the source's reflection, detector, contour, and moment
machinery retain the conditional status of the preceding investigation.
The kernel identities, normalization comparison, and model-filter obstruction
below are elementary once the displayed source formulas are granted.

## 2. An explicit pair with identical full signal

Use the current geometry

\[
\ell=1001/6000,\quad b=1/8,\quad
l_x=4249/12000,\quad l_y=5749/12000,\quad h=3251/4000.
\]

Fix an integer K large enough to satisfy the source's preselected slot mesh,
and set every slot length to \(\ell_i=\ell/K\). Thus every prime scale is
\(P=Z^{\ell/K}\). Equal lengths are allowed; disjoint fixed annuli provide
disjoint underlying prime windows.

For definiteness, let

\[
W(y)=\begin{cases}
\exp\{-1/[(y-1)(3/2-y)]\},&1<y<3/2,\\
0,&\text{otherwise}.
\end{cases}
\]

In probe j=0 use the first-slot weight \(W_{1,0}(y)=W(y)\); in probe
j=1 use \(W_{1,1}(y)=W(y/2)\). Their supports are respectively
\((1,3/2)\) and \((2,3)\). For i>=2 choose fixed nonnegative smooth
nonzero weights supported inside \((4i,4i+1/2)\). The other slots are
identical in both probes. Within either probe all underlying prime supports
are disjoint before the ray restriction and excluded set are imposed. All
profiles and K are independent of Z and of the target.

Use the same target, final excluded set S, ray group T, calibration, original
zero masks, base tests W_0,W_1, and Gaussian for both probes. Here the base
test W_1 from Section 6 is separate from the slot notation W_{i,j} above.
Take any required cutoff sufficiently large for both finite profile systems.
Apply exactly the physical finite operation (12.5) to obtain I_j(Z).

Define the actual finite positive prime sums

\[
S_{i,j}(Z)=\sum_{\substack{p\notin S\\p\in1_T}}
 W_{i,j}(q_p/P)q_p^{-5/6},\qquad
A_j(Z)=(-1)^K Z^{-\ell/6}\prod_i S_{i,j}(Z).
\]

No asymptotic substitutes for A_j. Fixed-ray prime asymptotics ensure that
these sums are positive for sufficiently large Z and that A_j^{-1} has
subpower size. Define

\[
J_j(Z)=I_j(Z)/(c_S A_j(Z)).
\]

The scalar c_S uses the unchanged base tests and S, hence is the same.
The unmodified residue correction H_eta(s) also uses that same S and is
unchanged. Since M+ell=1 and b=1/8, both probes have the complete signal

\[
f_\eta(Z)=\frac1{2\pi i}\int_{(2)}
 Z^{s-11/16}e^{(s-5/6)^2}
 \frac{H_\eta(s)}{L_F^S(s,\eta)}\,ds.
\tag{1}
\]

This identifies the complete Mellin integrand, not only its affine exponent.
If P_j denotes each full principal row, the source gives
\(P_j/(c_S A_j)=f_\eta+e_j\), with the retained principal contour and
local-factor errors e_j. In particular the exact normalized principal rows
are not asserted equal. A bounded combination

\[
J_c=c_0J_0+c_1J_1,\qquad c_0+c_1=1
\tag{2}
\]

retains (1) and the error c_0 e_0+c_1 e_1. The same low exponent follows
by the triangle inequality because the coefficients and profile count are
bounded independently of Z. No new low-side cancellation is claimed.

## 3. Exact normalized local response

Fix a retained dynamic contour point and a physical sixth-power-free row u.
Only in the dynamic region, where the source proves selected H_p nonzero,
write B_p=G_p/H_p as in (16.2). Everywhere else the full finite holomorphic
correction (16.3), with selected G_p and the unselected H product, is used.
There is no continuation through an unsupported individual quotient.

For each slot form the exact probability measure on its allowed primes

\[
\mu_{i,j,Z}(p)=
\frac{W_{i,j}(q_p/P)q_p^{-5/6}}{S_{i,j}(Z)}.
\]

Put

\[
T_{i,j}(u;s,w,z)
=\sum_p\mu_{i,j,Z}(p)q_p^{z-1/6}[-B_p(u;s,w,z)].
\tag{3}
\]

Then the dynamic factorization gives the exact identity

\[
\frac{H_{\eta,u,Z}^{(j)}(s,w,z)}{A_j(Z)}
=Z^{\ell/6} H_{\eta,u}(s,w,z)\prod_i T_{i,j}(u;s,w,z).
\tag{4}
\]

Every local factor and ramified label in the source is retained in (3).
At the principal residue u=1,w=1,z=1/6, the source's
\(-B_p=1+O(q_p^{-\sigma_p})\), with the already-audited
\(\sigma_p>0\), gives T_{i,j}=1+small error. Both probability measures
have mass one. This is the exact reason that the common signal survives.

Write T_i for the common slots i>=2. The normalized correction contrast is

\[
Z^{-\ell/6}
\left(\frac{H^{(1)}_{\eta,u,Z}}{A_1}
      -\frac{H^{(0)}_{\eta,u,Z}}{A_0}\right)
=H_{\eta,u}\prod_{i\ge2}T_i
 \sum_p [\mu_{1,1,Z}(p)-\mu_{1,0,Z}(p)]
 q_p^{z-1/6}[-B_p].
\tag{5}
\]

The signed measure in (5) has zero mass, but the actual multiplier is not
constant on it. Signal normalization therefore gives no general cancellation
of the exceptional character response. For example, the source main term
off u is \(-B_p\approx\omega_u(p)\), where
\(\omega_u(p)=\chi_p(u)^{-1}\) in (16.8), and is zero-extended at p|u
in that main term. The complete B_p in (5) also retains its error factors.

For an overlapping-profile variant, W_{1,1}=(1+epsilon r)W_{1,0}, with
bounded real r and positive 1+epsilon r, equation (5)'s last factor becomes
exactly

\[
\frac{\epsilon}{1+\epsilon\mathbb E_{\mu_0}r}
\operatorname{Cov}_{\mu_0}
\bigl(r(q_p/P),q_p^{z-1/6}[-B_p]\bigr).
\tag{6}
\]

Thus the remaining quantity is a specified weighted character covariance,
not a generic unknown Gram matrix.

## 4. The complete finite mixed row kernel

Fix a pointwise bad set B, a retained tuple of external parameters, and
nonnegative weights lambda_u. Set

\[
C_u=L_F^S(w,\chi_\bullet(u))H_{\eta,u}(s,w,z)
\prod_{i\ge2}T_i(u;s,w,z),\qquad
R_j(u)=C_uT_{1,j}(u;s,w,z).
\]

The rows and zero masks are the same in both probes. The weighted mixed Gram
is exactly

\[
G_{jk}=\sum_{u\in B}\lambda_u R_j(u)\overline{R_k(u)}
=\sum_{p,q}\mu_{1,j,Z}(p)\mu_{1,k,Z}(q)
 q_p^{z-1/6}q_q^{\bar z-1/6}\mathcal K_B(p,q),
\tag{7}
\]

where the completely specified kernel is

\[
\mathcal K_B(p,q)=\sum_{u\in B}\lambda_u|C_u|^2
 [-B_p(u;s,w,z)]\overline{[-B_q(u;s,w,z)]}.
\tag{8}
\]

There is no deletion of diagonal, ramified, endpoint, cap, or cross-profile
terms. Substituting the exact holomorphic selected-factor formulas gives a
finite arithmetic expression on the region where this factorization is
permitted. The full correction (16.3), rather than (7), still governs all
contour moves and tails.

For prescribed c_0,c_1 the energy is
\(\sum_{j,k}c_j\bar c_k G_{jk}\). If coefficients were optimized through
the unknown G, the usual Schur complement would merely rename the missing
estimate. Here one can instead prescribe the explicit coefficients below
and ask for their one specific quadratic form. A common coherent component
R_0=R_1 has Gram g times the all-ones matrix and survives every signal-
preserving combination. In contrast, a component with known unequal probe
responses can in principle be removed. Amplitude saturation alone decides
neither situation: it records sizes, not these phases and correlations.

## 5. An explicit coherent-mode diagnostic

This section is a diagnostic of a proposed cancellation mechanism, not a
claim that an actual moving-conductor character row equals a power density.
No uniform zero-mode expansion on the exceptional class has been proved.

Suppose a leading prime-density contribution has power q^{rho-1}. In (3)
its transfer exponent is

\[
v=\rho+z-7/6.
\]

After removing the common P^v, the fixed-ray prime asymptotic gives the
normalized limiting profile transform

\[
m_j(v)=
\frac{\int_0^\infty W_{1,j}(y)y^{-5/6+v}\,dy}
     {\int_0^\infty W_{1,j}(y)y^{-5/6}\,dy}.
\]

For the explicit dilation pair a substitution gives exactly

\[
m_1(v)=2^v m_0(v),\qquad m_0(0)=m_1(0)=1.
\tag{9}
\]

The equality is between the limiting transforms. The actual finite-prime
normalizers and measures in (3) remain exact. The fixed-ray asymptotic
alone supplies o(1), not a new power bound on the difference from (9).

At the dangerous real bin, delta approximately 0.386688531 and
Re(z)=17/50, the corresponding real exponent would be

\[
v\approx-0.1333224012.
\]

A nearby exact choice is v_*=-2/15, corresponding to a=52/75 and
delta=29/75. Choose the explicit real constants

\[
c_1=\frac1{1-2^{-2/15}},\qquad
c_0=-\frac{2^{-2/15}}{1-2^{-2/15}}.
\tag{10}
\]

They satisfy c_0+c_1=1, and
\(11<c_1<12\), \(-11<c_0<-10\). These bounds follow from
\(4\cdot10^{15}<11^{15}\) and \(4\cdot11^{15}>12^{15}\).
The resulting model filter is

\[
F(v)=c_0+c_1 2^v,\qquad F(0)=1,\quad F(v_*)=0.
\tag{11}
\]

Thus scalar signal normalization does not impose collinearity with every
nonprincipal mode: one known mode can be killed by a bounded contrast.
At v_*+h the exact residual is

\[
F(v_*+h)=c_1 2^{v_*}(2^h-1),
\qquad |F(v_*+h)|\le11(\log2)|h|2^{|h|}.
\tag{12}
\]

Cancellation at one point gives only a constant gain on a fixed-width
neighborhood. A power gain through this filter alone needs a mode window
shrinking at a comparable power of Z. The source's Mellin heights range continuously, and fixed physical
coefficients cannot be retuned separately for each height or unknown zero.

There is a precise obstruction to upgrading this test to a uniform free
power saving. For fixed coefficients, a filter which vanished on a nonempty
real interval would vanish identically by analyticity, contradicting F(0)=1.
The same argument applies to any finite family of fixed compact profiles,
whose normalized Mellin transforms are entire and all equal one at zero.

Even allowing bounded coefficients c_j(Z) does not evade the obstruction
for a uniform relative power bound over a fixed interval of model exponents.
Take a convergent coefficient subsequence. The fixed-ray prime asymptotic at
each fixed exponent forces the limiting analytic profile combination to
vanish on that interval, but its value at zero remains one. This is a
model-filter obstruction; it does not prove that actual exceptional rows
fill that continuum, and it does not exclude an arithmetic concentration or
mixed-correlation theorem.

## 6. A precise remaining estimate and the stopping point

At one retained dynamic tuple let the natural source-size envelope for R_j be

\[
B_Z=U^{\delta/2+\epsilon}
 Z^{\ell(\Re z-2/3+q)+\epsilon},
\]

up to the source's fixed height factor. Here R_j excludes the common
Z^{ell/6} in (4), and q is the physical weighted amplitude mean. The two
profile systems should first be partitioned jointly; a union of their finite
bin labels does not by itself supply any saving.

One sufficient new bound for a prescribed bounded signal-preserving
combination is, uniformly on the dangerous class and all its retained
external parameters,

\[
\sum_{u\in B}|c_0R_0(u)+c_1R_1(u)|^2
\ll U^{R^*(\delta,q)-2\eta+\epsilon} B_Z^2,
\qquad \eta>0.
\tag{13}
\]

Together with the existing count |B|<=U^{R^*+epsilon}, Cauchy--Schwarz
would give an L1 row sum of size U^{R^*-eta+epsilon} B_Z. The common
Z^{ell/6}, other geometric factors, denominator bound, and every contour
remainder would then be restored exactly as in the source. This is a
sufficient target, not a result. Equation (7) identifies the actual signed
prime-pair expression whose bound is needed; neither separate diagonal
energies nor optimized coefficients chosen from the unknown matrix prove it.

The source's existing estimates allow the two probes' bad sets to coincide
and do not bound their mixed character phases. The explicit test therefore
stops here. The recommended order remains: pursue the joint inverse/plain
witness estimate first. Resume the two-probe route if that analysis supplies
a known common exceptional response, a narrow mode concentration theorem,
or a power-saving bound for (8) on the actual simultaneously saturated class.
No new parameter or zero-free boundary should be adopted from this scout.

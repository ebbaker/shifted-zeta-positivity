# A cubic target for the actual plain probe

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Same-model derivations and finite checks are internal validation, not
independent specialist review or formal proof verification.

The cubic frame in [note 2](2_SELECTED_INVERSE_DISTRIBUTION_20261008.md)
has a strictly weaker sufficient version that retains the actual plain
coefficient vector. Its open chains contain two row-ratio kernels and the
actual plain sums at their endpoints. The existing buffered plain input
controls all repeated-character chains, with a fixed exponent margin.
The remaining pairwise-inequivalent open-chain estimate is unproved.

This is a bounded reassessment after the short-family
[complete-cofactor obstruction](../../short_families/notes/24_SHORT_FAMILY_FINITE_COFACTOR_PAIRING_20261008.md).
It supplies a more specific next mixed-family task, not an analytic gain
for either full moment or a new zero-free boundary.

## 1. The selected frame and its actual probe

Keep every convention, fixed separating parameter, derivative profile,
physical prime slot, inverse cutoff, and zero mask from notes 1--2. Set
\[
 w_u=\mathbf1_{u\in\mathcal C_+}|M_r(u)Q_I(u)|^2,
 \quad A=\sum_u w_u,\quad W=\max_u w_u,\quad N=U^m.
\]
The columns are the complete original fixed plain annulus, including any
zero columns from fixed exclusions. Let \(L_N\ll N\) be their number,
\(\mathbf1\) their all-ones vector, and
\[
 T_{u,k}=N^{-1/2}\psi_u(k)B(Nk/N),\qquad T\mathbf1=S,
\]
where \(S_u=S_m(u)\) is the actual plain sum. Put
\[
 \mathcal A=\operatorname{diag}(\sqrt w)T,\qquad
 G=\mathcal A\mathcal A^*,\qquad C=\mathcal A^*\mathcal A,
 \qquad f=\mathcal A\mathbf1.
 \tag{1}
\]
Both matrices are positive semidefinite. Their nonzero eigenvalues agree,
so \(\operatorname{Tr}(C^3)=\operatorname{Tr}(G^3)\). The original
selected mixed energy is exactly
\[
 E=\|f\|^2=\mathbf1^*C\mathbf1.
 \tag{2}
\]
All row selectors remain in \(w\). No column-pair conductor cutoff is
inserted into this positive frame. As in note 2, a successful bound for
the full positive energy transfers to the original signed residual by
the previously justified small-sector reductions.

Assume \(L_N>0\); otherwise the energy is zero. For the unit vector
\(v=\mathbf1/\sqrt{L_N}\), spectral Jensen gives
\((v^*Cv)^3\le v^*C^3v\). Therefore, with the positive functional
\[
 J=\mathbf1^*C^3\mathbf1=f^*G^2f=\|Gf\|^2\ge0,
 \tag{3}
\]
we have
\[
 \boxed{E^3\le L_N^2J,\qquad
       J\le L_N\operatorname{Tr}(G^3).}
 \tag{4}
\]
The second inequality follows from
\(v^*C^3v\le\operatorname{Tr}(C^3)\), using positivity. It is an
upper bound, rather than an identity with the cyclic trace.

Write the desired energy exponent and the earlier cubic trace exponent as
\[
 e=1+dm-s,\qquad h_3=3[1-(1-d)m-s]=3(e-m).
\]
A sufficient actual-probe target is consequently
\[
 \boxed{J\ll_\varepsilon U^{h_3+m+\varepsilon}\mathcal H^a.}
 \tag{5}
\]
Here \(\mathcal H=1+T_1\), and \(a\) denotes a permitted finite height
cost. Equation (4), \(L_N\ll U^m\), and (5) give
\(E\ll U^{e+\varepsilon}\mathcal H^{a'}\). Constants and analytic
losses must be allocated before the source's positive Sobolev step.

The earlier trace target \(\operatorname{Tr}(G^3)\ll U^{h_3+\varepsilon}\)
implies (5). The converse fails even for finite positive frames: take
\[
 T=\begin{pmatrix}a&-a\\1&1\end{pmatrix},\qquad w=(1,1).
\]
Its actual probe has \(E=4\), \(J=16\), independently of \(a\),
whereas \(\operatorname{Tr}(G^3)=8a^6+8\). Thus the probe can
avoid a large eigenspace. This is an exact algebraic illustration, not
an arithmetic counterexample or a physical character construction.

## 2. The open chain retains its endpoints

Use the original masked kernel
\[
 K(u,v)=N^{-1}\sum_k |B(Nk/N)|^2
                 \psi_u(k)\overline{\psi_v(k)}.
\]
Expanding (3) gives exactly
\[
 J=\sum_{u,v,h}w_uw_vw_h\,
       \overline{S_u}K(u,v)K(v,h)S_h.
 \tag{6}
\]
The endpoints cannot be replaced by arbitrary amplitudes or omitted.
In particular (6) is an open chain with two kernels, rather than the
three-kernel cycle from note 2.

Every canceled-ramification zero remains in each row-ratio kernel.
By the imported global family and primitive growth inputs used in note 2,
\[
 |K(u,v)|\ll_\varepsilon U^\varepsilon\mathcal H^a N^{-1/8}
\]
when the inducing primitive characters of \(u,v\) differ; the crude
bound \(|K(u,v)|\ll\mathcal H^a\) covers equal characters. Equal
inducing characters are not assumed to have identical deletion masks.

The needed endpoint input is already explicitly present in the
[amplification manuscript](../../../quasi-rh-character-amplification/manuscript.tex),
Hypothesis “Buffered plain input,” equation `eq:plain-input`, and in
section 1 of the [selector-energy note](../../../quasi-rh-character-amplification/notes/SELECTOR_ENERGY_LOCALIZATION_20261008.md):
\[
 |S_m(u)|^2\ll_\varepsilon
 U^{d\min\{m,\theta(u)-m\}+\varepsilon}\mathcal H^a
 \le U^{dm+\varepsilon}\mathcal H^a
 =N^{d}U^\varepsilon\mathcal H^a,
 \qquad u\in\mathcal C.
 \tag{7}
\]
This is an existing conditional analytic input for the actual plain
profiles and their permitted derivatives. It is not inferred from
arbitrary bounded column coefficients. Restricting it to \(\mathcal C_+\)
is legitimate. Equation (7) gives
\(|S_uS_h|\ll N^dU^\varepsilon\mathcal H^a\).

Without (7), the elementary bound \(|S|^2\ll N\) would lose a
factor \(N^{1/8}\) on chains with an adjacent equal-character pair
relative to the earlier repeated-cycle budget. The endpoint input is
therefore substantive and must be retained in the dependency ledger.

## 3. Repeated characters are controlled

Partition the physical rows by their inducing primitive character. Let
\(A_c=\sum_{u\in c}w_u\), and
\(P=\max_c A_c\). The actual sixth-power-free row family has the
bounded fibers proved in note 2, so \(P\ll_S W\). Define four
disjoint parts of (6):

1. all three primitive characters agree;
2. exactly two agree at adjacent positions, \(u,v\) or \(v,h\);
3. precisely the endpoint characters \(u,h\) agree;
4. all three primitive characters are pairwise different.

Call these \(J_{\rm all}\), \(J_{\rm adj}\), \(J_{\rm end}\), and
\(J_{\ne}\). Reversal makes each grouped sum real. The all-equal
and endpoint-equal sums are nonnegative: their block expressions are,
respectively, \(\sum_c f_c^*G_{cc}^2f_c\) and
\(\sum_{c\ne d}f_c^*G_{cd}G_{dc}f_c\). No sign is asserted for
the other two grouped sums.

Equations (6)--(7) and the kernel estimates give absolute majorants
\[
 |J_{\rm all}|\ll U^\varepsilon\mathcal H^a N^d A P^2,
\]
\[
 |J_{\rm adj}|\ll U^\varepsilon\mathcal H^a
                      N^{d-1/8}A^2P,
 \qquad
 |J_{\rm end}|\ll U^\varepsilon\mathcal H^a
                      N^{d-1/4}A^2P.
 \tag{8}
\]
The harmless factor two for the adjacent orientations is included in
the constants. These estimates count repeated characters, including
different physical rows in one primitive fiber. Every original weight
and mask remains present before taking these majorants.

To compare exponents use note 2's actual inverse-mass bounds
\(A\ll U^{1-\mu+\varepsilon}\mathcal H^a\),
\(W\ll U^{g+\varepsilon}\mathcal H^a\), where
\(g=d(r+z)\). That note proves margins at least
\(154297/500000\) for the all-equal cyclic sector and
\(147/12500\) for its two-equal sector on the operational buffered
region. The new target exponent is larger by \(m\). Relative to
those estimates, (8) adds reserves
\[
 (1-d)m\quad\text{for all-equal and endpoint-equal chains},
 \qquad (7/8-d)m\quad\text{for adjacent-equal chains}.
\]
Using \(d\le21/50\) and \(m\ge2/5\), the resulting margins are
at least
\[
 \begin{array}{c|c}
 \text{chain type}&\text{margin below }h_3+m\\\hline
 \text{all equal}&270297/500000=0.540594\\
 \text{adjacent equal}&1211/6250=0.19376\\
 \text{endpoints equal}&3047/12500=0.24376.
 \end{array}
 \tag{9}
\]
All fixed polynomial height costs and sufficiently small analytic losses
must be assigned in the same prescribed order as notes 1--2. These
large reserves do not bound the remaining distinct-character chains.

## 4. The precise remaining sufficient estimate

The exact decomposition is
\[
 J=J_{\rm all}+J_{\rm adj}+J_{\rm end}+J_{\ne}.
\]
The first three parts are controlled by (8)--(9). A remaining sufficient
arithmetic target is therefore
\[
 \boxed{\operatorname{Re}J_{\ne}
       \ll_\varepsilon U^{h_3+m+\varepsilon}\mathcal H^a,}
 \tag{10}
\]
uniformly over the operational buffered region, the actual selected
weights, and every required derivative and height profile. Its summands
are precisely
\[
 w_uw_vw_h\overline{S_u}K(u,v)K(v,h)S_h
\]
with three pairwise-inequivalent inducing primitive characters. The
bound must use their coupled arithmetic structure. Applying only the
available absolute kernel and endpoint estimates gives
\(O(N^{d-1/4}A^3U^\varepsilon\mathcal H^a)\), which does not
reach (10).

This criterion is weaker than the full cyclic-trace target because it
retains one actual coefficient vector. It still relocates an unproved
arithmetic estimate: no bound for (10), the original energy, or a new
exponent has been obtained. The productive next bounded mixed task is
to test a conductor-resolved or reciprocity-based estimate for this
specific open chain with its endpoints intact. An estimate only for
individual term moduli does not supply the required cancellation.

The short-family obstruction does not establish that this mixed target
is easier. It establishes a reason to stop expecting complete small
cofactor packets alone to save a power, while the mixed formulation
identifies a genuinely less demanding sufficient target than an arbitrary
coefficient operator bound.

## 5. Finite verification and limitations

The [standard-library checker](../../numerics/check_mixed_actual_probe.py)
uses exact rational Gaussian matrices to verify (3)--(4), the open-chain
expansion with actual endpoints, all four character partitions, the
strict-relaxation example, and the rational reserve calculations in (9).
Its [small record](../../numerics/mixed_actual_probe_record_20261008.json)
contains no large matrices or asymptotic sample.
Two fresh runs agree byte for byte: 2,368 exact assertions over 34
rational Gaussian frames. The four-way partition covers 1,764 random-frame
chain terms; there are two negative adjacent-group witnesses and four
negative distinct-group witnesses. The record SHA-256 is
`e7b21e05cdcca176a4e6493cbd3b7bc26d23227db519c0e746b119ee17068bfc`.

These tests do not prove physical reciprocity, bounded primitive fibers,
the global family/growth input, buffered plain estimate, inverse mass,
continuous application-region certificate, or the remaining arithmetic
correlation. Those retain their explicit source status in notes 1--2
and the amplification manuscript. No new family moment or zero-free
boundary is asserted.

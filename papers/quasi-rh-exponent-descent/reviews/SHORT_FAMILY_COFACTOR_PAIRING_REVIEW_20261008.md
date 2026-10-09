# Scoped review of complete small-cofactor pairing

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
The authoring agent checked the saved derivation and a separate same-model
agent independently derived and audited its uniform extension. This is
internal mathematical validation, not independent specialist review or
formal proof verification.

## 1. Audited claim and scope

The audited source is
[note 24](../short_families/notes/24_SHORT_FAMILY_FINITE_COFACTOR_PAIRING_20261008.md).
It establishes a lower bound for the energy of an actual selected signed
product response at \(H=D^{2/5}\), \(\theta=11/20\), with the
permitted trivial fixed twist. If \(M\) is a squarefree good ideal and
\(NM\le D^\beta\) for a fixed \(0<\beta<1/20\), the selected
products are \(n=bqr\), \(b\mid M\), with distinct good prime ideals
\(q,r\), \(Nq,Nr\le z=\sqrt{CD}\), and \((qr,M)=1\).
The actual tail coefficient is used on every row; only the lower-bound
argument restricts to coherent rows. For every fixed nonzero complex
zero-integral smooth annular profile, the selected energy is at least
\[
 \frac{D^{16/15}}
      {(\log D)^{2k_0+2}(\log\log D)^3},
 \tag{1}
\]
up to a positive constant depending on the fixed data and \(\beta\).
Here \(k_0\) is its first nonzero logarithmic profile moment. For fixed
\(M\), the extra logarithmic-logarithmic denominator can be omitted.

This is a genuine nonzero signed combination: \(b=1\) gives semiprimes,
prime divisors \(b\) give negatively signed triples, and all other
divisors of \(M\) retain their actual Möbius signs. The lower bound
does not apply to the full tail or to an arbitrary enlargement of this
block. Its cross term with the remaining products is uncontrolled.
Balanced low-conductor triples with all prime norms near \(D^{1/3}\)
are outside this small-cofactor block and remain available for the
unproved compensation.

## 2. Actual coefficients, cutoffs and deletion zeros

On a coherent row \(u=v^6\) with \(Nv\le D^{1/15}\) and
\((v,M)=1\), the radical comparison gives
\(Y_u\gg D^{23/60}>NM\). On the supported prime-pair range,
\[
 Nq,Nr\ge \frac{cD}{Nb\,z}
       \gg D^{1/2-\beta}>D^{9/20}\ge Y_u.
 \tag{2}
\]
Thus the low divisor prefix contains exactly all divisors of \(b\).
Their signed sum is \(\mu_K(b)\), and the whole squarefree coefficient
is \(2\mu_K(b)\). Because \((v,M)=1\), all primes of \(b\)
have physical phase one. The prime norms in (2) exceed \(Nv\), so the
original zero extensions for \(q,r\) are also one. No deletion mask
has been discarded on a row where it can vanish.

The condition \((qr,M)=1\) gives a unique divisor cofactor \(b\)
for each selected total ideal. On the profile it is automatic from the
stronger bound \(Nq,Nr>NM\). Ordered distinct prime pairs count each
selected ideal twice, so the exact coherent-row formula has coefficient
\(\mu_K(b)\) in front of the ordered pair sum, rather than
\(2\mu_K(b)\). This factor was checked.

Strict \(\beta<1/20\) supplies a fixed power margin in (2). At its
endpoint the displayed constants alone would not compare the lower prime
norm with the largest possible \(Y_u\). The argument does not claim
an endpoint extension, or an obstruction for every differently restricted
prime window when \(\beta\ge1/20\).

## 3. Uniform prime ideal theorem errors and the Jacobian

The proof uses the already imported untwisted quantitative prime ideal
theorem over the fixed field. Every prime norm in the pair sums lies
between a constant times \(D^{1/2-\beta}\) and \(z\). Uniformity
in \(M\) therefore introduces no growing-character theorem.

For a fixed first prime norm \(x\), replacing the second prime sum
costs
\[
 O_W\left(\frac{D}{Nb\,x}
                 e^{-\gamma_\beta\sqrt{\log D}}\right).
\]
The sum of \(1/Nq\) costs at most a logarithm. For the second prime
replacement the continuous function has bounds
\[
 |G_b(x)|\ll_W \frac{D}{Nb\,x\log D},\qquad
 |G_b'(x)|\ll_W \frac{D}{Nb\,x^2\log D}.
 \tag{3}
\]
These remain valid at the moving cutoff after changing variables: its
endpoint contribution is bounded by the same profile seminorms. Integrating
the prime-counting error against (3), including boundary terms, gives
\(O_{\beta,W}((D/Nb)e^{-\gamma_\beta'\sqrt{\log D}})\)
after absorbing logarithms. Summing over all cofactors therefore costs
\[
 D Z_+(M)e^{-\gamma_\beta'\sqrt{\log D}},\qquad
 Z_+(M)=\sum_{b\mid M}(Nb)^{-1}.
 \tag{4}
\]
It is essential to keep \(1/Nb\) in this estimate. Replacing every
per-cofactor error by \(D e^{-\gamma\sqrt{\log D}}\) and then
summing \(\tau(M)\) would not establish the claimed uniform result:
a divisor count for growing \(M\) can exceed that subexponential
saving. The saved proof avoids this pitfall.

The substitution \(Nq,Nr=Dt/Nb\) gives the exact Jacobian
\(D/Nb\), and the truncated pair integral is the same elementary
kernel \(F_B(v+\log Nb)\) as in note 16, with \(B=\log z\).
Consequently the complete signed cofactor inverse is
\[
 \sum_{b\mid M}\frac{\mu_K(b)}{Nb}
       =P_-(M)=\prod_{p\mid M}(1-(Np)^{-1})>0.
 \tag{5}
\]
The bare inverse \(\sum_{b\mid M}\mu_K(b)=0\) for a nonunit
\(M\) is not the rescaled prime-pair main term. The argument depends
on this exact weighted identity, not on a general positivity assertion
for the full response.

The removed diagonal costs
\(O_W(\sqrt D\sum_{b\mid M}(Nb)^{-1/2})\), hence
\(O_{\varepsilon,\beta,W}(D^{1/2+\varepsilon})\). This is smaller
than every fixed logarithmic order of the main amplitude.

## 4. Growing cofactors, profile moments and row counting

The uniform Taylor argument expands first in the bounded profile variable
\(v=\log(C/t)\), rather than pretending that \(\log Nb\) is fixed.
All profile moments below \(k_0\) vanish. The derivative
\(F_B^{(k_0+1)}(l+v)\) is uniformly \(O(B^{-k_0-2})\) for
\(0\le l\le\beta\log D\), so
\[
 \int W(t)F_B(v(t)+\log Nb)\,dt
 =\frac{\alpha_{k_0}M_{k_0}(W)}{B^{k_0+1}}
  +O_{\beta,W}\left(\frac{1+\log Nb}{B^{k_0+2}}\right).
 \tag{6}
\]
The existence of a finite nonzero moment also holds for complex profiles.
Since \(P_-(M)\) is positive, its factor does not rotate the nonzero
complex leading coefficient.

Splitting prime divisors of \(M\) at \(T=\log D\), the fixed-field
prime ideal theorem and \(\sum_{p\mid M}\log Np\le\beta\log D\)
give
\[
 P_-(M)\gg (\log\log D)^{-1},\qquad
 Z_+(M)/P_-(M)\ll (\log\log D)^2,\qquad
 \sum_{p\mid M}\frac{\log Np}{Np+1}\ll\log\log D.
 \tag{7}
\]
Thus the relative Taylor error is
\(O((\log\log D)^3/\log D)=o(1)\), uniformly in \(M\).
This is the needed step between the fixed-cofactor calculation and the
power-growing cofactor theorem.

For \(X=D^{1/15}\), lattice counting in each ideal divisor gives
\[
 \#\{0<Nv\le X:(v,M)=1\}
 =\kappa_K X P_-(M)+O_K(\tau(M)(\sqrt X+1)).
 \tag{8}
\]
The ideal divisor bound and a choice of preliminary
\(\varepsilon<1/30\) make this error
\(O(D^{1/30+\varepsilon})\), smaller than the main term in (8).
The sixth-power map has bounded fibers, and the full nonnegative row
weight is at least one on these rows. Squaring the amplitude contributes
\(P_-(M)^2\); counting the rows contributes one further factor
\(P_-(M)\). The resulting \(P_-(M)^3\) explains the denominator
\((\log\log D)^3\) in (1).

## 5. Verification and remaining obligation

The [finite checker](../numerics/check_short_family_cofactor_pairing.py)
was read and run twice independently of its authoring agent. Both runs
matched the [saved record](../numerics/short_family_cofactor_pairing_record_20261008.json)
byte for byte: 3,289 assertions, 27 actual pairing cases, and 108
phase/deletion checks. The record SHA-256 is
`ea54f5736dce0ab5358ff588b6df1715925f94fb7f74d0aa137951e5a59b083d`.
Its checks include the original truncated tuples, ordered-pair normalization,
exact weighted Euler products, translated first moments, equal-norm
distinct prime symbols, free/complement coefficients, and rational support
margins. The balanced triple has true coefficient \(-6\) and missing
prefix coefficient \(-4\).

These checks cannot verify a prime ideal theorem, uniform analytic Taylor
remainders, asymptotic partial summation or lattice counting, the physical
conductor comparison, or an unbounded signed moment. Those imported
inputs and their scope remain as stated in note 24. This review does not
assert a compilation result as part of that agent's check; the separate
manuscript incorporation and compiler result are recorded below.

The proved obstruction concerns one complete, nonzero signed pairing. It
explains why this pairing still cannot be charged separately to the
\(D^{4/5+\varepsilon}\) budget. It does not prove a counterexample to
that budget for the full tail. Cancellation involving broader cofactor
ranges, balanced odd products, or the remaining total products is still
unbounded. The conclusion required by note 23 is therefore a reassessment
of this attempted pairing, not a newly improved full-moment exponent or
zero-free boundary.

## 6. Supporting audit of the auxiliary free/complement split

[Note 25](../short_families/notes/25_SHORT_FAMILY_PAIRING_REMAINDER_20261008.md)
was read independently of its authoring agent. Its actual selected
response requires \(NM\le Y_u\) and a squarefree residual \(r\)
with every prime norm strictly greater than \(Y_u\). These conditions
give a unique saturated small-prime cofactor \(b\mid M\); they are
essential to \(t_{Y_u}(br)=\mu_K(b)(1+\mu_K(r))\). The finite
dilation profile retains \(\mu_K(b)\lambda_u(b)\) and every
physical deletion zero. Subtracting the genuinely free residual sum
gives exactly the displayed complement: a positive Möbius-weighted
rough-squarefree sum and a negative sum over its coprime nonrough or
nonsquarefree complement. The signs and the \(Y_u<1\) unit-region
assignment were checked.

The extra deletion ideal has completion modulus at most \(L_uNM\).
The shortest dilated scale is \(D/NM\), so both costs are needed:
\[
 |\mathcal F_{u,M}|
 \ll_{A,W}\sigma_{u,M}\tau(E_u)\tau(M)^2\sqrt{Q_u}
           \left(\frac{L_u(NM)^2}{D}\right)^A.
 \tag{9}
\]
Saturation gives
\(L_u(NM)^2/D\le D^{-1/10}/L_u\). For \(A\ge1\), the
existing radical-weighted row mass therefore bounds the normalized energy
by \(\tau(M)^4D^{-1-A/5}H^\delta\). If \(NM>D^{9/20}\)
the selector is identically zero; otherwise the ideal divisor bound
absorbs \(\tau(M)^4\). The resulting arbitrary power decay is
uniform in \(M\) and uses the full Schwartz row weight. It is a
valid bound for the auxiliary free vector, with the original fixed
zero-integral profile estimated separately at every dilated scale.
It does not treat a growing shifted profile as having fixed seminorms.

The arithmetic complement still carries squarefree/roughness conditions
or their exact signed difference. Its nonsquarefree coefficients are not
those of note 17's adaptive nonsquarefree response, so that theorem
cannot be transferred without another argument. The whole retained
combination is \(\mathcal C_{u,M}+\mathcal R_{u,M}
=T_{u,\mathrm{sf}}-\mathcal F_{u,M}\); the generic
\(D^{16/15+\varepsilon}\) bound and the proposed target equivalence
apply to this joint vector. No separate such bound for each new
complement is implied.

The missing-\(4\) example was also checked against the original
truncated convolution. For three prime norms near \(D^{1/3}\) on
the stated low-conductor rows, all singletons are in the low prefix,
the three pair divisors are in the tail with \(c_z=2\), and the
triple has \(c_z=0\). Its true coefficient is \(-6\). Treating
only one selected prime as the small cofactor would give \(-2\)
because the other two primes are falsely treated as satisfying the
roughness hypothesis; their omitted singleton coefficients supply exactly
\(-4\). The common physical phase or deletion zero is preserved.
Finally, the norm of a complete roughness mask is \(\exp(Y+o(Y))\)
under the same fixed-field prime ideal theorem. For power-sized \(Y\)
it exceeds the saturation and completion budgets. These checks confirm
the stated limitation, rather than a target-sized estimate for the
nonzero arithmetic response.

## 7. Supporting audit of the actual-probe mixed-family cubic target

The separate [mixed-family note 3](../mixed_character_families/notes/3_ACTUAL_PROBE_CUBIC_TARGET_20261008.md)
was checked against its preceding frame note and the amplification
manuscript's explicit buffered plain hypothesis. This is a scoped audit
of an exact sufficient criterion and its conditional repeated-character
bounds, not a proof of the remaining mixed correlation.

For \(\mathcal A=\operatorname{diag}(\sqrt w)T\),
\(C=\mathcal A^*\mathcal A\), \(G=\mathcal A\mathcal A^*\),
and the actual probe \(f=\mathcal A\mathbf1\), the identities
\[
 E=\mathbf1^*C\mathbf1=\|f\|^2,\qquad
 J=\mathbf1^*C^3\mathbf1=f^*G^2f=\|Gf\|^2
 \tag{10}
\]
are correct. Spectral Jensen for \(\mathbf1/\sqrt{L_N}\) gives
\(E^3\le L_N^2J\), and positivity gives
\(J\le L_N\operatorname{Tr}(G^3)\). Thus the proposed target
\(J\ll U^{h_3+m+\varepsilon}\mathcal H^a\), with
\(h_3=3(e-m)\) and \(L_N\ll U^m\), suffices for the desired
energy exponent \(e\). It is weaker than the earlier trace criterion:
the displayed two-row frame has \(E=4\), \(J=16\), but cubic trace
\(8a^6+8\) for real \(a\). It is an algebraic example, not a
physical Hecke construction.

Expanding (10) yields two row-ratio kernels with the actual endpoint
plain sums, exactly
\(w_uw_vw_h\overline{S_u}K(u,v)K(v,h)S_h\).
The common selected-row indicator stays in the weights, and every original
zero stays in the kernel. No additional column-pair conductor restriction
has been inserted into the positive Gram frame. The conditional kernel
bound for unequal inducing primitive characters and the bounded primitive
fibers are inherited from mixed note 2; this audit does not prove their
imported global growth and local sextic reciprocity inputs. The fiber
bound specifically requires the actual sixth-power-free physical rows.

The endpoint estimate \(|S_uS_h|\ll N^dU^\varepsilon\mathcal H^a\)
is explicitly supplied by the amplification manuscript's “Buffered plain
input,” restricted to the selected rows. It is not a consequence for
arbitrary coefficient vectors. With maximum character-fiber mass \(P\)
and total mass \(A\), the three repeated-character bounds are
\[
 N^dAP^2,\qquad N^{d-1/8}A^2P,\qquad
 N^{d-1/4}A^2P
 \tag{11}
\]
up to the allocated losses and height costs, for all-equal, adjacent-equal,
and endpoint-equal chains respectively. The adjacent orientations give
only a fixed factor two. The all-equal and endpoint-equal block expressions
are nonnegative; reversal makes all four grouped chain sums real. There
is no unsupported positivity claim for adjacent-equal or pairwise-distinct
chains.

Relative to mixed note 2's certified cyclic margins, the added reserves
are \((1-d)m\) for all-equal and endpoint-equal chains and
\((7/8-d)m\) for adjacent-equal chains. Using \(d\le21/50\)
and \(m\ge2/5\) reproduces exactly
\[
 \frac{270297}{500000},\qquad
 \frac{1211}{6250},\qquad
 \frac{3047}{12500}.
 \tag{12}
\]
This audit recalculated these transfers from the previously certified
baseline margins; it did not independently reprove that baseline's
continuous interval certificate. Replacing the endpoint hypothesis by
the elementary bound would lose \(N^{1/8}\) on the adjacent chains
relative to the old repeated-cycle budget, so the endpoint input is
substantive.

After these three bounds, a one-sided upper estimate for the real
pairwise-inequivalent open-chain sum suffices, because \(J\ge0\).
That remaining estimate is unproved. The available termwise bounds give
\(N^{d-1/4}A^3\), which do not supply its required saving. The
reformulation preserves a particular actual coefficient vector; it does
not establish that the mixed task is easier than the short-family task.

Two independent runs of the
[actual-probe checker](../numerics/check_mixed_actual_probe.py) matched its
[record](../numerics/mixed_actual_probe_record_20261008.json) byte for byte:
2,368 exact assertions over 34 rational Gaussian frames. They verify the
probe identities, open-chain expansion, four partitions, negative grouped
sum witnesses and rational reserves. Finite Gaussian frames do not prove
the arithmetic kernel, endpoint, fiber or inverse-mass inputs, permitted
profile/height uniformity, or the remaining distinct-character estimate.

## 8. Manuscript incorporation and saved-source verification

The existing [standalone manuscript](../short_families/short_family_reductions.tex)
now includes the theorem “Complete small-cofactor obstruction” and its
proof in the section on selected pieces that cannot meet the useful
budget. A separate same-model agent compared the saved insertion with
note 24 and found no mathematical defect. The proof retains weighted
prime ideal theorem errors, the growing-cofactor Taylor remainder,
coprime coherent-row density and the full-tail cross-term limitation.

The native desktop editor compiler returned success for saved source
SHA-256
`3c8ee8ee95b9afd2a4d16400ebead075207e38e38e8ede29ca5c7242b52c2219`.
Static source checks found 131 unique labels, 115 references and 20
bibliography entries, with no unresolved references or citations. All
local links in the current changed/new research files resolve, whitespace
checks pass, and the two new records reproduce byte for byte. These are
source and finite-algebra checks with the analytic limitations stated
above; compilation does not verify the mathematics.

The current continuation and next bounded task are in
[note 26](../short_families/notes/26_SHORT_FAMILY_COFACTOR_CONTINUATION_20261008.md).
The changes remain uncommitted. No new full moment, scalar exponent or
zero-free boundary is claimed.

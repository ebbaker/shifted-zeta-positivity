# Finite-prime pairing, a free completion, and the signed remainder

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Status: exact finite resummation, a rapidly decaying auxiliary free
response under the existing completion input, and an explicit obstruction
to identifying that free response with the retained arithmetic response.
No new target-sized estimate for a nonzero sector is proved.
This is internal mathematical work, not independent specialist validation
or formal proof verification.

## Outcome

A complete finite-prime parity sum does give an explicit shifted profile.
If the chosen finite prime product is saturated, the corresponding
**genuinely free** character sum has arbitrarily rapid weighted energy
decay, even after paying the extra deletion modulus and every profile
shift. The actual response, however, restricts the residual factor to
squarefree ideals all of whose primes exceed the adaptive cutoff. Its
difference from that free sum is an exact signed complement. No existing
estimate pays for that complement, and it includes the cancellation still
needed for the original target.

Balanced low-conductor triples give a concrete failure of a tempting
shortcut. Resumming one selected prime would predict coefficient \(-2\)
if the other two prime factors were wrongly treated as rough. The actual
coefficient is \(-6\). The missing \(-4\) is supplied by the two omitted
singleton prefix divisors. This is a failure of a hypothesis, not a
small completion error.

The [companion finite-cofactor obstruction note](24_SHORT_FAMILY_FINITE_COFACTOR_PAIRING_20261008.md)
treats selected paired blocks, including their coherent-row lower bounds. The present note
focuses on the exact free/complement split and its norm budget.

## 1. The actual finite-prime paired response

Use the good ideal monoid, physical zero-extended characters and imported
inputs of the [manuscript](../short_family_reductions.tex). Keep
\[
 H=D^{2/5},\quad z=\sqrt{CD},\quad
 Y_u=D^{9/20}/L_u,\quad
 \lambda_u(n)=\psi_u(n)\mathbf1_{(n,E_u)=1},\quad L_u=Q_uNE_u.
 \tag{1}
\]
The primitive character is extended by zero at its conductor and the
fixed bad primes. Let \(W\in C_c^\infty((0,\infty))\) have fixed
annular support \([c_0,C]\), and assume explicitly \(\int W=0\)
for the free-completion estimate below. The finite algebra itself does
not require zero integral.

For squarefree total ideals on the profile, sufficiently large \(D\)
gives the exact adaptive coefficient
\[
 t_Y(n)=\mu_K(n)+\sum_{\substack{d\mid n\\Nd\le Y}}(-2)^{\omega(d)}.
 \tag{2}
\]
This is the coefficient of the actual truncated convolution tail, not a
replacement coefficient. In particular it includes the unit divisor
when \(Y\ge1\), with equality assigned to the prefix.

Choose a squarefree good ideal \(M=M(D)\), independent of the row.
It may grow with \(D\). Put
\[
 \sigma_{u,M}=\mathbf1_{NM\le Y_u},\qquad
 \mathcal A_{Y}(M)=
 \{r:r\text{ squarefree},\ (r,M)=1,\ P^-(r)>Y\},
 \tag{3}
\]
where \(P^-(1)=\infty\). Define the actual selected response
\[
 \mathcal P_{u,M}
 =\sigma_{u,M}\sum_{b\mid M}\sum_{r\in\mathcal A_{Y_u}(M)}
              t_{Y_u}(br)\lambda_u(br)W(Nb\,Nr/D).
 \tag{4}
\]
The sum is finite on the profile. On a selected row, every prime of
\(b\mid M\) has norm at most \(NM\le Y_u\), while every prime
of \(r\) has norm strictly greater than \(Y_u\). Thus \(b\) is
the complete small-prime cofactor \(b_{Y_u}(br)\), it is saturated,
and the representation is unique. Consequently (4) is an actual
projection by total ideal of \(T_{u,\mathrm{sf}}\): it retains precisely
the columns whose full small-prime cofactor divides \(M\), on the
selected rows. Its saturated odd rough cores have coefficient zero;
its even rough cores need not cancel.

The complete cofactor identity of note 21 gives, exactly,
\[
 t_{Y_u}(br)=\mu_K(b)(1+\mu_K(r))
 \quad\text{on every nonzero summand of (4)}.
 \tag{5}
\]
The qualifications in (3) matter. It is insufficient that only the
chosen primes of \(M\) lie below \(Y_u\); all other primes of the
residual \(r\) must lie above it.

## 2. Exact shifted profile and signed complement

For each physical row define
\[
 W_{u,M}(x)=\sum_{b\mid M}\mu_K(b)\lambda_u(b)W(Nb\,x)
 =\prod_{p\mid M}(1-\lambda_u(p)\mathcal T_{Np})W(x),
 \quad (\mathcal T_aW)(x)=W(ax).
 \tag{6}
\]
All these dilation operators commute. Complete multiplicativity,
including deletion zeros, turns (4) into
\[
 \boxed{\mathcal P_{u,M}
 =\sigma_{u,M}\sum_{r\in\mathcal A_{Y_u}(M)}
        (1+\mu_K(r))\lambda_u(r)W_{u,M}(Nr/D).}
 \tag{7}
\]
This is a complete finite signed sum before any absolute value.
It retains the squarefree and roughness selector. It does not produce
a free residual ideal sum.

Put
\[
 \lambda_{u,M}(r)=\lambda_u(r)\mathbf1_{(r,M)=1},\qquad
 \mathcal F_{u,M}
 =\sigma_{u,M}\sum_{r\in\mathcal I_S}
                   \lambda_{u,M}(r)W_{u,M}(Nr/D).
 \tag{8}
\]
This sum is genuinely free in \(r\); it includes nonsquarefree and
nonrough ideals. Let
\[
 \mathcal B_Y(M)=\{r:(r,M)=1\}\setminus\mathcal A_Y(M).
 \tag{9}
\]
The exact signed complement is
\[
\boxed{
 \mathcal C_{u,M}=\sigma_{u,M}\left\{
 \sum_{r\in\mathcal A_{Y_u}(M)}
                 \mu_K(r)\lambda_u(r)W_{u,M}(Nr/D)
 -\sum_{r\in\mathcal B_{Y_u}(M)}
                         \lambda_u(r)W_{u,M}(Nr/D)\right\},
 \qquad \mathcal P_{u,M}=\mathcal F_{u,M}+\mathcal C_{u,M}.
}
 \tag{10}
\]
There is no absolute value in this identity. More explicitly,
\(\mathcal B_Y(M)\) is the disjoint union of nonsquarefree ideals
coprime to \(M\) and squarefree ideals coprime to \(M\) having at
least one prime of norm at most \(Y\). Thus the second sum retains
both kinds of omitted columns, with their actual sign and profile.
Its nonsquarefree part is not the adaptive nonsquarefree response of
note 17, whose coefficients were different. That theorem cannot be
assigned to this new complement without a new argument.

For the entire retained response, define
\[
 \mathcal R_{u,M}=T_{u,\mathrm{sf}}-\mathcal P_{u,M}.
\]
Then exactly, on every row,
\[
 \boxed{T_{u,\mathrm{sf}}
     =\mathcal F_{u,M}+\mathcal C_{u,M}+\mathcal R_{u,M}.}
 \tag{11}
\]
The response \(\mathcal R_{u,M}\) retains all unsaturated products,
all other saturated even rough cores, and every row failing
\(NM\le Y_u\). In particular, when \(Y_u<1\), all of (4), (8)
and (10) are zero and \(\mathcal R_{u,M}=T_{u,\mathrm{sf}}\).
The earlier Schwartz treatment of that unit region remains applicable;
the exact split does not silently discard it.

Each dilation preserves zero integral when \(W\) has zero integral:
\[
 \int W_{u,M}(x)\,dx
 =\left(\sum_{b\mid M}\frac{\mu_K(b)\lambda_u(b)}{Nb}\right)
                       \int W(x)\,dx=0.
 \tag{12}
\]
Moreover the Euler derivative \(x\partial_x\) commutes with every
dilation. Hence a detector profile \(W=(1+x\partial_x)V\) remains
of that form after this finite resummation. When \(M\) grows, the
support of \(W_{u,M}\) may extend down to \(c_0/NM\), and its
constants cannot be treated as those of one fixed annular profile.
The proof below therefore estimates every fixed-profile sum at its own
scale \(D/Nb\), rather than assuming uniform profile seminorms.

## 3. The auxiliary free response has rapid weighted decay

Let \(\mathfrak q_u\) be the primitive conductor. Set
\[
 M_u^\sharp=\prod_{\substack{p\mid M\\p\nmid\mathfrak q_uE_u}}p,
 \quad E_{u,M}=E_uM_u^\sharp,
 \quad L_{u,M}=L_uNM_u^\sharp\le L_uNM.
 \tag{13}
\]
The inducing conductor remains \(Q_u\), and
\(\tau(E_{u,M})\le\tau(E_u)\tau(M)\). Expanding the added mask
by its finite divisor inclusion-exclusion, the manuscript's imported
primitive completion gives, for the fixed zero-integral profile \(W\),
\[
 S_{u,M,W}(X):=\sum_r\lambda_{u,M}(r)W(Nr/X),
 \qquad
 |S_{u,M,W}(X)|\ll_{A,W}
       \tau(E_{u,M})\sqrt{Q_u}(L_{u,M}/X)^A.
 \tag{14}
\]
This is the same completion proof with an additional finite deletion
ideal, not a new conductor-uniform Möbius or prime estimate.

Using the finite profile sum (6), exactly
\[
 \mathcal F_{u,M}
 =\sigma_{u,M}\sum_{b\mid M}\mu_K(b)\lambda_u(b)
                                 S_{u,M,W}(D/Nb).
 \tag{15}
\]
Therefore the actual deletion modulus and every dilation give
\[
 |\mathcal F_{u,M}|
 \ll_{A,W}\sigma_{u,M}\tau(E_u)\tau(M)^2\sqrt{Q_u}
                       \left(\frac{L_u(NM)^2}{D}\right)^A.
 \tag{16}
\]
Indeed, apply (14) to each term of (15), use \(L_{u,M}\le L_uNM\),
and bound \(\sum_{b\mid M}(Nb)^A\le\tau(M)(NM)^A\).
The square \((NM)^2\) pays both the extra mask and the shortest
dilated scale. It is not legitimate to use the original \(L_u\)
in (14) without this mask cost.

On selected rows,
\[
 NM\le D^{9/20}/L_u
 \quad\Longrightarrow\quad
 \frac{L_u(NM)^2}{D}\le \frac{D^{-1/10}}{L_u}.
 \tag{17}
\]
Thus, for \(A\ge1\), the full Schwartz-weighted energy satisfies
\[
\begin{split}
 \frac1D\sum_{u\ne0}\Phi(Nu/H)|\mathcal F_{u,M}|^2
 &\ll_{A,W}\frac{\tau(M)^4D^{-A/5}}D
       \sum_{u\ne0}\Phi(Nu/H)
                  \frac{\tau(E_u)^2Q_u}{L_u^{2A}}\\
 &\ll_{A,\delta,W,\Phi}
          \tau(M)^4D^{-1-A/5}H^\delta.
\end{split}
 \tag{18}
\]
The last inequality is the manuscript's already proved radical-weighted
row mass, since \(L_u\ge1\) and \(A\ge1\). The adaptive selector
was used pointwise before taking the nonnegative row sum. No
row-dependent coefficient vector or selector was inserted into a
completed physical operator. An additional scalar row selector of
modulus at most one can be inserted without changing this bound.

If \(NM>D^{9/20}\), the selector is identically zero. Otherwise the
ideal divisor bound gives \(\tau(M)^4\ll_\varepsilon D^\varepsilon\),
uniformly for \(M=M(D)\). For \(1\le H\le D\), choose \(A\)
after the requested decay order in (18). Consequently
\[
 \boxed{\frac1D\sum_{u\ne0}\Phi(Nu/H)
             |\mathcal F_{u,M}|^2=O_N(D^{-N})
        \quad\text{for every }N>0.}
 \tag{19}
\]
This controls the auxiliary **free** vector, not the actual vector in
(4) or its complement in (10). The proof remains valid for the
complete Schwartz weight, including exterior coherent rows; it needs
no row truncation. Zero integral is essential. Without it, the exact
principal term in (15) would be
\[
 \sigma_{u,M}\kappa_{u,M}D\left(\int W\right)
              \sum_{b\mid M}\frac{\mu_K(b)\lambda_u(b)}{Nb},
 \tag{20}
\]
where \(\kappa_{u,M}\) is the residue for \(\lambda_{u,M}\).
It cannot be omitted.

Equation (19) allows replacement of (11) by
\(\mathcal C_{u,M}+\mathcal R_{u,M}\) in a proposed energy bound
using the weighted triangle inequality in either direction. It is
not an additive moment identity. It has merely transferred the open
signed estimate to a specified complement plus the rest of the actual
response. No new power bound for that combination follows from (18).

## 4. Why a full roughness mask exceeds this budget

To express the roughness condition \(P^-(r)>Y\) as a single finite
coprimality mask, the natural ideal is
\[
 \mathfrak P_Y=\prod_{\substack{p\in\mathcal I_S\ \mathrm{prime}\\Np\le Y}}p.
 \tag{21}
\]
The already imported fixed-field prime ideal theorem, by partial
summation, gives
\[
 \log N\mathfrak P_Y=\sum_{Np\le Y}\log Np=Y+o(Y).
 \tag{22}
\]
Removing finitely many fixed bad primes changes only a bounded term.
This is a use of the existing untwisted fixed-field prime-counting
input, not a new estimate uniform in the growing Hecke conductors.
The exact identities (3)--(20) do not require (22).

For \(Y=D^\gamma\), fixed \(\gamma>0\), the mask norm in (21)
is superpolynomial in \(D\). It cannot satisfy
\(N\mathfrak P_Y\le Y\), the saturation condition needed for (5)
over every divisor of the full mask. Nor can its extra deletion norm
be ignored in (14). On the usual significant row range
\(Nu\le D^{2/5+\eta}\), with fixed \(0<\eta<1/20\), the existing
comparison \(L_u\ll Nu\) gives
\(Y_u\gg D^{1/20-\eta}\), so this mismatch is present uniformly
throughout that range for large \(D\).

A smaller prime set with polynomial total norm can be resummed exactly,
but leaves the primes between that set and \(Y_u\) in the nonrough
complement of (10). Truncating the divisor sum of \(\mathfrak P_Y\)
at \(Nb\le Y\) also destroys the complete Euler-product profile;
its overflow and boundary terms must be restored. Either choice
retains a new arithmetic response instead of proving it negligible.
The fixed/growing finite-prime paired-block obstruction is treated
in [note 24](24_SHORT_FAMILY_FINITE_COFACTOR_PAIRING_20261008.md), rather than repeated here.

## 5. An explicit missing-\(4\) balanced-triple counterexample

Let \(p,q,r\) be distinct good primes with norms comparable to
\(D^{1/3}\), with product in a nonzero part of the \(D\)-profile.
Fix \(\gamma>0\) and take a low-conductor row satisfying
\[
 L_u\le D^{7/60-\gamma}.
 \tag{23}
\]
For sufficiently large \(D\), all three singleton norms lie below
\(Y_u\), all three pair norms lie above \(Y_u\), every singleton
lies below \(z\), and every pair lies above \(z\). The fixed prime
window constants are absorbed by the positive exponent margins.
The true prefix coefficient is
\[
 t_{Y_u}(pqr)=-1+(1-2-2-2)=-6.
 \tag{24}
\]
Equivalently, in the original truncated tail the singleton divisors are
below \(Y_u\), the three pair divisors have \(c_z=2\), and the
triple has \(c_z=0\), giving \(-6\). This keeps the actual factor
cutoffs and does not rely on replacing the original coefficient class.

Choose only \(M=p\). It is saturated, since \(Np\le Y_u\).
However the residual \(qr\) is **not** \(Y_u\)-rough: both its
primes lie below \(Y_u\). Applying (5) without that hypothesis
would predict
\[
 \mu_K(p)(1+\mu_K(qr))=-2.
 \tag{25}
\]
The error \(-4\) consists exactly of the two omitted singleton
prefix coefficients for \(q\) and \(r\), each equal to \(-2\).
The actual complete small-prime cofactor is \(pqr\), whose norm is
of order \(D>Y_u\), so it is unsaturated. This is an example from
the retained overflow response, not from (7).

The scale discrepancy is equally explicit. The unmultiplied semiprime
core satisfies \(N(qr)\asymp D^{2/3}\), hence
\(W(N(qr)/D)=0\) for all sufficiently large \(D\). Its multiplied
partner can have \(W(N(pqr)/D)\ne0\). A guessed two-term shifted
profile \((1+\mu_K(qr))\lambda_u(qr)\{W(N(qr)/D)
-\lambda_u(p)W(N(pqr)/D)\}\) would therefore assign only
\(-2\lambda_u(pqr)W(N(pqr)/D)\). The true contribution is
\(-6\lambda_u(pqr)W(N(pqr)/D)\). The missing response has the
same physical phase, or the same deletion zero, at the common total
ideal. It is not a free-frequency remainder.

Coherent inner rows have \(L_u\ll D^{1/15}\), which lies below
\(D^{7/60-\gamma}\) whenever \(0<\gamma<1/20\). Thus the
counterexample concerns the surviving coherent range identified in
notes 21--23. It does not disappear under the large-conductor odd-core
cancellation theorem.

## 6. Relation to the complete discrepancy bridge and remaining target

The free/complement split does not remove any term from note 22's
mixed-discrepancy bridge for the actual \(T_{u,\mathrm{sf}}\).
Its von Mangoldt density is still \(\delta_u\), its two edges and
low/low correction still recombine, and its sharp adaptive endpoints
remain. Equation (12) removes only a genuinely free principal frequency
when (15) is completed; it does not remove a prime-density term from
the arithmetic complement. Similarly, (19) does not bound either the
Möbius or the prime-power factor in that bridge.

For its fixed outer squarefree product \(h=cm\), note 22 retains
\(L_{u,h}=L_uNh\) on every nonzero outer summand, with
\(Nh\) ranging from order \(D^{1/2}\) to order \(D\). The
smaller saturated mask \(M\) in (13) concerns the auxiliary free
residual variable and must not be substituted for those outer masks.
No opposing-edge cancellation has been proved for surviving balanced
semiprimes, which can lie wholly in one edge.

The exact full target can now be written as
\[
 \frac1D\sum_{u\ne0}\Phi(Nu/D^{2/5})
             |\mathcal C_{u,M}+\mathcal R_{u,M}|^2
               \ll_{\varepsilon,W}D^{4/5+\varepsilon},
 \tag{26}
\]
equivalently to the original squarefree target by (11) and (19).
This is an equivalent response with a precisely stated signed remainder,
not a new bound. The imported physical operator still supplies only
the generic \(D^{16/15+\varepsilon}\) budget without an additional
arithmetic cancellation estimate. Compensation across distinct total
products, including the low-conductor odd products in (24), remains
uncontrolled.

The [cofactor checker](../../numerics/check_short_family_cofactor_pairing.py)
and [record](../../numerics/short_family_cofactor_pairing_record_20261008.json)
verify the exact free/complement partition, including nonsquarefree
complement terms, strict rough thresholds, unit boundaries and deletion
zeros. It independently checks the balanced triple against original
truncated tuples: true coefficient \(-6\), naive coefficient \(-2\),
missing prefix \(-4\). Two fresh runs reproduce all 3,289 assertions
byte for byte. The [scoped review](../../reviews/SHORT_FAMILY_COFACTOR_PAIRING_REVIEW_20261008.md)
also audits both norm costs and the final weighted-mass estimate.
Finite checks validate algebra and rational margins; the rapid-decay
conclusion additionally uses the manuscript's imported primitive completion
and proved row-mass lemma. No finite calculation certifies (26).

Sources: [rough-core parity](21_SHORT_FAMILY_ROUGH_PARITY_20261008.md),
[complete masked discrepancy](22_SHORT_FAMILY_SQUAREFREE_DISCREPANCY_20261008.md),
[preceding continuation](23_SHORT_FAMILY_PARITY_CONTINUATION_20261008.md),
and the [manuscript](../short_family_reductions.tex). Deep analytic inputs
retain their existing imported status.

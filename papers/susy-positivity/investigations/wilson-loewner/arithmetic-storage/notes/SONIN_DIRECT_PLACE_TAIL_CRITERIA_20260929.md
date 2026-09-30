# Moving source tails and signed place addition criteria

29 September 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed. This is a new internal analytic derivation, not an external
referee assessment. No new numerical certificate is claimed.

See the [active program](SONIN_DIRECT_POSITIVE_LIMIT_PROGRAM_20260929.md)
and [internal review](../reviews/SONIN_DIRECT_LIMIT_REVIEW_20260929.md).

## Result and its limit

The literal candidate positive approximants are

\[
 B_S[F]=\|C_F P_S\|_{\mathrm{HS}}^2,
 \qquad P_S=\operatorname{proj}(D_S\mathcal K),
 \qquad D_S=\prod_{q\in S}(I-q^{-1/2}U_{\log q}).
\]

The new lemma below bounds an exact place increment using **moving spatial
tails of the source-smoothed state**. It applies to every finite transported
Sonin space with the same algebraic constants. It does not assume that the
old projection is the original archimedean projection. It distinguishes the
leading signed covariance from higher returns; the quadratic remainder
shrinks with the source tail, rather than carrying an unavoidable constant
multiple of `B_S/p`.

This gives an explicit sufficient Cauchy criterion for `S={q:q<=R}`. The
required tail or signed-series estimates have not been proved along that
growing family. Even if the criterion is proved, identifying its limit with
the complete Weil form remains a separate theorem. The statement therefore
advances the analytic organization of the direct-limit route; it does not
establish the desired arithmetic limit.

## 1. The transported spaces retain two exact cutoff constraints

Work in logarithmic coordinates, with `R=1_(0,infinity)`. The positive-axis
cosine involution, conjugated into these coordinates, is denoted `Fcal`.
It reverses translations: `Fcal U_a=U_-a Fcal`. Its Sonin space is

\[
\mathcal K=\{h:Rh=h,\quad R\mathcal Fh=\mathcal Fh\}.
\]

All finite-place factors and their inverses are bounded. Since the inverse
of `I-r U_a` is the norm-convergent causal series `sum r^n U_(na)`, both
`D_S` and `D_S^-1` preserve `R H`; hence `D_S R H=R H`. Define

\[
\mathcal F_S=D_S\mathcal F D_S^{-1}
=D_S(D_S^*)^{-1}\mathcal F.
\tag{1}
\]

The second equality uses `Fcal D_S Fcal=D_S*`. All translation polynomials
commute, and `D_S(D_S*)^-1` is unitary. Consequently `Fcal_S` is a unitary
selfadjoint involution, reverses translations, and

\[
D_S\mathcal K
=\{h:Rh=h,\quad R\mathcal F_Sh=\mathcal F_Sh\}.
\tag{2}
\]

It follows that `P_S<=R`, `P_S` commutes with `Fcal_S`, and
`P_S<=Fcal_S R Fcal_S`. These identities do not use condition-number bounds
for a cumulative inverse metric.

For **fixed finite** `S`, they imply

\[
P_SU_{\pm a}P_S\longrightarrow0\quad\text{strongly as }a\to\infty.
\tag{3}
\]

For example,
`||P_S U_a h||<=||R U_-a Fcal_S h||->0`; the opposite sign uses the
physical cutoff directly. Statement (3) alone is not uniform as `S` grows
and supplies no summable rate over primes.

## 2. Source-weighted tail quantities

Fix a **real** compact smooth source `F`, with `supp F subset[-b,b]`.
Both additive parities are permitted. Set, on the ambient Hilbert space,

\[
V=C_FP_S,\quad W=V^*V=P_SC_F^*C_FP_S,\quad B=\operatorname{Tr}W.
\tag{4}
\]

`V` is Hilbert–Schmidt by the already audited smoothing theorem; `W` and
`VV*` are positive trace class. Operators initially defined on `Ran P_S`
are extended by zero on its orthogonal complement. For `E_t=1_(t,infinity)`
and `B>0`, define

\[
i_S(a)=\frac{\operatorname{Tr}(E_aW)}B
=\frac{\|V E_a\|_{\mathrm{HS}}^2}B,
\qquad
o_S(a)=\frac{\operatorname{Tr}(E_{a-b}VV^*)}B
=\frac{\|E_{a-b}V\|_{\mathrm{HS}}^2}B.
\tag{5}
\]

Both numbers lie in `[0,1]`. The first measures the input-side source trace
beyond `a`; the second measures output-side trace beyond `a-b`. They vanish
as `a->infinity` for a fixed `S`, by trace-class monotone convergence.

Because `F` is real, its autocorrelation is even. Therefore `K=C_F*C_F`
commutes with `Fcal_S`, and so does `W`. In addition, the range of `V` is
supported in `[-b,infinity)`, since the range of `P_S` is supported in
`[0,infinity)`.

Let

\[
A_p=(U_a+U_{-a})/2,\quad T=P_SA_pP_S|_{\operatorname{Ran}P_S},
\quad H=V^*A_pV,\qquad a=\log p.
\]

The two cutoffs and the commutation of `W` with `Fcal_S` give

\[
d:=\operatorname{Tr}(T^2W)=\|TW^{1/2}\|_{\mathrm{HS}}^2
\le\operatorname{Tr}(E_aW)=B i_S(a).
\tag{6}
\]

Indeed each of `P_S U_a W^(1/2)` and `P_S U_-a W^(1/2)` has HS norm at
most `sqrt(Tr(E_aW))`: one uses the Fourier cutoff, the other the physical
cutoff. The triangle inequality for their average proves (6).

A translated overlap of vectors supported in `[-b,infinity)` satisfies
the ordinary Cauchy–Schwarz tail bound. Summing a trace-class decomposition
therefore gives

\[
|\operatorname{Tr}H|\le B\sqrt{o_S(a)},\qquad
|\operatorname{Tr}(TW)|\le B\sqrt{i_S(a)}.
\tag{7}
\]

These are smoothed source tails, not tails of the unsmoothed projection.
The latter generally have infinite trace and cannot be substituted in (5).

## 3. Exact leading term and controlled higher returns

For adjoining a prime `p` not in `S`, write `r=p^(-1/2)` and
`beta=2r/(1+r²)`. The audited place-addition identity is

\[
\delta_p^S:=B_{S\cup\{p\}}-B_S
=-\beta\operatorname{Tr}\bigl((I-\beta T)^{-1}(H-TW)\bigr).
\tag{8}
\]

This retains the actual compressed inverse metric. Splitting its resolvent
once gives

\[
\frac{\delta_p^S}B=-\beta c_{S,p}+e_{S,p},\quad
c_{S,p}=\frac{\operatorname{Tr}(H-TW)}B,
\tag{9}
\]
\[
\boxed{|e_{S,p}|\le
\frac{\beta^2}{1-\beta}\{\sqrt{i_S(a)}+i_S(a)\}.}
\tag{10}
\]

For the first remainder term use
`||T V*||HS=sqrt(d)`, `||A_p V||HS<=sqrt(B)`, and
`||(I-beta T)^-1||<=(1-beta)^-1`. For the other term,
`Tr((I-beta T)^-1 T²W)` is nonnegative and at most `d/(1-beta)`.
These facts and (6) prove (10). Equation (7) also gives

\[
|c_{S,p}|\le\sqrt{i_S(a)}+\sqrt{o_S(a)},
\]
\[
\boxed{\frac{|\delta_p^S|}B\le
\beta\{\sqrt{i_S(a)}+\sqrt{o_S(a)}\}
+\frac{\beta^2}{1-\beta}\{\sqrt{i_S(a)}+i_S(a)\}.}
\tag{11}
\]

For fixed `S`, (9)–(10) give a leading coefficient tending to zero and an
`o(p^-1)` higher-return remainder. Equivalently, the expansion in `r` is

\[
\delta_p^S=-r\operatorname{Tr}X-r^2\operatorname{Tr}((P_SZP_S)X)
+O(r^3B),\quad X=P_SZ(I-P_S)KP_S,\ Z=U_a+U_{-a}.
\]

The source tails control the displayed coefficients. The statement does
not mean that either coefficient vanishes exactly, and it does not turn
fixed-`S` asymptotics into asymptotics along `S={q:q<p}`.

## 4. Two non-tautological fixed-test Cauchy criteria

Order the primes increasingly and evaluate (5), (9) on the *actual old*
set `S_p={q:q<p}`. All constants below may depend on the fixed source.

**Absolute moving-tail criterion.** If the right side of (11), denoted
`alpha_p`, satisfies `sum_p alpha_p<infinity`, then `B_(S_p)[F]` converges
to a finite nonnegative limit. An independently established bound on
`B_(S_p)` is unnecessary: `B_next<=(1+alpha_p)B_current` bounds the sequence
by a convergent product, and then the increments are absolutely summable.
One simple sufficient rate is

\[
i_{S_p}(\log p)+o_{S_p}(\log p)\le C_F p^{-1-\epsilon},
\qquad\epsilon>0.
\tag{12}
\]

It makes the leading bound `O_F(p^-1-epsilon/2)`, summable even over all
integers. This sufficient rate is deliberately stronger than necessary.
Failure of (12) would not refute convergence or the Sonin route.

**Signed leading-covariance criterion.** A less restrictive sufficient
package, retaining first-order cancellation, is

\[
\sum_p\frac{\beta_p^2}{1-\beta_p}
 (\sqrt{i_{S_p}(\log p)}+i_{S_p}(\log p))<\infty,
\tag{13}
\]
\[
\sum_p\beta_p c_{S_p,p}\quad\text{converges as a signed series},
\qquad \sum_p\beta_p^2 c_{S_p,p}^{\,2}<\infty.
\tag{14}
\]

If `B_initial>0`, every subsequent `B` is positive because the place map
and compressed metric are invertible. Put `z_p=delta_p/B_current`.
Equations (9), (13), and (14) imply convergence of `sum z_p` and
`sum z_p²`; hence `sum log(1+z_p)` converges and the product of trace ratios
has a finite positive limit. If `B_initial=0`, the source-smoothed operator
is zero and remains zero under every commuting invertible place transport.

These criteria involve spatial trace escape and signed compressed
translation correlations, not the arithmetic residual `Q-B_S`. They do
not assume the Weil sign. Their usefulness depends on obtaining these
estimates from the actual growing family, which has not been done here.

## 5. Compact source support does not settle the tail condition

Once `p` exceeds the source difference-support threshold, its direct Weil
prime correlations vanish. Equations (8)–(11) still contain the projection
and source-smoothed return correlations; they do not truncate. The finite
place changes `B_S` even though it changes no direct arithmetic term for
that source. That distinction is central to a fixed-test limit.

For each fixed `S`, trace-class smoothing makes (5) tend to zero. The
needed statement is diagonal in two parameters: `S` grows at the same time
as the spatial cutoff `a=log p` moves. No uniform *fixed spatial cutoff* is
being demanded. Slow movement of the smoothed state to infinity can be
compatible with (12) or (13), depending on its rate and signed covariance.

The elementary transport bound illustrates why a naive uniform estimate
loses information. Let `V0=C_F Pi`, `ell_S=prod_(q in S)(1-q^-1/2)`, and
write `tau0(t)=||E_t V0||HS²`. The canonical isometry gives
`C_F J_S=D_S V0 A_S^-1/2`. Consequently

\[
\|E_t C_FJ_S\|_{\mathrm{HS}}
\le\ell_S^{-1}\sum_{d\mid\prod_{q\in S}q}
d^{-1/2}\sqrt{\tau_0(t-\log d)}.
\tag{15}
\]

The right side discards the Möbius signs. Many subset products `d` already
exceed the next prime, so their shifted cutoffs are negative; `ell_S^-1`
also deteriorates. Thus merely proving rapid tails for `V0` and inserting
them in (15) does not supply the required diagonal estimate. A useful
argument must retain cancellations, obtain source-specific transported
tail bounds, or directly control the signed coefficient in (14).

## 6. Real sources, complex tests, and the remaining identification

All projections and transports have real kernels. For real `u,v`, the HS
inner product of `C_u P_S` and `C_v P_S` is real, so

\[
B_S[u+iv]=B_S[u]+B_S[v].
\]

The Weil form has the same real-kernel property. Proving the proposed
fixed-test limit on every real compact smooth admissible source therefore
extends it to complex tests; real and imaginary parts preserve the
pole-neutral moment conditions. Mixed pairings follow by polarization.
No restriction to one additive parity is introduced.

Even a proved Cauchy criterion above would yield a positive form `B_limit`,
not automatically `Q`. For a fixed pole-neutral source the direct prime
sum is finite, while inactive-place increments continue indefinitely.
The additional arithmetic identification must establish

\[
B_\infty[F]+\sum_p\delta_p^{S_p}[F]=Q[F]
\]

by an independently justified trace, boundary, or limiting identity.
Writing this equation as the desired value of the series is only a target.
The present advance is the explicit moving-tail control of its convergence
and the separation of the leading signed term from higher returns.

# Rational witness addendum for B03 R6

30 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Parent/editor **gpt-6-astra / ultra**, Investigation05 chat0049. The mathematical witness below was supplied by a read-only **gpt-6.1-sol / ultra** proof-check contribution. It is an internal shared-premise check, not specialist/formal independence. Actual saved-data endpoint verification is assigned to E02 R6.

The [B03 R6 proof](B03_R6_PRIMITIVE_ABSOLUTE_PAYMENT_OBSTRUCTION_20261030.md) and issued E01 R3 packet remain unchanged. This is a cheaper second witness within the same interval and same payment, discovered after the panel packet was issued. It does not expand or replace that packet. Let I=[1/32,1/4] and use the rational subinterval J=[5/64,3/32], of length 1/64.

On J put
\[
 A(u)=\frac{8187}{2}u^3-6u-\frac{u^5}{4},\qquad
 B(u)=384u^2+64u^4.
\]
Then Q=A(−sin64u)+B cos64u. The interval 64J=[5,6] lies in (3π/2,2π). On it cos is increasing and −sin is decreasing. With 157/50<π<22/7,
\[
 \cos5=\sin(5-3\pi/2)>\frac27-\frac1{48}=\frac{89}{336}>\frac14,
\]
\[
 -\sin6=\sin(2\pi-6)>\frac7{25}-\frac4{1029}>\frac14.
\]
Here sin z≥z−z³/6 for 0≤z≤1/2; the first argument is between 2/7 and 1/2 and the second between 7/25 and 2/7. The elementary π bounds may themselves be checked by the alternating arctangent series and π/4=arctan(1/2)+arctan(1/3): use terms k=0,…,3 for a lower bound and k=0,…,4 for an upper bound in Σ(−1)^k z^(2k+1)/(2k+1).

The derivative A′=24561u²/2−6−5u⁴/4 is positive on J: replace u² by (5/64)² and u⁴ by (3/32)⁴ for a strictly positive rational lower bound. Consequently
\[
 A(u)\ge A(5/64)=\frac{6370218955}{4294967296}>\frac75,
 \qquad B(u)\ge384(5/64)^2=\frac{75}{32}>\frac{23}{10}.
\]
Thus Q>37/40 and e^(u²/4)Q>37/40 throughout J.

For the primitive lower bound, the positive n=1 term gives
\[
 \psi(u)\ge e^{u-\pi e^{4u}}>1/100.
\]
Indeed the Taylor remainder bound after the linear term gives
\[
 e^{3/8}<1+\frac38+\frac{(3/8)^2}{2(1-(3/8)/3)}=\frac{163}{112},
\]
and hence
\[
 \pi e^{4u}-u<\frac{22}{7}\frac{163}{112}-\frac5{64}
       =\frac{14099}{3136}<\frac92.
\]
Also
\[
 e<1+1+\frac12+\frac16+\frac{1/24}{1-1/5}=\frac{87}{32}<\frac{11}{4}<\frac{25}{9},
\]
so e^(9/2)<(11/4)^4(5/3)=73205/768<100. All these estimates are elementary rational comparisons after bounding the positive Taylor tails.

It follows, with every omitted contribution nonnegative, that
\[
 J_I=\int_I e^{u+u^2/4-\pi e^{4u}}|Q(u)|du
 >\frac1{64}\frac1{100}\frac{37}{40}=\frac{37}{256000}. \tag{1}
\]
This lower bound needs no quadrature, no primitive upper-tail bound and no primitive-mode truncation hypothesis.

**Saved-input checks required at assessment.** Check both saved precision stages, using binary complete h1 and reconstructed accepted M_G^IBP, that
\[
 |h_1|>4.18\,10^{-10},\qquad M_G^{\rm IBP}<2.17\,10^{-16}. \tag{2}
\]
Then, since R/8=1/256, the general cost theorem gives
\[
 A_U,A_\infty>\frac{7733}{32768000000000000000}
 =2.35992431640625\,10^{-16}>2.17\,10^{-16}>M_G^{\rm IBP}. \tag{3}
\]
Equation (3) is a cost obstruction for every fixed U≥1 and the full primitive payment at the specified center and outer radius. It is not a lower bound on |G|. The exclusions and unchanged matched consumer are exactly those of the parent proof. Acceptance of (2) remains separate from the elementary derivation (1); neither a rounded display nor this note alone is its verification record.

The E01 panel computation measures a stronger lower-cost gap within its already frozen cases. The rational witness makes the basic obstruction independent of that new panel calculation once the previously accepted full-source endpoints in (2) are verified. No manuscript or milestone promotion follows.

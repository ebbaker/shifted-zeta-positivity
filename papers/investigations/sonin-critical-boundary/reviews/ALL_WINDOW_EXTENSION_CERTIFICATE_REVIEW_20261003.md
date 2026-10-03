# Two-prime extension certificate review

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort are not exposed and are not inferred. This is a separate-agent same-model implementation and analytic audit, not independent specialist refereeing.

Status: passed the analytic and implementation audit and the separate-agent 256-bit replay. No blocking issue remains in the reviewed bounded certificate. The immutable first-window certificate was separately replayed once at 192 bits; see [baseline replay](../numerics/all_window_extension_20261003/baseline_replay.json).

## Scope and arithmetic reduction

Reviewed [certify_extension.py](../numerics/all_window_extension_20261003/certify_extension.py). The experiment is explicitly bounded to L<=6/5, T<=200, even rank<=192, nodes<=80000, and 96<=precision<=384. Its intended next anchor is L=6/5, with the original three source moments, both parity sectors, and complex sources.

The code enumerates every prime power below exp(L), tests its logarithmic threshold with Arb, and raises if a threshold cannot be resolved. In the allowed length range this captures 2 and 3 when active; 4 remains inactive. The recorded fixed Sonin representation is {2,3}, including on smaller windows. The coefficient of cos(t log(p^m)) is 2 log(p)/sqrt(p^m), with no erroneous extra exponent factor.

The check gamma(T)>lambda+sum amplitudes, combined with monotonicity of gamma on t>=0, proves q_L(t)>=lambda outside the band. For signed weight w=lambda-q_L on [0,T], the resulting full source operator satisfies

    Q[F]>=lambda||F||²-<F,D F>.

Positivity of D is unnecessary. The code consistently retains signed weights in matrix accumulation and uses absolute weights only in norm error bounds. The separate capped mode integrates the positive part and uses its applicable first-derivative error estimate; the signed second-derivative estimate is not incorrectly applied at positive-part corners.

## Dilation and full moment projection

Under the unitary change f(y)=sqrt(L)F(Ly), y in (-1/2,1/2), the phase is k y with k=Lt and the operator integral has prefactor L/pi. The code includes both changes. Put beta=L/2, z=L/4. The normalized constraint functions use

    mean=sinh(z)/z,
    ns=sinh(beta)/L-1/2,
    nc=sinh(beta)/L+1/2-mean².

These are precisely the mean of cosh(beta y), the squared norm of sinh(beta y), and the squared norm of cosh(beta y)-mean. The code's Legendre coefficients, 0F1 arguments, alternating parity signs, and analytic sine/cosine moment transforms agree with direct integration. The projection removes the full analytic moments before truncation. It does not substitute a finite approximate constraint Gram matrix. The degree-zero projected coordinate vanishes identically.

The odd plane-wave coordinates have one common factor i. It cancels within the Hermitian odd block; mixed even/odd terms cancel between t and -t. The resulting real symmetric parity blocks therefore bound the complex source form as well.

## Signed midpoint error

Writing v_t=P_E exp(iLt y) and R_t=Re|v_t><v_t| gives

    ||v_t||<=1,
    ||v_t'||<=L/sqrt(12),
    ||v_t''||<=L²/sqrt(80),
    ||R_t'||<=L/sqrt(3),
    ||R_t''||<=L²(1/sqrt(20)+1/6).

The last line follows from the two second-derivative outer products and twice the first-derivative outer product. With V1 bounding integral |w'| and W bounding integral |w|, the code consequently bounds integral ||(wR)''|| by

    V2+(2L/sqrt(3))V1+L²(1/sqrt(20)+1/6)W.

The digamma series has summands 2t²/[b(b²+t²)], b=2n+1/2. Each first derivative is nonnegative, vanishes at both endpoints of the positive half-line, and has maximum 3sqrt(3)/(4b²). Therefore

    integral_0^infinity |gamma''(t)|dt
      <=(3sqrt(3)/2) sum_n b^(-2)
      <=15sqrt(3)/2,

using sum_n(2n+1/2)^(-2)<=4+integral_0^infinity(2x+1/2)^(-2)dx=5. Absolute summability justifies differentiating and summing in this bound. Adding T sum c a² gives the code's V2. Monotonicity of gamma gives V1=gamma(T)-gamma(0)+T sum c a.

The midpoint Peano kernel on a cell has supremum h²/8. Thus the Banach-valued midpoint error is at most h²/8 times the integrated second-derivative norm. Multiplication by L/pi yields exactly the implemented signed quadrature bound. The absolute scalar mass bound W<=h sum |w(t_i)|+h V1/2 is valid because absolute value does not increase total variation.

## Every omitted source mode

The tail ratio zeta²/[(2M+1)(2M+3)] and double factorial in plane_tail are correct. Here the maximal real plane argument is LT/2, while the exponential-moment argument is L/4. The projected tail includes both complete normalized moment-vector tails with the e^(L/4) bound. Rank is the total number of Legendre coordinates, split equally between parities.

For the exact projected plane wave and its Legendre compression, both norms are at most one. Their rank-one operator difference has norm at most twice the projected tail. Multiplication by the absolute signed weight mass gives the implemented 2L tail W/pi remainder. The certificate can truncate the exact integral first and then apply the midpoint error to its compression; this justifies combining its integral mass bound with the finite midpoint matrix.

The LDL routine tests positivity of cap I-D_M with outward arithmetic. Its lower pivots must be strictly positive. Because cap>=0 is explicitly required, the finite-dimensional inequality extends to D_M on the full Hilbert space, with zero on the orthogonal complement, even though D_M is signed. Adding quadrature and source-tail errors proves D<=(cap+error)I without assuming D is positive.

## Independent correction bound and limitations

The transported boundary gap is recalculated as

    g=(57/1000000) product_{p=2,3} ((1-p^(-1/2))/(1+p^(-1/2)))².

The correction bound L sqrt((1-g)/g) includes the source nuclear factor L. The generator validates the inherited record's success status, exact archimedean gap, and current prolate generator hash; it records the inherited record hash. This is reuse of the previously certified prolate input, not a fresh prolate reconstruction. The earlier single replay also checked that baseline input binding.

Given delta=lambda-cap-errorcap>0 and |K|<=kappa||F||², the identity Q=B-K gives B<=Q+kappa||F||²<=(1+kappa/delta)Q. Thus the recorded comparison fraction delta/(kappa+delta) is correct. No multiple-prime compactness theorem is needed for this norm argument.

The numerical proof establishes one bounded support anchor and covers its smaller supports by inclusion. It does not prove an unbounded sequence of anchors, a uniform positive gap, monotonicity of B or K under place insertion, or unweighted B>=K_plus. The absolute-amplitude frequency cutoff remains a structural cost barrier. No manuscript revision or baseline package alteration was made by this review.


## Completed replay and numerical margins

The final reviewed generator SHA-256 is

    6334c0a3cbda39458e30c4abf1a339b5a642424b421a034b83f9615eabfca4c2

The production [192-bit certificate](../numerics/all_window_extension_20261003/certificate_192.json) and separate-agent [256-bit certificate](../numerics/all_window_extension_20261003/certificate_256.json) bind this exact source. The latter passed in 47.53 seconds with Python 3.10.0, python-flint 0.9.0, and FLINT 3.6.0. The final source includes the exact integer conversion `int(Arb.ceil().fmpq())` for the prime-enumeration ceiling; this avoids the unsupported direct Arb-to-int conversion seen during implementation without changing the enumerated bound.

Both runs use L=6/5, lambda=1/2, T=100, M=100, n=30000, signed weights, matrix cap 249/500, and error budget 1/2000. All 30,000 midpoint nodes are included. The source-space gap is therefore

    Q[F]>=(3/2000)||F||².

The outward 256-bit endpoints in the certificate establish these convenient rounded bounds:

- cutoff margin gamma(100)-1/2-C_L > 0.01846260;
- quadrature error < 0.000320671;
- full-source truncation error < 0.000000009124;
- total error < 0.000320680 < 1/2000;
- the even and odd LDL minimum-pivot lower bounds exceed 0.38361079 and 0.06369404, respectively;
- |K[F]| <= 3458||F||², since the evaluated bound is below 3457.345.

The gap and correction cap yield

    Q[F]>=(3/6916003)B_{ {2,3} }[F].

The [replay check](../numerics/all_window_extension_20261003/replay_check.json) records certificate hashes, source binding, overlap of all thirteen scalar ball enclosures, invariant parameter agreement, strict caps, and five fail-closed argument checks. Different matrix hashes at the two precisions are expected; the arithmetic decides the proof. Stored minimum-pivot quantities are lower endpoints, so their mutual overlap is not required. Odd rank, zero nodes, insufficient precision, length above the resource envelope, and a negative matrix cap all fail before output creation.

The source, inherited record, and inherited prolate generator hashes were checked against the fields recorded in both extension certificates. The correction comparison still depends on the established inherited archimedean proof. The review does not replace that proof or broaden this finite anchor into an all-window theorem.

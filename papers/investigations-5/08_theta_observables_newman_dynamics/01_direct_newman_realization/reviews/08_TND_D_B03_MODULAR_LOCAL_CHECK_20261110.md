# B03 simultaneous-inversion local check

10 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance, direct chat0008. Actual model and effort are
unavailable in registered metadata. **Same-assistant, proof-author local
checking**, not a separate E10 assessment or specialist review.

The checked result is [Note11](../notes/11_TND_D_B03_SIMULTANEOUS_MODULAR_COMPARISON_20261110.md).
The single local check covers the selected Poisson-inversion candidate,
its tail comparison, the complete error terms and the resulting scope.

| Item | Check and disposition |
| --- | --- |
| Transformation | DLMF 20.7.32 at z=0, tau=ir² gives Theta(r)=Theta(1/r)/r. With x=e^(-2p), psi(p)dp=J(x)x^(-3/2)dx/4 after reversing limits. Bulk 1/1024 and face 1/256 are correct. |
| Test and domain | Squaring the sign-reversed Euler derivative gives the stated pulled-back operator. Q retains all six terms for each of the two separated products. The a,b wedge is unchanged; no product-domain integral is substituted. |
| Boundary and convergence | J(x)=2A(1/x) gives the complete flat endpoint remainder. The four expanded lattice/axis terms are not individually integrated. The original curvature face remains -H''/16. The true full pairing is absolutely convergent. |
| Error signs | A-C_M=r^(-1)R_M(1/r)>0, while C_M itself can be negative. The exact product error is AF+BE-EF; a universal triangle bound needs the extra EF payment. If both retained factors are nonnegative it can be omitted. No monotonicity of arbitrary signed retained products is assumed. |
| Matched comparison | For each n>=1, r^(-1) exp(pi n²(r²-r^(-2)))>=1 follows from 2sinh(2log r)>=4log r. Both actual tails and their geometric envelopes are ordered. The stated compact bulk/face envelopes share exactly Q, G, source upper bounds, cutoffs and exterior payment. This does not order signed values or optimal methods. |
| Full-domain fixed cutoff | Finite dual sum expansion gives -e^u/2 plus decaying exponentials. At beta>=1/32, the face derivative has leading 2beta²u⁴ exp(beta u²) cos(Xu). Fixed-width cosine subintervals prove absolute divergence. This excludes only substitution in the separately absolutely convergent formula. |
| Relative-cutoff bound | The first omitted dual term and the upper bound on A give (M+1)²>=r⁴-(r²/pi)log(eta C0 r). The stated asymptotic is for fixed eta. M=ceil(r²) suffices for the coarse 1% bound; direct M=1 suffices for 0.1%. Neither is a lower bound for arbitrary signed integration. |
| Collision control | Rechecked manuscript Section 7: H*_(1/4)=cF(k)(1+cos4k), curvature 16cF(pi/4)>0, with F(k)>=M0(1-k²/4). The control is inside the event box, shares the normalized primitive transfer, and has negative resolving A0 by its own complete moment error. It lacks the literal theta sum. Variable-kernel controls can retain the theta sum but fail the cosine/Newman test. |
| Evidence and gate | Full Note09 E1 is retained, without a curvature floor. No favorable signed remainder, collision exclusion, cost measurement or E09 contract is asserted. The other control families retain their source domain and certificate qualifications. |

The [replay script](../numerics/b03_modular_check.py) and
[record03](../numerics/03_TND_D_B03_MODULAR_CHECK_20261110.json) check the
coefficients, mixed product sign, beta minimum and coarse constants with
exact rational arithmetic. Three fixed radii (1,2,4), at 80 decimal digits,
check the numerical cancellation and finite-tail identities. The Python
standard library was used because optional mpmath/sympy packages were not
available; this changes no scientific scope or precision target.

For example, at r=4,M=4 the retained dual factor is negative and the
floating relative primitive error is about 1.4035e19; at M=16 it is about
3.8403e-4. These are diagnostics, not interval certificates or estimates
of A0. The universal conclusions rest on the written inequalities, not
these samples. No numerical campaign or additional parameter search ran.

**Disposition: no mathematical correction required by this local pass.**
The checked scope is the exact modular formula and the named tail-envelope
comparison. The remaining joint signed estimate is open. This local check
does not promote the work beyond proof-author status or close the branch.

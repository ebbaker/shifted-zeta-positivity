# Prime-variance exponents: fixed exponent \(\iff\) closed zero strip

15 October 2026. Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork.

Arithmetic correction, 16 October 2026, prepared for Edward Baker with
substantial LLM assistance: **gpt-6-astra (Codex)**, effort **ultra**.

## Summary

- **Fixed exponent and closed zero strip (thm:main, cor:rh).** For each
  fixed \(\delta\in[0,1]\), the prepared-prime variance
  \(V_g(X)=\int_X^{2X}\bigl|\sum\Lambda(n)w(n/x)\bigr|^2dx\) satisfies
  \(V_g(X)=O(X^{2+\delta})\) if and only if every nontrivial zero has
  \(|\operatorname{Re}\rho-\tfrac12|\le\delta/2\). \(\delta=1\) is
  unconditional; any sequence \(\delta_j\to0\) is equivalent to RH; the
  optimum \(\delta^*\) is attained as a bound, not as a zero (rule R4 of the
  11 October brainstorm). The bridge \(\Lambda_{\rm DN}\le\delta^{*2}/2\)
  converts a strip into a Newman bound. A half-plane bound
  \(\operatorname{Re}\rho\le7/8\) gives \(\delta=3/4\) and \(9/32\),
  worse than the published bounds. This corrects the earlier parameter
  identification: \(\delta^*=7/8\) would instead give \(49/128\).
- **Finite quadratic bounds (thm:finite, cor:height).** \(V_g(X)<38X^2\)
  for \(e\le X\le10^{99}\), \(<40X^2\) to \(10^{100}\), \(<72X^2\) to
  \(10^{102}\); the covered range grows like \(H^{10}/(\log H)^2\) in the
  verified height \(H\).
- **Short-interval transfer (prop:short, cor:gate).**
  \(V_g\le3X^2S(X,h)/h^2+C^2h^4/X\); at \(h=X^{3/4}\) the signed covariance
  \(Q_h\) has exactly the admissible exponents of \(V_g\); the PNT and
  Saffari–Vaughan inputs give only subpower savings.
- **Obstructions to descent.** Finite-prefix model sequences keep any
  prefix of \(\Lambda\), satisfy the PNT and the same diagonal, and still
  have variance \(\asymp X^{2+\delta}\); the semiprime sector has energy
  \(\asymp X^3/(\log X)^2\), which defeats termwise power bounds; a uniform
  Type II hypothesis already implies a stronger strip. The fixed-scale
  recurrence \(E(X)\le qE(X/b)+CX^{-\eta}\) does force descent, but the
  arithmetic contraction is open and little-\(o\) at the edge is equivalent
  to having no boundary zero.
- **Orthogonality floor.** For prime \(q\) and \(N<q\),
  \(\sum_{\chi\ne\chi_0}|\sum\mu(n)w(n)\chi(n)|^2\ge(q-1-N)\sum|a_n|^2\), so
  a universal \(Q^{1+h-c}\) saving over full families is false.

## Status

"Proved for each delta in [0,1]" (README); the core-proof review found "no
gap"; certificates are "continuous finite certificates using the
identified outward inputs", with the outward zero records imported, not
regenerated. The 11 October brainstorm recommends writing the equivalence
up on its own.

## Caveats

The equivalence converts energy bounds into strips; it does not supply a
saving. The finite-prefix obstruction is "for constructed coefficients, not
a counterexample involving actual primes".

## Reusable for

Translating any proposed saving \(\kappa\) into an exponent \(\delta\) and a
strip; a clean, self-contained statement that could be published without
the rest of the program; the orthogonality floor as a sanity check on
family-saving proposals.

## Where

- [Manuscript](../papers/quasi-rh/prime-variance-exponents/manuscript.tex) (thm:main, cor:rh, thm:finite, cor:height, prop:short, cor:gate, prop:model); [README](../papers/quasi-rh/prime-variance-exponents/README.md); [verification status](../papers/quasi-rh/prime-variance-exponents/VERIFICATION_STATUS.md).
- Reviews: [core proof](../papers/quasi-rh/prime-variance-exponents/reviews/CORE_PROOF_REVIEW_20261003.md), [certificate replay](../papers/quasi-rh/prime-variance-exponents/reviews/CERTIFICATE_REPLAY_20261003.md).
- Notes: [quasi-RH to Newman bridge](../papers/quasi-rh/prime-variance-exponents/notes/QUASI_RH_NEWMAN_BRIDGE_20261008.md), [arithmetic overlap (semiprime sector)](../papers/quasi-rh/prime-variance-exponents/notes/programs/01_signed_arithmetic_covariance/ARITHMETIC_OVERLAP_20261004.md), [manuscript continuation](../papers/quasi-rh/prime-variance-exponents/notes/MANUSCRIPT_CONTINUATION_20261003.md).
- Fixed-scale descent: [criterion](../papers/quasi-rh/quasi-rh-exponent-descent/fixed_scale_descent/notes/1_FIXED_SCALE_DESCENT_CRITERION_20261008.md); orthogonality floor: [Codex brainstorm](../papers/quasi-rh/quasi-rh-exponent-descent/brainstorm/NEW_PATHS_FORWARD_BRAINSTORM_CODEX_20261011.md) §3.

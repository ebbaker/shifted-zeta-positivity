# Version 0.2 status — 10 September 2026

The first quarter-step now has both induction premises: the original
full-old residual factor theta=0.9 and the new full-old comparison
H_J >= 1e-7 A. Hence its unrestricted Schur complement retains at least
1e-8 of the old energy.

At the second quarter-step, L2=log(56)/2, a three-interval construction
retains the first 288 spatial modes and adds 32 new modes. Its new rational
continuation satisfies H_J >= 1e-8 A on the entire old form domain.
This comparison passes at 2048 and 4096 bits.

The second-step residual premise remains unproved. The scalar-tail tests
at theta=0.9, 0.95, and 0.99 fail their sufficient criteria. Twenty
interval-specific weight proposals at theta=0.99 and 0.9999 also fail.
A fixed near-one case is reproduced at 2048 bits. The requested absolute
floor 1e-36 is not certified. None of these failures is a negative-form
witness, and the weight search is not exhaustive.

No new full-operator horizon or shift interval is claimed at L2.
The largest all-input horizon in the package remains the separate global
certificate at 1.98, with its inherited shift interval through 5e-17.
The first spatial step reaches 3 log(14)/4 and has its own floor 1e-33
and shift interval through 5e-18.

The manuscript states a conditional induction with explicit coercivity and
shift recurrences. Only the first step has all its premises certified.
Indefinite residual control, prevention of finite-depth accumulation, the
normalization audit, and independent mathematical review remain open.

## Next experiment

1. Enlarge verification spaces on the short slabs, using the saved output
   Grams for unchanged blocks. The current driver fixes the original
   256-plus-32 seed and profile degree 320; a broader verification-space
   driver is needed to enlarge the first short slab as well.
2. Improve the joint tail estimate. The saved separate output Grams already
   permit interval-specific Schur bounds; the recorded attempts show their
   current limitations. Do not infer a mathematical obstruction from an
   LDL pivot location.
3. Implement local gamma profiles and separated-interval exponential
   expansions, with exact exponential modes in the head. This removes the
   present global L<3 representation restriction; it does not by itself
   establish the induction inequalities.
4. Establish stepwise estimates that guarantee divergent total depth while
   the shift tends to zero. Preserve the full continuation energy and
   leakage information rather than only a smallest-energy scalar.

All 297,151,691 bytes of the new compressed matrix archive are outside Git.
ARCHIVES.md gives the layout, dual hashes, source-only reconstruction path,
and fail-closed replay commands. Current source-package files are below
1 MiB. Version 0.1 and its original records remain unchanged.

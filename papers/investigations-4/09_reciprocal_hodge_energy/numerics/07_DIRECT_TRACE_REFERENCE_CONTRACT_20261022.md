# Fixed direct reference for the canonical signed physical trace

22 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance; actual recorded gpt-6.1-sol (Codex), effort ultra.

Before quadrature, fix t=0, C=35, L=h=4sqrt(2), I=[C-L,C+L], psi(x)=(1-((x-C)/L)^2)^3, and
T=integral_I psi(x) [H'(x)^2-H(x)H''(x)]/sqrt(H(x)^2+H'(x)^2) dx.

Use unchanged canonical xi/8 degree64 ActualThetaCore oracle on radius8, outer radius16, 192-bit outward Arb balls. Exactly 1024 equal rational cells in s=(x-C)/L on [-1,1], one run, no refinement or search. For each H/H'/H'' polynomial range use centered quadratic Taylor at the cell midpoint plus a full third-derivative polynomial remainder bounded on radius8; add the complete source derivative tails separately. Retain all coefficient balls. Each E lower is acquired from its complete cell range, without RH, root assumptions, preassigned floor, or skipped cells. Integrate the nonnegative polynomial psi over each rational cell exactly and multiply by the complete physical trace range. Any unresolved positivity/finiteness fails closed and the run stops.

Purpose: one independent complete direct trace reference for the same fixed signed-potential consumer, with reported interval width and paid floor. No adaptive accuracy target, sign search, period method ordering, or exclusion claim. A finite sign, if enclosed, describes only this window. Report setup and consumer time, source tails, polynomial remainders, floor, range, and input hashes. The equally informed direct method may reuse every identity and bulk observation.

The failed default-interpreter import probe performed no quadrature; the successful run uses the existing /private/tmp/jsd-20261021-venv/bin/python runtime. No install or shared repository write is allowed. Replay with explicit --contract and --output paths; save the small receipt at the chosen output path. The staging run uses /private/tmp/07_DIRECT_TRACE_REFERENCE_20261022.json.

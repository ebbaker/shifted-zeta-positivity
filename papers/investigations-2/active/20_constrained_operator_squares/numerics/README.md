# Operator square seed checks

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: gpt-6-astra (Codex), reasoning effort **ultra**.

Run the standard-library exact-arithmetic checker from this folder:

    python3 -B check_seed_identities.py --output /tmp/operator-square-checks.json

It checks the finite-time residual energy and norm identities on a
nontrivial rational polynomial path, the three-atom stationary collision
and paired-operator normalization, and the failure of the proposed
cosine-to-heat identification already at low Taylor orders.
The [retained record](SEED_IDENTITY_CHECKS_20261014.json) binds the checker
by SHA-256. These are elementary consistency checks, not independent
review, outward theta arithmetic, or a many-body benchmark.

Source PDFs remain at the author-supplied locations. Their provenance and
hashes are in the project's [source manifest](../SOURCE_DOCUMENTS.json).
Large derived arrays should follow the repository's external-archive
policy when first needed.

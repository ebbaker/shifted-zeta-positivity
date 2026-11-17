# Decision07 rendering correction

16 November 2026, America/New_York. Prepared for Edward Baker with OpenAI
Codex assistance; lead recorded settings unavailable, internal assessment
support explicitly Sol6.1/ultra. The E05 r8 prerequisite audit identified
rendering errors in the issued Decision07, not a mathematical change.

- Original issued SHA-256: `f20c91a87c5b972cb45b3f7e26dc4a55d5e64499c808d220117b645d7aeaa392`.
- Corrected SHA-256: `51f393fb86bce0a279bd7d7faae273bbef0ccba99401b8f46fede06de1b34931`.
- In the exterior-sum label, replaced the single carriage-return byte
  followed by `m exterior` with the literal TeX command `\rm exterior`.
- In the coordinate definition, replaced literal `,quad y` with `,\quad y`.

Only these two byte replacements were made. Their inverse reconstructs the
original SHA-256 exactly. E03 r5 and E04 r3 requests keep their original
issued input hashes; this receipt explains the exception for Decision07.
All sources, domains, inequalities, caps, outputs and mathematical contracts
are unchanged. The final E05 r8 packet pins the corrected decision.

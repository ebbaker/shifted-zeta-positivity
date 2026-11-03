"""Build a disposable print bibliography from the canonical shared catalog.

Research inspection notes stay in the catalog and manuscript evidence record;
the printed bibliography retains citation metadata, DOI, eprint, and URL.
The output belongs beside the ignored PDF, never in the research source tree.
"""
from pathlib import Path
import re
import sys


def omit_note_fields(text):
    pattern = re.compile(r"\bnote\s*=\s*\{", re.IGNORECASE)
    while match := pattern.search(text):
        depth, pos = 1, match.end()
        while depth and pos < len(text):
            if text[pos] == "\\":
                pos += 2
                continue
            if text[pos] == "{":
                depth += 1
            elif text[pos] == "}":
                depth -= 1
            pos += 1
        if depth:
            raise ValueError("Unbalanced note field in shared bibliography")
        while pos < len(text) and text[pos] in " \t":
            pos += 1
        if pos < len(text) and text[pos] == ",":
            pos += 1
        text = text[:match.start()] + text[pos:]
    # Preserve capitalization of complete titles in the print style. All title
    # values in this shared catalog are braced; nested TeX braces are retained.
    starts = list(re.finditer(r"\btitle\s*=\s*\{", text, re.IGNORECASE))
    for match in reversed(starts):
        depth, pos = 1, match.end()
        while depth and pos < len(text):
            if text[pos] == "\\":
                pos += 2
                continue
            depth += (text[pos] == "{") - (text[pos] == "}")
            pos += 1
        if depth:
            raise ValueError("Unbalanced title field in shared bibliography")
        text = text[:match.end()] + "{" + text[match.end():pos - 1] + "}" + text[pos - 1:]
    return text


if __name__ == "__main__":
    paper = Path(__file__).resolve().parent
    catalog = (paper / "../../../references/sources.bib").resolve()
    output = Path(sys.argv[1]).resolve() / "manuscript_references.bib"
    output.write_text(omit_note_fields(catalog.read_text(encoding="utf-8")),
                      encoding="utf-8")

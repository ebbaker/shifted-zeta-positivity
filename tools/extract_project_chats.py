#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Extract complete ChatGPT conversations, with a separate diagnostic report.

Select by --project-id (the observed conversation_template_id export field),
--titles-file (one sidebar title per line), or both. Selection uses OR: every
chat in a requested group and every exact normalized title match is included.
Use --inventory-only to inspect all exported titles and grouping identifiers.
No fuzzy suggestions are automatically selected. Requires only Python's stdlib.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from difflib import get_close_matches
import json
import os
from pathlib import Path
import sys
import unicodedata


PUNCTUATION = str.maketrans({
    "\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"',
    "\u2010": "-", "\u2011": "-", "\u2012": "-", "\u2013": "-",
    "\u2014": "-", "\u2212": "-",
})


def normalize_title(title):
    title = unicodedata.normalize("NFKC", title).translate(PUNCTUATION)
    title = "".join(c for c in title if unicodedata.category(c) != "Cf")
    return " ".join(title.casefold().split())


def conversation_id(chat):
    return chat.get("conversation_id") or chat.get("id")


def conversation_list(data):
    """Accept arrays, a single chat, and common wrapped export arrays."""
    if isinstance(data, dict):
        if isinstance(data.get("mapping"), dict):
            data = [data]
        else:
            for key in ("conversations", "items", "data"):
                if isinstance(data.get(key), list):
                    data = data[key]
                    break
    if not isinstance(data, list):
        raise ValueError("Expected a conversation array or a supported wrapper")
    for position, chat in enumerate(data):
        if not isinstance(chat, dict) or not isinstance(chat.get("mapping"), dict):
            raise ValueError(f"Record {position}: expected a chat with a mapping tree")
        chat_id = conversation_id(chat)
        if not isinstance(chat_id, str) or not chat_id:
            raise ValueError(f"Record {position}: missing conversation_id/id")
        if chat.get("conversation_id") and chat.get("id"):
            if chat["conversation_id"] != chat["id"]:
                raise ValueError(f"Record {position}: conversation_id and id disagree")
        if chat.get("title") is not None and not isinstance(chat["title"], str):
            raise ValueError(f"Record {position}: title is not a string")
        if chat.get("conversation_template_id") is not None:
            if not isinstance(chat["conversation_template_id"], str):
                raise ValueError(f"Record {position}: grouping identifier is not a string")
    return data


def export_files(folder):
    """os.walk's error callback prevents inaccessible folders being skipped."""
    if not folder.is_dir():
        raise ValueError(f"Export directory does not exist: {folder}")

    def fail(error):
        raise error

    found = []
    for directory, subdirs, filenames in os.walk(folder, onerror=fail):
        subdirs.sort()
        for filename in sorted(filenames):
            name = filename.casefold()
            if name.startswith("conversations") and name.endswith(".json"):
                found.append(Path(directory) / filename)
    if not found:
        raise ValueError(f"No conversations*.json export chunks found under {folder}")
    return found


def write_json(path, data, overwrite):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w" if overwrite else "x", encoding="utf-8") as output:
        json.dump(data, output, ensure_ascii=False, indent=2)
        output.write("\n")


def same_location(left, right):
    return (left.resolve() == right.resolve() or
            (left.exists() and right.exists() and left.samefile(right)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--project-id", action="append", default=[],
                        help="Exact conversation_template_id; repeat for several groups")
    parser.add_argument("--titles-file", type=Path,
                        help="UTF-8 text file with one requested title per line")
    parser.add_argument("--inventory-only", action="store_true",
                        help="Write the report only, without selecting conversations")
    parser.add_argument("--overwrite", action="store_true",
                        help="Explicitly allow replacing output/report from a prior run")
    args = parser.parse_args()
    folder = args.input_dir.expanduser().resolve()
    output = args.output.expanduser().resolve()
    report_path = output.with_name(output.stem + "_report.json")
    if same_location(output, report_path):
        parser.error("Conversation output and diagnostic report must be separate files")
    if args.titles_file:
        title_path = args.titles_file.expanduser()
        if any(same_location(title_path, path) for path in (output, report_path)):
            parser.error("Output/report must not overwrite the input titles file")
    if not args.overwrite and (output.exists() or report_path.exists()):
        parser.error("Output/report already exists; choose a new name or use --overwrite")
    try:
        requested_titles = []
        if args.titles_file:
            requested_titles = [line.strip() for line in
                                args.titles_file.expanduser().read_text(encoding="utf-8-sig").splitlines()
                                if line.strip()]
    except (OSError, UnicodeError) as error:
        parser.error(f"Cannot read titles file: {error}")
    targets = {normalize_title(title): title for title in requested_titles}
    project_ids = {value.strip() for value in args.project_id if value.strip()}
    if not args.inventory_only and not (targets or project_ids):
        parser.error("Supply --project-id, --titles-file, or --inventory-only")

    report = {
        "input_directory": str(folder),
        "requested_project_ids": sorted(project_ids),
        "requested_titles": requested_titles,
        "files": [], "errors": [], "conflicting_conversation_ids": [],
    }
    chats = {}
    sources = defaultdict(list)
    exact_duplicates = 0
    try:
        paths = export_files(folder)
    except (OSError, ValueError) as error:
        paths = []
        report["errors"].append(str(error))
    resolved_inputs = {path.resolve() for path in paths}
    for destination in (output, report_path):
        aliases_input = destination in resolved_inputs
        if destination.exists() and not aliases_input:
            aliases_input = any(destination.samefile(path) for path in paths)
        if aliases_input:
            parser.error("Output/report must not be an original export chunk, "
                         "including a symlink or hardlink to one")

    for path in paths:
        try:
            rows = conversation_list(json.loads(path.read_text(encoding="utf-8-sig")))
        except (OSError, UnicodeError, ValueError) as error:
            report["errors"].append({"file": str(path), "error": str(error)})
            print(f"ERROR reading {path.name}: {error}", file=sys.stderr)
            continue
        report["files"].append({"file": str(path), "conversation_records": len(rows)})
        print(f"Scanned {path.relative_to(folder)}: {len(rows)} records")
        for chat in rows:
            chat_id = conversation_id(chat)
            sources[chat_id].append(str(path))
            if chat_id in chats:
                if chats[chat_id] == chat:
                    exact_duplicates += 1
                else:
                    report["conflicting_conversation_ids"].append(chat_id)
            else:
                chats[chat_id] = chat

    title_ids = defaultdict(list)
    groups = Counter()
    inventory = []
    selected = []
    for chat_id, chat in chats.items():
        title = chat.get("title") or ""
        normalized = normalize_title(title)
        title_ids[normalized].append(chat_id)
        group = chat.get("conversation_template_id")
        groups[group or "(no conversation_template_id)"] += 1
        reasons = []
        if normalized in targets:
            reasons.append("normalized exact title")
        if group and group in project_ids:
            reasons.append("conversation_template_id")
        if reasons and not args.inventory_only:
            selected.append(chat)
        inventory.append({
            "conversation_id": chat_id, "title": title,
            "conversation_template_id": group,
            "source_files": sources[chat_id], "match_reasons": reasons,
        })
    unmatched = []
    for normalized, title in targets.items():
        if normalized in title_ids:
            continue
        suggestions = get_close_matches(normalized, list(title_ids), n=5, cutoff=0.55)
        if normalized.endswith("..."):
            prefix = normalized[:-3].rstrip()
            if prefix:
                suggestions = list(dict.fromkeys(
                    [key for key in title_ids if key.startswith(prefix)] + suggestions))[:5]
        unmatched.append({"requested_title": title, "suggestions": [
            {"conversation_id": chat_id, "title": chats[chat_id].get("title")}
            for key in suggestions for chat_id in title_ids[key]
        ]})
    conflicts = sorted(set(report["conflicting_conversation_ids"]))
    missing_groups = sorted(project_ids - {chat.get("conversation_template_id")
                                          for chat in chats.values()})
    report.update({
        "unique_conversations_scanned": len(chats),
        "exact_duplicate_records_removed": exact_duplicates,
        "conflicting_conversation_ids": conflicts,
        "conversations_by_template_id": dict(sorted(groups.items())),
        "inventory": inventory,
        "unmatched_titles": unmatched,
        "missing_project_ids": missing_groups,
        "selected_conversations": len(selected),
        "output_written": False,
        "completeness_note": "Only chats present in these export chunks can be extracted. "
                             "Unmatched titles may be renamed, truncated, or absent. "
                             "Grouping selection includes every exported record with the requested field value.",
    })
    # Never claim a complete extraction after an unreadable chunk or a conflicting
    # snapshot. A richer/latest duplicate alone may omit alternate message branches.
    blocked = bool(report["errors"] or conflicts)
    if not blocked and selected and not args.inventory_only:
        write_json(output, selected, args.overwrite)
        report["output_written"] = True
    write_json(report_path, report, args.overwrite)
    print(f"\nScanned {len(chats)} unique chats; removed {exact_duplicates} exact duplicates.")
    for group, count in sorted(groups.items()):
        print(f"  {group}: {count} chats")
    print(f"Diagnostic report: {report_path}")
    if blocked:
        print("Extraction stopped: read/schema errors or conflicting conversation versions. "
              "Inspect the report; no conversation output was written.", file=sys.stderr)
        return 2
    if not args.inventory_only:
        if selected:
            print(f"Extracted {len(selected)} complete conversations to {output}")
        else:
            print("No chats matched; inspect the report's inventory.", file=sys.stderr)
            return 1
        if unmatched or missing_groups:
            print(f"Unmatched titles: {len(unmatched)}; missing groups: {len(missing_groups)}. "
                  "Output is available, but requested matches need review.", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, UnicodeError) as error:
        print(f"I/O error: {error}", file=sys.stderr)
        raise SystemExit(2)

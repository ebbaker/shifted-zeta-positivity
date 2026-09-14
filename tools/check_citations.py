#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Edward B. Baker III
"""Validate both CFF files against a supplied official CFF 1.2.0 schema.

The schema is an external input; this script performs no network access.
Run from the repository root: python3 tools/check_citations.py --schema FILE
"""
from __future__ import annotations

import argparse
from datetime import date
import json
from pathlib import Path

import jsonschema
import yaml


def normalize_dates(value):
    """CFF dates are strings; PyYAML also accepts unquoted YAML dates."""
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, dict):
        return {key: normalize_dates(item) for key, item in value.items()}
    if isinstance(value, list):
        return [normalize_dates(item) for item in value]
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--schema", type=Path, required=True)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    schema = json.loads(args.schema.read_text())
    jsonschema.Draft7Validator.check_schema(schema)
    validator = jsonschema.Draft7Validator(schema, format_checker=jsonschema.FormatChecker())
    failed = False
    for relative in ("CITATION.cff", "papers/shifted-zeta/first-slab-positivity/CITATION.cff"):
        document = normalize_dates(yaml.safe_load((args.repo/relative).read_text()))
        errors = list(validator.iter_errors(document))
        if errors:
            failed = True
            for error in errors:
                location = ".".join(map(str, error.absolute_path)) or "<root>"
                print(f"FAIL {relative}: {location}: {error.message}")
        else:
            print(f"PASS {relative}: CFF 1.2.0 schema")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

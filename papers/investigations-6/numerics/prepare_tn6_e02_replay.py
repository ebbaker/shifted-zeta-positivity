#!/usr/bin/env python3
"""Stage the frozen TN6-E02 r1 replay files and print the new directory.

14 November 2026. Prepared for Edward Baker with OpenAI Codex LLM assistance.
Worker dispatch was gpt-6.1-sol, ultra. Independent backend attestation is
unavailable. This helper checks file identities for replay staging.
"""

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import tempfile


ROOT = Path(__file__).resolve().parents[3]
INVESTIGATION = "papers/investigations-6"
NUMERICS = f"{INVESTIGATION}/numerics"
REQUEST = f"{INVESTIGATION}/research-progress/handoffs/TN6-E02-r1.md"
MANIFEST = f"{NUMERICS}/08_TN6_E02_R1_INPUT_MANIFEST_20261114.json"
GENERATOR = f"{NUMERICS}/execute_tn6_e02_r1.py"
GUIDANCE = "result-summaries/18_tensor_approximation_and_coefficient_bounds.md"
GUIDANCE_RECEIPT = f"{NUMERICS}/12_TN6_POST_ACQUISITION_GUIDANCE_UPDATE_20261114.json"
MANUSCRIPT_GUIDANCE_RECEIPT = f"{NUMERICS}/17_TN6_MANUSCRIPT_GUIDANCE_UPDATE_20261114.json"
FROZEN_FILES = {
    REQUEST: (10449, "3c581245746f1714b08e928191f84cf6f23528fe4eb2ad94ec04483ce56a56c7"),
    MANIFEST: (5230, "48727341987b33e7ebe0f9c3914142d4d653085276ce21479682561e241bc0f2"),
    GENERATOR: (27301, "e5379779b637548ec0dc8a0b52f3b1d563b6ba035228ea1e22636c618e08e70a"),
}


def sha256(contents: bytes) -> str:
    return hashlib.sha256(contents).hexdigest()


def matches(contents: bytes, length: int, digest: str) -> bool:
    return len(contents) == length and sha256(contents) == digest


def read_source(path: str) -> bytes:
    if any(part in ("", ".", "..") for part in path.split("/")) or any(
        separator in path for separator in ("\\", ":")
    ):
        raise ValueError(f"invalid repository-relative source path {path!r}")
    source = (ROOT / path).resolve(strict=True)
    if not source.is_relative_to(ROOT) or not source.is_file():
        raise ValueError(f"source must be a file within the repository: {path}")
    return source.read_bytes()


def read_guidance_receipt(path: str) -> dict:
    try:
        receipt = json.loads(read_source(path))
    except FileNotFoundError as exc:
        raise ValueError(f"changed frozen guidance requires receipt {path}") from exc
    if not isinstance(receipt, dict):
        raise ValueError("guidance receipt must contain a JSON object")
    if receipt.get("path") != GUIDANCE:
        raise ValueError(f"guidance receipt does not identify the source: {path}")
    return receipt


def remove_guidance_append(contents: bytes, receipt: dict) -> bytes:
    if receipt.get("after_sha256") != sha256(contents):
        raise ValueError("live guidance digest does not match its receipt")
    appended_text = receipt.get("exact_appended_text")
    if not isinstance(appended_text, str) or not appended_text:
        raise ValueError("guidance receipt must record the appended text")
    suffix = appended_text.encode("utf-8")
    if len(suffix) >= len(contents) or not contents.endswith(suffix):
        raise ValueError("live guidance does not end with the exact receipt text")
    previous = contents[:-len(suffix)]
    if sha256(previous) != receipt.get("before_sha256"):
        raise ValueError("restored guidance digest does not match its receipt")
    return previous


def restore_frozen_guidance(contents: bytes, frozen_digest: str) -> bytes:
    acquisition = read_guidance_receipt(GUIDANCE_RECEIPT)
    if acquisition.get("before_sha256") != frozen_digest:
        raise ValueError("acquisition guidance receipt does not identify the frozen source")
    if acquisition.get("after_sha256") != sha256(contents):
        manuscript = read_guidance_receipt(MANUSCRIPT_GUIDANCE_RECEIPT)
        if manuscript.get("before_sha256") != acquisition.get("after_sha256"):
            raise ValueError("guidance receipts disagree on the intermediate digest")
        contents = remove_guidance_append(contents, manuscript)
    return remove_guidance_append(contents, acquisition)


def load_frozen_inputs() -> dict[str, bytes]:
    verified = {}
    for path, (length, digest) in FROZEN_FILES.items():
        contents = read_source(path)
        if not matches(contents, length, digest):
            raise ValueError(f"frozen file identity mismatch: {path}")
        verified[path] = contents

    inputs = json.loads(verified[MANIFEST])["inputs"]
    if len(inputs) != 22:
        raise ValueError("expected 22 frozen manifest sources")
    for entry in inputs:
        path, length, digest = entry["path"], entry["bytes"], entry["sha256"]
        if path in verified:
            raise ValueError(f"duplicate frozen source: {path}")
        contents = read_source(path)
        if path == GUIDANCE and not matches(contents, length, digest):
            contents = restore_frozen_guidance(contents, digest)
        if not matches(contents, length, digest):
            raise ValueError(f"frozen source identity mismatch: {path}")
        verified[path] = contents
    return verified


def prepare_replay(destination: Path | None) -> Path:
    verified = load_frozen_inputs()
    if destination is None:
        stage = Path(tempfile.mkdtemp(prefix="tn6-e02-replay-")).resolve()
    else:
        destination = destination.expanduser()
        stage = destination.parent.resolve(strict=True) / destination.name
        stage.mkdir(mode=0o700)

    try:
        for path, contents in verified.items():
            target = stage / path
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open("xb") as output:
                output.write(contents)

        for path, contents in verified.items():
            staged = (stage / path).read_bytes()
            if staged != contents or sha256(staged) != sha256(contents):
                raise ValueError(f"staged file identity mismatch: {path}")
    except BaseException:
        shutil.rmtree(stage)
        raise
    return stage


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n", 1)[0])
    parser.add_argument(
        "--destination", type=Path,
        help="new directory under an existing parent (default: a new temporary directory)",
    )
    args = parser.parse_args()
    try:
        stage = prepare_replay(args.destination)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    print(stage)


if __name__ == "__main__":
    main()

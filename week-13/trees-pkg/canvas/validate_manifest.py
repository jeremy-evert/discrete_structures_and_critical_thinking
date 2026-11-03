#!/usr/bin/env python3
"""Validate the Week 13 Canvas package without contacting Canvas.

The prompt page is generated from the prompt files in lexical path order.
The documented separator is the exact UTF-8 byte sequence:
``b"\n\n<!-- PROMPT FILE SEPARATOR -->\n\n"``.
Run from the package root with ``python3 canvas/validate_manifest.py``.
Pass ``--write`` to regenerate ``canvas/prompts.md`` before checking it.
"""

from __future__ import annotations

import argparse
import json
import sys
import tempfile
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = ROOT / "canvas" / "manifest.json"
PROMPTS_PAGE = ROOT / "canvas" / "prompts.md"
PROMPT_SEPARATOR = b"\n\n<!-- PROMPT FILE SEPARATOR -->\n\n"
EXPECTED_DECISION_GATE = ROOT.parent / "student" / "decision-gate.md"
FORBIDDEN = ("instructor/", "INSTRUCTOR_GUIDE", "REPORT", "code/", "_notes.pdf")
EXPECTED_PAGE_TITLES = [
    "Week 13 Tuesday: Trees, Search & Decision Structures",
    "Week 13 Tuesday: Activity — Model, Trace & Audit",
    "Week 13 Tuesday: Handout",
    "Week 13 Tuesday: Concept Map",
    "Week 13 Tuesday: Glossary",
    "Week 13 Tuesday: Claude Prompts",
    "Week 13 Thursday: Pair Reasoning — Search Claims Need an Audit",
    "Week 13 Thursday: Decision Gate — A Tree That Earns Its Conclusion",
    "Week 13 Thursday: Recap Outline",
]


class ValidationError(Exception):
    """A package check failed."""


def prompt_paths() -> list[Path]:
    """Return prompt files in the one canonical lexical order."""
    return sorted((ROOT / "prompts").glob("*.md"), key=lambda path: path.name)


def generated_prompt_bytes(paths: list[Path] | None = None) -> bytes:
    """Build the prompt page byte-for-byte from prompt file bytes."""
    chosen = prompt_paths() if paths is None else paths
    return PROMPT_SEPARATOR.join(path.read_bytes() for path in chosen)


def write_prompt_page() -> None:
    """Regenerate the Canvas prompt page using the canonical byte join."""
    PROMPTS_PAGE.write_bytes(generated_prompt_bytes())


def fail(message: str) -> None:
    raise ValidationError(message)


def check_manifest() -> dict:
    try:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"manifest is not valid JSON: {exc}")

    if manifest.get("week") != 13:
        fail("manifest week must be 13")
    if manifest.get("module_id") != 218912:
        fail("manifest module_id must be 218912")
    if "Week 13" not in manifest.get("module_name_contains", ""):
        fail("manifest module_name_contains must contain Week 13")

    pages = manifest.get("pages")
    if not isinstance(pages, list):
        fail("manifest pages must be a list")
    titles = [page.get("title") for page in pages]
    if len(titles) != len(set(titles)):
        fail("page titles must be unique")
    for title in titles:
        if not isinstance(title, str) or not title.startswith(("Week 13 Tuesday:", "Week 13 Thursday:")):
            fail(f"page title has invalid Week 13 prefix: {title!r}")
    if titles != EXPECTED_PAGE_TITLES:
        fail("manifest page titles do not match the approved Week 13 page list")

    for item in pages + manifest.get("files", []) + manifest.get("zips", []):
        for key in ("title", "source", "from_dir", "name"):
            value = item.get(key)
            if isinstance(value, str) and any(token in value for token in FORBIDDEN):
                fail(f"manifest contains forbidden instructor-only path or name: {value}")
    return manifest


def check_paths(manifest: dict) -> None:
    for page in manifest["pages"]:
        source = ROOT / page["source"]
        if not source.is_file():
            fail(f"missing page source: {page['source']}")

    for item in manifest.get("files", []):
        source = ROOT / item["source"]
        if not source.exists():
            if item["source"] == "deck/trees_slides.pdf":
                print("WARNING: deck PDF not built yet: deck/trees_slides.pdf")
                continue
            fail(f"missing file source: {item['source']}")
        if not source.is_file() or source.stat().st_size == 0:
            fail(f"PDF source is present but invalid or empty: {item['source']}")

    for item in manifest.get("zips", []):
        source = ROOT / item["from_dir"]
        if not source.is_dir():
            fail(f"missing ZIP source directory: {item['from_dir']}")


def check_prompt_page() -> None:
    paths = prompt_paths()
    if not paths:
        fail("no prompt files found")
    expected = generated_prompt_bytes(paths)
    if not PROMPTS_PAGE.is_file():
        fail("missing canvas/prompts.md; run with --write")
    if PROMPTS_PAGE.read_bytes() != expected:
        fail("canvas/prompts.md does not match lexical prompt files byte-for-byte")
    print(f"prompt bytes: {len(paths)} files, byte-exact")


def check_decision_gate() -> None:
    packaged = ROOT / "student" / "decision-gate.md"
    if not EXPECTED_DECISION_GATE.is_file():
        fail(f"missing source Decision Gate: {EXPECTED_DECISION_GATE}")
    if packaged.read_bytes() != EXPECTED_DECISION_GATE.read_bytes():
        fail("student/decision-gate.md differs from week-13/student/decision-gate.md")
    print("decision gate: byte-exact copy")


def check_zip(manifest: dict) -> None:
    zip_items = manifest.get("zips", [])
    if len(zip_items) != 1:
        fail("manifest must contain exactly one prompt ZIP")
    item = zip_items[0]
    prompt_dir = ROOT / item["from_dir"]
    paths = prompt_paths()
    with tempfile.TemporaryDirectory(prefix="w13-prompt-zip-") as temp_dir:
        archive = Path(temp_dir) / item["name"]
        with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as bundle:
            for path in paths:
                bundle.write(path, path.relative_to(prompt_dir).as_posix())
        with zipfile.ZipFile(archive) as bundle:
            names = sorted(bundle.namelist())
            expected_names = sorted(path.relative_to(prompt_dir).as_posix() for path in paths)
            if names != expected_names:
                fail(f"prompt ZIP members differ: {names!r}")
            for path in paths:
                name = path.relative_to(prompt_dir).as_posix()
                if bundle.read(name) != path.read_bytes():
                    fail(f"prompt ZIP content differs for {name}")
    print(f"prompt ZIP: {item['name']} built and checked in a temporary directory")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="regenerate canvas/prompts.md before checking")
    args = parser.parse_args(argv)
    try:
        if args.write:
            write_prompt_page()
            print("wrote canvas/prompts.md")
        manifest = check_manifest()
        check_paths(manifest)
        check_prompt_page()
        check_decision_gate()
        check_zip(manifest)
    except ValidationError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print("manifest valid: 9 pages, 1 file entry, 1 prompt ZIP")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

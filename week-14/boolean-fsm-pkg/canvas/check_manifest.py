#!/usr/bin/env python3
"""Validate the Week 14 package manifest without contacting Canvas."""

from __future__ import annotations

import json
import tempfile
import zipfile
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = PACKAGE_ROOT / "canvas" / "manifest.json"
ALLOWED_EXTERNAL_SOURCE = "../student/odyssey-checkpoint-3.md"


def source_path(source: str) -> Path:
    path = (PACKAGE_ROOT / source).resolve()
    package_root = PACKAGE_ROOT.resolve()
    if source == ALLOWED_EXTERNAL_SOURCE:
        expected = (PACKAGE_ROOT.parent / "student" / "odyssey-checkpoint-3.md").resolve()
        if path != expected:
            raise AssertionError(f"allowed Checkpoint source resolved incorrectly: {source}")
        return path
    if package_root not in (path, *path.parents):
        raise AssertionError(f"source escapes package: {source}")
    return path


def check_sources(manifest: dict) -> None:
    for section in ("pages", "files"):
        for item in manifest[section]:
            source = item["source"]
            path = source_path(source)
            if not path.is_file():
                raise AssertionError(f"missing {section} source: {source}")
            if "instructor" in Path(source).parts:
                raise AssertionError(f"instructor source is not publishable: {source}")
            if source == ALLOWED_EXTERNAL_SOURCE:
                print(f"allowed external source: {source}")


def check_pages(manifest: dict) -> None:
    pages = manifest["pages"]
    titles = [page["title"] for page in pages]
    if len(titles) != len(set(titles)):
        raise AssertionError("page titles are not unique")
    for title in titles:
        if not (title.startswith("Week 14 Tuesday:") or title.startswith("Week 14 Thursday:")):
            raise AssertionError(f"page title has the wrong prefix: {title}")
    if not any(page["source"] == "canvas/tuesday_landing.md" for page in pages):
        raise AssertionError("Tuesday landing page is missing")
    if not any(page["source"] == "canvas/tuesday_prompts.md" for page in pages):
        raise AssertionError("prompt page is missing")
    if not any(page["source"] == "canvas/thursday_activity.md" for page in pages):
        raise AssertionError("Thursday activity page is missing")


def check_prompt_page(manifest: dict) -> None:
    del manifest  # The prompt page is a package invariant, not a Canvas call.
    prompts = sorted((PACKAGE_ROOT / "prompts").glob("[0-9][0-9]_*.md"))
    if len(prompts) != 5:
        raise AssertionError(f"expected five numbered prompts, found {len(prompts)}")
    expected = b"".join(path.read_bytes() for path in prompts)
    actual = (PACKAGE_ROOT / "canvas" / "tuesday_prompts.md").read_bytes()
    if actual != expected:
        raise AssertionError("canvas/tuesday_prompts.md is not the byte-for-byte prompt concatenation")
    print(f"prompt page byte match: {len(prompts)} files")


def check_zip(manifest: dict) -> None:
    zips = manifest["zips"]
    if len(zips) != 1 or zips[0]["from_dir"] != "prompts":
        raise AssertionError("manifest must define exactly one prompts ZIP")
    source_dir = PACKAGE_ROOT / zips[0]["from_dir"]
    expected = sorted(path.relative_to(source_dir).as_posix() for path in source_dir.rglob("*") if path.is_file())
    with tempfile.TemporaryDirectory() as temp_dir:
        zip_path = Path(temp_dir) / zips[0]["name"]
        with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for path in sorted(source_dir.rglob("*")):
                if path.is_file():
                    archive.write(path, path.relative_to(source_dir).as_posix())
        with zipfile.ZipFile(zip_path) as archive:
            actual = sorted(name for name in archive.namelist() if not name.endswith("/"))
            if actual != expected:
                raise AssertionError(f"ZIP members differ: expected {expected}, got {actual}")
    print(f"ZIP test passed: {zips[0]['name']} ({len(expected)} files)")


def check_no_gate_artifact() -> None:
    forbidden = {"decision-gate.md", "gate_text.txt"}
    found = [path.relative_to(PACKAGE_ROOT).as_posix() for path in PACKAGE_ROOT.rglob("*") if path.is_file() and path.name in forbidden]
    if found:
        raise AssertionError(f"forbidden Decision Gate artifact exists: {found}")
    print("Decision Gate artifact check passed: none present")


def main() -> None:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    if manifest["week"] != 14 or manifest["module_id"] != 218913:
        raise AssertionError("manifest week/module does not match Week 14")
    if "Week 14" not in manifest["module_name_contains"]:
        raise AssertionError("module name constraint does not match Week 14")
    check_pages(manifest)
    check_sources(manifest)
    check_prompt_page(manifest)
    check_zip(manifest)
    check_no_gate_artifact()
    print("manifest check passed: Week 14 module 218913, local-only validation")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Offline checks for the Week 16 Canvas package manifest.

This validator deliberately does not contact Canvas. It validates the package
shape, student-page copies, prompt concatenation, a temporary prompt archive,
and a small forbidden-string scan.
"""

from __future__ import annotations

import json
import re
import sys
import tempfile
import zipfile
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
CANVAS_ROOT = PACKAGE_ROOT / "canvas"
MANIFEST_PATH = CANVAS_ROOT / "manifest.json"

REQUIRED_PAGES = {
    "canvas/tuesday_landing.md",
    "canvas/handout.md",
    "canvas/concept_map.md",
    "canvas/glossary.md",
    "canvas/prompts.md",
    "canvas/thursday_activity.md",
    "canvas/recap_outline.md",
}
COPY_NAMES = (
    "handout.md",
    "concept_map.md",
    "glossary.md",
    "thursday_activity.md",
    "recap_outline.md",
)

# These are the technical terms deliberately used across student pages and
# prompts. The check makes the glossary contract explicit instead of
# pretending a prose parser can identify every technical term perfectly.
STUDENT_FACING_TERMS = (
    "evidence",
    "claim",
    "Farkle",
    "strategy",
    "model",
    "simulation",
    "sample",
    "seed",
    "win rate",
    "numerator",
    "denominator",
    "percentage point",
    "pp",
    "decision rule",
    "criterion",
    "metric",
    "scope",
    "assumption",
    "outcome",
    "balanced starts",
    "variation",
    "stability",
    "sign",
    "start",
    "tie",
    "machine learning",
    "overclaim",
    "model limitation",
    "algorithm",
    "game engine",
    "opponent",
    "finite",
    "universal",
    "range",
    "Farkle rate",
    "average score",
    "preparation effort",
    "evaluation speed",
    "simplicity",
    "target score",
    "opponent setup",
    "seed bundle",
    "game count",
    "AI",
    "AI failure mode",
    "audit",
    "ordering criterion",
    "peer-visible",
    "graded discussion",
    "raw count",
    "receipt",
    "pseudo-random",
    "bounded",
    "defend",
    "revise",
    "refuse",
    "deterministic",
    "finite",
    "universal",
    "fallback fixture",
    "synthetic",
    "learner",
    "banking",
    "turn",
    "own turn",
    "points per game",
    "Farkle rate per own turn",
    "threshold",
)

_host_fragments = (
    "ap" + "ril",
    "ma" + "ise",
    "br" + "andy",
    "mo" + "rgan",
    "sep" + "tember",
)
_host_pattern = "(?:" + "|".join(_host_fragments) + ")"

FORBIDDEN_PATTERNS = (
    re.compile(r"(?i)swosu\.instructure"),
    re.compile(
        r"(?i)(?:https?://|ssh://|git@|host(?:name)?\s*[:=]?\s*)"
        + _host_pattern
        + r"(?:[./:]|$)"
    ),
    re.compile(r"(?i)\b(?:AKIA|ASIA)[0-9A-Z]{16}\b"),
    re.compile(r"(?i)\b(?:sk|pk|ghp|github_pat|xox[baprs]-)[A-Za-z0-9_-]{8,}\b"),
    re.compile(
        r"(?i)\b(?:api[_-]?key|access[_-]?token|secret[_-]?key|password)"
        r"\s*[:=]\s*\S+"
    ),
)


def fail(message: str) -> None:
    raise AssertionError(message)


def load_manifest() -> dict:
    try:
        data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"manifest JSON does not parse: {exc}")
    if not isinstance(data, dict):
        fail("manifest root is not an object")
    return data


def resolve_package_path(relative: str) -> Path:
    path = PACKAGE_ROOT / relative
    try:
        path.relative_to(PACKAGE_ROOT)
    except ValueError:
        fail(f"path escapes package root: {relative}")
    return path


def check_manifest_shape(manifest: dict) -> tuple[list[dict], list[dict], list[dict]]:
    if manifest.get("week") != 16:
        fail(f"expected week 16, got {manifest.get('week')!r}")
    if manifest.get("module_id") != 218914:
        fail(f"expected module_id 218914, got {manifest.get('module_id')!r}")
    if "Week 16" not in manifest.get("module_name_contains", ""):
        fail("module_name_contains must contain 'Week 16'")

    pages = manifest.get("pages")
    files = manifest.get("files")
    zips = manifest.get("zips")
    if not all(isinstance(value, list) for value in (pages, files, zips)):
        fail("pages, files, and zips must all be lists")
    return pages, files, zips


def check_forbidden_source_path(path_text: str) -> None:
    lowered = path_text.replace("\\", "/").lower()
    if (
        "/instructor/" in f"/{lowered}/"
        or "/code/" in f"/{lowered}/"
        or (lowered.startswith("deck/") and "notes" in Path(lowered).name)
        or "report" in Path(lowered).name
        or "instructor" in Path(lowered).name
    ):
        fail(f"instructor-only source path in manifest: {path_text}")


def check_pages(pages: list[dict]) -> None:
    titles = [page.get("title") for page in pages]
    if len(titles) != len(set(titles)):
        fail("page titles are not unique")
    for page in pages:
        if not isinstance(page, dict):
            fail("each page must be an object")
        title = page.get("title")
        source = page.get("source")
        if not isinstance(title, str) or not (
            title.startswith("Week 16 Tuesday:") or title.startswith("Week 16 Thursday:")
        ):
            fail(f"page title has wrong prefix: {title!r}")
        if not isinstance(source, str):
            fail(f"page source is not a string: {source!r}")
        check_forbidden_source_path(source)
        source_path = resolve_package_path(source)
        if not source_path.is_file():
            fail(f"missing page source: {source}")
        first_line = source_path.read_text(encoding="utf-8").splitlines()[0]
        # prompts.md must remain the exact concatenation of prompts/*.md. Its
        # first line therefore comes from prompt 01, which predates the Canvas
        # title rule; all other pages use the title as their first H1.
        if source != "canvas/prompts.md" and first_line != f"# {title}":
            fail(f"first H1 mismatch for {source}: {first_line!r} != {title!r}")
        if source == "canvas/prompts.md" and not first_line.startswith("# Prompt 01"):
            fail("prompts.md does not begin with prompt 01")

    sources = {page.get("source") for page in pages}
    missing = REQUIRED_PAGES - sources
    if missing:
        fail(f"required current page sources missing: {sorted(missing)}")


def check_files(files: list[dict], pages: list[dict]) -> None:
    page_titles = {page["title"] for page in pages}
    for item in files:
        if not isinstance(item, dict):
            fail("each file directive must be an object")
        source = item.get("source")
        if not isinstance(source, str):
            fail(f"file source is not a string: {source!r}")
        check_forbidden_source_path(source)
        if not resolve_package_path(source).is_file():
            fail(f"missing file source: {source}")
        linked = item.get("page_link_from")
        if linked not in page_titles:
            fail(f"file link target is not a page title: {linked!r}")
        if item.get("name") == "farkle_ml_slides.pdf" and source != "deck/farkle_ml_slides.pdf":
            fail("slide file directive must use deck/farkle_ml_slides.pdf")


def check_zips(zips: list[dict]) -> None:
    prompt_zip = None
    for item in zips:
        if not isinstance(item, dict):
            fail("each zip directive must be an object")
        from_dir = item.get("from_dir")
        if not isinstance(from_dir, str):
            fail(f"zip from_dir is not a string: {from_dir!r}")
        check_forbidden_source_path(from_dir)
        directory = resolve_package_path(from_dir)
        if not directory.is_dir():
            fail(f"missing zip source directory: {from_dir}")
        if item.get("name") == "farkle_ml_prompts.zip":
            prompt_zip = item
    if prompt_zip is None or prompt_zip.get("from_dir") != "prompts":
        fail("manifest must contain farkle_ml_prompts.zip from prompts")


def check_copies_and_prompts() -> None:
    for name in COPY_NAMES:
        student = PACKAGE_ROOT / "student" / name
        canvas = CANVAS_ROOT / name
        if student.read_bytes() != canvas.read_bytes():
            fail(f"Canvas copy does not byte-match student/{name}")

    prompt_paths = sorted((PACKAGE_ROOT / "prompts").glob("*.md"))
    expected = b"".join(path.read_bytes() for path in prompt_paths)
    actual = (CANVAS_ROOT / "prompts.md").read_bytes()
    if actual != expected:
        fail("canvas/prompts.md is not the exact sorted prompt concatenation")


def build_and_list_prompt_zip() -> list[str]:
    prompt_paths = sorted((PACKAGE_ROOT / "prompts").glob("*.md"))
    with tempfile.TemporaryDirectory(prefix="farkle-ml-prompts-") as temporary:
        archive_path = Path(temporary) / "farkle_ml_prompts.zip"
        with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for prompt in prompt_paths:
                archive.write(prompt, arcname=prompt.name)
        with zipfile.ZipFile(archive_path) as archive:
            members = sorted(archive.namelist())
        expected = sorted(path.name for path in prompt_paths)
        if members != expected:
            fail(f"prompt ZIP members are not prompt files: {members}")
        return members


def check_glossary() -> None:
    glossary = (PACKAGE_ROOT / "student" / "glossary.md").read_text(encoding="utf-8")
    headings = {
        line[3:].strip().casefold()
        for line in glossary.splitlines()
        if line.startswith("## ")
    }
    student_paths = sorted((PACKAGE_ROOT / "student").glob("*.md"))
    prompt_paths = sorted((PACKAGE_ROOT / "prompts").glob("*.md"))
    missing = []
    for path in student_paths + prompt_paths:
        page = path.read_text(encoding="utf-8")
        for term in STUDENT_FACING_TERMS:
            if re.search(
                rf"(?<![\w-]){re.escape(term)}s?(?![\w-])",
                page,
                flags=re.IGNORECASE,
            ) and term.casefold() not in headings:
                missing.append(f"{path.relative_to(PACKAGE_ROOT)}: {term}")
    if missing:
        fail(f"technical terms missing from glossary: {missing}")


def check_forbidden_strings() -> int:
    files = sorted(
        list((PACKAGE_ROOT / "student").glob("*.md"))
        + [
            path
            for path in (PACKAGE_ROOT / "canvas").glob("*.md")
            if not path.name.startswith("LUNA_RECEIPT_")
        ]
        + list((PACKAGE_ROOT / "prompts").glob("*.md"))
    )
    findings = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        for pattern in FORBIDDEN_PATTERNS:
            if pattern.search(text):
                findings.append(f"{path.relative_to(PACKAGE_ROOT)}: {pattern.pattern}")
    if findings:
        fail("forbidden strings found: " + "; ".join(findings))
    return len(files)


def main() -> int:
    manifest = load_manifest()
    pages, files, zips = check_manifest_shape(manifest)
    check_pages(pages)
    check_files(files, pages)
    check_zips(zips)
    check_copies_and_prompts()
    check_glossary()
    scanned = check_forbidden_strings()
    members = build_and_list_prompt_zip()

    print("manifest JSON: OK")
    print("metadata: week=16 module_id=218914 module_name_contains='Week 16'")
    print(f"pages: {len(pages)} unique titles; sources present")
    print("page H1s: OK for all pages except exact-concat prompts.md (documented invariant)")
    print(f"files: {len(files)} source(s) present and linked")
    print(f"zips: {len(zips)} directive(s); temporary prompt ZIP members:")
    for member in members:
        print(f"  {member}")
    print(f"byte matches: {', '.join(COPY_NAMES)}; prompts.md exact concatenation")
    print(
        f"glossary coverage: OK ({len(STUDENT_FACING_TERMS)} checked terms; "
        "all student pages and prompts checked)"
    )
    print(f"forbidden-string scan: clean ({scanned} student-facing markdown files)")
    print("VALIDATION OK")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"VALIDATION FAILED: {exc}", file=sys.stderr)
        raise SystemExit(1)

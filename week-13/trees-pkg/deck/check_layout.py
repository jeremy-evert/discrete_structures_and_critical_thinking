#!/usr/bin/env python3
"""Reject extracted text whose bounding box lies outside its PDF page."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


PAGE_RE = re.compile(r'<page\s+width="([0-9.]+)"\s+height="([0-9.]+)">')
WORD_RE = re.compile(
    r'<word\s+xMin="([0-9.]+)"\s+yMin="([0-9.]+)"\s+'
    r'xMax="([0-9.]+)"\s+yMax="([0-9.]+)">([^<]*)</word>'
)
EPSILON = 0.01


def check_pdf(path: Path) -> tuple[int, int]:
    result = subprocess.run(
        ["pdftotext", "-bbox", str(path), "-"],
        check=True,
        capture_output=True,
        text=True,
    )
    pages = list(PAGE_RE.finditer(result.stdout))
    if not pages:
        raise ValueError(f"{path}: pdftotext returned no page boxes")

    page_ranges = []
    for match in pages:
        page_ranges.append((match.end(), float(match.group(1)), float(match.group(2))))

    words = 0
    violations = []
    for index, (start, width, height) in enumerate(page_ranges, 1):
        end = page_ranges[index][0] if index < len(page_ranges) else len(result.stdout)
        page_text = result.stdout[start:end]
        for word in WORD_RE.finditer(page_text):
            words += 1
            x_min, y_min, x_max, y_max = map(float, word.groups()[:4])
            if (
                x_min < -EPSILON
                or y_min < -EPSILON
                or x_max > width + EPSILON
                or y_max > height + EPSILON
            ):
                text = word.group(5).replace("\n", " ")
                violations.append(
                    f"{path} page {index}: {text!r} "
                    f"({x_min:.2f},{y_min:.2f})-({x_max:.2f},{y_max:.2f}) "
                    f"outside {width:.2f}x{height:.2f}"
                )

    if violations:
        raise ValueError("\n".join(violations))
    print(f"layout ok: {path} pages={len(pages)} words={words}")
    return len(pages), words


def main(argv: list[str]) -> int:
    paths = [Path(arg) for arg in argv[1:]] or [Path("trees_slides.pdf"), Path("trees_notes.pdf")]
    try:
        for path in paths:
            check_pdf(path)
    except (OSError, subprocess.CalledProcessError, ValueError) as exc:
        print(f"layout check failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

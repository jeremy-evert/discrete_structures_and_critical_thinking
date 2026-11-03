#!/usr/bin/env python3
"""Build the student prompt page by concatenating the five prompt sources."""

from __future__ import annotations

import argparse
from pathlib import Path


def numbered_prompts(prompts_dir: Path) -> list[Path]:
    return sorted(prompts_dir.glob("[0-9][0-9]_*.md"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--package-root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="package root containing prompts/ and canvas/",
    )
    args = parser.parse_args()
    package_root = args.package_root.resolve()
    prompts_dir = package_root / "prompts"
    output = package_root / "canvas" / "tuesday_prompts.md"
    sources = numbered_prompts(prompts_dir)
    if len(sources) != 5:
        raise SystemExit(f"expected five numbered prompts, found {len(sources)}")
    output.write_bytes(b"".join(path.read_bytes() for path in sources))
    print(f"wrote {output} from {len(sources)} prompt files")


if __name__ == "__main__":
    main()

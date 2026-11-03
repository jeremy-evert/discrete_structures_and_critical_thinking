#!/usr/bin/env python3
"""Make deterministic ASCII-safe listing copies without changing source text."""

import argparse
from pathlib import Path


HERE = Path(__file__).resolve().parent
REPLACEMENTS = str.maketrans(
    {
        "—": "---",
        "“": "``",
        "”": "''",
        "’": "'",
        "‘": "`",
        "–": "--",
        "…": "...",
        "→": "->",
    }
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", nargs="?", type=Path, default=HERE / "prompts_txt")
    parser.add_argument("out", nargs="?", type=Path, default=HERE / "verbatim_txt")
    parser.add_argument("gate", nargs="?", type=Path, default=HERE / "gate_text.txt")
    args = parser.parse_args()

    args.out.mkdir(exist_ok=True)
    for old in args.out.glob("*.txt"):
        old.unlink()
    sources = sorted(args.source.glob("*.txt"))
    for source in sources:
        (args.out / source.name).write_text(
            source.read_text(encoding="utf-8").translate(REPLACEMENTS), encoding="utf-8"
        )
    if args.gate.exists():
        (args.out / args.gate.name).write_text(
            args.gate.read_text(encoding="utf-8").translate(REPLACEMENTS), encoding="utf-8"
        )
    print(f"rendered verbatim listings: {len(sources)} prompts + gate")


if __name__ == "__main__":
    main()

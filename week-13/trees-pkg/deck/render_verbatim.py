#!/usr/bin/env python3
"""Make deterministic ASCII-safe listing copies without changing source text."""

from pathlib import Path


HERE = Path(__file__).resolve().parent
OUT = HERE / "verbatim_txt"
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
    OUT.mkdir(exist_ok=True)
    for source in sorted((HERE / "prompts_txt").glob("*.txt")):
        (OUT / source.name).write_text(source.read_text(encoding="utf-8").translate(REPLACEMENTS), encoding="utf-8")
    gate = HERE / "gate_text.txt"
    (OUT / gate.name).write_text(gate.read_text(encoding="utf-8").translate(REPLACEMENTS), encoding="utf-8")
    print(f"rendered verbatim listings: {len(list((HERE / 'prompts_txt').glob('*.txt')))} prompts + gate")


if __name__ == "__main__":
    main()

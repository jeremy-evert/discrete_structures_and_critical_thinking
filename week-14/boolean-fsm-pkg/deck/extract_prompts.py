#!/usr/bin/env python3
"""Extract the paste-ready prompt blocks into the deck's listing directory."""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE.parent / "prompts"
OUTPUT = HERE / "prompts_txt"
OUTPUT.mkdir(exist_ok=True)

for path in sorted(SOURCE.glob("[0-9][0-9]_*.md")):
    number = path.name[:2]
    text = path.read_text(encoding="utf-8")
    (OUTPUT / f"{number}.name").write_text(path.name.replace("_", r"\_"), encoding="utf-8")
    found = set()
    for label, body in re.findall(r"^```prompt-([ab])\n(.*?)^```", text, re.S | re.M):
        found.add(label)
        (OUTPUT / f"{number}_{label}.txt").write_text(body, encoding="utf-8")
        small = OUTPUT / f"{number}_{label}.small"
        if body.count("\n") > 12:
            small.write_text("", encoding="utf-8")
        elif small.exists():
            small.unlink()
    for stale in OUTPUT.glob(f"{number}_[ab].txt"):
        if stale.stem.rsplit("_", 1)[1] not in found:
            stale.unlink()
    for stale in OUTPUT.glob(f"{number}_[ab].small"):
        if stale.stem.rsplit("_", 1)[1] not in found:
            stale.unlink()

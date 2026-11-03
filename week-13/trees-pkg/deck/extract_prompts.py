#!/usr/bin/env python3
"""Copy exact prompt blocks into the files used by the slide prompt boxes."""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
src = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE.parent / "prompts"
out = HERE / "prompts_txt"
out.mkdir(exist_ok=True)
for old in out.glob("[0-9][0-9]_*.*"):
    if old.suffix in {".txt", ".name", ".small"}:
        old.unlink()
for f in sorted(src.glob("[0-9][0-9]_*.md")):
    nn = f.name[:2]
    text = f.read_text(encoding="utf-8")
    (out / f"{nn}.name").write_text(f.name.replace("_", r"\_"), encoding="utf-8")
    for label, body in re.findall(r"^```prompt-([ab])\n(.*?)^```", text, re.S | re.M):
        (out / f"{nn}_{label}.txt").write_text(body, encoding="utf-8")
        if body.count("\n") > 12:
            (out / f"{nn}_{label}.small").write_text("", encoding="utf-8")
print(f"extracted prompts from {len(list(src.glob('[0-9][0-9]_*.md')))} files")

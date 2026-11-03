#!/usr/bin/env python3
"""Copy fenced prompt-a/prompt-b blocks into the slide build directory."""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE.parent / "prompts"
OUTPUT = HERE / "prompts_txt"
OUTPUT.mkdir(exist_ok=True)

for prompt_file in sorted(SOURCE.glob("[0-9][0-9]_*.md")):
    number = prompt_file.name[:2]
    body = prompt_file.read_text()
    (OUTPUT / f"{number}.name").write_text(prompt_file.name.replace("_", r"\_"))
    for label, prompt in re.findall(r"^```prompt-([ab])\n(.*?)^```", body, re.S | re.M):
        (OUTPUT / f"{number}_{label}.txt").write_text(prompt)
        small = OUTPUT / f"{number}_{label}.small"
        if prompt.count("\n") > 12:
            small.write_text("")
        elif small.exists():
            small.unlink()

#!/usr/bin/env python3
"""Copy the paste-ready ```prompt-a / ```prompt-b blocks from prompts/NN_slug.md into prompts_txt/.
Usage: extract_prompts.py [PROMPTS_DIR]   (default ../prompts)"""
import re, sys, pathlib
here = pathlib.Path(__file__).resolve().parent
src = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else here.parent / "prompts"
out = here / "prompts_txt"
out.mkdir(exist_ok=True)
for f in sorted(src.glob("[0-9][0-9]_*.md")):
    nn = f.name[:2]
    text = f.read_text()
    (out / f"{nn}.name").write_text(f.name.replace("_", r"\_"))
    for label, body in re.findall(r"^```prompt-([ab])\n(.*?)^```", text, re.S | re.M):
        (out / f"{nn}_{label}.txt").write_text(body)

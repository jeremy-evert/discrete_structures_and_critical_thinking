#!/usr/bin/env python3
"""Copy exact prompt blocks into a chosen directory for the slide pipeline."""
import argparse
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("src", nargs="?", type=pathlib.Path, default=HERE.parent / "prompts")
    parser.add_argument("out", nargs="?", type=pathlib.Path, default=HERE / "prompts_txt")
    args = parser.parse_args()

    src = args.src
    out = args.out
    out.mkdir(exist_ok=True)
    for old in out.glob("[0-9][0-9]_*.*"):
        if old.suffix in {".txt", ".name", ".small"}:
            old.unlink()
    prompt_count = 0
    block_count = 0
    for f in sorted(src.glob("[0-9][0-9]_*.md")):
        prompt_count += 1
        nn = f.name[:2]
        text = f.read_text(encoding="utf-8")
        (out / f"{nn}.name").write_text(f.name.replace("_", r"\_"), encoding="utf-8")
        for label, body in re.findall(r"^```prompt-([ab])\n(.*?)^```", text, re.S | re.M):
            block_count += 1
            (out / f"{nn}_{label}.txt").write_text(body, encoding="utf-8")
            if body.count("\n") > 12:
                (out / f"{nn}_{label}.small").write_text("", encoding="utf-8")
    print(f"extracted prompts from {prompt_count} files ({block_count} blocks)")


if __name__ == "__main__":
    main()

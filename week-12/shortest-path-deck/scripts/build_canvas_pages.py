#!/usr/bin/env python3
"""Regenerate canvas/prompts_page.md as the prompt files, verbatim, in order."""
import pathlib
root = pathlib.Path(__file__).resolve().parent.parent
files = sorted((root / "prompts").glob("[0-9][0-9]_*.md"))
head = "# Week 12: the Claude prompts (all six)\n\nEach block is exactly what is on the slide. Copy the whole block into Claude. Predict the result first.\n\n---\n\n"
body = "\n---\n\n".join(f.read_text() for f in files)
(root / "canvas" / "prompts_page.md").write_text(head + body)
print("wrote canvas/prompts_page.md from", len(files), "prompt files")

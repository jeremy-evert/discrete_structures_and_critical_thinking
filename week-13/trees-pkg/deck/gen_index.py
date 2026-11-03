#!/usr/bin/env python3
"""Build the principle/prompt index and list prompt references for checks."""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
PARTS = sorted(p.stem for p in HERE.glob("part*.tex"))


def args(s, i, n):
    out = []
    for _ in range(n):
        while s[i] != "{":
            i += 1
        depth, start = 0, i
        while True:
            depth += s[i] == "{"
            depth -= s[i] == "}"
            i += 1
            if depth == 0:
                break
        out.append(s[start + 1 : i - 1])
    return out, i


def clean(text):
    text = re.sub(r"\\texttt\{(.*?)\}", r"\1", text)
    return text.replace("\\_", "_").replace("$", "").strip()


rows, number = [], 1  # the title frame is slide 1
for part in PARTS:
    source = (HERE / f"{part}.tex").read_text(encoding="utf-8")
    for match in re.finditer(r"\\begin\{frame\}(?:\[[^\]]*\])?\{", source):
        title_args, end = args(source, match.end() - 1, 1)
        title = title_args[0]
        frame_end = source.index("\\end{frame}", end)
        body = source[end:frame_end]
        principle = re.search(r"\\princ\{(.*?)\}", body)
        prompts = [a + b for a, b in re.findall(r"\\promptbox\{(\d+)\}\{([ab])\}", body)]
        number += 1
        if principle or prompts:
            rows.append((number, clean(title), principle.group(1) if principle else "", ", ".join(prompts)))

if "--list-prompts" in sys.argv:
    for row in rows:
        for prompt in filter(None, row[3].split(", ")):
            print(prompt[:2], prompt[2])
    raise SystemExit(0)

chunks = [rows[i : i + 9] for i in range(0, len(rows), 9)]
output = []
for index, chunk in enumerate(chunks, 1):
    output.append(
        f"\\begin{{frame}}{{Index {index} of {len(chunks)}: principle, slide, prompt}}\n"
        "\\scriptsize\n"
        "\\begin{tabular}{@{}r>{\\raggedright\\arraybackslash}p{5.1cm}>{\\raggedright\\arraybackslash}p{4.7cm}p{1.2cm}@{}}\n"
        "\\textbf{Slide} & \\textbf{Title} & \\textbf{Principle} & \\textbf{Prompt}\\\\\\midrule\n"
    )
    for slide, title, principle, prompts in chunk:
        title_tex = title.replace("&", "\\&").replace("_", "\\_")
        principle_tex = principle.replace("&", "\\&")
        output.append(f"{slide} & {title_tex} & {principle_tex} & {prompts}\\\\\n")
    output.append(
        "\\end{tabular}\n"
        "\\note{Use this to find a slide fast: slide number, lesson idea, and prompt file. Prompt a is the first block and b is the second block.}\n"
        "\\end{frame}\n"
    )
text = "".join(output)
target = HERE / "index_rows.tex"
if "--check" in sys.argv:
    if not target.exists() or target.read_text(encoding="utf-8") != text:
        print("index_rows.tex out of date: run gen_index.py")
        raise SystemExit(1)
    print(f"index consistent: {len(rows)} rows, {number} content slides")
else:
    target.write_text(text, encoding="utf-8")
    print(f"wrote index_rows.tex: {len(rows)} rows over {len(chunks)} frames; content slides {number}")

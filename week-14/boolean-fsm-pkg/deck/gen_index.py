#!/usr/bin/env python3
"""Generate and verify the deck's principle/prompt index."""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
PARTS = sorted(HERE.glob("part*.tex"))


def arguments(text, start, count):
    values = []
    index = start
    for _ in range(count):
        while text[index] != "{":
            index += 1
        depth = 0
        end = index
        while end < len(text):
            depth += text[end] == "{"
            depth -= text[end] == "}"
            end += 1
            if depth == 0:
                break
        values.append(text[index + 1 : end - 1])
        index = end
    return values, index


def clean(value):
    value = re.sub(r"\\texttt\{(.*?)\}", r"\1", value)
    return value.replace("\\_", "_").replace("$", "").strip()


rows = []
slide_number = 1
for part in PARTS:
    text = part.read_text(encoding="utf-8")
    for match in re.finditer(r"\\begin\{frame\}(?:\[[^\]]*\])?\{|\\stepslide\{", text):
        if match.group(0).startswith("\\stepslide"):
            args, _ = arguments(text, match.start() + len("\\stepslide"), 9)
            title, principle, prompt = args[0], args[1], args[3]
            prompts = [prompt] if prompt else []
        else:
            args, end = arguments(text, match.end() - 1, 1)
            title = args[0]
            frame_end = text.index("\\end{frame}", end)
            body = text[end:frame_end]
            principle_match = re.search(r"\\princ\{(.*?)\}", body)
            principle = principle_match.group(1) if principle_match else ""
            prompts = [a + b for a, b in re.findall(r"\\promptbox\{(\d+)\}\{([ab])\}", body)]
        slide_number += 1
        if principle or prompts:
            rows.append((slide_number, clean(title), clean(principle), ", ".join(prompts)))

if "--list-prompts" in sys.argv:
    for row in rows:
        for prompt in filter(None, row[3].split(", ")):
            print(prompt[:-1], prompt[-1])
    raise SystemExit(0)

chunks = [rows[index : index + 9] for index in range(0, len(rows), 9)]
output = []
for page, chunk in enumerate(chunks, 1):
    output.append(
        f"\\begin{{frame}}{{Index {page} of {len(chunks)}: principle, slide, prompt}}\n"
        "\\scriptsize\n"
        "\\begin{tabular}{@{}r>{\\raggedright\\arraybackslash}p{5.0cm}>{\\raggedright\\arraybackslash}p{4.8cm}p{1.1cm}@{}}\n"
        "\\textbf{Slide} & \\textbf{Title} & \\textbf{Principle} & \\textbf{Prompt}\\\\\\midrule\n"
    )
    for number, title, principle, prompts in chunk:
        title = title.replace("&", "\\&").replace("_", "\\_")
        principle = principle.replace("&", "\\&")
        output.append(f"{number} & {title} & {principle} & {prompts}\\\\\n")
    output.append(
        "\\end{tabular}\n"
        "\\note{Use this index to find a slide by number, principle, and prompt file.}\n"
        "\\end{frame}\n"
    )
generated = "".join(output)
target = HERE / "index_rows.tex"
if "--check" in sys.argv:
    if not target.exists() or target.read_text(encoding="utf-8") != generated:
        print("index_rows.tex out of date: run gen_index.py")
        raise SystemExit(1)
    print(f"index consistent: {len(rows)} rows")
else:
    target.write_text(generated, encoding="utf-8")
    print(f"wrote index_rows.tex: {len(rows)} rows over {len(chunks)} index frames")

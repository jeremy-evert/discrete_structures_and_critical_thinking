#!/usr/bin/env python3
"""Build or check the slide index and enumerate every prompt box."""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
PARTS = sorted(p.stem for p in HERE.glob("part*.tex"))


def brace_args(source, index, count):
    values = []
    for _ in range(count):
        while source[index] != "{":
            index += 1
        depth = 0
        end = index
        while True:
            depth += source[end] == "{"
            depth -= source[end] == "}"
            end += 1
            if depth == 0:
                break
        values.append(source[index + 1 : end - 1])
        index = end
    return values, index


def clean(text):
    text = re.sub(r"\\texttt\{(.*?)\}", r"\1", text)
    return text.replace("\\_", "_").replace("$", "").strip()


rows = []
slide_number = 1
for part in PARTS:
    source = (HERE / f"{part}.tex").read_text()
    for match in re.finditer(r"\\begin\{frame\}(?:\[[^\]]*\])?\{|\\stepslide\{", source):
        if match.group(0).startswith("\\stepslide"):
            args, _ = brace_args(source, match.start() + len("\\stepslide"), 9)
            title, principle, prompt = args[0], args[1], args[3]
            prompts = [prompt]
        else:
            args, end = brace_args(source, match.end() - 1, 1)
            title = args[0]
            frame_end = source.index("\\end{frame}", end)
            body = source[end:frame_end]
            principle_match = re.search(r"\\princ\{(.*?)\}", body)
            principle = principle_match.group(1) if principle_match else ""
            prompts = [
                number + label
                for number, label in re.findall(r"\\promptbox\{(\d+)\}\{([ab])\}", body)
            ]
        slide_number += 1
        if principle or prompts:
            rows.append((slide_number, clean(title), principle, ", ".join(prompts)))

total_slides = slide_number
if "--list-prompts" in sys.argv:
    for row in rows:
        for prompt in filter(None, row[3].split(", ")):
            print(prompt[:-1], prompt[-1])
    raise SystemExit(0)

chunks = [rows[i : i + 9] for i in range(0, len(rows), 9)]
output = []
for index, chunk in enumerate(chunks, 1):
    output.append(
        f"\\begin{{frame}}{{Index {index} of {len(chunks)}: principle, slide, prompt}}\n"
        "\\scriptsize\n"
        "\\begin{tabular}{@{}r>{\\raggedright\\arraybackslash}p{5.1cm}>"
        "{\\raggedright\\arraybackslash}p{4.6cm}p{1.2cm}@{}}\n"
        "\\textbf{Slide} & \\textbf{Title} & \\textbf{Principle} & "
        "\\textbf{Prompt}\\\\\\midrule\n"
    )
    for row in chunk:
        title = row[1].replace("&", r"\&").replace("_", r"\_")
        principle = row[2].replace("&", r"\&")
        output.append(f"{row[0]} & {title} & {principle} & {row[3]}\\\\\n")
    output.append(
        "\\end{tabular}\n"
        "\\note{Use this index to find a slide fast. Question: which prompt or "
        "principle would you revisit? Expected: a slide number and a reason.}\n"
        "\\end{frame}\n"
    )

rendered = "".join(output)
target = HERE / "index_rows.tex"
if "--check" in sys.argv:
    if not target.exists() or target.read_text() != rendered:
        print("index_rows.tex out of date: run gen_index.py")
        raise SystemExit(1)
    print(f"index consistent: {len(rows)} rows, {total_slides} content slides")
else:
    target.write_text(rendered)
    print(f"wrote index_rows.tex: {len(rows)} rows over {len(chunks)} frames; content slides {total_slides}")

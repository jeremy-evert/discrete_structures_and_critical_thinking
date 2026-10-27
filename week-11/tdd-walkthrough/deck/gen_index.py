#!/usr/bin/env python3
"""Build index_rows.tex (slide number, title, principle, prompt) from the part files.
--check: fail unless the committed index_rows.tex matches what the slides say now."""
import re, sys, pathlib
here = pathlib.Path(__file__).resolve().parent
PARTS = ["part0", "part1", "part2", "part3", "part4"]

def args(s, i, n):
    out = []
    for _ in range(n):
        while s[i] != "{":
            i += 1
        d, j = 0, i
        while True:
            d += s[j] == "{"; d -= s[j] == "}"
            j += 1
            if d == 0:
                break
        out.append(s[i + 1:j - 1]); i = j
    return out, i

def clean(t):
    t = re.sub(r"\\texttt\{(.*?)\}", r"\1", t)
    return t.replace("\\_", "_").replace("$", "").strip()

rows, n = [], 1                      # slide 1 is the title frame
for p in PARTS:
    s = (here / f"{p}.tex").read_text()
    for m in re.finditer(r"\\begin\{frame\}(?:\[[^\]]*\])?\{|\\stepslide\{", s):
        if m.group(0).startswith("\\stepslide"):
            a, _ = args(s, m.start() + len("\\stepslide") , 9)
            title, princ = a[0], a[1]
            prompts = [a[3]]
        else:
            a, e = args(s, m.end() - 1, 1)
            title = a[0]
            end = s.index("\\end{frame}", e)
            body = s[e:end]
            pm = re.search(r"\\princ\{(.*?)\}", body)
            princ = pm.group(1) if pm else ""
            prompts = [x + y for x, y in re.findall(r"\\promptbox\{(\d+)\}\{([ab])\}", body)]
        n += 1
        if princ or prompts:
            rows.append((n, clean(title), princ, ", ".join(prompts)))
total = n
if "--list-prompts" in sys.argv:
    for r in rows:
        for x in filter(None, r[3].split(", ")):
            print(x[:-1], x[-1])
    sys.exit(0)
out = []
per = 9
chunks = [rows[i:i + per] for i in range(0, len(rows), per)]
for k, ch in enumerate(chunks, 1):
    out.append(f"\\begin{{frame}}{{Index {k} of {len(chunks)}: principle, slide, prompt}}\n\\scriptsize\n"
               "\\begin{tabular}{@{}r>{\\raggedright\\arraybackslash}p{5.4cm}>{\\raggedright\\arraybackslash}p{4.6cm}p{1.2cm}@{}}\n\\textbf{Slide} & \\textbf{Title} & \\textbf{Principle} & \\textbf{Prompt}\\\\\\midrule\n")
    for r in ch:
        t = r[1].replace("&", "\\&").replace("_", "\\_")
        pr = r[2].replace("&", "\\&")
        out.append(f"{r[0]} & {t} & {pr} & {r[3]}\\\\\n")
    out.append("\\end{tabular}\n\\note{Use this to find a slide fast: slide number, which lesson idea it shows, and which prompt file it pairs with (prompts/NN, a = first block, b = second block).}\n\\end{frame}\n")
text = "".join(out)
target = here / "index_rows.tex"
if "--check" in sys.argv:
    if not target.exists() or target.read_text() != text:
        print("index_rows.tex out of date: run gen_index.py"); sys.exit(1)
    print(f"index consistent: {len(rows)} rows, {total} content slides"); sys.exit(0)
target.write_text(text)
print(f"wrote index_rows.tex: {len(rows)} rows over {len(chunks)} frames; content slides {total}")

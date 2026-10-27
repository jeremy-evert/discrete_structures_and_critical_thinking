#!/usr/bin/env python3
"""Render a Markdown file to PDF: markdown -> HTML -> headless Chromium. Usage: render_pdf.py in.md out.pdf"""
import pathlib, subprocess, sys, tempfile
import markdown

CSS = """
body{font:11.5pt/1.45 Georgia,serif;max-width:7.2in;margin:0 auto;color:#111}
h1{font-size:22pt;border-bottom:3px solid #333} h2{font-size:16pt;margin-top:1.4em;border-bottom:1px solid #999}
h3{font-size:13.5pt;margin-top:1.3em;background:#eef;padding:2px 6px} h4{font-size:12pt;margin-top:1.2em;background:#ffe;padding:2px 6px;border-left:4px solid #c90}
code,pre{font-family:Menlo,Consolas,monospace;font-size:9.5pt} pre{background:#f3f3f3;border:1px solid #bbb;padding:6px;white-space:pre-wrap}
table{border-collapse:collapse;width:100%;margin:6px 0} th,td{border:1px solid #888;padding:3px 6px;vertical-align:top;font-size:10pt}
blockquote{border:2px solid #333;background:#fafafa;margin:8px 0;padding:4px 10px}
h4,blockquote,pre,table{page-break-inside:avoid} h3,h4{page-break-after:avoid}
"""

def main(src, dst):
    html = markdown.markdown(pathlib.Path(src).read_text(), extensions=["tables", "fenced_code", "sane_lists"])
    doc = "<!doctype html><meta charset=utf-8><style>%s</style><body>%s</body>" % (CSS, html)
    # Snap-packaged Chromium can only read and write under $HOME, so stage there.
    with tempfile.TemporaryDirectory(dir=str(pathlib.Path.home())) as d:
        page = pathlib.Path(d) / "page.html"
        out = pathlib.Path(d) / "out.pdf"
        page.write_text(doc)
        subprocess.run(["chromium", "--headless", "--disable-gpu", "--no-sandbox",
                        "--no-pdf-header-footer", "--print-to-pdf=" + str(out), page.as_uri()],
                       check=True, capture_output=True, timeout=120)
        pathlib.Path(dst).write_bytes(out.read_bytes())

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

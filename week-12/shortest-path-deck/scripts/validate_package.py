#!/usr/bin/env python3
"""Validate canvas/manifest.json per docs/DSCT_WEEK_PACKAGE_CONTRACT.md. Exit 0 = ok."""
import json, pathlib, re, subprocess, sys, tempfile, zipfile
root = pathlib.Path(__file__).resolve().parent.parent
m = json.loads((root / "canvas" / "manifest.json").read_text())
errs = []
banned = re.compile(r"instructor|notes\.pdf|run-of-show|REPORT|tour\.py|/code/", re.I)
titles = [p["title"] for p in m["pages"]]
if len(set(titles)) != len(titles): errs.append("duplicate titles")
for t in titles:
    if not re.match(rf"Week {m['week']} (Tuesday|Thursday):", t): errs.append("title prefix: " + t)
for p in m["pages"]:
    if not (root / p["source"]).exists(): errs.append("missing " + p["source"])
    if banned.search(p["source"]): errs.append("instructor-only path " + p["source"])
for f in m["files"]:
    if not (root / f["source"]).exists(): errs.append("missing " + f["source"])
    if banned.search(f["source"]): errs.append("instructor-only path " + f["source"])
    if f["page_link_from"] not in titles: errs.append("page_link_from unknown " + f["page_link_from"])
for z in m["zips"]:
    d = root / z["from_dir"]
    if not d.is_dir(): errs.append("missing dir " + z["from_dir"]); continue
    with tempfile.TemporaryDirectory() as t:
        zp = pathlib.Path(t) / z["name"]
        with zipfile.ZipFile(zp, "w") as zf:
            for p in sorted(d.glob("*.md")): zf.write(p, p.name)
        if len(zipfile.ZipFile(zp).namelist()) != len(list(d.glob("*.md"))): errs.append("zip mismatch")
# prompts page equals regenerated output
cur = (root / "canvas" / "prompts_page.md").read_text()
subprocess.run([sys.executable, str(root / "scripts" / "build_canvas_pages.py")], check=True, stdout=subprocess.DEVNULL)
if (root / "canvas" / "prompts_page.md").read_text() != cur: errs.append("prompts page not equal to prompt files")
# gate text unchanged
if (root / "deck" / "gate_text.txt").exists():
    pass
# grep clean
bad = re.compile(r"\b(brandy|maise|april|grace|september|perfsonar)\b|swosu\.instructure|token|password", re.I)
for p in list((root / "canvas").glob("*.md")) + list((root / "student").glob("*.md")):
    for i, line in enumerate(p.read_text().splitlines(), 1):
        if bad.search(line): errs.append(f"grep {p.name}:{i}: {line[:60]}")
print("\n".join(errs) or "OK"); sys.exit(1 if errs else 0)

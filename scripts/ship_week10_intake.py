#!/usr/bin/env python3
"""Ship the Week 10 gambler's-fallacy story + board notes to a Canvas course.

Additive and idempotent: files are overwritten in place (same file id), the page
is updated if it exists, the module is found by name (created only when absent),
and module items are added only when missing. Dry-run unless --apply.

Target lock: the course id AND name fragment must match the live course, and the
host must match the chosen --env (savnac = loopback tunnel, real = swosu).
Instructor-only material (week-10/instructor/) is never uploaded.

Usage (Harbor on PYTHONPATH):
  set -a; source ~/.config/canvas/savnac.env; set +a
  python3 scripts/ship_week10_intake.py --env savnac --course 4 --expect-name "Discrete Structures" --apply
  python3 scripts/ship_week10_intake.py --env real --course <id> --expect-name <COMSC-2043-14xx> --apply
"""
from __future__ import annotations

import argparse
import html
import os
import sys
from pathlib import Path

from harbor import config
from harbor.api import (
    create_module, create_module_item, create_page, get_course, get_module_items,
    list_course_files, list_modules, update_page, upload_course_file,
)
from harbor.client import CanvasClient

ROOT = Path(__file__).resolve().parent.parent
W10 = ROOT / "week-10"
MODULE_NAME = "DSCT Week 10 -- Probability, Uncertainty & Evidence"
PAGE_SLUG = "week-10-the-gamblers-fallacy-told-with-coins"
PAGE_TITLE = "Week 10 -- The Gambler's Fallacy, Told With Coins"
RECAP = ROOT / "lecture-recaps" / "2026-10-20-week10-tuesday-recap.md"
RECAP_SLUG = "week-10-tuesday-class-recap-october-20"
RECAP_TITLE = "Week 10 -- Tuesday Class Recap (October 20)"
FOLDER = "week-10"
FILES = {  # published name -> (source, content type, module item title)
    "week10_gamblers_fallacy_story.zip": (W10 / "code" / "week10_gamblers_fallacy_story.zip", "application/zip",
                                          "Gambler's Fallacy Story: code and guide (ZIP)"),
    "week10_board_notes.pdf": (W10 / "board-notes" / "week10_board_notes.pdf", "application/pdf",
                               "Week 10 Board Notes (PDF)"),
    "week10_board_notes.pptx": (W10 / "board-notes" / "week10_board_notes.pptx",
                                "application/vnd.openxmlformats-officedocument.presentationml.presentation",
                                "Week 10 Board Notes (PowerPoint with ink)"),
}
HOSTS = {"savnac": "127.0.0.1:3002", "real": "swosu.instructure.com"}
CHAPTERS = [
    ("1", "One coin flip", "The computer turns a random number into HEADS or TAILS."),
    ("2", "Many flips", "With few flips the answer wobbles; with many it settles near one half."),
    ("3", "How rare is a streak?", "Measure how often five heads in a row happens and compare it with (1/2)^5."),
    ("4", "The gambler's question", "After a streak of heads, is tails 'due'? Measure it: still about 1/2."),
    ("5", "Meet the evil coin", "Same code, one different number: a coin with heads on both sides."),
    ("6", "The bag of coins", "99 fair coins and 1 evil coin: what does a streak tell you about the coin you hold?"),
    ("7", "Simulation meets Bayes", "Simulate it, then check the simulation against Bayes' rule, streak by streak."),
]


def page_body(urls: dict[str, str]) -> str:
    rows = "".join(
        f"<tr><td>{n}</td><td><code>chapter_{n}_*.py</code> &mdash; {html.escape(t)}</td><td>{html.escape(d)}</td></tr>"
        for n, t, d in CHAPTERS)
    link = lambda k, text: f'<a href="{urls[k]}">{html.escape(text)}</a>'
    return f"""
<h2>The one-sentence version</h2>
<p>A random thing never <em>owes</em> you a correction. A fair coin has no memory, and when the past <em>does</em> tell you something, it says the streak is more likely to continue, not to reverse.</p>
<h2>The story, in seven runnable chapters</h2>
<p>Each chapter is a short Python script that adds one idea. Run them in order; every one takes a few seconds. Your numbers will differ slightly from the guide's sample runs, because the flips are random.</p>
<table border="1" cellpadding="6" style="border-collapse:collapse"><tr><th>#</th><th>Script</th><th>The new idea</th></tr>{rows}</table>
<p>Download {link("week10_gamblers_fallacy_story.zip", "the ZIP (seven chapters plus the full written guide)")}. Unzip it, open a terminal in the folder that holds <code>gamblers_fallacy_story</code>, and run <code>python3 gamblers_fallacy_story/chapter_1_one_coin_flip.py</code>, then chapter 2, and so on. On Windows use <code>python</code> if <code>python3</code> is not found. The simulation is a check on the reasoning, not a replacement for it.</p>
<h2>Board notes from class</h2>
<p>Handwritten notes from the board: {link("week10_board_notes.pdf", "PDF")} (the same three slides as {link("week10_board_notes.pptx", "PowerPoint with the original ink")}, which needs PowerPoint to display the handwriting).</p>
<ol>
<li><strong>A streak of tails, one flip at a time.</strong> Each extra tails in a row halves the chance of the whole streak (1/2, 1/4, 1/8, 1/16, 1/32, 1/64), yet every next flip is still 1/2. The notes list the three-flip outcomes (HHT, TTT, TTH, THT, THH, HTT, HHH...) and set up the question "fair coin or evil coin?"</li>
<li><strong>The sample space grows.</strong> One flip has 2 outcomes, two flips have 4, three flips have 8. Circled branches show that the streak outcomes are only some of the equally likely paths.</li>
<li><strong>Which coin do we hold?</strong> The bag has 99 good coins and 1 evil coin (1/100). Six tails in a row has chance 1/64 for a fair coin. The box sets up the total probability P(G)&middot;(1/2)&#8310; + P(E)&middot;(its own chance), the first step toward Bayes' rule.</li>
</ol>
<p>Use these together with this week's deck and Tuesday activity; they add the sample-space tree and the evil-coin setup that the slides only mention.</p>
"""


def recap_body() -> str:
    import markdown
    return markdown.markdown(RECAP.read_text(encoding="utf-8").split("\n", 1)[1], extensions=["sane_lists"])


def upsert_page(client: CanvasClient, course: int, slug: str, title: str, body: str) -> None:
    fields = {"wiki_page[title]": title, "wiki_page[body]": body, "wiki_page[published]": "true"}
    if client.get(f"/api/v1/courses/{course}/pages/{slug}").status_code == 200:
        update_page(client, course, slug, fields)
    else:
        create_page(client, course, {**fields, "wiki_page[url]": slug})


def guard(client: CanvasClient, env: str, course_id: int, expect: str) -> dict:
    host = HOSTS[env]
    base = client.config.api_base_url
    if host not in base:
        raise SystemExit(f"REFUSE: --env {env} expects host {host}, client points at {base}")
    _, course = get_course(client, course_id)
    if int(course["id"]) != course_id or expect.lower() not in (course.get("name", "") + " " + course.get("course_code", "")).lower():
        raise SystemExit(f"REFUSE: course {course_id} is {course.get('name')!r}/{course.get('course_code')!r}, expected fragment {expect!r}")
    return course


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--env", choices=HOSTS, required=True)
    ap.add_argument("--course", type=int, required=True)
    ap.add_argument("--expect-name", required=True, help="fragment of the live course name or code")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    if a.env == "real":
        config.load_env()
    client = CanvasClient(config.read_canvas_config())
    course = guard(client, a.env, a.course, a.expect_name)
    print(f"target OK: {course['id']} {course['name']} ({course.get('course_code')}) state={course.get('workflow_state')}")
    for name, (src, _, _) in FILES.items():
        assert src.is_file(), src
    if not a.apply:
        print("dry run: would upload", list(FILES), "page", PAGE_SLUG, "module", MODULE_NAME)
        return 0

    urls, file_ids = {}, {}
    for name, (src, ctype, _) in FILES.items():
        up = upload_course_file(client, a.course, src, folder_path=FOLDER, content_type=ctype, filename=name, on_duplicate="overwrite")
        file_ids[name] = up["id"]
        urls[name] = f"/courses/{a.course}/files/{up['id']}/download?wrap=1"
    body = page_body(urls)
    upsert_page(client, a.course, PAGE_SLUG, PAGE_TITLE, body)
    upsert_page(client, a.course, RECAP_SLUG, RECAP_TITLE, recap_body())

    mods = {m["name"]: m for m in list_modules(client, a.course)}
    mod = mods.get(MODULE_NAME)
    if mod is None:
        _, mod = create_module(client, a.course, {"module[name]": MODULE_NAME, "module[published]": "true"})
        print("created module", mod["id"])
    have = {(i["type"], i.get("page_url") or i.get("content_id")) for i in get_module_items(client, a.course, mod["id"])}
    if ("Page", PAGE_SLUG) not in have:
        create_module_item(client, a.course, mod["id"], {"module_item[title]": PAGE_TITLE, "module_item[type]": "Page", "module_item[page_url]": PAGE_SLUG})
    if ("Page", RECAP_SLUG) not in have:
        create_module_item(client, a.course, mod["id"], {"module_item[title]": RECAP_TITLE, "module_item[type]": "Page", "module_item[page_url]": RECAP_SLUG})
    for name, (_, _, title) in FILES.items():
        if ("File", file_ids[name]) not in have:
            create_module_item(client, a.course, mod["id"], {"module_item[title]": title, "module_item[type]": "File", "module_item[content_id]": str(file_ids[name])})

    # read back
    pg = client.get(f"/api/v1/courses/{a.course}/pages/{PAGE_SLUG}").json()
    items = get_module_items(client, a.course, mod["id"])
    files = {f["display_name"]: f for f in list_course_files(client, a.course)}
    ok = pg.get("published") and all(n in files for n in FILES) and all(any(i["title"] == t for i in items) for _, _, t in FILES.values()) \
        and any(i["title"] == PAGE_TITLE for i in items) and any(i["title"] == RECAP_TITLE for i in items) \
        and client.get(f"/api/v1/courses/{a.course}/pages/{RECAP_SLUG}").json().get("published") and all(urls[n].split("/")[-2] in body for n in urls)
    print(f"READBACK page published={pg.get('published')} body_len={len(pg.get('body',''))} files={[n for n in FILES if n in files]} module_items={len(items)} -> {'PASS' if ok else 'FAIL'}")
    print(f"page: /courses/{a.course}/pages/{PAGE_SLUG}   module: /courses/{a.course}/modules#module_{mod['id']}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

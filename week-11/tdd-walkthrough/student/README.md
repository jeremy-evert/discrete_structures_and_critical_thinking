# Thursday student side: "Clean up a playlist, test first"

Mission: students repeat Tuesday's test-driven process, in pairs, on a different but parallel problem. Owner: Ivy (branch `ivy/dsct-thu-student-20261027`). Tuesday's demonstration is Anna's lane (`anna/dsct-tdd-relations-20261027`).

## What is in here

| Path | Who sees it | What it is |
|---|---|---|
| `WORKBOOK.md` / `WORKBOOK.pdf` | students | The numbered fill-in workbook (Steps 00–14, same numbers as Tuesday's prompts). |
| `GLOSSARY.md` / `GLOSSARY.pdf` | students | Plain-language definitions of every term the workbook uses. |
| `starter/` | students (zip it) | The only code students get: `Track`, made-up fixtures, the witness finders, `pytest.ini`. |
| `FACILITATOR.md` / `FACILITATOR.pdf` | Jeremy | 75-minute plan, 60-second pair check, stuck table, what changes in the existing Thursday plan. |
| `instructor-only/` | **never post** | Reference solution on a commit ladder, ladder and demo checkers, dry-run logs. |
| `tools/render_pdf.py` | maintainers | Markdown to PDF through headless Chromium. |
| `REPORT.md` | Flo / Jeremy | What was built, checks run, gaps, terminal state. |

## Printing

`WORKBOOK.pdf` is one booklet. One per student keeps the individual authorship the Pair Reasoning contract asks for.

## Checks you can re-run

```bash
bash week-11/tdd-walkthrough/student/instructor-only/ladder_check.sh      # red/green at all 19 tags, from a clean clone
bash week-11/tdd-walkthrough/student/instructor-only/check_demos.sh       # Step 01-03 demo output matches the record
bash week-11/tdd-walkthrough/student/instructor-only/check_starter.sh     # starter equals the reference before the students add anything
```

All data is made up. No Canvas, no student data. Python 3.9 or newer.

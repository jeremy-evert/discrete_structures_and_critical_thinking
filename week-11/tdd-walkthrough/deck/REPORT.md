# Deck report: Relations in Your Tests (Anna, deck session)

Terminal state: **PARTIAL (first usable deck, 12:00 checkpoint)**. Final update due 4:00 PM CDT.

## What is finished
- `tdd_walkthrough.pdf` (slides, 62 pages) and `tdd_walkthrough_notes.pdf` (large-type speaker notes, one per slide), built by `./build.sh` from `tdd_walkthrough.tex`.
- Order: front matter (legend, why we test, the predict-run-explain loop, "red is normal", 4 glossary slides) then Part 1 idea, Part 2 idea to proposal (filled-in proposal), Part 3 pieces and plan (tikz depends-on diagram, leaves-first order, one slide per piece with bins/boundaries), Part 4 build live (one slide per ladder step 1-19, red/green badge, prompt box, predict question, "what you should see", recovery, common mistake), closing, index (5 slides).
- PRINCIPLE tag (orange, title bar) on every slide showing a lesson principle; PROMPT FOR CLAUDE box (red, monospace) on 23 slides, each naming its `prompts/NN_slug.md`.
- Revision 4 items in this lane: why-we-test slide (smoke alarm / taste test), loop slide, "red is normal" slide, glossary (3 slides, plain-language one-liners), common-mistake line per step, Thursday bridge on the last content slide.

## Checks run (all exit 0)
- `./check_prompts.sh <prompts dir>`: every PROMPT box text equals the `prompt-a`/`prompt-b` block of its prompt file (23 boxes), index_rows.tex matches the slides (38 rows), glossary covers every watched term used on slides.
- Two `pdflatex` passes per PDF, zero Overfull/error lines in either log; every page of the slides PDF viewed as rendered images; two note pages viewed.

## Not finished or not mine
- Student workbook, student-facing prompts and Thursday facilitator page belong to the project session (`anna/dsct-tdd-relations-20261027`); this deck only points to `student/`.
- Fresh-eyes read done (subagent playing a first-year student, 40 findings). Fixed: antisymmetric wording (slide and glossary), partial-order glossary line, hashing sentence, added Glossary 4 (set, function, record, ~, equivalence class, comparator, end-to-end test, design smell, hash, recovery, drift), reworded witness test, `:=`, step 15 mistake box, piece 7 note. Not fixed (left for 4 PM pass): divides/1..12 explanation, worked edit-distance example on the piece 2 slide, 'git' and 'graph' definitions, step-3 green-first and piece 2 carrying two ideas at once.
- Prompt boxes were synced from the project session's working tree; recheck against the pushed tip before class (`./extract_prompts.py <dir>` then `./check_prompts.sh <dir>`).
- Dry-run result per slide prompt is recorded by the project session's report, not here.

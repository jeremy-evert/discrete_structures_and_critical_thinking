# Report: DSCT Week 16 Farkle + ML package (Ivy, run ee5f3c97b9dd2ed8d362972dc69ec4ca)

Terminal state: **COMPLETE pending Sol re-review** (first Sol pass at 096874e returned REPAIR; repairs applied; second Sol pass result recorded in "Sol" below). Not accepted; Anna audits. No Canvas contact, no merge, no student data, synthetic/fallback data only.

Branch `ivy/dsct-w16-farkle-ml-20261103` (pushed), base `origin/main` ee18526. Tip: see the final line.

## Delivered (all under `week-16/farkle-ml-pkg/`)
- `deck/`: 18-page slides + 18-page instructor notes (tectonic build, `build.sh`, `check_prompts.sh`, numbers generated from the fallback CSV), 4 prompts shown verbatim.
- `prompts/` (4), `student/` (handout, concept map, glossary, Thursday activity, recap outline), `canvas/` (manifest for module 218914, 7 pages, prompts page, `validate_manifest.py`), `code/` (stdlib evidence reader + 5 pytest tests, instructor only), `instructor/` (guide, run of show, receipts, this report).

## Checks run (real results)
- `pytest` in `code/`: 5 passed; Sol also ran it from a clean clone and two mutations of `evidence_summary.py` made it fail.
- `deck/build.sh` twice: 18/18 pages both times, overfull/error lines 0/0. `check_prompts.sh` exit 0 (4 prompts, index, numbers).
- `canvas/validate_manifest.py`: VALIDATION OK (unique titles, sources exist, byte-copies, prompts.md = exact concatenation, ZIP = 4 prompt files only, glossary coverage across all student pages and prompts, forbidden-string scan clean).
- Package-wide grep for fleet host names and absolute paths: clean.

## Judgment calls
- **TeX engine**: `pdflatex` absent on maise; `tectonic` (already installed, uses its local cache) builds the beamer deck. Anna's deploy host may differ; PDFs are committed.
- **AI failure mode**: `planning/fall-2026-topic-map.md` has no Week 16 row. Used "a confident reader/AI reports a simulation/ML win while hiding the denominator or ordering criterion, or treats one sample as proof" (see `deck/JUDGMENT_CALLS.md`). Jeremy/Anna should confirm or replace.
- **Decision Gate**: there is no `week-16/student/decision-gate.md`; the existing receipt calls itself "Week 16 Decision Gate" but is its own 5% category. The receipt was not edited; student pages refer to it by assignment name, not repo path.
- **Alternate metric**: no extra numbers are published, so that step is reasoning in words. Real per-metric data would need Jeremy's decision.
- **prompts.md H1**: kept byte-exact concatenation of prompt files, so its first line is "# Prompt 01 ..." not the page title (documented exception in the validator).
- **Fallback fixture**: 3 seeds (17, 6262, 2026), A wins 3/7, 6/4, 8/2 of 10, A-B = -40/+20/+60 pp, range 100, ordering flips; used as the lesson, never to name a winner.
- Fresh-eyes pass: done by a fresh Sonnet reader given only the student pages and prompts; ~60 flags, all fixed in the repair pass or logged above.

## HUMAN_GATE / Anna items
- Receipt route: how the existing assignment `assignments/week-16-farkle-evidence-receipt.md` reaches students in Canvas is not covered by the manifest (it is an assignment, not a page). Anna decides.
- Confirm Week 16 AI failure mode and whether Tuesday should preview the three-row bundle.
- Module id 218914 comes from the contract; Anna verifies against live Canvas.

## Not finished
- No live run of the four prompts through a Claude session.
- Slides were rasterized and spot-checked only by Sol and Luna (not every page by Ivy).
- Thursday deck not built (Thursday is a page, per contract).

## Spend note
Anthropic (Ivy, Claude Code Sonnet): orchestration, commits, one fresh-eyes read. OpenAI (Codex): Terra 1 plan (85,858 tokens), Luna 4 builds/repairs, Sol 2 reviews; Luna and Sol tokens UNMETERED (not captured). Reusable: the W12-derived deck pipeline (now tectonic), `canvas/validate_manifest.py` (week-agnostic apart from the Week 16 prefix; should be generalised), `code/evidence_summary.py`.
Lesson for next week packages: Codex sandboxes cannot write the shared .git (do not put `git fetch` in work files; coordinator does Git), and `codex exec` outside a repo needs `--skip-git-repo-check`.

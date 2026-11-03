# Instructor Guide — Week 16 Farkle + Machine Learning

## Purpose

Week 16 is a two-meeting evidence lesson, not a programming assignment, statistics lecture, or strategy tournament. Students compare the same two fixed strategies, make a predeclared rule, inspect raw counts across a seed bundle, audit a confident interpretation, and write a claim no larger than the evidence.

The student-facing finish line is the existing `assignments/week-16-farkle-evidence-receipt.md`. It is the special 5% **Farkle + ML Synthesis** category, not an ordinary Decision Gate. Students submit it as a graded discussion so peers can inspect the work as a class learning resource.

## Package materials

Use paths relative to `week-16/farkle-ml-pkg/`:

- `deck/farkle_ml_slides.pdf` — Tuesday slides.
- `prompts/` — the four prompt blocks shown verbatim on the slides; `canvas/prompts.md` is their exact concatenation.
- `student/handout.md`, `student/concept_map.md`, and `student/glossary.md` — Tuesday support pages.
- `student/thursday_activity.md` — Thursday workflow and receipt instructions.
- `student/recap_outline.md` — ten post-class recap bullets, five per meeting.
- `../fallback/quick_v1_results.csv` — validated synthetic fallback evidence; use the three rows as supplied.
- `code/` — instructor-only raw-count reader and tests; it does not run the game or import vendor code.

The Canvas manifest publishes the student pages, Tuesday slides PDF, and prompt ZIP only. Do not publish this guide, the run of show, the code, the fallback CSV as a standalone file, notes PDF, or receipts.

## Fixed comparison and instructional reading

The classroom comparison is:

- A: `learner:500`; B: `bank_at_425`.
- Target score: 4000; same classroom rules and opponent setup.
- Ten games per row; five starts for A and five for B.
- Seeds: 17, 6262, and 2026.
- A−B win-rate differences: −40, +20, and +60 percentage points.

The rows intentionally reverse ordering. Do not name A or B as the winner. Use the movement to ask whether a student's own threshold or decision rule survives. The safe conclusion is conditional: it describes these strategies, rules, games, and seed rows, and then names what the model cannot establish.

The week's AI failure mode is a polished interpretation that hides the denominator or ordering criterion, treats one sample as proof, or ignores variation and model limits. Students should repair the interpretation, not reward its confidence.

## Before class

Run the offline package checks from the repository root:

```text
python3 week-16/farkle-ml-pkg/canvas/validate_manifest.py
cd week-16/farkle-ml-pkg/code && pytest
cd ../deck && ./check_prompts.sh
```

The code test is deliberately standard-library-only for the reader itself; `pytest` is the only test runner dependency. The fallback CSV is copied from the course fallback source and must not be hand-edited into nicer-looking numbers.

### Tectonic build note

The deck source is already built in this package. If a deck source changes, run `deck/build.sh` in an environment with the package's configured Tectonic binary; the script also regenerates numeric macros, prompt text, and the slide index, then checks PDF logs for overfull/error lines. It writes `deck/farkle_ml_slides.pdf` and the instructor-only `deck/farkle_ml_notes.pdf`. Do not rebuild merely for this slice: no deck source changed, and no PDF build is claimed here.

## Evidence handling

If live execution is available and already validated, a live row may be shown as an example, but keep the same comparison and preserve raw counts, denominators, starts, and seed identity. If live execution fails or is not appropriate, open the validated fallback CSV and continue the reasoning task. Record the technical failure separately; do not turn class into environment debugging.

Never ask students to write a Farkle engine, implement machine learning, or find a universal best strategy. Do not add formal confidence intervals, p-values, a leaderboard, or a GPU/cloud requirement.

## Assessment emphasis

Reward a precise claim, visible assumptions, raw counts and denominators, a check across rows, an alternate metric considered without changing the rule silently, a model limitation, a repaired interpretation, and a supported defend/revise/refuse decision. Do not reward selecting whichever strategy has the largest row.

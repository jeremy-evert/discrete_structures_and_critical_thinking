# Week 11 decks: Anna report (2026-10-27)

**Terminal state: COMPLETE** (Tuesday review and Thursday deck both built; Canvas untouched; Flo approves upload).
Branch: `anna/dsct-w11-thu-deck-20261027` (from `flo/dsct-w11-tue-deck`, merged with Flo's split-PDF commit a40a7e4). Tip SHA: 6200246 (code commit; this line added in a follow-up commit).

## Files (each deck = slides PDF + separate large-type notes PDF, via `build.sh`)
- `presentations/beamer/week11_tue_relations/` : `.tex`, `week11_tue_relations.pdf` (slides), `week11_tue_relations_notes.pdf`, `build.sh`
- `presentations/beamer/week11_thu_pair_reasoning/` : `.tex`, `week11_thu_pair_reasoning.pdf` (slides), `week11_thu_pair_reasoning_notes.pdf`, `build.sh`
- `scripts/verify_week11_relations_counts.py`, `scripts/verify_week11_thu_pair_reasoning.py` and their outputs `reports/week11_*_verify_output.txt`

## Tuesday review: changes
1. **Fixed** digraph on the divisibility slide: self-loops on 3 and 6 were drawn above the nodes and overlapped the 1-3 and 2-6 arrows; loops now point outward.
2. **Fixed** exit slide: "The individual Pair Reasoning report is due after" replaced with "Follow the Week 11 README for what, if anything, you submit after pairing", because the report category is retired (Decision 029, `docs/grading-model.md`) while `week-11/README.md` still says to submit it.
3. No math errors found: 512 / 16 / 65,536 relations; 5 and 19 (n=3), 15 and 219 (n=4) equivalences/partial orders; divisibility classification; mod-4 puzzle (4 bins of 3, not antisymmetric); both/neither examples. All reproduced by script.
4. No overfull/underfull boxes; all 14 pages rendered and inspected. Notes PDF (14 pages) inspected: one page per slide.

## Thursday deck
18 slides, every slide has speaker notes. Includes: nontransitive dice (A=2,2,4,4,9,9; B=1,1,6,6,8,8; C=3,3,5,5,7,7: each beats the next 20/36 = 5/9, all means 5), prerequisite deadlock (cycle 0 valid orders, chain 1, diamond 2), relation-counts puzzle on 3 elements (512 / 64 reflexive / 64 symmetric / 8 both / 5 equivalence / 19 partial orders), and a worked classifier (R on {1,2,3,4}: reflexive, symmetric, not antisymmetric, not transitive; repair adds (1,3),(3,1), giving bins {1,2,3},{4}) with an optional 5-line Python classifier. Structure follows the run of show.

## Checks run
- `pdflatex` twice per deck (via `build.sh`): no errors, no Overfull boxes (Thursday had three harmless Underfull warnings on the table slide before notes fixes; none visible).
- Every page of both slide PDFs and both notes PDFs rendered to images and inspected.
- All counts/examples: see verify outputs above.

## Flags for Flo (source conflicts, not resolved by me)
1. **Pair Reasoning report is retired** (Decision 029) but `week-11/README.md` and the Tuesday exit slide (original) say to submit it. Decks stay neutral; README likely needs a fix.
2. **Run-of-show timing**: `thursday-run-of-show.md` is titled 75 minutes but its rows end at 1:25. Noted in slide 1 notes.
3. Notes mention Efron-style dice only as a puzzle genre; face values are my own, verified in the script.

## Limits
- Slides are 10pt Beamer/Madrid like Week 10 (small text, much white space); not enlarged for consistency.
- Did not run the deck in front of students; timing is from the run of show only.
- No Canvas writes, no student data, nothing merged to main.

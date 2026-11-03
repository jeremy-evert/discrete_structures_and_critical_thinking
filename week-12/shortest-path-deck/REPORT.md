# Report: DSCT Week 12 shortest-path deck (Anna)

Terminal state: **COMPLETE for the first usable deck (parts 1 to 8 including the code section)**; not accepted, Flo reviews, Jeremy decides class use. Final update due 2:00 PM CST Wed Nov 4.

Branch `anna/dsct-w12-shortest-path-deck-20261103`, pushed to origin. Pushed tip SHA at the time of writing: see "Tip" below (filled in after the final push).

## Finished
- `deck/shortest_path.pdf` (44 pages: title, legend, path, glossary, 35 story and code slides, 4 index slides) and `deck/shortest_path_notes.pdf` (44 large-type note pages), built by `deck/build.sh`. Every slide has speaker notes (what to say, a question, expected answers). Order follows Jeremy's: one-way street, die and 6x6 table, 1-2-3-4-5-6-1 total, greedy and where it is fooled, guess and check, counting (built one step per slide) with linear and log plots, code section, close, Gate preview, exit trace, optional "where this came from" (his one sentence only).
- `data/distances.csv`, `code/tour.py`, `code/test_tour.py`, `scripts/make_numbers.py` (every quoted number becomes a macro in `deck/numbers.tex`, plus four highlighted tables), `scripts/make_figure.py`, `scripts/check_numbers.py`, `prompts/01..06` (8 prompt boxes).

## Checks run (real results)
- `pytest` in `code/`: **8 passed in 0.00s** (asymmetric legs unequal; 1234561 legs and total; greedy tour and total; brute force no worse than greedy and equals the best; count = (n-1)! for n=2..6; guess-and-check best never rises; reverse tour differs).
- `deck/check_prompts.sh`: exit 0 (8 prompt boxes equal their prompt files; index consistent, 34 rows; numbers consistent; Gate text equals `week-12/student/decision-gate.md`).
- `build.sh`: second build identical page count (44 and 44); overfull/error lines slides=0 notes=0. All 44 slide pages rendered and looked at; title/tag overlaps and spacing found and fixed.

## Numbers (computed by committed code)
Tour 1-2-3-4-5-6-1 = 55 (reverse 1-6-5-4-3-2-1 = 56); greedy 1-3-5-2-6-4-1 = 39; best (brute force) 1-5-2-6-3-4-1 = 34 over 120 tours; 15 cities = 87,178,291,200 tours; 24.2 hours at an assumed one million tours per second.

## Judgment calls
- **Invented table.** Searched seeded random 6x6 tables (values 2 to 12) for: all pairs asymmetric, no ties in greedy from city 1, greedy 5 worse than the unique best, natural order worse than greedy. Then changed the (6,5) cell from 12 to 13 because the reverse of the natural tour happened to total exactly 55 as well (a pytest caught it). Greedy loses to the best tour, as required.
- **Counting convention.** Start fixed at city 1, direction matters, (n-1)!; no halving because the table is asymmetric. The n! and halved conventions are stated once.
- **Guess-and-check seed 3114** was chosen (searched) so the five-guess trace is short and the best-so-far drops three times. The prompt tells students to use the same seed so their output matches.
- **Exit-trace prompt.** The Thursday run-of-show has no exit-trace text; its Tuesday run-of-show has "Exit trace" and the Tuesday activity ends "State one bounded conclusion and its edge assumption; keep this trace for the Decision Gate." I used that sentence verbatim and say so in the slide's notes. Flo/Jeremy may want different wording.
- **Base commit.** The work file says base on `origin/main` tip 3c69501 or newer. 3c69501 is on `origin/anna/dsct-concepts-test-first-20261028`, not an ancestor of `origin/main` (9af6129), so I branched from `origin/main`. The Week 11 deck template is not on main; I copied its scripts from the `dsct-tdd-deck` worktree (46ae307), read only. `check_glossary.py` was not carried over (the deck has its own short glossary slide).
- **Authoring.** The work file assigns this deck to Anna directly with a same-day deadline; I wrote it myself and did not route it through Ivy, so there is no Ivy spend this cycle (Anthropic only, no Codex).
- `check_numbers.py` guarantees macro numbers are current and bans bare key totals in the slide sources; hand-work sums in speaker notes are written as words and are not machine-checked.

## Not finished
- No fresh-eyes read as a first-year student (the Week 11 deck had one).
- The six prompts were not dry-run through a live Claude session; the reference code in `code/` is what the slide numbers come from.
- Prompt boxes are small type (7.4 pt, as in Week 11); the notes PDF is large type.
- Not looked at: the notes PDF beyond a build check.

## Tip
Content tip `c583965` (deck, code, PDFs, prompts); this REPORT line was added in the next commit, see `git log` for the final tip.

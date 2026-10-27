# Sandy the Skeptic — DSCT TDD Tuesday demo review

- **review_id:** `sandy-sol-hanna-20261027T1150CDT`
- **role:** Sol / adversarial review (Sandy the Skeptic)
- **review date:** 2026-10-27
- **bounded_scope:** review the Tuesday TDD demo core for simplicity, clarity, excitement, and live reliability; inspect only the DSCT walkthrough inputs; write this receipt only. No Canvas, student data, merge, or changes to Anna/Flo branches.
- **terminal_state:** `COMPLETE` for the noon review slice; final-package pass remains conditional on that package landing by 5:00 PM CDT.

## Input refs

- Work order: `foreman_interface/jobs/tasks/hanna_review_dsct_tdd_tuesday_demo_2026-10-27.md` (run-bound SHA-256 supplied by dispatcher: `52633dce76ae711235dd287cd28ba4d6dcc2eb1fb835eda4d16808945d602795`).
- Review rule: `foreman_interface/spells/sol.md` (Sandy the Skeptic / Sol adversarial review).
- Anna core: `origin/anna/dsct-tdd-relations-20261027` at `4d1b0c69bc02a227661693fd030bca31f6eb4db3c`.
- Ladder: `tdd-step-01` through `tdd-step-19` are present; `tools/ladder_check.sh` checked every tag.
- Deck: `origin/anna/dsct-tdd-deck-20261027` was absent at 11:50 and 12:00 CDT. The core branch has no `week-11/tdd-walkthrough/deck/` directory or deck PDF.
- Comparison materials: `week-11/tdd-walkthrough/STEPS.md`, `prompts/00`–`prompts/14`, `INSTRUCTOR_GUIDE.md`, `STUDENT_HANDOUT.md`, `CONCEPT_MAP.md`, and `REPORT.md` at the Anna core tip.

## Checks attempted

1. Read the stated review lens, criteria, scope, and Sol receipt requirements in the assigned work file and `spells/sol.md`.
2. `git ls-remote https://github.com/jeremy-evert/discrete_structures_and_critical_thinking.git 'refs/heads/anna/dsct-tdd-relations-20261027' 'refs/heads/anna/dsct-tdd-deck-20261027' 'refs/tags/tdd-step-*'` — Anna core and all 19 tags present; deck branch absent. Repeated at 11:50 and 12:00 CDT. SSH `git fetch origin` was attempted first but failed before connecting: `Bad owner or permissions on /etc/ssh/ssh_config.d/30-libvirt-ssh-proxy.conf`; read-only HTTPS ref checks were used instead.
3. Fresh clone of the Anna relations branch under `worktrees/hanna-dsct-tdd-review-20261027`; initial status clean. `week-11/tdd-walkthrough/tools/ladder_check.sh` — all 19 tag outcomes matched their intended red/green status, ending with `tdd-step-19 | 39 passed`.
4. `python3 -m pytest -q week-11/tdd-walkthrough/tests` — `39 passed in 0.16s` on Python 3.12.
5. `make task-check` — unavailable: `make: *** No rule to make target 'task-check'. Stop.`
6. `make check` — unavailable: `make: *** No rule to make target 'check'. Stop.`
7. Blind live rehearsal: a sparse fresh clone exposed only `week-11/tdd-walkthrough/prompts/`; Codex executed the prompt blocks 00 through 14 in order, without access to the reference demos or completed implementation. Runtime was Python 3.9.25. Prompt 00 returned `ready`. Prompts 01–03 produced the requested examples/verdicts. For 04–14, observed phase results were: 04a 12 failed / 04b 12 passed; 05 13 passed; 06a 5 failed / 06b 18 passed; 07 one transitivity failure; 08 22 passed; 09a 3 failed / 09b 25 passed; 10a one symmetry failure / 10b 27 passed; 11a 2 failed / 11b 30 passed; 12a 3 failed / 12b 33 passed; 13a one test-collection error / 13b 36 passed; 14a one cycle failure / 14b 38 passed. Final suite: `38 passed in 0.14s`. Details of the consequential mismatch are in REPAIR-1 below.
8. `find week-11/tdd-walkthrough -maxdepth 2 -type d -name deck -o -type f -name '*.pdf'` — no output. No deck source existed to build, render, or compare against the prompt files.

## Findings

### BLOCK-1 — Required slides and notes deck were not available at the review cutoff

- **Locator/evidence:** no `origin/anna/dsct-tdd-deck-20261027` ref in the 11:50 or 12:00 ref checks; no `week-11/tdd-walkthrough/deck/` directory or PDF in the fresh core clone. `README.md` says the deck is in another session and was due at 12:00.
- **Criterion violated:** the requested Tuesday demo uses slides alongside the live code, slide prompts must match `prompts/NN`, PDFs must compile/render, and Jeremy must be able to teach from the notes PDF. None of those deck checks can be made without the deck.
- **Observed vs expected:** the core branch has the text walkthrough, prompts, and 19-tag ladder; the expected deck branch/build artifact is absent.
- **Smallest next action:** publish the deck branch and built slides/notes PDFs; then compare every pasted prompt against its source prompt and render-check both PDFs. Until then the requested slide-supported class package is not reviewable.

### REPAIR-1 — Prompt 13A can turn the expected three red tests into a collection error

- **Locator/evidence:** `week-11/tdd-walkthrough/STEPS.md:22` says Prompt 13 produces “3 red, then green.” In the blind rehearsal, the plausible test setup put `GRAPH = build_graph(names, records, pipeline)` at module scope (`tests/test_dependencies.py:8`) while the requested stub raises `NotImplementedError`. `pytest` therefore stopped during collection with one error instead of collecting and reporting the three expected failing tests. Prompt 13B then implemented the graph and the suite passed (`36 passed`).
- **Criterion violated:** the red/green outcome should match the step expectation, and a plausible Claude deviation should not leave Jeremy unsure whether the step is working.
- **Smallest bounded repair:** add a clear prompt instruction/test pattern that defers `build_graph(...)` until inside a test, or explicitly label the collection error as an expected red variant and teach the recovery action (`tools/recover.sh 16`). Then rerun the blind prompt 13A/B pair and update the step table to the observed supported outcome.

### REPAIR-2 — The opening hook arrives after the requested first three minutes

- **Locator/evidence:** `INSTRUCTOR_GUIDE.md:39-46` allocates four minutes to the smoke-alarm opening; the timeline starts it at minute 4 (`INSTRUCTOR_GUIDE.md:52`).
- **Criterion violated:** the review asks for a hook in the first three minutes. This opens with an analogy, but delays the concrete surprise that the brief identifies as the strongest hook.
- **Smallest bounded repair:** start in minute 1 with the Jon/John/Jonathan prediction (“If Jon matches John and John matches Jonathan, must Jon match Jonathan?”), then use the failing test as the reveal. Keep the smoke-alarm analogy as the short TDD explanation after the hook.

### POLISH-1 — Step 13 asks beginners to absorb several abstractions in one live step

- **Locator/evidence:** `prompts/13_dependency_order.md:8-24` combines AST parsing, call-graph extraction, graph traversal, dependency ordering, and transitive closure; `INSTRUCTOR_GUIDE.md:94` introduces reading code with `ast`.
- **Criterion at risk:** one new idea per step and first-year readable code. The step's purpose is “what can I test first?”, but the AST implementation can eclipse that concept.
- **Smallest improvement:** make a five-function dependency sketch visible first and ask which node has no prerequisites; keep the AST implementation as an optional extension.

## Dullest five steps, ranked, with sharper replacements

The deck is missing, so these are step-level judgments; slide numbers and slide dullness cannot be ranked yet.

1. **Prompt 13 — Dependency order:** abstract AST + graph machinery makes the student watch code inspect code. Replace the opener with a five-card “who waits for whom?” ordering puzzle; reveal the code graph only after students find the first callable piece.
2. **Prompt 05 — Same-bin checkers:** a large checker implementation passes immediately and offers little visible tension. Replace the opening with “Which score flips grade at 90?”; show 89/90, then name the equivalence property after the boundary prediction.
3. **Prompt 11 — Antisymmetric sort:** comparator and `cmp_to_key` risk turning the story into Python API detail. Put Jon/John cards in both input orders and show the family-name-only sort preserve each order; ask whether the code actually chose between them.
4. **Prompt 12 — Merge pipeline:** “put it together” is a broad label. Give students five sample record cards and ask which records survive and which IDs combine before showing the merge output.
5. **Prompt 14 — Cycle smell:** cycle detection and closure vocabulary are less vivid than the no-first-step result. Have students physically order three dependency cards where each waits on the next; ask them to find the first card, then reveal the cycle error.

## Simplicity and clarity read

- Steps 01–03 provide a concrete progression from pairs to properties to classifications, but Step 01's stated outcome is only “8 pairs, symmetric matrix, arrows” (`STEPS.md:10`); it lacks an explicit pass/fail cue. Add a visible check label (“check passed: 8 directed pairs; matrix mirrors across diagonal”) so Jeremy can point to a result without inventing one.
- The topic sequence is understandable in the guide, but several steps introduce terms rapidly: Step 01 has relation/pairs/matrix/digraph; Step 02 has four properties plus witnesses; Step 13 stacks AST, graph, DFS, dependency and closure. The glossary helps after the fact; present one term at a time with the concrete artifact first.
- Excitement is strongest at Prompt 07's transitivity counterexample and Prompt 10's order-dependent duplicate result. Keep those as the payoff beats. The guide's 75-minute cut does keep the transitivity failure and a symmetry failure, but the deck alignment cannot be checked.
- The blind rehearsal confirms prompts 01–14 can grow a working implementation without the reference. Aside from the Prompt 13A mismatch, all final phase outcomes matched their textual expectations; the independent report's earlier “21 of 23 phases” claim notes two fixes that were not rerun, so the fresh rehearsal is useful evidence but does not substitute for the missing slide comparison.

## Verdict

**Primary verdict: BLOCK** for teaching the requested slide-supported demo at 12:30 based on the 12:00 evidence. The core ladder and prompts work, but the required slide/notes package is absent, so slide-to-prompt fidelity, PDF rendering, and speaker-note readiness are unverified. Prompt 13A also has a credible expected-red mismatch to repair or explain. If Anna's built package lands before class, perform a focused follow-up on prompt parity, PDF render/notes, the opening, and the Prompt 13A recovery guidance before changing the verdict.

**Plain-language summary for Jeremy:** The live coding sequence itself works: all 19 saved checkpoints show the intended red or green test results, and a fresh Python 3.9 run built the project to 38 passing tests. The important counterexample where Jon matches John and John matches Jonathan but Jon does not match Jonathan lands clearly. I would not call the slide-supported demo ready yet because Anna's slides and notes PDF were not in the repository at noon, and the dependency-order step produced a confusing collection error before recovering. If the deck lands, the quickest final check is to compare its prompts with the source prompts, render both PDFs, and give Prompt 13 a reliable red-state recovery cue.

## Reproduction limits and next action

- No deck/notes source or built PDF was available at the 12:00 cutoff, so slide numbers, slide text/prompt parity, PDF compilation/rendering, and the “notes PDF alone” teaching check remain unverified.
- The blind run exercised prompts 00–14 using Codex; it was not a live classroom run with Jeremy, and no Canvas or student-facing system was touched.
- **Next action:** Anna/Flo publish the deck branch and PDFs; run the conditional deck pass by 5:00 PM CDT if it lands. Repair the Prompt 13A collection-error path and the minute-4 hook before treating this as clear for Thursday.

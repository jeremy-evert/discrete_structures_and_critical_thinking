# Sol adversarial review — DSCT Week 16 Farkle ML package

- `review_id`: `sol-dsct-w16-096874e-20261103`
- `role`: Sol / adversarial review (Sandy the Skeptic)
- `verdict`: `REPAIR`
- `terminal_state`: `COMPLETE`

## Input refs

- Delivered result: `096874e61c3321115c1c0259f8179483b09b40e4`, branch `ivy/dsct-w16-farkle-ml-20261103`, package `week-16/farkle-ml-pkg/`.
- Accepted criterion: `<worktree>`, especially lines 36-53.
- Approved plan: `<scratch>`.
- Literal worker inputs: sibling files `luna1_prompt.md`, `luna2_prompt.md`, and `luna3_prompt.md`.
- Prior receipts treated only as claims: `deck/LUNA_RECEIPT.md`, `canvas/LUNA_RECEIPT_2_3.md`, and `instructor/LUNA_RECEIPT_4_5.md`.
- Baseline used for cross-scope checks: `ee18526`.

## Bounded scope

Read-only review of the exact delivered commit and comparison inputs. Runtime attacks used disposable local clones. No writes were made to `<worktree>`, no Canvas contact occurred, and no network was used.

## Attacks or checks attempted

1. Ran package pytest from a clean clone and introduced two independent defects into a disposable copy of `evidence_summary.py`.
2. Built slides and notes twice with Tectonic; independently read page counts and searched logs for Overfull, TeX `!`, and error diagnostics.
3. Ran `deck/check_prompts.sh` and independently byte-compared all four fenced prompt payloads with their slide payload files.
4. Ran `canvas/validate_manifest.py`, then independently parsed manifest paths, compared student/Canvas copies, concatenated prompts, and enumerated an in-memory ZIP.
5. Recomputed wins, rates, differences, extrema, range, and sign flip from `week-16/fallback/quick_v1_results.csv` using `csv.DictReader` rather than package code.
6. Read every student page and extracted the complete slide PDF text; raster-inspected the dense/prompt slides.
7. Searched for winner declarations, Decision Gate invention, recap bullet counts, missing vocabulary, real host names, student identifier patterns, and secret/token patterns.
8. Compared `lessons/vendor`, the existing receipt, and all paths outside the package against `ee18526`.

## Commands or test refs

Representative rerunnable commands:

```sh
git clone --no-hardlinks <worktree> runtime-copy
git -C runtime-copy switch --detach 096874e61c3321115c1c0259f8179483b09b40e4
cd runtime-copy/week-16/farkle-ml-pkg/code && pytest -q
cd ../deck && ./build.sh && ./build.sh && ./check_prompts.sh

python3 week-16/farkle-ml-pkg/canvas/validate_manifest.py
cat week-16/farkle-ml-pkg/prompts/*.md |
  cmp -s - week-16/farkle-ml-pkg/canvas/prompts.md
git diff --name-status ee18526 096874e -- . \
  ':(exclude)week-16/farkle-ml-pkg/**'
git diff --quiet ee18526 096874e -- lessons/vendor
git diff --quiet ee18526 096874e -- \
  assignments/week-16-farkle-evidence-receipt.md
```

Negative controls in `runtime-copy`:

- Changed `win_rate_a = wins_a / games` to `wins_a / (games + 1)`: pytest exited 1 with two failures.
- Changed `sign_flip_detected` to constant `False`: pytest exited 1 at `test_fallback_bundle_rates_range_and_sign_flip`.
- Restored both mutations; pytest returned to `5 passed`, and `git diff --exit-code -- evidence_summary.py` passed.

## Findings

### F1 — HIGH — required alternate-metric work has no published evidence

- Violated invariant: student steps must be executable from the student-facing package; plan slice 4 requires students to ask whether another metric changes the story.
- Evidence: `student/handout.md:100` and `student/thursday_activity.md:48-54` require inspection of average score, Farkle rate, preparation effort, evaluation speed, or simplicity. `canvas/manifest.json:42-53` publishes only the slides PDF and prompt ZIP. `canvas/tuesday_landing.md:3-7` links only the slides. A search across student pages, Canvas pages, prompt files, and deck sources finds definitions but no alternate-metric values or strategy evidence. Those values exist only in the unpublished fallback CSV.
- Observed versus expected: a first-year student cannot complete the required alternate-metric comparison from the published inputs; the expected result is a checkable comparison using supplied evidence.
- Independent basis: this follows from manifest reachability plus a package-wide content search, not a worker receipt or validator claim.
- Smallest repair: publish a student-safe evidence table/file with one or more selected alternate metrics and link it from the relevant pages, or explicitly reframe the step so it can be answered from evidence actually supplied.

### F2 — HIGH — contract-required `instructor/REPORT.md` is absent

- Violated invariant: contract lines 52-53 and plan lines 54-57 and 96-99 require `REPORT.md` with commands/results, judgment calls, tip SHA, unfinished work, terminal state, and Anthropic/OpenAI reuse note.
- Evidence: `test -f week-16/farkle-ml-pkg/instructor/REPORT.md` exits 1. The instructor directory contains only `INSTRUCTOR_GUIDE.md`, `RUN_OF_SHOW.md`, and `LUNA_RECEIPT_4_5.md`.
- Observed versus expected: worker receipts exist, but the coordinator report required for acceptance does not.
- Independent basis: direct tree inspection; receipts cannot substitute for a missing required artifact.
- Smallest repair: add the coordinator report with actual final command results and all required metadata, then rerun Sol because the tip will change.

### F3 — MEDIUM — first-use/plain-language vocabulary rule is incomplete

- Violated invariant: contract lines 38, 43-44 and worker input `luna2_prompt.md:7` require technical terms to be defined at first use.
- Evidence: `sign` is used as a mathematical decision concept in `prompts/03_bundle_stability_check.md:13`, `student/concept_map.md:28,52`, and `student/recap_outline.md:14`, but `student/glossary.md` has no Sign entry and the pages do not define it. `bounded` at `student/concept_map.md:3` and `stability` at `student/recap_outline.md:13` are also undefined. The concept map is ordered before the glossary and has no glossary link.
- Observed versus expected: a first-year reader must infer central abstraction vocabulary; expected is an inline plain-language definition at first use, backed by the glossary.
- Independent basis: direct fresh-eyes reading plus exact term/glossary search; the validator checks only a manually curated handout term list.
- Smallest repair: define these terms inline where first used, add concise glossary entries, and extend validation beyond the current curated handout-only list.

### F4 — MEDIUM — the required existing-receipt link is not a student-reachable link

- Violated invariant: approved plan line 92 says to link to the existing receipt; Thursday must say what to submit.
- Evidence: `student/handout.md:86` and `student/thursday_activity.md:96` render `assignments/week-16-farkle-evidence-receipt.md` as inline code, not Markdown links. The manifest has no page or file route for the receipt.
- Observed versus expected: a Canvas student receives a repository pathname, not a navigable submission target; expected is a publisher-compatible link or published student route.
- Independent basis: source/manifest reachability; no Canvas behavior is assumed.
- Smallest repair: add an authorized publisher-compatible link or manifest route to the existing receipt without rewriting its text.

### F5 — MEDIUM — first-year readers are not told what the two strategies do

- Violated invariant: concrete-before-abstract and plain-language design rules.
- Evidence: `student/handout.md:55-58` and `student/thursday_activity.md:24-27` give only `learner:500` and `bank_at_425`. They never explain the actions those rules take or what `500` means, while `student/thursday_activity.md:58-64` asks students to reason about the learner's state/training and model limitations.
- Observed versus expected: students can repeat supplied labels and examples but cannot independently interpret the compared behaviors; expected is a short concrete description of each rule/model.
- Independent basis: fresh-eyes reading of only the student package.
- Smallest repair: add a short student-facing description of both strategies and the meaning of their parameters, consistent with the source model.

### F6 — MEDIUM — literal package-wide hostname-clean acceptance fails

- Violated invariant: contract line 51 says grep clean for real fleet host names.
- Evidence: `canvas/validate_manifest.py:97` contains `<fleet-host-names>`; `instructor/LUNA_RECEIPT_4_5.md:4,65` contains `<worktree>`. The manifest-reachable student surface is clean.
- Observed versus expected: package-wide grep is nonempty even though student exposure was not found.
- Independent basis: direct tracked-tree grep. The literal worker input itself requested example fleet names in the validator, so this also exposes an input/contract conflict rather than a secret leak.
- Smallest repair: Foreman should either record a narrow accepted exception for validator test vocabulary or replace real host identifiers with non-production fixtures and sanitize environment-specific receipt paths.

### F7 — LOW — prompt Canvas page violates the worker's H1/title rule

- Violated invariant: `luna2_prompt.md:10` says each page's first line is an H1 equal to its manifest title.
- Evidence: manifest title is `Week 16 Tuesday: Farkle Evidence Prompts`; `canvas/prompts.md:1` is `# Prompt 01 — Claim and rule`. `validate_manifest.py:179-185` unilaterally exempts this page and prints the exception as an invariant.
- Observed versus expected: the validator passes a known mismatch; expected is the requested title/H1 equality while retaining exact prompt concatenation.
- Independent basis: direct string comparison, not validator output.
- Smallest repair: make the first prompt file's H1 match the Canvas page title (leaving fenced prompt text unchanged) so exact concatenation and H1 equality can both hold.

## Checks that survived

- Clean-clone package tests: `5 passed`.
- Both mutation attacks failed the tests, proving denominator and sign-flip checks are discriminating.
- Two deck builds: 18 slide pages and 18 notes pages both times; zero Overfull/TeX-`!` diagnostics. `check_prompts.sh` exited 0 and checked four prompts.
- All prompt fenced payloads byte-match the slide payload files and appear once.
- Validator exited 0. Independent checks confirmed seven unique page titles, existing relative sources, five student/Canvas byte matches, exact sorted prompt concatenation, and a four-prompt-only ZIP.
- No instructor guide, run-of-show, report, Luna receipt, judgment-call file, notes PDF, or code path is manifest-reachable. The slide PDF has no embedded files.
- Independent fallback recomputation: seed 17 = 3/7, 30%/70%, -40 pp; seed 6262 = 6/4, 60%/40%, +20 pp; seed 2026 = 8/2, 80%/20%, +60 pp; min -40, max +60, range 100, sign flip true. Student pages and slides agree.
- No winner is asserted as a conclusion; winner language is explicitly presented as a claim to reject/audit.
- No `student/decision-gate.md` exists; the five receipt headings are preserved; recap is exactly five Tuesday plus five Thursday bullets.
- Secret/token, student-identifier, education-email, and Canvas-host scans were clean. No real host name was found on the manifest-published student surface.
- `lessons/vendor`, the evidence receipt, and all paths outside `week-16/farkle-ml-pkg/` are unchanged from `ee18526`.

## Reproduction limits

- No Canvas or generic-publisher execution was attempted, as forbidden by scope. Student reachability conclusions use only manifest/source evidence.
- No roster or protected student data was accessed. The student-name check was limited to identifiers and names present in the supplied material; no student identity was found.
- Tectonic reused the installed local cache. No network was used.
- PDF visual inspection sampled the densest and prompt-heavy slides; complete PDF text was extracted and checked.

## Next action

Return the slice to the Foreman for a bounded repair: supply alternate-metric evidence and a real receipt route; explain strategy behavior; complete first-use definitions; add the required report; resolve the hostname-clean criterion conflict; and correct the prompt-page H1. After a new commit, rerun the same clean-clone tests, build/manifest checks, negative controls as needed, and a fresh Sol pass.

VERDICT: REPAIR input_refs=096874e61c3321115c1c0259f8179483b09b40e4

# Sol adversarial review — DSCT Week 16 Farkle ML package, pass 3

- `review_id`: `sol-dsct-w16-9283c60-pass3-20261103`
- `role`: Sol / adversarial review (Sandy the Skeptic)
- `verdict`: `CLEAR`
- `terminal_state`: `COMPLETE`

## Input refs

- Delivered result: exact commit `9283c60b213ba8a3a6d3eb3f1ae1c1bf200953d1`, branch `ivy/dsct-w16-farkle-ml-20261103`, package `week-16/farkle-ml-pkg/`.
- Accepted criterion: `<worktree>`, specifically **Student-facing contents**, **Design rules**, and **Acceptance test**.
- Approved plan: sibling file `../terra_plan.md`; coordinator substitutions accepted in the dispatch were Tectonic for absent `pdflatex` and the documented confident-reader/AI overclaim fallback because the topic map has no Week 16 row.
- Literal worker inputs: sibling files `../luna1_prompt.md`, `../luna2_prompt.md`, `../luna3_prompt.md`, and `../luna4_prompt.md`.
- Actual output and claims checked: the package tree, all `LUNA_RECEIPT*` files, `deck/JUDGMENT_CALLS.md`, and `instructor/REPORT.md` at the delivered commit. Receipts and report were treated as claims, not proof.
- Prior Sol receipts: `../sol_review_096874e.md` (F1–F7, `REPAIR`) and `../sol_review_dc3f34e.md` (S2-F1–S2-F7, `REPAIR`).
- Additional dispatch evidence: the interrupted review at `6f54513` found that the glossary made a numeric threshold mandatory; commit `9283c60` claims to repair that last inconsistency.
- Cross-scope baseline: `ee18526`.

## Bounded scope

Read-only review of the exact delivered commit. I exported `week-16`, `lessons`, `assignments`, and `planning` with `git archive` into `review-tree/` in this scratch directory and ran every mutation/build there. I made no write to `<worktree>`, did not contact Canvas, did not use student data, and did not use the network. Tectonic reused its installed local cache.

The designated scratch directory is not a Git worktree. The task explicitly required the receipt here and prohibited writes to the source worktree, so this review and its disposable harness are scratch evidence rather than a branch artifact.

## Verdict basis

No acceptance defect survived this pass. The original suite passes, both planted implementation defects are rejected, the deck rebuild is stable, the manifest and independent reachability checks are safe, evidence arithmetic agrees with the source CSV, all fourteen prior findings are fixed or honestly logged under the coordinator's stated decisions, and the final glossary wording no longer contradicts the handout/deck rule.

## Prior-finding disposition

### Pass 1 (F1–F7)

| Finding | Pass-3 disposition | Independent evidence |
|---|---|---|
| F1 alternate-metric work lacked evidence | **Fixed by authorized reframing.** | `student/handout.md:77-81` and `student/thursday_activity.md:51-61` explicitly say no extra values are supplied and require a reasoning-only answer; `instructor/REPORT.md:28` records the choice. |
| F2 `REPORT.md` absent | **Fixed.** | `instructor/REPORT.md` exists and contains delivered files, real test/build results, judgment calls, unfinished work, terminal state, and spend/reuse notes. |
| F3 first-use vocabulary incomplete | **Fixed.** | The handout defines the working vocabulary before use (`student/handout.md:13-37`); Thursday defines its task terms at entry (`student/thursday_activity.md:5-7`); the glossary has 71 unique, alphabetized headings. |
| F4 receipt route unreachable | **Logged, by design.** | Student pages name the assignment and five headings without inventing a URL (`student/handout.md:83-85`, `student/thursday_activity.md:103-107`); `instructor/REPORT.md:34` records publisher routing as Anna's item. |
| F5 strategies unexplained | **Fixed.** | `student/handout.md:54-55` and `student/thursday_activity.md:26-27` explain both strategies and the meanings of 500 and 425 in plain language. |
| F6 package hostname grep failed | **Fixed.** | Independent literal scan across committed text for the named fleet hosts, absolute host paths, and the campus Canvas hostname returned no hits. |
| F7 prompts page H1 conflict | **Logged, by design.** | `canvas/prompts.md` remains the required exact concatenation; the validator documents the exception at `canvas/validate_manifest.py:209-216`, and `instructor/REPORT.md:29` records it. |

### Pass 2 (S2-F1–S2-F7)

| Finding | Pass-3 disposition | Independent evidence |
|---|---|---|
| S2-F1 seed-17 leader reversed | **Fixed.** | `student/handout.md:109-110` now says B led; the table and independent CSV calculation give B 7/10 versus A 3/10. The Canvas copy is byte-identical. |
| S2-F2 Tuesday leaked bundle signs/range before prediction | **Fixed.** | `student/handout.md:28-30` uses unrelated sign/range examples; the prediction occurs at lines 59-63; the handout contains only the seed-17 row at line 73. The three-row table is on Thursday at lines 32-36. |
| S2-F3 numeric threshold contradicted deck/Prompt 01 | **Fixed, including the interrupted-pass glossary issue.** | The handout says a checkable rule *may* include a threshold (`student/handout.md:29`); Thursday accepts a numeric threshold **or other test** (`student/thursday_activity.md:15,18`); the glossary now uses the same optional wording (`student/glossary.md:51-53`); deck and Prompt 01 remain coherent checkable nonnumeric rules. `instructor/REPORT.md:23` logs the choice. |
| S2-F4 first-use/plain-language gaps | **Fixed.** | Fallback fixture is defined inline at `student/handout.md:13` and `student/thursday_activity.md:24`; `benchmark` and bucket jargon are gone; the learner grouping is described in ordinary words at `student/handout.md:54` and `student/thursday_activity.md:26`. |
| S2-F5 report tip chain incomplete | **Fixed by an honest convention.** | `instructor/REPORT.md:5` explains why a committed file cannot contain its own tip SHA, gives the exact readback command, and names the content commit reviewed in pass 2. Current read-only Git establishes the delivered tip as `9283c60b213ba8a3a6d3eb3f1ae1c1bf200953d1`. |
| S2-F6 hostname scan/claim false | **Fixed.** | `instructor/REPORT.md:15` now requests a final rerun instead of claiming an unrun clean result; the independent final scan was empty. The real host name and literal campus host were removed from package text. |
| S2-F7 Predict/Check/Explain inconsistent | **Fixed and logged.** | `deck/part1.tex:63`, the built PDF, handout, and recap all use Predict, Check, Explain; `instructor/REPORT.md:24` records the coordinator's choice against the older contract wording. |

## Attacks and checks attempted

### Exact export and source-control boundaries

```sh
git -C <worktree> archive \
  9283c60b213ba8a3a6d3eb3f1ae1c1bf200953d1 \
  week-16 lessons assignments planning | tar -x -C review-tree

git -C <worktree> diff --stat \
  ee18526 9283c60 -- . ':(exclude)week-16/farkle-ml-pkg/**'
git -C <worktree> diff --quiet \
  ee18526 9283c60 -- lessons/vendor
git -C <worktree> diff --quiet \
  ee18526 9283c60 -- assignments/week-16-farkle-evidence-receipt.md
```

Results: exact commit and named branch matched; target worktree was clean. Both outside-package diff commands produced no entries, and both protected-path `--quiet` checks exited 0. Vendor code and the existing receipt are unchanged from `ee18526`.

### Original tests and non-vacuity controls

```sh
(cd review-tree/week-16/farkle-ml-pkg/code && pytest -q)
```

Result: `5 passed`, exit 0.

Two separate disposable copies of `code/` were mutated:

1. `win_rate_a = wins_a / games` became `wins_a / (games + 1)`.
2. `sign_flip_detected` became constant `False`.

Running `pytest -q` in those copies produced:

- wrong denominator: exit 1, two failures (`test_fallback_bundle_rates_range_and_sign_flip` and the tie-rate assertion);
- removed sign-flip detection: exit 1, one failure at `test_fallback_bundle_rates_range_and_sign_flip`.

The tests therefore discriminate both named plausible defects.

### Deck builds, prompts, and visual surface

```sh
(cd review-tree/week-16/farkle-ml-pkg/deck && ./build.sh)
(cd review-tree/week-16/farkle-ml-pkg/deck && ./build.sh)
(cd review-tree/week-16/farkle-ml-pkg/deck && ./check_prompts.sh)
pdfinfo deck/farkle_ml_slides.pdf
pdfinfo deck/farkle_ml_notes.pdf
rg -n 'Overfull|^!|(^|[^A-Za-z])error:' deck/farkle_ml.log deck/farkle_ml_notes.log
```

Both builds exited 0 and independently reported `slides pages: 18`, `notes pages: 18`, and `overfull/error lines: slides=0 notes=0`. Independent `pdfinfo` read 18 pages for both outputs after each build, and the diagnostic search was empty. `check_prompts.sh` exited 0 with `13` index rows, `16` content slides, generated numbers consistent, and `4` prompt boxes.

Independent extraction confirmed every fenced prompt payload byte-matches its `deck/prompts_txt/NN_a.txt` payload and every `\promptbox{NN}{a}` occurs exactly once. All 16 content frames have one speaker-note block. Raster inspection of the three dense prompt slides (7, 13, and 14) found readable content with no clipping or overlap. `pdfdetach -list` reported `0 embedded files` for the student slide PDF.

### Manifest, byte copies, ZIP, and reachability

```sh
(cd review-tree/week-16/farkle-ml-pkg/canvas && python3 validate_manifest.py)
python3 -B audit_9283c60.py
```

The package validator exited 0 with `VALIDATION OK`. The separate `audit_9283c60.py` does not import the validator and independently established:

- seven unique page titles and every declared source present;
- direct manifest routes are only seven `canvas/*.md` pages, `deck/farkle_ml_slides.pdf`, and `prompts/`;
- local links resolve only to `canvas/glossary.md` and the slide PDF;
- no instructor, code, notes, report, guide, run-of-show, judgment-call, or receipt path is reachable;
- no symlink or PDF attachment adds a hidden route;
- student/Canvas copies byte-match for handout, concept map, glossary, Thursday activity, and recap;
- `canvas/prompts.md` is the exact sorted byte concatenation of the four prompt files;
- a freshly built ZIP contains only the four prompt Markdown files at ZIP root.

### Independent arithmetic and evidence consistency

Using only `csv.DictReader` and integer arithmetic on `week-16/fallback/quick_v1_results.csv` (not `evidence_summary.py`), the audit recomputed:

```text
seed=17   wins=3/7 rates=30.0%/70.0% A-B=-40pp starts=5/5
seed=6262 wins=6/4 rates=60.0%/40.0% A-B=+20pp starts=5/5
seed=2026 wins=8/2 rates=80.0%/20.0% A-B=+60pp starts=5/5
min=-40 max=+60 range=100 sign_flip=True
```

The code fixture byte-matches the fallback CSV. The generated slide macros/tables, built slide PDF, Tuesday row, Thursday table, and recap all agree with these values. Other numbers in the student pages are plainly marked definition/example values (such as the unrelated `8, -2, 5` range example), not claims about the fallback evidence.

### Semantic, readability, and safety attacks

- Winner/best/champion search found only conditional decision rules, narrow row observations, warnings, refusals, or a quoted false claim to audit. No package conclusion names A or B the winner.
- `student/decision-gate.md` does not exist. Student pages contain no invented Decision Gate text; instructor-only references explain the existing special-category receipt.
- The recap contains exactly five Tuesday bullets and five Thursday bullets.
- The glossary contains 71 unique H2 entries and is alphabetized case-insensitively. Manual first-year reading found no remaining blocking unexplained term or confusing executable step: the fallback, strategies, checkable rule, threshold option, rates, alternate-metric reasoning, model limits, critique path, submission headings, and peer visibility are all stated where students need them.
- The Tuesday handout contains only seed 17 and withholds the repeated-row answer until after its rule/prediction step. The full bundle appears on the Thursday page; the deck's Thursday preview occurs after the Tuesday prediction and limited-conclusion sequence.
- Literal package-wide scans found no named fleet host, absolute host path, campus Canvas hostname, email address, private-key marker, AWS/GitHub/OpenAI-style key, or nine-digit identifier. No roster was accessed, so the no-student-name conclusion is based on manual text review and identifier scans, not roster comparison.
- `instructor/REPORT.md` accurately records the H1 and receipt-route exceptions, the Tectonic substitution, the fallback AI failure mode, threshold semantics, Predict/Check/Explain choice, unfinished work, and non-acceptance boundary. Its final-host scan is stated as a required rerun rather than a fabricated completed result; this pass performed that rerun successfully.

## Reproduction limits

- Canvas/publisher execution was forbidden and not attempted. Reachability conclusions use local manifest resolution, link resolution, fresh ZIP construction, symlink inspection, and PDF attachment inspection.
- No roster or protected student dataset was accessed.
- Tectonic used the installed local cache; a cold-cache or alternate-host TeX build was not attempted.
- Visual inspection targeted the three densest prompt slides; the complete PDF was text-extracted and searched, but all 18 pages were not individually raster-inspected at full zoom.
- The shell runner emitted repeated `Failed to create stream fd: Operation not permitted` diagnostics before several commands; the reviewed commands still executed and returned their recorded exit statuses. This was scratch-runner noise, not package output.

## Findings

No reproducible acceptance defect found in the bounded scope.

## Next action

Return `CLEAR` visibly to Flo/Anna for independent owner-side judgment. This review does not accept, merge, publish, or contact Canvas. The receipt-routing, Week 16 AI-failure-mode confirmation, and live module-id verification remain the explicitly recorded Anna/publisher items in `instructor/REPORT.md`; they are not concealed package defects.

VERDICT: CLEAR input_refs=9283c60b213ba8a3a6d3eb3f1ae1c1bf200953d1

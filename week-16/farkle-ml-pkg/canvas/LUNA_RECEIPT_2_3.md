# Luna receipt — slices 2 and 3

Date: 2026-11-03  
Worktree: `ivy/dsct-w16-farkle-ml-20261103`  
Scope: student documents plus Canvas manifest/pages and offline validator under `week-16/farkle-ml-pkg/`

## Commands run and exact outputs

Python syntax check:

```text
python3 -m py_compile week-16/farkle-ml-pkg/canvas/validate_manifest.py
(no output; exit 0)
```

Manifest JSON parse check:

```text
python3 -m json.tool week-16/farkle-ml-pkg/canvas/manifest.json >/dev/null
(no output; exit 0)
```

Byte-match checks:

```text
cmp week-16/farkle-ml-pkg/student/handout.md week-16/farkle-ml-pkg/canvas/handout.md
(no output; exit 0)
cmp week-16/farkle-ml-pkg/student/concept_map.md week-16/farkle-ml-pkg/canvas/concept_map.md
(no output; exit 0)
cmp week-16/farkle-ml-pkg/student/glossary.md week-16/farkle-ml-pkg/canvas/glossary.md
(no output; exit 0)
```

Whitespace check:

```text
git diff --check
(no output; exit 0)
```

Manifest validator:

```text
python3 week-16/farkle-ml-pkg/canvas/validate_manifest.py
manifest JSON: OK
metadata: week=16 module_id=218914 module_name_contains='Week 16'
pages: 5 unique titles; sources present
page H1s: OK for all pages except exact-concat prompts.md (documented invariant)
files: 1 source(s) present and linked
zips: 1 directive(s); temporary prompt ZIP members:
  01_claim_and_rule.md
  02_initial_sample_audit.md
  03_bundle_stability_check.md
  04_repair_an_overclaim.md
byte matches: handout.md, concept_map.md, glossary.md; prompts.md exact concatenation
glossary coverage: OK (47 checked terms; terms present in handout checked)
forbidden-string scan: clean (12 student-facing markdown files)
VALIDATION OK
exit 0
```

The validator creates the prompts ZIP in a temporary directory only; no ZIP was written into the package.

## Files created

Student-facing source documents:

- `student/handout.md`
- `student/concept_map.md`
- `student/glossary.md`

Canvas files:

- `canvas/manifest.json`
- `canvas/tuesday_landing.md`
- `canvas/handout.md` — byte-identical to `student/handout.md`
- `canvas/concept_map.md` — byte-identical to `student/concept_map.md`
- `canvas/glossary.md` — byte-identical to `student/glossary.md`
- `canvas/prompts.md` — exact sorted concatenation of the four prompt files
- `canvas/validate_manifest.py`
- `canvas/LUNA_RECEIPT_2_3.md`

The manifest points to the existing `deck/farkle_ml_slides.pdf` and requests `farkle_ml_prompts.zip` from `prompts/`. It has five unique Tuesday pages and no Thursday or recap entries.

## Content checks covered

The handout includes concrete-before-abstract explanations, a race analogy for why a criterion comes before a metric, the predict/check/explain loop, all five receipt headings, peer-visible graded-discussion language, the confident reader/AI denominator-and-ordering-criterion failure mode, and the worked seed/count rows 17 (3/7), 6262 (6/4), and 2026 (8/2), each out of 10. It does not declare a strategy winner or ask students to write an engine or ML algorithm.

The validator checks JSON shape, module metadata, source existence, unique title prefixes, forbidden manifest paths, page H1s, byte matches, exact prompt concatenation, temporary ZIP membership, glossary coverage, and forbidden host/token/key patterns without contacting Canvas.

## Not done or intentionally deferred

- `thursday_activity.md` and `recap_outline.md` were not created, as requested for slice 4; the current manifest does not reference them. The validator accepts future Thursday pages when their files and manifest entries are added.
- No Canvas contact, publish, upload, Git add/commit/fetch, student data, or Decision Gate rewrite occurred.
- Exact prompt concatenation and the page-title prefix rule conflict for `canvas/prompts.md`: the protected first prompt begins with `# Prompt 01 — Claim and rule`, while the manifest title must begin `Week 16 Tuesday:`. The validator preserves the required byte-exact concatenation and documents this one H1 exception; all other current Canvas pages have a first H1 exactly equal to their manifest title.

# Terra/Penny plan — DSCT Week 13 trees package

Plan ID: `terra-dsct-w13-trees-20261103-v1`  
Role: Terra / planning and reconnaissance  
Readiness: `READY_TO_PROPOSE`; Luna still requires coordinator approval.  
Terminal state: `PLAN_ONLY`; no files were written.

Preflight passed:

- `origin/main`: `ee18526`
- Branch: `ivy/dsct-w13-trees-20261103`
- Worktree clean
- `pdflatex` is absent; `/home/jevert/.local/bin/tectonic` is available.
- Use cached `tectonic --only-cached --reruns 1`; do not create a `pdflatex` shim.
- No Canvas, student data, or network beyond the required `git fetch origin`.

## 1. Luna slice list

| Slice | Exact files | Acceptance check | Traps |
|---|---|---|---|
| 1. Reference code and tests | `week-13/trees-pkg/code/trees.py`, `test_trees.py`, `pytest.ini` | `cd week-13/trees-pkg/code && python3 -m pytest -q` → zero failures. Trace assertions must equal the answers below; audit test must report `{("requirements", "tests")}`. | Ambiguous edge direction; unstable child order; BFS accidentally implemented as DFS; treating containment as dependency. |
| 2. Classroom prompts | `prompts/01_project_graph.md` through `07_explain_limit.md` | Parse every file and confirm one `prompt-a` block, optional `prompt-b`, no empty blocks, exact slugs, and 10 total prompt blocks. | Prompt text drifting from slides; prompts asking for real data; AI allowed to edit tests; failure mode omitted. |
| 3. Deck content | `deck/preamble.tex`, `trees.tex`, `part0.tex`–`part6.tex` | `rg -n 'PRINCIPLE:|PREDICT|What you should see|promptbox' deck/part*.tex` → every instructional step has a principle tag, prediction, visible result, and prompt where applicable. | Too many ideas per slide; answers without model assumptions; notes accidentally becoming student content. |
| 4. Deck pipeline | `deck/build.sh`, `check_prompts.sh`, `extract_prompts.py`, `gen_index.py`, `check_glossary.py`, generated `prompts_txt/*`, `index_rows.tex` | `cd deck && ./check_prompts.sh` → exit 0; `./build.sh` twice → identical page counts, `trees_slides.pdf` and `trees_notes.pdf`, zero `Overfull`/TeX error lines. Build must use cached Tectonic only. | W12 assumes `pdflatex`; non-deterministic generated files; prompt line-ending changes; notes PDF included in manifest. |
| 5. Student reference material | `student/handout.md`, `concept_map.md`, `glossary.md`, `tuesday_activity.md`, `decision-gate.md` | `cmp -s student/decision-gate.md ../../student/decision-gate.md` → success. `rg` confirms first-use definitions, peer visibility, and no private-data examples. | Rewriting the Decision Gate; copying instructor answers into student pages; missing Week 12 vocabulary continuity. |
| 6. Thursday and recap | `student/thursday_activity.md`, `student/recap_outline.md`, `instructor/INSTRUCTOR_GUIDE.md` | `grep -cE '^- ' student/recap_outline.md` → 10 bullets. `rg -n 'Decision Gate|Pair Reasoning report|peers|missing edge|cross-link'` → required mappings present. | Thursday becoming a divided-labor exercise; report duplicated instead of mapped; recap not correlated to slides. |
| 7. Canvas package and validator | `canvas/manifest.json`, `canvas/validate_manifest.py`, `canvas/tuesday_landing.md`, `canvas/prompts.md` | `python3 canvas/validate_manifest.py` → manifest valid, all sources exist, titles unique, no instructor paths, ZIP builds, prompt bytes match. | Including `code/`, notes, reports, or instructor files; prompt page paraphrasing; live Canvas lookup. |
| 8. Evidence report | `instructor/REPORT.md` | `git diff --check` → no output; package checks recorded with real results; report contains tip SHA, judgment calls, unfinished items, terminal state, and Anthropic/OpenAI spend note. | Claiming tests ran when they did not; omitting known limitations; pushing or merging without authorization. |

## 2. Concrete content spine

### Synthetic dependency graph

Use seven vertices. A directed edge `A → B` means “A must be completed before B.”

Vertices:

`project, plan, build, requirements, design, tests, docs`

Edges:

```text
project → plan
project → build
plan → requirements
plan → design
build → tests
build → docs
requirements → tests   # the one cross-link
```

Directory-style tree:

```text
project
├── plan
│   ├── requirements
│   └── design
└── build
    ├── tests
    └── docs
```

The tree preserves six edges and drops exactly one dependency:

```text
requirements → tests
```

Exact traces, with children visited left-to-right:

```text
preorder:
project, plan, requirements, design, build, tests, docs

postorder:
requirements, design, plan, tests, docs, build, project

breadth-first:
project, plan, build, requirements, design, tests, docs
```

`inorder` is intentionally not used: it is defined for binary-tree conventions, while this is a general rooted tree.

### Decision tree

Reuse the Tuesday activity exactly:

```text
Start
└── eligible?
    ├── yes → needs aid?
    │          ├── yes → aid route
    │          └── no  → standard route
    └── no  → explain rule
```

The original intake note adds a relationship not represented in the tree:

```text
aid route → language-access review
```

Therefore the tree does not justify:

> “Everyone routed to aid can use the aid route immediately.”

The missing condition may need to become a node:

```text
aid route → language-access review → usable aid route
```

or remain an explicit limitation. Do not rewrite `decision-gate.md`.

Displayed decision-tree traces, using the same child order:

```text
preorder:
Start, eligible?, needs aid?, aid route, standard route, explain rule

postorder:
aid route, standard route, needs aid?, explain rule, eligible?, Start

breadth-first:
Start, eligible?, needs aid?, explain rule, aid route, standard route
```

### Silent-edge test

The reference code must compare original graph edges with tree parent-child edges:

```text
tree_edges =
{
  project→plan,
  project→build,
  plan→requirements,
  plan→design,
  build→tests,
  build→docs
}

dropped_edges = graph_edges - tree_edges
expected:
{requirements→tests}
```

The test should fail if an AI-generated hierarchy reports no missing relationship, and pass only when the audit names the dropped edge.

## 3. Prompt list

Seven files, ten total prompt blocks:

1. `01_project_graph.md`
   - `prompt-a`: model the seven-node synthetic dependency graph and print vertices/edges.
   - `prompt-b`: add tests for the exact edge set; do not edit tests later.

2. `02_directory_tree.md`
   - `prompt-a`: convert the graph into the fixed directory-style tree while stating that tree edges mean containment.
   - `prompt-b`: test root, parent uniqueness, node coverage, and acyclicity.

3. `03_traversals.md`
   - `prompt-a`: implement preorder, postorder, and breadth-first traversal.
   - `prompt-b`: assert the exact traces above.

4. `04_decision_tree_aid_language.md`
   - `prompt-a`: model the Tuesday eligibility/aid/language-access scenario and trace eligible-plus-aid.
   - `prompt-b`: test the route and identify the missing language-access relationship.

5. `05_audit_cross_link.md`
   - `prompt-a`: compare graph edges with tree edges and report `requirements → tests`.
   - `prompt-b`: add the regression test. Explicitly warn that a clean hierarchy can erase a relevant relation.

6. `06_search_claim_check.md`
   - `prompt-a`: test a search claim against all seven nodes and a missing-node edge case.
   - `prompt-b`: assert that the tree cannot support the stronger “all dependencies preserved” claim.

7. `07_explain_limit.md`
   - `prompt-a`: run the complete suite and print traces, dropped edges, and one bounded conclusion.
   - No `prompt-b`.

Every prompt must use synthetic data, retain the Predict → Run → Explain loop, and include the AI failure mode where relevant.

## 4. Deck outline

Target: approximately 36–40 slides, including title, glossary, prompt slides, closing, and index. Use Madrid Beamer, 16:9, with W12’s orange `PRINCIPLE` tags and separate instructor notes.

- `part0`: title, Week 12 continuity, question, slide legend, glossary.
- `part1`: project graph, vertex/edge meanings, dependency interpretation.
- `part2`: graph-to-tree conversion and the exact dropped cross-link.
- `part3`: preorder, postorder, breadth-first; one trace error and correction.
- `part4`: Tuesday eligibility/aid decision tree and language-access omission.
- `part5`: code prompts 01–07, each following predict-run-explain.
- `part6`: audit table, bounded conclusion, Decision Gate preview, Thursday bridge.
- `index_rows.tex`: generated principle/prompt index.

Principle tags should include:

`MODEL VS PROCEDURE`, `EDGE MEANING`, `TREE STRUCTURE`, `TRAVERSAL`, `CHECK THE WORK`, `HIERARCHY LIMIT`, `DECISION RULE`.

The continuity sentence to retain:

> A correct procedure on the wrong model is still wrong.

## 5. Manifest page list and validator

Manifest:

```json
{
  "week": 13,
  "module_id": 218912,
  "module_name_contains": "Week 13",
  "pages": [
    {"title": "Week 13 Tuesday: Trees, Search & Decision Structures", "source": "canvas/tuesday_landing.md", "after": "overview"},
    {"title": "Week 13 Tuesday: Activity — Model, Trace & Audit", "source": "student/tuesday_activity.md"},
    {"title": "Week 13 Tuesday: Handout", "source": "student/handout.md"},
    {"title": "Week 13 Tuesday: Concept Map", "source": "student/concept_map.md"},
    {"title": "Week 13 Tuesday: Glossary", "source": "student/glossary.md"},
    {"title": "Week 13 Tuesday: Claude Prompts", "source": "canvas/prompts.md"},
    {"title": "Week 13 Thursday: Pair Reasoning — Search Claims Need an Audit", "source": "student/thursday_activity.md"},
    {"title": "Week 13 Thursday: Decision Gate — A Tree That Earns Its Conclusion", "source": "student/decision-gate.md"},
    {"title": "Week 13 Thursday: Recap Outline", "source": "student/recap_outline.md"}
  ],
  "files": [
    {
      "name": "trees_slides.pdf",
      "source": "deck/trees_slides.pdf",
      "page_link_from": "Week 13 Tuesday: Trees, Search & Decision Structures"
    }
  ],
  "zips": [
    {"name": "trees_prompts.zip", "from_dir": "prompts"}
  ]
}
```

`canvas/validate_manifest.py` must:

- load valid JSON;
- require unique page titles;
- require every title to begin with `Week 13 Tuesday:` or `Week 13 Thursday:`;
- require every source, PDF, and prompt directory to exist;
- reject `instructor/`, `INSTRUCTOR_GUIDE`, `REPORT`, `code/`, and `*_notes.pdf`;
- build and test `trees_prompts.zip` in a temporary directory;
- require `canvas/prompts.md` to equal the lexically ordered prompt-file bytes joined with the one documented separator, byte for byte;
- require `student/decision-gate.md` to equal the source Decision Gate byte for byte.

## 6. Risks, non-goals, and cuts

Risks:

- A tree may silently change edge meaning from “dependency” to “containment.”
- Traversal answers depend on frozen child order.
- The decision split may look complete while omitting language access.
- Prompt text may diverge from slide prompt boxes.
- Tectonic may attempt package downloads unless `--only-cached` is used.
- Instructor notes, reference code, or reports may leak into the manifest.
- Fresh-eyes review may reveal undefined terms or overbroad claims.

Non-goals:

- No Canvas access or publishing.
- No live Canvas module verification.
- No merge to `main`.
- No real student, employee, health, admissions, or financial data.
- No rewrite of the existing Decision Gate.
- No new infrastructure or external dependencies.
- No redesign of the Week 12 graph vocabulary.

If time runs short, cut in contract order:

1. Keep Tuesday deck and prompts.
2. Keep handout, concept map, and glossary.
3. Keep manifest, pages, and validator.
4. Keep Thursday activity.
5. Keep recap outline.
6. Perform and document fresh-eyes review.

## 7. Acceptance checklist mapped to the contract

- [ ] `code/` pytest passes from a clean clone; intended red tests are labeled.
- [ ] `deck/check_prompts.sh` exits 0.
- [ ] Two builds produce identical page counts.
- [ ] Slides and notes contain zero overfull/error lines.
- [ ] Fresh-eyes review sees only student pages; every unexplained-term flag is fixed or logged.
- [ ] Manifest validates all sources, unique titles, no instructor paths, ZIP creation, and byte-exact prompt coverage.
- [ ] Grep is clean for fleet host names, student names/IDs, and secrets.
- [ ] `REPORT.md` records commands, real outputs, judgment calls, tip SHA, unfinished work, and terminal state.
- [ ] REPORT includes Anthropic-versus-OpenAI spend/reuse note.
- [ ] No Canvas, merge, student data, or unapproved external action occurred.

The branch remains `ivy/dsct-w13-trees-20261103` as an unmodified planning worktree; no implementation, commit, push, or cleanup was performed.
# Prompt 012 — Drop ZyBooks, no required textbook (DSCT)

## Reconciliation

As of 2026-08-15, DSCT has no required textbook or external course for Fall
2026. The prior ZyBooks identifier, URL, release, chapter list, and section
decisions are retained only as historical provenance.

## Files changed

| File | Why changed |
|---|---|
| `course_metadata.yaml` | Replaced the operational ZyBooks adoption with an explicit no-required-textbook/no-required-external-course status while preserving the identifier, URL, release, chapter list, and prior decision as historical provenance. |
| `planning/fall-2026-topic-map.md` | Reframed historical ZyBooks families and section decisions as provenance; renamed only the textbook-framing column. No week, topic, or dependency content changed. |
| `planning/week-01-source-map.md` | Replaced the Week 1 ZyBooks-reading statement with the current no-required-textbook status. |
| `planning/fall-2026-course-design.md` | Marked the former ZyBooks-driven blueprint, section menu, configuration, and vendor question as historical/superseded; preserved its pedagogical and structural record. |

## ZyBooks grep inventory

The case-insensitive search covered `course_metadata.yaml`, `docs/`,
`planning/`, `lessons/`, and `assignments/`.

| File | Disposition | Reason |
|---|---|---|
| `course_metadata.yaml` | Changed | It contained the operational identifier, URL, and ZyBooks-first strategy. Those facts are now explicitly historical, with the current no-required-textbook status stated plainly. |
| `planning/fall-2026-topic-map.md` | Changed | Its source-family framing could imply a current textbook spine. It now identifies those families and decisions as historical provenance only. |
| `planning/week-01-source-map.md` | Changed | Its Week 1 reading statement now reflects the course-wide no-required-textbook status. |
| `planning/fall-2026-course-design.md` | Changed | It described a required ZyBooks path, linked selections, and a lean required configuration. Those are now clearly historical and superseded. |
| `planning/zybooks-section-decisions.csv` | Left unchanged | It is the preserved historical section-decision record referenced by the reconciled planning files. Altering its rows would change source/section decision data rather than textbook framing. |
| `docs/` | No hits | No ZyBooks/zybook references found. |
| `lessons/` | No hits | No ZyBooks/zybook references found. |
| `assignments/` | No hits | No ZyBooks/zybook references found. |

## Scope confirmation

No grading weights, assignment structure, weekly topics, dates, dependencies,
or other spine content were changed. In the active Fall 2026 topic map, only
textbook framing and the label of the historical-source column changed.

## Validation

- `git diff --check`: passed.
- `pytest -q`: passed; 0 tests collected and 0 tests run (`no tests ran in
  0.03s`).

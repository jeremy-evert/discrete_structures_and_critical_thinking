# Prompt 305 — DSCT Reasoning vocabulary inventory

## Scope and starting state

- Starting commit: `797819e3962ec8b240993a8b62d72b2a30fee769`.
- Scope: DSCT vocabulary archaeology only. No course-source, grading, planning, lesson, Canvas, or Savnac artifact was changed.
- Sibling lookups: none. DSCT's own grading model explains A3/A4/A7 as inherited-equivalent category labels sufficiently for this inventory; broad shared-artifact provenance belongs to Prompt 309.

## Search coverage

The following exact search family was run against the whole DSCT checkout and, in focused passes, against current source and historical/provenance surfaces:

```bash
rg -n -i -C 2 -e 'Reasoning Odyssey' -e 'Coding Odyssey' -e 'Reasoning Quest' -e 'Reasoning Gate' -e 'World Bible' -e 'weekly reinforcement' -e 'weekly write-up' -e 'checkpoint' -e 'evidence receipt' -e 'reflection' -e 'Pair Reasoning' -e 'Pair Programming' -e 'Show & Tell' -e 'A3' -e 'A4' -e 'A7' .
rg -l -i -e 'Reasoning Odyssey' -e 'Coding Odyssey' -e 'Reasoning Quest' -e 'Reasoning Gate' -e 'World Bible' -e 'weekly reinforcement' -e 'weekly write-up' -e 'checkpoint' -e 'evidence receipt' -e 'reflection' -e 'Pair Reasoning' -e 'Pair Programming' -e 'Show & Tell' -e 'A3' -e 'A4' -e 'A7' planning docs assignments rubrics lessons week-01 week-02 week-16 sidecar/reports sidecar/raw
rg -n -i -C 2 -e 'Reasoning Odyssey' -e 'Coding Odyssey' -e 'Reasoning Quest' -e 'Reasoning Gate' -e 'World Bible' -e 'weekly reinforcement' -e 'weekly write-up' -e 'checkpoint' -e 'evidence receipt' -e 'reflection' -e 'Pair Reasoning' -e 'Pair Programming' -e 'Show & Tell' -e 'A3' -e 'A4' -e 'A7' assignments planning week-01 week-02 week-16 docs/grading-model.md docs/curriculum/course-sequence.md docs/philosophy/teaching-patterns.md
```

Inspected source families:

| Family | Result |
|---|---|
| `planning/` | Current calendar, weekly chassis, topic map, Week 1/16 plans, and historical design blueprint inspected. |
| `docs/` | Current grading model plus curriculum/philosophy/history documents inspected. |
| `assignments/` | All reusable artifact templates inspected. |
| `rubrics/` | Directory does not exist. |
| Student-facing source | `week-01/`, `week-02/`, and `week-16/` inspected; `lessons/` was also searched. |
| `sidecar/reports/` and `sidecar/raw/` | Prompt 304 evidence, Week 16 reports, the 2026-08-16 design dump, and the 2026-08-17 decision pile inspected as provenance, not doctrine. |

## Object-level vocabulary matrix

| Term / object | Representative paths | Status | Apparent action / artifact | Gradebook / persistence / participation | Same-work relation and confidence |
|---|---|---|---|---|---|
| Reasoning Odyssey | `week-01/README.md`; `docs/grading-model.md:23-24`; `planning/fall-2026-weekly-architecture.md` | Current | Semester-long frame for inspectable reasoning across proofs, models, code, and evidence. | Names the 30% weekly-gate and 15% checkpoint family; persistent. Individual evidence is implied. | May be the umbrella for gate, receipt, write-up, and World Bible. **HIGH** that it is the current course identity; **MEDIUM** on its exact artifact boundary. |
| Weekly reinforcement / Reasoning Odyssey gate | `docs/grading-model.md:23,67-75`; `week-02/student/week-02-evidence-assignment.md:27-33`; `planning/week-16.md:89-97` | Current | Submit the week's substantive evidence using the five-part method. | Explicit 30% semester category; recurring; individual. | Likely the weekly evidence-package function; may overlap/alias `weekly write-up` and `evidence receipt`. **MEDIUM** because the student-facing label is unsettled. |
| Reasoning Odyssey checkpoints | `docs/grading-model.md:24,71-72,82` | Current but underspecified | Larger Odyssey evidence package. | Explicit 15% category; persistent/periodic; individual. | Distinct from weekly gate in weight/scale, but locations and exact artifact are unchosen. **MEDIUM**. |
| Five-part reasoning method / weekly problem-solving write-up | `week-01/student/reasoning-method.md`; `assignments/weekly-problem-solving-writeup.md` | Current method; template has historical basis | Sources, Rules/Assumptions, Work, Check, One-Sentence Summary. | No independently stated gradebook object; reusable individual artifact. | Same functional shape as Week 16 receipt and likely the gate package. **HIGH** on function; **MEDIUM** on whether `write-up` is the final object name. |
| Evidence receipt | `planning/fall-2026-weekly-architecture.md:54-65`; `assignments/week-16-farkle-evidence-receipt.md`; `week-02/instructor/thursday-run-of-show.md` | Current | Individual, inspectable evidence trail; Week 16 requires sources, assumptions, work, check, and conclusion. | May sit inside a weekly gate; individual; recurring/event-specific depending source. | **OVERLOAD**: generic individual trail, Week 16 assignment, and Thursday exit/critique evidence all use the name. **HIGH** that function recurs; **MEDIUM** on object boundaries. |
| World Bible | `planning/fall-2026-weekly-architecture.md:40-54`; `week-02/student/week-02-evidence-assignment.md:44-45`; raw design dump | Current direction, not operationally authored | Optional carried world/system/context that can make a claim or model meaningful. | Explicitly optional and ungraded in Week 2; persistent if used; individual. | Candidate persistent record inside the Odyssey; literal cross-course carry-forward and cadence are unresolved. **MEDIUM**. |
| Pair Reasoning / Pair Reasoning report (A3 equivalent) | `assignments/pair-reasoning-report.md`; `docs/grading-model.md:16,59-65`; `planning/fall-2026-topic-map.md` | Current | Pair artifact; reusable report records roles, evidence, win, stuck point, and next step. | A3-equivalent 5% category; recurring selected weeks; pair work with individual submission language in grading model. | Social challenge mode; its exact reflection/accountability form remains unresolved. **HIGH** on name and rotation; **MEDIUM** on report-versus-individual evidence relation. |
| Show & Tell / Show-and-Tell reflection (A4 equivalent) | `assignments/show-and-tell-artifact.md`; `docs/grading-model.md:17,60-65`; Week 2 Thursday run-of-show | Current | Public explanation/defense, peer questions, critique, revision. | A4-equivalent 5% category; recurring selected weeks. | Social/public mode. Relation to separate A7 feedback object is a gradebook seam. **HIGH** on mode; **MEDIUM** on final artifact contract. |
| Friday feedback report (A7 equivalent) | `docs/grading-model.md:18,60-61`; raw design dump | Current category name, no current template found | Individual critique/revision/evidence feedback connected to Show & Tell weeks. | A7-equivalent 5% category; recurring selected weeks. | May duplicate the critique/evidence-receipt function or be intentionally distinct peer feedback. **LOW** because source lacks a current student-facing template/contract. |
| Event reflections (Wacky Wednesday, Fun Friday, final) | `docs/grading-model.md:14-15,25`; `planning/fall-2026-spine.md:26`; `assignments/project-and-final-reflection.md` | Current categories plus historical template | Reflection on Professional Minds strands or final course closeout. | Three distinct 5% categories/families; event-specific; individual. | **OVERLOAD**: `reflection` names several unrelated functions, not one artifact family. **HIGH**. |
| Week 2 Evidence Portfolio | `week-02/student/week-02-evidence-assignment.md`; `week-02/student/week-02-evidence-rubric.md` | Current / authored | 40-point local-AI readiness and container evidence bundle with reflections. | States it is recurring weekly work and is inside the 30% Odyssey-gate category; individual portfolio from pair-capable work. | **GRADEBOOK-SEAM** and **DUPLICATE-HOMEWORK RISK**: called “not a Reasoning Odyssey write-up” while occupying the Odyssey-gate category and described with the 45% write-up split. **HIGH** on contradiction. |
| Coding Odyssey / coding-odyssey | `docs/curriculum/course-sequence.md:16`; `assignments/project-and-final-reflection.md:3`; raw design dump | Historical / provenance | Historical coding/project continuity framing. | Historical, no current DSCT category. | **STALE-LEGACY**: replaced in direction by Reasoning Odyssey; preserved in history. **HIGH**. |
| Reasoning Quest | Raw design dump and decision pile only | Proposed / unresolved | Candidate weekly individual evidence package. | No current gradebook object or template. | Potential alias of Gate / weekly write-up / receipt. **LOW**. |
| Reasoning Gate | Raw design dump and decision pile only; `docs/grading-model.md` uses lowercase “gate” | Proposed / ambiguous | Candidate weekly individual evidence package; lowercase current category may be its antecedent. | Current category says “Reasoning Odyssey gate,” but no named student-facing Gate object. | **ALIAS/UNRESOLVED** with Quest and weekly gate. **LOW**. |
| Programming exam | `assignments/programming-exam.md`; `docs/grading-model.md:76-78` | Stale legacy / deliberately unused | Historical focused computational assessment template. | Explicitly not a current grade category. | **STALE-LEGACY**; no action needed here. **HIGH**. |

## Name versus function

| Name currently used | Function the source appears to require |
|---|---|
| Reasoning Odyssey | The semester-long frame that makes a student's reasoning visible over time. |
| Weekly reinforcement / Reasoning Odyssey gate | A recurring individual package proving the week's technical reasoning. |
| Weekly write-up | The reusable five-part structure for making a solution inspectable. |
| Evidence receipt | A traceable record of sources, assumptions, work, checking, and conclusion; sometimes an exit/critique record. |
| Checkpoint | A larger periodic Odyssey evidence package, distinct in weight but not yet in concrete form. |
| World Bible | Optional persistent context/record that can make claims and models continuous across weeks. |
| Pair Reasoning | Pair-based intellectual challenge through an artifact; code may be an instrument. |
| Show & Tell | Public explanation/defense plus critique/revision. |
| A3 / A4 / A7 | Legacy-equivalent gradebook labels for Pair Reasoning, Show & Tell reflection, and feedback respectively. |
| Reflection | Several non-equivalent functions: Professional Minds response, social/peer revision account, Week 2 evidence interpretation, or final closeout. |
| Reasoning Quest / Reasoning Gate | Candidate student-facing name(s) for the weekly individual evidence function; not frozen. |
| Coding Odyssey | Historical coding-centered continuity framing. |

## Collision classes

- **ALIAS:** `weekly reinforcement / Reasoning Odyssey gate`, `weekly write-up`, and `evidence receipt` all point toward the recurring individual evidence function, but source does not state whether they are one artifact, a category plus artifact, or separate layers.
- **ALIAS / UNRESOLVED:** `Reasoning Quest` and `Reasoning Gate` appear only as candidate names in provenance; neither can safely be declared canonical or distinct.
- **OVERLOAD:** `reflection` covers Professional Minds, Pair/Show social revision, Week 2 technical interpretation, and final reflection; it cannot serve as a precise object name without a qualifier.
- **OVERLOAD:** `evidence receipt` means a generic trail, a Week 16 assignment, and a Thursday critique/exit component.
- **DUPLICATE-HOMEWORK RISK:** The weekly gate may include the active Thursday artifact, while Pair Reasoning, Show & Tell reflection, and A7 feedback are separately weighted categories. The source says pair work should not create a second Odyssey grade, but the operational object boundary is not yet explicit.
- **DUPLICATE-HOMEWORK RISK / GRADEBOOK-SEAM:** Week 2 says its portfolio is not a Reasoning Odyssey write-up yet places it inside the Reasoning Odyssey-gate category and invokes the 45% write-up split.
- **STALE-LEGACY:** Coding Odyssey, Pair Programming historical references, and the unused programming-exam template remain provenance, not current doctrine.
- **GRADEBOOK-SEAM:** A3/A4/A7 category names and the separate 30% gate / 15% checkpoint categories cannot be renamed, merged, or split safely until the course ontology and measurement model are decided.
- **UNRESOLVED:** Whether World Bible is a literal cross-course artifact or an optional course-native import, how frequently it changes, and whether it is the implementation of the Odyssey versus an optional context.

## Questions returned for Jeremy + ChatGPT

1. Is the student's weekly individual object named **Reasoning Quest** or **Reasoning Gate**, and are those aliases or different things?
2. Is a weekly gate a standalone file, or a compact receipt attached to the week's proof/model/code/artifact?
3. What makes a checkpoint materially different from a normal gate beyond weight and frequency?
4. Is World Bible the persistent implementation of the Odyssey, or optional context attached to it? What is its update cadence and cross-course import rule?
5. Which social artifacts are separately graded: Pair Reasoning reflection/report, Show & Tell reflection, and A7 peer feedback? How do they avoid asking students to report the same reasoning twice?
6. Does Week 2's Evidence Portfolio represent an exception to the Odyssey gate, or should the category/object language be reconciled after the ontology decision?
7. Which terms are student-facing versus only gradebook/planning/internal labels?

## Verification

- All required source families were searched or explicitly found absent.
- The inventory consolidates terms into object families rather than raw-hit rows.
- Every **MEDIUM** or **LOW** interpretation above includes representative source paths and the reason for uncertainty.
- Write scope: only this report is added. No course source was modified.

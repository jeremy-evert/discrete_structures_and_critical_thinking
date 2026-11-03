# Fresh-eyes review — student-facing Week 14 pages

## Review record

- **Reviewer:** an independent fresh Claude session (Sonnet), with no tools,
  given only the student pages.
- **Scope:** the student pages supplied for review: handout, concept map,
  glossary, Thursday activity, recap outline, Tuesday landing page, Thursday
  Canvas page, and generated prompts page.
- **Method:** the reviewer checked terminology and plain-language clarity.
  The table below records every flag in the supplied fresh-reader report.
- **Data boundary:** only fictional Boolean variables, fictional badge states,
  and synthetic examples appear in these pages.

## Flags and disposition

“Fixed” means the page now defines or clarifies the term where a student first
needs it. “Logged-not-fixed” means the item was a title quotation, a broad
vocabulary/style suggestion outside the requested repair, or an already clear
term; the reason is recorded below.

| Source | Flag(s) | Disposition and reason |
|---|---|---|
| `canvas/tuesday_landing.md` | Boolean algebra; circuits; state models; transformation; equivalent; assignment; allowed assignment; Boolean expression; variable; simplification; counterexample; satisfying witness; tautology; trace; transitions; incomplete model; missing transition; self-loop; finite-state machine; Claude prompt files; “predict first, run the check”; evidence; model boundary; defend; challenge; Boolean/circuit claim | **Fixed:** assignment/allowed assignment, simplification, missing transition/self-loop, claim/evidence, boundary, and arrow language now have plain explanations; input distinguishes Boolean values from machine events. **Logged-not-fixed:** “Boolean algebra,” “circuits,” “state models,” “transformation,” “equivalent,” “Boolean expression,” “variable,” “counterexample,” “witness,” “tautology,” “trace,” “transitions,” “incomplete model,” “finite-state machine,” prompt-file directions, “predict first,” “defend,” and “challenge” are either named course topics, already explained on this page or the linked handout/glossary, or ordinary activity directions. The title-only subject labels are not definitions students need before entering the page. |
| `student/handout.md` | Boolean input; output; parentheses/NOT precedence; F and B labels; claimed shorter form; allowed assignment; proof; `P=True` / `P=False`; unsatisfiable; model; `--valid-->`; input sequence; simplification; self-loop; state/input pair; missing transition | **Fixed:** Boolean input, allowed assignment, proof, assignment notation, unsatisfiable, transition-arrow notation, simplification, self-loop, and missing transition are explained. The missing-rule example now says `Open --timeout--> Locked` is present in the displayed model and would be missing only if omitted. **Logged-not-fixed:** output, expression labels `F`/`B`, parentheses, and the input sequence are directly shown in the adjacent table or trace; they do not introduce a separate concept needing a definition here. |
| `student/concept_map.md` | failure caught / arrow reading; bounded; universal claim; evaluate; four rows; exhaustively; satisfying assignment / print; defeats tautology; alternate arrow notation / inputs omitted; event; smuggling; validate; overclaiming; evidence; proof | **Fixed:** table-arrow reading, claim, evidence, proof, allowed assignment, Boolean-vs-machine input, event, transition notation, and boundary are explained. **Logged-not-fixed:** “bounded,” “universal,” “evaluate,” “four rows,” “exhaustively,” “print,” “defeats,” “smuggling,” “validate,” and “overclaiming” are ordinary words or immediately demonstrated by the adjacent example/check; extra definitions would add little. |
| `student/glossary.md` | operation / inputs; allowed; finite / bounded; maps; arrow notation; claim; evidence; proof; missing glossary entries for proof, simplification, missing transition, boundary | **Fixed:** added entries for proof, simplification, missing transition, claim, evidence, and boundary; clarified allowed assignment, Boolean input versus machine event, event, and arrows. **Logged-not-fixed:** “operation,” “finite,” “bounded,” and “maps” describe the immediately following examples in the existing entries and are not needed as separate glossary entries for this repair. |
| `student/thursday_activity.md` | Show & Tell; boundary; artifact; circuit; equivalent; truth table; variables; transitions; start state; traces; claim; evidence; unstated assumption; narrow; inference; critique; Checkpoint 3; Decision Gate; canonical source; course-work object; submission headings; “establishes … under” | **Fixed:** Show & Tell, boundary, input as a machine event, arrow notation, claim, and evidence are defined at first use. **Logged-not-fixed:** artifact path, circuit/equivalent/truth-table/variable, transition/start-state/trace, assumption, narrow, inference, and critique are explained by the instructions or linked handout/glossary; Checkpoint 3, Decision Gate, canonical source, course-work object, and named headings are course workflow labels retained as published; the exit sentence is an example frame whose meaning is explained immediately after it. |
| `canvas/thursday_activity.md` | Show & Tell; Checkpoint 3; circuit; equivalent; truth table; transitions; start state; traces; claim; evidence; assumption; inference; critique; Decision Gate; canonical; course-work object; submission headings; establishes / outside the model | **Fixed:** Show & Tell, boundary, machine input/event, arrow notation, claim, and evidence are defined consistently with the student activity. **Logged-not-fixed:** circuit/equivalent/truth-table/transition/start-state/trace and assumption/inference/critique are explained in the linked handout, glossary, or adjacent directions; Checkpoint 3, Decision Gate, canonical source, course-work object, and submission headings are course workflow labels; “outside the model” is explained by the boundary and model-limit definition on the page. |
| `student/recap_outline.md` | No term-specific flag in the supplied table; the review summary mentioned five bullets per day | **Logged-not-fixed:** a structural observation, not an unexplained-term flag; the recap already has five teaching bullets for each day. |
| `canvas/tuesday_prompts.md` | No term-specific flag in the supplied table; it was included in the reviewer’s stated scope | **Logged-not-fixed:** no row in the supplied findings flagged this page; it is a concatenation of prompt files and was not changed under the requested scope. |
| `canvas/tuesday_landing.md` | “Boolean Algebra, Circuits, SAT, and State Models” title; “finite-state-machine slides” title | **Logged-not-fixed:** title quotations only; the labels identify the linked course materials, and the page body gives the relevant plain-language orientation. |

## Result

The requested genuine terminology gaps are fixed in the student and Canvas
pages. The flagged `Open --timeout--> Locked` example is explicitly identified
as present in the example model; omission is described as the condition that
would make it missing. The independent Claude pass covered only student pages,
so this repair also checked that the Canvas landing and Thursday pages carry
the same explanations. This record documents dispositions; it is not a
separate acceptance decision.

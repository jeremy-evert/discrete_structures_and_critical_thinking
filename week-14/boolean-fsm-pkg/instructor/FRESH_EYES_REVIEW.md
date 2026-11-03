# Fresh-eyes review — student-facing Week 14 pages

## Review record

- **Reviewer:** Claude Sonnet via `claude -p --model sonnet --tools ""`
  (CLI alias; exact model snapshot was not recorded).
- **First-pass scope:** exactly six supplied pages: Canvas landing, handout,
  concept map, glossary, student Thursday activity, and Canvas Thursday
  activity.
- **Second-pass scope:** `student/recap_outline.md` and
  `canvas/tuesday_prompts.md`; raw reader output:
  `/tmp/claude-1000/-mnt-nora-git-worktrees-fi-dsct-coverage/e5282cd0-1073-4bf9-b12e-a05665cfbb4d/scratchpad/fresh2_out.md`.
- **Method:** terminology and plain-language clarity review. Dispositions
  below cover both passes; the second-pass flags are recorded separately.
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
| `canvas/tuesday_landing.md` | “Boolean Algebra, Circuits, SAT, and State Models” title; “finite-state-machine slides” title | **Logged-not-fixed:** title quotations only; the labels identify the linked course materials, and the page body gives the relevant plain-language orientation. |

## Result

The first pass covered only its six listed pages. In that pass, the requested
terminology gaps were fixed in the student and Canvas pages, and
`Open --timeout--> Locked` is explicitly identified as present in the example
model; omission is described as the condition that would make it missing.
Second-pass flags and dispositions follow.

## Second pass: recap outline and Tuesday prompts

The reader's recap flags were: truth table, counterexample, equivalence, gates,
Boolean expression, circuit rows, universal proof, finite-state machine,
state/input, model limits, defensible model, traces, transition, and
authorization. **Fixed:** the recap now defines truth table, counterexample,
equivalence, gate, satisfying witness, tautology, finite-state machine, trace,
transition, and model limits at use. “Rows” now refers explicitly to truth
table rows. **Logged-not-fixed:** “defensible” and “authorization” are ordinary
words here; authorization is an example of a fact the model cannot establish.

The reader's Tuesday prompt-page flags and dispositions:

| Flag | Disposition |
|---|---|
| small-step rules | **Logged-not-fixed:** slide reference label; the prompts immediately give the concrete steps. |
| AND, OR, NOT; operator | **Logged-not-fixed:** the operators are listed and used in concrete expressions; the handout defines their behavior. |
| expression, Boolean variable, assignment, equivalence | **Fixed:** Prompt 01 now supplies plain-language definitions before asking for a proposed evaluator. |
| P and Q | **Logged-not-fixed:** variable names are exemplified in the four listed assignments. |
| evaluator; Python standard library | **Logged-not-fixed:** the request describes the evaluator's purpose and explicitly constrains implementation to built-in Python facilities; not a Boolean concept needed to run the prompt. |
| synthetic | **Fixed:** changed to “made-up” in Prompt 01. |
| exhaustive check | **Logged-not-fixed:** the prompt contrasts a prediction with checking every assignment and names all four assignments. |
| AI drift | **Fixed:** changed to “Likely AI mistake” across prompt sources. |
| committed deck example | **Logged-not-fixed:** a direction to return to a named course artifact, not a technical term. |
| F, B; simplification | **Logged-not-fixed:** expressions and the proposed shorter expression are printed in full; simplification is defined in the handout. |
| tuple notation; operator precedence; mismatch | **Logged-not-fixed:** the tuple order and mismatch are shown explicitly; precedence is an ordinary programming term, and the prompt prohibits relying on inspection. |
| satisfiability/SAT; witness; equivalence checker; enumerate; mapping | **Fixed:** prompt 03b defines satisfying witness in place; Prompt 03a specifies enumeration and shows the exact mapping form. “SAT” is expanded in the Canvas landing. |
| `{'P': False, 'Q': True}` notation; S = P | **Logged-not-fixed:** each is immediately paired with its expected result and full expression. |
| satisfiable; unsatisfiable; tautology | **Logged-not-fixed:** prompt 03b gives definitions for tautology and expected classifications; satisfiable/unsatisfiable are defined on the landing page and handout. |
| finite-state-machine runner; alphabet; start state; transition notation; transition table; reference model | **Logged-not-fixed:** the prompt declares states, inputs, start state, rules, and expected sequence; the landing and handout define machine, input, transition, and trace. |
| validator; (state, input) pair; deterministic order; self-loop | **Logged-not-fixed:** each is directly specified by the complete set/order of pairs and an explicit self-loop instruction; self-loop is defined in the handout. |
| Cartesian product; transition keys | **Logged-not-fixed:** the recovery instruction is for a programming audience and describes the mechanical comparison the validator must perform. |
| access system | **Logged-not-fixed:** an ordinary example boundary; the prompt explicitly asks what the validator cannot establish about it. |

All prompt-source text is now ASCII; the only non-ASCII characters inside an
extracted prompt block were the curly quotes in Prompt 03b, now straight
quotes. This report records review dispositions; it is not a separate
acceptance decision.

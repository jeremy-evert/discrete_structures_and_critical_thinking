# Prompt 308 — verified Week 4–14 open-resource harvest

## Provenance, method, and limits

- **DSCT starting commit:** `e0e7ef0eb31c141a9df1ff21ff592ac53ca222b2`
- **Live retrieval date:** 2026-08-17 (America/Chicago).
- **Method:** opened the resource pages/PDFs named below during this run; checked the stated slices in their tables of contents or text, checked access without sign-in/payment, and checked license claims on the resource or its publisher's authoritative terms page. Search results were used only to locate pages, never as evidence.
- **Source families inspected:** Oscar Levin/University of Northern Colorado's *Discrete Mathematics: An Open Introduction* (DMOI4); MIT OpenCourseWare (MIT OCW) *Mathematics for Computer Science* (MCS); Matthew Van Cleave/Lansing Community College's *Introduction to Logic and Critical Thinking*; Open Logic Project (OLP), including *forall x: Calgary*.
- **Scope limit:** no final weeks, calendar placements, required-reading list, curriculum spine, lesson, assessment, or platform decision is made here. “Candidate” means a verified ingredient, not an adoption decision.

### Reusable-source legend

DMOI4 is **CC BY-NC-SA 4.0**, as stated on its [book page](https://discrete.openmathbooks.org/dmoi4.html). Its online text is readable without sign-in and reports screen-reader support plus a downloadable PDF. MIT OCW's current [terms](https://ocw.mit.edu/pages/privacy-and-terms-of-use/) state **CC BY-NC-SA 4.0** for OCW materials; the particular 2015 MCS PDF itself states **CC BY-NC-SA 3.0**, so that more specific, more conservative attribution controls reuse of that PDF. OLP's [license page](https://openlogicproject.org/olp-license/) states **CC BY 4.0**, unless otherwise noted. Van Cleave is listed by the Open Textbook Library as **CC BY**; this is sufficiently verified for the hosted book record, but a future adapter should preserve attribution and re-check the downloadable edition's front matter.

“OPEN-LICENSE-VERIFIED” does **not** mean frictionless use: NC/SA restrictions can constrain a later packaged derivative. Public access and reuse rights are recorded independently below.

## Topic-family coverage checklist

| # | Current topic family | Verified candidate slice(s) | Status | Main residual gap |
|---|---|---|---|---|
| 1 | Logic, Claims & Proof | DMOI4 §§1.1–1.5; Van Cleave ch. 1–2 | Adequately served | DSCT examples for AI-produced claims |
| 2 | Sets, Functions & Sequences | DMOI4 §0.2, ch. 5; §§4.1–4.2 | Adequately served | authentic data/function interpretation |
| 3 | Algorithms, Correctness & Growth | MCS §5.4, §13.7 | Adequately served | runnable comparison/measurement activity |
| 4 | Integer Properties & Cryptography | MCS §§8.6–8.12; DMOI4 §6.2 | Adequately served | safe, non-operational crypto case framing |
| 5 | Induction, Recursion & Recurrences | DMOI4 §§4.4–4.6; MCS §5.4 | Adequately served | code-to-proof translation support |
| 6 | Counting & Combinatorial Reasoning | DMOI4 §§3.2–3.6 | Adequately served | validation of model/outcome space |
| 7 | Probability, Uncertainty & Evidence | DMOI4 §3.7; Van Cleave §§3.5–3.10 | Adequately served | evidence-quality and base-rate lab |
| 8 | Relations, Equivalence, Partial Orders, Matrices & Digraphs | DMOI4 §2.6; MCS §§9.6–9.10 | Adequately served | matrix/digraph visualization bridge |
| 9 | Graphs & Network Reasoning | DMOI4 §§2.1, 2.4–2.5 | Adequately served | locally meaningful network dataset/activity |
| 10 | Trees, Search & Decision Structures | DMOI4 §2.2; MCS §11.10 | Adequately served | search/decision-tree connection and limits |
| 11 | Boolean Algebra, Circuits & SAT | Van Cleave §§2.2–2.13; MCS §8.12 | Adequately served, split-source | circuit construction/solver demonstration |
| 12 | Finite-State Machines, Invariants & Model Limits | MCS §5.4; OLP *forall x* overview | Adequately served for FSM/invariants; model-limit extension is a gap | an accessible finite-vs-unbounded/undecidability bridge |

## Detailed candidate cards

### 1. Logic, Claims & Proof — DMOI4, “Logic and Proofs”

- **Author/institution:** Oscar Levin, University of Northern Colorado. **Role:** ADAPT, EXPLANATION. **Exact slice:** [chapter 1](https://discrete.openmathbooks.org/dmoi4/ch_logic.html), §§1.1–1.5 (statements, implications, truth tables/equivalence, direct/contrapositive/contradiction proofs, and proofs about structures). **Burden:** select one or two sections plus preview/practice questions; do not assign the whole chapter by default.
- **Access / reuse / retrieval:** FREE-NO-LOGIN / OPEN-LICENSE-VERIFIED (CC BY-NC-SA 4.0; book-page evidence above) / 2026-08-17. The opened page exposes the named sections and practice material.
- **Fit:** excellent formal vocabulary for distinguishing a claim from a consequence and testing a purported proof. It has a direct Critical Thinking connection (premises/conclusion and validity), a proof/counterexample bridge (proof styles and false generalizations), and an AI-verification angle (translate an AI claim to premises, then locate a missing implication or counterexample). Computational bridge is not supplied; course-owned checking activity is needed.
- **Assessment:** **Authority:** instructor-authored OER with clear provenance. **Clarity:** friendly first/second-year exposition and section-sized activities. **Accessibility:** responsive HTML, PDF, screen-reader claim; math notation still needs accessible course framing. **Reuse safety:** adapt only with attribution, NC and SA compliance. **Why attention / not wholesale:** unusually modular proof entry point; do not make students read all exercises or assume it teaches informal argument reconstruction.
- **Course-owned connective tissue:** prompt students to distinguish formal validity from persuasive prose and verify an AI-generated proof line by line.

### 2. Sets, Functions & Sequences — DMOI4, “Discrete Structures” and “Sequences”

- **Author/institution:** Levin/University of Northern Colorado. **Role:** ADAPT, EXPLANATION. **Exact slices:** [logic chapter table of contents for §0.2](https://discrete.openmathbooks.org/dmoi4/ch_logic.html) (sets, functions, sequences, relations) and [chapter 4](https://discrete.openmathbooks.org/dmoi4/ch_sequences.html), §§4.1–4.2 (formulas, partial sums/differences, Python mention, arithmetic/geometric growth). **Burden:** one concise structures section plus selected §§4.1–4.2 examples/questions; do not assign all of chs. 4–5.
- **Access / reuse / retrieval:** FREE-NO-LOGIN / OPEN-LICENSE-VERIFIED (CC BY-NC-SA 4.0) / 2026-08-17.
- **Fit:** definitions and representations provide the formal layer; sequence formulas/growth offer a computational bridge. Critical Thinking: identify domain/codomain and an unjustified extrapolation. Proof/counterexample: test whether a mapping is a function/injection with a witness. AI verification: ask for a domain, codomain, and boundary cases before accepting a generated answer.
- **Assessment:** **Authority:** sustained discrete-math OER. **Clarity:** preview activities and practice problems are useful, though notation may be abrupt. **Accessibility:** HTML/PDF route; Python material is an optional bridge, not an assumed prerequisite. **Reuse safety:** NC-SA adaptation constraints. **Why / not wholesale:** precise, modular definitions; do not treat its topic order as DSCT's order.
- **Course-owned connective tissue:** a small data/table-to-function interpretation exercise and an accessible non-code alternative.

### 3. Algorithms, Correctness & Growth — MIT OCW MCS

- **Author/institution:** Eric Lehman, F. Thomson Leighton, Albert R. Meyer; MIT. **Role:** ADAPT, PRIMARY/EXPLANATION. **Exact slices:** [MCS PDF](https://live.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf), §5.4 “State Machines” pp. 131–143 (invariants as proof of reachable-state claims) and §13.7 pp. 531–541 (asymptotic notation and pitfalls). **Burden:** select 4–8 pages or one worked example; the 920-page text is not an assignment.
- **Access / reuse / retrieval:** FREE-NO-LOGIN / OPEN-LICENSE-VERIFIED (specific PDF: CC BY-NC-SA 3.0 in its front matter) / 2026-08-17. PDF opened successfully.
- **Fit:** connects correctness to preserved properties and growth claims to their assumptions; the asymptotic-pitfalls discussion is especially good for critiquing overconfident efficiency claims. Critical Thinking: distinguish a proved bound from a slogan. Proof/counterexample: invariant preservation and counterexample inputs. Computational bridge: measure small inputs then contrast empirical timing with asymptotic claims. AI verification: require a stated cost model and test a generated complexity claim.
- **Assessment:** **Authority:** MIT-authored, CS-oriented original course text. **Clarity:** strong worked reasoning, but denser than DMOI4. **Accessibility:** searchable 920-page PDF; no claim here that every diagram/equation is independently accessible. **Reuse safety:** NC-SA 3.0; link or adapt only after compatibility review. **Why / not wholesale:** unusually strong correctness/growth bridge; not a beginner-friendly complete DSCT text.
- **Course-owned connective tissue:** runnable pseudocode and a plain-language definition of correctness before notation.

### 4. Integer Properties & Cryptography — MIT OCW MCS plus DMOI4

- **Author/institution:** Lehman/Leighton/Meyer, MIT; Levin/UNC. **Role:** ADAPT, EXPLANATION. **Exact slices:** MCS [PDF](https://live.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf) §§8.6–8.9, pp. 263–278 (congruence, remainder arithmetic, inverses) and §8.12, pp. 289–291 (SAT/cryptographic connection); DMOI4 [§6.2](https://discrete.openmathbooks.org/dmoi4/ch_additionalTopics.html), pp. 432–443 in its PDF table of contents (divisibility through linear Diophantine equations). **Burden:** 5–10 pages plus one small congruence task; do not assign MCS chapter 8 wholesale.
- **Access / reuse / retrieval:** FREE-NO-LOGIN / OPEN-LICENSE-VERIFIED (MCS CC BY-NC-SA 3.0; DMOI4 CC BY-NC-SA 4.0) / 2026-08-17.
- **Fit:** formal integer reasoning paired with a motivating crypto/SAT consequence. Critical Thinking: identify what a security claim assumes. Proof/counterexample: prove a congruence property or refute an invalid cancellation. Computational bridge: small modular-arithmetic program or table. AI verification: demand a hand-checkable modular trace.
- **Assessment:** **Authority:** MIT/UNC sources are strong for stated roles. **Clarity:** DMOI4 is gentler; MCS context motivates but is denser. **Accessibility:** public HTML/PDF; equations need a course-owned accessible walkthrough. **Reuse safety:** both have NC-SA limits. **Why / not wholesale:** complementary rigor and motivation; do not imply it teaches practical cryptosystem deployment.
- **Course-owned connective tissue:** safe toy examples, explicit distinction between mathematical illustration and operational security advice.

### 5. Induction, Recursion & Recurrences — DMOI4 plus MCS

- **Author/institution:** Levin/UNC; Lehman/Leighton/Meyer/MIT. **Role:** ADAPT, EXPLANATION. **Exact slices:** DMOI4 [ch. 4](https://discrete.openmathbooks.org/dmoi4/ch_sequences.html) §§4.4–4.6 (exponential sequences/characteristic roots, induction, strong induction); MCS [§5.4](https://live.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf) pp. 131–143 for induction over transitions. **Burden:** one induction subsection plus one recurrence/example; do not assign all sequence methods.
- **Access / reuse / retrieval:** FREE-NO-LOGIN / OPEN-LICENSE-VERIFIED (DMOI4 CC BY-NC-SA 4.0; MCS CC BY-NC-SA 3.0) / 2026-08-17.
- **Fit:** DMOI4 makes induction explicit; MCS provides the powerful “number of transitions” interpretation. Critical Thinking: inspect whether an induction hypothesis is strong enough. Proof/counterexample: repair a false proof. Computational bridge: trace a recursive process/sequence. AI verification: have students isolate base case, quantified hypothesis, and inductive step from generated prose.
- **Assessment:** **Authority:** established course texts. **Clarity:** DMOI4’s staged sections are more approachable; MCS contributes a vivid application. **Accessibility:** free web/PDF; recurrence notation may need support. **Reuse safety:** NC-SA terms. **Why / not wholesale:** a genuine complement; no final ordering implied.
- **Course-owned connective tissue:** code/pseudocode traces paired with proof templates and examples of invalid induction.

### 6. Counting & Combinatorial Reasoning — DMOI4, “Counting”

- **Author/institution:** Levin/UNC. **Role:** ADAPT, EXPLANATION. **Exact slice:** [chapter 3](https://discrete.openmathbooks.org/dmoi4/ch_counting.html), §§3.2–3.6 (outcomes, sum/product principles, overlap/PIE, permutations/combinations, combinatorial proofs). **Burden:** one or two sections and selected preview/practice problems; do not assign all eight sections.
- **Access / reuse / retrieval:** FREE-NO-LOGIN / OPEN-LICENSE-VERIFIED (CC BY-NC-SA 4.0) / 2026-08-17; opened page lists the named subsections.
- **Fit:** frames counting as defining outcomes rather than memorizing rules. Critical Thinking: challenge whether cases overlap/exhaust possibilities. Proof/counterexample: two counts of the same set or a missed outcome. Computational bridge: enumeration of a small sample space. AI verification: compare a generated count to brute-force enumeration for a small case.
- **Assessment:** **Authority:** mature open textbook with exercise/hint infrastructure. **Clarity:** preview activities support gradual entry. **Accessibility:** readable HTML/PDF; diagrams/examples still benefit from an instructor narration. **Reuse safety:** NC-SA. **Why / not wholesale:** supports verification, not rote formulas; omit advanced PIE unless it has a clear role.
- **Course-owned connective tissue:** context-specific outcome-model audit and an inclusive-language scenario set.

### 7. Probability, Uncertainty & Evidence — DMOI4 plus Van Cleave

- **Author/institution:** Levin/UNC; Matthew Van Cleave, Lansing Community College. **Role:** ADAPT, EXPLANATION. **Exact slices:** DMOI4 [§3.7](https://discrete.openmathbooks.org/dmoi4/ch_counting.html) (computing, rules, conditional probability); Van Cleave [ch. 3 §§3.5–3.10](https://open.umn.edu/opentextbooks/textbooks/457) (probability; conjunction, base-rate, small-numbers, regression, and gambler's fallacies). **Burden:** a short formal slice plus one fallacy slice; do not assign the whole critical-thinking book.
- **Access / reuse / retrieval:** FREE-NO-LOGIN / OPEN-LICENSE-VERIFIED (DMOI4 CC BY-NC-SA 4.0; Van Cleave CC BY as stated by Open Textbook Library) / 2026-08-17. Both actual records/pages opened.
- **Fit:** unusually direct marriage of probability calculation and evidence-quality errors. Critical Thinking: base-rate and conjunction-fallacy diagnosis. Proof/counterexample: construct a sample space that invalidates intuition. Computational bridge: simulate coin/dice/base-rate scenarios. AI verification: require assumptions/sample space before accepting numerical probability output.
- **Assessment:** **Authority:** formal math paired with an authored introductory critical-thinking text. **Clarity:** Van Cleave is accessible; its real-life examples may date. **Accessibility:** PDF record and web text routes; confirm final downloadable format before adoption. **Reuse safety:** DMOI4 has NC-SA; Van Cleave's CC BY record supports adaptation with attribution, subject to a final file-level license check. **Why / not wholesale:** complementary, not a combined course spine.
- **Course-owned connective tissue:** contemporary evidence case, interpretation guardrails, and simulation instructions.

### 8. Relations, Equivalence, Partial Orders, Matrices & Digraphs — MCS plus DMOI4

- **Author/institution:** Lehman/Leighton/Meyer/MIT; Levin/UNC. **Role:** ADAPT, EXPLANATION. **Exact slices:** MCS [PDF](https://live.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf) §§9.6–9.10, pp. 337–351 (partial/equivalence relations and directed-graph representations) including relation-matrix representation around p. 358; DMOI4 [§2.6](https://discrete.openmathbooks.org/dmoi4/ch_graphtheory.html) (relations, properties, equivalence classes/partitions). **Burden:** select 4–8 pages and one representation exercise; do not assign all relation theory.
- **Access / reuse / retrieval:** FREE-NO-LOGIN / OPEN-LICENSE-VERIFIED (MCS CC BY-NC-SA 3.0; DMOI4 CC BY-NC-SA 4.0) / 2026-08-17.
- **Fit:** connects abstract relation properties to digraphs and Boolean matrices. Critical Thinking: distinguish a classification scheme from a justified equivalence relation. Proof/counterexample: test reflexivity/transitivity/antisymmetry with a witness. Computational bridge: adjacency/Boolean matrix. AI verification: ask an AI to classify a relation, then check every property with explicit counterexamples.
- **Assessment:** **Authority:** formal CS/mathematics sources. **Clarity:** DMOI4 is the gentler route; MCS supplies broader representations. **Accessibility:** downloadable/readable; matrix notation needs support. **Reuse safety:** NC-SA. **Why / not wholesale:** useful representational complement, not a mandate to teach all order theory.
- **Course-owned connective tissue:** an annotated visual translation among list, digraph, and matrix and a realistic data-governance example.

### 9. Graphs & Network Reasoning — DMOI4, “Graph Theory”

- **Author/institution:** Levin/UNC. **Role:** ADAPT, EXPLANATION. **Exact slice:** [chapter 2](https://discrete.openmathbooks.org/dmoi4/ch_graphtheory.html), §§2.1, 2.4–2.5 (definitions, Euler trails/circuits, coloring); optional §2.7 matching. **Burden:** a 5–10 page slice plus one diagram/problem; do not assign every graph-theory topic.
- **Access / reuse / retrieval:** FREE-NO-LOGIN / OPEN-LICENSE-VERIFIED (CC BY-NC-SA 4.0) / 2026-08-17.
- **Fit:** uses simple diagrams to expose modeling choices in networks/constraints. Critical Thinking: question whether an edge means connection, direction, capacity, or trust. Proof/counterexample: a degree condition or impossible coloring. Computational bridge: draw/analyze a small graph. AI verification: compare an AI's claimed route/coloring with the graph itself.
- **Assessment:** **Authority:** solid undergraduate OER. **Clarity:** low-prerequisite entry and exercises. **Accessibility:** HTML/PDF, but visual descriptions and alternatives are course-owned work. **Reuse safety:** NC-SA. **Why / not wholesale:** excellent small slices; do not overextend from a hand-drawn graph to claims about real social networks.
- **Course-owned connective tissue:** a data/ethics note about what a graph model leaves out and accessible text alternatives to figures.

### 10. Trees, Search & Decision Structures — DMOI4 plus MCS

- **Author/institution:** Levin/UNC; Lehman/Leighton/Meyer/MIT. **Role:** ADAPT, EXPLANATION. **Exact slices:** DMOI4 [§2.2](https://discrete.openmathbooks.org/dmoi4/ch_graphtheory.html) (tree properties, spanning/rooted trees); MCS [§11.10](https://live.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf), pp. 433–436 (trees, spanning trees, minimum-weight spanning trees). **Burden:** one short tree slice plus one concrete decision/search representation; do not assign an algorithms survey.
- **Access / reuse / retrieval:** FREE-NO-LOGIN / OPEN-LICENSE-VERIFIED (DMOI4 CC BY-NC-SA 4.0; MCS CC BY-NC-SA 3.0) / 2026-08-17.
- **Fit:** establishes trees as structures before DSCT relates them to search/decisions. Critical Thinking: identify branch criteria and missing alternatives. Proof/counterexample: verify a tree characterization or expose a cycle. Computational bridge: simple traversal/search trace. AI verification: check whether a generated decision tree exhausts cases and respects its stated rule.
- **Assessment:** **Authority:** credible math/CS texts. **Clarity:** DMOI4 supplies basic vocabulary; MCS gives data-structure relevance. **Accessibility:** open formats; diagrams require captions/description in DSCT context. **Reuse safety:** NC-SA. **Why / not wholesale:** strong formal foundation, but neither slice alone teaches responsible decision modeling.
- **Course-owned connective tissue:** human-impact/uncertainty discussion and an accessible tree-trace activity.

### 11. Boolean Algebra, Circuits & SAT — Van Cleave plus MCS

- **Author/institution:** Van Cleave/Lansing Community College; Lehman/Leighton/Meyer/MIT. **Role:** ADAPT, EXPLANATION. **Exact slices:** Van Cleave [ch. 2 §§2.2–2.13](https://open.umn.edu/opentextbooks/textbooks/457) (truth-functional connectives, truth tables, validity, proof forms); MCS [§8.12](https://live.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf), pp. 289–291 (connection between satisfiability and digital circuits). **Burden:** select §§2.2, 2.6–2.7 and one SAT/circuit excerpt; do not assign the whole formal-logic chapter.
- **Access / reuse / retrieval:** FREE-NO-LOGIN / OPEN-LICENSE-VERIFIED (Van Cleave CC BY record; MCS CC BY-NC-SA 3.0) / 2026-08-17.
- **Fit:** Van Cleave gives the entry-level truth-functional language; MCS gives a genuine SAT/circuit reason for the abstraction. Critical Thinking: distinguish satisfiable, valid, and persuasive. Proof/counterexample: truth-table countermodel. Computational bridge: evaluate a small Boolean expression or use a future approved solver demo. AI verification: request a truth table/model rather than accept a bare SAT claim.
- **Assessment:** **Authority:** appropriate roles, though neither is a standalone beginner circuit lab. **Clarity:** Van Cleave is approachable; MCS excerpt is compact and technical. **Accessibility:** free PDF/web routes; formula/circuit visuals need accessible explanation. **Reuse safety:** different licenses must remain separated in any derivative. **Why / not wholesale:** complementary source roles; do not infer a tool requirement.
- **Course-owned connective tissue:** a low-stakes circuit-to-formula worksheet and an optional, accessible solver demonstration.

### 12. Finite-State Machines, Invariants & Model Limits — MCS plus OLP

- **Author/institution:** Lehman/Leighton/Meyer/MIT; Open Logic Project international team. **Role:** ADAPT, EXPLANATION. **Exact slices:** MCS [§5.4](https://live.ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf), pp. 131–143 (states/transitions, reachable states, preserved invariant); OLP [*forall x: Calgary* overview](https://forallx.openlogicproject.org/) (available HTML/PDF/LaTeX, truth-functional and first-order logic, proof systems; only as an optional formal-logic extension). **Burden:** MCS pp. 131–143 is already substantial; no recommendation to assign OLP wholesale.
- **Access / reuse / retrieval:** FREE-NO-LOGIN / OPEN-LICENSE-VERIFIED (MCS CC BY-NC-SA 3.0; OLP CC BY 4.0 unless otherwise noted, per [OLP license](https://openlogicproject.org/olp-license/)) / 2026-08-17. Both actual resources opened; OLP's own overview says it provides screen, print, dyslexia-oriented PDF, HTML accessibility features, and source.
- **Fit:** MCS is excellent for FSM/invariant reasoning and finite-state examples; it does **not** by itself provide a student-ready treatment of limits of finite models/undecidability. Critical Thinking: state what a model includes/excludes. Proof/counterexample: prove an invariant or give a transition that breaks it. Computational bridge: simulate a small transition system. AI verification: ask whether an invariant holds for the initial state and every transition, not merely for sampled runs.
- **Assessment:** **Authority:** MIT text and an open collaborative logic project. **Clarity:** MCS robot example is concrete; OLP is explicitly advanced/intermediate and should be optional/background rather than default student reading. **Accessibility:** MCS PDF plus OLP's multiple formats; verify individual OLP edition details at adoption. **Reuse safety:** licenses are verified but differ. **Why / not wholesale:** strong invariant slice; **COURSE-OWNED CONTENT NEEDED** for a gentle model-limit bridge.
- **Course-owned connective tissue:** a finite automaton simulator or paper trace, then a plain-language finite-versus-unbounded limitation activity with no unsupported claims about AI.

## Access and reuse-rights matrix

| Candidate family | Access class (verified) | Reuse class (verified) | Recommended handling |
|---|---|---|---|
| DMOI4 (Levin/UNC) | FREE-NO-LOGIN | OPEN-LICENSE-VERIFIED — CC BY-NC-SA 4.0 | Link or adapt small slices with attribution; preserve NC/SA conditions |
| MIT OCW MCS 2015 PDF | FREE-NO-LOGIN | OPEN-LICENSE-VERIFIED — specific PDF CC BY-NC-SA 3.0 | Link by default; obtain compatibility review before combining adapted material |
| Van Cleave / Open Textbook Library record | FREE-NO-LOGIN | OPEN-LICENSE-VERIFIED — CC BY shown on record | Link or adapt with attribution; re-check file front matter before final packaging |
| Open Logic Project / *forall x* | FREE-NO-LOGIN | OPEN-LICENSE-VERIFIED — CC BY 4.0 unless otherwise noted | Link/adapt with attribution; check edition-specific exceptions |

No candidate above is classified merely from public availability. No paid, login-only, institutional-only, or RIGHTS-UNCLEAR candidate is presented as a required-free-path source.

## Broken, stale, and unverified items

- The direct guessed DMOI4 URL `ch_discrete_structures.html` did not resolve in this run. The structures material is nevertheless verifiably listed as §0.2 in the live book navigation; use the live table of contents and re-check its final direct section link before assigning it.
- The Open Logic Project license page did not render through one direct-open attempt, but its live search/opened project material and the separately retrieved official license text state CC BY 4.0. This is sufficient for the project-level classification, not a guarantee for every future edition or embedded third-party element.
- No accessible SWOSU-owned instructional source with provenance was found in this isolated worktree. It is therefore **not** represented as a candidate; this is an evidence gap, not a finding that none exists elsewhere.
- No dedicated, verified public video/demo was retained. The inspected textbook HTML/PDF resources are stronger and more stable than adding a video merely to fill a format slot. Any future video needs its own captions/transcript, availability, and rights check.

## Course-owned-content gaps

External readings cover definitions and many worked examples. They do not supply the DSCT connective tissue below:

- a recurring claim-evidence-warrant/counterexample protocol that applies to math, code, sources, and AI output;
- accessible alternatives for diagrams, tables, notation-heavy PDFs, and optional computational work;
- small, runnable or hand-executable simulations for growth, probability, graphs, Boolean logic, and FSMs;
- current, responsibly framed examples linking formal models to evidence and AI verification;
- a gentle, accurate bridge from finite-state modeling/invariants to model limits; and
- local context, student-facing vocabulary, and decisions about burden/sequence.

These are **COURSE-OWNED CONTENT NEEDED**, not defects that can be resolved by assigning more external pages.

## Especially strong cross-topic resources worth considering later

- **DMOI4:** the most flexible broad ingredient: modular sections, preview/practice structure, and a verified NC-SA license. It spans logic/proof, graph theory, counting/probability, sequences/induction, structures, and number theory—but should not automatically become a course spine.
- **MIT OCW MCS:** especially valuable where mathematical structures become CS reasoning: invariants, modular arithmetic/crypto context, relations/digraphs/matrices, asymptotic pitfalls, and probability. Its density and older CC BY-NC-SA 3.0 PDF license make selective linking preferable.
- **Van Cleave:** the clearest bridge from formal material to critical-thinking habits, especially claim analysis and probability fallacies. Its coverage does not replace discrete-math proof instruction.
- **OLP:** strongest as a rights-clear, accessible-format extension for formal logic, not as the default entry reading for this audience.

## Decisions returned to Jeremy + ChatGPT

Still open: the final eleven-week intellectual spine; which topic families combine/move/narrow/recur; final resource selection and required/free/paid mix; final burden; lesson/activity design; accessibility implementation; assessment/grading; and all Canvas/Savnac operational work. This report makes none of those decisions.

## Verification summary

- All 12 current topic families appear in the coverage checklist.
- Every retained candidate has an exact chapter/section or page slice, source identity, role, retrieval date, access class, reuse class, and evaluation of authority, fit, clarity, burden, accessibility, reuse safety, and connective-tissue need.
- Recommended free-path candidates were opened successfully during the run and required neither payment nor sign-in.
- Reuse claims are separately licensed and conservative. The two listed yellow conditions are the DMOI4 direct-section URL and OLP individual-edition/embedded-material qualification; neither is being used to authorize unverified reuse.

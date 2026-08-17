# DSCT Fall 2026 — canonical Weeks 4–14 topic/source map

All rows are `CONTRACTED_NOT_AUTHORED`. RECONCILED 2026-08-15: DSCT has no
required textbook or external course for Fall 2026. The historical ZyBooks
families and KEEP / OPTIONAL / UNUSED decisions in
`zybooks-section-decisions.csv` are retained only as source provenance, not as
an assigned reading path or course spine. The malformed CSV seam and proposed
remap are documented in the Prompt 302 report and run evidence.

**Renumbered 2026-08-17** (Jeremy, executed by Cleo/Lead Foreman) to resolve
Decision cluster E: Week 3 is the container/LaTeX runway (Prompts 307/316),
not a formal topic week, so the eleven formal weeks are now Weeks 4–14
instead of the prior Weeks 3–14 twelve-week span. Boolean Algebra/Circuits/SAT
and Finite-State Machines/Invariants/Model Limits are merged into one Week 14
to fit twelve historical topic bundles into eleven slots — see
`fall-2026-spine.md`'s "The Week 14 merge" for the full rationale. Every row
below otherwise keeps its original critical-thinking question, AI failure
mode, historical source lesson, and prerequisites; only week numbers and
Thursday mode (reconciled against Prompt 313's already-settled alternation)
changed.

| Wk / dates | Technical core and primary concepts | Critical-thinking question | AI failure mode | Thu mode / intended artifact family | Historical source lesson | Catalog coverage | Historical ZyBooks family | Prerequisites / dependencies |
|---|---|---|---|---|---|---|---|---|
| 4 · Sep 8/10 | Logic, Claims & Proof: propositions, predicates, quantifiers, implication, proof, counterexample | Does a true conclusion mean the argument was valid? What follows from what? | True conclusion by invalid argument; fluent proof with unjustified step | Show & Tell · checker, counterexample generator, proof verifier | `02-logic-proofs-and-sequences.md` (logic/proof portion) | propositional and predicate logic; proof techniques | Ch. 1 Logic; Ch. 2 Proofs | Week 1 reasoning method; Week 2 lab/repeatability bridge; Week 3 toolchain |
| 5 · Sep 15/17 | Sets, Functions & Sequences as Representations: sets, mappings, domain/codomain, composition, sequences | What did our representation assume, omit, or blur? | Silent domain/codomain change; representation hides a lost distinction | Pair Reasoning · representation comparison, table/sequence trace | `02-logic-proofs-and-sequences.md` (sequences); `03-functions-and-matrices.md` (functions) | sets; functions | Ch. 3 Sets; Ch. 4 Functions; Ch. 8.1 Sequences | Week 4 language and definitions |
| 6 · Sep 22/24 | Algorithms, Correctness & Growth: algorithms, invariants, edge cases, asymptotic thinking | "It worked on my examples" proves what, exactly? | Ordinary examples pass but edge case fails; correct output without correctness argument | Show & Tell · test harness, trace checker, complexity probe | `04-algorithms.md` | — (catalog concepts served by discrete-CS spine) | Ch. 7.1–7.3 Computation | Functions/representations; evidence-bearing tests |
| 7 · Sep 29/Oct 1 | Integer Properties & Cryptography: divisibility, modular arithmetic, gcd/congruence, simple crypto — **Odyssey Checkpoint 1** | What assumptions make a security claim true? What does an adversary know? | Security claim assumes away attacker or hides unproved number-theory assumption | Pair Reasoning · encode/decode checker, modular-arithmetic witness | `05-cryptography.md` | — (supports catalog discrete-math requirement) | Ch. 9 Integer Properties | Algorithmic checking; definitions and modular reasoning |
| 8 · Oct 6/8 | Induction, Recursion & Recurrences: base/inductive cases, recursive definitions, recurrences | Where is the logical bridge? Are we assuming what we prove? | Missing base case, circular reasoning, illegal inductive leap | Show & Tell · recursion tracer, invariant checker, recurrence explorer | `06-recursion.md`; `02-logic-proofs-and-sequences.md` (proof bridge) | proof techniques | Ch. 8 Induction and Recursion | Week 4 proof habits; algorithm traces |
| 9 · Oct 13/15 | Counting & Combinatorial Reasoning: sum/product, pigeonhole, permutations/combinations, inclusion-exclusion | Are cases exhaustive and mutually exclusive? Did we count twice? | Double counting, overlapping cases, non-exhaustive split | Pair-style work folded into Tuesday; Thu Fall Break · enumerator, case-partition witness, counting model | `07-counting.md` | combinatorics | Ch. 10 Introduction to Counting; Ch. 11 Advanced Counting | Sets and representation; recursion/algorithmic checking |
| 10 · Oct 20/22 | Probability, Uncertainty & Evidence: sample spaces, conditional probability, independence, expectation, simulation | How do base rates, independence, randomness, and simulation fool us? | False independence, base-rate neglect, gambler's fallacy, simulation overclaim | Show & Tell · simulator or evidence table | `08-probability.md` | — (catalog-aligned probability support) | Ch. 12 Discrete Probability | Counting and sample-space modeling |
| 11 · Oct 27/29 | Relations, Equivalence, Partial Orders, Matrices & Digraphs — **Odyssey Checkpoint 2** | When are two things "the same"? What properties does the model satisfy? A carried World-Bible system can supply the entities and relation to classify where useful. | Claims equivalence/order while a required property fails | Pair Reasoning · relation classifier, matrix/digraph model; optionally defend the relation in a carried world/system | `09-relations.md`; `03-functions-and-matrices.md` (matrix representation) | matrices | Ch. 6 Relations / Digraphs | Sets/functions; graph representations |
| 12 · Nov 3/5 | Graphs & Network Reasoning: paths, connectivity, traversal, shortest path, Euler/Hamilton as appropriate | Are we solving the graph correctly, or modeling reality incorrectly? A carried system may provide a concrete network, but the model's edge meanings must remain explicit. | Correct solution to wrong graph model; edge meaning changes conclusion | Show & Tell · graph builder, traversal, path checker; optionally extend a carried system's network | `10-graphs.md` | graph theory | Ch. 13 Graphs | Relations/digraphs; algorithms |
| 13 · Nov 10/12 | Trees, Search & Decision Structures: rooted trees, traversal, spanning/decision trees | What information disappears when a network becomes a hierarchy? | Hierarchy erases relevant relation; decision split lacks justification | Pair Reasoning · tree visualizer, traversal/search trace | `11-trees.md` | — (catalog-aligned tree extension) | Ch. 14 Trees | Graphs; recursive reasoning |
| 14 · Nov 17/19 | Boolean Algebra, Circuits & SAT + Finite-State Machines, Invariants & Model Limits (merged — see `fall-2026-spine.md`): equivalence, gates, simplification, satisfiability; states, transitions, traces, limits | Is this transformation equivalent under every assignment? Which states/transitions were forgotten, and what can the model not establish? | Simplification fails one assignment; satisfiable confused with universally true. Omitted state/transition makes model falsely comforting; model limit ignored | Show & Tell / Reasoning Odyssey mini-capstone · truth-table evaluator, SAT witness, circuit checker; state-machine runner/model defense, optionally carrying forward a chosen world/system/problem space — **Odyssey Checkpoint 3** | `12-boolean-algebra.md`; `13-finite-state-machines.md`; `14-synthesis-and-applications.md` (synthesis source) | Boolean algebra; finite state machines | Ch. 5 Boolean Algebra; Ch. 7.4 Finite State Machines | Logic and exhaustive checking; algorithms; graphs/trees; evidence and checking |

## Catalog coverage

| Official catalog topic | Contracted location(s) | Result |
|---|---|---|
| sets | Week 5 | covered |
| functions | Week 5 | covered |
| propositional and predicate logic | Week 4 | covered |
| Boolean algebra | Week 14 | covered |
| graph theory | Week 12 | covered |
| matrices | Week 11 (representation; also Week 5 source history) | covered |
| proof techniques | Weeks 4 and 8 | covered |
| combinatorics | Week 9 | covered |
| finite state machines | Week 14 | covered |

The old orientation/learning-practice lesson is a Week 1/2 habit source, not
a formal topic. The old synthesis/applications lesson is source material for
Week 14 and Week 16, not an additional topic week. No historical skeleton is
deleted merely because its operational role changed. Week 14 now carries two
historical source lessons (Boolean Algebra and Finite-State Machines) because
of the Week 14 merge documented in `fall-2026-spine.md`; both remain distinct
provenance even though they share one Fall 2026 calendar week.

# DSCT Fall 2026 — canonical Weeks 3–14 topic/source map

All rows are `CONTRACTED_NOT_AUTHORED`. RECONCILED 2026-08-15: DSCT has no
required textbook or external course for Fall 2026. The historical ZyBooks
families and KEEP / OPTIONAL / UNUSED decisions in
`zybooks-section-decisions.csv` are retained only as source provenance, not as
an assigned reading path or course spine. The malformed CSV seam and proposed
remap are documented in the Prompt 302 report and run evidence.

| Wk / dates | Technical core and primary concepts | Critical-thinking question | AI failure mode | Thu mode / intended artifact family | Historical source lesson | Catalog coverage | Historical ZyBooks family | Prerequisites / dependencies |
|---|---|---|---|---|---|---|---|---|
| 3 · Sep 1/3 | Logic, Claims & Proof: propositions, predicates, quantifiers, implication, proof, counterexample | Does a true conclusion mean the argument was valid? What follows from what? | True conclusion by invalid argument; fluent proof with unjustified step | Pair Programming · checker, counterexample generator, proof verifier | `02-logic-proofs-and-sequences.md` (logic/proof portion) | propositional and predicate logic; proof techniques | Ch. 1 Logic; Ch. 2 Proofs | Week 1 reasoning method; Week 2 lab/repeatability bridge |
| 4 · Sep 8/10 | Sets, Functions & Sequences as Representations: sets, mappings, domain/codomain, composition, sequences | What did our representation assume, omit, or blur? | Silent domain/codomain change; representation hides a lost distinction | Show & Tell · representation comparison, table/sequence trace | `02-logic-proofs-and-sequences.md` (sequences); `03-functions-and-matrices.md` (functions) | sets; functions | Ch. 3 Sets; Ch. 4 Functions; Ch. 8.1 Sequences | Week 3 language and definitions |
| 5 · Sep 15/17 | Algorithms, Correctness & Growth: algorithms, invariants, edge cases, asymptotic thinking | “It worked on my examples” proves what, exactly? | Ordinary examples pass but edge case fails; correct output without correctness argument | Pair Programming · test harness, trace checker, complexity probe | `04-algorithms.md` | — (catalog concepts served by discrete-CS spine) | Ch. 7.1–7.3 Computation | Functions/representations; evidence-bearing tests |
| 6 · Sep 22/24 | Integer Properties & Cryptography: divisibility, modular arithmetic, gcd/congruence, simple crypto | What assumptions make a security claim true? What does an adversary know? | Security claim assumes away attacker or hides unproved number-theory assumption | Show & Tell · encode/decode checker, modular-arithmetic witness | `05-cryptography.md` | — (supports catalog discrete-math requirement) | Ch. 9 Integer Properties | Algorithmic checking; definitions and modular reasoning |
| 7 · Sep 29/Oct 1 | Induction, Recursion & Recurrences: base/inductive cases, recursive definitions, recurrences | Where is the logical bridge? Are we assuming what we prove? | Missing base case, circular reasoning, illegal inductive leap | Pair Programming · recursion tracer, invariant checker, recurrence explorer | `06-recursion.md`; `02-logic-proofs-and-sequences.md` (proof bridge) | proof techniques | Ch. 8 Induction and Recursion | Week 3 proof habits; algorithm traces |
| 8 · Oct 6/8 | Counting & Combinatorial Reasoning: sum/product, pigeonhole, permutations/combinations, inclusion-exclusion | Are cases exhaustive and mutually exclusive? Did we count twice? | Double counting, overlapping cases, non-exhaustive split | Show & Tell · enumerator, case-partition witness, counting model | `07-counting.md` | combinatorics | Ch. 10 Introduction to Counting; Ch. 11 Advanced Counting | Sets and representation; recursion/algorithmic checking |
| 9 · Oct 13/15 | Probability, Uncertainty & Evidence: sample spaces, conditional probability, independence, expectation, simulation | How do base rates, independence, randomness, and simulation fool us? | False independence, base-rate neglect, gambler's fallacy, simulation overclaim | Pair-style work folded into Tuesday; Thu Fall Break · simulator or evidence table | `08-probability.md` | — (catalog-aligned probability support) | Ch. 12 Discrete Probability | Counting and sample-space modeling |
| 10 · Oct 20/22 | Relations, Equivalence, Partial Orders, Matrices & Digraphs | When are two things “the same”? What properties does the model satisfy? | Claims equivalence/order while a required property fails | Show & Tell · relation classifier, matrix/digraph model | `09-relations.md`; `03-functions-and-matrices.md` (matrix representation) | matrices | Ch. 6 Relations / Digraphs | Sets/functions; graph representations |
| 11 · Oct 27/29 | Graphs & Network Reasoning: paths, connectivity, traversal, shortest path, Euler/Hamilton as appropriate | Are we solving the graph correctly, or modeling reality incorrectly? | Correct solution to wrong graph model; edge meaning changes conclusion | Pair Programming · graph builder, traversal, path checker | `10-graphs.md` | graph theory | Ch. 13 Graphs | Relations/digraphs; algorithms |
| 12 · Nov 3/5 | Trees, Search & Decision Structures: rooted trees, traversal, spanning/decision trees | What information disappears when a network becomes a hierarchy? | Hierarchy erases relevant relation; decision split lacks justification | Show & Tell · tree visualizer, traversal/search trace | `11-trees.md` | — (catalog-aligned tree extension) | Ch. 14 Trees | Graphs; recursive reasoning |
| 13 · Nov 10/12 | Boolean Algebra, Circuits & SAT: equivalence, gates, simplification, satisfiability | Is this transformation equivalent under every assignment? | Simplification fails one assignment; satisfiable confused with universally true | Pair Programming · truth-table evaluator, SAT witness, circuit checker | `12-boolean-algebra.md` | Boolean algebra | Ch. 5 Boolean Algebra | Logic and exhaustive checking |
| 14 · Nov 17/19 | Finite-State Machines, Invariants & Model Limits: states, transitions, traces, limits | Which states/transitions were forgotten, and what can the model not establish? | Omitted state/transition makes model falsely comforting; model limit ignored | Show & Tell / Reasoning Odyssey mini-capstone · state-machine runner/model defense | `13-finite-state-machines.md`; `14-synthesis-and-applications.md` (synthesis source) | finite state machines | Ch. 7.4 Finite State Machines | Algorithms; graphs/trees; evidence and checking |

## Catalog coverage

| Official catalog topic | Contracted location(s) | Result |
|---|---|---|
| sets | Week 4 | covered |
| functions | Week 4 | covered |
| propositional and predicate logic | Week 3 | covered |
| Boolean algebra | Week 13 | covered |
| graph theory | Week 11 | covered |
| matrices | Week 10 (representation; also Week 4 source history) | covered |
| proof techniques | Weeks 3 and 7 | covered |
| combinatorics | Week 8 | covered |
| finite state machines | Week 14 | covered |

The old orientation/learning-practice lesson is a Week 1/2 habit source, not
a formal topic. The old synthesis/applications lesson is source material for
Week 14 and Week 16, not an additional topic week. No historical skeleton is
deleted merely because its operational role changed.

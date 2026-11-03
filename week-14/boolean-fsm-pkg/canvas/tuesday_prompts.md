# Prompt 01 — Make the claim checkable

Why: a confident answer is not evidence until its terms and test are visible.

Slide reference: Week 14 Tuesday, the small-step rules.

```prompt-a
Act as a careful checking partner for a two-variable Boolean example. Before writing code, state what an expression, a Boolean variable, an assignment, and equivalence mean in plain language. Use only the operators AND, OR, and NOT. Keep the example synthetic and self-contained. Then propose the smallest Python standard-library evaluator you would need for a truth table. Do not claim two expressions are equivalent until every assignment has been checked. Show one predicted row before showing the rest.
```

Expected observable result: the response defines its terms, names the four
assignments for `P` and `Q`, and separates a prediction from an exhaustive
check.

Predict first: what must be checked before “equivalent” is justified?

Likely AI drift: it may use an undefined operator, skip an assignment, or
announce equivalence from one matching row.

Recovery: return to the committed deck example and write all four rows by hand
before comparing any generated output.
# Prompt 02 — Exhaust the truth table

Why: a single counterexample defeats a claim that two expressions agree on
every assignment.

Slide reference: Week 14 Tuesday, the false simplification.

```prompt-a
Write a small Python program using only the standard library. Define F = (P OR Q) AND (P OR NOT Q) and the proposed simplification B = P OR Q. Evaluate both expressions for all four Boolean assignments of P and Q, in the fixed order (False, False), (False, True), (True, False), (True, True). Print a compact table with P, Q, F, and B, then print the exact assignments where they differ. Do not simplify the expressions by inspection. The expected check is one mismatch, at P=False and Q=True.
```

Expected observable result: four rows are printed, and the only mismatch is
`P=False, Q=True`.

Predict first: which row will expose the proposed simplification, if any?

Likely AI drift: the program may print only true rows, use the wrong operator
precedence, or quietly replace the proposed expression.

Recovery: compare the printed four rows with the visible table on the slide;
the row `False, True` must remain visible.
# Prompt 03 — Equivalence, satisfiability, and universal claims

Why: “one witness exists” and “every assignment works” are different claims.

Slide reference: Week 14 Tuesday, the equivalence and SAT checks.

```prompt-a
Extend a small standard-library Boolean evaluator with an equivalence checker. It must enumerate every assignment for the variables that occur and return a list of counterexamples, not just True or False. Check that E = (P AND Q) OR (P AND NOT Q) is equivalent to S = P, and check that F = (P OR Q) AND (P OR NOT Q) is not equivalent to B = P OR Q. Print the counterexample for the second pair exactly as a mapping from variable names to Boolean values. State why an empty counterexample list supports equivalence only for the variables and operators actually supplied.
```

Expected observable result: the first pair has no counterexamples; the second
pair returns exactly `{'P': False, 'Q': True}`.

Predict first: which result should be empty, and which result should contain a
mapping?

Likely AI drift: it may compare only one chosen assignment or return a vague
sentence instead of the counterexample.

Recovery: keep the reference evaluator’s fixed four-row order and print the
mapping before any summary sentence.

```prompt-b
Using the same evaluator, write three separate checks. First, return one satisfying witness for P, meaning one assignment that makes P true. Second, decide whether P is a tautology, meaning true for every assignment, and if it is not, print one counterexample. Third, classify P OR NOT P and P AND NOT P as tautology or unsatisfiable. Explain in one sentence why a satisfying witness for P does not prove that P is always true. Do not use the words “equivalent” or “always” without showing the assignments that justify them.
```

Expected observable result: a witness for `P` is printed; `P` is not a
tautology; `P OR NOT P` is a tautology; `P AND NOT P` has no satisfying
witness.

Predict first: can one true row establish a tautology?

Likely AI drift: it may confuse satisfiable with universally true, or report
the first witness as a proof of every row.

Recovery: ask for the complete assignment table and label witness,
counterexample, and tautology as separate checks.
# Prompt 04 — Trace a finite-state machine

Why: a state machine earns a claim by making states, inputs, and transitions
explicit.

Slide reference: Week 14 Tuesday, the complete badge model.

```prompt-a
Implement a tiny finite-state-machine runner in Python with no third-party packages. The machine has states Locked and Open, inputs valid and timeout, start state Locked, and these transitions: (Locked, valid) -> Open and (Open, timeout) -> Locked. For this classroom trace, every other input leaves the state unchanged. Run the input sequence valid, timeout, valid and print the start state plus each resulting state. Also print a visible error for an input that is not in the declared alphabet. The expected state sequence is Locked, Open, Locked, Open. Do not invent authorization facts or physical-reader behavior.
```

Expected observable result: the trace is exactly `Locked -> Open -> Locked ->
Open`, and an unknown input fails visibly.

Predict first: after `valid, timeout, valid`, what state should the machine
end in?

Likely AI drift: it may treat an input as a state, add an unstated state, or
silently ignore an unknown input.

Recovery: compare the declared transition table with the trace one input at a
time; use the reference model as the source of truth.
# Prompt 05 — Find the missing transition

Why: a model validator can expose what the state machine forgot to represent.

Slide reference: Week 14 Tuesday, the model-limit check.

```prompt-a
Write a validator for a finite-state machine whose declared states are Locked and Open and whose input alphabet is valid and timeout. The intentionally incomplete transition table contains only (Locked, valid) -> Open. List every missing (state, input) pair in deterministic order. The validator must identify exactly (Open, timeout) as the missing transition needed by the badge trace. Do not assume an implicit self-loop counts as a declared transition. Explain in one sentence what this validator can establish and what it cannot establish about a real access system.
```

Expected observable result: the missing-transition list names exactly
`("Open", "timeout")`; an implicit self-loop is not accepted as a declaration.

Predict first: which state/input pair is absent from the incomplete model?

Likely AI drift: it may fill the gap automatically, report only a count, or
claim the model proves real authorization.

Recovery: enumerate the Cartesian product of declared states and inputs, then
compare it with the explicit transition keys.

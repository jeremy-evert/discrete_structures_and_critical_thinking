# Concept map — what the check catches

Read each row as: **idea → everyday meaning → evidence/check → failure
caught**; the arrows mean “leads to.” The examples use only fictional,
bounded situations. A **claim** is a statement someone wants a check to
support. **Evidence** is the checkable result, such as rows or a trace, that
supports or challenges the claim. A **proof** here is a check that covers
every case. An **AI assistant** is a tool that generates text or code; its
output is a claim to check, not evidence by itself. A **self-loop** is a
transition that leaves a machine in the same state.

| Concept | Everyday meaning | Evidence / check | Failure caught |
|---|---|---|---|
| Boolean variable | A named switch whose value is true or false | State the variable names and allowed values | A hidden third value or an unstated input |
| Assignment | One choice of a value for every variable; an allowed assignment is any combination of `True`/`False` for the variables | Write the complete row, such as `P=False, Q=True` | Checking only the convenient case |
| Boolean expression | A rule that turns variable values into true or false | Evaluate the rule for each assignment | A confident answer with no visible work |
| Gate / circuit | One Boolean operation / connected operations drawn as a path | Match each gate to the written expression | A picture that does not match the formula |
| Truth table | A list of all assignments and outputs | Include all four rows for two variables | Missing the one row that breaks a claim |
| Equivalence | Same output in every allowed case | Compare two output columns row by row | Accepting a familiar but false simplification |
| Counterexample | One allowed case that breaks a universal claim | Show `P=False, Q=True` for the false `B` claim | Saying “it works” after checking only three rows |
| Satisfiable | True in at least one allowed case | Find and print one satisfying assignment | Confusing “sometimes true” with “always true” |
| Witness | The specific case that demonstrates satisfiability | Record the assignment, not just “yes” | Giving a vague example that cannot be checked |
| Tautology | True in every allowed case | Check every row; `P=False` defeats tautology of `P` | Treating one witness as universal proof |
| State | A named situation in a bounded model | List states before writing transitions | Smuggling in a condition the model never named |
| Input | In a Boolean expression, a value supplied to an operation; in a state model, an event supplied to the machine | List the allowed Boolean values or machine events, such as `valid` and `timeout` | Confusing a Boolean value with an unlisted machine event |
| Transition | A rule from current state plus input to next state | List each expected state/input pair explicitly | A missing rule becoming an unannounced self-loop |
| Start state | The situation where a run begins | Mark `Locked` before tracing any input | A trace with no agreed starting point |
| Trace | The ordered states and events produced by a run | `Locked --valid--> Open` means that `valid` takes the machine from Locked to Open; plain `A -> B` means A leads to B | A diagram that never gets tested with an event sequence |
| Model limit / boundary | A relevant fact the model does not represent; the boundary separates represented facts from what is left out | Name one fact it cannot establish, such as authorization | Overclaiming that a small model describes a real system |
| False simplification | A shorter expression claimed to have the same meaning | Exhaustively compare the original and shorter forms | Trusting an AI rewrite because it looks familiar |
| Witness versus tautology | “At least one” versus “every one” | Ask which question the evidence answers; `P=True` says variable `P` has value `True` | Reporting one witness as proof that `P` is always true |
| Missing transition | A state/event pair with no stated next state | Check every promised state/event pair and name the gap | Hiding an omitted case with an assumed self-loop |

## Use the map in the predict–run–explain loop

1. **Predict:** write the row, witness, or next state you expect.
2. **Run:** perform the complete table check or trace the explicit rules.
3. **Explain:** state the strongest conclusion supported by the evidence and
   one boundary that remains.

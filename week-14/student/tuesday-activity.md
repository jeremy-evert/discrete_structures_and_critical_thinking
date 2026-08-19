# Tuesday activity — A truth table and a trace are evidence

Work individually first. Consider the expression

```text
E = (P AND Q) OR (P AND NOT Q)
```

and the proposed simplification `S = P`.

## Boolean check

1. Under **Sources**, identify this supplied expression and its proposed
   simplification.
2. Under **Rules / Assumptions**, define `AND`, `OR`, and `NOT`; state that
   `P` and `Q` each receive a Boolean value.
3. Under **Work**, complete all four rows of a truth table for `E` and `S`.
   Explain whether the expressions are equivalent. Then give an assignment
   that satisfies `P AND Q`; explain why that one assignment does *not* prove
   a different statement is universally true.
4. Under **Check**, independently recompute one row or have a peer check a
   row and reconcile any difference.

## State-model check

An access badge model has states `Locked` and `Open`. Input `valid` changes
`Locked → Open`; input `timeout` changes `Open → Locked`; all other inputs
leave the state unchanged.

5. Trace inputs `valid, timeout, valid` from `Locked`.
6. Name one relevant condition this two-state model cannot establish (for
   example, whether a person was authorized to receive the badge). Do not add
   facts that the model never represented.
7. Write a one-sentence conclusion that distinguishes what the truth table or
   trace proves from what the model leaves open.

## AI Fluency check

An AI can produce a confident simplification or state diagram with one missing
case. Before trusting it, enumerate the input assignments or trace the stated
inputs yourself. If you use AI, record the exact row or transition you checked;
if not, name the check you would demand.

# Prompt 04 - Trace a finite-state machine

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

Likely AI mistake: it may treat an input as a state, add an unstated state, or
silently ignore an unknown input.

Recovery: compare the declared transition table with the trace one input at a
time; use the reference model as the source of truth.

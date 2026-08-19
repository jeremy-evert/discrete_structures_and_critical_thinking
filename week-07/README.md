# Week 7 — Integer Properties & Cryptography

**Tuesday, September 29; Thursday, October 1, 2026**  
COMSC-2043-1420 · 12:30–1:45 PM · Stafford 259

## Purpose

This week uses divisibility, congruence, greatest common divisors, and a
small reversible shift cipher to ask a harder question: **what assumptions
make a security claim true, and what does an adversary know?**

Bring forward the Week 1 method: **Sources → Rules/Assumptions → Work →
Check → One-Sentence Summary**. You should be able to show why a decode
works, not merely report that it seemed to work once.

## Learning targets

- Compute and explain congruence modulo a positive integer.
- Use a gcd calculation to decide whether a modular inverse can exist.
- Encode and decode a small shift-cipher message and check the round trip.
- State the assumptions and limits of a simple cryptographic claim.

## This week's evidence

- Tuesday: complete the modular-arithmetic and cipher activity in
  `student/tuesday-activity.md`; preserve its worked example as your Tuesday
  technical-evidence trace.
- Thursday: complete the Pair Reasoning challenge and your individual report
  using `../assignments/pair-reasoning-report.md`.
- **Reasoning Odyssey Checkpoint 1:** submit the individual synthesis in
  `student/odyssey-checkpoint-1.md`. It is this week's only Odyssey
  submission. Do **not** create a separate ordinary Decision Gate for Week 7.

The checkpoint asks you to connect evidence from Weeks 4–7; it is not a new
cryptography project. Exact submission location and due date are provided by
the course system when published.

## AI check

AI may propose computations or an attack story. Check every claimed modular
inverse, round trip, and security conclusion yourself. A fluent answer that
does not name an attacker model or a number-theory assumption is incomplete.

**Provenance:** `planning/fall-2026-topic-map.md`; `planning/fall-2026-weekly-architecture.md`; historical content quarry `lessons/05-cryptography.md`; recurring contracts in `assignments/pair-reasoning-report.md` and `docs/grading-model.md`.

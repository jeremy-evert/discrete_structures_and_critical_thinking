# Week 13 Tuesday: Counting, Carrying, and Circuits

**Big question:** How does a computer add and multiply, and what does carrying really mean?

**Carrying** is what happens when a place runs out of symbols. In decimal, 9 + 1 runs out of digits, so we write 0 in that place and add 1 to the next place: 10. The same rule works in every number system. **Binary** is the number system with only two symbols, 0 and 1. A **circuit** is a connected set of simple on/off parts. **Boolean algebra** is the math of values that are only 0 or 1.

## Start here

1. Open the [slides]({{FILE_URL:boolean_binary_slides.pdf}}) (`{{FILE:boolean_binary_slides.pdf}}`).
2. Open the two-page [handout]({{FILE_URL:boolean_binary_handout.pdf}}) (`{{FILE:boolean_binary_handout.pdf}}`). It has the truth tables for the half adder and the full adder.

## What we will do

- Carry in decimal, octal, and hexadecimal, and in a number system made of circles, stars, faces, and fish.
- Add and multiply in binary, using the same method as on paper in decimal.
- Meet AND, OR, NOT, and XOR, and see why Boolean 1 + 1 = 1 but binary 1 + 1 = 10.
- Build a **half adder** (adds two bits) and a **full adder** (adds two bits and a carry-in) from gates.
- See why chaining adders is slow (a **ripple-carry adder**) and how a **carry-lookahead adder** speeds it up.

## Check yourself

A **truth table** lists every possible input and what the circuit gives back. If it lists all of them, it proves the circuit works. One correct example does not.

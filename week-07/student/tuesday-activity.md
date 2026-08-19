# Tuesday activity — Can the cipher claim survive a check?

Work individually first. A calculator or a short local program may help, but
show the reasoning that lets another person check it.

## Worked example: an inspectable shift cipher

Represent letters by `A = 0, B = 1, …, Z = 25`. With key `k = 7`, encryption
is `E(x) = x + 7 (mod 26)` and decryption is `D(y) = y - 7 (mod 26)`.

For `T`, `x = 19`, so `E(19) = 26 = 0 (mod 26)`: `T` encrypts to `A`.
Checking the return trip, `D(0) = -7 = 19 (mod 26)`: `A` decrypts to `T`.
The check is not “the letters look plausible”; it is that `D(E(x)) = x` for
the stated rule.

## Your reasoning trace

1. Compute `53 (mod 12)`, `-5 (mod 12)`, and `gcd(35, 26)`. State what each
   result means.
2. Encode `MATH` using the key `7`, then decode your result. Show one
   letter's arithmetic and check the full round trip.
3. A classmate says, “This cipher is secure because nobody knows my key.”
   Name two assumptions hidden in that claim, including one about what an
   adversary can observe or try.
4. Use the five headings below for your exit evidence:
   - **Sources:** the alphabet representation and cipher rules used
   - **Rules / Assumptions:** modulus, key, and attacker knowledge
   - **Work:** your calculations
   - **Check:** round trip plus one attempted challenge
   - **One-Sentence Summary:** what the cipher rule establishes—and what it
     does not establish

## AI fluency check

Ask an AI only if useful to generate a second cipher example. Independently
check its arithmetic. If it calls the cipher “secure,” ask: secure against
which attacker, with what information, and why?

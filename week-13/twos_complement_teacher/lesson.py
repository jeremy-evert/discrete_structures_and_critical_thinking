"""Friendly narration and terminal presentation; arithmetic lives in twos."""
import random
from twos import from_twos, ones_complement, range_for, subtract, to_binary, twos_complement


def why(bits: int) -> None:
    """Explain modular arithmetic using a fixed-width number wheel."""
    print(f"THE BIG IDEA: WHY TWO'S COMPLEMENT WORKS ({bits} bits)")
    print(f"An {bits}-bit register counts 0 through {2**bits - 1}, then wraps to 0.")
    print("Think of a car odometer, or a clock. The wheel has no end.")
    print(f"One step BACK from zero is {'1' * bits}. That pattern behaves like -1.")
    print(f"Let M = 2^{bits} = {2**bits}. Adding M changes nothing after carry-out is dropped.")
    print("So -x and M-x land at the same place: arithmetic modulo M.")
    print("Flip x: (M-1)-x. Add 1: (M-1)-x+1 = M-x. That's the recipe!")
    print("For x=0, M wraps back to 0 too. Only one zero. Nice.")
    print("\n4-bit wheel (clockwise unsigned count; signed labels outside):")
    print(r"""
                         0:0000
              -1:1111              +1:0001
       -2:1110                            +2:0010
   -3:1101                                    +3:0011
 -4:1100                clockwise ->             +4:0100
   -5:1011                                    +5:0101
       -6:1010                            +6:0110
              -7:1001              +7:0111
                        -8:1000
""")
    print("Same circle, two readings. After +7 comes -8; after -1 comes 0.")
    print(f"CHECK: Python says {(-1) % (2**bits)}, we got {int('1' * bits, 2)} (unsigned -1 pattern)")


def negate(n: int, bits: int) -> None:
    """Narrate fixed-width negation, including its asymmetric endpoint."""
    low, high = range_for(bits)
    if not low <= n <= high:
        raise ValueError(f"Signed value must be between {low} and {high}.")
    original = to_binary(n % (2**bits), bits)
    flipped = ones_complement(original)
    result = twos_complement(original)
    print(f"Negate {n} in {bits} bits:")
    print(f"  1. Write {n:>6}: {original}")
    print(f"  2. Flip bits  : {flipped}")
    print(f"  3. Add 1      : {result} (carry-out {int(flipped, 2) // (2**bits - 1)}, discarded)")
    got = from_twos(result)
    print(f"  Signed meaning: {got}")
    if n == low:
        print(f"  OVERFLOW: {low} has no positive twin; {-n} does not fit. The pattern stays the same.")
    print(f"CHECK: Python says {-n}, we got {got}" + (" (OVERFLOW; fixed-width wrap)" if got != -n else ""))


def walkthrough(a: int, b: int, bits: int, color: bool = False) -> None:
    """Show operands, negation, the carry grid, and a Python sanity check."""
    t = subtract(a, b, bits)
    def highlight(text: str) -> str:
        return f"\033[36m{text}\033[0m" if color else text
    print(f"\n{a} - ({b}) in {bits} bits = {a} + (-({b}))")
    print(f"  a          {t.a_binary} ({a})\n  b          {t.b_binary} ({b})")
    print(f"  flip b     {highlight(t.flipped_b)}")
    print(f"  +1         {t.negated_b}  (negation carry-out {int(t.flipped_b, 2) == 2**bits - 1:d}, discarded)")
    print("  Carries above each bit are carry-IN; columns run MSB to LSB.")
    print("  carries    " + highlight(" ".join(map(str, reversed(t.addition.carries[:-1])))))
    print("             " + " ".join(t.a_binary))
    print("  +          " + " ".join(t.negated_b))
    print("             " + "--" * bits)
    print("             " + " ".join(t.addition.result))
    print(f"  Discarded carry-out: {t.addition.carry_out} (not a sign bit)")
    print("  Work right to left (bit 0 is the rightmost column):")
    for i, (x, y) in enumerate(zip(reversed(t.a_binary), reversed(t.negated_b))):
        carry = t.addition.carries[i]
        total = int(x) + int(y) + carry
        print(f"    bit {i:2}: {x} + {y} + carry {carry} = {total}; write {total % 2}, carry {total // 2}")
    print(f"  Binary result: {t.addition.result}; signed meaning: {t.signed_result}")
    if t.signed_result < 0:
        magnitude = twos_complement(t.addition.result)
        print(f"  Read a negative answer: flip -> {ones_complement(t.addition.result)}, +1 -> {magnitude}.")
        print(f"  Magnitude {int(magnitude, 2)}, so the answer reads -{int(magnitude, 2)}.")
    print(f"  Addition carry into sign / out: {t.addition.carries[-2]} / {t.addition.carry_out}.")
    c = t.subtraction_carries
    print(f"  Subtraction a + ~b + 1 carries into sign / out: {c[-2]} / {c[-1]}.")
    print("  Unequal carries in that subtraction operation mean signed overflow.")
    if b == range_for(bits)[0]:
        print("  Here -b has no positive twin. Use the subtraction carries, not the wrapped -b addition flag.")
    print("  OVERFLOW: exact answer is outside the signed range." if t.overflow else "  No signed overflow.")
    print(f"CHECK: Python says {t.exact_result}, we got {t.signed_result}" +
          (f" (OVERFLOW; Python wrapped to {bits} bits says {from_twos(to_binary(t.exact_result % (2**bits), bits))})" if t.overflow else ""))


def overflow_lesson(bits: int, color: bool = False) -> None:
    """Give a separate overflow demonstration and handling advice."""
    low, high = range_for(bits)
    print(f"\nOVERFLOW LAB: range {low} through {high}")
    print("Carry-out alone does not detect signed overflow. Compare carry INTO the sign bit with carry OUT.")
    print("For subtraction use a + ~b + 1, with the initial carry set to 1.")
    print("For ordinary addition, start the carry at 0. Different carries mean overflow.")
    if bits == 8:
        walkthrough(100, -50, bits, color)
    else:
        walkthrough(high, -1, bits, color)
    walkthrough(low, 1, bits, color)
    print("Handling: flag the result before using it as a signed answer.")
    print("Use Python's exact integer answer, or widen BOTH operands and repeat.")
    print("Do not just attach extra zeros to a negative pattern: extend its sign bit.")
    print(f"Special case: {low} has no positive twin in {bits} bits.")
    negate(low, bits)


def guided(bits: int, pause: bool, color: bool) -> None:
    """Present the lesson in pedagogical order."""
    print("THE PROBLEM: How do we write -5 in binary?")
    print("Sign-magnitude reserves a sign bit: 0101 is +5; 1101 is -5 (4 bits).")
    print("But 0000 is +0 and 1000 is -0. Two zeros! Addition also needs sign cases.")
    if pause:
        input("Press Enter to continue...")
    why(bits)
    if pause:
        input("Press Enter to continue...")
    print("\nTHE RECIPE: write the positive number, flip every bit, add 1.")
    negate(5, bits)
    if pause:
        input("Press Enter to continue...")
    print("\nSUBTRACTION = ADDITION IN DISGUISE: a - b = a + (-b)")
    examples = [(9, 5), (5, 9), (7, 7), (0, 1), (-3, 4)]
    if bits == 4:
        print("9 does not fit signed 4 bits; use 6 - 3 and 3 - 6 for these two examples.")
        examples[:2] = [(6, 3), (3, 6)]
    for a, b in examples:
        walkthrough(a, b, bits, color)
        if pause:
            input("Press Enter to continue...")
    overflow_lesson(bits, color)


def table(bits: int) -> None:
    """Print all unsigned patterns and their signed readings."""
    print(f"{'Unsigned':>8}  {'Binary':>{bits}}  {'Signed':>8}")
    for n in range(2**bits):
        pattern = to_binary(n, bits)
        print(f"{n:8}  {pattern}  {from_twos(pattern):8}")


def quiz(bits: int) -> None:
    """Run ten randomized practice questions with immediate feedback."""
    low, high = range_for(bits)
    score = 0
    kinds = list(range(4)) * 2 + random.choices(range(4), k=2)
    random.shuffle(kinds)
    print("Ungraded practice. Enter decimal answers; overflow answers use yes/no.")
    for index, kind in enumerate(kinds, 1):
        a, b = random.randint(low, high), random.randint(low, high)
        if kind == 0:
            a = random.randint(-high, high)
            prompt, expected = f"Negate {a} (signed decimal)", str(-a)
        elif kind == 1:
            prompt, expected = f"{a} - ({b}) (wrapped signed decimal)", str(subtract(a, b, bits).signed_result)
        elif kind == 2:
            prompt, expected = f"Signed value of {to_binary(a % (2**bits), bits)}", str(a)
        else:
            prompt = f"Will {a} - ({b}) overflow in {bits} bits? (yes/no)"
            expected = "yes" if subtract(a, b, bits).overflow else "no"
        answer = input(f"{index}/10: {prompt}: ").strip().lower()
        try:
            correct = str(int(answer)) == expected if kind != 3 else answer == expected
        except ValueError:
            correct = False
        score += correct
        print("Correct! The bits salute you." if correct else f"Not quite. Answer: {expected}. No bits were harmed.")
        if kind in (1, 3):
            walkthrough(a, b, bits)
        elif kind == 0:
            negate(a, bits)
        else:
            print(f"CHECK: Python says {a}, we got {from_twos(to_binary(a % (2**bits), bits))}")
    print(f"Final score: {score}/10. Your odometer of knowledge keeps rolling.")

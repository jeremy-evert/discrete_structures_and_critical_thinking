# Two's Complement Teacher

A Python 3.10+ command-line teaching tool for first-year CS students who know binary but have not met negative binary numbers. An odometer analogy and a 4-bit number wheel explain why two's complement works before introducing the recipe, narrated subtraction, and a separate overflow lab. Uses only the standard library. Practice is ungraded and does not save or transmit responses.

From the repository root, open the tool's directory and check Python:

```console
cd week-13/twos_complement_teacher
python --version
```

Python 3.10 or newer is required. No packages or installation steps are needed.
On Windows, if `python` is unavailable, use `py -3` in its place.

Start with `python main.py --lesson`. Run these commands from this directory:

```console
python main.py --lesson
python main.py --lesson --no-pause --no-color
python main.py --why --bits 4
python main.py --subtract 5 9
python main.py --subtract -3 4 --bits 16
python main.py --negate 5
python main.py --table --bits 4
python main.py --quiz --bits 8
python main.py --overflow --bits 8
python -m unittest
python main.py --help
```

All modes accept `--bits 4`, `8` (default), or `16`. `--no-color` disables highlighting; redirected output automatically uses plain text. The full lesson pauses between sections and subtraction examples unless `--no-pause` is supplied. The 16-bit table intentionally prints all 65,536 rows. Quiz answers are decimal integers, except overflow questions, which accept `yes` or `no`. EOF or Ctrl+C exits interactive practice gracefully.

## Teaching notes for instructors

Suggested 20-minute flow: spend 2 minutes on sign-magnitude's two zeros; 5 minutes with `--why`, tracing the wheel backward from zero and deriving flip-plus-one; 3 minutes on `--negate 5`; 5 minutes on `--subtract 9 5`, `--subtract 5 9`, and `--subtract 0 1`; 3 minutes on the separate `--overflow` lab; and 2 minutes on quiz practice and questions. Ask students to predict carries before revealing a walkthrough. If you turn practice into a graded deliverable, use a course discussion so peers can see and learn from each other's work.

## API choices and edge cases

`to_binary` is strictly unsigned: encode a signed integer with `to_binary(n % (2**bits), bits)`. Signed CLI operands must fit the chosen signed range. Pattern-only functions accept any nonempty binary string; width-based operations support 4, 8, and 16.

The specification asks for both a three-field addition result and per-column carries. `add_binary` therefore returns an immutable `Addition` dataclass with `result`, `carry_out`, `overflow`, and `carries`. Carries are indexed from the least significant bit: `carries[0]` is the initial zero, `carries[bits-1]` enters the sign bit, and `carries[bits]` leaves it. `subtract` returns an immutable `Subtraction` trace.

Signed addition overflow is carry into sign XOR carry out. Subtraction also records the carries for the equivalent single operation `a + ~b + 1` (initial carry 1). Those carries detect subtraction overflow even when negating the most negative operand wraps to itself. The separate addition of the already-negated pattern can have a different overflow flag in that special case; the trace's top-level `overflow` is the authoritative subtraction flag.

Overflow walkthroughs show Python's exact answer and the wrapped signed answer honestly: they cannot print equal values when overflow occurred. A second Python modulo check verifies the wrapped result. The most negative number has no representable positive twin. For 4-bit lessons, 6-3 and 3-6 replace examples using the unrepresentable operand 9; the overflow lab uses the selected width's endpoints. Eight-bit lessons include exactly 100-(-50) and -128-1. Sixteen-bit lessons use 16-bit endpoints so overflow is still demonstrated.

The tests exhaust every signed 4- and 8-bit value for encoding, flipping, negation, and decoding; every 4-bit addition and signed subtraction pair; every carry column; invalid inputs; endpoints and presentation smoke checks. Pure arithmetic functions never print. Verification transcripts are saved alongside this README.

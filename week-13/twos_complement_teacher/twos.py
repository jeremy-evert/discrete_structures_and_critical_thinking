"""Pure fixed-width binary arithmetic for the teaching CLI."""
from dataclasses import dataclass


def range_for(bits: int) -> tuple[int, int]:
    """Return the inclusive signed range for a supported width."""
    if type(bits) is not int or bits not in (4, 8, 16):
        raise ValueError("Choose 4, 8, or 16 bits.")
    return -(1 << (bits - 1)), (1 << (bits - 1)) - 1


def to_binary(n: int, bits: int) -> str:
    """Encode an unsigned integer without silently wrapping it."""
    range_for(bits)
    if type(n) is not int or not 0 <= n < 1 << bits:
        raise ValueError(f"Unsigned value must be between 0 and {(1 << bits) - 1}.")
    return format(n, f"0{bits}b")


def _validate(pattern: str) -> None:
    """Require a nonempty binary string."""
    if not isinstance(pattern, str) or not pattern or set(pattern) - {"0", "1"}:
        raise ValueError("Use a nonempty string containing only 0 and 1.")


def ones_complement(bits_str: str) -> str:
    """Flip each bit without changing the width."""
    _validate(bits_str)
    return "".join("1" if bit == "0" else "0" for bit in bits_str)


def twos_complement(bits_str: str) -> str:
    """Flip and increment, discarding any carry beyond the width."""
    flipped = list(ones_complement(bits_str))
    for index in range(len(flipped) - 1, -1, -1):
        if flipped[index] == "0":
            flipped[index] = "1"
            break
        flipped[index] = "0"
    return "".join(flipped)


def from_twos(bits_str: str) -> int:
    """Interpret a binary pattern as a signed two's-complement value."""
    _validate(bits_str)
    unsigned = int(bits_str, 2)
    return unsigned - (1 << len(bits_str)) if bits_str[0] == "1" else unsigned


@dataclass(frozen=True)
class Addition:
    """Addition result; carries[i] enters bit i, starting at the right."""
    result: str
    carry_out: int
    overflow: bool
    carries: tuple[int, ...]


def add_binary(a: str, b: str, bits: int) -> Addition:
    """Ripple through equal-width patterns and record every carry."""
    range_for(bits)
    _validate(a)
    _validate(b)
    if len(a) != bits or len(b) != bits:
        raise ValueError(f"Both patterns must contain exactly {bits} bits.")
    carries = [0]
    result = []
    for left, right in zip(reversed(a), reversed(b)):
        total = int(left) + int(right) + carries[-1]
        result.append(str(total % 2))
        carries.append(total // 2)
    return Addition("".join(reversed(result)), carries[-1],
                    carries[-2] != carries[-1], tuple(carries))


@dataclass(frozen=True)
class Subtraction:
    """All intermediate patterns and both arithmetic and signed results."""
    a: int
    b: int
    bits: int
    a_binary: str
    b_binary: str
    flipped_b: str
    negated_b: str
    addition: Addition
    subtraction_carries: tuple[int, ...]
    signed_result: int
    exact_result: int
    overflow: bool


def subtract(a: int, b: int, bits: int) -> Subtraction:
    """Compute a-b modulo the width and detect signed subtraction overflow."""
    low, high = range_for(bits)
    if any(type(n) is not int or not low <= n <= high for n in (a, b)):
        raise ValueError(f"Signed operands must be between {low} and {high} for {bits} bits.")
    mask = (1 << bits) - 1
    left, right = to_binary(a & mask, bits), to_binary(b & mask, bits)
    flipped = ones_complement(right)
    negated = twos_complement(right)
    addition = add_binary(left, negated, bits)
    # a + ~b + 1 is one ripple operation with initial carry 1.
    # It detects subtraction overflow even when -b cannot be represented.
    carries = [1]
    for x, y in zip(reversed(left), reversed(flipped)):
        carries.append((int(x) + int(y) + carries[-1]) // 2)
    return Subtraction(a, b, bits, left, right, flipped, negated, addition,
                       tuple(carries), from_twos(addition.result), a - b,
                       carries[-2] != carries[-1])

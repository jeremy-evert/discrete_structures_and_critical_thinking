"""Exhaustive small-width checks against Python integer arithmetic."""
import contextlib
import io
import unittest
from unittest.mock import patch
import lesson
from twos import (range_for, to_binary, ones_complement, twos_complement,
                  from_twos, add_binary, subtract, _validate)


class ArithmeticTests(unittest.TestCase):
    def test_ranges_and_round_trips(self):
        for bits in (4, 8, 16):
            low, high = range_for(bits)
            self.assertEqual((low, high), (-(2**(bits-1)), 2**(bits-1)-1))
            values = range(low, high+1) if bits != 16 else (low, -1, 0, 1, high)
            for n in values:
                pattern = to_binary(n % (2**bits), bits)
                self.assertEqual(pattern, format(n % (2**bits), f'0{bits}b'))
                self.assertEqual(from_twos(pattern), n)
                self.assertEqual(int(ones_complement(pattern), 2), (2**bits-1) - int(pattern, 2))
                negative = twos_complement(pattern)
                self.assertEqual(int(negative, 2), (-n) % (2**bits))
                self.assertEqual(twos_complement(negative), pattern)
                self.assertEqual(from_twos(negative), ((-n-low) % (2**bits))+low)
        self.assertEqual(twos_complement('10000000'), '10000000')
        self.assertEqual(from_twos('10000000'), -128)

    def test_addition_exhaustive(self):
        for a in range(16):
            for b in range(16):
                t = add_binary(to_binary(a, 4), to_binary(b, 4), 4)
                self.assertEqual(int(t.result, 2), (a+b) % 16)
                self.assertEqual(t.carry_out, (a+b)//16)
                signed_sum = from_twos(to_binary(a, 4)) + from_twos(to_binary(b, 4))
                self.assertEqual(t.overflow, not -8 <= signed_sum <= 7)
                for i in range(5):
                    self.assertEqual(t.carries[i], ((a % (2**i)) + (b % (2**i))) // (2**i))

    def test_subtraction_all_pairs(self):
        for a in range(-8, 8):
            for b in range(-8, 8):
                t = subtract(a, b, 4)
                self.assertEqual(t.exact_result, a-b)
                self.assertEqual(t.signed_result, ((a-b+8) % 16)-8)
                self.assertEqual(t.overflow, not -8 <= a-b <= 7)
                self.assertEqual(int(t.addition.result, 2), (a-b) % 16)
                self.assertEqual(int(t.flipped_b, 2), 15-(b % 16))
                self.assertEqual(int(t.negated_b, 2), (-b) % 16)
                for i in range(5):
                    mask = 2**i-1
                    expected = (((a % 16) & mask) + ((15-(b % 16)) & mask) + 1) // (2**i)
                    self.assertEqual(t.subtraction_carries[i], expected)
        for a, b in ((100, -50), (-128, 1), (0, -128), (-128, -128)):
            t = subtract(a, b, 8)
            self.assertEqual(t.overflow, not -128 <= a-b <= 127)
            self.assertEqual(t.signed_result, ((a-b+128) % 256)-128)

    def test_validation(self):
        for bits in (0, 3, 32, True):
            with self.assertRaises(ValueError):
                range_for(bits)
        for n in (-1, 256):
            with self.assertRaises(ValueError):
                to_binary(n, 8)
        for pattern in ('', '102', ' hello', 5):
            for function in (_validate, ones_complement, twos_complement, from_twos):
                with self.assertRaises(ValueError):
                    function(pattern)
        with self.assertRaises(ValueError):
            add_binary('0', '0000', 4)
        with self.assertRaises(ValueError):
            subtract(8, 0, 4)


class PresentationTests(unittest.TestCase):
    def test_lesson_and_modes(self):
        for bits in (4, 8, 16):
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                lesson.guided(bits, False, False)
            text = output.getvalue()
            self.assertIn('OVERFLOW LAB', text)
            self.assertIn('CHECK: Python says', text)
            self.assertNotIn('\033', text)
        with contextlib.redirect_stdout(io.StringIO()) as output:
            lesson.table(4)
        self.assertEqual(len(output.getvalue().splitlines()), 17)

    def test_quiz_feedback(self):
        with patch('builtins.input', return_value='invalid'), contextlib.redirect_stdout(io.StringIO()) as output:
            lesson.quiz(4)
        self.assertIn('Final score: 0/10', output.getvalue())
        self.assertEqual(output.getvalue().count('No bits were harmed.'), 10)


if __name__ == '__main__':
    unittest.main()

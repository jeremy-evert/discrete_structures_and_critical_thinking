import pathlib
import sys
import unittest
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'week-10' / 'monty-hall'))
from monte_carlo_playground_sim import simulate, simulate_three_prisoners

class PlaygroundTests(unittest.TestCase):
    def test_buffon_estimates_pi(self):
        result = simulate('buffon', 100_000, 20261022)
        self.assertLess(abs(result['estimate'] - 3.14159), .08)

    def test_darts_estimates_pi(self):
        result = simulate('darts', 100_000, 20261022)
        self.assertLess(abs(result['estimate'] - 3.14159), .03)

    def test_birthday_23(self):
        result = simulate('birthday', 100_000, 20261022, 23)
        self.assertAlmostEqual(result['true'], .5073, places=3)
        self.assertLess(abs(result['measured'] - result['true']), .01)

    def test_coupon_expectations(self):
        for n in (10, 50):
            result = simulate('coupon', 30_000, 99, n)
            self.assertLess(abs(result['measured'] - result['true']), result['true'] * .025)

    def test_secretary_finite_n_and_limit(self):
        result = simulate('secretary', 50_000, 20261022, 100)
        self.assertEqual(result['skip'], 36)
        self.assertLess(abs(result['measured'] - result['true']), .01)
        self.assertLess(abs(result['true'] - 1 / 2.718281828459045), .02)

    def test_three_prisoners_conditional_rates(self):
        result = simulate_three_prisoners(300_000, 12)
        self.assertLess(abs(result['A_given_B_named'] - 1/3), .01)
        self.assertLess(abs(result['C_given_B_named'] - 2/3), .01)

if __name__ == '__main__':
    unittest.main()

import unittest
from miracle_math import probability_of_streak, chance_at_least_once


class TestStreaks(unittest.TestCase):
    def test_ten_heads_in_a_row_is_one_in_1024(self):
        chance = probability_of_streak(0.5, 10)
        self.assertAlmostEqual(chance, 1 / 1024, places=10)


class TestAtLeastOnce(unittest.TestCase):
    def test_de_mere_one_six_in_four_rolls_is_a_winning_bet(self):
        chance = chance_at_least_once(1 / 6, 4)
        self.assertAlmostEqual(chance, 0.5177, places=4)

    def test_de_mere_double_six_in_twenty_four_rolls_is_a_losing_bet(self):
        chance = chance_at_least_once(1 / 36, 24)
        self.assertLess(chance, 0.5)


class TestAtLeastOnceEdgeCases(unittest.TestCase):
    def test_zero_tries_never_succeeds(self):
        chance = chance_at_least_once(0.5, 0)
        self.assertAlmostEqual(chance, 0, places=10)

    def test_impossible_event_never_happens(self):
        chance = chance_at_least_once(0, 100)
        self.assertAlmostEqual(chance, 0, places=10)

    def test_certain_event_always_happens(self):
        chance = chance_at_least_once(1, 3)
        self.assertAlmostEqual(chance, 1, places=10)


if __name__ == "__main__":
    unittest.main(verbosity=2)

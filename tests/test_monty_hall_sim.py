import pathlib
import subprocess
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "week-10" / "monty-hall"))
from monty_hall_sim import Mulberry32, simulate  # noqa: E402


class Mulberry32Tests(unittest.TestCase):
    def test_known_values(self):
        rng = Mulberry32(0)
        expected = [0.26642920868471265, 0.0003297457005828619, 0.2232720274478197]
        for value in expected:
            self.assertEqual(rng.random(), value)


class SimulationTests(unittest.TestCase):
    def test_seeded_run_is_deterministic(self):
        self.assertEqual(simulate(1000, 321), simulate(1000, 321))

    def test_knowing_host_rates_follow_closed_form(self):
        result = simulate(100_000, 20261022)
        self.assertEqual(result.spoiled, 0)
        self.assertLess(abs(result.stay_rate - 1 / 3), 0.01)
        self.assertLess(abs(result.switch_rate - 2 / 3), 0.01)

    def test_one_hundred_doors(self):
        result = simulate(100_000, 18, doors=100)
        self.assertLess(abs(result.switch_rate - 99 / 100), 0.005)

    def test_random_host_reports_spoiled_games_and_conditional_rates(self):
        result = simulate(120_000, 99, doors=3, host_random=True)
        self.assertLess(abs(result.spoiled / result.games - 1 / 3), 0.01)
        self.assertLess(abs(result.stay_rate - 0.5), 0.01)
        self.assertLess(abs(result.switch_rate - 0.5), 0.01)

    def test_cli_smoke(self):
        script = pathlib.Path(__file__).resolve().parents[1] / "week-10" / "monty-hall" / "monty_hall_sim.py"
        output = subprocess.check_output(
            [sys.executable, str(script), "--games", "10", "--seed", "7"], text=True
        )
        self.assertIn("Games: 10  Doors: 3  Seed: 7", output)
        self.assertIn("Spoiled: 0", output)

    def test_rejects_invalid_parameters(self):
        with self.assertRaises(ValueError):
            simulate(0, 1)
        with self.assertRaises(ValueError):
            simulate(1, 1, doors=2)


if __name__ == "__main__":
    unittest.main()

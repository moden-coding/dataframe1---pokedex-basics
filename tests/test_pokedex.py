import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

try:
    import numpy as np
    import pandas as pd
except ModuleNotFoundError:
    raise ModuleNotFoundError(
        "pandas isn't installed for the Python that is running these tests:\n"
        f"    {sys.executable}\n"
        "Select the conda/Anaconda interpreter (Cmd/Ctrl+Shift+P → Python: Select Interpreter), "
        "trash the terminal and open a new one. "
        "If you have the extension 'Python Test Explorer for Visual Studio Code', "
        "uninstall it and run tests from the 'Python Tests' tree."
    ) from None

from src.pokedex import stat_summary, strongest, category_report

REAL = pd.read_csv(ROOT / "data" / "pokemon.csv")

MINI = pd.DataFrame({
    "Name":   ["Sprout", "Ember", "Ripple", "Pebble", "Gust", "Bolt", "Mossy"],
    "Type 1": ["Grass", "Fire", "Water", "Rock", "Grass", "Electric", "Grass"],
    "Type 2": [np.nan, "Flying", np.nan, "Ground", "Flying", "Flying", np.nan],
    "HP":     [45, 39, 44, 80, 40, 35, 60],
    "Attack": [49, 52, 48, 90, 45, 55, 70],
    "Speed":  [45, 65, 43, 20, 56, 90, 40],
})


class TestStatSummary(unittest.TestCase):
    def check(self, result, count, mean, maximum):
        self.assertIsInstance(result, tuple, "should return a tuple")
        self.assertEqual(len(result), 3, "tuple should have 3 items")
        self.assertEqual(result[0], count, "row count is wrong")
        self.assertAlmostEqual(result[1], mean, places=1, msg="mean should be rounded to 1 decimal")
        self.assertEqual(result[2], maximum, "max is wrong")

    def test_real_data_attack(self):
        self.check(stat_summary(REAL, "Attack"), 800, 79.0, 190)

    def test_small_table(self):
        self.check(stat_summary(MINI, "HP"), 7, 49.0, 80)

    def test_works_on_any_column(self):
        self.check(stat_summary(MINI, "Speed"), 7, 51.3, 90)


class TestStrongest(unittest.TestCase):
    def test_real_data_hp(self):
        self.assertEqual(strongest(REAL, "HP"), "Blissey", "wrong name for highest HP")

    def test_real_data_sp_atk(self):
        self.assertEqual(strongest(REAL, "Sp. Atk"), "MewtwoMega Mewtwo Y", "wrong name for highest Sp. Atk")

    def test_small_table(self):
        self.assertEqual(strongest(MINI, "Speed"), "Bolt", "wrong name for highest Speed")

    def test_works_on_any_column(self):
        self.assertEqual(strongest(MINI, "Attack"), "Pebble", "wrong name for highest Attack")


class TestCategoryReport(unittest.TestCase):
    def check(self, result, most_common, distinct):
        self.assertIsInstance(result, tuple, "should return a tuple")
        self.assertEqual(len(result), 2, "tuple should have 2 items")
        self.assertEqual(result[0], most_common, "most common value is wrong")
        self.assertEqual(result[1], distinct, "number of distinct values is wrong (blanks don't count)")

    def test_real_data_type_2(self):
        self.check(category_report(REAL, "Type 2"), "Flying", 18)

    def test_real_data_type_1(self):
        self.check(category_report(REAL, "Type 1"), "Water", 18)

    def test_small_table(self):
        self.check(category_report(MINI, "Type 1"), "Grass", 5)

    def test_blanks_are_not_counted(self):
        self.check(category_report(MINI, "Type 2"), "Flying", 2)


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch

def calculate_total(smoothies, reusable_cup):
    cost_per_smoothie = 3.50
    cup_cost = 1.00 if reusable_cup.lower() == 'yes' else 0.00
    return smoothies * cost_per_smoothie + cup_cost

class TestSmoothieCalculator(unittest.TestCase):

    def test_total_without_reusable_cup(self):
        self.assertEqual(calculate_total(2, 'no'), 7.00)

    def test_total_with_reusable_cup(self):
        self.assertEqual(calculate_total(2, 'yes'), 8.00)

    def test_zero_smoothies_with_cup(self):
        self.assertEqual(calculate_total(0, 'yes'), 1.00)

    def test_zero_smoothies_without_cup(self):
        self.assertEqual(calculate_total(0, 'no'), 0.00)

if __name__ == '__main__':
    unittest.main()

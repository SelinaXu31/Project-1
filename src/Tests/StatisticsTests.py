import unittest
from Statistics.Numbers import random_numbers
from Statistics.Statistics import Statistics


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)

    def test_mean(self):
        test_data = random_numbers(n)

        self.assertEqual(self.statistics.mean(test_data))
        self.assertEqual(self.statistics.result, )

    def test_median(self):
        test_data = random_numbers(n)

        self.assertEqual(self.statistics.median(test_data))
        self.assertEqual(self.statistics.result, )

    def test_mode(self):
        test_data = random_numbers(n)

        self.assertEqual(self.statistics.mode(test_data))
        self.assertEqual(self.statistics.result, )

    def test_std_dev(self):
        test_data = random_numbers(n)

        self.assertEqual(self.statistics.sandard_deviation(test_data))
        self.assertEqual(self.statistics.result, )

    def test_var(self):
        test_data = random_numbers(n)

        self.assertEqual(self.statistics.sandard_deviation(test_data))
        self.assertEqual(self.statistics.result, )

    def test_results_property(self):
        self.assertEqual(self.statistics.result, 0)


if __name__ == '__main__':
    unittest.main()
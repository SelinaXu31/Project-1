import unittest
from Statistics.Numbers import random_numbers


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean(self):
        test_data = random_numbers(n)

        self.assertEqual(self.statistics.result, )


if __name__ == '__main__':
    unittest.main()
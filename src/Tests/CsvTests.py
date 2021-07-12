import unittest
from CsvReader import CsvReader, ClassFactory
from pprint import pprint


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('Unit Test Addition.csv')
        self.csv_reader = CsvReader('Unit Test Division.csv')
        self.csv_reader = CsvReader('Unit Test Multiplication.csv')
        self.csv_reader = CsvReader('Unit Test Square.csv')
        self.csv_reader = CsvReader('Unit Test Square Root.csv')
        self.csv_reader = CsvReader('Unit Test Subtraction.csv')


if __name__ == '__main__':
    unittest.main()

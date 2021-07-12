import csv
import unittest
from Statistics.Statistics import Statistics
import Statistics.RandomNumbersGenerator
from Statistics.RandomNumbersGenerator import list_generator


class MyTestCase(unittest.TestCase):

    @staticmethod
    def CsvReader(filepath):
        data = []
        with open(filepath) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                data.append(row)
        return data

    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_results_property(self):
        self.assertEqual(self.statistics.result, 0)

    def test_mean(self):
        test_mean_data = MyTestCase.CsvReader('/Tests/Data/ut_numbers.csv')
        test_mean_answer = MyTestCase.CsvReader('/Tests/Data/ut_answers.csv')
        data = []
        for row in test_mean_data:
            data.append(float(row['Value']))
        for row in test_mean_answer:
            answer = float(row['Mean'])
            self.assertEqual(self.statistics.find_mean(data), answer)
            self.assertEqual(self.statistics.result, float(row['Mean']))

    def test_median(self):
        test_median_data = MyTestCase.CsvReader('/Tests/Data/ut_numbers.csv')
        test_median_answer = MyTestCase.CsvReader('/Tests/Data/ut_answers.csv')
        data = []
        for row in test_median_data:
            data.append(float(row['Value']))
        data_slice = data[0:100]
        for row in test_median_answer:
            answer = float(row['Median'])
            self.assertEqual(self.statistics.find_median(data_slice), answer)
            self.assertEqual(self.statistics.result, float(row['Median']))

    def test_mode(self):
        test_mode_data = MyTestCase.CsvReader('/Tests/Data/ut_mode.csv')
        test_mode_answer = MyTestCase.CsvReader('/Tests/Data/ut_answers.csv')
        data = []
        for row in test_mode_data:
            data.append(float(row['Value']))
        data_slice = data[0:11]
        for row in test_mode_answer:
            answer = float(row['Mode'])
            self.assertEqual(self.statistics.find_mode(data_slice), answer)
            self.assertEqual(self.statistics.result, float(row['Mode']))

    def test_variance(self):
        test_variance_data = MyTestCase.CsvReader('/Tests/Data/ut_numbers.csv')
        test_variance_answer = MyTestCase.CsvReader('/Tests/Data/ut_answers.csv')
        data = []
        for row in test_variance_data:
            data.append(float(row['Value']))
        data_slice = data[0:100]
        for row in test_variance_answer:
            answer = float(row['Variance'])
            self.assertEqual(self.statistics.find_var(data_slice), answer)
            self.assertEqual(self.statistics.result, float(row['Variance']))

    def test_standard_deviation(self):
        test_standard_deviation_data = MyTestCase.CsvReader('/Tests/Data/ut_numbers.csv')
        test_standard_deviation_answer = MyTestCase.CsvReader('/Tests/Data/ut_answers.csv')
        data = []
        for row in test_standard_deviation_data:
            data.append(float(row['Value']))
        data_slice = data[0:100]
        for row in test_standard_deviation_answer:
            answer = float(row['Standard_Deviation'])
            self.assertEqual(self.statistics.find_std_dev(data_slice), answer)
            self.assertEqual(self.statistics.result, float(row['Standard_Deviation']))
         
        
if __name__ == '__main__':
    unittest.main()

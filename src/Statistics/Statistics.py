from Calculator.Calculator import Calculator
from Statistics.Numbers import random_numbers
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.StandardDeviation import standard_deviation
from Statistics.Variance import variance


class Statistics(Calculator):
    result = 0

    def __init__(self):
        self.data = random_numbers(n)
        super().__init__()

    def mean(self, data):
        self.result = mean(self.data)
        return self.result

    def mode(self, data):
        self.result = mode(self.data)
        return self.result

    def median(self, data):
        self.result = standard_deviation(self.data)
        return self.result

    def std_dev(self, data):
        self.result = variance(self.data)
        return self.result
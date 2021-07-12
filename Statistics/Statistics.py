from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.StandardDeviation import standard_deviation
from Statistics.Variance import variance


class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def find_mean(self, data):
        self.result = mean(self.data)
        return self.result

    def find_mode(self, data):
        self.result = mode(self.data)
        return self.result

    def find_median(self, data):
        self.result = median(self.data)
        return self.result

    def find_std_dev(self, data):
        self.result = standard_deviation(self.data)
        return self.result

    def find_var(self, data):
        self.result = variance(self.data)
        return self.result

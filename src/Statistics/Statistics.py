from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from CsvReader.CsvReader import CsvReader

class Statistics(Calculator):
    data = []

    def __init__(self):
        self.data = CsvReader.CsvReader(filepath)
        super().__init__()

    def mean(self, data):
        self.result = mean(self.data)
        return self.result
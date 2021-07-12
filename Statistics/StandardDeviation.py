from Calculator.SquareRoot import squareroot
from Statistics.Variance import variance


def standard_deviation(data):
    var = variance(data)
    return squareroot(var)

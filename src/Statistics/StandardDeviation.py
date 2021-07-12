from Statistics.Numbers import random_numbers
from Calculator.Division import division
from Calculator.Subtraction import subtraction
from Statistics.Mean import mean


def standard_deviation(data, data_size, ddof=0):
    list_numbers = random_numbers(data, data_size)
    length = len(list_numbers)
    a = sum((x - mean) ** 2 for x in data)
    b = subtraction(length, ddof)
    r = division(b, a)
    return r
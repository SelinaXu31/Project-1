from Calculator.Division import division
from Statistics.Numbers import numbers


def variance(data, data_size, ddof=0):
    list_numbers = numbers(data, data_size)
    length = len(list_numbers)
    a = sum((x - mean) ** 2 for x in data)
    b = (length - ddof)
    r = division(b, a)
    return r
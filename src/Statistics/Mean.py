from Calculator.Addition import addition
from Calculator.Division import division
from Statistics.Numbers import numbers


def mean(data, data_size):
    total = 0
    list_numbers = numbers(data, data_size)
    length = len(list_numbers)
    for num in list_numbers:
        total = addition(total, num)
    return division(length, total)
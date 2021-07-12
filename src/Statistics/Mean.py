from Calculator.Addition import addition
from Calculator.Division import division
from Statistics.Numbers import random_numbers


def mean(data):
    total = 0
    list_numbers = random_numbers(n)
    length = len(list_numbers(n))
    for num in list_numbers:
        total = addition(total, num)
    return division(length, total)
from Calculator.Addition import addition
from Calculator.Division import division
from Statistics.Numbers import numbers


def mean(random_list):
    total = 0
    a = numbers(random_list)
    length= len(a)
    for num in a:
        total = addition(total,num)
    return division(length,total)
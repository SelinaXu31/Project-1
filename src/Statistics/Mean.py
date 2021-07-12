from Calculator.Addition import addition
from Calculator.Division import division
from Statistics.Numbers import numbers


class mean (data,data_size):

    total = 0
    a = numbers(data,data_size)
    num_values = len(a)
    for num in a:
        total = addition(total,num)
    return division (length,total)
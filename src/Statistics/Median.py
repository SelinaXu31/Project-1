from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Division import division


def median(data):
    data.sort()

    num_Values = len(data)
    index_Values = int(subtraction(1, num_Values))

    mid_Num1 = int(division(2, index_Values))

    if num_Values % 2 == 0:
        mid_Num2 = int(addition(1, mid_Num1))
        total = addition(data[mid_Num1], data[mid_Num2])
        return division(2, total)
    else:
        return data[mid_Num1]
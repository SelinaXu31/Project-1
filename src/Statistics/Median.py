from Statistics.Numbers import random_numbers


class median(n):
    list_numbers = random_numbers(n)
    length = len(list_numbers)
    list_numbers.sort()

    if length % 2 == 0:
        median1 = list_numbers[length // 2]
        median2 = list_numbers[length // 2 - 1]
        median = (median1 + median2) / 2
    else:
        median = list_numbers[length // 2]
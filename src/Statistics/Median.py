from Statistics.Numbers import numbers


class median(data, data_size):
    list_numbers = numbers(data, data_size)
    length = len(list_numbers)
    list_numbers.sort()

    if length % 2 == 0:
        median1 = list_numbers[length // 2]
        median2 = list_numbers[length // 2 - 1]
        median = (median1 + median2) / 2
    else:
        median = list_numbers[length // 2]
from Statistics.Numbers import numbers

class median(data, data_size):
    list_numbers = numbers(data, data_size)
    length = len(list_number)
    numbers.sort()

    if length % 2 == 0:
        median1 = numbers[length // 2]
        median2 = numbers[len(numbers) // 2 - 1]
        median = (median1 + median2) / 2
    else:
        median = numbers[length // 2]


 total = 0
    list_numbers = numbers(data,size)
    length = len(list)
    for num in list_numbers:
        total = addition(total, num)
    return division(length, total)